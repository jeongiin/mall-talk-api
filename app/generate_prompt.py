import openai
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS

from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import AnalyzeDocumentChain

from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
import pandas as pd

def csv_to_txt(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    return rows

# -*- coding: utf-8 -*-

def generate_content(user_content, model_gpt="gpt-3.5-turbo"):

    # 발급받은 API 키 설정
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OPENAI_API_KEY = open(os.path.join(BASE_DIR, "token.txt"), 'r').readline()

    # openai API 키 인증
    openai.api_key = OPENAI_API_KEY
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    # mall_db load
    mall_df = pd.read_csv("/Users/timdalxx/PROJECT/mall-talk-api/mall-talk-api/app/data/xmall_data_v2.5.csv")
    mall = create_pandas_dataframe_agent(llm=OpenAI(temperature=0.9), df=mall_df, verbose=True)
    
    mall.run("옷을 사고 밥을 먹기에 괜찮은 장소를 각각 2곳씩 추천해줘")

    exit()

    

# if __name__ == "__main__":
    