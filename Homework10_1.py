from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    #word_count = 0
    #file = open(file_name, 'a', encoding='utf-8')
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №  {i + 1}\n')
            #sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now() # засекаем время

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now() # время окончания
time_res = time_stop - time_start
print(f'Время выполнения {time_res}')

time2_start = datetime.now()
thread_5 = Thread(target=write_words, args= (10, 'example5.txt'))
thread_6 = Thread(target=write_words, args= (30, 'example6.txt'))
thread_7 = Thread(target=write_words, args= (200, 'example7.txt'))
thread_8 = Thread(target=write_words, args= (100, 'example8.txt'))

thread_5.start(), thread_6.start(), thread_7.start(), thread_8.start()
thread_5.join(), thread_6.join(), thread_7.join(), thread_8.join()
time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Время выполнения {time2_res}')