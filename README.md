<a name="readme-top"></a>
<h1 align="center">Weather App: Working with APIs in Python</h1>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#future-work">Future Work</a></li>
      </ul>
    </li>
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!--ABOUT THE PROJECT-->
## About the Project

![api_image](https://github.com/kira-vik/weather-app-api-project/assets/35596661/ea963511-7590-43d8-930c-3bb094dda74d)

_Weather App_ is a project aimed at helping understand how APIs work, and how to handle JSON data. 

It takes the city's name as user input, and uses [direct geocoding](https://openweathermap.org/api/geocoding-api) to get the geographical coordinates (lat, lon) of the city whose weather you are interested in. The geolocation acquired is then used to make a call to the OpenWeatherMap API to get the weather information, and finally display the retrieved data to the user. 

This project has been developed in VS Code, but it is okay to use your editor of choice. 


### Built With
- Python 3.11.0
- VS Code

<p align="right">
     [<a href="#readme-top">back to top</a>]
</p>



<!--GETTING STARTED-->
## Getting Started

### Prerequisites

Here are a few of the resources that you will need in order to properly set up and run the project in your system. 
- [Python](https://www.python.org/downloads/)
- A code editor


### Installation

Clone the repository by running the following command in your project directory:

```bash
git clone {project-link}
```

You can open the cloned repository in VS Code using the command in your project directory:
```bash
code . {project-path}
```

Set up a virtual environment to keep necessary dependencies isolated to this particular project:
```bash
python -m venv {virtual_env_name}
```

Activate the virtual environment:
- On Windows: 
```bash
{virtual_env_name}\Scripts\activate
```

- On macOS/Linux:
```bash
source {virtual_env_name}/bin/activate
```

Download the required libraries using the command in your project terminal:
```bash
pip install -r requirements.txt
```

Get a free API Key at [OpenWeatherMap](https://openweathermap.org/). You will need to create an account and sign in in order to obtain the API Key. Enter your API KEY in `weather_app.py` main function:
```python
API_KEY = "YOUR_API_KEY_GOES_HERE"
```

Finally, run the program with the command:
```bash
python weather_app.py
```

### Future Work

As the project currently is, it can only be run programatically in the project terminal with the command made available above. This would pose a problem for someone who is not tech-inclined. As such, future development on the project will include a GUI to further simplify the program's use, and present results in a more organized and visually appealing manner. 

> _A PROBLEM FOR FUTURE ME_


<p align="right">
     [<a href="#readme-top">back to top</a>]
</p>


<!--AUTHOR-->
## Author
Victor Weke - @[kira-vik](https://github.com/kira-vik)

Project Link: [here]


<!--LICENSE-->
## License
Copyright © 2024, Victor Weke.

Distributed under the [MIT](https://choosealicense.com/licenses/mit/) license. See `LICENSE.txt` for more information. 


<p align="right">
     [<a href="#readme-top">back to top</a>]
</p>
