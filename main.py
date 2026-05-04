def valida_email(email):
    return email[-8:]=='@puc.com'

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': # letra.isupper()
            return True
    return False

def possuiMinuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': # letra.islower()
            return True
    return False

def possuiNumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9': 
            return True
    return False

def valida_senha(senha):
    check_tamanho = len(senha)>=8 
    check_maiuscula = possuiMaiuscula(senha)
    check_minuscula = possuiMinuscula(senha)
    check_numero = possuiNumero(senha)
    return check_tamanho and check_maiuscula and check_minuscula and check_numero


print(valida_email('theovisconti@icloud.com'))

# 1) Pegar a letra e converter para decimal ('Z'-->90)
# 2) Subtrair o valor decimal de 65 ('B' --> 90-65-->25)
# 3) somar 3 ao resultado de 2)
# 4) Obter o resto da divisão do resultado de 3) por 26 (28%26 = 2)
# 5) Somar o resto a 65 e converter valor de volta para letra (2+65--> 67 = 'C')

def cripotografa_senha(senha):
    senha_cripto = ''
    for char in senha:
        if char.isdigit(): 
            ref = ord('0') 
            ascii_char = ord(char) # Etapa 1
            pos_alpha = ascii_char - ref # Etapa 2
            pos_cesar = pos_alpha + 3 # Etapa 3 
            pos_cesar = pos_cesar % 10 # Etapa 4 
            letra_cesar = chr(pos_cesar + ref) # Etapa 5
            senha_cripto+=letra_cesar
        elif 'A' <= char <= 'Z':
            ref = ord('A') #65 
            ascii_char = ord(char) # Etapa 1
            pos_alpha = ascii_char - ref # Etapa 2
            pos_cesar = pos_alpha + 3 # Etapa 3 
            pos_cesar = pos_cesar % 26 # Etapa 4 
            letra_cesar = chr(pos_cesar + ref) # Etapa 5
            senha_cripto+=letra_cesar
        elif 'a' <= char <= 'z':
            ref = ord('a') 
            ascii_char = ord(char) # Etapa 1
            pos_alpha = ascii_char - ref # Etapa 2
            pos_cesar = pos_alpha + 3 # Etapa 3 
            pos_cesar = pos_cesar % 26 # Etapa 4 
            letra_cesar = chr(pos_cesar + ref) # Etapa 5
            senha_cripto+=letra_cesar
        else:
            senha_cripto+=char
    return senha_cripto
