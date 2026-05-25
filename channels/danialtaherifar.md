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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 220 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQhRo1FjIMTH3AQoMnVbL5a9_N5EGLJg4hfYqL9WuJAFmWClMJjiPW2hivvtCntRaZTGii_LzChXjK3A4Nlh9SGAPg33CMoAv14OnVYFI3GlTH0q__SXvlIeYY55wxzCvHBtrg9YX0zBrNsT8SDIT8qOfc908cLRjgZ_ZYglSuWrIp4OLI0qeHTl6eHLvd2K9rd8bhXDFJjy4AESNCrU_MtXssjak4hOlyk3NquoJgjaLLN48exI2YyLsc8W4euo5ty-WzSP_fj7sgkszXgGVY36xHaGquighwR7bfMZ0srbtJvxVYbRQaOxHN_3Z53YFjXT1RjLDrsFVWj6EBM8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 288 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlVZolV67YQ-ifkeAuW71soksEXpSEMaSIUpmcmXrCsNDvCrct0H9nS8hxhrtO4OtCmGSG7LtdQUtcKNVBN8JEBZolCB8Bo5MXzDm73WX-Xk4ksRvqte5edppYhMMEcChiCOI4Ollds_xjXgT4fQxxA6YodbQTBMCPwPmRSAffOixYbpyyCCQ58tqRhksiGHqL09FHy_0LijLozdtZJO-ipdx-jo-kR3KxLzWSFA8LA3wFJZyQYUcXdy0R8y0HRVgAX483yt1QF_NAG_vTDmoI5NjKMfRscNvp8rtwNQh_mskuuwoXumYeLxPM6SR8gUdpsgMfAzczlLnzjw1WFXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 633 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 752 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgfMJSRL9GTF2L4YCNeMnjfV71cX61G37tHAb3iaZIdyLnnGBmWpERJ65E-eaw07Xw4dYePxOvtdw45lfi0E3nuEFETqWkQvVXugcvUB2Kq9v-hmxGPzvjiGIeNXKNPil1yd_fxgXKXB1caZdamXjR5zFb3Y9i211s3cLVrl-DkYC6n9tTm9-EYHHo9KTbbGuXuGCkaXpAcf7_9De4z0Ld0sq2_Ok_67czl3cEkqbBZaoeaCR6cjJ3NQ4c5HyYaZGJ4vuHrHxN7T1A-9HwQjYvTZ8qGRcEsxE-kdD0yzDQ-Id8uXdEsfeD4s_AY3lFRUqNJskfgVoce26rtFavQWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Rf28e5Ku3C9CZvln7f-fWS-kc4VZ5GU-HF1lSr_yJU63cTgKqDwI_TKcfh8x9Wg89JQL1DIoP9lztkbTE5jMPgXsSVDIWnp2lvCWmMLL0OMU0LF3dDfPSy1yRAT8Rwwk8YKP6pdXCMkfj_F-xtRil6NzYZN8oZHXpQUDN7YRMJJ5-v1QEFbQ8pWCeeHH2v4ydtbK2ohmZPUcu3adSck72wGYNNJukQx4l7Kor8-4PxGNqFyo1pSKkk24k-9dkJBiLD4pyYqJcDQSIySEZy9Q4wMoCcn4G57fBa-zj_I6kRVlWxh2Vz2Hrubzld_tngrNiPEOoNOzxljEgqmoXYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 958 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odonTaxKpo1jSmgFIg0oZbk5K7zUWIqRXVWG7zGqKRBuIi4tLd94ni6RxjhMavmkY5QODvXA4jqW-0wcMZi_8eJWElTP7UVjL0RCQ98CMxgIXWNC8qOl21cvIumdLoAVBytggsue9jn3B6VAHlWt0pENwuQc71gO_FTvswLmLJrAFUbJsKiUvjJAMvmJKaG5Pi-jFepkVS-qfd-bZpC9-AB7-tpAbbT1uzrGdEPbWWeOVZ6XNo7whbfJUSbBUjkQnmei1y6sAR0kGWqzAgzfyX4NZnGN8RpxGdjg55JW8jRKNAJfuf-Y4qhgGDcSO-KzBd3TUPoAVAg-C14T2gXoSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfF_43tBMQalXCJdEi87HVaxFLBcIMA7x9bNdFhZUwPiY9tIVzzuChl5Wwy2tNv5NbYg0bTpGcw7DKlov_xFg-iNUyEE-ghIc5IcbYfP1lqsGXcpiVGg8AOgxdttDh9sbInPeETkEK4rn_ZNcGwSUrZ5RL4oZbiIom3sx9f_7SNsq2qQEmG9qOZaPGkFXLMIo6ZCEUsbQs4qyC2o1oIl31GQKMXyV7lJUoOXhYlHtU_Q1Ga4w8crhHrZBPNmftfm9WidoPf7CdfmPBovyUGpR6NGebg-fSI1x7bo05gUYs5hHES52BtuC90jt9VBEsDKD_Lr-TDXe9NGJuUVtdbBRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngjstOpj9mgEfSlPnDfadnZ5Ujo2gsR5QFX1KpBBA5JjCyJd_IXD3pqf8xmX6nN7ZQEpmDDPq2mRGurjmHxjMjIyejRnKDDdEKGKBRp-6XUb5FExaBSVDhoYAmm12jbiuU7Kpu4yYlPtXVw1yZJjKYjF8hRDnY3oFwK9jEuJ-5Qz-eOe8Eu0mvxuXvO0UIuFIIrCrM4Z_pJnUHo8rRzQUgho0EiR4TXTTOCFkIz0cbNIxwW05Jj1Pw7A1oFGBgF6Mu2kq9hYlIsCQ_ypiYdTGox1XpVoVKAu1Ae2szfP5ULvT0w0L1xDxtcRkZdsqwW94mMR00REILuULz-WZWmxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4jsCmyR464LGQ2g43CRvAKt5SlBvuEZSEXZ61vInyt9hp8LusP-BLFcStODuQtF34eH-wTTyi6_YY3dBDB1H4NLQQsZZmGNI0xqSqo9w_WikVlSrk4YwpRSjXwELTTuvkTotiqQJxuFHdfpr04c3CUlhrXPQgS-gABGulAuvYd5e2DZ5PJb0gLW1No6mp5otC4hKXIM47b6cJqJsv3RO0TVSJygkAumMmc9vQuurSOmhZnrfLEQWFkYG8X0dGHyTr5EvQnUdLwOyqnMOo0ysRfTn41TaoqShgNmFUD-9IRnAK6EE4Su5VQUr8Xt2MMorhblWfaBjiezrF96qMqoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PC1U8fiFUvr87W5VnxffiVBT2kXrccw-jG07aNFerMfCs50Y-2fz5_SMoP8PMvTayQso6qS6hxTyTy7IEb8PkK-cEiDESKQH4mcAxONoq1YgGU1qjKwpKJbZyJCIEI3rMnX09hs20j3BfJE9vUGR4CbLov8cfoj-5dxBV5HQJrUqUQ7dqvWWm_ZT47aG7uKHZJNF_5fEQDSZ1iYedJk6SPwS9nmR_U9EC_uShvZqK6Sxq4i3jlB35DLhXFPcFilodjBIZDLsTqYE96WKza4bcadBDP2i3wcjpIfiQa350Qh2l2_dD2NPX9az07-Q3Cfw7hUNUS-nQVWCj4lJdMCJaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnoePh3artnZejxqqzQnLjHaU6js4IwCAwGCGTPd4eiXna5-juFmXb3VQIryUSzpA6WgPd58-WIuH2vXrr_znTU-hpWtFNxBdgR4OHjbFZvJBkOztAK_GCt33JnVwFFL2edU7E-UVRugkqjFr87Wii7DmXqO3qxS58N0Db3PwvwyxSFaxn4nhphVl48L7L0sT7eIzOZBOWUkcDdq6FLKAs9gCB9aLIN6Faff6377hpl4Fv0V4zVkz2nLnzBIEGcr4Z263C6dy4YnQctpku7UV8XSCjHXjBRby7FTpDprcI26siQE5Iz-sS4kPbe02w5OBdPotqq-OBGk0s11va173w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=o5tuPKINUWnQDDn5NuoWPaQ1RfOO1rFaSVEchi602WZxyWjnW8w7weKaCvXfEle0JFayhZPzFrcztzncKiooCH7-8kCyEI8b18LUI1tLLfBrmWMdOnv6p4JF7tTcncm6vlBiDfQfAXQQvWmde9iAKeU61XWVSyyCl-AnxT0Oi_G-TWl9iB6T5tb_D-26KTV_G6rUzwzAUh8R5CETb_vbvsxh6bsjcVFG3fWonSI-Z7d-hgzHMOZBXjdSovBwg4MwKftPqU8NWrm515p0ZCy-2ykt8U9udNIwLjFIMlddfizgUR56utxXyMCwo7WxTtV8Y9AZPoOEgIvNQpSi4h1N0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=o5tuPKINUWnQDDn5NuoWPaQ1RfOO1rFaSVEchi602WZxyWjnW8w7weKaCvXfEle0JFayhZPzFrcztzncKiooCH7-8kCyEI8b18LUI1tLLfBrmWMdOnv6p4JF7tTcncm6vlBiDfQfAXQQvWmde9iAKeU61XWVSyyCl-AnxT0Oi_G-TWl9iB6T5tb_D-26KTV_G6rUzwzAUh8R5CETb_vbvsxh6bsjcVFG3fWonSI-Z7d-hgzHMOZBXjdSovBwg4MwKftPqU8NWrm515p0ZCy-2ykt8U9udNIwLjFIMlddfizgUR56utxXyMCwo7WxTtV8Y9AZPoOEgIvNQpSi4h1N0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owCdy1gzP1Xn6D-2NCtEqKg1_HsxSj9NWcvMXc4OZF3E-8zaHfqFPm6smMbS-Fk5G_Lz6bMVInhFs0FRMOJgRfKIOkuypm23q8Msl5a1d1HZCifpZSpu9fXxItvWOmm3X0E7gFtlLxN7wml9iTojKsstdmMTlAkI7IEOuvpuw8x20ScxRwnugeXHlMTyBfPB1NQKrgDOA7D5g0IP-PfNd63MDQUu9DujEBOMCaSpMBmaKaDWOPtMMMdoY-GGH8EuL6gpuOnIirCCfXP3n3P6gfzsGuwPUnEettVnBpN9-hKdhbcr1EN08tINiJ5S82CkgayiwjnF2Lgd8n2sp7YqJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC09mv4E6nkPtP_iio1H8XhgTfSohlohcsl8U58GlkItudVs-J2lF2OQxR4c-oilNYoIGv0Xd5aOfzDTK7wYbAvItTyLkZQNg8BqXw1GwNCkphSh3f_oRXFm49JNwkJxHSqXS7HfoRgr1LyeLVTxWGsDvh88lQkdOdvSzOFFpCbm3i4f9ym4PvWuRaSFgyae0sFkwMK7r3-MfrcV6efXhuGohg8nPLiT5mNvZUetoZgykKwj0HBv353yqfYG-RV2HNvvypm2RlAvI6JU0pSVcJ8Q-ng2XazzselIP-5fIIwUJerWhv9dFVUr3ZmHZgilqb63yqEmSFTVMoRU8idLRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLOYDsqs-zV5zXzdUUbS0ViO0-3Bc_3iO3s9S673aYfvxzkCctUaL0qrrcyuFv4khReTuKOgoD2IrsZzUJAHEwj_SJ-ObLOURfrpV0r_PYJUDMnaSyCd9NlmbcUoylluMMLl-eYDostlAnI8qR8wutdFw9yt0tTMQ6DAzIgRPqaWkHARxvTeAt2z84RvHtZkJXQnkio2BSc_HETKGymIwJ97AlGa2fN4y1gKG_HtyVotZhm_Q8tFfL5e5EEBzghADUa-x5Bq82SDry8tT49SloHHglmMazKBegvVYxM736ayY66GSrfxaZt3XIfn3szJZCE0Utkdd6JZ5OMXq4cZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXsd3oBy-G4ZysG20VsEcYgR2sDXMWwurR1PCfh5RgOXsypQ3T1ze32zXhqtUAMvA4b7MxLQq347RO0wnJQ9IoQmdEAK9AnvTqntZ5e0rIcYJx782kPg2UfAc0G3nhShyFNmK0U9BsmAjvxHHs2Ve70txOVtPLte6GHoMtifJf7Eq1S7JM6Pg1M68bLIxkwwsg8qPGaqCr0UX6--n5-p0RETOrK5V9K28Zm74x-R96iqfjUZBGBU2GRmeiCXL3RhumicKIVPLzGzM4wxbtiQ5MU86RqhYWkMKLQg5y8CCh8_XS-em2Mg4ElUsO3lwwL__wOi6YkCEijogZOq87CEuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m71UzMRR6gWQpJGl-l8RU2SZkoojK12jgXulL4yHutPGy9RI3u5Cyk6mLD8lvQelwrfVhGbq5KfdFYutOZmPL9vvae0g2jetnitIUvIu2KqmOQEmLn-U9heoPFWojB4rLG_SMkZrLCvbMftM71IT9RyEwjOcgDlM-xsmiy5xdfAF_6pul7pXcK9qr8orsqe-CX0u27JqYHOhrcJOEWf5sfw5TYzISE6NcgvVOcz1Dn0H0mGb8yjukxWufHCdFq0rDxPLCBa1cRfwyWeajCpFWRG3475OZCWy1QoHn8c-xMZwJTIpxoz5BVkfmTtC2uaJ4w5vzt2C6UBjKk8xRSdDWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyzisKXMG66TCGbPQRqF8T8JP63Q4vjwEQFKjjrUGAzJDDoyt-eOM6a75d6ZKUfgTwRXUfSqL_jGwsqT1yb1nGWsXnG6VusbuiVRvf8gj3Z9VxwVWgmeKetj87wpyh04rsHeRgsZ3OIL98rJHY0xxGtDoNycim9RixuOk7HTcecdbRcK0T2--mm_FIjcFLb8Q30STfXWrSvVey4BUfqeMIdlYcZA3ySkJNH6JC0PQi5R9C3qu6p0GMsV-V4m2stecG3HSYwvmquFpSConMoCjOJEZ17OtDwPNy-Oc4wcvfFh5wcQXtaKVUp7KxJCOBR0AvKu5kgz9S09gSVPlKKO1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPdy7XZL9xDs78ReNJ2q-SNQf9xpSpP3F1yFrL_4EswzyRGybaCi46ntuYVppB8PncBo8-AorZmLJ3WrzRVrXqPkzwuyKrxZx0sMNhUGAP_rLSM35xRGrfVVF2wGIF_vyVWqAPOIb1Vh1wLt8BGY-Q8lTOwgvs7GTXdIyc2XLoDJIFk2sFzuxJ_4sLB6KjU74nzn8VBMUvwOXARfCP5GnO1XhRTUMSBzkPUZuuxnIakr8N_xynKM1At8pS_NU0N2zFC8VTRznFoecS1umlOjOPEF7JTE7YOw2dE5jW8kWLL6_4R9NhI_xCjaLo-a_MBvDnBB1k4jnm7J-5HLjZ0NSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0OAe8L8sKOF_h28DOHn_4BBB0uhlJilgoFFGBjIMpyXjhgZ_b_SGIibqe7K6vDS8lDCsONsqGy3sE98wr4s9mkX3Rg2NMik6Sc_NNuGkFvCOeboknVWNqZHUirY9OCANxJIMsrPel8kvZG-1HcjRgInYJp7Tu5rczd3VHK-YjTNmLYjy9ElWHfVxRNyPA8clzNXWavSDrtp7s3q_ryWzuXwOeLw2IlZY0vFFNl17OsRcT7wNpBfrN8GS-WYnz1ghhQSzD40n_xeQS_LAy6VpI6inkc7LlPgP9FEvbgYYCUFsMF0SEFu3k4Zp-ax_D7tAc8p3nv_sCZPwdKX_NrdNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STd1v0TqwT8-03FKjvC6Pk5WHL2uY7rWuPUQJ-GCldv6-CUGZCcXY1eyvnF7hPlAOOz-TmGBtzRAomvqQzO8mUZPky5Y76ISwQGm__Aj9j1E6gBcM-JeIvE4y0WExh1IvyC1UX6_OQAGHS6NyiO9IAHQGwECRoOBjFjfdGzM3SZAlzc3bchssMZt8podxCkW2csvLe9yE3a2ylfVXUalXxn8QRTnBB-IA2ULl9lqmgHTAWrEv3qxlNp9_stDWCgeaK_U9RCE0WtDfgcDk-5-PuNlpSXFFS4Ml92uP5uCTWQvG85XuRpDiLcw42_0wg6MRzHLxdwZv3PiyiHHn3jWdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzCrMsdX9dgNkc68JTCUXBD1Pyym2bbKYVoSwUsKJnvz9zRohDuM9SdAIkBNpF-_vEkxKLIeTbyj_WGkQ9K4lABpy4yjB0i2SaGNqQXjkM8oYHgEDqA5VsIeNMkWKViCm1SFmJb5uSAIgFUSVM485f6p8pAzQsuZXu34KmVguA80GL8KSAXPjvMbrm1yM5SwjYclfPl3tP3ROIACo0DcdsgyGrtTVjEgFfVrxHCWF-kKui_ZNTKrX_1eg0PSSoJr91kRlltP_dkZqhkC3hik74qHWto2aetE9PS2YCitJ5Y_tC_o_rrRU9s6melnnmU2OVYvkv8pJJRY3T2orBS00w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJuvMF6YZc7YphZFR9DkOSWgCfMEGl41JWEY_tnqCFBfc8O44BS2MbcsbWLAoQSR_BsCTuJHtIwn7P4QyhsoUOGAa0JNNW0OvBK2iTOIs9ROFMPERhyN_DcpfQvyBvoWu81JYxwGImWkRGMDy5158ZtssBj60TAyN-p8P2v1TqkZOOzq3LqtIfkLfpVitfWXkl944DuhabC_XXXqi3KHI3_B45lt-NKAObP9evWe0_QEmMU_v9Icid5c7EqV8OVHoxjoKAZt3dpGjVl5cZ21xAUilN_wlrRWh6bu-NqfVK33nAf-TPEFGuOgLjIQGG6__5UvJ1BUktkq4YjpBv2peg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aAziY-U-Se7GWUCgTykwO5IZ_G7uDyA3ePNFe7_z_zUoF_roEY3W8_vNBxYgau0FHhJEBlVWtp69pmOqehiMtF-goAEhQwqsv4DlljeKCwOqzhT6Mdg_VMK3B2k5YnhqwpJKtgRNH9MJfNSbLvdeeRdXyhlA3-TrmJM4MAKgz4TnY2K2zqXXa3WV_Euis2QynJDOYMNb2tLtGQmrC212p6kMEgmDxDxKS3xgeELInwPtKVNUiUn061A07wcOZyfZcHdAky5fR4N8q27k2uzon-SrXikY19VsxYiar4dR_C-FZEJxopVJxCrXD5YBIP7VFUnfVDIlcpwazQ3nXETEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwSKovyVZ66ArUt4ftwPoixyqqzX8pfW9wPZQAVedatgO9ynLc6ZmqiLmiX3nw6NLlZUTjgsYCatXGkxrpCgsVoMOTwUsZzwCdMSwWinV8Dq2EYlCqWS3_sxNIzi6XbR00OvmgsFhGa-CkXgCxvlWxzywyHtYxD_-LnBKEJbpJw6NznPbyCJrducXa1JpzljaZShZd1aUZYGZBmEmdHOwwfbsYO_DUV4Z4VyUCpxK67vtmkzoLp9vD436wQV-xTduHSP3R_8Jg74KBiCZc4Thzr9243zrsFGYxAa1KfPqmTI7KlB8KnNzKed4PiXBVLYfWAz7F4r9sHvGXSc8nRLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hR9Ojzk7i4mD7-gd2yfbhBrxFUrg7jhU19JSHwVI-kdOthe6Uoy093-GDleE0pe2Lofde68F0wEqantNz29SGSoMohGHJm89VYSVQj5F8wt6K76pkLM9txIZ0hjOVgG3gYgr4IBzgv9-d90b-s7mstlozIypb6sAVBNQX2n0-M4UdrHPGeVDOjz5uLyNHAD-bUUH5skFDIozNj_ogROfKWkQ4ujJUxapkDcZSR1VX5-X1ZK-RRqtO2XXfwJ6np3q1-ozHWBUEK0mBcebsxijHqswfMaCjozWrFakEZWsDfDUJfx5Dk144cxiCto1SXzpZ7h8x-GqAecMFP1e2dw6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_xmXdE-2u2WxverADLgJtMWW_-485HrtDBMyH7LBkQ_bsi7FuMQeAqJZXiJEvb00KmFyIN-1VOyHi0MPsua1Q8_ENQeNcahb5lkcdFKNZRf3ske0-qEQk9abdp9YCiYNfEbWzgay_o-K4DOZfixKS5ypeFdpXKTvbJU9ooFVoGWwyFKq2LDaP4KtgUVwPVWbhV5J4pypN74zxsAyhb8k0SkY0Zaak4DuDdjIlfxAtiCnck142_gTavUgxZBGLKV5ctc3o82b4b4Xgme17-q7xGpdzvk09DjaM5-P4YnTNkYWm1e263CvgJ6OV9akwbIG-r1JOCtVydZ8xyuO0fNfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8pxb7hqZwN9tjuzMC-4j_NWn6NcDup4XLjFzIzD2g5mU0dUDvdIWvFH-yI6b3DkUvWsbgV7AbG7HYK1QcvQ0AATaakKBiPKacVgCDfcuZ89QcDRIxRMPmO_wQSoXF1r5D_mOeXb7DOpdrs8GbK3KO9Ivyx8pMf_fE0HpoLPT4NstAr0Yyhw29rOyUZ_RkeCCDJAs2Qi0dEB5Xjp5mTrmaUVatPAMHAiLygIvMzkSJ0mAktyNiPubGIFaPeY1DBvFGE78cf84LN8r3ZNQFETAZrC36iGwCjMqNunE3Y5leQIoHV93lO9Sde3_V4F-709-EP4All3GeJ_l8GzF-Iq4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZhK6tj9QeBqSznxZ5b8tGuiBasozOUytzugiCTxCcnnsf-oFvRe1_FQlMugihEWGN6Bo2XdzSU0x9GrxcBLw-tyuXP4K6ndqn8clV1hv9ZPjYwfy3IiKCQ14ozAus07uaiVM4VazWFyWJkrUJvBpRA6rmlMP0HqYeWjUXXmzFwYArNmyoUc-DCgh84F6BHlN1TB7vSkgtHJrZg4WEMWKkH0vZM4MHpCyz_Lp8ewlrzbHV_rskZX5zdfhiXXqf8A4mZYtfUpZkcb9ToV4XfrLaiLonKlquw-hBVoffLjaMxP-monAdJwJ-oWaCY2NtjHaQo13jpHlk6Y5VqMMPippQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGcLY4bi2yEJZKkEvgUAWLTHW1VUSC17iai2CGHAuf_Ily8w-hsgNGTwvfd1HRqyf0eHtH2duPQR6djXsp8_WGQnShyDCZ9K8uo-axwL1kuGRkyCv8LWPxM0BVrLs-N-ESB6PO9RNzRzwO46ezxc19gbcubDH4Bnb2EnYOSGDretGjhA2fkZpDKav7qRtpbo9AhfD82fXwkfVV6qILYOHIvZyX1Ac8Qu95Uormv5lWJJREY_r89KR-a_oW08l1icUnBFRLPkJWWFufypf4O32x54mDBXRFCWSONzYb4fWmkSUR2EQu7Q3KywnmxzZ2Ikz6R6httBAxrAtcigo5up6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3j0_skwkdZt1QUCsCN8TlpGIweX8dFiKiSJPibTN7ryY9B09_ZA5IDvHZWyT_g7nxgM3Ci33IwXf7J3SjEpwo0GNNkWbn99vapQ8ucLsehaREoLqefWLhtmc-otgvV6sCdymqLe562kxNaLcQrNFoiGaCXs0ykErOUB-oCss4nJmy1vYZ__L6PziUY8Fl7fJfYlPgGnW6rg2k0wvrbLS84369A2hfytHVNXi3CwGA3tfLwdPYtUNSmn5X2_1iLgoS2iKAV87UMSPeRqLGte-yyzyH9fawtLRmfoIUNOUsjx1HTHHH8XreGvBd2IYZaHrBkpi9_nMGC3kk7woQfJPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFaVi_fpusRtzTTSpgqpTLmbz18wj23UoDYxqPq6rg_opVVWnPSVe_wWO781avCs05LAFQ8a1gWYrzrbREir9nyRqT9yt8RTgPlnkCoAgUM_kAM3ZbYO51Cc3v8CoMSszJUPb30oSd9BtP1zE-OgGFuNImg6m06TO-ak_yvDOZy9HO5stVKa0Jwmxbv8OQCYDiKXV-xsYAiBTrvnZVB-PWjhFmyFNpYwMlvDEAJug_skI6SzXI74sNnQ_nuj93s_obBamB2C9Gzo4btHbY_RaaYgouMQntqiD7N1-RL7rjs63eDiQwR8OXSJtFoB7oGyFUOEYJnIOB1oC5U6sgjy1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPcLyu1WKwysyKepH7n2r6BmOw0ltRulH7kwrX6Hf__J9gBVKVTZp4XzbHBAgyX3R_4EiQDRKdqjI6Zb2l1aR17ZYjSJaJeK6l_4IusGGwDTWbkabY15qDxS-xMouyJ73q_XLecw02x8H9K6rXd1HZJiZZsiXABiCtM2aKoQM7QejCyR82NnAps85LMryjqGPTOXfaAv8cq2yB5Neqtt3hS822ou1z9RG2NcsKf5KjTPUirR050RVaxYRhTk1fI5zW3YcYQRK55oYy7bR4EpeLpSogh4psS06c-h_y67OqgHBpUWGwlTyrS_s2ZiNtEZLPOuahbp6L7HMm_rvxnhTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFsU3hEAtJtWiu_eEYlcMdg6hfO8BLlZgoqloa3wt_A_GzzX8vIeKxmXdxk3IHyDllA4r2zVzygOOAgoA4wr6gimIb4m2PDva5fkFyxaxEMPEvx5P7hzDiR5jSv3ZyEuItUCiLSi1nP3XoOCRzG0MC44NcENJ_J-iXMUZ0Z0VasduY_kf3LwqbGZtpQxSTtme-eR9KxtCaJNbyLXJ_dEoPnlhsRUhPzoLqtk_0MexQ0tyjmzVLjPVuHR04OZBbM_NLG1u_olkj_qI-jM92D2FWioFaQIySoA_KPcMJv1tu6UOXNXcN2bgaZ8SR39wj0BqA5DyLSvjtCGMVoNsb7SdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2ka41ZRVRDl8rjKsNgzNkIHwf6OPjERj53BqP_FZqTL7THFv8OkSta439_0O_jcrxVsCrMeLHxkSnuyu9hrsk5AYy5zprvOQHypUzeIkuZhcuNm4Ed7X1PuxHuMbDHznMjwT51Ne_gI-19n6t8XmLIPm6nPZFkktCN0pClyI6Pd8RVkVY1ee9huEhTE_Uq73iHWRZuVp1FotlE6BjCoKEjKsq0S1mBvBQvkR_EBe89Qj_A1LZvLMPQbR3kHRd9dZSGvLslQyiqQGKm0hmcUSwg6W6rA5f4k63oFVgnTjzO1-9W9MkqadxdFcJUgYKf5F_QCRil_KfS_q1_VxxcBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWIlL5H5xYXkhPbx-18fGANghzWbrntzc2qJbDzcOxW_ebgnEAhnNyExixJeIOOSlw3-nDEzUfIslgHe_z-y5sYY9K9_IOwzXkwgy98ZxZHJNPZ1lx6DaHfq-HHdMjm3NJ6Tt6iXMupF5g3F22JLK98oS-Qux33EFCzvc6faK9XNIwMzRZQG74rw0fzJENXcArxZ_QkDXqQadVzHh_yZB8mIHzywjShMsCpr57Gd7ALaQYt-WpDoOoIzhrkCKOBK2DFGGxGtMcpyxuodsIXvr7VB0NkEaXJTku4zG_56sEGDO8LktO8Zl8OvsQkbT0Qqc1d6V2ZB-v8KTWvR9ewZYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5bll13V5Z9PK4VVrXQFKBJ_7x37xPCKxRPmluN2xdAg0O7hnAEquJeykQlYo4Off7ZNVX3j8U6H7gHW7Zg-XP7Go57RJr404BJBNooFFLpffh7jMtUOWYDx2xtgY5_lrcPxYg6fUgzttemSLpyKMNXqJCp4IDNIoJJqdd7W6gAnWV9dq56xVCvL8gua4iH9ThOSUdlCPlktbYsjfilyPl-YqNF_BaNKP16nu3MFzu19UDzXAs74GDnZuwhfystEMyn--x94RDDnjBVC0UPrgZpplKXiCvb5aF_gf9OopE-b4Xbv_rRlKBm9FkAHdPYw3cHQeslT_2KVg5CTo7AqsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2qdMrsSSO5X87m46_67JEN07OuwlPObo6v1SS9Ri8-hfVEexgIrv2Rd-G-HN1fyUer9LFVZ84uRDC8E35z79GvquMtU5UhlM_aPg84HEFIp1obY2hx1xuHM5UkcT01X1P7ve8ACdPbsxIpbpj-_n13NxzRLQ5gCG9iTTHPQDfbvx-QodpDcr2b1EX3eMde9zehEHtBFVTaodSvok1yC0pxjJmJO5FdgxjnxXaKN_Oo9P3YZHpmbIzDW98uJTB8rNAynl00l_48OH1n8n22UbnJ8X0p41sw1KVc9HNZbnluR0qQ3EzBF5DAHOBzvxHrvzq-0Ktqt9vH_awIYTjXfkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awKtZUY9ul2-_hNJja52ZXom7pa__CEXwsd1UguCA3-xmzjQ_P7Q3BTfC84lSk_nAQGrHD25AvQUSVcnQaBblPpFKjWsiVrj0kX5l8eFxQ-Y8uBbz-zFziCarjeckHJWvBBOy1UhuFA89YOuAoWCNXc9EChpPmMiZssUnVZJoMAcVSh11JHyynVU9G1rKK6Urrx3YLNv3NjzJHJgd7xVCn6_RqBQqyWt8Ugnb8rPE9hE6cQCWCeyZiLCxUzUOIwrJGI9RApo2whfUzNWk4QXdHd-jH2wjX8aiOsUi2YCElOmv7zkwCniCWnW-mhj--bxgVPgVxV6jy4PrxgXJDxkuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApxHbvwkU4E8H7eOrYif9y7mSxWW4mwwbGwaPp6aJbVZEVFRvkcmJUm4nA4tZoudslLsuTWI30hgBGcQilvJqxF6Ga8Jb9IqB9L6WYI9F71xZefkvoWksohv4U-6fWB3CJ6yHlS0pjLrbwKLY_fJt_IufV3EiHSO3JI_6zh_6rp8THGcZ7A2aDuwQXUyV5VMbJL5Veg9szB5g_67aP56vR11_5KEX6dGmFdZv8lXHC79Bi4qcskLjULqjwD8tu8NbL6AfCeyoR9AbYECKyXjAUKNyl4NpN9Qob-fEpuOPzQvd7n7dD6ICDCqu9k2YkTjepbPGThaP7hgmQy0XxnGeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVcgbfTQTTHPtS6vvBrz0BG18TiB3rH5AZsVIiLRi2TpbBE4qR9mye1wfdFmG5-2sXP-nyqWIhq1HPbzldpUF8Cb3118IjOXKvPf2nW0nW3axtuL3xYn_FZZg0aHcUwgly0rdvpybfbVQEChVFUhA3IwAbCpyNZquHiGaAZdvjoFhZesVxHWQYJP-Ua9WYKEvoFGOomJKbGJOnt67og9JEAFNQaMY7OCEuOfUdp6LPXahsgysuPei1kWDg1dICq7zCbdps9SSb1fh6KBl4oulFWf6bSXr1JNClgUOICf-cLAqmtdyYeZVEvqlQvKcLQL_xfRZ5nJmWBo2ahBKrxbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKJ0zUh5VLDVN2vH4MEBF82o7yo52gs3OhlTUq8w5A4e4P-eIlMenTV2Ut9lDa9UoE1dW7T_ftS9zD6J_TmoBU10gJEexECYrhdk4h1AgkRtFkGVnvIMy05h6SwBRvHhrxUJv2elgMI_xHks-5pTIWmpReXNPlcoUs-MuKR3UJX8qPjbxHEZ-2fh0HvdhEwCWE5-g5WXEPb2Kt_pf83fqsmz3BteGxNn9fZOSM_4jKszCbtkpSLUSBjRVpvmb7CddTk0R9aiiftOtEvXg0nr_hjHb7Hr-mGuO5d9abxzQSQcSYc_VMcajTVgs3DEPqwplz98roYG8hAJi0LmAl_aMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdKU-dZlvXTR4QLoUuBt8tebuO69uPR0_8wBQcAsZnH4nrsjJiVruB2fnRovrohaDYkLuOigVR2tt_2nMkNW9F1-LTB_zpwrzLAruaxPU_0pJnyhDQ4T12CgaMrLt4nQzOL_V83N7IC-Wapu1cJe8PzhU4xURQ3b7qZI6qmPu9rtdopMSs-lH1-wYkHhV7FJikzErGnxvVJj1408Fibj9TdP-pnZ1vp5Byifo01hWYjjZsseYaQBCGcMpa5qCCQmEZtu6YrfPSi2160fJJehhFxE4TYBG4HiBxKBtn9Ikv0slcz-futUlSKxZ6AblTvQ9qO7GsHCktScQR3H6FhL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhhYQUbudLUcPSS9ePxMEqr5UPnXWfU94GJMcxWb3IWgJNfvybH7Tckz5T88C4XO2acn5t_vaFDA3BojkeWtqb5FprzoELTpr_-Zm2nygPNLbsaBaeKAHtIxhV01J01W7fwP23LRdAlKh7ghOqq4e_khw8TsPg7ooxSAaVj6f5J97G2XaQp2pWYSjKrSY-aueOIf2qOYoT5-Qv7j4WMAzgqvLP7B-fQd9co_lXX0ObU0aPnqEav-3zYNZwazxYwVJPMkZgR11PZyWtadPtSVRJ-B-_Vx2otet_CMi8GVyI6kj90zxyUNQr3KJYK-yUnSz3dd3F7upuVPc8Tl9cGLjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx-tIyUVo1Fwbrgcte-aM9WsCTr8AMiT2VxV61w49pap57Dfc1lD59GFceY7wmN1xVqQ7Te8_sumJLrkY6S0joKRJxrUWfLFiWONhNMSmLoY8w7_Z_D3t_BJeei6ugP0QtYGjRg0nbw6lV2BXk_c_i5DdHDAcGuC1Oi9WsXFfcWmROu_KMnNY6n2OUTcO3xF3D3DdCQGhn3thOolViJY0yhCEzMmuK_oemPLvY-_0znRWAzRvpZf8wNFXa10PbLb4KUmfO8ZWiZp9XvZIc1UhXHEERHpFf6hDba6ais6hk7EgjdROckqqSFmcJnfjR9By_aeQ0eD2sb8bCTMWHewqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAQJhuA-rQPYYskt1QZnLjppRQrDOkXvgnIghWtgTSsqbpcsKz3kXTvNKWc5aUqBCvxuDwvq4fbzzxYeKVs3lS32EAmhDipztMBYgg1aO7EWK79QcG1iKVHuKkRLNWPu9UIv9st3RVGtex5twDBdbXfLwbEgS0WN_owvAxPPlS9bxcqTiS22B92ghUeNubLpMhM5OTXj_zrkRKAHQSacZKRvlDDnLbUzoY16YRhvTHaAbSva7Fw9iSteHQ8Zjy-Iar9YskUJ7TBhUO7GR4Dxep7JhJ8JN9UpdjJ0Ff2tG1D0oSqi38WU3dKIYaezcdiViTEYUQYy4hmrI6ztWjnpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mklsARDyHzabNuTGYsRFjQL3XHRVaSaCz-vvj7Ju0TMz3x1q5lQ8JbSnm42HvjaIMBaGq2j-WIihTUr1uuhv3Otw2d51KQgMdd7Tk_8WJ3q8qqvGhnYqq1CoYoZTHLIrt67UU2AFTVu0CZv_Kv0-AXZIvP6S7HxN8NVmT5GeLd6kD1bXHLXMDX3WQyyBrnAVZplrzoMRx08a5DTq3PlCZoy9HivfJqmAoDcZIxHbEqRgaWk3cTz-bm0iZ10aGEse6lJCZ7aYGMGeMLBrLec0_HgpJs6v1EJno9V2kI1xzaOArHIJ_ErApjTvcqUahB-hvwi1Kszyfww7GdIncvYy1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT-wxz8NmfbMiuY1b66ctJJ8GrU1oCn1A11A9yTqCjQ6WfVAp2JQM2bsKxQnSJDp6N77dB_2lloCXeatLMumN1JpWNQWsvpEJu2WTNwM2HZ3xmhaL1DcJxXBYCzYGzp59xsf03RAfuzZBbEClCuEMGjtAk2Y37Ez02MLfpKv2ANRlwGb4bhTDuFlI8CO6xE8dIZIa9gV5F6YoTH4K3Py4CdhzM9YA0SzjD-hAP321NHf_YwSEFYo2-LcPXbGaljjlQZ2yn8nZerbEi_CfPb5dsIeQ4LQSvyMjCmBXEcEkD9J4eE2pp25lY6B0mmWCrE1WN5NrAOBZi2Dnv5SdVbsrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4UUy_1ybbF2_r8RjUOZgDRFWgzein1LtRDl3qFabfPg2Z7HcAIa8XWc7lHuAMSbX1CAPUjIDOb7HUZ0PTG11HDB57jT6_veICjTkmySRBCeuZi5J_CoRxbv8tuXatSK4MrtrOEX8yHy6RiWeIQQ9MMelElSeSSL3TsxzoVs9HKM-XtV7IvvHL6IL83qJ4nzmWiWhCktpw0H7yO3x2v9J7EJgQZ2MwMW8Xlm1oj8yRwSmm0ja1HLCjhg3QWAzcd4jiOZwYaXGVZqVLW4cWyn7Q45ZiQ-44lthj6X9RgOnoJ4YSDoZNXbRWEHVAjxRL1MkX8hsQiodadooek5_N0Ngw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV1B2blSMGezWAm-7wCTq9iVx9cwqbmI7d0ycokgZJGpoiSydxrPYGLvjtruk0e6jMgDTOjSITjG8w7vysOuhS6eEvZkkH3LH5WyUeXs-qsKZWcChP4KbLrcZQ1ZVXdSC30GxwV9TvKccZlJAvdjxbOVAitw2Cb-9ml5gIxNgJUeKRf62w6soedm4UWZzxyjR7MCm9uGX3y_BqGJ-7vGi9KSWkEAA715CWUtoAZonSqyZe1rCBf4dW907zGCmSTb-GkZRL18-DOA5qAq3JxgYZzqAzYboDynDl9qx12_jSCQfNWBhRYGgGgOU1ydsZgF7Vp1VQfCQrx135LYOPXZqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCvP9-CDlFMsid5SFkg3AlHi4ry18jD8Iu-riLBbS1gqkxsvqjxqm4sTRnP4RkT1tqEUyS9HfEc0RyG6MsDiTJSzUgCxXF6_eqv8sZzw3jB6hCKRQoma1pw_JQVN8MfvAZTma-av__gxwVzkU6MSWmumYRU3Do4DuvZUJF5VvqqDlf5DT2FwXbzYaKXBiP3JdbDVQOEpkvAvYb7OMGaiCUtTrQipchl5NvA5PTXrj30WoW6e4rXdmsw82WLAxqm0stP40iHZHxpsN5tlzVw_RbWzimrLRh93GiuELqDlwc03KNU-1hX_ybm-5nWXhAV-juBDL_i0fO1Yu0qCKuhddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-k0ajJ-DmiUFIrkVqRZCgJPdWzucnSIrFD25_N0YAjCBf62inKPPgk0dDshkLVPm3NTbUG8fAwVmEEWsiyUK7bt0bFj2EdtWiS8P-_oz4Ff_B0g6pJj-516CvXfXdCyTE1XXKXUXE4td6-_xmXJhTT32GcKZpCRmsoKVu228BqN_d9fcNROeLeG-EDiHvjrlg5rYzYqm7lyRMfaO4w_SZe3egp35gu6aua_gWc5nBk-9N4xmXw_dDuCg4rliXlEdVEQuj6qF5wkxXn31FPWpzcvtsecKdQQpVofDooWcb-lW0sAacXcx70o1lMez4ZgwRVR-5Bqe4arL63Ke1JLGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eisXIGIbjQJTJreZa7f35ORcjsCeXqeqX2lyfmasaffDrBktdqOjCraKT9Y7izjGNiIk3GP-zT3UQgPjcOpTDyQ5Kd6SYVUKx-UVs1rs_FPMSHkJcgl2MHzzjAayyQ4LcGHWPS17ahpHDwnU_S03-kOm3bNMI6qNZUDWKE9YWErqnjkb9A8q6XllTn153p8aqmAdAxKjhbQZ8injJCCGHmv8_KMPuI4B6gMJ_7UdVhEUgXmtAWGaNnFhvZAuQU2WVnX1xISMx7KdDIcOld3pobx5eHR0MWboEbPOGIxDYeeWgGquuFffGLopQcLdb0NXwL4w5MD5WbGXL6TN3pcJlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K14w6RRJzEAn1tN-BRdnWwWkX_LLYxAxyhSEEw0_NK05XpVIyG5r4aZjZO5aoRB9neoMzQNOgoBRzBO74QJfqJ2kiwFxjnmV4Ay7Oqg_dxOuKvqEl3d70QTGyDx0yeyGYZ6YpW3nj8Dy4_Qn8q7Rv01c9X4hbRvbtIIjFuXTg64BQSCfNj6gNTvm-Gk0wUE9uHFhQCtPM3gJCxItw0_nBDO9xOlQvXVqQbqw3t6HhImBdEtozmUMRGapSq9WsnooFGuhA1C11rDnPz2COiA4xPOh7GCVpSEUgiBtk8VJiT0P6MQsvoa4Vq5lNm-TYgTal4tcTY9rF6xCrvHaJaKmbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpqtd8kG1JYgUS-hQv3oEVY98loZgP4GAqLh1WT6C7fzyLjX5JCyOwPxI6pT94A0fiEWZ6UjUwUtcemQ-1ndHiImL_Z6A0h3wQCrk1u6Z4hmx6U_kaRCAsF7ZcUdWCFxqZJhl4PIoq6Itb4Q2edmFQy4CbKHcwzID4GdolWG3NVlie_XsP5LmoaPVeqVVOl7PL3dBd9jlVDF461lCsSgyd1rSnLJ_tRHRSqXTqbMv-61hQtjf61NhANzHBUhpDwT4jLdaoOAJLLSrNVURxM3Sls-muqjs8ZV-g7v70eMEBEx_HtTsrDvrmHixZeYZjTgiKr-yXQ5BhHauxGCosgkTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C86tct4KORyeEYuPqztmqsUGxqunmyPSXsgh-0rQyHyIH3zIBsvTv47rO6Z2J_wzAPAgPv3Jh4tRuXwUOxM0KAtp8XA69fV-PPMUpkiA8zwJqMUABdMMZ1Fj_bo7swn2ZHePV_m-eL62CD62OE9w_cKkYJRdwPX5ifubWXfcpQUt7QqVPB8QVObjLfij6zhrVsEzwu1SMJSmLVw8WypmF4ulbiUGTp83ro0Y3PAbLomS3WdStO3tDUH8YD06gip1cteUcx4gmcu6qcsPqlxTlfo1hlZlHKLEFEANHSKrZ2rM_gdlg9aNAwmJ2hlEKnKNPRdzp-enh1AjsBbDwWBCSA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hwn1G6CNhvLAqsAUQ55p37KTiOTKvMolR6_81Ukx2xF3VQP8MW18AAU7qGfqqaO-PalsTlhRpA32rx1YkptA1p1pbI1GJV52OE8luh5C_8j47BLEt84g1aIrqiPmP-uNBDHRJYychA_t8BLVfufXKCnAREosHb2Bb5q5DLPUcv5WhK9yFAwIwUEtpXCI_kjBJcQUWZi7wQ0bCie7m5_-_Raix9tg2diHe70X4nbvh6OH-GGW4BeZPUmbGvjelKnFT9TdtYaLWdH5aEju4lPD4UbrQlvlJ3nxFZVbANjVlDXr9-YnLD3BJNKSGUPpJVCGZgQjoxVequZoXNeFSZ0vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=hwn1G6CNhvLAqsAUQ55p37KTiOTKvMolR6_81Ukx2xF3VQP8MW18AAU7qGfqqaO-PalsTlhRpA32rx1YkptA1p1pbI1GJV52OE8luh5C_8j47BLEt84g1aIrqiPmP-uNBDHRJYychA_t8BLVfufXKCnAREosHb2Bb5q5DLPUcv5WhK9yFAwIwUEtpXCI_kjBJcQUWZi7wQ0bCie7m5_-_Raix9tg2diHe70X4nbvh6OH-GGW4BeZPUmbGvjelKnFT9TdtYaLWdH5aEju4lPD4UbrQlvlJ3nxFZVbANjVlDXr9-YnLD3BJNKSGUPpJVCGZgQjoxVequZoXNeFSZ0vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQXOVkqEW487H9KoIVMRqGp-CDxLdOjwAKY6XMQf0QxPPoTjlU943cvtSFQybsKUexQR-Z4NtEwJFV6lEdQ5_ahpFJNXP1dCqN-eAPa5cn9qu9uKUkqXrxseZnUUclDy-in2bDz0XBGWOToeHjtLPa_Am-BChj-89zbIBgvM4FtJFb2RjzyY4sjX-xLEKN-DbtKUS7Kv0m6xj0hRWQLEIBSipYFZz0-B-2HhOG3yW2C1eMvHe66kU7S30WvY-USkRMCcbWct-aZtjycLc4brdFJXoexoChdC0RD22DDtq1U-VXU8_ixAaFXmoHUiu_6JWx0kLA3-Cn_MZlxr4h0UIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNqsOBXhdj47yoVIQfktUH6S_afVc-2oTHvLsxVUa29wdN2iRTRlWEYJFhdV4i_FkKUbjoAmp4w42Ni7qRnuLCuHQ2w-LgE-Ejpe7O5T1zjn1wX7uBIdsWD_Q7M5lATvho076DOk5T3HbNOHUDaR8Y_2vPbWXe5sSJg8vIMWIC4VWL1-yG9IQQmhElSct8PtNNoNrPMd0VSk-olXEHE9RO753h9Hsw-w72ZAOqyOoPcFCWB8qvGBmkMfD5zjtJXukUoYdJ9GX4HZd-ijxENBgDj8Ia3kGsmvk8lQb9k3-8D2kIee1U9xY3znUXGtyCoRiSdq2xEvkMpwoz9J3l7_aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJR806p__1udPwi6JZ1KPZZ-AmDGGW22Ra-8kz4Ke2iPy0dCaa3HwEHcKVJHHAEI1iLNctx8cD_bW1LtsOz_Du_0I2d4BmQ0TId19cnaA28-QEZtD7Ewqgsl7QVx0DotiWi5YNMFZLBn6BVppQ_K2Xjdkl49ABbHxTngS8XeA_bGTYkzFwvdlgPtGKxtvEfmofuuZHVhpm73Dimd2321HgFh5oXINChi-1dpBs_5yLN-ebl0w5AFWZz2im5oGisUEOrLiwJt4KzAuv43EGsqA2XlH_6XveI2qDoGvfKm91pBANxDPVwzd9ItWf2rgne6p8CTf99YhNdOrDK90Bo2-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8DzzLKLQvgpKD5INZK7XU1GXNBZNdHlBUaVoO87RB6T18tLKqb_qGlt3AQdC2oeF9kbihJ3mi1Qsi0EHaM3XcqX9qnwFw4vIFKh1_QkEmBmjijgmtVPchzV4ALyQZiOTgcKmcBxa-Ouaeqm_JMQ6ajFfnlQn65FA9Ur7PLJn8m2p541vVbZQ-u4MBVUVFXpaQ0CQ_8jc5w6t4LGDBCN2VezMecPfVX8sHkwr8jBfnzsuaDcXpQxHhFrnGAPt7ICEnPkNks2LP1v9Syb4C7LzuHq-3avw8zAYCfz7p0vbaVDOXKcvU5N551LILeMRRsFLgTkZnDcPV2ipaeTUZ9oFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t81ALAi_im6lfcqfE-HPPhNPtYQgiOGA2yer5BokyhTNUGK_XgzWDVXeBkEwxXzJu8hl4JpFAwm9X9SSglrvUnMu6Cl_7ux40qTOoIG3AoR0c62A5T1NCIzlD78k9BcJ1z8S8-4UTfSye3q7QZwfbYai1vFkvczeLcu_4vksvSaBIPcREDARXWQhhFeuA7CJkl1IYO1_V54ySvGgM5WfsHx2O3p_uJia29OIxBtoWKMlFl0BjoHg4zNHNJHbD7u1C4X5fyCUhT6CmlDN5NgZ8ceRLONKYoynMEw3XSFwr7LO1qLFD7qGoPupqm3lVmoBQCffUsKsGzg2U7XyEsq2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdjiI55jUL14poHrX0xZN3nwUonbGt-eD05oM1Vuq37Xq27vY6he5dIHQyqTmCNi7mAI6zOGLUvP0Hc6zs6y9ul3u0IYLVoV2zJOGOBUkij381l_ZwCWLqH4tqzCnDLdFnL1XQZOCEgbgar3_ZWZ8-8k-SzGpC-9ievQZ5QFbu24CA41SKhgfKhaVZ1JgEGiX7Wvlt8laXEMULxGK6wmIeoa_E3P2YvrfUuBkU2q6kZJJCUKy1jutzrl4tPZ1WNKaGFO5hpCh5L_DGBVZPD7OjE89xL3c208y9LP_xqyy72wp_QyTWPBta7rixlSM4qoq35JthjjdluPE1g5Kg80Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZRsxGdcy0F21rTSs0RfF8yOlYVSngAaShySLfoqgyEvPz6r3dWzgCZ44GGuGsKywbTvR7BxUu2EGYiQMNBoCQlowrfUV6nfSpPbiMZEAvE-g9fPM_vOyGLA6zARV783LtmxC6Sd_5QWCMXvGnjddEyUV-ezFKOFsJX6EwEXYXOLxUGYbWEPGGwGI3Vd08pZW2KxHhVFlDdzgQWn5sCAVVxnPRPKxc0LEy52HKsiULQEZbLBvmfLZ1bogy7CUuKkCMi-p-DYUOoNGpQ9T_H7nW4YdFOJKHzx7bmyqyFN7xQB9Bz0MmYfAe8rrdGDrMgPs-tFrE-fxfEk2E3JlRnYdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rdm7b25T1uclEMLiaIU72EZPb0HhHn7-IJWhUfntwrYDRGXkLe4d1QiOuCsNXbbewt-wyXajwGlo6mgJWjSPELRi8g6s_hLyMeCkb6uyCPBYK3p25TagvofHh-jJfShajDetOkQ7_oHoI2kSo6WmF-WB12hjTt7D1_Pn0nY1SItDJjED5qnONlQ_Kn7DqH2Bpe5Qi6bpvznLg_o7scXoFJbRq24dPieSi_os_8iqhaKytOZtO_BPcfFwvqoTTuIyZpbbFaNo2gYF_4KYpIBgTOF45Jqq6VTbkw1AXf5AqhU59T1sIMD1MCVFlnxkitgBkcZNo3ecYTM9yKIzrjyAJE1Z5f1I9fKG96bVEO2kVE6EUxy9vcS3a9Co472p4MgRZeHdXAQIaDanh4GmRnpIuSIsg7AA4czCm_rNtaG2b6iVKqrhNycKCUquoTZN61gKJS09T-e9s61slezTPqZbPlsp8m2kh-LyjOW-fVu9MgnDk6WDRhjv5RHrpuQiGLcZ0TmK7fNKvkkQtBmePsTdyKwTd3YDXzfvwWJ7R26O81IeuBKtKvPAnLx8p2gfbrRkoIi5YVFXNJX2LjH_TnArEUmuexYrMZk9bmIe93iqtboL6ZzT5Kc3vwAfOzWeVIZk0Y2go2Ae1zKeiD8nJpCjGI24mSkfaBG-ZbuZkVKGsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rdm7b25T1uclEMLiaIU72EZPb0HhHn7-IJWhUfntwrYDRGXkLe4d1QiOuCsNXbbewt-wyXajwGlo6mgJWjSPELRi8g6s_hLyMeCkb6uyCPBYK3p25TagvofHh-jJfShajDetOkQ7_oHoI2kSo6WmF-WB12hjTt7D1_Pn0nY1SItDJjED5qnONlQ_Kn7DqH2Bpe5Qi6bpvznLg_o7scXoFJbRq24dPieSi_os_8iqhaKytOZtO_BPcfFwvqoTTuIyZpbbFaNo2gYF_4KYpIBgTOF45Jqq6VTbkw1AXf5AqhU59T1sIMD1MCVFlnxkitgBkcZNo3ecYTM9yKIzrjyAJE1Z5f1I9fKG96bVEO2kVE6EUxy9vcS3a9Co472p4MgRZeHdXAQIaDanh4GmRnpIuSIsg7AA4czCm_rNtaG2b6iVKqrhNycKCUquoTZN61gKJS09T-e9s61slezTPqZbPlsp8m2kh-LyjOW-fVu9MgnDk6WDRhjv5RHrpuQiGLcZ0TmK7fNKvkkQtBmePsTdyKwTd3YDXzfvwWJ7R26O81IeuBKtKvPAnLx8p2gfbrRkoIi5YVFXNJX2LjH_TnArEUmuexYrMZk9bmIe93iqtboL6ZzT5Kc3vwAfOzWeVIZk0Y2go2Ae1zKeiD8nJpCjGI24mSkfaBG-ZbuZkVKGsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbX9M0y3aol6JqPVeXpHuJllaKqEp8drNVVManuHTvhObe7_6A1hxrDadS58ZRFVRx1k-GDh-E_ov10XTldivZt_g-Ds-M2XS8OGLJ_0slrQd83nzBZmgnNjeM3OGNQ01UhHRfA26N0Ncp7TBCo5Z3zTvxiaYW9x4JUiWytGTlo6HxfiAwU7lxaE0ZQCqd54MINeX56TYACzR_7HwJ0bIv0MiPp1B97BhDSOiRPnEGVzYBH1IJ6mC30FuSLFyc30NtG-UFZJPrxu8rI7aoIiXG2UL4ZGWTMMuW3os-GIC75wdtt3teUyO2aEM2ofN0W1a0WJOj4bQa41YXm69IU8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7EcSP2po6sCZUYX4N_uovDL3WTNNp8xTeD6UB-Xb1MnM_EZNYyBIfC8KXv7bDch1aQGckk50oHCOpDGSwEB98r9_q0FEgA-eZEpInpr49kjS-_XgvTlg6k4CL8T-FZKyNmcyfDvj1yjXQaB2oBwEagtyCPVqf0QR9KuxviXZshPhsYJdDbToh1SwnVdtRWsl3iBGqQyD6pct_TL1Fb22wQzl225LmF0cSQwVcBs1bgvVtRBisAsuAL4LeUjiPDtqSXYRybULsusFvMNLldiTr1tKtT9P5tweUoVnMIBGlmNb1qxPr0tCvgX-sqXbNml17njfLKu0Qn1s52VSGVmrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmQIjxHxI2FPqrjNXdno_PFecgbtSBzodY8UHplPgyNOCXuyIFqjczZgXGLuh_atuQ8B3fL2TdhoKOKpZ0fvXU-R8eKonUi8eIS9WeceRL5jnlSWEfa_pY_aPOc34pM6aUiwpD8vcbT62RkSxAw1hoc-dLfuu1NKPlBCbLu2smvEfcBOzGnR5puvq7oakTlrolHz8U6dI91RN0Rblmg7B49f9G8yce8f6QcjDNnfKkvcv66LB3t3hebUahchb0kE7-jZolHDOhYWkPqbCZPnHgaW2N1ddn_3SK4UIuJjMCQyOnqsPTkgoA8U2ADrI5ZNQmwq_-7yW1fYc7OVp_UjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-rh6awJAc9NUpkmNB55A_f-ijumnt5E-NhvPPWQIjPE20LFK2wCF550k-wXpKj48w26cXX0kjMuwilOJe58ekixS90qgNXsjRtP64em2libUzIcLzhqNOhyBHV3l10N4ECX4fzPKCjeZgYo23zhL6n6LzYRpz0LBaQhF02pgpuo7ozZO08w1SLNGbwB7JyXOIwfh27NJvMkzr7eYpZprxZ6EsHHZaQXskRZkhojaC4D_F35quh3S63nJMJP4c-7GUwuY2KR9S7puxc73jxO8KGCwl19auKzSihtlsfH__De0RDOUjwuK7BceiazmEuYP8Wjsnw378X4VyV_srUumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHeivxrtyXu7Tk2-uub-gmomaKK_A4IG4yDs4Dt9VtIgqwzj7m1CalB1LhVf33WKQJi8zSq_Y3JeLOGKYCE5AMPRwr4JwZV5T7MQ2ZF-9hByVwP6kJdhwuiSu4thsTlylxo7Bwz0ZLGsDiGa9ZdhixL_eeNi7VXXkW3dD-vR-HCHRlyNwjaP7-ZgyY4iim_vBKjG4xwdlj5JKXrpGxIatbo-goDwi5YPIH4Lp7ywRlQogR56rJ5Cevowp8RZ6l-xN-3Ge__3Hl-6tJ6gDoMYdac2dbY9Tm0X1y4YJfYCxTdFgrVpm5K0cG5sEH-VavGSFDIneHXHg65YCzflBKxwsg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Uiaddr4KkVmbE50wEHd3_4-bQnGTr0m9W_qSOiObAa_slY0G4dz4EezVVvHb5il9mnGNoQIEPJXbCV7R6YB4o8fKgq8orxZZCI7CzCFqQsIBJ9G7ntcIM-s1c0Nz_V0HzeKl67aHktv5jwV19Rn_oqH0ORgYnWNNSUlKeZRTi858sv-JHZFUz8nEB2x8j0iTOOOIMObEsu7scN3bjoTkjmPvsAj1pLDufJJzWT4NJuMxgfi6dp7idhq9U8eJRSvuLkb141mdgBB7z2gPXOk6IZPrB2YTNLUorTxf15HGcJqqPVqzStgsD-lNWVrR4o3Ax15C4iYInul4ZEN1X9pX-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Uiaddr4KkVmbE50wEHd3_4-bQnGTr0m9W_qSOiObAa_slY0G4dz4EezVVvHb5il9mnGNoQIEPJXbCV7R6YB4o8fKgq8orxZZCI7CzCFqQsIBJ9G7ntcIM-s1c0Nz_V0HzeKl67aHktv5jwV19Rn_oqH0ORgYnWNNSUlKeZRTi858sv-JHZFUz8nEB2x8j0iTOOOIMObEsu7scN3bjoTkjmPvsAj1pLDufJJzWT4NJuMxgfi6dp7idhq9U8eJRSvuLkb141mdgBB7z2gPXOk6IZPrB2YTNLUorTxf15HGcJqqPVqzStgsD-lNWVrR4o3Ax15C4iYInul4ZEN1X9pX-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGu2wBMYB5Rfcf45uZeJydZjGgpZFnUjy8Js8B5jDNhnaEWSpnQk76rUVZVBJrhikCS7oKKoy3ZtzTTpGtBWHNG7ugwu26CwmN13iuMqVxdjQ2UxstkIzt_0lrN-LlXNvnrGMHM6pKRKrnpKYvv-uMk_HpVoX1aQCUNXdWl8yGMTEUHoaUhMahL1zdbqsJoJEFDN8g1RwEN9hxsuRX1yLlcauUW-e7_HtxxWPUr0PAg5F1EquIQE5J_2yuRUEmdFUK9ww08XzIPWSemh5up-udGW8BnPnI3BLQX4ejlTB3vkYKJyJEMofHM6ev9PiPwTRFVUvpfe1_J0R613Zi2XBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2s0MPs2i8KM89fwe4NA01ogJYNOVa_23gTdeG4iIqwYXkW46CvWKQtLd9WfQYywlcVrbXqlCgp64ZjACH89Hz6r7MZJpj6hxrTWntoHCnEYBkRXI7OwTSjDNNa75QE_WSQTzhaDJeyTXq8vNC6imFum__-vFbSQ1Gy9fz6xqu5w5VP7t_BBF2rgVBkerTTIP5dnwHWk0tE8sTlHr0Y15rsUyo5NzY1ae748V4TC942pknJUwIIvq4nto2TAYqis1j9Wfst2jh6mqaIpuYU5HymPj2o5K5oIx0qbsT0Hl0qojlCTHgbmq_jBjrjAzts8yhr8nSP2SnFnam-5DNFAYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIZrQ8mqcVS5_axY6t69VpmilBPur5-PUMhSV0pNIfAt575LicsJeL4n417ThBIoJVUDOQjUzd9sbQN1yL_3c83MCM4pyi2nQyYbwr7ZdaLhpqNm6h50L6WehkqaMb9n58PXjaMpNHaHBBOeVO45NZtiozvngetyyRJCLazYyIyfRQkLhBuQWip39EFaA9na8yLIlNihDheWPmsw9NrSucUZSx7RRK1JZdyM6ZHrJ9mbSvXWnRFWjEF34cH6XzjMxmiohkYAiroLwRdqKIVNKHKOsdEzaqwecb0_KFD-2LDAzitzmlCqRllBJhQQ3wk6MeG3V0uFiYaPJuQZuLXh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cizqyQpXXH0D9f6eKOYgQTH1f2kiwyhMhbqce2Gc7yfset77bHVepa8dv8kb3MCfsttPqFYrM54ngBBcuZdwLKakxlxgSrqVdEXg7fI4EQ2LxBa9yN31snlz4WQOx_d8cKCi9wiV2NH3kvrGiIV1nqUsdGS696VtO9RBW-MtFLNI-IXXTqBJeY_Tooqp0zkHCZsPwZ1JwdnCZJhg_QleJNvbnhQreUsUryNuYEnndE5vMEbcwwzaXlGNaw2C5W7igJNr7uj10SjTL3gDsN8LCj3SvUuJnxcSqC9n2xFyOVkiP9fQS2rZK200-sbKas8F6khvtDUd1ASZTLNkScfSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmYMzgY7YdiCdDaqiLSJOC7mR9WuT4fwR1Sp0SGqv1lrJoBbmeEAgjOs0cWeNEB1PS5t7RyMZhi2FxKeIUtIaNIdcy34fLO8q7t0Eoe6Gl19DJt4FGek_S9F3deG-dbKOblRxpHtJRdMmyakYCsCsqARyg1OTrTuYsyESSJTZ_Ngj2kQJGXAvY6n3aW3sU9fp98BB3EJKMALGojCmQeGcTIa06LB0bZp1MsqqRpn7DDVz3B1y6lcxXcBiwjglmY6SztiiSaSJITBmmJwcP8IeOPGMjpNPOQPl_fq1m4WnidKEhU1J1PP6igFsBeX1eGQoYatAcTX0ENYCHOdx5x97A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uID5iauaJkuEvbJnZkKREVqHjSRkPJE8EKzmHcq52fAl5tn-9ECDEXC39u1XC7bIbL4bvwrOUSIRhcyosy8W9l3KUPkGTNYyl40_ly5Yyyj7y1Uy7rlv7toT-4-7W4CmEPPWx_u6dccf7o8qRq_nXhxVitTsmllmSGi_9Q-V11qSzEbZt6DVhQRgAd7q081M0pvjP-0KgbdchKhzJgdp5jSMcfSmfVcMbm-EtRfZAcWarj_qX8EMsPEp4hSxaQDR1-QKV-JyL6DO6zAgbzbR0lsswQtTb74vGUdxHjoOqKh2Rrtqhn_CbWB_EAP5m8rLHQeM9jy6Y7RSIKWJiVESZQ.jpg" alt="photo" loading="lazy"/></div>
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
