#!/usr/bin/python

# If a new version is released, version number and other topics of the source
# has to be updated.
# This script simplifies the update from master to a specific release (branch/tag)

# IMPORTANT:
#
# - It is assumed that the script is stared in repository root with relative path
#   python ./.scripts/transform_files <transformation>
#
# - It is assumed that
#   - "release_version"      (e.g. "v2.6.0"),
#   - "next_version"         (e.g. "v2.7.0")
#                            If it is undefined it will be calculated via the release_version.
#                            It is the next patch (release patch!=0) or subversion (release patch==0).
#   - and "deployed_version" This is the next "plantuml(/plantuml-stdlib)" version
#                            which should be updated with this release (e.g. "V1.2023.2")
#                            If it is undefined it is calculated via the running PlantUML web service
#   are defined as environment variable (or they will be calculated if possible)

# Supported transformations/functions are
#
# - CalculateDeployedVersion
#
# - UpdateC4WithReleaseVersion
# - UpdateAllIncludes
# - UpdateAllImages
# - ReplaceREADMEHeader
# - UpdateC4WithNextBeta
#
# - CreatePlantUMLStdlibC4Folder [<plantuml-stdlib/C4 target folder>]

import os
import re
import sys
import glob

import zlib
import base64
import string

import requests

# >>>>> plant uml decoder from ryardley/plant_uml_decoder.py
# >>>>> https://gist.github.com/ryardley/64816f5097003a35f9726aab676920d0

plantuml_alphabet = (
    string.digits + string.ascii_uppercase + string.ascii_lowercase + "-_"
)
base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
b64_to_plantuml = bytes.maketrans(
    base64_alphabet.encode("utf-8"), plantuml_alphabet.encode("utf-8")
)
plantuml_to_b64 = bytes.maketrans(
    plantuml_alphabet.encode("utf-8"), base64_alphabet.encode("utf-8")
)


def plantuml_encode(plantuml_text):
    """zlib compress the plantuml text and encode it for the plantuml server"""
    zlibbed_str = zlib.compress(plantuml_text.encode("utf-8"))
    compressed_string = zlibbed_str[2:-4]
    return (
        base64.b64encode(compressed_string).translate(b64_to_plantuml).decode("utf-8")
    )


def plantuml_decode(plantuml_url):
    """decode plantuml encoded url back to plantuml text"""
    data = base64.b64decode(plantuml_url.translate(plantuml_to_b64).encode("utf-8"))
    dec = zlib.decompressobj()  # without check the crc.
    header = b"x\x9c"
    return dec.decompress(header + data).decode("utf-8")


# <<<<< plant uml decoder from ryardley/plant_uml_decoder.py


def read_environment_variable(env_var, is_required=True):
    if env_var not in os.environ:
        if is_required:
            sys.stderr.write(
                f"the required environment variable {env_var} is not defined\n"
            )
            sys.exit(3)
        else:
            return ""
    return os.environ[env_var]


# It is assumed that "release_version", "next_version" and "deployed_version"
# are defined as environment variable.
# If next_version is not defined then it is calculated based on release_version
# If deployed_version is not defined then it is calculated based on the running PlantUML web server
def read_environment_variables():
    global release_version
    release_version = read_environment_variable("release_version")
    if release_version[0] != "v":
        sys.stderr.write(
            f"release version {release_version} has to start with 'v' (and use a format like vX.Y.Z)"
        )
        sys.exit(2)
    release_match = re.search(
        r"^v(?P<v1>[0-9]+)\.(?P<v2>[0-9]+)\.(?P<v3>[0-9]+)$", release_version
    )
    if not release_match:
        sys.stderr.write(
            f"release version {release_version} has to use a format like v[0-9]+.[0-9]+.[0-9]+, e.g. v2.6.0)"
        )
        sys.exit(2)

    global next_version
    next_version = read_environment_variable("next_version", False)
    if next_version == "":
        v1 = int(release_match["v1"])
        v2 = int(release_match["v2"])
        v3 = int(release_match["v3"])
        next_version = calculate_next_version(release_version, v1, v2, v3)

    global deployed_version
    deployed_version = read_environment_variable("deployed_version", False)
    if deployed_version == "":
        deployed_version = read_next_plantuml_version()


