"""Optional real-Ollama interface smoke test, separate from the seven experiments."""
from streamlit.testing.v1 import AppTest
from run_experiments import CLASSIC

app = AppTest.from_file('app.py', default_timeout=260).run()
app.text_area[0].set_value(CLASSIC)
app.checkbox[0].check()
app.button[0].click().run()
assert not app.exception, str(app.exception)
assert not app.error, str(app.error)
assert app.subheader and app.metric and app.table
assert len(app.get('vega_lite_chart')) == 1, 'Expected probability chart'
print('PASS: actual Streamlit form -> local Ollama -> ranked table, confidence and bar chart')
print(app.subheader[0].value, app.metric[0].value)
