#Questão 03
import operator

#função que receberá as notas de cinco alunos separadamente para que, em seguida, essas notas sejam passadas por um dicionário
def studentGrade(grades):

  i = 0
  #loop para inserção das notas dos alunos
  for i in range(0,5):
    grade = float(input(f"Student {i+1} enter your note: "))

    #if-else verificadores de limites de notas (0.0 a 10.0). Caso a nota esteja fora desse intervalo, o aluno deverá reescrever uma nota correta, caso esteja dentro, a nota será adicionada ao vetor "grades"
    if(grade >= 0 and grade <= 10.0):
      grades.append(grade)

    else:
      while(grade < 0 or grade > 10.0):
        grade = float(input(f"Student {i+1} type your note correctly (0.0 - 10.0): "))
      grades.append(grade)
      print(grades)

    #iterador
    i+=1

def highestGradeStudent(students,grades):
  #criação do dicionário usando dict e zip para concatenar a key:value (students:grades)
  dictGrade = dict(zip(students,grades))
  
  #cálculo da maior nota
  higherGrade = max(dictGrade.items(), key=operator.itemgetter(1))
  #apresentação do aluno com maior nota e sua respectiva nota
  print(f"Highest grade student: {higherGrade}")

def main():
  #criação vetor com identificação dos 5 estudantes
  students = ['Student 1','Student 2', 'Student 3', 'Student 4', 'Student 5']
  #criação do vetor para armazenar as notas de cada aluno
  grades = []
  #chamada função de receber notas
  studentGrade(grades)
  #chamada função de criar dicionário e de calcular maior nota dentro do dicionário
  highestGradeStudent(students,grades)

if __name__ == "__main__":
  main()