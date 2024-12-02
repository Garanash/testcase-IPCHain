from datetime import datetime
from typing import List


def min_operators(logs: List) -> int:
    # Если есть данные для анализа тогда проводим алгоритм
    if logs:
        # Сортировка логов по времени начала (гарантирует то что все последовательные задачи попадут к одному оператору)
        logs.sort(key=lambda x: datetime.strptime(x[5:21], '%Y-%m-%d %H:%M'))
        # Создадим первого оператора
        operators = [datetime.min]
        # Теперь каждый лог начинаем обрабатывать
        for elem in logs:
            # Узнаем для каждого лога время начала звонка и время окончания
            start = datetime.strptime(elem[5:21], "%Y-%m-%d %H:%M")
            end = datetime.strptime(elem[25:41], "%Y-%m-%d %H:%M")
            # Ставим флаг (для того что бы понимать кто-то принял звонок или нет)
            flag = False
            for i in range(len(operators)):
                """ 
                Если время начала звонка меньше или равно времени окончания звонка оператора, 
                то оператор может принять такой звонок, тогда флаг переводится в положение True (принятый)
                """
                if operators[i] <= start:
                    operators[i] = end
                    flag = True
                    break
            """ 
            Если флаг в положении False (Непринятый) 
            значит создадим еще одного оператора с временем окончания такого звонка
            """
            if not flag:
                operators.append(end)
    # Если данных для анализа нет, то и операторов не требуется:)
    else:
        operators = []
    return len(operators)


# Вычисление результата
# Открываем файл с логами для чтения
with open('test.log', 'r') as file_in:
    test_logs = file_in.readlines()
result = min_operators(test_logs)
print(f"Минимальное количество операторов: {result}")
