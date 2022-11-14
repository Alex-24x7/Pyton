def print_data(data):
    if len(data) >0:
        print('Фамилия'.center(20),'Имя'.center(20),'Отчество'.center(20),'Дата рождения'.center(20),'Телефон'.center(20),'Категория'.center(20))
        print('-'*130)
        for item in data:
            print(item[0].center(20),item[1].center(20),item[2].center(20),item[3].center(20),item[4].center(20),item[5].center(20))
    else:
        print('Справочник пуст!')
    