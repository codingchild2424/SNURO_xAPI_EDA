#여기서는 xAPI를 다루는 클래스를 담을 것

import numpy as np
import pandas as pd

class Analyzer:

    def __init__(self, df_data):
        #unique한 actor의 배열
        self.unique_actor = df_data['actor'].unique()
        self.unique_object = df_data['object'].unique()
        self.unique_verb = df_data['verb'].unique()

        pass

    def analyze_activities:
        