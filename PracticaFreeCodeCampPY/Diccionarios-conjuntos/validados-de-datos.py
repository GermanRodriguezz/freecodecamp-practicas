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
    constraints = { 'patient_id' : isinstance(patient_id,str)} # contendra cada clave que deberia esperar tener en los datos a validar
    return constraints

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
        if set(dictionary.keys()) != key_set: # siguiendo el comentario de arriba, verificamos si el diccionario actual (pasado a SET) es distinto al formato definido antes
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
    if is_invalid :
        return False
    print('Valid format')
    return True

validate(medical_records)
print(find_invalid_records(**medical_records[0])) # imprimo lo que devuelva la funcion find y como parametro se estan pasando los elementos de un diccionario descomprimidos, se pasan las palabras claves
