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
usage: jinja-gen [-h] -f  -c  [-o] [--dry] [-k] [-d] [--debug] [--no-dump]

Jinja Generator

optional arguments:
  -h, --help            show this help message and exit
  -f , --file           Path to the Jinja2 template file (default: None)
  -c , --config         Path to the YAML configuration file (default: None)
  -o , --output-dir     Output directory for generated files, defaults to
                        configuration file name (default: None)
  --dry                 A dry run showing files to be generated (default:
                        False)
  -k , --output-name-key 
                        An extra key identifier populated for template with
                        name (default: name)
  -d , --output-dir-key 
                        An extra key identifier populated for template with
                        output directory (default: dir)
  --debug               Enable debugging (default: False)
  --no-dump             Flag to disable a deterministic dump of the
                        configuration file (default: True)
```

## Examples

See sample files in [examples](./examples) folder.

```
$ jinja-gen -f examples/sample.sh -c examples/sample.yaml
```

# License

MIT
