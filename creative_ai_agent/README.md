# Creative Project Idea Generator 💡

This Streamlit application helps users combine their diverse skills and interests into unique project ideas. It uses a **local, lightweight text generation technique** (powered by `markovify`) to suggest simple project starting points. No external API keys or internet connection (beyond initially loading the application) are required.

## 🎯 Core Concept

The agent takes 2 or more user-defined skills or interests and:
- Uses a predefined corpus and Markov chains to generate a related sentence.
- Combines this sentence with your skills into a simple project suggestion.
- Provides generic prompts for tools and learning outcomes.

**Note:** The ideas generated are simpler and less sophisticated than those from large AI models, but this tool runs entirely locally without needing API keys.

## 🛠️ Technical Stack
- **Text Generation**: `markovify` (local Markov chain generator)
- **Frontend**: Streamlit
- **Core Logic**: Python

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.7+

### 2. Setup
1.  **Clone the repository (or download the files):**
    ```bash
    # If this were a git repo:
    # git clone <repository_url>
    # cd creative_ai_agent
    ```
    Ensure you have the `creative_ai_agent` directory with `app.py`, `llm_integration.py`, and `requirements.txt`.

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Navigate to the `creative_ai_agent` directory in your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```
    This will install `streamlit` and `markovify`.

### 3. Running the Application
1.  Navigate to the `creative_ai_agent` directory in your terminal.
2.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
3.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 💡 Nature of Suggestions
- The project ideas are generated using Markov chains based on a small, built-in corpus of text.
- This means the suggestions are statistically generated and aim to provide a starting spark rather than a deeply analyzed plan.
- The "Tools" and "What you'll learn" sections provide generic, randomized suggestions to complement the core idea.

## 🔧 Future Extensions (Original Vision)
The original vision for this project included more advanced AI capabilities. If a suitable environment for larger models or APIs becomes available, future extensions could include:
- Integration with more powerful LLMs for higher-quality idea generation.
- Multi-step planning for project breakdown.
- Course recommenders.
- Personalized long-term memory.

---
Built by an AI Agent | Uses a local `markovify` generator.
