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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 23:41:19</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 321 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 484 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 589 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0Ta7JCpLBiRhSbmv8ya09YoIW_kPooi7l8j5L1P19894w3th58y8vAnsGDHmRKqYmh5ke3Y17ABEP3eDO-oGDzbc65uU87jNpXcMdV34gfn0VnY3OX484GFtEkjKxVvhq4ddWsp77AG3Ro1SD3RGnhafjeDXO3guVg_f677ErROqksSuiCDbM745WCUz_9nj6C6OjULCfOHaM4Ls3L-fCn_N3cxTx38HxzrAs21_FNxlicXG8gX39-iX7uSoHd8r5i-mvEukOni3xwHTUhFziFRV_9xbgfiD6r0dafoiMWv-C6uSMNmJ4yxcu9nbtf5dSdEA-CONwdODUM8WSXz9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXoWK1uO-Q01VzYI7TYTmJRFwU3yaYS9Dnx6e8ZbJ2dp_z1QhENBgctX8s0HxoHW2-AUsU5E39f2VJ-2v13NbsCnyNd3vZZsf5wQi98RSLdPalYLx9LCMLKIhkVumPQCDhspPILyWqU9toJHn7eNGLecxGV8s_FuFWbHKIuErBxvTfI-VDQqYJUFmrSEeUqnBwA4fpX6q2cdnzk8Ymzsi-91H6Emw3PuQvwl7l5OKKTgSAq7nQWtH0ldayUY1bzf_dHxhDC1aCeyXa2X8HKAebBx8kGe1tyJcf4YjSTD76kgE9AX6TfHrlVSg3DPu8ygRlol_t8D6aDc-BXMJCxrrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA5YnH0SSMnHh0HVYZ0Bc5b62Jyi-X3K4kpSVMF3SWFXfqRX3cegYR8jqOUST8iHIJuo--1lrMeHNLhxlgy2YYGj29mG2ZuXTgI4AJBB8pHLEmKzlten6slQAVFrrJpFV1zFrDAxkm3VEk16_OP0fVUREBCAJPGXp6u4q8gP9dk7nV27z98eRJntPbaZI616ZJA223U7v_EwViJuleMybnMxPPOpWvCB2nYdW8IMS9aLIQgktHJjSpTxdq_xhnszKsLwa4760OEPPnAuy277usyI_CE-B-gueUJLk1qG2qO5Cz04nnk_XJ-4r80Pf6O7E0twHRlTVt5QPNa961TMuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pby0rtd5ojKQFmkNW8yvWMYbZlCpK0n9MnyrJNTfq1CakI2cObEfCw7HBUA6R11uo_Lvv2e5VDWCjPcIP4Gv7W7qhFSYxILYPLzo4o0PBBVDXlcFCPFifTedn3zow7QxyCwCJwrNaM4ZxLm6pALj9m7ltgrp0uEdfM7kMtERA1TJFv5koaP1EDDDYqp5irmSebeSpDX-zURv7rXpknROXtedQQMzZw6IQtIKkwBq3TA0wdQmQDuJJn8ZTETYaZsziKtMmsQ9UFMWP5erSBO5MtqXjZcW0cZL-EmmdXdGfj4gTeIL_WOks8m_yX-zKSRZVQcxE0wR42L5-LMj9imOgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOZcEKzyiAirzYRRJWfpYl8JkiSB-aCW-sS2WEbsdoZDy-Gr6j2FQRMze4iVBye8CWVIGj4o_VWV__vmW7gUBanyugUodwPXHzYA-3hKYBpc-xAI1lNIepMNAMVQ8z1rGUSax-7Q4KZ8FfJc6vLtS2igzZcqEba1P3QT0FemK04c2syBN6D0gSGQ7qCmQjxp-yEt7FkWQI3q7NLZdzvFMC7SFUl2DkstoG4TzKdcvPNGIT0ACpA2IJP_42xMGfsrSjZjw5jUPfNyQpEB5ksmlc5BC_4zSEZW4ErsdW8BVV050q54G1lIRrfxv-tUdxNL6sDAitZ7CDDLIaG5bcJCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qo6OX0BGbpzwgjDQ6mO3iNdnkrR4_YnTt1rSUsZiy337UlNkWk6DMMeh35MgQa73oQxx762eB46MJSAwEESMzkkVQGxkbTGYvs_BcMZ31Dy-h7aTGeasNTR9eidXP12PaSoCAsXMbHTtap-gGijM97h6pSZSJrdmwvvd7ioBMA9Be33ueh-_7k1s72L_lAo2ppPCAhyyG_OpBZnOXG16cOzYUOpYKidQWIe106o7x7mgAqHNXop5jJAnjwX57ipAJGL2FlV50GBLavlVYhDh4kaCbuO15ywwvSBmvrUcyGKL8Ys0GV8jJkEB9G-B1xQd831kx9MLuZTpCJX-lVQyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fu52Pya0E5t8sfsrBKuhVhOnQGGSd85s4aUusquukrnjjyCcPAsSbYJ4zNmUkezBMjMtxn8S8JjmMsuOaR7KfNeFAkBq4qSODlIi9jbLcSl0HSeGceZaRS5484EdzgscOCZFVjV69eSig3T5LhIglllBlvoRdxFxTPzs9wb4LPhw8ZQYxOhLHQ2740Q9LGYkC04Po-_islERd_nt0yrJPVVSv85Y18DL8i2K2-O8cGFcnjVSZPfMoCK-KbEnW3PdTl9Bto4PmetrYhEaaruT8UBZkNCYuPdCoYpX5Rmwof7BoSFGcofD5IDe8wsrnhIlG1OIBlKU_uCbRcsIOJfu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONtVz-quIFJiQnuDh66JacebVIL5c3j6XBX_qVitPpjGo0d6TuqRZWJMOJU32fNMfPLQLxlZrQfQlML889teH30197NVdSU2V_N7149wUDXgO_ITSmhdfhZTo5ScWiVp5hkIJGJG4sHMwxrrg37rZUc1nh3x7FfJ2gPY1oLgkWkQk-C8Ar6Ono2FvzkTJfH5zb6fvESmaOd6v_vEUVWjOTCSIZvOjiDz2n_uxjkVh7YzMDA4tS_0t-ApwOK8eRLfMc1-_-FyzQjOJPD13oO8Mf3lB28ps6jC7fB2QOvFLEiPL7ev8F6_p2kP4GCclggAtpjR61HUWt0RcxFh5YWuHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCjy0ijGGBmz1eQVBVbMcpQchGYIOvv0twBaNPJRBgqcJDPFb8fEoU_qMvSl-w4_LGHvI5JZHwHC4y-HpPYAoHiYN7le04Iy-mNpd9l9rJjr2zocCjngs4xcmECFWA4blEjUM8Mi3EF8B95HR5FI2y89_DGlvwN5trX0UhOjAfoGkEidEGdFXpKxek_1hJ_E_XhJQlmycGwMGc8DxoSwTi-JyVSnKrqZsKQEHzyMIHPmAPRuQVes8JLDanjxh-xWGb0NLwVbAEpgoNlSXwD9ZPorenfrrh4oIf-nC0pWZJP9F68FOhaQ6gVocWc_ykn_Bw9Ow6i0mN5Qbl3VXXt5Wg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=RX2Pr7-MQJ2fft82EBx16UMp99V5Ox8bMP8goz6DmgDiN-IsTeRUZ_cmra-UdYFB79eB5v2VCJ9ofe3LQHvW1AWIY6LX8pHaZlX0QFpaFWNrbDoUDiTECFqTTAkiAHXh_xmifwoPN5xTjv_79lKcyNub-75e7uBpT7ip_52OYgs1h8ERUWgWH9II1PGfC8Hz5YZz_ClPyXjJsMMcuxB-UmXaHR7_uafOLRyhIWxWo6VSOMEbaXBXu5Lr4cYNQMvy0xNZkVye6g9J-MJsZdHWh86p0kwfmZsxI0La9QQrPPqUrYoVQ5IcoW02h2CMHzIKGx94pKM2y_8mTqhqZS393A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=RX2Pr7-MQJ2fft82EBx16UMp99V5Ox8bMP8goz6DmgDiN-IsTeRUZ_cmra-UdYFB79eB5v2VCJ9ofe3LQHvW1AWIY6LX8pHaZlX0QFpaFWNrbDoUDiTECFqTTAkiAHXh_xmifwoPN5xTjv_79lKcyNub-75e7uBpT7ip_52OYgs1h8ERUWgWH9II1PGfC8Hz5YZz_ClPyXjJsMMcuxB-UmXaHR7_uafOLRyhIWxWo6VSOMEbaXBXu5Lr4cYNQMvy0xNZkVye6g9J-MJsZdHWh86p0kwfmZsxI0La9QQrPPqUrYoVQ5IcoW02h2CMHzIKGx94pKM2y_8mTqhqZS393A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzkrdrle-Nqhcc0ftdqO9kT1IZM7IFF9qRDp945q4PStgX8nZgepepvreZm2qnzUkdtPBKRtPjN9zF7EP3MZthqPI4LOOl4YGqlq2eNyui26E3UtoqV8_GGeoeU8rRgYirEcvKErbkBnUgjOA2zZNYkV9ir9WlBCb_Ee8LnKcUo1Pv2WQs-HMbRZhf3p0Q6za2VIMe7xLaNefZay7BNqaC8WAKPWeLErV_gxXji8N6B_kzccQcIOO3FpBCFC3o7724S4NShSNOvfTe9nDM-bc8mHuQ6dnbcgrykSJB0s0CFGNWm6ccnFge1lxgZpqzxyO6Ux7eHAvo1xrrQXv7MkhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_1x30-I8GuDgw76JpKCA-rJC_6uHf2UThV0mXggTyTsjT1BJjxOrGb-gvDQXgOzLWRqAW8L6F47MHCG5c8J-iwmVckAUwMNxKWNLVtHAcFmdDHoFm3zozS9r3yYBfy2ZXrYqaXy7L8SN5EXwVpPdzcpY1p0t08sYT9-xQTsV9Cv-PiIoV5zZl2y_UeOeJh7uFgp_4STEB3oae3FgAko5wNkYbpm12EW31qZvX1jcHTBay4Y75tMHwX8JvcFYrGtthFpZdZkGtW8PbY_cVShfvW84QjBaIQqPRyJ6VAyznP4E1ubpHSC-3jWf0uSd0bvRMx9YnQLJ2aFT-91YqsAmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6Mst-QhskGgVuqHIRA8NH3ybvORN4q3K1yTwWtHN-Ghy7yTwSdkZ-KMcrddlYzVp5XB5fmwo6jCqdLOyEqXz4xXt6eTHFX7dpnWPIZ0Zo2kN-TQjUzZMBSydGmQK_pl9d95rfVdvRBX7XNCUTCCtH3FLa_U7leNj5tgDqr0ICFj7nuKbDvS8B0-zsbVQyg8zEn0_PEi7uoY1Q44Mmg4Pa9d22Y8zV5D4T_FCqjbLNvO5TnhugWeZkME4XbSJa0TtEB5BNgNEJuNmCuc6j8SiWFAQKGPnZ7jTZoUcYLw_Vrthun-MzwqlwI7fcUXlQ13Tx9StdE1bRrz1_w7uCixUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH3ov88-1lfJylgZvfm0maa6eLk1GD6rDMsPwdMS0RX1-ohxhieu8cqH69imaW4vZUyUXY07Xkf3RdWK5OEnuiApPc0geSuBkIfXVLv7934VYSu3GG0mPAOCcTDg5p5NNQhlELl80_em8g89TSIAtRHUlSJdUEAfsxd5Gq4nv0MOHBkbRSz2eQiO4stvyUpkCgcQ03iZLk86aP6eCleQACNtc4C4ve0RegO7_M9N-lBWjd9dG1EBSh9iCu36gpDvqNDcUJQAeRDfac-YXz6IXT2n33KROrD35g4OSoRzsiHFo-PMZQbFY-RrYzVuHnroR0HM0OGQR-g1u8FqwPc99A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk9EO8at5DtVxbxaacaU3Dv-7L4GAidRgtZ4bxmn7_3w2k97nnvsVAknARdkUJsjtmdI5Fz7Blz-pP0fZr1CP_qsdSWpKVkkfnlwvC_SLHNGDtpwo3SwjGIkFqrwBHzKNffxacIcFl6KckN16iHHVvDz5N4GGU6Xcu4FBjYZMby_BvDDy-VeJ-MUhtXVgdPKbDUlCBW0UOkNE_rw_vHlZ1vA1Xi_d57A8Bo8Dx_lcouzo_CUlcVvU7lTQBR-MQYSo7GzTEfThV_Tpj3tfAxbVkiqRCNMAlYlnj9ROMWM4-sT8LaMl-SBYAG-Zqe6qCqM-wUqmZ-p_ct3Ba_zcwPPRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHksvK-N5Un5_ZghsFg6FfgppoWrNbIo3euuNqZ-pPiSMmexhuHI9uSocD0UgFIBlrlP9jjl7NUek_Ha-uSeTRKnRc_6PO5fxTJZPM8Y8DaVK1rTbogXWGJzBlmXPSUJgf-ee0cM9EI-qkz7MbWecZYJhMSVBhKWPg3SBwN0bk3fusgPyQ-SB5POzWbNSvXWnRvm3G344asb0BL2IAJvnUOvaG5vh907aAjl_xbgspOMCP8dMiLrqLOnIftWL-Tuw0C6zmyBSf7CpTruqB8a3Nji-AO07NIU8dZSQiNstMcX-Nw5S9aXBn0fiD7yRKjZKjC-kUXTcpd2pgeHtiKU1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VPjYL_JEK86oEahweSHGF3biheYfNOEE6mavP1YTHMthfBNe56Nv6smHwsI-twRirAdCfxELvTMhZWazDJgkO4mmWLPgOKneh0n-TnvwQGyEdbOGz6evplh1176TmclKrexm7ljDhit5OhlR4wwZHeiV6cJNQFIqK7P8krWv6UJpOAH1LoOz8vPzIxtfqUH8sOuddu-Q5fDGT6U7FK26qaf-ryCFYt-aogCmLTuspeDkK4uRcGQSDyvHqbnBVP11Jqj82D6Cg8QJUOdEvDQ6UDzoBOtDlFFrZ9MM3Iun4bczvDQBicFb38P4ELC46B0mKSAQvwf1ytScSwrVUdij7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5ymOgDpbODWRFDobqYaYByukoOd3k6Ku50xsaZqIgYORPAt2fJsZchmlxPutB25IsdYJ5DxKFILfzkZxesUEScISTk94lQ4bcU_1EjU2YWDVy8is5KE6GGKNUtGf_hrrm7lQF9zDA_zAaNoNIUJSNUxryBVZypKBUNvfM8AesUafxK69IUDhKfzOiObC_gTPyqv0wGxd9gjSvblL1eiN5Ec9sxFoYKBcCUGvH0y8ZcCOfj9_UoSmhjGId4F7Q4FsuOyjdbRbZ1ArNbr563XypvKu8Vhd-rx-1UDxY2dnMwLk2vDQdmMZot95GFCShiuggXDZd9pducGTLJ37zxpcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDo_NFl9yIhCfUdhsedA87dgMjLApgWmNbeidj8zHg76EaVM2VdlNmMsxFMtZ76ohYthk640q1hXFOvHjQ_LYCmePVduvZChv3mA-CNvQgoVOGguZn7KB5HF-koYWsqNR_IgrSEtzLPMh_kk9kscgQxJDnJ8a4Ta0OrNY6esZqJPnEGLyxMmLUhk9bosysfXf8Ou-oli60DxW4oi4N4uUUHuPA_1o1YV4GuDJP2gftdfd3_WfuAFx8b8jhARCltaynpPEjjr-n4ueBzWmkDndZzG_nJ5XSSR0b7XUN3a4xTvkGF-lnjE30MsPRtdX-ulN9F1LZC6Q313qXRtuZyZXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXVA-cci8H-D9pXmy3slpy-WjL5wJr5p8q470oKuDaTF2kOtB5I_2X4fVlK6_XdrRQBh0Q4Ag9yAU_8F8BVt-KhVuHSulqks1_SK0kPwtXN-4lt50bg-caoUvBPNfJsisdmamVaIKcpMqM_oAkNVp2NXClHJEhh4WIyQpbcCcELfrNbnkO_kr2-l8i4WmvKd71RYDMHae7fFYeabSgwA-RVQmE-_y-i4gyrznXu6gvFflhaPt963sGqTx3mjbKz3xFhX5X3QeOnP78tIV0JHy_Q8fwJ5s1XcYbDRuhrTsRiuED6m5ZJE7sFkm762Y8mK2W1OeizXLoiy-Rt7w6sQjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0vPenUXS-8aYo50QRxbEo5801neMf7xjeZKOrOcqxWcISMMP3BC_8dFf-5KYch-cDzk-QJROg8dfurSYojHFnmW7eg_MtPqgy8pZNfmKvY6HUMPQ-N6_XwxXjnmX-pEVi_idVPi9s3rp2PPabvmYl5ijo-Tg4gDMmnWymC7QAQUuZq_qOLUNnztWjx6MaoihMVv3PqXQqNFkjziYTitk8WE_nmaAyx46Ko0O1qQCx_K9ao8FYCCQnx2MB_x9jNEmO_RoSn1yY5gcubtfxWOcSDbnlyL3hyspexQtIcHLwTUuy4GFOYeWVR69yuSbxzB0TP5eNA2qXhH6pjcYsoL3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTAcg-gA62MGMT28j-8gReM1rWQRe2KP3keuMUT73NQlawDFxptZilS__ca7tbR6DMt9hKTWQO1tQhRVblmSmhTPr1J83039z47mAV3g1IM-MRmyn30wUut_GcKXsGKd2lVsfBtPZmfqId9ABk4uXhqz-GjaLJN3yrnh5yxFhcFg9GN4e0Jp3vO4FCmjpxA_L-i5ko5OxC83MYvEih6DBhQrKZqyvp0MhyV5EblEqyPc-gBc9n1a5UF_AeVxx1HSCm32hveOQh_X74Ks8QAktGJn85RIBOPCEVUl18x9gCMhbH3pcF6MD90PwoufcYsr0oOgIQNavMOIo38bH4JD0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abRWBb0_hY9YhCq910BbmjuGT9cyuJ_MUV6QDKg513Wrbl5Mc5BQGCcJ_nwv1nFoYOIc4V94D-6Eq31iQwl7K5yi3VyzHnXxhanC2lk8Sri9eAAl1fiAsjafT4QvUnx81zcWlGdeV8Snd0uHSjuu72Xcj9OiDe6xBEJDk49zizG0pGS-OMEtt4MXofiHjhA7km1m5WAds-uFgljGEGfXjC-UIFFioy6PqEq-5I8226W9PzDbuesyNQTMCsJ1SclCeTU3RCceIdlbpY5zE7VxpAbJh3lsUYnoHc3EQYjzewWLBhWgx9QiH-jPfF8mnGNk7jPmw6hovx8lbNORhNGWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zpd-1KHERcSytL5Fjflkr6HsRX96hAD9ugBQxkhkFz0DWpEUvqLZGhbf88GMZsab6ZWHbwnm6uA9wMG_5vst0BgKeN4K2Nyt-HIBJLUBvvaerWWKGzdOZqmdBA617x6_nuaekLjsxKahwglZkx8fszRoh-f0Rg4Z2Ese_yYREOCf4ref8Vlfp_xF4ASE68AHBb9P59ECFibT2aSMkm_t-nUC45mpAUAHm1xIbpHQOfDkr4oOd-UefEvzjur4qg8smME1nBQF5D-XmxQKw80q_Tyk2pH-yhhwKFTr60c4P8U3xsGW1mr2iuV4v6M3c1ayw_X0-dBl3kH7FxmxDA9qYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVR6DC8fWxiJypH6Ab3HV3pQ-_NXu3YuSE7dH01Kb5wgkDS2VzkKl9_TzKeHz-78hc2kdHE_d8bXfeGa2FlnwDQ96gC0HgTdaTOvv_iwF3NstBb-gx9R2Oj2ghF2bm1UdbDFt94B9amY-pMeoxJVGGmHAgbWPBZn5JBgvw3izfhcjzt75mvigAshvEyd_YH5Nk46RzL-JAg_TmR-9eGmStzOE5goq42MA4PIClfaJeNPJrTlex70PD2QUtSZWo8mDwuSrZnxd606yLTF6Qv_jy0DlrUHCOhtv8BGBiqB_alEn9xEI46_IZS0kf4QcKhjZqeBP1bOzlB1DC899UbdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJKvBWTn3Tkqoors-t1DuTom9nNHN86imvysXyAAr6rth-8knfkB258gkrVcQDz-I3Hv0jbM3cpBFOE8FjyJZXLGKMg3A7VDzRG4Hth4OE7GHzsTXcFldOe7_4Q-TD22cYkdW6gVBqySRt0OGQTui64DL2-N9tf1Dwd8DinzfNpj0SJJsl_jU3KEzHaoY7h5mqn1KWqU4MGyCOKmzFxpqPDbK19y5NSGX5U-54gj73TKa5wmkka_K8mb_awr5Cfwnp2T40smNbRakt1G4k_1dws6vqmDrNsSm1w8-W6FOVn1yEwaIDqrkMFc0NeL4pUYqaNvJB7I6zAWrLy2WidU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPmclUoe4lYevX8P-ljKteBSyUA2fOxmHfP7oMD5SzL-bova_ehTZcM0a7DZRu5swU6Yu-puwvkjpgHU6kUdUVHJUUTQS-cT1VUjlKTXtGnjXl-TCvmyfrDUYe6IyxWMarFUOPEireezbIoUnGY3uuMkC-qsG8SJEFtq6zdyIXcCtXgsDNrrefQ4C9eXgtq0IKDjbd2MfbLP_HApP5pKqiy02W3mnr6pCQxfr04mr-kuJ8MR9V-DweEGZhwZTnUAvsWyz08EU-PDXeBP3lGgUhXDgymYZWGNpq2WQKwR-245RLLywbshI8o9y-uUvMJryBVdtjdkf7iHkhHChLV0Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ8GjzXqe8eOBT-rMLi1nYhZF74u60O2h3bYWLdl-fkg3HIzf9GG44Wq_agA_zyuUFiBUjylUNzNNwAy_rehIjbekfNg-Xf_PXCr99kKKFnBHvZJR4dk2wnUfDrd2ROtMthQ2qkAodKA_tQ1L2Mdm6qMOQaLLupkvdmq4Qvo416WFbwYupj91fuOWnMHVKM_9bk-mcswUBd-qXx5xna-chr66UpzPR1jo3KR7L0FRJORIWgEp-7rwlOjGZF7O_pB-J4br47c5XGJlujH33C05Elo5r_ETOGMuDa8xziCs2YLIRIaRQ_1dXjohqhGbTzgro4O59sbCsmuIho9-VD5cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StPBstOI9aOgN-EetYZQWgKSlCUiNj34ROK3pfzi6J1wpHGRnrutY72YWV9FwwwwTIHS8v925OLnYLTtzAe7qUE_DvP0xUbC5WVE92EFGVMf-H5oLDexrm8ayKk0LH64-VA469iDXe10Uzj6Y5cqjN1-ko5pZouhkjldzBNXWUs86c_7BX0eOGHHb_ZKuq_exM0JAvrhdmtiqCFind-7yyPXU8UpdHUdeHDFraTU7fBB-rPf2GxiNdQbsNM_jF3gQ8rPEZE-Ca3MqOjDVYR0talKj-84iZNtXQKNkNOeyTcL-pqJJQy1R1LQO6Clwq09sgmkLPc4nw6QDWfc01DuWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltaGuvHBDOqOzv54bTm9FH7o41Yvton8_iSKUEvPouMXlOlbKJqO8e8zx2eDInWSphYa171gk-SIl58AnHtH0npznT64joA3QxL6xaQrkVECEPFi3duwqLXcQLkzqLiCsQa86lbEp3CDQ72Bcfj2iB1f-8FF7sgUz6VzMb8DxkTmVqOIbEjQIywHPOR5VaJQ_HodCbsGfxLRC_7DrgqTeUBtw0xQTB4oMMLuRgQQi4SZmkMgopZg01AKs5BNBT9Wnd3vIjqLd_9jkJggVx8ZpC6XUe-C9rY_b4phq3jgo9zhGnMFcuLdrODAoHxlhN0kEqXDgicnRrZjZDY2sPNhCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME047sGCxWbyf2wmo-qmn0zEy3lUN7X0vzA7uTVDSPJu5zkLjw4UfbHAyrZz17gogs-OehQjnszzlATHJFVcns2K5oEXpWexSjvY6n6FV75qSH_AtH4zUwri9u4Osgc8YkcQenmok2_V31gfziuwXngyYSgHor6NdpKeWjaG2MWd_0TbVvLEUcNeSeFrtOy0YkFR-TI2zlHeipUrIEPZimn7qLilZn7ek2nDRdAWuOLxfRbdy10r2W_O49FRiJlfQg60V9fqa5cbsT3BQpdxDY7kgIIVBow74vcnCr_iS_9ubYAQwSRQRlipJhrgy3DZi8rDht7h4vgqOW6WYcjutw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeLXwZ-5OKVEMyeiBgdfkG-y1-hghaNr4WSyhZDK94x1BaKoX4AGJ_sahdUVbuSQCHwX5eMM8yA2b4wnskhQNo7U6PFZlB30qpFdnmuNy9kur5DEeVA_ePOkU_GRB4icD5Nkx2SzDudzIxJJpisFLjjq8zGqONhOCGz9v_MvlfyIa9Y7QjDLF8TUq2BKto60mcKSMQ17VBetDmw0vM3pcRTLuHEQB7z4eiDa1t7od-a0KnrOVv1eNl63iJlBQeGcMgroIGje8hv1I0o5JeiXSu_5EfWmbVu8PRcKt3khXGu8fQQJ4UCqUhWIDXzsQHvz0vumdRihXUOCgHruKVWZHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHFgyUXGJE-qTKBKxUWdea5_vNRBhpKIqpMz8uPXvBF2Bciwkjw0L6S1xXPtzPkBo4RhqW9nm0k1n-ztTVL2KLSb6LgPlf9xAXUy6m1sXpqsPtJwbHyWzsnKPdync088wB9_KAiF1J78R5vyJQ4M0yCCpohMkKHKR64l8Og9ZFV0uG8hY2_1QdKLe43LJHu6H3mXNPvPyDWbDOxUrQU2lQAdXzPc3aSFWbsbtSyzmZtAa7vGo6PvYYsWztT0Oso7S-1yRWOI08LHcERDIARW_xxyHiPV3cj5oDoT0EiQ3d5OEHfHckxJroJrR-FDXCrpU92Ufj8L3YEVfiOTKlfwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHRTMhX08jlQ3nV-VenU_Ia0LthAXU_6ynciArh9PqMpN7MYuUeq7Owjmen0BiHlb1p3UMN1SgdPnL24QtTCsqeDXVF8-glcYN2Ki_W4enf7Q88E30Gs6XHRs6WeaY1u6CtMRRWA9zUijk51rzXqyBLUCO8BdKsXjLQ7vc_dj-bfGs6EXJJ4nepb9tw7faba1bLHCg9p29BGTlGyxRt0od4d_ooLAo-0p7R_AoaRJNLLpEti8Msf3juGohjl9CrKbGPUyofMaB5tEayYuD7O_pFhyUHlMZN5DHuHJQkFrD0pOf3-Xl_E1Fnrm_SvbJV8TmboRoFJzaBFUvzarLg00A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hti83QpYRwfugcQBiygwlfcbPKgbwUZ60nHj7a7RvKLHE2AY0nOgqXXlXfXiyp5ZCitX4ThZV3IrOdNWcwtDol8PkdNJkX5bDjqznQxcPGCuygxwerMYQ6mxq6NmDBP2XGqp_NPfg643udeuIVkWHmXfLHzY6EtvLEWkgWxJ2BPmia_p7C1qadPK6VR_wQm64fl3T7O6ztgRtHDJiQLX0jxprOHSUdPckhSFqLtdfsOKS9Edf4POSHBgBdyPC1ZELwoe__-1e0Aryhojj8yWzH6qQI1ZGAr2tjw1YmQzJjArGzitjCN2CVkA_k6LK4aNH5egrsPsDuDoQeE_VFw85Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qn80ipRPepx-qCXLKJ6oDElbtIJyOnp8HO73rTrn-jaRpZmG7qBTk-7rL30CbzU3LhAyGnzQr21xrR_qvs-05yCSKtV_Bt3kTiWhqV5QhipTvHAwz__mH22aPLG-C0uj5Qn7Q05NmZk6r3EYCc8IoEFHW64Rlf0KWTQkcqYY4E95C5-cUYTjlThAYugNsduljZCe5pBwgeuOrmfOKRnFK12OVbbElxFRm2lHsTNeZIWFSeWI3Xifs_094vDWDD4cOTQeF52Q-vxs7Z0eRWjAI3jQugM2OkNQv4Gswtj6G6xl9z4eo3eynbIarcTC01YkmtEnd9GqUlb_0TWGArHiqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m07uc_HNjJOEaoqCpHemJ81gBq2RoJ6ZlIALlB87gXWum6Dyia-tseZ9qiFFDaW7fkHATg24crSRyNMfGLv1Q_CG45y-zBBPyL2IQvwNUc18DSVX2FHb-JZcoveRDeOl6aygMGkIeOLFxogjjR2pIOoVPrdTn_XrX11mOQUMFLXrVt2cBs6-8BHGJPGnmH6vdO9eM5VASK2zYQGaG7oTited9flkJKL2CotDZMF7qAFBIZkVm3zO22ZnHDjFM49ymR7EHtH2HUvABni-mvJYgILCfz_YUpCGvqCX5i1oCxoSR90UUH9R2jek5atfFtqlHRB1EzfRBzcmfts2Beh50Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVxP41Y4h9KEuVdRorHRXuew7qMJXpSGMEVhQ5XnCcdLUJpjVKkq9A_4Dh987TrrNxvBRkziec68xNGtHhn1du9EnSuW0pDVz2cTUhB0Zlt4o3Bv-YxbT3WMWEt1GAkFeUFv_M080rct2awYCmXS4HYNoYKHDW8_mN1vNdgiCwMYQLeTEU4VLzi0n4TTyzlrgmb6CZ7qjO1l4Qp511HPo8yAAlq2uNAAdfdiIipqfaXupXfdnjfxoWB8zNlFeVn9JDcWUIUKTtrN_Nyxql8ip7vGJTrpwnh5yBnzR_15qg5TLPFPc-dJKYnxHL2GvlcALriwUdYNN_sLCycMPeJS2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZF8ajIBymAXQaQ__EwRFGK0mHjvTm3y4JAuAYhrCreF3P8aJsaXgWz-TZttnwX5Eb4bPOz7qMICJXHq1095wZDTtOEJ6Xm-zfCzdzubEtLCvtl1dQYAvUVw51I24bJSl_KxPWf2TQ4Vo-cM9bhnNbJVe_Rvbg0dRzvZ7PueCiNkFxNw48pS_i2M0xUfb6c9VI3ATnPtivN33pzhyATY1z-i3Uo8QzAjwYYrYN0q_6RRgTrpxGzeLDJFxQJ1KhrjF3lUXsPqfM8JyKm_-25_FXngk3JxejYquAsY2jcWaNNdtjd_RnVCz5Qme603VXazaksAZFZGDo4rnZ3VgQaPsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4io6ChNwJdD0Y7B4YXmpjI2EdHTM_0qrxL8NWIvFkZt7uAJ_YbkwyLqnKD3dCmRotMuM_GYkvLGL2rdT05RFn9-sreTpcB0OgHTt8XmSLRd18W9EuMMQ2QkMsR-fR70JIAjvUIU59OU6SYjbWEwAN4inZVPdqimpLoGG46bdxliSItoApz65XVn97PChqDzdtnTKEOOHT-v1LUrdKwFVjlUhQ3Bw7KE5Ae5HhMUKnPdfmaZL3VVjHZBG5ro5H0kQeQFS9XQqwJOsvVJPy24lEuKhTzf6_lErzOM2bDSDYnOrkyz2Xd9SUZQfGmEh_Wmaf8qx3h_V6Fqzqsy8lPYoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQ-PXKiMczxbm3Y1GJXS95li67uLHgZ1bhPePdTLzVK9U5e9SsHQ5zD1-iWPoxR4tYnR17QtBLj1_ahrIhxSPpFO_6CSDt_T_F9Ro76aQAyJBGIJPgAjUxErLhmYL-4YH6R7sf1L6j_dITGcdJnThQg_E_wm51--n3dTQRISp-92IEpewRbE2AiZLrv-kXD0BND4CCwFF4eG6IuiA3Cjz_5wjZ7o2EYa5YwCZ3R-G4c-1XQdsR6m4L7LnRRuX7zJz9L_nue69CsQCQiC0i9dTpFSQqdUWqaL2yOeQQdoBrEGqtNwKTft9DzNeV34P-cUPJDw5sVJgxaHvthCJLf7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rvh0R4lYv8Bb8zoGHpAh05XBMwr-DsWbTQl4YOVuDPeWbTettJNtNYJD6a-YiJ-P-BeWbqIwxEv2JAm2PUtRd6ECGwxWyvtPZxMCk1_-5MaBtE9DzssE6PwEz7sf9aMI-ZgSPnGIO_rjx7RkqTExaZj2I6i1zHTrg0oRDEBkkx8Ye0wzGpq33PzhVB6JhGXn0sqYuIKRMtMX8CP-FTLNJj41JFaGuWjvf5qIPruyZFmDbpW4SkxEd7WrbESyJKDA1aoOFnUSD2LSqJIjT3_H5wD1mAjkghbcQvxYUE7MOHUFXuFsP2j8TYR09m05RBFl19AQDNw-RY0kwG--N_ZGrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMzX09iKxn4oMCqJdSkUi-dvI_eZ5cNuIqeDi9MrDR6gtK41YshxrldlLxTX7ZsQ9D0b_pMuDKs-ihjKL5y3oEsVL6d3D0PPHHWQUtqiSuiIdGAv_DDxlYntfOZC4DuuXaz_CsaD1EP8Ihk2xYo1MkbKViIlZN2IqCjtkYlyl-n3Fe6AuZEFXDS4OA8EhVAl1zbUBpxvBs0Lw6ErbsxSNfOlTwCeROXiy5Wlxi6VUvSWJ7wjTRYqw_qW7HrxG0-JZu6F5_VZoSXJmaOtvBJ6rofUZfbptBPp8y4ERUDiSVmu5H1_ISt6E0AQrmJK4NVcX5r6YEhQUPVLGzNELVHQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dsti6NdB8ZKICOgfbNipbJAWmO1pATf5dQaufLdJENXIv_JM-nHLt-BcLosYkLqZN38F8fe4p-QqCeGiSUgIa-rTpAvWY6MIfl0K8WYQHRMfvn8MKsmIFYOlnWegm9v6wLgZ2pIVcrm6gy1CRJVqONK0ohKj5vOJNqFM96vU9UAfzvCx5kYFCodk8va9mDhw_zAd4y2HjS4VRDeAtlz066lwVby2l8EPsWG-Vj5f2fQEEzy9S-K5ZFXCG1WlOWAuewNezwhGT6BYj8wqNJgXB7sTzkOAXG871XzsonbwcTTkg7yZxQxMZncLlOshR7Jy6AwIDaNxF9-cG-JV1HpsSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTltSs7qEaSWyRLzNL4e0jiy4Qy1iD5AgCZUZzbpqwqPKO_9ARK9sSIk7ueoAzS-Ypxo7wfYJLzWLTVcZH8iu1NKogsD1KZKG0X4J0H7De_K6PGEgMj66VpTCYcgt3g2xQNEN67jSmJEA7TgN9uTma_c5Ol3gzkOePzHf6yK9jcY9gHbSuBi7fpz8SBxoPzgheRHaqLq3cR6jZSp4tsJOyB1-Ux1GbbBR8wbvcvFwzlNjzIHFJ-jkKWSYa2wJIVkaPKe6UNal7rkUlnSdJsIOtMmdSuGs8JlyoWRvL26mWgyqJcUuqs0yjE8Yl7YnruQLYIamk2pirFU_AdaAkN7Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhEOcjoijyaKzAOzL8AszPNZx6moByyr2UzSNLa9L1YGxGChdvv3Zv7f1QBZ2vQaRk94O84Lw72copwO9hqGRSPqdwYNJ5FmjZHgjuQr4auo05Pr-iVbtv6b6tfxnXAf4Phnu-w_5Mfyxp_i_mxK0GEDrHeqdeT8PVk5f-rfCKPzEukpWDwxlB55BzKXvBWgAyXRXzCPZlMjAIWFtF0abzGomnpbG8aIXZ-NWUoXzu4GFrVOqqvdAH39QC1fz42tgmB_zOJUSWTOi3Vx6eAwCKE2mEaOGw31zFl2xK1hOGByc8oypabhrdWwcRPJCySKUF6qzbLHiZGx6p5JH0TupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5pTOt0rdn5T6uYwsLxwvI_iWsNvKFAGn95q7D-juepCbkJJKcJOfvv60bms992ZVSXKUppdv6pLJbvQBrkkYRCJtLt2pCWLPek4_FwCuIMo742POqBtd6h63VJMJsWQNIz3kcGxtYkyQzm821Up5KiKt7hqE96X1mKqs_VPqPncX9atYg8sK3-5W-VxVA-y11BDFutWwSwTg3QijtCYG5gTcnEP43jUCBH4mpBUqrfFHPb_unxwKbux0OHOj5lAf0C3fmlfMZTHsJ8orMzjmNmiT1cFflWi_RTrunAdiHYYtGHIh6js5XBZe_E32kJbltP2LF1zfn6kbmD5j-AZ7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muF6A1ptn963PbXVqeWor5i5cWeJX6C-LaSUytCmRCUe0AZiFxI1fG27fzKnu5UGNpIARFUy85oR9uIUPay60pb02t1loYDKvQkltxzT-VlCOQFtfuODsd-LwmK7RZ13-W-lPPxIXEQoARNb3_4Nbg6pbQ6FYSrrkI3a2XKEaZoVa3X4O1tvdUEMyBJTR_VE-pw2pVKbf8WZ51ygmLG2NGuWyY3etzVmqBV9_pNDGNkQQL0F9mULsgFne41fe4PytFguoFzakaZ6Z1P3YWhos3LywysxUUcxqaIxqACl4FprGghFqSNJnH8LV0zl1WwCCL0H_ypWGG26tGZ0KNHGGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlVo492p6VUashl7XmvuD4U-uKoTMgriTYEwPQUKjUPhVl-QNa7Qj1iI00rHv6wo9w6EVqz7JQ6dRZ9ZSGyZq0nCzkUgnIQOD6kv7ERJAFelGrYg7oTmNvAECNSPeyTPpN3zSwzENKmvQp5hk5mMbrTCJI8Lq-6UHEGnzucnPoybKfKOTI3LoEUHpQCY9nq9DvSIHUMMbBw7pnOwS7HjLfabHcS484glq0vIoN-fX5KdXiPTEKEviPiCoUdqiSOwvj5fmaHzjvRnvb2VkspjoUAwps6cmI_NmnLM34CZI14ZeOl49BKAod1VWcgIE2aXBbuTjUrusEr6A4tG3dmjQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pggTEEOW7BzFW25Ujqq5DSLqPDsWH6hXznfJlOaPi7IZwru13Q-6Pmtt5_xuzJaQ9msTWpN3yMRHymdl7BBmYCHxPFpHiTjRpCtTC40X823HgbQBLFqEqiqVo9NWweL2M7evNbb_PHCZZxBSdCl6y5_uA8Mx793YYxVP0okCho_rtNyXicOe3pBoOhQZFK2W5FAWQklXU3J3e3iV3rv115WMXXBv6i4vCw7Iy1MTulW5mH0WqJ7Iy-CdEgkKc77EoU_lwMhVdue3oTsPLk-vCkjdHLUN7O_b0n4LXeTj1tar_l8e4JY0FD0v_fduK_7GZhGwmc6prbe5KbzU3FJcvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufoojIW8yRC6v_feJUUQgzqpEu_VzWlowbrPZ9bZPilSVMyLwrjtbok3NULiu4mAt3OLoSQe0kJ01x2dkvZPLVOBlM_RDVZ99ab_ShF6F8OC15OtNI6YJdkWgXaH7yOc_519FBUVKON7X0huu6tfJfcQXyeXRdP-5npZWJzOKbxxLOl70iwmjHWWSCSBLnV9BdNkYEthPWYaPy3Lrmia0TfFV7VTxPRXNFdX0rozvtVUoByubLAih8rveSLu3eN3bLGPqUwf-KLDP1jzvCKVYwMtzkZkNTpXZe5hLiV8j99IHgus3eyJzeNxj5imtOxq9sr0N3-5xyiQMX4l3ArC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OS2jcnKInX0XQadOUJysvvZZ4OdABtuLaXBksEIp842RfS5M6LShjkhwj-zgW7t16PT_7nwJ1z1VjM9R8Oytc6jHK82uMr92ekMyOH7TbcDHIwvbwjHXYYt0d0-6sVWNgBGOVV-BFN_QFMnUMYp-Gji0l9O5l4JjrntbaA3jH0-WN00z5780plGV-H7qUBNpfGZxIdobZG_U3xK6Sc3JB-w3yjpVbRxjcqnpDLEUVm6XA22eD7meq1uB7A0ExewpE8V71S5rUWaZNu_X7O_c-Yp1MM_71X3V3pQQhCq8rat3gWfQ73DEAVslC6Z77ANALlOB3X_QhkmFqLXLsgBx-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJN1G6oMLWb9uMUtJJN1lKkuBFCjgbDsLiDMGCfunzpKNsQHgG8PhHISI0xjW7pQ_UvkpUqk6xmlH9t8bDbHAcM2Jlb0q9vXLmdiPv-W9iV6s34WLvnKpnv1BQBfeCL4y4BRaq2LcjBYPjiSeVdTOPAs-MCkC8nkFvnV_yERA3Voj1kTOqv139jpEmID0yR9MzrKkP78dXgkCtcpMts8VPTBUaOBPoKBI4lJnY8ALnChROXrQS2mPiLRZuzccLBe5frvt6RP9Gfm95zq8cCzl7XyCM0AAtU0CuJn0wQv9RN1gNmIVdRWuriZRY49NDBfM1YgZ5XFSZyaXE8A8GyfJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwpbunns0ZdtxT1W14CuZ1bOn4e81y9jCF83iuh_C9N0jIGSJYAdBcos0NhdDF6gSv66oVGnWTpyw1uy3Qlwzt-zbOFSIZkpKhHcm2EMvFVXFSrSnY6AN9qOEF9P00qEAr0a4ToXn4gBMyc62Ms4LA6oulOQAxORSCd9TuVIfaCXj3_dJ-eMwPcr6a8EEPj43lQ2Ud6cB8ommJbJfho91ptqmPxuWzH74zo-SeX0U9_04cZhIJsOpIMN0pjC4gTovhGi7qAgdqwFVFgsZz-qTN4mxgga4UHvs1SpnbuatY1i18xLFlITq05-Y_lpXX_-4rMRiYRRytXwti1KzwodYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P56iIVGF_wSjXbvKMDbneSkMZIM5SNh3L0xZywgWVhfnQ5SD79xXOVQ8m6-oOh3Sv4jI2HFy5ZWIH3VJZ3m1MwNgsmiI00LwJLze4r5ukRlJ55aqjsgFLDkG14gx5mlrsOtkNMVTEwIXXz20C7Dl1c7GqQmEPx1A5aVoU5Dt9qduzaEzFN8w6KVeR0OZvWGwYmXkE1E56FgJ68ea2lpYzo3HAgNfjQ_sNekVM_ZFI6jB72XkVl7hNKRThOcUQ_vqcQ_Z9aZvoWfB0rZntcCVE4reQdd7BupQ8RaP45lfkadTv-SZ1k9IzSEykmn01FoZFmHQYzy119ZT3jpmDr8QtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Pwqc3XkBL6ElJFuqaVeTQiWTad1_pL8niaY1QmeuwlzZ1yE4D4vbrfOyNUbyVscpUFDn6CTFCXb0FOWe2Xy-BF7UFXUvo0Joo7Lh3X-Fq3k1IsC5fHAojKeGYDB0G1NLaFhc4W24p3UWu9RM6SlfpNizKhGv_U_k167pl7Fr93pqAwlYmbpGfcg7Jsp8b62L4ZVN082GkkxnucZ2MSSfOY9_kjkhXhgTP3kGO06gZ3AUXKmp8t-PJIbGbhdKhGpMKChZnciZ0Xk4thMVe5qoh8DkspPG3yKy5sBw0S984Y3OodceBoEnBVlxFtkpSFuUV5rtP3zszd2dvGVWjNng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uHIuJCU5wPEpwuI1ze2KyBQnVJdItriW-aS8A6oJGOmg8Vbp-0pZg9GeVo0xCqaMQ_Fft20z7TW2i0jPFq4KAzOaGiFyNowDPRndhVNSE-Y7pGT0xPFmolH2T6vqORdYehAIUZX6HrSEeLREH2sF6wfmaVRjFbCn5oASWwLF20lI5v__ro6hy_w4VgvJvPkhYMFLt7ylaPhVpvH85PbiXeQ7IrvSfKHD5WcRoQkMAcKrldPMk10AAa7How0h-pYQXlEJJVM-QFNZeu1Ie-nVUfGQTPRtefDF5vx_uMovTlXn-flVewe02Rbf_TjvIM3WVKtJzBGs4mE2KGudFtlY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=uHIuJCU5wPEpwuI1ze2KyBQnVJdItriW-aS8A6oJGOmg8Vbp-0pZg9GeVo0xCqaMQ_Fft20z7TW2i0jPFq4KAzOaGiFyNowDPRndhVNSE-Y7pGT0xPFmolH2T6vqORdYehAIUZX6HrSEeLREH2sF6wfmaVRjFbCn5oASWwLF20lI5v__ro6hy_w4VgvJvPkhYMFLt7ylaPhVpvH85PbiXeQ7IrvSfKHD5WcRoQkMAcKrldPMk10AAa7How0h-pYQXlEJJVM-QFNZeu1Ie-nVUfGQTPRtefDF5vx_uMovTlXn-flVewe02Rbf_TjvIM3WVKtJzBGs4mE2KGudFtlY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIWpp8Io4MT6MxT3enRrHRIMzzQchlutvStyC-0BZFGcy3fPOqlrVAeBNBxINhVGc-igEc0DM12wLRhJf2jLn19uQGgRH6vQlykvmufabJZK6X0fk6mtCexc1EOO3mnLuNw0jJMxAaM6ngQ93QxR2emc1wkGMhKP4G77PrTPoGn9QDo4ZDE7-wubfZJVUck4BTct30X7vh2h-RAGeBDmKt0l3Y542nK7Zb0iO5QUap2Ugf71vtodVFupj0rP5h3RoP9yRls8QvMVMmqdYI53z6xh4-w3Incy781HFcoIIMaL4vYwEFycOLoTTZXvxkjn4428GfLLJ7XvUCO4ExAG1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8SIVf8NeonEFUlQnwEX_e_TsnKW0B8sdJXRygOBt6Zgg26IU0zC7_q3Ac4D9qzHgK_tFNomVczxabdAdE32sqI5LBoNLuVt4rhNRTKn5Z8EWyWIv40m_p9dGlEmK4QKF_ADjCuT85zJM27vV5ZsVadhx1odzr9O8BlIMcwmj-mcqw58VBVXG-SzMP4c0sPqBoQob-hY7eMwQudupbPMjaxyWMuEmjgtCfiHm6YqNIUoyw0YYKsR0Pp0Ohw_SJ4kMoEjWXHXXNsA-5sCVWcAW4o1P3t9inCu0ag_KAebsjJWxydiuXkLBKqtTsimatAQewrM6W1v3fy5rjnE9C18uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XG5yTcyTmB5neYZSt5Exw_HH9lRAWd_CDC2x-0-I7tUvkdUqW3vtHCId8DKE9WSrYehrUxEmPEMZVwGnKaLkqaogTUDJ0BNh1yAXNDABnfM6KdAeGwmJHgd_ekIb_gXCCKrFT_iw1d42GosFu2e27NhcA7jeXSuXDatLrq0G2aexbM1jt5FUKq4jg73jalLEYemakeb2qSEHr0nVgHKsuidtl9Rs3J8w5slNcErqnaY1furx0l4mb5QYHu5IPsbo8XO2rp_628IGO0RSqGoxkP-dfzRiE0rL4j1Pc7N9G0-D5yXVXg8E9Q5PCWEBauWkMuNXcBtm6Cn-23Rh485x5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG48qh_6amBApHL8dNfudMHvcP280rTrjjIbYtvoaVWeQ29PVNR1vA4dUdx7cFc0kdazf67r4kqAEyT9kR48B0Cl2sV9YaUO9ULcypyTeBvFGk4J_UuJksXrEVOtyeVG5TBurgGzLj46LqU6b8FHaKKjmK-yfDuMFiNUNdcaMOlPn6g9lMPuDfQuWFY0cM29Dxo19wEajVS8NbJexRT2gFcTYibpDAqB7_WK_5eT-R8frIHNrzNkgwreJlPjhz9yCBh2M0LwJLBYZmqNPOcCL6e_3K0fwtNVj687X3T7rZ73Rv0tHZ9mw29lD47EBBNmYMAD0wfJS_Kuz9ExIQ4Ptg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuQgKyM9UDMnfW_1lATnD524nU56kIErRWzMhSfRRExjNe42PsePTdG1dbL65bu3bRTR7OFqmB-D65QXkgrHV4D3_QpmjjLHdxpFA1xK_ndlDun6I1VX9Us90p8spv-8j_kInQiFp9kGnwagP561_q5vZ6azy07_b4WUI3PZxDJo3W8FV2h3yZQ_1d9hKKJb_Ueln6d-mjFhjc51POrieb9ZB2vQQPM9AnnZrTBR-fAJy9UtKec8kQH5WW7USAbi3bTbbSvuP8-Lklgn3_ASr9lL-mSO0G6-AJYZC7HpzSpjygwj8SDTEc8zVhOmYEtn_8v6tAUstETp-swXbxycew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AD7JcCaCs8VZDns2TjdEAsZi4QLQ6EcgRRUgrnae7axKr2bKOVPOOhADlGOwskxA0u8ZgClh_22zzPtWvXrlHu6bXbBMm4WyzmdGitaFDSm4t8z5cniBWwybrhGvrjZaEl7Swlw2mGQ89lK85tGXzK08hB1UuWdxXEVjHYp_cYoGL03nqq4NUH9RAoYcIkxeHqUx7Xm4b4Ya9oP0Z7YvSUvwcKDabxodtDjME2jeuJ9URgCEZA4vZtqTWUSnqJKasTQ5sjm6y0g9crKGrn7fZ-WW_Ou8K2KeG5uvZOQ7--IUO7f1WvthpvAmW_vsFbF6S6mpTLoF0Eax_acrN4hESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T926NKc63xYSrbEXt1NobWfayvAbvh1-2f8tWmN6XsNUZPHts26cjKzyGM3_KgVMD40nWWZW2BWxgkcdmrpbg1OTXhYeH3Xm4xSluHDvubKJYF6Ad55X-ZxMp4b6Sxu5KmGMEDXX3Fh-qg5gvktr3Wi1dYpICLP2Bc61c_wiFUlBTW1rYEGsRbCsXy9FGZO0Xc616WlrmQVJ1F38RNXOfrWWjM8Y4Q6xFhMtCILISoCB28sUAso_isY-sDoIbmW9f5yhy0g94B8MZX8F_JBiQOcetVhtHOuyJHv0_5bC6vatgkYAJTo76ymkCX6QIg9ZvbHWHhy84Y9iP7tFVuYTUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WmRFtRgxP2Ae8bG9-pYNYYdaojWMlV9eYlS9k6T_2U4dfSAzuWuE24Jw_E2m9_a1E16wO0kPDyWcZKshKCwYIkCq78nQpDUqw_dX5-nL889QZNWFfaBWjEX_S1fmCk0H_fpQEgARHgFpoKrGiDSbpnmUUktfRJ6tuwtthMWl0PI-VjPYWOiaa2TSuquV2h_Am3_5MEuNXp6XmtJdn5daK-4ZKy7OaDqHXxvNLKPpTCFxoFslMa8odIPFfJh2Y-tkKAZ7a9vA7XZwGApe2cUjPzsBfd4vYuOhnDFbzX1e9-kWbEDVDtYvSDC9aYLeynxVq2TXGiJ9qy2HQOmeS8oH9bpJDXUInHdrccYkDwKiRBS7vaVFw-h-qiW9zKjjZyfmbdjCg9ogLl9yFaiAN9AADChnv53y_FZn4lMuhSjoOnxSeFXSmrVf8vZbjGv42Vqf-We7RP-zzqGc2bd-5OBvAUDKfVOHYDmJuBXZekm4H4KrmmvBd6K3M5sYnzf_ICoP3Rw7OxGmGsiI7jmcRb1eHCbC9g5jrNOA7Lurp9xnK-fJZAs7ympX1Kmh27GS-VRmxkPhgxWMwelShiJd3AcxHJOKv0cXRjkqLZrpboXc3uNehy8WICaoZCEjyJmMSrtOTCEf1MGSoS0xnSR2cZ1hUQ0Jegfj1EUgXopFhBIWacU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WmRFtRgxP2Ae8bG9-pYNYYdaojWMlV9eYlS9k6T_2U4dfSAzuWuE24Jw_E2m9_a1E16wO0kPDyWcZKshKCwYIkCq78nQpDUqw_dX5-nL889QZNWFfaBWjEX_S1fmCk0H_fpQEgARHgFpoKrGiDSbpnmUUktfRJ6tuwtthMWl0PI-VjPYWOiaa2TSuquV2h_Am3_5MEuNXp6XmtJdn5daK-4ZKy7OaDqHXxvNLKPpTCFxoFslMa8odIPFfJh2Y-tkKAZ7a9vA7XZwGApe2cUjPzsBfd4vYuOhnDFbzX1e9-kWbEDVDtYvSDC9aYLeynxVq2TXGiJ9qy2HQOmeS8oH9bpJDXUInHdrccYkDwKiRBS7vaVFw-h-qiW9zKjjZyfmbdjCg9ogLl9yFaiAN9AADChnv53y_FZn4lMuhSjoOnxSeFXSmrVf8vZbjGv42Vqf-We7RP-zzqGc2bd-5OBvAUDKfVOHYDmJuBXZekm4H4KrmmvBd6K3M5sYnzf_ICoP3Rw7OxGmGsiI7jmcRb1eHCbC9g5jrNOA7Lurp9xnK-fJZAs7ympX1Kmh27GS-VRmxkPhgxWMwelShiJd3AcxHJOKv0cXRjkqLZrpboXc3uNehy8WICaoZCEjyJmMSrtOTCEf1MGSoS0xnSR2cZ1hUQ0Jegfj1EUgXopFhBIWacU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzCsHZKeb28xZy-m62V1TK43Ozf0bI8Ng_-2PL3PdLZW1eDULHKHVhm0YzZZOSM2J94tdM8kTN3UooX4UZfWzDXpLn90egaWi_BO-MkE3OqIRvxmMMtVc668WVoYUAFxN3cZctX3vm7y2SHq1HB9lEgqSoblLAqjvHwCrrK9Id-5JXKE7JohXULxHjBkKcdPHd0SHcl-ZSMjzvE2wAOglWSPSRgyULsWkf-5NR7dU5rSln6uBE90_W4VbN57kGvh_GLVZS9m0JYifKOO11i76g8vXwgJfQCldBsHCEuG7ktvLq3hXpgzURrZtryZLEUX8rmGBe3OTeeK9Oe6kTPxFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYpvtn54MwOixxdCnmClyGe0Ktj7wtMwcMWYXLC3Pk-dG0AFUqZrvXn65oalPq5l4MWEKmW7j6V5CPGrwiG8_a10tKFG67ozmtd8ialTR__heqBsW5wBpLZWqYtg3bOEN8eWHoNZJflCAHy7s9kSypT00d_iT3GL5i8cbrkRYCJJwfGvX2kxqDLxiq1Zyyyb0BrVxaKkYKAOvvElDhoQDozc6fBWr5c2jnYnIeXNXQaz5R4xi67ZeDZQaATI2xEm_VijpdSqo6x5E41y8lfisxawPy4UtuERDy-D_PYQyI4taodJMWZ463-2zvLtyW6bKzQ4L-gi6lbEIiLDzkYAxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5m9yPaMCIiW8Le-MmAKxSbr2SlsaWbQ7I9TwZtsXIEau5Mdj8Ye2M-PE_skAKht6bZxXaB5szO_N7fhQF3NOUGfu5MNH1pqmQNb1O0e6ClNFMh4YUlWiFx9I41HK1mvytjEUGnuvx0IWhfF1kmrr4S7yFSdbta6p_bCxWqESFJGFXbIGGwZdgNT7fvaCnhhaid6pLvegs6hxRbqOL4I72XBKI1uvOV8BeZXtUjWDDYIWTto5SpCrP_hZCfJ5PKmchIzXUlkAArkfJZm5lA5oxgfGs8g-_PaxUqGCo3OMHXQhtl9agVUk8bcdwbBac6PYbDZKXdcdnqAp7zFQjhCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPdDA0I1M-ThBvF0hhIwdxrJOZNV_34nFSWTOR5Essa7si3kjDBjJMzhz9Qw0jpcWqzhMf-YCIWAdiu3nx79BaD8BJMLcnkWWsDJvESSCTm9XiVDDa5UQqShOeQfBcwRhT6mc9IPQM98pGFZfXWJ3S_IE2ykobtYjy6RdxX3A-rqC7VObLE7Tn-CKdYAgY9uu6Zs7F7jTfCPp1V2s2Mq5-gyzk-nwq87fugd4W1jsoLt7fsI8nbbsNzb9iDdlSP69E1SzSxB5zFKt-6ytRCdPvcAp3_BFucLA5Ser0c4SDKeueQ__WKx6XC_-p5BCx11tou9oqLQ6k9dj_9FWGwGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS0UmTKEFg7dutAunyL9z6IsfK0xJuufaWANLXl2BFKKuOltdZ-bZ9Mzqx-SdN6TjTXLlpQLwopUhumwnUTaeT_V5-QYQBxawXCLgG6tU7ELUwJbqytkr0A6q4jlSBkxLLYjSWo_hFsJKFsSHgPI35lYACPvAG_oel3PvskXpbGdGgIpOaRV_2Wl_c3ONc2mK1I-nsUqatw8qXpJ3wzQAtm_5XEwWEl-pc11dq9B_KppCenneChThLTLiziQCuhZfyLm7-vWCqn-Kex6G0cO5yqZmhtttTObhJyVUtSjGfCJDaG1S2RFjC-XGJCytwGY1uKG5ELjKunBlNNwzdmY0w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z2iBrrE1GqNqJy5P5ChMWYqEhRV2Dv_qFBEVUwzG4USWzGIpVqEvp4SxJsNCPVXNM9IIwl2GwHt8GHeovhNbbtIG078ijFWHTsk_M6Uaj_MAplYwp_GpFcVdV4VAI0UVj3le_SD64I7ufaCwvq2LqCR3fL-J0ppT_zX45uL7FIYXhixO0C1FnSMGDzBxqE5z_fqkRBd_0t9F0pPiVUsIXZxm14V9sEeBEIK9cCViMks4Hreup9noO4Zaas_4xTQMEGPscvvqdyIkwAWiM_V5M8SeGLGGIC8XWc-Q58dXjffAT1AaBmLZH6BZoV3wh5cLX0K3uRcU05ipjcF0zr8k2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z2iBrrE1GqNqJy5P5ChMWYqEhRV2Dv_qFBEVUwzG4USWzGIpVqEvp4SxJsNCPVXNM9IIwl2GwHt8GHeovhNbbtIG078ijFWHTsk_M6Uaj_MAplYwp_GpFcVdV4VAI0UVj3le_SD64I7ufaCwvq2LqCR3fL-J0ppT_zX45uL7FIYXhixO0C1FnSMGDzBxqE5z_fqkRBd_0t9F0pPiVUsIXZxm14V9sEeBEIK9cCViMks4Hreup9noO4Zaas_4xTQMEGPscvvqdyIkwAWiM_V5M8SeGLGGIC8XWc-Q58dXjffAT1AaBmLZH6BZoV3wh5cLX0K3uRcU05ipjcF0zr8k2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwfjAOznudAp-4z9ZKdoUYCvgYr1BIApHUlD9OArwVqA1xpqPgzXFCIF7nZSb4JedoAqBV1HMxWjRbFyYyCKy6zsD3dCfQoZk288pP6mfnacbwYQNHtabmUpajoWBrT7BDU7qPeb5aOY4a-WHyrkDOabYWsqLCooBHWTtxw4L6aR3El2xr4nk7u7QsLyFYx-1QkJRMHOZ9qX4TrgTvLUuIbiEWcXmMl-pTudCIJX6zFvPmPQVQBoV-4v9aLspM1_uuVa3Qe8nGMz-L-EzMdR0jhZ4_EcBZGYuV9qzSJtL--A7FSYdx7Sh8Dfz2ctcCyuz8KR1r4Vg4XlltqBQNl1ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEyA8rdWL5ZNtgEx5AGmcUbXXTvg9AlMHsv_KOpa2yvqSAHB3xd84G5lUl9poXN_0DI_eXk5iQ8XBGJ6gymF_FNCfFX9g2yg8yVRBwg7OTpiyPDXK9EIuBbgHuVERpRIakHI3ltVMoaKJqYj9J7FuU_fbnu3lDo7TBPN7-MBreVfIOYBcWWB_nx36fsbP5rSPxlKM5I5-4V5o19Uy8I00QF21rlE1LQIO6SalUO0-bm_fmPsrmu5Bg5bIDIFoAFhXvY3bG3tHawFBJC-N_JQTlbTGz2bKSe2-teuK5GqnrUzJ4icAFD5KvUBHGTgQxbIlzs1-gcUc4ljxnWEegneOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrI7fbNcyJPvvo-4BSi5Q23erHgMRZD9k4RV54QEHNSnPuyz5lOEAiI5Y6SGuNz-Nio-tBP9EdA41hhfjW_5zCfu-yGvejdm11811TdNe73aRTvv3ALfvmJ4so6WBzDlPwFMoaGyDIqbP0PAVc4RK1zhvUgxmpUvr3q6yjfVyEOklasj83C3FMIq_Oe4JLdiMHGGeUA1t-hqO-DzDIRwMP0JsFCnCrg_WgvTLIv9cM5ZgwazZrkd5kFehYFr0ZgltCy5N8imY7E4pOD2G4JACjV2ERJIv_j88mWelhhl4NwXLhLeGM0slGQ_OOlo-J4UqbRYhrOTe54i40Xugs8PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8mwVgULA2LzTXXLqYiHwZwuZZz5D6SElQtNDK4moFtJa9JJFfT1Iyz9-XktjFt10yxAT4inb4nipdxVjXaeJgqpMCUPv-sY5KimtbDSEH3J5J494diYXrfd8eixw81R5XhiLkdDqNCm3KkKj-hNhfL78FI3GANKEWRwE0_ICiv5eJ1Yi_wYQOYMMe4lXwyKWLQOH-NZOTSe_mS-k47cOw1GSYOYathJnUwV5j9vBQLaLOrfLoGCqG6wJ6CTMarKjdx_T-FLpLP6AUjkY3l8LYI1hCiqY4FtmgiPuL2lq_Uo0h74RlUcGFBj-cVI6FUMMHpS4ZxWaahku309W40l0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhuhNgNm7vZpnUnquT8w8u2EMYUIX-UyzIyxHLLZC1aU4s_6f5oWscpl4I0OaLHjtPsq01rRhJkugSOeoJyFJMVdR5IOpMW81h1_vSy588lbcSM-aBoFS7BK2lrPP_e0cyWoDFArtjcHsoP16TGv_POWLp0HvV0nLEldP2W42hKI5Pe1uO4_MzvU52O6we1QUyAQ_CaMIz7CI0h4wM0xsKzQ3YLwfrLqn2wVk3wAlcS2SVInfU5kzSsNFjcuC-t2RrawXbKUos6BKV2lHJ5b7JqhZ5K2x9ZjNHOtz5T3TpZAmm1mqQ7w6l6Dl_kMNpu9Qm5oR6g3Wq8-PDOokF9tRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0IovfVfr-6e4zU_runebyobo3tc-v6xPOzhe6vcKIMue1YPxqU7jSfnpFo2N8zPIdo55DVgim_E17HP7eKLG8Njl6n1Ohhz2sRKJuX8ASQNEnSu_qKuIO8emQ4ZcuTfvCQH-Mg37movPzXdiRXDJyCU-Z-geUEwWQnGFSV-vh2jOQxftwOTFO_eeINwjlPC2P7RMk7EMru88iTxzwnE_05b6D3h9ZtxCLBZW7pFO5jpexRmDaToWBEs8VIXU0uUaUmF_dvSTcMaGrud2yNjIR_3YAuPalWgZR42JAkX3xyakYFDgrUmiJcLP26Fe2IiCYeQbgZ3AAkX3dnPPj8J4w.jpg" alt="photo" loading="lazy"/></div>
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
