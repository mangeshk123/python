def Marvellous_MSE(Y_true,Y_pred):
    n  = len(Y_true)
    total_error = 0
    for i in range(n):
        error = Y_true[i] - Y_pred[i]
        total_error = total_error + (error**2)
    MSE = total_error/n
    return MSE
Y_true = [10,20,30]
Y_pred = [12,18,33]
loss = Marvellous_MSE(Y_true,Y_pred)
print("loss is :",loss)