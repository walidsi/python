import logging

logging.basicConfig(filename='math.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y) -> float:
    return x + y


def subtract(x, y) -> float:
    return x - y


def mult(x, y) -> float:
    return x * y


def div(x, y) -> float:
    return x / y


x = 10
y = 5

logging.debug(f'Add: {x} + {y} = {add(x, y)}')

logging.debug(f'Sub: {x} - {y} = {subtract(x, y)}')

logging.debug(f'Mult: {x} * {y} = {mult(x, y)}')

logging.debug(f'Div: {x} / {y} = {div(x, y)}')
