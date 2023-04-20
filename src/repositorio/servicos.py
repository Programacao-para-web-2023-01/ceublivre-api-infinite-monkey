from src.repositorio.repositorio import db_conn


def buscar_histórico(id_conta:int):
    data = []
    if(db_conn):
        data = db_conn.execute('select * from pedidos pd where pd.id_conta = \"{idconta}"\;')
    