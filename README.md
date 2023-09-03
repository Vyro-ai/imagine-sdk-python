# Imagine SDK
Imagine SDK is a Python library that provides a convenient interface to interact with the Imagine API for image generation and manipulation. This README provides an overview of the library's features, installation instructions, and usage examples.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Integration With Other Libraries](#integration-with-other-libraries)
- [License](#license)


## Installation

The api works for python 3.6 and above. To install the package, execute the following command: 
```bash
pip install imaginesdk
```
If you run into any version issues, please contact us at [api.imagine@vyro.ai](api.imagine@vyro.ai).

## Installation

### Pip Install
The SDK is available as a package on PyPI.

**Simply run the following command:**
```bash
pip install vyroimagine
```

## Usage

The SDK needs to be cnfigured with an api key which is available [here](https://platform.imagine.art/). It will be passed to the Imagine class as an argument while instantiating it.
```python
from imagine.client import Imagine
from imagine.features.generations.style_ids import GenerationsStyle
from imagine.models.status import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the generations feature
response = client.generations(prompt="A vibrant and whimsical fantasy forest with magical creatures, glowing plants, and a flowing river, in a digital painting style inspired by video games like Ori and the Blind Forest.", style=GenerationsStyle.IMAGINE_V5)

# Check if the request was successful
if response.status is Status.OK:
    image = response.data
    image.as_file("result.png")
else:
    print(f"Status Code: {response.status.value}")
```
**Result**:

![Generations](https://user-images.githubusercontent.com/56919667/261864112-0e419627-cbbe-4fb1-82e2-2637ee6392fb.png)

The Imagine class acts as a facade, providing an interface to interact with all of our endpoints. It currently provides the following features:
- **Text-To-Image**: generations() -> Response[Image]
- **Image-Remix**: image_remix() -> Response[Image]
- **Super-Resolution**: super_resolution -> Response[Image]
- **Variate**: variate -> Response[Image]
- **In-Painting**: in_painting() -> Response[Image]
- **Alter-Image**: alter_image() -> Response[Image]

For the full list of arguments and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

Response is the return type for each of our functions. It contains the following:
- status: Status property which returns an enum contatining the status code of the response.
- data: A property which contains the request response.
- get_or_throw() -> either returns the response content or raises an Error if the response content was empty.
- get_or_else(default: T) -> either returns the response content or returns the default value if its empty.

For the full list of arguments and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

All the functions related to Images contain an Image data type as the data in their Response. It currently provides the following:
- bytes: returns the response bytes as recieved.
- as_file(file_path: str) -> str (file_path): Stores the image in the specified path and returns it. 
- to_pil_image() -> PIL_Image (The module is loaded dynamically, you can choose to forgo this dependency)
- to_numpy() -> numpy.ndarray (The module is loaded dynamically, you can choose to forgo this dependency)

### Some More Usage Examples:
**Variate**:
```python
from imagine.client import Imagine
from imagine.features.generations.style_ids import GenerationsStyle
from imagine.models.status import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the variations feature
response = client.variate(image_path="anime_girl.png", prompt="a cute anime girl in a forest", style=GenerationStyle.ANIME)

# Check if the request was successful
if response.status is Status.OK:
    image = response.data
    image.as_file(f"result.png")
else:
    print(f"Status Code: {response.status.value}")
```
**Result**:
![Variate](https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7a2a54f2-c762-45ea-a1bd-c655ed421caa%2Fbanner_2.png?table=block&id=d60f4549-e35c-4044-afaa-7cd9d17803a2&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2)

**In-Painting**:
```python
from imagine.client import Imagine
from imagine.features.in_painting.style_ids import InPaintingStyle
from imagine.models.status import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the in_painting feature
response = client.in_painting(image_path="couple.png", mask_path="mask.png", prompt="woman sitting next to a teddy bear", style=InPaintingStyle.BASIC)

# Checking the request status in a try-catch block
if response.status is Status.OK:
    image = response.data
    image.as_file(f"result.png")
else:
    print(f"Status Code: {response.status.value}")

```
**Result**:
![InPainting](https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7017cedd-aeda-4a3e-ad09-54eb8b93399d%2Finpainting.jpg?table=block&id=1bc58f0f-1d7f-465f-b414-200ceb2464b1&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2)


## Integration With Other Libraries

The Imagine Sdk has two levels of dependencies. By default only the requests library is shipped as a dependency. If you want to use Pillow and Numpy as well, execute the following command:
```bash
pip install imaginesdk[all]
```

### Pillow (PIL)

After running the aformentioned command you can now use the response data as a pillow object:
```python
image.to_pil_image()
```

### Numpy

After running the aformentioned command you can now use the response data as a numpy object:
```python
image.to_numpy()
```

## License
This project is licensed under the Apache 2 License.
