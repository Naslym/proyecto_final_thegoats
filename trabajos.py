def crearInicio():
    #suelo
    app.fondo=gradiente('azulGandul','azulCieloProfundo','azulCieloClaro','azulClaro','cianClaro',inicio='superior')
    #cueva
    Poligono(319,147,320,112,326,131,opacidad=80)
    Poligono(328,112,350,285,343,286,325,353,328,375,303,373,271,375,263,333,278,296,282,272,287,230,296,215,302,169,319,147,328,112,opacidad=80)
    PoligonoRegular(378,280,120,8,relleno='negro',opacidad=40)
    PoligonoRegular(378,280,100,8,relleno='negro',opacidad=40)
    PoligonoRegular(378,280,80,8,relleno='negro',opacidad=40)
    PoligonoRegular(378,280,60,8,relleno='negro',opacidad=40)
    Poligono(270,373,263,376,244,371,229,370,219,364,226,339,227,287,238,269,235,258,239,237,242,195,243,188,249,153,249,141,263,118,278,85,285,64,302,17,310,0,400,0,371,349,373,328,375,353,343,286,350,285,320,112,319,147,302,169,296,215,282,272,278,296,263,333,271,375,270,373,relleno='gris')
    Poligono(228,362,228,350,249,334,252,296,259,243,262,236,277,193,291,165,302,169,296,215,287,230,282,272,278,296,263,333,270,373,228,362,relleno='grisClaro',opacidad=50)
    Poligono(344,168,347,147,348,138,347,134,354,95,363,100,378,147,380,172,384,285,380,304,350,262,344,168,relleno='grisClaro',opacidad=50)
    Poligono(350,285,343,286,325,356)
def crearCuevaB():
    app.fondo=gradiente('marrónCuero','chocolate')
    Círculo(200,200,400,relleno=gradiente('naranjaMarrón','marrónCuero'),opacidad=77)
    PoligonoRegular(355,292,340,16,relleno=gradiente('negro','marrónCuero'),opacidad=60)
    PoligonoRegular(355,292,320,16,relleno=gradiente('negro','marrónCuero'),opacidad=50)
    PoligonoRegular(355,292,300,16,relleno=gradiente('negro','marrónCuero'),opacidad=40)
    PoligonoRegular(355,292,280,16,relleno=gradiente('negro','marrónCuero'),opacidad=30)
    PoligonoRegular(355,292,260,19,relleno=gradiente('negro','marrónCuero'),opacidad=20)
    PoligonoRegular(355,292,240,16,relleno=gradiente('negro','marrónCuero'),opacidad=10)
    #suelo
    Rect(0,356,400,44,relleno=gradiente('negro','marrónCuero',inicio='inferior'),opacidad=90)
    #piedras
    Poligono(0,0,23,38,39,56,45,54,43,80,28,104,13,115,0,166,0,0, relleno=gradiente('tierra','chocolate','marrónCuero',inicio='izquierda-inferior'),borde='negro')
    Poligono(60,0,80,70,103,40,120,41,130,0,relleno=gradiente('chocolate','tierra','marrónCuero',inicio='superior'),borde='negro')
    Poligono(179,0,189,20,200,34,231,63,247,47,259,25,290,46,304,72,315,45,337,0,relleno=gradiente('chocolate','tierra','marrónCuero',inicio='superior'),borde='negro')
    Polígono(330,0,333,19,362,17,393,100,400,0,relleno=gradiente('chocolate','tierra','marrónCuero',inicio='superior'),borde='negro')
    Poligono(0,166,18,189,33,215,26,278,42,302,38,339,44,356,27,378,0,398,0,166,relleno=gradiente('tierra','chocolate','marrónCuero',inicio='izquierda-inferior'),borde='negro')
    Poligono(322,399,329,373,347,362,368,362,380,352,399,318,400,400,322,399,relleno=gradiente('chocolate','tierra','marrónCuero',inicio='izquierda-inferior'),borde='negro')
    #Brillo
    
    #cofre
    Ovalo(110,322,90,40,relleno=gradiente('naranjaMarrón','chocolate'),borde='varillaDorada',anchuraDeBorde=4)
    Rect(65,322,90,47,relleno=gradiente('naranjaMarrón','chocolate',inicio='inferior'),borde='varillaDorada',anchuraDeBorde=4,opacidad=94)
    Línea(69,335,151,335,relleno='marrónCuero')
    Línea(69,345,151,345,relleno='marrónCuero')
    Línea(69,355,151,355,relleno='marrónCuero')
    Línea(69,363,151,363,relleno='marrónCuero') 
    Línea(76,312,140,312,relleno='marrónCuero')
    Línea(73,320,149,320,relleno='marrónCuero')
    Rect(97,319,27,9,relleno='oro',borde='varillaDorada')
    Rect(105,321,12,3,relleno='negro',opacidad=75)
    #estrelleas
    Estrella(63,278,7,4,relleno='oro',opacidad=70)
    Estrella(113,268,6,5,relleno='oro',opacidad=80)
    Estrella(50,305,5,5,relleno='oro',opacidad=75)
    Estrella(90,290,5,4,relleno='oro',opacidad=70)
    Estrella(105,243,5,4,relleno='oro',opacidad=87)
    Estrella(142,272,5,4,relleno='oro',opacidad=75)    
    Estrella(128,290,7,5,relleno='oro',opacidad=79)
    Estrella(84,262,7,5,relleno='oro',opacidad=85)
    Estrella(161,300,4,4,relleno='oro',opacidad=79)
    #monedas
    Circulo(49,377,5,relleno='oro',borde='varillaDorada')
    Circulo(30,385,5,relleno='oro',borde='varillaDorada')
    Circulo(83,387,5,relleno='oro',borde='varillaDorada')
    Circulo(59,387,5,relleno='oro',borde='varillaDorada')
    Circulo(113,376,5,relleno='oro',borde='varillaDorada')
    Circulo(142,390,5,relleno='oro',borde='varillaDorada')
    Circulo(174,377,5,relleno='oro',borde='varillaDorada')
    Circulo(168,395,5,relleno='oro',borde='varillaDorada')
    Poligono(185,382,200,382,200,387,194,394,186,388,185,383,relleno=gradiente('azulClaro','blancoFantasma'),borde='negro')
    Poligono(50,355,63,355,63,359,56,365,50,359,50,355,relleno=gradiente('azulClaro','blancoFantasma'),borde='negro')
    Poligono(99,382,99,388,105,393,111,388,111,382,relleno=gradiente('azulClaro','blancoFantasma'),borde='negro')
    


