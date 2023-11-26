#! /bin/bash

function replace_readme_str() {
  #statements
  local file=$1/README.md
  local old=$2
  local new=$3

  perl -pi.bak -e "s/${old}/${new}/" $file
  rm -f $file.bak
}

function replace_readme_first() {
  #statements
  local file=$1/README.md
  local old=$2
  local new=$3

  perl -pi.bak -0 -e "s/${old}/${new}/" $file
  rm -f $file.bak
}

d=$1

platform=$2

replace_readme_str $d $platform "${platform}-pex"

replace_readme_first $d "- python" "- pex\n- python"