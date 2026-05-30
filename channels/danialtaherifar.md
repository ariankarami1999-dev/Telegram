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
<img src="https://cdn4.telesco.pe/file/UlFoyFM48aWhwpK9_2FsquVVuV0sYYzb-6YjAz_5XZIQabDKWgoNeE1FDfNsb1x6IMb6aDlIgF8EQCb-rZmUuVeNFhOVj6dXvemIlZVeV-ys_VEuewcdQ5y8P-r62uL9wZIH4Dtid0nEzIttfmxhtMtydNSnysNE1-GVXIZRk4waC6wi4gzzcOqskkfX7qSTlMTmHhhY-7yKMZihYO7YU6y9H35mA0MKjEQAXkXI4ZYpYLUufS2LZQcNK5SnJaWIPaax5VaLHDLMEwyYYTpoj9975ghaQ35qOZAEl32DJSnvhs8qn_0FXZQa7qBHxVbntjodMhZPBmjOk54fHxS1TQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 22:06:34</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 267 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 446 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 552 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDiADd_U0vnwnLB81Bu5fol-C5DgcwF2r6VOLN3UspZ2gdzdFSvCVg3GlXyaoGDCbzwcy2HmX_w9NbMFiCJN6F4boReVWZuYXYYrIWPuemH4e3LQvllfMY8_IWezis2m9CeTjV0SBvoXDHC5sTDiH1dwcYEGfkHJklkdqofWtWin_Ply4y4VMnMZpLpri98C7NFbbT27Us8J3MYbDeJBeyO3Qf6uitobaiLVKbW6Mvrb_S686FIG4o5zaEs9__xmcBZWIfZlvPIOqqxWF3NQKr_EL0E2HeSpXCvxSkbwNdiFlF-5-Uvos96D8v0yhDiaHRZ1nXiahLWAvyiSL2p5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 597 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQcEoRTG0VRTeRuQpiFQAesz2j4mlJ1_KnUYq3VFoWzzvp-TdUHc9_OGSR1feI5PeBra46cilvY0Ln1cFP3__9kYB2hHl3-QPGxKIhXKVqLx7MOjSUWx2wT3OH68dR2pj7l2-pgH0JRIxXLvtSpv8_iMWcq8rz65tvRYIeLHtAd5dIEwUTU2S-4IUPAB1bXm7Ma_dXMnK0a901ZfI0Gx2IKNs-lO87kV2lWNNszuPRkfbE8t6Gih88k8oeKnB8GwEGhvEg2DzBNJ0exETxNYn675rrAC4Wlx9XEfI17h1V9YhOU7kef12asb4o0Ux0RBaWMMcqDFqz9RojPf93jGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjiBI8vsm4I0Bi4xoVwK2OeynKX6okFd7ccs6xVtJ-9BdTb8TaX8SpGtkIW6m012IiCsXSQiRQVnQnw5NDEZe9IsRoJwK7SPPvUyILFUPgnzBCQ0juRevxHnCLiM_ehEMEhxFT3iKQ-k_WAdIkG4aDZKLbGMenotGULIVTO7Azyxverk0WT7TXxlbeOXzOQfwq_6m2oT8s38p6evphFeJwcC4EIiSuINFswki82TZad9fobC3IInsoKs6Xv0UmW6WosQFOeGZV7iI6c1Fmaer8oCMYpfXYIFDqNBWNqMyuIAIOpjZmjSiNwsZUh8p1LhUfG3r2uc7t9v7sdgugNIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmHlLJGGUcFtiM3rIxIyngW7XNAYmat7tl4y9RhMuItqn7WlLf3xhufhl_BvEmOJMUw1d4qa1lln7M8GKlLJy4JssamUBXtpk7r2fJdzTUdYbFsrIWx0193sGIywv6GHoGAlNspVEXjvJpyAIFpkDUBBtdqaY6GSyP8-DQvfoAKN8101IU2rh1xpxb_krWLGQ2D8nsX3ptEL_kbCPVARMS41O_HlnxU0CqXCunUm0ClqdzugnXTJxqSpWlkDQv0CUs5A8Ur-2h7pc6g7g2C5RRWhbw4_SBVSe0ZRIO2e3nduWG0EkYBkvxdYzBlHsRFDGE4g3IFyIBaeUtNrKmnrTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uB6Ojd-LIY9pokegX23Ye_SDe48epgMVfPcnjuX5jAgrWp3iF_txY6AP1pcPZrOCavgFidlv5kK91WAq3Ytbn-FXqRJz8Dk-33pLmhKByTlyTEUyWUoGKIou8bBIo9qfZCFQ7z1HjQRkOIhLU3X8mUCHr7BsukfBN7nxq5PcKs5ZGC08paLcgKLHU1ELvdFAzC8FTTYR33WumtY7i8wQNSgeQd3B2O6nREF_gxPp6Jj0oLhm0JARvnDajXJA4li4OJICmDriXpW48FysmWOJ7lz0eiFQUgTpev9FC2nVekKcGeYWCOX4M3G29CdMpC6N0P2iuIAgUAhV3xzOFglW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 773 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 835 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGsm6HN6CmnMhH7Eo2wnto5gdQoJ9hv-aLjMXesxDGvFsa1SUYM6Q__njo3AT4XCg-bQmLfLZy3-_GwPAkdrXzB3e1sxXvQ7Arga49DaGpRnLU5HnsvR-TZyftv9KIesH2lYJNESwn1HXubJQVz_aAiWVnkLf8RhZZrM5rl9Lf5ViN8cubclEC1lOJhgUV83fiCRdFyabouRM9zKkOhsskDlRAZS9YzLGBf5iA40vgbkjN05EAPRJDBiQIHIBRSHvWwjKZ3S6zAgoYLt3hrrCK2g_j_6zE9IxMfJVo7vR6ov9nv2qr2jbR8-PvjJX3FXTUU1uG9et1Xyk_1zKQychQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlAwfdLa27L-zbcKIru7jVkCDAxFT3__OV2G1jJTBMVqf7ItV6i-lNaeRfkRJNTb_MTKE8bdN3tRpjRDADTEhgHnNFZn4rY3-qlkeTnVGgNf-zJEW-XFu7IMUCqEWfnY7wwAQmiuq6siJ0lRCGln3O7qDRdxsCJdx7vFn79R65kCUotcbpeJZ41zz2XkIFJq5lJFvQ56PRbfy0fFtglI2dKhj1ILYR46bZRrs5RoKjDfWUimqOpWlK8wVARUmzC44bIC74ScFNDZokqPn4-5wo-7jDg2paw3e_cgtM0ZocBDoNVi42tYKdSz6cLXgE2FXwlMGCBY0O1od_EYWctOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSvlgorOD7qnZHHkBWRTMGg9YO4UV0KptQZazc68w7QZuAUl37WAOs5WcaPTotf5LW-Ize1Gwng1rzAPmKBR-os4-kDX-tYdtMmZsAlOzZwEYCwxLuVdQLFtHLKokoRhJgBozKcacssyZQYfbvwBmcRzwCc4xAosS0vlVo-YGNSE6ZJgagd-eJd-eXvkY67-nQRfl5YlKi6FKPyT2eDGypyEUgJquDApB8umHmwwOvu_Xx9yZ9ZiSSTZ-6Onlb1OSYqKGEuHeP8hHvWJDemy4wokzRteRiJB8WzcQ3uqgYtEb96WcH8gTqQn_j48FdCw-zNOaW-9QaZtRIsRzjzFZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKIecz6iYJDeFFRxfGaxp1Q7zxBXks8fekuKthnR999m-GFYZIVGJ4XPc1PsQhD9sZYsrRrIdqNlTutFn2d9sU16iTY7E9sU7LNGu-ltr5nk8eEDcxx3KoPT7Pj7E-XguMjryhHxzj2918G7jQ7hn_XVbjY6zZ4qkoM1wYMWh10JrNO7hm1DjrOYuADg4MtPursr7tfu6G17ew86_WjnvS4w9BhSQrgCfwQeWuHGhWG_IyglxdKzqG60ekmeCQSNxVgJMjbr8zCawdEGbVhRjikpGYU9s1_JcEe9EmsYZaWD9rtDbQu78AySv73fejmtSpiLuQkEjZHWvQdvrEe0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 860 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNaQeovOK-pz7kRroovC1ga9-s04Ax5Z6lFBj2K6PBqHbScWlF2SbUGiHdy2ne8xicRcAXrONoKtTDer1FjeJyMYqxUUDDIb2qrwIR44hKccFrWqcprBOu6x1hpwDNaj6UDPjNhiuh32QhKmWG8KMfWUrxTUf8eByo91eaqdX7ts3D-4DXx2tllLGFzx2975zXxa-2bIWi2v2_7Lp2K_N6hV7PM47T4MD1bjFo9v9t7ZF32iwP67I8aO55hy9MmjrfNpoQK_CL3twaLcnKEjNPmc0URZ_p3J2dawdBvEVTHkkl6nSXnRc7KUinv3fNYmzfZU_m377J6HWcoIzLcA5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2E9qxMhX1vtz7oxbzM3cOewB0KbxAbcmT2TFzTl_kzsGiQY743sBNWn7hTg-OLdXR58gZrpAKDc1WZgr5MlJqAxuHt4f5I7QiNNoOe-l4uWeGRv59ZfttOrPWc4Y0rduCjSLVih-LSQbzbsJ7YG2lxLV0JDh5NI6gRBEw0Z0bsft7OSt7-ru1FeR7cq6d8jDVSNvmCvly4uNfBTpSm_6HlHz0ply2AoQ25fB1j0fDKj6YPbABWv4BxIFFTDvN0RZ9ccQSS_neANE3D7YIpadT0YAwmMake5-lOk50cJfqNMHtRo3MgHvF9qns7eJuRYcEvtKaKzB1mKjM98mCyA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaxkxyR7vPZyrasjqBL-Uv6qY_MGt6lBHwRaJOAYbzdKmZkUzmU0JvsbI-wWilN8LJbAXG3hUPh1eTt_0vXiWZNOWi7G7jvZBA0YjCwf9zxZuor994DiUJErellz2CBkj57z8tRtGvpFz2cHHuqKE-CeroI1yJDgrDbaNoDd1R95Yg8gI8ayAFdevkhYr1UxC3tMPHsJEPUuuT3-QR1VTMwBT1TOvYFSKrSTEapys7-g7F9tel96bWgYZRJDg_g4sfHbBzpsOeMwZBRZSYDhzt0lSe9sZt4o9fHbXDOsMpclKQu0i8vWcWlzMlr0giAUgP185btmFc-yOYldOSCleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ktieMIEz6y7svQ8GjiMMeKWh04876mOwNpF6_lIM1agrG6Sl0kbeUE0ehJ8SJ9J1VAjhJz2uSWipdALEoLcJvgH_VPJJpwUCcRbUs64VHc2Xa4JkYWafnnLmCLlXcQ2PSpTYbtLutumuqEq8uY6EnoJmPj8BgHNZgfrjOiHWC6ZriakcYWsBtVj5kudGI2t251087_acXEF68Gd4ysnQv70srBdTN0XpYwyU-nVhSVKMxLOcmA6XNJHsmvJE_HPLQf8IR5XhKfBtshAwjCP7w-9bPT5xq7w1AAuFSMbSz4IJpklwrO87i5rdMxvb4qmzeeJUg7eTZ7xJ030AaJzTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sV_O2N9Xeeauu2o4yNmwH-79Bb5lhh9a_pT1ReSklIrkC2oQsjMJsj7WWCyIsUSzyIFrxs_5nKhqDqp3laNQ3bmKDjKedBQF3Me_GZCCmO51uoMoAO32PGu6myHDdZGhesPri_Ww1Fl9aQDpL-DcWbM7M1SOC8F211lIgEOdaEQGgazQbZd4Js1lXSFTjUr57zSoo8J2dEba_K-Al156gJ9rNsdwMZxXAOMi-3qv9m8kPadsC4PlpXWFbdsAX5s7Gc1pFLLOdwo2ciJGuBEWRTsnjPC7RLwstaq379wOajGGoM9zHXNGYd2FZ84iu1WkKxhl0uQWwJf7PFkJFns_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGlrnK8DkSMdyVJG4Ytn9tO8RcWKn6lhxkJdkk6NjFyj5N-PHU71DfWE456xFi0IJoGW_dDlYoC_g7w11zYdlEtOAAMFdD2eqwb3rgFqMLARmoLXgKQ-oAt_TB3MDA-g_U-hOLuSqohPgip_-bxJLB3J8R59C-990CRDde5scOoXlSXu6kwfHfdEXwqX_bClKx83PNrlWqk-qEC1ZMw3blEi6GiObk0Cyi7nabosUI5s2oRzDRPs403lWWsDVYspI4lZ9jkIDkh0bvFVZ1e7XK7TuUFC26ExQdT9iDlydhxuIdhGHluNpDhoJrzbjGWdzOKHODCo2CC9XPt6byXUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSfISacvWUYDs7Ma0hu5Co8Z7aviDOhR24ThOavCoGwN4ryIqx3t28GodEgygGKtgionfOtyGSOWPokPKrlSQxnGhPfTzi6x2ObHlWDrtEu-CtaHRVfd5JMjZMPXlgtDHeFsNLDV75lkrpIcW7CelbozZ3XLNCSlmpNeNWboT6FhHKTbsRLlDV0T6bkV7Qcie6AKxAugHazTp1a48JxHuveH_mEaF_hhpQqz5huRm8OC5_lXQJVItfpt4DiSunYMZGf_T5BgivCQEIrlWbB_iQaZujSO7rw_7Pysy57LrPMmPcGK5djVHCjB5khttvGGZMcfgz5PkzY52b-sqmqNBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4q3w0nPDXM87bB0FDVNZKiwHAs40yw6kGaZsc15TbyxuiziaTlGKOPwuyp5lDQMY3wirFdBEAW9yBQWPnT4xkpg53m4kHFZHwm0mLlzM8t9EvdXWumIRMhR8P-27PZ7ZKVZ65_djxJNtPOa2IS39Ou6XG77NdQA6Y3ZBpeNQwz44KDeIHZTwhUeTG_Bd9fGQH2Als2HK7R9jQh8VAwmKtbFgjaCChcN3sqV7ICTD95TZ4k5ZbkUFFU3aC3ObMFGCV2KdIFudP-ttCrVLU1oUx8nAWDZHE8mcv3VjVK1w_SBOXv5ms-H5a3BkCJL4wO2YtXeuL0u0UItK05dDGm6Ng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=hhbnifY-IjTy4m4MBCF4v0dA0tqb7xXIFqAjt2d0x16kBPnQ2gaoGqUd3_928fBgMmp4v4oMZ4CaHsnrvpP-DAKIGA97DPjadzjyXDSGhE0TlDKbX8d13btPd7-_YRDsnKwnw8IBYVsGZeFyMF-GuJOcOnUeubdjU_RmTUEX1RyIj8ybOMyhNhUgEgqnvgSAIxC6yrJil2ESinnmDmXhFbWYEIC982tKiKH5VDpStBz5Ew2MJMatUX-txIKWDWfNEXa1FX1WYJauAQgF4f1uJQxTCKGRzWUdnDKLOCJgzvobTLjrTgk-TaBmIqfEVh0-B7OSL_tyC0_vMv2mxSN5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=hhbnifY-IjTy4m4MBCF4v0dA0tqb7xXIFqAjt2d0x16kBPnQ2gaoGqUd3_928fBgMmp4v4oMZ4CaHsnrvpP-DAKIGA97DPjadzjyXDSGhE0TlDKbX8d13btPd7-_YRDsnKwnw8IBYVsGZeFyMF-GuJOcOnUeubdjU_RmTUEX1RyIj8ybOMyhNhUgEgqnvgSAIxC6yrJil2ESinnmDmXhFbWYEIC982tKiKH5VDpStBz5Ew2MJMatUX-txIKWDWfNEXa1FX1WYJauAQgF4f1uJQxTCKGRzWUdnDKLOCJgzvobTLjrTgk-TaBmIqfEVh0-B7OSL_tyC0_vMv2mxSN5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbHujsJS8uZhwYa0kMDzgxAVvg1oQFjie8Xc7UJDk-EDSgOX1l-I3_UbPLkTaZO6Xm94xIDWdeFsJv4bp9Gt7o7PxhqcnnmwaYa9e4e1pSqBsEp2FsAwiTc_9JCGDow6pZhpuA7GNvBD3_P7k8GFpU-rE0SWiXxipjwSoLFpb1C1l3Y1jOqT1zgdq4lD4ufZty9AG4FfIHVX2aIGFNlkGulGrsTQFj5ACQL_S3VSgc9iTYNlDFnSqlyIE1LF7xav55HxQUChpZYXot7DpocH40sy-5yQRK9Qx6xf_H6TGK7KRJWHRqyEFxKJCYVdVgsYM_lzmKPnlzTOiGLnDxNaJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ9FPq15JC_szRSMKSAl3KEilz2uslnUma89Y9u2zHEN3sSGB6J2MbktG4-zkC_gCjtqd4Z9ixq0tRFedkas-oprRDndrnOn2fOgrNNb1oVFwTZ8_Dt1wlOWN1PjeytFf0cT7bbooJ1iFp8pEKVxifyU0vdpmMb-7iOGQGEMOSSnl_Ef5ZHbxRVKDArxlGIn-5OurvVCRf9OsaKhZCpE3uAIkRGFpXHBqlk2lTE7OxxOayjZyaf--ZMZj1QaoDk5075vSTg_Ek9ohYFckMGgzMXU5fQk3FHGaJQ7ivfpSBRbYPlBasPjIEq2ShgwRnBf5cDOwwhN4FwEhbTCkaDEpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlhdqA5pmKuXDRRktoxwTF7dEtID_K34xvHsHAGTqMZEQ3UTHpiqqquYLxSLzqCU3iLfKMNE19CKcm_uwLuoIwEeMhvd9qGAI4SUYH5l-AS_u0KZZ1-J6ow9-4L6Vd9fTsKuzDdtKynSMZ7h2oZELF7aKTmcnCFrfduY-VlD7f-aCxwttGm_52oUJypSKQhqIGwHI4OFwb2XVpe-3sGaISXq-CBfUVUcmMhTNP1SYs-MJATl_AyemaYpqe5jhhvp3yHK5cIox_bIUaEsB5ijiKefcufSA-zuCU7J0qXXVS5Ibk4W2tYS3Fuj50iOp9wgUTSNggsJ4BkIhBgXqmjipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dopcbGp6WZ_PmS6g4pu1YH2D7vN3ueAd7aYdFcBymCODzwKu3QlkXYS2qtfotJofBccdao5Ow6PBozDZa9KOE0o25GsUaJ8PzkVyE__tHu2-1PcePkXGa-JtSlet2ZsQ9FQuyLoh9JaYoIR_wQGYqqc3BbGpUL0ifWHs5MkJwXrmYGilzvsuJjckjQwrRnWCOtCosKBEHt6rb20aQ7uwnbd0n_eEM_J1sjKp6kNBp8dxq1Btq-RcgZ2r9Ehf-TuyBdYPZY43qcUriH2EgClWCtf8hreAgGkkgSDkqxVFCM1SZfYQsnFhYobW8HMbQhiNPhky18ustUbvA9ua5aHVQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPu4TAGm_PJ3d1MYNWGyjS0ElSdt4NwK8QqdubHgBLG1DqU40Xl1YZhnP-wFHYblGOucmJyHR9O2tiLkIqxufy8ivJoR4g-1w7otGJeEo3PVsx_UL8w-N2FtZIFS9rPLNPqQhL9k4VVdR7CQHLOv6rwmLgsOayON3WIPgAHwfNmSSIA-BJR08mWBYltnRMGukP84DuKZkKkJrYqSqwb-XT4iI5za3ukcDKDOUxCqCyUTndkL73dmW8gFhxwhwx3jpSOHjuEg5S6GU3na7e92GXWdUG1mf-BDiqVP3QFteufoAAUC7e6fm171FcHszYr1Fg59CknGpc4jcRi11-NfIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwLKq-mpoHJ3ZHvjdGbX0DZW_JL1cMUPM9Qee6XBsFV0wxMYwvjlG0xan2kiNemlbllK2IiHm1YOFHN3rsWBFS0hIhyIXpAN7OlXHKY1gEw2H1X7XOuVU5QHKq8LiqhaEUgLZQrKCQrFAODcsR1R-pcp4YX9z0PGl023m-cn0QuZ3zxmL8hekXUT3QXuP4LSt_ErP9cWJ8Hp7sduhXMfo0x7N8hvcwBVzcO8rK3CcmUBt12O66O9UqKHeQIx4dEsHtulKBGHK0H1ybKs3mXlTtxWQLfUMFb-mZR3Tqks-Q8wu0aNgVYV_tWSDjaC6NE14F3o7IIywoOichfXumiDcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQJ8u0_dd3dhE_EEpjgbr2oS7Q7nlxWXOpE7EKAeVcwiMJgRTbgpuGmmCSZWNWrFgtObiHQiQJ0WXoZl9rTM0I3pVhC0SFKZ1UTBuqBCsMBVu1dkPJnwCUBhHsKGxbQTbeJevfMWyOFjs-x-oU5TjnwFc_24MnJ3je9lACsA8ix_A3xd2sXXDsRlAppWzgeS3JmCoZp-tyCStUy_IrTEzDCdsnIsCn-aePyLQT_6kxKQknNsLVlcx5KsY2YnUPOTm-DpYNQKpgWRTJo1P822WnYdiX-hSoIeBYISveNik_-sSjZjkuVN-BQ-PA-PErlIMJFQ55_OO7iXGPg3ATdKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwtXf77-oLO93_Fnhl_KbMOjpwLzSTdDtsmN7orEvAvhB6f1WN84I0eWNSme3YNn1wpXQf9j6PpqWV0UQYOVYsiptkwOp-3g7v4991krjMglzpXeMpTk7636VPVqKqYFEfTfMvq4PqFsjVYC2Csp2n_GTBpHI66259eSbjWf9cKROCeKvJ69uyh0k5iBElEO7aSjj0j3aV1ZkAw7CdmAPDgqNUyCsbJ0lfQIT0Hrxq5okWCyf3mxfjSE5RQjqV-6Z1tm0CvTOziqJYhhPwJ56MMZ9g9Rig7Rgu_r9Fvj91xowyU2BlMAWDBDqY7sKoyBnq-gVOGG_JZNSFkTfRZt5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3P5tlEltzezZKKb4vkeOZtdz6aXzIr4B3Vov48FqEV_immmysU_B_90nh73NljR6Ie2wX4zlP4ocB8Ck68M_ZO7TuRLKLsI0XnBEmTZEMbpXPLboh32NKRmJZ2wkilIY5jcmN6JWy_2yFanaoVnadyAZnFlUxLgSVjCxo_rXsSJXqt73HFIUVIi9Sv3LrRfVXiqR2XEpNrVYG9H0yFxdY6xwFi01s2J5FtUhwpJCtjSj7AMnL_3R3bEvCCEyrFblP0jb2vASWNfFAKKEBdN47nElhWPeLk0_QVcHZNPw9zWHcXyiCiFGcmpwRseH5qT9V5YY0HN7OCTBK_EokTApw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hc82PvBJW6dZXgZUmnCzCobJRP9GP7ZOJX8_AnQHL7p3hqq_7Y-mnTSIpK1K7lrZa8MZctB-YAlU6S9UYWc9-U6YleLAJMD5uB3_42cGSjA2_DSMtCNL0qDgIq7E44jjFbbork-FzFiiHRpwo9RjPYC3WIF2iAWivgbDYic8D-7V1_On4zAVNG4ArNF_ca2Y2PWe_wCejGYjOJIb9qD9F0FoMBsJoCk5tGb9mICG1dBIGv4CCdsOA4PLknqP2zk5bdR7B6gXM24YTP1Suh6_F4_G8jM46yfS2HfgX7Ke8rOgm3X6fYBSP6RcpU1Chn133ncoqvHaMWRy85IwSeJ_DA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmW1EoAnxNaVEXqKNWbzds8B_tAeUd2BFTLYYlBQTgV3JhrIJNzV8LExnhrJoL_YNaGHMBprXLzcIF6tKHt6NcQnXnq-4-31-OqKFfDCbRzw7U7ZuIfw2PihdXLRIhRPwhc0p8mxceGQ5xft6YRZIRb0rd9wn4SaFsu9XPgjWsfCp9WCDLFNRmgyMTirsVz48Lx_htJGTkz6OE2QpUKgE3Cl4DvrvgZMwLajDNzXkpSt4GAbvN77IPh3ReYqL7Y_83xbKRiUvHY0oteneUnZe9puoOOtxIvdYpw8tf0d9hUlqvAt6Kz0Rch5bOKhvDFtu_67TnGRWZWUg6SqCe9Sgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIoe9ygRYhQCSe6qp5AOFPaLHdCBz9BjAouaPxXwPnrIkl3H1-TBIzKB36Ajhc3DBm3V0xeuHVH7k7LerqcNuEcWZKV_MWrWanVpkkLCIGomi9mCdxdXgnkH_uaCLh7pabORLk8R1DFlMPkocfkLTLgpBh2XYutLqtQ2bA8MF1b0wvt_FXeYV9gwljwwX6mriYisaYWEVnmHL-8vNJibZT--NiK6DiY8ii7C8JZ5n4F65WHFR-h8tDXIxxRVaM5NwEY67cWSbAxSlRUcxQgqaztCv-a_76L5J_t9rSuKAXI970OpF4hzNPtIti3trHQGOEQcbNzstjHcMOgVQ6MvTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLGr8T14jp_Mj4EfUgHb9JZu3oFoWh-8ugcSHxu--ZH4WlmK8hYlpDDUoJ4pVOpnqicscN79U4OR6D5T1iOxT6baEUMCyokjkzpBQV-nzyUg3jooUFx-5HARJAX932ZJWgBEvhBW2HmuRxraCspBlAtGFRXJrrtuAj33_JBrbyHBMUOFf9HaN9qSpk3gjWW1IJN1mbs7Rr4gl9X3nnGkytsz_LIj2cBItkZmMG17Oh9_r0CE_20E6biGs0xEGdEYupi5n2Sy1b9Hp-KeOqOXeL-Uhs-gXjk60YpoUPIiJQg2wXcYLhDojhW6v_94VC4AtoMqAX2ovyFyGS7Nd8ydZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fys7BMOsBHDvQvcUXaLX_MosKcbAbLoEbnN3LuJ4_f62dDSDXwc1C4CXEjuczrt29Da-Ilc_XlxLVLeqSkUM4o3vqipttIpj8R2jM2rnIeG0dWmaTWK077YDOd6wK_OsRo2uZdNTp11OzjUX-xHPebJrktp6cD-P08pnC5eZmuADleG-4en84xeO9UqRs9reJU9ZEZ70F-YSSemj8OFMSisLVSIaWuiAfdDPfs00KhXxs4idc_cI4DwQ0nD1EaCKcC03dsQVl277FMAy_GlKojcM_aPm9myC0cx1ccqFobPsh3nmGEw94q5kupXbQ1JVIfPh8NgHrCToou3TQrfb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSmF3dMX0GyTw2PjfuV_C6VKrj0ANMewNJ0CTiQCl0OQVcn3bjuCxLviD3A-SV5DMeSoh931vp0Dt7IHYtgo5awrNgMcaQPBWOXSZhtqXdtRTA1ULrScLOsyktAazcbYzU0xNinpdcU3PB8UpbhteRRhSUqEy188GOX7cilZ4GxxH1kF0uORkD1c0XT2s6SP6BxqrCnOKql0srsZlHQZDNO_eGOaX12KSypyd7wCj-VfwMcYGrj8-okTp5HDu9mz11MDye_GSsr5DzxGnmZQ2XjAyVd12Szz76Of_BImDg8qbWDFe7Dk8pLka1fRV2FXp45lbweo7SivITTh99AHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJyJaDA2AENNQJjIhne3MTfY8NXDzxq7fkmkWR8Ry2QiQgJkkP8DQsYwCKzVswz5vmik7zHVoOtGHKLxcvZ3BKO2NcfvNzmhcCg2_HOc0rzSo31ZnnGqUQZ9e-vI5rpAnhylWCeqLXrRO38jtrwHWb0LzuEKYaBsZi-668uwfgcySP4B3V1Rg92hAVHGvZApMfQnj1Tlgwt8B2wqJ7DaZ3gDwDSXvZ8Wc0MvUgUCCBSUIg8XycYZjX9g6I4gmLqRR69-3mZFs28CXVjFbe4I4LvE0C88ppuvNkIuSlVJUJhpdDu5kdiktQq1iQqWF-ckC3dqLzLxu_QO7GnxyiarPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ6cZrkK5q-6Osbqs11nSV3B1bm6pBhY0YbWxvOgX3E9izhEVDxdbIEASN69jGs9HPolK4rovMQYpMJy7dx-Wn_fpeH03y6E2ff9NJXIidgNMATTNw2fN9uvv0GEerPdbWRvSbFauL44yA0oNZLadiSCbXvMSZK5lZhQf-OWJhpTjdGfUE58ZHyQ4CVq1NkrEjVPo2HU-Hdj64GPjEd2A1_m9oAgaTd2wfmX6Oh0L8Y3cJSrWAQNh5UCAvs2uOcnjVkH2taxoQIctrjz3MjW6rzQvJguS7T5TvEUGuUzYMIzGc0SfT6Rzt5-hriFCjLhB2ZK-VJkErYvzyEQTmm4GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZkuMWuHJkg_gaZ5THQWu5bnDO6oUdiHeXbqU3Yel9odVRdlqYDpMFg09P1QyfD5yjNfiHC7XcWTLR-nncQLC3wZHwT8eSBJqY1FwgVAIf2OY4esrFKN2kCE0vSfnbd8ED0fuOXOnQAsKbb53mZC4UNOuZaPL5bIKgys2DcFTOFwOPppO6gA27MIVPiHXtLJHfoMAlcC4GajE6rdgikZlfaqxh98mhhx3XTe2QDbtwbfnGY_By27aVew80W90fY6e50rzUHE-PIhW-ujeyN6BXUuHQ8veFr2CgXZNFsmB1eeFB4YnUEXG_dlfUk2Qv-ql1z6lAp57Xrpp9_PTwW_Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4AM2fSWxjLpSrvIRm7L2_ePu2H2-CxTogplspe2xgRxhWuKohAjE3kRmxlPUVmq1CvluIcjKzHaq_bRXaOoqQJ5atQuhr4btK9swBtJwkRPoukAkTD4gBSx614wDy1PiyDro0HobIqC55SnErhQGFWpnu96ayGtxpd49jwvBr20GQ4MzCypjChRU_kFaKdhVpPEO3p2RTBNnAVIPEBWeFRerIJeAFndNeAp7URkWQ8Zh3S5zMI1T1u7grwCHjeH8V1k-skdDGoeoxIKsLQrCixJL7kWznU2u9SG-8SXl5LhfzuZIlNeh-JdqtPX7vQ4uh-gqj6ckbjdgTw4qeZUvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn4o9OGFou5nXTv5_HdygDI1_ZrBeMls99aZuJs110CbLb3PaPrGAGg4uRnmRr4TE_yT5Qe36mQvuhY31YSUpo1SgYIFFmaNwDmm0yKyB-OiylH47B73IcNlp-n0FQxM0y8XQkTOQLYRmBe6Y-5F_J3kQ_zYZf8s1aGXrCQZkRZ0yqWdUUkMqCsfzM67vpt_UNO5ZriIVI3_eNzZC0qyA5JGAa9b0tWtLYoqTt4xcbOBqkZYeylFhVHXZTCoTgdCo3aL8mLyocBf_eSxtOp1sPoOPyrbPJgy2TH7DWI96GEC2ZCl_WQPTRbDiXHrNPWRDs1_Z7z2f8NenVSXFaqL4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq3aeSrariyLCDwuMNodQJZWV4OV9RLskKLNZyZ5tqGcC5sTmiI-2b7ZlpThca9-kuLDbppC5LEq3t6rXjNuK1Yw7iWYmsFec0onwJDkkoY2vfzxQ4dsA2XOLu3MJkN2Phz4Dp9YlwfCnM80tt80LETmfLyriYIDMbhlxA0xlSsycIgsrFdO959LyWvyAxvMTZZTnO3EAtjQoH7iJ5Wjk8LW4Ed-XKuWYRd2wO4fLMhejEnQYO33qJIs8HY-zyEjWMeoF4S1KH_UnDg69PJ_rU4Wwiu6S4zVcvD8BWKpyBrM8YAib7q79DVVCAoM_-sG53KMV0NaHoDY8AO_v2Rmhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev7RFSW1pqf4A3BKmk2Tbv61chz_0b0SZUIVzcr0xHPMBE7TSUJ93qwXNW9MA7N8w_sXdnIz65oJ4Sa0Efc4XGJjJVZDL6lFxM8Gdjufdqr72geID5LCCX2SDIlqy-uxyBcN70GohHf1yYCmuH1V0TI_lpxqWBOJ-0_B2RY7isgTf7FTzDGdMkhCCumIYAHGopOVsGPTo4Sdo-5JZCM48x7JqGjl4-UuVRkHSxVRUh9PEbB6aT6b0fDkTu6ocZf9xIle6RXKDGtfEigKYZJeMwFw0TDstkqy_8w6H5Ah4HNP75AUeitVn0lqw8Bvdn2DniYJwJhNtw9YSQTkD15QLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqRiPV4Uzn68dHc3pW3zo-TeKjn2PINvh958k2afW_8RfaM4BoH8scJRiW2B79azxw6h13g5tU5kwFeOLmWQDZHtvsTNarBq2Dg_0pUJvTVy-oSHfmJy_8uZsSt4xgSU5AiCgWmi1RAFgfKRkqlqSPgOtp2495Wjqq2zCxI-xnMrLXbsVVA8AJ7VUjsAiDSxrzxEPpLc5yB7ekuOenV2YBp4IGo1b8Rr-pVODMQ_d8-kDFqwFZymFFYWvVSN3OshFu9vtJsHzlTCVfijdsmRONGucmgHSwhFeRojlAbjf6JBdHl9mzzCJm8mZbXBsbcoRQtQL5ZfSBHdkccSCTOleg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNlgchGAZRTWvo6MZTqxmU-WNi555RxbjQiTeXy0qwzmFRLiErdRZUb4LFZn4jplliezG01XUCYpRTIEQ3rc1v9jIqoOqxXbIgKeoa9-NYXo32wzuC61oydolqoD7g7jfA2nITfcs0tx39SL1d9GHOZ-YWvYqqSAC3HB4-NvuFXWY7CQHjlTNd8cTdZhxX184vzxnXdtCR7iVvnCHTgQtTl0QLt3sLvVEo6NhqsWx2ppWy3Q1WmYaDQ9G_TP5F_o-4Bioa-sFW4C6fb03VB7tTJGvNa9123KZILQ-oVyKhOpDNl6RUwma3I5KhWk_rhQjii4NTbJy7mQHAGR5OSgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGvNy23eO8M8-f7OTfxvGr_B28f24WxNjtR62QTAyJ0Kw8yGKW3KQ5SL1l4Mr1SLWboVJfiLOJQvM2IvoAEdnz2RrC5d1IBpWBjX8MOY79VYSSxUTTpXJaZRipqpf08pEs9ZlbxTCuEosQXjvDN4W2KdSBFtNrShHnZuGv2oHlbMTgXBx3jIXjLdnYLHg2VBhw9f_Go4_P-_TLc4gEHJzX_G23K-Lq5XnKIfdp2GbyCkyQtuk7bza7fbvCtNT0VIsS7uCJi6UDHLMH6zDofCfKMS2KqYXyCAVE9EJTsPyBAz_Dl6WpI7s2pXmpbsx1llaBTSAJM3dNJfQvCxf4A_Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeGKTY5HKHz9nKfBkzEBhNnOgwWK1Pkl1Qs7rwuzqxcQrnJVJISl3KG8_GmWXgwZeRARBingPigJHEY6rwoB2hY5Fv5tw_FBPRe1wwZcJ4dDoNbnFN7qZE54h3-1FmmRHQP1sD9FnkO6mIrhsyzQbbZYAx9ToSeocRJR6YeMXa-ff3XYe45cwGqB0Hwml6skb1-_29YKz5T3bf6NMG89_s7LI6IwGdK-RUVgz_E1hdU_fL507qRNelJpuMEDQql_-FKQuUysRDbNf0-BafQwirbCjb6rLHMWx7cerCWrb2W_UIHk4b9iiDOpUd3aAu2glP0NDEjrZHc1AQdeifBHGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVtJ6Bc7T3JhPI78rGRyz0YPyUWscETKF3GdbPTM8fXFB9mZKZPz0VJFJCBD_S_mHHozJATqZpb2HkmYkc4pxEsRQqims_IyIU6hd417mCg8mX_HWt6lh1THuTp64UoMfF7eKS18RJiDm83OtPsCSYGUYj1fEkQ5DJoLR3Oo4LMS8DkOJMBnlgTJnGhXjC8y1XScxb1HycAugueRKdNAWgvJ6cSB5ntfCwxHC-M2F2YQc21Zu_ez0DoiSq1-ANjJXAQjaeQQw-oIxgNSqEbDyLzcYPAEuIttGB_t8I1XG3YNYBiCo_gz3klObJdGK5y7SA-4bguO-zNvs0iPxuCreQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd7s_CDGLGUDTpuDkjJmUm2Vd-Hmnph_nBGl1T2_9lXHR9X1-Z_ZAoiVT_wA2Nxjd0jYDRqvT8dcKeilEMHv88stewThzvhdX3LZ_tGdgjoiQkMaAe02hlaz4Mmy36X2IpY_HwkUB0Kv1CXKlSkIMP7vv0f2Kx0jme0AygY8A7-tg0FVWuhDZGxmij-zLRTNgNnX_XqIqzE_qWJk2os1PBwYSDjN8hlS24Ju21U1HmJUsUhdy3CVmUeO2IlV0t5U1Vd0FsAih2g6xA1YFTdTga7ocjzbua3kq2XQD7Ku1xBCR_uJUgg7do9q3wFJdx4j3lbrQ8JAcVpU37odeCThtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5d757nbF1evMXFFDOoiTcgNOZokXribyai9aaIxitNRS2HV4nZSkwmrqkkPol_y_h1aCgUPg2THKmOy_Pl1M1nIPlmUYPiWCLOF-zCNEP94FHDJXmlVkf_TVMCiGnZDpQZDg7XYpBDYbJu_-95NDWM5W1ad3NM5gBjlQ8Rtk4blV_1DU_z9jbx1t_SuyKbiyIr_HOlq-WDFOS1z-iQM_qp604FmfzxHWdKKHqhs_BGUJW4cbxttUSZ4UmMQ9TIBIxU9nF-2x-Bsmp6nFN6yn_agKtlbZdPECe4KAjqnvIxvBC-1vPTQoPTiL950KL20RlXXJCyStwx-LKLHGgZLfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejoRgluMUXcDRRxZ6m3YCtIQGWsjvj70N7f3eS9ci3dFrMRlKWj8bj8cbZ_w2DZaVz_HMcaTAGBwLmrRwDYo9DrmS50QbqbKQ7UMo8P7AHA1uXmY3xc1WLWSDokb6Rme4r99Fdix32fJxOTp1j1cp4Cx-wzKzWV30fbNdpPrV7g8pgL6jfYC8KBUEvX7A8VtSFGDua_-tOb5C7Xe-bpJ1phKIhUp2ao1gR9Ys0S8JUTnRO6z0c7CczmPRkWYIN5tSbfEdc7IEdRjxx1YcGtPhcEpxOxd2k-aYsRq8eLU8QNqfbifZ2EkfWRpkq4YxVEqHes4n99MmrTOZ0cB7g0htA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMY2py3_E5ZBoi9A9czRxI1ooUDTVhoqy0RPnSM4pRipZhZOd3GPwid55ga7W4kbZ0i8K9NJHk-paLoK-dcxBYRxp82g4vFcsO0u3yKzd0RiAOZO6dl3Ygy5nSu7dG3oum9pNyQ13kzntPlrnVnUn-cE05flpEBT172xVgdQh-ifp3et8o-PM6RoMiql1EknW3p32leQapP2yxXTasCHiMWMxVfafrbfLgqCsmflQ55Mk6EbpIOGYwBX-DJn2AEWQg119q08bAvgNxZ5hyLxcz6B0KVLhLuGknBEDwEhlRjoueCF84EgkYdNRIVCVF2MYWtUh-TOYxCOwBJGHDWPJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxXSK6WnY6Je2Wmm_xbKpUBXLYPjNl_pFjCWdQMtE-M60gIish2YH17STb_brJkXw-zpBUYXd5TTYkDJ5sm9WH8tbY3Rl22OMUtNy9QSo6CRQoP1axPNhdLDzZTZkgMT7ALTHQARj4bXXmPVuMFd_UvOkzhXW9iIrJDBKaSclI1iDjoM5AtU9LSsNoN6XjNfi2gz5GUxQd3CxyvkxVNPtc7kZSU1gprxyBtJSUow1tcO3vC6EQKTu4QxS96pDsiQ9L7nktD0ZM5KKQivzROcZc3FdxWuI7-yGDGlRd3E-eCcWSNtJiCfq98WcqofSw-wwSa1dpI-cIeG1mItR9Iwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibBrI9u_nybdn2YLHpsu6GYCqm2kzKis8p5K1XhuzQ9QPBKj8gIgjMxfqyVcnuEQdMPmUoxboWW-1_iySrX3uN5EQNTuD_ZxTj9OWb9JHBx5vHOiaEUkR-VoJBIdINEh-CNC0GWi5TLLlkCZuvTqLhTILilieX3gTGS8wUMbgOYTcyvYojbso9CVOMlwuJEI2aX-Tqm8ACK3jxgmdD_uJkbBP6v7hRQr63oiw_TA2scP56cB6w5Uq9emZpXzEjxpxVmk-C8lDGb_jJWW1A_bAMiC2vjtHpdpDNGzxKg7dLt0hslgTzoVjB8sD5F4gXu3q2T0dKlKB1L004ZgozBxOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-toQpR1Xc2U5udgibcr7rxpKT8g6a2TqEER40tOjrUKVseoHiHrKEG1tcWLZdDEEDAdMFsvJo-D_BWLkd8lovucXtoowSs7_huNGT2HVoVLoQFw5UGqNBBNVXxaFOxE_Yxe2o4gT-E6hWqI-gkI5LNF_5T9uYr-QFj2aQfiiN2XyKEjvgTIfoQsSrtRYWQKsXurZ2Fhw9Z7uCq0lGYu3sax5nMqZZZh_B2kyUizprHxqZhOF6t4HhWHIq_Zk2usNjDtqgMM6uwkrIcqXbHuz1ixiCO7zCvuATrJOQOrYyBWLr1hIYPqbtPo0oQFpKQUF0JTiBPgwmpCV_gBNiSWgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzxQvmsXombBp89QmMHefpsgN71Z2SyeAmhNjxhymGpqICbf5SvUmduvIYtib4xUknWMrsVgjtTqs1WL3Z-FQ6vzEsrDOT0bwldrV4OSJ8yffFAiCDALAbYZVICSlbNjJhH7WaJr2_61tmvhE22ETKRQo5ZGw-DhyEBzuBgCrW7a9e5w13pIB2Su_edXp0WkgAHHT8MJiX2S-e9wF9FiK5pJWV15RWew7VPRW7YnEpTmNJFv7AUnLecStyYh9XB09cUYPxCMvdkaIVEbdeqk568r0_2mh3O5Ptorys2FAadrKrHFQg70Iga1wCHuhgr79JhTTeKR64TovZkYVhjxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cuXzTqa-Tf6Vz4IHbW4DhGcOMm9acFqioaZ_R6fOduROe6txgfzHaBYx68stutA_OIbn9Z1BfoSbGqMFuOwUQ_yFU2q7ck4e-j050i6mE2M4Qw2oxSwInk41C46B0IesWBM0gaBWK-thNlfcrRVsMlsci78JhtGPh4VwOo4XPw1pqy1LiHY1UHKBtBv7UNW1tvjgUfmCLKpPibxfNvr9nuJNoYkc_zPMFKe8zbip-JhMfyGGkomW-7_dKfXZvTJSyB85Kv16avVofwgh6Tvf64Bx9ABMQAXwFmjPCjxBedXHUWddjmxWxRDsLgfGJhw4TqEBr22NQJ0uDEu6WdJt_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkxO4sUzmXgtaR5bYPF_Nhkdvi3ooV83bhPiYHmMEnbJUUOsiRx4wgWdi3P6VGxp2ACO-HyWSCe9QZTSK7uTyNy7V-Yc914L3j94ko2BTrfgEzVOY5DmtIJjabUWfgwc2KXiJwMaZTnsAd0d3WJ9Yt_2k6hsuR-5parN6_nQLHdKQMAvPVhfSOmhHswmI-Qe-AF9ZGIfMv2YXxdynv-pOAgdVVcpJ2NW-fWYsSUr3UcDf0fW54djqm40Fc23T8HNuDaX1c_ij7CxVvqLdNz1n9-d3fmuQP5ca0tXzYDUsGiaWr3xJvlnNWpXdOqe2E5dy9wvRC1q4IL0xYs7jTWASA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcGXc8utf4cG1-8SzfcS6nr3_V65M4Bh8ffZfhv-ymTmNKLKUs4q82icoFTHC9774_NFOxAkCfnykUjevB-wSJTZL1u-J__C-vle4v9GfGgBwKDYtV4GVG_KgqoincRSxE0lb5zTr7acD8yGxvQ8XDkwqfH9IaNTZIvbYNDegPBy48FxHNmp-zQlMCjfQOWptU6ha0Rg8qOKeSEH1sBgXF6Mia3bd-QhZebHGTneUYu55_bzK_fQRwKWdbM_Cm1syCTjWJlKAw7oTRuGMeWB0FxUvzigng53yK9DuN_KdYm4PaKyR5QqNVctzWiWnC-p-SUaOWYNwwPxJrk7fI6Vhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTkEYPA0WeOTMumB5jWhZgWyD9PDElHechmPDlGBjYabWiL98VP31s7fdQFj-L30R5iH7M_QQpuNBo7AGpjBB5_NYBIlHdgzk-JSTE28vcvGOQAma9YoVLiLMVWEsoXEz_AqLrLPzN1t9qnDlhIPToqigFpmO_WF2ry4XRLzBmCYqcyHotKzTnsbJcpay_AEmieKZN83RAkn08TXGdcIU5oD2kXhW3GVysSIEXkSjDY2PTFVZVIqkkaq3P5PEA-0bwhKYURez9ld8G3MJ6J51nffnNQwwxDFqAQCNIjpu5-pggm1_b6g_zIGjPFnfKb7b54Mn18-ropm5EG1Piav7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HaZ7XL9oo1M98GTruzDsES6cOUPfewU3qRcXppidhqj4roI3aRGUtUMCbEHRWI7XQQIQBl2eme1qONpSJkb2rRnwlchqSDrrcevzmf3MmeZIJoX05fBcL3czXGbtDr1_AgztHDJApra51G4sb3B0DiuvY_9GvGZ4KkgudAk8iGH1cKsEsSd_vuycrjBk-nN2VXBixSwFKpKtNXZwFau7aajzVT1OcsaF9USFZJ_GWiQt78qby2oZwv9QJwYvMYGFWQac7ujEKNHPTZaeXSt9F5R-mhrlDvkH_RUF8Kt5iReh1JDE9W4w2CrkAUs9_fNCsuB6AC5Bms6ErBXQzcl7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zqr-J0NysTWd468Ia3R5NiyFMdGZy3F3n5lK5auq1XbBNl7KgcDutQ9qykDtxtOgBcrTfsC6H8jFbWMjM6rUUxDSoPP0dVYT01XQE01n82v4OtCigwXLw6ynw_7DFJPMphz4B4iIbHqfpZEewvFVR-RHKOei5v9ar1BS2wasOu1nilJGcTQiQDcdVlCNDaDq_ZvSH1EDu13n2DgTFaGqHHK7GeUJXDwkIHkTXjFW_WEGS0Ko4Lpq3buSqb3otdCiOIEFafWhiUR9G5OkAst0i-Df9hdBJexMDDYQg6Bx_AyH1o8RCHYOASqM-VY_LnG6xwG2ldj5ubfUtje__COrTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajAWQwh_Iksxo3UzYEOlAaG42VSAZQU2jw1KRfJdZgRsIj_Xi9qCnT9uohiBx9PaW09Vu2EvqeZqJwAoGTsGZze4GKIr_k-HdODJmvvT-r7f7J8mZOAHoB_eb20q2uWTPAkxK-15cbRooYDeWwmQtTDXxw3_PNIngjcrdisVkSwZJED3OXQEBOJHsMydANCV0rI1coC6QJ0_FTFj7sHOlm6mD_A5DKqH8V-Uk_afZc-ICTd311Om0OxJ1aJkZQwY5rfnpGyNiBwLIL8tI5ldKGE3_Z2Emni9fX6oASBjvU15drJByz7xWYQQvX8cUPxGaZT4PBq4B3on0ExMdp93JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtvTCOyNnMdo9jw2yrmVngIk_MdN55d13VcpAsdAaOy38xgR-gOCOV-RdSb-7_0jHdlZ5bznL5fsRk_MJDKBuLWljmciJnwNQs9wbPgxeDwqsw7bhATnjIpGNJaAtiGh6sAOnbDirWHNG8EvuKr6Q87LxPc_m9W6EuQEV4aQhsczgJychA9EDIWPCODr-Ex2LcYl2B-RG0xUFwDs35KAh8j71N8MY-NFP1MYBHTCiw82sh4CMrvEpG_9Ow9oGeOFav1H_rc7HCYfsxMA44bdXYw0f-gNkzpPt8qUReGlLKjrRR54n6q9ZpH_ibt7hQfNqAYDIgHWfSVEAfVXbfvK0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eodEZpN0CXeb0rIU2iaTnPVUF5m0T1v88KN8j4NsED3UHoP-AOE-LVBL6I8NyK__IBgoy7k-XQfzn9d79MeH3QbbgBY3w-E_7UU7oBMRfFjfTaLgd99LH4RjvIrZlEt5xCjKoTswfkws_dajh_8yBdY5gaqFHrAo-swEq6hUfy6khfxlKTnrLkuBolalxA6RvXILmJdRJuHTF7EhEzaLZ8uUZsCPi0UZ3g5Ua9tV425yORbtpXBDJauW5UJOpLPDe-2dmU0K1REzswEnmsoqCQ9JKsUoUeJPdRrADFGKFG56j0rcIZT-6Jr0BsaBryWxhEH-4kC6xwUFvN70yPikdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX3nPfc2TvmqWuIYXtqGeUFqHcK1xfrT-Hu88mfqD6qQhRPz5Tpi0QFIGU6MB2MAB35LOHr3jB4RCbMuyK2QF5zGVuPCGQ2PHBCWvUoxnG1fqeDRC0bwjJ-9Unrcx9mL0MJOl-zDnD87mIdxL3EhyFJb6E9PHjJAD0EwaeRK6BBByPSKfP8wCKVDERcF7ALUAYLdBudccQIN-wfofVVtQhdLjsWvC6z9FqLo9e4LyHEouzKxWIUNWNY8JXCyEB-7p4FMhbY0ZzPepvBt33PqiJe2LscU-45irKJv1tqD8tjiML1nS2QoznHBpVjpkSdqfvuj_FT6SWgf-HsryUrx-Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EAV9hAsr6fdLzU0zIPFplppPwuSLr3vvo_9zfNnWm8fZPLby1KgaFeQsxo7tu0PpFuGBchR8yjxQcR-qwYP9ZOSc13SXQM8L4WDseLtmK2X6ZVt78Zp5HJIFJk8OXHR-DYQZzvP1Q7A__PcPtcHsaTzwyV-tDSI0xtSGgl3CFWxWbuvmdDRi0t7KGV41FmMy_qiTJOJDNAjw8_gkU19gb4rOp53yGCqqpHbiYQxDPqoQLhQKdq52qiv-hR93PeRDDJ6QrTVFRdE3dLyhKX_HhGp7iNT4PQwXap7cj8HOFTfexSqU24MDwmFa4MhmgHOvTSL4hcVurcNscHUKCk02Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EAV9hAsr6fdLzU0zIPFplppPwuSLr3vvo_9zfNnWm8fZPLby1KgaFeQsxo7tu0PpFuGBchR8yjxQcR-qwYP9ZOSc13SXQM8L4WDseLtmK2X6ZVt78Zp5HJIFJk8OXHR-DYQZzvP1Q7A__PcPtcHsaTzwyV-tDSI0xtSGgl3CFWxWbuvmdDRi0t7KGV41FmMy_qiTJOJDNAjw8_gkU19gb4rOp53yGCqqpHbiYQxDPqoQLhQKdq52qiv-hR93PeRDDJ6QrTVFRdE3dLyhKX_HhGp7iNT4PQwXap7cj8HOFTfexSqU24MDwmFa4MhmgHOvTSL4hcVurcNscHUKCk02Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8Ob1CCscR8FTyBCMwifrHEibP_6Y4yKRIokDYLRAfRguw446O37zRoK87vpebFRDwK_Vb1sZknUWfoIZo7oM2zQ1ogrzpjBMNEulYR5-HCVgygboca99NEljp4DQcrG8ZHhuKtN6qkkJEhfrigKlmqBineiXpBeP2saj8J69flfXwqOGM5bRfwDysn3l0N5a9tA2YBaLQkDiauTjW5Ks5liqfxH1rRtnOWxX7w-zzfwR9-FHAf85-bf4sQByzPwadJWnZNfwDwOLyeRrXkkMiPTop1ocJjCTnIOObD-3RtshMe5IJJgZQbncqDOafIG8KhBOrapzTj5N9oKy9LSIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OejadphA3NNiVtQN-CEiGk_j-1fyWdd2i2UaTWCyS8ejIiLMewcQ7KITuTceg1OVK58aC08IwtyosMNB3LIRcKEABcZRIEFD2d-G9tmlqAZEpKcA_6PXYflCpEJlctXtptBaBZYq3sHEhzTRxqGsf1JOOKSMWlIlckKa67KS8w_gk1WOy52DtfQRQk-NCMwjVClHXye5cUZ6IhwoHN0k673ufgeHBRDAIj-Bfnl9YxdVYmpXh-qSgpa9ed13s2zLP7chID5m3bm_5SI9kASblVd8r2bNhZN04n_B0XkoKjhPu-eBmB7nieN1Rhrj_g1iewygBNUSY_C0LUzVfzoOqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbw_fi6TSTSESDgW6dSPbOdF-TBYi9T5Ck1TrlKGs_q7NoX89ywpOVnGhW7D1XXttq1Sp7HbPkthGiMowkS5o0SQcTGT69xrDefibHBmatsSaPHFzdSVbgRcD39yUWNUAjgjITfPWDvcshh0_ALano8f8e9On7Kd8XrV3jUiE8nDPEuP9UKWdiNo6qIeUjF0qLt1vQSslPfKlQQ5hvAnBxn3VJk0mPOWyA2KLzWAY4GBuOXPKtVyG0cbJmWnufxlZnY10zmFB0Png1ObH2kk-wBzTZIdo4sEuJp6opeZT3sNZGvKsvoOP2MzBVYQolOuxGhuCJ8owPX_81W8Q1BIiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rb6z7NkHbXV7gCxyMsILViz0vq8uE3nBXrTfBXcWFb1wihGToT6--EtSn9DQ5Ssl56KpGO30eUrsXFXdDRR2fDPT5AgqFCDfJ8kBleHIIJo78XwrA6ZY4xCIitXK-ZVeDWSL3I4inMXE8aplHO58sJ_2wS4RlothGvIyfAlDjT7ABUavu3h9l_znvVs55_mccoquWxwQxT1BteKQ9nNFcbDytrkafJrbIHTC0RhDJGA-sL6SeaVHYy3EpSvjtciqiSRLQ6z34wu6ODvK-m3Fu56diM4w5Wh9m5BEz3l283LoinxFlyr30jveeMH2W0catJ59TKtCOm0G7WcFxUeReQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyZ7Zhnw_BAcqhlEcTlOaCJQUMgTfeS1rfWEV5ZiBfr_ETgsClfcbyFhh74Fz12qYJYxeFZJk1aR51zLVM6ftUSSLupK747JUaCiHnEnpkQAMQUkS4M6jJHkqQc-f3cFrKwZKWNVhbErpOHisXKctIliLlXqm7RF_X1O1MU87EcU80G7nb7Yeix8t0y3y4hdvq7FR6Hs6P3VQlLUvbMr3rQngaARJGy_tfg8R9Qg3b_a381MEtjdTIAuQWfGSG55V39vOmqjuBC7e5p3C52VceunVK2IwA2z3CtSJh8BeAehPX4pgcR3bCbh6lq80w_Sx4L7J12cLVxtca09Q8Qx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Frp1as91VO602ln_HhkIrhTnfk50BSun4isSv4ZY2VOtBv4q7RIzNSD89A-lzfWsE9sy7M7OztfS7aWEiFKjP6_bGjz4VHNZiCBulark6tWnR0dwzAo78mqq1BourqiEXPiIC06VNJJsJ12Dl3a4IYfPsRL1jkVOIq0E_xpIxoa1T6qbCzte5szMmCuZp9jGAz6po0aqfLhk35nshP1-uLs1r0YESG_v15qN9kFlLJuFSV2S25yJN2HRRuBrbgAdrMCzOFKQAcBYP_TothJvpiNzucaPGH6xiewAQQEQuVHfBUrlDIGT1wfzx4JD0hvbVCyI-li8Y8vklYCHxXaF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1ol-OXkX7e8UIz7-PmrHsykev-fG9IbxM1bqwdtrDu2Kv56tpbROck22UcJIs9u8-RJaINXv4Me2C2lF4QlSPGP67Za95mJ-Ai0o2A6D1Or96hguKYM7wrQOg1wi08pQ4ycHol3PTxsCIIwNOda4Y7g377MwrEQRCTqzJM6imLErQaQ5vzgjIUUiKIduXvJHtinGSpCvzMut3Bs5ZQbzPU9D2A0pRCJCahs3wnuU_ic_Gia5rtn6jzu5jfkTeWombCMfi-a5yx_WRD5cShEmuSEn-vQ0VDDlkZh4-9pUxVsXS-fjon-5lqPUZbmQBm58PZsd7sHY6hfWiUU8ODQwg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=dagYxQcu87VxkCrC6TygQdOxv_gV1reFaLBH42E6o7O9rf1YlRb4gU3MiQvVY3LHs3JSoyRMcQJsMIB11-Ig5tgaWeWwCi6tuYSCKtFKIW6ZNa2pCmM8I3gD80uNQ1vQEP1uA00hvzxCI9_vtbzBaC7On5487CUwIoc15-AmCNiOhvA4df0rXVu1VA9ZwTspvAITzINRPPbHnXBR6SsqHxAM-wRdX48OjKCyaRJMXY4gIfDid8wrjUFKB0PrKzxPG-xgEWQnyA7l9NIslNRpjwAAzLJ9hFSpz567OlW8PWr06gkZ7YEJS-2tlA5lXMA-VdyWF3II_ALkxgZIeMJETVaxHO2I1rnJOucjge8RJwmX_vEbAD3NnFiJMalMNguGsbzfuWgHPYEtlc_pzyXK0mxDg8juLb3tTtFVCg4BjR-jSIKnc4tDHK2Hzdf25wpk9bJuMt-6Y-Wljg8NgGx7TXWOlVaNDmDSYWwvVFOq6eim3ES0gGrv3AFek1pB4UTqatwf_WtcojNjaqB4qTahJ1P4xNrXIzWT5AF5DyuJnbecaEvKfK0kYfF1ceeB3ZRDcH0CussInRCu4C6ddCTHLxnSscR3TxF0uBoqJeROLkxtmhtXdBNHZhFDq4tf37XiflIt14JtPyn63LNSslH8RlTzFaThlowKTNOlWOH_hzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=dagYxQcu87VxkCrC6TygQdOxv_gV1reFaLBH42E6o7O9rf1YlRb4gU3MiQvVY3LHs3JSoyRMcQJsMIB11-Ig5tgaWeWwCi6tuYSCKtFKIW6ZNa2pCmM8I3gD80uNQ1vQEP1uA00hvzxCI9_vtbzBaC7On5487CUwIoc15-AmCNiOhvA4df0rXVu1VA9ZwTspvAITzINRPPbHnXBR6SsqHxAM-wRdX48OjKCyaRJMXY4gIfDid8wrjUFKB0PrKzxPG-xgEWQnyA7l9NIslNRpjwAAzLJ9hFSpz567OlW8PWr06gkZ7YEJS-2tlA5lXMA-VdyWF3II_ALkxgZIeMJETVaxHO2I1rnJOucjge8RJwmX_vEbAD3NnFiJMalMNguGsbzfuWgHPYEtlc_pzyXK0mxDg8juLb3tTtFVCg4BjR-jSIKnc4tDHK2Hzdf25wpk9bJuMt-6Y-Wljg8NgGx7TXWOlVaNDmDSYWwvVFOq6eim3ES0gGrv3AFek1pB4UTqatwf_WtcojNjaqB4qTahJ1P4xNrXIzWT5AF5DyuJnbecaEvKfK0kYfF1ceeB3ZRDcH0CussInRCu4C6ddCTHLxnSscR3TxF0uBoqJeROLkxtmhtXdBNHZhFDq4tf37XiflIt14JtPyn63LNSslH8RlTzFaThlowKTNOlWOH_hzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pejx1oavgVClIzyi1zTuT-pr-JEaFtnMl3BZzUlGTLWWBYHl27mc3Dezr44AEqI62ikp-6qng4oF0fqEesMKiYkgYtyaKwa7mSHD_yp2pSbgB2DvhL2isabf8Sf5dbKW3oUQnmANkCoB0YSNxLI2-pj5qK2UJKR_H7qrAhmCM8dqJZO-RdAqadN6loUI9K6dkmzZmCO74yxPsNhhPodz9dyJLYGGXgQppr3ltMPAEkpTMNqXH1TeNNjE2iG_RyqEfYrVmTMzgl-96EmV8sE390o_rqq3z_FpkbfLF5bc3z3-rluGSfbX1yIv_eiLD0vXJHPChXqnjRY4mSyqHuccWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZS9BAv4lRqwLPcaq2-6FS-lpgnMAZl45B7TwfdyieJUph9ObTkkSsCu-sEItXxreBG7PUt7qRj8MTIHBtZ18Pc_JainkQW6D_rh7jprsU2l2EhfMaIsUT9S8k2J2WxfybMXNUhCyS_cCJG1WNDUD8FeX4CrUexeqryMLHz9HnHrGbJrk7OZZG0CZUESGSmIDQJs_BqctZ7r3x86G_klb63_EuKyV6KU8svJixq1agmhcvpxR7Iexxg54JeezndhClZURRA9GG2f92zBN9RJrmwfvl-3Sfq_uvE4fTYqxfHRjHVepS9i6fAWvaNzuhdSSOB_6k1mWvgQAWdsbnFjFHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwEwNFMwIwjjjwihSt-JmmZ6u1E_I-3laMQlGpCVIW45yZNEAdgXHXjTVbK93P4WL9nxf8uBXHgu-6wBkeYYc3DB5qcum5qWdIzzsCbXRcbE_70cYwRc_CIgXJ4bgfI2jOv5v1kk3G5wjELVZkWqF1qgF4JL5V2GkzsC41o1ty2-y6jgMfjvjIJrio6Ua4Qo1G-nLG0aT-kyaPffz9wkEWFJrGN65hD8O1bfEqEIdI8Fqc1r27K5_Gsi7FSR1WBjkGLmtiQJF3sCeDuRW8ulCjMaqcBpRIf_WhUR4knSr2fyYrQBqoFFNOaKZX9TJGLqW4T74ThUfaBLknf6_wMsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVlbJQLiZHfzs69m0Ve3XvRuGfeieyT340oM-yEqmvjf1qGOrcDUBAodIrqA3YePfRL8ewwjcsc0-tdk--jDItCKBxRZ8mxXceKxE-8OwQwhCm2aw2PUN2yBSDZoMGhyPfh8gUMtuRawokpqGHe0Vp-AhGVoc4bt_mM3JrIZ0a3rqI6Xl3ZINQ_sW9G-eMJ_Xs7nXTPo2leN14grWQwM-XnPfEKFaBhgKkHdHwACeaL1gE0ikXm_Ejxbci8OG5RUNM0kkRFC4lchVVyHZDBJliVmCdYFu9nkmFWSnupRZEUORntQqEekUG8lBCOxr4itde1QYeRbGJzBPXAcng0ofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIeigL99ptOas3QstFhhkIkClIMJu_vyRA_PUBK1jjROEH-Sx1brERBIFO_kbbYJ2K-1x9wvTOEFtg89pa0V147KMTvgrAqpwBg3tFhA8aHbx4Az5u8Ia6sybR3edDDqJoe_V7G4jhh8xBmreuXgRA18LrksPggdtRpOVykuGgLOeWjQ8-5LtFBFUT4ejsY62SZIxfhhD03mAa4Fmrr4fJq-t-jeeB8aEivkhKnfxhh-ZSsrgDVNmmktCL_1tNstp-8iao-ybpmXw2E75hjlw3f_xmchVIaCaF76CDpxda8oI8xkHqyLEZ5YxPv2s2IK-X24YdptFw1npxT97d7Lgg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m4jlX4LC_HbFWbcdoUEN4VUOaoQRJkoXDkNNkgJQSmYDDn_EHgg68JERFOcHwCIMmX5T10VEvhKLbPdCkgLwgLZwZ-XmvqhXLj8MP4DlerBEvgnLWHg1akeuxd8CA2oA9otJbfxGvImWsCR45Lp9zpV9qOUHbb4_Br58MOcWFPE7xa1o_Bk_nByES4fSmbmWS6mPdKA0zUkbGS3l8kZUUbrUa_TUc8KyeQ1sjruyvUWDPfuCVv2HgoVTBjQEaj68jTTKeo7deaPzUsCaD_yy5XnSOHf9rviFpfeIO5IIICRx2W5hrK6679RcaMNFc7wI_tBImWNdniscFyTeD9Rr37M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=liWqRJtJwWI9X0sCIC1jccqD-lk9cO6GEO9z2j2XUJQ-M0fRvEk_KZEaGFti3jwhFMuwt8LAE4aKWYc-jI6ygoPEwpTZjuDBJyiIRcBrtRQQVRJighccV1lSV51YlKbVD_SjR94wqTZhHCiK2paoCR19NlSCokHJhW8-yB4XFpR2aJcX7fgnUO_EMCgBjJIFeFdTd6WUfy1CQ6S7lz62TMn5Y04a3Cpd18QOZBf4sPsWzPQDg8Kh8EvIONDRxwqdc49AQ-iK2xHBxIHnOADN3hLoKPjPO7ElaVVp0oKw1A82zcO4zgMZYxo5m0ZFo0mvN6Y9PYnIv9DQ91Sl8Zz7m4jlX4LC_HbFWbcdoUEN4VUOaoQRJkoXDkNNkgJQSmYDDn_EHgg68JERFOcHwCIMmX5T10VEvhKLbPdCkgLwgLZwZ-XmvqhXLj8MP4DlerBEvgnLWHg1akeuxd8CA2oA9otJbfxGvImWsCR45Lp9zpV9qOUHbb4_Br58MOcWFPE7xa1o_Bk_nByES4fSmbmWS6mPdKA0zUkbGS3l8kZUUbrUa_TUc8KyeQ1sjruyvUWDPfuCVv2HgoVTBjQEaj68jTTKeo7deaPzUsCaD_yy5XnSOHf9rviFpfeIO5IIICRx2W5hrK6679RcaMNFc7wI_tBImWNdniscFyTeD9Rr37M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkoP4gOYCHBdaIKrBeH-9zXcADiLEtDzcB8w1EnjoK6ZJTGcLkMVYgY5IqURfhUf3QWLxr4C6_W16A9JrsI9r13_alqpC6dCYfN_PkZQ9qeBZbgiu7ue_1bg2bI7DCC9YCM03mvtYRKR8WlfPW9WWUKHQ3_p2jZb045u8hbFtYwn3Mg07sRINhMqbFSN-Y6mGe_D_vX-GqMTjPLoqOkSgewrF-47vsuCQ6pDEezl2pBRg4kqrxOXrXyxo57xbvz5BUy6gyfnr5fMUnINYlTX22Kuzo5J1O3PuFc99N0j6aaEBFEtkQs7ji7MmjDFLjyIu1_6HyvplVVXa2EflZHuXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLq8xDQoNYovZerww3QLYze-m75bttW9M0BX_JZuYOjX36yVx5GI2yvdfI-js1k0wzbbYF11prgr0pND1c3NwnjIgyaVJ1Aku2BtvfAlqU83s63UbyKW7wqkwIm3A8zk4R0pbUjKRb0ooOI5QjRVqU7bEplQ5M236U5Q8pTv2twDeeAnm82MgW-NrSXK_BnmQeAQfBeGowyUz7Dv7Isc7qC5ExHMxhbplviuVjr7YkxX-wT3qX0ENFcvgzxQskdIgNPrmoAk_un-KJ3NzmK2Bj5elnMHIRFbmi0u088rh1n1EOj8yy-i_bHS27m5jKJvN760dSzpclxuD6M-8GT1tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG9jOYwh3uThT_aGu_frw0UQgHi3ZGAYLm4RGbu4_LvPNGDYGsH_I_v1LCHiCB93Me5Zf3pAwoucxwbHbF0WdOuu5QAiUb8Dg6w-nDDpL-gvWlvIsZZ41CpxiUq9mbLBmuLhV07zkEp4yP95zOjlET5exHXe87dKugEMzcnYQgNm6HcUYFHm9_QVULBU1Q8gvk63TAp9kYLDhuZdyLbeYzsKjygzujMP9_ETq0iHhXPymlIYtDzbqXL6J-_TZ_NkHWCihy6rg-HuFysPsosSCOkDKNr3EaO6BCIYg66y1Fwh9cos2S-Cb2Rv2mxipkEJf_QHK04Ml1fdC57ABdiZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVHtt-EBfS8pkcnjJUJWeMORedAMF4UR9FcyU0C72cid4xBLzIPIBZz0cFb_YNV2UkYV71OO7DgBN-X-4vPqXyNwCAryUeMCasbicT942kazVzbuzmNTrgiTchBArtKlCqyQ15mHt1oPJUK4eTh9IQDsBUABV47rXU4U1CUWlJ99n64do0DXGyWt03s2VkY03dM--VNgMz3zGBzo5rtB4KBjeUYaKgX0fPj4IHZcpPjlzZTJRpv0f4ndGnQXz8dfMqGqQn3m2quzjz1uk7qfYJBxRcSiHcmfjy_N07HjYX3aQIyulL99brPSXzizpGM25hsAgSRKBiGGi5t60uv6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T87jBdvgCc1PyrTzR9tkTrj1TqtN68d947AjS7cPvii_vH-kuMv7WqCOyz-LHWCCSs8YkGuSDxpV4ClIR_V9lC_padFowlmjuWUMRvnHWZ-GVvj_hHh0yQ1Cts_4l9bddpGk_AiboVybymZiU_sHPN9gVyGMl6voTHFA41GwX570nnxuKb9qHJgnIWZ2R40dvpPJJYVhG0NXh-7Cjk1HVLrjwgmv236SQwln9j82ap9SrxVOnHAqZJsaRh7aLB1d8j6ooQa1gJ0iZkscwRVfm7584tDbvQWC_CECu_Z9AGQyJPakvl3cags6oOFzBzi0BPK01XYXiuX2o1JwOc7YTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcojQ6HSBsJIKuaNlpIEQizxO2EpUqBjETfUl7FMKayeKtkyY5STsOOu-5KOHyqhMM1fi9_V1r9WJX7-efZwSDd36ufBi_P0IYv5myjH_KCKOdH0KiiKWAcED5z0ULAE4aYngssL7x-ydeuEWyatVQrz_TgZ_dKjjd6QeATadGBv-aPCaPmJq9RjroJ6L2hhIGz3ktd8MIaglmFmkecGB6Pl6g1AwVXRmS90YZSC6an6rs5TuhKeOZKqS1Fs2jZfMtneP3g6VgmzRGrdsulOhuth5jW-75aTmpf9oWQ6Z_d6vfoqUR_pH1hq1wxd3UWpNaUdjbquB5ICbc69P5M3WQ.jpg" alt="photo" loading="lazy"/></div>
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
