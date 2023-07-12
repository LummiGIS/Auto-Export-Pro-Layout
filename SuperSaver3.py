try:
    '''the APRX must have a text element named mapnumber somewhere
    on the APRX Layout.'''
    import sys
    import traceback
    import datetime
    import arcpy
    import os
    import string
    from time import gmtime, strftime
    import subprocess

    #This is the path to a CSV file.  This path needs to be defined by the user prior to script execution.
    path_to_CSV = r"Z:\GISpublic\GerryG\Python3\SuperSaverArcPro\LIBC_GISMapList_2022.txt"
    
    CartographersName = arcpy.GetParameterAsText(0)

    RequestersName = arcpy.GetParameterAsText(1)

    RequestersDepartment = arcpy.GetParameterAsText(2)

    ProjectName = arcpy.GetParameterAsText(3)

    ProjectArea = arcpy.GetParameterAsText(4)

    keysearchwords = arcpy.GetParameterAsText(5)

    ExportToPDF = arcpy.GetParameterAsText(6)

    ExportToJPG = arcpy.GetParameterAsText(7)

    OpenOutputDirectory = arcpy.GetParameterAsText(8)

    OpenExportedFile = arcpy.GetParameterAsText(9)

    arcpy.AddMessage("Save and Export APRX Created by Gerry Gabrisch GISP, GIS Manager Lummi Indian Business Council, geraldg@lummi-nsn.gov\n")

   
    def get_time():
        #gets the current date and time.  This is the map ID number....
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    def get_path(aprx):
        #get the path and file name of the aprx...
        aprx_file = aprx.filePath
        #get the the same except drop the aprx suffex and return that...
        return aprx_file.split(".")[0]
        
    def make_outfile_name(end_path, mapnumber, suffix):
        return end_path + '_' + mapnumber + '.' + suffix
        
    #start the project file...
    aprx = arcpy.mp.ArcGISProject("CURRENT")

    #Create the map ID number which is YYYYMMDDHHMMSS
    mapnumber = get_time()
    
    #Get the name of the active map view....
    view = aprx.activeView
    #activate the text element...
    ele = view.listElements("TEXT_ELEMENT", "mapnumber")[0]
    #assign the mapnumber to the map....
    ele.text = mapnumber
    
    #get the layout in dpi rather so the whole layout is exported and not just some piece of it.
    page_width = view.pageWidth * 96
    page_height = view.pageHeight * 96
    aprx.save()
    
    #Get the full path to the location of the aprx
    end_path = get_path(aprx)
    
    #open the text file, write the values to the text file and close the text file....
    f = open(path_to_CSV, 'a')
    f.write(mapnumber +', '+ CartographersName +', '+  RequestersName +', '+ RequestersDepartment   +', '+ ProjectName +', '+  ProjectArea+', '+ keysearchwords +', '+ aprx.filePath+'\n')
    f.close()
    
    if ExportToPDF == 'true':
        #view.exportToPDF(r"C:\gTemp\aaatest.pdf", 96, 'BEST')
        arcpy.AddMessage("Exporting to PDF")
        out_file = make_outfile_name(end_path, mapnumber, 'pdf')
        view.exportToPDF(out_file)
        arcpy.AddMessage("Your output file is: " + out_file)
        if OpenExportedFile == 'true':
            os.popen(out_file)
            
    if ExportToJPG == 'true':
        arcpy.AddMessage("Exporting to JPG")
        out_file = make_outfile_name(end_path, mapnumber, 'jpg')
        view.exportToJPEG(out_file)
        arcpy.AddMessage("Your output file is: " + out_file)
        if OpenExportedFile == 'true':
            os.popen(out_file)      
    
    if OpenOutputDirectory == 'true':
        arcpy.AddMessage("Opening output directory")
        arcpy.AddMessage(aprx.filePath)
        filestring ='explorer ' + '"' + os.path.dirname(aprx.filePath) + '"'
        #subprocess(os.path.dirname(aprx.filePath))
        os.popen(filestring)

    aprx.save()
    del aprx
    arcpy.AddMessage("Your output file is: " + out_file)
    
except arcpy.ExecuteError: 
    # Get the tool error messages 
    msgs = arcpy.GetMessages(2) 
    # Return tool error messages for use with a script tool 
    arcpy.AddError(msgs) 
    # Print tool error messages for use in Python
    print(msgs)
except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    # Return Python error messages for use in script tool or Python window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)
    # Print Python error messages for use in Python / Python window
    print(pymsg)
    print(msgs)
