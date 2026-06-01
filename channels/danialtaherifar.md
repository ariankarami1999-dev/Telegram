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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 02:09:51</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 322 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEGj1W6aim5Gn-y3O9pmwsGJXKv2sXtYdXJx8MUIEe3uiG41sZ9EfWnVCRks7B4ybhVfQye1b7HS1uYSisJ1AZ9ZlUEhuq7S7JFbrrOb60yePAdHd0E2MXRSpk_D8s5G9M50kVpiWpfi17NBzOjApkN3yO5pNc6Ug47QAO3TRcKtDUaUyFPgQ_96RdY_RkAFmgxvEjaC8sei3V00e-46Y4alUDQzES6Ky1j2E6G1ypTzO5c8l-kfft7lJX_3vaKx7pfhiOxjRK5dfNy_6aDVh7zXt7Bx9CptK0VfBBnDMvTQrmy2RtB6HswU45WfgKQJZ98Y_wGeb2oOy4grOTEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Cdy7p45aknlPpI8TYDwZMO2NDcFSzN8t-MWaA8zjGprP8oOoB520wnaTmiv9RkrMATMHSZn2iF2F9hHGbCmF1YCHbTJ3ZaGL-lzncbUzIaRAsvA4p9_ELXlLP1l7mMbnYuQX7j_1ND7Hiob3yighJVuhHlpNkrfKk91cIWncAD06ahrWCym9DmS-1aPY2RFIYCbEuRwbSELF4UmiG-7n8WTn1eg1NmaGe_NH5SRhqcfccipZAQU6QgI6coJFCZKT0SXH8QRepq-CNJsg4uXxeKX3ssmOLT7O0G_MUkhg9KmlTSMcqfF6MMAHofslAXtmcJtpBVbVrHYV8Hxtx5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 890 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vREIhl3alxEfMXXuTEAE_Wt1NwVdkkrddw2wtuii4ysFgx775W15Wm1y89QbE9UgebG6vNM7Xb8Nu8R3S4B8y36WJLfpDCvCS9rRubbcDa-Pn_LKX2rXpRe2rwqeQH48-KvY0olu_00Rd2ykENYtzevYbCVThVMdLEFHGXjL9Pwg9Cw-nYVG3awOSe-XpbIced9tkGOgem6pDlVEy65BlZmNeYpYRmh475lWlbV2iwcfzeVo8HJu7bQNXj_sEMjQxXmyHEqVYdJqkhsZzl1QIhsCS6yckdp_iMeNVF9nBNEvs4Ob05yvqX67u7pD4iR4gl9QxlsNE1i55TpaFmpiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8sJP2tajyoddg5PhZVZOyAXCFrMoBNfDz2ke7lLk9jF-4Ehsq09HCd-RkZO9FmbZW3w4U9odt4u1j8h39Zz0IDH-EfYLmb4wtvXzqrwovwN5GmR0bPrrnYfwgMfCu_ztQL7kK7Q-luZuBeilsexTwKLzxIFTtOwGPLpq6fsJhWFU5Kh-VIxeLB9AED9YfNrrcebRwHyqC-efRxqDrXc3Vkv6T56vki-5m_oCjw6TUl2yY5O_AoX6aAh1TnLdw1LzK5v_KoXq2lUt7rrQVpovQmbbmyEMIEdL_UuH4SIAfwK_JMGrAW-LaHLdz0jN25KhCT4OWXs3zYLewcVkyy31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-footer">👁️ 864 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFy8-BApLb4Et4uiW6T53Mpz0-XkM_gXOHp4m53Q4RhfCvb55lyK0emWup-E2rNRxtPBahEh3ahXN6TqeqjFyFZml--3-GftZSQKt8dAkwLClZJZa6VDdBfNhTeocCiFSPRt9Dn3V3I67LuswyoKI4deLm7e6kQd3s4M3zTdGDEqqidTTwjP1lhHG_GVf1R0BfRzjvUHi8FnTD_ZX8mCPOm7VL9HsQQ9k8gpR4BL5BxL5WrZW3vkiIA9LXnvhb4XCanna3XaLDBfEr8yEONZ1smg2ZorhqwuP_WqngU-d0B4iUsacRfupoWFECgHS_UnlvtItIOVJmDzxELB709IbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkENhETe7Lu4jknpc8ATCK-mQ4tgi7Su1CuMfjOEWBCb5WMmhS2A10-fqccZT34PFySyw9CWrL6Osw9JAzbhUR7JdZn0OgJxpsa7Aq5xHQuUf_seE2c9MtNaazwGj3sxjO1vaghtGPCApAYY2yW_la7RAn55x49OrC-L_RdUHTH00mSyhxkxdv7xbbsUlsT0jZDpyEkFPc8h9GvvJoIOsRgcplV6nQUS-vtnhAYzwBzklZHN5dYm_dF5Baqyw5IN72yFhx8T93Y4eQ_kQRkElgFkgOA3HnY6oBrbwbKiAwJxbmCImz_KqDVEY9JWDnSlfiP92JXyxYsr7yFf9YDAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAoG21xuwvJ0kkjg9gbEk2a0-UgwNVVepIZ_d7OIdope7NgL3nw5cq88AHnBJUx8Q-7sKCadCX8x7kGncXufnqhMLnVqfZUpLfQZNgYD7xlCuACjXl_JGkiyt8iy8JYG7uM-8ZxjjUgVfrkTosFMNQmwUsyeEuzCI6Zm6L77Z9FedzfEMlIshG1ODhj9HFlkIVXjT7Qw-SvLQr_hDoNCfM5SKQv7GryoIDaBI0PmEBUMp9pH808h61YogzZGa1R6heSA_ptm5Q71tWvk0V8xwnSE0wFKylm3M2ZtMWjQvi3hypparkR2CWPFSUYOfcPTvOaDx4Fk2jQUN92nK5_lIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reku1LDCGnXyMnKlRhIeGvnS_u6wRw6xmeR0euwLM7ni8ztByefTUbC2yC4_pc848IHmNyJDU9vsj4Pou8cOyxlvMgHzwm--1SDVyrZX2BccZnXsXkDEdsb5y2f5qVjCI3Y2zJFtc486l5zuDVZn1BxYSc9J4MigRpQBPdt1pEaKlq7X_1p_pmkkejkC9G1TDqJRth7T0yXG3jIVQVcP2lxcu-FqZkZ5f8PtBvxg8uKZTYPhTnQhmY377ho_eDV9SdrAHIi8PZdllY1htTwvpJkXAQ6tYM76mjlAbPSHN0vhEhbJJk2Q4cLNqFhgHBCrEyljjYQ7yXHQKcxDGzHwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnqOYcbS1tuPxQtzLd8kvnfeNwD3mM_8fUm6gLY_cPuJHGxLlIRcaOWt4-jH7aOpC1Ok5jMy2JcZ_ziKh_Cw-uJOb02cSY4Ve8ODg6cmPlS9Wcep-NvmZHom4x7Be-Grelbdd9hfTcIVt96BSMGHb3aNDi9Ix5_23c5gi2u1k7HqtB7K1-Wf7Hd9o4yBT7_lXXXuXlwzv4jpL0PDUCrqqFJP0v_MbJo4reAJ7774JPEeSp8J03I7s0sZhRKQuUb54Ds7urpazs-jRLwdLFjXwFl0-TG6BAVc1_NGzbozCLR3SSHUkMcWRKHtaFyfVjqXEK0Ga5G-ZKGHsa7j-E3rMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZRN0MFkJzs3wZxlndcDjaqV6PeFbcO7-XDUQZgnqKKX2btM97g9KSd3dnoY7fDjGSkvYXLHdb4-IRS7ajUbmKXXN80SRG8lreHqOtpWwCG2DVzDhSSRX4uX3ycAvSu4mSL5s1a6a4MzeYVip2Gc6lzvXZq9WyHQOsnx00liDcmh0XuZOqgRxIBZPweRAMuLJUNBDqauo7j-l4DzOhhs34x4WO04lzPzVjTFdEC1kGKgh-Km44tfxi76SEixBBhZwZy_ANuEVKpESL69AgMzsfbHVE2Hl31hIN-EEmgSk8ca5qZHW2_5C8xlCQZvRBrKybgHeYiCQx_AkfcbHLdriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVQ7_L6e8Yi6PHZIai_-UPofFssNMhHWayQsqR_YStzG8TiaQebY1ecogYJg8yCyyb303yi50nb8fR3GVLzDBxeYqiUsvgiXxobMa1CEGtBVBDwRsQPXKcwCjZI5HmhbBb523zOGZ7ea46cFhP9CWL6-MUknLgCh2xGRVraz01qeoSbHQ14dvfbykyqmSbubRSMLg5evnd8HFSGagfTMZr0lSUmrOMyyW9s6pyJLDkMnMzXLmQDQHBQfIZt6EFGFwZQ0CE5dm2T3-ZUh0qbochEBg4QabG1SArEbUnrGBPdzWkyAmSWy0zeKcwwZadEsUmAsBUqbwpsGdHnlXS3xDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOSnuXY7LmxX-iWMqXTjycgWPY0LumqzsKYYvoZdBF4I5XL0XfsqmfhxXivMYczAUUOqvRc3dqn1PD9PvRtsE25CxIzoMSffn71NtlS9POMJWAPss0IKlc-ZmdjctqGqxz5SEgpIWAq0A43cOyL4KuVVCZnqVH8WMfYST8NuKrf2H_rg3gd7354TZydQIpNIvxHksesfJMNhO5HQamwzWs3GRqHEdhE68-W8hccR2FCcvq0yKl7g5eTWSajEuLQ_OkJylqbUoVrIjCezZowULgcDevptpSb6ZbZbYCXbXbYGkZ31tUaF6pdKFe4EUlRz91PQ5q8NdQVqDp7dpK-jtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=tT-UUMqjwCbFZV9jhbqpWoByUHseeSCSqdrLRXAOmeoL0SzravehFPuErN8umLfRHDW8G7ZjHaISmh4rom6DxwHBtwqHqBdOMCjXk_FEiCGyhs1LCW8cGzRAMJH9nMD_jsZDWAWAtSAOsW8H_qI50lWnsLyGTjfOzDMKH-uWv00ifgHGX5cOQqYBL6L00bnRL7SEch-mjvmXXrTKP_KkylgxQA4dvLZURGyuL3BEw-52-eRnEYWsftBWqiUud-kuTYaZ8P3RG7iP630WkaGyDk0-g8iC7op8dHrMmuD7IJhplCbZGlRUdto-lZcp_GoYkVNKEXQ63kl1dwVydq4JpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=tT-UUMqjwCbFZV9jhbqpWoByUHseeSCSqdrLRXAOmeoL0SzravehFPuErN8umLfRHDW8G7ZjHaISmh4rom6DxwHBtwqHqBdOMCjXk_FEiCGyhs1LCW8cGzRAMJH9nMD_jsZDWAWAtSAOsW8H_qI50lWnsLyGTjfOzDMKH-uWv00ifgHGX5cOQqYBL6L00bnRL7SEch-mjvmXXrTKP_KkylgxQA4dvLZURGyuL3BEw-52-eRnEYWsftBWqiUud-kuTYaZ8P3RG7iP630WkaGyDk0-g8iC7op8dHrMmuD7IJhplCbZGlRUdto-lZcp_GoYkVNKEXQ63kl1dwVydq4JpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry-CJopD-nOf5inkL_7kay5W5NNFDg2TRR0KMxpJ9sC5RDzk4YCL0yOiKqzILkmVXWxiJ0RCrc6df8QxFF31_hBt1xyM6EoFGEs59gGAaLUMjkS9iQUJullTNV5SgupCSoI0PH8O3fPPqx4kgvmPV8UgUWtGhDvPqxA4uAEp-35Sphl_udDaCFo4S37i8gMO7kkedE9huXAM0u4-Y9f0NNk0NGoct2CqMpJk4RWnsQDAEFWCD5jRwRo2nBodWBxVA2Qe_ZmvHAC3c5xz5AgCYg2WZBluf7ZnwmrrWWnx3peUVNC1v7518NcfthzP-tE6MomZzaB6YaT6yD3U8Wm0LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZegX4XExQ3nGVopyR7NaqtOHniHFQ9wIkZsn3iLRjyaSDcejX9AWS8fkHUGObRqkJQaN70VffTXCvVCRNhIzeqy6mc-QYD8zl7qvHSywyT0RXpOQRT4lny8mbDTbaDZB1XI99PsVUH2zM6ub5dwuKWgNeYzbh9v0tI94bsZJiumF7EXWBF_KBY9HJWoRuXg4t4_mXCuB8HvCDTQTJPnKA85oXXk9ROfEOV1dZhTb3T2RN3QFf2wnkKBlvbRiLLSJQNitDV-HuW9j6Sw_zkm_EP0p50Kj2LgJggf9su3CV-JhmyN31uKbhtds3onIhh4hIoqb1NpOlGuS8o-X_FV4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOCffzY8H6bGl6i7mw0tvP-NstC-2hshYrDea5b_kF4H7Ls6pK7_XIifYijQ0OUpNBWB79rkwiLo_FM7R38KYALwTHF_8fG2NTaHnStx4O9Dc4jOnQ2qYrCOywBnTEXHqIoJjTwvhC9PWPNwQYNYvZPyggYorgB3MJsOfwasRiJxfOH-uGMpclm01I_4WwZSlrj4tcndEQs4mK4UJrv3AqWD7nhJaJRnR1cFMNrx_N1nNDn1xQmTVnkPhTV8ZYhWUTfdxo2vmHlXbyYaRRupFBkfliMB4eB-PLRyNV7nO7icW63ydryzT5poFiwgBSZ_hgnatPOEWx0a9pNWqU_yPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9Lo8ldayTJH3dVdjF5cDR4m_ujB9Q2gwupo9FC0CBxOJ6eRxJYhXzRlhvoUbEzXIVuSjxOVIPETXjeUHCMwkgR79rrn4bhhmctqnGNbmuSJg5w8e7Y54ErkhRadQwI178NWnbkazEFpUgxfkA7Bab7A-dP_dcDWrD41P61o_XC_2M--WAgZon7zYbHAHQwQ--AEtba9_pDRpJm66DVLkFpSLSYt1D5BjGCZAJjn6lZ6aQ4F03TW31TdpqX_FMnuge2hjvFItuCfNcXAZh3FQmf3bPbPoYXiHDy7bbZ8Gh3juQsUwJ5p9dmj8xjDD9WL36AX_I-0o_E_3K7RashRXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8lXwDZnoHQC3RSzo0eBVrl7wAGw9Nj-ypqzdaCNINkOhu8qcrneE2LAcb0wEERr_mnyLAd5vjdGmb2EpHf1NFPoEf4qgBmyOPuPMhKvmEGJVRpvZMYK7F33nAgfM7H7oIv15RGcnVIlXtmuOB0S8GedpRHpAwoGfGfIDSNlvAgOsmYH9KdS7F9LJYXt_3oasx_CXmF4JcqpZgbPVledKPQuF3UzXOGodwJ1MzPX9nypRYbm-dh985KCpzn43rWfKFLz2Dofivd1KNoEjDcQMDOE4YKZpmxB7yvTw9Mg2qbis3maq52MVa3gZTAVKbYY0SKtDRUVSXGEL20s2vBS9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtGEotcaIwM4v7S0tCAHv4d3FJlGvtp3fvOIIX0v3eL2tTqKz1jw8dDY7_ZIjzKp16_mzR53q-ZMnW06F9_3AK6SPqT3mYecaKpehc2mAFX5NPO7QgDNlVJfpAtC3jnHkJ0heHK4ZW1DeIiu2zmhEjJpRMI0V5B7gnF-_vmZg-6LdxzqsCLJvLQWvgD1fUGSt2ZfJ7jPTpVX1GPRakBHWp6rskEV2Mawldss9ttAqYCXhBHW8nc5YECFm2QDoSkuqN1s6AnP0uNJnn9-HaIvJQIHr2nNiaBFIE_2RBPa8tym0Yv5SZpNa1PuDuO5R2CfOh6WuitwERMTi7Az15cyzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-Idnlty3fARyLONYd2jkf5eryfqK8a1JW2wOyfMG44H7Zh9KghdOoLCI3vdXB92aQwqnxsj3cMCZMuJPfJ0hoQWws8ZfreHdvKtfzyI6WbKYJuk3M2Xv_oxNpzf9QIE0dgwnx2sRJZ2ljjn-lGH_NMLLZXD7gpJ6Qx2ts4ft7Dtc2tvYljqBYuOehhEoEFzuDfyBuJF-0Trs2NQrhit4pu3JF3v7TC7uL2qrPRbHNM7sIhj-SdazXfaaNyPIV41p_ggQGmBmkiOSxrlSFTAjKM57U89xp_si9cdlo0xud6sCebVaWKGaVoTKoQ_-yVAgl4ThNoUm-mC5I3xlvBAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRlqAAVttnR8yLSO6FCewh1vl2zLEBC55HcfEjRfSbL2La9ypJYx9FShZGkbDIyclNcccXby2WGmaBEfVsVA7bE1Nt_CNsfXpWRCs_vjiV6PZkWNvKhmsmyOEvqh57JcsVlw0B7_Q4oFQ8L01f6qBVUQ-hMiLGgL0nNJZq4On8BRLawGwNU2MJJF9nfVCrvQakHFs2w9fw5Ek3R8i2o-yjncVQP7-zM9ppw1dhveWWpg5qOGERJWfo2D-XnlM0hJASvIO8_VpzUsu-yKcWZeWdEubz4YTLxNkaqkXrM6iMiuOdDBVl6uFkiJaNaqeiMppv67l_QB5PFM7lVbJiU0Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbY706YiqdtOsHqLJmksmA4nPTW-5VV61YlYMHsNr7k6lVgU_mHQYCZl9Zep9JCShFkwksTlaD-EepJ4BM-EzRmUHyVQma9dG_q2aIknwZTYqbEoyo7x48wDHXe0NtPAHKjnVLzQ4hAnl6DY9itzKNHgTmL38hKfRqcq4S57l3n231E9i6AxU1cUuIfV-8SXp9uyhPjhUdTEL8k3uOycxINBpoCg5FVEzkDfF9_lVPivfCE18GlTc2agifPMNe2rfGHXlDUqeMNZgOrrDz8HYYRaEHpFjPnINV1rgpNjkvRl_A4ykuMITfv51BRYMgzQUC1aI1HDNP64q1dQVhYb0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAGOUP8uvFODTZafqBZK0Jj7mAJIvMxnmTZq6kWN6PF_xmbtgr92YPHWjrcHYy8tEEWq2mmpKaMSQQjUs5QmWwLgSgy1A8de-2UOPuANO5wJcnlUiLv1daVIbMiihV2We0DYrxkeiAWH68r_qHBU5HB_iO7F3LC6aVFLjykpt_b2GZdhKuaXG1VlHv8-jjPzeiZTDXG47zKjHbGxPa8h0LCEBsFQazZuSzsdOU-8jtaTg8qqz-QUC2zAXhxJlq-Nx2b_QOlec28hM4AnpY6pMMbxtIQd4SDoP5XZUKClWymckZBunBsOaNHvlCSk5kqEKJiAjw9JkX5PME-JElJF0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfrxuQiaJaBp87Yje3k_tf6-caQD1o9AspZPJaHyBoHgCBAzAIwB6gqQ40sengA8eMfeDYmelebjWEuN92Xig53Ax1BUs6pItMmyDbTkcGnD4RUuY1rP_4RM0UKGvswgsx5XMjt_Q2X6P1h-WrCV4FMR1QKy-lusp_VdSiHTWow5qcQNRD37CmQONBBfdnOMDtup2O3hkX_nHvEDjtO9COHfwbBIdbL6VAuYLF_UyT-V9Q9WBBs6SKEuC-WUao1TNoTuA8wwaa1hP5EhAP4XTzdwljbuL7VHus8kGWzU7DJIjj4-pHwTREuEx0o4veqL68Bjv-K27nJJUVrZyaeSPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqYomZeIBUyYZP5ctLZ-SrCLZhYP7PiNt6fTl11Ctp3sJdNP1qhnpZe2cF7elEqWXoBeyf04I155ZltDcc_dLkZV8fqc15Jc24DJtaXVnXnfzDBm0opUeYD_t8kiV-d04hvs6VNfv4EY1m-XMVc_RnCkveMWcNTB6VCou1qn0tAmWf28nQ6e6c6TKXmHbc07NaXbnReqnvcn7dZziZZsSUF7ddzkKXkTUyjp30vTGGDDh_LJYqSqyd9JkVTqkG_cBrxwK0qpaUvLaptpSVvmFvshJY-8RSSSgME_2q7O-wV5-H2IWlGQ6QPO2MZImfKPNXbmx4gm-x0xb8igNNeAuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWCbn2MTPpwhZxd9TTneIoR0crYN369r0FLmJPN7Jo92gz4fDWshbu54aUCI-INkUbaLbj3LQGQ8qPR1z4oVmq__empmB82hn88tBYlJbCHeg4gfFYkLxViscLoUZf4zdH1YSVjA1dpVySb9-8km9K71Y-EKu2F4hBDvguPFBAWqjtECo8bAFwtXZOMREOf9Wo45WMz9XGggH8khuXrznpDBf3hHCaSJfNel-kPIhgwar1CcxmhpV9kWtb_24SBR1X3E8x6B2-Ky7Rrji53NKonf4-u6f5Ofwrlw8uGh__e8YcYlMSUt5twZIClAd8JzzJhgKg4HzpfOS8Vp49gNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5FmxO55mevUsIxJ7cIza4e48dL259qFQjrDQI_E2FGuniLURlTgx2AMk0T6E9Df1TVt2Lvg0rfBHzKzC-7TZ5YCN94yBNqoS6V95hm6lLT_0_Mym9f8DzN0vgJ1MhOIYu81L_tkMNX4ePs2j1X89gnQQmvayelbEJl8jYgYfoeEHX2VL-y69BnvKm_RNBCXk3YO3uxQ0rH-qfme8wr5HKhCS65DkznHQ0mF310AmUWVPVrr7Zs4x68JJcMK99keBT-CZOc9ZHUMbPiu-lX5JR86rKzkzE_ISI8SMClsYtbWq5TQAn-PKaQGf0U6gUAfp-JsJNt2f-RZM7uWpOjJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLM11uuwmynZ-wRDFhwbCkrqMdZTlfl3N3pGSXPRvIpWvhyKObFtr212SbkDyCfMhE4IhavbwfvWUU9UEXCdlwe3Mi5-UoQ6b70aNCc1DGGvP10mPhfpuZxGfilkudIBVZ_VWAohCQ1kGUTpdqVuGMXQypDhaUVtq4ujtUf9NKFJAS9lqQYlFtmMTehhqC9R7E51-ONPZ5D-NDuJGOUrJeYHP6FIzCGIlFMOA_4oqeZwAv_ANlffLUyedlH5nbZUsDt8axkk92KqnJ13u_IEzk96bBhTE64yRO7QoXmeNEbsIg3cRdjHrA4N6-HczZfpEnbc7M6sNJ-4ViXqQ0iarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcGdcvhCkiYidpeeiSxOT3LNa_FJXMxPEO8jb-tgwF7-ceNnnhUTSnGUlJEBx2NIqwRWsiFg5xQAOJ2dhZp9LqRDYu5W9k1makbIEggWMi0PI_GUnmP_7cAcFCkR7vI5B5olDlaOyQTitLDTcfhi0JtvPKJ_XKK6YP01XWBgyivew8GUTHBeu-lPDPb8hBUdmjASxMNtzay4MYwPHijXhoSqzJj19pjI-qHJ7i2C6w-i6hRWb46cCVsuX0Pwt63_UCgRFS7djWy_D9-TX5Zzu9PvXxznQEKrvvZPweyX_y7_sftUUgMYbOhtiT66DGBCWdTCg9Yue5Hf27T8tCmA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVASUavnKIJdTEMFRJL6xf0FVzy02FGlzBk-8sGNo2_7PXFreWGcx6-smXCrqS-AcRuZV0wctraTOt9tdrLxponTPLsdJ1AXJJHyZ9YChcm-4AUsM1KvMzRYCoT1UzKc5jADiX9g8lUfidaH3nxR_QVSYLFuqnodzQFwYL2akahi4t4M3uPAuEQocKQc-tLqUE05nQzBFxgtgOLdXZ4FdT1RoCRIMJ0w4_3jD_KOzVvpjBbRRZ3BEQY6D-mMGtGSO4BKeviWNOUkNkCbz69ySTi9k75H1FMVnqPC15sxpdjtoPg7ovRO0JTYZ0k7WHYe3TPvL6EtiUQ6dwDz5PRIkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtZAUbf7mvisrGbF_2r0YQqftemnAm5uPAH2ZIAGmt2ZFHDH4NB5NfLTlrHcBb9okcaIYjrNyAPEksp-avQB8CjcWYtm-K1YKyS-hgXiVTDI-bQuh2YH6DcpHpsYUSsnZchCgVuQ4J-BQ2DL_O3HxRtSb-DSbP3f7iCyBVbscJmcLPS7IVtU-IH7zCROCBz49oMWpY1JvHkNknGQ_TKjiQWsQ0KjuN7oFb46kVY6sdq5unFCKfrK0mmAJPyJHHoCwg8edYm9tMrge7YjeIc4Uipxt1sEiwsZVuxu5VQdlPdN-yTo-VwMf5Yvy_9QbwCLpjG7T4thw5rsAaGK_bOf9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPLhAoQ0rzZiAOf-K5_FUe2t8EZU3XQ_OXuExFswv3x-I6W42dTd6aUrDagOvmlFwh5xPAcOFH8-GyJE0Cs3w5TsU4KNcqDIoV0hmwlDQDBuupdmESnJcXlTaIYV62-FaR-MGBa21pRXxS6O5LEKezPWWhwmYSesXcNgJRI42-wZ8iOftjxaFXu18SwCf5QV8REdfuxLRmIE_Lv-Wy8_AkzhUid2V0hNAdN91NB-8o9FcCByHIK2T-ALMFMqaTQdRhZkF_e9L-uG15tiTj4Yw-MmIAXF3X01G51lJQcetcSXYP0H0vRzpDsmKhahVN1JjVvBHWKTHc-D6lJn5kD0rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOepnJR1wX6bT6dTOhNf53Ab9UksWjSZNbghzagQhPc5JEe3gGDRdlb9Xppkau0srZWe7ekhi5uwEox_3RFv9k6NsOZ4w1FkcQVJkDLwxDejRwwin1xc5d5wN9hGAeBPs_Zn5XUIPexjA23XScWUyGOUmejlGtpeVV6uOqq1XKHyNmqo4LgeCgU7IklM_0Au2ztk_8Ss5MRoqXDLY-0O4m4E3mg6UU54nHLOjAS-y3GsYsgER81QTujw6QdQbko_FrO_BC-M0KihtdPXv0AJz8AK-EQuGT3FStzENen20LVBK5XR2Y9xfE8O8at7JydlX4mnnv90S9tfxtpA1utNYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3VFWkc7Tbi7lEpYEui7Bo70_6tmpn24GeGQQMyW48H0vGr9QkB2UlLqaXgqS3gMzmONoX-Fk-JDx9gnl-cVgk6st9iAfRI_OapVRL6Ot8K0BxM1jhU3hoBAk2edPKzriCw7S0I5zgr-MPrtvvaHd5jfE69HqV3YyeI3TQFOgcUm76jQhf7ZXKiOjTw1qXL1vfHWuS4C1Iz0o4Vs7s5Cq9Hh9cv1TqZaBcHpRmIXSQqPEGzEKoYeltTmD160BdPR7v5DNzW_nsDaDR79Lv9rU0aYBIx3R7OaOOV4s7xuedB5zsFpLm8c3kpnXx7wuQWPrGc63aNQDnsLwKDNnG1EUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxKxWMm3PFi0qOrN5o1N9kguYXg3r8LpbiKXEcvpBOXRwwrlHIR4rF_YL6-ApZoEga365PYCwwMSpx1dOs9yQcHF6byKXChWnIWjIN6tZr3XbuYZ5HyhMuu15vuVhB7lJxC3iQaK7_hykDPzORgJ0wgM70pv3FldWhYgARuS2yvd4htV1jm4RYJPYRHBvqK-aJDx_5A4tYUXIUCKbKlBLF9WRU7Jp5MyvKmiCwXVoKD1lxv2EwgUAPYyJcP_UYLNZFhv2HuzIXZhmguOyjXJ1U5WuVDRh-MIYOg_IgrePnJ44Bt4eL4YxOB5aqu1ZrwX4uOYk340wJzvSiurxPlggw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw2lkMeAVPV6Ogo1Tsmi_6YQpRI8l7UPMNM8hUXgd_24ymutYKNRe56E0TZlVwbFe9BoeUKLx7enVKfcGazKub2PBFVi8Ag9Fl_SSJVDnFVl9w4jCreZoP7DoDbS_EslyvfqQR_uRoZL0_6P2dPLd3SGyXBbVEqz7iNEJBSlA8sPb53M1sO3_hKvXeigAhZUvrhnntzCy8vyqfVTaA7k5R2KMDgybvSHWhIIQyAv3fozPNmCHP6QDg2D7Y1RgR3nPyzeytP3CZovBTiOCloK09E_D10ygH3l0pDa998nnYfLySKNM350W6mSWbYI33jdsMZzDlo5rXvOAfkwm2yAvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9soAl7oJR5Vzvw9tbzTOXiPn_QRRAI9V8XH2UDDlDqOQXaE9rRwIhmHBhK9nre0DhnSgSDDQC2FCVrZnZfvm3FwcvRytUZX3eWQocLJHver_lgSTRktcuTYkVmzEHOMxgob8RQdNBEuNRlBrdJdiaez-IFwoqSDlUT6geE8Pg4BkP4YmyHSSxeyeynbFsXpU92_Ec419tccfdX-nYGo3VWKxclVlEJcYjofFkwgtXQ5K3Itkp0CmqODKJeWmU3sqqViLWVtazYyljlun-MCXoM-CkEoqGdnDmY6egOa_Z4Rh2FartuTebneNNUaXgFiJGHVzkvXdENa7mX53FQynA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ip1-1VfdRqL3ahonQrAdQZRW8yNl4pSEQ0tsx95vKmqgKww7lOqiaew_PPHXlN-VuzI4TqcPIfZEFQr8x7DTTbEozPuQGHxaQ2f5Au5ZIPuraRnyfIS8__fks3mqWArYt6xgLbPXUAVZ54Bc-afjdaBR7ZrUmitb0iKsKPSKqFUOFXfaijoo0BQM8krxaKXZ7QmnYJq-rtdHCWCI4IoCi14KdhXfC_EH8Qajs1_sqQlDyRvk2SmyrUYtzZcJxhAWqa0Aphh0mMH2nitOL5YDK8PsfrukilV8PxhT5gUrm_sPoZWDOXpQ-iVTKCwRHPjhUto_jEJx5EaurG95XxJBew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjlvfqxH_mOm1QfcautLSo6aOrz3ZSxuO2QYu5FYhie9XwgSxp-SfF4iPG0le-19tCEoc_GELwRMIAp9BIX8B7SNoaAIMPlExSOJXajuuXx5QMUY2plm6eqwc2GoGm-f8TqJdhDlVmXveamKlyxqI0Qj-TxfAbSLr4IcG5rcqr6hl0oXPi6HHc8yt6o_MfDxo8AFgk88nGq1PD5o0OR9D2CIgeI4WYs0lLwlfrGXCmU3aT6W068F6MfJgyBGJ03H-WrTNHw3GJHW5cEZcqFLuU8dJKXS1HQM2kwBaKn05MjIzjdJWK1v8f8S-00ThW2UV-CRFbfF07z76Ck1y0m6oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKmw8OMKYz8YrcOO5bsxUTGBOmKPyDlhWoOJQrspxx_Gkov8IRS-pw-O5F5BSj0NjhBMiHyfzTMiu7p19l25LrXqFz5QDXfwkglZY_nEiZRu1TYik-QfvD6BWfeWyMhgnl3NguXrpJCS6tYuB4aDSaPbJ_7iTu8XGJLzXzehZD4-_fYVYKpidvJNicyplupwxcxYhQ2p51BKtL52DHdTBJ4AwpHdU8y9SH1brQgEC63H7V843AGO_zctKYI1TQYnLgVff8MWheD5TahpupOpj60ujIY_Wv8KnuzcXqe4bflCMYfCyJoWeBA1bLM25is4X8RmqAsFBmlS2gvRO9rdjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdxirjA37vBJi0BW0jwzQqi-XgRHwq04Mkowy08-EGcWltHL2fYi9gMVUTpRMCc1wATPAxHk7aXFvMRYCO1aYgugJ-c2ffWud3_VK9Ycd2dYAPNmwcK2YA1Towa_28N23MDiK3Vfry1EnFoKNCAm0TsOWZTzj898fQRXBsQ3_KGzEU6my7uz7SGEMX74z7sDJ6phMN7qjEA1k3GM6GonfJy3jK--DkdqjCZ2BiykEPsyBmymksTTpk-t3SAYO97TC79ut7dumo9L8NMSmx1ucyxWevoWnP8ZW9J7F97K5scRCLmcbobT-MyrGv-JyGRNYsTO0MsS2rOrjLJEfkpJFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQLXKm-g8JBexW2yEiccQHhUqLrZBpD7XI3o_6hmC45QEf3PPAQwbsmvU95xcWo5vNve_TGRdk-S_KxvMU2WW4WbRc4TXtvpmRD6ReoMQGk7OCB-re6EjmeA0v118e6fpPx_DAmUtDDYDa7YMERPWiNGv2CmHn-A3zpjqoEFHee9XpAe5I-LAOayg3qLQ1F6hTRwjEqko9CY5IrXxzpdxqv3Ei0JEEOjJ20_rg-j_NSTQBws2hZ0hu8nEy9WQJtYwiEd4VSNEWLxTDF9_3nTOe-64od1qE-WCrF93kE1j9yJKoTabmwHWbtoqO_ioodUbT8iWHO8MhWd1NiY-7pmCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT-ORYFZ-avjf55mvECWaGoPwXLnnXbRXNpcsUlW82-Q-Qxz1B4L-g8gnLFTHTvFl6qX29NEuBWfSaPp3mh_28Za8PNzR05LRUFC5RSkS9t4MGerRuhFXLsanOIVspZRY134kWb-NOQTqCPSOQytFhrHK9eEAiHOlw1YuSVWmPlyK0plP0dHKYCkeuOkg2tX2u4KuX8fse0UqyD1Oa-MByvhmQMLULavG78tjUVRGaDtC93Lnnyv13isaj0Y5WyXPxqYZvLpvmuqNPZxdED6SMJhQ2K4ME7aX3bNjkjJelfPwsSOR1QO-gjH9nk_yQGyPH2rj2dqaozYvvSGrE8IvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1G1yeywwqERc9CwEV6LNQG78fBqtEJ6fyhxaV58kBTEv5i9Q15QccUA_OHtlOuE-gmU3SkFYmkzNVznxSKITqdDiiSAvTb33SyMK7VZr4PqWsQeSRIgZNOGS2ZtzncHl61xMwQNwMHcMw6c-YgTOwrTZk4N0zbawnzE6SyvbaTa9pK9hZ_MjRYjTXUMVOsMdiX7UtKoNr3I3Ui9036DuvNIGrSY8b5bOK_ALT4Hin-VhIC9PEO0Jl5WwrQYh2xLJcruOROSSOR2r13HyJExUu7Lys7mj9GwEXTdIbbfX5-bRw-MzGwY9GdBGAz42uShgle_kzpexE3C6VscPMUZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFH8U1dnBacdFmZMH7p7ogVS3NYUJ9I_gVQ-TwevUkvhxehgi1dwoDQlfmuBslf_DQqQYefpdBCs27lvUaBLpgSSu88eR_6iVv4KLaP42hsNK0uxJzT3xEeODuIDxdutwArRHP-VMSD_TRfOWoF9evtcJX_K_l2rSKcGs_gpKQLyWx-P52yP8FVlVHWNFOuzqgTfM6sW5mUcxqZBLvtGczHLLLdyxzcXJjTTOFeGO11_WvQDWeADSwWmiGP7N0wo2aGFRr48eCnUZn26qNiC4seFDWHeqy8gZKaI_Mbb4MvNz2w8k-FvN4IaiKzML1ybu7WpsLovq5tzpyqWrCkPWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjdcGdv8Myw3HX3X36KUeiVUGrsgtfZAsOIg9mY4YPKUFbPHlMqUF4UiEJ9h04drX1PKe19qYXMywN2Ju91MyQbu44UBNgiQxBTv4hLRksDd8DtA_c_Dq1QuHGZcfL7HzCuVjUmsDxuIAf28-6fqfepCTEre8Hc1C99HHazos12GjrpjQisYO7JVD6IJH4WYoBnC8mT4tqLGOTspTtfdksqAmMnrXcWExggXD8TQFeba_vc151-gYu4nYXEKQUbj4DkbN2uigSnbblr8ob4cNtUMXUamjuJBSGZeTT4lBW2ajztTZRd-HVgCdlF_0kwQhQNA1nHlHW8TMe53nrXNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlDtsnmuFB5j1P-yhmT4jQHMxEk7kSbzojR8FEcqD8UemGuGqPyuo6Q0tBsJrE4DCJe-FggsrxPZO07HfVFnh1IppNvWlCmNxDUcaPxadYSeHApAeN0Y7ziYesi3dI9MMSXRwkd8YHW9IDmmlX3pbXBgppeHB91ijjtbqrVIYUbAdRl7i4rthvpfJK0HbvFtA8vE8fwYQvM9NOtKpTJhylLExA-4iRPLP8E0S1nsLyz6RBJlBJA6NhbMBch8Z-EU26CqvIqia2mmcORI6H8ncFXk7K5dGZepqAE-OehNcqr6fjQx3tW8anVIbqsVf5rVei3r5KkAN4sTNjVRurejLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0ti3w9NJo2PfOkOmxwIbS3Rj6BPXt4mjDjaXPBiMmeEYd_kCznIswZy2euX5fjjh96_NaC7GONBzB947wnnEEt_PZ7kKcutfP-_iDeDvyMSJdtlZ0-aWb8OMLBxaYMN1tyBe4ByyPQhNgQNFQoR2UPJXHEdVJcn4qXfaOEKMmobxp74Am42biQrnMP1ZHPbTmVbod8ReB65rp5f71LfXYBGDlyF5Caf4KRshYRiqYOT4x9PqQeeW_dGQKQ0u-HszRFVKjFiZfhpm5o6h7_7UwgG9rtBl4eiqThwl_X8jaA_HuGnjF4Otum1TqSN_AEKlQxjs7uYnhaUnL9IkyQhaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwLj4yh1JcaeNo6VRVS_xhxT2aGBDHxmbL5P1Rqx0SzSWVTbngpUosYyC1irxmHAz470l0csIF1uLy9lfcbMc2NsQQqbxRjVO0DL7zC9qUgGunO8HG_D06r76SJCCXfs47TrvIbq5wbaOd3etyx13mgfVCCJx5MUo-hsvG3bsbE5-3ZmInJZLjUtCUissq6O5hneZS5GDmexKiz4ThxDXpRN8q7j9OEovreDQTrAk0ly8CHwRSbYOmj_Nx9ZYcsKvGhcvggXm3g8t7qr59d0AJpzJfL5I1NWlQCjWzq3Wi6ngesSDAoMcReKJUdX2Awg8tvQ0wQR5zOhnyboHdGt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHJFRdCRVkVDk4mSA_LAgfdP8Xa496HCwh9DvtMIe-UJZj9uwYG83MELHsePjJ9CKAlO7TrsZS6GX0TRj12knaJDXFAQ60dXOX6dp4Mj39amh3CC5a83CNDNGa2RYRqrBhae6wV3yRlfriEGo8Z-JTKzWY3qO5lmQ-q7mp2iz3FeILRYuLXL_QwSJPPbqDdMy-SdCxm15NvSJKvfOwOXPSdGf6nMpIigpnIp8_LL1PG8XmUD2WP8hfY0ETFU4gqFrYClJTP8ptOFzoBk14l9LLiqVoay-t_TXjLfoDSq4nPT6_Pogccxefc1qQHt1r69kW-ALrzHn570didurlvHlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtwqWhOxtzKNdL0J4uqrsajdjvwLOi0gJ1oqvZP4kSfIlz-Os2TEqZHaTRVUmhW_yxEsovycJc2S3tYDdBdURbzWDqfrD0aBjRmEW2XbkF8CzOfHSYTRE2i2Tb23jyOFD8-Gjuo-KMvNMTH4LwXI-lyyfxAaES-xc1JBNKEmOBh2m6gD3b4r3uYfOGkXjYcmG_HPBm54eqM-VG-1OUDFxKe30Mnp9049bMPDb_5kIUsgv4Tjq0tY06zUX81Spm7QrVnd3vaouc5Mv-NePDV86_0MmaRPvaPbFfP_ttekFa0ZEe7idCqgiBfIjzbHuCTzp8koy6GR71qJVuMhl1iiPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5VSG2pbEGNfPbL7ec-C9qf4VTj8nxfBWC-ZufUKGVyJWGxJvJqEg_JnDnzaPwtC0z8f594wEkTNhKTelSD5aIp2oKBUYtKyMMJ0VFG5w9Qbva3NdvvtW-oOamyg8_jUPoKvbKiOYu6CMZrg1_LIsDpP5ZvOtXTSUZ8ltzkdgyi0aq6kYqIqAwyTD0L6JztncAKY9g8L8Qr83412cEM5UUh8OZ1xIzVsgbjUvdmBH8AAJ3q7mAknKOXhLkKuljr2dguE4BAKbE6a_cn8R0AKSsd1eELw3XgY4QVXMgD1QHg4hFFbWQYJwfLRdIDQtS0WZgDYCib--sJMiUHlAk9YJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGvFQPzdV4MLSQrfjVrR4D11hxswA7ObI41NIjIFRf_TVPqTI48O7mP3h61P5TftGfEVKc2Iyhuyop7cK91uTaR03lX7P0x-jxaqOctTKiBXgX0Vne_TDSxk25EJ5FAaiZuiVjbvghrBc1Oc-rfusYgzuCJxj50ipA2ksAfTZhOobVVNGkxbpgUPeDm_XBKevA--04alinnLzCbNF_oO483jJ34pYNcA0uKleRtALJ1tuiO5-PECYWqNsoKEDlNbsMtT72ddch4VzxrRtlvsoA8Af06dwfrsLjKU9t0AIzLoogv2SYHZvXeefY1t3esWScKLPo74EQRn5MDIW_HXpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVwRijojqsPwKad57H8wpPepw4tF5Or_OCMSlOzrHiIgM3nni3f017brgm540ncRE9vm8YqJHnZLBMMrfXBeXlL_tvmCEgOv72I3hqv67k-awWse4yzp5VIqlNbh2x5XQzM_QNHhkiIQHLKvT4ZYWfN8eeEmPEty8gYHnyqJM73uyfPIgVpmARHXy7XkOUS1-Pf0dOGiipDyqfyQOusoLqu4cLQTaK762EUVfJ7NaSj21fgiysh1M--zrceYYSlw_bLeMzspN4Lkyiy0blb8tNyIpDxOg6yX_q5KNlSJmk53FzZz1MSqdy9dwxd2XQ2cdyI4is6Zffv5pTNeTmwc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHhqwIjwTIbQ9ghUk7OxZH43NqXfNv0e4gvjYlNVIOjGeTY1_PCshRASY-dM8DQigAslj-IhSwp1ijFtm2xJmrc3zFU_zYPs61ptvN4QHOEAmPH14b1UDvidegCXzy8sBRL1Z7cb-tb3jZuupDls77V7xIQkQn-4GAAwdO7WTxsI4x8zF-_V2ArQJlK3EzpDbAM1C1XALPsX5Q8N9M9E9K-ev-5jOtML9u5Ty0vcrcE9omdqmtqt8Kj9IfbONWFcSLljSPUZVkSdg_f0kcy_qDLmQZ8ffGjTv1qeFitCYUx-98059YVEaPdtU6Jh2lTtM9gYV8kVrSRZxGMgeri9BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryYpQ020R2hjOMgLKD6r2153wntfYHBRj--PL_Yw8EC7KbbwudwkvsGEfLRqeSbmptVGQFC83J330_E1ZuhkNM_jO7T9KIgD8am3Qbpab8zhDa9g_gaLiDCTkRZZqeNUOL9Gi3zmSGsFOVP7c4SE7u7qjf2h0tm-MPMC4vjIu94rrZh3b1Ydr7aZARPGXaYVry5Xn4hwvOffQzonDwX865aHGaoGFPHD4M6NMdoiWZR8dq4rYYO57ujpMilVQMoaODJutckAtK70f-iuBPz8FlE_gAC558J4U1ixOjelk4fVS11QriVPVs1rpmfRXzJoBXqOFxQmDMRxxMzhbQLYUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSmFfaKOUT4Byez4QMN5wKcLvvJEHCRjtYk1qKzDhtUsTsIjwZV8G_k6iKw0q6mtt50tfEZAI9xLGHYS2rOpffunTI0PmoDCgmONwbTEArFi3oPvzZXZJ5F1GvxP7MHarZzBmOho00olv1xTuZcy-cXZyCn5HV1o8xIBXkmZhmpXCd7u9mQwOaiM1Q4vWhfzw2AG7Zn3oCLdVfQ8NIFQrJwPJ8uAJ25aeOzhKwFHAWM2piUbKXLt_9RACgEE4A8QeYFZ4pDGcEZAOQI7AQRtkOZrwgItRLscHicSrd_mU20DZQqceqyGVeZhtnAbEl9dbTEZv9OrFJhxlnhfK1e6SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it1BjAmPlcF6bxBK5oqq_NdzLHAAWuO3X1hOI4u4atc_FeGZbZvCBynsoLtBguRoHa9k_U1V30lCwCk2pJJHm3j3mUJ3mj1e5XPBlq-it4b_8ryzeZREa-JQR6He_kuU0Co82PN9vYANqYEYSW1lP7J5uWirPmVIPHXd_a8JoZ6dD0REN934Qih0VXfiKSMVSmvdDETeSD3jNnAfNrno2QrVcZTuRjd8LLbab9j4_AOunZqxhhOMjV2953bLoIHLe81wgBOCszNqMPmsu6X6MPp92d0uH8ehPNbA0qKbUE7VJPHn-XTRr_c6-fuOEFDemeWGZqfHbsMD0vW0v6ihqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE16-PPHsBWHYPwQ6hzW3OBNMAHxt4h9dXHrtx05gyviJ-cE05kqdTClkT3qjcxULM4BLTxA50ElBxz8azgyTd5Cs_awnCTlsfrS9bTs18YaX9aauzVzjd1OP1x2op7fwkyepC915zZeAd-hfr2wQX8XfNh1nl5DS2-CIk4dA96HXyA9e7Xnw2PQHwpvUXoU5xAUcqFsGf2QdnSvzFkUOMrafA8okTh9Qb_WsgnEtgS8fDsa6wGzogFD7oId3pBcIwEK6t4acRE8yLpH8rEKwAFjF6xBG7fjKfoMPFAeRZnXXJqQyBWnHzcilq1Eqmc0hZDVznRuHSJUbhc13fViDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=k0UaNTDakoDBSF7z2b52SMX5gI_067ch7e5gJLu_Judm9G6c0CwIUGOPz1OJA3PyujlTGbQPTEQH4on_Viqafx_9Qcj1qU5_qwiNbOKLjhtPtHdZ7ql9RpV7Lrrf8hj5JqD-h4drRpClFkLbvDaeYJq5cZ2HnS0zk2VzXi6PU8nMAgcSpD2ccifZSkKyshcIT_B6baAkHn9br9Q9k0CmFgq87bmmDGq9yxKVDBJ8dJGjFRxofIJ4WbiX8gQkcI2rafstUfEc9Xdggsizg8_huZj6DmuUrA8F4F-wCdtV-D9qdkgSDAclzI8r4jOjvRiKuS3K3fh2Op6IdyThmj3KWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=k0UaNTDakoDBSF7z2b52SMX5gI_067ch7e5gJLu_Judm9G6c0CwIUGOPz1OJA3PyujlTGbQPTEQH4on_Viqafx_9Qcj1qU5_qwiNbOKLjhtPtHdZ7ql9RpV7Lrrf8hj5JqD-h4drRpClFkLbvDaeYJq5cZ2HnS0zk2VzXi6PU8nMAgcSpD2ccifZSkKyshcIT_B6baAkHn9br9Q9k0CmFgq87bmmDGq9yxKVDBJ8dJGjFRxofIJ4WbiX8gQkcI2rafstUfEc9Xdggsizg8_huZj6DmuUrA8F4F-wCdtV-D9qdkgSDAclzI8r4jOjvRiKuS3K3fh2Op6IdyThmj3KWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sry1K-0zKrQv3HfiRrHES7MX1usoHm_x8uLNRJrChMrhBT27d1P7QGGCg8b9iTRWXMohq1iMT7f6sViQBzCDmWzYy_4Y3bAX5iDCg-wlofMCHyG4MqzybV54Ge79p7ySoj1PENOcTOI1NeChgNjcJcvu3ZCNF2pVGmtVjf6LzKc5-jC5JB8-F4YVYY-CTBaYrHuTDAcmTn-guotz41n-93d7quceh2eD24kOcB__Eo4IJWWIsl_krUFBVXYN8AFZNQytga2IqNIgcC4wR_Sjhe0nVVojCjtpjju_0NFTw7BNQ2BFDD0T_GPfWWdui3o20ZpWVHueua73OPqrRODC2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX2CF-RaNxYfo7txsSKRdom47gf-nlu8gLGn9_hq5LJFEV7e8VhgWg3I_6C7_m5yxSLYPcLzsaGF7PxBOwtveeuefGiWBpyvwkzLpGqO8uqyhRY5kOHjVAN7wtiiK-ZzxRsftsLNbcvRiJr17OlUFFRRxKiYp-bWg-KJezvO8gXo2XagOruG0EInYxLytchQlu2NnQAmb241PI7gZE6hnuh1KgAk2ZdPxaGldw0vbSwO0UnXDIygdZhyXrwjE1te8QQhllAnavL9UHL6h6kblrpoT-JjmojznLYM1Gv0bRCGt2Dk3hIL2HFZFF7QmfsC6yzscpXVO2M18dWNe9xXjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bl3O5baQc8m1ywShO5YMdbDUfgjqiuK5MnF8xp4GdEboU1ARePIhZ7nI5JKd-0cEqJ98B1YXK60wyi1wWLu-PBQKwaOteg4miFKPJhd1mgzqO8f8D1mmLpmGm8Pq2Z4_b8YQ0KWUI0dUYmSiGXnDhP737oE3XZ2T7j2kLRraUBxR95V8lWVJh76fD9isBxAvabJHTa698gtkzNCWZfOypxEiiqjB2lzWKcBSFlF7o4XDkBfQSqw9sNlOXDQlktVtXwkN92TmpzB6FWD0hVIUh2TJ93JQ1tIDYj-emVDYMnEPVY9dLXXGljHR_gt2WpINEgoIfQx5FsY5nMjA6VjdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0TBig0DXg2rEV-4b-2rqhOa-uY5QWRRU91sri5XLCvIe87QBFWp3lSvV7e2HChyDDIYUd9ku5x3Uz19jENKeFDwzn54NP0gwtEQkWhQhXWJi_D_5vZENTzXUnJl9UuCwxJ0GaSwf0MTgJ_k2HeBUYEcVQz5KAyeaQL90aj14FYXM3-FuQPWBXcVvIRQtTBw3JbQeYBHeE6JhTBPc-WYHMt1KDYxAcs7ttVh7OlnbBq22923fgPSsWh3_weFju_9PGrkgjWmiTZqZ7MwcEc72_08lmxD86EaCnoyt_qoaBJFdTp4x77hQtUMg7RhOiwjpyz0Cvxh4TxYQCO5Xb_c0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX3wQe8T39B-g78WWKGxwe_V_IcPizTCRVIPHSfHuCFs3J0lCzXZGgmEBqRzsLUJbiVpVVoVVX-aQ0CaJQXMgi3fwtDVWieAvgRYLqLQ88vfKAWC936bpWVioqIMBqOxBUF-3IYL2E4QiWyymnoDxo_NkKeTdVDLim3TUhO4fVhxxR7dwUlC_a9k4-FFu85YNL0RRF6NSnN3GfVj20gf2hBL7NMbV_4GBxq-J8BAn4UXSDky5XZKFfR2sezvp37EYWtdieWJoYkdKKVNrv3qCRpP7pcgynGpFMMZVYPwp6ZBRFeoWuyDBJVxJ0DHibnZSdfawJshfrVtTL9jVgyxvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qb2HIGStVTYUP2xzt_MEvJyvqFV8KU4uJWDEBb5jLJ0FsmZmBG0SaSefmuPawbkLQO8Q0fDL-sG7J6jI0QallrKS-gczoEjV8VhjPZbIj8hNgrCA0hc640fCHhrQwjfHZP-7AbOnG_fkx0TbIiiTX3eL3r_bLO_E7KzS2PYy2AOnG4GqRb5GFOdFe5fldU779uY6H7HQnD8cspZodm6zIbtIXB-ylJU4dBQxcZRuYxsxyGuE-JWb6JgkHaLi-CpB1kqZ3deE8ZDjFPhhSlC-ubPefc4kuom3p0k4yKmHAvbN7I95KxHDhH8c7Cj4gGS3eg58oPXs2g1q5DrWvGvgIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2hHkP2lRggNP4JQcdoe5yXhARU9ohTi2FwaTEwXZZuEFE-3dkY2kfLOAfUSUTuPG0q1GT5fSdwSsRWtht7TzAC8mHSMbIcfIJ1p_Y-4pKOMlI0mShRQnmzyxcqb5sa5VZZMGWmP_PkBeumBacCy1Q1d5jPydkxQszUvMsgMXwKoykknAdGtCFr73w4PEBt4-nnfR_jIDezTra-BrjG4KFnokQNBiNTWkAcQvjWFoJbL-CTzQGoN8-bjCKOgFnaQbNkUpRxuFYh58oVIvDS5Llv5CPp5etKR-hDFjm9d35CtzZVcfr93FnMnFPGbrzBJHwCwSRXGy6EdLHPVD8RNHw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MLTjXVGu1wXaXw3DMut4mmvL-x_PBGyE_qSl2IuScvJwHQkj3NUARUwVBxxLpoy3qDTjZwwcxcAmCp53il0_P8iDKOZ0PT950wXFFbEwRZJ6Oj0rqkfCWR4iQnbFZJ9TP1JLExyLHOIf3xKLlVLoTl4kv9ysr4BiNo4QtI6zQSAiEJn4nKiyaAgCH-4HkjSyHsbN-ApytaEZeEvZQWLP2LLZywcJkqTZggpDqXl3ha8QpV0eBP88LYva_MUQDygHTaPZRlklnmyQBsTuD2kdt7q7YKwqOMgaBTuFyKbAyy2ExhkHYDbUE7silmYUAPmmYlDomBwyT-GVi7x-QmmFRV6NRjnb2hDtrtIxMc9JZU746I0uZmb9bjgNmmsTj5rN08bQ5yZJiFGZ_LxTe_qzfySiKjWi5-mXNB11V3mbYKdujLJX1aRxRuRC_Ez0y8Zup-2GkwPLbvd9q9N_gIEN2bi7O1CDy_20LpaFUwrPm4C9M9_oFYU9_dGGN5CxxyHGDUGnv-yo13QXTaWZBWKjY5OjLzqpZavbonqANfw--bu4n6S7DcExR2gclGPKf8saoXrdxgteyv8sDag2ubYQfZjIob2yAJ0BhfuvuyYX8-UH53vM6yloiUNoxFup5Ntw89bvgj4yxDLeRL3THPZr8-4atwr3ap3CM6avaXuhjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=MLTjXVGu1wXaXw3DMut4mmvL-x_PBGyE_qSl2IuScvJwHQkj3NUARUwVBxxLpoy3qDTjZwwcxcAmCp53il0_P8iDKOZ0PT950wXFFbEwRZJ6Oj0rqkfCWR4iQnbFZJ9TP1JLExyLHOIf3xKLlVLoTl4kv9ysr4BiNo4QtI6zQSAiEJn4nKiyaAgCH-4HkjSyHsbN-ApytaEZeEvZQWLP2LLZywcJkqTZggpDqXl3ha8QpV0eBP88LYva_MUQDygHTaPZRlklnmyQBsTuD2kdt7q7YKwqOMgaBTuFyKbAyy2ExhkHYDbUE7silmYUAPmmYlDomBwyT-GVi7x-QmmFRV6NRjnb2hDtrtIxMc9JZU746I0uZmb9bjgNmmsTj5rN08bQ5yZJiFGZ_LxTe_qzfySiKjWi5-mXNB11V3mbYKdujLJX1aRxRuRC_Ez0y8Zup-2GkwPLbvd9q9N_gIEN2bi7O1CDy_20LpaFUwrPm4C9M9_oFYU9_dGGN5CxxyHGDUGnv-yo13QXTaWZBWKjY5OjLzqpZavbonqANfw--bu4n6S7DcExR2gclGPKf8saoXrdxgteyv8sDag2ubYQfZjIob2yAJ0BhfuvuyYX8-UH53vM6yloiUNoxFup5Ntw89bvgj4yxDLeRL3THPZr8-4atwr3ap3CM6avaXuhjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0tS3APWOEtWNZ0MR3LHnvu4GnozGZLTVepi6oNtvrXCInpdD_IOtEqdJI1uwvGScgCarylalRawM4hacOMZgkSIDxK8wRGGccuiqURebUHo5FJfzU6evMdXLv1NxXJ2zmKcdM4DV5CdiFrtKYq785uA-cYdkgKuH3Jlh55vgRsyauvgNhyKdmh-GIrclORSuhHR3mT2mlZAH8euTQHwjDQnfBb0SGHhjivqckVzhEp1oAko4S0ncqrdCKeVPrYlZ7_76M_i6DJ6AgI0cpBgsCxDWFG60GDXaR7YloEJNoYUmfXZlHWbxpqGadgBfQlP-XqDSh79nBJudUm8t_VEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5kvscKx0f2Xp8B-nZxOEnkWhAU28JtBymjY8F1N8sEvnqU971T0LqmVQ8I4gGl9u47uRPwaqY8LEF2wk2Vj8Rf8llKUIOpzCdf7USGdrbEdohfJ2Tnith-aEHHpfyXr8wjUrP5LRWfX7kQztOmKUOVw8h8H2KbfcIVGWp_5Hdzh3v3UH5uHSYIfNCsX4Zem-T_Lab9-5CEM4mx7eBH9DQvmJCM6l8xk3noinbJBIYV6kq_Wi3wjYZPDkMQewfaqp9upD0j1wtutgEemHIz1BbXuiqxh38QGwk7cZp07fEdaOsBCZ_UiTtTkQiWAnfe5TuZNpH5wK5VGFyqciStYTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0Hrp1I4MA3sRWM2FxHQaFxOjHrGoWLfHEvcy66sKIoDMhhf_aZY14RELDZ5AOTQWjiZIIdiJUdXUA46CNpGqnd19XprVihKG66l6miLN0cXWr79CBEueR1RAoUMOnwq30-YU8fSLEZEOns7Oo128-cp1klmCTnZTxiPnd44VBa9xqXtsUilJ0OHDffdHIpqopQcO6SMfbR6YWR7FM6CXdTqLg19bWULA0ILdOkKOiKVrilAzPk8p0-vAa5VLZc_uzHJIek1l-LqwBHNCAPotZx2tgYMqLD3OlEHxzBvNROZcueAZ7C7bh-VrZYV0qKe9gDHiDCOqCTPv4CYO8gTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJHMA3UyaLAlf5Yk4Sya5bQh2Qmb8zNFlCoO1IoorluPmDV7TF9Lybfq1T8rhj7SisnIUlGnqo0-CLGMFCLaNMuRs7PvzaTgXSJvl-_UIL7Jka35Uz-oD1FQqYRkBWV1B8ZVY3he_3Z5QtxKZyN3wHh-3KcMYzgdX0YCZ-cLUYt47oPC4o-P2rHLrnuGwYGxi-KjkeL84maoQzMPq_IbTEUjwYQElOipegTWltO8lknaQFL2dpcv1uHu3WsZMrr-qYU763Knyjuwbh5PDi4ktjaf3BgOciNMexQJtWb7fPykhaljmPIvfyi-kRx1UBTuOeWucmsG0VJ7YBL_DA_xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3HUgJr8PscdrF9s6aKs2_-vmawVnwowOXMuiBtTqYBHJLiouFXrONhu_5UgRRfPDr64lmyGhHH5i7yr2M1TsTaUU9tXVHcrn5WFdset4HHNTe11l2sMK-6HABBfbwEQgXNakgd4L4nUR3Ffmny4WXiQaBotnRb8H6l6VLmDcWq0T-x6dQ_A33NAsRB5GCcrlxj0H50JzjaMspnG2d0K8q463Y8dKE7u1Om8ZCF28Yn01xhbuv2zkGhqtLXO5izkNTygjNgTeji0mXOnSqmPSYSumHmmIvFrpvdbN22p2Nz5jhwaTg03Ip3KHWNWgfCi55dlk33qXNDWtk90Ag2oJQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3BLh4xyRckg7f35kb0dSE60KJ5xFFw5HTGci4I7Kpbi2R_c2FaK5MWuQQeE3DuSGFJoFz7p3N31sp9mSECXE00XkJ4KQBl3Ez8M1GhXiOejwSqo0tBDOVX8gpJ6ezVMeTuUs8ZJ1E01tHFcgMEXZz9BoCV3coxPQsCJY9ezzV1aGWnWoO12dcVRF9HngzyoFCMAQfDsrC2ba1AVjI1lfAZUKsjtrSb5bLUKz07vpHylrhR2CedGZNaDXdWAJMXPNJW1nV2IfkOZhIDNaOR1MHGA2U9tES1M3tOg28z6BpTjqrzCEy3KoRrpmPqtR9ZlbFqB4GNb2J2s0ccycmIBYy8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m3BLh4xyRckg7f35kb0dSE60KJ5xFFw5HTGci4I7Kpbi2R_c2FaK5MWuQQeE3DuSGFJoFz7p3N31sp9mSECXE00XkJ4KQBl3Ez8M1GhXiOejwSqo0tBDOVX8gpJ6ezVMeTuUs8ZJ1E01tHFcgMEXZz9BoCV3coxPQsCJY9ezzV1aGWnWoO12dcVRF9HngzyoFCMAQfDsrC2ba1AVjI1lfAZUKsjtrSb5bLUKz07vpHylrhR2CedGZNaDXdWAJMXPNJW1nV2IfkOZhIDNaOR1MHGA2U9tES1M3tOg28z6BpTjqrzCEy3KoRrpmPqtR9ZlbFqB4GNb2J2s0ccycmIBYy8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMn3KpUTfGuDjiRImHoC7s24VUKyrSEJnbt3WNvmoPf3WK87Pb_HBTJ8wirnST3zD6sw8Cj5JPh1XafHoFj4gRbh06lyl_2vOUUZrBJbSQiRIvE0Mk8fmAF-lLEdsDCqAe5LDsVk6PclQ8sp8_XfXnR5V7KFmn5nyuly69ZdZg098CPS6JB6l92gmqQpJqwnOYlDj2O4TKAutkG2G0kpittZtQcmICm0QJC2Tdyv95ZZiXIh980gPZhonh3DCjd2fTOvLZ9u_RJ5Blz7RtLFUeb64r6K_qrtTunOVmqwCkRLoTcfBcdwlyJy6uHJyXWloUmXD14nCVzaNDzwf8dDFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYuNcz6Z7BM6YSd4IkDYj6I9GOXvg0V6Zjiy2pYNHQlXFNiIG-w_QYMWcmXOtvXBP77QvmKOeSVsr64pCA3JH708HwcD-JhKhdugTF9GK85yATt-44BmBLzQ9sXhWAptzbprfKeOdfLWQ6fAYW4nK6eA0vBYyvds5msnxgGJ6-VFmVWD-tIDy_XiuJvUYCwqfIU2uXKJmSNCXVykl18dsGH3YFPu4QMm4b5kQYXxBg75xYPUVRIj6XEoCbivok6TIfQ6Ac9X0Vo6VlhXX3gM3LNQ_Da77cix2wYx6OI319zwpGzqjLEFaa7-56kQj6vxPZKCEXYjtWzde2L_sYlx4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwjhJwag8HFVG-D5pGhapF_AcoO-VGRP5SYHlkefa-ayA5GZap5_F0U73d_J6wG5vYRzqqSUCaW1PsxWlnJPz2umjHRZfJJEN8v5YlIozyWKh8OLr2duGDBddE-kQe8XQUPKd3yWb5ozVVMBufMVvzvrOTTjsYzta1X3BHwarcl5yfpYrAVn7UxUc3WsgEMsQd9jfsYmTjNylrFs7_DVZv8l5DiixQuYtCSgZaEOn9W50cZTvNUCvKibk2LUpMklaL_enNx3j-0-1zFqEwKrl8lpm9gN99jpTV1vry8qHv43XfKX5yTmQowB4k2B64Bh2kM5UkW6dYr0suJl_zHJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBMlmcrszAbC33p6_sQQlT1T-F6CKlLwPtCr0OxszPRlGZ59e7q4aFPjwydNx_9v2iPp-nBenZtp5STQNGVmPfLbkP1t9D3CS2tnmmcufOnfEV9eSHHm1M5p7u-2I03ElZWCCK9e6IZCOuwh75KeYP8JUQxtPvlbFdjbLHaINU2gq7q910MiGPsMHmj32EONhvJHKtJjWVx0mHbZaT9ekyhAGqmAW9u4kGVVt2lC0blGvuRpYtrDG_F4yBT_gK8Parz_l5rKmioUcQkU6Vav0roi_yVxk4qt-t-tsPdCw7P-szfd50cu5Hc8J8n7K2oGl2wBeoe9qe86_sgj0Ie4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dm7x0zarG1BFQoXc2vFU1QYujdR5PJe745hnN_Pw5m8NQSShXeQjH_fVVBO9BtIl53arxx2leT3NCXB5eYgWXwh2D6f_cVWx2adGBOYrU4B-vFesLrSNbeMjGhwfFi5x1mcfGcj6cUn71QaCeZFKAmawQ9kciqjps4aNizyuIth1xCH78EnPSIvkzSI0zHR1-q91J4r0JQpYeoehsyxjprLk6ZTR9fk7mUf1gIq1baVlSYYNAQEAd433ou6QID4mxdAnYdVHYQSPeIWuXDpZn4weus6jKFwomfaOt2eBxAG_C5aPHS5FHCIuS4KlSo6tusIzFLAqmiDZzSrbsdId-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSeDX-3b5W5eFlhZedu0TvYpmXoASNxVmEEvcyzm0wcqTzjcrd4tyH9mtXmvtwphHnK6VCr1yrZ3jcHa58pTUpJmULfsbGj6cOyHOwVqNzaRbPlR0M_7_jBbgld82-81OijsLFyU4Rda0UdZ9N8CvwzWRQtESK_h2AUAEIcAj-JOLPlZA18k4W3XxtXiHvTAUlVUdX1U4QCAwiHWyJY654h8EhqG9a-awhb7rsAwoCSf6vf064kpHY_JzfOeUNAbu4pNfJnK1i6LjLl8dvX7F0aT_6RF-EWyqSOgxOeK_-nZOoYz7OXs79tKGaD6hW5tRGIYdQDKnr7GaciCfMjQYA.jpg" alt="photo" loading="lazy"/></div>
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
