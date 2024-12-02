import pandas as pd

excel_path_1 = "inflearn.xlsx"
readme_path = "README.md"

inflearn = pd.read_excel(excel_path_1, index_col=None)
inflearn = inflearn.fillna("")

if "Unnamed: 0" in inflearn.columns:
    inflearn = inflearn.rename(columns={"Unnamed: 0": ""})
markdown_table_1 = inflearn.to_markdown(index=False)

with open(readme_path, "r") as file:
    readme_content = file.readlines()

start_marker_1 = "<!-- START INFLEARN TABLE -->\n"
end_marker_1 = "<!-- END INFLEARN TABLE -->\n"
start_index_1 = readme_content.index(start_marker_1) + 1
end_index_1 = readme_content.index(end_marker_1)

updated_readme = (
    readme_content[:start_index_1] +
    [markdown_table_1 + "\n"] +
    readme_content[end_index_1:]
)

with open(readme_path, "w") as file:
    file.writelines(updated_readme)
