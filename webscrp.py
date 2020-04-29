from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import random
import shutil
import re


#https://pbpython.com/pathlib-intro.html
from pathlib import Path



'''
Antes de tudo este código precisa de uma pasta chamada TESTE
Futuramente as features que o código precisa são

1.Fatorar o código em metodos dentro da classe
3.Criar try para verificar erros
4.Criar senha para o arquivo zip
5.Estabelecer sequencia de numeros para cada pasta e arquivos
6.remover a pasta criada

'''


class InstBot:



    def __init__(self,hide=0,brwDrive="",pathFolder =""):

        self.pathfolder = pathFolder
        Path(pathFolder).mkdir(parents=True, exist_ok=True)
        options = Options()

        if hide == 1:
            options.headless = True
            options.add_argument("--mute-audio")

        self.driver = webdriver.Chrome(brwDrive, options=options)

    def login(self,username,password):

        campo_usuario = self.driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(username)
        campo_senha = self.driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(password)
        campo_senha.send_keys(Keys.RETURN)

    def listaimg (self):

        # Retorna uma lista de links das fotos do stori
        img = self.driver.find_elements_by_tag_name('img')
        srcimg = [elem.get_attribute('src') for elem in img]
        return srcimg

    def qtdfts(self):

        #retorna a quantidade de imagens
        quantidade = self.driver.find_elements_by_class_name('_7zQEa')
        return quantidade

    def tqreprd(self):

        # Click para começar
        self.driver.find_element_by_class_name('sqdOP.yWX7d._4pI4F._8A5w5').click()

    def geranomefoto(self):
        img_name = random.randrange(100, 500)
        full_name = str(img_name) + '.jpg'
        print(full_name)
        return full_name

    def fotonapasta(self,full_name):

        #filepath = os.path.join(self.pathfolder, full_name)
        #filepath = self.pathfolder + "\\" + full_name
        filepath = Path.cwd().joinpath(self.pathfolder, full_name)
        print(filepath)
        return filepath

    def downloadf(self,srcimg, filepath):

        #Este metodo recebe a lista de fotos da pagina atual e baixa a foto no local e nome especificado
        urllib.request.urlretrieve(srcimg[1], filepath)

    def passarfoto(self):
        # Click para passar de foto
        self.driver.find_element_by_class_name("coreSpriteRightChevron").click()

    def ZipPasta(self):
        shutil.make_archive(self.pathfolder,'zip',self.pathfolder)


    def buscarlink(self,bLink):

        self.driver.get(bLink)
        '''if status == None:
            print('Não foi possivel encontrar o link especificado')'''

        time.sleep(2)
        novaurl = re.sub('/stories', '', bLink)
        urlatual = self.driver.current_url
        if novaurl == urlatual:
            self.driver.close()
            print('Nada')
            return False
        else:
            return True

    def fecha(self):
        self.driver.close()

















''' Este for serve para verificar qual o nome dos botões da pagina

        for bt in srcbt:
            print(bt)
            
    #este campo é só para conferir quantos botoes existem
    
        print('Botões: ' + str(len(srcbt)))
        
    #Este comando impirime o link das fotos
        print(srcimg[1])

'''





