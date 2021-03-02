import requests
import logging

from src.services.request_mbta import get_prediction
from src.models.empty_option_exception import EmptyOptionException

log: logging.Logger = logging.getLogger()


def elicit_predictions(route_id: str, stop_id: str, direction_name: str) -> str:
    """Use the user's input to retrieve the time the next train will leave their chosen station

    Args:
        route_id (str): the identifier of the route the user selected
        stop_id (str): the identifier of the station (stop) the user selected
        direction_name (str): the direction the departing train will be traveling

    Raises:
        EmptyOptionException: If the API is not able to find a next departing train based on the
        selections, it will raise an exception
    """
    predictions: requests.Response = get_prediction(route_id, stop_id, direction_name)
    prediction_data: dict = predictions.json().get("data", {})

    if len(prediction_data) == 0:
        log.error(
            f"There seems to be an issue, and no options are available.\n response code: {predictions.status_code}"
        )
        raise EmptyOptionException("no available options")

    next_departure: dict = prediction_data[0]
    departure_time: str = next_departure.get("attributes", {}).get("departure_time")

    return departure_time
