import requests
import random
import os

def get_cat_image():
    status_codes = [
        200, 201, 202, 203, 204, 205, 206, 207, 208, 226,
        300, 301, 302, 303, 304, 305, 306, 307, 308,
        400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451,
        500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511
    ]
    status_code = random.choice(status_codes)
    response = requests.get(f"https://http.cat/{status_code}.jpg")
    return response.content

def main():
    cat_image = get_cat_image()
    with open("cat_image.jpg", "wb") as file:
        file.write(cat_image)
    os.startfile("cat_image.jpg")

if __name__ == "__main__":
    main()