from cedula import cedula
from scrap_bot import scrap_bot

import pandas as pd

asiento = '0514'
tomo = '1822'
provincia = 1


bot = scrap_bot()
bot.access()

for i in range(5): #10005
    asiento = cedula.generar_asiento(asiento)
    tomo = cedula.generar_tomo(asiento, tomo)
    
    cedula_consulta = str(provincia)+str(tomo)+str(asiento)
    
    bot.consulta(cedula_consulta)
    
    bot.collect_data()
    
    bot.nueva_consulta()