import numpy as np

a = np.array([[1,2,3],[2,3,4]])
b = np.array([[1,2,3,],[2,3,4,]])
c = np.hstack((a,b))
d = a+b
print(d)
# with open("test.csv", "ab") as f:
#     np.savetxt(f, c, delimiter=',',fmt='%i')