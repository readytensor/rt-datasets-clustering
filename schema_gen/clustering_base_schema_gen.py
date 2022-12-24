import numpy as np, pandas as pd
import os, sys
from sympy import pretty
import yaml, json
import pprint
from pathlib import Path


model_category = "clustering_base"
version = "1.0"


def get_schema_config():
    with open("config.yaml", "r") as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as exc:
            print(exc)


def gen_clustering_base_schemas(schema_cfg, root_path):

    model_category_config = schema_cfg["model_categories"][model_category]
    # print(model_category_config); sys.exit()

    data_types = model_category_config["data_types"]
    field_use_types = model_category_config["field_use_types"]
    field_name_lbl = model_category_config["schemaFields"]["fieldName"]
    data_type_lbl = model_category_config["schemaFields"]["dataType"]
    use_type_lbl = model_category_config["schemaFields"]["fieldUseType"]

    # print(data_types); exit()

    datasets = model_category_config["datasets"]

    for dataset in datasets:

        print(f"Generating schema for model_cat: {model_category}  dataset: {dataset}")
        # initiate the schema dict
        schema_dict = {}
        schema_dict["problemCategory"] = model_category
        schema_dict["version"] = version
        schema_dict["inputDatasets"] = {
            "clusteringBaseMainInput": {"idField": "", "inputFields": []}
        }
        schema_dict["datasetSpecs"] = {
            "suggestedNumClusters": int(datasets[dataset]["numClusters"])
        }
        # pretty_print(model_category_config["datasets"][dataset]); sys.exit()

        schema_dirpath = os.path.join(root_path, "datasets", dataset, "schema_cfg")
        input_fpath = os.path.join(schema_dirpath, datasets[dataset]["fname"])
        schema_params = pd.read_csv(input_fpath)

        output_fpath = os.path.join(
            root_path,
            "datasets",
            dataset,
            "processed",
            f"{dataset}_schema.json",
        )

        input_dict = schema_dict["inputDatasets"]["clusteringBaseMainInput"]

        id_attr = None

        # iterate through the fields in the input file
        for _, row in schema_params.iterrows():

            # print(row) ; sys.exit()

            if row[use_type_lbl] == field_use_types["id"]:
                if id_attr is not None:
                    raise Exception(
                        f"Error: Only 1 id row is permissible. Can't set field '{row[field_name_lbl]}' as {row[use_type_lbl]}"
                    )
                id_attr = row[field_name_lbl]
                input_dict["idField"] = id_attr

            elif row[use_type_lbl] == field_use_types["input"]:
                attribute = {}
                attribute["fieldName"] = row[field_name_lbl]

                if (
                    row[data_type_lbl] == data_types["categorical"]
                    or row[data_type_lbl] == data_types["string"]
                    or row[data_type_lbl] == data_types["numeric"]
                ):

                    # attribute['dataType'] = row[data_type_lbl]
                    input_dict["inputFields"].append(attribute)
                else:
                    raise Exception(f"What data type is this: {row[data_type_lbl]}")

            else:
                raise Exception(f"What use type is this: {row[use_type_lbl]}")

        # pprint.pprint(schema_dict)
        with open(output_fpath, "w") as f:
            json.dump(schema_dict, f, indent=2)


if __name__ == "__main__":

    root_path = f"./../"

    schema_cfg = get_schema_config()

    gen_clustering_base_schemas(schema_cfg, root_path)
