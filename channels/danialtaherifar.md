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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 01:00:47</div>
<hr>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 271 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSHcecX-HqTvhec38ie93JOVgU2ZLShAJZtAzZ05yi-TNp8KeoW0O5YtXoomcCpPuybrXGus40BE-nHJDMwr82Erfuey0c8G9HewU5dtQlrWTVzvH6_uDloPMf6JZJ2_RvJowz1q5TjJp5QS3wvonsNXPh8rFMs48n_--_SZwDhMIEN8NqxjnCjdr7jVQFfJzdmYFAnmpaiX6Iv1MCQjAdemgZ85IaBmnBjoQP7IOyUylcDl7mRnr4XkRACtINOmZ794qDGtnZTpKDmqYz_nTeNrpZ5Yy6lFFhJdg_xNZA0UhS-z5tgaPD-4XTUik9N9BWqMjf7ahda0gnGrFFEkGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBp-18rAJLX2cJ2KgW389yBd09JcX5MVNnSDnqhKd-MdL_WcIxDHrigQ2RaKnT2AQYqJ2MtMheXpD5kwBdeeBZcQTXXUw-mfBskwH3ceObhpDhTYuX2ilqhqW3UWzLiRg0yyWxXBzzEjm5e8xbDgqmTS7hkG5gm_f04_fQTs_ogVCF5eaCloT-KaGuit-Ftob9YMClfExnEMRf9dQTpjfq9cX-t5Q_N4WLelLpdTEF0xM26SH9kvhkXJ25GKd5kO_efY4P2wp24EjEmT24w3QD6XKaCR6-AxulGL0PlPAXItYom5U79X52Z3zekez6Fj9DYndxI1BvY67qs9TgeYOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtIc3giIYg1sb5JjfV2s_l3S0onnz714JMXuZXlsOuz2tKA5HkXK1YIvuM35Fqm8tZlKUbhjSiOwzecSyVewYzjahYHXE5m4ZFvR6a84DQfPOP7YMxbnJSfDYo-C6-11Q0rofmve5K1AY6JBpzX5NSCKFsBOKPwXzzrGcbpqERGXqgVORKDHR1lp4eGmDXtnBMagcPYtF3XBPGxdTvyAvlA8yu_aSyVNngv87aPr-9Xn-7i-e4YEDefAKAwTzRRQULWLv3gHEtQsEwoEhPpEXioqljdBdBz24Pengy4947bhySdVC3FdpSs-8hamGHhsHv_yG3O5wuNr7aOvOfv95A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sv2_O82pigJWoxeI51GBvzT5zMnLMrHqa6xcwqbn8X_K_PB3YhnEXbUtBXkWffENXiyPbsdNhc0SR-M8OjoHCQktuwmdVwzn0tJI1doTBwnaBR-He89akuqSCvmokODZWE17q7WWj6cAIUAcTI0_2zL71hCzcqI66WbGFY0bo598wvx0sxYkPEUmU_yA19gaBAWdsqar4ArU_aLLXfkEiE3gC0ALI47_Ccb8n6P2U2Upt5StdU-a6hhqBzCOEvydst6MvuLtGTp2gXe3iw1WWHnu_4kZYWi5Oi-2PnyB_rA0bdLT76RnKzWIeadDbZYk_od_2VAnYaDyshdl3YauXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6ZQp4SAE0Q9KJL8SgbNcZq7FBIiMBomlMmhPwBCyifcovmGKfW4HaRIFNIFpfhv0NdxJ25KX15aHeNakxjmCS-WaRkqEEE8xmen9Uy3mT3bAujT4OyWUgRyQSjJmPJadHUpAflKT0NUiDLGQB3daQes2Rrs4iJuoc85wzjPefnK8TAHNY51Fj7BbIAmC8rfuP8uemjjGrxJPcQoxr30fFs4lrETDAl3zRqmKBgXD2MyX6fGOH6lEhrn5zBmQCzxbFYhUuApBJ2ciST4Yss3BE0RMK37kfrr4bGRCvyFVwSdKPzAo0AGiMyq-RITIM-RNw9UZ-XWnplhe8pt136LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NH0TS150A5t47sY6HdMARkelMNA1HAZ4nHh2TQE7lxnmkcBpNoFHXbFnve0JLJo4RYVSRAnNUYBoVB4LPyDQpXtny4-APL0kP4JB1vCBWM0sx1a5vAS5mW1HNlU-UjqBEBvryzeQ6m887SFr8vSdRq-GanOkNpEj1rByibdWWEBXNWQs2MOhDBWzRn2Hybe9YoXzZ45MDl96vj2Mxk14KcF-imiT0N3G4ti-1xXnYnVurYoulOPOY36_BbJnPt8HcMYqTwz5Mw8aBuHr3wPhiLfYa-mZFo4BoiSJp_R6Dr0AyUDH3olAF0ZtowyaenMFi1_Lq2mBF7ZSwOouWXh0Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5MhN-zRqcOSvXgXe_6VZIxdhOTxZblyCRPqDX6rf9EOnLHW5BEpdqySQkZHmaMQhm7_IJDyO2p26lewSTEy1xUPjCougka18YNljpo7BNFhiMX2QIXMFGwRvxZB6560R1Cdpi0U3PvUaxrRXF-xIiiJqqMnp9Ol9DlYxlN-q_YCYG0YQEBRG1t9O1-ONLhElgeUjHuyhvjY1WOx7wZshGRkt0fYSrUyirziNCqpi5vwYxf2rYWaxw16zqeysLeS5g7Fykw89V4Vw4gpn9UcWnlYlr-qMuG-_BAtFwTf3KIn8QnrClkLUQVi1kocWsuanqJrLeN5aiAbQUhm9H2tug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=hz9Uh0siujAKSoh4OlRNBGKwoRasc2t0fzd0oMcOVeDp8hx8XI5ZyezgleJapCp7w3pjqc1n2ButUMvD2x_yl1YKMao-0-y9meicfo4FcvsvtdtT7lDOHYdkITbedWVygIb-1jIcY-3Q9LngSCTfehmTjOixv0WlUgsquKI7ERXEDkF2gHUXsy3lpq6Zvq6Xc_O2NwShTlVwqiBRPXAcrJvPQQoZQJJoz7GMu-xbZ6LrP1sU3mqJUumfe875DfI9j-ct_wT5ucLfVaFECgytN9-VPHOtHdsw73HhmQEK953vhL3-v55EzIKiA6T1wpkSSV5jdblGrhFJkdSEzqUmnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=hz9Uh0siujAKSoh4OlRNBGKwoRasc2t0fzd0oMcOVeDp8hx8XI5ZyezgleJapCp7w3pjqc1n2ButUMvD2x_yl1YKMao-0-y9meicfo4FcvsvtdtT7lDOHYdkITbedWVygIb-1jIcY-3Q9LngSCTfehmTjOixv0WlUgsquKI7ERXEDkF2gHUXsy3lpq6Zvq6Xc_O2NwShTlVwqiBRPXAcrJvPQQoZQJJoz7GMu-xbZ6LrP1sU3mqJUumfe875DfI9j-ct_wT5ucLfVaFECgytN9-VPHOtHdsw73HhmQEK953vhL3-v55EzIKiA6T1wpkSSV5jdblGrhFJkdSEzqUmnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVM8FyCJGaGgfKBbdEtlOsW0brxbkDQdzfPmIBrwifLsrhnNL9TblGgXVI7MgbDy6hHckklO9WkNUkkCR9mV_XFpIVEt-qBWjvhzlQEibii5BqfwpVeS7XoNMMicOPNLngkjtvSXbz0MWvEDEBUnwQQ4ROy1Qjdz-8ZUBXHwG0TIB-ghhnM3Oc_CMQ2nINylPhrIzRvrf8x5YIunDymy6g8Au5de1Y3kNY52s1ypfljQLV-ikzqNUIHEE6qTFRsnddmknQqRpCf9QoQPYlDuFhs459fnCGVHwLzoe6_6Fvn7p5tf_XQHS7dghVLrQFN6YJcTHiP4094ggfSgJaKyZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD8DbcD6E4GCbQ7B6lvnpXA6yGoATsy6XA58g3OPaVv0Fz262sAYPhFA2lkvUTR_nRqdSf8ru2dv90ayJXwPRta08FnbRnYW6Jx1m1fSQAr5PT-g0dA8H5rpatHU8VWGuwVw_BWkiv-r2YVeG-AieMNRJNnbK_I8Wfydktkb-MjmMOaBRY_C9LBcJ23jeVucVoFdJWTWaCPuqqhbwm0NdA67n3f1C6fOeksp8Oq5IE0DeTU19dtpKTU5k0W09qw2t0TZxg-e_GUH-qZVHl9UjBbCE6Bim9u8XIu2j3zBaJsNmfXpV--lwg-XJFTE9-copGcgMlh7BfhckvUSgY9o3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHd2PkKp-gWSa4MBbiQpz74rMeWw-gDYh8FyuB5Hwl891G7T9wCY0ZsWLP4M5rmDvgsY9frcSMvYsUhsh7nQeS_ZIM2PQANaZUWxpNz1OJmAGMydH4RhTIPpRBg85xwvOg_-_lKx2IAIAjTs_PgYautkXCdhlsYUeserzSE_-WsFKNNGkjOTmKyH3coyY4RZEo_xHJ2ClMtfGJiGu8Id1cJnfQo0-Uhm4vvnHQ0AwDPLJFAARbs1CsDimY2tj6RG7ubw_He1oDYpoahd_VAmzMVq23jEdecC3-tpRLzzk4jXps8SXrXf9AFF9KO4IpYCQCijo8FlKGrdgIQ4_XXocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRnLtfHlLUd_8pQI_El0zCQwcB7Ev6e8CzKVuW4bKhDFLzZL-ws0yZ8-CXwsYgfmSS87GfeCjd8RXtLr2rRYPOKt8O0Bkuvm1rgO4juit_eGbL6ejHLNRjlxqUHPKv4UpSjZgJ02acUzl4WNCFjEP6_63zg0pAD-lJGchA5nK2_Qx13zQzBV92otC0fxUA7wkbv4M0DOToK2WJcD6E4a-MZyAo0hvkVeFlJvrEdXUq5GoRwC2DWyMfmj00SNWNwVnXlQi9E3nhoZfvn3hw_0ftEMAPHBGvfmzvIsxRqQeUsP2njP52u4hcpcruOjamxmeRZgh0A0SHFXL31m8gbEBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCCZyJfn3LCL5yuSpYpzJgw66Z46HxOR-yLG5Z6IKtPV2bZYepzdEUauijRxcs2RQMnxuGopGVBo2cDsd5Dlj3MegRbfQ7hfXqv3KB-1_rVSGUZQFYEjOMEVB8PFBTn2-e4TGhR9a6LUPWUGSkfUymAsyWJQjNgsyRrUC94OC-rwxu4-UhSdBH2tG-mFmKDPNIx1Osqsi_bnvTQI-rCOin0NR-SuFBQB75TmmFKGlbgtGYZ7rV5glB6E0tnzwCsPmIwUJwR-T-FoUs6GdzpYkXzBCN3sFWWk9SwZ6iNIb44Z4XbjutHXfBrBC3Q9NI3VidG6xOQ6IpG3VZFHIlqYqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCo6I5D9NT06yfd9wOMxG0mRqAQz3aTmOrwt4PAtc3azTXJVRz9dnfnYlOU_oOCiL_W-9iR4bS_jeetl7xsdP0q9T1Y1OGevi03Djl9DyrKxzelE1sGTycdORxmUBecrlItI_BJ89pIdLoqfQkv3ERlvPaSylqha0FuT-kRKdZSf0VqHwSSsOSZe3ldnCXiOIvqB3mKzFjnG6i0ilR57tMPTOmBOFxLBbOvVdH5HcTrBNrI01XxCYuLujyNuudPBdiq5yNCSuIpqC_4Ar-Dds9SudyBr9JMFwcA--nC8nGiPNMHVy9_w7YE_4OiIdH9Xp1WQ31HysWeky7Npf7WAFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSqmia8PglLnHe3hMSvclWFI4zrNeRS4k_FqNW2THjVO7tk_9noafsAGzPB88QU9xg7q1Zl4pPLCGSoWRwn1ES-USceRSi2SzTkP_MK9ZxY8xr-HbIEdDAOjexkNEK8dQFollzvPkicoWflRw-YDA8JbkinBfmgZvIzCqRkvXZ-LVoEnV188vP7zRWM6d3DocMFOYqBDZUUpHratbUHH8A5yJsDOo48oc4IgBr3cbdaNEu3dNCDFEUREF8CVy_4S7t_SPSrBSOgAozZr76C0z-1IQRZAXDeP-0BwcsiaQKpWEaSFJ0iIXdVe_7tDGCjaK1J3nQj--nMojmRGhmPPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoWGY5DXlYUill3SDy26JRdibwXg8nUR9BDF0WFTUUms56uCkIuqq3eFReSW3wJI7Gqe_4pu3repqZLfqYZNnEGrglgaPkp_djWaoLFMxlr93pVLwQVZ-y9nMotpXsqnbxviSO1QSrRDukPkz3-yS-0YtXEjj2O2sg_Y7vHkpZL1irXsvCea1qb-q-IZFqxh9xJbX3AOKzVaSvyjmovBmYLn62fPkgWBXg5gV-tUsNP_8lRehiOb64iKCf9MTM5iIKFPm59qaPJctjh-V-KQY9WfRuxJSqoHVfg5kF9g3iLybTSiBiD7Mv_KtwBGI2gP0IKclSgH3fTqcaPCGp8yXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghzicf2yatBjWV5ujxWjIZhWLU6W3GZ9hIS0UoaFGhRMyJyHkQ3riBDDYyEVQDOFL9UMORqIYgAviuhPzgEYZz8ZR1pgaHsfDQjOAGzVHLm591jcWSy88S0m3DnWrtdKVkmE-g7JUplaclsOPNJWtIw9FDkyG4YBhkmwekjRWd5wRFLe2ldXoOQR5qQKxE2Y2Nt0MmDIx5xhIJyBTI_zKidl8fX_HfhfjnKPRwZqfWo52yHCZkjl5zNvEMJ9IxzpxX9bPuXb7NjP2tgM28jN5Mt7RQK_17iW0l2JrHFhr-trBTbbDyHlbRtQaJDOtwdqqrtoWUvvmD9_fU4S-tWMTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qefyUDEWZv6VqoarzfGvnfQMyzXBGSzdgkHS40ofmPzJ4PAQ8Ahikm_BoC1ePFf2Tc-Z2a3DRBxfAVOvG5mC_h7V0YwAUwZqz-Pe7AMRSLonz7ypsuNpkRjPP7LK7ow8FbQxTu6Icb2FTGgYESg93MeisagTGMieanhmD7ZBuUoo-uraGT1DvOn9uQfr-MexaHowLvir0MDQi0Py4f4KVcHb-5E1LpNOL1kpF5LlkjWVzqeCk2IvDgkP2DKR6zepNG_MkZuZcR618qPxKShETKLHtPKLbeOYC8dQh8vFd-Voo_BBgsAPsx22HoTYQzSNxDj4Vb4rJ_QuEUjeLLSNOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFfhj6Rn5OJrCu6nRWEiffJjAZWUasiHg6tM_lcRaRYshX-P0k2F8rCdXiliSiUzK21E9EGi52vtzUPkrFMoe2rxQ7CT8V0rcy9wKnfFDnj__fO-7COeI8kDwtiES7tsRVuWzapJ4I1OOj0CXda0v8KnLHpExExfIaDa-_lclJntSi2s2z6ZVAFE6ZjwzDl09gXtgxujAOs86dA1NBbvRZflVvs6U45UPUSaEaKArDnRxwq64Clm9X9LVycZiCaBd0xQAUSulEywMkQhnlRev42WqfvjcZgjqpatOfBRFVm5knSQsg8bLyfYbO5c--a9h0Hn51lynqXxZfHTnPz3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD6_fjFNXvdLnDjgFm01Z6W-vPJmKCuOp4mojck3RnQaunz9EK5Ig5-Ufy4btXZjHchQTi7-MhJSsYaUTpeCjuuu0CFMgFuowf-5MS2IgP21BuKxFpoKmBStbwqDG-a7MZ0gV34bzgwJxfZHN5ckQKtTeX-5ryv321-3WslodC8_BiMu4v0jVjfv6Vy4cVkuKBNTuGT1jcjo4YUhzZkyRXE9NWxFyNFHoP4FPpfbTQ6EsmXuG13KYjeli3nb4vKzoaPTRdIhzJ_52OySStgctHhKlrsc6inflTYORauzSOGtUsi9nMGJJtqDQXEuSqHq1mobrSXNPb4XNBlH35dDEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SslqR-x5bPRlmQAkNmLDpE5jVGCJnPIbc4JLpTlGR6NzPW4Dopd__WuiPkmRXR0Yzmffg6oJhjJRm98qG8gXxW2uVVHOaCc03cRaCK-hH13sR4THDLn8B0pbg6g8EDOvEeKudirv84eNeyjZk8QUSnxc8hu1lH2y5ANgB6P-QeDYaYdHV2YU39kSkRipGEKy5rsx4agRu8f7cJp3Tb6yYDumvvVb5WykpQkL1YSN6E44crOrhq2m5wkJ-SnIOt6OVtH01sV65qGtvIJE3dTveiAPsFc2rDCpV1Nr0F5WOHr2EZNKOgJZVALAEY7Ug5jX-y6bzzLRwG-2kSSt16nDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSmF3dMX0GyTw2PjfuV_C6VKrj0ANMewNJ0CTiQCl0OQVcn3bjuCxLviD3A-SV5DMeSoh931vp0Dt7IHYtgo5awrNgMcaQPBWOXSZhtqXdtRTA1ULrScLOsyktAazcbYzU0xNinpdcU3PB8UpbhteRRhSUqEy188GOX7cilZ4GxxH1kF0uORkD1c0XT2s6SP6BxqrCnOKql0srsZlHQZDNO_eGOaX12KSypyd7wCj-VfwMcYGrj8-okTp5HDu9mz11MDye_GSsr5DzxGnmZQ2XjAyVd12Szz76Of_BImDg8qbWDFe7Dk8pLka1fRV2FXp45lbweo7SivITTh99AHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBkywH3tw7y9IaEOzDB04iDYvc7lIN9wyt_DKf_WtgwWSonnts45_ieut41wlGN5ZjQ_hxjMHLrO-WdKE2MrrNvOXEspKfrc1Ci7NtJ8U2KxypnoxSqMg3B-PllM0eGR6gBsCvlAiffkKn_CU-fhX-cR__zZHujf_25wHGby9ZCzOtsk8JOoDaH6ua42HgVNaEsdkvpJVUIQ1epfvTjV6rYhkaXXRAs7Stvtd8-Y7QReBzvBv1Ddpj-R4TlEhAVl4GRivtaAgHzXQlWfHpXR-Qm9oYr6PlVmmu8m2uClIm6uOLwMZWX-2G48G3C5Vk2138z5EBhRTM_2o38hvRzo4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3RnEzr_xOxhqVbYnb3B3qFpae1nH52RUWuhrL4b0q5YJ2ap5Xy377NVgL5QOwtHpw9B8tncQTezwzfcV4AFO3bHmT2Oy4ILlPNCE3AKuIiQ0tNVYq4vBo5_AXVx1F3zucKvBG0TMHXJZZ22b_T7FL9MQROvSwgnomeHR0mAQvnLo3_buAmQ3Ewhj9UgZ-FTarr03cYf3yqGefTMAM42_8qzvLQjHv8X7ERCDf17g1oBY3hzs0Ph8CxvXLLCREdqGDGQpAbwPKukpt3O4s4QaOjWUu1AS9GYcaX6ycsIKvipEu01pQlXsEgOml4oI-aaHYWhHPaq3rcxHBv-949Tpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMZkOdk3FaCFMs7yiKvZYcgwM7Lyaz-JekWE8BdZlfC6WSCl7kjOmAVoo7Ntkl8z5MrmLAOzlHCSYZ3sa-6_63JfFGOoHUmTQ6NjG4AHGULwt4CV0mJeYPyKxDJo9xFXfZiOAApPhrwpRg4Xbp7CEFvm78cmowClnE7BN-A-A8v2QFdOPJN5O68dYHPa_qJF0xFOSd8kEW22w95rV3g9eB7w5B5dymZpVqFFUdC0LRndu5kymzeqswYd6lNUol_MXBidr4qIz0QqRtqJ2yCv42_j1HRrDmnJzXdxS4uEKS5K8uzXZ_BpglG3VZrVgwfZZj8k68xwcl948Z_pQeDDgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/addXoYeH0sE-at57ZrE94ncRK5KgonzmyxWGr9EPb5cdkuc9dba38FnNc9bE8wjDpyEJJVssMmkjTtREQ-W5TvYY56T2fnu0uEnnFs5Pgow2NqFkG6QB6m1OvURZnPhLHQwy3v6VEdNFUM8R1c4PHEw4eP-ADZBtvt4DcRv4V8tn4Y4tsvRHwP-GMcvyN90J5WkUHSFNybJoT-sA5B3y7i1ZNV6FI6l8eUxByyjORqpR5X37NCE5CXOcmMJf-BRlc_4nVDbKcx8wE8cp0uetC6zxtrqcdXkKJhozrdO4d17wxLkluPp7-GdhJjSNjUmqnGHnzriYm9uU4oSVzGTAvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoFpP3oPpArJdI0zZFUOxviN5vIDu3O3hu_3TpOpfp5i6cjqgtxMCHlUwIQIE4J0x8TzdIoe-wz2QwnmmWPlfcuGmNdb1iTDF8-eJmI0BV1IonMN1XJMauRPD7Akmsgt9o2qoVc0Bkel2Izl1rdkFAEdxKHW57sKfIqe_OVA5jfHmA67k6mRS8hiKkN93oaH04BfdVrdcZpR8OSxJUs77ppSCeH0LJMxKZYNpCFgx2IOv22J9QsaxDrq0D6ZgcNFb30DxOrarAG9ZFMWy4oNP5FpwjzOCJxbxoTufXzqpHrh-Ty2qsNWHj_m6nq0YB2_4dkSmkY9SMxoifvUnm-HTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJn5aRKlsJNoVsMgLyX1iY0-Wx-bIIr8N5QkA-b5DtmW3hHAT-qEAdNCOnSkwlmEhs8LpYX6bPECG5venQdVYvKHEGnsVvh1jx9bX4mFzcMMCD_Lv32DIKsSpW3Cqqfn8C9pAJdMVy8yaasKJcCUCV6xFQRXqeWGJXqN4xDAyzDRfWl_BMjyfOTGAYfbPEcLOeM3xWnv4MlEDNbXZr79SwlHVRUjlfQjEx049OVxh6h7FILjfoRkfjoTzxhQ9nuUeyvj8IAWtd8EURcwLBTKjMuJ9qyDaiyvl6vbZvcKvQnC5WdQDdSamQi1zf9TbCxDtAkJ522Vm_0_1XyZjk8NTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHAkePzWHiKGUXuR6QxnfdIoQ-sGzNOgmVewDvsr7sd4d7IxUYYNQO1LhuAzWPBKmIb5XWTckaJLSzXMfy12ZEA3CwaUfcJ4N6WtXTkaRmP6VlNCOgM3C7xS15aq2bTWLqakqsZN_R0BHoekySPnVS3F-1yYwtgP62LWa8h12YaOsGLYsGB8RKT2bQtDZPsPkmbJd6ZcOL6AVBpgbIXpdYjso4Xdhvgo_ZlHAq3ADYViSbPPqDLrrwduJeRDCb2GoqZ3lCzab99-6cze_61Yy96knqCg3TbGGxOLdFzMvTR3quZLtm77mzoG1uFMvS2ov_OlH8kzRMyJv5NwqY8EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsiqW7nG9JkYtZgo9dK2OM-5J1V2k-QB5kqdLhgM_sUPwaaSTPqYgun2JpbCZeYodrltyBxBxBghpi2_sxEHbCCDQMw-0I1r2GL27CnDyFG0nQzlUyUF2WGMeuZB5A24juYMSZOvoBD-FgcUBuexk3oQ5XAXkaeJ7YT0xFfLI9UXnHbRdls4nRCL_jtr0ruDCiCnaoqQtP2Y8tyvkKKL95cscqPA0sIoa7qPcuuhUi87VZec6-iPZyXbcQzIMek5HF9ffEbvpxI6nTkYOfYNZYYZd6ZXxi13vew6f81dZ1M3xG1JmorqQTSpu4Aj2Z_QffwPi-S4wK5mDRleO2c8Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBw_PGnFX_9ywivVmoS598CoNs-2O6Do4STBvBpGngB6vQd4kyTQqRikNQjgQOFlrcmXzIQXaIWdlPpFOTTOczRxpzuNY01RB7QzfSl6NNQHlra8zl_LwktB5OTPF81N1QJ7orYxxNPrEH7Gwdu3n1N7XL8Spmt2qXbduAeRzBHF2CcAuc4m20o3LkFuRwNWsyseyWGRjQSeE-t3nkgfXx9epBup_yuT49_wX-716BJ-9FzvskgOVqq-MCbHq6dbIfX9Eln6kDv3kKCpBGRb3IAtqSQXCawBoVuFENoiVcB4eVLO8hojuY2VCX9JCwPR7iZALolf79okH6gbB0H1hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmKBKZ0pBC3jfSEycrfhyzytpUPEGiEeZ19U7ccZLkPudw6lKvnI2M5e50COeFWb2mebNq880Dzg3PhHYd12DPdABaDI-rBrAaYY5zfu1XAHepYuofu58JLjmNDHOjwHQTSyhaxbsz391Uq-IO8nC2TjU9JqrPHh0OCFqomSK8MSPYXFf2DFQrMY4_H6Ly56Ibk1I2oA9T1MXYQBgrY6Vu8Fs7FvVU6WgXNpLl1VbRfR82yr_5UMpFeg2LzGr9EyQMLizvWI5qn0dx7nturHNS7VLIIqaT7cgJSHt7pDEGkU97jgfxbsw_R2jNKUHr9Z8-xPKMC_e4-Q72r-HQsw0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMmvlU7EM5baombKlpbV8bHNnoc3AW_jeSnvTArgVowUMNMqvwMJ45dLwQ_5LENn80CljUcDiZSpS4xQj2A6morBr1EmDQOx4OgaFbBArDidKEK1jcoBqKc10agrYU-GT0w3-QVqDizzfay-lLxidJU0XvR57H_uDbuFUdsxgVfxDK8PnCNV7EtsHuGvMOMRH2OCnSYNcCkvsSzW8CVhKY1ytAPxX8RHGgNHceC9u2Qv6a120tE-7UDdIzO6AGTkkPiVRjuctohkS2PnGNXvihszgKNicRJ-ekAzThiy3mnCUbHZRIgKRDz8q6JaqCi9f59FJT-D3r6V4OSbe_jbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjOBtu1pL5wvpbzLLh78mgHgM3Hp0ac8QXS3XDG_GBB8X_f3m6OaLoibn5_LjIoLzIq-IcXS-rNZ9vtgHUqoKCqWx_V68T7Nz4KFlqTkx_Yo5zKWu1PEUL5cQM2YD9UvEaPBHfbEXIuaYBiKvD3mtsdt63AIebcu2Nhq0lBROM_3yeLoGtz7k7Nhetbfj10RHyAkn30RS5Nbhu9tX1CozG2WDDi06n5uJi9gDZ6nopWEGEJrre_Vw4tu-DviC41En3UCt-8n-WEl5_0pzzd-T6Q2GjSssRzrYqsEEoatdyX3CxrD2-M6KEcO7oKREceLUD_TCdNt-QgKKhLSXVWxWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBfFf6w5gQH5h_F4yVW08AOB9watKj6XYLB9U8PqSmveRMFdwwl8ERW96PtjgyP7peAyzYF743sJjF5_Os2YVeryAk8l8xkPO1EieZWqgdS2dDU1GhDLnp6DYTn-Gx8YNo5u8ICnfu5q9DO_RPFGAgvTqceudVXKj2C1rcYcgAPlfTMZSn0bOjq5tBEpUZk3MZjdJ6eJTnMr8TnX4RPFilPbOCjsKz3FkuOSfMIsr5SPhEUUYDaQPSiF-U0miJB2s0fR1VFoT4AZL2v1RLnsQ1IbhsxTlUO62B0Wn5scbrTYUt0WujnDQwyEfmCQvkxw67kFZozZ-W1Cgq4nOgwC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbNadXnQT_QHU3yBZX5byf41g7kIO71Y8kyomPuFcpPxUw35SCbBL6sDPQ4NNUSTMWNMOKGCv6BHFaNvLE8gIJvM4MmMn1BfupRk4pV0SRnItvnN5WlmbNy_k9W9FpEjSV0oPCC_-FceVyLs87dcnPJOEYzJRYPzJmRYuDbUGyvHuH4WeKojRVKg07N8X9GqtsJhB8sxSJFgyJ50FKGampR0RMKCc6PJHkH_zs8xo7pEJpA731u3AiMgtKdYj5TTlHlwQ9NEd4jCill6zJEHHaxqRlnKSu_NfrHW8-R14g_7liE-zXKraBZsKAugm2are2_qACdJURPdaWvTI1uOmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-a3IO9WY8KXVeV0zfLqhZA-3HSa3kEJxqg8V4N_p2hc8hfMT7U4y79gYV6NlNQPyP5xWmEAVfgw6WzxACCtHNKuhFlR644IR4Xm-ZmTuBngX4-BXSg5oc0qm20OB4ug3UCbMrxstheDIH9NJhtuthtWwLKt4l1ngJOEuwhBw2hPcmFKMEhEXGSj6rToVkQM3tfAVd_oy3eldNmQYLDhfj6mdvGdJx_rI3TmwWzaEMR3iVVw0nBg4pmxKjB1rYm7fk3j7dYq7czxWd7jdlBn4GcEBEdPyZYHerItiyi8KNM8az9XtJiTkg1gDxK42vV2w5SLKVe-65Jqao3HG3iSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgDsZtFDPFdV9KhP28vWEu7el9IAzEP2UnwswfaZA5BOEWdNf3S_LNalmeqLAD_NyMdjlXSeNmFq0pCRIFK7QeavyEwWqDAbj6iYeF8f_6oxef1zWk-2AsMttphDTRXGeKJ8ZKMCtshXpIRM8Z8sWGD3O094qcDF8vlO-E21RMoDlBTFKWmLkLVI05hH4VPR_KzUw_ltgdytP6_z_45zjcOp4HPCr4NtGuN8JYgo8WCDVu9XR1vi9Iz5TmFppmxBBozsYhJ1zUb1xl_RvhPArPQXr8kqergqz__MzI3eUSs8cNuEEt_JEamC6gMcItSMdl0PWz0TfUDqA9Evxvs07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ituk1z8rqoKxMBY0FlNl5h6e0wWb2rd35EvkFDay62N09xB29oGrAhom7KelEEEpRdM8xQ32waLFbHwtKhG3ME9jg31gTqJVsIt3kJsifz6WBLNWlIbmkhSaRKSvrU_eJLc_vmST7FV93gLqEhFVBnAES24QW9Afz1BRbmTf6XNwzx5QdxymvtbV6g4hE8cKziodzkZB5CLP_DlPBNcgJUoCEfqgj4yNGZ5avgS7_84CM_Uy-20Y7AMKCxw8CGNYnIlvAYB6AbL3A6tjqm8Gmby7Vn-P29Xr4cStafvcmNTf_UCzICMDH-EBX9KOqZX06_yfWzMoDXiesHsfDm9C7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPD-Q3kUVaWiMMndGdTNhumFzBEx1TTyNvVRpUTdqERERinxcAU66OZwI0piJSVra3Yva85632XkgIfu3dOB03x8wZdVlKz-jhPihiqdRCsgIg-USzslO2lTyelku0GhCReGYJ5nam8gNFocT5OS0R8227hOwXqep_4UP8CrvRK5Oe4zBozGi_w7crilY9nKN8ECAaKmPu0j3YNISqF6DQxNnKZ3HLLg6gCRHopTvpX84ZoOGYZrK7t4DY1YeHeYHAc-uAzdsiSnyqHKF773SroOmp2bDBp4ZDNGjP80E8Haqh2EhjQpOH0-5mdZpuLjkMqUnlQJVzatr9EGx-ArLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLCjqTjJkHB7CldYdbkn7FXeVrCUiLm3xPGd3zWpBTqa8xT5MooBcFMfqxiGZfFpuLbAoyMHaJ8sSpzKEVbRWgZrq_J9tndkTvF4IfnobjgeNmpUQNKQy5L_lZRvqvMuoVq7lVKViNFzkZlAFXrOD7EgatJdtXvShtljVs70dLjrB8HAZIoYmedUzTuv5Eul2u7vNKqV8Jx3M5UVlGh4mmJpYcdyzmWDGK-OCuGjW_OT8BCbLuWjWPPwG4NxcYaZz7QghnZLCqVj8J7x9BQ8KoNQOx0x5O8aR6PRGMW-SgMS3chGMmYF3GL_OUdyCejDB1Wh6ohOV0hFYGz3fQFT_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdwGGrXGoWwkDTIdXbYHUBn587wVViD4SHZdG5aC-foHhnqDwFLtH95z5qAsXDnIvAAZd_ITjqVhWTLdoj7y18lb8sGgQfUAOAZNuDJKTAf88TVHqxR2bHBlZHai_RzwtY7I8kyTGApsVQz35_RVfdYNTVMDWJMTw3ifPcFhHxNuLHISMbhUNrRCMTKelWjp3iZJrOKNECm_f0qK7UCS6-aDqNvuPD1mKX0eMIrbWAPqHuNIq4Qu7NN-Gs4yxJDlGcpVVjrD4bqcCi9TqppI0YW-PbuQQBOdQKtA4GkDt0cB60nyK3v1wpBoOCWHsHQSms-bhQFYgsrrfwTGbDVuhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBxv0yHVKGYvhjWQ6PWZxf3p6Ar2Zq4Vt_lKKOUqUc4IUISzuNp0pRtkTIT8SKWAISm_9ndXNwVgkoSCVUCXXN-mzLIeZQ-7Zt1DFADln9_pEdPcotGwMVcT3LS5wKGlj5CZ52Eax1YI8mt8ao1Fd2IJ9Adp88hgV9Ms4VS5G7nFWKhB4nj7Yj1gjGK2GVoWx-Ps4CIAD8-sN2jEplusxJ8K_aPXw39t8CDsFXOJidL-I8D-l-FaVKggxPPqRp0yQFQg7bvMzUOWipBcN3yCe2WLGB9zpXISeHKYnUZOV0W3w3IlcQBLTxPbdtW6rdW89C4lnjZ1PX3-LGypYu3Rbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyrC0wZHw4Tv3Nt2946sm5hhh7Y4x-xQubo0o0v0emVdYIH9g443hdRhx0hAfFqXNUwBMbho4XE1RtM36H6JqA9utXjXa0rwQ2-FgembI0kZ4lIxe2xwGKXcjs4kXaL1z3Gd6m6W6YV0EnRgsANUVdymOE7JZy2TRB_HzZ_xwAViRTq2M2dqpCG7zCzH2ylO9Yb0LDcTVf2JGRm-jJOZZKC7ZVAg4CfRXDu_DIfZh4TY8LqjjKxGSDBWDSCLGgE77KfhtQtqaxlUK34qmXXpHJ-gx5-eztsWK9WLVqSsaYcewJOWJ0EfR65POzvsZs7AiHAkN8ObCtKGEg9V7r1Dmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrUdJNAmuqTdWgkvq-SFG4QZrP9k8qnY4ImENT6UwmBv7eiagfHjsVpTHwynRkPi_9BliTRP70vkQqpsF9ei3DvJbxYI_IIKJ2TvpmWx-NdlLzE26mVcktvnOWbOWFWkQGLXSEfA_X5r0OjhL-A51DsIR-lLofOcuwFXFqWVGcJmEAQX9QtEn4_M0Eu48mxj_V3TFavT7jhHSjIsvNfuOKfmgJ0S3rFs-qaeKW0DylmkY6Gc6z8IUk25lOuhkcxECtI6g3WXHh4ceTB7lq9bBYJSf-DT9bzfSrg0oFn1K_Hbor5GNDIDdecxAWF6uQ8Nf4Km-BC7pPYfZgccVyou8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsfTo97SrC9KYW8uXJT7NNWraw6mSNfpkFKIE4s9J3BcgYTAWYuSwIvCfsMDe3imzi2__2xrvSXt6HSH7XOmHwXhrC3OetSC6W8_fgoDbzdAvOLwP9QS6-6vDcK25iCkCh_eQRvXtNPcS5JZ5ZlaAycKfTN1D6FCo8JpuJKKuiNHZQTY7lf0ZqroiKjdB4ZBa1eSazwC1EQYyLLDXen-mgXb0Wy_kRPQQam3C9UUEPlAHD7pIC7Cb-IFr_DNXkhuGjWZSYBNQh5aPKXA14OJ0larKCmqTMg27Bzn8Z6Y3uoGOjXSwy3MGamTt4oQb6ZpWq4wdesHRkbNFc8gljywtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=fnUZDMcUa42Pq_4eHsOUL7g2RwMcuEryPlY0VA1b_OtIZIzhJeQf3Gc_6NRMBfBU0MSMslVXQb_iHsQg8NjM3laU6oVZ-MQaNOGME6sdo0cr-WNLpYJcu1KK4ExrZ75mHCwZN_3BGcd4K8DWLtS4UZbXCmYEFItv6ipDaYyhM7Cl_FGVK_hJE-00uVJhjtIm95u2f9Jbk7HvoOa3XiY_GrJtvxAY-U2FHLHA4SzQYJGGW6QTKVbE6Tr8nsznvXpvdkWgJZC2861HsslhXHjLq8OoZtKQ-PakZxSxyx_wYBqtfO7QD6cH3nnXyR10NgFhWXbCjr8iVxqXpLPuhIuyhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=fnUZDMcUa42Pq_4eHsOUL7g2RwMcuEryPlY0VA1b_OtIZIzhJeQf3Gc_6NRMBfBU0MSMslVXQb_iHsQg8NjM3laU6oVZ-MQaNOGME6sdo0cr-WNLpYJcu1KK4ExrZ75mHCwZN_3BGcd4K8DWLtS4UZbXCmYEFItv6ipDaYyhM7Cl_FGVK_hJE-00uVJhjtIm95u2f9Jbk7HvoOa3XiY_GrJtvxAY-U2FHLHA4SzQYJGGW6QTKVbE6Tr8nsznvXpvdkWgJZC2861HsslhXHjLq8OoZtKQ-PakZxSxyx_wYBqtfO7QD6cH3nnXyR10NgFhWXbCjr8iVxqXpLPuhIuyhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt5sKpFyB4-lMnBr297ILOnzXQ73TFPEy8L9p4NY9SN23BWQ76OEWtC4XptX6m6pc04cs0Ni14WzyexftRGJ3d3o9zJ31ujY9pM1Wq0oQglwaXwETeT2tJq23Km_isKLCpia4-Uw7ngrGbLBm9NmGFEvpR2q4dZsVil7nmdVugnDDDx2CIjl4w7whnPt1b_HgbHt3jJmadcynnZcOt24VPw_Jw3KNG8bDWnldX9sOR__ORoVDXeE03k0fP3bzcFl8xkrfiiH-Q97YvFxD8XMc4mOqXLGjLup2J7n2DsqUPPykN1RFtIin225iHydBIT_EaHnKFMqeQeVkI0QtxIc6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeDaV7E6vN3bvv9AjQHMuF1B_dIIEZhAh1FeIW8-cEo9cACT6IqGDiV7kn8fsBNq26ZNr9hEaQ3c91kAh2CM1EBT6NBa1XMcHQ1XcnVKpvyPyP9RFYTAlO29OzwgQ2U76KWLLEf07Ev2XZMEHEeE4ucRUv0XmyJBpiD-f4yXdMfTEhiwblaOCsdhjFVt3TbZbHeawsMafTGaWg6yT44ag02V1tTD7z1KWZQyFnQgqSyJyTs1yAHvIgHJyP7o_UhJDni03dbDmAOEVpXrTBxlWyonmERL7s8dlzU9tGu-eSuXAslqQkb1XwLYK4vnp0sn-boYbK5FGh8AKLtyPJIypA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoTSje9TUnrSZDAoawE6HbjS8Ys8S2UiIOXXr3lm0zqewbyNLDe1ftdLP75w7v_ts-kP2n-K2MfzrAKKjmx0vk66LehM4frHTVjTqfgq-rzFmd_0t2IQJP8e7jS_Fov-tQWOskn2eE0IKPueBE6DvpYr3qJ6ojX4nDwGx07RtHYn77eY1eqoZN3jaJE5G5HteS8pzSy-FafdUz5nNZbLPeXpPaf9j9fCuMopARYujJP1NiUWAODoBGIbCQST6rWJJ4hW5wPuPgohKyA17su2LmUX06tb0L6Q7RMTU5_WSzUxjllVyJDz7FT51Iu8kMwtVqbFRqVDAWs0dI_aC2sCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnLir2zK7-yQ8exrYBSZPMjWfI22lX6glVQeJwZTNbNmfuB9y3LVORz_4gksSQgUaL7AUuxfEsOIu8qq6weDEoBK4KO6MAE6PvaZOm3q_l4dCxCU3C_F_Q6f2U5s_knhY18HSuDG3-T67FJxvj3-0gwr8wiWohx4c1tHrTbA_HDn-7N_6CJXdczAQiO_PiXm8icOfxYfyCzDFhQM_bBUBt9t1ErYQ-AR42XJ6CFAcHCkY1o7CGKphJfLOEmViM2cp9LN_8_GyBbH5eDw779w4wdELjO9W18WcalvjPjfj5Kf9jA7FpNn8eobO36CyR5ANoVhhQv_HOxO-mtb8eMbkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEXqdrYx5COffn7F_3MLWl8VfIF_afyRZBF0JrZG10sK19HNVUfWMotOM7H3G2dK8drCk7gQxjngeAdV66GJSZ8CxWm9kjGOVAK0iDZ3fr4Yvq77r4qJaN3smVOvvZbJxqTOvwXh8WjdL84a7hjcsCOi0bTv7AhhoKuVt5FhoZkCPIi1aLCFnb9uFHnmHmr_lTKf7GizQiUzAOU3Z3f3pAUMdMsNjMJKQ-H7j1zF1BOFNZUzeGSIvDSnhQhgaxV2C-Wo2FgBVAJhZzoy5nt5PYyex5WUrlT_qUo509v_NrdkQcgd1K-bkYZT9FHz2j6f0oGozm1as7JqslqxMfhmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaxFKPozFiIVDwBNVvZbTSP0Iz0y0Z-4lJbGpQXg17G7-IZBAh3YZzqzDWgvnW9uRT54PXd_CZ0f9tojgM8r69NXh3J6dKyvjqLRl2T1kFB15rEbCJ2rYbnFGyNBG_nkdHDAmvCsOolSNumyK5qTQH0C9VomKFVqBIhcEj5ya1vMzGpvha8VKTDx3Ei-zsUhjSDuk23vomw_toNGEeyNEKH3QmJ9LVjJlz5HOf6GzXIYeYzPGDuF9CHEF2Xy-BqpA90GLgQNVTlxS85ztOwbdqxKhdX7KPTIHF4Sw9SASpPCPaVJbXZsd25aoDsSjyM9xXh_j7-c7beBgh01ZqLA-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=cGrbLBJjb4F1A6oyRnALUm9o6AoRoVMYnzI7coR57XacAmZWh0FJOw-ccwh8x2oBdNfbnXEpooULswkFvJoZ31r3MIudemYPBtWXyEYf3R_MyUo_KDU79c9HEDgrG9cEFbdNCdwy8vC00QPJHcWIQZRFXQ7mFtUVY2roQ_dmcLwb1fWv7dLEjg28nW2QOCrWVk-cOw3InwpQVL3iDskKrERPdLbIAHxaCb3Sq31Xatzh9aG0NPsnxtQFBSDjHaLwOdkNgTmL27zvSBFkqju2AuWzjnlAf_j39E8nlT-Xk1LMGUlL8NmFGujPjmGdULLu6D9Jmacjh6mHhEyYDGj9HGASBeq1n79JIOHRw60Dk7o4NjtBFwUnw_qfZvzJ4Hrmv1IMzRUKgW3rUMxJX_LYlFjPNzLtV8oYLcqGkQdnt0jHUBEKTe8Nl6stDmlQTcFeKPMNGH10y11M3hmE0bid5RMLeldnmcwAfk3Gx9xuuTanbyq5b0ZnD05dW5aXopzD6htHDme19eEY6X1eeZC2aX-mYXMo-5QeUk1ru3hACHMjYA-QgUj4dnFTLwmkTzxh_zQ4UPOcy4iag3xKbnU-o9oDy7GQIsU7OZ8aYWgh6nVv1PpSoz96lOEk6BmOifVE-Eik22jtsp5StVEWyYiHC4arQyCG_gTdyFKAgBY_TnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=cGrbLBJjb4F1A6oyRnALUm9o6AoRoVMYnzI7coR57XacAmZWh0FJOw-ccwh8x2oBdNfbnXEpooULswkFvJoZ31r3MIudemYPBtWXyEYf3R_MyUo_KDU79c9HEDgrG9cEFbdNCdwy8vC00QPJHcWIQZRFXQ7mFtUVY2roQ_dmcLwb1fWv7dLEjg28nW2QOCrWVk-cOw3InwpQVL3iDskKrERPdLbIAHxaCb3Sq31Xatzh9aG0NPsnxtQFBSDjHaLwOdkNgTmL27zvSBFkqju2AuWzjnlAf_j39E8nlT-Xk1LMGUlL8NmFGujPjmGdULLu6D9Jmacjh6mHhEyYDGj9HGASBeq1n79JIOHRw60Dk7o4NjtBFwUnw_qfZvzJ4Hrmv1IMzRUKgW3rUMxJX_LYlFjPNzLtV8oYLcqGkQdnt0jHUBEKTe8Nl6stDmlQTcFeKPMNGH10y11M3hmE0bid5RMLeldnmcwAfk3Gx9xuuTanbyq5b0ZnD05dW5aXopzD6htHDme19eEY6X1eeZC2aX-mYXMo-5QeUk1ru3hACHMjYA-QgUj4dnFTLwmkTzxh_zQ4UPOcy4iag3xKbnU-o9oDy7GQIsU7OZ8aYWgh6nVv1PpSoz96lOEk6BmOifVE-Eik22jtsp5StVEWyYiHC4arQyCG_gTdyFKAgBY_TnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFUJ0d_KE9f2WvuuwWS8F0TBEGBMqtCfWgSa8ncMx97HLNPekJFNowl6S6Uj3Ec4lVwFT3VJN_SDb-r-DEil108wCtAzRU7jIy1bVymkkRazcz0DzTpRM_gOHGLjI5I9orVDr9ArxXGLnVQNoGBfpGkYscRlAD6myFAjCCJQGSOBJhx1vwuZZMbIyHJHlYP7q0fmFnmYZkQ1afTXVStKmQxtqJk0eLuKABMhWZR6IOWNPRRdlaT07LuFPJTLUslIsScOOY1whXoeh_pecrGIt2AjywoD-dspl6vVKjRM9Pbvi9Op8DsxmQt9yO-Q0hDgNcrO5nKVgGSqTA97z2npTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mc98dlU6kVyMNVMHZEfnyzsLfOmC3k01Z7FmR2XrxCGwKcZzkw7ER5NtcB07NcGGbeORvN1_4jezheYL1ogMWClDPLEOt9y9QNqrLk1SLC6TjIFbbeg4Dx65tqPJy_wh5kJMjqvBJdxbHTF1QWNdQZwA6ywIkQK2OBOxhX3hpCuLq13aX-zNI0myo3irPHRVrV-ZvXYYBjIL9bGvI-aAtio_FxUb16oV0XUUPANyO0lq7Cl83tn2MH2TUdtx0W4aUdnjvTBosnIhjuhxWArk6lNJ-bauJQIRuM4nAd5uCRnw3ht2T3o8AfWbTVJPVAcykiDKoX68b5dbDqBU_Mo78A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyyY4YheFu5VVQenzcIg43PEKrvjs7alkxyNJuF5zCi8uZa9HnJKGIDbywqTIpR4I0ZqRkoZQmJ8XEq8ozL6nPX6LP5KDOWba3lYjpeci2JBxHYEFV_9Ex-2cpxHJcFTnLzD9YZrijenHmJE-uUToiOn8HgCTMg3pgxkwaJF60LwMX0X7mjt5CDkg-NqWcI7xapxdM2VXnBMuOjTEQd19OMfRvtp5eu-If39Jh0omkp_aVy2qtpcnp4tXgOllO4uH7ZfHWbvZSFh_IsMpSSwY5YVbIqmF6NyGZ7DlHBhQp8QlMVCbPGSUfj0Zh0iWrvJBnTSskeCgVJ_DuYR-skL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LShgUrjzNw8nOXGEkav-Z__SjUySOnxQGovVfZan_mEMAGB0f0XwOJWDHG8WszHQPVHyneq6Qk9qquszaRvKGwW4XH3MqJHHA_HT7Mm2Vd9rTc6nHX_8fmGe0edILaw6s7yaGM4CSmpDXCqehb_1AumX7oijxpUEcqYIAFQ3XLS2ta2XMzAC1OeQR9UaVKxkSEQGzZ8q6gZm1CVDl7rLJW-DsvnY9_ZFLGRBZVqHmhL9cS6SJIVSIXuHiyayNbJEyqndjylwxUKbHqLl3eyJVbZsxRfIymbYSD_F63KuSV1J8Txr47-WMxHgHpctg2jYv9ZNMMgKHvmb_CSFW0SWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3HZswnI7fojPlXlDmjdEJ-WqTXQ6X1f3I5rX7TOhFCm3JCd-kSSG6TI_24MCX-ZVXdGBVhLnobjt-vTMok7lg-0PJ0GhqBgsIdvgiVqpie_kPsXSCF9yhwW4iDmtJaFa4oqiPJ9yGdsINFh6nDugif9nv1gE_tswN4lg5RCN1kBq6tMBkh9mjin5SJmzaOPq1_KZXmPvwMEraFk4_htenHODZhoLI3CSMt-Ehg3Hf63GHbf5YOTg4Gy9_C6rZBX-1gGxVjO2JHY8iCofztF5xlHwpovvNKbo3UXAbiNsAdzii8MorxKFAZD97W3ISQR1DaL50DmrU-_Tdf3DxqGVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1ARqAiRx_wypuKW0EAcwwMixLh-wYomyp8VfSG3HYx47OXl_x3cn4yqewbVwMvK-BYb_75hdyNnW7pAoMA554rqwGcZqxdR0vNZ4LgCPSLTBDmfsmhBxI1u5Twh_JoMjW3ogHVSR5YRDNZjODoPvhPzi544SJ-6zAO8B2JeTfU03DUOp5mDmxamKd1dRKx18mnBABFgMZAVPHRnaT69Qe9_FptNtfLecp2_8_5PD-DaXZfMzvPzmSzY4eDAVkEx2gHoAgbEtTSBBqrRyYD9BId_fta4QsIJXC-Au9t76zf1cJ77rrAd8f_OpA_nuyE3GH98mi5ibInsM4nC_CVTRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laZ-Pi8ywpnYk8Jy7X-6S1JKC97YRAmBdX75F32HJkrWw-FaivfF2isElpo42lUChRuC4L1LzTApYgEF0QOiIoQREiwXUk9b0A16_ZqJWe7lbKUHhCupiTWDWpz-sfawp7jhhE9DyQc8ebaVp-0ettK4zR-mK3AcLr04JZVEQhoIAusyWqeIie9TKV0ttJvTmoKsGuwGBDTMZzW0o2BjVoVtcXADU8EnGv6s192-jl71ZICdxUD60xmBAFdGZ0ifBPzwDgXUKjat-lAIpr2M2PsSM6MkH4riXea7qh88WGXhcRmHGiub-XVvfAU4b-LA1BqVizgCbSYVZmdaMrfcgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vgP9ogTnqXAPWa_oREEzMKESBhTjicnuoD73c96QfW53JKwywLMUPow0XOf7dm_wzhiQPQaxo0wq9Id4h8MYCSgizG5qlktTo6bfZoiDJa2mR3gjJ-ke0ePyndCQzX3giyELxJ6EMJ2DSgHl5lNcNJWjypc72ZEHDSltVxGolBlYQ2o5d7rhKu2-KtqBZr3VA0cI3XsKiBcge9o4y0gN08eOf9o3ygx5QmodRq0vrI2YHIdCQHnZehhw7fu1_6TT-Lpwk5ynaIipwvl1CNOhnLKOiCsyy83_cJLFOGUc2hDYNhx9kFeY10H2HOVcnDChY3xcLvcFpCAqlVyS4fZhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtgR0p2IhA3XtXxLsQOcWzo9I96EtEhkRyJ4A76xQ74TYr5cSRuZebJX2G9NDnlt024Wec5TVwkQldh4ZHwGvGl5vVkEEHlPp_8EWmXO3glp6V1jZpFIOqZc_-NjvxGxF1eNTncUyrB6Uju14vEsFXPI6LYmFUIWY73lu-_6L0r7fosqvurHTADzXdshFe5b-fs7IxVRaAbFAkjHe5xavM86Ny3lMjCXPALAgO48EvqOoGt6opMCzMMIcW5WaG_BSND0MpjjS8AzJxeLK0h9Qhbogp3RaGXhiuA_95NffgW8AdpURq7Gd3Q0nCfNLeyeoEulS7qPO5yJpdRO0TvrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTpFif_MNfRzxtGRVysrMAj0upPy39MsxKo-5aeqGWbrhqt89IGkK1iSR9Tgswea-IHWpSnlluj0fcsx6BO_tmFhJ4wEzHJiOHUrpquwpcJTCFBmkUUg8XN5YvpyemqQ6fBxP2KECy2LjHuLSnZXLNhUl37hLPPAbR8UtIt6iY9vn4Bk3IlIP-ZGoInDkNAtY0mTY42TgdIhcu6_SqgFEPsze2n_PmX0dSlVaxVsZoDPpo7_cpr4bywNPQ_2g7CnTXsonfdX3IBN4yGgS8v8gji_Qw-0_hTZ5z4k83xC0YWY1b8THMFZl4qPpv6eUP5lFQQPWvZPNv6fAvfPn2ChjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrltIF8cCwxeaBY13ubAJaSe_DtjWmVFajFKOKyTt3AEfJO0gRM6o_qnlnHR8IIDHyXmvFbvkZfCpNsSq891179gt7tFJC5rLf9bHij-gXtLyP19_7JlTwMBh3LvY9bEVeeByqLzh3dtOrIboeEHvMuUzm5eMgzgCcD-QEK3FXpbeT1yPnuDXtLXKmseN42LtnahY5RWrcR8ntkChOYH3dAOitZhM1ve0BXG8WqoM1KveJ-e3JoJ0LSvgWrClixh7CjRsS9SEYHcxZduVV68jsrrpsEqE0uEANz-KPn_dsXYP2TUbhPycWOUYh6EH4EnldNWCY5nDlE6HoQKhFGFwA.jpg" alt="photo" loading="lazy"/></div>
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
