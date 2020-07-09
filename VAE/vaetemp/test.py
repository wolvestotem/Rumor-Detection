import numpy as np

a = np.array([[1,2,3],[2,3,4]])
b = np.array([[1,2,3,4],[2,3,4,5]])
c = np.hstack((a,b))
# print(c)
with open("test.csv", "ab") as f:
    np.savetxt(f, c, delimiter=',',fmt='%i')