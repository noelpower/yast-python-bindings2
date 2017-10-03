%module ycp2

%feature("autodoc", "3");

%include std_string.i
%inline %{
using namespace std;
%}

%{
#include <ycp-ui/YCP_UI.h>
%}

/* %typemap(in) const YCPString& {
    $1 = YCPString($input);
} */

%feature("valuewrapper") YCPBoolean;
class YCPBoolean;
%feature("valuewrapper") YCPInteger;
class YCPInteger;
%feature("valuewrapper") YCPString;
class YCPString;

%rename(UI) YCP_UI;
%include <ycp-ui/YCP_UI.h>

%ignore YCPTermRep;
%include <ycp/YCPTerm.h>
%ignore YCPListRep;
%include <ycp/YCPList.h>
%ignore YCPStringRep;
%include <ycp/YCPString.h>
%ignore YCPSymbolRep;
%include <ycp/YCPSymbol.h>
%ignore YCPIntegerRep;
%include <ycp/YCPInteger.h>
%ignore YCPBooleanRep;
%include <ycp/YCPBoolean.h>
