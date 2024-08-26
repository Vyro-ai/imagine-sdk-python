Usage
-----

The SDK needs to be configured with an API key which is available `here <https://platform.imagine.art/>`_. It will be passed to the Imagine class as an argument while instantiating it.

.. code-block:: python

   from imagine.client import Imagine
   from imagine.enums import Styles, Status

   # Initialize the Imagine client with your API token
   client = Imagine(token="your-api-token")

   # Generate an image using the generations feature
   response = client.generations(
     prompt="A vibrant and whimsical fantasy forest with magical creatures, glowing plants, and a flowing river, in a digital painting style inspired by video games like Ori and the Blind Forest.",
      style=Styles.Generations.IMAGINE_V5,
   )

   # Check if the request was successful
   if response.status == Status.OK:
      image = response.data
      image.as_file("result.png")
   else:
      print(f"Status Code: {response.status.value}")

**Result**:

.. image:: https://user-images.githubusercontent.com/56919667/261864112-0e419627-cbbe-4fb1-82e2-2637ee6392fb.png
   :alt: Generations

Imagine Client
~~~~~~~~~~~~~~

The `Imagine class <imagine.html#module-imagine.client>`_ acts as a facade, providing an interface to interact with all of our endpoints. It currently provides the following features:

- **Generations**: ``generations() -> Response[Image]``
- **Background**: ``background() -> Response[Image]``
- **Edits**: ``edits() -> Response[Image]``
- **Enhance**: ``enhance() -> Response[Image]``
- **Face**: ``face() -> Response[Image]``

For the full list of parameters and other details, check out the `documentation <https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803>`_.

Response
~~~~~~~~

`Response <imagine.models.html#imagine.models.response.Response>`_ is the return type for each of our functions. It contains the following:

- **status**: Status property which returns an `enum <imagine.models.html#imagine.models.status.Status>`_ containing the status code of the response.
- **data**: A `property <imagine.models.html#imagine.models.status.Status>`_ which contains the request response.
- **get_or_throw()**: either returns the response content or raises an Error if the response content was empty.
- **get_or_else()**: either returns the response content or returns the default value if it's empty.

For the full list of arguments and other details, check out the `documentation <https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803>`_.

Image
~~~~~

All the functions related to Images contain an `Image <imagine.models.html#imagine.models.image.Image>`_ data type as the data in their Response. It currently provides the following:

**bytes**

Returns the bytes received after a request operation. 

For more details on this function, check out the `documentation <imagine.models.html#imagine.models.image.Image.bytes>`_.

.. code-block:: python

    image.bytes  # -> bytes

**as_file(file_path: str)**

Stores the image in the specified path and returns the path.

For more details on this function, check out the `documentation <imagine.models.html#imagine.models.image.Image.as_file>`_.

.. code-block:: python

    image.as_file("file_path")  # -> str (file_path)

**to_pil_image()**

The module is loaded dynamically and is not included in the default package, you can choose to forgo this dependency. `See this <integration.html>`_ for more information.

For more details on this function, check out the `documentation <imagine.models.html#imagine.models.image.Image.to_pil_image>`_.

**to_numpy()**

The module is loaded dynamically and is not included in the default package, you can choose to forgo this dependency. `See this <integration.html>`_ for more information.

For more details on this function, check out the `documentation <imagine.models.html#imagine.models.image.Image.to_numpy>`_.
