# Copyright (c) 2022, Laxman and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	from_date = filters.get("from_date")
	to_date = filters.get("to_date")

	columns = ["Plan:Link/Membership Plan:200", "Amount"]

	data = frappe.db.sql("""
		SELECT gm.membership_plan, SUM(gm.amount)
			from `tabGym Membership` gm
		WHERE gm.posting_date between %s and %s
		GROUP BY gm.membership_plan
		ORDER BY gm.amount DESC
		LIMIT 10
	""", (from_date, to_date))

	message = "Top Performing Plans"

	charts_columns = []
	charts_values = []
	for plan in data:
		charts_columns.append(plan[0])
		charts_values.append(plan[1])

	chart = {
		"title": "Gym Mebership Plan",
		"type": "percentage",
		"data": {
			"labels": charts_columns,
			"datasets": [{
				"name": "Gym Membership Plan Analysis",
				"type": "line",
				"values": charts_values
			}]
		}

	}

	return columns, data, message, chart
