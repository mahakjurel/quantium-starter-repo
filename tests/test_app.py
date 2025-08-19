import pytest
from dash.testing.application_runners import import_app
import os
import sys

# ✅ chromedriver path
CHROMEDRIVER_PATH = r"D:\chromedriver\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# ensure Python can see app.py in task3 folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../task3")))

@pytest.fixture
def app_runner(dash_duo):
    # explicitly set webdriver path
    os.environ["PATH"] += os.pathsep + os.path.dirname(CHROMEDRIVER_PATH)

    app = import_app("app")
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(app_runner):
    dash_duo = app_runner
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsels Sales Visualiser" in header.text

def test_visualisation_present(app_runner):
    dash_duo = app_runner
    graph = dash_duo.find_element("div.js-plotly-plot")
    assert graph is not None

def test_region_picker_present(app_runner):
    dash_duo = app_runner
    labels = [e.text for e in dash_duo.find_elements("label")]
    expected = ["North", "East", "South", "West", "All"]

    for region in expected:
        assert region in labels
