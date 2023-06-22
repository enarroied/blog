---
tags: sphinx
date: "2023-06-22"
category: "Blog"
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"user_expressions": []}

Writing my personal blog with sphinx and Jupyter Notebooks: Throwing some light to the motivations.
=============

+++ {"user_expressions": []}

Welcome to my blog! I write it using sphinx and Jupyter notebooks. I have talked a little bit about why I did this in my [hello world post](https://ericnarrodata.com/blog/2023/hello_world.html).

I have written a [full Medium article](https://medium.com/@ericnarro/building-a-personal-blog-with-python-and-sphinx-45f9794869a4) on how to build a blog just like this one.

+++ {"user_expressions": []}

Here, I want to give some more details about why I created this blog, and also some deeper thoughts on the stack I chose. And last but not least, I want to discuss a little how it feels to blog using Jupyer Notebooks, since this was an important point for choosing my stack.

```{figure} ../../_static/images/sunset.png
:name: sunset-fig
:align: center
:width: 400
A sunset
```

+++ {"user_expressions": []}

<h2 id="Why-I-wanted-to-have-my-personal-blog">Why I wanted to have my personal blog</h2>
<p>Creating a personal blog is a significant step for me. I have a genuine taste for writing and a desire to grow as both a communicator, a data analyst, and a developer. So here are the main reasons I started my personal blog:</p>
<ol>
<li>
<p><strong>Because I like writing</strong>: Writing allows me to express my thoughts, emotions,</p>
<p>and ideas in a way that no other medium can. I have always likes to write, way more than other forms of expression, like public speaking for example. And I could also add: because I like editing my own content, using my own pictures to illustrate my blog. This is my personal space and I can really do whatever I want with it, and that feels cool, even if nobody reads it.</p>
</li>
<li>
<p><strong>The Power of Explanation</strong>: Writing is not just about putting words on paper; it is about organizing thoughts and explaining complex concepts. By writing and explaining things, I become better at understanding them myself. So this blog (and my Medium articles, and my youtube channel...) are a way for me to become better at programming, data analysis and who knows what else!</p>
</li>
<li>
<p><strong>Becoming a Better Communicator</strong>: Effective communication is a skill that transcends various aspects of life, in general. And as a Data Analyst in particular, sharing your findings is a crucial part of the job. Communication skills can be gained with practice, so this blog is also a chance to improve all that.</p>
</li>
<li>
<p><strong>Sharing My Path and Experiences</strong>: The journey I've embarked upon is filled with unique experiences, valuable lessons, and insights gained along the way. Through my blog, I have a platform to share my path, the challenges I've faced, and the lessons I've learned. By opening up about my personal experiences, I hope to inspire and connect with others who may be on a similar journey, offering them support and guidance.</p>
</li>
<li>
<p><strong>Spreading Knowledge and Empowering Others</strong>: One of the most fulfilling aspects of maintaining a personal blog is the opportunity to share knowledge and contribute to the growth of others. Everyone has something valuable to offer, and by sharing my knowledge and expertise, I hope to help others in their own pursuits.</p>
</li>
</ol>

+++ {"user_expressions": []}

## Why I chose this stack

I have explained this part in my Medium article, but I want to add some depth to it:

1. **Centralized experience**:
    I previously created a blog with R and distill using RStudio. There was one thing I really liked about it: from Rstudio, I was able to do version control with git, write my blog, execute the R code and create the HTML files. I don't use R in my daily life, so I was really looking for a way to have a similar experience with python, and this is what this stack allows me to do, with either VS Code or Jupyter Lab. And that is pretty awesome.
    
2. **For the sake of using sphinx**:
    Prior to creating this blog, I had only used sphinx once, after a Python Convention ([that I documented](https://medium.com/better-programming/notes-from-pycon-fr-2023-convention-part-1-52b1e44214c8#0e8d) on Medium). I really liked the experience, and since sphinx is widely used in the industry (for project documentation), I thought it would be a great skill to practice (unlike distill, which was fun, but not that useful).
    
3. **For the sake of using Jupyter Lab**:
    While doing my research about the best way to create my blog, I found out so many great ways to extend Jupyter Lab and create really good-looking pages (I discuss this later).

4. **For speed (of creation)**:
    It is fast to create a post, time can be spent creating the content, which his great.


+++ {"user_expressions": []}

## Jupyter Lab: reasons why it is a great tool for blogging about data and tech

I use Jupyter Lab a lot at work, and there is a reason for that: it is super convenient. I had some doubts about it being a good option for blogging, but when I discovered how it could be extended, my only question became: why was i not informed about all this earlier?

### Reason number 1: Markdown

Markdown is easy to learn and very simple to implement. Its minimal syntax makes it very fast to write. For people like me, who are all over the place, it makes it very easy to edit and write at the same time.

For example, writing a blog title as: ``` # Title``` is way faster than the ```html``` equivalent (```<h1> Title </h1> ```)

### Reason number 2: Extensions

JupyterLab comes with many different extensions. For example: 

* I can integrate a spellchecker
* There is an extension to use black to format code
* I can add [chatGPT to my interface](https://github.com/jupyterlab/jupyter-ai)
* I have a git extension keep my repo up to date
* ...

### Reason number 3: Your code is formatted as code... and the result of it displayed

I don't think I should explain this, this is why people use Notebooks in the first place, just now, you use it for blogging.

For example, using the very classic iris dataset, we can create a chart using plotly:

```{code-cell} ipython3
import plotly.graph_objects as go
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
sepal_length = iris.data[:, 0]  # Sepal length
sepal_width = iris.data[:, 1]  # Sepal width

# Create a scatter plot
fig = go.Figure(
    data=go.Scatter(
        x=sepal_length,
        y=sepal_width,
        mode="markers",
        marker=dict(size=8, color=iris.target, colorscale="Viridis", showscale=True),
    )
)

# Customize the layout
fig.update_layout(
    title="Iris Sepal Data",
    xaxis_title="Sepal Length",
    yaxis_title="Sepal Width",
)

# Display the chart
fig.show()
```

+++ {"user_expressions": []}

### Reason number 4: I am familiar with it

I use Jupyter Notebooks all the time, at work, for personal projects. So it obviously is a good choice for me, maybe something else would work better for you, who knows... But if you read until here, you probably are considering blogging with notebooks, and I have to say, it feels nice!

+++ {"user_expressions": []}

### Reason number 5: Jupyterlab-Myst

Ok, this is an extension, I could have added it to number 2. But, this extension has some unique capabilities, that are just so great for blogging.


* We can create simple but nice visual elements, such as:
    - collapsible code blocks
    - Tabs
    - Grids that display cards...
    - Markdown syntax is extended to better handle images and other elements

```{tip} Tip boxes

Did you notice this box? we can create warning boxes, information boxes, etc, and we can also use them the add some color to the blog, instead of the traditional ```### ``` Markdown syntax.

See the following lines of code are in a collapsed cell. For this, I just added a ```hide-input``` cell tag (you can download this notebook and discover all that 😊)

By the way, it creates a ```numpy``` array of size 4:

```

```{code-cell} ipython3
:tags: [hide-input]

import numpy as np

array = np.arange(4)
```

+++ {"user_expressions": []}

```{tip} Creating tabs
**Among the many visual elements we can add, there is tabs, see for example:**

::::{tab-set}
:::{tab-item} Tab 1
:sync: tab1
[MyST Markdown](https://mystmd.org/) is great
:::
:::{tab-item} Tab 2
:sync: tab2
I ❤️ coding
:::
::::
```

+++ {"user_expressions": []}

```{tip} Working with images

**This tractor is an embeded image from another website**:

```{figure} https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f38bd36f-bfc7-4fbf-931e-93a12b13a823/dfzmdqe-21c6a00f-1075-48e1-9331-268d3b6decae.jpg/v1/fill/w_1280,h_962,q_75,strp/pink_tractor_1_by_ericnarro_dfzmdqe-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTYyIiwicGF0aCI6IlwvZlwvZjM4YmQzNmYtYmZjNy00ZmJmLTkzMWUtOTNhMTJiMTNhODIzXC9kZnptZHFlLTIxYzZhMDBmLTEwNzUtNDhlMS05MzMxLTI2OGQzYjZkZWNhZS5qcGciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.Ek4xuKXVzPxUS9_fwUrdYwqUC5tbRhd1cZJYdFgy_M0
:name: my-fig
:align: center
:width: 400

A **tractor** in the vines 🚜.

```

+++ {"user_expressions": []}

__________

And that will be it for now, all this is pretty cool, I can't wait to discover some more stuff!

See you next time!
