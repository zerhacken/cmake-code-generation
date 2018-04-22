'''
Code generation sample script
'''
f = open("Sample.cpp","w+")
f.write('#include \"Sample.h\"\n')
f.write('\n')
f.write('std::string sample()\n')
f.write('{\n')
f.write('    return \"a little string\";\n')
f.write('}\n')

f.close()