#Group 1: Arithmetic
OP_ADD = 0x00
OP_SUB = 0x01
OP_MUL = 0x02
OP_DIV = 0x03
OP_MOD = 0x04

#Group 2: Binary
OP_OR  = 0x10
OP_XOR = 0x11
OP_AND = 0x12
OP_NOT = 0x13

#Group 3: Misc
OP_MOV = 0x20
OP_NOP = 0x21
OP_HALT= 0x22
OP_PRINT=0x23

#Group 4: Compare
OP_CMP = 0x30

#Group 5: Branches
OP_JMP = 0x40
OP_JZ  = 0x41
OP_JNZ = 0x42
OP_JGT = 0x43
OP_JGE = 0x44
OP_CALL= 0x45
OP_RET = 0x46

#Group 6: Stack
OP_PUSH= 0x50
OP_POP = 0x51

#Group 7: Interrupts
OP_INT = 0x60
OP_RETI= 0x61
OP_VMRESUME=0x62


#Special Registers
SPECIALREG_SEGTBL	=	0
SPECIALREG_VMTBL	=	1
SPECIALREG_STACKPTR	=	2
SPECIALREG_CS		=	3
SPECIALREG_DS		=	4
SPECIALREG_ES		=	5
SPECIALREG_RS		=	6
SPECIALREG_SS		=	7

SPECIALREGS = {
	'segtbl': SPECIALREG_SEGTBL,
	'vmtbl': SPECIALREG_VMTBL,
	'stackptr': SPECIALREG_STACKPTR,
	'cs': SPECIALREG_CS,
	'ds': SPECIALREG_DS,
	'es': SPECIALREG_ES,
	'rs': SPECIALREG_RS,
	'ss': SPECIALREG_SS
}


#Possible parameter types
PARAM_IMMEDIATE 		= 0x00
PARAM_REGISTER			= 0x01
PARAM_MEMORY_SINGLE_DS 	= 0x02
PARAM_MEMORY_SINGLE_ES	= 0x03
PARAM_MEMORY_DOUBLE_DS	= 0x04
PARAM_MEMORY_DOUBLE_ES	= 0x05
PARAM_SPECIAL_REGISTER	= 0x06

#Possible segment types
SEGMENT_CODE			= 0x00
SEGMENT_DATA			= 0x01
SEGMENT_REGISTER		= 0x02
SEGMENT_STACK			= 0x03
SEGMENT_TYPES = [SEGMENT_CODE, SEGMENT_DATA, SEGMENT_REGISTER, SEGMENT_STACK]

#Possible interrupts
INTR_RESET = 0
INTR_SEG_VIOL = 1
INTR_INVALID_INSTR = 2
INTR_DIV_BY_ZERO = 3
INTR_HV_TRAP = 4
INTR_TIMER = 5
INTR_SOFTWARE = 6
