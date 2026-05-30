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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 23:33:29</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 270 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 447 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 553 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFwqhbAgG5EutvcScFNWm3a2VMU82ws8ATUF9D9gDWq9yZst6VtXq7pM8tprLuwaume8rZ-ueMPbfBfp5zGhZqw3ftdzbK6ZW45eQFTUGg8QUAvDMQ-v4DZ4qznXL61MH6P6lE3IRvL0k2QWwvbtgvcx5iLLklV1ZBUvXgo5-ziib7-Lw0-XLxpWezm8NZwur5m50p46ehXNlOTcFd6_I3bIYVaKB5JzO9NXz765u4-HasTW7v-ldxtV10TBBAWNYOI9Krn5-4Hbdb3hoTrK_2PQ0PTgNJSyVk2oHHv1ch5itq56_9xzBpe2pf31n_yVKb5STpRxL7yGryXdGEk2aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhDVs3y5xWRRsc2KGYvkzMSG1rrPjgdFwy9K3JFU0fXRzfykiy908n3eMrU3raxA_MjUUJ7M4nRUqA7f09-RUgjLeoRMTevgb-RAiwerwERu7fD-U3mRCPiVNjnKGIgLqO3fUZKnPsE20QXMNN7mzW_Z6LNvncXDjEFEtU6CnvtHNsI-KolGj5825-i2w6C2WPCo4lVqQKS2WUA55368NRjfi9hPawIoNuafyuoYRaMIfbfmgnWzIs8_xu_Fm9_p8fVsIAGPubYcM-hQp_UlNZxwJ6hZFofAJY-LXyHVFr3UU1WFRKdUSj7Ff08iSIGKtK1HbaoyYNquCFSpFErMHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e23UCXZKnqr9sZm9cVOodPRxJHIAhvuaRY7m3U1ohDya2UEoe9K_rKzj7ehCE0gq5nMd5VeMzsN55we3kxKrVa2J_MXhHDhTPA58G6Be86yrtZI2XPYPQoWJY5crCO3dTTs_bXVpz03rg_ijUIw58eD6cufUJhOZEfw7NmImwUDJ0IRmzviMp9XwSdGdWHdB5KW_4YNQB4xEHe6uQdbY80AKPwf5IBupui98KdVbpPsOdkfzOXdi8VHo0xBO3_bkb-n34Fn7mPl3HzKyPvYXxbhkyUQe_n2CUWvZfz6We_REOnb0ftKKCZkcWRRtRHp2AaaPhOFx80FBzNNKc4tSiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMNkg96zbXqJ4XU0mJyLmG-GVxCimUx4OfxykFDIMxoVgJfAsd78Q1R6O2whkg8uqV7iANMG_Uq52Wbu02pQBQXcP3GH6gEBfV_HNUD6YG-N_WBFbPQsB0LebbdWXmDDLH3Js3aswe4KxHVVuZYLBSD_rz4fjcqoMMi_WMpGOxw1VL54cLyqbBx0PVpnDCzySus93VSZC2UO46v5S7k89v2xLlSEIBbJaMdWYlcFa3foSBF-5tbEi_gMQahIFgFZNKvJEoL-849bPUHdRRgxSQH7iC4CWtSzCLdVCOft5U1apQ7Ykt5FFctLgIz2GWdgow1gMo0VbGWlh0msAYITKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aERIlaqjmUty0B5Ru5xKxNLqnrDBYmLsFC9GAxKj4PExR_sQxWVC03jWH4CD8Rq3pY3Ax5Dk6MWwgKt1cU1pV7ISR8G3ZX1hl9AWy_1l27WHVvgFtI7ft7JXGyVQC2_zAAFDPIiqSlT6jFw90A4z9pwz8g0jP-aPAOGbiZ8ey8ZKfjydkd9KAHEquqSoocAeldVvqKefL6kHIG2lC5GWLzUv61Yack4pwirI0n5ckgyhRgH9aE4hhpmt8XaMC8KbN30GAgRG8RoyjAIYTTOMaDXHVX3yGjcpmGyhGgm2036YChNUBVIayjCQT1vCZUwheVst0RVQsMDPYN1FOIKkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSbBLrJ1OLykkEPi4LoEe0b5Sjzgr2kb75eizH3c7N3QLbKyw7LX17AE_YgdG1-G9v4aC73MXAJUbuwHKtnLVekLnVyiRZqKIKmsVnlBwyhQ6cxDwBntyaI04bLoMPtzm0q4xZzdbzYVZG50PYWOGpc80TrImK3G3PPUQExS4GDhjcEzpTQ1GwS3f6QaFrnBcYoUQahFOBguDqmwJ1QmzI2YfyLNdX1HqS1_FWRdyxvItcOS5YTlqdjVLeFnFHGQbjcYiVKp2M8BgeubUf98LEFZG7Bjhxn-OUfQf_-9pe-9I2auBToNzHuGyh5AztjG-YgomroN-gvFgdDmajkM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvT4c-IdMGR10tysZqy-BAPzEkDiW8knxSYQx_4y77-LFHCxSMa1hKCkjSt5sJktfQRUkxiGYy-NslP2Mxs2KnB5hPNLtTJWbM0Q33zCdrb7n2NgW_X0GajcIUl8pi6o5x1iI9ryLQipYNARaWKat-advYMJlGobmLHVrSV9JHxbkwYGYQlDMb4wCW3oFGoJY05qYXJOxgz9SNkN8v1t1wMVFFgyttMT5_zExSkuGGQDSN8TQaXcm9CMLjN2S8Dc2M_kf0XvCGHTmToZMP7mImeQxBobyi-PApq_-fLlnMeb7S3vzHIW9f2zRbjkOdT6DbqNtrAFOb4iwo6fK25HuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0BTzYizgbwKuKu_Um8HaHhKsk-NjG8vXgCvvK_nGzhOEQ6uFdCGsUcrs2QqevuJM11djt5QPB93MHHMjagou9oKwqUxTRxQaZGNFtJUbuszc9O13cf_WnkG8bkmKIgdjYsvICLf7H47KsHNoSkOAceXtVBSvFyItsvWmimIS3rJChHGcBP2hBOJuha7QgWs9Neq3CixiSM7iQpwVuWjYWWwXdF-fxh4ycVFcMJH7W5EcufLUjh_gVu1mQ-1Cg9n4hEd3Z-OjP9bO20hXjHq_glf0FmwSiVDzsWB43wCgXXwy9tQ6qGMsnbdpwerFYmfPqNiWTSAJ559547VYAADCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=MXA0KoJw5M_y-6QtnFvR4fqZu9MQkFHCl_dCzD94__TnlJOFOYm8bE1YzTSxWEhMO4BjMUXREJT_bSIVhKBL00cdCmZDM4uYnz-B0R4cn6HUmeTL02lQm3mRSjdjfyn8Tthb8dk7kMZLVvx13J3-rJr6uIkO3OaU6hGIZJzCNke_-MPKtjjmvLfuu4NmxLAa95seQseQx9a46j_-d_15E3tMQhW-F3JE2pUvxjibUHb9_Y7nUcx_gi7-LACYAVjBSP0gLtS-bPn5mOas7DcYy5YAqRSxpt5a-DM_gutUyBmfxyHIY3eNECrFYcDN4aWxZSlCpYTBvATmVNSnMnhl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=MXA0KoJw5M_y-6QtnFvR4fqZu9MQkFHCl_dCzD94__TnlJOFOYm8bE1YzTSxWEhMO4BjMUXREJT_bSIVhKBL00cdCmZDM4uYnz-B0R4cn6HUmeTL02lQm3mRSjdjfyn8Tthb8dk7kMZLVvx13J3-rJr6uIkO3OaU6hGIZJzCNke_-MPKtjjmvLfuu4NmxLAa95seQseQx9a46j_-d_15E3tMQhW-F3JE2pUvxjibUHb9_Y7nUcx_gi7-LACYAVjBSP0gLtS-bPn5mOas7DcYy5YAqRSxpt5a-DM_gutUyBmfxyHIY3eNECrFYcDN4aWxZSlCpYTBvATmVNSnMnhl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AazLm2lNsZl5nNH7_PIhlxxfsF-hEUkzCIsPqTrCp5ZJIJ-c0Pft9JB1g4h_30whKb5JZqsaVKA_JX6-AzUq82OjqTUt7I1QR1x51p3XKgVAmGcZMiALoZ9g_keAtnqI1M2-72FchInjqYYuG8ngVqmYUiZsJZ4Cm2i-Bv8iLjCaauVRFrW8CkFkkYflfI3sH0Mq6KYMbRR_LkxFyFiqcVUedrKENDITE0zQpezxK8L4GrTrg8ryLqlBaWyffATGc3sUMzWoFxWXV1kAxvImOCnrFJb6BZYZsahOcrkRmxhHwyuflFuAesn5rt74lRJF4fuODbWz1XwinSsgIi5lpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8_dYsGYxHOr1-SMvFPQ1BQHpPpjGvnTH-EkcwQ9Ykpma2XZa8pIcVzBCU-LsFtitEDx9lhE4mVVdLUIGULJWZo3x1GtetJfTZzp-7zaYoatR2LlXi9CluDU9ODiUnTyT2VDlhvLzP0Qf_AVxbkBIKqNv8g-RUUHP0Yo3GxCfh2E1DOVgw9JPvM4OXkhGwTixj05r3bhPDbHZc9wegwGH3FTpLAFqKjaJmzNokENxFI2qYMhrvsCWVFysOPS61McRz2vYlOLoSsmc1To_FXFRwsHV2nvI10iAjrMdbC99PmjN37vcv4z1JTMIsPuZ7P7e46dyjDQBalKlpuqejZG-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcL9latjRREp2dCau8nM8bL_Ytdpz1AnKj71eu6dMeBgEs6gzBtbBD26gSlgEeSU4bfOqkGGFsDDQ1MhS-aK3t_RoZGb6AeQOuvSle3If1mROAXJd4j_3mKV_hDnelOFW0SivpFupRlZEB7J4FdVHe68a4wV9meWJGVMCubMPiEw9bxRNLXZPwmNFQAAdPIVvZnQJ3UXqxkLso5DKrcmLttjA7AD6fNIOjqkxbz08NUFntg4repw4DLATHSHZtuY17ShU2YB-wJ3UfdcEIbfyDZKSNv8onPPX08rDWAcqGbt2lTpJOs-Mt13OmTWnF5-9773U20dm2VxFMkPFt2DVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLz9H3mbs-a2_kNJch8yJ9DXbfR5c95AyO0F-3mxk7t7-U0brHsfX3PDmO_VJUGxucDXgJWTDtuAUzqOmkYP__i2gzgLRnDebDt9ELalBqkWiyA8zjLMMYkkmjKkxyV8rrAJKDoWZBuQvLB3kjMfwApS9QprMKW81rQgoeoBZSxNROow0zjiOHQKSa061rG8sIQvaBsuhWZCIEAw68mDL57GlQKlF7ivZwFfBksGMNBX7na7KfGWUrcQuiiBqxvBV8dpmaicB13tcH4CVKM2kEvNdL8s4lhdIwvFYVaSFWoDqodcUflKwegaKk-rpmVmxgXOLxE6rJhqDzFVeKGriw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur5LSl3Gsu0wC9tDG8x8ck5eSChXeA4q6zdkv6KVdkDxG7tAWvMFC5VOJYvo8l2EQZjNW26aNuP3tJjZ_C5_7u-IpSNaH09lFJVQmsSbD871GYm0hgUquJEtis7NnT3ogxDaAd_H4SsU9LSpNMQsNJfYrAEE4z2boOBdACg4tTmG_LTV4vuFrnV6ntXPzvTusIM8gjPFWP-kSRCLzyl-Y6K6uJsoXZ86qnw-PduoboQ7zkuISi-_XLI1fNge-DEklUQU8qZlEpl4CCtuYT23Qqy4qgZybOePz1Lnznw3hxN_SW27RUqok_EKqv6ONd02nNYQj3yjgow5ZCcsXurT6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHdOrcWpUeDWPEZ2D8-E-AOU7AOZqi-Gp-GlkMQw1MXTbF1xvzJgeQv5-3dOFGuLKYF5ncWcwsjolM_u7L5ypEOhLA-vtOP4cgJplrgid3OAr_HmuCV_-1K_UzbWeOESGNZtYMI03tWuicg1Wht_eqrG4GBaKhqdUYZQ1D0d3cFLIQXtX08613qhSDBnPuqiR4pack1X23phJI-Mgtt4PLyQs7XgTOtaG9t8AygLZxyTK8PdmBgZHifE930qlHiKCevChUYnndZ2fbasn8dVHLB9enDP8FYuBEBsN3-QfAT1wSVWxQ7CRhyBGtfWgRjckbMIFFpUHgiV3k68_q2pbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWTiQZhAFKCQsQpQIg4ysFqrKJWFKCsi1qSav_IqAnJtxLPiQ5scmFT1ue23-J3X_vV-5TUx8PWXIVW0FBxqSldyHgffqH0V8doTz-7s_C8VqJNlyW_rIvJN2uefhK4l20bGGjig12_zorUyT2FDcYpVn2nI1gdgHtxYiGicZNaaDv6KyyUZDBbXcc38zaAOQb7HBHsJjNQMRD4ezvkoa8nZb7LSzOYXxD9hy2ajyxPebHp2s8eNEJ5cyOcqIXUbb0f8rYqa0zpI1KqIBl4goTqYCMY3ZaDr_VGlEbnx-HTUneA7wvjqpWYIMDXg-6DLhKhRIKGUSqpfCXXGe-qqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCGdM24CwcdjjCLCHwY2mfqZ6HMMCZ5hi65JGoZeIi8qAlnPgGjxXEP4Ny6w8EmCJuCExAbc5QtaxrF3HZJoc4gK1nIUHYn6-PZxCD2YDglZSwSe7Jdbxp4NEWigA6y3isRlVXPjdc525lmSAMXSetJpo_CcAG9PqmzWcPXsq9FgqMMFp191elx61hCDhay82JGwrdVTnG0wWWEKNLBvDXvAOpIrDfymv9a4dWW0kSu7-cyrNZWphT_5rdsjb78j3dUpbtsi4elS_Dlp2wVbCfZbakJqjhR6B7ou-qYBcQrPkP75OXihZPaAYxHURWTAA95zLilakQnOygjtXkBKxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5Ub-6-dtiH0RGAUW4Ks4oeN8en5fFeoNUwyaO-7gTsynKBsQ7GvmgmUqBi5lZaDF3AX_SQ-P3frgwyMl8AeInLjuLKwoiU1RTyxK-rGXYfhOW0MBrHoe3k7IcKZysXUcufhl993Zp2NJxfw6F-EGG6TUTPH2Ulxt8FBxQAWYxDcz1Cbva4z2uC4-pmtluj3jmQ4gpvYMT74EevlRhrfLlYYlmhauzQNqMfSHNQ0ZboywYlGPraKQSn_PpB5SQ9xEldGowVwxQaHWGVEKj12IHu2N171wHnmOMy28-qsKn_qv7sFOpCDIrXQXwN03rBFafX0l6rdkiJqrr5uTr22jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPNh6N4BPXXyJa5LYzcGBVe8U8r-S5LBPDMZw-JPbrm53BjqNsJHK0VRUEFLhak7vsCIe7eGPna3mC7xeAhLJAef1Z8jS6yjpepK900rNA_DFKgacS-7CanFdLEAR9_IDMIRrMmIOiRYYGtb_Gk64QrBgXbsV7ak4MJrutpA9tMVvB-1cP-ifcpq6_JFcfgWVEhJFS8m_Y2IRTeyd6a8o5bB1NaHocfFP7vIhLwFkhoe_LdFV-kMCBB9B219tB7MQchHP3vKhExUbsrZYM3YDNQ44M5ftJUtdbten9ffzbdBUH-xospe8IZuFDhd30aL7gs6SCr5Cuai965WNvE4xg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzPlMa1JD1a6a3vxrusNwGwuRVcgErvAIBmUWh9-fOAvy0Hm7eUGQKOXWhzVNj-ofO-bvigBS_WXSz3CQORi6WH7UomlLtBRiONTaSX0ZpjxJOaFlZzTSC5D-wylxpbGHGA47bC0DCu6usA-N_AB3O4N4j7-odLCRk4rwCbVl2vqQvWomiknZevKOIGl31cl29x66nbWjpxcmyzxwwHmW5MqC15QuufBzURU8FBU1Kc7MHE1i5TYtjJFsdFEIrJlHPOYo-V-CLTGty17bXiBG4A7H63_knywLwz8anieEnoh32qfZ0Wn29RBV2Sqtjt7B9ABt61SZcSK8BuIygpPuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKfquisO0nS36XtoBEAZngzMJQF_P75iVEN7I5Vdq5hB_RQhHJzIKBAN6Hr6dqo3C8OgGfZ7sF9rRSwNAxPuXtPp4roO_Jxv8xLYpMNP3lWDZFvvUt7A475Psw-bTr2uPOl6_bMrRNPhXFZT_A3N3Lv3axlV5O2wMHwBbJwVcx5jNe0znVRbSVvOLeXFdA-SFG8zVFAsFCvYoWK0b5dsHfDyULJDi7myyXqkeGMZmfnumEd217OmVkW1XoLF263L5FoGIOXl5nKm958akaVLM5ZYfH5P2MPurwLiKXuaA0MPANvrze3mYMaKQPwOUnSvXkt_r_ksl0awwwHmgHPD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZlR7k4SKxevc9FIobPGQ3WZX1Ndb0_BnXBpuEdVi1B95OcxDWzQMG3pwim3kYdD8KBz5ioUR5gzs7LidnWV59gtkhJq8CFxbcohsS33uMHEQKZgO0kU8gyIubWelJVX2Dx3aaIThRkbGUVvyByTV2veyQ_PymRCS_HSHkI_OTipjDcTRBKNPRhMSUOYXhFW4aLTIe2zsxWUSty6gJG9SyxqQVcCeuoGf1GWxtYhdAWFFRWMgbqEg7c2SLkVtrE4w9xaOkegZYiXhK2a6g12WGhaygvNQXS47ar_4MKTYrI7xYyXfZ6p2ABxCxLW1wFTrNnsC8lVIgIlJWeCICdAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSmF3dMX0GyTw2PjfuV_C6VKrj0ANMewNJ0CTiQCl0OQVcn3bjuCxLviD3A-SV5DMeSoh931vp0Dt7IHYtgo5awrNgMcaQPBWOXSZhtqXdtRTA1ULrScLOsyktAazcbYzU0xNinpdcU3PB8UpbhteRRhSUqEy188GOX7cilZ4GxxH1kF0uORkD1c0XT2s6SP6BxqrCnOKql0srsZlHQZDNO_eGOaX12KSypyd7wCj-VfwMcYGrj8-okTp5HDu9mz11MDye_GSsr5DzxGnmZQ2XjAyVd12Szz76Of_BImDg8qbWDFe7Dk8pLka1fRV2FXp45lbweo7SivITTh99AHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZrVHEjobXCWyfoaBm6YiDuOBYP5Hybb_nmMmOOp4FWYn-5aDDLLblG-RYRg0xVXI3yj3larkWHkIQ3ocGMSU_z-9ij7PMq4QpTGpaq4TW0bGHhp8DL_ihZNeCz3vnpmZ8E3B-crK_r8ZcM0R7ffrZV-TtMs_0355ZAZ9YSwqj8k4WIoPJgy4ji0tTQx9cjZFYBU7w6Q9_tXZGhgWFayGxM9bKlQHj3_Lyv18IfZtQvzRE0ZaCCoOqZSJRypNp4sIXXkT8Ey4Tn0gfw7R1syon7a5ftDHsKUf3RmsyO8c6iFafRhYV2S03hdulo4IDVNZ0_sRZENkjhkgGxNljqEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnZP3fQAeOYs_ZXIYl7jZlYkgtkgYoK-0s3-gZXabJyYDwnlvqk4IsgQ1ABNNlNggRhIJ49O0znVxMp4C9gydL9Y8NCbbKbCSlatiwBGJONLa4jUB9Zwe1LBbDTi82w66g1ds8u9aIIlbPM7UwYkz_wwD8LvuBR37psNht_wAtM6iATwp3hwVUcEMCdfaTAd2sNx4ZpU90VvwMDVmSNw4BS6uWTazIn-5kfQQeW3oEgBEDfOGFIu-nEutwtgc9uxNl9lR01mLvOXeZPj6wD5acKx9uuJiupJQApc_0Xh0pQzRKpC-VlxTCnFlxRhzvudzDuQ2bgxizdJW7TBd6Y5mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMG8h965IMN816Qq1vP_uPqj4nu_0Smch6Iow37k35iLh-KLCfLI_p_gQIrN1LldRAuem1c3MOTuES-vo519ajZZ8KPaDHXohoCRpHV4xeDe2jxV0Nl1227d9UwdqdJB0VO92lkINIgGrx-M_AA-ewnl4-rs-boO36w8l5II3eMVfGcklcXM0hv1R4rFwOu3kxJ2iUB-suG5Es_7z62AxKBtjJbH_Hwy_BiTQor_hbCP6emgsThqtj6UIF4ciuxwFC4NL4oyhfSZC7ECIAfPrmRBwF_-2JIC8jr-yHogJ29bufmuibN2JMHq_eoco1dOWTsuLTt6lgIVfX6XKFSMfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyXDnZyCOY5x3-jFTvkFtVL_oygoDLNfoef_35pFBRH26FgcxsBypD8hWD37Rsodld_MCJnqf2CEYKfIqEtUtlmCP6p5z_Fnw56Ga8JM_XYYmCCqrFTbzyunhF0C5b-XRKxW-5YqJD1CY8xXtJBGWWAdTmsEwgVBw-MjQSNwV-xOeAo6GPI1eLvhqiqsHZFDl6TVoVFGbG1j_3qhPiyFj8gHxBZp-frLIyTD5QkYG7wMb3kc5gwljIRxqDGbMH4mMz8fS9fZAiIfhP4PAECMpxOauWq0jSoBX6wuI1H8HgVJQYvlKUbORKkRJjkVWFY6i0-HmY1rJNJr2Cgn_a1Z4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QouG2b8wTwARi9ptA9DF56LN_eyOxU-g_QwFMM8GBENt1w-U5FHh2Z737Hu7186g6EtLoA6vM3W14urMEoL43m_UmoRPcOMaz6UrQHYiNp9PCtbW2AzE2cdB97tPgAz-uW9vlLXlLNzRIo2ATiSh1cRn_MptRiT8jgEr81JfY-J_E-gQdvX-vLnF1GsgH26mmhn2QlnQWzisyN53I8ZrXSAiuFiX5cZ6QgZQUVp2qvHlYbTRZZ29Dl9hxjSoPhvmDSYvbqMq8LQK1VT6jDmU2DgvbQGsmBXJ13GlQqS2tfXI6Nx8FXYTbMJJH-9U9DewSsfzn4Z6WQeCa9dToZRgHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNAMtfsZnDU3Rfkuobrxw_fjE9dZoDYVWvgwymb2VmuFKOF38xfTCLenp2cqIU_J66-i1M9T4dtlkj98tZsgLoBZ0MDiWjjLmo8JVeihtgLE_Vki7JOkrMQy4FE3rcuJ-NQ0RnE0AjqyKqeTxeVVbftVOH8r0AC_YbIWnX21-0EOqUf4eqOg8ikiKeraiSapB9O-YecIHsHFMMymWS2VYxs2aXhu7z_HBK05DyYpCp4prhFHV-tg6Y0beHrGjWjJeadm76LOavqWCmQsVujeVB1sYgbiJ4pVosrpyS3k8HvKTdGZM7wS1BCVFr9YM-JRVI5mAaAtOCSAojseOc0bFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2tvOHDW2udzZFcqYahCaVDg_t4gzBpqQNyuc4n4ri8dSgeYSBgRboxXLL7UEHEnpxqWCpRqFcJXiC7KVWq_13DCH18kKnxKJLIS3n7OzLwfEbu9EcURS07aPDGpnmEKUht9NA8IIBMGkCnabJ8cyaIWIym0XJiVSVE4e6nSI1QUQWu6QSab4AdIf0A3ALyFB9iD33izhm5SjnTVbpNvOwxYlnBy1KDjqqEMT4cltGKgvQJORe1tGX93MLbGWqZ8nrU71O1F9bkinmwE7mwhW8BZrEwrEBkK7Owa565_6OVy8p34BbsuTzHl84d7anhxGjQBeRNtuTy11ZVtEDOAgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pal1p3Wm31KXQKYmwtOkm7USUOI_7Sn-39zqzP5b0kOwujJKBTAhn9radyn6EkpPMcpPbDdtVfR84aqZwjklEEQRb-v-R8xvt6qNIydx2it_9ou343YFivDeZ2OdOA_I71qVT2Fe-uhAMcUQpGgtDPZFDBi7cWslaugSZbtbBNJgg56cmNctXysn3Maksg1hgwJ81YYsQfqD8ZO8ojcEIDSlFK310XHKKArXm82FHca9xFsf-_DkyljZzYT2hGB13xvNM6tiF26-9FVLwcph7zKG0FDgy6Q-_zIBN_gGQB4qNTpEdwSmSiuHTGPmHzfeBkszJGJSkPzdqJuhDTh2wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io884MnHNPQiaE_ygIBjR9Hji7P4HkE_05-gTdL2y3KxR7q7LxZnUpBgL6GiEozu1HV15lr2tB9lXqFKqFxpxcSBXgOBHLQia_KvhFXwcIWLGE4LS3pqIHzpuhVWB81hyXwYkTpEpZ410vD9Lq8h_BqGzsuDJ2409mV3yAnPkymhvLg5kywD63eEXBGV_ofqhasPpjVk48d3EAoCQb8d926Ye2wxZ_YSUAvBILAFRvYX1mpsE1Osi-ffZQ2NETtOCnYSrKomhQt25C-WbCwBgH8lg1UYXfKQKh0jwhIzMW727ZxKDskDIN-qFbSuU343Vwehs_kpoCNelNivnVw1Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A63yrimzbhuPPC1jjKRvz1Bblbp8edjvId-I8BFzI7Ro53YiYbH4atRo2KinSLjMyxfHu1c3keJyHdL9RlvhMjBZu8On37TcKFNjiIcRJo3Kk-OnxGIKj_g-23e7RYb1uUq6dWaAS0Gpl6sv7dl7mMWN9EugXFTpfbkFMfTEiRtj2L6D0luLwGh1UE0xuwhsFYmFVeccSJhL1YBW6ARILze4OFyVmp4BzHEhvqI7S5iM7ypE2LclhJLDokeFakYQj7Dp3A-rV3M9unmmf2RktOl228k2FsYuK45wyAUkNhjZcEZpdJYmtG1IEDY0icmGDSat3x2WAXuJUbHzuTs7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DlSZgNdrusWAQcVf2vVB6NfsuQbBsuzZfKglTSzIzbHjyyy4Yw3GrYFchvagm1dCFGCmatOeAxdjbs7XP1r6AkshRlfpYz2Ma4MgmM7ljKD5ouqD-DQV0ntWLROnJplMupwu4Z8ffTkI2DyYdPde-0U0WJ_WseYL_jY1lY2WRiLkRFXHxgza6AYQB-FaEp68KVq0Kxgdh98oGf14a_actaMaBluxXYhbiuXOkqmtCEVTurtrYlrRmWQUrjrgyMAGBSNJtZUnomsKpN4exYwYXaFZMN1x1ByLmakvzDLqMxn_VKPRldVjcweJzQchYjuWJjZI6P4zK1vl5AJQnqESZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlZST686ocGt_BQOIEe_piEP46gQi2Zi3IuhLc0mFhYqs78x6Uyb61P96oRbl450pRbdNIN2X-N6LAbpAXYyc_8BEmL8G-5swYNKK_mI5_imiO7tFuipUaMy3QQSnOPBr_N-KUTOreORYQE1peGQexvorhJlY5zrP81xU0sm13qhK-UIbIXC2fWTntXkmH8RY09n1aWXMq52qzSXsrImQZ7RNlsnc6vGgwz14-o9zf5lSG1349rRjT2STU1_MBtDrWgUwBYma9wPZXlNM-6aOMsvhGZx9Fs8Q7JAU_75z5psAd1OIi8u_vibPb-dPeYQAL2Y5D24R5SBOStoUKBPTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwju1RjIliT8LzjUMjsWuf5LXmAISTROeZbVlNOejPg_GkVPke9Wk3xeKgiXlV6LsfL6lX5fxzEMPCfvdwGMTwo3EJOKO3AdNfJBs8M_yO74Z9T7vX-CwBabUsaaiRwBB04KHPhH0igv64iL1Wc_0uH91e2wLg5PEzTTV7mf9XdgwzKFrh0CeuXLTMmzu_M54ptsnE8iULespyScEt0ieFgDxfdSxEz3fqf5On2p9wFhPPp0q_4dw_h07cGndF3OSj16BD7f7GRHIGFt_8PuO0-T29Rw38yl65isWeiUFsXjQ-xpe3DwIBmb-UzYo8Tuwesc06-0S_7l_IUNQVrLWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbLtHWKZc61IvFqEhomko31_-XY8s9Mhz1gP7R9keI3xLEBeCWd48aUiP3tV2wa5hM20wBOMSpBKbG7lu2xs4fC9Z7MVmH9AlG-khJdkSIXLpOyTGhTESaLdgc8wsk0ZdygDUcSTrgVdF94AWz7NafphQ_5-qCwY319PHd7z9fPCd5wWpX0f9K9NZd5oZ0xoBmVSEISO8gqk2XCvOXS5WXcsFMe48xxFL-oqKrUmTHBkrpzx1C3mk9aWjGQbkQoYxlE6fQbeKaMByQOcXxtq2APKQXSQ0cvqbsfL5ZA1n6jR0p8pBvWIdPVfxNv5iqC2nOHlUfTfiUq_qeAjXxBaaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP3hsS3iDuA5oe1cX7zgkF5wBtd9rdRi4R5KAJorRCfVF-OH2E4VRQ1qH_r1sbPPGdgo1SgXe-v8Ju0i1HydJJpVGaYLuWBzFGbnDgl6GykqsGtSqfOxcrOgc6IauPLTi5ccE4rSCbBHkFJAywYJKOY_F83ffhCaaarDHRYpKPI1DyyYtytwOxqqfDxCdOuCCA6ymcgPT2DN5zk4UPsiRsctpHjmFfqjeM55dqimQ5yqzXrTxwCI_8hGoL31XijGcqqiDkaahj4Z7PtNPrhONS4tmzvUmPoo28DItEsMwjNfC8myNKbyi3OQWfu-vU2YuY7Gqj1zP9l-R15Sk3568A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nORI88kPuheIZmJmrcckz8wKkmvSQCtd1y2QHbFXc0wD_qQnnHee3CeoIGoF2SJHYiGXrNsv934PxoAFz96qQhcjtC5esnJ_VV6ZtKhSj3Dfrou6pp9wdMEmkFSRv3jBzsWuCfPH_PSmGc_PJxTOBunKSlSD5GPZ3zIM5GsnciYvZIHJXm7R-bS_xTH9SzDjImZf3WP4pjTnWm_MQWqG_IqvXTQtuLoqXFFpdllHmBbanGtdd5X1mRh-zQkR4fmH4U7BXYDBl9DPEJw22C8Y84joxvdOSsQURL2MeKXa9PsY95Z3bVvCOBNFKNxxcPDQkD1Gr0xVPaGSgyhRlzQOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-NlOpmqbnCsYvzB4w3yyQqS1QaAwqcmGYqh2c_s3DioPQTA40w2AXqjLXcgb3Ks2aHnOOlbb66kXQgN2fgqNaNz0-OwFrbYu7BB19ibfU_mC6pLcciFIEfYQ1rRwPjE4temCcZDBHKTpCPe3i4TZW3nHivp9AwdgqAQR7DlDn9NrcVeZV7cFCiexiNsrha9dNn64t9ZdlQpoL2Wy1w45YtwKJwabCpbQPQYBfiU_qjxULHcKU5sZqel9qGcopI4zQ-jkFGl8lAAYOr-kEIVcF_k3VWuKkJgZMqAYElELEm8y8E0sPqiP6JXOD84MMzsUccgqvDvtqc0l58wYMl5JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN5c2jqEqMxAPNW5c6usZdu62P140cw7AljSaC1lioWctVovv-SrFow9V3clqj7PAwYtRV701cCoKfl7PemahhabkyrBZ0XkJe4Q4cCE-2fntJqaPbyVFtcoknLTvjAYb_8J10m5eng-8eqYDxXIz-UeN0W0yJsdzdcYigV3wFvWE7CBA7PKNZ11kiBPGIKW54DmZkU-mYtIuMp7K0OUtzf0abzhV-vU2kTfkkKWAjk3GDC7kZaqTvzIVGxneZWj8A6o9DKB2e28zY4-qjq5uZfNep5rozQuuiqxfxQNat9oAiadSM60bfBpxcozZ2rhGnhQgZQ50egU7LKx7dOEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXuZBfvGQtIcttncVWbAp9brRlJSLTQ2hX-eXkxiMp98nd-upsrENGjHv_5F82J9lZAmDv6NQVy2RvhSZZ5oxs5RD7fd94xL5qcBMrLscEbVQfvv0pudIpTSv8jgPYyhAXU-Yt57NxmZSRx3pVGeDgqHIUmTSMZv2RJemNOJgTLb5JAqOtHNXern3A8z3AKMGm8xqu_sdwSME7QeCIFaaLmldNjVklmTmgckDU5P8F2I7l7d3ehe407cepVBPC5an2Cjh470LtQFKauhd97vx4LDV02U08raDOKoJZCyxIdoYSGVXzGiXbqZtdhyMQDyPsImMHJqQZgEjaOnfPwp3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLoqqGt_h9H6KguLPxpI4bpvqL116ydQUB_Gj6UgXiS7o1hA2tn5rLl38wkKiuzFhpTd3TMGpy4XIzi6G7Y7WGuWmQIX_pUVP6DdGKfQYACtwSfHcFl0yyylqSRE8wCPBFViqf9jU3lDK0gY1hLUuscdnCqjKR93Dg-Qfmen4Iz0B9fA7abDANndE9qQJV6roiOuaLcSoI3xoapftuYR1difXRoW83k-qsVpXBMO-mkazEJnzelKZCKN7muuWM4VQd17jTGUWpzsPoWnmRjOADEAOei5fJ9mt7Z1b77m2mbWKoh-A9095umXKX5RJhCjjwN-Z24uO4LCkTfE-ldqkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHKnGKC7kprJ9f2oL3HX74tHHkK0pdx3nvivr5MJ6AdDcdE2nnNN2J-gLrRAizXFUBdTGeU2EW2rvEBnE9kXOQyk1jsptmC_NLAeE02NCDJKHfB-GKaTZomibA7cceXVJ6z8jxkpHVP5BLVpe3stRKNGJrhqIu3hpyRMIl8M60YLVOgyTfvqW7ZTwvLJTtoZoFfgKB5u9ROpBPrlXKRif4dB1yhUQycHCw6Ae5dcquuiNdDpgVP0H9XxecuzxIuPgJWGMQJIriHkOLt9MSnNWHE3iQWVzXn6qw8uaa-1Os_f-EU6zFGTWV1-QCmZ7YRsNwewa3MW-TDku-KmBIfGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-7yXM5nnFqofMpLWg6-_trQcN01G_d61z0TEHR7JOjthKxLMP6qm1fXP-HCJ1vCjtd8X8kFqpsZHJhVTKn6Y4xWcZEiNalpfEt9pZrQm6AJsMYC_NlEv_ZxX1Sdk7m86Gs4ctghu0GCIm2i-3djv0c1-ApZNQvYU2LyU8sq_FaIsvIUSB_nBpIt2sxnJcYlCfSwS7kyXmqGASv9Bohypi1dZjvvYNgzVkUJOT0J879Q2ch4TiFu19trolklPnXN10N3WYUEZCxdefE5VjrWfw6UzutbZzcWvkilDYQn9un5RuCzpIqBtqcC6oc9v5wRc7MRn84lLaMCZ_b3pkzkPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQcr1j-hV0O5R3vk-9mNVal6sDwJU45ziRXNyKCftDr39dvipc2unAZTIYMUPzIk1F0dxHeCFpl8vdarM21CNtxnly5Hlfg7yXgi-Bk4XluC-MTB-TxsuXKj4qq0AAiki-ShBW4xBIQAE0N48zpKXSiXCD3Xvm7XKp8qWsIgesRgAeIkg_DcMILmk6Sv0Gec-w9YLeTEEXZWDRHmDzPjDjuNUvsSS49VKn4EZZq5Z_yOU03lY_3eneN6ZOHtgi4uVPldgHiQrK6stKmcVVhXK7Xi_9E8YrSbVvCoGAYjNNHO1q-Wvx5eTeAf4g71BA7tE2D6qfEwl_OR47AAgnLwhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxI4z3QIrekxkwqVJ1_hIqVdB-5OncYNb7Qt82ydAlAiDBFmUe6w6Uhu-pJPe8OCiq2TuAEHTA_N-eo_fPGzCfaz5uRyt39JvODKV8TW3nHVA-MEcr9jzJptHQrv0pGTUrlafKFF3Hop5hcq9WKxWTa8OsZ7pqwsh3QuDWJb85xeIPg2rdcY9HdyNswkf6gXoC0y0cw-lTVkDs-gDVxZ_-WygE-t_xRHCrJgteMihSDPOre_SCvcwVSg0HWc1kdjQAJpTpFkh0Lzwkk_VKUm0iLhn-ineXsCHkS-eqqxtoJVg5La-0xTAaYCa6I5eVKx2FfMhtIEIpkaaInFblguIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7DsHbqwptA6spQDqJSlx93SfHYn-qljvJQyxiHfDfxQAsDTPBysI2On6W_rnu0ddJE5c2DPvOXEKhF1TgW1aCzG0Q-ujmAAEPv_-812JG-z9BV7OI0WXaEoH2tQ6gP0Y8Z8nh0l5xqE1yzCsXLbt3-fUnMJDp6MMMrQ6CM9s_fNhmYvFRCzQYtdzniQ0e7csCx0eDr5eC54FczLbUNnpCZSQ_k9mdIF-6AO8kcuMa8hRUEtxNSXZuUbjCSABoh60sAYagi8z4Wqg7GfYEKTmXyjLG2U1lU7LpRQr9AwKcnpl9vz6MfTqbN1jOUDPBypeajqR6SEb9ZJhu3pm_qbNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfcKF3Eb3JtCQGevxl9diEmxThFbdL6KW5yMHgj6Y43Hjkbp0nf5q6KuNyxQD4pbKljBOwXlVe_3QixXAzQWqBYAaD8wKTIi-IRuoMdC6Jfh3a1k8n7yEliGDfG2yToM-ItPyl7FCEVAv_-p-CcqsBZ1caC0JMWc48e4aa_XPdkNTZWp_tcQrBtTejY2O-TLdZ1sjOrICqRbegndQJf08LI7nAY9MIaN-GF-cPTYKIjeS2h55mtkaeiiIp7A6-8nPdbcKyK8nORxZLJwJLDB4w4TMe9hOqFZVFTYWCXqywWz4hHYxP9rYRJnZicSdbTwEovARjeYQb2x7sVeL8citw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLU8PVv4-UKU-gvfLQV0BEVkh056Hg26OfNWwHHlODMn97IDVy5AxuiJvNfOr5c8myHWX6aLfGP6uIuzD6HcK1LJ-Dgn6jDNlwTDOsBHJeYUmvWmyjRBKH1t8bRmllNL2ZC-VrIrvOKRpsBKet4w8TSBhoysvWq91LaJjpyvoj5nUVaZe89B_3dxNBvbLIrijWh31eXZvI13E6VSfCEs7knhjzuIMGJU8mk4cnloF-5GVkI6XXdTPCxem34u0jSm3MlXnaymNieByxZ6eNevm91P0dORhncagxbXa-aN4xPBQ5K4FZQO61Qk_YbQRodH_WjZ6euYJHnZNIbB4i5odw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAgmZSZP1F_DQdE8aWniqs6bVhB24oOqewdjj83PCJeTuqMqv2ih4w40Dl59OPzWTrodzr_4UWq8glrnotUwxHx9UALKKAH31oAqxzyV8JOh3Jt2qfGo9qzh50GnUjpFCDN1BHO7FQfhfnT2BqSjJVCdmONAI_mt1PbV330r2j86W2zUl8XETW6K1vmsQ6zTT4BeVsJxb3Tr42rhkKLkRec8Uanq1f8uNjBkMBAiaH1mXkUoHicnz3AL3RC0uuLOOqJJBpVVSr_UXPEUDVaW8ccqse9psUrJ0mEaos7hcgZZYY3SpvghlFJI1xN6XpOGZfnue-Ou4m2iB1KVhgzvHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv1MIXbiirrO72qyB2Kw0Wq0vKPf-F_oosY68OYX7GZFjudm5d2-5Cwd4aJZ3ck89jdLXY5W16A6YdwiBwu429CqfIKjkyBsddhnAm3-vXs7nX1o3xen3tAIR5Oae_6okibrO4dK5u6lCJ-BBdl7j0hDTxcGwNy4rAes_T-OoE36oAkjTsKpFUmuvYGxbMR72Z8NgKwcSkL9YUssd7hj53819pUVAg6yYjU9666nigDCKWQSJ_4eQrAmKFwMeCaEIqJXceqbK2VebLB0EeFfxZrkS2d2WvA2OWCveEKufKEvIYSIXzTBiPnTEVN4R1wtcQ8Qy0qg2OdCzeW0qXVGoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2whemZSdj1X2fkU3lZYnkvxlufCwoR9_2gCnhHZ0lWJFmt4tuQdU1C2BhwdJeaSmXlZqbjhtHUvJ_IZhWIkY6MENeCv6Ge9siNp2yzCHuA131Th0MGHZwqowvpvMcDjvPi8mB2J_mqRIKVX1E58HnbDDYsRE80FUPOqQCzATOHdx5VcjPtjlihfgIZQQqQiYecWohPBmODstL5CCtj8A_VdNCmkJ-rY6HF6tmr130HSzl5k2gbScU1WVBvxdzypCArD8KClNhpVhqwZcxG3HO8DyhmcbPereTefQ7TJ51mudhkdxrbcvokAv1rpSpc6LRP95sfdYKAPRBh7A86puw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvsOYtDGVNc8FKWtA6q17qeTKCjVihu9eGXAU9qpHkRjKu02NWKB2MJw_xSKsbsi6yTu7JiDaHk8l4xYQ5yGh5DFSD2OvKU5ZOXRe0zypZp4itdDuejzYnStY9nmOTKnQ22BjtrByYeme6Qjqostd88WyU2udB8zZaui9uAlbh2ge7ydjCsVsCzDxAkWjkkqzMazGaU7Ce7-Leq6JDpLMFXOjKnW4yc0d7gDjJlZmZkUXqkk3F32Up2bJXnaFMRlfzSxzO0vVjyojHwyg78Za6e5_TnBmStPn0fJdm_L0WeIDYwFJm9xHMUryaIqYGXZBwth7BhkGFctYDrPpKe1rQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=KTITYr0-zp1RZfKajC7lNgZupvBjC49Zevpo29kb7avvFEgIiIbbJeqoOFYKU8waJFNsArQSqZT93NPcrlbds0B3P2rCkJZJBejk0uOdEUaU_ArsZZ9mhBiJ5VpBgFYbXlegHVECmH2F89zrqhNfknlfySTjy9F_3lmuZLBufgSG6PHoxiaUbGky0jy-jM6Ou7jqQl611DQLhcdYDtTuc9XAavgGhoa5cjdvKaJSAtyc8YNS0nkVs3CBms8MKKjX2UyhsSOcT0r5RIH6F2hlpTXWEFTI5q_C8GOPZ9_5slBDlvhtkEAG-uPVTGixANlRHNOUoL4SSpwG_Q-itr6fEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=KTITYr0-zp1RZfKajC7lNgZupvBjC49Zevpo29kb7avvFEgIiIbbJeqoOFYKU8waJFNsArQSqZT93NPcrlbds0B3P2rCkJZJBejk0uOdEUaU_ArsZZ9mhBiJ5VpBgFYbXlegHVECmH2F89zrqhNfknlfySTjy9F_3lmuZLBufgSG6PHoxiaUbGky0jy-jM6Ou7jqQl611DQLhcdYDtTuc9XAavgGhoa5cjdvKaJSAtyc8YNS0nkVs3CBms8MKKjX2UyhsSOcT0r5RIH6F2hlpTXWEFTI5q_C8GOPZ9_5slBDlvhtkEAG-uPVTGixANlRHNOUoL4SSpwG_Q-itr6fEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNJuwwoC1HirK7FHydzcrEdNgkJ4hK6AlaXhUQzpMdvVGIkgRzqJ39rLIrq2ZMQu7Vqpuw-cnb2IoZmxdZ7Ji1BdEMr0gp3iLP-Sm0IcRpKmTOLft8_f9xiniIjR9hsxWcHpzhk5_QEOXFrL9tHL3HGis2PkPwB7z8eDPuFP3voVT5Ak6Y5aSscnfP9GA2eIeutcmHvBqUrWmESr41_fJ_1axi7njgl8PEdJ2pBM63HkebJDF_C2P4rTqpnZeLxD8srFnqxO_haK916qwj2Up1-Fftpo2zOGmCDBLzfSol_NumvpYMVHwapX-itH9BwuAzUilQwJ4LvGQz-BNGEyPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-x7_3mzYc0TkHtPmVflrTQoLgf90gmvJe4wlw0YBEshLNKpyTSrU2egRgviyf-srjiYKqq7f5aP6HjmmkKcqi3rgTeRr0X5G6wzXfFSVqlOdsb7cQeDnawnrfmjJa-sd2edoJnc_mRsx5NKprjwh2QbMd3k7lhZJQOzVzqAUG_exxp6i35DcTs8Q40zkYu7VPwV7OtXIM_5OUZl3A-XU0BJHSOAJJfFEtN6L_fYvpt4F7ttF1_f2Ix975ILat0LQcaMwJuH1s26zAUKBHam2blAJYr4soav72jlEXyJ5ZIOCSHg32i0MG3XI7kHQGOAQVz_U2vd9C-Qb5RcIHd-bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmqWdEyI0w_oMSe4FteRU2o8i53cwIN5HiqhiKh4Ke7u69PvgIx8c79k9DISdmIzjihNyH-lfqZwOckkIyL7LHWNgkAkV5MgFvz3SaG5w5rqXKP7cQk_ltY5czWO_JYX_6PhzsymsIm3kPCS3HMWm6sH60wxMAvmfN2RxryQhAAYSIOz8US45jMZVFG7m5WT2--5JthT0xPHeNIM0vnc_NW6KajIOjP_PF3pd-tDnsQaw83xMUl53P7sAyNRDIe21nefagohbk12oILQDVwkfnusQFgA61zOfuw1YdRGCiETq42k-65-UoaLIS2WaqACHstdnpgZJ3DqKo6azOlDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVxnB7tu3zIJ0bNJEwnGUxa4jdMuCeF-QKeMupAHABPDwuTWffnQqB1atmv-sI1QmeEsr6Cw7y6egN51w5nWdGfIhHNliQezpUjIGDDRxYRNF_V_AQnogaL6l-m74Szg7l4vzwHiVXd40i4uQUiVusHoH-eb_Xnma7xFmnH0IkL_HfcnXY7uzM42ABh-aPmV9vvEePQ9DmznJzaNrb2uDYHlyBaVzL7ZyvpqZ3xvDf7Yd5QR-UFQOMticoUxfNfipFGWDW6fpIAeLc0taCJrn8ecVhoCR9kJC56EQXFFo4PTdUb5W7Di4TfBaRYfKx80YZxEvqcFfU1MYNV6eSu2ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh_I03RYPIRrofvUrKkm55pm4HFb6ETssOuO1bciiQFODYiwNFu9csQDoa8t7XDnyBMaV_6vwU5VvUO5NhO6EUNdpnGNJhB_Y2HmtYAxFPQW7-WPrejbuUwafCUohnHOjBdCJAGZFG6r964ql2Y2LIWK4cmj2eZCu9SOwzVGr2AQw4-CY6gY0IcA-rKwtIXyp6A1D3dYF3LgzaveDDreCnR9nh4cbjknYv2YbngRxbXjTxT7xySllrCo50Y0I1b8-QOy9rZ_l63IOV2AH5XeTOFyTJ02OzbXk405jhlII8I3XaaRgH2AgUO3qzBJnp-yynsRhUoTta-65-u1KpiYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvT--_xLcz1GaRMnOHHv6TUMD_5Mfusaucxcu7vMcKPXwDuZe4dZLLWIaVSWim1n9pCYqZ2amnc_CQ4GYZ5p3nn-glP95MODPbgYRxEdKfzjmsYGnqlT0X-WbWAKmMdJVvDdlvCNZRJSJwwWS4MTMVORbhP7gnQRiHg1hh_aKDWGH6NfczRq3pK5QAHhgVsNpREcAW1iSH9nCnkkXZs30dv6a7nilr2jWJkbPO_VXGCTs2Gw71W6qB6kfAYnqWHmvFs3znK8tC4E4u4SXUmC1fuLSwTZwGRaG1G39qku3GsueICi7vtPPa50AnGLV536mJsMh2F6JlGnVjs_q8_zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKxkwsw7915Tui5F6UhKaeOH6qBgNDqP-UPRJpufZfbBGrJx2-wyu7-SLQeSt7xyuCb3GgtriXDm8TQb9G12VJHSgRYsfgDSt666FTSahZL7pc6ptP8P8iadGkHY1RHHoujcXNzITi7f7UcEsiI1D5s6sPVcqIPl3LrHZcVDsiM2Z4i7nBu3BmPMhQr_u6Ysb-gYhv7P0B2-eX8mU1TNiiCgcyDeGR5s6QZIhUILkxi9zHKVdKH8VdQ5ME5bBVSUMER8_KNPec9DrENYbw-isqIZ3QDa3amIXL1pObYLqxbEk4OFRk4CYqJkhLGkhYTuNzJRG1S4DdNJgHxju2DcGA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vszrcRuSJ97KQez7KF5z2r6kmA9GgkmX6zY47FU4k2bGcW5jDlYdfXw4CGvOhWJMjR6waiPXY7IDk4QxoPDnJNHd0yOppb0A0b4OmIW9TLATa-IMAUgdFk7wtqpAHDqhjM8VRr6nQwXxFYTPR8CRWwxcUS6a2u3Dz8aM7JN6WUmwIHd9v_P0JsIU4bAHclBIpKGnwRgROiqs5fYjjwJa2a8bN353UyCKvllmEgdN-c362On20_ldUD9fWUMEYtrU6KG7QGiTsozCXc8c6ucoQsE3YnnyXrcMke7-T0XqKRFZlo0oVHPz4M69yGNJbdq35EJFWSU4bnbIs31atikypYMofqvQbJYGUAE8CTLaEPpXe0xJWBPmhKQHrmdwn6cqbPa15yWE11ew70Oklhh0Kmppr_cAPkSEkIkSzFSMOXWIQ_8qMl6RYX7_inb_FbXcJ7ICM9tjCCLhX6j4mcidX26QiGViG_0uBr7LJ9ulBsX4SkaD8tYmZd6_6J-5R75jfbAHiPRM6aq5dmAZt7SnJTkXJRZlAid5Me21J9C1f2olmxuLMheSdgOIE7yIqsgJXqcU6TeNjzp5k0lZlJi4af_T6SnWCYEbfVyu3le3IrVgoblz8Hm8fG_5cZG1kPAY6V-jTOl1W10bVLAbEV_n04mgK_-2u1Vw59XzZwfS2i4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vszrcRuSJ97KQez7KF5z2r6kmA9GgkmX6zY47FU4k2bGcW5jDlYdfXw4CGvOhWJMjR6waiPXY7IDk4QxoPDnJNHd0yOppb0A0b4OmIW9TLATa-IMAUgdFk7wtqpAHDqhjM8VRr6nQwXxFYTPR8CRWwxcUS6a2u3Dz8aM7JN6WUmwIHd9v_P0JsIU4bAHclBIpKGnwRgROiqs5fYjjwJa2a8bN353UyCKvllmEgdN-c362On20_ldUD9fWUMEYtrU6KG7QGiTsozCXc8c6ucoQsE3YnnyXrcMke7-T0XqKRFZlo0oVHPz4M69yGNJbdq35EJFWSU4bnbIs31atikypYMofqvQbJYGUAE8CTLaEPpXe0xJWBPmhKQHrmdwn6cqbPa15yWE11ew70Oklhh0Kmppr_cAPkSEkIkSzFSMOXWIQ_8qMl6RYX7_inb_FbXcJ7ICM9tjCCLhX6j4mcidX26QiGViG_0uBr7LJ9ulBsX4SkaD8tYmZd6_6J-5R75jfbAHiPRM6aq5dmAZt7SnJTkXJRZlAid5Me21J9C1f2olmxuLMheSdgOIE7yIqsgJXqcU6TeNjzp5k0lZlJi4af_T6SnWCYEbfVyu3le3IrVgoblz8Hm8fG_5cZG1kPAY6V-jTOl1W10bVLAbEV_n04mgK_-2u1Vw59XzZwfS2i4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJOVNKiorvqIamkiYvgp2wav9lP0NvaZPlDr_bl13axrCQfJv4DZXMph5hQX_5lhs2soRaz_uJ_lAyipx1VRgQA3NWmn7OLOuXkiRoDSre7dK7qEJZJkoo8DtOAh9SOzwZdR8XV7CWcmoahSACrwW4QVGxK7ZCOFM5BDHWYfabDIZ6KXKd6hG_l1yrTk24Q7ZOHgDZIYjuQw9cbOoHfxQygIkyZhDA7LGAc0xfpFiYRpEU9P8AwlKsCzCRgOoSx4eo5G0-O4nE9fEP-PRaf4Ht_1mlPZsx3jn0J-PUUw2eeFkupYJbp8mu7fTXgm1oVJbno5S16MS_HtGR-MEox5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/likRsfuNztueys-_mYYbTSE4hsG9grFm2jIT5zRU2clgx8J9N0tuLZnphWkhObzkI6DqxhTPiZ0xNtYulmMMuNSAb8BGmN_VcPnyJ7nBfYDEh1E5tCJIniApJ4V9b40Z5X8zj8UUYZSE8E4-NUy7BqiIWqFgX3yEYXpID9H_hqOg9aB2_IbFbO2TBce6Bafd9JCq-JP8mXYBiz5nrwLoC0A25cV3k7SFEbGH1mgBb09Q4nJ5twWa11UV1VrcSFdixomt8yqFKbHK3z6Hnhgs-Wts0dD80ItXupLadC6uTmWqpsrmRd2LFiAefb8H-_PTrvOk2fuNUT1LrltBZRnKxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpuqTobhrXTqjhD6lmBCyDfucSkL9EKs9jZvyTpV3bKmKyajU4ej9pH2GzU5eWcMS0_7p4N6Wy6m33JlWSaoBZmhsvrRUK4fgdnvckvkHVhoAieuQ82lq0dv7boGXmn3KANa2RagjPLDiySbe6NNydfdrhFjoyM7xAcNZIM6MEpkh4I5s8DRP1jTmI02XUfvEsSKWvmC9rgHUHZRbKeRrJePASW_2F8bF5-2Lx7AUHhWbnte5QGdcbQs9QEUSff1gsm41YEuyCI47ytAhO7QYeJTWSKN3KeklpW0PBRf6afauq_Wc5Sckv97MUxLaRPq_X_1uyGHoyzx1o06nQ86IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUFT4MIQ_I5G-8P26K0lIn06yEpLEqFBQLdoi_Ipcya44iSkPp5XWRTUuNaKU6jwqxE3LYVhiZVTgBmmjgmX83-Yj0t7i8bCZN4fyH51EVxWf9znWtr2XBLVFPkCMqmWAppKeE2ZUkrw7AVgIon1KxcqT8gE1R7NRh0gUrg6NMoOLHKIeP4aaOqbeD-Y8ZpugaE9I5v7yS-i2ERP_vpIJ36D-AsL6o_RdYnlFKbf1EEqz1BYoGzqcXchWZbG_utWf6jTFGkyDespAcao1tTuKd3p3sQlaq4w-kzkAwBo-bu984TlmmiklAQcGrX2g2o8HwKGm9QMXnBl7BScdOcmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bu0MnlRWwDNu5Y-EeOYdNCtHPl1KbRifwmims4tBWpMJcUsyNfFrlSM8PSuI9Oi1PxrHXPZFZyg7cqfCE8q6atLbaMhajnl2Nj8KlbI_Lb5MhP8FKFzLEZtd3-ltm5MgW2fh8f3njw5mT_87jv4UFxyNmjlhr8jdPmXOVAiJRJyAW_ahXy03pEno22QdjGlniBwCHWVhUioEp7ThGz4KHjOa3AZSiUA922yVUQ95O0DpyAeBPhnnvVQEiqTGujTJ4vdkJ6MsdtaJOHIa1qjDwbqObyB2MoEVmylKV6fQqtDBtJzobdrSaEvGR8wkyTFkX1hDybpamghE52z6OHcJAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZIpNCGsPW1YSz57El4Xls_6mD4gYymw6DRb4C4IjKG0m4KWMMmMby-OloCpUgz60TQJgaJOqZsDe7Gf2qjQP3nFMY8i_Jen6hYBPqO7OEvbkGaEU_Mdle4_6gToI70aejK85FTQJeF445JB9aeb_mA-iw1Q6yDIfqdoRhyitRMZ2MsXFb0qcbu9M3y824wpQwyk3UOTfCGQK0z9L_FhLV4tH26CSjZTpgkFDQ7IaajpEQ1lcUXSUU8nidMzPWOSsdZnHC4B4J0EzKWZoF_Hr0pJEQdxxu2hjBQ3ASfqDA6MVkfvsr-71j7ume_MPAVeZfDIKCiMHT6E8eFdUhY44J4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0ZIpNCGsPW1YSz57El4Xls_6mD4gYymw6DRb4C4IjKG0m4KWMMmMby-OloCpUgz60TQJgaJOqZsDe7Gf2qjQP3nFMY8i_Jen6hYBPqO7OEvbkGaEU_Mdle4_6gToI70aejK85FTQJeF445JB9aeb_mA-iw1Q6yDIfqdoRhyitRMZ2MsXFb0qcbu9M3y824wpQwyk3UOTfCGQK0z9L_FhLV4tH26CSjZTpgkFDQ7IaajpEQ1lcUXSUU8nidMzPWOSsdZnHC4B4J0EzKWZoF_Hr0pJEQdxxu2hjBQ3ASfqDA6MVkfvsr-71j7ume_MPAVeZfDIKCiMHT6E8eFdUhY44J4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmecjheMAGMeJupnrN2pOiPA-kpNGOtyr0JCX8RrQXZwJBInEARDX1mpp7PV1zA5m-52T_0xnOfjqyXZdtwfLOqaZvNjun8XMNIcfWYONMoTe0JC8nl6CTLDVdeuGhJfdidRUZPuTnxatUnP1cjzvGN_DsyA--DSGOLK8YmiL2oqqIo6Dfz_s5ba-dr7mDkdqnF4mESSFeB9BThDBK5dUs3EBzK3V344yjy3XhonQYWFB7jysDTea-rcqI8tDO3OZp0w-EUREFwmcqQQ_Zk3tbneRFSsJIXyEA_J-1AeVXuXxOvOmT96R_1zwnwQoFXzC_bolP_j1EkUuRibRpg7NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3-LW_l3H_TyzBsBliZfk5C4wSU8PkH1KrzX0aMzAxSPZNrlrcQJwIWJMMSEkoLvT2deo2I6qW4hKEBiuQ9Eg-s0UWZcAf-1Bs9KmTh7IQpmkZm5-lZSM5aXZanVPaE-kbNkMt8EfTkJow3aV1zGBHBCMYCvzTN7NanADMZeuMhKcHrvbVb94ObeDK0BWbI2W1FzJWGEuwlk8D9ZWB1ElNbEnyB__HCUlEfj6KSzEMzdGuSZvAdVP7XuCfIAQj0WYLaMbh7mK9P0R4vUSa8iZiKRmbnfUpHGeIvTGCBwEPJ_HkPVg3S7tLogyA4ySxHx-qzOt29cam6Fsb5RS7DcTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOSB94QC6BOulGvmQVVqp5nsVDMrxrIF_BFtQXAxexqFcNhYGRis5D4HSq1rN-B7JAYqP99HMqxOnpIImlF6hJ_EIBil1V_Tti-a7Oz1p1R22pmjX6BjjT1laZ0_-o1sFjE7aAjKciqFMilL4kxHOqhcDhfwfpmnJ-GXep0Y62pHTTeHLIsMh6kd81ZSALcAKqMbn4C08lE_jO_JMrC-P5JaaIRtmuwXUB8A4CxEugZJ1T8ySL_dwHMQYgw7EUjwCT8Q-QatQMqt2fZE-vIg2x3Mlv-x8tBmaaKBISYC0_oMaLSuyVBk7BXZeVSkDwI8ZwkYWC0ceOoNY0A2DlW7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgXa13vUJwI0Jl_i01ZJN36kp_Pm2KA9-JQVJ3MBHmehfXlnXpKRvcxAQ8clcVxlukqLJTumEw7sbFWR5Y89ynE6xssXVsJggi762wQAVyLqtpXU8sb6-A700VMVuSZwCUaciZzlL7Ro4rybu7RBzxeaBNhE4UdnyA3Z9MKAz-K_Q40_O6r76B4vvIsX54wTmOpuEUaihBr-QKVLRXKf9XY6f_e0IIX1ufhaBjv-kt-Pm21p_JntTSZXvcPEBM1zhBC6oLEJDTFoNHHZmVXhcYQbrLooRTxHyxSITjqLblSwnpgMxQVVe2_JuWUS_wkQQ0IIx3sDXOabyU3ZftF-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFQYBODA9yIukzfrxWvllxOAL83fGpjbSE7hR9t5SvXKLGkgy460E3MFSgB2-gXqU2k9Zs1fpU1IT8aCxUDNXJ_ZTqkgL1IaEEIozOAGs5nTrl7b9Qak6Nzg1T89sGeBQuaJ5rZjJx-KhxWgAYcr66XD6pAf13Y8bv6RXK3_CiU8rLo6ncG-Y0K0qja0zxsHVtB1j0VLvwE80Xwp4HOYBP9LoBmbggywGVLaIyl2IHJc1a4Q3owvP2bknFdgUtmsV63WyLXXttKdwJSRtrHWSU6Xx6r2PzXgDV4O7myGJCzakV2C5IqOXm399FREgEo3QV_GtfRbRgiLArY9n4pBnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUkAC1wVoMQHiEgxeMq0ogfuKDwjbjyqFP1AdP0dbki1AWe0xyyn2cSffq0LMNms5wz27w0x96O97U4r4tHPQY8aIFyxul6koenN1MWOG8xeIILzEA15NaJbgXtRZQAOfhdJgANju4Kwq1g6q9-jsTeRVFLhJ_Z8lAOGzsnR7E_4H9IRtsrxaUbRVC9EStuhl6kzUWTnWY3pYcF9e3Fp2CaqX1DvN3bisBRRkVZAUDL9p8GpLZOoOwwKKtG8rT0GyrJmu8GkY19N7Q8fH6Jp-_KZJvA7aQsUsS6JkgAmXxx8ng-MMRQJl2JwSjOzQ1LATv3zpdg9L0haQFtT1D0xHQ.jpg" alt="photo" loading="lazy"/></div>
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
