from cedula import cedula

asiento = 1
tomo = 1
provincia = 1

for i in range(10005):
    asiento = cedula.generar_asiento(asiento)
    tomo = cedula.generar_tomo(asiento, tomo)
    print(provincia, tomo, asiento)