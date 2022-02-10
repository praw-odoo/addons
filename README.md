# learnndevodoo

git remote update: update remotes

git fetch --all: fetches all references to local

git checkout: Used to change your current branch, for example if you are in master branch and want to
change branch to 15.0 or you want to create a new branch from remote

e.g. New Branch: git checkout -b branch_name origin/version
git checkout -b 15.0 odoo/15.0

If you just want to change current branch to other existing branch
git checkout existing_branch_name


git branch: To display all existing local branches

git pull: update local branch

git log: shows log/history of git commits

git status: shows current status of branch, what has been modified and added to the branch

git diff: display diff or changes done to current branch

git diff --staged: shows difference which has already been staged

git show: display last commit diff by default or if you pass commit reference then display diff of that
commit

git add . : adds current changes or new files

git commit: it commits changes to branch
e.g. git commit -am "your message" where option "a" stands for add and "m" stands for message

git push: it pushed commits to remote branch
e.g. git push remote_name your_branch_name
git push dev 15.0-my-widget-msh

force push i.e. -f: Avoid use of -f, don't use this option until you are sure you have all the commits in
your local branch which is there in remote branch

e.g. You have take a branch from commit A
Then your colleague also took same branch from commit A
Your colleague does some changes and committed those change to remote branch, so now branch is on commit B

You are still on commit A
You also did some changes and then try to commit with command git push remote your_branch_name, this command
will give you error and will not allow to push you

Many people does force push to resolve this condition but this is not the right way,
Because if you do a force push in that case, You commit will become commit B and your colleague's commit
will be removed from remote.

git commit --amend: adds changes to last commit but you need to do force push in this case

git rebase: rebase your head of the branch to remote branch

e.g. git rebase -i remote_name/branch_name where -i stands for interactive mode

git rebase -i odoo/master

git stash

git reset

git branch -D: Deletes local branch from your system

git checkout -- . : It removes all local changes from your branch

git cherry-pick

git init
