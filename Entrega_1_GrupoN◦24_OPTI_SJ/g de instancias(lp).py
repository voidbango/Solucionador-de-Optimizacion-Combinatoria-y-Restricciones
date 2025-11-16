import random
import numpy as np
import os

# --> CONFIGURACION INCIAL 
# Tabla 1 traducida a diccionarios con los rangos indicados para dias y trabajadores.
# Asimismo la cantidad de turnos segun tamano de instancia
rangos_generador_instancias = {
    "pequeña": {
        "días": (5, 7),
        "trabajadores": (5, 15),
        "turnos": ["Dia", "Noche"]
    },
    "mediana": {
        "días": (7, 14),
        "trabajadores": (15, 45),
        "turnos": ["Manana", "Tarde", "Noche"]
    },
    "grande": {
        "días": (14, 28),
        "trabajadores": (45, 90),
        "turnos": ["Manana", "Tarde", "Noche"]
    }
}

# --> SE CREA CARPETA INSTANCIAS_LP
# se usa exist_ok=True para evitar fallas si es que la carpeta ya existe!
os.makedirs("instancias_lp", exist_ok=True)


# --> FUNCION PARA GENERAR INSTANCIAS .LP
# bucle principal que itera sobre el diccionario 
for size, settings in rangos_generador_instancias.items():
    
    # se definen las rutas de las subcarpetas segun size
    carpeta = f"instancias_lp/{size}"
    os.makedirs(carpeta, exist_ok=True)
       
    # 5 instancias por cada tamano con dias y trabajadores elegidos aleatoriamente 
    # con la libreria random y se obtiene la lista de turnos
    
    for i in range(1, 6):
        dias = random.randint(*settings["días"])
        trabajadores = random.randint(*settings["trabajadores"])
        turnos = settings["turnos"]
        
        # --- GENERACION DE PARAMETROS ---
        
        # --> TRABAJADORES REQUERIDOS (R_ht)
        media = trabajadores / len(turnos)
        desviacion_estandar = media * 0.2
        
        # R_ht: Diccionario de requerimientos
        requerimientos = {
            (h+1, t_name): max(1, int(np.random.normal(media, desviacion_estandar)))
            for h in range(dias)
            for t_name in turnos
        }

        # --> DISPOSICION TRABAJADORES (D_iht)
        # D_iht: Array 3D (trabajador, dia, turno)
        disposicion = np.random.randint(0, 11, size=(trabajadores, dias, len(turnos)))

        # --> DEFINICION DE FINES DE SEMANA (Conjunto F)
        # Asumimos que el Día 1 es Lunes. FDS = Días 6 (Sáb) y 7 (Dom) de cada semana.
        # F: Diccionario {num_fds: [lista_de_dias_h]}
        weekends = {}
        f_counter = 1
        for h in range(1, dias + 1):
            day_of_week = (h - 1) % 7 + 1  # 1=L, ..., 6=S, 7=D
            if day_of_week == 6 or day_of_week == 7:
                if f_counter not in weekends:
                    weekends[f_counter] = []
                weekends[f_counter].append(h)
            
            if day_of_week == 7:
                f_counter += 1
        
        
        # --- CONSTRUCCION DEL ARCHIVO .LP ---
        
        # Usamos una lista para ir guardando las líneas del archivo
        lp_content = []

