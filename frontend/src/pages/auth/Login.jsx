function Login() {
    return (
      <div className="min-h-screen bg-gradient-to-br from-purple-700 via-purple-600 to-indigo-700 flex items-center justify-center">
        <div className="bg-white rounded-3xl shadow-2xl p-10 w-full max-w-md">
  
          <h1 className="text-3xl font-bold text-center text-purple-700">
            Attendance Management
          </h1>
  
          <p className="text-center text-gray-500 mt-2 mb-8">
            Welcome Back 👋
          </p>
  
          <form className="space-y-5">
  
            <div>
              <label className="block mb-2 text-gray-700 font-medium">
                Email
              </label>
              <input
                type="email"
                placeholder="Enter your email"
                className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
  
            <div>
              <label className="block mb-2 text-gray-700 font-medium">
                Password
              </label>
              <input
                type="password"
                placeholder="Enter your password"
                className="w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
            </div>
  
            <button
              className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-xl font-semibold transition duration-300"
            >
              Login
            </button>
  
          </form>
  
        </div>
      </div>
    );
  }
  
  export default Login;