import pandas as pd
import numpy as np
import json

#json data를 업로드하는 함수
def json_uploader(data_path):
    with open(data_path, "r", encoding = "utf-8") as f:
        contents = f.read()
        json_data = json.loads(contents)

    return json_data

#xapi 키를 기준으로 모두 반영하는 함수
#만약 키에 해당 값이 없다면, nan으로 반영

def xapi_reader(json_data):
    pass


