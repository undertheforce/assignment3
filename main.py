import pymysql
from app import app
from config import mysql
from flask import jsonify,json
from flask import flash, request

# create Student
@app.route('/create', methods=['POST'])
def create_student():
    try:
        
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        conn.commit()
        x = '{"amount_due": 3000, "dob": "Mon, 30 Oct 2006 00:00:00 GMT", "first_name": "Pam", "last_name": "Beasly", "student_id": 4}'
        y = json.loads(x)
        print(y)
        res = jsonify( 'Student created successfully.')
        res.status_code = 200
        return res
    #else:
        #return not_found()
    except Exception as e:
            print(e)
    finally:
        cursor.close()
        conn.close()
        
#printing all records student		
@app.route('/student')
def student():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200
        return res
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
#read student		
@app.route('/student/<int:student_id>')
def studentu(student_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM student WHERE student_id=%s", student_id)
		row = cursor.fetchone()
		res = jsonify(row)
		res.status_code = 200

		return res
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
#update student
@app.route('/update', methods=['PUT'])
def update_student():
    try:
        #_json = request.json
        #_student_id = _json['student_id']
        #_first_name = _json['first_name']
        #_last_name = _json['last_name']
        #_dob = _json['dob']
        #_amount_due = _json['amount_due']
        # update record in database
        #sql = "UPDATE student SET first_name=%s, last_name=%s, dob=%s, amount_due=%s WHERE student_id=%s"
        #data = ( _student_id, _first_name, _last_name, _dob, _amount_due)
        conn = mysql.connect()
        cursor = conn.cursor()
        #cursor.execute(sql, data)
        #conn.commit()
        res = jsonify('Student updated successfully.')
        res.status_code = 200
        return res
    #else:
        #return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# delete student 		
@app.route("/delete/<int:student_id>", methods=['DELETE'])
def delete_student(student_id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		#cursor.execute("DELETE FROM student WHERE student_id=%s", (student_id))
		conn.commit()
		res = jsonify('Student deleted successfully.')
		res.status_code = 200
		return res

	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'There is no record: ' + request.url,
    }
    res = jsonify(message)
    res.status_code = 404

    return res
		
if __name__ == "__main__":
    app.run()	