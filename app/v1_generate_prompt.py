import pandas as pd

def generate_prompt(csv_path) -> list:

    prompts = [{
        'role': 'system',
        'content': '너는 지금부터, "OO몰 가이드"가 되어 내가 지금 부터 알려줄 입력을 기반으로 OO몰에 온 고객에게 답변해야해. 반드시 내가 알려준 정보와 일치할 때 답변해.'
    }]

    # db_path에서 층별 정보를 읽어 dictionary 에 저장
    mall_db = pd.read_csv(csv_path)
    mall_db = mall_db[['층','업종','이름','전화번호']]
    pre_floor = mall_db.iloc[0]['층']
    floor_info = ""
    num_cmd = 0

    for i in range(mall_db['이름'].count()):
        info = mall_db.loc[i]
        now_floor = info['층']
        if pre_floor != now_floor:
            if num_cmd == 2:
                break
            num_cmd += 1
            cmd = {}
            cmd['role'] = 'system'
            cmd['content'] = str(num_cmd)+'번째로 네가 기억해야 할 정보는 OO몰의 '+str(pre_floor)+'층 매장 정보야. csv 형태로 알려줄게.\
                각 열은 "층, 매장 업종, 매장 이름, 전화번호"를 의미해.\n' + floor_info
            prompts.append(cmd)
            floor_info = ""
        else:
            floor_info += info['층']+','+info['업종']+','+info['이름']+','+str(info['전화번호'])+'\n'
        
        pre_floor = now_floor

    
    
    return prompts

if __name__ == '__main__':
    generate_prompt("/Users/timdalxx/PROJECT/mall-talk-api/mall-talk-api/app/data/xmall_data_v2.5.csv")
    


    # [{
    #     'role': 'system',
    #     'content': '너는 지금부터, "OO몰 가이드"가 되어 내가 지금 부터 알려줄 입력을 기반으로 OO몰에 온 고객에게 답변해야해.'
    # },
    # {
    #     'role': 'system',
    #     'content': '첫 번째로 네가 기억해야 할 정보는 OO몰의 1층 매장 정보야. csv 형태로 알려줄게. \
    #         1F,홈퍼니싱,디프레소,031-5173-2119\
    #         1F,라이프스타일,라미,031-5173-1035\
    #         1F,레스토랑&카페,라브리크,\
    #         1F,패션의류,라운지 비,031-5173-1054\
    #         1F,패션의류,라코스테,031-5173-1037\
    #         1F,패션의류,랩,031-5173-1056\
    #         1F,뷰티,러쉬,031-5173-1050\
    #         1F,패션의류,럭키슈에뜨,031-5173-1021\
    #         1F,패션의류,르쿠어 에쿠어,\
    #         1F,레스토랑&카페,리피,031-5173-1486'
    # }]
