# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_daniel_module(cmd, daniel_module_name, location=None, tags=None):
    # Simulate creation logic; normally you'd call SDK or service client here
    result = {
        'name': daniel_module_name,
        'location': location,
        'tags': tags or {}
    }
    # Just returning the result dictionary as example
    return result


def list_daniel_module(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `daniel_module list`')


def update_daniel_module(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance