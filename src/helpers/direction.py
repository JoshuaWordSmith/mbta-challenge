from typing import List, Union

from src.utilities.utils import get_selection
from src.models.single_option import SingleOption
from src.models.user_options import UserOptions


def get_direction_node(direction: str) -> dict:
    """Return a dictionary in the expected format that
    downstream functions will expect it

    Args:
        direction (str): the direction a train is traveling
    """
    return {"id": direction, "attributes": {"name": direction}}


def elicit_direction(route_selection: SingleOption) -> SingleOption:
    """Ask the user for the direction of travel they are inquiring about

    Args:
        route_selection (SingleOption): A single entry containing direction attributes,
        such as a response from the /routes endpoint

    Raises:
        ValueError: As the direction attributes are not explicit members of the
        `SingleOption` class, we manually validate them and raise if they are not
        present
    """
    option_attributes: dict = route_selection.option_node.get("attributes", {})
    directions: Union[List[str], None] = option_attributes.get("direction_names")

    if directions is None:
        raise ValueError("Selected option does not contain direction information")

    directions_list: list = [get_direction_node(direction) for direction in directions]
    direction_options: UserOptions = UserOptions(directions_list)
    direction_selection: SingleOption = get_selection(direction_options)
    return direction_selection
