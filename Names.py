import requests
import bs4
import json
from data import gender_list, link_list, usage_list, names_dir

for i in range(1, 100):
    url = f"https://www.behindthename.com/names/{i}"
    requested_web = requests.get(url)
    web_html = requested_web.text

    html_parser = bs4.BeautifulSoup(web_html, "html.parser")
    finds = html_parser.findAll("div", attrs={"class": "browsename"})

    for Find in finds:
        browse = str(Find).split("<span")

        class_name = browse[1]
        start_class_name2 = class_name.find("/name/")
        class_name2 = class_name[start_class_name2:]
        start_name = class_name2.find("\">")
        end_name = class_name2.find("</")
        name = class_name2[start_name+2:end_name]

        class_gender = browse[3]
        gender_m = str(Find).find("masculine")
        gender_f = str(Find).find("feminine")
        if gender_m != -1 and gender_f != -1:
            gender = "unisex"
            gender_word = "unisex"
        elif gender_m != -1 and gender_f == -1:
            gender = "male"
            gender_word = "m"
        elif gender_m == -1 and gender_f != -1:
            gender = "female"
            gender_word = "f"
        else:
            pass



        class_usage = browse[4]
        ismulti_usage = class_usage.find(",")

        if ismulti_usage == -1:
            start_class_usage2 = class_usage.find("/names/")
            end_class_usage2 = class_usage.find("</")
            class_usage2 = class_usage[start_class_usage2:end_class_usage2]
            start_usage = class_usage2.find("\">")
            usage = class_usage2[start_usage + 2:]
            usage = usage.strip().strip(",").strip(", ")
        else:
            usageList = class_usage.split(",")
            multi_usage = ""
            for i in usageList:
                start_class_usage2 = i.find("/names/")
                end_class_usage2 = i.find("</")
                class_usage2 = i[start_class_usage2:end_class_usage2]
                start_usage = class_usage2.find("\">")
                if i == usageList[0]:
                    multi_usage += class_usage2[start_usage + 2:]
                else:
                    multi_usage += ", " + class_usage2[start_usage + 2:]
            multi_usage = multi_usage.strip().strip(",").strip(", ")
            usage = multi_usage.split(", ")

        if type(usage) == list:
            for add_usage in usage:
                try:
                    if add_usage in names_dir:
                        names_dir[add_usage][gender_word].append(name)
                    else:
                        start = add_usage.find("(")
                        end = add_usage.find(")")
                        add_usage = add_usage[:start]
                        add_usage = add_usage.strip()
                        names_dir[add_usage][gender_word].append(name)
                except Exception:
                    print(f"There was an error adding {name} in {add_usage}: {gender}")
        elif type(usage) == str:
            if usage:
                try:
                    if usage in names_dir:
                        names_dir[usage][gender_word].append(name)
                    else:
                        start = usage.find("(")
                        end = usage.find(")")
                        usage = usage[:start]
                        usage = usage.strip()
                        names_dir[usage][gender_word].append(name)
                except Exception:
                    print(f"There was an error adding {name} in {add_usage}: {gender}")
            else:
                try:
                    names_dir["None"][gender_word].append(name)
                except Exception:
                    print(f"There was an error adding {name} in \"None\": {gender}")

with open("Names.json", "w") as file:
    file.write(json.dumps(names_dir))

print(names_dir)