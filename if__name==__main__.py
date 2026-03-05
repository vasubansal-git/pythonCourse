# It is used to check whether the Python file is being run directly or imported as a module.
# It allows us to separate code that should run when the file is executed directly from code that should not run when the file is imported.

import vasu

vasu.welcome()

# -------------------------------------------------------------------------------------------------------
import vasu

vasu.add(5, 6)