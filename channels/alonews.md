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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 23:45:45</div>
<hr>

<div class="tg-post" id="msg-136191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
طبق گزارش ها بیش از ۸ انفجار در بندر عباس شنیده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/alonews/136191" target="_blank">📅 23:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/alonews/136190" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
احتمال حملات آمریکا به بندرعباس. گزارش‌ها حاکی از آن است که انفجارها بسیار بزرگ بوده‌اند و نمی‌توان آن‌ها را به پرتاب موشک‌های کروز ضدکش مرتبط دانست.
🔴
احتمالاً انفجارهای سیریک نیز نتیجه حملات آمریکا بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136189" target="_blank">📅 23:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136188">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/136188" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136187">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/136187" target="_blank">📅 23:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136186">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/136186" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136185">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / بندر عباس صدای انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/136185" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عوستاد رائفی پور: ترامپ و امارات، خارک‌ و‌ سه جزیره را نخواهند دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/136184" target="_blank">📅 23:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزارت خارجه آمریکا در  یک هشدار امنیتی از شهروندان آمریکایی خواست درپی افزایش تنش‌ها در خاورمیانه، سریعا ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/136183" target="_blank">📅 23:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_Gm5c2BaPpcDOYkyPbJkhsV8j_Ulw3s1WuuzBpgzKL-ZjLzeoCWgD07M3AgWAM-D0phg5YLVMIUCMB9bbcXvRS0Xg_6TM529v-HLyn1U-I6aSxwjclDtd3vLvUwv9knl__EQyc1L5Gr61IOKy2wNdn13ig-DpPNJBSjrMVJIXvUjo4QdT-rP4r6nunMO0jwhtr9hNQw7WoRjM7Eep9O3PTuiv5Z1_kTVOI4l1lr8A00m4XfCCc6BoRqPcOyl9LkBT0i7NdoBbBxTKXEw8nKsrRka5s05U8vOPNjBbQywr0LGw36rpMPG8ibSWdL6UDgQ-NBLyM-4ViL3DKLJHC_2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت متفاوت یک سایت روسی از سرنوشت سومین نظامی مفقود آمریکایی
🔴
یک سایت روسی مدعی شده برخلاف اعلام سنتکام، جسد سومین نظامی مفقود آمریکایی پیدا نشده و احتمال فرار و درخواست پناهندگی او قوت یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/136182" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
صدای چند انفجار از حوالی شهرستان سیریک در شرق هرمزگان شنیده شد و تاکنون جزئیاتی درباره محل دقیق یا علت این انفجارها اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/136181" target="_blank">📅 23:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری / هم اکنون گزارش‌های اولیه حاکی از شلیک موشک‌هایی از ایران به سمت تنگه هرمز است می‌باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/136180" target="_blank">📅 23:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره:
گفت‌وگوها بین ایالات متحده و ایران ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/136179" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سی بی اس: تو حملات ایران به پایگاه‌های آمریکا تو خاورمیانه حدود ۱۰۰ نظامی آمریکایی زخمی شده
🔴
بعضی‌هاشون آسیب مغزی شدید دیدن، اما ۹۶ درصدشون دوباره به خدمت برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136178" target="_blank">📅 23:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووووری/سی بی اس:
یک توافق موقت درحال شکل گیری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136177" target="_blank">📅 23:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ04aaPmWTejgs6iW_qhXVA5nyNQs_2XcCzajnPuh-DPonxZV_jE4AMK15DRKsICxCsRI8dLGqyh3M8WtRtOupAjfbvrSvG1b0JrdmTHddVzb3QDOrf9z85AuzoaNXm6627fVy_aKc1geIoXuNkFt6GA3ZCWX3jNCtXdZ0q7X-TqH80GkV_zBnMaTOCKp6OtZU_YDKg6Oww_ZvKcyem2-5IsDmp0Ry7ggEF0tjtXh4oUa9OJVtgBTQ9_7OJTVl4ominqdW67AIQdMYYNJDn3pRtLhyc46EGeNFmtL-XQQxV7sHUHM4XUKrearbOKDH1qSjE3ZCLbn8dep1aOQHxT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.
وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/136176" target="_blank">📅 23:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5xQixAuY-MTdOIzsru65j5aqLRL5UMzbHAVBHPgCnB9asGlwzBxMR9omg8sP4nCtwXTNgVUcaDN1Ve9dY-MQpvO2VuC2d2mcHhPIvPpzAMfBSPl3XAPv1g-Yl8-c814DTBIoCPuq60_hl_zh7WtLpUsqkHIbzjwrc06BkCQkidzyuSgfLsi_YnJBJg1TW1khXgLsCQidH0hWtTHysJTsKvcw0vhSocnAhbCFMPJuguv8eB9V9YYNPAt42nfrc0DYjts-mrehfH-iWePFnuM8lQUFU9qfhyHh3ZhCMvSZrizuSBAmLkaBGVIVygQ3QHi95ZYc1TBMlpKj_BxMySIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: احتمال برگزاری مذاکرات برای توقف درگیری‌ با ایران وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/136175" target="_blank">📅 23:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDd8WWLad0UMptrJmF8gPNOVOFjHQrFbHwLFa9siIRn3Xhxhy0DbNyqDj63KNg2d3mmTvZWIVau6KYwbL4EGj9cG6bDaPmrbMv7U08Cge-C3lsJHwrq0KiA1MwvWLN6o1-HQtxgsIVjsvjUT3Z9ZxPlB9XS2KpXZIJsIU_rlHGAhES09I3A5IjYMaGF1VVay27qSas-qO9IcdIo9JvkofGc6A1wtGRIACHjzCIfn8mY35aHpLC8iU25Xs_GrNVVQbqjWM01TEpvag3znY6PO8MIl0tQV34KF32hsDISpkUQUM2hme2YK4DOZWpH51UZu0gB-xbtvSt-Eem2roH6uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: فوتبال تمام شود، کار آقایان در وزارت ارتباطات برای قطعی اینترنت شروع میشود، اگر نشود دوباره تماس خواهم گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136174" target="_blank">📅 22:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JO9xy6clG5HNQgKm-YbjuDLeXjjjvAetpCMAEf5EuXDXH4n5LjtxFS3wHRzEK4HTgJ2Sn45fAx-k--EeUXvvFYCyt9V5lkkB3J3bqZYfA1QzlYXvY_g8Wejsdv7NpznvjH7ZmiILtztkA7lHpA2z67Fam9TA5Dt5_gfwASiUq5kqPewvfirOmmHswsr0lTEqdd1DBHXMRHFwCE5h3jKcfSY8_QyvpL6BmuxcBY4FsFtd5iaPqqXPhAsibMtozZyQG4e4HTT2gMS4zBC009EQkoVukzSsYmDgoCpE1nM8S4OH5PWil6y3Q9Ui9wf9_ELUD2cHWeHrq_M3dPjKLtL1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه رومینا رحیمی و ترانه رحیمی، دوقلوهای 18 ساله
🔴
بخاطر شرکت در اعتراضات دی ماه و تخریب اموال عمومی و... قراره بزودی اعدام بشن.
#نه_به_اعدام
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/136173" target="_blank">📅 22:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b921e97792.mp4?token=A6t5NtqrqXJlkJLtML1Sx4qZXVHflpxVuxl9Ze9zoGh9WpRFaFI6FuBwPcULrE6P0gMeO8TGoc4pGaispQDFGmzA9t-02t6kmVWo88h6j1wSFO0zWSFWOeDRbJbRdrw-I-5SuoBRghyxyOMf5CvVK0u2DkloFHrds9ycabqWZJ-5uPjD98VQHMNTO97FBBv_7GDG4WXmMPuEzRO-J1dyvTckiXeoEAPdZau2k6NGRJpxoWsmvrFtowIbwKSHhQLxUM8OaYcwBMEbR9Iu7nGhKouE8_2l7VmAXnnkujrKUQOfUXmkvPuTYeTm9P7nhMEF9hxjx5RUg01sbdaid-_YGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b921e97792.mp4?token=A6t5NtqrqXJlkJLtML1Sx4qZXVHflpxVuxl9Ze9zoGh9WpRFaFI6FuBwPcULrE6P0gMeO8TGoc4pGaispQDFGmzA9t-02t6kmVWo88h6j1wSFO0zWSFWOeDRbJbRdrw-I-5SuoBRghyxyOMf5CvVK0u2DkloFHrds9ycabqWZJ-5uPjD98VQHMNTO97FBBv_7GDG4WXmMPuEzRO-J1dyvTckiXeoEAPdZau2k6NGRJpxoWsmvrFtowIbwKSHhQLxUM8OaYcwBMEbR9Iu7nGhKouE8_2l7VmAXnnkujrKUQOfUXmkvPuTYeTm9P7nhMEF9hxjx5RUg01sbdaid-_YGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهم پناهیان
‼️
🔴
ما الان داریم منطقه رو آزاد میکنیم، مردم اگه بی برقی و بی آبی رو تحمل کنن، جهان رو آزاد میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136172" target="_blank">📅 22:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وال استریت ژورنال:
مقامات آمریکایی جزئیات سه حمله موشکی جداگانه به پایگاه هوایی موفق السلطی را شرح دادند:
🔴
حمله اول به باشگاه ورزشی پایگاه که منجر به زخمی شدن تعدادی از سربازان در مسیر رفتن به پناهگاه‌ها شد
حمله دوم به یک آشیانه خالی هواپیما
🔴
حمله سوم به یک خانه کانتینری که سربازان در آن خوابیده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/136171" target="_blank">📅 22:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
حمله زمینی ایران به کویت</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136170" target="_blank">📅 22:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شبکه اسرائیلی کان:
ترامپ به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/136169" target="_blank">📅 22:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شرکت هواپیمایی ایرفرانس، تمامی پروازها به کشور های خلیج فارس را به مدت هفت روز متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136168" target="_blank">📅 22:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iuOruwZqLevlb35oK6sPCCUtTMvboUrqZJaRrt2TFcQMRoBngYe0MARkF5KYrfSAK10UJgjlAREkSsAHe7HBWzGriRbcQTt5l39FhBf-s5w26HgMXvhYCuZAX3VEnQ10nNISCFR6hJG9RsfYt37P1fGdiQ6d1-ei5Ww1x9Q6vwqFk7vT8_M50R0HVa6Tzu1jqbUQbWa0RM5UvXw-DiVTAxfBniYD4npFWf8Gd0w7IQ3NLX3nunUDmD26vh2aAZ4Iy7HyluVqKuSBsXBmeFpSj3J5BzvOVbjsK8ZJI3y6S46nIyfgMdRCoN_ZECCCa6cH6rXgZ7etf5YeJ1jtI37y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی بالاشهر تهران، نیمرو میدن 2 میلیون و 137 هزار تومن ناقابل! تازه با 5 درصد تخفیف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136167" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ارتش اردن : ۳ موشک شلیک‌شده از ایران رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136166" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/136165" target="_blank">📅 22:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر راه: بازسازی سالن مسافری فرودگاه بوشهر به‌زودی آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/136164" target="_blank">📅 22:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136163">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اطلاعیه جدید آموزش‌وپرورش درباه امتحانات نهایی
🔴
آموزش‌وپرورش: بر اساس تصمیم ستاد عالی آزمون‌ها، امتحانات نهایی پایه یازدهم تمامی رشته‌های تحصیلی، در روز چهارشنبه ۳۱ تیر ۱۴۰۵ در همه استان‌های کشور، به جز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔴
امتحانات نهایی پایه دوازدهم در روز پنجشنبه، یکم مرداد ۱۴۰۵ در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/136163" target="_blank">📅 22:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136162">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
طبق گزارش i24NEWS با استناد به یک منبع امنیتی اسرائیلی: ایالات متحده در حال آماده‌سازی مرحله بعدی از کمپین نظامی خود علیه جمهوری اسلامی در روزهای آینده است و افزود که طرح‌های عملیاتی نهایی شده‌اند و در انتظار تایید رئیس‌جمهور ترامپ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/136162" target="_blank">📅 21:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌هایی از انفجارهای شدید در پایگاه‌های نظامی آمریکا در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136161" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شهردار نیویورک، ممدانی : نتانیاهو حکم بازداشت داره اگه وارد نیویورک بشه، باید طبق قانون، برخورد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136160" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت سامانه‌ی پدافندی پاتریوت در اطراف پایگاه هوایی الازرق اردن جهت دفع حملات موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/136159" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شبکه اسرائیلی کان: ترامپ به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/136158" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: ایران و آمریکا به لحظه «بیدار باش» رسیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/136157" target="_blank">📅 21:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
هم اکنون وضعیت در اردن عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/136156" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136155">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت پهپاد شاهد به سمت پایگاه آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/136155" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136154">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک
های رهگیر بر فراز آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136154" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136153">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
امان پایتخت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136153" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136152">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
انفجارهایی نیز در اربیل، کردستان عراق رخ داد. ممکن است برخی از موشک‌ها به سمت اربیل هدف‌گذاری شده باشند، یا این یک حمله پهپادی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/136152" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136151">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حداقل یک چهارم از موشک‌های بالستیک توسط سیستم‌های دفاعی MIM-104 Patriot در آسمان فرودگاه بین‌المللی پادشاه حسین، واقع در شهر عقبه، اردن، مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136151" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136150">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیرها در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136150" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136149">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندر ایلات
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136149" target="_blank">📅 21:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آژیر ها در اردن به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/136148" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136147">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136147" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136146">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
گزارش شلیک موشک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136146" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136145">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136145" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
صدای انفجار در آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/136144" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136143">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4EQBnSuQUvoKmJdDBxNsyZaYNaz3RCt49pTJzlPRXL5g9U2pCown-kmTsgB2GZdrYwefxyzSevldJSDzVWenOFJUY6fMNBssrtw1bFOibVvLn-wmivqBNQ5Wz2MZWKxiOKO8U9nBaWzQRkm1_3-rFAbwWSbdAPChos8Vhsd9e3sG55s3JTF-FO6mxU35Mu_CYZ-Wj2q2E9FLFZD2fAl4Jc8X8NRCesKpTXuYIFyooNenhTL2sEA9NHLrXH0uQS_-P58KiSiN6MI8qISYPtv18HBPJyIs3Fk4ROS30vEzbCDdgYianfqjaj-0C0-_sH-70fJrucixHiGXj2uwXuBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/136143" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136142">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136142" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136141">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136141" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136140" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136139">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کارولین لویت، سخنگوی کاخ سفید گفت که ترامپ در مراسم انتقال نظامیان کشته‌شده آمریکا به پایگاه  هوایی دوور که عصر سه‌شنبه به وقت محلی برگزار می‌شود، حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136139" target="_blank">📅 21:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136138">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رویترز: حملات هوایی اسرائیل در تاریخ ۷ و ۹ مارس (۱۷ و ۱۹ اسفند) به دست‌کم ۱۱ محوطهٔ تاریخی ایران آسیب وارد کرده است که  ارزیابی‌های یونسکو، شامل میدان نقش‌جهان و کاخ چهلستون در اصفهان می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/136138" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136137">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136137" target="_blank">📅 21:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136136">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136136" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136135">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد - به نقل از یک منبع امنیتی اسرائیلی توسط شبکه i24NEWS
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/136135" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136134">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نماینده اردن: نظامیان آمریکایی برای گردش به اردن آمده بودند!
🔴
پس از کشته‌شدن ۲ نظامی آمریکایی، علی الخلایله، نماینده پارلمان اردن گفت: نظامیان آمریکایی به‌صورت اتفاقی و هنگام گشت‌وگذار همراه یک چوپان در صحرای اردن، بر اثر اصابت ترکش موشک کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/136134" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136133">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
افراد نزدیک به ترامپ از او می‌خواهند که پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرد
🔴
ایالات متحده آتش‌بس را رد نمی‌کند، اما می‌خواهد که مدت بیشتری ادامه داشته باشد و ملاحظات بیشتری در مورد تنگه هرمز وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/136133" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136132">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری /  تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136132" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136131">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریای صدا و سیما و دایی یکتا مثلا اومدن برن جنوب و بگن شجاعیم، بلند شدن رفتن بهمنشیر که ۱۲۰۰کیلومتر با بندرعباس فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136131" target="_blank">📅 21:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136130">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYPW706Mbbt5GH1YjZ9ATLjK5asNLB2sDVPQH4w3PAq34IvqTdfJEkzZPJ8WM94guMQUQaCkADBUUsUhtWfGv9dfyhvP78JuzEgkeSqfrtVH3SGfBWxn5ci7g5dJ5rYXMmRSxVCWV7VJA1Msacaz4o4eWysSfo5ECPxl96ieY6Y8NmvQc_Bhb5NBqMUNPEwyPb6ndedd-yxPoF5Sbwrt1B6oaGFNu1xz4xCbndSi90kX1DJtWxIOnCnTfx3eSXv7XhA1EzNMXXRk4CATysoAd8olrURDbz24MXzy8-_A78oEivfv2572c-epms6cda6d_LMRukiX2zZj1A39VFcYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو: ایران پول کم نداره، مشکل اینه که پولاش جای دیگه خرج میشه.
به
گفته اون، هر پولی که ایران از فروش نفت یا رفع تحریم‌ها به دست میاره، به‌جای اینکه خرج آبادانی کشور بشه، صرف حمایت از حزب‌الله و حماس میشه؛ در حالی که می‌تونه برای ساختن و بهتر شدن خود ایران هزینه بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/136130" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136129">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
سازمان ملل متحد خواستار «کاهش فوری تنش» در غرب آسیا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136129" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136128">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-uojnF4-4xn3khtNoykxE8b2G_AyfM5mmdG0AYX8_uxZuNODq9d1qfXjNh54h4cML5aLbRvM2qjVAJqTw_bWHe93b2db0J21CK3qNRPER0DbzNzPrEPXGcXmk5DkYOjOVL6KwzHqwLBeAYEal6mkztX6ek9-9rznEgf_ETAZlBkCtQeQ8PqyMtDtjzZKz9ClaxhU_ktoE9lq4ImyA809mo7E4DHvB50G7QWUw417UTTm_xp9By9uidto9Afd7WtYGNSbwK123Fly18D6sxwCviXcaskM-445xikFcve-xXOtX-rd5mHQ1F4BnDkXXWSO6cSY87pL8TC3ynuURcXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقوع حادثه امنیتی در سواحل عمان
🔴
کشتی دوم هنگام تلاش برای عبور از تنگه هرمز هدف موشک قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/136128" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: موضع‌گیری‌های احساسی نباید ما را از رسیدن به اهداف دور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136127" target="_blank">📅 21:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت امور خارجه چین: ما با حملاتی که هدف آن تأسیسات غیرنظامی در کشورهای خلیج فارس است، مخالفت می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136126" target="_blank">📅 20:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136125">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یک مقام دولتی افغانستان به الجزیره گفت که در اثر سیل در استان نورستان، 20 نفر کشته، 80 نفر زخمی و بیش از 100 نفر مفقود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136125" target="_blank">📅 20:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136124">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مدیرعامل شرکت توزیع نیروی برق تهران بزرگ: به ازای هر یک درجه افزایش دما، بیش از ۲۵۰ مگاوات به بار مصرف استان تهران اضافه می‌شود که معادل مصرف برق ۲۵۰ هزار خانوار است.
🔴
پنج هفته سخت را پیش رو داریم و امیدواریم با هماهنگی و همکاری مردم بتوانیم این پنج هفته را با کمترین محدودیت پشت سر بگذاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136124" target="_blank">📅 20:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136123">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc6dbhIJc2oj9rxkXRpEYhDfbUUBtU-18Np7Cdv06uh_Xmj8rlfEfdjJ1f67BGwdBCYvcvKm7bUU4YwbhNOg2gJrxu4TTvZLaI2kqxoJilacttFeCvYjwXYhQZo6U-o6kSvwV9S3zVLVaMyBQWEZm5C4h2-bU7hqIkbsiqftwCxU6GsWnmy4lfYdu4U23LKop6fBCsdJJ6a4c2sPM8efjUSthBPuENt4JfdqZummR_8FnzsI8Gnk21cI15MVsHcvawciYi3TAX3K7gKSzHLhdajepu3Oe08SpmqgIIVb-vcCkpPtJo6U11RYQ4URw4RoCCCTwclaDMUSrMjS9EXXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بازه زمانی ۹ روزه آغاز دور جدید درگیری ها میان امریکا و ایران، قیمت نفت برنت از ۷۰ به ۹۰ دلار رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136123" target="_blank">📅 20:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136122">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
روسیه: آماده کمک به حل مسالمت‌آمیز اختلافات بین ایالات متحده و ایران هستیم
🔴
خوشحال خواهیم شد که بستری برای گفت‌ وگوی کشورهای عربی و تهران فراهم کنیم، اما قصد نداریم خودمان را به آنها تحمیل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136122" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136121" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: اسرائیل سطح آماده‌باش را به بالاترین حد افزایش داده و نهادهای امنیتی خود را برای مرحله‌ای جدید از تشدید تنش آماده می‌کنند. همزمان، مقامات امنیتی اذعان دارند که تصمیم نهایی درباره روند تحولات، به تصمیم دونالد ترامپ بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136120" target="_blank">📅 20:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTlF78GtiIY1sOnwOLlrr2dqCi9kvO-sOsJzdVc6MY0Mn-KVVH37ww7VSOPa4VlgbOirr-K4D1wBRt25wzpcEmqISUavI-c3_5BlrsY-CLWLhaYPcBnEu8saq9pefRh4ijn40Xm18VE5spa-a_1_Va55zlLR0ewhv9J1EWv-buR6g0CDZlpQ9ZugNo-6ZnyUOHCwUWRTL8sD3SJG1_QLBcNAsehlAqBfAQxgC8Og9G5o0fpPEYjljKpcj1umkasEnj2dvwG90Iuta9pVmpDqItkCJ-Y42NxmZIp9Ebgl9dnhS276d8o26XvMUD8B9VeUfd23jl5mgo_S7tbERfdBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک سیستم دفاع هوایی کوتاه برد به نام FK-2000 که توسط چین تولید شده است، در یک منطقه ساحلی در بحرین مشاهده شده است.
🔴
این موضوع بسیار غیرمعمول است، زیرا هیچ سابقه رسمی مبنی بر استقرار این سیستم توسط بحرین وجود ندارد. امارات متحده عربی تنها کشور در خلیج فارس است که به طور رسمی از این سیستم استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136119" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNkdswi6vNLxEo4pKgaN9Qq6Q19yK6VAifPUOTTUUhn1EjSa0hNoZbYKub5rVAQdvaIZMifz4S2eljhh6P-sBD0vFA3FosN-EuFAKtN61_Pe0akUo3tCS15fzIlVHgukiTfj9olicsLGjLUEPT3kjZHynTiiKXattQoCiOb4yYnYj3iJvGEegFlPfcVhCP1I_mCa_j_HI41ri3e-59Kgft3czIpotWdqQdaCzaXJEqTUqjJsEMrpFzYoDvgXGpjkg1xzEte1Nf3KJsS99YDstxrfVVsO0PS-mozKrMyElfyCLDV5DF27BbJJ86RNriAJzmWtH3nw-9zitkC5xfqFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا پست ترامپ رو تو صفحه ایکس خودش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136118" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / خبرگزاری عراقی نایا:
ایران آماده حمله زمینی به کویت شده و هر لحظه شاید حمله کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136117" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c25773.mp4?token=YqLEPmTncBbCrk9Lu63sHdFfx8wy7fp0w9zsDib3y22OMt9JqAJCqS_4HimePMxVNHzh-oTQnuSjO0J_fTx8LjiB9fqnQ6LGLaTMcjQKTdfkx0H6JRT9FzGDX-ArdTEbVUA2gOTMhFLBNUhrdnW8R47N1LVgw8ZmWfXYF3qUTLlNkhJershN3INGZvnOAdE9kcGCJp88kvT0-TI36kyNjPjYfqSgB2g7O2dG2GR0K_dMqAkQII-CajMvWpGv6GGReLMVh_fWc1a7Kc-zF7OnEj1BsuEFiXxXboeaorau_DfGuS00Y75uKIbQi4xRH5vZMGeJ0Uq2b_flwghtYFDc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c25773.mp4?token=YqLEPmTncBbCrk9Lu63sHdFfx8wy7fp0w9zsDib3y22OMt9JqAJCqS_4HimePMxVNHzh-oTQnuSjO0J_fTx8LjiB9fqnQ6LGLaTMcjQKTdfkx0H6JRT9FzGDX-ArdTEbVUA2gOTMhFLBNUhrdnW8R47N1LVgw8ZmWfXYF3qUTLlNkhJershN3INGZvnOAdE9kcGCJp88kvT0-TI36kyNjPjYfqSgB2g7O2dG2GR0K_dMqAkQII-CajMvWpGv6GGReLMVh_fWc1a7Kc-zF7OnEj1BsuEFiXxXboeaorau_DfGuS00Y75uKIbQi4xRH5vZMGeJ0Uq2b_flwghtYFDc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری /
تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/136116" target="_blank">📅 20:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: جلسه کابینه امنیتی و سیاسی اسرائیل درباره ایران با حضور تمامی فرماندهان و رؤسای نهادهای امنیتی آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136115" target="_blank">📅 20:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYN-uuKbOxskyDU3LD0EI_Z_cqpG7ERyj2inVbIf0MYRadMjXB1ZL4T8eyraTNK9rXrc1jORMXT_NU4832gQL7Sc3WV4I62NpqS3nWKaL25xL_NGZMU-8GeYuq__59PZToi7xzMwd8hAnGD0y5Fz28rrSHk3oqp3q5AyRqkWQuxSd7P8kUD8igT12Gh3ZzocCXjrTUSdJJInQuPrnCCcOykuUtOpR8uLirb_IpeZ41djRlKvyLtMF2PPI8bhqsd9UVJ1hwsgFKCxmpGo1T-4_6t0urbMjGaelioynh0ZIb2S4BRWFcTtn_vtNGUA11LToPxOD7llAdnX5Ypf49b_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، از طریق شبکه Truth Social: نتانیاهو به هیچ وجه، تحت هیچ شرایطی، در ایالات متحده آمریکا دستگیر نخواهد شد.
🔴
او در حال مبارزه با جمهوری اسلامی ایران است، کشوری که اخیراً ۵۲۰۰۰ معترض بی‌گناه را به قتل رساند و در طول ۴۷ سال گذشته، سربازان آمریکایی و دیگران را به قتل رسانده است.
🔴
تنها کسانی که باید دستگیر شوند، افرادی هستند که ایران را به این گرداب بی‌سابقه مرگ و ویرانی سوق دادند، چیزی که سال‌ها پیش، توسط روسای جمهور پیشین، باید به آن رسیدگی می‌شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136114" target="_blank">📅 20:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر کشور پاکستان: امیدوارم وزیر کشور ایران خبرهای خوشی به همراه داشته باشد
🔴
محسن نقوی، وزیر کشور پاکستان با استقبال از اسکندر مؤمنی، وزیر کشور ایران و هیئت همراه، نسبت به این سفر ابراز خوش‌بینی کرد.
🔴
او گفت که امیدوار است وزیر ایرانی «خبرهای خوشی» به همراه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136113" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پوتین رئیس‌جمهور روسیه فرمانی را امضا کرد که بر اساس آن مقررات ورود بدون روادید شهروندان چین را تا پایان سال ۲۰۲۷ میلادی (دی‌ماه ۱۴۰۶) تمدید می‌کند.
🔴
عبارت تا ۳۱ دسامبر ۲۰۲۷ جایگزین عبارتی در فرمان قبلی شد که تا ۱۴ سپتامبر ۲۰۲۶ میلادی (۲۳ شهریور ۱۴۰۵) مجوز ورود بدون روادید شهروندان چینی را صادر می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136112" target="_blank">📅 20:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnWy-vlWUHZvG5Y6AmzJ1aU2y6jeOVbtKT9vZATQ2ebPyntBnSGcHhdutiQFymOrM8FwXU3zLAw1_YLCv1xD44aiTohn_X7sTEg2XvaVjH4ZcBNObOablHUiiAh_WsxLJ6mXKFpzAZBIXlRMRjUOgSqpA3kcmOZzOSEZ19pxxUkeJ_jGC222Ho135XPTimgaL1-ty7VsLtgQKHM1jcsvHKF_UVCoXAJGI3wGx5s7GbeyRqj6QVMYcC3QX84aOlb7prO2RA6V2tPoCYOUStyjNTk_cy2aWs2E4WoypNMgkfBq-cp5TZwtFBr_vqxZdTmt9mHF1fj9MmNYIz4SuFe59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
🔴
این دستورالعمل به پیتر هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136111" target="_blank">📅 20:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تعلیق پروازهای ایرفرانس به منطقه
🔴
این شرکت هواپیمایی اعلام کرد که پروازها به ریاض و از ریاض تا ۲۵ ژوئیه و خدمات به دبی و از دبی تا ۲۸ ژوئیه را به حالت تعلیق درآورده است
🔴
همچنین تعلیق پروازها به بیروت و از بیروت را تا ۲ اوت تمدید کرد، این پروازها از اول مارس به حالت تعلیق درآمده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136110" target="_blank">📅 20:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روسیه: اوکراین به دنبال بی‌ثبات کردن بازارهای جهانی نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136108" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqpDSxohTgDB2RK0pP0CpxVFSsszXuFgE3r9sGO_xf5hrOScIeCDWZpKZbak6_VHxsBtjhwMVh9kFnkrYWsceWBkz6hojG7w1nV4q-Vm1Ag1kMddNc8Z6n50jbZnrIr_quf3AYMaYLSlBA5U1I7DhTc0r2sd1T5OXnlPq9JWLmRVlHnKxi05C3PUOBUFsqCfavoP546tun3R1ETWi4IPXpdCEqkv-Ig6gBXkPMQJRwCxdeD0Xr8jvbPliI_OFGnWvgGVbqq39Z-I-Cr_dZyLzANobmfsNW_dyRAFYSrV_ENQvripqGSgXoqCWqcBWK6aYS21E70F7g40ceNv8T6TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع: تصاویر ماهواره ای تایید می کند که سپاه به پایگاه "برج 22" ایالات متحده در شرق اردن در مرز سوریه حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/136107" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیویورک‌تایمز: «اردن» به کانون تازه رویارویی نظامی ایران و آمریکا تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136106" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یان برمر تحلیلگر و مدیر موسسه تحلیل ریسک اوراسیا گروپ:ایالات متحده می‌تواند تنگه را با هزینه‌ها و پیامدهایی برای همگان محاصره کند، اما بدون یک توافق نمی‌تواند تنگه را باز نگه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136105" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداسیما: چندروز پیش این ما بودیم که آتش‌بس رو نقض کردیم و آمریکا بعدش به سیریک حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136104" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136103" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری مدل "گران-4" متعلق به روسیه امروز به یک قطار اوکراینی در نزدیکی ایستگاه راه آهن سولنویه در منطقه زاپوریژیا حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136102" target="_blank">📅 20:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
ما رو از جنگ نترسونید. ما جنگ رو به چشم دیدیم. تو شهر و محله‌های خودمون. تو ۱۸ و ۱۹ و ۲۰ و ۲۱ دیماه.
🔴
تو کدوم جنگی اینطور رگبار مسلسل رو به سمت مردم بی‌دفاع میگیرند؟ کدوم دشمنی بجز جمهوری اسلامی ممکنه اینطور مردممون رو قتل‌عام کنه؟!
💔
صداها رو گوش کنید. رگبارها کلاشینکف است. تک‌صداها قناصه. با هر کدوم از اون گلوله‌ها مغز و قلب یک جوان ایرانی را متلاشی کردند.
🤔
ما ملت ایران یک دشمن داریم و اونم جمهوری اسلامیه به همراه طرفدارهای حرام زاده اش. دشمن دیگه‌ای نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136101" target="_blank">📅 20:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136100">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/136100" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136099">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdjSUNPjxeAHtBi7cxnVK6TAkALMwwSokbEe5DiVblMRf88Uepxku-1AdyiseUUNgN5yPXbgUhUgSUOASzc5t0mKf99IPgW4PI5aoKYIJGrisiN1uhptyZksqINsN-859eP-wTpBqu7ntKiQxEEm56rdwkkMIOvFK8FyySxq9xqW2gpkFBRIfXBM8ip93kK7MqYvVEuCWYaPGfLxr_S_wyDvp92IhSY81KMjyyQT4wm1ilgKCMbAn6XJ4u0249Ow3WuvS024D_8kXd80T09R_KI8cA1caalbXN-yg8v4MJxjhFsXGCgBHM5qbEuxWDllsobsh9eFYRJphCIDLhBQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دمای ثبت شده در شهر های ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136099" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136098">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
توانیر: بین ۷۰۰ تا ۸۰۰ هزار ماینر غیرمجاز کشف نشده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136098" target="_blank">📅 19:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136097">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136097" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136096">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/136096" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136095">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuxgLRSofXKEqMr4lsfwXNILDQnFxA8gzkjlWvbm3MYh8nzh1g89wrI8zdlPkRuAiIJ1LyS2lHxv-zk3zvTn1drQFeefU5BpAnu91SFcGnNK2-ng0hrqAmfzqdVHqZMQPssyyCAT5W1DG9aLuyH0frwRyciBq4nZFJQq26RZR0ZI5QmoCgEhiG7lVDJPGK_E407wfVPsjSfa2qEJXzFfYWIbCcd1qsOqupHmimcFRyBQ8Gbedzwgz9DpvYGHGA4xMxjoVik9AEMYXxrU3HPgCaZ5IdEB1bQxmztyhs0H1e8UKEuoD1ycBvTaFuBfqd52JMslAyv38guu0UZmcSMkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136095" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136094">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر حرکت ۷ فروند کشتی تجاری را تغییر داده و یک فروند دیگر را از کار انداخته‌اند، از زمانی که این کشور محاصره بنادر ایران را از سر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/136094" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136093">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFWJk3ACWC6uiXaua3KacaXvI-9ipebYGKeRq-UB_5XBHeDBGNvH7IVZF4o7kXQE1CGhKBIOlBvamDRrvjfrI81gwyUAK3N8pnykwiU-9wDFPV75kesmYASujbfKNH2tkHwPADW0gVRplyryUL--BxfheDkj483tsiRLfvoVC_KmuCSDjs90DyKfR31eFaqOzx90dyJuweLSqoX9bCuRRvH3P8EOzUp-BwIlNgpiQr-iIbfmxTHNxWiR6GU2OxbJJSYBMEEXWXYtEY5_0Mqdsgw8bU-Ytl1LIE1OnMcUWPYU2kbJ_DOgS18SyDDNWaSkiT5ylxxHWSI6ji_x_4Cvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: آمریکایی‌ها با قاطعیت از توافق صلح ایران حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/136093" target="_blank">📅 19:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136092">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: میانجی‌های جنگ آمریکا و ایران در تلاش برای پیشبرد آتش‌بس جدید
🔴
قدرت‌های منطقه‌ای با نگرانی از افزایش خسارت‌های اقتصادی و خطر تشدید درگیری‌ها، در تلاش‌اند زمینه دستیابی به یک آتش‌بس جدید را فراهم کنند، اما همچنان با چالش همراه کردن طرف‌های درگیر با این روند روبه‌رو هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/136092" target="_blank">📅 19:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / صدای انفجار در سیریک و غرب شیراز شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136091" target="_blank">📅 19:31 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
