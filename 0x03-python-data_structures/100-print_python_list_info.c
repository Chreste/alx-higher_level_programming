#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print python
 * @p: input
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	pyobject *obj;

	size = py_SIZE(P);
	alloc = ((pyListobject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	for (x =0; x < size; x++)
	{
		printf("Element %d: ", x)

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
