from flask import render_template, request
from py.models.asset import Asset
from app import app, db

@app.route('/')
def index():
    assets = db.session.query(Asset).all()

    return render_template('index.html', assets=assets)

@app.route('/create_asset', methods=['POST', 'GET'])
def create_asset():
    if request.method == 'POST':
        if "create_asset" in request.form:
            asset = Asset(request.form["title"], request.form["description"])
            db.session.add(asset)
            db.session.commit()

    return render_template('create_asset.html')

@app.route('/asset/<int:id>')
def asset(id):
    asset = db.session.query(Asset).get(id)
    return render_template("asset_browser.html", asset=asset)