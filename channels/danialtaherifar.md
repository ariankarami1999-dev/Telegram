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
<img src="https://cdn4.telesco.pe/file/iUdiKE3lW23jwJx947hrhyGEGnxnjO9n4Sv_1wTKjmC80Y90XHXy2IPGLO6GWBMVMjFU0ZzODydWNI4tHcRikbJ2Uq4K5tmMflwPp4MuU1g6GwXNicynsTSMP0krCUk-68_x7zDZXQSd4f_pz7Aw0gLqdcUxWDJTViVtQ7AsYgkTsAT8D-Sbpp2ZSQQ8CTTns-itRlp3kW6u4ujLZGPiEL-ZDn0cRixAMBGjUtCixWxFlyoj96Y9LhBP3CuXT9y35UhP9hfK7GCwYVFFxIdU3ZSYr2dlaAXS0Qi_KxLvsY7glcfhmJdHkASw7w6m7fMKvJ7UXlQK4WUkBHI5U5qoOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 481 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEGj1W6aim5Gn-y3O9pmwsGJXKv2sXtYdXJx8MUIEe3uiG41sZ9EfWnVCRks7B4ybhVfQye1b7HS1uYSisJ1AZ9ZlUEhuq7S7JFbrrOb60yePAdHd0E2MXRSpk_D8s5G9M50kVpiWpfi17NBzOjApkN3yO5pNc6Ug47QAO3TRcKtDUaUyFPgQ_96RdY_RkAFmgxvEjaC8sei3V00e-46Y4alUDQzES6Ky1j2E6G1ypTzO5c8l-kfft7lJX_3vaKx7pfhiOxjRK5dfNy_6aDVh7zXt7Bx9CptK0VfBBnDMvTQrmy2RtB6HswU45WfgKQJZ98Y_wGeb2oOy4grOTEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Cdy7p45aknlPpI8TYDwZMO2NDcFSzN8t-MWaA8zjGprP8oOoB520wnaTmiv9RkrMATMHSZn2iF2F9hHGbCmF1YCHbTJ3ZaGL-lzncbUzIaRAsvA4p9_ELXlLP1l7mMbnYuQX7j_1ND7Hiob3yighJVuhHlpNkrfKk91cIWncAD06ahrWCym9DmS-1aPY2RFIYCbEuRwbSELF4UmiG-7n8WTn1eg1NmaGe_NH5SRhqcfccipZAQU6QgI6coJFCZKT0SXH8QRepq-CNJsg4uXxeKX3ssmOLT7O0G_MUkhg9KmlTSMcqfF6MMAHofslAXtmcJtpBVbVrHYV8Hxtx5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vREIhl3alxEfMXXuTEAE_Wt1NwVdkkrddw2wtuii4ysFgx775W15Wm1y89QbE9UgebG6vNM7Xb8Nu8R3S4B8y36WJLfpDCvCS9rRubbcDa-Pn_LKX2rXpRe2rwqeQH48-KvY0olu_00Rd2ykENYtzevYbCVThVMdLEFHGXjL9Pwg9Cw-nYVG3awOSe-XpbIced9tkGOgem6pDlVEy65BlZmNeYpYRmh475lWlbV2iwcfzeVo8HJu7bQNXj_sEMjQxXmyHEqVYdJqkhsZzl1QIhsCS6yckdp_iMeNVF9nBNEvs4Ob05yvqX67u7pD4iR4gl9QxlsNE1i55TpaFmpiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRX1Sryzc4cJYQQhdL_w8yaM8yX4f5hG2gG1JIdmzteAY7-d2rZGHX7BPsRe7mt7v0CWxkdwB8mqRUgx1qmIy7FA5QIRq3UAbSETqljy8mhKujVlj4weRWuQY92jPEq_R4xJQp2LWriC2tvpsFao1Ip_OVLYXFmEK_9OHbcPoGCrsYn_XzHHobiAqgWv3dnDx1nBV1jPecKoJOEJjyuyKGVFjQabs_lR0dgp4lK2DXgyjfSRQC1GLoQeK71_lmWRjy3BQIz1IXM0_HoYZ1_sEp4xZy43GrVjIVEDw2y4Fags_Q0LGd0hTVu70hRARFB1NQ-T-qGdh-o958ldNkrj4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmPw9bdh4fbw7_JRO8QBdtj93ejghlhpQ-VTZJn5dxDwg48ccJfGzoqPjMdvn3X53z-eB_qKTTApwJExfTh21jKfTOi5qTHHGXBP7JQFvslh6DLdINN6n6LK-CNcMPImdcBlz5zeuJzZqdBmD_DvfKsN6RJbCQotLx4y-kUP97ZG3Ayeromo1Hs1jNtB_hLOLQ1oSp2tjppdY2cB9IVYAuzj0LLFy_LHlGO8il-DZdHBdME8Opb6gtnGtLHBZYAlQ3isqhsfK-Q8YPWj4-MEsv6ynSkeWumov3Qpn8M1SSaAoY4rFc5PI3AeSQpL3ORZfl-Jxeu2LAmNFbqCHIkC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSot2yxIwZYI0GIPWxK79rwfvdGTq5Z_DnbACKjNjcTZzFgrVutuqSbhEKyJ07TYKTZNRRvlKIT_Qqz42Nyu1WwmjD_XdvAag7fZGW9yQG3wWbPtujZOtvxwJm34ewxgyftNaf_BJf0wz5vErqJaNR4MScW-wiZmdN-K0V5cfGedslz85I29f9j4x5F1-AJy6vXQMxdgzMVkLrFVZWIBOYxWKZTRJDjOFdGHFty8oB0zp12G8AGvjVL2DIk-h7a9hJ7NANKxoSXewmR_CcIoumu0cC9PFtkGk7t5X7APrPWjSByNfAapj_p3fJZzqP3oRAPezkbSHT333E9EmXy0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/We1eKpgSL_Brq80s_GDkfs6-2tLqQ1CGMvQ9_MtosbWPwfAXBG8tJ74uC8cr8_Z4j1ULi2r_OQMRIgM-10eBNRPgk22VTriM3Zn3Wd3gqhOvWYtDge0GO4EGCatwBQDSheojVKMywAc45YYfObBUuypn4Im044QxlNqdN7DtGyJFYf5Wt8hIq66k7x8xzaDBl1KGtWazB_UCrZudH-BJLQFlIg5Fb8buX9x19FsB9fHhsbivm8mQYXRXD56qHO7C80whrayeVKkPZ_9T0XvIwQGdPclWbSFO9OMVOB4fcoNo_YvLgYNl0QJaEdnzI52q7_zviko4GS4APB-F_NO9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceO1J3vqFQxJjbd8GYOKxKDKnz3NQf85SHqDlt80Rb2eBYf_TK9qMMMznSW3FTGtTzeA6Bi2mhdpN5yzS9lCyqMG2iJq9zd4Qk6rdsvK65ZiDdMjyAvelhzUsVvvAHLUrHYfsjEK5TZQgstnonaRXaOm7DMDiMl09V4kg2GrwI6vp6BPs4oUIBhjanyOn7EnXWs1yZ68XTmgijtLK_klxqd9YZQqXSd2WjqXpjlHLb66c0GW61YVAI373UFdoRX0aPvmorz11WtfM3nKHEa6YAjJ4Re503X_faW51DOky2Z-IU6tIh2WlCES03JVwlA5eoWqWffCSAygjE82rWJzPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wa1tUHpyIhos348VLeP1Iey8Sg1aRgALqAAw9UowXtmSlc6xUaoS2v0Jx3hkUEeBvdpf84-jgs-Zq0LrZzn_8byJD87rjyGUaC5-tEo8eemeuA5r5uvgprr65MZYMS-ALIs0kn0ZFeR4TE8hq51gqjIzR8eHRdn3ue57203afeswYiB0w86gftUxoacHSiAbx7spbRlakfGAPQ_1VQwxlCqJy_Ldj0DQoiJYYFiKxVMlp2FbK3wIsUUbm2lgYeHdsea-vExxjyJfkYihmxgltZAp9npKTXuYCh_aS0yvWyOOY06aLyEn_i9H92L_cBMqIzI3uoKgl7rCghf1bD0JUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHgrVVV8JxY-iJvHXn7F8W2TgiGxAWAQJZkc1ZajNidavx9bSybp9NmmGlamlgU_ftP-g-_NkzCaZAL3wyCPpoiDnf5ed3InXz0Q80PnELkVX1f6N7XEXxmYnqIZ1BbRk1OFHYUa7RR6bO3lQs2YV4I6imauBKI2VmWVv0WRELNNeT2nGXcmZbqxq75EbaARgGqU8qeKA3HOwUeEMq2sRHiX4L4cifLM_XnFEB3TEXDES2yuMOavRaQcUeFv0aGa2EkKbIq7PpR2Crm0PgNZMZQSfOBnXGUfsBcvvZYIXtFJ-5mTYfydr55rcPSUGKIQgJ7UI_2AasxNtGcBPvZWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 855 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMQhyGQHW2Ja7Zuuph_KHY0a9Kh2tMb8UyQUXAAEduCWCv82mTMjwZS4_WXxk3j55ZGp7fV07XTc-jPwh-irVDV4evCfGvueqBYk76TQH99DbNiq7PKv2ubDxxumOADjiH8eAbLmoGlEeVzKpPqnDyHzMLhDyIVUctTRUGAlUcrfZU4AtFHmb_2hGVtl5BAL4YQdMYzlwky9w9grby_WHgwFsfICl8ienrmMkWcMbZby0760V2bzqt4xMqDA2UxM3Q5i3qrnaQl_MXh_tQPnIcg5u5XF9qKgJq91HjqSORye-F3NuhWyvuQCgz5bgfjzxCkstaBGnA1POqAynnZD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ivao1rIxQyhu4AoTM4_kG7LnI-WL72M0-kiiH5ts1muQ-mQO31f6e_hNqun9yiI5IRahQcCL-StdDo2fc3L291zq5fth129Nj3vQ7iIoDiRbubSJia0t3VTfyqAWpamjcDReQYzE6Yalvp-FJSTBcM31Kv_VRx3o_fglRwEHAi97RDwXxocmF58Emq45dKiFdCJzmJUvJrk47doFNpa6sKrYdjutFeiOQMUP__20DaaAuC7ahY34q0X2e4tFgzBT0ZVm3JV5idkBW7bF3ZDVIu2qXu3QmOCRpG9BN3n1yCXdsTF5vzUr-dIVhPWBqyNrSmlneY_oAxdTzGoQwWM_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYOg74KXtFA4ObpcPl7NdAdu3AoNSWcBG94RWqU0o-kGPZKEr1IXnYn2WKxqka3dvFRbEQg-1dfH8e0-_wHxQnxfq3Fi6Cj8lqPZvO7toWKIDyiT3GNi1T8yH0kyUeDY2TnrAJwt6YX5yhzTwN6dZDCzjmzCdmKxIJtDcEYbFogxIaC6gHMQTrWbTevQM312Obe2ApAD1zsWFdVvWFdGN9YC3eD1rCzSpipA7CP5wnGc4oAbHw9tfc3g79QwKEYlXpWMgNa6R-tf_tjjJOdlKvB1ewHkE5pbrRRGLhkEECHgWAn9igMSS2UgGSRNefmKPCoaHGubWB8sT0t1kn94Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyloY4_vBxrPTHKX41F6Hl2MkFa_2VCPOxNeJeKosVzwI5spY1fTMvCTYhq9M7lMNY9AckDPlFuW7FBoI4Ea32G18nPjuxox8UfqISYrXjzEC11Q594JNq1tLW6m6kUjdFSRZ-biKUbJO08hCGka6nTszspCSBvqVv82-FPzco3BmciuL7pf38vI_NizrvDkYQgupvArdXPBi8afDexhiKwBJIFHO8C2clBIYxOddGqygLjvTnnegpppmE8JaOiRcL_r9UYupQ_AItIhpckqVH3ztnWbHhxE6QDOm8haHZ6r-QJplLUCs4ni8TZY6R8fUdoQEkJJ5UuaLf6EJ4rHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-nrtG_IAhJnLaeayLZs8sy741SZ9gAFIvTVCSPT0ZF7AfYXb_Z5-BM0ctZlr2D2ELmNlAqGEdw9iOdmvG1k2PB8ekwdMHub4WnExjTl8jdXNGnZOve2KpIE18TYyXim52t_TfzQ7FDJLb2ISiRT2Gy0woM68QMxKZuHm3I9vfEAV4iWte8uQMQ_gTcUNk3LzuKzEnfPS6VShLfGI6GZRhU292JLU_8I2BLl4Va1OHKDtLjixCXn4B82ufnwLztstV-nG37cggexJQQEoSaDtGfD02ZrojKSak8vAze-g6_SxFezbRp2tulMs3x1xLti1d__wOM9CD1CCh2XZy0xgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5GLcH7vF19DERWlBMO_OI_NgNZwvyxPS3SBhLq0XGtb3iEw1tGq3cSJ5snij7muO54Ew9ZXnBpthMOVHyvu9TH0Mjav6nR95cN3VlSqJfNhf4gQ86j-LnBB20Fex34qQttcCpJkGazRPAyZRhp6QJwuRazjNXkkxyC3jR6TMwpHlKcMC7y59--zQBs988GflqwvmSfzZONg2r-B4I6t-GiF8He11-O68mMKtUJ-dcDKeAFg7kNYgJcq4gGWwinr7LORN8gyWQFH29FDMBKBf4fcFYbdya7jSL6n8by7m5npXEb1Cr5Yk7y1v9ozW22089TTg5YEqFuR5R9AG_iO1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWuW9hX-dnBHZgEpYV1Zm8vUbAYt_nqLzYdVffkojBntBxge-lIGLjlpWRXXXgqwf9ZwtPJUWsbkhV0-9NFT7AzX3nROPQwfn3V3II7LaFfMwKvql8xL1Y4W5bJQARjMhq3quo2sfPMS1kXNENlJdpbQLu1uKdzhCkMMK9dMDgclv-9z_n5uiMWDNnaq4e1E9INKNj8rd85VZNB4zBgMYofuZwD93TcnYQPkEHMIDyi0lqH2QMiEZZ2LtonG9v8bC35xNzzAcUwl1arYEMB1pVl6LHmWd1NSTdRPsZJltD9OCtn_kt6mE_31Jr3pLSKXnnu9rKJ4tVXdQyF5LaJ5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=JhHoaHSme8iF8-Kg3EWSaXdJF9cCYQSBDMiiX5ShCNso09z1_2EpbqQJFShYDpYPew6Z6fI1dQ6cn4ahjNXnJZcW2ne1tH4QlJ5P8G6TU-tNzgkjqxbV-gR9t9yhcYUL3TlVXTZkf8Qf_UaHtWVXS3tqKxCOHv6iFjZ2JTqPIXZ5lKvi_eXt9OGAHCSXcYbyiYtWNE45vnQk8wDqCNpsCUFin2ZxTC3S8TtSRzTHe7oR-IjBwa1JF2qSl3Wj3hDe4B1X1pNcgRwgiegx_d2HeZu0gAgbhr-EVAgVeo5ImmDslCuMQW9fy4lcKekFk6Enpl0eXoNkbA6gwHNxCfL5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=JhHoaHSme8iF8-Kg3EWSaXdJF9cCYQSBDMiiX5ShCNso09z1_2EpbqQJFShYDpYPew6Z6fI1dQ6cn4ahjNXnJZcW2ne1tH4QlJ5P8G6TU-tNzgkjqxbV-gR9t9yhcYUL3TlVXTZkf8Qf_UaHtWVXS3tqKxCOHv6iFjZ2JTqPIXZ5lKvi_eXt9OGAHCSXcYbyiYtWNE45vnQk8wDqCNpsCUFin2ZxTC3S8TtSRzTHe7oR-IjBwa1JF2qSl3Wj3hDe4B1X1pNcgRwgiegx_d2HeZu0gAgbhr-EVAgVeo5ImmDslCuMQW9fy4lcKekFk6Enpl0eXoNkbA6gwHNxCfL5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8YpdcjGaqWMl_5ODNbr-ZiOJcaYJQmVx-znDFLfKSCWV_5HhhWymM9ygGLQkU14xnPmk7sKNceTBtlGo-nFhJ4A2_3W4Q1Hf3dhoA3KMALaw10EtA-vqmUaWGXY5PJf0dOg0ZOT78lLeW2Fo5ibVemQHt6l9ONGktsCiPaMkf_IW_sjxhO62HYkThD9tvsGC2nMHYSguMpV-PpOzGiH9Dw9TeC8Bd5HLedUGmL7sbQO0JecvK9TokOmIj1y9QSTT-mEU2T-aUojK7Ro2_4TA69jKKsT-X3lmZ9jO4tMkcxjSMTcWsFquZXP0uHA91ynuHhXlJ2SGCjvcKgKWflecA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMnB6-6XD3QRINdUUURbsKQPEJE80BrY7_tQpgLdGi7-TD4DReen6ulr5xUuxE5n_T5wco6L1EVAyT8PrZ4jS-KZofkUbZIMrm62WTl4QZxn97cK2tAMvWSMKB4p_Ihg0gQowm0eP9qJlU_X7D6TtF22iCYOdR0Soq0n6z1tl315hJBxZfDXcWQIkaH9qQ3m6zG8wanMSWD_YOsl2vr-fSsUJqpqDyprT7wBd9R4qeN45GCg1txclnLnp5WevVazlHDOHlhOdN0Ra2zp0_E8PCkvlNQbABAdfdwNdJZcZY7FU50Y0xKbTOEGiaNaN9EECO6Q0FDTxyA0Tdca5dNRTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDMU4JO3sZhcnEzTYpQomF7FxnnR17Pbp1vDrjb_WgP2Ya2iWT3B4U2fW1AdoY46XSiaUhyugzohTDBftTFiiMw_um0Oq4n757yhM5597yt2W2gZnRyJQ5yX-5AbemcDD4vRhSYcehwUzh2wisVUblSnTHSBziYTvb0KYUz9PlU7AtUEJOL34tXLk-9_vplUiLeEZXqf2kjJYHVOwaUgr-Ief0Z_R41zTdlFQBVhFPbVIohaJLk0xL0adYPyA7ObciT-DVcdRfyTJoT_Mvs2cliixwzLMnDscC_qWGoOCX_JhdgSh58XD4zXWrTdkDgxIVwCLNaWp0Qng5iA2K33Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG3_48oC-ERSrro9OVDgOWgl1u6sRTeyeYQocYR0TNb3aCnEIoa9PJNng-wbsxIZfMLCauw6Nh5GnIn3dSp4nPUBr2K6WIxNEaxm3LkwUsJ_vXaJe_e2NjCUb_sPuBjNYyyZuvLLsYxMw70KkIF5dJn3xe30YPMKaN4CGof80YjcbHj4Si8Qd_rvw7GeXLHfMW1-7pTYK00zjPl4sRAL4yPxjMr5_GGCyR-XRiLo_hulCRaCneg9DWXN4SS66ao5s0OFqsv_z0KxKtfkL4vYXNoSGfClVEmhiEc3-o2U3LsvrVcYgb1aSg-GGOWxLPPGXkvkoVSWyIOAdI1LPvk_PA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 796 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqrVCfqh51vMqbp5lDgg2-0Xh4lIFcoX0LsvI0V4bEmqSTmXYPWuFj0pIvseAnHnvbUikxbp3Ywd2iPyniefzIUUQ1yDqJKVGMfzheiKQdoRAmclVeYaZKmPfWQG7Y_M8wQERNIPyby2YKWu3pkWXEPBcbBCb1j18knyfE2wP0xixGlmIBz7WXWDuWNuKJh51NA4cqX6ujJP3kPcAV_i3TI63EZrrCfsOqmT2ivm6C7V5CiH13z9qvVZaWw3VPyTWnDjpR0tOckKzoI_TsaXMR1TxgW9UymDp0gl7XzY9CS61JZBptTgyQrifELpAdJ_eRTexFkhnegpCmRUCcWLJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2LZP0sHS8oM4U43c9nNsonaa1tdUiHipg9nWAFZNMmsActBDtefrvGfGM7YJG59GkPRbJv32scS4jW1eMpQN6rYFtsB92vNGbbvRAT6KgJHYFDrgQQNM-ny7TldHTmrbY0yDFZeYYK0znugn3KDpJE3GEXxTA9tnjU0mU2PirOejO_k_fPFN8ECXzfwV6OkW4w5PIAa5HIRJfRNJ1_cyUhPvWkoienKlAY1JiBwwH-6uU1AEO0wRk4iV1z6pRDlYBtI0l7c9ZwHXpbBTLaiaCKWp-L5bPRF8simALqgyqVclrMCsckAFButvAe8p138JpD6_3KRuEYVNSuLSRkPTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wA0Sl4OB6vfg2R4hFMH0ovL4WNSL1KfOG3n1xUaPG_a4yhpaRNbC2qqUB8VSb-NHFiq1yGlmFIviNGQcl-qnXphxIJYqC0izuZOMufCSQ6RcU_kwpBTgJiFg8-kwdfwSBFyrA0SV4ekwHvVOtaIZCXjqqYhkuWZVb-RWNNC-1tNzg-w_hjls8Inbq0YA6sThBd-gHg-KP2giUMJLjnPCsMoWZdSPDStMKoRGo5-lzoMQxdZmcPvr1Topu8Q1BOAiBfEqpOvQ7B9TN37Pq7GCALn38TwYcU-_X8H_r7sw0rjrTkXa5XH-7iErIx-pHXFusGMkjAU-ZFcxbeTM5iaqfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qldflw6h1z4zpVGqHEYkHJ9DI1Idi65DfjLcvAImKUp9eFDriIijlDNCBelBBoMw-bXjltwhW33nKAk0NmVVbB5SZPdLWw7wH2h6MEny0uwzwIaMhgLHglSrrniiwTnizq--YNhqrpobjEwJ-22T7WJo5540-Sg4T5KfKuTTEL22w8dJ2o2l6w93iRue9KadgYFGB8U9368kUeP9trCT528hRA3ulfJ6AqUIKxJ6eAj_Ezw-0bQRLhHGWn8tZ5ptl0CGDfqf2zdoUrP-mAWloUnLZWxanDevIqK3xLiEaYt6TSktwMakgovuKuMZViIbzuudwz1rY4iC2khNKGWuKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3PDgsOa1qza0HTt60OgHiTojpoKdYUWsWSqncRIa2Ned521qwr2mVRZd2rOw9aq-zePDJZ2xEJClzBAMAaUV9c39PAs5ZvQ3zEzT10AZlzuNFUnzMp1JOOzajfXxFwusLrCBipbs7MAxsdgTPqI0USX4iWD7dSVfHeyI567WUxRvrV6frbrUc2G3VcurZmaqQHPFRo03jr98OpzOe-OG015strxsEpdFFb_aghjwHoqEiP3UX7SLdQ53jkFDkqJEVZlX7d8dyVxzWd0HDrG1-LJTsNhMKoYbGipyamxqHd4F_PtoXv45YxoiAXgjrmkHsA8aVrEX7R_PmEQ5NxcMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 658 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 816 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwIUd3QgO4RlMxPIaym-GPYKYvaCf7CoD02tsb8vn7y7FUxk9ndMiabel5I_8zjK8BfYyt6FDntMu25UhuYXyB3KhWlneiFWK7yCZqC2uDzu8NWvmDn4ihoU6OYTTp9oeS_hL8kbrg3HR1Ex2abl-9aNJncp7JHovwkvFB_TbYHg5Bq4_A29ssZFP07lPPblVOhIieeeRm-AwCm1VvWW7Q7JBkB78edSxVVx_J36MLA80ybqfgQoQ9BF0F0Cd0Wkd86GlcRgGHhoYpXSPYl7v_fI576fxqYbs9wp5kCC3NaWjkL_IzaFeThhrvbCVxJqW__ojbFliaHqM7uVM1X3tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOAvRshbJa8elqy07WTGtw3GkUO_Mr9zU28MfCT8SJjMI-7Z6NtFJTCT2nTZJqDnCsyfgMbMjFCUQZQtGD73m1MyJE3tQ0PqWDY_lc8uH935B3-VpIIpdExVhhWzbKre-7LWo1opkVshQrhm60Qgr_bqKnVveK03C6GrMSVOqEzKLCzVnlYCMblOhT-ft2UFw4HE_sO88zZwZhEZvH0ZYZWzMgX-3YGyA0aJQLjmnB0SNxeadVgUeiW550KCocwx6hCKENceCxkoaN3bNMhPAeh4XoTaUasGkCdWWKpUj7G1G48I41JMsgwdYiUg1SG14OEye0B59NwjuxdhVqOClw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q77O-JuiBjlq-Ds855Hu3C9G7RaOV7-7lsH1j1xJm4TX5LQDJkKI6jt9IbhDKN7QgSY1KxcNuOUcgTMJ5ZHDuSAepuKn0CxwwePX2gtC-gHyZRtLpDor-hAwXEmnuThQELjmnMw-sim8p9MJS1jwDBb8MzbGzANE3GZWz-a-MiqiXn_LCJ96FUKlQ3nC8e-YZ67OoH1R77djXA-QdM3MKR8QrKaUIgAiH8PvHcvV_2aEnNasuVwtoco9tSaoKLJTB4jFZ4TBRUAcgWL1UoAcUsQlQGktzyEbt-ZxCumEs6L1l5hK9g--a-8qCAf3-5FYZrjcKJdskKkSqpCaPyMZCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2BOj17Jx0f07ZvxWoWgEyqDfsQorVTRwYRAeA6gagPBIe3coRMqu4IINp7DrXWWILfYOtFmChYaZKMDlirbhJpz9MHSBRIYzSg0EnBM5KrElKuXEFnG2guDQp-A0_dyuV2LLOKxNYtYdGoRoLoK8jJ69-PCImp7WGmRu_avVdHe61detZ4UhvNwpr2FJbwMzjdCwEmbOSHEqw6xYAzqzs9cGFA0x_4GX3AUGTP8axiHrBMRXmM0yZ6WqxbBmPFH-7MHGOGpOCD6XcPbd_RI3Qy4SwEh_qHLjAlaKLpk150LGnfV6Lv4VpPVGdyNJ9YQa6j_BgsgZ_lf1Dg9WbLekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffgdFstkPMMdL1oyIltUYJuJW4Ju2Ntru8oT6O7BKNo2BmuglEkyiVBaFnCedaA5SoB5fRCPgLFI9c3biO9JYEva5U3uE1hoyLXujLEMkBgKWrUEcqH39jhTyAhx8fENhCCNRdTK2hRt9fBTUHglNfbEGjIePHiN7ExaLo-94q6HmKnkNW0imZqcM8GC77lFm9lWp25vl22G4xJy65T1yoFAREb0NKof6KmwIqAEfHos3c-Zagyen-7brM8ruI4u9jolNwADo2OQtESb9BiS_EVTraJXvU7a8wjZtJZYh5kjDuc-htdduIVvC-z_HRmm4GncwOV1FlGHnjeLm51HNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fn3tY_a9m9UsdYji2SdzNtg0VYDcoOMByzUerkDSgpNi7VHqqkt0gDkVm1WwTdpRZ85WHOp70kXhb59sGBHHjCB8RKzwa32tikhEUoRS8BNerBnq5lJ_4Uv1oDNYLCrYND0D7RkWsULEf87wif5ysA6mmoUONLujtN4qkZWNqeuiaNKAWN8688hRzISMOJONVrQTzkKfWAR9oO1VGRAyae4di4JIWPo-dRGGgChN7h8-_ILfFG7Ka8vpxfzUZFJ0PYvCdfR3uLLxmFND-oXAe95_iE6gWjfxkwW8c9B-cDxt2e5v_RSepuM0IbuqyOkYMRWtM-8fNVKG4st6LC2hiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXP8q8ET72HDCOnpDG5aZY72kl3SBA-oXo2wuE8WNSaZqsQxm0WkK3QOHXVmSEzu52MX5tBjy6IHCxmTUmrADpFB4XJhZntAOLOePpTjGukwCEFlAmt9xRJXFt88HyLjO0Qqliv7hv9nTGR851ZpkukHUxjsG2TpHMREH-iR66ln7J34qau7FDrP5pRoGBETiSl-e4ajPrvMYVkLrsCbEX-RJ-4xaTVQ7Ae-F484woz19r6c3FYKTO0YhT5ZpCanUd7agNF1dKSxOUIZKgT7wBT_fGL2-rMCXWI3MksRs6lYqJbViVhuCAOtsQgMtGb3kOZgaS_OAu_TbT3igGcqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aS-ngCvudw3mIhzSfNm9MKVGx7f8wkU2DuRTjIXt1xL3OagbqvzOqqUNRMV0eMrtDI7CoTCKdxQ_ZPQf1_uKwx9cjCXzVE6HvF5JXE8ew6Xa30uSUS2e18lrhVNkITLPIDF3jzTTzJuKG10NykfNFkvbJKnQTJsdFySIEjjDrM5DKsGo2u3qlmU4QUF8vqxVur0UTe3Iu_uNVcGs8mEfkIqcbf4MNUCWXnO26yAExywI85xqhirCju-j0b6wl_l9QxOju6T61iAEY87OnSVXGilMOTaQUx7D5pMDaA88w05xjRu0ZGbQuK3Cpg1agKVZ060ud_TZrHEUD_OxlbVC_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBg8AE4iWgjjfrAXUz2_RiYx9u2iILo6uOW0Ft0SZnBis0YnacE_-vhEvpB0B-t4eVJEQDw34T7no71E6f57aka-jZCQiqmkHlO4Szp1t4Z6Wjo6nBFpaGfjmTNU1_AOb5syNeZ8ljjxDbN9DcJe0MnTpvFvRT6ULSiMUUd06yTXemsy03KlKhnvDVuTxMjtln_XYVVjoFO5wPgdOtsRbsI4dATonj9r3P7NADHKpI0LMikOoivSfn-EY5Sj_2QZ4bZ5EKem5R5e4xPZzlECL390lu8z71f3snXazlwHOuSg492cUi2pTyQ15DEsuUtHn-cxF1nLUzNODFaNRUT-Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY0I91e3BNXZj-7SzyQanCbnp82PhLiCpk6nYT-VENldVdhJtFtjmd8cVW1VbAJe822CFH21AudpFTPB_B9u5nobGoQRh42fcssPDzhmruk-gXiaKS49iMXueAkXqn9Hbcn6evp-t1QBSiPHc0dWotMnOgPPEy50tFufjqFoHkkCtVZR3-Gor9c-WtkPYm2b3bLtiydrU1oJM-ivgagCEd_PBuiJCFgqgGguZJ88i9AXQGjeBCMCGrvfKAq8jPGChh_o8fmGO6d3oIVOsKnvHv9rOgPGeIBglTnXlI4CH3iUSr2T3AuJU7vHcUqTGOVyy6G4-8XaLVfwSPJhsaqOhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoR7LvxzL6ZZQ1Jzz0SnyMauwr79i09hB-wzNwovChRZtcC19y0a4-U95-pAlYniL7cABelQ0l_JtGk39TBR-GwNUG0vCporBzcwfp1UsRVNnBpHpKUh8dy_gfobpndJwnOfxYhnRyNe32-YPFRXW0J11BqGYw7GpxczTdT1AGu2Xsvzp-4FOOBJ6FOXd87cWI2EquTOQns60cmaTq98XYRVttgURzU1sSrp1aV7_a1Jokjir7Izk4AMZgQtJT0u0tUqFZ8hKv-34berqKTF0DO12RMq5poenZRQrBGXUV5RqGXd788zKgEDzmGvCC4yyNqdWuU7Wt-de5SUjn22IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsQ9RjV8p8X3Y25IGMSv_Epl9sI7gjoc0TgFX8TqlHfBwZyZ6i8OgucTxWqkmDy3EHrmBQlSV-Mo6HyHUE3G1YM3_bXa17xYT46_95B6a57wDwsC9ZVQdd5xKful7XQSCsENw09iVXazqpv9_UlnsO345MD_OFqKEqy_Yk8WAJ-jKK8begu3DT9nmKp3-POChlFbrPkGYwaEQy97SrN-SuD3Oh4jSGfR7ESMdiUVBXcMds2bXR_075gGNBgDbfzUmQvrh3doyhRm-XRP5mmgcgAHSXK3gLxs1xOrld4orqJk7Qk1WDn2BZZVhi0RJxpZSeYx14vfoXcLKfVGepVG6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tutc29HTlL6eB4dwdTiVptm87ao8Svf8f_RbYeZhUSBWVGyPIrgUliQFTz_igH2w_7gOc182eQfjWzNVHJ5Yz37gsuJB0stHzVHKN0p-PY6oRShIPEohJcdkQh88oN7MIXy6Bnt5y6-jsrkj3wVed4_owQtLxoDXPYv6QSkfWgqXApM1poC9nOH0-ACRNg3uWUb15vFdcUraZ_HvUKsC0pPUzNHjY3Xzn8kDohgiRVl5Th99fe9IhlydL_wR0tL5xhObSzdfChr0BB4Ve2QANB_7StXvqWHBh7vaE6Vc2xxEcogy3JWm-6nPXMuUSYwt5l1H8nO4ZAnSWRSjC8DZ7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 710 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWDAddHq6kNdppjArE5WPF1JDFvIAvi18pp-SJhha0mev4uuiZLdKQULO3f93-NNjB3ZCSEbOKtGVlMf_GB4pa0AGsuu3NtJusabxsGo3qDfbJEOd_3-PQIfXXpu2mWndRXn95waF_y0aYz9wdYKk3aU2Md0xWM4sqwL6tPWvXpFVi2md-61O7u0Q90iSNTpE4LtGCufN8lwfft-VqAVrOqsGThciQSZ92Ha3GOtHw7RJW7FAa8QsMGZvYq04jn6xvCPe_tczbBzcEp7sjShL3EjxPM1UjO4e_epiKBwTN8Uiz7UVy7FqmKuJ0E8-SDIEiY07SbVOGVV4zxu2O5eHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtQxCGZuy0Zo6uq6Wmwnv_9vWz7x7ngQwFsmve6TZc2ezDbKjnGiACKeNSA5Brc47kzyJ49d9YCxDnG93e764xdpc_W3b9r5xr0kGhTUf3XHF0um6rOl0dRrDQ08NXUkUcie9mHWdcIrSuxXQ8LBycN4F14AgJdTNJGM5VhswPyOEod5H6Eu_W7p9W04tmTvD0zJobW9XAN-pCEpsOEHIyjB-Ygec98ObRmBSXyspks3lUjTkJThaXti3T3iTN_gma98057tD8O9OQ5xap5k08dXN5iA-uS4QcDpnJSiH10E3tFnoXQuB75OHHIvfyQTKniihC_c4LSoM0mbqzEGUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBj2WwtcgmGtvCxP44wU747N-VMz9atL_ySPKVEw3lvy8Lgomle7ygWURzv4YK_UMjLqyVoxOjVEpoRxo9aQXKDoVHDoozYoX9fyswbwt8G3WwzVQl6mY1EctBp4P8J0dxO5_Pxd2wCoJSzEyStTM5o2xP3EJC80I1MmZ5B1TUaQZH60fjAwb6kdW7PTh3YUgmmKzR3IFRpCSBBf_5kVsMzaff-NPdc9Kq9jHNK8WtEGRAOuAsA0bXYoqfT1Zn3ANqNuy0cLH--lsOdBIZgYcDQtP7OxqoVj09I0SOMaTRus2RtkGC30xfeMk4Z5c-RfPkpm_lH8C5MIFdJW9U6cNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i8NwOmaLbZmdanBTPpQYZ3B_yGWDM90ktFFMkKlm_ErQhzye7FPJAiE8Xg8jG6-RILPx5unLu8qk0OF7ePZgUjA-hIVx7HZ-iGac53je-yjZH8s1OAEC9EkIbwA-ijQBIIoyPLPynH33uEYPfCFguJ3TbhOoq9a5UKQ4kqX_c2MdKI8SUq36y3990rv4O6RBflc3REioxy1mMY0Fcbk_CZtOe4j0GHHUgbe2L77_iAvyndtuAZbBhHcHY7Tzz68kXjdZo2fn8qfX4XYl2W0tMsU2KcgYUMNhlAg1NxAHNzrYH0tEjPPxaVwsIRDZ9ZEeI1oqeWm9dL40Nf8exf0tWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDP9rlAGzk-ETyJKn6X46E_qct4zN-G11D_pQr1Kv3QSE4kM7kCujvFu54cthsxDuAeKouMXAxC8ssel1-_BQwCeJ1oyG701nCv2N69g9u_j7Uxp7p_MKfC5SK4oigCP2bb9qOsrSWOq8IZ1e0eCwuUM7v_HiTl2FFloRY58AmCYcc8ZHtRPPB1bG_wXK8oGqXRvulH2wzNcvTXOpQR76qCCBmZrkRG2CZHMZ473C8aytNkbIxLZey_SnDCrD9UIhMyCcgfJBUbhOuLAPS9Caze-sbhAS2vj3aNW4IkAY_pDpfnYKUXwGaBI0hPbMSupWvIlra90Jxovk18C3EFIzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVqEBqohyKo1NCpkxhLZ3XKfrom3DC-9dGpn3IdAlhzZHmGsN3INgXzSMcrhMmclFNPw68cqs_k1Y6G65op2E3GpuBfeayGXwQAHqsFP2TYpszPt1fFI9bzsS5ZEfZCCC_vnPV0owkfzQpWaHHr7LD_fBkoyYJVr22VrLdyfeDmsPxnW6ErZSJw6dgN9z0WT_tw1xcpXi1_4Wp2pcxcHrCZNsq10hCbLu3uk0xaV9E4pcl9ZtYek5LJUGlCXk3867ym-dwd7AXLgCzB2XemWPqOE7xUHvFpTYvbGWZAgk58rsCgLQyWSVhkuHUIQ8rAg8nM_HOb84pXyPDVPF9DoiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUbEJD6eL3NpXWcjLH_PxcpzEEckNIJ05tGLVOSsP-Q-72d0TaNxdhhgdeaLCuVd4KzdTOwf8BExSeDsIAFUtal3_dCwg8WXTJqqsdouASmkRv_3XarA8GdprsTRTNbzRy-cUY0OmOHqiC_P4H31DgyGreqv1VbADdu2kdIWQJgpLEycLcsQDjFCSPFgdINI2BWNVoRoLC2GQeBopwW07WtV3oQ2oMthfVDb6jx86KbLBWhqH2fwsEtnxumoOqyUQyCnQcG6hXQZcvrSLEdEpaHbwfv7ndRt7PN0-iXKBo4mrVZZ0vHVG5bOVHOQdVDlsUu1TxU77mKajm_JXhIMMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHy8ihZ4j3iFXEA9Xksjd_DMgqdZnEEfnhkhQrZuJhpD5x4onbWfvj106PIz68ExPM3DQVnzbjtYAnb-SBg_aEXLI0NCBbayR3TSxqsRnmcxUfKBnVG6LZPsjbFDq1u195TwFTaRnalx8sBRaOjRjFWoGBiEXodZ4oaL6Hgmc6UYGcxjdknZNjw2RDLjK-0FDd2_UGQESy354NiOva1bYgkkK2ICqAr5m1tSe5Hgnc5lkLtih9UpHQG--y-pFA4lHMda1pSW9CWd7_FgfKS2IuhjGjyeoT1RcMPBLo95PJfxX8zhOa52fXTr37f8rbadYtqDSRfIh9-0Vg_hOJF5cQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOa5eoWYh8GTQrZNMQV-uUb_wS6rOqCwloNOBE20YEYQ9xV1OBgTrzqpGhyaiZcRjPcXMqPoxwKnFHntBuYhac0SNbXxh19KRTg4donGe46UbQOkCn1jgvO_tiqlmd0blSUUy3-gpwmUwyX7SlPgqRZSMw0ROIDGioy_Tk983VhQW0tDD-elEHolwhFgxpx5Ve7Wkh8E45m-kIJmNF7Lg0KwLFoma9WJo6zfUtwYZzyNB4WVRLoRVhpOCuWLyod66vN6WRIuEZJsHtJuxJg5qouEh6pSmgWNX8DXqheneh1lgxjTfAkx3boymR4URZcX1-A8zRMIb39NIAqtKlgl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieme9kxqfxqhY7CWchkzxIJpAoI7oEnrfAi718uyUpEreZe9i_hrmTqEf8tlVp5j_5xLuPyOip3KXwVhwP2f575UdW16m7pFo6U5fWy_hiIlcmxLvbi9kM8_2HlP1d6lkiusQOSZSdGxSs8uzFdrMY2Ywx6o_h1aASPkA97Bj3XGbN3dd3E-qajuLEkw5XeP3GNOFRLnOuUzhhppJ9_pf3trvOUIKc8AL8j4r_yqs6PybixZQj9pZxckjOhxcuWbQYXAH12Dyk3m_nYaWyq0dIQhvc1hRJEVbYcPScuCsBKVLbbnm5idfwWIH2RQdEyfwGBpN66NBR_VqCdpQaa5zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InEkXE-fRdpOCEY7HzCejIN4FLNK9_5c2wk6lX9P1gFnlJzZvz83z_o1MvZkNl6oUNVb8GSWVyspZxJwEG_pYXG9400NLhKiVB_7kYkgZIOlFBEcHkQoNwDHa5obFC3cFCg4hyQvDybHlVh5XSdJfza1XNBwBO9LndekmrBH36QmKdvdwPs8XgV2jMHeGFZpBzkJUeBiQMJZotDYrZ_8qsekXoeueMo5vb2jnHvovXjJ-sVJGGiKPe_8O6MHlvN_id4JuZIYYj6-SyCQYf7F1npX4duU_VT4FK_SJL5CFUMMVI-fZ8iCxon96JXeKGWS-2wz9-cZrC47_YaK0vDk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eF3ftRnuTwaMpSXk4OQmRzvnYjqHse0vWWHvduHgJmEu19hiySNHQaf5uZRmWBTNIk7Dg2VWWI1utUMv0yhrl5CWh-C-UdK2Y6LdBDUlSXfrCZ_BC23fmfb5X0gY3zJmv6uJ7hIgdYxW1ATgEnXOghmQ_IMRRPDehRZxO3zcdtZjRUoSI5EXfOLt_IVQcfO06yDNoRS_Yl-h47Y0h2wOE7bpwaSDFVbcM0-2FCJ9Oi9l5-CWIh_1s3AguPuBm58HDpB70q2Fc0v-uNm2M3i4nK7vxfXY0TEkDwHSjiukXIObgju2K81HZjfxwqd-uqDniIIK0i2xJx0-G1VaTH29AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIME8VB_lzopfmy2fLfTss2Bv_UYkp8EgvnfGUhm1botlGl6Xpa0Y_aIfFJCvO4ukoP8-23v51ILx2QF8CPVtxnBDcVVYktp7BENhGY8cu-RuXS_goXM3_rpj1UbYwaFTXPcmsw6NnUPDKel0yQbzbdw43a0C-FWivlmmfX0KUOhseZd9LzVM6yjgXVw4-kQbz1O9AS9LnZBDaZoLd21LFFllQg1fn_npeM-6rLRWZMdzXB-QTkkrh0lIK9SBJ4qNZUb7QbB1F2v7oaEiQduOwDpxgrZQFHAHlSksbvF6Hdzrsbu5Q5P5MRAAUg1KNFWyYDL8oRlPIiHa8dPjPfbbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4kr3J-nvWg2LBrbtdT_V2USRpY4exyuV7fsNkq_uQjoqwB-o1g9S2iyE6hAfeLwZwAW1NNGmDg_gDFH44qQwW0W8t6AzcVJQeK3W-b53u65QtMgrBaO3o0oQwcQRWO-MWqsJiAafzjog-3P5aOs-F8cyqxrTEKVflz6dRJVu7DAXbbVZh67Qnt_hQrRAYbmnnBddJavWdoSYqLFsGGPPBaEY7V_vK0-vVfjV7XY3-6taY_uRqttGqjH2mago58WxpFDwTv_gJLzBe7ebSl6V7-rwvdZP8aLBhx-Bmg3F6dN-9_t3hEuCr6CbKDPp6lDI7ebnzKoSugsORKIhIPDiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkrBbRcE2gRri49utwxiEyjh9Vhvz7wviN8n36E4k35cfJom6m919E5pXK0xboleHdTvWlID7rcRzwSTkPH17WbhOyB0DZlCdbg_fdL0WQu5fwkI4fX9n3H9Ju6FZBtmBetkOxmriQyvk6BQJBQQRsg7RVRLGCn9RKeLOJVibaehMap6MdW-jwJLQk77pqZJmAhjllfSLKpVtzFjK5T2rFG9eic0cgmbcQ8vu9t0clIuQWvExbleT9Kjj6IE89USV12KPidZyetoghET5rIlj4NXpqVOMPx_X4ZGcmrKS-2w_-O_lsc4RbGF2g9q5FoJ2SBHoeSYE0vqyLhwbDinEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8nJKJX-Il5JggUKQd4tcjmHTOMeGuko0esjbAEQbi24ZHKXKWVKAeCBzcjTvzaqSCOX48jD-lRS3OJCV3MIJxMvFEmb82zzjeatyRLISiA6-K5hG79PwGs6B4wuGbDU-68U3svJ5QvUoTJBrTtHhM9GLof1E4x6pF-kP6vq-9Onn4EjllpKbLD9g5sHyIv_8CkBlaFqAmqydc0NwfbZ_iEXQaOu65YRL15zfNqyFPXAFj2xb5-vzcWPo4_kfmFa6XsMcWRJZdfqtrp7JS5KiP7LNNu_09RWR_QxVi-E_iC0My9AHkSchrQV5RsdIzMBybnMT1T642EAPqe2NO171g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_CV5-HUNjRCYdtzqrFWI5Ijd-4hfYGZOYXexS1y6DoJeQ5uGiEFg1Nt2BlOP8MI_23TstVEFi5s3Uu8xAufrkOAJ03SZaD8SfJ0DUOhmQmgU6LZTiTlQQNbo-Bv60eJcOmSQHbmqv6tj7zKer7twk8BaVAw8PyGBFAMWRxUci2xnDAZudJXvv7m8rFrOtdGMWe8rWdd9jYUK6ZLmdSyrdskl9HsjapW9jQzeJyJyHE1Nz-JYCkhNdb9lGpX1fUqnoZtUSfCA_SYPAxZ7F5X5JjnBlqxgb7Sp0Bhm121aZOJE88xlVngh7d4d13zGkqT5EvFvoESxqjw9mfm3nDzew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFTAHt-xH5sfeOxPSQ067kp04Jlj7U57lweVssrL_-sRgqaNzbMVJRTTA_9o-LOmBiN7IL6BzhIGRFqSJDH34im-cABVgb4Y2bgCofC3SVL03mOVHrTRa5LcvttjGjmm7x3fbBOQzd6vLt7_XQyg-FmFIFftroifzH3s38qgA7x1UlE4nk6CP_VdAWCWyUs3B9PZTIT6m32DLTYoSnZur8VmeUlvUums9_rnq-iFoAsocWqorsZ0OprIlpIS5EM3hJt5_6LqevG5MWplr1NeaDmLp5ftIbvQ51zPDrcsn4p2Rmx6cMdHstYVA8DCFGwPsMRmhSQKMKwmPzKImQp8ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0OOoi099E7LfNlm0SSV4T_scMoO44zEfA1GEsiBaUC-1THm5Xr55Yaxw3CwQNCOEms3xe-XMLY9PORsuH-vJrGP5xJaXUPRx0xfFSnqBQflkYKOF9uJiWjOzqHgSvz9SkamYVAxcHt-TFpR7MtdYaLUr2sbR54Nvw0-vJITzXTSougRG6WuKZqBnAR0W06Dn15D3X6qewcr71eWwmgdTTYBa-RoJ5-Zue8O24BNb5i4wfK9evxQJ610bkcoxL_r6Bf7gBJI-MoTxTEJUalBFUAX392E9y6MeAPIZNBMfgxt3lW8vXLx9yhjcgziwg3JsCWQAzCfKM95LSqMuxEfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8UaPe6Kb2IVGKua-VXD3T9v68cAQBZodeUoNu-Y1p199aEzxbsO2GnkfqMBXrAqbKO5UQsmOsLdok33iN5efGBwEzVqCJtaBnswH88rHwv-v_BhQbKcy32p7o5_EaitkXPopjHpZVfQ8FcRbp9CFkiFaUeUdmfwnKUEnq6clYDxboz7w8GMIZ9vHus1JrtsiRv5SIT30dUZMJbwTh4jy6lpswt8ZCDeB6t674LcleobcrZeBtz_lfJ52Mw5vSeD5NrjoPkc0escGkEzdW4FsJJSBOv-tKxefnOHSoh-P4u1O6ao3QL1TQFvZi3Ex78m1NkkGYkqGmXZ355bJoDoPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar85qW7lH2KRfE9aE2UAqkWPf8MtBgEYDk1MaoRmUF9melRahWzgXOW1faNcBQvrMLbY2Z1tICruhempbt3KKyKmkel_jsPuqVSZUa-a7_Hekn6_Z4R7jegYr4BP4EEPnMN8WYoKY80WPWez8KM4QxEHLjZCNBYfX3wTovNwfytcVMBFLn8cDHD-7SdxxH0Qc41ARGz9DaANWPuUH_zS-1ot5J8luJGJJnebNAu_MSjreoFvZD6BLJlkTh383CnhhbmpWmRY2jFj81BxJSoeTzozgvMcdbI4KJEePvp_TJLMYm4bVXoayRJJQGvRpXcStrm-8IteOCXsB-PMWI2qeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaIY0r07zzc4rXEIGj7_RwMFYIbrgFGvJNYtcX3Yx2WB2dqUJE3EtV_oOMRrT_7SUJcC3yTfTBEBXwOXmRmiU3-upRMm46f8mfc1qTjAPMl1io1mvZtr0ypZQe8TYk3o9KzW78UdTTXtko9gjAXp7HKqKxQ4jNUADHlmetgrcxO9UAWEnXyxVkPKN7LzyjrGdkLNA6DJVyF_tN37Afou3yh1g4xy4lpyYak_K5Z_mXSCu9jid7lvV_f84kHt5qZsafTVaei-MCiXkoAdmODNNuZZ2D4_hqHs9OKqrkjbdsOqVm2EB00_2TLTxJjqx3sHVFMwGStduy-xqfqZ1P-5RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-2UlwS8Kk6SL-oMkcuttTGNJTyTDK3DEN6YjAd3OQ5-_2pxac0on8S8fXhLHU_9B7myz-FXz4mQLtp1-NIv-d5hnxMsTMUPdOm5UYBOBQxi-TjgPxsouQdg2QXcv_0rXjNGAeNxH_kvGvKVgTZAfjGGJIZnVLbUYkcNkD32K4FXpfr80QHhIpIS-9CY9pjsZ4rWDBoYAt8JzakDBQgEXWJZQsMjxvYHt5Gep5FZO_SkHEylJMIC6mO-oqKl70O4MvbhIHt6m_0fYx_Y6xoZLVE-jiRX16pcTvouZzgrGDfYy47Oh4Q_zpYFcuOSfRlnxsK1kATF7uYfAiLt4eWPMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c91f_Tfy3ADycpcS-Phs0Q_tmLBwxvjgInYNkFrS6mMPvPY61zK5hDJkfRj_dQA9sOBVV_rSh3QT8VKaTXPrn4OPJkriF_fcu0KAUMaTVG2ItKBXiG8be3ZsBbPHCGbV4nbmx3xA7REKNSj3uGDStjKbBeGEyk35LebSx1ZI3NXPQlrl-Yd-_29L_QAjkr1zeXacQCwyGco12E_1B7S_C2PHKCLilr1tUJG_6VUkeXm7W0SSrNVTwphdqkg5vApfbQa-yO9xfmZn4cibKvs4EJLds_Yl_OH-_oUK_SF3nCefYrvMtnJuVIc48PSISHqrKIg85RtzP1P6pUI-9RD5lA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Fxfpps3iKmSGYvcmrDA7zdnEYROxxHuLPMgAkl0czA3dhgFzWToZTaLYY0yed9AQJLd685VbDFn2vAmjT3yvYS6AcgKqeG-uTHN13ZvG8J7894hAHCHB1fP-YKiUGkwdM_EFnxlbOuQwejvOIV7lecT4kxtgAogmv5rV5vT2ppuKyAnQrL2wAQQSiAqzod6WPcWiPPHZRzUNqV6FjzeNeX3G5z4fys8fppzjl6ZvxisnScq1L3V08MaEkHPGwbsCKmnlCvZht7qwWlyMenzwTvF4621YeYgAiIp-0MwlSZAuIHRdQ7uxUEfvoJE7kQ4iAHgob0qz0ul-F4ojUi00iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Fxfpps3iKmSGYvcmrDA7zdnEYROxxHuLPMgAkl0czA3dhgFzWToZTaLYY0yed9AQJLd685VbDFn2vAmjT3yvYS6AcgKqeG-uTHN13ZvG8J7894hAHCHB1fP-YKiUGkwdM_EFnxlbOuQwejvOIV7lecT4kxtgAogmv5rV5vT2ppuKyAnQrL2wAQQSiAqzod6WPcWiPPHZRzUNqV6FjzeNeX3G5z4fys8fppzjl6ZvxisnScq1L3V08MaEkHPGwbsCKmnlCvZht7qwWlyMenzwTvF4621YeYgAiIp-0MwlSZAuIHRdQ7uxUEfvoJE7kQ4iAHgob0qz0ul-F4ojUi00iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDvrbKjFqYU7JT52UsTTyB4J8JJo6szxwwqFI4RBPKKF2LXHIQhDxnwT3-2ljAt_IhGHPU8NaSQPSRG6RD8y6M2x80DLHIbQPKTHECubXMkDBp7BKLUexqmiX8NXkFGf7qJTklrOaFY2ixsSKBtUyYxW_k_n0IfUn8RN50p9Po5DaQvGLuO4_xyW1HFVC-OjdYp6C8uMDPrFPajUcCtN087IaTNULm4uKFBz6V3i2lonnlyOWxC_Ya7U2ckfD8C7pwd2IEGa2TkyhnSy7uzKj1MN3Nrz7S8zZo3_4ENYKngD9rTR9mixnBe-rudBbeKagwkIgurb1NwhaeNGjM7ntA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCXA_aBp8hNJldbAzLdLUj05E_TNCVx-o_b2mrgTZUP2ZB3rrcyXSJMzvQxJjwhwzsEeW-GFlTML-EIc0YQd26QM9FTdGUOqsrBDREwWNPX51VUE9mcFbjwKLws0wHHg6o9_eUnTB1gccIpkeZ4o81h4K2G1WbFKXPOJyszDVK2Pprt4ZQ03ibaN4w9PNmeD4btm5m1UfQ8YvAahEfxHcwkmtJMmMz9gMjkZD7XsvOhVK0OIK3alP3HHX9hK0FZ3bfMdJYgtCxjxq9RMmzGN7-RA8rrDzJcYw3tkrJeqFvMHOvu85fWSh8pOIT6tkrtIv9hQcWPUpDPAD1HgCf-XoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-RJrX8s0zruOA0UYLHaCfZrsKIar2JYUpBA_OyRsat4h_JW8bQiyRz9JgZzSl0i6Yt9xOjiLE8Ae_YgSgkSbRhS9QejJHGTGnltOPgeJn1jGjPzgPdgtDi0vGh1iHEQopMTMx5GHAS2AU0hcvV0a0LqGRzt93_L70ZWufY1Z7fn07B2PDf1hyvOBXSgvq_QvoTCzjLfd9Ibjz7gXYim13aFn8Q36cSvIB77sjpdLFnRZyj7pW07mH04KlCG6YdniulUn1snvf8RBCWZCjn2mwM_jW0CiJEjOlU1dC3D0woMdQKpRFuFiBJQekRHSHfYuR5bhmKWJenKF0qroX9Miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKSKO4ToZH-GcwgP1K2bXEeRkerSrVLXZwDaJku6yTAM4PfqEpeP6eov5tbzJRTtb_MXFp825MVsrlY_QGiJMW4pP2E0icQ-P8My0F0hS02plM9IQ-1o-i8fhVhbWlnxID9G5mcL4rZfgRScYyfF9gZ-cQ-yrgal_eSNpl1TEuK4gF-kYnaZMWlDGps6yKW4ViVNiuBVpWjzIKJO7XjDENhlR_GPFg0UXP-SMhsFYHikkfkoMNMXSoGKShFqxl_7-xUXQyHZ-dXtfuSmAV7HO5yjOf_7fUrcH4kKtrGpKhjLdmGMT8DUKN_MWfbzSI0gLPloxSS92hzkE7hDz0tkUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLMvP-699F9JOZtDfkJblRV9wBwZKBsbKPRWilZazJkH1hCC6hg5UGrRX1uqY0l_258Cn8ssLz7nnvUT-xKmMWG7yyRTMedW_qXY_kbiBV9ojhnWqSwj16FYNxwqYHwJcuV8VLCJ-PcKpu6eYu5hxQx2Dia2o2Tgtl_XgFDIEG03Qm_lukwtLe-yRi4H7WvgsLLoGDodnbn-QVpGrwufFLAuiKFiBv5b9tXAAKq6LQaXPEvmsguBiblJmMjbNsEuYXviTdelm6K9EX0lsZ2f5FNfqUjHXr1gjqZ3d1h9o1Ym8SaJZRKZQ2dsKuCX4JvbFxEt5Tnz7cTHix-37b7_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dfa9viSMFkCVHSRTA-MWciiuXirih5ksfurfhNUuTV9kD_nb1KMlFoxdN4PGArTzIvFEsXNJ05vK55zM_XJGHfnE_bLZu_k-v-vXW-uE2qj_LMuOM3O_OxPchG5e1khs8B9G4iJaacIPfmywOVl0A58PScZIS443vbW8-g6BV9oG8MiQXvK0gaWYEMRWwJ4Tk-a_Gi2Jb-Q_2Crta-GTjGHPUKh1RL3_QNzvYM28DGiBf9HU8Ypfok7iAi0Re9pJ7QiVN5cFo18b6TsoWILfQWQ4Eq0Vh6tBNEaw5SRDO3VusjQQEjM_L_5an-NvKCZE72bRCyzI4d4_GleKtZ9t3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0pQ9MlBRcOhtT1ebgT2lgNIFxNVYBopny4ksDZt7mgWkQKLzEvwduXXE5efVj9xDhBjmihymIW46y-gLahGV01iqrPLhhl8cia6C1QMDIAumvtFEm6b9rU0_sTi0R-qzx485P6aZIgrcNWaaWSJtOnCNPMWG24GtUldRMg3s5v6luFuBBhOfSOvzfPc7pIEyW0XHJ79ILMsjxEQdbX1tZyiZ69-fdiPzFvxG8YnvWvxfRARdkhVWI2jAfzmzh-U98wUK5A6AllgSUUXFPakU02hdyq92wkKRg5coSQHjxUx7Y3UbVvqK1scHotcHH96BzC1aMEye_w284YSrQe5og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=albPVjwAaj0HituHxVEnM-sHBHxqbzm1aB8CcXgAuVG2xeZ1yGA1ReCpJW7EYOW7U0DDETnL9OvxGR5CY9adWdNHBmDBKLADbr75OpRZ7Vbx361Co9Pt5fC1TrIytroeLKx-_LFshFQU6MpqA3OU3EJQinhOcyusmgmKcB_H8pfWMKg3Q4WSfg5eobyn2nkxvqHq-STPDBWAH6UNiN5vvGcqTO1OO0ABJzuMQKaeoUi3-jG_P0wZdUtzf_zs7lNk2Nq3M_RBHSDUZql7UXPvAKAMXfv82Qp8zDDH55g91I-ZWT6PpVdRygY0Dgz71m0khHBZunTkWnYcqkzoHAc1a5_dctuVwHWe2fRF7o9IqB-1NHO9d7Sloy7B5RMAGm5EQkF-uAtgDO3FdLDfSC0bJ7860fI0OQcT5TAJGSIyyAJChH3-mOPt1oUNUSQ_e9vlHE2aCEKforAfivcOIG715L0zsRRMurgGPHszHJ7cmASJ25V1Pvi1RY3L-AWp1lRcsbh9s2TFdDcblloj_nwGsw7SadujBO1P7ieD8AuiGajpmP2M70PmkkjJs2U6bjbgfqDLuWzVVRMlZ-iLekzD5nvF0rzGIGkPP-APi6iOL_d-0MaVh4q3ZWrZxU8xF2bTZwXpCoK1YeTCRLEGAwK-Paz3itgqtUY1TP7SyOJ2QY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=albPVjwAaj0HituHxVEnM-sHBHxqbzm1aB8CcXgAuVG2xeZ1yGA1ReCpJW7EYOW7U0DDETnL9OvxGR5CY9adWdNHBmDBKLADbr75OpRZ7Vbx361Co9Pt5fC1TrIytroeLKx-_LFshFQU6MpqA3OU3EJQinhOcyusmgmKcB_H8pfWMKg3Q4WSfg5eobyn2nkxvqHq-STPDBWAH6UNiN5vvGcqTO1OO0ABJzuMQKaeoUi3-jG_P0wZdUtzf_zs7lNk2Nq3M_RBHSDUZql7UXPvAKAMXfv82Qp8zDDH55g91I-ZWT6PpVdRygY0Dgz71m0khHBZunTkWnYcqkzoHAc1a5_dctuVwHWe2fRF7o9IqB-1NHO9d7Sloy7B5RMAGm5EQkF-uAtgDO3FdLDfSC0bJ7860fI0OQcT5TAJGSIyyAJChH3-mOPt1oUNUSQ_e9vlHE2aCEKforAfivcOIG715L0zsRRMurgGPHszHJ7cmASJ25V1Pvi1RY3L-AWp1lRcsbh9s2TFdDcblloj_nwGsw7SadujBO1P7ieD8AuiGajpmP2M70PmkkjJs2U6bjbgfqDLuWzVVRMlZ-iLekzD5nvF0rzGIGkPP-APi6iOL_d-0MaVh4q3ZWrZxU8xF2bTZwXpCoK1YeTCRLEGAwK-Paz3itgqtUY1TP7SyOJ2QY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjeRiqO5ZqOnaW-PFfiP9X77Nw7JMwmeo-d7lnQNJVp0iO_FDuMQ8oQ21j3YEuAutA_U1P4ZJDjtS0hBVp3w89SeZY6hU_yWarVWdRPmsneM3IAkueNkv0UTNrZnmX2XbxDsTrYvxgMrvdDekG3EXUZuKX8rl37UpAC3FscXjQ6yhwjCfIeuxUPDSrRuFNbG-WU67AOFRatboorgrsBEgp6fsgk5t4bwIZgtL4hNMRxhcV4SwZPzGmKdlKOJL7YF8MZnV5MvJNX1OnOuO60moalO2d2Pug-x2N4sohQmdIrOXkmnCA-FPT-cy-qtnlvKGBZwIlTi_vQrk1mRFaNjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0dxSFmcrxIU_DpJvh9Q0Lx16xi0OMNmofJzKlPHYnp5BJd6q73co6wZx7WxCTKahCufLrqbhhBjrvrkwklZVPHbkTEvrAAahOTHohQWw7STWinmOLo11hQKsC2azJb6dBtq4-jccCgCeVHU2dWJ0ve09by-Z9ufq0ojKEihN5_RXRBk3fo7A8uvU871sfSX8ijI0xLIUN02YEP-93MDoldPJpUSQa8iPEY1xBqwUNtkYWlstjlRyS1ciRkS-d6xVEvUH5AMlaHAdTvGHBKxJklW7NpiZIbInLXvxYb9FPBHqrkMAm2vQGeCWoApR-B1aNtqvsU7gA9zmP5NnUbS-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lj-mY0RM3zW_9igh7tH8jM5g2mTAjmOlQH8eq71nhSS832ye2S8E0ArhLud_ia3ogKWlU1nzkVu5MVGhzel1srngcSqT7qn6p4OLM_5RQmzth-inJUZr2Jbf1nyHaiVnylmWNQ56pPyispLqWOWCJuDZV_qje2TqGMYuj67X2S_A_W02sjUI3f8uCTCxU7l7HeqH9LZRBjYonpjevgr5LLj6l-bEt5XYIXpP3HyWHyxced0mbe8aUz4aNmo4hWjoQ5v5w3o0QbXq8f_TABkI3UJ0G1hlxn3yJLeM6f77-J39-bbLotc5GIazvHwXZQN9MhrYN7rJzCizItqQDjgvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfXOan3i-DN2d2HoRpfc-4IKim4o7nvva8ZjKp5XmQfqoSic8TVCPZvc56hL7SLxAyOgyi4wL3r_2WWwD7K1IBd9htF8_OkrH8JQu9Q4wuobvcycZknyRsZ1SooEw53LajjSyEJjct-cvdF7BtfJfY_35DXJJ2HGqBs8AGQZMIVVCuXeg2BoCtft9BX5Gzmj01FjP0IdCS9HX4USo-nX6JpMLA44sQoLqSHfSoi92qpMKVlRYq-VYNVPKcFKtEtVIixvGzulhocjHbWFxsPDMBhhMteLaLzN2WCCXaNuE9CHLiiJ7TNEtsGDphNvEp8nXmqbyGTqIc3DbPdrI6j6dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCOuU9T_z0_bY_t15APeby-IEfIcVVLkH5jkw_0w2wcjT016tzvsyXRROGYqAfxABmYsKp-9jn7U_shkTuGs4mXXHf98KGj-trcYromaVWUTu5ZILoYy8zyx4nkjE3ov3MIC74N0VPczTrjmDCs5O_4KTxqtOPOabTgHCTh_D2Iq1LrbJIikoXYZzwFMqIZ594Q9ogYN0jjAWjbTh6xzcIOJairAtqPeqg-b4gUQolwRWzgl0Dv18foNefPvwm4p8eGIfHxRalgVadZCaJW6q3B6fd5ejs0uob18UDeaLr8LcyySrRYEi4Dra3dht54M490ZYiJI8vDfOVQYnQzqQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SjurHU7ttL0JbF2Y8hmnPfwYF_W-UM7nawDoIXy-t-49tA3c7FCCSkO67ONDRFXGNFFdSXrGFcgxGOA1L2TuE0ch3bjnaSMDddXreOEiCH-ikBh3ad-vfYj_DC2jPgS75ZrFEGoomxBVvZqp6WR0dbN6n27I935HSCxniAVCSoIeuhwwFz7LhZ-1xl6UaMYW5pWrETsFG7TUbXLn_cUPERbgW5SpvGCl7FEsRHLg7KoCjnxSqZnzkRfMwCditrqub2U-amV7Ff2WqSVw2QbQZalXeQcYOGr_XXrW5rr1XFcHJJjIl9kzZcwamrbGSstRrAQ-2Z-7Y37GTYWmEndvw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0SjurHU7ttL0JbF2Y8hmnPfwYF_W-UM7nawDoIXy-t-49tA3c7FCCSkO67ONDRFXGNFFdSXrGFcgxGOA1L2TuE0ch3bjnaSMDddXreOEiCH-ikBh3ad-vfYj_DC2jPgS75ZrFEGoomxBVvZqp6WR0dbN6n27I935HSCxniAVCSoIeuhwwFz7LhZ-1xl6UaMYW5pWrETsFG7TUbXLn_cUPERbgW5SpvGCl7FEsRHLg7KoCjnxSqZnzkRfMwCditrqub2U-amV7Ff2WqSVw2QbQZalXeQcYOGr_XXrW5rr1XFcHJJjIl9kzZcwamrbGSstRrAQ-2Z-7Y37GTYWmEndvw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7zpvenv5a0KSfDObIDF8lQv6h7HUocWAnstFTBj8ffyQ_dwZXchv9Bk--ZBVZKCqYdTKFxGwatvo5m7adETu57nr6H_bzYTIg_9h5syns2qzuZBR31QmoOQT4A-2y2BxoNgaRgrD785oQs8SbNqmhOHig5wRA_9nIoq2A0L2683HgEQiS1NBbPVPFEGxWMYsaqreExVkLvm7VuEjSAXpbeyK9f9doBPDiGu_eqrw8Se2NNMRV5fr09nGwhVrKYQGrjlAZSX-4hHSNqKsDo-TGsuU72piJPbeihIyCp4Y08cbZOEOoaKlk-hobjI-NOIBsX9nrjgpShMZNUfjdiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVuWK1CrkhEWEU2fLkWCjOW_ltgghy2_YbYL_xuWFQeDW_xQx_aHryTXGRe_MIDNbHsJt9W1ylSok9N8i6AFe4nNJXxK6wYx1jpibAFtPTT9Y6-Kj4OhaK-TfT7LHmeolftWEbEmIjH68MznQUw7TsHLRIB8U5LTDqK-l1kQ5-5uMP1BJ0IsGW-3Ll9KaIs4Ljaw_haQH_sT6tnjUsfQpJoD8EdUhsvFHiVurPgsBypUwekawf2UpNM1OV6UPL9hvpOUI-JobLHn-BE--62C2XBBtwiiz4aesGINYT9eNkL0QF1A2u60y_GdaHsGUGVCyfeLkvR7ocD7DtlVp8YAMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCR_U2Evw2_xB9b6U2HIyy9eaGIXphwO4x7o3QnMB5yxVx6tZMuBIbP_5ZKL5DOLqh1XSpxNF3gRf1r5cuNARB4qE_RDSxuI8dSxgSYK75ELfedOo3Sa4GLZ3xxvl5skLFGaPlRbZS3vIV_I02_udWHksp5fO1GNKFihofH1ZGW7xmNRizta0Tnf1XR3KTEsOd18Q4wIKmzkRCyrK7z2BYs6B6vu3_HS2MOywMFQFIfWgeZyYa1mbUsEaLpA_hmcnvxz3Thq-A6YC9z2EUw_zNkHX6So0V6g-Ukgv73UtdGm2a_ZUjNe-bghHAfCRLwx3XZI-DcT5VS5Uz9GYC93Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPf0bqsnAFuL50F-cFAXtIyIc4IPnTwd1i_6LRu6wWFVl76G9jZ8q-0swd7PvCc69QAN32cJxkuwO0eJOf2EGj-pWpmgW4JwBmt8hKG2E5qIYXqri35O7cxvZcK2dvy-ESViIuzA2wThLLMib8YGG7_bvn7Fx2WtHx_dLVmfb7IAzZve7EINEs-XjUDDE0vNEVgAbJkcl_Te9Vlt16yta1FgDX05JHrBhfwT8y9aLSAqwQrFkygQ1y3gQapzISbNLUXbCs_Jo2-ixmWwc9JOR5vmR-u306r-KLNhLGiWKGuDjzW7WIenwBKN--lnaQs-bQhBGxZn-K8Ry9zqQDGvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce9MSPvHgAayyZPgCpTy1XCaff85jd4GldW9KmVGFUdUSEtyQXV4HqESEcIMU-ewE-WmBQgx_or4CvqNhBwmtnhz-ZGMWoI7kTmUQUfCw6ap9nPg76PqWFh63dvtZy-xp_sDhqPnmTTE1Glca2Wl_zpcHaB9SRMy9sJVfbljRJWdFKMwsNrENtnvN5orZN014rHnWewZ53aQ4aWmyu4wW3zVAHQUUvf-O-aMFkEIc8diSkPkBYx7GbSM-Soli9gX20PWTD9qrHqFtF1T9NuvEOiZh1A0bO1E4NKoqAYGg3BfHeJ8ae3LnkKZZ-AhkVKFupwH74EMAX-WRFkriXG4qQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cip1OZ06cXxMXM8A2Mrz904TvSSsnFJlj3HQieCD3Mt3Km7hVxHYPTawptoEfhKBcElt6AuKMupFFT633DfTOztun8r2URSBWbTy3QnN2-StxzXh-CtRyhnqfcoOtQxOOgvgPzSiUAzhJP7W0M_XzXaLMANE6o25XGkvjPKx-Ym35iuo4tj9-PjqXlWjKTZQPA-Ma5GM_s54vWTnIeJ-mPqUCMM30-qQVDMNefCUIT5vWBoh_crvNhRAUSLqyVwYmCtbZyzaDyU36jc2ZdtjJI4FOcyxXgSt3oqluYdbk0JouFPN8PkpqfDW5d3av2mCsImekFs01acgTClFacstVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
