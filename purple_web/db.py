import pyodbc

def connect_to_db():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-7JF3UC3K\SQLEXPRESS;DATABASE=test;Trusted_Connection=yes;')
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        return None


def insert_user(conn, form_data):
    try:
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO test7 (
                full_name, date_of_birth, email, mobile_number, gender, occupation,
                adharcard_name, adhar_number, issued_state, pancard_name, pancard_number,
                issued_by, address_type, nationality, state, district, block_number,
                ward_number, father_name, mother_name, spouse_name, sibling_name
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        """

        cursor.execute(
            insert_query,
            form_data['full_name'], form_data['date_of_birth'], form_data['email'],
            form_data['mobile_number'], form_data['gender'], form_data['occupation'],
            form_data['adharcard_name'], form_data['adhar_number'], form_data['issued_state'],
            form_data['pancard_name'], form_data['pancard_number'], form_data['issued_by'],
            form_data['address_type'], form_data['nationality'], form_data['state'],
            form_data['district'], form_data['block_number'], form_data['ward_number'],
            form_data['father_name'], form_data['mother_name'], form_data['spouse_name'],
            form_data['sibling_name']
        )
        print("data inserted successfully")
        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        conn.rollback()
    finally:
        conn.close()


def insert_user_signup(conn, username,first_name, email, pwd):
    try:
        cursor = conn.cursor()
        insert_query = "INSERT INTO test_user4 (name,first_name, email, password) VALUES (?, ?, ?,?)"
        cursor.execute(insert_query, (username,first_name, email, pwd))

        conn.commit()
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        conn.rollback()
    finally:
        conn.close()







def save_form_data(data):
    try:
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-7JF3UC3K\SQLEXPRESS;DATABASE=test;Trusted_connection=yes;')
        cursor = conn.cursor()

        sql = """
            INSERT INTO new_test2 (
                Q_1, Q_2,Q_3,Q_4
            )
            VALUES (?, ?,?,?)
            """
        params = (data['Que1'], data['Que2'],data['Que3'], data['Que4'])
        cursor.execute(sql, params)
        conn.commit()

        cursor.close()
        conn.close()

    except pyodbc.Error as ex:
        
        print("Error:", ex)
        raise  

