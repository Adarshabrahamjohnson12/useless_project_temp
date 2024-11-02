from together import Together

# Initialize the Together client
client = Together(api_key='e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41')

# Prompt templates
PROMPT_TEMPLATES = {
    '1': "Write a hilariously absurd excuse for why someone was late to work because of a pet raccoon.",
    '2': "Make up a funny excuse for missing an assignment involving aliens.",
    '3': "Write a ridiculous reason for forgetting an anniversary, preferably involving talking animals or time travel.",
    '4': "Give a silly excuse for not attending a friend's party because of a highly unusual reason.",
    '5': "Create a bizarre reason for avoiding household chores, involving imaginary creatures."
}

def generate_excuse(category):
    # Prepare message for the chat completion
    messages = [{"role": "user", "content": PROMPT_TEMPLATES[category]}]

    # Make request to Together API
    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=messages
    )

    # Debugging prints to inspect the response structure
    print("Choices:", completion.choices)
    print("First choice:", completion.choices[0])
    print("Message content:", completion.choices[0].message)

    # Parse response
    if completion and hasattr(completion, 'choices') and len(completion.choices) > 0:
        excuse = completion.choices[0].message.content.strip()
        return excuse

    return "No excuse generated. Please try again."

def main():
    print("Welcome to the Random Excuse Generator!")
    print("Choose a category:")
    print("1. Late to Work/School")
    print("2. Missed Assignment")
    print("3. Forgot an Anniversary")
    print("4. Avoiding a Friend's Party")
    print("5. Dodging Chores")

    choice = input("Enter the number corresponding to your choice (1-5): ")

    if choice in PROMPT_TEMPLATES:
        excuse = generate_excuse(choice)
        if excuse:
            print("\nGenerated Excuse:")
            print(excuse)
        else:
            print("Sorry, no excuse could be generated. Please try again.")

if __name__ == '__main__':
    main()
