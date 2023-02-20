# First-In-First-Out (FIFO) Page Replacement Algorithm

# Function to check if a page exists in the frames
def search(frames, page):
    for frame in frames:
        if frame == page:
            return True
    return False

# Function to perform FIFO page replacement
def fifo(pages, n_frames):
    frames = [''] * n_frames
    faults = 0
    next_frame = 0 # Index to keep track of the next available frame

    for page in pages:
        if not search(frames, page):
            frames[next_frame] = page
            next_frame = (next_frame + 1) % n_frames
            faults += 1
        print(frames)

    return faults

# Take user input for the page reference string and number of frames
pages = input("Enter the page reference string: ").split()
n_frames = int(input("Enter the number of frames: "))

# Call the FIFO page replacement function
faults = fifo(pages, n_frames)

# Print the number of page faults
print("Number of Page Faults:", faults)


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
n_frames = 3

page_faults = fifo(pages, n_frames)

print(f"Number of page faults: {page_faults}")
