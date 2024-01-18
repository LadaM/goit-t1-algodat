import uuid
from queue import Queue

CLOSE = ["end", "close", "finish", "exit"]
max_requests = 9
min_requests = 1
newline = "\n"
result_line_start = "--> "
warning_line_start = "!!! "


def generate_request(q: Queue, content: str = ""):
    request_id = str(uuid.uuid4())
    q.put({"id": request_id, "content": content})
    print(
        f"{result_line_start}Created request {request_id}"
        + (f" with content {content}" if content else "")
        + newline
    )


def process_request(q: Queue):
    if q.empty():
        print("No requests yet")
        return
    item = q.get()
    # process request
    print(f"{result_line_start}Processing request {item}{newline}")
    q.task_done()


def main():
    queue = Queue()
    while True:
        ui = input(
            f"""Enter {min_requests} .. {max_requests} to generate desired number of requests.
            Enter a string to create a request with the respective content. 
                Enter 0 or nothing to process the first request on queue.
                    To exit type any of {CLOSE}{newline}"""
        )
        if ui in CLOSE:
            break
        elif ui.isdigit():
            n = int(ui)
            if n == 0:
                process_request(queue)
            elif n > max_requests:
                print(
                    f"{warning_line_start}Cannot generate more than {max_requests} requests"
                )
            elif n < min_requests:
                print(
                    f"{warning_line_start}Number of requests must be positive {min_requests}, .., {max_requests}"
                )
            else:
                for i in range(n):
                    generate_request(queue)
            continue
        elif ui.isspace() or ui == "":
            process_request(queue)
            continue
        else:
            generate_request(queue, ui)
            continue


if __name__ == "__main__":
    main()
