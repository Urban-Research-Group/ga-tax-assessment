import polars as pl
from pipeline import DataFormat

fulton = DataFormat(
    data_name="fulton_parcel",
    files_path=r"../data/fulton/parcels",
    separator=None,
    column_names={
        "Taxyr": ["tax_year"],
        "Parid": "parcel_id",
        "Cityname": "site_city",
        "Situs Adrno": "site_addrno",
        "Situs Adrdir": "site_addrdir",
        "Situs Adrstr": "site_addrstr",
        "Situs Adrsuf": "site_addrsuf",
        "Situs Adrsuf2": "site_addrsuf2",
        "Class": "site_class_parcel",
        "Luc": "site_luc_parcel",
        "Taxdist": "tax_district",
        "Own1": "owner_name_1",
        "Own2": "owner_name_2",
        "owner_zip": "Zip1",
        "Owner Adrno": "owner_addrno",
        "Owner Adradd": "owner_addradd",
        "Owner Adrdir": "owner_addrdir",
        "Owner Adrstr": "owner_addrstr",
        "Owner Adrsuf": "owner_addrsuf",
        "Cityname.1": "owner_city",
        "Statecode": "owner_state",
        "Country": "owner_country",
        "Unitno": "owner_unitno",
        "Reascd": "reas_code",
        "Rev_code": "rev_code",
        "Aprtot": "appr_total",
        "Aprland": "appr_land",
        "Apprbldg": "appr_build",
        "Exmppct": "excempt_pct",
        "Exmpval": "excempt_val",
        "D Yrblt": "year_built",
        "D Effyr": "year_eff",
        "D Yrremod": "year_remodel",
        "D Grade": "grade",
        "Livunit": "num_units",
    },
    new_col_dtypes={
        "taxyr": pl.Utf8,
        ""
    },
    append_files=[""],
    merge_files=[""],
    merge_key=["col"],
    pipes=[""],
    out_file="all_parcels",
)
