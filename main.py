import requests
import json
import threading


def load(start, end, json_file_name):
    json_path = "{}.json".format(json_file_name)
    with open(json_path, 'a') as file:
        for i in range(start, end):
            product = requests.get("https://dummyjson.com/products/{}".format(i)).json()
            json.dump(product, file)
            file.write(",\n    ")


def remove_last_comma(json_file_name):
    with open(json_file_name, 'r') as file:
        data = file.readlines()

    data[-2] = data[-2].rstrip(',\n    ')

    with open(json_file_name, 'w') as file:
        file.writelines(data)
        file.write("\n")


def generate(number_of_threads, number_of_loads, file_name="result"):
    json_path = "{}.json".format(file_name)
    with open(json_path, 'w') as file:
        file.write('[\n    ')

    loads_for_each = number_of_loads // number_of_threads
    remainder = number_of_loads - (loads_for_each * number_of_threads)
    end = 1
    threads = []

    for i in range(number_of_threads):
        start = end
        end = start + loads_for_each
        if remainder > 0:
            end += 1
            remainder -= 1
        t = threading.Thread(target=load, args=(start, end, file_name))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    remove_last_comma(json_path)

    with open(json_path, 'a') as file:
        file.write(']')

    print("Threads are done, file is generated!")


if __name__ == '__main__':
    generate(8, 100)
