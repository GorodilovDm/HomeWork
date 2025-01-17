from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            string = file.readline()
            if string != '':
                all_data.append(string)
            else:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = datetime.now()
    for name in filenames:
        read_info(name)
    time_stop = datetime.now()
    print(time_stop - time_start, '(линейный)')

    time_start = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    time_stop = datetime.now()
    print(time_stop - time_start, '(многопроцессный)')
