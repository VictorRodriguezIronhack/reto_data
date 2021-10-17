from config.configuration import engine
import pandas as pd

def collection():
    """
    Queries all the data in the database
    Args:
    Returns:
        json with all the data in the database
    """
    query = f"""
            SELECT * FROM table1
            """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")

def entry(id_):
    """
    Queries specific entry in the database
    Args:
        game (str): id of the entry.
    Returns:
        json with data of that entry
    """
    query = f"""
            SELECT * FROM table1 WHERE id = '{id_}'
            """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")

def e10():
    """
    Queries every entry for e10 in the database
    Args:
    Returns:
        json with every entry for e10 in the database
    """
    query = f"""
            SELECT * FROM table1 WHERE gas_type = 'e10'
            """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")

def sp98():
    """
    Queries every entry for sp98 in the database
    Args:
    Returns:
        json with every entry for sp98 in the database
    """
    query = f"""
            SELECT * FROM table1 WHERE gas_type = 'sp98'
            """
    datos = pd.read_sql_query(query,engine)
    return datos.to_json(orient="records")
