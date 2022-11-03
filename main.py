from cedula import cedula
from scrap_bot import scrap_bot
import sys

import pandas as pd

arg = sys.argv[1:]

provincia = arg[0]
tomo = arg[1]
asiento = arg[2]
cantidad = int(arg[3])

buffer_size = 999

df_buffer = pd.DataFrame(columns=['Numero de cedula','Nombre completo',
                                  'Fecha de nacimiento','Edad','Nacionalidad',
                                  'Marginal','Conocido/a como','Nombre del padre',
                                  'Cedula del padre','Nombre de la madre',
                                  'Cedula de la madre'])
df_buffer = df_buffer.set_index('Numero de cedula')

bot = scrap_bot()
bot.access()

if cantidad >= buffer_size:
    for run in range(cantidad):
        asiento = cedula.generar_asiento(asiento)
        tomo = cedula.generar_tomo(asiento, tomo)
    
        cedula_consulta = str(provincia)+str(tomo)+str(asiento)
    
        try:
            bot.consulta(cedula_consulta)

            datos_recolectados = bot.collect_data()
            df_buffer = pd.concat([df_buffer, pd.DataFrame(datos_recolectados, index=[0])])

            if len(df_buffer) == buffer_size:    
                df = pd.read_csv('./data.csv')
                df = df.set_index('Numero de cedula')

                df_buffer = df_buffer.set_index('Numero de cedula')

                df_result = pd.concat([df, df_buffer])
                df_result.to_csv('./data.csv')

                df_buffer = pd.DataFrame(columns=['Numero de cedula','Nombre completo',
                                                  'Fecha de nacimiento','Edad',
                                                  'Nacionalidad','Marginal',
                                                  'Conocido/a como','Nombre del padre',
                                                  'Cedula del padre','Nombre de la madre',
                                                  'Cedula de la madre'])

            bot.nueva_consulta()
        except:
            bot.nueva_consulta()
else:
    print(f'''
          ============================================================================
                                           ---ERROR---
          La cantidad de cedular a minar tienen que ser mayor o igual a: {buffer_size}
          La cantidad actual es de: {cantidad}
          ============================================================================''')
        
bot.drvr.close()

print('''
      ============================================================================
                         Todas las cedulas fueron recolectadas
      ============================================================================''')