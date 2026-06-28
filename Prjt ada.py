import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# ========== Генерация данных ==========
schools = ['Лицей 19', 'Лицей 8', 'Лицей 34']

params = {
    'План эвакуации': (0, 1),
    'Кол-во огнетушителей': (10, 30),
    'Система оповещения': (0, 1),
    'Кол-во аварийных выходов': (0, 2),
    'Обученный персонал': (0, 1),
    'Состояние здания': (0, 5),
    'Состояние средств пожаротушения': (0, 5),
    'Кол-во учащихся': (800, 1000)
}

max_scores = {
    'План эвакуации': 1,
    'Кол-во огнетушителей': 30,
    'Система оповещения': 1,
    'Кол-во аварийных выходов': 2,
    'Обученный персонал': 1,
    'Состояние здания': 5,
    'Состояние средств пожаротушения': 5
}
total_max = sum(max_scores.values())

data = []
for school in schools:
    row = {'Учреждение': school}
    for attr, (low, high) in params.items():
        row[attr] = random.randint(low, high)
    data.append(row)

df = pd.DataFrame(data)

criteria_cols = list(max_scores.keys())
df['Суммарный балл'] = df[criteria_cols].sum(axis=1)
df['Оценка готовности, %'] = (df['Суммарный балл'] / total_max * 100).round(1)

# ========== Визуализация ==========
plt.style.use('ggplot')
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# График 1: Интегральная оценка готовности
ax1 = axes[0]
bars = ax1.bar(df['Учреждение'], df['Оценка готовности, %'], color=['#2ecc71', '#3498db', '#e67e22'])
ax1.set_ylim(0, 105)
ax1.set_ylabel('Готовность, %')
ax1.set_title('Интегральная оценка готовности к ЧС')
ax1.bar_label(bars, fmt='%.1f%%', padding=3)

# Добавим горизонтальную линию среднего
avg = df['Оценка готовности, %'].mean()
ax1.axhline(y=avg, color='red', linestyle='--', label=f'Среднее: {avg:.1f}%')
ax1.legend()

# График 2: Нормированные показатели по каждому критерию
# Нормируем каждый признак (кроме учащихся) к максимуму
norm_data = df[criteria_cols].copy()
for col in criteria_cols:
    norm_data[col] = norm_data[col] / max_scores[col]

# Добавим также кол-во учащихся (нормируем на максимум 1000)
norm_data['Кол-во учащихся'] = df['Кол-во учащихся'] / 1000

# Переименуем столбцы для красоты на графике
rename_map = {
    'План эвакуации': 'План\nэвакуации',
    'Кол-во огнетушителей': 'Огнетушители',
    'Система оповещения': 'Оповещение',
    'Кол-во аварийных выходов': 'Аварийные\nвыходы',
    'Обученный персонал': 'Обученный\nперсонал',
    'Состояние здания': 'Состояние\nздания',
    'Состояние средств пожаротушения': 'Состояние\nпожаротушения',
    'Кол-во учащихся': 'Кол-во\nучащихся'
}
norm_data.rename(columns=rename_map, inplace=True)

x = np.arange(len(rename_map))  # количество признаков
width = 0.25
ax2 = axes[1]

for i, school in enumerate(schools):
    values = norm_data.loc[i, list(rename_map.values())]
    offset = (i - 1) * width
    ax2.bar(x + offset, values, width, label=school)

ax2.set_xticks(x)
ax2.set_xticklabels(list(rename_map.values()), fontsize=8)
ax2.set_ylabel('Нормированный показатель (0–1)')
ax2.set_title('Сравнение по критериям (нормировано)')
ax2.legend()
ax2.set_ylim(0, 1.1)

plt.tight_layout()
plt.show()

# ========== Анализ в консоли ==========
print("\nОценка готовности образовательных учреждений к ЧС\n")
print(df[['Учреждение'] + criteria_cols + ['Суммарный балл', 'Оценка готовности, %']].to_string(index=False))
print("\n--- Анализ ---")
best = df.loc[df['Оценка готовности, %'].idxmax()]
print(f"Лучшая готовность: {best['Учреждение']} – {best['Оценка готовности, %']}%")
worst = df.loc[df['Оценка готовности, %'].idxmin()]
print(f"Худшая готовность: {worst['Учреждение']} – {worst['Оценка готовности, %']}%")
print(f"Средняя готовность: {df['Оценка готовности, %'].mean():.1f}%")