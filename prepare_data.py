import pandas as pd

URL = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"

COUNTRIES = ["Germany", "France", "Denmark", "Poland", "Spain",
             "United Kingdom", "Italy", "Netherlands"]

COLUMNS = ["country", "year", "population", "electricity_generation",
           "electricity_demand", "net_elec_imports", "per_capita_electricity",
           "carbon_intensity_elec", "renewables_share_elec", "fossil_share_elec",
           "coal_share_elec", "gas_share_elec", "oil_share_elec",
           "nuclear_share_elec", "hydro_share_elec", "wind_share_elec",
           "solar_share_elec", "biofuel_share_elec",
           "other_renewables_share_elec_exc_biofuel"]

df = pd.read_csv(URL)
df = df[df["country"].isin(COUNTRIES) & (df["year"] >= 2000)][COLUMNS]
df.to_csv("data/owid_energy_selected.csv", index=False)
print(df.shape)
