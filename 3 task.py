import os
# функция для получения данных по ДЗ из файлов в папке
def produce_file_list(folder):
    file_list = os.listdir(folder)
    union_file_list = []
    for file in file_list:
        with open(folder + "/" + file, encoding='utf-8') as _temp_file: # почему-то на пайчарм кодировка слетает если не прописать
            union_file_list.append([file, 0, []])
            for line in _temp_file:
                union_file_list[-1][2].append(line.strip())
                union_file_list[-1][1] += 1
    return sorted(union_file_list, key=lambda x: x[1], reverse=False)

# функция записи требуемого файла построчно
def produce_union_file(folder, filename):
    with open(filename + '.txt', 'w+') as union_file: # w+ открывает файл на чтение и запись
        union_file.write(f'Итоговый файл:\n')
        for file in produce_file_list(folder):
            union_file.write(f'Название файла: {file[0]}\n')
            union_file.write(f'Кол-во строк: {file[1]}\n')
            for string in file[2]:
                union_file.write(string + '\n')
            union_file.write('\n')
    return print('Готово')

produce_union_file('txt', 'union_file')