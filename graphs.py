import matplotlib.pyplot as plt
import pandas as pd

# LER DADOS DO ARQUIVO
arquivo = "dados.txt"

tempos = []
vr = []  # tensão no resistor
vc = []  # tensão no capacitor

with open(arquivo, "r") as f:
    for linha in f:
        partes = linha.strip().split()
        # só processa linhas no formato: tempo VR VC
        if len(partes) == 3:
            try:
                t = float(partes[0])
                v_r = float(partes[1])
                v_c = float(partes[2])
                tempos.append(t)
                vr.append(v_r)
                vc.append(v_c)
            except:
                pass  # ignora linhas tipo "LED: LIGADO"

# transforma em DataFrame pra facilitar manipulação
df = pd.DataFrame({"Tempo (ms)": tempos, "VR (V)": vr, "VC (V)": vc})

# GRÁFICO 1 — Carga no capacitor 
plt.figure(figsize=(8, 4))
plt.plot(df["Tempo (ms)"], df["VC (V)"], color='green', label='Tensão no Capacitor')
plt.title("Carga no Capacitor (VC × Tempo)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão no Capacitor (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# GRÁFICO 2 — Descarga no resistor 
plt.figure(figsize=(8, 4))
plt.plot(df["Tempo (ms)"], df["VR (V)"], color='red', label='Tensão no Resistor')
plt.title("Descarga no Resistor (VR × Tempo)")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão no Resistor (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# GRÁFICO 3 — Comparação ========
plt.figure(figsize=(8, 4))
plt.plot(df["Tempo (ms)"], df["VC (V)"], color='green', label='Capacitor (VC)')
plt.plot(df["Tempo (ms)"], df["VR (V)"], color='red', label='Resistor (VR)')
plt.title("Comparação: Carga no Capacitor e Descarga no Resistor")
plt.xlabel("Tempo (ms)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
