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


class TimeseriesDataPoint(Model):
    """Defines a timeseries datapoint used in a timeseries.

    :param date_time_utc: The DateTime of the Timeseries data point in UTC
    :type date_time_utc: str
    :param value: The Value of the Timeseries data point
    :type value: float
    """

    _attribute_map = {
        'date_time_utc': {'key': 'dateTimeUTC', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'},
    }

    def __init__(self, *, date_time_utc: str=None, value: float=None, **kwargs) -> None:
        super(TimeseriesDataPoint, self).__init__(**kwargs)
        self.date_time_utc = date_time_utc
        self.value = value
