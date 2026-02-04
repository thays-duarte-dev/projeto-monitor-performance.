# PROJETO: MONITOR DE PERFORMANCE
# DESENVOLVEDORA: THAYS

def analisar_sistema(modulo, cpu, ram):
    # Calcula a media de uso
    uso_medio = (cpu + ram) / 2
    status = "ESTAVEL" if uso_medio < 60 else "ALERTA"
    
    return f"MODULO: {modulo} | USO: {uso_medio}% | STATUS: {status}"

# Execução final sem erro:
resultado = analisar_sistema("Core_Data_v1", 20, 35)

print("-" * 35)
print(resultado)
print("-" * 35)