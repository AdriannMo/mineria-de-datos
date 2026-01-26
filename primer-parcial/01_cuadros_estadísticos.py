
import numpy as np
import pandas as pd
from io import StringIO

raw = """Marca temporal\tNúmero de matrícula\t¿Cuántos años cumplidos tienes?\t¿Has realizado programas utilizando Python?\t¿Has utilizado Google Colab?\t¿Tienes cuenta de GitHub?
19/01/2026 18:32:18\t178920\t22\tSi\tNo\tSi
19/01/2026 18:32:23\t182712\t21\tSi\tNo\tSi
19/01/2026 18:32:25\t180370\t26\tSi\tSi\tSi
19/01/2026 18:32:27\t182570\t21\tSi\tSi\tSi
19/01/2026 18:32:28\t177622\t24\tSi\tNo\tSi
19/01/2026 18:32:29\t175166\t22\tSi\tSi\tSi
19/01/2026 18:32:30\t177573\t22\tSi\tSi\tSi
19/01/2026 18:32:35\t178430\t21\tSi\tSi\tSi
19/01/2026 18:32:38\t179169\t23\tSi\tNo\tSi
19/01/2026 18:32:41\t177263\t22\tSi\tSi\tSi
19/01/2026 18:32:48\t179884\t23\tSi\tNo\tSi
19/01/2026 18:32:48\t183016\t22\tSi\tNo\tSi
19/01/2026 18:32:50\t179033\t23\tSi\tSi\tNo
19/01/2026 18:32:54\t178218\t22\tSi\tNo\tSi
19/01/2026 18:32:55\t178446\t22\tSi\tSi\tSi
19/01/2026 18:33:00\t178166\t22\tSi\tSi\tNo
19/01/2026 18:33:02\t177406\t22\tSi\tNo\tSi
19/01/2026 18:33:05\t177192\t22\tSi\tSi\tSi
19/01/2026 18:33:08\t182451\t21\tSi\tNo\tSi
19/01/2026 18:33:08\t171513\t24\tNo\tNo\tSi
19/01/2026 18:33:09\t181619\t21\tSi\tNo\tSi
19/01/2026 18:33:12\t182298\t23\tSi\tNo\tSi
19/01/2026 18:33:14\t181419\t24\tNo\tNo\tSi
19/01/2026 18:33:32\t177291\t21\tSi\tSi\tSi
19/01/2026 18:33:42\t182085\t22\tSi\tNo\tSi
19/01/2026 18:33:53\t176453\t22\tSi\tNo\tSi
19/01/2026 18:34:04\t176263\t24\tSi\tNo\tSi
19/01/2026 18:34:06\t179997\t21\tSi\tNo\tSi
19/01/2026 18:36:21\t175842\t23\tSi\tNo\tNo
19/01/2026 20:19:21\t179913\t20\tSi\tNo\tSi
19/01/2026 20:19:48\t177301\t22\tSi\tSi\tNo
19/01/2026 20:20:06\t183060\t21\tSi\tNo\tSi
19/01/2026 20:20:08\t177935\t22\tSi\tSi\tSi
19/01/2026 20:20:19\t177700\t20\tSi\tSi\tSi
19/01/2026 20:20:26\t178318\t24\tSi\tSi\tSi
19/01/2026 20:20:27\t174653\t24\tSi\tNo\tSi
19/01/2026 20:20:29\t177139\t21\tSi\tNo\tSi
19/01/2026 20:20:31\t173479\t25\tSi\tNo\tNo
19/01/2026 20:20:39\t175588\t23\tNo\tNo\tSi
19/01/2026 20:20:45\t178774\t23\tSi\tSi\tSi
19/01/2026 20:20:45\t175031\t23\tSi\tNo\tNo
19/01/2026 20:20:49\t178396\t21\tSi\tSi\tSi
19/01/2026 20:20:49\t172068\t23\tNo\tNo\tNo
19/01/2026 20:20:50\t174197\t23\tNo\tNo\tSi
19/01/2026 20:20:55\t178584\t22\tSi\tNo\tSi
19/01/2026 20:20:55\t175329\t24\tSi\tNo\tSi
19/01/2026 20:20:56\t177685\t22\tSi\tSi\tSi
19/01/2026 20:20:57\t178678\t22\tNo\tNo\tSi
19/01/2026 20:21:04\t177143\t22\tSi\tNo\tSi
19/01/2026 20:21:07\t182318\t26\tSi\tNo\tSi
19/01/2026 20:21:27\t182377\t20\tSi\tNo\tSi
19/01/2026 20:21:34\t179419\t22\tSi\tNo\tNo
19/01/2026 20:21:35\t181662\t21\tSi\tNo\tSi
19/01/2026 20:21:38\t181760\t21\tSi\tNo\tSi
19/01/2026 20:22:06\t177888\t22\tSi\tNo\tSi
19/01/2026 20:22:15\t176535\t25\tSi\tNo\tSi
19/01/2026 20:22:29\t179862\t21\tSi\tNo\tSi
19/01/2026 20:22:32\t178378\t22\tSi\tNo\tSi
19/01/2026 20:22:50\t177451\t22\tSi\tNo\tSi
19/01/2026 20:23:15\t179804\t21\tSi\tNo\tSi
"""

