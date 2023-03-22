rashod_na_100_km = 0 # Расход на 100 км
all_km = 0 # Всего километров
price_litr = 0 # Цена за литр
all_rashod = 0 # Всего литров на поездку
all_price = 0 # Общая стоимость бензина

rashod_na_100_km = float(input("Введите расход топлива автомобиля на 100 км.: "))
all_km = float(input("Введите сколько километров собираетесь проехать: "))
price_litr = float(input("Сколько стоит литр бензина? "))

all_rashod = all_km / 100 * rashod_na_100_km
all_price = all_rashod * price_litr

print('Всего затратите топлива:', int(all_rashod * 100) / 100, 'л.')
print('Общая цена:', int(all_price * 100) / 100, 'руб.')
