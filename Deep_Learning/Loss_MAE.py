def Marvellous_MAE(Y_true,Y_pred):
    n  = len(Y_true)
    total_error = 0
    for i in range(n):
        error = abs(Y_true[i] - Y_pred[i])
        total_error = total_error + error
    MAE = total_error/n
    return MAE
Y_true = [10,20,30]
Y_pred = [12,18,33]
loss = Marvellous_MAE(Y_true,Y_pred)
print("loss is :",loss)