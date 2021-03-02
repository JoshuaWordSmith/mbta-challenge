import unittest
from unittest.mock import MagicMock, patch
from models.single_option import SingleOption

from src.helpers.routes import elicit_routes


class MockRequest:
    def __init__(self, data: str) -> None:
        self.data = data

    def json(self):
        return {"data": [{"id": "test_id", "attributes": {"long_name": self.data}}]}


def mock_get_route(types: str = "test_types") -> MockRequest:
    return MockRequest(types)


class TestRoutes(unittest.TestCase):
    @patch("src.helpers.routes.get_routes")
    @patch("src.utilities.utils.prompt_input")
    def test_elicit_routes(self, prompt_input: MagicMock, get_routes: MagicMock):
        prompt_input.side_effect = lambda x="0": x
        get_routes.side_effect = mock_get_route

        route: SingleOption = elicit_routes()

        assert route.name == "test_types"


if __name__ == "__main__":
    unittest.main()
