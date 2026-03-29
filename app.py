from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sharemystay-secret"

# Database config — creates a file called database.db in your project folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------- DATABASE MODEL ----------
class Listing(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    phone       = db.Column(db.String(20), nullable=False)
    title       = db.Column(db.String(200), nullable=False)
    city        = db.Column(db.String(100), nullable=False)
    type        = db.Column(db.String(100), nullable=False)
    date_from   = db.Column(db.String(20), nullable=False)
    date_to     = db.Column(db.String(20), nullable=False)
    price       = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    verified    = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables + add sample data if empty
with app.app_context():
    db.create_all()
    if Listing.query.count() == 0:
        samples = [
            Listing(name="Priya S.", phone="9999999991", title="Cozy 2BHK in Bandra", city="Mumbai", type="Full apartment / flat", date_from="2025-07-10", date_to="2025-07-25", price=1800, description="Beautiful 2BHK in the heart of Bandra with all amenities.", verified=True),
            Listing(name="Rohan M.", phone="9999999992", title="Bright Studio near Koramangala", city="Bangalore", type="Full apartment / flat", date_from="2025-08-01", date_to="2025-08-20", price=1200, description="Modern studio apartment, 5 min walk from Koramangala.", verified=True),
            Listing(name="Ananya K.", phone="9999999993", title="Spacious Guest Room, Hauz Khas", city="Delhi", type="Guest room", date_from="2025-07-20", date_to="2025-08-05", price=900, description="Private guest room in a quiet colony near Hauz Khas Village.", verified=False),
            Listing(name="Vikram D.", phone="9999999994", title="Sea-facing 1BHK, Juhu", city="Mumbai", type="Full apartment / flat", date_from="2025-09-01", date_to="2025-09-30", price=2500, description="Stunning sea view from the balcony. Perfect for a relaxing stay.", verified=True),
            Listing(name="Sneha P.", phone="9999999995", title="Quiet Room in Gated Community", city="Hyderabad", type="Guest room", date_from="2025-08-15", date_to="2025-09-10", price=750, description="Safe gated community, close to HITEC City.", verified=True),
            Listing(name="Arjun N.", phone="9999999996", title="Modern Flat near IT Park", city="Pune", type="Full apartment / flat", date_from="2025-07-05", date_to="2025-07-28", price=1100, description="Fully furnished flat, 10 min from Hinjewadi IT Park.", verified=False),
        ]
        db.session.add_all(samples)
        db.session.commit()

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stays")
def stays():
    city_filter = request.args.get("city", "").strip()
    if city_filter:
        listings = Listing.query.filter(Listing.city.ilike(f"%{city_filter}%")).order_by(Listing.created_at.desc()).all()
    else:
        listings = Listing.query.order_by(Listing.created_at.desc()).all()
    cities = sorted(set(l.city for l in Listing.query.all()))
    return render_template("stays.html", listings=listings, cities=cities, city_filter=city_filter)

@app.route("/list-home", methods=["GET", "POST"])
def list_home():
    if request.method == "POST":
        new_listing = Listing(
            name        = request.form["name"],
            phone       = request.form["phone"],
            title       = request.form["title"],
            city        = request.form["city"],
            type        = request.form["type"],
            date_from   = request.form["date_from"],
            date_to     = request.form["date_to"],
            price       = int(request.form["price"]),
            description = request.form.get("description", ""),
            verified    = False,
        )
        db.session.add(new_listing)
        db.session.commit()
        flash("Your listing has been submitted for review. We'll verify and publish it shortly!", "success")
        return redirect(url_for("list_home"))
    return render_template("list_home.html")

@app.route("/about")
def about():
    total = Listing.query.count()
    return render_template("about.html", total_listings=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
