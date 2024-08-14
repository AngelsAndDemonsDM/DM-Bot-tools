import unittest

from DMBotTools import Coordinate, Shape


class TestShape(unittest.TestCase):
    def test_initialization(self):
        shape_str = "##\n##"
        shape = Shape(shape_str)
        self.assertEqual(shape._shape_str, shape_str, "Shape string was not initialized correctly.")
    
    def test_equality(self):
        shape_str1 = "##\n##"
        shape_str2 = "##\n##"
        shape1 = Shape(shape_str1)
        shape2 = Shape(shape_str2)
        shape3 = Shape("###\n#")
        
        self.assertEqual(shape1, shape2, "Shapes with the same string representation should be equal.")
        self.assertNotEqual(shape1, shape3, "Shapes with different string representations should not be equal.")
    
    def test_get_list_coordinates(self):
        shape_str = " #\n###"
        shape = Shape(shape_str)
        expected_coordinates = [
            Coordinate(0, 1), 
            Coordinate(1, 0), 
            Coordinate(1, 1), 
            Coordinate(1, 2)
        ]        
        coordinates = shape.get_list_coordinates()
        self.assertEqual(coordinates, expected_coordinates, "The coordinates list does not match the expected output.")

if __name__ == "__main__":
    unittest.main()
