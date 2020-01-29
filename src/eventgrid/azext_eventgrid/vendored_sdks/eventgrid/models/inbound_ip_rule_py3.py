# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InboundIpRule(Model):
    """InboundIpRule.

    :param ip_mask: IP Address in CIDR notation e.g., 10.0.0.0/8.
    :type ip_mask: str
    :param action: Action to perform based on the match or no match of the
     IpMask. Possible values include: 'Allow'
    :type action: str or ~azext_eventgrid.models.IpActionType
    """

    _attribute_map = {
        'ip_mask': {'key': 'ipMask', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(self, *, ip_mask: str=None, action=None, **kwargs) -> None:
        super(InboundIpRule, self).__init__(**kwargs)
        self.ip_mask = ip_mask
        self.action = action
