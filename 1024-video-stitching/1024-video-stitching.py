class Solution:
    def videoStitching(self, clips, T):
        timepoint = namedtuple('timepoint', ['start', 'end'])
        times = sorted([timepoint(clip[0], clip[1]) for i, clip in enumerate(clips)])
        res = [times[0]]
        for time in times:
            if res[-1].end >= T or time.start > res[-1].end:
                break
            if time.start == res[-1].start and time.end > res[-1].end:
                res[-1] = time
            elif time.end <= res[-1].end:
                continue
            elif time.start <= res[-1].start:
                res[-1] = timepoint(res[-1].start, time.end)
            else:
                res.append(timepoint(res[-1].end, time.end))
        return len(res) if res[0].start == 0 and res[-1].end >= T else -1