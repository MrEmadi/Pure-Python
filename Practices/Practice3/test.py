from unittest import TestCase
import app

class Evaluate(TestCase):

    def test_glass1(self):
        self.assertEqual(app.glass1, "juice",
                         "glass1 should be juice after switching!")

    def test_glass2(self):
        self.assertEqual(app.glass2, "milk",
                         "glass2 should be milk after switching!")
