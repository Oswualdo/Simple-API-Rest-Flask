from flask import Flask
from flask import jsonify
from flask import request
from dataset.data import products

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify("This is an example of a simple API Rest")

# GET all products


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

# GET an specific product


@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = [product for product in products if product["id"] == id]
    if product:
        return product
    else:
        return jsonify({"message": "Data not found"})

# Insert a new product


@app.route("/products", methods=["POST"])
def insert_product():
    new_product = {
        "id": request.json["id"],
        "name": request.json["name"],
        "description": request.json["description"]
    }
    products.append(new_product)
    return jsonify(products)

# Update a product


@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = [product for product in products if product["id"] == id]
    if product:
        product[0]["name"] = request.json["name"]
        product[0]["description"] = request.json["description"]
        return jsonify({"message": "The product was updated"})
    else:
        return jsonify({"message": "Not was possible updated the product"})

# Delete a product


@app.route("/products/<int:id>", methods=["DELETE"])
def delete(id):
    product = [product for product in products if product["id"] == id]
    if product:
        products.remove(product[0])
        return jsonify({"message": "The product was deleted"})
    else:
        return jsonify({"message": "Product not found"})


if __name__ == "__main__":
    app.run(debug=True)
