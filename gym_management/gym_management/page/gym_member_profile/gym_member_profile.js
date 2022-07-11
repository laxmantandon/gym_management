frappe.pages['gym-member-profile'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Customer Profile',
		single_column: true
	});

	let gym_member = page.add_field(
		{
			label: "Gym Member",
			fieldname: "member",
			fieldtype: "Link",
			options: "Gym Member",
			change: () => {
				frappe.call('gym_management.gym_management.page.gym_member_profile.gym_member_profile.get_data', {
					member: gym_member.get_value()
				}).then(r => {
					if (r) {
						console.log(r)
						var html = frappe.render_template("gym_member_profile", { data: r.message })
						$(html).appendTo(page.body)
					} else {
						// $(frappe.render_template("gym_member_profile")).appendTo(page.body.addClass("no-border"));
					}
				})

				
			}
		}
	)
		
}	
