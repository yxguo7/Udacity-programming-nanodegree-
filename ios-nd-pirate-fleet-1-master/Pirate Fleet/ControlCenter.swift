//
//  ControlCenter.swift
//  Pirate Fleet
//
//  Created by Jarrod Parkes on 9/2/15.
//  Copyright © 2015 Udacity. All rights reserved.
//

struct GridLocation {
    let x: Int
    let y: Int
}

struct Ship {
    let length: Int
    let location: GridLocation
    let isVertical: Bool
}

struct Mine: _Mine_ {
    let location: GridLocation
    let explosionText: String
}

class ControlCenter {
    
    func addShipsAndMines(human: Human) {
        // Write your code here!
        let mediumShip1 = Ship(length: 3, location: GridLocation(x:0, y:0), isVertical: false)
        let smallShip = Ship(length: 2, location: GridLocation(x:0, y:1), isVertical: false)
        let mediumShip2 = Ship(length: 3, location: GridLocation(x:0, y:2), isVertical: false)
        let largeShip = Ship(length: 4, location: GridLocation(x:0, y:3), isVertical: false)
        let extraLargeShip = Ship(length: 5, location: GridLocation(x:0, y:4), isVertical: false)
        
        let mine1 = Mine(location: GridLocation(x: 3, y: 0), explosionText: "Hit mine1")
        let mine2 = Mine(location: GridLocation(x: 4, y: 0), explosionText: "Hit mine2")
        
        human.addShipToGrid(mediumShip1)
        human.addShipToGrid(smallShip)
        human.addShipToGrid(mediumShip2)
        human.addShipToGrid(largeShip)
        human.addShipToGrid(extraLargeShip)
        
        human.addMineToGrid(mine1)
        human.addMineToGrid(mine2)
    }
    
    func calculateFinalScore(gameStats: GameStats) -> Int {
        
        var finalScore: Int
        let maxShip = 5
        let enemyShipsSunk = maxShip - gameStats.enemyShipsRemaining
        let humanShipsRemaining = maxShip - gameStats.humanShipsSunk
        let sinkBonus = gameStats.sinkBonus
        let shipBonus = gameStats.shipBonus
        let numberOfGuesses = gameStats.numberOfHitsOnEnemy + gameStats.numberOfMissesByHuman
        finalScore = (enemyShipsSunk * sinkBonus) + (humanShipsRemaining * shipBonus) - (numberOfGuesses * gameStats.guessPenalty)
        print("the value of final score is \(finalScore)")
        return finalScore
    }
}









