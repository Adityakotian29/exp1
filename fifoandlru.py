
def fifo(page_list):
    frames = []  
    faults = 0  
    index = 0  

    for i in page_list:
        if i not in frames:
            if len(frames) < 3:
                frames.append(i)
            else:
                frames[index] = i
                index = (index + 1) % 3
            faults += 1
          
        print("frames:",frames ,"position of changes",index) 

    return faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
print("Page Faults:", fifo(pages))


def recently_used(frames, current, index):
    if index < len(current):
        if current[index] in frames :
            
            return current[index]
        
        return recently_used(frames, current, index + 1 )
    
    

def lru(page_list):
    frames = []  
    faults = 0  

    for i in page_list:
        if i not in frames:
            if len(frames) < 3:
                frames.append(i)
            else:
                recent = recently_used(frames, page_list[:page_list.index(i) ],0)
                
                if recent is not None:
                    frames[frames.index(recent)] = i  # Replace the least recently used page with i
                    faults += 1
                else:
                    faults += 1  # If no least recently used page found, it's a fault

        print("frames:", frames)
        

    return faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
print("Page Faults (LRU):", lru(pages))












