import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb
import numpy as np

# データを読み込む
credit_data = pd.read_csv("credit_data_with_business_info.csv")

# カテゴリカル変数をラベルエンコーディングする
# cat_cols = ['marital_status', 'address']
# le = LabelEncoder()
# for col in cat_cols:
#     if credit_data[col].dtypes == 'object':
#         credit_data[col] = le.fit_transform(credit_data[col])
#     else:
#         continue

# 特徴量の列名を取得する
feature_cols = credit_data.columns[:-1]

# ラベルを取得する
label_col = credit_data.columns[-1]

# 特徴量とラベルを分割する
features = credit_data[feature_cols]
labels = credit_data[label_col]

# データをトレーニング用とテスト用に分割する
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.3, random_state=123)

# テストラベルを2値化する
test_labels = np.where(test_labels > 0, 1, 0)

# XGBoostモデルを定義する
xgb_model = xgb.XGBClassifier(objective="binary:logistic", eval_metric="auc", seed=42)

# モデルをトレーニングする
xgb_model.fit(train_features, train_labels)

# テストデータでモデルを評価する
probabilities = xgb_model.predict_proba(test_features)
predictions = np.where(probabilities[:, 1] > 0.5, 1, 0)
accuracy = accuracy_score(test_labels, predictions)
print("Test Accuracy = %g" % accuracy)
