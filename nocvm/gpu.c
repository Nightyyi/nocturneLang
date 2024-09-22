#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <signal.h>

int alu (int alu_operation, int bus_A, int bus_B){
  int intermediate_value;
  switch (alu_operation){
    case 0:  intermediate_value = bus_A +  bus_B;break;
    case 1:  intermediate_value = bus_A -  bus_B;break;
    case 2:  intermediate_value = bus_A ^  bus_B;break;
    case 3:  intermediate_value = bus_A |  bus_B;break;
    case 4:  intermediate_value = bus_A &  bus_B;break;
    case 5:  intermediate_value = bus_A >> bus_B;break;
    case 6:  intermediate_value = bus_A << bus_B;break;
    case 7:  intermediate_value = bus_A >  bus_B;break;
    case 8:  intermediate_value = bus_A <  bus_B;break;
    case 9:  intermediate_value = bus_A == bus_B;break;
    case 10: intermediate_value = bus_A != bus_B;break;
    case 11: intermediate_value = bus_A >= bus_B;break;
    case 12: intermediate_value = bus_A <= bus_B;break;
    case 13: intermediate_value = bus_A *  bus_B;break;
    case 14: intermediate_value = bus_A /  bus_B;break;
  }
  return intermediate_value;
}


char* int_to_bin32( int integer_value ){
  char* binary_string = malloc(33);
  char single_character;
  for (int i = 0; i < 32; i++){
    if ( ((integer_value >> i) & 1) == 1 ){
      binary_string[i] = '1';
    } else {
      binary_string[i] = '0';
    }
  }
  binary_string[32] = 0;
  return binary_string;
}

int bin_to_int( char* binary_string ){
  int value = 0; int value_plus;
  char single_character;
  int i_max = strlen(binary_string);
  for (int i = 0; i < i_max; i++){
    single_character = binary_string[i];
    switch (single_character){
      case '0':
        value = value*2;
       break;
      case '1':
        value = value*2 + 1;        
       break;
    }
  }
  return value;
}

char* string_insert( char* binary_string, char* insert_string, int address_to_insert ){
  int address_max = address_to_insert + strlen(insert_string);
  for (int i = 0; i < address_max; i++){
    binary_string[i+address_to_insert] = insert_string[i];
  }
  return binary_string;
}


char* string_slice( char* binary_string, int address_min, int address_max ){
  int address_diff = address_max - address_min;
  char* new_value = (char*) calloc( address_diff, 1 );
  for (int i = 0; i < address_max; i++){ new_value[i] = binary_string[i+address_min];}
  return new_value;
}


FILE *file;

int main(){
	int error = fopen_s(&file,"gpumem.txt","r");	

	int* arch_memory = (int*) calloc(4096, 4);
	

  char ch;
	int accCounter = 0; int address = 0;
  char ch_accumilator[32];
	while (!feof(file)) {
		ch = fgetc(file);
		if (ch != '\n' && ch != '\0' && ch == '1' || ch == '0') {
      if (accCounter < 32){
        ch_accumilator[accCounter] = ch;
        accCounter++;
      } 
      if (accCounter >= 32){
        arch_memory[address] = bin_to_int(ch_accumilator);
        for (int ii=0;ii<32;ii++){ ch_accumilator[ii] = 0; }
        accCounter = 0;
        address++;
      }
			
		}
	}
  for (int i = 0; i < 4096; i++){

    printf("%d ", arch_memory[i]);
  }

  fclose(file);


	int* registers = (int*) calloc(64, 4);

  int alu_operation;
  int bus_A; int bus_B;
  int intermediate_value;

  int instruction;
  for (int instruction_pointer = 0; instruction_pointer < 4096; instruction_pointer++){
    instruction = arch_memory[instruction_pointer];

    int operation           =  (instruction >> 25) & 0xcf;
    int secondary_operand   =  (instruction >> 16) & 0x1ff; 
    int primary_operand     =  instruction & 0xffff;
    printf("\no: %02x s: %03x p: %04x  f_inst: %08x ", operation, secondary_operand, primary_operand, instruction);
    printf("\no: %02d s: %03x p: %04d  f_inst: %08d ", operation, secondary_operand, primary_operand, instruction);
    printf("\n%d,  %b", instruction_pointer, instruction);
    switch ( operation ){
      case 0b0000000: //END
        instruction_pointer= 256*256*256;
        break;
      case 0b0000001: //LDIM
        registers[secondary_operand & 0b111111] = primary_operand;
        break; 
      case 0b0000011: //LD
        registers[secondary_operand & 0b111111] =  registers[primary_operand & 0b111111];
        break; 
      case 0b0000010: //OP
        alu_operation = secondary_operand >> 2;
        bus_A = registers[ primary_operand & 0x3f ];
        bus_B =  registers[ primary_operand >> 6 & 0x3f ];
        int intermediate_value = alu(alu_operation, bus_A, bus_B);
        registers[ ((primary_operand >> 12 & 0x3f) + ((secondary_operand & 3) << 4)) & 0b111111 ] = intermediate_value;
        break;
      case 0b0000100: //WR

        registers[secondary_operand & 0b111111] =  arch_memory[registers[primary_operand & 0b111111]];
        break;
      case 0b0000101: //RD
        arch_memory[registers[secondary_operand & 0b111111]] =  registers[primary_operand & 0b111111];
        break;
      case 0b0000110: // B 
        instruction_pointer = instruction_pointer + registers[primary_operand & 0b111111];
        break;
      case 0b0000111: // BZ
        if (registers[primary_operand & 0b111111] == 0 ){
          instruction_pointer = instruction_pointer + registers[secondary_operand & 0b111111];
        }
        break;
      case 0b0001000: // BNZ
        if (registers[primary_operand & 0b111111] != 0 ){
          instruction_pointer = instruction_pointer + registers[secondary_operand & 0b111111];
        }
        break;
      case 0b0001001: // J 
        instruction_pointer = registers[primary_operand & 0b111111];
        break;
      case 0b0001010: // JZ
        if (registers[primary_operand & 0b111111] == 0 ){
          instruction_pointer = registers[secondary_operand & 0b111111];
        }
        break;
      case 0b0001011: // JNZ
        if (registers[primary_operand & 0b111111] != 0 ){
          instruction_pointer = registers[secondary_operand & 0b111111];
        }
        break;
      case 0b0001100: // CLR
        int temporary_value = registers[primary_operand & 0b1111111]
        for (int iii=0; iii< temporary_value; iii++){
          registers[iii] = 0;
        }
        break;
      case 0b0001101: // OUT
        int error = fopen_s(&file,"out.out","w");
        char* out_value = int_to_bin32(registers[primary_operand & 0b1111111]);
        fputs(out_value, file);
        free(out_value);
        break;
      case 0b0001110: // GAD
        registers[primary_operand_operand & 0b111111] = instruction_pointer;        
        break;
      case 0xcf:
        for ( int iii=0; iii < 63; iii++ ){ 
          if (iii % 8 == 0){ printf("\n"); }
          printf("%08x ", registers[iii]); 
        }
        printf("\n");
        break;

    }
    printf("\n%d,  %b", instruction_pointer, instruction);
  }  
  
  printf("\n\n||||||||||||||||||||||||||END||||||||||||||||||||||||||\n\n");
  
  free(arch_memory);
  free(registers);
  return 1;
}
