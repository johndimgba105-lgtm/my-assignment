# List of 8 buildings as tuples: (building_name, type, year_built)
street_buildings = [
    ("Lagos Mall", "Shopping", 2015),
    ("Oba House", "Residential", 1985),
    ("Central Clinic", "Hospital", 2005),
    ("Tunde School", "Education", 1992),
    ("Sunrise Apartments", "Residential", 2010),
    ("Food Market", "Shopping", 2003),
    ("Police Station", "Government", 1978),
    ("New Church", "Religious", 2020)
]

# Find oldest building
oldest = min(street_buildings, key=lambda b: b[2])

# All unique building types as a set
unique_types = set(b[1] for b in street_buildings)

# Buildings built after 2000
after_2000 = [b for b in street_buildings if b[2] > 2000]

# Average age (assuming current year 2026)
current_year = 2026
average_age = sum(current_year - b[2] for b in street_buildings) / len(street_buildings)

print("=== Exercise 3: Your Street as a Data Structure ===")
print(f"Oldest building: {oldest[0]} ({oldest[1]}, built {oldest[2]})")
print(f"Unique building types: {unique_types}")
print(f"Buildings after 2000: {len(after_2000)}")
for b in after_2000:
    print(f"  - {b[0]} ({b[1]}, {b[2]})")
print(f"Average age: {average_age:.1f} years")
print()