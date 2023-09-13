# scsc2023_demo
Demo for Stevens Computer Science Club GitHub workshop

## Cloning
You can clone this repo by copying the command below and pasting into your terminal.     
```
git clone https://github.com/joshbernsteint/scsc2023_demo
```    
**NOTE**: The URL in the command above is gotten simply by taking the URL of this page.

## Branching
To create a new GitHub branch from the command line, type the following command:
```
git checkout -b [NAME OF NEW BRANCH]
```
To get a list of all active branches on your computer, you can type:
```
git branch
```
The branch with an asterisk is the current branch you are on.

To switch branches, you can do one of two commands:
```
git switch [NAME OF BRANCH]
```
or
```
git checkout [NAME OF BRANCH]
```

It's important to note that you cannot switch branches until you commit what you have already changed.

## Adding, Committing, and Pushing
### Adding
To add a file to be tracked by git (to prep for committing), you can do either
```
git add [name of file]
```
to only track one file, or
```
git add .
```
to add all valid files in the directory

### But what does "valid files" mean?
In the home directory of the repo, you can include a [.gitignore](.gitignore) file. This file details files or file types to exclude from being tracked by GitHub. See the one in this repo for examples of how it works
### Committing
The most basic way to commit your tracked changes is to do the following command:
```
git commit -m "[MESSAGE]"
```
The message is used to label the changes you have made, and can be anything (but try to be descriptive)

### Pushing
Pushing updates the online repo with the changes that have been previously committed. Once you have committed changes, you can type:
```
git push
```
**NOTE:** The first time you push in a repository,it may give you an error saying push requires additional arguments, such as `--set-upstream origin main`. Simply follow the directions the terminal outputs.

## Additional git commands
|   Command         |       Description                                             |
|   :---:           |       :---                                                    |
|   `git pull`     |        Downloads the newest commit to your local repo          |
|   `git reset`     |       Removes all files added by  `git add`                   |
|   `git merge [branch]`     |       Merges `[branch]` with the current wroking branch                               |
|   `git merge [src] [tar]`     |       Merges branch `[src]` with the branch `[tar]`                                |
|   `git reset`     |       Removes all files added by  `git add`                                                   |           
|   `git status`     |       Gets up to date status of repository <br/>(if it is or not)                            |
|   `git log`     |       Returns a list of every commit and its message<br/> made to the repository                |


View an even longer list [here](https://www.loginradius.com/blog/engineering/git-commands/)
