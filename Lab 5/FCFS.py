def FCFS(head, track):

    total_track_traveled = 0

    for x in range(len(track)):
        print("Head path: Track", head, "to track", track[x])
        print("No of tracks traveled =", abs(head - track[x]), "\n")
        total_track_traveled += abs(head - track[x])
        head = track[x]

    print("Total seek time (total number of tracks traveled) =",
          total_track_traveled, "ms")
    print("Average seek time (average number of tracks traveled) =",
          total_track_traveled/len(track), "ms")


head = 15
track = [4, 40, 11, 35, 7, 14]

FCFS(head, track)
