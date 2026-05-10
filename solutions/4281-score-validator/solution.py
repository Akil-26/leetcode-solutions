class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for now in events:
            if counter >= 10:
                break
            if now in '012346':
                score += int(now)
            elif now == 'W':
                counter += 1
            elif now == 'WD' or now =='NB':
                score += 1
        return [score,counter]
