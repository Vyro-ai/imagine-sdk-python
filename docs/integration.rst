Integration With Other Libraries
----------------------------------

The Imagine SDK has two levels of dependencies. By default, only the requests library is shipped as a dependency. If you want to use Pillow and Numpy as well, execute the following command

.. code-block:: bash

   pip install imaginesdk[all]

If you want one but not the other dependency then you also have the option of installing the module separately.

Pillow (PIL)
~~~~~~~~~~~~

.. note::

   If you installed imaginesdk[all], you can skip the first step.

First, get the dependency for Pillow

.. code-block:: bash

   pip install Pillow

After running the aforementioned command you can now use the response data as a pillow object:

.. code-block:: python

   image.to_pil_image()  # -> PIL_Image

Numpy
~~~~~

.. note::

   If you installed imaginesdk[all], you can skip the first step.

First, get the dependency for Numpy

.. code-block:: bash

   pip install numpy

After running the aforementioned command you can now use the response data as a numpy object:

.. code-block:: python

   image.to_numpy()  # -> numpy.ndarray
