from src.models.single_option import SingleOption


class UserOptions:
    """
    A reusuable class for the collections of options the user will be picking from
    """

    @classmethod
    def make_option(cls, option: dict, index: int) -> SingleOption:
        """Turn the attributes of an item from the mbta API into a option to be selected

        Args:
            option (dict): a single entry from the `data` field returned by they mtba API
            index (int): the index of the item from the `data` field
        """
        id: str = option.get("id", "")
        attributes: dict = option.get("attributes", {})
        name: str = attributes.get("name", "")

        return SingleOption(id=id, name=name, index=index, option_node=option)

    def __init__(self, option_data: list):
        self.options = [
            self.make_option(option_data[i], i) for i in range(len(option_data))
        ]

    def __str__(self):
        return "\n".join([f"{i}" for i in self.options])
