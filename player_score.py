import unittest

class TestTruthy(unittest.TestCase):

  def test_true(self):
    value = False

    self.assertTrue(value)

if __name__ == '__main__':
  unittest.main()