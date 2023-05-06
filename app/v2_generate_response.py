import openai
import os
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
from preprocess import *

# -*- coding: utf-8 -*-

def generate_response(user_content, model_gpt="gpt-3.5-turbo"):

    # 발급받은 API 키 설정
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OPENAI_API_KEY = open(os.path.join(BASE_DIR, "token.txt"), 'r').readline()

    # openai API 키 인증
    openai.api_key = OPENAI_API_KEY
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # mall_db load
    mall_df = pd.read_csv("/Users/timdalxx/PROJECT/mall-talk-api/mall-talk-api/app/data/xmall_data_v2.5.csv")
    mall = create_pandas_dataframe_agent(llm=OpenAI(temperature=0.9), df=mall_df, verbose=True)
    
    return mall.run(user_content)

    

if __name__ == "__main__":
    print(generate_response("옷을 구매하기 좋은 장소 3곳 이름과 전화번호 알려줘."))
    