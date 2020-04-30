
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

dt = rptObj.bootstrap.dates.cob()

dt.options.sideBySide = True
dt.options.daysOfWeekDisabled = [0, 6]

tm = rptObj.bootstrap.dates.time()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
