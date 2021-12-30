import matplotlib.pyplot as plt
import os
import re

#활동량 시각화 함수
def act_visualizer(students, total_logs):
    plt.figure(figsize = (20, 10))
    plt.bar(students, total_logs)
    plt.savefig('visualization/act_visualization.png')

def watching_visualizer(X, data_list):
    plt.figure(figsize = (12, 4))

    plt.bar(X, data_list[0], label = '시청기록')
    plt.bar(X, data_list[1], bottom = data_list[0], label = '시청중')
    plt.bar(X, data_list[2], bottom = data_list[0] + data_list[1], label = '실행')
    plt.bar(X, data_list[3], bottom = data_list[0] + data_list[1] + data_list[2], label = '중지')
    plt.bar(X, data_list[4], bottom = data_list[0] + data_list[1] + data_list[2] + data_list[3], label = '퀴즈/메시지 등장')
    plt.bar(X, data_list[5], bottom = data_list[0] + data_list[1] + data_list[2] + data_list[3] + data_list[4], label = '퀴즈/메시지 응답')
    plt.bar(X, data_list[6], bottom = data_list[0] + data_list[1] + data_list[2] + data_list[3] + data_list[4] + data_list[5], label = '강의 평가 등장')
    plt.bar(X, data_list[7], bottom = data_list[0] + data_list[1] + data_list[2] + data_list[3] + data_list[4] + data_list[5] + data_list[6], label = '강의 평가 제출')

    plt.legend()

    plt.savefig('visualization/watching_visualization.png')

def personal_watching_visualizer(data_list, student_name):
    plt.figure(figsize = (80, 1))
    plt.imshow([
        data_list,
    ],  
    interpolation = 'nearest',
    aspect = 'auto',
    cmap = 'inferno'
    )

    folder_name = 'visualization/'

    #이름 특수문자 제거
    special = re.compile(r'[^ A-Za-z0-9가-힣+]')
    result = special.sub('_',student_name)

    file_name = '_personal_watching_visualization.png'

    output_name = os.path.join(folder_name, result + file_name)

    plt.savefig(output_name)