import os
import shutil


path = 'W:\LabWork7.3\my_project'
all_files = os.listdir(path)
os.chdir(path)
for i in range(len(all_files)):
    files = os.listdir(all_files[i])
    os.chdir(all_files[i])
    for j in range(len(files)):
        if str(files[j]) == 'templates':
            if i == 0:
                shutil.copytree(files[j], 'W:/LabWork7.3/my_project_out/templates/authapp')
            else:
                shutil.copytree(files[j], 'W:/LabWork7.3/my_project_out/templates/mainapp')
            os.chdir(path)