crearCuevaB()


# cañaDePescar
cañaDePescar = Grupo(
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
    
cañaDePescar = Grupo(
    cañaDePescar)
cañaDePescar.ancho = 50
cañaDePescar.altura = 50

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

Rect(0, 0, 400, 400, relleno=gradiente('azulGandul','azulClaro',inicio='inferior'))

Bote = Grupo( 
            Polígono(69, 229, 94, 280, 123, 288, 160, 291, 192, 288, 220, 280, 247, 228, relleno=gradiente(rgb(100,40,20,), rgb(80,20,0)),borde='negro', anchuraDeBorde=1),
            Óvalo(158, 227, 177, 40, relleno='marrónCuero', borde='negro', anchuraDeBorde=1),
            )
Persona = Grupo(            
               Línea(113, 210, 116, 247, anchuraDeLínea=8, relleno=gradiente(rgb(100,40,20,), rgb(80,20,0))),
               Línea(200, 210, 200, 247, anchuraDeLínea=8, relleno=gradiente(rgb(100,40,20,), rgb(80,20,0))),
               Línea(112, 173, 114, 228, relleno='black', anchuraDeLínea=5),
               Línea(112, 228, 135, 228, relleno='black', anchuraDeLínea=5),
               Línea(135, 225, 135, 245, relleno='black', anchuraDeLínea=5),
               Línea(112, 210, 142, 205, relleno='black', anchuraDeLínea=5),
               Circle(112, 174, 14, relleno='black'),
               Circle(112, 164, 14, relleno='trigo', borde='red', anchuraDeBorde=1),
               Óvalo(112, 173, 35, 10, relleno='trigo', borde='red', anchuraDeBorde=1),
               Óvalo(112, 176, 30, 5, relleno='black'),
               Línea(137, 185, 183, 300, relleno=rgb(205, 133, 63), anchuraDeLínea=6),
               Óvalo(183, 300, 16, 30, rotarÁngulo=-16, relleno=gradiente(rgb(139, 69, 19),rgb(160, 82, 45)))
               )
               
Remo = Grupo(
       Línea(137, 185, 183, 300, relleno=rgb(205, 133, 63), anchuraDeLínea=6),
       Óvalo(183, 300, 16, 30, rotarÁngulo=-16, relleno=gradiente(rgb(139, 69, 19),rgb(160, 82, 45)))
       )

app.fondo=gradiente('turquesaPálido','azulPolvo')
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
Rect(30,264,13,12,relleno='gris',borde='grisOscuro')
Linea(28,275,45,275,relleno='azulReal',anchuraDeLinea=1)
Ovalo(90,258,10,7,relleno='amarilloVerde',borde='oliva',anchuraDeBorde=1)
Rect(87,261,6,8,relleno='amarilloVerde',borde='oliva',anchuraDeBorde=1)
Linea(79,268,100,269,relleno='azulReal',anchuraDeLinea=1)
Rect(32,323,14,15,relleno='naranja',borde='rojoNaranja',anchuraDeBorde=1)
Línea(32,323,47,337,relleno='rojo')
Linea(30,337,47,337,relleno='madera',anchuraDeLinea=3)
Poligono(172,302,176,294,186,300,180,309,172,302,relleno='verde',borde='verdeOscuro')
Linea(172,308,187,308,relleno='azulReal',anchuraDeLínea=2)
PoligonoRegular(47,365,15,3,rotarÁngulo= 300,relleno='grisPizarraOscuro')
Circulo(47,359,7,relleno='grisPizarraOscuro')
Ovalo(48,386,45,44,relleno='grisPizarraOscuro')
Linea(123,196,149,250,relleno='tierra',anchuraDeLínea=20,rotarAngulo=-50)
Línea(100,291,128,311,relleno='tierra',anchuraDeLínea=3)
Linea(120,214,161,209,relleno='tierra',anchuraDeLínea=10)
Línea(109,295,109,288,relleno='tierra')
Línea(113,300,110,307,relleno='tierra')
Línea(95,221,169,240,relleno='azulReal',anchuraDeLínea=3,opacidad=65)
Ovalo(117,373,20,15,relleno='amarillo')
Ovalo(117,373,17,14,relleno='verde')
Ovalo(117,373,12,12,relleno='rojo')
Línea(105,379,129,379,relleno='madera',anchuraDeLínea=3)
Ovalo(219,270,60,45,relleno='grisPizarraOscuro')
Ovalo(219,270,45,28,relleno='azulGandul')
Línea(201,291,237,291,relleno='azulReal',anchuraDeLínea=3)
#personaje
Línea(185,374,172,389,anchuraDeLínea=4)
Línea(185,345,185,374,anchuraDeLínea=4)
Línea(185,374,196,389,anchuraDeLínea=4)
Línea(185,345,167,365,anchuraDeLínea=4)
Línea(185,345,200,365,anchuraDeLínea=4)
Circulo(185,338,8)
#sombrero
Circulo(185,330,6,relleno='trigo',borde='rojo',anchuraDeBorde=1)
Ovalo(185,333,20,5,relleno='trigo',borde='rojo',anchuraDeBorde=1)

app.fondo = relleno=gradiente('turquesaPálido','azulPolvo')

#mar
Rect(0,200,400,200,relleno=gradiente('azulGandul','azulCieloProfundo'))

#arena
Polígono(0,280,300,335,400,320,400,330,300,360,0,290,relleno='blanco')
Polígono(0,290,300,360,400,330,400,400,0,400,relleno='trigo')
Polígono(0,335,400,390,400,400,0,400,relleno='madera')

#basura
Polígono(53,240,80,245,76,260,60,264,49,252,53,240)
Línea(65,241,61,226)
Línea(65,241,72,227)
Línea(65,241,80,234)
Línea(53,240,80,245,relleno='blanco',anchuraDeLínea=5)

Polígono(106,222,121,219,139,229,130,242,106,221,relleno='cianClaro')
Polígono(160,200,180,200,178,223,160,221,160,200,relleno='azulAceroClaro')
Polígono(160,258,173,250,187,260,173,276,160,258,relleno='agua')
Rect(19,240,20,40,relleno='caqui')

Polígono(16,200,50,216,28,220,16,200)
Polígono(173,295,205,292,220,319,193,319,173,295,relleno='salmónClaro')
Óvalo(40,320,30,20)

#personas 
Círculo(358,300,19)
Línea(358,300,360,360)
Línea(360,360,380,389)
Línea(360,360,338,387)
Línea(360,338,335,349)
Línea(360,338,328,325)

Círculo(120,280,19,)
Línea(120,280,120,342)
Línea(120,342,100,378)
Línea(120,342,140,374)
Línea(120,320,96,330)
Línea(120,320,141,330)

Óvalo(320,237,120,60,relleno='cian')
Óvalo(320,237,100,50,relleno='rojo')
Rótulo('¡SURF!',320,237,tamaño=20)
Círculo (320,160,19)
Línea(320,160,320,212)
Línea(320,212,296,240)
Línea(320,212,338,240)
Línea(320,200,287,176)
Línea(320,200,348,179)

#sol
Círculo(120,40,60,relleno='oro')
