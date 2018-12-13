# coding : utf -8
import liczby
class Test ( object ):
    def test_answer_type ( self ):
        assert isinstance ( liczby.num2text (1) ,str )
    def test_zero ( self ):
        assert (liczby.num2text(0) == 'zero')
    def test_one ( self ):
        assert (liczby.num2text(1) == 'jeden')
    def test_two ( self ):
        assert (liczby.num2text(2) == 'dwa')
    def test_three ( self ):
        assert (liczby.num2text(3) == 'trzy')
    def test_four ( self ):
        assert (liczby.num2text(3) == 'cztery')
    def test_default ( self ):
        assert( liczby.num2text(4) == None)