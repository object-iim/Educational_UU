import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, "r") as file:
        st_r = file.readline()
        all_data.append(st_r)

start_1 = datetime.datetime.now()
for num_files in range(1, 5):
    name = f'./file {num_files}.txt'
    read_info(name)
end_1 = datetime.datetime.now()
print(f'{end_1 - start_1 } линейный вызов')

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_files = []
        for num_files in range(1, 5):
            all_files.append(f'./file {num_files}.txt')
        start_2 = datetime.datetime.now()
        pool.map(read_info, all_files)
    end_2 = datetime.datetime.now()
    print(f'{end_2 - start_2} многопроцессный вызов')