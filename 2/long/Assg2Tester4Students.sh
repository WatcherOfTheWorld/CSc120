################################################################
# CS120 - Spring 2017 - Pokemon Grading script                 #
#                 Abigal Dodd && Tito Ferra                    #
################################################################
# Notes:
# - 'printf' is used in order to allow easier handling
#   of input for Python
# - 'tests' directory contains the expected output
# - Pokemon.csv is the pokemon file we'll be using
# - TEST is an array containing the input for these test cases


#Test case input
TEST[0]="./tests/Pokemon.csv\nTotal\nTotal\nTotal\n\n"
TEST[1]="./tests/Pokemon.csv\nHP\nHP\n\n"
TEST[2]="./tests/Pokemon.csv\nAttack\nAttack\nAttack\nAttack\nAttack\n\n"
TEST[3]="./tests/Pokemon.csv\nDefense\nDefense\nDefense\nDefense\nDefense\nDefense\nDefense\n\n"
TEST[4]="./tests/Pokemon.csv\nSpecialAttack\nSpecialAttack\nSpecialAttack\nSpecialAttack\n\n"
TEST[5]="./tests/Pokemon.csv\nSpecialDefense\nSpecialDefense\n\n"
TEST[6]="./tests/Pokemon.csv\nSpeed\nSpeed\nSpeed\nSpeed\nSpeed\nSpeed\n\n"
TEST[7]="./tests/Pokemon.csv\nTotal\nTotal\nHP\nAttack\nSpecialDefense\nTotal\nHP\nSpeed\nDefense\nAttack\nalphabet\nSpeed\n\nSpeed\nHP\nTotal\n\n" 


# If files already exist    
if [[ -e "results.txt" ]] 
then
  rm "results.txt" "error.txt"
fi

#############################
#      Testing with Pokemon #
#############################
printf "Testing pokemon.py\n"  


# Testing
for i in $(seq 0 7)
do   
  # run Python program
  printf ${TEST[$i]} | python3 "pokemon.py" 2>> "error.txt" > "poke_out.txt" 

  # Diff
  printf "Test %d: " $i >> "results.txt"
  diff -iBw "poke_out.txt" <(cat "./tests/poke_expected$i.txt") >> "diff_result.txt"

  # Prepare nice and readable output for failure
  if [[ -s "diff_result.txt" ]]
  then
    printf "Failed\nInput: " >> "results.txt"
    printf ${TEST[$i]} >> "results.txt"
    printf "Expected: " >> "results.txt"
    cat "./tests/poke_expected$i.txt" >> "results.txt"
    printf "\nReceived: " >> "results.txt"
    cat "poke_out.txt" >> "results.txt"
    printf "\n\n" >> "results.txt"
  else
    printf "Passed\n" >> "results.txt"
  fi
  rm "poke_out.txt"
  rm "diff_result.txt"
done
