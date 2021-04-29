head = 15
track = [14,40,11,35,7,14]
total_track_traveled = 0
track_traveled = 0



for x in range (len(track)):
    print("head path = ",head," to ",track[x])
    print("track traveled = ",abs(head - track[x]),"\n")
    total_track_traveled += abs(head - track[x])
    head = track[x]

print("Total seek time (total number of tracks traveled) = ",total_track_traveled ,"ms")
print("Average seek time (Average number of tracks traveled) = ", total_track_traveled/len(track),"ms")
