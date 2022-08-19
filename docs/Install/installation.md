# Installation Guide

CDA python runs on:

Mac OS python versions: 3.7, 3.8, 3.9, 3.10
Ubuntu python versions 3.7, 3.8, 3.9, 3.10
Windows python versions: 3.7, 3.8, 3.9, 3.10

There are two methods for local installation in virtual environments: Docker or Conda + pip.

**Installation without a virtual environment may have unexpected/unresolvable conflicts, and is not supported.**

## Docker

!!! requirements

    - git [(Install)](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    - terminal/command line


1. [Download and install docker](https://www.docker.com/products/docker-desktop/){ .md-button .md-button--primary}

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