# 1. FUNCION OBJETIVO (Maximizar Z)
        lp_content.append("Maximize")
        obj_func = []
        for i_idx in range(trabajadores):
            for h_idx in range(dias):
                for t_idx, t_name in enumerate(turnos):
                    D_iht = disposicion[i_idx, h_idx, t_idx]
                    if D_iht > 0:
                        obj_func.append(f"{D_iht} X_{i_idx+1}_{h_idx+1}_{t_name}") 


        lp_content.append("  Z: " + " + ".join(obj_func))
        lp_content.append("\nSubject To")
        
        
        
        # C2. Cobertura de demanda (R_ht) 
        for h in range(1, dias + 1):
            for t_name in turnos:
                R_ht = requerimientos[(h, t_name)]
                lhs = " + ".join([f"X_{i+1}_{h}_{t_name}" for i in range(trabajadores)])
                lp_content.append(f"  C2_h{h}_t{t_name}: {lhs} >= {R_ht}")

        # C3. Disponibilidad (D_iht = 0) 
        for i_idx in range(trabajadores):
            for h_idx in range(dias):
                for t_idx, t_name in enumerate(turnos):
                    if disposicion[i_idx, h_idx, t_idx] == 0:
                        lp_content.append(f"  C3_i{i_idx+1}_h{h_idx+1}_t{t_name}: X_{i_idx+1}_{h_idx+1}_{t_name} <= 0")

        # C4. Maximo de dos turnos por dia 
        # Implementamos la Ecuación (6) (<= 2).
        for i in range(1, trabajadores + 1):
            for h in range(1, dias + 1):
                lhs = " + ".join([f"X_{i}_{h}_{t_name}" for t_name in turnos])
                lp_content.append(f"  C4_i{i}_h{h}: {lhs} <= 2")

        # C5. Prohibicion de turno noche (h) seguido de turno mañana (h+1) 
        if "Noche" in turnos and "Mañana" in turnos:
            for i in range(1, trabajadores + 1):
                # h va de 1 hasta H-1 (el penúltimo día)
                for h in range(1, dias): 
                    lp_content.append(f"  C5_i{i}_h{h}: X_{i}_{h}_Noche + X_{i}_{h+1}_Mañana <= 1")

        # C6. Definicion de fin de semana trabajado (W_if) 
        for i in range(1, trabajadores + 1):
            for f, h_days in weekends.items():
                sum_X_weekend_vars = []
                for h in h_days:
                    for t_name in turnos:
                        var_x = f"X_{i}_{h}_{t_name}"
                        # C6a (Eq. 8): W_if >= X_iht 
                        lp_content.append(f"  C6a_i{i}_f{f}_h{h}_t{t_name}: W_{i}_{f} - {var_x} >= 0")
                        sum_X_weekend_vars.append(var_x)
                
                # C6b (Eq. 9): W_if <= sum(X_iht)
                if sum_X_weekend_vars: # Solo si hay turnos en el FDS
                    lhs_sum = " + ".join(sum_X_weekend_vars)
                    lp_content.append(f"  C6b_i{i}_f{f}: W_{i}_{f} - {lhs_sum} <= 0")

        # C7. No puede trabajar tres fines de semanas consecutivos 
        num_weekends = len(weekends)
        if num_weekends >= 3:
            for i in range(1, trabajadores + 1):
                # f va de 1 hasta |F| - 2
                for f in range(1, num_weekends - 2 + 1):
                    lp_content.append(f"  C7_i{i}_f{f}: W_{i}_{f} + W_{i}_{f+1} + W_{i}_{f+2} <= 2")

        # 3. DECLARACION DE VARIABLES
        
        # Variables X_iht 
        lp_content.append("\nBinary")
        for i in range(1, trabajadores + 1):
            for h in range(1, dias + 1):
                for t_name in turnos:
                    lp_content.append(f"  X_{i}_{h}_{t_name}")
        
        # Variables W_if 
        for i in range(1, trabajadores + 1):
            for f in weekends.keys():
                lp_content.append(f"  W_{i}_{f}")

        # 4. FIN DEL ARCHIVO
        lp_content.append("\nEnd")
        
        # --- GUARDAR ARCHIVO .LP ---
        file_path = f"{carpeta}/instancia_{i}.lp"
        with open(file_path, "w", encoding='utf-8') as f:
            f.write("\n".join(lp_content))
            
        # mensaje de confirmacion
        print(f"Instancia {i} ({size}) generada en .LP: {dias} días, {trabajadores} trabajadores.")


print("Generación completa!!!")
