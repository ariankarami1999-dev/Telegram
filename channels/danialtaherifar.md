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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 271 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6GdNtvdOFxufkOUaQkE6b7irUymEF_6TKUlmCKtRFL37IpKLTg58dIHR-NNZ9FTwJ5tbWM3tsOb52_08le4ybtM_rH03tSWWLZkpeHGyPx2IoALohJPN5udynoAHI5NV9fj5ztK7B8gdmVqrXwHYmoJlYVUmWdQbcsJZ9LCe8O3262wYR05kvaX2eYDUMDb1_TTz8xLFuK9P4Pi3ofMSPUbdYBTjjk2cCj-v5Bxzr6hsoaoR23oxnKR7PYqbGJXanrtDwjNmrzPFf0cWcGh8hPS55gmBJTPDoq--lH9TM6fssqS0hvIG2wQ16fqc-hUry5_SDWn6JTxQHoFVDZWDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWqjL0VqqINgcV1CH2darlEhK4L6_9W-bXrYIBCLVavAy7D9q7q2_9gc7L1GLax8KiwSWst8YF6LRpnYHFtELEYPMIPWdk0ATqsSaB3dV7plnyRPxIC2DO5Zo5CNhCXLy21ngN-MIgKOx-IFulcU4P_3T-tNF4k69Yw7NNuayJFUbBGe63JbfruMlIyNSB_bZ1wCboYhWc8OP1iKqU2bwQrEebfcm6Ho-fm1bm5-5pr3XMm0AiAAZJMDCLd-yN0RFA5yCaDfDx9fkmJlvoRQFvzjuxNTFGgdEr4FYNCGPU0NaCsffvsIaTa7CHqcpjhx8glHwvjZGt9saXYFc7bGow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTf3ABrPpvOmk5nmBSiyBVQnidQmAele3ylcfRGSA-yVUX61hqyGApr2torOkl6AYOJLgDrXvXaijxrDIomDf0Q0k_II5Ju6XRXluP57NBaxxeW4rhimAm_yPoXVzMpfg8ZAthU3gZgxPCH1h_qa7IzvcBEmM5ww86KUjDLxSnHiFn_No5QNWQb6wqD5uWo6DcGRACr8xp1L13tn2C7DcdQ7zXrcI4kEmM0Ni_P2sH2ZtCslq-_sOhXw6tXxDo0_YCZN6d9_Az9-VG2QBxgrk1r02DZCh__BLlOjKOdLuvQRK2oaIDY7eI-y5ItCpLsl_diMFFcwWnWXB-Y3zh-nGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITpNRlVpbXCayAEv8HeVRE8H5kT1ndtY7JbXZ-yvHbr3ZJNLl91nT93mnvbdlS_oo5k4Urx3lwcs6yQ2UoeFKx2fJLiITlwMWtSrjRZfww7W424kS_-WEMpIxQ6nhoUMiY2YJKMEqtkJDjMQ_BU4fpIdSODOMvnVwcsitSvSsBiM9SKosmhIbz98NYIXk1Jvb4pkFHvootwcIJNVkXAhPpgCcuMhDtETDcfv0nMHDOBiuyGOY_ujkkLL7_hXyKKUu1yRxsXMFJA_RYIRQMdIguXMxeW0vUyUCXutTWt6NjEJFhrgo6V6K-jT1xcLGYhOiX11dLsmOPUZoh5AESSKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_hQjeHnzk1lXYF9csdQpZAlpblbBtwq1M68e2sNbzwYtTgA2Pl3YkHrTisaZFCMW6oM2xpNiCZ0eloS_uc2SSmth2SdXctsdZsMDLqQJSpPEHqjm754AFgiP-X3E0TllyRp-GkYgaUTaclBqFoDREqt_tYPYRzfUAhnjNRYGArZn-C4HrBhE6Qwo48O1SXNYDpCUEJgarZeAqO1SpnnPDIRjiOjSBCcEik8wkwJqVK_wbd4_X0eNiqtypRX7QJtpaaU-h1W3GXZw5_pCNSwbbfDHJT9eI7x-805_osuQAhnGLknPAHfoVRujWKDkjT0hXIdPi0WodqOtFxe9cZSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnxwiUaQLo3_tne5_e5iJy8vP-R7lFsguyJKNSE8CQ13iQVUFQrlem_ZyJec1H4DLLe5_m8i5tRX4vK-V0McqCqPSN4LHT9PETlxFexA3Xg5_NvfK1VoO7hZzCm5sf-33lNyIBW1OpK48TVprY2jusUpXMKhBe24QhM-ctUjhAPMEyr5ydCx5XmEC_0Y2fv8jbeUDNKBAQqndJLMmgnOOT9J-sqGUYoPFjAsnCK5DsUI-RZ2Z_FvmTubJK0W45NJzS8ry3e1ho1vcFSxn9s4xIE2DAa3I7U1w_xtvIRI4rEVB9F52ucF1kq93iKWWIJX6Yx2TPoHlP_bktdhyFuv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmA1hRCMiv7sbz16QprN9UlK9IZytk0xmsXs2BbYQbc2s4ABzJsREEEkaQJJtfd9RKSYqkHKuXUBaPpZ6NSPFdP6VlJhXGJ01kjQY3EB-8WzCQNUeqm5RUMts2wATkypyiaxvDSITX2kfITlHCkFPErlsJs9e5hQfgygOvEP7-Uqp8HYILJHSHe3TvwGNK0B8qMaP27CDB-yGMjRTpFSfm_oLNAqj0vU4hIeEiKOfqVoxcJk4mn63vA7flZEswylFNg-B97tgRkjD--DVTGdkU1PXZI8eEqB49UOTZ53CbP04C7Tdw87VNo5qQxmoDhJkIh7ulALiD4fwcOQZMk3AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfmLlSJLWYtShff7WGPmEpH-fy_U2n1XaBWWZsoKerJ2XZrYWA2Pto42c_ny0NuJ9yjhpcfBm6lqkbN48ZJrMMe6ouUOlGRBENKEpRWHcgzftFYdktTTi7rxSVkmQhmu2HcH3Wio36dcsgavYUvwIVSy5qdzd1BpPsvjh6_7fTXN4l7KYq0GfEjRq-MM74qKPDxhua-0h1Y-exUF_30M_GnfGClcnV3wJumddobQsHYf0sXN0droMXTOFD_HQ8WsyCc97hWw1TpSY6NNJy649M2qN8-8sSO-uw5kY7DtZXQl-4uJ78vAPPoJsI7LY_HjPzYnLqzc9nZy4brKwmVirw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=FNOUjvWOdE-lBOx0G_2BSucFAYgZkP2szXp5LaJcrL9Trb5MZ4Fmr4KGTwj1vilFFnnLQ8wobtp2WUH_5af5ALIrxwRsO3KbKK7MDKVmgVHRm52E0xTSwbQn2WkLyv2mzOCXoVEoSOz2V6lscXvGXGtONTqrIJAe4bxbnCDf88SzK7c3Fav7qPlH5hILYHmmdHh-NisEEK5Ugl3TSbu7mOedRj_zdJm9ZHeD7KeFnpzp99R2N8vazeWPCCu2hX0Ty9lVCA5cwKSpJdNTuOqjcPJICv0fxiViRf1YZu1POmk29T4_CLp6nR9KpbB8Cr9wph9p5D8gZtfc4wHX10ZDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=FNOUjvWOdE-lBOx0G_2BSucFAYgZkP2szXp5LaJcrL9Trb5MZ4Fmr4KGTwj1vilFFnnLQ8wobtp2WUH_5af5ALIrxwRsO3KbKK7MDKVmgVHRm52E0xTSwbQn2WkLyv2mzOCXoVEoSOz2V6lscXvGXGtONTqrIJAe4bxbnCDf88SzK7c3Fav7qPlH5hILYHmmdHh-NisEEK5Ugl3TSbu7mOedRj_zdJm9ZHeD7KeFnpzp99R2N8vazeWPCCu2hX0Ty9lVCA5cwKSpJdNTuOqjcPJICv0fxiViRf1YZu1POmk29T4_CLp6nR9KpbB8Cr9wph9p5D8gZtfc4wHX10ZDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCy7O5Stqmo8xxxw6FJ3Sgu-okJpV1XeCUibeg_OQ9zP7GJzgLxTtyAMHQHvvfjs0m63JyMg1OUZYcO0pv3JwJD8xe8vhNdqPYTC0RjCmXsjE4wBpvw2gRBm7WbOV7xEZpQZp7b2nISAfvuaRna79HcDcZNuCKdE4xF2c4znuut_cdy3t4g2nMuF-_duuelK4UlUzDQwOynE43VcLvLS-A16gnXao7LBTDk_JLIfHhVcsUrwg4xVdXrZoZhbv9RwwVklDlDO0X9NsQB6LsDO2u-fg4t3rKfHaHPstx7wcN0sgA9vV9SHdlwqqxzyqGlDPGUjrgONxnunj6M3HXz9mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1P6TZgTMV7ICbWrl5lJPK960RvTMmW8faurNsWFwcEQdqQqi2osyS15FP6F8lVTHxRt7BGV70tvJoFgOiUaGvpRjfggoVIGVnzStU93FMrftJ33TyCuxWmYBMYMZBrgnkielmXF1kPkyN4o-fwHpDnFrZUkuXfrjPXPHbBZs-xx2rXp1xEJ1TI2baQio4XBXjWEyIvfgJhM_RNo-XkybG-expUbhMMbwss33P_eBStHUYNz48alv37jvrwfLVetHuIY5aLUo40oFAEchcE4xvcZfQL8_SF3mVqtz1cnUHHsaK5hWj6SgFr1o2tOaZ-UlYff1ctzJALkBbJg_wNN8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_4nrdar-KHgXAaGe6cTEYZs80cLkpsCkTmkyfFzxIWUd0sH7O_fFAyoT7tJBQnmLIiNATwaT6dPP_TxGlc20BRvFRKBVEhZPSHJBuMBnJ3k0zOa1UcnPfb1hS9kmW5lJmMgp_1554wLPYfoM_jecnYJfgDI3sHoV28xG_jMtpzDhwYidx6MzQNFVFc92-yc3EhyheTzL90PuEJzbBgQBP0haH6LFjONNCW32ReImyQNOCQHwPFKjayoAWsLc4kuGt57ExXX4wosQd_DDya1ljurwMFTpEURrzoVAHcJwmS6_zU71jfxHsN9WlLm6X3US_pe-4_4jb8_aIxjq3Tsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKmPp4LsD567cXVsLTtq4xRRltrAdCTlkV-UVWAGlv2yIXTDGqKKcXyaayqboyw6BrDpxO-sGCP3KUtfXSlSpow-cB1T1vxhvN1-iAz81k2w-a5f069QpUeSDTLjPPgz6NO4HthqJogJ8g7BYQxHJBcyhIXK5a2BUZ1Ove62l_JF8zk4KFeQy2VaEi96CF6nWrtcM_82wjwQC6BYni1YEXLgJLyxjTH3WbWjJKtXWUQbQK8q6cM2IiVhTkbPZCPz5ynAKSVydTSErz4lbjD-x6lPAoDumnBSnXauOKe7epgFAtPZNyHaEr35RRabZqEeKm1ZVkvgpMA8LREbVvDrwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhYf5pSwTRuXvp_IbcMrJOZeRQ5T1pMthvbHycP3g0CDWu27-34MWfitlPZLjSvUaa-tx1p0PWRtWj7PUO8XpArMpJf0ekgW1qbH9ZJmVtrBbut8_AQlFHgRM4CNHXYLlalVBVnYI8m1cHV1-TULRg_zM4sr7HCZotdHuLdmKJPeEUs3t-OIdiLkNvussHibWTnDYEsug5AgjRiLPV7H91V_9RHbHTxvDc1LoxB32gRBMath8h7jzIRhn9HUSPJM5qbjdTahMcFVElc81KOgrY0Ce5sKkxZQb1qzrG_sk_LIil_O09vnyCsklgahrSTIRH2FDCz5s7T3IZnD_cQK1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_JXaA5vRYTHTeEe24gOLkmyUG83H4sB7krRCqnWszb0dP_29I40054HQKFF9XjJAC801rJ3rw0GkeeKPQ7Rs97Qo7G-WgrQEgxTUJSLY3B2twlSUQgMGoIYyXSY3kYVuAx7CqtnsSx0GC5GwrE4dW98WSGeTXnGQTEaF0Xo8kDv7lDGFnS-gZALakuWGxcSBavmYHQSaCK3zhBDSNW3ZDLu2W4rRGwqULNCnYzOSLDBnI_a-5rl_qTO6RLJMeSE98S-AzrVereYz8ObDQ79XjT6ngUhP-nTAVCmpidWySv6P3A7m4O-zLJAan7zK4-WnuACqMTCiyW5VJgduhxdZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ashUrK_KzJ5R6b8rMy8FNQTAbehJXyV9Dw_K8bcB25k52kVuKq_lQf-bZRhLxLTfa8flXXUmv4aBzBFU7kkXlaMHxj0PJlxbglrafQN64HditURPd9l33hpNK5_zat8jhWREkSpBHZXm-NbfbQpBF7Us7xYep4ABuAZhmp3s6TTRomuacsdsrikx7hqB6jJL6_4zsxybyL1HBrLblV_DQQ9tV8CT0DyZnMhBziL3iIxSrW8411UJbEy7uqdyFplNwV74RipJ0KTsepdcogYoMe8mdvb7eyMY-EYC-JsaQ4g_h0ZvEKsyNeAJ_J7mmVXYrCwdd_uen5cuFi9Iul37Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rt4QKfZVF3OVujzIiVwOkwXZakOvetmjl5_6hdsTcqBXrUUfxghfVpLDTE224kueq0Pm3ZqYGzhHm2JwtvErdKg2A9vJNGNbpfGtVamFAdv3FxYu16qTUgr5MEyl7ShDx7Eb23Hd3olEyNjfiBZIrknH13oqZjEk_Qc-CMUWheeCRMa0SbhJitRU0pI_Ltxx2iaUogpiYq54VTFSoDwlD0wGYWFPQBwnemclfLTdITi3BotnWVcBfhLroHjfRSo0kib2I1PPYGEIHhmv5juDCImQCPnFy6pZk-W15a72zFs5H1vbtMe1UHlcKOlEUQzhXG37CX1gbEvWS837vw5DAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnHu_C-4qpooXjaohMMgqTDY29p8FnZxnwNTXCr44wmJiI50yCQ_siEQWuELXGzHvAbDK31UOemeUjPd5_Afp2el-O0LoMQREfESF1YRMl6DMDQ-L9TSnawl7sSoWPvPQ-DDSGZ1mHMlqZQd5Q081bS4N2v5xgjRAB--jWuueCdE6TKjupg3xct4ddRW9evdabbJUwQsONEcUhVTQzayfA968J0FGHhw5e0DBEeaR42hbz3eHD0uIVH_xTeUn9sw2ltu3Ailz58kTTllv2TJyzLwIkErpjRLrNUn8xeAz6yycxLgLeCX8t3oIxW_-fg--qNx9Z0ySI2uifW3nUBUpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6vsxHsDnMeGJB6T82VEI4rd49aVMIa15roZy0ePZMITW6jgg8o4i0hh3NgaGHqss-Ar6n7I0onYEbpHRlTJse9Qys_CjxRpiPn8IgFfMIjggbzvaGu0zi9_DilezhFez2hlYXlsry4bzV4AIWOx2557DvNBtqsbLSEW_5E5z_LqLdl_Nu5W7I4Pj0MisxqLGU1zlgTf_efszAVwiK6zWE2PFFhn6BQx5SGWEVDRjECJje9u51VifMnYGZevwqiwtPzvjbeW3mGWCi3s23XMBpHpxCw9SLHZS6BDwMHtPAhaRyftEVY_imAxUjbQ6pZpUxrqWVsovoolEinDgMUbmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyiUmKnB_XggPYeMNnijY-lB2WDmXutzioy1bMIyNsIoNjRBD1R980d9Ix4oNzMUyLGzfcfEZMhnDi68JDwWR40EgYY6WEoPmNDEduFq-s8P4uhuMAAmYVExh2fwLzJkpZSBhlx3rocFOPja3E1SUZYUKeWVxg2Sg29ufymV47TNDA83rGTnZFS29WBWcARTEr4-4g-Gbw2mokyiDUlgkmvYEC5V3QuORZdOIArSeY2q0Fx67Jt5xAVv_6mvtUfF8QtObvPH9vpCsLp_UNgOEGjRUXCDJCnUzyVWEF-HR2BBaOn6XJwJCjlziBqnOOM9A4UOKKa6YfLoHrboK9toqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO-ttHKujn35R5f7A_O_Sp4lzEd6oQvq1PktnRpu-0P4O2P9Xc03YfkXGcgxOxG5bLp5D1r72JU2zF5Cn37lmk_hCYTrlnrwCg3x0WmrdgnYocR3V60M4kr-XlwBxxC0ivuItdJ6nIhjqP8u4o6iqmXaMLTwRNZ3IeHX_j9-MJkJ10Rwa7_EXsM1BPTlwEmq_msRD4GgRcKEzI3OiX6MJOUOIAjZWLv94z7z9ATy0Thp1bO22jGQ-ZNHRm1dmsvgpl6-hsyog44Jt-NJl1ylTpveHVi6HmFM4orPhOH54kBG4mOUUQmUgU2qgDvaVWHau9hnqypoKKxY30Vr4mxJ0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEFWAyeMd42poy_1A9bN-bRswxR0K_ZG8UbS0zGHiINMaMGhZiGyVgHwoezacY75pAgzCt-XYobbHQlSUY0gl3pCR463osK_KhCi0V4m_X8DG_yj1kfXFQsbVTYCt5omOEgTaUAY75pefV7BrNk74e8xf_AD7-pxhFrxgoPPgsLJaTvxBFB04i9M09c24wifpSLIpyNmr5lIdquRETADZgT0KQkC2LTN7U3Hc_hTPur7jklYOj-_7V3AgNzB99IdHS_vPo5hrPHJylIWLMicLVBx2Bpy8WKTjWpNH0gFxrAmMzoeMetlhJcNSKHM48SHZePfioeK8ZFpI5BVjN7rQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjImQqDgoVs7LfnoLW8Fi0k070H_vPCKI_d2cclbntuqRKx8aWuhCZmzyoU_a_Z75ylGMygrzxYveubUbz-yjaR1xOvtIjsbe77imexTUZU6LwAZXOTOfMUEAQEQ7xKf6gBQL1X3WEDDk5npLrA4PyZ-GUpz06aV5h8FOQZ97xm6xb1AeAnyDrZn6vbBl-vUvptbMbvUcdlpSLa66yc_9TJWmHNFA6jDqC2WqV1aycdamyHDRdXidE5IuRq0ecNgHUnl39Q4wK5fR9LCbHFtE-GGVA4a4AFGbL3GPh-s0yoocdxUC4iiZCTZE-V-ImFumFEE0HUUYR9CkWwROsUEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVCtzRIrKP1vzBUR_eH88eCZ9d50OyojHfQ3W2m3BdCodAnYuaaZn_0MnZ4yAi2DO9_BFhn0YH7L4Lw2yGPKiWhgobM_TjhD0xFkPypYckvMPR1RbmNuGgDTaaA2yM-PTG8dqgqmwEDKEQCxwb2oRWgz_mJWkofCwytnDWQXvN6q-1bPEd6BTciXLbDT1uQbFRtvdX5LqaGnX20yQzsgPcgtQ91A2mG-g9wVU9zz3wmIpRSmzaV_pD-RZzHSZ4IgtAIofGgGmaHBII8UhEYRXMLV6w1kduIMzgR-F7xdGYJv2L8DOFO8tedYERXUCvDchcjy8LeLCyZ51SuJXUiywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P08AG21xh9N1q5u204mktUwsPsZ75QAxOdPS3HfJjQ15rcrfFVYton4073P-Q7Vvd3obmTv6vtFlVQRYs8AqopSp0Z5f1T-1hmBg0FSeHAGm_l0-josx7KBd7HYX_7Zrbag0XNtfsXcUflmMbgEpuatK2YiVFT7Y7srugH4E93OcTelli2mg0w2OL2NWRZBa-0dYVVitEroGp5uA736y2u6T_6ur3c5XdoPTuuXmzmjIBGATLnuElMRO4qUjh9Ztqf9mDpIlA6h8PmDRYy3epodBxc-UVHfxz5O6URTQ7VjGVg-xwgGlhBVsAE1H1CSsMMy1DIh3SEx0O9mhJTkd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN6b3nj8KNF1wPuvdNna6vh5TocyuEaNC-JpY5noQtfHisKGBY6w9c6lwHXW402ZdRoUCnrVAEGuWvvFbszTq2dgSe-k3teXAVI6RnZVgUXOmAVj5yjug_j2jFTKXmX1btxe4LVfePXHrcdXJy_shQ6MpC6Ol4esr86TVyuS2fvguuuqNwLbfhH_g05RXs3vFGOCOt_CIf_y7WbkcUXwdmJKOBjYZ_c0o3yaAmV3aeWP94ZhUZZwXitE7g86nMA2gkWKZvJ3MWUt1AhHX41ItVNxhB1jcg9P1XB6pJ9nKuQG5LfOAEH8PutnflYx3xRSvO87G9LW3sO0mQIkJNjqxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyQp3y470OpXYE1qsWG2kF3r3rLELGaPmeA3WSjdqaveYgJsDzAel6IPmOs_Wgnrqa7A2c1MGoA1YMU_DmywLUkCmv5jKay4cbedJMblUaTBMNowRBLlPeBwVVxTaw3chZAhMLGhbPJKBujGF3TmL_YuYfHUAk_RcVCv4gjrBpZ2Yeb_k6zIrWYyV1AgODLAqXEtfAS6Xw5ojP2IxwuLclxS653Qbw-AZT2kKAsy0lWucU2hjm8XKqdb63NB0LIU_TcUAJHaSBxS9ZaSwqVIdPWH40M5traTEN_rdJgvDUm4MJil577UVwR_sjAd00o35Gunf1nMVqE1ttuS-Rg2KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQcAgfCD4Oy_X4X024fQVMnMBv9-mbgEhaBXSGSJyN7fplILdrDJjlc7r3ajJaBzZf_S071M1hqEEAwLt1q6POzyJXE98vKo--XWqk6BID2FndVw74uTiQF_iEBtqTMvouCsX5nJqSmPXS2sS3X6og9WSZZWAD6JMBjnrpZ6casGRBvkCbPCokvqBoOfaMIFyvTEucTogLZabfZgW-JB2obp7HxqBhaIBNpi1SdHGS8iO5w4U_IM8xo9glkJS79elgHSt-rppSJ_DX7z7-GP2ql67Aiw_gaEAjgGcqlQf-4GXzql4eXe_4SugHYARVJ6DtCnz3VI8Pw67x06HKNGgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfNkh9foVIf3l1tUogblOPQ72bqpn-Jdw5TDH0SjtknrABzMASqPhqzhzRUz8E3zx-D9vF1NZIDXgZaAQri5nWPU_pvzvRvvePgALwLIWo8kP6-dNwze9zqIR1ZBQLdqlkyMw7Y_VHb7NVlL2yM_XcUzmRF5IlyaBHswSUTfe40H0xkjZz7jHicZx62Ty8YmlEeqtCC8cpmMF2zwurEbp0eS5JdrL_UqWIBGA6I_JbuNmWGEFVfwbrkiK2nWWKiE9W2wKzoLsvUyEnyeZ-Cq7xR_IpLYba26PlV4V1qa9PzzjFF8qsFZ9PyfwsFbdDPf8COc7s5eHRGDBibVFMUoDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt_VZg7qnh5UVQ3GCnu1a5nRIOmTNFC4nyN0hNbQxMeRYBqPA0cW3mF0Ff3Um9yT5BHfQY6L9E5zuLkvVdpjg4ACcOzUa0H4FDYMvkiOiiS0-dygxqwQgBNcq1AtzSzfSXr4RLVFqxdW6Oww4eb3oPk7Yxigvb8-TkLPNkYQCihbmYpeJBje-wUGwTcfTK1by0jePz2jg2XO9u2imDr1paFcGkiV-cTOuWfen_OPu2xQ9HVwa3DwB3ZAqzNMH5KosMUX8YpEyUNOz1LzEbGX4WsGvXOqKqxMdFUPOOCSboFEda_uZS2DBkxKepbqbOMp7BvUKewETFpEqBVw_mnTGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_v68-KZhhtOd-txPYtbjN-Q7cO-O_E-UixMI3P3uCo31rhR1y6FC1nW-Tfh6tb-DoFPJ8gkw0CWADW85ID7EVD4ut2T1nDc-J5Z-r_7EqOXXMjTEWA_C8UVD87JWMzKNozhVHHjWOiXx-_OBVqwo_EnZX5_l9cEKtlKnDN5Mhks8LdPXJWnCSFXCOhxP8j1NtI7_DSkkessx8szHXdxp-joxy_86hHlWyA4hT4KlYqWqbJ50z27D52FdjC3C9Y_VtOwdpHi_UI5WGaqd5_XeRfK9AXUfYdbthTF7zuHEX9kt86MKctOBa6IzMWQOnam2hBGZLIDtyQiMMEsuWZ2OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvviEycLc0kgji1rETTIRnxfNccIGnXZf3-tQeewKkWiq_pTmlKCO8AN8gk_p9mX4_rwAaz9oU8kEEU9Tf-JQLKFsXckoacujpLc31Ta2N7AWvQwQR4Yt-8HDUHub67M7Y-Rv_11FFK9o_C0wgUw4biSX5zRwh7P-oTvOo7o6gKCMch82DOWlPMQe8r8kwcChRXO_2roM7NJj19QHabV0PIEw52uHGjwI2JkmBPk4_Xd6MNFCa2Kn-jnauBdLVApn5kG6Lj9KZEpKshPyda0MZMQ6GrKVj7ixQEvva-yJ_pA8KOw1Jt1ahAhrztJPF6lBP9EUsGYKK387Lnbe3YBoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw-B4t4QZOelnCniCRAYqX-ISjG_vka5J4fnBt0ICKgPKKMNgDfVApJz4Kfywm7HeNiZNcDwBPvo31YU1yRKlcpJQPylzcd1P_29D_LkwETtQqCWm3uH6nPi7VpfCzkMgL6PZ2kCvyLzyP_ZL4CJMsqm4ohy_eua4HbQzUrG6VPqvN2HiR5M4xBWHjS1JCzAU3kzGY3FIrTC6uYO8zGIHUEtWPofmahB0AytfGmEh5wAYnpG3ZBK2hTaV7ggvVW3WJLhCkqdD1UKRdBpI8D4m_-FfwORbjqS3LxCjLl9mNDJq-EpN8avkw2fU3zn15eygM3RzH4QnEialpcmCvvqbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyLEVqVs5RUo9T_DFSwmWXtiYsTANbOArpYirrUGTQKIfxqnBQk-eDuDzJDtClUZjXqyma8H8zvQ4LKGQwhH5GRkDega3f2QErKT5TRIs8D4gr4BDnmwfD3boVarGm4UdhnUFAXqJ21xPv27SXEZIjom7StwJ0_06aR5FvqJvNROXNjzhV60lCHBpGsYK1eqsRYV1TdJJEpvfpq7AziKWDiYmnY44toR2rLelZesJDGrODwsYeJE62ejIEKAxuwdo7o0bzsE8MWcpjSWXROTgHMk-qfMSsoQTo1yAgpUO1msuWTWKFCj5sVZ9Ta-9nhFUtDFGP2U7f8Nk-wiD3q6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcMJiKKx6FgZel-gsyOTUQOAeuukfs98idzcD7xG0FNKX6vasEVuSJubNngH3EQEVg2KPI4bRWu-0GkTjUVyjsB_chluiNUWaFTrZSUnEa0XSdDHKq4XxFTj3LhHtmLMoI7RfXT7fqCnrM3YuxxqCABkLjZ3lBNAU4ZIIbv0bxpaAKg8Pb25u7CXQRSVKHfPgo68xg9bCyyvXtu40b1MMZRzebqJcUNw4baeqqVfk5LA1UMgB8ix6ILG97AkSmxsTsr3vtdvdrhEC-R_nUKM6RE8PwZpvLF8nmzx6sI7UX8owDoPlQpkC58NDWqfb-PPUkwTIzq7GnDUg6FWpmUjfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTs-N5_YegyNWqJj5WyjZrSw_xwO6pgkGJTxiaDiATDZiSYIO2B7mSTxSkCQE2Q2WfDpTlXRe9XwWJFPCl9b0ZoCvMZoXGD8lEWOkywsWYNFcY7vR1Tg-mZfb2jPm5ZqRk95nmOyNkeQgGUqxtkI5_16Z90TlE1ynjDjGq5zYFcWzss7jzQNJA-Ieo6rCpClPT31dB3eBqNPSuk-FZNTV119c7uwKa4Tm6gIBgs4fXJi6gNvWdXJpbEINB4tXerctNBYtsNH3YQ3_JhW9d8ssaLLDQD5-CCb5n3JPta1er0QzKEJeSrS3B78i48q_57Rc2GOPoA5q8ZmvT4Snf5HUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuIQ3JMfjPpkpaVznIfE61N1TYnliQ_6O13estAa8q9jJ_aa8OB5E8VoppXW9vluhx6xzgPjPFT0HPBaTv8mFpUVB2rwfCtKdiwEfhJ5BuIGETTgRARHaEk2v5ph1W3rIU3tt2AXvQxqRFoItFKpgJaIpDXjKOxEGAXKIezwDZAazCPyEalX5aS2gfq7XbWnT6GRKI-UZZhYd3hkud_cLIGcedXoimK6CEHnCc7Il0Vbzw3DzYs6WB07WO6uJkeh744ZP9W1CRLW2hsEW0ACOXK-LqnuWcycAkUd8rfhaSMMtGNRpZTSZvL750mn2PrZ5AuvC8j8-kiqA8sOpos1HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7ZNW2yqrFE6PxVQHhZYkqFpaGZ171QR6OFwabT9WTKvHGB5gQe9Gw5-7ZLrckyED2CmzzmSnUOJ2Yto45vwQGz8KIWBd7BZogy6tiYInJcXShNRdSlSyKIvWmnLdOczBf0UBTFwCqgoVMRVwyWRhHYRkXSqFuv5daRYrj5tkw5Jth8f77y8d4xf1IV-qknF074BT0PCTjLYROxOwrqqxrVeAQdwgLqugGgf6M8iaS4oNRB1tLupUsn3k1B34SS9bKSuAx3IR2wjNGfL3w37oxggIi051dJxcJlLs6-AriXCT-FdR7ceAfYzmcJ9Oki80XwHG3eZnMK7PMK-9niRFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfGtFPn0eVYzTV6Uw-X7rU-lNmfPyOZ48s1qM9J4utigfFbuUGAOAL1d7qjz0CS-LSJx6X0wIRKNeIl_GlIPnXTi2AAPAs0NBmj5ld_4nQkK0ylcbFBOUA8vdxsuxMoAvnU_T59XWUhDGFTgGzwfp3zkFN1X5wcQncbKsIgETbjPXfFpY2qJgbFrxStlOzA5w7H-MTW4hLAtlXxv1wyItw67KOeRQT8HAuAqrdVWBGe8s8K1wOuPiY_GUVIOwGJwyBkaCyMpxbJ4mFaXXKYQQbgA75_gd99DPqxmjT77nNiiM8-9iyFt8VoXUjoeaTd35Kxs2491kTs1HzQnu7LoNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cak2CpFhuN7rCUxxiwZ6YaoRIECTAEOz_yDxE7sAr9xRwHIasmd7eOv9fkl_g7kbYYpljtNiE738Lql8uJhfVCDF1Fp2_m3rcOr4HC1trXjMYBiz_KRmFEM6iGzywFcWhZYqnehBZHG1Lot7Y0Z7BwB41JuoiZ08QBdoCZYljJKS1xTlXK6QkPbBIdkXmDDbpTntTkOwhboWDj-HKkFgUaSr6SGeufgkfLCdydPbC01Lp1CU-xcwVfR79W611UhSwS0VEmunaQ0rFcIssYpdzI0ivJUmvdfMUbayW_JxD1TavWUt-hH3exeaKojaMCUMOE2VrKa8WzL2XR0LJlzBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHoZhCDVJztzF5KZxDFlouK9nd11XsklIaHz7EfxO2yNBlPRSuFb_me5OCcbnANn2b2TTXBwxizyoz84AZ9NtHI0yk2F3rMGKLBNfKZj6QUoXviWkZJqtDhsPJDjDuDa6zpgjYdfX5QvYdFRGdPy9K8ELRBPKKmKi0FkA65jT7bPq59AMnpQ1U8YaWxUZA5fk2Su37GyekdGUGPGdEG6q6NYL1U52oI_e3WE52k7CdTBAhpel_BKrNLAlMLP_OrqI9Pru63uZ49uZsFbrn44StITCFOFOdvAezuiwgEE_iveDXGd7g4sMridVYhOVy8gPGCXTzVCBHcchx_2IRAWuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL_9-WhjwEr-XN5Cat-R-Zy6lDRbU22HC_tf52289lC8oklJRLtcFltb-T2i_rLRGKZiufER5eF7s8p7QdhbSNCA0EOjr3ONG1ShycIT-DuoYc9xs5BBQ3xoBm7nyJ2PsIsg1fHf4Tum7gHqSH-bZ1_Ngq4-ffWW93kQiMWyLb5AnURP3PIaPi5MEM6RZy1T9OFmk38pc1DPGay-bv0mVa92Ukoc0M_C1Es7XWbJcZIhPJa-AIl8mxuTY1UOIMn-AQLPEGylSR9GkHVf0ToonudNO1slZPkvEu_YCkVxlO6SXN7OCYXMKr8Wz7DABHOIMm_DL-mdAvnFF6EjchpfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHtqqGfX-i6tiwwk1OxIj_vbKOBymEO18WeNLxOKf2n7ISpsoZoLeXYBptIVV4vSJ_oE31rProGApXl-N9ui66teco6RelSCi26-gX233VvkQgoKs7J5fqPCYNdl1xx21B0G1gv6jKdhvJbzFyBbvMHV2QMlMr_sYbVykeGg6OH-jdNVdzLhE0xoSc2iPoyIC3mpHQFrMG5EmPraZVkrgmJWAoQXIIjPiEqBXE-TKprsC6ByZegRNSwEndWL6uK1-h4ZHt8vOgBP2KBlWmMGcYMFMtnBnJ4yVxlXAdLwB9arjjvykpYCGhZUKPZU_11vZeCk99K4XbbrHM7jC23-3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajEjeTX5b06CpptU2cn7e9fU-eH5I4r5WHW8DEd7bHmoDA0XqIh1mv7utD1IQRXX_pEc5P4QHpEPda7YV2azpWpWSghfNiJXy_ZIsCgx6CEraQHS_L4RuBfeyIUBypr4D5ajvjsB5Cn0JKLcsXbDoXAgZrAaqJJd__YnUFPsP_qKiq6Uj-Ok8GK6PRnlWAHpU7a090p2LbDZZ6KuCdwCbSrEV4U2vqDvmWm_vAG04gMeGb8pHWJVxToG-In_Uc6GxgxdK9YkXISpNh7_aa8OudrrhKcwlTgUN5X9qrr-CP12RQc75URgqGeme5F7G_xv6O_sYSle0MIpyzOwLknJ4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-2NBQVCkuMk8egNqyvR7-zZYcbNV7gh8mIKujw9N-oQs51VuYyFTniJ2odLzaCdQ9AUxBFNF87nOYnplKxXnxu-T77sO6fepbuWU0wh3V_Am5fqq6_HyrrKVZq4msO4XW9EnDKWHY0fdiUplkCYVBrqFjvjM2NbwRJA6qRo3TDUd5bCY9M__zkyyTQzV__f5J7ZdfqnLz8IpWqziU0WDmBIkzoZRyCbed0kwPMNlr8XmvN1ozW5e3IZcOjLJ3k-ymHo8pN8D-fMSUIQaeprjcrt055oz-xWvz4VyFALfHykxhT5lSXE0SPtkVVt-MnERSFgOHh4M6TWFUbs7AmF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZhfK9dBf9a6H2GefzxFtZYlwMEnvlNpzTWVAufa-PXwRuTl0Da_Tw7xkBZUYHypZGVi2T4SH74zZCuhKVBKjR1YsY1XbXA1qrA2Ng_ulbCEUnEqdCaRGiFoWsG7mJ71kEz6zK-L-ZlxiG-yWmCv9gqOBx233yjeCEK1w68vEgtnWOBcyhKlVSDy8PXdFw729euERegrzTB_MLppBpH7T5ZdGBQcCY7DTd46d2Ek1lh_7LWqe6isdVp04I00wImNW0TXICoRanfZokRHmIqKq39jmdR6jZL2ej1CcanHlISpzIPwKjV2Top2ql8dkRru3WelZvvykeUCnsx9Pa3dAVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLjYSIhW7x1pxSr8ajw9-65DVJzI4X5kst4YWztr_M93XgEW7SyHZhq_49o2QTbfnhdNrxfJRPjIy_VXT8vCf1dZ9ZUoMIjrIEeK8pu6kl81UXWwb40oW8tjSPD0xrVxiqQczUzcpIzNbWFYp9MopHbUWy5xghZBytEdlJ2SjQ67bPnvL_WEkpofzs6Wey1NEoksPVBQuXzwTyH-QjbkwGhpzkTJhzMPuP90YxusfjyGl8DAhwA77NI6M8iqnUOZS3jMtdrIIGgmKfqBPLxfM0kUuiViwvbAlNKkLzm214s_lBRhf-sAQpj4GB6Wj0vE0hNxkGjqXPckq1_DEFyt3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUtu8M7NSmvqqcsb0u90DsOpe39RmZfbWBCV5RZSYYIWE4Wgo-iU72L1l8IgqeB4Z1Yj8LtqK49I8MQdQKWkozOYSub9gTcP06o3B_SZ3mjXB3Khm8JSaQlTxfYU0t3_AdbAdkHDSd8u_4spDB7AppU_XzyMUfBkHMNdq19YvQK5kOpgld2jXxrLQW3Zq-rAu2ZMe6PEHdKdYK6Sys6wEzBmBp6noIMYozp_aHsjd6eKYSpz8J3AsI9z21hWFSliRmLFuF8r3w83IB9Eb2aumrK_XV1_nKBMI0MnuPkEy05_mgGPUCb67BPlLnld4j_rKHQQCOz6VT6CCfg0dN1SOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6J5gARJ4uHJeGvEhdgLL7iJoQ1UoBuJZgIUNHHZR380U3kgsiBXcz2uQXX8CDnpxL61JGo_AE_U7TF2FkGst31zaqLLqw_OjJnVVZs9A-PbWKTxWu-A3FMhxci-yZ0Dh1ZdybKCLKbfqyN_nTPSPxRTXHm5td1g4ZklQ2D5HRD-JM7Pr7XXZy_lsAwnpTVkC_NoZMN41p_4amIK-I-mhbeTlF2t_aLF4JnDOiOrlgmIXfp0tvaeiLlQWMIkS60FLZBzNBlqSALSwclJHt4kRUbiIsGSgHQ4UwEGaUtAsC9mG7O8X7mpDFV7GU4-SdKAYK0cToF6d74STtkcqy8aEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPMQT4Xu0YUCEi9dtx6pl2YzQGL0HPAnpevdX9AjYqiIRJJY_WbhiAFFulhLmSLTKe9-T2CskEmJg__KgoEGadkaJJoBJpjFq-wZFUENSqY_976-wZgHTPGHOFvn7uA_asNeLWH1SeXnaPPkPwh7joKGdvrDb3kiQSXXFNDlyuHMxSeJgImJ9cPsqMUqYUs7foKN2SOfJCd5nhnZVGeJhUNwZXTos57_C0Jdz3h-1kPknrwtPSTkbTQUOvtaSzydXtfUtvaLc8Gyb6U3kQLo3KPeFZXDVVks3M2RR-l8iWC66VdYOhejvRyVBqRfMG8FuklFjcLk2Ny8PNrXCuclOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGtrRPJ857rBsg6lYu83SGCkjCTCR7nlbzuYD0AF0MiWoUC8MzCfShZMCugUskg-ESUSDISS9xgD7MZPwYXRJW0kRaRdwupAQ9XUhIvdqJJLLkWLc4RrOUOrLyIDu79bQ0tMC32j0fjotIcqmoHFglRYePw_lsMb9TZ1B_YG_pchm5BnISipdsollwfHWtwo05f4Rdh9NKmDmVSz7QZ8Xno-A1kuys5BMPV7i_KiVrFx7kbJXG8eF8P0sTs6P3VQgpVzH_9IY9fYrnjqIHff8jjjUS3mC2u6c--gMI_sksv_4oKLBfT32XhuBMOcngFL_HvEhik2hlk40lKZjNdBQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP8VCq1iC1HnM4c85q1j228RRsJMq3LqjlzBiYJgKLDJrlW8qkpOBbXj10AjpCSHsLgt_6af1JoZM1wGVB4XddDXdRx942Hmzy9_Vh4c0km1QP15BzbVxEPAqtv2Pe_Se5CZ9uLU7a3p7_KoquYG3CwOMFKY7RRkXotOy_gCBzOvKpQ9EgyTtvQnVfgPnbsqE78FSOmOJUkBIQJIn2tyRPhymEzNCzH12P9CjAFGJO6gbwtXge9XhJz05fP5slZb6-Nob_wVNGV0hIPF7P2JxmLTsg_H4lVOQ4hDbCyhbuvJ1zON3sLDl2OdX47uM8BTL-0RRZNdIjRqoHqKQ8RNIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1W12I7xUfwphdCNuf_TT8V0f7O6nUgige4otfcv_lJQRctrtV74GmbGpSaNRw8jxLNu1IFFW7TurykIlD8h7WJbEGJcs2g3TbvNR9AL1HxoY6B0wnqr-TIms3IrTpNwpreQlKzv9HoAEaQZDtgNGQN7l61LkZu4AAmh9eGgg7Cm4FBZyMWRscnh9MWj0vSsQFjYG0IKNNboVpORMEfZNiYCsWkTu8w1KrswIO-HXMKfr7ZuJPzChDlU1a3i1G7MVHIzPi4a04NLU_j2nVK48P-YkgYqtEVdkVDxkNNhPzLPsnfeZy_p35y8qLloyDdLIz2Cl611rEUcHjfVsqdLUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h52DCraEREj9KLfR2b4uUV08a8tAMIZ_yLSSWhbyD9OZIXSMoy_YW1lp37KDjCEQiTpCWtDfaCLJrEsBnmxy-EH86U5038mbWd5atLZZ5c0QKeoRPnXHCB-uB8V_ZEeS_9DfXf0OCPENhiAWCiEGGzC_ZFPYr-hDiQA9S407LtbYSADn5sM2I0O8dsJKkUq3xH4BPlct8hngdUrFIQsF3c0SExEdC3bbwuIkxaNCQocG1aRVz2GO3VkMuPZIvpypiopASwuLbYGO1wR7opsmsWkeyfYKqx9U7JQVkZO3W9rUW6dC0d9WFdPcRM2ruG1t8jWFVD3vVkUk5iF0GRtS6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY71rB-_EUCDz9cnuzXnbvqxhA8DZo5OdZQfn52fKVcxRRGJ0pilKYbgnx18rFN3LbYvMhiyC8S92JI4KLTJ2sxf9008ROKM_3XUHSzHg8CsobBTkSSzgfLkV_bZifUJB_mcHTKRRcWcPCaRFXIKdMH_sNTCH88wQvWx0YAm0xiyFFl3Pt-ONry7HbwFkCBAvgQO-UU1JXMAU9Q98zBwURCPYPfSqHDTBzPUoBkUWqZSIItWaz-5lSVwspRA1tKk9GiZIYqI9h_2KY7vEe_XUZCOAXPWEvlxt-T_mEwj6rMF9RTfJ_uZ1NcHXfAeHXcv-Vbc9qCh3xSLh6P-LThE-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=D6IumrtB0dqMF5x4zP-DUZ15MklIbY2FNuouMwtPLOcWNTyp1oHUpEqmpuqBKo8vDmtNYnlE5S6PNLjPCojGrWMbUKwYNYol_TunbYF5OXxFppsThEmfRbXj0Y-c0vKzXPzCvvs0VO2JCSE-41ZkBtTi22JXxPYa12_oMU9gQG-lNwmCofVM_n_-IGeoOjdmbwJP5vd8xtzmJVGqFWM3tMSYJCRNmlc1XoCQESjrNL6xcpUGi9sHNIlBhde1G9S2Px95k_SGer1nbjAkCjzLJIMr7kBxAU3ZVBuUkwH8-h3QzYrXNm8uhG74x6kLyklhciA_tMRfH5qhKbi9zDU-zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=D6IumrtB0dqMF5x4zP-DUZ15MklIbY2FNuouMwtPLOcWNTyp1oHUpEqmpuqBKo8vDmtNYnlE5S6PNLjPCojGrWMbUKwYNYol_TunbYF5OXxFppsThEmfRbXj0Y-c0vKzXPzCvvs0VO2JCSE-41ZkBtTi22JXxPYa12_oMU9gQG-lNwmCofVM_n_-IGeoOjdmbwJP5vd8xtzmJVGqFWM3tMSYJCRNmlc1XoCQESjrNL6xcpUGi9sHNIlBhde1G9S2Px95k_SGer1nbjAkCjzLJIMr7kBxAU3ZVBuUkwH8-h3QzYrXNm8uhG74x6kLyklhciA_tMRfH5qhKbi9zDU-zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S97MUNCzGKlT845dFoRpr4ScRgMxpJZ6TTL-uxcP5N_I165ZgkOECnAr2hbKNJuCl0WVRd-6MeiXuZl1SCknrGmLkHSieYV6BDYVO2u_zYF4mA1znMlVRd36oTiiKSWg9udfVfntEcx4AtKNIQztHWGIMC0HEymbjsr3L1Ba4_PIs2fdxg2ty_1PKjcZhUqpZtk8Wi8UYCJ8nsj2MjLoE73ZtEgtkrGnWDePlfPzBe_wcc-27IgRfNG_UrjC4GduyL8vXaqpRTIZnFUla-FKdqaRa3iHoFO4mVvxH5aWF7T9zl8AotJgs0aS-4Fr33FJxdXnRV9Lz5UtC1J-sCe_Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICIFYozMP4vds6zJfqWfT4vS71_07uLYKhECzHMBQW5DvqyaAGvYQi_wwAi2rPXrbjLcUX5jzdLPtkk7tyhN-C8V3bd2Y_8RscEMeT-2IcGuHvdxwFDU9aca18tB7GK7V6_3MwBeHCVmeLSVirLIADxbHeMsE9jCCvlH6h0XgetMHS2tXAimGTKcfkPJDvxAO3DU5zv1whyGkfXg0EwylK0EUA1U6dGC-3pnV7zoIPWW3gjFMWSFs0BiATLrPp_D4H70rp_oH6CGJWXwubREKLom_0o8Sz2Qu7Ha6gYQFFz_wjRMS6adxAPc_zA4mQ8HgYDD1iIJ5Wvhf1wwVJtVnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quiZC7-rtd2VjM0AxGkhht5g7ZaORsJBMIETQSyLUSVSXiSp2Hp3ZLAH6QdLovLSnrUq4CJsg2m8KvLjyyDI4lhNdZUbwhGSmadcOPsevC3ipO2KemkAvwR4QGCfTv0EmXp_MShMuH0E2qmnunSRVLUrjEvLG7dKeEHYnc82u34nryY5YsgfOxF-QpQvXR49vMOGhVlnNNo2iZhb-LgWTuvsFvSUthY83A116ON2_Nhp_pweeRvL5wFTJIpeufdqj1144XrbJBjRZg3rx-OvNoUKoBxQYxXX5jHJWCn8fascR8lo4Ep2PBWt5wkBDPJ2bssrBezGshn7kGAq0e-zgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHRpM-oo5c8e6tu0TrTJaPbpKbtXJkH05U0Pg5Z-pYwL4BiUPBDjIUCr0Kn87rI22Md-rJMCq4U9RRgjs5VLHIhrbgcCELzQoiS46fu73x7rlXicQpm9kVp0StX-Sn2Unkb0cDCa_Nny4Cd-DMlKbDMUMN4UTtscDPGdthiWV3dhtrWVF6EPcaMsay7_FhCMvjgP6ixSNmq403AW6dFGmS96cWn5dIYXsfa2vCknWRxmWQTX9A0PnOCSoHzUEmg4_4Aq9Wz3xPvkLqK6VWSUNVljEkn06lmqHGLlCyHV9bfZFsqrrQpk5p27o4Yyf2QGpzHqx5LnMXaXdEXNoHzm5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFQAQG3neX7D65_yAR-8TW9f-JH71fqn_SGwAVuRUrlreNpfld1uSFBg2CECSCl-u6hsOEeoLlD4lh9HPkI111GanfPGaX5ihhluVxnM6s3nUNpH1nanpdXYCIJmMnUwHZqhHxmQKCEhxnmW35WyepJ84B-Yjvq9Z1GSNF_L7c2AdgZ4UhkeGtiT3EfdZMG0OGP_Z1_CAbLHAnHl6vdQZg1c2Ew0P8LEtpCrsIZF7-yC5vyBiEKHGUBhb8r18KFMasqGJNHu8hnlM4NJYvqkhyfnbppOFjG3tJT1WmNX10y0G9ks4Vtgi4h6tV83YG7avb8nbwVhgpcscJB5PT5kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvKHBQQx0D1fC1eONvoq_eTIKZZvks9vIPjA1C0Rs2OwTyoyW3TbtJACux7bcEEVdIzpFFg0dhsVQwt97JycIfjWs6TB5e5PWyUmw63nGaBoM_br8suCc2lVu7XW020yVh87bF34BelzYQCaOwbWRZI2lQR-h5IOcNyHJ5RKMsTJhvB0ew2n_YAcYmcH_0HMhx6k_PiOUdx0bH-Ql_zwFXWzKqJ80JuXpdSFJHMWAdjtkLmVf7jzQ4zjIKfcjVsu7K6cZqMFIyonmwaPonUQ5SBjRqN8WbbNsFnhmMaklq5Hfb8_0De2N6-03g08TUXGuNqJogvwNBDH9FLxW5Yu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgjqGkBzcAXkTp7JW_7bLYBBcmJmM9VHBhemkg4ubwN6BB023j6vaXBpDDbm5qSB88ayMK4cUPbEim0VBN33GellItP0mZYy4rPpAdcSTuuTWa3q3vTvmy-1Dzd-jk9VBlI5ge2q0qohwlbrk5bA__4BeFj3FvKITrqVgrg3nEr2ThP5YftI_at15AYzYjBviyB1EKnmeUAAG__VjMT0S2IxGAFFrgBbYq5hOE2xHPn4IUuMfRpit99sPYdAyOlBSxFFbGWFWAlHlTjtI3UqCFES6DMPukS_focAHQ6oGSNFvfnzeKQrH-1jOtuLg7f6NUqK8NllQMJNOSR3Du4Icw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=J8qUYHw5jhkbDGje4LkrH4QDLBC09i_pPn1ZCqfmDRIrwb0oLUppAGyxK6r7dES3wwpTvIilL_pRu-H848sSR5CfHy5y1rLqdmZtp9i3HFqvfjvHhiPWSXGgRKU3Rs7T300R9Qbdfg7MU01idgw5V3zX7XX67Ap2NokveyTsjXDzsnkHtEo7FnCAFZWnR3f5C7Do-HafHiTck5ZSfxLRil-qEI7bxZHO5l47HxdwWKoC9frccNGyUOKQKNCR00rQRdCOoyHcliaMcOq9lAQRIOrfmUdMJADvJ4Bxmr4ncrVAgIbu6UIa9oCEOEYPW8LNif_NWuBAB2a_zvSd50Mwqgs4-XyzCsxwq21GOKcdQkdV3f76g9T9jnmyhGYolTeg33kDwEL4W2xr46vByg_O1f-ldAWGE6ZZoJS55aoWfvUWLT-mUDaZHvqH9GgU5e_505KZ2RskEfhZ0G8nE_jx9eUli5AY1ftoIDAgDKayuBHbEfoc3n-NLOJ5ivh_b9innKau42tXoH4xevaREp5wYnp6BUVzA1JXbC2p1rvqpPQ-oMxbE1I-XEdUex17TEgR2uUYxY92SdyJNqLlRk3_qGRNjA28cpCRW8D_aRzc6fKE5NLoZTu6XbCOtWKy0_vHUIqAiDW32FdaL1dIEdv0GeZ-R-iYoeS83YZKhBzorlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=J8qUYHw5jhkbDGje4LkrH4QDLBC09i_pPn1ZCqfmDRIrwb0oLUppAGyxK6r7dES3wwpTvIilL_pRu-H848sSR5CfHy5y1rLqdmZtp9i3HFqvfjvHhiPWSXGgRKU3Rs7T300R9Qbdfg7MU01idgw5V3zX7XX67Ap2NokveyTsjXDzsnkHtEo7FnCAFZWnR3f5C7Do-HafHiTck5ZSfxLRil-qEI7bxZHO5l47HxdwWKoC9frccNGyUOKQKNCR00rQRdCOoyHcliaMcOq9lAQRIOrfmUdMJADvJ4Bxmr4ncrVAgIbu6UIa9oCEOEYPW8LNif_NWuBAB2a_zvSd50Mwqgs4-XyzCsxwq21GOKcdQkdV3f76g9T9jnmyhGYolTeg33kDwEL4W2xr46vByg_O1f-ldAWGE6ZZoJS55aoWfvUWLT-mUDaZHvqH9GgU5e_505KZ2RskEfhZ0G8nE_jx9eUli5AY1ftoIDAgDKayuBHbEfoc3n-NLOJ5ivh_b9innKau42tXoH4xevaREp5wYnp6BUVzA1JXbC2p1rvqpPQ-oMxbE1I-XEdUex17TEgR2uUYxY92SdyJNqLlRk3_qGRNjA28cpCRW8D_aRzc6fKE5NLoZTu6XbCOtWKy0_vHUIqAiDW32FdaL1dIEdv0GeZ-R-iYoeS83YZKhBzorlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCXwHrcTngzkMetP6lDjFjdn5ZHTZyzYUsuBPvq1HR_uB5wGmOm-_KcuwPiCRceN9gzed8bTzgtO36m2GHGg3Lmi1k4Oane5b_bn9Yl6_lJN180M2m9bpRw4ygEZSIcJBNnLowD-Da2u8B_LFWjD3ztOmWWg597wxFsY4pbhc8FwM3pCkv_UTeHjv7mkUKQ8TPyhs1DydgM_wFYpspGR-qyhPuki3X_j_m0mn3GTsMGLdlWk20_qTjbUzF4CWtZbC4lAp4ptJ2JVUOkKWIboochQNpS7N9vM-Fp2HZ9qQNhcOZghfIYoMS2jnGocbCD9L4O_19CDBKAyUWl69Ek3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IIYNb6gycbzwIbLJJtBWw7YScOZybUvrF5sW2aVlFd4kpJY7haTgUYqSD8uiAtzOZOuCwPmY-14S48A-ZZ1Ky1GoE9ZKDnL27_ePSyhSdHyFuLf61no3xIv1Vk7aMc4dE4dTv1KtALz_3I5au0wkdN0jN9J0oNBSqZSRw-3bdichlUBMPztgda_Q4fMeKl3wueRmegjLwJR0eeTN4IsN5G-ifxU9TTLIOcj-cqa8xiqT9SCDps4OZP5bSOsVare6NGkQy6aRh5iPXs1_y_WypYMRQlsanI1IjP40o_XmX1FSZa55sHEhYo0iMLZmNL-fv0qTC3XGD8U3Rk8x2pIknQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWjID-DyVroIfgIjOoHWHNPROm5LFZ-Oi4CzjQijOIvy1TPOr71MwW56QTYIOd-EOj8QGwpWpOkyox_ixbswh6e-2xRkSTMg9OcvFPV5c4hLHe7HNX5JFZZz9a8ulKvYMGv2ZsrCzbVuNl1ol4p9J7k1wfByY5K-oaICuUNO81fJvep2j2LlgCIz79UemF3_9WvWhtS5jyTHSAeqw4jiYt1F9BLqivwoSGmEE5FSmaijW7pSHuD0jB982LPm4G9UfFT6ZIZEtJ6u4YmbLZSgK49UhRz_BHqtqGalWn6z5aH8W7BJeInMIjyS6Ko7GtRbDFVO2Ue-IkA0EpAoow31cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHoD4IleV-JBpRF0BTIEgjsXyaU20CAagCm7fgzj_wqRMJ-BrahOQYPRdAa2xeE7Mu4UG29TUomVBWjTq9mIcykLfys8mNga-U0Lc7HcFTXG27cNtfJpaKHMwH9YoskvmqyRI45KdtYuX1VCn0DCNbEUNY5N5Y73q-UYg_a9Ny0nJrJbMXIubh9fvTuia9EbZrP2udKioMLIAcU1229YJU-R3RNaPUqiL5Y67eTKqstf_WkNo3WT4U4ZmGCVGAVkIYEVLlspQoIDssO17nMXv2jeK8ZpOolqwHV8jwiLr-YKEUpqboIxDg5rvvt_hjYYs7bV728BxZcn-Qc0Zx3RUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TINS4A34-XY2T_ZkSyhyjjDcUrQpFEB1GOt0hLT4cogffJtTo_VjyvZwi1i1sXE7GiuwQRN9KBYmRih7xX2Aj_EXRaNBIBjHGMiTu4Iv38G3iYrzA5hFWUxOw0oKfYkYjmlsDR8SgYc4bGOk112lwckl6JKi_Ycfwit2i9zVVMomk-75NDHTl_jlNezuB-H1Y93KEnH5IhYr6K0VIwNPejd9ejdFSi8LBPHWtSAb2gjOy8A8eII6BIvMSUnNQOJL9SA3SzyWsScf6JB2XTbt4OpsVbaX8bvFpfB37hwPmL3jPURVYIEU10FtvOmcdWZdryANYJt0PPeBYdjXrFuydA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TJkP3VT2aoOw6Ec0Mlhr-M2GpI_DWjeK4LCTULdXNg7CFGLzWALJACUnFZaXjwycte58Qj3e483KL3_4CupzeA9AAazrNPcnD484p5L6IoUQ05kFl2h9Ha_icuwbWi_qurS6AH66G9HpBNJnLR7ty1QWmlo6QT6HrH8ogqIjT9mpQ1OLH4tFiMlvu2McHBqqey166d8F2k4gT-CH0Gs0P-6DOjUTwM9zywFtvtq0Yh22a1Flm__47jv6YGJMQjHkx-9JMEfGHP35zr0Bw5QDWHI_TtjReDQgyDjU0vIzJRH0YIIAO6vPFNaTu3Zg5JO2mqeuZTUCtgiJw_JOeq_PYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0TJkP3VT2aoOw6Ec0Mlhr-M2GpI_DWjeK4LCTULdXNg7CFGLzWALJACUnFZaXjwycte58Qj3e483KL3_4CupzeA9AAazrNPcnD484p5L6IoUQ05kFl2h9Ha_icuwbWi_qurS6AH66G9HpBNJnLR7ty1QWmlo6QT6HrH8ogqIjT9mpQ1OLH4tFiMlvu2McHBqqey166d8F2k4gT-CH0Gs0P-6DOjUTwM9zywFtvtq0Yh22a1Flm__47jv6YGJMQjHkx-9JMEfGHP35zr0Bw5QDWHI_TtjReDQgyDjU0vIzJRH0YIIAO6vPFNaTu3Zg5JO2mqeuZTUCtgiJw_JOeq_PYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP5HUWdHL1CffbNj_9lRcl1cOt8aA4f2gwelRIBSG22FE2lBTnMS8SFkzh5X9NEA1Bm2Kbw4NsHkAuUOFP2s8sNiKRaiThpN3CqhRJ0KIb_BlXwBtP2iY5cPuP6e2H97Qkxj1IZQrAsZFkN7DP-qktsQXX7lJmc4BCCnAgi8jcMpwHRYfpfkgqvB61mOmJRcmWFOttFCSZAv9rBqUDGfVLorUqOxSIMjPONp3292j6aD_9fsTS7ADCKkxQ-DLZLqj4Q1ap8N6UNk9qMeHEbOre8xJ7yevH5tHtg0e-XxNWBHEqPftFEMdnTvcSnmc9cu6fkqL25JGh70hOqjcWf7hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuyBweOHzrsg2n367Usd9ORuiRJDzJmeOVao53CAHLJ_q26dXnVY3kRwUeSDv5eKfSfQMLfH5XLW7b_2miZtr3D5d_iVZmaiY2Ldnwq-j8bChjtHdcCS8Rv_k7B3QXhkSDqClderTNtnS0jP2df3FJXshOaNOTwSjfK00cKCNVpDQiYB_-N985_v6s5pFd9-s8aS9uAowXn_ZNxtqSSARnsRng4MvrwAxCax5JzBdCIDoD-pRYr9NxJQvlDRF9iltwXjiI8-RCx5F9KmoiJ6xjbrqyrxD26z7hl93pt5Aq9kxQRINj-6Vs-adMPQdvk5pKkBqMGW-r_2SEBs8SEn_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwPd518ZcEAzIwyyHOZ98W1if08X_lEYXg1Pou95C-1BcHUxBz8wGPUbx58brMOwC_BQuabKZdZbM5AnyT_105a774Lep-0_Q15i0Muow00FEw9HIl9-M8jB6XL5_8eCgz6HRNdhks61rC1059MewJ9OO-NeVb3_I5hysj6q8eCI361YDrS0Vm5Anb8lfV0lMsqXHQxqSpsiqeGMtJO64aIHiK-15sS9F8tFFfZwNTKPH420a9e7eURKuvvFt5BFG2Yqy40Pqao990sbcDCPaHzo52j-0ShMt-shAqpsyrezDnbaunSi65PQ2JYKxV2JX7Y4MQlo96HPH6h-7UKizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZp8nb1d_jayJd7Gu3-DB3vanhEny6fnJsb6T7ENq0WNO1Jm8EJJa8tpEbOxfqnplAk1JjpGqbVTB_fHHIzmF5smh5ZdpZ81HqeyyatWA4rzPen7UUZVZiToYRayL5L24ppIzKTNBlpbN6V9euf3bk9plB6CIlixYwtXjNfq7UUNh1iyI9hYlufxAZauYWRu0jMBdpLWespo0eKUSlyALHIpAFJDwWdZ9_6qokYY2l6oH4pLw45Mlin3vdU63fXksy4M5u4NnoSIdvBHRxK4vzFARBtWWwE3ziAi3IMCZw2KgAMjlZdpTd5KZQQX0JyLdO9uXMc_3w-YPxgoeTq0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX0Ze3F5WTinhfx2LI2rDjOnLW3bacOcd3lotbQLpvagLJcjaMgV_SsjM9bdyvVKmYFvuuUiPkVPvDf6A7vyLVciUr6cxA9pXQP1s47WciHkxMoq8tgnjH7RYcWEkEi9M2l73MBVEdaD_Vj4utSMv9jy9aC6AR-CgIwKg2SQnmmMoQTixznP72zu_5XEzUgldcnjZwGEyM9K6aqfaV9ImhIz-8L6dpRsdUcJAk-JU4pFo81AENcmZuXXL_s7seBwGEPMRl1batkGYMQGhGFzuYxuZOOskoXKyIgQZTdBnyY23FYmFkJX0RfDEjmnbafmYE6flzQfwxRocCDmdlAr0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4fUiVMb-3mS2ihi0w0GI7XM4DV4PKrZvQz1FZKDoYT6djc3EiTHQZyq62K8iDm9JspQBDdsyJIoU4sfMohwqQE78nnHiq3qyxgQz6cLGfkggkjzHZmRMFfPDdS-L-Z-lw1yRWcqT70_PEaJHe8X7kEbvrFVJJlUzChtJtE-SwjdeHQpVvdaoH6Wdo_E5NcboSemhZDMOAfJPG1YLtRdq7iuFbflcvRN_ZSk6YRjGnDzt1pcvtW31patEtKveJdrron1iqYivAkZb1mGjIT_muuwAjf5ECzKPOM6n9fURuCYnBPZmjFabMGz9p7umFkeOMiUyFHGtkcdqjq7FVgGCQ.jpg" alt="photo" loading="lazy"/></div>
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
