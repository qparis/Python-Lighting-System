def between(scene1, scene2, distance):
    def between_scene_item(item1, item2):
        result = {}
        for key in item1:
            if key in item2:
                result[key] = item1[key] * distance + item2[key] * (1 - distance)
        return result

    return [between_scene_item(scene1_item, scene2_item) for (scene1_item, scene2_item) in list(zip(scene1, scene2))]