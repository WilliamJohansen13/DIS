import pandas as pd
from app import app, db
from app.models import ClothingItem

# Læs CSV
df = pd.read_csv("Clothing_Items_Final.csv")  # eller "Data/Clothing_Items_Final.csv" hvis den ligger i en undermappe

# Tilføj til databasen i Flask-app kontekst
with app.app_context():
    for _, row in df.iterrows():
        item = ClothingItem(
            name=row.get("name", "Unknown"),
            category=row.get("category", "Other"),
            price=float(row.get("price", 0.0))
        )
        db.session.add(item)

    db.session.commit()
    print("✅ Data importeret!")
