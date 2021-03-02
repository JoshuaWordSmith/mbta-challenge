import unittest
from unittest.mock import MagicMock, patch

from src.helpers.predictions import elicit_predictions


class MockRequest:
    def __init__(self, url: str) -> None:
        self.url = url

    def json(self):
        return {"data": [{"attributes": {"departure_time": self.url}}]}


def mock_get_prediction(route: str, stop: str, direction: str) -> MockRequest:
    return MockRequest(f"{route}/{stop}/{direction}")


class TestPredictions(unittest.TestCase):
    @patch("src.helpers.predictions.get_prediction")
    def test_elicit_predictions(self, get_prediction: MagicMock):
        route_id: str = "test_route"
        stop_id: str = "test_stop_id"
        direction_name: str = "test_direction"

        get_prediction.side_effect = mock_get_prediction

        prediction: str = elicit_predictions(
            route_id=route_id, stop_id=stop_id, direction_name=direction_name
        )

        assert prediction == f"{route_id}/{stop_id}/{direction_name}"


if __name__ == "__main__":
    unittest.main()
