// Implement string/integer inter-conversion functions

fn int_to_string(mut num: i32) -> String {
    let mut string: String = String::from("");

    if num < 0 { 
        let mut string: String = String::from("-"); 
    } else {
        let mut string: String = String::from("");
    }

    while num != 0 {
        string = format!("{}{}", num % 10, string);
        num /= 10;
    }

    return string;
}

fn string_to_int(x: String) -> i32 {
    let mut val: i32 = 0;
    let l: i32 = x.len() as i32 - 1;
    let mut negative: bool = false;

    for (index, character) in x.chars().enumerate() {
        if index == 0 && character == '-' { 
            negative = true; 
        } else {
            if (character as i32 > 47) && ((character as i32) < 58) {
                val += (10 as i32).pow((l - index as i32) as u32) * (character as i32 - 48);
            } else {
                panic!("Wrong format");
            }
        }
    }

    if negative { return -1 * val; }

    return val;
}

fn main() {
    // Testing string_to_int
    println!("{}", string_to_int(String::from("-10")));
    println!("{}", string_to_int(String::from("12345")));
    println!("{}", string_to_int(String::from("10")));

    // Testing int_to_string
    println!("{}", int_to_string(15670));
    println!("{}", "-190");
    // println!("{}", );
    // println!("{}", );
}