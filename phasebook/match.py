import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # Get the highest number and make it as the length of the loop
    if len(fave_numbers_1) > len(fave_numbers_2):
        length = len(fave_numbers_1)
        high = fave_numbers_1
        low = fave_numbers_2
    else:
        length = len(fave_numbers_2)
        high = fave_numbers_2
        low = fave_numbers_1
    
    for i in range(length + 1):
        for j in range(i):
            # Restart the loop if the j is grater than the low number
            if j >= len(low):
                continue
            # check if the number is a match and return true
            if low[j] == high[(i-1)-j]:
                return True
    return False
