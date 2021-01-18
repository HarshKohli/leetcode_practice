# Author: Harsh Kohli
# Date created: 10/20/2020

import copy
import time


def recurse(rect, level, points, unique_x, unique_y):
    last_point = rect[-1]
    if level == 1:
        min_area = float('inf')
        for point in unique_y[last_point[1]]:
            if point in rect:
                continue
            if point[0] - last_point[0] >= 0:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                area = recurse(rect_copy, level + 1, points, unique_x, unique_y)
                if area != -1 and area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1

    if level == 2:
        min_area = float('inf')
        for point in unique_x[last_point[0]]:
            if point in rect:
                continue
            if point[1] - last_point[1] >= 0:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                area = recurse(rect_copy, level + 1, points, unique_x, unique_y)
                if area != -1 and area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1

    if level == 3:
        min_area = float('inf')
        for point in unique_y[last_point[1]]:
            if point in rect:
                continue
            if point[0] == rect[0][0]:
                rect_copy = copy.deepcopy(rect)
                rect_copy.append(point)
                p1, p2, p3 = rect[0], rect[1], rect[2]
                area = (p2[0] - p1[0]) * (p3[1] - p2[1])
                if area < min_area:
                    min_area = area
        if min_area != float('inf'):
            return min_area
        else:
            return -1


def minAreaRect(points):
    min_area = float('inf')
    unique_x, unique_y = {}, {}
    for point in points:
        x, y = point[0], point[1]
        if x in unique_x:
            unique_x[x].append(point)
        else:
            unique_x[x] = [point]
        if y in unique_y:
            unique_y[y].append(point)
        else:
            unique_y[y] = [point]

    for point in points:
        x, y = point[0], point[1]
        if len(unique_x[x]) < 2 or len(unique_y[y]) < 2:
            continue
        area = recurse([point], 1, points, unique_x, unique_y)
        if area != -1 and area < min_area:
            min_area = area
    if min_area != float('inf'):
        return min_area
    else:
        return 0

def minAreaRect2(points):
    min_area = float('inf')
    unique_x, unique_y = {}, {}
    unique_all = set()
    for point in points:
        x, y = point[0], point[1]
        if x in unique_x:
            unique_x[x].append(point)
        else:
            unique_x[x] = [point]
        if y in unique_y:
            unique_y[y].append(point)
        else:
            unique_y[y] = [point]
        unique_all.add((x, y))
    for point1 in points:
        x1, y1, = point1[0], point1[1]
        for point2 in points:
            x2, y2 = point2[0], point2[1]
            if x1 >= x2 or y1 >= y2:
                continue
            if (x1, y2) in unique_all and (x2, y1) in unique_all:
                area = (x2 - x1) * (y2 - y1)
                if area < min_area:
                    min_area = area
    if min_area != float('inf'):
        return min_area
    else:
        return 0



