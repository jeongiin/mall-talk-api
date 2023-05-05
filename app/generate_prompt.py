import openai
import os
# -*- coding: utf-8 -*-

def generate_prompt(query, n):
    
    return query + "\n === \n" + "위 내용을 20글자 이내 문장 "+str(n)+"개로 넘버링해서 묘사해줘." 


def content_to_array(content):
    array = content.split('\n')
    return array


def generate_content(prompt, model_gpt="gpt-3.5-turbo"):

    # 발급받은 API 키 설정
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OPENAI_API_KEY = open(os.path.join(BASE_DIR, "token.txt"), 'r').readline()
    # openai API 키 인증
    openai.api_key = OPENAI_API_KEY

    # 메시지 설정하기
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model_gpt,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    
    return answer