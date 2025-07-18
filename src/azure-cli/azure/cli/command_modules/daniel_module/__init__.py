# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azure.cli.command_modules.daniel_module._help import helps  # pylint: disable=unused-import


class Daniel_moduleCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.command_modules.daniel_module._client_factory import cf_daniel_module
        daniel_module_custom = CliCommandType(
            operations_tmpl='azure.cli.command_modules.daniel_module.custom#{}',
            client_factory=cf_daniel_module)
        super(Daniel_moduleCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=daniel_module_custom)

    def load_command_table(self, args):
        from azure.cli.command_modules.daniel_module.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.daniel_module._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = Daniel_moduleCommandsLoader
