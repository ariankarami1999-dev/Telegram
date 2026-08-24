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
<img src="https://cdn4.telesco.pe/file/bwzWoeNmdeEjwCxKik2NSpr3oUcLFZ6tAhxG0mlJL0KVCPRIldBauPe2Rr-IsBg72NfzSCSRwc6HJHJjGEiBCDklW2-ImQeDk4NOSc8FyYJmhnypxrf7HiQm7QTscl8NKKTlhkboKyo0TjrJmLNYz29VXIenynyNz5E0OLJfY0A5Xv0dLdvNBnJdyqxoi149nrvf7H-qNGV2C5bRYyhKgZfIBJf8ccFwe8hIWxXV-XC_Kq6J9R1VHyo3nhla37uaEboG7qhX_Zssu1vryPBOXUoLagvqBvQxk6HuL7a2xFdkPEh6HMlvwrEs2F2wmuPtAg57UQ8NsVgL5eZFD2XfNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 14:31:48</div>
<hr>

<div class="tg-post" id="msg-143521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=ZaQziG0d37I-lWR_dtlf2zC4h4Cy2wXBiQEwFbXoKQk19bY1_NE6yerVgymdQRzvEpAMu8IJk0P6rMIYmzNZu5S96hdGj95a0wSGUqjcifyFj3gVTP3Tss-09_R_rKIMr8fNRPJivsVfiXKwlolwYIohUTHsxHFkVLl6lSv0hlmqyeMDp0D3WDBsfHz-T3X1DUKLDhKfJDwxAxQ8WzeezOccrnqk0kfs7nqSqcdWX19lP-E0d0VceUfBpWjLg3uJor9M_Bu2WskPWLgm_NE3cdfitmK_u8MxpjStp05WCu--drI920qhwxLa6d3GHmlbzJnq6rrWlbAhlkT85t5-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: وظیفۀ ما خدمت به مردم با هر گرایشی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/143521" target="_blank">📅 14:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb7af662b.mp4?token=L8d473MvzfRK5xRdDcg7QvWljOAvOe-evTN_Q2GwhCG0MaFrEG-iO6j6ATNwDGANFauTXMVVzfuJwlKQpa94P_tSyZXpl_e0aK728s-HZ-bZCzlUEf_IZD3EHFfs0m_4TSD6jomvpdDnCBSK72paGXAXZ4VLm9wLo43PiXzoukGm9fmysrR2QNcoRjxDadGETn_Ry2Q69jQGoiDvRctk8hSpzapTVAv_ouZ0SAGWjr1y_vDiJmyZRtlsMVbfwJQzLiZIApWonbLjDx9lGOWcPtQmHwIAHBnL_TBLY0h9uuHO38WsC6gKg0VLkHcQz2AYKI0LlJ6wKd67SbZq3h7YNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوباره حمله روسیه به فروشگاه ها در اودسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/alonews/143519" target="_blank">📅 14:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143518">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
👈
زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/143518" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143517">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH1VLpA40sQhfBUVmvJgrBoqOVpsUsEsXuatCd8PnR_Ah7tGnPPWQeE6V7mRR0dIFxoCyfPKKTdopugvrfwce4zGKtiuFFM2EnysYIRWQDhgKo6iKLT-4ZXQEsTg9A1j8giVxjKU__3yjHXUtgRFYY7rueqbnVOPj8D3tsp7-TOE11F30a1ZIHeFnJbb6O6Uf6Zqq2nHDkmY4t9JkFcJG6bFNxGFwliZ76QB-HehMQ90LPATpqHSVFTcEEL_efmEpCgeP3_UZlSI8wSy-U3WorXs7A8NX6ZWuwTlfYBV3lYf3H2A5uURTD4Gf3J0DtK7Iif9_19NdGHH--cv-mZD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر قطعه قبر به ۱ میلیارد تومن رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/143517" target="_blank">📅 14:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
👈
اژه‌ای: درباره اصلاح قیمت بنزین اختلاف‌نظر وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/143516" target="_blank">📅 14:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
انفجاری در نزدیکی اداره منطقه در شهر پالمیرا سوریه رخ داد و گزارش‌هایی از کشته و زخمی شدن چندین نفر منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/143515" target="_blank">📅 14:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
هیمتی: بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/143514" target="_blank">📅 13:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رئیس کمیسیون اروپایی اعلام کرد که ۶.۱ میلیارد یوروی دیگر در سیستم‌های دفاع موشکی، مهمات و تجهیزات راداری که اوکراین به طور فوری به آنها نیاز دارد، سرمایه‌گذاری خواهد شد.
🔴
به گفته کمیسیون اروپایی این تعهد علاوه بر طرح‌های تدارکاتی مصوب قبلی به ارزش مجموع ۱۶ میلیارد یورو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/143513" target="_blank">📅 13:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9XoQ5mAfhp5I2RsoLyFYFJdI-AytaNlI1qhTFT7ZlVGL6X1-oyM3joyFNlnuhf8JcyZZ3gE9Vg9R_UJFW9y6O5727ZDh-HUe8m8jhDqwjCGNho99oJlCeOqQ1UYWD8rosJ7svquLBMTtqg5mSAEt3OLzlyFHobrSmZpbcxvDwAaWE37-Mg4BBAstCdY8dt6B03ZYQdiWfPdRXI3Hsre-sdXa9-DZQrPAD6orIqvPavyQac1i7DVyOQNlKlZwxVV2ri5UW8Jsw-1lURcjGALZNjWucCTm-LYupr2XfqN740YKugQDKeSNJu-snsan70ftse3YnNBMZ5drJGKvKg4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاشینیان: ارمنستان به‌زودی روند درخواست عضویت در اتحادیه اروپا را آغاز خواهد کرد
🔴
ارمنستان قصد دارد در آینده نزدیک روند درخواست عضویت در اتحادیه اروپا را آغاز کند.
🔴
به گفته نخست‌وزیر، ایروان آماده است تا روند رسمی پیوستن به اتحادیه اروپا را آغاز کند و پس از فراهم شدن مقدمات لازم، این موضوع می‌تواند به همه‌پرسی گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/143512" target="_blank">📅 13:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u86l2HZnxDAsGDCvEBmSvjaSXVngqNPEzBr0Y-siZ2Pz0xQIO--mtcWfqZgGEjvPq5WCO88j7gmpIp7q6GMiEtN2B7cPtZd2-wHXNNVEPX8eIbc5hGN3NspnrG8DSc70oYKw8SeT1gkst7S7YFdOn2qkQlMrk_-jH4AgCDrS8_3JPl14gpUGxF2pwR_QQqI_-9Ry-w_PdP89N8zIynh9rk7S2uWtPN6XK4LW5FB7jsonmR_ZEo_bFn6OhVyRFCg9mLf4e1W8zQ2YLR4fdY-i0d1ANKvWU8IlTXW-nmGsABKne_NcUb6qp3F4IlNuyZ2HHnQuV9ti7cZMtnctMRSFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهر: ترور یک بسیجی اهل سنت در زاهدان
‌
🔴
یک بسیجی اهل سنت به نام «نادر سارانی سخی» توسط گروهی مسلح در شهر زاهدان ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143511" target="_blank">📅 13:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع پاکستانی: واشنگتن از عاصم منیر خواسته بود تا از نفوذ پاکستان برای بازگرداندن ایران به میز مذاکره استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/143510" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=APsVT_AGDOiZ1paZ_SnZS2nUio_EMW41N-DQYGNLwlW-UXhLCVHRPlVv5NxmQgI1BXYeZW62-HTJB2UxFosn_vQJIRx_NzJsp6uuvTIn2JIFpuO3v06IqDh7O-ZpzWQPIEU4CJ47Y1wa2M2uVEcdApOe_xVrgpAdJh-k_BYPIGSXTw5HBz4ga3BliWRK3KEfou4VffRSMYXl4P5xPoalYiSOCLZ92IAFnl2wNIQJg4AlUVHupgGUkfQeQZdefMQoSqBIsniU2UeCZBIrQZ0mNsXmYEu92VQkNbPaTVwctFLJxj9nNDNWjmn2vP3KiTiLwNz79Y-SDkRV0ccvzoyQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=APsVT_AGDOiZ1paZ_SnZS2nUio_EMW41N-DQYGNLwlW-UXhLCVHRPlVv5NxmQgI1BXYeZW62-HTJB2UxFosn_vQJIRx_NzJsp6uuvTIn2JIFpuO3v06IqDh7O-ZpzWQPIEU4CJ47Y1wa2M2uVEcdApOe_xVrgpAdJh-k_BYPIGSXTw5HBz4ga3BliWRK3KEfou4VffRSMYXl4P5xPoalYiSOCLZ92IAFnl2wNIQJg4AlUVHupgGUkfQeQZdefMQoSqBIsniU2UeCZBIrQZ0mNsXmYEu92VQkNbPaTVwctFLJxj9nNDNWjmn2vP3KiTiLwNz79Y-SDkRV0ccvzoyQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار در بازار آزاد 204000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/143509" target="_blank">📅 13:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
دلار هم اکنون 203,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143508" target="_blank">📅 13:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d7c61107.mp4?token=iffoE6emBTgY6rRrUijep2PNLNbjs1JCq-BZEurVJJfB69AThI0W83-2Ln537G22RvV-I0V8qHOHY3h-qZbTwVKC2X42K-nbSPmWriKEh2uBXneD3wRWyRjsv8z5M_XBz5KepfkeZIgHsbjFGPRwYBaYwp9pco3r5HoIee0aNbCFeVCi6S0dTMpCSPxm_f3moI1mTxvaa4vbfrZK2jTRxTXl4MjFtKFFoty4nRFbDhe1BUgGPZQjw_c23zHVnrQnjinXbyOz5pLqTE6KEbgHHhke4fhqTTH6xoXV17HMmGrz6caQsANCnFywngsvUlhUU1I6yNburgPTdvLShgA-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d7c61107.mp4?token=iffoE6emBTgY6rRrUijep2PNLNbjs1JCq-BZEurVJJfB69AThI0W83-2Ln537G22RvV-I0V8qHOHY3h-qZbTwVKC2X42K-nbSPmWriKEh2uBXneD3wRWyRjsv8z5M_XBz5KepfkeZIgHsbjFGPRwYBaYwp9pco3r5HoIee0aNbCFeVCi6S0dTMpCSPxm_f3moI1mTxvaa4vbfrZK2jTRxTXl4MjFtKFFoty4nRFbDhe1BUgGPZQjw_c23zHVnrQnjinXbyOz5pLqTE6KEbgHHhke4fhqTTH6xoXV17HMmGrz6caQsANCnFywngsvUlhUU1I6yNburgPTdvLShgA-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو توی کمپین انتخاباتی به‌سر میبره و شماره خودشو منتشر کرد و گفت هرکی دوست داره بهم زنگ بزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/143507" target="_blank">📅 12:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رئیس ستاد نیروی هوایی اسرائیل:
ما در تمام جبهه‌ها در حالت آماده‌باش و آمادگی بالا باقی خواهیم ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/143506" target="_blank">📅 12:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ارتش پاکستان: سفر عاصم منیر به تهران در راستای ارتقای صلح و ثبات منطقه‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/143505" target="_blank">📅 12:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awhe4GwSoQdCPwbBhI8bYQkXenppDEMIIqtWVJK0Gcp3_HWcuTe2SHmDdUrKq4EVTPYHLSlTQw-M-SpPtaEI_gZifhrzxlvbt2l5vjpi46_Zk_tWhxvRD_lO2CSpDDA9WaDpiyL_yY2E78HT-Ge9GsNgYlauH_zUY2hAuNQyx5zKK5QJmXMAfmK77QQtVu55v7Ot-iRiqxVsy1KMCL0fdIp6g72AxCdRN6160ht6kc56Yimaj85jUAXJu2BizPTco8qSwISX6nXtx6Wv84ZQOPS9rzz025cnmKZNW_a-ur_wnmsLIe-oA44Q-a1b3qdmZ7voCR-lT6Pe1i6Rpum4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش‌چشم، کارشناس صدا و سیما: ارتش آمریکا به زودی بخش‌هایی از عمان را اشغال می‌کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143504" target="_blank">📅 12:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46d5c3.mp4?token=tSTdazu74dhK51sID7eIbiV8wlUTJH7sipSi_583j7Xc_C4mqMibKXnYBB4PTD1u6-TDni2DGPkKg3j74MUt0zRkXqYVWtOoaZfthv3Az1c6wGaBWjjPyerzUxdwW9EAW57Tig25_DQZVuPxSBmhVcjWW6yv4DdvSyGH8fet3_wI5EDBWogId4SNBXTBrDP9fBG89RcR_Ocn692uVObbOjI412yLcHZ5FFHD5r9MoycX0i1anVBfWngSs5EJcAa57KbmvsL9Lu6Ogjk9UhA3hq--G7PS_bHgSigkjONYkZA9lvTrgSks9Kc4Jsmwnk07xiVkZakef6rNcbZs1oxUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46d5c3.mp4?token=tSTdazu74dhK51sID7eIbiV8wlUTJH7sipSi_583j7Xc_C4mqMibKXnYBB4PTD1u6-TDni2DGPkKg3j74MUt0zRkXqYVWtOoaZfthv3Az1c6wGaBWjjPyerzUxdwW9EAW57Tig25_DQZVuPxSBmhVcjWW6yv4DdvSyGH8fet3_wI5EDBWogId4SNBXTBrDP9fBG89RcR_Ocn692uVObbOjI412yLcHZ5FFHD5r9MoycX0i1anVBfWngSs5EJcAa57KbmvsL9Lu6Ogjk9UhA3hq--G7PS_bHgSigkjONYkZA9lvTrgSks9Kc4Jsmwnk07xiVkZakef6rNcbZs1oxUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکندر مومنی، وزیر کشور در فرودگاه از عاصم منیر، فرمانده ارتش و محسن نقوی، وزیر کشور پاکستان استقبال کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/143503" target="_blank">📅 12:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تسنیم : عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143502" target="_blank">📅 12:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تسنیم : عاصم منیر فرمانده ارتش پاکستان دقایقی پیش برای دیدار و گفتگو با مقامات کشورمان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143501" target="_blank">📅 12:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دلار هم اکنون 203,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143500" target="_blank">📅 12:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6zzBS_nhzGiqVeJ0NKeZQu7C2Zc7Zu4EM1R5_wlSS67dWDV-yUqINhutEai1lLG7JMy8h9v54t4AHcN9KLFeXVWLr3-1ODUwYlPGBM08gwBMzgUrSjRJk79HYtM6uJPweTEUeP4EZ7jak83EiIx_60J42Tqp9nA41K_0NlnJEkjgMMbYA5SKXSCCkjLYfr6me7wX2_9fylPR25kTWT_8ab6Mf9Y22tq5zHeeVkfA-4WIpkP7aw-MkT063CL3xZDFwmLklBerb8MTAv3ujsnJEYmockRUEt-Sx8E62wFQA96cwcNPUzPIC6AN4hsU-axC24VrY4yAZFrB3w3HFZRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازنشر سخنان قالیباف توسط ترامپ با عنوان «ما گرسنه هستیم و توان ایستادگی نداریم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/143499" target="_blank">📅 12:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فووووری / رویترز : فرمانده ارتش پاکستان پس از تماس تلفنی با ترامپ سفر خود به ایران را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143498" target="_blank">📅 11:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فووووری / رویترز : فرمانده ارتش پاکستان پس از تماس تلفنی با ترامپ سفر خود به ایران را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143497" target="_blank">📅 11:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83496bb820.mp4?token=b5v0L8zPNINxeu03B9tEpjJ4EvCk0X6w40qBE0Up7_FiAlsG5mbLyPP1aA4AxtrfKHJs_0wXOkQm3G8K3rgBS20ideIx8HKSo_96RZmQdksLzBSDk6eceQ5vYQL1Ue3VZZp4Wx2MsHb_KXw4qHHobM2ly99x-D0EpIsWiW_r5PpexX86J2bGRHSBbEe7MlL0hzHwQuKUilMcN0eRLyffIRDbZi_rB8ybhjVsN1LrVPxGio0BlSZW_0a2j24APFW3YfwKeFeFqtOFkU5vtWzmOGyhznaEXL_RsqfXiAo-hlQkaORONPep79GeR6MTapSGf3ydTRucHm_e9oVjeYT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83496bb820.mp4?token=b5v0L8zPNINxeu03B9tEpjJ4EvCk0X6w40qBE0Up7_FiAlsG5mbLyPP1aA4AxtrfKHJs_0wXOkQm3G8K3rgBS20ideIx8HKSo_96RZmQdksLzBSDk6eceQ5vYQL1Ue3VZZp4Wx2MsHb_KXw4qHHobM2ly99x-D0EpIsWiW_r5PpexX86J2bGRHSBbEe7MlL0hzHwQuKUilMcN0eRLyffIRDbZi_rB8ybhjVsN1LrVPxGio0BlSZW_0a2j24APFW3YfwKeFeFqtOFkU5vtWzmOGyhznaEXL_RsqfXiAo-hlQkaORONPep79GeR6MTapSGf3ydTRucHm_e9oVjeYT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سقاب اصفهانی معاون رئیس‌جمهور: هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌هایم را خرد می‌کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/143496" target="_blank">📅 11:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بقایی: ما از قدیم شطرنج باز بودیم، در سالای اخیر پوکر باز هم شدیم، الان هم مدتیه که ترکیبی بازی می‌ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/143495" target="_blank">📅 11:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ca4bf0018.mp4?token=pcDy3ZLYYdUiwxpoe8ZPC_hCqI6RYHlAWyB3eungaJvpXdLFq3VAxKr2kVvWzMBsqLkEati6YFyAU9xKgXAUw5phFj5guh8pYAftwEZ-3OAbJHLhDuXPBzWlnG_cSs4dWDYnmNgyjdFXBN5qOx_SY1UdpLrvoAve7Cr2pmankeejUcjIHpal2uo-2gibOk5q1xn6nj9wOqwAFo8dDp2MgYr11io686hj5KmlnawcrufPQ_j5yKpPnEVbb_KmPkWR69JkyqQrrRE-2UxEHQNT-lVTtMhRyZ-c5AjE7Eprj5rYqMm2DR9bNL1N4D3Og-3tYKSmVwqcLN-iq3NHoF8Dhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ca4bf0018.mp4?token=pcDy3ZLYYdUiwxpoe8ZPC_hCqI6RYHlAWyB3eungaJvpXdLFq3VAxKr2kVvWzMBsqLkEati6YFyAU9xKgXAUw5phFj5guh8pYAftwEZ-3OAbJHLhDuXPBzWlnG_cSs4dWDYnmNgyjdFXBN5qOx_SY1UdpLrvoAve7Cr2pmankeejUcjIHpal2uo-2gibOk5q1xn6nj9wOqwAFo8dDp2MgYr11io686hj5KmlnawcrufPQ_j5yKpPnEVbb_KmPkWR69JkyqQrrRE-2UxEHQNT-lVTtMhRyZ-c5AjE7Eprj5rYqMm2DR9bNL1N4D3Og-3tYKSmVwqcLN-iq3NHoF8Dhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در واکنش به خبر عبور روزانه چند میلیون بشکه نفت از تنگهٔ هرمز
:
جنگ روانی
آمریکاست و صحت نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/143494" target="_blank">📅 11:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRoxMlV9UNTMCRpPM9zqm-ZM2GiW485-8l5THJo8KFPyCDr-wGMyb8K0UzQ6BwyosCRPDVa07tnaqhb7Tsvly61FjjjyDP9XKxqf3GJiv02PtRIz9P20a2V5LWi49UpHXrssx4HNV4JXvuy1Pc2ddGPh6HudsT2sfmdxm8XyaI5BWLRfFQtfWDwiBAq6zqUXAPqptbM5hOOV6t1x810Ax4BvLUsEzot2Udk4KpUkVlpAv1a_2bmxPHPZ6Tfb1qn6aIpacvwm5mLfTw1SgpWB7hGy6VHGLZGkhXWR-9Mwftr9R9CVTFU_SmFYxC7dvzH4jFTimlR1byYKwLf06QLCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: ذخایر نفت خام آمریکا تنها برای ۴۱ روز دیگر باقی مانده است که پایین‌ترین سطح در نیم قرن اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143493" target="_blank">📅 11:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درمورد گزارش‌های مربوط به خروج هواپیماهای سوخت‌رسان آمریکایی از بلغارستان: در مورد بلغارستان ما مواضعمان را از قبل اعلام کرده بودیم. ما هم شنیدیم که چند فروند هواپیمای سوخت‌رسان «کی‌سی-۱۳۵» (KC-135) بلغارستان را ترک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143492" target="_blank">📅 11:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی از وقوع یک حادثه در فاصله ۶۳ مایل دریایی در غرب شهر ینبع، عربستان سعودی، دریافت شده است.
🔴
یک نفتکش در غرب ینبع بر اثر اصابت یک پرتابه ناشناس آسیب دید که در پی آن آتش‌سوزی رخ داد، اما هیچ‌یک از اعضای خدمه نفتکش زخمی نشدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143491" target="_blank">📅 11:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درمورد گزارش‌های مربوط به خروج هواپیماهای سوخت‌رسان آمریکایی از بلغارستان: در مورد بلغارستان ما مواضعمان را از قبل اعلام کرده بودیم. ما هم شنیدیم که چند فروند هواپیمای سوخت‌رسان «کی‌سی-۱۳۵» (KC-135) بلغارستان را ترک کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/143490" target="_blank">📅 11:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت خارجه چین درباره اعمال تحریم‌های آمریکا علیه ایران
🔴
تحریم‌ها و تاکتیک‌های فشار به حل مشکلات کمک نمی‌کنند.
🔴
پکن از آمریکا و ایران می‌خواهد با عقلانیت عمل کرده و خویشتن‌داری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143489" target="_blank">📅 11:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1beabef1e6.mp4?token=GPeVGWBJpr7mcK7x5ezwQ4ydwqIF6GN90Ce311dUv2NceOpaSpjGMJwAG8XUHlzKDQ2ZhjHWna8fGXgyb1ka7d_OMJqa1ors--lLro_nRj2HCInbs3UMxgj8vod_YgVWabb_XpkcZFK2Iz-Xxe6Tfhr9C4WGbcMZTWJgf-DBqJNf4YDJRnG4jBY_nc-NH0j_-9mnVCptv5dU6ejPj6Vqwc6CP8NCNtD2m1GdeEtmdBpO3avJp9JcV8THWYyFTdJQbqNsCR4FMagHM2TVynIs-6efk6yKbb1m48trwKuLuPjS6FPIL3J7FORsE2pDDrA_6DtVXqf99mQXUS2a5KRraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1beabef1e6.mp4?token=GPeVGWBJpr7mcK7x5ezwQ4ydwqIF6GN90Ce311dUv2NceOpaSpjGMJwAG8XUHlzKDQ2ZhjHWna8fGXgyb1ka7d_OMJqa1ors--lLro_nRj2HCInbs3UMxgj8vod_YgVWabb_XpkcZFK2Iz-Xxe6Tfhr9C4WGbcMZTWJgf-DBqJNf4YDJRnG4jBY_nc-NH0j_-9mnVCptv5dU6ejPj6Vqwc6CP8NCNtD2m1GdeEtmdBpO3avJp9JcV8THWYyFTdJQbqNsCR4FMagHM2TVynIs-6efk6yKbb1m48trwKuLuPjS6FPIL3J7FORsE2pDDrA_6DtVXqf99mQXUS2a5KRraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی پربازدید از وضعیت ترافیک تهران و موتور سوارهایش!
‏
🔴
برخی این وضع را با ترافیک بمبئی مقایسه کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143488" target="_blank">📅 10:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7737782734.mp4?token=Zw7WyaEITx4M3u6t4cXrKq9oCvw4VVPCJiX5DJFU5KPfHCuA2xc3xFBDO2SMlK8X8_XLcQ91BtYjpHyKklugBCwybfxFX-IG6vIU9rvrxb6fwlc1Bynu9PdMsEqmtSNQArdR84S9ab3GN_I_eubeK7JZ9WeMGfhD2GejCXfehuGr4RhHAKHClVr_4iMZs1uQVvQtKaj6zaGzljtfNIyj_My0UVH1jFwLkIkgobPi269zo1-gckPXDo103JYJfM5nHfN9Ge4Ux24dDQIIsZiKipIw4k5yME4g7XuBL3Sr9MSTp4s3QpOKVCeZPIQ8uIC5hymSqQ-A307K0bzTeGLRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7737782734.mp4?token=Zw7WyaEITx4M3u6t4cXrKq9oCvw4VVPCJiX5DJFU5KPfHCuA2xc3xFBDO2SMlK8X8_XLcQ91BtYjpHyKklugBCwybfxFX-IG6vIU9rvrxb6fwlc1Bynu9PdMsEqmtSNQArdR84S9ab3GN_I_eubeK7JZ9WeMGfhD2GejCXfehuGr4RhHAKHClVr_4iMZs1uQVvQtKaj6zaGzljtfNIyj_My0UVH1jFwLkIkgobPi269zo1-gckPXDo103JYJfM5nHfN9Ge4Ux24dDQIIsZiKipIw4k5yME4g7XuBL3Sr9MSTp4s3QpOKVCeZPIQ8uIC5hymSqQ-A307K0bzTeGLRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: پهپادهای دریایی ما در حال کار هستند. روسیه ناوگان داشت. حال دارد به آهن‌آلات تبدیل می‌شود.
🔴
اما ما باید بیشتر غرق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143487" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f6d9ec24.mp4?token=cbj81piovdY42Nt1U8lNp3f3VNN4qbUMJJmIqslxGbKiFEuFVAW6cf3e5aYPmj96mvaC5RwSrT1W0WC3VICaztq8buv60cPgudFOQw6wMVszUY15L8pYPC-MZrTynnfLjzidW8wdksdn_PJX0Msr_nNAMHlwOf3NyiS9pQh_m1C96N-7dKzXP8QqXp3Zmssc5Qfx9bY8MWZbZdMwbGoMuhldmKPa3yw-x6ZfjNCVreVQWG8x7FPg9k7VYmB3wufVLH5HAnEse_79_d_yxCvrH5BKEgZeKmZ2WGSPWQu_g5BuMY9vZx8ZMJaR0RIKtv6_cA-D1vdMs_WMqnVvUvLvB3lYEu1U8fOS26tfDHkzNHzw3eSSzkwy9j-j-zspdTXK_-lJmtJfNkBLF6r_9DygB859VgeORhCm7aTtstKOeZ2dZdyJK_Cg3enuR-4uH3rNR4_A3KxtaEj0zzLOCRdk0SCIrPhUDBrqHF2IcTJDNWu0ZpBoUyVzsgz7LuNSJ5DChH0ymBoUvf83JOiFm4OY0XeK_gJJ6JqOCHKjo1DbNgYbsCgnyh0LdvqSULc-CVaOj3jS4pHJnQKPGuKQhrAt-1A1xmJdMR57H68l52RvlfplrSmPg996h2cwTHYjUAdrgFg2ZmmxDRkBTVxX8dXMvsykfnv_eJk7oCpawbVw2pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f6d9ec24.mp4?token=cbj81piovdY42Nt1U8lNp3f3VNN4qbUMJJmIqslxGbKiFEuFVAW6cf3e5aYPmj96mvaC5RwSrT1W0WC3VICaztq8buv60cPgudFOQw6wMVszUY15L8pYPC-MZrTynnfLjzidW8wdksdn_PJX0Msr_nNAMHlwOf3NyiS9pQh_m1C96N-7dKzXP8QqXp3Zmssc5Qfx9bY8MWZbZdMwbGoMuhldmKPa3yw-x6ZfjNCVreVQWG8x7FPg9k7VYmB3wufVLH5HAnEse_79_d_yxCvrH5BKEgZeKmZ2WGSPWQu_g5BuMY9vZx8ZMJaR0RIKtv6_cA-D1vdMs_WMqnVvUvLvB3lYEu1U8fOS26tfDHkzNHzw3eSSzkwy9j-j-zspdTXK_-lJmtJfNkBLF6r_9DygB859VgeORhCm7aTtstKOeZ2dZdyJK_Cg3enuR-4uH3rNR4_A3KxtaEj0zzLOCRdk0SCIrPhUDBrqHF2IcTJDNWu0ZpBoUyVzsgz7LuNSJ5DChH0ymBoUvf83JOiFm4OY0XeK_gJJ6JqOCHKjo1DbNgYbsCgnyh0LdvqSULc-CVaOj3jS4pHJnQKPGuKQhrAt-1A1xmJdMR57H68l52RvlfplrSmPg996h2cwTHYjUAdrgFg2ZmmxDRkBTVxX8dXMvsykfnv_eJk7oCpawbVw2pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی درباره پوتین: چین دیگر نمی‌تواند در حالی که کسی با لباس ملوانی و کلاه نظامی، با تلفظ بد برخی کلمات، درباره حمله هسته‌ای صحبت می‌کند، ساکت بماند.
🔴
چین باید واکنش نشان دهد. باید این شور را خنک کند. چین باید با روشن کردن این موضوع که هیچ دیکتاتوری حق تهدید سیاره با کلاهک‌های هسته‌ای قدیمی خود را ندارد، نشان دهد که جاه‌طلبی دارد تا یکی از رهبران جهان باشد — نه فقط از نظر اقتصادی و فناوری، بلکه از نظر تمدنی نیز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143486" target="_blank">📅 10:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رئیس اتحادیه طلا و جواهر: برای خرید یا فروش طلا عجله نکنید چون احتمال کاهش قیمت وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143485" target="_blank">📅 10:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tg8NtKYN3ZCS8wK7aBzUKTlI1XQF38pCot0u1KcqrbdorjM1-WwdqtM-muoKP90OOi5cGl7bNZjRODSDRW1fsFpLhAtSuISCCLmKJYqLIoh7cU1ijXoeEiSfh9xW61Yu07x4fzaYs6NnAa2OklbiVWJS7r4jEw_6XwJGKmY2aE2OTNP8trWAyk3OVtsl5iUETj5tiJFIl7WKG5Ft-04Gzf6n_Ip8zu8nZPouiYC7acZBLYEktgzNQTYY7WmTrO9_lg-2nBBTbXZewa9pvWtZ4e2wUCjGWX30R97tfhIfSfhaErQfcc7uUW8cY1g-LJopX30B8cnX3fDuy9xQCrqtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی اونس طلا دوباره افزایش یافت و از ۴۶۵۰ دلار فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143484" target="_blank">📅 10:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جیمز روبینز، پژوهشگر ارشد شورای سیاست خارجی آمریکا: تلاش ترامپ برای کاهش تنش با کیم جونگ اون، به همکاری کره شمالی با ایران در پرونده هسته‌ای مرتبط است
🔴
رئیس‌جمهور آمریکا امیدوار است که مانع انتقال فناوری از کره شمالی به ایران شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143483" target="_blank">📅 10:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: کاهش سهمیه‌های بنزین قطعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143482" target="_blank">📅 10:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143481">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AciPGEmr7G8x9kNmK2HhvW9SEtev130yRchGVo8E-rmT3ZdUJvv5E7_qUBJRzluIxrNVOwvB9Sl3J015ZBuEXJjTfQZH7DJ0Ufijjf8aOFjqN3GXcDGRLpCAVqt8RKz09xYJ3fkhTiBITA0W9i1Ke-L3XiowEEAFm8lYZxjjcQbsKQZRMnvNjpgsj8AeQbx257bKC8IFX6k9jDzZInFJgRZcEpic9Gq2LH80-ZkQRAWnmBPCLZx1eIqfjTzu1XNxPHnkxxc6PIqElyqeX_4tfMT-r59ddS7tZj88WoZ3JqRl0_PT0D1YNx4Ss_xKWu6FHjfXqw2Be2wVUwrNRkAQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران «تنشِ نظامی و اقتصادی» جدید را «گسترده» و «تلاش برای بقا» می‌بیند؛ پس ممکن است دست به هر اقدامی بزند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/143481" target="_blank">📅 09:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5sj1xar6eFiRl4kiFnFFLeel8qPEn14bxlSW_FWbGTM5VevA0dzpEpiurRWTAXCZiPHykjgJXmaMPvSDbcqx_4yxc4kmpl62iF8jyqNAuu22N9iQ4F-8b1RnAlPSQIojNjKDTjnYtqH4c7KEu92pnfBnMh5cZJMLCO9TWBrPyJdlMyTE-VILJrUXL3pmYC2MmSbIuWp3MgAQBEodYTX4RCVQsCSEjK-YTRSBYOv9-04kCwmOBSL-kfO2gMn0opxC4R8LIwmrFlgKLcG_yd1NWeYqbDjBpxZvvAbMud6MWdW6_DHfCEMXHlOylL6rhfh4q3ym7Dy_OuXvCY1-vkXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه FT : وزیر خزانه‌داری ایالات متحده، اسکات بسنت، می‌گوید واشنگتن در حال ورود به «مرحله پایانی» در برابر ایران است و در حال آماده‌سازی تحریم‌های گسترده برای قطع باقی‌مانده پیوندهای مالی و تجاری تهران است.
🔴
او هشدار داد که کشورها و شرکت‌هایی که همچنان از ایران حمایت می‌کنند، ممکن است با مجازات‌های اقتصادی ایالات متحده نیز مواجه شوند، در حالی که دولت ترامپ به دنبال ایزوله‌سازی بیشتر و تضعیف اقتصاد ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143480" target="_blank">📅 09:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=HL79ekHWxp5TxJ38adoyu_UBYGQi2ioiD-UzanK7NsVnpvkohtPHdF6XjovVXjhbAh_ejP-bISGGoxNx3_BhQwTZ99GfFHJ5Ll-XEwLuoMjcXeBoakRCbFmWScOarzukyIWC4kl2xcQDIdpqybiRYlUE_WYGsA3sKAmwtHdIs_mR0_F-XdpD1li9ryypTnnVWce8IxEsvrlp_HNgcRu629PidlnMXQ_x_TVKzpt6ZZar0Ls2ApausVCk8K_VRLjR8PiBPGLSyE4bleQUjpn8_iKiwSaFJQJeyAy1EshGWUFZoy2GhVtcoUDWDqSuIZfChIzY_XSXXjNg5aY_AYn-Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=HL79ekHWxp5TxJ38adoyu_UBYGQi2ioiD-UzanK7NsVnpvkohtPHdF6XjovVXjhbAh_ejP-bISGGoxNx3_BhQwTZ99GfFHJ5Ll-XEwLuoMjcXeBoakRCbFmWScOarzukyIWC4kl2xcQDIdpqybiRYlUE_WYGsA3sKAmwtHdIs_mR0_F-XdpD1li9ryypTnnVWce8IxEsvrlp_HNgcRu629PidlnMXQ_x_TVKzpt6ZZar0Ls2ApausVCk8K_VRLjR8PiBPGLSyE4bleQUjpn8_iKiwSaFJQJeyAy1EshGWUFZoy2GhVtcoUDWDqSuIZfChIzY_XSXXjNg5aY_AYn-Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته سه مرکز لجستیکی شرکت Ozon را در مناطق مختلف روسیه مورد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143478" target="_blank">📅 09:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfCb5vrPHkPrxhem5W7Xqy13YHB2mDQlwJTiLDm6J3TrcfvOjSx5U2vJDZHQBVLeLragVUbGnO-U2a20r-Qwxa2n5DhGwCNYEaHvciUiel3Gc-_pkYF4SIc44lv0Wxf_XyQg_Wh-EwD55u0h056Fckf_flVTEF9rxDH0A1yEZtR5GokX3ZwKf5dqMiDhNoD16cfkK7CdbX52Z2epayCZjJMd5nx7PMgOTu3wwBUSrOO5vmRTs9P1mmgywXBZ8MvLc9F0dZoMmnSgGR5qx2BDI_ZEjRRkIfmN_-g2TtuVOp7gOQDG6A9IGtnK2OWZc6sOAZKgGFLs-v0QJpRuMmzqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۰۱ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143477" target="_blank">📅 09:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ونس: هدف نخست و اساسی ما از حضور در خاورمیانه، جلوگیری از دستیابی ایران به سلاح هسته‌ای است؛ فشارهای شدید علیه تهران هم در همین راستا است
🔴
تلاش می‌کنیم مانع وقوع بحران انرژی‌ای شویم که ایرانی‌ها در پی ایجاد آن هستند
🔴
یکی از قدرتمندترین ابزارهایی که در اختیار داریم، الزام ایران به پرداخت هزینه برای تلاشی‌هایی است که جهت خفه کردن تجارت نفت و گاز می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143476" target="_blank">📅 09:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عاصم منیر راهی ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/143475" target="_blank">📅 09:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
در سه ماه اخیر، ۳۰ نفر در سواحل مازندران بر اثر غرق‌شدگی جان باختند که بیشتر موارد به بی‌احتیاطی و نادیده گرفتن هشدارهای ایمنی مربوط بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143474" target="_blank">📅 08:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfbf705a.mp4?token=mgI28P2GmV0E_foshGPKMn1Hz5qD8m1EuzFKvP-Mu_oirqoal_fZro3zoxug_eYt4hbpfFG6pifo1diiWhVNEGuxb8hcft63hRvMAY8lcZsefEMGZlVNO2Wwjh_M68M7qbDsWlI8ils2us7Ll1lQKNhpWXlh-gaV_0_qwNtwqiCegRjQ9yZfxpTRjctbYQUnGA-lHSvLvV4tf6h56FtRFWyeg_Lyme0b84Qqi-VXh7ogukfo08j_7uUwiZCgdyVN3iT5X63pYvlrTgiSI1I17aovr4aMOUx4lBvqkgqft1NT-6cW_DZpisFpWMyzZnMjKkXS87xKRaFlHC2tIXauqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfbf705a.mp4?token=mgI28P2GmV0E_foshGPKMn1Hz5qD8m1EuzFKvP-Mu_oirqoal_fZro3zoxug_eYt4hbpfFG6pifo1diiWhVNEGuxb8hcft63hRvMAY8lcZsefEMGZlVNO2Wwjh_M68M7qbDsWlI8ils2us7Ll1lQKNhpWXlh-gaV_0_qwNtwqiCegRjQ9yZfxpTRjctbYQUnGA-lHSvLvV4tf6h56FtRFWyeg_Lyme0b84Qqi-VXh7ogukfo08j_7uUwiZCgdyVN3iT5X63pYvlrTgiSI1I17aovr4aMOUx4lBvqkgqft1NT-6cW_DZpisFpWMyzZnMjKkXS87xKRaFlHC2tIXauqoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمب‌افکن‌های استراتژیک آمریکا آنقدر از ارتفاع کم بر فراز واشنگتن دی‌سی پرواز کردند که آژیر خودروها به صدا درآمد.
🔴
یک فروند B-1B لنسر، یک B-2 اسپیریت و یک B-52 استراتوفورترس در آرایش پروازی به همراه F-35ها و F-22ها بر فراز نشنال مال پرواز کردند. این نمایش هوایی بخشی از جشن‌های ۲۵۰ سالگی آمریکا بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/143472" target="_blank">📅 08:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های کشتیرانی: کمتر از ۲۰ کشتی باری طی دو روز از هرمز عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143471" target="_blank">📅 08:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKgAEMOQOgn3vrtt6RePNDHKXUtHBbZPmungoKJbB0DSPy2HtT_gm7hgQhKBDDJthZyrxRhfNF-DrVek7zafNKRcofpmlPYFlv4ewRdgcqYdyhd_fKShFCd8dn65MLtHwXeWHTTzgWGS3qjdrf3aW4ytaEgtTCQ7D5h08kAS0HQ4klp9S5_MjZHgu7UWfU91gm70LqcZh-BagyZ4iUoZgkv2B4DU_6wKZHtTZD_Z7-9j1e8zJ8RrwS2hNX-GBlDNt9yADNNoGbmConvs130B3kK6Ia8YRf0Unvupab7uSyX3RsEsG3kP_HKZ9xrs6YzzTm1IeSONgaTpq5n55zHseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگراف : ایران تهدید کرده است که در صورت راه‌اندازی کمپین «دی-دی اقتصادی» توسط دونالد ترامپ برای وادار کردن تهران به پذیرش توافقی برای پایان دادن به جنگ، به کسب‌وکارهای آمریکایی حمله کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/143470" target="_blank">📅 08:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر خارجه عمان فردا (سه‌شنبه) به ایران سفر می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/143469" target="_blank">📅 08:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اطلاعات: هزینه‌ها دلاری است، حقوق مردم ریالی
🔴
روزنامه اطلاعات در گزارشی از «تناقض دلار-ریال» در اقتصاد ایران انتقاد کرده و نوشته بسیاری از کالاها و خدمات، از انرژی و خودرو تا دارو، مسکن و مواد غذایی، با معیار قیمت‌های جهانی و نرخ دلار سنجیده می‌شوند؛ در حالی که درآمد بخش بزرگی از مردم همچنان ریالی است.
🔴
این روزنامه می‌نویسد در برخی صنایع، مواد اولیه با هزینه‌های ریالی یا یارانه‌ای تأمین می‌شود اما محصول نهایی با قیمت جهانی و دلار آزاد به بازار می‌رسد.
🔴
اطلاعات پرسیده است چرا هنگام افزایش قیمت‌ها منطق «آزادسازی و نرخ جهانی» حاکم است، اما وقتی نوبت به حقوق و دستمزد می‌رسد، همان منطق کنار گذاشته می‌شود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/143468" target="_blank">📅 08:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f800119c93.mp4?token=oqR_PqIMQfu41dbi_ItuB5KKjKJTLu3OHTBZ2lkTl3a0j9rMbeHgQo6jKenIaAweOklWc-pmCcSJFu-BoFQ9IqAhtfiopnJ7aEtPB54LRlt7NlgWaaiLOLsI4SEaFjvNa67wCAV75TTMF2db3M5DfXxzFbB3btK1eAa6Ut5AeKUllwfmkJTeAGHhbDpkIhuHv_U3Z4TzQvORpOMOKDXxTcu3FxUvLR4wjxFHHjloxD45CATphfQ01C3mY-nkMuNoEG2RnZCYI5Kyfe0J8RAUjOviRjLMGo90--ZaXUwUHNtrbtsL3aOv8hNK1dfsOWn0-q3ZG6Y5yLAYWVtAf0GvvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f800119c93.mp4?token=oqR_PqIMQfu41dbi_ItuB5KKjKJTLu3OHTBZ2lkTl3a0j9rMbeHgQo6jKenIaAweOklWc-pmCcSJFu-BoFQ9IqAhtfiopnJ7aEtPB54LRlt7NlgWaaiLOLsI4SEaFjvNa67wCAV75TTMF2db3M5DfXxzFbB3btK1eAa6Ut5AeKUllwfmkJTeAGHhbDpkIhuHv_U3Z4TzQvORpOMOKDXxTcu3FxUvLR4wjxFHHjloxD45CATphfQ01C3mY-nkMuNoEG2RnZCYI5Kyfe0J8RAUjOviRjLMGo90--ZaXUwUHNtrbtsL3aOv8hNK1dfsOWn0-q3ZG6Y5yLAYWVtAf0GvvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اگر ایران سلاح هسته‌ای داشت، کل منطقه خاورمیانه به طور کامل نابود می‌شد / اسرائیل که قطعاً همون اول نابود می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/143467" target="_blank">📅 08:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر نیرو: خواستم یه خبر خوب بدم به مردم عزیزمون اونم اینه که از هفته بعد قطعی برق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/143466" target="_blank">📅 02:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143464">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
برخی گزارشات حاکی از آن است ایالات متحده امتیازاتی به چین داده و از این کشور خواسته هیچ محموله‌ای را بصورت زمینی به ایران ارسال نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/143464" target="_blank">📅 02:14 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143463">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
حالا این وسط یه سری عکسا هم پخش شده از جورجینا و اون پسره
💢
مشاهده تصاویر  فقط قیافه پسره
😐</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/143463" target="_blank">📅 02:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143462">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سه حمله هوایی نیروی هوایی اسرائیل علیه جنوب لبنان. دو حمله به مناطق شرقی شهر کفر رمان و یک حمله به منطقه القنطره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/143462" target="_blank">📅 01:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143461">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: رژیم ظالم را نابود خواهیم کرد آنها درحال فروپاشی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/143461" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143460">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: امروز در سحرگاه ما حمله مالی به ایران را آغاز خواهیم کرد که بزرگترین حمله در نوع خود است.‌‌
🔴
هدف ما این است که تمام خطوط اقتصادی را که رژیم ظالم ایران را سرپا نگه می دارد، قطع کنیم.‌‌
🔴
هر کشوری که به عنوان شریان مالی برای رژیمی در آستانه فروپاشی عمل می کند، باید انتظار داشته باشد که انزوای خود را با آن تقسیم کند
🔴
هر گونه اقدام نظامی علیه نیروهای ما یا علیه کشورهای خلیج فارس توسط رئیس جمهور ترامپ به سرعت و قاطعانه پاسخ خواهد داد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/143460" target="_blank">📅 01:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143459">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: روز حسابرسی اقتصادی ایران در راه است‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/143459" target="_blank">📅 01:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143457">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=aKA_vMk4oKw_3b3eSCg81nur0E5ERLANZrvzmoqMGUnSejAuiIenhhjb57mZgwSoLaA-eHdRCMD6H0p_c9JeqNGnRiTXGEDWh-RLZwBdQ21uQw8l76-lUB_8xGKWW0V6FLaleOqlJLAEY_pdhIVnHzMPT-1FUMrn5SIaAMTWO0AJs-WpG9mLfrnU4yng6SB8648XWwC1ic6PVBIUYKyVacHKmTwYUF-EPsxEwNlMMZ9HY1rsrlYprMsvFVZLQJi_csT20TozaYR2zyATZZ6_g2PiyY65b5o8jiFkhxej4pzwLgqRTQs1jeiUuUlxbAZG56SZUy_-htHGEJPDLEdZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=aKA_vMk4oKw_3b3eSCg81nur0E5ERLANZrvzmoqMGUnSejAuiIenhhjb57mZgwSoLaA-eHdRCMD6H0p_c9JeqNGnRiTXGEDWh-RLZwBdQ21uQw8l76-lUB_8xGKWW0V6FLaleOqlJLAEY_pdhIVnHzMPT-1FUMrn5SIaAMTWO0AJs-WpG9mLfrnU4yng6SB8648XWwC1ic6PVBIUYKyVacHKmTwYUF-EPsxEwNlMMZ9HY1rsrlYprMsvFVZLQJi_csT20TozaYR2zyATZZ6_g2PiyY65b5o8jiFkhxej4pzwLgqRTQs1jeiUuUlxbAZG56SZUy_-htHGEJPDLEdZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/جنگ رسما تمام شد
🔴
عوستاد خوش‌چشم : جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/143457" target="_blank">📅 00:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143456">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236ae62ff.mp4?token=NDpXqwKGfVH0cdZ7ph5mv6M2d4o8558boYYva5afh65ER7yFShLjNxgnQGU2S1gWnEuT6Oe_IqCKISBXDQ-wJvpz_wBtdZQxzkUfxIkn-JFyAi_XpLdihq5Rk7KscaNTk_nSAtSxXBgmlNw8MM51q0c85mrboTNwx8Bv4iemEt-D8GqJnI0mUeFFJuYFfYGBv47sJ6HuXDXSRr_bb-e13ZBkxxKxUZUBSRtneVOAAztaBxmOasIXvvo2q6MyA4Z8O3htw8z9h9JtbPqQdyWuY_Is4MIay8ovD4Q5INqDTLnN56mH3SU7GGwuBbemiO5zO7YMq9_HQu0zCXFwpF54CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236ae62ff.mp4?token=NDpXqwKGfVH0cdZ7ph5mv6M2d4o8558boYYva5afh65ER7yFShLjNxgnQGU2S1gWnEuT6Oe_IqCKISBXDQ-wJvpz_wBtdZQxzkUfxIkn-JFyAi_XpLdihq5Rk7KscaNTk_nSAtSxXBgmlNw8MM51q0c85mrboTNwx8Bv4iemEt-D8GqJnI0mUeFFJuYFfYGBv47sJ6HuXDXSRr_bb-e13ZBkxxKxUZUBSRtneVOAAztaBxmOasIXvvo2q6MyA4Z8O3htw8z9h9JtbPqQdyWuY_Is4MIay8ovD4Q5INqDTLnN56mH3SU7GGwuBbemiO5zO7YMq9_HQu0zCXFwpF54CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط مکرون دوباره سیلی خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/143456" target="_blank">📅 00:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143455">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=f-rKu4Fcv5b_z6b0DP3y0vMbSPbop83X6ESvNFeJuPYRMNR2PoD4M2bSNI8eVpae9dWsnNsvhCiXqXtfyi1ulHqjEVBansEifA4qCVsimEuY2bgILRjhqQxGFpoF79sMGhD-RJTawKS7kGgKSmfr1I50XwgM3Dt3rfFO6QHlEF_zdagxOmXUSwYbWAlVg5k7ik9vCi4f2WTGxG3D50uu6MS5AO0XxokzH13rHj-0paNaNL7kS5PD02e0v1GMFtf-TStShfRRpNJ6zl2qzXrREICvcHnwIgZwvvRIQk0Jwo_n6jqadFAtCDEHkYYGXVfn0zhvPLYd-op5QxyPJjVCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=f-rKu4Fcv5b_z6b0DP3y0vMbSPbop83X6ESvNFeJuPYRMNR2PoD4M2bSNI8eVpae9dWsnNsvhCiXqXtfyi1ulHqjEVBansEifA4qCVsimEuY2bgILRjhqQxGFpoF79sMGhD-RJTawKS7kGgKSmfr1I50XwgM3Dt3rfFO6QHlEF_zdagxOmXUSwYbWAlVg5k7ik9vCi4f2WTGxG3D50uu6MS5AO0XxokzH13rHj-0paNaNL7kS5PD02e0v1GMFtf-TStShfRRpNJ6zl2qzXrREICvcHnwIgZwvvRIQk0Jwo_n6jqadFAtCDEHkYYGXVfn0zhvPLYd-op5QxyPJjVCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی غیرقابل وصف یک پیرمرد نسل ۵۷ از دلار ۲۰۰هزار تومانی و نابودی جوانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/143455" target="_blank">📅 00:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143454">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/143454" target="_blank">📅 00:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143453">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/143453" target="_blank">📅 00:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143452">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ایران امشب رسما اعلام کرد از امشب هر نفتکشی از مسیر جنوبی تنگه ی هرمز(متعلق به عمان و آمریکا) عبور کنه جریمه میشه و یا خود کشتی توقیف میشه و یا اموال کشتی مصادره میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/143452" target="_blank">📅 00:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143451">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مایک پنس: ترامپ و اسرائیل دوباره برای «تمام کردن کار» وارد عمل می‌شوند
🔴
مایک پنس، معاون سابق رئیس‌جمهور آمریکا :  «زمانش زودتر از دیرتر فرا خواهد رسید که رئیس‌جمهور و متحد ما اسرائیل مجبور شوند وارد شوند و کار را تمام کنند.»
🔴
آمریکا باید نیروها و تجهیزات نظامی خود را در منطقه حفظ کند تا برای اقدام احتمالی آینده آماده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/143451" target="_blank">📅 23:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143450">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrhEN3nJ7SJhWdiImsRVfhn0IrxfH-iDPnmRQ4_2qPc87dhx3uZ1PBWMMWgEQFdEXLQ_74f1zz-eQw7_YMzccpWbn-hdsQaJ3ai6mgNW3HkQIRKgwrPlwHs28L3P67V2Un7_nJ2b-UMQ39Lt2cM7rusSIbDYSrk5QQrKSRnX03lphuPr_bvkpNjCbxM2uW1qj_B1V5vCOtHzi0bFE-tN9ncW50vMWTmWSsd_hJpfGU6bTfXJQsY61y70M0ccaNmMzzdWuFAKheVg0EMYXWY9d7c3mDqWj3l4d_oUVPtVYQcENvvU1j_OWDg0-TrnWiJNL1W7O6l23oRXvncw-I0bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«ولودیمیر زلنسکی» رئیس جمهور اوکراین  درخواست‌های برگزاری انتخابات در زمان جنگ را رد کرد و هشدار داد که این کار می‌تواند اوکراین را «نابود» کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/143450" target="_blank">📅 23:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143449">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f7bbad3.mp4?token=piX_Za6NMjug6bqkk3QLYvMym9BObeFjTIKyqq85510Ath3DOKrtzdciQjycOyxKYHTez1iA6PmKnPRIvNJQzvWy8qAm9ZQyuMUYTHJPOgkbuqqHiBWytPqJ9DM0F7Ldn_OQ5Rs__S-jJDoDcnSXX4DMgsyokCAOPzH7XwBPXRLbYr83U6Jf95KX-08cfVVA4cJkAzQpZmzPES9WYHJkROgepl7y_e6vXa7Kew72nQwM-ThbQg3TGaBb7OdDLNDh0ISttOyOTQyZzYMmPudkjxi8Pga24r45YUripOTsYRaD5J-8NkdF_0sPpOtLybbDtojZfrZUVJQasZAlJGEwogMDnAw1VeO7FuxJPsNrgxuIYpbrDJA3mMlKfiBmfw0g-LoxcdQbsSj2k2NlXSxs1aS5O_6IgrgSHsMcaVibZwv37W-euTkIHwT4JzZTUrUvktThmk4DlBGj40O74Syot9FjVTmBAyMnXmXGRis_48f9344HzU6lyhq7Nzk9YrMBdGOaYM8GhQdICbIrIm-jFUxYNFWgvKV_KlTG7nclKNqEGmV4v9HXqGBtznbh4LiP9jgKZ7ARS6gF6_Z4UJG8O6Lb_mdd7QgX241s1enDho5uyxaXThgvMhViseRONtG6sRblVZWDu2qygtkvMG8qtw41FNnfZL_C7MWoT9bg1vc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f7bbad3.mp4?token=piX_Za6NMjug6bqkk3QLYvMym9BObeFjTIKyqq85510Ath3DOKrtzdciQjycOyxKYHTez1iA6PmKnPRIvNJQzvWy8qAm9ZQyuMUYTHJPOgkbuqqHiBWytPqJ9DM0F7Ldn_OQ5Rs__S-jJDoDcnSXX4DMgsyokCAOPzH7XwBPXRLbYr83U6Jf95KX-08cfVVA4cJkAzQpZmzPES9WYHJkROgepl7y_e6vXa7Kew72nQwM-ThbQg3TGaBb7OdDLNDh0ISttOyOTQyZzYMmPudkjxi8Pga24r45YUripOTsYRaD5J-8NkdF_0sPpOtLybbDtojZfrZUVJQasZAlJGEwogMDnAw1VeO7FuxJPsNrgxuIYpbrDJA3mMlKfiBmfw0g-LoxcdQbsSj2k2NlXSxs1aS5O_6IgrgSHsMcaVibZwv37W-euTkIHwT4JzZTUrUvktThmk4DlBGj40O74Syot9FjVTmBAyMnXmXGRis_48f9344HzU6lyhq7Nzk9YrMBdGOaYM8GhQdICbIrIm-jFUxYNFWgvKV_KlTG7nclKNqEGmV4v9HXqGBtznbh4LiP9jgKZ7ARS6gF6_Z4UJG8O6Lb_mdd7QgX241s1enDho5uyxaXThgvMhViseRONtG6sRblVZWDu2qygtkvMG8qtw41FNnfZL_C7MWoT9bg1vc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجسمه "مادر سرزمین" در کی‌یف، پایتخت اوکراین، به مناسبت روز پرچم (۲۳ آگوست) و روز استقلال (۲۴ آگوست)، نمایش‌های نورانی شبانه برگزار می‌کند و در این نمایش‌ها، تصویری بزرگ و درخشان از نماد "تریزوب" (سه دندان) بر روی مجسمه به نمایش در می‌آید.
🔴
این اقدام، تداوم‌بخش نصب نماد فیزیکی "تریزوب" بر روی سپر این مجسمه در سال ۲۰۲۳ است، که جایگزین نشان قدیمی شوروی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/143449" target="_blank">📅 23:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143448">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcaa486ed.mp4?token=MJbV3bBsF6pjZYRd_9fzrkXjBsvHe7YBgtHWYh5LO8kNNTT3iV_VczJRS1yIYRlUGye57kXRrOosNsyYsn8dr6KX77UHQ-rZRvnRV7g0W7X6jp05PkttxV-CnNL1VTb0IEYKvLDT0Ka-87b3iO7dAY1CkYFb_94Asn8Xi9Bc_-0VP_5JfabN22QNdN7DUaeXf_fFnNlYav-CP0u4t1u2U8Nonk_E-yNof-r_qZD3_CvRi3pAbJMlrXFoWjhQdaFFrVZhU-UfFXQZFX4oRHfdJoSHAo-0gxttOb3XDyKJjkYfCB0lk90pqGvVUkiCTsPSJ851tlostBF_-1-MbxIywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcaa486ed.mp4?token=MJbV3bBsF6pjZYRd_9fzrkXjBsvHe7YBgtHWYh5LO8kNNTT3iV_VczJRS1yIYRlUGye57kXRrOosNsyYsn8dr6KX77UHQ-rZRvnRV7g0W7X6jp05PkttxV-CnNL1VTb0IEYKvLDT0Ka-87b3iO7dAY1CkYFb_94Asn8Xi9Bc_-0VP_5JfabN22QNdN7DUaeXf_fFnNlYav-CP0u4t1u2U8Nonk_E-yNof-r_qZD3_CvRi3pAbJMlrXFoWjhQdaFFrVZhU-UfFXQZFX4oRHfdJoSHAo-0gxttOb3XDyKJjkYfCB0lk90pqGvVUkiCTsPSJ851tlostBF_-1-MbxIywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات انسان‌نمای چینی رکورد پرش انسان را شکست
🔴
یک ربات انسان‌نما در مسابقات ربات‌های انسان‌نمای پکن توانست ۲.۸۸ متر به‌صورت ایستاده بپرد.
🔴
این رکورد از رکورد ۲.۴۵ متری پرش ایستاده انسان که خاویر سوتومایور در سال ۱۹۹۳ ثبت کرده بود، بیشتر است.
🔴
این ربات همچنین رکورد ۰.۹۵ متری سال گذشته در مسابقات ربات‌های انسان‌نما را بیش از سه برابر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/143448" target="_blank">📅 23:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143447">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دلار هم اکنون 200,500 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/143447" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143446">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
دویچه‌وله: هرمز، اقتصاد عراق را به لبه بحران برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/143446" target="_blank">📅 23:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143445">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حاجی‌میرزایی: دولت از وجود گرانی‌ها آگاه است و تلاش می‌کند قدرت خرید مردم را حفظ کند‌‌‌. حمایت‌های کالابرگی را برای دهک‌های پایین را افزایش خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/143445" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143444">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbac205b5.mp4?token=RjYFiguVnXnCo9RT14e0vpcEPi5Mn5j3qsp5kp4ct7ZJER61kVIbl_e9JYvfLnv4ngvNdns7HsoU-oa13V9e3-uZXrEt8Vf-WAYRsIsTZOU2Tz9u2YD3fioieDVjNa5cXx6LtqWVhNd83BsHe665gDXR9swg4H6t3wAoLWmEX_Rzj52MmqzDJeaDAE8WKzhBx_46fdurW9ugjS-KM0zD4wvgThbmDt-PVHciYdszRXGyewspzEIfF5zVbA13HCSLzU2XWXncd03tvnoH8oQGDXdRt6yMsqoPT6DT3frYvTIHj5k3bW2OXFhnjaDMDtyeME-rOXm-ZPljBtWXEEWy5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbac205b5.mp4?token=RjYFiguVnXnCo9RT14e0vpcEPi5Mn5j3qsp5kp4ct7ZJER61kVIbl_e9JYvfLnv4ngvNdns7HsoU-oa13V9e3-uZXrEt8Vf-WAYRsIsTZOU2Tz9u2YD3fioieDVjNa5cXx6LtqWVhNd83BsHe665gDXR9swg4H6t3wAoLWmEX_Rzj52MmqzDJeaDAE8WKzhBx_46fdurW9ugjS-KM0zD4wvgThbmDt-PVHciYdszRXGyewspzEIfF5zVbA13HCSLzU2XWXncd03tvnoH8oQGDXdRt6yMsqoPT6DT3frYvTIHj5k3bW2OXFhnjaDMDtyeME-rOXm-ZPljBtWXEEWy5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر موسوی؛ پزشک:
روزانه کلی دختر میان اینجا که همشون ویروس HVP (زگیل تناسـلی) دارن و بعضیاشون رو مجبور میشیم رحمشون رو تخلیه کنیم. یه خواننده معروف هست که تا حالا ۵ تا دوست دخترش اومدن پیش من و همه رو آلوده کرده.
مراقب باشید که با هرکسی نخوابید.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/143444" target="_blank">📅 23:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143443">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d1960c5f.mp4?token=gDfbQK-dyXvH4_Q9462bH7Fix803uL2rgOwqI1mHqfKP-W-aJBnpvpsa-A4i9Rp-QkcnVZKGa7kuXGIJBOuSgBvZ4Hrtq4OQONi6K_W0KFWU5JbwfEHlVhavUnsxN8sd7uxeZqOkunFYds51dTci6f3vZwOLz5eTfZEJ9Hy_lztrPQrm9XHxBPQHdoHwZNJmOC6TjH6pHy9NAw3DetPi77zR-L3Oj7f8kRkmTRxg9qEtqfLAgk9RxUmKf6bRVD7mt4ilJFMKXLOzJcc7P0PmT3Nn87jbPGJcXMPAkymRzh9D3hbe1aWdLz61Gv4Z43aQyAcaZZMbNUd68d0UuM6s6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d1960c5f.mp4?token=gDfbQK-dyXvH4_Q9462bH7Fix803uL2rgOwqI1mHqfKP-W-aJBnpvpsa-A4i9Rp-QkcnVZKGa7kuXGIJBOuSgBvZ4Hrtq4OQONi6K_W0KFWU5JbwfEHlVhavUnsxN8sd7uxeZqOkunFYds51dTci6f3vZwOLz5eTfZEJ9Hy_lztrPQrm9XHxBPQHdoHwZNJmOC6TjH6pHy9NAw3DetPi77zR-L3Oj7f8kRkmTRxg9qEtqfLAgk9RxUmKf6bRVD7mt4ilJFMKXLOzJcc7P0PmT3Nn87jbPGJcXMPAkymRzh9D3hbe1aWdLz61Gv4Z43aQyAcaZZMbNUd68d0UuM6s6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یادی کنیم از
#رضا_نوروزی
، پهلوانی که از شاهنامه آمده بود.
🔴
من برای این سرزمین، میجنگم. برای بازگشت شاهزاده رضا پهلوی، میجنگم.
🔴
من با جمهوری اسلامی و رهبران روس و چین میجنگم.
🔴
می میرم! برای آزادی تو، این فرزندانم،
کوروش بزرگ و داریوش بزرگ را به تو میسپارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143443" target="_blank">📅 23:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143442">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36986be7e4.mp4?token=stpOd5K0hnHtJkDFYLvQBKIwVtFq1RFR9iWzdA3pWmjXmZrIQFgUSEq9WACKo_tNY1gdTEppL9zqHaDvddvkp3Qtcg5744IAZVCteqYqaEsBjftGDthapHusyTsrjwrvuXLWzyuPC0on-GfsXiouC-mQj7yRKOmpe83qC2BmmVLIVluUDQ3aYC6CENHMPSdOFLtxGkfj_K-JiWZ0j7Vltl6nsS_QhdxqbI9zkiVrHtrA_nDfeqqK9fw_QE26rNqiOtckKxgqXPRnTNYY7vOEDvkrAwAgEUeQ17YruJz2KrAR98TSX-6CR7uhgENDQfaOs0qylqgSadDZySqOlrsEGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36986be7e4.mp4?token=stpOd5K0hnHtJkDFYLvQBKIwVtFq1RFR9iWzdA3pWmjXmZrIQFgUSEq9WACKo_tNY1gdTEppL9zqHaDvddvkp3Qtcg5744IAZVCteqYqaEsBjftGDthapHusyTsrjwrvuXLWzyuPC0on-GfsXiouC-mQj7yRKOmpe83qC2BmmVLIVluUDQ3aYC6CENHMPSdOFLtxGkfj_K-JiWZ0j7Vltl6nsS_QhdxqbI9zkiVrHtrA_nDfeqqK9fw_QE26rNqiOtckKxgqXPRnTNYY7vOEDvkrAwAgEUeQ17YruJz2KrAR98TSX-6CR7uhgENDQfaOs0qylqgSadDZySqOlrsEGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین در حال آزمایش «ربات‌های پلیس» برای گشت‌زنی و کنترل خیابان‌هاست.
🔴
در شنژن و هانگژو، این ربات‌ها با دوربین، رادار و هوش مصنوعی می‌توانند با لباس عملیات ویژه برای شناسایی موارد مشکوک در خیابان ها تردد کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/143442" target="_blank">📅 23:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143441">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
محمد مرندی: حملات آمریکا به ایران در روزهای آینده مجدداً آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/143441" target="_blank">📅 23:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143440">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: قرار نیست کالابرگ همه مردم افزایش یابد
🔴
برخی از مردم نیازی به کالابرگ ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/143440" target="_blank">📅 23:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143439">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362a915d77.mp4?token=DoVq5nB97XYf36aUYuyrMBsKiit59hQih6VfS-ymMF_hYeE4qhuXigGWcUQddvKBg1ULj89uD5CmkblTMUWesVCU6EiqQditqbZ215fFh1kzMqKWSJMY3BNaz8dZN_WlhQYeEosgovsEsUIP5gbAlRXCuEcNlx5fIJYebX4Ek-pSR9w7n04mIH2-AFULa0gWN5545yStM9ca1LXVRuJXHtVNmYNeyyh3-Y75mpL6HVbsLmdg2Eb_B2pwEpg7oI__5iSr_eX24H_3LMtz8CMVJ9sZfCu-cBXOrMt6C_Ae7lymWMSVkL0kqRS1Eh4M1J2gjwto79lYUzqYcNL3T_H0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362a915d77.mp4?token=DoVq5nB97XYf36aUYuyrMBsKiit59hQih6VfS-ymMF_hYeE4qhuXigGWcUQddvKBg1ULj89uD5CmkblTMUWesVCU6EiqQditqbZ215fFh1kzMqKWSJMY3BNaz8dZN_WlhQYeEosgovsEsUIP5gbAlRXCuEcNlx5fIJYebX4Ek-pSR9w7n04mIH2-AFULa0gWN5545yStM9ca1LXVRuJXHtVNmYNeyyh3-Y75mpL6HVbsLmdg2Eb_B2pwEpg7oI__5iSr_eX24H_3LMtz8CMVJ9sZfCu-cBXOrMt6C_Ae7lymWMSVkL0kqRS1Eh4M1J2gjwto79lYUzqYcNL3T_H0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر رئیس‌جمهور: قرار نیست کالابرگ همه مردم افزایش یابد
🔴
برخی از مردم نیازی به کالابرگ ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/143439" target="_blank">📅 23:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143438">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
به گزارش کاربران اختلال در اینترنت شدیدتر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/143438" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143437">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هواپیماهای جنگنده اسرائیل همچنان به نقض حریم هوایی جنوب لبنان ادامه می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/143437" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143436">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
متکی وزیر اسبق امور خارجه: ۹۰ روز اینده بسیار مهم است، ترامپ می‌خواهد ایران را مشغول تفاهم اسلام‌آباد نگه دارد تا انتخابات را ببرد و بعد به سراغ ما بیاید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/143436" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143435">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNgeIb9Q9wob0hyvUOcpegH4CGs6WqSq2iZeK9aPQXmL6WNW4iytXIXIAsCkx1C9KhejphvEeDF8HmhBhpXz6YmpzfRfEbT046p1elGwOmk5GqrW9xld92JcMWmvIPKJa4rVxQNX5LiKXVtpa8Mr7ReilXiaaKDh657FjgUX5x26NpS6GQx_qYdZ2tRtGOiOkVqLo5BpizMGHuGrSO2bNmpODbgUcKN7AUJApINoW2Bfkyyg_dBmtB6AQFVQ50EHMyZ99vatX_8VTS2HJQ38X0L8qaeHhRxTKzrTsOdFt-1Gu4zycPngqphjjqvNhphbH62gGE6tRad8ouwttayDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
رضا پهلوی: قیمت دلار امروز از مرز ۲۰۰،۰۰۰ تومان گذشت. امروز قیمت دلار ۲۸،۵۷۱ برابر زمانی است که جمهوری اسلامی به قدرت رسید.
🔴
حاصل نزدیک به پنج دهه حاکمیت فساد و ناکارآمدی در جمهوری اسلامی فقر، فساد و ‌انزوا برای ملت ایران بوده است.
🔴
تجربه این پنج دهه یک مسئله را برای همه روشن کرده است: در جمهوری اسلامی اصلاح ممکن نیست.
🔴
قطار ایران در بهمن ۵٧ از ریل تمدن و پیشرفت خارج شد و امروز جمهوری اسلامی آن را با سرعت هرچه بیشتر به ته دره هدایت می‌کند.
🔴
امروز وظیفه تک‌تک ایرانیان از جمله کارمندان دولت و بدنه اداری کشور این است که به هر شکل ممکن با اخلال در فعالیت‌های مخرب جمهوری اسلامی و‌ تضعیف آن زمینه برکنار کردن رژیم و‌ نجات ایران را فراهم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/143435" target="_blank">📅 23:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143434">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق: ما پیشنهادی را به ایران و عربستان ارائه کرده‌ایم تا یک شورای هماهنگی امنیتی واحد ایجاد شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/143434" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143433">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0_nGXj9rKzDqbyvwriIT3WbyEmXlAH1id-XdaOE4a5jR-aHnijSS13QdWa3S7jiJBiNLYdP8R7VFm-Ln65Xjm6IBakiRm2FteWaEO5RdFEry0SyO9AAyRAW8JCS4GgJOxaf6OA0LANdWAjB7Rj4KecijjpdQI08_2nKtWRiqwZLnoXd64nCcOPCVeD0l2X61HOmpM9w154EInfXYIAaf6H7ycj5eUqIrGVBaiVXe1-84Sa_wFgG432xCpTw1DBpmvLo2g6QNLPpfcplwENCsh4fzn1fb7C_ihwpqQb53rIQAfpthyd_FEJD0m65fP7DwJ3TVoKYgFPIq0P_uH7TRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری که حمله هوایی اسرائیل به تپه علی الطاهر در جنوب لبنان را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/143433" target="_blank">📅 23:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143432">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=R2h5_4ptXD9NZqwnO9xbysBWy3cQm4BQvrgFvBI-ZfGTMP-bN9iCVa8Hy8YDUKmlP0-I6husW-BBqN9ZIsgpM0AuZf6W-OUO1jlNa4_u5qC_pBYTNN0ARNWne4WRyPKLXnfKoIjVk0idjTfxbcBNlXOaCB9BGXl_cTomuX17xYorBAdf1EnOkSNc-T66BTe-_N_VSvB9i1QImMTGufuIdETFS8TvzkPe57mLg9fMRBl7k8GfpU5ukfiKiFFNYc91J54f9UI3-FObekWnHi4K4-hvFghLHdtG5-i4N97ex3dtXfADV0FC_DtcE8mJoa4vjp6Q36bV3qVizPXObyUDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d033a4797c.mp4?token=R2h5_4ptXD9NZqwnO9xbysBWy3cQm4BQvrgFvBI-ZfGTMP-bN9iCVa8Hy8YDUKmlP0-I6husW-BBqN9ZIsgpM0AuZf6W-OUO1jlNa4_u5qC_pBYTNN0ARNWne4WRyPKLXnfKoIjVk0idjTfxbcBNlXOaCB9BGXl_cTomuX17xYorBAdf1EnOkSNc-T66BTe-_N_VSvB9i1QImMTGufuIdETFS8TvzkPe57mLg9fMRBl7k8GfpU5ukfiKiFFNYc91J54f9UI3-FObekWnHi4K4-hvFghLHdtG5-i4N97ex3dtXfADV0FC_DtcE8mJoa4vjp6Q36bV3qVizPXObyUDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس دفتر پزشکیان: قرار است جانفداها به سراغ ۵ میلیون مشترک پرمصرف برق بروند و بگویند صرفه‌جویی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/143432" target="_blank">📅 23:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143431">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFHjrZslQ40n-EAMBcpywgxFU5PHc0Fx6DcK4d9Cx3TKDYQRLAPBQWWDbr4Y5K8zdLkR96ge5z6uqNRMBdOJeNkJzgopjJzc3xFZEUtsRSxVCzZABjG_mZ-IXEFVOxg29yVHP8hPsZaUxDUc9ckSxIJvgY_pSslSm1aJ0OlIhLPGs_DeburZsl7gUAYSnm6isl5kkiSY7jdNacWjYDu0hcZa8RVGPyUyOp5b3-FjUKG_RTQHCIuo2AdAOpY03t1eoc1EZlLg3Gw1Sgiu6eDtuwdLpQfaloUHws9XV48tcUdpzbH9VmSUROKHcIrldWcjNabmD1Lto2SXYTKDXtRNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به ارتفاعات دبشا، در جنوب لبنان، انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/143431" target="_blank">📅 23:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل شهرک «براشیت» در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/143430" target="_blank">📅 22:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
طبق گزارش کاربران وضعیت اینترنت خیلی خرابه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/143429" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4GULPdelHIMlPUdQkk9XC0mXYHs6wZiGAP8sW5B0v1X_GewRKBo8b1cfuFKYWLvx9t_hmKXhRSy7xrbTk9dXuEIBd-GnBFJJ3h93ahrQJ4H5Y0M5Tec7FSpXghy2zCmnSIo4iObqg7GceWt7izIAdCUPw1AEPQUCAn875PkcVXR-5-iUyd_sNgzqR-F7alG0wgPLy7e-VZX5zs8YV3XU2NzznSq3racaoK-_lrNfjvXqB8Log_2VB7QAHWm1xQd7kkuoO-MkqHRpTydDPz_RmjJOPA54kSwsiVss6UkSKKZoZJpGyOEcAdjShvZlf8fz9Ww1oJHSoXQvlEwA7N9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی: اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت نه از طریق تنگه هرمز و نه از هیچ کجای خلیج فارس صادر نخواهد شد.
🔴
ایران مشارکت یا حمایت هر کشوری در جنگ اقتصادی آمریکا علیه مردم ایران را به عنوان یک اقدام جنگی تلقی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/143428" target="_blank">📅 22:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=nV0lbRo-vnf-dBf57Bm3VHzO9EV0rWl217rFeFN_blit5ixe3GfPqFmGGKv-JoK8Ut7iyk6-dVJqXmyBgaOJ-QK32y2UdM3Ontkcdpl6p9prtI-Bdv9W5zicqSJqfJ_WrM8zmnnOFJoCxJXs75vC5Xk0y1yUMOWsEDnkYS6lp6jL_WqN0ge914Dh1HydsgeAKATFhXzGgjX9OceoKx-4hVcPImkTJK9hPk52LiIPyEmMCA8KevpvX-YqkLeJGwy1nEsNB3z-0XKJ_9AoiQF2iRvAXDGyazyMPaz0tLtsAUgNZChRJxp0G-EE816r3lWGzrkthmE0upTzA3xo_LSntw0k1sfWNIccO6f4prU8X0onOPhMqj2nRF9CiJX0l5C_DE1jYrFP40mztAplJkwWzzJOFiPGUsipQVABfP0YwKnDha7MhOP0mmNIYnSfl0Vq5rEu-cCb7u54Kfd3mUROKR5IYTHUbXpKntp7u1lVTj0EZWd0D29ZJDDJc5oq-dqIy0y-vZZAULMrGCi7PwgOYVckp8Qp_9ypnPelicKvqEUuogFtb6VEfBQaqfwx0v3QJx1rqcOdHzd4XOVx1xAvSUVdbSy22At6HjNWIRhftZjU9eh7LtR6rAywFQNmzmoUF_Uhx0E9oiAN2optbjV518ALI_TJSeqRI6LFuSoKT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c05438d58.mp4?token=nV0lbRo-vnf-dBf57Bm3VHzO9EV0rWl217rFeFN_blit5ixe3GfPqFmGGKv-JoK8Ut7iyk6-dVJqXmyBgaOJ-QK32y2UdM3Ontkcdpl6p9prtI-Bdv9W5zicqSJqfJ_WrM8zmnnOFJoCxJXs75vC5Xk0y1yUMOWsEDnkYS6lp6jL_WqN0ge914Dh1HydsgeAKATFhXzGgjX9OceoKx-4hVcPImkTJK9hPk52LiIPyEmMCA8KevpvX-YqkLeJGwy1nEsNB3z-0XKJ_9AoiQF2iRvAXDGyazyMPaz0tLtsAUgNZChRJxp0G-EE816r3lWGzrkthmE0upTzA3xo_LSntw0k1sfWNIccO6f4prU8X0onOPhMqj2nRF9CiJX0l5C_DE1jYrFP40mztAplJkwWzzJOFiPGUsipQVABfP0YwKnDha7MhOP0mmNIYnSfl0Vq5rEu-cCb7u54Kfd3mUROKR5IYTHUbXpKntp7u1lVTj0EZWd0D29ZJDDJc5oq-dqIy0y-vZZAULMrGCi7PwgOYVckp8Qp_9ypnPelicKvqEUuogFtb6VEfBQaqfwx0v3QJx1rqcOdHzd4XOVx1xAvSUVdbSy22At6HjNWIRhftZjU9eh7LtR6rAywFQNmzmoUF_Uhx0E9oiAN2optbjV518ALI_TJSeqRI6LFuSoKT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری عجیب در استان گیلان، که یک مرد در دفاع از زنش دو خانوم دیگر را میزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/143427" target="_blank">📅 22:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a7ead4df.mp4?token=bYsiJcrMmpM-yYtr7r8_oq2mTrF0OUC8PtO3eYLdw3fvJnH-tzgx7-MTT8HB5J4sQT5k3O0qnGoj0olHOd0Dd1nxb2C0Tatxx7N1o8zzt4qIyzTQYFURuBFncUNH6lBru5YSaFlLM6EDu7sGKdaS0o-1rz3rK1hoIwak5CgzksVQltK9ldlMFzTUHQPTis-R7XdyeTGceplzhdFBdea6RPLPaCb_x6NBA81_10WN8vNhRcryV9enXdlFSd3fbg-KBrzqSTI9e3QpY2FIBKjAEtcdY38T6guoEANREhIfflytP9sUMQi39zuuwR5LdHJjcV6LSRbg_FSCm04ftziURpEF8spT3mNGvl0Z_xsC4QnfpSOrmWACfAQBKq89Z7hvcx5Jzs0O5M18WQ8aviJlaCfHU5VagCyd-3AoRe3HlCShloHtNUso8-ucxrDmyjOJN19gkezpXjfcZkaNYwcOPd2m3R-ZhqB1146C9OxuYVA9c7l69e2jfqVpFfkRJMzq7Dwhmv4F9LEY0hwbeRR8dIl1SPQe1MFo32ho_88iAGrVnpFQpR4SHBFvC1xByc_-hPy3Dcu0Jlqswva4ulyvL4qVYC3GVXAFBrcly92uuwDTDUnrcBNN6k7nEmcAA5jGts0S5fFa0AP8634a5_0ZswcInWZEwaerewBTuhbjlmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a7ead4df.mp4?token=bYsiJcrMmpM-yYtr7r8_oq2mTrF0OUC8PtO3eYLdw3fvJnH-tzgx7-MTT8HB5J4sQT5k3O0qnGoj0olHOd0Dd1nxb2C0Tatxx7N1o8zzt4qIyzTQYFURuBFncUNH6lBru5YSaFlLM6EDu7sGKdaS0o-1rz3rK1hoIwak5CgzksVQltK9ldlMFzTUHQPTis-R7XdyeTGceplzhdFBdea6RPLPaCb_x6NBA81_10WN8vNhRcryV9enXdlFSd3fbg-KBrzqSTI9e3QpY2FIBKjAEtcdY38T6guoEANREhIfflytP9sUMQi39zuuwR5LdHJjcV6LSRbg_FSCm04ftziURpEF8spT3mNGvl0Z_xsC4QnfpSOrmWACfAQBKq89Z7hvcx5Jzs0O5M18WQ8aviJlaCfHU5VagCyd-3AoRe3HlCShloHtNUso8-ucxrDmyjOJN19gkezpXjfcZkaNYwcOPd2m3R-ZhqB1146C9OxuYVA9c7l69e2jfqVpFfkRJMzq7Dwhmv4F9LEY0hwbeRR8dIl1SPQe1MFo32ho_88iAGrVnpFQpR4SHBFvC1xByc_-hPy3Dcu0Jlqswva4ulyvL4qVYC3GVXAFBrcly92uuwDTDUnrcBNN6k7nEmcAA5jGts0S5fFa0AP8634a5_0ZswcInWZEwaerewBTuhbjlmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آجورلو: تنگه هرمز بسته است؛ عبور نفت به ۲ تا ۳ میلیون بشکه رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/143426" target="_blank">📅 22:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTNMj4_TzkC-BWlYdoFItDzTHRDHjdlX3PZipA2Qx2CWpU5XG5EC_MGUDEZ5Uds4C4387chr4pkkAG-ZIURzwL5leQ9v2AiKluHVUIlrvkO57jy9F5xC1AMzIPhK9yE0H-kPUuvUtxNH-xLQwyw57uG1zw-mYpO24hPuHQnB_JEwv3L8gcOxTYAHe2a0uhi5U4zEo61Pe__UZzn_NLXYf6dr11RXS71Pi7YAyoI6pDiupVTjWKqxdVZUI4hcaFu7PntZ-K-Lcwu34ajYaNn1dnZ33jwGyvdyLtHOaOG2wwMTnRrH0F2k1xtmsbhvsnfMzh2GDRuK9Z2VIsaT-2DrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد زیادی هواپیمای سوخت‌رسان نیروی هوایی آمریکا امشب در اطراف تنگه هرمز فعال هستند و یک فروند هواپیمای گشت دریایی P-8A Poseidon نیروی دریایی آمریکا نیز بر فراز دریای عمان در حال پرواز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/143423" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvvUKRDRmanFLOXbP7YUG3nbUk5JEj6vxV2oteSLlCuVkTeXI4o3wCwpRSKRCCIwvLSo5jWB5s0iHxbSwOnm3Mw6zEmS7Id_d696c7HM6I8IKAXRJiGG6fT-83RlSaMIuq5T7rJ7T_HbHFmYB1PZSKGYfxmCHcXphEh72hW0pirow-SvUsszDU4q-78n2lCXEhpf8bfYm5-9gIjA56b6E9dHIJnObAwOPY-OfE-soZwET5EnOS9v4fGgk35a9uEwL12yJPxXR-Z-dgmEHZ9m7uMAOyg_oa-0O4yQ3-ue3Mu6JVY4CbnF8_S2uNbA6Q65k8BFE6qAXCZI30UvBw-wWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید محمد مرندی
:
«احتمال اینکه تو روزهای آینده دوباره درگیری نظامی شروع بشه، خیلی زیاده. هر کشوری که با ترامپ برای تحت فشار گذاشتن و گرسنه نگه داشتن مردم ایران همکاری کنه، شدیداً تنبیه می‌شه. اقتصاد دنیا هم در آستانه فروپاشیه.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/143422" target="_blank">📅 22:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اداره تنگه هرمز: ‌ کشتی‌هایی که از مقررات ترانزیت ایران از طریق تنگه هرمز تخطی کنند، با محدودیت‌هایی در سفرهای آینده خود مواجه خواهند شد. صاحبان محموله‌هایی که به خلیج فارس و از آن سفر می‌کنند باید فهرست به‌روز شده کشتی‌ها را بررسی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/143421" target="_blank">📅 22:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
از زمان سقوط بشار اسد تو سوریه تا به امروز ارزش پول سوریه در مقابل ریال ایران ۵۳۰ درصد افزایش پیدا کرده، یعنی بیش از ۵ برابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/143420" target="_blank">📅 22:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb908fde6a.mp4?token=iXOcXp7dFtIQ4N1MUhgfmC7-q3TM8ZGccgZ90vxmUeRZHkllC_1nmqMy47he-Vg7c8YuMHxn6y399IGiI4O15lv0bDlnfvzB-1QHlvod1ABHRQi1lfauwKFHe1JZy36NqRMjbafRYCdy6paFHh3rcsTLT9GmQ5Ip_WgKZBhSm0Lb0kRkmBWGfNVQ0nyJ4czDyzm7S30d6BsINuimDCbhI1gXgwjJ_xmYiQ4bSfTMYByQi0ooRiwY0rhqxW9n_-FYOCN4UxGKfGp6Am5MNZk3GUWzhvnwKZ8QOv_hKsxmVujsnH7_fG-IVMUPhJQMnMvTlycySyjtMEpxaAeH6Zsqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb908fde6a.mp4?token=iXOcXp7dFtIQ4N1MUhgfmC7-q3TM8ZGccgZ90vxmUeRZHkllC_1nmqMy47he-Vg7c8YuMHxn6y399IGiI4O15lv0bDlnfvzB-1QHlvod1ABHRQi1lfauwKFHe1JZy36NqRMjbafRYCdy6paFHh3rcsTLT9GmQ5Ip_WgKZBhSm0Lb0kRkmBWGfNVQ0nyJ4czDyzm7S30d6BsINuimDCbhI1gXgwjJ_xmYiQ4bSfTMYByQi0ooRiwY0rhqxW9n_-FYOCN4UxGKfGp6Am5MNZk3GUWzhvnwKZ8QOv_hKsxmVujsnH7_fG-IVMUPhJQMnMvTlycySyjtMEpxaAeH6Zsqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات های انسان نمای چینی توانستند امروز در مسابقه دو، رکورد یوسین بولت، سریع ترین انسان دنیا رو بشکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/143419" target="_blank">📅 22:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143418">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا به فاکس‌نیوز: به زودی وارد مرحله جدیدی از جنگ با ایران می‌شویم و به تلاش برای پایان دادن به آن ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/143418" target="_blank">📅 21:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال ۱۵ عبری: دیدار وزیر امور خارجه سوریه و رئیس موساد مثبت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/143417" target="_blank">📅 21:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd6uy6JgXvowmlDa8tJTRbm3V5uvcBCYXIZh7zsxR5Se0PX9291inodBbQKY68x_pz2f0NLAixlfuIORJbToRrn_taeb2iH0Yj4m8CoqlbVU4Mb-BJA8_cNr2-2C0ZQy38WwL4UVNOmwR-AopWqKlGNOLqaUDm3oaPysrwOcMYjINm9qKHQTjRS73vQqwzvcHajX42PL-Xy_WKjDQNkkZ1JQo1lV773bFRy3zbBkRh6Jx9VnftJj4Q1VpUAE4V8ev5OqRDf_FZQ7t_u-lTg5UPWdmwdAzLfMs0Q0ZIqbFSKl2NNS1bBYsyazXOCRwr5NnR-mhOyp9CDPDRCi-SX3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس ابوعلی سینا روی اسکناس ۲۰۰ سامانی زده می‌شود!
🔴
با دستور امامعلی رحمان، رئیس جمهور تاجیکستان برای پاسداشت ابوعلی سینا دانشمند بزرگ ایرانی،علاوه بر اسکناس ۲۰ سامانی از این به بعد عکس ابوعلی سینا روی اسکناس ۲۰۰ سامانی هم زده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/143416" target="_blank">📅 21:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-143415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e471f88ae8.mp4?token=OqQDQNa66xs3lKd4KXFOE9dExPC_15aEMUsi0CYbzW9SrWu6WDGvH5hVHDio1wsqWeo4z5wFBA4LjGJFbTt0E5Gdk300Wj7wYFFYQjTBqpjTK4OAwMMPjgu-_eZS2zeRAYKA4f4fVp9HWjz9y9t3zhsoJmQ3UqG2g_vd0TvtBiamAOJPm0mYFca0o9pbN35FxTnn_rgqRkXvZAgwjah7teIwfMmPkp89oeQNpLHCIHVtHxuOAaEY25UaCco8rvDre3pI_k98NpnaV0x_XxCCrz0EMRPfCXm4XAvWpEqabT4_Z8jm2MEtKqKDRw-NtMhYTVx7VXfHOqsGhtk8LHXLIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e471f88ae8.mp4?token=OqQDQNa66xs3lKd4KXFOE9dExPC_15aEMUsi0CYbzW9SrWu6WDGvH5hVHDio1wsqWeo4z5wFBA4LjGJFbTt0E5Gdk300Wj7wYFFYQjTBqpjTK4OAwMMPjgu-_eZS2zeRAYKA4f4fVp9HWjz9y9t3zhsoJmQ3UqG2g_vd0TvtBiamAOJPm0mYFca0o9pbN35FxTnn_rgqRkXvZAgwjah7teIwfMmPkp89oeQNpLHCIHVtHxuOAaEY25UaCco8rvDre3pI_k98NpnaV0x_XxCCrz0EMRPfCXm4XAvWpEqabT4_Z8jm2MEtKqKDRw-NtMhYTVx7VXfHOqsGhtk8LHXLIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی: صبح تا شب درحال تامین ارز هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/143415" target="_blank">📅 21:42 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
