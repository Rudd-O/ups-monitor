#include <Python.h>

#include <glib.h>
#include <gtk/gtk.h>
#include <gtk/gtktypeutils.h>
#include <libgnomeui/libgnomeui.h>
#include <pygtk-2.0/pygobject.h>

#include "eggtrayicon.h"

static
PyObject *
create_window(PyObject *self, PyObject *args)
{
  char *name;
  EggTrayIcon *icon;

  if (!PyArg_ParseTuple(args, "s", &name))
    return NULL;

  icon = egg_tray_icon_new(name);
  return Py_BuildValue("N", pygobject_new((GObject *)icon));
}

static PyMethodDef EggTrayIconMethods[] = {
  {"create_window",  create_window, METH_VARARGS, "Create an EggTrayIcon window"},
  {NULL, NULL, 0, NULL}        /* Sentinel */
};

void
initeggtrayicon(void)
{
  init_pygobject();
  Py_InitModule("eggtrayicon", EggTrayIconMethods);
}

/* This is TERRIBLE, but expedient. */
#include "eggtrayicon.c"
