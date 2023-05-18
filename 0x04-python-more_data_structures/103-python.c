#include <stdio.h>
#include <Python.h>
#include "lists.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a Python list object
 *
 * Description: Prints the size of the list, the amount of memory allocated,
 * and the type of each element in the list.
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	long int size = Py_SIZE(p);
	long int allocated = list->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (long int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

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
