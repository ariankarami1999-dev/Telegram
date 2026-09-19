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
<img src="https://cdn4.telesco.pe/file/qLhLmHA8OLXraenVcJUmytpExJKMH8newebthXSX8tIjEnzP6QW2pU2pOHXKeYM_l8-IbnaqMArVnH779FbVc-358vSHVVto8dXiOJpE9FiHoUiHC8mLwHnct6KT1x9GnwGogZBTHXIBjGi0qHDQtdcKq0-VKRjbgMJgs7u6Oj-SYmp-nSvQT6Pn11h2Dfx_QS8y-Er9pPr_Oi2-cIDz9vQAgH2iPa0byVHs9H0xgTAv8TCNybYDNNhQhMagss1hK810mOOzMJr09dChbMSpVcBmGJc51nzAPTlN8lTg5ol9IijeO9rP-exxzT6c_Hs3vk-2KJ7555Xl7Mwb-DgWng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 02:05:02</div>
<hr>

<div class="tg-post" id="msg-148299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/148299" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDiWP7k7KWIypqYQgiRINk1_RC4izINLX7-X9PjPaDJNDYsyvRzINLHvD22y8hHEvYY7mu4UGvKh0CfTlX5cdfHE7ILBcnYOLOT5RP9hzn826SEFasTFQnRtfqgtCNgN0MTv3tOFxSUx4kuCzZ7vsvp_2eeANTEbZ8bVyZSlsqtHwEeLZ7rcJ_k2kkNWjbBAmjwBItGlb_rj7SZ44HdJ2gy93b4rIErtF_UWNNumEWY5CQncE8hKBSnXuTvNh8a35x998XkoSfxzdA2vLCEpE91Gq7QKT9TTysY-dsd4r8-5J-IpUxoUCtPD0JwzZsPC0Hx9wL4MTONT8siYmUbuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افرایش شاخص سفارش پیتزا اطراف پنتاگون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/148298" target="_blank">📅 01:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/148297" target="_blank">📅 01:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/148296" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/سفارتخانه مجازی آمریکا در ایران، با توجه به تحولات اخیر در منطقه، یک هشدار امنیتی برای شهروندان آمریکایی صادر کرده است و احتمال بسته شدن فضای هوایی را اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/148295" target="_blank">📅 01:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/سفارت آمریکا تو عربستان هم هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/148294" target="_blank">📅 01:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/هم اکنون منطقه در آستانه جنگ جدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148293" target="_blank">📅 01:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری/سفارت آمریکا تو ترکیه هم هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148292" target="_blank">📅 01:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوووووری/رویترز: ساعت صفر نزدیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148291" target="_blank">📅 01:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سفارت ایالات متحده آمریکا تو بحرین و اردن هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/148290" target="_blank">📅 01:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سفارت ایالات متحده آمریکا تو قطر و کویت هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/148289" target="_blank">📅 01:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سفارت آمریکا تو لبنان هم هشدار صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148288" target="_blank">📅 01:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خبری در راه است
⁉️
🔴
سفارت آمریکا در بغداد، اخطاری امنیتی برای شهروندان آمریکایی صادر کرده است و از احتمال بسته شدن فضای هوایی به دلیل تحولات منطقه خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148287" target="_blank">📅 01:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b9da2b2a.mp4?token=KjgHqYedBGoM8Eddk3qF3xyHfcgDDT9Q5NA8-jWHjPlQalz5kbX8bQ7MtOgrMFRCcRtsF1exatAObGDDyzEzsG3R7JbK55FQsHTutFZ4eS7brZsFO6ES5B-Agm2z4T4W6cwb0mjlAAwr5bMXYqJGE_MadGQow8AFZ2HsMUx07Mwbj1lf0iYP-geMwUjnQGXynR6y4rWC5xuUUYuzQDU-XdsHbVqnHe8iI4wU8tK1O7rnszci-h3VyRiAODDjZIQY-m85kwb8bsdGmeV_nyeUeqNdmoS2_7tOL1NpY9kPsl3Vo6GsRcT-xTWkDOFzFhtZ138IaMgQzw35kUURLfG-XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b9da2b2a.mp4?token=KjgHqYedBGoM8Eddk3qF3xyHfcgDDT9Q5NA8-jWHjPlQalz5kbX8bQ7MtOgrMFRCcRtsF1exatAObGDDyzEzsG3R7JbK55FQsHTutFZ4eS7brZsFO6ES5B-Agm2z4T4W6cwb0mjlAAwr5bMXYqJGE_MadGQow8AFZ2HsMUx07Mwbj1lf0iYP-geMwUjnQGXynR6y4rWC5xuUUYuzQDU-XdsHbVqnHe8iI4wU8tK1O7rnszci-h3VyRiAODDjZIQY-m85kwb8bsdGmeV_nyeUeqNdmoS2_7tOL1NpY9kPsl3Vo6GsRcT-xTWkDOFzFhtZ138IaMgQzw35kUURLfG-XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات عجیب دو دختر جان فدا و مومن و انقلابی در دورهمی حامیان حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/148286" target="_blank">📅 01:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
👈
محسن رضایی:  محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148285" target="_blank">📅 01:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
👈
محسن رضایی:
محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/148284" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سفارت آمریکا در مسقط، اخطاری امنیتی فوری برای شهروندان آمریکایی مقیم در عمان صادر کرد و از آنها خواست در شرایطی که تنش‌ها در خاورمیانه همچنان ادامه دارد، احتیاط بیشتری به خرج دهند. سفارت آمریکا به شهروندان خود توصیه می‌کند هوشیار باشند و برای احتمال لغو پروازها، بستن فضای هوایی و اختلالات سفر آماده باشند.
🔴
این هشدار، ساعاتی پس از صدور یک اخطار امنیتی مشابه توسط سفارت آمریکا در اسرائیل برای شهروندان آمریکایی حاضر در آن کشور، منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/148283" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هم اکنون بمباران جنوب لبنان توسط اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148282" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148281">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ژنرال ارشد ناتو: ما آماده‌ایم تا به هرگونه تشدید تنش احتمالی از سوی روسیه در بخش شرقی اروپا واکنش نشان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148281" target="_blank">📅 00:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148280">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYj_qBQG2fKivva3eNp5KG2KG00_nXQUzuzECiua6SVHeLrPzWXyi7z2bk_lCMy9J-6BShaTwrEX6F3__cHhGCasS94JQsIQQnnoQb7A0_Wbw5qjCP-pT7M2dfz9CCvZfI7-E91eWWslhCjQM1m6N1YsTlqP0u6VLLDjTt87UNzSsrPJCEi9tXcD4n9JvFTRTJf5fqYR-oSF9RQSophsbIyVwrsnPpdhJeL58U2o9LmxS9EZ8kCV0AZihY8A45gVlN6z1fhd4KM74_EyMq8cocFwoFv1pEaDXrlGKfEqGEWua95KxcI05MEkYbphC50NwmobtY-gP7Gsg5PxFSKlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یه پدر تهرانی که ۷ نفر گروهی به دختر ۱۵ سالش تجاوز کرده بودن، رضایت داد و هر هفت نفر آزاد شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148280" target="_blank">📅 00:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148279">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd1c6f7c4.mp4?token=XcrFIrms4q9SZwoNVIbmELUNIk3VG8H_qAnVSwnrluFkkpSHcBGPiiM1hFs9X5tQfFinAwnMOyGR0yTW_3qeL08kYnKBhhjtcR2zCwXhGwYz4hsg7X9unTh6Dlo2K9EWv7-xFvp2y9eQrkcHegb9gOvIBLsNn6Ij4TzDghMJTJnsYqqhgxEpc45LW-ErWRYUDTQ473c1pwBQ_JxPBbyWRM10gTsIBjRrlfK6dSkNXWM40vmUNWYu9jYwb99Q6Ab5_U56PGO4SmEGLsA3wo8IHU8CJMhKM7MeyjvBMnf85ysw5DOHoVcN9ds51joVSg-NgpqYrjLhvfgq7vK1f6I7mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd1c6f7c4.mp4?token=XcrFIrms4q9SZwoNVIbmELUNIk3VG8H_qAnVSwnrluFkkpSHcBGPiiM1hFs9X5tQfFinAwnMOyGR0yTW_3qeL08kYnKBhhjtcR2zCwXhGwYz4hsg7X9unTh6Dlo2K9EWv7-xFvp2y9eQrkcHegb9gOvIBLsNn6Ij4TzDghMJTJnsYqqhgxEpc45LW-ErWRYUDTQ473c1pwBQ_JxPBbyWRM10gTsIBjRrlfK6dSkNXWM40vmUNWYu9jYwb99Q6Ab5_U56PGO4SmEGLsA3wo8IHU8CJMhKM7MeyjvBMnf85ysw5DOHoVcN9ds51joVSg-NgpqYrjLhvfgq7vK1f6I7mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از استاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148279" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سفارت آمریکا در اورشلیم به شهروندان آمریکایی در اسرائیل و منطقه هشدار داده است که با توجه به افزایش تنش‌ها، احتمال بسته‌شدن فضای هوایی، لغو یا اختلال در پروازها و محدودیت‌های تردد وجود دارد و از مسافران خواسته وضعیت پروازها و فعالیت فرودگاه‌ها را مرتب بررسی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148278" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
گفته می‌شود کارشناسان سپاه پاسداران ایران از منطقه باب‌المندب، بندر و فرودگاه مخا و همچنین پایگاه جبل‌النار بازدید کرده‌اند تا امکان نصب رادارها را بررسی کنند و بر روند حفر تونل در ارتفاعات مشرف به منطقه نظارت داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/148277" target="_blank">📅 00:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KztRVUl5o3fiMiH8nuzUZUB2WWefvjbTPpSg2TzwW9guGUb0PIS9hrb93b3QowdZniZ7sm77osIlB3uJULaoRXMEDsc_dzL5u25OQP8-c9jU__EokFjW_m4MseJyvTkv_D_VOpI2GKt8DEKovMOLkGE3qpMzUgrhnHspes7AkZNyvywi9an6lP4kbFFFxGD_GWJyhzZzMca0kWOzvr_hGAMw2PKbB4aBf7Vjgy5S285HAuD5uIEHynmg983Lz9vgdCnfXiYo_1qIWzTbMCXWfo-KCJ3ivH-h0QvF1vDM0rEr1JA5a1dvYlDa3rzT8Sqeo9FZA8vgcQlPWXRVPfMoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
اینجا ببینید
😐
👇
🚨
مشاهده فوری</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/148276" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
امارات گزارش هاآرتص درباره هشدار به اسرائیل را رد کرد
🔴
یک منبع رسمی اماراتی گزارش روزنامه هاآرتص مبنی بر اینکه ابوظبی در هفته‌های پیش از حمله ۷ اکتبر، به اسرائیل درباره حمله قریب‌الوقوع حماس هشدار داده بود را رد کرد.
🔴
این منبع گفت: امارات مسائل امنیتی را از طریق نهادهای مربوطه با کشورهای دیگر مطرح می‌کند و چنین جزئیاتی در سطح رهبران کشورها مورد بحث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148275" target="_blank">📅 00:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af31257978.mp4?token=D8S0c02OzDsQVZWueXVj03R1DNT0lpTlVylNmxq-StPPWj9M2j4Fe97o5xmWcBtmszxsHKSEMnvUQCAWxHqmU4IhUd09G1jS24zQ_wTz6OWHBH2MIPD4Qo1M7tdmBtTpn14JB42jc4SHijE64pjjOQ4N-2rn8ijH3_SBetVO7vXWmLda4Z13NGRpg3X-BVC9x5kWHUNwCXiQINeIG08Qt1E1k--noCq4J_mL4grH2v0YQGd6Mitgc7uqCzNwTVdnn1lH_8dRgwGyUjk5tyZwdupPUJg0mFC7D7fcjn8gOwOyNtgMOVvxU_Bl9cqHx-fEPAN62WwkzH9BQYzCwGlLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو دفتر سیاسی انصارالله: این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/148274" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148272">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4X9jGAmr4cfYjpzFHiPt66C_TMTVECsmQ0u2_wocqAgTYT3hmVg-Uc5tcQylSgSUczNciQX3kYoeFCQvSBopUCk0Z5WG5Bf50QIXoxG1HA1IwD-0EaAyfE5dF7LADmi4bO-89aD_tw-VmWxzez9KyS7HGyfFWadKHtNbYmdSY7bVsCklradoGZK5ODt9LV9jP-bnO93JgF5Mt6T4tufKLu9tcqqvsyyFsV-wCckDkAl48qNTb6WbrUClDKCUleZPy7iwJIL6wwhdLfAGIATPlSn3NDQMvCSvjFsQqjGmRyhOnXHTFXevf6t0pnkS8JB12PwLjjXEdv7PK81wiHJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e49b11fa.mp4?token=SEYKLD5LRPNqt5CBDMVOeS-TInaEHSGQW--I2-nH3dnUaHAsxu_7h3AWXTCEpeBgLxqKEY4Q9nIRWpcEwE6G7CCbqIln-85v4kylmAHty8KuyCXm5RVSlxT59jXhUntrZ9noVeLlB5gtYN_14653iUt1bn1sqcpX--wP7LJWb-BuCU73_ZFAC2lQGV3N0FOSxHRwO449MoIAXEJ36z8VGBW8u0iTCmftx9mXrM_tpKY6AfcltAST6V2kyIY1dc2ieZp30DXQEcjUCkuKJ96A3AkzklfrJD02HYGYAUBgFoGg0hE39qwvRxTf6_RFXHz9nEoPvsDxQ-V0KK0GCQhTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل حملاتی را با بمباران هوایی به شهر کفر تبنیت و منطقه نباتیه الفوقا در جنوب لبنان انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/148272" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148271">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نخست‌وزیر لهستان: درس تاریخ 17 سپتامبر 1939 فراموش نخواهد شد، اگر کسی جرات حمله به ما را داشته باشد، با پاسخی قاطع روبرو خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/148271" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148270">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نقض منطقه پرواز ممنوع در محل اسکان ترامپ و اعزام اف-۱۶ به منطقه
🔴
هم‌زمان با اقامت دونالد ترامپ در نزدیکی کمپ دیوید، یک جنگنده اف-۱۶ امروز شنبه پس از ورود یک هواپیما به محدوده پرواز ممنوع، به این منطقه اعزام شد.
🔴
بر اساس بیانیه نیروی هوایی آمریکا، این هواپیما حوالی ساعت ۷:۵۰ صبح به وقت محلی رهگیری شد.
🔴
در جریان این رهگیری، اف-۱۶ مُنَوَّر (flares) شلیک کرد که احتمال می‌رود ساکنان منطقه آن را دیده باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/148270" target="_blank">📅 23:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQxK0AoUcGtWNgmG__iFkccoKaK4pTN99DJunNPTzHVo-FXsbkSid7WBzRq5CjqBQb2w1DdiJEI24n85pB79ztXOGV5tBBhfTSXd9cZnQA-65VupQKtMOCa_a-qF_AutL4Z9m279UeT1x248Lvvoj7rmmS4eNr3odOoo-71E16l48rfvTDP18BSYwohSCts60b_spgBG3pMtLUA1zhaK-3AAji3DvRp2Y_DURz37KZqZMh-y3d5S-DIK2RTd7B1MVnZCGfsc_Hhk0a4jRyMq-hPG5tlesJPjm9P-bDGG5nXMX1OarP_9wV8OawHTGJMpyeh109ZWJnybG2r_HCHHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی میگوید یک موشک بالستیک شلیک‌شده از سوی نیروهای یمنی به سمت شهر ریاض را رهگیری و منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148269" target="_blank">📅 23:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEGY-VAF9QFky0kkYFubdAqVqalsnytQhx137K6z_4F9PWaqhVzFz3zcfZNdfJd_RedZWo-ycojXXYjdvNycHapMf2F1DNGQ_3YYu2a4znCyHZZoLJT9TukaX3f9NGJCNTaRGcMnNOAVYb20TUbbLAiUu6nkFVyy-a8-dwKcnxbVQnT0WEd1wbNI6Up0TEgIbLlt57DkTQfHDiAQSDIsfVEKRC-_WTJSt2xt-rK19fNnEWjdWQIrk1yqc057A-Tk7ec4OiQJPwXc_b8XxrcIMN3Pz8_IpUKpIb7UqSWfFbg-UzpdT3xTeX7f8RRLSLSUoy9ox8aoRoLR0KSdaGURkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو تصویر از یک کشور به فاصله چند دهه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/148268" target="_blank">📅 23:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا: جنگ با ایران در مرحله پایانی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148267" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ما نمی‌پذیریم که عربستان به بخشی از درگیری جاری میان ایران و آمریکا تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148266" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
امارات میوه و تره‌بار صادراتی ایران را برگشت زد
🔴
رئیس اتحادیه ملی محصولات کشاورزی:
بیش از ۲۰۰ کانتینر یخچالی ۴۰ فوت حامل انواع میوه، تره‌بار و سبزیجات صادراتی ایران، از سوی دولت امارات متحده عربی برگشت داده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/148265" target="_blank">📅 22:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی سازمان غذا و دارو: واکسن اروپایی آنفلوآنزا امسال به ایران نمی‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/148264" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/148263" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
آموزش و پرورش: ازین پس آخرین جایی که تعطیل می‌شود مدارس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/148262" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / ترکیه: آماده کمک نظامی به عربستان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/148261" target="_blank">📅 22:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
واشنگتن‌پست: محاصره تایوان می‌تواند آمریکا و چین را وارد درگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/148260" target="_blank">📅 22:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpEMY3T-58N3EZiNKkvvGuzdZvzvvmfZN0q6fyxLyFUlN8Wm4YYYAkldaVzsEzetzVgtSZQgnH9Fchr_BTSIGHtN5YFvahdSyLQh45cLW0fpy4DRsAeyzDMMWdTl3J69KCXn8p-9coZkbNU3ZDBtlTrJs90bUNS5QrOE3Kd0DM1GbZWFqWFPzyBXofVXuWBBHsxTbIlBBHcSYaFdK2UtUyyfCat_Ao9vcz8mnqkwWyNRjMIT_RkJjFqo1u-jFmpBgY27a3hnRpYl9l5LQCHvlXvImH9IPvMfobTfOUfaUNKIkVg0DcuGsNXPRkBWFS3IisaUvTtoAy2euCZaRxt9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار تصاویر از اپراتورهای زن پهپادهای FPV در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/148259" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148258">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تاس به نقل از یک منبع ایرانی: ایران آماده بازگشت به مذاکرات است، مشروط به اینکه آمریکا حسن نیت خود را ثابت کند
🔴
تهران همچنان برگزاری مذاکرات درباره موضوع هسته‌ای را ممکن می‌داند، اما تنها پس از اجرای کامل توافق اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148258" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148257">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دولت لتونی فاش کرد که اطلاعاتی در اختیار دارد مبنی بر اینکه روسیه در حال برنامه‌ریزی برای حمله ای محدود به اعضای ناتو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148257" target="_blank">📅 22:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حوثی های یمن: با تعداد قابل توجهی موشک بالستیک به اهدافی در ینبع، تاسیسات آرامکو و ریاض حمله کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148256" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148255">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: نیروی هوش مصنوعی [در ارتش آمریکا] تشکیل می‌دهم
🔴
رئیس‌جمهور آمریکا: درحال تشکیل نیروی هوش مصنوعی هستم؛ درست مانند «نیروی فضایی» که در دوره اول ریاست‌جمهوری‌ام تشکیل دادم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/148255" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148254">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل : ترکیه به طور رسمی مجوز فعالیت بانک ملی ایران را در استانبول لغو کرده است. این تصمیم، عملاً تمام فعالیت‌های این بانک را در کشور به حالت تعلیق درآورده است، از جمله تمام شعب آن در شهرهای استانبول، آنکارا و ازمیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148254" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148253">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
به گزارش شبکه i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قبل از سخنرانی خود در مجمع عمومی سازمان ملل، در شهر نیویورک فرود نخواهد آمد.
🔴
به جای آن، او در یک پایگاه نظامی خارج از شهر به زمین خواهد نشست و سپس به منهتن و مقر سازمان ملل سفر خواهد کرد، جایی که قرار است روز پنجشنبه ساعت 14:00 به وقت محلی سخنرانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/148253" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148252">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در ادامه تحرکات نظامی خود در جنوب لبنان، اقدام به تخریب منازل  و زمین‌های واقع در شهرک «منصوری» با بلدوزر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/148252" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plQqZv4Edh2bho4RjQdONrYWLHBEamkEv-LZCMF0YC-MoOf6W0HT7b_ir4T3jFNGgj47LfeaIOLmL9hFeE0_LTeWGTC8wChQayLfEv4x8XEQlzPQJgh7OIhWpjUrCncOJiPGC8-CqkGb9r0i_grpakw697ez0QqJzUrMOg89mxPKZwKJt5ViAUF-jhhzRb0ugpW9-r2LUTv8VyaS_NGHz3pnxhl8mTQDmAjwT0Mb-LYUucuzHY6icueVzgUr-JPA8nFTTMElxQD8gbKPlb6fFR7xAgQuWzo8p4EB4WkzyLGaMuB0AsRokyhJNWh7CjEraKV9D_y3mTzjCe5QmmBR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: متأسفانه، دادگاه عالی ایالات متحده از شجاعت برای بزرگ کردن دوباره آمریکا محروم بوده است.
🔴
در طول ۶ ماه گذشته، با تصمیمات معیوب، سیاسی و احمقانه خود در مورد تعرفه‌ها و شهروندی حق‌الولادت، آن‌ها هزاران میلیارد دلار به ایالات متحده آمریکا خسارت وارد کرده‌اند و برای همیشه روشی که مردم از طریق آن شهروند کشور بزرگ ما می‌شوند را تخریب کرده‌اند.
🔴
این فصلی غم‌انگیز در زندگی و دوران آمریکا بوده است، اما ما پیروز خواهیم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148251" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در یک فروشگاه درپی حمله موشکی روسیه به شهر دنیپرو اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148250" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/ساعاتی پیش عربستان سعودی رسماً از پاکستان و ترکیه خواسته است تا پس از حمله به فرودگاه بین‌المللی ریاض،
پیمان دفاعی مکه را فعال کنند و اقدام نظامی علیه حوثی‌های یمن را فوراً آغاز کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148249" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر کشور پاکستان فردا به ایران سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148248" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148247">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148247" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
👈
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست.
🔴
شروط ما مبنای مذاکرات بود و آمریکا آنها را نقض کرد با این شرایط نمی‌شود از پایان جنگ صحبت کرد
🔴
ایران و عمان درخصوص تعیین مسیر امن تردد در تنگه هرمز به تفاهم رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148245" target="_blank">📅 20:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnDOetuTimbIw4agZhvSxgG-WeS1Fr8c3A_p56VnHWxprsdhk40a7H3pgZ3gcBBZNI60rvjeDUvXgUAPW-7hxDFqXIDutOyd_Ty6y9RuW3vC0Kd-rATMMUEINjam5WP_pkiFYNK8aFjl_vLDkSpXt8XGgsKRnktvBrilvCv8moJFFYwqPzalxQEp8xTqwCL1Ut1zIqioZo67WSQssKaLTFrrd_aOiDu4AC0jcDRABgahMpqbkVNWafKI-FeEA27Q8H3H6Zonsq2N9hFRljsdoMqe6BEUktkBwwrWYRLTYCfyabmcuOnr0WlXxFbHb-sZChuqQMdn5PU2_JJtMvnhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر وایرال شده یه خانم تو دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148244" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148243" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148242" target="_blank">📅 20:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هشدار سفارت چین به شهروندان خود در عربستان
🔴
سفارت چین در عربستان سعودی اطلاعیه اضطراری صادر کرد و از شهروندان چینی و شرکت‌های تحت حمایت چین در این کشور خواست تا اقدامات ایمنی را تقویت کنند و بلافاصله پس از دریافت هشدارهای امنیتی از سوی  مقامات محلی، به پناهگاه بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148240" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148238">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZDDVgQRC-KZbKmxEFvqB7PM3nAegaImD-4M0IhYXx8AOQriZIyFblN9JhtppFuesNIk-FO-o9BZcsVrb0EOFXZWOOwJ2jrDHliJeAJZVISCfxBiYJDfLBa6kULxU5ZXnjvRA4w8scW7pmmpic_40BZyG2Ux965xPn51Uu8Dz1ax3-oMT_oEHCbxhpNiqYrgjTnQLd-7P-YgCr9lz2VTSq_ydpwlcmJkI5064BsGL5IJr1WvFS1uz4eSegu61MeGZBCuI46FYx0q0ph7Yn3QIYNpVrew3tNwJ5coACIigOivewlp75h5fUWy1VBzuCscFoxN1H4VowYci7mDGsOyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzPqDRU47SNic257HB1_alTUmwZDvUaEz0i3VsXGlM4ySjcdwU5FMrQQYCz4el60ncWBzhm6fDVwC_QHvv9QJN8jv8iQQPZCecbvk7PKsB16fPaZG4nzt8uNN1fDpXYX9bEPODtW5IWhgtzYtBzqdi0t1AeQcjpQg7c3qPjhTBpie7LqdgxP-L7GhddXOI_kyD0ePHaU3V6Jh41PVhkwq5YuM9jTibUssMJkFczjeEdG7bIYKxAic4m_wdyPKjl0Q0z-lfWz0w3TFhVrOsbc9E8g_zT0s3rdBw8IqA02UQkRcV6i52i__7uHJqJ87U5VffC5HB6XN8cKoXnZxx3TmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قیمت امروز انواع محصولات سایپا و ایران‌خودرو تو بازار آزاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148238" target="_blank">📅 19:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148237">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نایب‌رئیس کمیسیون امنیت ملی: عبور کابل‌ها از تنگه هرمز هم منوط به مجوز ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/148237" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148236">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو: دو سال پیش، نصرالله هنوز در پناهگاه خود بود. حالا اون‌کجاست؟
🔴
سنوار کجاست؟ ضیف کجاست؟ هنیه کجاست؟
🔴
و ما چه کاری با خامنه‌ای کردیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148236" target="_blank">📅 19:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148235">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ساعت کاری جدید ادارات از اول مهر: از ۸ تا ۱۳
‏
🔴
رئیس سازمان اداری و استخدامی کشور در بخشنامه‌ای ساعت کاری دستگاه‌های اجرایی را از ابتدای مهر تا پایان سال جاری، از ساعت ۸ تا ۱۳ تعیین کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148235" target="_blank">📅 19:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148234">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
👈
محسن رضایی: ما خواهان پایان جنگ بین عربستان سعودی و یمن هستیم و من معتقدم یمنی‌ها نیز خواهان توافق با عربستان سعودی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148234" target="_blank">📅 19:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148233">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ رئیس‌جمهور آمریکا هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148233" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148232">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALn9dpzSFY59LxqSJ1mjAtiUbPrH9t5gM6TaPsfu-piiR758aBBAejmxssYyB5nuNef0J_lT8k_k80e4J0s-yRlHmShEth3Y2ZjdjPtHbbyoF5fnhiKr1Cksz52In0ygKSYFMS_cuSXO3CrA4b1Xe-hHDEJrSGyj-v1yMcEfyz3WhKqW9Y4Nbn6zlMA-kHd4POEGUFO13tcr3CEffdXTT2EYAg4NOtyrhSd6W4PQOSaxouXRTTLF2aZDPgRXZ-7QyyZCr09-XbApumLwFvXDLX-NlWAe-y5UHY43OVzSIuLIECxGCDSP1GcP8cX8QuMEmu8gPTwKxtG-iGYHR4A4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین تارا 3.5 میلیارد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/148232" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qogMSTC8iOLM01v7AuJPaB6gGLI5qTXfzZlc8eGeqSNrFj3uq416B6YBx2esrU-9brlPZGk7jkCxK2nUSBVmJVyVQrUHXRyyF7p8vbLyQ3koLutkUJn5_xdMJ4XITk14QvWxTEZPoj9HueuwAy3DFh2NPBM3aXhrIrj5QngxTEzhEma_gD4cFH0MAsAlxt2sFCy96iyLUZVCv_hfNqpOHrnkwijeDAfWBYAfpGlJbQftvM206IrwiqGoPcE7WuskOQWEa90zYIFMwqQGA17JzV-msNVHDC8gIu9o4nuRHLA2UKGFtBAF8aheTu2MRxOM37huatNpE_3A9D0ipWKJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوبا در خاموشی سراسری فرو رفت
🔴
شبکه برق کوبا به‌دلیل نقص در خطوط انتقال فشارقوی از کار افتاد و میلیون‌ها نفر بدون برق ماندند؛ تلاش‌ها برای احیای تدریجی شبکه آغاز شده و برق برخی مناطق و بیمارستان‌های هاوانا وصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148231" target="_blank">📅 19:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3De9_wJe7SF2VMMqG2ad4Ii_kUmgxjVO-zhkGYoyzN1w7nbDEJRg4zAcPPga05G2h4k5LdNccbi9fuFx47KVvRBJLwFiS6s0JRHRtKus7bigWwmfiPQ2Wd5Xv7gd7pHqlMtO8GWpu93AbZvFRM-mjZ4gAoosGdwlRNrnRYV9RQTWDKF27MGZ0B3Ldewf8j3jxL2EsijIcdKN0mkbzEmqLVjKIwSwL5VHbtho6z02uRiCL6w7STC0Us2eSHvTGXLYTMRyc8sk9AWoOyVQgM_mnnXiIOi_5Moq3KZAPM7aqkDePayRBZ3WxMdtcXLNYYoqyTrfYuOe91b-vzsHwRp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ نظرسنجی‌ای در تروث سوشال برای تغییر نام هوش مصنوعی به «هوش برتر (SI)، هوش افراطی (EI) یا هوش معظم (SI)» منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148230" target="_blank">📅 19:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
گاردین: بحران سوخت در فرانسه در حال وخیم‌تر شدن است، زیرا جنگ در ایران باعث اختلال در عرضه انرژی شده است. در حال حاضر، ۱۱ درصد از پمپ بنزین‌ها کمبود بنزین یا گازوئیل را گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148229" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌ …</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/148228" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148227">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پولیتیکو نیز اعلام کرد که خبرنگارانش در روز شنبه از ورود به محوطه کاخ سفید منع شدند، پس از آنکه ترامپ تصمیم گرفت این رسانه را همراه با سی‌ان‌ان و ام‌اس‌ان‌او از ورود به مجموعه کاخ سفید منع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148227" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148226">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ویدیو وایرال شده از ارزش پول ایران
ادم نمیدونه بخنده یا گریه کنه..
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148226" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148225">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌
🔴
ما نقاط ضعف ارتش آمریکا را می دانیم و بیش از گذشته برای مقابله با حملات هوایی آن آمادگی داریم.‌‌
🔴
به این باور رسیده ایم که استراتژی خود را در قبال واشنگتن پس از خروج از یادداشت تفاهم تغییر دهیم.‌‌
🔴
اخیراً یک موشک ضد کشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/148225" target="_blank">📅 18:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148224">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی پادشاهی عربستان به مواضع انصارالله/حوثی در جبهه شرقی تعز، یمن غربی.
🔴
این جنگنده‌های نیروی هوایی عربستان از پایگاه هوایی ملک فهد در طائف، عربستان غربی، به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/148224" target="_blank">📅 18:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148223">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ: برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148223" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148222">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت
هگستث، وزیر جنگ:
برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/148222" target="_blank">📅 18:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث وزیر جنگ:
اگر ارتش ایالات متحده آمریکا رو به چالش بکشید، شکست پایان شما خواهد بود.
🔴
در دوران ترامپ، جهان آموخته است که ما فقط برای پیروزی می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148220" target="_blank">📅 18:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: من جای ایران باشم، دنبال ارتباط مستمر با ونس می‌روم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148219" target="_blank">📅 18:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5phdGSj23PJrjOPCq-D24XozCv70VQLv81W17uDMJUnSRlVGJxmwXYDXovSWs4vfo48VwSZcr5yxZDyS5sS-H0aUMn7iLOqAs1SFJfORlSYSrQxyh2gDxP7GUn9OclH93dJOnf3ekq4Gf7x7FIUXW8c76M2mK0hwvq_OrJJVZf_XKir27jdSBCNKDD-6cmABp1ZPYMhcqLH2zMdLFbK33EEuHQ-v29a4ZpR-la9piu-iXwO8VC_sBTxSkwI5vBQSk4onue_3tLcnjhmu2QaRE4QDPTC9sIOmBcL2puEBZqpYbyJmBXL9XfQFuvdbFKSspTCtrGnZi67Q5Z--98LwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی تراستی‌ها برای افزایش سهم محموله‌هایشان، کشتی‌های رقبا را لو میدادند تا توقیف بشوند…
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148218" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148217">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب در مناطق مایس الجبل و المنصوری در جنوب لبنان ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148217" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148216">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حسین پوراکبریان، عکاس و طبیعت‌گرد، تصاویری از پرواز صدها فلامینگو بر فراز دریاچه مهارلو در استان فارس منتشر کرد و در توضیح این تصاویر، با اشاره به گسترش نمک و فاضلاب، نسبت به وضعیت زیستگاه فلامینگوها ابراز نگرانی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148216" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهایی حامی اوکراین است تا اراده ناتو را فلج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/148215" target="_blank">📅 17:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148214" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جوزپه کاوو دراگونه، رئیس ستاد نظامی ناتو: در مورد فعالیت‌های ترکیبی، درخواست خودکار ماده ۵ (معاهده ناتو) مطرح نمی‌شود، زیرا معمولاً این فعالیت‌ها از آستانه بحرانی پایین‌تر هستند.
🔴
منظورم این است که یک حمله مستقیم در دستور کار نیست. اما یک حمله مستقیم، به طور کلی، فوراً منجر به درخواست ماده ۵ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148213" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148212" target="_blank">📅 16:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کمیسیون امنیت‌ملی: کاری کردیم که آمریکاییا دخل و خرجشون دیگه نمیخونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/148211" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148210" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه هرمز همکاری می‌کنیم.
🔴
این تلاش‌ها نتیجه‌بخش بوده است. حجم نفت خام، بار و گاز طبیعی مایع در دو هفته گذشته، بیشتر از هر زمان دیگری در شش ماه گذشته بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148209" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ژنرال برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (CENTCOM):
نیروهای CENTCOM در ماه‌های اخیر، انتقال بیش از یک میلیارد بشکه نفت خام از خلیج فارس از طریق تنگه هرمز را پشتیبانی کرده‌اند
🔴
ما به این دستاورد مهم دست یافته‌ایم، در حالی که با ارائه حفاظت هماهنگ، به عبور بیش از 2000 کشتی تجاری از این تنگه کمک کرده‌ایم.
🔴
مسیرهای اصلی عبور در این تنگه از مین‌ها پاکسازی شده‌اند. هزاران کشتی از این تنگه عبور کرده‌اند.
🔴
بیش از یک میلیارد بشکه نفت خام از طریق تنگه هرمز از سوی کشورهای هم‌پیمان خلیج فارس صادر شده است، و ایران به دلیل محاصره قاطع ما، هیچ بشکه‌ای صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148208" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=U6g34qlg2oy5D9Cw1JEsJrGRRVgmYdR470ArD5erq13B_i6aTAt0ZO6NN2J7u3fn1YSBeaaiYF8n7SMNIBtA8ErYYdbFYjYcyig-wGsZyzoG-Ba15DhRPA5zNAHjfQyu-5_462HBwGTqxAogA_1aiFhFu7Nuc7Ik8pIW3aDdVFL99akAMpnXDL_UlamLDyRN84srm-65xFc3EvXd35O-PFRjAONDaNWoBdpJGF8VZBkVD9iJOrGL-rgeMD5RFglQFY9a_3_vJrTtHmBuPu1aYpaGtizV-KydvCqkynKf8oZPhzI4RN0YupjmjXS0DOV4w_UxHwa80R2F588P4lt52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=U6g34qlg2oy5D9Cw1JEsJrGRRVgmYdR470ArD5erq13B_i6aTAt0ZO6NN2J7u3fn1YSBeaaiYF8n7SMNIBtA8ErYYdbFYjYcyig-wGsZyzoG-Ba15DhRPA5zNAHjfQyu-5_462HBwGTqxAogA_1aiFhFu7Nuc7Ik8pIW3aDdVFL99akAMpnXDL_UlamLDyRN84srm-65xFc3EvXd35O-PFRjAONDaNWoBdpJGF8VZBkVD9iJOrGL-rgeMD5RFglQFY9a_3_vJrTtHmBuPu1aYpaGtizV-KydvCqkynKf8oZPhzI4RN0YupjmjXS0DOV4w_UxHwa80R2F588P4lt52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل وقوع آتش‌سوزی در فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148207" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
هیمتی: چرخ اقتصاد کشور فعال شده و اوضاع درحال تثبیت شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148206" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUMclqIJ_PiN0m-2XoSEKnVK9wiCYjgHlgnWdFGmGbKLdApb0SMQOmtb59H3F8k8gvMITY0fpuO9yChEbE50jWej7aQdKiBUPMr-qYEYbGhbjgxBx1_x3M5zJ5kP4QgeD4cAp8Boz_Yk32DIULOPnlwrhWgb2wceP894Wv4QzITqasW8OuGkvYKIkJDYQ8M1ZwetOfXLRPcr54JfFI6ExGV2OAUt8GDfSXLCyh1Nlt4f0uITVueJ0lgvj-3gw9X_8TyzPZLCse9uc_U239W4OXzJvM73KlkfToxpJ0XDRb9qlv5CKGli_K4-x1IQ04jl6YPBXz64cUSorf_8smh4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاسبی جدید با نوبت گیری دکتر: ۲۳۰ هزار تومان بده وقت بگیریم!
🔴
نوبت‌گیری پزشک و دندان‌پزشک حالا برای برخی افراد به یک منبع درآمد تبدیل شده است. برخی بابت این خدمات بین ۵۰ تا ۲۳۰ هزار تومان دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148205" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=imv0JY1MPyY0jL7DGyAoBAsOXmYg4naNHs1vDD3HN_G4sxgkL00TutADVi2hTJQzMc0BBkr4yLHfZXZmNrhnjsmScifgxETiFrRdd8iPjO9cFk0QzfWdIThNEPwr7O5v03i_2bOTX1N0VUP8tpkyoEQyyl3Ybs5o-kVM-mr3PJloX4Mw7cz5HK7sqHt79lsNGUyP2jDOoCHqZCgj5RKvbvQ1vXV0NFj1M0yGvB0rkQCmh9cG_L1fIoYJ8IeM7Xo79qtGZy1X8ZW_d_NmV9myWxbXdDfBk8ho_SYfG3eykH8tZxZ5wjp2pjUx99uxx3BqVCWJEPm54XyiH2bhZ5iUQXXjIqKPUIck7MxcB29W_m8brK9tU9SGX1rVFehG62qfQoe3akF-ikgDP7lALsh-ARsg4_QfoBNfTtQzWXgPCRT3GriYefmGJCllvK9t7TllCxMWHZks3cczgjjKYERIOrlAOSVoG510SyjDLp5C4lLvXycokE3_XfE9Kg0fo_OpEnY_If0KekyrKzjS3g8ymwgLNEFEBXEzTx6hhEbNt3W3AHy6aTCdX2p6Znd1GxLVtC9E15q6guKz6mphSk7mY0EngNDfxrkda93ACCkbLLzXE5MdXEq2SGQFfnAxoI2Qi0msrGso2iGwoX4pa5vDRAzxobsJnxNMztWCKjFofa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=imv0JY1MPyY0jL7DGyAoBAsOXmYg4naNHs1vDD3HN_G4sxgkL00TutADVi2hTJQzMc0BBkr4yLHfZXZmNrhnjsmScifgxETiFrRdd8iPjO9cFk0QzfWdIThNEPwr7O5v03i_2bOTX1N0VUP8tpkyoEQyyl3Ybs5o-kVM-mr3PJloX4Mw7cz5HK7sqHt79lsNGUyP2jDOoCHqZCgj5RKvbvQ1vXV0NFj1M0yGvB0rkQCmh9cG_L1fIoYJ8IeM7Xo79qtGZy1X8ZW_d_NmV9myWxbXdDfBk8ho_SYfG3eykH8tZxZ5wjp2pjUx99uxx3BqVCWJEPm54XyiH2bhZ5iUQXXjIqKPUIck7MxcB29W_m8brK9tU9SGX1rVFehG62qfQoe3akF-ikgDP7lALsh-ARsg4_QfoBNfTtQzWXgPCRT3GriYefmGJCllvK9t7TllCxMWHZks3cczgjjKYERIOrlAOSVoG510SyjDLp5C4lLvXycokE3_XfE9Kg0fo_OpEnY_If0KekyrKzjS3g8ymwgLNEFEBXEzTx6hhEbNt3W3AHy6aTCdX2p6Znd1GxLVtC9E15q6guKz6mphSk7mY0EngNDfxrkda93ACCkbLLzXE5MdXEq2SGQFfnAxoI2Qi0msrGso2iGwoX4pa5vDRAzxobsJnxNMztWCKjFofa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون: به نظرم این استدلال که روسیه به‌نوعی به‌خاطر استقلال اوکراین چیزی را از دست داده، کاملاً اشتباه است. داشتن یک همسایه آزاد و مرفه چه ضرری برای روسیه دارد؟
🔴
اما درباره اینکه چرا این موضوع مشخصاً برای پوتین اهمیت دارد، پاسخی وجود دارد. پوتین می‌خواهد یک الگوی سیاسی خاص را حفظ کند. او دموکراسی نمی‌خواهد و اوکراین آینده‌ای جایگزین را برای روسیه به نمایش می‌گذارد: کشوری آزاد، مطبوعات آزاد، جامعه‌ای کثرت‌گرا و رسانه‌های آزاد.
🔴
او از این متنفر است. مشکل همین است. تهدید علیه ایدئولوژی او، خودِ اوکراین نیست؛ بلکه اوکراینِ آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148204" target="_blank">📅 16:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148203" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148202">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbtPhMtXSeHTlWq-zKxijE9bThN2j0qBjeNPb8UmoN3CyT3jLelW1ovq8txGQhhTCtSvy6ejTZlYtQrOp9dEW-SuO-5MD5kaRQ15PVulMCxmDlEDkE19NtPeiM4cGiryXuMMXagZvf3hLZfYRcfAgAzePcc9ZHX-xJemYWjUEJG12M0WSeyRSuamHHdfMkLLGP4qwKt5b7m4CSIFlLpMOqcC0phiMQcvIbjB40I7z2Dcqo_JUwP-9JicTV-kAek1mdPdAHJXAPB4oSIfZ2Bammw8mEg9wzsMh5FbbSPbdP2jt5Z5bK27sC6_bYl0oiQSCimyw0wnnLHkKiY9JcGuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148202" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148201">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=UcwJYJFAOWLn05gu7YyPvrTUnPFZ10VpUmbKCn1aTEjI2hYVhXh4opy3T2iCnM8oamng2P_paDTO2IJP6PTU7MU43775jfo499K7aWepZJAepEh265E4WTmtMG7d76hzW4YS_vrWEBYTWrKUGzATMVcVhGcsN8Pp7BbzLDcmEM5OOhWIqVWBIqEoUfuRm2lDZwUAjWF1McnxY_EnL-qjtgpMRgHDbdK2e1zhtg081TfCzt3VxLK-A_9eKaH371Tbh465YFWdV0f9Cp90oKcGRPDMpQIwFHwdSgowTcNTsYlKaAjGg_KtNADjcy94Pl4nfCLGmi6LjPNysb74BKT4GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=UcwJYJFAOWLn05gu7YyPvrTUnPFZ10VpUmbKCn1aTEjI2hYVhXh4opy3T2iCnM8oamng2P_paDTO2IJP6PTU7MU43775jfo499K7aWepZJAepEh265E4WTmtMG7d76hzW4YS_vrWEBYTWrKUGzATMVcVhGcsN8Pp7BbzLDcmEM5OOhWIqVWBIqEoUfuRm2lDZwUAjWF1McnxY_EnL-qjtgpMRgHDbdK2e1zhtg081TfCzt3VxLK-A_9eKaH371Tbh465YFWdV0f9Cp90oKcGRPDMpQIwFHwdSgowTcNTsYlKaAjGg_KtNADjcy94Pl4nfCLGmi6LjPNysb74BKT4GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال شدن سامان‌های پدافند هوایی در ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148201" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148200">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCrMGti7UBeR0gGBMUeNHvaOhiC0fM4I0ap8JXvAkv1gGN_86aUVhdwVTo3wlV01a0J8lKn0N0mSPFIWSuf66KxCBceXmqBqO7Y6MIQ46tqifCnOWE8WuciN-d-PAT73vr5GxxTvxUiJbxMrj9yvFBtJEP3FmJ1ZA7O9MXWsLCJ7yXOpHq_SHHD8XT9dyXJo_IdXtW-xD88K25XH9kjdIEgZpMMykyCt0ffEcf3TEAO1bH8z7oSBym7JaQNKuIVQtI0z9eSiDLyGS-ZsDa36Al90271gZRwTNqjFb-xQ0eNOLI3u834Y68_UspcwmjZ8UeerTxmPU73yRYcvWcMwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: شدت بارش باران و برف در مهر و آبان ماه به حدی شدید خواهد بود که در اکثر استانهای کشور احتمال سیل و کولاک وجود داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148200" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e1hG8GTyvS1mVo2cWCLA05I9I1EHLf2EIYu87cExTLtwddmz_7ew06PDwOUVxPxElfmkwgEwlrYmy_VkRJxQpMRJZp0KbtD-kAGmAJol6I3chG9qlhF2OuCHdAKQoZ_G_dyXXx_nkojRKlPtswlMSsPeZswIFmVZjRDllWR79xDw5YHQajOVb-1ED-MG5h7-p8xgd82sVUry4pX_Q2CAAG8koiMFd2h5ZMbtJSlRvm-WsRGP0W8CjA6q3azqBnFQzLsjBTJc7Yk55wOUUl8P65jbO1ZQZKZjQP1GPKHSqnZXoHoOEJb3zuNULkSGE_Ogek0pEmKuiQbGkxGTeYza8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QCGlXs2-sxgm8tEHy5Nk6sQl-vK5BNWrtdgrGeNuJcFwmrQBeVIIfOtzruCFccsZYpdEa8qHGjlx6-nkiijAvYsz97q6YS-CuXr51yfPiQQikhCc0rZkH5ojeSLfLYD76hlDtt7FKs0bO6EbadSERjMF9y4tBqwLa-MrRA55Qf8q2IHpSIH2Uuk0_E8kfUwTaVz7nMqfxPNiFxfM4h5CtnH2TWTwXmHmEOlJxWhP07xeVTSrR55yNr1pGAOq-18mqCxg8DPTFDbYsKL6YYvTvMVQ6fUnDRQQPehbgb-ndfA72STI7at3LSaZAEWMfiHDoi_tuZuqROlN16-nLWNjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S9CEcBhW90AqeXin1Q_idK_l2xOL-qNVpQtrkgzj40ZCib1YLOyQGtvEsA3Gk-ctRBAKmoI3UsHMUScfBzWjTmDLmme1MbecbRMxmlBvy3yRqaBB2SnscYYP4b_7-wQ76NtMKEBc10E1RqMtRP6Z10BOKFqSUdlLyS4j14H7zeylw-SJf9owO50wFsK1OLlHPCDssJM4MAAzJ9PyHjHWrCpfkkPclkKGpmI2tdgPIO5YGo0pBJbSjsqZHZnwCMhEBgIICWrBF6zhV3GWiF1fL_hu7MxdfxX93DBAdM3IH6evtMqGTrn8Cho2WYpLAWzVQfK0wAi1rhbNcCoFuA0Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zvn0vaRPVFBCQ-BWYfX8VY_VGqkKO0OA4cDrliZW1MpyC7e3KybCdalGtKFtBVKY3jYbgB1m7GslgS91CxUPragcw3axUJdY6b8hRNepcrPbAJpyg3FVmk7aE_45uMSizoT2bX1vqkes_NDgV83KmBzWY45yPLMmw4Q9Y8O0DTcZo2RoQAPt1wUd6KTERctKGVr_JEzpU_zk31kGd7JKa_HHx-6JAoysAdvsd2b2csIqjbU5uO36Ld_fIpmUmlU2glTNqeYSZvZ8870ZcOt_-mDPwNPSaoPISS3hbhVjCva_sHBABaefEdRODppxphVrYh_Uk4u7EW5F2p_dno0TlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جزیره فارو اعلام کرده که مهاجر می‌پذیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148196" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=TtLyGLrTC9sfTe_RzS7ctZ8ZQpbjpmau1zuZO7jIyFoRv9vs_sQ9KqrITh3Bwfw-sfn5f4SYKUYUt3oPhsy5Nvr7xmtZ4v538X8Lz7fAgSr8cUM6q1Ld8PeJoHlHY-JdbxoQA7Tx6prXT6Y88a_y-5zmsCS55zWAURrxRhN1yCnh_E8GdqnvEgzJGOc8XaaBORm57L6VCALZaaiMnVFaYXQiHKjVj_w8TTFUk0x-yA8ctSAPSzF58if8hLfNvt4uCAmtVFo71ZqU6_fZr2m-Qv9E2lKTnElh3MZ_ao09yrHqkbeDXcNRYD2LaPsJUjk9GgJLeyYFcaht_KcwU8gciw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=TtLyGLrTC9sfTe_RzS7ctZ8ZQpbjpmau1zuZO7jIyFoRv9vs_sQ9KqrITh3Bwfw-sfn5f4SYKUYUt3oPhsy5Nvr7xmtZ4v538X8Lz7fAgSr8cUM6q1Ld8PeJoHlHY-JdbxoQA7Tx6prXT6Y88a_y-5zmsCS55zWAURrxRhN1yCnh_E8GdqnvEgzJGOc8XaaBORm57L6VCALZaaiMnVFaYXQiHKjVj_w8TTFUk0x-yA8ctSAPSzF58if8hLfNvt4uCAmtVFo71ZqU6_fZr2m-Qv9E2lKTnElh3MZ_ao09yrHqkbeDXcNRYD2LaPsJUjk9GgJLeyYFcaht_KcwU8gciw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قار قار کردن و توهین عده‌ای به پزشکیان در دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148194" target="_blank">📅 15:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پوتین: رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148193" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148192" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148191">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148191" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
