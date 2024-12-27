import pandas as pd


class Modulo:
    def __init__(self, max_len: int):
        self.max_len = max_len
        self.file = 'dados.csv'
        self.df = pd.read_csv(self.file, sep=';')

    def get_file(self) -> pd.DataFrame:
        return self.df.query(f'qtd<{self.max_len}').reset_index(drop=True)
    
    def get_maiores(self) -> list:
        return list(self.df.query(f'qtd>={self.max_len}').id_modulo.values)
    
    def filter_modulo(self, df: pd.DataFrame, grupo: list):
        return df.loc[~df.id_modulo.isin(grupo)].reset_index(drop=True)
