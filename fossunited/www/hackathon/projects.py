import frappe


def get_context(context):
    context.hackathon = frappe.get_doc(
        "FOSS Hackathon", {"permalink": frappe.form_dict.permalink}
    )
    context.projects = frappe.get_all(
        "FOSS Hackathon Project",
        {"hackathon": context.hackathon.name},
        ["*"],
        page_length=9999,
    )
