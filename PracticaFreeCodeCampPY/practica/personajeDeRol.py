full_dot = '●'
empty_dot = '○'

def create_character(name,fuerza, inteligencia, carisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if not name:
        return'The character should have a name'
    if len(name) > 10 :
        return 'The character name is too long'
    if ' ' in name :
        return 'The character name should not contain spaces'
    if not isinstance(fuerza,int) or not isinstance(inteligencia,int) or not isinstance(carisma,int):
        return 'All stats should be integers'
    if fuerza < 1 or inteligencia < 1 or carisma < 1:
        return 'All stats should be no less than 1'
    if fuerza > 4 or inteligencia > 4 or carisma > 4:
        return 'All stats should be no more than 4'
    if (fuerza + inteligencia + carisma) != 7:
        return 'The character should start with 7 points'
    
    str_line = f'STR {full_dot * fuerza}{empty_dot *(10 - fuerza)}'
    int_line = f'INT {full_dot * inteligencia}{empty_dot * (10-inteligencia)}'
    char_line = f'CHA {full_dot * carisma}{empty_dot * (10-carisma)}'

    return f"{name}\n{str_line}\n{int_line}\n{char_line}"

    
create_character('ren',4,2,1)