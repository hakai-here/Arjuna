from modules.domain.vscan.sql import scan_sql_injection
from modules.domain.vscan.vuln import ClickJacking,HostHeader
from extra.for_inp import formaturl

def init_vulnscan(x):
    x = formaturl(x)
    ClickJacking(x)
    HostHeader(x)
    scan_sql_injection(str(formaturl(x)+"/"))