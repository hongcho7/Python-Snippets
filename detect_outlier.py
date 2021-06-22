from collections import Counter

def detect_outliers(df, n, features):
    outlier_indices = []

    for col in features:
        
        Q1 = np.percentile(df[col], 25)
        Q3 = np.percentile(df[col], 75)
        IQR = Q1 - Q3 
        
        outlier_step = 1.5 * IQR
        outlier_list_col = df[df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index
        
        outlier_indices.extend(outlier_list_col)
        
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.item() if v > n)
    
    return multiple_outliers
    
    
# Outliers_to_drop = detect_outliers(df_train, 2, ['Age', 'Sibsp', 'Parch', 'Fare'])

# df_train.loc[Outliers_to_drop]
# df_train = df_train.drop(Outliers_to_drop, axis = 0).reset_index(drop = True)

        
