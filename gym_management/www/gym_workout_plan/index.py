from dataclasses import fields
import frappe

def get_context(context):
    context.plans = frappe.get_list("Gym Workout Plan", fields=["name"])