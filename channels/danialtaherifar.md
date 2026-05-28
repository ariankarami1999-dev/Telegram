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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 259 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 353 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwm99Lz0df7MVzciC5iGxYFGjiEeO2x6Kui7hdxMFVObBrlbQKwtwuBYrw8DvaJR4ixobv9XSFJC8DNIcFVhvC7zDomiK3g5ytVSKmD7t3oe5My3CbCqldctkwJ2eukfR0H0PXtPYs7Qm6_ODNf5wZvOYOgwMTjU3NwbC3HJ54HWykV_oSl0yWQw06Ll5bvd_jvcdqegEO4EmL-IEmQsLGnYDheNvWvuewGJ41Q4mr-BQCNceDdApvkxXfnFLzZui7ju7mCPUucWt5OCyPv1_dz1WGNDqdVKW1JP6qpf-jhEyjvNshcjCxZpkkB-G64ito5h27g8_mpyUvvi6gIEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 447 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8-yMnvxOb9-mEox2-2xcnzEXUD04poF71E8IWJdh3b_pv6AcoObdcEVNSLh1Af_L1V5PBWHTmrESrfpE4BIgcq7CPclR7gGB6FN35JDlyi_hl3Iks2x0BMg4U3UW8kWWJPisxCL6qX369mPi6ipdIE6yTfJCoko8iQGc02nbeMLLs7tpknWjaB6rPy5OmbOuiBGh1AL19H1HTpweawjkpxDuW1PdkeBENRA0AvvTP6NNUnO5sini7lhI7UGZOtIVHY_Zh6YoTcV3JRfBqLG8gnP2DuNZ-nWKd2cnU_zb9fMI-shEVAz8bncqvXMHfa6gz1l2dj92eyloaLa5tjvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 705 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 801 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/volov1B-VXzxURzm0OL5DXuaXBqXREavRtskad-_mbPzMgsW9_w60q8nCe5YZiR4h9iemPbUkjNwt3JECc8vlWJvnauYpPt6dz366cDuS0YSVRBnj7Z4zaz-ta4oMAW_GFNOPgpmXs_wAg4InvYiPaue7pkXRd5d8FQM7Q8MRqVivou-2F8D3FUrZo_-OwRrJqB_xDU5kXdJdbwnfOIEBK7JdLucC69znrm-uM4xYtJ_S9y06cmMQybGoJvs4p8ESZA67d4BqDo9LFRK1rCrcDO62s3s1keF4735YdGVaWimkD5CSFGoJnfkFN2ATR1SqWn1HTnRPtcFVb5RhPzSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzIQoMh-vDzGuCr1HFM6ipzsEFQnR6TlMxJQbnxt9y4dMIbqAyxVLrn8iNabCbeNSknzpNAfEeYLN9JNDKHc63UoYxb5tc5fjEE_AeY800CAvXpvkSyRfz0FjyKvjEYaYYOKbE1wGF8ESbFnhFYobbb2OjHS5h1fDPhzZiEIp28ZuACT0fgnmVDxKRnaT8g3O48lTAp-oXMhGIBkLRvEJ-cZLKmg0VjESkxrnK9ov0FzS18ZXjeKp3vi0qbNmzpGdyhaPCjkUlvE3XQDO_dkomVBk14KO7mkWeS5BaA8cYLz3BBR0mSvBWxKXe-JTjr5DPMTl5GLDOzm9YDFo-IydQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxSc7yw--sWvg3YTvoNz7amNVCM4ce5Ua1BJpPtDPuS-_85jF9zgFYEuj90A5psOn9DXS66VT0fV_Ff-iXjRM91S73zI9L47pcNQdliladHajTh0284Bui3svj8JIPGiuF7abcqZkd7uOtmgc-wyyC2YXC01lfo_cf5bwlxMcFBiZ8BFxA8epD9c6gGJyM6mnHzboCSX1efvhlri7Lco8QttsiHyIhc7zlHn4r2z2JZMXlVAcX9v7atS-DbLug0LVwlJLm3YGdAjNRmq1cKnk_xNpdZez91VCjtkuiXvMhGwb4NSnxiACdAB5ibRIGidt-7UEgMSMhkwr-EsZd3OfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 827 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd-QxiaKonKAeUDeTEdO5p8LJKf7eIc9aKgvpk1hZHb82HbZT7UpSFBM5hLPP9CuWs-ZCMxXsTZzxcSlRx4PcR4K6xCYA-cxM9wVOrY9oUJCHHz_pWv0zZa622nrklV0ZnHA8kaPQKOrzwYu_l_jssHe3fKPdVymcfYNALnXiouDXD0aG-1gO6fEuvPr3CLupp6tLuYmBJxAFQjRT57Zrjh9WSIDk9XsxCc_Iqi67Ei5uz7D63GHlObIAjzFzxRaB_fhp0ZN18dUysBK5GHw1-Ya4g23lI622wC80tlLZZV3o96bWBNcjMmyqYbhd-fOlZy153oltRpBYFfIbbutEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bheZQ8kZEcpvhvvAkrVXizZ0nQu_CccVAFF7sRt4Jh0DykRGxUnRSBu4yISAF155PdHNFNGCS6tTXTCjJD8qPqCZaRGli5Q0dN2LZotk0QBwqVrWj1oB-w4BvYtzAH6GnB2Ffcw0CySTDTcQKUkEL_wGR2RCXVpvMoMtLqQpXoIlZgctJ3GYFAe7DdqBg7ZYxaFBT-D81ABXV5aOaI-qnhEMCffw6fOgdHEO2a29xReU4B4_1LKSI291_DHCT5pmkm8hlFfTo8gI_JHPItmBglEVEprZoii1paYLQxfDue4uqypJ3__un4UimTVDv5WSGCJNrMrYyuC1KT4ZOstTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpFX7f1gO4i9wmZO0hUHH6iX4GJat4IRezhXpYj9w04i5F9rut0eYHaTLRplpn5LavUHX__hBKAER2tta4OCWLxCvWowNzV0I9RWng6PKE-apy2tbmx1mL85lqHNsF6ZrLP70iiax-L6FNkjGS3bsqCDidT3rnN-qNeCqzjFDLdM_66ZLh75vh_kMHpe9joffVr-uF_YrdST4ArXVt0VJA_MPBZOunFnPtPliK-k5fsTEHoXYIT-FSqRtYhZzG9o_LTXa6AiUwQSIhIcoAK_351xud_ZOgUkMnR-UHjVsg5yH7NhF8l6ADuGOmzfeUFwo-fRb7GRTaKDNTWVxsFsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANPm2VfybSeglyAUIwAKSBdR4C0nhNa9L4MsKUqmquViHHwBja33O4CiZoInY_4HNeWyloYRQGDZw0SBvDi292TqBz5gY8MtmVvoUtVg2lC_yYrnJtNlblh6x41jw8HO6mBFPH6zQvNkykTzooqw4dnwGEeXfP866PUDrxwooM_K5DZFipeQEr-4kYwYj1BJgQbIbbDx2_ZA9Kfi7R7OK0uG-z68fe0u1oYZB73RHee1SDBx08k_JDrYWFxzdyi49uyPH-vQm2nq7BGOyJInN7COtc8kp1gt_Vn4LN8PwYMIfPq_3G0Y53WsLR2PPbWqJwheSpvcsbwXjOypKoiVYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEeksjWdYN-5xXwvc9oL6YFom_CkZHc9n3wQsrDX3OpT3DqC4Fkb3IdHFWL4V5E7CQ2fhMLAs86gaC4dC1_J-l5eIt2BgDCma7lnwssH3KkLkE2vVO1wpzFTVS429KO7Zv7e2dPy8GbAYo5ybKe1M9BKnnc2SD6ZoIRnW8xcCPLCkDdsfBnWmn3jzcuVD7pfiGBFKmCJBEeWL3we5m0DDjaKpPtEtNMed9Y_jWSSaoEiELjbWBNyHTtg5YLxFTHNvqFbmMmemv20N78tIbAPGFF6siMdoMnF8NTmRPVhKN9pR5cZV_6CfT7sCSdWf3J1z4V2cR_jUp8w7yalCV8iLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXdGXzbp7IumrhIm04ONyeF_GogPsWTYEJhGyzCALbohmhOgb5mgZtja0-JhV7aON2lmaX1qMbUvdBMyeyQi2ebQQrwOV38y-Pcqd9HN3IJHjZmyqkoeG_YwLpcWMACIUtz1MilclhG1xGKPsAlq_gvp0XkI4WVk4JFeItbSwC8Dnwr7xXKUT_4bmvLuC-ttqgjsAxBs3dSFwyynUJi4lUL_rmxFRwtMbWbmxUlTnNlIq3rt4rQ2q-_d6fWZzFolGxif9uk7Coy3CvNx5v2ABr0EM8QNB_SPgWrgDFX6OAhDXhB0bclC6-Hb2dWpH3xiE1t3PY-viAcQN0_xDjjU6w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=cHqdwRUEGcE4hKKdZB9wV3fmwD8qD2s6abUa0GF1vHYHAI2FqtRou3cVbmtpnbmO9A0lZjgsiKHc8VydubZ_6FpTstD-pigHHfjcm1s1Hk6uU2sAQ1aOGVE0tyDHC6-ctYrrDmUjzmbqdBSWuPZBAVKCesmb_MSmZoRsWagw5T1ir7cMmhtWP8fa_IT3cweS7FoMV8xKQsKTA7IQi5wgZfVkSTdWAS7Vvpg0YzVy4Ow9oCQK_2_aoxvqpVTBREMtzYPBmKGrkUPuTURNNJhAytQTo2g1_66YuajCJhNb-w0zqNLkmw1uV3lYDvjVtavH_6QAgf18amhvU4ks7kEJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=cHqdwRUEGcE4hKKdZB9wV3fmwD8qD2s6abUa0GF1vHYHAI2FqtRou3cVbmtpnbmO9A0lZjgsiKHc8VydubZ_6FpTstD-pigHHfjcm1s1Hk6uU2sAQ1aOGVE0tyDHC6-ctYrrDmUjzmbqdBSWuPZBAVKCesmb_MSmZoRsWagw5T1ir7cMmhtWP8fa_IT3cweS7FoMV8xKQsKTA7IQi5wgZfVkSTdWAS7Vvpg0YzVy4Ow9oCQK_2_aoxvqpVTBREMtzYPBmKGrkUPuTURNNJhAytQTo2g1_66YuajCJhNb-w0zqNLkmw1uV3lYDvjVtavH_6QAgf18amhvU4ks7kEJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKvelbAEWZCg4NoZTD6mNgkGABIpm2oHaeY5TpkuSqoj1M-9Yc22TPsbrVNYG3LfX3E-p0oaKCFqG5onAbJg6bWRkFL0qWPU4S1tnQmLMBMoQ_UGf73qHGvU-K5SrtYEjszuTvjNq5DPQak-PRSP75HS-wePtoZG0G-K4hhzPTplOaZfHbhvbdu3TSJQ2rWMvAT4rUlhr0Q7YcOn8u9n9kMyxXMhyJzdBh0_5FTQGxWKuIgPT_fgzcQ_Npgq_nnbsEr71zxkskt3In9yNYDQ8if5VqNqR06gONHDVdGzFLyX3A9D-vzwN1c4ELOv71FOTxZtUEifiOyEfx4lbxHLhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a60vsMwQvFlfy-iVwTQH9GUqMJ-_XBEcumwWzr9VA1RIrFo9_E5DZaakvgxTZj5IwQBoXP_kuHwvKueWtvEbEy3org-3xv2eUh-jkcuCI4s0A-JbAKN6tPv2U7jhXUIfmEgNCJpEhyamDlASwIZmc7dgyogfCg2C4tZA3orkcRkLHuNub30YRwJEjmfh37O225KKcQO4sisALcK4xZ0e3bBduxbgmL6j0pWpRUdCMo5rsty_iEXOqTwBZvEaDTbjbCb7MnGeP50_D0Z2FdXAE8IdHToryZJGZ0ujzGy7ygcN4Eseag2gsDLyAyeX72XQcmyi4Fghvo_plzyiN8P86g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UomJ8m4GSgGppOp_QbVqjulaBo74Othm-IZMrwU2uxPR9BFMBDrZYUU5CwWFbfmb2_c4jOPRnw_iVO3t4zmOMKo7ue8LfiAGTh8udayBUWXGRW35XIUycU_Lj7qCqxYkDCGoRs8a82-Hh8dFObfmSejdmaTmKA54T6KgNKo8YwsG77ZlyD8-BIAd-P24qGHH5KYK18gfziTZD-gOGgfYFGu-s511_YNt-hef6n8iq-w-YvebKEOG6di1S0aozKLREBVeEKLBURFpzviFUG-Ck64YgeHSB6FCs70RZ2FgcrLNQrV1q_pmsKc3-kIlnVrISl8T4WLasMLaO77YMQ_Clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjMM3mcIYnBkw8HrBYFt5ySQ5E8NPOGuW7rr1YwlSmQWDb039BxtZn8iYA1t0s-RgjUG_MAGUR8J8SgoF4Hppt3VEUi2V_lAA-fZzkbDMNWrB510mu72_iQP04G4YtCLSCqaAfjP1upWIOYjuEKyV61PY6yUpCxtJRw_wCmoBzejhjMLCwpNvYkGA-6GmtYtbg_xBZ4UI2vGFN9zozou-CvQXs7IdzRyxvLvGZPLMLOtB0P_I7IAyo9JC03k7h7egTg8QNLBTOtKUZWKeyd4h0Eimwn1JrVxPlRadBVMYEX8sdfKlgfpgbWc6UCZvLEKeparTALkqeCdXwXVB-7SGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3Sd-1kttOMwPqZQWb_0dnrlAh7lVGxMfGYqPWGRkx4mjlChLle7doElwKqMN_1UgGFyfqNcSimMOL1YrAluSdJZqY64OGeTvXzzD5daRpz6lGxXmK5g4c4qxzd9cX-081L1rrQGNGYLClOsTB3RwUgeN2dSDROX8ezPZef_bUDYW3wU6KmutyvBSkYnwssQEb4sJWTlJmTf_EM_r0zpRgDVaF4nZ2lWQ8G5UtDfppjZ8l4VBPkN0aFLsSd4GF2HCAb8RzS5dPpL31w8Nf7srd1czcNFfx_Ahjq7z4OtJJ6FNXvF232mmwdfc-l4q1Ql9qWt1pTWCaE7eCNNQLJc1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjUgR0O-B295At_9XnmwwiJ_pRHXQ59YRRvip3F5sWg9Is731frhFf_xVLjwuiD4jQogpM-cAkNu4VwYCNc9CXrL0SuUuRVhUSSpcej74uAe7OUMo3l35eeSQIVuDIHo-9in20xVxvzfwoiDYZSPHiopdPoLKmtuh_j_r2JVMrQRjS1cj9sRp7WN1XT0FE1cBqBnPBY5F_vJiqbNgFJWq1-MrSEPc2mw3trHQDFaAJWYqt7q_Fts5abmRB4eK97wqnCVyR657H-3mvjk_5_93Z-qWoBmUBt5zPzC8WfeVdkjF9dBdf7fqRoG_olmugjxDeUxrzl2A3sbiggukWeHkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3v3jmRWZxITqXmZvwdMlJAx6QIGYUUZCQgNDc3tngeJuClVPTuqy8LC5yOWO-YBE5xEgjOxcIhsTo2wd-5S2Y1cwZrH8YF8mht7FOr0ZJ6b9zSH2u7yX4dwz_-LD5sTnZSaxXidRUeOJ-SswYQTBOzBS5obRMxz4ks8ZX5-NjdBgUytlrVS1pXiQkvrl6LT7FEuZpo-4HCde2mmP0zFlFme7ddtza4PzglxFjLT9ciWzqoTnfq5eh-qhAN11FwMBJciC-a95VqLM9QlOZWEA1aVedCubHAGF0omCJ9-qPLS_8RMzerme0SeEMwBV2Aqa7T7uAE1052CIHbRBsBOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WuvDGYE0xpuW0nVET4PII49F_2-W9EGpGObtUYQGYIin4rAyYh9CFFMIwX0s5B1JxKpxw_GTzCXELX7SeNGRrFgp_vcoQ56H6z5B418pQVliHiI61rfPbmGya2TKhBc_Esa02mAO9T-r-0vh5k4vOK4HcsnsfwDCHrNl3EITpfqo4rzhBYVEdKhnjdCqz6yGfDLlF8cE3ITrlTrbWUDxm-rHOtn-Bw89BDoFkEgjfiTLSANtqJpXFXqYbXNcaMsYXb2kXmzNUw_JbfjQAyZ5ZXUAaFhLJXClNbDoqOvXExOSGBtwIWqzA_BK4Y8Fpc9GIGMFHuKwkfw-8V0h23uQ9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGPhGw9t01NQCL9f5accK7PEQKQ3kLL0Rv7QyhlfAc9i1t_d_RYQf5Q6mUaLdu38bzX9x427FsyMJYAt70WpKeJqMVAl6nWY1_3fmwzMcqePd5q954ViNbWxzqi52mx9BItrILiXfxxTV8PpXGAApi5Ih_iRed6r8cKlMu4AmXDC06V4wWF_OLFXTnZj3gdSpbppJzrQVKdLfH42Btfz4bGOAI0cfB6C2LGOTDYqHuxNLDqnFoaKlL-wNqmE6U0XRqEgmNx1bVp5RHmWaral2LhaPptzhOszKfoJWXKv-WZdEwcAd7rGIpBSKCLZOXA3P6kO5rKGE51ozgfiI2HGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfRBYMabDDheqh59vho4tl6XDHty9BS62d7kW7dWAj9t1Lk3QYapbLNEWlVzbnQwTRhi2rnohhXgkrFQCj_RGhfatT1quugvGCxoYrDdiCNyAZScjJJv_vBsjoCJt_HjYjAq_srLZBsdce4DAZvzHzGmtqqfMNrOeREGkQSBteyWhKlxBI2xGGM39-LRKqwfg-OikEgavFn2RG21qKf5n1naMvN2fOOWhn69oXWdQzxm-wwwB1bR83FGiC-kOgF0Rj6rsupLMa_-0CvcwZ8LrF96Z0Qi5h52pJmaEIl0UsSG8JUjnHiLmp9YZ3-qz6H6cO-IKkPHdcm03bxGW1jN5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baPY3lSKzVX7_V-WGQUxyIMJ2g_xK0CavFdKjQw_gMVIJlYjrakkPoYF7Kxr9ecPCFy0mf-gMcfmVHL1uYCKGNvMIpk9XOe_5DoVnUioGMdB03EO-A6vOOrX2E1LN9X_28Koxpwf5-8HGrO3shjeHwZTu95zAE7-54p05zLzoJDfG0MWZ5arF5PXmlnGEjtPk3PEyew4BQhR8Dc0j_XM5tmhgB8nJcF3Trd2IjvbIDHvT-7UrtaB_dSH-4ouNG7JFTytJZHq5OWUY-rLeXfclPj83Rz30MmgBNrtIgwzYma4OgmWRNRh0nxVJDNodzsnNBAtw28zB6tNb4LfZVvyOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rskQf7NELG3PAcJjAsEDVzgflqIzkXvRkrkof8MLxFw8uhQqC3DTXchFpFzStp7Aj5VB8zRUO6vV0pURzgzGsQRFtY4DCAOJgGpEaz8dTJUJuExU1FSwrjyqD_Ci78zZxERDAjODPeT_8kkloXqedJdWwzTvMm96OlR_mVyYhuTeNrrGBA23Ezt9pN5p1lC-xh-yfwlQidWRA6lRq86RXwf8kmOv2slg-PUlkFSHVCSOgZvL-WDwVnnjOuaXb41w9nJhh4Q9xUwsYA847FcoXHTLbSprev4rp4OjiJDjdb6z3vCf0FqHPPl2ZmLfGSe-RG2PEolXFPVVc4Jb_T7pTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6KKMy_i7xEohyXWpZ_xv2OYKcusN1BOO35YUiZMyj7Cq0FSgmmypqvAkZBtFSGEATRlcNXrIgk7TLknHgMTL8nb46wpVyE12BMgrGWEizZhzHoJLGCq5b-7xxWmSKXGEcII9PWNwYmPjZyyH5qUFxB7Ro1IepkUxLUkmJKPjEd48_3OKpOV2kuUkFiAspkeCLg72kcWkEtoTRbCB7tNXXZcNPEVksj0tMh_ZxOdVxRJpABz320x-Zvg2V1BSc-CnI_kHu6QNsNamaQtXk3IqAyLWjfIBK3Yh_PUpfogF9fd3_RcDdALfKY9SVsDyYpJYUNoSfgqUArKuO0IJzE3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SH9Q7SouwMAaAnL5HeRPWkzm60bvJ9XRe0EUSHRHUk0gVvfDNfF0UR9agVnnOTr1f804mBGlsDpyIRczc4nmCzkE8nrPycTcEsIc7NXatRpbN1zBPuPDHJ_SujG-zOyGjJihQyj2aHDyT57_d8ZVXl77bAtcw9qdfzChAKi3mJK492ZZKQ_8UWS3NouDTzKwlfSt6Zg4ZM4yqNkRAJPRJBNKAqwtUwbMXpUObCb1-SYvi7VdisPgakuwTTKVE9ZkzWktMnkzEoBIG6EdmYOf3RhpIAPLC-ZfRkLgMUzikd5AKmrPm4OOW-o3ZPG0e9mDqCcHAFQUW2hv6-NiqZg7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9q2UkDBpGAAfStNdnEDjjKnSh_BCFa8rxH4_WCNMUV-v5LVweXKbVQAvxB5secxQHP2xqnxzHmVh5C7b1byvXK_4FvpQkeIKAD7bLpcm3TVzNWVfLEaGHNDC-JCo-rAKTEw8IYO9d3n_rO6n5BdGj1zaxMR16agp1QsCRAhWNLFBli9tBT8w3vqi84mYTNo0u44_InAK-vONSt_jt-eKc9LKHmrzJzWNI4yRnR4YaD__kXYZLqbkIk83H-XeUlIrUW2MvEJMCiSglgWTG_3GFMYj19ZtNo9n3fIZloFBbT2bYCcy4yGLereRhPRQ0OjONyv326xSmWslo2FbH0fSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lN07FrV3IcdRotALpmv8QFayr5983AC4yC8XYKhq-0FF7kvuGphJUBTM1kqkbG3vFWMkFCLCiPPeCSTo0MtZq2Z35Uj1SSt-ouw-K4HZZFHXACXuTLCyKSKR5HVa6JDEXUFiccsJHlUhyLoMBukUTm3Vemd2Ll58cyCDBi5shj6C2ySFbLdcHoOt5qnX7IvAuwWqCFlqZ2tS45EtR8NHJ2O2KFpgP94nRsT0kzzWpJsYDHIqgSxss27RTpYcOp_ZAe1w-Ka7tjPYev4TDlevh4zEul0d0uySYBe8K4WGxhN29-X51FkCGCvoN15jjnuGhzzr95jGjigzJU0vcdhfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnGKRUgM5eXag0AKaxSmXeGQYIvPTkrqQQcPjtJnkV1XsyPurHsoQ312gyuZCzbrvg0X8gt37-7cblbE3TYSo7vNS4NvdPx7cSAMJHxqUa7Qa_5LyT-s-zc2MOvshYj_V8DkaAUbvdiOmQkJvZTQgbr8EUj5T8gQefk69xkpkOLj7hLwxL2hvy8Al4nTWWwEOI5rm17wByILbn7VgfePvgRbE8R6FcpReAv7MI48Qek7X0pMMOSvNu5crHnjyNFjDLJnWzE-nWrOURKCwnQVQSWwwXhVWAxQ6PFeSN045G4_fgQ7LB2Ysw20vp7Cq94bcLOkiZboLWCklv7SOUX33g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l94m9yv0Rs7-3f5Lo5CkG9jJUfarUoNDjORnRvcmZ3EuafS-bcVVHVP-c213nbeGtPyy3sGD8GSk347Nv19U8wRtPP7oNvOshrQDDJKWUhR5o1qMqBmDjgTdgMr3mxCPgkj6WyXRkHvQKlJfOV29NX1F7y6_A5sXahvmJfxS7S4ZZn-xu7GAv1h9293OPIuf6n3UYEY4DDJxOJax8ibnuTPCocQBmZynMHUbifdKa4TDF9o1r0L7aplrUlkLa0nsc-zJzioLAkHdHl20VtZ_sLVJtFLDf8KGWSeVVb-hEFH1uxz7pFFLfdsMgv8784j-8EmNytrN-BjDbS_lWmpg0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANtYEKx8ca88ehJRNHpY6Lng0mhqJAXvirw2u4RQSMZWdVFbgBmM6f5vT7SNtNLbzdZW-g1LQqdAZkSgzTV_RY2iyAE8_iSb0rHNNhRZ0Qof2BsowgHTg48JlwsrFS7n1uyJvWE8N037ME1rURD51mT00A-4WgXePtnCVIU_ct0GSbeNbStnO9wqZjKBklz2a74jX9ID8_kZ24LJU68aDNI_gkJ29Q8O7kNzasuDdl5hYenb1ikoYOVznhEwAYIqKSu232xR_L8iTidSeUOsB9OudzezeXnB4iPzbqZxZREE8Tfzxj86rph149_xvOl6vzFekYKPGTt47yyb1G-mfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0a6GNsqEi-AegrN4SjzZqj5n23sY39GPYArWEMMw7KIrvfnCj91fOlqV4ero0-77zjAf9j4zRNio_Ru16WGCDqXTLUeEKW2kzM-QAdp_sQT1HK_8op4oecRtIlUQQbvb7Kc2pNv25umtnAzoDexiNMa0kF6ajELPnW4gQIdhwxZFVDcvIimlx-G7st-7u0v1wCnxcNa79TdHQHfyQ4Kgdt_rTjccMJA-UC9xPKJafGls8FmPUKLVedTi73IsPVjn-fAFARcGpTGxvUmthVUCCw85ROIliXlHUkIg4S-dtFAEvEAt1whHdPs0m_6--DBgDedAlNLnKMGzrKcTQGI4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeorpXxDYci5zIE_Dwa9VkIGF6fuCHyKHQOYScqyu9to5tATkYW2xeb4hWmLe_-RaO3L4NU6d1npEHJqW8vHNTBiPFb5H2BVGp__2OyX87RaPTc4H4FNNwTg8weTrzp3UvFfIi3FIlDeV3IHZNwFUi2qwaric6hRmQo-Eco_DI8NeKjcd-mR__uM9OCi_pkZYrTKYUSC30sCAnlBl3B2VMTLwXZo47bpIoFuxkzmp-m_7F41xvWjdZHIjsACZ35SklKnjNf8sVwWu5QmQQfK5uoad3mYSwrR0rEEmG92yESMvpP8UPEYss7lfMz3cIuOcOw0Bvv9iwxNoglxkccDjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgzmPSgB57o85naWDKSgG79G1nAwr66OUHiP-xPKZ1Lsst2jijPt159fNScYGGymHlh-JJkNogIKSyTJtMk8wMKeD8PzYsVED4hnVuLG_be90cTYUnr7efIUAqkfoSlecgpl1UABLDvXQoB1qWEGTNWPl8I_bE0I6YYeC3uuAoYUM49T5nHCvYVlXqhqnJKZo4oSk78rpgENubkoFtYcBpLxNF0qDQTyufCTwGTUSMXKcqr08y-ivm7VoHaztMWLZ1X3pYifc_pk86SZo0l3aCY3CJRAbho8ozwgdQCuUpY9raELhSX0fUIzHvEd2ByZ0tIF5F5RjtTON6jMgF-frw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adADdfBHv3BzvqYNp-g9Q8umrM1ch5RLii_U84cjR4qqGnY_yHONVUKc9deFKrqnJHVy3ju5QVho7iq_1n9d3nxJ-29icMCkX8OmteRi9cg616znKkwnebyueJzmXXF6wbgUpwGvI1Vkf6IcUH8d_wzEtRLVI5tJrMMgBRx4kqY4OniYJXct5o9lkjzxGN7hctlWX1fP6E--BJlu-7jnKbcU3iCp44lZBm0hgGmapKhd3I8enQ6P2UzcgYdykAGzUCYa7xydv4nZMy6reUAVlF6J_2bp4hgUaSQ3r9Wg54KiCwPHNylj4u3hG3UmOujMV8gcPBKSBwScyhQrsIFRZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA9QobdBSUdtfs_7OdozQ-3kZmVHdbfntEyzwQDRrUap-5vTp8Jd0hc84oKqjEh8s46zFiB0jRCnwunhp5IYgz7l-b-z7SVIA4A9hEoxHc6PyowZ5Ezcrbiif1JzNISODa3KQESOpDtCJ9URnEgMH5ppuQcnFea_6D7EN7XNr50FHmB8w8jnuIq0a6nbFi1RBGJBTCXrtNtJG2uAeZWGMTyZ_-uMuf73JIWbl3oPArqOnFn1_Z_3tKARo4LoBV2j5WbnkfR15ByxVf4C2v28jCnETLkaiFFjXBCMRdt-vIHYiVcSVKc62qgE_uPCpD75U2uU9ioLtkPbfnkxLlDokg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iaZQUXRsNMDV2LZp_VgXcqoKLKI1mXbk1C5Efpv7zJn5KCCCUKg8PxyWyQwmqNGtYoVqbkJZuXQj9rUWuL77h27yBFWHBDhBh3NpN3YPYlau_3R6jrMA2dTqv_Y_cEzkhqQf2ndoT8W35g-_YvPn3gwHvANghuHSfl6B-piW4ES2sRLRqvhfg40Se_Z2ijFyIGVa9IytSz0PSMjBLN6RkJ4dWGkM1kHCUle3nw6tPBHYXoqYdEbOWn9yQ2LYoC-S_bxuuCaSLfXIf3iYoJzU19giK69WsdiYA5dT9IQAps3TGVuc0o23_b8PxbuNoEzjqcySymd6ggHRiafamv4C-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_mov4GIn0MQY_3Lq2D7BQ_CQHIzrAeFAOHuDqPHeT2EU_CPif1krinVNIXlpytoHLzUNNMl0_esGM5rLTmAcmX533hN8Qx6RWnFD1pNJgWrd2_spRAomGhJq8hs2chomrdqd5mOdw4zC7sivCFfClK5kXWKKsOQHoX_WpvA18O9RcX0fBAZ-Yj3V5Q2bJPe1LRhN3gxR4y3VJkL9Zvfer7uoDuaMuRgF5Mg08AnnIBbsi_hF5cbirnLcB4lFJnnH1C6-bgLKMVgTvmUxNWv037uVqjsVXVaKVDxQvcuGqSgLvpDRdvOMotJVl3EQGz7XRsQnVhJT9N3p9A7vy1ahg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2gY1J-p0sjX-1HLxNhJHcUYDxe8DJNPIDRGj3J41iJcWehns7zu5ztPYUHErXDDEMs9voOZJNkaWyslr5fH8EpoaLOHjcplumeR3_OHLBylmwKGXr5QrSpxNsIGfP2P-SA2xTdVEucDscHKlCBaIdopjXifr-QMRStBGLaYifqe97ynuNYUmGBoDAGNz7aRLRsttJy1yLwAxcWAD9he8JGm9MNkb53ynaRvhRhGIBAaAej6Bzje_uMSmM0JBx1qNwjy053rmRWDi6i-RRy6QuROLX40Ba7Y2BjdpIDR-orRyY_5KhNRmWrvoqdey-B1TgJuz_WVHumIeCAdGVeWIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgEsiu__Hns1ez-f-E14T0iwbje-WKgpngEsdQzPkTOlwPfH2rIZx34KGGwvvMH4JHUxYn7ZZn8kkZPde9et7EZo59i7GTOHabcWHoD7iV0HtfEL8U0RGZ2pqKnaTwPGtmUCX3LevBf-7i9l5p-iqPvdT-97IrlAWAxVt6TnD-7OAT-NjW-qwN15tBcp7cwjUl7Xcfo1theFimmy_U2SxCMaQW3__MnVt9cud0s5SPjI0h3sejZpbZ7gHP0IAC_cIbD8raP2MpMxSLKLV8DxY4wuNSYYpQt-sFnORs5BZAo9Ruh9hIGdBBVj5TjZIY1bH-w_Uv_FZ_PSMrLo5ZV4uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl0NFxRilnjq8eluJQbbQsrHB3ImawK6EtAPvbvcbWJ4QhK4hKzgzRKSPyAVFi9hg3jWFQmEkiIzcx5jVeQinLh5BlO-pNWQRMrcDIwyNRq0Ar_98sIOwkNtS2Z0TJ4r3XZA68SacFzGpLMLXiqK9i5AzwEU3qoAxHhR0x7MDuaYgPYccuiXtEPQilKPOfR8_U-cuukJPIE9UxNGRn0vAZK_5RLeW2_PZEuXxvQ75vsFP8nLh6rmIlaZRBYRvM4IHP4y-tuUIjKML6ia3sS6alFOP31RGBTlpq_ex7yxMSVAEAwyuNLETRWKX_CB4PvqxxU9RHyhEBBcTKfjDI6euw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BovLb3lqG2Ptp2o34u9tScZqvJNUS7Csphh28KAImPQEqYOwdyrhMNDUv3h-Xi0OiNuMDMqTd4GEGM8QI2IwDA4Da17pcwgeNAJari_beoH-03nq7qc1YlR05BUoLymC3aVgDnxVVkSJv3PddH6z0A8HpDs9VvaxZtm-5DMxO1Xgn4vdQ6qRRNJm9qA_LJ-PyS1ENMmQox0JIxwXOElaaQE-E7udUGGLdap0wfsWMWqnJcGgokh0GSYplA3w3EPjPhRhbBCnEtAcldz8Svl9GeqOXsbCAz4KP2Vsu9domJdyjkQy8WfE82PfYBnmp4UVz-JJopK_6NYlAAJDlPi4sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Akz2GUeWkm-2I18R8oyb5WrjEYsnByyWKMmN6-sHrLAQB567QFDblGSETRn6Lbf6ibLb9p_uGJvXl1PQjOFZV14AcMdC9rJKLDjmW3H9AI8J9Y9Lqon0zVoOEi5nVhpl2upoMF8ratgT777d3RtxBJzr--5TRg-KS-ORmG5Kbf2oS1iIFeygPZJLqsk8_5TUkah4TQGehTAky6_YlqFH0PpS2xKe5GarnzMV__qFZ6EOK6MxlCLnI6f5xz8ez5d8msg4YCEeApcVe18LBobBbsqWhPSl6ODQi0vHJHarTyznVB3Uloa_C7dYRJ4ihl0uE70nTcfB_MZ0lgS0Zc755A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oidSPkiOHsogFKCBMO5YlhcX6F1u6czyQZUuSyBYkiB_yW4i2H2BHg-ugSagOdSZtw-WEV13LetXFuoe80mvbAp6tYhPfCyEsM5JpAVKSlRoFOYROTYo7qN1Uv0kHI0LUf-78G2xGr37_05QUQxvi2-7xNwxBe09sgSmotNB62B7FcHmu6-e8v5xh2MPaZ2cpo93fDyLGgKA6H7EUuRr493cqt0LvkvKEYuPuIPrTIx5y45m_an1U2F-6wIbTC7ibjYXebLGsC-Jpel38ee0n7PgJLYzxunbXKC7FW_d8rQevKYz8N2vDcZ6TZ1sE8w1jwr_FDRpV-6MbmO9kd365w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i19DN30a9Z3OtHE3nJ4n4-ACXw_A9ctcOL-YjOsufnrAEtRmz8PU9yGqVAUNcnr_KzF6J72bXEB5sXdjIJZP6PUeHWGrEe3FSEiRUSj11Wq2LXncUyTTy861ekoCUNYRL7FgbNGnAIDztAUBAGf9Dm0EkPfiL-P3uFndWvfSvbVZCwA6KIRhACcfIsQPAezJJmjZOeycEvGlSfOwUb59Js6yi4Xd9yj-DzUyaWjHwt7vwcswhbF_QNrbyfKy9EcNrN6wbcoXCYfLm_gffRevma4w5iI9iZ3pqgm_6_2Xoe08Ef1PZBAvWblUtJulQIUvu9n-7L59FmOpWfTBWvfzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_aLvZslEqaqmKiSXrBEyc_-f1jSDUd8kXSdqWmyqpQgw5gBt4PV6vFIHCQDCg942dywVnZdeNXbuH3m5RFfKz8hbALKabwNSdlLAZi_dUfc7wzhZGtPufSmYHuyckJJoEsoPKCebcZr4AlcdY3V5pslyllA_W9H-gk-yALA4OlQG0PqsMmITy6SCzCHQtSlIkY0KHsQcpsM4wqfYaHFUCVNxjxS_F3TCiX58XpHuEnplm9MEpnionY7CNSkEt4ZNp8ch7nogJeoxABl5ytVnq97YDzJvsliwr6ZBBU8xmnoyplhZf_8Xebng67P8aFOXhG4Hb_hgZCOdpWg6GBIVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncNpxMNurWd36kqKg9lH8NilWrPi2ADGawI89z_lIpXOoNRTh3ALDcpVS44teWK7VfLSuK-m96dPU8i3Bbuj9Jp9BrDliHjH7dlCNUMFIKb4LUa7eZEvTOck3Q-GTQ24YRNzwHpxlsCet0McX9-Y97fyRkR2J67ah-HrGELjZlM-PPMvSEvT1AcHH-HiO48EbWEzt1G1oSka9TNngSV2S8VVw5obLGIW_57sOrhgjiWMnABKr0IrxvqRuEpdbijwUo07hRqY-aPqm9WqOaOv3a7uHbYd4BKO5XGQ2ZULOg1nY8PjubFsdEeJIEIKxBQMD0Aihf7N9Y7BVEZaFf_ijg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7nyqjJoJ1yd3-TinBgWowzmKnJNBP5mjwITSs9r__MRMasKsqjQVZhdX2Io5DEVPI0RWTzB6L-cRy-HRkP3NoDtK-3iDQ0VISKsOXw9rapsqTomUWBZta09b3qCBFITGANo_8eUJIG7jpRpulVGqCq71YjPAzbd6r52VohJRSs4rifZm4D6cWNSJc5txw9cTy3puFu4XKZZ-NEf_1-A8Asw_X0iDanU5b5ubx2iPrsP47rXGkaz6DmuImGeQN8eMaUWPqKEk90s6v-wonXfcRTpvU0V9deePiv-sV8Ywy_em8qWKByrU9S5kmWsmsAG9rCNO1QKItPo4k1bvX8zSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bog1u_KfC2w8qtqtz_nijHHykMD4p0A5lYNLKAdHEG51kv7uXDRWnnsLIL69BtxC8voEnvnw8Yo_PBAGtYOuCyzGd3U_L4WQKjXSRikGNb3T_rq63xgz4xsPdfcqzHerYM8dt8CI_3lgw2tGTCHVL6u1aZ1i1nmvxcgt0JniT0Gm_g-A8CNKi_WdhJJqgj-0JTy0T3wHayHdXbQQZdI2q1toGubadTcOz7Ild9eVJitm7-UVmy5q4SpK3GPywZAA-ReueH9H6TttEJzFD06vvLH5fLuYFjnFlpgUilFrBSMe-8xWtaXXcJqb8FnveIA9wNZI-CN5uLcw5qq78vuy_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb0Tycvj3RAYgq5m0p-2V6m-CzQjC_TT-wccD1Hslr0YWtK6SBmC6RHLo2cCaygDoIYPxjdXNpX_JP8dH1A3TDBhJGizLJCdhpyoMXvu_1rqtse3DRGI_Q2fB8wTjAM2C_NE4C1BM72goAo2qvjGR3KP42EB_vSdJ5oCAf3Zp_Of68wtLNHjIwF0p_vw2TuAHK15g7myS_qeQNcbLMl1_TxlUoUJ85cRg8w2R7Y2loXoLeTP7gfUoXU1YZre_k8WuD_F2iWBHDjfVzMtHxIf3dy3HgSSOmweYLnHCkr6HhmVZcqE8W0qfiAGuScCu0NRMxrlF5NIvIuyf82j_UeEkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvFGqbIH73hS2-LOll2Eqh3_XS3qS6pimdH4_PZ6wUQDzssvOxvHaYtnhiNt2WHBw0Pe_ciBXJKnbdAAu-RUTRsgN9gt8Mebork0EU68z1d4f67wFEhUv0moMcDHJiyL-bVNa1hkkr66voMi8JgpQE-hs_pQyOjs8hd8VZh-mY4aogSopg8lw3kWhAb8_FCg6h7t9WR0R7k1St_nK1jgYmjWvjwI2zrd4m_L5sfsb-Vi-D_clxmKP7BtlsZCGpA5XFBfkLlhO0CVbD1Pxi-pnRYznyYNebpygVKVZeR7Gc2dpcPvmS2bQfuEHd3OcK2bNZtmr0Ma-SkdpBCPYltdDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbuMq8g0DQymSJKCF37BYCLcZrxfRAH1pF2-4FTNwlSbMnW86Dj8NxN-0pp_-_EG4ZSsgWVjoi79eSQ6xwIGrnz9zgd-RhWZ6CzeAJPN9xwoNRiuc6XvfefrGyahOtwMd2zT5f20gExYMgdVsIjBxMrBHeI_SgeEhvMWdP-RDXex-gxI6BlqHYkelsS5tnF0qX8EovOREzOPk4LH8XXwvddNY_KEloRyUL0KqltT2BvH1geKSY6xiUV3_MiK9WwSD8oLix7DDDUiYZxDnxDHP05Weox1QXLuNVcS00thCUvO6g-qBAY_Y8sSBS-aXQ0x8V5VNlXzQJ6AF9WMb1J6XQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcMUCC6cP0dCdot1umhrAniKVgksKRxX3XDr7wXF_FvKLzV_O3depioWZbLv_OG62h9KTjmy4uXZY90UkwWlZjMPkIZHaH8JDs-BaesauX5iV_yNLrrffCQt-VYmWVsx4CxI2cdZs5C-8ScPhZ1uBDDCVsWR8NsADhnP9m00EmgDt92-iMHfIckl4FBfBWlsSbhAMHsVdD1KIPPQA4bFZLMdE18AbRAMBSaKt_1UdrEEo6pzwRqIUZF-56b594SC88Eu8voR2oFB80rtODR0rVYIVBv8ucUvAIOoe-7aiCks9pNiGrXkLghV6GdbaEIMd2587vtKYdPr_RiMCIG3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flVRXvLAoeDyL5J0WcvKLdWy9eAjr8fNO-JQ9rlYfNUKh9EQT95Zqgpzr1LGwLmy8St3DtblcE-hpeianXEN7sC4CJjh1C6pvuTYNsJLyAz_op6wcj_DcYD_viYXIBGba_lil2tgv_kOlt8eLpB4KhKc9Uz6rjbPfqGNg4vpZjuzuX03bs_tG5oxbYQo9fH0I813Ep31F9XMHRfSoJZgj7r2-A6fWL2Tf6wSp-3ikGGjpbIaXmMQDjVSKXoDPmcjCcPeRbwEZpbcwXsy3Q1yrAkRh8kwy61h9ZHis1XBMO3nC_r0svYOuGAXOyLK49irVWeBmskW4w-gf8Xq_s8jVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKSjIA3hbfF1myKlZTpxtf-AdPuULCOFVyGZk6qs3lY8RKEOkQ9zJK3_uXXn-k-mB9LIMJ3u41ZAcecahsSnbc-NFK8b7nLcXRndnitw7K80V3bJ1XNdvVsJ61LRyoumQWRH0_aas6NmdA39fZkCpEzo_UIwW4ZwCTuioPVVsvAhJCkCPRPnrf6amAZpa3cBNu_kEK6g2FVl0H6fGQkcVpvVkuklQwutrrRrJd0wKcSke2x0zkPnOJAqcCeA5J0V8srA9gLVOt7TIaeVc3gKAP7OqWrQ6H_-L7hAGJQf9yO2u5HFS5WefrhfeVH2NYRFJuYJDF-27KqvC5AAwTr0Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlOWP24tDMxPAIDwyaPxCfqvomBxXDG2L5L6MqCIs-KWYXBOTVXQJGYLmu55_WBnr1CCrUVp7a4UPu96Uw9GEPb_l7Nm75VGVeuH0XOT2sJkGjy_ZBSbo0zQLghOtt-8xdOktoPQnepVjCVqs7wZFkrGdrC1lw0jQa6Rk0guXxH4nzFlFxIbSsIsMwxN8h-7hyN7f6bFAwM5IiilODMnL2UpIBKkqs1fMz658jwHD4eD9hGlipZth9LE-k52Sg8SP0Ige-DhnC50IXXURHQeRk7Cqyk2WNBZqqSuOO7k8UbOc_e1yQMOP2TuryYyFl1S7RWPHY9vSyK0_CGAmxiwSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpx56tVcY2lKFH5Ox0bwzjJbWU42Yo7ek38hKw51PPndlpZMGeJub8uTDI5i50-p-4xG_9TLwQvxjTWmU-X45QkjWJ1W67I18djSb0I_21OTms9lswNASsOUPGKWoLP8CRpFwnlBp9Wx19RVQGcRZB4eD__ZIUCLZ6KhRWVxlnPsFKRkqULDqV8EkQLY2PBh7qdhoaKzJH9FXNGN2BJroCvTNeJSdMRNoPuLjPlMFMo_ZN_Ku0BSjKi8idaa88kKoGReVgMAG1Pge3X_vmL-gpBBrIed5Q_4FRusaF_JoHuF14ICPI7LuhFw91R99LAsTfv_nX_kIV3fIK8os7an0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXT6eMqXXWJ_Q284V6pXVzRDn83fohbz-v-mnrvmmE-tm7aMLXsmDcNggGr3MYHdb8rqJXcStsk7p708b7p2xx7f8vkCQetsehcSs7gxA8X2BSLKevSbYC52-xLY-iHQU5r1uO78_TVr4ovm4v44-P48EOeFeCA0mKiuLWJXvgnUrdxck0LFROx61NugbHesg8sS-VkiL6e-Zm1CxrHKBc8sVAxUYrgPLlcPepAd5iHy4rXgUsIHr7Sj-0KTXRe3slDtOkPxwefsE20npxJi0w9c7t-h-sEpwhLGGmesDnXQmRjMa03yRgmJ3HgUa7DllgVEiTF9_soGDBRP1WgGUg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Ix_zT-wK2PE9v0lIf9PFgGKEPn5Yc5whIcEKbgmPZJxKM34x_sphOX6qmLUC3pfw8qAxjgZyg8FSxqKYjwk_K65h_FX4Wgt_gm6R2M_cM7SE_Au3lPcK8ucLORt50hCUXyiOBMfsOut3lZUuDtixHoDRTv5--1Byiwqddg26YBpRkkX09oMHHs9y3LkOIq4e6M8FFRXOa8PbjPe1MdDnCI0uBU8TpIRP9KzZFg3JnRr8yp8HycgBmw-Ig8zu1Ygj4JTi4M9QYXQJioNPS6jOJFgZTX_VJ5GqHL8TkXunYUbmfHXh0QI-DCTGVX4_b0GVTAR46yuG1hOqCuRbcRsbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=Ix_zT-wK2PE9v0lIf9PFgGKEPn5Yc5whIcEKbgmPZJxKM34x_sphOX6qmLUC3pfw8qAxjgZyg8FSxqKYjwk_K65h_FX4Wgt_gm6R2M_cM7SE_Au3lPcK8ucLORt50hCUXyiOBMfsOut3lZUuDtixHoDRTv5--1Byiwqddg26YBpRkkX09oMHHs9y3LkOIq4e6M8FFRXOa8PbjPe1MdDnCI0uBU8TpIRP9KzZFg3JnRr8yp8HycgBmw-Ig8zu1Ygj4JTi4M9QYXQJioNPS6jOJFgZTX_VJ5GqHL8TkXunYUbmfHXh0QI-DCTGVX4_b0GVTAR46yuG1hOqCuRbcRsbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHg9MdfF7aBQpXrsrQKMltNVthYd6TdqoI3WFUXqnqL0QTr2X4j5A4a8QQDVYKK0OHKGS6a5_ShsILoUb46FXuXOWWz-sDKM4PXL5Ltelsi-micay1aIvQhI4_f-1O-ZcB6i7ceFZcRnxy21SfUsttaW68tv5GXa_KwYNCbUNmUs6OHUX-L9iiJpN2WBDlCM4kvP_uD_NCSBiHLMSS_Et8jXpIrHASuaVLZ7E_sy628tCs9333N9JHyCTOd_xp0XZqpX8IsdnrmxaEJj3ag5y-RZE_WVxB7TrO5d3V1lrSGlildkfTFOpdxoQLCjtE0xa597-W3DWGqoqSHZgqphbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7Nb1MT41sghaGhIBsjd2lolkWmO0VQhxTzZ5ZtkIkuWUt-K8idCRdHcLu44BvQaJhVXllbadA-7NRHIAY8jBvuOpeCt9dVVunqfL8p8mEbgICwidjF9fjw0rAFA3TyAh0Taz6XfUK_ccoCZm89-djlmMoeVyYaIrMy3iyaJ5sXSMfNvJyuImeD5XhTqmQfD_ya_cCyrTf3NJZqGycjJnIM4vPfChghaMVtE7cYBDRenTXKj8VN8UkYY_7AjNVvCOiQwAQNmtkkUP2pO4xxZtj2_Dh8Zdju77eFpuAVIYUli2G73x7ITUl0ECR6Ueq01MmmK3sKc7Mj7C_k7f21IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q46VNtlYRNcZHngrhdoyWt7EafNBhe7QcpOsu6CCXSY_uDREFwzHedmsl_7AufRB-m3ve-ZeDCggr7JkfWVHMWyod27g9vPXvEC_qollgI7285IcgfBpRSyP5abicPYdxBqGdQVCbAr-fh1dCuNAcHPkNo7ZFYwKp-YLylgX4XN_jMhNvkT37PxEK2Kt4t4FQQa1PhYePmO5xiHCU1yIKgPGXO4gT2nMc7pvS_vPL9JdzxHjxTdY1FCywIbpJ6TskLHCld250lILsBDvCvP5BsqvPMkeSpPw4l4uE3Yep2SnZJl1Uh2hKW8W6Qc-Tf8osXj5nCsRgXFWDF9BeChV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHukkp1uzQw4sPQDAROySdeOKHQG_e7wuz-lc74IHje0vG5bFPwEKw2fVcXMZrIGzHn-xdgAnNSgr4o2f6jNAHABzFxP_51hfAxkXymYVWL4QqJtTBgMN__kXtYLoOK0YlimVXZgDptVETlkZhTAVptnkFBkUQ1SDjt2P944EnRPcl2R9pXotUADQsLrt7wH9dD-QsboHnvf6pWvdS6y2WKPNaTyhlg7Bxj-VpyekVIXXqge3Qnbm1pOCZM3nbxi-ugTzAJj_u0JwBTN0kCRaFQVxWyJB0a4zwFxQQ6ZK49KoRNQrYuBdLTrzqueoH0-FwnjvL29zD98hp6N6qHnJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdywcAQUeE4044rePUnwgwB7oprxSnrt0GtUDlVJKevnllgQeIjvJtXMwXVf3brr-VmigT351LCWBns-t3ARL7PlclPAGoODmbkIhplWMps22ElFlS2QjNq7vsmEfL8cuEsCM343oZcrKLFg29oEzgQGFRTdiGRF0zDHamEAi3DoLY8z4b_9ZM-cOAuQx_ko1zZs_I-MGxKylf1QKveXsS3DYpRN5IK0_8hgAAiCLMIDktt1-QYLWrZxkM2Gisi9AsKa0V-8e7TVbsQukZIg7lISgNzDZ12bTMJga22Mzoy6oxmTwqoHquRDgiQS7o8VpL5BcEYPb-nPGC3IoGqyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XNiWZPXxX18c3tQBptRMIBJF2XMKXMhnA8kXipfYdP5SNymTmSINVRsNd8PPwoklnkddF06un_yyQiQ6Hh_26rziWahuZq06tS4sxxz9r8qzps6ZDo7908uCp969BD2KBybVorC1Pay695P_vAYQ4-3UOk_7nEJCkYk5aD7pEgEsGSNX8Xnt5mImHFb2tjyz6JJnhB4HSQ9Gl_L322YY5OmEfBz9Y4J3rUb43z9ruUzmqVjW7rEkcID4BoSBBO0ze45wnU9R1KP22UoRF5Mn7BCRRNkyQxaSHETlujnBRbwofxMLhjLioBqWmbui70CRniE99MihtXjywZBhsN5IMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpaQP_tAs0tyYKs_Kx9NbnJNDiolE_VndK4LBlvtZUQQuijog34nsNgoJ3mOm3nM632iQUlLw3a5nVkOLpRjKVdmJUrOtFi2gvcv2KZSNZlLuZ1B44gmZwJuTst_g3LSgWbbzF361OyIAsFJmDfHQj1vQVvlyecaDU844SNbUdAOkuyA44JTTJ6UMKbfmSd742aJe5r1VULtmpWZWyrFGVqFX-6MH1gsDevzoQqg3e9u35Y1U-tDrAaIYFMKcIeCuU1jsiIiu4XMHkOs4oZTmNtyvqzanz2XETYJVVdygZlv1XMEXrdR-IXxgPSlCI3CE2Ordt6A7WX_UnGffxc0zg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=OZtKMBLx7vx5k7PJZ8muN8mSk0Qs2QeuXE6PjZmtLMDTQEMNBq_jgDQNlxxgzAgqTKoQ-sh7FnrdmllcYo5U7QH5_BODNixf9cHwDXBwHWjoAJ00eqrTUpDEBweo3w9UboO6ycikgbOkbUrcF3Ei90AgvChhAmTr5U1pYOWg8FLn0EVzg3jy5R9fWbq0xjasmkvyKVe2TdGItskrSXOzeV5dS3qCFA4wwy2P_IN7BNT0JkNIHygulQd0FvBd2rJezxfmqIAwbb6dSdCIH0cgvBOUHVAQZR59tBJEksjD-RT0w3FlTdSbnyJO3eNu07YSSyYbHgqoi78pzEH9ZizpCYRX82_3WxPxs9iSinZbWt9nN5TkSa_M10VGsbsUQQtK_k9QhK0JhNx5uq_kfnCoqQOvt1mpa6Qi1IBj7ySF5Rs2Hn38GQxC4ONxeJpFtpobcJh1IoeJZwBt4MGEde6nLRfZ34EM4prLCBQFS8RrOVjhURZcaYLU846Q1gjaS1FpWbLYZoNv-AAjJQr4Vd7lFRsB_3mdJOAx_s8VMokVy7awW-mYpIS22KIoypRBZAPCrLQr913pmfx_mS-fQJjoTiO-3MnQXyFLA_yQKtKPdG8hAHqWVuT8jhocL7NQSxkz7TWLw5HApjForlzkLwZgCAqJKFSo0FjjuCLf_f3T1Ds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=OZtKMBLx7vx5k7PJZ8muN8mSk0Qs2QeuXE6PjZmtLMDTQEMNBq_jgDQNlxxgzAgqTKoQ-sh7FnrdmllcYo5U7QH5_BODNixf9cHwDXBwHWjoAJ00eqrTUpDEBweo3w9UboO6ycikgbOkbUrcF3Ei90AgvChhAmTr5U1pYOWg8FLn0EVzg3jy5R9fWbq0xjasmkvyKVe2TdGItskrSXOzeV5dS3qCFA4wwy2P_IN7BNT0JkNIHygulQd0FvBd2rJezxfmqIAwbb6dSdCIH0cgvBOUHVAQZR59tBJEksjD-RT0w3FlTdSbnyJO3eNu07YSSyYbHgqoi78pzEH9ZizpCYRX82_3WxPxs9iSinZbWt9nN5TkSa_M10VGsbsUQQtK_k9QhK0JhNx5uq_kfnCoqQOvt1mpa6Qi1IBj7ySF5Rs2Hn38GQxC4ONxeJpFtpobcJh1IoeJZwBt4MGEde6nLRfZ34EM4prLCBQFS8RrOVjhURZcaYLU846Q1gjaS1FpWbLYZoNv-AAjJQr4Vd7lFRsB_3mdJOAx_s8VMokVy7awW-mYpIS22KIoypRBZAPCrLQr913pmfx_mS-fQJjoTiO-3MnQXyFLA_yQKtKPdG8hAHqWVuT8jhocL7NQSxkz7TWLw5HApjForlzkLwZgCAqJKFSo0FjjuCLf_f3T1Ds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzqKubMiadbK9iOwZTmqjASMsYbHWgShVa8woIJjGk0ZNscHrBlI773Hbiey5HbENNyroFVgUXyjIAsrJxbUhSqvCaDAl_PEEsIYc7IueG1vS0daEbBoLyIu9oivTbq8dYZzWjawOHXm_14rKl9D5tBECHo-Blzs0RorWmTewkHmpdOVkK45LfV-nWg2Xp_vMd50hk3KL6sfrVdD2Zo_cAL7Jr0zvu-tDufN56q_HFKMfPknF5N1yJhqRdQjPlEcZhgrvuUSAtW6ji_KzqTU0A2598ilqRUP5mWIl8vW5urXb3B3gidPlWWmzEs0Gl98qO56l0HZOGav1LrOWGdX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwXYZ95kElFF6GVazOW6U15NMKG0pXx2O6duWwxmfaBzBIT6xt7sB_pOyrTe0vbVMZqLM2CDhDvUlbCPUsnC5Sc6DeEu2ghT2l3kcdZ-6F9nxW5WPhKn-KcWDFyeKx1ypFrwWIpMGSsKo7O6NgBrZDFQYQnp_E2jkCOqmeyN6hMi4Ko1uBgwpASurImfkaIB0S2NCLu8yyGAFXMv74Q26OGCV-S4J3fm0YKL9DuqKF2irR7qrDbOXrb30PPCm8Xdjaygd4N0jTdFKXCQoa6pOKq2m8i9GwZkZKcUeIBK61ZS13FwwwgnNCUmmjOsca-mJTtoNXHRPIA17G7TqXoz3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6WwK8YWScmfTJr0T2AYzFmKtZLQTYMsEjA3tc_ol_ji5xREr36HLdPqD_pun7lQ_RQ7_ogSnPWVsF7UT7XluFdsQprhkITlNix_SoGBrIBcYHFQdll-nGiEpefEq9wAu7tyi8CLrIkR0TpqIE0tQNgmmdhyC28aJPwzC87jjr-hulYrz6g_4B7V1BAnGzTB05-EIG3IEYdCOkeBt89XO2L76EodNk7lOb0-w1dA37fpGH8mOBmt6fnOXEFjM51TJ2yR3sKq88FO5u3xld-A983QuBmHE9sl9JwCoK8qJEZZjpgLbGcg0gzNOGkD9rVRa_ng4kQUXmUTcNxKUYm3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxSPE_a1ITY_TZ90r1pMK7gUlamBU3A5Kf0cYUMDMHMbLxm48DC34l45Rk4ek15kN3sw70Gm4KFPSdnQ8YBD1xi65DnSDmsZFSoORFZvAeTt2BqH3FSOfC84P4m5-PpvQpSsw8xeuvuf7l8okPBYmGonE-xPUkFprZtP_kSiKhK8iohwY49GwCW4sA2LQF18hEvICMJcmJn9keS4f3NpJzINMr0UGKUV0MrJea4lyXi3JkIoUoB3VS4PrZXsqouH4oFhdWXYRHnE3gwm0ajxqNiMZN0DFikrB55nQ4UZ7GbgMATc0-riQzDRMxGKa3Trb_cKSBc1oUAFRnryhNagxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-IEE81iOVttZW8OBkmSDKWn9hqLCvgi_u1HY41m6KocvMzUpnGZLyezoVfhXSFeIaNDuP2IPIOEWIpPDrK4RzPgtbOpUYGSqXA_pftfUgBxPQWKNjqNIm4LBYc1rhcEkVRIYVj_fAUJJ-lnlDnmdXPI2ORtJuIAQazqxqt9ngMxDtphwPj-XRMwtuDLxGMmxj0lBsmazFJMwD819qvv73XbSGdI_9Yb4ik2VQWaIYUFNMvWbVSAuaVyVR78uTA8XSBJlnNvdySRH9li_K3ujr-w3e6NF_oUsVg7gHRaIM4VQyMq9FZID6-7MylEePYNzmx-HibDUHAJIK5VopO2Tg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUbcOjBmJkWsSWd5EaVY9kKUBi6vl3avfAu9eVgIuxuqV0Crnad1cic3IPlalf1fGgB1X7ZG7g3EYNUfFDcKo4RIzjeWLoFnvn8y7iXTcm6_Nzx0n_GGkHBN4pOOVpoJxWTk4CaYCikccPCmrO_QmOLGLI0gDhf1Z3cJDJnE4W_0KYi6Q-ngwl1brlWG3hAgVsvBvpQbZ43uclhA1gYkQ8PU-ZHnjw9omj8jKCH5y7ud4ws8dYCFoOfdUAM3G-U2pokUt2ybtEWKohcgGhggyrE1NBLmZ6diFco7KLhcDjk8e1m4QyMRax1I30mzBxAzZu52afK3iCCWcV-F2F60pTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUbcOjBmJkWsSWd5EaVY9kKUBi6vl3avfAu9eVgIuxuqV0Crnad1cic3IPlalf1fGgB1X7ZG7g3EYNUfFDcKo4RIzjeWLoFnvn8y7iXTcm6_Nzx0n_GGkHBN4pOOVpoJxWTk4CaYCikccPCmrO_QmOLGLI0gDhf1Z3cJDJnE4W_0KYi6Q-ngwl1brlWG3hAgVsvBvpQbZ43uclhA1gYkQ8PU-ZHnjw9omj8jKCH5y7ud4ws8dYCFoOfdUAM3G-U2pokUt2ybtEWKohcgGhggyrE1NBLmZ6diFco7KLhcDjk8e1m4QyMRax1I30mzBxAzZu52afK3iCCWcV-F2F60pTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enP2iRX-ij8_S-bV9hsXKRlT8i1qVPUsd3nQm4h_niMS8NLMQm1SkmIRXR1aZ4bG4PdJNNT0xNuzdbmb5yUgE49T0NIpAo-ZSmq8BnbX3Q4CHIzGXC2k_8OU-w6c2yZNyhjE7qvBCLNxQyqQw8RNm3GMfM1n2Z9ZJAVqbpTXxBAErPlejoEdnOxIph4_BVogtH8EHfwV9P5B-eRBzcwWpXmeUvX-dDRZX1HXt8iHwFQLBr6jJjy2YFnR7vl6rM8S-kUzBqQHv4ki3wDzwE4TeJZG90uqRpDcgY4Mla45KQFgT1bB7FvDZjG-D2uOqCe_a_j9V5oGqYPpNeozrV7puQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scfWThF_p_0BDZxLuboCJRnCT-d3KT3ipvS6dmH0F90Gc-_kqLZMsfMBvf4MZ1VbTcuQwijr_xfs-0LsDcCarRKLfCAm2ugkF_HGaVg5F8YHryXYsjbP7Xb4ubefng8kq05IYirLLhqF06Q2MPvITY86cU_jKfIOmINzfMq9I_Bk390RztLIlR9cdo_nBxt_KKPtppwkcr-HzY3XP6cBDaw6ubTjgDyH-rfow6smTHSalb58yoYL75FyI7hGEiFiwBwsO7cnxAeXo78dvSxymiWVi6WYh__caP1bkXB7JiboL3gSx1vsnBTNU9uX9Pb8qj057wJfErGBDS-Wwnc7TQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYYZ8QF1a0TM5s-e5ISiUgPcy6PYEPRpThbpB_mWC6K8ZbXssEQHkgV48hrPgxy9HzdmYvdmzUFX7euFBilvs2NgEWy1FGbUZhVt9p3V9PE3ZvrCJT5vL_cXJHKaNHlK_7QXJyHFJchuUQH2ZRmqJ1Ek4P6r-QNbVUzFXsHLk684TTwBGcW5YdJV0SSl4oKOBTiP5PqcQQcLe7KN5_u3PzLVP52E3gnnvewrMh9m5_j09XBPLo3x-wt3ZQ82oq_2CSdgvq9x1ALWah-usMrP51Ij85bk8B1vIMxVeUwM4P6H6F0TJXoZut4GRubcYz6SjR9sSQIhQD1_hVJrrnIOww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyRvPhJyJutqCMfTTIlW47-HClU1TwhHrxN-IswWJQHp-4c_2iar8yYFea0ZAq74TjL76rKUkyFnr3nXplVQ4C9odAl8bGXe7MbRDOiyVctHfPDi3OHNN0k27sLwd9VhOHxPqUoVY8qwbVMXrwhPcR-N3zyhlzjP8-25p_SFuxyK6sjvJCoxuLhsJRmi6GPWQnA6HOZpwbj2vY_Nv8MzCA6tS1GQR5-x_rGlsK3YqApHVhWJ-yESxRnSKY4rwNyj8AqV6eWKdSqIvt_9N3dcfP9ii7ogisZAX99tyK0XBXCD0n0uySKiSF6Q3ZKqWlYwYZ1syzRWxN0dxnYv6lV7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6V_GJZXB4FJU3X2XyjZDM0s9bDteZ-UwDtVTho-a1J19QZjwZlWUkVuI_ah3Cs_X3qojIwKlYueA7MTHNFTM4EaQb7iswzDMxtHmF6Ouq8pEtEt_AU0ZzoD8FHRXqfanZlt8BW-2JRg61V7BbNfmAAfvLe6gswfD3PnDEdzq7hgzbIarQvIDx_0GDNHFfgaOOQPl6Q3hGHdiFTsWVWtki-ZI7xOmavB_frCdjVnWpKZAeqmNUEt0CzbnS5AFjEjym-WIpHtg2xNzj91zofdx614_gKPhdZpeWIUYpU0ODzhX7hJGA5E2hz2fKJ146ofI70jep3pBIisRKHZZuqU9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJVJhSeZB7JHRw7sNp4ATQdRMX9rDdn-BABwroJFgZKbE0wIHYTBRzTicCXykmwgTD3X-zEuyIIvrMLg4G4ruNxCNx9NJtWMkm6wEG0Tjy8bpAnv6BNajiIBXUDON_1DDcnEFHm2jCHUHe7ZTXStamqz4GrLVop1JVhRik3AviGJ4hkqsPygO-ReliTNaz44Q5soIPWtg_5p-vCiOx3Th6tl-u58Nh-BbnxxtzwQgUos0D1g5mcuaQmmJ0csnEdwTAsJh-tDgLJzERo-8N5AbFjXqTjS4Q55ZBF2A5XFFxpYJsUCuN7k9CDF7GPun_TcOHWqbeYm9qgNJj_dei-5PA.jpg" alt="photo" loading="lazy"/></div>
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
