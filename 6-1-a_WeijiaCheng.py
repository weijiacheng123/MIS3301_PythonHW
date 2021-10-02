# Define main function
# asks Kevin about the number of videos
# Opens a file to save the recording times
# For each recording asks Kevin to
# enter the time of recording and write it to a file
def main():
    num = int(input('What is the number of video? '))
    outfile = open('number.txt','w+')
    outfile.write('the number of videos is '+str(num) +"\n")
    for count in range(1,num+1):
        time = float(input('What is the time of recording? '))
        outfile.write("The time of No.{} video is {}\n".format(count,time))
    
    
    # Close the file
    outfile.close()
    
                  
    # Display what happened
    infile = open('number.txt','r')
    content = infile.read()
    print(content)
    infile.close()
    
# Call main function
main()
