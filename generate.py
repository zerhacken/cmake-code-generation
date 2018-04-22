'''
#include "Sample.h"

std::string sample()
{
    return "zerhacken ";
}
'''
message = 'zerhacken'
f = open("Sample.cpp","w+")
f.write('#include \"Sample.h\"\n')
f.write('std::string sample()\n')
f.write('{\n')
f.write('return \"zerhacken\";\n')
f.write('}\n')
f.close()