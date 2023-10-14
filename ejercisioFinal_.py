#sonido del mar
sonido1 = Sound('cmu://600529/25328863/Sonido+del+Mar+para+Dormir.m4a')
#sonido de la playa
sonido2 = Sound('cmu://600529/25328868/Sonido+ambiental+de+la+playa.m4a')
Bote = Grupo( 
            Polígono(69, 229, 94, 280, 123, 288, 160, 291, 192, 288, 220, 280, 247, 228, relleno=gradiente(rgb(100,40,20,), rgb(80,20,0)),borde='negro', anchuraDeBorde=1),
            Óvalo(158, 227, 177, 40, relleno='marrónCuero', borde='negro', anchuraDeBorde=1),
            )
Bote.ancho=60
Bote.altura=30
Bote.centroX=360
Bote.centroY=190
               
               

app.fondo=gradiente('turquesaPálido','azulPolvo')
#mensaje
mensaje=Rotulo('presione para comenzar',200,50)
#sol
Circulo(13,28,50,relleno='oro')
Circulo(13,28,59,relleno='oro',opacidad=70)
#nubes
Ovalo(121,85,45,15,relleno='cianClaro')
Ovalo(134,80,45,15,relleno='cianClaro')
Ovalo(146,90,45,15,relleno='cianClaro')
Ovalo(256,78,45,15,relleno='cianClaro')
Ovalo(271,72,45,15,relleno='cianClaro')
Ovalo(282,83,45,15,relleno='cianClaro')
Ovalo(29,112,45,15,relleno='cianClaro')
Ovalo(43,120,45,15,relleno='cianClaro')
Ovalo(45,110,45,15,relleno='cianClaro')
Ovalo(247,143,45,15,relleno='cianClaro')
Ovalo(264,149,45,15,relleno='cianClaro')
Ovalo(270,137,45,15,relleno='cianClaro')
#mar
Rect(0,200,400,200,relleno=gradiente('azulGandul','azulCieloProfundo'))
Línea(0,200,400,200,relleno='azulGandul',anchuraDeLínea=4,opacidad=60)
# arena
Poligono(0,290,270,343,400,340,400,400,0,400,0,290,relleno='blanco')
Poligono(0,300,270,356,400,350,400,400,0,400,0,300,relleno='trigo')
Poligono(0,355,400,378,400,400,0,400,0,355,relleno=gradiente('madera','trigo',inicio='izquierda-superior'))

