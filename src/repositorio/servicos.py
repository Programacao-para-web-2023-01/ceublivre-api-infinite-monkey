from src.repositorio.repositorio import db_conn


def buscar_historico(id_conta:int):
    data = []
    if(db_conn):
        data = db_conn.execute(f'select * from pedidos pd where pd.id_conta = {id_conta};')
    return data