from common.Opcodes import *

_INSTR = {
	OP_ADD: {
		'nargs': 2,
		'name': 'ADD',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_SUB: {
		'nargs': 2,
		'name': 'SUB',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_MUL: {
		'nargs': 2,
		'name': 'MUL',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_DIV: {
		'nargs': 2,
		'name': 'DIV',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_MOD: {
		'nargs': 2,
		'name': 'MOD',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},

	OP_OR: {
		'nargs': 2,
		'name': 'OR',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_XOR: {
		'nargs': 2,
		'name': 'XOR',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_AND: {
		'nargs': 2,
		'name': 'AND',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_NOT: {
		'nargs': 2,
		'name': 'NOT',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},

	OP_MOV: {
		'nargs': 2,
		'name': 'MOV',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES, PARAM_SPECIAL_REGISTER],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES, PARAM_SPECIAL_REGISTER],
		]
	},

	OP_NOP: {
		'nargs': 0,
		'name': 'NOP',
		'paramtypes': []
	},
	OP_HALT: {
		'nargs': 0,
		'name': 'HALT',
		'paramtypes': []
	},


	OP_PRINT: {
		'nargs': 1,
		'name': 'PRINT',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES]
		]
	},


	OP_CMP: {
		'nargs': 2,
		'name': 'CMP',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},


	OP_JMP: {
		'nargs': 1,
		'name': 'JMP',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES]
		]
	},
	OP_JZ: {
		'nargs': 1,
		'name': 'JZ',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_JNZ: {
		'nargs': 1,
		'name': 'JNZ',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_JGT: {
		'nargs': 1,
		'name': 'JGT',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_JGE: {
		'nargs': 1,
		'name': 'JGE',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_CALL: {
		'nargs': 1,
		'name': 'CALL',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_RET: {
		'nargs': 0,
		'name': 'RET',
		'paramtypes': []
	},

	OP_PUSH: {
		'nargs': 1,
		'name': 'PUSH',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},
	OP_POP: {
		'nargs': 1,
		'name': 'POP',
		'paramtypes': [
			[PARAM_REGISTER, PARAM_IMMEDIATE, PARAM_MEMORY_SINGLE_DS, PARAM_MEMORY_SINGLE_ES, PARAM_MEMORY_DOUBLE_DS, PARAM_MEMORY_DOUBLE_ES],
		]
	},


	OP_INT: {
		'nargs': 1,
		'name': 'INT',
		'paramtypes': [
			[PARAM_IMMEDIATE],
		]
	},


	OP_RETI: {
		'nargs': 0,
		'name': 'RETI',
		'paramtypes': []
	},
	OP_VMRESUME: {
		'nargs': 0,
		'name': 'VMRESUME',
		'paramtypes': []
	},
}

def doesInstructionExist(opcode):
	return opcode in _INSTR

def getArgumentCount(opcode):
	#TODO throw exception if unknown opcode
	return _INSTR[opcode]['nargs']

def areParametersValid(opcode, operandType1, operandType2):
	if not opcode in _INSTR:
		return False

	if len(_INSTR[opcode]['paramtypes']) > 0 and not operandType1 in _INSTR[opcode]['paramtypes'][0]:
		return False

	if len(_INSTR[opcode]['paramtypes']) > 1 and not operandType2 in _INSTR[opcode]['paramtypes'][1]:
		return False

	return True
