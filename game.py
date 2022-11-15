import numpy as np
number = np.random.randint(1, 101)
from time import sleep
left = 1
right = 100
count = 0
predict_number = (right + left)//2
#print("Chislo iznachalno", predict_number)
while predict_number!=number:
    predict_number = (right + left)//2
    count += 1
    if number == predict_number:
        print("Вауууу")
        sleep(2)
        print("Вы угадали!")
        sleep(2)
        print("Молодец!!!")
        sleep(5)
        print("Загаданное число", number)
        break # выход из цикла, если угадали
    elif number >= predict_number:
        left = predict_number
        sleep(2)
        print(predict_number, "Загаданное число больше")
    elif number <= predict_number:
        right = predict_number
        sleep(2)
        print(predict_number, "Загаданное число меньше")       
print(f"Ваш алгоритм угадывает число за {count} попыток")