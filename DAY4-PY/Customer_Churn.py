# Create and save a dummy churn prediction model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# Dummy data
data = {
    'account_age': [1, 5, 2, 8, 3, 1, 7, 4, 6, 2],
    'purchase_frequency': [10, 2, 8, 1, 5, 9, 3, 6, 4, 7],
    'churn': [1, 0, 1, 0, 1, 1, 0, 0, 0, 1] # 1 = churned, 0 = not churned
}
df = pd.DataFrame(data)

# Prepare data for the model
X = df[['account_age', 'purchase_frequency']]
y = df['churn']

# Train a simple Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save the trained model to disk
dump(model, 'churn_model.joblib')

print("Dummy model 'churn_model.joblib' created successfully.")

import pandas as pd
from joblib import load

class Customer:
    """
    Represents a customer with behavioral attributes.
    """
    def __init__(self, customer_id, account_age, purchase_history):
        """
        Initializes the Customer object.

        Args:
            customer_id (str): A unique identifier for the customer.
            account_age (int): The age of the customer's account in months.
            purchase_history (list): A list of purchase values.
        """
        self.customer_id = customer_id
        self.account_age = account_age
        self.purchase_history = purchase_history
    
    def predict_churn(self, model_path='churn_model.joblib'):
        """
        Uses a pre-trained model to predict the probability of a customer churning.

        Args:
            model_path (str): The path to the saved pre-trained model.

        Returns:
            float: The predicted probability of churn. Returns 0 if the model
                   cannot be loaded.
        """
        try:
            # Load the pre-trained model from the file
            churn_model = load(model_path)
        except FileNotFoundError:
            print(f"Error: Model file '{model_path}' not found.")
            return 0.0

        # Feature engineering: derive relevant features for the model
        # from the customer's attributes.
        # This must match the features used to train the model.
        purchase_frequency = len(self.purchase_history)
        
        # Create a DataFrame for the model prediction
        customer_features = pd.DataFrame([[self.account_age, purchase_frequency]], 
                                         columns=['account_age', 'purchase_frequency'])

        # Predict the churn probability.
        # The model's `predict_proba` method returns probabilities for all classes.
        # We need the probability of the positive class (churn=1).
        churn_probability = churn_model.predict_proba(customer_features)[0][1]
        
        return churn_probability

# Example usage
if __name__ == "__main__":
    # Create a customer with a long account age and low purchase frequency (at-risk)
    customer1 = Customer(
        customer_id="CUST123",
        account_age=8,
        purchase_history=[15.00, 25.50]
    )
    
    # Create a customer with a new account and high purchase frequency (not at-risk)
    customer2 = Customer(
        customer_id="CUST456",
        account_age=1,
        purchase_history=[10.00, 12.50, 8.00, 30.00, 15.00]
    )
    
    # Predict churn for the customers
    churn_prob1 = customer1.predict_churn()
    churn_prob2 = customer2.predict_churn()
    
    # Print the results
    print(f"Customer {customer1.customer_id} (Age: {customer1.account_age} months, Purchases: {len(customer1.purchase_history)})")
    print(f"  Predicted churn probability: {churn_prob1:.2f}")
    
    print(f"\nCustomer {customer2.customer_id} (Age: {customer2.account_age} months, Purchases: {len(customer2.purchase_history)})")
    print(f"  Predicted churn probability: {churn_prob2:.2f}")
