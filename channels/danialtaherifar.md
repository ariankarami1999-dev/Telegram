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
<img src="https://cdn4.telesco.pe/file/KB1AwuDIgmZJ2HFHAPlzl5DdHk3OgUVDyimsCxisT4AtHmhwimhtPy9-j3HmXOaBc4G8y7j4SbtQpJLkZXZxkD17RZ34xBFQlBx02td5To6Eg9GMTApoQQt-aTZb_9RKssgPzKSrQvqT2DWRkr-EWqm85XHJKQv758n_EbygAG7-a6rnCkQC2ch1jRMHhzqmq3KwbAS4NXqUaswumBuB3fTPU2xOrQhg9WcaqUZ0H69X9YEqHPlTUt2kNxd00YnscYDvc1iOGZLTynaBe3I6-6R-53X2gxjHa4nebe50ll8zIFQc9jD7dKQjJFI0VU_MAjIqT0hfr37p5zQU6QrCSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 316 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 483 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEGj1W6aim5Gn-y3O9pmwsGJXKv2sXtYdXJx8MUIEe3uiG41sZ9EfWnVCRks7B4ybhVfQye1b7HS1uYSisJ1AZ9ZlUEhuq7S7JFbrrOb60yePAdHd0E2MXRSpk_D8s5G9M50kVpiWpfi17NBzOjApkN3yO5pNc6Ug47QAO3TRcKtDUaUyFPgQ_96RdY_RkAFmgxvEjaC8sei3V00e-46Y4alUDQzES6Ky1j2E6G1ypTzO5c8l-kfft7lJX_3vaKx7pfhiOxjRK5dfNy_6aDVh7zXt7Bx9CptK0VfBBnDMvTQrmy2RtB6HswU45WfgKQJZ98Y_wGeb2oOy4grOTEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 843 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVQQjg8183iofZZk7NafWG3lkp8r3U7W1wkjFdiOjdDDaoaAUn6S_ol0WODVaW2tfGJBvPn4Te4ZNLNBraPwnMHkjO_T7ct3CD0rqhHIsygEyyL55TJc-DLZMv57AhCliV0FCvpP9N8M8Pl9Ls4IlZTPemvGcfnwSLeuZpMA8hOEOh_5_BcKKY4ItQqmKwcUEnKA8Po_EBR-Ss0igjCG2Xk2UpdrWWLhNeFdgLuuCph1LFuq6Pq5DB1YMAYo7IknEGqSfsK-zymtFlXcYuLnJnBr92KDXP_5KwUNihy-CAyrgL95sVn6p5lJnNbmVgnB2r0GEKyey67glwxrnY6c7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtZixY5cb5IBM6_bNozZ1jrS8Znv9u2B-xwllo7hk0nqKw3rxqyC5cjEczAoZCYPa_0PJDdq-tyWoMYtPZItrwQmayBmxMEh15q8_PWSBNPLzK2qgfxe1KasyOJZqKTpfh6UcjKCBpLOGNV6YoACs3rse-PjvIgJo0iVfNFOQtOazZ8S_29fPtjpoBEc2cQK-Os5IFP7nkEjejzeMmL3Ft7r2GAImxG-uCSjqjhL3T6NKANcM9Hhr0ggl5zc4ROT4d8pDJUF8s4wk--Fy-Z9qwKzgGS7VDm4ZhR-G99Fqu7wUFAasj9mCCrZWUkG2hnUQLYSJjUtnjzbbzzaIDQa8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEbxgikzVJJdRNOx-yzO3HYzIEz_Z336ti4k-KXbePEk5kOUK-GlyUqPFb-Uexgvl5cjbO6AJj8JO9TmQHvOVEeO-rfycdyQx5wjlR6D7jXfLOOy5HBhZ0WMztICwF1-JQgu8xB017gLbP9oiJa7pfeRgrurjgk74Mi70ZQX_ATVdLoMX6nDM_ODHZOrkqPHS7jAFlYz35c9-um5rBZZschDzod1TSLgvEV3x2pnrzQWC3wwLXe0EXomTy-sXMR1k14Cykb29296ZM7Mmg97pnyEglWPyoW96fs0kYgv39pdy5mvx5Ry3cn9qOiRnd8MOdhV373HeR9Pd5eaeAkuRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idCj1thljPFgUI9JJstkLOOknVhiuzAeAXpM-fNBFMW5wqtZZwnjdyjcX9Pr_r0CMG5c4M74r3nDRBoxBDGjeUoMug-365dZ3Ci15yZD8O-JZl5_4QxEmjvPV1-tu-KOlzyGu9q9SiLHLr2fdAOGhgQY4-WUaK05k_S0ZhummDrvu-tJDpLf7VfVgS9Q3-hwITYughnHHgkxyXub6msfz9PFTZ7Y4ma49MLu8tRWzaUgE7h9mhXciDDu2f2-dZy7PaR2iyt-k_tzD6fcfZcEf80iHs8NlI_6J4PV0cKIdBThYbNhYiOEulw-PeJnNUirrsGENFlrAxd5ekzx8nYv7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTKLFe6acW-9bSm-M_MksX0YhM_maNFFJcsHgINtGjVMzkQqBFQ9LIgydJA06iWOkk3qNv4u1fnjC8MnZhtlZcQk04Y5al06cTBOoDQKAEs1OQZ84JzR2ypnTqpGqPhqSdIMD2OYnAY-LcxMFkKyzmaks2RIvMimLo6Rrmt4KFR5mq6Cmj82RkXaOHtYnxEVeNkuxAtY-4rfHbhGZ2qQ_MV6lL4CMOXwI_1cq0X6WlDVCf6axZo0KNDxr0OScCmMMndKjdha30mfNI9cbgwQzLB31SZq9TgLJdTQokrbYcqiPIw0S8WMaR8lEtO2cOwdPcXOsPLTLr4P4y5NZZ-hxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcM971HB2PmKbo-zAuEm4eIjidZ_jVgSyiUBghPwDqHVyv1HBPUvUjnpO9hrkQomZAIurtTYiCZJWExEJxiwX0LgGZI7ifxcAMF3Xal0wS2p5RCzv6cdwcd1OcMEGX4Zr_fDRIDQ6P0eQTHE63IUzTDGsSuBl8QRl3N-j4vyabg15RmnNmqqqa-mEPwt4QjVQmcemfos97gBdYQB3oXA7CA5Z34KgMTl6qzu-WMfxbc188rDI9moKs5b75nK36pfDP2Hf0_pHeJSNeRBdwkT9SHBMgzkCD8-bJEbP57TbJi8a5fMuuGPCGeyhToG1j1RA8B-Um2HVyxm0q6Zn6lrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kutEWcMMWM6o8MehMzJZFQZ9MVTf_dBPTJ4-qPv9YkLzyb2izbI3qa878VO6arc_sltloLFjPcsCynY4fL3_Sa0yxr9s8ywjYQ3mEaNfHk9xUGFvmCBAMgBOudO2MIOzvQGcbMbaE9E-USc7ag9Jd_LLBRsLtFZdO6BznPUJ0Id8pA4RPT9AAMRAv3rX3MftY6TSkCU10JZr3LHG4xeTHtMepqwgT-JB2t6lVboHEX3QyQAIMgzw0TCAClwxmkdD8eE7W2KtnbIn-Gqi3ZoAdMp_2XflH8naX_iM6xA3KLjfXrpNsT4dJx9ru9EoEX6z9gA_DjEXCf4Ce_xpJFPDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM-bIxRN51bg_x7dexbmi5cL9l5u09Wams7IapYGhYYESPBynMiCpQiDDxaThJfP2niAuGjiN0KfqkC0Aci1HfNXSMF90h1ttGYkUrxFrrYOKG8TS5-1h5V-xjtxDAsGZwjveKNy7nhMPvZiS1fHycF48NBkI_T3rAozmMv4hF4NBVzofABqS9EU8kWN1Es5gX7yj-PptVXytt1uozUg_pjZZOghjs_oedge62wn10Kb3R_7znxHvyZ1VwOSC96L-bFHK_onFpzE3gu69DS5HKbIZy30xuJkmLplbQUnli5X7YP43zzqmjsE0PL0DR2Uj4H0WVC0HCWZxCdern5uBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fh5CAOEBheujQow6_fQz9B-3n9rmP9brz1nY-auA-b3NG6QQWM9bMtFz8bbdOVh_qv0CdMu6j6NZqOSS4Vvfw-9nWLp2xymKRvaITGQ0Pkvq8TuKVmcl6ie8Cc-Fv2OXJsFcTIZKxdSS_Yec82Fk9_i5-DFr10U7yh_5bsrKNFBhpuZtun-erxpfSrndA93PCD_bYt1k9FQtcj8TFzmgDx4GKbwl8C50maORLm9GgbtGuWMtdm4tHRzg6DOcxGRMCwjIW1FXwV8L7PSvaJmNh9C3GabyTwujkSwn_JJb5UtmS086IXBcKjpbeIqwd7jhMINj_6vt3oLwGxuV9j2z6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilhNnkZrLBiAC-XWYJPifmmEvoH4a5Orey3WyJ3BAIncQazoOAFG5KeRhIsynjE5J6c5FgGtH4vhN8oi6ldJt_HMsL1f8xyvefBprKNVmyFHodyXmK6mwyJdBGy3GuT1zkFj4F2bm49nzhyWacwyAC71qsTWa7A9evqmaRm4EnADHNskDzIkyvjLiU2KWpKnOzUVBa-aufZsg2_bjHwVJ-Q-TCBe5cW92RE5y3DRLdLRp-9PL8XzBHzhPj_lE7z1CJkSZPJkkBGitLbXFgYIewvY6u8DzhUzU-R6eYHTvI-mVvMezjSSC1SKCC4bJYqT3UQoxOO07v92a7X9I9LS0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=oJFT6uH_D8UiZJFIe9kfL4xjFVQdBN-mMv9NT0YOGoUkGobSQS_cxfKavA6ITv36u_CJFJHCXFfE6PkJALou6GXadH0S77E2-FXyuL6PJD6dQv-xZKehuHwX_Fxc7W9cEYT4Z2XhhelE1MgBPktQPTXjQCfGa2HQ1ik9T6wc84UNRj7UXniKV-Gs43u0QKQqJ2qodRMN-SniU8P2MBJgbsDkh3gx8hyArnDagGuaD8ZSpvoJ09VGVl-59NAUgZzBujTHjod2AmRpz_f_WPg63mUEKZQqwc2rZkAHcaggJnKlsQKlKmH-iPmKoXO7GtnMpnzDkMW6iwfSEaDuJ4fD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=oJFT6uH_D8UiZJFIe9kfL4xjFVQdBN-mMv9NT0YOGoUkGobSQS_cxfKavA6ITv36u_CJFJHCXFfE6PkJALou6GXadH0S77E2-FXyuL6PJD6dQv-xZKehuHwX_Fxc7W9cEYT4Z2XhhelE1MgBPktQPTXjQCfGa2HQ1ik9T6wc84UNRj7UXniKV-Gs43u0QKQqJ2qodRMN-SniU8P2MBJgbsDkh3gx8hyArnDagGuaD8ZSpvoJ09VGVl-59NAUgZzBujTHjod2AmRpz_f_WPg63mUEKZQqwc2rZkAHcaggJnKlsQKlKmH-iPmKoXO7GtnMpnzDkMW6iwfSEaDuJ4fD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY-ZV6YZ-Ixb6B-Uv1dZjVAtd5lG2_Yw-wsbSXQT078n6Sy03pVm7TrulZomfHhZd2G1QjohaxQa-IdxF_ZZ1l_GXAELtCrH1_pgYaSWawkPEGeyWGNQB7nsAKkCcRJNH5julPyH-WpIkmdhZC8Oodd-30NRqEnVmzg_6H5J1vwuHGxb3jRKKoM2IeU5VrX0XNGQgM5FHxjJrj0JmBS91FlP5iV3xmxo23Os812ibVQ73YDuxxhtqFrSP6G95DyBDpRUteZDJzMtCrWgFuPengbD4rIVvEouGu4qYSQ6K_NeHZj6RqCu_d4iDO8YlGlqTr3wGmVGi9qIJ4hVEtoeJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCuLXIyfl3y_LNJgLiJ7UIwq5RL6npYzSpn8s4-qR9wjYqHpsPXrkdtYgduapuEzgy3lSbq0ONfko2l8VPSh21LiF_tDt7s6r7rHrbyr-k6Jfo9NP28VjyeKyENQF0rQaLAUdcFfyzAq1uOot4a1XUSfgIXnKsrVzMcyT1XrMlcpu-DVHqYXqLY4KToXWCo4J3GQdUxsgx27JJG-XcIlgGSjkBw0Y7tEsrWDqxo8AnpTD7bbazig6E-xvhvLME7IMt2JRV7QS-QuK0If2X2rhPu65fr_QLGT1_ly3nsqzziTu9AyKk35S2JLh4jMSXjnFlpUyI4M_B92Xt9KV_Wgrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUw8K3vH8v4Jd_ws_T6lP0K24v8wmKYQt4KOcRzTPZWvoLNFlLbp-nAQ4rPBYSh2aWwTjgiowPzNiJE46RCMTUpqDds3Rnodj5rVW6_LCoea6-O4jTxpPVW6-e_Mdl74bpK9pmcuCLX9tWS4mkXZB8ZwPL4wnxYdMAw1CfNyjmVdjhBGnHOVS0_7JzymeRViMJJtBBsPEz7c39dVZ_fLwLRAmKVLpb_rgHcAy3Y7yyKr7RYaDRGwye4zGLPeMJ1owqfhNOFBX3fWGR3e64-vnFleQv7ziPgBhHdpLkR_-FFmxlBLobZO78plSEG-1ekkv4nKwFumebz6tQT_zLdNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKUmxB2FVtZY_2xpksjXeof41XPsCy3M0bJeRfhaaRtoHZ4cJCjdsiRHVEnMXGyE4wTKh3004j4ZwquTupfiOp8BGS7y5jL0S18TL9uYJi9pt9lh2qnKQx8y0dP7DXX3jq6c1NomVeFq3FkGh1XwM8Qrszh9qam9ykHsr-qHmGu--IpkPTAkDLTtfaOC1EJU9c_omV0fZui_sOhFijsyfu_paMse-kU_wqYs1AKAOnppbBYDGajue7Ao8MJC1PP9HQ7FsIK5wFEOw487eDWB7zkbBFE2rVfgMaVlsWrmTaCPFcX2ubF5UXnTMcLzlCnr4TDyHZKZSvXYPg7owZ0IIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmGS46azcjDCnuqS-MC82lVaWhkMCiTNNCFNt3227PZvOrgUd5v532Uic3HxtgRK8Y3oNm9jfQ78SJTD1eSCv-MALW9cLLTebBm3nfb5VUpWAGMC9JdlGMLRAeyCTl2eXEj2ZgN9Ah3DdN6xxI8bm2cYYQc6czdpfahTLpqwd5u3bOImjY_UBIJofvbIwl7kgrrt6xWfOoobI6-m_Cjtqj1T-JuaTjRjRdeikPXNNaDN5HlYZzg9YufBpW1MQVcLBXZbpZA4-NCea7M_-NC8LvcwGIhF9ci0Tr0TZbav2wXbJTNm86B86LNigWBIdFk1eji-aMjZI09Zf3p9ryII2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRINqdZZjmJke_d8Bv_-Npl8T9reIBxFH4qccMN-WS_ncLYxualPkIRcBSV_53XIofCpWq1VzUUUZVl9VvvQsTGN2MF7mGRbWpysjksYWDssMndO5yQW_ySvdhYfZSGDVQwx-PgxJA2CfusL3mCN1aEl1w-qtN69ibMP59tq_851GWcT1edwXtt7Yl3IG1TJWz64TSmYcU-nXgckLCXu_N3YvFGeSCgw2WXKqcNmDxVTGJOaLDxUtTT0DVI0uwYERNjRXyNkcP1fHt-UCRFvPpKEsJiVmyWVdywMVhyyVpWQojgbcYpG33VJsRbVaaVk1J3mHqj9fsYaCWZI7FMvtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRSR9yaFmxDC-3o3FVXpY6VprMWpsIdBD-zzTrQ0skXdTplxFcMIQcKd_pumP9H3Sk9rlnyGqXmDHM24ygNLiHA5d7yYm7ml0koLfSklGehqnJcr158M-LSt_ZXiOZqgxvZrzB1E5LCtGqrWYO13gh1rvndQWGAwpXnMPgzAZ4t2eqtprixUJDJ0AXKolbg8J8Hib5BTsOQItgT0ABX7_w_2OEqMqunXEkmhfkw2zxO8KDqGuyL8Wan8GQY2cg2nCycm9xVMPqcWiM1cUPLL-9ZLyFjc3UIpFl6orRAnbcIBNyqDxVDinlaw39wgBEqNFnEAUlFM9U8FjXldC4KYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flCyWYTo2BoVAPVj8cX0E_6vDoNxfu2FkshnNWoqgCp5XvuwYhI5EkizdQZVlTUtkzydS8piykR6LDWSBXggua4y0bfZl1Nd2InQH1y-IEi4aDncaNm_hUFjn73u4G9rF35zFzXcqVNHTQB6ZPTWee4SdFT4XeJt5Gil3gjHf8n1HBKdv-h9c199q9BdzGaSpaE4Lxlpx3x_FxLvYao0ZHD0YHytKxBk3KEansIj80mKdS3RwgUYagYK8UAiCgIX-rcaUwqPwWab3unn91HqJlZk5GdGEDJytAdoEa1TM2l1MZ5DPqBPmThdaysNg5W6SnxTE73Ty97vcKkHCvrvBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9V7lIhFxjc3mnMrrAGdR1xs0RXXrowIKheveMqvqk-YkhZrvuOS27he0wZhmQehdDcaio1LI-CrJJc0yT3Zrfm7mSjAzPw0uA7HN3om2JbNqmtaubt_uzwVWbOygDmlHVGEDhfgGLr8I9ggHpxGVxEcsgm00Q4Of5EBdq_xoAjTY9WLvvjvrZtn4-Wy6o4YQXVU0_ppEJPSHtJ2FyHXd3Cdgbjk9M2SmXJE4SvROO9ZZPQ3Vp5Z2v2Who7ccoVM6ZPIPKRilC4xs-n7kz9OFZsaq9GcitNCX9BzUuWvpHCFa3XFJFaa-5f2-WVx4Mo7jvBDnA3hbvjtZA4irkDsmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMhxjnhaaGe36J61Rs8SA5QH74jfZ_yfDCXbzsDEgk_-mVvDHVHtOAY1srcA2B81aOUiXQJiXyT3wwxtCylpefMWCiSpkVWkDHHOZrn10I2GGKA6qHMG9Ybvvnn-UevVNAI68ZDd-NwW6v2lOSE5NTUeh37DC29q01tF4Pu3SJ7Dt94amcPy-D-MgUSIkBPyKTHeOWQpqB2W_OeGh1y13mhSY2LhfHn0QFs7UghZT2TmM2T85e0HNbn73OBbBuuBcDZD55stNVIILPP104Rc-9fiaShtqsApXXtBrO8qbwvUpN8c9Lh__kntz6hnX-BUcj0v1AadZIMxcz3c1zKJQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6DN3mWad1lm2ve1dv1auPRHaR0xPr70qsQ85aCz_2-YUwW68GnSJzJLs5xtkGusSCDApxw3tjUXpRhCTysFP1x2pwDWtOOCU02VuIiezNsLkS4h969InUExvuBBWgho-7oh2_HIPQFegEL1L69CmO4rkzzYq3entu4Y0aqIEfYCIVWk9tkyvDHD8FRFpDXKQ_orFbdQOd--BO4cMzDLQi-kq8GL8b3uNctNX-YE-yKSVsosJgZRl-tUn42xq7cpz5VCtuL8dbX6n65SyLJGkYgtFiV5lGFsBZv6lmcRiOnWKDTbBZ9t50QSpnRLG5OlKCGvfybjiJJSUSi9iHH0fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiKr2OTO3X3xIWqCXwE9MQC4glnzlocFPt-FdtojnlmakdYdy4OWDNIc1wd2BlXBlONOMMzFszV-mv4N0G0HWSS9DYUteWoR86C2TmvLz_jSFiRJ6KVKVpLsw8WYvL3us9YufPLyWYD_O7NCWYZLcsOQ44z7Ots06ztPccbtIjwapHA85xBeWqrwNx1_k5nYFjeF_PJo4SLzGJmQWV5v0tDV0Lpe_5ik7tMdTBSVo3iYiTsqvOlKKQpCVBeJDgdehDr1DMz-QXxyvwrPPf-QpPdA8NmvMiivzDlBewlfv2NO9Ca96ugX1eLdxgfvlSFTWsKhUj-TVADsTdMAZKzNPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRjkdG2F1xZa766kudonSqfYwiHt2hdNNaFY8LpzFXTPCyq0X53sskeWjFwt4zryK4Ls7TmmcWwFy7W2cOu_FWnoC3bxV_sEEUaO_xSBcEmHaZLQjb0KiD1xOUPPtxvhDUV_B7UROB807rErSFokE99sZGIg3bUhVob-NTR-pKgX5AfAurkg2uYiJdwGtGVSP692wwPv1wHWhDgev29udx2C6hxkTErBGchAYhFKyyj3Jlc4mRaZjRkvOedOkhQRErUh4_krM7NBhYliIbDlR_qtR-BrSTbfkW1XdaYrya3dEAEfjh14ENA7xoyDx96JvoGOpR4jQvTiHBtBPmdjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSj3H-Vzf9Uya3BX1zFkb2TsGRR6pKrgpg2rLYGaD6WRF_N2IePVKJ4jHsLJXBNSeoN2O_A3GA-o7gurMFNBJcAvDQIm2G4TvRHZ75PR8DWFUb1Zr11bppt11HC-RkzgJyWrlHUdzlymKFMJdv20C4Kgk11NWL4Zip5wkNTiW77mhEL21ip73WO98sDkYU_5ConlgCCLqk1EoZkr9JQM7X6pAQgCNPtkNqutR4_lrTc6cEjv2iwogUD-fM_PiAjtMMLG5_cvVnc95XrXJhuMyLHkO9R59BDW6zvSX7ZKPAZr0COOuZA_Kypl_tNWyedLM30-Fv4rg0n1AFS31cDk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l055WTQoBuycg2NfpVubsBWJwjWaabyPEBZhmvrXxxvOFyLNEpUiJjw4-knGdOtJcojUpPbEHszZMBcNlfAeWflNIYfpPG1KnuYZEEcepo-bpZ6nKaliZ8vItJ5HdEMHywGU2gaPqrlQ087ea6pzCB4nSJOZgDuXZmKRgTh7C3Mq5HAMlx6VwZuCUE4Hn7-LerqpqRNwVef8mQDf8ibU09-9xkVqwJooi0rO5vpkIkI7y61mUOaac8LxLhZ6TMEBX8pzkDAKqRh4iEGl3bTwwLvhpl16nQZNV5gnVsxfqhXtsFf_pOfHzeIdCiu1OvP604gGOdATFNZGV9KlPiVrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_qtCJtFBxsoM9c6SnxHoZ9wSUFmBRr5t0ThuxF0gVvMbbtct57JHZKVCp_VOi5NLAb53kC4yLvZsX6M3l2Vkgj5SPlIuuArZl2NFoaMNh-9JH4JXArUj3SrjSkeCgLen5ve4ab4uaLVpcaQn9ERUQeI8kxgvwK9j47o4Gh_zAlJkRy5HYTd43k9nFL1a462o-W0lL6mfgBnRy2MzYkvOLfjgttxHOFLbKU0uR5kDFAW_k8p0xmKpxF6UYCZJr8ITyDPJ1Wyg-tCuv61gCQlWwPHSX1fVNQoa3gUj69ocjnpVD_HHcmlgb0lV97jjE-l52QbKAEV3CA9U4VJawRV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIc5Ibyay5CnRPKm_-Wkp5vQBI0MYZgvESN-feSQlyAFtpG0QBs1QSnVq2o-OHur8y1r73WsJySdVtQBpXl-45nQDsrgabCRkEHz2SJk9kYTDCbruyxpwXy5dPEhD-ngmzl5TMkfWARWd7zRsZ6mZ5GukQ4C7buHJWPxccAhx9Jj0MM0UqPyoeDIsW1IQpAHNIG23mO1ncmB6v2VHI6nwTW60fhHJBmeIMxHs6aWUKta6Arq_3tTP7xIVdkqq3MhiTLsKglT68gX9TZ4RMPys5DBRKEAQGVqZcIHFYFn48Ru1l7q61Q9o7pnlGKgQjOXxgFY3j-5RV2INJLpzwZN0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTE0SyFvCxA0U0vebKsrwCP3kAC7sKLOcoB_sMMPT9GSLpsFdECO_-UaQ3jE5_gMnvO3S6ATcCIxU3f16ioej8LxA7fGM7g5t9ud2g7VNkplr-mgo_KiBFO8Io1hNud-kitzkLsOlGDtzpce3uyG4eNdnsJDbbo7_uAWAm3JZQqD7j97sztaVxZ0BuVdsABLc1mjIIepegi5x4Q9iZfrDpGZh4jGAR4wuHaG5h6ULj0laPOS0oVZY6SL_BBbZixLNQZtMWawB3VNpG5QZr7EosloY7wHXeo6jiAIGX_W0VJ9bMzu6DTOcrDWzONXvtHEjjoXrZPj5MCKbwljoCD4IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVVbMY9t8ErwH-FG1Pr9CLHQ4TeMVWCKFz3U-A-qrTLDLeoZPPJYpZMM-iHaM5ougSUbM8WouTI27y62OJ1zlRVATFNS2tlmWt5wV8VcaXf-CxKT-FRU495pzVnKSYoYE26iCo-vjWMjar5Qj9tvHvfvjKBuFJ4Fl56eS8rUyh5zlxUS5ZZwtBhcB7f_gzekYtU-eTPM-yYYvF-fxRrfN2oqMlU8NdX-TYCw0xoWdpvtQzoj57mXP4Nl5y3lf7_GZuz7JKTVthXD8kUHHxSO4wdIAfqOjgMA3WcE8yPBRX77CkC-w5OMUJZLI8PZEnlFYsP6qhs37fhKZU9Ha7bNbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqS9ynB8RfteFwdEARML0OS6j7zD06O2zcPIzNrjmlBFnCBqSU_JVUHoUKblLJGh8fVcmPHE1XC_CrfWRY0q5Zl64cI5gfTd76IJOjVHCNQW82ysdYQnbHMdkFGWi1lfMUJwB7S9gqzHvoS55-yoJttPsBdhyRJrgJN8ogSjg75bYCCYTGp3xFR68vSsq7mqKvbpANhe-ooqW0gT6WuyfNltOS8nUJkSpdgyD9u0jxsJl7Oj7oxkjugGIqYe0eUiuHzLinDcSZmqE4to6-03G6Mzd67WmaVqlXq0SRko5LkolTjeoJANUphyPkkdni_5BrZFFzBVoxaOSBtxuUcBPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb-zTo9aEi_qliKZHdMj07mZvvyx8CQI80qVj3VnBZO2FyuLRiOnHrJQO4xyXFBjb2xBImykgqeGsQeYbHtw-tQ9vrszvL0VLINMWHlTFjqEeMJ79-CEzGLTKvx7OgvvFlwJC6_cmCGcIG44I71tdOabH25H7gJNG7XzQKWTd2Gu5amW0NvQ8CZlmwzOMuTfBDjAWufjYJ8T4-nW2PD3ATtxkItmFVl9swyWq3UGRODKFrtjYtynCuM-mRvwrWMShOsCBMuhDAHNJntcYR1pH_UTyan2Najx8LQFj06BExuBsVFTAi0n8f-ialHgMn73EGhs_96iMG6veHAzOkGH3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmTMbjM1KZcfmJVAJkGmo99rb_0y9DZuDnyFeRhTl9MI1rzsSunBqSUU8SmnPDwHX-9nmCegJ8HokJtuZgKV17M8mJksR_P4ZsRRwmZwRcFszyC4FeThfYJHH1eS1Q0-kLgCQiftCfbZMYRi54PcEhoHqBUegs84lPkKiGA5iuzfP43zr7_uwvLW9E3yy4QFZmmKjhPbifL9lARdsOXwZOmAXwfcV3BSgAGDn6WD9bZxp8SyqLshN6YXd3UO91-MSHAqlCMH-fLqChLBarBbasDG5dNuvRKflhKk8nNy04B_sFEXfIwbdFSFn4OXMuFtQ7i0qvFF_IyBIZ3mme6r0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssw3JllL5yrXMlO5jimPNCcQ_aNTMYgZsb-UrGQUV4ZKfZZaNbQz6igaBDJwqVpa5F0dkBgGx7ONMcENO7L7VydQU1CLqNGGIahPQiLNmDrhWPzvXyOGdWXu8aB_p_SziOfhyF8wWyGndhEM0WJRFwiQbaSN4xPCyH_PgEsf4ntRQqKiH6ungSWSprsRctxFNFtgJLDviQTjtPpAZ8ufSJGoIs7G6z0C1JIfexpN1KgkkUr2aNTs82ZW_RjKoJPCd0NtX_HeVwuiCuO3kU23UtoDxrIZS6DkFMH-TVlZKDriwaFvvpO1p8u51l2TALyHsiWE_BEeJ_TKWjBv0xgybw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdyYO8X8rKyp6wQA9PEeNCXAB6D5aqFOQk-JRUZZNjGhW_5mBs9lem5icUDdeSAEyJ1OcIplyb7mgNRMD_NX1JfiSAplvLemTrHJE4vSiln-xl4td-MNqqxwmv6BQ0Kt0caFcK3A7y3DJJBAnLuUkzkdJbHNe34t4_-D-WqLBprHXOLDmmYffdD-Uh6McVE9-5x3Q3xJjqebWHh0dmAl-PDMf6CJDw84sGQFdmc3-kar4HCykF-TOy9pMmKECUYktgxPKi4Q-1lEMNb9GwyFfQ44iEVx7tOw2UIqFKZ5wc63O2ws_QJsrvgS6tL9D1fXRmN5G6eWoH9Twd-CBQ1vtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6PU8hROg1hVvW7cMeLfBMyqySBI_vRi06TVHNMqh51_rOZSzpXuKxtvxtOzkN4VC_O4gof9LHwfBW7qADL0OqPHy6yRRR0He16S9KHYfgJAAAHfvGRDb15WOluKZ-JgSu3ainvOiHjqgJn5cTtLFn914Rn8upj9FWFdf0KL0jyuUbhWw4_4wAXtjAnvNtb1J_nR2p89Pd4cvU3wRpOEsj-C6oe0E_mvr_UltzfdsVqBvVPCyhvPJZ0A-saSUawmNc014euVmCiTLnAV3K8giFVG9ihmXyYeVA7cGvtW37vZuHm9WfriMj-zdvwzMFmKNppwat74QqDeacNSz7boCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HozKQTiUx3p8k6SIfwAxQbK56L57DkTKsteo7ziGYkGuhILpRwhFNC-737G1-6T96h4k6DnAzP3VrflnG2OjRCHv101VU50qUmrpFXd2Oqc3LTGtyipvGgO9OOIqS6RfufDQvr6PhOM1kVxUYhPMAoHedGmJ0gzLBr3rQPNGDRBYR2-Sq9Xs9Cj7qYnbvwuGcoKW4p5ixyJBzldGq3ROy1FQ-Pvd-05z9qjMAq14pCRu1WqZdGYRfUeuH9lf8pFMTISX7ZqzY57AJQQFzoFiem3vLFGoWySeITr2tt0pBHxZ7OBvBh6eJSKFTvSEaQy_ZwPwmpuXFDbIAnGCSwCGMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8cpG-ELaXRTJCQ7TDlMKWRX0tALbCtbznZr4slneA5nFH4jv9dpmpSgGzSiCOVEet9cUbHqj9fsurSBIZyNMbqdXo5-8s99UESmHdqoesQXC5xmo2SNFGXCaY88gnuA2Bh_2Yd3RlbMDH-59JSGg2Et5jaEx9eEpv4lX1iSY8jHrVfslx4dPzMqtnvsFJfsJXtn222-sE0-a9jm5tfakJaQdB2j0gqEwt-KAB_9l5st2kJKACLIpJnsk9ZoCyFOTnZpAgYo8HZHc7w_AAUvBqba5OcyHbvGsH7DkOaCGj7tT9PAW6dEqe7uUDPbkc3pf-eDhNV9_HDlrz3jKeYSVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhSputE5GZpUkXENUjDzTGGJ0PhZzQMcWjU1QxIJrMffWCGIrd1gjEYmRjRlScDNjr0zTLT1LcTC63U6o81l5YeZgAWMKzr3QzpG-4iyFybsGKu0j9KH8hnUyqV2Cb2Co8tCnuzBQBwfwHR6RBsP_ePnG9z5lzRreZx5hy4k56NR94teRSOtypGDSK23G7Uy83PsCwugi_CzjT7Pwo8sPX2Ups1LAx_aPm7FTUzzEALw_oRUA5CvF5zitGE8TlkEsKoSnyvGf7gpBuzMcYWvMzw1rCEQ_4kDAdsHPXnepfxwh5wQvifOUbwKitbfMX1M0vg8PNwv1_-r8OLJT5Ckbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOmBmKj-b6-VEFCtDKI29r1Oc1S6m1jXGXwT9TrZV0nwuiWAPy4TfTV4JMx_C_8o8vM8_1xj0xWC0-mJ_UEGj42S8VhGRTQ1h_jP7mSma7MjcwCRRd5dvklcOYHL4gz3r4IS1Vryz8HHqPpaXLHy6_e8IKgUdPwJDdSgM1m-1SLn_PuXlt9Yp3oU_YAS1LHUb8_hT6AciHIY-rwd2N5B3rDDPdl78KZKTC65q_7XN7xv8lxo35rh6tn1Myn2F3rQtc2KutAD_6kjxv2YkBrXAf1pVgxJySvQdTZ6ictw-1KPEUQlp2t4rZwaEmSCm3WqZXzi2XRYvX7qtXfdNFL7tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNyy5CE_JQ3OOnRj_26PKBW25y1G0xkiOnr01WxCrX-Reu8pKC5oGKasuFsaGEQXZlJlTAg5aThgtitJ8IoxGywrTTY_smzp80WqE7KfpkJj1QOkW_B47okibrc2kHhgmidzcobgldkcFemiNUu5YP_FpPpm7ZyhdR0lAX82qA_XVWFsUNQyFjWusPVPRtxpX-j6ndxrVxjqinkbGfjuYjM9rhGnvP-TivYM5o7-8jl7maanZ873pwfYU53bK36WYL0rROBV0OWA4Z4fll6IBWKJag_nECxhAtgP2p4L9A4kba9IaESuV1bBJ_t8Yc9dyboDE8kjwcMjBHbzrc1mmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVwhpXD1qHNYJUFLjI5X9wZhBCSuuinLs4NTCOAU-rPzOeL_XgU6Suo4Zp1ENypDAnoxZgblQ4Fwt13xWP8F2zjC1Pal1g_Mo6HZzquQuh9ZxkzVwHmdl0Lq116XXOo6FVOffrNnJU1M-5lAmfNl-hALk4xCadNhiLFHCwF-FVd4jaFvJjIcMzFU9JIlgm21-9lzp4rZQGny2Hh84tZMBmoIhIsZukXxJdU3FqoW7QNrSmtQvSj7PYTBMZ9OnX01nnY0-KovrHKfJl9w8f2Dl_EXBUd_QtWcu3tHkgomzuwLaC9d3jG3pvRczqzdTlnp8qoRbis3AjVjvoV5wtH-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4sbuutrojAGK4EOafukeZHmMTLIg0pwo9Vsg2soSFoJdJ_79PmaaKMN8s4-w8OHIaDKs7CRVuE5OranUJD9uLOZaIo0X_n_nVOp_F-Bj4P_tiunL7NBnS-ShYvMrG4r1xfwS_uaQX577J0AYqPZxxHct3kYBnDuBJY8HNux8gSlpFl3VVbNlerJySWv3VPrJrzCCi5NY7eE5uXVRGgJBXSiaCmxnvEPdI4Fijme3_fwqxFM-6IuM2lR1Ho--jPQSkEWJkvLQ9qQWEr5RJ_upNruSwrEqHtxcvpBU7WSXCyEcXl_GA4v6B_w9fymTiARXioB8X-kAy89s4QwXeAziw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kV2PBw5p7eyPM-6a1w9v5235gdzHRd7by-bpUZ961_wXtOvORwFAIm4vv0JXTF5RuH5uU68-l2SYgCR0nGLNeOXnYcJLw515880cngjB6UsXCnR-154mZeO6ISsuK6t6kLMCDo3lZv_SJ-ipTTaOQxzbbNR5XuwPOZ3dyCNgoPyGyiBM-hqwLpOd4PMdf7jjOPuPL4QzVrzPp0wquBwhpdl4qOpITzQC2WTXc-NtIk5RD0IhKGjyIdYbB87NbLsqcCnFQ4_Nt3Qbu2dsszr4oqZfrh_vSCoJOjYbU34LMa6VLphMscw_9BOoTlzzw-KTxBSLdd9ATSBqqfHgwg30qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9sBszA6VGzpI25gbd-qK5p6cKr_nGJptL_Pyus8fgT4nob4bG8Ub3bGxMVzhUlvMWRCgQJraypeDuvzWI9VL-DLEQT4ZH1TQ__7yNTQSBq8lbBtbl7suheWfZysPILyOv11GHEUA5vcBY5reXEkJgP2bGxL4iYfir-vARc-KkCb8uZX9mF7RGhdW0T4CPlnI2tw8lrohq0aoayjGBjUGe0XUufa8gRI5Fo287OfMrxpFKLHVCos52vO9oxsbOlZLkjJJwb9sg3y9CN7oNZJzzqbxV8mVhpQKt7Pgc0XZsv8A0VeLLsTyECGsAdlTBXu3AsO_T3NC4VWw3eR0oRYbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZw5KrFQVNC8qjZ9elsgkPrGfyo6e8GUu1P9u_5PgtSIbu9fbXT8_Y79s6ECNASuAxrlvfTy2LtNPUZIsnqnUJF9YwZ4mbnHGI3t-FjoLle1B26D3CX1dIceHRKvoIDH2LDeyvnALVirTvbjiZKuMSr_iirSjq9I2GIvioYevAo7Ez_94gt2mt4n3C0ZTl98UWe8D0VAFvaGuHhUkr2izn-7PA10upazmpYQwrf0mmzV7WEFICIuNnKZKw3488DqGoKJ6S6Tle2rrEQIjzOUDkbq8prbBXQQudAQvAzhfAIeVexMfgNTZHXrYuMYfDfERgEnHIvQPd3E9Jy1p1y21g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFXnY2eZlh7CMin4sXkuDQYTBURhGnWzvfJcvctkd8MBdrryW9HAas3VgNLYrH62bKW6SsJhGIw4xmTssGKE3QZ_qLfiLownkDbugLa9pn-K9h10g5om-ELclnOyrHFjXdoflhCeHsAjV6Tbr9JcSN8yXNcdKeayEI5Q9GzqPatWCBSgh8O6HuV11sPyqEfT-UddBM7_1Gl6Zb_yCK_xYY-DF8eQ1o1DLPpkHVFvuzLleA1p8jnL6VyMl13PTd0aVL7GBWJkk2Wu-Mi4gHoDDabXBnqKW3NcPXSaoM0ejYb2c_s9hEwP_ixwxckvuk5avQiemndSudlNtSgdrUaBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiQ44F2-_bXmkuGLgYLvtpnLsiy_DdGW2d24x5SU2ninrPXUp64wsiWMLTedTmtosxprVnZvrvL1YORY_PMRYJC05DbcRNpRgskUWobdrtwuQlcmFmKahsRwn6SeRFGhC98f2nkiK-K330aQLorXDV9cN3uhPbR6ehDiRCjHAVAsrSuKJU3Q6Cfc_GeJKMNEQAArEPhJ5fzfmWje7px98-R5E-mLTv1yWJdd1rHQV-gzOCc2meHLu-DTUdamlvI07KFW-4WEylcey0gE63wDFDfD_rhZoI50K9QDFD4Ej41Os6d97yooCn7ztF62WQdOaxLughLj2tF5LvryMd5SHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6NP0N3NU4ziLaka7PRwK4AyZSk2LmrYGLY0kgJ3GAnH6-IKzvI5IRZ6MfgNL7JSO0DfmLCo6h8XA26ooXQBx6cGGRnm9PiTf1FTBKPX8p4F9yCr8TzTbgBKVWCwIL2eqPQmKMqpayKaBukYyrK8XQ-nNQKFI357bMak7XRYQ2O6PBvoxljJqe7ecPLzMKrVGHW1sI6DwGiAMmWKuVCJ45yoWfPtHOfn_aL6knsGAjq4DcvFl2UyPVco1pjNlNaiLGPEyh0VPUTfulmX19MgVPpGwbCZHW4fRuZXybVQ81610KtylL2Zsxqo4kp44axad914rFT7mfkmo-QquHtvIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh6BBnUBepIGbeU-dVrhCgx9go0x5YI_l1m-TlLocYoXFT0DjTpBZl1-lOKv2vpj4ybL9Syet8i0n5ZY9fSUy5NfiYYSgG3XP7GNdd0r2bxXdI9vl3i6BagcKf60XFH9rLECcENZAmOMQqaolXmEO_YDVOA0FhQSDFAd0ZXo8s_08u4ZPLkpQ0hul6xzxlyoi98uCL7wSFGj9EQFVuJADs8xPdoQrLmlEKsd57b-4L1w9qquEtc6A33E2-R2Gy4Fpn6SoqK7PDYIY8d6lPhg6oWk9mxeZXqsRovafNf_8h_eEwhVaOsPxZuYguQkJQUyg8i1TBdS_NTMZY8TB2AeHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUvXcBHba5wf2AUQaj5bfvWbqyNHZCtl8ksYxH3yusVLtSYM65BTobGNW_inM0P6jz5lTWriJUMay6TDJLHGxhqwaELZ_g4ZwgUg5_hKj4ufHSSVQgoOFqUr3DIHpoE9Jjtb2iOpdmO2bpbE_gl_LGYg7KmbKWJNwsAS2A6-jfNMsI31V0z--62kMLAzpNXum3Duz3Lvmcfcz5qRvHzYcX3B3vu8EJxjzzAITV_vEW_Euma3fSmOY-CHEAjWMUdlgHFjQqL_Z4xOENhUh7gCWEjn3eMEBm5kkkGXrnwCvw_-lD2TANmoi0_8qG4tsCMiEDa4_8UeTTrxfuAOf7qf1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzH-AheegDi7ynA4b-IEtoJCDnm0G6jASB5wY7UJk2LzldZonRtjuRbUGefTCXK-YqK7w2DnWBc9BO8GEqzp7JPEWervPPFyCcfwf3Jpf4TQtEgf8qhoaK7NDz_TfPscImiJ1Mir0H2evzbV1U8kudpqORKGp1EY3YRnf8QpPukc07pysvMOBK7uxk_JKJnVUiQXnNLrWITd24chLczd31qibre1CByQtsVnyEV8F1pui3kXb95uiZPWve1BJPlSqhFw1ZA19vTHzjFL5ljn1mQdVTfxuy3jJnP73p-aqrC790l-_95rgUbWwIHBpQCozIywqEtjMax1fFpf76rIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sh81c8EeRgWicFWPvO_HHoN4Yz7YbEWgvElHdyIaEzIdSHG3vj1JT8ToNKfzEr0CekBWNOBg8B7gyT3jZICn_WLaC1xv1fUQOdOncbzdlptVWGAMQyisSA_u3rGV5OEpTcpS-QLtCGXmKYeV8fI7QDt9VrgJbT9ArV_lFwZ1qJHCIpe_JWmQoUNCHOSGKDvwrd0DAj-9YYslLGjzyVQySsLvcnVhYerU7iyYBTKSmtM_YiLXfvWT7H7nds71ucSzkdCeWUQQlMd3XP8VdzqQ3MFgPu1rb4VQ51mzDgyEpwbb0zDhN87UBDGhViFC14msmD3skI1aVuLroPhNhoJDMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCf7xgVfOd4YnK_h_YXNHs2tVpkiciLceJui4Eza_LYNJq2uPTISaAtUw_zLvS-oCNuCXiEWH4OqU8K23EOLLh5R8dWRXtfP-7UwV9Sbe-4dlJ0H2HMRGIs4D-UrNsddLs-osZA6Gr8x8lq5dNcok3SKrIMtBAvNuzTE6EOLGpyqN3MqYwvHcDuUXSy5Fg0w5-1qhUICTKfxmckC6HFF8LGgGfIXJrx9-1W2RTSk6B9YkXk8t5JxLOXSlQPQkmmvgJET1bZmiBZzh7s6GIxkBgNjwxgHVqOaLK1JKcn7o9pw4E2yL3DX5PvoiDkR-TBMLWry8kdACuuKiihSGZvEqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4D-EyVsl__pLY4-65dyQes_6RuBIcvz-ux5du-Bq5PZAEfNQ8PxJTIgwzYOh6PrNsayM7gBz4HhtvxAyML3W4SlOQO_8i8i1u7qAhChca9Bbet-rqzZ-O05_R-9aIux9gObk1ORIQYSH1fQwoC8N_gIlBNeGh4Cf9TdPPefnO8T5qcXtzNrPGku4iW9ohaRhYQbdm6jKl2Qrqz_Fg1lJOlyoRA6aoMjJ3YJHdyobLN9VKAbRxYrk5bySd_KKPn1-id2P15Lshh77s4lPRP_9zqYY5XbgNO-UjAicgc2EnNoQM86ZyJLG_43C7dva2z48bYBC25Ava1N2Ep6sM_6mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTOf309A3wvRAC2W5qWhDfvhVTEcYUZ_CzhBgmI9b-fhoTmCtWb_XIhh-wjc0sogP4gEgRjFll9dbZJGiKXAm2KzeSq13XYu4pgVY17IuQJE3ayHgZPBodgtZiE8j2FCXSEMCK6Rb2HhiDqZs7vRNJm5L_uHzq6MniMH_1o0Ld3U1ak-Tl2FOLOAy9BzuZKAVnYl7Agyn_PXemczwTdAOLGVkZD5o-hO8pk8FOZzhXMMkVJbSTrl3NGgaeLBuu2fAGpkp6pXYvfyMz32R7Lq_lTE0vyTZYLM3WTS8afWKdCIOUBqmL76F6cfV1J9XK1XHPbJ3CizOvituRuZB1uFvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZEH3Zg_Z5ydSxdxc08djrh2GCcLC351U5lCZ_hrJXgqL73a40nZIq7FB2UamsZQVb5Xw-cg9fr4AwtfArR90NAhSqrXp2TjaVJ2E9ypAhgrUOwqKzVWUqw7XtXDUwZw9q6lWhLU3qQRXmRzyhwlxwQiO_cw4HJj5pPyuXGo2h1y6TeVaDibLYQyp5X493LDbt0KpBXPT6VKdeDMnPGHcvYRYZi20cc5hGJAwn6ZK6D2vvZrNkVJiLjMHV7tuiH_IAFykVN0mikoawZPkx1BW6rNVUT707nv7rNyVx7_xmkI5MDJ5H0wayEyAJgjBd0MXTLpsqKUlFCdDKBniyo1Ew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=c5hYagFvgCh9MsYldOjxlN4dQJCmfyhnKvEZ_dt__BcKcUX3BcPOa9yYbVX2QxxM7jlKLz5KB0B8DTfsVcimudKaBqyzBml2cLhAKTo7-9oyrbJgJa9xIUk6Q1N7-BW-rzTjO_MmvAOmKzcLojdrLDK1r6jwxnOeIfnXpfoVc5if4DoLF9EpvCimf6v2c3qh_yxNDl30t0uDamgNdS7qy2EVeiyg-i02RwZO4ozHc5vEVqsardfqTIJcN14fW7oZhIhlH07g-S6XzTSPtD_Z4_3P-4IguyhMG0MDgzbP4IwWahKbAEhhTcOXqXmACBOf-mXwFJwVWPCiPkmcsU89wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=c5hYagFvgCh9MsYldOjxlN4dQJCmfyhnKvEZ_dt__BcKcUX3BcPOa9yYbVX2QxxM7jlKLz5KB0B8DTfsVcimudKaBqyzBml2cLhAKTo7-9oyrbJgJa9xIUk6Q1N7-BW-rzTjO_MmvAOmKzcLojdrLDK1r6jwxnOeIfnXpfoVc5if4DoLF9EpvCimf6v2c3qh_yxNDl30t0uDamgNdS7qy2EVeiyg-i02RwZO4ozHc5vEVqsardfqTIJcN14fW7oZhIhlH07g-S6XzTSPtD_Z4_3P-4IguyhMG0MDgzbP4IwWahKbAEhhTcOXqXmACBOf-mXwFJwVWPCiPkmcsU89wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbV9v8rwFWFzGqO1qXnagolN1kMihIf8Nq8-MKPPY-9zTO78qzVqb5YYhXqc20JacIrkIMrGNVgmh1-K7CTO0zZNZXGNDHruk-Ph2-WEy1tAuodqHo2IczOt0T5Zfmgu7ROEZ1v8LMGmWIdhIoYMcVc4-aXIcO7sepSz85MzGzH7BtqR8SnuL6iD3nt5OGSfQFrAc2_XCvnZDzofzbYJS7BA-JbG7diAJ_kzFLy8ikUahzLc_gLGq-773TEzCUxfeCyAzHnZw_If6iw7SsW0FUJTCmodhUfaNRqLGDelOWbT-dYOwoWHKpL3bHak-F0M393NL7QwewaVo5KFMXozLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_UaI-WLjcux9rZjxF5lGR392x0a3WyU8OlUQg2j7mVIhgNhIfii_ZbHSysHSo_2zWjh2U8Jkj_WCGQc1dX1v-3qHP6DWtmRfnlnsh4FZrG8cg062S1Fe7zWu_T5r4ju8MNh3b2plqXKLzFh0fiecA1NZhI_wI_Kf4hfgtV14cvXF7rv89S8GvBgB93N7IPzfaNVl9gcI0HlSIlUVn7kL98sjU4SJvgQ9VBn2n00noJN5bq7Wf4DDmSxWXQp3VwGfl5_KLKHcuDQE_wQGztXk8mxlnirQ9EPHDJfWt2zZJNTrRHEtOVB6naXEH2qib3wjgm88R9S5aGDxE3SlGdrlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDdMV4ctzIC0YG5KrcYAnn-xt58Fx9ONL1EpY_enMNxxVjD__ZTQiKfuaoYvPaPEcZDEtQW9FcyVjl0WCDq1iBY7mdiKrm-thJjRmTNBEvT9F1qARfDETXg5t6IuIsnpwS5tAwQD_THSJnDwqXX2f0spO8ZlaPwKshTC5sdTevtGybcUV8gMqWs3Sz1ljBh1yKr-RWY6mfx7TVSxvolkUioLhW9JWH8wAnfEcoU9rhyQXzQKkSlN75eftkRo-G0XuHArgS_G6-0nbYW1s6kKzG3kUNSPT3NqgjjowF0AuIThLKZfCrEgs1vtBnaxb6VGKxNEBZcE3DDSFuP4wQsIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urPRp6pnCa1algnTr3NBQjKzi5JhOJHa1vpB5LBC8YB_R_tcz2iUFiRV6AjcrnK6YvBVVggb08Oad_ZlK67cEIgvIZdW2vRfgn8XLjeKcojeNPCl5AJDn2h7nHDEXXX8xHi5WeIvIV6AYfw1vRKLQzLuQ8yAK4F2wO_FSY4AdPQiS1u0eRbfi9pIr4tq7czMJazyqElTjgqpVkblbqDQea-CqiqDu6JNQzZ_mU_hBPpqHZZkkDmU9ETEDhlxcb3Znnv5klvdjUVmmaF-nAUhEYGLI3QyD6Bt3EIE25pzfGmltRlnzHwzw9pvky2bewcQqjvhDLjzdfx1rywpje7Qpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bhs4RU7BuPDTQcYRcpxXPCIFGmNGBEM9NPqojMUbauqj71hNfr6hKj-DrAyYQxpvQZET00Msozk7LL5-QrWeFVptVOtvrz1L8UyTtk8-2wBW3zN5Ugd66Kau90RfbHck3Msvu8IyPnvgBxuNOphvNWka_ZQwp4Kt0vbALq9itMmJClsDmS0joVqcnoaRt7g-yR4rQjHPTBFWIuUD1gC8NoObBYMmb0gQO3-No8PbHFLIy_pXiSYl5TtmpN-vaiLKhG4PQc1712-kxHkiz7A5iQ61hYDvOhdIZwPVrw4FzqTBGpTIyAhmXYBjtbU0FS6fED5tYigE5h2VAdr58hteJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geOHA3H00qHDOW73RLsZzh2HpR1E_8FcZD5kqs--UlCkQHUiAwauqwglxaB-tFJMGF5--19VDNQqtUC1TTiQ-tEvnxER8DORbCwtzBNsCrK9cl2ECTZeRIHI7VbNVtJIP8WxlV3XwprD2aG-ooMLSEgqH9yOHkEtRIvZxf0LsYfdf7PCxQU9GISxR0EeVCus9uMrC5cSD-RkvdkF2MXdLpyWvQW6zl8UM8EzeMnTvFYpvmRtUkxN-KoMvMiEehMlhc8R2vmw7E85BKgPX4cGJhUA3eCcCFoDuS2m8p42YZwjGP1kSEDaGLwGjv2X3lSKH1kWwiXE93dsLuA7Y4uBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDVfPH8CdWVAG4knh5JH1WngxAM9uwD5ySMO06CBjWVkA4gF3EupIb9h__svEd3eBHs-zYhOBDhANTpv2hEdx31usuE_spAXfE5gNnVgN57BIcOAqr-QM1kOlj9lHq725u69su5mu0H88NasRAFeGaActDrwzT-FAqlMaBN5UKkaqCEPiussW0ezC152PmDmar6f4t4T6kA-40LfDvdYvzJDmWQo0aLdsBvUydLlbtHqfuZjeWV4ZgvA8W0BElpuyzrcv1J4FO8d4NhXJgh_hjKp9wRv8K9h52Ml8fQ5jtpyveD1xcmckr966PAGSlMrS4-SwtqMz1wp5oN5cdfj8w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nN2ocK3v_vGBUawkkwtStS4mz9nfNfk0clpG-ebpD5YHwlxJjJhWMoqikE0sP_lxzmn-NmDPjnSsKIcVzkXEc3vvprGu84R7ykZqUD_vylejvdhD0xO7g4qeRsl8187fdg7Dg6FSZCdvVODI6wP74aYW0ItKYNkn2dPy0Qmubp_56zJMFPiwf_oaejRFHhxn8Ts0xKqQ1yJQkIjTDAWLMmYWeym5QHQHLk0MST2ff56OehJaJsQ5reL4l8H6AU72ySH6UNT4_PvMO3u0ZVKnZW4_Fgv3hB3oFEjEXHJBMswKmP8YqZqyqEfyQtRUY_S59Ff6wFyPFbh1FSy49E4x5kH3ucgaOGo3qc6jcqjJNwGv-CD2U3Dpe6E2JoeNm2gMNE5uQAnQ5RwwP69_dxgu8_3LlUxeQqEVLGAqXMIoaF29-YrAplAKK3X_6qpt2vEbVKjXiixvIWXh2Xs12wgP4I36V46noq6okBbZw7vEKbgVbVsZCX8on4JwasFOsDZIUL685zGTc92dzO4tqfPAkHAp8v4pSjfJKXrPI0PXhRhoT8qLDUnqPtmRTcVEVqY3-jkoUim8JpG3R4XvH-geBtTQyEzuzamSD-Re4frQVZ3upA7VaZw_AWyHF22Eaxp2gaPba2YrvYf6QUnYOhQIuKuyNfVdgmJREfDN7TA49Hs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=nN2ocK3v_vGBUawkkwtStS4mz9nfNfk0clpG-ebpD5YHwlxJjJhWMoqikE0sP_lxzmn-NmDPjnSsKIcVzkXEc3vvprGu84R7ykZqUD_vylejvdhD0xO7g4qeRsl8187fdg7Dg6FSZCdvVODI6wP74aYW0ItKYNkn2dPy0Qmubp_56zJMFPiwf_oaejRFHhxn8Ts0xKqQ1yJQkIjTDAWLMmYWeym5QHQHLk0MST2ff56OehJaJsQ5reL4l8H6AU72ySH6UNT4_PvMO3u0ZVKnZW4_Fgv3hB3oFEjEXHJBMswKmP8YqZqyqEfyQtRUY_S59Ff6wFyPFbh1FSy49E4x5kH3ucgaOGo3qc6jcqjJNwGv-CD2U3Dpe6E2JoeNm2gMNE5uQAnQ5RwwP69_dxgu8_3LlUxeQqEVLGAqXMIoaF29-YrAplAKK3X_6qpt2vEbVKjXiixvIWXh2Xs12wgP4I36V46noq6okBbZw7vEKbgVbVsZCX8on4JwasFOsDZIUL685zGTc92dzO4tqfPAkHAp8v4pSjfJKXrPI0PXhRhoT8qLDUnqPtmRTcVEVqY3-jkoUim8JpG3R4XvH-geBtTQyEzuzamSD-Re4frQVZ3upA7VaZw_AWyHF22Eaxp2gaPba2YrvYf6QUnYOhQIuKuyNfVdgmJREfDN7TA49Hs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWb00eu41RseJFGE8Qh3ymTaIAC95deNd6K6IgaLNk8B-qADVHSxNUOTktw8mZUzS3XXyLGW_RdpW4q5g5gfoZL1bOt9mZ_D_kmz8Q0RcMhNuAYgV1n3jgGpGQcV9N_9Amc1bGscn8ta9hmu9-wZzPbaLO0PeJ3uB6hQvZgAFfHzCi9KShu0ePiNdkDUzZHiUYQ69WZz9msG6ZUp9WLJa-zmh6AGSISUypsbSd-HueFL6ovWA2-3QPkIz91S2hcN_R8R3eiwASNFduqOdIjQrUdME2h-1wcmDX3DKVg8s2NEdgF26lo62Vw9iylHibUoLUr5r34Iadk1-LEefYYlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR4KMMUltfiePXU8O-Woo6NvuLeoxtKGw7IGlpiKS1IU03V3HjIAqtgzI7433d2-YuVhZXgcgPgZf38eDGLwyAgm02VFSGczPMQVxOyJw9gwslyqp9zoKJWMoULhHRrxdPEDPN2ID4b_iz2PPwIIhVeG1RmMnxgf3hnxq8kZfl-pr9N94LihQBRMdvNXBlF4Fk1nMSDlXMkDqEpLKhMv1G_aGO_ps11JHKLx9P23tGISsIulZSKqJrUM_Pw0_1iAlF7dvh7EZLirRRR6fWqXbRg-lFxg1e4JScZYA8humPp2LIVxYKcjx-67L-DX0-k9Bmv1oAWPxilwqXqNy9gfow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjyaDiRx44JSAaoxII0zQQRy1myKNgWEquKXwPmhTCYN7QXVoRdMEYIYfiaNxviwqO0j6lh1uFoQPwNoz7KqhtYRk0wqMUxoMBNwQ_6TEJmCXRMwINyfVMz88fzPrHU9JmUg4qrH8cxMKy1aQOT7aXxOpHIMarVUgB-MJ9e0a6jdrGZ9j3_YCPIJD315uOKh0Hl62sKB3VWmr-BWjJjgHcFp87GQFWLo11D__fklHQA-yKaQqQlMpQsXtHlBgiINPjkdK_OBC75ylpH9A1vUFrjqw_tYGohRmBv1dH4xqXizIL5ExqDykdbdOfLrWUYMkHmWJXFXiI-HhZDCzz4PsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwTranTd9BZWbx2-Eg6iR-EHZCFEOKe2_xPwdgtLvvsTadUv0ZqxPU5NOYqaWVDJVV3yelMv-u2MlYgkxJLPjCUnADmj7wYWC0wRSF31mKKLS-e4qCpfGs1UngAri69Z9UNV5JfuKUgsMEmawznwFb5g3BmQ3WE9f-kIpfQoSZQt2EqnxiC6cHPW8SAenPnth6W7ulJnvIV-ujCDN5XUw9AqVbmaAVvZQGJvDm8Shs-JEvA5cUCxVEN98gUrbeLIaVJc9utTHq3uLjZLsd_leaPfRmbLg-zEnYtvMrzKhkEqmjXSH3gLVMvd1l2SILk9tn9657FlZQl1Z9wxITTicQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uo00U-ufYx8tGvRfFlawOx5lI83gjO6Ko-VnKJfgPSsWEqZQojHhubL3wadcuYZ6o02TufZIgMrTqnrLBVlmml7PgW7jYhBn_GD0v9ZdRgz99u4Mos4NuWNEb3MKaURwNCKKq9c3z3HXUODzvsY5-cdGCku9-kuDpzTTFXy5SkPH6se9N8E7_Sk3jkS_UKu3fLSuRZfkwmQSoaqN2FLZejFv67F9n1-0EmtqGnQ7qWSpjvKjUOdHbVNbjGZ089Do_mXrbAUPGdu-a7b2rX0-R-2p2hyDxmV2_QZIzQq_ITjI0QaSgrrOQr5xHh4dSVAq3GgeFtnIddqZO4OzAbMXVA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3SJPi9TrkhBeHnEOjlEBDHg6iD0rfw9yTSMXhkGMthlLbK4Pu2d8E95DjcHYxpuoFhmASpoLgE_JQS8HVM5OHNLoEEKwmwdEPYuvffxLtdQTrVe1rLQ3p_dCGYOBRaEDyXlcq2wp-OVCd6SZO5WJhX7IcJhxiPgvH2mdaitg1RWIB1AAhZQ3lctUnAylxrK_R-qcso6Peksy3KX6CyLTb4MjerXNhNL5SRx3vrIbua4UZrr10waUnob6CuJfgbPD2UdFDWkhZPVrAsaxa85pd5bqA2Oqq29vpqjz26w1XrJu-6uOKUXHKhigH0kxMThFSGx9M0lgZDCfKg6c-W8vOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3SJPi9TrkhBeHnEOjlEBDHg6iD0rfw9yTSMXhkGMthlLbK4Pu2d8E95DjcHYxpuoFhmASpoLgE_JQS8HVM5OHNLoEEKwmwdEPYuvffxLtdQTrVe1rLQ3p_dCGYOBRaEDyXlcq2wp-OVCd6SZO5WJhX7IcJhxiPgvH2mdaitg1RWIB1AAhZQ3lctUnAylxrK_R-qcso6Peksy3KX6CyLTb4MjerXNhNL5SRx3vrIbua4UZrr10waUnob6CuJfgbPD2UdFDWkhZPVrAsaxa85pd5bqA2Oqq29vpqjz26w1XrJu-6uOKUXHKhigH0kxMThFSGx9M0lgZDCfKg6c-W8vOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXq2fGtMAwyDzDr3tJATlsCBIS0CgAnWtFIdcyzk3Bn4A7CVQPioUW50XAicLJBbM5ZuAmvUG1UemmfW9knvVLXIeRlGcJok-WzyzZ01bcPzIcZQtILkc32JeLO23aq-Vwvkp4SHq9gfDNQU5KQeIkHwiwLVY5vLuU2HYo4vnzz6SQpLSMYUM-ucXrYpWQbMdt2Lo_IxXD41CSPKEVai_Y2Ux3tzQbqqg_UvVg76cvWPajx65AkbauKBzCDQjL4RNF5N78qCZhEZrLiK4xHybX7fR3VytnZ1k4x8K1AGMDyS5ucThRcJxgs6AbzVX37uUAHHyk4uToiaEphX9FQT9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlpdj1RXSOqBgB9ZZLQhhZ_9hmtSIMUt2fDyDt1R8CPO7Kc6HaKmg4g-HJGj_5UXVzSz1GnKG7qeyJSyaw9zXq8vjWSaiBMxB8znbNSWSbKEZuB9QeES72bKtBgqs3xNvwZ3zCyWir2z-W9GtK1Fxr8NrSseS2MFyB-HUZOzxutXF7SF6fejr7aXPz87MY-HDnnWJwTAT558_T8KoUXRdPDVe_M8tb5zWiLbU-uJuUYsLx7ZujNXguiDDCIcKsXb57a6XoWUEgsvyEND78yfkXq1slJFw4nuAforYevIKq4cwHgl4VzF99PpNcC7AVMNxBjTQYoK2IvqqcdzEYuweQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KE5Gi-jxH4Vxjt5FBhXw7JT-PkLpL7F8NBW03_9pO2Wgwo4PvzbyIuBuUySMLr3t0fwkgmoaVbW5Obj3-vYroP2AIAvj7ZjnATOKj6B39topefVczlnpOIwG4dXnYbvjq0FVyDtYOlioqZvDPcytHbzhrMMUIP5j6KX4Mz-m2FpfiMm_c6NMIpMnAITAsJ1Gkka_9t0DRbV2O33TvxQElKGjS1xyGKJI8ht63SMtgmiWLR7oXqeMLifc7OL7QA7EUa0dTrqVWp8Yt-qSLNAQQJ0POxTeXcW98eE5j7_le66NhD8no7IATKKm2QU8kD2j5LXNYosaFGXPrwnY32jDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn9l3p87U1gN_sCoKbEpQxGB58Y0qLTM06JSniD6EujYg5buKyvUJC0o_L8rVZxkrwCqv3gaKj4YTHOVbpk_bz-CeA_SIBeh2wGuGcA0IhIr4jdesQSKRkMiVZ9wkdGL9edGnxaVyZIyIJZu0royRpqmWoc5tC5jfR3u8VWZTHgL6idgcp4RN3hQLwhG4DSFjs9N2C2HHEOOjWOvMa43F0fuX7oEwrUTPjkMQevHY_sH_A11fw-x0cjXzwb7x1COxApXJO3h7KI74pmL9l-a01YBH89al1oodN9r6R4Q37sdvZnLE6Ak9EpzQUTjYaLNxJdxBgbNvuH7-z0LSEv1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgAwj06HGb8BppT7a8S0mghnGCgIQB-FYEBqbWFKDhxitJ-eJkp8V6XLUzwLjse3GlXOJCgB-ev2DBXSTDoNhMoI-wTOSHUX4tcRBrcpJ0tfIPO7jlyPQDI0pFde3NVn2bj6GA_zJEVzUN7VvAG3R9t7DyYMQZD9fkF67HUYAsCSnxRSz9J-5TFWETteFzNJsgpEJXS6v_fM87qMBrajz6-UQn-oi5pj-idiUPQgXx4B1JVAHxI4Cdo9Ea5fubXBgYaZcAUDCe6A9ejBw20GUTMHZHYNNprZLK995jU2CVP-9wjlMoRsQom3DAdzofDv7vONww78qXB8tvHgkQUVUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHmB-OvlaBhAF1x_dxt5OE0wakp6pBg2dGPRb6mHAz__Os6pwUrnWWQ8ystTgoL8qT4PgMwgzvSuepPi2f6-XnjuD_l-udtg1626ybw56ziCWkkank0nI-AmWuv52EYrdoQN1FZzS0sAKIDt8EV5l47znfxp0MJ6ELa55wsT2oYy21nPb1Cr5tKE0tosl2T5lWOcrzJ9HKbDSGuBBMgOsTC_yX3WRzZdAczdkdQ6E93-2YaDKxlt053_j5o09y3Qts4uAFw-PoKN_FDBqjJxwuYOyKoZmTnxURcfJZAhOngK06huAo4jvL4MaziBfCCWNYh93ChL5LVd749_G8W5Tw.jpg" alt="photo" loading="lazy"/></div>
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
