

import frappe

def gym_member_weekly_summary_mail():
    members = frappe.db.get_all("Gym Member",fields=["first_name", "last_name", "email"], filters={
        "status": "Active",
        "email": ["!=", ""]
    })

    for member in members:
        try:
            subject = "Weekly Summary"
            content = f"<p>Dear {member.last_name}</p><p>Your weekply report is here"
            frappe.sendmail(recipients=member.email, message=content, subject=subject)
        except Exception as e:
            frappe.log_error(e)