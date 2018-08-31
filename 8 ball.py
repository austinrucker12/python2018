name = input("what is your name?")
print(f"hi {name}")
import random
mylist = ["yes","no","dont count on it","most likey not","very much so"]


while True:
    n = input("what is your question,and if you want to leave you have to say thank you magic 8 ball")
    answer = random.choice(mylist)
    print("your answer is %s" %answer)
    if n.strip() == "thank you magic 8 ball":
        break
    

