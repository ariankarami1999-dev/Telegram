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
<img src="https://cdn4.telesco.pe/file/IF56yJXK-gNl2Rm7oxdLVwrpL3l0Z2lshdrl7xnSmS31bDqIOpiMl0WqOEPjTyPs_BKLW8dn77XZrA14XDdXeyLQtjsmkKjAYZw7W3A-IytOQm4LM_TZlHOYFCp2wzr_yuSbZLSFMeYc3YKPMndYV9vrGu2brf6N4Gg4JbwTBdOuMDWyD8N0qP03DAiWlu6A91vikY6Y_EwATbL1Qih5NhxzZZekIZiiolVdyapvJVOQqlG9EYkH3csqNssi_zwUp539IGBpAy8bAnrFeEtgaTWjVzn8UOw-1tTSfcS2O45Uo_bLw_vDrh1YwbWRLkXmsYIAUR2ZCMK7vYkhEUniAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 20:58:16</div>
<hr>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 274 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 372 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byl9m6IAhbDFVpW3skiBpPV8NZ6QIE6sWQaE0uEnOO948IwB7UPT6yXcEOfUt1rR3ufRU4UELkcxklPgppY8-ODR-6H1kA404kQ_ACSmbdwdN74D2_Sd2gwTGVxsKCBdFp3qcLT8ax_pYAckQ8vV3mcrKR_2Mng0RCoDxJp-X6tNaoL21m_VxGUO1N3Dp8PXzftuEEcLCHniu95PtfILqqrAlbQg8T8gc-GuX8Eo-WQEA7rKFEOlmExbWoLz7LVeXJlWUOUBt305XsuqVxA0MrOK5DcKrv5FnZ6aIj0I0R_GDcFtjTv3jUU5fJzl_ZajdA36ja39wWCOSZgY31NdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 469 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovy-f1ND5vi3MZ_KUnqczYv-h73m5-07L7jF5ddqxi8N5XIxZtPMTr2imaBT-gepjTrsuAO99k4WxsKyumtWPkdEkYotcUlT4JCaLjpQbsxKnV9Skftl2hcyuCnjip-otGudF90_Clu48FC-b80qEJobKItlnf8msbwqdMncw_h2BTW53h-Hb0oRrIKNjr7w4BISzmOlOAvGT7-kNXKDRCw_aoi61eiE0x2hpC76rgSPGvMzmadlpMI6kmGjgEXuIzHBLl1_l6JdraFVmMM6E0CfUlqjHrI5mUQu_RbqqoY0wL8i6M8j9tI3tqDXu1F20uFNMPuM2tuZHtOiJzS9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZtSZxzBZcsYCo769y-4p8L8qG-eSctBV9OeMIVRu-8DaToeep_P0xN5QvZhgX2xxS3A3JDIhsxbMvPnUO1TtdzKp8wG2roc9ZgLSCk3QAxyk3Ti9JK4ct5_l3EOoeAST3DIcvRsNZRceXjfsADyoLNhICQ6hq17tGxb1MNC8qOmQi7JeMT85xgfqKyumCQVzmNXwNIQ9GWlA7YnUj1Ob09_ysgUyyp8Z2_DbbHTVeFpJYPERMYz1pkgNqO0aE1ulY8y4sVr0d1XAqPlnSSHpHzf3PbzKPK3kLlbBC7iQlhwZf12Gn1uDw5E92Sqms-9z0shZZwx2WHN3EJFD-qgIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAUBxYNoiEdL4MwvcbgsJqaC3d5HnkrnxYE-rDGD2sQGo2b0KmTNfRFPo_i3OQ38tfgMRKd2z_mhJDk7f3cWAnceFdcwdEU67UaE-uYUl-nP6QLPIwifwJuJcU0z8-oMLhrNEwhLz6eETP3hIsLfu-haKR2s4P4ZNcVSsJqaH_yTKUi2-f4MELkVpvoIbEVT42gbC1Y7PdeOo3fnMFEylywsgJlHuEtVcH_1xJxaFWl0kmJGtHkt_hzt4GZTC-A0P_KO1skzqK2WV5hmkYdoJKYFPJ7P8YTEh-FYMzWdusDvhGuEX5xVBWbGNo7wlWhCg4mx1FtBOOM9q5eai4j38w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhvuLwWlgiuWpAVKLRIOYsiQCNfopb_UDxzrayHkfzEcEFRAeqI96-g59PMRGnzNDI-SN1uq1gtyYkTvKia1FKsdVfslb113fn5tRrVgeFxpCYeXrnyjm3Mpt7P34NEbUmLTbR01VomvNPEroed0-nufwuI8PamJ3pqTLbwlcwzXlcBx8GuzT5890Dx4aOCxmIAvmY3Xdlyu6HsSAa-s1n-Pl5a6-qU-JhjUpilfvXHp8tj-lGKgYXclYLBXvX7dFpyLFhbZjJ7mrzYFYCqrw7lhAUB8hwiP1liKQ_kmWkH5b6Vuy44bjqKUx3Gkem0u4P5oxzd2kBDqgbjCypYL2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ex8yoBNg3Csq8d-cl3tE2VMhTSvUYw-1dI7dnAXWtCeYGAcR0pB_LD9Eu9f3WDm6sa3jkcwxc8nmmkV2D-Q9N4x78D6JkR5BjEp2hEf5NPaS86y1eLQVGKnZ-3-wRrnthmcGr92_B8HhIJAcIR7w5n6OTW-QHNBFXqLDH5kqeaJGIEtMM7-BW5DeptFzIgTpH-VoKBrsNkJwXUb9Gasss_LRqdG1sGJLOwj4BnJy_lkHb5Cc5akJKtOpg9aa8-DNaH-4FdcXPn9njJ9fNNLCG5IGwTOXhWuAo0Tj74H_b18qiPoHQ9fFMxLbeHyIN5QEn9AoIpT_Ucr9hQogOqGshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4QVWJXPMS28LOTWHTQP-MUnRM9h5cinTabFVtOD9telcCK_4yzXUjNi8k_8r2j9G9kVGvAEcqYp-5F6IyZJi36Y9ndTioR3TAFnfUB1apNxydVAhj2puwOl2Klb_tp7C3PPV86IZLm7gbGWVQHzL5P8mo5ms3uHksz_-i7y_rmHWxSxpjSGVSFUjdQwlF5iYOw8v2JGL3R0CdK-QRDtx7ArOjUCn_5nLFud22iJymWY2GqEpOP7Is_r_o2IkcdinJWDOsM5GVqzDvWaHKT8EUzgCGGb70d1UiXpoGNipXD-50jbQjjWNeEQVj2iL9nCOVhsjw-dv8S9tO69RaplBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWos78ZTn7AVFcGP8K8xcecz3ROff9o1IPjb8pEG4g8hYPFRMqQpT24t9tsjtDsY1nrQ0zLKGAvfu1wPb0XTex5WTcOr5yoCQrc9ehV0Nie6tpIMTAEy9Tk20varPGlPtWHz0fPpdesKvUy7kfFeuo0SsEE-YCX7gy6-t7oXCgN45b-vRBNhjnEFI167x9rBhRjG4lg9EFJ-mNfOjbhKYrmLF3M0RJUbd4H09NzhufH3HcRZX8u8vxphdo7lQfqqgxd46dxPRekh0uPlrDXqdIFA_P1iQvDOZqwyiC-x3GRx0VUvrH5htMaDfXRKMODFcUWlstiww9r9L3HP76KU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaPWneMgwnS5n-unV6c8Wj8YnPW0vVimo2BO6CoU6NIb5W8LWcTJ2KcLwZjyjfpQWs8xIN9a9pQQ-6wG9mNgRkbUdRTicsel_-NqgQUgSgbjn1xlicz-PlRM6f_LL40T0Q6yaAGoWYjlvY0B386IWazc436lIK4I96UR82892Yq_Gr4viWzaMMh_ulSIj2zSKgjPzztH89LYvMGG6nov4X1TgSQ71Bxp2uXiLyLRkWpAtyT0Nd826J8oZ9RrB6n2d2aVvaIRJ3n0KXW9PFcHHfFcSmS9VZAXgY3ZwvTDeAsemGHb7uMuyWkPk1HEyDo5EPQH4HqQ8liJSwsfj7osJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlNY_kVKkWUHDz7ZlPbTdRYBLj_gpjTHArX1j-PD6iboPVHSjuv1RAnCHhamVIpfCWNNfkGxezs5AioIZ_NunuJ58obV7zjDKZrebbSMvNtYkdmhREgzL8djeBMvB-Ufx9xpT879wkH2L-2NYiG2beXAiGsUiF1R2EeEWZb0OgE8EETIy1-OxoY14sS1BsEMO0fzpka7fE9vocY34yGdhK3NUKRna1Bf82KawWLZed7n83GnsUvA0qm4yN-egSt2em-sd0OBqmjXdVWIvk0uNAy3WJ0KnvgnAqD2W9wc8sFAhxNrNqU5EMkYeoR2vLGR91Zw0OeDM5ZGhQCs83xJ_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=cdN9Qhn70l4BSPdyOnsIRHsODuAMtICyR7fyW90rNhcIoOQThs3g2ayTOcfxDNFi4buVb3UafITYV2fxrKvfb95tIixQ99U5UmuFLKz5uEyh9ZS7K7rLe1I23dVaX0j_zYc_-R7KUzWOfIEc9B5FPo9yAqZamoizduoFYz1UMRwXSBNJ7_9Y4myqco64eN8CGIwHH0e1WmLfH6aRH4aY8USCFUX-GXzBZ6iZgR_vjviJ6QV6ZlLdLh1vFbg5r6IkzyzbGs3Egnpp-45qVssSinzlnnO9SBslgDL9Id91doTXEkxP1SF851yGblVivPHbbceC2V22imn3A58cJqrpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=cdN9Qhn70l4BSPdyOnsIRHsODuAMtICyR7fyW90rNhcIoOQThs3g2ayTOcfxDNFi4buVb3UafITYV2fxrKvfb95tIixQ99U5UmuFLKz5uEyh9ZS7K7rLe1I23dVaX0j_zYc_-R7KUzWOfIEc9B5FPo9yAqZamoizduoFYz1UMRwXSBNJ7_9Y4myqco64eN8CGIwHH0e1WmLfH6aRH4aY8USCFUX-GXzBZ6iZgR_vjviJ6QV6ZlLdLh1vFbg5r6IkzyzbGs3Egnpp-45qVssSinzlnnO9SBslgDL9Id91doTXEkxP1SF851yGblVivPHbbceC2V22imn3A58cJqrpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frIfrMwxd4f6w9DpHgAacvpbUq8een0yeqn2K6Tx8ZiSXtSK8qKsDEhmgigqawOd3XwOJSwXLbSmvTiQvJ_ZnP-7f5iUIJXQUB2HtDOct3yWY5XH61XyDr3kvXS5dPj9NhmtpB0Q91VJ2vd0xWQQaSE4Xb4VXsRs1-EHj8DFZjnC55qpEq5nxOqIDIEWRfdC-YYN6OZX_WiFRR9MSkyrHB-Zq7bD2S9LxyK7cAl0b5UUkrRiD_Xh3ebLHk7x6VaF8kqTknqLBA0YK95fmFXpo4fU1BbX7J7cCe6hJdILcZccM_gb1nr67oTFQfdLtMVgRRYaKr2hNzHKaXhhNBgzoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfZO2msdtX5aeN7uKJJmzxLhcKLWGigCRuz_xA_oCkD8Ppr-Q0oDWWKWhHugjfxD6ZLeajTl2_ChzDHZ_D69GirTiKBngJk0sdXXy8JMEagYPWPfm0TInKccm7gkCJ6UVowcDG67hNOhpwkOdOLE16_Bvb_lhbmMr1xexI-o-2Q59JuFxwuKVExV-u4t9kRkqqc63sXefQm_us8GNuxWrao9f_qFiF6FgbIra63AC8wBzfqc4Caa_NQ_WNbQMZQxWx2eCgMUXH6_abty_tXId6Wi54LsaH29sHSqvZEuIFKh6XYLxqxouzIDnGRMuaHs8k3xJOTC4QrJmpftfnaFaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckWDqcWG7REfur3_zHgUM3lTrX0U93V2wBjVU-sWYw4oPx6JyZHTVz3yK44fOSFjYaMUr0NNMpXsDJEOWA1O0Q1wjqpPhrejWTMw7nNiEGmWvaanpdYDm7r6IpzgSGyva5-hFuuWE5oAfpHyL5hld9jqWHoXPS_UxooCEorofIIhhoGCq_sl6ajMlmXaD2azWs8PhDCxWw8FQUQqB0otn4o3_HbDV_JaRV1d5Gv154iN9wZF3mMX5l_V0-VzQXA6kwGb-w6Dqbn-fhQB-_Fk8C6Px2xhaQDGU51I7JXaTnAivhGw0iWhfo46LAGoIf9b4iPl4YDihO4kd4V492pfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcgHe5zCEzLwMI5PiHN_PQsuKz1ktumY7kGDz4TODP8w-3OFL987mkIrik8Sz-n2RWYPkT0l5IfAcA8kiLnBgnb2g2SZuTo_9wDi_gPQaUt1_9dkn4Fk7JcBs0QDIZKpiEXXdHj2zb_Naj1pwtbJ9ma1VycfNtncAv4EN34oSCiccy_2wiHhaV3yFa3bl-QxP1DWqWDiFFceFSCobQ--OBt9zlWLhDhnmzUOmQUO4pI3-NJvlslknmn9P3wIYN7JIvwm9gYj15iS9rU-jUAh896NofeAxGV9KDi0UvnY-Yf9aKXZc_Db2Fq0TV1qwIVfXOEHs5WxK4H9m7BBsntvuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XifREDWD_gUGMBl5IT9RXgXTUeXpy5XMfO4dES723RPJqJUQlRnr9w40aXtg_89iRGYcgUI3t8FqDkm1AG-5obR9BhA9Cwg05P-jiGNC016BnNyVyB22KmwY2qBJ52iOkXfBOsyEKF1WHBAGRTbTttzEtepddSJGOfkZdQPB-I64108qozkCjT0DLZwfuU5lSkcOxDlInL98agwjBV4ec7DA2o_PHO91JKzEi5UJ4H4lnu6WPLvZLLwYOcU9DkEtG4DS1eWqSpQ2F5X_Xh7Hip96FmnEnJ35NxmrR-YQCeboQ0Qtyxt6e3BdQpWATw8wvI8iv6rbJoaHtxvTT1C6EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB1F8gfirscdAYok7aM8LSnjFuJjn_-kH74CN0VSl4qVzgbARZDOAv4SX0CB9Dlwux6uVs6_LtK8u7TPshmLFs4jEYJwPjlpUuZZwISlgUB_crxhCHkxb_gkdLpDpyDPLmcfn_LmWOFx58eCok9IgwZoEieGGp1LHuCWFSXuMO9dEtpskxoQJkbXdv4Dg4AoSNn7_rXpoPX7jXv0KpG1ZNOtBk0BpaCxv7o67kcVmGIzG3SFYbPlS3t36iHi2P4ht6u6tgxrbn4SDVZ6V5HmrW81tHvm14Tg5oVWD8ZExbAmjNeUKEe0nXNMb9ho6avIK9R44xW43PSYkhn1fF_9vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhDlR4MaX1WU8wj4fBgkiCs9Dj-fU-3k28It-9jGrzsz7_BHIMBQWZWW42ETmo3rd4v7LCaq1AUOAkHh8hLK-n1jZjBJ3AhFFxPc5WQvEZGkvuL14DJmH_KJD47hy6u_FlYAxOywOZfFTEVzqgwK27slfUijEzrQJ5_s2dK254nbRxboVnzQb9PQj--_R_tsVpKu5_5-bftpMwhjOQrE9jmKfRMEQx5jn9aVEvHR32CMl0g0w_EBx0bXIj-iJHCzL9iEjXG_MIP2DVfNMixeuFC9m2m-s2luHO1sOtB_XLEtos3PhPJKan8MbhQLUwNUaDDHw5Vr3zoX2wiCknhrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eq7fibOUcGDpR_Mu7WvzKLJ-fDkNuxXpBobeNhn2E9gxDg6fY1EL4aMbq9UVH8BXDivU6I9_7wvGrvfkAcd0ysCOXJq6KMyuIsodc2zJm0du-E2OPnQ4sA9bOvhQXQYYYdC0hjVI9Fh4QnjKr3sE0O-G8-MgMNaUc7h0VzCnhvnEdW8uwkLibn2lmSHyzuQqhbPu_PXzahKva070wsJj7MGZqhyK0C6QYktp_7RCq4gUrcQdqE-i53nDckh124CJ58uqPC6347xZxz-IKQgVPP8r0qmZ_0i8O6rJorEzgu6KEz4cBeMSTFwSrOOWiBL0bchNLdRE5libXiALddM5gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOcFlUD_Uzjd-q8QFmDjHJ5-7PG1Z4Ni4gnEtm3agoOwTk8JoADVa2NmRKEhL0BWakDE0smBW2wPRRp9_1A85nt0z2ydLBI8ni7LHL3ODwQiQq7eJ-lfEIjln0SXpsJJuF91JCZ-QcN3hbb7l8Pr5CoteX8pqUTJEYw_GO_5EveHd04KOVi1wBZl7nceA9vJVvVwNIWEGduK3UAL1CjBPXOJSDFZjAEhkcYKKkq07OKSwph_K_zIc6K4cGwhGJ5JpObb2IDLOUuct2dqgGqpg_b_HNv2nJFP8YNWTXlmb1I5kKWJZ3L6o_EteUJb8xo4BA8neMDP3k5S7JEBuGP_GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8vZ10INPZU-YR5ax5x-0XFhyMzt2LFKIeJ2NulgYw6BlnZ0OifmQMhhULfcHqNg4u-UTvmFaHd15MJ8F-zmInbxcRrPFhluX53BvuD6rJJbK-KU0mfHJpunyBecL1AGxIwvwJ0-tjErXYJ2fwXMhBBWlYcDqDXyXoZ6UOsmEsAvR-kbK-0EJfZTXMiKVlxpLJ_P_EhbPkl7NaDNW5CeoL9dDoEZK-bdR9uM92KO4cqr3z3WVBYJQEjmlybXIvmTeZcnPSqusFlkhPZ213DqZSzEcBqnigTPm4550k_G1RlOMRpO8gdmtLz6RmZBYR6iuS2TKI-gogabfKNVrN5Vpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDIBwh3QqPfZwNfcNUU5DtnS0VMoX7Azxc0zlHMH8viPcYmbKoTunhy_AMecw_KHNQV5A8iZdhIc5kye079dKPk_9uKzHhJWSK9G3sSjcJXn9JWXRzz8JbH6AvLpuMMWoIYvRsXwzxiqSl_XtwLsHRRIeRgIrNN5_5Gzu9_UHcwHv5z2Z-Lm48g0UtdQjuoNfdk7HhQ_Tc7Y7_wKCsc3xxM36XrYVCH0VJy2XLilXqCXM9Y8JgAclDg9YAVh5j_m-TTvMn0EnRG9EcOdiQ3577VWGtSJPnUx-dyDH-uqMRYzvNS_omVAjXOVpEB3MO32xOqWsmS7TasVeN9crc-qwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt1VqXqBpo3gC1ZapqkZi4w7fCpiKocpRz-phzLCQnytFkZVVxOXiwSZ-9Rl8tuHjb-wM1pGuofas6CCsVrpekbXB6kdt61ko5pCN7WavdVLsm0i7DgSsWuMDgXkQhJP4HyoZ0mAffTBnqawE04RK7qSzbqULfur4gOXPVBo0sE6AZwr6Q3dGMK7ir9ljqEN4V9qHyk33REceVtCIsjGkYOUZARhO4olipebMdtIFMrGQdsS2whJVsk8YXzEgvuREVBm0Zl4VsRldbTZsaGh7NG4TrDZbJGmhpw-rItISFSFyw1AgT4S1GJmRWNOdAHVaYYI3nqzFruLp6sbhOwf7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqDzGl9FQam7MB06b-IHt2QJj6f4D-r6uTi17TsgMfNFxcarRtJrl6hYo_cgMXVY_znzAUNsYXNMZdoqwuk5FJCQP2IdNYnmJ_HA5PY23h9earQr6J_qm-E3CYgu5XEs46hjjBziPZhycAzCv27E82EKt1MmjJFK0tZWgo1K7tAm0MQJKKXgrYW2NINIl6yGx9h5uXwBl7E8X5DFR-EiDGHW79EioTI2qYwCjcfcbCuAEAPQoF5XmSdWKLrpRq3iyzZWU1ZOGe2QM0Wlz57nFYBtbgi7KLgKPVOcuWqFPEyc3vry7rzAePDmmmFjvbSGbA_o4nBT3CtItPpNRfsgPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntdHs4JQrW3ixzDV7jNcpK61TrrKrk_8-77d4bMJjp0xM7ZAP4DYN0fgLZnK5FpmC0qRjd_SnNYm-DVD-8n_Kj5tdixs9kfeS4DUmZswVMSn4FFC4Bl5o7QJuO7NW6iKuyjX-CGZh3KlJmpv-j48a4FaIriue-MVCnHTvq8KwP5ebOl7wD3saKz4FpvOo1vBTUZf-u6ifmvrc1kqCoyHxJF3cor-KGwktY4Kkmd2EldYFVlPNEjD6kdNgPcm5yKR6AiGHu__rU2kDpRqPCxjObBe4Ar-7EWuYrWwzyzN2AANCZgxv9i_iK8R7l61gHe6x7lzn7grJf_uG_PEHI0kuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OklxLFO_6lB2aEQWo6KBL1IS1sgR6UAkfTEqGuofrOpa87DVMEOoamQUCCX_s8WpWww18lOn505hUPCMpZtQE_A-xPjtUAdD9o2u_i4IMM5oM8y1nj2z8p50V33KcsRSXRz5LWzgDg-kMZdn-3jrEYAPGdezsUlAva_z3KtZd0gp7p7zhyH2csIvJ8ZjzYkzdU9hwAeHiobrLXPNmpl-3ONQ2Tru22aJQghlo9Q2dYhuzuLEHfBlJKatwlF7bk56yhSvE2zG9RsOm1wmzrPTn75fXFVMDOC1qAIMCZYvdMO0bQZRPCWjpLSNazMjVasiUuaDHIMXzMF3FCNAfTxxuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQOspoPQyT-1-xownMQa2er_Kpioz4cbh5I1VY107Ii1APE20THFq3l5w93F8ZVR2R20owDdA8nKookVRny95z9VX6XGvhITdSAaVsKOJp36cT2qlQkkqsNMyTBGvloqhdR8bPcOK8KVB4cj4nsDQhxSpJf1GpsmV9RZxbS9VhcJ0iEDWWpDNfVCGLMiZOtyc8vqijtrpMUg2SzdS_H3N_l5k5wSiW8WN8ZBtsuWqAdRbLLK7nfsPQIJpxHeIA3r-kMOBDbgSBRt5CQ5F-zx9WhYkN-GIzPw0_dICMnAmTMs3vgwJKRyrH9fTEw9mbzVRnPqU-xmg9uLFZdtXIuqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0hgl-wNGUczgqLVeiwaQaoIqR3Y5jRAWg3ksZ-lCwAoDAXRdm9i4m-VCGHxAf37UzwWUz3FrQqRKarpN59EjgFfO8FT00Rfkb16uatUdKMfrOU578kY1gH_SZ7rnVS2ZphGoKdQSIKiLD8LSMKZgGIa2KlI8Cil2sILKip2N67GlTd6DrVM0AG9dmHkf6OP6miO3bGN6jBBRsMR94UbBoUtMdVPYXei6jAUTuQKSGYmFh5OEQF5Wn_0XajMxB3w-BZdGBY72PedR5vh7XS7DWuyWeNasTTN87ZLhQsG-i3jmaryeM04mVvO4T888_XeFzg6LgiK6uZ7klhEUuPjGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvUhYoYth-x3-zUnRc7wSdsFXGlWCWqNUmf4hHFnjXC72L7F5ygvjeX-EZAMX_32_NUHuCISjUGl6TEii6aPx4zQxsxblk659ZV_QI0HooCpFVGsq1LzvI3sxHRvg6ZpRjwSfuvDiiCQVCaOj8Q4DvVNCRf7B_SxGPPjtn_XALzWEt0oYRpCujOwZXRRi8T15sRCEhT0AujeZoAUzrv5eEgh9kp276Eqjww900027Vh5vcRFUky3KCJ1iWFVcdoOY8OZBH7Cwyf7bq1FHVUtvTSud8SVhtrx-wXWDoLIOCRCFOpuY0KbNLoKeaTDxsDclt5gBFmxnmVt3wzQ1TT9sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNvNPc1EzFpZGBMxoCb9PA_LYyUgsIvemq5WsY2uYb4IBdbf2mtKr8XOgjZZwkbtOJetb3u9TrLZ5mZMZIoZz9sO_t15Hf2ZClskG0_aFr22kFj3ZyWXAQlWB92oD-tJ9rMf1D6v_lAJEJVKC6oXfzwogh7XagKoQ2sd3MyWfl0i5GnsFPFnpzczHMdjMsz5PlJseKZuj8kv_RgChViIaDPI2K9Jtk7GBufgbE7KLe8ow9RH7J2V0-AAG_EVxlCBFQ0ooNS5fkDhx6ceMou2MeAybldKpqZ-dAcUeJQ4TbNaBoDskAy9pn19hWdpKW9zZaH0fL0aGNeW5bLISTraeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVLehiI27tBAaLZKP3wGm6jVUHGxHiZ9SdW7bEvKkvfDICbhehAgAamDP8aTrnpJ6-hkaQMwpB9KvTm88NHszyKUkHWWeojaANzp45Qugo_wOtWyVx44KT8PXbnE4LW6kKx_bZ_mLTE0xt7P3OxdZUsGoaXYyho-PH5oq67XrK06FxXKP68vERuoDaA-upjcBvraRzPqAeAx8tlOQcxRP-FYdHLHWaOlwHMhu17hyLsCV2vDrbdBZZLVFkk9HNHthgWqv8V4vTWQdV9BQIAZtiC2J8IYoAwGMm9lLBC2UK5ii7IHM642ux2y8TrJBaWDyvIKJXErJ27I6MlEGwJ5HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFgEoiQWYN2cnKKXE-t3EDGHnOmC9v9XKXm9avqStovVHF1_nz6HjVTvw9LxmOMTpkso_rmSDttw829H7G_mQBDWadMYM9IsvX6HXumSWy0SiCdSGOM92qVg2tF_lowPKFuK70xkMk4cBJ2E1CsEABzJySRDNwz3oW4H9oK0ynYeTOeX-qCzPt1zhef818eoFluix5Fj0mhl3GBpxJWbGbHaF2uvAaCT59Tk9ICeV6mNh4NBhMKYEJ1R4dYJS96Q-81K14tctxMF7J_H7uG1jRti780lRrNnhS3KbjqB5Q_l5TK6QTe4ax2F65xqGkrBpXYo6k6QPruxGfq5u9MyUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBhACKX_qNoyKB05YTAi3VpzpLkUs3_6RuNHFQqrH0H-iEZnfkjL2Jd6_QrVzy7HDTV4IBHmAxzAi4NWwn40G2o-QnCIghLLvEpIl5na5kfOzWS6ajKLMDV7amf83Pr0s_CrpylnfnOxfzWAAV31XWf4kh8I_j2t_8e4SFY5cAH9l1nUax-wJwNeWczriirFZE3SNtboGhDct7ehn-jamxvv0l7hez8xAIqJR3pewplhURCB1pnSi6isggsJVp6CRWHOwdsMpHVOfoEE3lkM5eTwhLGXP9csZxHLhnqrWkuVWfXYdv3C1eIzQc8fDkkivpB5ZMLji9zFdviq7KfSoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNwM_Myfu3vBJHb3CaiPxnUumpxWo9Y1Yxj3qCvowBayXlyf9IFTIdXKC37eg0T_Lua6cIMDnDsVWkla-ouyjNjrz2LoVg8y0nH1sClbBzRnTy72jqnAWgm5UuDG2WD9Kl5szLH9AQ8so-PsTHOqpl6wVXW3YWQy-GzYJVjFUKlgAzHVTMpzWev9ozqEPfMA5VEdE9qVJRby3IdrlQKVONE2JsxpGmike7Sj5ApkvT-pPyNLhrMKrwsKWq5O7kU081qR518_gpI-SreXdZc_WNtSBwCvz7m-0Q09XD2Pw-ruhxSJdBMiauZ6O8ER9QYv78RyU_tey-vnQ_AmpNbCDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhgO58ErEQnQxP1NEHJt0vzKUOZSwaefNjMmU2HM-NyJReVMlnNbFCFImlHIXhNEjGhhf9dq0p__wSt38kHDSdhbtZnczb204olw-SRqa2M-48gYf3dvY4Vh3GfDrM3jWNcEB0WpQEZyl8SagbWy-satbpbfdzBomJ2YcCHdsnDKqPs4HLmhk8RyhyTfWm1kJlfG4udVYvdI-gUupvV23dJEFzkna6qy-kosRugge9LzgOCadPVRMbJmSRCxiL_w7Ai4XzkUk51G_tbDCOK3NFJgVmcFNuasoDQvaHYfC7Q4fCdhUVkxTfSpDmNMsPcGpVbzdpXEdBw2047YjZCOtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYG6NzUKm3tckCNndFef1tgtPPoE4NiQjWSmLOWKWgikD6UFRhlSmoV26kPcMRzGlVGJ1d6Gt8zCkGtAWQO3VOwTjq0Y6rPhpupNxMvNTxwni6QO7HnqTbzlRjEQbG3O0fu0TKxpsvkS3tPrMMTQWdbSuxn0GDMNyFoyw0kudCS804NqsagwoL7R42LK6nTBltE8b6wOLpZJMiY14iEbXHLL0IXtqCnkdAg_tlGBTNlU64oshyP_nSlGO_B6qI2oN-31-Vcha7aTU0AasO2r6sqwZogg86HBQSFG-rFVqRn88BXFfA1sr_cdweLnsVz-Hl2PcqsjDJAMbexUrYirdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-bEyBUsTPe8vSroaE2oYoowMYghH5Ne0oPYGyjIrtyeZuP6OEjlkJvn5B6vSErqT7Yd-H1O5SQ5xY-g0Ba-FqXcn1Hu6JxOYks4jW8OYRrFE98KeknwtVMHC6h5Ml8RLYPWw7857dcpMbPDtFww1RMtiXVnI1gBTJCe0Wkz11RwoEc49bqeFE5C8rMI7_CGV7NsBeHFpbDvmH6XQUV61TSNy9i-mTaK2cpJSNWpBc4SnK88Ay0qYlkJJtm2ie1a1P9CmIzH0ka5uhhpEzLv4P1iB2CpjyFAvbcJYeH320PyK81gjHVpbYunVNTQE39gIsMimcdLhDEaYULVFXFKWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBWpdqSP006iQMaDtS8tefBXuytUl44a7QF88kie5Zj0CTOep7eE-Mb8kl92mzK7doD67Ggfge0czn-zVUXwupnnfuZ9yf2suEW_jHtvlOnp8onNXhg-o7ruI_Kv6eIFgGpmsJkwIawOgJhaxosDKYk5Pv0lFoL3eGr8eJ3Y-Hlz2S0K0lzud5pJM03QVbKjwSeKW_XHw7539Ip01S4R5c5_DGfOtXFm4tV_h-ZsmuBTlQGpuoa9sIB2nSjaZxoRQgdVntm6zVn5uPAGDCl5jShd__EYtXumgq_qP1VrYhE5PDgVgawd6saDA8EwG9dG2KqZ6DzTG6QEFQ2oVEz8nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezBS8yr7gxfQdP_eoBWVBlPyPwPONolEMHSAxuwDRflZKvN7eiq-1wo8M3H11EIqPz7SGv7G5z3EW5xGGIVIxc1ACToxg_xRezIrTMtf_3VE66y9c-Zt3tYs-Nt5w9PEpH74ySNHMJhvFw-p9EtBXtkc_TGaeFBH6y3lqzrKKKFMyHILApW6hfL0vjKtjngAi2oZ2jvUtCIwoHt6PIN6dCbu7bZ_3XxQp84_bgUsKPVb9g_I_jKbWQ7rmUv0H9XyzonwAulelz4pLUi1iABuNbk1unW_C93p7J4wjv6aixZW-MNlJtPvjiAjFZ_W3aFJOryrEN31JbXzHFU7zQzQWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3rJM2j1QshscYGvNlA0cXPexWsO7yF34A5fbG13RzFBj7kj2kZoTt-wbpNujApdSlZUdZBYDlxdP2ENfnDpF3tUsFHc7vU13o5G486POcPaC1vV-JATCy33NP14vhuYhAocJ2krqKsqhcTxl0kMcqSH54HmSc2XYZ8M8nRiAJ8kNjUQEQ0j1IIdDqnDyNsgzztWpib98q1tP91mefsrN2QA1GFXCOo7Rs6C52mpUuVNyR1WL8AZhR0QQHVDGKA0evm4_EWSPmiizEOlkCF3Tw_xXL-gm8fkZiIJ-glbuOQmNo3jaip6Gpk-uCe0COhWcyrEd8HNMr0MOBImNzwWFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kto4S7c-qM9g5A4uy0Z5QiNTdtxpKrvBK64AK6RZLn9xJD-hlCbkkZKPZZi2D757vJQEDj6KnMyu7Az4CVNLb14uCGg2cCDyv-gifPxZlkAB1qhCtVPsMKLj6sshtr96qhYQLLkAXO6dvMtYrNCKh9qcqVYMLBYuWVGLAU2y6qTfwT1DCkPba78R8JU8YEwTzxctBEUhCITcfHgeZud-QYPfIUsc5Zfr_D-Q_5h1goG4JLCrAKRgdUz9tmUfnRZImeNF3RJESsF5PJwZHJqGtnBfzLFwezZyeEJkPv-piy_eD2ZLbTaTGMngb5r2LNdeSD-oQHpflBa2xa0x78cjrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrXJxPZ1tKVzgn6_lG2HxrG39w4QPPwZb0Xv8gqUCX7Xtatfag3NVtM0fRVDUWGm4VZsNNE-_zsUHXnCv8ga1Qq0OUjQjRU7339WzrSfG7b9DMuan8eitIkzNBr5YC0k84h77kLnA1kJ7oTPfadn3VxUh1as5B8o4aQ8Sqz1OOSL9IMlbzKTmB1TDLa2n0fuvRzJVhK9yJlJkUeaXiBmnJkY2Xwe2S2b5-Fqy3jFzvQLHero7MdQrugUbQEtmcYE8rfmdQr572P49Hng2HkVapG637LAPJgi8XGfmBWTw46IvBI0f-ezS9Rcw9pvXvgRfyCMwU9SkWYdCm7g7Fgwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWZm1Nc8kc9T5Rs9oFV_A2y630ByqriglyhNbSOnTS5Iui4tnT1iGaB5ggszgvuozVzxKqYlq6c48s8BKfy-68SqQYyU3uaNsMKfCUfLkVzvTte7EWZsaSJIxCpioqz2wUGLvNDS9SrzcP8mhv048zmkqhukDM3J8QOyh7LzwBcSwijxu30YPVdKIW2d0K29gp7ki-EIa16TYi32bWPGjCXuumBl2ZRpm-oPRh8O5450Y6WnOMY6csVSRLVKYDxGNWry5RDufKjEppfkFfMFseOEcMp6nkZypTOwlHxU6zsvNpXUFsPHwNxfqMOeJoo4jbKXz82ultsPSnQ-d66tHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQWLb9_g8FJkeH6Qs9EmoDpeNzVnv4NaHL2Yy6u1dMQ0bbUp_uOYp3zGHXDp1kgMjo7TCecPpv2-yvaFSSJbp3Ra9hIqIwOv3vjKI97wfY2UNGlfj2BcejwkJ6szO6d25ZtbQoLGCHoPp9o5jr6zydH1_0SkxQbRGAW91MYBK2IRbcm_vyKAGgtYWyUJgb86PTZxRdY_Zr1ZXghTyG7OYMIVn-IykDkniXwIIlFUNX5VwfH252TH4mV-3SuqbhtsQobU3O3OigAtVFNZwZoMqebQAwVBX-6KrG3EzNNZ9DmmQVREsPhQIiSarrztuelfjk506HBsNju9uZk9NYvjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-jjXIRp8Y-7dwxgyeh-wc3ToIOZ5YLmRyaeQhl0Z7GzhIn3I9AAEYL6ZeeujhUPt6gClElNHQxpxSR10trlqETCKs2LEgYb4L66YgBzNAZYypSJea6-StD3qUNtaf9x7RR_vqeXAIrIiRek9miHyzz3bNb08_mpsbg8u3Uq0JZSzgjRyoH4iIHfInsy0Z5cstWUiiEUZ1mQJsKznaSTAoMozTbZL_J_im3R1ckYXti66p0gBu11AEprW1DoIAniXht-ihEnaySQCSVMOAPAGK7lDrisLqYoNCTQ1DxAshXcpfsdK5ZUoScE_dlES7dFteW4hnfUZbGy7RzAxbslMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXFNrJPDVKQ1LnWbizatnWz-W7BDsI8NQdSeDtrOLt0vl0b71vxZG6lVVc4ozYo744q0vBPRD9INl5w28p8Y9AnosVBWTPEjMr_aLv45pskgOU3fp3wzon0zHgW4ZAGBSMeJ1uiNBuNulD49bacJ-qU4m8RzweM4YbSlb_Lh0MYqTWFjmnXddWzR-wghXyNB5koFxyT5uQk9xEVID46aJyiHAnNB9UaOtPtrWPl2dp7t42z4AX1Rszya1cwk-ygFEDR2NSiclVrj0miznBmimO1-xhM3RzFyiw62TtRzCB8b-sdOY0qWoK2Mgf76GIHs2NaFjAvJI7SgtH-MjTsYaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mhsn5Lh47HncQb_r02zGv7XR-O0TmQgEkny7g5MKcU-TqAlCOvsp9wjOB2kA-qRoDRUcqoAi6btxxS6VPmww8zrUZYm8JZv1_ZS_ShEliUiVGKXSSQMQiOkYBKC-1QPLaiAaLq-BJPO3h8Q0d2PfBulYwVCcieys0GBJy4D6pZ9bjMmdJq1QpDMBRdZWQf0C9ncGRA7GZcLPG5YzqokUwXjS687K0Nuxpa-jMseP7JCEdo8HvdCu47aUc-kM4LSRBkZpfsYVzCeJy4jfx-rVuRSRWNNupfhItZD4iWbcMuWRF9Fg46TigH3z8CSIr-TK5CpnMyiIQqXxrvqOnnf5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8CnvTni_PQ0IHxV1KPRfeBYodT-lwAzXwvHHRaI827W0TlD_BxH0Qtnav96q5PW7FCuyZDoKenTmGea8ldeLm6XwCNhLhAD_uXT29FRN-6cPqGP7yQjkemGIuJjBE-thLDlpqs99vVkOv_8MnajgsUZwIvhKsAu6yOn01U6Xwjrywv8Mbp65fTrEAugSU_Sh9PtTQGXqlQSYyn6-edboWqC7oeW8M6Ul3sv66RnWTgkgN39K989MINhaSfsUdWXxt79kYzL66UAKez1GWJ2x8CXSUNuo9iYfGPASOKufIwB31ihqdrCmDahvycyok8LgcFSFYUZGXvx3ejxB1bWSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcpkR7fzwX8eKDbMvmzUWqqZWDbZiv7FgV0X66ruiOUBFpO9_OU7H_Di97lMgFoov4bAiYIK8JxV2b-It_2P6TDwiE4TB3FXZAZUtsmjvObmBQwm2EOqSnQw0g160jPFWg79uBbj7npak6KnnJsbaEMM8D9lTe0LspjnN6bda8mSUqvB41WS55OXKs_QkUoRJdYf7Yf0oI0TxP3ktJ8jOGRkqUvhmLqnAVGltMYOb--EsxcYiiSJrji9V2u9NNJnfMyIJho-FiWXtCYijFD0cvFEZlvRLRrAHr9hlKs4BlrRz2pfcCerZ-bGsU523khGdoyWgx_oEurEf9eZ-mKUZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhOdYb96x0oXO7QePKxIRlaX6esgSs28nFH4GCl575GsN2C-zdQfm9oAzD7wxqRMOmYi-gvTLTzaL4lzqSv03xIFmez-8kF5jo7lSYdv2eSxdVKTsPwllVLIBqvXTnhNcjZnmt5giJm6GR4D1MGlN5KEoiKWcOCkz2nBxT21bUgPT7gj0hF0PhBuDXWZB8nDcavSUXuPbu7IrUUt3-q-7_ez_AqbJWFGExXrCq_9bdff7qtYzOS9UjDurD1Q6M9n0GY2e5fyg_i53O-aLs6dmPlX8B9LxHbQ7JdNvV2ab5zoXWWLNy5t24X2xUXQzxtavArt9d3qm6Wn0sblOOQQrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9gWUhCJIDgBI8XPQdp6Qtb8LX-iTr8IQtZ51OCBgWoOv6LMDSFq3BwPdkjQigK_ZDkopC6lE1-WBcq9eLVQM2iznTDgCtcOjaX6bUmou6ViwAB9pCFGTDvVzX4AHoL-21Cy6KXbQ9nS-S5U_WCsxTVmX9aHXuNdpbOx_SEGq4YYq_M6Pi-Bn19ZeKNzWewSjm-Mp95ZdPlTSNC5RJH_inMN4pCa7LCrTDIoe-IcwB0miyx5Jry-5EOPBFVgO29nxoUecMF6gCQpLIwp3jNMgpeskpV9OE48bFscakeIagTAmrqW3cTbJtXzNWK5d2XEBuHJgeqocRV1Q9X1KOAArg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYII4bDJfcJGoPYK6MXdQkz2tH5CZeeASq5-mviIUypM8MMMPgS6yvuoF7DqLi7rv677FjbYAJCp_qmlVolhcUyf7f6J-xV24nQ-TE_vqYaw5YxJ6WgmYasESSml2bqRcWbvL5a8oImUlWEax8S0N2LNmmMj8jyaUOKaTqAjCyP7QlWoajFkrhmyYsdyIFv6AzWsmByfLCSms4q4wQF-q2vRnDziajiHFH8o3EHWVODst9OrOapM7Q3_okbyuKKBu_DbaRLQ5HQjuRjn1sNt1-UI4IVMe13eACzwjRMxu8KuOSZXEjpAJgbn2YAjyQBOCzm9qUQ7s575cO1RkQtYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcONjJp0ejtcJNHXMduJ7xY8rAUB-1ppwnEk-WNwT4ypqTRfd-ZouGtEwACHst9EOGse86ttWzNCjENZ2C5S80NC4Yb_RGaaDb8JuyTxOYtF_lrP262S1E-jhem7-lLFcQcPBU2FpZFAfR6Yt1c--xXjHJM67HMaxnmAo0W8RWAhWP7hjt2Xnx3vtxm5LW_5bI-tzpIqKfHDV5TnkQLsQA9t8gS_RmKepz0vWQ_qa7NgDV561AOIhpafJOanaDgGYf9zXR3YZTCOKI_eOvPkVb5TojO-5EbZ1aauB-13tbdSHC8nZDwf6s-zKl9kVOQ8UP6fmNfz85iw7Gys-pp8iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCwZaHvNePcObUTat7-5qlRA6-FRBL7AmZKMeruq3A1-wsxMfFAGNatMGrrRSszuvsu64rUjIE5CMtlvijUQcNX_jjszqIMePKjUrimhZ6_9w1D6VnGebj8iaHRMSWQBMqhLWkVf3YZqAYGRQ7u1tVRIl76YKVpZwOHk56iVSd-ta4EVqHc4GolYv6goLdGMI5NFmlGKqLKuLIe6o7yTuma5WTaNbx43PYfC0wlWaZx_Px7VYKHCY8k3jcBCyIsy96v6-zrQVJPG3Mmx556uSszuYJzfsuYDVycx12BeYqFKNYtNYTFT7wmU8Ual3hi7UWiZ_V4ai3I_B_0pO_55sQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rF15VJ5obHek6b_IikXHEcw3xRdeKYFVjFIde4eG9TjhlonoK7v6cSv-xyjLTbJA3YSMpwd9JE2PQMpILEHx2RyGe3eLRcz5r9yUhU5BoKrI-INND9kaEjiRN82Fzn7RZiGgU6cgTqajJ9uwIRMrbkwV5YiiCvbQzra4uX-E-IBst57k9-Z_sxuLhioRNCD_P_nT-tK8UWumGLk6N3RDEdwjCinFb-t9fEOZtQvTeHVYJgn3vvwJSFv5jFCf3afJZg9Fg4xdj4YDeN_TTHToEuqOpTWgPuCAgn7zIx0Vn30g9TXcaxsGzKAYBQ5E38wNC9eClhtXZgXjy0itwKqB4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8WfmJAF-Q3-_e7U-hscHhLLDO7TU6lwfuPHU7K7n841iT_MXpoXGYKFU02ifxlqJecUYiSRgpAVko9b53PPOboUaN7NSlj4b9TU4nM7vziwrVZWcY0ZHgdD4C-vSLgt3ryJ-iaUHd_FtymM7smm5ciy18m3Z0oDY8h2utmOxpQL5Syuef5bJTn8pHx28VSC2L71CvQVr6Engi58xnPMTi4koriV35y3uquNdjEXcyfUHoDUp37luaG5K8WSL0cNu5HNykbqUK9h2AD0S6SqMxry65vepxkFEoOMhWNhHPNFiaA-cQpw5epLZ3zTnM9BVPMoDPvj7eGCsihFu98mvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9okcK1dW5MREa-C9ntXvouS0SD7jaaNEceAhhcaA4EkOUKH0iPmA1EYOfylL-6k0a4EZ3Gp00rPszNMCixVJoDS0TH2YwcoauJO8sMVdwFLE1VFYhGJbu0SIDQujNusbtc2PJna-cpq8wze8Sr-0BGOFwaSqqJVjYqVZScda3iXkNcj9ooeecCOo2KPjrqZjNnRZyPp1uBsfdchcwZzruFUmgPTREvUJhKCO2hUMOh6PkeDqrRwbwS0PA5S8BvEmm7BhMltXNrUbq6zIGvVujT_n9ZWMKqBn_CxN1u8G7tMxiQO3bKhkNTZCBD2GOjEx2WTy_DHBfxnWuD7MxU6Vg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=j4rMXICspV4knwUSGa7zGTWIYDzklhebJjPcwooMT_5Ah9DXMA3VWqBXBV3kAM_-hgYO6aBxTq8cjBncQNSXDIgNgBNITKx72byRrOzZOqhZTMvYdOBXOOmORQHY_OA9_J_vXEjp4Y3wg1bGDx4M3UDotbdIH5mz4UTgadjL1-5FSr0_3YjJfvz5VshqzUVR3N-9loYJ8p5QCR7eOpuQAxRGYjboCu5kKYyGnoM-Ns8FU3kAQYZnuXMcd3Nadd7z8iKAbmt9JBh9Qzei7v8sfl-U57Gre6qxpzMjsM_Uv02yDaHw1kDKCvMIzLAGjZdgyVHdyREY1nwqihlglJPAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=j4rMXICspV4knwUSGa7zGTWIYDzklhebJjPcwooMT_5Ah9DXMA3VWqBXBV3kAM_-hgYO6aBxTq8cjBncQNSXDIgNgBNITKx72byRrOzZOqhZTMvYdOBXOOmORQHY_OA9_J_vXEjp4Y3wg1bGDx4M3UDotbdIH5mz4UTgadjL1-5FSr0_3YjJfvz5VshqzUVR3N-9loYJ8p5QCR7eOpuQAxRGYjboCu5kKYyGnoM-Ns8FU3kAQYZnuXMcd3Nadd7z8iKAbmt9JBh9Qzei7v8sfl-U57Gre6qxpzMjsM_Uv02yDaHw1kDKCvMIzLAGjZdgyVHdyREY1nwqihlglJPAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQW_PRkpkBRBWUG5nPnhaC_fTIIQCF5UtvMlawALOmWweWDJmU0i-eXuXcfOvUSjRTx-UFEw3UKqShL36uTNPwhsvJDxmOiGrIzQc0DSOIW_UN6FjMDTmo33EYVsmQgRIQX8FTdodZvHh2L1a76tKoZ903PgE_Jmj4QX08Pwu0jykZNazwPMHPBO9UJGZiPNtcFosqMFTql8cLmjD2zjWy30dbdMWMVfluDKKuIVoHbxYrsFxwDwN4-dHyGhT8-G_Oi8QBVU-k_s4gPVLdpSLEwOczmoTMOuiLzRUX2xZSLyW1uPZj4SqOoWewwQOz6Wyx8W2tsUkfEkOAGFTZd6ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw7FcyjwTwJLsMDi2IW6gXuQSIwCSi_qYV5jPmlv8MRcBtAcZbywSuzt04h4KXZCnE77m1H8mTtj1pF0fJo4fkaFmERmiA6R9Xo9ASnac2rCww1Ls8hRfFRfwiGJqJ680LJaNYeMF_nwlNAS7UA3Koqt57fzQnO-1HKeFgIDcuGyM_pCWlMLeJy9lHuwbs5zC7l56TP3I3DKVDaX_NWg9gMiLxbj-_49NlH8hZjEixWOenGQ_8q-GdA2dJNmHOMsRQnO-HZS8tOdLrSScgO0bhGxtEr34t97p8EDU1XfQEjeatOAkMvyxF87U-whgciSEPIBqBoHqgTWvCYVEj5WJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kto3CDwHJAVOnYmfINY4UHJFHM_M2NzK33ZUgRt5cFs5GnxXinL1MalTlPOKYjYUu_gXx61YiDigWFBkAGSP_SNyAYztLLk2IGakyOYoR9bf-EliuhJVYJY-fpXUVZUSeNRDX71UZltNcq3_JoW3R3Y3Q71PQ2_foWMNjZKEk1iPMviaB1cBHtS_Y70_C-nLEDXuiAcgfQ_p9pGIL4I2BSyhWR8Tvsefe2jj-VSI7P45-NSj5qPL_HLg98WRchycuKL29a5WzHNOiW3QrupJ7kCrCaS45WHOhBTRKizknXMKArrGuQpVxEw8pzaIQhIC5rGo9dMIvGhZGRAHJXQenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fou-NPMG-_tCp9m9UH8mtE7LqOY3XaM0bAlG2XhAWuljEqQD8zycUn0l4EQrEFR9LzT2EcWCpySP_Mic65RYDVqk3HQ9wrMdw3A4cjt6fJUtv5RmMvcazZAHeu8VgzAk-gJmgNQ4wvht-7awcpdSaEjIfn8KjRoih6TY7rNZuYl31DnQgzL-DyhlJvnHs9RhhsR20dMFrid03-bEL69-LEpsc8AVgdNxmkhkPZnZKLAtN8al-mjIzf1pPdRW3a1S3JVLWfdKuZusO8D9i6emgBuZJEpPCf8KgMwNz086h8Z-TOPWcybdlvyEf3hL-6e5lMwJCZjQyUJGDh1qzbug4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nfl5Ww5tDzeWMjgPANWGLLWLj28VdCYHxWHIjuJGtV_Pv4qY_Ru_4Q6hFCnRMm8l7HSOTQbD2ED-AmgQJqZvqXBzrnUWA-oDqSiLKC6OC6-gSu77OcDprQFLJ1rZ9Ktmf5I28zafH1xp6r5c-Dj4xysK7WKfFigrdO3HAD2igF_xE7etVpxOgAdkJ9VEdPYIJZ7lDiO8pfFIr27Zv3km4TQHNKMlWkSY3zIYwT86ly-PNRinfSaoq-YmYvKE7wCVR2IzGUww6Lq4cPB8_q9qyhECbVrXEzpeFPmmUIbi1GRllqDMdGxHhITGA0QYqdwdMuuIcbNaqOOmSjJ5C6a5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sugEjyFjQDMDFhE6HWONg1gXgPLg-JMCoODDcPcPmdM9-xqo1hSgSKTf-TLCboq7LkR3N0xUlvUNlkIzutJc0YNqRU_G1lgd7O_t6mO6PBObltS6dMjmdFKtEbn4K29bxFlmSBoyTkpK5zrqVDrtSyhKtqIoSWBU5TVKMPxpgNwdVD9phh3hTNdsUQbisxsJRq-yEsEtjNU_LPVScnjIln354tbv9DIpl517NOyoIBtJh80WUUiJRpyFkwJlu0cYRsp1-rAtu0P3FGAlM0jKoBMfz_Y8kPX2GraxlLy4RnyfsBmgmactggpWjM2TcZsvI9ZwVBfoNtw9zlDHljHjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuvPCo6UHgv1WojYEnVJqHZDpUX8eFRUflzWaWI4BOU_gu30GowNjHIVtHm-rop7rArYEkh1L0vyeBq7Ai7oYKRdDoF1l8JthYLr_cNIIJ0S-eeGuww_JlMdbHyxCH25RtZ80HIJOVchVbwOcanUmJhgvis3ubD212dNrv6PV4KC49ykJ1WcQF_TWBgIbmvoAoqHbV7x_A174j3nTKscJ5VzCL8HuiMH1mqz1YnLeyeTb8KeeHH4hNhbxyLSxPl_1XA8CvDZhyefeo9tUd4_A8JCvUoVGTSmeMjotXGDYecuZokKE8iqOmpZTTeA84wHbXbaLpQj2TFRuGdCgs8LYA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sQ9sY4qc61lrs5q8J47M0-0SCUTtJfyQoNRHSqMvWdRhA_g82qi1qzYeeqk_YClEIsgT32h7EgZs5ymrntUslhSa72cboXncm4_us1MndqE6RLpGj4lu9dNacPcAC4t7_i9Vwr1jzhQg4o_bHElEnxBPFaYoRc_sKjkEwiokgenwaCNBETISWlmZRbx1nSsaMxzte1lBlW6SZ1YTrt1aeDyo4343HHpgnxi3FjzU1NPBRdGGVncJSfEpw1Ei5gOUz-aIrWLDv6Umr32FC9YXGiCRLCCY0Mp653Ap_-HYeV4yYlji9oB6kSmT1oYD616749Jc0jCvl8ED64gT86PnwB1lqjH2ei2UZIV9d7GPisKzdZ_P802L717fRRBYY3oXdKMtAR1z7Zr_pENMFwHZWF1bJyGLUGn21YktxeNmJys-Y2oZwuyP6dnK058GVD1b0FyeYjhIrN0_gsuuCLvBlbNRsiAUwGDOuPcFbNLD9pYa1hsiQWZHbxMvWnU8rWlGSRI5z3R3EBZaBumZKnil9LyMKKyCIErA0i8p5eEN2dD20v4a7YXH66ooSmx_W3O1ckRn6sxKXcsaAbJHRniFaYqDt238U99J0ETXJdjxA0aRlk1WSqYUk5OPJEbrw-D6kOuGOMZwpwUv0P9WXtvVC8wudx_i80zjAAnub4ktjus" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sQ9sY4qc61lrs5q8J47M0-0SCUTtJfyQoNRHSqMvWdRhA_g82qi1qzYeeqk_YClEIsgT32h7EgZs5ymrntUslhSa72cboXncm4_us1MndqE6RLpGj4lu9dNacPcAC4t7_i9Vwr1jzhQg4o_bHElEnxBPFaYoRc_sKjkEwiokgenwaCNBETISWlmZRbx1nSsaMxzte1lBlW6SZ1YTrt1aeDyo4343HHpgnxi3FjzU1NPBRdGGVncJSfEpw1Ei5gOUz-aIrWLDv6Umr32FC9YXGiCRLCCY0Mp653Ap_-HYeV4yYlji9oB6kSmT1oYD616749Jc0jCvl8ED64gT86PnwB1lqjH2ei2UZIV9d7GPisKzdZ_P802L717fRRBYY3oXdKMtAR1z7Zr_pENMFwHZWF1bJyGLUGn21YktxeNmJys-Y2oZwuyP6dnK058GVD1b0FyeYjhIrN0_gsuuCLvBlbNRsiAUwGDOuPcFbNLD9pYa1hsiQWZHbxMvWnU8rWlGSRI5z3R3EBZaBumZKnil9LyMKKyCIErA0i8p5eEN2dD20v4a7YXH66ooSmx_W3O1ckRn6sxKXcsaAbJHRniFaYqDt238U99J0ETXJdjxA0aRlk1WSqYUk5OPJEbrw-D6kOuGOMZwpwUv0P9WXtvVC8wudx_i80zjAAnub4ktjus" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm8Bx_UKqVePY64MGIdB_BD1bqmdrM0IjmJZnzgo4rAorQ10AtOfoFfK6mYp_1h4qkGjbztgO8VGVn_KsoarM00OaUTDXaXqvkPscRN1kuEK8BqB4htxdJyLd8c0dZPrWXVGof1LbK6tfg5AppHNB-Km8ubNP-9lsL39cRE80k-yA1R0sRdnKf7pSE6CaLrXcdW6ULx381HqNilFBeM6rkrE7mgmen_2mQ_ISBixezbQqeIkpw0uCSj6dHRK0oPnOceXTOGoCsE9QB-QdL5hNSzbH7reXlIFrWShdRV0ok52CLUxMMvgxHuytL0jnLBz8Z_h3mmy6sqObF3YyJU5tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlLJMLWkJEynY4wDsFDmLB18YG1GuMD1zoEns2G0LsPmF8AsWpwv_v1U_mjj0hjouFN60zBWuFP0pK4deIIrdgtja5WLIn9PW8ycQAgtv2FXyd1L32dgB4_xGzK9ESO9mH-LbpFSophsvcfrXHYLmQBCv5s6viFD2gBkHg9pMfBpKHHRJzJKWSI2BNliQ3kW1-CcBs-62KmJuqkJuaxrGYA_ldc8BLcD-RYSoTU-zbghtUFwnjLcd8P1bw6LcbnvgZ3Y8SqzE0tCWy1OiatxvoQbjhdDi_54ZsW1vDqoR8CHPcxKXRNdcKGVW5zrfFUngLJy-MzO764GK7F6rBjedQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5DPAwH5ArBheQYEGTv1aYi5xjEVP0Z0SpHPSrPUmROnNcjGv_GcZzSiyB7psepwNaxzfgDL1KiW7hwa66ciUY3QU3-Sf9n8xJU11YRxvkAGZkk97i93XZWagLBGoGRwZQRkk5LmPxBpsexrJszsyxmsB5T5W5V73l1BWtQWOpxN1QywLcy7vw_1IcD-9_jZk4qEz77yGIdyrin2muhHHjIm2nEKD1kQSQtOycTJm5IudJ5OTpe9TN0WC050o29Dl8pC8xqB59Fj7K3dMem5CQ6Y9Dp1UIjjo_E0yyO--OdqBii927-Gp4tmw7lY5sQugdPH6c8lXEUHhuCyNY-Zpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_fhabv4GuRNdGnE6pKxQCodsFArlI7TIu05vcUZrGFx259X-1-9FeFK8U6G2aonjvA1F8GGbg-kM3pX36kFK0e2laTuW5tgCjG7JUeaYvaIRK6yOKk2_8fGW8QV1wKHcYO9NuNs0UW4pfqZzexmoZ-_y9e8skEpV2PpCoeGe_QW4B89FmPHG4kApbu1q2BKLFSMKNwDyLExGUsG93Hp-1Oq6_IT-F-PqKIDghpUYT12crslmoBnBvMSaz9-AGq8hmLJ7yLqJSFvwmWgK8dpiv7BOQMuaxxP6nVZG6zEVoxblk37umrB1NuQGP2kNultGjCtGfPOlwzkdCKTj-A9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOsy0IxjJESwB8cI2RLvczBCRapIbiT_lYpuRjoYK1IlIyw8dWmwBtw51DkCmZriZQk3EISXt4zorat4z9ljA9gop44rI80AqHe12PcnWyGlJhYO8Hyc8KXf7e_o1IMRtFkidKk5aqY8S0HnWrpztOEYgPSD6MYhM0L9twwzv_mx88wMENsZU9ZmkGbDLmxkCwXkjIhwkbG8cgjnecw6FKs9hFL2xdB7GkPfBm7fnDhI1XNjIn4l3Aj9oxMkMhD6dfzaI4bMrklts20kMiQ5ST-cHZOf9OTZoHucN6l2kwOcFoU6guM43lIwCtWerr1QK8mwJ2xWtlYy-Fw66-eEZQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QhgbZ8RrxCO1sc9KBDcLzrVLErKZQkZoFqt0go8xA2sXhJcqPqN1fg_ezcpOMSZfiMValp9VjdTpKvfFcWGfmYhVIlPoVTAkiBlv2caqWWFFewrBHeYLocXhMuz9968SSoORpLvzpwj_fXoNZq9G3N4A6UG7s53Hmi9xsv9XKyW-QyFZ-wv0Hy3EsdRiMaMmpJZ2vOUA3_6nM1tzy3UzsZeSPCBRtL2WHTKBB2r1NK4NdszLdcuK1qfkzxIAEJLM8KhcUk1LCkYey-kl7JiIDqx6Ru7TAVAPB10SBOhq_-HSeDk2kgVRdvADYV1mUC8ZoF4hmxOfF9mPBZMIf3jSGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0QhgbZ8RrxCO1sc9KBDcLzrVLErKZQkZoFqt0go8xA2sXhJcqPqN1fg_ezcpOMSZfiMValp9VjdTpKvfFcWGfmYhVIlPoVTAkiBlv2caqWWFFewrBHeYLocXhMuz9968SSoORpLvzpwj_fXoNZq9G3N4A6UG7s53Hmi9xsv9XKyW-QyFZ-wv0Hy3EsdRiMaMmpJZ2vOUA3_6nM1tzy3UzsZeSPCBRtL2WHTKBB2r1NK4NdszLdcuK1qfkzxIAEJLM8KhcUk1LCkYey-kl7JiIDqx6Ru7TAVAPB10SBOhq_-HSeDk2kgVRdvADYV1mUC8ZoF4hmxOfF9mPBZMIf3jSGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7L-5J0ItT5OL7475wb8LxFhnkjEh25VGtRWZ2rxiWl2yol2C8GdaUgVW0JFNzSnRIzaQc3idd6awKNgKBKW7TZbeQZ5-dC3Q2TM23Cw1U3kYgCQ19FCX7KIHfshdaSUCUNo9wP3j8qDm4ipl2uFJDH_9twA8XQEARje4B559AxHXYXXK6cTueLZsMJzOYY-AwqgmRbQEJkgajPpUIacNxhk6kWS4uvgxG50MKQ4pG7WqokEbPfeycXca3bUK9prW-DWN_Ztvr7suiiHs93QS-gjh5tD_Z7uiOlj1t6WkducEwq3DxVSGjVx1HDmjNhU4nQLQUZwEwmg48MIm56tIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-SgD4Tzg4gZxIquvOsmuZVte2Vohl7V5Ps3dNFuYSA_JR0pNgbHa0OEg_nUAHNUaYPGHkl-XwszxV6YHEIYXc3I4DVonrwgEGmCfwls7MkbFEa4FkpcZQbr1JqRZFpWA8lXOTFAqot2o2B0m8XaO8Sr3KB4bh2fLBViR9a49tY397_wgkNs7ccr-ZUuhhzmixvJXFid7wfDK_4XZ2q18hvj9dR6YCJoDScFEaJI4Sd2-EiY8IxC3kNoHYeOJvbH7bD0wl1Kv1N0A1lfCjpPOQYnPJzKrj6zhqdm6KQ3WxuhoKD5cTc-Usy6w3xVnsvGew8gcY_HnIvNiXBqvSzL0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ3WUW-zTB50jvCQGoH1wHYubN0tyhYEmnGK0TPWO_P1Jh5lOXM835mLiLnUSecLSsagVMeug6_wIwxtRCdS029QwGrjV7qRoas3fqilD_riBcaANewEB7zL7tNCjGVC_D-d5kMJmXywI7MNwC45aNQhw0iWXfZtrJSN6ixJwLc4-Zj5KCATtzFSC5tOLAoir9otZND-hcFrj7Oht4nlragKgst_eSRmX1l01hhA2xZUqCrtK75F_Qt9jP5TP8meBQPjtK_S9A_cVm5hvjvwbZ_Yp58LXKbIi-EYNuycE_TQneCAIEu7Oboc9ZcQsZBBYbuht2nC-_4nGLBTizTZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAVtWI-5Xv2Japh8PD1kSaeLHwJy4x4jeJ7hClNEfTeaJba6LcSnpg4GxsaBkyIn0Y8QOkkkVGUrckUneIr3t9eHh_DzMYBu0vyS8wkZWVVYryJiLltTdWvBaSwjBU5z3mVIEfMw_tuULCsNLwOQNT9C8HDFq6CbH9Er3wImMzIj7K9VNQjdQVxPMX7vkKIPdSN01Hs4S_n6ctSZoQdHXRXizXVHPoKfgQCGKEYAi8Inox-mLwKbY9oMERGP_GOo2BVt98K_52sHqc5D5gT-uluywbk8UUoRSGuH32Il-LucYiJxCcJVT2McT7JdLp-hRAj9aEEFRpOLoC0l0DLoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfEZYVPFpf1KnNcTlcXsYDJY7OZ1mS5T7AnbOc0GaX2ghc_pg3eFl-24eKU2Mpt26Ov5j5RmtY4sbqSwGYyBj8yjSYk6Zv8AB_dj_Hw5qJmpq6H7n1wskk1Wg0bQyyUjAcdYgIaWa7fBzd0KhYdz2jzXAWo2_ptUwc8N2wNbAlDRJGfrKTgKI7Yk2bWFu9-Y--7lI5Lwl0AzkwREAMDDsnd6cjLfoPAbLH0HUMW27UhOo9tKsvVvDi5CBEyKSTUc8YkeXsFIWmW_0RWd_IcbIenC_YhNrQ9cuhT4vmwnHdI0Iwy7CRQXPMhtgD8dCj6VCFHyHmU4lSqwi98XYt7YZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPeCbq2dj-5tnDmAK40yt4PlkcUeqMIVXyiw_Jm2eVYNkIVgjKb2asEr7lUVcU7lSAychnqSZ8dLpZ52_UTysZPLrtc79bBoyHKyrk8DwrtId6D1Hy48Oquk_EQdRMug6Oj24maF3fBRXmQZrRNkknJ-ptwE0VJnivYofKKwaQ3zM6_EKovyeSYmkYsyEHYVtE9bMF056rnc1yHV3u5mQAetWL1EZd9nKzFbq7erhJKf25Nt2_N74jUvD5DfOAcxMv6aNQyui1kfkO8Fk28TKrql33OwLHyIYqkibkBlX8KXJyc7aUBt1JkcVvtBHHzON_IDgu23nSHuN09ei606qA.jpg" alt="photo" loading="lazy"/></div>
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
