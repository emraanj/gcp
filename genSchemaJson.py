from xml.dom import minidom
import json

dataType = {
    "Edm.Int64": "INT64",
    "Edm.String": "STRING",
    "Edm.Int32": "STRING",
    "Edm.Boolean": "BOOL",
    "Edm.DateTimeOffset": "TIMESTAMP",
    "Edm.Decimal": "NUMERIC",
    "Edm.DateTime": "DATETIME",
    "Edm.Double": "BIGNUMERIC",
    "SFOData.property": "STRING",
    "SFOData.localstring": "STRING",
    "SFOData.navigation": "STRING",
    "Edm.Byte": "BYTES",
    "SFOData.ToDoBean": "STRING",
    "Edm.Time": "TIME",
    "SFOData.GlobalThemeConfiguration": "STRING",
    "Edm.Binary": "STRING",
    "SFOData.AccessibilityPreferences": "STRING",
    "SFOData.ThemeFingerprintsBean": "STRING",
    "SFOData.ThemeUrlsBean": "STRING",
    "SFOData.EPCustomBackgroundPortletProperty": "STRING"

}


file = minidom.parse('schema.xml')
models = file.getElementsByTagName('EntityType')
for elem in models:
    entity = []
    fileName = './tables/' + elem.getAttribute("Name") + '.json'
    f = open(fileName, "w")
    print('Entity Name is : ', elem.getAttribute("Name"))
    property = elem.getElementsByTagName("Property")
    for prop in property:
        data = {}
        name = prop.getAttribute("Name")
        type = prop.getAttribute("Type")
        required = prop.getAttribute("sap:required")
        data["description"] = name
        if required == "false":
            data["mode"] = 'REQUIRED'
        else:
            data["mode"] = 'NULLABLE'
        data["type"] = dataType[type]
        entity.append(data)

    entity_json = json.dumps(entity)
    f.write(entity_json)
    f.close()
