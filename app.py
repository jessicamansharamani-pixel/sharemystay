from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sharemystay-secret"

# Dummy data to simulate listings
listings = [
    {
        "id": 1,
        "title": "Cozy 2BHK in Bandra",
        "city": "Mumbai",
        "price": 1800,
        "dates": "Jul 10 – Jul 25",
        "owner": "Priya S.",
        "verified": True,
        "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=600&q=80",
    },
    {
        "id": 2,
        "title": "Bright Studio near Koramangala",
        "city": "Bangalore",
        "price": 1200,
        "dates": "Aug 1 – Aug 20",
        "owner": "Rohan M.",
        "verified": True,
        "image": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80",
    },
    {
        "id": 3,
        "title": "Spacious Guest Room, Hauz Khas",
        "city": "Delhi",
        "price": 900,
        "dates": "Jul 20 – Aug 5",
        "owner": "Ananya K.",
        "verified": False,
        "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=600&q=80",
    },
    {
        "id": 4,
        "title": "Sea-facing 1BHK, Juhu",
        "city": "Mumbai",
        "price": 2500,
        "dates": "Sep 1 – Sep 30",
        "owner": "Vikram D.",
        "verified": True,
        "image": "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=600&q=80",
    },
    {
        "id": 5,
        "title": "Quiet Room in Gated Community",
        "city": "Hyderabad",
        "price": 750,
        "dates": "Aug 15 – Sep 10",
        "owner": "Sneha P.",
        "verified": True,
        "image": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=80",
    },
    {
        "id": 6,
        "title": "Modern Flat near IT Park",
        "city": "Pune",
        "price": 1100,
        "dates": "Jul 5 – Jul 28",
        "owner": "Arjun N.",
        "verified": False,
        "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&q=80",
    },
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stays")
def stays():
    city_filter = request.args.get("city", "").strip()
    filtered = [l for l in listings if city_filter.lower() in l["city"].lower()] if city_filter else listings
    cities = sorted(set(l["city"] for l in listings))
    return render_template("stays.html", listings=filtered, cities=cities, city_filter=city_filter)

@app.route("/list-home", methods=["GET", "POST"])
def list_home():
    if request.method == "POST":
        flash("Your listing has been submitted for review. We'll verify and publish it shortly!", "success")
        return redirect(url_for("list_home"))
    return render_template("list_home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
