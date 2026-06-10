import os

exp_path = r'd:\_ASSISTANTS\COURSES\SEM_4\IML254\projects\personal_website\experience.html'
with open(exp_path, 'r', encoding='utf-8') as f:
    exp_content = f.read()

# Replace broken deep links with root domains
exp_content = exp_content.replace('https://inqka.uitm.edu.my/main/index.php/kik', 'https://inqka.uitm.edu.my')
exp_content = exp_content.replace('https://www.mpc.gov.my/team-excellence', 'https://www.mpc.gov.my')

with open(exp_path, 'w', encoding='utf-8') as f:
    f.write(exp_content)
