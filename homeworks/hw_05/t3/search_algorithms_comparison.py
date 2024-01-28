from pathlib import Path
from timeit import default_timer as timer

from boyer_moore import boyer_moore_search
from knuth_morris_pratt import kmp_search
from rabin_karp import rabin_karp_search


def measure_search_time(search_func, file, search_string):
    start = timer()
    search_res = search_func(file, search_string)
    end = timer()
    return search_res, end - start


def print_table_divider(width=30):
    print("-" * width)


def main():
    # choose paths for test
    parent_path = Path(__file__).parent
    file1_path = Path.joinpath(parent_path, "text1.txt")
    file2_path = Path.joinpath(parent_path, "text2.txt")

    # choose strings for test
    existing_string_text_1 = ("Експоненціальний пошук використовується для пошуку елементів шляхом переходу в "
                              "експоненціальні позиції")
    not_existing_string_text_1 = ("Дельфі́нові (Delphinidae) — родина ссавців підряду зубатих китів ряду китоподібних "
                                  "(Cetacea). Представники родини трапляються в усіх океанах і морях, "
                                  "а також у деяких річкових системах. Дельфінові видаються дуже розумними, "
                                  "вони швидко й гнучко можуть адаптуватися до нових ситуацій.")
    existing_string_text_2 = "Triples Storage and SPARQL Query Processing."
    not_existing_string_text_2 = ("As Stephen King said – 'A short story is a different thing all together – a short "
                                  "story is like a kiss in the dark from a stranger.'")
    test_strings = {
        "text1": [existing_string_text_1, not_existing_string_text_1],
        "text2": [existing_string_text_2, not_existing_string_text_2],
    }
    search_algorithm_by_name = {
        "Rabin-Karp": rabin_karp_search,
        "Knuth-Moore-Pratt": kmp_search,
        "Boyer-Moore": boyer_moore_search,
    }

    with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
        text1 = file1.read()
        text2 = file2.read()

        # for each algorithm run two tests: imaginary string and existing string in art 1 and 2
        for text_name, search_strings in test_strings.items():
            text = text1 if text_name == "text1" else text2
            for search_string in search_strings:
                print(f"\nSearching {text_name} for \n{' '*4}\"{search_string}\"")
                print_table_divider(55)
                print(f"| {'Algorithm':<20} | {'Result':<15} | {'Time (ms)':<10} |")
                print_table_divider(55)
                for algorithm_name, function in search_algorithm_by_name.items():
                    search_res, time = measure_search_time(
                        function, text, search_string
                    )
                    print(
                        f"| {algorithm_name:<20} | {'Found at ' + str(search_res) if search_res != -1 else 'Not found': <15} | {round(time * 1000, 5):<10} |"
                    )
                print_table_divider(55)


if __name__ == "__main__":
    main()
