from flask import Flask, jsonify, render_template
from database.models import Product
from database.database import get_db

app = Flask(
    __name__)
#     static_folder=os.path.join(os.path.dirname(__file__), "../static"),
#     template_folder=os.path.join(os.path.dirname(__file__), "templates")
# )

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# @app.route("/products", methods=["GET"])
# def get_products():
#     with open("data/data.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     return jsonify(data)

@app.route("/products", methods=["GET"])
def show_data_from_dtb():
    db = next(get_db())
    products = db.query(Product).all()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)