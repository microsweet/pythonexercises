def make_album(singer, cdname):
    print('singer' + singer + ': ' + cdname)

while True:
    print('please input singer and cdname')
    print('enter "q" at anytime to quit')

    singer = input('singer')
    if(singer == 'q'):
        break

    cdname = input("cdname")
    if(cdname == 'q'):
        break

    make_album(singer, cdname)

