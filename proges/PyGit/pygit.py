import os
import sys
import config
import path, dirrectory


def reset(projects):
    not_saved = check(projects)

    for project in projects:
        if project in not_saved:
            os.chdir(project)

            if os.path.isdir(project) and not ('clean' in os.popen('git status').read() and check):
                name = os.path.basename(project)

                print("\n" + name + "\n")
                
                dirrectory.remove(os.path.join(project, ".git"))

                commit = input("Commit: ")
                if commit == '': commit = name

                for command in ('init', 'add .', f'commit -m"{commit}', 
                                f'remote add origin {config.GIT.format(name)}',
                                'push --force --set-upstream origin master'):
                    os.system(f'git {command}')


def check(projects):
    not_saved = []
    
    for project in projects:
        if os.path.isdir(project):
            os.chdir(project)

            if not 'clean' in os.popen('git status').read():
                not_saved.append(project)
    
    return not_saved


def save(project, commit, branch = 'master'):
    os.chdir(project)
    
    if commit == '':
        commit = os.path.basename(project)

    if os.path.isdir(project) and not 'clean' in os.popen('git status').read():
        os.chdir(project)

        for command in ('add .', f'commit -m"{commit}"', f'push -u origin {branch}'):
            os.system(f'git {command}')


projects = []
project_folders = []
for sub_folder in dirrectory.sub_folders(config.MAIN):
    if os.path.isdir(sub_folder) and not os.path.basename(sub_folder) == '.git':
        project_folders.append(sub_folder)
        for project in dirrectory.sub_folders(sub_folder):
            if os.path.isdir(project) and not os.path.basename(project) == '.git':
                projects.append(project)


command = sys.argv[1]

if command == "reset":
    if '-out' in sys.argv:
        selected_projects = set(projects + project_folders) - set(sys.argv[3:])

    else:
        if len(sys.argv) <= 2:
            selected_projects = input("Select Projects: ").split(' ')
        
        else:
            selected_projects = sys.argv[2:]


        if selected_projects == "all": 
            selected_projects = projects

    for project in projects + project_folders:
        if project in selected_projects:
            reset([project])

elif command == "check":
    not_saved = check(projects)

    for project in not_saved:
        print(project)

elif command == "save":
    if len(sys.argv) <= 2:
        selected_project = input("Select Projects: ").split(" ")
    
    else:
        selected_project = sys.argv[2]
    
    commit = input("Commit: ")
    branch = input("Branch: ")
    
    print()

    for project in projects + project_folders:
        if os.path.basename(project) == selected_project:
            selected_project = project
            break
    
    save(selected_project, commit, branch)

elif command == "projects":
    print("Projects: ")
    for project in projects:
        print(project)
    
    print()

    print("Project Folders: ")
    for project_folder in project_folders:
        print(project_folder)
