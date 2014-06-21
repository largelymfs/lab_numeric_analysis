#include <iostream>
#include <cmath>
using namespace std;

const double stand = 0.693147190546;

int get_n(float e){
	int n = 0;
	float ans = 0.0;
	int i = 0;
	int f = -1;
	while (abs(ans - stand) > e){
		i++;
		f = f * -1;
		ans = ans + (1.0/(float)(i)) * (float)(f);
	}
	//std::cout << "Answer : " << ans << std::endl;
	printf("Answer: %.8f\n",ans);
	printf("Err : %.9f\n",abs(ans - stand));
	return i;
}

int main(){
	std::cout << "e = 0.5e-5" << std::endl;
	int n1 = get_n(0.5 * 0.00001);
	std::cout << "N : " << n1<< std::endl;
	std::cout << "e = 0.5e-6" << std::endl;
	int n2 = get_n(0.5 * 0.000001);
	std::cout << "N : " << n2 << std::endl;
	return 0;
}