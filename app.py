import streamlit as st
from hi import run_research

st.title("OpenAI Research Assistant")

# 1) Input Fields
user_query = st.text_area("Enter your research query/topic:")
iteration_limit = st.number_input(
    "Enter maximum number of iterations:",
    min_value=1,
    max_value=50,
    value=10
)

# 2) Run Button
if st.button("Run Research"):
    # 3) Perform research
    with st.spinner("Running research pipeline..."):
        final_report = run_research(user_query, iteration_limit)

    # 4) Display result
    st.markdown("### Final Report")
    st.markdown(final_report)
