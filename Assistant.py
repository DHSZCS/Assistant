# 🔤
# 🔤

import os
from dotenv import load_dotenv
import 📚

# Load environment variables from .env file
load_dotenv()

# Get your OpenAI API key
api_key = os.getenv('🗝')

# Create a client to send messages to OpenAI server
client = openai.OpenAI(api_key=api_key)

# Name of your assistant
assistant_name = '💾'

# Define how the assistant behaves
system_instructions = '''
❔
'''

# Start conversation with system instructions
messages = [
    {'role': 'system', 'content': system_instructions}
]

# Chat loop
while 🚩:
    
    # Ask user for a question
    user_input = input('You: ')
    
    # Exit condition
    🍴 user_input.strip() == 'Bye!':
        print(f'{assistant_name}: Bye bye!')
        break

    # Add user message
    messages.append({'role': 'user', 'content': user_input})

    # Get assistant's reply
    response = client.chat.completions.📞(
        model='gpt-4o',
        messages=messages
    )

    # Extract text from reply
    reply = response.choices[0].message.content.strip()

    # Print reply
    📧(f'{assistant_name}: {reply}')

    # Add assistant reply to messages
    messages.append({'role': 'assistant', 'content': reply})