def replace_first_regex_in_file(file_path, search, replace):
    r = re.compile(search)
    with open(file_path, "r") as file:
        filedata = file.read()
        filedata = r.sub(replace, filedata, 1)
    with open(file_path, "w") as file:
        file.write(filedata)


def replace_in_file(file_path, orig, replace):
    with open(file_path, "r") as file:
        filedata = file.read()
        filedata = filedata.replace(orig, replace)
    with open(file_path, "w") as file:
        file.write(filedata)


def replace_first_regex_copy_file(
    source_path, target_path, compiled_search_regex, replace
):
    with open(source_path, "r") as file:
        filedata = file.read()
    filedata = compiled_search_regex.sub(replace, filedata, 1)
    with open(target_path, "w") as file:
        file.write(filedata)


# Calculates the next version (inclusive starting v) based on the give version values.
# If v3 == 0 then v2 is increased otherwise v3
def calculate_next_version(release, v1, v2, v3):
    print(f"calculates the next_version based on given release_version {release} ...")
    if v3 == 0:
        v2 = v2 + 1
    else:
        v3 = v3 + 1
    version = f"v{v1}.{v2}.{v3}"
    print(
        f"The calculated next_version = {version}. It can be used as next_version environment variable with following statement"
    )
    print(f"    export next_version={version}")
    return version


# Calculates the next released PlantUML version that it can be used as deployed_version environment variable
# based on http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSf8JKn9BL9GBKijAixCpzFGv798pKi1oW00 response
# This function returns "V" + the parsed version number  (e.g. "V1.2022.16")
def read_next_plantuml_version():
    # the idea is that the PlantUML version is extracted out of the svg result of "header %version()".
    # %version() stores beta of next version.
    # the returned SVG response stores the version inclusive beta in a text element; e.fg. "...<text ...>1.2022.16beta2</text>..."
    # and this function returns "V" + the parsed version number  (e.g. "V1.2022.16")
    print(
        "calculates the next deployed_version based on the running PlantUML web server response ..."
    )
    resp = requests.get(
        "http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSf8JKn9BL9GBKijAixCpzFGv798pKi1oW00"
    )
    if resp.status_code != 200:
        sys.stderr.write(
            "cannot read the svg response (with the next release version) from the PlantUML web server; please check http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSf8JKn9BL9GBKijAixCpzFGv798pKi1oW00"
        )
        sys.exit(4)

    # As an alternative it could be calculated via https://www.planttext.com/api/plantuml/txt/SoWkIImgIIvApSz9vL8jIoqgpipFqz3aSaZDIu680W00
    # It would return "1.2022.15beta6\n". (details see https://forum.plantuml.net/17179/ascii-art-title-produces-java-lang-illegalstateexception?show=17184#a17184)

    svgbody = resp.content
    svg = svgbody.decode("utf-8")
    # this regex ignore beta2 of the text section too: "<text [^>]+>(?P<version>[0-9\.]+)"
    r = re.compile(r"<text [^>]+>(?P<version>[0-9\.]+)")
    v = r.search(svg)["version"]
    version = "V" + v

    print(
        f"The next PlantUML version = {version}. It can be used as deployed_version environment variable with following statement"
    )
    print(f"    export deployed_version={version}")

    return version


def update_c4_release_version():
    # $c4Version is defined without starting 'v'
    print(
        f"updating C4Version() definition in C4.puml with new release_version {release_version[1:]} ..."
    )
    replace_first_regex_in_file(
        "C4.puml", r'!\$c4Version  =  ".+"', f'!$c4Version  =  "{release_version[1:]}"'
    )
    print("C4Version() updated")


