
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.bootstrap.navs.vertical(["Active", "Link", "Link"], type="pills", active="Active")
rptObj.bootstrap.navs.tabs(["Active", "Link", "Link"], active="Active")
rptObj.bootstrap.navs.pills(["Active", "Link", "Link"], active="Active")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
