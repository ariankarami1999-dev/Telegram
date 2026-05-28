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
<img src="https://cdn4.telesco.pe/file/PbK9rFh8iVgCCEU8ZiOEnjQ7G7HcoIst5FDVfbZocbiSToMkrMuZRpkJI2rp8D1vqvTgGKcMVrVLjo2BT5e5chTKDoKuywpfoYOobCMhFvAA809DdJIHQR1lDC9CeVJePO2BqwqRfmF7mqpTs6fOIXpD89I1jGfT3Vl8NOjorGp9N6yLyFt045Z-0ZLMIzNqtNMsrk950Ef0zNvfRFUE6CgP3X9GRu7M7WNXlerfB7J0haqZQGF6zf_PwIwcScKlGyH_32lipxG8Nr7aYcB-o0OsUrKVLZzFnViOnG6zzdLJAJmRV8dEmxAqxX-HpZ2VpswIM7imQcYJv4hGnArffw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 253 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 347 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJc_CKadHLiBq1j8ZbKM60kkrSbKWEkABQIqFH4uxqPRUi_PEx69YXmrqFLGrLgiWJFfEX0Rxl5T6XsB3CfVnyktUcjHaALGBqiYzFx3t0MjrmnIicyu4fEHhqFunUCtWEqeRGrfcCuSi6oUnUTi2fv87r0BuEcc9KZgiQesLChJVGfSpSwQLHKIJa73WqXncjftdUt84PEyNuI1TLptqVwgk1cbdtAfTy_VPCV2vh8wJmuJ1GKWuZVn0TIGx3R2YpsvQEeU1CUrjYGOqNDoUfrGTfg4t0twFCt9_T65YWdzdiVq0-9LZhhDpelENv_btsCJluCf4lQffIbT8PyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 442 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RinpQfzWU422E8RiBuAClkzWTgpuHsvN4h3iA9hrYADpsCv2Mt6bfHHtACavANU9QgqqqbiJh9NeRE80JZC8D21KnL2SL07RR8KDk-IqDEkouGcxas54te6-UmVhnZrxJkgtk2-zreI9cBFRDs8JonKyp2sOcLmv_VUac6V5AkjY3fvsftyIldbbOykNNUui3ooJFYAwfQXgm3wXU6TJNRmm0CugyQuOfHDD-kHCTJ0mXXoAJtP9Ay_lLRFeYPkqvU7U3IhfCgRHs71914DRd6DMjUWJT1IArJ5TUIg5ZNFfUQMiP7vB5D0AP3rz8O04EbZ9lbFvbYj_9iSnsYeJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 703 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWDp5DN6XbbEd3ylpBV1UwJVa9H_coL5IQxV3hIqX0rTr3nyc3wKOrD__r8rPihuKlwmTe0S4q3icnjdDXwGR78k7bn1PjAXTjpxzuTAEgLfhFVFYGaStiL112mXroEOFeVxkJLhF3C-4HLkMu7T1jEnAAi5_jd9oTGl28p1nM_EvizrG3RvMB5evdii6VS1BDg_fgFdU_zgbGGzPIv8EpXyu8M1qcgJ7axAcd9O8da_TJ1X60bncm25C9j0sMyguhsPeO8UXs27LnWdb-UaGvZUqh13T5CKWOpDr2MoToFS_IxrxWg3tWEnQ4f5wGTkMzGYWs7rEx4x1WlLQq4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz1DUxT-E0D_ReBbTvbT4wQX9v6EpPTQ4dmZqqnhXdwKgavODQ3U_-6Xw68Tw4UwWX44Ga_yyXVwBTkTBdetopCXXCUI7xEcs5JU-Pbw5mFXdX4t9A0EFK7HVg0UcY0p-CUva2Gis6Te7ocLT1zXHquTyPhiQT7FfUpiFfAc3-e9w_ehbAj21cWeR7XzVIw4D99rVTQwhNUPXeB3MxkQakttD1ETrkFKqTyls11y8mN33de33PL3XZZXyAjKdBTbdc-LywpNYTxlWPR0VRzPMflgj9gAx16vvTCXFbYzVvHc0j9TYCefR9R_OI3X7FdQUdasg_N214QwN2sVUC49gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 999 · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJq8ff3Qzs3HfGIqRdk_MvZ2btazhA9zUeCzf4znqpF8AdLnd-l3hWLqZJZp44D3oJ8rmr-mFuVCGLJE1Pjj_Gnn98yHlm9yWjNXaEc5XprGfA1HzEFA3Sn-DU5rGnoLVKNnlW611v6IrKhessYU03CeZeLvzjaC-VMnGWQ93xS5Z4a4RHOGSMKMA1Loc8CrtYifmDXmL9SoSg2PPZr8H0hQSj8RWsS_O3rPwcPPMIJ3zgJrSVNODDE57MYuIHc9LRP-2H9ZignkKDbznw3rO-A4-SS2E3z7jB4rkFfu8k4e8Ux2C5yGcHnpxEQRyAvUGP0by6bc5P01g1tqAQKmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 756 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 778 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/volov1B-VXzxURzm0OL5DXuaXBqXREavRtskad-_mbPzMgsW9_w60q8nCe5YZiR4h9iemPbUkjNwt3JECc8vlWJvnauYpPt6dz366cDuS0YSVRBnj7Z4zaz-ta4oMAW_GFNOPgpmXs_wAg4InvYiPaue7pkXRd5d8FQM7Q8MRqVivou-2F8D3FUrZo_-OwRrJqB_xDU5kXdJdbwnfOIEBK7JdLucC69znrm-uM4xYtJ_S9y06cmMQybGoJvs4p8ESZA67d4BqDo9LFRK1rCrcDO62s3s1keF4735YdGVaWimkD5CSFGoJnfkFN2ATR1SqWn1HTnRPtcFVb5RhPzSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBufH8VIrlMcOGgySB_U4v9oozyWbgj-MFYbhz10HF5ed2UxfPLkRLPoXyNDYuFlh9dPyAfNOwVxa_Int9KG2tocF9K79d2iYzB6ybsosIX3l2F7OYUkStNQmXggml9NiJtq_JkOEtPaqOkkOQaU7delc3k8Ep6vkSBzsusVVTW0fZb233XgXVLG7DQbTXZlaecrpSbTE7b6MSwp7AUAHFpyd5IjRy2P-HPhklv6Z46ePcIVzmIp5cccTfRF7GpgnD1EZtuUKrh3hWv9nEr1ZkLoelKO9xyfuMC3xsU_LkWLP-gfLWJU1CmYKMEEmEgGNt0R9uGRHzIqbdvTTh2Hhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Trw7T8l2UzdLRWpwuuFxfGnpDOsPuA_503iwV9ZbV8V2AJO_5ZsMAd9hGhg9yt78FIIQQqqXtTg1XK8AG_6Tak4NNtY0zswWAKwe9-DakrUC4WU6X1o80PflQG7JPodmTV02vs0thYGLHm4Acj_3PRQgpprVcUTU8L5FEZZ1341g_b9LIjWnvFFyoeK553sP5ezrvcMGdvjPveGDHJAjmXfejjR6SozN4Shihyzvy5H7pyVWP_ylAlaV7C1mqKeg8Lyj72lATjLWnOsK2l0TAqNnRlWyNiJn5ugd2OaNHdATMZDn7egxs1ELGnulJZNxotlz7vcZrAO5wmFnxZBxwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9O9B2kJVmSW6x3N6Nrwr-B_4PVS3bpPu-YQCm0BxtSpNjae4PtF0Tr6t0lGoUTdcLgdq3-5ChfBSnXu2mQkvWQUda6bdILB7_vI9hSIL-YK8IwT6ehqUS3XAbcxhtvg0rtP479FywSQronTrqvltC3PD7otz28cBEYR5ZZXIrpt_IvErTnY5dRXPiPHuSuI-VlUlstFz-P80CdZpsmygky32vYCdsxxz7opvKtfUhDYMDni6gBok9-fiA59dfd9wb6GErwLNfyFl0vIPynHGr4ni1RzI37gZv9gA4URZ3RC2Pa0812vMM4Bzkf8XRdT_RMc9acGIVDi5ZRq3MSMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 933 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_dUL4iaZRo8DHgQftHvVR9fEQfw7G1yxmfIx5Z2rooN9CfCPtF06qkRshUten7O4M_MWEXsW1GId1sljjvqZ7XV0mrRm13qGreg-0lnkCpjyL8NqUJ2D_iFtyvbLP5sMr8quezgjGAWSNBeN_DrAm_7j4oQ5hwP7e9IwAoMefFBWOrKbztAXIpaUvQrtYogogyfFbpNX46pX0QRZS_WA5xt13jliyKF_7feg6jsD8F_EnWz1hBjuPtRZe7PcvUvzxWdbDUbhVbZDsIM37VMOc3P7Qqkas6rAJAstvDHwN4RylqncwTkHmIFSWd_u0SU7SD77BEy43DU7n1XBAgjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fro8Z3Az1BrTjLO8Zl9WJ10m0LtJGQylkk6gjfMfe_THjDuLXNBjw4absUf1mOi-Fg50vVAkpDilJpg55juc5Y_RKNKFCf9SITVPwXMeZpx51dFOLWLTOQ-QTHTw9FSQvwC8mscdbdBbjr8ee13pvogGwyyoloY7DogXqoH3uq4CTYcq_o_dRSziigkJxhdMMahjcWEuyit-uzKrbyz846ipaOQ5FoOQ9VIkEGpUM5KSqhH1O9LZQuzafsAi3tKEaAymVKfeHKXMBjcLTvuod1qmaKrnbUTH-46vqeLPG5Uqfq5wgcNMyEOF3WKB8XqqpBUeuxnXaxRoujgYNiX5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8JytubOnd_p2ItA7_fXbmK7m_DFJh70ufOa9O98YfmApGawwPrJHbIr6swmGTS002c-abBSTgH2CFg1uoZTZ_6Ig_mCQDiJ4-fTskCl4vs5DslOg1dvPBtZtnC8P-MsNBSdiYmIcYX6wnoC-MhX710xNQX8iH5CY_s7mPacLqx4zljCMXlZ__rIuHH9RqS8hOHDiaDUlZqo319xoUcttjGI2IjWE4qJGAVoLhCPxchpDUhY9wHUJHCuZH86REnR5ofi0AmV7TujcEt42cVTPB6SmgvIyHbsBEsMTIVMo-WkwlS0iy3w5aa6Tii99fd3BOy9zSOvtGPT9Z0yAlksSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 872 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gM7phtaNbQczTVOJYM5AfqT_AFA1ECnCCkIEUfFHaVjsO_dKGMX9V5Fsk7ZT8fOnEoQjQmj5STelux3UX0sCjFrb-gFXUiXF4Yahx79r5duLXVk2xqeMaf2WWbOV5p1QI36QrMDWREkk2yuNWt0mIbwn00Hokwur7qhpGdUb_FGsdkyf3LbECqBi5RaWw9m7NsiufNb9_xZHn_xQ2nEkqhfGPOTlbVN7QdYz8MICc3uVYqm76UeCawMOnY2pUSpEu-X84MTb1_fU6g5tNpb-WrwfE78N9QMbgnkSQ95z1n-JTHnS1ZiHU_g1vWZr4Ghq-ehInPHmYUNhpCK2rA0nGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2XwesZUrwlmHgFGTiwHXfAE1Zg1p41vWAoyyl3_7DOXdvE7-M2oty6UnutDL2XlSLL0KbcuZLZVj_sws_i--to5jrJqJkgd8bSGeT3L004WhwoB1Jxplql00SWneod0xHhMiX70WQQ-wCC0ytauqy_41XIvC1xqvOztufjLk9dikmoyO2Xbydllej70orF_rx32HbbBhgDUsBNVZRsKVA5hafl2puc3T1hfS0LPwBluBQk45ipWdM2ZEYrN2sMSRJhwJgy2Y_v2uwI36iA5SUVDNyE7pHfDuepy_sZhdA9zvLf5iQOujSLh-poS7SlP0DUgRzOWvMzmT6lDEpDz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccSVEbHHTyOb1qxtPd88omsXSzynZbAP-fSMhqFB1gTkFSeYYJi_MIQTkkrXuxPOfNbhWBzPMCjjeGS3fmVC5awfkLYkVcHcg-76Pq6Rohead1LEvCDjjR-TFsYHNBlgYhCTt-tv56Uz-7wKcHzpPYj9ljFURdYCBU9bWMMKI135p6iDW9vpeS4jzKshpXYYATzlK0c2mkERSTZbcTNLXSZgh8ir19RqzYRAFut7dbf7bXRKZuYgcTgdVsNNk6NRWrlntZd7Vs6NIkSPFcXyRBUs5cpIq3YjGZq9xX-SbKVNnbWoVruTSkLFIy0c6JKk-SOOl1SEITi_YaFs0oKOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBj4hrRyAL0kpobc4e4psD7Swkxq_--F1YEIlFMlc4bIEB785ZR-_R9NgNvWm21-N45R9Inl2yDF34ZRPNUhNJ8se0X5T746zdKo9ljwudXjo0caixLrYx7bKIXxsRMfokKV6XQIEcmTBUTZViOXQ4vMPOrh5qpb9eDgm0ASWYM15kPf21x_seLl1dSy-r1VaCbynlHr7P1ay2PCCuM5Jj75QcE-OhOstkjluKDuACQJ6YpOcBzXhpiQXoDr_MDqvPWoil3mrH92Dn4G0OBZEUN_C5FfWExHudcbx--HOoe8jbGocr430SqSZQXe2wxoXHuZHElTumCkSRmYjme1dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 947 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlpMgBSIuGPalNrBoRZJYlMrqfrGWtuhSMR20cnCNaWIsV5TVKg1f0TcUcRDrba1fqtouRIj4A5hMy4QkLmEl69YuQdtPgjakyGAYhC_TMsfZmgZR5X7cRiaqCt3trHkqcL3Gd-zowWZCLgHYx_jaunpDB3ahlCBhan1C3KDgvlVhJinofPT8qmRy0OxCDlOzk7-uE3N4IdlyNYgtY-Uw6gZ4MWTuih1KNBNVHRAayKxvQvmuEdvgarcWqJ8EimOUjWRlHWet2VDmO2sLObTn84Feytc_oALqNykMV0HUxjH4YqM_DnvUEdidzM0GjlomdLs0NYQm_BkNWGpza19AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=fCyMet9gPGDtn06KMh50-zP1HPnHJUWa0nJlyl11vN64QPNAyiJid3bEvT8SPX6s6Y9totRwM79pWfNjK8XpKuKRYD9JQIZnpoBp_jK6_da_TUvZ5dOyOYCZppPFuZGWzqXW6hhmnteiKxmjY-hJps0eoqa2fbpLr8XufgrAJCF0FR43XMNDcXMx8wWSEpK-dA9vNDCMUsaUwJiQdFby7jf7yd1PkReA0b9Yl3WXLMo_9MEH4tlWNr66Btw2m-KI-Y77vYm3VjOo88YEKEJkYTCeT5nF_M0e4wMCbTsJieuyf7SecOSV_-8lCW2wXwKjU30a8PCqJY3SYbsXraZjWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=fCyMet9gPGDtn06KMh50-zP1HPnHJUWa0nJlyl11vN64QPNAyiJid3bEvT8SPX6s6Y9totRwM79pWfNjK8XpKuKRYD9JQIZnpoBp_jK6_da_TUvZ5dOyOYCZppPFuZGWzqXW6hhmnteiKxmjY-hJps0eoqa2fbpLr8XufgrAJCF0FR43XMNDcXMx8wWSEpK-dA9vNDCMUsaUwJiQdFby7jf7yd1PkReA0b9Yl3WXLMo_9MEH4tlWNr66Btw2m-KI-Y77vYm3VjOo88YEKEJkYTCeT5nF_M0e4wMCbTsJieuyf7SecOSV_-8lCW2wXwKjU30a8PCqJY3SYbsXraZjWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssSQzZ2Ka_3Ai-zGbF44uNvCC3fvN9SGPaFB4WdTJK7EmcuHuDMzKHdKoyHmf7JokiCUkSx0n8RBA2cS-WNm4FLrLKOKQEZQ9SrnRXgF9jSQ6_mIIV_-DfTWl9fJiFIOWMOMxLtFQEs29rfS4Ye54B84edZaYwRM3DVWeah9SF-Dc4QVGNdigYXgnYNEQWTUYNUT672N3yqSS5gCPe9kzfYouMsBf456khSB95LAdySlqaNMzL8w723BoAslJAsPduJ7AQHe1MwmSGS25MjSzjEccS0U7mllpwegDHqNiWCnJwPLwnzpeNCIDtSIUWBe3qYM1u_w7yIZ7LbytyF2nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK58LrGk8Mpb0Ki1lAz3zgjWl48l-4asBcFbObYtiR9bCuOw4vZYl0dmgCZUrHnygThk07ntA2ZO8EfYCfFOaBj69lX6-whlawN2B3_4TScVD1zKgD5PVukvQ10UpPBlZE8t53FgGfDW_IzzYEsd78sBCmRAT4Xyni_Vi8CC4X0jI7fBYCfSH478XSJvznNu7F7k4tTBlzNCOoDS__g8sKLHXp068ubmwFP8Z6dutlkfzUzDg4-xE1vR629mSTWMCC04x5TTLd_SYlEbi6FWn1cIRdcTLgR_VgjpHDpIKqzPPXY_4243X_N2813VVisliJ-0W0XBfCzs63i6V-QibQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlPmaLU4bpzV86YoI7UBJAVJ30X6CtWFZdbTL5URgnlnu9mswSv-bpTgh96ZNt859QC7Vh3MPlME4SXn-PGdqhLl7k9Z7LUzt_DOZdn9eyYPO70EYeL-cy5fTOu_JZV2S909qST5tnDrsqSwCinz5JQSyfGoy17jiAha6RzRRZqT5zMVgb4aN0Ndl6eLF2cQ8JHH0vAcn8ZYzPEYah6NxF-fsYhXLjpqg4vwi-69vyJP636e2BnmwJA0v9wV3KCtMxkSbucjpypkRsnb4vxWq8WqYKAlweS5LlJx9ETS-MgVUNAttLP0CWZiVuMKqL6n30jRSQZAh3SMoHaaVVh-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8kjOrwwF0cKIfbgmv544ReWQzV7gL18nJXetRe19wjGz_gq_-20m5UeY9lDMw5XquwAO5fgJKaaxgJHju07po0ClQQhP6r1rszGI1XP32nBLlrrWHmJZTYlD8w2yOONGjuGwSLH6n1ah9RVQZbp3C2CHNWBKGr1ErM-4VgAAHJcjK4GoVqDtZNr3Ns1GcFQotIPXdClHYH6F4bPIieej0bTrPpN1raEiv_Ph1Nm5iw5jS8Up2U8H6K9T8Z0aXUHx70mZ2GrVlumVBoam7kcVql9cJU1plgZ471TTvOUzdu-sIfeaKiCPq-NoXPq6WdFDFIqRPdm-ZYU-vrVDHLSdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX2S5jm2zivgVGGBlXJxZwMAre9EOJZo5Xzy9QQvGlJ8DgABRCCF4taKGsEz-LufjtiAjnH-Hxy2rIyfvJ7pOOVXUn8K6ztX3opIqm5Jd-FiEaTHWoVB7kDBdohdTXl7ZckeP3E6tIs01uQ9FmKveUl8PR3WYYiFT9xADWTpyvXm4rPPd7iTHLpgyZqh1ZHHucVawByNwcZiJlg2CdHOZ9g2v1uz4gG0OFyH9PXCshWVtWIWeUOc1tLDjAtgNrdOV3j_2JPFJBzZQIlwZF4ULocN1708dyZfhydZP9K6_-OA3-73ErQTNGj0uUEU9KWBJLoGZpjrbCMn9-dZvyFTAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6M5qmbPjkksLalsCGfJB7YqLgldGG2l2JtsjHynIHwFV-R1NFqQ4KqVQpNttSpoAu9HFX_RB8foYa9p46LudD_EoYfpR6i9yDz3e8PSgSeGirieztsWwvWnbLIY1X7_R8V2g8hbwKb4rL3JCCKhTviHKDmC-wOkihhm4z1nL6O6JoJHRW1PMJFXFCQNQYO3wl35vVfyzRxJQ5x7mIlzfsosPuG0hV5rMhCWbiwqIhKLJVbQxLGMg66rZhoHoUxdswMFQhEi-pJC5K_RxqBrzgud290rlw4LQezi9h9keiG5898CzL--yLerL5ZQkwOC5OZhx2rlnklKMo-8OKSv2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzsR-xqlmof3lKUBvzYjjIJz5eSFkffa6XpF5iNGzIKkW13fuoXW3IX_A0tyu3aIizKRqkzqpGnCJ1oLQuWlabA_z5V-B4VrPYeU-KcsucLUvcxDRAwDPXEIbelkGS3Wa3PtBFeeDzXtfDdyqnSuDYQi2lABj5sSNV8nn-m1gp3o1FW80gOvNZY3sHjnFh1Eyf7iDsg3x4oB2NvA7knBNAoaLpqEa4WdlVAmFAduXqv_BvgWGvsA9YPQt2JA3dlTTpLsxT9UYRQmJqTeLhIhw0dn_v-IruYUh4RBJc8dhN1NVf_0X3Q_q7uPQ5gYiZgydX_w_W-W_50wGV1xUW_ImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBDVUbqgIk8TOYF--3qAeaMfPYbupj6pZ3BwTvUwT46uBZ3DfmCEM-7n2j6v5jzkqh_P8F4YueTgdjIkwKKcK9V3ZUW85mLrYHYXw85z7_rziHpgdT1HBeWiKk3EM4hIE-sXmDBUx1zONou0jyXkrORAvksum1IFC6WE5SAPwgiGq7BKbcX_oEiKcH34VK2HzCrRPgTYftkA_q3bJMs0g-pLwfjSTVE19NjevmlR8T1a9wB0upv6E_RxZ6UZae6U9DDTh_7OuihBkSjoBDF7pJ2F1QN-0nogJqTQ_d1KQnbp_nG2wvIVyUpak8rGWl9JH7ohMfba1PMqlBDQkj2dTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldWvRPfnMPxFiLlOb_RmfdSOvoU8bTs0MDqlhWDHhgk4Dq4Nyqqq7hHF34aITEqHuwsyixiMWNz00hEBKETE8br_Vtl0xHW_-ZSpWisXaIkqOe_KlLZxqwLsM8iGFoQDBUTIhWtBPTUX4OWbrSj3jVZZrjerhCa8JoQjtX2uIN8qZ3zAPLFg9ZqEN-ivaPA4HOfUa41_45iSzpCFeoytoW53DDLw-qH50TwTi6Ag7MhZl-ejNYXCrIz68iAV7r_AmxABk5Httk7fb8aH4K2QbSnQVTaRdvtreItuwtKu5gBxh4FTrXCumXTzWpFMrKabjQuIuYDyvT1jqKJ677CQEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB_pYNkxhUHjlHSk_MMF2t8eXc4y4MzTJZgWzXeRJen9VmUXnpk6UUnlIMVwOftuylDAfIPmeKAtXBJhbiHjsfRsnccBxdIRtGsaSp4Cy1XucFjRlVw-W8PkAUlk6ZxUQ5vNO9H_lMuWSbpN-CYARm7xeWn7hug4eKEp_xhOATzfyhdf09LSBtq0bhOMOWRHsXAfYfCAXbOUFvMKKGaz-y-u5EemW1M_GABkAicW7oM5qfLqUrs7bupKI00gS8_0aSIJTBYLNm6Kd2P0V0KrReoNRV6bAYNPAf8YaioCag4cTGkkzdDtk7ArU2XeueZQCzCIC2nKdLVnXW2GFV984Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5OWtR6E9UwV5dY2MNkEL8NRhR6PB5qjA-kYe1N-UDDhF9sQ5NwSduA-WuJO8VWf-ac7w5FAY7tuT4ASBPifLurioMXjTpmLmiQ_hxD310Cx-Lo2hcQ4EmOttzkzXffacYrUEtJ9T1Nlqx9ypbPWSiulDsKutBpghRu21H0ZGfCAP0gZ_U11v6tcVlePavmzVBOa04m-xIywoRq-_CMS3IaOfBdTaVmZTvxDdwPnfrAtqYR14RwNsj3pd22UxyRB-tPFzUACpvA8FISGwAXfdKsnjBOTpHQNlVZXAbULglUWVZaHoUGCdVIVReIMc34uLQknfBtAdJsaVz1Y19GtCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9m-I66fAM0acbuFz9b0vh0FrmEUljBwJ8qBnD3lq8Fc2DBbFaiRXEI5oZKbhomG-o_Bh05b6gIyP__4Bc-aO4DFOJ1gJU_X4GeteeyXPMIU2me6lS59og-5fNd_sSoVkA3ogD1v5C54w0g2q3Mqu15gWTlIHCovLbbrHq2nqXHAkdbrooLCUi8zLxjbyZ6aXiRDj-2dMbUMxQTgHJb12AFZjswtFRsfwF_SM4b2cmVaMzgDnL7NLElIW8hJo9xTv7uHp7-Dgi_sprQhHN9mpv4_JxyWt_L6lXm8Mqs1lTGmv21kc5Nk77rzNvFsIOqgcVoSTPYAj0roKsszUkdp9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnS3HGNBc-N0X_bHX8qpGtpJex-uc2RroAbhcC8V8Iau9LngWtsAU2pYZIhVrsfUwinMTyD22oZZKNHH1VlgW8fv9FsTVcYx9--uI1YBDm71WMb9jacnXLQo799orFajN3ENs-CQd3edv5uPR53Tc8CsW3Y_tIwCBDi4c7xjdDN0LiUAs0rIEtf8-HghTRij49BLc_P8mSrE8vNTzzO-BXIZW8nuN4i9UwlT1rQA5qfuqgu_C3krQGZWxZfVp6sQu3UidGwLixik7H4920OBMT-w92fzraayc5FPw-NH49p7UXRjWjv2aTAmUUp_qSRTAvAO7q5SpvRLS8B5IRAUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEKIV-jS-WYHR5LqxDt8aj_k1jCRn4fSRQgTwAdmQ4G2-oXN42bmYSKrnmf2M-DfhUHAUFXdEhDlyqj8h6BJxLOFunP9zUkPHcOTI4_oShknqeCBrSN7dnA_Hn3mWSXCZQxAXID8bmoMi5X8NqQXtdXnUzUeyDfpamPCa4ZBIZ89nPzZ29LpdmDouD04Ho8rMdKNBmtA2LSGvt0645mglzqhVzom6PyKwypviEEEbDzfVC3_PC6W6mHhCvJkqAamkfjaDSBRKShI1sPW9KYSEbT2f521UUORqR0pNZbOHKGMGw-ukLW566MeH3dGN85g6bm6WOy4OcKenru9uUQbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Exa9Sl1oVmQ_WxK9R55NFQHFpYjxmYOffChe0QeD-Z8k4nvj5hzGWsuEVNvhvl9F3_6bdMCesz54vRoB6USdNAgxeCvJ1ak0LwJ-vUkF4AJ5ppjufpZ8zhP9lf-VRx7ZrX3RnfQtMe3ZEOZH0ITS5Zux6uWatnHmEku3FtujCW85WrINaV0Xsao2y9RrDMX3zHOfeHPpKq8BogfYBvQjZLdIwdyEtBNzrrzsH34Z-7SchaUVVPYB1J_iHhcAlCs9uw8PSLxcJEQuktu4D_K285e20IYxxr2Z3eMGhDQ1wzH8FhWFuZlYJ1rV6PlIPuaDTvAXMcdaXJbIZXCP-a00AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwsF9s99QtA7dJoR9IpEV9gEDMssdafqfZG5eRXWtJPyOoWt9-VbGt4teYzCbIS-2F4kMKcVpnp-V2r2kiDCbcg5OfkS038xywwtsJd6gh-SGy4fBCc2oWit7ZYRnJ2U4JdRGDPKBTxzoFvtgbMZDH6ZX2ua-9dPQu-WcidfnH5qtjAtCE-X0NR0p0kbktXioCWXw5QIdz747haUioi5_nDrtVwR5sdmM_grOxLyepbqMcwH_rueXaS8AHxXjhks8bdWHiLHadm4S3Trka_mfB46LpBafS8ZCeMHW7KPhjrXFo5k7AjEMr4b7eBR8orcO8rSZO0LIl6eqsY4wd6s1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9Rz6_xzZCtlmPTjqWreXH9QGSLepopJJx_fppeOTHVLRnjsU4mxxwNEkzZ63i8XxhMzGayQhVPFBw_EZ5fJ7F7VwoWZjsy3gMaqAaP01Rn1yeiDPG2yW3zEmGtqLwvtK3TI4LaGpHFOLVYxgILxhjy5EWEe2a1kOhB9VLN7JxrUH29ZIDsJEdrMPMBStDJggMH6-cnD79sjj2mwlW0l0uDThr6P202KzZmT731nmmSP9CZ6oWKTwuEdQMsaR1CZZuDfHtG8dMvGhy4-ho0BpyaHCEg8TM6_WRhJ2pIlmkFmfkKgHy3a4_xIL-dQ2BY4cR0WeciZ7va86QcOIUyWRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrqpcJnPZaU-jgoYCipFpda1AQPrUCQbBe25kNS27ggcxx-XW3VqSbFC4_lVT-a53mQUI2Fom5ZCuWwAun6t3H8WwBbDwBIHd_e3bjDb35XaIz7LQjcWa3McmD1Jq99nRvpnQj0R4b2cDK1KndXLjb6KfH1uPo8YtaAAcxpbIwNeEzMVAlRiIV11w5Q1HQeqYXqJ9SxtiV4zZ7mh8-Jdi0vJkcUu2Fx0Q1FB1kzS5nhPpibBTbDJzeePP3t_qtDa2l5kGtV1UaxOeklnel6iCH3h9ekqU_DuX0p6mTOfEKq-K3hY7HC4_bZ3n1XbsARhFvVNuMGm_DL8jY82r7cWVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBF-O3MXi3wiOD6hvXJmyyYix5UAt-saqQEgCOBiyUmG-vrYppnrcEu5ult__jyxrJBf26lnh8U36Vcwv3LM8EvtjJKuD3m6Hqlr2e2UCJIgXy2VOzChDztvEFKqZCVsKR8x_RRDGELOrdBZrWXzigUwJ6-KLPgh2xY3JGrmfZALEtKl87zAENMVqCgQSzZOZlEhokcYQy-VS_50ZqkumVKaYOI8RAKcYCaqrgJOYLlibV0Aexl9Rkl09_X8hvDV-Lb6jAB3BAw7iVbju2COfjfEEFkA9y9Y7BcIMH0vtoCCZGzI6g3m7iL4UuDqAIIxtnOBEXfC8B4aQgrNDmyfLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUZYINX1n4gPCT3sb6yKQqvY5gC5uIC2CoPecsEUSbwmK2xFWlHuck9mCUGGIJN935m1XpNdYCniLvPBwdOS1po5_OUDKP3USdr1TG9pzmGOmi2YyTNhqGUpMpWdDkT4CSQob5lkmu91OFkT5V32V1bbba5Cr3K1mVFW3YtxmtNMuY311KRtSUwTdDrr22QA50eoKq5Z32HF0O3ivdBhVzS0X37CpuAqaaHDQQaeXrw6Cj17ZEpOMUFRdHU1rbftFfYIcpBJT5gI4DxAN5VXebUVOi7X1B5Ju6hpAmpYp_wlNssA_JFz__k-P31UhrNJXl9zW7zkytswdhYXFguAZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu-_DxVt2xg7wFt_Yj1HzqhMM4RpQhc8WZlG5Y3sWYU8xxCH6IxGDc_cbJC9RyV5PeBh043E2kYVdvJpLihM2l7quEdSBgv_0m22dTgItdDwjNpGgXakcjBqUc5b1pDoZeG0eUYJEwQsYt2WAVoGjy0QBHWW_btm-LQYqFFnTP7PFfi6Mqs1aed9aycJrUZcpfuE7bslRC49Emw1tfIFXBLltO5dkoyfiJtygF4846ZacCThY6YVsQZI8oNqmHmBYqkw8zuJbDc-i5TjLBOdmmwzv3jC_inNEjN6azsiLuQxBi2lhWmlUCLuA0YHCadJlnFSti-nrS8TS2nCRAXHLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOrG7Ou1H-GBiqrK23c3omwu7KdMWIQKYfq5wPFOuHqTBzgK0z67T1ztKCvNCqXNtfiG_F2w_BpzEWJqEdZECL9FoXmDtlRYxkfWENYDl-OpHW_ylmU6gVbPRLo4oJDyrdufVqni4xbcNxfKDMdzjRnqK2m-CwGbH-3Be9RA7CZXQ1Hjau9kwW-oddeZcluvS5X4cvhSXBZSeSYTvNjCshuy3qQQGjYRbuTLA46EPGTebMk2BnNnfl53ET_yHWWqIpcb0ZvoerL61rEp_8SQIFJTiPQeiTb45-suSP3GwRAHmMe-xNdzWy03Ao24bdx7Zoj-Rt5yUKRS8AxGkIbv7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjrmqjUo5avciPJ0sF5yUx-ebAavisl4WdKvNWmoHAn789TLxlogGCuQGoue3rSRCEncsqmX5hiyR1mF4uv0Q4zoMxDVzHbO64NlKNqwTAKOZ2vNxBj1DVv2mitfV6pAYc-wAb3UVgvm7i8jXVTQPi6ykHd_18y1KzNMqIHhfuyUy9eAzqQ0YWaFsUSsXzQraqgXJFpJToeNjnK1dEu1Yko4RiLoaOwAF3ybwYrpcI9d_zJDoWEDRb4vdlK9urPTFuOIGpJyB8l-YWGYKWA7wbz0A73fz_pkPv2kDv4l7pVUoYxktsGqbKqXq40WC9URJ5v9RZaOip2xs_N_LMKr6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2GgKDKqt067i3wyR5ZT5b4uaBQeqTph1l8VpXNPWB33YSJcIVPmG-KoWKDFJBS-5Bq6vSPdSNA1exImcgHuFt1vSH0YRhjwDoRMSJk1qKyN1s5dfRTdqxApTv93TSgzPDudSQjvY_KNBZM3kZ_tlPhOfm8XijS_ly4UQbTNBx-MarQcySWUDK2WsyVsnEFPu_lvugv6svOVYRlj3vFr1msW7kNNr0fKViiFjGviBEIqFngrWgVBVGScF92ce15vzwltuhaoWXPN7Nk9dU0-9xLRFHtJlXt9ebWeilDWP4G6rHVcitiu6c8Jj51dd8V6gBqQFSN3kZkCcuUchzggmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikLumpHwGmpM2vyyUuYyGWsVrVN1r3Fd7hFznDajJrj_NQ31oVIsneYYpxCRhamK2hV4Yai6xleUWCOVjrkiqxhbOFB1NaWo2MEu4E8qtItua1LvcPGx_0KFyxN_KJfwSj01f9p4p8IwOv9N1WVItTmr7SjMNX9H0_-Qbncj21Ov3ZzM4Wyy70uxsDujovbPnaeDHFulWIMuKgySHm52A6fwe9Ce71IGeP0MBQLCLQ5qpV_h5GTBt1ofpTaVoG-xVBXrXrX9tq2U4KLOQM8vCAE6SL68Okd7-JB1-RGvaEMUeytzfSclXwIZh1tmJBoFAdjPUHAZyOf-XACkxmSfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkLK3FLCy3ufJ14UbsWL0WHF6uQ0JCk7tmeJppK2lTHdTgGDJLX7zNSKT70PbMniOyhCK2WJtmkCTxa9sqKTdfKSLZp2UuZhAJGM1Gqh-Ienci9hpA9ewRET-OZ7IV9jRQjBgb1up-PBoyoXWAcrNPR3vmJaSF5h57dZgAzEDSGHMQ7o_t7Mk7yZScpjjUdGhVN1m-SO_OzttSjYSeSzhbH7nL9Te-SmOQMvn0crZKm4hQEfy025ii2bfdnpCGfrjAZi3clwzi2wRWPSMzjDLbrByJjdRVL6fldAJDzWmKoGvuxBVeE41KY1hmzfQBdaL3rUoDJjkQCN8gYKXZqoJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc7PA2lieq_KzrUXJagHruFXmmyYCYbt7G3oqE5_sremNXA9sSzc08csZ2eA4EG3-dlqNAxdvsGn_fHRfQQ0xp3P1Ruot0DTnQTARjvhNZBPh9TVf6D7wfVAasrNzhywrQaMJpU9-dhgjeNd9orF74EzUI0iRFrLVjuKD1r1W0BcnW6ilSLTGbsACc4biLxUtMjJTRW4ad6GGQ65MrpPmG9tqUV6fz0qPtwTTnpb_a3HyvvgytjJUnrAQrjMnCb8D_AGHHMl1cOahP1KUmak3hVktM8P_yG9TDqr_B_rTu269YAr9Rj3FcQndfoazkd9Hegb3AwRXNJ5Qm4JgnnlPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnuBJm3kpfh0EP8iSYYbdTTtHK1JxnwdP0gm1XGB5IVkDLjm_CMcpY9zFiKPG-HKX6UjART1ll3eJRelIZtafYRgSFkfjJ8WzpVDClDmwSVUdhWRkNLZR1F1cp--tv-Nvc5jo3sLpn9FBOdY9SN9l6yeSyuXTuwDpn7kCKpQnIklECdEhRQS60nCxGRZkW5GoiSXoi5_5NYh7m4mGNAwllKJ9lVm2EecHD1Qcn_iWAfKqZnszfm0Gdem_vPbnsETPykwsAO5aqLQjFxaVj-vJ4pwZHg7cAkr_jRItV3eBcqybJd5nyA0co4Ieh6-_TwvyTZ-VUHEQVeZHtcJ91jV_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPe7C5JzaqK5z_hEgUGZMcZ2T6BACZbWm5B-8UMV42UGc3nYLB9NahV8RwjA_1PC0CPxulcpWfdCllGT5fqk9qiLUVgaTU8pASn-IOxDOXUYN-zovaDfTm2nwpl8YjZtoNSTrak75kuYXKmnmqPTo-BkZYJYvP-51oo55j7DzQdeRVhzMzldu6jy5FUZSu0c6owUeeyURus9FA4sqeNdRG4KP4hnbHS-ijmS0NrgvSpkxm2L0ZAh4dtJA9dolthGDjQ7UyBk2Y4yEXH3kLXF9Y-ptnCZ4hDD_3EF5hd3uBa3L-BNRetsOXdrJT71XeGzVT1E7-MiMXmlTnsVIcZuIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLt66VYHe_EG6xdgngSvnqMC2tgA6A8EmLc5wOGUQ5dCw6G0JdT3W4n5e21X_aGK49nFSX6EZr-GqlCTe-B0q5LoWjEihaMfwQivOygwpWAHI7Y35TEM4nrcBnTCISxV8GOBjcsLHU1Ets_wajt9O0VjhWvs6AJVPAYE45Gs2Gi7Gm7fyMRgMB4l8CfC5ovavyFXTKX79ZmPunoMf4cw8V7f9FBgPEIzHNXsI6eHMuYeiDs3YJCfuFqs_ahZWCsdWVNJTTeVdJRluN9WbB0u41PAf0oIFh3D1dMbEAhdyxyaalHOtWYIdtItioSLEcc9-F8ixM4E4suafvp_D5USsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAXJt8tSshDQl1mAZ5LkNjMixGJyBiJc1cpWslTPnRB-5pIVboVCKlxyIk2zCRc3sBtxCj6dAYmtM2ehf0u4zt3yM_yXmEuHU1n1Hm4mzVKdBlgDDFrBzz7yNNlqmwtw2VUgrECvelbTEsRZ10efibPgVkEQIyyQltrQVFfcmJka7ucQkwgsGUSkdPHvphy8s37iDclx21FxW2K0q8mJUhadcqkBe3HysxnDgVmMwmkPhp2LMj63mQ3hyiKvHW8uSBg0Rx_DhbyyaHHmpo5YRNPH7vaEgC1dcWKqThtE_yWSNd8lqUOXvRoCBnmkDOowlinHJDfKG5MvQUUwO3fM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOXgxAZVnWoEHfxnhPXas9CNw5TRTsjPItxSQLRVk3qO8ma7Qi_cKeIIza6UTDCyqYr3mnUUxjKb-SL5xBS1l8k3rbsucKt1k0b_cf26XXt4jGTuxvgDZJL-5w5S0QA65JEA5H0qbhwgrAyTWzP5NEDVixaGm9eeYnO5sJ6pzr61YEYblWIVG8bBBtaHzuJyCim5JDbFedNuYNpQet0pdyXIveQp6UrIub2mx-dPJmjkr_5NXGJHFXOrdDWG8hX0zKGHGsidL9URKBiTLfdl4pzI2FWqgFMBAK5SV30kkcvmuq49MHohvRuMcshkN-JeCxRI7GowfDu1nzHlCGF8hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2I7Ri8fptkJ7nDDsZhe8ccNBkbWoyoTvznolUaS_GOopRTyDMn1h4OnywOO7Lm1YA2Ykg1iMC4PlSiv0Qfbw9lnQAK2tTGzMX3kD6C7TAsgpsx1gPYJ6fAM1gzwoD2LZAsqkB7aAOMj7MiSBky9hLV7ygGCBna_vhAdARVJNkuNCWrnsuHfdGvdrL8oYZIF_UbNgKmJffq0VYCw6JvxmzcVI7oEeLDNtvlq8lWrLTZA8yMCzQn_WPq6AvRZ8uGrIwwa7g3GI6yvQ78BUzQutzrbs_YrWXqUaac8E3DeG7ncShvzQBCF57SxrY9gzPlBsvawQS4Z1Deo1j9Xm7H10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhV7mh8vBAhsidAi9DE6mJjLx4f4UrCgr0iX_YSU7Cq9alPwA76Ie6judRzkBC8iqxbBed408dHuGU6Q10QPWJ9BbFhG6cLU0ViPLtaXhlpqgdd6IpksqznRDjFUHLWrkPqfuXqMIlLzN43TtUN5fqr81qpOMjjBpo5f3CxHkA3Myggb2onU5nDhaVoh8C_gJjIQrHHG6xDj73tk0tpl1PqWnMyuZjFak0b33kDExXoFKAxbj4A9pceLtX7F3eM2mti4XOXp8zJnNB1sP8EsYd8OIfBwHGCVUVBdZeWX3bmrGvA7bgmOD7W_TmPxucz8rqQs3XYyZXrRBqSugBiJUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxpVP4kdA6ThwOgkpwdfpvBF3EWz1nD13r27XDKE00ri1ifIvCLVy0LsLYXS-ZL7QntN5Dkve330yOXq8NYFBVUitVLDAUYAvMiy4gQINVpNeS-6OM_1ENmsbxoU_WN5I2lQqCMVNXmlyMOAzas9xIs7xS3SxXBhwu1XX2FDB5ClxdjHgn7COX4GP4LqthrtmW6vZbCcBQCGM-lD9BsS8dVLNGJmF9vXKMf1172k3DvA_UrydjuEuQKq8EQkgER-XIrouaaipmlcqxaynV7EUXsqWyGR7P2m7dRiLiIK-GVPSlQzHwpHWsVQYLAxt0_7FXhljT9C2wXopR5gEiiyMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIoWOiGvFI3AcRiI7ZeZVelVJ6vE0QTJOsGJkb8HJ83hIS0fBpeNRKy65Hi95piPtZ9bTFn4S9UrvpZMwUhErz4ygGtm7Hx-vi4uTYdz0NG7prQ7ev5hAw-J6f6OO6iScAJQW2gnUeGU1gpNmuScdca_kgqZ6zMpGDbrWOlW90xbYrZTPPWAEVVaO1PXDv76tP8OPEtt1NF9_fBsuRGIbJW7nzpMHEXN8BXoKJyI1Q41dqv2C4ux7plmmRi70aBzSYjxukHTIEih5C0c9PEt0wzSmx-kEsyeUDyVCz04gVk1kVutYFDutd0W_1nxNkhMlPQ6Jns4KJHZ92h0gi_IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gsws6VNGRlrmqRYR98U7baqq4utPFImfak9PV1d403HiB8DnHQi3QDSvmwwW6b5lSuWCRpLBgyP3gD1qti5M8d8r_myjTMCJa7QKVZCq8bI_MWnrLR7iur5cntxZai-syWBGcZiUg3ECdzBFOCaIQ7oK8p1EOoAqblhcX5Smmc_dVNVFmLBj0cMspdd2jJV_qSG7nXbsuI0drPULg25gNmyTXIV_MVxmyMwksKVgt0NbET95c_n060YkN4qU9R4gyTUyElc67etw5ZIUaa6DNsvmSZYpeuOWocbUGlWXcBLrHmQSI-oR9Y2Vh-617jbQb9KZrHxc9XYdGTEH2GYnUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFsDVt2sWRbhQRFGdAP3exdskvR53ZICqprAU2J0oo-ddB_214HDbdmawmqur9liBxh6XxE3xSMFa-4iVfXaH-yAmc6-96_eZW_Nh3LSSvenuTzR74VZltx5W2dE-0nUYsg8_UKf5xJRCd1coj4zUse7R06IUOVLN3Q-XpMewz4QGdsfA9z0uTqybi1bESmk7Rd4T_AeUDR7Nivwxo6WlxD9PimNMkLN9G9r4dmUbiEMb17bBPkFURz9fjYQ0Z3zcvsG4vWKll9BHGsanEilO3k2tNRVWDvAv322Xv8dBr1euPHOZ6XKF8bc2p3V5rFiwmePniNtiRAzbbxUSV1IHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ976xYDMbdqusM23iCxKxmhTjdt5EYoIrdp4DvUrwfGaBrvjNhdq0M6yse3528JyFrvBku_G68fBBKt88pm0TtaqKbKYoECT3DXps-92t84Vmcnus3meTZHrc72yd5fu4lm4O1AVPOajAM6VbqZhg2IPfBoCAifw5SPvekhtJ8uv50WTQ8onAEN5V4eYRCuIpubZxUfeJEI79qdE7_wIwKbHpvFeJoYZ5LRmfGwawqdMYouzZBgePTtcyCHLNRUTpfGuqsiNSxctO3XK4BVEimui9Cgwu2FLRmCUzXy8Jx88HOEtE5hAaGjLlyoSY35fsNU_hSpeoiQd6ZOrlADtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcuY1tZfVdOycxUp5V1-BCKc7cSftq-2NQUwM_s1Ut8iONFFkHu9hvZ2ir3zqku1wOSdSNsZrt02ryOlOCjxhq7sZ1TvKXQRPRkFxma2kaV_lKOkJX0fRJd9m99tD5D9yEX8u7SuvZ2SBpLd-x9rQ4DOovIR32XZeMufHWuuazZ8NyEF9naJWXetnqZua66PBgS6D50XiqMdcHW9LaLNACuTsfQZzpoRzn3ZA3pu3WjSFkMUvHSNzV4Kk47Gd5iwrfZ0uC_xpwOGPayLt6WfXqpjMQaDxm4TTGO3ENmR8KTt3id47VcjODKEkDMZFZptL5M3PeDrgalKgy5-3b5ssg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVsEn8TPqa8EHANRVeENGhTe0aFYUWL94FA2gCx3dd9x92Z2HVZ7QLhBv59paW_Rf7PQ1lUSSEAyUyNkMeY8bI4hV7DczlmXOGnAzO8X2J0OF1q7BF_ks3xITY_N6ialQF5vFI4vlNKMVu-LlOZftqYezpg4G5wR80KCc7B0HkDode0HnrSqTXHM3Kwj9Qix9hRT3gcO1HLDQdWCoO4vxgChqV_nsJ8iMdcBLLe-KmCpuerhLFvcSFeYB6LAOay7BLAcu2VNSZoMy3FNnBhrkHdn3E7aB0qfw_6Yw0rtOqM3vUykITyuU5FOE5k5JmblMkwp_PW3SDbcuxic98Ni_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUJafuBnKvySant2w_YzLxOkHXSGkDQY7V2gEqAhDISyPSfA_sOh7N52LSicZhQs6HuhL1iVJxVoTq1Bi_hiv56PkUOVvaUgjz8YtRgeexTWtxWJvZ4Nddcsl-rTM_klERAGRwEtTMWQ8iEmFI-utjRWwD0CENgRPxd8M0ibYwmqV4kTf81ZeMmqkWsuiNBFm5aRo9y_CuCKc8SpjLIWnnbFrN16KJavaa0UOIFTUTpMoD_fWILTpDj5-jiCi6cl3qg1xYTMk4-WkDD_NtrjhYEuZ6VJTFmM09r0alYZfP2n0_DkOF4pmRZTeDUZKWBf5TcR21JP0DbV9_7DcS9mPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnEYGwhfC9BWTc_5eEzy6grXcHmdU74jdFmDtmtirlvwT92FfuxQfr9oTxm3-lH8iRnIA0X84Gsx-Udhpq_8xqbrMQo_yGR8xtEcSfFoygzOmZOcQkzg1V4Wwcwe1WXbLQESoeVxAoOmj_e7jfBnI7IkCkpZbv2xDoRtSA3x3MpF1TV0S16uwWJo0soQqkJrllLBT93lVXAMQHl_BYxvqXkz0RwrZWAeOR75r9r1rZW0lyVziXbX50QYcYdOHYWQR5kOWHtILIr4py0QhUs-bbWJM2W4SMrVLXuiauTWGR6JeWMcn9oekdvbR6A7FYa-Ay2ffQlHX-LpEGRNXYt39Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RknNJ1lkwznhMEz-xMECJPXM8jmjmIfQk827dQP_dILP1wTw-f7K8wCtTUbOV-yfy0cWbaKitWqknxIfcrfNOCA3DE3PVIJOcaQqF_XktCZG8pxCqFdlO3nk1xZ1d2FiSWqXCGvJqm9hnc4jHzo5vA8jRm5D00f7q0cH5bdOSTrw-AIL4pGKBxL8oxu5q4_enrVWuTr-WBE070qlATKU8FruwkXY2pEnD9KgdMCS8FPNpiA3NDiD6qPWuGcN63c2CEMnEgWRVSYLIdszRQTAQZ4mMhNRV045L3vuyCt-E3fNMPgr531fcG3G5v7WzgZQTIAtOSs6-WOp323NOhunYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlNG4xNNCUHerrPSQSujor-47WNMuHnb5sMZVFIIdPTeW8ikOLDuSJsV-qV7-iWUhBdwlbcknfW_9yPLyc7jIMJjlpuBlENirzuhah-INLVD7IB-3qOURKCDtnBUGmPG8tYquk3e65Qt3_pmMNb99y_HLcxLicHisJW6e-IDZvf4zHKTdRxeDHWwugSqCzsP7-TdnD8f0G4hQT92_y12qK0fk9LmxS_7yX1Vtp34BRHbzfOYDc6-kjMrNSR4pxz45YahhTEVtBDB9kaFaLpBa1yiDuAj5hIO5I3yIEHj2N6h4K5Rs1LBn45AnicpXO0jfQCdEYSPeZnsX2RjmdDJfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhCETjWUZkj5KFKYDpgjW1Zhj-9WptH3wRr6cCbbLqZCEN1zgmkf_o7oUIrZ_09Te9Wh951oVjiJZ66gPhvg1-5jcKvaNtUjrWRGpiWlwaW5y-lcjDXdr7wYFogmeMW3PE7pbSoEqttbVSFAAcYgJOplB-PJFjNoXBoW_xJWvWB5_QIoSyv5PNMUMEN5WsbqK6R2iFkgDL28qxlouTJbvku3pBjiNFqA6pnqkVlQq9Z0O0n8TDxgpkNxxFh6CiKMQspYNJCrf5hpNxnge3of_wGqPIDXx8b5TM_xXsPAgHbZRBIIqiUIh7nYDbzTprDAsL11OcJviKfWbTGQznH2bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=LDfiM9mbgTLWERS62YyT0Ar-dmn9rBk1ro5SkXE2IOivSX3ldiFfnm57tlx7WmnBtWr8y_hfO2ROOzJpqhO7wWc5dutlZY0_-ReCqalEmohK8vQ1iB1p0SnLYHiKGLsViC_nDRSTu-cbxCviBqsY552CKnKo5UsE9KiJcGl4Vy06LuXmvTOiPVL_Lkml-IbV21rVr_loXoKs9Vi1UoXx3NJkZeACQ33tVn2hNVAN7R6u9RZMsIoaTaNULHle7Jx5azN_D4nFCBOL08HblCCEggAcEwPHntN56BAD1GQaibqf55_18hGSSUu8BYeO_3vFsupJe6l5nJOuN08cLkSTHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=LDfiM9mbgTLWERS62YyT0Ar-dmn9rBk1ro5SkXE2IOivSX3ldiFfnm57tlx7WmnBtWr8y_hfO2ROOzJpqhO7wWc5dutlZY0_-ReCqalEmohK8vQ1iB1p0SnLYHiKGLsViC_nDRSTu-cbxCviBqsY552CKnKo5UsE9KiJcGl4Vy06LuXmvTOiPVL_Lkml-IbV21rVr_loXoKs9Vi1UoXx3NJkZeACQ33tVn2hNVAN7R6u9RZMsIoaTaNULHle7Jx5azN_D4nFCBOL08HblCCEggAcEwPHntN56BAD1GQaibqf55_18hGSSUu8BYeO_3vFsupJe6l5nJOuN08cLkSTHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4ZkFp3jWdeUCn6tmorSmyrzQXuDT3rDxh5CfQP8L1uuj-4glog5trEFRvZDLIJQer7pS1P2SCPCXGtKfuNvTbeWHTJZRRnYSyQujYRUG7MkaYozU-4g0K0qZRH9Ud__WD7wOUP1hJ2JAHpj7IgSGA4dGmN_NT7vYvw-l0BPAMWb7buEtVcUri-JEGhxesDuLCacK_MzIqXOCLsr1uqzfFjQ7RDaLCBqmptPL9I5q_aRwFqRPXhLaySQVmcQVkmy-sxJUG0c81ZPUE8pC2naHmGYDEBT-i2b_7T4bm18n60lx37Wj45laTC8SuMtx-MTriTYV3aR98ujwObbLuJAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTuL5GuQ6WFoMC2EaLx5beTWr_qmkFIMWLstuKZ5jUgdMJPMf8UneOiAS6K6T7lOE528nWnuX75MedZiu9LPysgHAdry8AtWYQ0c-34HK4zYPw3owH7Ob6m9Fuud2WT7Tk_NeXOSBfB7zzmXv68wVo1lpoOvwR9xej33VMd2OWKKBw8LwLIu8tW-MfR3T3Wl-O2zXojkn93UBJbKJxIW3wsfmZ1L7InZLFTnfqOEMp0rAI9EgLu_aHceaIasPZTzSYRtVmR1J6UtsEZAT0syM9C6OMduTwRZvS0Hf1-mHyHDgwNqY0WGjf-x7aw_QQ9iYVXEQwcRJyo-VigwnTt9Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGgJLeBuDjLvNe-JtS3WArf_ud6hCbfGjPrI_dak6T5Tc7TFkRYz7HywL39rTRdIdpU1BmWhB9gkU3FhSmujN_u55ne7AMdvu8f1O2Ssqn8a0Z1CB9gMDrVX3lo9n4nzjZaxa8nQoWKo8IjKyYAcKgXirwcyHDHv9zIPzRQAICwmqGfjop-PqselOjzBPO7A6HKK2Z6sbEPat9f-7zWzo8sq9MI6gxEDVFd68z3q1A-Hn1Z560rTo3r2LP0tXBWhmOtCAENnBkRWZ972GLq9yN2K1oDGPzA3QOaF8vDEw1ZdFq22d_W6dWk4bnZpuPFpgXAgwZWq_s4VymfiZTaWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0XlVhfuKDcdc0SLBoHXU3qOheEg_YJYk9cgpYPnfVnn4fobpXoFaiar7VE9Fwkn4vHn5b15Yu4Mm0I0claimSlfeaqZEfbi4r00IJxsFoiDpZGJxGF8xetWLENyb1CSI16ZMYB9tovob9VB6c1_bjR3yovx9rOLETjYjYMD3g4hYWy8a-AwbPa3Ypj80q9HIMNqY0O-Ge9RJKjWkXHrAnZRDU2MZktmOvcZ60Y639mLo0QBcVFTepQqzKcKNm5Of-38hH_lSLkIIy9vZg4TY63ubJIADgrVMVvHigZdrjcFCZ7Ymx_E40F1GnO6wuXY1UomTdXA7e99NSZ1PB_TjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYDcL89oaVrNc9xKpI0UfLIOCXZ8niw920AzXQkt8_Ykaw65Hhk02D2Vu_M3DfrbTYvBVqqihlsOQkfvjL5uPALZ1ZHlU-MYUmetyjVywSbqjKbxErFzYOKkpFBJRR--EpneGUBA9uYOaIh6RmC5nwVQCb3OMG7DhHXclkjmN9IdUYglpA3tl1tbeDq4jmtL0I4SWA1Dfx7PIiAnh7t_wAZP1w-3g15qzRuQKR276jlS0FdXn47ua-vTxl2NAcjUKeemS_Zrp6gEAgyoAIL3-UEoArnqozGc8UmGrKO7VIvZpURCJ-m34bo1SveSRdB91UVfP5M3p2qVrOaPlCu-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THOtJ7fc1224us7jb4UemuYtpB7j-aZX_40Z7i5pql9iOC2K_vrAFUQGAUxttBkX3WorMQoNivqtPurZi7Q42LvN5xMQ4EPXUDSAa-H44k5Ny1kNOlh2ZClbd1hSYcb-La4764DdW7P8B5ltxFLK88ovMWFRO9yeSQPMfQlY8SUKqFATfWtmAuoJAbhGI7-ldQRkwqPeESsDMSjFaUXswxNwNFJvHkP9Na6ll4ewmnCexftiwECqdxP8eYg1YK1tY6aEOblDi93xJP0ynCqhDR-bfH9Me0VYZ-SEaFF0JfKIsVHE-9JwHvhhlsERjg_FlRmqODzvJ2LfPpdbqfbIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAypk_1tl3XSxNqT2NAKLns9rtGGka6cj_vzJkObCtRqIVSTksGZpDNRQlP1WCwWlTicl3xIYuMZgL7uXOLLzJYGA9pKN8jdpiqM0L4CDC98GRWcSlNMHd6a0fW-1vzoIt4tvKHp45V9MrtTgBAdIMwIijP1UvmaqDpMLlqinawcdFy5ZKSxiH1mbjerVdVP-eUVdhi7MM6BpyPvmuFbJvSEFFLG7w356oUFx8HLVZL0InvLDgslWZnL076RB-LZT8viw1z3ST0L-pvr8rkCp3ZHxolVtwveyA3-w4xhieAb6FMDUrOqqwjeyvADp6NYRlXZlZh9YgU3CZ_0muP3NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TdReSDJiDkqUcHYI1U8OGsjZZ6zqVmUJgmCmNlhkGDZACexYEmNq_5vBQ_rBxlnyXu9hMSd2CnYvuz4qQjdq1ucX5oDH4Tu8toSkerqC7X_xnWHicmQvyl6DsvuiVOsGlq06BIs--FUMLPF78emiWhHHZTyWHJv58BfTDV-adO2F0yjqlIT-6v17RXGwe6RVJRrlNF72gIcpCXhQWLHWEaxJTLqk0O2C-JISCTmMP716YR2gCGuicSA0qdMDdk5CGiag7FhjTZ7cEFykAcgGRTVVLDe7VUAeleVCMdmRmnTuPJSd3bPyrz5dfbNhpiD3zPI3gy8UVKRign904pSjORrlhmeqpR4t1RXBchQ0seP4UPkrWXB1_sEDqlrJTmz5u21vjYnH1iooak7Rx4Rf77ffFlLCyDu8Y_jU2L6XrhD5bMYfv1Rol5Ozf8Lq3t1ODgdPwjIihBXaINf9z3VXAF0I7iQbZoHHHwaQ4yPzFWc1Xwgwn2UK5_vO-hwF0Q7bgOFmREgW_r3l2YXqt0Pz0P373Zeoi_7jQ0qp3k1TEpv5NF-jF1GT_2KTTh_-hhOoQmb8r2AXpC7tIzOR8RJbfPfHO6pAP585pAev5KiWVXdLrC57lDNOD4JlCD3F-fWrIxQwP13hDUQgG6ehs7WdBRbgdGJ5OB3npJrve3ufUYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=TdReSDJiDkqUcHYI1U8OGsjZZ6zqVmUJgmCmNlhkGDZACexYEmNq_5vBQ_rBxlnyXu9hMSd2CnYvuz4qQjdq1ucX5oDH4Tu8toSkerqC7X_xnWHicmQvyl6DsvuiVOsGlq06BIs--FUMLPF78emiWhHHZTyWHJv58BfTDV-adO2F0yjqlIT-6v17RXGwe6RVJRrlNF72gIcpCXhQWLHWEaxJTLqk0O2C-JISCTmMP716YR2gCGuicSA0qdMDdk5CGiag7FhjTZ7cEFykAcgGRTVVLDe7VUAeleVCMdmRmnTuPJSd3bPyrz5dfbNhpiD3zPI3gy8UVKRign904pSjORrlhmeqpR4t1RXBchQ0seP4UPkrWXB1_sEDqlrJTmz5u21vjYnH1iooak7Rx4Rf77ffFlLCyDu8Y_jU2L6XrhD5bMYfv1Rol5Ozf8Lq3t1ODgdPwjIihBXaINf9z3VXAF0I7iQbZoHHHwaQ4yPzFWc1Xwgwn2UK5_vO-hwF0Q7bgOFmREgW_r3l2YXqt0Pz0P373Zeoi_7jQ0qp3k1TEpv5NF-jF1GT_2KTTh_-hhOoQmb8r2AXpC7tIzOR8RJbfPfHO6pAP585pAev5KiWVXdLrC57lDNOD4JlCD3F-fWrIxQwP13hDUQgG6ehs7WdBRbgdGJ5OB3npJrve3ufUYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryvJk4T2OvqXcRNDc-f5CHJHT7gu-pHxjqQ2CR7ECn45Y2BMXTCtNywHrEeCPLYMDs91WkdEGXqE5YkaLCu5yJtgPK0W-tpbKfHRDMRrYRQSGX17rml4bpdyvGoOzV_1AyBd2KiO3Bb1KL5VD6LdQMvDCF3JE0Ftnlr3MwJ6swbM75xOjlEdQLLnQTmXNN6s3uG5JM_7fDrNEOjcC8xIgvZbBXslNrEH8OHo1JFuux2BY_hEDSA8dFNpYS-X_ajgqDFqJ-9qJ78YmFArya1jHtq1K_WsIAzDXTS1rOWn3KtqE-bjhSZesxeGFuBKNsgqfXQJp1tSWj_8ibhY_uUDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjXReFl-ZZq2nGZG177x978lvkunGwuz9Lq5Pgk72scaynMGBo1jFOqRIZ8IHZ2mCy6vXwGdoIDkbRZX2BUje1e_qD6JstRmTRDg0XTMLFazgcPs5DabSepkPt4pTNgvOXDtfRFSIA-yuT7DEYL4kUsQ72gnvh2G0Oifo4FvyLU0TY1H6Vf4MIc0CrF2sYbdN_irH1Q-4ZC_9DfAcBKCTCs7Zvc0TxjespbKkftND66-sjoqy7B0i0WTIiSrFFBS4UTmguS7ZIBGz73akBQg_GBAiMIzbPszVwLHnkWXGd8JxhR_UsbTWIkFLmkqfi-HaxETrL5qphpXHZKxsDvwJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1CLw4ilmqZce2-QP-vwV57J0XDncz0B69Hto6u6zDzNfH_m67RWIM9P65N11_ZGvOHmVDwFgc9JbzWM21vNTrYiS6Cu7xH1Y3Lz--IRLIAwtIOLP90zPtNm_q-t-NXmCc6_R_xSbXoZ0UJ0v0vRFCiXQgWqZKD8Zr6C2Ru_h8x2fIXXW8GZY7PftrnqGeexS9Q1x1X6FMlngeXhEsf4HPYWLuY4B12pxsLB2j-7xBafVYW1HMGpB53Nf8QsjOvcABJTZBnGA97Ua-k3K5C9EXW3gN4u5GbDDvmA4MMGrfjkHZdM_ZK0P_6prUOJYE9HCDy5gGlErbfXKdoxa8Q1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehPcJvWi8L_OQMr52PvKN4jQsvXLZ2Mh9IB1Lh1VRV85YxZjeWKOya4c6_xxf1-ar1qhS-If33XYN-v12EFZ_9tZuW_d8wUWSJzlHXJ4AF6z70PzE1SHs1dDQUOH6i6zSI4QsWHP6ayzATM_l7UhQ2FBSgh1NGXoNNzvXB7_3Dc2aB6J55a6rjzS6BdkpxUoWn9h6H4GTxH_jixjrqpwDeqkCkDHeib6XkROdFulkgcoxfndJRFbdPEdNEQXfSp24fn-qF3WDNA7UyYTd4MowOyzLYepFcH7nnMWDXG8vhys94rDCBID6CY6mGYHe0QPpid-0aoIjiomL6Zxo45syw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxPqrY617ku0XtanZQEG6bctRjLx_6pRScvcDXpjTGiez5oaTUnkyyoTGyEU62eE2DTJtsMCh4T1E1FjwjYXCPWb4wn1gZbXWjlt0Fvbp_nL0EGvKeMvz4OS7CTdOf5pZUQLH6kNz_O5oyMZme9tNXcXQNs2s7rey7ofM2UbtZdNxpcuR3QK-ecFDyflxZ7nPIitLh_jS5aJDLgQSvxj7p2WRU-Z34ZHhH8AApe9j12yQA7aBe54dniqEF1Ln-wKcR3ARAh-dYNtKohBe0tbGVniex7IDO7pw88AoStZcJaX5HnLzZd1o97otBHam_MFFrOLnotPemgXS4P-lvq-xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aS8kZL4CGl_6Q4nUdLjAO9lgIfuTL9EUfoG9hSHmJLMjinJobZySZJmDyCjh9zZv9dCIbITmkNmEel_cMHK73iDF-3eyURePAaVQelKtwI1OYWIUvV9ZBWBAR5GkADhNoc1_e57c43yMmLvdAb-fiVkDKBWNR9XPhMiWhRyw9uCIfPztWs-I60nvuGjzSsFs9Akdc-i605U6I76Dj5mBgaeherzGXtcGjfnkqZfWFh5Z97UlotPQVjwM75BMRqFX1KfPMSjRUEI_Di2Jm5Uy8HWY8WQ5Fq4vTFjLfz4G3b6l6KT2V_AO7z06gPQpnY8_Yv6ekmxvjjttdJIQLIE5q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0aS8kZL4CGl_6Q4nUdLjAO9lgIfuTL9EUfoG9hSHmJLMjinJobZySZJmDyCjh9zZv9dCIbITmkNmEel_cMHK73iDF-3eyURePAaVQelKtwI1OYWIUvV9ZBWBAR5GkADhNoc1_e57c43yMmLvdAb-fiVkDKBWNR9XPhMiWhRyw9uCIfPztWs-I60nvuGjzSsFs9Akdc-i605U6I76Dj5mBgaeherzGXtcGjfnkqZfWFh5Z97UlotPQVjwM75BMRqFX1KfPMSjRUEI_Di2Jm5Uy8HWY8WQ5Fq4vTFjLfz4G3b6l6KT2V_AO7z06gPQpnY8_Yv6ekmxvjjttdJIQLIE5q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3L4QLJOynJHBWLD1zGbFAAM0mV8DhwxYM94ESOPuGueSMyFpxGVw_VmjocG-sFS0_Ekxnbn0htu0h8fKTqa6eYMCD3QAhonnK8BZ4Q5Bq8gKPpGzS4J4KD9WjBU8g9xSrvYR4js_cYaGr6n3cBBqsjKJMcLfdUSmTcTrOOJckKqMaX7fgcgdsH5ogaJsbgWRqBUWefOyXzYGc2YSGLVHwEU9aD1nm3bevNbjizdFe_SekJQj1bGpKRIhBuW_KTsRnz1i7HLD-rHQmSI0v1K5u29f6uATeDFibtCLkxtJvPQHnfz7Ce4AL3SEy_BRi39rB-Q1h9R5KMT0HIgmuvd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFTek0SJv-YvYCRRBPQ4vIuOteyYQtBSF0r4PQ44aDAf6VjgwHcqGq72QvH44fo7ngqN_JImSXxFKF5-6SveG35MRKjmnyFb5_u6UFDPH-pGE71fKHjHvk1dBmMFMkpH5hf4MBAqtC3woXTPYSEWHcaJXe3muhYUZnl6ymcyvMAU50rTtoOhLgbDgoiYsNp04sZwLFfucLIw88bHQADXoNRuCsYUnCMLSvFQrRnYZLRRKW24o44VclbinrrLnNp_L4QfHPhLMQVfU6q-CtOmaui5bSHAQRZU5WAHSsodE8MdIletn2jlXtT-ZN6qio_rwB6tWY16PTBdYDE4Km01Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jn3TS9qNrG5T6HveUVEGFOla0RsQ0aPVZQyDb4N4MHpysdOArCdgw9dEZo95zeNfK3tFN3kLjqxJc7aylu-DOb0sUO1i7lhsfTpFJkbejRQOGHwl8yhNtfsavWj9omsbNW8qYa98h6IkyPAUNNwffQKBQer1drOOA6x912TNIHDU-3KNXAaalb6ouQ4kLjEYFQVqIUwpRFREHhziersXs1vcZKcdVEXhzW2ghxno3Z1iteqpOFRKkitnHYyqsLmXsiBRN-yDSiZtwpD4uEJCXIHqZ4VREKkDABNJdbSqul_XIuKgkM7jMo-RK4Scglo0fovkgcYzeD-mIdzBdZ316A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VERjlVbNIeQ9PLhsXZtPdCXhruAK-jmEkLEvdW0COxI3m1h4mJAb98OhZkRGKqRrxhNOCgmru9Xr1RtR3Szw_Q1T5fv53cNWwPkSl66ZdBriMYw3J3a11qhcpRVXWyERU_Xm1y7BzZJD7-Ro8EJ3S-t4mwNkuuGQr2oe9ynU0w9hK4MnpOoj-wHtB5u4MRxAjFvzVuXZ9OzIsFJwZ1jGeFU85vBlP5cwOw73nh-5FBj-9UKbGdOPo79E6Q5lOacWDcQjCDnCYb0Y9jyH6pZlmZZo9p8TaOizbF-16jHstB5O3-MuHvM4SW4ZCeBKYKkNJWSis3MqZRNisu7JV2VlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ha7b3eXIh4AshNThm2Y7JUG0Xa7zBQGAETt0TD1sMRbvmUWMniJGwBgLU5Rrio3NAWUnXTDOVNmGa8JEMIcZ-EEFVzJuat2DS-KkcIARq8SGUz0radh3B5lXEUydbc_KdKUd-UCWhFbDMxH7-WHlAyptGKzL_RwsBwqPQchFeScbkAkuiGDPjuDdO6PlhsrhqegP_e2MG-_7k21bczPmCWsSQRbSZ4w5c9ZPcTP4qkAVhvJGsG3crDSjjhlGunz-EWksakld_pZ879_SfjMM-pHQsdPNfK5d0P4dRAUDiPdszQ4rqq27dHvqjPTYaUHljAcjAv1RdKs_cnxliCcgfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSmpidYcxbfs27OTe0nRp29PuMJAKanA5HXnUh6XV2mJm0HbSKgcO8XQj5YE-x36bH-z-PMLs6DweLLhL-wzj0s3HMEzjuRcJld4IIzlkROfv4SyDIA_uoMlHmwmKfiDnL1D5VQ2JKfwfaisdWcvhy6tRkaylPGCoE7X1QMzje-tOwlzzTWLXMmA0ZvO-fzF4GUyk-3OUvBd2XYNj5aFsZ05Y1wZBwHw4Z8uuKitZtnbqNI6RDCemcVb4kiORSOXulwQ4Xw2rvn5Z1Txkq0xUbEFGX2q_Uv2KlL7MwL-Orgh9yd8GZJxkOv8QDOANOp78_XSzkLQycLjmHLULX-MSQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
