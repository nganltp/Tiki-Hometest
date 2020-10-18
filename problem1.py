import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def sum_descent_m_c(X, Y, m, c):
    D_m = 0
    D_c = 0
    for j,y in enumerate(Y):
        x = X[j]
        y_pred = m*x + c
        if (y-y_pred < -1):
            D_m =  D_m + 1/2 *x
            D_c = D_c + 1/2
        elif (y-y_pred > 1):
            D_m = D_m -1/2 *x
            D_c = D_c - 1/2
        else:
            D_m = D_m - x*(y-y_pred)
            D_c = D_c - (y-y_pred)
    return D_m, D_c
    
def gradient_descent(X, Y, m, c):
    D_m, D_c = sum_descent_m_c(X, Y, m, c)
    m = m - learning_rate*D_m
    c = c - learning_rate*D_c
    return m, c

npzfile = np.load('data_hometest_1.npz')
X, Y = npzfile['arr_0'],npzfile['arr_1']

# y = mx + c
m = 0
c = 0
learning_rate = 0.01
epochs = 100
loss = []
epoch_count = []
for i in range(epochs):
    m, c = gradient_descent(X, Y, m, c)
    print(i, m, c)
    
    epoch_count.append(i)
    Y_pred = m*X + c
    loss.append(sum(Y-Y_pred))

# plt.plot(epoch_count, loss, 'b-')
plt.plot(X, Y, 'ro', color='blue')
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')

plt.show()