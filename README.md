# Calculations of Geoidal Heights

In this project, I attempt to calculate the geoidal heights in different points, by using gravimetric models and measurements.

## Setting up the virtual enviroment on mac

Head to the root folder of the project:

```bash
cd ~/Desktop/my_project
```
Create the virtual enviroment:

```bash
python3 -m venv venv
```
Activate the enviroment:

```bash
source venv/bin/activate
```

## Creating the requirements.txt

After entering the venv, type this command to create or update the text file containing the current packages installed in the venv:

```bash
pip freeze > requirements.txt
```

## Installing the dependencies

When the user is inside the venv and wants to install the dependencies for the project, use this command: 

```bash
pip install -r requirements.txt
```


## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
