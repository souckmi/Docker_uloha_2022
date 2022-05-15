import datetime
import db_connect

def sql_prepare():
    return "INSERT INTO params (patient_id, parameter, datetime, value) VALUES (%s,%s,%s,%s)"

def extract_parameter(record):
    values = []
    lines = record.split("\n")
    for x in lines:
        parts = x.split("|")
        if parts[0] == "PID":
            patient_id = parts[3]
        if parts[0] == "OBX":
            params = parts[3]
            value = parts[5]
            d = parts[14]
            date_time = datetime.datetime(int(d[0:4]),int(d[4:6]),int(d[6:8]),int(d[8:10]),int(d[10:12]),int(d[12:14]))
            single_record = (patient_id, params, date_time, value)
            values.append(single_record)
    return values
    
        
def saveParams(records_list):
    config = db_connect.load_config()
    
    db = db_connect.conndect_to_db(config['database'])
    db_cursor = db.cursor()
    
    for record in records_list:
        parameters_values = extract_parameter(record)
        parameters_values = extract_parameter(record)
        stmt = sql_prepare()
        db_cursor = db.cursor()
        db_cursor.executemany(stmt, parameters_values)
        db.commit()



    
