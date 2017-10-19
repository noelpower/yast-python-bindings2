#include <YCP_UI.h>
#include <cstdarg>
#include <string>
using namespace std;

YCPTerm Id(string id);
YCPTerm Opt(char * opt, ...);

class UI
{
public:
    //
    // UI Built-ins. Each function directly corresponds to a YCP UI::Something() call.
    //
    // See the documentation at the function definitions for details
    //

    static string AskForExistingDirectory		( const string & startDir, const string & headline );
    static string AskForExistingFile		( const string & startDir, const string & filter, const string & headline );
    static string AskForSaveFileName		( const string & startDir, const string & filter, const string & headline );
    static void 	BusyCursor			();
    static void 	Beep     			();
    static bool ChangeWidget			( const string & widgetId, const string & property, const YCPValue & new_value );
    static void 	CheckShortcuts			();
    static bool CloseDialog			();
    static void 	CloseUI				();
    static void 	DumpWidgetTree			();
    static void 	FakeUserInput			( const YCPValue & nextInput );
    static YCPMap 	GetDisplayInfo			();
    static string 	GetLanguage			( const bool & stripEncoding );
    static string 	GetProductName			();
    static string 	Glyph				( const string & symbol );
    static bool HasSpecialWidget		( const string & widget );
    static void 	MakeScreenShot			( const string & filename );
    static void 	NormalCursor			();
    static bool 	OpenContextMenu			( const YCPTerm & term );
    static bool 	OpenDialog			( const YCPTerm & dialogTerm, const YCPTerm & opts = YCPNull() );
    static void 	OpenUI				();
    static void 	PlayMacro			( const string & filename );
    static void 	PostponeShortcutCheck		();
    static string QueryWidget			( const string & widgetId, const string & property );
    static void 	RecalcLayout			();
    static YCPString Recode				( const string & fromEncoding, const string & toEncoding, const string & text );
    static void 	RecordMacro			( const string & fileName );
    static void 	RedrawScreen			();
    static bool 	ReplaceWidget			( const string & widgetId, const YCPTerm & term );
    static YCPValue 	RunPkgSelection			( const YCPValue & widgetId );
    static void 	SetConsoleFont			( const string & magic,
							  const string & font,
							  const string & screen_map,
							  const string & unicode_map,
							  const string & encoding );
    static void 	SetKeyboard			();
    static int 	RunInTerminal			( const string & module);
    static bool 	SetFocus			( const string & widgetId );
    static void 	SetFunctionKeys			( const YCPMap & functionKeyMap );
    static void 	SetLanguage			( const string & lang, const string & encoding = NULL );
    static void 	SetProductName			( const string & name );
    static void 	StopRecordMacro			();
    static bool 	WidgetExists			( const string & widgetId );
    static string UserInput			();
    static string TimeoutUserInput		( const int & timeout );
    static map<string, string> WaitForEvent			( const int & timeout = 0 );
    static bool WizardCommand			( const YCPTerm & command );
    static string PollInput			();
    static bool	TextMode			();
    static YCPValue	SetReleaseNotes			( const YCPMap & relnotes );
    static YCPValue	SetProductLogo			( const bool & show_logo);
    static YCPValue	SetApplicationIcon      	( const string & icon);
/*    static YCPValue	SetApplicationTitle      	( const string & text); */

};
