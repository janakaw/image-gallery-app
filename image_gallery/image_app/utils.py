import glob
import json
import os
from pathlib import Path


class ProjectUtils:

    projects = []
    sliders = []
    project_path = Path('/var/image_gallery/static/images/images-gallery/Project')
    slider_path = Path('/var/image_gallery/static/images/images-gallery/slider')

    def __init__(self):
        self.get_projects()
        self.get_slider_image_count()

    @staticmethod
    def get_projects():
        ProjectUtils.projects = [ name for name in os.listdir(ProjectUtils.project_path)]
        return ProjectUtils.projects

    @classmethod
    def get_project_cover_image(cls, project_id):
        file_path = cls.project_path / cls.projects[int(project_id)] / "H380-0.jpg"
        img = open(str(file_path), 'rb')
        return img

    @classmethod
    def get_project_image_list(cls, project_id):
        images = []
        proj_path = cls.project_path
        proj_dir = cls.projects[int(project_id)]

        project_path = "{}/{}/[0-9].jpg".format(proj_path, proj_dir)
        for f in glob.glob(project_path):
            images.append(os.path.basename(Path(f)).replace(".jpg", ""))
        return images

    @classmethod
    def get_project_image(cls, project_id, image_id):
        file_path = cls.project_path / cls.projects[int(project_id)] / "{}.jpg".format(image_id)
        img = open(str(file_path), 'rb')
        return img

    @classmethod
    def get_project_text(cls, project_id):
        project_text = cls.projects[int(project_id)]
        return project_text

    @classmethod
    def get_slider_image_count(cls):
        ProjectUtils.sliders = [name for name in os.listdir(ProjectUtils.slider_path)]
        return len(ProjectUtils.sliders)

    @classmethod
    def get_slider_image(cls, slider_id):
        slider_path = ProjectUtils.slider_path / f"H900-{int(slider_id)}.jpg"
        slider_img = open(str(slider_path), 'rb')
        return slider_img

    @classmethod
    def get_slider_text(cls, slider_id):
        slider_text_path = ProjectUtils.slider_path / f"{str(int(slider_id) + 1)}.json"
        with open(str(slider_text_path), 'rb') as f:
            slider_text = json.load(f)
            return slider_text

