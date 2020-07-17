# FEC 2019 Q3

Gathering FEC filing summaries for competitive 2020 races at the Q3 deadline

*Created by George LeVines (<george.levines@gmail.com>)*

## Project goal

*Save some time reporting on quarterly summaries for competitive races.*

## Project notes

* You need [fec-loader](https://github.com/PublicI/fec-loader/).
* FEC loader needs [PostgresQL](https://www.postgresql.org/download/).
* In postgres you need the standard localhost database called `postgres` with user `postgres` and no password.
* Do python stuff by running `pipenv install` and  `pipenv shell` from the project root after cloning.

### People involved

* Political reporters Simone Pathé and Bridget Bowman gathered list of candidate committee IDs.
* Ilana Marcus helped with bash script.
* NewsNerds #campfin helped with various FEC filing questions.
* And Chris Zubak-Skees built [this miracle thing](https://github.com/PublicI/fec-loader/).

## Technical

After cloning the git repo:

* From the command line in the root director.
  * Run `pipenv install` then `pipenv shell` then `jupyter-lab`, which should open an iPython Notebook in your browser.
* Open `analysis/fec_files.ipynb`.
* Follow the instructions there, running each cell as you go.
* Find your output in `data/processed`.

### Data sources

* [FEC filings data](https://www.fec.gov/data/filings/?data_type=efiling)

**NOTE**  
*While it's possible to download bulk(ish) raw data from https://www.fec.gov/data/filings/?data_type=efiling often the number of listed items is not the number of rows that will come out in your CSV (especially true on a filing deadline day). One way around this seems to be to fill in some date parameters that are outside the bounds of the dates you are interested in.*
