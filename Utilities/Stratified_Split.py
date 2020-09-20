from sklearn.model_selection import train_test_split

def Stratified_Split(X, y):

  """ A function to perform a stratified train-val-test split.""" 

  # Execute train/test split:
  X_train, X_test, y_train, y_test = train_test_split(
      X, y, 
      train_size=0.7, 
      random_state=69,
      stratify=y
      )
  
  # Execute test/validation split:
  X_test, X_val, y_test, y_val = train_test_split(
      X_test, y_test, 
      train_size=0.33, 
      random_state=69,
      stratify=y_test
      )
  
  print('Splited data into Train-Validation-Test sets.')
  return [X_train, X_test, X_val, y_train, y_test, y_val]  
