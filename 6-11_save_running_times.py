# this program saves a sequence of video running times to the video_times.txt file

def main():
    # get the number of videos
    num_videos = int(input('How many videos are in the project? '))

    # open the file to hole the running files
    video_file = open('video_times.txt', 'w')

    # get each video running time and write to the file
    print('Enter the running times for each video.')
    for count in range(1, num_videos + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    # close the file
    video_file.close()

# call the main function
main()

