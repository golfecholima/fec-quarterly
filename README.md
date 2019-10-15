# FEC 2019 Q3

Gathering FEC filing summaries for competitive 2020 races at the Q3 deadline

*Created by George LeVines (<george.levines@gmail.com>)*

*Reporter: George LeVines (<george.levines@gmail.com>)*

## Project goal

*CQ Roll Call politics reporters are interested in saving some time reporting quarterly summaries for competitive races. This attempts to help them do that.*

## Project notes

### Staff involved

*Political reporters Simone Pathé and Bridget Bowman gathered list of candidate committee IDs. Ilana Marcus helped with bash script. NewsNerds #campfin helped with various FEC filing questions. And Chris Zubak-Skees built [this miracle thing](https://github.com/PublicI/fec-loader/).*

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
