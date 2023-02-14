from Funções import *

carteira_teste = []

mxrf = Ativo('mxrf11')
bcff = Ativo('bcff11')
alzr = Ativo('alzr11')
kncr = Ativo('kncr11')
knri = Ativo('knri11')
vino = Ativo('vino11')
xplg = Ativo('xplg11')
xpml = Ativo('xpml11')

add_carteira(mxrf, carteira_teste)
add_carteira(bcff,carteira_teste)
add_carteira(alzr,carteira_teste)
add_carteira(kncr, carteira_teste)
add_carteira(knri, carteira_teste)
add_carteira(vino, carteira_teste)
add_carteira(xplg, carteira_teste)
add_carteira(xpml, carteira_teste)

Ativo.mostra_carteira(carteira_teste)


#possivel(carteira_teste)
