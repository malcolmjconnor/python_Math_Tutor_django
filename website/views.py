from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'home.html', {})

def add (request):
    from random import randint

    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        oldnum1 = request.POST['oldnum1']
        oldnum2 = request.POST['oldnum2']

        # Error handling if no answer
        if not answer:
            my_answer = 'Hey, you did not enter anything.  Try again.'
            color = 'warning'

            return render(request, 'add.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

        correct = int(oldnum1) + int(oldnum2)
        if int(answer) == correct:
            my_answer = "Correct! " + oldnum1 + " + " + oldnum2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + oldnum1 + " + " + oldnum2 + " = " + str(correct) + ", not " + answer
            color = "danger"

        return render(request, 'add.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

    return render(request, 'add.html', {
        'num1':num1,
        'num2':num2,
    })

def subtract (request):
    from random import randint

    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        oldnum1 = request.POST['oldnum1']
        oldnum2 = request.POST['oldnum2']

        # Error handling if no answer
        if not answer:
            my_answer = 'Hey, you did not enter anything.  Try again.'
            color = 'warning'

            return render(request, 'subtract.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

        correct = int(oldnum1) - int(oldnum2)
        if int(answer) == correct:
            my_answer = "Correct! " + oldnum1 + " - " + oldnum2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + oldnum1 + " - " + oldnum2 + " = " + str(correct) + ", not " + answer
            color = "danger"

        return render(request, 'subtract.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

    return render(request, 'subtract.html', {
        'num1':num1,
        'num2':num2,
    })

def multiply (request):
    from random import randint

    num1 = randint(0,10)
    num2 = randint(0,10)

    if request.method == "POST":
        answer = request.POST['answer']
        oldnum1 = request.POST['oldnum1']
        oldnum2 = request.POST['oldnum2']

        # Error handling if no answer
        if not answer:
            my_answer = 'Hey, you did not enter anything.  Try again.'
            color = 'warning'

            return render(request, 'multiply.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

        correct = int(oldnum1) * int(oldnum2)
        if int(answer) == correct:
            my_answer = "Correct! " + oldnum1 + " x " + oldnum2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + oldnum1 + " x " + oldnum2 + " = " + str(correct) + ", not " + answer
            color = "danger"

        return render(request, 'multiply.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

    return render(request, 'multiply.html', {
        'num1':num1,
        'num2':num2,
    })

def divide (request):
    from random import randint

    num1 = randint(0,10)
    num2 = randint(1,10)

    if request.method == "POST":
        answer = request.POST['answer']
        oldnum1 = request.POST['oldnum1']
        oldnum2 = request.POST['oldnum2']

        # Error handling if no answer
        if not answer:
            my_answer = 'Hey, you did not enter anything.  Try again.'
            color = 'warning'

            return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })


        correct = int(oldnum1) / int(oldnum2)
        if float(answer) == correct:
            my_answer = "Correct! " + oldnum1 + " / " + oldnum2 + " = " + answer
            color = "success"
        else:
            my_answer = "Incorrect! " + oldnum1 + " / " + oldnum2 + " = " + str(correct) + ", not " + answer
            color = "danger"

        return render(request, 'divide.html', {
            'answer':answer,
            'my_answer':my_answer,
            'num1':num1,
            'num2':num2,
            'color':color,
            })

    return render(request, 'divide.html', {
        'num1':num1,
        'num2':num2,
    })