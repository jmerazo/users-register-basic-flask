from datetime import datetime
#Exporta los datos creados en un archivo plano
class Logs():
    def saveLogs(self, names, email, city):
        export_data = open('users.txt', 'a+')
        now = datetime.today()
        export_data.write("{}".format(now)+" ")
        export_data.write("{}".format(names)+" ")
        export_data.write("{}".format(email)+" ")
        export_data.write("{}".format(city)+"\n")
        export_data.close()