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
<img src="https://cdn4.telesco.pe/file/IT-_mesDln1Hs6g1UW1VwV2d4mhNhR7BWLcwYxVOzZdkL_SxnMpv66sOAKxUDvq1tzvwehckRxJq8BIMF9d2MGZCYwJketJyUZgnjP3I9BV05-xt3oW5nTBtUxmFAvF2nWXaorf_wWsnP285FQkWbA422JBu5QaunqAU1IGxD2h27av8u8fJZ9513wVejOfmc1wSjRxf43rDbVk2Uazaj7MKp8nDGJ3DJGgmW3K7iBSsn3gG6PUpARST0xgJ20PKrxTHdd7g1mJCkxgwBVI7uh4OJE-cJsgdgyE-sBDaTuAW4s49XYX5hIs5lXSCsPcZ4ibriBJlrQDVS9cndmiLqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 18:15:48</div>
<hr>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4NzkJKqYYckFrGBjvl8BquiEB_OT5qHD_kaGdYjgi4XyaH6RxVzmd-0nLnfisX1Fh8nYZmXSC3KLEMPBGc69QygXNYNnoCDbq0h3-QAvvYy1UJQAihSLLZ5wEkU8NxBkE1xvADLRYstldKktfh7li_Kiidqx70exy0Pwe5_iVmkazgHSg0AbEWJuxsoRYE0AOtpAtoXd3I1rDxfYgmbXUFzao0XXZ6JAMSzg1T3ph-iTITRothMPajaNwtiaUJjQf7DsmVi_8F_PP5-jF9uN6QhkgHkJne0BR8PMKgqy6J7JLgeogT3doh0EupQ0NHkd2iQ_H6shXtiFKcUam7ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 155 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 565 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8fo9JTUePTAYuXlLarGqT3yQV0GW4Vd0G4l8ncLdDtpHwsmDf84qe_g_uW2564Gp3GbJUXCHfz4Lv11vEJ7xK5UuP_NhjCyILl0uz8RyLxGa-lnZerundz1mX38R4QCgJHW-Y4oa8O5BjTLZRVWPyyOVIIZTx3CFVGblX3NwV5-LJJbZnrkjJ50wYEoUceTYeQvI__MKI0ropo8wrtxM7-km6cWVA9cIcot-e8_4Cp1Gt2nIK8oVW0hbFkmWXV8MvD8bXvlbUjHUb0TngBQrsRDjPk48OeF0LRtXaoMPuQLYgA0NnIdIwT-6dea6y2WyCs-c4pBV02BijLw6egkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juIyWYFK23RSB_wgQ1RxMB-kiKeLdHoYKmBJXdrq9Ax0mty1Hpjdve8QyGeZ__aQNVa08LbDUgdrCnY7wU6L8P0eNAk0FR2a-16vYRdgz2mD-ey-PV7FDL-0yeZR6koZaoeGiwyQLvttcIIy-l3Mk30j0tbJl52AitvZ6f3INNZH6Vbp79x-JT-3fYe493UlobxrTVX0r8ANqxwwsZzybYgbgFTfN3c5Nv9KArMCHDu_PevpcSXuCkGmJZ6tMIGnJfOmGZuBp5Rg7YJmINouq_0GeTqLjNVa5kwIrK_4-zu9EqPxOidu0ivKrayAnxxI-4VwtEtUjnFyVgIunjaBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1xOovCDNcEpsSeNhUVFybTh-_4KIQEA9_HuDdyt1k7R4-Rv-Jmgvtq8EpG73XrwVA3TlZFIKRpdmQ3ERTuvdSvgAjigjgHZosvaCkABX2Nrp4qhaLlOU5d9inW63pmZ-DEI2zFEwgQpG8ZouItp_GD5u4uX8Id9_UB8BKojZHfodk0IdBlK4tS_6_eokfZiBLz0gZn6eiZRSLc4YmlS20E0hpsd3bGfpmNUT5KAFUgpzBy2Vjm0PO6bAIgv0ZVbATpjPxI-CN5AQnR94PpCNDAh0kYgTqvBAlTveW_gYL16gxJ46LvlUsXYdg3VHBjpzQ8HCdlhSgbaoRQbbPfKzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZCy17fqNzBkOu27-hJt4C9UvsCn8TrDDD6_KtmhwUZXDpo3RAs4iso5U3U4xq9vkFcOFIHAuqkiyQmBZXwquXNXAcp7dJcJJJCxXaBRDA68EXpiUVQnQFQQCrB2SJ1rxZbEhTqeK-iwkZUEVtv-ur6ZhF-oKfcSroyPdfPzjQFNRb7tEAPDFg21DnVwyPPc9NFeHQ2j2LJGbCjOIIr1HGXJZjYygOFRT8rLHhcfkHu7IFYZNQ_5o-tH9EvJcfz9QRI6xd-oS6ZTmd2T4dFcXc0Db7O7z8wxZdvaymIhxiSOhiYevs-Jgo0TvClms2w2uZSNiT9r5d4JjeEVzLLy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 789 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLliQzHvoyViqXc9MsrKIxRlq-hJkPEG2TDFa6hmX2qqex0VvPYLmgvOorFooSA1huV56z9ThcCTGMIYJ0q8E1Pd0qoB0kjPxkPmsepiviVivFTwYyRhTEC9YqjRhmBkp2lzmHIOits1wd8ZFN4s4oDSyXer7P5Z04GqWkASFre5eszChKNmra90sv-uzZHYAEcvCzhFCGOcVM16pby2VqG4Y4A_9aWJ5AsukNu2nBgez7dsp-WIdugwv_J50ESPpKSovIjfiJMp91Yz3rxXdWdgJqT8yBPrYml5lirR2brf9GEc08cgs30Iv-2WXElAEOUjxlUwMw_zcuKeNVuuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffjc4KPVWeRsrwuG66vwfFM788hNtbBCJD1xsLEiaixwqS-9p4Sl2SpqT0C3jZgkG6IOMjUzjdLINzsxRiP4WvfnHcXozQd1IdolmO-RmhBrZWthyGiAhFFs6iYcrCNRIbAcmJPc9FnkuszS3ncFBl64JlWyEIjzFlwPN5gA81HpwcDW77MKuw0QNybC6ZR0HMq4Wcvp-tzmC_YWtCIx67mq9Nj8G13XuwMffFxkGWFrivgIyNXji1AYU1fHl2kAE85LNPpKBqWfPFNCEbCe6smzLKTgH86AjKByuYVYdJJyNzs6S6jXxNr7ijwRKOYPl3o78MOwsijrEIunp4UNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fO8oU46UzY463su1Sn8mweFweZA5k7i1qsCVBIpoY1sUp0BDhbQXO6o9bi8K6V2IUEvlSjsRAu1huJTN9COA27HZOIcGyIFBbYeqTuBSNfUKx4t9oKOmm_31S53O409cfBGFwfWLlT1NVzgQNKnooU7h6l39Iw4AjlER2P-pfZ3hN0KzXEXlqbRJYgiStWmu-w8dNIGHPW0wgqMTfLnV4la9Jg0ZkqwyO8WMSLNTyRDrbLuIi6m2Rp86iyujeVI7qapFgE3Fmj90UR41I0BcUHo3SjP2oPaY0A1FElTeSyLKYAFOaFs5cPc9wujB0vf7Dds75fwzimGT0OFIjIZwDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TctJUwK2sCCMK_WiVAcPPBFTB-1Es1gD4VXRmUum39_VoJPiPJ6GhymxBelwHZ1-zJNUdW1tFc1Mqc_jleuoyPqLXxYzT28UrBXLzPDLFs9M-5Ht2QVhfoH5m434ffbrXyukrgivQ-e7m1KlPgnRYb-iTKFV5ZLc5yN4KphAnl5GqJDAXwe_bvbn-MHV8JGMUoGX2V0sRAKff2ukYx4m2JzOy4-PwwRKWWjrDftFTK67_W-N83S69yWRKMQCqk5FWe_LKteHnZiaX5DSLoNfVi3mzJfJbm7RXpaOFSawQsL0hzXJ88Qm4rw9VKO_e4fssBMG1cTIbqtAYSrs2aUNDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 649 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGYOhmEKSTf46TmGmzm88uHg1wAiFnKYEDDfgAxYviTwmK2v3OSjyKzI5jsAeWR-GfWIQ3MkmWBjcoitpZvMTmn-ppECiuVAbAsGEStz1HtOQsLaJe1aq8Y4eKSgWFS4tzb59sAPA_F7hhF6AtdZWPxA4FGuzhZmh0JtGkeBjs0-6QqRXwrBTNLvCOA7dGeD2GWJdNwoph6HGoo4g7YXIFh5deWndrM44KH-mW8-8_Zj6RHxGozzQmtR7qlS2F8sYdw4D8awWRXsj11E8poquB51eD4axBni0tMwe-_R2DZkkaikracFVHgZQpj0dXn2DFZqTZ-3SJB2WXpNcN_lAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 844 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 797 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNSoPdVVJVie9ARmXnGY-lhzpgcwaBdWWVROZLbW4gJ6lx8lMQBsoc_RuJ4AuYG7q-sfZm65xUd__OI2lpnvzYbJl5ZkPQxP0drD-b42zSBtNfOnkeQs81qfFQlCX63SUDhgVB_y_19B_7YoDvxzW3Opl_oqBQ45O9dOfaiX9UEgVWnmI_KV4v1_4r0ZF5BfHlXmYyvOwIVesoCcl60TAhvk5oU0NP2Tn00li7SiNjVTJLAkHeJI0NSUDSYOU5Wa4_HEGsCxrddUPYKOgeQM7Gq00Z42mPE8qyA3n6mSIS-R9c8NeDZEWYYch4tjG-Oz4W2VLwxRbbsfB7tUSBOj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK7sHGCNevFCMxFUU3NMf44RhlSxn12FWGema0I0zqTX1UhXA3RnCewa0tTGAeqKbQvRY2nkD9esgmet1R4kVbVLxdXyF8JSjoLckl7OgvxW_sGk9g4vOPODhW9NPC_cnAueYMcFD0vWb_VPR4BhAkdAWxsqV59oVha_ZFyaeor-ocPDTcR6t5J27nrJ_RdRIVTMjWyRUJNSWJMdV73lTnwloZgSShZzp6-cm84TYmLEN7mKcKENKVRBQ-t_mzz1pBgAzFwDJqG5kVDehtbv0M_i0kVRjkyiuq_hoNDCnwrSwXrCXa3pqbI9CX40w-oFpwKR5XiWUPT7Y9bAY1kl_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CO85LS5jxrmqz0RyG9qStnOUy_5eifZnklyiKIh6ks1rd5oPmwgi1bLQlg33Nd-OxmsP1iey5qT1VCS3uPrBlGNKWVzDW-hFoThaIPwBJnNkvZnCTVVy4weIMu2lKu1yE4S1jvAGi_-DA2RtMZiNU8f1C_KYF8upY21Sm8DV5LrDl67wSE5yXj7O4bMLbKKU1NS0tsr8jFK3sKMZLjRvjRBTg5EFcs2gMgWu6dWT63O53irDWy3yc4thyRztsn4G9RsXabODCTZK8hXz2b8BQSGsp1NtLCkYBWmre_ZXr_POADUGLKYFrnHFfcN0w5pKBRC4Xm0ZU00kE_WBkFAsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-za8dtoxVwGeUzLmF8yPqSJEs9q3F3I4BnACmmNZeo81rH-t77ef0moQZIYUgUsmB9lgMywlLw37kmJfmDLcyGLbY8VNqvBYDyUK0j9fIn8lFIhowQ60UtGAz_z691-zWoe2b-8YDqyLhUlFqU4fGjzAUBk-5kEnO4RllYLUcXrlT835ybdiByiLqxtXaVaG67Ev2yLVvoW1tX63wZNHm5j4lsXenw801cw9ssLNjfJe-7OtB-RY6v0VOcTXMd7reioORVh1Bz6KdhQ2UI4p6Gqnrxo6HPUB9npcIUmme8L_2LuswKuX-HqA-fZbpruZp_PDXz8FLMmklAZtRztwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0srT2w-KY-fwMctuA-b7rhOhLSJk2eRZl_5kATZaZWkUQ1-A1Yej9qksF3GTTdxFAa9eqKQnRjAcH5jEJ3WR4V8LK3s4xAElanhc3JdlV46zzCQZ4jErLipMNiFQEYhmedFzdG5-qH0KSPMsoBD6GN1HUXER55MPao1zx6hAP81XlZuCE04c-xcwxIVk8pfhy8PRZH8Sy95c-i_J2JNDpCfZrXPQJ410XjOPkLO17WJPuV9BWtvZFLRn5QqsFe5Q6q9txqGFNxwa6JRT21XWIZJlXJEq2Pk99-44t6j0KUioKYM8ZiptzFnitAk1oqimj79BMsifarfJ7mMRVJlUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVLFa4DXEqNnm6nCj_rVfyHF7vmPotag_xSyYfxNtxjsX2isyrYo294ACuzgD2CzxmQ6iBfTHmo4_KVvnUIePpfnJF2F3WAi9gZdqO-GXTfjq3Jk-OUsnqd1fW3NaQEDmRIzEG9CMM2u5IuJGwRqHby8n7oPkRNJsq7MjLJDPvQjuJJnFMuT2N9WJ2s0T5e-wzoP5A2zQY_JezQ8B388S2agPHdVW0XzWHjyxyo8vmrlUIGPbvFKwN8NHPbPYHukHznSc6Us31Bh_ktomctQrn_x2Rgl89E4f0DYSub9tRaufNzcnZWVG_Rlnqr_7OeQEivlEUDXcL_lzBkQ1dFCwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 938 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyVSrZQ-860nWJqMH9ayIAU6xybVZDp-TzAVPVNoDOD54JXBuso4eya0Qn94FAH1zRyjoU3fPiDSsBO3QY79RDHjAl-q0phfmscscgyMmPwUh-ZyNOPqRD3SCqwfShkh1oFa-Y6uhIEE1BBae7MwSMIKCYeKn98j81vaCT-77rhMefqels0VgcjXaShQzbe4QHPAQaaefXGWZZwgn9MqcKlX0isiX7KSShWxgpRjmmxxVlivQ2ooT7nrfqfuT8jR4i5uYLRcPXW1CJITuIxefqY6W2JQpbB_eAUtM1pFZV_X0RTdRPkqhr6ZXB5KdPGqqfwHqFtyvYcOg7BKXyteTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 865 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=r8KJrb6dTJZ98kJWOH3cP_V5ftwmkaSJnCAaHt_rPJHMAUCtOX7bMfWTM45Cv0sfVHUoG-FnrqGuLRG8_sfJJBgp6FeST7e5vAsMlrQkaTpdlXO1_NLmvnxvuOVarqJ6LhuR12x6xzU2wT0sk-D7RykyXWBIHHAxl-Fs0-VkR7oeymUGHGY_SERfkP20pftqrQ3g-1YuqqDan7XX3GK2iaKJEaAwqxR-II8YrDVDL-odupUs-TYO10pCgu38DWwNsMEpewLzcbSn8w4Rc7UY8UV1G1B3V-6d6VE9YYwlZP-PBwGiGQJuysiD2rErxkPw1JX17vRuMYOZsw6z5jfh5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=r8KJrb6dTJZ98kJWOH3cP_V5ftwmkaSJnCAaHt_rPJHMAUCtOX7bMfWTM45Cv0sfVHUoG-FnrqGuLRG8_sfJJBgp6FeST7e5vAsMlrQkaTpdlXO1_NLmvnxvuOVarqJ6LhuR12x6xzU2wT0sk-D7RykyXWBIHHAxl-Fs0-VkR7oeymUGHGY_SERfkP20pftqrQ3g-1YuqqDan7XX3GK2iaKJEaAwqxR-II8YrDVDL-odupUs-TYO10pCgu38DWwNsMEpewLzcbSn8w4Rc7UY8UV1G1B3V-6d6VE9YYwlZP-PBwGiGQJuysiD2rErxkPw1JX17vRuMYOZsw6z5jfh5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulxmb-IDOlFrRQ5g5tADcGAcwjKxxK1znuCKhW7nOlT0DYecv-JJo8GQXJlhWq6-4KMiUWcvnQ_YUg89-V4W2bc4eH-gMRbSI6uPNaeneP7aENo92PwFfNfSaWknVV66qUIb4PD93Ccun_7zUCdexuq8dhANjcR3aXgW9NeJgU8rbW3osrLwcHLTcLneoOdiXbUapIx30T_U-qyDEcOwOxA8lyaWXBaDj_r6ZTTq-Nje5enTPByVmE7YZYNOtSdleRsOnGy5XwksljM2OaWW-eDJFbp2v_YeVpjIm6kgkMVLqyQiQU46FGb0VchKXLyxnm5ugEYokenE5F1Kj4OUTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm0iLh_IAdCW3_b-sCxhbNwAfWNkO2qsFVyVkRGRS1KVmkhFX7M8rGNzscoSuJg4TNAiHj4Hi5buNoOvQqU2xFfYSMkiLEZwiSJe9mG8ZIZluo3HLI9fykFxfceCqeMT9puQjPS9db3laKwuU5zD0B4AVuR6RhTXuiYW-c96vDyFQj6zKQ3UHAqPUrnT30Ll4l3THfoK1Pl6P5rCI7IXqTcsxFBJZ280lQW9UcW0hrekCdqxDPFCTgevZTyU0e_-MNgGy0wWNgx6TPKjhAaezsItxWQ2WG2-FLCY-euuUla__KfW7zIhEt7qectkrj8C_CsSjI4SJxB-cHOcD8r83g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5UXeEIpfCKhEGes64shnlA8SCpuEHIFQ0wMqUm_fsXY8-i24zkAHYYKMBPqhpREP-CeYjUtEkyhuvBAlpbbE9fZodzDcrnHadB9S-5ZwSEwHT6AsqnT-A8yyRuBTg1xzIZzDqF9dDYi7hg8xPbIRh7J3tg8ibkzdH1ezGGUomcES_20wdA0kotU0awaz3vkakrKoN8Xa290hPe4H6oCvqk6BfxusHb-QXxyMG0FS52Tohex9mwOeGELAqFUcOwR_Wq6gS1vgxCyit84ZMK7byFKzJlMSfIjRsa4-ai5yz4kLAvxNoRbqqY6bCZ-jPw3yfjnltg3PkgrZm0JKqcJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XH0ufl_TyomuvxyPh0IdvGHvDHEnLHSwXwseYmvO-Z7sd2_uhy7aCrnPIVdMMVSDJQZEQUlQKT_GNbPXmapGys2keTVY7BwhxS1sn5dszJcef9j3RbvL-F2lscrg--KNFG0HUP9LVCDVYjAC-qgRnRknzf6cjLtrdkQgc4mzG3qPuUpBBvioF5cu0leb141BMe4YP-C_9RYC9EdlHjKF_BRSMkLNy_BMw7T5mS_GgkfB07TcXK8_ExcxCUcsdd8pSMqr_tNwfmJGbkqFNQ9DN9Z8lA_S0H_Ot6u_lZCW42nm7kt6j1-uSTeV2iYuQRg0oQtKGP9RnU4lvIu_2aIc5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jumlV3dxyteKb44K4H75VJZH2a7DwL-Jf21mVlsoGhlhRUPSjsGcnybnQvhSdLMsXfsVzLQF5zBnD1cO11AY3f8wZsHMl-Nf685SJMkSvSpPUZ9L6U3Gg1ne4q1MXUZKfPtPfoTxoY6CC0QJFLVs7YUMpul3m42UD-Jm6yPbp7eJEiZfzpHvz-EuzdSaA4lsmnEYz1SklTtf0SDIj24pwsshRhCy5nxvL4Qq4ioN85vk-IIqZ0vVqtNuDYZnUqQiApFaNBLb1oeNw7JjCFhvwp6oE5LnCDB2HMkywciJwPIfUOlY8Fk-urab88ybVyaPvIzX3B36ti9Fj0h0bV0AHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anGIYO9U8_m8x0ibn5_626RKj0EW6iWtfo9MsrjpujgA0VaXnsYWR1KqIw38ONlfZQ1HUHhjLWl9UQxCmbz0aeCuebqNX1-_k8GHcNLHj63ReEeu5jBM9qalfywJnzgj80g2vACuY3jfEhMRHb5p91Qi5Af9Yd5jPdi1wlYHN3oBdXCplsU3cvmeHrRH0CU-h1emNTHk-8pV-5I1HZu4W03WJ_psuNOV-HsAh9oZjADWbvevOTHDituVlT7JuhHNHARbQbWsfD73UpcMhRAyMICnOG6TwXdlubqelrWQ9DPsMj3HCc5od8-oB16NRS9sYMoCE3qI9R-dYrYr7UFcuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8JEkdUTEbWhPDomcWmZoeTfDteo3myXYS6Qp6wMVAiLaT-nMEMsMrbo6mMbHVhpn6pBZEZWmFgsq4-oRA5QGQk3Bvir3sc0HrnaOVFIXoaOpVKph-IySIwm29eR2GO2dh_Ea2Lf7IuJogGvaYqlHM7M8HrpL42rv0l4G2qhScM8N5vgtFtBfIMSISR8hhne3vTzxwDdd06mvDbS8Vsd9ka_1QBVpO4ztzd0QnL6rvktuythpMOhCLeBwL3gCr93nApikaXiVX0iDoWAylcw-84PfpfsLVlHXOcjVAkyGsJBV0StHyC-s4MdgpVpYuhxZ0F3iqv53YKr4CtiHNRLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsaAR9YmDAa8T49nacrvOj2npDnSjuv28B7mSCoMrXHENC5cu6XAAhlXQhMt4sMLczX5A9q2QsTJ_pe18JyIOHY01uTDFja1vSwkrh_-zIezrLr2GEMx3uFLhlRabrKppOCkihx92zREYUffVI4XhK00qBZPePfmA8Taf87WvCRW-Dj6FFmjod3yZgrQ-qwSaINEEg7rrtSBkoaClWNP5AMbYR4BZElhykKmElYd76MSvJ8dOAi2IYKfk7vJO8NVK0LhyFe7WjBvwsQjgrntQYfJYfP5tzjjRvRxrmonv6TTvYBaykTHJIryvIvWEy_bCFd7rRoWxHi9ZM1XCnd8iA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgQB5k8wBtVKKKc1wSkZo2EMlcYfkL0S1KkjAyZoWO4rUUEvtkJbjO90NmqAs5O6xafnSDVK_TgRo8rxNwotrujSk4MLArHyRAwhybKglLVe8NsICWj3emtcuh0-1gGpgVV8E65EGIrr7IXj5AoSkKfiFZMIa0awVLuRGfJqzoBHD1P3sBggsdzyF6N8uQBC8cuTPbW5UslkKMpZmGEIs_MPTYwIgrnO1N2HijRTzQukAGI-NoLUfwOCZ6GAruiTpDPs2ppJKY-wBF0SN9e-RllaOJDTeaN2QPUWOqboO8IqHUx0icnQk0Nk9iCZuPnNobZ-B0eSyWOSe8I-4QTj2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5z34A4RuRO3q6qMR4hAuitEEhgF-RGpVCRxVCH0HaXwzrTz9BfLSrZQrzvedabh0raPNEuqZYBy_Bg1ls2K_cSKfWbG0FCkihQNtDkiG1BeJymHeu1UuAj4S6FxVI2SN_cn-jymT_gdE44u1W5rbwRXM-hrjlWQPRh3FHPleZlzEuG_eACNHGU7qMmvlj2ypbVEtvmKBCsxIyGUtQrUPWjQCTHMa6XNGWxAh9M23aCOomVIKmVdfkbhjD3_FtXDbRaogPga4suYPVw8l9MgKfqH6Nuc6r2-rYV_xWR2a5Ame-Ysi3wmwxszgdiq57CiOIqbTXyS4Cf_jflGIDSPLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDrSYCriMZ8FQxTtMDszYbTU6jrts9H6tE3AqAi9qanXGI1dJinhqdc-jpD8zYjxHJluBvMCLMNgGhq5Ma7gHQoHY1y90dvQaubEuQBiJgNjg18m1fGAAFEU-p9jQM0ol3Qpz5Zq6t4C5FePZ23LJY5KQF3NmjzNTp5G4x18kVLk8HLUViebbHMbsvyxSvSBBmuDt08MKUkNI61eSio8M8mUrkRplXUyF_5SjgBolWgj-u96sPWvyMIpFCzawL0LB7oQdjDHqCiXnvL7_4pitqP3Khy-cDKOC27EYhv9GvmpM2n6uXnM2Tu3ga365d5W9nkBGMAxuAoPdix8YrNWcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQOC6TSW_n758KO9lo6qXFxYbEwJqZsAmRW7RLi0W6M9-aBNBmyFaETDRRGVZQLTnvWRav4iWrL571udjG5ywIQJIKqkM5qha6sAGS6hayHtcH1edv2i39Gj5VAdjrZRVHhyZjDKj_IhqdBTETNLr51AMCTHfet106J7PTuP_FL8JprxJRznhpSkB-GpdXjQnBVXS0MMfvU4B3IxhfXI3QP_S5_-gRWeIf-Y3axnl-rrr_pLzgdlA84UKmmuJl8zt-N_OqEnyDtVfrldBSwaCO5JW0vls0l7RjWXIiS6pYFW5eXGqu0cMTz74zY-Wmd_2ZIoUVicJKR-c5_2AVHEew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aL224dSENGlfXFAJ-aun7gMXwtCMGElJm6xb3-bxsOk0TWCOXx_IKhjJGRVNI_M3mTxThdkVGXQxaHyHGBJYDhzguTcP3RtBT9EiQRhmVZU905-9hqgeW-BuuB-02ZsvIG4eF2s57PxGmD1fKkBUbIQuJs98rv2TJ_xO2fzHL0CHDwNpxhAMVn9tPLPCFBi2SvWflci5EdjvDEt1e8T4WOE2j1_CoG4s1Zerhu002nZPKYM_qWx-i_M63jDVtQsSRq4JQZ1nhcATzsS2mZDjy3r8Wt41WhZdN3lOz3wvvE3TZN25x4itoPHh1xaL35Saln-wNWzeL9eEHKEIwLYmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v501znjdmUcpRyP1v6TOiJ7_msiOI_RrENmznCLRndGZVJ44pci1e6-r7HaIw5SUXudS088HCjm6GLulxKhnUFxQGoahVGvX-U2dGGdEA2bwIRi0Gw5YFAw7LucwRtz1ALYtyUMHJjH1SL8bDdQG2RayNJ_Sndk0mTlWK-i4aXXHRu-fDV7Mz2iQbJf2hIsPPfxgtMjGchuZWHy_zH5CJtXiT_oBqicnq8_Ol8TsILeWBEcEUZHkfH5yyH-mpswO6mYJgjQLQs-BRSFGt07cd5x5ap0Xm_WkqiIAy_c62jiZULW9_9raa3Ow9bVJ3nusg_krJMI06kapKiqIdJeHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwBb5addX_mPQZP2gdP1fci0Et9ft2P5PfwGNuVA29HK25NCsOB1jQFpeSgHTvNx28KX41PTcBaOteeCn7WjQQa4TmPwtDyHLEZmm17I4wyCcnVgblREoBl4Lf3_eHUqZ6Sgw2rcVdXqTtkPTn1GJ9xHOsLtG7ROkheZVHxtE8Zh0V1Rnnqnyz1zjZ9l1xHe_QQySnPdY1ao-gpucmDi2O22FJenxUVg6loF67o0UxzdXqPuas65UEuA8D32OSHJS4_sDnfS7s8lFd8fd7SaJnOjOtiFu2nfwUZNgYSlLhOEt79P6P_JeYsVtZUAEtCEIuElMOemjdZd5Ain6ltnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHlKYTY3KKR4OoO6W05KOkIALkAF4m3onHqx5sV9VEDjVNT1RM8UpQA0tG_4HVnW9OPrOAOtbmd-_lhPudXfl7sgFilk68yIIxv_CI222PKtZtoA0Z4X-gylmGLZebn4UU6qyA_cR4LnBe1exAsMoLqhOGngR13HCibbgk-1GQvZd9tKeP8C0_7LajyO5pI6eDtlPX6ttkml6vk_oYAKdSKKB7Xk7hh0KYdA1rTDKvtVnm7kyLTbZELPFRxtp4a-3XjYxnk3s1HUJjO1-sf0_vPvtl-z_Zl39GpfHPiewxrD6qe2VWhnoV_JoFs-oqFrv4xILzKnegkltgSo8bYonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOhSlrsFy6Ert36xInlvP1PI8AkiDkAqnVn-r_qCmLPx6ZoiMIaUrMos94FmPWs1asw8GDE1fvjUxMIYt22AnX7qbAOVZxbQ3--hZx_OZnpI5axJYmtlKRTsp48vSVHXUlQA6xX2lLdgpbPFeEfLSP8prX9g4r8REQCHtY50yJxinIx_NFg_3eEb2sBpMz95eXcCe7_4t8ru0VwQXTlkAtLF29KGpXW17JfJURTeIhUYGDhtI3S997T1ap6_B1ZnyEVJ9SEcbRzoddtiVwBQ_PdYtn6v5GcKCKSf22FwCSeF1LnuifjnfK4AJwXVc3SHVWt8SIQjCxdWCWq-gAxlUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrn0Eso_AMq9qPDi7xe7k81dvJZKfRWpJUbpUZR46c_NnTN9UDI4pqNhIGTJdyRRVM-wfU2BCgwMPa_60lyjsGeAC6C2TXCp8Pc0rKD2D3AfyoKJxDXZyGQTeDlBIQ5rl8oOqG51gs6oKnynYmQaSKIKoaBz9lxE9aqPQMoGkvuOMCeLOm631EmOlYW5b-OGBG-ySjJCx9BsMW_wUXj0jubJCscHjNt6cvGdERAZrVKvoEO_c23f99e-ldJbFPWIarpqvWKPeE3nLKe3g-q1JtbTBXT9j1dsCDkHgRc3C1n70Xq1M-etPTpUrqCsS-YM7DtdDiJVK6Sa0bNHr1DPSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbMMoXx8FpcSFyzUS0RVp2NvjKK9DdR_6n7MruaXhjsd6QiPhkIVHUw6iXSmEwBA2mYNkn8fml134bOx2dU67Se7SaQEzvZ9RMNJbGDssTcrtTAnytJpd2QSv2Diw_MtosvDuD59VOo9_dvgJ_mYMS3-MTqCfb9Cp1pZ-J9Orq2U_PkqKsmrDwokpDzQpULlo9nvo0akc2GQy8mFDp9G02LsJXfPW90wbF0vl0YtVedcwz1VjcKCdomAMeo49QfaqLWqqHR-HA7HdNDZOFvn7H-WddqW-CQysOPx9hITAV4Ua0FpJkDeBbxLEo-i9j5XGL08W2JufJlzJzS5ZkRSKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD3xyJWD9Xtw54OplLUAxbeMMnK4ZQwwbKcFucPQFOD83YMzaMa4O_8nyH7gj-9xZ7yeqJkpnKOCXjEl_RUXzLdOTGSz0HLh-ikdNtMbWbiySFsnVlnYLp08Esp0ZiQHpt8sKF2KkyK7FY77tV_2R9c695wbpgLBlz0mzw5nbVJGV-k0ZT7fA53zttOv5uX7a-BfEPIKwtB98Lr6Z4zqyDzJSXG7oudpyo6BM7WjIAghSsHfzHl4GWRZzdMfxVjh9h_9CEbZMoe0ZgcZXCg7_ze3_47YLlEcDSslePeex5F0JMUImN8QfaIZxeYxfgA4NlPBsg78QcGjWiiYgcJGdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUItvKYT62OF3b2y0H7JqELrFDqqDVcw8jK1uS5d8lRiIsRzcRDBGpinUhFuwu0YLpcybmRkKbVoVVwrCgd-Pxnn4YE4FJJm6qevxZsfppGNswRJmwLjom6pLlZNhdzEc0YI1zGz3zJgE5u5Ias43eO8QrevVvOw_JxWSuQy3Jo4su8CtpAV4WyxJb4Z0UbAFQQLDebYg-PAiGvmEL6m9jdhh_hU4MY5n6-ySdhsAROfj9SEtCdweNZAiMeSaTlr282TRyXeBxHLPEQwsGPsb9Z_XlV8SMiE-fS4JqlQhFLPLTk_Uf9GYyyUMdqv-JM9XaX2orsgSka9T6PTsswxSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iph-vpvUrv2VV_eFtYwwClR9qsJ0KiHjSSqTOUDPcaiXvrVyrS82AZqndAAbMKKlOBdfhueCYx63FeCcaivust_tStgEG4tROYV1erfWNLN1pbrJuP_K42LDyLbzP4qBPt7rlxs9YKxsSee7BC2Il_xa3l5rIElPKKAtQ5lwOxfjB7w4SThoDPzUPK7DjomLRm1nhPxkjmQzRZllh6v61idCimk1gs9spyGnSfEvQzIrSbusIrlHatkrESkvtDbNah0qYKpyaj4Zt7o4V4dQUSjnt-svgiTNdxR6lWDjHC5YKgoOs9_qL_gCGjCr-LF5LbWnhr2bv52QL_0xQNj2rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_uFeBKvPc1xdsvzg7-SONh6DMd6z-pzrUMagWQVvvUJkKU0WVj_sXaSsPDexoiKvTPmJ3fYx6SoRXJcRuyD3Z7-Kqg6T_WBczPcg8q1iA1493d8o1yMCgQk1L4BrRnUryofTi53QaeuZw7usXmLbgghebAP0ioIx3agjj-WQfxfDC62m3k8iAjWSvlXisOgJ_xte-qnbN-T-spiWx1Eg-piGThC5chNWT8T_qIwuNWJdhsfQDirALK0A1wwUV8UCktE2K9TAI20W7Nfj7dcX0yfLLJxH39vGpR5ABn1H6WU3BG7wy4L5xnsf0RFUwbFRm3ygIo67gCDvagwLuSOtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mo2wZdxmRwLpCWV0r_lCuQyGQS6ZaUzpRCq4sFpzy_3NKh0yl4mz3BlMY26YXUYgaHmxe-FmVE6MwJvuRlY0e1a8bzjIosceI4Da5SW6EIPUhcwNPq_EIN1cldt40kP_4J252kmHBGiAPamcuCdR7Y0hbob9EgXP_NRqLOtjjFzKs1bklpYIsBxL2QXjU3EzQJ6KGWEynCk7kL_Az0jYtT6TUU7uLLJEOs9e6e_FSF0t_arQ_Bju35t29ei_MR86m0hgop4tEmuhFqOPfx1kCmDYi8j0D06EG_B3FH81QPMOlPgztzV51LQDyV8r1p5AqfoMU7BDwjfpLmgsbWsOUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pil8zgXVqY3Tq6q9nuM54cFBs0shvivSYdYs2LF8Y7GC1n9d4QgnjT0vDgUVSj7n4d0jpDyZF-vfpXkovyYqyNU6Y0DhMYmFp3pleO2D2687dcSgaHvp4Msop0403DoSzqkHswjTJHCM4TfQhJ0jQjsQh0z7x80fqQYqfuwf2F5anEGrBrCITvC5pLDflwK5qul5k5xw0Gt2wBCOPTxaH1unju4clm_2UNwitYZFyuEvJkaKb_W1cvUA7LEzyAOpjcbXco_Y80Yj0jOR9lWur9oQqqTGWcZMWU0yb9IbG4dgB9aJq82g-klu5fJUWygehM5A2Pe1wwQJVref48S1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOarZ64J110Kmye5EOQP7JUIkrwsWiASLNVYDDGT0xgwOGlVo5XiJ8lSkvdmd8DQ_gSCNFIGNw02rgRoheJ2wl2cv4pwqYrRWp-lWpSsKjhOYQp30LpsqXWxf-fHbPODqTHN3jCRwYztZgs952gkbK5GoJfSCJeVJKdQB6H5NYkONAVYBFDOoBg4lHTm2W1QQxpo6XOBoA4fzbl-VKbXOdQyI-f9oiyO4ir1Xd4DJaGWtl3gRRtdyqT_m8-YK6yDQ5OjFBxk-KPVVsXQi7N8otFcqdTGm33xoAbgLIk5HofsHJxvCICJvYDBqxlClMm4InP0R30I0OxiMquJ6hX_AQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNxcr7f7WtxDgTEImKXHO0uSP1sO7k6HceQcjpZTBuE1NfCSvU4zLLnkw4KdtGXUuUagXHWxBDYofR-DLwyouc_obMwzekaY9YKzYWIaXl7uU51wATsPTpZtbM2672eSSqkCD4knQaNAHdmjexJxnHpeK9KYY4tUvsGrGePanBCYwd9hmqnUmq5yNKHcAzHCpX-a_o-VKcjOP1Ybb_tN4-ZG8PEq5NlUcZd-8n6QfP_9SCDNcFwUJrc2LsTn-JpZ3rU5d-iRlg2kJGh1wM09meXGzh0ttDdYkm3ojAtb_1d6iw7iHPb_Y_qiPEEdxKDB08g9YFQ7fYoEpWN-lnrmGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMCW7IdjcLXW13noJ_W0tEBIxFTEAk5qccawLUlVQNzS1Cjm1eaMXb3QpKjb9fK4Q9WXxxrVGBVJV58ZdYXw54-EjcEYgHY-m2dC4d9vYYd6Df0K2XaJ5jNCPZxxAiBHHtxhLSLfdsAKTrmn4m1m2KH623p_gd7Cv7-iw2PCn4QNWiScI58bLfpLkf8qMr_oj1ifsN0EtbduwfFD4fSok8Qv4IwdY7JCpKplm51sb0LhXZPvUMCV0gz0TebVoSaX_-vPkSZFEVJZG1rQCfTuni5zFjQ7bf7tnTB4C8FcSwEGjSsru9lSLOqKfCWAHJT5MhpDNGa4OG96wlARllglwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 541 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD02lu9lYbVy6qFCh-y002QPlMZztTgtUk90vxtpINDuxnrQBBVIzLlS52YFcgFzWcuNH6c2xhezd4w2pEQl_l3JulyZJy7bH75WLzh-CsRR48vwVk68t2mWbQiuxU5xM7JJTK6ak4e5LFmFj04b3wzipUkV3Jx-arL9ps9kSd1uqAT4zFwfR1sER6aM7Z8yQG30LOrKPM31Ohex93F2ejqTNRg2brwg4hfufHD1sMdIkyLI_doszqkU4slV7GbHbv55zp7EemxZ6BCAVOdjURfO5rKh3FRrm2q8lRWCobV3Uv21A3AR1HvE_6THhlFNEBMvjUn1VgrzW3f9CTj1Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjcwv3u6Dakm8xJCMIHOxw9O69PLE8bgK83GERl6PRqXZBi11-AYdLplrXVsPq6B2uoNDfe4icm1P-0r5w-Dle-OHWum0vaD0qgfe2TW0LBXuwBiNVxbK2impLIEynjutUtWseFqS_QlyWaA-EFuKYTRelGqKSHSlXhcIRrfHB_l8zkUD_nYxqDbHSBJAeNEqVXsPPTKSojxJBOchGceqCs58Qa2oBISknDEF78mjNGdfOeSJroLBRiVRUwXePDXbsL48P5WHaq6YXaJHtEVHAZMZlTe1Dzgw3BtVcVt39KgtmLwX8NQDEB0raFvbxjqIAg3ICksdgKP916IqPcLJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOYsFBeJZgbBmsFvV0_nGiYuVdIboCzQuSMRS3X_P1VmyEn6bnNVtwqZLjhIVcWUAtb3CKCpNoh6YNbPohmwVcfHSfK2_jUEYLm4NOVHZDe1rorx8aUMA9lXX5um1Re3h3gW71EOMJ5kmuzeezCckxp0l2z2viH37YBOeVQElGv0oJeWYNsMj6ghTRW0oJsyKuq-zCaicTSK14X9QESOenox3LSgynh3Vi3ej2RR5CE2hNzx0fzCuph3skjLC6DtdOUdnJPwjTYqXwsdS4MCpyERD5cpsFCYE4uL1o2fMJB1eTDts6qe5YV1X94Y57UQOQxH4MuNradrBoMVUUvCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POK9ZprI-tt5C_ej6t_UniMcTDvhbpiEM-h3NO4VIvFCW3mr6KUfPlrnj-cyzje-uA7GCwvvIyvh0HE813HFJ52vyPL_vj7NsrVrBUnhj4pCEtsQaAZdYRNsur99MENMLQiGSJLSWE7PDN2VYSuW-4FTFAU4fXnK4mWD51lXBmS70bPRiwJkgKDsoOnNSzwXeZZr4aIKcxzdG2vfW0ZBols0PuRGS2D9FrEHdsuckgddwZWSe67S_Y1lN1x4kjGwlhc13JiQIW3RiG0WQTSGzsNyKe87QSHwS5MLOUPhs4UC745aXycZvoPfsdG8Qjsny5tWk7G5FYhMY0YxUDPxxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoSwkPNpPUf7_zKy6O6-NauijRVqpQqa5GWJ7-ncRT9iG2pXooGtKO0yX4aybD11OKCxcqmy3XdhHfZJ1NUr-RaCk1xKPpHHfgwG8NwyE66Mruz628VutU5D3aJAmvSfOEbHij2motunPM6-PM0ph3Pw6DiMi1dpZWTMsPXs6jg7yfiXn51uzuaqGFd7qmPEm900Re6clsmQbYqqvrgjEzkPUJVureOawbHFuWEOXoqQCnnuOMESTOqAjBT2oa1wIiUh8WIWtLMNdqNxVyP4ZLQK5V2shmHbqqf61iyeG8uU9qmPzfgrebWIwEz1vuT88Sbkmto1UWlpOOlTOtOAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSwYL5lNN1_TNi2nDaOsE9BSiW-JoHCvsDxEYX_lXjaMPEfUGWJyj43Vx9FJzJaMBu4y2tu6tFaGKtp0jPsy7TcwfmToFgEtW4V0LWWeIGK3HE03j90Hu86-a50XnTw9Q0vkoR8hyAJ5QSVpkgpS7_c2Yr49-xWaLU4roLGy5abm0A5WUZkzqaza9xSjxXjQlOT1ehMIhtrEOWlfMRPdZH7rarRGHxK7zbT5ZFezvyLEB_X_AbKGDh_qxv3l2-z71puCInSTu8Vm-nfsfX7lvErPoOcP1_rvC0dZQdaigeGegB6txEy4bmCCdH6c9QZ4uX3KAB6eGvDTH_gg9w0ZrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1uhVGJeKNWGVN2kiL9oXl49qn0WSHpis9AD1WU5zk5ETfun6ag4tHLjoR9vbd8xkvKjtlmr9oYelyx48jEqTo6Za0Ci3dV68yNMBHKN6HVGijkHrTFtcb4gI7oVDXiIENL8ZAlL8PV8ACuC1nqtVPE_0gED6wqDxkksp-yZXfzT8HFB8DGMFMVkwIxtA1wwuYT7LuwuQYVO8LM4wsKU6spjJ9_HveJCc9MAyL9VPBGnjx-HvWTX5JBsmRu3e_rjPpta0DA3dGX9W_vk1b7_1z8hbT5wXQvHXZ4hcewk9Y2RomtbKLChVPXDnsDax2arWCsWAvgRI_Gh6L1-8PavWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aesMeOzT_mFIJNu6JBVBja0nh3NqX8-A4qjAJsUnpeFrj59ViG3F0QFw_-L1mVEJTzbzSKwg850LpQqk-FlOCN7n0XEjei-22doIMMkcs6g8YDuXegf8rya50H4CpM_KrXHZ6HR525EGDYXo-NclUy5o_wkUo8Rr-_1xAqzLl_tZmCmbxQE3QPIWndVJRi6uFvyF4hrJNnrVVEHok1PxTGwC68N3SaKXMere7iDrWLCvZEfIpJWbHmRH3drpIY037p0U49K8yayGPx12MPq8N54PyzWIEzTlb4MB7HzXAzD1ne2BvFSDNGqrm7dtTglevuah6HA6AxgUrr9CObTjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2NFMRfVClF6ppEB5g0cIK9Q72WO_z1uAxtNs_YVGa6UDe5pNGEQ3UD2wB3PhmzXvzgnzN0CmSBdG1XIyvZ33L6Or9Y-SPbcXF_s8TG8_xd4JL0FKRenEOGcJbCnYx5miVfJT6wd64aZh2EN5LUS-5lyH_a7lgQsoDXL7J7lpyOF6_i9wvotLaPGFDsC0kAuiy0918qJyLtwIv-EeS4of78Ilze4bjMnt4KC3FkSAZvjXBUZS0E4Zc3elFzIutYKiLUfRpfYivRRc67FzaFNY29gNy2klcT8rLsanOO6sxw39PMfsJjGoup2Ls46nIIe1kGvcTqsQHguYYnlLj0j6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4b-zJGg1tcoQm_nJ4W3k9B73yNkIZEb3clejg1KkzZ9MpVnwTCCriA7DSBjEi72402sWBHKylrHx19JewRh1xOt6TFeVwabEmHy40yWtIfYtUZy4JMRIwZyonhEUiGXrbPCzszalWD8ATNhBNsYdrjIQVCT7pbdrb_X1VK87vrzP9sGUq0g9onsENtqlsJQIsZ2V8d7L12c4Du5SXySm7Uw5wN4PcrvVcU8134xUUF9JmNRUjtpP0nEq7EmR7IcOk50Hodke3JMeu1hM9AjjlHs_TKuqhnmYECuSxyfyrqkJ1K1RthnbQpPdRTs8QEBgncmypEeoEwI1HmbHsOSuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf1eqzdHbyqYfg7pGfF-f1SRcKfxiF9sUJbRIGqA59LHl7xdwZvSoXOtasQ1x6TW_B-rdDvqHGUxUQQFlnRbyUtM5lUM5i2mJvXaKGOmxu-J-5ZZIzzW8TkWjTxZPD-X6ia7xj_BpOCglqCgvCJfARbPXzb8kTR8iYFfDNDJe72naOcDqiArBnLBFotCbxUoP-JfuDCFlfcMfiHRtItwA2Y0Je9rgRqFFZnluH9Muls-SdsS2S3ARK57iUD2Xy6JI_EDBkwGONTi4aRVvEkdSpwPUORf9UvrmHcg5SPmJy_3MPlC3Zk_9tv4scBrSzEgaFJlhQsgtpcDHAWk--FouA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulDXg_FvhAFWiwcRoyV9SLCiN7Jn4-0aKFy7SYvVf3NcLVyZEmYt6-Uq9gOQWiplqW36_ODPIwJ33uftmBy5c9Xoj354A5fcoSXDu200nRuI5qcwFfXT29WK6gcxejn20ypikQeX752V5ZARqNhGfRw3mgtce4XM6KtTS5MGNODuJpOL-kM0X0MbayJj32-ZrE9ckWs7TeCB0xAsly0kwgzkZxDG6MdklI0pjJTyEr6tvlYCS1Kb6NWNeb6mqHJSlQAn_b56C8_WR3DXEEW9qGIkMLO2jtRITlJD1kM7bxIKa5-XKzdNQBw_RMOwoXC0ObXLbGCUNh73ew_yfOHlgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UT6NWEOGarjwGwF2tuK-1j-RLx9BQ9eIF9jT8_WsGFd-PQps2oOSE2OkF771DqqUAnHeYcVgNGXg-LpnxVjl-2x_Ca1pv1YNksPdbSWs_04-jboAQx1gLSizTrLQ2MPmT7u7HGieJ1uciwEZ2VMYoWLkJ3RvayV3E_fAB5pAYG2n1iAtoCIbLjNqk35AoIppU5Q3PqQvNBtOMAmmT7eFUgo0-rZ0-aolGO6V8TicWV56KsHQSRRoEN2UW5Nv1p97b05zlOz3diOGW-YTboCkYKC76lSgLzExI1fJhLKTLgeXyuUdg2u9JsTNuPg_PRmpExXkCnW5QAqX9b4XsR5hmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzwVxqr5FX9d2C9ZSSdWPg3Gxta2KSUDSnYVsmz3-zSXVikoCl0ojq53_3aECUWDfWTHbIq4l5PexCRL0E3am7S1N2oua1K7ZUt31Hr8GWBfhBzq2kk4Z-9Ww2k_XzjVgAxuDNUzBsqMEVo_TFBsqLvzf9GIuc4TtLb7Ii2_MQMpt76ZvCjLsXuJABY-UqVlMok9rs71R6usfdxPgjIsV5HQlc6BvqOkRx8I01HNegdiJE0UlqG7LNkjClLsy9Krfbz3d8nRjgE5uW07bbW1NrT2F2i9-hXP1pD2fTzDeJdCPwOYr6WZWw72Wm6lUe477ehjMUdlUStw1NkYD9Qc9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDZyGmrGofOV129IHfXw0JaQT1oj6-qjQPJeFC9NSMErOeX3gKxpkLs1XWpAnB84rMBsyImNlw9RgDD3iqoy9iJMQqdanWUdpbtfzpVG2D-4ItGI9EB2KZm2vxLbopPDYo9RbXW_LwBdv8CGdr8zsKGSuA9B7-KMQcG65P9U5S2f2tDjJlMPdqh5BViRyJdlIlJ-jK0nuVCepZJgj35agrb0pzst5nwLStMzDRN7TB1Tqn_LxnE_pIkn6SFEkxMqBMBGYS3rFImDnRLLn4ghvnI4E63MIA3oufou7E3yV6IH3yIm6KDOYYC4G6P5njV01lJWK40YP9kvPP8cTKfzHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtpFJP748SM_J7jM9IFqE1KhNjy-DQ1j_-hzmch4vla52UPu5UMHFLW4e2KMmGiybEwhBXl7wTePnLNhmwUrxetbOyXxG_mdPXZeKrUuXFc644LmrtnbgXkQpEH9llojv7T3k5UqxdZoksyhIaKJjvVsOTmenjjWskjXDPwUKrws7fLIZhAYknAw4lwpCRCSzG2hJhEj9S8nicAXnjUkO4DCVZ2Ci2xl49B1bFr360zBDFq8llsGeoLej7MVBkkrmF6n6O6A3VU77C6XxwB2EpM5d4dnnj7YTCFxNxNmHKbwL05vLlKlDS52muiwjoy6Wi9dAFEHq4dEwV_Yve6Jnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMwmtIzfAsAJy20_hzylWwwomrD03AGC47blBWb1A-UqswXsXX2vduuTs4Q7vdA4GVwBn2Ne3TvCLVisZf5c9l9VFUHMxxyTgS3htpMn4Bw3UsMZT40zlFEkmk6BPaZKqTNWyLGqw2yssBJuV4jEmyIJx7YXswoEzkIlbE16dGQO0PVONO9yAHKYhvT7bFFCe1Of-bQ3H6dzaQhBljnr0r7F95qdY_MpFBFPktqID-lK9wSOOn4ZDHG7naBZ9MtaCuR_TnSq54PeOmUk9fZsYcR0BQPlhXeJN4vbW5JW4VGZVx52EYsXxAghmkHmFrxVHREFfNwlsPM7Xay_Q3c3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRq6q0a9LJd8FITld2qXNUZWHFP42soeC_9si577kDt9mEuwix_5ZzUN70pOEhzmHsPtnKl5UMBTLUdBR4N-j1RMzFtsaslNTEJClkFJP_xhmImGBeiCfIOwz-jAsAtHditFlvtS69MD8RHdsBAUu6XwVyXiedTOrjkqMAr32eyKFLGyRmqZ7wf9sVLkm292oEuyVL-5ZHl6ZS_CrFvOAR437OUSQp4fps8XBLHCQfaheItO4k9SCkdxDMbJYMYwk9oQWmSOPOsY9amSmDuU40_uwjUkj4wgudROwyKZVLBKR4DykKSU6-Q_rHhqzsf7KTbUdRfCP8meT_aroKv_kQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=WaSZXjprz_sfU9dI9IZzGZZDV8bH6I5VD6dOkMuFcRhAHFcrPlxMftR854qvKO1QAfWtVw_aVTGkf0hQHC5RoTaZzdE6iFbZNYJc2vF7yNe4LT-D7Whj_zHgUaQBeDsRDwimC84WUGh6p0fIUh-vznB6lgHO6GziRWGzVu5_lgV3XI_sTAQIpzDwOpcbDThLf_8RQTP52zke9KTF2NHG-650dd36kyB6qTsZ2SEdyy_CEVNAFAEtmI8lqx4Mci8db5mq3tgqzZbLbi_ZiyEgsLbSgmguhfeWgNZT2Eqm-QuNUCbTr6Wu5RCAg0ATa6RB3RW8H7sCkUeO0ltP6ePzJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=WaSZXjprz_sfU9dI9IZzGZZDV8bH6I5VD6dOkMuFcRhAHFcrPlxMftR854qvKO1QAfWtVw_aVTGkf0hQHC5RoTaZzdE6iFbZNYJc2vF7yNe4LT-D7Whj_zHgUaQBeDsRDwimC84WUGh6p0fIUh-vznB6lgHO6GziRWGzVu5_lgV3XI_sTAQIpzDwOpcbDThLf_8RQTP52zke9KTF2NHG-650dd36kyB6qTsZ2SEdyy_CEVNAFAEtmI8lqx4Mci8db5mq3tgqzZbLbi_ZiyEgsLbSgmguhfeWgNZT2Eqm-QuNUCbTr6Wu5RCAg0ATa6RB3RW8H7sCkUeO0ltP6ePzJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx0xHvHU2d6f516H_SfDtDC0qUzKVIVh8Ben4msKsp7ep35Rdu9Q453-OY_JZ6CgGn-RbzAWg6QyYUI7llg666BA6vdZg7PyWh7u0F0BCrScB71fPKmVDIl2gaZyfL4DbFU-lOOvunjTag4EXzsSjNVi0KnwI1rDs_kWd375c9DrulxiANzOBIa-TcF4zdmVlwARC5h3RCoT_EdcMs9AIfHnWzwfSnKm40tt76NndqUeDcGbHhMH5gbRRYlawVj2ipRjsYUaeuqRJ3UdzbVFoN5jUnRCloNZslU7VJr_9gXKws-2GxHsMh4z9xAvev9Onj_aJRK8CbuY24c7LGBsyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhM-plHj-LBEiaqSfYyOrIVWsHHS73wvxNslStUcW6pEQ-vg-zbv9VhvdUEbZuNMr-IvqYYe4AFIVJaSDz9l4zR3iGkwhK04V17Mpl-U3tqkaNtTtbj-yDVHUvE-06cf73d5uMlreESqgj-S7ndrHxwcscjK5X-fRqQmgr6wu-SvB-YM7WBmgpmc1OoQ_VRr9Pcao2ivvhKeSAE2a4PyZnM-j6javXUFV_pHwqfZS9UIx77makH0AF9_OQxgYSLflhCccIMm6j5iLMAi2kYYZrkimu51ua6C3-jVwZSInIPL5EN9qubg7pSY1H7QAZiWasoOY1buayfMCCmnYvl08Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWhIQO37BWyROnfX84hMcS70RCLvnsaD174oWDB1zyulDKWRIr9E9GfshJSaS6fEMUyy-HHfudPr9D0Wxg5QlK6zZHOWw5Ssm-ucixkjcE1jBuDGAZxZFygjImnKyXiQdKfBDN37R5ragHiPQvnTlHE4GC_dKEhIMOHfpKqGfhCU1nos1xCb1dYRC8UGGJS5ophVdbl1Mt8v2dziaVPL-a9h-Bz0UUxEdsz_bX-oODvKB0A18CDIE6EjKWi-nlhleVV-l20d5sPJfdcGHqdcgpNQBwvrqh9cZFrJj2GE0SAXUhtaYyFqDOdb4ucP-fr-YnS2-Lv4wzZP3Y40hYoQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fW8SUE52aeQqiY7Z2srbTzL6S_1ZayAL_sDXhlv9Ou2xujrwQOzHk5zr-VFD4GLaOfKmaMwctVr6JMhZj-s2FeyFbESZsibsP-fc0zD1Oz5IzT2CUi-bCVQA_DZxFIJ9ojPaRvdhK5gxAKe_O_W56f65h6U0sWEocULENS7fZ2jyy-LdxiD4ZAh3FXxURaylRRoUNceR4bsbUJNdrLvEvnI7JQ54zyJOME4ZtXFrVP801wl_FXfrmIdfOwahxXP3nvDPS3ED-3pa2qwkEFfw9qdkz0gSJFaCy2z6CWrjH9dmJgoTkV_yowocinzYBr8FZz8oqvHJkmZH4Jac-pM9oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrXrlrIbp9zzUZmDvnKWX2UkW_VIMGFSYMhlaOny13LoNOglpxR6Z8SArBTtIZwMCo644usGmpkuzHyzt5TTzz10BjsBqoR1gnS3eq83bd4FwFZsyjtgUNLxzuUYovJqDua6SXdfiWLWJU75gUbbAh2DvsdsK6manv8JoVC19kHysVfyNa7KHw27a2P-nCzepiYWld3eb-y3-FhwIZtrP9Y1actrn8FQukkP_fw5t8z1_qp9dftZMbMN22QXjIXf11-DqEk6yTXLaDNBJvqtsMDuQHBXJB_-1uXitrq-xrM3IpMLj8mzxEf6GTD3y8JN2MSyPeLEehQ0Ax0cblVm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuZ6Jo9UbJakrSjeF7U8O-ivmFJ8XT-91krCjEnsw2zBwWGVru75BQIA70LgICXELMijmgN4XS1j7AVMNFIK5KaPUw5u0MyJ5Ua9yRC6DmqK4-2G_SUXkYeIrPUDE2aSyoelTiHAXj8BSlG2TR_z-cMLOrzQgMzxAOq5TT2auGapY6wfVc4sYEmq8Tn5KmvGfYk8-HwuDFcPRbrBv5suKXrIwX6bCujasJ38o6rzP8Lz6QPfpKWTA5_ISGQMuTp7Cjm6vUWxiqapm8ptT1XYdY6YwUgSDzS1SOD49aL3DXGv8Pk2HOyfgstwSD8Q9c1BGgGA21wrlssdIRHC5THHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1vLfJtwtJsQG3dlrgPAdmunD7-8dueqf8uKnDE211Q8kLXaO20LV4jGk9RkXqIvE4-V9whnzC2WsZcvNfS-KFBvDi8FXbXKyJhxS1FBKxk8KD4-_jD_yFpE-Ok8AB9GS4PTkug5xByyy4pb32ORYxNp39Zec5dJnT_si3e3hmeL38DQAXrEJ5ZIlTH0sCj0qlN9zZgy1FcxcIZUJoAfDJ85hZ5O7UPe7pKGSRXdPAZC9xN3yiJqzWab28e4J-SBeBw9Ayu7BWv9Wk9M-JMMSEQqSBL4bNq-Xk084jUFbtm7dBchQcLGDKZTy9EYnRvej-oZMQiwnUGWhwJe92vjJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=X2woIS3v6Kwd4hURONTPpDTGQ6rWxEitVBIwqVan8MU95DfrE3NM72BJ4bzv156SzDt1K_g7wIyhZZU83lqCNGotmfn9IE82YZHNSX_sZarCzUzUE0-6wjpTR77gJH1Xh6_QanMMnYkO6N3zeRRh36_0t0N5zhdtXaevZZo40AQ8k4tCTdktTWBH9yClmnLXasqABjNOD-TuPnlpwp1AFLCXiJepqEXFVFTcWa5pzCrePtfq65dYNaFrEQvvSgpqNx1IFUNAXulI7hP0LJvGY074v9wjoXwwxKz-_zba9-54Gal9n_Wzbkl9oZQrLnWIn8Giqp2wTJCNClm-KhXHelfZWQ0Um2obU25VhJGtRKdXNNciJl6fD98fOJ-gt3BySyqzg9KRAQkvy4iuj_KL9fTS8usFQ73zv3FMhqfKlzJ_akpdlZjh8DItKcMCofPA8N8HiuGIijvxpxiIWnkXmVHct69XCDozmc00ehiMmr5kmnf1wl7YVyufQ_I-3Dr76EmOQzfV2Nv06d7vKDuV1E3IJiUXkTi4-m7u1yFF0cFMwxN6ha0kGSN2WU_AEFosdZ43LTCxIVOgEWJXuNlg33m8ViExVFNfrj-wsJuTWZZWfKnsdqSRrx1ViB0fXBuhXbUGqnEo_Vbif_xSgEKnbWyVIBoDHTGiZ2botXQIHtU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=X2woIS3v6Kwd4hURONTPpDTGQ6rWxEitVBIwqVan8MU95DfrE3NM72BJ4bzv156SzDt1K_g7wIyhZZU83lqCNGotmfn9IE82YZHNSX_sZarCzUzUE0-6wjpTR77gJH1Xh6_QanMMnYkO6N3zeRRh36_0t0N5zhdtXaevZZo40AQ8k4tCTdktTWBH9yClmnLXasqABjNOD-TuPnlpwp1AFLCXiJepqEXFVFTcWa5pzCrePtfq65dYNaFrEQvvSgpqNx1IFUNAXulI7hP0LJvGY074v9wjoXwwxKz-_zba9-54Gal9n_Wzbkl9oZQrLnWIn8Giqp2wTJCNClm-KhXHelfZWQ0Um2obU25VhJGtRKdXNNciJl6fD98fOJ-gt3BySyqzg9KRAQkvy4iuj_KL9fTS8usFQ73zv3FMhqfKlzJ_akpdlZjh8DItKcMCofPA8N8HiuGIijvxpxiIWnkXmVHct69XCDozmc00ehiMmr5kmnf1wl7YVyufQ_I-3Dr76EmOQzfV2Nv06d7vKDuV1E3IJiUXkTi4-m7u1yFF0cFMwxN6ha0kGSN2WU_AEFosdZ43LTCxIVOgEWJXuNlg33m8ViExVFNfrj-wsJuTWZZWfKnsdqSRrx1ViB0fXBuhXbUGqnEo_Vbif_xSgEKnbWyVIBoDHTGiZ2botXQIHtU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5Q8MWHx0B1vhPhAKZBGtWE4MMVl_qe09xb7osq7Zdvkm_AGJTtpMyUIoVtxLSdfOnohzSE_BIvtQhtaRg6Ku10hJ2Httazn5Blyv_32QSTEDHujHHHErSffcbNUW_oTb_4g4ZG0jYYhn6IGscLv39mQ4WEz6LtX4pvSQ7L2R0R9ZKFekhNYuoqtjk8p19xL1ZoA2XMjk-7o0zM7GId7yjBYc6Sz-ygIVoNyk8jAZoJgfJYOP1HOj7E99dgE05GpH3GEeV4Q28kOGhdCkJxKGx7AzLbAZq-S4e-rAEJARt--fzIxEJuE-FmL3Ba6nbogwIZA1erpAL3vLxI5TmxY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIRdV4zx0hyuw1Cq2NgC0w1_6E3g-9St9sio8FryMDCIFI4i0N50Mpt8gguLIEUuiBYf41H7e8O53qV1VyEDoql3On3z0qiX5dGbO6atQgigi_jPb0sGSS1_Z-oWLItLl7J80CeZZQ2sATdsQhgzbr80WkuGF6aW5ugQSxb6Bd3YzSWHt7PPVy2spQRAO--fskHx06Uat2TXW8IWsm3bJzBulIMKrNWFfv3mV9EiKR3qePsjP8ffVb7GOMV20ZHzaamii7tNKZWwlN0jt7Gw2pzmJYr6-3QY3AqKjiQe5N0sgOajWaHGzNbWWQJVHExzNXy92Drp2c_QrV5Jijyi4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JqdU_t4s8EzH6RXE6_BRztFf9PK9NBwq2glYsqEB62Ia60S8iEhPKYPoSTq92Tu6zG9PPvf1M4GUuIc3sTNsbK4meieWxxHFiFv-giQix9w8ucVkH4BZiV80TFXilJ_0BYXPaI0wb16C7oDfsgtoIaAjdDhI_E15Mx7lSmCu9TOWf3lOa1w89vVPECAwLVZHl03_I0-EEpUlw4czns9WCsndpvnFQl1OcCN5mMlUVaq4rF5tSeMuhk1FD9G6sJ4TN59HFdzSePubUnk0wc0xFdc7n_FoYEmeKq61zyg9AJb-dla3ilrRgCMkG8yOJWcGIMV91TXGaOQx6oKZIaCo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQuSu4xMXUP6aCtL9R9cu5QMIF1AR3U-AKNiL7ZD3-RRDdZ975xKWENeerPhxiz76UkdtBOnTDxFTWDYmtbRBplgi8gJ4pzh3HUVtF4qiaoQo4nIxCsY_2rGA7A0EFhEPD_K_OVMva8JxeLAt5zi4b4auwISwqsDM3dS7CKZ_PwSKdGU93qHtb6ZaUOTXxuPY78LQLD29MrKv16sD73_DEgP-TkPcufrBAh2Ngrw_C9SEMF6uhMRtI7iSyCAmd-zM_4R4voyvUy-hHc01UAJsWw_ZB5HRVayTLpmTIUnw7aCVdEOnvfmn7I_SImTcstSI-ReD6_POtGyIMvJIeFVKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q29rK2EM6qxjCjc1uBRzuP3UAe7AIruWmogliVJsaIKIcKyvEHgDM8xhsxAcwlUpqAzFVjL362cSIwK2UPk6jwkNEKBj32dl7bMm0rwNrH8jLSYmXbKIb11zdf8GOlrcdOhe3YSv3_kI-y8Z1mABGzKDJvEOd5pm8YYpBFaOMZcM3O9VE7ImCPuACcyM8tDvOOsdCB4oi9yRolOaDxINj9EcWm9tFWp9pyVQ_nPA3TnOqziGQdbJV1BiEnqhUgmBpSBJKBdsfyqXiv_4o9cf8DRElNHyR7xFvqMitg3I7JyPFgaeiwjt08auUcQW_VXG_3LOe8lvdIMMaNx5KMxhjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUSWNivw3u5Wwu-nYhRyaiD81F-xMHb5nk22WBrjGsJAnHTrehw3brmbBVA3w9Q3PvXLGuFH_Je91GYIUpnnMyW3Kp5tgq9V4F0ZhA9xMRWkPeMDyay08VYaQLC8tr2rEwtlXak1REtgjYgmAOqW3oVKkK-VeuMZp7FzxKH4Mh4XRLEf1b69o47uXwfESRCfVHQ5pAY7aIhF9Qge-SqeINkY1looQ30937rflA3cCms6xVAU_EUMY0rcHFLgs5lXbiLTbqINPG6g4dKMJNLuQMCL2jkYTNADpk8Ru2SLz2xGNKIKOOosgcUdzqYhsNArdcqudiZckBefv3MwqrRiQFk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUSWNivw3u5Wwu-nYhRyaiD81F-xMHb5nk22WBrjGsJAnHTrehw3brmbBVA3w9Q3PvXLGuFH_Je91GYIUpnnMyW3Kp5tgq9V4F0ZhA9xMRWkPeMDyay08VYaQLC8tr2rEwtlXak1REtgjYgmAOqW3oVKkK-VeuMZp7FzxKH4Mh4XRLEf1b69o47uXwfESRCfVHQ5pAY7aIhF9Qge-SqeINkY1looQ30937rflA3cCms6xVAU_EUMY0rcHFLgs5lXbiLTbqINPG6g4dKMJNLuQMCL2jkYTNADpk8Ru2SLz2xGNKIKOOosgcUdzqYhsNArdcqudiZckBefv3MwqrRiQFk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq3kInyy7A3sztj-SMBM26CFqEN4c_vYXk9l1wVjAm23FqZKjaNZgXk1VfFnPobgzo1lAUgAMuC1auOw1_-R_W-AttdtbpGZrYrLN_AEL6LAuQxTGBrJWk7wxLVIl8LPIv5cBgnhLyIgKGbfxCS-lyGDj_eN5-ccUkeRMIQKQGdcx9IfVb2MaGoz7FHiKKe4BMaAEV3bgY4nIDj4gaVTTLseXJIanaHTl3xKMrvvVnvx8SkVGJgOQR53CwqU_Zrsf5OMjFmhMmKkP1xI3qM_7KyrXjQ8GaozTKnCWXuRDHFtQ2kw3ZKicdVhi8XWUxmG84wqa7faA3LGAV7-wv1XmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWNDu8sZG4_09zqsKEsZDd3FBRf1eXa__CmR-OTFoTErUfzBToO5LqXxACnOfribVNp0RYxyVPKGirwmMlM8r-UwbRQgUf69EpO6px38etCQ19xk0P1gyRHzE9B1Nl5V6zUmfY5J6imkuB7yJiE3pE7OgPYJhC9kC4R8l7B0woyxkdcWSweseZz_aataeINQUoSBHRiQ1TtIlHI8DDYv8EQ-PkyB3210YB8XjG9R3L1MxqRXcLWZEicfpsNHDxm8-Zzffb-miSuTpJmFfZ46hbWuWQVLxMy8Fklu_brAlwh6WnKnxp3WXmKRbaq_nO7KgojCfDyFKhd7ZXE5PI82_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LH0gRsRa6fpiQujDCdHh-HXNKcoz2kkCCAkyc6GESvShivY7xYaFKeMQgYG9ey2BLw4xo5_PWsnjC1J7Pb3ifjeXQviWjkDkhY0HM0HRg0Qr5Bpm7aCHkiA_cmtSDh04eKRj7dy0roX1EEXpEE3A5ii4ITHeyzjklJHe7NVzUy1AQBjUe9grh45_eAeP8msmjorK4wtP0Ef_wpUb7nR55481JS0Ucgvh0nCGjID3r0OdqbxweCdWYZc_ge17GYuq8cV62Knkjfw72OLsJ_8Ysuaqj-gyKv0SNBA_H-SbHloCnKgobvbkyiI3zC1IV3PyVNPvWsYUt_yyxjMdO1D4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCHu21Utfc4L_tiKdYtoVF3oCzrUwsm8RYS9L9k2EmXn_HJ3vLEDdHpwSWv6yAjXZlmD9X6trp9AtkGcRkukOla5QU-kMuQF0X4JCXflTXeuxbOf1fl3pMSQvXNZLoWTbYbOOEEwaRlI2pVtldXXzkQqGd1fSE7Ny6TI4_rlaAdlXpAZcm3pxMuADxvW9Z1zGi6z16fwL8skM22qoTSsDM5WwezD30Xo_2cA5gCe-uebpe97U8tpKCY8-TvV7jhFH7n-DDvXooDuHayza8fAKvLdK1RNgX8QQXyjJq8X6t6JGdkExELJshIErbQXoQHdyewEdRpfe94uGrSJBzuEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGL_4eiPWnIhWVcRG_0I46W9WGVJEG5P2TI-0oyjzAzVUIDTf0fWWiwZyjEUcn0TgxZICgUnOPOdvVgl5K9BfeXxasf6_TgJDwZNw-SLJuqOXnCmJGpftlyv49hWtQiJDREq0SGrkwhDQs_7L0k7dT4poBbpj09FR8uaUUuhA80pXO6jyB4JgM93YXhffO5bmXM-0-EeF6pDjnmXcojXeCOq64MFqDBP8QxhUr-rCAAFE5M0RZ0D0gThyHOJ3f1vSajVki-vorEzgFugtZLC4Jl0f_Pr6jYzp6VG-oMcxBLHDMiXH_vbJgu0fTD4li_VxQUrFgQU3r29cDxng9SjVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci801OWUlyyt88l7brLCWgFiL2btPCLldOfQ44ex-Gk8z6t8d16vIVv-zqHwpuegNCU499wJ5N8f5C1sppPMYcXvYIFYb0qKiwSRGmeX6QZdOB95oiz9uirZ8CiVPZGCcikX4rxxgEVqIMajfqoIUniETY60cAJzc8H5AQ3L9YhC-bCIzaixw39SiMYbTSMkWfCWOZ-i77m_V5KrJ3tFCE3I9s26IIOKECE8Xr4HDRj5iPEzg71gE3anDaC2W1pC0XYvr9Q3iOpHLYyuZoCFFhgzdMofJ5pUtAP-Fdbo4euCMJo4-tIfsZsKgiSzxTeadylO77-dyxHfykDZ6LWc2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-798">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wordfence.7.9.2.zip</div>
  <div class="tg-doc-extra">5.5 MB</div>
</div>
<a href="https://t.me/danialtaherifar/798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود نسخه حرفه‌ای پلاگین Wordfence Premium نسخه 7.9.2
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/danialtaherifar/798" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
