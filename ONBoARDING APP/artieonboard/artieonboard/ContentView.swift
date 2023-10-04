import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var phoneTextField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Setting up gradient background
        let gradientLayer = CAGradientLayer()
        gradientLayer.frame = view.bounds
        gradientLayer.colors = [UIColor.red.cgColor, UIColor.blue.cgColor] // Change colors as needed
        view.layer.insertSublayer(gradientLayer, at: 0)
    }

    @IBAction func sendContactTapped(_ sender: UIButton) {
        guard let name = nameTextField.text, let phone = phoneTextField.text else { return }
        
        let contactInfo = [
            "name": name,
            "phone": phone
        ]

        // Assuming your Flask server is running on your computer and accessible via IP address 192.168.1.100
        if let url = URL(string: "http://192.168.1.100:5000/add_contact") {
            var request = URLRequest(url: url)
            request.httpMethod = "POST"
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")
            request.httpBody = try? JSONSerialization.data(withJSONObject: contactInfo)

            URLSession.shared.dataTask(with: request) { (data, response, error) in
                if let error = error {
                    print("Error: \(error.localizedDescription)")
                    return
                }
                
                DispatchQueue.main.async {
                    // Changing the screen to indicate completion
                    self.view.backgroundColor = .green
                    let label = UILabel(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
                    label.center = self.view.center
                    label.textAlignment = .center
                    label.text = "Done!"
                    self.view.addSubview(label)
                }
            }.resume()
        }
    }
}
