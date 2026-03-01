import re
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(patient_id, age, gender, diagnosis, medications,last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id,str) and re.fullmatch('p\d+',patient_id, re.IGNORECASE), # Nonereemplazado por el objeto de coincidencia <re.Match object; span=(0, 1), match='P'>, donde matchindica la coincidencia e spanindica su ubicación en la cadena.
        'age' : isinstance(age,int) and age >= 18,
        'gender' : isinstance(gender,str) and (gender.lower() in ("male" ,"female")),
        'diagnosis' : isinstance(diagnosis,str) or diagnosis is None,
        'medications' : isinstance(medications,list) and all([isinstance(i,str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id,str) and re.fullmatch('v\d+',last_visit_id,re.IGNORECASE)
                                                            #agregue un +cuantificador a su patrón de expresión regular para que coincida con uno o más dígitos
        }# contendra cada clave que deberia esperar tener en los datos a validar
    # en la clave medications pregunta si el valor es una lista y con la funcion all devuelve un booleano para garantizar que cada elemento que contiene la lista es una cadena
    return [key for key,value in constraints.items() if value == False] # el retorno de esta funcion sera una lista que contenga solo claves no validas

def validate(data):
    is_sequence = isinstance(data, (list,tuple)) # is_sequence toma el valor de un booleano si es parametro "data" pertenece al tipo de dato lista o tupla
    if not is_sequence: # de no ser asi , es decir si la condicion es falsa
        print('Invalid format: expected a list or tuple')
        return False
    is_invalid = False
    key_set = set(['patient_id','age','gender','diagnosis','medications','last_visit_id']) # creo una estructura set llamada key_set que seguro luego usare para verificar si el diccionario de data tiene ese formato sin repeticion
    for index,dictionary in enumerate(data):
        if not isinstance(dictionary,dict): # si desde data el valor de dictionary no pertenece a un diccionario
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue
        if set(dictionary.keys()) != key_set: # siguiendo el comentario de arriba, verificamos si el diccionario actual (pasado a SET) es distinto al formato definido antes
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue # esta sentencia debe ir debido que si paso datos no validos como elementos que no pertenecen al diccionaro o invalidos
        invalid_records = find_invalid_records(**dictionary)
        
            
    if is_invalid :
        return False
    print('Valid format')
    return True

validate(medical_records)
print(find_invalid_records(**medical_records[0])) # imprimo lo que devuelva la funcion find y como parametro se estan pasando los elementos de un diccionario descomprimidos, se pasan las palabras claves

"""
Una expresión regular, o regex, es un patrón que se utiliza para encontrar una secuencia de caracteres en un texto. La searchfunción del remódulo toma un patrón regex y una cadena como argumentos
Devuelve un objeto coincidente si el patrón produce una coincidencia. De lo contrario, devuelve None.
"""
