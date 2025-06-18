import streamlit as st
# Import the LLM integration function
from llm_integration import get_creative_idea

# Set page config for a more engaging title
st.set_page_config(page_title="Creative AI Project Generator", layout="wide")

# --- Header ---
st.title("Creative AI Project Generator 🎨🤖")
st.subheader("Turn your diverse skills into unique project ideas!")
st.markdown("""
Enter two (or three) of your skills or interests below, and let the AI craft a unique project proposal for you.
This app uses the Hugging Face Inference API to connect to a language model.
**Important:** You'll need a Hugging Face User Access Token. Please set it as an environment variable named `HF_TOKEN`.
You can get a token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
The free tier for the Inference API is subject to rate limits.
""")

# --- User Input ---
st.markdown("### Your Skills & Interests")
col1, col2 = st.columns(2)
with col1:
    skill1 = st.text_input("Skill/Interest 1 (Required)", placeholder="e.g., Machine Learning")
with col2:
    skill2 = st.text_input("Skill/Interest 2 (Required)", placeholder="e.g., Music Production")

skill3 = st.text_input("Skill/Interest 3 (Optional)", placeholder="e.g., Python, History, Psychology")

submit_button = st.button("✨ Generate Creative Idea")

# --- Output Display ---
if submit_button:
    if skill1.strip() and skill2.strip(): # Basic validation
        st.markdown("---")
        st.subheader("🚀 Your Creative Project Idea:")

        project_title_placeholder = st.empty()
        project_description_placeholder = st.empty()

        with st.spinner("🧠 AI is thinking... Connecting to Hugging Face Inference API... This might take a moment."):
            idea_data = get_creative_idea(skill1, skill2, skill3 if skill3.strip() else None)

        if "error" in idea_data:
            st.error(f"😕 Oh no! {idea_data['error']}")
        else:
            project_title_placeholder.markdown(f"### {idea_data.get('project_title', 'N/A')}")
            project_description_placeholder.info(f"{idea_data.get('project_description', 'No description provided.')}")

            st.markdown("#### Suggested Tools & Technologies:")
            st.markdown(f"`{idea_data.get('tools', 'Not specified.')}`")

            st.markdown("#### What You'll Learn:")
            st.success(f"{idea_data.get('learn', 'Not specified.')}")

            col_details1, col_details2 = st.columns(2)
            with col_details1:
                st.markdown("##### Difficulty Level:")
                st.markdown(f"**{idea_data.get('difficulty', 'Not specified.')}**")
            with col_details2:
                st.markdown("##### Estimated Time to Complete:")
                st.markdown(f"**{idea_data.get('time_estimate', 'Not specified.')}**")

            st.success("🎉 Idea generated successfully!")

    else:
        st.error("❗ Please enter at least two skills (Skill/Interest 1 and Skill/Interest 2) to generate an idea.")

# --- Footer ---
st.markdown("---")
st.markdown("Built by an AI Agent | Powered by Streamlit & Hugging Face Inference API")
st.caption("Remember: AI-generated ideas are a starting point. Research and adapt them to your specific goals!")

# To run this app:
# 1. Ensure you have `streamlit` and `huggingface_hub` installed: pip install -r requirements.txt
# 2. Make sure your HF_TOKEN environment variable is set (Hugging Face User Access Token).
# 3. Navigate to the `creative_ai_agent` directory in your terminal.
# 4. Run: streamlit run app.py
