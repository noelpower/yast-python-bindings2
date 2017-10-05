#include "wrap.h"


string UI::AskForExistingDirectory(const string & startDir, const string & headline) {
	return YCP_UI::AskForExistingDirectory(YCPString(startDir), YCPString(headline))->asString()->value();
}

string UI::AskForExistingFile(const string & startDir, const string & filter, const string & headline) {
	return YCP_UI::AskForExistingFile(YCPString(startDir), YCPString(filter), YCPString(headline))->asString()->value();
}

string UI::AskForSaveFileName(const string & startDir, const string & filter, const string & headline) {
	return YCP_UI::AskForSaveFileName(YCPString(startDir), YCPString(filter), YCPString(headline))->asString()->value();
}

void UI::BusyCursor() {
	YCP_UI::BusyCursor();
}

void UI::Beep() {
	YCP_UI::Beep();
}

bool UI::ChangeWidget(const string & widgetId, const string & property, const YCPValue & new_value) {
	return YCP_UI::ChangeWidget(YCPSymbol(widgetId)->asValue(), YCPSymbol(property)->asValue(), new_value)->asBoolean()->value();
}

void UI::CheckShortcuts() {
	YCP_UI::CheckShortcuts();
}

bool UI::CloseDialog() {
	return YCP_UI::CloseDialog()->asBoolean()->value();
}

void UI::CloseUI() {
	YCP_UI::CloseUI();
}

void UI::DumpWidgetTree() {
	YCP_UI::DumpWidgetTree();
}

void UI::FakeUserInput(const YCPValue & nextInput) {
	YCP_UI::FakeUserInput(nextInput);
}

YCPMap UI::GetDisplayInfo() {
	return YCP_UI::GetDisplayInfo();
}

string UI::GetLanguage(const bool & stripEncoding) {
	return YCP_UI::GetLanguage(YCPBoolean(stripEncoding))->value();
}

string UI::GetProductName() {
	return YCP_UI::GetProductName()->value();
}

string UI::Glyph(const string & symbol) {
	return YCP_UI::Glyph(YCPSymbol(symbol))->value();
}

bool UI::HasSpecialWidget(const string & widget) {
	return YCP_UI::HasSpecialWidget(YCPSymbol(widget))->asBoolean()->value();
}

void UI::MakeScreenShot(const string & filename) {
	YCP_UI::MakeScreenShot(YCPString(filename));
}

void UI::NormalCursor() {
	YCP_UI::NormalCursor();
}

bool UI::OpenContextMenu(const YCPTerm & term) {
	return YCP_UI::OpenContextMenu(term)->value();
}

bool UI::OpenDialog(const YCPTerm & opts, const YCPTerm & dialogTerm) {
	return YCP_UI::OpenDialog(opts, dialogTerm)->value();
}

void UI::OpenUI() {
	YCP_UI::OpenUI();
}

void UI::PlayMacro(const string & filename) {
	YCP_UI::PlayMacro(YCPString(filename));
}

void UI::PostponeShortcutCheck() {
	YCP_UI::PostponeShortcutCheck();
}

string UI::QueryWidget(const string & widgetId, const string & property) {
	YCPValue val = YCP_UI::QueryWidget(YCPSymbol(widgetId)->asValue(), YCPSymbol(property)->asValue());
	if (val->isSymbol())
		return val->asSymbol()->symbol();
	else if (val->isString())
		return val->asString()->value();
	return "";
}

void UI::RecalcLayout() {
	YCP_UI::RecalcLayout();
}

YCPString UI::Recode(const string & fromEncoding, const string & toEncoding, const string & text) {
	return YCP_UI::Recode(YCPString(fromEncoding), YCPString(toEncoding), YCPString(text))->asString();
}

void UI::RecordMacro(const string & fileName) {
	YCP_UI::RecordMacro(YCPString(fileName));
}

void UI::RedrawScreen() {
	YCP_UI::RedrawScreen();
}

bool UI::ReplaceWidget(const string & widgetId, const YCPTerm & term) {
	return YCP_UI::ReplaceWidget(YCPSymbol(widgetId)->asValue(), term)->value();
}

YCPValue UI::RunPkgSelection(const YCPValue & widgetId) {
	return YCP_UI::RunPkgSelection(widgetId);
}

void UI::SetConsoleFont(const string & magic, const string & font, const string & screen_map, const string & unicode_map, const string & encoding) {
	YCP_UI::SetConsoleFont(YCPString(magic), YCPString(font), YCPString(screen_map), YCPString(unicode_map), YCPString(encoding));
}

void UI::SetKeyboard() {
	YCP_UI::SetKeyboard();
}

int UI::RunInTerminal(const string & module) {
	return YCP_UI::RunInTerminal(YCPString(module))->value();
}

bool UI::SetFocus(const string & widgetId) {
	return YCP_UI::SetFocus(YCPSymbol(widgetId)->asValue())->value();
}

void UI::SetFunctionKeys(const YCPMap & functionKeyMap) {
	YCP_UI::SetFunctionKeys(functionKeyMap);
}

void UI::SetLanguage(const string & lang, const string & encoding) {
	YCP_UI::SetLanguage(YCPString(lang), YCPString(encoding));
}

void UI::SetProductName(const string & name) {
	YCP_UI::SetProductName(YCPString(name));
}

void UI::StopRecordMacro() {
	YCP_UI::StopRecordMacro();
}

bool UI::WidgetExists(const string & widgetId) {
	return YCP_UI::WidgetExists(YCPSymbol(widgetId)->asValue())->value();
}

string UI::UserInput() {
	YCPValue val = YCP_UI::UserInput();
	if (val->isSymbol())
		return val->asSymbol()->symbol();
	else if (val->isString())
		return val->asString()->value();
	return "";
}

string UI::TimeoutUserInput(const int & timeout) {
	return YCP_UI::TimeoutUserInput(YCPInteger(timeout))->asSymbol()->symbol();
}

YCPMap UI::WaitForEvent(const int & timeout) {
	return YCP_UI::WaitForEvent(YCPInteger(timeout))->asMap();
}

bool UI::WizardCommand(const YCPTerm & command) {
	return YCP_UI::WizardCommand(command)->asBoolean()->value();
}

string UI::PollInput() {
	return YCP_UI::PollInput()->asSymbol()->symbol();
}

bool UI::TextMode() {
	return YCP_UI::TextMode()->value();
}

YCPValue UI::SetReleaseNotes(const YCPMap & relnotes) {
	return YCP_UI::SetReleaseNotes(relnotes);
}

YCPValue UI::SetProductLogo(const bool & show_logo) {
	return YCP_UI::SetProductLogo(YCPBoolean(show_logo));
}

YCPValue UI::SetApplicationIcon(const string & icon) {
	return YCP_UI::SetApplicationIcon(YCPString(icon));
}

YCPValue UI::SetApplicationTitle(const string & text) {
	return YCP_UI::SetApplicationTitle(YCPString(text));
}

