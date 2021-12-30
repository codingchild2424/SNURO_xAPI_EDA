from json_parser import json_loader, json_parser_to_pd
from xAPI_Analyzer import Analyzer
import matplotlib.pyplot as plt
from visualizer import act_visualizer, watching_visualizer, personal_watching_visualizer
from auto_word import make_LA_report

#argument_parser로 변경하기
#data_path = "data/XAPI_npe_1215.json"
data_path = "data2/XAPI_5d933d.json" #<- 데이터를 변경해도 잘 들어가는 것을 확인할 수 있음

json_data = json_loader(data_path)

df_data = json_parser_to_pd(json_data)

xAPI_analyzer = Analyzer(df_data)

students, total_logs = xAPI_analyzer.analyze_activities()

#활동 시각화 결과물 visualization 폴더에 저장
act_visualizer(students, total_logs)

unique_actor, data_list = xAPI_analyzer.analyze_watching_time()

#시청 행동 시각화 결과물 visualization 폴더에 저장
watching_visualizer(unique_actor, data_list)

#개인별 시청 행동 시각화 결과물 visualization 폴더에 저장
#for문으로 loop돌리기
for stu in unique_actor:
    verb_list = xAPI_analyzer.personal_watching_time(stu)
    personal_watching_visualizer(verb_list, stu)

picture1 = 'visualization/act_visualization.png'
picture2 = 'visualization/watching_visualization.png'
#이건 사용자에 맞게 적절하게 수정해서 사용
picture3 = 'visualization/personal_watching_visualization.png'

make_LA_report(picture1, picture2, picture3)