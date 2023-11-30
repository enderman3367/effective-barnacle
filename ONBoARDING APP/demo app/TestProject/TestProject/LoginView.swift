//
//  LoginView.swift
//  TestProject
//
//  Created by Tunde Adegoroye on 24/04/2022.
//

import SwiftUI

struct LoginView: View {
    
    @EnvironmentObject var session: SessionManager

    var body: some View {
        ZStack {
            LinearGradient(
                gradient: Gradient(
                    stops: [
                        Gradient.Stop(color: Color(.displayP3, red: 1, green: 0.473, blue: 0.16, opacity: 1), location: 0),
                        Gradient.Stop(color: Color(.displayP3, red: 0.94, green: 0.604, blue: 0.434, opacity: 1), location: 1)
                    ]
                ),
                startPoint: UnitPoint(x: 0.5, y: 0),
                endPoint: UnitPoint(x: 0.5, y: 1)
            )
            .ignoresSafeArea(edges: .all)
            
            VStack(spacing: 0) {
                info
                username
                password
                login
            }
            
        }
    }
}

private extension LoginView {
    
    var info: some View {
        
        VStack(spacing: 8) {
            Text("💀")
                .font(.system(size: 200))
            
            Text("you login here")
                .font(.system(size: 35,
                              weight: .heavy,
                              design: .rounded))
            
            Text("you should probably count your calories, fleshling.")
                .font(.system(size: 15,
                              weight: .regular,
                              design: .rounded))
            
        }
        .multilineTextAlignment(.center)
        .foregroundColor(.white)
        .padding(.bottom, 50)
    }
    
    var username: some View {
        
        TextField("Username", text: .constant(""))
            .padding()
            .frame(width: 350, height: 50)
            .background(.white, in: RoundedRectangle(cornerRadius: 10,
                                                     style: .continuous))
            .font(.system(size: 13, weight: .bold, design: .rounded))
            .padding(.bottom, 8)
    }
    
    var password: some View {
        
        SecureField("Password", text: .constant(""))
            .padding()
            .frame(width: 350, height: 50)
            .background(.white, in: RoundedRectangle(cornerRadius: 10,
                                                     style: .continuous))
            .font(.system(size: 13, weight: .bold, design: .rounded))
    }
    
    var login: some View {
        Button("Login") {
            session.signIn()
        }
        .font(.system(size: 20, weight: .bold, design: .rounded))
        .padding(.horizontal, 60)
        .padding(.vertical, 15)
        .background(.white, in: RoundedRectangle(cornerRadius: 10,
                                                 style: .continuous))
        .padding(.top, 40)
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
            .environmentObject(SessionManager())
    }
}
