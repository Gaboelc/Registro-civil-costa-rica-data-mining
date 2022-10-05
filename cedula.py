class cedula:
    def generar_asiento(asiento='0000'):
        if int(asiento) < 9:
            asiento = int(asiento)+1
            asiento = '000'+str(asiento)
            return asiento
        elif int(asiento) > 8 and int(asiento) < 99:
            asiento = int(asiento)+1
            asiento = '00'+str(asiento)
            return asiento
        elif int(asiento) > 98 and int(asiento) < 999:
            asiento = int(asiento)+1
            asiento = '0'+str(asiento)
            return asiento
        elif int(asiento) > 998 and int(asiento) < 9999:
            asiento = int(asiento)+1
            asiento = str(asiento)
            return asiento
        else:
            print('Asientos completos')
            asiento = '0000'
            return asiento
        
    def generar_tomo(asiento='0000', tomo='0000'):
        if int(asiento) == 0 and int(tomo) < 9:
            tomo = int(tomo)+1
            tomo = '000'+str(tomo)
            return tomo
        elif int(asiento) == 0 and int(tomo) > 8 and int(tomo) < 99:
            tomo = int(tomo)+1
            tomo = '00'+str(tomo)
            return tomo
        elif int(asiento) == 0 and int(tomo) > 98 and int(tomo) < 999:
            tomo = int(tomo)+1
            tomo = '0'+str(tomo)
            return tomo
        elif int(asiento) == 0 and int(tomo) > 998 and int(tomo) < 10000:
            tomo = int(tomo)+1
            tomo = str(tomo)
            return tomo
        elif int(tomo) > 9999:
            tomo = '0000'
            return tomo
        else:
            return tomo