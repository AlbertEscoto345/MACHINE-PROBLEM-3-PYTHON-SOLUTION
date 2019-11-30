import numpy as np

print("Input data in the form [[Xi],[Yi]] (Sample input: [[1,2,3,4],[1,2,3,4]]) \n")
A=eval(input())

x=np.array([A[0]])
y=np.array([A[1]])
x=x.flatten()
y=y.flatten()

p1x=np.polyfit(x,y,1)
Ep1x=y-[np.multiply(p1x[0],x)+p1x[1]]
error_of_p1x=np.linalg.norm(Ep1x)

p2x=np.polyfit(x,y,2)
Ep2x=y-[np.multiply(p2x[0],np.power(x,2))+np.multiply(p2x[1],x)+p2x[2]]
error_of_p2x=np.linalg.norm(Ep2x)

p3x=np.polyfit(x,y,3)
Ep3x=y-[np.multiply(p3x[0],np.power(x,3))+np.multiply(p3x[1],np.power(x,2))+np.multiply(p3x[2],x)+p3x[3]]
error_of_p3x=np.linalg.norm(Ep3x)

p4x=np.polyfit(x,y,4)
Ep4x=y-[np.multiply(p4x[0],np.power(x,4))+np.multiply(p4x[1],np.power(x,3))+np.multiply(p4x[2],np.power(x,2))+np.multiply(p4x[3],x)+p4x[4]]
error_of_p4x=np.linalg.norm(Ep4x)

p5x=np.polyfit(x,y,5)
Ep5x=y-[np.multiply(p5x[0],np.power(x,5))+np.multiply(p5x[1],np.power(x,4))+np.multiply(p5x[2],np.power(x,3))+np.multiply(p5x[3],np.power(x,2))+np.multiply(p5x[4],x)+p5x[5]]
error_of_p5x=np.linalg.norm(Ep5x)

p6x=np.polyfit(x,y,6)
Ep6x=y-[np.multiply(p6x[0],np.power(x,6))+np.multiply(p6x[1],np.power(x,5))+np.multiply(p6x[2],np.power(x,4))+np.multiply(p6x[3],np.power(x,3))+np.multiply(p6x[4],np.power(x,2))+np.multiply(p6x[5],x)+p6x[6]]
error_of_p6x=np.linalg.norm(Ep6x)

p7x=np.polyfit(x,y,7)
Ep7x=y-[np.multiply(p7x[0],np.power(x,7))+np.multiply(p7x[1],np.power(x,6))+np.multiply(p7x[2],np.power(x,5))+np.multiply(p7x[3],np.power(x,4))+np.multiply(p7x[4],np.power(x,3))+np.multiply(p7x[5],np.power(x,2))+np.multiply(p7x[6],x)+p7x[7]]
error_of_p7x=np.linalg.norm(Ep7x)

p8x=np.polyfit(x,y,8)
Ep8x=y-[np.multiply(p8x[0],np.power(x,8))+np.multiply(p8x[1],np.power(x,7))+np.multiply(p8x[2],np.power(x,6))+np.multiply(p8x[3],np.power(x,5))+np.multiply(p8x[4],np.power(x,4))+np.multiply(p8x[5],np.power(x,3))+np.multiply(p8x[6],np.power(x,2))+np.multiply(p8x[7],x)+p8x[8]]
error_of_p8x=np.linalg.norm(Ep8x)

p9x=np.polyfit(x,y,9)
Ep9x=y-[np.multiply(p9x[0],np.power(x,9))+np.multiply(p9x[1],np.power(x,8))+np.multiply(p9x[2],np.power(x,7))+np.multiply(p9x[3],np.power(x,6))+np.multiply(p9x[4],np.power(x,5))+np.multiply(p9x[5],np.power(x,4))+np.multiply(p9x[6],np.power(x,3))+np.multiply(p9x[7],np.power(x,2))+np.multiply(p9x[8],x)+p9x[9]]
error_of_p9x=np.linalg.norm(Ep9x)

p10x=np.polyfit(x,y,10)
Ep10x=y-[np.multiply(p10x[0],np.power(x,10))+np.multiply(p10x[1],np.power(x,9))+np.multiply(p10x[2],np.power(x,8))+np.multiply(p10x[3],np.power(x,7))+np.multiply(p10x[4],np.power(x,6))+np.multiply(p10x[5],np.power(x,5))+np.multiply(p10x[6],np.power(x,4))+np.multiply(p10x[7],np.power(x,3))+np.multiply(p10x[8],np.power(x,2))+np.multiply(p10x[9],x)+p10x[10]]
error_of_p10x=np.linalg.norm(Ep10x)

All_error_vectors_list=[error_of_p1x,error_of_p2x,error_of_p3x,error_of_p4x,error_of_p5x,error_of_p6x,error_of_p7x,error_of_p8x,error_of_p9x,error_of_p10x]
All_error_vectors_arr=np.array([All_error_vectors_list])
Least_norm_error_vector=np.min(All_error_vectors_arr)

if (Least_norm_error_vector==error_of_p10x):
    print("The coefficients of the 10th degree polynomial f(x) that would best approximate the data are: \n")
    print(p10x)
elif (Least_norm_error_vector==error_of_p9x):
    print("The coefficients of the 9th degree polynomial f(x) that would best approximate the data are: \n")
    print(p9x)
elif (Least_norm_error_vector==error_of_p8x):
    print("The coefficients of the 8th degree polynomial f(x) that would best approximate the data are: \n")
    print(p8x)
elif (Least_norm_error_vector==error_of_p7x):
    print("The coefficients of the 7th degree polynomial f(x) that would best approximate the data are: \n")
    print(p7x)
elif (Least_norm_error_vector==error_of_p6x):
    print("The coefficients of the 6th degree polynomial f(x) that would best approximate the data are: \n")
    print(p6x)
elif (Least_norm_error_vector==error_of_p5x):
    print("The coefficients of the 5th degree polynomial f(x) that would best approximate the data are: \n")
    print(p5x)
elif (Least_norm_error_vector==error_of_p4x):
    print("The coefficients of the 4th degree polynomial f(x) that would best approximate the data are: \n")
    print(p4x)
elif (Least_norm_error_vector==error_of_p3x):
    print("The coefficients of the 3rd degree polynomial f(x) that would best approximate the data are: \n")
    print(p3x)
elif (Least_norm_error_vector==error_of_p2x):
    print("The coefficients of the 2nd degree polynomial f(x) that would best approximate the data are: \n")
    print(p2x)
else:
    print("The coefficients of the 1st degree polynomial f(x) that would best approximate the data are: \n")
    print(p1x)