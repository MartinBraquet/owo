# Automated OwO Hunt and Battle

[OwO](https://owobot.com/) is a Discord interactive game where the player can hunt animals and battle with them. However, this game
throttles the number of hunts and battles (one every 15 seconds). This Python script will take care of hunting and battling
as soon as it is available, without any human intervention. This makes it very cheap to level up animals.


## Installation

```shell
git clone git@github.com:MartinBraquet/owo.git
cd owo
pip install -e .
```

## Usage

### Configure credentials

Set up the following in the [credentials](credentials) file:
- your Discord username
- your Discord password
- the Discord URL of the server where your OwO game is set up

Note: the code in this repository will not share your credentials nor use it for any other purpose
than logging in on your machine and run the owo commands.


### Run

Run all the cells in the [owo.ipynb](owo.ipynb) notebook.

## Feedback

### Short Comments

For any issue / bug report / feature request,
open an [issue](https://github.com/MartinBraquet/owo/issues).

## Contributions

To provide upgrades or fixes, open a [pull request](https://github.com/MartinBraquet/owo/pulls).

## Disclaimer

This script might be violating some Discord or OwO guidelines; running it for too long
might block your OwO game for 1, 12, or more hours.

