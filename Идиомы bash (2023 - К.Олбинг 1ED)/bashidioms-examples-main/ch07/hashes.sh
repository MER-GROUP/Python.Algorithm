#!/usr/bin/env bash
# hashes.sh: bash Hash example code
# Original Author & date: _bash Idioms_ 2022
# bash Idioms filename: examples/ch07/hashes.sh
#_________________________________________________________________________
# Does not work on Zsh 5.4.2!

# Books are not as wide as some screens!
FORMAT='fmt --width 70 --split-only'

# Declare a hash                                                         <1>
declare -A myhash   # MUST do this, or `local -A` or `readonly -A`

# Assign to it, note no "+"                                              <2>
###myhash=(bar)            # Error: needs subscript when assigning associative array
myhash[a]='foo'            # Insertion 1, not 0...sort of
myhash[b]='bar'            # Insertion 2
myhash[c]='baz'            # Insertion 3
myhash[d]='three'          # 4 Different than our list example
myhash[e]='four'           # Insertion 5, note, not 4
myhash[f]='five by five'   # 6 Note spaces
myhash[g]='six'            # Insertion 7

# OR
#myhash=([a]=foo [b]=bar [c]=baz [d]="three" [e]="four" [f]="five by five" [g]="six")

# Display or dump the details and values                                 <3>
echo -e "\nThe key count is: ${#myhash[@]} or ${#myhash[*]}"

echo -e "\nThe length of the value of key [e] is: ${#myhash[e]}"

echo -e "\nDump or list:"
declare -p myhash | $FORMAT
echo -n      "\${myhash[@]}   = " ; printf "%q|"  ${myhash[@]}
echo -en   "\n\${myhash[*]}   = " ; printf "%q|"  ${myhash[*]}
echo -en "\n\"\${myhash[@]}\" = " ; printf "%q|" "${myhash[@]}"
echo -en "\n\"\${myhash[*]}\" = " ; printf "%q|" "${myhash[*]}"
echo -e "   # Broken!"  # Previous line is bad and no newline
# See `help printf` or chapter 6 "printf for reuse or debugging", we need
# this to show the correct words:
# %q	quote the argument in a way that can be reused as shell input

# "Join" the values                                                      <4>
function Join { local IFS="$1"; shift; echo "$*"; } # One character delimiter!
# Note the Join above requires "$*" and not "$@"!
echo -en "\nJoin ',' \${myhash[@]} = " ; Join ',' "${myhash[@]}"
function String_Join {
    local delimiter="$1"
    local first_element="$2"
    shift 2
    printf '%s' "$first_element" "${@/#/$delimiter}"
    # Print first element, then reuse the '%s' format to display the rest of
    # the elements (from the function args $@), but add a prefix of $delimiter
    # by "replacing" the leading empty pattern (/#) with $delimiter.
}
echo -n "String_Join '<>' \${myhash[@]} = " ; String_Join '<>' "${myhash[@]}"

# Iterate over the keys and values                                       <5>
echo -e "\nforeach \"\${!myhash[@]}\":"
for key in "${!myhash[@]}"; do
    echo -e "\tKey: $key; value: ${myhash[$key]}"
done

echo -e "\nBut don't do this: \${myhash[*]}"
for key in ${myhash[*]}; do
    echo -e "\tKey: $key; value: ${myhash[$key]}"
done

# Handle slices (subsets) of the hash                                   <6>
echo -e "\nStart from hash insertion element 5 and show a slice of 2 elements:"
printf "%q|" "${myhash[@]:5:2}"
echo '' # No newline in above
echo -e "\nStart from hash insertion element 0 (huh?) and show a slice of 3 elements:"
printf "%q|" "${myhash[@]:0:3}"
echo '' # No newline in above
echo -e "\nStart from hash insertion element 1 and show a slice of 3 elements:"
printf "%q|" "${myhash[@]:1:3}"
echo '' # No newline in above

#echo -e "\nShift FIRST key [0]:" = makes no sense in a hash!
#echo -e "\nPop LAST key:"        = makes no sense in a hash!

# Delete keys                                                            <7>
echo -e "\nDelete key c using unset (dumped before and after):"
declare -p myhash | $FORMAT
unset -v 'myhash[c]'
declare -p myhash | $FORMAT

# Delete the entire hash                                                 <8>
unset -v myhash
