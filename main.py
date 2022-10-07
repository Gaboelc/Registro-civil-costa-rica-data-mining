from cedula import cedula
from scrap_bot import scrap_bot

import pandas as pd

asiento = '0000'
tomo = '0000'
provincia = 0


bot = scrap_bot()
bot.access()

for i in range(1): #10005
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
        bot.consulta_cedula()
        
bot.drvr.close()