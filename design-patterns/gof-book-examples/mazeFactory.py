
### 1. Definição dos Produtos (Paredes)
class Wall:
    def __repr__(self):
        return "Parede Comum"

class BombedWall(Wall):
    def __repr__(self):
        return "Parede com Bomba"

### 2. A Fábrica Abstrata (MazeFactory)
# Em linguagens dinâmicas, a fábrica pode armazenar as classes 
# que deve instanciar em variáveis de instância.
class MazeFactory:
    def __init__(self):
        # Por padrão, ela conhece a parede comum
        self.part_catalog = {
            "wall": Wall
        }

    def make(self, part_name):
        """
        Versão equivalente à operação 'make' do Smalltalk.
        Usa o catálogo para garantir que o tipo correto seja criado.
        """
        part_class = self.part_catalog.get(part_name)
        if part_class:
            return part_class()
        raise ValueError(f"Tipo de peça '{part_name}' desconhecido.")

### 3. A Fábrica Concreta (BombedMazeFactory)
class BombedMazeFactory(MazeFactory):
    def __init__(self):
        super().__init__()
        # Sobrescrevemos o catálogo para usar a subclasse específica
        self.part_catalog["wall"] = BombedWall

### 4. Função CreateMaze (O Cliente)
def create_maze(factory):
    """
    Note que esta função não sabe se a parede é comum ou com bomba.
    Ela apenas confia que a factory retornará algo compatível.
    """
    wall_1 = factory.make("wall")
    wall_2 = factory.make("wall")
    
    print(f"Labirinto criado com: {wall_1} e {wall_2}")

# --- Execução ---

print("Usando Fábrica Comum:")
common_factory = MazeFactory()
create_maze(common_factory)

print("\nUsando Fábrica com Bombas:")
bombed_factory = BombedMazeFactory()
create_maze(bombed_factory)
