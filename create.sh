cd lib-a # Package with 2 versions
sed -i 's/version = .*/version = "0.0.1"/g' conanfile.py
conan create .
sed -i 's/version = .*/version = "0.0.2"/g' conanfile.py
conan create . && cd ..

cd lib-b && conan create . && cd ..
cd lib-c && conan create . && cd ..
cd lib-d && conan create .