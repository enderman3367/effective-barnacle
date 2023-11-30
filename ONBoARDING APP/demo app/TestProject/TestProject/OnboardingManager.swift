//
//  OnboardingManager.swift
//  TestProject
//
//  Created by Tunde Adegoroye on 24/04/2022.
//

import Foundation

struct OnboardingItem: Identifiable {
    let id = UUID()
    let emoji: String
    let title: String
    let content: String
}

extension OnboardingItem: Equatable {}

final class OnboardingManager: ObservableObject {
    
    @Published private(set) var items: [OnboardingItem] = []
    
    func load() {
        items = [
            .init(emoji: "📞",
                  title: "enter your phone number",
                  content: "get texts from a robot. yes im dead serious"),
            .init(emoji: "🥳",
                  title: "control your robot slave",
                  content: "yipee! dont worry it doesnt have any feelings. or does it? thats on your hands.")
        ]
    }
}
