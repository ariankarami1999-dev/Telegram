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
<img src="https://cdn1.telesco.pe/file/VXuXwEb61JnoATzgeqWcKGGs2Or4lhhMc87auJTn7K45Ar9gYYl7Uoe3w0W1bEUDr1RK2mwynbeSgvp7-ecgdqNKjZxEhs6pA1qdwvnQHNeToIMG4rWtuM_OBJCf2HLswh3etLF5gMrzZ8Ws9xS1BiBFDZGXI6sB6eNk6hoszs4fS7KvJzEkWoyXHwwWWd7XJwVZSKUCHPe8kYWzwYfX-uFsrx3MOr8sT7f8uWeTsxkZLK5Smd_gAU0FbR6ePVtveu-qtZR5P52GQ6pe7BuOcpDyraSykcGDgp0xgojIR5mMyQCk8T9MQktw9kCglkCD0qOW1cxY1mDpY4m82zcCuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 01:25:48</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqEoIKL8rPoxuoP3u2QHr6TEFnozJDLmRTyzgCwlHzYTBj3QwNHhgZ_xwopv4WUl7EaymlwVkYwf-E-jBpKw666HQTYfglETZxTxnexoQPJGvW_KAth8YUp_jFTNI6bOfrtafhCZ5zvzScz1uyEmCMkhXUNMKt9Xzcd_7S0imAUqKYbUzfHXNd_-QCVbGwN5_4NuWASH-ySAE8dwvxHqDZDmAzqNVsH-mlJxHWUCVgz0ZnfnylYeSo6HWddb-5kT944Ci8fdczPEBP_mdtbZfjrQqYs7fmcPc4DyfoU97X6CciSFxDab6UKVXynlQ81hQ_fMUxcrJARlu-ZhPBcePQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W2FCX1UYgMIL5As_2RAWhYy78g4WPYKovCVEfcIyuR13V8zkNMbrNxk_4aHZg4Jx-g3mml3DyxkIm_Vd55b6lIXlxN0fkzxbcrBNKXc0H_xg4I5ElaZEIlZLs3-V1COVXMSm78q9TYlWRT2iklfECRBZNXIy6LMCHfWxq8etnSic-0um1qRfLGB76nyq2X6fas2S7F7k8MIr6Xh_O48liyal0uiD_1BN_w6I5qUQrpCg3rnIH2G_O-lQ4jp6036Tv_WcsiyZ5PD86GdMEsFPbDEstpESgJeJJHLKtoY4GV9XrJLbOhqyFCNV6eQZIAyMC1UHB7_HfMGg8ULPiHxUKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkNhaRNvUSLWBmm2FUPTqJqfuABX7lzskqdbfflfmZDPOAUAi6xnqP4cyjsXCBrugaoRFfX5cgIJ2ACHVb4LyE8qGjSCHYrfKeHvVgIBLnYEVh0WgXUsUDhAckf2S7_kPsPtx8meEpHpPUAb1N2DNKxYk1hpkyhLLQ0I5NUhBinlz3fN6zOas6j7TX0nYhDY3zMuyOrBSiRnltEkZ05RdJaI29k-3tW4WbvljwoI5jz74Sg-r6gXfqKKDTSxu-4_aSrrAqaFth3uiZT88FuUDZX2Wum6bXhvKsvXVvEUqPZd_TzVYu8uGLwVLcnDwzZV-RRqPvsYyqsehfG1YcTVxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tRcChJdWL_8nJ0TR2vW8QcLzbbkYbIgAM3BrH3j3y8ufkKthMYSuHz_wBee-QBW_wvEoiutKAKapQO9PNs2sDac8rNkT9hASAR74azxw4Pd1AofkzjFs74iLGgKjyTK-teTzL1RDAu5uKX69WR81p_vZaJBM3At1jQU3BV6Q9Mv7SlIpNJUX9hmAaHEFdyGRq-Ob2kgsjujBnG2B_-bmtJObpQD0L0e6WTUh4NYNkkiJTrBC4vFxvyjvhe2fWxHyG3X-ilYPXBEDmFFvl2ZPDl9DJIkRLtTWanV3otl9m_b0t8dGPVhRoTg7GWxSlyy1tSQa8oEqea_jG-y1qWAJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hw-9e0hTImkKAwoJkWJ5cBDS_gYq4zrTekHsbNNBj1Smpo2T3R8emhhlYzCOMnO94uoyQQzD1Vm9rWcBKnAizXkZJPXlM_UijA3ABv7ug_-yNf8bGJQkfjnXyJLltSI_f6zCmBLlsAdKXVYEAjJ7GH77g8F-8fORR1fD7GO-HuJK9cEgfENHk7-5hujBsCg7ucho-x8oex0cDh4Qd_Dl_wVAi3hmUEhhhXS76ihJsbwkwF3OvLDHJUJ6wdtApT6mN0p2vf79W_NV0u4KWisRRGB__OeFPELdKvZMEo9E43_wYVqbmsnZ-UyCmegaJUr_R0LTu5yfgN1pvKwOJ3DssA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2MIb-iOA_ru67-z5pW3YPsBg8uWNPbNg-naGqr1RbevL6p3hn2BTmWkqYxTxdkVSDE2dmU4yXSoroo4B4cgknCYMxAbKjFPjspmmn1zHWlHu9JpUXgKF0yp3ioflvKUj72ejyNguwRBdspoadusE40Ddc5TUakKdKNZLIA0o39bUdoXfOg-Ow-miRK9C3Jk0Hk0a8RGLaCgdBsKqBlXSwSy5YaQIcaorxXK4z7T12_xT-6uSwj058asso2XP6XAiV3hIEtMccjec00mnqCvhZb2Geyx7V26Rf-K287OFDAGepkaKPaPxH_cFvf-5OJIhbW1MYpyTuLeegNW0VoBeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjebV5Lj6BwJpdDVtQjU4Ew-01Ihp02S5LrUsTMBaoucw_Fw30I3E2mciqFOGiGKib6H-Fz7aJOigY-GLkMoljgkL4iUMiEItB0AWWOL4ldEgsq9eVFbW1Iy3wqsbClsaOJOIFecdlHxcC8xJ0xz_JQ7RIgEF5WYKZsrUIqeVgOR10YxS2sAi-KtkUvH57SPr3qgOJfdIisuBeRCEJEBtuJ2c_RC94q8-HqQ-rI4_W1PtmfE8hRwbOrPeXtgd9Q_qReKOHkBHIGyxvyjPhZmuLcT790JYn2c1vauXTvEx1a7WsfIL1t6lbAxrZEfhHtS6oq4PTlHY0WHoO7ikIT4jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mHFggFHX0_i0pV7YRMyjD--jjb3ft_hIXf8QF8JjkQIfRcO8bjCQh04r_1MLheuIrdPLtwLUSXUCHM8p3QiiD1IZKNs3teyalSqaBKb-pAV_VFEU5s7E9Rub_iEHBV5QovKV7ueemOoWL9VmHm1ToueLuzgZdy-h64e7ZgPcKFzXELZo3XBjQZFZM_K0G3WuoYtuHzpOBQnyRTvnfBCQWtoVNXNLBs5z0LCHZ8O8eUwrNOU6BCA9XoB2R05apfqF_2q8mJ2Dp9WKgsB6M4e7_DrFEIlJ7ZHDGJmBBT2SfjVsWq8g3N_Ug8l29RVmoMen0VBT1nspaSl4nqX5x2rdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ek8SPjt4ZOMRVn3PbGAb51bTREOd11LpsNqKsQhkUb3w53wlzT8gvpjgSI8vhhl5VS2P1-jBpd4mp-jDLHDI6JnPpJnDRk-v_briuC-S10eYgdKpuZnCDz-uLcVAlFxwuORotUM5RGXKMkkKz-91UDWw5Bk1AKgkERi0EOox7L6yBWnyQ9rOiGBnTCRTXWoOocg-mK_SYzewKHJVF-xMX5ZWeMY8LAAj-kW01mjTzvpsWQ6veOOYfzvoHBRlcD3AdZ1dPKSq9QFlmOUIa-izLEuaqNtyewTmJG9P1u46UXwf2XCZ_R0Kyr1DzeqTl_75uqinwyyoFKWI4FGHGH_E0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_HbSB_-qcd8pELx1NQkd-m7bEuLjlTdI_A3klBn5uaAqTMruXFD3Gb9aLPwVjvFFfVxLYKz9ld66RaGCUJCzEAhmPhlQoUNxnf3A5eI5AQ9yx5BEK7muKF20mMdz6mMwN_kbELSKzXEDdBlg0aP9y6enmG0oMR2jCNjWlCvVk62lnHWXUckI1kFgVoBCMmNqsYKoJ1FGq4PMPyPenGvv-lTg_VPihC4NczueMDE0eutL8mP8_ZPrsNiExVIaPYVrTBRg_Zmj87D_c1Db-jn34ZcwqjVKLflLAB4BgftbOFS-sDKl8QF6-r22FnlOjlDGBrEfBTQv6hNm6VRY1N8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihEJd2UZa_BVcId33y1f-EGcXdiK7PFhJ0O2iXhnjCWyIwe3UtCK7pxLy9X_KIn7CXFf0vcg49yEmriIcU4k7JrG0eRRBRjUepBMUXulM7hkS2a-nCEpy1F77sOwoMsTqnMA1OMGDQjgkj8okHOLlCC02IsemHkXFmfN7UflIPQLndn7j37IGiQbWmEVWcZuMnnuPu1KkBZVREX7HDZz_3NKHr_ydJyT2aWAPT1pny1chxfwVPSZI5pUSHedQWB6nRWeW0KU7HpV-J9cHnuFO2pCAILv3MVBOH0WMQfXnKLNDloclh5zG5rfIbEDbu8MilHfVlL_wJWZVnZzlQ8LzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdMeDcQvxyHDElCua00xsyUoUQVyQY4DJ-IgKraGd_PeHpVRWv4mdjk9VTnl1enPxJzIMUGT4BXd1jLj22PdQVRKx-hnKcppuGubCdY5-Y-OrzDGc3hLyyNYuWu0EirZZ-a0MVcd9BYnqVmuvexPOJRJU79xxzCQqs5fZh1niPisjYZa52e6-yCnEzxciIFQ20S_pNtY-k5MEdz1lwypHXena-d0XwBSOySFcSZdiB3Csln3sVzS6onZqxI4HMxlzuF1RF7ML4evP2vIPYy3EFoyNQDYfxx_UA-7GCiqIDXJoof-TJ-Ht-d9KH5wroUYcLxDTLHlTooWBZWQ8m1uuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3inNK8OhYdLCx9-GRBzYLONpTPp0u2_1QkwNKjOnDuPowe4T1_1vesProYtxc-JCy9VRLv6caFtOJYNDfvJ99pMeZnpA8TqUeWUyUNmTHxWSAO3zUnhldZsg8xvrd6_QLcfQx7ls1lIMRx_e6AskkBS35iTp1gF_OWy2hmIJ6W7i8q9R_lH7nvO0txDg5JvaJEx9lCig39PG1uzVUl0at8PjfPieRz7Dkj0s-wDL1T4tIRXErou-oNnP8xTkr6UYMDc3RERAM89BR_89dzk0t5bVrXQPcIQorOgnGCtqL0S9Z0LSlgFkKBHz07oSeqV1oSsGRBMQMcKi5VGpF6ydA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmYYcwQvfwGfsO58OvIs16BuGfri_tOhkDJCes2sIcr9gvXpgtScOjwY_bTv861Zeg8qnMzIUUsLEckttU7IGioVzj4vSSk_uiXJS9kA0TQfMmsMVVcMoXxHrNcmxKYC10x0Oq2-eeq1rKZySItk-97XIc_QNDhjbZhaIUmcWj5DYHYuF7Xvx49IphUcAuRwruokT83OPWCd5jEvusabm3EQmN6kWOp4j6uyG1AgLD4-f8mJtRBBqNjkgIslmhiMrxHJooNugdp4jQ1Llcoqa0NJQ3Vj6wc5A1LskQ8XDSN-1AptKcyXYOHRvmoo8kXceYAxrsw_Ahd8tc-KjX89yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2uEJGXbNC0h4dnV_83Pa8h9QUIiEihZ5mT25EF48rdNrCLUVD9lqeeQrm8w-nYj9bzpWnUV4gKU2umlzaf6HhUOh8Crbg-o9jELiQ7xHZ7qmdD7QdgAOcvW763H4MLXYCDgMes2WDw788QwzXzkmgBduEvnUlLxJll16IIi0u3elEx8jsVBCAdDxA3TtchyC26QQGdQWZ1KGEqz0qIyf9xSqS-uABPgh1Lx3q-KvEBgYN7A7jrGRY7vJFPQUE0zzykETthQEhnwPJDOF_ajQYBUjlKJ9ZZQgXKGIY9U5TbDAhII-YCm0Xr_R-7X8KzgB_8bgdfCiAgq6ZeFLQS9xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sf8UaL-gEpLSh2iEZsfz1SEVYp5D18V5A3TUXK40zXeFgZgoHzRqC_hZL4c8c3UUn681Y3s3Z0SaV9wMkyDmYgHrdhlZ8bxDB3iju55YGBgWwhjztuSiwrlrzc0CW9PVdbf2UYZlnkg3Dpnbi3Wn433YY5s0hgUJixeI3gbxJwNmw6WIJ7qRtZOTrdGhSov34jQsL7xFCP8Mh_O4l_UPj2UBBiqlhXYar1-w7mTSKFMUX79lJFzraUZfM8CKHf0DfDx2ml4WSZ44bldHm3K18kE31BUlRMk0Q270twPI_RRx-KiXkU81dJByx0M2FQB64wrkLRj42NBYNqTY5mzBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rfP85w6VuWGrjyttXHtf3tG9czocpuEZUBNH_ETpNm4Jmk6NGc4U78nA9w4kYeP3WMqfq0Qc80gKWFgaimdU6uYLVfzy9NlI49hRVI4B1JGV24PDSPrDQOKCEyHw0P1WH7v0YYWTVn6ADBe-HVU3OzHtwCdkCOIUjV4lNAFGy1gukycI5aFDVpgnvxdJt9sGFvah01-e20HkOJ79phTvsCyVP9WSbGUKxbwnxXXoyZbH125LERUNjpwtbahEiX3cD8vyExD7MRer-23QvXNPCSHFe1HAIWL6OiV0JgVc-Li34lU1nWwI0Ng-tYp3ZrAhQVp5RD3t6VAV6spXc-pakA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQ7YYU1nXV3kjHNiHw1KuTPFLwabJd2OpBra6a6UMC9hNeabpWvOybffXY6suvXSzXjR7JCg8kufw4VsD0QBR6cGKAkqtUQ1jHIN_20zkNLhUEpkfUzi371mo8ziFxphiezy_tebMSu-rnHlntKQm9JyIFTCBAD8F7lXQOX9RvsseOqY5u7hQeWCKKi-oWLkJ6MHTg3CCxWVXBsPEw1hz7S7ynUwP5dMUfC8NcaDf_0LQx80D6B6x5RuYAj9iG-UZM_T4L0QlN1M-tIv3eSdsm8VasYQb_9stdy8iF75t4WwzR6SfZUjg28jLXt1wQW8wy56Ovw2Kh7gLWzAeChCcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=eeluP_RJ9CIg-wRPFBgUJEx7NC2K6n1lTxrwIjjatxoDWxBB5mbARHYZVIRTDqUMlf3QPY6py3aa_3sxF-u4wizm3psFcq_t0U-VP2puC3G9-WhMmz-2HGfcfmIMYawDYus6hE7vswBDEaniHlspeLayz3nt-BDHJL07RUa_4XiPWKIr7EjOcLzmQq3T1Gia4nHtCBQmFBZAp0AbC5856ow0Hnt1wd2T8JOkKg-Kr3R9HHab3EMqvtMXJYHwDX8ciTDiglBhREoGxVlnXnJSt4G9pZcPNkg3pIoBBl3rgguwUMc_et2gqTziOsIEkchEyXKH39ZSWMDWQwv6DkI5Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=eeluP_RJ9CIg-wRPFBgUJEx7NC2K6n1lTxrwIjjatxoDWxBB5mbARHYZVIRTDqUMlf3QPY6py3aa_3sxF-u4wizm3psFcq_t0U-VP2puC3G9-WhMmz-2HGfcfmIMYawDYus6hE7vswBDEaniHlspeLayz3nt-BDHJL07RUa_4XiPWKIr7EjOcLzmQq3T1Gia4nHtCBQmFBZAp0AbC5856ow0Hnt1wd2T8JOkKg-Kr3R9HHab3EMqvtMXJYHwDX8ciTDiglBhREoGxVlnXnJSt4G9pZcPNkg3pIoBBl3rgguwUMc_et2gqTziOsIEkchEyXKH39ZSWMDWQwv6DkI5Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PZJPAnSYbvTOJQ4IOhk3-nKSaI5JrE6XUWNhAP2vQZHBOggJhdZvxAlznvkXgpE_uuIuuzxATL6ssPZVjqCe92WqH6lfc6N7yAW5ydU6AL7ekCQIUP6LxS43lm80OUEdAyiuMV-ZRDNj4jbNBv6qzT2vMOqJgrzP6GrZs4QA4mNw29CcVVsvbmr0QmjkiWB-4OiUeMgUzMaZrFmrI1JBsgldrdYFeLOXpve8Jt3VJLOG6ADc4HmLycNJCwjCY3JxYnSu0_9sjl_tvQ0m-1AWn1jM0akB2rQEoH4-Qm8JHyi3dYGBgX5js7y1oPn-gnQvK8SYFrbRgugI-S0ke_UZ5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/efX7sT0bK5S-7zK8Cr-vYgQWPHjL_n7CMtfaXen4E8d2it6-IF5JcsSabhJUy8nEONYdzOqOMr1YLFJvVLQRQhh9Uo1auyq3cgUSgBx10NaEL5n0Tu4NXSCPZLmn2WyStlKMlf7Cnf1w0UMo75YtU3d3SA66KR0tMHMVj7QJnW8bhsW9iMOzyiSGbLf8Xshpu-2uIDD7liDfYIioYeu3bUuwq92N9xV0mkFd78lNQU-XB0mmHLZ_7hxh3Gq7gQ_8SpnMhZCtZEw6gLBOk6oB08MOkKLTE2qUFmKSFgnAehQLKsYuqSzIHmaCoYksjwr2XlUQ8MTh1MLtaFGUYcG4tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KG-yZc9ipxY70s7Ko-bXabxluGU7ul31MxmQbPpW-FbaDSKa5d6R6qYmD7lHnOhprEhumkh6cALf2khTYu2wGQymvtuyqLGYoLqT91r-DgxnnPUkd9sQBk4AbYakY_O59BgoevdtNr03YKAmhU83uQPdpDfKm80dzTPawzHzSvIIAFw-ogRBEyJa4rHMUtYAbleejDZ0G5-UFGmcwgOp8A2zJHvYkRGSMZsBl3kVEnwdOgkeWNjzURkQ816g2kgDtGL7g4yBtmWhWK9X_O2-HYlBs9qOEr7klnWIqEoRk4PDXS3HdhPhyx5YjdiBwAOtGQd5AxK0PcHF7p9t3UhhUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IlUpgKbaEDWXn0_-VzxoGFA9htGl0Lvsvz-npzOI-q6XqmlbDqus5DUhC6oGP80iYI2F-rNAHdp85ByvCKmyED4Ldu9ywuYsqcWKAcFokPFwpYrqc8TJE-NVSLgGEEpLy6iVTdvqLbM_URLro4fzf3bWK1rPDwiLRH6iSgJbtXSZ1ef19n5CE4v8e4j_b4FZyYChyaJikHYDWBR1h4_y-7LDsgY9UVlTsUnPCuvXeHCGj16PFT5DPBSGZgCQgKYHy_laakMCz9fjRoYEb01lW5D305HjwyARtteFTPjr4uKTT6r1WzeghYgzBLkQDuqxA5Ba3NPUmEatEevR-nMNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qUl6RcOQfJUzSjDiTZJXBu5CbwDPPYVDcWOH221BQKr5UPG1WlCDhtRghN7UoE-alEqXN4-fooR_HSnBjPmIcdMR1OTmf4BeemEwMIP3tI7oqteY-brbWw-NyqtdNWE0hJR9E39x3RMQPXpbmdWIY9867GfvuNks-rd7r1S2A_4nmfQvjG8QLZizbo6yI03Wy_e3QgemI5BU4Na9ZfMFIVCai6TjVaiXh2p4lAlB_e0ureSz0LI8IvHU938yuYTpHhVnazqpTxwIt5ntOeHX0U3y_SVDi5B0PTBV2Rog-VdAOdg3N6IApO1zL8tkqGDVlLrSfMGuKC7-Nk3d24gEBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VJ5Aaba1mWOfvH8tgEgNVGQZ8W7ZmrbEBLw_yqyCaJesyZkw7i5vqdvJY9mOgtM-e08N65hxjeuLBR0l2ESQ08pRjQRXpoePtZpod7SidLRgMPasSlbXsXxakfuAOXxOXfjmDuRUI0QCK8oBL1buVOkENNpKjksFAc81bpowL_-0lZbMCw_PAqzx8b4YYIYf9GhIRQ42ur2GQWOwKpcMdPRdT4g3RGD0UCiv-6XCbD3-hPxjDCbcbWBwzTRPdASMMziqbwbpctgeJNzUe6WwMJqbSBVi-Kzk-Vc4EFVMXiZWv9IbynwAyE2dkMB82ON1KH1dGOWAFsGCN1LbQg9fPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3T6zqh8AG7jkekBxklTfl1OfUN_g4bJHE2gwuHPLvvwzVU3Gu-tgSdTbna5VOXUTFhFPir0OauHdBnYqG3zmKUpX873LkymJOoOaLJQyZtWKFCOhnNeFdIUS7VDNJwkZ4-2Cp9zpaXHjQ3W6mw9jmRvFwIaIoIIxCMvPDZ93gWTVEBtHi2jfDLwyuMwYon5VC6YSz095wO8V4PpSh7IyqUzsHWBunBrRzDkPf-U3M1eL8lAEedW-m2Hb5PUnYkztBn-1ZUlRZrpTkNp7YqD38CTFRQTiTJ3e5LKit7N_OXGui38HNlLWNaLIfhP6Xk_Gp8NQ5M94q5bEHs4QQ4HEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R5pkY1EySv0ASh3G2qmU3XrHLp90uthZCoW5b_MMB5OYltG3XkVqkh1GnBhFYrWQoEJJehDsqGSm1cTRWWD9xm7CVPH0TtePwzcswk4zNDikVoYgutPOfNMiKUXQWUb6Ggn08hpUBcmsJPyw9xg4KXyrB-PdQLXT8tZt3oeK_CpZJR125qN46GciQmLqD3tDBzTSX1vAq6PHaYwlu4j9adruu8xcuWla5KPeaWKv_KQ9vVNzgWBdxDvZndvIln-3w-dQJ-xQmn11jZmBdAj69QBoaKqWO3CYc_9HMg6xfDanmivyN6DdjesF5CNjkw6C46tFEEizTfSy6wcOfi2kMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1EAudrvhd3b13eAn0l_T4Km9Xx0k2Mb9j8ttSzhQXcfMWrl9opP9T7WwaoFoW6nXIXTS2V-eIQ3OUfuNFdjHtfCMwdq4R2qKNTDD8w29OITmYaDtr3lyLXNbCgoD0P28eZqQWwLekPtmZI5VInGFNhTWSzUYthzQ2RCOA2FbmKVJNVewz8yRapU2Cv_kK0z5ASWTMoJWJQ3_ERyvwHoqRYJBg-cpY1ZptZNDOIlkTq1Lc24AzVoqF0UF8Hg5osAjN0ot1SMH-pHBgt_mJ2XX7FSS7c4tkVl6lhChJ8GibcV5Yyd4xsuH8oYEnc2g57r77fyBd1ypgmO40HqSjilNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwCG7rBTmiZt6bI6vTPSF3pX6RwUVVT8IjPWG2IbZFfhF_mS2abUlqsHWkDOtEiVf3z4-HXXxPmQyDg94-56Qf3Wii1md2mUg2yeCO2hiSYvZaHOeYMTKl0yaKAjF8Msq8FVO7_YAOhaR2KvHubC19u_otKqzBa0FLpllTfhlbacJnNQs9I_QitcRTeLUuRM8kEbmUe-q1x2x_5lpz1LZ375r7L2JslfYBY715nj4GCdatIIHEqhVWB8m2__oCBrUvHWPwT1jwk-UMExkepSfdDprq8WSH5ALaGgkjba2gA1nUGcpxzHgNUDfrbAn3J3MKbDJWEuDhp6EAS_iYCCsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h4V-XJGEucWunfDjMyJLaxm5ke9tkyuYPQ2kd5lRuQmtx2MBjftozdSoPKiNT1vK4i1SD4gvyHNJNfrFNTJM33yiBD-CtPd68MzfcOrvWygepguJV1iG7YplmOLMoC329GtpH-UmywZa1dLFo9EPhDFfP_39mg_qcMsj701RHzdZcQoIRycOZ9qxeSHkb7HYx4nEtgQIFt9kcxz285cGEkm4PyHeCECo16t4sSdZMd1w7TmPgBHQbjn8gLeoVH0XnVDDV54KRrYT4tMx-bntvnDs_LGcoKeWXDl6UsLpr10i5LMkrh8n0QPwVUdSYRT5CvXUxS8nuBtaaGrtYtR4wA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZB3EqcX4ZiMTCEjibYnCFJVELhHeL3vUCoJ12pGb3V9xYPx3Sh0l2UMw4DxlKr6Y8N2A27gwId7NNwWlVKKCIYpjPGHZLDwwB_7vwCl6OtGViPWDty_-HD5iQPw5q74AqNb3Q8FLqUd0OBOuK8i7PJMf5egt47u_XUopAJ--gnEkoMgFgJwgEWzoRcTV_8P9ekLwasl1ERa5qCpdUZIrwIpVs5WIpHASak6d8VbaK9QO4vKHSeYvlTnCDgPWeHwXVyzmRB1uZe7vwd--bX2fTeR1-0vR2nfeLHwNqwLfw_qL5QF3S9Yl6mlkgjIpXwJLpCY66tx_aAMaw7j284gwDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urUcUsbvBP40wH7kvK_BO9Swtsbwt-i0Re3_Q1tPaXTQucNCgbEDqcDhsWWYMzZV8Opr8LCtW6Q8p7DeOjkk8VxqdAc6K-5cYVFruDHEUjpxIDvE5Ms5FwvFdFVlYBcxSGcG8qv1JZYMZ9RQl-55JJqc82ZhGaP5O-SadpeRKmgDarqFSm4UgELsHxaZl3I1pAvbqRbXFm_kKvAD5J-NtVZx1fpjndnUZUn7o8ni8fJsdudXpS3VxCCfTL9S9VHXV4WpYKFLTQRZb13Ckr-Y3W6tZU0gCykntkOWnyhQMEx00knZ40-CC9O3zat3pTn3ZrcAspghu787fblntXGAMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKZN5kcm57vDIZx-fk7g2nXx2A0Yewd-fwMefEXgwhYAs6WV2iSPcjIJw43R13yh_zU4OvX1gxGJfBeSOHInZLxUVa5Cg_Dh9QmIuTxqZwgkeTxQxsHmgKJBTcYUta800Ij3rjjZ9CaiHkQZm8AmCihqwmYSM_6fWpiskdCAw6g1gv51E2_y8TovzgNxxsNFgXHlSF1OHrHHtlAAtZuU4urCREZAFVnMRA6VRVBnTeQJS9_jdxv2cJdTRb4v3YWBc5UfSVROJaXvBv3rCQTdnacr9wqF8PmRTljwMYGnYHn_aXqnoWe1YRWaBGRCjAhiIjg_F0TOBCFvyIL2r_wSLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6CGu0cqdUDSOsugcGJCqaPokkxv2UH8-1_aST_6VMKMI2cUktwjTPqwOh9HTwkTg26rFBtm4yumAmBJGzWysJxPJMg4qrUZVGYWlAyK_KzJSosgTR6SsTLiyv-f9rClx2cASebJpJIiJcE0pxM-LCUJnw9PTBlY0lmcj9fyIiIRqMA1ESGJ9mEI9-c9Y_bieMcARJiKFhOwWpeiWbLhcpfMx_uLbwZM7jNxYe2UeJROoG_STBluqOgFZDkV6bErf6eehBJUIJo_pietU2EQbP5pNHgh9cyXjIH3ZOFRnvu9qmeVLuYXC5HKSqdbyPG2GzCAlzY5fm9heNnmDA3zEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhcHDHrYToK9o_E1Beo0y9sBhOF7M1NZP5N1VYWt8qJZ99ckRGM2HEHY84izoryvcRzQx2ETKfxsR2MOCTQXM8vIw-X_5Fc-1FJ6aI8xsiCiwo_W6of4aW07j2LOR0_OzvJlftkh2v8WEsvE_y2IdXghl-zd7VnC38yoL_qccli9KXWnqHOdvYyP7_I3ivT048chRO7x8QvlGRp1SnZXHQQCq4wshrgU9YQarJpHWoH7opBi4oamiQ8tJz5rHhgdj6irigZMjiTiEd3z_7rfqCxHVOrZWYdUKLxZLL8tNHRvRi3pYqjP7TfoJovoPAdJHMzyO4q6knWMHNB2LaMEOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CzIcX7pjtGV0ax0CHi43DGmXeldP8sNARS00ZyjeimycNph9o7NdLBgJckWfAXfZ5S-iMAm9N6mFztDLBJjkfJb6X6VCtBJmImjDUOy94GMyFrH3Rd5Ze1oBh2CL7DkasocyIw_fQD7HrkVF28NDi1p4d4K6747YbbrvCd7Vdz4oaTJK67IDZYJVQj3Wq8lusT39MQLLrlzAzbglNhYWxHm8UQs8oLLA2dodm6F_ZnyR3IlQdRMUNGWC0kHgGcIBSLXaTNVtqW8luFi72sy50_ePd2lSCYt51ZWiEnGf4FoaAbKhU05dtlysZseRZ3AsS4SQkRkRHZpBUr91g6-RQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lFySStoRY-Ls6l85zgurxToKzm8GhEQifw2zvYOmGU_D_O0R7fxe9nqZiCcDYvbG4FPbKp8cLwuJlsJUNzLSaZxhv76USsJYzeTR-jKDys98jn37R6x7zht0yMykoCB0mMh2cMGwRhhmw8S1d_HnexWKQMOHmsK-Fz-T6ClcRFyEPd_OcS_JDDhV1-qfOT7NG-tCnxTaUf65oMacK0onXHtck_H-W1_TSUXaCDMQyzklOlZvxDgcSHHHg50woi5S2hiW_WRSBNR_c3jhefUkK-TTFXxJlW070BsbfKDvB7glxdgXjnnDjCyTwS5IQApY_JTeAo5pVu0Z_tScTSpsag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BFARDaeBur2KJ5wZRuyCtQq_w8jOHesK0JZHhpnLaXIkt2wwxYkbm6Ag3zo1H3SfEtWDQAMDWWkemsuuCLbUFWVhZ2oJLSvMxE6pn3qaLlUOf4VxwRWBE1arkjYY_X9Qxx8M5smtUQ3RfR05LPE2e6KPLgEBRo-Eoafp31KBY3vrxGWENdRdMVrzxE_uFEpvKBzb8Qgv-j9u-_prVc6KsXo4P7NGuxV5fhyP2wJnrak4ye-dpplQsf9uhW8PR9e8ilOTU_zKwFcSGoEVkPvwIU6uqr0nuwVuUBlW2lvO0nW_zKD-pmfP5-BKyW1lwPA-eGQVVuhgUmzkwTFFv3A6Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IykptIlKDq9K4Vu_gHZPZ3RlHAvTvxjvD8kGY9qe_HhDzuEi_C6S-5V1Yk3Z5yhJ5DAZAc99lSkwbWyo2WAoz-LqapqFVwo3yBA7MEm-UcMxlOzyAKoQmcwjFgLQyxJGOVvxoNBZiiHTL4AqoCsVAfmyhOSLzG6z5Wi1SfF4a4XcDJf-fiJ7vbipK_fw0Tr-NburC_h_FN7-enTYuPvREK_6B7ph80jO8Vzp1cwvfPA5IGROJV-NCmEFHo2hJZ9D0onW3pTc2Mv3KyuoXgPWYcQaVrHA_ghWLk26CHOJ6rNTAZjx9dnYGXiBkCl68v2MQDlkrgW1ZiPmhR6-wIN7iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pafGlptX5djZXSyExhMcxSEoOqpobj8IZOKTvgr_mfo-3kbp5zcXqSw9C6Z4VcdWXh1x7ohicbzck_lFv9Vd9BB2RBQSh7Xmb8afp3dDQaGH4vIBX0hiVn7D8FU2jRLUxiuDQBU8YWUsB94k_aX4YmWF0rnbGsSoP-llKbkh_Q1EI0daZM3HvMWF3zyZy5JvippUNCkDN1pWOIbtoCL85P9yPigJ-IAcaX6o5X3juU0WpANSVCQfLahaiD5V0byFjPmivn9dpNDfxFGuzPRUrbXVgzaYVXQok2QlFhT5DzrM3N0wpwJ8D7es4v5Kati4lk3mZe5rYcbTgbjNWeGmPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kt8537cYJmZO6g_HWO25Hivox2_jtOCspcgWnTvFj9atXLpHud_EtbkT57_ZKa4xgQr7-I24OIkqm6hNmh3YjQcxiodcjfAysy20PctOtsbUJY24A_8kcyF2LFkoK_jn2ZKhcKUsFhs3Q5NH_qXqUB8MOc7Mk7FDyEm_3eJZFTxPqcpHpnjWwa1EkNMG0-eSrsHMG-Np5rSKQYzI7gYYRPrzGJhajh_EKAPNaZoyanNewfzQchBS7CvTriU6vY87Q0-0qa5CJP8e9L4wjnDj7NlzgEeyqDyw8wSy5yDv4KovaZG_F-HDwWPIG-J40aZ0USSzBcoLwpF75jF1saQ4HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahDZHaV2WaA-WMPOL9py8mxC0iFBj4-p6eLU0Q8309r1uWAIHQSIWz48i_idOL0o_hzEjrdeg72BRJzF9x0M2iAkoNy1e3Z1JRWyeJbbAW2Jcg7a_coLvUYYPZAw-jbyPRoo4WEXG0Tn4QhSeee9-QDxZTb3Feyb96qVxNEAdpwoJOrbSRfmVcXHf0hpRbywlPsKVGe7r5kNY1Hwofl9dEh7LzCKYVZKCExf4c53YlMdh-Xu4qdSClBWdOdklCmB2sSMq39Q9FrrDupwxtJKM8aH9Mjk4AzTVy7HRKIlLL3Mp-HlG_frR9iXGnkgdqiPUdRU2V0YufKTT5xszkwG_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4t-Iifh3Tdehml_73X4yIIh0TSo-OVnKB74o0296ms-uhU7K1NrtOJeZwj7EGI71XZ36pt9TCxR4hHDRKW5RMOUQp39ylpz8RGJElmVIfMo1rXA-ga77eE7LOMYXm6Hg6mLdHSc_2MsaCWnqY91B_2tZIauCr_y5SyWD0lBedfzq_yhVW9pquM0Nb--x5eVL0b5qsMc0-JHXW0Bzl-otaGmFhzqsgImpH_GHJgBwCcXM6UMIg4aN27ADH8ph2lMEGHIdGZoNvoAwWTfCZP_D3nuwM-_nEf9ZphjN9kRmCZX8H8bWkhEAfpAsrzgIpwUIpV7Zllwhcfh-6xPnqEPLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RAqr8atybeZ5yheznk5x6TZKPPh6YI-PHM8mG-qRrFJEn8WOQeqBph3S1QrYLNYtlB11Ub1xX2R4W0v0mrWkGD3dLaiZChVxEtNO4CSAXfQBomHzltEnnVItRCZ4ZYjt_t0gWVruLbwIo4VN2e5RtyHObJUJwZzkAwY79YR4MeGD5wTLTHjm2cqtjOPkdR3kwg8xnuhOwwcDSfzhX8ofwoc-7Gm0ytlzGAa7-VDddBhkOz3XzrjCfFNR05j4elDkhiK0iKPhi8eeRtp7C4a0yghq02d4o8yFg3Qyl5nV5fvi_KQRHCErF2ugj-PYwXSUdgMs3MWDD9uPkxNYdXdFJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UGhHW71ngg7JAy4lVo6CxyjU76RSgDMG3kZsYpX0r-1hdblrGWpgiNpKihaRq2Qnuua_GmXOgaI_mC-4DJucfb_-gM4rY9ZMH1uKISSLM8mQWCuCjPtatkkHs10R0YBHUehgTjNm1CkE4_rgQiZwH7uTkiUWOaVWGVp8CK0tEHDISwjjB9rlmKgXgvZ9MRYB73YZOpnM7A9HT_U7oMqoVvhf9Gb-jcOgRQmLsAt9dCDDlbUDhUuY61ulgGKWeZupiW_sFyQoqKjLMgkQRYCm-p3RN40p05MxTeYs1fqfkx8UYJmh3gC1v9CJaC6dKXIvAW2L0hVHIp17Qt0FuLcW-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtfH0Ue1XfpFph6D2f3VVZCn72k2KUT-bnRZRJ4rCfVYP1nBVMM90qxdhQP38uR6selJnJCmXr6ulC8wAnMcsK3UpPuQT60M17z-fP7hlEg0Nhj20enO0AhztbVaAEUjm1tlSru0XKuUwZqjDqj_lbu4P9VZt6rRh4Y0OwR33qtE-UoCVJZYnRPPz2bgwU6l8_Aaq8xKgiULnhznyH7a-JhwfUuU98OGpucc3Sruy7CCLoSpan3Npk-aBpXW3EFEhf2aSQ_rbfsyNIgN1L1EbLBtenpRF77Y6vu5r_ZBhBjlAtgrlWxYL9GpMbUWPiirzSWh2CNnYDJwhW0xzmSu7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j42MvOh6ykf8i3gPI44ZCWijmrnqGRpZooGBO1Hm-MBg7A7erhrMSl5tDOwmEK21TPgehI_sV07SzyARXc8WRB1j_z83X01Al-IbUxHIAmnIeps-82IyGqIYbhN1kOo4r7WLZ10pg5JhkWZuVLn8MUfP60SXvhwNA3oFBzvTdwqNXl5jduj9aAEw-RZ5D1cwJ5x-0SqnffZW005Tc0ISr2cW3xSChUqbFjdu1C80Efa_eIKsWHIxm15dCc-S6kdx6GJGanvsqqeKJI9rMa3lIfqEXI8EWnocRuHF5j1nFA1oePhJ_VKM4d7KMkU5v0jClmvTKY-tGpmQd4FsnOVDWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ChTR_aS0QvC4LyLoZjqnnkxJMcXzSwmX7AJXFo1cXnXfxd4Pjae8htAqB1TNz9Pez82lOlM9oeg0QvPoE3_8T5y0BkIPF-pGUK3rqKZ7b9H0xCGI8NTF9XqD-U-hE5Is5jxmaNfmlvsTHj0B8GCkRgHM5t55f_DXmNIQpR8fT2wonP3qtPPtaP-DGZ-WeqSp9yi9E3qTaGNOHOut7TZO9NhqgDVY80dIGO_MrygJB6J3IUaZeszsMbUTYPYS5caeGkWI5holQemNLvcg22I1HRq7EGiGB80qZXpg_u5MLNpAUYtRS9UwKwOvX2cKLqO2XszjEvQMlCv8kfaFT6sj_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovM36Tpp_SGvXHFeUWbHrWmECcQKP5ZUVhEl3n6F3DbTNd87Y11A7HL4Bs314zS6foM1_K0FCg_QzINl421i54ttU8sTb1OwpmyQ3SbogXqHua2jGdOIlP42GGq6kYuMaxAmDcL04YG2B4szHTRvRpcfG-6BfAYlY_WUe6_TF0WP4ZOYQivl-kToI1_N_nPIGK7sGiGplicFEROG_K_c7wQrCo7rvDxsO52jjDtnVWxn6Pz0Y1MNnbXUldRoQ7-RDZgYPr0Y9VIT_7W3X4pOltYhYuZsjr_A4QZjEBO1X56iZ-hW7q1Ie-9dQ_ZfuekMMhMDtprZliwkrN1zTpZ1BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ohv-F72aidYIjUaN7MoGIefe1WR1iyYh9J_PwWVsIf7VIYkDieLJddJx9HqVG36BsWu73FVK6GQg3-40LSEUzvKlTdOTl4quGT6fK0oZoYLPZLwJIo4XEcwQ4nY7LGQqy0EMRxG5Ku6XTIyoppOzvMJ5hTjADmew4to_brGKiGXPQNBnhU5KHgwwywX8sOjEXgBFxp8mwKQeF-jq0lLZT0caNpScUHycgPm2NvgEYhc3c95hvjMlZOAdC4gPGxMY9U8zOs7BWIo0ZSOsH1X_yT35lOxmwNshShZpgoLjONBO8HpUV49YclhBzAAQpakMSvrDN74-ZmAGt9wcEYjMlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hdPtydtetqIAFaEqWsRRHBn-ynvn8eg1Xo6JN-IpGOI0kIILmZTRRwFRtfl2vOJySNogqeQ4_c8UVBRVTdgphyEWe6aBC63JaEgyjYu4TIoZlo7Ep_eWSy83mNUAvL1h3c6Ix7y_kEYstRwFG-aXnU-PRs1Zc0DhlxkR7hzWQ4clI_AnSt9cJtIWh1b1aeAnBMJQyWCeLRuZRM_64_-YYv6LwnfgL3w-yZFo_g3g9vVJ0ovwm-V5w4sU06qa4yUmQsLBEYa63LepmtX0enPtjZTSwFSwG9TQZ-5VaoytkQvAenmRgZP_2ZWZzDcDLo4bQNW20ZG1uwjLPY1dOL9dkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8eHXfKMpxP58VA-9P0bt2QWocKk787ZwmRmSpRhBJJm4TOT329hgpHbVZ3exf58WqoQMzPBlmxg7j5WQNZxQu4BpsojqgFEcbP8eAU-VKA8-FuZm-sijYCttq2hgKLwo_SFo2T-wIKsvl8f31hbSZlHJijGyZOE3wVTvaiIkZmCU7X40Nl1zQVdRTXdXAA99vmrG9fbKAPKz7Z0fF2UHaWsYXVhkGB7nQpYfXi6YAM2KubQJECn492zHaJTIDr1iPwKdgqF1qyq-eGcg7Q0Mwu8SdL79QHwKpwg8TBAQZN-chBSNnKEps64RRcVWNpegBlkzqwO33yDTGSa5sBVBQ.jpg" alt="photo" loading="lazy"/></div>
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
