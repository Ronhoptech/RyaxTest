def handle(req):
    data_file = req.get('data_path')
    print(f"Got file: {data_file}")
    return 0
