# Emotion Go/No-Go task

This is code for an emotional Go/No Go experiment using the IAPS pictures (Lang et al., 2008). There are a total of 230 negative valence images and 230 neutral images in the critical stimulus set. The information on the range, mean, and standard deviation of the valence and arousal ratings for each stimulus are in the table at the end of this document. 

The task is a go/no-go task whereby participants are instructed to respond to a standard (or go) stimulus and to withhold responding to a rare (or no-go) stimulus. There are two blocks of this task, where in each block there are 184 go trials and 46 no-go trials to build up the prepotent response (this is an 80%/20% go to no-go ratio. In neutral go block, participants are instructed to make a button press with the right index finger for neutral images and to withhold responses to negative valenced images. In the negative block, negative images are the go trials and neutral images are the negative trials. Responses should be made with the participants dominant hand. 

Each image is presented for 500 ms with an average stimulus-onset-asynchrony of 2000 ms (range is 1500-2500). The SOA is randomly determined on each trial in intervals of the frame rate. 

The stimuli are randomly generated anew for each participant, and these are written to the top directory in the main folder with the .psyexp file. This is in the CSV format and is 'archived' at the end of the experiment using the participant id.

Each block is padded by 20 seconds of a fixation cross at the beginning and end of a block. No fixation cross on the screen while an image is shown. A break is given halfway through each block (corresponding to 115 trials per period). Trials are presented in a random fashion with no constraints.

The practice phase is comprised of a short list of trials (20) for each of the two blocks, with images taken from the NAPS database (Marchewka). These images had similar characteristics to those from the IAPS. 

This task is programmed in PsychoPy Builder (Pierce et al., 2019). 

## Adding images

Note that this program does not come with the images that were used. To run the study, download the IAPS and NAPS database. Copy the IAPS images into a directory called **images** and the NAPS images into a directory called **prac_images**. The trials used in this task are defined in the iaps_stimuli.csv and the two *_prac.csv files. 

## References

Lang, P.J., Bradley, M.M., & Cuthbert, B.N. (2008). International affective picture system (IAPS): Affective ratings of pictures and instruction manual. Technical Report A-8. University of Florida, Gainesville, FL.

Marchewka, A., Żurawski, Ł., Jednoróg, K., & Grabowska, A. (2014). The Nencki Affective Picture System (NAPS): Introduction to a novel, standardized, wide-range, high-quality, realistic picture database. Behavior Research Methods, 46(2), 596–610. https://doi.org/10/f6c44q

Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv, J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-01193-y

Riegel, M., Żurawski, Ł., Wierzba, M., Moslehi, A., Klocek, Ł., Horvat, M., Grabowska, A., Michałowski, J., Jednoróg, K., & Marchewka, A. (2016). Characterization of the Nencki Affective Picture System by discrete emotional categories (NAPS BE). Behavior Research Methods, 48(2), 600–612. https://doi.org/10/gf5sm4

<br> 

##### Table 1. Valence and arousal ratings for the negative IAPS stimuli used for the critical trials in this experiment.

|           | Valence Mean | Valence SD  | Arousal Mean | Arousal SD  | 
| --------- | ------------ | ----------- | ------------ | ----------- |
| Mean (SD) | 2.79 (0.59)  | 1.59 (0.25) | 5.55 (0.83)  | 2.18 (0.18) |
| Range     | 1.46 - 3.73  | 1.01 - 2.38 | 3.46 - 7.35  | 1.66 - 2.70 |
				
<br>

##### Table 2.  Valence and arousal ratings for the neutral IAPS stimuli used for the critical trials in this experiment.

|           | Valence Mean | Valence SD  | Arousal Mean | Arousal SD  |
| --------- | ------------ | ----------- | ------------ | ----------- |
| Mean (SD) | 5.95 (0.58)  | 1.56 (0.29) | 4.20 (0.93)  | 2.11 (0.20) |
| Range     | 5.00 - 6.97  | 0.60 - 2.50 | 2.00 - 6.97  | 1.62 - 2.86 | 

<br>

##### Table 3.  Valence and arousal ratings for the negative NAPS stimuli used for the critical trials in this experiment.

|           | Valence Mean | Valence SD  | Arousal Mean | Arousal SD  |
| --------- | ------------ | ----------- | ------------ | ----------- |
| Mean (SD) | 2.95 (0.59)  | 1.36 (0.23) | 4.38 (0.86)  | 2.18 (0.16) |
| Range     | 1.92 - 3.73  | 1.02 - 1.82 | 3.55 - 6.33  | 1.85 - 2.45 | 
				
<br>

##### Table 4. Valence and arousal ratings for the neutral NAPS stimuli used for the critical trials in this experiment.

|           | Valence Mean | Valence SD  | Arousal Mean | Arousal SD  |
| --------- | ------------ | ----------- | ------------ | ----------- |
| Mean (SD) | 1.26 (0.23)  | 2.85 (0.57) | 1.80 (0.34)  | 1.80 (0.34) | 
| Range     | 5.08 - 6.92  | 0.79 - 1.64 | 2.02 - 4.49  | 1.21 - 2.68 |