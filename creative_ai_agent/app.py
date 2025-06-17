import streamlit as st
# Import the local basic generator function
from llm_integration import get_creative_idea

# Set page config
st.set_page_config(page_title="Creative Project Idea Generator", layout="wide")

# --- Header ---
st.title("Creative Project Idea Generator 💡")
st.subheader("Turn your diverse skills into unique project ideas!")
st.markdown("""
Enter two (or three) of your skills or interests below.
This tool uses a local, lightweight text generation technique to suggest simple project ideas.
The suggestions are based on predefined patterns and may be less sophisticated than those from large AI models.
No API keys or internet connection (beyond loading this app) are needed to generate ideas!
""")

# --- User Input ---
st.markdown("### Your Skills & Interests")
col1, col2 = st.columns(2)
with col1:
    skill1 = st.text_input("Skill/Interest 1 (Required)", placeholder="e.g., Python, History")
with col2:
    skill2 = st.text_input("Skill/Interest 2 (Required)", placeholder="e.g., Music, Design")

skill3 = st.text_input("Skill/Interest 3 (Optional)", placeholder="e.g., Writing, Data")

submit_button = st.button("✨ Generate Simple Idea")

# --- Output Display ---
if submit_button:
    if skill1.strip() and skill2.strip(): # Basic validation
        st.markdown("---")
        st.subheader("🚀 Here's a Simple Project Idea:")

        project_title_placeholder = st.empty()
        project_description_placeholder = st.empty()
        tools_placeholder = st.empty()
        learn_placeholder = st.empty()
        difficulty_placeholder = st.empty()
        time_estimate_placeholder = st.empty()

        with st.spinner("🧠 Generating a simple idea locally..."):
            # Call the local generator function
            idea_data = get_creative_idea(skill1, skill2, skill3 if skill3.strip() else None)

        # The local generator is designed to always return data and not have "error" field for API issues
        # So, we can directly display the content.
        project_title_placeholder.markdown(f"### {idea_data.get('project_title', 'A Creative Idea')}")
        project_description_placeholder.info(f"{idea_data.get('project_description', 'Consider combining your skills in a new project.')}")

        st.markdown("#### Suggested Tools & Resources:")
        tools_placeholder.markdown(f"`{idea_data.get('tools', 'Basic tools like a text editor and a search engine.')}`")

        st.markdown("#### What You Might Explore:")
        learn_placeholder.success(f"{idea_data.get('learn', 'Exploring new connections between your interests.')}")

        col_details1, col_details2 = st.columns(2)
        with col_details1:
            st.markdown("##### Difficulty Level:")
            difficulty_placeholder.markdown(f"**{idea_data.get('difficulty', 'Adaptable')}**")
        with col_details2:
            st.markdown("##### Estimated Time to Complete:")
            time_estimate_placeholder.markdown(f"**{idea_data.get('time_estimate', 'Flexible')}**")

        st.success("🎉 Idea generated!")

    else:
        st.error("❗ Please enter at least two skills (Skill/Interest 1 and Skill/Interest 2) to generate an idea.")

# --- Footer ---
st.markdown("---")
st.markdown("Built by an AI Agent | Uses a local basic text generator.")
st.caption("Remember: These are simple starting points. Use your creativity to expand on them!")

# To run this app:
# 1. Ensure you have `streamlit` and `markovify` installed: pip install -r requirements.txt
# 2. Navigate to the `creative_ai_agent` directory in your terminal.
# 3. Run: streamlit run app.py
