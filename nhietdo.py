from convert import chuyendoi
from unit import unit
nhietdo=float(input("nhap vao nhiet do :"))
donvi=str(input("nhap vao don vi nhiet do :"))
print("nhiet do da duoc chuyen doi thanh:  ")
print(chuyendoi(nhietdo,donvi),unit(donvi))
