# Readme

## Project Description

Coding exercise for Professors Schmidt and Choukhmane.

Outline for `workbook.ipynb` is as follows:

-   Setup
-   Load Data
    -   FRED (pandas_datareader) - skip this section
    -   FRED (fredapi)
    -   Ford TFP
    -   Fernald TFP Shocks
    -   Shiller shock price data
    -   Check all loads
-   Merge Data
-   Data Processing
    -   Log real-per capita versions
    -   Log hours per capita
    -   Log real labor productivity
-   Local Projection (regression)
    -   Starting with one regression
    -   Run local regression for one dep
    -   Run local porjectionf for all deps, both shocks
-   Plotting
-   Economic interpretation (also available below)

## How to run and produce plots

With all required dependencies installed, run the Jupyter notebook from top to bottom. Note my FRED API key is hardcoded within (to fetch FRED data). Plots produced in Plotting section of notebook, with PNGs saved to Output.

## Economic Interpretation (TFP shocks and real GDP)

We see that positive TFP shocks are followed by increases in real per capita GDP under both Fernald and Ford measures. For the Fernald shocks (utilization adjusted), real GDP rises in a hump pattern, peaking around 7.5-10 quarters after the shock, and returning towards baseline. The Ford shocks produce a larger, more persistent increase to GDP, with peaks around 5 and 12.5 quarters post-shock. Overall, the figures support a positive relationship between TFP shocks and short/medium run effects to real GDP.

## Setup (using fresh Python install, uv for virtual env mgmt)

If have conda or packages already installed, can skip most setup cells.

```zsh
uv init
uv add jupyter ipykernel
source .venv/bin/activate
```
