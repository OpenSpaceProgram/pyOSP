import sys, tty, time, os, json

from flask import Flask, request, render_template, url_for
app = Flask(__name__)

alt = 0
lat = 0
lon = 0
last_time = 0
debug = ''
    

@app.route("/")
def get_stats():
    global alt, lat, lon, last_time, debug
    return render_template('layout.html', alt=alt, lat=lat, lon=lon, last_time=last_time, debug=debug)
    
    
@app.route("/post", methods=['GET', 'POST'])
def returnPost():
    global alt, lat, lon, last_time, debug  
    debug = ''
    
    if ('Altitude' in request.form):
        alt = request.form['Altitude']
        last_time = int(time.time())
    
    if ('Latitude' in request.form):
        lat = request.form['Latitude']
        last_time = int(time.time())
    
    if ('Longitude' in request.form):
        lon = request.form['Longitude']
        last_time = int(time.time())
        
    for value in request.form:
        debug += ': ' + value
    
    return "done."
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
