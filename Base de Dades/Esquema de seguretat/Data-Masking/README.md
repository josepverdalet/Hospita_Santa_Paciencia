Vistes aplicades a Zelador i Vari:
 
 
 
*     DNI: 'XXXXX' || RIGHT(dni, 4)

Agafa els últims 4 caràcters del DNI i els posa darrere de cinc "X".

Resultat: XXXXX1234A

*     Telèfon: '******' || RIGHT(telefon, 3)

Oculta tot el número excepte els últims 3 dígits.

Resultat: ******567

*     Email: LEFT(email, 1) || '*******@' || SPLIT_PART(email, '@', 2)

Mostra només la primera lletra, posa asteriscs i després manté el domini (el que hi ha després de l'@).

Resultat: j*******@gmail.com
