import gradio as gr
import openai
import os
from v1_generate_prompt import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OPENAI_API_KEY = open(os.path.join(BASE_DIR, "token.txt"), 'r').readline()
 
openai.api_key = OPENAI_API_KEY
 
def answer(state, state_chatbot, text):
    messages = state + [{
        'role': 'user',
        'content': text
    }]
 
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
 
    msg = res['choices'][0]['message']['content']
 
    new_state = [{
        'role': 'user',
        'content': text
    }, {
        'role': 'assistant',
        'content': msg
    }]
 
    state = state + new_state
    state_chatbot = state_chatbot + [(text, msg)]
 
    print(state)
 
    return state, state_chatbot, state_chatbot
 
 
with gr.Blocks(css='#chatbot .overflow-y-auto{height:750px}') as demo:
    state = gr.State(generate_prompt("app/data/xmall_data_v2.5.csv"))
    state_chatbot = gr.State([])
 
    with gr.Row():
        gr.HTML("""<div style="text-align: center; max-width: 500px; margin: 0 auto;">
            <div>
                <h1>Mall, Talk!📢</h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 120%">
                OO몰 가이드입니다! 무엇이든 물어봐주세요☺️
            </p>
            <p style="margin-bottom: 10px; font-size: 94%">
                Source Code 🔗 :  <a href="https://github.com/jeongiin/mall-talk-api.">Git Hub Link</a>
            </p>
            
        </div>""")
 
    with gr.Row():
        chatbot = gr.Chatbot(elem_id='OO몰 가이드✨')
 
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder='궁금하신 내용을 입력해주세요.').style(container=False)

 
    txt.submit(answer, [state, state_chatbot, txt], [state, state_chatbot, chatbot])
    txt.submit(lambda: '', None, txt)
 
demo.launch(debug=True, share=True)