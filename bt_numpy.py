import numpy as np

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# Reshape: Tách chuỗi thành các hàng các cột
temp1 = np.array(list1).reshape(2, 4)
print(temp1)

# Kiem tra mang 1 chieu, 2 chieu, ....
print("So chieu: ", temp1.ndim)

# Kiem tra mang co bao nhieu dong cot
print("So dong va cot: ", temp1.shape)

# Kiem tra mang co bao nhieu phan tu
print("So phan tu: ", temp1.size)

#Tao mang tu 0 - 100 , buoc nhay 2
list2 = np.arange(0, 100, 2)
print(list2)

#Chia cac phaan tu trong mang deu nhau
list3 = np.linspace(1, 100, 10)
print(list3)

#Tao mang gom 3 hang 3 cot co gia tri 0
list4 = np.zeros((3, 3))
print(list4)

#Tao mang gom 3 hang 3 cot co gia tri 1
list5 = np.ones((3, 3))
print(list5)