#choza
Rect(260,280,130,100,relleno='tierra')
Poligono(245,299,271,265,314,239,332,228,387,267,403,300,242,299,relleno='varillaDorada',borde='varillaDoradaOscura',anchuraDeBorde=3)
Línea(318,213,332,228,relleno='varillaDoradaOscura')
Línea(331,213,332,228,relleno='varillaDoradaOscura')
Linea(341,213,332,228,relleno='varillaDoradaOscura')
Línea(352,213,332,228,relleno='varillaDoradaOscura')
Linea(265,299,265,380,relleno='marrónCuero')
Línea(279,299,279,380,relleno='marrónCuero')
Línea(296,299,296,380,relleno='marrónCuero')
Línea(310,299,310,380,relleno='marrónCuero')
Rect(297,313,29,64,relleno='tierra',borde='marrónCuero',anchuraDeBorde=3)
Linea(324,300,324,380,relleno='marrónCuero')
Línea(338,299,338,380,relleno='marrónCuero')
Línea(353,299,352,380,relleno='marrónCuero')
Línea(368,299,368,380,relleno='marrónCuero')
Línea(380,299,380,380,relleno='marrónCuero')
Linea(329,227,336,227,relleno='marróncuero',anchuraDeLínea=4)
Rect(315,314,10,60,relleno='negro',opacidad=70)
Circulo(310,345,3,relleno='negro',opacidad=75)
Rect(346,321,25,23,relleno='negro',borde='marrónCuero',opacidad=70)
Línea(359,322,359,341,relleno='marrónCuero')
Línea(348,333,369,333,relleno='marrónCuero')
#basura
figura1=Rect(30,264,13,12,relleno='gris',borde='grisOscuro',visible=True),
figura2=Línea(28,275,45,275,relleno='azulReal',anchuraDeLinea=1,visible=True),
figura3=Óvalo(90,258,10,7,relleno='amarilloVerde',borde='oliva',anchuraDeBorde=1,visible=True),
figura4=Óvalo(87,261,6,8,relleno='amarilloVerde',borde='oliva',anchuraDeBorde=1,visible=True),
figura5=Linea(79,268,100,269,relleno='azulReal',anchuraDeLinea=1,visible=True,),
figura6=Rect(32,323,14,15,relleno='naranja',borde='rojoNaranja',anchuraDeBorde=1,visible=True),
figura7=Línea(32,323,47,337,relleno='rojo',visible=True),
figura8=Linea(30,337,47,337,relleno='madera',anchuraDeLinea=3,visible=True),
figura9=Poligono(172,302,176,294,186,300,180,309,172,302,relleno='verde',borde='verdeOscuro',visible=True),
figura10=Linea(172,308,187,308,relleno='azulReal',anchuraDeLínea=2,visible=True),
figura11=PoligonoRegular(47,365,15,3,rotarÁngulo= 300,relleno='grisPizarraOscuro',visible=True),
figura12=Circulo(47,359,7,relleno='grisPizarraOscuro',visible=True),
figura13=Ovalo(48,386,45,44,relleno='grisPizarraOscuro',visible=True),
figura14=Linea(123,196,149,250,relleno='tierra',anchuraDeLínea=20,rotarAngulo=-50,visible=True),
figura15=Línea(100,291,128,311,relleno='tierra',anchuraDeLínea=3,visible=True),
figura16=Linea(120,214,161,209,relleno='tierra',anchuraDeLínea=10,visible=True),
figura17=Línea(109,295,109,288,relleno='tierra',visible=True),
figura18=Línea(113,300,110,307,relleno='tierra',visible=True),
figura19=Línea(95,221,169,240,relleno='azulReal',anchuraDeLínea=3,opacidad=65,visible=True),
figura20=Ovalo(117,373,20,15,relleno='amarillo',visible=True),
figura21=Ovalo(117,373,17,14,relleno='verde',visible=True),
figura22=Ovalo(117,373,12,12,relleno='rojo',visible=True),
figura23=Línea(105,379,129,379,relleno='madera',anchuraDeLínea=3,visible=True),
figura24=Ovalo(219,270,60,45,relleno='grisPizarraOscuro',visible=True),
figura25=Ovalo(219,270,45,28,relleno='azulGandul',visible=True),
figura26=Línea(201,291,237,291,relleno='azulReal',anchuraDeLínea=3,visible=True),
figura27=Ovalo(40,210,30,8,relleno='naranja',visible=True),
figura28=Línea(24,213,56,213,relleno='azulGandul',anchuraDeLínea=3,visible=True),
figura29=Poligono(219,221,224,218,relleno='oro',borde='trigo',anchuraDeBorde=6,visible=True),
figura30=Polígono(53,240,80,245,76,260,60,264,49,252,53,240,visible=True),
figura31=Línea(65,241,61,226,visible=True),
figura32=Línea(65,241,72,227,visible=True),
figura33=Línea(65,241,80,234,visible=True),
figura34=Línea(53,240,80,245,relleno='blanco',anchuraDeLínea=5,visible=True),
figura35=Línea(45,260,80,260,relleno=gradiente('azulCieloProfundo','azulGandul',inicio='izquierda'),anchuraDeLínea=9,visible=True),
figura36=Óvalo(24,305,30,20,relleno='oro',visible=True),
figura37=Óvalo(24,305,20,10,relleno='rojo',visible=True),
figura38=Óvalo(24,305,10,5,relleno='verde',visible=True),
figura39=Línea(6,314,40,309,relleno='trigo',anchuraDeLínea=9,visible=True),
figura40=Línea(256,250,290,245,relleno='tierra',anchuraDeLínea=3,visible=True),
figura41=Línea(274,245,275,239,relleno='tierra',anchuraDeLínea=2,visible=True),
figura42=Línea(264,249,264,255,relleno='tierra',anchuraDeLínea=2,visible=True),
figura43=Circulo(252,220,7,relleno='amarilloVerde',borde='oro',anchuraDeBorde=2,visible=True),
figura44=Línea(244,227,259,227,relleno='azulGandul',visible=True)

