Usage
=====

.. _installation:

Installation
------------

Install the CDA Python library locally:
--------------------------------------

1. Download and install docker click this `link <https://www.docker.com/products/docker-desktop/>` or copy url https://www.docker.com/products/docker-desktop to your Browser
2. Open Terminal or PowerShell a and navigate to cda-python folder then we will run a docker command
   - `docker compose up --build`
3. Open a Browser to this url http://localhost:8888 and you are up and running.

4. To Stop the container from running return to the terminal where the cdapython project is on your keyboard you will click **Control C to stop** the container .

To delete the container use this command in the cdapython project directory.

- `docker compose down`

Pip install
------------
Alternatively, CDA Python can be installed using `pip`. However, this requires python >= 3.6 on your system. To check your version at the command-line run `python -V`. To update your version you can download from https://www.python.org/downloads/ additional python installation help can be found `here <https://realpython.com/installing-python/>` . Once you have the proper python version, you can run CDA using:

`pip install git+https://github.com/CancerDataAggregator/cda-python.git`

**NOTE: We recommend the docker method because pip installation can be a bit more cumbersome, and will not be as closely monitored as the docker installation.**



To use cdapython, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

