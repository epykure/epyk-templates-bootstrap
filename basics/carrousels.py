
from epyk_bootstrap.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

tm = rptObj.bootstrap.dates.time()

rptObj.bootstrap.badge("Test")
rptObj.bootstrap.alert("A simple danger alert with ")

rptObj.bootstrap.breadcrumb(["Home", 'Library'], selected='Home')

for d in [12, 55, 85]:
  rptObj.bootstrap.progress(d)

rptObj.bootstrap.spinner()

rptObj.bootstrap.lists.horizontal(["A", "B", "C"])

rptObj.bootstrap.pagination([1, 2, 3, 4], selected=3, sizing='lg')


rptObj.bootstrap.carousels.controls(["https://www.imagdisplays.co.uk/wp-content/uploads/2019/04/HIllson-O2-Event-LED-Screen-1900x1066.jpg",
                                   "https://www.cesaretfelix.com/images/dossiers/2020-03/caniche-102122.jpg"])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
