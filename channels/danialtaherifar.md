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
<img src="https://cdn4.telesco.pe/file/NH1eCgYYCk-t0iDPlm3lHOIMfV2VQT_0EbVl8-uHQbQfSFGS2TFjXKe4B-ETZkywHR9xKj69TvmsXzdtWZmuyx4d1qRhV-W2Iph7hkRgUOPJe5yUP4gdf6YfNaXBu36ZAzBAmnZ0ZCboJ5nmzeSNwJOZEays-tm07Ekl_Qqux3_-0Bk7nl3PUJSx8WEmUQ4EZazCU6Uco3lD_05kC_jjGmP63PR3gwzZBQJ16CIJGMfj_ADcx13voBT_XwZyC5-hJnZTuddQxtXzGtRZyydQ55BNrAzbw3UOZ_jLbVu2tU9BYOFZHUJxB-0SBak0hRpoqyhg4hkCvWBzf1JRedtHEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 06:08:37</div>
<hr>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 211 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQhRo1FjIMTH3AQoMnVbL5a9_N5EGLJg4hfYqL9WuJAFmWClMJjiPW2hivvtCntRaZTGii_LzChXjK3A4Nlh9SGAPg33CMoAv14OnVYFI3GlTH0q__SXvlIeYY55wxzCvHBtrg9YX0zBrNsT8SDIT8qOfc908cLRjgZ_ZYglSuWrIp4OLI0qeHTl6eHLvd2K9rd8bhXDFJjy4AESNCrU_MtXssjak4hOlyk3NquoJgjaLLN48exI2YyLsc8W4euo5ty-WzSP_fj7sgkszXgGVY36xHaGquighwR7bfMZ0srbtJvxVYbRQaOxHN_3Z53YFjXT1RjLDrsFVWj6EBM8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 287 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlVZolV67YQ-ifkeAuW71soksEXpSEMaSIUpmcmXrCsNDvCrct0H9nS8hxhrtO4OtCmGSG7LtdQUtcKNVBN8JEBZolCB8Bo5MXzDm73WX-Xk4ksRvqte5edppYhMMEcChiCOI4Ollds_xjXgT4fQxxA6YodbQTBMCPwPmRSAffOixYbpyyCCQ58tqRhksiGHqL09FHy_0LijLozdtZJO-ipdx-jo-kR3KxLzWSFA8LA3wFJZyQYUcXdy0R8y0HRVgAX483yt1QF_NAG_vTDmoI5NjKMfRscNvp8rtwNQh_mskuuwoXumYeLxPM6SR8gUdpsgMfAzczlLnzjw1WFXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 632 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_neLemS7bGmJPFOWxrHwhFb9P6B5ZPhs6jN_8YmzDwSscyoWLK7OMhGxBjn-kVfC4BlZzNRzYCGgYpJjt8WsQx_bYyvMbbQVFyYeaUizLQ3Tv0Co-tt1QiftAxDlhDVJwXAUno9wbMMZBeGOPPIRZKqaXL31329ndwLcyu_4ap8XJnmP3r-oUrAKAjzIEkqx32YmkQVlNrQ0hP48mhL22ehyQDmH06BuRK237vVLTTEUIbecWyG4oe7xVdpq41mkLqAyl8vLBDGkT_vW0bmmoEf_rWYYaAgQPVUYLFjU19KjBKpZlIm49zl5m8OWQAAhaifg8AVay7f6wpIZQnPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHGv1ouSSqf1vA36iVGen6Smb5-xp1l-6DhtDDx81TE_-b3dwtpDpFbeVR1XP5KpxODE8IDC7AVLSGuEkXzDE_-R-LL781hpoWX9h74q3QpgfT0nozlxss9Mr5AQnU90GMkV3KDyBWXW_7sAy1VRchhGODrYTp5QFEdLNCtIaNB3vhs4HfZzto50-ZcKAdKjQ5ZTF3unkuB5aq7CiwfIrtIfVfHpnTFYcWFNpmIaEgxqTk9PUt7S7wv5n-SKNF16oRgtbUbZKj3kEJ3NBWqh9M5RVl8OUsfGClimf-WHyN1MHspgH2Y0M9PtRx20VCS98m2oXbcP1B-OzGapfQBSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq97uf9NxSUCVj8tG6pmIhmfbmIoqTwlRIQdudA8Xj8DQP_CCT96FgwPInU4z3inANYBshiJx8VySiXloIYMDHX4lT5hxza2fqtpo3gWu1QLVE2wQW1UTxUzVWgPPFsCS64SOxGqTPIM5bBi92NX1NYOIUfAiWK_0cM0_I24DcC76x9732eEohUcsIxUOiieLrkG8gjdNGP6kzsP9fsfOVbrfwKcPXuNGi_Pfd0OlkP2qgs2-NAOEYXu8JxpWj35iqnoAcr51OgrRHGr928H9z6XjUTB8hE-SPnPVvfJHvxMCyz-j02lF8vdl0X3HRYPk2vM2byYjGEuXXFo2a021w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 746 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5xNMwfY-GppXUzJvsgHEQe7F9fs6kkELfd1138KC-sPL-qvMqTWWQCMTcGBi6ZldHPpPuWdaOiYjF1bXBb_6kkMVVddM1ZyjGtlcUZw2S-8WXxSnh0ayTbPWK1CWd_Mo7ccQyXtZtP2IA9ciq4TYrTmCBFZWi8K8fvBfqlMB6W0rEJ98XzKB1l0oy4Z1Q_DLfBG1EtBohBt0QPv1tgRxOOX4ywIYicC2WVI6_xsToOZjxrx8rHCPmKzTGgvASFpjJpNutbzD3d-SVKQW_sI-sQUGlysZrkaYewy5LiAFXzHzHeT3o4UhBjcaLzmTCRn-RdWTuoC-TfAQaqZ3s3npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 956 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-UEWa0nP9awUiwh1MGLtyKBxLuRkhVpFmlQjZzXE_WM2EJs9RJGabrvyb2yQ4Qh_uhLia0fO07ZHtyEf_riTBHyoNrVJxiDRKwOk9gJmdm3SMzfRHxanwWNvj0-ZxaW2qaxyofXLAOlxMYUWCzeEgmTzKjKwoiLwSzdwPSSABj4Jotk0kaFytAPPpMxT5Tj4he2sgU4b6pAQKu2K1bGkVohe7OrRnLl9Yyqudvb4ufhA6BRW-oCdbLKTrF1PHPmz1rBD2puR2OtYfE82ou9aTsbLmh_-daEhDmdLCdOuYoirXUCZIYWh5O7LuhiWW1Pd4R6FqLCTF-MjL2r2oFKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6PNLSQ4Stx_ngc6j9LPVkQ6IMt31YwawFW579B-T1SlvhYAxom8ZIAItxUswDcnn6R_gt6ZnLTT_Us6So8R0bJDBPVwghoMacsZBkZOGIbYcget3QLvglUp8YD-RSfkzzVmD2iclR34KwMvre-gYmovgZ9Nd6zzhpDVQ1XsmxTXs_P90k10qFBbWLreUzekakI41jOHp2DWLcE5e5eUbugKzY6nd8rlhIQFw0fIr780odkDB4iZ8n8iHRzaGcc-T70A43T12dukClI_zIkeo7Uy6OQNZlI263CBaH-fdAMZHpkDpI6U3_V4DI_2OfLWekfNIFEIX0-phzAbhCAVpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK9wW9-FH1FSAvAivvhRvdNdQvZqJeW-uR5orU9s_L3-5AJVU4DafifpUv8XLRPhunsAvngq8novvGJpE-ySJYkUdaPyDYtsSxHHcdqzE0fKR-p25_YNoZnd5Udti5AFuqaKi1MUQPBXVzO6tje_Z56sZEA06Ux2HMFp8fYDg2TCKLAh0rQoWoFTQvQUiD2Mp4CD__bTE7NizIeSp-_JxjjFznxe7VWftp-axevg4_nnIIu4wCw05-oFzBK7JjlREaqNzihUvI9ddzsFQVQMY675cX2mE4bESsKH7zzcAlSif9RSAKJ0IfCHG_4Ujk3j6OUkLkDZnLWzqIfPZy4JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgXZZ6IID2pTSxK9-4MupARv7ad-HR0V9l26sAbeyA8GShSdq77Mhccjs8tmjthdDvh7vDAgTRK_dT5KKmHTpfzcHIeVlh0WR9YtrYMdydebwW8CwYfhR8D46VgmdDnnUXBJzr3SZp8JvAmot_arVDnfAgQ5oWyw5nnpbDVsBj7Uj2YpVfg5lD4vOkI6E_Xo4Zvd7f7Kd0qVPIIHCTR116AOTg_V6z6Lv9mi5yKf8pBDgQqHyFJi6Im6lHRUwepqS3GaGqYHV8OLgkO-zDDOoNu_lco9Bf2JI0Os1gj0s-ip0HlmmCMRAw_MKsBSLjSY2V5E1elovgwFzWKRN81C6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 849 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO7tY-1h1aXZGYq11m3sRlTpU-B0RZPLiwtSWxnzeroDRt8J74rWRPttZytQ8cgfSqlTJOZ-7e-l4WuBHGnsm-prSjVyNz7USoYX6QJSaptBNpileH3Ig7utha7rzod0aGwQxvdARJIktMLse-WEsvBVaYe__xigG8YeBQhyI8spfgjORfWEQVT-bLo7DvuORoMfXok2GsYeNzv4GYxIgP5xBVAgz_mYA2yOK0FtvjPGTu7IArOGaTxgbD3YX3YOGE1owuTgO7EVKDhfqPExS4SK444hXvev13zbb7R0cUhBpoc2FKemcHqB_NvnqJoedAP6cf9_nnAgwdKhXggZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9f2qIvLbR1pxjEbofUkTUQ6ZFhD0TlmL1Yfa3A3USF27XnvmPhFKLIvQhy_DudBBTFprzD8gUPQksSiEUnPxMDqfr3qeftUuomVtJxgfDb85RSD_kOkxewLYLrZK4VYKm4-YBP8owyQFyJ6uGis8995vgOyrfPKLIfxpQGTkWnlGA3kF35I_uhcKpwGGMlTqDtiRjBNQ7tNuYcL-Vf89SYLpn40G_ShVYWlOsQLdrALrWsIz1VOAaQf0OK4Xkks2IJnp0gm6CpAG5CNzs7vJfeUik1ueZ6yFZDDP_daRb9RQr1ju34zzBpDFlrPIH41lGDuR7SzlCsfqR8XVT2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB3NaEhAO6osx19QKQt3uzWDH0JK8_Aldk7UrDCmouhBHX1f6LrTfeJQfZefE968dzaCkQ3gy86ZjG0doP9Sgm-yCMR5_Im8j2YDlNXMqC7cVMV9NU22WawIXxQVOFN16nGhYAgAMGaO4XDo2kZNoyQnUEDFUHn8ua3ihEwWYiUbTIXHDS78hgneMW22Tv0UtdqAm3itKmjm8eN9P-M45uY24cJqe7SreWBuI2Gm6wlKtmGkWuIl02EoJWtP5s2-apVpRkfy7mmdxLU-AU-mDbR2aIDsAqWunsa7o5I9KIbMuciUp4ayCoZ0IgP1_ihmCDPbMWGQr7Ne49aEwffGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJoDFlz1mWTefQgNF5-hYfogXsgXFOgkXmH1EJeWV7A1xWORbC30lG6HpI8_pyS-NTInmZx5KKVDGILmjBuhMkDiNIbQcwJRoixDNPhTxR2YJI23l7O7-8-UM8XR9m91DNKVWRrpdCmDmgWvWxyNYKnTaj4ntsYFJx4BdY57vrYDd9vTphpbPWqol2It9n4PUKxtwWi3AKUibzn4UIs0pX5qh_MyUt6c0yTLw6S9hDyXkikZL0U9Z8jJ9ZI_ZH-qk4GRAACYlUvvwUCyXFY_euOTurcQrt09ISgM8QTB7nw0lk-1WPm9WfH7rKAag7nQTjq44zHzluJanOUc_2St7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJrEUHiOGT5mv_NeK11xYgpbRyTGkaYgG_DRtW-_b6CVzeHDGX_dPAOgXFP9T8n7hfnbOwQGvTGPWH0UCGQZKgl92fJL2rjuXRgb3xEcG-AzSTSTMzxFkAEB114c8RPf88M5bOWXhO0h5kEQoiMMTbWmQjQRQzdiUE-qpSTr4qh19lxf9EQ-a0XFfhD1XrnZbouTb_uUTC8fyZDG401ax46kFOyf6__tfViWYXFx6Gm46SelmE_UTYyPCfHprRRdIV6bkIdpXt7g_n2Jb4btkL-qPbdQHeBFaw7PCuNpxgGeM-M5E2OfQKS4TqSzrc-EPYtW4O2xHHIeVLdLbH1eWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VixfpNWt6N0Oo1NN9o2mdU_-gx8aFsECARR28GdblA5IZqdrRBzVln1zHOEZqy9-PkCq6sg-Wg1qqhwIJdniIOIXRuRU1uBcHgl2tvQDOw83qqXrweF8V_WpGdVx9Tx7AU8FSMu7GLHAaJRm1dIDG2HNkeutVSV6eNwvhEL0Lr4ACPfytgKRn5cbL3TbYT4tu--dG1UBDbt3UQ0vwzDQU9rHJuhvDPEpwp91e0PTdxD5CN92uaTPfgUNSHenSchTEJfUoRF432zl7nWqyQTKjAwE5rUxHmwQLumzMBu7ddyrh1qP_eWd7-SCeXFAX-f6HkfQGLyNXOtkHojaJ0rBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTB0TpcfxSsrOF7MVyz3b62n0CUUbZu-vh8iHyBwFicaZ5-kcpNbBRK3wW3qCZiNopXaDS_3H_y_WidohjGRMtif0vnefzGu_L0RrG2E4yS-bkA4AwyPjYueitPkdgC-c6kJXmUxFdhNS2yMJVQ1adilmzYgLN_pf9cu6GmzekyTKFLAkgpfXqlnix-uLm4rBtG0LWIQsGCK1FWJN0JwgQ-9f1Kxz9ofPK2-zHEy2cNfteRswVfY2S-R1O2biepqKpezpUTQxJvD9z3nBGZ1xDCo4Vrie_9uvrEVwj-vmQPOK0OnfdkbLAhimy3CnwGgrd8lL9lgaSCN5k6mv4VMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=sqBln33j7CJSdGUxfCC2eslhT3Nk0gWqOstbxvKTmJLPCHt6OImoixBJbixkDLoYfciGWbYJbaI-AOhPOe3eqAtBVWQPxTyxYaDrki1Ujvm8zVWBa9wuilHoKgO4c7JWBljlqWi_wI97-mOWN628Td6_62CFfII4Cnw9WwAxhBPtqmsdmXFzH9nkZn1rkHji_NwuzBWPfxYVnhKQPG7MAp0lDi0Lg7CiGBYL_AjfptSZhbu9d3thZ9bOgAB0hIaO0nHVlyMDPE5eqgMQrZkw0BpVwAhaT5L7FJZDWbd9f34kUoD-3woBClr6FVtxyLCJzAUtkyTRDKaWWROskyS16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=sqBln33j7CJSdGUxfCC2eslhT3Nk0gWqOstbxvKTmJLPCHt6OImoixBJbixkDLoYfciGWbYJbaI-AOhPOe3eqAtBVWQPxTyxYaDrki1Ujvm8zVWBa9wuilHoKgO4c7JWBljlqWi_wI97-mOWN628Td6_62CFfII4Cnw9WwAxhBPtqmsdmXFzH9nkZn1rkHji_NwuzBWPfxYVnhKQPG7MAp0lDi0Lg7CiGBYL_AjfptSZhbu9d3thZ9bOgAB0hIaO0nHVlyMDPE5eqgMQrZkw0BpVwAhaT5L7FJZDWbd9f34kUoD-3woBClr6FVtxyLCJzAUtkyTRDKaWWROskyS16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VToZEphCaBjNY34tysycQsl2NAeFah6RzGJ2CGVB0XacK43PYAJGxIs9Ze1xQJmqrnXyuvJwPBtofN6uFr_0filRfFJ4RBBmNLsN0drpyJ_1N7tjaQxQHylXq9WDfYcFHs34H2VetzwjSsk_4tRvHfYhKyYJmZaSKvf0k13aVRz1UDU4CpqFIMLDWOCESSHmeJixwcwT2bmy5s4fq1tljymn6MYs8b_Aazcomdia2oqXRjZhjd8RuFUJXJVDPYk6xHpgxusjtDerIX00rjG_SyOO6bQV87aIO0OlKRQQnSh4BqE26BCeLwsD7hXJjpT5z24k_YP3V6EYcjsCiwuFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdcFKJm97joGIyOwRpSYTVAdVoMVpK9-pAj6s4pG30bMIYplPAfboBaFIZBUc0uIQ-AUzAyvoCIzSOTWNjNWFYtUqms1AK_bm92n1ICZW2bc4PmQ-fy08ylUJINiYsClPBtJ7A6Ru3IgctxnjB7tMEY-dS5LFkr8cDCDy80KbFfJyXW3A4rPL2ddNBPc93QkoDxX3PTYvcXSkwCsalfyBcq7lq972pLgITEbR6cFWn8pFEH4r0jd4L5ljsc7784ZeMYNC_2gJIYs8SpxAzBeXRWlqavklbOfxyhPEgD24xZ3KnJabjsuJ_nTOOKZC8FmgJrJvFizemv2WevlNflRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWKDgg5YvHMLAMxu2WLAqjpKPxNORMwAYzKiDBRx0wzMr5wl9eK3cw59W6PD9tMGGsFVpK-Ea30Z3pnzcsS8D-rOj-yDdjpM_cGTN5zvDiZoLHD4cF48O3bR7DPmypxCbLu66BH9RSdfbPFZTZfwZ8dJ4r-d7_wu8mjZNEe6XNJBw4pXQpvbRXfM68ddxn96ZMXFSdyJoDByPePj_xIQlbrG7vStAb7F61MugKZyrQVIHrOORCFxOrdyNcFbo-OuMUuc1b9e5y-9fbjdXkzMDfi4zuXzL5t8b5AEq9B85_J8nqdypVjPen-CkGOhqXAUxogzA7MsHJ7WrASso8--Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3UAtSY1iemKptjpq-2TzwBbDV5NC9sEo4dc7v0qwmOCPZgIhM_k1cXw5IXVcv05AowKWrcnywWLEzLOZgoiDWiaUV-jBTAOkcuGmClcOiTvGc8Amr2zAZw1F5nFJ96NA4FeYDGOIUDROTlF3lfDzg1JPiK18S7SgOQ1ZBJEwYqBi5o0LMECulPHRHOGgcENbrjme9xH_7yHBW5QqusN0TcSxH65nIPicQ7XZLTxBDZEngc5IgvyccIZuXYNbgQFcweaCODAVX61VsHYmO4p24s88p0ZUBq84Ft8SZQF1PdTBdsTCSqS1LY2e6wUkVHqZu0Tk-iS_HOTILmRO_jbrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 795 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw6KpZFD3QzLQ2mC41mO-Njc8xKbh-U-3pGE5FWPszTAiRyroT6Kseqz-f-rbXKOsWUtdCZNf1Z2ImDcIRhD1mTit39XEC2neHya_tmHd8ZHsjkt0PDB6Zs-R3F2hX0GBvbC65KOPG2pNe4v-4P8GgYgFPk6t1qc56o-b1pGYC8Iie5kMkKCSUkMG0aIjhOcrU9n8Go6lp3UDDSmRnijSQIy4_luFyzTH3E5Y_SzQx22MKjpMs72ogk6b0PkkQCCsWT-7y4By8RQ4V7CojrtSUW95AXbnShnZ_vAG8D8YpcMm_MIKhCAtz_oBiTFbYwnaqrtSJfwt1admyzxkxqG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQZGDYAoMqO0JdFnrP7i5rl3EwgMNDf66mIHQntGDkXpICdZIuLAwZWu8_rPkuacuk9dAtS0luphihbgy8nXm2-nnWuJPfZEvcebBU7Lt-qOZY1l3smcfTiYTLuKCaaRYEjX-s8OjnmNAMXv1bybTTsrwFLXoV64AO4CoJQw1tLs-4Jcwdxmra4YgLqysdBJ6dUKRXFbGcZnsK5dh3Ue_Eg-dwVupd_y7FR-wOSpXrAxbIajgOzVvvuSx3c_EhS2LmCQuNL9pfqUMEwQEiotEMOnIm72nedTdICUVVWWBmUw4Zfk6YsDHbr5EjeGPYh4BArHJmcQgh8XYQqlpyiCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otQQKThVvD8_T-VYj_aRQubvNv1A1S73o4n7ucmpkQWy51hYjuhDunFv4neppueKJYKWwpYsKxqUQz844qYuniDUsEpgpoyq7c5BnSrN-sw2o8v413E2_0-pU1ZWU7FyYw3Qd_wJcFiOCc6_XFVbGBrc9AngO6BOnlamdzPBOoMUDDLj0APJCV1gkphQGslteKBDz9AyL7MW1GMxQ_4HOyLBB1Qdnr3LtKK6EkWIG1LXXUuq0lNyPNnPwZTy6SyXE-yEhIMIH7f6FOfS_uwydvOdzO2pUuVEC1VnidQLFj4O2MXNNe6r8v4wsxYEtT3XK3YpQcbLc0p_MWfIsKvIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHdhvf_H7SFIq4vkORHq44ySmJaS0Cw5nfG_T_ljPZ1SkmztLNjAS25cbocxvHK6aNmuNu_iyvPo6XzGKP2UwXWwoS1lZXwBMDQZ418A9zf0rfVno3YyzKyypLXNEslmsw6NFLrdDy_OdXSYhBp2rj4-OjCMFroNkIhtIig_csGhyGQGa7J9OtnN-sIN90mmsRQyrhspA4h6M0TyMnAHMA7MWlsawDGE_oGJuTtI92FacppW6fl6OsgDn_nhiNsMRbV9BswtX4zVk5WEwQJeXY8kVGZ8XjhEyR6nsawEjPqHiq8mSJNaSzATIlQD41TBXNdpmRvxgn63W3kqwT-_nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B45mfiX8hD4ZJYAQKK9xrLHuKNNq9zgZcl6xkdeumgRRy_iUWZpZicfw7t63P--OdSDPffykxN9ZVb-mmAw5BUcQJMN1B0j_jmiqq7QjMhM-GKP6H7jo-tsu7yxzyGvCDBWbKZYr3Hc2uwhS625J7J_Yi2vnuC_rh87QT01OWZa4CuPpckUNHffPBsKXN-25k8LCOTWCFoTSJREKYYzBkJgOSyoiC9UnV4jeqAZswJ2HuyylD71soz_SkuEsskeyq9k4zOjowt8wEfV6AgQFk6SUZilf0Si7M5SKm4wYLKjrRwZG-cKeRu3BXiH1-6UMXP_kvHEBfe9qcwwTPI46rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwyv65Gul2IgLID4TOv864GkbNRib5mxscXvldU1CJeM4UKiOPRyZyUdZRYiGWzdOdY0OtPe14kCafvJKELsJVeFg3NCj9fF-jUqdyIG9GYZ1zHpGTcgcmH7d9STax_Ul2_bdGSq0gG2KBsxkxcu6IhSTa8jLL1NKAn-25uW4_vjzrM5gTEOU2DUHlx1i_4fdBpp-v86fbZ-frRoN9cUcO__32DF4sFhY5O9SjJrFWZXAaQxn9CoPmWfB6bOt6SVVCTQt2-KoZe8xZNg47K0uEY08kNeMpIJ_fMTv-QohGG0pudQimNdxS9u59Yx1elUjwfpXOJHaHoJdZXuD-At3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnX4Rnrb20UFyUayCMtx5SAZpDuLPwAK_1i0BAT55LKP8nNTUnep1IG8Xu1Q28JYMdcx-AvcnoZ4filAUu1nkF3Il7M6PR2lHUhcmAuclwotVpwnXUmD-o9kGwevq2QH_gcsTUmJGr294o7RpFVjgft6NjfugYwOL9c8ivKrkgSCOM-OZy2P7tZ-_lmqWOWTbKg7zipDX6kYG4o79JgJBQ6iJjaMJLl2LNNYDefK9BH496qp8hABaKvRPBEvdAPeb2Lc4gyVMYy3M-ED8avClOkO3eagESzXPMrWXLEYczRCQYi0wE5FM5vvCeyttTgF-ZfBysXzQcZWICVAAITHQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqFM7r6mIodxPl3s0pxoH3Dq3_hjX4UctZPEdTlHa9zpNsmNxTuhSafggnxpojfmI9Dy4UW9BF8dw6xSEIa_Z91RYENSGddG_9n-iSvgwNsf6MRsxRmcq8jS5UQ4_s7Mvuf_81sEpE7I-Yd_guF5TWjsZjqFozdwt2zoI4w7G3jngUdvty1f8QYaLENqZn7AwuDF4jwDVlaBndEAIyWX-6mQX9HYjcLmNAZVLw-AFs2ZaQl3QjBryn6dJAG9jY7jqbT9Cr3wAr17iVKEPO2-h5Q1-k_Pt6LqOdzx-J_6_EGA3hDWu06r7Umml-HOHwzWBSYGiUiHY83ewUtJ3QwXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLLIC7IkheMZ3ZfhYVQHGjWcIXuo8jfD536muPktexYmlwgA5ZD43my0W9n9vINYyj5fU9FQoxMh0sT6VR-YZ1GECSnuVhmwegkn8-FNg4ne55NPRDGWK10hdmklaIn_oc33BC5LV1NKWDUrHCNa0Q_HJMpawwoRZViRF1bwCvb-65YvlAnfdEd_Gj3ay_3w8DN4rjeOhXaq2p67E3oPHCM2UlnQkvNRg8uu6wiarly6xxhe2nIS8vZ__mKUcm-xUucLHaERO71QxI0S4hteW5Fe7Vt2AiFovyMIVo_di9OJ-VnviEXnu_aGhfHPf0xVlti845OgsxcSPsmRCWgc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fpun2OE8lAgeq8lT3zYe65U0fYux0COyNg5YsOhJOQz-dWAJVlZaFY8qhJcjJ7K9bFD21UVvfqOV_tOtMB8IpE_fsnlt4uJQJ6-YXDnqoctNePvXi5cbk-l6lkfmBsRjQPZVKNCmM_zX9e5tnq7xaa-9I6TBL43SZVOdz70QLOxJWshs6zXgfIzNaq8X9M089hV_NhKCAV6phE-4QWAVu_rmbxXdcQVFIHUZxE2z7HyAjTYdcN65IHH7f26U2jqYB6kvwFbeK4Bx1ivTgWswSlA97skdAr-UT-4N61MJk4uzJazg2yjh-57-4nMkjRTowS827jT1wBysTnuO2eOvoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezPcWoj9A7KhIY98cStYKehooqlojpCuVZdG3BX2b_yIf7GAGz3OWzJk1LlxO4PV2IbtQ0tLwkRKb5lpOPlHaxIdj1Dfai8RagWv6c1ML4ZxfKd7kBd6nIvXHHg_SSVph9UyGRbycG3odtMtR2hS9ICFoFf23K6mVjC76CuMpj6gVrQoAPtLZqvSuw0QwpHQ2-3BiZ3veuUvfM_8n6v3Eo62dBF1ea6XGaxQnFZHePw0DrbMG1oSS4AEaE4eJiPaD5FZYGzYZelvcsrZCd8sNpBGt_yPdZjnqojlNda_TdaNkrf8tCiTeBu8FxPGhrC-bRx1gNFn-hofwepmOe4SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAKtGKXWIloegGjndYKtjVpbIHk_g_8486-k6vrGDAZMFxG8JI6cqW7mH9vUDKQ1YwfGr8pIIKUKjP_O1lpe1mKIHD-3DT-Sj1pVbJJgLlE3x860mT8P56UYV0tvjvMftYfHLBjg7L5i0wxkx11NNef94C9RuxfTsb3d4VR1pMJUgordiDyYiglylaEmj1w9R0i0lNneve7peT8E2WNkGrsquOf-YG2CEaloYyelpsYEPUlWdzDYCED-FOECoiTMBWyMM2-oUjQ19WIenIdb1GWckFcb2ucEbkfjvSsHUihDuaWfT0MNa89AlCf49FcbWKvGLBUl1A0nBSw8oorThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlXxOWRuvZBh8ndCndTusKFudRBkDPxOrrXoUjDzckcxOh_XqyIzV1Q22syIhWxoV1lN_zqJHU1VOyuUkvoql_fDVSu_6rPRNIb0tyxhzTgqc7IRkvTsg8iz9ZjyM3ogfeMKecUhzceyhTGBzSR4yDLafm1JtWEFfoG2uajK7zD6s2GGHT_VbMRFZ_vnCUTv7E8PR99ncgA0S5uqr-ALpMothtC3awx6LljPFBI12iBeyNcBHFTE_Bc71fAOuuzZ-pKV5ho9TbM90xtooQi_EseUMjH0vufpYiF6Gg8e4dyS0D6wNsSZ8Qf2VL9qMIDft6NTRyKqjvJMDGa3HtkOFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMAHJP07_cduoiPmlrTFNypMRHXWDwbW0dubUw3TBZ7aLZUUzeC0o6wpOE7ymcf9GPPlNACCQgSAESOeyMfvNQHn8OmvEm76EEm_GBIBB-Oa5PNzBcyOhFKmZH4xPw9LN10x43hHHQ2urTCxzeRC4sZubfR9HUqqplRKuT_6YuxDm_-F32uqaby9N1kiNzfrGCFRNjkmrMsu7wcNqo9_eblFR10IoLvlZpUBPP2bgjdbrO4tBK5NYaRbBNQntICczOKqf0ZQ8yxLAnE38XeT_Bc2-uy8-dHgGu5mNqcwxzWLNmj9vCaNZMQb5WuxH8UWhyuxcgAMb87ArZtzz5YmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Vjg1Ir5gthKmXsZ0TO_M5DOOVSc6HkH-JTVIUfHij7THYgOc7WdzSVeL5gCyD0aFts_6IYI3JCxyPiy6BR4hpFJbsw1jSUGRODxPEK1dE9PA4yOjbpUVACfEost2-wgn8avYiS-NkkLRsqhpi5FaiDrPigGoDqaeQSNM38qCIhefSVeucB8kyFDZB-rOegr8lQeKOTcrdjHav1_5MqibWgBBWgNn9RHuuCKl6idmaWVA-KiSt8P6icDkCkVPBvFX6WrvK5SlISsyijBlYgiPBn4TsE65RL7e1PBJNMSg6kOBdn-ryEeJY2XStQvbYT9eeiHgJBDWQM5bHtwuj7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvTlMiI7FBDlgOaXezdJ6zJeL1pUnNDkHzQ3pCp1wZQ4qzjq-1-1XmgrfF1o7L2oWvkCRDO1gDLwMqoYm87yaCnOih3WVn82UPnSFHUep8s15XyteOOGvaiKecG1OpzABqQJ2ZgPylZe01_HX5iJkuIV9iQ9hNUavYh5YU43Oy63xi6_yLMNPsPuso87Co_r-6x31BAmogL8ydG1wIX70CyIxYgFkB9VsbKEaxdMhfttgaI8yY8PN3ibgcjS2Y4labR6D9oT_W0EokAxLnnC3X5TKWG2hrDTPAUyRCXgKcu4UoXfkZmm3JrHai7sm3xP5hFrfxdoRC9r6PXhwB3YgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAJBYmyzMhtbmL9vKXw1M4FKjWF8zBGXAgDQAgNFOYSFn63q32df_YDJzQLBo5tl_TNxPfc8HG37oKXqSqBMrvvOd5Xqy_XNGNByt4707f2_2vXVERRfOrNJjS4a1V_mltJ7px16mZb5A_ZjD_3j34JmAx7zFb2D36241OBAFUXmV9BWvfKM-xFIE6tss5wD16mgoqHwcdiZb3rpDVUcEjmKzEhOoSHuSpbNpnBytkwAIIs-ieVAgrIb4XEwNKMZ2CSgvPD6HWUmNqL88to40F588WK1RuDg5OeUESyp6pKlyLiLDlb71YIC99718_iePDHkCLupIxFlrBY5rezazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHMtk4NjCWUjEFCLXU0my6TNP1MsCru-6VJc0tUJv-boD2_8xEONNc8XNj8dk_x2xMvoOmdg5qGpxiqMB9OKzHdY_75qyZVlbIlxT6Pl31CRYMfxaZfrRZ0-MMZtMvHsNFF6gaiSHFJM6IjvOl5NFtF7jooCDe1UaGk2j2Q3_gvsBhH_8vo1nDtiyqIFt7AglDoqt97TtoqEbeRL-7c0gxlLRBfiMAklq8kZ24NgO0I3ScOqxm0LzOovLDLSv2_Qqj92YWrvg2Xso9OYncUM_P_9DO5iw8Nz-bC9_CZ5pB7d-HZYT9NvB9_bwo_Z2O7HZYmJPUjB2Lomol92adozrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Tcdxuuk32BI6ey-oNAxFSkeAkWM4zGUdGJNXvRcIp-wzx6D44DDc3ZAuz8quRxFgg3v_j0V7ssxDV3j_SMLEBgAGg_u9St5wh4j4FlJ3UUJA5R5fi4pIegMFfwv1AgB-kHo96J3tXFB7EntZMhUu3pezvNHWRreHhVXMNK5QsK4HQOjVNmmq24zs0KxgXurU6T_cj96xOGtbj2YPawDK5lfywud-1nzWmBbNMFkpQ2bncjejFdMgMRcb7DsG1Z6KFsztyyAawX9vCtc14HA6-1u1gKpMvp8GaDq_ZWJsvTmYWF-qk8meQBFaRD3pugseFgCH62twOzcWJzCs2bHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSWm5G1rldtYgIN0AAV53AWSQvVcAbvWuh4YVodXAMqL1f_4EbB9Teb-BiVI5bK5TlBvpKM4FzsANJdPwp-2Hmq-1fwk5Lv8CiMCkX0JBE9yZ-0nn9MPriywcwPehicr6-rrK48u7mE0DCdrQM9lhYRIkxMwy3u05Ta8G9dLzc_ge7_w3lI2335f7swjdKGU29kCbQDY3GFXjH0rMTyHCPYdHf2YF8F65ngq5iuQmkHaenU5FsXj3OmQK4CQIsb7ER1FeK__bUcCRLluaEEyMuEq_ngyg0nGLrHd7L0Mz5rb6si-BXt9kKiDIRXL2HPrkO2uZT23xsuF7w729F1Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm4zpKgkkV2iNiQb3rqdFcFa9Jt947RsxiELdHWk92CfiJom-AsG2I2j9z33cLLoSaXmEC3u3nVLNOC4tPgOtHZIj53kXoPtw-49fm98dwolRnVIPTx93UAdbj6nvlwz4-bsx-Lrlljb8u_J09dDewMInzGmNHnmi79fFqTRbhkylfesBOEKcYG0h6zX1VUCqCNWCSrSWTLAe4eL50cTfERnHpdW_ajB2nB6-8MD7XTMkjNyeH3m2JV3Q_EnoD3KUc88EQMyXihJ7in8ZHt4nRruL81UKIn5ZARp0DupBY5Km_UMSZGoTuImc5MtfY-iAfBMrTO3djwUNjguoL-GwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2qVGZCKZJAXVPjChozdtFUkGHFWN5PI8rnHJHdBUOoCAFB5IvXOR2v4teiHQwjkiVjHDXSpR50FzeXH2xs8DAX9axtnig-c4IE8zEmzZh4u_XkhVedgIoeJbDB8MNqontgIzw3pG0t00bQ18xJPQGX_TEfZdE-auzevUcemdDXmJMWrN6vX9xFHwDnY5rAl7GbjfF4vt3hRB99EWRU1LEcXGRC_GbtUI8ndxSoW2I8Gk33n8B8zFXPEcS2GvVryfIRYdsxF9Gt_pTl7zBFOupCT-X0sYDaC9VMUTf5s5_aoD7S2uC1r6L9izLFPyZ3nznQ1E9zFnCoWsayzETZ36w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLYvQIoa6Xdi2Vy_hO_7u1KcZu2WSH-5REMmnagIi-cSoOtewSM0Qxc5ImQInruNVtFszp2-e5DoJfblErnttPXmh_dA6oEJiachb7VHDnsGF1k-3thhbZ_nL5NQTehNI536PINIL-3hY2r8bZciMrewgUigB6RxARmHR-lSdGmdYfX9FR4uffu_HkIKSlq6BtDcWVBIMKHNEGs7LKkjOeiMuExqTZ-4AP8QYbbjMW65uaoRFM6Pzt_1hYLwoM-sw19pCXaQcXjgu4hbMEukef_wIzH4GXd7rYWi5RjWWsVNWoDInpn49Z8XEtfWDnNhZfbt2NOQnhiXfm0HPQLGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOF8gSJ3alhvdyVsPR7eK6s2qfIB8bq9PlTM2S0A1dfrZBVy0-c3OW2BFeR3bi6Wzg__BxRDjKpzKwe0b6erkptEydZJqdMhojOLh3-uCV39P_QYYzRLHtVDX-THIuhsOmb_PFJGeoD8K8hD1Yrrv4ckPleR2O9RTEV7lW1PiF9PkbKmbgW1pVT2q-wk7leT7jEEKsH4K3l94AJ9ssR2RNoO59-x1eK2fnu-cwFVZ2X5TWZsX35cRuR-utMNyNpaKxoQrY-7y9Tf5FntDCQ-zfPOdVqM6dcC2s5reiR-RQzava0BpRSt9utyOvY9oK1rvVHxHRvI-S07aNU6tdj1jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S20U-B2nG6CqDPai8bQZL34wHrJ0tWHapHcv0XxadDtkMzFsVYyArsxY4-MVKCpDKiY98Xc957HrWteAZ82kOibu8-8FxHOyV1NSQgyR3Al5UjIL901BUIAHlGQ_cOq4uFEESHUJzEY8VDGYa-PIYKQpktJI3bQmwmST9lN8BLleDKvg7MmY6wftDpgiWUv9pqQCHHbQ6PbokRFRWDmabg2mWW66NKnkC2hENbyK2cOGzF1NjZ3JVtkAda1U04WxipxMqi7blnArTkfPKqnHVNPD3opCzweRsZdSohQSqERLVzM5ZoHNGccuQznaQ5UiIyxd0tV5wvnfqUzeO8-HDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBAmZdHypi7cEZz3PyBAJLrVhUeGVuGGb23pVXbySTu3QUwboyoKpyTPsBQDeSDRsVi2FiRmlvvMCv3aEFS-VSz12RXVfe1G1VP1oGJlSUb4u0Q2EoR_DnKFPM8DKiUFXMr9aBloN1Vcp2bFLLkw_QmKkK4yugOj3QXFQKSLd0xvnGRomCqogCOZ0ebq-45_xpFHz2px2D86cJbi66neZoHWHDaoWOHrHrdHEmTD4N_lSOq1YPBGwEdhKSUNLAns5QBA0I2-hXecT8NU0At8t_VzsEhq04A_UK6Mz8DDwNXIgfuNhHjHWSyDn5S4NFa2EQlsRfUDLEU3VuQ5iZiZAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 678 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 688 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ5rxcwGhkmFOrhWCrcxBR7o5HMU1JznUC373XEkQda-EVy4I-wc-gwtcKe7UlhpOw-ceAH0h401sWTeZe1b9hQkFOJ7smD7xiKnphpXIBBFzaQh6w6qGLGZiIDaU3K0TIu9wqAdvK88hkWMzRfBedJnmufiqVw0oPocgIq-7kHBA1w7FqCx9JFc_khIuvJfJuUiKmpTaRGTlsI33vH9JJpoag2sC7NhoIRv1gfyZDoPpWIRYon_jErWRBSbuinl4p7gyfKBscj8S0HxVziUIlRFDr16Bm3REVQZJYUOvgvJUoFawvZ1t9vHjj-WQXqmc5tvLPh9IMGNeP7F0GXqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZI5ITitHR2UAsCaNtx_6gqWOg4YcYubm6-rzYdhQtlIVIflACU3ICUnExNaLUkNVXKPqYpJuQtzMyRbJtznI7YikY1HdLEVjzOsdWLXNpNE4206NDJRmXJEU2EN4-WcNbPevLkz-VvRqfMgaKMzhtwUz8z9PlL-LKsnNyu-rq-MklWpLqnztExYWmGP9TvJB11hYY5cjhXFIQrolRf-M9Jb16EpD-xRrf8mv9opexvmKe1oIGX6I194FV617bt6kAv6t4HUIdIox4_9D6ByUukeJcnTvPIDMv50QzMuNWDH8bGvjOSVdepsC57YXWcgmaJsNRt3mp71w4bCbF46yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSUY_YCCo3dw6EE3XA-_CTQe9RWWIfx8SM5vHN0KHIcPtwDVgUpZlNZSh7Z_UPD0c7YA-CYe4ssVCbA1xt46ZGV7Lo_YIKKNAGHXbkoeRI5O_oIVjMswKOQcu0jv2eCxw4iwQwMv9TfpUr4j2Q5eqiT1hgfz3pcgw_-2zKRxqA12YYnB_zahAXq-UJqqRJGeOFYjQ8F-EW1myS0XEVzrxuHvlx3YccjU5QcFrRNS0M0aQaEOSVOZPNIe41Zf_5w3tDhu9PXGPUyI8tLmm1CSokZXObvRsG5rd90nU95CQridzRMWgCR-9VJz9rXLkBKg6ni7VmMVL6LkIhNHd9CSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3SXp8I9xU_3Li65YOVZq-5SBVRggWwGjTq5ec77Be6t6XbK20AxGXslYui3xxQlbd8iNffsdvIlJziJr-RVGFjGNyzD1qcvtHKTq7KLoKxkqok9D-EBSQXpWWfSRnTZbQ11j99DGyr04MwLSEy0_sA7VfU7aoyBf1qlhmkID65PoKfaOZVgd-vD5jFeFcrnwbq1jsyGUtmN-fMJx4WucjN8YzFPbbOhYza3AfatPH9LxE3NFlL5-2ejxI7MFtlUP3xYIuMVPnq7hxv-j2v4rMIo8pXotCMxlexJSXX4VSLdnMwuzgEBnDtq3JyHq9WIhCo6dmPS19U-mkkNEbR0LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz-vdmI_7wcXcrHqhUi2LLDaAiXX0ID7A0e0UZt0ijdq6Hx_bVvBLtdLN9SvXwp8EMiVbHmxFqrkNVhAxik-IoWRmM8MTM8_qao0KBHMOA0YVVaWJMzS0_C52btJn5s8sxEflKKTQT8oFYoBMLquYLfHDmyRKRgGVNO53NjkKCNPMEcI0ICsHHSB54OxGsgW2Ynu0Ru4NSfp8eiuJpyJGtRFKV66gP4-fQXLtkHYIAX73ncqz_O6xOV0ISpE2RoTttTarx0rWOEttw3jCQbbY8pQMqErwVUYysrSS6ICnf4aRnDsNjEZmKf79fmamZXpkt-s6w59rP7toiVwpjTEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3zq82Wdty7dqXf5EgIHfridk7SaRWYazOcCrIwv-sssOUdinUMw56N40snBY_SYNe-wk8MpO1f43XeDR7eYLg7Cq-tLuCt5cltudW2z97RpVD4HzVe9oP3RgvB19yXZqajy9aNRO_Mrtfse-K_gV1FTuU3UrFaytS2UQnBwR8T2W3vXz2tfRsApiATIPj3n0l6fXHfL83pVxizWN01kmzdHZoxqvbQ8lPDmW6qbtsHLjm0-lbvOFdwEaWC6BxjUt-5cme-8c_DDvBdDi-Vc5f7iEMvMU3e5OsgROAsPpHhYHF9NJ_sDeWTGYG_4O2E-Yp2FC-I8yHSUgjXnb1ji7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqEcR_hsW5dEuJlSIAj_4bKouxwCrf7_9fQLuaj9TbL4cv58W1BWsWahEEXKW0xpGUlPvLh6HCOZFJqb8XSW4uM5Jq6xi21qyPd7uxOyLJofuSbi5jBTej2gDblMnG9XYf0_4eDuK-Boud68evgkhps_aVhMRH30Ta1j_X-2WIWTWsaFlCXNarpE1OeFlG80iUy1KQ5MRmbGLrj0l5SKycKeCArj-35ePxaeQXXK8Bl2_o4JIP1Gb1-x07JnBD5e4PJys7Mg65ZorPNVGB7esSsvLAr00wkblSjAYxvwTZqbO3MGOUquVHH6nw7tubnTKCoJMXWz4Sdz4M9JyayCgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 900 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsFZQv_fzM5ce0Huv6_1-UispI0U8jARkw9lFvhNvonNWhSZKNzm8hXNH0mjROymFydSmqyNljcDQlaDGUvhZBruBfI6R01-17NOT9yj75OWCB6iRcdseuxitzBPDC__GfoUse2ZlJ475PvwEYnnWWABKUaFqd5XFSQwE_BN9KgfXmNb1O3owNvg2b5MY2L4p-yhbL4fmtH5KVV6juWF9mjqf7Sfc94S8ffOAgxPRDSh2UNK1kgGrbAR8cAOZNExCKU8eoiVH9sb-5gi0LeJb3k7U7IwjBRztT49Lm1eqZ783DYXM7tMr_sdfRKJXjYLqde81JvHXCpG64UWA_Bw4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC-vR53N5yCIEJaj_qV5KIRQ8wB5yhJYGbMNa9ZNpCzu09MhrF2sBsqt_ii1FuC6vwHuLsGfLq1J_Dmh9PU8w6ZNc-4I9yLhSsUKNucQu9HvxFbah3NTKp7GoY5xi9coVitrjbvovsKEx-kywMQ4GE004exBPZjjpT02HQRLaPBuiBL3N8-8cqFFjD86IIIJ3ybt9-s0Q75KhVDY0mN9LA20Rj3e0ONzaGj1CR9Vd4a5yZgM3vGy4sd4nrgsYchf1z-vdlzzjK7_zBZfXQbrCDl63mHync2uNKN7xE6Z7GHODPWfWB5LmZvw6HOhuvvQCxd2udtACg_RilIZYJ_5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OL1lq6yA1YM7gTVqK35v6_qt9nWDXuUWaa6_4j6WoySgc57bV5-JgmkH5jCR6sqUhIRENGJ0fzT2MzT1C854feQ76nnOJH7wZzfdqdGwOzHh_mAUsuWQeDIxdz77QlomZH2FVeUOvvd-IH2akieJ1t1NwrFO8vi4MPoAvz0jFjI83WgSMAaEyQhzXtr9UhfOTxetUugUlQ8UiNTHV6zazSRMAiM-MF6sLTrU0IQdHhBkAJ7aIgqysDcN_7HZt0w8HKcpw7LdE2ym9of96-CEUmrVgDvkfOwJGMx3LYGHyPDy8Rk9NS_EEyG0Gyhn8Xkv9v81BusOH8Pop2gmyeCdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaCOGaL9ZaYw7wT3s2g2i0ENY3wjYwRcl7xMYFZkSdi60pAg28DEfYZUCG6FI479lkqPbTBkbpvOfDg3aDIyEX8RQvOGJl7K66jHpXHrCjWCq2j4gZ0GX58iY1WhCf1lU5H3l8RHZ6e-ySKy0QHRn7kdneriCR6cVc9ghqPjNQfEpVXwMGfsoqsK6jg9Z7FO00LLSmCKMkvKSu17PamSMHJHi5P_j5Y8Ilfqr3D4wA5xV5lUWszb-TnadMD8qZvY7nSl_b-wizfFrcCvGqjpun4U2qp245tKOCyrU35ZSwnUq_2swqIGoriWmNl804ZpC6xmwl_Yd3Db_JxbWyfRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqA2U_GFZIpaSbnlbxtn8hJ67PypvlS3wMVvW6THbl8dQ-8DamgUl5QCQRmk56r2H1Cu92M-IOMpLTVIcPwc3fj8ouWktllWqhroK_rbj8GA9KzJt8Ub6B16bIT-Q8eE8rDJ8dE-5ifWkFnZybr1Cb5HEY93YVNb3J7htkAC6-mwwnayjRKrjXQDwta3ImJ9FyZ0XLalQjTOp1BAw5uIfblj7xnYaO6szvvGHrlA12ZuUIRbtQ1b9Yv1PlWuAQuegJEmU-bOqwnSfHZiNJOWsTmIM0GeS6zefsmdbSMACbmxJvLhjGtSi-DV9c5emG-lvjCCTXJMSHXs-r9qOfim7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYRQKkOizoXnns1bp_c_Ka_11_sVyMTl0OEvUqkv5AJuAhdYMQzzTkRmxRP8d4-JS6LEaCcToKWL5Sf40DxWZWvFRR0m3uNHUnqIVpiSUgaagywgZTztJI8MJQEx3VtcLu-X8pOpSh-1frqrZj4RmtunKR6YVolfUVVU-BMzMA9TQ0jdqcNuI7pZGuOSyZyLPqiCplTKPaGLrOrJqP-Fq2E1UHAkKa_WEL8kb1NIOTtCAO6FpnBN4W1Zq2ibaciuqYFIsbBqqAO5fFQqKxmDy3ZhWues6Ej7uYEuMUOOqFIxZnm_zLu8xdTObXkqztCG16JF_h4zhj7bMHzX-TmaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 620 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT6XGqYZm88lRudAzfGZWIMCKZUNuBbqzPop0U2LI5fuxmYiWmZ-FhdcHxTvRCeX3WK8_88IDZe5BUf8CCkximpibnZGWY9xTl5rvj9XoeKF2H6jgCcOT-XG8CeTEpm-QGDSHzQfyTekY3hPnzG9Y7i1YPTVqHhVdQSRFizqiOgdXw7NqCdIJlIGvTRpetxMjR2M5MBLFSscnPISp4P8xwR-H1Oh5qxuHsIuGVYZIHDfUsRcZW9EmW43jVeMBUXEXb9bQ9bDLhCloouErxd0rxXeqEHHxqlFkfdfzbSiUI7ztfdiBckZqrijJT3g-0ayZ2WCukGcoCelGIspMXOU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlXP0jGyHTtF3P3ImAfJzjEnsiqaFYVu0bc_2XJRXZRGDGIpH-AifajwSIKrN9Ky9YhEwyojHr4r2qhB83Lb1SQ7q-JPUUTcRtg5BcLMYw4GE2rN49UZ-1rFfBUU-zZ46xgN277datczAF4u_ixT_nni6pOU9MLr-59-f_ySrXUNSlqUaxoWd5_FXYEewqGCrvo1qP11iWAX7iWnqn0vpISlZ2dujCNtLB5AM4VfB1F0ag5nCHAUCNRTOPxJ7YtTMl-hUTImTz8XERJ6Q3mCrdYMgx42XQDYMuTWSYPZCJmfKlpWP8QVt-FNFRcQbHTt62dnSvkkaRkRlY4ZmgRi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqyamJEXg_XadjqbYO6aCM0VgoII88vc4Hu_h3Bkzy-qyB9wCfwX8-2G0_Hna-W-dzRg45M78kxP0o5o8un9g78rcJ36gS2oGlWVXYFB_apnRHuL84EbV5XAbcEAxEJoYq3vZ29pdxsM0R1teSTLkBs8H8_FwlL7xMbMelPqYUpLvVVERNISVv-6eVKkIgL3c3vsaNAEmIYWFK5A_yIWimkMnk5qDeFTdwW-Yxk-rBwXib72j5RXGRTV4l7kuNxiC5LZhqe51nuxXhHKenhwOH5Y1AYNTFTUaC77Pxa1ON3Rj4o8X-KJ4c0EHuzg9IjI4y28m142swWwS4r_jOzJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Inh28nDVK0YGShLwrbOvkSTkCufvAQBQ0FiN5J--YyWuRv-Jh6LRaK7hcrzbl0dU84RavR_tfRPtx3Wg9F7dxFQ5Fi9SOb9ZfHWFIYEME-S12D6xW1BVtA2tc-DmBHilYPpyNeUtcD198R3LAa7DD55_80NBufoUh_XohB4evtEaRtxxoDkefxy-GcDoRIf9SNsLI7aOrXvnCSUmbk1RhVtNOJCpDDv1RETUBl_oAKLj_NEN-ssm9h9oQrFhHd_7Db4fm3Nknzjob1tJ7ppfAvx9HXoFbjUyC8egBaUn31AwW7Qzt9vegPfUd81lCya8LgUDi7x9MRu-eg1LLwW7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Inh28nDVK0YGShLwrbOvkSTkCufvAQBQ0FiN5J--YyWuRv-Jh6LRaK7hcrzbl0dU84RavR_tfRPtx3Wg9F7dxFQ5Fi9SOb9ZfHWFIYEME-S12D6xW1BVtA2tc-DmBHilYPpyNeUtcD198R3LAa7DD55_80NBufoUh_XohB4evtEaRtxxoDkefxy-GcDoRIf9SNsLI7aOrXvnCSUmbk1RhVtNOJCpDDv1RETUBl_oAKLj_NEN-ssm9h9oQrFhHd_7Db4fm3Nknzjob1tJ7ppfAvx9HXoFbjUyC8egBaUn31AwW7Qzt9vegPfUd81lCya8LgUDi7x9MRu-eg1LLwW7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axP0Gj8aR0AcDZc0gNNF11jmpT9-ce_dMpsrV6PGxEbCBzexBkS_BmNwpvkUjiKpnJ-SPsLsicRC7M7yfroVCvMv0FcEHZTCitRZMzpcl3YIrDNYYEn0nYSWfKIffjCh_9j1GwNSlzdjUricebWEJm2nCPIDy2eTH2S8xfDcpkZUsV_B6Qiqeqrx7oBFAEsh1IZdjFrIhGDAHgrcomW9KZZPYWmA1zbPwfSayOXBtd-k-TLdt51GyKwFqew4YvIGP2RPRTbTW5vcRBntzt4LiL4nAhS9bUfv3HzUBs6--Oj6qTe3a3DQNUhcu0UlnimMCfL0FyGTIdLb-2SnZyDpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi1HhCRdFm8sIexCYoTN62cp1atornqb9nKC5aUSr8ollfLVYml50mHoLlR4JMTuqJBoahcUR_vqJg3UqmUV1IVNIv4Yypqd1SWMVhnIQ0Gjr6uDx7qLXtU19tzlnc3n6UY0co4XM2wNjPSlAPjUJzeifzHjFI-fwAW7MRgvC8fgm9iny5e6o-5dr7e-mHjPJ1qRridY_wkjG0L3MPb9p-Vtvq8MqZD61S8GOgqmxYef9O2ogfGv-GcQTSm3832sgn3nE62ObQ80yB7PfI3Uf01H_vZWPOQpkCAsDFlVIDtF6mACO4imOPf5zi-lNmalZAj8nJQh5l5yxWyNmUqABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNQYDQG1ZJ3euOAZsDqSphDZXszKea-M8Nc8Sj7tb7rhrWuY8oUr-ak_SOVPjFTtTO7TtJqrFIIYEtCJJ2q4UO-KxQKQk-6J5HeJpYuy0ipQZ1UJkoUMp1X0oL51vYiiCdmHyfvJiav8EtZiO1xXNjyNNrokQ5xDcsLkcKVhiadt4zzZRSiwILcbg2h3mTUqdVFccyiE8knX9Cjhaccg1zEl8NFc6Dj-G5hEkBtzP160F0gOGgXdNB-aQ9dPIGHyxXrfBvtkGz0xNAgA9elW9tMRqw1W8RjWWoQ7qKoaIM0LPrOjAeGHmn1-IVGR3Eeo4YnmdccLA9P2yPF5yOTyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8OYqwox2_2oWTFLw2T_LTLxcTZPta2biEMP-AZjG9flokjxooFqbzrk6VNsyoCske88Hxl3d3iJ68t5Nz9oXPGo4pvzhDXu4Qf9gyN2n5D2UwQQBUDmbUWOPytk3Hw_IQjcFccLm8ID_-mGYTA3b6qdKic3WGrJkyfn7s4l67zCrgHjm2SB-lo7FrtOWPfwtZMAv2xZia2G1AtrDcbki3UrBHU4EUUFu9kRygUYZPNJhWAkc7M_bfdPSNeCKJWf8smlhKCKunJH93-h1cpkZkv_tvo4sj_GKEqh47L05dmeR6j1xunHtxc_X0FqAOVyArvr1DNBRg5Fxl6KkW3Dpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RY2khG2ATombnTyYIsPFh_HRCa8zW4gNnAtD6lLdPyN_Fkt47yE__fqJwKXmkY53S-EpW8NA4y7jm0l1-K8VzVwiXg5orq32dun8C0Xs_88fBHnIFrKn7x6UWFUEi6d8PupMGFUv_6EGb7gYOTgDzLVsLCyeReIAjHpLrcxUXlNymWorDi43yddPg3vcRr-7sXktUqHKRz8h6OUkbmVJiw5ImbH46Bsa8A32w9-Dnki-zi-YEFs059WY1FGaK-3tZSzfEKCxR2Uw82HRLYC7Y4NWxRPPWnjkBCRnxClhxTSzwjgvX2tlKsja6YtFeb7Jb06tfuZUrAN86FkatGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWag4RDIXYhT4WI64GP2ToNwivWnrHlPETFf1m1awWY--7HeLOgC7pNof94ZRf_fhG564fZH09mzpcGqeGjKg-488oQ4Jyjerpedt_yU6DfK_IdVQIwU9dfQ8mvz7_VPYshi5gLw5wY9gLsaIESylH8fh-34w3y7TTqmLOb65Ei079qTUJ2yCXZy67Nz1oN6ym0oode95Uusl3A_FokI0BPLbz23nXKmtjJroKTUc15txZeBxu9IezGxwDNXxfapDpBzSDY9yl2lMBEUmU1lNMHapK0DnQXO7NlvOUKMcUDnlWc86r4V6qudZV6tdoGZAYWJnszomkfH5g9YRuSTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOHyYD0aebIBGjZnBbxcOWwZ-wnT0F6DOhTzak3dDkhWWYWM9ZcJekS5q-TARdrn-nnABxuSklSbNtowNGmHe_K3a3bw0LHB9BvBNT8M-oaXmzN27MDWdJcfj-0_wVBwcliIoHvEzq7XgPu7nMI11lM1SUOM7dNHRjadiFLX6CoErT0g_C8ANlsZV42rwEGGE25JmBWvmWkfbL6TqNm1ugkPS9RpCFbibrFxCFGhcs3r4eyU_THXJNMkhXHLo2xD241gCYSEiJAnbbt2sZUxBR__yj7ol1nCPxGwBQeXdNT8_hA0tRTVIevkUGVryP-DCOZfhCz0Eio-oyhqGkp5PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=VlMzV3aWX1uTsSqDyLc89SQukR2rGyAE7ZennbOrtNzm5_tUwCuTL9mxgyY-EsVVuh5hl-FYSTJiKpUY0YvwMuVPxuOrtZwcBW-udLaQoO01C3BzneC1WzAWNG4rXERvxKw1cKL-5FPhyPYHowDXrYnk2dHUzGF7pZ1H4CRXb1Hj9dm8Z4iYxc8P_PoBDRobXEEnXgfOat-dWaarlvoO9fMIjtu2vW0HJGrqFMl-m1ehbVfLMxh24qwA5gQX28v71z7l1pAKrk_EF4WnlKTOrKQFpm8pR9IO-zIC3iJ5dXeNNnckzQ4xpQQWe70Ru3wW-rmZHD8fyTP4kmG2zvzpuzmvqjsXfZhJhZdcJOKmXdPi3eoBmL4kexLkEgQq-2MYF6veSozcA-1sTnb1dX2BNo3L-HwVSqY-CyNZeNA0T8DVrohYA_X30ZY9HoiQVl9lV1Xg8tOh8-V_iAJ-A5Ipg8xXktiquFbjuAIMLTBHGMdByHKCOHKsvdke-AD8tYHH6zDK-IXx4PsOE_dPG-yTLIuaadp1xtSpjD6U8N1qcefoRQ-HOeACNwIBLVP-SOe51NaLVTkO5JNed11zm5Nu342d9cEqB2_95MY-Rf7HzYQPeRh7DHNa4cfdEmhfB4pq-riRoHZTS2L_DndrgCEUwtY1PRqG522J3g-cV4gQA_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=VlMzV3aWX1uTsSqDyLc89SQukR2rGyAE7ZennbOrtNzm5_tUwCuTL9mxgyY-EsVVuh5hl-FYSTJiKpUY0YvwMuVPxuOrtZwcBW-udLaQoO01C3BzneC1WzAWNG4rXERvxKw1cKL-5FPhyPYHowDXrYnk2dHUzGF7pZ1H4CRXb1Hj9dm8Z4iYxc8P_PoBDRobXEEnXgfOat-dWaarlvoO9fMIjtu2vW0HJGrqFMl-m1ehbVfLMxh24qwA5gQX28v71z7l1pAKrk_EF4WnlKTOrKQFpm8pR9IO-zIC3iJ5dXeNNnckzQ4xpQQWe70Ru3wW-rmZHD8fyTP4kmG2zvzpuzmvqjsXfZhJhZdcJOKmXdPi3eoBmL4kexLkEgQq-2MYF6veSozcA-1sTnb1dX2BNo3L-HwVSqY-CyNZeNA0T8DVrohYA_X30ZY9HoiQVl9lV1Xg8tOh8-V_iAJ-A5Ipg8xXktiquFbjuAIMLTBHGMdByHKCOHKsvdke-AD8tYHH6zDK-IXx4PsOE_dPG-yTLIuaadp1xtSpjD6U8N1qcefoRQ-HOeACNwIBLVP-SOe51NaLVTkO5JNed11zm5Nu342d9cEqB2_95MY-Rf7HzYQPeRh7DHNa4cfdEmhfB4pq-riRoHZTS2L_DndrgCEUwtY1PRqG522J3g-cV4gQA_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuCUnBQrkwZl6t2clnx7Rcu4eBpmECb41LU9ZVG61S4M7O3aUGeWz___7HhYsu5ZxfTy6hKakZU_kbPDrHjVvnbhdtiuRJML5l5yR3cJLegN5lcoe3Yjuij0UN7ddoSPRTzOVAcf6Ik9qWBNzqzFNEz3yYbiwvsYFQN_pgENsYNzMrRXMav84jNONbxoSHEyX5AML9hyHS-bKilxK06_Xh6VfLeHAYGvh4KcjrMqAlYhv5f1ZalIQp98xEqF1f2Jurspuao56eNbGtOCLnlYRg4ee_q_88uHE73VCRYiJWv-SJxppzmv3epECcSL4JlP6lqbqHQjkRXBDMPWizjpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBKndJHV5xVDZ1Rb12BqUl0vbdA23NnGNRY95I3Wa9_qSGASYyc0CCxoMTunrLqSFV3Rin3QNZXEKu4NrH7Xd2H3rxYFZ7Wun1GJ8TK9i_7llWY40sA4-umAJ5O1LBuJphvNZd1-Xmyi9qHZIJKKPQVgBc5c8P7J3Q-9CBgT6iJAd0h1vr3vBOoMapf7B18w3VhIGkbZewxuqFHLF79mPMvIMWXhZs4kLUV-C1vIp0N_YK3vh7xPG9wz8aN32RMMVyrxFPagFfZMn2sLvALKCk_rBdYXF4Z_MOuTKsyN8qSucDfLFZv9q6ds02NGe9vwT-p09hACEuHLN5VkIt1kRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8zf2RKudoPGi1VNtN8A4kKu9V4_LtOd04ySwDnQ_w2tFRD-Y1Q5wAahKMH6osfvWWSX8bq3IgMIC5mgWZw0Q80U8DcX1Xg8E4EjBd5AFe4VLrzEQUCuZYOBqHdrn61hdRO6ookrQZM4_IW7mPEfo_z5m6DNEdiZvc-b7Qzl97w0ADPGq0Bt_duwPPK_FNcvuQpUETp_mPpNhLfm1zybXAf1oPLn-8-BLVXAxnbSf1HJE11J2d3jMT2G6Wg7DF91P2p6QzHIAJ6PHNuf2pgqoZBoyfRVMgpx5GuZAb0Z-pZyxZqFXX-3FsQIKhSmeoBMI6HlTufBZv3iX3V6kx-3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9JpeFdaVClApdbVNtoUn4ijIeVc8XG2Mu6Ops2Ex28zwajZKb6BdRBaBGP41OVNvAmft23mfX0E2op1TNKIQT2Oj4-Zw4OGHzXhslrMKiInJM1beOQYaWZmkHFGXdFNYqOrJq1ur4OJmK_-hRi81MX30x98-vIY6aqivd8hRgf7gXcD9cdKkCfg9oHhHegK6_UD-8VWI95zK9WjvKpJBfrCK2QDkAzSSz-UOp3_opxWVtrEypCSdcCPhgX0wEH6pGBzsRRHbCqjBdqtf3vDZ1HtwcR-jmu22-PTcpvHccymqjsF7zIT-dIkgLCBxE-WEULEtpz6-13kQJnie63vZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL_foS86nnNok4X0cnqS4rG7tovMk15Bdqk8ss3XNrndIRLa-wLfN1VlWomEWOHr0g5dfoA8ezzA8P5m2B3EIOHRIFbpUNBxXZj16Qqdvw71ES51YYKJy__bDhfej2tOFREXExzS-_ojxHeUiR1ofeIKQNA1aOqwvJXE4czCrMDMynaRQPGCf_mMRt9UO1hq-cXJ5yWa35lAGQ2Lct8vxamaOMnA7-18bF9FIQTs6Fa1kxyY2MjVRTxpgZFoJ8LEfqQ9JMWDt51uDk80lLqAXb99PMXMumTTdACanpOLDbegQUydlQGrw7NojIYCTwXoroipXTkAmqEDRPieGqWxxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZmF9vUz6Beg0kuSbkI3fwuXFblxH4DRwIJ4yBkBWO0NhGGf3AE8CVWh8Sy0oLXEV59cn30i2p2zebkmV8T_YgqMqqfYuRu9RwK9ThDhe5i-1_2kZ6UmKLXiRKGJZKBi8xpB_dmaNI5M2ry36QQR24eK3l7JQzoW_nEbOhfmXZp13-xAtRTuyJuyMjCHKAv34npUUe_6-EWyR5OfOS-XZ1INjDi53kHVMK45qLCOVQHh0QCuq9y48esTltlHZ7DKEUYNcxz6rn0i43b2E5PADf4tzshec6gcHxINOaQkcy6tlgAOfsNG701c5QjdZywOi2ffhll6Mtb9lwyrSM2bMv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZmF9vUz6Beg0kuSbkI3fwuXFblxH4DRwIJ4yBkBWO0NhGGf3AE8CVWh8Sy0oLXEV59cn30i2p2zebkmV8T_YgqMqqfYuRu9RwK9ThDhe5i-1_2kZ6UmKLXiRKGJZKBi8xpB_dmaNI5M2ry36QQR24eK3l7JQzoW_nEbOhfmXZp13-xAtRTuyJuyMjCHKAv34npUUe_6-EWyR5OfOS-XZ1INjDi53kHVMK45qLCOVQHh0QCuq9y48esTltlHZ7DKEUYNcxz6rn0i43b2E5PADf4tzshec6gcHxINOaQkcy6tlgAOfsNG701c5QjdZywOi2ffhll6Mtb9lwyrSM2bMv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe8SzJOdbKjG28pZeBv1wKOFtudPJB5UivpT9AuT4PhmyQA1CxQHKQOIRNk8v-Whr_AiKTSPg0q_a7I0u81OvII96WETBcNyewWK19-0FMiQUon4cNOx7zWQExgdLIwINM5wEYnZguSpgy06zpk737hX18vWQM7Hq9wldU_WH476hOgoqeQAJGRPW5xyfm5gFFlce5FSO_foVR2D0U_r4wOAv9GE_cFP_v4sDfi33PLuORokgcweK41osWZg7iGiYV3rv_cCLbOFTC0N7eY2bxRTuUBD6HBmWROpEd0hMBKdyDTFUVMkIcPBtVQIjaTceyfJjjLPFKlILofX-g9CEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVGOE6Yb3BDl5S4fZMaaJodRBLmUML_xGAlLL35XxyVW3ilXf-BTWLqYqEC4D40-xVWaV94WHw4iouAcwsEN0BR7lzF1sD_OLaOlZEx2-OMLXZLtvJYUg3GGsGz6Yc25YSbqyKYI2_tQXZNL4UVUmzbreW1YTy5ZubVLL_voiPkCN3J_pXNpEe3nSfKLYrLFyOKA9otVyH9NmId539yd0vBDt8un0cxDWzW-FgPGtwN_ZYYd6l6kfCwiJosEwgMKWN0krt1_SUL_u2lqsKuJ7g-wSdCDQqgY-hUNagNxhaG5ZnaVNLbVsmFmHzDJ4kkmxkO1o3YrXxog9kDkqrO6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsUyGsPHRV6rkOC5-nXbm49MVTihEcOSXixK9SjkgAQtT19ee0qNlHFnq5drmU2KOQ0Z5jrWFdAHKIoVfAR3bJpxfoL8CpeaHcQKC3ra5nc8ydbRH-77xpDlD_LnKItFiOm55NV_zmUKpML9S4fOUtA2Miqj3zs6uKnLckR_BHdZteWJ_n1pRZSHQc2aqcjz7Cd4Y5Cw3UfWhrapbsEqKZXcfYVXkusvP40TlpulbhL61jHZhwHdToiYf0IDf2ygKUrOBzz6zXGl1vfD7euQeulybWT21jMwhqLDLxFPaiLUoCOfHuyKdHlW643E4gR7ZcDjoAeIH-RFZ1QIv63NvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUg88uzVi3ywIa5Sa-wb4GQ5zMpYUwZ9HBoe4oqgdAyr2itajyg2TMip1FXiUvz71KzWE3S0nN_Xqt0uAMRNLbYytloAZtuuFBbxSNJolnOTPyFcpNVXqg4ClVncAzD5pwzX5u3LQsJOK5cIGRzfaQW11FhbkmHF2Ci38tqOZ8ZjxjqgNdwCsSYDd_ObZ775bq3ALUeOV_PN4vXAifm_QrX4A4d_WPpkAbb_4jXdXr-mDU5PJ-0b58LGEj-0wiUUg0PmnP7GdcXcuwnaVMG5UyXKQSXAG3p65xpTPio3h4gWsrxonv0uZDxvU0DXqaH27f4w8Uo6fLgXB7z4Ai9_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6gIP_ikJe9NNb8TvNYabn0VLC2SbH8Lztl8sgnsz0XQf7VFJPD8vZEGUouZS6dlif9Uv31W9Vyju2ARo60N4rEB4JL6dBNZHeP04EtRTUU15jC3lN2NbkCR7gUL2AVSSf6ctfphf6jTSC7gPLoOvtVRF0EBeDO7rJJ5O77LjaC14Ho-dwRjRWwgOIXOKjwa32PdzVpZlQup4nNC6uZm2PkE3NrL1y9qfhSFAhsDOmTFX-AFaeBlI4upNAMYs9LH0i64Nxy1mt7Q0MOFoCszoC8pn_GLoDg2jLDzcJa6qx41Tw4x1TUXHVbW_3Gsh5B2qaIyfabCA7nOkM5OMw6vdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN6ggYUE-UlB5a7x1FXYOVFDZGf5JmuP28b5Jt42Ov2bP1fwe9RyfvsPBIVyB5Zu08_3pknD5Dsg4u2h9TARAHqjaTjWoGMjs9IhbsPDNA6KNZ5qQa9aJJtQKpfHU4b_ca6z8RLPpLgfr9s_k-X0AinlIT15RuapQiyqWLZ_Ac1PANrRMkTUZuS87NrIY8CHv2smnG77km3fUVMx2-JCX80nW7UhvasTgkSyVbbruB8Pv-pnw8Ph6ssDIWEUaW20YRmkOeRYmUXHqP_Lppbnz0__QZ2Ku7FDuy6jrKsnn__BLGLTVLIzTbFbd8rEh-0DZGGEI4cAZCZiBNcEgewEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آزمایش گوگل دیسکاور در نسخه دسکتاپ
💢
بعد از مدت ها انتظار گوگل به صورت رسمی فید دیسکاور رو در کشور هند به طور آزمایشی فعال کرده و محتوای توصیه‌ شده مانند اخبار، آب‌ و هوا، امتیازات ورزشی و قیمت سهام را به کاربران نمایش میده.
♻️
فید دیسکاور روی دسکتاپ شبیه نسخه موبایل است و به‌ صورت الگوریتمی درباره تاپیک های خبری، سرگرمی‌، ورزش، امور مالی و سایر محتواها قرار گرفته است. اضافه شدن دیسکاور در نسخه دسکتاپ یکی از تغییرات بزرگ گوگل خواهد بود چرا که بیش از 20 سال است که صفحه اصلی گوگل بدون تغییر مانده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/danialtaherifar/807" target="_blank">📅 22:07 · 22 Mehr 1402</a></div>
</div>

<div class="tg-post" id="msg-803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Yoast 20.4 Package_2.zip</div>
  <div class="tg-doc-extra">8.4 MB</div>
</div>
<a href="https://t.me/danialtaherifar/803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود رایگان افزونه ی 20.4 Yoast Seo Premium
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/danialtaherifar/803" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">elementor-pro-3.12.2.zip</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/danialtaherifar/802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه صفحه ساز المنتور پرو
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/danialtaherifar/802" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Rank Math v3.0.33pn&1.0.111fn.zip</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/danialtaherifar/801" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
افزونه سئو رنک مث (Rank Math) نسخه 3.0.33
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/danialtaherifar/801" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">jannah-theme-6.2.0_NULLED.zip</div>
  <div class="tg-doc-extra">10.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/800" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
قالب جنه نسخه 6.2.0
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/800" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-rocket_3.13.0.1.zip</div>
  <div class="tg-doc-extra">3.6 MB</div>
</div>
<a href="https://t.me/danialtaherifar/799" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه راکت wp rocket- نسخه 3.13.0.1
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/danialtaherifar/799" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
