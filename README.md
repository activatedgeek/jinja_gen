# Jinja Generator

[![Build Status](https://travis-ci.com/activatedgeek/jinja_gen.svg?branch=master)](https://travis-ci.com/activatedgeek/jinja_gen)
[![PyPI version](https://badge.fury.io/py/jinja_gen.svg)](https://pypi.org/project/jinja_gen/)
![Project Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

## Installation

### From PyPI Repository

```shell
$ pip install jinja_gen
```

### From Source

```shell
$ pip install -U .
```

## Usage

```
usage: jinja_gen [-h] -f  [-o] [--dry] [-k] [-d]

Jinja Generator

optional arguments:
  -h, --help            show this help message and exit
  -f , --file           Path to the YAML file containing all configurations
                        (default: None)
  -o , --output-dir     Output directory for generated configurations
                        (default: None)
  --dry                 A dry run showing files to be generated (default:
                        False)
  -k , --output-name-key 
                        An extra key identifier populated for template with
                        name (default: name)
  -d , --output-dir-key 
                        An extra key identifier populated for template with
                        output directory (default: dir)
```

## Examples

See sample files in [examples](./examples) folder.

# License

MIT
