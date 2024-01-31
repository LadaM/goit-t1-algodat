from priority_queue import PriorityQueue


def convert_image(file_name, target_format):
    # Let's assume that this function converts a given image to a target format
    print(f"Конвертація {file_name} до {target_format} формату...")
    return f"{file_name.split('.')[0]}.{target_format}"


def main():
    pq = PriorityQueue()

    # Users upload their images here
    pq.enqueue(("sample1.jpg", "png"), 1)
    pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # premium user with higher priority
    pq.enqueue(("sample2.jpg", "tiff"), 1)

    while not pq.is_empty():
        file_name, target_format = pq.dequeue()
        output_file = convert_image(file_name, target_format)
        print(f"Зображення було успішно конвертовано і збережено як {output_file}!")


if __name__ == "__main__":
    main()
