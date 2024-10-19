# step sequencing 

the current step.txt format is:

`[ms for auto, 0 for manual] [filename without extension] [0-1 start/stop] [fadetime in ms]`

"auto" means a step that will auto play the next one after a set time.

"manual" means it will require cue/step input to progress.

NOTE: the auto time must always be put in the preceding step

e.g. if step 3 is to be played 2000ms after step 2, your steps would look like this:
```
1, 0 1 1 0;
2, 2000 2 1 0;
3, 0 3 1 0;
```

any effects will need their own format as needed, but generally they go:

`[input channel] [0-1 enable/disable] [any additional control steps]`


<img src="imgs/sample-playback.png" width="500" />
