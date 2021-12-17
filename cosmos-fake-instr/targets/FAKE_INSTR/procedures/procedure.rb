# Script Runner test script
cmd("FAKE_INSTR EXAMPLE")
wait_check("FAKE_INSTR STATUS BOOL == 'FALSE'", 5)
