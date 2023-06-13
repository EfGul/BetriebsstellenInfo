from fastapi import FastAPI
from data.data import df

app = FastAPI()

# Endpoint which supplies data to specific operating station
@app.get("/betriebsstelle/{rl100_code}")
def get_info(rl100_code):
    '''
    Function that returns the corresponding operating station information from a given RL100-Code.

        Parameters: rl100_code
            rl100_code (string): RL100-Code identifier of the operating station.

        Returns
            Response (dict): Name, short name and type of the item as JSON dict.
    '''

    # Convert to uppercase because all RL100-Codes in dataframe are uppercase
    rl100_code_uppercase = rl100_code.upper()

    # Check if RL100-Code exists in dataframe
    if rl100_code_uppercase in df["RL100-Code"].values:
        # Define the column names needed in the response
        RELEVANT_COLUMNS = ["RL100-Langname", "RL100-Kurzname", "Typ Lang"]

        # Filter data frame by RL100-Code and relevant 3 columns. Assign to variables name, short_name, long_type
        name, short_name, long_type = df.loc[df["RL100-Code"] == rl100_code_uppercase, RELEVANT_COLUMNS].values[0]

        # Building the JSON Response
        response = {
            "Name": name, 
            "Kurzname": short_name, 
            "Typ": long_type
        }
    else:
        response = {}

    return response
