from TikTokApi import TikTokApi
import json
import matplotlib.pyplot as plt 


api = TikTokApi.get_instance()
#How many results you want
results = 500
#input your tiktok ID. "In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value."
trending = api.trending(count=results, custom_verifyFp="")
hastagsDict = {}
musicDict = {}
durationDict = {}

#goes through the trending videos
for tiktok in trending:
    if tiktok["music"]["title"] in musicDict:
        musicDict[tiktok["music"]["title"]] += 1
    else:
        musicDict[tiktok["music"]["title"]] = 1

    if tiktok["video"]["duration"] in durationDict:
        durationDict[tiktok["video"]["duration"]] += 1
    else:
        durationDict[tiktok["video"]["duration"]] = 1
    
    try:
        for hastag in tiktok["challenges"]:
            if hastag["title"] in hastagsDict:
                hastagsDict[hastag["title"]] += 1
            else:
                hastagsDict[hastag["title"]] = 1
    except Exception as e:
        print("No hastags")

#removes hashtags that have been used less than 3 times
for num in hastagsDict.copy():
    if hastagsDict[num] <= 3:
        hastagsDict.pop(num)

for num in musicDict.copy():
    if musicDict[num] <= 2:
        musicDict.pop(num)

#sets theme for matplotlib graph, makes it dark
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use('dark_background')

#Graoh for Hastags
fig, ax = plt.subplots()
ax.bar(list(hastagsDict.keys()), list(hastagsDict.values()))
ax.set_xticklabels(list(hastagsDict.keys()), rotation=60, horizontalalignment="right", fontsize="10")
ax.set_title(f"Hashtags used in {results} viral videos", fontsize=15)
ax.set_ylabel("# Of Hastags")
ax.set_xlabel("Hashtags Being Used")

#Graoh for Music
fig1, ax1 = plt.subplots()
ax1.bar(list(musicDict.keys()), list(musicDict.values()))
ax1.set_xticklabels(list(musicDict.keys()), rotation=60, horizontalalignment="right", fontsize="7")
ax1.set_title(f"Music used in {results} viral videos", fontsize=15)
ax1.set_ylabel("# Of Uses")
ax1.set_xlabel("Songs Titles")

#Graoh for Duration of TikTok videos
fig2, ax2 = plt.subplots()
ax2.bar(list(durationDict.keys()), list(durationDict.values()))
ax2.set_xticklabels(list(durationDict.keys()), fontsize="12")
ax2.set_title(f"Duration in {results} trending videos (secs).", fontsize=15)
ax2.set_ylabel("# Of Videos")
ax2.set_xlabel("Duration")
print(durationDict)
plt.show()