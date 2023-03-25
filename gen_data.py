import numpy as np
import pandas as pd

# データ数
n = 30000

# 年収の平均値と標準偏差
income_mean = 50000
income_std = 10000

# 年齢の平均値と標準偏差
age_mean = 35
age_std = 10

# クレジットヒストリーの平均値と標準偏差
credit_mean = 700
credit_std = 50

# 債務不履行の確率
default_prob = 0.2

# 年収、年齢、クレジットヒストリーのデータを生成
income = np.random.normal(income_mean, income_std, n)
age = np.random.normal(age_mean, age_std, n)
credit = np.random.normal(credit_mean, credit_std, n)

# 債務不履行かどうかを決定する
default = np.random.binomial(n=1, p=default_prob, size=n)

# DataFrameに変換
data = pd.DataFrame({'income': income, 'age': age, 'credit': credit, 'default': default})

# CSVファイルに保存
data.to_csv('credit_data.csv', index=False)