# testcase-IPCHain

## Задание:

Есть лог звонков call-центра. В нем зафиксировано время начала и конца звонка.
Количество записей в логе может быть очень большим.

Нужно написать эффективный по использованию памяти скрипт который сможет определить минимальное количестов операторов
call-центра, чтобы ни один звонок не ожидал оператора.

### Формат лога приблизительно такой

```log
FROM:2021-01-30 22:18 TO:2021-01-30 22:31
FROM:2021-02-04 00:46 TO:2021-02-04 00:53
FROM:2021-01-29 18:46 TO:2021-01-29 19:02
FROM:2021-02-02 17:02 TO:2021-02-02 17:09
FROM:2021-01-30 15:44 TO:2021-01-30 16:05
FROM:2021-02-05 11:58 TO:2021-02-05 12:14
FROM:2021-02-01 00:29 TO:2021-02-01 00:45
FROM:2021-01-31 02:59 TO:2021-01-31 03:11
FROM:2021-02-02 15:06 TO:2021-02-02 15:17
FROM:2021-01-28 20:58 TO:2021-01-28 21:26
FROM:2021-02-03 23:29 TO:2021-02-03 23:48
FROM:2021-02-06 13:55 TO:2021-02-06 14:19
FROM:2021-01-31 04:41 TO:2021-01-31 04:53
FROM:2021-02-01 18:45 TO:2021-02-01 19:00
FROM:2021-01-28 13:29 TO:2021-01-28 13:49
```

### Генерировать для теста его можно как то так

```python
from datetime import datetime, timedelta
from random import randint

for i in range(15):
    rand_time = datetime.now() - timedelta(seconds=randint(0, 1000000))
    start_dt = datetime.strftime(rand_time - timedelta(seconds=randint(0, 1000)), "%Y-%m-%d %H:%M")
    end_dt = datetime.strftime(rand_time + timedelta(seconds=randint(0, 1000)), "%Y-%m-%d %H:%M")

    print(f"FROM:{start_dt} TO:{end_dt}")
```

## Решение и запуск

Для запуска программы: склонируйте репозиторий.  
Запустите генератор логов, он автоматически создаст файл test.log с 1000 записей логов
После этого можно запускать testcase.py, он уже выдает ответ на задачу

```bash
git clone https://github.com/Garanash/testcase-IPCHain.git new_prog
cd new_prog
python log_generator.py
python testcase.py
```