from app import app
from flask import render_template


@app.route('/properties.html')
def properties():
    return render_template('root/property-grid.html')