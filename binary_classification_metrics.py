'''
Binary Classification Problem
'''

# Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)

# tp, tn, fp, fn

def true_positive:
    
    tp = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 1:
            tp += 1
    return tp
    
def true_negative:
    
    tn = 0
    
    for yt, yp in zip(y_true, y_pred):
        if y== 0 and yp == 0:
        
            tn += 1
    return tn
    
def false_positive(y_true, y_pred):
    
    fp = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yt == 0 and yp == 1:
            fp += 1
    
    return fp
    
def false_negative(y_true, y_pred):

    fn = 0
    
    for yt, yp in zip(y_true, y_pred):
        if yt == 1 and yp == 0:
        
            fn += 1
    return fn
    
# Precision
from sklearn.metrics import precision_score
precision_score(y_true, y_pred)

# Recall
from sklearn.metrics import recall_score
recall_score(y_true, y_pred)

# F1 score
from sklearn.metrics import f1_score
f1_score(y_true, y_pred)

# True Positive Rate
def tpr(y_true, y_pred):
    return recall(y_true, y_pred)
    
# False Posotive Rate
def fpr(y_ture, y_pred):
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    
    return fp / (tn + fp)
    
# ROC_AUC
from sklearn.metrics import roc_auc_score
roc_auc_score(y_true, y_pred)

# log loss
from sklearn.metircs import log_loss
log_loss(y_true, y_pred)

# Matthew's Correlation Coefficient (MCC)

def mcc(y_ture, y_pred):
    
    tp = true_positive(y_true, y_pred)
    fn = false_negative(y_true, y_pred)
    fp = false_positive(y_true, y_pred)
    tn = true_negative(y_true, y_pred)
    
    numerator = (tp * tn) - (fp * fn)
    
    denominator = (
    (tp + fp) *
    (fn + tn) *
    (fp + tn) *
    (tp + fn)
    )
    
    denominator = denominator ** 0.5
    
    return numerator / denominator
    
