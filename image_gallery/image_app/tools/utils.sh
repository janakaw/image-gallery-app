#!/bin/bash

base_images=()

function rem_pattern() {
  find . -name "$1" -exec rm "{}" +
}

function get_project_dirs() {
  (
    IFS=$'\n'
    projects=($(find ./Project/* -type d  ! -iname ".*"  -exec basename {} \;))
    echo $(IFS=$';'; echo "${projects[*]}")
  )
}

function rename_files() {
  (
    IFS=$'\n'
    files=($(find ./slider/* -type f -name "H900-[0-9]*.jpg"   -exec basename {} \;))
    mkdir -p "slider/new"
    for i in "${!files[@]}"; do
      printf "*******%s\n" "${files[i]}"
      cp "slider/${files[i]}" "slider/new/H900-${i}.jpg"
    done
  )
}

function count_files() {
  IFS=$'\n'
  projects=($(find ./projects/* -type d  -name "[0-9]*"  -exec basename {} \;))
  if [ -f "./json/projects" ]; then
    rm "./json/projects"
  fi
  touch "./json/projects"
  for i in "${!projects[@]}"; do
      count=$(find "./projects/${projects[i]}/" -type f -name "H380-[0-9]*.jpg" -print | wc -l)
      desc=$(cat "./projects/${projects[i]}/text")
      printf "%s %s %s\n" "${projects[i]}" "$desc" "$count" >> ./json/projects
  done
}

function create_index_list() {
  projects_str=$(get_project_dirs)
  projects=(${projects_str//;/ })
  mkdir -p "projects"
  for i in "${!projects[@]}"; do
      printf "*******%s\n" "${projects[i]}"
      cp -r "Project/${projects[i]}/" "projects/${i}"
      echo "${projects[i]}" > "projects/${i}/text"
  done
}

function del_numeric() {
    (
    IFS=$'\n'
    num_dirs=($(find ./* -type d -name "[0-9]*"  -exec basename {} \;))
    for i in "${!num_dirs[@]}"; do
      printf "%s\n" "${num_dirs[i]}"
      rm -rf "${num_dirs[i]}"
    done
  )
}

function get_project_str() {
    in_str="Commercial_Alexander_project_ACT,_Developer,_Bugress_Rawson"
    out_str=$(sed -i 's/developer,//gi' $in_str)
    return "$out_str"
}

function get_base_images() {
    IFS=$'\n'
    base_images=($(find . -type f  -regex ".*/[0-9]+.jpg"))
    echo "${base_images[@]}"
}

function resize_image() {
  out_dir=$(dirname "$1")
  image_name=$(basename "$1")
  out_image="H$2-$image_name"
  convert "$1" -resize x"$2" "$out_dir"/"$out_image"
}

function resize_batch() {
    get_base_images
    if [[ -z $1 ]]; then
      return
    fi
    for i in "${base_images[@]}"; do
      resize_image "$i" "$1"
    done
}
