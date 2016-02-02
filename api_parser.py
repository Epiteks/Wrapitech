import time

def log_file(msg, code=0):
    date = time.strftime("[%d/%m/%Y %H:%m:%S]");
    with open("api.log", "a+") as f:
        f.write("%s :[%s]%s\n" %(date, code, msg))
        f.close()

def clean_json(json_raw):
    return json_raw

def epur(json_raw):
    return json_raw.replace("\t", "").replace("\n", "")

def get_classes_by_calendar_type(planning, type):
    output = []
    for item in planning:
        if hasattr(item, "keys"):
            if "calendar_type" in item.keys():
                if item['calendar_type'] == type:
                    output.append(item)
    return output

def get_classes_by_status(planning, status):
    filters = status.split("|")
    if "all" in filters:
        return planning
    output = planning
    for _filter in filters:
        if _filter not in ["registered", "free"]:
            return {"error":{"message":"Invalid filter : %s" % _filter, "code":400}}
        if _filter == "registered":
            output = [item for item in output if "event_registered" in item.keys() \
            and item['event_registered'] is not None \
            and item['event_registered'] == "registered"]
        elif _filter == "free":
            output = [item for item in output if "room" in item.keys() \
            and item["room"] is not None and "seats" in item["room"].keys() \
            and "total_students_registered" in item.keys() \
            and item["room"]["seats"] > item["total_students_registered"]]
    return output

def filter_projects(planning, filters):
    filters = filters.split("|")
    output = []
    for _filter in filters:
        for project in planning:
            if _filter == "registered":
                if project["registered"] != 0:
                    output.append(project)
            elif _filter == "all":
                output.append(project)
    return output

def get_parameters(method, request):
    if method == 'POST':
        return request.form
    elif method == 'GET':
        if (len(request.args) == 0):
            return request.form
        else:
            return request.args
    else:
        if (len(request.args) == 0):
            return request.form
        else:
            return request.args

def get_marks(html_raw):
    pos = html_raw.find('notes: [')
    pos2 = html_raw.find('});', pos)
    output = html_raw[pos + 7:pos2]
    return output

def get_modules(html_raw):
    haystack = "window.user = $.extend(window.user || {}, {"
    pos = html_raw.find(haystack)
    pos2 = html_raw.find("notes: [")
    return html_raw[pos+len(haystack)+11:pos2 -4]
