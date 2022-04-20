# Installation Guide

There are two methods for local installation: Docker or Conda + pip:

## Docker (Recommended)

!!! requirements

    - git [(Install)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    - terminal/command line


1. [Download and install docker](https://www.docker.com/products/docker-desktop/){ .md-button }

2. Open Terminal or PowerShell and run:
```bash
git clone https://github.com/CancerDataAggregator/cda-python.git
```

3.  Navigate to the cda-python folder:
```bash
cd cda-python
```

4. Build the docker container:
```bash
docker-compose up --build
```

5. Open a Browser to [http://localhost:8888](http://localhost:8888).
This will open a docker container with all the required packages for using the API in ipython notebook.

!!! notes

    - To stop the container from running, return to the terminal window (from step 2), and type **Control C to stop** the container.

!!! notes

    To delete the container from your machine, use this command in the cda-python project directory.

    ```bash
    docker compose down
    ```

## Conda + Pip install

!!! requirements

    - terminal/command line
    - python version >= 3.7 [(Install)](https://www.python.org/downloads/)
    - conda [Install](https://docs.conda.io/en/latest/miniconda.html)

1. Open Terminal or PowerShell and create a new conda environment:
  ```bash
  conda create -n cda python=3.7
  ```
  type `y` when prompted

2. Activate the environment:
  ```bash
  conda activate cda
  conda install jupyter
  pip install git+https://github.com/CancerDataAggregator/cda-python.git
  cd cda-python
  jupyter notebook
  ```
  type `y` when prompted

3. Click on the folder called `notebooks`, then the file called `example.ipynb` to
  open the example workflow, or create a new notebook to run your own.


!!! notes
      You only need to create a new conda environment once!

      - To exit the conda environment, return to the terminal window (from step 1), and type **Control C to stop** the notebook then:
      ```bash
      conda deactivate
      ```
      - To return to the notebook in conda, open a terminal and type:
      ```bash
      conda activate cda
      jupyter notebooks
      ```

## Customizing your cda-python installation
### Installing previous versions of the cda-python

Versions Available:

   - 2.0.0
   - 2.1.0
   - 3.0.0 (default)

#### Docker

1. Navigate to the cda-python folder

2. Use a plain text editor (bbedit, textedit, vim, nano, emacs) to open the hidden file `.env`

3. Edit line 6 to the desired version:
```bash
GIT_TAG_VERSION = 2.0.0
```
or
```bash
GIT_TAG_VERSION = 2.1.0
```

4. Rebuild docker container:
```bash
docker-compose up --build
```

#### Conda + Pip
Specify the version in the pip install line for e.g.:

`pip install git+https://github.com/CancerDataAggregator/cda-python.git@<version>`


We recommend installing older versions in their own conda environments. For version 2.1.0:

1. Open Terminal or PowerShell and create a new conda environment:
  ```bash
  conda create -n cda2.1.0 python=3.7
  ```
  type `y` when prompted

2. Activate the environment:
  ```bash
  conda activate cda2.1.0
  conda install jupyter
  pip install git+https://github.com/CancerDataAggregator/cda-python.git@2.1.0
  cd cda-python
  jupyter notebook
  ```
  type `y` when prompted

### Modifying the localhost port in Docker

By default, both Docker and ipython notebook use port 8888. To use both simultaneously, change the Docker port:

1. Navigate to the cda-python folder

2. Use a plain text editor (bbedit, textedit, vim, nano, emacs) to open the hidden file `.env`

3. Edit line 4 to a different port:
```bash
NOTEBOOK_PORT = 8889
```
4. Rebuild docker container:
```bash
docker-compose up --build
```
