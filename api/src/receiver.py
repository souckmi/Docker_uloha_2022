import db_connect

def sql_prepare(patient_id):
    return "SELECT record FROM patient_record WHERE patient = " + patient_id

def extract_parameter(result, parameter):
    values = []
    for record in result:
        lines = record[0].split("\n")
        for x in lines:
            parts = x.split("|")
            if parts[0] == "OBX":
                params = parts[3]
                splitParams = params.split("^")
                if splitParams[0] == parameter:
                    d = parts[14]

                    dformatted = d[0:4] + "/" + d[4:6] + "/" + d[6:8] + " " + d[8:10] + ":" + d[10:12] + ":" + d[12:14]
                    values.append({"value": float(parts[5]), "time": dformatted})
    return values
    
        
def getParameter(patient_id, parameter_id):
    config = db_connect.load_config()
    
    db = db_connect.conndect_to_db(config['database'])
    stmt = sql_prepare(patient_id)
    
    db_cursor = db.cursor()
    db_cursor.execute(stmt)

    result = db_cursor.fetchall()
    
    parameter_in_time = extract_parameter(result, parameter_id)
    
    # some to jason stuff
    return parameter_in_time


    
