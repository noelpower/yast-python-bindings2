from ycp2 import YCPSymbol as Symbol
from ycp2 import YCPList as List
from ycp2 import YCPString as String
from ycp2 import YCPTerm as Term
from ycp2 import YCPInteger as Integer
from ycp2 import YCPBoolean as Boolean
from ycp2 import YCPFloat as Float
from ycp2 import Id, Opt
from ycp2 import import_module
if import_module('UI'):
    import UI
if import_module('Wizard'):
    import Wizard
if import_module('Sequencer'):
    import Sequencer

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

def run(func, *args):
    from ytypes import pytval_to_ycp
    l = List()
    for item in args:
        l.push_back(pytval_to_ycp(item))
    return Term(func, l)

current_module = __import__(__name__)
meta_funcs = [
      'BarGraph',
      'BusyIndicator',
      'Bottom',
      'ButtonBox',
      'Cell',
      'Center',
      'CheckBox',
      'CheckBoxFrame',
      'ColoredLabel',
      'ComboBox',
      'DateField',
      'DownloadProgress',
      'DumbTab',
      'Dummy',
      'DummySpecialWidget',
      'Empty',
      'Frame',
      'Graph',
      'HBox',
      'HCenter',
      'HMultiProgressMeter',
      'HSpacing',
      'HSquash',
      'HStretch',
      'HVCenter',
      'HVSquash',
      'HVStretch',
      'HWeight',
      'Header',
      'Heading',
      'IconButton',
      'Image',
      'InputField',
      'IntField',
      'Item',
      'Label',
      'Left',
      'LogView',
      'MarginBox',
      'MenuButton',
      'MinHeight',
      'MinSize',
      'MinWidth',
      'MultiLineEdit',
      'MultiSelectionBox',
      'PackageSelector',
      'PatternSelector',
      'PartitionSplitter',
      'Password',
      'PkgSpecial',
      'ProgressBar',
      'PushButton',
      'RadioButton',
      'RadioButtonGroup',
      'ReplacePoint',
      'RichText',
      'Right',
      'SelectionBox',
      'SimplePatchSelector',
      'Slider',
      'Table',
      'TextEntry',
      'TimeField',
      'TimezoneSelector',
      'Top',
      'Tree',
      'VBox',
      'VCenter',
      'VMultiProgressMeter',
      'VSpacing',
      'VSquash',
      'VStretch',
      'VWeight'
       ]

for func in meta_funcs:
    #print "adding %s"%func
    setattr(current_module, func, (lambda *args : run(func, *args)))
