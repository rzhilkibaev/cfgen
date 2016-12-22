[![Build Status](https://travis-ci.org/rzhilkibaev/cfgen.png?branch=master)](https://travis-ci.org/rzhilkibaev/cfgen)

# cfgen
This tool allows you to generate a config file from a template and source configuration files. Variables in the source configuration files are evaluated every time the tool is executed which allows you to resolve them dynamically using system shell.

# Problem
You need to run a build tool `build` that requires a configuration file `build.cfg`.
```
[git]
branch = bug-111
```
Every time you switch between branches you need to modify this file. Not fun when you do it several times in a day.

# Solution
In this particular case you need to create `cfgen.metaconfig`
```
current_branch = git rev-parse --abbrev-ref HEAD
```
`build.cfg.template`
```
[git]
branch = {{ current_branch }}
```
Run `$ cfgen build.cfg`
The tool will evaluate contents of `cfgen.metaconfig` executing `git rev-parse --abbrev-ref HEAD` in the system shell and then write `build.cfg` using `build.cfg.template` as a template. These files can be commited into git so you need to create them only once.

# Installation
```
$ sudo pip install cfgen
```
The fist command installs the python module, the seconde one installs `cfgen` script.

# Usage

`$ cfgen --help`

# Features
## cache
List variable names (one per line) you want to cache in `cfgen.caching`. They will be cached between executions in `.cfgen.cache`. Useful for variables that require user input but don't need to be evaluated for each execution.
## metaconfig file hierarchy
`cfgen` looks for metaconfig files starting from the root directory down to the current one. It merges content with last variable defenition winning. For instance if you run `cfgen build.cfg` from `/home/me/git/myproject` it will look for `cfgen.metaconfig` in `/home`, `/home/me`, `/home/me/git`, `/home/me/git/myproject` in that order. It will loadd and merge them all. While merging, the variables loaded later override the same variables loaded earlier. This allows you to set a global variable with some default value and override it in a subdirectory.
## template file hierarchy
Similarly a template file is looked for howerver only the last one is used.
## jinja2 templates
Template files are jinja2 templates
## context aware evaluation
The variables defined in metaconfig files can be used as environment variables in followng defenitions.
```
current_branch = git rev-parse --abbrev-ref HEAD
binary_name = echo "myapp_${current_branch}.jar"
```
## shell evaluation
Since variables are evaluated with system shell you can use all shell features. Here is an example of setting `aws_profile` variable from user input:
```
aws_profile = /bin/bash -c 'read -p "Enter AWS profile: " aws_profile && echo $aws_profile'
```
