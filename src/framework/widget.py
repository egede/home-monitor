from abc import ABC, abstractmethod

class widget(ABC):
    """Base class for all widgets that should be able to display on the screen"""

    def __init__(self, geometry, updateinterval):
        self.geometry = geometry
        self.updateinterval = updateinterval
        super().__init__()

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        self._geometry = geometry

    @property
    def updateinterval(self):
        return self._updateinterval

    @updateinterval.setter
    def updateinterval(self, updateinterval):
        self._updateinterval = updateinterval

    @abstractmethod
    def update(self):
        pass
