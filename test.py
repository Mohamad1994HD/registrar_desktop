from excelsheet import Controller


if __name__ == '__main__':

    c = Controller('sheet.xlsx', new_file=True)
    assert(c.append(['yamen2haddad@gmail.com', '0533', 'Syria']) is True)

    c = Controller('sheet.xlsx')
    assert(c.append(['mohd2haddad@gmail.com', '0533', 'Syria']) is True)
    
    print "done"

