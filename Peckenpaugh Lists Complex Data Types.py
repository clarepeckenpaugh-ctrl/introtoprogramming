print("Assignment 3")

# Problem 1: Lists, Sets, Coersion

one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
one_b = one_a.copy()
one_b[5] = one_b[5] + 3
one_c = [float(number) for number in one_b]
one_d = set(one_c)
one_d.add(10)
one_e = one_d
one_f = one_e.pop()
one_g = len(one_e)
one_h = len(one_e) == len(one_c)
one_i = list(one_e) + one_a
one_j = set(one_i)
one_k = len(one_j)

# Problem 2: Dictionary woes

two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

two_a = {
    "two_patient_dictionary_kinoko": two_patient_dictionary_kinoko,
    "two_patient_dictionary_dango": two_patient_dictionary_dango,
    "two_patient_dictionary_mochi": two_patient_dictionary_mochi
}     
two_b = two_a["two_patient_dictionary_dango"]["name"]
two_a["two_patient_dictionary_mochi"]["year"] = 2018
two_d = {
    "Kinoko": 2021, 
    "Dango": 2019,
    "Mochi": 2019
}
two_e = list(two_d.keys())

two_f = list(two_d.values())
two_g = dict(zip(two_e, two_f))

# Problem 3: Set combinations

three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

three_a = three_setE.issubset(three_setA)
three_b = three_setE < three_setA
three_c = three_setA.intersection(three_setB)
three_d = three_setC.union(three_setD, three_setE)
three_e = three_d.copy()
three_e.add(9)
three_f = three_e == one_a
three_g = "They are not the same because three_e is a set with values 1 through 9, while one_a is a list with values 0 through 9. To make the comparison True, one_a would need to be changed to a set containing exactly the values 1 through 9." 

# Problem 4: Changing variable types

four_a = 8
four_b = []
four_b.append(type(four_a))
four_c = four_b
four_d = four_a + 0.39
four_e = type(0.39)
four_b.append(four_e)
four_f = round(four_d ** -10, 0)
four_b.append(four_f)
four_g = type(four_f)
four_b.append(four_g)

# Problem 5: More variable type changes

# Continue from where you left off in Problem 4.
five_a = {
    0: four_b[0],
    1: four_b[1],
    2: four_b[2],
    3: four_b[3]
}
print(five_a)
five_b = str(four_f + 300)
five_c = type(five_b)
four_b.append(five_c)
five_d = five_b[:2]
five_e = type(five_d)
four_b.append(five_e)
five_f = [int(number) for number in five_d]
five_g = type(five_f)
four_b.append(five_g)
five_h = type(three_setA)
four_b.append(five_h)