basura=(
        figura1,figura2,figura3,figura4,figura5,figura6,figura7,
        figura8,
        figura9,
        figura10,
        figura11,
        figura12,
        figura13,
        figura14,
        figura15,
        figura16,
        figura17,
        figura18,
        figura19,
        figura20,
        figura21,
        figura22,
        figura23,
        figura24,
        figura25,
        figura26,
        figura27,
        figura28,
        figura29,
        figura30,
        figura31,
        figura32,
        figura33,
        figura34,
        figura35,
        figura36,
        figura37,
        figura38,
        figura39,
        figura40,
        figura41,
        figura42,
        figura43,
        figura44
        )

Pez= Grupo(
           Polígono(183, 127, 185, 149, 211, 169, 210, 107, relleno='rojoNaranja', opacidad=65, borde='negro', anchuraDeBorde=1),
           Polígono(135, 77, 127, 108, 173, 117, 191, 106, 186, 95, 182, 94, 178, 86, 164, 82, 154, 77, 145, 79, relleno='naranjaOscuro', opacidad=65, borde='negro', anchuraDeBorde=1),
           Polígono(121, 172, 121, 189, 127, 193, 133, 205, 143, 209, 139, 194, 139, 174, relleno='naranjaOscuro', opacidad=65, borde='negro', anchuraDeBorde=1),
           Polígono(154, 172, 159, 181, 164, 185, 171, 186, 181, 181, 190, 181, 187, 177, 177, 159, relleno='naranjaOscuro', opacidad=65, borde='negro', anchuraDeBorde=1),
           Óvalo(141, 142, 98, 77, relleno='naranja', borde='negro', anchuraDeBorde=1),
           Línea(127, 106, 121, 176, relleno='negro', anchuraDeLínea=1),
           Estrella(110, 130, 8, 4)
           )
           
Pez.ancho=30
Pez.altura=30
Pez.centroY=260
Pez.centroX=134
    
#personaje
personaje=Grupo(
    Línea(185,374,172,389,anchuraDeLínea=4),
    Línea(185,345,185,374,anchuraDeLínea=4),
    Línea(185,374,196,389,anchuraDeLínea=4),
    Línea(185,345,167,365,anchuraDeLínea=4),
    Línea(185,345,200,365,anchuraDeLínea=4),
    Circulo(185,338,8),
    Circulo(185,330,6,relleno='trigo',borde='rojo',anchuraDeBorde=1),
    Ovalo(185,333,20,5,relleno='trigo',borde='rojo',anchuraDeBorde=1)
    )
#remo
Remo = Grupo(
       Línea(137, 185, 183, 300, relleno=rgb(205, 133, 63), anchuraDeLínea=6),
       Óvalo(183, 300, 16, 30, rotarÁngulo=-16, relleno=gradiente(rgb(139, 69, 19),rgb(160, 82, 45)))
       )
