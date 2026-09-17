import datetime

def main():
    print("Hello from my GHCR test container!")
    print(f"Current UTC time: {datetime.datetime.utcnow().isoformat()}")

if __name__ == "__main__":
    main()
