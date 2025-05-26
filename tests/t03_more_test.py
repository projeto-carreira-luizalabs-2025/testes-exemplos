from unittest import TestCase

class Box:
    def __init__(self, value: str | int):
        self.value = value

class TestMore(TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        Antes de iniciar todos os testes daqui...
        """
    
    def setUp(self):
        """
        Ao iniciar cada teste..
        """ 
        self.box = Box(3)
        
    def tearDown(self):
        """
        Ao finalizar cada teste
        """
        del self.box
        
    @classmethod
    def tearDownClass(cls):
        """
        Ao finalizar todos os testes
        """
        
    def test_should_have_a_box(self):
        assert self.box is not None
        assert self.box.value == 3