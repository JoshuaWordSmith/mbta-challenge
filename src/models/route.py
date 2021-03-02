from src.models.user_options import UserOptions
from src.models.single_option import SingleOption


class RouteOptions(UserOptions):
    @classmethod
    def make_option(cls, route: dict, index: int) -> SingleOption:
        """The routes have a different attribute key for names, so the inherited method
        is overwritten

        Args:
            route (dict): the route as returned from the /routes api
            index (int): the index that will correspond to the user's selection

        Returns:
            SingleOption: a possible selection for the user to choose
        """
        id: str = route.get("id", "")
        attributes: dict = route.get("attributes", {})
        name: str = attributes.get("long_name", "")

        return SingleOption(id=id, name=name, index=index, option_node=route)
