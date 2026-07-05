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
<img src="https://cdn4.telesco.pe/file/ImPoUW4ZnVcsvQH267dLrX65Qf-kW8VYx0FaFG0r47jYt5tXdYWj3qnEdyjYuD9dvLkK2fFZucj6JKVf6eGzi_MLnyz_ueZ_r-MoHvfgxnV0I-iWdhgZRYMRoBYYyY3OhkQQmtjkAKCnfs2uMvFgw2mEeiSydpSZFrnlziYAVkZHu3rvZU4dxFnRnMK4PAg6KinXRysshe5BsMZvxxzoBLhRjKYpyDVH6JINtdlz4nTsNSeIG1QKlUhaKD41H2XcYXfmLvHvFug1lbvJu8yNwaGWIZrO6F7XI4aCTboex7A3bWmh_t4ZknhmYjgvxc8GKpHLoIbOhaFSgX7aEHfQPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 01:23:25</div>
<hr>

<div class="tg-post" id="msg-135080">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
نروژ دقیقه ۸۰ گل زد به برزیل و یک بر صفر. جلو افتاده ...ده دقیقه تا حذف برزیل از جام جهانی
🤩
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 153 · <a href="https://t.me/SorkhTimes/135080" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
تارتار : ما تو دنیا هم نشون دادیم با کادر ایرانی میتونیم مقابل بلژیک و مصر بایستیم و به اینا نباختیم، شاید یه مقدار مقابل مصر شجاع تر بودیم صعود کرده بودیم، کادر ایرانی نشون داد چیزی از مربی خارجی کم نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 489 · <a href="https://t.me/SorkhTimes/135079" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
مهدی تارتار: من می‌خوام یه پرسپولیس جنگجو بسازم و اسم ها برام مهم نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/135078" target="_blank">📅 00:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
علی نعمتی گفته 48 ساعت وقت میخوام اگه با باشگاه خارجی نبستم، میام پرسپولیس ///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/135077" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
مهدی تیکدری: وقتی رفتم با استقلال قرارداد بستم هم پرسپولیسی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/135076" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
تارتار : تو نفت مسجدسلیمان، پارس جنوبی جم، ملوان بندرانزلی، گل گهر سیرجان بهترین نتایج تاریخشون رو رقم زدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/135075" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
تارتار: از انتقادای منتقدین که خواهر برادرای من هستن حتما استفاده میکنم. من ۱۹ سال تجربه دارم فکر میکنم شرایط اینکه به تیم محبوبم کمک کنم رو دارم. از پیشکسوتا هم رخصت میگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/135074" target="_blank">📅 23:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135073">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f1df6e4b.mp4?token=adDNrBz8dc4Job2bRHS4zaftdlXLiLjCasMs06_hzigxIYm3CvvNWbCMm0YxyU1y_GzEbgpu4bsGFiyc2QqAWXpxKmvuzrHwtaq0dcQdUS7bQcZ-GOqAG0uiuPJbKJjun-gPvinwzSm0IitkIfq6r4mMFT6GSzJRD-UcCAsO8pegyihlvgaly8mnesZf42t_BAnTSOaAAw-JoJQDfyzWnqk8VGmvRz7XIl4-MKAQ7H0SN8cmKQ8pc0k9FZRD8WbSWaZTDLkYEtZmrID_KQxlcnzFReuWrj3F52a0C-zOeq-lAgfJptv2l-0LUvK6Ccws9DbQ_VIRyGtxT1tyDFUcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f1df6e4b.mp4?token=adDNrBz8dc4Job2bRHS4zaftdlXLiLjCasMs06_hzigxIYm3CvvNWbCMm0YxyU1y_GzEbgpu4bsGFiyc2QqAWXpxKmvuzrHwtaq0dcQdUS7bQcZ-GOqAG0uiuPJbKJjun-gPvinwzSm0IitkIfq6r4mMFT6GSzJRD-UcCAsO8pegyihlvgaly8mnesZf42t_BAnTSOaAAw-JoJQDfyzWnqk8VGmvRz7XIl4-MKAQ7H0SN8cmKQ8pc0k9FZRD8WbSWaZTDLkYEtZmrID_KQxlcnzFReuWrj3F52a0C-zOeq-lAgfJptv2l-0LUvK6Ccws9DbQ_VIRyGtxT1tyDFUcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش مهدی تارتار به حضور کوتاه مدت وحید هاشمیان در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/135073" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135072">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e534deb415.mp4?token=RWYTfLfqHbEKLvqbIN33LZnNtU67bV-B8kv6YW2O0uPBjfrxwtzpuJAVhQL_-ucZ1q2fLln-p10VY7dD35RCqiRWN2gVhE2qWjBoyg_kKU7UXKu-3Gnqyhb4Rt_3lUKpMUM5rXCmRd1YHUscYWD0lHMWZy4M4ciaFbFukdXNRNMmhn2e4HmEtUJMknT-5nz-Fd7VVYCMy4smMPVG4XcUkPpC1WtdhmMV6DnTOiuaoQYLy2Sr0v6NfXvXZsXBOtbM67drL8ucY_dhZPQI3pw2_tuMW0s3nRFR0XNn4zB7mbsp7fK1167PAscNTi8m0MgQK47wMI814eSAFD5ZWLpEtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e534deb415.mp4?token=RWYTfLfqHbEKLvqbIN33LZnNtU67bV-B8kv6YW2O0uPBjfrxwtzpuJAVhQL_-ucZ1q2fLln-p10VY7dD35RCqiRWN2gVhE2qWjBoyg_kKU7UXKu-3Gnqyhb4Rt_3lUKpMUM5rXCmRd1YHUscYWD0lHMWZy4M4ciaFbFukdXNRNMmhn2e4HmEtUJMknT-5nz-Fd7VVYCMy4smMPVG4XcUkPpC1WtdhmMV6DnTOiuaoQYLy2Sr0v6NfXvXZsXBOtbM67drL8ucY_dhZPQI3pw2_tuMW0s3nRFR0XNn4zB7mbsp7fK1167PAscNTi8m0MgQK47wMI814eSAFD5ZWLpEtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مهدی تارتار: می دانستم حضور من در پرسپولیس دیر و زود دارد اما سوخت و سوز ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/135072" target="_blank">📅 23:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135071">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
تارتار: ما برای اینکه یه تیم جنگجو و دونده داشته باشیم نیاز به تغییرات داریم.. یه بازیکن اول باید جنگجو باشه بعد فوتبالیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/135071" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135070">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
تارتار: خیلی خوشحالم شرایط طوریه که مربیای داخلی هم میتونن به تیمای بزرگ برن. از هوادارای پرسپولیس میخوام بهم اعتماد کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/135070" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135069">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
اولین واکنش تارتار به سرمربیگری پرسپولیس: 18 سال تجربه دارم و می‌توانم به پرسپولیس کمک کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/135069" target="_blank">📅 23:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135068">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🔴
رسمی؛ مهدی تیکدری، مدافع راست ۲۹ ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/135068" target="_blank">📅 23:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135067">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: فکر می کنم بتوانم به عنوان یک سرباز به پرسپولیس کمک کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/135067" target="_blank">📅 23:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135066">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: فکر می کنم بتوانم به عنوان یک سرباز به پرسپولیس کمک کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/135066" target="_blank">📅 23:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135065">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HjC0I-db5-28YoFaYWM_2U_xIPWnv1uXagVyfHKy-qe9bQWCtLIO9lKR3RCJS9lZusK0-EM4t281VqgHvE6ZtT5sb671LoyWmHOiQRdDNBlRH8YmQNqXcK24qYv_V3PgxMmo2Bqpw_RILvqNuRvaIWVU4eJmtYtq26fA1WRndoayb4lmBFb5ESaWML5LGohLMa6Wq1oRC-xrD6lWe4_BZW6cmJ26eRfA5OvJvMDhMegRIsY1LEInx4adYy3k-fl68iZ1qgmT8gbPTbcxzzgJ5iDvQ8_JGqKcSAjyE57idUC6qULkQVFLt6fgxSy1a-dWqEoWYgdzkM8l_E4tRYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه گل‌گهر از سیدمهدی رحمتی و جانشین تارتار رونمایی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/135065" target="_blank">📅 23:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135064">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4dD-A9WJunNJuyLZYc2KZLjFQDTFh_VWfrOE-zHYfOsLHpzCU7FTScOfnIeS8AfGTaDt138WDPqrDcSFrwQigWjNRwDmezNuQotY2Oz5kRMNJ99VdiD4-AeY88a_9NlwEF19OW0rQpMdH1psKYbfQFWT6_Jr5QIEjTpXegkG_aAGPecsqCIbFIM8gdu63lzHsPvLcn7RjGXbfgRHA97Go7xWLLF7gQVCOhY2YyuJayqwtbWALOJYXeMPVj1iTSIZGzAsce8fugCyVtq04cFCMajx-5bpUbMBgIkt-8LHwQsnnX6ymBaxeimcrgYBGUkM5BMWFbb1EBq4iERN09riA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
اینانلو عضو هئیت مدیره پرسپولیس در گفتگو با فوتبالی : از اول هم سرمربی داخلی می‌خواستیم
📚
به دلیل شرایط باشگاه از جمله آسیایی نبودن تیم به این جمع بندی رسیدیم که سرمربی داخلی انتخاب شود. چند گزینه داخلی داشتیم و مهدی مهدوی‌کیا جزء گزینه‌های ما نبوده است</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/135064" target="_blank">📅 22:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135063">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
رامین رضاییان بعد از وینیسیوس جونیور بیشترین جایزه‌ (بهترین بازیکن زمین) در این جام‌ جهانی را گرفته است. همچنین رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/135063" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135062">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
پروژه جوان گرایی تارتار تو پرسپولیس
✅
پوریا پورعلی 30 ساله
❗️
جایگزین میلاد سرلک 31 ساله میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/135062" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135061">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
پروژه معمولی سازی پرسپولیس آغاز شد
❗️
پویا پورعلی هافبک دفاعی گل گهر سیرجان به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135061" target="_blank">📅 21:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135060">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f006bce86a.mp4?token=XeqoBiicRJcpLj-a2Buy5H6zyIksoSYg8vmCKBRPd_85TqylnKGZNiDeUt4B3eVKH67rwmQJzUOwXiLjFRZ2cH24TcdLbIBi6NZQ3sGCpqzY_24s6KKPzwytRhW6RUPQnnol1ql6fdnSuyJvFtUGoQaWuMa2m9Et2THrgZxpoRfhKke6vUvQqavwXvQzU9YzN085wJQjmpPT1ggMYh2xcvmm8r7JbCvPCuPGZFown5FO-K7EP0yKz43vV_I7zcHkKCgr62B-btsUDZ-Jm--uD-WpaqOd5HvgpoG1_Hhk9PQW1dpS-md1MW7-2NkaWzVWQMnZ6mivaa9eNM6ThWBYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f006bce86a.mp4?token=XeqoBiicRJcpLj-a2Buy5H6zyIksoSYg8vmCKBRPd_85TqylnKGZNiDeUt4B3eVKH67rwmQJzUOwXiLjFRZ2cH24TcdLbIBi6NZQ3sGCpqzY_24s6KKPzwytRhW6RUPQnnol1ql6fdnSuyJvFtUGoQaWuMa2m9Et2THrgZxpoRfhKke6vUvQqavwXvQzU9YzN085wJQjmpPT1ggMYh2xcvmm8r7JbCvPCuPGZFown5FO-K7EP0yKz43vV_I7zcHkKCgr62B-btsUDZ-Jm--uD-WpaqOd5HvgpoG1_Hhk9PQW1dpS-md1MW7-2NkaWzVWQMnZ6mivaa9eNM6ThWBYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه معمولی سازی پرسپولیس آغاز شد
❗️
پویا پورعلی هافبک دفاعی گل گهر سیرجان به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/135060" target="_blank">📅 21:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135059">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
میلاد محمدی تا این لحظه به پیشنهاد تمدید قرارداد باشگاه پرسپولیس جوابی نداده است و اولویت او لژیونر شدن است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/135059" target="_blank">📅 21:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135058">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🟥
علی نعمتی در آستانه بازگشت به پرسپولیس////خرمی   پ.ن فقط این و کم داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135058" target="_blank">📅 21:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135057">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTSVEpKPQWQoZw6Sbd_wU9amWkNq-zA5f8qK5KMe2u9RGzIvcEqTCvky9Tu46bqfu2kGKZsSVF4NvNTbnhlqrvnJuXlb5fjHzCSW6xpkrJ68z_53MYNMJqTixzMuZ93C2shFuppw_hX0_MXCVen9m2k7G28lJ1SsoFvDtR5W-FD163r-tr8SMNzeYge6RrGLyss8drdmVF60lwc3q_LuC4NcrRguPLSXPy6zfm2nHaHwOe7W7xLK0ky4oiVpvqFyIMY8sH77yzi6uvSn8ms4N-DylEV4YwXLwMeQ5WDJpbEh03QWq_aBsz9dMCMDTeFIm8lRigm6AKgYcYG9RU7yEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
علی نعمتی در آستانه بازگشت به پرسپولیس
////خرمی
پ.ن فقط این و کم داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/135057" target="_blank">📅 21:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135056">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpghB9YdI5vtB6ycAJk5DJQifhTtiI0XjsBUYG2Brx0Cx1eiiC8ovTzsi1XOKR2du3aX_6DQPGA8ApSsAH0ZP2PflKQEPfHPn_P-d5AwZ2HkyqRLNeRbSvGAu_bYwvqY1fdMT-sAA2xWQBbIZfjKPJaBiUe0YnSw8Wvzy37KWNnSVXdONtQAOtUE8GHao6rdmBtPBo7mGXzsJBM2xdCHOafx1GEOJzx18MFxR-0X60bPmwr_X84Mv3g8ZLie4MZbosUvgKvSe60eEwKBfwRhJ1gCsbvmojJZMU8_umqG9wOwP90fUddfAnsisEwiSX__C4CBEZY33YREjibG2MujuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/135056" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135055">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
پورعلی‌گنجی، عالیشاه، بیفوما و گرا تا حد زیادی جدایی‌شان از جمع سرخوشان قطعی است.
🔴
کاظمیان، شکاری و سرلک نیز مهدی تارتار بعد از بررسی وضعیت آنها تصمیم گیری خواهد کرد. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135055" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135053" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/135052" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYa0Q8bpjhI1p7TNV3v0cMuSbLCQ7njIQGTEqLP07TN0UEFfr6tDzNY3e697FA2hbJJb02Z1adRSdl-PZlKAhoMk9hweLv-b1TCK0TGXFtfrqta4tz6gcIN5yYMx71wtQTLgiuw8jtDwcuyqsvYvRXyfrknJt3NieVyc04gdplG-m9Bj1BOZlONK30q-PSeQV6Rx-iHyuP7tmfmi9qGqzrzIyiIC1jaMxytGj3iImffM5xMX2boTlx9b62wxnVpA4d9rwqPGnzrAw9BZqoZMT5CNmN2I7A0_t5xmhksxWvWlcrEbp3OYjGWaedhJPPrn4qKA-vISJnfub1Bl-KDioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135051" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/135049" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZGaTrNZULVYn6794rihIHeALl03Op-4-rzHrdoyKB5ryo4ajmOdj1PnXc7K--o2cgSDqLjt2pXljiRnLYmDa4zV_xzfHW3dZa_8eqTebWWjwqnYoF8tCXgBZeOsp4EkG_lhkrHdLUAiUkdHrjOxGwQ9uexSyl5PhgkZvSzD84SY_e-36sekPi-MN8w5cPydRmGbPBnSZi10Nt-LA_-SowEdBBGZendCmMtpD9chTr-gszJrrTMQ2W-VbMwbjcAyULqeJKBqM_5uqgYXSTMVpm1VmgQv6KGwwNvdtyZDSH2V2HFCaj_Yuiyriju5i1_W5zsB2yeO2ZRT9ri2JmANLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135048" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/135047" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5elwLOWOSwrv7jrxwgHxyOkrFYo8EX2JE2m2bxO2n_XoDRvLsv1z0AkrVinz2G4uFynzvXltYASmkfuHiVeqIhm8MMg2dlnz39LGJSS9bWF67MehSf-KW3IxORh3UiEQr4PcS_9uLUknpIExhyyPEJJUg67YIzvDVxGdns1y9nePXJqF6I8oopyQnzM_PKn5CIcRrh8CkgugxqLRoKVnep7lPB7IMnKk9KkGQTkSRJ9enO4TeM4WN3RJUwcPzAbkbm_qLNYUQl263_yuYHYDjWDcnQRfySv4I8LSkYL5VrlDYO62lDbqBak9SlQySgViE9YQHWuADPZ-p6TeOoXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/135046" target="_blank">📅 20:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/135045" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/135044" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135043" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/135042" target="_blank">📅 20:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/135041" target="_blank">📅 20:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135040" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d10HFZUzFBTNvv5mymNgI9RK1yeFGuJnaCMrbgPlwp8jg6g30VmGl_g7V5O63p0ciLomBcvTtEkz261G71GbAr2bwcpqJtFIWnY0sNF-h-w2ORAMelk5-Y0hDHaLQ2BOHOsAxXqk-SeVylKlbQDQNK1VxEItTHPmnS8XtHHCusupU176MbZqmWuJzNDIhPNfVFamDzr17rBqah4kUz3EuTXvsybfNtJBz4uwgMh9iTE_BxuWd9ORUFONMBdh9nVBRxlPLWDZzB4yrp6aspxJWWmNGkeolDlvoneBg_KL2f-KUmiwa6QK8ODFQ8XLgf19sPOV_-1y4ZCFLHeMLU6O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135039" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/135038" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🔴
رسمی؛ مهدی تیکدری، مدافع راست ۲۹ ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/135037" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpjWwm1GQ32alTpjsH3CZpArEdzn8MCKwEgLLChfEY3V9fOsFeFU1P3zrb-c9NToCaBDXUjRh-kQDFlsA7cbXtXaT9rGIgM8_RE6eCzwe1NGqh4rWtYphYsDUppeAz-S5SAXeYV2iM_QgxwndIhJBEkoShbUQGrYW1wh6B7CgkH3LF_YYRwBYugJwTxDHxhWDm3KIsfBpSVqtUwQjZRnDcm9ZkEgOXjH_5cfynHbUfJ5RkcHFKmZENGcCbAzOAvTxqej7kYlDQDnMlMVDaeMcwLu8SkGrjc9b-xxTyzmF2zPmkF_RyGfumgGjNRg46VQs_GeF_tAAps0yArLCVQcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135036" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135035" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/135034" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
🔴
یک سرباز واقعی، ستاره متعصب و جنگنده پرسپولیس؛ بازیکنی که برای لباس پرسپولیس، سر خود را جلوی توپ می‌گذاشت.
❗️
❗️
مدافع محبوب هواداران پرسپولیس، امروز ۴۹ ساله شد. تولدت در قلب آسمان مبارک، "داش علی انصاریان".
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/135033" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: تارتار از هفته ها قبل سرمربی پرسپولیس شده. حتی تارتار دو روز پیش زنگ زده به آریا یوسفی و گفته پاشو بیا پرسپولیس
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135032" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
❗️
حقیری :علت جدایی خداداد عزیزی از پرسپولیس مشکلات مالی شدید باشگاه اعلام شده است!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135031" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی جدید پرسپولیس خواهان حضور پویا پورعلی و پوریا شهرآبادی در پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/135030" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
مهدی تارتار تصمیم دارد چند بازیکن از گل‌گهر را با خود به پرسپولیس بیاورد. در حال حاضر تنها انتقال مهدی تیکدری به پرسپولیس نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135029" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/135028" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/135027" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135026" target="_blank">📅 16:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
✅
باشگاه تا ساعاتی دیگر از اولین خرید تابستانه خودش رونمایی خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135025" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135024" target="_blank">📅 16:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135023" target="_blank">📅 15:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135022" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNQUX-zlw4MrTonqrWQcn40wUaueRSMmNPaxctuNsq40vPzsc2okKwy92yiqZdVi6UyaWRe9Qo-gKDMiDrYx6Y-LAwrUU_EXvNtyv77RpJk4tDmZd3Nx-WgJATXW4dg_R5qzbSf0yCK6u_AcksNe1lfXulZSc2_yiA9vq-2-B7f-35egLK93CugX0b7wPqd-v0H-frNKpiG5LvpTmp3GdOgQDipy8TPnRA98cXyFonhW7CQMlv9k5fkUyt8dTMxkgB-mGr1QVwzf1EmXReRvWkmtoRuLOa03bgqLyruzGAlrhtNzFvMWerKKDLWCQKVV-nltVTa-mMtfBQW0FhqWfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135021" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135020" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
تموم شد مبارکه..تارتار رسما با پرسپولیس امضا کرد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135019" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135018" target="_blank">📅 14:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ورزش سه مدعی شد تا ساعات آینده باشگاه پرسپولیس رسما مهدی تارتار رو به عنوان سرمربی معرفی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/135017" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U86I0xNTT1FRI3X-qQA45Lb52wf-UbdRGkOPlXWyiUyrmoQF12eJ4PbS9dc2t4qQ0AXZTTDaNuQm_d8lAumiGvB5-SgT_5GGTlid1gHqtbRpqsFf46TT95kvXbQRzgtw1ShKvOATgNf70bV1dkQzrX1wmQeGecIfVRi-FdG19D-yojSxN9w4ns3zb1jpHWMC0mW_330NAGSg2SoXavdHgV7Pl1Rq1ezE8vGoGzXA3x0vdZtN088w8zLl_v8NSbpbxX0Ju-DVO-p365fx8sL3l9raUHmQfcVi-GqVS67SXywL8Sbm938GJOsGZ2oB-wgqfPiJRfUejRQtfrHblRYQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135016" target="_blank">📅 14:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7568e30ff8.mp4?token=jYErEuUI2lEVIyOLN3-Vl8_Zb5PQjoD169E5e79HR0xptE0U0_8liDb5wWq_jWfpMYMXriZ-7ebxszuEKOu1bOAMn_a9aL-SYTAk1DhLL35KOFhSXh8fWxP706cfGn6CWsSSHnNFhK-HMMQp2UQiMwkdarFe6on_FPdXPv0kNiqQSr1xBiHC0dQfpML6vIxIOLe6KNslpr8DazWRR58E3foLu_E9-9x9wfzNvM-mGXtbuQ_Rw391dCPGipptcIBXePZ6CL2sHa6_BN0WwNNaQ8rkQtvYqb7nwR2tFuTipRNPJkYFuin8a1Rgz3jtJeecxs5fL9d_amg1upYspRQu6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7568e30ff8.mp4?token=jYErEuUI2lEVIyOLN3-Vl8_Zb5PQjoD169E5e79HR0xptE0U0_8liDb5wWq_jWfpMYMXriZ-7ebxszuEKOu1bOAMn_a9aL-SYTAk1DhLL35KOFhSXh8fWxP706cfGn6CWsSSHnNFhK-HMMQp2UQiMwkdarFe6on_FPdXPv0kNiqQSr1xBiHC0dQfpML6vIxIOLe6KNslpr8DazWRR58E3foLu_E9-9x9wfzNvM-mGXtbuQ_Rw391dCPGipptcIBXePZ6CL2sHa6_BN0WwNNaQ8rkQtvYqb7nwR2tFuTipRNPJkYFuin8a1Rgz3jtJeecxs5fL9d_amg1upYspRQu6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مارکو باکیچ : خانواده ام به من گفتند به ایران نرو!
✅
قطعا آنها دوست نداشتند من به ایران برگردم. پدر و مادر همیشه بیشتر از خود فرزند نگران او هستند و من حالا که خودم پدر هستم این را درک می کنم. من هم اگر الان فرزندانم بخواهند به کشوری بروند که هر روز در اخبار می خوانم مشکلی در آن وجود دارد، مخالفت می کنم. نگرانی آنها طبیعی است اما من هر وقت خبری می شود برای آنها عکس می فرستم و می گویم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/135015" target="_blank">📅 14:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135014" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">😀
دوماگوی دروژدک با پایان قراردادش از تراکتور جدا شد/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135013" target="_blank">📅 13:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135012" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0jCuFJes6TXRV1ZuD1LHlyvXFV_tMH0bOxOMz5XK0P_E5vo2vXFNe8xuVNmwG9YjUhqCFyMrp1CFLw64IJrtME_XqGlXkcVtoxfW1Rxphwi0BeFxG7sbcsS_zYsCBp5Nc7r_Y-oK9LooU0E45EEKfy9J4xHquASgmq-fWRadMBQgVGWpCJQjQ_YLa71Df3lBylyn3oYHjBTOam04zTxwdDuRTkkg6d9IFo5Jne1pu37tcgZd5iBFmpgH9sEkECVSbPb3VCUbKbEFvSeIMmdht9bfV8c4Vy38Au3GPIR6edtf6-tJmYA1LpCP1mPtD_OmT8TUx9RpWeVqpifOVThWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری؛ با پرداخت 20 میلیارد، رضایت نامه مهدی تارتار برای پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/135011" target="_blank">📅 13:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl7P8r9Io9dRZCy3ISaYvf5E22sj0sDxgY_jMSWBn34QgUK-87gYxvzdlcDtFh-tDMTJpc6W_B9-ohfgtTp8OpKYJ420sGfiAsnikp0580NTbRqdEFJ2YbArpcRNv9DEElkdjq_G4CCv4XxLyS2rUoFprbt01IPt7p_ghaebKBNqLvTZENB1gjNuJenx6iAEvMG6wXf28THOzLxo6bHJxJgGTfIkP1KxA5ONGKbDfxcTW9NR6vcCB2h--Ak1zMKr3nXZp25zcuID_7DOX782bGpqKqf1IAk9BzsNtyrhizWYuPA99CZOTeM1NoFifzONp_BtIYmJCBA8tAT5NQWBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135010" target="_blank">📅 13:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
#فوری
؛ یورگن کلوپ سرمربی سابق لیورپول با عقد قرار دادی 4 ساله سرمربی تیم ملی آلمان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/135009" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/135008" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/135006" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/135005" target="_blank">📅 13:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/135004" target="_blank">📅 13:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1xAXeUKTqiMGvHsnnMHPE4q9RVa86PiycKo_Cjlq_AKRgFeGDrLJMnqiVsxidTyFNt9u1bO5ZmcKGGjP_hjD68qOs22-jwGzeuUYo4YIqNAJBcmf7MeW_6hFIEMuBWeoq-f66Wt0IcrRyW9C8uYrrS8QM5QspQxaa6JxLcJLP_1JK6I8amaCp9I2hA8sxZAfMKrGPkx0IrquH82wy9YMquiRk1EGJkAmVX8B7ZWGQhpSmmrJl1s5wspXFNl7kzfljjC4gB4fMxQCJxECT6qf5Cq2z2YvLUdGwJBG_gfWrOHVceEr24WC122v-0buljOHoZa85oVyy4FYiuK5U-0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
🔴
🔴
سرانجام تارتار به آرزوش رسید
🚨
ازش حمایت میکنین؟
👍
👎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135003" target="_blank">📅 13:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
باشگاه گل‌گهر سیرجان ساعتی پیش رضایت‌نامه مهدی تارتار را برای باشگاه پرسپولیس صادر کرد تا او سرمربی جدید سرخپوشان شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135002" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135001" target="_blank">📅 13:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgv05UZxKqI7kIxBY7aJ-pWQlXnTU6RFYGE8bvmJSXgXDIM0AfGaNjq5SVOtQywlDKsV29HHXH8HddG7wTZNOKFZaPfsDCkKkGsDBxZh5l4sDsk9ZCdVvEfSUQVfgPIQUf6U2zrozw1oo00EzX_eZ8jc1XnHvpRvHwlY7jSms2d6XZKxtNYx01PDBzpvulskRBIsk5vm2HamBumCoUBD4vpcjamaY8HXEdeTs5Gpx_Hy2aiOR5tE-V-StaKquKEgcJIQ3wS0EaZVoVyRI1ejs3GAYCWHpn6GgyU5LlnSA1sALDqhWZ462Ml-_d3faItC8BwIiTfQYrF_eD1AbhBghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جلسه با تارتار در یوسف‌آباد و خارج از ساختمان باشگاه برگزار شد!
🔴
یک قدم تا مربیگری مهدی تارتار در پرسپولیس.
🔴
جلسه تارتار با فردی برگزار شد که شخصا اسکوچیچ رو در ترکیه هوا کرد.
✍
سپهرخرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135000" target="_blank">📅 12:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/134999" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
#تسنیم‌‌‌؛ مهدی تارتار در آستانه امضای قرارداد با پرسپولیس.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/134998" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/134997" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAZ-MvfVYnM4bPWV-l_bl8azoPfRUo8FkfhKBPbJoXF54ikx505YGV6MZxLE6G7DkL7jcpvOk0y6HNa3tYnYhDqI6hbiJKKryqoWKSTSpRfJi1A2ZzJAFXas_CctinQEPCAsUvKn6-ndrpn5N51RDqBUXde1IR8M_MHdUOkTgOQCoIpJdKm2zveOMvzJjqOf6IVjpVL4kZSlqpCgSJI5_V-ARdpw3hAbLkXl2ug2U_0_Ctjvcu13cMrkHYvNOnWMjZyCVeIykZnu0-f0bILMEDyrvzbED8luMsv1amz_eaL31SZLQfbd6jLUCN0HO9evMOMSHFaKCeg-1kwHdWbS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
بانک شهر از این موضوع اطلاع داره که اگه این فصل مثل سال گذشته رتبه پرسپولیس جزو چهار تیم برتر جدول نباشه قراردادش به عنوان مالک با سازمان خصوصی سازی فسخ میشه!؟
❗️
حالا برید دنبال انتخاب مربی ضعیف ایرانی و نقل و انتقالات ضعیف تر….!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134996" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
قرمز آنلاین ؛ اگر تصمیم مدیریت و هیات مدیره به سمت مجتبی حسینی تغییر نکند تارتار سرمربی سرخ ها خواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134995" target="_blank">📅 11:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134994" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
❗️
#فووووووووری از قدوسی
🔴
تا ظهر سرمربی پرسپولیس مشخص میشه که احتمال خیلی زیاد آقای تارتار خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134993" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
پاسخ یک مدیر ارشد باشگاه پرسپولیس به سوال قرمزانلاین : فردا به احتمال فراوان سرمربی معرفی می شود
❗️
این مقام مسوول ساعت ۱۲ و نیم بامداد به سوال ما پاسخ داد و به نظر می رسد منظورش از فردا همان دوشنبه باشد//قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134992" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
خبرورزشی: حدادی روز اخر مذاکره با اسکوچیچ که همزمان بود با روز عقد قرارداد دو تا بند به قرارداد اضافه کرد که اسکوچیچ مخالفت کرد و همه چیز کنسل شد
🔴
1_ اگه جنگ شد تا روزی که ایرانه پول بگیره
⏺
2– 500 هزار دلار از مبلغ توافق شده کم کنه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134991" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
۳ گزینه نهایی باشگاه پرسپولیس برای هدایت این تیم مشخص شدند:
⏺
مهدی تارتار
⏺
مجتبی حسینی
⏺
حمید مطهری
❌
شانس تارتار و حسینی تقریباً برابر بوده و شانس حمید مطهری کمتر از این دو نفر می‌باشد…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134990" target="_blank">📅 09:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134989" target="_blank">📅 09:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkjhUEjykbZfmdaTQuSlgYcHRB8th5i3-SAL_8jb36uUKBfWt5qxt6CEKHiCU_0Xt3hExqiOh7KA3OqfcxNM-4mw0J76YgyWJlOBFjDs4a01OZwQw4NFloLx2ogvUNogaOWRw3Ltrj4l3URzxkmmVpGeLNvYKvUXIFBsUtBXHs-AqqQT-JU1o-UcfWNhdqVCmWrDjdU0yfESWSEZjxzG-WkqoclIO8pI-mgLVOqOG6Wc4MLhNqFjqNq0k-Ut4r05dA_3hfqn7Uc-cznkI1RyENOcY0qombt4_h4vzBWS4oCMgwucrh-1rviWNHYGeAeOODQs7pvnMQ1S9RknZOaYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/134988" target="_blank">📅 09:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134987" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه ها تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بد نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134987" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM3gXjTzXvcSTALToakTCJhKFjt81mAf-hbeAOU8ccS-QirNsqgsazZfq9a0tK8tD1vH3i2iH2FoqYtv1yZ0gvFO8Fz0XrHufTg4qQm2p2-n1XnrrDmQOVVzn_v_dnNeX1D1oUX3L0SrZrZLYw_1QJKEu02E805EoEDRZzmHw-KDsNRcBpU77R4CT1qO2t5xgxAef3KZH--VYfHcnzc5-oJnLLJDVL4kkwOpQEZmxWILoGInqXZZEd_UQ0Cwh5f1eV35bRvF-eT_uXRpPMdLWB7wzV4uyIBe9qC6dQLBn3nzyNnSoktxoZ6CpTNwByark43ss0EDuKSgKfIH_GfChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134986" target="_blank">📅 01:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nx0L3ZFyG00YLolCgWpxc6pW9dF7ys90LaHNw8Zqys1o2dPBLJDjSJ-3-tiEfSmMt8iq0Tld3hIc_ZLqJb2iRpnz6YkihMpIqYs4AogHUsUzOD-Ch6rqRhwi_4olLLg885YzuOpIr6FmroB4ZReZ80CAHPMow4Rd9-96uKzl9PeKo5JYIZROPRNcOlQvKOlapgpyx7DMHf9jAS6LEDlYQdBTiQD5RZVbmUOOAONrikQFNqAU-2jglljA1Oh4sn9N3VaeJ9LUr76Vc0xomWUjxCwFZosTFdsqriUOiHtrEGOahMi4CXxQpm6qx81f0vjRIApqm_hZLAL7mEA0xeRHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
یحیی گلمحمدی با حضور در تمرینات دهوک عراق به شایعات حضورش در پرسپولیس پایان داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134985" target="_blank">📅 01:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از ساعاتی پیش دوباره باب مذاکرات با اسکوچیچ را آغاز کرده است و کریم باقری مسئول راضی کردن اسکوچیچ برای برگشت به میز مذاکره است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134984" target="_blank">📅 01:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
🔴
خداداد عزیزی: آقا کریم ترسو نیست ولی دوست ندارد اینجوری سرمربیگری را تجربه کند. آن هم باشگاه بزرگی مثل پرسپولیس. شاید او شرایط را مهیا نمی‌بیند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/134983" target="_blank">📅 00:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
کریم باقری آخرین راه ارتباطی باشگاه با اسکوچیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/134982" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
شنیده ها :
🚨
انگار حدادی دریبلش خیلی رونالدینیویی بوده و دوباره رو میز مذاکره با اسکوچیچ نشسته است.//قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134981" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134980" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فوری | حمید ابراهیمی:
🚨
مهدی مهدوی‌کیا سوپرایز بزرگ باشگاه پرسپولیس برای نیمکت سرمربیگری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134979" target="_blank">📅 00:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134978" target="_blank">📅 00:36 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
