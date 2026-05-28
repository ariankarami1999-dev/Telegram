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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 23:51:25</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 264 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 362 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwm99Lz0df7MVzciC5iGxYFGjiEeO2x6Kui7hdxMFVObBrlbQKwtwuBYrw8DvaJR4ixobv9XSFJC8DNIcFVhvC7zDomiK3g5ytVSKmD7t3oe5My3CbCqldctkwJ2eukfR0H0PXtPYs7Qm6_ODNf5wZvOYOgwMTjU3NwbC3HJ54HWykV_oSl0yWQw06Ll5bvd_jvcdqegEO4EmL-IEmQsLGnYDheNvWvuewGJ41Q4mr-BQCNceDdApvkxXfnFLzZui7ju7mCPUucWt5OCyPv1_dz1WGNDqdVKW1JP6qpf-jhEyjvNshcjCxZpkkB-G64ito5h27g8_mpyUvvi6gIEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 461 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0cJ2nIW3KfnHZb2WTyXo4yLfoAnaQg0Nv4VNUQlL_4w_uDWEEI3_-dNOQtMKqa8vmOW7emggw0sHagwW7AYGJGxx26S4VKjpZMc_cjiEhOnSPd54e9ZbP4Y7JlP11yy74JuGKbPlNIgQyPVxcyyQfxvLAUHpII5S8We5WPJFn1u_GESBO1Dpev53h5Lb2EFhNHRtImctNzmh3WCLxsuDia8b0S6eQuMuFEgeSgMb3Q6l4KMKI9anHMgVwpJerBcmgBa6SPHWGLYbn7wwP7lWfunP-WsCoc2FAsx5Oc4RKhth8fjV2FWBen2snrkapIS6s9INsSEEhTiQ_DCrMiCcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpzjLG_t3OkZveVgjGk4I4JT8tPeAU0CtMMLHmslpYnTsNm-zumiszCjH6R79fxgWlasLzXWERFNFmO2Q8aKoEMPTvPMj65qd-t011vJV283FxYUcNIioFUG89HSDbxBTEaiDN-1Atd0cMnGYMk9g7njX6YVpOGT1OwT-MwsN0EBIc0wOhT7v9wwgKf_sj6rxSGoVU9UMNZjwsKCEzc82wIU4p6GB4LEPjzmULvmvZdA8GP3CpwBdbcVpXSYU613D9FsV2kcljSoxqG_wgKWdgMpbDtJvVPIrhw7fhhstNjnwPqayccjvaXkNruDmAvhHV3IVx9wx2sM29wYS3rCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzVrI2pTw4HK5bdxK_ZsGMK0E0gtXjEsz9FFKGQJuv5k5ba3tgDPIcU1YHnYLaj-6Gyy4CvAdD_UzmlorJQuxFMZNIiXLwHQzZFxnbcnhM5NdWtaOpRFBKt-EbZXZofxITmh5dcyRvrALcJPNZqVP8D4EbNFsu8MkPxzhquOmo1fzBLSEBgTnWzVnDp6yYnDw3xJ7MGSaDmQu9TQDu3jnTC5SfQpNKjyAOEqaCffhIiWcTmrBYaX7yfNMvLO8HN73YjjLxx7rKC4nH07lF2-JrgAPbckYx6YM6-z4G4vCJkSUMGOiN4IE4M2ypd0jKU3XPkMSbg5It9ooipNwGCk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SInGaNEGrwl17c2U3z3keIXl9gu3uwenchPpn3lVLj97xc6abnU4GLQhlj2JmO_l64tb0E7GO3ExW3A6Nn74tB2j-PVU-629n-PHJR5dN46pDwuRqaGmeGz5loB4bZrZt1QHDvHweNPvBSk0YKydcgBoCSR2z9FGfRxDxW_EU7swVdo1YOObQVE8c5-J19SFIOUKqCUZW8JUmfQsE1K8TwHEfHPyAaUw6Ak3XSpRwQirylQR7QP-KlPXPpPFdXiw1IMUM1fwI1_VqHfEDKpUyQB-_GUlMVKiT0Bhnu8FiD54Uvu9zob1Z_HHTXAh4vHSIDkJQj5whuabQMkBSfwBKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LssGC0rbPIyPHQWXaRNZ5SNZ1o16KnBFNPnuuYZx2uEScFG-nTQYils-WqWG7On_XMAVGcEKXkHu4y4zRiKxXarcAR_dr60n5xWYHc5Ulf8bopAA9vLnQaEsPYmUlGBuH7Fxgx9y6pdWXfcdiGI_LRknfqCUpi-2oGD7olNhel20LikNLNe4IwE-sgNFlgsJbv_t6wOLL3bmnP-P0tls7x9XAzduk1ecfio1Z7xqHjmh8sZ4ybSsbP-RVSrBDzsG00Qa7Ul1ujoNZ9gF9jdK6z4yCnN9UO0eC3DD-d7kMBti6QkLnPZP9BUO4HWsL-5ZV-ARiGZ_q7JbFOqj6Z42jA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=unmmeDIvj289HwoqDrVDHSV4r985Dm2ENsE17q1Y9PUH39iUy5mKnIuK2JTtLhPhXplSB1d-HTzZOmOTAoo0_aGt5Du3hlF0PTj4w6-wwYHpNwzinI1kAsovoDQZeqNfowHc4wywh_lly9T17qALWTO4OalPbrfaLFOzumXb_TD98y4uus_ely2m_JpefjcPm51nwDu1AXJyZ9B7T7Wv0hvp8Y10QnYLdZ964WSjtr8u2YQKL-htO8dTncQUeJ1bFv56cQT6q8POip2T_-tvcqSAVvuQyQtPf3lSxR_ULsSCGV8XECRWbSL5SzvEnk22MVWGO4r3ObDgXTIxvPLB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=unmmeDIvj289HwoqDrVDHSV4r985Dm2ENsE17q1Y9PUH39iUy5mKnIuK2JTtLhPhXplSB1d-HTzZOmOTAoo0_aGt5Du3hlF0PTj4w6-wwYHpNwzinI1kAsovoDQZeqNfowHc4wywh_lly9T17qALWTO4OalPbrfaLFOzumXb_TD98y4uus_ely2m_JpefjcPm51nwDu1AXJyZ9B7T7Wv0hvp8Y10QnYLdZ964WSjtr8u2YQKL-htO8dTncQUeJ1bFv56cQT6q8POip2T_-tvcqSAVvuQyQtPf3lSxR_ULsSCGV8XECRWbSL5SzvEnk22MVWGO4r3ObDgXTIxvPLB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_JrWs87efyc2ZBjUCkYHgTJ-azFij0KFR9HyRfDEmBPmmTVBdmkk3PjerN44RrMHI8-o_mj9_VPzip9IYTjgtHX_r7lxLbchFzaWwHn0LVl5mUS5v7SH6U77XQ05UpJUATglxRL3HxAiQ7bGgx8zU9YdccmvubPQK_i3xltB5xjUoNZ13iKv0pZSg2QSLNFhQ3PA7ETgPa8T64KQSDeyYbw2sWDpnoAnbFNjl_8v4npAIjotGfipsZfTtjo6uyO7rcJ1vBLQstON2MBqW2x9uZIuagjsye40NWuir5I-LOYsTTlSfTQLNfQjIwWJGUgDaZdH6t7MMled1TyDVP0sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVxpUr_XdyP_neir0ZeW_RTgnOV-Z-htZz5DdOS-LaTRBaei24sd5tWHhOi_Ul7MxV1dYGEgf0OqU9e33vkXfoH6MqUvZKayfuxzrNXtDedwDPFt9puEQFqUNeTocelsh4ngajoDXc6T5IwOwrDQS3AophFeF4JVEQbIBuj_83lh2Wx1UGV2hPoMBNY75OKo8OfZrGd5cJ44hx7jTdQC_PBDbZyITOC30wFaUZd1PlzB66xO-tThtfZ9Uz57P0dtfiKQBvix5PdhSniiDa_a9EcMqRVDgrQHuDfkf1TMORyS3nPST8-LslkrgZElddy2nYxzWkeqnBWvw4_1RtutoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N89gX-LqbgTNGhoeIbUdpHJZasL0C_GY4MiyXaO0BE-ZoyeSvK-hoo8ye3xA3HU2fi9OrOScz4Q3JyBhtnX3PXuhssEPyvIzcWOlWDlh5iLMOZLiiXiVLf8VdLyCopoL7FrsD2pFrTBpZBsLFlkC95erhfM6ddk8GGGszcOzmfSP6kCPQmLSYBmWCrXDNuilIjKdEpYu1DH2HPWVgWxmllEeD2KjJ-3i2o5cAyE4AXNxMHVumRkeSj3qwJYcosSSZf-Dc78fzSZHWhhv0wK8yRReLJ6xSugowlr6RiSyDiFUIP34_ao73Za6uDlk33T79J493wZyFSCm1kYn9a0RSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZQ4GfUcfIL0gmJdAp-j4WW9OqECechvAPkswbyp7G58lY9P3tu4WO4PZndibhIFjGtgrEbETTYZChKVmHdItkmECUlgUrzq2hMza1We_FI1QdTKsMDm_E7vJr6Twtu0XFMsK-XSWY1Lt5LbNi97FxdguBzy7tkqbEEhrvi2r31uG_4-3Oo0ojOUxMDuZrx77FtxZDkjsIq3tfxdcF9BYUDo0METNFP0zRyYA-9fvg3G7zxkunuXVxb2TDyphmD49NFtLLcQjQ7HemITminloFoq4hKeDxxBj49ARBy7_htwqjcaUkFGBavmRVYWVMRc11ixkM1uzHAcyP8hD-EcVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD38LCW6ObuuDEYOdo-o5Qpj7JfQ5Rin1oOf04FODuJmUaKJyhLnjH0cigckWdbtNvUMhu5hZHTEaUpUlQ05FXTcBI8gjLJli9dHhiET3swlBBqr-hDmgJpwkaDrfVziiX3p0a0WOYR-s3Fqrg0LYUujmCPQh19XjYBzngKDVE5MHnG4JqJYxakGzvi4nFzc3h9dXjpFlrT_va6YrU7RG7XbWrj01LY1llF704Xqdr9ZZPk1AShiy63vmQtMs8vzPtPuqm1z0bm2GK4BbCM8sgqHlfi5PYSbg8nODL5HC36UDF0_w7yfbBNG6T4ILiSRbQPrWGPY2P_16x2f3oOHWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx9Dx_vIOjF8EUcF0JXdgqY5ZvDJGghg-oH0Q88eqJC3oYFD2lYS_fXvsznpMQ1cMLEmuzaTOzHzpwa13VJVbiUE5ISr_5iWuLe6uqKE8cz02-U97JvOu_1NAVlVtiECYmMjOFVNlFzyH-6K4QydZSBWbutKHFhBUNG-yNKLMSFN-tVduIp3CTDfNnx4taJDArAGg4pWoP0WRw4R-9d-H1wyda-zyzseHZAg-uq9VNKP_BJxz-EwdtFm4QX_MjgCHWPPWkvlGCXUFUZoafoLE60OZJedHRbW6RBI9ihIqUkWGEBqmZjlqisj7XrrIntSoYk7qdsDfxJJ3eECb7tyxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCY_45R2r73LcW4Joi7KAMSBgJ47bGhLgnkplWi7aatrfNCcJ5nZ3c9vjOwFSQJIibLWhCQAcxV8AwXQbx_r5nBCdm1qfw1jmVwSs3cq4chSKnCzS0Bb9j6KSwjrxnIwpBv4vPwGRAxd-h1psdUNQ9nlPCS9qJBR373YY9xb6kh00EVX_SRvMRKWHulNoAmblYAj4ypBo-bb-ge8Dh-5ljS8cXemeRcjZ5iKyfvRny0mbQBtxxoZTZsh2cNcWc2eMeSlTMiTBVwkmyBISU6G1rIcV97IWrMjjfaRV4ha4XCjUCBuRTdR8ivjYnTAAbnaTuzxIE_xHyzZjyLXzPI8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7O31WlGwYGIkaaTd4SDMQqc4d9CWP0GAH7wUjlJ6LSLpcIpr56M71vRr2btOAxjlVyIz3G-XxN0fcTG4qrXdAQU6INgJnx8co_sKupULKt5YdnJIsNljwjeB-9g6QGYXYG6-5WLBK0z_5T9kYBbrrKRtpy8fb4-DrBirFZvnjKltihrG74PnksyK4K7V7ksDs6Z_If9VHu-JkER4J_OqYBm6bR1sjYfJSjMS2gmzzqy0lL3-gfYxWQEX69D1VYkbksHtrSLHnwX55smzmUv1eerG1k-pPmq6Q4JUYrwIGNGXiZzhAo8W1WR8LmGU2wNtBdtccejvEbBp789oFkhzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf3yCOyMDC29CqmNhWzdzcgR6T01v24-lMF4LEN6xSvqUTYO28TkQ7fckp7JfaE-IifdvoXDvUjTaRwzB143jXrmRIo8ja8DbhameDKWOBFuo64Y4yRuZ2uZIU0PKMscSgoJLEmo3bTROrMbRmT9CgMYTxjUkR5sC5rLIRqizoiD2ylR3YF6BcxCL2w4blFijE3lN27HuuMapPWrHbNl4qEAnZUR2xbrBqXji2jlE-4HaJo5SceEjp_rYsNVHweVxBtx0-aytqrRUT75Xef3XfRLt9ZYZJsPdzPfFbXSJA3ckp6w5uxsiG5t9JBiMHqAfwWy4Rj2QCCyoOYKgdAaOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmBuYPyXsHuA9Sl373DzJju1yUhQXFCmeY977fjiZbTC6uXjKAWRDk9v3mpt2QmSZKzhkGbnm64KX8SrzDTpgVoWjctw_jbtpC8fgkEK8qVfUy3ITTaXINtpxPV5PtHjloMS9CmUbG0L2w-E6A5iD8r9apLum6pRdSJdHhGvI2s7iObLJSnIJuu-xdtFqu0_yeFhBaEW4t76SeFNw0oEzrAbMrycRGTtqbTwVhC9ureQm5X_o9a8NKC5ps0ul-J6q0CdSVTgn1ofrGZmpFst8oFcacDPgwMNvwDcb0q78E5rxcpy2v_1PWcy3g-nmNqGw0075dsX9wkQBJNcQtVaGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSr4sWQQVU6mqw1DbbSNAXdcrLiSknn7BC2Mri7yIxY_hlBI8z06jsphob7T6JHWTFN1pKJcwW0bV7OCZG5XiBGMmWJkhr5VAqcC1QOjjVjCpaX6OOxdTFSIGVi3kV4aLoE-k1i3DCrSpgDdO0yEzvOgCOKesrhD-9CATYtFelQ8e65rG1vmeqwzb_Na_NPagQIoqhMhtuCZtGHxUN3OouY2enXKBWkm68SvUW4LasrP5521j3ZHv9G9v4GLusfWvTyFp6YgElJZ0F95D61ryXdzEPG0ZdiKI6XbgHsNHQtqukngrHCjEyQPELNZzhMSDpoenVX7pc1xT944Dxzcdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR1GtVOS-CR2Wha7U2xa7wzeUMI2O28VWPs-Eg7bKE6Ld1sRLX6tGdoZpbe65-PMg6g90E8I6Ly5dO87RZZnpOUE7UVuZwXD6or-TNH6HqSmzfqih-HnqPS8gpx2UfsjF48kzjUyZRZ5gIoh9UwbZ2PPV_pNj0mH0Nflv7NCYC7icWDxdoFYigOXs8OeUBGUYfOvPQoF-JTIR-bmE4ZIs1ZXqSg7rE2Q6JpwVuaz0nZFQ3Lu_x040VUpab_6FPnvNpSxXoL7WA-2ACuBq87c5OzTyuz83bxH6Tv-2BKhIESLVyOJroAt4yS4D_GdQXBKZo7D2dWvsYqBs4I5AL-m5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0AjEvt2JVJNiCKzxNRz2Bbwyf29MYFl2eU3dVNDvk__FIlsV09DVwJwamyZdh1iEmpw7og3BUQDEU4e55JzgtWmwkNgP_lRN_tcFDzAX3wY37fVCCHNCD4_HrLZMc6RflFrczqA3tbCmtaE_Wh_gSC3X27lbsGp4Gxqu2tAnvdPXUV9d607_T1dVA1Yba-yy7vsB01IOF4AcT4OBASQIlyWo0dBZWdZpMHYjiHN1hDUJkWMIShDDOA1YyU0cAO3xAawXV32FcNtRBT8Lrnj16829caeTFhO3VYksPxVu3_AYc7j4s_qWkSl9m3-QtN3T4zC2sbwkRq74s8si2bTbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g8N8WsMkwWUiezLh8SChiGExKqrXlAeZn7DtCYWYWFka4ijRBWUBiEemaipEzwtaGHRZMCuBCZqKrWuYU7l47OZK216dof7N9-m3dAGUTWdTVjxV2leE3HCsm9rg6mdp9P9PMT15bLXZ73wiuShlkgjQ5qY_o9zcn0UPiFlg_ZE04QZ9O-X0JsPJ5Wj5BfSET3hg0hXdhMFvAys5YHLhRRScHkmKxSExTBzgzBp--q-qRyni05OamaFJrLj-jNz2A-gA10xm1ofgPnytIa8HN8m0Fc2AFoimH2XDd4oEJiDN4WapSFGq9nKxn4Q3Cfzt-XmFMqy4cC01aPNlyLznxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpCaqfo1j4sHT1RG1b-AzL8yLzPUwzC8UZ-96JX2l6vPffc8Jjzwr_OmJWU85f_QiOFC2MUpB0NV_89DgSos_zXxIiuBvII1Dgc1wTdKAHtQoFn1X6PJ28WAw7L1aU161G3lIyDyEWSESmvmBulGVu2hOZXqn5m4FsD373z2-zF59Gx0wwZoRIOQiN-EYALyYppg6H7A3APMCrnCYN37dmvFE284yLLN5b_CbJPJkLWMa8TKUT8Q5gasBl3kqmuL2nBQh3qHiKt8x7EJ5F8d_S-vHV_u1PImpnRUuyYvJmQdf5SOFqAaoCli0L3krwsDQuQUM-VLuWYsCHelIbJiMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5ivHtsOKkUx-DHFuQn15kGhpw1CF50_Uovo1WtG9QpIl7-wxsF_M5tavSD8b0gQBULbpfxy6Ef63BcgPc4cNPSTcprjTMHbOenRZibjoCkYHva0aC0Gi2S4tUZuZpkn09gSmGocCQ2a4yFyWwQxfpnP_ZPkEP9q1_ketHi-7mPh8KRn1KUKmwtNcfodubn6EX6euVI5mqxkeToWbpqNiHDyFjia9m7QlT0nWb1r-qXTYMQFEfr7dS1Gp2YYQ6d0wn-cbkyKxttq4lTvbGWrrMSrKKmnC0UxIDWHdmwHG3Gzg1xz1CyemaXxxSIFU3dwIno9IrcD9SEu-QFTzFgGrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcO7WiKBksi-JwRyejWk1A89YtM6DEv0NV-Wdb8f3lr-TVAuCpoW7sTGb8fECXgFpOIE9CLZnwElsth487hmfyp9c2xCpcsXqiq0Knkz4Nz013kdiQUogHe3mT4vR5svSZcjY48kum85Qh5M7tKpNC_9xIkW48AaQI-ilXbh9XFTBQig9IeVEEMnLmfgsZeEslcwT05P6DjWCWACghchht4tlIH-tqFNmuKk2vNJnpYbBYeR6IEuzeK7Y3DffZaKTWs-YeTwO772kWFoB21-eJtk0gM2q0kIZbKz1qv9fUky4icUJ-2KwRzvopKeJ0owXxTNj46OozRiP9cMvZqTIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5aRKFP3U0LSPy7REfLhQFoPMhf37qYTCLRuiatvCvShOQECeX34lhQZcf9qxlWJYO28-lmiz_As6dKgmNaLiHpo2V1H7AWBXWIrGZRt31SDcriX7KTWPqa3Kf_J6whzaMpZqbQdxcMB9xbODPF1Q5W_J4izK5L_Rz88hpRbdinqamGPVopAOJ8a8OCoNcTvMzkAOfD9nBibfyRkN5pPTS__gfnLI5gWVGw8mWIV90feDZP57rBzAroC7Z6acmWFQ8jfNBYdiMki2GN7XrEl8XRn7f_4JH2NTN8QPGpmXRiB7fqDLZSlO2tZtG7-c7STLRAmho0a8--l2wy1UrjZgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiMHYQRh4w95kgfgXjHNiNxsvksbETLISVTDZOXE9KchaXiGT0w3kFOx7gzYwHj1ty7VIPxzEgCLGoGF7nz2apj1IXYjaOuotH6XxSFj-vxDstfURyAdnhqL3gwwTHmpluMwCvMWu_wPfdaS5HA1EphXzMfsbCxiLfHgFdNmyDbam2imgBg-Mxw9SYSqWIDXqEKTkHxrxfxUUDEIIdeEmEJYDRDBaUL5Eb3KM4mk3YfxBf4MqkLJ3ndvEo5rg6t2qgbJqoSncKTIVlHnpQzFiCUBsPj1G0VQLgSasyzMkGC8IGwRLInZ6vM3sMMhlVmOr3CwKzXlygUV4dJZWVn-Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFusJScuMbaxIELuEMIk6Z6mH7LW3dgls65QLqpD05TH8Zj2kcMMlfrjHxyjeGew8doz2hygiOzh3fbxEwWpG0BP17Dg_Ulou6N4dMUzS6dsbYHnnZ0pNdm96lXjgc706oz-oCkaIzoRN6EAzOFkBpcd4mn6NzB_rdu2TJ4p0J8rugIYdCDEunw_z367AwmICkK88_JhEFKEjL32ikLkIS1ZC3zT8k8-EQR4Ky63Zi2btrrG6zE-RVBVtUBbhxCVEZXhWmBt9jm32H6R3nD_aelVNgCc9mrAwpjmfifqyIFJgPtDx1ArGYcj0IJyMji-AhCt47cBk4TlprCfsS3cww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQRHbyjvxSMzYN-3iSSBYJ58pxOZT-1jUixBYatjpYnBXKrr9CAp3VtlbskJ2EA6J0aksKzV2x4ym1qZBroiILl2nF5yknCq1BENwE2uBYTnUXWy-Z6sYHRZwhIHhrfHT5kQRwEyFx_ccjWLS3GwdsOWVJ-Doiqo_IgVHN9oRXEBRsKgjQBynd18Fvp6y5GpcbeAuN8O-8CIdTxkRckgiB6GxAjdV89gHa5kp4av1xpKIpNgs6iK4T_XmZHloYYZ8tAjKNyiq5XZ2GgAZ0bFV839FXLZBvY24bwpxsdwK36vp_Hs_-CDr5T-Pxr1lFu5DjEiNeoSROakNE09aNvYNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKwfRXYQLzBc-cE-Wi1bcxtFoL01LEMRvqeJQZlUduqAbnXgWFFnt98BhaR8BFV9bZmfbPZmwb6xlwPRXH_PXx2oeopAJy3izT_BRl7_005xO8lIvSGEodyorMSGQcnzooGx0m5FO8JexMOHiu7Fzm4ZV5cATq7jf7Bx3M6XD6aiCR6TLXDGg4YFeU8gU-vp2DGsPqUhgO05Q2rC_JfZGuKTAP0N0YLxU_wd9oOHx8vxvu2fHl2Fbe5zKG3kVn8LiBcp4KEpGT1GBvT_L2FPFFFbAd2hORIz9VzOAfjPXpuSzANWW_sDyiyV-HuBIsh9zuG1eJHFNOwg_hjFdJmPEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIYpXOGnus6KOy8f4qvF4_nAGgz3KZza6MDF9c5H3QDLb8aH5AI5dSvA75_atpk-q4sI6MGS4MTfTfUP0G8EICTeqCNDrAwxoLiNEFyDqTbo0h4CXNCNphrAuwUvQh6MNvmXvO9K8NyUQUqF6kIYYdO-HhsnB6BbLRzlkjxLwNepjFgU-LUxMWHVS0qtwnBzqMXT8Axpp-M7XrO4iC8OPbNHPzY9dN-i5zcKE-2WRSWc9A3iiUIjqhIIQ8ZoE2D2iIMbzeWAarPLWObB-P9Qn0B5IZjo-Y_h9Etve9nu0CGrDu3DqlSB4T5EswR_JPFc8k_L4JRlsFreiNQpU9aw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htnRDqqmAsYS8b7bqRAywpGoNgk26NgjIWP5tzMVwANbZ5RwMWYcCszuLrZ2A20akxycjBkHA40RXQTKozjhLpCm2wPFIywEgVZgmviM5OJJxqfgMntwWTc_ZDhNule4bMXQZlul2lTulh9IVrahk7ofUVJtLL5_jjNZyIe9WzW34G5R_wRSzKDTf5QzDe3oVOWP5sw2jgqEEOd1_JZoKFGJMZn9iHO28XgCvkz_EQ69j7ZYagxuMm5eKYhTg0pRRW8CE0bkuEae0XM7ZxYnE4B5doUkJOFA6xoLxVVsMpN5DrH6ck7a_7KQha_I_nl--i5vVWZCXg28ylLAgSgarg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9gmn-17cy3okHabAmCcLHWk-6E-PbTVrVLWc_naRgUXj4L0Pjt9bhuZh48Or9FKqnxhDzV_jNDwbWRJci7cv4CSEOu7Taca8qTHGPLTWyuzANDuF4hiSpQi69kaIvfwMJpVBoQF_7dSc7iqpA8j2nJCEpJ1XWyQ4eoIgZ4Xcx34Cxg4aGYvpsvdPriwMrxYG2-b8pe--_5C4WSGmwybq43vqLgZx3_HTYqTvsoYmA57MAdQHK4fpqTqAltFNQepnmnuIKcKqjBdVSII1e6uPFkcwzYH_3n2G12VuQlxHRnXrecNzgnxtHICfDGH9PMflrEC36AFDwRYayrJnGPJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIRIPLEVUKMFG5s6AUNbNW4NPkaIq5txPMEUX7YcxkFEvM6wB_7fIPQzmiAe4P8nnU0ug4GLAmsGNjaD-w1aZ3VKGh6NW9PrmrQaxr-tW5P2L1_ot4xwBFDycBQsYsENkVn6vkVslnY7mySMUhWmB0DFvm-G0kqE76VeWnhon0k7aT5BdHNkpLeeX2uSxyx4ANtM6N47c4wqLiJefJqQU2ungnBC71xo-6p9OFunk5UIE8DJdFLuSyhw3W9hg9Gq3_Xctl4Ln2iuDGbNRmxqfAiaqHVZnUxYNAUJDoxWAN4uFJyRXDi5WH0MGTYY0KiW2-pxNhFeh_cFP6P-jIHKbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7Zn-ZF8ZysgGztCEYzCITQK_mBiMDMoGWRFumj7hGHOL8Lp15PG9RdezRowHeoklBqlapp3GtBWKv3EhkpmOVzorddq77vRSV8jP37cu3VKbIAMXVNLTWzQxhLxC4m_FSapaM4GaBLAuPLEcet3ZOE4fAAs5RPrd2mwWC4pXcwo5SSdpv4ogREYcLW07lHsDhxuoLeRyeUdEcccv1XaqQIR9_k4_GN65sV3vj61VtArLeC-ZDgc7RxJ1OmCaaQxPn6yKjmWkwRmEaVPF9qMyyOW3K9XKDiyR6H3UazruPZyyQ5WzNGlBcTIMkkxDOSaNpVqbNWwGxZCEqTrCIz_cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0dMzwXoF8dEv8SRQ0W7bZlqBla8ecticgKpzzcCTEN4EnQE23fFFHbBeHwdU77mlEjOji_kBc7x144o5ig_95cmTH4YiiU5-B_SmHfzWhX9ukWgbUxQPRO5mne0_K4PWdMxRSbaOM0tdN2oU5UPN77FK7BdclOFs_Y2nezqcGBO9mEg3sjGuM4UkW0weeYQg9UJOlSra5PhrQCOVbxjYcp-V7iD0_41ucWzokkNUWviM_KnFmPPDhoP-MJQ5622BigfSLBDWloMdT3SWRdLUFIpeEkn9tW_eYKAnQcZL0ohs79XzP93dgxyfqfbRQay_JpB9U00ip3JoZOafgdGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IprJ3dAGBIgfX8kUv9_Ufy6oUg43hM-cLKLVJNAePU0GdV5sKWly-4sdfYH1yLHnNUY1LZQeFvMiDNCz8ySHSRHwfs1UGvzHbP8uZvwG_Aw86kiuGDv7g9giMBTGX9kDYBSpc8D9nfPkgdhDzUvDIVlGWxAtjJY_MdOPo4mAIluJp0fX0OUhxTL2GzMUeyJlq8eOkbjK2kx63sC0oChRlYuTixu2a0rgXBBO8n8r0FARWxxbUJfnQtfFUouN9-gNZhBeaXn51NYEx7wFDf1jRVs5G6pT_rdwU0EmYWh6ix-twkuSiB8gE7bCdJDZehzfIbObqNLFix8356B6o0orOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abE65f-oQ3geaWGUZ37lpqKfOPsl1Yl-YUbdTP2cQvPXTf7nC-9DqZiQLzhPUzT-5fpOtyxV5PTvlqWOcfwc_RsGeFKootqMyygtFwyGW049UR53HvIjuJw93TVxzlvJOOf2C9ZXaop1Mb2OIkT5Ilv_XKnOqqLMLl8X1vh2WZSuLoiStbMHwpTRA-n0BfsKqHogscMjKaF0HejUh3TIPZQr721HCkJ-z0QJQafo62WzZ63XkK0_fFWiG4WVeCabxGvUBV5PPFWtJWq1uMrTLOwB9yXWTgJ9W7OabTpRreQc_i0GHyu61bP8Wj-iqfeAwEOfmxSinTOKuc0my0jubw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akgVthVBXKG2dmfAfFgwIvhXPa9I6b0zRWl69wU62xG_UFqc-4Je1-urVZTTV-ei07nQN85baJByvLrrI2le9m5RgH5GNhYv6ExlGUWe61GSVVDNQlpBWz4_i8Qfjp0OaIur3yR3Jq8ZZGYQ1qIk27DlcIrSPwLOTKaAgjfjOm8_aS_F7dV27R75ncNDO3SUGr46FRsMbgBypHJVNvZJsPO8_uu1dF8gTq0swmgHvTQuWzQwsVXC-GoRJXmox3sRfvtmBEB9-BVOX9om-JhlvQJuNCUYK-SspdUkA-h8UAvJAKX5DzNOEZNm3942b1H7IqJ0dqMReuwsJSuS4nCqQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VleC9eaQyCp79Db8MO_VX20p0i7X0ok886kT3oSVcMb0r0AoMz8LZ0inOUsKjI-oR1Qr4S-_YuYM_jjmyHTtzSw1uF-C4HXmFFpHHaOoenC14wlGCc8UUDQX4x5PNPxcmMQOjVw4Ohgh1-HLFn1d0RIpdQPtt89uMmJS_rIGwlOMp5Dr1FIMF8KQYHFzfBkXFOcBKOEKrXHck29ajFM0yvbqsyaK1BuHptql0mupscoiwPk-ROHMy_SA2E2yFlo6IOvOeY0SM2G7uIvYOKL0ofjVzzEZFzqU2T6iZJPq-QnFWdxH1g-6Rhx0A5vaytqME-spqVZ7v8wQev5jgz4jjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STCJQJVTUAEcDEWpI49B_72vuz0zWF_sFUJGpN5_DCQ7lIouOSBYki_a7qRse_FXf5Waq7VopfIkcP0hzCTZpfj-iPXWjK04MsqYPnsLXTZfxEQNktsSpVD2hcvnnw4wpmvChl82Ur4AIwZ8ak5hQCBpaqUgH3MXRVDVBWUWL9Pv6zqXwFOfYEwOfEzg2yshWjhseUlrJ4MVuRtd-BxhrNzUOAwG7NjTXkhB0WMWDgTBpY-bmdAg2AzRqqehQWGYWy8zmEixyXzWBSQVZL9Su9VH42qpH-kngfOx0uPTCak8WGkjFZhNuGTfEQCSQJynNDlBXi2KGhisS-SW-G4qgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9oTMpulG34fqMxN7dVKWaZ-qlrOdI7S0UgUL997ut3o3lnWnrJDHbMB-xMsVCj6xkNI1zPGxaaD6ipHe_KgeYYTCzSJ-Se14xZX9wtDFNE7iI5vOoo_ncezBB7D_2mIfAWwDNd3VHrGIkmRaq0m9cHo8U7nkvmLR9YhcKL2cA8MG5Bg7qWlam1QlWmGjf1tUJq4M2xBDWS34F_X5ppBVegChaB8VUsf7axP4oKvq7azsC6ifT2rJ_40cREXFatfmQeV2_UvD16ibvDr3C7GSHmAh-x_OO0WZvrR3GDu1B-Od70AXEUbYVb0yWxX8FA_SpKnX2_DjnHdx_8bDJmyog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtIuaNIsNZvmMXXNIbX0tqqtTqeFePQeU7DA3R_THXY77W7_0x5FYGSkydpbFXZpIFOu0hgO14iGAuUv0hXZ_blG9qrIIPMn1w0oe6k_I_rFCpfCS-f__xzQEkrtFP8ldUcZQbMHPRB4i5ZqdjsDyLDQyAG8yfP2759aN714x6EdTIVBUlxBRRCiorFHrdLd7VMzjPZX7LBg2EKvI355PRKdAj0Uk7keI_k-ZKEJC5gY5swR_A9_dV7okDq0lcZu6rZixnes_-PeHM5q5S105jtH5P-n0pArUt9nMfirGIZJ4LPuFBPHqtK0R2P3yvC_7UUxD7bid4sI-ACinvOHvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbDkmxjmA7CnmUm9_CH854qaNiYjChH0ej8KI6hJnj_67N9O3Xhi4Jtf-WM7EgWDg2gKlr2hQoIwFjYIaCD9qXqAft_eSwx1UO2CGiJHPNSiOL7yHnXws-QPkKgB5827pyYJUT-gcIHLawmo4s8xyitLRreoRF8tBmWbwpr-oqx_M_ghiEYPOu5NTD_Zg8SsjRv_GXeKlVcSoRCENL5SxKrZ3oRnAcnxMRI9AuEEeX-aX528C2fNLwMcpjJEM-4Bl8YSVD7CuWeiJiPSAyAeUGdL5fcvSL129ta1cWEaa6AiFo8h9sP0tAFmlzNXSuDAGDNns9ELXbD2AJMh9s26Jg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=lnVys6BAopFszwJbF6fg8KzcrltkH2M_WlbJ-31C8QaiRT6U2-tiY00S7KzVJWnBKKJRqMZaYKNLwc6w492J54h-MZb4ZQslylsyISj3C-V2aGq-2tit6UL6v2KKn0BVNup5-EQTgjrEOvb9HuVqxhWkEypPg7d2UDA1TWNmHLpu2BJE5E6cjktmCQ60NsHu60m4dNW_RueS02Crk7qsfSIL17rSsGgBBxz1Z9n99LSp49_edJF2kTteA90AwdmiI_FgXXuCQd-9ERzJqnYzvenzunztbbAZ3b-EVJ5DWt7SMMFS27wMrCOrlmJGLcZ9zKBmOAn8HTtfQPOoy9txxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=lnVys6BAopFszwJbF6fg8KzcrltkH2M_WlbJ-31C8QaiRT6U2-tiY00S7KzVJWnBKKJRqMZaYKNLwc6w492J54h-MZb4ZQslylsyISj3C-V2aGq-2tit6UL6v2KKn0BVNup5-EQTgjrEOvb9HuVqxhWkEypPg7d2UDA1TWNmHLpu2BJE5E6cjktmCQ60NsHu60m4dNW_RueS02Crk7qsfSIL17rSsGgBBxz1Z9n99LSp49_edJF2kTteA90AwdmiI_FgXXuCQd-9ERzJqnYzvenzunztbbAZ3b-EVJ5DWt7SMMFS27wMrCOrlmJGLcZ9zKBmOAn8HTtfQPOoy9txxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd4DRU4fSvMkYVwhnFUX5eXdtabYzIPlVsRLsMGaxfFKc39aEhoHKt9yMhtiPbJgb8E1yTX53RKzjfFbW0IP4_HcTuxzueH5W-iobne8poIis_mVYFxVOfCXDOfmXTYH88-YUt-Ku2b-Aly7dkcBRW6su_dT3DAlb6F-cggmkUeVYAnVD1Tz2fdq512ZJokquzsmMBIDvZBLvDFYJnQrsexUphdGDjypJQ1uF4Mc1sL3pJIh_kVUMX03FIIdtvdObHACPe1lO3VvI6NXu_3jd39U2kkEJQznHpUzwMSFbdXWTv1G58KWCB56Czbdp3iwqsm_umWYBREG3hGFEWoADQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjkYHXAk-WbW4JxeuvlnBIvacIA8KdQLlNUUEfPJclZ8ukKZ0NT0MQQrjub0tSK43-cVwLvkUh-qiLxf5oNpSMEApLBM5ffCjOh_OpfUMS0xQ40WXzpsWYyrPfN04rUt4ZqQ62OM1UjEoGEaBp0-HLRVDQgNAVbt7Cr4MN2DHfN07xugyWHsO26z-EQnxACBji0wlzp6oPnmU3xYadwCS0DBMXi_YBBuqGEHek27GW07JmkhaALwzhEYfXXoEQab3nl9ilfHZJJIRhGDx1HdUZasL-ASmMzhzbFrOpNxFJLHG-Wpg4uCzGWtF61J0oMavYugVZ0hshEgT4g8NnjbOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/drdSJw9cTrXz8cSadf9nnzwpy3zaMk8v5ejOefKTNvbydvuAuksj61ekGTgIdJKNRCbdIn8VMSrrRTfSkseS3NdXAb4v4OnwocdCDsoUYHHs_nGZ5jhnxJGhIcA9AnkysoGv8MNNrmyhNVVBeQMpOR2uYtPy3-uoja4Ay9iTQuYSNGGHdxUAyx_kCLM-rrKdLQvH496QzLSSmLDTRveei-eTsngyAyctlqm3QC_DuXB63IaJMTe75R3qA3S_eD8lIFAyd6oIDXVQfaWtdn7Li6bSau2U7lytCeshijjIyX9r9gKHUQFdh2jBCTo7d6q1g1oIVg0kLvhk4DhP0q7HJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mT9d8XRXf1pRYmtiB-HQ73BlSKgokjbiCE9YvMR94aqS2vyZieN2eHmyHbOIcpKHHjW6IcNDQzK_mHvMpFeyjoSjBpgN0ierEhpqQdt1Wmjw2nLbtoWa2X3zf85ByNIbvKTiBeza98x-lhGArrjaUH5kfD9k_5Mdc2kykKowt0jrrP3n9RExvIJRR9K1GfjGM4Q__o5DxiQ6ChQ6NX4JSUhDhFmGggIQhFzMwK_2PegrhrMwu4NCzfaC-ClsVXgnlbMvQi_4zVsIqh52_rncgze4NTRl2UGQMJn-9TrTJ4tK1bQQ9NHHEe4J1sBAznxwbbuoT5kMpuhFOhJ8flOSDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7BzeCV-cWslnYGXF9M0WUx4YyruijR9vh-j48hQUYxZVss_m0mKNVIfFrGwC1lo8qg6lIhe5DdL67_rs2zHX4UgA1oDnTzz4ScgKhh5XeDZrBVwUHPuM_ZpoGsoL49E0ajphukJwc6aSMATmyi7Ivdv8t2C-IrLzWB8Odg52wpNtazP9P2byrD1_xNuMKUUwu3vdGXsw107fkLNBZziWOTxNYqYh2nX6TrTweP9m_wfJNw-38DxInUCizYHicWLd06OJcRYYUP33Z3iG_VtJZngIRKeY_THgTL9Kz1zil1Pr8lu7Ni0dmpjGCcdLoWD3sHIh0RWIBcnu1eZgexPbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9liDDAn0FsVFoZ4Rx5ne3MOIcSBTlws_eBtHu-K5-JMaWiIakM6_zYtlSM72ULrvNk7vSUxXCqrYff-_rLEPVZp9wOW-I9KFEnQHJzf_1LrcBVDyq6-nk4URjAf9W7iZl-7r4wYCkUhHtM8C4Yxm_LiHLJv-W87a2Et1reajJp93bvo4MXDRwD7goyt4DZwCY3ql592NldQqQ7ILKx3XhZ8cZEJHUcsPGyGAbpmRIHcvBiRbD1hWqSQqoV8e41_Zi4Dq-A-lg-3LyRRqHPHti3K6h087sDY-zRzHo7xgQdh9pkXzU-CjL6mBdhRKBzFyply5RApv3AwR9wrCHgttw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=KziDbCe0DWmUWXfcVKZQvAtO8AGIMxdTRDCqtHxKeHA8wd0OAUp4w9ryKKEeWUk81NiwNX2oH4wy9PYIAmhmUsnHtOzVbWoUueeuB1z5E37FqBIrHaGDwZHC1ROQsHD59dd5ktqSrmqKsfRhGj706yldedJIBeB98D8EmxQfz-gizHrkBD2RhOWKX5T_ZNXQ1sv-zBIr5FR55c7gx1dLpxFstfpr8sor8mSRZOCeIPgcF2MJb6r-UIjXMR4XoodfDCHHtz1KuZmVdnXF5ftUmrYp698p5G8Lm-GZJeLMZlm4yzVsw1z6CrNfp9_6rnuqzK-ByqtPM4K_4-i_cwxgs0d1USPtwWIXi4DRDcQoG09vBEKOmzh5spxYYrWARRz0CsxyPh0_AICJ9bfgkj4TDti_V8ucyRAQmOU2j21cFCIhLqinFLrSO6F5I4s3mbZiWYSfc6j4eq52I4vqZEVG9EAHTiBzf_bYoKjEM1_6uBPumwiQU_1Avhaka1NO_JigDnArgkTRLZdzFtX0EGryIQE1BZp3kjACC0IqauShojToSadxKQXkYzgd0O9kk5L636EIdkiRsWZgNZ3UK_TmZPFpGN0S7PLY0ibOOF0Fo_ShFBmT0YPG-MxJB7sdw-hTc8HF2gWQDIeXelDQrgHQ50Tzp_Yhh6I8Zw43cLvMdRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=KziDbCe0DWmUWXfcVKZQvAtO8AGIMxdTRDCqtHxKeHA8wd0OAUp4w9ryKKEeWUk81NiwNX2oH4wy9PYIAmhmUsnHtOzVbWoUueeuB1z5E37FqBIrHaGDwZHC1ROQsHD59dd5ktqSrmqKsfRhGj706yldedJIBeB98D8EmxQfz-gizHrkBD2RhOWKX5T_ZNXQ1sv-zBIr5FR55c7gx1dLpxFstfpr8sor8mSRZOCeIPgcF2MJb6r-UIjXMR4XoodfDCHHtz1KuZmVdnXF5ftUmrYp698p5G8Lm-GZJeLMZlm4yzVsw1z6CrNfp9_6rnuqzK-ByqtPM4K_4-i_cwxgs0d1USPtwWIXi4DRDcQoG09vBEKOmzh5spxYYrWARRz0CsxyPh0_AICJ9bfgkj4TDti_V8ucyRAQmOU2j21cFCIhLqinFLrSO6F5I4s3mbZiWYSfc6j4eq52I4vqZEVG9EAHTiBzf_bYoKjEM1_6uBPumwiQU_1Avhaka1NO_JigDnArgkTRLZdzFtX0EGryIQE1BZp3kjACC0IqauShojToSadxKQXkYzgd0O9kk5L636EIdkiRsWZgNZ3UK_TmZPFpGN0S7PLY0ibOOF0Fo_ShFBmT0YPG-MxJB7sdw-hTc8HF2gWQDIeXelDQrgHQ50Tzp_Yhh6I8Zw43cLvMdRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEuEE4qWW8QXvPMVrPezfZ9o5P0Nt4zEhk_wuFHJdz8qW8cfrR_WElR0Y4O4qhTk2BViENyXBMjNmhW3TFxZinreuFFWRA0VGsG0JCCFWSIGbAvnWnErSEX6Ogospj0dms1H-1HRXYzy1xHItJhfyb4UzOKxchJKqDEYS8S0o2JFi2Cv2Q7zXlTffO-2td_kOHyajpR0TIzKzgL4gMH2GSxbtB87VGO84Nln-vw9n4CDUMXG3ornMZ29z2_nRqzRUHIzXLM82w70ISoCQN8JToRgGnBkSRnTxra3Gw3Wmac6LxkvslysXF7-omoNtKuyQ_ga8XwBz_m5nqLjZ2geEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8X2kmtiHeBJDNk0PeW6sT2RTCC4gTBTts2mCZ8XLI3sZMNjmNkVdSKB-2UWuHev3jMZ9fF6Gl9Y8BOlxFp60CRBNyCAEcVdHcFWVIT6arrm2_73Wv-H6WuPziGUCeub8UXenURL5cldOI52WlbI6eEMOq_BONRDKjqgkcigIEv9mfAwakf83pL3g0f-gJqmx1RuX5p_-KSB5XvLnypwZ21l3eFtBtNHW2DF-e49pnYfRFjx7N-bwQEMrGiSx0q4GMEiuWx7HLFbXxFNz7wi9UXM5atR3YSwqCkcyM0BarBg8ytl6n2UI0BAACOfc2HQdp-IVqvUmb53QNqAhCsrtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rtdt2882N-evmEDPIVZZsej5WTmXhNGvfjS9YCsRIh_j4My9ZiHF8cwng24Rj-57sBKgTmyJIyyb9xXJrjh_PFwu-qufXcnSHVP3GzW9VDxhxjgiEs0hbtb3UchG4qt1B8NT09PGn3QZzBfKF80c1xbhHmEHsf01ZkXX6XGl7zmRrWrv43bj9UTqjCJG_lwz2AuI6BP6SBK0m73HiLYEY8qCE7BmAxszzzchCiptXGxMV1pIyfA27lsg70TQHzhafZqPkPHUc6Eixkq7lc3VHk1A1TtWYVN2NjyP7JYg6yLy9KoVCGJ1qm7Ee52wdp2ts2tmTPRyd9h8K7qA-OqSsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQ9jnGFkOVWc6Zs_HnzHUDmIqXMCSt5l-R2BkkdkA7jTRKWjOorQ0nRNtLeqgWaWnFejYDZbUQpA_ut-4J8ByNfOqDc5_Xa3JPULDo50qFBtS7cAbjoZQwLzmZyKGnHyQJu8FEDVYs28xWhGu41giqbbzpZtTZD-6juxCKeWW5sKFBJVLm5IQ8X9BKqyK4qG4SpYF3fKfeJFecbhsW-SXfs0HXvON_77u7AYxJpUTejcC4D76YhlFAAt2QjC82j0md-vwuKeaI_fpjTvu2Fzj_Qe9vFKdeAc-SxmAWkPYoCfmMrDFVtJT3HLi1zed33PbXbDn98Z5D_oA5qTXktyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2wfupJuUI0ojY1rTnnhGTm0e_aWEASiU7scoIXIOgLWfrAPclsz8kjyYnzefSU7YA_z2hg8okfjbxETxnd8_1Yv-R6kzm15ErdfYirZQas9PwLDNRjfRqVI--Yh6u-dKe3CQHMYo6KFUXK3nmbkh64bZIawrYQAN871DWFg7wSGgLzYqWpe7IgMHR0sxLlxJ8wPvB42P2tCZiI3Mi9Mhe0_fRPOa23U462qxtQkw030d6iIxT-DTo-4VyWUTjnXodiJgS8pbQR9prGzkNhGfE4CE1GcrpKlJTaAJcNYa7F9fJZ2Zvu2Xpt8rQ0wzGmL7Cw-_7qIvkUzo8UvxtAhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APJAAI4Bg4vPPcOQJHBPX_IZlNfmhNKAVHcfebwGQRshGIWiF-RDgEXlNBM8QJWwRjydFLcp6-cSA5ln71LCp_aye-bO5Ld49LgYh77pgSj37OXvuQ_N-hdXnAirW8ENE2q_G5d9eT5EKYR7pewDe7sF2caY42DEM9B0u5kSjKqMVLiFacwpz8aFPe8YH1abdjBU_SN-5Ns2Q75hksbZy5wTG7Nxdz587NVva_IK3-ffbLGj9BwcAM7Q1-UhcLMBBC5KfgnIy1XFZDy5AwxJDRc_MP3-_4yIxDFXG1qTcnpVJyacb0aZN89U_-l0HdDYPPTcwEHZMlz5i_SAjbupGQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkVtIlpq7qNz5CDqx-OdMOLaP8UmMgkyMJw4yteFHWEYV129lDrGVcyW0nwbAmqqtceoD_i23R8-G9isB3G1Ei4Q9q4ngyyT9D_tMHYTFxuGDj69ZenleP4WpCo-7m6wYYdab7KoDF3cWKcPhRjIDDZhiTeizrLDtQqh8y6pOk5Clz3o0O5i3tXxuZYbf1GzYs4wxfMuRemthUAMnhYYr0vULlnsV3n6bv7ed0kwYwdi1tSkt_CUUNq_OTEF6zcTSyqmqUsjnbGVHnfRtAKRL9bDk_I0H2AGYaWdqOjqonMzcCGVT927ysoIUh5IcG5whRuHOm3BRN4L1OBwaERa8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lip89W0aiM1hGhp_AIO3yR46LY7Yc0LblNa-3zvwOAFggxoIxza5r8foh1I48PSlItqnoIGAslcQ5V0J8ujj6huEtU7eNPobLGcONp8LkvCvKLqLL2Ixzqcb0z6W_1Fl16nyaZbfT75-VrTykbYUFmKqVUyuXY8OYqi69ZV3YCvioDppghb8fvbCAuJE1n7V0XHdk7K0NLZrqoEqOXPO057jGH3vjBglSp9ZJ1DRgNbY6hsSrlJZpCvIbzmQBtBddXg6c6eBRu60Ycae3xH64K7KqDgFOOjhu779iY3u3BwWS9ffkEmK3nsNwQ8CVpul2N_PWem6aKiiWFMzU9NgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQJJHJM7v1FE_q9rTfLXtrfUEbj4cKOTsFmsHjSyXBof14M8FcmVimz7geCq44rMTkxrwA5p14pX5t31NElcF2b_xpV4U7VQtX7Ly4rC0v7H_I3MykkkDZjE_sGSUSaKYhxQ5h-tSrhWirhEU9FZEgmTVahzHSDKAgI2rHwBTG8bAhuhKO7FI9TZY2Ff7eC1NnIeXfVYE1GGL32HiW0nTD_CwKc9X9NqWSewBUbz91rckPW_xhpinoZf6x-aT-LBSh4yLUhV7KxFuH0TFml4fk2kQFh-qAXTpL3BCbqM0nyQbfWLF93UJyQ4hQ846KTBRUh-nZwajovHfBHL3bKQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZ34V8QnGGbkIaMITZf3Z8kHqYZX9S-bXzVkby_JOhtgcDP5sLtZn8nYeLpvumlUkU9Pog1tqWIXdVVbAKrZGgiY8N5koAW5NoLrbnK4fs4VKDfGRq3X2An_vE2joxS_7myEPdDAUOzuVhLXExMJCqJ5Hq4a8IB-PvWV3WYmHXFPm3CePntmHTfKU0xB2-MDM_jOcSvuSJrXZdQxL_i6KCGUDzK5VgRM_oHlrmkJkXbbXydLSrswKDgt1nqa_9F8XBASSZ_T30EbyLFJktdLQA8sjcBLin49VSpVwgEADBkYxvJt-ZdwPuyZn4eo8slWxl5yIgYJ-5z-Xb1y4QS9SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FulunXLwxs32vX2WeSqpQgnkPck8dlJdaoxaZp1iQHULTSMFvlUzTa11SBrPw5OKap6ug2KWABa4ekdRoyz5ayCh4h0pdYRJcCWSu_caZFSCnsYUHbZgbBycZAzC-bBQ19yYEDNkg__XiR7jlGkjdTvirojEL1lhBp7OXryXxEfUQBbLS2NWIh_lN9aUrE-ZC2spkOzvTm2NKxmPrpdgNvST8x3JHH_EKkPufLnIYCQLlbq0s4IKOrdzvCCkMMSEErD5SPMZ_aIw6ioVUOr-lQlqN34VlgJ5y2Aw7OF9Km1FLopgrq85pxvQgH155fWmWf8mcx44ho0NV5QlW2HV2A.jpg" alt="photo" loading="lazy"/></div>
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
