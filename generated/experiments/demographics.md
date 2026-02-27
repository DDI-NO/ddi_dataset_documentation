## Overview
DDI base demographic data

# Demographic Data

This experiment captures demographic attributes and subject metadata.

## Variables

| ID | Label | Definition | Level | Domain | Type | Sensitivity |
| --- | --- | --- | --- | --- | --- | --- |
| SUBJ_GROUP | Subject group | TODO: Define semantic meaning. | visit | dem | text | none |
| SUBJ_GROUP_TEXT | Subject group text | Label representation derived from coded values. | visit | dem | categorical | none |
| NATION | Nation | TODO: Define semantic meaning. | visit | dem | text | none |
| NATION_OTHER | Nation Other | TODO: Define semantic meaning. | visit | dem | text | none |
| LANGUAGE | Language | TODO: Define semantic meaning. | visit | dem | numeric | none |
| LANGUAGE_OTHER | Language Other | TODO: Define semantic meaning. | visit | dem | numeric | none |
| RECRUIT | Recruitment | TODO: Define semantic meaning. | visit | dem | text | none |
| RECRUIT_TEXT | Recruitment Text | Label representation derived from coded values. | visit | dem | categorical | none |
| RECRUIT_OTHER | Recruit Other | TODO: Define semantic meaning. | visit | dem | text | none |
| EDU_YEARS | Education Years | TODO: Define semantic meaning. | visit | dem | numeric | none |
| EDU_LEVEL | Education Level | TODO: Define semantic meaning. | visit | dem | text | none |

### Subject group

- **ID**: SUBJ_GROUP
- **Label**: Subject group
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/subj_group
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Subject group, subject group, SUBJ_GROUP, subj_group
- **Sensitivity**: none
- **Derivation**: none
### Subject group text

- **ID**: SUBJ_GROUP_TEXT
- **Label**: Subject group text
- **Definition**: Label representation derived from coded values.
- **Source schema element**: dem:ddiDemographicData/subj_group
- **Semantics**: visit / dem / categorical
- **Allowed values**: Cognitive symptom group, Parkinsonism symptom group, Spouse control group, Ordinary control group, Orthopedic control group, Family history "control" group, Cognitive symptom - extension from previous study group, Neuropsychiatric symptoms group, Skogholts disease
- **Synonyms**: Subject group text, subject group text, SUBJ_GROUP_TEXT, subj_group_text
- **Sensitivity**: none
- **Derivation**: sql_case
### Nation

- **ID**: NATION
- **Label**: Nation
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/nation
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Nation, nation, NATION
- **Sensitivity**: none
- **Derivation**: none
### Nation Other

- **ID**: NATION_OTHER
- **Label**: Nation Other
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/nation_other
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Nation Other, nation other, NATION_OTHER, nation_other
- **Sensitivity**: none
- **Derivation**: none
### Language

- **ID**: LANGUAGE
- **Label**: Language
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/language
- **Semantics**: visit / dem / numeric
- **Allowed values**: -
- **Synonyms**: Language, language, LANGUAGE
- **Sensitivity**: none
- **Derivation**: none
### Language Other

- **ID**: LANGUAGE_OTHER
- **Label**: Language Other
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/language_other
- **Semantics**: visit / dem / numeric
- **Allowed values**: -
- **Synonyms**: Language Other, language other, LANGUAGE_OTHER, language_other
- **Sensitivity**: none
- **Derivation**: none
### Recruitment

- **ID**: RECRUIT
- **Label**: Recruitment
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/recruit
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Recruitment, recruitment, RECRUIT, recruit
- **Sensitivity**: none
- **Derivation**: none
### Recruitment Text

- **ID**: RECRUIT_TEXT
- **Label**: Recruitment Text
- **Definition**: Label representation derived from coded values.
- **Source schema element**: dem:ddiDemographicData/recruit
- **Semantics**: visit / dem / categorical
- **Allowed values**: Advertisement, Referral to memory clinic, Continuation from another study, Cohabitant/spouse, Other
- **Synonyms**: Recruitment Text, recruitment text, RECRUIT_TEXT, recruit_text
- **Sensitivity**: none
- **Derivation**: sql_case
### Recruit Other

- **ID**: RECRUIT_OTHER
- **Label**: Recruit Other
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/recruit_other
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Recruit Other, recruit other, RECRUIT_OTHER, recruit_other
- **Sensitivity**: none
- **Derivation**: none
### Education Years

- **ID**: EDU_YEARS
- **Label**: Education Years
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/edu_years
- **Semantics**: visit / dem / numeric
- **Allowed values**: -
- **Synonyms**: Education Years, education years, EDU_YEARS, edu_years
- **Sensitivity**: none
- **Derivation**: none
### Education Level

- **ID**: EDU_LEVEL
- **Label**: Education Level
- **Definition**: TODO: Define semantic meaning.
- **Source schema element**: dem:ddiDemographicData/edu_level
- **Semantics**: visit / dem / text
- **Allowed values**: -
- **Synonyms**: Education Level, education level, EDU_LEVEL, edu_level
- **Sensitivity**: none
- **Derivation**: none

