from errormail import errorMail
from datetime import datetime
import logging
import fdb

def queryFb(fetchType, query, envConfig):

    logging.basicConfig(filename= envConfig['LOGFILEPATH'], 
                    encoding='utf-8', level=logging.INFO)
    try:
        connection = fdb.connect(
            host = envConfig['FBHOST'],
            database = envConfig['FBDATA'],
            user = envConfig['FBUSER'],
            password = envConfig['FBPASS'],
            charset = 'utf-8'
        )
        cursor = connection.cursor()

        cursor.execute(query)

        if fetchType == "one":
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()

        connection.close()
        return (result)

    except Exception as err:
        logging.error(" " + datetime.now().strftime('%Y.%m.%d %H:%M:%S') +
                      " Error while connecting to Firebird-SQL" + f" {query}"  + f" {err}")
        errorMail(err, envConfig)
        exit(1)
