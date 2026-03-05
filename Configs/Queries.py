from Configs.DatabaseConnection import *

def retrieve_names():
    names = []
    try:
        with engine.connect() as conn:
            # use engine to execute a  sql query
            result = conn.execute(text('Select * from places'))
            # iterate through returned results from query
            for i in result:
                # pull the name of the place from the results
                # and adds it to the empty list
                names.append(i[1])
    except Exception as e:
        print(f"There was an issue with executing the following command:"
              f"{e}")
    return names