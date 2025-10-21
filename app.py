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

# Define scenarios and theoretical alignment (0 = EUT, 1 = PT)
scenarios = [
    ("Would you prefer to receive 500 or a 50% chance to win 1000?", 0),
    ("Would you prefer to lose 500 or take a 50% chance to lose 1000?", 1),
    ("Would you prefer a program that saves 200 people for sure or one with a 1/3 chance all 600 are saved and 2/3 chance none are saved?", 0),
    ("Would you sell a mug you own for 5 or buy the same mug for $5?", 1),
    ("Would you prefer a 1% chance to win 5000 or receive 50?", 1),
    ("Would you take a 50% chance to gain 100 and 50% chance to lose 100 or do nothing?", 0),
    ("You paid 100 for a concert ticket but feel sick. Would you still go or stay home?", 1),
    ("Would you prefer a 100% chance to win 300, or an 80% chance to win 400?", 0),
    ("Would you behave differently if you lost 10 cash vs. lost a 10 concert ticket?", 1),
    ("Would you prefer 100 today or 110 in one month?", 0),
]

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = []

st.title("Behavioral Bias Assessment")
st.write("Choose your preferred option for each scenario. Your responses will be analyzed to assess alignment with Expected Utility Theory (EUT) or Prospect Theory (PT).")

# Display scenarios
for i, (text, theory) in enumerate(scenarios):
    response = st.radio(f"{i+1}. {text}", ["Option A", "Option B"], key=f"q{i}")
    if response:
        st.session_state.responses.append(0 if response == "Option A" else 1)

# Submit button
if st.button("Submit Responses"):
    alignment = ["PT" if st.session_state.responses[i] == 1 else "EUT" for i in range(len(scenarios))]
    theory_labels = ["PT" if scenarios[i][1] == 1 else "EUT" for i in range(len(scenarios))]

    st.write("### Response Analysis")
    for i in range(len(scenarios)):
        bias = bias_map[i]
        user_theory = alignment[i]
        expected_theory = theory_labels[i]
        explanation = f"Scenario {i+1}: {bias} — You chose {user_theory}, which {'aligns with' if user_theory == expected_theory else 'deviates from'} the expected {expected_theory} behavior."
        st.write(explanation)

    # Summary table
    summary = {
        "Scenario": list(range(1, len(scenarios)+1)),
        "Bias": [bias_map[i] for i in range(len(scenarios))],
        "Your Choice": alignment,
        "Expected Theory": theory_labels
    }
    df_summary = pd.DataFrame(summary)
    st.write("### Summary Table")
    st.dataframe(df_summary)

    # Store results for class summary
    if 'class_data' not in st.session_state:
        st.session_state.class_data = []
    st.session_state.class_data.append({"Student": f"Student {len(st.session_state.class_data)+1}", **summary})

# Class summary table
if st.button("Show Class Summary"):
    if 'class_data' in st.session_state:
        df = pd.DataFrame(st.session_state.class_data)
        st.dataframe(df)
    else:
        st.write("No class data available yet.")
