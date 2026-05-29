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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 17:23:55</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 273 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 371 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byl9m6IAhbDFVpW3skiBpPV8NZ6QIE6sWQaE0uEnOO948IwB7UPT6yXcEOfUt1rR3ufRU4UELkcxklPgppY8-ODR-6H1kA404kQ_ACSmbdwdN74D2_Sd2gwTGVxsKCBdFp3qcLT8ax_pYAckQ8vV3mcrKR_2Mng0RCoDxJp-X6tNaoL21m_VxGUO1N3Dp8PXzftuEEcLCHniu95PtfILqqrAlbQg8T8gc-GuX8Eo-WQEA7rKFEOlmExbWoLz7LVeXJlWUOUBt305XsuqVxA0MrOK5DcKrv5FnZ6aIj0I0R_GDcFtjTv3jUU5fJzl_ZajdA36ja39wWCOSZgY31NdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 468 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1GNf5f8nH-Flp-s0W-xzPcWFGYolIE-_d-7NNIvXeI3DLvCVe2FSM531IDVVt33cDAtwm3qsYeuOnTDKdlNvHsMFnk6uPcFNOLEIzE_DjhFotQrZvLUopDwt3qK3Ms9_f-HeW-eU8f60-5J8B0Ev6q_cLnAV6vQeHQeZNdfeVFzK2kzgZ2Ihq-rAhA6ZBbZ-ImOiyTuuYcP1Ha8xe1DKR289nabNo3TbeUaFMBr4XpJamfcaXeiN2azfvjaPQjxx1qut_0LMh9UZW_PEe7xqVZ12BUzkZxIh0UXGjXsFEd8rHQ1zKmr4yeqa3oV7sC2xokiegjU0W9c8BukW0Wy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 708 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgwyuneDj9GAI5YA_9hRVSKzvMZriezVWViYw-mApRFE_qQieQ-0QG0j_ws7IXob6gMdwSWm3iJkbkGn7GGTTq6HjNvJbfdOTZIVexgWUZKZ04Yz0DGMmfH6SDFoYPZN-ygd3vd6K-yySGj-rudpW7-pJVElVU7WMcKFEYO952Np1NmYTs3PXsF7tTLKqLl8FFYwyrWAp_lOqWctrvEw9IFkIOQxPwUbuAOjtjxUt8hz1JMdrGZofa16raZSxS8BtBatFzgk9xhgMWYNLLU5uW_tOpsPeIvJLiGDNq1B8JUh7Z7oHnGk-XYdHuWf_4dWju4m6DrxRQQ4y16KsVCBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 868 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLA-AMC_DM_sjk-yDlnkBpawv5IpfROMG-Eo-kdYdPzaIBOzHl81UfLWEVnW1JjJJ0srD-2P5mgetwEQYDKzQrRSm9yzmz2S2dNCgjAVEHxbMTuR7oLFWVjzM_nEbRvSrpv4o-9KAI857Nw3g9kdKUbHNc40kFv5fQI7KaWc2h5hCarPyG4f3ShkYUWEp4au5QXw2PthlyoRbSk9BsScZ_KD-GeeZcPM6vlvSnsdTj8H-YljRCNzPYP9TmVGc1OGyGNeUWv3k8FQ_6NxeVxxGyXkevFO-7fvpj0VtVoxGJpTj6Klj1FiJX2ocNsgwEL4-hAypOKw-dptPOG7EybK4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbDpYM2Q2sEKXrUcivIDCaIeqW40ALstbrY3v9W-2lPkU8Kj1OTHEO0WQliyBPSmK00Cy9DRG9-hd7XfGE9jsKSRtuuQA0vyj2qbNjqy0ijzd7rgOUZAJo9SEnkIoCx6pm8jXzB_dUhKmXA5X5E0ykKN0Sm5kh509JvCUVgYa99bYS8YxlvdbvAHJpIMQ7-MgSLmQROofpDnYfZDcUi6SkGXwbPnXq2fVWa6lOu_u_LuBmLU1dh0OSyrh4xdr7ddvrM3rs0CeTTx9_1VzfCF9fd1nzuxs3ESgUcHqfCM1HtQHVW1dmzBb6PTylAibalyDwmpz6BcdQja5uaBAdFn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 760 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 781 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SakPz9dsx5CwRtUrSBq-JVg7q5Ov5L9F-UeWqTa19POUY5IctAP2a9365Y1OpXA1uV-qbhvCqD95A34pGQT2-UjoP9SoowmoyhoJv_rVqKYkkZI6SvPsNuvVr-EofDCVbuvdU75oZGwzLkSdGOxQGU5OhnCe8C1kka2iMmvggzz0KkZsJep2vmytpPAS3ds_rjuztte79ZEIoelyEFpCYArGGNEuyOSY_V5UKafP-viP1I5ZmC4GYnkdiH5FaQ7LfybWXwek-jPmfvMT55V0w86fP9bcAUu6Irq-MR-OlhkjZsXas9Bp_PuIW7s2JcyfOupgveXWlihZdMNPZ57jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFx9axArozX9kDmLfYUIczksX9VCSmbvDBD8AfUI0YF-0s9V9pa3-olMAd6n66euvNXpelbFNchW3tBX2JwiwhMCbJMiEEe7pevbYF95p9ardx_36utqhDzODXXsE9poFnt6C3YTqwYOmSgjDubXb9XDlnWR38j8C0NO_ZsLBESbW3xXDh-5zY92gASBdJpLGVtWLdDrvAf3zbp0wNN_xpcJD6UIYQPAxDaNdkYfvIe5aYWcKec2XrkwoC4FOEvMqNLxki6bya45EOOd7hJGb8LmmIoB2v9CZu4s9WuMpTvmnMUFbbvCuiqKo1-2pAEsq8aGaKQAdr3y7xONx1Ax2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btX8LxsYKRHrXrKe-zlBqgxy6an6hnVLKFiyA3_gw-W9Ef3rya1MHBENxTBBf-ZfAli1_hgw4JOxzUfnSxlSiiuY6isa5sQtgk-PneMFz1ipP13folgcfXv8V_82Cnj2R9qEvzfnGOnlYPdUJWmqt15NR_Ahfym8l-30JxNJYLZXLX1fGNTpwq87kDh5fu7RrM5Ips7Nkiuf2aMasO63cQ3pygB7vaaJI6MwZYy3cek3wqiawuBJalG1lcYYgRjvmw4OyE_b09NbUdutEVZEslP9vNfQpNKSCehI9A_kf-FK7D4WzfFoIuWzqZUGe95WXUkdyY8xFqMAgj4nUGjCwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 858 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 871 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4HLyj6nNRr01_l-XGKAOe23R4WcR7BsRfHWbLYXJoEAIx7AmWouqrguW4FMz8ekareYnqTtLFvCNctQR-pAWBL5_c-qoOYEr8TpkMix-2I0Uag8DAbW8IEgMvnEokrQYC7nJGPoazRx0IO9T63nuq-0Z0l2GNn_UKwb2yhc_kE0UF58fChn7WaSSQAC62E1gieRqOZ1K1IUYaK_f0dT70USy6qIDjiO6oBweS2xKMABtZzzho2PnNiJubnW6uKMIjDsExdc4bM0Y_xoIZcHhS3azCcJC8S8ZSkldFQtsK2F8P29C_ZH0Ay_O25mCajwudgkheJFzaALUlhDzrgSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 854 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiYhQw0bdtq1VxOZ_ZHUQ7KtwGhjVTKtzJHeVtBKe9xSCPsntiHt1uWC-RoZQHffcag1Q8rD4p_B2D-Zy76kGz2pio1gqdfARR-1HOZ-73B8Cy6knRsnotycbHWLxNgsfSL9B2rsY7k077Fw4t7auDYSwOFsfARvSpi5HraBiZ7_mKpOMBPnm4yPkrGjBU7b2H-eyMPxvmcW7fDv0ees3sulivJk5YvdCJA7jckWMjzIg1n9eEWEG4F4ahdwN3mW6MmRn6llCGWUt-7_3GQRitWbjXl00mCkGoYs1i21szMgHhTc61868hzOF9W1Clpug5saVJdC-Vz0pMfxs5Dv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 829 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgXB1h0j4hdESQcpYX3HBEDcDEtowSvvhbrK_WZAqFjbPiMBJ3j817UEdKnLtWXwkiMuBE05fPiKdrvZrCsLWs2HMFYoIwqdZn_cr2qF3oZztsvEZgdsKL3ZmWPIEMFwkk5tkabCzZaDuHHJhdGf6md-IpFNxwWyT4EXANUKUkOJkxVv3aZ90_HuKMLMM2EErSyE6XEFpq4xJ0OJsSSyswBkWBibK0u3JAubVRP4yUHkD18KxEzLRizi3dIEswJcDccVjBapMB1fyaM7ZPFTAh9ogVQMudOO85OG1IOqp3HJFlQkt-FmnXDPUUPyIK3KYaPIy0r8BKYkNpcFzvyG7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urwh9UnCJBz8BaVwSthv7NGR1x_FcQK4awMOtBVriO3ZkNuLtZFALofRXf3z7cW8HVM5YakVKI5Qn1kEmwrvwIX8e5oPosy6I8XAPmXRm3E93pmhj-vapYfKxUmYIGefmYrpDiTRUlhQWd1gI6Be4PUGy-Zlf-gnN6njvXq2D1dJHbxFyDpjpdpF2Muxds_IOIHsZ4qi2Z5LJMp6Nl99A1r7x5727hKoBV29YBJr_AIgbx2QNG_-359zs0LSYAGwcMckptus4KI8ELoYVSvXibAeMgagIu8Qk171RZvfSEf0tjaeYKzsyGQ0CbLkJP14uBp03MF9NM2c8VE16uXhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFE0SWjO_9mG_UJNWeksdaT8QrFhCddc42fJp9cHSt119pOpPQ3ORlfpa1SMBiwcZZTM4e4EoEVQfd0hd0MFjUlMJTDTCkJ27PZ31xG_MvX56AQDaJGzfDCW5ifJ5K_fh9enWgrAu73I_iHzWZDpD7tEznGchuvTgL-MfncKFeSgh5IDBUV__4zZ-MOqnZFjUm-u1zd8Sd8LOoHOwjlDgycl7ZguR31glQr2Rvt794i9HYM8F-SJ3htTr0eJM6Ql5ZJGBD_y1fnUwuqXY1I0IckbB9BOKO35pNbi6WrxGbWjKzBz7EtsGn0-RBPoF0LDgIOvzgLcgAvPWr7Hd9-rvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4Rk-PmImy6wK8nG_jmqQfN_PuZRNxhRbSqt7pLCFGWtP3ttopDFDMsNEPrORzhx910F19kna0xPQx1IHjgE_yHO56NE0f33VmvxmaWlwcHTzjCVjbRoeQydv4BkT0-Y1nan44CHsHdtdjo5LSD3xGeu2LSfD04wIy4ZCiTH_1enwrj9QAvwwyTn4UTOL3hqEayxv4MooY1YXFOQ_x9Ln_BYtDO28kK98f7Qn1jssV8sYQ4gQyqD7JcO31IA1EedpBOwIpBT3Bc_q_D2UJZuZXtlkUzVtBI3afNHUGsEknNZlE8n2QNDHiikIFI6NlmUV6cWRI8BOP5oFirg3rKyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_ZCAvKsoO6Omm7bUc255ffSJfC5l2-yAwC6jndWtcJOw9Z-tmlwfqTlFyyLJx9ca8sT-X2MkRJwVvYSTq2mHj4aug_bLwAnLVNcfUQIDQuhbjOM79dsdagno0wFOfTj9yA0FWmwhvGiyTDUeT19AdNZBIuPfb_ESyjbNRQW2xJQPYOfk3UCNIOd55CCnNWOgHsC5ct28qlEllNEsGm51AV3b34CHb_0do0C8SSPOdx98b-mQHDS4sJ640V3za-gIhF6SZV-TwXVD_2_LuUOUQlLFdN0tG1gwGe7dOYL83UGfOI1RnEYqbcoyWigc04FXS6gJjYLH707BGR2PY0BAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 950 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuivDG1W9hfS19PhR9WxgVnWPPXz9pEPb58ISKtlR5FuG8KlhOX4QLQAvTAme7P7JUiSSr9cjZrNbG0RImuv2h80UrPCyGA2XBnjYusv5s4ZOyihOcc3O3D6c0Pg1HtHD_DktrxMS4LjBxeqxKaLaPtfhCerr_wFjYwk8O3lfxGqyva-3fP8cglK8GQNhkW7SGSnbKRlmjBqihK0iEUSLgso5d8vj5XjOuBAkaV17mOACb-IzoDCvSWwbA2Oxx8XRpNDR_-BdxlDi4oPujip717O_7jpo05wVw1g0W9EHYQEfcJ0MHchg4r-HvnJYs-AEqgMoPHayGSUH5HRe1drCg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZnNEiDcHGwpsFGq9FGn0YV3kQd7vVCubnRE1d32la-4STpxy4Tti6Vlg_1D9ktZDKuPueELSXWwRyfHyC0yNQVKyfjsJl331XHa55_QWTy47laXFRoNIJ8575Ik58FNZb-4YdO58nbMrK-DzPCZ69rcF6Oqm8pd8GvO62YKQanlJsppjbTK5DeVr_jdyiYMMVg11bYitWvtN4xQ4FMix6ToMeGvS6lav5SkB3wUo6jGbh73do5zmsUN8gAM9sdyEhSdNGyG8CRo0ZCdfqbyJxIlcDs62XZhTKQq-AVBzAaY8UmARhp3Mw0Ly0lpPILS19j7v8eaD6AmHtfrYDfRFaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=ZnNEiDcHGwpsFGq9FGn0YV3kQd7vVCubnRE1d32la-4STpxy4Tti6Vlg_1D9ktZDKuPueELSXWwRyfHyC0yNQVKyfjsJl331XHa55_QWTy47laXFRoNIJ8575Ik58FNZb-4YdO58nbMrK-DzPCZ69rcF6Oqm8pd8GvO62YKQanlJsppjbTK5DeVr_jdyiYMMVg11bYitWvtN4xQ4FMix6ToMeGvS6lav5SkB3wUo6jGbh73do5zmsUN8gAM9sdyEhSdNGyG8CRo0ZCdfqbyJxIlcDs62XZhTKQq-AVBzAaY8UmARhp3Mw0Ly0lpPILS19j7v8eaD6AmHtfrYDfRFaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzFkH8L0M52DLiuoxyTvT6T7KeXdk3DYu5M8-gfi6fRfQU5Zt6caNgbhcfHtZY0XVawX4uHTJdxI7U00-x5Zp-Aq6c21CiU2dgxvT6BsCtwUvsKX9Yje0Qjw-l5dVAJIldnQP9y71M9TF6247SfqPXmC3siVJJ9zkGtX6VRyTwwaoJbSzbcFuBIW4GI457weXA52JtZGf7mLImxHtcYt1ozLAOFHW54ZE0zW1IarWOTZsM-rwtlIQBFI-xWcggU2GMSbqq8z0Ez7qfuFwGZ4Dc0feWr1UP2y3M_hOwxs_phH7R0czzFTLbeRfiXG8EpSE-BFHUmO3EWw7kod4i_YCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku5EA5PzRQ75H5-UFG97XiA2m2nW3Mx_5GfgDyJR-dq8Wf9hqbV_AeyDjf1_e_XHhsM5a7MMv1a0o_acw6Nx2oom_6aQdMKv1XvQ-c5kPM3iNtb1WI5tXBK2x5ylrZhjLvjLSQjqIaBnCzu-xBdv6zhiIVwuQAtIA3F_6P4V_WHlQKnqfXZmzNvBrTxs3hQ9EmQoswKozP0PpsYxiCTysD4b7Y06J5nOqztQphWcyCzDzZnhHSsYHeuyMtPrc12POdMek1oNgVWYm5Gs9G-PSFy0yv1-WspiSltgeGt8bLKpfFZu_KY1oCzPo2b2k1jdrOeMnb9NlYirKqDwCNuH5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zzae0phdO5zdI-IMXUHLenCUKxDkwX-Km1kd8HgmDTgCJC7zm9Up7MDBfw9xfeb9I6dMy2juQutX8uYBcjZXIq8AY_GQHTJ2obXr6ikuCib2IO7eCeELaHQjCsN-2HVY4Dl2mbFEDwMxTt5dF0SMzxb3t5iTCIFWxOzd3MgeMctGS2C4EMQ8RLylEeoW7lZhC8Oubw5mJ-Ha5j5jLRcInh7dSnhFXUNQtvWG4fo_IWYzcDiF3gKOdVtmf9pFuizmbVYESqHE3PiEKgJnzapoctcR9olaGzbi3cEfTFeJuArj-NHW2nzxxX06-5tlwKMQuG99U83DVADxz1nJMqqd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGlRyqsksUN_H-Q7Jh-XSeuQMhmto_hRxnznIc36QlUQyqLu0d97QwQo8E2iFqEE3dr03fAXWJDcXPsdqShYtbW5JgU7cD8s6jiVMaysItGp1JIRmJN6QthrP_e-NE6jyRPl7o9c2uHbNFgV6WB9_Gg64NfQ2Nz9l6Zun11U9ah3pWUs8r1Amf7Oeta20KeHPPymNorO-cqVkmMHhd9pC5w1WT8hxr3dbrWopmIxTqH2E6rBU2PTkJ4taPf6q3g7Fs5g-bwam1qPvx5RfOJtuuPXpolmmOF9NRygvKvN30v4zsDdLNzPOLysKUlCZ2_ZCCMwAsoqBGXk2sgaO0hFuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_QJn6mAy_NcYfUooW3TpcuXWKGfpuobQaGwbqisYUDIcJPmVHSg6onZtL6oQLZt3FusttVc7NvTWV6-l1anr63pYuPP2vUw1R_jCu132LQFxCOl0EjCN0Fk31tTT0HV5sYVcHseEhkxFyQtTTSfz_HGFg61vIuucgJ4VqrX5g91q3NQxAzvg5mDSjeroCOPhTfnD_PAYX3vJYEjbSugdSAW1aonY1RLguBU2XNyXrtuGvsZKgAqFXmn9H3Kbry34PPeHBsXkyhkI1qa7ewEwDVY6Uf72wruYwpEbvB8qaceNDgat1ritRclBeOUm7xgzG5v7xGMgFCh9XLI_y_HXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSRaM-64oKzuQt0pm-fm48AF2EcudKH7jVddYeSYGALPnMc0uFcnjlgl-FBEh5HnldXwwtyzz2jYhV9pHQ1dGEmE-v6zsusi3pj0JBAQZl-90AS0HAf18OysngxgZ1E3fXrNHXX_D6YyJsvQLwZHwevI2WeLu__6UhijeMx0SSDLtkRvvge2BYXaWfIN-NK9EVMuVpCxyj4nWIIF7OBasTeocIAo8tWyc8Oh8cKh1JbFCEOA36lpyORsOW2AeGXrLhFwevWLlhr-eScj3jV2TsmfO3dTP7oaZCrIbNo5lJeb0qCKvoTYbwfZnWCsE-288xTUWhxDBdpSfPdQ7SQOKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-XmTCPhpaKgRkWEVrOTQADtH28NZUwouVvDutPEd5RqeKCAmHZwXRIzs29BMtRe6ZPiN7NZS7id8g7mrcrs9oJeTqFiCk8-9VX_QRTrovHd1KkEUvXD5Z2tI18m0Ll9lRvmHPA4wLx5OETWgGHklxxnMvMpb7t13BPEna1D08WWhycxr_7ppCQhfIu5-8FplhBl3BvfGZQDTItz_uNs9pNorWKWAJeFxr69O51eKUPUvjO_xTcIXq2VvgkcGzXIVM8Vm6n5gdSYYFsocZwCgrkPEb5R_SnX-QJMOMqIlYneoAftlKfdSH1c_jn6m7MuXWJqm3dNqePTjhdlOGrMJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiEJGZ1V-eqhGelNEd9s7beQ16scE03Ji6Y5fv-aV4ronm0jG0OnOX1Whn3Xk9yDRIKtUZ8x9iqhyV9GBjHeYQ04I8IFqcLX9HWYoLPIc2s8PQ54QIwkWmG3WyX9x6XANAbQxQ3LefqVE7IQXfHtoOjEAvaQIERWffqpeDh-1CGXQeKgd2Tb3bU8Vwzcgoif1b0MZYj2DB_2PlpKGgvPmY3ueWJ3pr7mnPOdfk31hHfPNkuvJfWsQFhDwBCdkuPOgaBqjTPTNXnvUiMitsc387rCG6zHJb4tHIgBy8qxSeFR4rNksU7VQc59VZ31WsR5goPERTnR27R644dTNDhxgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loijwg1BgCdf1bPctGTTeitFtY1WGRSlj9g103RsRj2ZgRr04Oc6bPLC4rWLvIwVFtJSJzYZ4i8WmaapM1BSxNR3cj1Bcv7obI1OeK0VNRNH3XfQHPTkbXdySQc9t7RsKv_8F_kdIN7MogNMfyXwARggGybipSIY6ATOs7cvLZNqsLd6SugqvC_KqXbYQlaaLj3hSkcqjLm4dUvwwb1PfjhqSHCRjDOglXG8l1SGjeNmbT-rls1zKN1APOExpI8Z5YsvgA7em6X9uJ1tTUZryE_imRUIt-1EvdjAGT7nUWffwuXAuwcMdXkPiv1paYrLbguo6Ntfjs-SSKGIoUO5aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-2x-NUVVm5AtE2kNxUQreBgvH7bTOZoy8tsPDmtcf8moDd31eSooTQwPYbivwmkjvSUlSdSmKjo1g0-d1qkrIWsSu-IZF5JlKFsPjpFkksZQhTZCs_ZN1NP2nbJ1Mjw2e4qeDFeJBQ9zdmQsvPTh3H4C4DHAxw0XRDNL-HYtUQcPQ6GOl8hdgXlkgpa-cyNVcnoXsvSdNoTwocsf5tF-fTLBw8aHvQ9a4iyUingGEAi4CpJDbH9ema84LhQ12SVSAADe7yZR9_28hocEbEnZsScP2evtHGskERMgg84NRvukcS-hPHzkk7ZTJKIqEzXaamrqa2x9AP3BRQumjkFYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9HAFoDroJnecOoLKoqwnj31WHks8hwweiRndFJrNTVVqnbqKs4jwGdThAK2I-5lrogYJsh5gpvJ5pwAkbPT_xPtNeADXXWPF1IUt6-VEOXQ0VBrgBqJsQubmdNiuttq7P-rfr4OkSivp5HwRd4Nv0Nvl38Ni04_-UQHWdw8DEHNiqAu83ECTUz0EbQ6X0U07n6Qnfk2k4v_99lvq1CPZg9ps0LXBEwIzwsBhh9lwzVcNiX7NM_eNIzuG7Ig_5Zxr5DLW5oCm1N7Kg603x1LTU6LtVKsLavU_2EA8EGDj28H-oKqhzfjnx2ajjs9GM1AHah7YgPxzRi4SEtkhbHW4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLLAM-n0x1TxJXH2argAlt6shEuWDxhJtibfXn7eNvPFvxGV4BPzMv8kf20lvn7F8nV7--x9KcSKs9wpUk6_G2UkJ-5qd5GO_E82MsvG6kmmzOKtTQd2zXO8ZA2p8BEFMV2CXmOJ77ubjgbTyHb-k1jLcbMe7nHjZP3VYTFRUN6YhFUd0YYXEyurCqbKJ-rXLgEgQUYekGKEG5SakybYXMvtmqj9r64V4FNNwlahqI-2XNQ6zBYLe72vsDFbKDTIE7pgZ1PesDrm3q4nAJOMsC_pG5jqfx7Vyzi9vvsIvg9FczM3B4vdF8QJRDS0RRpRbVrOrXBIh4GA5YhiKvFyIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKeSmQOe27Fgd1Oqs0EBIMcxph3j2Pi-UAq5Pq9YwPksziN_u6S6I-lBGzhPfKgw3sivVVq17V1h5tU3ZYvJTKGrMKG0ugB2x0t9AjH_3KJ-_dhY1IyHkDPXjMi31spu6VOPT09fYKqkXkb4GBMDOFjnfTuyyE_ocNI2E72IAHb-_qF9H7N0DPxs4CHKzUabaOXcuYGXOxGVPnOS8Fu0_0oepnlbRAkmhJwzGto74R9OpjOCU91ClicldU03wwaN5pqKrsHvWSvK7uIG_wIQ3_64qGNPy9MeA-_FepwhCx_upi3-5ibej5trxIwN3yZNJksGR6cwEJrERsSzUAn4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUu-iRt-96SD67ymEjzE1lsj3g94-OHryjcB263pRkib6c5oPrm3k983uE5_kGJ3jsTQCYNCmlXlBIYNSVfYmkBDpSer8GFSUnnPPDjW2wECcq1jqIiliKbbfCLgdrcxRCYl7IpAESOSHuAgDfeLgobprth82AQlXCi_tkZBPNsfUGYENTqrU6ZxpUCuPb5XL-7tfY7BWKYNX3w7ANzDziO1oho-NitqNHx0BFSjSIZXyma7XkOw5blkQYqSqUOWuUm5PuQsh0FsepmsRb0NV6Nt7CMRgCtaf1dezCdSl70fhEIiQ8W-PyFIqJg0EAOQXBbKovJDGcAxiW_eJ2eTZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yhx57xMj5OmOjqlmAWuHLoUMSlba755jWrQISTTmyeSfjtqQVm-_Xigej603doimPUQAXg1XbAWGWNh6gJPU0zkVvHFo9cb52E75AJeHcVvV1wLuEsfKOop7dzVtqYAeQX5mLyGKrPpGPSGzrlUGbFZzpO7yYFU3hQwxMo5r09cP3xpHlVYki8afIKtO9bQyEV68fw-E_1w0vHgvI9dpxP02SrITlZRRK3rultqO9jMwGEzmoBXbRYulykhadSYanUHam0GVyMe5CsdjqjZv1Y8Qi4ZNSwUA2zRNNzrnUNVNeOMTwYJzEfTslAXb343WQ9ZTUEsxIlbcMDjRvkUsCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Db9dYVs8Pm2u_o6ntWIfnkgpAcRBV-gJpfBQxAEfz9Gq_-F_6Y59elGstxyg8M8Sz9hRY6Dlt7VqROEraXYH2aaY9bHn1U4cFyOOUc1asVqz_zTOWCLwsQWYmEGZvqqTsR637Wseg28lpoMljpAIBiDrx5MJxFvKKcREznOfG1qkIXp2V4KOSRhdr2Kp51C_Yf54jYgPtR6j8ndecIlXuOa4Euroc_ibTWC0IS6suQM9ypjOKZRT91bwstfcMAeAU9gPkyX4NCt7r1mYQ4qjnZxrJcdhr3t0xWiXGiof0oh6eabQmkHDkqYIDZe99Cl1pXE3QZFTJKbLsN26ouPe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/searjOWV5akJ_-YUjG4Rqd9fR7zzH1za8R4RxDJlaaD_5Ra4b2CR1bfbYkaDfutsuPrCgKAXQoROO8gpGT4R72ityV7YPQHeKvzj5_GuhZRTCmKtXVGT3Enmb0vl_JHlGREcGwEimcDQPsXke_fi7_wbSQ_ZChSddTtJudOlfe5n29YMkeMdgAC8aL5_JaoWA3ZRzG47cUc8ssXfFrdlzJTD1am_X4QW-G3d3wWVOIspBDl0HVX5snc4o-qxWc5HTKBIKAMQl7cvjoTsCAFVlv6gQfHhsfrEiv91hF1UeoJkATPQ4RbsboNHynfqw8aimNx-pwXUG4W8ZM4VpCbnsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNdEvh6jZNLCcCdiImEUypwAPDDKa7_VuyGyJ6SBUw1PYbXUPEwFWUq3cXHvZ2ktrOt6rakTFnkxKu-63eqWa16ZntQ5FNRQagip3osnXdl27scwtvDaXBQCLtJjZZHLOJMWUCWnMUYRLKb15yVcJyR8i6bgMdgmWan2XeEXfCM4ORDrsvKVn_lDwDY2tK58ZtaXWybpIvVo7KoSKwmVqg-Pv44A5AVqlZItg---pC_EnLa3JrH9p1U_3i_Ni4_Ck5YdPyBtt4bErmIbbnvNdxItqmIbuL1-6m37KHx88P-gOAsXmKVIftm5q6cZBoryE_Z-I7i1xslvydyTUft80w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8xpF15BD0lwwsB8M0PT8Y2k2uLeayqo_HdOacbhSJnZtDYvm4eNngvUbCy74ghrMyS5noYHUqICDKnt6Pz_90PDO6ww8r2tjRLf0Evc_FYcw5XtURgipr2WhxcYZpNcmIh8FArDRpg_X_SDJ8qpu-20g39ZIYfg-AcM7xHRuVmj6Aw8Q4wrLebHFBQOHTeKGurpxcliXE0jgdbzKY6VlwCPQuY7y9JbfG4CXuV11vZ0qjAOVQcoR_FmIwhFjPdcb2RYfYrkC49wjH4zmm7x_wvpVTzXZBAKEIPa8RG6zRRUm0rfRD_IoQZP5EKXlXjyL9pHAvTJOWx3WSExTPa1Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swe0AaTvVcEZDzrUav90UYt_49-Dpb0tOPUve-XdESTttHqhwsEmBzg5k-3ttxcrk-H-2LsRWKrHv-8wplahXzoE0x0-20CvLzAsl7RWppntIuT8ekcez23nfqmlswx259irROTh8E_0bND-VNhAnYdpFn4SwbUXhJk33w64PYEks4LMZ4dXz_84YNho_7QTbLyfXI5aAFyhlVuE_ldG9VFwzjq8Oteb5jlgLNRwcW9lWa21Q7TFR6qvT6bfPDaL1DcfZEcscLUwYMRUuPRZnA6ehwKwsoVh41L8v_lB9bPAl-KvnLque1QxWsagJJrC5Wyq8BHGU77T4345p3PhhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKh-EzVkMqR3hZia0KextJ9j-plRE0wsYtUTshd2dotbIhX-oSu64jeT7zx7Z_k8i4vBzsW7WdX2sKjbEw7cM_4fSs_p7bHW-kJbt2oxR-3Lc0tilhpyCV84vtQxd8ipuVj1agX6Fs9SQYavgQkdWAIhko6Ps8Wf7Ne9RZTBtxJ3QOv-8byDK1zBcnY59aw6SU2SnLnk40_lWjJqI7ipFPV-pEtdlVYGYOmbF6-2HRkwKvTDfOYyXXzOKn9BuuBCQanqRhOQfbfg6m6saYkg95aYKZ25lpM9WWoFsNNDUD4vBr7kB3UKtlmBA2yWPUNcu3nLHTdrVbSbEdFntU7PiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLhObgHD42cbXJ07GpkzkqkD6jVyT0He-t0hmykQv6_WRGjGsbt7eEnXr3K8m5123Iqw09FHzKu7f5XczClUryyQNdeD4QNbbwX01wtQupV9PEjCW2hYKxiJKJNhg_O0krIt3oRZ9nO0V0-kokofh0B1ml9-3cWENEAUWTEDi-sqGbG4l9Ak5ub7swrVUix5Z8a0KI_G8NVxiqWcHBLdBIM8PcOgwQF-5vf4wgCyR9uRzRgqmg_oYJTFqtpm3PNVP4bFScyd0sduQNVskJb26LSVpQ-i6cEB9NjYFyoFz0e0cIG0anKvSKK8y1JCNfGHlj3P82HpW6LO3ZZ3jer4Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhFiFtln9U6bQyVaROEBoqLw8gi1pgPA7nkD10ujzawyz6ambtT1tTy-6BM0HV9vcB-ZfNmgLMqM0GUUTncv--sq5hCqFLv9h-bSMy31iizwAnWiuNTdRjUlv9GfDFXM1uGfWB4Xu8nBpLyGFBN-Oyemk8T_VOHDuZ10NAjuJ3XpMZwlwZwAc-otXaSS0pIYLoTjRkhMnUy2iUKCsZBELbfc7Z05JsJMuw-Uzd92cmN_hKnEeifNfoE9hHpU_TywYC4-GWEh_0ygowbKcT2Em6gntACtV8JNN5Kr2lHPDdSl8kGBmk9B41WdEbGvP2JnoAbjsncmlEBUHFBxLtLSgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYV-Y65xlcg28_l2CCHgS-fHDh-sgz7u24UsbqroUPjkikVd8OCwzk0FKOhgvSETpTdLXLJGKREjXx7IWAUi6bTdhTD2wwh4056J4Heie5BxWraNWq1kuixzXTUiVC1LwQMjFAn-OGZsy0RHIXvOl95G20_VN6W9dw5ylEuy8we58BAh8YPA64_pCA2kGSWyjtGnaH0XYdvVUAnxLP99CliDjUppGCx0cI4J_b3W0riJjNaXDNdgkKjCuuySStwK1CH6jV7UHw-ijCRvYNeabj9ncDgudymO_Dj36CnEJparpdGq28X9hRikcUCiUrWiEUdV-ECbCX2wFOOJv-tPyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AF1xyrOvBPHRINE0dJZkPwcWsRNfFbOdfyRGOD9Tl9zWb1Gs7GkQ5iBBOxlwFt6NKT1cClbr40_fuMh0H5bIADkQ1CfSuifADyXIQWMmzWOWGpR0Y84R5tMWTJTJSwcAn07J31zuADcMERcO4QmAIqQVya6FPoYxLupXUCP3j_QQfmikM5lK1buWnlM4zeC3J2c_y-_-bz3KxmxjTprjCRExKp207fnrHvXA4GtxQ2PWbtwx8DFFBySn5zC7X0xDXXwB5vNPx2QyCiklYrMfLqX4lplFtWp4AdtymK3rIZzv2c6aepdU_Hc9-PRFxWLdQMSLt4wQBlXc1GwfmRsleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPbbN35lMCsFBc8RBrZ2sY2D_5oxKxkElqNYlIsEiBubyc7oW4mUAVcoWVfJP7zdjAdDCgk0lvNaqYH5oW0jdP0rz6Q-vAKpSIv9I7gP02Qee0MfElMDxweIkSAjQz8y-lZ6PYCyxrVTtLHw4QOhPeggwgFk7Crw_pGrM6yDVrndzgqp638TOphpEha4KiQ_gpHi2mq-Q9GYeU4va5_lj3A7af4k2JrjdAUQ4H_WUPZmlYpMkCyKsSrUoZOtPkyZgX9M6C8RspiMRReWAf6tmkLfuewWKT8DF35WrYUtJVgpR6ZuORvqf6vSWj9467bxeCssMK6sAPXRDPwhrM68_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ1lgGL_nRIIlqLlmU7vAhxaHGGr1zlcPDoZkMHPzkGCokOaWZ_dwkg2aF0OsYWXXr_eYneVw_FR0X48agoL7KwIZ0FzvjQrHFCOw-TqgWGX1q__Szf_-_oG0WuNa_HEQZbJLWxja_4Mw7He4Cc_JU9m2iNlaWNEOflXYvcETaoDdxqVwAd3GQsH4DPfQaFteICJw9EUmg8Pvs0jJTpgle0jnKGoshO89Z4S9DrmcdzdsVT4ajbmWXdxAqRnd-FYVaL8fczMxj13KbywU_cHBzuV52BoPJzJpCA1YRxidH_w3nzVBBQ_dS--8AxjjP33nog-r-dW3hQZtJN1x7sybw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvEcqVMoRU3AtMLcU1DYNm-hBj2_Wg9F7JU5JJfYom6IuHMOnJCX-tcZr2qQP8S65hcp5cC-DqT9aDQBwqxIoqLJiKIfSoeleNReRLXvvKrF1eBbq7D9RsO8XK0Y78C9LxCVmOTV4a32qTV9iYIAywNEd9HNjcaLFNebflb8xu_jpNOvTd6ijaZGT4R2zgD_1WTRbv54hiLSKx9UNnG0DGAW1YsYW-ZpixALGefusKz9hdfoeXZZMLsSm6oAEbsCsnnxvazSPeFVCK21cJbPWs88Rad-Yguxv4clqKupl2ZGP_8BQH7SkZmnjd4a2Jt0RbqTZL-KSFpy6MdDZVN_vw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cA5SAZ--f3LPh6T-Ii8iIPHqq-rIzIf7UdsHKBxpbPAkkEImGcKMfMRrgDRu0gE_J7CFvMYKzw9rwq3vR8AJNc939jgSWTDYtJzfAF5nwkaDcpAJDXfmF_WHkydZH8NBz_G6yp5ELzwL07fk5vepoZFHaq3NgvIBuFdChp77X0-vq3vcpZ9dAKfV04H-g-EZpw2AVdOmCss884o20xhhG12eYcrS5GClp4SL1Q20eXl89TgJK0jr8Tm5o1vaMcyttbllZYQrpAkyLzNLeAR43-SbgRNeOhHcYqDgfBs750Z_Fj12yNhJWTJe6sQQeUqMiJIRLoaTnsOaHyuZdtft1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSlh5pA0U9yCqPhg56hcWJFkjfs8_vDiOnR-ZaFFG0cXTZ480ZxI_xDCEov4jnz2wkjO0TDfKpnGctnTMSUZEykIf_5Ze-Gxc3mkXmmxupOxkxUCyL2MJKc4ORRlLIVLFv6OoBMybLDPnun5B8ExYK3_ro12YI4xeEKLcAZw5p_Ru2JdyKwLSKoqqc_FpmRGEIWwzhsKXKC5bi8loNfZgjDMuX8rUp-xynZH0CjFLfXZeE3NrbwICn7dkvitq8zJF5B9XUv2gwP1vW7yYHlxZW8S-vDmfq8eyksfz9GwsDgjglvgYHsnY0fk7kRUrkA8cFQDvmcLXnDJ4nCGBvjEuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtqNntqWDJoJLBFkqWS2JU4WamSEP2F--uqpA0HJhBTOcMXObA1M8tha3uHN6oz1DAVX5QK1FEdVRmY_owaTm9j8Ddjfpkm8HYM0ivv5wM4DL7wla55zH8ziyX6TqxCwATitaEBLPcitgn6FDjfqtTJspdXBcByFib6l4_JIRKwj_0o9h0jg78NFgp9q52qaBfyciqxjicABAJpbZjouI65YdC1XKQGHFa2ubmhlC1aXbpM6HWiYIQJ2tIcuBXn-wVx9oNfzRAL0o2v8Pr22T8mpV4RMXEhtwOHchclxcL0v3MURTlIZQeY-LdlDPZ3HwGpDWD_prqK239iF5D1DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYFErVFv9EhUS0uOJ1pDzCbfe3RezuNfX-WpTYa252fV7SU26G29My4S_ToHkCJhA5iB03ZOb3VjPIP5eN9oPy8EuamMlm2tUa5ZfpGbXzQ7MXBS-Psq_pwt_tZSUJdbAFnUJpuy4m6JRhB_0km_qxYF6nKmibdVImFBbGag2_RXb_WI1MnKlVg21HprwyenuquKxRJeeSb3j3gFfpPfMG7CYtDKPRU5BKAzeIONTwUpGP2_HPS3oLi-wqpmQ-05Ggg2vXCUVAc_BwI7OTKgJXLNyX3FNn8zj1L9G0ZbrGRKZ2Ze-GFfZ06Q3g4x56lQQFdIbUp0-gH15ARvZgItSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3OyfHuW-nOJ0gGvwMkMdl9QmWGRAStACOZZKfbis0O5v_iVpHUEiJmArFkWccUDgA_-Qizdy3L0KJ3NXuDiWwJGgA28UySv8S1LpZUBwUjHPzeitCSa9L6VqpV4_7JSYHqKRAyQVOdZcIxulUrjxpMD_ZCnZ8jQfHpnNH-UgyClCjw9NoRJWmr966hnyLihyZXKb3byBKmmVtYZWFCeaNOOiVrSaney8-2gkvUFz_r74uz_EIFO99AUa0XfmiMvYlU3fW8ivcamJNi-dwGCfTpcXLcHbLF3bE5cs8JXwVgJwqsqGCEWS3tWNPhOH3gDNPWXLJuGply8cWuD4Z6MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArxFW8l9z_EGScdKKQvM4ubIsyOgoe5V82_ijrkfNt5qCFFlQH6vQ-D3GTv-ShWOeB7zkyROnMShn1GPLOaYz8QUm_LqfMsfXJiJ7BxVKTIkg4wFCS8KUkZYsyt8-nik1dba7exkcsm2PXwDsvvbiYcyyJlFx8zgViRyr5FD3ihk2chQ18dDIXNqS_CsGwM5CIFCj9oMn0DXWhkmLC7LIPR71C86JHgTUWynuBtg3-hLbMcdcDZ6bhNmrArgHVW0Hqk8La88kd0jE9NVh7J3LRY5kRIhB4o-joVMeZqbhQwVjyCNwi4RiPCgBONDs73rvTzqyglADqFCrB9UZA8QoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiURNvRcy0UyeUjYHWKX74ODoXQelSsNR7JjhWfwMABSL7sn5q18Dq31mimUPsBmR6PQ8UpSROA3oq2vOum5UdVxkAKhyUQk2Y5Bed6V8v0qK8qOqSEV-uOnbfJMyCnR52x2jUaeWhHk0VynAubiynDIgJkGBWFTC5MQUtXAhOANI2XZy1cv8RJuK4bBXYRTC4d926E2sI4cUuwDFBZoW7SvhfTWA226UNorJwludAhBi6_I4TG3Ae2rs2-0PaJ25UZkygZeOkjTFIc8WF-53l2zyWHnovs_H3tCuSe5AmqtlpTdZlFJ1ZF1ko4-2M2MisuQMyagHM3OzMsTNPI6pQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQzOJzpKCzZ_slwkl5kHJzsWWMOzOJhMIadtlLBqGQvBajRd4OJyGJOAMaFMxRWgarAR1Eg1CFLCBSaBcd44hBAavPj8jywPojKdn6ZaZrTqS1wmG7qs7c-cFHLjttb9vdWVfDrMWV7bYz_mUJVeBKGtmlEzDLLsItkauqLeJej-IlTEUjUxEjdhNzUN3Tfg4lt4KqwrtP_9EjMyaF41ncmpfqjY2Uz0PXXUQRn2oAivxnqbvr-LVPksAoGKhFhZLwtXEHss4j2E4DK-rePVAwkiqpIsAc_pHFSjIMqKdohcXNezb6NTPt8SrJu-1jYgBweIRxJmugC-n9Tq7RQLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9ahVzXW6YwbUef36YAcnK7HEMTCTXP161yAnp895ky9qDcWykUjgvHB-B2GgFxZUDvOomjcipWY0PBUrieq5B3lvu5F9-YNqGk37q2NSAvXVA_Q7GAc0YlEyMB_WN2yVnSIDGyoiO1607jCAnsD5PDhLyIzjXh9i87ttMF1WMsHvyMEHSPbVCAuUgwbV6ySI2WTrASubyvyzC9tKQ6G0-zWlLYcaP0xGe4ZveU-XSzgvpV57FnT3RiYaecyAaYfzQHBpvKDORltv0wt7BawmH4U_C6SbVo_qW-DOvT0Z05KszHgrKNyIzwCBv62UFuwXhot0URUyHH5qmy5E7ElNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cItxfeeB_LHLxccQSTVj1dZLLaqDICJ3UhrAR53PZMKovCQ-FOaNWOpPBRS9tOX9eUJzO6-tv1hjwpvOt_jnn-PG92GC19BR4iHarmuFO6fRO4O_mjPoPmSQmCK9PulPCE7pPmafBRiA0raLZvV8OdJS2BsdomLKcwekyPbaNm_ubc2rX-bYXK0il-kgdYyQNJuNawC5kmKQQeCy2LCIlcIPB89LXPj0Dv_iboff9C4mAowDHuYrpLCvYF6z3cgM3BsYo6D1iPDB_S9yjMno9NI6U1QAmHSa4kUTmaLTLiP1cAL1oKhZ7OYX4VhBFoOpmdhW4OC6lnyhNTxS1wF-Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVk6QMqFLd2pVyPJ_QKIyqXuXgxgvRX_zGfW7SZLjnmnYhNeye2j_ag0-OgaYUxAR88hQEYCAv9D886knIu4DYj4lMINVNZSdbOC8Wo2wVWAukQScZNrU-ZIY8Baygq6LoEfnt7ZLbGWtBOp-aZw1TlYvXwXRu65FFxLULRE88pFv65dwhwUqrIDlzTslYYthQYClsVsIAoq5G-iuA-_Ce7OPmMLQ8Ya0eJwXalOhpnrttrrMjoN-OOreNqi6lvip7kLGVsX3lmedZXme3QbsTRgMTwngbwX772P0HSt7sUgPDAmNaxUluOW0xBQJwTFuwSkX0u3dHLfLn4uivNhaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls8GXqw8FV8sUwsRhtwf2B98TV-TI0RxXGkNzJ-3YBWuw_P48Uy-6F3oQQX6iom2fTs84L7JLXWaTbPhwHx0BAxFbXgs6lazxDU4UeMEla6uHvD77dC9V9Aejy_eZjbcdglZC4xhc4eA6wzc4X7oUjCUNnJns207y6st55B-5rhOVrByF2GUWU6eKk_F5iSze5-tzgwOGpnFapXoa1gaOFw-iGJlcBxV5rrP2UaDs3Ap7HPO_8Q0IXCJLDXlS5Xojl7_ENby45AJW146Gwg419Wp3hs7FmSYyulHVv9yS9Jxk7OuThgqmFWbjPWYKvdQ3ddQXOfr9UqKUHMp_Qno0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1owsgAB94HpOoNq6KIXon9CSw_uGtJdFff7cCKW6FHZ8UFcoYDczSNTZ1N1I4j9PEWKM0-WdcNTVXN5oFlmecf3Okq3-M6SOCiFcWhRFgDsblgyuJMU7qICXYYyFQfFQaW2EQ-UkClOxxoKcvDamTYUOaOCxPG7u0aiAgy9CPnYV8SvlMGeQiX1zu_wK0FeSd4das9Lo4s5d62sMaMP7Jh8Un1K5ItUTUIe-3tSnn3FMh35xE9UiortztOYxX64ApzmrIW-KijIpkX5x1B66GHmkuuINrj6aFCeZ7La4I9vzUaKjIiNcFyCVxZje5FRYRG_ZmhjlpcZq9oNXbxwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmrGwj0SkF_-XIWfALswUud8GgdiH-iAzn2F5SbgIXJE2zcse-sVscjry7vnjvy4OXgXVJQimOdU7JU3I7MGe3tMj9N-Srk3_pV-bCAdbGcdODvBTdamZbCLsWjvMl1y8_lb4jyB1_Dbxx80cjZTHCkvZoVyW9Dr5VnCPXxzdCbzr1IGlBOBgJ8cwI0VBI3S066-_Akk-tJWbcbl-wzc5zG6qTStOt1NTT0KObtA8z-vbP1a6AKxa6a4kyn0tmbj3fHrztPA4dC9yiXXj2xidkF9fsMrtOxX98x9XhChfXheIImG_E6-uubt7q0Ha5eScvV9cjJ8r20kO2m-Z6gx6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsd948geXOsSqk3vyTA0uugczf9RedbSAZufM4cC33I7dj0Huu2ZrZN_c-NSSA71DSQxyPqqpjtNJXDRTYnUZEJsQvu10Q-hKeTk2vBng8p-d6DihU2z5FMhY53Qzfo16LhEJn2C97VijydQBgzyDKnO1A28bRxlC1rOO_xKA36BdQ1h2sd1xIomG6Hqtrblh8cquzcdtopHN-gf-HE-NSpmBObGD78HtoY3pcNrC5sP0EGCpUX1HHMXWrauKvn9BxFOoXTXP9uYV0PJ72_I90Oge4Bkr222G1Kq2gExb_jH2xPH9OBjomKk_l6uuKU9q-BHbpK6U2YB4lMM6Jl43Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQwuC7-vkD87uYj9xlyEuK0CXclZ_X5VmkwSv_Sho3yUJbscevc5G64Rf05kUEfJqtJv_F9foFigSYjnLgU8K0tORmAJUQAE98nQljuQbBE9px_WeJW2hvqQF32B41445rO_UyPu7unKyhp2DR1H6pqiITZsThKemsIgENaR6jtRbUFTmYKh0n_RANqPToqCrItmg_8QjJcGGVTXXuEoUH0uxmUNuyXzW3Y8uyAPtEsGdb_GG0hA9jVfCj8-ujAAHI4KrccK89mEINGekt3V3JW2sqUHem1DoZh0u-L9p0Q3pxLgSZJe0GslSVKMXqEVUargtbE6GVWwlJCLE8-SrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFWKI5Q26JCClf-fk_ahd0uBRYsYwM4GJIyGxJNuyG_1xXFFHRJEMOqMUI0m8HFNVJ1PjyfTUSD7psh6iHHlgo7cbCkpMEbGaAReceDNi7fuXNK5ox2WB8QkGEe7Z9c7nkH0j6Do3ZXtJJH4R283b0x_tTTdE50hZe79MVIidqCDbey1No8HKc6v9L43xE-tFb16ezyMku5GNT37WmzbFrkPGF1SZzTIZsBCSmfnteCI6i4rrn7QEehUZGFFCbFcXd0l-7lKcAkfFVZlcbUhxaGbPWF7gOO2gs4VKZyOHbzsm_yqwBopok66uk3LtZ22gwRUK4oJJmmyDZzFvNlnBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOH5qTO9-lGRpa3txnphJMA_v4t_wasbyYo3xRpTP0jklrKWGDVKePYMHA5wq1UXOOJanNFPIap-IEyopkoeiXg-wIE4pEAm9t9F0NWiOd_LXzPPefaeHZKUts__pvmsp5XBRketsONTmoarCScYRGZ938jH54dxTQ5l2-xlABqa-33JMMzOkfc3-VOVReSx4BNXFvKEgB-nlVtP3Kmw5OIHXWtfzmqTDjzb-NUXZEAaBSIIl2cT4NmW7m8x0XgsjA2ZPfaO_a1O3ZVrvwHPZAzipPoikMn5M0KRDUZZAIJMhyaKEz5LGM8lVp8O0Ur98D6Rvm-asjBAz_8a-7Tgxw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=XccOLKw0hhrYkMPZBERU4XJgg9R5ikAhJm4o9-qks2ZSfNDC-x5xACBQGNPuNTZruI6uDneNNgXkubKkr8DIgRr3Xc7yyhqS8z3Ae8T1DfJwmWXS-CKD8EsSTHqwDFTyCFxDz64QXyUgcJbdQCQnWNihUUlLnrJn6fuZfVhzlBQtLQadEzBF_aHysXJI9QM2R6QWLzkciceKiZjtY1LrAadFBn8iSdFQWLdfDvAI3-b4HVog9hhF2DpW1EJOMxK9P0_QBSTiSwIO0SroFSryop31ETRQlh-rAb7cF9DNwnG0Da5rsrdB0i2bvKNTMZzA7hhI4OuJqiHXC0ujKpUppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=XccOLKw0hhrYkMPZBERU4XJgg9R5ikAhJm4o9-qks2ZSfNDC-x5xACBQGNPuNTZruI6uDneNNgXkubKkr8DIgRr3Xc7yyhqS8z3Ae8T1DfJwmWXS-CKD8EsSTHqwDFTyCFxDz64QXyUgcJbdQCQnWNihUUlLnrJn6fuZfVhzlBQtLQadEzBF_aHysXJI9QM2R6QWLzkciceKiZjtY1LrAadFBn8iSdFQWLdfDvAI3-b4HVog9hhF2DpW1EJOMxK9P0_QBSTiSwIO0SroFSryop31ETRQlh-rAb7cF9DNwnG0Da5rsrdB0i2bvKNTMZzA7hhI4OuJqiHXC0ujKpUppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d85E4Q-PN4ldocYWYDSnVMYTkLQMKeQqGtNzuRX8BQS5qzN15_k-ogbFLxraE1RdwwB_xLH1YWVacZWu3bUaz2M163rtj2dkjgtnUUTAvhROcEkriFqearlbKXKkb_NqmkkCo-8tRxsuPxnZsYLFNdACD9rQsuezx151D8dTzTF3XVlk3l6Yat0OZgSSO9zM64UjLEzntTYssw66jdcTWQyk-fJf_NNqHB0thfQtUgj-AxhLg_pMZi1Q0-xqHjDIsoH25sDqlffZtQ92sr1fixK1auvVtUB6G6xbym25QFNT9TqxGcRGeqrHmzOtNmfk7-J8vIhD8HRjhD6Jc1d-Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_-x6AfAZTKEo34KyW3VkrR6ekvxnr1dyymQPNSrl1tizoCwVW59Kr_1E8tWjN6Q5M_cwMAL0yt8NOxnDcr0vNfPhSPo4acUabN3OxuEi2jEwpKn0fETPKJVzB6ShZxysuAI7yNlBPsi9s1Y38a_oPA1QWYvm55xxvqoD19E67DaWwMpQldqne5KSQ1Y1w6yijt1VwSgZllh5YcLNrr74m5QR7bERncnyHx1lBvntpKc2BTw0en1-RhY8dbVDv_0UgplmYt6NsN4WgWiS1H0tIQvsj7ULvVdD64nsA0Bg_961CQ6aLxzm6qJ3IJ6TjpxG5Gc49W2mTuqu8grNz95KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACduGeVh17E1UDbDVOnwZoUJDWP4NxzRP-jSvsYPChWxjCS9uy5PaYTuq0ushfvZCu96mGESICQCi9OiixJjU-DUbysFFtySrpxF2JbARsDIenC8EnAqrXZ7eMmxxVxhIJsCsy8JkCgl7rAnHUV3oKgJGUjBN76qhkOe0jVfu8Nv7WgR5bg8SRudDMAL_9HbC5rRxy98xV7m5InYkgCVQYwL7o_luBVuk-thZVo86wmny0mRsOIlEqmr55yCUbbS6GOOgUinuHluKch9WyGhQvXJ4IJiN-Qf7ogx8vpbkzrz1q6MjgJnthYLhx1RJ8TfkaqX68L6EFDVBrscTivAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FF9QWHt2sBnuEKzc3y-iegPGKu_Q0oV4xwPauVhEV2tEU1bPcAUPLUMxyNyZwjEaCFQSeeQQrDY3RyeAyI48kY0Yaq1mp2WbdPHobAshXAJA4tCMpGRbsVprStCnzgRhgjyA3PZZ586Ru9-bXwasZQEUIUTwNWzMJ9hJwMPoKHRw6c92fp8_nFPAgAPRJdWED1Cttt6j3XOWe9NU7QUc7L_UtWi163GxvnQTtChGo_AN-mS-YRWqgXXra46d5IBJdc3SnzW31BXs7zmXswfnP5oU_Tm3OvegVR-robY9dkQNQ7A-6SmwG2F5feqyw162FQ3ZbYlFEZmKMMc29An1Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNVaULAtApm3i45CFUpG81Q3fSBb2Z4amEdSJVQMwQ3DFZlXCYz5wCJ_cmQ_wNtchuUnQA-HtDEn4qLI7kOdptmOFkHuasBMsgjveCel1LgO1d-1mBjcGRHQdIjzRbir_F0kiwWS_hIoVAISGQgEOoSK9KYrJTQ_wR3zCFyd9Ls73T7zpelmqXYWZDnY8Wwfms2v05gM_CMntqyVBANb_6TH_pU8mb-m4xjP2CmWXJfg79viU5sBqlbry10rJ9N3xQG_WG9MYhGEsrMF11j6K91zNwuBAOh3LlowKcT8tL2q2MJYNncg0qWEXkAG7i4NGNLrV9ue-DIEDpQLHvpdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0wYk8TiBUcRA8sgyjP_kwBZgXmvDFnR2o-HZ0WbIykDAZFkYg1FP13C-PO5eL5stJGobNtVPbXLTRUAWZBPYejwpjo8LB0GBjiVG-DMQE2Cb5kS4Z2buLOP7TECNfrm8t8I0reMjyF4dUclEN6A2lsVCmw-w9fsNl8ZaaxcB1WL5fBFMcRPTU2wLrF52Ga9ooufvcJo49xk3v5wq53LuS2oA4GUqbuLT2k1CHIbGKJuutYW90mJog_rRfIN0lUhJi-I9qxGSw5JAho3G54FNxGaO4p0fCwzPln8a0XonR0-i_AdigTqRPZKjlSZEBEPElDXa15ghhus181-DVwuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrZEQcSd6L4CDOclbEd2eKjDzORzzgVuOdKfWFXsjKgTUmAm9Ddnk4_HOszyE1AV6dsMIfBd7s8AQECeMoFOcXOs5y6CPLg5r_dC49itNVaMf-DwNKIq4vtnTqB8KmYQzX3PZM7lHpqGDS72F6maHi-2j03zerqvWwSQ2VMu5wc7-4QjP8VS7fez1m4MqHWuOxl_0CikN4_jEW9aw0dNQQsWR6Prt6Ot_c9fRHt0MCgpmABMWwoBGduy8MKRBQJ0RG11MVFFsDoVUFTHnlM1RSoyin0tHCzu1hSmdccx0dMqjmFGnIydRBQe-YxSezmIUKNDAXae4WLKGdaorc7_Jg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=DNja6xbPvein0IBseyHNopP8g38Y4fHU02okLXHk7CYk5NivSFQmwLAJYoWbyBWpdjkfhM7ANdGqKSV3xr8s3t8C3ID-FNGkV1hf7HSPSUOgz8ch8zrtNWNMDIi-ulFn_b-_W-ujm8mmNRzCYcw-aC7xf2Fi9q7tU_-CBIT-1IrNQdX9_uL4lovEm4eVLpeyM7Cgsgv379VuCTiu7enQDikITtkuW3iWoIlY5I-fmm_kWO9SFaKa4mWX96948ZiBGhxRdTNgAC8kup9DdohTmRijVYqzqyENr6F-ve3qRTgzJsZ48d47-AcU2LBpb0RC8jljxWPT4XkfQhMFBtOL0oEx3wF0mxXKOawA-yJuWbMGnX3PNXCtViEI4deLcl-xYEB-2kISwR0it0SgbBZnkHHv168BRviyPHxLhYApUTjiMRPMv_thTSzkjznyHLrR7avwGkKl80f-z0hjdXK1_JDtmvSug3g2H0eWbv2EqC0Qi1Z3MvysTD5r4FxIoshEWh6tqZvxyQOBBF9GfGXOJARTC3us0oEdWq0W5_ZwQgNfIjmv7ZR4lHlOaEuk3st4hoMBVUXANw3_Htpo2ZClbkYzCaC_3tX7D6KzMnnc39OpzNNpjegAAj_kgd_ZgPsETPVj7KfgnutfGV-RhNEn_Qn4YXom8nC3Tw7XMPQliY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=DNja6xbPvein0IBseyHNopP8g38Y4fHU02okLXHk7CYk5NivSFQmwLAJYoWbyBWpdjkfhM7ANdGqKSV3xr8s3t8C3ID-FNGkV1hf7HSPSUOgz8ch8zrtNWNMDIi-ulFn_b-_W-ujm8mmNRzCYcw-aC7xf2Fi9q7tU_-CBIT-1IrNQdX9_uL4lovEm4eVLpeyM7Cgsgv379VuCTiu7enQDikITtkuW3iWoIlY5I-fmm_kWO9SFaKa4mWX96948ZiBGhxRdTNgAC8kup9DdohTmRijVYqzqyENr6F-ve3qRTgzJsZ48d47-AcU2LBpb0RC8jljxWPT4XkfQhMFBtOL0oEx3wF0mxXKOawA-yJuWbMGnX3PNXCtViEI4deLcl-xYEB-2kISwR0it0SgbBZnkHHv168BRviyPHxLhYApUTjiMRPMv_thTSzkjznyHLrR7avwGkKl80f-z0hjdXK1_JDtmvSug3g2H0eWbv2EqC0Qi1Z3MvysTD5r4FxIoshEWh6tqZvxyQOBBF9GfGXOJARTC3us0oEdWq0W5_ZwQgNfIjmv7ZR4lHlOaEuk3st4hoMBVUXANw3_Htpo2ZClbkYzCaC_3tX7D6KzMnnc39OpzNNpjegAAj_kgd_ZgPsETPVj7KfgnutfGV-RhNEn_Qn4YXom8nC3Tw7XMPQliY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbnzYzzKWPILAiRk3MmFzUewNdTBuV2SveCzXv8gwGwmnFnYXKOZZnmZEqzC2QKEVG3grnc0_T48WBPBbmx_Royfxcw_NbrCeu_yPcKIx2VVJ62_rhijb1ryBx1Uk-KvI6NLJLRPPhka7kxYR3PL50w_RqLvtNgU-vKkOQQD05SwHW2y6n8qC2vRqj18Bfe3_2STIitNDx-I0FjepPYMtARdVoP5j6-1sbfdOcfRahujrIJyJ6H8dCuZ8AGaqDz1x-bH8ar6tvtsx-oZPrsimWHKu-IBaVuNBnT1hhO1ZAXy8InSOQo6lDNziid7E2zFy6QssT0fvX13QaRpe10Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lD21kBLNJnAeLjFAwYtnKVWzTJHzQLxL2h1CwLKZddP2fIrCJjqQDBV_EiTM8eTCgb5w4swJ1FFc93LPOIStOEXkSA0VnVl2hCbqxmJ4kk-8qNfhvyJVEKqSAfBlkdVU03GjvScKI3FqhS0FNfAqLCnlHGmzha_6xpJ1ThglEUbw6wK0QMkXRmRV4qOSYQDckuS4WZkiNwtu-koSsQbd58gsdfNtvnIAR-n4jUmrhchcPnNHN6FolkIOSCGA0VcCTKKkxAoAq_1G3m1RojME3gEpsLdB5jFtsDXAAzN7H5NsgUX-iN_H48GC2AdR6PZq9XutibzdVm6iFwzEihq2Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/via6lRkpaAJXL24UxeS3bFozgiPDCVZYKCzhozPqoB-fpRYZJQUSDnqlBEcpxNCIQ78SdR0G6TBGBR_xVV-NFr7h2alOevpk5rkV9q7Qhr_1aJIXfxP9GeQMJ_EvuL8W-gBAeBqfG_MLELoEZvNvB7f31uniIgdGAl2AJ9HkIGwFswDPBRAokvpzoZT_cjnbFfsa2UeDpCAzuVZJsPu-j7g3-S6DWfBGHwPEY_sVKIZNDnxo1ypyVh6m687D3k014gzddmIGST7IMmiy2oMqPsV6BWOP6lRgYmxKZS6sKoIxY3vGhND9Z9K2fHmdMyMJY0GpJ3TJam-XkvvqMRw3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmWrtz8yVvu7njRJByEk3lnoSTmJFny3dG7Wc9UcZIrwcxXZ1SRHTO6DbxVcN-mi07rkVSIqAlBtlkrg8M3GkQNXHkBRhXO_0Sa8wf02m0ENMT1Qtl7mpEI3HMLUtQdnmu4nrQIFoazA-r6cMZ-FcftvL7Rus-Wy4rw888kk_4ZSvyGpS6qaTidoB-zKlXhA9nrwJnFKjz-XRLhwunpcr7Eu6eAqTtdVX31KYEJWywcg7wZJL5nDJyqkyTIHbjHliDczS2hlnoYdJGcofn5DnUGE8wDuFKeiSy-59hQyo1dZgGQqqHAzzsYS9Ov5ko4aI98Yy9XVL5OHc8FoWUH6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuQcZlTytAxSDBX2BR7xWaFRYrWB3hNQkzx0O2w6qW7QYdh4N8cCg1WCSbgc7BT0TlK67SfQG_niHVwimElTuqgV_vlumorszGzhPaSSv_AneJeQnoRfm8H1bAHbXKZyDo8g2ZPBKCwsEKDEF-Or7wd1Fi4aK-XYaXNjWnLJEVUIRFb004b6zdiJZ4kjrOAQb-zlriFKHiGCHwW21kiqQ5ckYn8LbEoAtlLFTlfSusoV6mOtgQXBVAPoO2CWADZXQ3NVbjA9NPqgrkIJ0-LMQWs7mf3JXphlO1zs8QMmPqOQNNnCBcF5mbh_YDwtwC8zyYp5ywwjWSq4OijM2yjtgA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YDJ37Y8wMQXbWSSMPcgDfRkxL2Sfr9npBpjELM5fbrthyTMz4SfP4eNqJwIADOxoUG-I4_6HV9OWhhKshsSE41Fb_lY8BGswREELHrX8SsJre8pMLd1cM9NJbN4wFXavDxMxs7WfVQRm2o2CkAWR2b2PuHDU9-sbLKVFgd0jg856dXZUuvpq67lj3rUVTnhBgfyhwSq6tQm2sbfewv7deEIYSW5J4Vm0hmtJuDVZ-UlwSki_JiwXSLbxWk9GHTOVRlQ2l8g_T2OIcADm0njPQLbpYbZrbQmldLUo_7eMH45VR0Q5H5ny8FtKs5wNLn4j8QXO3R4NMqaWyAUpZ0Isu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YDJ37Y8wMQXbWSSMPcgDfRkxL2Sfr9npBpjELM5fbrthyTMz4SfP4eNqJwIADOxoUG-I4_6HV9OWhhKshsSE41Fb_lY8BGswREELHrX8SsJre8pMLd1cM9NJbN4wFXavDxMxs7WfVQRm2o2CkAWR2b2PuHDU9-sbLKVFgd0jg856dXZUuvpq67lj3rUVTnhBgfyhwSq6tQm2sbfewv7deEIYSW5J4Vm0hmtJuDVZ-UlwSki_JiwXSLbxWk9GHTOVRlQ2l8g_T2OIcADm0njPQLbpYbZrbQmldLUo_7eMH45VR0Q5H5ny8FtKs5wNLn4j8QXO3R4NMqaWyAUpZ0Isu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGmzRTQWJuqiDYXZuUYJuoDzhkpTe_s02o3VrxSWvpYuY84dCJjUWVdFmu3lCJzDxVynHGfE-i4ZsL4fpGjTxQNuE3guYd1C5NMyNoIGFg99DXkqbjiHzAabIa147qFimBJms8TluhN4oaNCBsODRDqk4cr9awI87qT0D9QQz-yOlGBRY-t1aa0LrzggXRS3Akof8WM6w7bLZmbGVOxdYB43U0TscdbQo8l4-zEKMIx7Z9Q8ko3TQvrjiRc8btd9qzLVgTtMsEu4W9AfaXuUbj1SQKV1_tDsvfoTTxSZ3wMbbX5QMtyA5E6d8DcqxLmbcYOXKELJsnuqZTorIGzVYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_ay3LHYSJoysM8C4Pd-MDYC-pmNkVACzH3M0FfoOFFrh0AIyRfLJ9F-DSZ0i59nU4NNX70oW3kITB7EVSghNVW2iEMXDYIuvOph_m9XF9U_nnQiUw04Ur-BuEtyCBcefKUZZPYbPBe1hn2aIjcpYgJD5UwPCsBgQoV0PG0s8QYWBl4nLhNyolBwzCG7U7RhgzFIjUtJEK5XzuEkMRvfJcbBUY-pnNL1rCQhN1QBKP9YTmdFHFhabczhX_PrtTx0QrHMKVbxv9rvM2zawVP3t1Ivfv5rlaQXM5eWAJdvHbhriGk6RihdP3kIKsmdIeTo4E4YBnICRwykvZYAfxiI_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad3CrdbeB0jJGpooZWXWHSXUPDP6nx1dlGha4F3Z3ZQyOyY2STjTF0X9epR2KnrM41D-lQSQmaEdIp9ihGegJjNUzWuxwp7ZKTQCFMLGSL-N4WXFsHbf27g-m5gUSB9U6m0oEfJwjq2Dnq4Mf9WKC5Z_5R65mUTBTIHOkHUUn9NdpeMsllQ-nqWSxq-GtfFPFEbjcP7bx-aucBNvf2_x-xUVVL2LPSgYpf4VBcft8DHAoN8smvM33jDRS8v4yit7duMORVZ1dnOd-AVmM0aQImzDtWic2bE7LLzs7na4pmm124scbYVYxoPmcxnXEcMrbadWc_XC2se08fErPnoILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU2eDRGOeqbrjIgO2_hqoDXDI8G_KHHFcZVsp__2jLHQJbQ7y0Nuep0B4qQZmmDY6J5WtZPaKmnyxQWXoK12QK_RG9lC8071dwB3Xh7aw4yJyY4di9DFu60lLw2Vcvpcqq7pd_gE-56GZgOC2MOqzyTueN91OVWqeovPnmoMDhrw_FWA1bfwvXRYIPppbrqjoO9MIbZ0PEAXwm05fu_lSSXBJqUwJqzTEO5OeBT8RF5gsUDO6gSo0S2KPqtBswfr81vRxUo6yht8DWZkY10jFsis9Z3AlZxbXAXADPLzsiDiJH7EPs2GSdcaZRjOnT1kxWSyoyNpkU85KREQ_vYZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhHJ9L6Tu51KvEMnVE4DMR6WKdp0yvntjYAoPYdDXiuzYJ5zXcDiRaGD_hfs-Rf19sdBJLxs9sXQ_qUHDiMJXyO_-kiiLdgpku3PLHD2GJv6klrghyK5EJCEQEENjfFLGif1mHyUqGTrq1TtHumV0FaVPGOLjsPzFsOpN4PzeB9CIdl96sYmh9NwieoSqHHBIdChrzWY6Meh7IjKtCZHSK2Um0qTCHDewQQMjUHKW0SUbd4CtQZi97sQPyaod0Oi_chaVOhs6iDTu3rYwN9C9ZtIUFJ_QTwEHwhr4feVlK27nt1dZiFKkRUfIq-4kuR12vazV1LKkwPeHz7KQ2gxCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGXPU7eZUkJjNh4eMcFvDh-BTSCWDyDEA_6O9fxtQ0uZll-g7bLFol-ybUJZZWFANpSoBAKRPrW0nKDspnl5cq5vk-VgI5mjDN8u4avOSk2c9Ftl3mtwTiaKShsPJgHTpPPxUMU_vfeU1qm1dR7X_l0a5WAnVegu9JnzgJ0yBT0iJxCuyD8bmzejRGTDiq54Hf5ePOsVzfGeGiQd1-VTuachBieTv9z8Ro13u1JJnQb5jkvZwnzLyPLY7rap6-LV57FQMawOfnB724OVEu1_kzQoOWZDBMd7iVpg4mIXUTKYJa6W2RrxyUjwrtdUW2qxWk71B0B0ytg8r8nPbNbSVQ.jpg" alt="photo" loading="lazy"/></div>
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
