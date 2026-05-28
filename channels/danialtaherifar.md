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
<img src="https://cdn4.telesco.pe/file/CvyUhswOOKKXsa1KUgEinvyZd8m2kXE3Iq2DrBlST2eVpF5miO-mzcD2sYTEWr_OQIXvHi32RGmBiUxhBDqzQJ1QsXxSw_o8o927xV67L5IKaAFneq3dkjZVJ1PD6432PaUGa37jiEqkVslDMQSWLEA7R5TjFspQsZ4oEggP9DCpb-N7JzY-kT2ny36n_6ir4jlIlkPRSH-JjFRJUhq6cd9inUgDq3KP9qkWWoiRsjWXxTIendSNXsEYH3LFNdrGqRl9DZ7npqfcPFaJejg9MXJ9HhapCR10ZZoVaP1KAERt3h56tGV9ixPPtM9FjcP0nPClD3ZwMkVlIbm9bAlnSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 01:45:09</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 266 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwm99Lz0df7MVzciC5iGxYFGjiEeO2x6Kui7hdxMFVObBrlbQKwtwuBYrw8DvaJR4ixobv9XSFJC8DNIcFVhvC7zDomiK3g5ytVSKmD7t3oe5My3CbCqldctkwJ2eukfR0H0PXtPYs7Qm6_ODNf5wZvOYOgwMTjU3NwbC3HJ54HWykV_oSl0yWQw06Ll5bvd_jvcdqegEO4EmL-IEmQsLGnYDheNvWvuewGJ41Q4mr-BQCNceDdApvkxXfnFLzZui7ju7mCPUucWt5OCyPv1_dz1WGNDqdVKW1JP6qpf-jhEyjvNshcjCxZpkkB-G64ito5h27g8_mpyUvvi6gIEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 463 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8-yMnvxOb9-mEox2-2xcnzEXUD04poF71E8IWJdh3b_pv6AcoObdcEVNSLh1Af_L1V5PBWHTmrESrfpE4BIgcq7CPclR7gGB6FN35JDlyi_hl3Iks2x0BMg4U3UW8kWWJPisxCL6qX369mPi6ipdIE6yTfJCoko8iQGc02nbeMLLs7tpknWjaB6rPy5OmbOuiBGh1AL19H1HTpweawjkpxDuW1PdkeBENRA0AvvTP6NNUnO5sini7lhI7UGZOtIVHY_Zh6YoTcV3JRfBqLG8gnP2DuNZ-nWKd2cnU_zb9fMI-shEVAz8bncqvXMHfa6gz1l2dj92eyloaLa5tjvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 706 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWDp5DN6XbbEd3ylpBV1UwJVa9H_coL5IQxV3hIqX0rTr3nyc3wKOrD__r8rPihuKlwmTe0S4q3icnjdDXwGR78k7bn1PjAXTjpxzuTAEgLfhFVFYGaStiL112mXroEOFeVxkJLhF3C-4HLkMu7T1jEnAAi5_jd9oTGl28p1nM_EvizrG3RvMB5evdii6VS1BDg_fgFdU_zgbGGzPIv8EpXyu8M1qcgJ7axAcd9O8da_TJ1X60bncm25C9j0sMyguhsPeO8UXs27LnWdb-UaGvZUqh13T5CKWOpDr2MoToFS_IxrxWg3tWEnQ4f5wGTkMzGYWs7rEx4x1WlLQq4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 864 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 818 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 758 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 945 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/volov1B-VXzxURzm0OL5DXuaXBqXREavRtskad-_mbPzMgsW9_w60q8nCe5YZiR4h9iemPbUkjNwt3JECc8vlWJvnauYpPt6dz366cDuS0YSVRBnj7Z4zaz-ta4oMAW_GFNOPgpmXs_wAg4InvYiPaue7pkXRd5d8FQM7Q8MRqVivou-2F8D3FUrZo_-OwRrJqB_xDU5kXdJdbwnfOIEBK7JdLucC69znrm-uM4xYtJ_S9y06cmMQybGoJvs4p8ESZA67d4BqDo9LFRK1rCrcDO62s3s1keF4735YdGVaWimkD5CSFGoJnfkFN2ATR1SqWn1HTnRPtcFVb5RhPzSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 999 · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcpYiZ20_TGCdlNksCfLFZPb40HZz-nSPrQiul0fsgJJf3MOeVwUqbCgvSo1Lc74Tybkb-LXuhQAO0cvVmgKI67uSCtK8WWhPpPjCIeqwsJPPY2ld8A3UUatKlbtRApDGbXlu87ba1Jle_9A-fpd_bmKOLvN_h6xyfpE_0pZwlyUtyWTL_fumDy27AuuuqdeHVyP6f1IRHo2VIetRbXvY6I3WyDO6t_BbeFpOAsl0a2BTLah5SYnE8aV88N6Vd3NVxVb75EZMymAnHDRIg5pnUrSMe7WwTVe3BkdgHgt5z7mjjTdcgONfH-5jEJHXca2pgywVdJyZh_79m1-Dq8ONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKLmcBgpevut7VLkk7zl08VMDRITqn3bvnrIYXKqUCrI7TlbX52Bx4f1d6xmlTBWLWdXjdc94oVntOROlC0g-Lt8uAefvvj6twr5iE5rk-dY69AuJHoZbgN-b5VIJN5R4VP1-C6REMNlRqc4udqW_izmA6pO4jpCnPq38Or8aK3p8iyZY1WY7xJGclYZZzdYO2InVEA5V4zI1ZolzRCJPt-Bpjg3bKina8Lql9GsPQyt0TuL4COG8UJOV_tA6mZE6ZjQ0-ozwIerDFR4kGhAcWbhG0PXo6aN7FRjgwK7Sp-Ddm6l_TybszyzzTPV5RHCrcSLGnJfqjFM0pGOyqxrwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JETNup313rrOp08zROSIUu_22Aw0IUWye3mmvDadjWla5gRBTXfFdR643jBIT3sBJK0oberPC8k29QVPLMgy1lzeq6j6SA10Wr9TL1O5Ec7gESBfBG4CKGZV2E6nK5vKidMBruBuGn663VdD6bTJlhnKdS0av-ADdCuGC34j06SRNhMgcMHu2Q5_QiAHSwZNuuexL2ele5C3tyfmrfn4a6sH-Ja0sqPPhZA6aOsmGGHkGrNYcr4u94HZucFDZE0CGU-BO96CozZGM3iRjhV4eIBPLkUavlRumqFQ08gJ2Q-iJA53lG1Z-tpk4E6yBeP-bNAPOm0Pz8NqV8eGJISzmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqd14KyLLYs29uHvEWloBRrJ81iA9YYWe0DBAedTLozBjz_hnQZ3frCT5MzMNMIuTAFMlTOmIwtG-YoSdWQxzTXwP_baMFGw9ympEQhqt-0YlGzxheE-Iah2lqNZxmrpyo8BEtPFtAg9FzgB-3TEVfUT2bJBtlzNUoaLdN7dqDNQb3SB4y8Y6QHJ6FHDEQQBSDLWUtJXgSnepCqVvpY4ENgxU3wq819eVl-G2miRKuSscA27z6YltIVr9nqUYdb8SlolV9st8tiRjsB8-wFN3wlmiRRnQkPJ4FNk62zVbaOu5K1FoP6M7k05oR0-X9yix0Wqfjnxvi4IqOGmH2ZRvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QigH5WhfVFDIaYGk7OmxYjJCqTziyJImiOwP4eAZrfIXWF-Dy44S6k859EG83t-RHpF-63HxMi7xEcValFuo19icJ3rRGTtWZmNmDEwEuAHXBqd_Q2m82rYkT_t3sH1hps5oBgL30sSMiW1HTGY05h9uE_n35oIwyoKbUgRc1TcnLPrPDpFzxOtkwDqhzotl4ItOimClEZVp1bozC9oc_uPJ2RQS4k4jxOduYyDfXU2CsbkLf9n119qkg3TEQFniGtPHhJ3tLqcpn1TsMZZrLMlfsHvu97C9DY-gFdWiIAouSzm84ztSKXlVobPWSrpDFKiPgB52VdGfkcaZ3y9zMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWQ4F4svKClcv6N2ln6qDoiEoNdvfb0eAg6M8ojXhBZKw37cbqR8esq3bVxtr5Uv_8CEUwgDWDiCWuKa35i_9xrv2ddq42ilRCVoWmpxF9e58hruHcPu3uP2pQ9lcs7AZPierAMiTWnBr_CWrQqnsfiuPyhY-MRZhaqAoKIJmWjoHqfexrtQlWy1EZmMbHvtOx5EUR6yAdMTFCen6HtWd4fzU9Rmicq8SRXe-ztBGVWvzqo6Mm8Bwgy5RMzxzW-IXR30eFhUXHUU_m6U8VMXwVulD9lRWljHOZ0uYIkHBvIsArIK56b7PRuPe4kE0Sp5kmdCHaRdxON8XKGlR0fpzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmQ7a6O-7CltxbDiFveXJu1LoE4DOvKeIN-80xsDqS8Fw1mV2yUKHimZwvtEDMDpMj-nKgT7ZGnng_QiJG8HUjhzljfPJkOlWp846TJ0AvwriJxDK-3AO9hcyJLSpLpjR423uAe-kouEg8DxkmQ4ItvViYgNKfhA3fYNMWo_pnKPwp2HnD4SFp40S_aKS4lETzy3BZarqK1qHbcpZEf6u5REojiJUHbzs_iovk_R0LzJ2HJByMpeteuyQ49OZGHpSsPmycNdrEhdZILDnDz5FEd9iMlTDrVtKiJSCACrsE7MapzdWUCkpvXUz5ru7rBs3gn0t0XNM4vRogB1h-W_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iW_9DLqlnd2aMsoRbxq5SMZCkpp8HC_5j7EQBh-i2gb1nGiQ5p9HenyNIXekLxY-CspwIMGMSLf5OwfRImxEFLDXtSb-kweEenafwMt1uMFII5uYjCYlWgepu2bReEyADwPSrOk9gZ5v0C1o5pkA7ACow5DK9sE8BMtZWmlM9179rURA2nQ-80rCs8-b_P9VuHmh7oSsUJ_aVBCjkUm5jprdgnxfJp6aZAGAyvYKUYpohwfgWLi7reNSZe8_Sm7WuOltVpM1CLLkAPi7zyx6p07CQPiB57zh2g-e6-DWHwWsQp2WPXAf5jcMOiSPCx6Q2fq3mkvdEJWLc7x8DH2njg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdOPgS10qpINnmOIG3s0waUawGoRpMtcJWh8XGV4_fcpVLoy70uWqNoiTKteagfKOXKnSjtFz7SOM5frEe51cBLJDOH4l0CO_L2WUCZNBJNYwReqtQpboQsMK_IQbJHc7hFl4LAfRO4ElN_otNUiXkxtgy5-avEdp4xCuJ-0-yBwgvy3-iYBmko6mCKfv4x6tJX5e0jcklmWJ-mJaLYq1D_90FXI0rfKZLaGx_RDiONCSZw7uZrPnzoFMO0B1hsnTkRgrtzFybbhPULHl_XpWPlDVtiUZBTOe3aWv6mB1Uu11VC7Rkl6ukinjteAK27v2DeJgl-1854uCSnuNlmT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flk5DXinZS-Xs90WcpnyaraqOqSgSVarcDgtEgBKDSIlXbPDmyExVXuW0-iEMExMZQQO5v1I2PsbhBQObywbsu987mEY23jPS0XrsJyFKa48uq9Gi4JbwkoA2P0hj13eRGkN8SnmShCx40xcpM0AugQ8ql7SJxbqVHKChrtXrB1ORKHbleimfWJq3FCKEV4AXEiKncoOItCvWPgImfrgHmzbM0DP_GtPInANGqbqYjVnmTxaha5wfFZ3k8AhWNgycjw9nN9fCrTa2OTk3UGWH1rbG9OaBjW9C3VL8MyLgelLv6xZD0JQO7hvEAyscVdUTkGYGtA7njC_yUW3GzaBRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 948 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDw4VFd4A3-OGxM58jwACY9SkJ1OgYBSjBVAWXc51-G7_9p9FcEeUSPUtWN4WLIfJxZu-kGpZobjyYHtLLB9B-W-20pCpounAAvFy4JDmp6SSh4oYONe33pf269hUAiqCHlqIe1faR_f7Vx-VKkdlk1BBlpCJE7cDcCBmxEVwWieCPUanHd5CvKg70RC_cC-LM1DPFv790nj7wt_GCNs9fa46p7hXh_L5EuuYoZGLNHU49rh0MjQpjTI0T49pq-Pw6xQF97Y08FOIShSiFZfSloKt6ZFiWG6CDaiAk0SIMZLD50s5bWzhhSDZW8DnqXwzTH14nfnZltOj07HuUufQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=E1HE0s0oRzkC7rr1nTv4U4IuL8DEdpqtzVykFbm7YtDBeDfGENQMrrwFoLPYstR3SFAq0wmUMQ3wxQrJCIJmoHXk-PYCjwtIhowJ_EVv7WggmFl74zVgKKdv-LPtwnouNX-CjwvcF-TtPT1ON-nFheCgJjWQ0_QTfN12qKhEdi3seH57wnWS3Qw3-8S5YgyE0DdgfvjODCQvU3NK4y1PndF8pC8L0K6qH5IFFo6LelELD_aZL0eQsRlekDgGFhUwL96GJTYPA8syuvrM_9ZoHm4EUvfhP6Nsj8qNdHObHXc62MhiulZk9qBiRvwTktvOfmjp-cr0ih71dm5BXtrU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=E1HE0s0oRzkC7rr1nTv4U4IuL8DEdpqtzVykFbm7YtDBeDfGENQMrrwFoLPYstR3SFAq0wmUMQ3wxQrJCIJmoHXk-PYCjwtIhowJ_EVv7WggmFl74zVgKKdv-LPtwnouNX-CjwvcF-TtPT1ON-nFheCgJjWQ0_QTfN12qKhEdi3seH57wnWS3Qw3-8S5YgyE0DdgfvjODCQvU3NK4y1PndF8pC8L0K6qH5IFFo6LelELD_aZL0eQsRlekDgGFhUwL96GJTYPA8syuvrM_9ZoHm4EUvfhP6Nsj8qNdHObHXc62MhiulZk9qBiRvwTktvOfmjp-cr0ih71dm5BXtrU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V76AuF0RdZPIDwsGYFA_bm3avwjFTZ2RbU7ocHjdhE7ucEjszTg9XMYjMgI65xOY-bjRkzmS5FD7gwnW_Dv4BfnzGXzUP54p9gJjZQmYhNt3c65Q5rZdAboSLP9RguyBonTdqyYJTmIkvmI80ydaE7tXmYS_wKi96GjWErJz3d8BQzhmGBYitlqxFRpO4eTiPXdcSk9xeR8eZDKVXYSBQ-TAZibxJza6MfJaVoKIUb-JVIfS27QFOs8-nL-m4uIkdKnFiA9GlDKL8MhJgKmt8khu6AtewuH4FhFVDLrfnLDe6o_nCzneZ6dFzQmvDeA0fZctu4yOa6u02-Fei0518Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZSJ2l5Kg5Wkd_naz2Btd6fTUXL_L3Re6UJtLN0TPR7QIfN4mx8Tj4XLpEdfJ63DEzAVt0vWMkXSGqqlKzqjyiFLAFqx-ZeukF5EBjKSGGwzLu9zEmPw_ZVSX7jm_V4_SMDyMbki6dr-oSF1rkNNPicqCTXnT7ri685yDUAotuHNTqqjbNgRYyA3r9cqGGLpo4hvmtnH9zbJs02g5hjLGlAUSyjgmBcWhh-KSgoD90fJmS5pUOKjePb66W-7vm8mAJ18jLhSO0yMpw7kN2HbMe5qTfR15CiXFLqnompFnL3dZ7HKX09GiM8Wz19Vs1p0eH1HV-B_KDe3-VErsRZQyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFDNof_oxtt3iaFw2bZexUVnuHTem2Sn9Wl2B0Dkm0mNtHenSW1k-U8rbvRnOufvqnwqyC6y-Z160KklP4TJcpkAwR3cbzQpje9U0YO-aqu2bww8vTkDJmIs2J0bZxzcKHL3L3LzmXsUMQf0itGvymx4NO8YOeb3ackl-765i8eyuM6rURZFwi0zmfl7L0t4LSMNL8j9TDj5hf6PCcWMmmWeS_QaAtOoB_iMk7kUYIbgNYWi6niOmwuE0x0XtfX6psZVGRkP0O05m14xKkBrKOb-5Y62SkC2d3IFaHxfeZT1K8V3pZb51D-buF8Zp6pkts1uLRZoGLHnDVANgdA3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uh4knBlas5kig0_eDUxMrpSxi5O-kpvD8n-002VZ-rorHv4Z-33BzdDUJPMwphjx-ITTRUIVRwi-3yffQJVCxieaH6qGqBo9AwSFIi4cE6HWp9wmpytfgb4G6pA3MNpRsUkqfvqfJWeSgO0bDt2lPpmeSQBZK-7eD8SYMuVIhI4eb25ty_QySxpT3RdzBrSaI1naa3Y8qOGWiKuVbzPjzSzvg3bjKqhVZeommC_mqzRzgB_HZ8-oIFsbZjhu7QhFzAhfBIQvJd-kbFKGVfwkiLoMWkZrVP0FuWV3TZJKjttwiwiB_wJUu189XVLBxrmKG00qLNFfqgpVOqq4R-hyVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaqU-0_AYZj9SmB6CxVQ0NvqFFsQuYUOUo-UL5L1VdBo-L_41WJKInu3r7E7El5_N5RAYUBceis2W7ad2bGpofeSnVqJ3Ttl4ifoIT_ueKIiWa5OoHTZqC83pxTmF7G9u-VZdN14A2LYdhp6aov0dieayTOaUOXlxyk0BGJhMVhf8_RR-QI-Bv0QHIO7kgAx4aVNkockBe9CzMIOIgA2VxjPouJs6a86gdg6AIY6w6DdXUq4B3oIBtQdK-9Ec6JgKNL6SwB9H9Zb8HPuG_hZz6zARcJBUK81GbLe7e759_2dQTyhxN5J4TBRH-fBMMMn9jg-aHcMv38qWdargP4m6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmVkejrECs0eqAQkD9bcXyTUtbZ3OgCXxIvRQ8MKkZvLfN8e9Ot0GhitttfT5QQ44KKDdCWP51ILumzjiWzToGwnZfO0GX5S8G9cWWreR5aMVsUZlJ9zq3wIDuSn9BFc0Kr-9bPgOBiF_9bVef-ZBYrK1nM6B7wtP_VXy_zqEQfSIav4QAHeGfVURJn-rA2Mh56DLbHgQRUijopqHaimpG2MxUltHGCvbu7CQVGQcHBAeLuiNHV6pSP47zs7ptSxLIQAdIXebYlqbE-NR1MVbTSI8QU312BomMRbRXCZBlzz1D92baDSMURQec5dy66JQu29G53wXLlohjmF6xsXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJCnro9YKgnssKkVQlSyItyRYoT_EYFIWgnd3pb7Tu7vr52kJOHXZCEv0aXvKce1abSUsfPHjH6Mj02lo2-nuzpTQou_peb2cUmWXeSyD7UTJwtnjkxKn6jz03XlXusnP_P8CualoXuBfyIo7VmvNYpNIzwrbp3ss8SizNbSrULm4pah5-FkW102jY9gUPTFIAXQTElenB_Upq9w-IPCnR3MQ9wYGbeRgvRb1ZFNxx-a_2qU2mBlc_Nx3I-EU-ETMvRHRLtL_4xS36A-gviO3fs3O2F-Dfu8oT-gfd0wytoYINzyueVJ-SYj8-ayXJZ0YATXpqvQl0UoqhF-9T2SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FA2HEbw5WTSQN7Y746-z-B6GrwugJKmaZY_9WcnxC05qfQkfT5eq6qMRet4mC9IUJT1zHeIaGeMS9bWgbPm8d8TZ9wqFuxr4QIn7ZlXXalxsCfILyefINDqPq4wosgzpiTybIVW1hoi39LjR8PkG4I9gGRx-IXoG5Gl8WvTls6hjQVfk1mGe_ACnuvv6fU9it1y7W057ZVTKdqRke0qglo7JSJGdSNoeH7Dv1Dv8GnifNKPV-vNbd56Ivww04nHd-W-YBta7EQZ6f7QD5UyUj_WuGwMCiCdIxuZz3qdvHEnqgKlfR0o2kZvuDc9lx3F3oIQNR9-CiTSfbTIHoDtG-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8GrenZefRurorZPD_7r58BNXQ-UtgThPMw3QW6vI3LVCko28qHTIBuvLtVO32YE_x2J0ga74vXoCoEj64YfNLcI_U2U7hB6z2wLKYTFCyb-7tPsoPcozoo_B77OAvU0DG6pX4Vh70Rm7llc7xRdxJCA9tAYG5kKiwtGsG6s7MXrr1ABLNWB-7CTy4E8k3u3H5cZ5IdjR2Kg1RYbRsap4zRLf5uF9H7cQosQFPk7yCr5vLA76rJFl_1TkSi7PHe5KaucarbEymkqV7NKzJk3Dty1CqLaX8_n8TYMeLzYrp_CG18wfHwR0PFTCyCcxoV001F4a-xEQquqEvmXEI1t9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3ra8RpT6YcfS8bZ-KyNpnhkOEmWhH1N3X3AU8NRhO-tfiCojgoYphX8bwMDpwRo4CcOe228igUWwD69FtzpFil_s2Op564tOb9Vu2cuodkCjQ3VR1Nh1Lean4_HeNYSC5Vuy-rjGEcECRcm3drjZWDgria0-j1ppPIKpf-9fwcGRoBoogj-L3lwJqHuDjdAKhNbIB0XUVTcgW51wAv8EDWULsM38MTWbrQe8gJaiBHttElRPyI9NNtabTEfDd4eczrBA5Tg8urOzv_v1ZvqObDOz2KncD1I_7O2tspnnrSoiKEcvw8K8ek3OXe7R-AXX4sWXqbnQhK6bS4yVocHLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0IdXTyqBaj4eUiuGg24k9szyFtYpzXPbEv2RJ4Ibg8f2r2YR3bszmaW5noC9z1EGr-pdMY19ZU7hpmU5Y_FHkzER21PRDYQbWSSGOhIUUU7pYCCx7QrtQTUS8I3qfy1zbwhoFd1Lh1gZvBOPumROr7UZMRdXDGvefAzELVqxr9eNIIYyPC-KtGHEHC-D_WvlExNfRUc5ftKECOp2O1uwJT5wOlTPFmzDrfetYV0lq0Lsfh0cflD-PG0_Cmcdyvn0dfj-Rzg8-H_7CIMaR-1EtLVNcDhPgB0HLlktshPmkGyOoTe_2p0SnxXqD4Zbf5qWENRFTM9q_WY6BG9WNEBMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJkdrUB9atfg5RpfxruXoRQPl9Qj8vyflSCsU5MUlx0NkkMuebZYwDLezkX_E6ebsLSeT0pxoeNWYUYpabOOlxREUG2HHeOU6N6CgSIHw_F6Uuy-axjLqw42u64HW97sh-xY5Y1TBeDr99VZmzLvLj_8iuijxINfznL0OMKl6BkC4r_AYL1u4ZGcQgwOGkMv9RhhrnyhoQODLhQZBSHRXsCTQOZjGMR8NqS7fOdg6a2_s_g83EYtkMO6NYrw4dFjTeVjYX0_-mE6KdKoVgB9XUqjja7wk83B_TgbQ5DgEldii4yIQoCGN72WW9vrHJdcFj3_58nYc3QuJfme5QJ6Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ct2eCPhCcrn_Z1B-xkRbkQeS_oqV4JZQNMIWvhYeF2C3ivQV-p67BQzgzyjPfl6MG3OdHqcrbeVGO9zwtzRsmo9CYfwUO6EUAH49IzV_tQbm-DkmVtSFzo1GB6-DAAs-AKh6f8EJdZTJ5TGM1mqm6M3-R4PP9xm2xQ9KGe5zCvkzAoVRjmSPfCBNtMIx2_aIDr_WV6zxXhzsyYPkcJGvFfmMncV8TqmnxcgYFOzqAlNi3HCNTNiGpvQzRfauosLB6AeV2UUhGqUDQkdLH0j6afKxjFy79BaF1a63pIg46fsNYgHVLRz0B3k_44VbLRiEcJEBEvjIYT2wvH0FajKmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBB-v6mdh-lcn-gEzn8wRza4_yKFK0J5Ke2vuLdC0L1HSBnO4oMoALYgduGlQYvD2wErXFsY7eBXSPITPMrolFQs-rphepZLHW7GXgReooWo4kuuKCEge7G3_8s9Q-6-IrTmzUsEygdme26fIIuXMxPTPQ1pMi8AMIgKGbtjRPCAA-ij9o394Al5n2g040W9nTiPC8RxHV4zs5Rml4eRWvUPdEuV0n18WgaLGRu_xJNplggmWadd-NHTTd6e83vrm9DHq309sZ93zn-j6M_x1SKQEsFbxnRDyVrZ6JQOADzkKdNc87QFYwHInnxxHEwkNNPES7psg80VQsAzrjiRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8N8WsMkwWUiezLh8SChiGExKqrXlAeZn7DtCYWYWFka4ijRBWUBiEemaipEzwtaGHRZMCuBCZqKrWuYU7l47OZK216dof7N9-m3dAGUTWdTVjxV2leE3HCsm9rg6mdp9P9PMT15bLXZ73wiuShlkgjQ5qY_o9zcn0UPiFlg_ZE04QZ9O-X0JsPJ5Wj5BfSET3hg0hXdhMFvAys5YHLhRRScHkmKxSExTBzgzBp--q-qRyni05OamaFJrLj-jNz2A-gA10xm1ofgPnytIa8HN8m0Fc2AFoimH2XDd4oEJiDN4WapSFGq9nKxn4Q3Cfzt-XmFMqy4cC01aPNlyLznxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbQd3M94cr5t6ao-mOLy_VXF7-QFq_G04pQ-bj7I8Pfp2cqj8nXLa2tH65nV2wywy_axlYddKdddQONBK--Che3DocMxhCQyjVqiIQiQ9FH58B6dccqndGJfDO3qjf7bpkNlM_lW7jfvUVdxAeyhlCJfrWn0gmdTrDL2FwYQQ0Lp1IkV9gKlil74d8S2DOXxteidG_-y9vB9i63KQf9Wepb7f1EZFWGNx4I5uGa4FEWpblBV0R6GidaUcQCu68Cz2enfwJj5Pom0Kxyj5q_gVAjm_iKLnU7KzmMGs7wn_FaBPxDgIdfoCLCzySlvwRVoqegwYS9-1p13RIpLitq51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1SjxBMC0XcvZK6membldNPN0rfZ5wnK9sNkyBZ1vk9vcCOPLWBNaFww4GgW1_v9LzMu9sY7cmt7uEVwiPS0Yew8L37HPvDhXFvW8bkp9ujrE1fpukfYGv0qAwGe5gK_fA3uzZ5pXqyCgWihDemkNflvt6DZeMTIn0YQA9IreVaSLXD8ztfd0Pqy_9MoGPjCRMtH6-b-fs6EwY1yXg4b82UlCfb1OYAvjh8a8JrRbBz_dcvJKhQEhDIrOQee-sOHmz1irE8sJ5UCvFxjO1JAPslgmLIzB2h2ny4Y-W_4DYALv5WW_z9oA_jEueP1NBiNl4ryFyIlXBVDg4xEupLGRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd_AN9CdRSLi5USPe4byWV3bdhSr8KNhN50Zh6MJHfGSKvs5YGVt_l2E5UC7__4nfl1SpkDAHTeYfDTALdgLzBBP9_ZCNl_f7ajVHimv4JDkTBb_PEm4QUhsYGeSTjChgQ4kabWDQnaSqYbrkz1Yg04eX1SGRtr8p061aBL0vUP4lBeaxR6xdK-9ZGJiPRvBxE6a1E4xLC5e8hRb1Od-YGk_1bAHfxyet2bvKNCrFVbJx_Jf4zj9zgLn-rUFTQ4YvAhxSBmoswvrfb6B6ChjnesgB1g8OtqD3kwrfCHf5CWxFUzmAMN57wPljWAOh7XoGIel6IZiA2e17LDJfwntsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je3l98Ed0FWC_qIXYcMv3WISITu1aDkdvhXmGSqHi2ddVfji4j6j90PgWTTiDE2bnCw2sm7tiXl1dcA5_8ESHdziMQFRXiVnyGspcaS_nU82PAiUc-RfcZC5eOoqYmX2R9-FBsaumRmtH5SpC_prRdRq6TuiRvUw_x5AK8hXFI4xju_LaLSwALPQua5IrvBC8m71YOkpHohhc9i2ZcjKsxURxpOSYxNRPAZT3LnIB31fRq4NZGpkD4CYpaMmRCp4HRmba4rBZ7WL_JmcAfoF97M3nwyPTX0dZcPbQgJXh2qqPa_aCbeIHFXqCwxcyE3_HV4Ej13-TWWkf5wLTqX1WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_LX0_uujwkhJBqUBUtUgK1PbASBC3c5Ed7m0oM3HaojfgzfdXLt-wRBb_Ki8XbSwtxmAhbEjKGOfyGAM3JVJ-qqG5OWxkvvxPHSA7SAhpbKIyqlwvElCbsOMjSP27ZIt0ZiGqShmgLq8h4hX5-nNAJyOz7FCwlG3FV-bcaezkZXVv7Cxg3XVVjdBBio1oDc9OsvBYd373S49DozsYs-MfGSOPgy3Byd5-3T8nuDVm1N2w7U65vU9P4ouLN0H80MfAxwZo4wb5e4A5kWveNjtiEydDSb_GqtTGiFRpY_i1LbSRBO5yxj1lT_i8nukTngkWktihDGl29wdl8wh64yRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y54zI_32dNvAXfast6_EBK6TE3nS7paOdP10BVWsANehdymnKBpP7eUxujNFtX7nfqoSWEg0Nvq3GMrKUyg1MteZE8MgiYgXEW1GM9vhhzPG4hfnY6hX27JrIPJNRw9b0RqviV7E0iD8vv6Z1xuhApM3-jOcMFjYDzoRlO1pfga6B1zLQ3t659rKS6m6oXhj_0mue-B7l9qhhQibndapf1FmAfMayg-Sb216R-cWyLktvu0QmgjsCQQ9S5YyT7QuajH8NuGtkTbCdcmFPXCmp5ISW9LQRsnMGyaVGf_lrlIX-ov9iyFU17bGky9v8mrjQk5RkLaUkuA8n523hYaFxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pasj33E9mpgO2FIOl2Gv3EPGgUZY5DPgLVvI6VM9M342YBpx1PMEiRsTpj4cm5zcTrHNq45Das776yt-Q0hJobKufJohNC0xbgiXzQaghAfo9mXRwtShUMKlFjzSAsRrslHTnm7hTBS7cUdhrZQNoxql7g--o-laKfmKVb2P2BOTEG1JttWrT-tWJWB90hv_ys_eTGcGG7ZK9XXpDNQzehSvuqPBeINxqPuZFee9JeUocP-V2yXtUM8Nvqw5L1_yiDu_Rnzt1E9YJ2GECnLi-_NpyAKGzGF09nZ4dmWP0hGXFSr-AyBlejeZzN5aspDxx2VUnWAMY65_2WJwELfqzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWI2NT_eby_Tg9dWcu4Q2NJ6pW9RoGMOixuCHW-ENWoYOgTvdBUtJNBycrSqpr3kMmbEnGOvGT0dDyrX0wZin94UXkYZ5PhZh9kgGVIoI2BXzeUFzWkxOWxzbtISGVoU-kGEgDaX7424ipNnHsn0zrwEfQ3o9UhW8sWSfYdqOHfKY5pylXVRb2-yFQbkC2gK9yG7_gbVdPC781TsGdAVHigszebEmWN8a2WCe3R-8twLkbkuQ_9NACf6-t_YVbYaxmhZoUs3QAuXvit3hJ_HDokK_An0OOsH303NoPoPnFk2jiD_klgnEtlosyq-6AOWMga9k3zNOtfBww8VhjLB0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7vHxNJ9FyQzc2lqga6tRTklOuz6xD5IsYWORyayVX5-Wb1FFWjeGv2V9uRHkX9UMmscGMuk71rdxz1E2gvhpEnxj1XUinAcjqlkcNdxfYsWwIaTQsWtQsxXewdAR_rrF2wt6w_Ofsii1Xmh2P9zDb4PaJxCFSctdOWq9-3acN00tcAwHf6642G9puOqAPoSf_84xyILRpzHjSgvakxsy-VC0d8wulTDQOQ28L0QYCi21gIyh6sPU6VJyoBdGp4F23Mm9z3cY3TDbkGqYWgWAvXqL4qXWUdrFSTpjjgPuZoNLxca3IKA4zYxURLe_Yzf8SpQrZYNpv7wYTa8A-AlgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POO4AAHi3pm2thUgNkfvDendjictfjIhxnDqMIE7w1YbzsG5oC0uYtJZhzflcSbIOAikOCYroD9J4z588EHj4Wi1dizrfQVZwUHdiSvams3I61RsNZ_9rX8Xhg8cpnlYpIOTMV8qR6PXseDSclcPXYfNP661GtRMhh4dQYM8j0hpDzpNk7YoGMZr25gHHYOpREegcmCVC3PAcNq8Q0YlYGW2kmQ9orkBySZu89u2SG-xiPQIMfKeQRnYilODcNTIuJAf6Y7R-2tn-dIc-5R9e-mOUR_B1wAi86KxayDY30pKW28yUl5kTyUGigl_t0qzupQgutFEnZRUMU81bwsdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7XkP758TbRMYPQVpCndluPAp5ApcdTe8-9B-kpKE6CHFAPbtIgHa4bNuWGCbU7-1r3ggtCNB0lTiP7rQsQAy6botKW-6ZaOFFKkJG4nGhj0JAlhtsNzepYrxwf4oaQwUDRVK8QnWSPW6FWjgFMBh2HZ-S6sUSwFpMm8zH1cxsbdCL3i5dHgz-6XYzrcvk5OVKTQV8Psdy6rYdzjlZMji37eocwM0NJLAqaLT8ENAvSL78-WwHAZILSDDj5MaQ19TApg5Ed5G6q78rJiDyZHpO_6ZSVgT2Q_UVlA2Uo8zhS7wZCs5zq4XzZPiyVYnL47ocSt2YFIQec1sksZawxkUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6sAwwPBmm_0zRh0mhzATEi9YiYD-UMKN5R87NaKu4Nd8u7PHiBRAD82br6JnSrkU-nOzmt3AfCGAp3-_XbzL4fQF3hSrbTa1oBvKiQDVsf0K0HZGk85G0Of8m_ijWWmntrqduF5wpGLPxd3WV82UDs2TieqPBytdyICyt6XqAPzZMbdIX7tZlRkYQ4IeVA_TmMDTEFTewmdjRy8iUeBH-sJTSyQJfmXfAtyWYFTh1XJfYBuY7T2WY2J69xjOhRj6gDF4W5XQTWHoW7gSNxh4FHC2bb2-JdTWBsihA-pK8addAeBgP4El9sgS7X6S-7Od8qKgb7jSPung8xNLlbb4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1kziiCH994S9KWqaSvbFftqf9IV59NZu6FyxNVOhouT7eKmANAG0ZRsZ65XWJVF_nVyNLhGKM3U0-jaOrWYxjBOtsqY7y1nDuXlTx6fQI3vHUpvxj0rSVTZNyyJHfgnk1xrj4iqmdnXlQD4D3LSnTwGQNmVRfYU4CxW54CPK-iaebi76WdeZAo78bWgAcIQHXxZYPWRSAf4qNNOif-li465r_ZtFigOYd4zh9qa50nafPxFx-ht9GECODoGX3MGR5wqa4E0K39fdEd08rRhPzypw2KiL0K1m50X3kCt4gGbQYWQXQaY1Bt89HrF_DDosvgpvP9LlZw2Ur7yqAH_Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWzfmSwofKKlT7nE8vDwohvFyYs6wOMCQHRKfdiiVDxv3HGk5xr25JukCi5FDMhzsQtEftFr_5edj8hu3B6eaMh4s6-eShoUm5rLQpmJNK6NLSQHxt-zL3cGK70K-6JlfR774N_KOf5anAMsrljrRNoDqKQlm-nphL_TdD2BoOemYqCp9FLAdlkqYU5et7UWlkkQ0SFdza_JFajbsLP4OGcL51SkCOQuSzoJ7mBg0eJMs3yETIHFdkipwkDT0vSVws8degNAfyt50ky8t3DX-H23Ejrzb3H2Z7ikmSV2MD2kO2zSoz823o4mflR_8HAjZziq_69hGDOArW682J8hmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX7WqDRRwxgdIw0YHrlhTUxj89ZN_5SUOf1RvYUjhWwSoxrTf5Yhdzg7fqNURTKFjhyoTZl9Cfw0Re5oiSxMN6nE1SzAcdFa8SpsYGarCaFwk85NWwt75p6TUv5DzwJu-lWeLKszmMS6ubt8CkYryx63QKhEqXfzRIVtmH-UqPzF1wMFa0HifaZ7HsO1QZgN-vfsSzS6zRYyMRHNPLF6JUSEN5HqbM_FSPWhYnSoHIa7VhDnyPRxRmfRWl6D9Di4rKg4LtZPQTGJLTBtSYrc5woBWThVtNiLDA-AAaG_u3YOd4wXSit29h5eXdYXEOOXaXvz2_qzy-poLYwKeLDf7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5oOS-WnbbbaTdo4yih1aNmhXRr9A0zCdmNz4SCCUtXR2y8crH5vYQeJUdsclQcl5QGAKHsqLQsbjs-GjYgpPoVFIXfORqUgxhR8YWMzDCvvE-758WWxiOarh2QCmVWXhaIgjKayeiB_Y713eouQAR4sjdAHTmBQG0Os_lTc3qEQEyYsbFa6ToervbEkhDxdXlFNXdmvnYPX64HW6XqQv5VYJ8FLJ_tdsZ7rCrQiP0kDsmb1-r45mTpzlVYM8YcyArgbJc53_rKgHFEucaRLkSt0FRjr0xGVfmzJb1sxr2Wgrk53M6ErK6BUCNcePH-IQLw5v3QC-HsU9-dmFNc8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCJ9tk2MgAffv5_xDFpdBkppB6uQ4ZZnIhukHGViERAff8yg7_ly3-yG7omZG-MeAb9Cxcg-vEtimG_Q_z85D5bUhZGe3e_4ES6ZCYtiKLkFNj3MO37QCg_w3-yVBKjG-EbFbMChEw8ypGEJRjpW6SV3EtN-vL7c1WNfQ6k_mYiasoKsQpWkUmDjAUI4je3XHWtj5EGisiXn2989jgwwVGf8o92Y1C2z70zZxkLP9F_H5ptAFj3YaZZu4N0IsBCq7U38JmV8yCtNccBpOTzY_ZLKDfOvIhcxzg5l8_sD9RAThHcpcsvursKRAU7odvSRVr0r2icFqcurgJ0mAexYXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYqX17yEtPsTazi1o-j31X2DqvhUYZI63d-suRtWOuF-jsOsIRwA1dlkg2oG1mfOHZfTOtokcBrsCM1MrJlmZLUOb_eNLeIlUMTn442gEghMF_TVEsa46W7iilKYjuoyXuGf48QJUF7YGdzvQmJPjOyzzKf4ismcL-hsoPiVgegCmQlp9i64il0c_0bIma-9qY3ntFfJTWYfE75HnLMwUOxgyvCfMqK84HNxhmJiyFWqwHqsJDc6cama4l2y6dTrCg7xJeCIJyxA8jFJxm1Nnq1pV21OGQXxysNy5UGI6PzLdyd4EEAHC3w5Fnk1C5uWgKNt8oqq93Zsu-MHn8RT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNH7SNxhdElE0rk-g-FB81CoLEQ0UrXtDQtpkrM4sZBdk6e7uOUGu3puIQeQolUoBtIQP7jdHz05MY8ShuPnxJHV5KrHj0EO7zg89f4G5jviDUbihrC583A-VLu809_QoElTMTUlZW0CCJLh3x8TZJswbXe0rllxY5BtuwJlPTNLHTlse_6vopscsofKTtwQt502c0X7d8AAZ_pTeQDW-GcaWNFZ27RLexsYzqtbyJoIMeyWBW5I6fsLtPeinITKDaSncDmrKF2BsT2Fuk4nW2D-bfddOR6zrn2a_7gvniGUW7Fv9dNZt-jtRu0ixFwMBo8P-rW9nQp3kX4UbzBbsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRxzmxT2_MUGHQVTmfkhxB00UdNpaf71EM2T80CToGz1CgrCfeian-hpCWP1_x8igLIniDBsAnkGId3Ru72wHV0qKO0VpZ4l2a5NdQGyA0E7bGMasSrvImk8V2Q9K02lS8KA0cADnRPOLptqkqOa-t8mH2_kqHY43gtU4COOzcsH9ghFNSyECZWM5mpoorNJ8ZEpGbBLkxLUttzdVBZPa2t_b0HtELZlwgjjggRVbCLWRx-hDPgTQiS-HNa3qoBpxHEx_yQm5riVsu_tpHaoiiroM-Ng2QVHuyz3RJY2ScU8l43Q2zsCHtDB59u-Z8a1B_LDW9z6gr5tprTcXP0KQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RW8-X0IiMLiFLkG1ca8oDqODV8zjPLZug2U6lXWXnA7GRcKT803eH8khqkP_b7K6H8L1juJeLveLO-8yhsp9H_sQPZ7SAUVXcYBGuoJpgZvp1HJl7znlAa8T3KmrSFj_NNARhC4iE5QgelaLoiOMBwg54RwM8tzJzT7JcsFbsU52nh9AwiBmeWGqAcmH-o_I0aY14UUW9cRIanIeNQ2y_wXAiHl5njH5XERJO8tYA1tuJAMECE9E8SCedR6vPiBayFGXM9r021Ie0MX5A53HvgoLR4-BTxVSffujNUo_7JSCOmcJ1aUuax54Fn7HIaRL7xN83JOdRlVo1DQTqMBKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ypm7Aiy7Uxwwap8eePW9YNdZl9sMBzuYHkqYINUi6TSmHHrgMwNEcTNY1G06SEOglE36nn9M-oU2DBYh_DhfakkD-yd0wZBsuBXqrnCqTfH0TkNxE8hbStEvrGfm_MoS-gqJEZmmH20oVGG38v5niy0C9gIUHVIbBvcXdiaWwoRDZj-MYf2ve0xwsGbs5OhIYvTxtCi8vrjg6eGt3uKmIAo0HvMTJghCylBEOYLdkBaD4pkCvADJ7e_ISIluJBTE6Al5bC5vulTbvBvuHUfAlz78n-ECKZalWxe-qFsMNrzcgFftx0aFvl5uiabnUaXVUYlCSZ_97C6xJYpF9p_IlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrkYNHMARPl7ag-aX3XE-LGAC23GSDU5lEm1P1gS7-ZTLHI7GIFnr4reNi1J-ZFMZiqszWRtyxyvVhz8qpeW-b8gaeuX-yqWTugSA4_RvusmyGu2sO4MMT2GeA5iRLbDHA-6wM2CPtchh3U8A-O1f6FErlMzKGouxYW6e_sJqc66CVfjcL3PXHOuMdNtWatXADpGOIzIIE9BpHd6Gtq38QlJzrDvF6T7kmd9XPueBpR3IEYYoianXvgOBMVJSViKRtZFidGdkmZwrE5XegaH6eDjg5TIvbjVZN7-j2EwKF5GfpNKX79Gva5TALSKjN5-pIqmSMkXBSv890yLzY1y5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwzP0n289C6DaELVmJskyIPTct3YhygUZD8rlNOvOqKZlP2k5_JBG41G7wR9ucXXK9zN3F5E2oamKXs0nl_IucckscFf9v33Y-wgBaKnnHnJPaZPc9YxGEK5YjEulbak1mJRSaMcjvN7tOJtei6jk76hjawwVz_BafJcRARcS4y3J9AQnXlBBeBmqIu_f1cBOiR_pH6X4KDRcLZUsUsCi-6gLTISwNAPzuLLbwTKP_oykXWXKG3HPWWW2R9A5fc6IeNS4HODCSkwU3Hh2-lamJZeRi8A7lPepxXTCzzOxHc3RC0I3pqCtJViTb8wy0gALMGqFk-CkKmDUS7bpQdD9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6Kad7urpA78qQpdDPeTD5q4Dce8h1bK8ztv4qSvAmwK5qSXqtn2OmCmj90jlxrE4Njl5AArRuRrceoh7ipIsb4KDYw4cDF7vp_kkyhbt61YZK2MoylTFVeBPHQ08D5DUCkKuG02ZOquisYTqKq4RjoimFGLj-vUkMZXr-nQpvQDvD-kYIoGPXEbbtUK6WMJqGh_To2mPHLC-iT2XFb4UeRGjrN6X2CjtXSDBFHeTlMnS3GH7CSwOP4ZC-xB3zAUBmbL7OaHf-BcbiWhFh0Vro-gQyfexcUcKz33s_CluJUBaJemmAVTl5d7Jos9IFIySjAqqUjAS6VbuJ75iNKZsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7T2eeV7G2W-_D3BoeDBsh3TOnWR8v7JE8HyZouE9UwGw0x_azUg6jlCmvyS5qwe7LZ9RgvZkvAwhpgmjbtNaocb0c6WJcImey5zXDnt4x7asharujtVtqJfmkKxlZmvBh0Qrtfu_ZktERB1jf5QNsT6hs6iHoB-u4GzoIeuvaDhCXeQ6SdaFmfVXbgb0t00xagk6hjgykT-kgjIoxBl2nMHlMeDMJIqdxayITu-YqQH-4SEnZFDlQ1boGO7en-YjyNim76k-400CBmNoPuFDot8X0mvV5sFy5MnT4cH7OKqgROdZd6RRA3lCNyYzYh8yzCEGDxenA2Rb4JAA3BndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQ4op1ilwb8gayzij5gWfUEK5L5PHCUUMEa1Tm8V7VhnjUzzN-nNiIIbvT9B5W3agl1uOmv64_l0Oe7pTInjxaZNmHnh7cu3Y023pWxi6NgIIIJUCt0GYAK1YNuIaboUklzz56iceXOy3DKXW0dqXRcPb_stcXBQvR1z8XPtP9PkJc9f9VqbqxAztZp-tW4J2PZyYYuM5IV9PY1ZR9K0gPPq4vl_pP5p5r5eFWB-YEQz8ZvUJwE6o8WvDdnixzUHBagRUJNEIa-SkdkAelNc-phZOQbM-PKxVacD-8bXnJz3ax6ZNxRUOlnEAbPqS4UdofJGWo3pt_cwgbZIf-Rc9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxNTHTBmtHge8qhC_a1fvJXaEVbLiOEIZwSZtBTZ9UVGKGNrIf8lR9-GiJ1qXq87YCzM9bQRAMVkVJZFdAiNw642h5M8Eg0a56ILPyMfN0DpRaSmuush-cg4j_ltX2ZrIOYqAl5eov1R34O1LKnsGqCGZ0uwm5QcPfwEKXX_gmZWwDlPWpU_ABTpWyf2tWsKXrIy7GjkYnHemp0OQC-28Z-_nmIewMj0_cl-qBQB3-aX3uyniFygs6j_djPBYKJi0fWy9r74QAXmLNBm5rlNU47ffiayriRWuupNyZSqX--gyFmY1UMPxKW-Dx6QS35la23rwVNIXUIoUoIPsKGGZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_EKjnXJpqi453NN3nAWnwHD7cxMIpSGoqiGJhTftjsZBf5bi49GXcTkYAYO4txna0BbnkhNTPodg0zia1sOUuK6wqVeRU1r-Zez4myC9R4wDdSSYR_twC2AyzN_Za4qar9jmrZOkpc0Z2HBE9EkGzp7UlPOI2ESEwXh0BAwwPVQPgkuNHuRk4SERrMavOuDV1YEoNlO87YWiVSqMC_BZL9PC6WFwrYkngvMlmeDpFhwrganvbLD_jhmNT6Eh3lNUZ1RdkFz0xoBcaaXEzi8zcMYH2VqllnLyN7YVzHFNE1wDXGZ9tdM4kcDTf2WzWrNCE6rp5om37yoSrZfHo671A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7qLEc1isIl2QMF7GzJrA7bkUuVja7LaLT9yclRWlaUtq7IhmcFmwOsQMFbJKcETVwtIwACiTHSzIoh6xcxdMGkFoWnvBED2fNqeFtjEerS0yunep_2BZmypiwtELQnJ2W2B4kHC8aELTsAqwIphagOqYrITZlQ_uXrKouCXFWWXxKmst3FVi89ld4s31bcYpFSOqYn3McTiskiSFnrPwGFNoqmEjx5-DHhCvQcm3cqfumBTjWoHixblDpn6ZQzoxIecTSVq5C3T5HhBuXnXk6M0OlAw5waIxdCw9i5MBsM8XQyydZaxy_P3tHG4aSCSHyZnYn2L4Xh2SoKRa5Ic0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua1yV-wjaE7nMAwZnNLS86dYTvFaJWc0Z_WYY2PD8V-KcTNSF7MqAZAK4oPQOJMaCA1oENuH9uw2YFUi4E8hmX3OMvJhQxsYAmhFYxL34bYXt1_XeAKJKEzy29Hg_SmpC9wJCDO9sgVrsXvJzCFTJFuMppBBfcjlz0Z8Ua0Hvo2yuaIbBmULylWtLKINF2XtuDLW76XWbrBKeoOJxlhdFRNVDhMQQiS75jLvLKbb3-HplNoIFCAU_ksQa2Nm-Og8XVTbPhi0WbPixlHwUDHWc1RLXJ0zfoNFQ35A3cRGffGyUJxh77Ak4bNUsvTOYmu3fdNhgEIiROCgZf3tibaiwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dK_6Dd9Cq3Eo9oICQVfJVw8xlB5_Ck-4g5r3ZkAF0cmv8pNoBRfUrtZeXOlOAigAp-n0rBAopvELTi_TWjBonObANdh9uxbHqv52yBoBMBjYagh4M_rRVmD-JtHL1Xm9p7jLkql4MyefKGtd1uQ9wCkzi4FcXhw1sHmmWYmRO0oC3vFpby25XrLSUQt_Og8M-q_215V2VbeYnJPsDaxv56XUFnIiqF-fdF18nGNs7RoMEV5zjHuFvEUdKu9ixUWyr3EQRflkFZZ9pD-VrTYHWHp86akjiN-WOhkkysmnvCvzziU7vPlHrpSWwq54zq5yuu8Y3Ftgd5WCdDs7QIREfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=dK_6Dd9Cq3Eo9oICQVfJVw8xlB5_Ck-4g5r3ZkAF0cmv8pNoBRfUrtZeXOlOAigAp-n0rBAopvELTi_TWjBonObANdh9uxbHqv52yBoBMBjYagh4M_rRVmD-JtHL1Xm9p7jLkql4MyefKGtd1uQ9wCkzi4FcXhw1sHmmWYmRO0oC3vFpby25XrLSUQt_Og8M-q_215V2VbeYnJPsDaxv56XUFnIiqF-fdF18nGNs7RoMEV5zjHuFvEUdKu9ixUWyr3EQRflkFZZ9pD-VrTYHWHp86akjiN-WOhkkysmnvCvzziU7vPlHrpSWwq54zq5yuu8Y3Ftgd5WCdDs7QIREfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5qdb3RpFk4PJn4g_CtVZQK9IiA2ju9X5xXI91VGPn9KaAyGdpnBuu75KxgoCg3ajkp2ix77YkYLhh6xZhQKukO2qc_R7MxNu3H0TiOyoVfAj1eG_p8c3gkAEjksp60NlHLFFtjTnB4hcrYt3Oy87gYHeNhkNXkIm4QyRJqHZ-UagjlAG4gd2gA0-NBijPQaPh92RIDWPvXhvXvZj2KdfKqZGZjyEHbaaegkksy4_AQOCwUuOjKhuXvAShQRZLlObVFCmZRN665qxpUwqs8ELOgw_f8OaigM1bjv31DBeRGUlBME0T2t61OYvSxVBMl1NkNKid851lDcI9jPwBkYBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJa49_YHXkXfFxvt517ZbEnSaIU_1yx_oUxSsjowUBJiWjNQ735fPLivPs-dJwynR4myBxhyj4A9DyS4w4E6V73zxa583vfk-mmoS8i0x5hxv2nNCGIWDCWP6CpGPfo90b2RUl_T11n6MJr5WNfwGBDBSZovQWhtL6AxjneUq9ldqE72FnvUX7Q3etQhiBW30UgYMocsHkEZf03tj5fTgcYtEqDMbGkm50TilpLDz4cQaUAKYaNi87auzE9gVaaAk2hjohI-24aiegYXS1XincQREP-drpZGZuvGDoRYd9u_B-lV6pa0JHFWYyFHiBHcyw5xZrQzYe5lVWjmvYCpaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSQUAfPFCMxbbTCbFCzIAwjl3yn3kXeW4GmPDH6IEz1HwOEResLc_YnOMBuTc1-tpma7Ye8axElcEzDVfu_cvEjKTmiTwx29jcqIfRPiuP3EsTgdRyCbVo20cT37c-acVxvPhD4mVH25mRGLPOuFO4va2qzB5yFphfewS86pnFCr26uDaev9XCnXBLvbf9b4zXCOZnXC8REajYNa0NOyyMGHAY6n0mZ9liG77Gj1KNPw4tJBU2QuYE9y5gDMnXvtGTQvrW8aB4vVXt0ygT5cnngaorxozjfaSvMrwxPzPdcuvOC4x9HKhVuNcUr7ZxADlt74Mgt_lkiI2n-oM7oAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptnPB1aN2Y3oR8QyJV26avRhVzf8O6VbJGOjBzHFwT2RawlUmYKbJR6VU_8OaIBaR-SJti1M67I8KuD0dfuX5-7t6vrzzKkMXn-BbCZy67cPzYH60ndZD4tvP_oOokSjl9BAYkazpAbej3J998FhQX7Dwi2Fnc_VMbieLIm8xLe-Th4P_Qa4XarFx07Nc5bAga89wMPxl-bBJZuVBKd2uLbt29bcAPDkjTJqrJbpjf_HOx_iHbpRcqjJHtBiw5wUfAVx4h5u3qD59IwjJkyUKMFRKPXtm_F6imvXL9nIOdwlHtYgEvQZ3zakQpyBs5BPKtxnZQX-WuQRHH-l4KsMMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DY-LOPL5_KsBOevOTlY7ZmQmOulX0PhqsX9aZpliM7VoMGM7veMyoEzg7P1Pi2mSU-2DBxGMevSvZOlieyyMiypou7mPgz3REzZv_EMM79LNCOFTFVtqM1XO4nNN9w1Rr2LQ5vddyfrHTsZ8fWo7FRSli3qyuHxYHYHB43NyJQQLHS1CXvkp-qjsDATrnxpz7-NNAUIGqoaz08bK_K-Smaj_THwbUV1Mp8fe6dJol5Mm_MqeI8erLv3vpv6ADm3BTqLQRS6BobNM_LKoFuTnFYQbkq7_-YHvU8qu4KEVdMgOHyzj52quLG7pN-bQvLwMMZuM-DtZuYj6mxpJV1FwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5eRcFPDKoB83lMUYLKvIGNNyFQdzbsdnBWWfKlrj0btzLRCYnZsqexB1hk9SmMdSth7YvxOef59nsWxdtPSQEu_NZVgskLfu9KIkUvzKi_sRYM8VApXoHbdNMQ5QRq9yR_XThA7wFIBbHrLABV9WCI-qzqFmo6GLVEbhkymhMmLfUuAwHHXUSIPz9FtYUENe0NlOu9Q159w8IZ52miHsUnaPY2cNvvQxUPUYsQzA4RGVJeV2wgtZvuV9MhqbbaKrG0NkF8wWZnvh9A3q41dlej7XN0T5llEqWRTU1AUG_breiNtuuHU-HM-aIw1TXHYrzVfEu0GPUWh8izsN34xAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbFbiBMnKnd_C5Nkh5PGcHiT3OcPmGGOK9uUJqzDvYum4klPifU7r_eNL0EX77JocDow1zMO4oTCV3b86AOlnP6gqnTMOarRLUScVZWjSOZHWrMVP283hzx-lVWDUzhP1q3-lGzPP-6E_ovb2E3d4G7Hik-DKPZz3wga-IO_n_qjAxuTuORoNqCY2eLXuu_LqkW-1ZkJTjlWChoGcWoeNmYDdsJBr0OoynDS10eirzw8Ex12w7jd25-cX_6bHFoDuh2Bd4tg79faKxAm-Uo1KAhInT5kEhJa6P625pl0i17ifG-JkJEAxym_cwL0eh7IpzrI0xSpjarypHnOaiBusw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=lVAU9jukedAtHmiaWBZ56hmtt-rbKatyPp1354odXfGuUN_Q2ds9WL19M5rO9uKEQeEL2boqeJPBiwTEMdSBAmU2B-3Q0U_4gN2QuZH__nrTLOlhpKUZ1ygzIfyuN1ZsDKW2bD9uoAh7W8QR_tuhUMdgVhb2n1Sw08scSoA8S1BrS-ZEWvZM1FexcI6JTc7WUG6PT7F23MMj64i2xbk6DimUX3m_FjzxA3LeNilKDVxTNEvzLB34TuJfBz4Euz81h1fEW3C1Dt03cPNLUb_mqdeV5t0Z8aiFjJt3IuYK_KfIWveipezAYCQmWqIsxJ3FKeOrNb43PTUySi6Dye0K7wlpXp8tmlcyyZ5_p3VFSzaIuH9JYJNMxcDbSUcLyzVaxeKq0LuClLBkvNpbDFKQl8fXlp-WWIvcntA-No84B74BATT_wQt_MuxFSb3D1aKNDMT2w240KpGBExLkHVQDXyIjShhJIA9Pdi6qZ5UOeTYYWb9ammlHIUS5DxsD3nPzBRyV3YdU8Az1k5XNTCiOy0BwpfmI9-cM1nxcIKFYerXYgEQncutVc29exq2JSeEFYbKkrQucVtlXwxuLNC-0pgq6fOz9MEMomAz_Q--ucvYFGFUEF-L65eDKvnRP5youX_0fZFhYP8MT1vlfEtYi9ncvmX3ZPBd8sUwW-1XZzYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=lVAU9jukedAtHmiaWBZ56hmtt-rbKatyPp1354odXfGuUN_Q2ds9WL19M5rO9uKEQeEL2boqeJPBiwTEMdSBAmU2B-3Q0U_4gN2QuZH__nrTLOlhpKUZ1ygzIfyuN1ZsDKW2bD9uoAh7W8QR_tuhUMdgVhb2n1Sw08scSoA8S1BrS-ZEWvZM1FexcI6JTc7WUG6PT7F23MMj64i2xbk6DimUX3m_FjzxA3LeNilKDVxTNEvzLB34TuJfBz4Euz81h1fEW3C1Dt03cPNLUb_mqdeV5t0Z8aiFjJt3IuYK_KfIWveipezAYCQmWqIsxJ3FKeOrNb43PTUySi6Dye0K7wlpXp8tmlcyyZ5_p3VFSzaIuH9JYJNMxcDbSUcLyzVaxeKq0LuClLBkvNpbDFKQl8fXlp-WWIvcntA-No84B74BATT_wQt_MuxFSb3D1aKNDMT2w240KpGBExLkHVQDXyIjShhJIA9Pdi6qZ5UOeTYYWb9ammlHIUS5DxsD3nPzBRyV3YdU8Az1k5XNTCiOy0BwpfmI9-cM1nxcIKFYerXYgEQncutVc29exq2JSeEFYbKkrQucVtlXwxuLNC-0pgq6fOz9MEMomAz_Q--ucvYFGFUEF-L65eDKvnRP5youX_0fZFhYP8MT1vlfEtYi9ncvmX3ZPBd8sUwW-1XZzYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4g7Fwht3f8DazrPELvUn0mQGb-CzaVo-jRcDH5wHyxPVBHiNH0tnqJMdaByLuJItw0YAISyYYL-OiYI_d0ek1JvYKDgyTggA_ACc96SUahAXq5VwZ2VFmZ53TnFGuLQKIL_erCE-ovZtgw7ZAowGug3pl49Vzh4MFIQdGqkKq43S_1a4yskRLF4vgl60bKU33D5O1bFcdOBuP4UkwJ-2iK0NAYJkgLDs0dyXqcqzbphL0_eXrd8Ldvv8bXq3LmCkFuRXWOu9NbR5jphO1gZi-atwN8HQzUuxOSDIxfGvY0qFgEa4DtBXVe6ZUMNViiFtqyhpt-ZpanTt-nAKfs6Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myJuvRQSvjXcCAhl4da2MGF8ixj9TKM9ch6Jl5TJaE0lxo3ZamAo3SUAb4-fX3DlOvEIIabn4hFnrjDr6a5GSPR7xLJmSjCtHA3ULVAZxRZ__QtYWV2NiOU2a8GpaR4W2IZgTNop11Ges_iR1A4fw4vBo9pTxWc2GBk2xeIYPwzhLBrrUDWijYDgY7WTD5yb8YPTWA6FsQCAj5tS2SPh5hv3ziDv4NQvBx0V3aGljxeY-h8t_huAcNWnozVkiMLrDROuQDC75PhAWz2_ZyugnXiDC_XQcJyo6TMAXJksLGeUEdCcxN7zaxa8_z0xuFnldcKMp_THpBuLflgC576P-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJsNw2i8C3xHI6ISi-XgDC9QAOBdW8SbTh_0CUtWLeNBkGuRBgIfPVW64QGi2rfLGsZgpbDVE2x0C51-GAbBIinDMmMB3ZLTWvwpF9zYlX4cIJdvObd08aGFzUa0rAPcFq39KsX9MX-JEqZBJ4qwqPer1uOGSa7PUN4Rif4aL6qYAeIJppsehCMJX7gvA2I_4wp2n2sD3ozk9Tr0cv-5nV4jDlfPqUzv15h2lYi7v9FuBLED4UMZbQNf2_6TII1C7q4TSw5I5SByO5w8OctpprYuxH-Zl9ZuEXiNCw-bZ3ibT0dUttnWNrrCd2TgScNj7-qre5mDrROpp-lJuLKZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quQiSu23ueh2_Ftaxf0X7Oj8UvYslrEk0Z8mBT47xnovomJ0iP567mgiUXkcOn6ZERdmFMZn2A26bcV02VD0nHacxWna7ixj7Vcd5qgaMcsOPdBMKfLAarv6aawOr0vRQmwij8LB6PwH47uI6wowW3CNFSKCCvS_qgvhSUO-Qq3_ssO4wiplOzCNdIcUwkxsq0PxF-bWxYmk7qDcX06P9Ocs-h-bj1Av_BbmUttxaUYxg3Ks_phvSjpTk0w2EkveU9lAgCiMKXQUh9D5wp9NQ6z5CS7UadTnCLVgKGY7UvtveMTrLkQBpfXZUGkrdoRlrDFVFpfpYbuGF4nd_qyq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5put2u7bo_AAz6htRmbbFqnD-bWNyChpF44NZ3cHipwMScqRts2j43eyR5rR0dYl3_v_TUiPS4xaCRrN4exLG9L_iUuWTaFu-gAc6nb2pRtYv7Gp5N3i0N99O87fE6-1dq8LoQUor3x9BFeItgpVqtn3URlO7ndQuaeh57yIT4P_mYWqDw-2VoMntXzcPlxtSCu715woULK3NAFH-L09vC9juE7POJsoxRrbcEnVTDhyQOGsPT_eCQ2b0GvnfKciSiKgkARIhIIqYSj0MviflzMW_3H3G2Iku64btt6nRs134fUUEnxpp2BOg0-hhzxQtG-x9v1MZSinqjiWi5_pA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Rz0V0U131ybD_aV7cx57vM_qIzodUVsyP64_910tSRH4qXsfiYUYvn2qCEHya6iPMk1FdHT-k-RahhSPi8KALOQIX67AIgto--teEeVHOZVhjVOj-YPQs2wsvnoaEqAfGTk_5rnlmHoX54Dq8n3W7eOFGMsTxz7UK57JzG3pQqU1Mx1Gq6cqXm-GLHozDqqKfX1E00XT9_Huv9HzuaHt-bLn5B-87xMaMOv2oHmX8llP3aQkaIUm73myE29t4gpAjD_yD2uyw9JujR_MasPzohUBUfmV6N6h9YGqYaBjYH982DbnfpTJyCQ-NKHkbIxPyu-ZGCy3hHwnYeeWYE0TPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Rz0V0U131ybD_aV7cx57vM_qIzodUVsyP64_910tSRH4qXsfiYUYvn2qCEHya6iPMk1FdHT-k-RahhSPi8KALOQIX67AIgto--teEeVHOZVhjVOj-YPQs2wsvnoaEqAfGTk_5rnlmHoX54Dq8n3W7eOFGMsTxz7UK57JzG3pQqU1Mx1Gq6cqXm-GLHozDqqKfX1E00XT9_Huv9HzuaHt-bLn5B-87xMaMOv2oHmX8llP3aQkaIUm73myE29t4gpAjD_yD2uyw9JujR_MasPzohUBUfmV6N6h9YGqYaBjYH982DbnfpTJyCQ-NKHkbIxPyu-ZGCy3hHwnYeeWYE0TPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdksTrcvWNGRWE-K3C-BU3GFJDwZG2sIZfriJf8L25vmdVE-Y9a9FLN6AFRyEc-Vz3TiBimkkYXiFxvqH5GM_RV6WYC3GoQ_LWWlMnup8rNGYPkMxIiY79C8FHPBhOEt98SnJbHrHyC7Ad87mbOikzObR6oD9Sk3CXwPG9fjlLVH885Q8T6O6Al_T4g6tsdRHhH8qESVfAN6wENR0fn4Sp8N3T2Wr-8iThlk4I1oVg6RXQFhpyA0wGnFQD1m9485TCkP4lrDIAWME7kOe-ITmF27pbYi1hmU4CluJ9BHHPq0LEdMCR8kLQWaa3ciSKkVZaJTP7tVbzv6ivchGKzlGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5PL1tn2VWpQZ9wdxFmEs2CIPOm4wwVKhEy8PCMJ1r1hbGnvv-oXskLUfJro_N32FDEb5yJwW9FYMaXuMTCKqP1DfqKLGJVjCSio5c1ZZlAgtxzxAvpJrvUu09yCuNsY02mHdzJyY9QUcTvECMq7W8_kX3HqLuFZAr5KyNz3-pT2QvS5wPDxkNKxhTw5mq6JvIMz1IGh5hgkil46kGSs1HVvQXXXUM02risEiWGHjOdeYC6vHbBKJm70IAXAGLI-Xl1D_SFXcMxwdsVtnG60PiIrBWlgDOE1z8o5PlGtZAlxjrSOf0EiecG17kCVNmyV5dMtLyf5UywOmJvCwS9rRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeuiKrQTCcpVd2NUxEGsqw3eW_HuifpXTUcK53JnHV6w-Q_AP1r9uzaQ1aUm2J3ZbkhBdd-2h1QvhbN7dhQbjZw2_Q167HMWo64X9Im05r7eZJU00V99N7LiUQxZCcRwNB4YnDkv2T65dQ_NIMUfn9643tq52sHcl77dLmt4_5U0F7-YGUT7HWjXq_4pcJWITNjRmboIvKeMuk3rqDvnq-WDqSfJ7M9HCfvOXDK05Qc4I8hjqRKB7KfTI8N3t7Ok5Ukgj59_C5ZtHTPIgpZ6vkT-60-hiwPZgLFfc78Gp9YcGUMnpfbeFJm1KVgQuP0rbUTOgwMaJNLlay7b6SVkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2CxD2-gxUzsK11kbxwFQVHye1ZCLgSvyvzJrkIgTuq_vli9ItrPyFZFn4_-lJHUBH7GR5Bgggi8AsYPHdFwJYkAMaQGuUYTHsffiskNzrYIZJProcwTZrgHlc031zCSgCnBHni2HGo4l7JIPf9SuIdrU30xINuiAju9F7GzsZQiFvAp55oEGcKSr8Wo_xKwvYr2iSS9K4FG58pc2Uttv657PQ-ttKlTmi1M9MUyGznzuX6UCyhVxbaZmByZ4N_VSo0e8rfEITmXl8864POEHkliC_IB_TppYzE1TrTNKpPjPPzosYNnIJ_USj17dY8dK-8rD4JOYrBAFgrA2ozaSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuhCw5muqjVTjS7Z1j1i58LYtcsw5b0ESHBjXdRYKEq6vSQTcownm4F33lFC2PFi7fzW9vqzk6JcKUIEaXd6w0c1aUW850mlp8PKsuF-D6jZKzDY8_RHOR_2j0GlkDqRCnUpHAyJTAk-YDjLr73kA1qn4SUSm30dKrtWulGZBxZMEJ5M-Z8fN1gRIXYMX3c2RdMBxledRggaOEQCOsd6HP_b8fJXdGj1KESFtHooml08CVUqvRP8aV0yYuIlWu10YjAI1mQoZBQ8qFlB4dnYfxbf4w679XZaWZr4UGziVMEiXLlwBqucBx-uBGF41sx1g0usRM_m2nRJJsOhwD17fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKYrm_tLQ5v_rs2zU7HfirZzlGLgjdF0W6-6XM7vZ6WLXL7hrx_JEuS5IE_3EKDM-IIGUAoWb4zF6qCpLJ1V9hLUCKBn6dbrxWUl7AbiVOps8bs8CFmow7y0hbiC_RqKKb4v8GmC23fwz-Htbq9XJfMlFbw5kBrTwVGADzKKZ88NmD4TBPiwcd8cEu5y4kywlr05Yf0oYcdm5inl8uDAAl7XqhEhR5JFNGGqnU3qYcAYXDc177ngGJ7XMODbYbHxY5PW8hrRqDuH8TPkDKHJAqfJOZ06y5MbnxRxaCtRQ1jFFWaef_nY9sKbEHefDcfPA5rfMRfcXLdgeC1Uou5bgQ.jpg" alt="photo" loading="lazy"/></div>
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
