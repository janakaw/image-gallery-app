#!/bin/bash

base_images=()
projects=()

function rem_pattern() {
  find . -name "$1" -exec rm "{}" +
}

function get_project_dirs() {
  (
    IFS=$'\n'
    projects=($(find ./* -type d  ! -iname ".*"  -exec basename {} \;))
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
