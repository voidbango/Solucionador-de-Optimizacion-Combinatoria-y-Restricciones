import random
import numpy as np
import os

rangos_generador_instancias = {
    "pequena": {
        "dias": (5, 7),
        "trabajadores": (5, 15),
        "turnos": ["DAY", "NIGHT"]
    },
    "mediana": {
        "dias": (7, 14),
        "trabajadores": (15, 45),
        "turnos": ["MORNING", "AFTERNOON", "NIGHT"]
    },
    "grande": {
        "dias": (14, 28),
        "trabajadores": (45, 90),
        "turnos": ["MORNING", "AFTERNOON", "NIGHT"]
    }
}

os.makedirs("instancias_lp", exist_ok=True)

for size, settings in rangos_generador_instancias.items():

    carpeta = f"instancias_lp/{size}"
    os.makedirs(carpeta, exist_ok=True)

    for i in range(1, 6):

        dias = random.randint(*settings["dias"])
        trabajadores = random.randint(*settings["trabajadores"])
        turnos = settings["turnos"]

        media = trabajadores / len(turnos)
        desviacion = media * 0.2

        requerimientos = {
            (h+1, t): max(1, int(np.random.normal(media, desviacion)))
            for h in range(dias)
            for t in turnos
        }

        disposicion = np.random.randint(0, 11, size=(trabajadores, dias, len(turnos)))

        weekends = {}
        f_counter = 1
        for h in range(1, dias + 1):
            dow = (h - 1) % 7 + 1
            if dow in (6, 7):
                weekends.setdefault(f_counter, []).append(h)
            if dow == 7:
                f_counter += 1

        lp = []

        # ============================
        # OBJETIVO
        # ============================

        lp.append("/* Funcion objetivo consistente con modelo */")
        obj = []
        for i_idx in range(trabajadores):
            for h_idx in range(dias):
                for t_idx, t in enumerate(turnos):
                    val = disposicion[i_idx, h_idx, t_idx]
                    if val > 0:
                        obj.append(f"{val} X_{i_idx+1}_{h_idx+1}_{t}")

        lp.append("max " + " + ".join(obj) + " ;\n")

        lp.append("subject to\n")
        lp.append("/* Restricciones */")

        # ============================
        # C2 Cobertura
        # ============================

        for h in range(1, dias + 1):
            for t in turnos:
                R = requerimientos[(h, t)]
                lhs = " + ".join([f"X_{i+1}_{h}_{t}" for i in range(trabajadores)])
                lp.append(f"{lhs} = {R} ;")

        # ============================
        # C3 disponibilidad
        # ============================

        lp.append("/* C3: disponibilidad consistente con modelo */")
        for i_idx in range(trabajadores):
            for h_idx in range(dias):
                for t_idx, t in enumerate(turnos):
                    if disposicion[i_idx, h_idx, t_idx] == 0:
                        lp.append(f" X_{i_idx+1}_{h_idx+1}_{t} <= 0 ;")

        # ============================
        # C4 max 2 turnos por día
        # ============================

        lp.append("/* C4: consistente con modelo (<= 1) */")
        for w in range(1, trabajadores + 1):
            for d in range(1, dias + 1):
                lhs = " + ".join([f"X_{w}_{d}_{t}" for t in turnos])
                lp.append(f"{lhs} <= 2 ;")

        # ============================
        # C5 NIGHT → MORNING
        # ============================

        lp.append("/* C5: prohibir turno night->morning */")
        for w in range(1, trabajadores + 1):
            for d in range(1, dias):
                if "MORNING" in turnos:
                    lp.append(f"X_{w}_{d}_NIGHT + X_{w}_{d+1}_MORNING <= 1 ;")

                elif "DAY" in turnos:
                    lp.append(f"X_{w}_{d}_NIGHT + X_{w}_{d+1}_DAY <= 1 ;") 

        # ============================
        # C6 fines de semana
        # ============================

        lp.append("/* C6: consistente, define W_if correctamente */")
        for w in range(1, trabajadores + 1):
            for f, days in weekends.items():
                sum_vars = []
                for d in days:
                    for t in turnos:
                        var = f"X_{w}_{d}_{t}"
                        lp.append(f" W_{w}_{f} - {var} >= 0 ;")
                        sum_vars.append(var)

                lp.append(f" W_{w}_{f} - " + " - ".join(sum_vars) + " <= 0 ;")

        # ============================
        # C7 no 3 fines seguidos
        # ============================

        lp.append("/* C7 */")
        num_f = len(weekends)
        if num_f >= 3:
            for w in range(1, trabajadores + 1):
                for f in range(1, num_f - 1):
                    lp.append(f" W_{w}_{f} + W_{w}_{f+1} + W_{w}_{f+2} <= 2 ;")

        # ============================
        # DECLARACIÓN DE VARIABLES BINARIAS
        # ============================

        lp.append("\n/* Declaración de variables binarias */")
        bin_vars = []

        # X variables
        for i_id in range(1, trabajadores + 1):
            for h in range(1, dias + 1):
                for t in turnos:
                    bin_vars.append(f"X_{i_id}_{h}_{t}")

        # W variables
        for i_id in range(1, trabajadores + 1):
            for f in weekends.keys():
                bin_vars.append(f"W_{i_id}_{f}")

        lp.append("bin " + ", ".join(bin_vars) + " ;\n")


        file_path = f"{carpeta}/instancia_{i}.lp"

        with open(file_path, "w", encoding="latin-1", errors="replace") as f:
            f.write("\n".join(lp))

        print(f"Instancia {i} ({size}) generada: {dias} días, {trabajadores} trabajadores.")

print("¡Generación completada!")


