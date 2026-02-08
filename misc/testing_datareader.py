def main():
    print("Hello from codingassessment-02-08-26!")
    import pandas_datareader as pdr

    fred_data = pdr.get_data_fred("CNP160V")
    print(fred_data)


if __name__ == "__main__":
    main()
