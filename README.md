# Datasets for Clustering Base category on Ready Tensor

This repo contains all files related to the datasets used in algorithm evaluation for the Clustering - Base category.

The `datasets` folder contains the main data files and the schema files for all the benchmark datasets under Clustering - Base category. Within each dataset folder in `datasets`:

- The `raw` folder contains the original data files from the source (see attributions below).
- `processed` folder contains the processed files. These files are used in algorithm evaluations.
  - The CSV file naming convention "<dataset_name>.csv" is the main data used for the clustering analysis.
  - "\_test_key.csv" contains the known targets for the data. These targets are used for extrinsic validation using metrics such as purity and adjusted mutual information.
  - The JSON file with suffix "\_schema.json" is the schema file for the corresponding dataset.
- The Jupyter notebook file within each dataset folder is used to convert the raw data file(s) in `raw` folder into the processed form in `processed` folder.
- The folder `schema_cfg` contains a csv which is needed by the schema generation script (described below) .

`schema_gen` folder contains a schema gen config file (YAML) and a python script which are used to generate the JSON schema files stored in the `processed` folder for each dataset. The generated schema file conforms to the Ready Tensor specification for this category.

---

The following is the list of datasets along with a brief description for each and its attribution:

---

## Concentric Circles

#### Alias (in scorecards): concentric_circles

#### Domain / Industry: None (synthetic data) 

#### Description

This dataset is synthetically generated. Two clusters are created which are concentric circles (bands) with some Gaussian noise. The goal is to present data with non-Gaussian clusters.

#### Dataset characteristics

- Number of samples = 3,000
- Number of input features = 2
- Number of known clusters = 2

#### Attribution

Synthetically generated data

---

## Gesture Phase Segmentation

#### Alias (in scorecards): gesture_phase2

#### Domain / Industry: Biomechanics / Biosciences

#### Description

Dataset consists of features extracted from 7 videos with people gesticulating, aiming at studying Gesture Phase Segmentation. Features define the velocity and acceleration of hands and wrists. The gestures are classified into one of 5 categories: D (rest position, from portuguese “descanso”), P (preparation), S (stroke), H (hold), R (retraction).

#### Dataset characteristics

- Number of samples = 9,900
- Number of input features = 32
- Number of known clusters = 5

#### Attribution

Original source of data (multiple papers):

Madeo, R. C. B. ; Lima, C. A. M. ; PERES, S. M. . Gesture Unit Segmentation using Support Vector Machines: Segmenting Gestures from Rest Positions. In: Symposium on Applied Computing (SAC), 2013, Coimbra. Proceedings of the 28th Annual
ACM Symposium on Applied Computing (SAC), 2013. p. 46-52.

Wagner, P. K. ; PERES, S. M. ; Madeo, R. C. B. ; Lima, C. A. M. ; Freitas, F. A. . Gesture Unit Segmentation Using Spatial-Temporal Information and Machine Learning. In: 27th Florida Artificial Intelligence Research Society Conference (FLAIRS), 2014, Pensacola Beach. Proceedings of the 27th Florida Artificial Intelligence Research Society Conference (FLAIRS). Palo Alto : The AAAI Press, 2014. p. 101-106.

Creators: Renata Cristina Barros Madeo (Madeo, R. C. B.) Priscilla Koch Wagner (Wagner, P. K.) Sarajane Marques Peres (Peres, S. M.) {renata.si, priscilla.wagner, sarajane} at -A Home 04-06-2020 Dr. Sarajane M. Peres

Dataset can be found here:
https://archive.ics.uci.edu/ml/datasets/gesture+phase+segmentation#

UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---

##

#### Alias (in scorecards):

#### Domain / Industry:

#### Description

#### Dataset characteristics

- Number of samples =
- Number of input features =
- Number of known clusters =

#### Attribution

---
