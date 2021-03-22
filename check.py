#!/usr/bin/env python3

import subprocess

command = subprocess.run(['git', 'log', '-n', '4', '--pretty=format:%s'], cwd="main_repo", stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0].startswith("merge branch"), "The top most commit shall be a merge commit, but it isn't"
assert result[1] == "add student's new file", "The commit message of the second commit should be 'Add student's new file'"
assert result[2] == "add john's new file", "The commit message of the second commit should be 'dd John's new file'"

print ("Exercise successfully done")
