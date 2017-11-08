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

def meta_func_creator(func, lowercase):
    if lowercase:
        func = func.lower()
    return (lambda *args : run(func, *args))

current_module = __import__(__name__)
meta_funcs = {
        'BarGraph': False,
        'BusyIndicator': False,
        'ButtonBox': False,
        'CheckBox': False,
        'CheckBoxFrame': False,
        'ComboBox': False,
        'DateField': False,
        'DownloadProgress': False,
        'DumbTab': False,
        'Empty': False,
        'Graph': False,
        'Frame': False,
        'HBox': False,
        'VBox': False,
        'HSpacing': False,
        'VSpacing': False,
        'HStretch': False,
        'VStretch': False,
        'HSquash': False,
        'VSquash': False,
        'HVSquash': False,
        'HWeight': False,
        'VWeight': False,
        'Image': False,
        'InputField': False,
        'TextEntry': False,
        'Password': False,
        'IntField': False,
        'Label': False,
        'Heading': False,
        'Left': False,
        'Right': False,
        'Top': False,
        'Bottom': False,
        'HCenter': False,
        'VCenter': False,
        'HVCenter': False,
        'LogView': False,
        'MarginBox': False,
        'MenuButton': False,
        'MinWidth': False,
        'MinHeight': False,
        'MinSize': False,
        'MultiLineEdit': False,
        'MultiSelectionBox': False,
        'PackageSelector': False,
        'PartitionSplitter': False,
        'PatternSelector': False,
        'ProgressBar': False,
        'PushButton': False,
        'RadioButton': False,
        'RadioButtonGroup' : False,
        'ReplacePoint': False,
        'RichText': False,
        'SelectionBox': False,
        'SimplePatchSelector' : False,
        'Slider': False,
        'Table': False,
        'Header' : True,
        'Item' : True,
        'TimeField': False,
        'TimezoneSelector': False,
        'Tree': False,
        'VMultiProgressMeter': False,
        'HMultiProgressMeter': False,
        'Cell': False,
        'Center': False,
        'ColoredLabel': False,
        'Dummy': False,
        'DummySpecialWidget': False,
        'HVStretch': False,
        'IconButton': False,
        'PkgSpecial': False,
       }

for func in meta_funcs.keys():
    #print "adding %s"%func
    setattr(current_module, func, meta_func_creator(func, meta_funcs[func]))
