
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo


toast = rptObj.bootstrap.toast("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="Title")
card = rptObj.bootstrap.card("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="Title")

rptObj.bootstrap.button("favorite")
rptObj.bootstrap.buttons.checked("favorite")
rptObj.bootstrap.buttons.dropdown("buttons", ["A", "b"])
rptObj.bootstrap.dropdowns.buttons("dropdowns", ["A", "b"])

rptObj.bootstrap.badge("Test")
rptObj.bootstrap.alert("A simple danger alert with ")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
