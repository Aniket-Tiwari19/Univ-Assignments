qa={"Q1":"y","Q2":"n","Q3":"n","Q4":"y","Q5":"y","Q6":"y","Q7":"n","Q8":"n","Q9":"y","Q10":"y"}
def push(l,it):
    l.append(it)
def pop(l,it):
    l.pop()
def peek(l):
    print(l[-1])
def checkemp(l):
    if len(l)==0:
        print("Empty")
while True:
    print("The participants will be asked 10 questions  \n Answer in (y/n)")
    ans=[]
    print("Now answer the following questions")
    for i in range(0,10):
        print(list(qa.keys())[i])
        try:
            a = input("Enter the answer (y/n): ")
            if a not in ("y", "n"):
                raise ValueError("Invalid input. Please enter 'y' or 'n'.")
        except ValueError as e:
            print(e)
            continue
        if a == qa[list(qa.keys())[i]]:
            push(ans,a)
        else:
            push(ans,a)
            pop(ans)
        peek(ans)
        checkemp(ans)