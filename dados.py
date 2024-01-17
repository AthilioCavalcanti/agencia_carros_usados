from typing import List
from carro import Carro
from carro_combustao import CarroCombustao
from carro_hibrido import CarroHibrido
from carro_eletrico import CarroEletrico


carros_disponiveis: List[Carro] = [
    CarroCombustao("BOO0L00", "Accord", "Honda", "Sedan", 2018, "Preto", "Álcool/Gasolina (Flex)", 170600.0, 65000),
    CarroCombustao("BOO1L11", "Yaris", "Toyota", "Hatch", 2020, "Vermelho", "Álcool/Gasolina (Flex)", 82600.0, 50000),
    CarroHibrido("BOO2L22","Compass S 4xe", "Jeep", "SUV", 2023, "Azul", "Eletricidade/Gasolina", 280300.0, 3000, 11.4),
    CarroHibrido("BOO3L33","Prius", "Toyota", "Sedan", 2019, "Branco", "Eletricidade/Gasolina", 115300.0, 15000, 1.3),
    CarroEletrico("BOO4L44","Han", "BYD", "Sedan", 2022, "Vermelho", 459300.0, 100000, 76.9),
    CarroEletrico("BOO5L55","E-JS1", "JAC", "Hatch", 2022, "Prata", 109300.0, 9000, 30.2),
    CarroEletrico("BOO6L66","Bolt", "Chevrolet", "Hatch", 2020, "Branco", 186076.0, 11000, 66.0)
]