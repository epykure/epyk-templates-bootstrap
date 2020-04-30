"""
Common module for all the static data used in the different tests
"""

import os
import random
import json
import webbrowser

# Deduce the \outs folder based on this module path
# the \outs folder is excluded from Git
TESTS_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATHS = r"%s\outs" % TESTS_PATH
OUTPUT_PATHS_LOCALS_HTML = r"%s\outs\html" % TESTS_PATH
OUTPUT_TEMPS = r"C:\tmps"
OUT_FILENAME = 'report_example'

#
FAVICON_URL = r"https://raw.githubusercontent.com/epykure/epyk-materials-templates/master/static/images/logo.ico"
IMG_PATH = "https://raw.githubusercontent.com/epykure/epyk-ui/master/epyk/static/images"

