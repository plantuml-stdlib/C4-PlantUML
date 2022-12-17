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
#   - "next_version"         (e.g. "v2.7.0") and
#   - "deployed_version" ... this is the next "plantuml(/plantuml-stdlib)" version
#                            which should be updated with this release (e.g. "V1.2023.2")
#   are defined as environment variable

# Supported transformations are
#
# - UpdateC4WithReleaseVersion
# - UpdateAllIncludes
# - UpdateAllImages
# - ReplaceREADMEHeader
# - UpdateC4WithNextBeta

import os
import re
import sys
import glob

import zlib
import base64
import string

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


def read_environment_variable(env_var):
    if env_var not in os.environ:
        sys.stderr.write(
            f"the required environment variable {env_var} is not defined\n"
        )
        sys.exit(3)
    return os.environ[env_var]


# It is assumed that "release_version", "next_version" and "deployed_version"
# are defined as environment variable
def read_environment_variables():
    global release_version
    release_version = read_environment_variable("release_version")
    if release_version[0] != "v":
        sys.stderr.write(
            f"release version {release_version} has to start with 'v' (and use a format like vX.Y.Z)"
        )
        sys.exit(2)
    global next_version
    next_version = read_environment_variable("next_version")
    global deployed_version
    deployed_version = read_environment_variable("deployed_version")


def replace_regex_in_file(file_path, search, replace):
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


def update_c4_release_version():
    # $c4Version is defined without starting 'v'
    print(
        f"updating C4Version() definition in C4.puml with new release_version {release_version[1:]} ..."
    )
    replace_regex_in_file(
        "C4.puml", '!\$c4Version  =  ".+"', f'!$c4Version  =  "{release_version[1:]}"'
    )
    print(f"C4Version() updated")


def update_c4_next_beta_version():
    # $c4Version is defined without starting 'v'
    print(
        f"updating C4Version() definition in C4.puml with new release_version {release_version[1:]} ..."
    )
    replace_regex_in_file(
        "C4.puml", '!\$c4Version  =  ".+"', f'!$c4Version  =  "{next_version[1:]}beta1"'
    )
    print(f"C4Version() updated")


def update_all_includes():
    # reference tag version is with starting 'v'
    print(f"updating include paths with new tag version {release_version} ...")
    files = glob.glob("./**/*", recursive=True)
    for file in files:
        if file.endswith(".puml") or file.endswith(".md"):
            print(f"    {file}")
            replace_in_file(
                file,
                "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/",
                f"!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/{release_version}/",
            )

    print(f"include paths updated")


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

    print(f"include paths in images updated")


def replace_readme_header():
    print(f"updating README.md with new version {release_version} and badges ...")
    # remove whole part before "# C4-PlantUML" in readme
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

    print(f"release README.md updated with new version and badges")


if len(sys.argv) != 2:
    u = "Usage: python ./.scripts/transform_files.py <transformation>\n"
    sys.stderr.write(u)
    sys.exit(1)

if sys.argv[0] != "./.scripts/transform_files.py":
    u = "script has to be started in repository root with relative path: ./.scripts/transform_files <transformation>\n"
    sys.stderr.write(u)
    sys.exit(1)

read_environment_variables()

if sys.argv[1] == "UpdateC4WithReleaseVersion":
    update_c4_release_version()
elif sys.argv[1] == "UpdateAllIncludes":
    update_all_includes()
elif sys.argv[1] == "UpdateAllImages":
    update_all_images()
elif sys.argv[1] == "ReplaceREADMEHeader":
    replace_readme_header()
elif sys.argv[1] == "UpdateC4WithNextBeta":
    update_c4_next_beta_version()
else:
    sys.stderr.write(f"{sys.argv[1]} is an unsupported transformation\n")
    sys.exit(1)
