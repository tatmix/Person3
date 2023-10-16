import funcs_workers as fw
def main():
    sys_adms = {"Сумароков": 55200, "Сизиков": 23300, "Митусов": 65000, "Смагин": 65000, "Иванов": 37000}
    act = [
        ["Информация о сотрудниках", fw.info_workers],
        ["Сотрудники, имеющие оклад > 35000", fw.salgt35k],
        ["Сотрудники, имеющие оклад < 35000", fw.sallt35k],
        ["Сотрудники, имеющие максимальный оклад", fw.salmax],
        ["Сотрудники, имеющие минимальный оклад", fw.salmin],
        ["Средний оклад", fw.salmiddle]
    ]
    while True:
        create_menu(sys_adms, act)

def create_menu(kwargs, actions):
    print("Меню:")
    for num, val in enumerate(actions):
        name = val[0]
        print(f"    {num+1}:  {name}")
    try:
        answ = int(input("Выберите операцию: "))
        if answ -1 >= len(actions) or answ -1 < 0:
            print("Неверный пункт!")
            return
        actions[answ - 1][1](kwargs)
    except Exception as e:
        print("Error =>", e)
    print()


if __name__=="__main__":
    main()

