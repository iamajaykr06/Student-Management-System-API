from db import get_db_connection
def create_student(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
               INSERT INTO students (name, department, course, academic_session)
               VALUES (%s, %s, %s, %s)
           """

        values = (
            data["name"],
            data["department"],
            data["course"],
            data["academic_session"]
        )

        cursor.execute(query, values)
        conn.commit()

        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_all_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT id, name, department, course, academic_session FROM students"
        cursor.execute(query)

        students = cursor.fetchall()
        return students

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_student_by_id(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT id, name, department, course, academic_session FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))

        student = cursor.fetchone()
        return student

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_student(student_id, data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            UPDATE students
            SET name = %s,
                department = %s,
                course = %s,
                academic_session = %s
            WHERE id = %s
        """

        values = (
            data["name"],
            data["department"],
            data["course"],
            data["academic_session"],
            student_id
        )

        cursor.execute(query, values)
        conn.commit()

        return cursor.rowcount  # IMPORTANT

    except Exception as e:
        print(e)
        return -1

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def delete_student(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()

        return cursor.rowcount  # IMPORTANT

    except Exception as e:
        print(e)
        return -1

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
