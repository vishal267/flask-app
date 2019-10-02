from flask import Flask, jsonify, abort, make_response,  render_template
import pymysql

db = pymysql.connect("172.31.17.41", "user1", "redhat", "hello")
app = Flask(__name__,template_folder='.')


def readmessage():
    cursor = db.cursor()
    sql= "SELECT name FROM authors;"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
       return render_template('flash.html', entry = row[0])

#      print (row[0])
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



app.add_url_rule('/v1/task/1', 'hello',  readmessage, methods=['GET'])
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80, use_reloader=True, debug=True)

