def main():
    # Читаем значение k
    k = int(input())

    # Вычисляем количество шариков
    total_balls = 0 
    for i in range(1,k+1):
        total_balls += 2**(i-1)

    # Выводим результат
    print(total_balls)


if __name__ == '__main__':
    main()
