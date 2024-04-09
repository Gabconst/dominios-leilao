from dominio import Usuario, Leilao
import pytest


@pytest.fixture()
def mark():
    return Usuario('Mark', 100)


@pytest.fixture()
def leialao():
    return Leilao('Intrumentos')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_lances(mark, leilao):

    mark.propoe_lance(leilao, 50.0)

    assert mark.carteira == 50.0


def test_deve_permitir_lance_quando_o_valor_for_menor_que_o_valor_da_carteira(mark, leilao):
    mark.propoe_lance(leilao, 1.0)

    assert mark.carteira == 99.0


def test_dev_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(mark, leilao):

    mark.propoe_lance(leilao, 100.0)

    assert mark.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteiira(mark, leilao):
    with pytest.raises(ValueError):
        mark.propoe_lance(leilao, 200.0)




