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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 23:22:49</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 158 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 370 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 474 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byl9m6IAhbDFVpW3skiBpPV8NZ6QIE6sWQaE0uEnOO948IwB7UPT6yXcEOfUt1rR3ufRU4UELkcxklPgppY8-ODR-6H1kA404kQ_ACSmbdwdN74D2_Sd2gwTGVxsKCBdFp3qcLT8ax_pYAckQ8vV3mcrKR_2Mng0RCoDxJp-X6tNaoL21m_VxGUO1N3Dp8PXzftuEEcLCHniu95PtfILqqrAlbQg8T8gc-GuX8Eo-WQEA7rKFEOlmExbWoLz7LVeXJlWUOUBt305XsuqVxA0MrOK5DcKrv5FnZ6aIj0I0R_GDcFtjTv3jUU5fJzl_ZajdA36ja39wWCOSZgY31NdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 541 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1GNf5f8nH-Flp-s0W-xzPcWFGYolIE-_d-7NNIvXeI3DLvCVe2FSM531IDVVt33cDAtwm3qsYeuOnTDKdlNvHsMFnk6uPcFNOLEIzE_DjhFotQrZvLUopDwt3qK3Ms9_f-HeW-eU8f60-5J8B0Ev6q_cLnAV6vQeHQeZNdfeVFzK2kzgZ2Ihq-rAhA6ZBbZ-ImOiyTuuYcP1Ha8xe1DKR289nabNo3TbeUaFMBr4XpJamfcaXeiN2azfvjaPQjxx1qut_0LMh9UZW_PEe7xqVZ12BUzkZxIh0UXGjXsFEd8rHQ1zKmr4yeqa3oV7sC2xokiegjU0W9c8BukW0Wy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 848 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgwyuneDj9GAI5YA_9hRVSKzvMZriezVWViYw-mApRFE_qQieQ-0QG0j_ws7IXob6gMdwSWm3iJkbkGn7GGTTq6HjNvJbfdOTZIVexgWUZKZ04Yz0DGMmfH6SDFoYPZN-ygd3vd6K-yySGj-rudpW7-pJVElVU7WMcKFEYO952Np1NmYTs3PXsF7tTLKqLl8FFYwyrWAp_lOqWctrvEw9IFkIOQxPwUbuAOjtjxUt8hz1JMdrGZofa16raZSxS8BtBatFzgk9xhgMWYNLLU5uW_tOpsPeIvJLiGDNq1B8JUh7Z7oHnGk-XYdHuWf_4dWju4m6DrxRQQ4y16KsVCBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbDpYM2Q2sEKXrUcivIDCaIeqW40ALstbrY3v9W-2lPkU8Kj1OTHEO0WQliyBPSmK00Cy9DRG9-hd7XfGE9jsKSRtuuQA0vyj2qbNjqy0ijzd7rgOUZAJo9SEnkIoCx6pm8jXzB_dUhKmXA5X5E0ykKN0Sm5kh509JvCUVgYa99bYS8YxlvdbvAHJpIMQ7-MgSLmQROofpDnYfZDcUi6SkGXwbPnXq2fVWa6lOu_u_LuBmLU1dh0OSyrh4xdr7ddvrM3rs0CeTTx9_1VzfCF9fd1nzuxs3ESgUcHqfCM1HtQHVW1dmzBb6PTylAibalyDwmpz6BcdQja5uaBAdFn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 845 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 765 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 987 · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SakPz9dsx5CwRtUrSBq-JVg7q5Ov5L9F-UeWqTa19POUY5IctAP2a9365Y1OpXA1uV-qbhvCqD95A34pGQT2-UjoP9SoowmoyhoJv_rVqKYkkZI6SvPsNuvVr-EofDCVbuvdU75oZGwzLkSdGOxQGU5OhnCe8C1kka2iMmvggzz0KkZsJep2vmytpPAS3ds_rjuztte79ZEIoelyEFpCYArGGNEuyOSY_V5UKafP-viP1I5ZmC4GYnkdiH5FaQ7LfybWXwek-jPmfvMT55V0w86fP9bcAUu6Irq-MR-OlhkjZsXas9Bp_PuIW7s2JcyfOupgveXWlihZdMNPZ57jAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFx9axArozX9kDmLfYUIczksX9VCSmbvDBD8AfUI0YF-0s9V9pa3-olMAd6n66euvNXpelbFNchW3tBX2JwiwhMCbJMiEEe7pevbYF95p9ardx_36utqhDzODXXsE9poFnt6C3YTqwYOmSgjDubXb9XDlnWR38j8C0NO_ZsLBESbW3xXDh-5zY92gASBdJpLGVtWLdDrvAf3zbp0wNN_xpcJD6UIYQPAxDaNdkYfvIe5aYWcKec2XrkwoC4FOEvMqNLxki6bya45EOOd7hJGb8LmmIoB2v9CZu4s9WuMpTvmnMUFbbvCuiqKo1-2pAEsq8aGaKQAdr3y7xONx1Ax2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btX8LxsYKRHrXrKe-zlBqgxy6an6hnVLKFiyA3_gw-W9Ef3rya1MHBENxTBBf-ZfAli1_hgw4JOxzUfnSxlSiiuY6isa5sQtgk-PneMFz1ipP13folgcfXv8V_82Cnj2R9qEvzfnGOnlYPdUJWmqt15NR_Ahfym8l-30JxNJYLZXLX1fGNTpwq87kDh5fu7RrM5Ips7Nkiuf2aMasO63cQ3pygB7vaaJI6MwZYy3cek3wqiawuBJalG1lcYYgRjvmw4OyE_b09NbUdutEVZEslP9vNfQpNKSCehI9A_kf-FK7D4WzfFoIuWzqZUGe95WXUkdyY8xFqMAgj4nUGjCwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dovy-f1ND5vi3MZ_KUnqczYv-h73m5-07L7jF5ddqxi8N5XIxZtPMTr2imaBT-gepjTrsuAO99k4WxsKyumtWPkdEkYotcUlT4JCaLjpQbsxKnV9Skftl2hcyuCnjip-otGudF90_Clu48FC-b80qEJobKItlnf8msbwqdMncw_h2BTW53h-Hb0oRrIKNjr7w4BISzmOlOAvGT7-kNXKDRCw_aoi61eiE0x2hpC76rgSPGvMzmadlpMI6kmGjgEXuIzHBLl1_l6JdraFVmMM6E0CfUlqjHrI5mUQu_RbqqoY0wL8i6M8j9tI3tqDXu1F20uFNMPuM2tuZHtOiJzS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 935 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 811 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVGkrAoN6HvGBHC2g3zKnDmK8xVG9h1nx_R9kf-TDzRfgUiqKgNMK_QCeACG3FKRGOmvubrRzze1QZozrOh68H4HUAWhyGTC683WbONOHbDZ6A9gcvGuUC56ZMXmGSjwJ94V3ulf51rFe69mrQqXf6ecM1bcYaV9A7DzcH0O3N70N3mdH-_HwVvR9sMva_USM8bxgHnQ0s1P3h6R0vmE7vP5GV0zD6LAFAl6j0hOHrkCCRZSj4ZLuDvW6pqMxpahYoIHsY_pWGapGZJhiCjzOGPzLhTa4amRMLSLxNc0ToK0LPdlqcOYON9Pzja3IlqiVI9RYr2QO5Rf78anBL3n-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 807 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAvflAVlEEPenNwZhHimVTjsVkrZ6CkeZPUZ7MhSW_lameNTUl-yfyngrEhbwsvQlTMfrx24sOqEX557Mgbs8Wt7yIwE2bFkJH-ye5hxd_1heKSPyuzVmh-HAgaSVJM-k6_0y5_Ut4W5fh1ldcQBMQ6_VaZjguqxdlq2NK5HjKtVZ1K_aTQPzo0RtGPE9vgaaKqFCT8tKwDKqTcIuY7wpZDvwfbASJnm_xr0pK83Tb46371WA2PxBlydfB08csri2Y5rurNfs5jCE_y6DhB2Tw7jOoBq5wfgAux-ywMD0CKvS1CVGwQCiZOOcBw2Ww9IeHvFnZ2iRuxy-XFuahSPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdwuztM8i77XYVezdSqYybR41TZjAnZfLq1Idq7z6UqUkp6Uo5bMY9SHX1CebVj8dPGEv00aIJMufZeO66gQNzmIrcNmXGKsm9t80GFroerMWVQVTcv74XQYyp5eKI0uc67miUSh4Mt9qto9WHgsoOjwioerPuJ1Pyv-xiOAz6PBFxZhCHqupJfnX71XCK35F3mFXkFXt06Gl_xt7dLUBDubRkb1913zw_BO228-5pfWBDI1QsvV-SvAWrHdBKF2s3A7o0vIgLf2CNFKryHl-46_LnaKw9pnIekc-rl3S1thINOAP8pvvHK9iuNYI_R-noDen_ejAqhIplVnJMGxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Clov6Ox9oZbR_glNSEPWMaWsttYZz_iSKyZwjWZWnlDg1CZQMr839MR-jeVrsNmGJHf7ia24ZWExauaXjtptCz1fZGRX04SOkgMv7HNu2ohZ2i-w-Fwt0_gmiyOf4rl2m4MC8WQ75D1H65ZbLCyIaM4EIcJOSH-cNIm6EengabdZ_WkZPyK8Tw0qTWefd4W0t7l8l8j46NGoQN72baAjLVNkC5y4cGL9fkQHLiOZx7MDq6csvO4LFVmwR66hE2pcCtWpLx8-F8XwOPciHtj9dO8cPixe6wSsM9YbUh36DIbF4gyUFXjIO_xn829Bz-jgm9cTV58q3KI9tomO8K8Trg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIgnSy3T2G5pNhWsxjZp7wx-X4cJgGFas0uNEK6roIzk7eC5GN-RSAZwQVOl4Nf_xd6OVjD7vx0OFQe4cdiLo4xywB7aGzLPLFpeW9GC7OHfYLVnNNi-RsZFmMuaZxovUGvWOn-rPswkSEqg85FICTxbQ9kjULKbSpLLvV2g5mlDumSwZTLA66BHm2hYPjk3sFYLMKt2AM8x8u4HFUycHsBhj_674GJE4Us_uFILv9JDWhk3j3BGo61_UNzU1Mk-rBGWUGhJrlYQEAsQV4TdhaPTprZuF3usakTG4uUeT0whqbTilYGlahNE35xc7AEHtloZ8aWuxpW4K_NvN23Ngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1rZW6HfIDhUCkdoat8wzm3J5Jjk6mj5mJpGRa8EcDgJQLJCnxwEfCXf2B2U_ned4Bxhj9QjaPUq0h-9Fn7Pf8WAWDFJdcKAFXLOrlSp64EZvnJvsmr2HvK9jlleO0-2KzpI0idvQBDSBzPktBkpkq4U3RHxUVjG5hZcN6T7QBjmTzp5MTTzs-Bre17gu7_34adui27LWHODAWfb9IvG-9WPvfuO4mkSmurl7MC_tOaYa2VAH3AJ9Bl5NcvqWo13cKTtfd9s0q7gMfsjCQnNirbXMetT00GhuTlK4OayccBOEn_JPqRmFSHkOjHtEp-ntzhVKxrFEf4cqWH3a-dRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OV30GP7RiSjC6VZtM8_MvRZgjp_Vk4isml0juPzV4X9-4tmuFOs3hGEDavE0-jWFQ6oP6irAOvSJjTV6-0mnTEZ_shQouwqWnwPBsD1vgY-6tc9Sg-O2_TK3YhrA4X7t7-Ju0i_dZ0j-1wqP7gFsIzeHzJrYVsu7kKYCEu5ezhzpVHLRxN3wogdQrEJF1JsX1tok_kIEYk1zJVWi12OmxL89yAjaN6RuD7V91OD0l7H61DfgexMic0rGBsoEDIjSZpPCQxy506xccDpBdBarYClF20KeDCLH9PG4pfUq7VVQkLlbkvGjc-MnjcI1HARLO5TNpGiIYXTKlR9M0f-arw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HImI9yIbS9hEYucheUmWoRckmtuWBtoYoBBf8q9WTZj5RptsWG1GePYp1VYU_PTniGXMX6ztHt62cBhm1etRyvHSHYhEIhMKwpcXxkvDgx5swUl-xA7k87_kCRYptAWqbTf9Q7xBJg7iBQA1XIkehQR0YB8SnsB2kPaXdiuJ6Oebj9h6QBxJvr1Awj0yxuFI6tP4zddVC-lZPjZa5_FaKMnkIf8AelxQ6ejbHll8hzlAtWiUcMRaLLrytPdS8aYdK6UMRcHhyxvGPsbTZpdniAKouU7cpXet-drlevc-g241KAkskSPlt3-qEQE8_40OIdXFV4PDJ7pQ3GJXGGmdXg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=bs0TKfNvqpKQ19KjFyDrmgeBlAZxrB10LmNqKtOVB6T9F_V0yxi3QgBrtZbuL-7mLJBm0QjpcjLxjKp0k8OY2xCBk753SgGM-n3BaP16FddYjRM-EFMG3MDAWx-yy9Uo43UvwdOacxHWVbekCU_sslmz_oPDQpcGkYHNNNpBKAOzNu6o8gIqCHlpr2ZSMZb7bOG8DhwaDXyYelzLAfemMvcmJf94Gqx4ZuiHFin_ji7R28GdG8h72qyBJTcq3AE00HBHtHAlOWsHzJsIJinT2Qb2LxUho54LqcKbdG2OabJPZjdDcus0PT9GvPAINHS4MlVVsrcJxHPMyxx0f4Tjkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=bs0TKfNvqpKQ19KjFyDrmgeBlAZxrB10LmNqKtOVB6T9F_V0yxi3QgBrtZbuL-7mLJBm0QjpcjLxjKp0k8OY2xCBk753SgGM-n3BaP16FddYjRM-EFMG3MDAWx-yy9Uo43UvwdOacxHWVbekCU_sslmz_oPDQpcGkYHNNNpBKAOzNu6o8gIqCHlpr2ZSMZb7bOG8DhwaDXyYelzLAfemMvcmJf94Gqx4ZuiHFin_ji7R28GdG8h72qyBJTcq3AE00HBHtHAlOWsHzJsIJinT2Qb2LxUho54LqcKbdG2OabJPZjdDcus0PT9GvPAINHS4MlVVsrcJxHPMyxx0f4Tjkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6PVvKcKMGnQt0VWucvWVILgSZI_YWLiv8yN6nBltRM5JgqzWUe25klqAehG92XF3zZQWqsu6myiS2FOx1R-_pmYJWxND2TiLg1bl68qjrv0Uom1tXmPGXA73olm-ESOz3EVYDdhlbrehrFn1HBorpbzX8Ddt3xxxOG1rqXXSMjwkkKCVU2nZ9c_AOtJQzND1NDdeIQP1I3WoJ81m9TeC3PF8lf2-z1QllZSoVWetwbK78FR8VZpF0sCwJ79kOgcpBKbsgpEUYvpyCpf_frNpI31QQr_tJ1R7m5WB-qsKF716mffuagu98aPcAVm3kekDdL_diEhiVk5x6e0qdIwFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R03CQw86FXaxfYWan9JjmLDktNL3j9C2OiVqRkWRDj9DILet0RdMCO5JSRKvE9QzPrPC_yjbIcaexOAz-nVRCd3MiSg2hOrQw6JmOQ7W1Nrzk4eoD1KdWcP2yYuMkCuhEXjLN5ydcOFb60r2mLcbkTotQqql8G1rWU4PLgNe8JTwckVFK-YUva3Tj2EqCJ_WVzMol8Vp3atCDSnSS1xwOQDVmd9pECb6T8RwvfXtUOgP12m-t-Dc2Wqo-sGp703IRLsaLdZ8hAJnLHcgYPC4a4AH1LdfCFGI1zDTlpH2Ly7NwzOjNjn-N8s1oMWy8E7ME0QiBGNtHaBPz5HDZTKmdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W3ZHjjo2vKc3u9PwvwfxlUuc9mPw13BpXrYuZa0bMry-4NzIZHYJOhWhqArZEdozzfrNCerv0Iv5Pg3j7c-B6ppE0afTEa87MY6SiQXdGM8OnuvTZ5C3VtNJ2XlDmY7dXpC3dFXxrYtEVF8HWQCol2XhQODx3Kai2ZmPu83Luk-8qbezv2A-BacU4sPsOmQPQxN8VcoPDijLerfiojj4cyjWFxjqV2AzjEQCUgQ6_Xh57WvDyedu2mIgNg449b639-UqLKfRrqNf12LYJr31FLFkNqFOomE_haWG8CDmt4-FLPo-smGB_z-awVl3YdoakN_tDnctZpAZ3wcxAyIj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk6gg2b0Ub_QlNK1SKfZWMVS4uRy9ZVfIbgCMNS9orLtnO5jZC2rslHwVIMti7iTIx1jKRFc-L_AlJfSXoThFOpARuq-vOuk6qjLu8q1dIojA0xBVhLW2CXpBRZ63cCxJL_GZdYsLC7GXMukUYFsjAvXBZ4mY_8YwhDKlhxNjAZ9-SgJMNKSIQewGs_rS1Kq0bdimRpM-oJekuovcihc_m9SQ3IULRXNUbeM7dHZFpGo7wTbPkCHR1eeKhPQ5Yeo1ymYsM8axjpgHOsBHJS-UtcyPvqn-rsXgf8yQkvWocYruDNzLQBonFTR-aCEikteZkP7zXQEhqQkdiIH_A2XlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtSRBrGZabir-yVm1Vdq4k7DnoMtMYg6RDQXW8LXtWRflp6H2oetpyOat3L0dDfFOoWUlAXrbIqKO00HT6iy0ywjJ9aP2nBNN5m_y5P3iqXSmUZTrsY0O0zjiGtmO0hOKUMDS3IgAEFhtv9oq8rf2_rkVPAsUA5CESR0QQyve4odD8zx-iKeuf1DAicZXSkkh3VMiqZKPYFA_u7_-_F44tURBZvoFIR5XweHjU7n0BycDtoZ_DcNE_DHPFOkzNg48hfSVmCCNhztv1MRhdbRW-jbu668Rnf0kNL5tUMy11SBd0Vcft1aTKa2lc-kCbUv5C61NcKprA5NXGpQLzfV4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIb6gBynppFSyUBrf7mF6kqCVKFomQdhtmr7FMwjESrKLWZrhsKD5LExH0I7ChJN1uimcR8NwFmkqqCGcQHTf5z73jko9Kmw5I-O_0hw798AyqCcmXKXNx8uBmwSeiEZ30rSue9megMUhh7vv_lMRb5LDw3zD2Hd0hGJC8Juuc3sMQpdAN0EEXdgXj0oIf_zMz2jZt6EOaMbgltQ2DNDgSjc9Xi6jcXtVDGi2gcybWKVmwq49ZXbwnBDm6wFQC2Piqs--XfvLo9cRw8WkRwAZ2gnBdZwEsTnigVyirTWG4GqxQHf4VRMPYnBUu6hFkXfKNuBFLCrrqdvxrQyf8AszQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4OFpXYBBCIcv6TJa_ke8Mf71gfllQ2RPc65ZLCqD1DNIl4cha041Ifjmx1qxsQO_HVD2wBcIbZV-KZ5d4u4w4Xa0wFjEG1glZDxSDci4qswU0FTiqnbV_y8jrmTun0mogvFodiKiJp5zsxxzpKu8v6aAo5DcJE-58Y7VSmMgGGS53pDM_O4Ao7do9acNrKtHul9VKLfcui7lnsYrkGttg0NboI8BEyUSGnY3awXii2i3bxUTjd8cJSeneVWZw7Y0iSnXznRCZ1j-HPtj-zBgou9a-DvKwfR98mWRTOjEOZhP_SkkdZMle9GLzoEPC2VXeazdsWLC8z4Iw1NMIOYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqzWne9mEDOKVvUOK6d9-gk3JiL9uzbqBrpxNMT7V4RSrBE2YCOoyaFTmFdBU9rfFLWegsjhDwFWX4OCQw904d6D1RQxs5O16ondwSnos_PXbdw7mx8mBb_2YiVyPJCw9cJ8YnBL1sxPHXcCbG3n8QoTAXz10DPeLS6y4kRziOGfnJ2PvHspu08FNu0jbruTRoTQb4F3cck2zSwpECkxVkdPhkaIuWPI2FsqZjNYEJN5KXivze4NfBb5rmKSbWrR9Dgp6k8O3yfaBil6tsBD7ECZpJK6YuLu15rvkfyyeAskN4gy_YYeGFqmj4Qiorp3yLaIMudkzpekKEwr2d21wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT16j_sypw6wK7xrPywuu5h20MUoiSmSFpjWF3LHJLasGkZcFCTiEjBWaQNy2gcvpZCZd59zgbV2kyM-nw5Fc-706P2J3Dxvdv5mXp2f4VgCLIAEhEHX2EIk7n64Eicbpl-mpbfOGbJ3KpcpdM0JT5ryE51k1HITflgenCqAz5zHTxToHUF6bHuqFSmKDq-4Vsqjm8VpLN2xZxV23L0-rNzCCal0T1bywPPgWOi8ZA8LsgXMaepGjbHRPDaP3Vj2rHTPiNe5QZVebh-pcmQAzzpfEkSYKtbUffcHnYoBJPLQMoeKZnignqO8_K5ysOJD2eso9bquvy-U2X0NMwyR1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngYaG7RvWJZbhO9qyV-7nlrI1DLDVhmj21tX0HliJYroQjG6bdMNnKsRch_KCZRfR3PxXj3-xt28Qb9Acse2HAkAm8XZoJMrZGwr0Cro3U-syTEiY_pC1JhFrML_KYyx8tusn13ciCCTNkWzfs837c7kfAsWuHbKaud_7XrV1nrm8lE4pmqEZzxY9jUPZe218S8-RtRpdGCb9v3OBaT8oWOFqFYCkaiGZxQ-5a1R59ny2VoxiHGlgDymzlpAM4lt3GLjjiXluDG35BqDHCZ8X8M3HhIabOGFsSBmYA-Ef9-138qP-xAODOvKj9bRonSssf8Mo5zwVpjUcR7FEkE5Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7EHOd7CE9Kjr5C73p350go2kX9bgBfyRQxDJa5Y_CI2L3Wc-Ii7mPwjaWQYbpbHRm2QLU4f8SlbkQmiGJezIf47382QxI88FIyTfgjrlehdprEeNowOOFhJC5oRw7lhmBDiEErp5EUZYt2txGBYlL4F3S1_gZopwoTQ9czf0bOmaCgbm80ct3uZKAlAA4QIH1m4OG5invnODEey7Lr3EFWUN7ctxlHONwv9r9V9c9iG4REhAZxavSMJM9s9N_ah9mCxBpfnDmKtIbK5ue8pVCIKnFUwMVhqX49PG15W6mCvHvQH2lhdmX2XP4ZJ2szn0HGsL77SDue2raeNi27gpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhz1Qeoi-dfk4PmAUM68_fZtTYdo_NC_eJeu0doRCH0Izc86j0B5ZYfX9UWX573u6S8MBzV04v1dSASg-PeeJHl6EJMsOmR0AYxHEt4sHMc2KkZbAV9c7UjGqPn4pkZlQ8Oo3KfnQrWbo1C-aUOVfL9YvKCjw1QlOiakWhD2drEkwP8ChrDopBg75f4GjSJvAwYOkAYdQHvWlRnn7SqITs0rIvENjzWIK5pMuHgVDWjeJmzkdm1l8OBhesGFzvg0M7wvZnR5-WEDvR2d-YDPTJra043C10sHKb8PjGw-j2n6w0uZl_wwm_gH5hRpQ82OalR-ZnP15UkMfet4UnyTIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h9vJdluK5xNQH-BsL9RrsnM40oiz-ycD2mgLwIAOPLluscoNhikbKrH6pMJJQJEL-TY4OribViUf8lZJseZhCRRdKgJ_xf4SLbr2r3t3ggclR7HdhHIAQqPierGdniCobf9hlwNBYqX9uVKo2XfPodfnEOYDoQH2MtEwCo0hyWb463Nt58Yb_pXyJ6w9bR4UESuz_9XzkFwEuUwoFJoiZQhbbJc7Kf3q_-09zZ4NMMShF9CWnYG0w6z5d_15wFtW4xZXlaVhniI_8W-0rKLkpp_KX12Btew5UwHBorTSxn2Xo8Y7iZCEBqhZZQEnw35eo5IuX3fD9owzEcYnp0wqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTc3gCm1uTt1S4n08lZY9oy9k0NYWROwc2nyugwPnjswhB88eJ2RP-JZYDC0Y0JmAOd0mnKIHZikK1nNFIBtQCVrwaqRvUGZyI4V3hdLgQExxosjH4WOrP9sSMzbJY4ZjNPAHr6H-1BrTdnVrkpPF9r5TGmwJAbRGYfPVa2eaPPIiViAkAzKxDzblzWQM_YslFK_zh5Lx9STs00QXbaTHcmp2FnkoLk_B5TP4aBKGrqprT2TS-vWuYvWyqq09iHzpSZAjOpeu6XrSPDQGq6BINXyzw9Ogd7rOYAlbNPPGvtWS68paX1wbbDjBkhtJERlJduPVTaiNp6-Tym5xZNFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6RPck_6cBT2HukFJw16uVtnqOCdQiBbkJV5sXoIKQMIRXMzbhBKhhkWloP2RWzeQWjmMNSgeAIrz8gx1Xwldvd-gMXlposoxgcq1JI_4xW_65rCJ5KIUX8hN2MqOUfVJqiAHyZLGM85NezCO-NzlafPTb2uyIfOCaM-w1lNSGxg2ULDP913NxKnubpV5wjYzt7Lm-jcM0c06V2E36uco13wO8jWR2rvRUzcf9DoICwb9xNW4Qs59dRCzJDP1wqs3Rz7I94tRACgpgcLUcHj0Ad20-IGqPn-3A8m9siWaX0_P6anE0AaCsJbTSb5T6ArwC85bDeR6Svecx67nlzHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqZw7P63jY3sKX2wes0cEiMTghPeoftKwh4-E6urt88UvgtvWOFNQD1r3Y0e_IXX6uEpUgiv2avcwC-H3sLWbrouzIen_tthRSfc733QVDVHZifHqsdLh480GMbJopAlIOlWbVAGI4pW8sfci1HEeIt5ZpEBzB7yhu52s7dWA30ZYx-_vwr0qZ8tlztEJhkUuUrMGGSgr5aVkyuqB66P7V2MZ4CRKlyqKVuO6NBsj0_JlSuxN-dBNl07Xs8YcHiOL5PDbo6i6dG2Zd5QAlTiC_jZufx4qxrwu-NDNwh7qBCmBlSTh-LON3AEEUqijLRLxyWYqMUPfj7PQrG1K0omdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEmR2hg61G2N1X5yoJEU-EEPuM_HS_n6q8_e5-qWenMuwGgY86z53uHUAOl4XqCCRQCigC8S3-PsANCo8K29gU_mMWVzdu5uOC16GESDKAypVrpbJNsPfLtRWBZpA2HPe-Z1H1gOjcZQJza3TDa4SEvyo-L4f436P1eEYsSkh1lKqAjLvTr5qSScNMH7ogetrOVjzbz_VN0HtNEmU_7c8B8p4mtF8DO5SO-gxbLDZ5ojtTVFk0FSH_8O9ED8o8YALYkM18ywQ2NhgeGcFMAoHSh4JhQAlh8sHLuyAMdsaAzyPHczcshSjtone0MDaHnSfBtoJALqGhEd68R8a00Y2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEnePe4MtzeDIg3YgHnDGpA9DCUo73HEdyKWKbIwprSgzgYa-UUUnONxFaObk_o8ZNHG3hjFFhMEIBYdTbah_qsXSy3RuPiZNOnnvetQb4rl215ZQIgvCQ0nwv6h8svPn7S2yEH8sCU8ieUSgtqAZbRpMIxji2yG9N1hWyilxoCLMRR2szPf5OmJrQLdZLVazQYuj5i5FQw7DNsF502l6JWRqwzSbXp3uMwxciIDFfV9zfIsQbmpd0nau0bS-enkLX4A4Wp4-eQVN5E0DSvROmTaDvdaVXXJkm_fnNmhJetdSD7Ai0-OmA2ZqApLJnb-Tw22Rxw6WK3k1heXznQFww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M78BO-V34F9A-4SEz93V8u__gsrRuWLr4HrGAyi-iLqgsTWjeGjCbLEFhIi037WcxYEzyNjQbNFot8O8C3VDl39uGXEp_RH_gYwR8LIOULwyPAheU49pqq6WuwIBl_BgnaBl-Z2tEU0_PhWFHRIN58pucuODOyVC2WChMRUfxmwvohpADgOYNXruAnZiUG6sPSyCN-3eWf4LachotWIFW1LI9zsEYKfTs67iyC7rs4vssFvPO1D5WYu-5DgO92xxHYkeE6kEiKaIwH2A41WzAVh67my0HcKJeoHrEhZ3aJy_l1aa3xP02HB3pBZ7jd2odoCxrVGRBS2g8Thf022sbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iavnKISrjBiDbJM6SdKh6Naki66MQtBJkAAWWAEJ5PfKxoF-_U7eqi93L4KqP7AN_JxlZJd5_zoJhVuW6AxLTd-Sl2BJisN26UND82_BkC7Cq94SPY7zh4fibmWtyrpOTQQJzvCPHc26Yb87eMLR0zklQsEMwEaD9420nwyZUvMSoyuLKZgoe8x3Od3bYmyirWiP4NSn6msZO1Moeo43EUWSN39uS10WUu5l0hdbxXjyKT2WIVT5yobRCVjwvilulelxA5Wj5Xs85z7-gjxHJPpaw0MKeFIgXXfabIw4n9ZHmXn2Arj-kXnNrN4QITNKdzCJnNNmTgPYJzhKzt9EZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEkecf0QJGvOn_ieukn0yyeVkrROnsIdGrDyRhzYXF2ZhNDmYobMcQcN2cum4vx6gxLpjKHbNHI6kjNzBOx-k2y33zSZLVAWeeVXJqL3P61aHWYdKxVHci_RV590dljSyxwtyzZp8JpWLNSMz7kElY_lh1lBKOXCJUlsWXDeaLN_3lWw2foALaTNiljBoI0aLa5ybeac3X_56qbuSk_8Byr8OD-xBOrtKerz2aqHrYYoAJAC-jrJbFmC9X-1KRIdcqBPXyYWlekOrFAOdRKU6ZWvnOSGbbiOcE9En9InXQ640zK9mVR5fgzS8vQ-ZnnC8iwJ8hd4m5DolFikS6-5mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVI9SsozgC9_wKSP57VC-jDDkN1K41ZYNW9S5COUCFuy2vsh62MLueUfETwmNXNiUrQJ-dZcoG3zFIyrPNAyEjPsVw8NzKbFC5AcKrzylqFZI4wjRZ17BJA3hBrwAmQfx8AXEoQ8D5WJiliRgs8c0zINLqhbrCS9U9IAx-OfWjBb7RjvYab_bSc-7WDxQROTDzFY263ri7EE6zRYq52b3RxsMRERrh_ijysqoyW9J9uArzbSP79D_JOYmVxF2unL4wiP88kR5Y0xHcjdX3OTJtFZq_IHvTQtQy-4nQ9xhforKbYlL_snrzeMpkK7bjQzGDEe9aDR-Vnc2aIt2kvsMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyEIn7Crh2I_N04xlBGXWllrBE7Dq5z9gVgw86fD8GoLaIXyEwS8Upqii1hB4A4C4smdbUt_ch1gxrZ-m-q9HVFKJLbPCEmZzMNKJUkmZ5xfJLqGaJJ0Le0iBG5Z4vITQ-RC-Sif28rbbTY9C221R6s1g-g-sCwMJzK9RTiC_UOWEyawTqL7oxIiINvLofQGyI3EEVF4Ar8dIPJK7MKVHRlMGG70j-2hFE4nREZx3ocFBvUGBB3nsjz_SAOV6o9CHsDU6wRBK5QVhgBmEGRCqoVys1kotQr9a7DqHWnIAGQEJVINrhuF_WBl7pojRrT5_whoSm58hZ6_Ut-Zmddc6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1XvzDRjSk0ZkXltwA7DKINbudUJBxLhnG-Qnv7YWQDPUsThx1_CmFfWT9yltj1J5r9TjXqIzoXxB1gmr62f8NrZafS8xMgDNVb8l7_eoSjj1KQwnyS9oWIfNf0vKwnfe5bXhO60-GfQsXeHO1M8j1AVxCQmOMBeDUFItlHnn8-rtBny0u6VPc0lRU9XqTCG9lXbOZcz_0QjEm4mwRH05kwmukwrdaSg01E9X3JdyAr6G-hzdUZZ-TJNa64TI8ljEQ4KFL8Up9Is7UXQ4QWphY255_-AZgrYJ6hcY7qQ9SqpELT3PHfxCFl9w9coeXZMvyB8ty51-QTCUQqY0-AFXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJGjxVe98g0CPHVn7JQLK81FbD4XCKQZ0eTecbtwzkc3LjmQBJt172yOqEpONsmaVBEIVbIRANSC8bv4Bkwu9L5uYuzrNZ8WAWEuxtYdpTXSq9WuoLWD9ZIVI5VRN1oSrSatP_SZFoY7b_08DS0Dz4AKJXuJHzsphdLnUJWTM2iUWemYNgSVCjP2gZYz3uh-zFvBNOl9Pm1gnbAIshJ_vDzg8XezSI4TAGpZ0Ho3lW9VruF4L5NXiYg5RliatzZZdM6gleQox4pnlgMCDIwfmI3sZzXjB4i-cc4gXVnO4ladIDS6xZkiw-kBfVBNp2tqbMVmoXdbbWQesO9vOCkMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjW0ciwHXlcnzf7vXGsIl8Q-QpDdt6EHh6yc09Zodsipqgmye8ATlVcfc992dAHd-KCO0-Zr07ZFMopWAG1oRPkCesosczM_oZyH_jpgfZxs6nuHOokO149QeRL5m5P62TdKm6FyO5CV-7VZC8zxtNhKMreR7LwgKGBrhQ_TSTTImnma1qoacOzVcNy6MC_pNKs5egL1gSyuesGwHCU5Za8O3t0N3fgB-uwBQXCs8Jn83sIBXAWFamQ4iCwOYd8oqKJPh4jKXkzm7eq9vj0r2-_T7eaAzi8zYdwgwBLuL0ddzziZcuTJYlz5fBqcBxgSozPt831fGYKBtfm9OpaaTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/it36_5zHqPT7gE0Gef4d2X2zHlCet0QrkwY8JWxTlp_YQo-R45tEDoVfbys24vX__WjycnGNdvYlBrLwJ2mNKY_OxfUQBPeoCWOWytBtto_K2BvduZybHttBSC9Rkcbje3q0qF1LjmBfxzWxrYO9gf2QwJaCz65HeEhcJ8pRnX0VQzcpVJubjBwxt7yIu4R_TTjaIV0BMDHLaDJKmDP9I0yLcNIkm5nY6UGRDxg--oSDtnCwWZmP8zz90wPUVjMu-Xd2_AwuuStqjQa6XnokywM1v3pkn1ECdXaG4byDElM1OBgDycb1a-rZrrA8pksh9gHIZIrnI63OolGkFiuNrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC2jp-SA8iT2V5iU6Vu7ED5XmT_ozecV6oF5811Ej7wi-jIQ-n7ENm4mQHEKsFzONDIA0FVbQMjZyKqv51DAnWEZlswS6FzCtG65iscdum6mTfBpvBgJ57g0naA-nvVUA1wfcpPgfafy3-q5g3qTU_nEjVLhmYrWhbZSumuzLem95ZLlwTXis28agG8EF-msunS_79oky0nAJ2zomdqWdpDKOrtJOl4vKnWjiLVhmmVqEwgpuwpmKyWHiWhwuMbVsIT9PYgxbOoAk84NghBx2aHIwu-LNMLzCvyv4Wajo1Yxs12ShcS2k2azSH8GxMYgT2FKvQKhUn7KNJsmch1b5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu5_aL3Lj4FTdtbtbePs99h0_EXhXga2P6fL_Jm0xC4dgNrie94hPxCPdw9BLieYVG4jn0YU2rSY8lpPJov1TdskuiV_RVYRJP2WK48TK1tIj6GAA_IA-QfVbNTEwQ1Ibhk3fa-9WaiQO8Fel-K7DJDIwY3iAUyWASe4gw-jOBLiOkusBwKlSgQ6d0FdJzcBQyv6cF9GLbP8Yi6DzFxlavO-FwSADd2rp637AZxxLEOoL83ZmKGps5QuO-P2fZHgsu-G8Irqp1d1StFc0DM_lhDKbAcVK0jGidLVTSLkbMwIDNo7CCWLDN7_dFAlZ8V6c5H_-cKO_b3PR6KZkWaQoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a05tRvd-479FXa8MEslgeXHgG7apXRkuK4OV1JHAUigoxHyaZL64QpnMicZIJ3nPaNtwSHML4wuphcFZpmKeUUUimxLPF4kn03yZPGLNa3QQ6nKN2mfyuDyWsY-Jsh2_hvmc_VkO7jv5FhorkfH8iKZPwF7xIJ6LDpYTGuDfh5h0aHIPIHwvx1OXp6xHKnJcVCeRTtyuAvPDHNBgew7GED97gbEnDWtFlTv66I-7hcgCxMAfdsZeKDu3aUfPtVV8RsgGyZrIYHUeYiXtcP5sttUJofXms6w3avxA18I5lelyCRCuji68zICbGc9sv4aOLZlisweuqsfLgZwhxziOWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8gzzTWQ4WlpLUrV2nMREjnWrjyW36_1XOb-9A5TGIGl3_-FZhTnhmT5GlNcwsBw7Y645mII_6csxjOpK_sDNP7KNmtNQcWwtiXTm6wojZxoFxqCOAFGxDM0VVscWsSwGynikARif-2l6eA5cPhxWvMZTuhLp9U5bDyL8CPRb-phYLocThW6lr9Q5VKOkjd88O7U_8vXnPrJxdGyCRMMj2C0H1_GoqqNwt-4pR2qmC6m_oQe7P2t0SJvXQ-D1s42NWnypuhUAOgeAMPvHRTvG8kr1El5KictvT42L6zE8EtkZFHkyYEd-NtgxpuvEvLUNeNdIYChgUTtm0ElQEZFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3r-UJ6_9y-awsQb7D79XgWEhXDdAvNDIUQs_dpneb3NXqY2Us08KJ8lOr8M3lBvdxPtNrczs2OcB6SbFoAKK1EAQGfk8xAs7TZwgzuM3Rdy7eMjRfuSFQwxHW1pHzXqGnFXTc1Sg-j26XO0l6TqGwjxgqrc7hueKC4ouNzsc8VXYum0588czKkPll7PFCTgwglPEYv0HDmFedKtcuZazA1-M1Ez4KjjyT12I25C571_U0mULfqKmAIIQNoIoDI_g5OGnFtWzmgZup-qm65NKBGHsxzXoL72GjemvrxRYh-uKS9aPDz6tG_vQcMhCI5yrA2Y6jwJK2Gd8xcm7J2n7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lflxho1NJBtb_mMTDudTp8Zbjyo_1Tg6IAc88qEtfDwtEatt9sVhrGSd3uw7OxUvaiZfAj4l-Dt_8oRM-QSOO4oRnK_AIO_YbvNewl5MX5tqM21yMgHa3s5wu2NsQGo9MQS5vSAf7JAbwH6bMqbmRt6wKzI1i79h_CQNKKlZAJyg4RH3jHTC7CngLd5gd3FTh4n0IZ3HWIMXs5sW_aLCIb-lW_dY7MFwL6AzDIIToEptma6w8KxN8bKA67pecRrhnJOqNNFfXFstWHkWeU7j03-iLJNkd10OMIiJdxQaJDtbPeGNhx7AIOxUrW0O-V9rEGijDQZBnzmyPpqADAZ9aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoWIbRxnNf4jFMQ1_fQayCCD-PCk2phTB2jUWGNUH7e3GYnni_L1RsPHEHAD9yylTMix2z73Pgj8szy-Uu87h1eEuBigcWv5daLEnZ5o3mDJngEOmBxt-22ak6pzhaS8KSTuWZTQCgHu4r0MGAcPNfSfIMBv7UQbAfvkJy_V-zIFYJCSyM20KOwCvOnV3SxyjLDXLkd0sIDe-3aOzg_0VVIzkFnZ3HCTZ8097qV9a1h1523K9qzx9C0aEh81aDUNA0jVIVn1fyI6qggJFNzgbHa8PTrmWSu8wo9uiBI6aOMZJJtfd2e7mYod20Gkj8CciUhkGgWWy8I7YMGZR55CNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfiebcvXc0FLO_PmdHzyaOhNkGz9Ow4mvhDO7eskdi6g0TTldxJHqjWROkYMsqiRhbWZmzHL0Yex1UOFxXsfzsf02dlRg6b3WqUxTZxNKnoG7IXjObXwTMLu148r4qscspEk97R7Cupct69sUu89eiOMJ9BtS7uLozeb4TZ4-MO34rQBOxLhINid0ayeX0tvJtpBBnYraxcPTfKJE2RoVAkBNeASy9gd7gn3jlYsKgbbYah-2rjDHfMR2XUhfALvcS-srCXAe1ePj8QjrSNvl8V0TlHCN6RheGS7RRSBE_BM_QGnz3XBSs_bZtY5lmSpQowK-zrzK_n8gy6pEEY23A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KMyoHx_bO2X_urKO4arFycFGQqb9E79alJBWPtdDGGBL-jrXVtKcMJpUTiRQ8tq5n0fQEUr_GFGOajasLsJ2VsfrHF_a-2AEFLdsgaTHyQhMBynOSJZVYSklkwTzf7C7JWNG0tbG3zHQRxR9Ni70dW-i_qLV1kBXzVnRVqkL5Lf77IjK6JJiSM1BQIpIBDJ4LnS5RUmwVqMaOdMC5gmEvqrwiKDpq9w6lrLMniS2d1St8Pxl6UTZ8quCd_glRMJ7ZUlZ3M3YeRSQkF0ifDuNv31mj4zOxCxkqtg1Y7m6QAMfG1llUVGj6sVDKLEakhQzA589uZ-PFWl9hEqL2HeZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBYdzeyUYcgwqDIwl_vd9IHW9G6cssgC9G4Wub8Pius-ZkRMR1I6pPBQzAZhv8nItqeiXOGpb6aYxLgceL2_7XgrQh-I2WZG4ogHxn5hopQN5dbYVI-W0gpJtgvzpFko8NarMn6ENEPXPsfbM7xo9K5NlDh2G9tY3w3oSbGDGnIaPVGQ9Bg-yQx8F41D9JgEckdhf0AH4sh5DqqdrxJXZO4HZ_WIAmY6MeAMea9atgFV6ytirHlUyYXXQkHiyUnHHII3yF5aQfvadhieNu5TlDq7OnnczOEEDIFU2Rw1xf-A7at4xeD5fnyqd69Ty1Nr0sN0opDHjOJiCfZgH4lq9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ni2eBDk44n-ZWAbEKE8ZWHnAKtmGmqnD_jYZKXeowmx6AbdkOMvDCKV4H7nbEhOXoIEdPPMA4pjPdFfcZu-Q_ZMj100BHL4hqKXxBRPKtyNai_plICaJKNZ7PNmQyGdDUCwvbde38A7TnVBhV_kDdSR4ZRtzsBeil_YCSpG-i7pk1EkBIo8NcnEnZj0WG8DCTrjO88LhhPA1x5Wm8UG2aDZMIiAnJE0rt4fdrjrLqMCyFF6Fp44Mof_YqH_JAE1HTAMQP1RmkDyCntgB904FDYwr4UTIpbs8F_iHdnnOL6pbg7kWgGwDzhnP8bOYucCH5admXXzpxJUTsG8LDoKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7kwbz5tgTr7kcJG7yCTt-dEqlOSgMM7VWuXiEkXqfL5Sban_8coALp99klbR8pm1j7utWcRjcEbTa6Mh6ENqM72bj7MchIMWqcCpYTSEx189KFUZY0mBF1Maozhg3D8p9wOBMO4lhyEPdXGMa06uVvDBdpcjTn9BGCJFWlH92SzIC89d_fiKG-EyAR1jR5vHZSTGV6I_-xT5e1hzWnV0RGRlfk9saJRnxlZ6in5WMBWO1fPy4YvPfkkfusBmc3DiXkoSRk5d_JxSNiDXT8j5k2Qdzufp-V_Os2ESdtnFRfsMdPKcvLx7r68ZlkkrFxietOw1j-rM-iwXYOny7xq6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5lyNCHW2HO3892qkqoZ_OYD4fT5JRmGXwoy0XjemOOyvSxD3_2xzzaFPc217bXc79XOz-8ypixyJLb8Ur3M7jgRNqaQ919FBSs2RK4xl8y-LUHd4AMeHgfbNsmg5t_MbFKFISEwi3DeBbblD2oWy3MCtNoYPeTdno00ESTXWbLiaBD_8bjGmnEIlxdoygcu8qVRL3Fc0UPY7z8vFbY8zoA3kLRAselnoSHqtmhKAOwPQ2anyF0J8OF8yPvLbDZUmo1nU3Xih5aEARUwWahQvyY9616-E0GyOwYnCS_LBCDqcZoljzmoLkne41S_TYgs87v_7RuTrm9WLb1vP2t3YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWMbVxksQpm5CkxrTN0zWwU9JwiumT7d_XaM0GD49HLN5LIlHsYMY_L0aQRN_Vfa3rMcu3vjPE_w85yFWJTdwbOMe1xHrz_sLb-ctFJ2pyAi4vStn6_SYRfxQJd2LNF0QzsWZCtbru9yaUlWC8iqtDlCWA7ZSbEDPNXPPWtGZf3cLc3N6kUOKaIwUJxce-ZhMqhMkLajTVzsHW4VU_b-HwRAHfHL3NVrz_Zxbb4Znyi5ViuYLb__zPHBu1oDQX2_XesvI86RB2mnQ9qA2acnc1rpkzdZHaZa6ujouw4T3IWeiP_FT_zdlPDqEY6qsOyVFxRwEFjrj09YLlUhkdAENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmK8hKZ0cch1uxeZtFaazHmNFpGlyAUtSPZOuLRtQFTLF5VIf8FNuEXLdcJ778bohFziWIg4bhpNhP8uEoXuICClT0OrqLiwDrRQjOcD5sIHEVH9Vetfhbq4i-hHFARi2LE_J-06d3DhH4-oDqWhxcUjnh9qza1Hogid7nTqCXTKWWjd9tS-Gb0Hju70p3N-Cekrti4fV6N2V-geWClC-n1Jr-PkLT9N1CovB3oXaYxHizQVBsnk8uIn5yXHhmo3gz2o2HELF9gf0IimUprUPsUSPR4fw0QSdwKodUo-tFmhPeqlvELj0iY8_ePR9vXeKHGxjgAjEPoC7p2yQ0QoJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU7O-vRrhbQUpJCxO_zXcQ3iFkoptOcbMvexsYGGAaLGnyMYbysZui_IOgUumV1pBrruTr0J1fmtUT8do5zN_26D4DiLdYt7AM8Jnf-139wU5X6q4sRr6yIpPtTgvRdkKImqhpV0fgzPosQsPsCyY5OtgCn6-A_JOP3HsC2mzNQ9liiqTPQioo0EScaumiAd4nodqn5X2cu4PgzsE5mzofRg62m0oTmW8BR6THfXvIHgVpd7qjY5abtMkFNwtFY4qeJ-d-R7TK45vr_o3HYMQZ71YfTrZbZWkxXePt2fXmX0yx6QEaJpTJvl3_-_kYxcqGT14VQP1jvLLE3bQa5Bdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj2lCMLgoRFWsngmYN280FTN4kSTLGpEKfWrg6k8fkkJss_J2mSWwplpuArNDURRHuoqXgN5M550_LNrTXG4H3wVb-LDZaxqaeRcdk44inYmUTG3-QRg9pjiIAu8J2BawoN0m4iEs3A9ToOdDEKUTtyV_V40cAi0joU7m9QLypkMORYlnJYF3yN0SeuR8Z0oc_uFdAcx2WG0PgaDPVYgfjR_1MXF3HifzLTd2Hz98ZgYsqYh8Qo217GkKqoyHxz24xMK2H4N9OhsZYmHuxCcqzi_xdemmoSHEQNUx0dr8xLaddlYai7crXLn3rUiBZIot0Ly1QVEh6GPlcI97TqXXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWafxIj5hO-kkwmUI8K_joNuK5dN9g-gCYOZELYceqcMzB9nRxFnfoHvnpBf58zYWPMBAyeq10h5iVFKoNmIBCAP3wBj-mqDtNS-JAGYyTBHZFQkFVZ6wThg_UhawUn7SVNUJq76KlnRYPeiH2tQpzV_ghrDNmm1HEifonLcfMpGRbJz0ARyJCT4YpIGtac_6qFPxue0p0WmQooC6_5HpfuGelRdneB7YyiZakTqeoiWpcmYdPcUuapUku9thRtw9e0CZB87sDHBI3k1DmG31WrPwqrqXVSBmD9ogVVMtVWCoLNr-2YYu3mBL6ybOduENvPMea6bCmGCi0iNjSkrfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwIdEynUQLf1tgUWvEtX-AvXGd4DvMeedYS9SHIT4a4YtbXwZJuI8Exx9kimVQoxy6GAspEM3vPiJLftD6ulASKxlHnVaHRb3kKaSC2lcVZPAV_s2hVx2WeDstwj35W0F0ejWjiHFksJda9pcqCT7DMQOhRDJwVP6xef1JYyG6vJHYAU5v2ENQEN26APf4Ay1tgWetgvkrEzXtCEec46ohOLgc5yA9E2zB3TYQDM5GygjB5Bjv6Uvww4aiZitrhWjT-7dZ9opyBVxqaq17iOYRAxsmtCV8QtlQsCz96qqc85ofjsL_5KljxaYoEcPanz-PTA7euiHfi0JmNK691wkQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=NbWa2EjeGYUrqfepFKedA5InO6WAGt9QbD9L-MweW4NPkgYaRk1Yu2m4tQBQ_8DLM5yohht-Uxe6W1ppumd0im7geueIUMMJe8B2DOBaLKm095uhN_h4ngIv1URa6FF0yHKDFpOj5xRKjRsf0mJ9GPGT4mQCDMqWVGl_ZZJtCcuENw1-ZKlYYDstY9BcXGsch4xB0w_sV54BS9oW0B-ynvnvDWkvDaSmADOF6eMY_CTlV1r9wt_kDC17DYRC2vs72Nd6MNjo_l8HclowMxuaxWF8GWrXIn3f_rCTUbA3sl-WkMP5iJjhH2L61va2r6nOzT8vAxSNqSwwJk-FcFJA3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=NbWa2EjeGYUrqfepFKedA5InO6WAGt9QbD9L-MweW4NPkgYaRk1Yu2m4tQBQ_8DLM5yohht-Uxe6W1ppumd0im7geueIUMMJe8B2DOBaLKm095uhN_h4ngIv1URa6FF0yHKDFpOj5xRKjRsf0mJ9GPGT4mQCDMqWVGl_ZZJtCcuENw1-ZKlYYDstY9BcXGsch4xB0w_sV54BS9oW0B-ynvnvDWkvDaSmADOF6eMY_CTlV1r9wt_kDC17DYRC2vs72Nd6MNjo_l8HclowMxuaxWF8GWrXIn3f_rCTUbA3sl-WkMP5iJjhH2L61va2r6nOzT8vAxSNqSwwJk-FcFJA3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFlK-m1-QG3zSf-zPBPjkzDdkKksJbn9-9ArPnChyueskbisFwg0gJTk-YMVnPYqYXDg1-UIhmsHs70351Y9YSEghxrQuBwFjJN_kf8ozwJXH1MwL4eRLtayX78rEs8DIMF3WIWvAAOGdrEdn_2v3v9_EaEmwhAxd81PKBUva3iXCqbTax5lkw2X3r6KLSKGPFdkrUJeyXNsvmuUz5rEHIlf1HodItlqT6N5H0p3rqd-YG3D6p-rkGsZvQxGf_brSxqNrIhAnd2pz4gAX7HkOpDHYYqVjXuuT__3-U1y-nw9E-sOyO2ewV86Jq8JVRhWINV1Q2Me7A_k5IUDXcBk5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnagbMjfhD-PcCh12r1LAlWiDSlOgwmwgdpWsp7UaOBJ8N04IEtKL150ASYc7FsOFaIbdXQ9jlGbUXcEnNtydfcmFGzuZPFJJ2o0KeP4UqoZ3vkI3A_ez0XZ02mGcfmcNBAA34j13EDXqMH_tElBVUR8pbwga3snblVp_Gd9-oxUK9jlKx7B_CvIHoUCerUAErCzeCSYdRyTZ2ooX710K_a2sjw8dZaAhV7_i6SxKvPPPxhZ6ZWjXz0e3E8gFxixx2dTA2dgiRUrtOvh4effi30gajSQAdyH0l3uGENf8GjNUOn_8mUdi5UemerLNHbtq-9o0xP_8Sb-YK7DvJgYDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5iKrBoQ4RCw1HoXHBp4Ko1T10P1tuX7RqQAa50mN115wTTEjwk7Ezw3_itTLMDTylcMFl2qTsFFNpFe5jyFIZ6f0pmvLjKVz1QtBA97Hs6hD0oB41laIGM7sW6JtRiudsKjmMyaP_nkXB0cRrq0OfaqWNa7re-6coefsgtz_qcrfpHMhHGYUhWGtDanZGra70eeej744fWDI9PgRsHZFKInHrWVhY__fd6clcNRsuI1BloC5f719sZzRNQaFt1WM912vopkbo1LZjKKDTOOwoph5Komtax_xEr9swc2lA2odv7WVPpDI6zPoCx_BHfZk-w-m2OBtwElnRkupQIBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuNhrIn9gyXa63GKucglzEjbolMQZvqOjWxd5uRtX8e-sUiL2X42wYXfPE8wvIZ1azIcdt9MMjPE9wHGSBTd1I-UMPo4qpIB30YvrLAML6yD0R240mRtfBzk7qU1JuhI4NEAngXEQ5_EwKTf2dZacmZTfXu6ZhJAwxP-3BbfxdZPmjxsUyIRq9WzWTp86A2opUyiH0HPXtjlpQ0V4bzaeVGtsyYeJG4aQyv_RoLMg5a-h5hq6OqvsTnwpTDwG6jZeosQCgfqXkXPOz0DeJEakQj8V6NUfuWGufwH-cjN59euQmJFK4yVFTq4Qq_7A19ccV5AgA97QIKbUzJJ1JIjiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Luof8dA5BNaXtHh9yMGPlCT_DBdoFCVLLw1DkVPXwVokwCKZnmePkaOIXerXE7c_c4sppwHxkBevluUf_Ld6nX8d83kuZZwhT8agXiO6-yzPj9Lj_YFy5SHVDcPGggK47jFLThGC0URZyN0TkjOzxJ_xdzykPEdzeNmQxXSbENXNPoLSMoABYS-0PK2f6F0cSQX8XJiClUGTkoliT0cN-ZYa1VKN4vjeznDIw_X9v_QBaSdDmXcbq9L0TfAWUtluBVyathQOXfadtt5s_nma2ujdqT43qSLJ0MvsC7ovmUZVQm1TdrPkNeLC1uJvMUTF0K_FaMyc_4Gg8CZbR7NPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZgLgw_vOp3pvEX0SHsKk9Ac8CK1jqV2SPkFkDWkko9KBMzLzpjFiDelicep4CbF6J5HpkCZVbGIzS82SX2n5AcceqyJWedAetMy-BdqJetquqDJ2NEnTSfnFuC4RmKISFgiTxoipaLaZBPuc5skM24LS3N_N1gyGDnhqKbPKWRDhJ4QSb7fCkmVMp0SX3jv1F5_DPJ3W9fLNp3spYlHGlG_xjU8SJUr4Ycztm3UiUR9Va0w2rolHOESasXya4gKZchWAuOz7Klk6QoZdvbnDBxsi651R0lGy4d70c4cyVnBUkB_9ZlhpwEKVNfxXTpSuoTfX1Dc84o2m-0pc2yTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWNe4gOy_zkqo77UF_jMbMmA2mpQuGx0c12qNZNBMD71NNQOQgPGypB2QjeVmQ3hrcrPf14HPaPTVGSunkZzoY2d4epA7JlXMGc6iRMFX22w21ygwHrndKn_f_JgFuUI_G9lP_3NwSKcS2a9Tr-4GmGGzspqUM0yJ30z_eML397KxrP_FJKeRrQLbj47u332-g6OadvzzZOno_hHEYn_H8G3-4hZ_cY-OvTtLITGhcA8UZWYwRFEQqbRatK9qxDf8kbhph4LSf4cxniEewJ2Zkfw7tiDa_65apzWgAg-r2nv2xBjnfbQykWVAicwHOBdLe9eATqUzGJrfx7K3pL77A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Qhs-SqfVJeK5GW4Lm3QoPSiMdltsbfIQYqIjnXcj7EuMGxhgRouzKc241T2KQd-lPYHnovMqgE9Op2X5FPx2i5qgTxt62-z8ju-PqWiREFyooGXd_5gxV9W149uwYSX99UNfyaBqZ68wpn5AoXL6iUQ1zUUj6jIhCAkel1tvYH6gOHkvGxq2MENzZ3h_EPQrze9K-2EAUxA3ink0VGcEeM64cGMOXib6UZlZAfx9kL_c4cT80Qwj2oSlzANFKZ42AK05PBU9WegdFFULC4vtNpmOLqNCVL_wlGJNsknUOHL3LHsRtkh5_xnxF6MhWkDB_bb4dRLIDRzhGludT4YB07wLCpADAHGE00G5tQxj4fOJs3ZtbzW4MKlMpeJJ9JKCz6VoMtP9tJjvud2ChjMulpLFd1yA-QxWZlkLB7X6kIEpUaaRjyoqWjdE9-RGdIQ_xVh_hXc5hgKHai3otHhcPCGZ8005iZTMCyY4_gp2pCNPJg3AOe8MStMozYmvTyhiH9Mwfh9WVXrr80SGHMvd7oFwCupMxdmGLAfbZ1GSzK6KCzjnuLWLavrx8BBmbr10oiRb6IKqEdrUDGhoDlfBggfHKvqoqk02tKLShQK1pMX9qPn3-3RRTSS-5eWtBG2ZUuj5ga9w-RKAFqy55LLQCF38akr3ZT1fxt5Owz-4iyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Qhs-SqfVJeK5GW4Lm3QoPSiMdltsbfIQYqIjnXcj7EuMGxhgRouzKc241T2KQd-lPYHnovMqgE9Op2X5FPx2i5qgTxt62-z8ju-PqWiREFyooGXd_5gxV9W149uwYSX99UNfyaBqZ68wpn5AoXL6iUQ1zUUj6jIhCAkel1tvYH6gOHkvGxq2MENzZ3h_EPQrze9K-2EAUxA3ink0VGcEeM64cGMOXib6UZlZAfx9kL_c4cT80Qwj2oSlzANFKZ42AK05PBU9WegdFFULC4vtNpmOLqNCVL_wlGJNsknUOHL3LHsRtkh5_xnxF6MhWkDB_bb4dRLIDRzhGludT4YB07wLCpADAHGE00G5tQxj4fOJs3ZtbzW4MKlMpeJJ9JKCz6VoMtP9tJjvud2ChjMulpLFd1yA-QxWZlkLB7X6kIEpUaaRjyoqWjdE9-RGdIQ_xVh_hXc5hgKHai3otHhcPCGZ8005iZTMCyY4_gp2pCNPJg3AOe8MStMozYmvTyhiH9Mwfh9WVXrr80SGHMvd7oFwCupMxdmGLAfbZ1GSzK6KCzjnuLWLavrx8BBmbr10oiRb6IKqEdrUDGhoDlfBggfHKvqoqk02tKLShQK1pMX9qPn3-3RRTSS-5eWtBG2ZUuj5ga9w-RKAFqy55LLQCF38akr3ZT1fxt5Owz-4iyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KibiKhAGX3GO86SLJkC7Li6jWZDJb89ZSOaMzRjYCfuKLkIL47elIc81EkZ63rZqe38AyFr4Biv4B-OuR6-HQ1uQhO75HhW59oHj55pBZ37PzTrpu2Cryh8kDx_TqL0QSzTMJ3H2wiDZ1GE8787IRVqCba4qIgfne3rUx2Crs5qrSM6LC00seKaSq4fcqKq2lQ9RX0XgRe9-ltDt4_CYE-GJN57jZ1J5XiBpkIyX8p8BoJ8pAfGe_AxOI7NKon-sb6DYdYL5hl8EI0etmdcI98AqmsRR8nWmG9xtgBemT2bJfa8rT6gF8wo3QUXzqxjlN34qN2Cgp8orFzCWL2_qQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsB_LGfwXGbY-eQTwckULSXqo9r0pCRrqiLys9EoXLQlBzCheoQspwavM259cBn-S9NSK5EV5wOtq6f4Toik8suLLwCnTwLukd6MITPFuXbIRauQGM98ZUWUY6WBo9XVUnCg901dahwzrLj__TgOe-p2oUDheptpMO2QR0Q1xg2uMN2cKZkXLcH6M1U5kwsah5tr6vlrLomJl9BIj7GW1AEqQaPov3mo3FqimfrBXWYQc-21gma5PCrC_qh48p1DIw_x4AgQ_FK_UAeqgWl9NZIAV5z8RhWKT-7f-7RTf3akn-7HoZoiR7LKn7C4GGSv7v3bftcIdiWGMk8Oxflq1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IU68q24NLG4x2ulHaIx6Hy0Rb6ZhsRC04HZvzy7wSp7kaqZPGn_hg2P-Z7cAG4X8lhd3VRChFMfhyPOgmoS7zfsj9cU283IAnmgd4eKA4MvH4X9yYnIHRthAJ0pTCvimAne9_62jQCxulOrygSChECgxTxipUYMfFuF9r2f5YoXuwabOLlCyJ-nVwMhk-50mHzKN3cObb9YecFL1Sc0GY5dqHqdG_nbp-1QYBvIIz9QThD-20MH9ml4ypu7AILTR409Ebrxa_21DwFynTIzqxhzFaCEyvgYyV58BP6y_kjHev-rSMTIvWWtEVAbJkcu1GvLC6H3ngxUXL7dOKym0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLrCoOsfnqXwhE6L1XvmOynUqNOseLTeMTQCZA0vLJbB52EPrT1qzkZt5RKLkDQiL9RWB43UGaySicsr9MPkxyzkn6j93jVLA8Sqvx-ki3O_sdI0VYOqeCfwqS0wxFXVNG0QHZwKiyiJBRNbnHIy3PM116bgdrlI5neDmF1btDB_-9lvAZUPQ6zBnO-5OpjmvviotWYZdCya4Gn7agrBB7kTNdo-GxwqOBNnyFSdbKU7hqdi7UqHGILWJbfiN4bxbSSwcRgIIk8dKEscJGA68PGYwpebADrZtMSSvY3OO8U6-ib7Z0dJ5yXb2gvNynY2OgnDFMGw9yvh6nrmztAn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L56IAsw71PR51NwOxjLKHS6LJ7vBMwKgJ-2H5gvGvv3GIbOqR0WpvyC8cvGMbrQKYAtYvJE8bdNAzW15OI49bhsBbD1SnfqjMtbRKb-RRAE6mbf6TXeRcN_C7kXeJYgkTWXXR1lBSQ6XPlvT2lL6Trgfz4nL_ZLcWuHbDateXdjRpUgkeyHefSYSA70Cnd0gkiC_QvQfPiZMAp_KOmPIv4TAHrMRfqHRvMSo2ajupJVXEOTl_9_HTEmsG5iv7M6qdo2ZzDd2DBRsmdOF0ynpxtB_9nJOY8kpySKvgR66Wh5paZk8CO7ldPmbyEnF4ksqr-uPu17QSgyF2-kF0Popnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0U-knYEcqf4AcfbIMQ9oZXzoNVwWRsNz5tpJVHUg-RvEUoIfcQdWH2IXs6NDeGjwId-RK0mlYPug4c08vgEiy_LOlM5hNwVg4eu8S26Yto_RIQPvhynBdLkGk9UeLgNYDyNRMXEJUz4QPpdtaWjoqxFkUxRFaFQlewp-svWTxMgHy7beH7bMXgSgnZGt3tmHpuciOUpSD4hKZ2FDy-rpJiPX_Cg-PB8ldmOtQ8BicUxjWQfb_NdaqpHHAj3E7lgbhbkzXeMHBLZI8tgms01fLWcChbqZi3u9TdGlvY_QnCBe-xALXrss4092-iATPY_dEIX5dh6mq1T5QfcZwDVY4kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0U-knYEcqf4AcfbIMQ9oZXzoNVwWRsNz5tpJVHUg-RvEUoIfcQdWH2IXs6NDeGjwId-RK0mlYPug4c08vgEiy_LOlM5hNwVg4eu8S26Yto_RIQPvhynBdLkGk9UeLgNYDyNRMXEJUz4QPpdtaWjoqxFkUxRFaFQlewp-svWTxMgHy7beH7bMXgSgnZGt3tmHpuciOUpSD4hKZ2FDy-rpJiPX_Cg-PB8ldmOtQ8BicUxjWQfb_NdaqpHHAj3E7lgbhbkzXeMHBLZI8tgms01fLWcChbqZi3u9TdGlvY_QnCBe-xALXrss4092-iATPY_dEIX5dh6mq1T5QfcZwDVY4kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdyl08-kb55XhIN2pZ4o2t5N9D-GqpiCprCd2eTYQwKDsiA6cFByEuWiRoHXbE98FOp0C1LvuHWFWE4Xfp2Ym59GU4YCy-xw85panQfPOR2jVPNC6Si7vrqYUu1nrrqoS7Gcc2hb5KnUiVe4TFmjpZbo5AB843UOpug3wTM-rTO6lCqrij3AaID63_MfX75JDLaD2eF5VGaeBbtFZIv8u5fm9eXrYuhI_aKtc_KKpKufIieJ2NTfVRRhanqjv_i1QyoB6KuTeNCy8XdMjKxQgn9r6fRHdnoFNyR8WlvtkriQu_vVfzdsd084l4uqsj4TT-2lo5Emdjp9S8ebioeAiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJVGA9bY38HcfUSr7HwrV3Jwe6MwEJ0nXqEpyV8Dtj7eFRPVZ8ROoMDsaUxXOpHG5rltsjv5W2n5naabPNDc3luMPr7JKDLXbX3CZoynejqUrl6ai_3TPPlSdC3bwtrIWqcOmacFRznkbhuoUcSlyt51LsCelZBdaz4pjU-TWrRe3FiJc4FeW_rZllVobJtJL0ij8XdAlFssNWqyd1WZPKcxh3AP1z_V6URq-ctNxOpiSBE5tht5G84lrMddT67D3gwNkkQGtSdiDckdTJV-vbpjA9V92m-01FenRw8nGRSKWSdNzGJllBoNR8BdrbrybhRWJ2pObEbqs9bPegkhSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdVbf8gNRHpaDX9T-YgQr0xPpCLAEB_DCr0grGP-OD6YO4jmOmZaYs29_8PbhTSSI0DrymF-yTlEK9pjyXZ-VUmjR03wLm55SmazmN6FXYk4DiaP-ZcFImIlPE1fkAmYvmx8QSB74mMwTAlkwrkypNtgosH-RCyXa3O7gjq76s4LMq7OyvPKld49bxtKPm0KonUukVsYOTqvJhCEFFLc7GUABENeLMui5jeef_12vwYjYgSkTRjKUoLhmXu4Hede5Etxjia_SjINdqmPoJhIvDydSC_d5u5l944DX94EPhk9xTu1P6zhcjdDZpI1_7YXPyjXV17NY96CfQRCs3MU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxm9z2c-qcKt3pEux7IA3ggjoQlRCmRqcq8zBNps2H1Hn3XbEC6XLm5vlTBuAkmBSAsCmZAHrq33rAEOixR7XOdI3P9rtyE9v0MorOymaRFT3qx6L0ZpniA_mtTdKyBY2YSjy8Ekf00FINdPbaFC9ckgCGhfxC4dIN4ZMQgGXngpulO6Sk2f9BKGekNu6KpwHpFJrmsu8IZBUhI1K9c_GcuDC738JDdY1p5GPVsOkv9hy2OIo5t1flIe1r3OfNUnzKIL_4Nw3WOdUuKuIFv5JqNICDJHt74Ty2yErRcTZ6sl89tuUIqjauotdtEDsV1VPUYSQychwuK8DCkRbuz-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bc9uIzltST74LLgmMNdlpPXvEUpLEu9FuXcCQa5H1WdH8lQ01UzGvcbv5rzIY8GVFqVJgVoLpKcmll4mEAwDV1mzIWmR1ZmaZfyAbsWdTWq7Kk4tm7-9Owkz_UnpaJHfz4Pv8hVbKvplgklpedbG7W-QAHS9f1stYxKbchJrp86qlECc3Zfoa_lRrMmcqJDWIEp-DGdP3icxN39UhivhwvOqEzx5RX9nWaBBDWrTjtKCgeOncLNeOrFfCYqIiFH6QiRP4UOAXu9tFYjItFvzTDvxLA5vMDe4ccUQpFbXKN7QlEp_QaLaTOpyfKCj414ZRjgH628x8zmQaj7Lomfltw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIMfQrEdah3MlzB1zLRHmRKkbgQIPRFaFGmkmx22kzYGLoZxspeYTDh3JbbSLt_mMQAMMQ2VC-G1WbJygdycIaBazsOpvofpmVj-1p3hud2mtu7qBYCbV8S4lVGHTRFb_l3RdN4MwuIVR_4tU4h8PajvE8Ra8wTDEXvfLtV0KbRjbi9sOgtNvQgmsw0Z-cbXcPztow-NanhBxWZdt-jRx0Rge2qfcV47k31QbCdrqCh9qLp-jzQEm0UXNbsuVv7rt2qD-aJt1CkPxMLD5m_vWBzbrmO-eQP08lAP6Q4TzjeqnZOg8ACOphD-FGf4xrp2JIeA9rWcJCem7veZA-qvbA.jpg" alt="photo" loading="lazy"/></div>
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
