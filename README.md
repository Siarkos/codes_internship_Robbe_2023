# codes_internship_Robbe_2023

README : 

AnalyzesGeneration_05.ipynd : Creat an HTML file containing informations about all the session of a mice to compare them easly. The HTML contain some analyses of the trajectories and a tool to see the behavior of the mouse.

AnalyzesGeneration_04.ipynd : outdated version of this analysis

ExploreExploit_FunctionReward_Sequence04.py : up to date version of the code of the acquisition code for the habitat protocol and linear_turns protocol. Can easly be modified to create a new function
                                              deciding according to which rule the animals get their rewards.

ExploreExploit_FunctionReward_Sequence02.py - ExploreExploit_FunctionReward_Sequence03.py : outdated versions of the acquisition code (can be used if you want to see how to implement that the animal
                                              must change patch to end exploration if necessary)

In_progress_video_processing_02.ipynb : creat a changed version of the video showing when the reward are given to the mice and indicating the types of turn

In_progress_video_processing.ipynb : outdated version of the video processing, does not detect the shift between the positions of the mice read in the file and the frame of the video

analysis_all_session.ipynb : agglomerate the data of all the sessions of the mice chosen to allow the user to work with the evolution of data across session and/or mice. Also contains some tools to 
                              help the user do so.

trajectories_analysis.ipynb : contains a lot of analysis for a single session, as well as some tools to investigate the best values for some transformation (like the cut-off speed or the sigma of the
                              smoothing)

modelling_reward.ipynb : contains an attemp to modelize the excepected number of reward in the linear_turn task. Only works for a slope of 1.

video_read.py : read a video by moving frame by frame

own_Functions.py : define some functions to be used by other files

median_thomas.py : define some functions to be used in other files
