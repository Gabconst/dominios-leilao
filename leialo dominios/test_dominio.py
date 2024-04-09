from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.virgil = Usuario('Virgil', 500)
        self.giovanni = Usuario('Giovanni', 500)
        self.lance_virgil = Lance(self.virgil, 300.0)
        self.leilao = Leilao('Instrumentos')

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionado_em_ordem_decrescente(self):
        jack = Usuario('Jack', 500)
        lance_jack = Lance(jack, 500)

        self.leilao.propoe(self.lance_virgil)
        self.leilao.propoe(lance_jack)

        menor_valor_esperado = 300.0
        maior_valor_esperado = 500.0

        self.assertEquals(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEquals(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        jack = Usuario('Jack', 500)
        lance_jack = Lance(jack, 500.0)

        self.leilao.propoe(self.lance_virgil)
        self.leilao.propoe(lance_jack)

        menor_valor_esperado = 300.0
        maior_valor_esperado = 500.0

        self.assertEquals(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEquals(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_virgil)

        self.assertEquals(300.0, self.leilao.menor_lance)
        self.assertEquals(300.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_maior_valor_quando_o_leilao_tiver_tres_lances(self):

        doku = Usuario('Doku', 500)
        lance_doku = Lance(doku, 400.0)

        jack = Usuario('Jack', 500)
        lance_jack = Lance(jack, 500.0)

        self.leilao.propoe(self.lance_virgil)
        self.leilao.propoe(lance_doku)
        self.leilao.propoe(lance_jack)

        menor_valor_esperado = 300.0
        maior_valor_esperado = 500.0

        self.assertEquals(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEquals(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_virgil)
        quantidades_de_lances_recebido = len(self.leilao.lance)
        self.assertEquals(1, quantidades_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        doku = Usuario('Doku', 500)
        lance_doku = Lance(doku, 200.0)

        self.leilao.propoe(lance_doku)
        self.leilao.propoe(self.lance_virgil)
        
        quantidades_de_lances_recebido = len(self.leilao.lance)
        self.assertEquals(2, quantidades_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_virgil100 = Lance(self.virgil, 500.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_virgil)
            self.leilao.propoe(lance_virgil100)










