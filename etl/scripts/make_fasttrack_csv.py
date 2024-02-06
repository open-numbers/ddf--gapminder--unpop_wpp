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

def read_datapoint(indicator):
    return pd.read_csv(osp.join('../../', f'ddf--datapoints--{indicator}--by--geo--time.csv'))

dfs = [read_datapoint(i).set_index(['geo', 'time']) for i in indicators]

df_all = pd.concat(dfs, axis=1)

concepts = pd.read_csv('../../../ddf--gapminder--systema_globalis/ddf--concepts.csv').set_index('concept')

concepts_all = concepts.loc[indicators]

concepts_all.to_csv('./fasttrack_concept.csv')

concept_map = concepts_all['name'].to_dict()

concept_map

df_all.columns = df_all.columns.map(concept_map)

df_all.to_csv('./fasttrack_data.csv')
