# ----------------------Arroja un  arreglo donde se eliminan los números repetidos ------------------------

# def filter_duplicates(ts):
#     cont = len(ts)-1
#     for i in reversed(ts):
#         if ts.count(i) >= 2:
#             del ts[cont]
#         cont = cont - 1
#     print(ts)



# filter_duplicates([7,6,4,3,3,4,9])

# def filter_duplicates(ts):
#     ts1 = []
#     for i in ts:
#         if i not in ts1:
#             ts1.append(i)

#     print(ts1)
        

# filter_duplicates([7,6,4,3,3,4,9])

def filter_duplicates(ts):
    ts1 = {}
    ts2 = []
    for i in ts:
        if i not in ts1:
            ts1[i] = ""
            ts2.append(i)
    print(ts2)

filter_duplicates([7,6,4,3,3,4,9])
