#include "yast.h"

static Y2Namespace * getNs (const char * ns_name, const char * func_name) 
{
	Import import(ns_name);	// has a static cache
	Y2Namespace *ns = import.nameSpace();
	if (ns == NULL) {
		y2error ("... for a Python call of %s", func_name);
	} else {
		ns->initialize ();
	}
	return ns;
}

static YCPValue CallYCPFunction(const string & namespace_name, const string & function_name, int number_args, ...)
{
    va_list args;
    va_start(args, number_args);
    YCPValue ycpArg = YCPNull ();
	YCPValue ycpRetValue = YCPNull ();

    // create namespace
    Y2Namespace *ns = getNs(namespace_name.c_str(), function_name.c_str());

    if (ns == NULL) {
        y2error ("Creating namespace fault.");
        return YCPNull();
    }

    // we want either a function or a variable
    // so find a symbol of an unspecified category
    TableEntry *sym_te = ns->table ()->find (function_name.c_str());

    if (sym_te == NULL) {
        y2error ("No such symbol %s::%s", namespace_name, function_name);
        return YCPNull();
    }

    SymbolEntryPtr sym_entry = sym_te->sentry();
    if (sym_entry->isVariable()) {
        if (number_args < 2) {
            if (number_args == 0)
                return sym_entry->value();
            else
                sym_entry->setValue(va_arg(args, YCPValue));
        } else {
            y2error ("Too many arguments for variable in YCP");
            return YCPNull();
        }
    }
    constFunctionTypePtr fun_type = (constFunctionTypePtr)sym_entry->type();
    Y2Function *func_call = ns->createFunctionCall (function_name, NULL);

    if (func_call == NULL) {
        y2error ("No such function %s::%s", namespace_name, function_name);
        return YCPNull();
    }
    if (fun_type->parameterCount() > number_args) {
        y2error ("Too many arguments");
        return YCPNull();
    } else if (fun_type->parameterCount() < number_args) {
        y2error ("Missing arguments");
        return YCPNull();
    }

    for (int i=0; i < number_args; i++) {
        ycpArg = va_arg(args, YCPValue);
        if (ycpArg.isNull())
            ycpArg = YCPVoid();

        if (!func_call->appendParameter(ycpArg)) {
            y2error ("Problem with adding arguments of function %s", function_name);
            return YCPNull();
        }
    }
    if (!func_call->finishParameters()) {
        y2error ("Problem with finishing arguments for adding arguments of function %s", function_name);
        return YCPNull();
    }

    va_end(args);

    ycpRetValue = func_call->evaluateCall();
    delete func_call;
    if (ycpRetValue.isNull()) {
        y2error ("Return value of function %s is NULL", function_name);
        return YCPNull();
    }
    return ycpRetValue;
}

bool init_ui(const string & ui_name)
{
    Y2Component *c = YUIComponent::uiComponent ();

    if (c == 0)
    {
        y2debug ("UI component not created yet, creating %s", ui_name.c_str());
        c = Y2ComponentBroker::createServer (ui_name.c_str());

        if (c == 0)
        {
            y2error ("Cannot create component %s", ui_name.c_str());
            return false;
        }

        if (YUIComponent::uiComponent () == 0)
        {
            y2error ("Component %s is not a UI", ui_name.c_str());
            return false;
        } else {
            // got it - initialize
            c->setServerOptions (0, NULL);
        }
    } else {
        y2debug ("UI component already present: %s", c->name ().c_str ());
    }
    return true;
}

void Wizard::CreateDialog()
{
    CallYCPFunction("Wizard", "CreateDialog", 0);
}

void Wizard::SetContentsButtons(const string & title, const YCPValue & contents, const string & help_txt, const string & back_txt, const string & next_txt)
{
    CallYCPFunction("Wizard", "SetContentsButtons", 5, YCPString(title), contents, YCPString(help_txt), YCPString(back_txt), YCPString(next_txt));
}

void Wizard::DisableBackButton()
{

}

void Wizard::DisableNextButton()
{

}

void Wizard::EnableNextButton()
{

}

void Wizard::DisableAbortButton()
{

}

