from django.shortcuts import render

import json
import urllib.request


# main single page
def render_page(request):
    with open("/var/image_gallery/static/json/projects") as f:
        projects_list = [line.split() for line in f]

    projects = []
    project_prefix = "http://localhost/static/projects"
    for i in projects_list:
        images = ["{}/{}/H380-{}.jpg".format(project_prefix, str(i[0]), str(j)) for j in range(0, int(i[2]))]
        desc = i[1].split(',')
        desc_len = len(desc)
        if desc_len == 0:
            desc = ["Project", "Developer"]
        elif desc_len == 1:
            desc.append("Developer")

        project = {
            "id": i[0],
            "main_image": "{}/{}/H380-0.jpg".format(project_prefix, str(i[0])),
            "image": "{}/{}/H380-0.jpg".format(project_prefix, str(i[0])),
            "images": images,
            "title": desc[0],
            "description": desc[1]
        }
        projects.append(project)

    with open("/var/image_gallery/static/json/sliders") as f:
        sliders = [line.split(' ')[1].split(',') for line in f]
    sliders_list = [row if len(row) >= 2 else row.append("Developer") for row in sliders]
    slider_prefix = "http://localhost/static/slider"
    sliders = [{"img": "{}/H900-{}.jpg".format(slider_prefix, str(i)), "caption": sliders_list[i][0],
                "title": sliders_list[i][1]} for i in range(0, len(sliders_list))]

    context = {
        'sliders': sliders,
        'projects': projects
    }

    with open("./debug", "+w") as f:
        f.write(json.dumps(context, indent=4))

    return render(request, 'base.html.j2', context=context)


def get_work_items():
    projects = []
    projects_json = {"projects": [{"id": 0, "name": "Commercial_Sunshine_Bay_NSW,_Developer,_Arendol_Admin"}, {"id": 1, "name": "Residential_3d_floor_plan,_Property_developer"}, {"id": 2, "name": "Residential_Casey_ACT,_Designer,_Neon_White_Design"}, {"id": 3, "name": "Residential_Retired_house_SA,_developer,_Rizwan"}, {"id": 4, "name": "Commercial_Young_street_NSW,_Developer,_Bugress_Rawson"}, {"id": 5, "name": "Commercial_Aranda_project_ACT,_Developer,_Ben_Hewlett"}, {"id": 6, "name": "Commercial_Childcare_NSW, Property_developer"}, {"id": 7, "name": "Residentialcommercial_Casey_ACT,_Architect,_Adhami_pender_architect"}, {"id": 8, "name": "Commercial_Alexander_project_ACT,_Developer,_Bugress_Rawson"}, {"id": 9, "name": "Taylor_ACT_developer_Shane_Anderson"}, {"id": 10, "name": "Residential_Lambton_NSW,_Architect,_Riz_office"}, {"id": 11, "name": "Residential_Multi_residential_unit_Seoul"}, {"id": 12, "name": "Residential_Ryde_NSW,_Developer,_Urbanwal_Group"}, {"id": 13, "name": "Residential_Unit_interior_VIC"}, {"id": 14, "name": "Commercial_Whyllar_ACT,_Developer,_Bugress_Rawson"}, {"id": 15, "name": "Residential_Kitchen_render_NSW,_Architect,_Riz_office"}, {"id": 16, "name": "Facotry_Bungendore_NSW,Property_developer"}, {"id": 17, "name": "Commercial_WagaWaga_Centerlink_NSW,_Architect,_Adhami_pender_architect"}, {"id": 18, "name": "Commercial_Goulburn_childcare_NSW,_Developer,_Bugress_rawson"}, {"id": 19, "name": "Residential_Multi_residential_project,_QLD"}, {"id": 20, "name": "Commercial_Rivett_ACT,_Developer,_Bugress_Rawson"}, {"id": 21, "name": "Commercial_Childcare_Sunshinebay_NSW,Arendol_Property_Developer"}, {"id": 22, "name": "Commerical_Pat_project_Seoul,Property_developer"}, {"id": 23, "name": "Residential_Corlette_NSW,_Architect,_Riz_design_office"}, {"id": 24, "name": "Residential_Kitchen_design_ACT,_Designer,_Meg_Campbell"}, {"id": 25, "name": "Residentialcommercial_Monash_ACT_Developer,_Brite_Development"}, {"id": 26, "name": "Commercial_Office_design_ACT,_Designer,_Dept_of_design"}, {"id": 27, "name": "Residential_Baulkham_hills_NSW,_Developer,_property_master_interior"}, {"id": 28, "name": "Residential_Baulkham_hills_NSW,_Developer,_property_master"}, {"id": 29, "name": "Residential_Multi_unit_project,_Architect,_Riz_design_office"}, {"id": 30, "name": "Commercial_Queanbeyan_childcare,_Developer,_Bugress_Rawson"}, {"id": 31, "name": "Commercial_Googong_NSW,_Developer,_Bugress_Rawson"}, {"id": 32, "name": "Residential_Woolware_rd_NSW,_Developer,_property_master"}, {"id": 33, "name": "Commercial_Taylor_ACT,_Developer,_Wonderschool"}]}
    #projects_url = urllib.request.urlopen('http://localhost:8000/image/projects')
    #projects_json = json.load(projects_url)

    len_projects = len(projects_json["projects"])
    for i in range(1, len_projects):
        text_url = urllib.request.urlopen(f'http://localhost:8000/image/project_text?project_id={i}')
        image_list = urllib.request.urlopen(f'http://localhost:8000/image/project_image_list?project_id={i}')
        images_json = json.load(image_list)
        text_json = json.load(text_url)
        text = text_json["text"]
        text = text.replace("Commercial", "").replace("Residential", "")

        image_url_list = []
        for j in images_json["images"]:
            image_url_list.append(f'http://localhost:8000/image/project_image?project_id={i}&image_id={j}')

        # = urllib.request.urlopen()
        project = {
            "id": f"project_{i}",
            "main_image": f'http://localhost:8000/image/project_image?project_id={i}',
            "image": f'http://localhost:8000/image/project_cover_image?project_id={i}',
            "images": image_url_list,
            "title": "",
            "description": text
        }
        projects.append(project)
    return projects



