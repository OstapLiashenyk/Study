import matplotlib.pyplot as plt 
import numpy as np 
 
 
def function(x): 
    return x ** 2 - 2 * x * 4 
 
 
def create_basic_polynomial(x_values, i): 
    def basic_polynomial(x): 
        divider = 1 
        result = 1 
        for j in range(len(x_values)): 
            if j != i: 
                result *= (x - x_values[j]) 
                divider *= (x_values[i] - x_values[j]) 
        return result / divider 
 
    return basic_polynomial 
 
 
def string(x_values, i): 
    s = "" 
    divider = 1 
    result = 1 
    for j in range(len(x_values)): 
        if j != i: 
            s += "(x - " 
            s += str(x_values[j]) 
            s += ")" 
            divider *= (x_values[i] - x_values[j]) 
    s += "/" 
    s += str(divider) 
    return s 
 
 
def create_Lagrange_polynomial(x_values, y_values): 
    basic_polynomial = [] 
    for i in range(len(x_values)): 
        val = create_basic_polynomial(x_values, i) 
        basic_polynomial.append(val) 
 
    def lagrange_polynomial(x): 
        result = 0 
        for i in range(len(y_values)): 
            result += y_values[i] * basic_polynomial[i](x) 
        return result 
 
    return lagrange_polynomial 
 
 
x_values = [-5, -1.6, -0.8, -0.2, 0.6] 
y_values = [-2.31, -1.25, -0.73, -0.2, 0.57] 
 
lan_pol = create_Lagrange_polynomial(x_values, y_values) 
 
xarr = [] 
yarr = [] 
for x in range(-100, 100): 
    xarr.append(x / 10) 
    yarr.append(lan_pol(x / 10)) 
    print(f'x = {x / 10}; y = {lan_pol(x / 10)}') 
 
 
s_val = [] 
for i in range(len(x_values)): 
    s = string(x_values, i) 
    s_val.append(s) 
 
str1 = "" 
for i in range(len(y_values)): 
    str1 += str(y_values[i]) 
    str1 += "*" 
    str1 += str(s_val[i]) 
    if i != len(y_values)-1: 
        str1 += " + " 
 
print("Polynomial:") 
print(str1,'\n') 
 
 
dot = float(input("Enter dot you want to check:")) 
print(f'Polynomial({dot}) = {lan_pol(dot)}') 
 
plt.plot(xarr, yarr) 
plt.plot(x_values, y_values, color='orange') 
 
for i in range(len(x_values)): 
    plt.scatter(x_values[i], y_values[i], color="red", linewidths=2) 
 
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5) 
plt.show() 
 
arrx = [] 
arry = [] 
 
for i in range(0, 5): 
    arrx.append(x_values[i]) 
    arry.append(function(x_values[i])) 
 
lan_pol_new = create_Lagrange_polynomial(arrx, arry) 
xarr1 = [] 
yarr1 = [] 
xarr2 = [] 
yarr2 = [] 
for x in range(int(x_values[0]) * 10, (1 + int(x_values[-1])) * 10): 
    xarr2.append(x / 10) 
    yarr2.append(lan_pol_new(x / 10)) 
poh = 0 
for x in range(-100, 100): 
    xarr1.append(x / 10) 
    yarr1.append(function(x / 10)) 
    print(f'x = {x / 10}; y = {lan_pol_new(x / 10)}') 
    poh += pow(abs(function(x / 10) - lan_pol_new(x / 10)), 2) 
 
dot = float(input("Enter dot you want to check:")) 
print(f'Polynomial({dot}) = {function(dot)}') 
 
plt.plot(xarr1, yarr1) 
plt.plot(xarr2, yarr2, color='orange') 
for i in range(len(x_values)): 
    plt.scatter(arrx[i], arry[i], color="red", linewidths=2) 
 
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5) 
plt.show() 
print(f'Error: {np.sqrt(poh) / 10}') 