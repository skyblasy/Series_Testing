class SampleComparison:
    def __init__(self, sample1, sample2):
        self.sample1 = sample1
        self.sample2 = sample2
        self.alpha = 0.05

    def run_tests(self):
        # Perform Shapiro-Wilk test for normality
        normality_test_result = self.shapiro_wilk_test()

        if normality_test_result:
            # If both samples are normally distributed, perform Levene's test for equal variances
            equal_variances = self.levene_test()

            if equal_variances:
                # If variances are equal, perform t-test
                self.t_test()
            else:
                # If variances are unequal, perform Welch's t-test
                self.welch_test()
        else:
            # If either sample is not normally distributed, perform Mann-Whitney U test
            self.mann_whitney_u_test()

    def shapiro_wilk_test(self):
        # Perform Shapiro-Wilk test for normality on both samples
        _, p_value1 = stats.shapiro(self.sample1)
        _, p_value2 = stats.shapiro(self.sample2)

        if p_value1 > self.alpha and p_value2 > self.alpha:
            print("Both samples are normally distributed.")
            return True
        else:
            print("At least one sample is not normally distributed.")
            return False

    def levene_test(self):
        # Perform Levene's test for equal variances
        _, p_value = stats.levene(self.sample1, self.sample2)

        if p_value > self.alpha:
            print("Variances are equal.")
            return True
        else:
            print("Variances are unequal.")
            return False

    def t_test(self):
        # Perform t-test for equal variances
        _, p_value = stats.ttest_ind(self.sample1, self.sample2)
        print(f"T-test p-value: {p_value}")

    def welch_test(self):
        # Perform Welch's t-test for unequal variances
        _, p_value = stats.ttest_ind(self.sample1, self.sample2, equal_var=False)
        print(f"Welch's t-test p-value: {p_value}")

    def mann_whitney_u_test(self):
        # Perform Mann-Whitney U test
        _, p_value = stats.mannwhitneyu(self.sample1, self.sample2)
        print(f"Mann-Whitney U test p-value: {p_value}")