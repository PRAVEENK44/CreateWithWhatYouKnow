import markovify # For text generation
import random

# --- Predefined Corpus for Markovify ---
# This corpus should be diverse enough to generate somewhat varied sentences.
# It's kept relatively small to be embedded directly.
CORPUS = (
    "Consider developing a new application that blends technology with artistic expression. "
    "Explore how data analysis can reveal insights in creative fields. "
    "Build a small project to learn coding and share your musical ideas. "
    "Design an interactive experience that tells a story using psychological principles. "
    "A fun challenge is to combine your interest in biology with game development. "
    "You could create a tool to help visualize complex information for others. "
    "What if you made a learning roadmap for your unique skill set and shared it? "
    "Try to find a project that uses both your analytical and creative talents daily. "
    "Investigate the intersection of historical events and modern data representation. "
    "Develop a platform for community collaboration on art projects. "
    "Learn about machine learning by building a simple recommendation system. "
    "Create a digital narrative that adapts to user choices and skills. "
    "Study how environmental science can be communicated through interactive design. "
    "Build a personal website that showcases your combined abilities effectively. "
    "A great idea is to write a series of articles about the future of combined disciplines. "
    "How about making a short film that explains a scientific concept through art? "
    "Develop educational material that makes complex topics engaging and accessible. "
    "Start by sketching out a plan for a project that truly excites your passions. "
    "Think about how your unique skills can solve a real-world problem in a novel way. "
    "Perhaps you could design a workshop to teach others how to blend their own skills."
)

# Build the Markovify model from the corpus once when the module is loaded.
TEXT_MODEL = None
try:
    TEXT_MODEL = markovify.Text(CORPUS, state_size=2) # state_size=2 is default, good for small corpus
    print("Markovify model built successfully from predefined corpus.")
except Exception as e:
    print(f"Error building Markovify model: {e}. Text generation will be very basic.")
    TEXT_MODEL = None


def generate_markovify_sentence(max_chars=150, default_sentence="Consider exploring a new creative project."):
    """Generates a sentence using the Markovify model."""
    if TEXT_MODEL:
        try:
            sentence = TEXT_MODEL.make_short_sentence(max_chars, tries=100)
            if sentence:
                return sentence.strip()
        except Exception as e:
            print(f"Error generating sentence with Markovify: {e}")
    # Fallback if model failed or sentence generation didn't work
    return default_sentence


def get_creative_idea(skill1: str, skill2: str, skill3: str = None) -> dict:
    """
    Generates a basic project idea using Markovify and templates.
    Returns a dictionary with project details.
    """

    # 1. Generate a base sentence from Markovify
    markov_sentence = generate_markovify_sentence()

    # 2. Create a title and description using skills and the generated sentence
    skills_list = [skill1, skill2]
    if skill3 and skill3.strip():
        skills_list.append(skill3.strip())

    skills_string = ", ".join(skills_list[:-1]) + (f" and {skills_list[-1]}" if len(skills_list) > 1 else skills_list[0])

    project_title = f"Creative Fusion: {skills_string}"
    project_description = f"Considering your skills in {skills_string}, how about this: {markov_sentence}"

    # 3. Generic or very simply tailored suggestions for other fields
    tools_suggestions = [
        "your favorite search engine for research", "a notebook for ideas",
        "standard office software", "Python (if coding is involved)",
        "Canva or Figma (for design aspects)", "GitHub (for version control)"
    ]
    random.shuffle(tools_suggestions) # Add some slight variety
    tools = ", ".join(tools_suggestions[:3])

    learn_suggestions = [
        "how to blend different disciplines", "project planning and execution",
        "creative problem-solving", "researching new topics",
        "communicating your ideas", "adapting to new challenges"
    ]
    random.shuffle(learn_suggestions)
    learn = ", ".join(learn_suggestions[:3])

    difficulty_options = ["Beginner-friendly to start", "Scalable to your comfort level", "Adaptable difficulty"]
    time_estimate_options = ["Flexible: 1-2 weeks for a basic version", "Depends on your scope and depth", "A weekend to a month"]

    parsed_output = {
        "project_title": project_title,
        "project_description": project_description,
        "tools": tools,
        "learn": learn,
        "difficulty": random.choice(difficulty_options),
        "time_estimate": random.choice(time_estimate_options)
    }

    # This implementation does not have external API calls, so network errors are not expected.
    # It's designed to always return a dictionary.

    return parsed_output

if __name__ == '__main__':
    print("--- Testing Local Basic Generator ---")

    print("\nAttempting to get a creative idea for 'Python' and 'Music'...")
    idea1 = get_creative_idea("Python", "Music")
    for key, value in idea1.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\nAttempting to get a creative idea for 'Art', 'Biology', and 'Storytelling'...")
    idea2 = get_creative_idea("Art", "Biology", "Storytelling")
    for key, value in idea2.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\nAttempting to get a creative idea for 'Cooking' (single skill)...")
    idea3 = get_creative_idea("Cooking", "") # Test with one skill effectively
    for key, value in idea3.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
