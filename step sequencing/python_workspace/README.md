# Generating a sample-steps.txt file

It is pretty straight forward for Chris to make a google sheet of cue numbers, measure numbers, timestamps, (MM:SS.SSS) and instructions for what files to play when. This script takes in a CSV file (which can be downloaded from google docs) and outputs a sample-steps.txt file with timestamps in totalMilis, and reset-seek data baked in.

Example google sheet [here](https://docs.google.com/spreadsheets/d/17-FvIYuNMxmJuJlqtZbwRWJIw8Gkfkmd7-DORgU26tw/edit?usp=sharing).

The coloums are:
1. **Movement number**. This column is ignored by the script, and is just for human use only as a header
2. **Step number**. This is used for the cue number by the patch. This should just be in order counting up, starting at 1.
3. **Timecode**. This is the timestamp pulled from logic or any DAW with the format MM:SS.MMM.
4. **Measure**. Measure in the score. This is also ignored in the python code.
5. **Use Reset Seek**. If there is anything in this column, it trigger the reset seek code to match up with the new files that are being played.

## To run the script:
1. download the google sheet as a CSV file and put it in your working directory.
1. change the file names to match the files / paths present 
```
input_file = 'hub.csv'
output_file = 'sample-steps.txt'
```
2. open terminal and cd to the correct directory
```
cd path/to/folder/python_workspace
```
and then run:
```
python3 genSampleSteps.py
```
upon successful completion it will display:
```
Output written to sample-steps.txt
```

This will create a new file that looks like this one [here](https://github.com/kitchWWW/chris_cerrone_tools/blob/adding_python/step%20sequencing/python_workspace/sample-steps.txt).

This generated .txt file is still missing all **file names** and **fade information**. This must be input by hand, but is significantly easier than doing all of the math to notate all of the reset seeks.