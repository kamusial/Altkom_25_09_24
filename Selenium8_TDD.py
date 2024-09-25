def mnozenie(x, y):
    return round(x * y, 5)


def fizzbuzz(number):
    try:
        number = int(number)
        if number > 0:
            if number % 3 == 0 and number % 5 == 0:
                return 'FissBuzz'
            if number % 3 == 0:
                return 'Fiss'
            elif number % 5 == 0:
                return 'Buzz'
            return number
        return None
    except:
        return None