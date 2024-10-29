import multiprocessing
import threading
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            while line != '':
                file.readline()
                all_data.append(line)
            break



files_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start_time1 = time.time()
thread1 = threading.Thread(target=read_info, args=('file 1.txt',))
thread2 = threading.Thread(target=read_info, args=('file 2.txt',))
thread3 = threading.Thread(target=read_info, args=('file 3.txt',))
thread4 = threading.Thread(target=read_info, args=('file 4.txt',))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
end_time1 = time.time()
print(end_time1 - start_time1)


if __name__ == '__main__':
    start_time2 = time.time()
    prosess1 = multiprocessing.Process(target=read_info, args=('file 1.txt',))
    prosess2 = multiprocessing.Process(target=read_info, args=('file 2.txt',))
    prosess3 = multiprocessing.Process(target=read_info, args=('file 3.txt',))
    prosess4 = multiprocessing.Process(target=read_info, args=('file 4.txt',))
    prosess1.start()
    prosess2.start()
    prosess3.start()
    prosess4.start()
    end_time2 = time.time()
    print(end_time2 - start_time2)