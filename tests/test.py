# -*- coding: utf-8 -*-
from garbevents.custom_sensors_events import GetData

from garbevents.settings import Settings as ST

import pandas as pd

import openpyxl as xl
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import MergedCell


def parser_merged_cell(sheet: Worksheet, row, col):
    cell = sheet.cell(row=row, column=col)
    if isinstance(cell, MergedCell):
        for merged_range in sheet.merged_cells.ranges:
            if cell.coordinate in merged_range.coord:
                cell = sheet.cell(row=merged_range.min_row, column=merged_range.min_col)
                break
    return cell

