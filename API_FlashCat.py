import flask
import pyodbc
from flask_cors import CORS
from datetime import datetime
# from json import JSONEncoder
# class CustomJSONEncoder(JSONEncoder):
#     def __init__(self, *args, **kwargs):
#         kwargs['ensure_ascii'] = False
#         super(CustomJSONEncoder, self).__init__(*args, **kwargs)

app = flask.Flask(__name__)
#app.json_encoder = CustomJSONEncoder
CORS(app)
str_connect = "DRIVER={SQL Server};SERVER=LNGLA\SQLEXPRESS01;DATABASE=DBFlashcard;Trusted_Connection=yes;CHARSET=UTF8"
connect = pyodbc.connect(str_connect)

#
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
        cursor.execute("Select * from Desk where ID_Deck = ?", id_desk)
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
        id_desk = flask.request.json.get("ID_Deck")
        name_desk = flask.request.json.get("name_deck")
        status = flask.request.json.get("status_deck")
        created = flask.request.json.get("create_day")
        number_flashcard = flask.request.json.get("number_flashcard")
        ID_Account = flask.request.json.get("ID_Account")

        created = datetime.strptime(created, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (id_desk,name_desk, status, created, number_flashcard, ID_Account)

        sql_insert = "INSERT INTO Desk (ID_Deck, name_deck, status_deck, create_day, number_flashcard, ID_Account) VALUES"
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
        name_desk = flask.request.json.get("name_deck")
        status = flask.request.json.get("status_deck")
        created = flask.request.json.get("create_day")
        number_flashcard = flask.request.json.get("number_flashcard")
        ID_Account = flask.request.json.get("ID_Account")
        created = datetime.strptime(created, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (name_desk, status, created,number_flashcard,ID_Account,id_desk)

        sql_update = "Update Desk set name_deck = ?, status_deck = ?, create_day = ? ,number_flashcard = ?, ID_Account = ? where ID_Deck = ?"
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
        sql_delete = "Delete from Desk where ID_Deck = ?"
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
        cursor.execute("Select * from Flashcard where ID_Flashcard = ?", id_fc)
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
        cursor.execute("Select * from Flashcard where ID_Deck = ?", id_desk)
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
        id_fc = flask.request.json.get("ID_Flashcard")
        term = flask.request.json.get("term")
        definition = flask.request.json.get("definition")
        id_desk = flask.request.json.get("ID_Deck")
        example = flask.request.json.get("example")
        status = flask.request.json.get("status")
        sound = flask.request.json.get("sound")
        update_date = flask.request.json.get("update_day")

        update_date = datetime.strptime(update_date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (id_fc,term,definition,example,sound,status,update_date,id_desk)

        sql_insert = "INSERT INTO Flashcard (ID_Flashcard, term, definition, example, sound, status, update_day, ID_Deck) VALUES(?,?,?,?,?,?,?,?)"
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
        term = flask.request.json.get("term")
        definition = flask.request.json.get("definition")
        id_desk = flask.request.json.get("ID_Deck")
        example = flask.request.json.get("example")
        status = flask.request.json.get("status")
        sound = flask.request.json.get("sound")
        update_date = flask.request.json.get("update_day")

        update_date = datetime.strptime(update_date, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d %H:%M:%S')

        data = (term,definition,example,status,sound,update_date,id_desk,id_fc)

        sql_update = "Update Flashcard set term = ?, definition = ?, example = ?, status = ?, sound = ?, update_day = ?, ID_Deck = ? where ID_Flashcard = ?"
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
        sql_delete = "Delete from Flashcard where ID_Flashcard = ?"
        cursor = connect.cursor()
        cursor.execute(sql_delete, id_fc)
        connect.commit()
        resp = flask.jsonify("Delete success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@app.route("/fc/getAllWord",methods=['GET'])
def getAllWord():
    try:
        cursor = connect.cursor()
        cursor.execute("Select * from Word")
        result = []
        keys = []
        for i in cursor.description:
            keys.append(i[0])
        for val in cursor.fetchall():
            # Chuyển đổi từng giá trị trong từ điển thành chuỗi UTF-8 trước khi thêm vào kết quả
            utf8_val = {k: v.encode('utf-8').decode('utf-8') if isinstance(v, str) else v for k, v in dict(zip(keys, val)).items()}
            result.append(utf8_val)
        resp = flask.jsonify(result)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@app.route("/fc/addWord/",methods=['POST'])
def addWord():
    try:
        id_word = flask.request.json.get("id")
        word = flask.request.json.get("word")
        minusWord = flask.request.json.get("minusWord")
        denfinitionWord = flask.request.json.get("denfinitionWord")

        data = (id_word, word, minusWord,denfinitionWord)

        sql_insert = "INSERT INTO Word (id, word, minusWord, denfinitionWord) VALUES(?,?,?,?)"
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
@app.route("/fc/deleteWord/<id_word>/",methods=['DELETE'])
def deleteWord(id_word):
    try:
        sql_delete = "Delete from Word where id = ?"
        cursor = connect.cursor()
        cursor.execute(sql_delete, id_word)
        connect.commit()
        resp = flask.jsonify("Delete success")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
if __name__ == "__main__":
    app.run()