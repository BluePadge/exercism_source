class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {
//		String numStr = String.valueOf(numberToCheck);
//		int length = numStr.length();
        int numberTemp = numberToCheck;
        int armstrongNumber = 0;
//		for (int i = 0; i < length; i++) {
//		    armstrongNumber += Math.pow(Integer.parseInt(String.valueOf(numStr.charAt(i))),length);
//		}
        while (numberTemp > 0) {
            int n = numberTemp % 10;
            armstrongNumber += Math.pow(n,)
            numberTemp %= 10;
        }

        return armstrongNumber == numberToCheck;
    }

}
