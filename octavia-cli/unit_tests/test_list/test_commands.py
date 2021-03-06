#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from click.testing import CliRunner
from octavia_cli.list import commands


def test_available_commands():
    assert commands.AVAILABLE_COMMANDS == [commands.connectors]


def test_commands_in_list_group():
    list_commands = commands._list.commands.values()
    for command in commands.AVAILABLE_COMMANDS:
        assert command in list_commands


def test_connectors_sources(mocker):
    mocker.patch.object(commands, "SourceConnectorsDefinitions", mocker.Mock(return_value="SourceConnectorsDefinitionsRepr"))
    context_object = {"API_CLIENT": mocker.Mock()}
    runner = CliRunner()
    result = runner.invoke((commands.sources), obj=context_object)
    commands.SourceConnectorsDefinitions.assert_called_with(context_object["API_CLIENT"])
    assert result.output == "SourceConnectorsDefinitionsRepr\n"


def test_connectors_destinations(mocker):
    mocker.patch.object(commands, "DestinationConnectorsDefinitions", mocker.Mock(return_value="DestinationConnectorsDefinitionsRepr"))
    context_object = {"API_CLIENT": mocker.Mock()}
    runner = CliRunner()
    result = runner.invoke((commands.destinations), obj=context_object)
    commands.DestinationConnectorsDefinitions.assert_called_with(context_object["API_CLIENT"])
    assert result.output == "DestinationConnectorsDefinitionsRepr\n"
