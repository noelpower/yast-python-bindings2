from ycp import UI
from ycp import YCPSymbol as Symbol
from ycp import YCPList as List
from ycp import YCPString as String
from ycp import YCPTerm as Term
from ycp import YCPInteger as Integer

class Wizard:
    @staticmethod
    def CreateDialog():
        args = List()
        content = HBox(
            HWeight(1, ReplacePoint(
                PushButton('Help', ID='help', opts=['key_F1', 'helpButton']),
            ID='rep_help')),
            HStretch(),
            HWeight(1, ReplacePoint(
                PushButton('Back', ID='back', opts=['key_F8']),
            ID='rep_back')),
            HStretch(),
            ReplacePoint(
                PushButton('Abort', ID='abort', opts=['key_F9']),
            ID='rep_abort'),
            HStretch(),
            HWeight(1, ReplacePoint(
                PushButton('Next', ID='next', opts=['key_F10', 'default']),
            ID='rep_next')),
        )
        opts = List()
        opts.push_back(Symbol('wizardDialog'))

        UI.OpenDialog(Term('opt', opts), content)

def ButtonBox(ID=None, opts=[]):
    """

    Synopsis
    ButtonBox (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('ButtonBox', result)

def ComboBox(ID=None, opts=[]):
    """

    Synopsis
    ComboBox (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('ComboBox', result)

def DumbTab(ID=None, opts=[]):
    """

    Synopsis
    DumbTab (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('DumbTab', result)

def Frame(ID=None, opts=[]):
    """

    Synopsis
    Frame (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Frame', result)

def HBox(*children):
    """

    Synopsis
    HBox (  );

    Parameters
    """
    result = List()
    for child in children:
        result.push_back(child)
    return Term('HBox', result)

def VBox(ID=None, opts=[]):
    """

    Synopsis
    VBox (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('VBox', result)

def HSpacing(ID=None, opts=[]):
    """

    Synopsis
    HSpacing (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('HSpacing', result)

def VSpacing(ID=None, opts=[]):
    """

    Synopsis
    VSpacing (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('VSpacing', result)

def HStretch(size=None):
    """

    Synopsis
    HStretch (  );

    Parameters
    """
    result = List()
    if size is not None:
        result.push_back(Integer(size))
    return Term('HStretch', result)

def VStretch(ID=None, opts=[]):
    """

    Synopsis
    VStretch (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('VStretch', result)

def HWeight(weight, child):
    """

    Synopsis
    HWeight (  );

    Parameters
    """
    result = List()
    result.push_back(Integer(weight))
    result.push_back(child)
    return Term('HWeight', result)

def InputField(ID=None, opts=[]):
    """

    Synopsis
    InputField (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('InputField', result)

def TextEntry(ID=None, opts=[]):
    """

    Synopsis
    TextEntry (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('TextEntry', result)

def Password(ID=None, opts=[]):
    """

    Synopsis
    Password (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Password', result)

def Label(ID=None, opts=[]):
    """

    Synopsis
    Label (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Label', result)

def Heading(ID=None, opts=[]):
    """

    Synopsis
    Heading (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Heading', result)

def Left(ID=None, opts=[]):
    """

    Synopsis
    Left (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Left', result)

def Right(ID=None, opts=[]):
    """

    Synopsis
    Right (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Right', result)

def Top(ID=None, opts=[]):
    """

    Synopsis
    Top (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Top', result)

def Bottom(ID=None, opts=[]):
    """

    Synopsis
    Bottom (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Bottom', result)

def HCenter(ID=None, opts=[]):
    """

    Synopsis
    HCenter (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('HCenter', result)

def VCenter(ID=None, opts=[]):
    """

    Synopsis
    VCenter (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('VCenter', result)

def HVCenter(ID=None, opts=[]):
    """

    Synopsis
    HVCenter (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('HVCenter', result)

def MinWidth(ID=None, opts=[]):
    """

    Synopsis
    MinWidth (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('MinWidth', result)

def MinHeight(ID=None, opts=[]):
    """

    Synopsis
    MinHeight (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('MinHeight', result)

def MinSize(ID=None, opts=[]):
    """

    Synopsis
    MinSize (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('MinSize', result)

def PushButton(label, ID=None, opts=[]):
    """

    Synopsis
    PushButton (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    result.push_back(String(label))

    return Term('PushButton', result)

def ReplacePoint(child, ID=None, opts=[]):
    """

    Synopsis
    ReplacePoint (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        for opt in opts:
            l = List()
            l.push_back(Symbol(opt))
            result.push_back(Term('opt', l))
    result.push_back(child)

    return Term('ReplacePoint', result)

def RichText(ID=None, opts=[]):
    """

    Synopsis
    RichText (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('RichText', result)

def Table(ID=None, opts=[]):
    """

    Synopsis
    Table (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Table', result)

def Node(ID=None, opts=[]):
    """

    Synopsis
    Node (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Node', result)

def Tree(ID=None, opts=[]):
    """

    Synopsis
    Tree (  );

    Parameters
    """
    result = List()
    if ID is not None:
        l = List()
        l.push_back(String(ID))
        result.push_back(Term('id', l))
    if opts is not None:
        l = List()
        for opt in opts:
            l.push_back(Symbol(opt))
        result.push_back(Term('opt', l))
    return Term('Tree', result)