points = [[36278, 22934], [36278, 21967], [9773, 3461], [36278, 3461], [9773, 31408], [9773, 3368], [9773, 36255],
          [9773, 23627], [9773, 13846], [9773, 35363], [9773, 23993], [9773, 34352], [9773, 24571], [9773, 23772],
          [36278, 27196], [9773, 38134], [9773, 21070], [36278, 20273], [36278, 35590], [36278, 34373], [36278, 36818],
          [36278, 16968], [36278, 13472], [36278, 35203], [9773, 18615], [9773, 2562], [36278, 33787], [36278, 31364],
          [36278, 26024], [9773, 34731], [36278, 30947], [9773, 31617], [36278, 27191], [9773, 20273], [9773, 21522],
          [9773, 5597], [9773, 12897], [9773, 3235], [36278, 17132], [36278, 24527], [9773, 35111], [9773, 33981],
          [9773, 8147], [9773, 39012], [36278, 4552], [36278, 10561], [36278, 7097], [9773, 33251], [36278, 2650],
          [9773, 2650], [36278, 6912], [9773, 38044], [36278, 23271], [9773, 15542], [36278, 11747], [9773, 7588],
          [36278, 34234], [9773, 19077], [36278, 31408], [9773, 38886], [9773, 25009], [36278, 25980], [9773, 15466],
          [9773, 29581], [9773, 17871], [36278, 31891], [36278, 12996], [9773, 7657], [9773, 20642], [36278, 30904],
          [9773, 21891], [9773, 14158], [9773, 37604], [36278, 27241], [36278, 2258], [36278, 19430], [36278, 38154],
          [9773, 23192], [36278, 33242], [9773, 9893], [9773, 7046], [36278, 6011], [9773, 29481], [36278, 15466],
          [9773, 20949], [9773, 11168], [36278, 34275], [36278, 33364], [9773, 14924], [9773, 29379], [36278, 6897],
          [36278, 21070], [9773, 35590], [36278, 21373], [9773, 6011], [36278, 6212], [9773, 33884], [36278, 23627],
          [9773, 34921], [36278, 9216], [36278, 10004], [36278, 503], [9773, 25837], [9773, 17305], [36278, 28593],
          [9773, 18223], [36278, 20838], [36278, 34731], [9773, 26101], [36278, 27614], [9773, 3352], [9773, 30002],
          [9773, 27614], [9773, 26025], [9773, 34336], [9773, 22507], [36278, 31188], [36278, 36377], [36278, 33981],
          [9773, 27971], [36278, 15696], [36278, 32513], [9773, 14203], [36278, 29379], [36278, 3830], [36278, 9169],
          [9773, 29391], [36278, 22931], [36278, 780], [9773, 4841], [9773, 405], [36278, 4094], [9773, 3830],
          [9773, 36377], [36278, 2702], [9773, 2258], [9773, 4094], [9773, 31508], [36278, 35488], [9773, 34765],
          [9773, 16161], [9773, 18668], [9773, 33242], [9773, 25980], [36278, 38821], [9773, 33361], [9773, 31891],
          [9773, 38154], [36278, 13312], [9773, 34976], [36278, 31508], [36278, 14158], [36278, 39805], [9773, 17267],
          [36278, 22507], [36278, 33884], [36278, 29214], [36278, 18668], [36278, 17871], [36278, 2149], [36278, 736],
          [9773, 2515], [36278, 18112], [9773, 39805], [36278, 35747], [9773, 9953], [36278, 14924], [36278, 18223],
          [36278, 4841], [36278, 12572], [36278, 9877], [9773, 9739], [9773, 36151], [36278, 23192], [36278, 14203],
          [36278, 34906], [36278, 2515], [9773, 15086], [36278, 39532], [9773, 36075], [9773, 38242], [9773, 29619],
          [9773, 27110], [36278, 34729], [36278, 21522], [9773, 26099], [9773, 11423], [9773, 28725], [9773, 1761],
          [36278, 20642], [36278, 36696], [9773, 36696], [9773, 18723], [9773, 13038], [9773, 24527], [36278, 39912],
          [36278, 26379], [9773, 9877], [9773, 38205], [36278, 18723], [36278, 2562], [36278, 25837], [36278, 38449],
          [9773, 39532], [36278, 26099], [36278, 34921], [36278, 27110], [36278, 24107], [36278, 38044], [9773, 18112],
          [9773, 20838], [36278, 38242], [36278, 34765], [36278, 15542], [9773, 30766], [36278, 33169], [9773, 12572],
          [9773, 23271], [36278, 2886], [9773, 24107], [9773, 27605], [36278, 36151], [36278, 13846], [9773, 34234],
          [36278, 6617], [9773, 38449], [9773, 9216], [36278, 27971], [9773, 37919], [9773, 35747], [36278, 10171],
          [36278, 33361], [9773, 30640], [9773, 27241], [36278, 9953], [36278, 36255], [9773, 277], [9773, 736],
          [36278, 3235], [9773, 30904], [36278, 38959], [36278, 17267], [9773, 39912], [36278, 7683], [9773, 27191],
          [9773, 30947], [36278, 123], [36278, 24337], [9773, 16968], [36278, 9995], [9773, 29138], [36278, 29601],
          [9773, 35978], [36278, 34772], [36278, 39490], [36278, 18615], [36278, 31930], [9773, 19487], [36278, 23772],
          [9773, 34772], [36278, 20448], [9773, 4290], [36278, 38134], [36278, 688], [9773, 33787], [9773, 24337],
          [36278, 7046], [36278, 33450], [9773, 12746], [9773, 31933], [36278, 35363], [9773, 23131], [36278, 31933],
          [36278, 34976], [36278, 277], [36278, 21891], [9773, 17132], [36278, 3352], [36278, 24571], [9773, 6212],
          [36278, 30002], [9773, 21373], [9773, 16019], [9773, 3850], [9773, 35488], [36278, 17305], [36278, 24325],
          [36278, 29619], [9773, 14354], [9773, 32574], [9773, 33364], [36278, 15086], [36278, 27605], [9773, 503],
          [36278, 29647], [9773, 33169], [9773, 20448], [36278, 26871], [9773, 22931], [36278, 1139], [9773, 27196],
          [36278, 4198], [36278, 34336], [9773, 29601], [9773, 34275], [9773, 12996], [36278, 8147], [9773, 182],
          [9773, 19311], [36278, 19077], [9773, 19430], [36278, 26025], [36278, 23058], [9773, 14442], [36278, 3998],
          [9773, 2886], [36278, 29581], [36278, 30640], [9773, 18683], [9773, 36223], [36278, 37919], [9773, 35543],
          [9773, 35203], [9773, 12730], [9773, 24325], [9773, 6897], [9773, 36818], [36278, 38886], [36278, 2314],
          [36278, 18051], [36278, 18683], [9773, 11747], [36278, 9893], [9773, 16050], [36278, 39592], [9773, 4552],
          [36278, 14442], [36278, 33251], [36278, 23131], [36278, 37604], [36278, 29481], [9773, 12456], [9773, 10171],
          [9773, 22934], [36278, 36283], [9773, 31364], [36278, 4338], [36278, 35111], [9773, 13312], [36278, 5597],
          [36278, 37382], [36278, 17172], [36278, 15351], [36278, 34925], [9773, 34373], [36278, 7657], [36278, 16978],
          [9773, 16978], [36278, 35978], [36278, 405], [36278, 22713], [9773, 9271], [9773, 2149], [9773, 37382],
          [9773, 9169], [9773, 35591], [36278, 2088], [9773, 32513], [36278, 13038], [9773, 3289], [9773, 15696],
          [36278, 39012], [36278, 21212], [9773, 31188], [9773, 17172], [9773, 38947], [9773, 7097], [9773, 21212],
          [36278, 33512], [36278, 39302], [36278, 12897], [36278, 38947], [36278, 3289], [36278, 11522], [9773, 18051],
          [9773, 2798], [36278, 29138], [36278, 15037], [9773, 10004], [9773, 33450], [36278, 1761], [36278, 23427],
          [36278, 35543], [9773, 38821], [36278, 28725], [36278, 16161], [9773, 2314], [9773, 13472], [36278, 9271],
          [36278, 16662], [9773, 31930], [9773, 32261], [9773, 23058], [9773, 26024], [36278, 13303], [36278, 3713],
          [36278, 20949], [9773, 13303], [36278, 34352], [9773, 123], [9773, 4338], [9773, 15037], [9773, 3998],
          [36278, 11423], [9773, 38933], [36278, 19414], [9773, 38959], [36278, 23496], [9773, 33512], [36278, 1056],
          [9773, 19414], [36278, 19315], [36278, 23993], [9773, 10211], [9773, 34906], [9773, 36283], [36278, 16050],
          [36278, 3368], [9773, 12616], [36278, 9739], [36278, 26101], [36278, 3796], [9773, 21967], [9773, 24552],
          [9773, 6617], [9773, 28593], [36278, 14354], [9773, 2088], [9773, 14835], [9773, 3796], [9773, 16662],
          [36278, 35672], [9773, 35672], [9773, 22713], [9773, 29647], [36278, 30766], [36278, 16019], [36278, 24552],
          [9773, 29214], [9773, 9995], [9773, 688], [9773, 10561], [9773, 780], [9773, 34925], [9773, 23427],
          [36278, 14835], [36278, 35591], [36278, 12616], [36278, 3850], [36278, 36223], [36278, 11168], [36278, 38933],
          [9773, 11522], [36278, 182], [36278, 19487], [36278, 2798], [9773, 39302], [36278, 12456], [9773, 23496],
          [36278, 10211], [9773, 3713], [36278, 4290], [36278, 32632], [9773, 32632], [9773, 2702], [9773, 19315],
          [36278, 19311], [36278, 32261], [9773, 4198], [36278, 290], [9773, 39592], [9773, 1139], [36278, 36075],
          [36278, 31617], [36278, 12746], [9773, 26871], [9773, 39490], [36278, 29391], [9773, 6912], [9773, 290],
          [9773, 7683], [36278, 25009], [36278, 7588], [9773, 15351], [36278, 38205], [9773, 34729], [9773, 26379],
          [36278, 12730], [9773, 1056], [36278, 32574]]
#points = [[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]
start = time.time()
print(minAreaRect2(points))
end = time.time()
print('Time taken = ' + str((end - start) * 1000) + ' ms')
