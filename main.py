from webscrp import *
from users import Users


bot = InstBot(hide=1,brwDrive='chromedriver.exe',pathFolder='E:\TESTE')

if (bot.buscarlink(Users.linkp)):
    bot.login(Users.usernamep,Users.passwordp)
    time.sleep(5)
    bot.tqreprd()
    quantidade = bot.qtdfts()

    for qtd in quantidade:

        listsrcfoto = bot.listaimg()
        fullname = bot.geranomefoto()
        pathdafoto = bot.fotonapasta(fullname)
        bot.downloadf(listsrcfoto,pathdafoto)
        bot.passarfoto()

    bot.ZipPasta()
    bot.fecha()









