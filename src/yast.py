from ycp2 import UI
from ycp2 import YCPSymbol as Symbol
from ycp2 import YCPList
from ycp2 import YCPString as String
from ycp2 import YCPTerm as Term
from ycp2 import YCPInteger as Integer
from ycp2 import YCPBoolean as Boolean
from ycp2 import YCPFloat as Float

class Wizard:
    @staticmethod
    def GenericDialog(button_box):
        return VBox(
            ReplacePoint(Empty(), ID='topmenu'),
            HBox(
                HSpacing(1),
                VBox(
                    VSpacing(0.2),
                    HBox(
                        Heading("Initializing ...", ID='title', opts=['hstretch']),
                        HStretch(),
                        ReplacePoint(Empty(), ID='relnotes_rp')
                    ),
                    VWeight(
                        1,
                        HVCenter(ReplacePoint(Empty(), ID='contents'), opts=['hvstretch'])
                    )
                ),
                HSpacing(1)
            ),
            ReplacePoint(button_box, ID='rep_button_box'),
            VSpacing(0.2),
            ID='WizardDialog'
        )

    @staticmethod
    def BackAbortNextButtonBox():
        return HBox(
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

    @staticmethod
    def CreateDialog():
        content = Wizard.GenericDialog(Wizard.BackAbortNextButtonBox())
        args = List()
        opts = List()
        opts.append(Symbol('wizardDialog'))

        UI.OpenDialog(Term('opt', opts.base()), content)
        UI.SetFocus(String('next'))

    @staticmethod
    def SetContentsButtons(title, contents, help_txt, back_txt, next_txt):
        UI.SetApplicationTitle(String(title))
        UI.ChangeWidget(Symbol('title'), Symbol('Value'), String(title))
        UI.ReplaceWidget(Symbol('contents'), contents)
        UI.ReplaceWidget(Symbol('rep_back'), PushButton(back_txt, ID='back', opts=['key_F8']))
        UI.ReplaceWidget(Symbol('rep_next'), PushButton(next_txt, ID='next', opts=['key_F10', 'default']))

    @staticmethod
    def DisableBackButton():
        pass

    @staticmethod
    def DisableNextButton():
        pass

class List:
    def __init__(self, items=[]):
        self.l = YCPList()
        for item in items:
            self.l.push_back(item)

    def append(self, item):
        if type(item) is list:
            self.l.push_back(List(item).base())
        elif type(item) is str:
            self.l.push_back(String(item))
        elif type(item) is int:
            self.l.push_back(Integer(item))
        elif type(item) is bool:
            self.l.push_back(Boolean(item))
        elif type(item) is float:
            self.l.push_back(Float(item))
        else:
            self.l.push_back(item)

    def extend(self, items):
        for item in items:
            self.l.push_back(item)

    def base(self):
        return self.l

def ButtonBox(buttons, ID=None, opts=[]):
    """Layout for push buttons that takes button order into account

    Synopsis
    ButtonBox ( term button1, term button2 );

    Parameters
    term buttons  list of PushButton items

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.extend(buttons)

    return Term('ButtonBox', result.base())

def ComboBox(label, items=[], ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(String(label))
    options = List()
    for item in items:
        if type(item) is tuple:
            l = List()
            l.append(item[0])
            l.append(item[1])
            options.append(Term('item', l.base()))
        else:
            options.append(String(item))
    result.append(options)

    return Term('ComboBox', result.base())

def DumbTab(tabs, contents, ID=None, opts=[]):
    """Simplistic tab widget that behaves like push buttons

    Synopsis
    DumbTab ( list tabs , term contents );

    Parameters
    list tabs  page headers
    term contents  page contents - usually a ReplacePoint
    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(tabs)
    result.append(contents)

    return Term('DumbTab', result.base())

def Empty():
    return Term('Empty')

def Frame(label, child, ID=None, opts=[]):
    """Frame with label

    Synopsis
    Frame ( string label, term child );

    Parameters
    string label  title to be displayed on the top left edge
    term child  the contained child widget

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)
    result.append(child)

    return Term('Frame', result.base())

def HBox(*children, **kwargs):
    """Generic layout: Arrange widgets horizontally

    Synopsis
    HBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    result = List()
    for key in kwargs:
        if key is 'ID':
            result.append(Term('id', List([Symbol(kwargs[key])]).base()))
        elif key is 'opts':
            l = List()
            for opt in opts:
                l.append(Symbol(opt))
            result.append(Term('opt', l.base()))
        else:
            raise SyntaxError, 'Invalid keyword argument %s' % key
    result.extend(list(children))

    return Term('HBox', result.base())

def VBox(*children, **kwargs):
    """Generic layout: Arrange widgets vertically

    Synopsis
    VBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    result = List()
    for key in kwargs:
        if key is 'ID':
            result.append(Term('id', List([Symbol(kwargs[key])]).base()))
        elif key is 'opts':
            l = List()
            for opt in opts:
                l.append(Symbol(opt))
            result.append(Term('opt', l.base()))
        else:
            raise SyntaxError, 'Invalid keyword argument %s' % key
    result.extend(list(children))

    return Term('VBox', result.base())

def HSpacing(size=None):
    """Fixed size empty space for layout

    Synopsis
    HSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    result = List()
    if size is not None:
        result.append(size)
    return Term('HSpacing', result.base())

def VSpacing(size=None):
    """Fixed size empty space for layout

    Synopsis
    VSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    result = List()
    if size is not None:
        result.append(size)
    return Term('VSpacing', result.base())

def HStretch(size=None):
    """Fixed size empty space for layout

    Synopsis
    HStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    result = List()
    if size is not None:
        result.append(size)
    return Term('HStretch', result.base())

def VStretch(size=None):
    """Fixed size empty space for layout

    Synopsis
    VStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    result = List()
    if size is not None:
        result.append(size)
    return Term('VStretch', result.base())

def HWeight(weight, child):
    """Control relative size of layouts

    Synopsis
    HWeight ( integer weight, term child );

    Parameters
    integer weight  the new weight of the child widget
    term child  the child widget

    """
    result = List()
    result.append(weight)
    result.append(child)
    return Term('HWeight', result.base())

def VWeight(weight, child):
    """Control relative size of layouts

    Synopsis
    VWeight ( integer weight, term child );

    Parameters
    integer weight  the new weight of the child widget
    term child  the child widget

    """
    result = List()
    result.append(weight)
    result.append(child)
    return Term('VWeight', result.base())

def InputField(label, defaulttext=None, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)
    if defaulttext is not None:
        result.append(defaulttext)

    return Term('InputField', result.base())

def TextEntry(label, defaulttext=None, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)
    if defaulttext is not None:
        result.append(defaulttext)

    return Term('TextEntry', result.base())

def Password(label, defaulttext=None, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)
    if defaulttext is not None:
        result.append(defaulttext)

    return Term('Password', result.base())

def Label(label, ID=None, opts=[]):
    """Simple static text

    Synopsis
    Label ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)

    return Term('Label', result.base())

