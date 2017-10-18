from ycp2 import UI
from ycp2 import YCPSymbol as Symbol
from ycp2 import YCPList as List
from ycp2 import YCPString as String
from ycp2 import YCPTerm as Term
from ycp2 import YCPInteger as Integer
from ycp2 import YCPBoolean as Boolean
from ycp2 import YCPFloat as Float
from ycp2 import Id, Opt

class UISequencer:
    def __init__(self, *cli_args):
        self.cli_args = cli_args

    def run(self, funcs):
        Wizard.CreateDialog()

        for func in funcs:
            ret = func(*self.cli_args)
            if type(ret) is tuple:
                data, ret = ret
                self.cli_args = (data,) + self.cli_args
            if str(ret) == 'next':
                continue
            elif str(ret) == 'abort':
                break

        UI.CloseDialog()

class Wizard:
    @staticmethod
    def GenericDialog(button_box):
        return VBox(
            Id('WizardDialog'),
            ReplacePoint(Id('topmenu'), Empty()),
            HBox(
                HSpacing(1),
                VBox(
                    VSpacing(0.2),
                    HBox(
                        Heading(Id('title'), Opt('hstretch'), "Initializing ..."),
                        HStretch(),
                        ReplacePoint(Id('relnotes_rp'), Empty())
                    ),
                    VWeight(
                        1,
                        HVCenter(Opt('hvstretch'), ReplacePoint(Id('contents'), Empty()))
                    )
                ),
                HSpacing(1)
            ),
            ReplacePoint(Id('rep_button_box'), button_box),
            VSpacing(0.2)
        )

    @staticmethod
    def BackAbortNextButtonBox():
        return HBox(
            HWeight(1, ReplacePoint(Id('rep_help'),
                PushButton(Id('help'), Opt('key_F1', 'helpButton'), 'Help')
            )),
            HStretch(),
            HWeight(1, ReplacePoint(Id('rep_back'),
                PushButton(Id('back'), Opt('key_F8'), 'Back')
            )),
            HStretch(),
            ReplacePoint(Id('rep_abort'),
                PushButton(Id('abort'), Opt('key_F9'), 'Abort')
            ),
            HStretch(),
            HWeight(1, ReplacePoint(Id('rep_next'),
                PushButton(Id('next'), Opt('key_F10', 'default'), 'Next')
            )),
        )

    @staticmethod
    def CreateDialog():
        content = Wizard.GenericDialog(Wizard.BackAbortNextButtonBox())
        UI.OpenDialog(content, Opt('wizardDialog'))
        UI.SetFocus('next')

    @staticmethod
    def SetContentsButtons(title, contents, help_txt, back_txt, next_txt):
        #UI.SetApplicationTitle(title)
        UI.ChangeWidget('title', 'Value', String(title))
        UI.ReplaceWidget('contents', contents)
        UI.ReplaceWidget('rep_back', PushButton(Id('back'), Opt('key_F8'), back_txt))
        UI.ReplaceWidget('rep_next', PushButton(Id('next'), Opt('key_F10', 'default'), next_txt))

    @staticmethod
    def DisableBackButton():
        pass

    @staticmethod
    def DisableNextButton():
        pass

    @staticmethod
    def EnableNextButton():
        pass

    @staticmethod
    def DisableAbortButton():
        pass

def ytype(item):
    if type(item) is list:
        sl = List()
        for si in item:
            sl.push_back(ytype(si))
        return sl
    elif type(item) is str:
        return String(item)
    elif type(item) is int:
        return Integer(item)
    elif type(item) is bool:
        return Boolean(item)
    elif type(item) is float:
        return Float(item)
    elif type(item) in [Term, Symbol, String, Integer, Boolean, Float, List]:
        return item
    else:
        raise SyntaxError, 'Type of value "%s" unrecognized, %s' % (item, str(type(item)))

def run(func, *args):
    l = List()
    for item in args:
        l.push_back(ytype(item))
    return Term(func, l)

def ButtonBox(*args):
    """Layout for push buttons that takes button order into account

    Synopsis
    ButtonBox ( term button1, term button2 );

    Parameters
    term buttons  list of PushButton items

    """
    return run('ButtonBox', *args)

def ComboBox(*args):
    """drop-down list selection (optionally editable)

    Synopsis
    ComboBox ( string label, list items );

    Parameters
    string label

    Options
    editable  the user can enter any value.

    Optional Arguments
    list items  the items contained in the combo box

    """
    return run('ComboBox', *args)

def DumbTab(*args):
    """Simplistic tab widget that behaves like push buttons

    Synopsis
    DumbTab ( list tabs , term contents );

    Parameters
    list tabs  page headers
    term contents  page contents - usually a ReplacePoint
    """
    return run('DumbTab', *args)

def Empty():
    return Term('Empty')

def Frame(*args):
    """Frame with label

    Synopsis
    Frame ( string label, term child );

    Parameters
    string label  title to be displayed on the top left edge
    term child  the contained child widget

    """
    return run('Frame', *args)

