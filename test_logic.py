from main import parse_json, route_by_outcome

def test_parse_json_plain():
    assert parse_json('{"outcome": "resolved"}') == {"outcome": "resolved"}

def test_parse_json_strips_fences():
    fenced = '```json\n{"outcome": "callback"}\n```'
    assert parse_json(fenced) == {"outcome": "callback"}

def test_route_callback_goes_to_callback():
    assert route_by_outcome({"outcome": "callback"}) == "callback"

def test_route_resolved_goes_to_done():
    assert route_by_outcome({"outcome": "resolved"}) == "done"

def test_route_complaint_goes_to_done():
    assert route_by_outcome({"outcome": "complaint"}) == "done"