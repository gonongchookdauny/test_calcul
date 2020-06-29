from django.shortcuts import render
import math
from django.views.generic.base import View
from django.http import HttpResponse


class TestCalcul(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test_calcul/test_calcul.html')

    def post(self, request, *args, **kwargs):
        template = 'test_calcul/result_section.html'
        data = request.POST

        try:
            method = data['method']
            num1 = float(data['number1'])
            num2 = float(data['number2'])
        except KeyError:
            pass
        except ValueError:
            pass

        calcul_method_list = {
            "plus": plus,
            "minus": minus,
            "multiply": multiply,
            "divide": divide,
            "divmod": divmod
        }

        calcul_method = calcul_method_list[method]
        try:
            result_val = round(calcul_method(num1, num2) , 14)
        except ZeroDivisionError as Error:
            return HttpResponse(Error, status=500)

        try:
            if result_val % 1 == 0:
                result_val = int(result_val)
        except ValueError:
            pass
        except TypeError:
            pass
        except ZeroDivisionError:
            pass
        return render(request, template, {'result_val': result_val})


def plus(number1, number2):
    result = number1 + number2
    return result

def minus(number1, number2):
    result = number1 - number2
    return result

def multiply(number1, number2):
    result = number1 * number2
    return result

def divide(number1, number2):
    result = number1 / number2
    return result

def square(number1, number2):
    result = pow(number1, number2)
    return result

def square_root(number1, number2):
    result = number1 ** (1.0/float(number2))
    return result

def logarithm(number1, number2):
    result = math.log(number1, number2)
    return result

def factorial(number1):
    result = 0
    while number1 > 0:
        result = result + number1
        number1 = number1 - 1
    return result

def divmod(number1, number2):
    result = number1 % number2
    return result

#
#
#
# def calcul(request):
#     result = ""
#     if request.method == "GET":
#         pass
#     elif request.method == "POST":
#         number1 = request.POST['number1']
#         number2 = request.POST['number2']
#         operation = request.POST['operation']
#
#         if number1:
#             number1 = int(number1)
#         else:
#             number1 = 0
#         if number2:
#             number2 = int(number2)
#         else:
#             number2 = 0
#
#         if operation == "plus":
#             result = plus(number1, number2)
#         elif operation == "minus":
#             result = minus(number1, number2)
#         elif operation == "multiply":
#             result = multiply(number1, number2)
#         elif operation == "divide":
#             result = divide(number1, number2)
#         elif operation == "square":
#             result = square(number1, number2)
#         elif operation == "square_root":
#             result = square_root(number1, number2)
#         elif operation == "logarithm":
#             result = logarithm(number1, number2)
#         elif operation == "sin":
#             result = math.sin(number1)
#         elif operation == "cosh":
#             result = math.cosh(number1)
#         elif operation == "tan":
#             result = math.tan(number1)
#         elif operation == "factorial":
#             result = factorial(number1)
#         else:
#             result = ""
#
#     return render(request, 'calcul/calcul.html', {
#         'result': result,
#     })
