import frappe

def execute():
    members = frappe.get_all("Gym Member", fields=["name", "first_name","last_name", "full_name"])

    for member in members:
        frappe.db.set_value("Gym Member", member.name, {"full_name": f"{member.first_name} {member.last_name}"})
