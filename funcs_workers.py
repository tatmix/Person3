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