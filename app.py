import flask as fk
import MySQLdb
import JSONEncoder


class SpecializedJSONEncoder(JSONEncoder):
    
    app = fk.Flask(__name__)
    app.json_encoder = SpecializedJSONEncoder
    app.debug = True

    @app.route("/")
    def home():
       return "Hello world"
    @app.route("/temp")
    def temp():
        db = MySQLdb.connect("192.168.21.57", "bootcamp", "","bootcamp")
        cur = db.cursor()
        query = "SELECT * from emplyees where emp_no="+temp+
        cur.execute(query, param)
        data = cur.fetchall()

       return jsonify(data=cur.fetchall())

if __name__ == "__main__":
    app.run()
