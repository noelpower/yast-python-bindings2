#include <y2/Y2Namespace.h>
#include <y2/Y2Component.h>
#include <y2/Y2ComponentCreator.h>
#include <ycp/y2log.h>
#include <ycp/YBlock.h>
#include <ycp/YExpression.h>
#include <ycp/YStatement.h>
#include <ycp/Import.h>
#include <ycp-ui/YUIComponent.h>
#include <wfm/Y2WFMComponent.h>
#include <ycp/Parser.h>
#include <ycp/YCPMap.h>
#include <ycp/YCPList.h>
#include <ycp/YCPPath.h>
#include <ycp/YCPTerm.h>
#include <ycp/YCPString.h>
#include <ycp/YCPVoid.h>
#include <ycp/SymbolTable.h>

#include <string>
#include <vector>
#include <cstdarg>
using namespace std;

class Wizard
{
public:
    static void CreateDialog();
    static void SetContentsButtons(const string &, const YCPValue &, const string &, const string &, const string &);
    static void DisableBackButton();
    static void DisableNextButton();
    static void EnableNextButton();
    static void DisableAbortButton();
};

bool init_ui(const string & ui_name);
