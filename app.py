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
    ("Would you prefer to receive $500 for sure, or take a 50% chance to win $1000?", 1),
    ("Would you prefer to lose $500 for sure, or take a 50% chance to lose $1000?", 1),
    ("Would you prefer a program that saves 200 people for sure, or one with a 1/3 chance all 600 are saved and 2/3 chance none are saved?", 1),
    ("Would you sell a mug you own for $5, or buy the same mug for $5?", 1),
    ("Would you prefer a 1% chance to win $5000, or receive $50 for sure?", 1),
    ("Would you take a 50% chance to gain $100 and 50% chance to lose $100, or do nothing?", 1),
    ("You paid $100 for a concert ticket but feel sick. Would you still go or stay home?", 1),
    ("Would you prefer a 100% chance to win $300, or an 80% chance to win $400?", 1),
    ("Would you behave differently if you lost $10 cash vs. lost a $10 concert ticket?", 1),
    ("Would you prefer $100 today or $110 in one month?", 1),
    ("Would you choose a known risk over an unknown risk with similar outcomes?", 1),
    ("Would you avoid a decision that might lead to future regret?", 1),
    ("Would you estimate a task will take less time than it usually does?", 1),
    ("Would you stick with a default option rather than actively choosing an alternative?", 1),
    ("Would you rate your ability or knowledge higher than average?", 1)
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
