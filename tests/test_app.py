import pytest
from dash.testing.application_runners import import_app


# fixture: run the dash app
@pytest.fixture
def app_runner(dash_duo):
    app = import_app("app")   # app.py file ko import karega
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(app_runner):
    dash_duo = app_runner
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Sales Dashboard" in header.text


def test_visualisation_present(app_runner):
    dash_duo = app_runner
    graph = dash_duo.find_element("div.js-plotly-plot")
    assert graph is not None


def test_region_picker_present(app_runner):
    dash_duo = app_runner
    dropdown = dash_duo.find_element("div.Select-control")
    assert dropdown is not None
