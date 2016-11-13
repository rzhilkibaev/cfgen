[![Build Status](https://travis-ci.org/rzhilkibaev/cfgen.png?branch=master)](https://travis-ci.org/rzhilkibaev/cfgen)

# cfgen
This tool allows you to generate a config file from a template and source configuration files. Variables in the source coingiguration files are evaluated every time the tool is executed which allows you to resolve them dynamically.

# Problem
You need to run a build tool `build` that requires a configuration file `build.cfg`.
```
[git]
branch = bug-111
```
Every time you switch between branches you need to modify this file. Not fun when you do it several times in a day.

# Solution
In this particular case you need to create `build.cfg.metaconfig`
```
current_branch = $(git rev-parse --abbrev-ref HEAD)
```
`build.cfg.template`
```
[git]
branch = {{ current_branch }}
```
Run `$ cfgen build.cfg`
The tool will evaluate contents of `build.cfg.metaconfig` and then write `build.cfg` using `build.cfg.template` as a template. These files can be commited into git so you need to create them only once.

# Installation
```
$ sudo pip install cfgen
$ sudo pip wheel cfgen
```
The fist command installs the python module, the seconde one installs `cfgen` script.

# Usage

`$ cfgen --help`
