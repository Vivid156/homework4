immutable_var = 1, 2, 3, 'string', True
print(immutable_var)
#immutable_var[1] = 4 # поменять второй элемент в кортеже не получится, так как это число, которое неизменяемое, как и сам кортеж
#print(immutable_var)
mutable_var = 1,2, [True], "строка"
mutable_var[2][0] = 500
print(mutable_var)
