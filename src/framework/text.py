from framework.widget import widget


class text(widget):
    """Display a simple text message on the screen"""

    def __init__(self, text, geometry, updateinterval):
        super().__init__(geometry, updateinterval)
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        print('Setting text')
        self._text = text

    def display(self, server):
        print(f'{self.text} at geometry {self.geometry} and upadate every {self.updateinterval} seconds.')
