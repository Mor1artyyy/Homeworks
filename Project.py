import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)

n_students = 30

kr1 = np.random.randint(2, 5,  n_students)
kr2 = np.random.randint(2, 5, n_students)
kr3 = np.random.randint(2, 5, n_students)

real_final = (kr1 + kr2 + kr3) / 3 + np.random.normal(0, 3, n_students)
real_final = np.clip(real_final, 2, 5)

predicted_final = (kr1 + kr2 + kr3) / 3

df = pd.DataFrame({
    "Ученик" : range(1, n_students + 1),
    "КР 1:" : kr1,
    "КР 2:" : kr2,
    "КР 3:" : kr3,
    "Реальный итог" : np.round(real_final, 2),
    "Прогноз (скользящая средняя)" : np.round(predicted_final, 2),
    "Ошибка прогноза" : np.round(real_final - predicted_final, 2)
})
print("=" * 70)
print("Таблица результатов прогнозирования итогового балла по курсу БДЖ:")
print("=" * 70)
print(df.to_string(index=False))

plt.figure(figsize=(10, 6))
plt.plot(df['Ученик'], df['Реальный итог'], 'o-', label='Реальный итоговый балл', color='blue')
plt.plot(df['Ученик'], df['Прогноз (скользящая средняя)'], 's--', label='Прогноз (скользящая средняя)', color='red')
plt.xlabel('Номер ученика')
plt.ylabel('Баллы')
plt.title('Сравнение реальных и прогнозных итоговых баллов (БЖД)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(8, 4))
plt.hist(df['Ошибка прогноза'], bins=10, edgecolor='black', alpha=0.7, color='green')
plt.xlabel('Ошибка прогноза (реальный - прогноз)')
plt.ylabel('Количество учеников')
plt.title('Распределение ошибок прогнозирования')
plt.axvline(x=0, color='red', linestyle='--', label='Нулевая ошибка')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

mae = np.mean(np.abs(df["Ошибка прогноза"]))
print(f"\nСредняя абсолютная ошибка (МАЕ) прогноза: {mae:.2f} баллов")