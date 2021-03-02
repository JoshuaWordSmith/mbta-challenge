import requests
from typing import List, Dict

from src.services.request_mbta import get_routes
from src.models.route import RouteOptions
from src.utilities.utils import get_selection
from src.models.single_option import SingleOption


def build_routes() -> RouteOptions:
    """Retrieve and assemble the routes that can be selected

    Returns:
        RouteOptions: The available train routes
    """
    routes: requests.Response = get_routes()
    routes_dict: dict = routes.json()

    route_data: List[Dict[str, str]] = routes_dict.get("data", [])
    return RouteOptions(route_data)


def elicit_routes() -> SingleOption:
    """Ask the user to select from a provided list of train routes

    Returns:
        SingleOption: the selection made by the user
    """
    route_options: RouteOptions = build_routes()
    route_selection: SingleOption = get_selection(route_options)
    return route_selection
