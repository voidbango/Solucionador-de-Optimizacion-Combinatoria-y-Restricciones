import random
import numpy as np
import pandas as pd
import os


rangos_generador_instancias = {
    "pequeña":{
        "días": (5, 7),
        "trabajadores": (5, 15),
        "turnos": ["Día", "Noche"]
    },
    "mediana":{
        "días": (7, 14),
        "trabajadores": (15, 45),
        "turnos": ["Mañana", "Tarde", "Noche"]
    },
    "grande":{
        "días": (14, 28),
        "trabajadores": (45, 90),
        "turnos": ["Mañana", "Tarde", "Noche"]
    }
}

