import requests

from src.services.request_mbta import get_stops
from src.models.user_options import UserOptions
from src.utilities.utils import build_options, get_selection
from src.models.single_option import SingleOption


def elicit_stops(route_id: str) -> SingleOption:
    """Ask the user to select a stop on the route they have previously selected

    Args:
        route_id (str): the train route the user previously selected

    Returns:
        SingleOption: The item the user selected
    """
    stops: requests.Response = get_stops(route_id)

    stop_options: UserOptions = build_options(stops)
    stop_selection: SingleOption = get_selection(stop_options)

    return stop_selection
