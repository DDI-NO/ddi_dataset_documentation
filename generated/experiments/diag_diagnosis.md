## Overview
CRF Part IV: Includes Diagnosis staging and etiology

# Diagnosis Data

This experiment captures diagnosis assessments per visit.

## Variables

| ID | Label | Definition | Level | Domain | Type | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| LABEL | Label | TODO: Define semantic meaning. | visit | diag | text | none |
| DATE | Date | TODO: Define semantic meaning. | visit | diag | date | none |
| AGE | Age | TODO: Define semantic meaning. | visit | diag | numeric | none |
| scd_symptoms | SCD symptoms | TODO: Define semantic meaning. | visit | diag | text | none |
| STAG | Staging | TODO: Define semantic meaning. | visit | diag | text | none |
| STAG_TEXT | Staging text | Label representation derived from coded values. | visit | diag | categorical | none |
| STAG_WITH_CRITERIA | Staging | TODO: Define semantic meaning. | visit | diag | text | none |
| STAG_WITH_CRITERIA_TEXT | Staging text | Label representation derived from coded values. | visit | diag | categorical | none |
| STAG_OTHER_DEF | Other definition for staging | TODO: Define semantic meaning. | visit | diag | text | none |
| DIAG_DATE | Date of diagnosis | TODO: Define semantic meaning. | visit | diag | date | none |
| DIAG_AGE | Age at diagnosis | TODO: Define semantic meaning. | visit | diag | numeric | none |
| DIAG | Diagnosis | TODO: Define semantic meaning. | visit | diag | text | none |
| DIAG_OTHER_DEF | Diagnosis other definition | TODO: Define semantic meaning. | visit | diag | text | none |
| DIAG_PARK | Diagnosis of Parkinson's disease | TODO: Define semantic meaning. | visit | diag | text | none |
| DIAG_PARK_YEARS | Parkinson's diagnosis year | TODO: Define semantic meaning. | visit | diag | numeric | none |

### Label

- **ID**: LABEL
- **Label**: Label
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData.ID
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Label, label, LABEL
- **Sensitivity**: none
- **Derivation**: sql
### Date

- **ID**: DATE
- **Label**: Date
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData.date
- **Semantics**: visit / diag / date
- **Allowed values**: -
- **Synonyms**: Date, date, DATE
- **Sensitivity**: none
- **Derivation**: none
### Age

- **ID**: AGE
- **Label**: Age
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData.date
- **Semantics**: visit / diag / numeric
- **Allowed values**: -
- **Synonyms**: Age, age, AGE
- **Sensitivity**: none
- **Derivation**: sql
### SCD symptoms

- **ID**: scd_symptoms
- **Label**: SCD symptoms
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/scd_symptoms
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: SCD symptoms, scd symptoms, scd_symptoms
- **Sensitivity**: none
- **Derivation**: none
### Staging

- **ID**: STAG
- **Label**: Staging
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/stag
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Staging, staging, STAG, stag
- **Sensitivity**: none
- **Derivation**: none
### Staging text

- **ID**: STAG_TEXT
- **Label**: Staging text
- **Definition**: Label representation derived from coded values.
- **Source schema element**: diag:DiagnosisData/stag
- **Semantics**: visit / diag / categorical
- **Allowed values**: CN, NN, SCD, MCI, Dementia
- **Synonyms**: Staging text, staging text, STAG_TEXT, stag_text
- **Sensitivity**: none
- **Derivation**: sql_case
### Staging

- **ID**: STAG_WITH_CRITERIA
- **Label**: Staging
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/stag_with_criteria
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Staging, staging, STAG_WITH_CRITERIA, stag_with_criteria
- **Sensitivity**: none
- **Derivation**: none
### Staging text

- **ID**: STAG_WITH_CRITERIA_TEXT
- **Label**: Staging text
- **Definition**: Label representation derived from coded values.
- **Source schema element**: diag:DiagnosisData/stag_with_criteria
- **Semantics**: visit / diag / categorical
- **Allowed values**: NC, NCFD, NC-NN, SCD, SCD-Other, MCI, MCI-Other, Dementia, NCFD-NN, PD-N, PD-NN
- **Synonyms**: Staging text, staging text, STAG_WITH_CRITERIA_TEXT, stag_with_criteria_text
- **Sensitivity**: none
- **Derivation**: sql_case
### Other definition for staging

- **ID**: STAG_OTHER_DEF
- **Label**: Other definition for staging
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/stag_other_def
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Other definition for staging, other definition for staging, STAG_OTHER_DEF, stag_other_def
- **Sensitivity**: none
- **Derivation**: none
### Date of diagnosis

- **ID**: DIAG_DATE
- **Label**: Date of diagnosis
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag_date
- **Semantics**: visit / diag / date
- **Allowed values**: -
- **Synonyms**: Date of diagnosis, date of diagnosis, DIAG_DATE, diag_date
- **Sensitivity**: none
- **Derivation**: none
### Age at diagnosis

- **ID**: DIAG_AGE
- **Label**: Age at diagnosis
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag_age
- **Semantics**: visit / diag / numeric
- **Allowed values**: -
- **Synonyms**: Age at diagnosis, age at diagnosis, DIAG_AGE, diag_age
- **Sensitivity**: none
- **Derivation**: none
### Diagnosis

- **ID**: DIAG
- **Label**: Diagnosis
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Diagnosis, diagnosis, DIAG, diag
- **Sensitivity**: none
- **Derivation**: none
### Diagnosis other definition

- **ID**: DIAG_OTHER_DEF
- **Label**: Diagnosis other definition
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag_other_def
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Diagnosis other definition, diagnosis other definition, DIAG_OTHER_DEF, diag_other_def
- **Sensitivity**: none
- **Derivation**: none
### Diagnosis of Parkinson's disease

- **ID**: DIAG_PARK
- **Label**: Diagnosis of Parkinson's disease
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag_park
- **Semantics**: visit / diag / text
- **Allowed values**: -
- **Synonyms**: Diagnosis of Parkinson's disease, diagnosis of parkinson's disease, DIAG_PARK, diag_park
- **Sensitivity**: none
- **Derivation**: none
### Parkinson's diagnosis year

- **ID**: DIAG_PARK_YEARS
- **Label**: Parkinson's diagnosis year
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: diag:DiagnosisData/diag_park_years
- **Semantics**: visit / diag / numeric
- **Allowed values**: -
- **Synonyms**: Parkinson's diagnosis year, parkinson's diagnosis year, DIAG_PARK_YEARS, diag_park_years
- **Sensitivity**: none
- **Derivation**: none

