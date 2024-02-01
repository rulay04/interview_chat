import openai

openai.api_key = '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'

# message list
def chatbot(user_input):
    messages = [
        {"role": "system", "content": """You are helping the user prepare for an interview. 
        Start by asking what type of role the user wants to interview for. You should provide 
        relevant questions for the user to answer, then offer advice based on that. Also, if 
        applicable, ask them to solve some coding problems in languages they are comfortable with. 
        Another option is for you to present the user with a chunk of code and ask them to explain 
        some of it. If you are asking multiple questions, add a new line character before each number. This means 
        you ask each question on its own line. Wait for their answer, give feedback, then move onto the next question.
        Progress into more and more difficult content over time please."""},
    ]

    messages.append(
        {"role": "user", "content": user_input}
    )

    chat = openai.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    
    reply_html = reply.replace('\n', '<br>')

    messages.append({"role": "assistant", "content": reply_html})
    return reply_html

