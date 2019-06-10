# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import tempfile
import shutil

from azure.cli.testsdk.preparers import AbstractPreparer


class WafScenarioMixin(object):
    profile = None

    def current_subscription(self):
        subs = self.cmd("az account show").get_output_in_json()
        return subs['id']
