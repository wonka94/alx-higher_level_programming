#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: pointer to a PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	Py_ssize_t limit = size < 10 ? size : 10;

	printf("  first %ld bytes:", limit);
	for (Py_ssize_t i = 0; i < limit; i++)
		printf(" %02x", (unsigned char)string[i]);

	printf("\n");
}

/**
 * print_python_list - prints info about a python list
 * @p: pointer to the python list object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long int size = Py_SIZE(p);
	long int allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (long int i = 0; i < size; i++)
	{
		PyObject *obj = list->ob_item[i];
		const char *type = Py_TYPE(obj)->tp_name;

		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
