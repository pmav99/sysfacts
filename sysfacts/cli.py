import io
import json

import click
import ruamel.yaml  # type: ignore
from pygments import highlight, lexers, formatters  # type: ignore

from .api import collect_facts
from . import __version__

# https://yaml.readthedocs.io/en/latest/example.html#output-of-dump-as-a-string
class StringYAML(ruamel.yaml.YAML):
    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = io.StringIO()
        ruamel.yaml.YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


syaml = StringYAML(typ="safe", pure=True)


def colorize(string: str, lexer) -> str:
    colored = highlight(string, lexer, formatters.TerminalFormatter())
    return colored


@click.command()
@click.option("-p", "--pretty", is_flag=True, help="Pretty print json output")
@click.option("-y", "--yaml", is_flag=True, help="Return facts as yaml")
@click.option("--no-color", is_flag=True, help="Don't colorize output")
@click.version_option(version=__version__)
def main(no_color, pretty, yaml):
    """Gather facts about the system."""
    facts = collect_facts()
    if yaml:
        out = syaml.dump(facts)
        if not no_color:
            out = colorize(out, lexers.YamlLexer())
    else:
        if pretty:
            out = json.dumps(facts, indent=2)
            if not no_color:
                out = colorize(out, lexers.JsonLexer())
        else:
            out = json.dumps(facts)
    click.echo(out)