def HBox(*args):
    """Generic layout: Arrange widgets horizontally

    Synopsis
    HBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    return run('HBox', *args)

def VBox(*args):
    """Generic layout: Arrange widgets vertically

    Synopsis
    VBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    return run('VBox', *args)

def HSpacing(*args):
    """Fixed size empty space for layout

    Synopsis
    HSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    return run('HSpacing', *args)

def VSpacing(*args):
    """Fixed size empty space for layout

    Synopsis
    VSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    return run('VSpacing', *args)

def HStretch(*args):
    """Fixed size empty space for layout

    Synopsis
    HStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    return run('HStretch', *args)

def VStretch(*args):
    """Fixed size empty space for layout

    Synopsis
    VStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    return run('VStretch', *args)

def HWeight(*args):
    """Control relative size of layouts

    Synopsis
    HWeight ( integer weight, term child );

    Parameters
    integer weight  the new weight of the child widget
    term child  the child widget

    """
    return run('HWeight', *args)

def VWeight(*args):
    """Control relative size of layouts

    Synopsis
    VWeight ( integer weight, term child );

    Parameters
    integer weight  the new weight of the child widget
    term child  the child widget

    """
    return run('VWeight', *args)

def InputField(*args):
    """Input field

    Synopsis
    InputField ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    return run('InputField', *args)

def TextEntry(*args):
    """Input field

    Synopsis
    TextEntry ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    return run('TextEntry', *args)

def Password(*args):
    """Input field

    Synopsis
    Password ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    return run('Password', *args)

def Label(*args):
    """Simple static text

    Synopsis
    Label ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    return run('Label', *args)

def Heading(*args):
    """Simple static text

    Synopsis
    Heading ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    return run('Heading', *args)

def Left(*args):
    """Layout alignment

    Synopsis
    Left ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('Left', *args)

def Right(*args):
    """Layout alignment

    Synopsis
    Right ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('Right', *args)

def Top(*args):
    """Layout alignment

    Synopsis
    Top ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('Top', *args)

def Bottom(*args):
    """Layout alignment

    Synopsis
    Bottom ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('Bottom', *args)

def HCenter(*args):
    """Layout alignment

    Synopsis
    HCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('HCenter', *args)

def VCenter(*args):
    """Layout alignment

    Synopsis
    VCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('VCenter', *args)

def HVCenter(*args):
    """Layout alignment

    Synopsis
    HVCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    return run('HVCenter', *args)

def MinWidth(*args):
    """Layout minimum size

    Synopsis
    MinWidth ( float|integer size, term child );

    Parameters
    float|integer size  minimum width
    term child  The contained child widget

    """
    return run('MinWidth', *args)

def MinHeight(*args):
    """Layout minimum size

    Synopsis
    MinHeight ( float|integer size, term child );

    Parameters
    float|integer size  minimum heigh
    term child  The contained child widget

    """
    return run('MinHeight', *args)

def MinSize(*args):
    """Layout minimum size

    Synopsis
    MinSize ( float|integer width, float|integer height, term child );

    Parameters
    float|integer size  minimum width
    float|integer size  minimum height
    term child  The contained child widget

    """
    return run('MinSize', *args)

def PushButton(*args):
    """Perform action on click

    Synopsis
    PushButton ( string label );

    Parameters
    string label

    Options
    default  makes this button the dialogs default button
    helpButton  automatically shows topmost `HelpText
    okButton  assign the [OK] role to this button (see ButtonBox)
    cancelButton  assign the [Cancel] role to this button (see ButtonBox)
    applyButton  assign the [Apply] role to this button (see ButtonBox)
    customButton  override any other button role assigned to this button

    """
    return run('PushButton', *args)

def ReplacePoint(*args):
    """Pseudo widget to replace parts of a dialog

    Synopsis
    ReplacePoint ( term child );

    Parameters
    term child  the child widget
    """
    return run('ReplacePoint', *args)

def RichText(*args):
    """Static text with HTML-like formatting

    Synopsis
    RichText ( string text );

    Parameters
    string text

    Options
    plainText  don't interpret text as HTML
    autoScrollDown  automatically scroll down for each text change
    shrinkable  make the widget very small

    """
    return run('RichText', *args)

def Table(*args):
    """Multicolumn table widget

    Synopsis
    Table ( term header, list items );

    Parameters
    term header  the headers of the columns

    Optional Arguments
    list items  the items contained in the selection box

    """
    return run('Table', *args)

def Header(*args):
    return run('header', *args)

def Item(*args):
    return run('item', *args)

def Tree(*args):
    """Scrollable tree selection

    Synopsis
    Tree ( string label );

    Parameters
    string label

    Options
    immediate  make `notify trigger immediately when the selected item changes

    Optional Arguments
    itemList items  the items contained in the tree

    """
    return run('Tree', *args)

