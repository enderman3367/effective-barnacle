//
//  TermsAgreementView.swift
//  TestProject
//
//  Created by Tunde Adegoroye on 24/04/2022.
//

import SwiftUI

struct TermsAgreementView: View {
    let action: () -> Void
    var body: some View {
        
        VStack {
            title
            content
            agreeToTerms
        }
    }
}

struct TermsAgreementView_Previews: PreviewProvider {
    static var previews: some View {
        TermsAgreementView {}
    }
}

private extension TermsAgreementView {
    
    var title: some View {
        Text("Terms of Service")
            .font(
                .system(.largeTitle, design: .rounded)
                .bold()
            )
            .padding(.bottom, 8)
    }
    
    var content: some View {
        ScrollView {
            Text("you agree? (to give us all your money)")
                .italic()
                .padding()
        }
    }

    var agreeToTerms: some View {
        Button("Agree to terms (these arent official dont worry)") {
           action()
        }
        .buttonStyle(.borderedProminent)
        .controlSize(.large)
        .padding()
    }
}
