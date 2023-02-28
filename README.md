# Auto-Export-Pro-Layout
ArcGIS Pro Auto-Export Layout to PDF or JPEG with map ID and metadata.

The script will update a user-defined text box located on the active layout with a unique ID (the ID is the export time - YYYYMMDDHHMMSS).  The script will then export the active layout to a PDF, JPEG, or both to the same directory as the APRX file.  The exported file(s) will share the name of the APRX but with the timestamp ID appended to the file name.  Options include whether to open the PDF or JPEG with your default viewer software, or open Windows File Explorer in the directory of the output (for easy cutting and pasting into an email!).   The script prompts the user for some optional input parameters like who, what, where, and why.  These values are written to a CSV file along with the project output path.   If you are asked to reproduce a map you made ages ago you can search the CSV file for names, dates, ID numbers, or project locations and find the project.  

