from time import sleep
import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def main():
    start_time1 = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    end_time1 = time.time()
    print(f"Работа потоков: {end_time1 - start_time1}")

    start_time2 = time.time()
    threads = []
    for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
        thread = threading.Thread(target=write_words, args=(word_count, file_name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time2 = time.time()
    print(f"Работа потоков: {end_time2 - start_time2}")

if __name__ == "__main__":
    main()