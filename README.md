
# Stray Dog Map Iran

## Introduction

Stray Dog Map Iran is a project designed to map the locations of stray dogs in Iran using information provided by the public. The aim of this initiative is to raise awareness about the stray dog population and assist animal welfare organizations in their efforts to provide care and support for these animals.

## Features

- **User-Submitted Locations**: Users can input locations and descriptions of stray dogs they encounter.
- **Interactive Map**: A dynamic map that displays the locations of reported stray dogs.
- **Data Management**: Efficient storage and retrieval of user-submitted data.

## Motivation

The number of stray dogs in Iran has been increasing, leading to various social and environmental issues. By creating a centralized database and interactive map, we aim to:
- Raise public awareness about the stray dog issue.
- Assist animal welfare organizations in identifying areas with high stray dog populations.
- Encourage community participation in caring for stray dogs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary libraries.

```bash
pip install -r requirements.txt
```

## Usage
1. Run the application script to input dog locations and generate a map:

```bash
   python main.py
```
2. Input new locations and generate the map: Follow the instructions within the app to input data about stray dogs and view the interactive map.

## Project Structure

The project follows the MVC (Model-View-Controller) design pattern, making it modular and easy to manage.
```
Stray-Dog-Map-Iran/
├── controllers/
│   ├── __init__.py
│   └── main_controller.py
├── models/
│   ├── __init__.py
│   └── dog_model.py
├── views/
│   ├── __init__.py
│   └── main_view.py
├── main.py
├── requirements.txt
└── README.md

```
- controllers/: Contains the controller logic.

    - `main_controller.py`: Handles the interaction between the model and the view.

- models/: Contains the data models.

    - `dog_model.py`: Manages the data related to the dogs.

- views/: Contains the UI components.

    - `main_view.py`: Manages the user interface and interactions.

- [main.py](main.py): The entry point of the application.

- [requirements.txt](requirements): Lists the dependencies needed to run the application.

- [README.md](README.md): Provides information about the project.

## Contributions
Contributions are welcome! Please read the Contributing Guide for more details.

## License
This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.

## Support
To support this project and help us expand our efforts, consider making a donation. Your contributions will help us improve the platform and reach more communities in need.

## Purpose and Vision

This project is dedicated to supporting stray dogs facing difficult circumstances. Our mission is to advocate for animal welfare and nature conservation worldwide. By raising awareness and providing tools for the public to report and track stray dogs, we strive to create a positive impact on both animals and the environment.

## Contact 

For more information or to get involved, please contact farzin7akbari@gmail.com
