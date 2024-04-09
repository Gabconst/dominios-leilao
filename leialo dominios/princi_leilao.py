from dominio import Usuario, Lance, Leilao

virgil = Usuario('Virgil')
giovanni = Usuario('Giovanni')

lance_virgil = Lance(virgil, 300.0)
lance_giovanni = Lance(giovanni, 100.0)

leilao = Leilao('Instrumentos')

leilao.lance.append(lance_giovanni)
leilao.lance.append(lance_virgil)

for lance in leilao.lance:
    print(f'O usuario {lance.usuario.nome} deu um lace de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}')