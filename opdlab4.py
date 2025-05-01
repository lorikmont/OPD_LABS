import unittest
from opdlab3 import most_frequent

class TestMost_frequent(unittest.TestCase):
    def test_m_f(self):
        files = [['text.txt', 'и'], ['text1.txt', 'я'], ['text2.txt', 'не'], ['text3.txt', 'на']]
        for f in files:
            with open(f[0], 'r', encoding='utf8') as file:
                text = file.read()
                self.assertEqual(most_frequent(text), f[1])

if __name__ == '__main__':
    unittest.main()


