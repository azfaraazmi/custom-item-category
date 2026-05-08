# ERPNext Item Form Fixtures

## Files

```
fixtures/
  Item Form.json        ← New child doctype (used inside Item)
  Custom Field.json     ← 2 custom fields added to Item doctype
hooks.py                ← Snippet to add to your app's hooks.py
```

## Setup Steps

### 1. Place fixtures in your custom app
```
your_app/
  fixtures/
    Item Form.json
    Custom Field.json
```

### 2. Register fixtures in hooks.py
Merge the contents of `hooks.py` into your app's `your_app/hooks.py`.

### 3. Import fixtures
```bash
bench --site your-site.com import-fixtures --app your_app
```

### 4. Verify
- Doctype List → search "Item Form" → should appear with Is Child Table = Yes
- Open any Item → scroll to "Item Forms" section → child table with Form Name + Description rows

### 5. Re-export after UI changes
```bash
bench --site your-site.com export-fixtures --app your_app
```

## Field Reference

### Item Form (child doctype)
| Field       | Type        | Notes               |
|-------------|-------------|---------------------|
| form_name   | Data        | Mandatory, in list  |
| description | Text Editor | Optional            |

### Custom fields on Item
| Field              | Type         | Inserted after |
|--------------------|--------------|----------------|
| item_forms_section | Section Break| description    |
| item_forms         | Table        | section break  |
