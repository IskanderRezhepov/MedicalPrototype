import unittest
from unittest.mock import patch
from streamlit.testing.v1 import AppTest
from decision import DEFAULT_OPTIONS

class AppTests(unittest.TestCase):
    def test_render_and_decision(self):
        app = AppTest.from_file('app.py', default_timeout=30).run()
        self.assertFalse(app.exception)
        self.assertIn('Educational prototype only.', app.warning[0].value)
        app.text_area[0].set_value('Synthetic sore throat')
        app.checkbox[0].check()
        result = {'probabilities': dict(zip(DEFAULT_OPTIONS, [.1, .2, .6, .1])), 'confidence': .6}
        with patch('decision.decide', return_value=(result, result)):
            app.button[0].click().run()
        self.assertFalse(app.exception)
        self.assertIn('High likelihood', app.subheader[0].value)
        self.assertEqual(app.metric[0].value, '60.0%')

    def test_synthetic_confirmation(self):
        app = AppTest.from_file('app.py', default_timeout=30).run()
        app.button[0].click().run()
        self.assertIn('Confirm synthetic data', app.error[0].value)

if __name__ == '__main__':
    unittest.main()
