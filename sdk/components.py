# https://betterprogramming.pub/how-to-remove-null-none-values-from-a-dictionary-in-python-1bedf1aab5e4
def cleanNullTerms(d):
    clean = {}
    for k, v in d.items():
        if isinstance(v, dict):
            nested = cleanNullTerms(v)
            if len(nested.keys()) > 0:
                clean[k] = nested
        elif v is not None:
            clean[k] = v
    return clean


def Span(content, class_name=None):
    return {
        "_type": "Span",
        "props": cleanNullTerms({
            "className": class_name,
            "content": content,
        })
    }


def Container(children, class_name=None):
    return {
        "_type": "Container",
        "props": cleanNullTerms({
            "className": class_name,
            "children": children
        })
    }


def Row(children, class_name=None):
    return {
        "_type": "Row",
        "props": cleanNullTerms({
            "className": class_name,
            "children": children
        })
    }


def Div(children, class_name=None, style=None):
    return {
        "_type": "Div",
        "props": cleanNullTerms({
            "className": class_name,
            "children": children,
            "style": style,
        })
    }


def Col(children, class_name=None):
    return {
        "_type": "Col",
        "props": cleanNullTerms({
            "className": class_name,
            "children": children
        })
    }


def Icon(name, class_name=None, size=None):
    return {
        "_type": "Icon",
        "props": cleanNullTerms({
            "className": class_name,
            "name": name,
            "size": size
        })
    }


def Datatable(data, columns, class_name=None, busy_when=None, show_export=None, pagination=None):
    return {
        "_type": "Datatable",
        "props": cleanNullTerms({
            "busyWhen": busy_when,
            "className": class_name,
            "columns": columns,
            "data": data,
            "showExport": show_export,
            "pagination": pagination
        })
    }


def Badge(color, children, class_name=None):
    return {
        "_type": "Badge",
        "props": cleanNullTerms({
            "children": children,
            "className": class_name,
            "color": color,
        })
    }


def Column(id, value=None, title=None, format=None, right=None, width=None, min_width=None, grow=None, cell=None):
    return cleanNullTerms({
        "cell": cell,
        "format": format,
        "grow": grow,
        "id": id,
        "minWidth": min_width,
        "right": right,
        "title": title,
        "value": value,
        "width": width,
    })


def Form(name, schema, children, class_name=None):
    return {
        "_type": "Form",
        "props": cleanNullTerms({
            "children": children,
            "className": class_name,
            "name": name,
            "schema": schema,
        })
    }


def Select(label, name, options, min_width=None, class_name=None):
    return {
        "_type": "Select",
        "props": cleanNullTerms({
            "className": class_name,
            "label": label,
            "name": name,
            "options": options,
            "minWidth": min_width,
        })
    }


def Button(label, is_submit=None, class_name=None, busyWhen=None):
    return {
        "_type": "Button",
        "props": cleanNullTerms({
            "className": class_name,
            "label": label,
            "isSubmit": is_submit,
            "busyWhen": busyWhen,
        })
    }


def collection(collectionName):
    return collectionName


def documents(collectionName):
    return f'$["{collection(collectionName)}"].*'


def is_busy(collection):
    return f'$..busy[?(@.id=="{collection}")]'


def format_currency(rpc, symbol):
    return {
        "method": "formatCurrency",
        "params": [rpc, symbol]
    }


def selected_currency(event):
    if (event is None):
        return None

    if ("state" not in event.keys()):
        return None

    if ("client" not in event["state"].keys()):
        return None

    if ("selectedCurrency" not in event["state"]["client"].keys()):
        return None

    return event["state"]["client"]["selectedCurrency"]


def form_value(event, form_name, property_name):
    if (event is None):
        return None

    if ("state" not in event.keys()):
        return None

    if ("forms" not in event["state"].keys()):
        return None

    if (form_name not in event["state"]["forms"].keys()):
        return None

    if (property_name not in event["state"]["forms"][form_name].keys()):
        return None

    return event["state"]["forms"][form_name][property_name]


def format_template(template, values):
    return {
        "method": "formatTemplate",
        "params": [template, values]
    }


def switch_case(on, cases):
    return {
        "method": "switchCase",
        "params": [on, cases]
    }


def commify(value):
    return {
        "method": "commify",
        "params": [value]
    }
