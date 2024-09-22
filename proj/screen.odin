package main

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:slice"
import "core:math"
import "core:c"
import "vendor:raylib"

data_to_val :: proc( data: []u8 ) -> u128{
  value_filtered : u128 = 0
  counter : u8 = 0 
  for individual_character in data{
    if individual_character == '1'{
      add : u128 = 1 << counter
      value_filtered = value_filtered + add
      counter+=1
    }
    if individual_character == '0'{
      counter+=1
    }
  }
  return value_filtered

}



main :: proc() {
    using raylib

    fmt.println("goodbye world")
    screenWidth :: 512
    screenHeight :: 512
    InitWindow(screenWidth, screenHeight, "rlib")

    SetTargetFPS(60)

    windowShouldClose := false
    
    

    out : i32
    x : i32
    y : i32
    old_value : u128 = 0
    color := Color({ u8(255), u8(255), u8(255), u8(255)})
    buffer : [256*256]Color
    for !windowShouldClose {
        data, ok := os.read_entire_file(".\\connection.txt", context.allocator)
        if (!ok) {
          fmt.println("Couldnt read file\n maybe file path doesnt exist.")
        }
        if ok {
        
          defer delete(data, context.allocator)

          value_filtered := data_to_val(data)     
          if (value_filtered != old_value){
            fmt.printf("%016x\n",value_filtered)

          instruction := (value_filtered >> 32)
          operand := value_filtered & 0xffffffff
          switch (instruction){
            case 1:  
              x := operand & 0x000000ff
              y := operand & 0x0000ff00 >> 8
              index := x + (y * 256)
              buffer[index] = color
        
            case 2:  
              r := u8(operand & 0x000000ff)
              g := u8(operand & 0x0000ff00) >> 8
              b := u8(operand & 0x00ff0000) >> 16
              a := u8(operand & 0xff000000) >> 24
              color := Color({r,g,b,a})
          }
          } 
          old_value = value_filtered
          c_index := 0
          BeginDrawing()
          for cell_color in buffer{
            DrawPixel( (i32(c_index%256))*2  , (i32((c_index/256)))*2  , cell_color) 
            DrawPixel( (i32(c_index%256))*2+1, (i32((c_index/256)))*2  , cell_color) 
            DrawPixel( (i32(c_index%256))*2  , (i32((c_index/256)))*2+1, cell_color) 
            DrawPixel( (i32(c_index%256))*2+1, (i32((c_index/256)))*2+1, cell_color) 
            
            c_index+=1
          }
          EndDrawing()

        }
        if IsKeyPressed(KeyboardKey.ESCAPE) {
            windowShouldClose = true
        }
    }
    CloseWindow()
}
