import streamlit as st
import pandas as pd

# Define bias mapping
bias_map = {
    0: 'Risk Aversion in Gains',
    1: 'Risk Seeking in Losses',
    2: 'Framing Effect',
    3: 'Endowment Effect',
    4: 'Probability Weighting',
    5: 'Loss Aversion',
    6: 'Sunk Cost Fallacy',
    7: 'Certainty Effect',
    8: 'Mental Accounting',
    9: 'Temporal Discounting',
    10: 'Ambiguity Aversion',
    11: 'Regret Aversion',
    12: 'Planning Fallacy',
    13: 'Status Quo Bias',
    14: 'Overconfidence Bias'
}

# Define scenarios and correct answers (0 = EUT, 1 = PT)
scenarios = [
    ("Receive $500 for sure vs. 50% chance to win $1000", 1),
    ("Lose $500 for sure vs. 50% chance to lose $1000", 1),
    ("200 people will be saved vs. 400 people will die", 1),
    ("Sell mug vs. buy mug valuation", 1),
    ("1% chance to win $5000 vs. $50 for sure", 1),
    ("50% chance to gain $100, 50% chance to lose $100 vs. do nothing", 1),
    ("Go to concert despite being sick after paying $100", 1),
    ("100% chance to win $300 vs. 80% chance to win $400", 1),
    ("Lost $10 vs. lost $10 concert ticket", 1),
    ("$100 today vs. $110 in one month", 1),
    ("Choose known risk over unknown risk", 1),
    ("Avoid decision that may lead to regret", 1),
    ("Underestimate time to complete a task", 1),
    ("Stick with default option", 1),
    ("Overestimate ability or knowledge", 1)
]

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = []

st.title("Behavioral Bias Assessment")
st.write("Choose your preferred option for each scenario. Your responses will be analyzed to assess behavioral biases.")

# Display scenarios
for i, (text, correct) in enumerate(scenarios):
    response = st.radio(f"{i+1}. {text}", ["Option A", "Option B"], key=f"q{i}")
    if response:
        st.session_state.responses.append(1 if response == "Option A" else 0)

# Submit button
if st.button("Submit Responses"):
    scores = [int(st.session_state.responses[i] == scenarios[i][1]) for i in range(len(scenarios))]
    total_score = sum(scores)
    st.write(f"Total Bias Score: {total_score} / {len(scenarios)}")

    # Bias breakdown
    bias_breakdown = {bias_map[i]: ('Biased' if scores[i] == 1 else 'Rational') for i in range(len(scores))}
    st.write("Bias Breakdown:")
    for bias, result in bias_breakdown.items():
        st.write(f"- {bias}: {result}")

    # Store results for class summary
    if 'class_data' not in st.session_state:
        st.session_state.class_data = []
    st.session_state.class_data.append({"Student": f"Student {len(st.session_state.class_data)+1}", "Total Bias Score": total_score, **bias_breakdown})

# Class summary table
if st.button("Show Class Summary"):
    if 'class_data' in st.session_state:
        df = pd.DataFrame(st.session_state.class_data)
        st.dataframe(df)
    else:
        st.write("No class data available yet.")
