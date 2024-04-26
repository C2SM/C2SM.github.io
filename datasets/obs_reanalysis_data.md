---
title: Observational and Re-analysis Datasets
layout: default
nav_order: 1
parent: Datasets
---

# Observational and Re-analysis Datasets

## "Raw" Archives (as downloaded from the original source)

| Archive   | Size[<sup>1</sup>](#1) | Location | Access | Status                                | time period    | Variables | Temporal Resolution | Spatial Resolution | more information |
| --------- | --------------- | -------- | ------ | -------------------------------------- | -------------- | --------- | ------------------- | ----------------- | ----------------- |
| E-OBS     | 660G            | IAC      | direct | different versions, updated irregularly | 1950 - present | TG: mean temperature, TN: minimum temperature, TX: maximum temperature, RR: precipitation sum, PP: mean sea level pressure, FG: mean wind speed, HU: mean relative humidity, QQ: global radiation | daily | 0.1° and 0.25° | [E-OBS](https://www.ecad.eu/download/ensembles/download.php), [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/insitu-gridded-observations-europe?tab=overview) |
| MERRA2    | 15T             | IAC      | direct | updated | 1980 - present | many, temperature, precipitation, radiation, sea level pressure etc. | hourly, sst monthly | 0.5 lat x 0.625 lon (~50km) | [MERRA-2](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/), [Climate Data Guide](https://climatedataguide.ucar.edu/climate-data/nasas-merra2-reanalysis) |
| ERAInterim | 5T             | CSCS[<sup>2</sup>](#2) | direct | static | 1979-2019 | W_SO_REL, T_SO, W_SNOW, FR_LAND, T_SKIN, T_SNOW, FIS, T, U, V, QV, PS, QC, QI, FR_SEA_ICE | 6-hourly | 0.7° x 0.7° (80 km) global |
| ERA5      | 50T             | CSCS[<sup>3</sup>](#3) | direct | updated | 1979 - present | FIS, FR_LAND, FR_SEA_ICE, PS, QC, QI, QR, QS, QV, T, T_SKIN, T_SNOW, T_SO, U, V, W_SNOW, W_SO_REL | hourly | 0.28125° x 0.28125° (31 km)  | [ERA5 at CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview) |
| ERA5      | 17T             | IAC[<sup>4</sup>](#4) | direct | updated | 1940 - present | 2t, tp, 10si, mn2t, mx2t | monthly, hourly (variable dependent) | 0.25° x 0.25° | [ERA5 monthly](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=overview), [ERA5 hourly](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview), need to delete original data after processing because of size |
| ERA5-Land | 40T             | IAC[<sup>5</sup>](#5) | direct | updated | 1950 - present | 2t, snom | hourly (variable dependent) | 0.1° x 0.1° | [ERA5-Land](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form), need to delete original data after processing because of size |
| CERRA     | 16T             | IAC[<sup>6</sup>](#6) | direct | updated | 1985 - present | 2t, t, r, ... | 3-hourly | 5x5km | sub-daily regional reanalysis data for Europe, [Wishlist](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp), [Download Status](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0), space constraints prevent us from keeping all the 3-hourly data which have been processed into daily data, see sheet on download process |
| CERRA-Land | 12T             | IAC[<sup>7</sup>](#7) | direct | updated | 1985 - present | snom, sro, tp, ... | 3-hourly | 5x5km | [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview), [Wishlist](https://docs.google.com/document/d/1YtIabO5PMTsD_i_PqycmzIbrOYigNmuublt_i6FKrhY/edit#heading=h.brsa23yzcugp), [Download Status](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0), space constraints prevent us from keeping all the 3-hourly data which have been processed into daily data, see sheet on download process |

## Processed Archives (e.g. aggregated or regridded)

| Archive | Size[<sup>1</sup>](#1) | Location | Access | Status | time period | Variables | Temporal Resolution | Spatial Resolution | more information |
| ------- | --------------- | -------- | ------ | ------ | ----------- | ---------- | ------------------- | ----------------- | ----------------- |
| E-OBS and MCH | 50G | IAC[<sup>8</sup>](#8) | direct | static | 1971-2020 | tas, tasmax, tasmin, pr | daily | 0.11° | E-OBS (v23.1e and v26.0e) data with higher resolution MCH data over Switzerland (prepared for CH2025) |
| MCH | 7G | IAC[<sup>9</sup>](#9) | direct | static | 1971-2021 | tas, tasmax, tasmin, pr | daily | ~2km | gridded observational data from MeteoSwiss over Switzerland |
| MERRA2 | 17G | IAC[<sup>10</sup>](#10) | direct | updated | 1980-2015 (v0), 1980-2018 (v1) | tas, tasmax, tasmin, huss, psl, pr, hfss, hfls, rlus, rlds, rsds, rsus, tos | daily, monthly | 2.5 lat x 2.5 lon (same as cmip6-ng) files are consistent with cmip-ng archives, no time period is indicated in filenames |
| CERRA | 6T | IAC[<sup>11</sup>](#11) | direct | updated | 1985 - 2020 (v1) | 2t, t, r, ... | daily, monthly | 5x5km | sub-daily regional reanalysis data for Europe, [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-single-levels?tab=overview), [Status](https://docs.google.com/spreadsheets/d/1xfM4TZCGXZm4M4VLQW3XPyAk6IX9vjlwj_p6ymX4aDU/edit#gid=0) |
| CERRA-Land | 1.8T | IAC[<sup>12</sup>](#12) | direct | updated | 1985 - 2020 (v1) | snom, sro, tp, ... | daily, monthly | 5x5km | [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-cerra-land?tab=overview), [Status](https://docs.google.com/spreadsheets/d/1e58ps_yBmxUG0jvL8ZmNNr7Zz_UXuqIZsz4MdRAzvbM/edit#gid=0) |
| ERA5 | 500G | IAC[<sup>13</sup>](#13), Euler[<sup>14</sup>](#14) | direct | updated | v1: 1940 - present, v2: 1940 - present | v1: 2t, tp, mx2t, mn2t, v2: [<sup>15</sup>](#15) | daily, monthly | 0.25° x 0.25° | [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview) |
| ERA5-Land | 2.2T | IAC[<sup>16</sup>](#16) | direct | updated | 1950 - present | 2d, 2t, sd, snom | daily, monthly | 0.1° x 0.1° | [CDS](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form) |

---

<a id="1"></a><sup>1</sup> As of May 2022

<a id="2"></a><sup>2</sup> `/store/c2sm/c2sme/reanalyses_dkrz/ERAInterim`

<a id="3"></a><sup>3</sup> `/store/c2sm/c2sme/reanalyses_dkrz/ERA5`

<a id="4"></a><sup>4</sup> `/net/atmos/data/era5_cds/original`

<a id="5"></a><sup>5</sup> `/net/atmos/data/era5-land_cds/original`

<a id="6"></a><sup>6</sup> `/net/atmos/data/cerra/original`

<a id="7"></a><sup>7</sup> `/net/atmos/data/cerra-land/original`

<a id="8"></a><sup>8</sup> `/net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v23.1e/processed/, /net/co2/c2sm-data/ch202X/Obs_Data/EOBS/0.1deg_reg_v26.0e/processed/`

<a id="9"></a><sup>9</sup> `/net/co2/c2sm-data/ch202X/Obs_Data/MCH/processed/`

<a id="10"></a><sup>10</sup> `/net/co2/c2sm-data/rlorenz/MERRA2/`

<a id="11"></a><sup>11</sup> `/net/atmos/data/cerra/processed/v1/`

<a id="12"></a><sup>12</sup> `/net/atmos/data/cerra-land/processed/v1/`

<a id="13"></a><sup>13</sup> `/net/atmos/data/era5_cds/processed/`

<a id="14"></a><sup>14</sup> `/nfs/atmos/c2sm/era5/processed/v2/`, automounted, the automounter mounts filesystem when it is addresse, e.g. with "ls", "cd", before you cannot see it!

<a id="15"></a><sup>15</sup> `/net/atmos/data/era5_cds/processed/v2/`, [Variable list and progress](https://www.polybox.ethz.ch/index.php/s/5efYkkFrSVC64lZ)

<a id="16"></a><sup>16</sup> `/net/atmos/data/era5-land_cds/processed/v1/`
