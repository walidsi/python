import logging

logging.basicConfig(filename='employee.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        logging.debug(f'Created employee: {self.first} - {self.last} - {self.email}')

    @property
    def email(self) -> str:
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def fullname(self) -> str:
        return f'{self.first.capitalize()} {self.last.capitalize()}'


emp1 = Employee('John', 'Smith')
emp2 = Employee('Todd', 'Bailey')
