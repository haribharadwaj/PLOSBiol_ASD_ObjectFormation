# Data files and plotting scripts for MEG study on auditory temporal-coherence processing in ASD


These files are associated with the manuscript titled "Cortical signatures of auditory object binding in children with Autism Spectrum Disorder are anomalous in concordance with behavior and diagnosis" submitted to PLOS Biology.


## Data files

The data needed to reproduce all the figures in the manuscripts are included in two directories: ```NeuralData```, and ```BrainBehaviorCorrelationsData```. Data are provided for each of the 47 participants (26 typically developing or TD children, and 21 children with autism spectrum disorder or ASD) individually.

The ```NeuralData``` directory contains six files, derived from magnetoencephalography (MEG) measurements and transformed to "source space" using structural information obtained using magnetic resonance imaging (MRI). Five of the six files contain phase-locked evoked responses (```ERPsummary_zscore_*.mat```) in the form of arrays of shape ```47 subjects x Number-of-time-points```. One file contains "induced" gamma-band activity measurements (```gammaFig3.mat```) as a 47-value array, one for each participant. Participants 1--26 form the TD group, and participants 27--47 form the ASD group.


The ```BrainBehaviorCorrelationsData``` directory contains summary MEG measures (evoked-response amplitudes in ```erp3.mat```, and gamma-band acitivity in ```gamma.mat```) for each participant, along with three behavioral measurements (```aud7q_raw.mat```, ```srs_sci```, and ```nepsy_ICCinh.mat```; please see the manuscript for information about the measures).  Participant ages are provided in ```age.mat```. All files include 47-value arrays, one for each participant.


Finally, data from the surrogate experiment conducted to validate the stimuli (needed to reproduce Supplementary Figure SI-5) is also included in the ```BrainBehaviorCorrelationsData```.


## Plotting scripts

Plotting scripts to generate the following main and supplementary figures are included: Fig 2A-B; Fig 3A-C; Fig 3E; Fig 4A-D; Fig SI-2 A-B; Fig SI-3A-B; Fig SI-4 A-B; Fig SI-6. They are either in Python on MATLAB format. The ```.m``` files were tested using MATLAB Version: 9.4.0.813654 (R2018a). The ```.py``` files were tested using Python 3.8.8. The filename for each script indicates the figure number that it corresponds to in the manuscript.

Please reach out to the manuscript authors with any questions about the data or the plotting scripts.
