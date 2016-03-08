#-------------------------------------------------------------------------------
# Name: Employees_Movement
# Purpose: PFM
#
# Author: Ivan G.
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

#Parametros
#arcpy.env.workspace = r"C:\Student\PFM\PFM.gdb"
arcpy.env.workspace = r"C:\Users\Ivan\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\SECURITY@FACILITY.sde" #Workspace

#Employees = r"C:\Student\PFM\PFM.gdb\NuclearPowerPlant\Employees"
#Employees = arcpy.GetParameterAsText(1) #FeatureClass

Employees = "C:\Users\Ivan\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\SECURITY@FACILITY.sde\Facility.DBO.Employees"


#Start an edit session. Must provide the workspace.
edit = arcpy.da.Editor(arcpy.env.workspace)

#Edit session is started without an undo/redo stack for versioned data
#(for second argument, use False for unversioned data)
edit.startEditing(False, True)

#Start an edit operation
edit.startOperation()

i = 0 #Variable para contar las iteraciones
try:
    while True:
        #Variables
        MoveX = random.uniform(-5,5) #Genera numero aleatorio entre -"" y +"" y...
        MoveY = random.uniform(-5,5) #...lo suma a las coordenadas del empleado.

        #Actualizar coordenadas con el cursor
        with arcpy.da.UpdateCursor(Employees, ["SHAPE@XY"]) as cursor:
            for row in cursor:
                cursor.updateRow([[row[0][0] + MoveX,row[0][1] + MoveY]])

        #Suponemos que en la decima iteracion se reporta el accidente a los...
        #empleados y dejan de moverse.
        i += 1
        if i == 6:
            break

    #Intervalo de tiempo en el que se "mueven" los empleados
        time.sleep(10)

except arcpy.ExecuteError:
    print "ERROR"

#Stop the edit operation.
edit.stopOperation()

#Stop the edit session and save the changes
edit.stopEditing(True)