def Heading(label, ID=None, opts=[]):
    """Simple static text

    Synopsis
    Heading ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)

    return Term('Heading', result.base())

def Left(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Left ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('Left', result.base())

def Right(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Right ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('Right', result.base())

def Top(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Top ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('Top', result.base())

def Bottom(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Bottom ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('Bottom', result.base())

def HCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    HCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('HCenter', result.base())

def VCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    VCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('VCenter', result.base())

def HVCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    HVCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(child)
    if pixmap is not None:
        result.append(Term('BackgroundPixmap', pixmap))

    return Term('HVCenter', result.base())

def MinWidth(size, child):
    """Layout minimum size

    Synopsis
    MinWidth ( float|integer size, term child );

    Parameters
    float|integer size  minimum width
    term child  The contained child widget

    """
    result = List()
    result.append(size)
    result.append(child)
    return Term('MinWidth', result.base())

def MinHeight(size, child):
    """Layout minimum size

    Synopsis
    MinHeight ( float|integer size, term child );

    Parameters
    float|integer size  minimum heigh
    term child  The contained child widget

    """
    result = List()
    result.append(size)
    result.append(child)
    return Term('MinHeight', result.base())

def MinSize(width, height, child):
    """Layout minimum size

    Synopsis
    MinSize ( float|integer width, float|integer height, term child );

    Parameters
    float|integer size  minimum width
    float|integer size  minimum height
    term child  The contained child widget

    """
    result = List()
    result.append(width)
    result.append(height)
    result.append(child)
    return Term('MinSize', result.base())

def PushButton(label, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)

    return Term('PushButton', result.base())

def ReplacePoint(child, ID=None, opts=[]):
    """Pseudo widget to replace parts of a dialog

    Synopsis
    ReplacePoint ( term child );

    Parameters
    term child  the child widget
    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        for opt in opts:
            l = List()
            l.append(Symbol(opt))
            result.append(Term('opt', l.base()))
    result.append(child)

    return Term('ReplacePoint', result.base())

def RichText(text, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(text)

    return Term('RichText', result.base())

def Table(header, items=[], ID=None, opts=[]):
    """Multicolumn table widget

    Synopsis
    Table ( term header, list items );

    Parameters
    term header  the headers of the columns

    Optional Arguments
    list items  the items contained in the selection box

    """
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(Term('header', List(header).base()))
    contents = List()
    for item in items:
        if type(item) is list:
            contents.append(Term('item', Term('id', String(item[0])), List(list(item[1])).base()))
        else:
            contents.append(Term('item', List(list(item)).base()))
    result.append(contents.base())

    return Term('Table', result.base())

def Node(label, expanded=False, children=[], ID=None):
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    result.append(label)
    result.append(expanded)
    result.append(children)

    return Term('item', result.base())

def Tree(label, items, ID=None, opts=[]):
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
    result = List()
    if ID is not None:
        result.append(Term('id', List([Symbol(ID)]).base()))
    if opts is not None:
        l = List()
        for opt in opts:
            l.append(Symbol(opt))
        result.append(Term('opt', l.base()))
    result.append(label)
    result.append(items)

    return Term('Tree', result.base())

