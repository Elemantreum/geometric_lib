# Лабораторная работа №1 по ИСРПО
## Описание решения
### 1. Клонирование репозитория
```bash
$ git clone https://github.com/smartiqaorg/geometric_lib.
```
### 2. Создание новой ветки
``` bash
$ git branch new_features_465957
$ git checkout new_features_465957
``` 
или 
```bash
$ git checkout -b new_features_465957
``` 
*(Команды идентичны друг другу)*
### 3. Добавляем новый файл **rectangle.py**:
``` py
# rectangle.py

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return a + b 
```
### 4. Делаем коммит с сообщением о том, что добавили новый файл
``` bash
$ git add rectangle.py
$ git commit -m "added new file rectangle.py"
```
### 5. Добавляем еще один файл **triangle.py**
``` py
# triangle.py

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 
```

### 6. Исправляем ошибку в формуле периметра прямоугольника в файле **rectangle.py**
``` py
def perimeter(a, b): 
    return a + b # Неверная формула
```
->
``` py
def perimeter(a, b): 
    return (a + b)*2 # Верная формула
```
### 7. Делаем коммит о том, что исправлена ошибка
``` bash
$ git commit -m "fixed perimeter function in rectangle.py"
```
### 8. Строим граф всего репозитория с однострочным выводом коммитов
``` shell
$ git log --all --pretty=oneline --graph
```
``` shell
* 0046072e86f59c8b3711275f18ca574ca1830341 (HEAD -> new_features_465957, origin/new_features_465957) fixed permiter() in rectangle.py
* 7494640a0514dd98e061d6aa028118ce3d85bc98 new file added
* d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```
### 9. Построим граф истории только текущей ветки
```
$ git log --pretty=oneline --graph main..new_feature
```
```bash
* 0046072e86f59c8b3711275f18ca574ca1830341 (HEAD -> new_features_465957, origin/new_features_465957) fixed permiter() in rectangle.py
* 7494640a0514dd98e061d6aa028118ce3d85bc98 new file added
* d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
```

### 10. Берем хеши двух последних комиитов и выполняем
```
$ git diff 7494640a0514dd98e061d6aa028118ce3d85bc98 0046072e86f59c8b3711275f18ca574ca1830341
```
``` bash
diff --git a/rectangle.py b/rectangle.py
index beed4b8..90e717a 100644
--- a/rectangle.py
+++ b/rectangle.py
@@ -2,4 +2,4 @@ def area(a, b):
     return a * b

 def perimeter(a, b):
-    return a + b
\ No newline at end of file
+    return (a + b)*2
\ No newline at end of file
diff --git a/triangle.py b/triangle.py
new file mode 100644
index 0000000..49864a2
--- /dev/null
+++ b/triangle.py
@@ -0,0 +1,5 @@
+def area(a, h):
+    return a * h / 2
+
+def perimeter(a, b, c):
+    return a + b + c
```

### 11. Cоздаем new_features_465957_test из new_features_465957
```bash
git chechout -b new_features_465957_test
```
### 12. Удаляем только что созданную ветку
```
git branch -d new_features_465957_test
```
### 13. Защищаем лабу и лутаем баллы!
![](ITMO_is_proud.jpg)


# Описание функций


# circle.py
## Функция нахождения площади окружности **area()**:

#### Параметры:
- r - Радиус окружности

#### Принцип работы:
- S = Пи*r^2

#### Возвращаемые значения:
- S - Площадь окружности

``` py
def area(r):
    return math.pi * r * r
```
### Примеры вызова функции
```
area(3)
area(5)
area(10)

>> 28.27 78.54 314.16
```



## Функция нахождения длины окружности **perimeter()**:

#### Параметры:
- r - Радиус окружности

#### Принцип работы:
- C = 2*Пи*r

#### Возвращаемые значения:
- С - Длина окружности
``` py
def perimeter(r):
    return 2 * math.pi * r
```
### Примеры вызова функции
```
perimeter(3)
perimeter(5)
perimeter(10)

>> 18.84 31.41 62.83
```




# rectangle.py
## Функция нахождения площади прямоугольника **area()**:

#### Параметры:
- a - Сторона прямоугольника
- b - Другая сторона прямоугольника *(не противоположная)*

#### Принцип работы:
- S = a*b

#### Возвращаемые значения:
- S - Площадь прямоугольника

``` py
def area(a,b):
    return a * b
```
### Примеры вызова функции
```
area(7,19)
area(10,20)
area(20,40)

>> 133 200 800
```

## Функция нахождения периметра прямоугольника **perimeter()**:

#### Параметры:
- a - Сторона прямоугольника
- b - Другая сторона прямоугольника *(не противоположная)*

#### Принцип работы:
- P = (a+b)*2

#### Возвращаемые значения:
- P - Периметр прямоугольника
``` py
def perimeter(a, b): 
    return (a + b)*2 
```
### Примеры вызова функции
```
perimeter(3,5)
perimeter(5,10)
perimeter(10,20)

>> 16 30 60
```



# square.py
## Функция нахождения площади квадрата **area()**:

#### Параметры:
- a - Сторона квадрата

#### Принцип работы:
- S = a*a

#### Возвращаемые значения:
- S - Площадь квадрата

``` py
def area(a):
    return a * a
```
### Примеры вызова функции
```
area(7)
area(10)
area(20)

>> 49 100 400
```



## Функция нахождения периметра квадрата **perimeter()**:

#### Параметры:
- a - Сторона квадрата

#### Принцип работы:
- P = 4*a

#### Возвращаемые значения:
- P - Периметр квадрата
``` py
def perimeter(a):
    return 4 * a
```
### Примеры вызова функции
```
perimeter(3)
perimeter(5)
perimeter(10)

>> 12 20 40
```

# triangle.py
## Функция нахождения площади треугольника **area()**:

#### Параметры:
- a - Основание треугольника
- h - Высота проведенная к основанию a

#### Принцип работы:
- S = a * h / 2 

#### Возвращаемые значения:
- S - Площадь треугольника

``` py
def area(a, h): 
    return a * h / 2 
```
### Примеры вызова функции
```
area(7,2)
area(10,3)
area(20,30)

>> 7 15 30
```


## Функция нахождения периметра треугольника **perimeter()**:

#### Параметры:
- a - 1 Сторона треугольника
- b - 2 Сторона треугольника
- c - 3 Сторона треугольника

#### Принцип работы:
- P = a + b + c 

#### Возвращаемые значения:
- P - Периметр треугольника
``` py
def perimeter(a, b, c): 
    return a + b + c 
```
### Примеры вызова функции
```
perimeter(3,3,3)
perimeter(5,10,5)
perimeter(10,20,10)

>> 9 20 40
```


# История изменений
```
commit 0046072e86f59c8b3711275f18ca574ca1830341 (HEAD -> new_features_465957, origin/new_features_465957)
Author: Kirill Zgurskiy <kirillzg@yandex.ru>
Date:   Wed Sep 18 12:56:42 2024 +0300

    fixed permiter() in rectangle.py

commit 7494640a0514dd98e061d6aa028118ce3d85bc98
Author: Kirill Zgurskiy <kirillzg@yandex.ru>
Date:   Wed Sep 18 12:50:52 2024 +0300

    new file added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300
```
