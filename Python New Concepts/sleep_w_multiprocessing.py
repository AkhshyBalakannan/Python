import multiprocessing
import time
import concurrent.futures
from PIL import Image, ImageFilter


def waste_time(seconds):
    '''Simple finction to waste time'''
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    return f"Done Sleeping {seconds}"

# # Basic without multiprocessing
# # import time

# start = time.perf_counter() # Calculate start time

# def waste_time(seconds):
#     '''Simple finction to waste time'''
#     print(f"Sleeping {seconds} second")
#     time.sleep(seconds)
    # print(f"Done Sleeping {seconds}")
# waste_time(1)

# finish = time.perf_counter() # Calculate end time

# print(f'Finished in {round(finish-start, 2)} second(s)')

# -----------------------------------------------------------

# # Using Multiprocessing the old way
# # To run this block of code uncomment line

# # import multiprocessing
# # import time

# def waste_time(seconds):
#     '''Simple finction to waste time'''
#     print(f"Sleeping {seconds} second")
#     time.sleep(seconds)
    # print(f"Done Sleeping {seconds}")

# if __name__ == '__main__':
#     start = time.perf_counter()  # Calculate start time

#     # call multiprocessing manually
#     # p1 = multiprocessing.Process(target=waste_time)
#     # p2 = multiprocessing.Process(target=waste_time)
#     # p1.start()
#     # p2.start()
#     # p1.join()
#     # p2.join()

# # ---------Either above or below code to be run---------------
#     processes = []  # Collect process

#     for _ in range(10):
#         p = multiprocessing.Process(target=waste_time, args=[1.5])
#         # Normolly for multiprocessing the args but be serialized pickle object
#         # Which means python objects converted into format
#         # that can be deconstructed and reconstructed in other python script
#         p.start()
#         processes.append(p)

#     for process in processes:
#         process.join()

#     finish = time.perf_counter()  # Calculate end time

#     print(f'Finished in {round(finish-start, 2)} second(s)')

# -----------------------------------------------------------
# # Using Multiprocessing

# # import time
# # import concurrent.futures


# if __name__ == '__main__':
#     start = time.perf_counter()

#     # with concurrent.futures.ProcessPoolExecutor() as executor:
#     #     p1 = executor.submit(waste_time, 1)
#     #     p2 = executor.submit(waste_time, 1)

#     #     print(p1.result())
#     #     print(p2.result())

# # ---------Either above or below code to be run---------------

#     # with concurrent.futures.ProcessPoolExecutor() as executor:
#     #     secs = [5, 4, 3, 2, 1]  # Different sec
#     #     results = [executor.submit(waste_time, sec) for sec in secs]

#     #     for f in concurrent.futures.as_completed(results):
#     #         print(f.result())

# # ---------Either above or below code to be run---------------

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5, 4, 3, 2, 1]
#         results = executor.map(waste_time, secs)
#         # Here the output will return in the way how it started default behav of map
#         # so this is looks like not that big of improvement in time but works correct
#         for result in results:
#             print(result)
#             # Any Exception is created it can be accessed here only
#             # Not while the process is done and so try catch should be here

#     finish = time.perf_counter()

#     print(f'Finish in {round(finish-start, 2)} second(s)')

# -----------------------------------------------------------
# IO Bound Operations but for Multiprocess we use CPU
# Download Image from url using threading

# import time
# from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]


def process_img(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed.')


if __name__ == '__main__':

    start = time.perf_counter()

    size = (1200, 1200)

    # for img_name in img_names:
    #     img = Image.open(img_name)

    #     img = img.filter(ImageFilter.GaussianBlur(15))

    #     img.thumbnail(size)
    #     img.save(f'processed/{img_name}')
    #     print(f'{img_name} was processed.')

    # ---------------Before using executor -------------

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_img, img_names)

    finish = time.perf_counter()

    print(f'Finished in {finish-start} seconds')
