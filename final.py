from tabulate import tabulate

class HouseholdBill:
    def __init__(self, id, owner_name , address , electric_usage , electric_price , water_usage , water_price , service_fee):
        self.id = id
        self.owner_name = owner_name
        self.address = address
        self.electric_usage = electric_usage
        self.electric_price = electric_price
        self.water_usage = water_usage
        self.water_price = water_price
        self.service_fee = service_fee

        self.total_bill  = 0
        self.bill_type  = ""

        self.calculate_total_bill()
        self.classify_bill()

    def calculate_total_bill(self):
        self.total_bill = (self.electric_usage * self.electric_price) + (self.water_usage * self.water_price) + self.service_fee

    def classify_bill(self):
        if self.total_bill >= 3000000:
            self.bill_type = "Rất cao"
        elif self.total_bill >= 1500000:
            self.bill_type = "Cao"
        elif self.total_bill >= 500000:
            self.bill_type = "Trung bình"
        else:
            self.bill_type = "Thấp"

class HouseholdBillManager:
    def __init__(self):
        self.bills = [
            HouseholdBill("H01", "Nguyen A", "Ha Noi", 35, 4000, 5, 30000, 50000),
            HouseholdBill("H02", "Le B", "Hai Phong", 30, 5000, 6, 32000, 60000),
            HouseholdBill("H03", "Tran C", "TP HCM", 45, 4000, 8, 25000, 45000)
        ]

    def show_all(self):
        if self.bills == []:
            print("Danh sách hóa đơn điện nước đang rỗng!")
            return
        
        data = []

        for bill in self.bills:
            data.append([
                bill.id,
                bill.owner_name,
                bill.address,
                bill.electric_usage,
                bill.electric_price,
                bill.water_usage,
                bill.water_price,
                bill.service_fee,
                bill.total_bill,
                bill.bill_type
            ])
        print(tabulate(data, headers= ["Mã hộ gia đình", "Tên chủ hộ", "Địa chỉ", "Số điện", "Đơn giá điện", "Số nước", "Đơn giá nước", "Phí dịch vụ", "Tổng tiền", "Phân loại chi phí"], tablefmt="fancy_grid"))

    def duplicate_id(self, input_id):
        for bill in self.bills:
            if bill.id == input_id:
                return bill # tồn tại
        return None
        
    def empty_value(self, input_value):
        while True:
            try:
                value = input(input_value)
                if value == "":
                    print("Giá trị nhập vào không được để trống")
                    continue
                return value
            except ValueError:
                print("Giá trị nhập vào không hợp lệ")

    def validate_float(self, input_float):
        while True:
            try:
                value = float(input(input_float))
                if value < 0:
                    print("Giá trị nhập vào phải lớn hơn bằng 0")
                    continue
                return value
            except ValueError:
                print("Giá trị nhập vào không hợp lệ")

    def add_bill(self):
        input_id = self.empty_value("Nhập mã hộ gia đình: ").strip().upper()
        if self.duplicate_id(input_id) is not None:
            print("Mã hộ gia đình đã tồn tại")
            return
        
        input_owner_name = self.empty_value("Nhập tên chủ hộ: ").strip()
        input_address = self.empty_value("Nhập địa chỉ: ").strip()
        input_electric_usage = self.validate_float("Nhập số điện đã sử dụng: ")
        input_electric_price = self.validate_float("Nhập giá điện: ")
        input_water_usage = self.validate_float("Nhập số nước đã sử dụng: ")
        input_water_price = self.validate_float("Nhập giá nước: ")
        input_service_fee = self.validate_float("Nhập phí dịch vụ: ")

        new_bill = HouseholdBill(
            input_id,
            input_owner_name,
            input_address,
            input_electric_usage,
            input_electric_price,
            input_water_usage,
            input_water_price,
            input_service_fee,
        )

        self.bills.append(new_bill)
        print("Thêm hóa đơn thành công")

    def update_bill(self):
        input_id = self.empty_value("Nhập mã hộ gia đình: ").strip().upper()
        if self.duplicate_id(input_id) is None:
            print("Không tìm thấy hóa đơn điện nước cần cập nhật!")
            return
        
        for bill in self.bills:
            if self.duplicate_id(input_id) is not None:
                bill.electric_usage = self.validate_float("Nhập số điện đã sử dụng: ")
                bill.electric_price = self.validate_float("Nhập giá điện: ")
                bill.water_usage = self.validate_float("Nhập số nước đã sử dụng: ")
                bill.water_price = self.validate_float("Nhập giá nước: ")
                bill.service_fee = self.validate_float("Nhập phí dịch vụ: ")

                bill.calculate_total_bill()
                bill.classify_bill()
                print("Cập nhật hóa đơn thành công")
                return

    def del_bill(self):
        input_id = self.empty_value("Nhập mã hộ gia đình: ").strip().upper()
        if self.duplicate_id(input_id) is None:
            print("Không tìm thấy hóa đơn điện nước cần xóa!")
            return

        if self.duplicate_id(input_id) is not None:
            while True:
                option = input("Bạn có chắc muốn xóa hóa đơn điện nước này không? (Y/N): ").upper()
                if option == "Y":
                    self.bills.remove(self.duplicate_id(input_id))
                    print("Xóa hóa đơn thành công")
                    return
                elif option == "N":
                    print("Hủy xóa hóa đơn thành công")
                    return
                else:
                    print("Lựa chọn không hợp lệ")
                
    def search_bill(self):
        input_value = self.empty_value("Nhập tên chủ hộ hoặc địa chỉ: ").strip().upper()

        result = []

        for bill in self.bills:
            if input_value in bill.owner_name.upper() or input_value in bill.address.upper():
                result.append([
                    bill.id,
                    bill.owner_name,
                    bill.address,
                    bill.electric_usage,
                    bill.electric_price,
                    bill.water_usage,
                    bill.water_price,
                    bill.service_fee,
                    bill.total_bill,
                    bill.bill_type
                ])
                print(tabulate(result, headers= ["Mã hộ gia đình", "Tên chủ hộ", "Địa chỉ", "Số điện", "Đơn giá điện", "Số nước", "Đơn giá nước", "Phí dịch vụ", "Tổng tiền", "Phân loại chi phí"], tablefmt="fancy_grid" ))
            break
        
        if result == []:
            print("không tìm thấy chủ hộ phù hợp!")
        return

    def main(self):
        while True:
            choice = input(
"""
================ MENU ================
1. Hiển thị danh sách hóa đơn điện nước
2. Thêm hóa đơn điện nước mới
3. Cập nhật hóa đơn điện nước
4. Xóa hóa đơn điện nước
5. Tìm kiếm hóa đơn
6. Thoát
=====================================
Nhập lựa chọn của bạn: """
)
            if not choice.isdigit():
                print("Vui lòng nhập lựa chọn là số")
                continue

            choice = int(choice)

            match choice:
                case 1:
                    self.show_all()
                case 2:
                    self.add_bill()
                case 3:
                    self.update_bill()
                case 4:
                    self.del_bill()
                case 5:
                    self.search_bill()
                case 6:
                    print("Cảm ơn bạn đã sử dụng hệ thống quản lý điện nước hộ gia đình!")
                    break
                case _:
                    print("Lựa chọn không hợp lệ")

main = HouseholdBillManager()
main.main()
