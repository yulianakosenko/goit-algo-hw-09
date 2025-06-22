def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    Обирає найбільший можливий номінал на кожному кроці.
    
    :param amount: Сума, яку треба розбити на монети
    :return: Словник {номінал: кількість монет}
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет у порядку спадання
    result = {}

    for coin in coins:
        # Обчислюємо скільки монет цього номіналу можна використати
        count = amount // coin
        if count > 0:
            result[coin] = count  # Додаємо в результат
            amount -= coin * count  # Зменшуємо залишок суми

    return result


def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для мінімальної кількості монет.
    Будує оптимальне розбиття суми на найменшу кількість монет.

    :param amount: Сума, яку треба розбити
    :return: Словник {номінал: кількість монет}
    """
    coins = [1, 2, 5, 10, 25, 50]  # Номінали монет (порядок неважливий)
    
    # min_coins[i] — мінімальна кількість монет для суми i
    min_coins = [0] + [float('inf')] * amount
    # last_used_coin[i] — остання монета, яку використали для суми i
    last_used_coin = [0] * (amount + 1)

    # Заповнюємо таблицю мінімальних монет
    for coin in coins:
        for i in range(coin, amount + 1):
            # Якщо використання цієї монети покращує результат — оновлюємо
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_used_coin[i] = coin

    # Відновлюємо, які монети були використані
    result = {}
    current = amount
    while current > 0:
        coin = last_used_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


# Тестування в консолі
if __name__ == "__main__":
    test_amount = 113
    print(f"Сума: {test_amount}")

    print("Жадібний алгоритм:")
    print(find_coins_greedy(test_amount))  # Наприклад: {50: 2, 10: 1, 2: 1, 1: 1}

    print("Динамічне програмування:")
    print(find_min_coins(test_amount))  # Наприклад: {50: 2, 10: 1, 2: 1, 1: 1}
