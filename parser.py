def response_parser(data):
    if len(data) > 1:
        return 'error: more than one person'
    if len(data) < 1:
        return 'error: no faces'
    emotions = data[0]['scores']
    for key in emotions:
        emotions[key] = round(emotions[key] * 100, 3)
    return emotions
