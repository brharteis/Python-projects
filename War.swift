//
//  ContentView.swift
//  GameDemo
//
//  Created by Benjamin Harteis on 11/9/24.
//

import SwiftUI
import SwiftData

struct ContentView: View {
    @State var playerCard = "card7"
    @State var cpuCard = "card13"
    
    @State var playerScore = 0
    @State var cpuScore = 0
    
    @State var playerRandNum = 0
    @State var cpuRandNum = 0
    
    
    
    var body: some View {
        
        ZStack{
            Image("background-cloth")
            
            VStack{
                Spacer()
                Spacer()
                Image("logo")
                    .padding(.top)
                Spacer()
                HStack{
                    Spacer()
                    Image(playerCard)
                    Spacer()
                    Image(cpuCard)
                    Spacer()
                    
                }
                Spacer()
                
                Button{
                    deal()
                } label: {
                    Image("button")
                }
                
                Spacer()
                HStack{
                    Spacer()
                    Text("Player")
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundColor(Color.white)
                    Spacer()
                    Text("CPU")
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundColor(Color.white)
                        .padding(.trailing)
                    Spacer()
                    
                    
                }
                Spacer()
                HStack{
                    Spacer()
                    Text(String(playerScore))
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundColor(.white)
                    Spacer()
                    Text(String(cpuScore))
                        .font(.title)
                        .fontWeight(.bold)
                        .foregroundColor(Color.white)
                    Spacer()
                }
                Spacer()
                Spacer()
                
            }
            
        }
    }
    func deal() {
        playerRandNum = Int.random(in: 2...14)
        cpuRandNum = Int.random(in: 2...14)
        playerCard = "card" + String(playerRandNum)
        cpuCard = "card" + String(cpuRandNum)
        if playerRandNum > cpuRandNum {
            playerScore += 1
        }
        else if cpuRandNum > playerRandNum{
            cpuScore += 1
        }
    }
}
    #Preview {
        ContentView()
            .modelContainer(for: Item.self, inMemory: true)
    }

