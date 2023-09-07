Usage
-----

The SDK needs to be configured with an API key which is available `here <https://platform.imagine.art/>`_. It will be passed to the Imagine class as an argument while instantiating it.

.. code-block:: python

   from imagine.client import Imagine
   from imagine.features.generations.style_ids import GenerationsStyle
   from imagine.models.status import Status

   # Initialize the Imagine client with your API token
   client = Imagine(token="your-api-token")

   # Generate an image using the generations feature
   response = client.generations(
     prompt="A vibrant and whimsical fantasy forest with magical creatures, glowing plants, and a flowing river, in a digital painting style inspired by video games like Ori and the Blind Forest.",
      style=GenerationsStyle.IMAGINE_V5,
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

- **Text-To-Image**: ``generations() -> Response[Image]``
- **Image-Remix**: ``image_remix() -> Response[Image]``
- **Super-Resolution**: ``super_resolution() -> Response[Image]``
- **Variations**: ``variations() -> Response[Image]`` `(Currently Not Supported)`
- **In-Painting**: ``in_painting() -> Response[Image]`` `(Currently Not Supported)`

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

Some More Usage Examples
~~~~~~~~~~~~~~~~~~~~~~~~

**Variations**

.. note::

   Currently Not Supported

.. code-block:: python

    from imagine.client import Imagine
    from imagine.features.generations.style_ids import GenerationsStyle
    from imagine.models.status import Status

    # Initialize the Imagine client with your API token
    client = Imagine(token="your-api-token")

    # Generate an image using the variations feature
    response = client.variate(
        image_path="anime_girl.png",
        prompt="a cute anime girl in a forest",
        style=GenerationStyle.ANIME,
    )

    # Check if the request was successful
    if response.status == Status.OK:
        image = response.data
        image.as_file("result.png")
    else:
        print(f"Status Code: {response.status.value}")

**Result**:

.. image:: https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7a2a54f2-c762-45ea-a1bd-c655ed421caa%2Fbanner_2.png?table=block&id=d60f4549-e35c-4044-afaa-7cd9d17803a2&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2
   :alt: Variate

**In-Painting**

.. note::

   Currently Not Supported

.. code-block:: python

    from imagine.client import Imagine
    from imagine.features.in_painting.style_ids import InPaintingStyle
    from imagine.models.status import Status

    # Initialize the Imagine client with your API token
    client = Imagine(token="your-api-token")

    # Generate an image using the in_painting feature
    response = client.in_painting(
        image_path="couple.png",
        mask_path="mask.png",
        prompt="woman sitting next to a teddy bear",
        style=InPaintingStyle.BASIC,
    )

    # Checking the request status
    if response.status == Status.OK:
        image = response.data
        image.as_file("result.png")
    else:
        print(f"Status Code: {response.status.value}")

**Result**:

.. image:: https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7017cedd-aeda-4a3e-ad09-54eb8b93399d%2Finpainting.jpg?table=block&id=1bc58f0f-1d7f-465f-b414-200ceb2464b1&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2
