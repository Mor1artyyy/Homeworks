import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Устанавливаем seed для воспроизводимости
np.random.seed(42)

# Количество учеников
n_students = 30

# Генерация оценок за пять контрольных работ (0-100 баллов)
kr1 = np.random.randint(2, 5, n_students)
kr2 = np.random.randint(2, 5, n_students)
kr3 = np.random.randint(2, 5, n_students)
kr4 = np.random.randint(2, 5, n_students)   # не влияет на прогноз
kr5 = np.random.randint(2, 5, n_students)   # не влияет на прогноз

# Реальный итоговый балл: зависит от ВСЕХ пяти КР (среднее + шум)
real_final = (kr1 + kr2 + kr3 + kr4 + kr5) / 5 + np.random.normal(0, 3, n_students)
real_final = np.clip(real_final, 2, 5)

# Прогноз методом скользящей средней ТОЛЬКО по первым трём КР
predicted_final = (kr1 + kr2 + kr3) / 3

# Формируем DataFrame
df = pd.DataFrame({
    'Ученик': range(1, n_students + 1),
    'КР1': kr1,
    'КР2': kr2,
    'КР3': kr3,
    'КР4': kr4,   # добавлена, но не используется в прогнозе
    'КР5': kr5,   # добавлена, но не используется в прогнозе
    'Реальный итог': np.round(real_final, 2),
    'Прогноз (по КР1-3)': np.round(predicted_final, 2),
    'Ошибка прогноза': np.round(real_final - predicted_final, 2)
})

# Вывод таблицы
print('======================================================================')
print("Таблица результатов прогнозирования (прогноз только по первым трём КР)")
print('======================================================================')
print(df.to_string(index=False))

# Визуализация: сравнение прогноза и реального итога
plt.figure(figsize=(10, 6))
plt.plot(df['Ученик'], df['Реальный итог'], 'o-', label='Реальный итоговый балл (по 5 КР)', color='blue')
plt.plot(df['Ученик'], df['Прогноз (по КР1-3)'], 's--', label='Прогноз (скользящая средняя по КР1-3)', color='red')
plt.xlabel('Номер ученика')
plt.ylabel('Баллы')
plt.title('Сравнение реальных и прогнозных итоговых баллов (БЖД)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Гистограмма ошибок прогноза
plt.figure(figsize=(8, 4))
plt.hist(df['Ошибка прогноза'], bins=10, edgecolor='black', alpha=0.7, color='green')
plt.xlabel('Ошибка прогноза (реальный - прогноз)')
plt.ylabel('Количество учеников')
plt.title('Распределение ошибок прогнозирования')
plt.axvline(x=0, color='red', linestyle='--', label='Нулевая ошибка')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Вывод средней абсолютной ошибки
mae = np.mean(np.abs(df['Ошибка прогноза']))
print(f"\nСредняя абсолютная ошибка (MAE) прогноза: {mae:.2f} баллов")