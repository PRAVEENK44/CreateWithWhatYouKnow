from huggingface_hub import InferenceClient, HfHubHTTPError
import os
import json # For safely parsing potential JSON in LLM response, though less likely needed here

# --- Hugging Face Inference Client Initialization ---
HF_TOKEN = os.environ.get("HF_TOKEN")
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0" # Selected model

if not HF_TOKEN:
    print("Warning: HF_TOKEN environment variable not found. Hugging Face Inference API calls will fail.")
    # Application will likely fail later if this is the case, but we let it try.

def create_prompt_messages(skill1: str, skill2: str, skill3: str = None) -> list:
    """
    Creates a list of messages formatted for the Hugging Face Inference API's
    chat_completion endpoint, compatible with models like TinyLlama.
    """
    system_message = (
        "You are a highly creative AI assistant. Your task is to generate a unique and "
        "actionable project idea that combines the user-provided skills or interests. "
        "Please provide the output in a structured format as described by the user, "
        "using the exact labels: Project Title, Project Description, Suggested Tools/Technologies, "
        "What you'll learn, Difficulty Level, Time to Complete."
    )

    user_prompt_parts = [
        f"Skill 1: {skill1}",
        f"Skill 2: {skill2}"
    ]
    if skill3 and skill3.strip():
        user_prompt_parts.append(f"Skill 3: {skill3.strip()}")

    user_prompt_parts.extend([
        "\nPlease generate:",
        "1. Project Title: (A concise and creative title)",
        "2. Project Description: (1-2 sentences explaining the core idea)",
        "3. Suggested Tools/Technologies: (e.g., Python, specific libraries, hardware)",
        "4. What you'll learn: (Key skills or concepts gained)",
        "5. Difficulty Level: (e.g., Beginner, Intermediate, Advanced)",
        "6. Time to Complete: (e.g., 1-2 weeks, 1 month)",
        "\nExample:",
        "Project Title: AI Story Weaver",
        "Project Description: An AI that co-writes a story with a user, adapting to their input.",
        "Suggested Tools/Technologies: Python, Transformers, NLTK",
        "What you'll learn: NLP, prompt engineering, creative writing techniques",
        "Difficulty Level: Intermediate",
        "Time to Complete: 2-3 weeks"
    ])
    user_message = "\n".join(user_prompt_parts)

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    return messages

def get_creative_idea(skill1: str, skill2: str, skill3: str = None) -> dict:
    """
    Gets a creative project idea using the Hugging Face Inference API.
    Returns a dictionary with project details or an error message.
    """
    if not HF_TOKEN:
        return {"error": "Hugging Face API token (HF_TOKEN) is not configured. Please set the HF_TOKEN environment variable."}

    client = InferenceClient(model=MODEL_NAME, token=HF_TOKEN)
    messages = create_prompt_messages(skill1, skill2, skill3)

    try:
        response = client.chat_completion(
            messages=messages,
            max_tokens=500, # Max new tokens to generate
            temperature=0.7,
            top_p=0.95,
            # stream=False is default
        )

        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content.strip()
        else:
            return {"error": "Received an empty or invalid response from the Hugging Face Inference API."}

    except HfHubHTTPError as e:
        error_message = f"Hugging Face API error: {str(e)}"
        if e.response:
            error_message += f" (Status: {e.response.status_code}, Details: {e.response.text})"
        if "is currently loading" in str(e).lower() or (e.response and e.response.status_code == 503):
            error_message = f"The model ({MODEL_NAME}) is currently loading on Hugging Face Inference API. Please try again in a few moments."
        elif "Rate limit exceeded" in str(e) or (e.response and e.response.status_code == 429):
            error_message = "Hugging Face Inference API rate limit exceeded. Please try again later or check your plan."
        return {"error": error_message}
    except Exception as e:
        return {"error": f"An unexpected error occurred while contacting Hugging Face API: {str(e)}"}

    parsed_output = {}
    key_mapping = {
        "Project Title": "project_title",
        "Project Description": "project_description",
        "Suggested Tools/Technologies": "tools",
        "What you'll learn": "learn",
        "Difficulty Level": "difficulty",
        "Time to Complete": "time_estimate"
    }

    lines = content.split('\n')
    if not lines or (len(lines) == 1 and not any(key in lines[0] for key in key_mapping)):
        if len(content) < 200 and not any(key + ":" in content for key in key_mapping): # Heuristic
             return {"error": f"Model did not return a structured idea. Response: {content}"}

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        found_key = False
        for key_prompt, key_dict in key_mapping.items():
            if line_stripped.lower().startswith(key_prompt.lower() + ":"):
                value = line_stripped.split(":", 1)[1].strip()
                parsed_output[key_dict] = value
                found_key = True
                break
            elif line_stripped.lower().startswith(str(list(key_mapping.keys()).index(key_prompt) + 1) + ". " + key_prompt.lower() + ":"):
                value = line_stripped.split(":", 1)[1].strip()
                parsed_output[key_dict] = value
                found_key = True
                break

    expected_dict_keys = ["project_title", "project_description", "tools", "learn", "difficulty", "time_estimate"]
    for k in expected_dict_keys:
        if k not in parsed_output:
            parsed_output[k] = "Not specified by AI."

    if parsed_output.get("project_title", "Not specified by AI.") == "Not specified by AI.":
        parsed_output["project_description"] = f"AI response (parsing failed or incomplete): {content}"

    return parsed_output

if __name__ == '__main__':
    print("--- Testing Hugging Face Inference API Integration ---")
    if not HF_TOKEN:
        print("HF_TOKEN environment variable not set. Cannot run live tests.")
    else:
        print(f"Using model: {MODEL_NAME} via Hugging Face Inference API.")

        print("\nAttempting to get a creative idea for 'Python' and 'Music'...")
        idea1 = get_creative_idea("Python", "Music")
        if "error" in idea1:
            print(f"Error: {idea1['error']}")
            if "raw_content" in idea1:
                 print(f"Raw Content:\n{idea1['raw_content']}")
        else:
            print("\n--- Idea for Python & Music ---")
            for key, value in idea1.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

        print("\nAttempting to get a creative idea for 'Art', 'Biology', and 'Storytelling'...")
        idea2 = get_creative_idea("Art", "Biology", "Storytelling")
        if "error" in idea2:
            print(f"Error: {idea2['error']}")
            if "raw_content" in idea2:
                 print(f"Raw Content:\n{idea2['raw_content']}")
        else:
            print("\n--- Idea for Art, Biology & Storytelling ---")
            for key, value in idea2.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
