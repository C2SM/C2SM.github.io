---
title: Climate Model Data
layout: default
nav_order: 1
parent: Datasets
---

# Climate Model Data

## "Raw" CMIP archives (as downloaded from ESGF)

| Archive   | Size (#Files)[<sup>3</sup>](#3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CMIP2     |	0.01 TB (500)       |	IAC            |	direct / rsync | frozen (2010-10) |	           | native[<sup>1</sup>](#1) |
| CMIP3     |	6 TB (40’000)       |	IAC            |	direct / rsync | frozen (2016-12) |	           | native |
| CMIP5     | 130 TB (700’000)    | IAC            |  direct / rsync | frozen (2023/01) |	           | native |
| CMIP6     |	520 TB (5’500’000)  | IAC, Euler[<sup>4</sup>](#4) |  direct / rsync | weekly updated   |	           | native |

## CMIP next generation (checked, standardized, regridded to common grid)

| Archive   | Size (#Files)[<sup>3</sup>](#3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CMIP3-ng[<sup>2</sup>](#2) | 0.5 TB (5’000)   |	IAC 	         | direct / rsync  | frozen (2019-03) | 	  	     | native and 2.5°x2.5° |
| CMIP5-ng[<sup>2</sup>](#2) | 33 TB (100’000)  | IAC            | direct / rsync  | frozen (2019-09) |  	         | native and 2.5°x2.5° |
| CMIP6-ng[<sup>2</sup>](#2) | 175 TB (500’000) | IAC, Euler[<sup>4</sup>](#4) | direct / rsync  | ongoing          |	monthly: co2mass, hfls, mrro, npp, rlds, rsdscs, rtmt, tasmin, tsl, evspsbl, hfss, mrros, pr, rldscs, rsdt, sftlf, tauu, zg500, evspsblsoi, hurs, mrso prw, rlus, rsus, siconc, tauv, evspsblveg, huss, mrsol, psl, rlut, rsuscs, ta, tos, areacella, gpp, lai, mrsos, ra, rlutcs, rsut, tas, tran, clt, hfds, nbp, rh, rsds, rsutcs, tasmax, treeFrac, zos, daily: pr, tas, tasmin, tasmax, zg500, mrro |	native and 2.5°x2.5° |

## "Raw" CORDEX (as downloaded)

| Archive   | Size (#Files)[<sup>3</sup>](#3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CORDEX    |	370 TB (800’000) 	  | IAC, Euler[<sup>4</sup>](#4), CSCS[<sup>5</sup>](#5) | direct / rsync | monthly updated | | 0.44° and 0.11° |
| CORDEX-ReKliEs | 23 TB (100’000) | IAC, Euler[<sup>4</sup>](#4)          | direct         |	monthly updated |	|  	0.11° |

## CORDEX data for climate scenarios (checked, regridded to identical grids if necessary)

| Archive   | Size (#Files)[<sup>3</sup>](#3)   |	Location 	     | Access          | Status           |	Variables  |	Resolution |
| --------- | ------------------- | -------------- | ----------------|------------------|------------| -----------|
| CORDEX.ch2018 |	11 TB (1’800) |	IAC, CSCS[<sup>5</sup>](#5) |	direct |	frozen (2019-04) |	daily: hurs, huss, pr, rsds, sfcWind, sfcWindmax, snw, tas, tasmax, tasmin |	0.44° and 0.11° |
| CORDEX.ch2025 |	46 TB (3’500) |	IAC[<sup>6</sup>](#6) |	direct 	| ongoing |	daily: pr, tas, tasmax, tasmin, zg500 |	0.44° and 0.11° |
| CORDEX-FPSCONV |	30T (22'949) |	CSCS[<sup>7</sup>](#7), IAC [<sup>8</sup>](#8) |	direct / rsync |	ongoing |	1hr: pr, tas, daily: pr, tas, tasmax, tasmin |	2-3km  |

---

<a id="1"></a><sup>1</sup> Native means every model on their native grid they were run on

<a id="2"></a><sup>2</sup> CMIP-ng: Next Generation archives were maintained by Reto's group (Jan Sedlacek/Lukas Brunner)
Ruth Lorenz / C2SM took over cmip6-ng in 2022. contact: cmip6-archive@env.ethz.ch, documentation: https://doi.org/10.5281/zenodo.3734128

<a id="3"></a><sup>3</sup> As of June 2021

<a id="4"></a><sup>4</sup> `/nfs/atmos/c2sm`

<a id="5"></a><sup>5</sup> `/store/c2sm/c2sme`

<a id="6"></a><sup>6</sup> `/net/ch4/data/cordex.ch2025/`

<a id="7"></a><sup>7</sup> `/store/c2sm/c2sme/CH202X/CORDEX-FPSCONV/ALP-3/`

<a id="8"></a><sup>8</sup> `/net/krypton/hyclimm_nobackup/CORDEX-FPSCONV/ALP-3/`
