#TODO: auto-varification

sync(){
  cd ../../../../tests/mozilluminate/
  git diff HEAD~1
  python sync.py
  #read -rsp $'Press any key to continue...\n' -n1 key
  cd -
}

pause(){
  read -rsp $'Press any key to continue...\n' -n1 key
}

timeid=$(date +%Y%m%d_%H%M)

echo "Before you run, make sure: "
echo "1. you are in tests/mozilluminate/test/manual"
echo "2. you are on the MASTER branch"
pause

git checkout -b test$timeid
cd ../../
source dangerous/setup_credential.sh
cd ../../apps/
mkdir -p test$timeid/test/manual
cd test$timeid/test/manual
touch test$timeid.md
echo "Test env created"

pause

printf "# Suite A $timeid\n\n## fxos.smoke.X\n\`bug 2\`\n\`story 1\`\n\`active\`\n\n WHEN This is a NEW case\nTHEN foo\nWHEN I click the button\nTHEN magic happends" > test$timeid.md
git add test$timeid.md
git commit -m "Created new case X in new suite A"

sync
pause

sed -i "s/NEW/MODIFIED/g" test$timeid.md
sed -i "s/active/draft/g" test$timeid.md
git add test$timeid.md
git commit -m "Modified case X"

sync
pause

sed -i "s/ A / B /g" test$timeid.md
git add test$timeid.md
git commit -m "Move case X from suite A to suite B"

sync
pause

sed -i "s/ B / A /g" test$timeid.md
printf "\n# Suite B $timeid\n\n## fxos.smoke.Y\n\`bug 2\`\n\`story 1\`\n\`active\`\n\n WHEN This is a NEW case\n" >> test$timeid.md
git add test$timeid.md
git commit -m "Move case X back to suite A, create new case Y in suite B"

sync
pause

head -n 8 test$timeid.md > tmp.md; mv tmp.md test$timeid.md
git add test$timeid.md
git commit -m "Removed case Y and suite B"

sync
pause

git checkout master

