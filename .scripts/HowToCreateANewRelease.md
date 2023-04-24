# How to create a new release (WIP)

The idea is to
- create a new release in the "release/$release_version" branch (tagged with `$release_version` and `latest`)
- and a MR that the master branch can be updated with next beta version
- create in PlantUML/PlantUML-stdlib a MR with the released version

## 0. Preparation

The process requires following 3 versions:

- **$release_version**: version which should be created (e.g. `v2.6.0`)
- **$next_version**: version of the next beta which should be stared
  as soon the release is created (e.g. `v2.7.0`).  
  The master branch will be updated with a `beta1` of this version and C4Version() returns `2.7.0beta1`.  
  If it is unknown/undefined it is calculated via the release_version. It is the next patch (release patch!=0) or subversion (release patch==0).
- **$deployed_version**: this is the next "plantuml(/plantuml-stdlib)" version
  which should be updated with this release (e.g. "V1.2023.2")  
  If it is unknown/undefined it is calculated via the running PlantUML web service

### 0.0 Create a new issue with the title `Release $release_version` \(e.g. `Release v2.6.0`)

and a body like in https://github.com/plantuml-stdlib/C4-PlantUML/issues/248

### 0.1 Check that all open issues of the related `$release_version milestone` are fixed

### 0.2 Check that all other open changes are done

Update copyright year, contrib files, URLS, .... if required

### 0.* ...

### 0.x Check which is the next released version of the PlantUML(/PlantUML-stdlib)

it is used as $deployed_version and written in the released README.md  
If it is unknown it can be calculated via `CalculateDeployedVersion` (details see below)

## 1. create new release in branch `release/$release_version` (based on master)

Atm following steps are semi-automated and can be executed in a bash shell:

### 1.0. define the relevant versions as environment variabels and create the `release/$release_version` branch

\(in following sample the `release_version` = `v2.6.0`; `next_version` = `v2.7.0` and `deployed_version` = `V1.2022.15`)

```bash
export release_version=v2.6.0
export next_version=v2.7.0
export deployed_version=V1.2022.15
```

If the deployed_version is unknown it can be calculate via following (don't forget to set the environment variable after the call)

```bash
python ./.scripts/transform_files.py CalculateDeployedVersion
```

As soon all versions are defined the `release/$release_version` branch \(e.g. `release/v2.6.0`) can be created based on master branch

```bash
git pull
git checkout master
git branch release/$release_version
git checkout release/$release_version
```

### 1.1. Update `C4Version()` in C4.puml with the new release (e.g. `2.6.0`; without `v`)

```bash
python ./.scripts/transform_files.py UpdateC4WithReleaseVersion
```

### 1.2. Update all include paths and create a release version of the README.md

Following script calls

- Update all include paths with the release version tag based branch
- Update includes of all image urls with the release version tag based in *.md
  (after that images displays the correct C4Version() number and uses only the release-tag path in all includes)
- Update README.md with the new release header and title (based on the `readme_release_header.txt` template)

```bash
python ./.scripts/transform_files.py UpdateAllIncludes
python ./.scripts/transform_files.py UpdateAllImages
python ./.scripts/transform_files.py ReplaceREADMEHeader
```

These changes can/should be checked and if everything is ok it can be committed.

Following commit all changes and tag it locally with `$release_version` (e.g. `v2.5.0`) 

```bash
git checkout release/$release_version
git add -u *.md
git add -u *.puml
git add -u **/*.md
git add -u **/*.puml
git commit -m "Create release (branch) $release_version"
git tag "$release_version"
```

And if everything is ok it can be pushed too

```bash
git checkout release/$release_version
git push -u origin release/$release_version
```

## 2. Create `Release $release_version` \(e.g. `Release v2.6.0`) itself

This is done manually \(incl. an additional check...)

**Important:** As soon the release is finished check that 
- 'latest' tag is re-assigned to the new release branch
- and '$release_version' tag is assigned to the new release branch

As soon the version is released the release branch has to be write protected

## 3. Update master branch with $next_version beta1 version

### 3.1. create a `start-$next_version-beta1` branch \(e.g. `start-v2.7.0-beta1`) based on master branch

```bash
git pull
git checkout master
git branch start-$next_version-beta1
git checkout start-$next_version-beta1
```

Following script update `C4Version()` in C4.puml with the next beta release (e.g. `2.7.0beta1`; without `v`)

```bash
python ./.scripts/transform_files.py UpdateC4WithNextBeta
```

Following commit all changes

```bash
git checkout start-$next_version-beta1
git add -u C4.puml
git commit -m "Update version with first beta of $next_version ($release_version was created based on previous commit)"
```

And if everything is ok it can be pushed too

```bash
git checkout start-$next_version-beta1
git push -u origin start-$next_version-beta1
```

### 3.2. Create a MR into master

This is done manually \(incl. an additional check...)

## 4. Create in PlantUML/PlantUML-stdlib a MR based on `release/$release_version` branch

> !!! CHECK that the correct release branch is activated  !!!

> It is assumed that following calls are started in "C4-PlantUML repository" folder
(and not in the "plantuml-stdlib repository" folder)

The process requires following information too:

- **$deploy_repository_folder**: folder with the local `PlantUML/PlantUML-stdlib` git repositiory.  
  E.g. if it is parallel to the C4-PlantUML repository the it could be `../plantuml-stdlib`.

### 4.1. create in a PlantUML/PlantUML-stdlib fork a `C4$release_version` branch (e.g. `C4v2.6.0`)

```bash
export release_version=v2.6.0
export next_version=v2.7.0
export deployed_version=V1.2022.15

export deploy_repository_folder=../plantuml-stdlib

git pull
git checkout release/$release_version

git -C $deploy_repository_folder pull
git -C $deploy_repository_folder checkout master
git -C $deploy_repository_folder branch C4$release_version
git -C $deploy_repository_folder checkout C4$release_version
```

### 4.2. prepare the C4_*.puml and INFO file

```bash
python ./.scripts/transform_files.py CreatePlantUMLStdlibC4Folder $deploy_repository_folder/C4
```

### 4.3. Commit changes with comment "Update C4-PlantUML to $release_version"

```bash
git -C $deploy_repository_folder add -u C4/**
git -C $deploy_repository_folder commit -m "Update C4-PlantUML to $release_version"
```

### 4.4. create a MR "Update C4-PlantUML to $next_version"

This is done manually \(incl. an additional check...)
