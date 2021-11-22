# iamsMediapipe Action Recogntion Built on Mediapipe
https://user-images.githubusercontent.com/73752977/142786709-4adbadb4-13c9-4c0e-bf2f-0b309074346c.mp4


#### Step 1 : Install Pycharm
- Head over Pycharm Website and Install Pycharm. I use the Community or Edu edition.




- Create a new Pycharm project

- for convienience I am using Python 3.8+ 

#### Clone repository and Install requirements 
- Open Pycharm Terminal and type 
- create a new project
- clone this repository 
```bash
git clone https://github.com/exponentialR/iamsMediapipe.git
```
- Install requirements
```bash
run requirements.txt
```

#### Prepare Data Folder
- Open Pycharm terminal and go into the cloned repository 
```bash 
cd data 
```
Below you can define the following the type of actions you are collecting data for. In this case I am collecting data for OK NO WAVING CLAPPING and SALUTE
The Subfolder argument takes an integer and automatically creates 30 subfolders for each actions.
The --pat argument is the parent name of the data folder.
The --video_length takes an integer value. It is the length of the seqeunce each actions will be running for.

```
 C:\PycharmProjects\iamsMediapipe\data> python create_dir.py --actions OK NO WAVING CLAPPING SALUT
E --subfolder_numbers 30 --pat actionData --video_length 60
```
If you have everything set up correctly you should have the followingas depicted in the screenshot.
![image](https://user-images.githubusercontent.com/73752977/142783752-a922de1f-790f-409c-8480-21ab3ceda92f.png)

#### Data Collection
There are 4 Options for data collection as provided in the code.
- Collecting hand data only 
- Collecting face data only 
- Collecting pose data only ```collect_data_pose
- Collecting all hand, pose, facial data only.



