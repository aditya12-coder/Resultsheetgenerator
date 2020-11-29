# result sheet
# import random

# variable initializing

NOS = 3
# , "Compu", "O.Maths","Nepali","Health"]
subject = ["English", "Maths", "Social"]

# -----------------------------------------------------------------


def data_input(n, sub):
    # student name input
    name = []
    for i in range(n):
        print("Enter name of student-", i+1, ": ", end="")
        nm = input()
        name.append(nm)
    marks = []
    marks.append(sub.copy())  # marks.append(sub)
    marks[0].insert(0, "Name")  # [["Name","English", "Maths", "Social"],]

    # mark input for all student in all subject
    for i in range(1, n+1):
        mark = []
        for j in range(len(sub)):
            # -----------------------------------
            print("Enter mark for ", name[i-1],
                  "  in subject ", sub[j], ": ", end="")
            mark.append(int(input()))
            # ------------------------------------
            # mark.append(random.randint(25,100))
        marks.append(mark)
        marks[i].insert(0, name[i-1])
    # [["Name","English", "Maths", "Social"],["ram", 1,2,3],["sam",2,3,4],["kris",3,4,5]]
    return marks


def add_total(n, res):

    # [["Name","English", "Maths", "Social", "Total"],["ram", 1,2,3],["sam",2,3,4],["kris",3,4,5]]
    res[0].insert(len(res[0]), "Total")
    for i in range(1, n+1):
        res[i].insert(len(res[i]), sum(res[i][1:]))
    # print(res)
    return res


def sort_result(res):
    # selection sort -------------sorting process
    tmp = []
    for i in range(1, len(res)):
        for j in range(1, i):
            # swap
            if res[i][len(res[i])-1] > res[j][len(res[j])-1]:
                tmp = res[i].copy()
                res[i] = res[j].copy()
                res[j] = tmp
    return res

def display_process(result):
    # display process
    for res in result:
        for r in res:
            print(r, end="\t")
        print()

def file_out(result):
    x = open("text.txt", "w")
    for res in result:
        for r in res:
            x.write(str(r))
            x.write("\t")
        x.write("\n")        
    x.close()  
    print("check text file text.txt")      


result = data_input(NOS, subject)
result = add_total(NOS, result)
result = sort_result(result)
# display_process(result)
file_out(result)
