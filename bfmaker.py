import os

def search(n, N):
    global cur, result, count
    if n == N - 1:
        for i in subject_queue[n][1:]:
            flag = True
            for j in i:
                for k in range(j[1], j[2]):
                    if time_table[j[0]][k]:
                        flag = False
                        break

                if not flag:
                    break

            if flag:
                for j in i:
                    for k in range(j[1], j[2]):
                        time_table[j[0]][k] = True

                flag2 = True
                for j in range(0, 4):
                    f = False
                    block = 0
                    for k in range(9, 17):
                        if not f and time_table[j][k]:
                            block += 1
                            f = True

                        if f and not time_table[j][k]:
                            f = False
                    
                    if block != 2:
                        flag2 = False
                        break

                if flag2:
                    flag3 = True
                    for j in range(0, 4):
                        if not ((time_table[j][12] == False and time_table[j][11] == True and time_table[j][13] == True) or (time_table[j][13] == False and time_table[j][12] == True and time_table[j][14] == True) or (time_table[j][14] == False and time_table[j][13] == True and time_table[j][15] == True)):
                            flag3 = False
                            break
                    
                    if flag3:
                        cur += [[subject_queue[n][0], i]]
                        result += [cur[:]]
                        cur.pop(-1)
                
            else:
                continue

            for j in i:
                for k in range(j[1], j[2]):
                    time_table[j[0]][k] = False

    else:           
        for i in subject_queue[n][1:]:
            flag = True
            for j in i:
                for k in range(j[1], j[2]):
                    if time_table[j[0]][k]:
                        flag = False
                        break

                if not flag:
                    break

            if flag:
                for j in i:
                    for k in range(j[1], j[2]):
                        time_table[j[0]][k] = True

                cur += [[subject_queue[n][0], i]]
                
            else:
                continue
            
            search(n + 1, N)
            cur.pop(-1)
            for j in i:
                for k in range(j[1], j[2]):
                    time_table[j[0]][k] = False
                    

N = int(input("과목의 수: "))
subject_queue = []
for i in range(0, N):
    subject_queue += [[input("과목명" + str(i) + ": ")]]

for i in range(0, N):
    print(subject_queue[i][0], "시간대 입력")
    j = 1
    while True:
        if input("more? ") != '0':
            subject_queue[i] += [[]]
            
            while True:
                s = input()
                if s == '0':
                    break

                ss = s.split()
                a = tuple(map(int, ss))
                subject_queue[i][j] += [a]

            j += 1

        else:
            break

result = []
cur = []
time_table = []
for i in range(0, 4):
    time_table += [[]]
    for j in range(0, 17):
        time_table[i] += [False]

search(0, N)

count = 0
fd = os.open("result.txt", os.O_TEXT | os.O_RDWR)
for i in result:
    os.write(fd, ("case " + str(count) + "\n").encode())
    for j in i:
        os.write(fd, (j[0] + ": " + str(j[1]) + "\n").encode())

    os.write(fd, "\n\n".encode())
    count += 1

os.close(fd)
