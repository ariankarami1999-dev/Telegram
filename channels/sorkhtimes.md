<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/izXnxO6cpWykXVvVtxuwIxj-tBQAkqLZJXDlv8sh2wBjXgNld5Umv6PokunRY53q5PfXJQKd_TWwTYxPC7j4QBzmwrgpBFhdtMM8NZ84gk5NDvsMh-8kEUxqRSU55kIwCP-zQArptO9cToN8NyOizkSc1ymvTqPAgkmJ6KoIZHWHwejemC-vdbOZB6ardK28KpmFvzxUWRemPeoqrmh26SSKCBpUDerPbatp9IspSqhXHoETH4a663k9GT5Re_joer_VTa9ww0RMGh9tcZXvF1sE8dEAw-DatIHSuru9JT1cLDdHJLbXvbzQsnEIZoapRJNO5wnHQFbd1oTecYfOjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 22:40:19</div>
<hr>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎙
🎙
محمدمهدی محبی : اگه یه چیز در مورد هوادارای پرسپولیس بخوام بگم بازی استقلال خوزستان تو ذهنم میاد که تا لحظه آخر حمایت کردن‌. امسال تیممون جوون شده اگه به امید خدا این نسل بگیره مثل دوران آقای برانکو میتونیم چند سال قدرتمند ظاهر شیم و به حمایت هوادارا نیاز…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/137667" target="_blank">📅 22:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
محمد مهدی محبی: اسطوره های من اقای مهدوی کیا و شماره ۸ واقعی پرسپولیس علی آقا کریمی رو دوست داشتم. امیدوارم بتونیم مثل اینها بشیم و کارهای اینا رو انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 247 · <a href="https://t.me/SorkhTimes/137666" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412b5348dd.mp4?token=GvZXRKWkFlHq78afgeAZ9_GZhDoAiJvG79avtyYDLg5izXROO5nKo0qe0tlXZ4x5yCzrQLZnCFtjMtzQZrfqAYzAluGFbFLL_X_8sb6BnqLFJrrvgmXU_vIfN9d0W2NQnjio_7IB5o-4I6q_8yqoGEzitdiQHnFul5Er9rYpNfyiTjVlksj1o9YaOe5yQDvk1wCEmdYqUyBi7awUklQgH9lTrDcHmeyiipKfOAlWkwHNWoXfzaXKhatLpfkgx42NE0i3uDB4R482ZzD8B25QCY6ifvWY6sjzUiu46177TwH8LRcclym65oxVCSmq_ei6ZktAih582aOQEAUpPJpz4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412b5348dd.mp4?token=GvZXRKWkFlHq78afgeAZ9_GZhDoAiJvG79avtyYDLg5izXROO5nKo0qe0tlXZ4x5yCzrQLZnCFtjMtzQZrfqAYzAluGFbFLL_X_8sb6BnqLFJrrvgmXU_vIfN9d0W2NQnjio_7IB5o-4I6q_8yqoGEzitdiQHnFul5Er9rYpNfyiTjVlksj1o9YaOe5yQDvk1wCEmdYqUyBi7awUklQgH9lTrDcHmeyiipKfOAlWkwHNWoXfzaXKhatLpfkgx42NE0i3uDB4R482ZzD8B25QCY6ifvWY6sjzUiu46177TwH8LRcclym65oxVCSmq_ei6ZktAih582aOQEAUpPJpz4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽
محمدمهدی زارع: آقای تارتار به من زنگ زد و گفت اگر به پرسپولیس بروی موفق تر از رفتن به استقلال می شوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 368 · <a href="https://t.me/SorkhTimes/137665" target="_blank">📅 22:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
محمدمهدی محبی: آرزوی هربازیکنی، بازی در پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/SorkhTimes/137664" target="_blank">📅 22:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7f1f896e.mp4?token=Ugyd1pNVYve4iINVBriJCIg7Pa_ye5GMxpTNVtqrK6UZm8fCTnCb14VnzfQP-bEee6f8QB2ULq07HhBnQTl6X7zrcDAY5gPrP0V3giyLk3PI8Lf0DLPudsP6iTHsiQw-ZJymVtL-jmzNS8gBmrRnHJIi8NTeKoxCIAYcz_3JCi8vUGzyKQ5tDScNGeVEyJbUJOLIvHbfRnayJaSupqrjG1SP0QDQr2tj-XgV9uIAXqGWf1ij1QNB-KEDyc1dhXr7FCisl-LynKQv6qOenETR80q4uBBlCkICF8oVz5OZtDYS2nEC1vjyu6OcXxTbDqBs4haVJJe1nsbNnwq---TDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7f1f896e.mp4?token=Ugyd1pNVYve4iINVBriJCIg7Pa_ye5GMxpTNVtqrK6UZm8fCTnCb14VnzfQP-bEee6f8QB2ULq07HhBnQTl6X7zrcDAY5gPrP0V3giyLk3PI8Lf0DLPudsP6iTHsiQw-ZJymVtL-jmzNS8gBmrRnHJIi8NTeKoxCIAYcz_3JCi8vUGzyKQ5tDScNGeVEyJbUJOLIvHbfRnayJaSupqrjG1SP0QDQr2tj-XgV9uIAXqGWf1ij1QNB-KEDyc1dhXr7FCisl-LynKQv6qOenETR80q4uBBlCkICF8oVz5OZtDYS2nEC1vjyu6OcXxTbDqBs4haVJJe1nsbNnwq---TDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
محمدمهدی محبی: آرزوی هربازیکنی، بازی در پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/SorkhTimes/137663" target="_blank">📅 22:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0ef813af.mp4?token=qge3P_oTMWSLQLd3gXPpBC0CBUa_dnuKmQLIANxjWArLvALNLwICEA-ATK_4BQ-oc5BTzoLV6xds59LeCwpre-UezchkS-JapJtz87gecXHzqSa3SKxZ8XcoA7o1UjeI0JM_ClWjQ8TTVFSvW8RF7st3Ib3CzMkcrGtJtJH9gPrAzAyimDWbYCRr9qQpodhkivo0pjNCDkqDlx5xknyZoELwN4M4Aw6EPt3LPqLdgTOciU24YRAHEdFP7oSLEBNmzr21IDG85gzBLFOPs2XSduKpKXt1--3FhM8hIq8KQUZkqUWX5H2gVYJdphjYwV3q-_ocE_u3vDbFbI1rdjC-ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0ef813af.mp4?token=qge3P_oTMWSLQLd3gXPpBC0CBUa_dnuKmQLIANxjWArLvALNLwICEA-ATK_4BQ-oc5BTzoLV6xds59LeCwpre-UezchkS-JapJtz87gecXHzqSa3SKxZ8XcoA7o1UjeI0JM_ClWjQ8TTVFSvW8RF7st3Ib3CzMkcrGtJtJH9gPrAzAyimDWbYCRr9qQpodhkivo0pjNCDkqDlx5xknyZoELwN4M4Aw6EPt3LPqLdgTOciU24YRAHEdFP7oSLEBNmzr21IDG85gzBLFOPs2XSduKpKXt1--3FhM8hIq8KQUZkqUWX5H2gVYJdphjYwV3q-_ocE_u3vDbFbI1rdjC-ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا شهرآبادی: مقابل منتخب کرج وقتی 6 گل زدم دیگر گلی نزدم تا شش بماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/137662" target="_blank">📅 22:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ceeaa77c.mp4?token=Ga0gjyazHmS-2XPLAFTuWL-8gFof8f7DhB74Bh9Ikw5Pf__TmeSvVr7f3mpnvwxAqUNV_CBt7Dk1DwmmhNiRQhkSfUVf4UZgkXHmFZ6JZXGXbra_cX4P3USA0rHKMJ-AOTcNuF9zytMyIoZ9sBO6QUuE1VocAuZSRS3N2E26An7zK5cSmDtrsTT0UCoOGpn4VSw_n8C5mlVDDnUt2SaxcWZ1Ezagha9ZiUf4slTcyVFu3K4DD_l0hINvH3UfwAcY95Lhz54uQKMS4TqgjFWAoxQ_djeRtEJy75ynW4Ok5fav6jkVWG9zp_MjXJqdPg3ijXbjJtn4xZc7WMI_ZgkIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ceeaa77c.mp4?token=Ga0gjyazHmS-2XPLAFTuWL-8gFof8f7DhB74Bh9Ikw5Pf__TmeSvVr7f3mpnvwxAqUNV_CBt7Dk1DwmmhNiRQhkSfUVf4UZgkXHmFZ6JZXGXbra_cX4P3USA0rHKMJ-AOTcNuF9zytMyIoZ9sBO6QUuE1VocAuZSRS3N2E26An7zK5cSmDtrsTT0UCoOGpn4VSw_n8C5mlVDDnUt2SaxcWZ1Ezagha9ZiUf4slTcyVFu3K4DD_l0hINvH3UfwAcY95Lhz54uQKMS4TqgjFWAoxQ_djeRtEJy75ynW4Ok5fav6jkVWG9zp_MjXJqdPg3ijXbjJtn4xZc7WMI_ZgkIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
پوریا شهرآبادی:
🔹
خانواده من شاهد هستند که از بچگی پرسپولیسی‌ بودم
❌
❌
قبل از اینکه به استقلال بروم در نوجوانان پرسپولیس بازی می کردم. در زمان فرزاد آشوبی در تیم نوجوانان پرسپولیس بودم و گل هم زدم. در خوابگاه خواب بودیم که سرپرست تیم زنگ زد و گفت ظرفیت پر شده است و بعد به استقلال رفتم. با دایی‌ام پرسپولیسی‌ شش آتیشه بودم. شاید اگر به استقلال نمی‌رفتم به آرزوی بچگی‌ام نمی‌رسیدم. آرزوی بچگی من پوشیدن پیراهن پرسپولیس بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/137661" target="_blank">📅 22:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba743cb41.mp4?token=Pv8YudxjOo5Xm9XT0yiVymO5VHXIMtbtQ6SeDh9fESYTXRLuLCXP8rgTIHjK4ldJiCjFfgvJSHp3qh0qX1bQowUvmQvSGhxsgzQoKzLZOk7NqOe7DgI-zG0ZylwhF8VjwFzslbQEg7W-Er1upk8k7E3krsG5XSqtUhO1Mrz0uglBQ57KWTJW0g3B2VQr4sFz1PJ4LVXFNkmhP9mO8JjKSpOLc1uHiRNhwwO02PZOfoo-Ib0nWc02PGFLix_6_ldHN6QbPpXB93oh5M1JzW7R_eSyMEA9vzEwB0Fkr2LbDrTyuGLkYc05K5TMpY9qZPdJULIBaQS-hhZp6w3__o_Vvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba743cb41.mp4?token=Pv8YudxjOo5Xm9XT0yiVymO5VHXIMtbtQ6SeDh9fESYTXRLuLCXP8rgTIHjK4ldJiCjFfgvJSHp3qh0qX1bQowUvmQvSGhxsgzQoKzLZOk7NqOe7DgI-zG0ZylwhF8VjwFzslbQEg7W-Er1upk8k7E3krsG5XSqtUhO1Mrz0uglBQ57KWTJW0g3B2VQr4sFz1PJ4LVXFNkmhP9mO8JjKSpOLc1uHiRNhwwO02PZOfoo-Ib0nWc02PGFLix_6_ldHN6QbPpXB93oh5M1JzW7R_eSyMEA9vzEwB0Fkr2LbDrTyuGLkYc05K5TMpY9qZPdJULIBaQS-hhZp6w3__o_Vvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کوروش اژدهاکش، بازیکن جدید پرسپولیس:
❌
اجدادمان گفته‌اند اژدهاکش بوده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/137660" target="_blank">📅 22:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7ba4ecee.mp4?token=nUYhlYAdFYYgxeMZV_wL9Du9ir5lBur2_ueELBPppKBh0E_3dnzR6dPO_u_OClzouytXZCb8c-k6ue6X8cm_GdJkJ28oXeZ5wmIPSbgldvPZup0bxBwy3yhRS5z7IiBBSxcc4BY8l6si4WauPKCSGbIELlOqPD_TuT4JZbKSB9o2x6tw2XvLcYZ-WsEV34cHiLZPmwTHtSjKcG7m4QWFKTIYl_1PIuOJOOWfiJLTgH1LPHhJtBdeuJHLYtUJRuwvp3u5CVYPZgnive9CK2fE6A70Saa9Ao14WEM6wVPtmw4DyGUGRFiOaqiCMDEJzmAQ9CqA2MOpvx6YkQPyzyxpsgh0mEjcSeUq7SfLS4RRK3cD2TknPadJrTa9Fu3-l-VLAR09FzrBbKR_Udi0zbXugJ6VXbXxkaMiM5h3AD4P8NLWhG278icfQEN1ujj-3NGXkZ6kyLEBXQBr_vE6KpFavAXy7gtpyF2eNTK432Wl7qYzdM5RccdYJ4EuR2dwrcUWv5FRcMXRFrX_uali9tmAV8dyjOYVxseW7cg-HLCoOITUOS8CLdboHmvM_kltb-lsXW8SgmXdf8IatnTDkVIJ8kfcSC2tVFobnsfVmVkLoYjOHlb3n8t4rqKS0lGOubh5k-ApNp9QMnWaeRjXtYlGRKdahnBxpiYJ8SJSCxsTQNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7ba4ecee.mp4?token=nUYhlYAdFYYgxeMZV_wL9Du9ir5lBur2_ueELBPppKBh0E_3dnzR6dPO_u_OClzouytXZCb8c-k6ue6X8cm_GdJkJ28oXeZ5wmIPSbgldvPZup0bxBwy3yhRS5z7IiBBSxcc4BY8l6si4WauPKCSGbIELlOqPD_TuT4JZbKSB9o2x6tw2XvLcYZ-WsEV34cHiLZPmwTHtSjKcG7m4QWFKTIYl_1PIuOJOOWfiJLTgH1LPHhJtBdeuJHLYtUJRuwvp3u5CVYPZgnive9CK2fE6A70Saa9Ao14WEM6wVPtmw4DyGUGRFiOaqiCMDEJzmAQ9CqA2MOpvx6YkQPyzyxpsgh0mEjcSeUq7SfLS4RRK3cD2TknPadJrTa9Fu3-l-VLAR09FzrBbKR_Udi0zbXugJ6VXbXxkaMiM5h3AD4P8NLWhG278icfQEN1ujj-3NGXkZ6kyLEBXQBr_vE6KpFavAXy7gtpyF2eNTK432Wl7qYzdM5RccdYJ4EuR2dwrcUWv5FRcMXRFrX_uali9tmAV8dyjOYVxseW7cg-HLCoOITUOS8CLdboHmvM_kltb-lsXW8SgmXdf8IatnTDkVIJ8kfcSC2tVFobnsfVmVkLoYjOHlb3n8t4rqKS0lGOubh5k-ApNp9QMnWaeRjXtYlGRKdahnBxpiYJ8SJSCxsTQNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
پویا پورعلی:
❌
به مهرداد میناوند قول داده بودم روزی پیراهن پرسپولیس را می‌پوشم.
❌
از 5 سالگی پدر و مادرم برای پیراهن پرسپولیس خریدند و من با آن پیراهن شب‌ها می‌خوابیدم.
❌
از مهرداد میناوند که مربی‌ام بود یاد می‌کنم.
❌
در خونه به خونه نزدیک بود فوتبالم تمام شود اما مهرداد میناوند 5 الی 6 ماه درگیر کارهای پزشکی من بود.
❌
اميدوارم امسال قهرمان شویم و جام را به مهرداد میناوند تقدیم کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTi</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/137659" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc72057e80.mp4?token=STKLFLCKqyX0Qmyv2CDLDSKp0G9v8H-4zEgshC_2h2SpQ_ZTDzUxAHRW-1mRcyzrKGcn6KWjlxRBFavkNau6cJuBn4gtjTQyRiXk3exxR6JYF-bBEn9segCHsM1VKFWmukkIgNoAx1CE6nqheKU_v7wD96cNYxjOR8tuIcmK9Frucoc6_X_4X0cCBuPyre8rAyh_n_Z8TUcxMOpoG-8MyOK1IgAT6Hf_ao1vpWPYJvAuxg6JyS5gp07XdApv2jn_BtAWytemBu-1LAKv0yXu6-Syj1EapCbiaNxzzSApJ47BEPSdiq90j4DiFauYM4E8JAWiLjbRQRocWlCQCZ1ZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc72057e80.mp4?token=STKLFLCKqyX0Qmyv2CDLDSKp0G9v8H-4zEgshC_2h2SpQ_ZTDzUxAHRW-1mRcyzrKGcn6KWjlxRBFavkNau6cJuBn4gtjTQyRiXk3exxR6JYF-bBEn9segCHsM1VKFWmukkIgNoAx1CE6nqheKU_v7wD96cNYxjOR8tuIcmK9Frucoc6_X_4X0cCBuPyre8rAyh_n_Z8TUcxMOpoG-8MyOK1IgAT6Hf_ao1vpWPYJvAuxg6JyS5gp07XdApv2jn_BtAWytemBu-1LAKv0yXu6-Syj1EapCbiaNxzzSApJ47BEPSdiq90j4DiFauYM4E8JAWiLjbRQRocWlCQCZ1ZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
امیرحسین طاهری، بازیکن جدید پرسپولیس: امسال در لیگ، حذفی و سوپرجام قهرمان می‌شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/137658" target="_blank">📅 22:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
بازگشا :
❌
❌
اردوی خوبی در ارزروم داشتیم و امیدواریم فصل خوبی را شروع کنیم.
❌
❌
در پرسپولیس همه مجموعه امسال به دنبال آرامش تیم هستیم تا به سمت قهرمانی برویم.
❌
❌
❌
در باشگاه پرسپولیس ما نمیخوایم پول هوادار و پول سهامدار رو خرج رسانه کنیم. رسانه بخریم که…</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/137657" target="_blank">📅 21:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
بازگشا تو لایو باشگاه
❌
❌
هواداران پرسپولیس تحت تأثیر رسانه در تلگرام و اینستاگرام میان کامنت میزارن که فلان بازیکن رو بگیریم خب ما اون بازیکن رو جذب نمیکنیم چون تو برنامه و لیست نیاز باشگاه نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SorkhTimes/137656" target="_blank">📅 21:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/137655" target="_blank">📅 21:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5143f09995.mp4?token=CJEx3E14BdYmQbu9O2hf36Ac8uOjlzcJioqIqMPchq8aY30IzqIVo0vfO3vPxoueQ_luuHOaABqArx0qT364JMA8C_DdhMF7PE4F8NBhZJIYhfDwaYKtPDWOmEn1REdhFSEsBQ1Pmiel6EbD7ikvLC8FTqSgZ2q4KILgDVBu_ohHkv1nfosg8TjuMV2vGgyU6FV0LjASYSmyTTXtJVnPSVp_Rjme_lEMWJPYGq9dW4ya3Z0TqYrdrFGA59BLBIBpWGTe72Pp3jdt7HeKAaw4E_Vt8KSsWFoV8yNTUOoRXpaq6rPZ7JGtR7Cs-nMXevsOWoZK62OGCRbjGadUQiIQnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5143f09995.mp4?token=CJEx3E14BdYmQbu9O2hf36Ac8uOjlzcJioqIqMPchq8aY30IzqIVo0vfO3vPxoueQ_luuHOaABqArx0qT364JMA8C_DdhMF7PE4F8NBhZJIYhfDwaYKtPDWOmEn1REdhFSEsBQ1Pmiel6EbD7ikvLC8FTqSgZ2q4KILgDVBu_ohHkv1nfosg8TjuMV2vGgyU6FV0LjASYSmyTTXtJVnPSVp_Rjme_lEMWJPYGq9dW4ya3Z0TqYrdrFGA59BLBIBpWGTe72Pp3jdt7HeKAaw4E_Vt8KSsWFoV8yNTUOoRXpaq6rPZ7JGtR7Cs-nMXevsOWoZK62OGCRbjGadUQiIQnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/137654" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
تارتار رسماً با جدایی ابرقویی مخالفت کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/137653" target="_blank">📅 21:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2nepFcyiyypvy22oIkIk0RokVC6ruK6nx9FJ7OTQg10brQI5jqh4SO0_Tp-Tw6mJFjB9dF-LKCTLzz86PY7WH6i0RrOo_NZ3tx03qUBLji7lyj6VpQTObMCoEnzfxV03_pNP4HbH_u-hV-_jymR2WIw5FiTRpuw3gcXz5KtjVLXBCaN8eia8f3b36TSezfxCTkUB35X0q10HQXzNLY2_Wc2dxEFTco8o4f500QAKowbIdqhcn1S50rgfTxWZ8SJN6zPo6RcPPmy6u-jjtjLDucwQeNXhfTMcuT3JOOLCYwetBk2FiHuSnSVP4vP6Bno0_ycNDRu5MXJwETkf__NnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد قدرت و جوانی؛ شلتون مقابل فونسکای آماده برای شگفتی!
🎾
Joao Fonseca -
🎾
Ben Shelton
🎾
فونسکا بعد از برد مقتدرانه مقابل کسپر رود، با اعتمادبه‌نفس بالا وارد این جدال می‌شود؛ اما سرویس و قدرت اول ضربات شلتون همچنان برگ برنده اوست. شرایط هاردکورت مونترال و بازی شبانه می‌تواند به فونسکا کمک کند، ولی اگر شلتون درصد سرویس اول بالایی داشته باشد، کنترل رالی‌ها برای برزیلی جوان سخت می‌شود. بازی نزدیک و پر از گیم‌های کوتاه؛ شلتون اندکی شانس بیشتری برای صعود دارد.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/137652" target="_blank">📅 21:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfotsjlkX5nLOU2XJyD_fVEdL0TshOTwsJ21ekdDY6jZswZ3MvQIltSizKgCCuvzXu1E8C-zE8v9Z5hkRauEjnZf-j-EOH-m1i91FGzAeswjrSmOvF5s6AAO0j1FVsCb0ZaB0ktltaVkLmUY2LtKnRG7P--3svCyvH2kwN6OZ66GRAaVAO9hFyJOtbWNaFP5Anh2ZI9c6PmI6_kfrLlO2OMkagG571-nrvPOoxdnSCDCjhBJiaihZk-QaJQ877L2Nz6Elj64oe_BtDxtbel6CEIIqPG5dQrLE4ETu70a_rd_dm0orrzqjiccyC1a8DNS49sgHgLYrbW2gwcnmXj66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مهدی تارتار با پسراش پیش از بازی تدارکاتی امروز که تو منتخب کرج بازی میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/137651" target="_blank">📅 21:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
محمد قربانی به مدیران الوحده امارات گفته دوست دارم برم پرسپولیس. اونا هم گفتن هر تیمی زودتر رضایت‌نامه رو پرداخت کنه، میری همونجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/137650" target="_blank">📅 21:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
وحید فاضلی در گفتگو با ورزش سه :
▫️
ما حداقل به 3 بازیکن دیگه نیاز داریم تا اسکواد تیممون بالانس بشه. در یک پست 2 الی 3 بازیکن داریم ولی در پست دیگه شاید 1 بازیکن داشته باشیم. پرسپولیس مثل تیم ملی باید 2 بازیکن تاپ لول در هر پست داشته باشه.
▫️
از ابتدا…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/137649" target="_blank">📅 20:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
میگن دیروز تو بازی دوستانه تراکتور و شمس آذر شجاع خلیل زاده بعد از پایان بازی با محمد ربیعی سرمربی این تیم درگیر میشه و همراه بیرانوند شبانه میرن سراغ زنوزی و خواستار برکناری ربیعی میشن و ربیعی هم همون دیشب حکم اخراجش میخوره و برمیگرده تهران و بجای اون نکونام…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/137648" target="_blank">📅 20:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
ابرقویی به‌خاطر نگرانی از نیمکت‌نشینی در پرسپولیس، به دنبال رفتن به سپاهان است
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/137647" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137646">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
✅
باشگاه نساجی به پرسپولیس اعلام کرده است تنها در صورت جذب یاسین جرجانی از آلومینیوم اراک اجازه جدایی دانیال ایری را خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/137646" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137645">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
اعضای کادرفنی تیم پرسپولیس :
🔴
سرمربی : مهدی تارتار
🔴
دستیار مربی: وحید فاضلی
🔴
دستیار مربی: علیرضا محمد
🔴
دستیار مربی  : رضا جباری
🔴
دستیار مربی  : کریم باقری
🔴
مربی دروازه بان : حسین اینانلو
🔴
مربی بدنساز: یاگو
🔴
آنالیزور: میعاد قاسم زاده و محمد کهن  …</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/137645" target="_blank">📅 19:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137644">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
✔️
✔️
سرخپوشان در نیمه نخست با گل‌های ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدری، با پنج گل از حریف پیش افتادند.
✔️
✔️
در نیمه دوم نیز پوریا شهرآبادی…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/137644" target="_blank">📅 19:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137643">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
پرسپولیس نیمه اول بازی دوستانه با منتخب کرج رو ۵-۰ برد؛
⁉️
گل‌ها:   ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/137643" target="_blank">📅 19:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه پرسپولیس‌برای‌فروش‌حسین ابرقویی به باشگاه فولاد مبارکه سپاهان منتظر تاییدیه مهدی تارتاره. درصورت اوکی دادن تارتار ابرقویی راهی سپاهان خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/137642" target="_blank">📅 18:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137640">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYkPGWTDs8SfnWIKeSnOhPy6JB00NnzZrq3nA95vo8r4Eq040DFaefLCfnVFsxUv2oYRsPV4KlvLYZ1ZL3hDeWo1MbLg1jLYCyWtwZ5biHq4Gv6wwcuJfcY9vr6meB7N5NI7zzUoQRh9cJSEoyGE52ttnLPRzmUos6Ijcu0FFD8MYF7kFTsZpAaOYwfU-3sieqGZ8QssbpsYaxHO1WWlCzEVjmC8kMEKZ-tS9SNmfU3g_06EBcoO-GPpAgNH064uLk9K9QZEg89b3qHVP3k2WQPHub3vz8qDJO8yJIPTgCSzLp3AT18tW5gGOP5uRCI1-dl-_L744HMKoIDlvblZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس نیمه اول بازی دوستانه با منتخب کرج رو ۵-۰ برد؛
⁉️
گل‌ها:
ایگور سرگیف، یاسین سلمانی، امیرحسین محمودی، علیرضا همائی‌فر و مهدی تیکدر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/137640" target="_blank">📅 18:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137639">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
باشگاه سپاهان اصفهان امروز برای چهارمین بار برای جذب حسین ابرقویی نژاد به باشگاه پرسپولیس نامه زد ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/137639" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137638">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
پیگیری‌ها برای جذب قربانی همچنان  ادامه داره/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/137638" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137637">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
مبالغ رضایت نامه ای که پرسپولیس تا الان پرداخت کرده:
🔴
محمد مهدی زارع : 170 میلیارد تومن
🔴
پوریا شهرآبادی : 150 میلیارد تومن
🔴
پوریا لطیفی فر : 150 میلیارد تومن
🔴
محمدمهدی محبی : 80 میلیارد تومن
🔴
کوروش اژدهاکش : 30 میلیارد تومن
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/137637" target="_blank">📅 17:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137636">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
❌
حجت کریمی، مدیرعامل تراکتور در نشست خبری عقد قرارداد با نکونام:
❌
❌
پیگیر جذب محمد قربانی هستیم. ۲۰ روز است با باشگاه اماراتی مذاکره می کنیم. قسمت شود با این ملی پوش قراداد خواهیم بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137636" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/137635" target="_blank">📅 17:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
ویژه برنامه تلویزیون پرسپولیس با حضور بازیکنان جديد تیم
✔️
✔️
در این برنامه، چهره‌های تازه‌وارد پرسپولیس حضور خواهند داشت و درباره شرایط خود، حضور در جمع سرخ‌پوشان و حال‌وهوای تیم با هواداران گفت‌وگو خواهند کرد.
❌
❌
این ویژه‌ برنامه از ساعت ۲۱ به صورت زنده…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/137634" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
خبرنگار ایرنا ادعا کرده در شرایطی که باشگاه پرسپولیس آماده پرداخت مبلغ رضایت‌نامه قربانی بود؛ باشگاه الوحده اعلام کرد به هیچ وجه حاضر به فروش قربانی نیست
✍️
ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/137633" target="_blank">📅 17:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
❌
حجت کریمی، مدیرعامل تراکتور در نشست خبری عقد قرارداد با نکونام:
❌
❌
پیگیر جذب محمد قربانی هستیم. ۲۰ روز است با باشگاه اماراتی مذاکره می کنیم. قسمت شود با این ملی پوش قراداد خواهیم بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137632" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
حجت کریمی، مدیرعامل تراکتور در نشست خبری عقد قرارداد با نکونام:
❌
❌
پیگیر جذب محمد قربانی هستیم. ۲۰ روز است با باشگاه اماراتی مذاکره می کنیم. قسمت شود با این ملی پوش قراداد خواهیم بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/137631" target="_blank">📅 16:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137630">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
❌
آخرین خبر درباره قربانی
✔️
✔️
این بازیکن در لیست خروج الوحده قرار داره حتی با تیم تمرین نمی کنه
✔️
✔️
باشگاه الوحده رابطه خیلی خوبی با ایجنت این بازیکن داره تمام کار جدایی اش به این فرد سپرده
✔️
✔️
پیشنهاد خارجی انچنانی نداره تراکتورم از یه مبلغ بیشتر بهش…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/137630" target="_blank">📅 16:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137629">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری از فارس
🚨
مهدی تارتار اعلام کرده نیازی به جذب رامین رضاییان 36ساله نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/137629" target="_blank">📅 16:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137628">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6oBq3pvsldK9WQVXAQME-fUoCmbsHaucVkE7x4loCDOax6LYA4_SpVPLKRUseGeDDrED5uyf0Jqu2zlrKd1n-zOG9SA0n_Gb2Blk2OAy1S8bjsTyivvqaQPnvyIIcg8JKSXF5i_ZjiwaJKzwiq-YiwO3Lw1c2LGwXPqYz4EGCD7XRYNPsxb_6sDuN9YmsWd6nJo53LXQyuX-3D4XLXMrEY6uS5ccP67cy9VY7n0lWCojF57AjlFMHgB2PPlUuiSVTk0P0lQgjGN2PcFUCpsnUDHwtlyLFO-tbYsGcjjT9Xj80hbcZeuR2voKVI2yjESrNKTC-FfZZ3oF2CMqStSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
داریوش شجاعیان به تیم شناورسازی قشم پیوست و شاگرد مجتبی جباری شد.
🙃
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/137628" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137627">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
رئیس هیئت فوتبال تهران: ورزشگاه آزادی و تختی تا پایان سال به بازی‌های لیگ نمی‌رسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137627" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137626">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137626" target="_blank">📅 14:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137625">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137625" target="_blank">📅 13:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137624">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔄
🔄
🔄
گفته میشه باند شجاع خلیل زاده و علیرضا بیرانوند از محمد ربیعی در تمرینات تراکتور راضی نبودن و شبونه رفتن دفتر زنوزی و محمد ربیعی رو برکنار کردن...!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137624" target="_blank">📅 13:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137623">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuFwpMEfeGUKQuSR8c8O9ROaVZh_x7yS9sg4jbBvGlAPdzVr04l7SdZO9Xn0TV43r4iSGSrXIvCNYRkNn2O69Y42SMNc3kDti-58PvUMZlOy4IGCBUyqZRj4rZZVWnYVq22JcW9eThMUKV7WByRaZdGda7r3HQv3-6OVijUhKQ5ipUJ4LkmJa03t0IawcOCJp6Vy0hCo63xwA_N9YNfg275INaKFSGRP0Nndnoh2Ommif-5n14NgoIDSTG5zsrV7YBUcxHvas8n5BtcN2KysBcw7BM-JydZT54jWLKELL3OSaazeNLVbOwcG-GmzBbUYz-J0__Ds2a85F_jnfppX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
چهار دوئل جذاب، اما این‌بار بدون فشار امتیاز و جدول؛ فرصتی برای آزمون ترکیب‌ها، بازیکنان جدید و تاکتیک‌های متفاوت.
چرخش‌های زیاد و تعویض‌های متعدد می‌تواند معادلات را برهم بزند؛ اینجا کیفیت نمایش مهم‌تر از نتیجه است.
⚡️
دیدارهای دوستانه جذاب امروز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137623" target="_blank">📅 12:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137622">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca828cb00.mp4?token=R6nujIZrOJ0w-mvFv6G9j672GRxAR57-xgOM-3bD356dlN9_ozJDvsXYORcHnTBdARnW7Yu4PJhyM8t3RCbakFsc0eKBjTvpy7bPqSq6sReDp2jVa-o70R6U-vYettVrYKahnyXaRROsZdI314fMTTYyAdVm6YFfuEYCR7VA0k8QUg6WQnbHAiUN5VLa7AU57fYsLvjkNVvAre8L6gq-P9Yu-QNOoWtoiOGZyxKVqf1kTeAs1RzQjpr8DxylMrlN5X3A0GaC3rkcSUpLF3FtaxH5QO8Eks9c74GJHUuHyVK6ccK5nbXEcwLeVZIn8d5tlzlPBGjLiJd_NTOYetBaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca828cb00.mp4?token=R6nujIZrOJ0w-mvFv6G9j672GRxAR57-xgOM-3bD356dlN9_ozJDvsXYORcHnTBdARnW7Yu4PJhyM8t3RCbakFsc0eKBjTvpy7bPqSq6sReDp2jVa-o70R6U-vYettVrYKahnyXaRROsZdI314fMTTYyAdVm6YFfuEYCR7VA0k8QUg6WQnbHAiUN5VLa7AU57fYsLvjkNVvAre8L6gq-P9Yu-QNOoWtoiOGZyxKVqf1kTeAs1RzQjpr8DxylMrlN5X3A0GaC3rkcSUpLF3FtaxH5QO8Eks9c74GJHUuHyVK6ccK5nbXEcwLeVZIn8d5tlzlPBGjLiJd_NTOYetBaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137622" target="_blank">📅 12:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137621" target="_blank">📅 11:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137620" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
فوووووووووووووری
🚨
رامین رضاییان تا دوشنبه مهلت داده به تیم های خواهانش و اگه تیمی سراغش نره با فولاد خوزستان امضا میکنه/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137619" target="_blank">📅 10:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137618">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
بعد از دوسال هنوزم آوارگی ادامه داره
🔽
دربی در اراک برگزار میشه/ایران‌ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137618" target="_blank">📅 10:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137617">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
میگن دیروز تو بازی دوستانه تراکتور و شمس آذر شجاع خلیل زاده بعد از پایان بازی با محمد ربیعی سرمربی این تیم درگیر میشه و همراه بیرانوند شبانه میرن سراغ زنوزی و خواستار برکناری ربیعی میشن و ربیعی هم همون دیشب حکم اخراجش میخوره و برمیگرده تهران و بجای اون نکونام…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137617" target="_blank">📅 10:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137616">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
✔️
ورزش سه: حجت کریمی مدیرعامل تراکتورسازی هم اکنون در جلسه با نکونام هست و تا ظهر نکونام معارفه میشه
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137616" target="_blank">📅 10:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137615">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از فرهیختگان
❌
❌
پرسپولیس برای رضایت نامه دانیال ایری کلا 120 میلیارد تومن پیشنهاد داده درحالی که برای جذب زارع ، لطیفی فر و شهرآبادی مبالغ خیلی بالاتری پرداخت کرده
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137615" target="_blank">📅 10:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137614">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137614" target="_blank">📅 09:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137613">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137613" target="_blank">📅 09:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137612">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
❌
❌
ورزش سه : محمد ربیعی در فاصله شش روز مانده به شروع لیگ از هدایت تراکتور برکنار شد و جواد نکونام بعنوان سرمربی جدید این تیم انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137612" target="_blank">📅 09:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137611">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
محمد ربیعی هم  در تراکتور ابقا شد.و خبری از اوسمار نیست
🔴
قرارداد ربیعی بند تمدید داشته که در پی توافق با باشگاه تراکتور فعال شد.
🔴
تراکتور نیم نگاهی به اوسمار و طغرل ساغلام داشت و شرایط و وضعیت انها را بررسی کرده بود اما پیشنهاد ارائه شده جدی نبود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137611" target="_blank">📅 09:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137610">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
فرهیختگان: مهدی تارتار جاسوس پرسپولیس رو پیدا کرده که یکی از بازیکنان جوان تیم بوده و امروز برای دومین بار به تمام بازیکنان هشدار داد که در صورت درز اخبار اون فرد رو اخراج می‌کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137610" target="_blank">📅 09:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137609">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBG9G4JnF9P1Iy8QmEC4nLMPWtWcHYR6uG5lh1AkURlIYelPq7W10_cacCdX-qaqPJcbbkSqFa6TsVGMUQqyZ2X6Q1NOovDDNmCDE8OqMZK0UDc1cB1PfUsl8dQ4URwch5XrNcgZW6JTDblG6AzW3JRrNA8G4laY5ScMOhdJgaoDrWyckkUbc18C8anqL12p3j3Z9fRP3jeHjzxMDGRrcAn441f_Aj5-0OC19fJQiGiexQq3nvAUAp-E2k1wQ-CKSwz__lWR55rcSOb2rjMhym0veKvXfO5boNUsAa-iC_YCByJB-U1N0SXT78NhQAoDoTIVExYIB7Csswa9683h-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137609" target="_blank">📅 08:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYPn8qpYZvUabof663KmfmuoTjyEt85KjWRsmZ28QY2aYcfhA76h5pmmWKHBjLeKS_gxlwmr4FRq-Ti-0Q8CsDufx8FMEnMx5B_0TmqlrmNSo11Vyq6YyoXIkAHTODAhoBs6ckrBWwTBfgOvGlwrc8zdQiOPOhjabQNnev6aWv0f1xaXf6b03gymZeCiWrTO8_ic04ZfwVsIe1sTg4H4pP2_MvELZILS4ubUbfGZhW27zMVDEYNg6e70k_d5CouqO5wzKVyX2jakvq53XogF0asdUy9S0op4Y0ENA43yctJblwIFf6owMZMwDpXUj8JOBB9YwniXi5UH8CkmEZB_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137608" target="_blank">📅 01:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137607" target="_blank">📅 01:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137606">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137606" target="_blank">📅 01:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137605">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚪️
⚪️
⚪️
پرسپولیس برای تکمیل لیست نفرات خود در پست‌های دفاع وسط، دفاع چپ و هافبک، به دنبال جذب سه بازیکن جدید است. با توجه به محدودیت‌های سهمیه لیگ برتری، سرخپوشان برای دور زدن این چالش قانونی، استراتژی جذب بازیکنان آزاد را در دستور کار دارند؛ بازیکنانی که تا…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137605" target="_blank">📅 01:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137604">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خبرچین رختکن پیدا شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137604" target="_blank">📅 23:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137603">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZOklSOxII_GVo1AvJwF3NAioPj9RCsZynxKry7AwL1zUO3C7GSNfaW1VqPbKXzCa5f_IQ8QCUwWEjDzZbteco3M2yBaU83nuDH4olldS4mgvAOEgTZe3sOESEmBwiwQ10YzQjsHB6e2Y3aNijpoMZWXidSVhmtvHUuaQbohfdSVY_xiME77aDalVJrPn9xLw9R-Kw-RVaTsquaFMsJewq5CooNp0diPKiffFWCGGGY6TNwI_ymEwM_tpNthqhDw8_xpras2Exti11rhXcFItjnbjfJic7LmoNP3ehoQDJl2jgOrS_heTImAjlalmDuLvxSKGCy2-JmPBkf7DGEUuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باشگاه سپاهان اصفهان امروز برای چهارمین بار برای جذب حسین ابرقویی نژاد به باشگاه پرسپولیس نامه زد ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137603" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137602" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
پرسپولیس امروز برای اولین بار در دیدارهای تدارکاتی گل خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137601" target="_blank">📅 23:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
رسانه های تبریزی از نزدیک شدن پرسپولیس به عقد قرارداد به محمد قربانی نسبت به تراکتور خبر میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137600" target="_blank">📅 23:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af588d022.mp4?token=qRPsu7X-D5A_119FLBS8UBlsq8TYr1iCy5-wbMBRzlIt916D8qG89AHPYOXOEEVDhmzcHNRHNX0sioDxVwAJNpa2RP3IJI5wG6XJRhcwJ1Kc8smlP_lU2nL45zdb2F5WJluQsoMSx7oQ4Y-tQVappanwN_VesP-KGa_8I4uGZv8g96kD2tRY3Dv1O6ax1nAsqZ9pSkUJCA64Dr-S6Yitmw3SIgrIGJ6Xvp2EF1Sc_UOUbZyI4LzRZbd2fUTItJYdj3zOmsZuAWcRMMw2gle5z2Kqvl_4YmNR6CshJlwQDdYnwLqs1X66qPjKEWmzhmO73z_vSLk1zz9ItWnn3_lcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af588d022.mp4?token=qRPsu7X-D5A_119FLBS8UBlsq8TYr1iCy5-wbMBRzlIt916D8qG89AHPYOXOEEVDhmzcHNRHNX0sioDxVwAJNpa2RP3IJI5wG6XJRhcwJ1Kc8smlP_lU2nL45zdb2F5WJluQsoMSx7oQ4Y-tQVappanwN_VesP-KGa_8I4uGZv8g96kD2tRY3Dv1O6ax1nAsqZ9pSkUJCA64Dr-S6Yitmw3SIgrIGJ6Xvp2EF1Sc_UOUbZyI4LzRZbd2fUTItJYdj3zOmsZuAWcRMMw2gle5z2Kqvl_4YmNR6CshJlwQDdYnwLqs1X66qPjKEWmzhmO73z_vSLk1zz9ItWnn3_lcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شایعاتی مبنی بر مذاکرات پرسپولیس با رامین رضاییان وجود دارد اما مدیران پرسپولیس به خوبی می‌دانند اگر رقم درخواستی رضاییان را به او بدهند، ممکن است جو به نفع رضاییان نباشد. قرارداد کنعانی‌زادگان، علیپور و پیام نیازمند در لیگ بیست‌وششم به اتمام می‌رسد و قاعدتا این بازیکنان با رقمی کمتر از قرارداد رامین رضاییان حاضر به تمدید نمی‌شوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137599" target="_blank">📅 22:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
#فوری
❌
مدیران باشگاه نساجی تصمیم گرفتند حداقل تا نیم فصل دانیال ایری و کسری طاهری را نگه دارند، بدین ترتيب حضور این دو بازیکن فعلا در پرسپولیس منتفی شد.
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137598" target="_blank">📅 22:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
برای چهارمین بار متوالی ترکیب پرسپولیس لو نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/SorkhTimes/137597" target="_blank">📅 22:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
دقت کردید ترکیب لو نمیره؟!
👍
❌
پ.ن امروز بازی داشتیم هیچ ترکیبی نیومد بیرون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137596" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUEoJC02y8dZRUiIclO6Rqcx_EY9eojay-k9Ip7XQS2p5S2QcmmvftKmbGDmA-bsMAXVOvci3nv6m6ifCzI_OjgvsL9XOt0_WsJ3rXMRtkgo0eRdLi9Z558twcmtEg9MOzsSvV7VXIFhvB7IgczLQQP3KFNKq_Bs8LcsRMPUZtyDblsyy1wv4LuPz6S9K1KhXg83Yya0LYdniZsyXa09xiOuIe9wV1_4I-XRUW3j0OHwGP_EWYNGAnQiUxSx4LfX2MYh5iytaGm3s5EPTDTSYzmvzJQABU6qzErbYN41m2nsdvoqtA2m_AmbRyFzfJaQwUg97QRMJDbXD3khX_0q0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
⚽️
🤍
فوووووری از فوتبالی: درحالی که فولاد به شدت دنبال رامین رضاییانه و به توافقاتی هم رسیده، ایجنت و فرستندگان این بازیکن به شدت دارن با پرسپولیس مذاکره می‌کنن و احتمال بازگشت رامین به پرسپولیس وجود داره و تنها مشکل مدیران پرسپولیس رقم درخواستیه این بازیکنه و اگه رامین تخفیف بده به پرسپولیس برمی‌گرده
🚨
🚨
🚨
🚨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/SorkhTimes/137595" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137594">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
طبق استعلام از فیفا، از نظر قانونی مشکلی برای جذب ایری وجود نداره.قبلاً به‌خاطر گرون بودن رضایتنامه توافق نکرده بودن، ولی الان پرسپولیس امیدوارِ بتونه نساجی رو راضی کنه.
🔴
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137594" target="_blank">📅 22:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137593">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
تارتار جاسوس را پیدا کرد؟
👍
شنیده میشود تارتار تعمدا چند ترکیب را در بازی های دوستانه در اختیار چند نفر میگذارد و مشخص میشود چه کسی ترکیب را به برخی کانال ها میدهد. باید دید در شروع لیگ باز هم ترکیب پرسپولیس به کانال ها میرسد یا تارتار بعد از هشت سال مانع…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/137593" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137592">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
فرشید حقیری: محسن خلیلی رفته به یه بازیکن ایرانی سوئدی که تو لیگ 2 اتریش توپ میزنه پیشنهاد داده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137592" target="_blank">📅 21:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137591">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🗣
فارس : دانیال ایری هیچ مشکل قانونی نداره و استعلامش اومده مشکلی نداشته و مذاکرات پرسپولیس با نساجی آغاز شده
💬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137591" target="_blank">📅 21:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137590">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووری از خبرگزاری مهر
❌
❌
نساجی در انتظار دریافت مبلغ تا رضایت نامه ایری صادر کنه ؛ دانیال ایری در آستانه سرخ پوش شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137590" target="_blank">📅 21:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137589">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALDXjSNc1sdasxOOlCCKUgRnqj9mUJSV7kbVyB40oXBAaNLchsrj12drurdXgqYoRd1kT9RC3Km6XVKOPPxtb89QRcNvWDUtpVjTX76RdH9RwofY8YF0jyt3I3gktBLTLtfegm-JRYa4zq31mF6WD0-cTpGKWQVsMMRJ41BCHGLbKMCAvtQdv3xzFqq7u85TqubNVnqZNYHcllQlzxuKh4Vd_VUvy5TgfnF7xC1UrcwfmeqtpaEbWgo76WgbgIHeFw_bl0wbvXCnyYCqV-KSEQjVnbI6JIiiRleGNGR-wlJJkR0FxgltUEJzcuwjsLZb_VAtyBwe5AmUmUPyMXo_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
#رسمی
؛ کوروش اژدهاکش هافبک19 ساله آلمینیوم با قراردادی پنج‌ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137589" target="_blank">📅 21:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137588">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDZJmMYpoJYnb4p9ZjOqRbfnaN0KUw4lPHnEyYxuIMDFdEugnsCWHYCpczN98RYU9KkADfiRX2mAEeLFxdvyrrkVy8SOGbx2lTR_nzCOl0Sd6ExK32Tkw171f-3bWKUQtYQzunY1igIAQqRbQsvxTQzosFuRoe0UUrsasQF-GVyyfvligZ0RXPlp61DfbGKXvouHju3NXiPbrmBsoaXySbIHjn2PbePIVyvkIsUzclJ_Xww8h-7iWgTa6entfkxccyT2RUUzAk3RBis8qScbgnt6pMBMcSkfwRn9K3LBcB5PgqPSO_doixmEaTDYDAkgR_5MOl3rSIi4ndJ43fF9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
#
رسمی
؛
امیرحسین طاهری مدافع22 ساله نیروی زمینی با قراردادی 5 ‌ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137588" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137587">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcsxMJgoT9VnCOl4407vs6ki9oi_0PeZ4Gfv6gO3X3ufBRYq6ZiLFdLD_Gy2pft_zPpd-vx7aoxx2lWZVKi1_qRBbIO2hSdPT9q0-yKhs2vgbwChTf8AjgAqgGwOCnZGJqy8pigSaIMNRrlQManrLzDorNUzZU1Gg_dI0NLLPl247H53cI4o80flCJRq8xSCE0LY_xZE3msYtK_5ICACN9omloFurwjCmqP7yL1zyKSn3W4PZpQDw2Ow1DIAxTmXHfWcNGnVLUizbSI2tT3QB70gX-fi_-WBWe6JQV8noXtr6Cf7k_rwHzs1q8X06jP-kJ9bRk_fJsF32EMNipw0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
فقط تا پایان امشب برای بونوس ویژه Egypt Power x1000 فرصت دارید!
💰
با حداقل ۱ میلیون تومان واریز، فرصت دریافت ۱۵ فری اسپین رایگان بازی Egypt Power x1000 رو دارید.
📌
نحوه دریافت بونوس:
👇
1️⃣
واریز حساب حداقل ۱ میلیون تومان.
2️⃣
نوتیفیکیشن بونوس داخل حساب کاربری نمایش داده می‌شود.
3️⃣
از همان نوتیفیکیشن وارد بازی شوید و اسپین‌های رایگان را استفاده کنید.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
sportn5b2.com
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137587" target="_blank">📅 20:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137586">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
دستیار خارجی فعلاً منتفی شد
🔴
مهدی تارتار خواستار اضافه شدن یک مربی خارجی به کادر فنی پرسپولیس شده بود، اما مدیران باشگاه با گزینه‌های مدنظر به توافق نرسیدند.
🔴
در نتیجه، جذب دستیار خارجی در مقطع فعلی منتفی شده و تارتار فعلاً با همین کادر به کارش ادامه…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137586" target="_blank">📅 20:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137585">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
ایری خیلی به پرسپولیس نزدیک شده؛ تارتار اصرار به جذبش داره و پرسپولیس هم در حال مذاکره با نساجیه. اگه توافق مالی نهایی بشه، ایری سرخپوش می‌شه.
❌
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137585" target="_blank">📅 20:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137584">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
✅
پایان دیدار تدارکاتی:
🔴
پرسپولیس 1
🔴
آلومینیوم اراک 1
✔️
گلزنان: علی علیپور برای پرسپولیس و عباس کهریزی برای آلومینیوم اراک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137584" target="_blank">📅 19:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137583">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWkI3CnHkqfL4ZiKDzF2F8871ke6japqQLfWi0Lyu2HAURFj_UVs7znYS7WQFvkVDmqWcuScvajkgawroCWsZIm9dx995ID8i3OFjKCbvmp4eHGUteGFLt_unwYAmFeNRAzaWEnIfKJSjEmaZdK3AsWy9x_qU6yw-NWOGtwXlZLsPvwMADz95jXYxKcF_hwhugP7t6kOofTC93LZMSh7j0Ro1Jwm6YWss8oiqfkpJ5CT_xYNMylomR9fgyEkJPwl76cXPD4ZsBUzkU7ZgWIMcNdiZTqMp_u267NTUM6FE-K3Ug-GnLvmq-AYQsmeoAb89-lXPSP8zrKBUuDdDIgUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137583" target="_blank">📅 19:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137582">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🔴
شنبه بازی دوستانه داریم،پرسپولیس و آلومینیوم  قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137582" target="_blank">📅 19:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137581">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilN_Cn_bInJp1QaAhtw37JGBxetjLd7oXePdIVirPhrj-WdGuIRm-_KiWk_-3PaUaDASiLV55eOVL9-h_c8_-KG9p4n4RHg3pqmn8u5hWno_eeUA7DV6J4sZueuwhcrf4t1oWF6kZbeQJFgpMHo48SrjOWb5aB6zmfm2alQUc4hd5ENL78EXDrf6jjvy01twm5JndfhoQR8-oU-RzALXwyUECqU3nfETvCXZDx6ZfvGoOso-CPecCespj70U1vAbiceIhJIswV5KT0ijk0rLKUMLlhFonEkEaCZKQy3n2wp7erlkF7HI8-QxTBKnifWiut0fidOAdd5i8KYd03UhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از  کیسه دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137581" target="_blank">📅 16:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137580">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137580" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137579">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137579" target="_blank">📅 16:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137578">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚡️
⚡️
⚡️
محمد برزگر:
⚡️
⚡️
یکی از الگوهای خوب اوسمار، پذیرش انتقادات است. او خودش هم قبول دارد که پرسپولیس زیبا بازی نمی‌کند. این یک واقعیت است و در کوتاه‌مدت هم نمی‌توان انتظار فوتبال چشم‌نواز داشت. مهم این است که سرمربی این موضوع را می‌داند و پنهانش نمی‌کند…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137578" target="_blank">📅 15:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137577">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137577" target="_blank">📅 15:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
با اعلام رسمی سازمان لیگ، پرسپولیس و استقلال در ورزشگاه شهر قدس از حریفان میزبانی می‌کنند.
❌
می گویند بازی ها با تماشاگر برگزار می شود اما نمی دانیم چرا خوش بین نیستیم///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137576" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🏟
برگزاری دیدارهای پرسپولیس و استقلال در ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137575" target="_blank">📅 15:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2RbcDxgjl7oCaqycdVxBbMhhFWjCtYSjLW511ZPuWOxXSnDwKX2LAGBcnb7Se8DrPqc_4AuUDVr9RV3UiKkYIQM2Zlgnqo7RR7gR5lIiiaB86GVxgcexmyIRbUOhDRpymPZpYc3x_P4WC8J891ktvvyYWvjWnMA_21sXlbL4H-wePpY2-e-qSnOK1-XZf7m1tMAqQhTkwgVz4hS8kDPA27m8P-xaz6im3HPQlNtlxBQsMtI8-_1Enz69a_5wgFtBvp1qWExE_Nh1c-UEFYwSOB3PoMcBc6jUqLX-qtDYysIA8pnpW6jNwLuTfVRUN8nvjQnhUz3x3l31UuIZj48cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
برگزاری دیدارهای پرسپولیس و استقلال در ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137574" target="_blank">📅 15:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
فووووووووری / قدوسی
❌
قربانی به تیم های خواهانش اعلام کرده همان پولی که تو امارات میگیره باید بهش پرداخت شه  ( یک میلیون دلار + پول رضایت نامه! )
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137573" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇦🇷
💀
گریه‌های مسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137572" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3CpevRgAgNGXKicF511tCXAJ61mgfD1jLrbNNcRw7HJXSUfSqpN_zcEG6mMsd2casnHHnl3_jDFbyqpLIlZxkiZpfj_Hx7yDL0iA2tRABbbABNa_ZZLQjOnuqgrsGP-o4AOQpxoTBGRWu0yWUo4XIwMEUlTUM1JXYiZydNsrpUDn0PLWJokE-OVj06g2mx3DKnqCXRxZDelCExN8q68Lrh6uVmD1dai0CUv98njbPZXLwbqNG94itMFL9oD_wiCltRuCbreaIfQmZ6m0WIvNN6xmN1Dwrp1IZAOsNiynzXSSx67161ZwIJRuSmfS8a_GFSp3oRhTfsjZgJaywpv3jWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3CpevRgAgNGXKicF511tCXAJ61mgfD1jLrbNNcRw7HJXSUfSqpN_zcEG6mMsd2casnHHnl3_jDFbyqpLIlZxkiZpfj_Hx7yDL0iA2tRABbbABNa_ZZLQjOnuqgrsGP-o4AOQpxoTBGRWu0yWUo4XIwMEUlTUM1JXYiZydNsrpUDn0PLWJokE-OVj06g2mx3DKnqCXRxZDelCExN8q68Lrh6uVmD1dai0CUv98njbPZXLwbqNG94itMFL9oD_wiCltRuCbreaIfQmZ6m0WIvNN6xmN1Dwrp1IZAOsNiynzXSSx67161ZwIJRuSmfS8a_GFSp3oRhTfsjZgJaywpv3jWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137571" target="_blank">📅 14:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
رسانه های تبریزی از نزدیک شدن پرسپولیس به عقد قرارداد به محمد قربانی نسبت به تراکتور خبر میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137570" target="_blank">📅 13:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137569" target="_blank">📅 13:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
قدوسی: حضور دانیال ایری، ابوالفضل رزاق پور و کسری طاهری و حسین نژاد در پرسپولیس منتفی شد
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/SorkhTimes/137568" target="_blank">📅 13:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔄
🔄
🔄
علیرضا بیرانوند:
🔴
🔴
فوتبال بدون تماشاگر عددی نیست. آقایون تصمیم‌ساز خودی نشون بدید! فقط فوتبال می‌تونه نشاط به جامعه اضافه کنه. بازی‌ها رو با تماشاگر کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/SorkhTimes/137567" target="_blank">📅 13:10 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
