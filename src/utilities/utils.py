import requests
import logging

from typing import List, Dict

from src.models.user_options import UserOptions
from src.models.single_option import SingleOption
from src.models.empty_option_exception import EmptyOptionException
from src.models.user_exit_exception import UserExitException

log: logging.Logger = logging.getLogger()

USER_PROMPT: str = "Select one of numbers to the left of the above options:\n"


def prompt_input(prompt: str = USER_PROMPT) -> str:
    """A simple wrapper for the input function so that it's easier to test

    Args:
        prompt (str): The prompt to show the user

    Returns:
        str: the value the user entered
    """
    return input(prompt)


def build_options(option_response: requests.Response) -> UserOptions:
    """Generic function for taking responses from the mbta API and turning them
    into printable lists

    Args:
        option_response (requests.Response): A response from the routes, stops,
        or predictions endpoints

    """
    options_dict: dict = option_response.json()

    options_data: List[Dict[str, str]] = options_dict.get("data", [])
    return UserOptions(options_data)


def get_selection(
    available_options: UserOptions, print_options: bool = True
) -> SingleOption:
    """Prompt the user to select from a printed list of options

    Args:
        available_options (UserOptions): The options the user is able to selects
        print_options (bool, optional): Whether or not all the options should be
            printed when the function is invoked. Defaults to True.

    Raises:
        EmptyOptionException: If there are no options available to select, we exit
        UserExitException: If the user types "exit", then we exit

    Returns:
        SingleOption: The option that the user selected
    """
    if len(available_options.options) == 0:
        log.error(
            "There seems to be an issue, and no options are available.\nPlease try other selections"
        )
        raise EmptyOptionException("no available options")

    if print_options:
        print(available_options)

    selection: str = prompt_input()

    if selection.casefold() == "exit":
        raise UserExitException(f"User input was {selection}")

    try:
        selected_index: int = int(selection)
        stop: SingleOption = available_options.options[selected_index]

        return stop
    except Exception as e:
        log.error(f"Invalid input: user input not found in above numeric options\n{e}")
        return get_selection(available_options, False)
