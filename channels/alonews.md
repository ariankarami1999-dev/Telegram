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
<img src="https://cdn4.telesco.pe/file/uY-NJy5aX6_IqawzALUZWRvW8UT_wjYfLj7vF5MtjvImJiXn9QHV1oBolL-j9sGN9TMfeQabH6eUjCUHpfCKA72Avr7eY-V_etHhNwCtn2787CMAzlOo7ltq8Wss_26SnJFXjJJkV_Jk-L1_mD5KOE9jDvWSYxBhtahc15vcW5zwjlIoIQpMdxvog04vRRgQLPuzsk0SKc1tHB-Q-zdjYndrhQR8kBnTwQ_eYlEFF2nE1nywKPpf7wRaWim3sQEYx9cP0Lp0lYYtCHCA__KNi9C2BCV9WzLVJqy70X3RNPKRIw3jk2l8pmQ7XZ8nQkdcNiAlUXDa8ptNF171hM8BDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-138443">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
در جلسه امروز هیئت دولت عباس عراقچی وزیر خارجه، گزارشی از تماس تلفنی وزیر خارجه اوکراین و آخرین وضعیت مذاکرات با عمان ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/138443" target="_blank">📅 16:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138442">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUilM4Wv7wv_s-cQ0vcw2F-G1v3YukqeYiegwU9AZL2evpayDQnlDlC0JPdOM7RQyBaLpV100f6OIWmw3uMafqIhaH_eq7RSFoj-9X94k5S8UUIU2XxtKwa21Of3iPhCIno8HvLnDGkVK7bODOP2YFMdXOT0Jhi2w1413o6QE7bxdPHiyWt8hmmQm9bCYhdQSEU6OxnhNNsn8BLZb5lo2NG30YRdkKRl7FyRBg0G6JrRDu56OWVhSZIzoeYq3VKbgqIJDWRhn5xFjIKNvX6snj6inoqPpqO1dK1i5mRZqGfYSL-FvYR2ANqKkMhYsV5sQo_u-0YvCBXVeQmS0cvJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138442" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138441">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نتانیاهو امروز با وزیر دفاع آمریکا، هگست، دیدار خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/138441" target="_blank">📅 16:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138440">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFmoXMv07MBXA78wSgerIy3nUlvXSkGwzZlQOWERmOE0yGUmZGrVClp-cShtQm5s6iCYuVvn9U_UVJJbsbLvAtePRBSbpy37pLkWLPsjXTip0ljD02OBxgyhZuHvHdLUv6KqARj15R5nBz7LI5sIB7SQtA_B0RPA2Jr58HO1W84S4b5YJhpf4NCztmVl7usjksg4-VUEftV1N93AJ3kZlRHdX3Q7Lu_hY75J-Iq-zfY_A_w2CZaBR0YDaUHexOOf66zuyUn2xcddg-PDvtsYGNro1zCQTQRD0d-TraM32RlvIfCotVBU3t3TPugTqtafm0-5zIq2Dey5W31Yk37g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون جهش قیمت نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138440" target="_blank">📅 16:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138439">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: من در نظر دارم اخطارهای جدی‌تری را علیه نیروهای نیابتی ایرانی مطرح کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138439" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138438">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: شبه‌نظامیان مورد حمایت ایران «سرطان جهان» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/138438" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138437">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ:  فعلاً اجازه می‌دهیم ایران به گفت‌وگو ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/138437" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138436">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=J_TAOVLA1B8m75KU4EgcP3MmfL5HGMknk764zeKIHIUUBx599OtZXapGFlwiBJdV1TGeHJjzoKhjkrmg_EwlDQ8CguMjGjc-jNlzW-nE-E3nbWQ8U3kzVGG1sdljiFe4Xhk1RXftN30O-zv2RWd2ft4VaLtXR2ZGrriJ-gmWX14MUitySgnvgva5Z-EOSp0n-L4Lb0DmcKGUHzS4_1ne1f-rPfl9Z9bvbRlallp1QUugBTb3NBpLXEjvRWTOeQJe9bnDNxly_mcrIQjzgSq6OaUVYtQ4ZF_sHgiZbKoAYtntsaJ1YXeFxzYQAFMrqmz11J_e2iR7nuAyaKBKaqIliQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=J_TAOVLA1B8m75KU4EgcP3MmfL5HGMknk764zeKIHIUUBx599OtZXapGFlwiBJdV1TGeHJjzoKhjkrmg_EwlDQ8CguMjGjc-jNlzW-nE-E3nbWQ8U3kzVGG1sdljiFe4Xhk1RXftN30O-zv2RWd2ft4VaLtXR2ZGrriJ-gmWX14MUitySgnvgva5Z-EOSp0n-L4Lb0DmcKGUHzS4_1ne1f-rPfl9Z9bvbRlallp1QUugBTb3NBpLXEjvRWTOeQJe9bnDNxly_mcrIQjzgSq6OaUVYtQ4ZF_sHgiZbKoAYtntsaJ1YXeFxzYQAFMrqmz11J_e2iR7nuAyaKBKaqIliQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حمله اخیر ایران به اردن: این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را سرنگون کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138436" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27adb3179e.mp4?token=mG0_BQraJGu0VmMafOk6bZh_hOG53VaYyIEkwDN78U5dmJgdA0yZyvJWYu5dBVIXsHGyPJQG5k0N9WUpPit4w26md8_2j2scJFNpRNngpvsEk3URm0ahZe-BqxI6K0sQxpyGpIvdO1ZGXI3EWsJ4YudhSzgewBjuZQt_dzH1vSWOX1clT_pbFd8-FUfSWPOmC35vI1UeeF_wgh30EOLWi9z72ARvz9kpk-IbzbVlzniYhP8ChWjg5BBsJep8pU_9S1Urjss9mKhXBIE94aiztcT2bMh8JSJPk-YbKMVz6PUI_o1pVUSRjtfhVnZn5xhU8qtEbBapciLG7jP7wywSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27adb3179e.mp4?token=mG0_BQraJGu0VmMafOk6bZh_hOG53VaYyIEkwDN78U5dmJgdA0yZyvJWYu5dBVIXsHGyPJQG5k0N9WUpPit4w26md8_2j2scJFNpRNngpvsEk3URm0ahZe-BqxI6K0sQxpyGpIvdO1ZGXI3EWsJ4YudhSzgewBjuZQt_dzH1vSWOX1clT_pbFd8-FUfSWPOmC35vI1UeeF_wgh30EOLWi9z72ARvz9kpk-IbzbVlzniYhP8ChWjg5BBsJep8pU_9S1Urjss9mKhXBIE94aiztcT2bMh8JSJPk-YbKMVz6PUI_o1pVUSRjtfhVnZn5xhU8qtEbBapciLG7jP7wywSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما قرار است حسابی لجنشان را دربیاوریم.
🔴
آنها را به شدت خواهیم زد — کتک سختی میخورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/138435" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ در مورد حمله ایران به اردن:
حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
🔴
حملات دیشب به نیابتی های ایران در عراق، با هماهنگی با حکومت عراق انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/138434" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری/ترامپ: ضربه سختی به ایران خواهیم زد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138433" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس جمهور اوکراین مدعی شد پوتین قصد دارد 500 هزار سرباز دیگر را بسیج و به اوکراین بفرستند همچنین 30 هزار نیرو از کره شمالی و تعدادی موشک بالستیک از کره شمالی و ایران(؟) دریافت کند،لازم به ذکر است زلنسکی به ترامپ در مورد رهگیری پهپاد‌های انتحاری ایرانی پیشنهاد ویژه‌ای در ازای دریافت کمک‌های نظامی داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138432" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
عارف: وزیر و مدیری که اختلاف را به جامعه بکشاند عزل می‌شود؛ تعارف نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138431" target="_blank">📅 15:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دریادار سیاری: بدون اجازه ایران هیچ تحرکی در تنگه هرمز انجام نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/138430" target="_blank">📅 15:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
آمیت سگال : نتانیاهو دیدار خود در کاخ سفید را، به گفته خودش، «عالی» توصیف کرد و گفت: «این یکی از بهترین دیدارهایی بود که تاکنون داشته‌ایم.» کاخ سفید اما با لحنی محتاطانه‌تر، تنها اعلام کرد که گفت‌وگوها «مثبت و سازنده» بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/138429" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138428">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آکسیوس گزارش داد شرکت لاکهید مارتین از موشک رهگیر جدید PAC-3 ACE رونمایی کرده است؛ محصولی که با هدف پاسخ به افزایش تقاضا برای سامانه‌های پدافند هوایی، کاهش هزینه تولید و مقابله با تهدیداتی مانند پهپادها، موشک‌های کروز و موشک‌های بالستیک توسعه یافته است.
🔴
بر اساس این گزارش، هزینه هر فروند PAC-3 ACE حدود ۲ میلیون دلار و کمتر از نصف مدل فعلی PAC-3 MSE برآورد می‌شود. این موشک که قابلیت استفاده در پرتابگرهای فعلی پاتریوت را دارد، نخستین پرواز خود را در سال ۲۰۲۸ انجام خواهد داد. آکسیوس همچنین از تلاش پنتاگون و صنایع دفاعی آمریکا برای توسعه سامانه‌های پدافندی ارزان‌تر، از جمله پهپادکش‌های کم‌هزینه، به‌منظور افزایش ظرفیت تولید و کاهش هزینه‌های دفاعی خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138428" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138427">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
به گزارش العربیه به نقل از یک منبع ناشناس در ارتش اسرائیل، فرماندهی مرکزی ارتش آمریکا (CENTCOM) پس از آنکه یسرائیل کاتس، وزیر دفاع اسرائیل، به‌صورت علنی اعلام کرد که هواپیماهای آمریکایی مستقر در پایگاه‌هایی در اسرائیل طی هفته‌های اخیر در حملات علیه ایران…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138427" target="_blank">📅 15:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138426">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
به گزارش العربیه به نقل از یک منبع ناشناس در ارتش اسرائیل، فرماندهی مرکزی ارتش آمریکا (CENTCOM) پس از آنکه یسرائیل کاتس، وزیر دفاع اسرائیل، به‌صورت علنی اعلام کرد که هواپیماهای آمریکایی مستقر در پایگاه‌هایی در اسرائیل طی هفته‌های اخیر در حملات علیه ایران مشارکت داشته‌اند، ابراز نارضایتی کرد.
🔴
این اظهارات جزئیات حساس عملیاتی را فاش کرد و در پی آن، سپهبد ایال زمیر، رئیس ستاد کل ارتش اسرائیل، از دریادار برد کوپر، فرمانده سنتکام، عذرخواهی کرد. همچنین اسرائیل پس از این اتفاق، سطح آماده‌باش خود را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138426" target="_blank">📅 15:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNsWZaeJaRF8dk6Kh77kon7R0Qi5SymG651i93dtsKtMc4vRqt4_cGmVK0u-J6beDgBhcyK9Xr2VwZuMZCYMAPle3lMa5SWuPFi1Six7hfA_HgcBlPCPqJMK3ettYzXmU8QKAKm0AhLO1C_e-o8wdEjR-SjiZlS322eaM6vWtekcGpPfLZdCJdleIXvcD67ouJaP6vv2XHk5Z4FwZktfz0AcSfSepJZzA_tjX0Jx2be70EDGc51vTb8wTIKPmXydukvROYr9gRdn1rKor2M1xQo4KK-_99vQ3K2pzuZykHJMdhBmZRp1AP4sGYebm7cM9VCpL7Orsk65sUkIQGiE2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسپانیا با پخش اذان از مساجد در برخی از مناطق این کشور موافقت کرد.
🔴
دولت سانچز، یکی از چپ ترین دولت های اروپایی حال حاضر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/138425" target="_blank">📅 15:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
چین: تفاهم‌نامه ایران و آمریکا که نتیجه ارزشمند میانجیگری و تلاش‌های چندین طرف است نباید از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/138424" target="_blank">📅 15:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عراقچی: اوکراین باید مسئولیت حمله جنایتکارانه به کشتی تجاری ایرانی را بپذیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/138423" target="_blank">📅 15:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138422">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الجزیره: تعداد کشته و مجروح های حشدالشعبی تو حملات دیشب آمریکا و عربستان به 50نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138422" target="_blank">📅 15:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138421">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شین بت : یک شهروند اسرائیلی به اتهام جاسوسی برای ایران بازداشت و متهم شده؛
اون قبلاً تو یک یگان نظامی محرمانه خدمت کرده و متهمه اطلاعاتی برای کمک به دشمن منتقل کرده
🔴
همچنین از اون خواسته شده یک سرباز اسرائیلی دیگه رو برای ارتباط با اطلاعات ایران جذب کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138421" target="_blank">📅 14:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138420">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008da4110.mp4?token=qNq0ED3a35Wjh0AZaiTWhMVKLOF1L2eWmP5ymWViOR1CkAg0dHgPk9PhlexLld7sJQEFv09pbRjJj5u8irVIcNRU7Scw2AiCHT5gquUXlUQRYYsrbeQGGDOj__T4mm5uyanLPN-O5RKjzaSqVGRIYaW2t8TizpBSvRJALUmO82FHKT9ZJ5qaDrlURcsQqcIKE-oV-XEKdMByBfEPmm41MfldDbwsSahL7j-50RCZ_n56PifSyd9_TJkNKu2K_d-ZEev1bXWmV-sNolmuaxOgm4XCcWh6UI9ZCuQWD39rtHvVoCsC_JGo0t7zaNFchXc8iWMSARHpQ4TseYUTgDoe7JuzD2ruK5WDaPFxPb4DUzuGDo9X3vZg0MjRjCbKPnjElMnQeDSUFuT_-9dSns4-9axJUvzTQ__dU9jZ_2eeNY5Bz7r5nNlIypN0Pnjr5E3pAQk2Fu5Zoi3O-CmJkPM8y03SPM38tNF_3r15zrKp5sPzrloYIhjdMWBwelzlKnHvcHs6-XTJQW5mt6pDLYM8-36Mf50UUxIXmfnt_bvxRwr6BfSEN4Lx0pPd_5crLeeznhJShPG6OfIjpYLtynXQZ1_2yP8vi8DZ8LeRdFBg01YPSu8Y0tMBAqrA785nMPLw5kqyStJ4815VpP6XOpooIcjHiESeSZE9SW9NZs5kR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008da4110.mp4?token=qNq0ED3a35Wjh0AZaiTWhMVKLOF1L2eWmP5ymWViOR1CkAg0dHgPk9PhlexLld7sJQEFv09pbRjJj5u8irVIcNRU7Scw2AiCHT5gquUXlUQRYYsrbeQGGDOj__T4mm5uyanLPN-O5RKjzaSqVGRIYaW2t8TizpBSvRJALUmO82FHKT9ZJ5qaDrlURcsQqcIKE-oV-XEKdMByBfEPmm41MfldDbwsSahL7j-50RCZ_n56PifSyd9_TJkNKu2K_d-ZEev1bXWmV-sNolmuaxOgm4XCcWh6UI9ZCuQWD39rtHvVoCsC_JGo0t7zaNFchXc8iWMSARHpQ4TseYUTgDoe7JuzD2ruK5WDaPFxPb4DUzuGDo9X3vZg0MjRjCbKPnjElMnQeDSUFuT_-9dSns4-9axJUvzTQ__dU9jZ_2eeNY5Bz7r5nNlIypN0Pnjr5E3pAQk2Fu5Zoi3O-CmJkPM8y03SPM38tNF_3r15zrKp5sPzrloYIhjdMWBwelzlKnHvcHs6-XTJQW5mt6pDLYM8-36Mf50UUxIXmfnt_bvxRwr6BfSEN4Lx0pPd_5crLeeznhJShPG6OfIjpYLtynXQZ1_2yP8vi8DZ8LeRdFBg01YPSu8Y0tMBAqrA785nMPLw5kqyStJ4815VpP6XOpooIcjHiESeSZE9SW9NZs5kR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آتشفشان کیلاویا در هاوایی
🔴
تصاویر منتشر شده لحظه فوران دوباره آتشفشان کیلاویا در هاوایی را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138420" target="_blank">📅 14:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138419">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: تنگه هرمز رو یجوری بستیم که دیگه از این بسته تر نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138419" target="_blank">📅 14:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138418">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf55992ebb.mp4?token=ntU9TRSiM_Yk6pWqxjG-_ZNsDnjtn-jitYODAqjCHU0ThpK9C7s0ySAXe8OXu1wJrsptYEwbtliJYxpKTZF5-CR9rWoyDZVRZvTMO9mz2WRJfJ98BS_pDqo7EersJOPtAM9GkYDCs5OEmsNc8t-NWiAZ8KwQyEbDc8Bvj_g-mlJ0KclHMvGwyoedS1XcuFEGqlWTCrFo6qpEJwxOxo9vRBVMM6Mc7dvetsh58IHY0ii7Zwbn5uzljo8KR6hjKXxMz-eeAhyejOU5Gxtqh_9kEBgGKwmObxM2jpIvWsWqwrxE4HvWGMiA3TnW3gWgWtkykl4PeEE67Yy_PvcT7FjPt0ZDCkutRDeHZxvpAlVx-a1hYtmEv6731HIGCZgD9pk4fs29Jrc2F6FlVg9t1WPerQORbwNVhKwO9yVbKZLx3XPbfp8wHyieGK4fp-JL4G8mtBDeQz6kJD5bvGLbTVqz_MuRcnW0MgAN4-1Xe7WH5NABL8tI9BHnU9caZJFHJLoDke1oRRZP2CFOMQdwYzA2vkfeUt_MQ0tIr9XH3OlZAuBISMXNxYZGBUBVwaUNV2zJHMd2pNYWlRCwAvS9Z__eA4pV2CwZR48oaQCG2q3hn3TCRVKwrrHJghDtnV672ev1nHNDp2uNXjmTsusA5oKCLN5sWaLhHpn-e19LTl-tZ98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf55992ebb.mp4?token=ntU9TRSiM_Yk6pWqxjG-_ZNsDnjtn-jitYODAqjCHU0ThpK9C7s0ySAXe8OXu1wJrsptYEwbtliJYxpKTZF5-CR9rWoyDZVRZvTMO9mz2WRJfJ98BS_pDqo7EersJOPtAM9GkYDCs5OEmsNc8t-NWiAZ8KwQyEbDc8Bvj_g-mlJ0KclHMvGwyoedS1XcuFEGqlWTCrFo6qpEJwxOxo9vRBVMM6Mc7dvetsh58IHY0ii7Zwbn5uzljo8KR6hjKXxMz-eeAhyejOU5Gxtqh_9kEBgGKwmObxM2jpIvWsWqwrxE4HvWGMiA3TnW3gWgWtkykl4PeEE67Yy_PvcT7FjPt0ZDCkutRDeHZxvpAlVx-a1hYtmEv6731HIGCZgD9pk4fs29Jrc2F6FlVg9t1WPerQORbwNVhKwO9yVbKZLx3XPbfp8wHyieGK4fp-JL4G8mtBDeQz6kJD5bvGLbTVqz_MuRcnW0MgAN4-1Xe7WH5NABL8tI9BHnU9caZJFHJLoDke1oRRZP2CFOMQdwYzA2vkfeUt_MQ0tIr9XH3OlZAuBISMXNxYZGBUBVwaUNV2zJHMd2pNYWlRCwAvS9Z__eA4pV2CwZR48oaQCG2q3hn3TCRVKwrrHJghDtnV672ev1nHNDp2uNXjmTsusA5oKCLN5sWaLhHpn-e19LTl-tZ98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حشد شعبی عراق تصاویری از پیامدهای حملات هوایی آمریکا و عربستان به مواضع خود را منتشر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138418" target="_blank">📅 14:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یک خودرو مهندسی D-9 مورد اصابت کواد FPV حزب‌الله قرار گرفته است
🔴
این اولین حمله به نیرو‌های اسرائیلی از زمان آغاز آتش‌بس میان دولت اسرائیل و لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138417" target="_blank">📅 14:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfzZISBHE-1fPO6mvtDPl4bF1OdBk17ElK4E4GkqQYZ2UXE1YvNLr2VOrJqtzuckoH1bpc41qx82ggnlcJSPliFysTAARmm-EdlWUMbiBPGCQ-HoRe7ou4NxofBUhxJFcVirk2zZHcEWvsaqPv6pReIA6G1ScgIqjVGyYbqjdwxUaSs50978EzTuRCSEGaz9sPoJRrzKHac4KbiB3qAzAAsJ4FbLzrQnWwkgCxwzPMS2-zLEhOpnbsxg0KTXBZj5I2C5VTukUGSbuqbRwo0rVOERzibzgrI1gEgTuZy-wgnxKHSRgycdbW4KSDtprEFeaFkdDcH3jdGkC5cLwrngBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران حملات آمریکا و عربستان علیه عراق  محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/138416" target="_blank">📅 14:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نشریه پولیتیکو گزارش داد که هم پیمانان اروپایی آمریکا از حمایت از طرح این کشور برای گشت مشترک در تنگه هرمز سر باز زده و اعلام کرده اند که باید آتش بس دائمی با ایران محقق شود تا وارد چنین طرح هایی شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138415" target="_blank">📅 14:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245226179d.mp4?token=nCwhbWBuKyRHgqCEJSjkQvHvcPVtU9J74QHc_CTS-1Ne0fMPzXgJAxEI1qvOMMJ9MrxJz_zTae3Z_NkyF9e2KuiV1AoJQO8PnW8cDZ_DjezwKivJN35s71K4ICXXNOTHDtrI1uN4bgQeWRyk4m5jjBZx4y4gETtG4zXtQpftS11MNDGYLNPL7Q85uk8p1cPABSqTGy0hsoVMUPzjsqFv2KSUwxlO4pcHm9RJBYJVsqG_a-how8gWwN24MbMaHAdROKQQzoRKQJXy3b-vNDCzJazAQlBkg53XiRc9vj8JP9M6c5FyYZCxDhzzjawTA78v6rvqNRZAAFyQBAit6onuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245226179d.mp4?token=nCwhbWBuKyRHgqCEJSjkQvHvcPVtU9J74QHc_CTS-1Ne0fMPzXgJAxEI1qvOMMJ9MrxJz_zTae3Z_NkyF9e2KuiV1AoJQO8PnW8cDZ_DjezwKivJN35s71K4ICXXNOTHDtrI1uN4bgQeWRyk4m5jjBZx4y4gETtG4zXtQpftS11MNDGYLNPL7Q85uk8p1cPABSqTGy0hsoVMUPzjsqFv2KSUwxlO4pcHm9RJBYJVsqG_a-how8gWwN24MbMaHAdROKQQzoRKQJXy3b-vNDCzJazAQlBkg53XiRc9vj8JP9M6c5FyYZCxDhzzjawTA78v6rvqNRZAAFyQBAit6onuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چُرت زدن ترامپ در مراسم خاکسپاری گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138414" target="_blank">📅 14:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رویترز: ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138413" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyxjOn-_9fRy440YGJ9S8RGiwNz7cqgehPg6dnEpgGHs-_kUVBAcrM-Sy-cWP8xz_RDZpXVAshO_ws9zbt3PiX8ujDr1vF4CQvRC3ij50ZhDqV160YlmSn8zbTRIiQG8uuqH428hSnANLu2MMW-S_Pk9Xi9aCEADZ-DOb2S5XPojhtNv66i3HYyvKAY8pRcVc0aW7VNCavX9suJivCHq7hfKkAynqh-I1RhC3vEb1iSyddGyQx6yEBI5yUhcm9QZbDRmcAUShbfzSJENqXwE34VX1rHW3G8qPKixvz9tKAAkme0qWctLdLLyuz9QK7sBTmbzd6P5H8SfTG73SiI3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده، حوادث متعددی از جراحات جمعی را که پیش از این فاش نشده بودند، گزارش داد. این حوادث شامل ۷۰ مورد جراحت در ۱۸ مارس و ۲۹ مورد جراحت در ۳ مارس بود. در میان مجروحان، دو ژنرال به نام‌های کلینت بارنز (سرهنگ) و براد هنسون (ژنرال) بودند که در جریان حمله پهپادها به بندر الشعبه در کویت در تاریخ ۱ مارس، دچار جراحات سر شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/138412" target="_blank">📅 14:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه
روسیه :
روسیه مورد لطف خداست
🔴
وقتی شرایط واقعاً سخت می‌شه، کمک از بالا بالاها می‌رسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/138411" target="_blank">📅 14:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دقایقی پیش، زمین‌لرزه‌ای به بزرگی ۳.۹ ریشتر حوالی سرگز احمدی شهرستان حاجی‌آباد را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138410" target="_blank">📅 14:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران آذربایجان‌غربی:‌ یک پرتابه به یک منطقهٔ خالی از ابنیه و سکنه در استان برخورد کرده هیچ تلفات جانی نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138409" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز: یمن در حال بررسی امکان وضع عوارض در تنگه باب‌المندب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138408" target="_blank">📅 13:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / بنا به گزارشات دریافتی، دقایقی پیش نقاطی در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/138407" target="_blank">📅 13:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اکسیوس به نقل از زلنسکی :  رابطه‌ام با ترامپ خیلی بهتر شده
🔴
الان رابطه‌مون سازنده‌تره و مثل قبل دیگه این‌قدر احساسی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138406" target="_blank">📅 13:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d865add6d.mp4?token=u1Vov9bObfpvsfh5NWUHP2OYbwtIdxDUMRsJUIwlLiH5u7wUecyC4pG2Rg7R9DFdJZrXZXFrFZ-E6OawRE9pOW1peS5CX2PN5Pt2SXNBeQBm8oDuUGE4nflfLgt0hcmOqIkTLNDsopTR8WfwomY58iFuV9aW_ADz-pDLNbdqCus8CvNr6C_w6XwCOYobqfh_swlCpHoNj7T3sF1fyu1r0UNazHTnDZ7H2BbEWlJae9jyLxH6aUyr_VZkZ8w9ERXlaFRvFPLZPD_XpBC_eLNisrMRAzVF0TPKbxCgN_bjF8FN3R9q-xBI0lTcvXBn1DGhNSzNlbcLR0R_9SZ16O5zYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d865add6d.mp4?token=u1Vov9bObfpvsfh5NWUHP2OYbwtIdxDUMRsJUIwlLiH5u7wUecyC4pG2Rg7R9DFdJZrXZXFrFZ-E6OawRE9pOW1peS5CX2PN5Pt2SXNBeQBm8oDuUGE4nflfLgt0hcmOqIkTLNDsopTR8WfwomY58iFuV9aW_ADz-pDLNbdqCus8CvNr6C_w6XwCOYobqfh_swlCpHoNj7T3sF1fyu1r0UNazHTnDZ7H2BbEWlJae9jyLxH6aUyr_VZkZ8w9ERXlaFRvFPLZPD_XpBC_eLNisrMRAzVF0TPKbxCgN_bjF8FN3R9q-xBI0lTcvXBn1DGhNSzNlbcLR0R_9SZ16O5zYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع چندین انفجار شدید در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138405" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وقوع چندین انفجار شدید در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138404" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گزارش انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138403" target="_blank">📅 13:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138402" target="_blank">📅 13:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrWP1pwfWKh8f6tpQfaGJ17ls1lgVBQviCub09Lj9OVbb-bQ8FraPeaFtE7ea0mEulayRoot4IFDIGoIhSgHQJ14jALich7dI0WlSGOpE_XSCIObW7z-663voxAM7PNHeuEXE1RrVM5S8E8IiJD84r03EVCXKKomxD5gOF2fZjD9RiBfU4SXIG3iAGn1Q4qVpGuSXKczQtpsdJaxN5L3gFYX3rTeMoioLwL-SdTC1_SxLMMZ51p6EgjM_ThXgsE7PPLtASiwyjLBa6qdSupGTwEeoGhQOnVNk5g4m1WHryGKhxZ-_T4oZ9pRptIqgwfnRDQoFJXPXrJhGgQyGhMtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۷۵ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138401" target="_blank">📅 13:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag2Q6t9FXiHMEXIftmx9QsljX0c4AdvvQi_fzTE_pyTjpqITDN9N745Q6mhXDU5QOfmNwATlRqsjhVTZzdQpfslSFnwDBJoP_CHFR0-7NgiTji0DisMw8nCK_P7P-PhFtqeNGO2vKFKB2CyCQiNtjX_4gfhgtB0H2TYIOS7j4vHg0SQGRNBSOc-nEq8O_3tEBFnG0gA62qBOjCjTewdqrGpzey1HdnOg0s2fKfFQiWq6KbPMGqn8E5kHG3OXXaDTedtz7UBu8hbfPDncoizk_sikNvD4jGJ1eUMwRUeJfQiJArHcnxq4jsTF3Y_BFr61c7UJ4qj82HJVB5YcEnN0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک کشتی باری که پرچم پاناما را به اهتزاز درآورده و نام آن "جدة اسپرینگ" است، حدود چهار ساعت پیش در مسیر تنگه هرمز شناسایی شد. این کشتی پیام سیستم موقعیت‌یابی خودکار (AIS) را با عنوان "بدون خدمه سعودی و نگهبان" ارسال می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138400" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سلیمی، عضو هیئت‌رئیسه مجلس :
ترامپ و نتانیاهو دنبال کُشتن «رواجب‌القَتل» و «مهدورالدم» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138399" target="_blank">📅 12:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دلار هم اکنون 193,400 تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138398" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
خبرگزاری ژاپنی:
چند کشتی مرتبط با ژاپن که در خلیج فارس حضور داشتند، از مسیر مورد تأیید ایران از تنگه هرمز عبور کرده و از خلیج فارس خارج شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138397" target="_blank">📅 12:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پس از درگیری های دیشب خاورمیانه، یمن حمایت خودشو از عراق اعلام کرد و کشور های عربی حاشیه خلیج فارس در یک بیانیه دسته جمعی از عربستان حمایت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138396" target="_blank">📅 12:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نرخ بیکاری ۹.۱ درصد اعلام شد
نرخ بیکاری افراد ۱۵ سال به بالا تو بهار امسال ۹.۱ درصد بوده؛ یعنی نسبت به بهار پارسال ۱.۸ درصد بیشتر شده
🔴
بخش خدمات با ۵۳.۸ درصد همچنان بیشترین سهم اشتغال رو داشته
🔴
همچنین تعداد افراد غیرفعال اقتصادی (مثل دانش‌آموز، دانشجو، خانه‌دار و بازنشسته‌ها)
🔴
به ۳۹ میلیون و ۵۳۵ هزار نفر رسیده که حدود ۷۹۶ هزار نفر بیشتر از سال قبل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138395" target="_blank">📅 12:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۵ میلیون و ۷۵ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138394" target="_blank">📅 12:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138393">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ادامه آتش‌سوزی در بخش ایرانی هورالعظیم؛ حریق به دایک مرزی رسید
🔴
محیط زیست: احتمالا علت این آتش‌سوزی عامل انسانی بوده
🔴
مدیرکل حفاظت محیط زیست خوزستان از تداوم آتش‌سوزی در بخش ایرانی تالاب هورالعظیم خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138393" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138392">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شرکت منابع آب ایران: شرایط آبی کشور در وضعیت نرمال قرار دارد، ولی بارندگی در ۱۲ استان پایین‌تر از حد میانگین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138392" target="_blank">📅 12:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138391">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏
👈
فروریختن یک مرکز خرید بزرگ در ژاپن در پی وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138391" target="_blank">📅 12:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138390">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOxKDIFXxSYrusa6d_rdtVP9a_SB9yrA_eBV1eoqqqkzqF1jvAc1kprf5iAnDpioORotMCR-LGinfKJNjp0tVXG3E1qqvQDgOmLg6HlSHrou4zA1iV8Zcji5n6XPOomjUjBX9-ttKuBXl6dep00ggX-iHuJUnN4m85RO02DZ_QCzVacoUb0w1QGiO_Bpz4FDIPiaJJUnsH-fDkk1K16uPc-Nn6xx0oD54O5mKuxg7XvQlOsHSg40HaxL4IdpVfZyALhs4Jfv9FKGiIBlCI6My5whDU1bYORD1qKERLc3cL0eOOJhw1MGlOOiNfokpgxifQXV-vm8d0lSwykfzQQklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانشگاه های ایران از رتبه بندی تایمز، یکی از معتبر ترین رتبه بندی های دانشگاه های دنیا، حذف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138390" target="_blank">📅 12:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138389">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / مجلس سنا آمریکا با 86 رای موافق در مقابل 12 رای مخالف لایحه تحریم‌های دو حزبی روسیه و ایران را که توسط سناتور لیندسی گراهام مطرح شده بود را تصویب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138389" target="_blank">📅 12:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
زلنسکی : این طرح ابتکاری دست پوتین نیست
🔴
این مهم‌ترین تغییریه که از اول کار تا الان اتفاق افتاده
🔴
ما باید توی فناوری‌های نظامی از پوتین جلوتر باشیم، چون پوتین نیروی انسانی بیشتری از ما داره
🔴
باید با استفاده از فناوری، از مردممون محافظت کنیم و کمبود نیروی انسانی رو جبران کنیم
🔴
این دقیقاً همون کاریه که داریم انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138388" target="_blank">📅 12:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f025f0d044.mp4?token=SMAbUIZ1uGGPyyqLhu0vU0rVOuWzfyFUwZ5HBRRGDPMiHN096VKcdjwXWPuDCK7lVe70M4ymABkWX74Zq--If-v0i0zS79-GQ3jt2kq7aQJ1RHdyjxAmH2rbI-OmEgUoj5YB65g9EvI7mkl9sqH2KTxq_rRrZQNnnPrw-AEGuRKCW2otVI0s3ogircEgLOlH73vyu9mA6lBI2-0urAvlG5lvw99o5z0At7ZrzGuae4k6n5FppL1Rk7PuEuf1wYAdvMK7j-PPFREVbZA471191WQa1bm2gJqYYPIfcteoCfmlyhzZX1yfVGOmJtUHe5SVGneqD2HkuiUnWF1PdeQ8kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f025f0d044.mp4?token=SMAbUIZ1uGGPyyqLhu0vU0rVOuWzfyFUwZ5HBRRGDPMiHN096VKcdjwXWPuDCK7lVe70M4ymABkWX74Zq--If-v0i0zS79-GQ3jt2kq7aQJ1RHdyjxAmH2rbI-OmEgUoj5YB65g9EvI7mkl9sqH2KTxq_rRrZQNnnPrw-AEGuRKCW2otVI0s3ogircEgLOlH73vyu9mA6lBI2-0urAvlG5lvw99o5z0At7ZrzGuae4k6n5FppL1Rk7PuEuf1wYAdvMK7j-PPFREVbZA471191WQa1bm2gJqYYPIfcteoCfmlyhzZX1yfVGOmJtUHe5SVGneqD2HkuiUnWF1PdeQ8kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که پایگاه هوایی علی‌السالم در کویت، از تاریخ 23 جولای، مورد اصابت مستقیم قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138387" target="_blank">📅 12:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
الجزیره: قیمت نفت در معاملات اولیه امروز به دلیل تشدید تنش های نظامی در خاورمیانه بیش از ۳ دلار در هر بشکه افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138386" target="_blank">📅 11:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">علائم مصرف هر نوع مواد مخدر ، آخری از همه خطرناک تره!
هروئین: چرت زدن.
شیشه: انرژیش بالاست.
ترامادول: زود عصبی میشه.
تریاک: مدام خمیازه میکشه.
شیره: بی‌حال و خواب‌آلوده.
گل: پرش افکار داره.
متادون: کسل و بی‌انگیزه‌ست
ایران: مرگ با درد شدید از ناحیه مقعد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138385" target="_blank">📅 11:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک منبع دولتی عراق به تلویزیون العربی قطر: سفر الزیدی به عربستان لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138384" target="_blank">📅 11:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✨
⭐️
پیشنهاد ویژه برای مجموعه‌های مختلف
🔒
۲ جایگاه قفل ربات الونیوز برای هفته آینده خالی هست
🔼
میزان جذب شما حدود 30هزار ممبر
🔼
💵
هفتگی ۲۵۰دلار
✏️
شیوه کار: مجموعه شما قفل ربات الو میشود و ممبرهای آنلاین به مجموعه شما هدایت میشوند
◀️
سفارش دایرکت</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138381" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل شده در شهرستان سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138380" target="_blank">📅 11:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138379">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دستور نخست وزیر عراق برای تشکیل جلسه اضطراری در پی حملات مشترک عربستان و آمریکا علیه الحشد الشعبی
🔴
در پی حملات مشترک عربستان و آمریکا علیه الحشد الشعبی، نخست وزیر عراق دستور نشست اضطراری برای بررسی تحولات امنیتی این کشور را داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138379" target="_blank">📅 11:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138378">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDgXaChJJWkiBiXbBknbvfNWzPTiZt39OZUQiqD7YFUQMSJM2-7M-YvI5zhjEL4kB6ljDw9OIhOQc2Y3JsuwxwFrSa3uU3LqUfaInjrK6KEJTu75m6V4hNXZT_2sbwac5iuMO-0S9rUoUfVySKAtGgFDfurD_13zr4fZ8djxYzdLujbtjLwAAQ5DBWN50-v5O8L1m6DQTbEcpj4Bf6dAA7i9kKhwIYTUIMy_gaKcrVIgIe3Ml5DqmmgM3bNhNVCRJn4CYXWhFqYOGD81Qva6m347cGiI3TLcwf7NJfQmQVoS3gHmnBvbGQ6-2RaCHY87dyIvCNfDcf8Mv-j2zWpJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان امنیت فدرال روسیه؛ دوروف، بنیانگذار (تلگرام)، تو فهرست افراد تحت تعقیب بین‌المللی قرار داد
🔴
روسیه مدعی شده دلیلش این هست :  تلگرام کانال‌ها، گروه‌ها و ربات‌هایی رو که به ادعای مسکو سرویس‌های اطلاعاتی اوکراین و گروه‌های تروریستی ازشون استفاده می‌کردن،…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138378" target="_blank">📅 11:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138376">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دبیر کمیسیون امنیت ملی: عمان باید بداند مذاکره با آن‌ها در صورت مداخله آمریکا، هرگز اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138376" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138375">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت دفاع روسیه : دو کشتی باری حامل تجهیزات نظامی اوکراین هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138375" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138374">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be8d96d36.mp4?token=YJ5QR4bORxZuLQFK4jXWL-mZe3CVBXW7YpPNUgokHA4IlzPkfnszM0wDFlPYxTNa6BkftORRHMaE4vraWp7lH-EJHzLg5xfDLwptpT3ahUQ_ciLolgizMF5jqzjZKjGQPBAqCxFIHmqWUmkZkaonvIpC-mVD4nmYhLGRX8OVoJEbnikJtUOY59d1MPnC3FOksDL7Fxa9Ce7yh5SpeCdWqY5S7WP7jfU8A2vO-NnHBFlXbRXYHRIrFehWxEctnhP1GmbKNgTsioOAUGOYABLokILaGozIhFgL3-b7gshQ_tk6OTuaI8MOpeeonJGtLwRVOCz-1T0qh82zNVSt6Vxhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be8d96d36.mp4?token=YJ5QR4bORxZuLQFK4jXWL-mZe3CVBXW7YpPNUgokHA4IlzPkfnszM0wDFlPYxTNa6BkftORRHMaE4vraWp7lH-EJHzLg5xfDLwptpT3ahUQ_ciLolgizMF5jqzjZKjGQPBAqCxFIHmqWUmkZkaonvIpC-mVD4nmYhLGRX8OVoJEbnikJtUOY59d1MPnC3FOksDL7Fxa9Ce7yh5SpeCdWqY5S7WP7jfU8A2vO-NnHBFlXbRXYHRIrFehWxEctnhP1GmbKNgTsioOAUGOYABLokILaGozIhFgL3-b7gshQ_tk6OTuaI8MOpeeonJGtLwRVOCz-1T0qh82zNVSt6Vxhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی دیگر از حمله آمریکا و عربستان علیه حشد الشعبی در نینوا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138374" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138373">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو : به نظر من، اختلاف این گروه‌ها بیشتر سر اینه که ما چقدر قاطع هستیم
نه اینکه از نظر فکری با هم فرق داشته باشند
🔴
کسانی که فکر می‌کنن ترامپ خیلی قاطعه، می‌گن بهتره باهاش درگیر نشند
🔴
ولی اون‌هایی که فکر می‌کنن می‌تونن با آمریکا کنار بیان، معمولاً خواسته‌های بیشتری مطرح می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138373" target="_blank">📅 11:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو : وقتی نیروها و سربازان شجاع ما متحد باشن، هیچ چیزی نمی‌تونه جلوی ما رو بگیره
🔴
هانیتی (فاکس نیوز ): امروز با ترامپ دیدار داشتید، جلسه چطور پیش رفت؟
🔴
نتانیاهو : خیلی عالی بود، یکی از بهترین دیدارهایی بود که داشتیم
🔴
من همیشه از ناامید کردن کسانی که دنبال پیدا کردن اختلاف و ضعف در اتحاد ما هستن، ناراحت می‌شم
🔴
چون چیزی که امروز دیدن، یه اتحاد محکم و بدون شکاف بود
🔴
رئیس‌جمهور خیلی صریحه. ما یه هدف مشترک داریم
🔴
نمی‌خوایم تهران به سلاح هسته‌ای دست پیدا کنه و آمریکا، صلح جهانی و اسرائیل رو تهدید کنه
🔴
این هدف یا از راه دیپلماسی یا از راه‌های دیگه محقق می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138372" target="_blank">📅 11:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
معاون وزیر علوم: آموزش در ترم آینده حضوری است.
🔴
دانشگاه‌ها مجاز به برگزاری ۲۵ درصد کلاس‌ها به‌صورت مجازی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138371" target="_blank">📅 11:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138370">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRmV20kyVRx0fe9NanXiJaFMcmmf2zC4HYLLTsykokYHzk4Htt7-CARRXKfCtT4eAgosUAKek10dYJiX0jq9PrhXKf7XMCQS3ZdVxVmuw5JCgY2aix5aAbKzQ7sje_Kud36lM1TV0TuKBBbnxvt6BFX4KFXIJ5zxkeiLCFNBGddGjI3AYpMv4thhHViEIRTHee_c86fwv2cnn5kQM2fC_TagA6s-FB9X_20yF-g_1UdSARnAWgQAOfCDm62bKtyFBhSNsexD3axCrxvCBaQEyoz49QY7qRPsKKmSPSOOfsuPpePyjSsgHRi4e9yrwVJPGtUxNMbB1zxVneAmrWb4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز آمار: تورم نقطه به نقطه خوراکی‌ها در تیرماه ۱۳۴ درصد شد
‏
🔴
این شاخص در مناطق روستایی به ۱۴۰ درصد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138370" target="_blank">📅 10:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138369">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b1c8f5ff.mp4?token=lNihtIEIp9JSmmc4Apk3KmGpx1mW7FqudHtBYGsDbIxevpGsQddlU7UCeUmPL3nnqiqQdOCkQfZEfrsWqchrgKuHx3b4z12QQk7uqHDmpi4k0j1jDV2f2lPqBa069xj1FxFtnJ4gOWLsUz61OihIci1_a34AeoW6UvqNu70hYUr260vVFMl76IX3Mtq3oNjgZ_qdbxxgPbtXeiZNWI1nOI6_Nyw1xgmmrE7b7l-jinMrlD2moPwPtf4CNpFY9homPxwjMukfXMvjxwkWuhUPLBmtMxUNfEzZvWAUb3bxQxBpmHjR2tFTkBdwY7L11lmc30_OyrA0PdEON0e2FGGP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b1c8f5ff.mp4?token=lNihtIEIp9JSmmc4Apk3KmGpx1mW7FqudHtBYGsDbIxevpGsQddlU7UCeUmPL3nnqiqQdOCkQfZEfrsWqchrgKuHx3b4z12QQk7uqHDmpi4k0j1jDV2f2lPqBa069xj1FxFtnJ4gOWLsUz61OihIci1_a34AeoW6UvqNu70hYUr260vVFMl76IX3Mtq3oNjgZ_qdbxxgPbtXeiZNWI1nOI6_Nyw1xgmmrE7b7l-jinMrlD2moPwPtf4CNpFY9homPxwjMukfXMvjxwkWuhUPLBmtMxUNfEzZvWAUb3bxQxBpmHjR2tFTkBdwY7L11lmc30_OyrA0PdEON0e2FGGP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیر کمیسیون امنیت ملی: عمان باید بداند مذاکره با آن‌ها در صورت مداخله آمریکا، هرگز اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138369" target="_blank">📅 10:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138368">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حشد الشعبی در بیانیه ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر کشته و ۳۰ نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138368" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjDyWT3Y2PslsbkrVqy__GYOSaOg93CKLSUje0R-S_NLYVmfowyPlWeXFMBjh8jefJSma2I_niTGhQ13Eg4u06y_i5popn8nsyu89wmsgt03_98nHB93J5tx2UerbNhlvXgh2J4eRPc9sA2aanDfLHq57557Iv4CAC0kvJjTZLjS3jTVrOrkqzm_tP1cNzffAfJCdS619x96_GjS4Qk9BA11M4l1xUUVgV0rl-p8kJZiswsD3iPfXx38_DF8uRS89z83ENYzVsli2iTOVVWV96dYP8RLB-hwVVf-Dgzs6Cv6MbftoBmJXzaJ1Beqwn0Ydcq7ptahds3J1lFlm1IIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCR6XzvOBUB56Tj9rjm_lqXanDnLormeqV-dwpKS2Rnhz4QmMcD5i8kFhz1m1zjJ4FZGI-34YuGoa1IQiLZSxg1_NQbbdURIotmm20_doihI6qy05Mu8H-YzqPLjUjdffqa0UF_Q8jSHAsv08Heo_i7h0McEweKVA3u-e2gYqjA-cRqmhximozhX4njOInm-IZ_daD4kXIoNjpLL_grd24ve7NaZRT_kg-_X6KBkl2Ajok1kQbA_sFo1VNbhYQVBBxTirD2osAo-2TEVTu5eDFpR-UuOhf8blTTkCnchVqgJIuBqcLfOMR8oiy4SbNbB7-X4jvU4PiqHY3oZjaIJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EICIgMzvcH0_-kL6AAvXvGRegNoQBdfy3TVESDqOrwLSGO7zyuTjuZFLzwQRn6uDIEpLA7aGuxG-zuIq233_I5hv9oahv6vKR4GjU_090KlB29AweBgO0KhcC9_iOZUVxTRv6QafMfQCBxm6Hzn0U0QUzURYb-XQl-mGQoNtpG9igqgtsN5Rfvm29G-v7JcHzp7CZs7niI85hYwojfrRHtt8R-4hx3ctOUyS-b4dLyVCZyuLHVUn3Qxd8tTjHmrJTIP35BWG1WjWIakB1kp2x3YNvVPH5Vlv58ytTGPtHFhJbKkq0irMWOAGWxDkKxDFQBQg9b8EOYM5SZEBJT2prw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگری از تخریب مقرهای حشد الشعبی در عراق پس از حملات سعودی آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138365" target="_blank">📅 10:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز: من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
‏
🔴
هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.
‏
🔴
موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138364" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138363">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد به شهروندان آمریکایی هشدار می‌دهد که از سفر به عراق خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138363" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سازمان امنیت فدرال روسیه؛
دوروف، بنیانگذار (تلگرام)، تو فهرست افراد تحت تعقیب بین‌المللی قرار داد
🔴
روسیه مدعی شده دلیلش این هست :
تلگرام کانال‌ها، گروه‌ها و ربات‌هایی رو که به ادعای مسکو سرویس‌های اطلاعاتی اوکراین و گروه‌های تروریستی ازشون استفاده می‌کردن، نبسته
🔴
از این کانال‌ها برای هماهنگ کردن حملات خرابکارانه؛
🔴
عملیات تروریستی و حملات سایبری داخل روسیه استفاده شده و به همین خاطر برای پاول دوروف حکم تعقیب بین‌المللی صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138362" target="_blank">📅 10:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روزنامه کیهان: دفاع از آزادی اینترنت به سود دشمن است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138361" target="_blank">📅 10:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت انرژی آمریکا، ایالت‌های یوتا، تنسی، اکلاهما، لوئیزیانا و آیداهو را به عنوان گزینه‌های میزبانی برای «پردیس‌های نوآوری چرخه هسته‌ای» انتخاب کرده است؛ تأسیساتی که از تولید سوخت، غنی‌سازی، فرآوری مجدد سوخت مصرف‌شده و دفع زباله پشتیبانی می‌کنند.
🔴
این مراکز همچنین برای استقرار راکتورهای پیشرفته و مراکز داده در نظر گرفته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138360" target="_blank">📅 10:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خبرگزاری فرانسه: وزارت امور خارجه ونزوئلا در بیانیه‌ای اعلام کرد که این کشور سفیر ایران، را احضار کرد تا به اظهاراتی که «تحقیرآمیز و نامناسب» تلقی شده بود، اعتراض کند.
🔴
مقامات ونزوئلا، مشخص نکردند که به چه اظهاراتی اشاره دارند، اما ویدئویی که به صورت آنلاین در حال پخش است نشان می‌دهد که عباس عراقچی، اخیراً گفته است که ایران در مورد مذاکره با آمریکا «ونزوئلا نیست»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138359" target="_blank">📅 10:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیویورک تایمز: ایران به این فکر کرده بود که یک حمله موشکی نمادین به یک بندر اوکراینی در دریای سیاه انجام دهد، پس از آنکه گزارش‌هایی منتشر شد مبنی بر اینکه اوکراین یک کشتی باری ایرانی را در دریای خزر مورد اصابت قرار داده است.
‏
🔴
به گفته مقامات ایرانی و غربی، تلاش‌های دیپلماتیک تاکنون از تشدید تنش‌ها جلوگیری کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138358" target="_blank">📅 10:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPa-VfmZfaToIqYjsEO9oExJuVYj1I_mq8vCrc7cuXF5_n3OwBNVXD32rYRzAiSKG6UK4Atn1ZD9j1xDnjPgu1pd4jgix1d7fKl97PomqGiBNxUbx6HB7mGJx0Rpj-X1ngBKLyT1wzpj9IEJ-r0mvSqJQJEfo2YGwc88TP2h0hR17ZdBtXcBgm3bnwQe-V_gwG5jRpvE4JQHxrzVu1F8ao0u7osfyqfxfTY64Ud308Ch97r0AfN1jWHf7zn_VQ80qRlghRBNpTlciN2rKMur1Swo1C-Uam5siQRz3sdgHneU70l9iMM8d5OyM33iNEsfZFm6dquFmTrwCFFdSy_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشته شده های حشدالشعبی توی حملات دیشب آمریکا و عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138357" target="_blank">📅 10:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6c48fc229.mp4?token=Vm_BkKMaM-KtMbmSBbtYMiFqBMgs_Esf_81pG9nZrsBL2-Ge_Zsmz-FjZ9P2aQ7COBYPr0m70Cf_vOwH1OAXqdIU5Hc04J-NIXM4tg7ocOgcTpiI8rb39usDvKgR3inbPbpXhC9bZn-Cy3wQ6VjvgPUvL0soz0mzV8X74AkD-F4dbVpQlDXAyHqFojzZ5A7Yv1PLLpquSZ_aMoX8noRUztnpMY5pTOifrZ2Ug9gb8gxXOpUi0-xvSKJcfdfKzdko2LbQYlUFPra0FC3xKVMZLbeLgiyCiEgb9msQZ6UONTE_b_AlCymyHSfZGvP7Uj6U38x4YL8YnFSt6GjfHALXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6c48fc229.mp4?token=Vm_BkKMaM-KtMbmSBbtYMiFqBMgs_Esf_81pG9nZrsBL2-Ge_Zsmz-FjZ9P2aQ7COBYPr0m70Cf_vOwH1OAXqdIU5Hc04J-NIXM4tg7ocOgcTpiI8rb39usDvKgR3inbPbpXhC9bZn-Cy3wQ6VjvgPUvL0soz0mzV8X74AkD-F4dbVpQlDXAyHqFojzZ5A7Yv1PLLpquSZ_aMoX8noRUztnpMY5pTOifrZ2Ug9gb8gxXOpUi0-xvSKJcfdfKzdko2LbQYlUFPra0FC3xKVMZLbeLgiyCiEgb9msQZ6UONTE_b_AlCymyHSfZGvP7Uj6U38x4YL8YnFSt6GjfHALXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حضور نتانیاهو پیت هگست، مارکو روبیو و اسکات بسنت در مراسم تشییع لیندسی
گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138356" target="_blank">📅 09:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رویترز: تهران پیشنهاد عمان برای مدیریت مشترک تنگه هرمز را رد کرده و این طرح را فاقد هرگونه شانس موفقیت دانسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138355" target="_blank">📅 09:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138354">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a620e7eb.mp4?token=vQ-MhDTNfKARXLYVWt7FpBXfrQesngr0QPCTs2qOmHRPz1YhUVlsT13c9TSitt9ccfM7FcGR7NMUc5UBCuizB1-47Y7ePZSBdjmWPiGqCwZ4SdJuiuOne-K5AMbHxBnPvXvtrpE0t8yxuTqBjjwUN40zuAxCvR5PjPiq56zA85GPQ2N0P8W5RQsLOPj8ozbP_h5i20BKRhuBEtukYYSMGQDoGVguNZX_czPINWdU10T21oujPj5bW9-ol7JvyMbdnW78lJlQDiPA1BA46qRXquTeTP5RiZsXz5lvBcGOk0d59cfJ6ZAhL7yT66ZsliIpyYqtQ1zgBKNnk7MIpwCzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a620e7eb.mp4?token=vQ-MhDTNfKARXLYVWt7FpBXfrQesngr0QPCTs2qOmHRPz1YhUVlsT13c9TSitt9ccfM7FcGR7NMUc5UBCuizB1-47Y7ePZSBdjmWPiGqCwZ4SdJuiuOne-K5AMbHxBnPvXvtrpE0t8yxuTqBjjwUN40zuAxCvR5PjPiq56zA85GPQ2N0P8W5RQsLOPj8ozbP_h5i20BKRhuBEtukYYSMGQDoGVguNZX_czPINWdU10T21oujPj5bW9-ol7JvyMbdnW78lJlQDiPA1BA46qRXquTeTP5RiZsXz5lvBcGOk0d59cfJ6ZAhL7yT66ZsliIpyYqtQ1zgBKNnk7MIpwCzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام
:
جنگنده‌های آمریکایی و سعودی در پاسخی قاطع به بیش از ۳۰ حمله پهپادی هوایی که طی ۷۲ ساعت گذشته به دستور سپاه پاسداران انجام شده بود، چندین مرکز لجستیکی و انبار تسلیحاتی حشدالشعبی را در سراسر شرق عراق هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138354" target="_blank">📅 09:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138352">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYYn9tuGjkvhgh986PLwdcBNJ2ATBBlBrtu8zzDLtChRJjsd935MutSfC-wMBahdWaYHvF0vjutEdKWcZMsX61VpiCQrwfE7gth6l8Vq45NMIXc93Csu-tdjNzD7eOOay-fCSuRwO-fYti4CpXnakwoLUWjaNtcEH-ejcHy1R7gkhudKlh6CCOpA6Smm8KHmluJyWqf0319GkmJEtV-XSqnfAGb7Hy0SSEJBvPTY01x91V-f8n9lvQF0NG2uS0biu-OwSzfVv7BctAAk5vSSCSsteGzjeUBPY2r5MspJoId4kFppFUV9wsBcHD267LcnUfdbVnAtGpNQL5czDcouRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-3zXBGgwZR4ck05wTG-zLv1ILs7NgpQjq1YbbDT1Tf_BML7QjvrwqG0-_fhkywEqgAfK5NMSZTkyS4ibEznA2EZkMGKSn8NCdDe5HX5Hy4SGobKM40_OTLKma7xvzcCaqQUTGOMkZNpy6YpVdGFEUnP9eR_2nhR5AzAVWeYcy4Iwv-qU8SbsPfEIm8pOsxXqjLYkhFdxY1ICbApV7SLn1YY_Ibkp3-vh7PCgHSCc8hyBS6ya3Oa65zMEfBoonevQ4j-0bXTAQafppO5FeR4C2QPUG7uXj0aHpdtzWex9wmQhnXYcSEnZ8Jcwqzbrdl9snGh1nHmZCT5rmaNj_IPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری جدید از بمباران سعودی در مقر تیپ 24 در منطقه المقدادیه در استان دیالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138352" target="_blank">📅 09:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589d2ad2c4.mp4?token=bSqvwdUvD3ZVqDKavUrx08njPK5uueXr1_yo_PnLvliZIzWfRHXUwiZuYEVxOVgYRdCFfRK7fnbFOvb_-qVTG1iCbjYj3AQIync1piGElIPnD3R-UGGvwz-rBstdknW8B7rlBW6S3pNRmF6IfvzUgm31fdg3RmFOumH-Shrrk_UKodqhH2q9EuI13h_TP2Vk8AJyTEO6WT2r9lOfbADd-ukdg3xk2Pv94Zj_h6a-ikG_ol-tvz6JmlNTaV69HBbgwYlh1uKMN_wVFMG5CMmpJgRAfpG-_QLwfHb1X8LHV9PnEnDwvT0q3-Os5L6cKq05tSUwGlVxutuaFwEy5xzZM7WFd1cOAbFY_LaI6C5YWuZbu_eMKnxdHz73eBTl_OtKdp10TG5DrDXIKlPbMs_pjJZUp72UmeptZ0zDQFufWZHBgP0_KNxj5mbwwHaAYaRY36m88WZZ_ghqZ4ip26M9b72jLxGnOaWYjTB1y5piNU_NcTVtRyD5VyUPT0300uKDIecg5-MAw-gij39qTLNlPHuuYPsGIBYrKpi8TnOXFBbshv4M88mngot8ZPJilDmnE_BYiBoK2iFaFYukV4hYvEhDThu6kQ_7KaPUQkE8c2lKYA_1TuIT8_3ja7f4J5aC2Cut8ySbD5QrXS2SNuKfAjEubDp-ntgev3R_BrlTmYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589d2ad2c4.mp4?token=bSqvwdUvD3ZVqDKavUrx08njPK5uueXr1_yo_PnLvliZIzWfRHXUwiZuYEVxOVgYRdCFfRK7fnbFOvb_-qVTG1iCbjYj3AQIync1piGElIPnD3R-UGGvwz-rBstdknW8B7rlBW6S3pNRmF6IfvzUgm31fdg3RmFOumH-Shrrk_UKodqhH2q9EuI13h_TP2Vk8AJyTEO6WT2r9lOfbADd-ukdg3xk2Pv94Zj_h6a-ikG_ol-tvz6JmlNTaV69HBbgwYlh1uKMN_wVFMG5CMmpJgRAfpG-_QLwfHb1X8LHV9PnEnDwvT0q3-Os5L6cKq05tSUwGlVxutuaFwEy5xzZM7WFd1cOAbFY_LaI6C5YWuZbu_eMKnxdHz73eBTl_OtKdp10TG5DrDXIKlPbMs_pjJZUp72UmeptZ0zDQFufWZHBgP0_KNxj5mbwwHaAYaRY36m88WZZ_ghqZ4ip26M9b72jLxGnOaWYjTB1y5piNU_NcTVtRyD5VyUPT0300uKDIecg5-MAw-gij39qTLNlPHuuYPsGIBYrKpi8TnOXFBbshv4M88mngot8ZPJilDmnE_BYiBoK2iFaFYukV4hYvEhDThu6kQ_7KaPUQkE8c2lKYA_1TuIT8_3ja7f4J5aC2Cut8ySbD5QrXS2SNuKfAjEubDp-ntgev3R_BrlTmYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس نیوز: به نظر من اروپا یه قاره رو به افوله، اشتباه میکنم؟
🔴
زلنسکی: منظورم اینه که این اروپای متفاوته، درک نمیکنم چرا از اوکراین دعوت نمیشه برا پیوستن به ناتو
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138351" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
آخرین آمار حمله عربستان به عراق به نقل از نایا
🔴
۱۰ کشته از تیپ ۳۰ شَبک
🔴
۲ کشته از تیپ ۲۴ حشد الشعبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138350" target="_blank">📅 09:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
تعویق درگیری در خلیج فارس می‌تواند برای میانجیگران وقت بخرد تا راهی برای بازگشت به دیپلماسی پیدا کرده و از بازگشت به جنگ تمام عیار جلوگیری کنند
🔴
مایه دلگرمی است که وزیر خارجه اوکراین با عراقچی برای کاهش تنش‌ها گفت‌و‌گو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138349" target="_blank">📅 09:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
حوثی‌های یمن با صدور بیانیه‌ای، حمله مشترک آمریکا و عربستان به حشد شعبی عراق را به‌شدت محکوم کرد و آن را اقدامی «جنایتکارانه، بزدلانه و غیرقانونی» خواند که ناقض حاکمیت عراق و مغایر با قوانین و موازین بین‌المللی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138348" target="_blank">📅 08:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
تعداد کشته های حشد الشعبی در موصل و دیالی به ۱۲ نفر افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138347" target="_blank">📅 08:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرگزاری ملی لبنان از حملات توپخانه‌ای ارتش اسرائیل به منطقه تل النحاس، در مجاورت روستای کفرکلا در جنوب لبنان خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138346" target="_blank">📅 08:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138344">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kuvr6BA_HC3i9wi-hE1JgyQEBp66mV9EA0WpodUUr3p_tM5x2E_TbB6Q89a5deOokTMaLt0gXYAZIZIU0fzEoqe5CKJhoVyapu6YA0eoTe7_HMlz8rqhCX7HM8N-AFpUVqaZDec_bcgxrrzjwYkKmKQ5wcnjR_yFr76RN0K2lD9PbH0rRDQ2Ydzq4LFo9dhHFmL_Cu3kWTsQykPytA63L8JdCmjENbSw_eBW3C9lDn8sdMVP67bpNujAXrqlKUrMiRO8FRbaaW5KWxd6Ju8N4LmCtTnLIajDF3bLKR75w3NOTaQWdLQdMOiZe8YEOOlu36rNfwAS1Z0Wcqrb0o9v8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9Fl0fQ6GDc_J_A-8_V2IeuWT2ve-Jhtw2JaDbCXjxikSVYuRvqALt1nWSsSTUt67YrVeUEHWqWep7Jm66t0yLw7GpNY40ePti4oh7d4y4XxokH4cd2FCZ_XqAzVRmlBFGuU0At3PO1XjsY7AOIjurltoISVMDL5KHxr6PErh9lhnulwJ4t6ZIU9o5oXYXXc0y-UA8DnrC8cV955W8zuqh3-d_fpfSz95VRHcUM1y57Lq8-sCMa40wz0gNKeAs1ToDgwr71SgoxaeyPZVbKRXLEej81Y7VORTwfOBotdlq1B0H4ayr7uxPYX6yfcAnLCOoLP7g89z-HqUVb2ZVIwUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارش روزنامه انگلیسی از نسخه جدید پهپاد حدید 110: پرسرعت و غیر قابل شناسایی
🔴
روزنامه انگلیسی تلگراف در گزارشی به بررسی نسخه جدید پهپاد انتحاری «حدید 110» ایران پرداخته و نوشته است که این پهپاد پس از یک فرآیند به‌روزرسانی، اکنون با ارتفاع پروازی کمتر، سرعت بیشتر و قابلیت پنهانکاری بالاتر پرواز می‌کند و شناسایی آن نیز دشوارتر از گذشته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138344" target="_blank">📅 08:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138343">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز: پیش‌بینی می‌شود که ایران در چند هفته آینده، بین 300 تا 400 سیستم دفاع هوایی قابل حمل ساخت چین به ارزش 60 تا 70 میلیون دلار دریافت کند
🔴
رویترز: سه منبع آگاه گفتند که انتظار می‌رود ایران ظرف چند هفته آینده اولین محموله از ۴۰۰ لانچر موشک دوش‌پرتاب دفاع هوایی ساخت چین را دریافت کند، این کشور در بحبوحه جنگ با ایالات متحده، در حال بازسازی دفاع خود است.
🔴
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگترین تلاش‌های شناخته‌شده تهران برای تقویت پدافند هوایی کوتاه‌برد خود از زمان آغاز جنگ با آمریکا و اسرائیل است.
🔴
وزارت امور خارجه چین اعلام کرد: «گزارش‌های مربوطه کاملاً بی‌اساس هستند. چین پیوسته در ترویج صلح و پایان دادن به درگیری نقش داشته است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138343" target="_blank">📅 08:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=at5Iuu673X1owiNRtW1C7ht-or0MNuRqyBXaDMUOqJ390VfVCYt9pF24srAGs5ie-spjSN2IFDndoa8L3SbXhscaERASek3PA0j4FLjmje5EUzmKeSRf_2VWIRU1EB2ZEQLQOT4Cn6t8ljHApVSDmI88yDt8jj1_p2HWgqL8qyW0-56yXBg8AzdecTug3Kjc2p5lYV4cK8naiPhW8fKnyzb-nZiFoI7JTS9bxCKik9si_MO4wbOmSc3UM0qRQCVz-ureCiNav07ylIBWEPyfgg5x-16IsgCqgVrctzo-wbbvyzJEEvWiUEajgazE2NxKN2M7U0SvAc1ATNLy9K0wDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42cf14717f.mp4?token=at5Iuu673X1owiNRtW1C7ht-or0MNuRqyBXaDMUOqJ390VfVCYt9pF24srAGs5ie-spjSN2IFDndoa8L3SbXhscaERASek3PA0j4FLjmje5EUzmKeSRf_2VWIRU1EB2ZEQLQOT4Cn6t8ljHApVSDmI88yDt8jj1_p2HWgqL8qyW0-56yXBg8AzdecTug3Kjc2p5lYV4cK8naiPhW8fKnyzb-nZiFoI7JTS9bxCKik9si_MO4wbOmSc3UM0qRQCVz-ureCiNav07ylIBWEPyfgg5x-16IsgCqgVrctzo-wbbvyzJEEvWiUEajgazE2NxKN2M7U0SvAc1ATNLy9K0wDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صلاح الدین
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138342" target="_blank">📅 08:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
تتر با افزایش ۲ درصدی به ۱۹۴ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138341" target="_blank">📅 08:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پس از حمله بامدادی ایران به اردن ،کاخ سفید پست جدیدی از ترامپ با متن
« کار این جنگ رو یکسره کن »
منتشر کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138340" target="_blank">📅 08:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نیروی دریایی سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138339" target="_blank">📅 08:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/138338" target="_blank">📅 08:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-BbcZx49WzZH002IEdY40BZSUJuk_E9DkvmOev62KYnJkerMsONeAJyyaoYUlh3WqV9_avLmiYcze0vtcOgcDv8Py2pb1BIm3ErCnGjEHq6rEOIxfQMCMnxBMwPwi2beCz6LbACwfBfuqf2tjcTxpPC3MZej-hexjJK2UBtdeF5r50Zu89rBjmYbehYc2nGFHN5ge5xm8NgT0r3Qh4LalB6Y_oZj41hqLdbx0fGwl49EwxTwPbGWj7o4TdydU9t3HYG0wZ4cUbEc3BbjfEFXY3pO2fyUkMTrbcAIXi6NcYWavt8g2atRAoQ4D7yyJnbpgInnjX2pRt_VgynAa8DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آخرین قیمت نفت خام، ۸۷.۶۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/138337" target="_blank">📅 08:32 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
