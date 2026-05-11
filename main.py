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
escreva_senha = False
email_invalido = False 
senha_invalida = False
casita = False
nuvem_x = 300
nuvem_y = 75    
background_color = (152, 209, 250)
indo_direita = 0
estado = 0
sol_x = 70
sol_y = 70


while running:
    clock.tick(60)

    ##UPDATE

    dt = clock.get_time()/1000
    keys = key.get_pressed()


    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            if escreva_senha == False:

                if ev.key == K_BACKSPACE:
                    email=email[:-1]
                    emailescrito=texto.render(email, True, (255,255,255))
                if ev.key == K_RETURN:
                    valida_email(email)
                    if valida_email(email) == False:
                        email_invalido = True 
                    if valida_email(email) == True: #Se o email for valido, passar para a senha
                        email = ''
                        emailescrito = texto.render(email,True,(0,0,0))
                        email_invalido = False 
                        escreva_senha = True
            if escreva_senha == True:
                if ev.key == K_BACKSPACE: #Poder usar backspace para apagar 
                    senha=senha[:-1]
                    senhaescrita=texto.render(senha,True, (255,255,255))
                if ev.key == K_RETURN:
                    valida_senha(senha)
                    if valida_senha(senha) == False:
                        senha_invalida = True
                    if valida_senha(senha) == True: 
                        casita = True
                
                
                    

            
                
        if escreva_senha == False:        
            if ev.type == TEXTINPUT:
                email += ev.text
                emailescrito = texto.render(email, True, (255,255,255))
        
        if escreva_senha == True:
            if ev.type == TEXTINPUT:
                limpa = False
                senha += ev.text
                senhaescrita = texto.render(senha,True, (255,255,255))
        

    window.fill((0,0,0))

    draw.rect(window, (255, 255, 255), (300,300,500,100), 4)
    if escreva_senha == False: 
        escrito = texto.render('Email:', True , (255,255,255))
        window.blit(escrito, (310,310))
        window.blit(emailescrito,(310,350))
    if escreva_senha == True:
        escrito = texto.render('Senha: ', True, (255,255,255))
        window.blit(escrito, (310,310))
        window.blit(senhaescrita,(310,350))
    

        
    if email_invalido == True: 
        window.fill((0,0,0))
        escrito = texto.render('Entre um email válido', True, (255,0,0))
        window.blit(escrito, (510,510))
    if senha_invalida == True:
        escrito = texto.render('Entre uma senha válida\n(8 caracteres, 1 Maiuscula, 1 Minuscula, 1 Numero)', True, (255,0,0))
        window.blit(escrito,(410,410))

    if casita == True:
        cachorro_imagem = image.load('cachorro.png')
        cachorro_imagem = transform.scale(cachorro_imagem, (150,150))

        cachorro_font = font.Font('Somelist.ttf', 50)
        manha = mixer.Sound('manha.mp3')
        tarde = mixer.Sound('tarde.mp3')
        noite = mixer.Sound('noite.mp3')
        
        clock = time.Clock()


    ##UPDATE

        dt = clock.get_time()/1000
        keys = key.get_pressed()

        mouse_x,mouse_y = mouse.get_pos()

        for ev in event.get():
            if ev.type == QUIT:
                running = False

            #AÇOES INSTANTANEAS

            if ev.type == KEYDOWN:
                key_pressed = ev.key
                if key_pressed == K_x:
                    if estado == 0:
                        estado+=1
                    elif estado == 1:
                        estado = 0
            
        ## APERTAR TECLA [X] PARA MUDAR O ESTADO DO SOL (MOUSE OU TECLADO)

            if estado == 1:
                sol_x=mouse_x
                sol_y=mouse_y
            if estado == 0:
                if keys[K_d]:
                    sol_x = sol_x + 500 * dt
                if keys[K_a]:
                    sol_x = sol_x - 500 * dt
                if keys[K_w]:
                    sol_y = sol_y - 500 * dt
                if keys[K_s]:
                    sol_y = sol_y + 500 * dt


        # Nuvem não pode sair da tela

        if indo_direita == 0:
            nuvem_x = nuvem_x + 100 * dt
        else:
            nuvem_x = nuvem_x - 100 * dt
        
        if nuvem_x+120+40 > 1280:
            indo_direita+=1
        if nuvem_x-40 < 0:
            indo_direita = 0

        # Sol não pode sair da tela

        if sol_x-100<=0:
            sol_x = 100
        if sol_x+100>=1280:
            sol_x = 1180
        if sol_y-100<=0:
            sol_y = 100
        if sol_y+100>=720:
            sol_y = 620

        # Mudar a cor de fundo e mudar o sfx que toca se botão esquerdo do mouse é apertado

        if 0<=sol_x<426:
            background_color = (250, 212, 100) 
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    manha.play()
        elif sol_x<853:
            background_color = (100, 220, 250)
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    tarde.play()
        elif sol_x<=1280:
            background_color = (41, 30, 7)
            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    noite.play()

        #Desenhar a partir daqui

        #Desenhar primitivas geometricas
        window.fill(background_color)

        #Sol
        draw.circle(window, (255,255,0), (sol_x,sol_y), 50)
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x+100,sol_y), 5)
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x,sol_y+100), 5)
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x+80,sol_y+90), 7)
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x+90,sol_y-40), 7)   
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x,sol_y-100), 5) 
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x-100,sol_y), 5) 
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x-90,sol_y-90), 7) 
        draw.line(window, (255,255,0),(sol_x,sol_y),(sol_x-90,sol_y+80), 7) 

        #Casa
        draw.rect(window, (50, 168, 70), (0, 550, 1280, 300))
        draw.rect(window, (227, 195, 132), (200,350,300,200))
        draw.polygon(window, (196, 103, 49), ((200,350), (350,150), (500,350)))
        draw.rect(window, (148, 219, 227),(225,400,55,80) )
        draw.rect(window, (128, 85, 1), (350,400,90,150))
        draw.circle(window, (0,0,0), (360,470), 5)

        #Arvore
        draw.rect(window, (128, 85, 1), (900,400,30,150))
        draw.circle(window, (20, 107, 2), (915,350), 100)

        #Nuvem
        draw.circle(window, (255,255,255), (nuvem_x,75), 40)
        draw.circle(window, (255,255,255), (nuvem_x + 40,75), 40)
        draw.circle(window, (255,255,255), (nuvem_x + 80,75), 40)
        draw.circle(window, (255,255,255), (nuvem_x + 120,75), 40)
        
        #Desenhar imagens 
        window.blit(cachorro_imagem, (500,420))

        # Desenhar texto
        cachorro_text = cachorro_font.render('mais um dia calmo', True, (0, 0, 0))
        window.blit(cachorro_text, (400,100))




    display.update()