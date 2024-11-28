fNumber=int(input("Enter the number to print the fibonacci series"))
fSeries=[0,1]

def fSeriesFunction(fNumber):

    if fNumber==0 or fNumber==1:
        return [0]
    for i in range(2,fNumber):
        fSeries.append(fSeries[i-2]+fSeries[i-1])
        print(fSeries[i-2]+fSeries[i-1])
        #fSeries.append(fSeries[(i-1)+(i-2)])
    return fSeries

print(fSeriesFunction(fNumber))