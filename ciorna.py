

diabetes_test_counts = {}
for column in diabetes_test.columns:
    diabetes_test_counts[column] = diabetes_test[column].value_counts()

diabetes_test_counts = pd.DataFrame(diabetes_test_counts)
diabetes_test_counts.columns.name = 'Value'
diabetes_test_counts.index.name = 'Attribute'
print(diabetes_test_counts)

    
diabetes_train_counts = {}
for column in diabetes_train.columns:
    diabetes_train_counts[column] = diabetes_train[column].value_counts()