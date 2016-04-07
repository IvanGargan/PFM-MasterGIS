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
#Workspace = arcpy.GetParameterAsText(0)
wksp ="C:\Users\Ivan\AppData\Roaming\Esri\Desktop10.3\ArcCatalog\SECURITY@FACILITY.sde"
arcpy.env.workspace = wksp
#Employees = arcpy.GetParameterAsText(1)
#Employees = "Database Connections\SO@FACILITY.sde\Facility.DBO.Employees"
Employees = r"C:\Users\Ivan\AppData\Roaming\Esri\Desktop10.3\ArcCatalog\SECURITY@FACILITY.sde\Facility.DBO.Employees"
#Start an edit session. Must provide the workspace.
edit = arcpy.da.Editor(arcpy.env.workspace)
#Edit session is started without an undo/redo stack for versioned data
#(for second argument, use False for unversioned data)
edit.startEditing(False, True)
#Start an edit operation
edit.startOperation()
i = 0 #Variable para contar las iteraciones
#Try
while True:
    #Variables
    MoveX = random.uniform(-50,50) #Genera numero aleatorio entre -"50" y +"50"
    MoveY = random.uniform(-50,50) #y se suma a las coordenadas del empleado.
    #Actualizar coordenadas con el cursor
    with arcpy.da.UpdateCursor(Employees, ["SHAPE@XY"]) as cursor:
        for row in cursor:
            cursor.updateRow([[row[0][0] + MoveX,row[0][1] + MoveY]])
    #Suponemos que en la decima iteracion se reporta el accidente a los...
    #empleados y dejan de moverse.
    i += 1
    if i == 1:
        break
#Intervalo de tiempo en el que se "mueven" los empleados

#Except

#Stop the edit operation.
edit.stopOperation()
#Stop the edit session and save the changes
edit.stopEditing(True)

print "SCRIPT COMPLETED"