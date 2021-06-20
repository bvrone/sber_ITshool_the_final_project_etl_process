# -*- coding: utf8 -*-
import sqlite3
from datetime import datetime

from py_scripts import table_utils
from py_scripts import data_upload_utils
from py_scripts import project_constants as const
from py_scripts import init_tables
from py_scripts import daily_report as report

con = sqlite3.connect(const.DB_NAME)
cursor = con.cursor()
init_tables.init_schema(con)
init_tables.init_uploaded_data_tables(con)
init_tables.init_report_table(con)
upload_date = datetime.strftime(const.UPLOAD_DATE_START, "%d%m%Y")
data_upload_utils.upload_daily_data(upload_date, con)
report_date = datetime.strftime(const.UPLOAD_DATE_START, "%Y-%m-%d")
report.get_daily_report(con, report_date)
#table_utils.showTable(cursor, 'REP_FRAUD')
#table_utils.showTable(cursor, 'STG_TERMINALS')
#table_utils.showTable(cursor, 'terminals_tmp')
#table_utils.showTable(cursor, 'DWH_DIM_TERMINALS_HIST')
con.commit()
con.close()