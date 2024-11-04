import os
import pyttsx3
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPEN_API_KEY'))
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed if necessary

# Function to get recipe response from OpenAI
def get_recipe_response(prompt):
    try:
        # Update to use `ChatCompletion` instead of `Completion`
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error getting response: {e}")
        return "I'm having trouble retrieving the recipe."

# Function to speak text out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function to handle recipe requests
def main():
    print("Recipe Assistant ready. Type 'exit' to quit.")
    while True:
        user_prompt = input("Enter the recipe you'd like: ")

        if user_prompt.lower() == "exit":
            print("Exiting Recipe Assistant.")
            break

        elif user_prompt:
            # Make a query for a recipe based on the user input
            prompt = f"Provide a recipe for {user_prompt}."
            recipe = get_recipe_response(prompt)

            # Output the recipe and read it aloud
            print("Recipe:", recipe)
            speak(recipe)
        else:
            print("No input provided. Please try again.")

if __name__ == "__main__":
    main()
