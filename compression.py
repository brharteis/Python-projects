class compressAnswers:
    def __init__(self, answer):
        self.compress(answer)
    

    def compress(self, answer):
        self.bitString = 1
        for letter in answer.upper():
            self.bitString <<= 2 #Moves bit over two spots 0b100 to start, then 0b10000 ect
            if letter == "A":
                self.bitString |= 0b00
            elif letter == "B":
                self.bitString |= 0b01
            elif letter == "C":
                self.bitString |= 0b10
            elif letter == "D":
                self.bitString |= 0b11
            else:
                raise ValueError
        return self.bitString
            
    def get_compressed(self):
        return self.bitString

    def decompress(self):
        answers = ""
        for i in range(0, self.bitString.bit_length()-1,2):
            bits = self.bitString >> i & 0b11 #Gets two bits at a time
            if bits == 0b00:
                answers += "A"
            elif bits == 0b01:
                answers += "B"
            elif bits == 0b10:
                answers += "C"
            elif bits == 0b11:
                answers += "D"
            else:
                raise ValueError
        return answers[::-1]



if __name__ == "__main__":
    from sys import getsizeof
    answers = compressAnswers("ABCD")
    print(bin(answers.get_compressed()))
    print(answers.decompress())
    print(getsizeof("ABCD"))
    print(getsizeof(answers.get_compressed()))



    