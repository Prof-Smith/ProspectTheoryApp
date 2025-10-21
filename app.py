# Regenerate app.py with improved formatting for decision options
app_code = '''
import streamlit as st
import pandas as pd
import numpy as np

st.title("Prospect Theory Decision-Making Activity")
st.write("Please enter your choices and reflections for each decision round. After submission, the app will analyze your responses and provide feedback on rationality and behavioral biases.")

# Define decision rounds manually with improved formatting
rounds = [
    {"round": 1, "option_a": "80% chance to win $100, 20% chance to win $0", "option_b": "Guaranteed $75", "ev_a": 80, "ev_b": 75},
    {"round": 2, "option_a": "50% chance to win $200, 50% chance to lose $100", "option_b": "No change in wealth", "ev_a": 50, "ev_b": 0},
    {"round": 3, "option_a": "90% chance to win $100, 10% chance to win $0", "option_b": "Guaranteed $85", "ev_a": 90, "ev_b": 85},
    {"round": 4, "option_a": "10% chance to win $500, 90% chance to win $0", "option_b": "Guaranteed $40", "ev_a": 50, "ev_b": 40},
    {"round": 5, "option_a": "50% chance to lose $100, 50% chance to lose nothing", "option_b": "Guaranteed loss of $40", "ev_a": -50, "ev_b": -40}
]

# Create a form for student input
with st.form("student_input_form"):
    choices = []
    reflections = []
    for r in rounds:
        st.subheader(f"Round {r['round']}")
        st.markdown(f"**Option A**: {r['option_a']}")
        st.markdown(f"**Option B**: {r['option_b']}")
        choice = st.radio("Your choice:", ["Option A", "Option B"], key=f"choice_{r['round']}")
        reflection = st.text_area("Why did you choose this option?", key=f"reflection_{r['round']}")
        choices.append(choice)
        reflections.append(reflection)

    submitted = st.form_submit_button("Submit Responses")

if submitted:
    # Analyze choices
    biases = []
    deviations = []
    rational_choices = []

    for i, r in enumerate(rounds):
        chosen = choices[i]
        ev_a = r['ev_a']
        ev_b = r['ev_b']
        rational = "Option A" if ev_a > ev_b else "Option B"
        rational_choices.append(rational)
        deviation = abs((ev_a if chosen == "Option A" else ev_b) - (ev_a if rational == "Option A" else ev_b))
        deviations.append(deviation)

        # Bias detection
        if chosen != rational:
            if rational == "Option A" and chosen == "Option B":
                biases.append("Certainty Effect")
            elif rational == "Option B" and chosen == "Option A":
                biases.append("Loss Aversion or Probability Distortion")
            else:
                biases.append("Other Bias")
        else:
            biases.append("Rational")

    # Display results
    st.header("Your Results")
    results = pd.DataFrame({
        "Round": [r['round'] for r in rounds],
        "Your Choice": choices,
        "Rational Choice": rational_choices,
        "Bias Detected": biases,
        "Deviation from Rationality": deviations,
        "Reflection": reflections
    })
    st.dataframe(results)

    # Summary statistics
    total_deviation = sum(deviations)
    bias_counts = pd.Series(biases).value_counts()
    rationality_score = max(0, 100 - total_deviation)

    st.subheader("Summary Analysis")
    st.write(f"**Total Deviation from Rationality:** {total_deviation}")
    st.write(f"**Rationality Score (out of 100):** {rationality_score}")
    st.write("**Bias Summary:**")
    st.write(bias_counts)

    # Option to download results
    csv = results.to_csv(index=False).encode('utf-8')
    st.download_button("Download Your Results as CSV", data=csv, file_name="student_bias_analysis.csv", mime="text/csv")
'''

# Save to app.py
with open("app.py", "w") as f:
    f.write(app_code)

print("Regenerated app.py file with improved formatting has been saved.")
