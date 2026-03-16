"""
Arquivo main responsável por executar o processo de ETL.
"""

from src import extract
from src import load

Extract = extract()
Load = load()

# Brasil
br = Extract.extract_country("Brazil")
Load.create_sqlite_table(br, "universities", "universidades_br")

# China
ch = Extract.extract_country("China")
Load.create_sqlite_table(ch, "universities", "universidades_ch")

# França
fr = Extract.extract_country("France")
Load.create_sqlite_table(fr, "universities", "universidades_fr")

# Itália
it = Extract.extract_country("Italy")
Load.create_sqlite_table(it, "universities", "universidades_it")

print("\nProcesso ETL multi-países concluído!")
