import unittest

from unittest import mock
from framework.text import text
from framework.widget import widget


class WidgetTestCase(unittest.TestCase):

    def test_abstract(self):
        with self.assertRaises(TypeError):
            widget('8x4', 2)

    def test_text_instantiate(self):
        with mock.patch('framework.text.Text') as MockText:
            text('app', '8x4', 2, 'abc')
            MockText.assert_called_once()

    def test_text_getters(self):
        with mock.patch('framework.text.Text'):
            t = text('app', '8x4', 2, 'abc')
            assert(t.text == 'abc')
            assert(t.geometry == '8x4')
            assert(t.updateinterval == 2)

    def test_text_setters(self):
        with mock.patch('framework.text.Text'):
            t = text('app', '8x4', 2, 'abc')
            t.text = 'ABC'
            assert(t.text == 'ABC')
            t.geometry = '80x40'
            assert(t.geometry == '80x40')
            t.updateinterval = 3
            assert(t.updateinterval == 3)

    def test_text_display(self):
        with mock.patch('framework.text.Text'):
            t = text('app', '8x4', 2, 'abc')
            t.update()


if __name__ == '__main__':
    unittest.main()
