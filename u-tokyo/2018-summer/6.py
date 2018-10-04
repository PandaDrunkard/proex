import sys
import dataset as ds

def sort_by_bright(img):
    size = len(img)
    # use index as a bright adjuster for images of same brightness
    bright = lambda e: e[0]**2 + e[1]**2 + e[2]**2 - e[3]/size
    by_blight = sorted(img, key=bright)

    return list(by_blight)

def distance(e1, e2, size):
    '''
    e1を基準点とする。
    '''
    if e1 == e2:
        return 0
    else:
        d = 0
        for i1, i2 in zip(e1[:3], e2[:3]):
            d += abs(i1 - i2)
        # append (0,1) diff to distinct pairs of same distance
        d += 1 - e1[3] / size

        # print(f'|{e1} - {e2}| = {d}')

        return d

def new_centres(img, centres, k):
    size = len(img)
    clusters = [[] for _ in range(k)]

    for im in img:
        cluster_idx = nearest(im, centres, size)
        clusters[cluster_idx].append(im)

    # determine new centers
    new_centres = []
    for cluster in clusters:
        c_size = len(cluster)
        r_avg = sum(map(lambda e: e[0], cluster)) // c_size
        g_avg = sum(map(lambda e: e[1], cluster)) // c_size
        b_avg = sum(map(lambda e: e[2], cluster)) // c_size
        avg_point = tuple([r_avg, g_avg, b_avg, 0]) # 0 for dummy index
        
        centre_idx = nearest(avg_point, cluster, size)
        new_centres.append(cluster[centre_idx])

    return new_centres, clusters

def nearest(e, centres, size):
    nearest_dist = 10*10
    nearest_idx = -1
    for i, c in enumerate(centres):
        d = distance(c, e, size)
        if d < nearest_dist:
            nearest_dist = d
            nearest_idx = i
    return nearest_idx

def main(filename='image.tif', k=32, epochs=10):
    img = ds.image2(append_index=True)
    
    centres, clusters = cluster_img(img, k, epochs)

    new_img = []
    for c, cluster in zip(centres, clusters):
        for element in cluster:
            if tuple(element[:3]) == ds.WHITE:
                new_img.append(element)
            else:
                new_img.append(c[:3] + tuple(element[-1:]))

    new_img = sorted(new_img, key=lambda i: i[-1])

    out_img = ds.format_square(new_img)

    ds.save_image(filename, out_img)

def cluster_img(img, k, epochs):
    img = sort_by_bright(img)
    n = len(img)
    centres = [img[n * i // k] for i in range(k)]
    clusters = None
    
    for epoch in range(epochs):
        print(centres)
        centres, clusters = new_centres(img, centres, k)
    
    return centres, clusters

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')