# Emotion Go/No-Go task

This is code for an emotional Go/No Go task using the IAPS pictures. There are a total of 230 negative valence images and 230 neutral images in the critical stimulus set. The negative imageshave an average valence rating of 2.79 and arousal rating of 5.46. The neutral images have an average valence rating of 5.94 and an average arousal rating of 4.19. Each trial in this experiment is trial unique (i.e., no images are repeated across trials). 

The task is a go/no-go task whereby participants are instructed to respond to a standard (or go) stimulus and to withhold responding to a rare (or no-go) stimulus. There are two blocks of this task, where in each block there are 184 go trials and 46 no-go trials to build up the prepotent response (this is an 80%/20% go to no-go ratio. In neutral go block, participants are instructed to make a button press with the right index finger for neutral images and to withhold responses to negative valenced images. In the negative block, negative images are the go trials and neutral images are the negative trials. Responses should be made with the participants dominant hand. 

Each image is presented for 500 ms with an average stimulus-onset-asynchrony of 2000 ms (range is 1500-2500). The SOA is randomly determined on each trial in intervals of the frame rate. 

The stimuli are randomly generated anew for each participant, and these are written to the top directory in the main folder with the .psyexp file. This is in the CSV format and is 'archived' at the end of the experiment using the participant id.

Each block is padded by 20 seconds of a fixation cross at the beginning and end of a block. No fixation cross on the screen while an image is shown. A break is given halfway through each block (corresponding to 115 trials per period). Trials are presented in a random fashion with no constraints.

The practice phase is comprised of a short list of trials (20) for each of the two blocks, with images taken from the NARPS database. These images had similar characteristics to those from the IAPS. 

This task is programmed in PsychoPy Builder (Pierce et al., 2019). 


## References

Lang, P.J., Bradley, M.M., & Cuthbert, B.N. (2008). International affective picture system (IAPS): Affective ratings of pictures and instruction manual. Technical Report A-8. University of Florida, Gainesville, FL.

Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv, J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-01193-y
