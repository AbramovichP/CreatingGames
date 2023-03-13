rashod_na_100_km = 0 # Расход на 100 км
all_km = 0 # Всего километров
price_litr = 0 # Цена за литр
all_rashod = 0 # Всего литров на поездку
all_price = 0 # Общая стоимость бензина

rashod_na_100_km = int(input("Введите расход топлива автомобиля на 100 км.: "))
all_km = int(input("Введите сколько километров собираетесь проехать: "))
price_litr = int(input("Сколько стоит литр беньзина? "))

all_rashod = all_km / 100 * rashod_na_100_km
all_price = all_rashod * price_litr