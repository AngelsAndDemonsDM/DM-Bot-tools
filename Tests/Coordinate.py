import unittest

from DMBotTools import Coordinate


class TestCoordinate(unittest.TestCase):
    def test_initialization(self):
        coord = Coordinate(3, 4)
        self.assertEqual(coord.x, 3, "X coordinate not initialized correctly.")
        self.assertEqual(coord.y, 4, "Y coordinate not initialized correctly.")

    def test_addition(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(3, 4)
        result = coord1 + coord2
        self.assertEqual(result, Coordinate(4, 6), "Coordinate addition with another Coordinate failed.")
        
        result = coord1 + 5
        self.assertEqual(result, Coordinate(6, 7), "Coordinate addition with an integer failed.")

    def test_subtraction(self):
        coord1 = Coordinate(10, 10)
        coord2 = Coordinate(3, 4)
        result = coord1 - coord2
        self.assertEqual(result, Coordinate(7, 6), "Coordinate subtraction with another Coordinate failed.")
        
        result = coord1 - 5
        self.assertEqual(result, Coordinate(5, 5), "Coordinate subtraction with an integer failed.")

    def test_multiplication(self):
        coord = Coordinate(3, 4)
        result = coord * 2
        self.assertEqual(result, Coordinate(6, 8), "Coordinate multiplication by an integer failed.")

    def test_division(self):
        coord = Coordinate(10, 20)
        result = coord / 2
        self.assertEqual(result, Coordinate(5, 10), "Coordinate division by an integer failed.")
        
        with self.assertRaises(ZeroDivisionError):
            coord / 0

    def test_equality(self):
        coord1 = Coordinate(1, 1)
        coord2 = Coordinate(1, 1)
        coord3 = Coordinate(2, 2)
        
        self.assertTrue(coord1 == coord2, "Coordinates with the same values should be equal.")
        self.assertFalse(coord1 == coord3, "Coordinates with different values should not be equal.")

    def test_comparison(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(1, 3)
        coord3 = Coordinate(2, 2)
        
        self.assertTrue(coord1 < coord2, "Coordinate comparison (less than) failed.")
        self.assertTrue(coord2 > coord1, "Coordinate comparison (greater than) failed.")
        self.assertTrue(coord1 <= coord2, "Coordinate comparison (less than or equal to) failed.")
        self.assertTrue(coord1 >= coord1, "Coordinate comparison (greater than or equal to) failed.")
        self.assertFalse(coord3 < coord1, "Coordinate comparison (less than) failed.")
        self.assertFalse(coord1 > coord3, "Coordinate comparison (greater than) failed.")

    def test_hash(self):
        coord1 = Coordinate(1, 2)
        coord2 = Coordinate(1, 2)
        coord_set = {coord1}
        self.assertIn(coord2, coord_set, "Coordinates with the same values should have the same hash.")

    def test_repr(self):
        coord = Coordinate(1, 2)
        self.assertEqual(repr(coord), "Coordinate(x=1, y=2)", "String representation (repr) of Coordinate is incorrect.")

    def test_to_dict(self):
        coord = Coordinate(5, 6)
        self.assertEqual(coord.to_dict(), {'x': 5, 'y': 6}, "Coordinate to_dict conversion failed.")

    def test_from_dict(self):
        data = {'x': 5, 'y': 6}
        coord = Coordinate.from_dict(data)
        self.assertEqual(coord, Coordinate(5, 6), "Coordinate from_dict conversion failed.")

    def test_from_tuple(self):
        data = (7, 8)
        coord = Coordinate.from_tuple(data)
        self.assertEqual(coord, Coordinate(7, 8), "Coordinate from_tuple conversion failed.")

    def test_distance(self):
        coord1 = Coordinate(0, 0)
        coord2 = Coordinate(3, 4)
        self.assertEqual(Coordinate.distance(coord1, coord2), 5.0, "Distance calculation between coordinates is incorrect.")

    def test_iteration(self):
        coord = Coordinate(1, 2)
        self.assertEqual(list(coord), [1, 2], "Iteration over Coordinate failed.")

    def test_getitem(self):
        coord = Coordinate(3, 4)
        self.assertEqual(coord[0], 3, "Coordinate getitem (index 0) failed.")
        self.assertEqual(coord[1], 4, "Coordinate getitem (index 1) failed.")
        
        with self.assertRaises(IndexError):
            _ = coord[2]

    def test_setitem(self):
        coord = Coordinate(1, 2)
        coord[0] = 10
        coord[1] = 20
        self.assertEqual(coord.x, 10, "Coordinate setitem (index 0) failed.")
        self.assertEqual(coord.y, 20, "Coordinate setitem (index 1) failed.")
        
        with self.assertRaises(IndexError):
            coord[2] = 30

if __name__ == "__main__":
    unittest.main()
