
let galleries = []

function show_project(project_id) {
    let gallery = null
    try {
        galleries.forEach(function (item, index, array){
           if (item["id"] == project_id) {
               gallery = item["gal"];
               return
           }
        });
        if (gallery == null) {
            gallery = new Viewer(document.getElementById(project_id + "_1"));
            galleries.push({"id": project_id, "gal": gallery })
        }
        gallery.show();
    } catch (err) {
        console.log(err.message);
    }
}
