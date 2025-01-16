class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def utility_message():
        print("This is a static utility method.")

Counter.increment()
Counter.increment()
print(f"Count: {Counter.count}")
Counter.utility_message()
