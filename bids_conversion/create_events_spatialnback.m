function create_events_spatialnback(path,pathBid)
% Function features:
%
% (input)   path: path to Presentation logfile from spatialnback task
%           pathBid: path to place where new _events.tsv file
%           (BIDS-compatibile) should be placed
%
% (1)   this function converts task logfile from fMRI scanner into
%       _events.tsv file required in BIDS dataset (classify responses and
%       calculate reaction time)
%
% Author: Kamil Bonna
% ICNT, 20/03/2018
% Ver: MATLAB R2017a
%%
[~,name,~] = fileparts(path);
subjId = str2num(name(1:3));
ses = name(6);
newName = strcat('sub-',num2str(subjId,'%02i'),'_ses-',ses,'_task-spatialnback_events.csv');
%% log conventions
spatial_events = {'s1, yes','s1, no',...
                's2, yes','s2, no',...
                's3, yes','s3, no',...
                's4, yes','s4, no',...
                's5, yes','s5, no',...
                's6, yes','s6, no',...
                's7, yes','s7, no',...
                's8, yes','s8, no'};             
%% reading data from file
fileId = fopen(path);                                      
gcl = fgets(fileId); %(get line)                
while ~contains(gcl,'Subject')
    gcl = fgets(fileId);                                   
end
fgets(fileId);                                             
G=textscan(fileId,'%*s %*d %*s %s %*s %*s %*s %d %d %*s %*s %*s %*s %*s %*s %*s','Delimiter','\t');
fclose(fileId); 
%% create clock 
i0 = 1;
while ~strcmp(G{1}{i0},'1-back intro')
   i0 = i0 + 1; 
end
clock = double(G{2}-G{2}(i0))/10000;
%% find stimulis, correct answers, and time
h = 1;
ind = zeros(240,5);
for i = 1 : numel(G{1})
    if contains(G{1}{i},', no') || contains(G{1}{i},', yes') %(is stimulus)
        % index, right button to press, time of stimulus
        ind(h,:) = [i, contains(G{1}{i},', yes')+8*contains(G{1}{i},', no'), clock(i),0,0];
        h = h + 1; 
    end
end
%% find subject responses
ind = [ind ; numel(G{1}) , Inf , Inf , 0 , 0];                                                   
for i = 1 : size(ind,1)-1
    for j = ind(i,1)+1 : ind(i+1,1)-1 
       if strcmp(G{1}{j},'1') || strcmp(G{1}{j},'8') %(response found)
           ind(i,4) = str2num(G{1}{j}); %(ID of pressed button)
           ind(i,5) = clock(j); %(time of response)
           break;                                                          
       end
    end
end
ind = ind(1:240,:);
%% classify responses and calculate RT
ind_correct = cell(240,1);
for i = 1 : size(ind,1)
    if (ind(i,2) == 8) && (ind(i,4) == 8)
        ind_correct{i,1} = 'correct-rejection';
    elseif (ind(i,2) == 1) && (ind(i,4) == 1)
        ind_correct{i,1} = 'hit';
    elseif (ind(i,2) == 8) && (ind(i,4) == 1)
        ind_correct{i,1} = 'false-alarm';
    else
        ind_correct{i,1} = 'miss';
    end
end
ind_rt = ind(:,5) - ind(:,3);                                            
ind_rt((ind_rt<0)|(ind_rt>2)) = -1;
%% create table BIDS-compatibile
k = 1; 
h = 1;
bidOns = zeros(1,260); 
bidDur = zeros(1,260);
bidTri = cell(1,260);
bidRt  = cell(1,260);
bidCor = cell(1,260);
bidSti = cell(1,260);
for i = 1 : numel(G{1})
    switch G{1}{i}
        case spatial_events
            bidOns(k) = clock(i);
            bidDur(k) = 0.5;
            bidTri{k} = 'spatial-stimuli';
            if isequal(ind_rt(h),-1)
                bidRt{k} = 'n/a';
            else
                bidRt{k} = ind_rt(h);
            end
            bidCor{k} = ind_correct{h};
            bidSti{k} = strcat('images/',G{1}{i}(1:2),'.png');            
                k = k + 1;
                h = h + 1;
        case {'1-back intro','2-back intro'}
            bidOns(k) = clock(i);
            bidDur(k) = 4;
            bidTri{k} = 'task-instruction';
            bidRt{k} = 'n/a';
            bidCor{k} = 'n/a';
            switch G{1}{i}
                case '1-back intro'
                    bidSti{k} = 'images/1-back.jpg';
                case '2-back intro'
                    bidSti{k} = 'images/2-back.jpg';
            end
                k = k + 1;
    end
end  
events = table(bidOns',bidDur',bidTri',bidRt',bidCor',bidSti');
events.Properties.VariableNames = {'onset','duration','trial_type','response_time','correct','stim_file'};
    nameBid = fullfile(pathBid,newName);
writetable(events,nameBid,'Delimiter','\t');
% new extension
[nameBidFolder,nameBidFile,~] = fileparts(nameBid);
    nameBidNew = fullfile(nameBidFolder,strcat(nameBidFile,'.tsv'));
movefile(nameBid,nameBidNew);
end
