import streamlit as st

st.title("Decision-Making Experiment")

# Round 1
st.header("Round 1")
st.write("**Option A:** You have an 80% chance to win $100 and a 20% chance to win $200.")
st.write("**Option B:** You receive a guaranteed $75.")
choice1 = st.radio("Your choice:", ["Option A", "Option B"], key="round1_choice")
reason1 = st.text_area("What was your reasoning for choosing this option?", key="round1_reason")

# Round 2
st.header("Round 2")
st.write("**Option A:** You have a 50% chance to win $200 and a 50% chance to win $100.")
st.write("**Option B:** You receive no change in wealth (i.e., guaranteed $0).")
choice2 = st.radio("Your choice:", ["Option A", "Option B"], key="round2_choice")
reason2 = st.text_area("Why did you prefer this option over the alternative?", key="round2_reason")

# Submit button
if st.button("Submit"):
    st.success("Thank you for your responses!")
    st.write("### Summary of Your Choices")
    st.write(f"**Round 1 Choice:** {choice1}")
    st.write(f"**Reason:** {reason1}")
    st.write(f"**Round 2 Choice:** {choice2}")
    st.write(f"**Reason:** {reason2}")
