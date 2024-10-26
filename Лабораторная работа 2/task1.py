money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
i=0 #переменная для запуска цикла while
months=0
while i>=0:
    bydzet=salary+money_capital
    if bydzet>spend:
        months += 1
        money_capital=bydzet-spend
        spend=spend+spend*increase
        i += 1
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
