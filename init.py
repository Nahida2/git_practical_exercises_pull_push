#!/usr/bin/env python3

import subprocess

#Create a bare main repo
subprocess.run(['mkdir', 'main_repo'], stdout=subprocess.PIPE)
command = subprocess.run(['git', 'init', '--bare'], cwd="main_repo", stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower())
assert result.startswith("initialized empty git repository in"), "Could not initalize git repository"

#Create John's repository
subprocess.run(['mkdir', 'johns_repo'], stdout=subprocess.PIPE)
subprocess.run(['git', 'clone', '../main_repo'], cwd="johns_repo", stdout=subprocess.PIPE)

#Create the first commit
with open("johns_repo/main_repo/file.txt", "w") as file:
    file.write("First line")
subprocess.run(['echo', '"First line"', '>','file.txt'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)
subprocess.run(['git', 'add', 'file.txt'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)
subprocess.run(['git', 'commit', '-m', 'First commit'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)
subprocess.run(['git', 'push'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)

#Create the student's repo
subprocess.run(['mkdir', 'students_repo'], stdout=subprocess.PIPE)
subprocess.run(['git', 'clone', '../main_repo'], cwd="students_repo", stdout=subprocess.PIPE)

#Add John's commit
with open("johns_repo/main_repo/johns_file.txt", "w") as file:
    file.write("John\'s new file")
subprocess.run(['git', 'add', 'johns_file.txt'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)
subprocess.run(['git', 'commit', '-m', 'Add John\'s new file'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)
subprocess.run(['git', 'push'], cwd="johns_repo/main_repo", stdout=subprocess.PIPE)

