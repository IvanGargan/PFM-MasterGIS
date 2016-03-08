#-------------------------------------------------------------------------------
# Name: Closest_Facilities
# Purpose: PFM
#
# Author: Ivan G.
#
# Created:     07/03/2016
# Copyright:   (c) Ivan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Importar librerias de Arcpy.
import arcpy

#Sobreescribir Output
arcpy.env.overwriteOutput = True

#Parametros
#arcpy.env.workspace = "C:\Users\Ivan\AppData\Roaming\ESRI\Desktop10.3\ArcCatalog\SECURITY@FACILITY.sde"

arcpy.env.workspace = arcpy.GetParameterAsText(0) #Workspace
Network_Dataset = arcpy.GetParameterAsText(1)     #Facility_ND
SafeAreas = arcpy.GetParameterAsText(2)           #Facilities
Employees = arcpy.GetParameterAsText(3)           #Employees
Polygon_Barriers = arcpy.GetParameterAsText(4)    #Indcidents

Measurement_Units = "meters"
Output_Geodatabase = arcpy.env.workspace
Output_Routes_Name ="Rutas"
Output_Directions_Name = "Direcciones"
Output_Closest_Facilities_Name ="Facilities"

arcpy.FindClosestFacilities_na(Employees, SafeAreas, Measurement_Units,
    Network_Dataset, "", Output_Routes_Name,
    Output_Directions_Name, Output_Closest_Facilities_Name,
    "1", "", "TRAVEL_TO", "", "", "", "ALLOW_UTURNS",
    "", "", Polygon_Barriers)

print "Script Completed"