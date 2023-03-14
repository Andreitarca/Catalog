from testing.teste_sortari import teste_sortari
from testing.teste_unittest.teste_generale import ruleaza_toate_testele_unittest
from testing.teste_vechi.teste_controller import ruleaza_toate_testele_controller
from testing.teste_vechi.teste_domeniu import ruleaza_toate_testele_domeniu
from testing.teste_vechi.teste_file_controller import ruleaza_toate_testele_file_controller
from testing.teste_vechi.teste_file_repository import ruleaza_toate_testele_file_repository
from testing.teste_vechi.teste_repository import ruleaza_toate_testele_repository


def ruleaza_toate_testele():
    ruleaza_toate_testele_unittest()
    teste_sortari()


    #ruleaza_toate_testele_domeniu()
    #ruleaza_toate_testele_repository()
    #ruleaza_toate_testele_file_repository()
    #ruleaza_toate_testele_controller()
    #ruleaza_toate_testele_file_controller()

