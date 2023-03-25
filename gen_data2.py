import numpy as np
import pandas as pd

# データ数
n = 10000

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

# Marital statusのデータを生成
marital = np.random.choice(['Single', 'Married'], size=n, p=[0.4, 0.6])

# ビジネスに関連する情報を生成
years_in_business = np.random.randint(low=1, high=20, size=n)
num_staff = np.random.randint(low=1, high=20, size=n)
monthly_sales = np.random.normal(loc=50000, scale=10000, size=n)
monthly_expenses = np.random.normal(loc=40000, scale=8000, size=n)

# ビジネスの住所をランダムに生成
cities = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka']
addresses = [np.random.choice(cities) + str(np.random.randint(1, 100)) for i in range(n)]

# Order履歴をランダムに生成
num_orders = np.random.randint(low=1, high=100, size=n)
order_history = np.random.normal(loc=50, scale=10, size=n)

# DataFrameに変換
data = pd.DataFrame({
    'income': income,
    'age': age,
    'credit': credit,
    'default': default,
    # 'marital_status': marital,
    'years_in_business': years_in_business,
    'num_staff': num_staff,
    'monthly_sales': monthly_sales,
    'monthly_expenses': monthly_expenses,
    # 'address': addresses,
    'num_orders': num_orders,
    'order_history': order_history
})

# CSVファイルに保存
data.to_csv('credit_data_with_business_info.csv', index=False)