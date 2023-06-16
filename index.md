---
html_theme.sidebar_secondary.remove: true
myst:
  html_meta:
    description: "Eric Narro's Blog. Data Analysis 📊 | GIS 🌍 | Python 🐍 | Getting your first job as a Data Analyst. I share insights, thoughts, tools to grow as a data analyst."
    keywords: "Data Analysis, Python"
    property_og_locale: "en_US"
    property_og_description: "Eric Narro's Blog. Data Analysis 📊 | GIS 🌍 | Python 🐍 | Getting your first job as a Data Analyst. I share insights, thoughts, tools to grow as a data analyst."
---


# Eric Narro Data

::::{grid}
:::{grid-item-card}
:link: about.html
👨‍💻 About me
:::
:::{grid-item-card}
:link: projects.html
📊 Personal projects 
:::
:::{grid-item-card}
:link: blog.html
📗 My blog
:::
::::

## Recent blog posts

```{postlist}
:date: "%Y-%m-%d"
:format: "{title} - {date}"
:excerpts:
```

```{toctree}
:maxdepth: 2
:hidden:
about
projects
blog
```