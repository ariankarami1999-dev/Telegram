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
<img src="https://cdn4.telesco.pe/file/UgD4taVn6tasnNnMPlqW0VrASWKVMSO_K89Ti9xtekBRXjLr-jxxCRd3u929sFc9Tr6g5CGI1nsU5NCVjIGR-kTH4ePf2cOuGHyMWu1YjMp3tJKVJa3dRHsMK2-HhRjwa31UVlFQefGfAnPVs4FI5wWVmnSAMx4TNQmsztHlpqjmG91a14kWfUcM7Tt8cB9IIHmw_tCVl2-D4XN_8ZCyRbzpr-5jECJfV2-Gvc9KdNIAZzWD_xjDzRdCnl7JoGtKDVtMRi3d7UfKI21av-MCL1Xo6OVjFUdi8Ki9bmaS7mVwJNkuoPvVM1tCTlAThCzqNvXuZ9Dnv6xiAzjXuEDE7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.56K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 02:56:55</div>
<hr>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 422 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3C_wJO_aO0GbVNf6BtJGMebAY97wIwXz-KDyekEIPOsk-6mQP5OVjPrjaSaItYE7wlX_YJ4WojXBlUyZCDSb29cATNdoF8buMHbKSlzuC6YpvTgziusby8XpNSnRaUUGpYmZ9E4onB4A_cp5722q1TtbdJQg-Pp0OSfZc0xkVR2onFm3CMLrTR0BaDGs3XXGTTYbypJzoFYajLZPsnjQB3gu-7kKHOEe9HEQp19JnaJt05G_Oub8xomIqBzwmacIu_kB_5p_4zZGs35OAIE1Pd273uH64Idb8qt2lcDfYAC3WoeUyoPJfLg0nHbGqjaMExMzm9g5RW5_BLKV40VrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 427 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 590 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4aZCRlEfCiXib7VknfzeopsJ0veajYgOBLMS6-cpg0PqtSt96q78XP1tuilpPiZmDI2cv_QnblZ3zCN7UKsAL2mR3uKZ3T_6qfXIvs9qaMPAxEtAOH8EOKKh7vGRrQTR6pArP8Fj1lEPATpckzPr5dmrWH3I5e0S_Our1Ix3Mzj4KzYTDhWaezoTrV1VCJvbDxk5bsDkaUZXH4bLNmRZYQTz5xQvkZ1nW6K73JyFrbGutwMan34DK8IDkmc2fPNVVyIgZjOg2lzLIgqIfdESwWQoVbs9aTmv01Al2Z7k4eUp9YGDGa0kC2f4aTWQtYoeMXR-3DjBRp-C9cZICMKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L12lOJhVanI7m_QDe6EsffmHpAecNBX3O0ka2hq_bQ5sJuk6Qyzw7BXJ6E3A9qg3ifSUJh7b577YD5vNcTAVgzz1OAGfIF7NQ5Q2-AxtUUwXsr66REERHQ-8rUxazvmQgFdSmqtzSKbPPFyWC9pmby5r2RJdkCWGlEyUTsmSXHpQiNw97TLJ390YbaVpGL1CxSGO99-gYzOebQQyMZyVQ1BV_46Ty94JQwaknMvxMEv-Z90eU_pzWsNrn_5TDUOrUlhhVDTPM0nFYVtqGjjcE6Ba-YqK-7GbgaO1JJd4A_7u_TM8NQ_LsU_sAtE-tdQX3NjCN6S0J3jc7EewqZtRKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc9CYsDrX8cMiLHL4qrvX72z0eiR5iHy2G8G08PPeXcaHtKe2z67xjDLUjNf1Y4qCU6M_6hjKRrFeXwqRuHylwkR9XTjo6DxgX7f2_igO7pNtUDuyo6faV6feJGRoq7tLSRz53EfJUpPri5moKPgiQTBc7m6HtO13WOykFmyIm2SjAn4WNvbg9kykIVgiEhuHOE8MiPbE-6z0iK6pTX9FbiRd6HlN8oDvSJncimg5iDZk15H5qQVD7caz09jxh4vztsCvf3zQvftPeXtqZ5gbJvNmaX_GxeB4EgNc56AIK2xtOpXFXkuXBaL8KYfZhgBlzdc9DRabKBv8atDz9bTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 742 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMa2WHyQDJu7mHK8C6YG3snFJ_DTyU8JCHQL_IiFFBmOyxdIOsN6aTP6M2zAZoVOGMroPyarKhXRR8USeQll4N9GHINQB8RTbl7W6UiKxF_pm4OpShkPWNG4B5M9sPBeXcoo7pIXMiOUczIZ0i0hE76-sY32k0Y1ThWCE1lfLRWPFLjI6e9oTDR0XY9D6jglfd9W3g5O2dIbnDdRag-ownwDCRY9tO4HdFAYEBa0qUeyiI_twhWWeKxAAKM3hPV52j66VDvowVhjmHcHoiq8n271kd9vQ3_BihU5-bPMpKacoWCQj6Oe_uccaJhlymuTTW6tw1P068_kxN6CsuzsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oobadYoOv2ZkDSacXm14KFXGEi7xfUMMSIomC57XVUpwfKY3usQoiVBLNSPwwEblukca3TfwnloJImc5VFIluBtPY1hflFunmNuwNTMJBpAxpqqqxZJnpPaN4txvqDkffNCi2e9OKz4HnjaA72bvfVyjKk418UEgVbD9veg3Pan9qeQfDaKBHYNwWpMy2dAUfCR7qGC9UnJ6SVQri-GGUE57h5BKIVcizDaC5krs7YzX_NFVn2KnnFnCzJPtQZbmocHtPYxzNv_MPIYEdtSAlxJ9a076lHMCAW_7ztukTaUxg5r5ss60UZVJz-AI7sVVfvzZmZV4BUQB2mYA3MEong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JchApyYMsdvQREreP7ZnDDQo7f89Alzb_o0gQnMcSoFn6VzXKmAZcbGLNzupo3fVh6nNVF5rgS2C9YiLeQULr4aolPEJP3eJdwp5WRAE0sHyVJ7eHPCGC2tTza-GRX3LIKZndrZFDTOwbx78mHTyXNcO4dkjnlK1Fv4ufB5oha_O1dWHIC1_s4BHJN_p6W63T70hLJOR7nDvlVO8jmM-r5uEffVDp4PWn4CFBhWIBnXncXOMMc8_-oxFOYdbpRip82UhKcDH5lgvJ8J_Vy7bODN7vkpiaFDGcLW2aizltvuMO2CJui-8tl_poeCisfyXdMwBzCNxZlTdkSmF6zICWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R937dAd9hW27O2jwq4o5oEVTA1Hg3ubBEkHFSvyXNVUuybAnFIB0R_tqNK4mJw7XWty19t3O1E6BpXv5JgKY6jrkGWLKFOb_9neqAcSqLiI84WxrzHIyiWioIrGZ0B9aDmrFKH6WPzu5chGGoTXa_DRkwwd7aRNUdEpz9qCpPeYqG57ffQFBqcM4a7mcHHvA8zaTQ9PGiHaG_aavbFLr8CjpV2dXBHrFT0uBIYwgFyZWw5AjUJnoqmI5imCU9zkoO_dAm5rLbL1_EB4wZkMhfyV-Tzz4XFCoPSvQjnzzws7Asv_JHS-QyMEQBtRU-5_RSqVuGeNhuaAEY_Vif-fDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfa-IU92xfl57Q-lTyPiVFBfUwdoVoeB7K65e9G0XLZKSYNpu9c-G6EQDM9K_03efanUxoatKtGqpiBzoJxLeR_dNY6c62hEUq6LPDB3SOFFt2HGtF2b1lU02CZQoPkPcSv3e-x-LEmZLWybDlisqSv1EFDz2-nLf0fTGb6PEvh7EJUCtEXbhv-N5qotjUMXO64Cpr2gACkwU74xgcF8BLUXbWukgR311ZE0dhqDt74rKe-WIOMNqKbuVWv9W8WCTyLIej67oa09aJNlrawGiSLoH-EihXhBI-IaGfsNuKprL23yXYMV3p0N7s5Ht2esONagHQb30pL2EYPAWJYLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 749 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJjqwmyvHcNu7LkbyvyXQXQr6ImMg4y7yivBnbcwzOUZaGA1Yn6fnrOKODFAp5iZsDtWBrMiIXX9DrpdPCSH9Ce1PJHXU2dY_bV0xLhbk_pSyQFTVhRJSQ-MgH-TInyhM-cOxms3rKe3Yy7ZeBrjOFtZmPXI9_qyLp9YwN5CbHT5XG0d1iaTzhwki86NLd2mngO43mfHyBvLTiA2zWyob8Psrff89i1LaJo-OD8DAbederbRpop8E5pa72YBN0vg3mLmqMfnqL_r4LMl6ctM2r8XlaWRbjxmCSMNHHQg_Tm46lZffZ9bcwoCIt4-fWoFA_lqLhwerknscBwtRUxKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCkADv99NoTNzuD-_fr0wVqewb7Pf5G0nj2Xjc7qAzM1d_Hr2PbhrMa511HF9QXIbJL_jcmxr72btsMCJDNS83KjysmSXliEIcFjXNpsHGf2JZIzrmFjYDyfYME9KXosmOesPipps_7IqntQiBYVO4_YRKMQ50KTSqmeFb4cUiR-oVCTDEmHC2neX0bjSeNGfDJiqyRonV8btj7intww2yxVkYeFgr2JQ_sZI_E4_qLd2_j4wzV6ljAgfYdzfbWghSZGjt0j2p8MqyBbM8ovmDxAR5hJ6RPr0fuqSyTEj71cTrsikqsqiG8LZNyg5cSaRU5A2xel1AhVwN3xtBMQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 867 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjEJ30ifIpbq64fcAzKGnE3more6aQf55vCJ7XqCCExrDH3EUqh7vnYrTor3aSdWOyuYYezZk0oR8k5W_2NlpSUNpWusbq87nY2m__CXftjW2fQ1NLDk-GRLFnQQWjM2O2FS-ukl_mKaJmfv9kcKDIet16jnUHHOW5TNlroVvrUprG-NITH5ol8C9Wom8BIynrGh0ynAuMRZqOy7as5wmKrOxRprsjUoudB5i7T9CxqlnvZfvSGKO0mskhXAnncR_HAW8BDJW-zKtryR3pUp5EvLJvu8Y1xQPUOllfEj4Wre66a9UF-qxnORLlo0Q4MpKWVU_L8-stGCLqln_0aU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbTA0FaHcj7BdxM7WlgQaMWxYdY3H7Dgd38gFOiW5OjKWVYtxQOI12BQWUgyLIi8SIlfQLRKlXO9d4P5T91DWS0WLYuWLY4IOCfpyDe5EAXJJes8NyQ7Nhh_YR-WcxmVW4HMoCHdQlG-n_tgPXNjxaxSZg62D_LNy9qtm9B-SlqhSPTWnxEN01IfHylMZ34ZL3eAtn6AX9HkzcE-PMVKEcbBsMCHPPm8ia9OcU1iUezZIs17IhTBdAyduglSCg6LUipN7dAk8qc3S1iylDZdkI0Tx6pmD9AyxImvsAMyuha2Np1D8KCIB8K9SyQOF_JRFFGGIQSVct0t15vJlFj7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqET1rojAZzHcEILIMJigJvFrakIZXcuVfJWgoEeDzKq61DXMYlUkF8L_AacKFZewoEg7pIfDr4sGDb3vjkUj8seM5IvSaq2Ujop-fyBb_y8eVjjEsc9wnrd0gOp2oLIMtU7RrlyKauRFEjQuuV8oYp2rnSyzeO-hgYx9IHVjg7u02RMg0mCZctjH3UW7BMOY9d_hnzrWMrOB8I8qaKfAmA30kQD5_slEXODWw-RQr2rggCjuySmjLX8F002xEKpEHNdy5R-9fbFFFjzWGSo-QhF6xzonLHQoVquOLDgakrHAifxTSEjGmd0sMuyelUWKBUejhd03SucuxRO6l3x1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVzWaUgZenlTW3SUQhRqwniZ4wjMVIMmeiwA5BjO6cnPGdSjH5PEV5pWkfjMnb63_OKsznD3byVFbozo-KjWI0fmAt4odFEf2iW4aNTwEsJIcauLj8MaK47_QS8CTEKJmizTcew_E37Ka3p0F7Lq72Ygu7YoaQU16D38e5tK2yDzMbs4gU0Q9POnL6GSAftHB-c1L5ibsLqsPMA6Jp-zNlU6ITd_EoZXZlf3wOpS46JT4sYD5fK8d8AOduVHBg0osEt6TsugedPk7c3R3zx3kvzei2smCFA_-5y6wJgF-UXHJtjxu4Qa78nveQyG8wbT2VnEEpBYQHPD6C60pStMXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKIDWWUNmzl7FK1Hfyb9HZ2dYTRFql9CVh0QASPeWlNv-rcXZwnw0OY68sh-dnZswTnO51qyQiySeQ6y9D90eEk14pX1sj4aUTWU91d_5sDmZEBRklKjie6lzEwY4nWxXzaQdIcIWdjUNik8oYU5_OCEoOfRutpGKh7thArj9xA4uTYJ40RICgXmb2m9mvoM1umZ7DE7BqkKN1jyditaiDHte-zfRTOWC9CTG259GqwIZy503W_aPeWmPeGc2u5ebcG3xeHxMGr19Lo2jkQOgeO5rVt1VQmRWMbYNaN-Rl1Wwb-nPkEg1gHXWsNItLd6LEGhKbzFCViG8yZnxjGWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 862 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=kmH-zCzkYM7q2DKL4mFBZyxCR_dYwQk5Ibt8btAK6fOLBSKxxwrlyUAntTd76uFTGMdVMYGg-_LYzGIMz9XehmoXf8Zqx6UXOOcQXKkuaJaaPIZJaC7AH-otBUm20dOKh60pnMIsQGUf2mqSKIL_edy6hCMGcfEU4OT3XmQcOk6Gyzcwu14s-Teo9ELJP7y9NCn5vcgLZpYzpMwtUxjIzrD2BBYlPX5ftxXXAipHhYqD-T2XmCKkkkSZH2HAfEUYgsILcIIa4t5N49IBOCDAtBvQwcX13BymekN5t-1kNLRU9r3IVGd6wv5Na-w1b7KRwN1zRAK666Q36J8KTQLNnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=kmH-zCzkYM7q2DKL4mFBZyxCR_dYwQk5Ibt8btAK6fOLBSKxxwrlyUAntTd76uFTGMdVMYGg-_LYzGIMz9XehmoXf8Zqx6UXOOcQXKkuaJaaPIZJaC7AH-otBUm20dOKh60pnMIsQGUf2mqSKIL_edy6hCMGcfEU4OT3XmQcOk6Gyzcwu14s-Teo9ELJP7y9NCn5vcgLZpYzpMwtUxjIzrD2BBYlPX5ftxXXAipHhYqD-T2XmCKkkkSZH2HAfEUYgsILcIIa4t5N49IBOCDAtBvQwcX13BymekN5t-1kNLRU9r3IVGd6wv5Na-w1b7KRwN1zRAK666Q36J8KTQLNnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4X_i9lBVEb82v4Xlg3HsUlEJYZmnqkL0CVxrExAAMECQjqN9nCWlQ6pySfs6sZkcNIOlXuajYGHrbwT-Te9qO-o9696jLN4Vbb0zlisuqOLdaYCxi3mspDeVDFz3KEwMT4nnVWobzevvk8yBt3b-JOOto0OxMeVPmBh0T8Y3SLgTKFSt79-fRpq0urpkeO6dcMx_k1pWBJngzfS0_wKOpgac8LXbmu_J34X3uhyndtaD3eroBGMUgdT0sRsuPif9b5bcg1kWsPr5Rsvo7cEWd6XoaWdv0IQXk9Bs-pH7EA5riDSzXo_4HWIklLiFDYIgaEJ6wfMoT8Y2azOtnDYvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 920 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_RAl-VPyexw6EcIPCpqecJ86FMCOMi-IHunmnwOBPdmV1JOuDSQFg7wfzk-hzDsmgppmPCaHBgxe17n7dVPmHz5QhwBrFcMTLkRswqPX_xtGrYl-Ju3_RjGTGWGMppJ7Rof7nQx3KvObEgk7Xn5PPDAm8zA6g3CsmJat_fHm6NVDH_mrdkNSNinFes8DuotFjHwoMTgfSrLUXnj7jHCFkwzJoWD2S3JPDeNK3muXqSJR1gZgf5F5qK2lcIcX6ld2zI10he7QETzkLNfEJCfxAPozOPtNqi7WIgkfVEc888zgjsgjHPBlbriTyXpcrdek7ppzHCHQoTsOMrSjViO2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6uvdrZ-oXvvyhDIqR_mGmtCMugsH4vBni1I7rgPEi2zY7YRDKUSNVaWS8qn8D-KWRM7T3jxEWvks-OJZ-wXwltsmW2ttcFjdBcL-DsZ0bqm2XM1XLmkj2lyPPMc4Lp740myw4JI7ZmIqz93l-i3Cad0LcWJ5H1Uln3xKPBHiSWfLzohvf_eEgaHjdKlgqg6ndZ6MxYgOW1TrvNYqSgh8DXhulvxHBAW7IVIjbaNLn92C6009NNrm1-bjdlTlicWdOxFsWYsKI43z8kUBv6OP0cqJuOKoazGid5zGZCl9KP2yEYVuSgf0zac4nWFEX7dLbA1VnejZinUR5mbVw_VUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCYZ7-tykt8i4y_CRK9vOsDom54Bd8ul_4FqGApW7M8BhhCoycDqApzbdL8fV7hk0Qw31wwnyjN5r3OFnFfQfZMpOAdJ-n4reNeNwc8tYoJFHxQGVKql0Yh2o0GZlqJWvaGNejRE0w41JibL8h9RR1GXL9t91mNiaoHry4DMyf908ewnItmMkPLO_TOAXfZ85IF3hTPozPAA0Cn79J0KReZfV1VHEwKTr-bZqJyF6VAcXzY-15ffomMYOI3UAu5V5pVlRDa-ENu3o6L8JoBRrwhN_QUBH_ZxiXMiFEFni1uGRvNAALH1fvRoL-yzgH7gwpvJuHKv_ajdLk5wwjx5vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmfejJmWMrI_hRmvZHDUpfF1bcUqSVzerXMC2rR3wX_O4Q0aYy2nbH21orH0dp6qNtKAFXCJC466kgE7NlZalAHt1KxUmiJrWe1ztu7_46NhhS5wwG41BEpay4PAhYKILiCt_zxnT_HfEEdjE-kbA3co6FbWn8LNeSJkIq2qWf1QLuXbYATXa4PCLLUKh_lURhMYWsuFiQE0GPd9dVFoqWu_B8YYJwobr3Ra9ONDXq9180DuuwHLRhI33sqfOn-OTb6kRmk8jGEsHzpQJl6fjk_HMAvlIVkF1UBhNAiPudQXA7Te-U5DBJVuBjF4zDy4D2Xf2zHYcCSXPuDhTkUdlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkcyRIGBIrg3WSgE0vbbR10dHcXk8zQUwHrgFvIug0WrhMNP5j38BI1DRKyI3MqxuXA9fa2HwVbgDB1KCoNEPuISkxvDDPCglcOGzZHz5lfX-Z9gl9rngPDmggye3D_GxQhe6-6CTc_BurHhG11wfLi6gnjKOshxMMPFJvvyBcQOnk12hF8NNS2VZ-usQmAhX4Mi9WlOn4_aXnGmiAD2f23li2WtPFGo5VwlcSGAuX8q-9CthHR8MZ7Y7ZqRL5W7itOJP7CE-rQSm32dRs06JTaj6OtSHwX-Mg5lSg-H9tzHz6Im4UXXnK_XqiLwmAw5spo-EeJOeiKiuUPf3mWylQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdkLVcxECd5QbODQkTpTkXedAqsCr76046bW8T_UfEn7kcnmfxIqfyyWrb-3nmpdAB5I63c9HJpnMctwGeiW4Rx8PQCg7d-42O6nKNgP883PXaozu9023_CQUBp4ha1Pq0lY5nVB9fmsiZPPOxhwxHUjRCQHax7RjXGa_IY0z5TDSmGoDsH2m3YulOf5MTeeZp1nSFli3DLg9WOjxlG2s4TpWS3vS3fqi9jBeB-2ZKRpsYY7t5P7TZ5mPQCyIDrjOwZGaTAxIgsb5VfTuCVAxJJ_Bu5NDqQ_00r53I-_6oGoOBjD11ZR9dtVfjQvZlb2x33rmnjGrgbCXf0yY7PRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQ5FIeIK3HsBADqmXdoBNM4mwVG8G9pksGXqht_xBBpkqC4Ay6tiOYgdf9p9OnbrgsK6nwpmmYtuo6WmNBmCREo-a6oNrx8bOiEZzWEF50dJeh54lH3VtLUK7muxu8YhSB1LyMOWj7xZFc2eLeuC5UAUNtNjiuo5R5l_8O6jLTQv4Qv6zxCJfFp8UlEmMGbj6nhukF90r4W0PVBRTOsVHbwe_bAurVRjt50LqFDt4XhwROTLW4ZsdyQuhDlh1eh6h2Qb7LPvhexbi8bM4Lsic8dgqyVLChkHuROqeZo4rc4MWLj6RkQ9PdV-VgcHNvggcN_L_dnFalWhC1TfZVKX-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR29onYrwnzPWtZVdYUvbgAZcyMOvDx8OTCNj702zVDGJTh9O467bsPYX0VhM4yuTX6r9PlKX793r0EgM2wUDP2CmrN4qJODhp0l1DVb7y4wAjVoQ8Tzn0yt6AGQaQQcakZCmdvGp6bslxX3fzjUojejKJijp4OQbSCsxM9jbSe5KNc10YY2kvH6hRxImdIl7A3scabLxgI7coC-WdtwHABbSWJjJVxCmuatQGl2jQCaUIjNGzik-vD5Sly3krUh_vd57OAqW6nOrhx9q4Zi9ik9GYkPdP2Wzo9F7gh0dkvazjnMret5h3HvD9sZAxbg6-dpmc50MdAO8X_l2WjVwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdkEdlkOyOJZ1A8ekJkpIOYZYjTGy0FfoLxO8uu4lFnBhSP7L17qT1o2P99Eoka6dc-Icp876JD_Delhe0pPMBVVO1w5cm-hz8xcWWbLjQKmOu0OwaSHu9ZNmVLIORdWNWpILgZuvp9P6hQMHRMg5756LVPF64D44cO61PfiONcXLPvHwPdTcBz6k2M9ISJ4tPvzx6cltqmc8A-cZmvG5K2Z4GWslpwjx-pqnXytxhf7Lax0yvfaKg_DHdw8HmCmDkgKw3Xn2zOgauQzN3MtR-5IqCp57X3pxyb66yspz1o14oU-Sw7xAtmLVrK3oBPtLZNooZQbQtCxY5psQn__Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-yNB9Zr8TFcimgqYWEtGNX5bW3A-iKTSpyFZb4gxnLT-ccgrpS8FxsHlmNyAAEasz7jSAy9URRFlraAxMs5iQuiPDG65h9fuynm4l9-H5HvVJAsgS4oAcuoif8nfDoYMROtKMTRMLZ8QNz9LOEHO0sYC2eHvAmWLiZwCcZuvIU6I7Ima1NjVxY-zRIzpIHLaraj6douTLPu85pLBhMLh58Pelpci5-jsnC7u2eXRK-T8CfU8KmfAcTLlpxH6tf_v_1Nku88hLRQSUDXRyfQbD6UraFVuV1NGXkTYj29d8CxX8WO0riVJKAEBlgjFPHH5zY94CdvRW_OcMuc8V1m-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W21P3nAIEjO-nBYh5X_uXTjxZuHP8KM48kov5e4u-NuEurpTK8gqoM3JSZ-Nq44wR0l0Xzyo-Z5DJzaFEI1Xug3avkQSPhUkAkq9Qv6EN4sSvghIJuYXOmQyiOpd6R8MQuRdRjkTfDHutH4IAi2fh7MOtid4B960O9HW6_vggRK4g5pBf5I1h2wQZe-zn2c3cFJKN-XSp-fhGUueoYXDO2r2K-TjopO5VOolZjO-HmRT59fZBc7zuOkSzRQdmsc3cOomdqVQXNEjuyOIuvcHlMqnRobdlQhiuXayx9AL78TzDR_xBloLu4Kk0BkLtdJJeTCqBlcWrKYAK-BSbto6gQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzj88v7XB34NmZX8gY38ez1pZYsLuGgtIjkiLh7JwWXe-MsRGgD3R7wfC4fjQfvVQCLfLx4mjzCughnL9PcbA59vFqPGkoXBWV9dGSGE2EV9gWJWpKRdmA8tifFyUtPsy557fjvsBtJCC-zRWYpk5CvsP1AxzPuORA9jPrzmUDgkcDDQilfGruXmH3hHbiQuk93mgE8-e9Zu3Uljv0o1MnB-iekObCnjOX1gJ4S-z1btYE01jcZqRoy1zo-VjiE1CLD2uDT1X2clbl-SfKIJDCaIIuYioVm3JwRDHi_9uMOSg1JKjpCJ9FAYQvkhflj9Pay6HBcJv0aJdZg5ox7NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QX_16UzmGzU58PejeXczEnIyNx_6Y-Ck_7o-nK6zZ5PIjOVW6CEVvdHCFQ7LgRLVy9jG3D4RsaWKSRH7LdPTWn0MASEgh77rCZlzFLpYCPd0uMrhBsrSTI0m8nKvgo-uWa63HfM2eXo7Jgb_8kUCpVQoONvUAemxeld122HzlpWbKjugyr37OHUpUGLprhzwXM1ZTVY2YdYe3dpGMd2k57fZhTaLonSJfDrlZLyzseOdWscaQGCuGoEFoMUmk1ZEzwlQsaD1w9mEGIEhpJrrYgUT1ACvWuCtgP7-E3MextomU6VZDSq6FuHp4NPHyQ3GpxhCLpwuGxk66qL84gkwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFE6j6joNMrIGGY2V-XfYO9vlcYprHN3uNOOP_U2IsbOAVYWa71mR_Y7KBeRk0AHBRZuxn5h6PD_fWuPVbTnWaSmAwuRSOSJG6p1W7Ye93enfRgFLj0nyCMLbLZr82vmqGoB9vAMpVI6LNLMjCG17qByD9azH-XidF2ya1SJsaVCqap_fZO-c2seSRbZPJMKmpFJhJIPuUbNrSHMgtp-GDGM76L-2nH1F32QupjzBVh48DclLxOXNlNLymvF4T-rSt2b8LMEnn2smrM8WczqC8Th_K0UgTQR9QHgyRTeAgkZhLYjlJuNLla3n4aB2PcvO_asokTglSwV9oMONIa9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmNNvgjXQuUOCeKsx0MAdiaqYxm4uFpzcGDOiZpeBb_IgPl-Y-1FpMihoQg4lss7RbV6N_F0Lttlc65JkDtD8B1FST05nJQhk7qQh443Ucejc38HFlDdCQcAkXI1Gi5040rtu4wrPSnaTO0GXyj_Ho1i4tTmbsGczlUgusUM8xptnUiwlctcaqA5YUWloal-BJr0PV5YzSbXSgytzmbthdXdcfHFd1XDBxLzmV15m1FV9weh5GBxvOEPQ8wpDcUXh5ppziOgpIHcoW4RlQg8kiuQNrrnOV4qqUveSBhKtyaP_gDShi4S6nLAQZwAWf4BYqmIS6ybpUPZWsR_8OdSnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5dHRjOWjxQVkx_dz_VTX6TPo8puOuvXj4X9eDOx93msS0PTT_KuzkHNOYeV_Pbrrta5Ksfd97Y1_J8U3cPqdmsk6HwkSP5BdAQ-f1ytu5H1jlJxsuTN2K5xbiZUqNUBLx4Q5_ix-kSvz2oXcPY_dfCMkCZXk7sO1W8bA829AAitLdAzHdAbmxHg_LHJX4zCy_PMp_GXioN8f5fe0K0HOqXuj6DNpbLBTMqJXWr9jlVd0gnocSxdcGM9brgSXwvT-l_K8MbC8sz-5jF6adw7rWZnrzAxifdd-V5p9MDgIgOdKd1WWb3P6Lc9FikGtrGNZRMiBJWYrjL2RFYPQCxD_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkMtIwMyyO3yCIS4F1ysJpy7m_jaPN6xWVxzLThq4LoxVCOh16CyIQ9hWTPgJow9AsPaB0cGnLYx6veEQu8BXdCtSc-pOsP_13ErPehKTj4xGBwlvVPG7cNKUbbT54enbRQyy21rSkKTIsePJVpbLl0_WaYob-Z_mKqi1qDUCJcnGO-4sor24ppqM6ZsZ6N5fsOz7Ie-_iIRfIiwTKrtofJaiiMeB9b6C-ftFBI4EruojN2RyiTnMpoWNDEiozcIMWZqQUuQIzBSdBRvNdrTfpVUu3gaPLyF6c2Swe9v4v_eIUam-fIUGm8hea-2EqVSoSEwKWOXisn1wLpXG9qDlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIuFxCBiw0oFtYphSLg66Lp3uy8WT20fTxP5h5_d3XqyRfCWXNOSxtglca-8Qe1aD0wYhnz2hJQHz2R4Hx8OrDQlXfGOE7OIY-ffxNpbY1F0HBlw7nw3vkzpNihQo65S_F4WJfZXd9ngm4upOiGNLjYLrgsS-NicvUVs7-Dm-PTiJibKAFvqzHrtJCmRIzDgvy_P50ezZNHJ7bLTVjHwelXNg_C01rbjJ5NwZ7Vh2KqXnerYwJjFh2rgVFlNXvy0gDYlvPzy_yyykZ51ZkwpBE-WVWhjBJK95Rm9DdoQS8kzpTHW3WBMVe9L4DbUKuJ2Wpj8-C8aenw_lk4uRWkSNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnx9WvlMgJCboHlRm7bCZGuC0I5r9jGdgRjf8JzPleuaeU0c87mWquCzLlMRX9rByU4E6WOiZDmCj14g1EF4V3PBbdJdxW9fuxfFe1hN5rPZ0DYbTMGcvOSX8A_PkzVn1qG0w3tTj9Ib5gb97mo_DpLrlYBYD_MfuoGyqR4t-6q5IixbcfoM9RTDkVJdU_bz2Co7fQNfjqVN2txNR6WSBYTyAgS3eOE4PXKDGPa5sVVBOGos4c2O0fF1vFyZz2-i1ISBiSV9LUULqL81eKAMGVLulGDbAIns-Tb-mdeWmWcOV5LK2279N9qQsCUxwr6Sds-q25wFRSrsRrOgQXgmPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfFNYt_FIu4ENig0w5EbvMvl1fY-RWvv2odGhgV-nKsHniJOk9CiQHiwCNw779V7_y88gxqSrcqAxgN_XpvGgs_xqANjT8C1NIZyCLHfUA9UN29c2cakWDzy-clSQeOlbluq67s0VsKATgD4RR_6524NbfyETtfZIJgZNoaNd4YsVwRrnwbrYPOu_CoMNsfzWnGjwTlL4tydPD1oCY4AFaDAXHjonRofJ1idy02diCjQ3oD8KlmgnFwTLO33MQePQ-WgOVapbtViuA6xAghfnZywaK9b6vpKmVSw5gVlw8ctLlzyyGi6mxDuOT7ppeSLdmpQS6FzTcjN4fIulTqptQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRs-L7N9E5TYDeb_2O97fxQjVlN85bWCXWN0nfoUuX2ORFEIRr0DQ9mM5ToJFAOyAlNfnWufi-y4DcujNDByvtgmm8A6q22nxJFgMiiNFszaOl3FfAec4vOu7iU6E0fCM83yqpmi4Vl9K1wHXNZpK3xi3RdveKd6epsXKs9EZwDFtEUMirBXKiMTeJNuZCAPd48nsYKaaVd4D-kppOSE4xElmB04JEeewPMryjXtfNQd6t9-l9PJpXncNoV6u1ZbU400I7RxV8jyd4vymW7tEKrNoIjnm14Thr03FluCglwgfjLVVVDml5lizWY3W_8g0DR_OSRWR5sC7AB7TkfZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXTiXLIhgKxVI5amsy7iG1Od00mntoEPBSpoTP2fCrux4FyU9J_L7DytB0eGGzh54E_t31s-_Knw-tTkt39QhNnvZCl7ogl_9WF4RSllnCFp97aqOtBHNwUZFUwS3ICwqOdx7ZvvAwjDe5sM6IBoOkyvYg2SkJJhyTL7CGxg1HrI5v5o_sn6Kx7CbvasR2xyUzNeXss1Wh7OoSqvgz-Z0s4Dict1SpowKtNRWU-aq2cHXuMeKRwtjZMkKupTd5tP53oX5iCPGRvFTSooFxBMSU9YSeReG61WA-J55K0F2f-yBgRifMqkB6mrjy-eRQVNZYrYDe8XXWs9zCrhXjQPrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PncYSmkHdmXSP-1RrTbWi2jg4LEIM6buLXk423ssv28i7wilKl_TVE5kDRLM8QjAPMm6n25OYFyqbGloXORoZYW8Iogl9YVccsMLT8bOzc-ouhJtxAJBiAhorjtMIIbO5VDKq-VRMEHokmabCIZZWKI3fT_zfCSDw_X8nsWsBhwX97f7h3zusYac5fZUdpReAH4jsBfYzhOaxQaEyX8iPqFhihjQWC6qDKhud8GR2Jk8tDUBednBBgtP_kkqm2eKp_kWu8ifJzcSCqfiaoxnah1pQ9D2YgVCaDM6bv4ExYpqYh-U9hQN5G7APpzNUfB1z8FWKwWWysS6ppP2CTGiow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8ryIUhPOZCczcKrw1_U5yVDWrwfZfMJpTcZNop6RT1krELyf9QIZ27osC57QYuf3fIX6rgWuSGo3CFtfhcGv_UG9btrOXW4JZt26B6v3r9GJzj5UsdODNZQWu5UQXb893XqcxkRbDpr0NlFXkWLmZnyMvuijV07mseDF3iV0Lp0XQgh5qSrWWVrqWeitHR7NaP9biiyJt_ilTqgk-addatAVhBLXfroSn69Cwy2-qoU4iDbTrfGLH2ZD1DE-tnkGnWwa-8UaouJG44WaSBCM4jNAchI_dKp-zfQ09C5RB2zgZSQMtdjc_IlqWp5Er4II7kHNPTec-lCv6zZ8-G2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubSRQmP5WKn3QcYyoe4DTqcOgFNPC-2yW08VKA1jb6k1YrmJhBnLKQ7K-ENTX11T7meKviKyFxf4S4HRpm1vwwZg4Ks-PQBQofhhy8wIlz4MenC-KzRpRHLYEI_aRXeHW1Fs4cRADAeanceP45hOledF92PEKrSt18VScO4SbPiQGnreBn-mWH5UcnwVrI8gpUy3JTCfrNJy16sAMg27so5N1hY5VH4eHwKr6ubuQk90ygeZqhZM-CvQ_qmP7s2U8DPmaDUINRk2Mn24nC0EX8jdSBcdUe9GdBfzj85F73K1pwhRYJeK9eTx2YJjA82fF3Wx6Cv7kUHPbDIOhBYEkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmb6ZCWYrGtLnzxZh24D1bE-UaWTXzWe-RgN5X4NN74Ty0xhSRQkV9yqQTBBmxNvOw3Uet1dmClpM32cscgczPbICqHqCPtwM-p-WKapX5iRF8bgQuC5Z1MLf4Aj4MKeh6WaEdnBeTT3qYZSo76bk08h-uyzQElzaYIc79RmRI8DN-sGvIwKnb26RFEcHiG8ohD9BC-HWmnmK6WTQ49sxB-ZRPyXQT4nLGywGxROHhjGu5wZ32YXiol3YQBrqRaX6d2YJTrF5ma7m2XQ5OwEoB-NIMexww_UhRq7pS7laStg1kJIVCS6sW70do2U9MCAzUDp_X2Mw3ncgNiCfQ6f0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tse0LtVO0KDgWhD9PLlWFNGQjKjWVZ3yeVx7H63XDHM-TKZoI2lv1u1EAMd95yTBXyqLkxZ72VOdsr2xvMAgtBjavtSuhXyouXqC9md1e7H5iUB5JGiSxovjuM3TdWRqHRjFbhK9YWjY1mOpbBbHitzqsEEu-HggLozz4MNBraLSXet7RGkjPYnXDnUpWUcob1JsD1j1W1ZyZC4m_dnPQm284YVlL1TXEzbnYMNxQL_dSdapnyHRJWbe2988tBjtfjZWnBeVoAP-FrKWf-Q15FHtQuWQT-fk5ckCVR1mDwJA7KSBofNJBK0GBW6ekq2YrdVsLnzn_HAOjObmVP_fXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0Dy-5uacyMyLwF2Sf5LHePn5XgDwHGgSHXrMWC9j5MP7PoXVIm3WZI9jzSysy62rpuFurk2siUUMCZXCLxLc4nTr_1lyl_DVEktPdBMU09fh-E3GvitdC-PLDBVJ7f6eioEt5KjA0t9MVqK3G8Op6oK7RhJ0bu9F9egUR7IM-qJgTiIziqqmNKBrkkFMfP_OSgWUAQmcS1T5hEKy_7OWcalcN-o1o5NavWqrhuvSNFmX2A7HyEdLI7UFJA99uwuuUMRRrUjAKzk_Ag7fN_zXnBJ6qnW3i79ysIxHxYUMUMGN9y7Yat-hNCo8u-DiDxCwC54bkVZGaXV_uw3OkWhfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuUbNshNZnCEZlfDMDniWrSIHFezPKZS8hM1hshO8JhqSqrJiwK8f3rHg3KevbtBQgTqz6bGl4-IgFYswm6MAcgBaQxLCHhnhjQNhSQ4yKLD1nVoW8uF4ppJfHaVYDyBm3MTNnsflTrzSYBssUs9ma9fHGlJlmz8pmOtjXuWIfiIFnyl2nD2e6t4ZshRJcpGFwYmPrtClyCz5W3H5nWxdluRxQ6slz29Un-tZVpgd0jkhDtk0bESg9195h0IGA2B0WCTFY_pRlMokZYiomE0uzdvPqS0RiV0bYZxgN5LaCXJq-06XA4P2htWR6OiII84KNLsbSGbf6BTF11Nv2fw_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSqBhcsS3DnConKLTRNaDvC-zm2HZHpeeJgMG8aZccSku39ecI5yMjCyXnxL_3BDBs0BWi0Prn7qdHcwU8xUeHy1WtgIgIk8W2FQB6M8tcWfAcVFcSCY5RnaI8Jd0tjtacKFPX3D96I-dGgfl21jG4k7Yd5ll58BarVuOmCvrXQ8wdKKcrW_lcToqSrwh5hjRf3wD-pCL9Lf585g0Sg4wSC-rs0DJTNYKCtFTijioXUmOH5v9HfDvfXe_QFQHx7qgGAiQzEnunPFyrNSl1rYFHN5zD3rgJimB9QY1mHrYRsluSxmCup-DcDCYJqH46D3OxPp0yQwOoVMBvGxsSkd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otrxv3hhd2jDjvGPLOIsNZdydzN9J7M7Z4FUPGPhv1uZG5mFqU320GsJ3qNASmDI0Q5_6v2cCXgn3Q54PgaLBw0me6iUA946zSyl66qneamFoQuylqQT_tADQmS12nlS6xzVUcefbo73b8_2gD2f6vzTegFc5evfHdB_mX7Of1_gShMeYYLsXQuaEIe7132ABlo2VpV4zDeTJhx2x9woMczY0rsqh-WGJd0_jRQo73qGBDYgdHlVXPKuq3qdXpc1rEws4cRlbckeH_9oky2B7uPZeE9MD1nTl84beTu1tDfmzDkQ04MoGh8awfBFBuRA1B0rLHBx14zIXZYkS1xbLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDsognQXtwjajUkT3NqH7gX5bq2muboMkHYX4gq-QVAo26BK_MLKnPrzy2f_3VzZVfhqR3rme_fcDHiRBjSIJaTyKq5mTRRKzEFC4VrM0GKXwTKnaIEbqghf790fSalyJXJBK72NHdTyr1DI7eey7xqvQTwI82bei87_n1G61GF0aYY7VbcEaBTPQuvQhQrbq1YX8T7GDS7stuWRO2-NcD8vqkZlChO9x184oIttp64CL50FKW5I3_4lfFPJK7NrWMpWm98UZeXJHYvE5tpTSh3xyzuK-1ZdqL7gxMctLOJpvrQiKMOIv-3pYn0zlrJ278uaYE457yeIpr1_6omkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aH918piCkeI_rz3fTjR5etAHXWBy4uvOUW1zA60s5cFnMkhlAfSmY3_s81tTBcvprrr6dKhpnDKZKLdQ1HKZYyFlVTIrv9TK3_dXf5-PV80DrigkMDVDO2E-BoxKlbwRo5TrlDK_378_VIQUAFSaRjRfkpzp4vKN73pK0Vn-VSmDeja2cAcBQzOF_pBaWJ_fF2CqkJJpkO4zStZP5mWCO3K2RN_3iYMi_XvZbSG9HIku_VY-_Q8f9hJdObJYELqzIUQE6gGE-Pf3bHSgjSiNaZpfDXeb1bRMFMKhZZOYbjEkxVfBIcAvmJOdhagKTRr1ZbgAROYe6NwcKJwEHRpoqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbx3HpqlokoveZkH7FSk9yxqLfXnMcXtxazgzxEV9YHqILo1NW89xkRCQe1tr8yilZl-ptbKV-6n6dAHg4wYUe2pvHkxCg9BnLscxfQLHinJ2jJTAOQUmAzhbZvzlqIBozXpiXwRbkg0rzqzOcjowGfeIjT-JM_-9H1-BMFUovHHSdVw8TqYReHpg9vhxBX6GTRz80zoQGZoyxmVkLijOVqWG5eBmF8ax55SO7RpvILa_UUKOU6ueJVbxUMOeFgD50sxtFbxd4nguZ2Jey8Dcx9pcqsEjVQvT7VplSjxXfLaOSQn9IAr8NqPLgcP5ooJSBymNDfQqwwTdonYdg6WQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nR4BkBrh5J1klpEdCHZ7CyheIKh-jVLWiOhFGG6ay6NOnE9ZRebFJS6eLy5cJZrddx-xEeZ3eAo6TddQ2fs2cHero78t9Xz0-xv3Y3TFJwiglBi6IZ6ka01B0rRiXJqNM0uo2z1T6cdAGazq5Z8dmYCQnbaW2NQyUR1MwR1UBLjJlb5MzAoGJAZLiknNkDpk7MNYgavfb4izdh9DME8rL-Y78cjB6lCv-oIFwJiHscBtT1sg5qY9C0H2F-YGJG4iadCvRNO47wCkrkgPoJBmJcM3GWfkwur_zHdF9CaKtP1LfUEMpWhFiqDZ5Zd7pKKLywyuIq5Yjt6bTa_NUmH3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mkDXDb1HW0ujLN3yu1lcuFs4n9ANSPY1cjhOk7qk6nK2dAmf_G17_sGJwMrh7YGh9hj7NjuUsp1qXP1WZ3eb3EXPTAlrc-FVeBdwfPr0YZtNCs450L4pxtUxy3lYFKboZvHZTS2dqRENfDIupjq8lgJH8H0o3_XANMYqvR1EZoUAzjMaKBxP6xzdvTY8nQ8WbJat7h2ZNwmIYqYPHnIUcXK5y6dhOBmP3DeGX4gZVtYCd5ajB0fXlPDGSgp3iZavZRGDfT0AWywRawEwpAQPcuiDmznEJI1BUYX9S4PwM9wBwZD4niJwbbZ-xH-rF8189qdbAjJgUwcRjt-4zEz8Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRRx0CU2zC03I1qB_QVBnxTCNtzHp2VOs8hpOlyVwLRYY2obgO64SlR3qNbXygE4ugqQ9PMBV1bFS-VOEayhosKPItsZfsDBBfypK_HaVJHX9H1CYFDPH8Ts2lRcKxbIJdOl_5b7eBwDMF6XCa11wCWlW4yHznWzah4eG54D09PS0SfLlGTJbno7QMl6B5A0EwnKpOmqMvabnAKhc4ph77OxU840VoaoksoJLal6zbIlPn6YXkxLM-JmyYnQuDWxxpweshrwAbMkhqwvId7JSR8GM2cniXKGMJoP_mTW2tgNZIJ5yD-P7LWiJeCjZ6ZrMYpYr3gKEZhu0fNivXpUcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S29FFo0Kd2k2U6vXuktV-q5N5ILx2F33v_KNXhf1qF4L8_HsRnC0XQViHTRc_glk_m8YbZMjqDR3e_qF45XmaUkAzRZ4lQHKxq2zRSwcEd6N9Ikg8MgiRVI5OS0rJe-h_95C2JdwphoZW1PpjOyXqJv9a7d_Jhk0uCazHAiaXEEvo2_JEkltICTMz6PdX_lBJGGeLbQmT-Sx-QLQcmOosAOL1y_ViD0X-LGj-WvbhZmbzrbzIJeyjoi_GWdNloyQODqIdBX2XHBlDH_DwudpIIAhBPm2Gf8BXjjlWmPjCCj-QOxTBzqXM-kFRUUeguzLy_ZLYQWNjDpybc_8iggOzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXMS6FxGkPkf0zseApGF6e6xdwp7CUQS0RyQNh7C2_70mFaWtqDpSgZ63NjvuMvXmDZRDDFtgKUVJ-N59KkWq1m4RXLztKyPGXBgGVajzhgUpj3OVCAhGuU8oVjHsrolbJ3Ic1hrN54-mpvs_wuiLwo7TOnvt4dWqIcI8KnPWpXjxKvbk8UtxvPA06bhBNQ0QqzBcVeaStJ1PKBP7tuwhIGJUXHPFLj9ZfolHfF4aNvQJEsBFMQ8vjNH6OUqiBR9YbvLalVte5XyHxgSP0PxIgWtZ50SFMHfIKSZFltLx1ro7mvRy3no5ym-gcgghrijkB1sx6ZcytftH1X8d5BbeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gm_82WA7GPURIBsM6jyXE_VxNaWQKaJdgUvuTCOxMIBCH_S9aCc6L07Wfugu2NK7hW-VLJzoCV4F18mt6GXTFoAF_7YN4t4VYxY1qLPeKd6C5AavHqI5fNx3sOhtiH6Z91pKDOhJry7XZXcfDbToE-BtPHZ-9DF966VpdcO3ADu00xSmw0WXdrS7yDzm-RjNG46-HFnTxjnvDzrzMlqUa7gaoWzw5wv2o5KGmuQiCYdY_KudLFkSbCxGeJFCKNu0N7KqrJHDOQOElvFkFS-yuS3dCWpV8odJolGb8Kw1_WdQkDG3K8jY4sExBr5F9pjrCFcb1mqdOmW4i9TCv9aCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ou2KrNXhgQVV8bzx-2Ku7VF_z-YVqTVXJuF5FTehfmZoMsUkHDZcMwkfd-op6Sp44iMfgtHDD8ai-IIqnYWLwUmsmY6XjWkdWAo-5-VHTFcQJhJiBvtA_pudbGGQWKMpcGpt8s7Y1gy7FUpONMX2_aKkbr2aLFhiptfzvy_O5o6zklLnuFU13duedjuO7Rb-0CJ_Km1vDGqkqn7X8mvaLBX7z6PndbISUlEN8K43kIZIkO8Prv3Ra7fuodaYc9sFRILu9mTHfraxTTPgYguFfpotp73dZngnlaKwf1Jwte785szuUtnO8gZfftSdgd2Aeu_u6mxNruACPhkbroxtYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxdMxyTclm5Yf58NYVPL_mrzIccYYyUx4E4xXKZLlXJnm_YUyGgfk6J6dV_FWfs73ApTOOUNIFxjFESwHntXegtuitIK7wIihOMOCA69bnYGvjQs46R8M1WHMYLpOsfK9p93uL-bj_DOfXBlgFO7Hbv4xfmF_xZmlm_F_uimBDtB2-I6AKONhFo6-q3QGhFyXnxDFDTy5139N2C_k-4J5uf9C0ceLLbXInp6I2m05JTAAzwsf-fycF37au80kw-IbsWmHs7wlB0yI_xgm--cXATTrGAw3iMExjIPqmKrP-tcyXcsqekd7YFs-xLlrfTSZOWGFHfGzov2TgHIismoIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3TSh5oobNoK-01jlZAwm_ZldCTl2ukY7P7C_t1BIS78Pa2Hjx_3j_7tj_RVGXhA0L8JNJ1OxQQHTyEjb_20QESPfZq6A_Jbrr9LnMKemXqkUsoMs1F7YvIY1WV35kqjAmkHmGWZTzNG7uLpg5j-MfdagYF8FbeV7kbozwg-Az8TSylXzALYZiu-6SJSNeFsjXTfHzzbz7gTJNJvLaClsDF0e8e3fj8zpe_VYzP5iS_x0JVKfR0aUS7XumLVoQsyUx2ZkRLTVSg6Ze8FNmskxkdH2wscGj1ff3Huzjf3OQNFcDZpVQqR3_68SaFBbe7f-MReFT8qGopERLCduBjHKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUHaLVYNXriXHafuFPL48-8CwjO9oxdDj1zVAea3DduCPDbeaUfeFcdVOdLLbl_h_5Y77i_3wewpZIGvkfEaOLZw0cQnUpp4Q9UapgPByYVwaicdoMpU2iOEiDGBN889KKvrE_6aYwWjssuwxcHlFBigUppG6a-wWBOKIZn6s0hEv4bCZEs0DMPgF6GsfYGkMcMlpJxv3BdhC9p85xyZHzdopCegny3US9iAAoBwhEwc9c3LbyeVS-pLeL9AkKAKGZxRaaGrfMCSe3PyUm51jr1AD5JG5qfjm1xugj5w1dWls4yY3HlgLh0jeBrFsnbBvoRdx3TRK61MChfblywFMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFsEb6GjVm44woZT0y6w89sA7hiXo5Rpt2BGULS_9B-PBfTsverBQDKVP-OYoT1V1-uF99yZWN-TLWQ5I8XdmFs-Y3WW1GtxaGI4bZ_EWUtbxuCktR6pzOBrUGnXNBf04SkjGQjJLr0WDRrbz14s2L8vOmlRxy6V2c_wFR_AQcBMxIN7nv_JfpyxehNMMHYQtxbTr8K-vaULf5gPpg9J27YOq0LCtsxsmRXnKfP95HjpvrW_kJa4X42U7lNLFSVcaB2K-FmlVWaS2vQb5M73DEdpt5E1XSd7-G8NycPrfkeBZrGat9A5hBksI1_8U-7XtOHrEQhiuRBkBW5FpVGYsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=d5HYNu9BQIRh9WYNp7SN-AisCqapmD_vtY4GKnsreBGf-9z_CSpqPbUbSLDbRSabDHHtzsHWHHZAJA6Nz4bsHX7AaY0RVG-cLCOwczRNSYwmK3QijbzFj4WKpqL_SWXmvgM7Y2aJbjEOUYa7wFqubypoWatVZ-i-R-iOLEjIvhyRQNC8Wgumw1QBPQoDNP1k4itaizsSZMmymHw3haLwq7cVqX8RVS1jXRqxulLNNrVkoyJR1AL6friT8avWTgLkC-14w2XqK68gvyXvzAC4qmyr6ozZIYSfa0hRM82l3-W5HRgSHXZXQBGUmm7GtltfOQorlAcY6dxHbYpnK17IPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=d5HYNu9BQIRh9WYNp7SN-AisCqapmD_vtY4GKnsreBGf-9z_CSpqPbUbSLDbRSabDHHtzsHWHHZAJA6Nz4bsHX7AaY0RVG-cLCOwczRNSYwmK3QijbzFj4WKpqL_SWXmvgM7Y2aJbjEOUYa7wFqubypoWatVZ-i-R-iOLEjIvhyRQNC8Wgumw1QBPQoDNP1k4itaizsSZMmymHw3haLwq7cVqX8RVS1jXRqxulLNNrVkoyJR1AL6friT8avWTgLkC-14w2XqK68gvyXvzAC4qmyr6ozZIYSfa0hRM82l3-W5HRgSHXZXQBGUmm7GtltfOQorlAcY6dxHbYpnK17IPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UV_Zu5wnOqwoN3jemk5nLplReYWevBQ872TlCiVn8rDfrdXQH-YyLmsTML-GK2AQ9ilf1Qe6c7NGgsRhs0LGm9rtaKzdclc1c6d-b8jobHdMbezbRw0JCkzTtREVbuJejDcyUTwNUm3ZzfnxSyfesoqZ_ls2wZtnCj8rTMtCiR8DMlN4_BmrTpgjkZCmIygBC-Du7JgnsTf0wpJt-6QUymK-SmUAmWvL6fBorUCHis9bYbLd-1souZxXg2bfHkBj3i6cqWyuktLVFquFRcr12MktMjSGtIip8glk7lIiHa2fmP7x6UAe1yMNZ2Zn6E86CmGCHjKzsGG92qWfr9sxBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe5xOOcgdXbaIsG36XbowObvm1bBIrCKG0zm0RzmjcxB6pbmyliMse4-DWDMs9mgLnf8qQL8ZeEDzqMSxhOKG-nN-bl517XLb9GcvDScDN22Snhnty25irBTzJqEUm4Jjn6SsGDSePjNDKDePqza1GPrGQgwB-PazjlfR4AqzND5HfBVwi9vz1llgqBV58xsEV2x4cV-QRfrJA1dnpRBhHNFEZJWAY092hXx1S_-vHx83OpMNnWwaVCu-LCVHlcwTPTrpK2bORMEnjkH3-pYlVHHfQCzynU06GGTG-EpF8AU0G-2XQFwE3-uz7KHvBWGq9AXmyOe3jQ3_USM-2x4Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixqwpuzelWjuHCl96MhNcy6hpMichyv2eCTayW6lYr1dm3pdtEOELggw33yfTSDjMPzR_fzNd5gCnp-mgKu9rue2fyL7KUbHWAs-8AL6B7IlsXTlHXc1JHfSTpR0XNegvZJDIL2AbUQ_vOxLUlUahEPKlPxyaRSKxExKyhlnBNhy7_RGsJFTpDuCzfnkYoVtWhgj8-3-t1yNSVTm3TV8OqKnOe77oJObRjPF8pG0HTTU3zjfzQtymMEc5Zz9mh-kQJ6TFzwFjWeTa8dCYOsw3NnbfZKTBwZNLGjcDTi1qSWt5ejQenPPiOiunA3i_BpV7TC1m83VgxjxTBMhgNcmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlDg4m-M17gRasn3uRCOzqR2we61W_t3H4AGRS9kHDR_MWqI9EjUF5NhrD_VICsSy11KN0rb9zllVEky-O118uEwcIQ7QOCpo8tATWNsvqVW2EgXbnANdxb_pCEoIZ28R6JqcMphxIcIOtn7o0pasDzEvPR_FtoX2tj-hS1wg4QkwzMYp_7-XM-DVUks_GRmrP-ax3hZkziBpJKlxgu0N9-M_Oikbha7ZqFJhLCHHLSPOOxGwjIH1PbnwHXUNbgmT9tAXARtX9w-lVezpHKa8ut0KDi9cUkpCtaXweTfx9StdI-IHoRnfHe_C8jwZfFuREz9RRifvokrl3bWezPjMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6uOsIJyXDEJL4yIZLvbs6pZWqrhH-XGVLUQBPy16h20zr8RsPYCM2TQNX0ahflVjaXKdq37WDi74EvRsXjaQKicDgUz3YO1C3OZLJerzRDvr2DNv8rMnxIetIDF9sH8PDptY0GEjUcbzZ1d4ebswvWrkgP8zAce8Vfrf5SOcllL8ukEF3ecI0KBAq4udzWQvI_RHcqz1tzA4nMRZZUaetvxFQpXrYroSKK3EdqwBSPbXMQlZdDvJejD1JUB-YBjukxcT4n-mBgKtkJbzh123wHkQ64wtwNeCT0IS84s7W7nq4T1plJXKr2row2XiOi8fWjo2DHBP-mCxSDCJNzk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQaCV1lGlFQSQT4HdLmhM95TETZacx-a9Ix8evewEGwsgPZj8O8_-KDDFkqDuZBaBmTQXjltmHPE8l2tTL9oEguuuuXrjpBXIc49RjWmF0rWtP2B-_Sq1StrEztcSX4u79u62wxHlS9Bjtbr9g57YpnqTWR9IpP4XOieRiTpciheuZXJlO7ZBhqyCUrOIfktRPzwJFZHsDef06dk-3bSFdl7JlUiREw2D9OT6jAZAkmQGWNG1FmF3msyZvyLhz3ml0JcZspy52jANbX6m7lvlVr9-LvDgDRAyo1ayWMCto_EEGKZ8Zncwi6SFC8ezVul1JfnH8nIs0KrtoGB2oVyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpV9p7bFqd6FDJxk08npv0LBHlhwML9HB2Y_3OoKJIhlvGjACmTQT2zTXvyyWFn4ylL_zfAiJs8CwZAvz4phlVx5TZJ1EDRQpogEGGSdJpogg5G0q4REXHcmaC20fr4DbMoKWGo9WPD_vGDUpV0sKuXklQUVZTW_-NlQWHuQZ0T5Pta-TeMAS_0N2OIwrzDa1GYCMKmhkVdQQX3NHWzFjdtVGCAdw6jT9XXSv8oxGiOqGvBQH7SKcWVFSJhokAMhMNu3iGZLo-djY0qd2g5gkOj6UGVnjNdOso8Ci5dwXA6jW8wa5AH5_iM4A8synRj66PB5pmD1Iti4Y4vuCIOQog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=CMmjlsFucg6xm28-5LmZ7hZEkPytt4KPugVl2U_9zDfTQlt4l0FKBPVwqrVthkY49KZiougX_2syMeQxZcO1PJ3X94C0-ofQBOpS_-rEC85RAqye0s6DObaYsiSQ59clltKyRXhia1V1X1WCxI2tu_qhcYM2izICsmll8_96TYsnd7y-5OMbKx4avRlIyU5Rh46Fz5SZ5cMUIB517CI1s_BHonwKGGx5BJwqBVSt5YvLK1WRT5IXQ4wkGWd4Jsq1fBc8dFWMDM60GzCkbiahwSXGlmnOqK8tsyLApbQ2euOeY5iqwkBL0rNUuDW4oyrvVj0IsfLlc4Ix2ePghorvp5d1mDqFpFgD4sc4C-iLsOV40XuuhUvF0AYw48QmWSm75cfGsRNuzYEpIiw1PmLYD9PFpix1zxJzrQd8-KPVRG2yCv5nUtG981CmcW21UgL5Y3cONv4eGdMPrE5sK-c-qJqyGaKUY5zYkuwa2eSbBdNXZ4WRUwoDMIK4bIUt67CSsaRwExuGmBYrIjC9ZW_eEsEQ9HAy6mKBKA5F1I_WyEb4ztJLYGNufvc_ksud7aYYmWKOI_Xgfw8aHpQtE_TerL3YE5qTX7FJTZXCCemB4OqWoCGlT7kzF8tvKYqo4TblnCFUkzBhtXSh3Dg8GMW-v6wRZohFKIFF5uUUwC_me8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=CMmjlsFucg6xm28-5LmZ7hZEkPytt4KPugVl2U_9zDfTQlt4l0FKBPVwqrVthkY49KZiougX_2syMeQxZcO1PJ3X94C0-ofQBOpS_-rEC85RAqye0s6DObaYsiSQ59clltKyRXhia1V1X1WCxI2tu_qhcYM2izICsmll8_96TYsnd7y-5OMbKx4avRlIyU5Rh46Fz5SZ5cMUIB517CI1s_BHonwKGGx5BJwqBVSt5YvLK1WRT5IXQ4wkGWd4Jsq1fBc8dFWMDM60GzCkbiahwSXGlmnOqK8tsyLApbQ2euOeY5iqwkBL0rNUuDW4oyrvVj0IsfLlc4Ix2ePghorvp5d1mDqFpFgD4sc4C-iLsOV40XuuhUvF0AYw48QmWSm75cfGsRNuzYEpIiw1PmLYD9PFpix1zxJzrQd8-KPVRG2yCv5nUtG981CmcW21UgL5Y3cONv4eGdMPrE5sK-c-qJqyGaKUY5zYkuwa2eSbBdNXZ4WRUwoDMIK4bIUt67CSsaRwExuGmBYrIjC9ZW_eEsEQ9HAy6mKBKA5F1I_WyEb4ztJLYGNufvc_ksud7aYYmWKOI_Xgfw8aHpQtE_TerL3YE5qTX7FJTZXCCemB4OqWoCGlT7kzF8tvKYqo4TblnCFUkzBhtXSh3Dg8GMW-v6wRZohFKIFF5uUUwC_me8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpyWbX5xhMACm84Y7ojDpV7fV8n-0QIaCYHSzEQ7FUPTaiDFbxDJ6W0wJE-zu_aJLyorMvi7VI77dmIE3swr1ELTzAiR2TiQR37exZ2ThZ3bNd0KLoGUxud3OxgTerhRU0swRtYrs6DMPV_30DlVynU5eA5y6W-DR4H0RfVZrc46ppCIpnkDEGcVa7N69pZwOGHCxdaLLgzIVBDdLcALqJTnjDAd7ojkKQoNyiQcAuRrjCoNGRHGtACY3pwIM0gtnOmgTVPU_lWQU8SJ4aYcBI-HeHxWopIwfF08jsob5aI-6aSfbDvYWoGLQXgvod-byz2V-CI9qDifGUQWYkF45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vpVUYimgYWZ0Da0NubUFEAac1EW4LfH9s8aRZUA5hiuCw6RBXcrYXN2FgTpnbj42OT8k_JrKxO9LVGXTs6RLifcZp_mUDUnC_xi9v7Xbr3sFhnocyLuTQ5tYqsESQ3-eiWcEKwUVUXL_FRuuOzm_74GWPhq6vaxIzwJsdT2mxDmAnyjqnXnTlkynGIGI8DSVoc6BMnb6QBluN4n6RksKSjm2uGhiTxhnmVZXTEfmYs_qlAFPdWY5y35kTmASVVS22Woom5z-PQ5n1sSCLE-JkMfUr30nnuUjLOgNY8YWTFz8K1LGZ_qikTgy7k965KkQWosuGM6avrPUbQVAzDb9Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i435k-uAcOOkAMscyE0ZDGyExONM-z4wQeynis90d_QlOv6W5zzFzCb1OdZfhL2GUqUGPgkra3nz4BcFtYI2QcMSysaRHE5miSWTsliF3JiFYdrtm9MKCvXfU6bCe1QR1xVFhd0Jh7WutVaiYoH_qpc2TLB47Mt9Y6OWQlQG7zldVlX2ojKy1NEBwQFk0E6TydUPEPWbrax-SUC5n2kPPOYfWzgSx-NHdpczkvM9kIJBQW0MQyi0qMDm2cYIQ3lNOcI9lGpkjeDmNbZJk7KsAvYNmZPdUORlSOss1yhiEJZbRezLUjdOXHhH-vMPkeL-bWrZ9AER4uS2c5GpLafQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miyHeFs-QaCxYCfyOOX3TmR2J8xxGylK1PnvB6APqm5SL9KrinahEBuyWs4BcAyLDBIeiK3tpJlFPPjbQ-A5zm0kS4MKgNaYnS9EVbQ77cZSKJ852MA5Q7Jao-EHlgYKvBIhRhIgtkYLMLtMP23OAqjJlcxHHgEWqRsALKP41ETOMaKtBMc27JuzYRC00w18b_y_-_qmHIZGOINW4Hnv-g4rk4SC5Sfl7hdA9k4Pas8KG1DOX5Unup3M8no0pOIDfhWPkdcx9ga9HdiS21FkkNh44OO6SIoKsgYibapAfFUeBUNqsz1tGpQmZEDbI_Mz4BQ_sA8GOuIkhkW4kNbVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9ksqCv_JWHb72XLpNhlBsM7vNCmyYw9JSEEHufDIuyBTyDUSkr9gzt17nV97HHEoxCTa62TzRw9_6b7pEVabOX73lNEtSW6_fitZ4j5ebAvpcn7IRi5cJNqLwUjZt89J3QSt_yV273gk3usK_Yk4p8OZNUxolVFzj4zU4bnjuPFbkh2nlqiYybgk4o1zVjJdYYeFmfm_m_AC05-h1hXyQGwwgDdnC0u_SK5YisPewvSJlSI3392M-fBX102gaHSPUNX5jm0yoMcMjayTHhRwDAZ4aKczuspaxCEv2yYe2ixQYvgIsZKfy9BOIZ68bcqDaR7H4lXWYUcfDpkf8srmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V999t7jKupCroxP_yJyAs1bYQnrmjExjRE55q2Eq7d1iVBFSU9zd7evmI9YybqNSrQo9Wkx7bzaakrU6z5Yxl5_g5F5e66blXkkJtMBsqplyKhF3OH-y0u7FA8Gl8mtCt3-Z2UyQRq8x63uzTRS1eXjEe0Zm7PLN9qpqiD1lC3YoZ5qHtP2FzZiNnGKBg3oZNy49EfhPb4_rXfhnFdC89x08N2KQDQPfKwu1Ncbnl6pZV1-rAF1NkNiAGN-W6ItgsMTyF7kYVi_YQjRJLkKb1DumehP5R1qmAJWqjnzyOilcAAYLeS9uZJuL5u4uDpX8WtNm9kLcIK4sCI7f_1PogE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0V999t7jKupCroxP_yJyAs1bYQnrmjExjRE55q2Eq7d1iVBFSU9zd7evmI9YybqNSrQo9Wkx7bzaakrU6z5Yxl5_g5F5e66blXkkJtMBsqplyKhF3OH-y0u7FA8Gl8mtCt3-Z2UyQRq8x63uzTRS1eXjEe0Zm7PLN9qpqiD1lC3YoZ5qHtP2FzZiNnGKBg3oZNy49EfhPb4_rXfhnFdC89x08N2KQDQPfKwu1Ncbnl6pZV1-rAF1NkNiAGN-W6ItgsMTyF7kYVi_YQjRJLkKb1DumehP5R1qmAJWqjnzyOilcAAYLeS9uZJuL5u4uDpX8WtNm9kLcIK4sCI7f_1PogE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM9OB4FIyqvkrDMX4BRpVs534VAbodLcqU_yRMjNTMo9bXcS-00MTZGbZvo46hNwOLR_K6cXQ9YIjRywbVVDrEGvVzTmpizmX2tKU2IeaZ9EDs1ypHZOzA8qEE_SIyKdGeUlFb3dKLVYDMI8MP1hhZUnjEXe_uLdL5FU4Bl8XHrD8mjehD1we6bFL53f9mhgCup5SRr8BoYVj91-CuGURA0YCalTHuvKzvILYzGQduJhkHUMpOQmk-8T8l2OP1OPLwoXDOg-_IHUJ-mgTSpSBH8RfbzXn-gRFfaBM7mqQwfPBTPyXuIRR0iKBlZE9vjuBI0aYW3TxbuXnSXuSeOHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UydjNOODrrFaSZfyeYLGDk3bt5tq-9T5EFu_7Ge-AtlsYllpaTRXQLudhSnA4XBcRhFJHtRVYn9vRYM9afL-NMTecmiWFzfvEVDtqmW_vv0sTK4KpdR7rzB7LATQfx_6Z2VQfpNHZENlbBe50a5GUxcbLxg94HJeafIgxzLNiTRCYudc1tDrhcec5hI9sQMgQ57JZnN48y9wwFPim8B8c1OThSIrc4z0AB01NShenAjqP19Tt786MgiHILXjnvc2WboLyDE9niCf8Ec3-xS5K-lNSpp7IaPD8dWbgZdxKDiLdiMYS1oSlcVVUx5KuSMtKZf4mEUnx8aQPTfBavjA1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWb_81U6j_Y-Xvq4C0LNQFaDGwl9LOaku1uV81zXsMStjqVeqEduVkdnyma3TMkW_esrshZRIwyRFdqx7WqlOrQv5jClW6S0YwjlKs7954Zk9HUTmByPjkeucbC4OHPU44zLT82TSwb0Shv9oBOwm12-JwGnLwCRxUfzmEYZkT57SA9JIhWV7TSyU58KNvNrX6-txr9zyqcX08bFGM9apVdo5h94BJPjAhzCTxNmuOm220X2Igu8Vk0qSdYy7wLeuPSZK3E4u50ytSGgUAJHdEsHy9Jvm3bhvI2YO9iR_hG8XCQAqCuLLVrdexLjHUjfbgCxYPOS7hStHsYGCV0sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLMCWexaLUJWP4N6h3uHx6TmnBY9FevNhb3H7sTRtxLDu2KOKoAmo7gLFLzClmueT8IKBnZKd0UNUhttV_cDIj6r1Y7QUngevpNpe9K0VYwCmzs7MEpyUlH-9Ct0wMqX6T2VroiEw3s5pcZsmVPcNY9iKPlxBBoDENMHBAinin4HP8VXLJvQEAkzX8Wdr2BUDKylTsK-emp8BkWSswlzcsvaW48GI9Hl3uqrhMFmIlSvZxQxgOe_LLr6VghupY_i-Lt-TVVksgtfGImQIK23dRmWm6g4yA_03oHzVcTgqVZuTMYwPv53hP7816BoNZwLkiimLSyQAlOfJrY-xtXE_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvUUOPuDLFQIFhhAyIkGiXVFFQOshVZcMljb3w9eOUnbCAv2qBWne8brYGkDDVl6ERLLcD0-A5jKSfl6e0EyXHyJclwVmyUizi8Kc682-WrGvsHNHgfPfvPfIk3Y9wXfb-HEEq-1xHtgcMMf60GO5tqD7E31e0RcZ5Tbbe-fwaRCa6RD0hMbxvIbAbljd_TZpWOGZVdXbk9CYdbb-ZfaBsjZK2lQ2RgBBVdx3XCznv5i9VZLUBh01xeEhtXFpOJ0BKi4NX8n3fZlhSE20XmqryWgayjNPnwHxrfYVe7oSRtr677Wt-ly1Zz6zRfEzvhG7wG7M9JB40DUqPZGDBbjsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm6DrNcXr8SRnCQrs9GQH9tqPSRAc6FibCD-_BahaJEZ2bm1JYQeLe6TM52-SDCfcNEZraMSvzjScjymo_hTGb0ckTzHtbdPLLoS6pt3DBkzlrLxFt3sB8AUYQBK1CSVm8HRWSer53kOv8OspD8PiAICbw_9R470vtD0KH76fHyPzHfkPrXWHZaHUOmg-srxSj-G_6vjZJLjuv4pHSdP56y7ip5W6fhOwQtUVyxROnU91QoHMD4KUs1zK8LA-yZ_uk5nlaVqiq7i51XgoExbggl6mG3q72QzHcY6Pipyr0B1xpnBpylMrFBtWvL0G5iTxH3dL07ox3oldYR2hRLxbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wp-schema-pro_2.7.7.zip</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/danialtaherifar/797" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
دانلود افزونه اسکیما پرو نسخه 2.7.7
✅
کانال آموزشی دانیال طاهری فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/danialtaherifar/797" target="_blank">📅 19:29 · 23 Farvardin 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
