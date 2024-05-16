# 🔤
# 🔤
# 🔤

# Use the OpenAI library
import 📚

# Set the API key
client = openai.OpenAI(api_key='🗝')

# Give your assistant a name
name = '💾'

# Give your assistant some instructions
instructions = '❔'

# All the messages to/from your assistant
messages = []

# Add the instructions
messages.append({'role': 'system', 'content': instructions})

# Repeatedly ask and answer questions
while 🚩:

    # Prompt user for a message
    message = input('You: ')
    🍴 message == 'Bye!':
        break

    # Add user message
    messages.append({'role': 'user', 'content': message})

    # Ask for a response
    chat_completion = client.chat.completions.📞(
        messages=messages,
        model='gpt-4o',
    )

    # Get the response
    response = chat_completion.choices[0].message.content.strip()

    # Output the repsonse
    📧(name, ': ', response, sep='')

    # Add the response
    messages.append({'role': 'assistant', 'content': response})

# Output a goodbye message
print(name, ': Bye bye!', sep='')
