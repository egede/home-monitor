from framework.widget import widget
from guizero import Text


class text(widget):
    """Display a simple text message on the screen"""

    def __init__(self, app, geometry, updateinterval, text):
        super().__init__(geometry, updateinterval)
        self.text = text
        self._message = Text(app, text=self.text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        print('Setting text')
        self._text = text

    def update(self):
        self._message.text = self.text
