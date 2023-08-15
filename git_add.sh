git add --all
read -p "Enter the commit message: " message
git commit -m "$message"
git push origin `git branch --show-current`
