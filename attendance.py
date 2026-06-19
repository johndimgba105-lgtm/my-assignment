# List of 15 contact names with 5 deliberate duplicates
contacts = [
    "Williams",
    "williams ",
    "Amina",
    "Amina  ",
    "John",
    "john",
    "Fatima",
    "fatima ",
    "Emeka",
    "Tega",
    "tega ",
    "Yusuf",
    "Kemi",
    "Ngozi",
    "Samuel"
]

# Clean whitespace and normalize case
cleaned = []
for contact in contacts:
    cleaned_name = contact.strip().lower()
    cleaned.append(cleaned_name)

# Detect duplicates using sets
unique_contacts = set()
duplicates = []
for contact in cleaned:
    if contact in unique_contacts:
        duplicates.append(contact)
    else:
        unique_contacts.add(contact)

# Final cleaned list (no duplicates)
final_contacts = sorted(unique_contacts)

print("=== Exercise 4: Phone Contact Deduplicator ===")
print(f"Original contacts: {len(contacts)}")
print(f"Duplicates found: {len(duplicates)}")
print(f"Duplicate report:")
for dup in set(duplicates):
    count = cleaned.count(dup)
    print(f"  - '{dup}' appears {count} times")
print(f"Cleaned_contact list ({len(final_contacts)} contacts):")
for contact in final_contacts:
    print(f"  - {contact}")
print()