import sys

def read_input():
    num_total = int(input())
    stock_list = input().split(" ")
    num_req = int(input())
    req_list = input().split(" ")

    return num_total, stock_list, num_req, req_list

def not_enough_in_stock(num_required, num_total):
    return num_required > num_total


def convert_tshirt_list_to_dict(tshirt_list):
    tshirt_dict = {"S": {}, "M": {}, "L": {}}
    for size in tshirt_list:
        key = len(size) - 1
        if key in tshirt_dict[size[-1]]:
            tshirt_dict[size[-1]][key] += 1
        else:
            tshirt_dict[size[-1]][key] = 1
    return tshirt_dict

def check_large_availability(stock_large_dict, req_large_dict):
    for req_size in req_large_dict:
        if req_size in stock_large_dict:
            if stock_large_dict[req_size] >= req_large_dict[req_size]:
                stock_large_dict[req_size] -= req_large_dict[req_size]
            else:
                req_large_dict[req_size] -= stock_large_dict[req_size]
                stock_large_dict[req_size] = 0

        else:
            for stock_size in stock_large_dict:
                if stock_size > req_size:
                    stock_large_dict[stock_size] -= 1
                else:
                    return False


def check_availability(stock_dict, req_dict):
    if not check_large_availability(stock_dict["L"], req_dict["L"]):
        return False


def separate(size_list):
    l = []
    m = []
    s = []

    for size in size_list:
        if size[-1] == "L":
            l.append(size)
        elif size[-1] == "M":
            m.append(size)
        elif size[-1] == "S":
            s.append(size)
        
    return s, m, l


def main():
    num_total, stock_list, num_req, req_list = read_input()

    if not_enough_in_stock(num_req, num_total):
        print("No")
        sys.exit()

    s, m, l = separate(stock_list)

    print(s)
    print(m)
    print(l)

    # stock_dict = convert_tshirt_list_to_dict(stock_list)
    # req_dict = convert_tshirt_list_to_dict(req_list)

    # if check_availability(stock_dict, req_dict):
    #     print("Yes")
    # else:
    #     print("No")


main()