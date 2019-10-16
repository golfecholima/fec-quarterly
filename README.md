# FEC 2019 Q3

Gathering FEC filing summaries for competitive 2020 races at the Q3 deadline

*Created by George LeVines (<george.levines@gmail.com>)*

*Reporter: George LeVines (<george.levines@gmail.com>)*

## Project goal

*Save some time reporting on quarterly summaries for competitive races.*

## Project notes

* You need [fec-loader](https://github.com/PublicI/fec-loader/).
* FEC loader needs [PostgresQL](https://www.postgresql.org/download/).
* In postgres you need the standard localhost database called `postgres` with user `postgres` and no password.
 * If you change this stuff make sure to change it in `etl/fec.sh` and `etl/pgquery.py`.
* Do python stuff by running `pipenv shell` from the project root after cloning.

### People involved

* Political reporters Simone Pathé and Bridget Bowman gathered list of candidate committee IDs. 
* Ilana Marcus helped with bash script. 
* NewsNerds #campfin helped with various FEC filing questions. 
* And Chris Zubak-Skees built [this miracle thing](https://github.com/PublicI/fec-loader/).

### Data sources

* [FEC filings data](https://www.fec.gov/data/filings/?data_type=efiling)

## Technical

* In `etl/fec_files.py` change `committees` list to whatever campaigns you're interested in. Save the file.
  * The script filters the source data for those and `report_type` of `Q3`.
* From the project root run `.etl/fec.sh`.
* Find your output csv in `/data/processed`.

### Project setup instructions

After cloning the git repo:

* Pull filings bracketed by desired dates from [FEC filings data](https://www.fec.gov/data/filings/?data_type=efiling).
* Rename the file `filings.csv`.
* Put it in `/data/source`.

## Data notes

*Add important caveats, limitations, and source contact info here.*
