from cedula import cedula
from scrap_bot import scrap_bot

import pandas as pd

asiento = '0340'
tomo = '0828'
provincia = 1


bot = scrap_bot()
bot.access()

while True:
    asiento = cedula.generar_asiento(asiento)
    tomo = cedula.generar_tomo(asiento, tomo)
    
    cedula_consulta = str(provincia)+str(tomo)+str(asiento)
    
    try:
        df = pd.read_csv('./data.csv')
        df = df.set_index('Numero de cedula')
    
        bot.consulta(cedula_consulta)
        
        datos_recolectados = bot.collect_data()
        
        new_df = pd.DataFrame(datos_recolectados, index=[0])
        new_df = new_df.set_index('Numero de cedula')
        
        df2 = pd.concat([df, new_df])
        df2.to_csv('./data.csv')
        
        bot.nueva_consulta()
    except:
        bot.nueva_consulta()
        
bot.drvr.close()
