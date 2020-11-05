import unittest
from transliterator import transliterate

class SequenceTestCases(unittest.TestCase):
	def test_sequence(self):
		result = transliterate("ya 7mar")
		self.assertEqual(result, "يا حمار")
	def test_sequence_darija(self):
	    result = transliterate("nta 7aamed w m3e9ed")
	    self.assertEqual(result, "نت حامض و معقد")

if __name__ == '__main__':
	unittest.main()
