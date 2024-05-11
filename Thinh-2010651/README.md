# Lưu Quốc Hưng Thịnh - 2010651

## Cài đặt các packet

Để chạy được chương trình ta cần phải cài các gói trong file requirements.txt. Bằng câu lệnh:

```bash
pip install -r requirements.txt
```

## Cấu trúc source code

* Folder Login: Chứa code chức năng Chấm điểm
  * Level0: Chứa các file được sinh ra bởi selenium IDE
  * Level1: Chứa code và file.csv - data file của chức năng đăng nhập ở level1

* Folder PrivateFile: Chứa code của chức năng Đăng bài trong một diễn đàn
  * Level0: Chứa các file được sinh ra bởi selenium IDE
  * Level1: Chứa code và file.csv - data file của chức năng private file ở level1

## Run code

```bash
cd Login
```

```bash
python Level1/test_login.py;
```
