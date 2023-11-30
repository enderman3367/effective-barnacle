//
//  BioView.swift
//  TestProject
//
//  Created by Tunde Adegoroye on 24/04/2022.
//

import SwiftUI


struct BioView: View {
    @Binding var text: String
    let action: () -> Void
    var body: some View {
        VStack {
            
            Text("✍️")
                .font(.system(size: 100))
            
            Text("Customize Your Bot")
                .font(.system(size: 30,
                              weight: .bold,
                              design: .rounded))
                .foregroundColor(.white)

            TextEditor(text: $text)
                .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
                .padding()
                .foregroundColor(.gray)  // Set the text color to gray
                .overlay(
                    // Add the placeholder text as an overlay
                    Text("comments? idk about anything")
                        .foregroundColor(.gray)
                        .opacity(text.isEmpty ? 1 : 0)  // Show the placeholder only when the text is empty
                )

            Button("GO") {
                action()
            }
            .font(.system(size: 20, weight: .bold, design: .rounded))
            .padding(.horizontal, 60)
            .padding(.vertical, 15)
            .background(.white, in: RoundedRectangle(cornerRadius: 10,
                                                     style: .continuous))
            .padding(.top, 40)

        }
    }
}

struct BioView_Previews: PreviewProvider {
    static var previews: some View {
        BioView(text: .constant("")) {}
            .padding()
            .previewLayout(.sizeThatFits)
            .background(.blue)
    }
}

