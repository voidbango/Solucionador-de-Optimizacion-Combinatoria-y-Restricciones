import random
import numpy as np
import pandas as pd
import os


# --> CONFIGURACION INCIAL!!
# Tabla 1 traducida a diccionarios con los rangos indicados para dias y trabajadores.
# Asimismo la cantidad de turnos segun tamano de instancia
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

# --> SE CREA CARPETA INSTANCIAS
# se usa exist_ok=True para evitar fallas si es que la carpeta ya existe!
os.makedirs("instancias", exist_ok=True)


# --> FUNCION PARA GENERAR INSTANCIAS
# bucle principal que itera sobre el diccionario 
for size, settings in rangos_generador_instancias.items():   
    # 5 instancias por cada tamano con dias y trabajadores elegidos aleatoriamente 
    # con la libreria random y se obtiene la lista de turnos
    
    for i in range(1, 6):
        dias = random.randint(*settings["días"])
        trabajadores = random.randint(*settings["trabajadores"])
        turnos = settings["turnos"]

        # --> TRABAJADORES REQUERIDOS
        # se calcula la media razonable diviendo el total de trabajadores entre el numero de turnos
        media = trabajadores / len(turnos)
        # luego se define una desviacion estandar del 20% para que los valores no cambien tanto
        desviacion_estandar = media * 0.2

        # crea un diccionario de requerimientos y genera numeros aleatorios con la media y desviacion estandar
        requerimientos = {
            f"Día_{d+1}": {turno: max(1, int(np.random.normal(media, desviacion_estandar))) for turno in turnos}
            for d in range(dias)
        }

        # --> DISPOSICION TRABAJADORES 
        # se genera un array 3D de datos aleatorios
        disposicion = np.random.randint(0, 11, size=(trabajadores, dias,  len(turnos)))

        # --> GUARDAR ARCHIVOS POR TAMANO
        # se definen las rutas de las subcarpetas segun size
        carpeta = f"instancias/{size}"
        os.makedirs(carpeta, exist_ok=True)

        # --> Uso Pandas
        # se convierte el diccionario de requerimientos es una tabla de Pandas
        # con los dias como filas y los turnos como comlumnas gracias a ".T"
        req_df = pd.DataFrame(requerimientos).T
        # se guarda la tabla en un archivo CSV segun indice
        req_df.to_csv(f"{carpeta}/trabajadores_requeridos_instancia_{i}.csv", index=True)


        # --> GUARDADO DE LA DISPOSICION DE LOS TRABAJADORES
        # creamos el MultiIndex (índice de 3 niveles) y con pd.MultiIndex se crean todas las combinaciones posibles

        idx_disposicion = pd.MultiIndex.from_product(
            [range(1, trabajadores + 1), range(1, dias + 1), turnos],
            names=["Trabajador", "Día", "Turno"]
        )
        
        # se crea el dataframe y con .flatten el array 3D pasa a una lista 1D
        disposicion_df = pd.DataFrame(
            disposicion.flatten(), 
            index=idx_disposicion,
            columns=["Disposicion"]
        )
        
        # se guarda el dataframe en un archivo CSV
        disposicion_df.to_csv(f"{carpeta}/disposicion_trabajador_instancia_{i}.csv", index=True)      
        # mensaje de confirmacion
        print(f"Instancia {i} ({size}) generada: {dias} días, {trabajadores} trabajadores.")

print("Generación completa!!!")