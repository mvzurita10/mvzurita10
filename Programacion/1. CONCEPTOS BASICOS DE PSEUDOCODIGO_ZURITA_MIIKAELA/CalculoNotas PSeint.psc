Algoritmo CalculoNotas
    Definir nota1, nota2, nota3, promedio Como Real
    Definir nombre Como Cadena
	
    Escribir "Ingrese el nombre del estudiante: "
    Leer nombre
	
    Escribir "Ingrese la primera nota: "
    Leer nota1
    Escribir "Ingrese la segunda nota: "
    Leer nota2
    Escribir "Ingrese la tercera nota: "
    Leer nota3
	
    promedio = (nota1 + nota2 + nota3) / 3
	
    Escribir "----------------------------"
    Escribir "Estudiante: ", nombre
    Escribir "Notas ingresadas: ", nota1, ", ", nota2, ", ", nota3
    Escribir "Promedio: ", promedio
	
    Si promedio >= 7 Entonces
        Escribir "Estado: Aprobado"
    Sino
        Escribir "Estado: Reprobado"
    FinSi
FinAlgoritmo
