import streamlit as st

# model = pickle.load(open('model.pkl', 'rb'))

def run():
    st.title("Brain Stroke Prediction using Machine Learning")

    gen_display = ('Female', 'Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    age = st.text_input('Age')

    ht_display = ('No', 'Yes')
    ht_options = list(range(len(ht_display)))
    ht = st.selectbox("Hypertension", ht_options, format_func=lambda x: ht_display[x])

    hd_display = ('No', 'Yes')
    hd_options = list(range(len(hd_display)))
    hd = st.selectbox("Heart Disease", hd_options, format_func=lambda x: hd_display[x])

    mar_display = ('No', 'Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    wt_display = ('Private', 'Self-employed', 'Government Job', 'Children')
    wt_options = list(range(len(wt_display)))
    wt = st.selectbox("Work Type", wt_options, format_func=lambda x: wt_display[x])

    rt_display = ('Urban', 'Rural')
    rt_options = list(range(len(rt_display)))
    rt = st.selectbox("Education", rt_options, format_func=lambda x: rt_display[x])

    avg_gl = st.text_input('Average Glucose Level')

    bmi = st.text_input('BMI')

    ss_display = ('Formerly smoked', 'Never smoked', 'Smokes', 'Unknown')
    ss_options = list(range(len(ss_display)))
    ss = st.selectbox("Employment Status", ss_options, format_func=lambda x: ss_display[x])

    submit_button = st.button('Submit')

run()
