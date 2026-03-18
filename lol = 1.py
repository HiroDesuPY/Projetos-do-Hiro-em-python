from pathlib import Path
from shutil import rmtree




pasta_bus = Path('.') #pasta atual

print(pasta_bus.glob('*.py')) #busca por arquivos com extensão .py