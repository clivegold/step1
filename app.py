import os
import uuid
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())

BLUE = "#777799"
GREEN = "#99CC99"
YELLOW = "#F0E68C"

COLOR = BLUE

@app.route('/')
def mainmenu():

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>
    <u>Main Menu</u>
    </center>
    </body>
    <img src="static/floorplan.jpg" alt="Floorplan" style="width:200px;height:100px;">
    <p><a href="floorplan.html">Larger</a><p>
    </html>
    """.format(COLOR,my_uuid,)

@app.route('/floorplan.html')
def floorplan():

    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white"><br/>
    <u>Floor Plan</u>
    </center>
    </body>
    <img src="static/floorplan.jpg" alt="Floorplan" style="width:800px;height:600px;">
    <p><a href="/">Home</a><p>

    </html>
    """.format(COLOR,)

if __name__ == "__main__":
        app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))