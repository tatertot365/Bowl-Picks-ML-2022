import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import IS_415_Project as proj
import statsmodels
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics

df = pd.read_csv('teams_col_add.csv')
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'home_postgame_elo', 'away_postgame_elo', 'week', 'away_points', 'home_points', 'home_post_win_prob', 'away_post_win_prob', 'point_diff'])
df = df.dropna()

for col in df:
  if not pd.api.types.is_numeric_dtype(df[col]):
    df = df.join(pd.get_dummies(df[col], prefix=col))

y = df['win/loss']
X = df.drop(columns=['win/loss', 'win/loss_L', 'win/loss_W'])
X = X.select_dtypes(include=np.number)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12345)

clf_decision_tree = DecisionTreeClassifier(random_state=12345)

clf = clf_decision_tree.fit(X_train,y_train)
y_pred = clf.predict(X_test)

output_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred,})

cm = metrics.confusion_matrix(y_test, y_pred)
cm_display = metrics.ConfusionMatrixDisplay(cm, display_labels=['no', 'yes'])
cm_display.plot(values_format='d')
plt.savefig('win_loss_confusion_matrix.jpg')
plt.show()

tn, fp, fn, tp = cm.ravel()

# Accuracy  = (true positives + true negatives) / (total cases); the percentage of predictions the model got right
accuracy2 = (tp + tn) / (tp + tn + fp + fn)
print("Accuracy2: " + str(round(accuracy2, 4))) 

# Precision = (true positives / (true positives + false positives)); what proportion of predicted positive identifications(no) where actually correct
precision2 = tp / (tp + fp)
print("precision2: " + str(round(precision2, 4))) 

# Recall    = (true positives / (true positives + false negatives)); What proportion of actual positives were identified correctly? 
recall2 = tp/(tp+fn)
print("recall2: " + str(round(recall2, 4))) 

# F1        = (2 * (precision * recall) / (precision + recall))
f12 = (2 * (precision2 * recall2) / (precision2 + recall2))
print("f12: " + str(round(f12, 4))) 


# saving and ouputting the decision tree
"""from sklearn.tree import export_graphviz
from six import StringIO 
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True, feature_names = X.columns,class_names=['no', 'yes'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('win_loss_decision_tree.png')
Image(graph.create_png())"""
