import unittest

from testing.teste_unittest.teste_controller import suita_controller
from testing.teste_unittest.teste_domeniu import suita_domeniu
from testing.teste_unittest.teste_repository import suita_repository_file
from testing.teste_unittest.teste_validare import suita_validari


def ruleaza_toate_testele_unittest():
    suite_domain = suita_domeniu()
    suite_validating = suita_validari()
    suite_repository_file = suita_repository_file()
    suite_controller = suita_controller()

    runner = unittest.TextTestRunner()
    runner.run(suite_domain)
    runner.run(suite_validating)
    runner.run(suite_repository_file)
    runner.run(suite_controller)
