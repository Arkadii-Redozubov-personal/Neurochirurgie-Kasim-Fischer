import re

with open("admin/dashboard.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "treatments: treatmentsData,",
    "pages: pagesData,\n          treatments: treatmentsData,"
)

content = content.replace(
    "const exportObj = { treatments: treatmentsData, team: teamData, texts: textsData };",
    "const exportObj = { pages: pagesData, treatments: treatmentsData, team: teamData, texts: textsData };"
)

with open("admin/dashboard.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Dashboard export logic updated")
