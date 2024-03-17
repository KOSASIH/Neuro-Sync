import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def developBrainInterface(eeg_data, labels):
    """
    Develop brain-computer interface functionalities using EEG data and labels.
    
    Parameters:
    eeg_data (np.array): EEG data in the form of a 2D array.
    labels (np.array): Labels corresponding to the EEG data.
    
    Returns:
    float: Accuracy of the brain-computer interface.
    """
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(eeg_data, labels, test_size=0.2, random_state=42)
    
    # Create a random forest classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the classifier on the training data
    clf.fit(X_train, y_train)
    
    # Make predictions on the testing data
    y_pred = clf.predict(X_test)
    
    # Calculate the accuracy of the brain-computer interface
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy
