#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015, 2016, 2017 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Ssoftware Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from . import SMA
from . import AO


class AccelerationDecelerationOscillator(bt.Indicator):
    '''
    Acceleration/Deceleration Technical Indicator (AC) measures acceleration and
    deceleration of the current driving force. This indicator will change
    direction before any changes in the driving force, which, it its turn, will
    change its direction before the price.

    Formula:
     - MEDIAN PRICE = (HIGH + LOW) / 2
     - AO = SMA (MEDIAN PRICE, 5) - SMA (MEDIAN PRICE, 34)
     - AC = AO - SMA (AO, 5)

    See:
      - https://www.metatrader5.com/en/terminal/help/indicators/bw_indicators/ao
      - https://www.ifcmarkets.com/en/ntx-indicators/ntx-indicators-accelerator-decelerator-oscillator

    '''
    alias = ('AC', )
    lines = ('ac', )

    plotlines = dict(ac=dict(_method='bar'))

    def __init__(self):

        ao = AO()
        #self.l.ac = ao - SMA(ao, 5)
        self.l.ac = ao - SMA(ao, period=5)