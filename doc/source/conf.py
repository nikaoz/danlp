import os
import sys
import sphinx_rtd_theme
import m2r #Convert md files to rs
from sphinx.domains.python import PyField
from sphinx.util.docfields import Field

#print("Evironment \n{}\n".format(os.environ))

#print("Before, current path: ", sys.path)
sys.path.insert(0, os.path.abspath('../../danlp'))
import danlp.about as about
#print("Sys path: ", sys.path)
#print("Current path with os: ", os.getcwd())

#if not 'READTHEDOCS' in os.environ:
#    sys.path.insert(0, os.path.abspath('..'))
#sys.path.append(os.path.abspath('./demo/'))

#on_rtd = os.environ.get('READTHEDOCS') == 'True'
#print("Printing the environment", os.environ)
#print("******************* In rdt", on_rtd)
#if on_rtd:
#    html_theme = 'default'
#else:
#    html_theme = 'nature'

# -- Project information -----------------------------------------------------

project = about.__title__
copyright = about.__license__
author = about.__author__
release = about.__version__

print("!!!!! Test values !!!! ")
print("Project: ", project)
print("copyright: ", copyright)
print("author: ", author)
print("Realese: ", release)

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinxcontrib.apidoc',
    'm2r',
]
apidoc_module_dir = '../../'
apidoc_output_dir = 'rstFiles'
apidoc_excluded_paths = ['setup.py', 'danlp/about.py', 'danlp/download.py', 'danlp/utils.py', 'tests']
apidoc_separate_modules = True

add_module_names = False

templates_path = ['_templates']
#exclude_patterns = ['setup.py']

#Html theme
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'canonical_url': 'https://github.com/alexandrainst/danlp',
    'style_external_links': True,
    'prev_next_buttons_location': 'bottom',
}
html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "alexandrainst", # Username
    "github_repo": "danlp", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/documentation/", # Path in the checkout to the docs root,
    'author': 'Testing author name',
}

# Extensions to theme docs
