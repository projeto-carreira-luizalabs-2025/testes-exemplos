"""
(pré) configurações para os testes
"""

# load_dotenv()
# Configura ambiente de testes

# Carregando fixtures
from glob import glob

def refactor(string: str) -> str:
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [
    refactor(fixture)
    for fixture in glob("tests/fixtures/**/*.py", recursive=True)
    if "__" not in fixture
]
