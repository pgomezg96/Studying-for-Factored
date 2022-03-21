# --------------------------Encuentra el número menor en un arreglo ------------------------------
# def Array(ts):
#     min =ts[0]
#     for i in ts:
#         for j in ts:
#             if i <= j and i <= min:
#                  min = i
#             else:
#                 if j <= min:
#                     min = j
#     print(min)

                
# Array([-10000000,5,-2,3,-500,0,-999999,1])


# ---------------------------Encuentra el número más cercano a cero en un arreglo, priorizando el par positivo-----------------------------

# def closest_cero(ts):
#     min = ts[0]
#     for i in ts:
#         for j in ts:
#             if abs(min) == abs(j) and min != j:
#                 min =max(min,j)

#             if abs(i) < abs(j) and abs(i) < abs(min):
#                 min = i
                
#             else:
#                 if abs(j) < abs(i) and abs(j) < abs(min):
#                     min = j
            
#     print(min)





# closest_cero([-0.01,5,-5,-0.001,0.001,-1,0.5,50,0.01])

def closest_cero(ts):
    min = ts[0]
    for i in ts:
        if abs(min) == abs(i) and min != i:
            min =max(min,i)

        if abs(i) < abs(min):
            min = i
            
    print(min)





closest_cero([-0.01,5,-5,-0.001,0.001,-1,0.5,50,0.01,-0.0001])


