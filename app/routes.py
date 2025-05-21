from flask import render_template, request, redirect, url_for, flash
from app import app
from app.models import (
    get_all_clothing_items,
    get_filtered_clothing_items,
    get_cart_items,
    add_to_cart,
    get_cart_total_price,
)

# Midlertidig kunde-id (indtil login-system)
CURRENT_CUSTOMER_ID = 1

@app.route('/')
def home():
    return redirect(url_for('browse'))

@app.route('/browse')
def browse():
    size = request.args.get('size')
    color = request.args.get('color')
    sort_by = request.args.get('sort_by')
    sort_direction = request.args.get('sort_direction','asc')
    items = get_filtered_clothing_items(size=size, color=color, sort_by = sort_by, sort_direction = sort_direction)
    return render_template('browse.html', items=items, selected_size=size, selected_color=color, selected_sort_by = sort_by, selected_sort_direction = sort_direction)

@app.route('/add-to-cart/<int:item_id>')
def add_to_cart_route(item_id):
    add_to_cart(CURRENT_CUSTOMER_ID, item_id)
    flash("Item added to cart.")
    return redirect(url_for('browse'))

@app.route('/cart')
def cart():
    items = get_cart_items(CURRENT_CUSTOMER_ID)
    total = get_cart_total_price(CURRENT_CUSTOMER_ID)
    return render_template('cart.html', items=items, total=total)
