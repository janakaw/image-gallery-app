

//
let galleries = []

function testgal(image_id) {
    let gallery = null
    try {
        galleries.forEach(function (item, index, array){
           if (item["id"] == image_id) {
               gallery = item["gal"];
               return
           }
        });
        if (gallery == null) {
            gallery = new Viewer(document.getElementById(image_id + "_1"), {
                //container: document.getElementById('portfolio'),
            });
            galleries.push({"id": image_id, "gal": gallery })
        }
        console.log("teest");
        console.log(image_id);
        gallery.show();
        gallery.stop();
    } catch (err) {
        console.log(err.message);
    }

}

// const gallery = new Viewer(document.getElementById('images'));