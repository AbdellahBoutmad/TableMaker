class HTMLTable:
    def __init__(self):
        self.headers = []
        self.rows = []

    def set_headers(self, headers):
        self.headers = headers

    def add_row(self, row):
        self.rows.append(row)

    def generate_table(self):
        table = "<table>\n"
        if self.headers:
            table += "  <tr>\n"
            for header in self.headers:
                table += f"    <th>{header}</th>\n"
            table += "  </tr>\n"
        
        for row in self.rows:
            table += "  <tr>\n"
            for cell in row:
                table += f"    <td>{cell}</td>\n"
            table += "  </tr>\n"
        
        table += "</table>"
        return table

table = HTMLTable()
table.set_headers(["Company", "Contact", "Country"])
table.add_row(["boutmad shop", "0600000000", "marwicos"])
table.add_row(["boutmad shop", "0600000000", "marwicos"])
table.add_row(["boutmad shop", "0600000000", "marwicos"])
table.add_row(["boutmad shop", "0600000000", "marwicos"])

html_table = table.generate_table()
print(html_table)
