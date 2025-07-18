# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.daniel_module._client_factory import cf_daniel_module


def load_command_table(self, _):

    # TODO: Add command type here
    # daniel_module_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#.{}',
    #    client_factory=cf_daniel_module)


    with self.command_group('daniel_module') as g:
        g.custom_command('create', 'create_daniel_module')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_daniel_module')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_daniel_module')


    with self.command_group('daniel_module', is_preview=True):
        pass


def create_daniel_module(cmd, client, name, location):
    # Your create logic here
    return f"Created {name} at {location}!"