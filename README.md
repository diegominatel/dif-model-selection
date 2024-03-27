# Fairness-Aware Model Selection Using Differential Item Functioning

This repository is the official implementation of the paper entitled "Fairness-Aware Model Selection Using Differential Item Functioning". (ICMLA 2023)

## BibTeX Citation

If you use any part of this code in your research, please cite it using the following BibTex entry:

```latex
@inproceedings{minatel2023model,
  author={Minatel, Diego and Parmezan, Antonio R. S. and Cúri, Mariana and De Andrade Lopes, Alneu},
  booktitle={2023 International Conference on Machine Learning and Applications (ICMLA)}, 
  title={Fairness-Aware Model Selection Using Differential Item Functioning}, 
  year={2023},
  pages={1971-1978}
  doi={10.1109/ICMLA58977.2023.00298}
}
```

## Abstract

Differential Item Functioning~(DIF) is a powerful tool for developing fairer tests and mitigating bias in applicant selection tests. DIF aims to detect items in a test that favor or harm groups of people based on aspects such as gender, age, and race, which should be irrelevant to the assessment. Likewise, in machine learning, selecting a model from a pool of candidates is essential to identify the one that minimizes or eliminates discriminatory effects in its decision-making process. As far as we know, research into knowledge discovery through supervised machine learning has predominantly focused on including fairness notions at the lowest level of the pre-processing, pattern extraction, and post-processing phases. This fact evidences a need for studies on the impact of model selection on the development of impartial models. Herein, we present a novel approach to fairness-aware model selection to fill the mentioned gap. Our proposal introduces ABC, the first group fairness metric based on DIF concepts. We experimentally evaluated our approach against two model selection strategies by employing ten datasets, six classification algorithms, one performance measure, four group fairness measures, and one statistical significance test. According to the results, our proposal stands out for achieving a trade-off between improving the sense of justice and good classifier performance. Consequently, ABC is a promising metric for selecting fairer models with high predictive power.

## Full text of the paper

Access the full text of this paper at: https://ieeexplore.ieee.org/document/10459924
