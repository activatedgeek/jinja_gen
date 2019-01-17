# Jinja Generator

[![Build Status](https://travis-ci.com/activatedgeek/jinja-gen.svg?branch=master)](https://travis-ci.com/activatedgeek/jinja-gen)
[![PyPI version](https://badge.fury.io/py/jinja-gen.svg)](https://pypi.org/project/jinja-gen/)
![Project Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

## Installation

### From PyPI Repository

```shell
$ pip install jinja-gen
```

### From Source

```shell
$ pip install -U .
```

## Usage

```
usage: jinja-gen [-h] [-f] [-c] [-o] [--dry] [-k] [-d] [--debug] [--exec]
              [--no-dump]

Jinja Generator

optional arguments:
  -h, --help            show this help message and exit
  -f , --file           Path to the Jinja2 template file
  -c , --config         Path to the YAML configuration file, defaults to
                        <file_basename>.yaml
  -o , --output-dir     Output directory for generated files, defaults to
                        configuration file name
  --dry                 A dry run showing files to be generated
  -k , --output-name-key 
                        An extra key identifier populated for template with
                        name
  -d , --output-dir-key 
                        An extra key identifier populated for template with
                        output directory
  --debug               Enable debugging
  --exec                Enable executable file outputs
  --no-dump             Flag to disable a deterministic dump of the
                        configuration file
```

## Examples

See sample files in [examples](./examples) folder.

```
$ jinja-gen -f examples/sample.sh -c examples/sample.yaml
```

To enable executable file outputs,

```
$ jinja-gen -f examples/sample.sh -c examples/sample.yaml --exec
```

# License

MIT
