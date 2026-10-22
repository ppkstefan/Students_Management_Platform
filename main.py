from Domain.problemClass import *
from Repository.repositoryStudent import RepositoryStudent
from Repository.repositoryProblem import RepositoryProblemaLaborator
from Domain.problemClass import *
from Controler.serviceStudent import ServiceStudent
from Controler.serviceProblema import ServiceProblema
from UI.ui import *
from Repository.repositoryAssignment import RepositoryAssignment
from Controler.serviceAssignment import ServiceAssignment
from Controler.serviceNota import ServiceNota
from Repository.repositoryNota import RepositoryNota

def main():
    path_to_studenti="C:\\Users\\PPK\\Desktop\\info\\python\\Fundamentele_Programarii_lab\\laborator_7-9\\studenti.txt"
    path_to_probleme="C:\\Users\\PPK\\Desktop\\info\\python\\Fundamentele_Programarii_lab\\laborator_7-9\\probleme.txt"
    path_to_assigns="C:\\Users\\PPK\\Desktop\\info\\python\\Fundamentele_Programarii_lab\\laborator_7-9\\assigns.txt"
    path_to_note="C:\\Users\\PPK\\Desktop\\info\\python\\Fundamentele_Programarii_lab\\laborator_7-9\\note.txt"

    repoStudent=RepositoryStudent(path_to_studenti)
    repoProblema=RepositoryProblemaLaborator(path_to_probleme)
    repoAssign = RepositoryAssignment(path_to_assigns, path_to_probleme, path_to_studenti)
    repoNota = RepositoryNota(path_to_note, repoAssign)

    serviceProblema=ServiceProblema(repoProblema, repoAssign, repoNota)
    serviceStudent=ServiceStudent(repoStudent, repoAssign, repoNota)
    serviceAssignment=ServiceAssignment(repoAssign, repoStudent, repoProblema)
    serviceNota = ServiceNota(repoNota, repoAssign)

    ui=UI(serviceStudent, serviceProblema, serviceAssignment, serviceNota)
    ui.start()


if __name__=='__main__':
    main()