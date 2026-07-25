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
<img src="https://cdn4.telesco.pe/file/gGqzAfwT_q-OmEUkRMRaUVE7hAV667MKtdi4Z_LS0S4J-0J-gmPaKcgHIVEbI2mmtcJa1KjHQ2W9JH6gwvCuARQt1UN0kBclRMU3u6fRZ-SyT6_XV3N-ojir149mFMr9BWPaQITHvI8b0NZfUT0GJO6Jd3Cd2omQdh9aeq_jTDvQfNySwCy2zaVbWqVe4Pz01Kr_9MxECGJp88YJibIeux4FTF0F3RvNieljWeQorObpFmbTsvzFz6L39rrUWqakfYdSk6l1eFdRbzP9wWmfVlYV55T1dzgA7_5iSJeScCETehwJpRh0NzFpWiiCpiEsX7NiErNIvOTP78kSKctPiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 02:57:18</div>
<hr>

<div class="tg-post" id="msg-675306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع یمنی از تجاوز جنگنده‌های سعودی به حریم هوایی استان صعده در شمال یمن خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/akhbarefori/675306" target="_blank">📅 02:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
برخی منابع از شنیده شدن انفجار در اربیل واقع در شمال عراق گزارش می‌دهند/ جزئیات بیشتری هنوز منتشر نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/675305" target="_blank">📅 02:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675303">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d261d61d47.mp4?token=qZhC2M702THPAUcI3YiSaocPgj5b6YRtELJ-vQ53XuBo1FLzmV-DHlQg9egM5-JERXF9SlsW7M0QmL9AlmRKqDXjMLjjOzPNz-Wu8V_F_XM2ShzYA4S-Qol1JyBSc7rJcI-SdrglfknJWH7P8A9Ho4afQIHxz7Rpy3uPGwJiEZwC3GuMOz1C2Z4ZV5s-dIlUNTtXGVXpfk6eZbaIHyX9uj9AqSDuGwDCaeUuEGosJ1EloWLZoZNxNVigko7UgVIETY3x_W1wmht85mZAJcEYG8oKjAKCWqGxJl-Jl98S4CrnBRzKQmQPfm2o2K9X15RI9Oj0vK003lhtJVY639pkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d261d61d47.mp4?token=qZhC2M702THPAUcI3YiSaocPgj5b6YRtELJ-vQ53XuBo1FLzmV-DHlQg9egM5-JERXF9SlsW7M0QmL9AlmRKqDXjMLjjOzPNz-Wu8V_F_XM2ShzYA4S-Qol1JyBSc7rJcI-SdrglfknJWH7P8A9Ho4afQIHxz7Rpy3uPGwJiEZwC3GuMOz1C2Z4ZV5s-dIlUNTtXGVXpfk6eZbaIHyX9uj9AqSDuGwDCaeUuEGosJ1EloWLZoZNxNVigko7UgVIETY3x_W1wmht85mZAJcEYG8oKjAKCWqGxJl-Jl98S4CrnBRzKQmQPfm2o2K9X15RI9Oj0vK003lhtJVY639pkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سرباز کویتی که از شاهدان عینی حملات موشکی ایران است، می‌گوید: موشک‌های ایرانی بدون هیچ تلاشی از جانب پدافند آمریکایی، به هدف خود اصابت می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/675303" target="_blank">📅 01:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675302">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع یمنی از تجاوز جنگنده‌های سعودی به حریم هوایی استان صعده در شمال یمن خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/675302" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675301">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تجاوز صهیونیست‌ها به جنوب لبنان
🔹
برخی منابع از حمله هوایی رژیم صهیونیستی به منطقه «النبطية الفوقا» در جنوب لبنان خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/675301" target="_blank">📅 01:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515003979a.mp4?token=I0GessnClZlXLWwaLGj_3pSsdU9PcniJaHPwSFPKQHWoV5ZH2V6LkBDTWY9goVYKaABkwGhpmcELHEX9XWmlRBLv_wSMjDqClYuNytMuTk1sh3xvmGBdV0ZWS0gCr29W1Q-RWjzc3ouqi4KQgyIRgk-9_h2Qy1yXUV1zkp6nPTzB-f1j0PUrGjqeoMbP1zoZEP67OKzWoutEe3o9e-cEQRhVTrjFaW8Q4A-jie4mWZnQQPA3eiZ9XHbd9v6W5T6N2ai3FmpfbTWRvm_rLfQIwZUModSgfpixZ0LZurcvVJTEj2TPOkuHXaIjqg8lkWFMj_1OBBc0lBkA2e_BHyPNTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515003979a.mp4?token=I0GessnClZlXLWwaLGj_3pSsdU9PcniJaHPwSFPKQHWoV5ZH2V6LkBDTWY9goVYKaABkwGhpmcELHEX9XWmlRBLv_wSMjDqClYuNytMuTk1sh3xvmGBdV0ZWS0gCr29W1Q-RWjzc3ouqi4KQgyIRgk-9_h2Qy1yXUV1zkp6nPTzB-f1j0PUrGjqeoMbP1zoZEP67OKzWoutEe3o9e-cEQRhVTrjFaW8Q4A-jie4mWZnQQPA3eiZ9XHbd9v6W5T6N2ai3FmpfbTWRvm_rLfQIwZUModSgfpixZ0LZurcvVJTEj2TPOkuHXaIjqg8lkWFMj_1OBBc0lBkA2e_BHyPNTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌هایی بین نیروهای یمنی و گروه‌های وابسته به عربستان سعودی در استان الجوف در یمن رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/675298" target="_blank">📅 01:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای سنتکام: محاصره دریایی آمریکا علیه ایران همچنان به‌طور کامل برقرار است
تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی آمریکا (سنتکام) اعلام کرده است که:
🔹
۱۲ کشتی تجاری را که تلاش کرده‌اند محاصره را دور بزنند، تغییر مسیر داده است.
🔹
۲ کشتی را که از دستورها تبعیت نکرده‌اند، از کار انداخته است.
🔹
۲ کشتی دیگر را برای اطمینان از رعایت کامل مقررات، مورد بازرسی و توقیف موقت قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/675297" target="_blank">📅 01:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi_zE3wLYLI_G1SBtWsmryNnQhlxC8OLoAgo6oTAf9_K-lafZxZo0tBM2KD07PI4UVIdzDWuRd_2JS4I0uH11peCKL3NyY0svsXqZmKpHHmjkHH53IxZvrfqp71IB-dxRg7hAg3wuSHAfJYCiiSMd17n0aEKt1ZMASVT3zkkMNs5Q2leIJLSBjW_pTomhuPE7mtOfjEfkBdrvwZIVnHgX0_EYDH6CUPE8Evk-YisD98YoWFJmCF7G0GcimqFzp6EtpQ45l1rBijsbP4abKvxKjWyZiD7LUOsKCAYz6pXUCgi7g2Dc-wWMFn3TRhv9h-0AEzfWUpJr_PPJVmBM4Eeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر فروشگاه آنلاین داری، این پست می‌تواند هزینه تولید محتوایت را نصف کند.
قبلاً برای هر محصول باید:
❌
عکاس می‌گرفتی
❌
لوکیشن پیدا می‌کردی
❌
ساعت‌ها زمان صرف می‌کردی
حالا کافی است یک عکس ساده با موبایل بگیری…
رقبایت دیر یا زود از این ابزارها استفاده می‌کنند؛ سؤال این است که تو زودتر شروع می‌کنی یا دیرتر؟
@digitall_cast
ارتباط با پشتیبان :
@Digital_cast_support</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/675296" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533ce86674.mp4?token=fpxJJ5zoTixTPeHo_coSumC7RA7BMRsQ1oQ1bRN55DglUozDBBqtlwhuEykl825OF-66iEA54XUvx1axNccEGsK1x65EDFgZwZnvkDjwGiJO9j9PmLwa0VwDyh3urWLZ8-MZ75b16l6ZI6-4ktwmhlYeFWGSNmWqVLMFM8QCjP2lRND7IpXAOHMyQ_6nTdHk90DPqVRInfpAMRf9xhWzte7YSgUjoSGT8jolzzgHYKcRVh-IQPDPgTcJ0KLkMc0rD8Kq62PKnVbh2Uy1i2vy3inZYe6x2PWkwB6JqBrwp_PFSEXP-LgluvMix5ELj6jzMk9et7s5z6xLkE1FZ54L3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533ce86674.mp4?token=fpxJJ5zoTixTPeHo_coSumC7RA7BMRsQ1oQ1bRN55DglUozDBBqtlwhuEykl825OF-66iEA54XUvx1axNccEGsK1x65EDFgZwZnvkDjwGiJO9j9PmLwa0VwDyh3urWLZ8-MZ75b16l6ZI6-4ktwmhlYeFWGSNmWqVLMFM8QCjP2lRND7IpXAOHMyQ_6nTdHk90DPqVRInfpAMRf9xhWzte7YSgUjoSGT8jolzzgHYKcRVh-IQPDPgTcJ0KLkMc0rD8Kq62PKnVbh2Uy1i2vy3inZYe6x2PWkwB6JqBrwp_PFSEXP-LgluvMix5ELj6jzMk9et7s5z6xLkE1FZ54L3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ۴ سرباز به هلاکت رسیده جدید آمریکا در جنگ با ایران  سی‌بی‌اس:
🔹
یک سرباز ۳۰ ساله آمریکایی آخر هفته در عراق در جریان آنچه آمریکا انفجار کنترل‌ شده برای انهدام یک پهپاد تهاجمی اعلام کرد، به درک واصل شد.
🔹
پنتاگون اعلام کرد گروهبان مایکل امانوئل سوینتون…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/675295" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675294">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1059e02fca.mp4?token=Yx4hdrY8N0irTNQTRmImdUCUw_dmT5WVKIx7GjQ-_gmpWpUS7jDyvSokP4g4s6T2kvev1LmFLYPoLmNMJKaTvWf4MeuGssufReJg7RCYBlUK20x09ej7c8EE7DTxo8UOzLzfnYX174iQXtmBODcXF3RRGkydgG2n9O65WNlt3zH5vpdCqMNWuS5xeBCX-g7kwQVXXUeTwSJC-1XXDfi69FBe-OwC8ycIDhL0z9Bh27MIsPmT3mdtMFxMngHVRbToXHCeDrK_sGvXTZpbdnufC4H_k4tiaPhMeqAPY9XACFgl4gBlOLw7vLclkRdnqnDYW-6yPVBOFF5e6dl8NB_PQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1059e02fca.mp4?token=Yx4hdrY8N0irTNQTRmImdUCUw_dmT5WVKIx7GjQ-_gmpWpUS7jDyvSokP4g4s6T2kvev1LmFLYPoLmNMJKaTvWf4MeuGssufReJg7RCYBlUK20x09ej7c8EE7DTxo8UOzLzfnYX174iQXtmBODcXF3RRGkydgG2n9O65WNlt3zH5vpdCqMNWuS5xeBCX-g7kwQVXXUeTwSJC-1XXDfi69FBe-OwC8ycIDhL0z9Bh27MIsPmT3mdtMFxMngHVRbToXHCeDrK_sGvXTZpbdnufC4H_k4tiaPhMeqAPY9XACFgl4gBlOLw7vLclkRdnqnDYW-6yPVBOFF5e6dl8NB_PQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری در برلین در پی حمله با خودرو
🔹
در پی زیر گرفتن مردم با خودرو در برلین، وضعیت اضطراری در این شهر اعلام شد؛ گزارش‌های اولیه از مجروح شدن ده‌ها تن حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/675294" target="_blank">📅 00:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675293">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رسانه‌های عراقی از وقوع انفجار در یک شرکت سرمایه‌گذاری اماراتی در استان سلیمانیۀ عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/675293" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40532c012e.mp4?token=Bdw3BlebjSDQCPZ5jYCGgcwoKJVWA7ygQ7JWtdw2FEhQK_GGCWVehwrsaNK7jRZac8MWLsluFgZqrv9gwricrZ72_3KBZRnn_chC5VABAFQx_ZsAighSSIEsGpKLm1O9zsIXKXOuneAICZUYpQk6TN5jCsW84Kn_pnejuQw7yEcjwL4gII9t_MTrhrp1MNL7uQQG7GObL9S0KQ9eHsKA2XDUpg1Z9XmaQ7b4z40PmuV4zDAEBqwEd-mxFdSfpXtd90yII4eGj16Z_cz0azVYzZNvwVsDUS7OYiL7gZIsIHfupPzN3rE9YxW4XO7aGVa8yGkviILsNYzqyWFvOTbScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40532c012e.mp4?token=Bdw3BlebjSDQCPZ5jYCGgcwoKJVWA7ygQ7JWtdw2FEhQK_GGCWVehwrsaNK7jRZac8MWLsluFgZqrv9gwricrZ72_3KBZRnn_chC5VABAFQx_ZsAighSSIEsGpKLm1O9zsIXKXOuneAICZUYpQk6TN5jCsW84Kn_pnejuQw7yEcjwL4gII9t_MTrhrp1MNL7uQQG7GObL9S0KQ9eHsKA2XDUpg1Z9XmaQ7b4z40PmuV4zDAEBqwEd-mxFdSfpXtd90yII4eGj16Z_cz0azVYzZNvwVsDUS7OYiL7gZIsIHfupPzN3rE9YxW4XO7aGVa8yGkviILsNYzqyWFvOTbScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک میدان نفتی در کرکوک عراق
🔹
برخی گزارش‌ها از وقوع انفجار مهیب در میدان نفتی «جَمبور» در استان کرکوک در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/675292" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6552d0ad6.mp4?token=htQeoAunFp27tD3yDo4-HG1Jj624WuWxPsKVkUbM-OsLwBkqJALq78_lPvGzwTNtpepJ6cdPdl6Fn8Z4ZoFbzpn9_JEN-eMuL9JjAq4qaJSJOXX60_MbhaWX56Fln4O0yg7E9f4yCpKtWahk26ZV4gm2D7l1QEiMOIs9w_fWuygaP9lOFTXzr-tC8VPc7_ZsdhzvvltDaCElrMvi9VU4255BjWue-xFVrYJT2LIbnhyX7Cux5-fGG4sIISpGMNIH9bZLUN2c_RGaUSyWkAZ3KUg1e6gRgG_ToS4JdhrompxxQH0-uHMB7p8AkGshtm2JwlhEnz6-RZMp1f5MuFjbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6552d0ad6.mp4?token=htQeoAunFp27tD3yDo4-HG1Jj624WuWxPsKVkUbM-OsLwBkqJALq78_lPvGzwTNtpepJ6cdPdl6Fn8Z4ZoFbzpn9_JEN-eMuL9JjAq4qaJSJOXX60_MbhaWX56Fln4O0yg7E9f4yCpKtWahk26ZV4gm2D7l1QEiMOIs9w_fWuygaP9lOFTXzr-tC8VPc7_ZsdhzvvltDaCElrMvi9VU4255BjWue-xFVrYJT2LIbnhyX7Cux5-fGG4sIISpGMNIH9bZLUN2c_RGaUSyWkAZ3KUg1e6gRgG_ToS4JdhrompxxQH0-uHMB7p8AkGshtm2JwlhEnz6-RZMp1f5MuFjbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت پدیده نادر «شبح بروکن» در روسیه
🔹
در کوه‌های اوستیای شمالی، سایه یک انسان همراه با هاله‌ای رنگین‌کمانی روی ابرها ثبت شد.
🔹
این پدیده نوری که «شبح بروکن» نام دارد، زمانی رخ می‌دهد که ناظر از بالای کوه به پایین نگاه کند و سایه‌اش روی مه یا ابر بیفتد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/675291" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انفجار در یک میدان نفتی در کرکوک عراق
🔹
برخی گزارش‌ها از وقوع انفجار مهیب در میدان نفتی «جَمبور» در استان کرکوک در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/675290" target="_blank">📅 00:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
عراقچی: اروپا، اوکراین را پاسخگو کند
🔹
وزیر خارجه ایران در گفتگوی تلفنی با مسئول سیاست خارجی اتحادیه اروپا  ضمن محکومیت شدید و قاطعانه حمله نظامی رژیم اوکراین به یک شناور تجاری جمهوری اسلامی ایران در دریای خزر، خواستار واکنش قاطع شورای امنیت سازمان ملل متحد،…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675289" target="_blank">📅 00:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd_Wqjt4JRhRxFc_nDMXsTDcq9uHGDNHywbl88cA0eJpHtshyyRC91mGyyK2Mkfoni0QtEnNnzi5Ov6Hm10BFpMUEHbxlhuddqHAzUqD2iWM9EgZdTGzqPvl-I_DsKxW8z1nhCB4kCqER2ogdnAG57D0p1SrQ2HN0N1Zk5WGGqxgmCZeZMcqvNxwG8s4DjtEdCbFLjF-lFQDQ6JJCYyVXsEkw0cSuaS_SdAxtjxbeH9UAsIpET6SKYvoDOPUG6m3nYA7PVsM_tdTp5LtjxnfFK92pSe5jLHuP-jlvAotBV8CNMry24cIN0dSWM1TF5h2TxdLIAUE_Rw92Kv-XxikJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/675288" target="_blank">📅 00:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منابع عراقی
:
در پی حملات اخیر ایران و برای چندمین بار پیاپی، سفارت آمریکا در اربیل هشدار شدید امنیتی صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/675287" target="_blank">📅 00:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675286">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdBDB1_EgPKt4kiYp28Paio8_A2Uhho5QBYSY5V1eG2nReVf6YzvW7M6KfVoyjZKpuEmTkdhur_VArdCTfMJHwJKA3xsZrnDGpBinLjdfy3b_oV8Yl9J-s33YKn45heNGgqjjRjm-n5qWdEVjNpwOivPD1WWBZn_C1ksApPk4fvGP0EpTTcxYcVlZUlk7CT2fesbuvniR0deJVNPir9Y1OG9HscCqtZpPlwdq-lRLOE4OZJqKFlHsP_CdHPze-FwAPwR7J8lrMdeHn5oUso0tHMvaYRPZjXxkCb9Yox7c45P-WRgwciOvGZ9ETsf_1zUHLOJ4bFqNkCBYtjZestxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عروسی قرن در راه است!
🔹
رونالدو و جورجینا در ۱ آگوست رسماً ازدواج می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/675286" target="_blank">📅 00:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675285">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDVnCfD0InQQrhP3jBclQHHF6eu--1216-W_b66ch-90O4npe994Y4QKN3q_o5QGILN7g_XMPyvOoPQL3bhpveP0rhnQ1lfpPEf_fWYwwPsNgkiwto7oLiNLwbljRcoRwM8tYcNEwCv1PFCq45kYFKg75l-HQJQg_6r6TNUtXULgU2xDeReiQZ9pKuaJEozjeX-Hd6RVbGCeddP7YwrGlUK24ZeCeRHgYqXiPPn7SnxfBaaGqiX9KckjI8Sk1geOY7bSTZLrb4QAlmGTzrV5Jmigfb6l8tmKpK8FF1EdPRnHra3MTjgt0YatsB-IKlrIkfHOBSAebuHgbxT6W3l2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/675285" target="_blank">📅 00:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675284">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dMJvlN17xpPxMD0ruzIOMU_QU7TEohf9ZWc1uPLhOR1EuXiMBkENGviY8EP-oZHqEZm8LajrniDppPGNgBmroIhFv1k8YiL8qbHYL-Flq9qMS2U4_WHXTe8vpt7Qhjo0uaL84sNuVCABlaIs15UKoEP8BA4n1DqFI08P-UfXNCmwuJfvUoXIv4gb4my-mAgpSxdyN1hqQnU9eJWI4HVi_L0MTLyynSyYhcgXuXJf00t0KyBP_O6yUeNCjpEgw-BkZCbAlf8cd0XnsQ7S5YMDCGo8ACZynRZ1OZP2MKcYlqOgnAACxkjMx_qVoiNs47bevUGzyOCgdeUzQOZ-QfYcYGbwA5vbUA2ybqNawhyx5wxC9qhGdXhxsdge2pDdzJTfXN7niQeMuk4xBF_bg0VskCbsI8WLgw8Sa2ptFycIyQA_wK1hNg-IqTM56zXMq41EZwqsekgb_BTuSPf7s_FSWNtXNEYT3dQAOlPHzcnYTCgU5aGyPeMxMVo4395ZtNFCcY6ayyzwvw8aA1WZuHfIGm7S8EBpiZyWtNYgpe7JfOV_IsCVvzpLNKDjKsDoUYfcyangSg6yGBTGe4h5uI2H1z7Gc49Auh5CEzTzryeYQQObmUzYEGRKDx8YoG48cDJ12-bQcSLtEkT8E5JbBhVCfA0tSgJGOzz9taTB1yEcb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=dMJvlN17xpPxMD0ruzIOMU_QU7TEohf9ZWc1uPLhOR1EuXiMBkENGviY8EP-oZHqEZm8LajrniDppPGNgBmroIhFv1k8YiL8qbHYL-Flq9qMS2U4_WHXTe8vpt7Qhjo0uaL84sNuVCABlaIs15UKoEP8BA4n1DqFI08P-UfXNCmwuJfvUoXIv4gb4my-mAgpSxdyN1hqQnU9eJWI4HVi_L0MTLyynSyYhcgXuXJf00t0KyBP_O6yUeNCjpEgw-BkZCbAlf8cd0XnsQ7S5YMDCGo8ACZynRZ1OZP2MKcYlqOgnAACxkjMx_qVoiNs47bevUGzyOCgdeUzQOZ-QfYcYGbwA5vbUA2ybqNawhyx5wxC9qhGdXhxsdge2pDdzJTfXN7niQeMuk4xBF_bg0VskCbsI8WLgw8Sa2ptFycIyQA_wK1hNg-IqTM56zXMq41EZwqsekgb_BTuSPf7s_FSWNtXNEYT3dQAOlPHzcnYTCgU5aGyPeMxMVo4395ZtNFCcY6ayyzwvw8aA1WZuHfIGm7S8EBpiZyWtNYgpe7JfOV_IsCVvzpLNKDjKsDoUYfcyangSg6yGBTGe4h5uI2H1z7Gc49Auh5CEzTzryeYQQObmUzYEGRKDx8YoG48cDJ12-bQcSLtEkT8E5JbBhVCfA0tSgJGOzz9taTB1yEcb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/675284" target="_blank">📅 23:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675283">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: هیات عمانی تهران را ترک کرد، اما دیپلماسی متوقف نشده؛ این بار در سطحی بالا که ممکن است به افزایش امید‌ها برای یک راه‌حل مسالمت‌آمیز و دیپلماتیک و کاهش احتمال گزینه نظامی منجر شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/675283" target="_blank">📅 23:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675282">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ایران، تعرض نظامی اوکراین به کشتی تجاری ایران در دریای خزر را محکوم کرد  وزارت خارجه ایران:
🔹
مسئولیت پیامدهای ناشی از ماجراجویی رئیس رژیم اوکراین، برعهده آن رژیم و حامیان و محرکان آن خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675282" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675281">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
ترامپ دستور توقف تمام حملات به ایران را صادر کرد
👇
khabarfoori.com/fa/tiny/news-3233105
🔹
حمله اوکراین به شناور ایرانی
👇
khabarfoori.com/fa/tiny/news-3233113
🔹
بامداد مرموز؛ چرا آمریکا دیشب حمله نکرد؟
👇
khabarfoori.com/fa/tiny/news-3233081
🔹
تصویر گوگوش در آغوش اکبر عبدی
👇
khabarfoori.com/fa/tiny/news-3233085
🔹
تاخیر در گزارش سم‌شناسی لیندسی گراهام | آمریکایی‌ها روی مرگ گراهام مشکوک‌تر شدند
👇
khabarfoori.com/fa/tiny/news-3232948
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/675281" target="_blank">📅 23:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675280">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcddb9a3f7.mp4?token=Q-Z1nH1PgWL-lwG_zmOe-_NO5ppaxphLsYx-MH0HWE9Azc_xNnX0KKw57CsJJ7oiZAWwAO7GbWJI7v0ErXp0vk9Hy4LhD5kKQtq9FF0il_T__w36F4rOHLg1k38GfvXKduLUDFXs41ECrdRK5s3Jn4SdSVhReDGfEGMGFxmaprKaoSJdIZeBAwOo8RXM6BcVzva4WYpSDizT3Zjf460fu2h6zVgHr4uYhAnJHxpaj_nLMMKw4JppqGXW_C_xkIizfor2Ar436sElDlAxl65F-BcrOMb1Y_JirwnIMNrzZFpOB-v2EFw4spAL_MK7xbO_E6kLhZ5Pl7MIwoPC-XfTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcddb9a3f7.mp4?token=Q-Z1nH1PgWL-lwG_zmOe-_NO5ppaxphLsYx-MH0HWE9Azc_xNnX0KKw57CsJJ7oiZAWwAO7GbWJI7v0ErXp0vk9Hy4LhD5kKQtq9FF0il_T__w36F4rOHLg1k38GfvXKduLUDFXs41ECrdRK5s3Jn4SdSVhReDGfEGMGFxmaprKaoSJdIZeBAwOo8RXM6BcVzva4WYpSDizT3Zjf460fu2h6zVgHr4uYhAnJHxpaj_nLMMKw4JppqGXW_C_xkIizfor2Ar436sElDlAxl65F-BcrOMb1Y_JirwnIMNrzZFpOB-v2EFw4spAL_MK7xbO_E6kLhZ5Pl7MIwoPC-XfTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر ما ادامه آرمان آوینی‌هاست: اگر ما را با خليج فارس تهدید کنند، آن‌را گورستان شان خواهیم کرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675280" target="_blank">📅 23:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
برزیل از اعطای روادید به ۲ فرستاده دولت ترامپ که قصد داشتند از مقامات در مورد سیستم انتخاباتی سوال کنند، خودداری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/675279" target="_blank">📅 23:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
🔹
هر کشوری، چه انگلیس، چه کشورهای حاشیه خلیج فارس و چه دیگران، اگر در جنگ از آمریکا پشتیبانی کنند، هدف مشروع ما خواهند بود.
🔹
اخیراً هواپیماهایB1 آمریکا از فرودگاه‌های انگلیس استفاده کردند،…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/675278" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675277">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای کانال ۱۴ اسرائیل: ترامپ دستور توقف همه حملات علیه ایران را صادر کرد
./انتخاب
اخبار لحظه‌ای دور تازه میانجی‌گری‌ها
👇
khabarfoori.com/fa/tiny/news-3233105</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/675277" target="_blank">📅 23:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675276">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سخنگوی سپاه: انگلیس درصورت همراهی با آمریکا هدف مشروع ما خواهد بود
🔹
هر کشوری، چه انگلیس، چه کشورهای حاشیه خلیج فارس و چه دیگران، اگر در جنگ از آمریکا پشتیبانی کنند، هدف مشروع ما خواهند بود.
🔹
اخیراً هواپیماهایB1 آمریکا از فرودگاه‌های انگلیس استفاده کردند، اگر همراهی کنند، هدف قطعی و مشروع ما خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/675276" target="_blank">📅 23:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmqZSoJ0B39ODgALJzLqJTe7lxMe81MKtnWgoQ8kK30gzSYM4o7a-hF9xhVQHYmT9VNrMeQGVmQ1Hsv8T-d_g6sw32L7A3-fCvKVgBop3bjMfRE21Tilqi75_AHRU5s63rDcaazxGEiM0Wp39Acb0H2KDCzZMGb8ViRMaLgU2nkxFL2mMPh-J917BqE8FFkGKn7KV_FMHBgznhP9a-w5PmHQBH-KkI89q1YQKeHp5ezy4vtyrBlSSansULdys3LfjAnvvpOtj8cuJX2mButgeaJ2Qk2IPnlbwuv-Jq7pQAscBFxOjfZLGbiiJfBYXH9sX_5E4qBmCeWhNDHH8GdUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2j3vdW-E2sne5gptyPjPMxL4iI-hCLRJXa5KPKa2Bh7muVPwRXY3OJ_4Svh7gsCApGAwRcB1I-53xSXeycHk4pkLwfC1pXpqJJeJ9YobpaNcEyJxyaSRvfATMHdgXWfHKZw2mYUftcen_go5LO4UZVKMQuQbK2d0eYJmVtR1zcCwP4VRwHDUFXlOjm0-JFM2jho4YhHMaxGN5K3-0AB58ZahktUnzBCe19DkHLlVobl3KVjs76dUr6oOuLRb-mya4syhtavms5c37UgJqOvavSz1QNxg4CZQmtk3ED1qblfBi59vORHAosrhIraewaeRTyntf_P6Vb2nCIowziBEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/675274" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=YNNeak773NEhmSsGKGkpEiVjR1s6Y99-0O-do-yx06gUkBQOi_7Z1TnbkPLFCxpIGs_U7RlCdN0IhhxmlXJ0fDowjS-o6ZfOR08xf9FkCUFZZ5YcmQggHskUgjSva-qd3m6037lg6x6pGBIm9iyHGg5hqkhPou8BiEHC-KIkiUNtJi66VgiPZU2SQQNQpdlE7Co7xmAsgL1rmCejSxwOUFVdnrAbh-TLLID39Ap5j5gsC7PeVmTSEJ9VvH4HRKxejeeVa_pLwdgz3owvwj79kFQnqu_u67E7fdrF5QCLYeD-yhFvrooGzggOu32MACRsC0dgjuSOA26uTcMyI4m5Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c8107cff.mp4?token=YNNeak773NEhmSsGKGkpEiVjR1s6Y99-0O-do-yx06gUkBQOi_7Z1TnbkPLFCxpIGs_U7RlCdN0IhhxmlXJ0fDowjS-o6ZfOR08xf9FkCUFZZ5YcmQggHskUgjSva-qd3m6037lg6x6pGBIm9iyHGg5hqkhPou8BiEHC-KIkiUNtJi66VgiPZU2SQQNQpdlE7Co7xmAsgL1rmCejSxwOUFVdnrAbh-TLLID39Ap5j5gsC7PeVmTSEJ9VvH4HRKxejeeVa_pLwdgz3owvwj79kFQnqu_u67E7fdrF5QCLYeD-yhFvrooGzggOu32MACRsC0dgjuSOA26uTcMyI4m5Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس: بحث اصلی میان ایران و آمریکا، تنگۀ هرمز است/ هرگز تنگۀ هرمز به شرایط پیش از جنگ باز نخواهد گشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/675273" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6x2ZtrFSbQW0Cb6xbHW2LJ7q9eUQUd2dMmnkCkDdMNgboiS19Gd3a8EGBKG5nKSJfZRkiT_W0BD-6trtIZRgyZpwGbordO3tk3-QsrDpu529fr34HZocg1WLpSY_HBVXR6TkJl7ckTZaKqIkZoInIMepahnNHuu_sEF8_wa7qxSx7ztIowCKpb37l2zAh1FuOmoPmiHTyH0R47aK0KhCAQi_gIidNkYryWRahq4fMsPvsXu2MHqjCHrfpiD8ZCimBLz4Lpk03xmKOcxOwFfDLR4osHaW5FRz18lfcG_TmHsh1S7wRbXmM6i18sD5Zua-pAbad8kk1ztgm_r6Ob5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منزل «بن گویر» هدف حمله پهپادی قرار گرفت
🔹
رسانه‌های اسرائیلی گزارش دادند که یک پهپاد در نزدیکی خانه ایتمار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، اصابت کرده است.
🔹
جزییاتی از حادثه منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/675272" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EquFggwSrzdAu7YZ2a_JKzIf2kD-h7-xTzgxTjY_wKVDVvgnc4s9YooUXJcUxrbDc5I5V_XBIXB3-bSCVIPyNzBfymHY4-_pu4Hq8FTHaUjn_dT8r093ZMfJ3b_LReLYauWxrlPn8mLteMcE973YjnobDnq_rq6nhA5zxjZODzl80VbJo7LQFyV0XpVnjwz-syFR9zrCxnpoGzxhUkJZ00FcfiLlAgaMRLM726dddL2lAgdqCHWlLUu8ZJe8VxPSY8PbdTIx5KLCkyUMbM7nlccnncqMpPXmf6gbZO7Yp7X-6ivFGTAN61G_JUXhTJPxAp4uFPvcuMNRDzUwS64Uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چیزی که دیروز محل تردید بود، امروز به مرحله اجرا رسید/عرضه شمش طلا به دلخواه متقاضیان! چند وقت قبل، ماجرای شمش‌های طلایی که در فرودگاه خبرساز شد، واکنش‌های زیادی به دنبال داشت.در همان روزها، برخی با تردید درباره اصل ماجرا صحبت کردند و آن را صرفاً یک حرکت تبلیغاتی یا نمایشی دانستند.
اما حالا با گذشت زمان، موضوع وارد مرحله متفاوتی شده است؛ عرضه رسمی شمش‌های طلا آغاز شده و این محصول به شکل عملی در اختیار متقاضیان قرار گرفته است. شمش‌هایی که قرار است در وزن‌های مختلف عرضه شوند و امکان خرید، دریافت و حتی بازخرید آن‌ها فراهم شده است.فارغ از تمام بحث‌ها و قضاوت‌هایی که در روزهای اول مطرح شد، حالا چیزی که اهمیت دارد این است که یک ایده از مرحله حرف و ادعا عبور کرده و وارد مرحله اجرا شده است.در نهایت، بازار و مردم هستند که درباره موفقیت یا عدم موفقیت هر طرح اقتصادی قضاوت خواهند کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/675271" target="_blank">📅 23:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgurLKmyvGijpxeJ4HDoOwqgQNytV3Q3Z7mGMytKzBH1wicbmazj_c3Gmsi_ntrVL4pGr8X50fsmm1pPqOzk4ulkeq8YZb-obpcMxrnLTWRp6XtWgDO8Dh_g5_Z_PuHeiGTZN-5z_ozWhIN-uG9SWxekVcjPNqIcywRIfTyw9Ex5DYvLspyZOnDSKWqPq692mqmHylqqHBnJrVjSKyKhz2s0ClMeoUzOwQgm2rr9Sywhd1iHs44xUxzV0yHDo9zxdZ0sATguQ_51x7bdWBZD7dOKjK7vYNF82u1-7N6IwbKAtTtZ6qQX7nEef-KV9oFF3tVaRIRxIXEJODuCOVo-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه ویژه زائرین اربعین امسال
🕋
زائر گرامی، برای پیشگیری از مشکلات خروج از کشور و تأمین امنیت سفر، انجام ۳ اقدام زیر، قبل از حرکت به سمت مرز الزامی است:
🛂
۱. دریافت گذرنامه معتبر با اعتبار حداقل ۶ ماه
📝
۲. ثبت‌نام در سامانه سماح
📱
۳. ثبت شناسه تلفن همراه زائر در سامانه همیاب
جهت ثبت شناسه، فقط از طریق لینک زیر اقدام نمایید
⤵️
https://hamyab24.ir/l/qlx
https://hamyab24.ir/l/qlx</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/675270" target="_blank">📅 23:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
دونالدِ قلدر کانادا را به بهانه «سوءمدیریت جنگل‌ها» و آلودگی ناشی از دود آتش‌سوزی‌های فرامرزی، تهدید کرد
🔹
سگ‌زرد هشدار داد که هزینه‌ی این آلودگی را به تعرفه‌های واردات از این کشور اضافه خواهد کرد. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/675269" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
شایعه سقوط شیء در آسمان یاسوج تکذیب شد
🔹
در پی انتشار اخباری در فضای مجازی مبنی بر مشاهده و سقوط یک شیء ناشناس در ارتفاعات شهر یاسوج، معاون سیاسی، امنیتی و اجتماعی استاندار کهگیلویه و بویراحمد این ادعا را کذب خواند و تأکید کرد که چنین رویدادی رخ نداده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/675268" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b73b783e.mp4?token=vc6inaD7ZHTkqf0ft5t2jhGCU_AzT8rmomr7vFfiq9slx-oqihDY7C5WfhQqDkLHBF4GZpJpthTqWfQZmaHUfZsxX_DE-mGMwVN4erR_USGurH71ZT25AgL3_tNsrfFFbqdPYohff3YYIv6RCVi6nbl736g0AOZtaxYrPL5qCEwN3uFqN6c-HI6kXwwo7Wh-En-rIMYTk9JwyB6wqs4A0gQ_Jwh5W54_vw2hCJIda9lkpoR7m1UcE2EszerLFTqglJgiEuVQ9Cf0FOi50N9vEhxRZ6xkOT_38sr94Jz6gpvSd7K6xm3LoLyU4eWDftD32iLq-PstKP8vhpF8-dmtig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b73b783e.mp4?token=vc6inaD7ZHTkqf0ft5t2jhGCU_AzT8rmomr7vFfiq9slx-oqihDY7C5WfhQqDkLHBF4GZpJpthTqWfQZmaHUfZsxX_DE-mGMwVN4erR_USGurH71ZT25AgL3_tNsrfFFbqdPYohff3YYIv6RCVi6nbl736g0AOZtaxYrPL5qCEwN3uFqN6c-HI6kXwwo7Wh-En-rIMYTk9JwyB6wqs4A0gQ_Jwh5W54_vw2hCJIda9lkpoR7m1UcE2EszerLFTqglJgiEuVQ9Cf0FOi50N9vEhxRZ6xkOT_38sr94Jz6gpvSd7K6xm3LoLyU4eWDftD32iLq-PstKP8vhpF8-dmtig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از قاب‌های رهبر شهید در میان زائران پیاده روی اربعین در جنوب عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/675267" target="_blank">📅 23:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: برنامه امتحانات نهایی برگزار نشده و عقب‌افتاده پایه یازدهم در چهار استان اعلام شده و برنامه امتحانات نهایی برگزار نشده پایه دوازدهم نیز پس از نهایی شدن، ابلاغ خواهد شد
/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/675266" target="_blank">📅 22:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی ارتش: تمام پایگاه‌های آمریکا و ضدانقلاب در اربیل عراق نابود شده است
🔹
دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد.
🔹
در جنگ جدید از پهپادهای نسل جدید علیه مواضع آمریکا استفاده می‌کنیم.
🔹
پهپادهای نسل جدید از آرش ۲ قدرتمندتر و مخرب تر است.…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/675265" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2134834fc.mp4?token=PsxOwJFGPmw91lvBWKTcvd1bSnfV-Caet-ThJBACfrextSUJdzAQYviuCRwZfxQOroYz2hnShgay7c4zsB2o2dgqwwkqz1SFWQQ7AzzVSl0TOYUNyLbUeoQByoX_vs8alJbEfjg0EgqL_773e_NcoR49YWQ7lmNo4dnOhNznY4ogK9nmW0biRE2xKYcTbn7A7DBP0Q5WM84ouk9GwB_7I_5FWmFVtClz_BtLG7cF2j-uSg11bDTwGTXCxrpFFsrYHMnSyrVIk0ERgdvozsE5TvgwziFAnqXvZm_x6pemFsPXzQceEDZqjBcIWAD-8N5xhACmhnFbHeL8Dk0wjW9BLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2134834fc.mp4?token=PsxOwJFGPmw91lvBWKTcvd1bSnfV-Caet-ThJBACfrextSUJdzAQYviuCRwZfxQOroYz2hnShgay7c4zsB2o2dgqwwkqz1SFWQQ7AzzVSl0TOYUNyLbUeoQByoX_vs8alJbEfjg0EgqL_773e_NcoR49YWQ7lmNo4dnOhNznY4ogK9nmW0biRE2xKYcTbn7A7DBP0Q5WM84ouk9GwB_7I_5FWmFVtClz_BtLG7cF2j-uSg11bDTwGTXCxrpFFsrYHMnSyrVIk0ERgdvozsE5TvgwziFAnqXvZm_x6pemFsPXzQceEDZqjBcIWAD-8N5xhACmhnFbHeL8Dk0wjW9BLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از گریم‌های مختلف اکبر عبدی، مرد هزار چهره‌ی سینمای ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/675264" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
رئیس سازمان اداری و استخدامی: تا زمانی‌که قانون فعلی تغییر نکرده براساس اختیارات‌مان حقوق نیروهای شرکتی را به صورت مستقیم و بدون تاخیر به حساب‌شان واریز خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/675263" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr4GS9tuXHeNAwPujheXBn28Kn-fU-wE2zSVu7gAyHbUVYJYDHueGBtXff01JHeMWWgCOT8YmV5oOarqZRGV-GNTBTy4-iwf9HQKhohJceBRxxnrzIOL2Xr7wLbr-z1XypgXTnWEIltND7ecWnEFsgZoDEKoJhRsod8V05uF3jurYj2DG3uSKVHX53p1DstVYqTEFxq-OXd0uHwWmpfkJqfAKasV9vYR2T6UyfzoJmQmEvl_Mv_Y0f2Lt5fbk7GXZL-W1D84IyUH5T1_YjmykWKjOybmcDpNzZ9Px759BG9Y-O2ZJlz4AkDL05b0KtUKNfF1yWVHdCPc5Ha40BVbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه کارهایی مصداق کفر هستند؟
🔹
امام علی (ع) کفر را بر چهار پایه استوار می‌داند: عمیق شدن در وهم (کندوکاو در اوهام)، تنازع (ستیزه‌جویی)، زیغ (انحراف از حق) و شقاق (دشمنی و لجاجت). این عوامل، حجاب‌هایی هستند که خرد را از حقیقت بازداشته و انسان را به گمراهی…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/675262" target="_blank">📅 22:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc947bc56.mp4?token=fX_3eZGgoAkb7gDRQfJp-J6NcXXP3LvRUexSYFeW8ZAjTHxZT5J-NWL66SZSXpwvhSmf_Hvt41IKRr5VqtFin7U_NCSslTbDcjkPC6YVHi6sS-B5I1JwzCt8oglYfYdMC9Ki60Xyp0nZKBCfq4XFO04gXNRqf6emdGLhJjgD_LllLozQAu6D7qwgi4MzvgII_97Yom74_D9s0_l-em2-ivdG-zY3bTdwoJTua8rjnObGm8kiC9phoR8TmpNCUHcsOd0Qlpfji3eTAKNaS8SnqrUqyN_CtxJfdjxIj8KGgOWgZTvCVsGzidAAq3jHo_69cXZcecyB4veX1Ms7VD6tuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc947bc56.mp4?token=fX_3eZGgoAkb7gDRQfJp-J6NcXXP3LvRUexSYFeW8ZAjTHxZT5J-NWL66SZSXpwvhSmf_Hvt41IKRr5VqtFin7U_NCSslTbDcjkPC6YVHi6sS-B5I1JwzCt8oglYfYdMC9Ki60Xyp0nZKBCfq4XFO04gXNRqf6emdGLhJjgD_LllLozQAu6D7qwgi4MzvgII_97Yom74_D9s0_l-em2-ivdG-zY3bTdwoJTua8rjnObGm8kiC9phoR8TmpNCUHcsOd0Qlpfji3eTAKNaS8SnqrUqyN_CtxJfdjxIj8KGgOWgZTvCVsGzidAAq3jHo_69cXZcecyB4veX1Ms7VD6tuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین وضعیت تنگه هرمز از ساحل بندرعباس/نورهایی که خلیج فارس را روشن کردند!
🔹
گزارش خبرنگار خبرفوری از قلب تحولات جنوب ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/675261" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmOs67eMvQTt1PBJAhKFwdmTH7eGSziikttlBFpAZfnQywlvLOrv5-mvTrr7yvDGSUATi8qIu2HSMJzPeaXgjPQ0L742ftE31cMxbKKqbw9Twlcxmz0cQW4GGxeJMeamQYCB7KUoMH1wGZpzDfoGMR79NjUS5xIHwPzQVsZlaGiazODPQi59zxPd8aOPfuFQRoC6TFZfRUe8MKWxW6TU-o4SjoTeyzrw1MfvJMIvmETX6I3ivUIOp4dJ-fqnp6D6088MpLTXe-PTg5ENCxBd9QzCVurCFkoOuuHvGppd0aL9LZZjbjJ-mylcjGhun472gMte0VNBquOjmIY6ENqFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای زلنسکی: شناورهای مرتبط با ایران را هدف قرار دادیم
🔹
رئیس‌جمهور اوکراین امروز در پیامی ادعا کرد «در حملات دوربرد خود در دریای خزر به نتایج بسیار مهمی دست یافتیم؛ از جمله شناورهایی که برای انتقال محموله‌های نظامی مرتبط با ایران مورد استفاده قرار می‌گرفتند.…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675260" target="_blank">📅 22:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0e668086.mp4?token=oR_dsxTT8abKGatN5EsnlNumWeCZqfLXGqgYUPKn4rSW7RcjMO4ajp9GT5w1RR0-O_ai-wNJWsRRWxY6Utq-3EuIOK_xijVI-pazAGnPgMkUjo9161Iid9EQA0ymOD_eMDcQEuynfZ0AS6PFPrORmqZw1QUVhncYB1Pqex2cgngpJBEwUeS1Wxro_HzYPiAamLbqw5c8tHcWaQXnNDsF4lrTnjF6ieZqW70OTNenf-Lz3Hwsh76AliV0Pnpg8BXAbgpF2OBOivbZBNgVYrgB1ap2NxSpNx7KDzPFAB4CvPJnX7mF2oLltx7FZJHsmMdQl0tHl9UKwoldxhsfQ-KyDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0e668086.mp4?token=oR_dsxTT8abKGatN5EsnlNumWeCZqfLXGqgYUPKn4rSW7RcjMO4ajp9GT5w1RR0-O_ai-wNJWsRRWxY6Utq-3EuIOK_xijVI-pazAGnPgMkUjo9161Iid9EQA0ymOD_eMDcQEuynfZ0AS6PFPrORmqZw1QUVhncYB1Pqex2cgngpJBEwUeS1Wxro_HzYPiAamLbqw5c8tHcWaQXnNDsF4lrTnjF6ieZqW70OTNenf-Lz3Hwsh76AliV0Pnpg8BXAbgpF2OBOivbZBNgVYrgB1ap2NxSpNx7KDzPFAB4CvPJnX7mF2oLltx7FZJHsmMdQl0tHl9UKwoldxhsfQ-KyDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی به مریخ از فاصله ۵۵ میلیون کیلومتری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/675259" target="_blank">📅 22:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای کویت: هیچ حمله‌ای به خاک ایران انجام نداده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/675258" target="_blank">📅 22:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn-2RKxEVW2uQmsCxOdRyIQ2V1gt2cIDMPBo_Mm8CyF2P0G2m8IsGOkOcW5kZNcZbdTW4mKLRerUEW16HeXWc6-miMYy92e0UQ4yu3tAZussKFVkULezlKkCVBjCO21CdymIyT18wt1Zp7owG7CrH8L0wyAs-6lDIEbaHuppykOq_dJFBkd1NrsrMjFYCpA6OaHGLE2RKj1a1QMSnckd9tIrAe_BGwJEIbcBkDGGK5t1LsJG2AQKiO-W7ZLIx_e2Q1Y5-E8yWYDvTv5qWRrVIV41XG8BmxGU0r_wi4k3ANxhW8As4c7Kkg-B1f7k-7FHhTOYG0WAlOlu_zeymSIh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKsEu-fnruufu9i9T0jg-NXad0K4YhJPotFt7u1iLp7xbijBtaYok8IleIixYsToROYf8f3K2W368wl759PNQSxXTQb4fvJ-SRO_sT046fIqFQ42v3aEpXkA5sawQ2VYcb0eBLlNRnHXshSyWJ29_Yny2JgxKxlfUhWA59CyGzoaAhCjMO1Qgvy1ffxmiOmMcShTUVoHIilq0qS--KbiiU48Ju29PexwbOkXL_62rCxZZh7knfVxSnfdsfbVX5f5ydvpKSSXxFwz1ag1ubbEJbgI6rK0twCUyCdb0DPD95ECLbpvGaXZpqB4aLjXT0OHFyzdAAxGfnS28okKH0_6tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان وابستگی کشورهای حاشیه خلیج فارس به آب‌شیرین‌کن
🔸
کشورهای حاشیه خلیج فارس بخش عمده آب آشامیدنی خود را از طریق آب‌شیرین‌کن‌ها تأمین می‌کنند.
🔹
در قطر، حدود ۹۹٪ آب آشامیدنی از طریق آب‌شیرین‌کن‌ها تولید می‌شود که بالاترین میزان وابستگی در میان کشورهای منطقه است.
🔸
در مجموع حدود ۴۰۰ واحد آب‌شیرین‌کن در کشورهای حاشیه خلیج فارس فعال است، اما تعداد تاسیسات بزرگ و اصلی در هر کشور محدود بوده و بخش عمده ظرفیت تولید آب شیرین را همین مجموعه‌ها بر عهده دارند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/675256" target="_blank">📅 22:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: امسال استخدام گسترده‌ای نخواهیم داشت
🔹
در استان‌هایی مانند تهران، شهرستان‌های تهران، اصفهان، مشهد و شیراز کمبود نیرو وجود دارد اما امسال برخلاف سال گذشته، جذب گستردۀ نیرو انجام نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/675255" target="_blank">📅 22:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رئیس کل دادگستری استان هرمزگان: مسیر تمامی تونل‌ها، پل‌ها و جاده‌های بمباران‌شده، ترمیم، بازگشایی و آسفالت شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/675254" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سخنگوی ارتش: تمام پایگاه‌های آمریکا و ضدانقلاب در اربیل عراق نابود شده است
🔹
دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد.
🔹
در جنگ جدید از پهپادهای نسل جدید علیه مواضع آمریکا استفاده می‌کنیم.
🔹
پهپادهای نسل جدید از آرش ۲ قدرتمندتر و مخرب تر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/675253" target="_blank">📅 22:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
«اشک میناب» منتشر شد / تازه‌ترین تولید موسیقایی در سوگ فرشتگان دانش‌آموز
🔹
همزمان با تداوم آیین‌های تشییع و خاکسپاری شماری از پیکرهای مطهر دانش‌آموزان شهید میناب، بنیاد رودکی قطعه موسیقایی «اشک میناب» را به همراه نماهنگ این اثر منتشر کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/675252" target="_blank">📅 22:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
فرمانده نیروی قدس سپاه: رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به حق و انسانی برای مردم مظلوم این کشور است
سردار اسماعیل قاآنی:
🔹
رفع محاصره ۱۱ ساله یمن، مطالبه‌ای به‌حق و انسانی است.
🔹
عربستان باید از رفتارهای پرهزینه آمریکا عبرت گرفته و به محاصره ۳۸ میلیون مسلمان یمنی پایان دهد.
🔹
شایسته است عربستان به‌جای فشار بر یمن، توان خود را صرف حمایت از مردم مظلوم فلسطین و غزه کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/675251" target="_blank">📅 22:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای سگ زرد: اگر به ۱۰۰٪ خواسته‌هایمان نرسیم، به جنگ باز می‌گردیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/675250" target="_blank">📅 22:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
تظاهرات گسترده در انگلیس در اعتراض به همکاری با آمریکا در جنگ با ایران
رسانه ITV:
🔹
معترضان خواستار توقف استفاده از پایگاه‌های نظامی انگلیس در جنگ آمریکا و ایران شدند.
🔹
معترضان ضدجنگ در مقابل دروازه‌های اصلی پایگاه هوایی نیروی هوایی سلطنتی در «رف فیرفورد» (RAF Fairford) تجمع کردند و از نخست‌وزیر، اندی برنهام، خواستند تا استفاده از پایگاه‌های نظامی انگلیس را در جنگ آمریکا با ایران متوقف کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/675249" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW64CMA86goNged9MPIascjrbukF8aFaAD0Zu2YjRtPEKHZrt_w24DbVGS2epwFNUyex4e9he-ap4KiUaeHqIye0c-BQMALCwIY-qABOdxwohCvG9vfMFHQ535v7h-whNTX3Ub83i4El6doXM10uynd9DOct0dQnNKuDMcRLPK1QlQUC7tM-tQTDjfqIfnp3lxbQ5Fe-4Fw_x5ULp-BqTirVU0bhXyehsh28NUL8VY7R7rlVpgOdhfZk6lSkAIO2a5HAfl4uoUrMFFvJOxFuwUivx8jo-UsH8hggDvOUWzu9iFa6KCBGXOFZdHXTKkxquV9tB-C5OzT07vbjBggN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مام اسپری سورملینا
💥
هم خوش‌بو، هم ماندگار، هم راحت!
⭕️
داخل هر بسته ۲ تا مام اسپری هست و از نظر قیمت خیلی به‌صرفه‌ست.
✅
کامل بوی بد عرق رو از بین می‌بره
✅
بدون حساسیت و بدون لک روی لباس
✅
مناسب خانم‌ها و آقایان
✅
ماندگاری زیاد؛ فقط یک‌بار بعد از حمام استفاده کن
🟡
🔵
رایحه اسپرت و دلپذیر
🟢
ارسال رایگان + پرداخت درب منزل
🔥
سفارش با تخفیف ویژه از لینک زیر
👇🏻
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori
https://yeklinks.ir/mamtele?utm_source=@Akhbarefori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/675248" target="_blank">📅 22:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RDes5ia53W0PmXt45IrsLoClsd7YcCIsldWX8ZQm7UImaIa8VyiSIT27j6I_V885knu8eihsSYhjASkCgRVgXi8eQL_pCaQMgEgBY2S_wl8iR5d-iJacEeoWqM1DE85dprYaZStcc4wRsI943mwrGK2KeGKOJaP3aQnxtAN_gPbJ5KgdFQiOPBk-E4a3mcijBKQz1fAmHJR_8ysBZURKfw6FReVnxBn_it9dS0DhNnnZqDU0iJIVE0jUoY3hDghOqv5FFOz03erHJRPBPDrlf3M0THZ_26OJFwfa6h6T_PRfm05QXh1gFhmsh3hHRTFy3acubw0-R4v2_1mBrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل لَتیدان؛ شاهکار مهندسی دوره صفوی و طولانی‌ترین پل تاریخی ایران در ۸۰ کیلومتری بندرعباس
🔹
این پل با ٢٣٣ دهانه و بيش از ١٠٠٠ متر طول، ۳ برابر سی‌وسه پل اصفهان است.
🔹
لاتیدان روی رودخانه سیلابی کر و با سرمايه يک بازرگان هرمزگانى مقيم هند ساخته شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/675247" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOxhafBbJG0U1BrAxWa1lj2Lea43WJn4BcZeAkmXc5J4eseAXS9Ys3qKctNBpyv5bhg8fVMjZeTtxr3lO6reEjIWgGZK_K-faCwbGc1FHGMRt-yOKoHbfR_ij4UHrkRcjoysFJ7Q5TljtaRJMwYlbVzvS7t-XGan_HQgg99g4Wbe4X9hDY6Gfcjo3sU0YYB6y23c80FyeJT-7qOFzpd0o07R70CQ316DGjTMB9TM6IH1NgdeVa7IMivQ1tJUHRte_wUPwj8ProJg5UVduNbUCeQ_dtYJNINqrKUniRuaGn2R-NIFgjdAQaNPLrlQandy_xVcMZgL8gGxdSZYVMGxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
زیارت به نیابت رهبر شهید
◾️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲، شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/675246" target="_blank">📅 21:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76eb5d57cc.mp4?token=pT9I02H9dGvmpiMDXbaPUzB4USRRVcpMFrmx7Rqe291H6a9QFa4qgBhTQ1BraO5IFKrF9sXRtsUP5YRpJlG_m__eFGTvYg65AJUGXK3PvPaeyX9oGi1KGOdxM3efxvCqgfgiV5i0VUanGGjo143JARuKWhgyQqKYOh9g7ub4XanGDly08Ohkf-7fmFLVjmvo6Vg6w-DJWFa7D0ZuNtaOSTPCkGrWtlqU5deLKTnCXzqqfwO7k2QxG7o2CFW7CN6nveeBwmgIIpCf-tZ24thAYXuxIsWS9F2Eh-ayhWCW31txKzNPkcwAM9xejwD08HflsB5_WYUf-ethPCMEINPXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عضو هئیت رئیسه فدراسیون فوتبال به پاداش ۱۴۰ میلیاردی قلعه‌نویی:
این پاداش‌‌ها نسبت به گذشته خیلی ناچیز است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675245" target="_blank">📅 21:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsDtwx47MK03kSgm4UIJTrLkTLCH386yArQSYEbspyZinUsOukTrpod5IPW6SUjPfM9qI1gRoCH5MF3MO7E7bHeRPvSpzYUJ46HKe0c9me_eVoU5zwS-uoRG7SGoH9u1UPRqTmSdskZ7ujtfba3IVd0sxU9YxEmaJoXrrYMzsZ0BS3e4UcDhPRioIqNsx7HBqcacWzDsr3pxArk453x5eX6J_cGpDm8Aid04HNES13V1krYOvKh0jxTFIwHH-WvR0L9jKOs8WgJ5OWVkt0COBhifDYqqADnOGAnNAtOCL8WtI1vMQZ-HgG-_O5RriREoP7KlBmOfYzJCNDCtNYotlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زرشک سیاه؛ یک میوه، هزار خاصیت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/675244" target="_blank">📅 21:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند
ادعای رسانه اسرائیلی وای‌نت:
🔹
قطر و عمان فشار قابل توجهی بر ایران وارد کردند تا موضع خود را نرم کرده و از آنچه به نظر می‌رسید یک عملیات تقریباً حتمی و بزرگ آمریکایی بود، جلوگیری کنند.
🔹
اسرائیل ارزیابی کرده بود که یک حمله بزرگ بین شب جمعه تا شنبه آغاز شود که این امر باعث آماده‌سازی‌های چشمگیری در اسرائیل شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/675243" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxOyZHAfvsssSZ-QN_2FjU0OSqZa330KZYWKUgeTihinN2GXS9OL0Hukz1Z0m6i9eUFDJdcoI8hqJmWigOnL1P5PV0KigUGNlpT5eaPDGhFT5gqNWZE1R9kWQIC-2MyV08ljX3dDnUJj0aiPz0VtPOrbU3kAQvGc4HArNJsyyCAhlrmKbQRzxeyu2zx9v5B_3f1A6TUQm9uEzRMf1ftvb2j07NGy16cklqJqqlV1DUuU55ZeWSuOAovFhPSqnESBS_1wUlK8jJIUUIsUETnZPbt3cagq2F4qmC5Tlqb63nYqniiubgee5bH7i67n2qgljCJzZ4OZZLbNRjovzfGTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
🔹
کیتی پری، خواننده پاپ، کاخ سفید را به خاطر استفاده بدون اجازه از آهنگ «Firework» در ویدئویی از حمله نظامی به ایران محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/675242" target="_blank">📅 21:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02181638c.mp4?token=kZ4MqM7Q_3o8T2LCvqxx--BRNdu-OQmAwLp6r-OZF_xmoAEqZ72FZlWgBqrbwbNjBE0ELA40qcuivs4T1Jr6eWqw1N7ISKfQMsyKqMqC5K4O2zb8TOAwVXud2KynAAbIQ1dSZpD1qUQh67WZaNrOK8eAzt6_gn6GnBnKU5_Lf_ni-URNzj_jX21TKSABhArNYp4KQ5-iuYV9a5_VK4AiYIbWdy4Bokb8SnecyNHvZvLlF_p1ZM1zuV-16U4uRDnH_BXrDWc8yzvbH01ySS7pA-P3TRXE5AGA0303kJVLmwEfLMEpstgV-t-yOfxQJacu8ALckjZnToXplAvgYWTBsSRjUvAw2ufoyDX-0Y5bM0yKtpYIyjzmv03undz5vChcF_jP_Ty3GOVxNjHxx_0XPKkX5a5A1j_qCxXzPTYOqDofp12FQO1Sl6YmKR4Nb0tvJ9mbvYmIu4HF2nliM5Ntu5kzAPsMaC6r7I9r5R0A2JGDp-tp5sDPhDk1AkbBjAZ3C7P1WFZJ533ddEHleu5wC6mdK0LtL_z1hmhLiC9AwYSZnIGqS_mjnKLLc2JqkSpYOLi8WALFIy6Nwr3Gp2yKINcNV31rLbqI560i1cAffupy4izA3WBmxV9QlkDrlWwWFld8IyQTnq321UA2aTsPrJw3cmJK4cYTLGil_tQXLd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا سپاه شرکت آمازون را در بحرین هدف قرار داد؟
🔹
سپاه پاسداران انقلاب اسلامی شرکت آمازون را در بحرین مورد هدف قرار داد. این شرکت چه اهمیت نظامی دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675241" target="_blank">📅 21:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4729e529f1.mp4?token=WgAiARhiI-9wwITo-YfFJxaQDkpNaPK-knGNL5EfVOZS6YKuM8Qe6y3k_wWdMhWw9bEgbQ_p14du_MH4CKKKkDOb9uXQx5tbTA6cTmy5sKXVRNGFiBDC1gA7yfvlTmExnGybvqZIk5poUd2KXgpn2xt6I1VP8LteSO69BUqOEOoRE49PxUXfVsz_h8ODi11nqV8CTolno_2ZVUtLxJCbmcUFNFz6XTYhATDZBbToeo2gDGiHwxaUZ5vJjLM35XNnQMwicA84s_HegVPd_EQcixRlNmRIDuAeQr-cN3mj6FdgAdJlFKs25z7vsJEGQg2KQZ9EHzKhQB6Hst3CeMI7gH-hxN5SAns4EsXouW-jODchCSUjMoWP3G79lkflpFSUgxwhmHP_phIsTrKW4_Lp45v4Wq2Kgkbc1RGpnkudetpPEWMlhdXdB_APG3QSPGzr1rWcsSUnjnbNMpSvTQIw7oP7W1EIlgrYSRQOJNRcwfD1shXWJdj57bogBc4ugdWRJ-r8l9yBlVPOiMnytRmxZozkYg6xQOjmWglI2Q3X5qFYVpz-8Q6r0I-7sUEv5XzcWVgxSpNmyJ8L5_ItU-yidMSq9LlYenwDvxYoO6aNDMm6u2LdlTL0qSn3oz32nJtNwtZlMmJHjNjSaYzG70wfJrezRPWsyeGKfGYlCKH9jic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4729e529f1.mp4?token=WgAiARhiI-9wwITo-YfFJxaQDkpNaPK-knGNL5EfVOZS6YKuM8Qe6y3k_wWdMhWw9bEgbQ_p14du_MH4CKKKkDOb9uXQx5tbTA6cTmy5sKXVRNGFiBDC1gA7yfvlTmExnGybvqZIk5poUd2KXgpn2xt6I1VP8LteSO69BUqOEOoRE49PxUXfVsz_h8ODi11nqV8CTolno_2ZVUtLxJCbmcUFNFz6XTYhATDZBbToeo2gDGiHwxaUZ5vJjLM35XNnQMwicA84s_HegVPd_EQcixRlNmRIDuAeQr-cN3mj6FdgAdJlFKs25z7vsJEGQg2KQZ9EHzKhQB6Hst3CeMI7gH-hxN5SAns4EsXouW-jODchCSUjMoWP3G79lkflpFSUgxwhmHP_phIsTrKW4_Lp45v4Wq2Kgkbc1RGpnkudetpPEWMlhdXdB_APG3QSPGzr1rWcsSUnjnbNMpSvTQIw7oP7W1EIlgrYSRQOJNRcwfD1shXWJdj57bogBc4ugdWRJ-r8l9yBlVPOiMnytRmxZozkYg6xQOjmWglI2Q3X5qFYVpz-8Q6r0I-7sUEv5XzcWVgxSpNmyJ8L5_ItU-yidMSq9LlYenwDvxYoO6aNDMm6u2LdlTL0qSn3oz32nJtNwtZlMmJHjNjSaYzG70wfJrezRPWsyeGKfGYlCKH9jic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرکت چینی Unitree از سگ رباتیک As2-W رونمایی کرد؛ یک ربات کوچک (۲۵ کیلوگرمی) و بسیار قدرتمند که برای محیط‌های سخت و صخره‌ای طراحی شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/675240" target="_blank">📅 21:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: موشک خیبرشکن، اسب بارکش زرادخانه تهران است
وال‌استریت‌ژورنال:
🔹
سلاحی ارزان، متحرک و دقیق با برد حداقل ۹۰۰ مایل، ارزان، دقیق و کشنده است. اخیراً، ایران از آن در حملات پیچیده استفاده کرده و خود را به عنوان یک دشمن سازگار برای آمریکا ثابت کرده است.
🔹
به گفته مقامات آمریکایی، ایران از ترکیبی از مسیرهای پرواز، مانورها و سرعت‌های مختلف برای گیج کردن پدافندهای ایالات متحده استفاده می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/675239" target="_blank">📅 21:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57794715bd.mp4?token=FRhBen0j_cS-2iBrY2NWv-vL8NXMbOmD0zG522SIH4lKNv8rfkXNy2JY0Fe1emOj0dw3BrCgzA8Of0CDI5908a7hCmBAn9yk_jJWDKywtRFbjPA27gqDOhWepM-QmZ6Jce3IXwlsOBZtukltBNaFphuBiIpSY-_S3hUw3YqX8qsEqZ80XqCEOY8TYH2kth4VqGl_ZP08o-pqLUyuoHSOmu8HzpY3BX7K79GPYoyb_SNdwSQrqgiL6lYxSPRYnCEDDhsB_byhxLGro5pgXwxK3G4yZI1iqdjpJKCE0HxEZBn4b83a8H33V8ZWJOb6A04SCGyGIGXKm8toxq0qTrzonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57794715bd.mp4?token=FRhBen0j_cS-2iBrY2NWv-vL8NXMbOmD0zG522SIH4lKNv8rfkXNy2JY0Fe1emOj0dw3BrCgzA8Of0CDI5908a7hCmBAn9yk_jJWDKywtRFbjPA27gqDOhWepM-QmZ6Jce3IXwlsOBZtukltBNaFphuBiIpSY-_S3hUw3YqX8qsEqZ80XqCEOY8TYH2kth4VqGl_ZP08o-pqLUyuoHSOmu8HzpY3BX7K79GPYoyb_SNdwSQrqgiL6lYxSPRYnCEDDhsB_byhxLGro5pgXwxK3G4yZI1iqdjpJKCE0HxEZBn4b83a8H33V8ZWJOb6A04SCGyGIGXKm8toxq0qTrzonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مشایه همه به نیابت از آقای شهید ایران خدمت می‌کنند…
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/675237" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675236">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0c70e5af.mp4?token=IkWevTq7RygI5c-gZz_9uB9g8uZrBRcGvv5AU6gETqYoxT9-2yoqNng3wplI5y3bTt55U59JPqpTk4-fflEXjipT4JGRd4BVKx5nO2UjKnpaX_PWUyOFOLuYEsvCxcrlumaJcCTZ_mUWKxTD7xHq7W14JdQUJlfwwK5qjYvzMENKiqNAkImWY6nVt_8wL8YHGv-qYR6tR9v6m6y414_UsP0Eo01Rr-4_HrcVSqyD-ydBRIdIJN0HytKFzPNt_unLU2HtAA_MI53Sfr9cc4RPEMtOHGb9uAQBeXh2JI23PEMxEPTDguY2ivKddb1KCXjWewHv-KyJPmgEGpBPDXgUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0c70e5af.mp4?token=IkWevTq7RygI5c-gZz_9uB9g8uZrBRcGvv5AU6gETqYoxT9-2yoqNng3wplI5y3bTt55U59JPqpTk4-fflEXjipT4JGRd4BVKx5nO2UjKnpaX_PWUyOFOLuYEsvCxcrlumaJcCTZ_mUWKxTD7xHq7W14JdQUJlfwwK5qjYvzMENKiqNAkImWY6nVt_8wL8YHGv-qYR6tR9v6m6y414_UsP0Eo01Rr-4_HrcVSqyD-ydBRIdIJN0HytKFzPNt_unLU2HtAA_MI53Sfr9cc4RPEMtOHGb9uAQBeXh2JI23PEMxEPTDguY2ivKddb1KCXjWewHv-KyJPmgEGpBPDXgUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فهرست خسارات بسیار سنگین آمریکا در پی حملات ایران منتشر شد  سردار محبی سخنگوی سپاه پاسداران:  طی ۱۵ روز (از ۱۷ تیر تا ۳۱ تیر) آمار خسارات وارده به شرح زیر است
🔹
در حوزه راداری و پدافندی:  ۷ مرکز فرماندهی و کنترل  ۳ سامانه ارتباط ماهواره‌ای  ۶ رادار پدافندی…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/675236" target="_blank">📅 21:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675234">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da6aa40f0.mp4?token=bZp6iNXysdbJUTBYANuDCZZtpM1cs8yFcHWBhJehU6xx-G9BvwHKh-1zkkLp0-UeFUFQvdCEjtohMqjOYbS1fQUMxH2UrreDjWCk-Lmj_pPjXkFhMekNXSaBCX5Sl8hhOmrBvTmL1EnMt1NC1qz36GObkes5Vm5adAiOD9NCiVeaX7B4BeRKPMkb_lgWutYKdi5HR8l7VbsoiHndb9NGz0PEvvUKaeUdXWl7Tyxc0MK9TJLXfRy4DfS2BUN-4MBpkVeUtO4vYjCC6QVR01LhDRl6OjupLBBUBLjbTox4lrf1998U8TYLN6-rRDMkDMQ6RmDy2TMNPpZHB7w8eKkk1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da6aa40f0.mp4?token=bZp6iNXysdbJUTBYANuDCZZtpM1cs8yFcHWBhJehU6xx-G9BvwHKh-1zkkLp0-UeFUFQvdCEjtohMqjOYbS1fQUMxH2UrreDjWCk-Lmj_pPjXkFhMekNXSaBCX5Sl8hhOmrBvTmL1EnMt1NC1qz36GObkes5Vm5adAiOD9NCiVeaX7B4BeRKPMkb_lgWutYKdi5HR8l7VbsoiHndb9NGz0PEvvUKaeUdXWl7Tyxc0MK9TJLXfRy4DfS2BUN-4MBpkVeUtO4vYjCC6QVR01LhDRl6OjupLBBUBLjbTox4lrf1998U8TYLN6-rRDMkDMQ6RmDy2TMNPpZHB7w8eKkk1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: شب‌های روشن
🔹
ژانر: درام، عاشقانه
🔹
خلاصه: اقتباسی درخشان از شاهکار داستایوفسکی به کارگردانی فرزاد مؤتمن؛ داستان استاد دانشگاهی تنها که در چهار شب، با دختری مرموز آشنا می‌شود و میان عشق، انتظار و حسرت، معنای تازه‌ای از زندگی را کشف می‌کند. با…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/675234" target="_blank">📅 21:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675233">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تیر تا ۳۱ تیر، نیروهای مسلح ایران ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردند.
🔹
همچنین ۱۷ پهپاد…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/675233" target="_blank">📅 20:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675232">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fd1feb15.mp4?token=UIpnX2AXzIcDb11hWzyHfbqBx06VidJJ5N6EopqQgrulQOtFUAdb5OW8aFC2Jrhn_4BVCYdvyDEJJkVCyTLQ5mXEbcBqD0Js5oxVkBIJ63EC4X8Zlc34RMCphoYO-hIpcnwdcG8BvtYm7hvSvyQfuassuLdxRP8dJ5amYagBZ0zCiB24alPg5Z3rV6TjcjwjTI1PREyh8EppSzofO5eTUeSfOX4S_tlP8QDXHTyQGSQ3tXniNAGraF_BAQBoD4NqlBPk-PA7NRMRC3cYFtCN2g_VNn__f5QWZ8imuEoqjN53RVas6vrFFMoFS1fULXL28gdlbEGQssIBWc9zKwmojA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fd1feb15.mp4?token=UIpnX2AXzIcDb11hWzyHfbqBx06VidJJ5N6EopqQgrulQOtFUAdb5OW8aFC2Jrhn_4BVCYdvyDEJJkVCyTLQ5mXEbcBqD0Js5oxVkBIJ63EC4X8Zlc34RMCphoYO-hIpcnwdcG8BvtYm7hvSvyQfuassuLdxRP8dJ5amYagBZ0zCiB24alPg5Z3rV6TjcjwjTI1PREyh8EppSzofO5eTUeSfOX4S_tlP8QDXHTyQGSQ3tXniNAGraF_BAQBoD4NqlBPk-PA7NRMRC3cYFtCN2g_VNn__f5QWZ8imuEoqjN53RVas6vrFFMoFS1fULXL28gdlbEGQssIBWc9zKwmojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارلینگ هالند در مراسم عروسی جیجو دوناروما با طبل نوازی به سبک جشن معروف نروژی‌ها، لحظات شادی را رقم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/675232" target="_blank">📅 20:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675231">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f68c4b9b6.mp4?token=BU3ZV0ku-OdgP5fQLMUQjYVgz300iWIcUBIwZadssHfS_AeR15mBDXTsge6T7tIBR_8VxXtN-UDxVev8O_xfW-wUINmG2uw-SMjH__KMKY5Fk22WwkyEIu0YTdZdCRwNymFWQpSSKy2eYuZxPH4q_rNu5cp7tfnYG3AF2pQZ39_i2kKizZUCDwf-jxIwiDr5ORULCMeBNCSL_F_twe4TF3wMWQgDJiMbMNpGiz5zMQl9Pblu-R-zxuouxSMrSgO8dHnnvb-0cvx1EmP8Sp82azUEe9QoTraIXafkQMgnzTnlufthuccMHPjNOfZbrkXRXz9owq3E_NrjmmHR301IlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f68c4b9b6.mp4?token=BU3ZV0ku-OdgP5fQLMUQjYVgz300iWIcUBIwZadssHfS_AeR15mBDXTsge6T7tIBR_8VxXtN-UDxVev8O_xfW-wUINmG2uw-SMjH__KMKY5Fk22WwkyEIu0YTdZdCRwNymFWQpSSKy2eYuZxPH4q_rNu5cp7tfnYG3AF2pQZ39_i2kKizZUCDwf-jxIwiDr5ORULCMeBNCSL_F_twe4TF3wMWQgDJiMbMNpGiz5zMQl9Pblu-R-zxuouxSMrSgO8dHnnvb-0cvx1EmP8Sp82azUEe9QoTraIXafkQMgnzTnlufthuccMHPjNOfZbrkXRXz9owq3E_NrjmmHR301IlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره مسعود ده‌نمکی از انتخاب اکبرعبدی در نقش روحانی فیلم رسوایی
🔹
کار به جایی رسید که رهبر شهید هم پیگیر این نقش بودند، اما مرحوم عبدی در آن درخشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/675231" target="_blank">📅 20:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675230">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8910d6e24.mp4?token=FH6CA7c0gmEhTlBykMyNCeHGIxqMLpXLVlUzABMSBJJW2tLFpPjhR6fzK92AdHNjZcEt1l95sv8EnKPUMfHLraJHGnrzRAscZPL1nAKpIV7lHMwL-UiTndibILmg3GWFTFYFY2qFcy1vgbD-8a5Sw7FzGecAnm2gtyqr9VOqI4WJgNGq9KCMEiv7bwwD_gfDdSG4ulpH3kOZzilFAuBEGXyGC8JaU8gwIDaINFdfaOJtwyZM7lt0W7OsG_k7D5_-QuNg4sYfv50GSvkLBlUIP4uwNIo_-Af7xEKO71RSncecKFkyh7vTiL4xk4ALrSCh38ndfKx2w68oLPzIdAi5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8910d6e24.mp4?token=FH6CA7c0gmEhTlBykMyNCeHGIxqMLpXLVlUzABMSBJJW2tLFpPjhR6fzK92AdHNjZcEt1l95sv8EnKPUMfHLraJHGnrzRAscZPL1nAKpIV7lHMwL-UiTndibILmg3GWFTFYFY2qFcy1vgbD-8a5Sw7FzGecAnm2gtyqr9VOqI4WJgNGq9KCMEiv7bwwD_gfDdSG4ulpH3kOZzilFAuBEGXyGC8JaU8gwIDaINFdfaOJtwyZM7lt0W7OsG_k7D5_-QuNg4sYfv50GSvkLBlUIP4uwNIo_-Af7xEKO71RSncecKFkyh7vTiL4xk4ALrSCh38ndfKx2w68oLPzIdAi5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی از شلیک موشک از جنوب لبنان
🔹
منابع رسانه‌ای از شلیک موشک‌هایی از جنوب لبنان به مناطق پیشروی ارتش رژیم صهیونیستی در شهرک کفرتبنیت‌ خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675230" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675229">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3NnBWSGTA7-iYIxWZGhgF-8xaKAHSAf3qUC331WplQNxPMMVbpy8H9HpAF_lkAiUVl-fwEo10lT0siBjO9b1ZjGLfnkEXasETlrMKXlTcBuuK8Jl29KjjPcAgU7BD68BTxNvU2eBIl1odUqB4GbImcKsCB-4xDstQq8JpBocRaFvL1yOOXK9iWN9ujUvVK1nWgNvA82Q8aF2qCpUbX_T6NXOAjjCRgXeeirOGD6KXziVsDDxCdKJMqbVKTop5RXld64LUz92hsnZytiqfFlNzqXUaGrTnmKMICwBBQ4l2x86CQvNHCaFCaVoItpAJML_KR_Js5rbbhKDbi9StHzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان ذخیره گندم کشورهای جهان
🔸
چین با حدود ۱۲۵.۷ میلیون تن، بزرگ‌ترین ذخایر پایانی گندم جهان را در اختیار دارد؛ پس از آن کشورهایی مانند هند، روسیه و آمریکا قرار دارند.
🔸
ذخایر پایانی گندم ایران در سال ۲۰۲۵ حدود ۳.۳ میلیون تن برآورد شده است.
🔸
ذخایر پایانی گندم، میزان گندمی است که پس از پایان سال بازاریابی در انبارها باقی می‌ماند و یکی از شاخص‌های مهم امنیت غذایی کشورهاست.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/675229" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
روایت تکان‌دهنده از برزخ؛ وقتی پای «حق‌الناس» به میان می‌آید
🔹
00:10:00 همراه شدن با ندای زیبای مرد جوان
🔹
00:14:50 تفاوت خواب و رؤیا با تجربه نزدیک به مرگ
🔹
00:19:00 اولین مکان سنجش اعمال مرتبط با امور حق‌الناس است
🔹
00:23:00 عبور از مرحله با احترام به پدر و دعای خیر مادر
🔹
00:35:30 تغییرات رفتاری نسبت به همسر بعد از درک دلشکستگی‌های پنهان‌اش
🔹
00:48:00 رؤیت حق کتک زدن شاگرد در اولین سال خدمت معلمی
🔹
00:58:30 پیچیدن عطر خوش در فضا با ورود و حضور کودکان
🔹
01:03:30 ماجرای مطلع بودن فرد بیمار از امور احیای او در زمان نداشتن علائم حیاتی
🔹
قسمت دوازدهم (حق)، فصل پنجم
🔹
#تجربه‌گر
: نرجس اربابی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/675227" target="_blank">📅 20:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko83BAyujJwgz_84xuSRYCfgRyNDdlO7wM3ZfcM4P3rdwnLwf1AHXBeGcSoS3hr8XUufcoJprE53IGdWYpvl8irLZD753y3kX1Kmq_a_1c2URVWqMTMY4Q_4LtIy8GIcMGLNIKVsfUzHD_934DQsOMW2Mlc1uk7QXaRMZbDWS68YUjpNi5Ai0zwu3aDZW7LFZ5apAryPThQ3kDri1I24Mno4ulnWUZHU5d8Cv4z3LkUYKVOW5vWYjbj7SxhjgTu_f-ols2L8GzxVwrSxoP90IhQzy3utdmAtxBOx5mCjroikYvZsMCzGiHqY2JQeuvx6Lhx3__akRABG89MeHCCa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تیر تا ۳۱ تیر، نیروهای مسلح ایران ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی، یک جنگنده اف۱۵ در داخل شلتر، یک هواپیمای پی۸، یک هواپیمای ترابری سی۱۷ و ۸ هواپیمای سوخت رسان هم منهدم شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675226" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a26a310e.mp4?token=K_f6zN7MQuDsotcOV9-FTx4of7lewGr862MciOgFDR7yQuGUgRweLoY6hEnpJffca_E_-F7TXpv2BnC0ydTiOhQ-yuxqMLu1tclG72YybDk82-IyTxjvF62DPtq92Ppc3QgBy5clIYJI2s4wkfUeRtkqLu8NunhJ67ymmTDynnIccWs8TevYYNLAHPrCBJENuW6wAWDxchhV4puhftLueo1-uwLE89TMdW2xxIi6gVwS6WldSOjzyBHGmuM8IYmraaq0mTZa7zJE2vw8e67gnz0nc-2HTJ8OCPD4EOYF_PQfpiJUWoJoxnXLpwe49Bwp6oO4BfVFw0X0HiLyVBMh9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a26a310e.mp4?token=K_f6zN7MQuDsotcOV9-FTx4of7lewGr862MciOgFDR7yQuGUgRweLoY6hEnpJffca_E_-F7TXpv2BnC0ydTiOhQ-yuxqMLu1tclG72YybDk82-IyTxjvF62DPtq92Ppc3QgBy5clIYJI2s4wkfUeRtkqLu8NunhJ67ymmTDynnIccWs8TevYYNLAHPrCBJENuW6wAWDxchhV4puhftLueo1-uwLE89TMdW2xxIi6gVwS6WldSOjzyBHGmuM8IYmraaq0mTZa7zJE2vw8e67gnz0nc-2HTJ8OCPD4EOYF_PQfpiJUWoJoxnXLpwe49Bwp6oO4BfVFw0X0HiLyVBMh9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا آخرین لحظه عمرم با افتخار سرباز فدایی وطنم و ملتم هستم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/675225" target="_blank">📅 20:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB-4aze0fNY1LbIu7ERNoLwjfZSj32T8MOIhfdWcY9yoQ4EoOXEhvzu8mLH1RMst1GPRb6B2jI7By5YXuhMlnJk3aQ820fYP_ArJBCzkRn9APBU0cg8hEszrU4mLNo-KaDPp7gwAOKI0JP2GA15P_Yf82j3lOrqt7hCGlrqPfu01Hg1HWL-qQKsx27ZGFKwsmqj-4OkK0sR3G63PTQC6vkYOcojl5eNXVQERMeGleFCXZsNmTWO12ARJMRVlwsKhm9IlbHK1R2ooVq68dfB7e7J31EJvIIqIb15Boz_GhtFO4KlEr3d_An53A94R3zmMIyZiXk7Yfgc467eqiwyn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت آلمان در تهران شایعات مربوط به تخلیه کارکنان خود را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/675224" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e7e43c57.mp4?token=RgHXzZGu8HhafpsN1FHjt0nabyGm-0GYpXePY1cK_-BfrNIT1VlAKyUVpi_O77TnBetHaReLMiiicLtq5nwS621JQkJcpKaYJWPkUy3y6slL2J9uG0nY4k_TMmmc5OIhyrFT4IAtOhdVw77LIilNGTroKG5nRUikEmSGX-2m4fmqBZNVsdekDfLg2cPS3PDDdt6vbDzyWwN1_gatlVenTVFpOIttWEjzjstGthnsEY86J8-ZjDL_qisoGbH6j1CkOB8RfXfWV9hGOcuSaAi_Y8O8LFuw3miISF7TBHfTahSJhqgl_ovlQPxV2NNmm_tDBkrT5htE8PskMnSxi0HUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e7e43c57.mp4?token=RgHXzZGu8HhafpsN1FHjt0nabyGm-0GYpXePY1cK_-BfrNIT1VlAKyUVpi_O77TnBetHaReLMiiicLtq5nwS621JQkJcpKaYJWPkUy3y6slL2J9uG0nY4k_TMmmc5OIhyrFT4IAtOhdVw77LIilNGTroKG5nRUikEmSGX-2m4fmqBZNVsdekDfLg2cPS3PDDdt6vbDzyWwN1_gatlVenTVFpOIttWEjzjstGthnsEY86J8-ZjDL_qisoGbH6j1CkOB8RfXfWV9hGOcuSaAi_Y8O8LFuw3miISF7TBHfTahSJhqgl_ovlQPxV2NNmm_tDBkrT5htE8PskMnSxi0HUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔹
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/675223" target="_blank">📅 20:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675220">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PCNxUolnO_On7pRatFkvPRPEQLXM2jGViH_DEFaVkY766JjdfwrNaCfgPVfQxmPXVKc5mMoJKQW0ih5Zs7r5V_QuS4H6fULRlWbL3DO2XMINhBUpkaX5zdWVv7K0Qe1408MTZ-BsCd5Z7XJZFzMooJPV5coPlOnfaAfqzNqfZvGZ_IVR-PrlT9KSSz0_XE1mTAw7p5fEKnkj5lbZCeykyeNi3AE1fLmPutdaSBIOnGSvEcqRe7osqe0BWTAXFLIGKcrw2M0TqniNQnt2oa29nmw35vDHEcrwlXZ1c0N0ZlgGmnZ_P6KD33Pekee8SVTnFAx1XLOGGRzDPGrQEZnfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aerhIU_W40S_pms9xfQt8-m-zGWuYmJDDdY_BJGPGWZEsKhDzZSyPczm5pqLdaUhu3Q0Io7g09cPBuJuqs8RowViYnShFeqsrkZz-Oua3ZqihraTvVNyxySCMbNOA20PfIrIAaviFKa9ohHDH2TNfyJXdnR2D0KMjYqaYiN8mCWpEsCHkkH7jW_muiD88XSatLrejv_9DWMfGsQoHdgeS7t1mJ1xfnQLPVWBF0n4Z7d2WPRvXQEDpGhYsN_JwrQ_xiNpvnX9XHVjzQAz1NLm0qoIbhSh9Z9JIo6tG6hcNkg5iAFWW0_RXeXzgNVqWtE3w2hnepWx1jBQmXKjr5GebQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۵
دارویی که بهتره همیشه در خونه داشته باشی
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/675220" target="_blank">📅 20:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675219">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8Hiw15vq_o5B7WYfl5V6sHyDinChBNG0nfNF5CUeT_ZaYF8C0C2KSDCsmgINkYF_6tgNDZWvN0M3PK4ysij7_YnRo7fJZfLXqNCVFJV8gcR5f2axqXKS290BSB709KRU0dEKhcInB3kUfnjnYbEqy7j6j0bvV0VvDiIDZCvNM_3qrFU_K5X1RCUvcQlXntrRuKj_p1TUPKYA-Nla82VHzWeiUbAMieoFMajiuQPzbwXyPjgl4PzzshHRvp-C6oXGDid-6G2TuG9TQHUpdndkfFaZvhAhD2PiTi40hOmtFJTAjAWRDX1C25Ax1I7CoIatROKBR1RXKw-2jx1hCBwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/675219" target="_blank">📅 20:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675216">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE4NL106Hdk3xJnDLsoGEqWWS2cU1YfZ4RuN59QabT0pyro8hervrYZg0vCeYkng1ype165xzcdp8GKEczmbI8Wnvb5dfpzMA3mWF-dTSwpJbMXEPxGbrB6eM3dlw8lYFioFeYoUMjCEFIZrEB2VPyoDaVg7mkVKMBCsX2gTGaGBNSf4GKqwfP30WX3of8FY6UW3ENrlEhj-Bas-WGvbireLz281JiBqDoSATzeiBTvYDhwl6crzknh9IavSyzvo1QHgHqhnExf1H-YBOB5p-Q_c8OeecNPMfnJD_Z7k9CAuFJChwwbXLwn9SSfcwgRkwMWLzVqT1R91jIfuvPxcJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwLK_WAXXZdeB6Ch8HjSHq1MVdxDUd-Lvei6cjaQy09BTBPVeeHOC7_X0nNa1y5u1yAZafxPwKQ1lL16fhqfLVqFRTlpnUXMz1w3E9tr4rj7tWqfJpAdEUViUVGQ5smOaO9s71qETr5GNNSZec2IrmedWUp_b90xxfbFRblApUOOz33ApNN14xS0_6n1YQDnqw0CKZZJaXVvL2cQaczDvWP4B6N7lEQ9mWE7dlxJZeRd7qji4os44KIcRglt3Lxs6WnSiBusRJSAXcsQaro3mftAjtfwNVugd6XYrGW5jfn5RMaLkC4O6i8SW_jByvrlXnRivNZFVsANMrjhOmQ9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بخشی دی، کتاب پر‌طرفدار این روزها با ترکیب شگفت‌انگیز معما، روان‌شناسی و داستان‌های پزشکی
🔹
کتاب «بخش دی» اثر فریدا مک‌فادن، روایتی انسانی و تأثیرگذار از زندگی در دل یک بیمارستان است. نویسنده با زبانی روان؛ اما معمایی داستان بیماران، پزشکان و پرستاران را دست‌مایه‌ای برای پرداختن به مفاهیمی چون امید، ناامیدی، روابط انسانی و چالش‌های اخلاقی قرار می‌دهد. این رمان، علاوه بر روایت داستانی جذاب، نگاهی عمیق به پیچیدگی‌های زندگی و قدرت همدلی در سخت‌ترین شرایط دارد.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/675216" target="_blank">📅 20:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fabb55f0.mp4?token=h8qevlKgVOcl9YqvkkG-54ikcGkDdxEfICjlZdY8G7kIwZUrgYqHXWM-qrAKkMQUDzACztp4LxkPsHkI3joC-kMb5Pufq8Mh5Z8_qYL54zA7mdcLULA7HYFtxjLsm3p_hylKeFX7aeQGmWrpB7VBlUg9Kk3VZXgo9VmalSPr8o6F0LIDgfOgjYYPCWqqOXCxmYfGXeEb6HlkGzamMTHhsqELwasme51xdnpV9AT3fTaZpvfbvQZzOOxgcbFw9RbRDC1DoxmSoVxSPYBvHJDlw9dtzHUrWynklRmhVRvc2r7U6DrLjaucBpYaGwW5TC1DRxzViCFSnFqLfaIGkIdQQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fabb55f0.mp4?token=h8qevlKgVOcl9YqvkkG-54ikcGkDdxEfICjlZdY8G7kIwZUrgYqHXWM-qrAKkMQUDzACztp4LxkPsHkI3joC-kMb5Pufq8Mh5Z8_qYL54zA7mdcLULA7HYFtxjLsm3p_hylKeFX7aeQGmWrpB7VBlUg9Kk3VZXgo9VmalSPr8o6F0LIDgfOgjYYPCWqqOXCxmYfGXeEb6HlkGzamMTHhsqELwasme51xdnpV9AT3fTaZpvfbvQZzOOxgcbFw9RbRDC1DoxmSoVxSPYBvHJDlw9dtzHUrWynklRmhVRvc2r7U6DrLjaucBpYaGwW5TC1DRxzViCFSnFqLfaIGkIdQQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ دردناک خرس سیاهی که از تیر برق ۱۰ متری بالا رفت
🔹
ویدئویی دردناکی از گرفتار شدن یک خرس عظیم‌الجثه در بالای تیر برق حدود ۱۰ متری در ایالت نیومکزیکوی آمریکا به‌طور گسترده منتشر شده است. این حیوان پس از ساعت‌ها ماندن در این وضعیت، سرانجام بر اثر برق‌گرفتگی جان باخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675215" target="_blank">📅 19:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX5nAI6FhyFXMOyw1dheohDezpLKQ6CSPLhBaQfOuIAkQKUdLM3vimIbie0GkW1OP1PKjYAqqlRKKWbiaV8JYfJ_-qh5YsgrDUprGl92IdaBS_2XYAIET5E9AO9lA_Dlbb2aSCVrOS0TX4uzDjeHCt4wVBeCnOCIJYx5bRsFe-LAXsQri9zq64IFitQFkzZBpePbcOChd4N-qyopBu4Gptn4IMc-eicKUeaN4S415UC7WPdGv42vqGl55Ht_8A047BL2zECm3_ShOy6hMVJ8dtESb3qRf-5NhgsQKE4X0mKNvbebkVk-buFASu7TVJx3G-KJTqngm1FODl8T7QgIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر: تردد دریایی به طور کامل برای تمامی وسایل نقلیه و کشتی‌های دریایی از فردا یکشنبه از سر گرفته خواهد شد
🔹
این وزارتخانه در اطاعیه ای از «همه خواست تا از مقررات و دستورالعمل‌های دریایی موجود پیروی کنند تا بالاترین سطح ایمنی و امنیت برای همه سفرها تضمین شود»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675214" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsaR1gbyOytSCkTZyZwENymAkgZu1MqaacSOQghRWFV6aMnSDh1mtBb6rfcPazyCkU2jAAGUIHxId_zpLpscg-caAI6_ZCP8Gq9fIXP4vNPcfJ8c6ZI01IJxY4ZKZ0G-7RvMEHoDejPEqha8O6HsGDaD_ZAUr2eFK5AN6LkswEKp90mtMFqEIXzYn7N5gwjxJFe2aMksn5MDsv-aBhLZWtNRix8GedHlcLAur0uKwYd-Ozz5MJqc_Ade_wOX_12mjLaYAWuhBjh8Kj8gafVf9KPhZhEvLj7b79XKFwsluoPpo8qATgtcOkW-rRZ4cIz2Z23M5V_SwYYWQLPa2BVQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حالا که رسید به ۱۰۰ تا
🔹
حملات جنایتکارانه آمریکا به ایران متوقف شد، آن‌هم زمانی که نفت باز هم قیمت ۱۰۰ دلاری را تجربه کرد. این اتفاق نشان داد تحولات بازار انرژی تا چه اندازه بر رفتار سیاسی واشینگتن اثرگذار است. تجربه جنگ اخیر نیز نشان می‌دهد هر زمان بهای نفت از سطح مورد انتظار آمریکا فراتر می‌رود، دونالد ترامپ با طرح موضوعاتی مانند «توافق»، «مذاکره» یا «کاهش تنش» تلاش می‌کند فضای روانی بازار را مدیریت کرده و از افزایش بیشتر قیمت‌ها جلوگیری کند. هم‌زمانی توقف حملات آمریکا علیه ایران با جهش قیمت نفت، این برداشت را تقویت کرده که کنترل بازار انرژی، یکی از مؤلفه‌های اصلی تصمیمات سیاسی واشینگتن است. از همین رو، هرگونه پیام یا اظهارنظر درباره مذاکره را باید با دقت و احتیاط تحلیل کرد؛ زیرا در بسیاری از موارد، این مواضع بیش از آنکه نشانه تغییر راهبرد باشند، ابزاری برای مدیریت انتظارات بازار و مهار قیمت نفت به شمار می‌روند.
🔹
هشتصدونوزدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/675213" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5afb5b61.mp4?token=qNxOECqevz8muuPPphiY2nAYet6jbPcmP5eLGXRdMvKWC3-o-VqWXvUxCXoqV_XGcsEtm4VXum9pLfpU-VE70hePxej_qu0tQbuhtomX4SQ5pEKInVATcWQlFrTsBToUoj0Fd80daM27ojQW2-Ln_bGCbzUhGOBpIOkz3IRLLAojo2gVHC94UDvpHSI_c-rXr-9kmgqv0HXtslxSsWMXlPDxC2bxwT-CBsTebtQVOWoc3kRf_F3UgCC5fWljw7ARTMCqwZ2stvuam_bY2gQmmDcy8AM61p1lhWyLw-fsdn8ewJf7CCwKvjabd3WVwadQRV34JYmWD8nTsvQm_YcN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5afb5b61.mp4?token=qNxOECqevz8muuPPphiY2nAYet6jbPcmP5eLGXRdMvKWC3-o-VqWXvUxCXoqV_XGcsEtm4VXum9pLfpU-VE70hePxej_qu0tQbuhtomX4SQ5pEKInVATcWQlFrTsBToUoj0Fd80daM27ojQW2-Ln_bGCbzUhGOBpIOkz3IRLLAojo2gVHC94UDvpHSI_c-rXr-9kmgqv0HXtslxSsWMXlPDxC2bxwT-CBsTebtQVOWoc3kRf_F3UgCC5fWljw7ARTMCqwZ2stvuam_bY2gQmmDcy8AM61p1lhWyLw-fsdn8ewJf7CCwKvjabd3WVwadQRV34JYmWD8nTsvQm_YcN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوک یمن به قلب نفتی عربستان
🔹
یمن با حمله شب گذشته به بندر ینبع و شهر جیزان معادلات جدیدی در تنش‌های خاورمیانه ایجاد کرد.
🔹
این دو شهر قلب‌های نفتی عربستان سعودی بودند که مورد اصابت موشک‌های انصارالله یمن قرار گرفت./ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/675212" target="_blank">📅 19:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIkfURP7Nc6qdPU05cmoxyR1af3YK0j-pWzC4VrBExop1eJUqtAIrbn1h9SzY1GTyHttYXiWanWauisfek0uF3LGkjnmOAt7DTsUq8_sI1QdCIsXAMEvFj60s-V9x--HnbjSaceEoeHXujW9SF9j3_63Bx8V7ZNtUXyWV6a-6jHDsMmsAEU_jQHE467E_4DMC_HmGISj6eIVt2xg4pkdXQlpouhCbGCdtL4olYkbyQzLWv5sI-4qaS9_KfteTCnIQzxTYfux5QmpR1hDBcjFCzxaJOD_FpJUBrH4sVesfUZize2UCB6kvuXsX6AUO1hpgRbO7ZydL6W8mdthKC9o5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارنامه ادعاهای ترامپ درباره ایران
🔸
ترامپ ۱۰۶ بار ادعای «شکست ایران»، ۹۵ بار «نابودی ایران»، ۸۸ بار «توافق قریب‌الوقوع» و ۷۵ بار «باز بودن تنگه هرمز» را مطرح کرده است.
🔸
تکرار این ادعاها در حالی ادامه دارد که تحقق‌نیافتن آن‌ها، از نگاه برخی تحلیلگران، نشانه‌ای از دشواری پیشبرد اهداف اعلامی ترامپ در قبال ایران است.
@amarfact</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/675211" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675205">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMDbJtH9-h0wnXSSGNKEBBwKWi9uZIgb94bg2n7Cb9F1ner-t23w9rd-cB6RT34jGElKAltFqCL82I4NBKrlaNFq2gYybx0A8sTyWlEEVbuko7G1sJ5va_uow6c8-KhfZSNrK_9KIPpQrl0HA0Jn91JMDFPUIxcSxprQRWvkhgIhH9gWY8CwQ10Q_Xlhy4e5J5aaO5feQptWLMfXM7s5qIAsY3Zq1lPWQbPhKJjZ2mKYly7ez_6pAGLo-YIZECm7lkmEF_jeAULt0l2iO-Foji5TDskPjNTGv2hsQDm-E6xSf_42eeYAVZqS2_-qs-WMGk3Xq9ZP2Mex7jb5_XxPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhB4UybjBxZkrx1ldIAcrr0Lseu_z-fhuuFm5vuY_FYYpqZe589wyps7c2gDYG3y-qtiWt78fq1dZ8lcqufOu8so9p--XpmrTa6EiCGnrpOWrU8PPDyAexQU72uTXNtFIGwF4q9p_7AAXuaAdHytFyADbDAnLisxVuHgDG-QAVqpGW7loe0UzPl_NkMM-wQJjcZHBdu1-bvskpozeUTbqpjU4fEFMhBfUaMVICvYS62mB_LiG2iwGEoWB3vdteNYW23Ehxn2tF-jM_DSgNCd6swLib96z3l02hPhM27AB3Cbl6qDvgj444BX4kmeE3MD41a-8g0Dv__6tWiqgtJhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLvam_eU-I2Hz8IgfGxtQTVQCJx_pfNO6YaLBn8lB1Ko4gSmc_xsYi5xaOXgaODFCnSo2cCUOCcZaOqHi9X9NCjv8527JZhma-8r7ZKtecT52S7ws6wUDO_OeywjznsbuOBzUoW35-wl8oRlq6x6AYmPRUkCPWqeUxGOp_4MTO33R0FSCdS8bIZbIqgQTEeMTWoFXVjlaQb0j3yzjUSp9aKdS7xKdpRyWLiM_8P87LmbqINin0R53dfKDOjhaxjww3HNeV-I9XF5bI64vQ8aZg7AmuMcmq2eOydzQzwN0AqnqX3aEIm700IrwP9dJoIFfu3VqSRtNsu0TfMUfijv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRgkGLeoIOfGw9gt3YqRcN6AtFi2rpoVQzhBdXN-pd6tf_C-Ewc89w3hG4JTvmF05-Ota2uRW_qFhpwwTK5LUc5KWtX1QftAG-BgRswHkTb0RUkwsx7nzUOzLGAow3po-yTFdu0tSG9e-_mrZ_xg0MvL0kleE0uWDbMpAD_dZki9ByTXYZbrMbJw6-jxONEee4kS9zakHdresCZB0Yq6hm7nE3T8iUhPi7JhEqLBa-pWz01DVdsw3VpKmgkGztHse9f1MPGuLGyRoETYJ9LjnHIHWFCc5bZfwDU-cZVdN1izLTH02Le5-et-JYV-Jy2HTeLHj5CSvAVIq1oOi5RS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfD80YsUnvt9BoNXc9dBH2ZR7YJo5EMueYqyjzpLCdnkCzf7kPxHD0Uhd_m35T9Fwpep3i5WUHaJ3cEn_mdkZkDHSHWZbizz6H0ahon5IWKDpHwEjyyz48GrKfH8tgxxQFGWU8QAuKVsxb-BhpFBZjU3ciGF1thS2xqsCMMPgyq--micS397mc91XAQhGig2v3jZTaZzyu42C1Qg2bKyBkjN_47u14WLpopxiyT7sFhoSj2K20E6CAXRcV9VSsbEiaWiao0mDSeZ2xZuVvhPwkzmumnzLTJCLKnzChkoniW4qlsQHEpEy7EqOz3W6YHmAqqmXy8JzR1DDMB31Rcq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAr5hW3Y-UC_sL614fpchsMbMNiHDyvJx2PX6m3HtQfW-V2SroRystZxQ9_JNG2hJnyP1m_ZFCuZFS0Lob3tPq-f7h7AlsMaymgZiHdQn-_kWRjK7Eax36hBh4tUmWMG--AWFRw231s3Ojz1EZeHIfPvQto54YbdwqYHJbbngBVrFXRqXp1j5_Cak8jIURMLgPswuDav4VO-uQ_Jfix1IPEZgRR5qPodTZubBAzTBkPWa_-YkX9zovMvwpDIDtQVeKWN9YdQhXD-RgQuxg7vi283u2ilgnEE3bhYYyS6YSCfgib2XL1xQHCxizFa3sbC7EjU5HC9eWrviT4lI75k5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگه عاشق دسرهای خاصی، این ۶ مدل موچی برای شماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/675205" target="_blank">📅 19:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCz_kuOF20h7vXhw4WvgjyO7FPohFTuvVxmmswkfpok_2I_PNCCGvJ_UMqys06jNJc0p9wQdctQfq4AOdhFKsux3ih0FxiFUGFA03njP95kadqDZ1ju1VESte6Uh5ncmx8U-shJrFG-2LgFppil8Pd7bMS4SQ0YMaFovH3SSHd6PNU8eg1yV-5TfOvmqFnEKLgm3lqRN45830R4SXz9dkDpQOJ-IkY9ksi_U_OGTpOAhpslaEA6YlpkzNzQEOZF8H4p4OYDtJEDeCPI1QSM-X2PhBvfw_dIbiPsh8V7K-4RIW0KPewCxaXYQvikmzX_F61VGwj3BVHfgswmMO7HZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمتی که برنده نداشت؛ مسافر در شوک، راننده ناراضی
📊
دیتاک با تحلیل بیش از ۱۵۰ هزار گفت‌وگوی کاربران درباره‌ی اسنپ و تپسی، واکنش واقعی مسافران و رانندگان به افزایش کرایه‌ی تاکسی‌های اینترنتی را بررسی کرده است.
💎
این گزارش، علاوه بر تحلیل داده‌ها، یک سناریوی جایگزین برای اجرای این تغییر قیمت ارائه می‌کند؛ سناریویی که می‌توانست از شکل‌گیری بخش قابل‌توجهی از نارضایتی‌ها جلوگیری کند.
🔗
دانلود نسخه کامل گزارش
👇
https://dtk.sc/0xgmj
منبع: دیتاک
@dataakcom</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/675204" target="_blank">📅 19:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE389mYu7OfGRdigaoOCPPmMX56aXnd1d8egGoP-F72eLuwbzOmWCXZ0WWqpUOUAUEP7HSlzkWrIrlz2irAghse7W4QCRuClWkpxpHLP_njH_ezS-cHCc7zwZga5S6XUDDIRI9UsDbvNdxW-IlDQ1CvXP0SeBddJU1JXrVvibmr71vVocMUw9qLCOEAePHoO23-aQCrgb9bhvhETgaj0Cy3kOqNLZ71mp-MQ4l-PfgELYBr8Vtf1L4GHAKHBnmkVw_cC84qkcK_j5ikEIRiOgB_UrykqDfTnEkknv_9ZrszeXS5PR1EXkQ4dEbqXToBG7h9Bt-h-E_qXWUxJwkNTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قابلیت‌های جدید واتس‌اپ؛ ویژگی که برای کاربران ایرانی ممنوع است
🔹
واتس‌اپ در تازه‌ترین به‌روزرسانی خود، امکان اشتراک‌گذاری موسیقی در بخش Status را با اتصال به سرویس‌های Apple Music و Spotify اضافه کرد.
🔹
با این حال، این قابلیت برای بسیاری از کاربران ایرانی به دلیل محدودیت دسترسی به این سرویس‌ها، عملاً قابل استفاده نخواهد بود. در کنار این ویژگی، واتس‌اپ امکان ساخت مستقیم حساب کاربری روی آیپد و بهبودهای جدید برای نسخه CarPlay را نیز ارائه کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/675203" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675193">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K3uzE6JuCaD17Oc-g0N9-5j8nSRkqhQ-Q4D82_mVPDHQayhPkP-4RnIUOWh4skhwFtg-604nocmMbkVhS4ylw8qyrGh_fCA9IbEyq2QwmJbfgzfeDtJqcX5gUtFch3c3QJ0bN5OSm9JN5iVsz5ZRZ407JSZ5UAoI3lpETrIZ_lqVyuVwmy3zGfSAjnZhCWak0SmkN5iiPqPPC03E0hMa5jNdmF3xSAIxEr7m_sHS68__nmRwSCic8sP0nHk5ryI25Q7S-9L3qxx-pb51g-mBwp9YWiEluLaryy3HKblW1JKRaUiufDlkeBqLrP_-LQuMfZf4PGfJSV9obniQj1l6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0ZyhHYOHGblY5FVg6SytTL8f08rJUNIG19IWrleGY8HgPAwJf6U2PksDAC_y1V_zEGnhX0CfkzaXUZ77iDoIYBvUGE_SWO3Dl9tS2ZhSZ6tUq59VBipjKP-0sgLpDjMUH5rxOD3eKLBa7dqcDg-7tPGv-_YvEjsPA1JI-0IVeLWsRLGGBg4PC00Xezgzzv7O2D8UC5HNzk7MiaNGqnZfBCqU0B6vSeAit07UfPqbOmM6dAyCiVyrAkCeT2DSMAHS1H_WhI3HT00qbIPtZteS3OV0dlMIqIbYS2S6M4ZrF6NWkyhMgSkvi2GNnr6fZcHNirMizK3t-i185r4Kd8uGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhER0-0PE_5oohtZgEC5AZTSv1NC9qCdl_TRN9H64DQ2JVW_2cjMNKYLhHlVI_GG4GTNKsGng8j_cyz_jNoQQUheDRWjpQMydw4CzqUP27SBwsGrN_qdPt4DQ5X5n1-vu3E0Zb1uA1Hdix1GsQ1_-CjH0n-EyBo15OHVkd6laH1HAPrSIuRQ8gYEpSgnsBCpMLce5j41lDWM2FdDuFzlMiIpF5iMLjNhGSuPyJpciKBUPZGK9lB2nqngCePNa7z3VW-zbNqyD5CmNTUvi2WDUNCqiu5v31fgfOFLXR_M3OkXRE0NdtCQODukNrgTebA78qS6TmWvYjn8nukFiWUYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUGkIA1HKke9OJ8ciu25oPy0E84p7lV5zSn6YSpOD43jwGysFqKiBeNuplA3GhoMqcyRKRh-WY86Bz4EsBGwh-omliLZFiDgQHCj30UgZWlvsHQkZ_SsusR90Glg_7RKbcqe6g0bBgYEOOe4GTzAvuEhI6S6qVEVtIG8nJClvBStk4Sgpm5FN3r8lS0-cIgKclPXpE8xl-UP955y2prmcDZpTp-F1z8G7AlqLXazjhm5tbeuDNnD3Lw8m9h0ia2VnjzwwI6hVyi0_w6zM6450s6cNvj3ozxaStMtIuu-RFUR9Ko9mmc7FM4VQ8FOflPk1Ty8GkymLCD-iMNCf0ZBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MY6OWsKJf3zd6vhtYAj1E-Fj-Ae60lN2a7i7yHD07yjvSXDK01sKvfrwIKgpzXcT9Yr4J1NkL5e5iy2cWk0hn4ThEqA5UXTIZTLr6b5PhVCFBLdYCDfN-jxAZxX9t9C2dCdxt_Tef8HGUaEw-Xq2C14ghuwOq_pphDCF5VXPFLGmXb8DXaUkykVFXEaYDtl7oKGyeZguOAZC-ioYBjlWat6Z2VoBNhkBsuMTtLJQOV56Gc8OrQamiacrOtacnUslmht3OU7ZSFmRYbSgWVr1id7WyUmXwanj28BgtJUtFmoCzn9uRdcXhJUvtcWtKNOeGTmpbOhzwOoFb-HwZJlNtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwZdcCoCnT3x9MgqErOX3KvMLTKp-DWIVEDPsGZXwRns5fesK4lLy1VpBvWsXppzP5H0LvYAqJ4asLkNWNRUPW-KKLWA5NSkTkYNqoLBYsAqJEPAxVtFQigX0oPEIT08_uIqhQdf3w4_5LspXFOqubTU2KrZWgr4AHynm3JKXZRS_vQyqP75V_UIiToC2AaMl0Rf9eXMs18xM2zLqoJY2ZvBAJRqS1fziRs3Nh2DU7jhepF41Zj5MCn190dtS5EwW4Q0h_3Prl5IpyZyf-aeSiASpmU4ztQSSunel5ljn5SO0jP70AjrOyeoH3e4O-CRNLCGHpcEPhLcru_RGew_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg7oFHsebkAkE6WzW5cQNftp3mJKEyW4lpbRSqvMZA7etkQmpFZ0s0iQqICifuHkMepyUp-MxaTgheF2enF6HYzes2EdZPfHEsxiECsY_-aVTwnZydgsut0csL0sPTtHFsa5eyH1DPwcui36j_nPOH9dlaYOvyNuf4UV5CBpy7A-3mvEwNAM1nDOkY0x2wMq3Q-p3CwVUNx-fuK1GKzKp_y1CRxnicDUG0uZY3JSFtLu6kobho5KPaxI2WEEpVYZ-rcQk0huB3LyU1sj59kVdLh4N4fakbvmh8xOYjAWbBeR0S_QkSR2XCHC64o--iSdszU3VjQ8l2xUL6_81dOKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OampnMp0NtG6S0YemwNPajfROP9X2CRBAEmJFxN6DUmrp1bWTVxBRuXR5UuyGjqqmGpmQj2z36soR2fmwen4UZD1ottn0rSmY7vqkmWb1vr4SfuO1mc4GirnAKv_8XTz8DzQaWJilazPSGova0sngfHUmev-XU_xYyNUmn7bqnSb1lsUc9PVTosWtKuZyIc3TDJihbqNZTM4M9ASn-ngxDU74Mkj3UoxOHRicwa3kTtYZOvJKm-RCFfyHZeqsRrKI1PasfZjtoNGS-eMFDAwBg-jqXLAKQxaUahRb1jxpXRG0p-Ia4iGy-zPydXahwMAz_kvlLgIlvYb-i1535b8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZAwHs-IaQanv6aqtJxyiI6CTHp3R3pCCs5Jd3CaZxMI830bT558vqp5i7_rOuMbQURUDTOFtr5VElJbyJAUILELSxsSMDv_VuKAK-rgtJr9SADUFZ4wqYpthCk93TvoiZDTbzzxVIuuc6VvUXEMxwLCSKBfwRxyGxrcBjhGK4hCXC378NDE8oSIb71K8nHAtRkvVKJPhqCrV0GdILIg6E7Kb6hPU5cgntIbYeowz4785kFmVeM9iFZnbynknUMx10xERWAgXaxWEuZPuirDM5Ekd5UnNGenR1Y2hBq2PGfhD67Rrjcpb49EY_RB35-g9H5kHTqdgUpyKWxmWP1-ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلخ‌ ترین قاب دیشب ؛ وداع مجید صالحی با اکبر عبدی هنگام انتقال پیکر به سردخانه…
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/675193" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675191">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8fb9157.mp4?token=gmuM4QJMNqSJOcA-PFlQKnDfdSGOtkZV5PpEL8-lZvTq5bSFr94-JxhXPIw9hfrvqwWV2Zv9mw9CKH4YOhdNwxjvlvfNhSGmhQ345IFRVQJAlGEqyy284GTGwdLNyBZHBIeIaxIXTPVDSBYfpT07SSdhsALo3InelAwFOZ15Qm1ZN2zHQrwzzZxwKo4pq171axK1W054PBdd1waKCcoJjkG78HjUEOEzjgrs06KxzkhFP-b8DhGQqDiIFJW7vi3vYA1TGO2NaQjXPG2KwDDtmKEwWz66FfcPaud1QaHIDijgToR8--hXBXykkoblKiRQSuli3YSEXE8-VZ8v66J63SHfOXfjdI9E37YirhhXUhzAg1hCHJy6ANBYO_eGCmlkU1CS872tf3PIPZVSPvAYNrvG5fDwjxDnfucH3ZKrt37M76ojZmRo2_B0rcKjiCUm4z1aE6w3GOgG2nGmwqJ1_QWGnAGLkDUFg78eE1-oLUvT6NlTEOY6ujFlC7X9uae1sHSiuvpZ1FnAkmlCwk7Jt1mRf36OJ6Mbm3yJttx8uSyRN70bM2vhB253TJFaCzsrDDXsB1vnyVFLaYVBkZ0RLuWH5DvXAsTE-GzhQAMElkARD6aLspLVO5HZSQFCtj59oCJPBYufHERBAT4XHaiGne3TGth26xZP04lIqxMyylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8fb9157.mp4?token=gmuM4QJMNqSJOcA-PFlQKnDfdSGOtkZV5PpEL8-lZvTq5bSFr94-JxhXPIw9hfrvqwWV2Zv9mw9CKH4YOhdNwxjvlvfNhSGmhQ345IFRVQJAlGEqyy284GTGwdLNyBZHBIeIaxIXTPVDSBYfpT07SSdhsALo3InelAwFOZ15Qm1ZN2zHQrwzzZxwKo4pq171axK1W054PBdd1waKCcoJjkG78HjUEOEzjgrs06KxzkhFP-b8DhGQqDiIFJW7vi3vYA1TGO2NaQjXPG2KwDDtmKEwWz66FfcPaud1QaHIDijgToR8--hXBXykkoblKiRQSuli3YSEXE8-VZ8v66J63SHfOXfjdI9E37YirhhXUhzAg1hCHJy6ANBYO_eGCmlkU1CS872tf3PIPZVSPvAYNrvG5fDwjxDnfucH3ZKrt37M76ojZmRo2_B0rcKjiCUm4z1aE6w3GOgG2nGmwqJ1_QWGnAGLkDUFg78eE1-oLUvT6NlTEOY6ujFlC7X9uae1sHSiuvpZ1FnAkmlCwk7Jt1mRf36OJ6Mbm3yJttx8uSyRN70bM2vhB253TJFaCzsrDDXsB1vnyVFLaYVBkZ0RLuWH5DvXAsTE-GzhQAMElkARD6aLspLVO5HZSQFCtj59oCJPBYufHERBAT4XHaiGne3TGth26xZP04lIqxMyylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهه نودی‌هایی که عاشق حجاب هستند/ روایت دختر دهه نودی از باحجاب شدنش در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/675191" target="_blank">📅 19:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675190">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghCg_uhxab_N-DBo24nd6zb_-JeANOuZ74A2RyDw79ydNf0cfXINh12x0dSnmYSly0LUSG73nYpv3GPY5_s1TOFBLtD4ciwewgvkyVNvK3Jxtjeu_zpdN2bhU7GJ-OiGyM_5_QdvNAH1jjSDvFCHv_GRTK1kFwC_Y2rzvk9dN_tlCXlgo06og2UuuYfCCvClHEJ8LeClzK5bPCmU1zLdjaJs2ICQY_snWnKr3yLJKXJxhb5lb6ITg6VQsLs0H99FPqMtJRS1-d3Zwty9CNoicGeJ-uI_QIzluop7cG8j9GJERGmnXMtYr03vXvCW3TbO01CQ9VY8TDsUlAdCXyjnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675190" target="_blank">📅 19:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675189">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3vO1ud3C7-fvTo8xwxhBaqlxNIGRZDrTs6te7CjA6q-AViQyL44ExIxND7vyvz70Ffqz1zeGQOFoMtt70FdiF0RedOpV_po0opTKQdYFIoS2jDLull72J9bIBG2xjTzCxyhu_Wvc3Vq2ToKc8ZVZ2lJ2Z_zctbzICV-9_G-wIRWfhpoKMOblvMT3a0vY5EGfGZXhfuSQQN8ZuowDMseRGF-K3CltM1iYrQDycsqJJt8NMVfZoZTUt0QBMxYpX1d_1gj3edE8_mGTfVpXvShXcp4xMYTDwezF3pvqSEtoKUy0vA7O96QdVkrpKs53_O8V0PdE89dHcb1JCB_LCMXJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگِ سطل؛ کشتار برای یک ظرف آب!
🔹
در سال ۱۳۲۵ میلادی، دو شهر ایتالیایی «مودنا» و «بولونیا» وارد یکی از عجیب‌ترین جنگ‌های تاریخ شدند.
🔹
همه چیز از آنجا شروع شد که سربازان شهر مودنا به چاه مرکزی شهر بولونیا نفوذ کردند و یک «سطل چوبی» ساده را دزدیدند.
🔹
این…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/675189" target="_blank">📅 19:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675188">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUwWETH4rm7HMHql-9iuBti9W_27OLbEinubrnn0-s-YjChT-rOI70hh2_aAxRkRYhV3EkhmPLw8z8sCm6-YPMYi2yhplsYabjw1BNxI02vy9u0NXXuxC53tDYYLxU4FbG1sIdRimXdMaM2c23nroWN5S9VR2R1dzc783vkvtFOMof1G3ysDokPUFfE6CO2AoqV11CFXobewYgkUaq10fGxuoV5i3xJ_3FzXWmRv8c9QuR0AEgrn_KnxZhXSWAv4aGrNwx4FjL2vCmGkJ5mVrgTNWS_yAw15C2HezNlfPLp7ImwrINEayWcDwWW-AEin86XKl-Nx9t5kBq1AcSrcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
ثبت‌نام محصولات GAC آغاز شد
اگر قصد خرید خودروی وارداتی دارید، اکنون فرصت ثبت‌نام محصولات
GAC
در
سامانه جامع خودروهای وارداتی
فراهم شده است.
✅
قیمت قطعی
✅
تعداد محدود
✅
ثبت‌نام آنلاین
🔺
آغاز ثبت‌نام: ۱۴۰۵/۰۵/۰۱
🔻
پایان ثبت‌نام: ۱۴۰۵/۰۵/۰۵
‼️
با توجه به محدود بودن ظرفیت عرضه، پیشنهاد می‌شود ثبت‌نام خود را به روزهای پایانی موکول نکنید.
🔗
ثبت‌نام:
zaya.io/TGrun</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/675188" target="_blank">📅 19:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675187">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5fd88f97.mp4?token=b3fXSXC_ARlSHXMq-f4QqeLssTep59f1mxHatmlKSsJxVkOWsqZP0wPNJAaVkkEu1SahzKzaX2kQY5rWjvCFtT93vl5qb9GeMYSNnNbi9N35AZTzEUeo3dCMQ43YyLuCErxyDKtd_ARCItSDVGJokpgtChPMG8mWBfvRtR6omu12KHlECRCS0Q2rzIox50tZRS-9JAkVtXd3gPaZvh8PhoES0y6UG8TtdF30Twyv9QkH1T2-OTVAvkgjgtxzQtQ0ZQBR0G-KCqva_6ZtYlFDjU07ucV3ZatiHziYmiboPPpI2dMX89E_zIybFoipYEMjTz6FTIQm9tLrJ-UkzhibQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5fd88f97.mp4?token=b3fXSXC_ARlSHXMq-f4QqeLssTep59f1mxHatmlKSsJxVkOWsqZP0wPNJAaVkkEu1SahzKzaX2kQY5rWjvCFtT93vl5qb9GeMYSNnNbi9N35AZTzEUeo3dCMQ43YyLuCErxyDKtd_ARCItSDVGJokpgtChPMG8mWBfvRtR6omu12KHlECRCS0Q2rzIox50tZRS-9JAkVtXd3gPaZvh8PhoES0y6UG8TtdF30Twyv9QkH1T2-OTVAvkgjgtxzQtQ0ZQBR0G-KCqva_6ZtYlFDjU07ucV3ZatiHziYmiboPPpI2dMX89E_zIybFoipYEMjTz6FTIQm9tLrJ-UkzhibQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط هواپیما بر پشت‌بام یک خانه در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675187" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675186">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035057ce0f.mp4?token=oMCr3_DcqwUuCC773_HsedgOF67_2AwzfAPBSizYYze022db6AU9EsilXheujFnakZp16PEEAEIEUYrQVIO3A_phy11llXjhNgI_S7zxTVjn18MUQ8KIbNn4cVV1cLpJE7NHwaCjxERQrN5fAyJ5xeK2WRLQGYFJlg4rsyJGssnk81OOR_LR5Xso5lrTrN2N5bWVsIffNp7_e7GTAZH27cyIHKq-_Hmn9-mSXexp8DAI-QIOoNNIwn7UVzKERMGS7w-XhGmAtxFg_3SUa-t5NInQebo-5sVZLcTodTULgoDWXvRfIdv4I99m-tfYTtnjaeXYnF8_DpGUuBn_2pOgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035057ce0f.mp4?token=oMCr3_DcqwUuCC773_HsedgOF67_2AwzfAPBSizYYze022db6AU9EsilXheujFnakZp16PEEAEIEUYrQVIO3A_phy11llXjhNgI_S7zxTVjn18MUQ8KIbNn4cVV1cLpJE7NHwaCjxERQrN5fAyJ5xeK2WRLQGYFJlg4rsyJGssnk81OOR_LR5Xso5lrTrN2N5bWVsIffNp7_e7GTAZH27cyIHKq-_Hmn9-mSXexp8DAI-QIOoNNIwn7UVzKERMGS7w-XhGmAtxFg_3SUa-t5NInQebo-5sVZLcTodTULgoDWXvRfIdv4I99m-tfYTtnjaeXYnF8_DpGUuBn_2pOgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این نون‌ها خودشون یه وعده غذای کاملن؛ حتماً امتحانشون کنید
🥖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/675186" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a67650241.mp4?token=DVtYROhBdZ8e4BGC0fsq1lEH2-uKzfbrc24hmEFdIDVgnBe7ZnSZOkSDCeZjFKaEsBV-oJEKOHOl9yPi3_Vh6c7xult1GeHlFYjkbA2b_qJiN0k-dra3mNnBBZ59T3V2o6k48PUBF86-v6ejQePqc_21z9fDCQlS6o-dMe0g6YcujZ6GshmEZQi4Mn51eAEb3cDT5kh7GLUgllsrCfn509zuEfKG5bMa8VfKAz47e3ehem69gBobwSufQ_FqXqNfpcCDeJa5rIf5ELiXAxFQqWcRFXS3Q-Y0HjHEz_XGAManpEvorN-RzFfaiKPnDkr-mH_2EwsRnz2L07XRbEYLww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a67650241.mp4?token=DVtYROhBdZ8e4BGC0fsq1lEH2-uKzfbrc24hmEFdIDVgnBe7ZnSZOkSDCeZjFKaEsBV-oJEKOHOl9yPi3_Vh6c7xult1GeHlFYjkbA2b_qJiN0k-dra3mNnBBZ59T3V2o6k48PUBF86-v6ejQePqc_21z9fDCQlS6o-dMe0g6YcujZ6GshmEZQi4Mn51eAEb3cDT5kh7GLUgllsrCfn509zuEfKG5bMa8VfKAz47e3ehem69gBobwSufQ_FqXqNfpcCDeJa5rIf5ELiXAxFQqWcRFXS3Q-Y0HjHEz_XGAManpEvorN-RzFfaiKPnDkr-mH_2EwsRnz2L07XRbEYLww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کامل زانو زدن پادشاه روم در برابر شاپور دوم قدرتمندترین پادشاه ساسانی!/ مدار
https://youtu.be/wGPuPBpm5AY?si=Z2HXd-mzpNNvhg4K‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/675184" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=QJCl0WAWMuCYsq4Ns9p5RY_a7MS1e3x9w1RpSpeJ8sNd1Fh3irryvzD_ePHu0SlDHH83fyNjFQCZlY-mmCGHbTWUgVz8ICndJcAE0H9LUI4LoHoNGiLMU_YtlKysh0HM4ePy6WHw8sawHf67w5xDNhZwonObQL3oTt28xvojgBPmq38iwwNvHaun1KboZmDscznHVxEv4yZASd38W9IudrkR5hqZzHpgGE-BhV3HyWstj9Od431reuyKOS3IlzHSwhLf8KhdStDXQiyoHj8IzzoP9xsgl6IRYk2DWbu-p2QjJac2TpbYeALFDClv4_r4HTlJv1WqoKnqb6Po1Ww_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=QJCl0WAWMuCYsq4Ns9p5RY_a7MS1e3x9w1RpSpeJ8sNd1Fh3irryvzD_ePHu0SlDHH83fyNjFQCZlY-mmCGHbTWUgVz8ICndJcAE0H9LUI4LoHoNGiLMU_YtlKysh0HM4ePy6WHw8sawHf67w5xDNhZwonObQL3oTt28xvojgBPmq38iwwNvHaun1KboZmDscznHVxEv4yZASd38W9IudrkR5hqZzHpgGE-BhV3HyWstj9Od431reuyKOS3IlzHSwhLf8KhdStDXQiyoHj8IzzoP9xsgl6IRYk2DWbu-p2QjJac2TpbYeALFDClv4_r4HTlJv1WqoKnqb6Po1Ww_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/675183" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران راهنمای کسب‌وکارها در حل چالش‌های تامین اجتماعی
🔺
اتاق تهران با ارائه مشاوره تخصصی در حوزه تأمین اجتماعی، فعالان اقتصادی را در اجرای صحیح قراردادهای پیمانکاری همراهی می‌کند. آگاهی از ضوابط بیمه‌ای و تکمیل به‌موقع مدارک، از بروز اختلافات و هزینه‌های اضافی جلوگیری می‌کند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/675182" target="_blank">📅 18:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ده‌نمکی: اکبرعبدی یک وطن‌دوست واقعی بود
مسعود ده‌نمکی، کارگردان سینما و تلویزیون در
#گفتگو
با خبرفوری:
🔹
اکبر عبدی مردی از جنس مردم بود و برای مردم باقی ماند. هرکس که ایشان را می‌شناخت، می‌دانست که به‌صورت گمنام در حل مشکلات مردم، رفع اختلافات خانوادگی، آزادی زندانیان و بسیاری از کارهای سخت دیگر مشارکت داشت.
🔹
مرحوم عبدی همواره در مشکلاتی که برای کشور پیش می‌آمد، از جمله در دوران جنگ، در کنار مردم بود و می‌توان گفت ایشان یک وطن‌دوست واقعی بودند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/675181" target="_blank">📅 18:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675176">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvJPeB3ES3kMueCClvxNXDPCAdEMP3q05zDRwMBeA1kzjMaJXjnlhBTze6p4xksucjgn8rxu439dcLcZGUc9hm4tkPy8otecosaFbUQ4lFCFom0ar9Mk-Y_y7z3n3Dj56hvh2uXdTU49zrVp3kPjru5wGJ7-6QAp0_7GUyMAM6vSYbdcnhfktzodpj1HcM_7CDKdBSI06ivSy6QTvZ7QlgQKqkxPMMGwU02lAjEYwGwklc9Vv4yZLsUR0I6lmOGVXUi1zZFloKwj5saM6puFUxznmAu0KRRo4ygWYa6AkT2qeVO1Czo4VgRy61wAOngGZwSSArdxiOtjvndghcKQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-XR8G3EIS2JNKOORUPM-bWDUxamLc1Yho1bmkMg7D4iZC7N2MdbHgL4ANiZD-qq6NRRk1N5J0xxV9XR8iZDOvrDQIFrA497P66sdnQceNLjH_r0uqAmLUxtNPlJyq43_uEMzyp6B6X1Qvr-oM9eHPyyjWRZFDA6saEkGcPgPB5NIt3cOW4Q4oRh5R4JEDOw-2lU_TwR1JzzaMEECpaQ-lGBmcd5Bk4dIzYFDnuvcxp2z9Mg9MQuOgIdA1Csh6ihDZ0kj4GNB0MSq7-HeoTU55LggcUSfN5Vk9EKBR8n6nZTKSOSm6lWvunK_bycArfAQ-QXKVG8O9sonQZO1_Zpww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت احساس تنهایی و ارتباط اجتماعی در ایران و جهان
🔹
طبق پیمایش گالوپ، ۳۳٪ ایرانیان احساس تنهایی می‌کنند؛ در حالی که میانگین جهانی ۲۳٪ است.
🔹
با این حال، احساس ارتباط با دیگران در ایران کمی بالاتر از میانگین جهانی گزارش شده است؛ چراکه تنهایی همیشه به تعداد روابط بستگی ندارد و کیفیت آن‌ها اهمیت بیشتری دارد.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/675176" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675174">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5r9EeJGQuN-2-aYfb5MdPbLoHcWv--pprjLcLS2L5PIw-Jn2kN7HLakMfBPOE98LDR-px43Hi4UXquZiyMKZImyT5wLr_nJgcazdS_iQy7NEBwDGRS4WI-WwFnyt_85fN5k55vbYccVo2wX-fPxfq7SR2AosqC6aqa9urxSdJxgKN6ssgVLqb-sEFnBeCZyMakRhQ4I5wa7cYkxl6Pk5D9KZ_52x_1cnuDfWDQxvONqpXLYtXBPUaY0V3e9Fv9ZC1OYJtR82ruU3txQh2IoqxcMy0v5l86DAS-d4ajvYSzmylqyWQ_tzkPuSNorxl6x1kOVQaul-2PK6B3-MIKrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش معین، خواننده به درگذشت اکبر عبدی: «هنرمندی که با لبخند و خاطراتش در قلب مردم ماندگار شد؛ باور این خبر تلخ بسیار سخت است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/675174" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
