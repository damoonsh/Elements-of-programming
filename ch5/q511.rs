
fn check_divisibility(num: u32) -> bool {
    for i in 2..(num / 2) as i32 {
        if num as i32 % i == 0 { return true; }
    }

    false
}

fn return_primes(n: u32) -> Vec<u32> {
    let mut primes = vec![2];
    
    for val in 2..n {
        if val % 2 != 0 {
            if !check_divisibility(val) {
                primes.push(val);
            }
        }
    }

    primes
}

fn main() {
    assert_eq!(vec![2, 3, 5, 7], return_primes(10));
    assert_eq!(vec![2, 3, 5, 7, 11, 13, 17, 19], return_primes(20));
    assert_eq!(vec![2, 3, 5, 7, 11, 13, 17, 19, 23], return_primes(26));
    assert_eq!(
        vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43], 
        return_primes(45)
    );
    assert_eq!(
        vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43], 
        return_primes(48)
    );
}