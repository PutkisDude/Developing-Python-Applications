#AUTHOR LAURI PUTKONEN
#5. Generate a lottorow (try to use an array here).
import random

lottorow = []

while len(lottorow) < 7:
    number = random.randint(1,40)
    if number not in lottorow:
        lottorow.append(number)

extranumber = random.randint(1,40)
                    
print("Lottonumbers are:", lottorow)
print("Extra number is", extranumber)
