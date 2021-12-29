import pandas as pd
import numpy as np
import json

#데이터의 경로에 따라서 json데이터를 가져오는 함수
def json_loader(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        contents = f.read()
        json_data = json.loads(contents)

    return json_data

#json_data를 받으면 pandas 데이터 프레임으로 바꿔주는 함수
def json_parser_to_pd(json_data):

    actor_list = []
    object_list = []
    verb_list = []
    timestamp_list = []

    for i, xapi in enumerate(json_data):

        #object에 있는 결측치를 대체함
        if xapi['object'] == {}:
            json_data[i]['object'] = {'definition': {'name': {'ko-KR': 'none'}}}
        
        actor_var = xapi['actor']['name']
        object_var = xapi['object']['definition']['name']['ko-KR']
        verb_var = xapi['verb']['display']['ko-KR']
        timestamp_var = xapi['timestamp']

        actor_list.append(actor_var)
        object_list.append(object_var)
        verb_list.append(verb_var)
        timestamp_list.append(timestamp_var)

    df_data = pd.DataFrame(
        {
            'actor' : actor_list,
            'object' : object_list,
            'verb' : verb_list,
            'timestamp' : timestamp_list
        }
    )

    print('결측치 확인: ', df_data.isnull().sum())

    return df_data


    #시각화 자동화 함수

    #워드로 보내는 함수