Remo.ancho=30
Remo.altura=15
Remo.centroX=360
Remo.centroY=190
def enRatónPresionado(ratónX,ratónY):
    sonido1.toca(loop=Verdadero)
    sonido2.toca(loop=Verdadero)
    mensaje.valor='Que hermoso el dia de hoy'
    if mensaje.valor=='Que hermoso el dia de hoy':
        mensaje.valor='¡PERO QUE PASO CON LA PLAYA!'
        sleep(1)
        mensaje.valor='Esta demasiado sucia ,pero aqui comienza mi nueva misión'
        sleep(1)
        mensaje.valor='¡VAMOS A SALVAR LA PLAYA!'
    #if mensaje.valor=='VAMOS A SALVAR LA PLAYA!':
        escoger=app.obtenerEntradaDeTexto('Toma las pinzas, ingresando la palabra pinzas')
        if escoger=='caña':
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif escoger=='pinzas':
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
def enTeclaPresionada(tecla):
    #if caña.tocarFigura()
    if personaje.centroY>200 or personaje.centroY<400:
        if tecla=='derecha':
            personaje.centroX+=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='izquierda':
            personaje.centroX-=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='arriba':
            personaje.centroY-=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='abajo':
            personaje.centroY+=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='derecha' and tecla=='arriba':
            personaje.centroX+=2
            personaje.centroY-=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='derecha' and tecla=='abajo':
            personaje.centroX+=2
            personaje.centroY+=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='izquierda' and tecla=='arriba':
            personaje.centroX-=2
            personaje.centroY-=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
        elif tecla=='izquierda' and tecla=='abajo':
            personaje.centroX-=2
            personaje.centroY+=2
            pinzas.centroX=personaje.centroX+6
            pinzas.centroY=personaje.centroY
caña= Grupo(
    Poligono(26,3,31,1,92,44,135,86,199,183,180,182,152,129,145,117,129,96,89,52,36,9,26,3,relleno='verdeClaro',borde='negro',anchuraDeBorde=1),
    Poligono(152,129,145,117,138,121,145,132,relleno='verde',borde='negro',anchuraDeBorde=1),
    Circulo(129,134,15,relleno='verde'),
    Poligono(129,128,134,132,127,151,118,147,123,125,relleno='verde',borde='negro',anchuraDeBorde=1),
    Circulo(121,152,5,relleno='verde'),
    Linea(141,87,108,104,relleno='verde',anchuraDeLinea=4),
    Linea(96,42,69,63,relleno='verde',anchuraDeLinea=4),
    Linea(42,3,23,18,relleno='verde',anchuraDeLinea=3),
    Linea(116,121,114,103,relleno='verde',anchuraDeLinea=1),
    Linea(114,103,74,59,relleno='verde',anchuraDeLinea=1),
    Linea(74,59,27,17,relleno='verde',anchuraDeLinea=1),
    Poligono(23,18,9,22,5,24,1,31,1,38,2,43,5,49,14,57,45,79,51,87,52,93,52,103,relleno='azulClaro'),
    Circulo(50,108,4),
    Poligono(53,111,54,118,47,128,39,132,29,128,26,121,30,114,36,110,33,119,31,117,30,122,36,125,43,124,47,120,47,112,47,105,53,111,relleno='azulClaro')
    )
    
caña= Grupo(
    caña)
caña.ancho = 50
caña.altura = 50
caña.centroX=335
caña.centroY=356

# pinzas
pinzas = Grupo(
    Línea(269,4,235,24,relleno='black',anchuraDeLínea=9),
    Poligono(267,8,266,11,279,13,290,20,294,28,283,38,275,36,276,33,250,21,relleno='black'),
    Poligono(283,32,259,15,252,19,relleno='blanco'),
    Linea(235,24,69,145,relleno=gradiente('blanco','cian'),anchuraDeLinea=4),
    Poligono(66,142,36,165,28,174,26,180,21,187,26,188,33,182,40,172,46,168,52,164,55,164,60,168,62,174,58,185,54,187,56,190,51,194,60,193,70,182,67,161,71,160,68,153,75,149,66,142,relleno='black'),
    Circulo(60,158,3,relleno='oro')
    )
 
pinzas = Grupo(
    pinzas)
pinzas.ancho=50
pinzas.altura=50
pinzas.centroX=80
pinzas.centroY=345

