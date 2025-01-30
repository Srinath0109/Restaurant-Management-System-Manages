from flask import Blueprint, jsonify, request
from models import db, MenuItem, Order, Bill

restaurant_routes = Blueprint("restaurant_routes", __name__)

# Add a menu item
@restaurant_routes.route("/menu", methods=["POST"])
def add_menu_item():
    data = request.json
    new_item = MenuItem(name=data["name"], price=data["price"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Menu item added successfully"}), 201

# Get all menu items
@restaurant_routes.route("/menu", methods=["GET"])
def get_menu():
    menu = MenuItem.query.all()
    return jsonify([{"id": item.id, "name": item.name, "price": item.price} for item in menu])

# Place an order
@restaurant_routes.route("/orders", methods=["POST"])
def place_order():
    data = request.json
    new_order = Order(customer_name=data["customer_name"], menu_item_id=data["menu_item_id"], quantity=data["quantity"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully"}), 201

# Generate a bill
@restaurant_routes.route("/bills/<int:order_id>", methods=["GET"])
def generate_bill(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    menu_item = MenuItem.query.get(order.menu_item_id)
    total_price = menu_item.price * order.quantity
    bill = Bill(order_id=order.id, total_price=total_price)
    
    db.session.add(bill)
    db.session.commit()
    
    return jsonify({"order_id": order.id, "total_price": total_price})
