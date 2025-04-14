from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
import base64
from io import BytesIO
import os

app = Flask(__name__)

my_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(my_dir, 'mushrooms.csv')

# Load and preprocess dataset
df = pd.read_csv(file_path)
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
x = df.drop('class', axis=1)
y = df['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


def plot_confusion_matrix(cm):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='.0f', cmap='Blues', xticklabels=['e', 'p'], yticklabels=['e', 'p'], linewidths=5,
                linecolor='w', annot_kws={'fontsize': 20})
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')


@app.route('/')
def presentation():
    return render_template('presentation.html')

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/result', methods=['POST'])
def result():
    algorithm = request.form['algorithm']
    if algorithm == 'Logistic Regression':
        model = LogisticRegression(max_iter=1000)
    elif algorithm == 'Random Forest':
        model = RandomForestClassifier(n_estimators=100)
    elif algorithm == 'Decision Tree':
        model = DecisionTreeClassifier(criterion='entropy', max_depth=5, min_samples_leaf=5)
    elif algorithm == 'KNN':
        model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    elif algorithm == 'SVM':
        model = SVC(kernel='linear', random_state=0)
    elif algorithm == 'Naive Bayes':
        model = GaussianNB()
    elif algorithm == 'Linear Regression':
        model = LinearRegression()
    else:
        return redirect(url_for('index'))

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    if algorithm == 'Linear Regression':
        y_pred = [1 if pred >= 0.5 else 0 for pred in y_pred]

    accuracy = accuracy_score(y_test, y_pred) * 100
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred)
    cm_image = plot_confusion_matrix(cm)

    return render_template('result.html', algorithm=algorithm, accuracy=accuracy, cm_image=cm_image,
                           classification_report=cr)


if __name__ == '__main__':
    app.run(debug=True)
