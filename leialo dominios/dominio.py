class Usuario:
    def __init__(self, nome, carteira):
        self._nome = nome
        self._carteira = carteira

    def propoe_lance(self, leilao, valor):
        if valor > self._carteira:
            raise ValueError('Não pode propor lance com valor maior do que o da carteira')

    @property
    def nome(self):
        return self._nome

    @property
    def carteira(self):
        return self._carteira


class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self._lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self._lances.append(lance)
        else:
            raise ValueError('ERRO AO PROPOR LANCE')

    @property
    def lance(self):
        return self._lances[:]

    def _tem_lances(self):
        return self._lances

    def _usuarios_diferentes(self, lance):
        return self._lances[-1].usuario != lance.usuario

    def _maior_que_lance_anterior(self, lance):
        return lance.valor > self._lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self._usuarios_diferentes and
                                          self._maior_que_lance_anterior())










