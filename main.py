from modulo import Modulo
from ag import AG
import pandas as pd


def get_group_ag(df, ag: AG) -> tuple[list, int]:
    """Retorna o melhor indivíduo e o valor da função objetivo aplicada nele."""
    index = ag.get_group()
    grupo = df.iloc[list(set(index))].id_modulo.values
    avaliacao = ag.evaluate_group(index)
    return grupo, avaliacao


def run() -> pd.DataFrame:
    modulo = Modulo(max_len=200_000)
    data = modulo.get_file()
    
    ag = AG()
    lista = []

    i = 1
    while len(data) > 20:
        ag.df =  data
        grupo, avaliacao = get_group_ag(data, ag)
        
        dic = dict(
            ranking = i,
            qtd = len(grupo),
            grupo = grupo,
            avaliacao = avaliacao
        )

        i += 1
        lista.append(dic)

        # Resetando o dataframe
        data = modulo.filter_modulo(data, grupo)

    return dict(
        ag = pd.DataFrame(lista),
        sobra = list(data.id_modulo.values),
        individual = modulo.get_maiores()
        )

if __name__ == "__main__":
    run()