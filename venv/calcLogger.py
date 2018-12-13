import logging
import Zad3

def main ():
    logging.basicConfig ( filename = 'app.log' , level = logging.DEBUG )
    logging.info ( 'Started 2 + 3' )
    Zad3.btnPress(2)
    Zad3.btnPress('+')
    Zad3.btnPress(3)

    logging.info( 'Equal : ' + Zad3.EqualPress())
    logging.debug ( 'Ended properly')
if __name__ == '__main__':
        main ()