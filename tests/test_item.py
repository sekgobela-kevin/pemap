import unittest

from pemap import items as _items


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self.object = "age"
        self._value = 12
        self._value_callable = lambda: self._value
        self._item = _items.Item(self.object, self._value)
        self._item_callable = _items.Item(self.object, self._value_callable)
    
    def test_get_value(self):
        self.assertEqual(self._item.get_value(), self._value)
        self.assertEqual(self._item_callable.get_value(), self._value)

    def test_set_value(self):
        self._item.set_value(False)
        self.assertEqual(self._item.get_value(), False)

    def test_get_object(self):
        self.assertEqual(self._item.get_object(), self.object)


if __name__ == "__main__":
    unittest.main()
