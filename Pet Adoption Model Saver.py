import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score

def encode_categorical_columns(Pet_data):
    '''
    Adjusts the data so we can train our model on it. It takes the catogorical columns and splits
    it up in multiple columns that are True or False.
    
    Parameters
    ----------
    Pet_data : Unencoded data.

    Returns
    -------
    Pet_data : Encoded data.

    '''
    categorical_cols = ['PetType', 'Breed', 'Color', 'Size']
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded_cols = pd.DataFrame(encoder.fit_transform(Pet_data[categorical_cols]))
    encoded_cols.columns = encoder.get_feature_names(categorical_cols)
    Pet_data.drop(columns=categorical_cols, inplace=True)
    Pet_data = pd.concat([Pet_data, encoded_cols], axis=1)
    
    return Pet_data

def find_best_params():
    '''
    Searches the best params for the model.
    
    Returns
    -------
    grid_search.best_params_: The best params for the model.
    grid_search.best_score_: The best score the model achieved.

    '''
    
    model = DecisionTreeClassifier(random_state=42)
    
    param_grid = {
        'max_depth': range(1, 10),
        'min_samples_split': range(2, 20, 2),
        'min_samples_leaf': range(1, 10)
    }
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=20)
    grid_search.fit(X, y)
    
    print("Best Parameters:", grid_search.best_params_)
    print("Best Score:", grid_search.best_score_)
    
    return grid_search.best_params_, grid_search.best_score_
    
    
def test_accuracy():
    '''
    Tests the accuracy score of the model.
    
    Returns
    -------
    score: The accuracy score of the model.

    '''
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    score = accuracy_score(y_test, predictions)
    
    print("Accuracy:", score)
    
    return score

def save_model():
    '''
    Saves the model in a file for later use.

    '''
    
    model = DecisionTreeClassifier(max_depth=5, min_samples_split=5, min_samples_leaf=2)
    model.fit(X, y)
    
    joblib.dump(model, 'decision_tree_model.pkl')


Pet_data = pd.read_csv('pet_adoption_data.csv')  # Import the pet data.

Pet_data = encode_categorical_columns(Pet_data)  # Encode the categorical columns

X = Pet_data.drop(columns=['AdoptionLikelihood', 'PetID'])  # X data
y = Pet_data['AdoptionLikelihood']  # y data

save_model()  # Saving the model

    

    