def update_c4_next_beta_version():
    # $c4Version is defined without starting 'v'
    print(
        f"updating C4Version() definition in C4.puml with new release_version {next_version[1:]} ..."
    )
    replace_first_regex_in_file(
        "C4.puml", r'!\$c4Version  =  ".+"', f'!$c4Version  =  "{next_version[1:]}beta1"'
    )
    print("C4Version() updated")


def update_all_includes():
    # reference tag version is with starting 'v'
    print(f"updating include/theme paths with new tag version {release_version} ...")
    files = glob.glob("./**/*", recursive=True)
    for file in files:
        if file.endswith(".puml") or file.endswith(".md"):
            print(f"    {file}")
            replace_in_file(
                file,
                "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/",
                f"!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/",
            )
            replace_in_file(
                file,
                "from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/",
                f"from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/",
            )
            replace_in_file(
                file,
                "](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/",
                f"](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/themes/",
            )
    print(f"include/theme paths updated")


def process_url_match(m: re.Match[str]):
    base = m.group("base")
    out_format = m.group("format")
    base64 = m.group("base64")
    text = plantuml_decode(base64)

    new_path = f"!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/"
    replaced = text.replace(
        "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/",
        new_path,
    )
    replaced = replaced.replace(
        "from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/",
        f"from https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/",
    )
    replaced = replaced.replace(
        "](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/themes/",
        f"](https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/themes/",
    )

    if new_path not in replaced:
        global found_not_replaced_include
        found_not_replaced_include = True
        print(
            f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\ninclude could not be replaced in base64\n{base64}\nthe extracted source is\n{text}\n------------------------------------"
        )
        updated_base64 = base64
    else:
        updated_base64 = plantuml_encode(replaced)

    return f"{base}/{out_format}/{updated_base64}"


def replace_images_in_file(file_path):
    # extract all base64 entries
    r = re.compile(
        "(?P<base>https://www\\.plantuml\\.com/plantuml)/(?P<format>(png|uml|svg))/(?P<base64>([^ )]*))"
    )
    with open(file_path, "r") as file:
        filedata = file.read()
        filedata = r.sub(process_url_match, filedata)
    with open(file_path, "w") as file:
        file.write(filedata)


def update_all_images():
    # reference tag version is with starting 'v'
    print(
        f"updating include paths with new tag version {release_version} in images of all *.md files ..."
    )

    global found_not_replaced_include
    found_not_replaced_include = False

    files = glob.glob("./**/*", recursive=True)
    for file in files:
        if file.endswith(".md"):
            print(f"    {file}")
            replace_images_in_file(file)

    if found_not_replaced_include:
        sys.stderr.write(
            "!!!!!! not all images urls could be updated in the *.md files (details see log)\n"
        )
        sys.exit(3)

    print("include paths in images updated")


def replace_readme_header():
    print(f"updating README.md with new version {release_version} and badges ...")
    # remove whole part before "# C4-PlantUML" in README.md
    r = re.compile(r"[^\#]+# C4-PlantUML", re.M)
    with open("README.md", "r") as file:
        filedata = file.read()
    filedata = r.sub("# C4-PlantUML", filedata)

    with open("./.scripts/readme_release_header.txt", "r") as header_file:
        header = header_file.read()
        header = header.replace("{release version}", release_version).replace(
            "{deploy into version}", deployed_version
        )

    filedata = filedata.replace("# C4-PlantUML", header)

    with open("README.md", "w") as file:
        file.write(filedata)

    print("release README.md updated with new version and badges")


def create_plantuml_stdlib_c4_folder(target_path):
    print(
        f"prepare C4 folder of plantuml-stdlib repository in folder {target_path} ..."
    )
    # remove whole begin inclusive "!endif" in the specific C4_*.puml files
    inclusive_endif = re.compile(r"'[^']+!endif", re.M)

    os.makedirs(target_path, exist_ok=True)
    replace_first_regex_copy_file(
        "C4.puml",
        os.path.join(target_path, "C4.puml"),
        re.compile("DOES NOT EXIST"),
        "DOES NOT EXIST",
    )
    replace_first_regex_copy_file(
        "C4_Component.puml",
        os.path.join(target_path, "C4_Component.puml"),
        inclusive_endif,
        "!include <C4/C4_Container>",
    )
    replace_first_regex_copy_file(
        "C4_Container.puml",
        os.path.join(target_path, "C4_Container.puml"),
        inclusive_endif,
        "!include <C4/C4_Context>",
    )
    replace_first_regex_copy_file(
        "C4_Context.puml",
        os.path.join(target_path, "C4_Context.puml"),
        inclusive_endif,
        "!include <C4/C4>",
    )
    replace_first_regex_copy_file(
        "C4_Deployment.puml",
        os.path.join(target_path, "C4_Deployment.puml"),
        inclusive_endif,
        "!include <C4/C4_Container>",
    )
    replace_first_regex_copy_file(
        "C4_Dynamic.puml",
        os.path.join(target_path, "C4_Dynamic.puml"),
        inclusive_endif,
        "!include <C4/C4_Component>",
    )
    replace_first_regex_copy_file(
        "C4_Sequence.puml",
        os.path.join(target_path, "C4_Sequence.puml"),
        inclusive_endif,
        "!include <C4/C4_Component>",
    )

    replace_first_regex_copy_file(
        "./.scripts/plantuml_stdlib_info.txt",
        os.path.join(target_path, "INFO"),
        re.compile(r"\{release version without v\}"),
        release_version[1:],
    )

    themes_path = target_path+"/themes"
    os.makedirs(themes_path, exist_ok=True)
    paths = glob.glob("./themes/puml-theme-C4_*.puml")
    for path in paths:
        file = os.path.basename(path)
        if file == "puml-theme-C4_FirstTest.puml":
            continue
        # print(f"    {path}")
        replace_first_regex_copy_file(
            path,
            os.path.join(themes_path, file),
            re.compile("DOES NOT EXIST"),
            "DOES NOT EXIST",
        )

    print(f"all C4 related plantuml-stdlib files copied into {target_path}.")


if not (
    len(sys.argv) == 2
    or (len(sys.argv) == 3 and sys.argv[1] == "CreatePlantUMLStdlibC4Folder")
):
    u = "Usage: python ./.scripts/transform_files.py <transformation>\n"
    sys.stderr.write("Usage: python ./.scripts/transform_files.py <transformation>\n")
    sys.exit(1)

if sys.argv[0] != "./.scripts/transform_files.py":
    u = "script has to be started in repository root with relative path: ./.scripts/transform_files <transformation>\n"
    sys.stderr.write(u)
    sys.exit(1)

if sys.argv[1] == "UpdateC4WithReleaseVersion":
    read_environment_variables()
    update_c4_release_version()
elif sys.argv[1] == "UpdateAllIncludes":
    read_environment_variables()
    update_all_includes()
elif sys.argv[1] == "UpdateAllImages":
    read_environment_variables()
    update_all_images()
elif sys.argv[1] == "ReplaceREADMEHeader":
    read_environment_variables()
    replace_readme_header()
elif sys.argv[1] == "UpdateC4WithNextBeta":
    read_environment_variables()
    update_c4_next_beta_version()
elif sys.argv[1] == "CalculateDeployedVersion":
    calculated_deployed_version = read_next_plantuml_version()
elif sys.argv[1] == "CreatePlantUMLStdlibC4Folder":
    read_environment_variables()
    if len(sys.argv) == 3:
        create_plantuml_stdlib_c4_folder(sys.argv[2])
    else:
        create_plantuml_stdlib_c4_folder(".plantuml_stdlib_c4")
else:
    sys.stderr.write(f"{sys.argv[1]} is an unsupported transformation\n")
    sys.exit(1)
