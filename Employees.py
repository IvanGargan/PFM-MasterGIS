#-------------------------------------------------------------------------------
# Name:        Employees
# Purpose:
#
# Author:      Ivan
#
# Created:     17/02/2016
# Copyright:   (c) Ivan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Importar librerias de Arcpy, Aleatorio y tiempo.
import arcpy
import random
import time

#Sobreescribir
arcpy.env.overwriteOutput = True

#Variables
arcpy.env.workspace = r"C:\Student\PFM\PFM.gdb"#arcpy.GetParameterAsText(0) #Workspace
Employees = r"C:\Student\PFM\PFM.gdb\NuclearPowerPlant\Employees" #arcpy.GetParameter(1) #FeatureClass
MoveX = random.uniform(-50,50) #Genera numero aleatorio entre -50 y 50 y...
MoveY = random.uniform(-50,50) #...lo suma a las coordenadas del empleado.

#Actualizar coordenadas con el cursor
with arcpy.da.UpdateCursor(Employees, ["SHAPE@XY"]) as cursor:
    for row in cursor:
        cursor.updateRow([[row[0][0] + MoveX,row[0][1] + MoveY]])

#Creacion de una layer para evitar locks
lyr = arcpy.MakeFeatureLayer_management("Employees","Employees_layer")

#Intervalo de tiempo en el que se "mueven" los empleados
time.sleep(5)

print "Script Completed"