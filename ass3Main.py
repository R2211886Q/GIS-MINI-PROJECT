import tkinter as tk
from tkinter import filedialog
import updateProperty
import createDataframe

def selectGeodatabase():
    root = tk.Tk()
    root.withdraw()
    geodatabase_path = filedialog.askdirectory(title="Select Geodatabase Folder")
    return geodatabase_path

def main():
    # Select the geodatabase folder using the GUI
    geodatabase_path = selectGeodatabase()

    # Update property locality using different spatial operators
    operators = ["WITHIN", "INTERSECT", "HAVE_THEIR_CENTER_IN"]
    for operator in operators:
        result = updateProperty.updateProperty(operator)
        print(result)

    # Create a DataFrame for analysis and visualization
    dataframe = createDataframe.createDataframe()
    if dataframe is not None:
        # Perform analysis and visualization tasks using the DataFrame
        pass

# Execute the main script
if __name__ == "__main__":
    main()