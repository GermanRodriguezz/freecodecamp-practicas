def create_character(name,fuerza, inteligencia, carisma):
    if not isinstance(name,str):
        print('The character name should be a string')
    if not name:
        print('The character name should not contain spaces')
    if len(name) > 10 :
        print('The character anme is too lang')
    if ' ' in name :
        print('The character name should not contain spaces')
    if not isinstance(fuerza,int) or not isinstance(inteligencia,int) or not isinstance(carisma,int):
        print('All stats should be integer')
    if fuerza < 1 or inteligencia < 1 or carisma < 1:
        print('All stats should be no less than 1')
    if fuerza > 4 or inteligencia > 4 or carisma > 4:
        print('Alls stats should be no more than 4')
    if (fuerza + inteligencia + carisma) != 7:
        print('The character should start with 7 points')
        return f'{name} , {fuerza} , {inteligencia} , {carisma}'