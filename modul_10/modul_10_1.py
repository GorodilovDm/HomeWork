import threading
from time import sleep
from datetime import datetime


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')

thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'), daemon=True)
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'), daemon=True)
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'), daemon=True)
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'), daemon=True)

time_start = datetime.now()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')
