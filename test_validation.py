import unittest
from decision import validate_result, validate_options

class ValidationTests(unittest.TestCase):
    def test_normalization(self):
        result = validate_result({'probabilities': {'a': .2, 'b': .3}, 'confidence': .5}, ['a', 'b'])
        self.assertAlmostEqual(sum(result['probabilities'].values()), 1)
        self.assertAlmostEqual(result['probabilities']['a'], .4)

    def test_invalid_results(self):
        for values in ({'a': -1, 'b': 1}, {'a': 2, 'b': 0}, {'a': 0, 'b': 0}, {'a': float('nan'), 'b': 1}, {'a': True, 'b': 1}, {'a': 1}, {'a': 1, 'b': 0, 'extra': 0}):
            with self.subTest(values=values), self.assertRaises(ValueError):
                validate_result({'probabilities': values, 'confidence': .5}, ['a', 'b'])
        for confidence in (None, True, -1, float('inf')):
            with self.assertRaises(ValueError):
                validate_result({'probabilities': {'a': .5, 'b': .5}, 'confidence': confidence}, ['a', 'b'])

    def test_options(self):
        for options in (['a'], ['a', ' a '], ['', 'a']):
            with self.assertRaises(ValueError):
                validate_options(options)

if __name__ == '__main__':
    unittest.main()
