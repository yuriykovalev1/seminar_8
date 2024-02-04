def read_data(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.readlines()
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    

def print_data(data):
    for line in data:
        print(line)


def write_data(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        contact_name = input("Введите имя контакта: ")
        phone_number = input("Введите номер телефона: ")
        file.write(f"{contact_name} - {phone_number}\n")


def rewrite_file(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        for line in data:
            file.write(line)


def find_contact(data):
    user_choice = input("Введите имя или номер телефона: ")
    founded = []
    for idx, line in enumerate(data):
        if user_choice.lower() in line.lower():
            print(line)
            founded.append(idx)
    if len(founded) == 0:  
        print("Контакт не найден")
    return founded


def select(data, founded):
    if len(founded)>1:
        for i, idx in enumerate(founded):
            print(f"{i+1}. {data[idx]}")
        user_choice = int(input("Введите номер контакта: "))
        user_choice = founded[user_choice-1]
    else:
        user_choice = founded[0]
    return user_choice

        
def delete_contact(data, user_choice):
    deleted = data.pop(user_choice)
    print(f'Контакт {deleted} удален')
    return data


def edit_data(data, user_choice):
    choice_change = input("1 - изменить имя, 2 - изменить номер: ")
    line = data[user_choice].split(" - ")
    print(line)
    if choice_change == "1":
        line[0]=input("Введите новое имя: ")
    elif choice_change == "2":
        line[1]=input("Введите новый номер: ")
    data[user_choice] = " - ".join(line)+"\n"


def export_contact(data, user_choice):
    file_name = input("Введите название файла: ")
    file_name = f"{file_name}.txt"
    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(f"{data[user_choice]}")


def main():
    flag = True
    file_name = "phone_book.txt"
    while flag:
        print("1 - показать контакты")
        print("2 - добавить контакт")
        print("3 - найти контакт")
        print("4 - удалить контакт")
        print("5 - изменить контакт")
        print("6 - экспортировать контакт в другой файл")
        print("0 - выход")
        user_choice = input("Выберите действие: ")
        if user_choice == "0":
            flag = False
        elif user_choice == "1":
            print_data(read_data(file_name))
        elif user_choice == "2":
            write_data(file_name)
        elif user_choice == "3":
            find_contact(read_data(file_name))
        elif user_choice == "4":
            data = read_data(file_name)
            founded = find_contact(data)
            if len(founded)>0:
                rewrite_file(file_name, delete_contact(data, select(data, founded)))
        elif user_choice == "5":
            data = read_data(file_name)
            founded = find_contact(data)
            if len(founded)>0:
                edit_data(data, select(data, founded))
                rewrite_file(file_name, data)
        elif user_choice == "6":
            data = read_data(file_name)
            founded = [x for x in range(len(data))]
            export_contact(data, select(data, founded))

if __name__ == "__main__":
    main()