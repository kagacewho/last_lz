import Archimed as arh # импортируем файлы
import pyramid as pyr


def main():
    user_input = input("Archimed = 1. Pyramid = 2. Выберите функцию: ") 
    if user_input.lower() == '1':         # Добавляем из пирамды
        a = float(input("Введите плотность воды: "))
        c = float(input("Введите массу тела: "))
        d = float(input("Введите объем погруженной части объекта: "))
        e = float(input("Введите плотность объекта: "))
        arh.archimed(a)
    elif user_input.lower() == '2':       # Добавляем из Архимеда
        h = float(input('Введите высоту пирамиды: '))
        s1 = float(input('Введите площадь верхнего основания: '))
        s2 = float(input('Введите площадь нижнего основания: '))
        print("Обьем усеченной пирамиды: ", pyr.V(s1,s2,h))

if __name__ == "__main__":
    main()