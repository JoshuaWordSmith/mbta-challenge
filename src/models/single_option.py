from dataclasses import dataclass


@dataclass
class SingleOption:
    """
    A class to reuse for the choices the user makes between options
    """

    id: str
    name: str
    index: int
    option_node: dict

    def __str__(self):
        return f"{self.index}:\t{self.name}"
