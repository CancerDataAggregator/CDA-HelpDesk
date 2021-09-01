Installation
=====

.. _installation:

Install the CDA Python library locally:
--------------------------------------

1. Download and install docker click this `link <https://www.docker.com/products/docker-desktop/>`_ or copy url https://www.docker.com/products/docker-desktop to your Browser
2. Open Terminal or PowerShell a and navigate to cda-python folder then we will run a docker command:

   - ``docker compose up --build``
3. Open a Browser to this url http://localhost:8888 and you are up and running.

4. To Stop the container from running return to the terminal where the cdapython project is on your keyboard you will click **Control C to stop** the container .

To delete the container use this command in the cdapython project directory.

- ``docker compose down``

Pip install
------------
Alternatively, CDA Python can be installed using ``pip``. However, this requires python >= 3.6 on your system. To check your version at the command-line run ``python -V``. To update your version you can download from https://www.python.org/downloads/ additional python installation help can be found `here <https://realpython.com/installing-python/>`_ . Once you have the proper python version, you can run CDA using:

.. code-block:: console

   pip install git+https://github.com/CancerDataAggregator/cda-python.git

.. note:: 

   We recommend the docker method because pip installation can be a bit more cumbersome, and will not be as closely monitored as the docker installation.


