#!/usr/bin/env python3

import os
from jinja2 import Template

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.') and os.path.isdir(os.path.join(path, f)):
            subdir = os.path.join(path, f)
            if f != "base":
                yield f

def get_image_directories():
  circle_directory = os.path.dirname(os.path.realpath(__file__))
  return list(listdir_nohidden(os.path.join(circle_directory,'../')))

def main():
    """ Render the Jinja2 template file
    """
    circle_directory = os.path.dirname(os.path.realpath(__file__))
    config_template_path = os.path.join(circle_directory, "config.yml.j2")
    config_path = os.path.join(circle_directory, "config.yml")

    with open(config_template_path, "r") as circle_ci_config_template:
        templated_file_content = circle_ci_config_template.read()
    template = Template(templated_file_content)
    config = template.render(
        images=get_image_directories()
    )
    warning_header = "# Warning: automatically generated file\n" + \
                     "# Please edit config.yml.j2, and use the script make_config.py\n"
    with open(config_path, "w") as circle_ci_config_file:
        circle_ci_config_file.write(warning_header)
        circle_ci_config_file.write(config)


if __name__ == "__main__":
    main()
