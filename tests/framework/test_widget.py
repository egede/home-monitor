import unittest

from framework.text import text
from framework.widget import widget


class WidgetTestCase(unittest.TestCase):

    def test_abstract(self):
        with self.assertRaises(TypeError):
            widget('8x4', 2)

    def test_text_instantiate(self):
        text('8x4', 2, 'abc')

    def test_text_getters(self):
        t = text('8x4', 2, 'abc')
        assert(t.text == 'abc')
        assert(t.geometry == '8x4')
        assert(t.updateinterval == 2)

    def test_text_setters(self):
        t = text('8x4', 2, 'abc')
        t.text = 'ABC'
        assert(t.text == 'ABC')
        t.geometry = '80x40'
        assert(t.geometry == '80x40')
        t.updateinterval = 3
        assert(t.updateinterval == 3)

    def test_text_display(self):
        t = text('8x4', 2, 'abc')
        t.display('X')


if __name__ == '__main__':
    unittest.main()
