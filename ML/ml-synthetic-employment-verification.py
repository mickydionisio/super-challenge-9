import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create a fake employment verification dataset
data = {
    'income': [25000,50000, 60000, 70000, 20000, 80000, 90000, 95000, 40000, 25000],
    'years_employed': [2,5, 6, 7, 2, 8, 9, 10, 4, 5],
    'verified_income': [False,True, True, True, False, True, True, True, False,False],
    'fraudulent': [0,0, 0, 0, 1, 0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# Split the dataset into features and target
X = df.drop('fraudulent', axis=1)
y = df['fraudulent']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a machine learning model (Random Forest classifier)
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(classification_report(y_test, y_pred))

# Simulate real-time alerts
def check_verification(income, years_employed, verified_income):
    features = pd.DataFrame({'income': [income], 'years_employed': [years_employed], 'verified_income': [verified_income]})
    prediction = model.predict(features)
    if prediction[0] == 1:
        return "Alert: Potentially fraudulent employment verification!"
    else:
        return "No issues detected."

# Simulate real-time verification checks
income = 25000
years_employed = 5
verified_income = False
alert_message = check_verification(income, years_employed, verified_income)
print(alert_message)
