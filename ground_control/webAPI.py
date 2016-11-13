import sys, tty, time, os, json

from flask import Flask, request, render_template, url_for
app = Flask(__name__)

alt = 0
lat = 0
lon = 0
last_time = 0
    

@app.route("/")
def get_stats():
    global alt, lat, lon, last_time
    return render_template('layout.html', alt=alt, lat=lat, lon=lon, last_time=last_time)
    
    
@app.route("/post", methods=['GET', 'POST'])
def returnPost():
    global alt, lat, lon, last_time
    
    if (request.form['alt']):
        alt = request.form['alt']
        last_time = int(time.time())
    
    if (request.form['lat']):
        lat = request.form['lat']
        last_time = int(time.time())
    
    if (request.form['lon']):
        lon = request.form['lon']
        last_time = int(time.time())
    
    return "done."
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
