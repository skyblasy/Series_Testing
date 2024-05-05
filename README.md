# Series_Testing
Testing Difference in Series Central Tendencies 

Taking two samples through a decision tree of tests depending on the nature of the data; 

Shapiro-Wilk test for normality
│
├── Both samples normally distributed
│   │
│   ├── Levene's test for equal variances
│       │
│       ├── Equal variances: t-test
│       │
│       └── Unequal variances: Welch's t-test
│
└── At least one sample not normally distributed: Mann-Whitney U test
