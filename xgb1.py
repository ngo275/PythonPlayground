# 必要なライブラリをインポート
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# データを読み込む
df = pd.read_csv('credit_data.csv')

# データ前処理
# 欠損値を平均値で補完する
df.fillna(df.mean(), inplace=True)

# トレーニングデータとテストデータに分割する
train, test = train_test_split(df, test_size=0.2)

# 特徴量とラベルを分割する
X_train = train.drop(['default'], axis=1)
y_train = train['default']
X_test = test.drop(['default'], axis=1)
y_test = test['default']

# XGBoostモデルをトレーニングする
params = {
    'max_depth': 3,
    'learning_rate': 0.1,
    'n_estimators': 100,
    'objective': 'binary:logistic',
    'gamma': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'min_child_weight': 1,
    'scale_pos_weight': 1,
    'random_state': 42
}

model = xgb.XGBClassifier(**params)
model.fit(X_train, y_train)

# モデルの性能を評価する
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: %.2f%%' % (accuracy * 100.0))
