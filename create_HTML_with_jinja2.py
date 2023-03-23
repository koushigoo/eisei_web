#%%
import gspread
from google.oauth2.service_account import Credentials

# お決まりの文句
# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定。
credentials = Credentials.from_service_account_file("C:\\Users\\Lenovo\\Dropbox\\学校用\\D1\\eiseikagaku-sheet-api-f3c39c50f9f5.json", scopes=scope)
#OAuth2の資格情報を使用してGoogle APIにログイン。
gc = gspread.authorize(credentials)

#スプレッドシートIDを変数に格納する。
SPREADSHEET_KEY = "14CPjUBi4KvIPkw-121STDHERuHTKHpqkPcZw6xRuFrw"
# スプレッドシート（ブック）を開く
workbook = gc.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.sheet1

#%%
# get_all_values gives a list of rows.
rows = worksheet.get_all_values()
print(rows)

#%%
import re
def clean(string):
    file_name = re.sub(r'[\\|/|:|?|"|<|>|\|]', '-', string)
    return file_name

from urllib import parse
URL = "https://docs.google.com/forms/d/e/1FAIpQLScT49x69waetiKe0gua2XuHo35ujf5GDkO7b6d-nD46zD3JLw/viewform"
URL2 = ""

# %%
# 22/10/4 いい感じのwebページにする
URL = "https://docs.google.com/forms/d/e/1FAIpQLScT49x69waetiKe0gua2XuHo35ujf5GDkO7b6d-nD46zD3JLw/viewform"
URL2 = ""
dicto = {"細胞培養":[], "試薬":[], "消耗品":[]}

for item in rows[1:]:
    order_by = parse.quote(item[0], safe = '/-_~')
    rgnt_name = parse.quote(item[1], safe = '/-_~')
    manufac_name = parse.quote(item[2], safe = '/-_~')
    catno = parse.quote(item[3], safe = '/-_~')
    norm = parse.quote(item[4], safe = '/-_~')
    num = parse.quote(item[5], safe = '/-_~')
    etc = parse.quote(item[6], safe = '/-_~')
    category = item[7]
    URL2 = URL + "?usp=pp_url&" + "entry.64995494=" + order_by + "&entry.1159638795=" + rgnt_name + "&entry.324196607=" + manufac_name+ "&entry.1345709044=" + catno + "&entry.1062189828=" + norm + "&entry.1261218697=" + num + "&entry.52235968" + etc
    if category not in dicto:
        dicto[category] = []
    dicto[category].append((clean(item[1]),URL2))

for key in dicto:
    print("<h2>" + key + "</h2>")
    dicto[key].sort(key = lambda item: item[0])
    for item, URL2 in dicto[key]:
        print("<a href=" + URL2 +" >" + item +"</a><br>")

# %%
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('HTML_template.html')
rendered_html = tmpl.render(dicto=dicto)

# %%
with open("index.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)
print(rendered_html)

# %%
import git
url = "https://github.com/koushigoo/eisei_web.git"
repo = git.Repo()
repo.git.add("index.html")
try:
    repo.git.commit("index.html", message="autoupdate")
except:
    print("no changes detected")
    pass
else:
    print("commited")
    repo.git.push(url, "main")
    print("push success")
# %%
