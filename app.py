import streamlit as st
from decision import DEFAULT_OPTIONS, MODEL, decide, ranked

st.set_page_config(page_title='Synthetic infection decision', page_icon='🧪')
st.title('Synthetic infection decision')
st.warning('Educational prototype only. Not for clinical decision-making.')
st.write('How likely is a bacterial / strep infection based on a short synthetic patient description?')
st.caption('Synthetic data only. Never enter real patient information. All inference uses local Ollama.')
patient = st.text_area('Synthetic patient text', height=130)
option_text = st.text_area('Options — one per line', '\n'.join(DEFAULT_OPTIONS))
model = st.text_input('Installed Ollama model', MODEL)
confirmed = st.checkbox('I confirm this description is synthetic and contains no real patient information.')
if st.button('Run Decision', type='primary'):
    st.session_state.pop('result', None)
    if not confirmed:
        st.error('Confirm synthetic data before running.')
    else:
        try:
            with st.spinner('Running local model…'):
                result, raw = decide(patient, option_text.splitlines(), model)
            st.session_state['result'] = (result, raw)
        except Exception as exc:
            st.error(f'Decision failed: {exc}. Check that Ollama is running and the model is installed.')
if 'result' in st.session_state:
    result, raw = st.session_state['result']
    rows = ranked(result)
    winners = [k for k, v in rows if abs(v - rows[0][1]) < 1e-12]
    st.subheader('Top choice: ' + ' / '.join(winners))
    st.metric('Model-reported confidence', f"{result['confidence']:.1%}")
    st.caption('Uncalibrated model estimates. Confidence is self-reported, not measured accuracy. Results belong to the last successful run.')
    st.table([{'Rank': i + 1, 'Option': k, 'Probability': f'{v:.2%}'} for i, (k, v) in enumerate(rows)])
    st.bar_chart([{'Option': k, 'Probability (%)': v * 100} for k, v in rows], x='Option', y='Probability (%)', sort=False)
    st.write('Normalized JSON')
    st.json(result)
    with st.expander('Raw model JSON before normalization'):
        st.json(raw)
