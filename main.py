# python3

def parallel_processing(n, m, data):
    output = []
    threads_time_list = []

    seconds_count = 0
    for i in range(0, n):
        output.append([i, seconds_count])
        threads_time_list.append(data[0])
        data = data[1:]

    for i in range(len(data)):
        zeroes_list=[]
        while 0 not in threads_time_list:
            for unit in range(len(threads_time_list)):
                threads_time_list[unit] -=1
                if (threads_time_list[unit] == 0):
                    zeroes_list.append(unit)
            seconds_count+=1
        for zero in range(len(zeroes_list)):
            output.append([zeroes_list[zero], seconds_count]) 
            threads_time_list[zeroes_list[zero]] = data[i]
            if len(zeroes_list)>1:
                i+=1
        if len(output) == m:
            return output
        
        
        

    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    ievade = list(input().split(" "))
    n = int(ievade[0])
    m = int(ievade[1])
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i, j)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
