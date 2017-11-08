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

def meta_func_creator(func):
    return (lambda *args : run(func, *args))

current_module = __import__(__name__)
meta_funcs = [
      'BarGraph',
      'BusyIndicator',
      'ButtonBox',
      'CheckBox',
      'CheckBoxFrame',
      'ComboBox',
      'DateField',
      'DownloadProgress',
      'DumbTab',
      'Empty',
      'Graph',
      'Frame',
      'HBox',
      'VBox',
      'HSpacing',
      'VSpacing',
      'HStretch',
      'VStretch',
      'HSquash',
      'VSquash',
      'HVSquash',
      'HWeight',
      'VWeight'
      'Image',
      'InputField',
      'TextEntry',
      'Password',
      'IntField',
      'Label',
      'Heading',
      'Left',
      'Right',
      'Top',
      'Bottom',
      'HCenter',
      'VCenter',
      'HVCenter',
      'LogView',
      'MarginBox',
      'MenuButton',
      'MinWidth',
      'MinHeight',
      'MinSize',
      'MultiLineEdit',
      'MultiSelectionBox',
      'PackageSelector',
      'PartitionSplitter',
      'PatternSelector',
      'ProgressBar',
      'PushButton',
      'RadioButton',
      'RadioButtonGroup',
      'ReplacePoint',
      'RichText',
      'SelectionBox',
      'SimplePatchSelector',
      'Slider',
      'Table',
      'Header',
      'Item',
      'TimeField',
      'TimezoneSelector',
      'Tree',
      'VMultiProgressMeter',
      'HMultiProgressMeter',
      'Cell',
#      'Center',
#      'ColoredLabel',
#      'Dummy',
#      'DummySpecialWidget',
#      'HVStretch',
#      'IconButton',
#      'PkgSpecial',
       ]

for func in meta_funcs:
    #print "adding %s"%func
    setattr(current_module, func, meta_func_creator(func))
