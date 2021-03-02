import unittest
from unittest.mock import MagicMock, patch

from typing import Union, Dict
from src.helpers.direction import get_direction_node, elicit_direction
from src.models.single_option import SingleOption


class TestDirection(unittest.TestCase):
    def test_get_direction_node(self):
        """
        Simple functional test of the direction node
        """
        direction: str = "Outgoing"
        actual: Union[Dict[str, str], Dict[str, dict]] = get_direction_node(direction)

        assert actual["id"] == direction
        assert actual["attributes"]["name"] == direction

    def test_elicit_direction_value_error(self):
        route_selection: SingleOption = SingleOption(
            id="test_id", name="test_name", index=0, option_node={}
        )
        try:
            elicit_direction(route_selection)
        except ValueError as e:
            assert e
        else:
            assert False, "Route selection without directions did not raise an error"

    @patch("src.utilities.utils.prompt_input")
    def test_elicit_direction(self, prompt_input: MagicMock):
        prompt_input.side_effect = lambda x="0": x
        directions: list = ["North", "South"]

        option_node: dict = {"attributes": {"direction_names": directions}}
        route_selection: SingleOption = SingleOption(
            id="test_id", name="test_name", index=0, option_node=option_node
        )
        direction: SingleOption = elicit_direction(route_selection)

        assert direction.name == directions[0]


if __name__ == "__main__":
    unittest.main()
