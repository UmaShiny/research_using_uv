import win32com.client as _com


def excel_show_docs() -> None:
    """Show all opened Excel documents."""
    excel = _com.Dispatch("Excel.Application")
    text = excel.Release.__doc__
    print(text)


if __name__ == "__main__":
    excel_show_docs()
