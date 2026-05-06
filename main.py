from pygame import *
import sys

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

init()

window = display.set_mode((1280,720))
running = True
clock = time.Clock()
texto = font.Font(None, 25)

email = '' 
emailescrito = texto.render(email,True, (255,255,255))
senha = ''
senhaescrita = texto.render(senha,True,(255,255,255))
limpa = False

while running:
    clock.tick(60)

    ##UPDATE

    dt = clock.get_time()/1000
    keys = key.get_pressed()


    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            if ev.key == K_BACKSPACE:
                email=email[:-1]
                emailescrito=texto.render(email, True, (255,255,255))
            if ev.key == K_RETURN:
                print(email)
                valida_email(email)
                if valida_email(email) == True: #Se o email for valido, passar para a senha
                    limpa = True
                    email = ''
                if ev.key == K_BACKSPACE:
                    senha=senha[:-1]
                    senhaescrita=texto.render(senha,True, (255,255,255))
                if ev.key == K_RETURN:
                    print(senha)
                if ev.type == TEXTINPUT:
                    senha += ev.text
                    senhaescrita = texto.render(senha, True, (255,255,255))
                    window.blit(senhaescrita,(310,350))

            
                
                
        if ev.type == TEXTINPUT:
            email += ev.text
            emailescrito = texto.render(email, True, (255,255,255))

    window.fill((0,0,0))

    draw.rect(window, (255, 255, 255), (300,300,500,100), 4)
    escrito = texto.render('Email:', True , (255,255,255))
    window.blit(escrito, (310,310))
    window.blit(emailescrito,(310,350))
    


    if limpa == True: #Para limpar tudo, o retangulo que cobre tem que ser desenhado fora do ev.key
        draw.rect(window,(0,0,0), (0,0,1280,720))
        draw.rect(window, (255, 255, 255), (300,300,500,100), 4)
        escrito = texto.render('Senha:', True , (255,255,255)) #Pedindo senha
        window.blit(escrito,(310,310))
        
        

        


    display.update()