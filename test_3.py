#----------------Encuentra el número mínimo de halls para un n número de conciertos--------------------------


# num_concerts = int(input("numero de conciertos: "))
# time_intervals = []

# def min_halls (num_concerts, time_intervals):
#     for i in range(num_concerts):
#         left_interval = input(f"hora de inicio del concierto numero {i}: ")
#         right_interval = input(f"hora de inicio del concierto numero {i}: ")
#         time_intervals.append(left_interval)
#         time_intervals.append(right_interval)

#     print(time_intervals)

#     for i in range(len(time_intervals)-1, 2):
#         res = int(time_intervals[i+1]) - int(time_intervals[i])
#         print(res)


def min_halls (num_concerts, time_intervals):
    cont = 0
    for i in range(0, len(time_intervals)-3, 2):
        if time_intervals[i+1] >= time_intervals[i+3] and time_intervals[i] <= time_intervals[i+2]:
            cont += 1

    print(cont)




min_halls(3,[0,30,5,10,15,20])
