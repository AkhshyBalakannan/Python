import time
import concurrent.futures
import threading
import requests

# # Basic without threading
# # import time

start = time.perf_counter()  # Calculate start time


def waste_time():
    '''Simple finction to waste time'''
    print("Sleeping 1 Second")
    time.sleep(1)  # sleeps and does nothing
    print("Done Sleeping")


waste_time()
waste_time()

finish = time.perf_counter()  # Calculate end time

print(f'Finished in {round(finish-start,2)} second(s)')

# -----------------------------------------------------------

# # Using Threading the old way
# # To run this block of code uncomment line 38-46 or 48-57

# # import threading
# # import time

start = time.perf_counter()  # Calculate start time


def waste_time(seconds):
    '''Simple finction to waste time'''
    print(f"Sleeping {seconds} Second(s)")
    time.sleep(seconds)  # sleeps and does nothing
    print(f"Done Sleeping {seconds}")


# call threading manually
t1 = threading.Thread(target=waste_time, args=[1])
t2 = threading.Thread(target=waste_time, args=[1])

t1.start()
t2.start()

t1.join()
t2.join()

# ---------Either above or below code to be run---------------

# To run Threading using for loop
threads = []  # Collect threads to give .join()

for _ in range(10):
    t = threading.Thread(target=waste_time, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()  # Calculate end time

print(f'Finished in {round(finish-start,2)} second(s)')

# -----------------------------------------------------------
# # Using threading now a days

# # import time
# # import concurrent.futures

start = time.perf_counter()


def waste_time(seconds):
    print(f"Sleeping {seconds} Second(s)")
    time.sleep(seconds)
    return f"Done Sleeping {seconds} sec"


with concurrent.futures.ThreadPoolExecutor() as executor:  # module imported way
    f1 = executor.submit(waste_time, 1)  # Will return val from function
    print(f1.result())

# ---------Either above or below code to be run---------------

with concurrent.futures.ThreadPoolExecutor() as executor:  # module imported way
    secs = [5, 4, 3, 2, 1]  # Different sec
    results = [executor.submit(waste_time, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# ---------Either above or below code to be run---------------

with concurrent.futures.ThreadPoolExecutor() as executor:  # module imported way
    secs = [5, 4, 3, 2, 1]  # Different sec
    results = executor.map(waste_time, secs)  # Map on iterator
    # Here the output will return in the way how it started default behav of map
    # so this is looks like not that big of improvement in time but works correct
    for result in results:
        print(result)


finish = time.perf_counter()  # Calculate end time

print(f'Finished in {round(finish-start,2)} second(s)')

# -----------------------------------------------------------
# IO Bound Operations
# Download Image from url using threading

# # import requests
# # import time
# # import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    # https://images.unsplash.com/photo-1516117172878-fd2c41f4a759
    img_name = img_url.split('/')[3]  # To split the name from url
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Map will run the func with list iterator
    executor.map(download_image, img_urls)


finish = time.perf_counter()

print(f'Finished in {finish-start} seconds')
