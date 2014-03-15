import unittest

def soft_assert(assert_function, param1, param2):
    try:
        assert_function(param1, param2)
    except AssertionError, e:
        print "hay error", e
#        archivo = open("log.txt", "a")
#        archivo.write("hay error" + str(e) + "\n")
#        archivo.close

class TestOperations(unittest.TestCase):

	def setUp(self):
		pass

	def test_add(self):
		a = 1
		b = 2
		result = a + b
		print str(result)
		self.assertEqual(2, a)
		self.assertEqual(1, result)

	def test_add2(self):
		a = 1
		b = 2
		result = a + b
		print str(result)
		soft_assert(self.assertEqual, 2, a)
		soft_assert(self.assertEqual, 1, result)

	def tearDown(self):
		pass

if __name__ == "__main__":
    unittest.main()