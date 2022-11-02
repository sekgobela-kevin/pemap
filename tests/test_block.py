import unittest

from pemap import block as _block
from pemap import items as _items


class TestBaseBlock(unittest.TestCase):
    _block_type = _block.BaseBlock

    def setUp(self) -> None:
        self._marry_item = _items.Item("Marry", 30)
        self._john_item = _items.Item("John", 10)
        self._ben_item = _items.Item("Ben", 30)
        self._ricky_item = _items.Item("Ricky", 40)

        self._items = [self._marry_item, self._john_item, 
            self._ricky_item, self._ben_item]
        self._sorted_items = sorted(self._items, key=lambda i: i.get_value())

        self._objects = [item.get_object() for item in self._items]
        self._sorted_objects = [item.get_object() for item in self._sorted_items]
        
        self._values = [item.get_value() for item in self._items]
        self._sorted_values = [item.get_value() for item in self._sorted_items]

        self._tuple = ((item.get_value(), item.get_object()) 
            for item in self._items)
        self._tuple  = tuple(self._tuple)
        self._sorted_tuple = tuple(sorted(self._tuple, key=lambda i:i[0]))
        
        self._block = self._block_type(self._items)

    def test_copy_items(self):
        for item in self._block.copy_items():
            self.assertNotIn(item, self._items)

    def test_get_items(self):
        self.assertCountEqual(self._block.get_items(), self._items)     
    
    def get_objects(self):
        self.assertCountEqual(self._block.get_objects(), self._objects)

    def test_extract_objects_from_items(self):
        objects = self._block_type.extract_objects_from_items(self._items)
        self.assertEqual(objects, self._objects)

    def test_sort_items_by_value(self):
        items = self._block_type.sort_items_by_value(self._items)
        self.assertEqual(items, self._sorted_items)

    def test_filter_items(self, key=None, limit=None):
        self.assertEqual(self._block.filter_items(), self._items)
        items = self._block.filter_items(limit=2)
        self.assertEqual(items, self._items[:2])
        items = self._block.filter_items(key=lambda i: i.get_value()==10)
        self.assertEqual(items, [self._john_item])


class TestBlock(TestBaseBlock):
    _block_type = _block.Block
    _block: _block.Block

    def test_get_items(self):
        items = self._block.get_items()
        self.assertEqual(items, self._items)

    def test_get_values(self):
        values = self._block.get_values()
        self.assertEqual(values, self._values)

    def test_get_items_by_value(self):
        items = self._block.get_items_by_value(10)
        self.assertEqual(items, self._sorted_items[:1])

    def test_get_item_by_value(self):
        item = self._block.get_item_by_value(10)
        self.assertEqual(item, self._john_item)

    def test_get_items_by_values(self):
        items = self._block.get_items_by_values([10])
        self.assertEqual(items, self._sorted_items[:1])

    def test_get_item_by_values(self):
        item = self._block.get_item_by_values([10])
        self.assertEqual(item, self._john_item)

    def test_get_items_by_type(self):
        items = self._block.get_items_by_type(str)
        self.assertEqual(items, self._items)

    def test_get_item_by_type(self):
        item = self._block.get_item_by_type(str)
        self.assertEqual(item, self._items[0])

    def test_to_tuple(self):
        self.assertEqual(self._block.to_tuple(), self._tuple)

    def test_to_dict(self):
        #self.assertDict(self._block.to_dict(), dict(self.tuple))
        pass

    def test_to_multi_dict(self):
        for value, objects in self._block.to_multi_dict().items():
            self.assertIn(value, self._values)
            self.assertTrue(set(objects).issubset(self._objects))


if __name__ == "__main__":
    unittest.main()