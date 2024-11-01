#!/usr/bin/env python
# coding: utf-8

# S=P*(1+r/365)^t \
# A - конечная сумма вклада с процентами\
# P - начальная сумма вклада\
# r - годовая процентная ставка в десятичном виде (например, 0.05 для 5%)\
# t - количество дней, на которое размещается вклад и через которое происходит начисление процентов\

# In[1]:


import pandas as pd
stats = pd.read_csv('stats.csv') 


# In[24]:


stats


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

stats = pd.read_csv('stats.csv')

def calculate_result(principal, rate, term):
    return principal * (1 + rate/365) ** (term)

client_principal = float(input("Введите сумму вклада: "))
min_principal = stats['Минимальная сумма'].str.replace('$', '').str.replace(',', '').str.replace('₽', '').astype(float).min()

if client_principal < min_principal:
    print(f"Ошибка: Введенная сумма вклада ({client_principal:.2f}) меньше минимальной суммы ({min_principal:.2f}).")
    exit()

results = []
for _, row in stats.iterrows():
    bank = row['Банк']
    product = row['Продукт']
    rate = float(row['Эффективная ставка'].strip('%')) / 100
    min_principal = float(row['Минимальная сумма'].replace('$', '').replace(',', '').replace('₽', ''))
    term = int(row['Срок вложений'])

    if client_principal >= min_principal:
        result = calculate_result(client_principal, rate, term)
        results.append((bank, product, term, result))

results.sort(key=lambda x: x[0])

results.sort(key=lambda x: x[3], reverse=True)

print("Результаты вычислений:")
for bank, product, term, result in results:
    print(f"Банк: {bank}, Продукт: {product}, Срок вложений: {term}, Результат: {result:.2f}")


# In[5]:


import pandas as pd

stats = pd.read_csv('stats.csv')

unique_terms = stats['Срок вложений'].unique()
unique_terms.sort()
print("Отсортированные уникальные значения столбца 'Срок вложений':")
print(unique_terms)

unique_min_principals = stats['Минимальная сумма'].unique()
unique_min_principals.sort()
print("\nОтсортированные уникальные значения столбца 'Минимальная сумма':")
print(unique_min_principals)


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

stats = pd.read_csv('stats.csv')

def calculate_result(principal, rate, term):
    return principal * (1 + rate/365) ** (term)

client_principal = float(input("Введите сумму вклада: "))
client_term = int(input("Введите желаемый срок вклада в днях: "))

min_principal = stats['Минимальная сумма'].str.replace('$', '').str.replace(',', '').str.replace('₽', '').astype(float).min()

if client_principal < min_principal:
    print(f"Ошибка: Введенная сумма вклада ({client_principal:.2f}) меньше минимальной суммы ({min_principal:.2f}).")
    exit()

results = []
for _, row in stats.iterrows():
    bank = row['Банк']
    product = row['Продукт']
    rate = float(row['Эффективная ставка'].strip('%')) / 100
    min_principal = float(row['Минимальная сумма'].replace('$', '').replace(',', '').replace('₽', ''))
    term = int(row['Срок вложений'])
    
    
    if client_principal >= min_principal and term <= client_term:
        result = calculate_result(client_principal, rate, term)
        results.append((bank, product, term, result))

if not results:
    print("Ошибка: Не найдено подходящих продуктов для введенного срока вклада.")
    exit()

results.sort(key=lambda x: x[0])
results.sort(key=lambda x: x[3], reverse=True)

print("Результаты вычислений:")
for bank, product, term, result in results:
    print(f"Банк: {bank}, Продукт: {product}, Срок вложений: {term}, Результат: {result:.2f},")


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

stats = pd.read_csv('stats.csv')

def calculate_result(principal, rate, term):
    return principal * (1 + rate/365) ** (term)

client_principal = float(input("Введите сумму вклада: "))
client_term = int(input("Введите желаемый срок вклада в днях: "))

min_principal = stats['Минимальная сумма'].str.replace('$', '').str.replace(',', '').str.replace('₽', '').astype(float).min()

if client_principal < min_principal:
    print(f"Ошибка: Введенная сумма вклада ({client_principal:.2f}) меньше минимальной суммы ({min_principal:.2f}).")
    exit()

results = []
for _, row in stats.iterrows():
    bank = row['Банк']
    product = row['Продукт']
    rate = float(row['Эффективная ставка'].strip('%')) / 100
    min_principal = float(row['Минимальная сумма'].replace('$', '').replace(',', '').replace('₽', ''))
    term = int(row['Срок вложений'])
    if client_principal >= min_principal and term <= client_term:
        result = calculate_result(client_principal, rate, term)
        results.append((bank, product, term, result))

if not results:
    print("Ошибка: Не найдено подходящих продуктов для введенного срока вклада.")
    exit()

results.sort(key=lambda x: x[0])
results.sort(key=lambda x: x[3], reverse=True)

top_banks = results[:5]

banks = [bank for bank, _, _, _ in top_banks]
principal_amounts = [client_principal] * len(top_banks)
accumulation_amounts = [result - client_principal for _, _, _, result in top_banks]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(banks, principal_amounts, label='Введенный вклад', color='blue')
ax.bar(banks, accumulation_amounts, bottom=principal_amounts, label='Накопление', color='red')

ax.set_xlabel('Банк')
ax.set_ylabel('Сумма')
ax.set_title('Топ 5 банков по результатам вклада')
ax.legend()

for i, (principal, accumulation) in enumerate(zip(principal_amounts, accumulation_amounts)):
    total = principal + accumulation
    ax.text(i, total + 0.05, f'{total:.2f}', ha='center')

plt.tight_layout()
plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

stats = pd.read_csv('stats.csv')

def calculate_result(principal, rate, term):
    return principal * (1 + rate/365) ** (term)

client_principal = float(input("Введите сумму вклада: "))
client_term = int(input("Введите желаемый срок вклада в днях: "))

min_principal = stats['Минимальная сумма'].str.replace('$', '').str.replace(',', '').str.replace('₽', '').astype(float).min()

if client_principal < min_principal:
    print(f"Ошибка: Введенная сумма вклада ({client_principal:.2f}) меньше минимальной суммы ({min_principal:.2f}).")
    exit()

results = []
for _, row in stats.iterrows():
    bank = row['Банк']
    product = row['Продукт']
    rate = float(row['Эффективная ставка'].strip('%')) / 100
    min_principal = float(row['Минимальная сумма'].replace('$', '').replace(',', '').replace('₽', ''))
    term = int(row['Срок вложений'])
    frequency = int(row['Выплата процентов '])
    if client_principal >= min_principal and term <= client_term:
        result = calculate_result(client_principal, rate, term)
        profit = result - client_principal
        results.append((bank, product, term, profit))

if not results:
    print("Ошибка: Не найдено подходящих продуктов для введенного срока вклада.")
    exit()

results.sort(key=lambda x: x[0])
results.sort(key=lambda x: x[3], reverse=True)

top_banks = results[:5]

banks = [bank for bank, _, _, _ in top_banks]
terms = [term for _, _, term, _ in top_banks]
profits = [profit for _, _, _, profit in top_banks]

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(banks, profits, label='Прибыль')
ax.set_xlabel('Банк')
ax.set_ylabel('Прибыль')
ax.set_title('Топ 5 банков с максимальной прибылью за минимальный срок')
ax.legend()

plt.xticks(rotation=45, ha='right', fontsize=8)

for i, term in enumerate(terms):
    ax.text(i, profits[i], f'Срок: {term} дней', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

