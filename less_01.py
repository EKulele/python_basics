name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите возраст: "))
weight = int(input("Введите ваш вес: "))

if age <= 30:
    if weight >= 50 and weight <= 120
        print(name, surname, " - пациент в хорошем состоянии")
    else:
	    print(name, surname, " - пациенту требуется врачебный осмотр")
  
elif age > 30:
    if weight > 50 and weight < 120:
        print(name, surname, " - пациенту требуется начать вести правильный образ жизни")
    else:
        print(name, surname, " - пациенту необходимо пройти полное обследование")	
  
elif age >= 40:
    if weight > 50 and weight < 120:
        print(name, surname, " - пациенту требуется врачебный осмотр")
    else:
	    print(name, surname, " - врач удивлен, почему пациент еще жив")