
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

toast = rptObj.bootstrap.toast("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="Title")
card = rptObj.bootstrap.card("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="Title")

tm = rptObj.bootstrap.dates.time()
modal =rptObj.bootstrap.modals.actions("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="test", events=['validate', 'details'],
                                       options={"vertical-align": 'middle'}, sizing='xl')
modal = rptObj.bootstrap.modals.modal("Test Toast !!!!!!!!!!!!!!!!!!!!!!!!!!!", title="Title")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