# Cargar datos
df = pd.read_csv(StringIO(raw), sep='\t')
df.columns = [c.strip() for c in df.columns]

# Variables
df['edad'] = pd.to_numeric(df['¿Cuántos años cumplidos tienes?'], errors='coerce')
map_sn = {'Si': True, 'No': False}
df['prog_python'] = df['¿Has realizado programas utilizando Python?'].map(map_sn)
df['usa_colab'] = df['¿Has utilizado Google Colab?'].map(map_sn)
df['cuenta_github'] = df['¿Tienes cuenta de GitHub?'].map(map_sn)

# A NumPy
edad = df['edad'].to_numpy(dtype=float)
prog_py = df['prog_python'].to_numpy(dtype=bool)
usa_colab = df['usa_colab'].to_numpy(dtype=bool)
cuenta_gh = df['cuenta_github'].to_numpy(dtype=bool)

# Descriptivos de edad (NumPy)
summary_age = {
    'n': int(edad.size),
    'min': float(np.min(edad)),
    'p25': float(np.percentile(edad, 25)),
    'mediana': float(np.median(edad)),
    'media': float(np.mean(edad)),
    'p75': float(np.percentile(edad, 75)),
    'max': float(np.max(edad)),
    'rango(ptp)': float(np.ptp(edad)),
    'var_muestral': float(np.var(edad, ddof=1)),
    'std_muestral': float(np.std(edad, ddof=1)),
    'cv': float(np.std(edad, ddof=1)/np.mean(edad)),
}

# Frecuencias (NumPy)
freq_python = {'Si': int(np.count_nonzero(prog_py)), 'No': int(edad.size - np.count_nonzero(prog_py))}
freq_colab  = {'Si': int(np.count_nonzero(usa_colab)), 'No': int(edad.size - np.count_nonzero(usa_colab))}
freq_gh     = {'Si': int(np.count_nonzero(cuenta_gh)), 'No': int(edad.size - np.count_nonzero(cuenta_gh))}

# Tablas cruzadas (NumPy)
def tabla2x2(a, b):
    t = np.zeros((2,2), dtype=int)
    t[1,1] = np.count_nonzero(a & b)
    t[1,0] = np.count_nonzero(a & ~b)
    t[0,1] = np.count_nonzero(~a & b)
    t[0,0] = np.count_nonzero(~a & ~b)
    return t

tab_py_colab = tabla2x2(prog_py, usa_colab)
tab_py_gh    = tabla2x2(prog_py, cuenta_gh)
tab_colab_gh = tabla2x2(usa_colab, cuenta_gh)

# Medias de edad por grupo (NumPy)
means_by_group = {
    'edad_promedio_Python': {'Si': float(np.mean(edad[prog_py])) if np.any(prog_py) else np.nan,
                             'No': float(np.mean(edad[~prog_py])) if np.any(~prog_py) else np.nan},
    'edad_promedio_Colab':  {'Si': float(np.mean(edad[usa_colab])) if np.any(usa_colab) else np.nan,
                             'No': float(np.mean(edad[~usa_colab])) if np.any(~usa_colab) else np.nan},
    'edad_promedio_GitHub': {'Si': float(np.mean(edad[cuenta_gh])) if np.any(cuenta_gh) else np.nan,
                             'No': float(np.mean(edad[~cuenta_gh])) if np.any(~cuenta_gh) else np.nan},
}

summary_age, freq_python, freq_colab, freq_gh, tab_py_colab, tab_py_gh, tab_colab_gh, means_by_group
