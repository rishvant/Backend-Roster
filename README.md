# Roster Backend Engineer Assessment - Web Scraper

## 📋 Overview

This project extracts supplier profiles (UGC Creators and Video Editors) from the Twine platform, delivering clean, validated data for Roster's operational needs.

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Ensure Chrome WebDriver is installed
# Download from: https://chromedriver.chromium.org/
```

### Running the Scraper
```bash
python twine_scraper.py
```

### Expected Output
- CSV file with 100+ validated profiles
- Console logs showing scraping progress
- Statistics summary on completion

## 📁 Project Structure

```
roster-web-scraper/
├── README.md                          # This file
├── twine_scraper.py                   # Main scraping script
├── scraped_profiles.csv               # Sample output (50 profiles)
├── Technical_Documentation.md         # Detailed technical write-up
├── requirements.txt                   # Python dependencies
└── .gitignore                         # Git ignore rules
```

## ✨ Features

### Core Functionality
- ✅ Selenium WebDriver for dynamic content handling
- ✅ BeautifulSoup4 for HTML parsing
- ✅ Automated pagination (handles 50+ profiles per role)
- ✅ Rate limiting (2-second delays between requests)
- ✅ Comprehensive error handling and logging

### Data Validation (5-Layer Pipeline)
1. **Email Format Validation** - Regex pattern matching
2. **Brand Name Filtering** - Removes Studio, Agency, LLC, Inc, etc.
3. **Test Data Detection** - Filters test@test.com and placeholder entries
4. **Duplicate Detection** - Email-based deduplication
5. **URL Validation** - Ensures complete, valid profile links

### Data Quality Standards
- Valid email format (RFC 5322 compliant)
- Individual person names only (no brands/agencies)
- Complete profile URLs (https://www.twine.net/profile/...)
- No test or placeholder data
- Zero duplicates

## 📊 Output Format

CSV file with the following columns:
- `name` - Full name of the freelancer
- `email` - Valid email address
- `profile_link` - Complete Twine profile URL
- `role_type` - Either "UGC Creator" or "Video Editor"

## 🎯 Scalability to 1,000+ Profiles

### Current Performance
- 50 profiles per role: ~5-8 minutes
- Memory footprint: <100MB

### Scaling Strategy
- **Parallel Processing**: ThreadPoolExecutor with 5-10 workers
- **Distributed Architecture**: Scrapy framework with Redis queue
- **Database Integration**: PostgreSQL/MongoDB for incremental updates
- **Proxy Rotation**: IP management for rate limit avoidance
- **Checkpoint System**: Resume-on-failure capability

**Estimated Performance at Scale:**
| Profiles | Sequential Time | Parallel Time |
|----------|----------------|---------------|
| 100      | 10 min         | 5 min         |
| 500      | 50 min         | 10 min        |
| 1,000    | 100 min        | 20 min        |

## 🔧 Configuration

### Headless Mode
```python
scraper = TwineScraper(headless=True)  # Background scraping
scraper = TwineScraper(headless=False) # Visible browser (debugging)
```

### Target Count
```python
scraper.run(target_per_role=50)  # 100 total profiles
scraper.run(target_per_role=100) # 200 total profiles
```

## 📝 Technical Details

### Tools & Technologies
- **Python 3.9+** - Core language
- **Selenium 4.15+** - Browser automation
- **BeautifulSoup4** - HTML parsing
- **Chrome WebDriver** - Browser driver
- **CSV module** - Data export

### Key Challenges Solved
1. Dynamic JavaScript content loading
2. Email accessibility and extraction
3. Brand vs individual detection
4. Rate limiting and IP blocking prevention
5. Data quality assurance

See `Technical_Documentation.md` for detailed explanations.

## ⚠️ Important Notes

### Ethical Considerations
- All data scraped from publicly accessible profiles
- Rate limiting implemented to respect server resources
- Data used solely for evaluation purposes
- Recommended to review Twine's Terms of Service

### Production Recommendations
1. Check if Twine offers API access (more reliable)
2. Implement authentication flow if needed
3. Use PostgreSQL for large-scale data storage
4. Set up monitoring with Sentry or similar
5. Verify GDPR/privacy compliance