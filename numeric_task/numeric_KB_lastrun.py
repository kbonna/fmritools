#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Wed 10 Oct 2018 04:20:40 PM CEST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'numeric_KB'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/connectomics/Desktop/NeuroSci/Projects/GG/task/numeric_KB.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "setup"
setupClock = core.Clock()
#--- variables
N_block = 4
N_seq = 12

#--- create rows to iterate & shuffle
bOrder = []
for i in range(N_block):
    bOrder.append(slice(i*N_seq,(i+1)*N_seq))
bControl = bOrder[:]
shuffle(bOrder)
shuffle(bControl)
digitSize = 0.1
digitPosL = [-0.15, 0]
digitPosR = [0.15, 0]

ibiDuration = 5
i = 0

# Initialize components for Routine "infoOrder"
infoOrderClock = core.Clock()
informationOrder = visual.TextStim(win=win, name='informationOrder',
    text=u'order condition',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
counterOrder = visual.TextStim(win=win, name='counterOrder',
    text='default text',
    font=u'Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "isiCross"
isiCrossClock = core.Clock()

fixation = visual.TextStim(win=win, name='fixation',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trialOrder"
trialOrderClock = core.Clock()
digitCenterOrder = visual.TextStim(win=win, name='digitCenterOrder',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
digitRightOrder = visual.TextStim(win=win, name='digitRightOrder',
    text='default text',
    font=u'Arial',
    pos=digitPosR, height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
digitLeftOrder = visual.TextStim(win=win, name='digitLeftOrder',
    text='default text',
    font=u'Arial',
    pos=digitPosL, height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);



# Initialize components for Routine "feedbackOrder"
feedbackOrderClock = core.Clock()

textFeedbackOrder = visual.TextStim(win=win, name='textFeedbackOrder',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ibiSun"
ibiSunClock = core.Clock()
sun = visual.ImageStim(
    win=win, name='sun',
    image=u'smiley.png', mask=None,
    ori=0, pos=(0, 0), size=(0.27, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "infoControl"
infoControlClock = core.Clock()
informationControl = visual.TextStim(win=win, name='informationControl',
    text=u'control condition',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
counterControl = visual.TextStim(win=win, name='counterControl',
    text='default text',
    font=u'Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "isiCross"
isiCrossClock = core.Clock()

fixation = visual.TextStim(win=win, name='fixation',
    text=u'+',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trialControl"
trialControlClock = core.Clock()
digitCenterControl = visual.TextStim(win=win, name='digitCenterControl',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);
digitRightControl = visual.TextStim(win=win, name='digitRightControl',
    text='default text',
    font=u'Arial',
    pos=digitPosR, height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);
digitLeftControl = visual.TextStim(win=win, name='digitLeftControl',
    text='default text',
    font=u'Arial',
    pos=digitPosL, height=digitSize, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0);



# Initialize components for Routine "feedbackControl"
feedbackControlClock = core.Clock()

textFeedbackControl = visual.TextStim(win=win, name='textFeedbackControl',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ibiSun"
ibiSunClock = core.Clock()
sun = visual.ImageStim(
    win=win, name='sun',
    image=u'smiley.png', mask=None,
    ori=0, pos=(0, 0), size=(0.27, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "incrementCounter"
incrementCounterClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
t = 0
setupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat



# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=N_block, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # ------Prepare to start Routine "infoOrder"-------
    t = 0
    infoOrderClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    counterOrder.setText(i)
    # keep track of which components have finished
    infoOrderComponents = [informationOrder, counterOrder]
    for thisComponent in infoOrderComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "infoOrder"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = infoOrderClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *informationOrder* updates
        if t >= 0.0 and informationOrder.status == NOT_STARTED:
            # keep track of start time/frame for later
            informationOrder.tStart = t
            informationOrder.frameNStart = frameN  # exact frame index
            informationOrder.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if informationOrder.status == STARTED and t >= frameRemains:
            informationOrder.setAutoDraw(False)
        
        # *counterOrder* updates
        if t >= 0.0 and counterOrder.status == NOT_STARTED:
            # keep track of start time/frame for later
            counterOrder.tStart = t
            counterOrder.frameNStart = frameN  # exact frame index
            counterOrder.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if counterOrder.status == STARTED and t >= frameRemains:
            counterOrder.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in infoOrderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "infoOrder"-------
    for thisComponent in infoOrderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trialsOrder = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'stimuli.xlsx', selection=bOrder[i]),
        seed=None, name='trialsOrder')
    thisExp.addLoop(trialsOrder)  # add the loop to the experiment
    thisTrialsOrder = trialsOrder.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsOrder.rgb)
    if thisTrialsOrder != None:
        for paramName in thisTrialsOrder.keys():
            exec(paramName + '= thisTrialsOrder.' + paramName)
    
    for thisTrialsOrder in trialsOrder:
        currentLoop = trialsOrder
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsOrder.rgb)
        if thisTrialsOrder != None:
            for paramName in thisTrialsOrder.keys():
                exec(paramName + '= thisTrialsOrder.' + paramName)
        
        # ------Prepare to start Routine "isiCross"-------
        t = 0
        isiCrossClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        isi = random()*2+1
        thisExp.addData('random_duration', isi)
        # keep track of which components have finished
        isiCrossComponents = [fixation]
        for thisComponent in isiCrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "isiCross"-------
        while continueRoutine:
            # get current time
            t = isiCrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + isi- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isiCross"-------
        for thisComponent in isiCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "isiCross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trialOrder"-------
        t = 0
        trialOrderClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        digitCenterOrder.setText(digitC)
        digitRightOrder.setText(digitR)
        digitLeftOrder.setText(digitL)
        responseOrder = event.BuilderKeyResponse()
        if isOrder==0:
            correct = 'left'
        else:
            correct = 'right'
        time_zero = core.monotonicClock.getTime()
        thisExp.addData('onset', time_zero)
        thisExp.addData('numdist', numDist)
        # keep track of which components have finished
        trialOrderComponents = [digitCenterOrder, digitRightOrder, digitLeftOrder, responseOrder]
        for thisComponent in trialOrderComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trialOrder"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialOrderClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *digitCenterOrder* updates
            if t >= 0.0 and digitCenterOrder.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitCenterOrder.tStart = t
                digitCenterOrder.frameNStart = frameN  # exact frame index
                digitCenterOrder.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitCenterOrder.status == STARTED and t >= frameRemains:
                digitCenterOrder.setAutoDraw(False)
            
            # *digitRightOrder* updates
            if t >= 0.0 and digitRightOrder.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitRightOrder.tStart = t
                digitRightOrder.frameNStart = frameN  # exact frame index
                digitRightOrder.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitRightOrder.status == STARTED and t >= frameRemains:
                digitRightOrder.setAutoDraw(False)
            
            # *digitLeftOrder* updates
            if t >= 0.0 and digitLeftOrder.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitLeftOrder.tStart = t
                digitLeftOrder.frameNStart = frameN  # exact frame index
                digitLeftOrder.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitLeftOrder.status == STARTED and t >= frameRemains:
                digitLeftOrder.setAutoDraw(False)
            
            # *responseOrder* updates
            if t >= 0.0 and responseOrder.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseOrder.tStart = t
                responseOrder.frameNStart = frameN  # exact frame index
                responseOrder.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(responseOrder.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if responseOrder.status == STARTED and t >= frameRemains:
                responseOrder.status = STOPPED
            if responseOrder.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseOrder.keys == []:  # then this was the first keypress
                        responseOrder.keys = theseKeys[0]  # just the first key pressed
                        responseOrder.rt = responseOrder.clock.getTime()
                        # was this 'correct'?
                        if (responseOrder.keys == str(correct)) or (responseOrder.keys == correct):
                            responseOrder.corr = 1
                        else:
                            responseOrder.corr = 0
            
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialOrderComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialOrder"-------
        for thisComponent in trialOrderComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseOrder.keys in ['', [], None]:  # No response was made
            responseOrder.keys=None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               responseOrder.corr = 1  # correct non-response
            else:
               responseOrder.corr = 0  # failed to respond (incorrectly)
        # store data for trialsOrder (TrialHandler)
        trialsOrder.addData('responseOrder.keys',responseOrder.keys)
        trialsOrder.addData('responseOrder.corr', responseOrder.corr)
        if responseOrder.keys != None:  # we had a response
            trialsOrder.addData('responseOrder.rt', responseOrder.rt)
        
        
        
        # ------Prepare to start Routine "feedbackOrder"-------
        t = 0
        feedbackOrderClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        feedtxt = 'WRONG'
        feedcolor = 'red'
        
        if responseOrder.corr==1:
            feedtxt = 'CORRECT'
            feedcolor = 'green'
        textFeedbackOrder.setColor(feedcolor, colorSpace='rgb')
        textFeedbackOrder.setText(feedtxt)
        # keep track of which components have finished
        feedbackOrderComponents = [textFeedbackOrder]
        for thisComponent in feedbackOrderComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedbackOrder"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackOrderClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *textFeedbackOrder* updates
            if t >= 0.0 and textFeedbackOrder.status == NOT_STARTED:
                # keep track of start time/frame for later
                textFeedbackOrder.tStart = t
                textFeedbackOrder.frameNStart = frameN  # exact frame index
                textFeedbackOrder.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if textFeedbackOrder.status == STARTED and t >= frameRemains:
                textFeedbackOrder.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackOrderComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackOrder"-------
        for thisComponent in feedbackOrderComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsOrder'
    
    
    # ------Prepare to start Routine "ibiSun"-------
    t = 0
    ibiSunClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ibiSunComponents = [sun]
    for thisComponent in ibiSunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ibiSun"-------
    while continueRoutine:
        # get current time
        t = ibiSunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sun* updates
        if t >= 0.0 and sun.status == NOT_STARTED:
            # keep track of start time/frame for later
            sun.tStart = t
            sun.frameNStart = frameN  # exact frame index
            sun.setAutoDraw(True)
        frameRemains = 0.0 + ibiDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sun.status == STARTED and t >= frameRemains:
            sun.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ibiSunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ibiSun"-------
    for thisComponent in ibiSunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ibiSun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "infoControl"-------
    t = 0
    infoControlClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    counterControl.setText(i)
    # keep track of which components have finished
    infoControlComponents = [informationControl, counterControl]
    for thisComponent in infoControlComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "infoControl"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = infoControlClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *informationControl* updates
        if t >= 0.0 and informationControl.status == NOT_STARTED:
            # keep track of start time/frame for later
            informationControl.tStart = t
            informationControl.frameNStart = frameN  # exact frame index
            informationControl.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if informationControl.status == STARTED and t >= frameRemains:
            informationControl.setAutoDraw(False)
        
        # *counterControl* updates
        if t >= 0.0 and counterControl.status == NOT_STARTED:
            # keep track of start time/frame for later
            counterControl.tStart = t
            counterControl.frameNStart = frameN  # exact frame index
            counterControl.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if counterControl.status == STARTED and t >= frameRemains:
            counterControl.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in infoControlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "infoControl"-------
    for thisComponent in infoControlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    trialsControl = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'stimuli.xlsx', selection=bControl[i]),
        seed=None, name='trialsControl')
    thisExp.addLoop(trialsControl)  # add the loop to the experiment
    thisTrialsControl = trialsControl.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsControl.rgb)
    if thisTrialsControl != None:
        for paramName in thisTrialsControl.keys():
            exec(paramName + '= thisTrialsControl.' + paramName)
    
    for thisTrialsControl in trialsControl:
        currentLoop = trialsControl
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsControl.rgb)
        if thisTrialsControl != None:
            for paramName in thisTrialsControl.keys():
                exec(paramName + '= thisTrialsControl.' + paramName)
        
        # ------Prepare to start Routine "isiCross"-------
        t = 0
        isiCrossClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        isi = random()*2+1
        thisExp.addData('random_duration', isi)
        # keep track of which components have finished
        isiCrossComponents = [fixation]
        for thisComponent in isiCrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "isiCross"-------
        while continueRoutine:
            # get current time
            t = isiCrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + isi- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiCrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isiCross"-------
        for thisComponent in isiCrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "isiCross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trialControl"-------
        t = 0
        trialControlClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        digitCenterControl.setText(digitC)
        digitRightControl.setText(digitR)
        digitLeftControl.setText(digitL)
        responseControl = event.BuilderKeyResponse()
        if isTarget==0:
            correct = 'left'
        else:
            correct = 'right'
        time_zero = core.monotonicClock.getTime()
        thisExp.addData('onset', time_zero)
        thisExp.addData('numdist', numDist)
        # keep track of which components have finished
        trialControlComponents = [digitCenterControl, digitRightControl, digitLeftControl, responseControl]
        for thisComponent in trialControlComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trialControl"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialControlClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *digitCenterControl* updates
            if t >= 0.0 and digitCenterControl.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitCenterControl.tStart = t
                digitCenterControl.frameNStart = frameN  # exact frame index
                digitCenterControl.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitCenterControl.status == STARTED and t >= frameRemains:
                digitCenterControl.setAutoDraw(False)
            
            # *digitRightControl* updates
            if t >= 0.0 and digitRightControl.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitRightControl.tStart = t
                digitRightControl.frameNStart = frameN  # exact frame index
                digitRightControl.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitRightControl.status == STARTED and t >= frameRemains:
                digitRightControl.setAutoDraw(False)
            
            # *digitLeftControl* updates
            if t >= 0.0 and digitLeftControl.status == NOT_STARTED:
                # keep track of start time/frame for later
                digitLeftControl.tStart = t
                digitLeftControl.frameNStart = frameN  # exact frame index
                digitLeftControl.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if digitLeftControl.status == STARTED and t >= frameRemains:
                digitLeftControl.setAutoDraw(False)
            
            # *responseControl* updates
            if t >= 0.0 and responseControl.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseControl.tStart = t
                responseControl.frameNStart = frameN  # exact frame index
                responseControl.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(responseControl.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if responseControl.status == STARTED and t >= frameRemains:
                responseControl.status = STOPPED
            if responseControl.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    responseControl.keys = theseKeys[-1]  # just the last key pressed
                    responseControl.rt = responseControl.clock.getTime()
                    # was this 'correct'?
                    if (responseControl.keys == str(correct)) or (responseControl.keys == correct):
                        responseControl.corr = 1
                    else:
                        responseControl.corr = 0
            
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialControlComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trialControl"-------
        for thisComponent in trialControlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseControl.keys in ['', [], None]:  # No response was made
            responseControl.keys=None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               responseControl.corr = 1  # correct non-response
            else:
               responseControl.corr = 0  # failed to respond (incorrectly)
        # store data for trialsControl (TrialHandler)
        trialsControl.addData('responseControl.keys',responseControl.keys)
        trialsControl.addData('responseControl.corr', responseControl.corr)
        if responseControl.keys != None:  # we had a response
            trialsControl.addData('responseControl.rt', responseControl.rt)
        
        
        
        # ------Prepare to start Routine "feedbackControl"-------
        t = 0
        feedbackControlClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        feedtxt = 'WRONG'
        feedcolor = 'red'
        
        if responseControl.corr==1:
            feedtxt = 'CORRECT'
            feedcolor = 'green'
        
            
        textFeedbackControl.setColor(feedcolor, colorSpace='rgb')
        textFeedbackControl.setText(feedtxt)
        # keep track of which components have finished
        feedbackControlComponents = [textFeedbackControl]
        for thisComponent in feedbackControlComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedbackControl"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackControlClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *textFeedbackControl* updates
            if t >= 0.0 and textFeedbackControl.status == NOT_STARTED:
                # keep track of start time/frame for later
                textFeedbackControl.tStart = t
                textFeedbackControl.frameNStart = frameN  # exact frame index
                textFeedbackControl.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if textFeedbackControl.status == STARTED and t >= frameRemains:
                textFeedbackControl.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackControlComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedbackControl"-------
        for thisComponent in feedbackControlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsControl'
    
    
    # ------Prepare to start Routine "ibiSun"-------
    t = 0
    ibiSunClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ibiSunComponents = [sun]
    for thisComponent in ibiSunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ibiSun"-------
    while continueRoutine:
        # get current time
        t = ibiSunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sun* updates
        if t >= 0.0 and sun.status == NOT_STARTED:
            # keep track of start time/frame for later
            sun.tStart = t
            sun.frameNStart = frameN  # exact frame index
            sun.setAutoDraw(True)
        frameRemains = 0.0 + ibiDuration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sun.status == STARTED and t >= frameRemains:
            sun.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ibiSunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ibiSun"-------
    for thisComponent in ibiSunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ibiSun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "incrementCounter"-------
    t = 0
    incrementCounterClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    i = i + 1
    # keep track of which components have finished
    incrementCounterComponents = []
    for thisComponent in incrementCounterComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "incrementCounter"-------
    while continueRoutine:
        # get current time
        t = incrementCounterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in incrementCounterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "incrementCounter"-------
    for thisComponent in incrementCounterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "incrementCounter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed N_block repeats of 'blocks'













# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
