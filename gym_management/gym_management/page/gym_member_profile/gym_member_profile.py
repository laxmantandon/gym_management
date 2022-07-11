import frappe


@frappe.whitelist()

def get_data(member):

    member_info = frappe.get_doc("Gym Member", member)
    transactions = frappe.db.get_list("Gym GL Entries", fields=["*"], filters={ "ledger_name": member}, order_by="document_date asc")
    membership_info = frappe.db.get_list("Gym Membership", fields=["*"], filters={"member": member}, order_by="posting_date asc", limit=1)

    return {"member": member_info, "transactions": transactions, "membership": membership_info}
