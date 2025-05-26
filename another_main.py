import app.another_injector as another_injector_module
from app.another_injector import Container
from app.another_injector import AnotherInsertUseCase

if __name__ == "__main__":
    container = Container()
    container.wire(modules=[another_injector_module.__name__])
    input = {"seller": "luizalabs", "product_id": "p1", "a_value": 199}
    output = AnotherInsertUseCase.insert(input)    
    print("Inserido", output)