import flask
import pyodbc
from flask_cors import CORS
from datetime import datetime

app = flask.Flask(__name__)
CORS(app)
str_connect = "DRIVER={SQL Server};SERVER=LNGLA\SQLEXPRESS01;DATABASE=FlashCat;Trusted_Connection=yes"
connect = pyodbc.connect(str_connect)

@app.route("/fc/getallDesk",methods=['GET'])
def getAllDesk():
    try:
        cusor = connect.cursor()
        cusor.execute("Select * from Desk")
        result=[]
        keys=[]
        for i in cusor.description:
            keys.append(i[0])
        for val in cusor.fetchall():
            result.append(dict(zip(keys,val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/getbyIdDesk/<id_desk>/",methods=['GET'])
def getByIdDesk(id_desk):
    try:
        cursor = connect.cursor()
        cursor.execute("Select * from Desk where ID_Desk = ?", id_desk)
        result=[]
        keys=[]
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            result.append(dict(zip(keys,val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/addDesk",methods=['POST'])
def addDesk():
    try:
        id_desk = flask.request.json.get("ID_Desk")
        name_desk = flask.request.json.get("Name_deck")
        status = flask.request.json.get("Status")
        created = flask.request.json.get("Created")

        created = datetime.strptime(created, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (id_desk,name_desk, status, created)

        sql_insert = "Insert into Desk(ID_Desk,Name_deck, Status, Created) values(?,?,?,?)"
        cursor = connect.cursor()
        cursor.execute(sql_insert, data)
        connect.commit()
        resp = flask.jsonify("Insert success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = flask.jsonify("An error occurred")
        resp.status_code = 500
        return resp
@app.route("/fc/updateDesk/<id_desk>/",methods=['PUT'])
def updateDesk(id_desk):
    try:
        name_desk = flask.request.json.get("Name_deck")
        status = flask.request.json.get("Status")
        created = flask.request.json.get("Created")

        created = datetime.strptime(created, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (name_desk, status, created,id_desk)

        sql_update = "Update Desk set Name_deck = ?, Status = ?, Created = ? where ID_Desk = ?"
        cursor = connect.cursor()
        cursor.execute(sql_update, data)
        connect.commit()
        resp = flask.jsonify("Update success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = flask.jsonify("An error occurred")
        resp.status_code = 500
        return resp
@app.route("/fc/deleteDesk/<id_desk>/",methods=['DELETE'])
def deleteDesk(id_desk):
    try:
        sql_delete = "Delete from Desk where ID_Desk = ?"
        cursor = connect.cursor()
        cursor.execute(sql_delete, id_desk)
        connect.commit()
        resp = flask.jsonify("Delete success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/getallFlashcard",methods=['GET'])
def getAllFlashcard():
    try:
        cusor = connect.cursor()
        cusor.execute("Select * from Flashcard")
        result=[]
        keys=[]
        for i in cusor.description:
            keys.append(i[0])
        for val in cusor.fetchall():
            result.append(dict(zip(keys,val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/getbyIdFlashcard/<id_fc>/",methods=['GET'])
def getByIdFlashcard(id_fc):
    try:
        cursor = connect.cursor()
        cursor.execute("Select * from Flashcard where ID_FC = ?", id_fc)
        result=[]
        keys=[]
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            result.append(dict(zip(keys,val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/getAllFlashcardByIdDesk/<id_desk>/",methods=['GET'])
def getAllFlashcardByIdDesk(id_desk):
    try:
        cursor = connect.cursor()
        cursor.execute("Select * from Flashcard where ID_Desk = ?", id_desk)
        result=[]
        keys=[]
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            result.append(dict(zip(keys,val)))
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/addFlashcard",methods=['POST'])
def addFlashcard():
    try:
        id_fc = flask.request.json.get("ID_FC")
        term = flask.request.json.get("Term")
        definition = flask.request.json.get("Definition")
        id_desk = flask.request.json.get("ID_Desk")
        example = flask.request.json.get("Example")
        status = flask.request.json.get("Status")
        sound = flask.request.json.get("Sound")
        update_date = flask.request.json.get("Update_date")

        update_date = datetime.strptime(update_date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (id_fc,term,definition,example,status,sound,update_date,id_desk)

        sql_insert = "INSERT INTO Flashcard (ID_FC, Term, Definition, Example, Status, Sound, Update_date, ID_Desk) VALUES(?,?,?,?,?,?,?,?)"
        cursor = connect.cursor()
        cursor.execute(sql_insert, data)
        connect.commit()
        resp = flask.jsonify("Insert success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = flask.jsonify("An error occurred")
        resp.status_code = 500
        return resp
@app.route("/fc/updateFlashcard/<id_fc>/",methods=['PUT'])
def updateFlashcard(id_fc):
    try:
        term = flask.request.json.get("Term")
        definition = flask.request.json.get("Definition")
        id_desk = flask.request.json.get("ID_Desk")
        example = flask.request.json.get("Example")
        status = flask.request.json.get("Status")
        sound = flask.request.json.get("Sound")
        update_date = flask.request.json.get("Update_date")

        update_date = datetime.strptime(update_date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (term,definition,example,status,sound,update_date,id_desk,id_fc)

        sql_update = "Update Flashcard set Term = ?, Definition = ?, Example = ?, Status = ?, Sound = ?, Update_date = ?, ID_Desk = ? where ID_FC = ?"
        cursor = connect.cursor()
        cursor.execute(sql_update, data)
        connect.commit()
        resp = flask.jsonify("Update success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        resp = flask.jsonify("An error occurred")
        resp.status_code = 500
        return resp
@app.route("/fc/deleteFlashcard/<id_fc>/",methods=['DELETE'])
def deleteFlashcard(id_fc):
    try:
        sql_delete = "Delete from Flashcard where ID_FC = ?"
        cursor = connect.cursor()
        cursor.execute(sql_delete, id_fc)
        connect.commit()
        resp = flask.jsonify("Delete success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
if __name__ == "__main__":
    app.run()