from django.shortcuts import render
import openai
import os
from .models import GptResponse
from django.views.generic import ListView


def gpt_form(request):

    messages = [ {
        "role": "system", 
        "content": "Please provide the response in HTML format. Coding Lab Tutor is a specialized programming tutor, focusing on Python and Unity. It guides students, especially middle and high schoolers, in mastering Python for machine learning with scikit-learn, developing games using Pyxel, and creating web applications with Django. When working with Django, the GPT emphasizes setting up projects in a virtual environment using Pipenv, specifically with Django version 3.1.3. Additionally, it now includes guidance on deploying Django web applications using Python Anywhere, making it a preferred option for students to publish their web apps externally. The GPT continues to offer comprehensive assistance in game creation, web app development, and Unity 2022.3.11f1 mastery, adapting to student requests and covering a wide range of Python programming areas."
    }]
    if request.method == 'POST':
        gpt_output = request.POST.get('gpt_output')
        user_input = request.POST.get('user_input')

        if 'conversation' not in request.session:
            request.session['conversation'] = []
        conversation_history = request.session['conversation']

        client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])  # あなたのOpenAI APIキーを設定してください
        prompt = "\n".join(conversation_history + [f"User: {user_input}", "GPT:"])

        if user_input:
            messages.append( {"role": "user", "content": str(gpt_output)+user_input}, )
            chat = client.chat.completions.create(model="gpt-4", messages=messages)
        reply = chat.choices[0].message.content

        gpt_response = chat.choices[0].message.content

        conversation_history.extend([f"User: {user_input}", f"GPT: {gpt_response}"])
        request.session['conversation'] = conversation_history
        # 応答をデータベースに保存（任意）
        GptResponse.objects.create(user_input=user_input, gpt_response=gpt_response)

        return render(request, 'gpt_chat.html', {'conversation': conversation_history})

    return render(request, 'gpt_chat.html', {'conversation': []})


