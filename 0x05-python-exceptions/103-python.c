#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_float - print python things
 * @p: pointer to PyObject p
 */
void print_python_float(PyObject *p)
{
	double z;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	z = ((PyFloatObject *)(p))->ob_fval;
           printf("  value: %s\n",
           PyOS_double_to_string(z, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
/**
 * print_python_bytes - print python things
 * @p: pointer to PyObject p
 */
void print_python_bytes(PyObject *p)
{
	size_t r, x;
	char *str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval, r = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", r, str);
	r >= 10 ? r = 10 : r++;
	printf("  first %ld bytes: ", r);
	for (x = 0; x < r - 1; x++)
		printf("%02hhx ", str[x]);
	printf("%02hhx\n", str[x]);
}
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, x;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (x = 0; x < size; x++)
	{
		type = list->ob_item[x]->ob_type->tp_name;
		printf("Element %ld: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[x]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[x]);
	}
}
