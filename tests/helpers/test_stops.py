import unittest
from unittest.mock import MagicMock, patch
from models.single_option import SingleOption

from src.helpers.stops import elicit_stops


class MockRequest:
    def __init__(self, data: str) -> None:
        self.data = data

    def json(self):
        return {"data": [{"id": "test_id", "attributes": {"name": self.data}}]}


def mock_get_stop(route: str = "test_route") -> MockRequest:
    return MockRequest(route)


class TestStops(unittest.TestCase):
    @patch("src.helpers.stops.get_stops")
    @patch("src.utilities.utils.prompt_input")
    def test_elicit_stops(self, prompt_input: MagicMock, get_stops: MagicMock):
        prompt_input.side_effect = lambda x="0": x
        get_stops.side_effect = mock_get_stop

        stop: SingleOption = elicit_stops("stop_route_id")

        assert stop.name == "stop_route_id"


if __name__ == "__main__":
    unittest.main()
