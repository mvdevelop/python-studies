
"""
    2️⃣ O — Open/Closed Principle (OCP) - Aberto para extensão, fechado para modificação.

    ❌ Errado
    class CalculadoraDesconto:
        def calcular(self, tipo_cliente, valor):
            if tipo_cliente == "regular":
                return valor * 0.9
            elif tipo_cliente == "vip":
                return valor * 0.8

    🔴 Sempre que surgir novo tipo, você precisa modificar a classe.
"""

# ✅ Correto (usando polimorfismo)
from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


class DescontoRegular(Desconto):
    def calcular(self, valor):
        return valor * 0.9


class DescontoVIP(Desconto):
    def calcular(self, valor):
        return valor * 0.8

# 🟢 Agora você pode criar DescontoBlackFriday sem alterar código existente.
