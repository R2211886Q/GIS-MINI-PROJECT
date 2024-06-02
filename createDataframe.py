import arcpy
import pandas as pd

def createDataframe():
    try:
        # Connect to the geodatabase
        arcpy.env.workspace = "Toowoomba_2024.gdb"

        # Read the data from the feature class into a pandas DataFrame
        fields = ["FIELD1", "FIELD2", "LOCALITY"]
        df = pd.DataFrame([row for row in arcpy.da.SearchCursor("TWB_Property", fields)],
                          columns=fields)

        # Perform any necessary data manipulation or analysis here

        return df

    except arcpy.ExecuteError:
        # Handle any arcpy errors
        print(arcpy.GetMessages())
        return None

    except Exception as e:
        # Handle any other exceptions
        print(str(e))
        return None


# Example usage:
dataframe = createDataframe()
if dataframe is not None:
    print(dataframe.head())