# 🍄 Real-Time Model Training Flask Application

Welcome to the **Real-Time Model Training Flask App**, where machine learning meets interactivity! 🚀

---

## 📌 Overview

This project is designed for **data science enthusiasts, students, and educators** who want to understand how different ML models perform on the same dataset — in real time and through an intuitive UI.

Users can:
- Select and train models like **Logistic Regression, Random Forest, Support Vector Machines**, and more
- Instantly view model **performance metrics**
- Explore classification results using the **Mushroom dataset**

---

## ✨ Key Features

🔹 Real-time training of multiple machine learning models  
🔹 User-friendly Flask web interface  
🔹 Built-in preprocessing (label encoding, data cleaning)  
🔹 Displays accuracy, confusion matrix, and training results  
🔹 Extensible architecture for adding more models or datasets

---

## 📊 Dataset Info

- **Name**: Mushroom Classification Dataset  
- **Source**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Mushroom)  
- **Target Variable**: Edible (e) or Poisonous (p)  
- Contains categorical features describing mushroom characteristics

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask, Scikit-learn, Pandas, NumPy  
- **Frontend**: HTML, CSS (Bootstrap), JavaScript  
- **Hosting**: [PythonAnywhere](https://pythonanywhere.com)

---

## 🚀 Try It Out

You can explore the application live:

👉 **[Click to Open the Web App](https://pfait.pythonanywhere.com/index)**

---

## 🖼️ Screenshots

- Model selection UI
- ![Screenshot 2025-04-14 051038](https://github.com/user-attachments/assets/bd4733f4-9e06-401e-aed3-9ba61bdb7e62)
- Model training results (Accuracy and confusion matrix output)
- ![Screenshot 2025-04-14 051209](https://github.com/user-attachments/assets/798b1181-4707-45c6-a54c-d47d56be7592)
- ![Screenshot 2025-04-14 051236](https://github.com/user-attachments/assets/613b089c-ae34-4487-9fd5-4505c8dacd12)

---

## 🔮 Future Enhancements

Add dynamic hyperparameter tuning (GridSearchCV support)

Support for uploading custom datasets

Visualizations for feature importance

User login for tracking training history

---

## 🤝 Contributing
Feel free to open issues or submit pull requests. Feedback is always welcome!

---

## 🙌 Acknowledgments
UCI for the Mushroom dataset

The open-source Python & Flask community

Scikit-learn for making ML so accessible

---

## 📬 Connect
Made with ❤️ by Ahmad Yasin
🔗 LinkedIn www.linkedin.com/in/mian-ahmad-yasin | 🌐 https://ahmadyasin.vercel.app/

---

### 📦 Installation (For Local Use)

```bash
git clone https://github.com/your-username/real-time-ml-training-app.git
cd real-time-ml-training-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
