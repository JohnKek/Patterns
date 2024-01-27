from __future__ import annotations
from abc import ABC, abstractmethod


# Iterface
class Developer(ABC):
    @abstractmethod
    def write_code(self):
        pass


class JavaDeveloper(Developer):
    def write_code(self):
        print("Write Java Code")


class PythonDeveloper(Developer):
    def write_code(self):
        print("Write Python Code")


class DeveloperFactory(ABC):
    @abstractmethod
    def create_developer(self) -> Developer:
        return Developer()


class JavaFactory(DeveloperFactory):
    def create_developer(self) -> Developer:
        return JavaDeveloper()


class PythonFactory(DeveloperFactory):
    def create_developer(self) -> Developer:
        return PythonDeveloper()


def create_factory_by_speciality(speciality):
    if speciality == 'python':
        return PythonFactory()
    elif speciality == 'java':
        return JavaFactory()


if __name__ != '':
    factory = create_factory_by_speciality('java')
    developer = factory.create_developer()
    developer.write_code()
    factory = create_factory_by_speciality('python')
    developer = factory.create_developer()
    developer.write_code()
