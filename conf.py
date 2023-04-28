# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

# -- Project information -----------------------------------------------------
import sys

sys.path.append("scripts")
sys.path.append(".")
from social_media import add_social_media_js, SocialPost

project = "Eric Narro Data"
copyright = "2023, Eric Narro"
author = "Eric Narro"

# load extensions
extensions = [
    "myst_nb",
    "ablog",
    "sphinx_panels",
    "sphinx_design",
    "jupyter_sphinx",
    "sphinx.ext.intersphinx",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    # "nbsphinx"
]

# specify project details
master_doc = "index"
project = "Eric Narro Data 📊"  # Meta: Site Name

# basic build settings
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
nitpicky = True

# Add theme
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "search_bar_text": "Search this site...",
    "analytics": {"google_analytics_id": "UA-88310237-1"},
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/enarroied/",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/enarrodata",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/ericnarro/",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}

html_favicon = "_static/images/logo.ico"
html_title = "📊 Eric Narro Data "
html_static_path = ["_static"]


# https://stackoverflow.com/questions/46269345/how-to-embed-plotly-graphs-in-sphinx-documentation-and-nbsphinx
html_js_files = [
    "js/custom.js",
    # https://myst-nb.readthedocs.io/en/latest/render/interactive.html?highlight=plotly#plotly
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
]


html_css_files = ["css/mycss.css"]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    "README.md",
    "**/.ipynb_checkpoints/*",
    "docs",
]

html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "projects": ["hello.html"],
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

#############################################################################
## Copied from:
## https://github.com/choldgraf/choldgraf.github.io/blob/main/conf.py

# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "blog",
}
#############################################################################


# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
]

# MyST-NB
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "auto"


# -- ABlog ---------------------------------------------------

# blog_baseurl = "https://ericnarrodata.com"
blog_title = "Eric Narro Data 📊"
blog_path = "blog"
blog_post_pattern = "blog/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Data Analysis, GIS and career transition advice."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2


# OpenGraph config
ogp_site_url = "https://www.ericnarrodata.com/"
ogp_image = "_static/images/logo_landscape.png"
ogp_social_cards = {"line_color": "#4078c0", "image": "_static/images/logo.png"}

ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
    '<meta name="twitter:site" content="@enarrodata" />',
    '<meta name="twitter:title" content="📊 Eric Narro Data" />',
    #'<meta name="twitter:description" content="Eric Narro\'s Blog. Data Anlysis 📊 | GIS 🌍 | Python 🐍 | Getting your first job as a Data Anlyst. I share insights, thoughts, tools to grow as a data analyst." />',
    #'<meta name="twitter:image" content="https://ericnarrodata.com/_static/images/logo_landscape.png" />',
]


## myst_nb default settings

# Custom formats for reading notebook; suffix -> reader
# nb_custom_formats = {}

# Notebook level metadata key for config overrides
# nb_metadata_key = 'mystnb'

# Cell level metadata key for config overrides
# nb_cell_metadata_key = 'mystnb'

# Mapping of kernel name regex to replacement kernel name(applied before execution)
# nb_kernel_rgx_aliases = {}

# Execution mode for notebooks
# nb_execution_mode = 'auto'

# Path to folder for caching notebooks (default: <outdir>)
# nb_execution_cache_path = ''

# Exclude (POSIX) glob patterns for notebooks
# nb_execution_excludepatterns = ()

# Execution timeout (seconds)
# nb_execution_timeout = 30

# Use temporary folder for the execution current working directory
# nb_execution_in_temp = False

# Allow errors during execution
# nb_execution_allow_errors = False

# Raise an exception on failed execution, rather than emitting a warning
# nb_execution_raise_on_error = False

# Print traceback to stderr on execution error
# nb_execution_show_tb = False

# Merge stdout/stderr execution output streams
# nb_merge_streams = False

# The entry point for the execution output render class (in group `myst_nb.output_renderer`)
# nb_render_plugin = 'default'

# Remove code cell source
# nb_remove_code_source = False

# Remove code cell outputs
# nb_remove_code_outputs = False

# Prompt to expand hidden code cell {content|source|outputs}
# nb_code_prompt_show = 'Show code cell {type}'

# Prompt to collapse hidden code cell {content|source|outputs}
# nb_code_prompt_hide = 'Hide code cell {type}'

# Number code cell source lines
# nb_number_source_lines = False

# Overrides for the base render priority of mime types: list of (builder name, mime type, priority)
# nb_mime_priority_overrides = ()

# Behaviour for stderr output
# nb_output_stderr = 'show'

# Pygments lexer applied to stdout/stderr and text/plain outputs
# nb_render_text_lexer = 'myst-ansi'

# Pygments lexer applied to error/traceback outputs
# nb_render_error_lexer = 'ipythontb'

# Options for image outputs (class|alt|height|width|scale|align)
# nb_render_image_options = {}

# Options for figure outputs (classes|name|caption|caption_before)
# nb_render_figure_options = {}

# The format to use for text/markdown rendering
# nb_render_markdown_format = 'commonmark'

# Javascript to be loaded on pages containing ipywidgets
# nb_ipywidgets_js = {'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js': {'integrity': 'sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=', 'crossorigin': 'anonymous'}, 'https://unpkg.com/@jupyter-widgets/html-manager@^0.20.0/dist/embed-amd.js': {'data-jupyter-widgets-cdn': 'https://cdn.jsdelivr.net/npm/', 'crossorigin': 'anonymous'}}
