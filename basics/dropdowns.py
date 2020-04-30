
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.bootstrap.dropdowns.menu("menu", ["A", "b"])
rptObj.bootstrap.dropdowns.text(["A", "b"])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
