def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
#ничего не выдает и ошибки нет

def inner_function():
    print("Я в области видимости функции test_function")
inner_function()

#выдет на панели 'Я в области видимости функции test_function'