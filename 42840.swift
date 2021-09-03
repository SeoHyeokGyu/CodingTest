//
//  42840.swift
//  
//
//  Created by 서혁규 on 2021/09/03.
//수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
//
//1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
//2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
//3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
//
//1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let arr1 = [1,2,3,4,5]
    let arr2 = [2,1,2,3,2,4,2,5]
    let arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    var dic: [Int: Int] = [:]
    
    for i in 0..<answers.count {
        if answers[i] == arr1[i%arr1.count] { dic[1] = (dic[1] ?? 0) + 1 }
        if answers[i] == arr2[i%arr2.count] { dic[2] = (dic[2] ?? 0) + 1 }
        if answers[i] == arr3[i%arr3.cougitnt] { dic[3] = (dic[3] ?? 0) + 1 }
    }
    
    let max = dic.values.max()!
    
    let result = dic.filter { $0.value == max }.keys.sorted()

    return result
}
