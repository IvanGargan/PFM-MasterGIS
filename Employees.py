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
import arcpy
import random
import time

#Variables
#arcpy.env.workspace = r"C:\Student\PFM\PFM.gdb"
Employees = arcpy.GetParameter(0)
MoveX = random.uniform(-50,50)
MoveY = random.uniform(-50,50)

#Actualizar coordenadas
with arcpy.da.UpdateCursor(Employees, ["SHAPE@XY"]) as cursor:
    for row in cursor:
        cursor.updateRow([[row[0][0] + MoveX,row[0][1] + MoveY]])

arcpy.MakeFeatureLayer_management(Employees,Employees2,)
time.sleep(30)

print "Script Completed"