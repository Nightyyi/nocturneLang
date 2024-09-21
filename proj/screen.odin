package main

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:slice"
import "vendor:raylib"

read_entire_file :: proc( array_out: rawptr ,file_path: string ) {
  data, ok := os.read_entire_file(file_path, context.allocator)
  if !ok {
    fmt.println("Couldnt read file\n maybe file path doesnt exist.")
    return  
  }
  defer delete(data, context.allocator)
  
  array_c := 0
  for strlist in data{
      array_out[array_c] = strlist
      array_c +=1
    }
}

main :: proc() {
    using raylib

    fmt.println("goodbye world")
    screenWidth :: 800
    screenHeight :: 800
    fmt.print("a")
    InitWindow(screenWidth, screenHeight, "rlib")

    SetTargetFPS(60)

    windowShouldClose := false
    fmt.print("b")
    dat : [1064]u8
    datptr := &dat
    read_entire_file(datptr, ".\\connection.txt")
    out : i32
    x : i32
    y : i32
    for !windowShouldClose {


        fmt.println(x)
        x = 0
        y = 0
        for x in 0..<800 {
          BeginDrawing()
          for y in 0..<800 {
            DrawPixel( i32(x), i32(y), Color{ u8(out), u8(out), u8(out),u8(255) }) 
          
          }
        }    
        EndDrawing()
        if IsKeyPressed(KeyboardKey.ESCAPE) {
            windowShouldClose = true
        }
        fmt.print("right before EndDrawing()")

        fmt.print("f")
    }
    CloseWindow()
}
