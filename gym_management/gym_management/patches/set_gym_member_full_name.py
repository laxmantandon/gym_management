import frappe

def execute():
    members = frappe.get_all("Gym Member")

    if len(members) > 0:
        for member in members:
            frappe.db.set_value("Gym Member", member, {"full_name": f"{member.first_name} {member.last_name}"})