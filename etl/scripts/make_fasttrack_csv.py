"""A script to generate fasttrack csv from this repo."""

import os.path as osp
import pandas as pd

indicators = [
    "population_aged_0_4_years_both_sexes_percent",
    "population_aged_0_4_years_female_percent",
    "population_aged_0_4_years_male_percent",
    "population_aged_0_4_years_total_number",
    "population_aged_0_14_years_both_sexes_percent",
    "population_aged_0_14_years_female_percent",
    "population_aged_0_14_years_male_percent",
    "population_aged_0_14_years_total_number",
    "population_aged_10_14_years_both_sexes_percent",
    "population_aged_10_14_years_female_percent",
    "population_aged_10_14_years_male_percent",
    "population_aged_10_14_years_total_number",
    "population_aged_15_19_years_both_sexes_percent",
    "population_aged_15_19_years_female_percent",
    "population_aged_15_19_years_male_percent",
    "population_aged_15_19_years_total_number",
    "population_aged_20_39_years_both_sexes_percent",
    "population_aged_20_39_years_female_percent",
    "population_aged_20_39_years_male_percent",
    "population_aged_20_39_years_total_number",
    "population_aged_40_59_years_both_sexes_percent",
    "population_aged_40_59_years_female_percent",
    "population_aged_40_59_years_male_percent",
    "population_aged_40_59_years_total_number",
    "population_aged_5_9_years_both_sexes_percent",
    "population_aged_5_9_years_female_percent",
    "population_aged_5_9_years_male_percent",
    "population_aged_5_9_years_total_number",
    "population_aged_60plus_years_both_sexes_percent",
    "population_aged_60plus_years_female_percent",
    "population_aged_60plus_years_male_percent",
    "population_aged_60plus_years_total_number",
    "population_aged_65plus_years_both_sexes_percent",
    "population_aged_65plus_years_female_percent",
    "population_aged_65plus_years_male_percent",
    "population_aged_65plus_years_total_number",
    "population_aged_70plus_years_both_sexes_percent",
    "population_aged_70plus_years_female_percent",
    "population_aged_70plus_years_male_percent",
    "population_aged_70plus_years_total_number"
]

def read_datapoint(indicator, geo):
    return pd.read_csv(osp.join('../../', f'ddf--datapoints--{indicator}--by--{geo}--time.csv'))

dfs_geo = [read_datapoint(i, 'geo').set_index(['geo', 'time']) for i in indicators]

df_all_geo = pd.concat(dfs_geo, axis=1)

dfs_global = [read_datapoint(i, 'global').set_index(['global', 'time']) for i in indicators]

df_all_global = pd.concat(dfs_global, axis=1)

concepts = pd.read_csv('../../../ddf--gapminder--systema_globalis/ddf--concepts.csv').set_index('concept')

concepts_all = concepts.loc[indicators]

concepts_all.to_csv('./fasttrack_concept.csv')

concept_map = concepts_all['name'].to_dict()

concept_map

df_all_geo.columns = df_all_geo.columns.map(concept_map)

df_all_geo.to_csv('./fasttrack_data_geo.csv')

df_all_global.columns = df_all_global.columns.map(concept_map)

df_all_global.to_csv('./fasttrack_data_global.csv')
