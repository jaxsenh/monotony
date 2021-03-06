from locations.location import Location
from objects.notifier import Notifier
from locations.actions.home import *


class Home(Location, Notifier):
    def __init__(self, player):
        Location.__init__(self, player)
        Notifier.__init__(self, "home")
        self.notify.debug("[__init__] Creating Home location")

        self.actions = [
            [
                WakeUp(self)
            ],
            [
                Eat(self)
            ]
        ]
