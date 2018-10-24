import { group, sleep } from 'k6';
import http from 'k6/http';

// Version: 1.3
// Creator: Load Impact URL test analyzer

export let options = {
    stages: [
        {
            "duration": "5m0s",
            "target": 25
        }
    ],
    maxRedirects: 0,
    discardResponseBodies: true,
};

export default function() {

	group("page_1 - https://www.f5demo.net/", function() {
		let req, res;
		req = [{
			"method": "get",
			"url": "https://www.f5demo.net/",
			"params": {
				"headers": {
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
					"Connection": "keep-alive",
					"Accept-Encoding": "gzip, deflate",
					"Host": "www.f5demo.net",
					"Accept-Language": "en-US",
					"Upgrade-Insecure-Requests": "1",
					"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/62.0.3183.0 Safari/537.36"
				}
			}
		}];
		res = http.batch(req);
		// Random sleep between 5s and 10s
		sleep(Math.floor(Math.random()*5+5));
	});

}
