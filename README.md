# **Kandy** Python Library Examples

Examples for **[Kandy.io](https://www.kandy.io/)** [REST API](https://developer.kandy.io/docs/rest-api) _**[Python wrapper](https://pypi.python.org/pypi/Kandy/)**_.

&nbsp;

## Library
- [Source](https://github.com/aharshac/KandyPy)
- [Docs](https://github.com/aharshac/KandyPy/wiki)

&nbsp;

## Examples
The following examples are present in this package.    
* SMS.py    
Send SMS to a mobile number via Kandy.

&nbsp;

## Building and running examples
1. Open terminal window.

2. Install Kandy Python Library     
We will download and install it from [**PyPI** - The Python Package Index](https://pypi.python.org/pypi/Kandy/)    
Execute `pip install kandy` in terminal.     

3. Clone **Kandy Python Library Examples**    
Execute `git clone https://github.com/aharshac/KandyPyLibExamples.git`

4. Change directory to *KandyPyLibExamples*    
Execute `cd KandyPyLibExamples` in terminal.

5. Add **Kandy** authentication and personal data to source file `SMS.py`.    
  * Substitute **`<domain_api_key>, <domain_secret>, <user_id>`** with data from [Kandy Developer Dashboard](https://developer.kandy.io/)
  * Replace **`<source_phone_number>, <destination_phone_number>, <message>`** with personal data.

6. Run example.    
Execute `python SMS.py` in a terminal.
