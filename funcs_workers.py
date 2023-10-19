import  pickle
import json
def info_workers(kwargs):
    for k, v in sorted(kwargs.items()):
        print(f"{k}  {v}")

def salgt35k(kwargs):
    s = [f"{k}  {v}" for k, v in kwargs.items() if v > 35000]
    for i in s:
        print(i)

def sallt35k(kwargs):
    s = [f"{k}  {v}" for k, v in kwargs.items() if v < 35000]
    for i in s:
        print(i)

def salmax(kwargs):
    m = max([val for val in kwargs.values()])
    for k, v in kwargs.items():
        if v == m:
            print(f"Максимальный оклад у сотр {k} = {v}")

def salmin(kwargs):
    m = min([val for val in kwargs.values()])
    for k, v in kwargs.items():
        if v == m:
            print(f"Минимальный оклад у сотр {k} = {v}")

def salmiddle(kwargs):
    print(f"Средний оклад: {sum([v for v in kwargs.values()]) / len(kwargs)}")

def save(kwargs):
    try:
        with open("workers.bin", "wb") as file:
            pickle.dump(kwargs, file)
        print("Данные выведены в файл!")
    except:
        print("Ошибка в работе с файлом!")

def load(kwargs):
    d = {}
    try:
        with open("workers.bin", "rb") as file:
            d = pickle.load(file)
        print("Данные прочитаны!!!")
        return d
    except:
        print("Ошибка в работе с файлом!")

def save_txt(kwargs):
    with open("data.txt", "w+") as file:
        file.write(f"{kwargs}")
    file.close()

def save_data(kwargs):
    with open("data.json", "w") as file:
        file.write(json.dumps(kwargs))

def load_data(kwargs):
    d = {}
    with open("data.json", "r") as file:
        d = json.loads(file.read())
    print("Данные прочитаны!")
    return d

