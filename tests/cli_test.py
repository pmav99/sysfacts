import json

import click
import click.testing
import pytest

from sysfacts import cli


@pytest.fixture
def runner():
    runner = click.testing.CliRunner()
    return runner


class TestCLI(object):
    def test_help(self, runner):
        result = runner.invoke(cli.main, ["--help"])
        assert result.exit_code == 0
        assert result.output.startswith("Usage: ")

    def test_version(self, runner):
        result = runner.invoke(cli.main, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output

    def test_json_blob(self, runner):
        result = runner.invoke(cli.main, [])
        parsed = json.loads(result.output)
        assert result.exit_code == 0
        assert len(parsed) > 0
        assert "cpu_info" in parsed.keys()

    def test_json_pretty(self, runner):
        result = runner.invoke(cli.main, ["--pretty"])
        parsed = json.loads(result.output)
        assert result.exit_code == 0
        assert len(parsed) > 0
        assert "cpu_info" in parsed.keys()

    def test_json_pretty_no_color(self, runner):
        result = runner.invoke(cli.main, ["--pretty", "--no-color"])
        parsed = json.loads(result.output)
        assert result.exit_code == 0
        assert len(parsed) > 0
        assert "cpu_info" in parsed.keys()

    def test_yaml(self, runner):
        result = runner.invoke(cli.main, ["--yaml"])
        parsed = cli.syaml.load(result.output)
        assert result.exit_code == 0
        assert len(parsed) > 0
        assert "cpu_info" in parsed.keys()

    def test_yaml_no_color(self, runner):
        result = runner.invoke(cli.main, ["--yaml", "--no-color"])
        parsed = cli.syaml.load(result.output)
        assert result.exit_code == 0
        assert len(parsed) > 0
        assert "cpu_info" in parsed.keys()
