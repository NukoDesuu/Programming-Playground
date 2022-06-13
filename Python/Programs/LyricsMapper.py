import time as t

class Player:
    def __init__(self):
        pass

    def Play(bpm, lyrics, beats):
        bpm_v = int(bpm) #beats per minute
        tpb = 1 / (bpm_v / 60)

        #time per one beat (black note), d at the end means "dot" (multiplied by 1.5)
        b = 1
        bd = b * 1.5

        #double beats (white note)
        b2 = b * 2 
        b2d = b2 * 1.5

        #quadruple beats (whole note)
        b4 = b * 4
        b4d = b4 * 1.5

        #half note
        b12 = b / 2
        b12d = b12 * 1.5

        #quarter note
        b14 = b / 4
        b14d = b14 * 1.5

        #one-eighth note
        b18 = b / 8
        b18d = b18 * 1.5

        dur = {'b':b, 'bd':bd, 'b2':b2, 'b2d':b2d, 'b4':b4, 'b4d':b4d, 
                'b12':b12, 'b12d':b12d, 'b14':b14, 'b14d':b14d, 'b18':b18d}

        for i, e in enumerate(lyrics):
            if e != '*':
                print(e)
            t.sleep(dur[beats[i]] * tpb)