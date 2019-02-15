This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case P1
		>>> hive = Hive(make_test_assault_plan())
		>>> colony = AntColony(None, hive, ant_types(), dry_layout, (1, 9))
		>>> colony.food = 6
		>>> harvester = HarvesterAnt()
		>>> harvester.action(colony)
		>>> colony.food
		7
		>>> harvester.action(colony)
		>>> colony.food
		8


