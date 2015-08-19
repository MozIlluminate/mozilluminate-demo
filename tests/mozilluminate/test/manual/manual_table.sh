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

cp ../../../../tests/mozilluminate/test/manual/table_template.md test$timeid.md
git add test$timeid.md
git commit -m "Created new table case X in new suite A"

sync
pause

rm test$timeid.md
git add -A test$timeid.md
git commit -m "Removed all cases, cleanup"

sync
pause

git checkout master

