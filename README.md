# Auto-Export-Pro-Layout
ArcGIS Pro Auto-Export Layout to PDF or JPEG with map ID and metadata.

!!!This tool fails at line 52 when executed from a Catalog Pane but runs fine when executed from the Catalog View.

The script will update a user-defined text box located on the active layout with a unique ID (the ID is the export time - YYYYMMDDHHMMSS).  The script will then export the active layout to a PDF, JPEG, or both to the same directory as the APRX file.  The exported file(s) will share the name of the APRX but with the timestamp ID appended to the file name.  Options include whether to open the PDF or JPEG with your default viewer software, or open Windows File Explorer in the directory of the output (for easy cutting and pasting into an email!).   The script prompts the user for some optional input parameters like who, what, where, and why.  These values are written to a CSV file along with the project output path.   If you are asked to reproduce a map you made ages ago you can search the CSV file for names, dates, ID numbers, or project locations and find the project.  

The user will need some basic Python skills to open the tool and set the paths to a CSV file in a directory the users has write permissions to. Add the tool to your Catalog Pane, right-click the script and choose edit.  Find the path_to_csv varialble on line 13.  Set the path to a new blank CSV file. Your layout needs to have an existing textbox called mapnumber in the layout prior to execution.  


Here is a screen shot of an active layout in ArcGIS Pro v3 with the mapnumber text box added.
screen shot(https://github.com/LummiGIS/Auto-Export-Pro-Layout/blob/main/supersaver.JPG?raw=true)

Here is a screen shot of the code where you need to set the path.
code change(https://github.com/LummiGIS/Auto-Export-Pro-Layout/blob/main/scriptcode.JPG?raw=true)
