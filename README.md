# Imagine Python SDK

Imagine SDK is a Python library that provides a convenient interface to interact with the Imagine API for image generation and manipulation. This README provides an overview of the library's features, installation instructions, and usage examples.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Imagine Client](#imagine-client)
  - [Response](#response)
  - [Image](#image)
  - [Some More Usage Examples](#some-more-usage-examples)
- [Integration With Other Libraries](#integration-with-other-libraries)
  - [Pillow (PIL)](#pillow-pil)
  - [Numpy](#numpy)
- [Support](#support)
- [License](#license)

## Installation

The API works for python 3.6 and above. To install the package, execute the following command:

```bash
pip install imaginesdk
```

## Usage

The SDK needs to be configured with an API key which is available [here](https://platform.imagine.art/). It will be passed to the Imagine class as an argument while instantiating it.

```python
from imagine import Imagine
from imagine.enums import Styles
from imagine.enums import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the generations feature
response = client.generations(
    prompt='''
    A vibrant and whimsical fantasy forest with magical creatures, glowing plants, 
    and a flowing river, in a digital painting style inspired by video games like Ori and the Blind Forest.
    ''',
    style=Styles.Generations.IMAGINE_V5,
)

# Check if the request was successful
if response.status == Status.OK:
    image = response.data
    image.as_file("result.png")
else:
    print(f"Status Code: {response.status.value}")
```

**Result**:

![Generations](https://user-images.githubusercontent.com/56919667/261864112-0e419627-cbbe-4fb1-82e2-2637ee6392fb.png)

### Imagine Client

The Imagine class acts as a facade, providing an interface to interact with all of our endpoints. It currently provides the following features:

- **Generations**: `generations() -> Response[Image]`
- **Background**: `background() -> Response[Image]`
- **Edits**: `edits() -> Response[Image]`
- **Enhance**: `enhance() -> Response[Image]` 
- **Face**: `face() -> Response[Image]` 

For the full list of parameters and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

### Response

Response is the return type for each of our functions. It contains the following:

- `status`: Status property which returns an enum containing the status code of the response.
- `data`: A property which contains the request response.
- `get_or_throw()`: either returns the response content or raises an Error if the response content was empty.
- `get_or_else()`: either returns the response content or returns the default value if its empty.

For the full list of arguments and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

### Image

All the functions related to Images contain an Image data type as the data in their Response. It currently provides the following:

#### bytes

Returns the bytes received after a request operation

```python
image.bytes # -> bytes
```

#### as_file(file_path: str)

Stores the image in the specified path and returns the path.

```python
image.as_file("file_path") # -> str (file_path)
```

#### to_pil_image()

The module is loaded dynamically and is not included in the default package, you can choose to forgo this dependency. [See this](#integration-with-other-libraries) for more information.

#### to_numpy()

The module is loaded dynamically and is not included in the default package, you can choose to forgo this dependency. [See this](#integration-with-other-libraries) for more information.

## Integration With Other Libraries

The Imagine SDK has two levels of dependencies. By default, only the requests library is shipped as a dependency. If you want to use Pillow and Numpy as well, execute the following command:

```bash
pip install imaginesdk[all]
```

If you want one but not the other dependency then you also have the option of installing the module separately.

### Pillow (PIL)

> If you installed imaginesdk[all], you can skip the first step.

First, get the dependency for Pillow

```bash
pip install Pillow
```

After running the aforementioned command you can now use the response data as a pillow object:

```python
image.to_pil_image() # -> PIL_Image
```

### Numpy

> If you installed imaginesdk[all], you can skip the first step.

First, get the dependency for Numpy

```bash
pip install numpy
```

After running the aformentioned command you can now use the response data as a numpy object:

```python
image.to_numpy() # -> numpy.ndarray
```

## Support

If you run into any version issues, please contact us at [api.imagine@vyro.ai](api.imagine@vyro.ai) or [support.imagine.api](support.imagine@vyro.ai)

## License

This project is licensed under the Apache 2 License.
