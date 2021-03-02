import logging

from src.helpers.routes import elicit_routes
from src.helpers.direction import elicit_direction
from src.helpers.stops import elicit_stops
from src.helpers.predictions import elicit_predictions
from src.models.single_option import SingleOption
from src.models.empty_option_exception import EmptyOptionException

log: logging.Logger = logging.getLogger()

def main():
  try:
    print("Welcome! type exit at any time to quit\n")
    # Ask the user to select a train route
    route_selection: SingleOption = elicit_routes()
    route_id: str = route_selection.id

    # ask the user to select a stop along that route
    stop_selection: SingleOption = elicit_stops(route_id)
    stop_id: str = stop_selection.id

    # ask the user to select from the available route directions
    direction_selection: SingleOption = elicit_direction(route_selection)
    direction_name: str = direction_selection.name

    # retrieve the next departure time under those conditions
    prediction: SingleOption = elicit_predictions(route_id, stop_id, direction_name)
    print(f"\nFor the {route_selection.name} route, the next train going {direction_selection.name} from {stop_selection.name} station is departing at {prediction}")

    exit(0)
  except EmptyOptionException as e:
    log.error(f"Please try again later\n{e}")
    exit(1)
  except Exception as e:
    log.error(f"We ran into an issue:\n{e}")
    exit(1)

if __name__ == "__main__":
  main()
