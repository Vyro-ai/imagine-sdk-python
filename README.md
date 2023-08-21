# Imagine SDK
Imagine SDK is a Python library that provides a convenient interface to interact with the Imagine API for image generation and manipulation. This README provides an overview of the library's features, installation instructions, and usage examples.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Features

- Seamless integration with the Imagine API for image generation, remixing, super-resolution, and more.
- Clean and Pythonic API design for ease of use.
- Strongly typed responses and error handling for reliable interaction.

## Requirements

- Python 3.6+ (Required)
- NumPy (Optional)
- Pillow (Optional)
- Requests (Optional)

The optioal dependencies can be opted in for by using:
```bash
pip install -e .
```
Or manually installing the components you need. You have the option of plugging in your own implementation of certain components if you so choose to forgo using the provided ones. If you run into any version issues, please contact us at [api.imagine@vyro.ai](api.imagine@vyro.ai).

## Installation

### Pip Install
The SDK is available as a package on PyPI.

**Simply run the following command:**
```bash
pip install imaginesdk
```

### Cloning The Repository
You won't have need for this unless you want to modify the package itself.
- **Clone the repository to your local machine:**
```bash
git clone https://github.com/Vyro-ai/imagine-sdk-python.git
```
- **Open up the imagine-sdk-python directory**
- **Install the library and its dependencies using pip (Preferably activate a virtual environment before you proceed with this step)**
```bash
pip install .
```

## Usage

The SDK needs to be cnfigured with an api key which is available [here](#). It will be passed to the Imagine class as an argument while instantiating it.
```python
from imagine.client import Imagine
from imagine.enums.status.imagine import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the generations feature
response = client.generations(
        prompt="A vibrant and whimsical fantasy forest with magical creatures, glowing plants,"
        + " and a flowing river, in a digital painting style inspired by video games like Ori and the Blind Forest.",
        style_id=GenerationsStyle.STYLE_IMAGINE_V5
    )

# Check if the request was successful
if result.status == Status.OK:
    image = response.data
    image.to_pil_image().save("result.png")
else:
    print(f"Status Code: {response.status.value}")
```
**Result**:

![Generations](https://user-images.githubusercontent.com/56919667/261864112-0e419627-cbbe-4fb1-82e2-2637ee6392fb.png)

The Imagine class acts as a facade, providing an interface to interact with all of our endpoints. It currently provides the following features:
- **Text-To-Image**: ```generations() -> Response[ResponseImage]```
- **Image-Remix**: ```image_remix() -> Response[ResponseImage]```
- **Super-Resolution**: ```super_resolution() -> Response[ResponseImage]```
- **Variate**: ```variate -> Response[ResponseImage]```
- **In-Painting**: ```in_painting() -> Response[ResponseImage]```
- **Alter-Image**: ```alter_image() -> Response[ResponseImage]```

For the full list of arguments and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

Response contains the response data and status of each request. It contains the following:
- ```status: Status``` property which returns an enum contatining the status code of the response.
- ```data: Optional[T]``` property which contains the request response.
- ```get_or_throw() -> T``` either returns the response content or raises an Error if the response content was empty.
- ```get_or_else(default: T) -> T``` either returns the response content or returns the default value if its empty.

For the full list of arguments and other details, check out the [documentation](https://vyroai.notion.site/API-Documentation-e643af82991f4265841cff2951eac803).

All the functions related to Images contain a ResponseImage data type as the data in their Response. It currently provides the following:
- ```data: bytes``` returns the response bytes as they are.
- ```as_file(file_path: str) -> str (file_path)``` saves the image in the specified path and returns the path. 
- ```to_pil_image() -> PIL_Image``` (The module is loaded dynamically, you may choose to forgo this dependency)
- ```to_numpy() -> numpy.ndarray``` (The module is loaded dynamically, you may choose to forgo this dependency)

### Some More Usage Examples:
**Variate**:
```python
from imagine.client import Imagine
from imagine.enums.status.imagine import Status

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the variations feature
response = client.variate(
        image_path="anime_girl.png",
        prompt="a cute anime girl in a forest",
        style_id=ImagineGenerations.ANIME
    )

# Check if the request was successful
if response.status.value == 200:
    image = response.data
    image.as_file(f"result{i}.png")
else:
    print(f"Status Code: {response.status.value}")
```
**Result**:
![Variate](https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7a2a54f2-c762-45ea-a1bd-c655ed421caa%2Fbanner_2.png?table=block&id=d60f4549-e35c-4044-afaa-7cd9d17803a2&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2)

**In-Painting**:
```python
from imagine.client import Imagine

# Initialize the Imagine client with your API token
client = Imagine(token="your-api-token")

# Generate an image using the in-paintinting feature
response = client.in_painting(image_path="couple.png", mask_path="mask.png", prompt="woman sitting next to a teddy bear")

# Checking the request status in a try-catch block
try:
    image = response.get_or_throw()
    image.to_pil_image().save("result.png")

except ValueError as e:
    print(f"Error Code: {result.status.value}")

```
**Result**:
![InPainting](https://vyroai.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7017cedd-aeda-4a3e-ad09-54eb8b93399d%2Finpainting.jpg?table=block&id=1bc58f0f-1d7f-465f-b414-200ceb2464b1&spaceId=60572bb8-cbeb-42ba-b882-c88845384d44&width=2000&userId=&cache=v2)

## License
This project is licensed under the MIT License.
