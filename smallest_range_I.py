class Sol:
    def smallest_range_I(self,arr,k):
        return max(0,max(arr)-min(arr)-2*k)
if __name__ == '__main__':
    p = Sol()
    print(p.smallest_range_I(arr=[1,4,5,1], k=4))
