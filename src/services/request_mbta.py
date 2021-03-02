import os
import requests

from typing import Dict

BASE_URL: str = "https://api-v3.mbta.com"
X_API_KEY: str = os.getenv("MBTA_API_KEY", "")

MBTA_HEADERS: Dict[str, str] = {
    "accept": "application/vnd.api+json",
    "x-api-key": X_API_KEY,
}

def get_mbta_payload(request_url: str, headers: dict = MBTA_HEADERS) -> requests.Response:
    """Convenience method for sending get requests to the MBTA API

    Args:
        request_url (str): The url to query

    Returns:
        requests.Response: [description]
    """
    response: requests.Response = requests.get(request_url, headers=headers)
    response.raise_for_status()
    return response

def get_routes(types: str = "0,1") -> requests.Response:
    """Retrieve all available routes for given vehicle types

    Args:
        types (str, optional): Defaults to "0,1" which retrieves only heavy and light rail vehicles
    """
    request_url: str = f"{BASE_URL}/routes?filter[type]={types}"
    return get_mbta_payload(request_url=request_url)


def get_stops(route_id: str) -> requests.Response:
    """Retrieve all the stops (stations) along a given route

    Args:
        route_id (str): a specific train route to search along
    """
    request_url: str = f"{BASE_URL}/stops?filter[route]={route_id}"
    return get_mbta_payload(request_url=request_url)


def get_prediction(
    route_id: str, stop_id: str, direction_name: str
) -> requests.Response:
    """Retrieve a single prediction of when the next departure will be

    Args:
        route_id (str): The selected train route
        stop_id (str): the selected station
        direction_name (str): the selected direction of travel
    """
    request_url: str = f"{BASE_URL}/predictions?filter[route]={route_id}&filter[stop]={stop_id}&filter[direction_id]={direction_name}&sort=departure_time&page[limit]=1"
    return get_mbta_payload(request_url=request_url)
