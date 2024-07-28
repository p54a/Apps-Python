import random

times = 1
lenth = 16
link = "https://t.me/+"

for i in range(times):
    for x in range(lenth):
        rand = random.choice("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM")
        link += rand
    print(link)