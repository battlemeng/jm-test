
def download_jm(page, path, name):
    with page.expect_download() as download_info:
        page.get_by_role("button", name=name).click()
    download = download_info.value
    download.save_as(path + download.suggested_filename)



def upload_jm(page, upload_file, name):
    with page.expect_file_chooser() as upload_info:
        page.get_by_label(name).click()
    upload = upload_info.value
    upload.set_files(upload_file)
