##Проверка, являеться ли введенное значение числом (положительным, беззнаковым).
def isdigit(string):
    if string.isdigit(): 
            return True
    else:
            return False

##Проверка, условия что Координаты заданы не более чем с шестью знаками после точки.


def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0



##Задание №1
def zadanie1(string):
    if isdigit(string) == True:
        i = int(string)
        print(i % 10)                                   ##Остаток от деления на 10
    else:
        print("Введено неверное значение")


##Задание №2
## проверка на условия:
# введенное значение число вещественное 
# - y (−1000≤x, y≤1000)(−1000≤x, y≤1000),
# - Координаты заданы не более чем с шестью знаками после точки.

def zadanie2(string):
  ## проверка значения вставить на float  
    x, y = map(float, string.split())
    if (get_count(x)<=6 and get_count(y)<=6 and get_count(x)>=0 and get_count(y)>=0):
        if ((x*x+y*y>=4) and (y>=0) and (y<=x) and (x<=2)):
            return print("YES")
        else: 
            return print("NO")
    else:
        return print("Значение x или y содержит больше шести знаков после запятой")

print("Проверка Задание 1:")
zadanie1 ("560")
zadanie1 ("234")
zadanie1 ("560")
zadanie1 ("8521")
zadanie1 ("244565482")
zadanie1 ("3")
zadanie1 ("234")
zadanie1 ("7324615")
zadanie1 ("5666")
zadanie1 ("9907")
zadanie1 ("1345678")
zadanie1 ("9")

print("Проверка Задание 2:")
zadanie2 ("1.802 1.406")
zadanie2 ("1.012 -1.234")
zadanie2 ("-2 -2")
zadanie2 ("-1 -1")
zadanie2 ("-1 -0.5")
zadanie2 ("-2 -1")
zadanie2 ("0.5 -1")
zadanie2 ("0.5 -3")
zadanie2 ("1 3")
zadanie2 ("1 1.1")
zadanie2 ("1 0.5")
zadanie2 ("1 -1")
zadanie2 ("1 -3")
zadanie2 ("1.9 1.5")
zadanie2 ("2.5 3")
zadanie2 ("2.5 2")
zadanie2 ("2.5 -1")
zadanie2 ("2.977 0.689")
zadanie2 ("-2.985 -2.152")
zadanie2 ("1.88 -1.404")
zadanie2 ("-1.669 1.756")
zadanie2 ("-2.805 2.503")
zadanie2 ("-2.766 2.076")
zadanie2 ("2.099 -2.966")
zadanie2 ("0.963 -2.218")
zadanie2 ("-2.586 0.942")
zadanie2 ("-1.089 0")
zadanie2 ("1.467 1.609")
zadanie2 ("1.851 1.313")
zadanie2 ("1.979 1.638")
zadanie2 ("1.634 1.342")
zadanie2 ("1.762 1.666")
zadanie2 ("1.545 1.752")
zadanie2 ("1.673 1.464")
zadanie2 ("1.801 1.789")
zadanie2 ("1.456 1.493")
zadanie2 ("1.912 1.442")
print(get_count(193.1))
