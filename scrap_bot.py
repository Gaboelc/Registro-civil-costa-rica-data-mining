from selenium import webdriver
from time import sleep
import logging

class scrap_bot:
    
    def __init__(self):
        self.webdriver_path = 'webdriver\chromedriver.exe'
        self.drvr = webdriver.Chrome(self.webdriver_path)
        self.drvr.maximize_window()
        
        logging.basicConfig(
            level=logging.INFO,
            format='{asctime} {levelname:<8} {message}',
            style='{',
            filename='%slog' % __file__[:-2],
            filemode='w'
        )
        
    def access(self):
        try:
            self.drvr.get('https://servicioselectorales.tse.go.cr/chc/consulta_cedula.aspx')
            print('''
                  ====================================================================
                                        Pagina accesada correctamente!
                  ====================================================================''')
            logging.info('Pagina accesada correctamente')
            sleep(3)
        except:
            print('''
                  ====================================================================
                                           Pagina no accesada!
                  ====================================================================''')
            logging.error('Pagina no accesada')
            
    def consulta(self, cedula):
        cedula_input = self.drvr.find_element('id', 'txtcedula')
        cedula_input.send_keys(str(cedula))
        print(f'''
                  ====================================================================
                   Consulta nueva va a ser realizada
                   La cedula a ser consultada va a ser: {cedula}
                  ====================================================================''')
        
        logging.info('Consulta nueva va a ser realizada')
        logging.info(f'La cedula a ser consultada es: {cedula}')
        consulta = self.drvr.find_element('id', 'btnConsultaCedula')
        consulta.click()
        sleep(3)
        
    def nueva_consulta(self):
        try:
            consulta_cedula = self.drvr.find_element('xpath', '//*[@id="ImageConsultaCedula"]') 
            consulta_cedula.click()
            sleep(3)
        except:
            print('''
                  ====================================================================
                                          Cedula no encontrada
                  ====================================================================
                  ''')
            logging.error('Cedula no encontrada')
            regresar = self.drvr.find_element('id', 'Button1')
            regresar.click()
            sleep(3)
            consulta_por_cedula = self.drvr.find_element('xpath', '/html/body/table/tbody/tr/td/div/div[2]/a[2]')
            consulta_por_cedula.click()
            sleep(3)
            
    def collect_data(self):
        try:
            print('''
                  ====================================================================
                                        Recolectando los datos!
                  ====================================================================''')
            self.cedula = self.drvr.find_element('id', 'lblcedula').text
            self.nombre = self.drvr.find_element('id', 'lblnombrecompleto').text
            self.conocido = self.drvr.find_element('id', 'lblconocidocomo').text
            self.fecha_nacimiento = self.drvr.find_element('id', 'lblfechaNacimiento').text
            self.nacionalidad = self.drvr.find_element('id', 'lblnacionalidad').text
            self.edad = self.drvr.find_element('id', 'lbledad').text
            self.marginal = self.drvr.find_element('id', 'lblLeyendaMarginal').text
            
            self.padre = self.drvr.find_element('id', 'lblnombrepadre').text
            self.cedula_padre = self.drvr.find_element('id', 'lblid_padre').text
            self.madre = self.drvr.find_element('id', 'lblnombremadre').text
            self.cedula_madre = self.drvr.find_element('id', 'lblid_madre').text
            
            if self.conocido == '':
                self.conocido = None
            else:
                self.conocido = self.conocido
                
            if self.marginal == 'NO':
                self.marginal = False
            else:
                self.marginal = True
            
            self.data = {'Numero de cedula':self.cedula, 'Nombre completo':self.nombre,
                         'Fecha de nacimiento':self.fecha_nacimiento, 'Edad':self.edad,
                         'Nacionalidad':self.nacionalidad, 'Marginal':self.marginal,
                         'Conocido/a como': self.conocido, 'Nombre del padre': self.padre,
                         'Cedula del padre': self.cedula_padre, 'Nombre de la madre': self.madre,
                         'Cedula de la madre': self.cedula_madre}
            
            print(f'''
                  --------------------------------------------------------------------
                  Datos Recolectados:
                    Nombre Completo: {self.nombre}
                    Cedula: {self.cedula}
                    Fecha de nacimiento: {self.fecha_nacimiento}
                    Edad: {self.edad}
                    Nacionalidad: {self.nacionalidad}
                    Marginal: {self.marginal}
                    Conocido/a como: {self.conocido}
                    
                    Nombre del padre: {self.padre}
                    Cedula del padre: {self.cedula_padre}
                    
                    Nombre de la madre: {self.madre}
                    Cedula de la madre: {self.cedula_madre}
                  --------------------------------------------------------------------''')
            
            logging.info('Datos recolectados')
            
            return self.data
        except:
            print('''
                  ====================================================================
                                          Datos no recolectados
                  ====================================================================
                  ''')
            logging.error('Datos no recolectados')