def archimed(a):   # Добавляем функцию с условями плавучести 
    if a>1:
        print("Не плавучий") 
    elif a == 1:
        print("Не плавучий")
    else:
        print("Плавучий") 

g = 10
F = lambda a, g, d : a * g * d



def main (): # Добавляем фунцкию main
    a = float(input("Введите плотность воды: "))   # Ввод значений с клавитуры
    c = float(input("Введите массу тела: "))
    d = float(input("Введите объем погруженной части объекта: "))
    e = float(input("Введите плотность объекта: "))
    archimed(F)

if __name__ == '__main__':  # Для модульного запуска
    main()