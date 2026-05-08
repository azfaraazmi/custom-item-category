# hooks.py
# Add this to your custom app's hooks.py

fixtures = [
    # Export the full Item Form child doctype definition
    "Item Form",

    # Export only the custom fields added to the Item doctype
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "in", ["Item"]],
            ["fieldname", "in", [
                "item_forms_section",
                "item_forms"
            ]]
        ]
    }
]
