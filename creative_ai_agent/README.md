# Creative AI Project Generator 🎨🤖

This Streamlit application helps users combine their diverse skills and interests into unique project ideas, learning paths, or even career suggestions. It uses the Hugging Face Inference API to connect to a Large Language Model (currently configured for `TinyLlama/TinyLlama-1.1B-Chat-v1.0` or similar) to generate these creative outputs.

## 🎯 Core Concept

The agent takes 2 or more user-defined skills or interests and:
- Understands their context.
- Blends them creatively.
- Generates a meaningful output, such as a project idea, suggested tools/technologies, and learning outcomes.

## 🛠️ Technical Stack
- **Language Model Access**: Hugging Face Inference API
- **Default Model Used**: `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (or other compatible small instruction-tuned models)
- **Frontend**: Streamlit
- **Core Logic**: Python
- **API Client**: `huggingface_hub`

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.7+
- A Hugging Face User Access Token (API Key)

### 2. Setup
1.  **Clone the repository (or download the files):**
    ```bash
    # If this were a git repo:
    # git clone <repository_url>
    # cd creative_ai_agent
    ```
    For now, ensure you have the `creative_ai_agent` directory with `app.py`, `llm_integration.py`, and `requirements.txt`.

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
    This will install `streamlit` and `huggingface_hub`.

4.  **Set up your Hugging Face User Access Token:**
    This application requires a Hugging Face User Access Token to function with the Inference API.
    - You can generate a token from your Hugging Face account settings: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). A fine-grained token with "Read" access should be sufficient for inference.
    - You need to set this token as an environment variable named `HF_TOKEN`.

    **Linux/macOS:**
    ```bash
    export HF_TOKEN='your_hf_user_access_token_here'
    ```
    You can add this line to your shell's configuration file (e.g., `.bashrc`, `.zshrc`) for persistence.

    **Windows (Command Prompt):**
    ```bash
    set HF_TOKEN=your_hf_user_access_token_here
    ```
    **Windows (PowerShell):**
    ```bash
    $env:HF_TOKEN='your_hf_user_access_token_here'
    ```
    For persistent storage on Windows, search for "environment variables" in the system settings.

    **Important:** Do not hardcode your token directly into the Python scripts.

### 3. Running the Application
1.  Ensure your `HF_TOKEN` environment variable is set.
2.  Navigate to the `creative_ai_agent` directory in your terminal.
3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
4.  Open your web browser and go to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 📝 API Usage and Free Tier
- The Hugging Face Inference API provides a free tier for making calls.
- For basic free Hugging Face accounts, these free tier limits are generally quite small (e.g., a small amount of credits, "less than $0.10" per month was stated previously, but subject to change). Usage may be rate-limited or may consume these credits quickly.
- Users with a Hugging Face PRO subscription typically get more generous monthly credits for the Inference API.
- If the application shows errors related to rate limits or model loading, it might be due to these free tier constraints or the model being temporarily unavailable on the shared infrastructure.

## 💡 Future Extensions
As per the original issue, potential future extensions include:
- Multi-step planning for project breakdown.
- Course recommenders.
- Personalized long-term memory.
- Team generation suggestions.
- Image generation for visualizing ideas.

---
Built by an AI Agent.
