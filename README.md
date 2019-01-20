# sysfacts

[![Build Status](https://travis-ci.com/pmav99/sysfacts.svg?branch=master)](https://travis-ci.com/pmav99/sysfacts)

`sysfacts` is a system information collector.

It can be used standalone or as a library.  In order to achieve its goals, `sysfacts`
tries to leverage existing cross-platform python libraries.

## Installation

### `pipx`

The recommended installation method is [pipx](https://github.com/cs01/pipx).  More
specifically, if you need to run `sysfacts` just once, you can do it from a *temporary*
virtual environment with:

``` shell
pipx run sysfacts
```

If you need to actually install `sysfacts` for your user you can do it with:

```
pipx install sysfacts
```

This command will create a virtual environment in `~/.local/pipx/venvs/sysfacts` and add
the `sysfacts` script in `~/.local/bin`.

### `pip`

Alternatively you can use good old `pip` but this is more fragile than

``` bash
pip install --user sysfacts
```

### As a dependency for another project

If you use [poetry](https://github.com/sdispater/poetry), you can use:

``` bash
poetry add sysfacts
```

## Usage

### Standalone

On standalone mode the output format can be either JSON or YAML. You can also choose
between a JSON data blob or pretty-printed and colored output.

``` shell
sysfacts --help
# JSON output
sysfacts
sysfacts --pretty
sysfacts --pretty --color
# YAML output
sysfacts --yaml
sysfacts --yaml --color
```

### API

The main function is `collect_facts()` which returns a python dictionary.

``` python
from sysfacts import collect_facts

facts = collect_facts()
```

## Alternative projects

Well, this is not really unique, since there are several similar projects out there

- puppet's [facter](https://github.com/puppetlabs/facter)
- chef's [ohai](https://github.com/chef/ohai) is written in ruby.
- datadog's [gohai]() is written in go.
- if you have ansible installed you can also use `ansible local -m setup`.
