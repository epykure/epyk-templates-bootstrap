
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

rptObj.bootstrap.inputs.button("value", "@")
rptObj.bootstrap.inputs.radio("value", True)
rptObj.bootstrap.inputs.checkbox("value", False)
rptObj.bootstrap.inputs.inputs(["value", "value2"], "Data")
rptObj.bootstrap.inputs.segment(["value", "value2"], "Data")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
