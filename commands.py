import redis
import time

""" Запускаем контейнер в Docker командой docker run -p 6379:6379 -d redis
Порт смотрим в Kitematic. За адрес отвечает VirtualBox. В PyCharm - install redis"""

my_db = redis.Redis(host='192.168.99.100', port=6379)

"""Типы данных Redis
1. Строки
2. Списки
3. Множества
4. Хеш-таблицы
5. Упорядоченные множества"""

"""Базовые операции"""

# my_db.set('test:1:string', 'Python')  # задаем значение
# print(my_db.get('test:1:string'))  # получаем значение
# print(my_db.type('test:1:string'))  # определяем тип значения
# print(my_db.exists('test:1:string'))  # проверка существования значения с данным ключом
# print(my_db.getset('test:1:string', 'JavaScript'))  # возвращает текущее значение и устанавливает новое
# print(my_db.rename('test:1:string', 'test:2:string'))  # переименование ключа
# print(my_db.keys('test:*:string'))  # все ключи из базы по указанному шаблону
# print(my_db.delete('test:2:string'))  # удаление записи по ключу
# print(my_db.exists('test:2:string'))  # проверка существования значения с данным ключом
#
# my_db.set('test:2:string', 'Hello')  # задаем значение
# print(my_db.expire('test:2:string', 3))  # задаем срок действия
# print(my_db.ttl('test:2:string'))  # начинаем отсчитывать время
# time.sleep(1)
# print(my_db.ttl('test:2:string'))
# time.sleep(1)
# print(my_db.ttl('test:2:string'))
# time.sleep(1)
# print(my_db.ttl('test:2:string'))
# time.sleep(1)
# print(my_db.ttl('test:2:string'))
# time.sleep(1)
# print(my_db.ttl('test:2:string'))

"""Операции над строками"""
# my_db.set('test:1:string', 'Hello')  # задаем значение
# my_db.append('test:1:string', ' world!')  # добавляем в соотвествующий ключ дополнительное значение
# print(my_db.get('test:1:string').decode("utf-8"))  # получаем значение /
# # Добавляем decode("utf-8"), чтобы избавиться от b при выводе в консоль
# print(my_db.strlen('test:1:string')) # определяем длину строки
# print(my_db.getrange('test:1:string' , 6, 10)) # делаем срез сроки
# print(my_db.setrange('test:1:string' , 6, 'Python')) # замена части строки начиная с указанной позиции
# print(my_db.get('test:1:string'))

"""Операции с числами"""
# my_db.set('test:1:int', 1)  # задаем значение
# print(my_db.incr('test:1:int'))  # увеличиваем значение на 1
# print(my_db.decr('test:1:int'))  # уменьшаем значение на 1
# print(my_db.get('test:1:int'))  # получаем значение. Снова 1
# print(my_db.incrby('test:1:int', 100))  # произвольное увеличение значения
# print(my_db.decrby('test:1:int', 50))  # произвольное уменьшение значения

"""Операции со списками"""
# my_db.delete('test:1:list')
# my_db.lpush('test:1:list', 'Python') # добавление значения элемента в список слева
# my_db.lpush('test:1:list', 'JavaScript') # добавление значения элемента в список слева
# my_db.rpush('test:1:list', 'Go') # добавление значения элемента в список справа
# print(my_db.llen('test:1:list')) # определение длины списка
# print(my_db.lrange('test:1:list', 0, -1)) # вывод всех элементов списка
# print(my_db.lpop('test:1:list')) # вернуть одно значение c левой стороны и удалить его из списка
# print(my_db.rpop('test:1:list')) # вернуть одно значение c правой стороны и удалить его из списка

"""Операции с множествами"""
# my_db.delete('test:1:set')
# my_db.delete('test:2:set')
# my_db.sadd('test:1:set', 'Python')  # добавляем новые элементы к первому множеству (аналог set в Python)
# my_db.sadd('test:1:set', 'JavaScript')
# my_db.sadd('test:1:set', 'Go')
# my_db.sadd('test:1:set', 'Ruby')
# my_db.sadd('test:1:set', 'PHP')
# my_db.sadd('test:2:set', 'Python')  # добавляем новые элементы ко второму множеству
# my_db.sadd('test:2:set', 'Java')
# my_db.sadd('test:2:set', 'C++')
# my_db.sadd('test:2:set', 'Ruby')
# print(my_db.smembers('test:1:set'))
# print(my_db.smembers('test:2:set'))  # получение всех элементов множества
# print(my_db.scard('test:1:set'))  # подсчет элементов
# print(my_db.sismember('test:1:set', 'Python'))  # проверка на вхождение в множество
# print(my_db.srem('test:1:set', 'Python'))  # удаление элемента из набора
# print(my_db.sunion('test:1:set', 'test:2:set'))  # объединение множеств
# print(my_db.sdiff('test:1:set', 'test:2:set'))  # вычитание из первого множества второго
# print(my_db.sinter('test:1:set', 'test:2:set'))  # возвращает общие элементы указаных множеств

"""Операции с упорядоченными множествами"""
# my_db.delete('test:1:zset')
# zdict = {}
# zdict['Python'] = 2
# zdict['Go'] = 4
# zdict['JavaScript'] = 1
# zdict['Java'] = 3
# my_db.zadd('test:1:zset', zdict)
# print(my_db.zrange('test:1:zset', 0, -1))

"""Операции с хеш-таблицами"""
# my_db.hset('project:1', 'client', 'Alfa')
# my_db.hset('project:1', 'status', 'work')
# my_db.hset('project:2', 'client', 'Omera')
# my_db.hset('project:2', 'status', 'start')
# print(my_db.hkeys('project:1')) # получаем ключи по первому проекту
# print(my_db.hvals('project:1')) # получаем значения по первому проекту
# print(my_db.hgetall('project:1')) # получаем словарь

