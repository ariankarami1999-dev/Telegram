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
<img src="https://cdn1.telesco.pe/file/UhEiX0junVzt3OWNp9WoxPI_L8LLeMsHhfLFFZY3-bfSZKSvc4WV23_AlfjckahkVwe1cvRd0KB8w9EZH_yAoUqGz22AsLPeSTGQTg2MqiHCDcgV1cv5dii39tLQVQgI2dvv1jUxXdRfFbhS1tGsZDwbhi9d3tZfURE3KCq60Tb4vWxnrELcI-eRM9pBfYe2Sxo3ZGn--JhFZruBsS3LklMXVh6ql_rqqwXhZzXOaavm3qR8cMU52ZaScqlQCO5bvt4OBYNz03MJZFe5IeOwTIWfFsBZkAorMfvZJNvIlfP91ds37lUfCo111G_DL2NnGrPQG5KcEjdoeCyq1xfJYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.2K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 09:00:17</div>
<hr>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hp2Co08XmhnOo6cW95udP8-6hztuUiijKUubnLhyzbOkr_YskXTkYUEp82VRBdQTjNNSmDpKMXSfmdUSjxSiCgYGhGVfrchOo70CbY6TrbZMeeD8hL4aAuLUV6oeV5KWzLqqLfC9U6P4EFm2IGJAU2XRre3ICo35wl2mcT6d2DkcM6Pxa2By2ZcapRXzwU8xf-qgJb2My7Rwc3hYjY3tLgkCXlkmnp_WvYTcLvWycO9h_P888XKt8b6btRWIkm7OBXJ3Ev4LxZDftYV9TriISVtOb8ZWQXeaK2o3wekLCkhIy1OaBD4eRIDPnbzyYGRGPeR85Riy4kr37NeENArB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nug2T_qwBXAqI1XICuXgR8WJF5WeBPIfyw-Tkku1XgRHkhVnULCc7pRP0KW1esqgVthXB4UUE_EjS0Ze667Bpy1OfRMpwjSrVRFPyiRcDPc7T4pELuCEAEwaLYT-_lUKs7-_w_q39Dlh1rQZ0Mf9cWUTggRKYqhL0vlUvx_bLPPskG7Pq0dKNiIrALJlqNfP-yjvH1NTpFTiScnOJI_OBEh9P7B8aGGT3oWerwBZaSEPZBuHJXBQ1wb8GaWNxUbAtLc8WVgByMi_Wa92SHXdp4DTzB48iVLA7UyGZlSZdo2kEBIjmr78869hWNQhy0juZHNoaepnMs5fobjBtyVrOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vzMfLPiAz7e-VpoUqOVC5ukSnE6rJYstpL2FQEvL6qaNU3SEu1crZf1BBtLatGlk27EPxf13DvchrsJEOeTACAU3cmY6XL09fdRXegy78r1a5ENeNh1K-bsKAvtPqplOKttZC8qZmrFkMtG6OAksjosMBouBiOcZIz92K6_wGCXmu8h5fAMKl3Tsel0xzUEHH_1V9BTJLMOjwNQq3gdVDoIntd8dzwY_bQ0bOAUmpa-KWEpBisoKZWGrNzfsksI98T1SM04MdqZmgMjSW0OeqBgEmmdVdhjt49dcgkl2wPFhRNaUGd7mP0k6YhqkRvtl2HFRlrL05VMIVot3o6P3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JBtM1MWwEGLpA0wUqaL9D-vNDKVAUv0a3KygVIOM2OQBvT0_dNr3Dln5OHHf6IWMKwiJiKe3F2SSzGF6X4ASkXMQOCDQQQ1q13S76P7fbuYptxxwf2U5AzJoB_uCdpEPNdvaWky1T9Z6aOQwbgk4YPyA24F61IjumzoSyeSf64fdmoPQaoGx51LQ1sR7Rzc0BnyNlJA08IfT1PvGGMtl_V4WPQu2inNO9YO9NJUwMa8Ls7-q2A5vZ7q7pMgB7a2QP1hWYP1EP9aRd_7aEOf3mSWj4BNPxQoMqKMKOjzye2HRHASOaJpGntvO9AGtb3tyChpG-4_-B9CT0wHI5nBN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAZl4nx2va7Syi61r4KBAzB-bm_yUuZQ9FIcN5Y4Qh7r999k1rjjL0H3i_9FbMEN27-gVeqFK1-bGodd-zJ7PVBEDEd30ymCzcUxkf8EY3OD-7eqSf-yanZ-ja624OLkydvAj2cpeFSqKo5a6lzuVvk3lUEfz0ePlu0Td3JmPbc5otRXqSO37ic1t3NQeEYDDLUjZD4OJy6Io0TULZHhJbxHF19bQ4tcoZi-rzFKIHbc3_GR0O1WCP8mXnk2oWpCaFnbbmm5sGcfSVIX3S15p5ARo0vtcb6rDjZImazYD9GdwpBUhSzqeIE2d8YJa5oOVfYagBy9fnFiGiWlVsKyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aclUE24Az7LQmnCxCNaMhz2LQUQEg08GScOuRpoomDS-Pqcy4NvpFCnsTN_2SzYbu5F0t99KQ5UQRuVeGpeh0RUcGHXHfnGG96xBYBxDAQCIYw8oPsOpwzPAMmR85lhNNMFQAaUQ0E1LqaV_Wm2uE2JQYkaLU_AVecCORCwzl8pPzwuXncusiX3V30Cf9AeZgNI7RVhDyITI7aGdXzReWndr3cqNxeBO9b3TUqU2ue_r5xQgqc1SCryUW7XltHNarrATQR4MlijBWfEcSpFdMFW1pe4hutz1tgFi_70Qw0yGuReu61S58JGK_SMFJlbb1jtluMgZlYvwVNDrZt0aVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PTkDMqqsYVc-TqLtXZ7jKmj5cCm2t3YaOr3KH4WhHIb3bUGtp0r9daJSPyb2K4HK8luiJIGIGY25_pDqAeZiU1tJWrYghnBNl39-QLz8snSk2CCXRNLdDpPqsloI92hKSm_67Zvq3P64ToTT3AftIZqu97RB0gFt6jpIhPnIYgIkkfSeKsRelrIx0sxOZrT3AXLQwG4VpHpx4ZWH1s0QVqR8NYmlBOZb6ZNAfEeLcKLEF7QCa-V4sJMb2zmy3dV6Qk3j1m-_OGFU_ZO4Ydx3HF4mORMMUBSS5QlqhU0kfvxE-QTpg6jVAZmRS7EdY2hbhNQ-t3onqSbwaMfFUrTWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IvlDQExSD1Fp1Ogd4GBdEac_PQVWzfOHSSO7e1lFM5eVx-dD5RBgm3kM-tKGRQ4H5h8kpJO4hV6zHpb3mImxlUXb_Ia-9MIpkF5SENjPpic8R7KeuRdJCSBkVDxUHAi1m0wEi3Wez2uLQSZPnUZxW4aewR5iYaNuw1DvTPgfp31vt59UxaJXaTCrZdNwYpmnXYtmG-t1uQfoPSnKHjpf4RBZCRxt2So7ZndIQNXJTtky-R4KDBw1PZ1O6O-blcSe8KcqOw2mSG5xfZEgmQXBVB5yETBmvXl-VY2e_6uoYQENQgmabBjt1Vkv7KeUEFLMn4SI8UC_5wpzj3Uf-V5Q_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CdQ0C2nAVYS_jDnL61dYNDNXvMPBS5g_mB_bF3sFjDEx8ZnHwlVk8cDGsVtcY-uw74zcTjgLfW5vzZPXeAzDLqA0QpWyzxkDE2YllRyEK7yuaAcf-Rc6XUJwmOHxjYy8Dk9I7Gl4dbIX8calOKlbJeXS5DdOjrrLeI82rxftsVlQJyhoARxhG-dKiwSbHa-0XHJcb0vRFhOgtZUd4WsBXhwiUJPF8qFZPhiLdSOy4q7Gi3SuLX8BqDw6YcO5Qo34IAmSFrWd_vXk3qXrR-QyY11T2tgCO9qLvOB4BHZ0pnsj2qhjL1qlXqZY44BBe66MY5Vu310PS1XXggbPFLwpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsl1H8eND813kYC7xG9XzLpgRFIej501T8j6ugOhC1KJoD4pdoRCCwuRUGxTamg5L4ayhVeGmRq3_FKfv3jwou7ya0JrZFbFaEVpKGTTHn9_MLkBmhEqB62eqFp4KRyCOvoiajuu1hNEH-JkU76j2kOtso_YZCayGl0by4Z9bruS4BGuLZz60ZBpdbk8xGlSy-a_JCnE0YO5uVoSt7pIBhZN3b86fX6H1P-koxV1AXZdSfQuq61ibHuaovFMEFjH-fFPv_3j5TqX5UdJs9BKx2OQRGwW4mzVFVv6StNEbYFdqq9FnW0kr34FAw0WxCYyR7xHr__--jqj9XWGD2uxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mldDrRtgVlDMCuRXYp9jpWl0ChtnYqo_2YOs2rAp7U3MCz5CaDfCZSbA2ai_tl48tQHxdji4rHAYpk4hGz2P84IZy7zRDCULF0B29lKLh6BdlmUt_7Y3dLtJ8WhrNoRXhCJTp6AweX0gwRH6dWDyVKZy-NTpKRzvOlycuPf0Bg5PPKhege2UyHGDPeVR_i_DaOXFIYSVFKu1sYVUhD2waijm7aej1zkJiAmy1zJcchzQlteZqJCWop-5UyF0w9Y21PXOlVig-WDFfR5ZHrT_jecJRxVaLyFtu21qlui_a2X-l_f-4MKBrdb72SfMYjfntE2qB56tWbFKy_PNarIyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QbDJ8X8Mj6o6rr8Hl2eOegAPnqw0AOKQSuaEbXL91fVJzI89JEOTBKXcwzX0b3q8smGkuq7BuSN4U1zmHJb3E6TrQ5NT7kMsiF5cT9EeHBbgTRnlEVnh8gwRxyuZsFcXuwSSQ7wBSoJtPsGJ7XdBuMsmNovaYpUxkp-b9NI2KFToyyrizXe785ssDFsPNTR5YD8Xmlc17EYwNj0AIgfM3IZgVmyW_p9vP7gXWxbMh4EJkkdtcGon5_IFJHxLLntDhgd6bZJmgBIgZN6FAmpoNJYqhdX73ZZBkEU_rsKJexm8CS8l81B_rK55kCRAz6wxQn4J9FxnvayHXbYCIMOIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_7hvLFBe-FXoUyhYSxeT6u5-XFkm_oObjYhl1r9Uzb_uDCMdhtPV6N-cXHbmW8YjcT_Y-K-uXi6ohwj_wG1p0BlZYun-60iYIqmbZv0W1JD8zLJ3W7EcjltvOoKSCyn9yLBtzYB8uDUIgHBrP8o70L1t1K1VCqZhyeoScbrAp5fQhCPx6QFirZXOgvSSVXIhWeI_YAsGojJ77Dw4H-UFF5nhUgkyRPYPTrS0fuEZceJlI-_PisnIsl4CcxGkJJyrxw-B1QYbkBSDu8_KDc7iF4qsPdXReYT9ba4wO_VLO-2D-n96fZHpk4D3bhPO-tMFGWwJL02R_cB6vmfe91NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrEQNsQ5LJpZ8iWyJ5UheL_zJoRcn24VcYh9INn6Hrli2owuxlOAO4vKzKUZyIUgg3kEKm-DqD4GrHBpJtXreVP0trMu_jEUCOnGS1tI_Jn_1uR7fU0d21PKwl0zFBR7qo75bfK9hbcT4l-1IhNKl9xbsU22NWllVRkHjtgEiyuFBgllLbEmqjJaUbY2RiCbdpVMP7IGEHhLYptP6Bv3M-P_Y9tHoSXjkDEokkozRGy-jWQBfrksksl5dydT3z4IR24UA7dudwCIGVj6cwtJpEuSA9WSHqH8zDmNCBb6llCLLojFvUB5S_2vJxLmF7kWIxj8o3rNanAHnW2WlCvQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NPiABCyezq6V0nvrECfbZeMCiKzDCxJGHQhhHoSz_50f8ftPmfy-SvOKZkM9r2zDEM6fY14QoP0eyKBsXN3rRRhWdABaviXx1AkIMMRq4DA_NiMFSHEB5dj62mCSI2-IhEwOKklFDKZztYPrbZ4gkeqy5u-vYa3BpxU6ptbGOVkPmaeqbkm10VTsPhVHwBzU-_52NJ78oLnBpCJGHueYItpnihiOLnYZCvRnqYl7WYhQ3fONAbc9BxFPQyO2gBaVce_Jw--Wy_BA4Pp_xMbn_EYa03SIM3NMNOpcCcdjMgafAM3P4-RTE9R36hcDoQXLRVy0ccmCrsXspz-KFmJfzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgayjxmrgN4032oR_IOdbSWRnmZKQMFpsQflt5MAfVl7r60KMhMt69ogqcVrrcOTgMwm6imRFnY7janqVND4HVidbUMtgSBV5gelrLZMYGkKtfRDFfPrMk5SdmTzUG9sCjRLtIjUlAmVoVlPlSZSblk03cIPqZ2llLoyoDm52aPGvC8oj6XIZ-_rfLBcW2ItwQkixZ-WENQ9MFg_ADLJsa7HTdrCuQcobtCTq-UTiqbbR4Kb6feB6DWg9nkKmXxQomdUjRpccD8r_acVCI_ZlbrAlCtHA81htXNF07C1xkjFxtlFxj4TVLstfDeMJFlgA7gZ5eP5DvnyPfS96QcipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IujdTnyVhuiQRWcdyBFTmEYTAOaSdwleGIHYs-qzl1PD82qS1qHpGCPIZZsf6OvQXkJqX4QJzQsk4PQgTNDOg1DDy6N0FxTeDk1aV3HHDV0WUmSkjQJsZ6xfawNJ_OcL2tASovy_D0PKhxnbOxIso4K9SGZva27uaxBcE_mSOn57AFhHLG-Fn6vrvzMTB2xVg_XI6PGYK-ciwTHwHhDtdF0DCKgERrYUHBEHd-D4DmM2MTDiyXZz4w523fDoXG_H0k-YLDhrVezf6PQ5JrmK_Uh3PXPsLOnaRqMQGxAAb0ERq90fXncqaY5QrQR_a7EuE2E0LmeQl-phHq77mh_qFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUVHmJ-6Zf-TUrnmvVKrESo8yCIPFn3U_xq4geQ52nyU2vQGp_DjT5ogdataNRvvYSwrjOuMVO1hW2_HfXZIiWV94yjMAn9EStMXKWuXhonuuz7WHNvs2qV8O9hwhTOwbk5LOGZoTLeAjFV9Kg89JYKQuCxmSSwBavqrFx0ziSwo_gHUrPtvpXse_c9DdyRHMyqJq8U1TeWv8y9ORsxNR7um_jygAb9OiYfCy4LjL1XDaxZKNn5t5Fm09FDqQBvcJoYEZT0DJyNOR5WF45xTmG05GqYiwVhaR-JEPg0ikWD0mvPmkjOgHUTccJX86u2L_xACHjoVqtCkCDIQpAfbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDp_qbOEfaHswZHpPQa6wA6LybvUTGvzjUoIPo_2haXMSPZKfUNsN1pWzWoWTKesrctZbEiy_zUD1dJSOxctKaPcrYl5AvsW57HB74L3MdJt5Qxlb-yvcT7HNOlx6aQZteK3QDmbfAWYwhCQ9DfPnWXOc7ABfXyPQwrwOrfbT7jWHGaQsRxQGllgBIi2lHlRLaiwJbpDGQcniXc5D5FfkRcoF1FY3pveI4LffWwccVDgpGykTNqsjchBdhMVxveUMumhq-00_3UBuKbTtHMTrERkL5X11OqojQC1IDQfX8n-IE4RP3XSu5oDaaaZ4CLByfm4mCDUwQ3LJcdBkogPMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuHZRAt0ZlleJY3PKQ68Lx00fbo76qNQyUbG2qbqTWDKDu0mm9bEE2bW1h0zKcfC9crL2jihQO_ZgLqRfW5w8AtbInKcBTwogBD4M-9wQPvYDwKj3vYZF7IWBmvTUQwZ2xZjjfSvjKgPkKZ9wGOpVT8bJQFghvILLvOvLgDjM7ZQ1cw3XklBoVel1rl56VXsfStQL-A0vrTID2e0PrylgWgYZo2FKK1_aGqsfqNLzsTyrQPDBaaC9BRsEoCoY52Ku_wUwe68GXnHj0m2TALrjonwbKeeeKpshwyvFrukYED7T9VJIQGJ9J9hBGC58d5f40gcU5VqbfrxpLXOQi1J4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WN0m9yQAxwHSOV2gSMVGlC9S82NTNGOQN7fCbvwTdBC8eryYzqIgf-I1xPkTiPEwDQmOAaUY5iK8g-awaUOywlu5hdNRrqglKn56D3dPQkhF8iPRiqnP35lo8YQKHKU7no5_AMY0S-q9vDshEJwuF6sXmM4GxaCVwxekbQ23YY_GM1-5G8D5blw7bISQXPO41d2tpIJ9z1bnECTZbglSbiOOXprl7U5Ix8LIbQOZUhMHtd7P5yTbbuWiPOxo6dtZYpigLiwIGREyPuRWo0tmwMa11tYjilMoEmipug78UTBtV4_ra1lv6dcQ1EX9CW_ODDQ7Tm5BcrBrxUKeCi_2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k4PCnVcqmtTxdyJt4gQ5biVqq5nZGMhhKPbdxSSTqFA2623_IX86kdqWxhX122wBCA0Czrc3xnVtnztEKiD4MPBq9e1ItbhvZQEvn70-vR6_uze4cboXjKm4lN-Y765Kqa7sK42S2IG_hgs0ZMI9SguNdZn-_svFaNzJC_YMleByCORFgr0wI00IGUjLVV7mL_QuRD5XbzIKkyDOVc0778KQOToz61NiHzw7WJdXkzg8CtCrYg-ZasEMOu90UXTLWyCPpvefjfKSJTZI1qMuDQNrgkM0Out6kejbPpT2mLcjOa3LXZZ3iMJ3Hlf_GIDhXsDH9DtOPwkXa0aAzkOC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bq8_uHbTjYJ1N-LahptE4AWmT1Kbca8O9UYgZDlv3K1A6YcVqRp7bf8Hs8Z_dvU0pEof_KUZhqP55o4FixCdFUkEbelLuYQ209MRefWV35fPHwoTt2--Fd8WOqfnTokpcIU-IbzBdyqQYZ7_1CIxo7K-aavJgIuyRWwDN9T_AcYzrfcYchox0u-B_ENqY4rGGGIHUUry8v81HPR7jIslDjTqIoaq9Q43ypHGeFMk_v3-0bAHH-EyNunBnv92C15LQPW4-XDKnlQyfYWwkS_nnJqS7Rv7iXjIVsLVJJuJx56tSsBydDsY9h-GFESfWdjQilsWps7VlGnTEWhSuMOBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fYsZSC5nwbEi5k63_fj-jaeAc4kGG0MFO0dZx_UNMZy-0nglOmLddH_n0DepnOB2uNcgmb-xSUXLvgKbqZHoyXp6WTUy_FdCiEr2GWAw-StNneDU2m8pY87zv4VcjFe6YM9-b_V-hygDooeOiJwGWO4kxqY99A9VmlHqTGkvsCs4TtZlSVVQTv3d32v9uEsQZCumevZrz7tXYscIK2wusUYXWo9npTAJ2NO6lZGpaYpy4uVQ-dvBWuWNIlrEVTlB-XgZBJFrUEjDZIAmnAkqnywbgVMOoNc4c-RH9ekloeLKd7J6qK0mmU7sEgde7yZFoqaDDZDp1F0oRl1j-vSNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PoV_HGo3Hz7MypPCQfbhyHe3OUGmzHf464v27LlpJhFzgTLh-eeH0LETW8iTENHaT7ACZuK3gZVWAj_d_Z_4jizwwenX8T_DaZajS-gOXN1LB2R_8HUMkVTmnoQrrZ4E35KTkIewlTR3z1NzOCLzIMuJUKIGzv_GdORct4sJMFYi0LEvqAd8mWHuoQSkoFyII-lrxhocmqV47DjfNaOllS0Dtzg0oCh7skNhjKFFgMv_r-ghjlHkQif3WQUMNYy_f8u78ck0xST4BrAhFCd7GT56C7nlSiF7dvffFYy2Wg8YwBA-Ku9fQDgjADItkhrge9kLeIEIvNk1NVU_2SyIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6Ehv3tR2V8ujM2J-YP6wCgnLFxySL9rU7tmWaWJKPwD0sLYsXNzICf6sJqDfRpPTPgDvjFi0HAaIqk9zAltgu44x0_x8K5sJq5JaSKwtEvxEJZG25tt9rxSHyx-jb28918cHpl_e7-_2DcyTHTbQvaWKCA5BFwiJisCqWI80hLuNkOJ5GO9_TcFFmuX2xFv55GOsu4SA-MsvdUV5mit7O-6P4ZMx66_YhbIZtyKo_Lff8L2aA-T73CgabWsCch5zV8c-MpBUlczzcOcu-l9b5ae-sz4ERrzj6_8KnRzLe2_zjKJ_jamxTeLWzbV37apcVi0r8vP8Ql__fDnseEoHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CaagD00w9yLs_mtZpn4pQ5Dwh-9U7HOgS-iAh17PR-4ae1pIoljykLjMIKdVrNTnRT4ZcoY_p4P8XPy1tBtAIZOMhwpMPDekntx-h_BMsKuBFEtuYtS_xFuO598eLGs4c5DuhpLIrebGCkRvtFtGHKHc7Erg2XIVgOabuEHb5heLzdv9hDGYBBEoONcHeL2Fu9_DCrgMVjkf2Sr1MzP2f51i4VpjSZ-MYYUjnQ59Y9C-dqBwUhRkHP1XnKnJG-j3sphlAq1QuIZlPGa-Np0Qja0-BtPNldatQf_EmuMGstl_5Ej1G6ejnzrJntV2F2Lupvsd7ykmm-ABXW-UmUkD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tXIHaGiHZv5iaLRENpZqG89V1BqI3qZgJXk8-Mk0WJ2_cCe9Sj5BR1FA6CMz6p30wE7sduMqBj6nzweg9RaXpUyPA097d-9BoC9V1UEbGxNvPWWgOZgb39SchBxZJShf7qv40-jX85AW9ViyeZtWT55n5lHU6rut582_VsnOJeYnLjzIlZ19j8QIxtZEPweeWeRUpBkxmrz4lLLiHYdB993ETkHtEkNbndpKUwrIH228RMBK3o5sYeWvEzZhJ0jIIwl-7NVK5YJs8rJuMEMxG38Zq8Wy-tUy9Hm1vKDpm55NmB-rlHWf631Y93ibsIXHRdAi4slk17_YDMQikkBdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJhqBW6f0BCq1Xpyj2e5FgB2hhk9u2x01uGW5-iNGQvrrJEl80-NHMgjXdeELbbxmceRQtoyCm2qwHmWQthYyiMTJOjG_sZwycgyBTxzuNYxgoF23h7Iqca92sxrwah5kRvjUdSGOBXgMpuTMi13Ecs6oGqoP6lA4Uu3qNKxeya5Ta70TVjFVYx1UB9i4p21pIR9sT76D8t8wW3gOP9xZQlIPwSngL4JXa9kxUf7_qBZjCrCfZ1-mSGZYuADDc_1GpM3Dio95gZWPJkfECUosdq7MYqY8sCri2h1GXEMOQJ0GallTUrgqSmjsdtYRpHhdcPnEEA0Oa-07MuTJVegTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skVce3ZfQwxmWbHmxNx7_2vj2rVmUK-Toh7XM9-17YSc4cl5DfdvXKucHuzjiXKMbx_HtBS693K1fUvdcuD0c8NwxMdCiBchkc_v5K-tUYNQQDODjHcskInlxj6Wdq6qKji0nvUm9LCw-NOBDVcHovZenRou86-vz5Jno9-Z4JSKF68S6S2N_H-j3b85kj4-lyCakGiwsgZYqwraIR0EzmCrlC1ilQ1CwwxR0BliBsrCxCkhJE3VDlWUSYvQnVavCUpF8w68__k0R6RsCXnvPRcDMfgU3VLZH1DEPZBjLrQSXI9qye775R5rtFxbvagZsLQj8_JAxHqOVcacd2Op5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iz9XoygfWp0jPIamEpZNC4lMCmX9W0VnL8cmS3zOy3TsUpXofxYPhJTCyWUaF0ho-mnnOaUSSZljsVRs4JHQtLAEeQ-idRNHH0uMNdGWWJIVR31kKClJWdVtV-ZmGYIVHoAiD5YjypKwm-_MMmPAXf_dyCrXBunuC_HM_EdZFNXhX-iNs2eECPeEPyg_kZH10iVgLpAgyxGaq2XhXOz1ErnaTiFUHfjqly_W-aIH3DlqBZSAysMkaCBx8W4G2AuL_J-ZzAXLBw2nsTd8Rydu7HaMJnclrHoPPG8KnPIHNpnxo7jlYsJ4a8GpZd2bN8RYi-cgYf3mnSCdP3nJRtcvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJ4T54GpywyUAijvm1jUuXDXByzgCsL0jC2tx1W390ejZAqpnJk0q7pjkZHviWPsvYzqWnBnxpSzZRyLz7FmCUgiCWOcQ51WmqPSnisIOmeAUCW0_Vz2LQ-0qfiFlKOeULlmJjqrK0jzhEJF9dwZ2kzmozxCVcfkgGmgb4oMq9Xl11GJYhGUddd1rlWuoLjzKqS5fCmcWYmjMlspOGj8yHMbALshDsUlZJcuWWJ6KDJ3yhQoelBzpXtKhFUXNgbGx_GozCVKWsrBVP46fmjSEc2xY1FaTcQ3l8wZUwyxfvdRUoshm9PE-ZZ9BkrMv5i8fCAli8ReFs14fz2tE3kMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RzXKcjkwBUMWPvd5Stb3rn22Dph2ihUiLZHe7c3iGAdS21ci8SnBMYpuo-5biYE02w8g9NjBvh8XmB_qHLxGuqBsHKYr9q7ZUi7Li9T8FwYvTHF0bwZCbGeNfIxkgmP7YWpDJtJWWjiZCBu6xs7vdWo6e7zQyZSRkS7y4UgOzEu8BFAs93231UdkD8c_Vz9oT5WP5LMSdHLkOu3MdsW88WjBKd1l8-CYlViPxOq6mEtX4gwG67PGYbIaGz87J5mWYZ-0H5h_T3hPq8ytdc4Pb985WoFCYW_gU8-hpENGZSz9SnHKWQCFY6zeP2Ivk8n_NNbKFV0KXyZnFfaT1iDGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7-z22z4YatB1nrZa0sfEqCTsBvp9pDRY75HdhyZhGRhSnc0wL-qu-HmvsAEqmsIv2epwVe67kyhu1wR5AZjM0tXIgILAruxCNz296meNX2cC-IuPDYWaiCd4kvakP70618C7bH541n2CsMYSNkXFPyUtfREmCsdjq6q8qzzxBbK-kfslNmiXoJkt-M4QC2gGSJuAo7wwKLqT1RAwDu4nf1RcMGpSjJ-7oCh2HYJt2eXzqV2_zVDbk0Fs8r83ngFet7S1DT5o3m99DaBQb22t1tdh8o4B_splV3AbUjJi5-SgZMdvAueF4ORXzhxdqspOKDuROt-ZrLY0zkRhmjlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iA9a28I8crqRyPl-LXuQNCaHf68bodYIGh9qqBqQad3pD-OgUllZCP1I3WRLYLzAbSvfoGPzKYGZiujhl5taf7ZQtZebga5uBiFtFEQPz2Z5EvfOPjoeXRhpf9CNllj4fUUKNvviKn6jNP1xhTZ65D9W8rYPB79u5EKjyiHW5Vt-PPrXj8qaqevKqZqb0debtvZIL46_XYXSt_42FQu9YSQrOmN3PAiVvKt9xv0noDKEtvgYR2Cr8UhpXxavIR4w-HLbSsROxKnxfZ8A0BFPBVpSM-ZCzarInT1bLjOByPllBQFu8BHBsLXGnsm_AymsHOXW0KYS2xty6edxsCtB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ms0gzfOuHQwy-Ey0DlDXjYyIh4KrCc5isXBvdFTUWTn1rdTmB8sG4ejT0oiHTqHNvf8z13ypS5viI9Kl7H3XoJHxvYwN2qFK6nMefTeq7PCdlblPoM_cK6A34xG8ZcR42JTC8pFdFbW0q5DyhsVbEOl796q8QYh_TTseuGwzDEGFDuW-KuRyIR7IhC49Eoe8nwPuf1delxYYXdnj6TkTjdAbT93Todhe4h1nGek_elzKjWqwT5mxbtpVmwHOVyfdKPo4hNIvKhoERA9eEZgin6_0WizjxyptRHi6D0G3mPRtzZbkXQbq8_UXXlEfGJj2P0nOPn_nq0GmlBZw2bLcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R0gnmc_O_8dEoF0Fkrc7WwyJnsrFkghL5UMtwyiNI5UQ8prE-P_E5hlL-OPDqqSech7gxuYGpmLbA6kNOCpT5_iSOir-qvFMr_SngDWaHaSKhrlcyAZNji6Yr-DO-Zpy286_dE8eflvEETYkxJwE6FV_U28o5MebJGfGAm7Ba_A4fVfqoKnz4W01EMl-moOlH_LcWMO_68ni3oYpH4tqj9a5QBRNNcHgpvfIyViFbWFjRtMubLiVNDEG8kVBect5OEpyPEYZkiJH7C37O45roeIucbfBOG0xcYl45N70nM5g0Jdk_LtOzngxdtQ7i7s3gpohuFgUS6p_PBEa-38kTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HeXranec7Oc8VNcIGpiJ4VkLhjyf6-I9RwR24QCajbA9zMzyzeN7cQeKUX9twU1qFQNlSKt68dTDhllqop0KsJhdnrgbpuMUuJEt4iI4VR05aR2jGqnU0lZNgBUAaZBRnft3oumhwAJfbpvZJ0Bd5Cf_6CAzS_8CjgWRoGHv5ib6W-hDeTGO8sVsBFx98IU7ORZbBZteRktqUD9fXhpgQlT3Fv0pPb4MBF1bgTVX3M_91NeyPagWcldklE-EG8OwHIYzq0UrLehUoJ3klRZiEqFI7JcGMX3sXfKmFie2a0-RSKB0glgFN3Eh12cBsv9l2dDo9C8i8UM02_aRG4UxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=r0GclCDzVlXEALxmKUI6c1l5-R5ZtbPbjTSFFxgXrWh3y2X2oR48OyazeMZlj0xOh-VA3NNPoqRue2Cf6J28nYgr6EUQHI7HOxvoBldBJaf7liLScTrXhcPGoKe39fM7-R_0xyEk7rPWJ4qVJWps4J-mUxv3SJG2KqUew4ZQ9WeHo5cvarlJvgYfEhWWdaDkYeXuX0GtCc5eIOrymt_a-S2bulY7iAqezvh7Q1vSJgl3nfI7b4wqvEzeCBAfmC3yCwWyRxzFtqwfzvzE7FsIx6yMZ-7YTvoPqzdyzjEra1ydDkpoNTcIsux-4ucrhrXRYaNdbF9EuHaHEJSj7KtwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=r0GclCDzVlXEALxmKUI6c1l5-R5ZtbPbjTSFFxgXrWh3y2X2oR48OyazeMZlj0xOh-VA3NNPoqRue2Cf6J28nYgr6EUQHI7HOxvoBldBJaf7liLScTrXhcPGoKe39fM7-R_0xyEk7rPWJ4qVJWps4J-mUxv3SJG2KqUew4ZQ9WeHo5cvarlJvgYfEhWWdaDkYeXuX0GtCc5eIOrymt_a-S2bulY7iAqezvh7Q1vSJgl3nfI7b4wqvEzeCBAfmC3yCwWyRxzFtqwfzvzE7FsIx6yMZ-7YTvoPqzdyzjEra1ydDkpoNTcIsux-4ucrhrXRYaNdbF9EuHaHEJSj7KtwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THcmuDVsEkzRjcSQrb-L9XzMdIT28ROqJendYqu8k2LRlZYkW-RezhJbFEgeg5ZKZSaaYkOG0KryAWH14Wo3LrzL4I3h_ca-Cxk4W6SiDhVoAwkDCwfnhkDjK9JsZtVQ1SyV8HHFBFd0NL68yuxaVsEfjyR0BzkPZFlCF6RaL5tx7H2ifuNqkmGRJ9L_9Mtypw87YE3H8B8jOK87di8oQlJngaowopySqhUiFwYGRPPO4arZzKALgesPVMxtWQCYjR2AGpalB47NNQXNwuGOuC9CcOciUVD3bQKNgUGhAXnNr-THNbgsGkNmNx4OHfmrzDYKy2uHptoY51yXIJ8Jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GvhKcWFI6o08qCVVQuTRpOIRXV8fRctUjeUWbgnMExl-QfPpQZPaUeeQbhRZLnudbsVB-joHUpErxakT9c1hjGkctDtBEKpvZMzdexg0IyIjSU-JkR9BItJip7vvT8zBXF46pdOR0-k7frJ5y_rbOvsev7vmnd-oo9pqvP5BZcWHJQPitcihCp_FVQSgyx3wjz3x3pfmNkanRXhZ6R5VrSJH78Mf8sFLpXePAT93bfZX5QdtA8RXi7rF-oJM1k0LpTb5p6izsxf0sS5NuMLXGfVGwh5KKlTC2cX0uUwfhiJFjppzi7i-bF904Dke3A_4oSsQ9eeODgvTQpord5RicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a1cncmgi1Nlh79v4zqGDfz-E8CUYvoXsOScTvOeIpGv14isuWL1xf-0uUkgUjCCOWb-S6PFhpg6hwPtsZbS8_zdHjm_lC_kyn2v4W9q_oMGYjyTo1MbrxPu-q7NCsJdtGfz1u7Y4g3yw1eAD_n7JRCw6f7Pys4UzXf335lPwwDM1qspcNjOrrE883RW9I2By-SuLI2eaf_Wts5-ZIuSbmEOQvG_eBaV_TcF6yFTib5iB57uSrd9kPvgE3pZMr1R8vJ5-7YdG7q5Ibr_mTqCqQPJqma6SrjhiOR4rzgGi0arS_iEi5GfZs1_ykzVreWvvRi85mm7JVTv43z-fBJncJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DeBnlN1go1sYwAFq8UX8BPMARTFHtzbtU6nAWOCD7ir7VWF6bFweLtlw-5H4FeSbedqWcOtg4aWXd7aS31uEJ6b0URecqn8R6uVBjCv6ZxU1RE6lHxebOniFMvSG2BXna3gFXa12Hi5bXwCqzQrjIrRBGCdL66Xm-v_Tj0ssUyZyzFPfL-E5d90-tiotCNGb_wFYrRB7rkMh9Ien-XzFN36nsHQzGylOWa-p6mgKpZAEkelua1i0atbCGYTlj1yT5xjV1xzkf1X6E7zAfsRoOnZ2pzEpxfHy51e_5Y4na3NqtJQAeey0gUBtnH-K5sMm_jtwuRxV-kew1eaaO79kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XH70GSKSAgiH_6x5XGN9T3-Ew_NYecIJby1TpIut5v6Q7Nq1t-o-_o-rbpUiv4nxsfKyprODEgvZyPlYKMmJXPsRm8CoAo4VAgLIBYN9BfhO6yM57noKPG3zAvyHmU8_b75OvzwraGoWCf_6tUjAmNpWlYZ31vvvd-cAWYpnzsARKWOSrxvab93lwhExJoeafi1-VcKCQ021ffR4UC6uIguoCD72QYF0am6rpFY5Nd4Wxcz3MTYP2-8Q0oJB3ieCShL06ZEdJJXU7shFktDzvai7Bk6My8Eq2C1unYG4VuGPipKUN8vlsCQEGibLTQsy6lUI2CR3wR93AjWuQTrSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8pWvQ94UJDckEH5fV3NE81li9ga2AMbgiEXiI7Wt3H6rhOekVc7zoEsREruCOXmpnK-sf01j1nBSJTqW9xTyyHmcaimQK2sbZLwh8u7MuiU3vI5MIAh26RS8d3v3HaKUHv9w1rEBV9O1FzndPndchzDnq1ghc2l4nNhtW8AlyFo_6sJ1dx47yWsJQ_uwfqSzvAoiZvY6qXfjNkwAfzGyoyxA_RAXnXNPUfyNIghbKggvAYtnhVMlifCnfabOYzLrjmrQG4XKQ2zhu61xStGWlkAY-vJ8qEvi0mMtpRsPeeKP7GhDCqnMyWqDKVt9IQvRzJ3ACdVWKnQ5WI2dyWfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pBxnxyEA-2MhmQtfMGXCoKMITZGEQMkWFPlu4kuNDlMZSkHCafRwW0X711uNNx6K8ldCn9BOqNkVzrrwev2x5MllBlYcwnrldOl3-CdhR4HM6Hai6FqELOunvWRed8vUZoyA6xrC01OYHr8X0RVgzg5qkzqMXj6YPCpSNKEW-lQScKhZOpwTKKGMqZxTg2uYqgTyE_hxCVOPQy90o6ty9nncTC3Yb6qjvk8x4gu9UXZptTdZYWwL4YExG1xzxApv2er8s_Uf-VkYfjzXylBRZqH-znTEvwO4WMndAi6aPzb3NUpn6Ydd8RnU4WMUNyGqn4oEhiSjVJqBgJs6Wh1b8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiKo8ExKbSJcjrdbe5cKye2l4cnqrDG6mhkVVOItRSY_4GKnM2BhCSMFaH4hOIXfFmnb2v07ZUJ0XOI9eOSAUigcPZp6r-0NFQGtqb2E_7JfTZd4WSfXucAixns9ib2brRf878bLITzYQWDe3KesPm_PSIWUrX3jH1nv0Wyrsiur2v9E2DDMxWMiUyFL7s2ACIghMn9QDGel8CUPUodqKTJWA08u2KTJYB2xLf-zS0nhEaWJWZsuqB85iW1rTFPvA9b8rkofO6kJUKSTwVcd2PEEri_Jinzk9wnv9R8YUvD6qV9GnTpFBo9gsesUvYIUZI6ROdu9b-IuHZGrY_j0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnJDyNCDpca9EBWY16ct4raSCsPvKohTTObY0dLFntdTClsSvhttEQlLZVit8HgIbLQgh5KgyK2MrrAuYFKIkzY7rgRGIQctbjEm6pNnpBkFnCkKkICqynRWotXXU-e3bcGPchZYrEDriKtXFB1w0935OMNHiWoqyoMNGK2VrfffbxSPCmAUhbSGDdF0wkorf9NfU8QjvRqAYlh0KjgKegkCEhNnaieLy8yajlXzDWRgmC6T7HqbdKsECwGOVh1OsvvYwoYkI91N_fCrL_vQ7K-3OXbrdYEqfqkFw_dhb9FqHs72x9C-X0QxnagUrBfPU4yCQb53FjmZdKvFFu4thw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZ6aS_mU1edhQ5qG4zD2Y0rzqY-D7NnO8xPQkfPZvhyWOqcKHnA_ytwTzHgewRruMVoAEJPW-b-lhad3wSbaT8a-Bz0M1ArkLuZResDjlL30rLI37jC3MqnnWm3aLu5OOY1P89ZMAWvA0L9zdQ-zNp8aXM7VXhbUVFf3Wj-rOx7H5P48x6FgMNvoDgQseEvRkTDZhHty8zWZE6C-N16-Pi5GsuuUQyTFeip-s9Y2rwvz2VLRASsvutHWKj_DuqV8NmCDiNlsBBS7-VFFnZ_whSGT_5VUGYYF-JkmC-8Mkk1qif7ATGnweKF6FUXJvj-FH1eT_KYyhAboIBL0MQsJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fzz8GWMU4oZdGsvDKGYBrX6oKem9V7-AG6uZAtwADmzJHnXC_shj_FRu4K9ElokREHTYXbBu8PKLA8Vu86UpHWtW9UZ04akLwoXuF-vodoDXiYMfmHqs00Qi5n_RA8FXRvDnpDJqp4gqQEh-VjdIvv-XpgjqOKfXQap3MvssYPlBu21SWUw0nynhdwV4kqLkXaUwJ-Dmp8YxCedtfLpkNAXcNe7JKk-FRhSA8iJqw8nYhRACsmP0SYSgwdUas4B9IhQWpnXrEg8ZU5lEg_sp8EcU8sPDbJWKvJvYpa9a2nYWoBB_rgm6nnm8kv9Vs8e7Aty33Lw_Pt2wYAKAwKSXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vvGlvNZBk-hl6T8ZKJsrBTug91xOAGIjLIHZZsT_anFUPhwVHuGEHt5nEA_YcmGmpscP-XUhBbEnMU48-wwn_9IInSNUSr3dLGEXJmIfH_m2pcT6f7s-BSmwXl6UHjWG3YFEfuDFCMmmOdv4CY_kacjqn2Bpzf7RGfn1exXYcYyeeXu5kbplBnCfbgkdNKqcsu1JA1hUTWQdf0yyv1KYt6uEnocQ965Enth-8_q96AKJ9_26TqbqeBD1Gymf_tueRgEHFWbyC1qlOAZy3wKYUxICzPNxxLE7kQNt0udp7B7E1Bzgmd1rv08y7QjrVY1JO8zWWyx-rH8A2NFlql79MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GB4wce6GCjPHG-VKiyneAsxarjBsCIOImNppPPM3homm3zbbiDfQjRnoncoHbzx1eLRfLh2ew0EvMbKlHYJgQNg3RyKjmAzzVRc0Dv2ippyZ_ME3k9Wo2h6E-4mXEx73Q3Un3m0MpapP9_uNQ7bDiaPIbqrhUUmKhsW39szrijpFDwvVQN1BiK62WIeokz8aib7vjUPbiP-fRJlFTHrV016LYMf0XJ9iL4Yhqrhf5OYJnTNbepiiMdlr4qc_YLzQfoCPK2-jeVzIqh15uozr2RrNu7MWskScCgcyYOyDolG2Z6yqITWgIsfoetp244zly4C8ZaHKH9t7BJaAEMSuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ndqmylAKZGK9NYeBTlUTpZrBg7XtPsESZuErfV3UQYFezlfNNwufYLAwoovoH9jRXq3AEukVhEf_CSkSh35xoQ5wuuqn2Yte5h3zI2vwEpan_U8J2FWY7f85967znBqiZL-zheugr3BIJz6PvEA3uZ2wZTz8IavRHI99bTu2M0_93tRhccDXhUDKets2H5J4V_N7bY_KNocY0q2bk-u-c7LLnKktfQi-Bp4Ec5UxL9Akjgsat23eFTcIIaK09EAUeCyny_G6vKrfeEQVzhDZrquboLAbUkvBEh6jPS1UQlePFEBu4tAA1LvhqMjjoBcCJ8xeyo1zKqP75NM3_TWVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TI6tqSpnS6ASA-vTTTpLmPhu8Axd3USCeUCZ1lKrfsWP0Fvcx3m-QtN0J7-vL8FU0n2i870pVXZx-aTzWsVaqkdR64VDMYfyZ3Y7jtzVHrCRiDfUAtJchezLa1mCPTEWWWHHC06ZCCs8SV2Zd9-3P0JLqXnVWRl9K02h24oesp0BSlqOQ0ZWRf0HRA_BgUhqwrozxRsT7r88GznaT9zR0iFr5ulKR_e2-eJD4sDgiV0xHFvf0rrR2uwOXYndQSBEeepQ-qpwlVT_XymoeynHp4vRqh7KFhwnvoorgRnDTptoYpLoRjNKg6pB9GuQqUWAMmCRM9sqoPGGuCbMezB7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bX5mpiltXnnnR_rlSzHno6hthHHP8r2LUZxy_8xhRvFJu3w1ZHa91IHXsjuANjFPgN7xjPYys3ByOcwG2lYJQeocWabP_Glf_IQSNqKJLx7ii29KTS1o3Dfnw2P5g3wRqsTx3L8irFe7DnhQ7IqF30QmthsukkJlys-Ub-iZ5ciew3P_Bm-Oxh9CuzX5wyOEcPdUhhcOnKDE3Jmr0UlDZODiFu_-92NqKiAJ0in5JQeoq-LxvkO5WE1nsP5-yAe2Ax2IDIUHX3Ifk0zrqa9FBGNW1Pwde4_ZgeX7gzGL3ufeySvbItVKdFvxXi4nDY38S8vWqj2XhmrlgpQvz8_-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-o85j4PaWxE48xXzRTkQYPPOJkUbihY2tbJM6J24Uw9AXSG3naMVc-OqThksVYEd99PUiXWYDDwXsfGYn73ZK2P3stLRSDKc3HNYyIHmnQiwlCXj4NZc7QtRlOsgNcg_SRLVHtJPcaUF4Q4ABFCOLaYnTHSjM1mJUnaeo1OhaP1jfxwCTFduzB22IW64RgdttRWXpwnE7vN_agusOnXXXL3NdrO7w0b1cZQ4R7ec4RBUxFJxlNtNvCTVuhh0MCJp2cq_Ay_k_wBMTn0HMNBxd--PAPujbjAfdsTOWPaveQq8b1xymwxANKL2h5keKdnY0snOn_dpL4oeT7xia-rBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QoaXbbERmUzgx-Q9LgdED1g4mUcSaSPRUCrjFe-JcD860URXP4D8h-I9K28BOy5mfy7SN2UObdwKVShsQInTxEjrvsncRxjUtlYr3C6p7PfbQnEOaOt-EH4UGOx7KcJo302LbquVZ5KmvReiFt3btBFXvuv-qWGdV3buPHFejb5XPWSLshr5Oyn7qPSJoqi3uM-FWTXpFKtEcJmTXsWLuaA82oR3bI0RSVL0kqpvkXSmnhPuddDFFMIIWnNDW0wfnzaZSaexT8EutYjipmL7Yi0H4O4AQOvvAjK9pN0tcunOmdSUCmOpxUdcua976PsQcIyWWP3koLCmYAgANmPHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhmYQ4fpeAnpzw4Ue5kN3xu0K_0FghOk7taBaR7FyUa-tPe29QW60xf-iuYlPQdDae3Fzfduel1r9KGJsRdZ0NP9zmxTo1pFIxKZNWENaY_d21BLo14JppOr1vmagROITKLmqIjBIe8086JFBhPWCbG9fWoGErhiKyEYVrPwDbb_eMh-NOvM9Qb13amJ41U5f-3QSQTAgMeJGdJ6BkRHU1vKmDO42B963zULuHQrppUO7g5x_HXwWHzBYUeP0M1Cydm_mfqmjcVK6O3_ky62jOLx2gA3P33l72byaqs9I1p_3imf4VsBCF4gKfo_HgtMSaTDmxbQw33eLb0ggXtHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NxZT1VxNyiLqAg1tICHZtbAkdWIwuxoM6OGLWNvnG9HihBOzoU8cqu2G6954FJxkNiPRDRjJthBM_mCTaiBm1NySpgo4QCyJ0Kjwnbj2UOlycY_8mjlSymAbOsG-u8EummpLloPTGyCkArOOVfuMnRAlEGkEbV-L_PhpA4WC2syaEzJs3kVOGMXAFhrth6vfUNCjRbZpyqwweKxeAlw5NPPMqVU5H29OrwQk-ymtANtT2hlhZaKZUmiiG4_xYvLjCbBHmLqZia0Gyp-DA97t1TNGTl8V0OAyNrUajrtTGetJhZJGb2uKXQz-93qTUp-bohkhXUhpcl1WdRBHeUcV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uoi3lJRs8C4osH-qbFdrWZOJnJQ7hvBq0zGXUZ6qlb0lge860ujCCzglDFZJKGNRah3GBvbUOvQ65PQ53pCho61CiX6LZW7okcNE4CI_yk91ocmhGc2kNXk9bRTODBbxdIxldduJsqZ5QQI3La-Lm_Y52_EkfzB2PvtDTzuFshLR3Xqtaz4xJFSVJUxIjOI7Zw4Ff8n9StplyKoT_Ithfe_I7UAJjf7_U__GHFzP3R0xhn0rNKmMP_lm0veS03SuF7u-T7cuwpWFaHIFHwcClppOE2deLaYSe9xfSU281bbP9HSAZTZAN-EkazDyVnADkYRrcgahoUBq8pPQYLl0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tuKBILpcEyUQ0h1TKFtk9sc5Xde28RsPOXa8v1M82UzVoAqikb4FmadXnuG8RDj_xrl4JhzqyJ4ZfTJxwZOEfjGHua1gJd9q475K7vzM89imA5G_U1QT9Lmzd5Typfkm9_SY01avyTuXv92NcjkFy0AqWgAkFqyPN8VUR8HbjdOiv_oI55IcObiw1K6XhZI42wGafMXGFaEK770T9xyispE8U9BoNonCJ2uEaXW60mwBtTbnc7I690e2Hk0rK1zGFy3OC-KoXeg9wnPtOUJ2Arh7j5gNQhYM1idnCQ5eTseiUyUQ8jijl5-xDnqC80__u86o5UkrmhqA-Yi6geinkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/THynLvmA1GoOlFCbwMq-2GIZZKVdnSpjNRVp0NW2LYWSCVJuafhlFhrkcaHMfG3IGd2dPWq8xrTDwx-C9pZC_gmZnzsQN-X393_TMhvzQbObblYr8zLfGARSEhSkPneFjNYfrzLeLAflgSMjXOf4rvv7VlQWJN7wV--Mtj0hSxL8vLrsHCBPBK43XiY7i3XwPagGFjvt2JMIhqW1gVHt3kYHOVJb3Q1XoaA5LT7eQFfwI6XJkXZWE44g8afO1UPtUh8kXpw-X_izeLmSTda8XB887kxHHoeAkw53IMsQ-TXhui1fJoKjImSXzhfIBfpN0wAhKiS4lqk-F8VQv4XO5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vpfdjB-Fy7EXnDycn0-SATb_xBDE4pWjtA1DVMLk-s85OxxvU-T8dDMEEyP0J8iOOxRsJ3fEkIPSuEBg15SyRDgcPBI8NNLURfpOYC_AdDe1DQERMqlmXfIoBjhn9rxP_xbG-RO-H0W4ojREBfOrPo3e0AspSgAJ-dVSB447NobKcu1lOkAi-_dP1RxD9TtQV2hOLTweXLhTqZf0PfLs1viyQH0oAR1KT_DkI6GrpuX4FkCjr-EJY9vBzOKjkJ3gronX-eynLBvc1nV3CINDO0xEsBkSBlq56mJqqVoWqVcOKiLPu669TRM7H68E3wzqvePej2zr1XUpjAxQm0dJPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pPsQeiUFESrH80-DG7Hxj6nTBzYUEXBhOcnfEvI6MMNQv9pcsKkGx14-0qkU3FAwjKgVVK8gagydYf-Uym00ia1hJaQE_wTxDWQezQwBfAVTLGyUAVl6j0xyusEbDyqqlbyxIsBzb54Kh047ixDaFf6kT9woYfhn3aWBrqqXWrs50jxyCDgKdB0o47PfrMoDEm0Z3navwchCrrqOp7xY0o7TWeM6zqaby5a8iqrj3p4SzIFTHzGnCQNsaUvRr9bMD-WPN59nd6aQhUEW-acEhXLYQCCENdHE1yFa0CKZnhrSBk8Ulfr9I_pgR58leOX0LMEqQNa2SNoAuJzLrCoy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnOUilEjrbZKXoO4jES9m81k9u7u5yAZMPEyhCeWP_uQMk_fOkPdOoUdHEdNMgoxJcV2vI6YVPD90tK3B1CMP6kTurnyJtoZjgx1ksw6u_Wa1tceILDCQv7mZmwtbqF1udJJ_V7tDruxlr6HOg8dgADBelZ1ggr-1biD951vG4bbk5RG9eG4S6yGBw1MPxMWo8IcyTaJWJIIG8Whg_6pQkMzFN6LkXWsZDPu3A9ZHah6YmSmHxJ1fCVGPCkWLTG-mqeuXTNvzcrZwoGWEv97ca4Qkc5SXeL6fWbZCMpOeYy3i13wRXTfvVdhEuE_FR1ova_XeygIX_JaAzkEckc7XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWnhlCMPMZxdnnZTiixzMB0E1VKuB-xLc2ZqdNwvJ28H1ooywWiB-oPaVt_YyCi7u-DpmCsvg_7klaqCjP7M_rmaUsvjFpRjAqAU7NeBhlUD6rXbAbg19HEVj9GEZmObWsxzs8wTPl8yWTru_PgKksiW-fBqVZCrlc3g2HI5QtylsDyhppm6AEH0HLfHg6N8FMXVqfMiDlhuId2OPBvZ60LU1dLBvOZi7euCZCPlBMQmpfTxGI90QXM3QedhMEzDjxuV25-p_XwJKnYHBxfoH7LopDYuA7TwqchWQT965LWf7yO1MvVu4g5FojSm-S29CnbEAd9y01Z6dHb4md7fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sXCnD-Rz6SPBz6l__g1Awwb8r03pzi9LVhlEI7FxWrQd7jFQedoEDMwp4Hcf80STPjQsy3zCUTwLRIP6t1f_orzyx77KCQ2PsGxncnlhNl5C1ARG9XhNHnl7ebJXIBnQoXRoaIU8wDjqEHbArcd3VMYMnPeUMC6EhXHdpjbdKXeBEvPVdeZggSLXfNUO7qUlzsBsQW2wsSNCctU3rX8o1z_Uj_nt7t82cKOz_oQavA1TjjczT4u6lggn-s0P_1wQsO47MBDMBFsjFKn15yymXCYcClEquyKVET-Hm3RGmUJ-eAl88w6-PznL5buKAKQqbYFx4_4ySMdVK5WUu0VFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCk54L0NEv16Mm1LgU6Su-7OFX2zwNWgtU_48ak9sGKp90MQA7HChT8Ck3vhbcfvv8lcyOSgHglRoWmfHTlto-GhAt5GGlLpk_xxZnGKi5QvJMXC99fSBGw8MyREv9QfsnUuaFWF-lt6NeoHG8HeMng64krWAY0TNnBwv9xm3eEcglB6GcV2oZQCkknlov2VB3LzSjmu8LXfuPkEsC3_GjFtoCOtEK1Jh4Z_qzZHAO2E_jSt82elAArHj3mKFXFPS51G6BnsfpOhisZ-fEG31Ht2Qbzh4d0QX9L2wXx24s56QasSQ4Wdt_zVyKnlMh0_n7LVg1iSKQpd4W1KKAEFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HTDNfdQMuk_NcRH_pt-3FGSQCNs9b3Tj52DoASaY6PZSzpQhx6cDfivB9XwC4jDViUHgg5IGKjg42WN-uXKw1Zi6NrIwCfMlQHQCBYHxOaQlM3OBx8XOcCrQWqbILWuuWidE9e4IYxCHCmHKLUbbI82TsE3VsIhcfkJ6WxBrIrumuJOiJvVKfQk4ds3tkA10g8vjPZ_9LlWKc63Jr7v4m72khKIRFxaX-PiXbkrrAVAwBOFCNIhYMj6TwSKuW809Xm8NlbnyBzHcd36pNGAR3gkMUh7DUHGENixfk2EP7jlpHhuUSwUKJFpFME86tzbJi6dFdzVn0O3HHiQrBrJhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t4I6wq5MoQ82kWcbJOAdeJ7hmZyCMK9M_RSoqxVECmxG1HynRKE-CWU0Mo5ikU7QDKCJFp2FphpDyUTDHDwzdRoGMnxqvmku8_ysNbUteCpQH4HOw5TQac9uW5QLUtHgeO4HpA3FLlfibEdyAflaDmHpOCFunw6E_SMkoox1Bv4v1PZ7X6vJwPQiNH-kvb_kxwp0gZktFWg1dcpRkFWY9FBW4dPophGgVDFFthQc92jl1Zt8AgzuYkzAcCUAaXjsUew69kdKPeimgw0ASjO_gL9cDlzZBRTLpM-lc_aMZyh_bjFd0WKaIb_jDa_ir1w0zH4SyBctkEGjDz5sxNqIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rWgo6JjN9WEFC6_Y7mH8iDXmGI4OBsI_hpSOAwHdGDlBuhvJfoxzXccwTbkhsjBjFQ8VilXQ1M49BrdGzbmWdhHrQiN9YcuiK8zXzaZ6nG-oMGsUIPr5NBhcyMOnxvzHQoXq6hnVnAWIYgL1kK_9EbeRya7Nh4myqdQLW5eGQBP-FVLBUADNo_5tLVV3FDHmrmj1KG9eeYqaIaniFmU1XjZrf7USRIoEXA_5tjL4eEOmJ47SVZE7fbqIOdRmkpTGo9ttdrIcQ33tuwI-IELClGe3q1QhrmkZM6X8jQKT_bWWcnoRpuVm9yVjZYYjJGIODgRIaJB6RqcqhMljpIBkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sc-W6bMOmBXg4jKlsM7gDBcffGSv6ojSDtYqD0p5n3o8aMNdT7zaqBwOMvWalS7HkyOq4E-H7EIAJsjMnp8xLDdH9pO9Bb4vboDS23roIubtB-NV2sUhxhFWjcl0J13LLfy2K7iqjti2Szm-G-b7XHKrpknLk_QfqIiEdmlW7N_9chqmZBl0U9hKnd2tEVRR71QQEXb9KQwHmmrEV1GbsvU3E-vwBB-_z7sgQ5tYxUCHkIXvjN-E_pFisDJwkN_kcFT6wDgGQFRM8kz35Pm2H_zhW7FyYlhPba3EPShtmbY2AMeQHMxSbJfpXVoUJPBRLWNCn6p7H14uXJ9KS4IcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlcAnpNZSMjg6R9QY5ckZMGwFxS8EjAiNUxJQK7VkV3lIDkbVCopq0-LEpYGXPz_EwLRAV0LV1A4BY5wspgD1O8RP_SfhMz6zvDHzMrzCzEZmnorAXYvWVDka84qTxsq9nBLz92VqUSnQ81IgDfRq1-0rYEJLqaGPsEHXlxs0Q5HtP2J6QVYZb7nU6tplpocmotiiuXt9fDlFtuBcR-iXisgLATaiG9RoNXa2Anx08X2_TKzNvSvqKnspthaoXIKOnJ9GJfnfdJJTE7v0BK_G1QiTbYn8ktpuG2CZ1lpyREyxg2cxJGlBUwYhufh-dl3NdeTfKGARyz-N9uMvKZXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWS2dymEJK1wcrYSAJxN0gHmf_1cXXgIBpDpJsASdNTBSxU-gewuCe1-6ZRhBZMw1O9jOtzJlWt3kKomOYyvCtEWKAB5X9I26GSdBWF-yzeWQOHtkFuWwNeqlLBJkazgej1OPElVAXj_9T2gvYNJdWReJNI7RDdG8Pr99ttNzZdYlIZd0vYjM7NwHb-5wbe78ERDMlPam2fO3WWf9-dNJ-q3j-2aaJL_l0MGNKvF3qQN4bwYX6CsVt2qIOQCHz-NTko4WHQNG82mjcY7iiCSZIHZvcc5MkmsOshwQZ9fa8433Hq8rdOMsN1p2MufUEZPacL9Z_Rr8IoRPwRVEOhM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxanuK_e0NAmy9dUbnbN4hypuZTlOrv623lwwbnpLuiT8DMluzMkTWRvlAwZ5aOBi3yhGZkisMyeuRZuwidzfZUHa1W2_7q5lmFb__w21PsFTQrZb_NJwWGp1mP9wbub9_ytgLpKIhXwdRA7X6J44ZMlR5bwz8RjoeLlQRimPT0hlKrpb4mcth8u4IGbgwARQYW2d1UjlqaQi2V-cJn7WxfjIgxQhcnVP8K90IE0PzdbMEgBE2ODUhHDPzPlFhu8h8yq0aTYx_uopNP8-aapQX2eybcRwp5hLzWEHnrUspNPq3T2E2ZQT_dBL9G3NvZOu7W1AHnymfdIo8x4cHPhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLdEw_VS9PEdpO0p2itPtLZycb9OIDYqlC0JCN0g8Yseji0zzEPVGGxADtEsBQi9LppROibtl2rprsFP_NPJcjpde5zvRbimGIlzWByU8yHLQAd0w2YapotMj5XVQQIRruRoM2buM2wW-k90kVlsbo7I8cMsNBVY1GT05DYfLG52_XnmcyTi59jO3Dt9hMcUgCQgs4SXY-qMEPSe0cRQiLqacR5frOHfIgjYNXHWzShSy531Grcn-tknhe9oWvFP-je7A7qeD0mBn5GtKMYKpsJjFQAI_cmv0-cyJ6MntRH8gzX4rETtKPLSqQblPX3SPqRgsoO-FCgSCnqJw2fsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
