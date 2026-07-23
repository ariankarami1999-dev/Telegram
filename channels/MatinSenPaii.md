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
<img src="https://cdn1.telesco.pe/file/vrIic-vELjnum9mMAuXPs4YT_Uc_cysiEvD5CbLapEBOgODWBMCbtGbPQYpCjoJbldCj8H8XrR3SD6svjT9vW6iakMXuAN6AdKLWbh0lC_BW_uy02BASmNuX0MQd5k1-acaqTs_2dKnIlV73lX9c5DVjFk7UBv172UnMcKWR7vw5z27RS7WG4Lf-RgMleX5VcY0QzPf0avrAlW245F79EdahEq_i2Ws2xEVMQsCHD3oTOuW_9yfwzAAVtvvnkCu2jgFGDp8iRlx3NJsZ7H5hoU3qlibD5D5oAB9PABXLzlJBc7UTDN2prr0hhc6hJnb2pfyLby9dmFuk3DRv2my0mg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-4638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">انگار دارن یه چیزی رو روی فایروال تست میکنن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/4638" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یهو خیل عظیمی از آیپی تمیزهای range 104 کلودفلر واسم از کار افتاد
ایشالا که خیره</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4637" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj5OQMXo6eGTWrYUsKybK1mvnqIkftGTVcq_bk--NHqoY3mwBK5rKHlPY6oLM49ECvyVGi0m80DniwNBh-agLFKVMBHg0QBKkeKhzIZt9I0Gxnct33UNmDyqj0Jdfv63OCdEW9AoUy2Qdil7MaaVnGbrsgytkh6Ivo_3GeJRoWF8TAPhvwb5-SlyVMQjSzZyYTjya1p8jOx5iBNKf6xq_Uozft2o6qN2SzQFOOgpELZrvisMFckIEGUoVMVY7DO-D4WmdtVqz2oiDezj105xT6xvroWZ0Vb2h5lyKVguh0oA4tKgihR5EaxXVWotqWOFPqp4_-MkDkyuyQWeyaHPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/4636" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y-WSgd_rsE1JvyqPZuSQoIg8fKYLeVaQsIY9fNanmf1eHy12XL_ISmkKU1CRAy4Q0ypmJ1RQtzkUuo6IScH2t6DOG9aetyFRrl4NUvIq3hXnMwD6FhlsOAvlWbYX4Uceyc6kt8P69QNRI0u4SR5AD90EPDhh3YcrYs77dkFSgY4DDasgIt8SSKjuxvNlain_OR-uL1wFORdahENCwwItvSL_UPGath7mYBFvhnL86BnwG1oYpnJ_gCD4lQXYNBXz2CMa6jPpP8iNRnmSCZfF6RUiiAdPphrNg_uKOycVVbpQftv8P9itBF8OtIfzaCAM-69pZRPtDLGmNYuco_WZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام
😭
اکانت Nous Research سازنده‌ی هرمس ریپلای زد روی توییتم
ولی واقعا قدرت این ترکیب hermes+9router+opencode+mimo هنوز باورم نمیشه که از پس این تسک پیچیده بر اومد</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4635" target="_blank">📅 04:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بچه‌ها من اگه کمتر هستم این روزا، چون دارم روی یه سری ویدئوی کاربردی کار میکنم که اگر اینترنت قطع شد به دردتون بخوره. و یه سری مهارت که تا اینترنت قطع نشده بهتره یاد بگیرید که بعدا اگر لازم شد آموزشی بدیم، بتونید سر راست برید سراغش</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4634" target="_blank">📅 02:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4633" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4632" target="_blank">📅 19:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دقیقا. درخواست نوشتن راجب ریتالین هم داریم چون متاسفانه خیلیا به خطراتش آگاه نیستن</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4631" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">متاسفانه من مثال‌های واقعی زیادی از مصرف خودسرانه خیلی از دارو ها دارم میبینم و متوجهم که ما همیشه دنبال یه راهی هستیم که زودتر جواب بده، اما همین راه‌ها هم بدون آگاهی ممکنه شرایط رو بدتر کنه
❤️</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4630" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4629" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4628" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_lu7eKY7dq3sjAvZA9_E8rlHVwZ3PN9v7SQwl1Yw5HfSxm-E6IFCVJ35705bCAU_HxAf8I5FQUpkWf9lSxqG7Hz5ED0n4HnAMLfWS7z9TGFHLgSBzeyovSiAyDhEgLFLzsZgYWOr2aRBusK-T2S-cAaP5OXrKXw9B9_XUHThpit3iLyTtKdu78OIV6Ry6KmUJuHOafXVGPpwHduMuvqHD_Ma4xWFJM_ng022et3j9J7Fr88ZL6du-w7ZrASI8NK5dxq0MYIWVsjy3ZgQzgDLnqvfNSCF_Br_-dnKPp1mddQTD1ny9Lx_UP2XXGQ0WPj5PvinxuuMYLNwlv4B8TYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.
ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد ایمن محسوب می‌شه، اما درباره استفاده طولانی‌مدت هنوز اطلاعات کافی نداریم. بعضی مطالعات، مصرف طولانی‌مدت اون رو با افزایش برخی مشکلات سلامتی مرتبط دونستن، هرچند هنوز رابطه علت و معلولی ثابت نشده.
از طرفی، عوارضی مثل خواب‌آلودگی روزانه، سردرد و سرگیجه هم ممکنه در بعضی افراد دیده بشه.
ملاتونین
دارویی هست که به‌صورت آزاد می‌تونید از داروخانه‌ها تهیه کنید؛ پس تحقیق درباره نحوه مصرف و حتی مشورت با یک متخصص قبل از استفاده از اون، اهمیت زیادی داره. معمولاً پزشک با توجه به شرایط فرد، پاسخ بدن به درمان و علت بی‌خوابی، دوز و مدت مصرف رو تعیین می‌کنه. اما اگر قصد مشورت با پزشک رو ندارید، بهتره از مصرف خودسرانه و طولانی‌مدت، به‌خصوص بیشتر از یک ماه، خودداری کنید.
جدای از همه این‌ها، بسیاری از متخصصان خواب معتقدند ملاتونین نباید اولین راه مقابله با بی‌خوابی باشه. تا زمانی که سبک زندگی، بهداشت خواب و عادت‌های روزمره اصلاح نشن، نباید انتظار داشت هیچ دارویی به‌تنهایی مشکل بی‌خوابی رو برطرف کنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4627" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YR0cudbeBlqyOZfCNEb_A-r8Y7ShOC2eSiV0b79ELoZVXKUlC_-XkzrmohQCbQC--E5AsI87l8y2w56Z4t9vj1P0MqurhLSQDGBbmHmNNODRWHP4GXUxMURbIw2eDCpFe3ryqkXj7fRFD4-1IaAhaT2JQeGIN50jTxzoeYda9P_FmM5yjOtjY6zWwR0Z7syP4ZoabYkzb9yfsIAFuUS4wqEnxMLbmne0HvlrP3MYUARiw-ESOh6gqT5_glXpQ5qcgBfuzq_Ssf2bgBU59Xg4OiX80IArpWWPT78pJ9zMHate5Sz0BYTCAgWQUtOMx5K8CkjIytwqC-jPaOmHwztEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فقط داره گند میزنه
الان نفهمیدم واقعا چرا نیازی به 3.6 flash بود
😑</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4626" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بچه‌های Fireworks AI یه بررسی تخصصی منتشر کردن که نشون می‌ده مدل Kimi K3 نه تنها با Fable در حال رقابته، بلکه ترکیبشون به سطح SoTA (بهترین عملکرد فعلی) تو خیلی از بنچمارک‌ها رسیده و می‌تونه انتخاب خیلی جذابی برای برنامه‌نویس ها باشه.
البته برنامه‌نویس‌های پولدار متاسفانه
😞
https://fireworks.ai/blog/kimik3-fable</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4625" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4624" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4623" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4622" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4621" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4616" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/4615" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/4607" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiRKq0m5OEbJnpLp5xEkoJ_MIe7sTTbvhVdFUh8c26aZFvLjbfYLlc-iVhu_eiNKpJpsOumcUAPiWDyw4auVGm-btlZ7Hde6ZoHgtrf_cCVGqEnHpKtOoONHM9TOmornTCKGKUmAgztvF9oHzhyjWmoc_j2znKdCe_x2ogO_igyV5ryHdgSYEK_7o22iUdu3jwUtFrMT8bVSKUJEkTETq9YkFUNXoN_8ntLrOzOkNGUYv0NmNYUxM-9t5wSxEpCaL1grWDjcFE1cujzSOfSthg6gl_VU15N5D_OW9lI9aaAxjV_xMnTXS88m0W-AzUM4fuV4jp65-c64e8VR59JnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/4606" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه مقاله توی
exe.dev
خوندم، راجب این بود که اوایل سال ۲۰۲۵ خیلی‌ها می‌گفتن هوش مصنوعی مثل یه «کامپایلر» جدید عمل می‌کنه؛ یعنی همون‌طور که کامپایلر زبان سطح پایین (مثل C++) رو به زبان ماشین تبدیل می‌کنه، هوش مصنوعی هم «زبان طبیعی» (مثلا فارسی) رو به «کد» تبدیل می‌کنه.
اما الان جواب فرق کرده:
نه، کلاد کامپایلر نیست؛ خیلی از اون بهتره!
چرا؟ فرقش چیه؟
توی دنیای واقعی، نرم‌افزار لایه‌لایه ساخته می‌شه.
مدیرعامل استراتژی می‌ده
👈
مدیر محصول فیچر تعریف می‌کنه
👈
آرشیتکت معماری می‌چینه
👈
برنامه‌نویس کد می‌زنه
👈
و در نهایت کامپایلر کد رو باینری می‌کنه.
هرکدوم از این لایه‌ها دارن جزئیات رو مشخص‌تر می‌کنن و کلی
تصمیم‌گیری ا
نجام می‌دن. مشکل اینجاست که ارتباط بین این لایه‌ها پر از اصطکاک، و جلسات خسته‌کننده‌ست.
کار اصلی کلاد اینجاست: هوش مصنوعی می‌تونه
به‌صورت عمودی توی تمام این لایه‌ها حرکت کنه
. کلاد می‌تونه همزمان باهاتون درباره استراتژی محصول بحث کنه، معماری بچینه، کد بنویسه و بهینه‌سازی ماشین رو انجام بده؛ بدون اینکه نیاز باشه واسه هماهنگی اینا جلسه بذارید یا از کسی اجازه بگیرید.
یه مثال واقعی
:
نویسنده‌ی مقاله می‌گه برای سیستمشون نیاز به یه سرور DNS توزیع‌شده و سریع داشتن. به جای اینکه خودشون بشینن کد بزنن، اومدن چند تا ایجنت هوش مصنوعیِ موازی (کلاد و کدکس) بالا آوردن تا کل سیستم رو براشون بسازن.
نکته‌ی جالب ماجرا اینجا بود:
وقتی خروجیِ ایجنت‌های مختلف رو با هم مقایسه کردن، دیدن ایجنت‌ها کلی از مشکلات لبه (Edge cases - مثل وقتی که دیتابیس Rollback می‌شه) رو
خودشون متوجه شدن و بدون اینکه از برنامه‌نویس بپرسن، براش راه‌حل و منطقِ کدنویسی طراحی کردن
.
هرچند اگر نظر منِ متین رو بخواید، ai همچنان نیاز به یک متخصص خوب داره که بتونه دیتاش رو Validate کنه، پس به یادگیری ادامه بدید دوستان خوب من
🔥
🔗
منبع:
https://blog.exe.dev/claude-is-not-a-compiler
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4605" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4600">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4600" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4600" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4599">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpewt8oTN5JYkbMjoCJEd77EdouTFDNpTLxle22tT_an2MVUqcrrCuFZx4tBk41NkKUevoFyYk7AzI4E3aTwDYcJamiSdFnKNoyKbdydDpaxV8eiWQy8FJfYo7jEWuBkxN47qZET4Y4iAGnWdEshly9uK5iCD8j_ibOtt5bxyKbxfQ14_KBLmuBnARs84x3Ms6TiM_K6ED0c9t21LIvXoF9eV7LeSzN_BaOppgXb7QweSihiUtdHA8GDT-EbqHpWZFj2tku7ibj7ymg8jMBIuoFpOh0K9CZ8cFYpnh-VbxVZ1JUDgf9JnTQMTNxL3zs526oKZbBrxzRsbUqN95Mdvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/4599" target="_blank">📅 17:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4598">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده! فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن. در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4598" target="_blank">📅 16:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4597">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SEvPjtdULvf9EWc4MrSuYO70Qgk60Kwk5hRetaqSnQfloeFOPVQY6FJSiX7X_TgGJ49MuZ6oD0Y1jGj38Q40IjrkHqibNHKCRP8EF94CA1pSfhjMe5Nxe9u1vZNorr4ASKrlfOf0pvDQXBfSoxKSXlnQdbFyQh95fKFUd_VY8GEfkRriyF8iq1GpuZIF2t0lhlqznzzXECs4pY9JdoY2jez6yZe1s-ze6kSGVkIP_wOMwHUAnog9s6X-C1_ttfq0FhjkSxFDe0aZWtm4S1ojGqvcZ1t7OsmFy90AinmYTXTvbrCh2s8OHuCievW1V7Zu4s9cAyvSC8tF28GLYul2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4597" target="_blank">📅 15:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4596">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEAX1TuZuqg9a2GBmpKm7zGp8KMlGMB2Y_30fKg8j-f6uXrC69XURXl4UIfqBnUMCJFlHqn1HnYt2aCkD6e6szABhJ0nNGOB30pD7AxSxwPFxYAaQwyOozGQ8kxqm9sr6SRkLq3tJMSqyahB_Ha1w5DTrCouq41hZjf4mdot7M4K1IDXhNXJsIqqgPzBzqEhOnL5n1GMWR-uK3rerZt-ZUYz8x4rzxarxvft_eCD9p1LY6oMd62YhC8hZqPXuE2sz_XSJsVsIPta2ddyWF4bFYyw4rrKZDL33A3661sJi1TDlmwjjAuTcZbAOlMNlUXAejFhXrtbgsnAkPRm5Uz69w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه شما هم با نمایش متن‌های فارسی در Claude مشکل دارید، ریک سانچز راه‌حلش رو براتون آماده کرده!
فعلاً این ابزار برای macOS منتشر شده و کاربران ویندوز باید کمی منتظر نسخه‌ی مخصوص ویندوز بمونن.
در طراحی این پروژه، به یاد زنده‌یاد صابر راستی‌کردار، خالق فونت وزیرمتن، از همین فونت استفاده شده است.
کافیه لینک زیر رو به Claude بدید و ازش بخواید نصبش کنه؛ بقیه‌ی کارها رو خودش انجام می‌ده:
https://github.com/m4tinbeigi-official/claude-rtl-patcher
به همین سادگی و خوشمزگی!
😄</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4596" target="_blank">📅 14:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4595">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VgDzfWseADKUjJ7Rm41ufGeDAFNv2KCh9yILZqScFDfpsKp8wgu3BnBOQBwg16Zb5anAnkBJZiyQAbtb8XxTtc9lh3c-GdT_DIE7d77GUugfDQ9LISdp4E28rYrc17xKNW1NKPlQiMSJg2_Vqk7rGqAQ1zPeuBk0NAplzbvdxGlltypab3ASDc5bc-FkXUSy1wQmYIKzh7ry4uf8sGy2rj3PV8kMc78gfLMS_wpfv8gbJSe5ndmwbA6v34btrhO40FHprQGurDs7Vl0xKqlVKbVsFdU1a-kKclTqmHqapA6wg5JDICVu8ah4y8uZ-qWyTmmY39Szch46Sb9DSy8FnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
@whitedns</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4595" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-poll">
<h4>📊 دوستان پروتکل WireGuard واستون وصل میشه؟</h4>
<ul>
<li>✓ 1- وصل میشه توی Aether، اما پینگ نمیده توی V2ray یا تلگرام🚫</li>
<li>✓ 2- کلا توی Aether هم وصل نمیشه🚫</li>
<li>✓ 3- وصل میشه، اوکی هم کار میکنه✅</li>
<li>✓ 4- دیدن نتایج(حال نداشتم تا الان aether رو ران کنم)🤡</li>
</ul>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد(با پشتیبانی از MacOS و Linux)  توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.  تغییرات…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4591" target="_blank">📅 01:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vxEA0DoExPQTVPTLwJ86ttuAqHl6HW1Cco18NtSO9SVLDNsKD85zrddfjXGhuwYtsprcEdVLQHVW26gc5r91qjDrBQxA_ENVVvSKn0BuAm_6XXtqlyeRsKvE32nXIbEXjzCHYNkmL-R4yL_C6Qr6m-kPsh5GJy0rAgvs90bTnRBC2HD1MMQJHDHCrSslEL7sHHJ8-clefZt4BZpq4T-zNv69n4VSeQCjiOjrsJDBetqU5oTeE4R6iLZOh9MU-UN8N833Os3iPzZ6RmFZA9hjXSoR-28okQUGxJ77nZIooDM0obtagCBjdYzaMzFe02s9XnUbNLXrBS1XvNBH8jChpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.5.0 منتشر شد
(با پشتیبانی از MacOS و Linux)
توی این ورژن، هسته (Core) برنامه رو به آخرین نسخه یعنی v1.3.0 ارتقا دادم. که توی این نسخه تمرکز روی پایدار کردن اتصال و اسکنر بوده. یه سری ویژگی کاربردی هم به رابط کاربری اضافه شده.
تغییرات اصلی این نسخه:
1-
اسکنر قدرتمند Ironclad:
بقیه حالت‌های اسکن فقط چک می‌کردن که آیا Gateway پینگ می‌ده یا نه. اما Ironclad یه تونل کامل و واقعی می‌سازه و یه درخواست HTTP ازش رد می‌کنه تا صددرصد مطمئن بشه که کار می‌کنه. یکم کندتره، اما قطعی‌ترین حالت ممکنه
2-
اتصال مجدد (Reconnect) هوشمندتر:
قبلاً اگه اتصالتون قطع می‌شد، Aether می‌رفت از صفر کل آی‌پی‌ها رو اسکن می‌کرد (که تو حالت‌های سنگین ممکنه چند دقیقه طول بکشه). الان اول همون آی‌پی‌ای که تا دو ثانیه پیش کار می‌کرد رو دوباره چک می‌کنه؛ اگه واقعاً مرده بود تازه می‌ره سراغ اسکن کامل
3-
اضافه شدن بخش Obfuscation:
این قابلیت دستتون رو باز می‌ذاره تا شدت مخفی کردنِ هندشیک از سیستم‌های فیلترینگ (DPI) رو تنظیم کنید. پروفایل‌هاش با توجه به پروتکلی که انتخاب می‌کنید (MASQUE یا Wireguard) متفاوته. اگه دیدید رو حالت دیفالت وصل نمی‌شه، درجه‌ش رو ببرید بالا
4-
تغییر پورت و Bind Address:
الان می‌تونید پورت SOCKS5 رو به دلخواه تغییر بدید یا اینکه روی آی‌پی
0.0.0.0
ست کنید تا پروکسی رو به کل شبکه‌ی لوکال (مثلاً موبایل‌ها یا تلویزیون تو خونه) Share کنید. اون باگ کلافه‌کننده‌ی پروتکل UDP هم بالاخره تو هسته فیکس شده و الان بدون مشکل توی شبکه‌ی لوکال کار می‌کنه.
5-
پشتیبانی کامل از مک و لینوکس:
این اولین نسخه‌ایه که کاملاً مولتی‌پلتفرمه! فایل‌های نصب ویندوز (exe و msi)، فایل‌های مخصوص مک (برای چیپ‌های اینتل و اپل سیلیکون به صورت جداگانه)، و انواع پکیج‌های لینوکس (deb، rpm و AppImage) رو براتون گذاشتم
6-
رفتن به System Tray:
گزینه‌ای اضافه شده که وقتی برنامه رو می‌بندید، به جای خروج کامل، بره تو تسک‌بار پایین ویندوز و همونجا تو پس‌زمینه کارشو بکنه
ممنون از
@rqzbeh
عزیز بابت مشارکت‌هاش تو این آپدیت؛ و ممنون از
@CluvexStudio
عزیز بابت زحماتش روی هسته‌ی برنامه
لینک گیت‌هاب برای دانلود نسخه‌های مختلف:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.5.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4590" target="_blank">📅 00:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بعد میگن شبکه‌های اجتماعی چطوری پول در میارن
"Data"</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4589" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4588" target="_blank">📅 00:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اون روز داشتم از claude راجب s3 storage سؤال می‌کردم و کمی داشتم دانشم رو بالاتر میبردم، صرفا سوال جواب بود
فرداش فید گوگلم پر شده بود از خرید فضای ذخیره سازی s3 و کمترین قیمت s3 و...</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4587" target="_blank">📅 00:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یه مقدار برای همین طول کشید. اما خودم هم بیلد رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4586" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">در حال آپلود</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4585" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjBHfGLzVPrdjF2AuNRUMtQmmPU7p2cB8TChx72ufXKIk7BwwxOU3_t0chac4NbmLl1I-gnwQLr5gH1v6gMFpg9oTZsTJnio3ppWci1GvJ0dIbrRK9XC7T8Vec44yqZL4vgvUWSZCKSdDtp6toMYdhXBSq4MKMAo9Ae-fps7mJi6cl0paXIFQc8IKkpRD9O15ttO1romeixKI3D4KIDursLcQlwgtkqTEOM4WrDiMq4vQhSFNijTCdQABYpyjxjX4D2A_RnUuMKwPvn2jSnbJ3x9kBVo7Z1U41xuAyvywVeeMQatf6XgGFBXGeGz0qHQR-kYO30N8MKdUBkyc9U4OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی تغییرات جدید به GUI اضافه میشه
🙏</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4584" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4583" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هکرها زدن کل دیتابیس ثبت اسناد و املاک رومانی رو پاک کردن:)))
یه هکر الجزایری به اسم ByteToBreach (که اسم واقعیش زکریا محجوب از شهر وهران الجزایره و قبلاً هم پورتال دولت سوئد رو هک کرده بود) با استفاده از اطلاعات ورودِ یه کارمند، وارد شبکه‌ی سازمان کاداستر (ثبت اسناد و املاک) کشور رومانی می‌شه.
هکر اول کل سیستم‌ها رو مپ می‌کنه و اسناد و اطلاعات کارمندا رو می‌دزده، بعد سعی می‌کنه ازشون باج بگیره. وقتی دولت رومانی باج رو نمی‌ده، هکر کل دیتابیس ثبت اسناد کشور رومانی به اضافه‌ی بکاپ‌های آنلاینشون رو پاک می‌کنه
😂
(یعنی عملاً کلاً نابودشون کرده).
این کار باعث شد کل بازار املاک و مستغلات رومانی فلج بشه و دفاتر اسناد رسمی نتونن هیچ سندی رو ثبت کنن. هکر هم دیتای دزدیده شده رو تو یه فروم دارک‌وب گذاشته برای فروش
👌
خب باج رو بهش میدادین دیگه ای بابا
مقامات رومانی گفتن که دارن کل شبکه رو از صفر می‌سازن. با اینکه هکر ادعا کرده تمام بکاپ‌ها رو پاک کرده، اما خبرنگار ریسکی‌بیزنس (Risky Biz) می‌گه به احتمال زیاد اونا یه نسخه‌ی بکاپ آفلاین (Cold Backup) داشتن، چون اگر اصلاً هیچ بکاپ آفلاینی نداشتن، فاجعه‌ای تو رومانی رخ خواهد داد که تا ماه‌ها نمی‌تونن ثابت کنن کی صاحب کدوم زمین و خونه‌ست! یا اینکه باید برن از دارک وب، اطلاعات خودشونو بخرن
😂
😂
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4582" target="_blank">📅 21:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cXMwv5Jf4LcwjJLjRk_Q_8dmd9pnHbXwDF_-B3OX39V6LF7HG3oMcP1zPnxy-Xjn9cyyCbZKR-bbo-0hsju24siS21gJAMlH9tzAjQHPAeqM4y8oLqbPzxUqHw5U-IdgeAgB0i4rKCcuhlCZu9qwP3PjZfou8g5IxjpzABxYpNN0DYylc5P87eQcfK7vvE1YtVwuBWFltfrXg0DqxFZR6xrlqFeWamLjG3yi7_wI34xmLM7gN5mho_CdTw8s7NiK-FShScBRLS24mzuzkaMhDRGf3fjma2lLkwl_gtaoOLz06RvkDGakBJP71TFD7_q4IVJzS_SexZj0ffwg9ZVndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4581" target="_blank">📅 14:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:  https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0  توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:  یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4580" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.3.0:
https://github.com/CluvexStudio/Aether/releases/tag/v1.3.0
توی این ورژن بیشتر روی اسکنر و پایداری اتصال کار کردم:
یه حالت اسکن جدید اضافه کردم به اسم Ironclad توی این حالت برای هر IP کاندید Aether یه تونل واقعی و کامل میسازه و یه درخواست HTTP واقعی از توش رد میکنه نه فقط یه پینگ ساده. :))
یعنی اگه یه Gateway رو با این حالت انتخاب کنه مطمئنید که واقعا کار میکنه نه فقط جواب پینگ داده. کندتر از بقیه حالت‌هاست چون کار بیشتری میکنه... ولی از نظر قطعیت بهترین گزینه‌ست و همینو پیشنهاد میکنم.
- ریکانکت سریع‌ تر بعد قطعی قبلا اگه تونل قطع میشد (چه MASQUE چه WireGuard) Aether مستقیم میرفت سراغ یه اسکن کامل از صفر که توی حالت‌های سنگین‌ تر مثل Ironclad میتونست چند دقیقه طول بکشه. الان اول همون Gateway قبلی که کار میکرد رو یه تست سریع میگیره
و فقط اگه اون دیگه جواب نداد میره سراغ اسکن کامل.
فیکس UDP روی SOCKS5 وقتی پروکسی رو روی شبکه لوکال باز میکردید اگه AETHER_SOCKS رو روی یه آی‌پی غیر از
127.0.0.1
ست میکردید تا از دستگاه‌های دیگه توی شبکه هم بشه وصل شد
بخش TCP درست کار میکرد ولی UDP هیچ‌ وقت رد نمیشد
فیکس کردم. (گزارش یکی بود issue )
پشتیبانی از OpenWrt یه بیلد استاتیک جدید اضافه شد (aether-linux-armv7-musl.tar.gz) که مخصوص روتر های OpenWrt و سیستم‌های مبتنی بر musl هست.
(یکم مشکل بود این قسمت، کلی وقت گرفت، یکم دیر شد سر این بود)
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4579" target="_blank">📅 09:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گویا شرکت Moonshot ، توسعه‌دهنده‌ی مدل چینی Kimi 3 انقدر به خاطر تهاجم مردم فشار اومده به سرورهاش که کلا فروش اشتراک‌های جدید رو متوقف کرده:))
همینطور اونایی که قبلاً اشتراک ۲۰ دلاری رو خریدن هم شاکین. چون مدل سنگینه، توکن‌ها خیلی سریع‌تر از مدل‌های قبلی مصرف می‌شه و کاربرها می‌گن بودجه‌ی هفتگیشون تو دو روز اول تموم می‌شه. (این رو با مدل قبلی یعنی K2.5 که خیلی به‌صرفه‌تر بود مقایسه می‌کنن).
توی فروم‌های تخصصی (مثل Hacker News) بحثِ جالبی راه افتاده؛ خیلیا می‌گن دقیقاً به خاطر همین مشکلاته که ما باید به سمت مدل‌های اوپن‌سورس و اجرا روی سخت‌افزارهای خودمون بریم، وگرنه حتی بزرگ‌ترین استارتاپ‌ها هم یه جایی زیر بارِ ترافیکِ مدل‌های هوش مصنوعی زانو می‌زنن.
هرچند توی ایران متاسفانه نمیتونیم زیاد به همچین چیزای گل و بلبلی که خارجیا میگن واقع‌بینانه نگاه کنیم</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4578" target="_blank">📅 02:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هرچقدر بگم هرمس برای تحقیق و پیدا کردن گسترده‌ی یه چیزی عالیه کم گفتم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4577" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبر فوری :  ‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید دو تا باگ SQL Injection و RCE داره  نسخه های اصلاح شده: WordPress 6.8 → 6.8.6 یا جدیدتر WordPress 6.9 → 6.9.5 یا جدیدتر WordPress 7.0 → 7.0.2 یا جدیدتر    @Linuxor ~ seramo_ir</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4576" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خبر فوری :
‏اگر سایت وردپرسی دارید حتما هسته وردپرس رو آپدیت کنید
دو تا باگ SQL Injection و RCE داره
نسخه های اصلاح شده:
WordPress 6.8 → 6.8.6 یا جدیدتر
WordPress 6.9 → 6.9.5 یا جدیدتر
WordPress 7.0 → 7.0.2 یا جدیدتر
@Linuxor
~ seramo_ir</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4575" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSR9P5L19pPtK1-CmZRAax_67-9V9vSiigDYIBhR_sW8SPyBB3b5uJ2scxcBw-GINcihfmn1CuPbXVMPG295BWKVY_LT8jk8_Se17408T_JL3ECalIRQMCOcuCDF9Rsa9QFKCChsCKflhrnBeMVV0V6L_ZDglR4IPYykKtFNmvOXB74B5jtl6EQz-J4M3C8hK5pHCuCDFpqQqnY0A4HXHa3g1_MVAecE54F9LhXglOqrXgK8_9lydASrXWVPd9swlNtnQLfzdMZryqDAaH4aH5iXNQjx0q6AJBWEqVXNWwHq-q_5efdkMe2UVPj9sGn7lJnSaBJLglDwqCaTFkTfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌های متخصص امنیت (که توی حوزه SOC و Red Team فعاله) یه سایت و کامیونیتی زده به اسم VulnCity (شهر آسیب‌پذیری‌ها). که یه مرجع جامع و دورهمی برای بچه‌های امنیته.
1- مقالات و آموزش‌های دست‌اول: مؤسس سایت هر چیزی که توی پروژه‌های واقعی (مثل Red Teaming) یاد می‌گیره رو به‌صورت مقاله می‌ذاره اونجا.
2- شبکه‌سازی: بچه‌های امنیت می‌تونن با هم چت کنن، پروفایل همدیگه رو ببینن و یه تیم بسازن.
3- بخش Vulndark: یه قسمت باحال داره که اخبار مارکت‌های فعال دارک‌وب، فعالیت گروه‌های هکری و خبر لو رفتن دیتابیس‌ها رو پوشش می‌ده.
آدرس سایت:
🔗
https://vulncity.com
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4574" target="_blank">📅 20:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرق H3 و H2 برای من روی یه اینترنت، 18 و 2 مگابیته
یعنی H2 سرعتش پایینتره
همینطور وایرگارد و gool هم برای من همون سرعت H3 رو دارن</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4573" target="_blank">📅 20:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من حس میکنم به قدرت gool پی نبردید
یه تست بکنید جداً</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4572" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 حالا دوستان MASQUEـی، بهم بگید کدومش بهتره توی آپلود/دانلود؟</h4>
<ul>
<li>✓ http/3</li>
<li>✓ http/2</li>
<li>✓ مسکی نیستم دیدن نتایج👺</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4571" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 توی Aether بیشتر روی کدوم پروتکل بودید و براتون بهتر بوده تا الان؟</h4>
<ul>
<li>✓ 1- MASQUE</li>
<li>✓ 2- Wireguard</li>
<li>✓ 3- Gool(warp-in-warp)</li>
<li>✓ استفاده نکردم</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4569" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر دنبال یه آرشیو کامل از یاد گرفتن ساخت کانفیگ با سرور شخصی و تمام روش های
#اینترنت
آزاد هستید از مبتدی تا حرفه ای میتونید از این آرشیو کامل که یکی از بچها زحمت کشیده و آرشیو بسیار کاملیه استفاده کنید.
لینک سایت:
👇
(باز نشد با فیلتر برید)
filtershekan.sbs
خلاصه:این سایت برای تمام آموزش
#امنیت
ساخت
#کانفیگ
و تمام روش هایی که شما رو میتونه با کمترین هزینه و رایگان وصل کنه رو گذاشته.
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4568" target="_blank">📅 13:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">اطلاعیه:
سطح پهنای باند و کیفیت اتصال اینترنت در تمامی اپراتورها و دیتاسنترها به‌طور قابل‌توجهی کاهش یافته است. بررسی‌ها نشان می‌دهد ظرفیت پهنای باند نسبت به روز گذشته کاهش محسوسی داشته است.
همچنین برخی رسانه‌ها از اختلال یا قطعی در خطوط انتقال پهنای باند و زیرساخت شبکه در برخی مناطق کشور، به دلیل حملات منتسب به آمریکا، خبر داده‌اند. :))</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4567" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آپلود عملا مرده</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4566" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F0McFU4K07XUF6Qtfp4xv-FhaIy470h5ZdMtp5G6ULBK8t5MuvS0DTrklI47DmvrwB40ae490dhfGagMusyeCQfwTKcNgjzC_bI2I5yVcaw2TIXawFSxsbEpztWylT7V16hX0KKwybRC4KpngYfaYsXrhBzIDwj1tOLlZAMXrYoKnMTDG6p1tejcOThyE4FGr8gv-EcPvP3oGUfPCaq9OsOnWqGW8AyHxqvehOO8ruxk5_DDP9iWBrpFXFWFtQfsqEzJOASh2DAlXPtRe0-cqTrth6WXUX2CxZkHoavNnjIlQjHom1uEnjrbDv7G71K_rMCHG4n9QiKp5SFQeHWp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کپچایی بود خدایی حالم بد شد
کم کم ما ربات تشخیص داده میشیم،‌هوش مصنوعی انسان</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/4565" target="_blank">📅 22:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=Vdy3ckGlwEOv3Gped3XDiT_vFm7cIySsbmjbDc1Ur8FzZSe-AMhw1hcE_P-VYUWhsNAE3xzupr5-LCz2T66Fsc3YiHFCEeuwfwG-cvp6tDlDQ0UZ0ni5dJ-5YF4YCAPW_gr0irldz_IkDCOmbGSKKUGXrEIrO63XgzE_X41U1H-vCTwF31ehaMSUZk0ApJJcTTTJgqI1IOWt-XWkAV6_C2RvVuKlECfA3lXMV5gfKtUa1y2VjdaBEg4rZxBbCkyW9-AxBhAwjLkRJ8__akZibSg-N38hxzn-Ttfd0iPzhz5AUt4d4d17DiN26X1nVUuQsAES32nDhcULwOBSk_jZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d80c0238b.webm?token=Vdy3ckGlwEOv3Gped3XDiT_vFm7cIySsbmjbDc1Ur8FzZSe-AMhw1hcE_P-VYUWhsNAE3xzupr5-LCz2T66Fsc3YiHFCEeuwfwG-cvp6tDlDQ0UZ0ni5dJ-5YF4YCAPW_gr0irldz_IkDCOmbGSKKUGXrEIrO63XgzE_X41U1H-vCTwF31ehaMSUZk0ApJJcTTTJgqI1IOWt-XWkAV6_C2RvVuKlECfA3lXMV5gfKtUa1y2VjdaBEg4rZxBbCkyW9-AxBhAwjLkRJ8__akZibSg-N38hxzn-Ttfd0iPzhz5AUt4d4d17DiN26X1nVUuQsAES32nDhcULwOBSk_jZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز : ترامپ از کشته شدن سربازانش بسیار عصبانی و خمشگین شده است.</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4564" target="_blank">📅 22:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سرعت نت من به شدت پایین اومده. از 30 مگابیت به 2 مگابیت عملا. با و بدون وی پی ان هم فرقی نمیکنه
نمیدونم چه گندی دارن می‌زنن باز</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4563" target="_blank">📅 21:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رفقا یکی از دوستان من به اسم محمد، خارج از کشور هستش و برنامه‌نویس Back-end با بیش از ۵ سال سابقه کار هستش و روی پروژه‌های مختلفی از جمله سیستم‌های رزرو پرواز، پلتفرم VOD، مارکت‌پلیس، سیستم‌های پرداخت، احراز هویت، پنل‌های مدیریتی و معماری میکروسرویس کار کرده.
تکنولوژی‌هایی که بهشون مسلط هست:
Node.js • TypeScript • PostgreSQL • Redis • Docker • RabbitMQ • Microservices • Prisma • REST API
هم برای همکاری Remote میتونه اقدام کنه، و هم اگر فرصت مناسبی باشه، برای Relocation مشکلی نداره
حیفه که از چنین استعدادی استفاده نشه
😁
لینکدینش:
https://www.linkedin.com/in/mr-ln
آیدی تلگرامش:
@MRLN2001</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4562" target="_blank">📅 20:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این وسط مدل Claude Fable 5 موندگار شد.
آنتروپیک اعلام کرده که از ۲۰ جولای، مدل Claude Fable 5 رو توی همه‌ی پلن‌های Max و Team Premium (با ۵۰ درصد محدودیت‌ها) نگه می‌داره. کاربرای Pro و Team Standard هم می‌تونن با استفاده از Credit بهش دسترسی داشته باشن و یک اعتبار ۱۰۰ دلاری هم دریافت می‌کنن. به نظر میاد فشار رقابت سنگین با GPT-5.6 Sol و Kimi 3 باعث شده آنتروپیک از برنامه‌ی قبلیش برای حذف کردن Fable 5 از پلن‌های اشتراکی عقب‌نشینی کنه که خب قابل پیش‌بینی بود
🤤</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4561" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مدل Kimi 3 اومده با context یک میلیونی و به نظر خیلی خفن میاد
هرچند همیشه گفتم به بنچمارک‌ها اعتباری نیست، باید در عمل دید که چیکار میکنه</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4560" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یکی از بچه‌ها به اسم ارشیای عزیز این ایمیل رو بهم داد، برای خرید سرور:
من از hostvds خریدم. ۹۹ سنت هزینشه، یه ۴۹ سنت خرج می‌کنی ترافیکش‌ نامحدود میشه. هزینه رو یه دفعه کم نمیکنه ساعتی کسر میشه. اگه یه دفعه آیپی فیلتر بود میتونی سرور رو حذف کنی یدونه دیگه دیپلوی کنی.
پرداخت کریپتویی داره
با ایران مشکلی نداره
۲ ماهه باهاش مستر dns و پنل ثنایی فعال کردم.
پایداری و سرعتش خیلی خفن نیست ولی بدک هم نیست.</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4559" target="_blank">📅 18:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbidcdOr1aKZf-9QKQSnaSM6IMp2S0sckZMSBCklf_8nII9RWj4v9b2jScS4q8N9hQEW2dyR0uMvDUQPSfJ-8GEE66q38_yspHbCyWEg8lOTLJZzJ9oZgpBLr2h5oBEZNhnkN1KSDVWO6WMYOMeVig0ZfpgiNd1nKFaZy_QGAm5kyS2zUtKRZERSdtrFvwEp3mwbfvPpnsj9x7EUCFBsj-nyuJIT59GVjp38RZxoGwdk08Np2auattoCYCApqY--b7ieILMhh20wRURo1CrFF0qadIEf845LTDZxFxtxQUJXtKLz2zz2CVP96goxHg6czqpuucioC8s82XGETja_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان گویا yotta src روی سرورهایی که برای masterdns استفاده میشن، ابیوز میزنه و سرور رو بدون اطلاع قبلی می‌بنده. لطفا دیگه به این قصد ازش خرید نکنید تا اطلاع ثانوی
و میگردم سایت اوکی پیدا میکنم واسه‌ی خرید سرور با کریپتو باز هم</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/4558" target="_blank">📅 12:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">پاول دورف و ایلان ماسک هردو گفته بودن اگه دانشجو هستید بهترین چیزی که میتونید یاد بگیرید ریاضی و فیزیک هستش
راستم میگن اما حرفشون یه اشکالی داره، یادگیری ریاضی فیزیک برای پولدارا و بی دغدغه هاست، برای مثال به خصوص توی ایران یادگیری ریاضی و فیزیک درامد خوبی نداره و شمارو اصلا وارد Positive Feedback Loop نمیکنه که توش پیشرفت کنید، ولی واقعا راست میگن من خودم اگر هیچ دغدغه مالی نداشتم تا آخر عمر ریاضی و فیزیک یاد می‌گرفتم چون جز بنیادی و مهم ترین ابزار های فکری بشر هستن!
@Linuxor</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4557" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان عزیز لطفا مراقب خودتون باشید و توی جاده و نزدیک پل‌ها تردد نکنید اصلا
خیلی خطرناکه این روزا</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/4556" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u-kbWPGsW-5SPLUdSE0y6zY0rUuatTQhme4goJ1c_yLXkItHPJkkUXx8sV9zKh1-8pfXKmo0kxMqDkFZSoGqcFoQfp4X7bh_PKHgQaPIjUF1Tq9w1e7hqEz3NKRJ_FIbP9RXOEsJA_ojSgYnZjO5tYHpFAbGf1h5yDDmtkUcorbXX49IurQa-eSVa3vuld2UqujWVtk4_BW5guPONTIZig6OtY8c5LwZhrzWZNTtLdZYeYsZYo9h-8dnW3SKwl8vngkR0HbNeYpxIxf89CNDeFxTqdRe_lcVVJXt7_awlZbGHrno0mRlG4i26irlCGb2USV6kI2uNBjx5O_PgJT5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که تا الان براشون کانکت نشده بود، یا کار نمیکرد، حدسم اینه به احتمال 90 درصد واستون کار کنه با تغییر پروتکل ارتباطی Masque به http2. من تا الان Masque روی نت مخابرات واسم کار نمیکرد، اما با این ورژن جدید دارم همین پیام رو میذارم با MASQUE+Turbo+Ipv4+Http2</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/4555" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید! نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن 1.2.0 ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک: قبل از این، بخش Validation ابزار با پینگ…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4554" target="_blank">📅 02:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4552">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/upzX0kAJjc-PuTQfKvUMJ9Q89cs9vH74xjXmz-010mKOMPBd6qq5bAA_7ECr6sH3xK3gcrRHTsmpLwt2K6r_wA-1zsEixOLBEf3rbii21WcGOzMHjeUgnrqkMsSQ9HSFozLtOD7qN1HTN-kNnzgRC6usdIGahWXd6tKPo3WJHMHvM-DI7f0iVZ5T9hGU_bJ2R51N_DMOKL8XUWKQMaowK0DPQWiDVw5syNxXY9r0tOsUgiFr-BgPlnDM0m62C89zCF3eeUjYzQrPslNTyRPvDfRyiUqiL81I29XdpPryQQULGUr7J6IuXlMtoPBqN1_ZFh4bC7ifHGmcQMnJKeZWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DpErzkBwU8halTdUjSbslAMkCdlBtYIHWRFpI37gpCbBxtJdQfIz4_PVRrp6XCw4GbfSz0BPoUBUHMF2ACjcxXnoiZ-BJSwp2HvwMWcGxF2qf2dpMTm9j7IruU-Tmefa4I5hJ3uRAv-OT2BuNxrR0EZGkPeGmes4VEO1t38--7SQhHzOzSPxhMfP4prsqeZmlIHpcnoaVXhNefob2ej8yTPgU8m5wHq7z4Q_Y1BL3-yo5ESO_9yC-ONNj0K1yI7VtG2ZvyXR1xPzAX1OncaIQyGh5f88M6fOe70shC9MLgG5BIf591UcjWJtW8zm3rs6XuwK9iguqgt2K2eu_zZFBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/4552" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4551">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به زودی به GUI هم اضافه‌ش میکنم</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4551" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4550">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether منتشر شد.
v1.2.0
چند تا مشکلی که گزارش کرده بودید توی این نسخه برطرف شده:
- مشکل اینکه بعضی وقتا تونل ظاهرا وصل میشد ولی هیچ سایتی باز نمیشد فیکس شد.
یعنی SOCKS5 فقط وقتی باز میشه که مطمئن باشه
تونل واقعا کار میکنه... :))
مشکل دیر reconnect شدن روی MASQUE HTTP/2 هم برطرف شد.
الان براش HTTP/2 PING اضافه کردم و خیلی سریع ‌تر تشخیص میده.
اسکنر MASQUE هم بهتر شده
چند تا رنج IP رسمی Cloudflare که برای MASQUE استفاده میشن به اسکنر اضافه کردم، همراه با پورت‌ های بیشتر
در نتیجه شانس پیدا کردن Gateway سالم بیشتر شده.
موقع اجرای MASQUE هم دیگه راحت میتونید بین
HTTP/3
و
HTTP/2
انتخاب کنید.
کنار هر گزینه هم یه توضیح کوتاه گذاشتم که بدونید کدوم برای چه شرایطی بهتره.
به طور خلاصه:
HTTP/3
برای شبکه‌های عادی و سالم
HTTP/2
برای وقتی که UDP یا QUIC محدود شده
لینک پروژه هسته:
https://github.com/CluvexStudio/Aether
اگه خوشتون اومد از این پروژه، میتونید Star بدید بهم :))
Readme
هم بخونید حتما!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4550" target="_blank">📅 22:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4549">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
فیلترنت به طرز همیشگی افتضاحه و عملا سرعت آپلود نداریم داخل هر پنلی چه کلودفلر چه سرور شخصی با ی راه وضعیت بهتر کنید.
دی ان اس گوگل اختلال زیاد داره داخل هر اپلیکیشن وارد کردید کانفیگ رو دنبال گزینه Dns بگردید و هر مقدار بود بزارید روی این مقدار مشکل حل میشه:
9.9.9.9
9.9.9.12
149.112.112.112
9.9.9.9
💡
داخل پنل هم دارید تغییر بدید این واسه همه اپرارتور ها جوابه بهتر از کلودفلر و گوگل هست تو این شرایط.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4549" target="_blank">📅 21:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4548">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4548" target="_blank">📅 21:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4547">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مدل Fable 5 - بودجه 100$</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4547" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 100 دلار</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4546" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مدل Fable 5 - بودجه 25$</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4545" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مدل GPT 5.6 Sol - بودجه 25 دلار</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4544" target="_blank">📅 20:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه آزمایش خیلی جالب توی وبلاگ TryAI انجام شده. اومدن یه محیط ایزوله ساختن و به دو تا از قوی‌ترین مدل‌های هوش مصنوعی یعنی Claude Fable 5 و GPT-5.6 Sol، یه آهنگ (Uptown Funk از برونو مارس)، یه متن از لیریکس آهنگ، یه سری ابزار (مثل سرچ وب، دسترسی به APIهای تولید ویدیو و ابزار تدوین ffmpeg) و یه بودجه مشخص دادن.
هدف این بود که مدل‌ها رو به حال خودشون رها کنن تا صفر تا صد یه موزیک ویدیو رو خودشون کارگردانی و تدوین کنن! هر مدل با دو تا بودجه‌ی ۲۵ دلاری و ۱۰۰ دلاری تست شد. نتایج و درس‌هایی که از این آزمایش گرفتن خیلی جالبه:
1- آزادی عمل تو انتخاب ابزار: هر مدل روش متفاوتی رو پیش گرفت. مثلاً کلاد تو هر دو حالت فقط رفت سراغ تبدیل «متن به ویدیو» (Text-to-Video). اما مدل Sol تو بودجه‌ی ۲۵ دلاری، اول عکس ساخت و بعد عکس‌ها رو متحرک کرد (Image-to-Video) و تو بودجه‌ی ۱۰۰ دلاری همزمان از ۳ تا مدل ویدیویی مختلف برای ساختن شات‌هاش استفاده کرد.
2- درک سطحی از شعر: هوش مصنوعی لیریکس رو خیلی لغوی و تحت‌الفظی می‌فهمه! مثلاً وقتی خواننده می‌خونه "Make a dragon wanna retire" (می‌خوام اژدها رو بازنشسته کنم)، هوش مصنوعی دقیقاً یه اژدهای واقعی میاره تو تصویر!
😂
3- مشکل در ریتم و تدوین: با اینکه مدل‌ها با ابزار ffmpeg بیت (Beat) آهنگ رو پیدا کردن و کات‌ها رو روی ضرب آهنگ زدن، اما حرکات داخل ویدیو (مثل رقصیدن یا حرکت دوربین) اصلاً با تمپوی آهنگ هم‌خونی نداشت و یه‌کم تو ذوق می‌زد.
4- کم‌کاری توی بازبینی: یکی از نقاط ضعف بزرگ مدل‌ها این بود که اصلاً خروجی کار خودشون رو نقد و اصلاح نمی‌کردن. یعنی وقتی یه شات رو تولید می‌کردن، همون رو می‌چسبوندن تو ویدیو و دیگه برنمی‌گشتن که افکت بهتری روش بندازن یا اگه بی‌کیفیت بود حذفش کنن. (به قول معروف چشم‌بسته تحویل می‌دادن).
5- بودجه‌ی اضافی کمکی نکرد: دادن ۱۰۰ دلار بودجه واقعاً زیاد بود! هیچ‌کدوم از مدل‌ها نتونستن از تمام این ظرفیت استفاده کنن (نهایتاً حول‌وحوش ۳۶ تا ۴۸ دلار خرج کردن). می‌تونستن با این پول کلی عکس ثابت از کاراکترها بسازن تا مشکل تغییر قیافه‌ها تو طول ویدیو حل بشه، ولی هیچ‌کدوم به این راهکار فکر نکردن.
6- هزینه‌های پنهان: با اینکه بودجه تولید ویدیو محدود بود، اما هزینه‌ی توکن‌های خود LLM برای کلاد به شدت گرون‌تر دراومد (حدود ۱۷ تا ۲۵ دلار فقط پول توکن)، در حالی که این هزینه برای مدل OpenAI زیر ۴ دلار بود. با این حال تیم سازنده به صورت سلیقه‌ای، خروجی ۱۰۰ دلاریِ کلاد رو بیشتر از بقیه پسندیدن.
حرف آخر:
هیچ‌کدوم از موزیک ویدیوهای نهایی شاهکار از آب درنیومدن و هنوز شکافِ بزرگی تو انسجام داستان، ثبات چهره‌ی کاراکترها و خلاقیت تدوین وجود داره. اما اینکه یه هوش مصنوعی خودش بره مدل ویدیویی انتخاب کنه، پرامپت بنویسه، ویدیو بسازه و با ابزارهای خط فرمان ادیتش کنه، یه کم ترسناک ولی باحاله!
لینک مقاله اصلی با ویدیوها:
https://www.tryai.dev/blog/ai-music-video-arena-claude-vs-gpt-5.6
سورس کد این پلتفرم (اگه می‌خواید خودتون تست کنید):
https://github.com/hershalb/music-video-arena
هر 4 تا ویدئوش رو آپلود می‌کنم ببینید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4543" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب گویا تیم Turso دارن روی نسخه جدیدی از PostgreSQL با زبان Rust کار می‌کنن و هدفشون اینه که چیزی شبیه به LLVM برای دیتابیس‌ها بسازن. این یه قدم جذاب برای امن‌تر و ماژولارتر کردن اکوسیستمش محسوب میشه در کل. منتها این بازنویسی همه‌چیز به Rust هم خودش موج/تب جالبیه
🤔
لینک کامل خبر:
https://turso.tech/blog/a-new-modern-version-of-postgres-in-rust</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4542" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مافیا بخوابه، شهروندا بیدار شین همه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4541" target="_blank">📅 09:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سرعت آپلود به شدت ضعیف شده اینجا</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4540" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4539" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4538">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4538" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4537">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4537" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4532" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4531" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4523">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4523" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4523" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4522">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OAqONc3Rdv_80ubfCpKSWASNnfyik7zu5gijBV0RYYY1B9OfC6bonLIC2bBcNhrdMWH0e_oWmmsJA83C0mm2fORsFkJq7A5aGaDwymY4gehTi_RaCI01JBf4eh5v_sYeMyByNW1St_GxaNgzMGrWoEcT_3yH0gkJzSys7r3itwriv1L89XkmskeRpKPnTsb3NJrueN2VFu6fHyY47kmhdH0LTzVwHuw8lUqITj-X49yAcsJJaM-oWc3EpGD5b6B7QRq97lfhR793h5OfLN6Mfq5TqIySrhNWwJbxKAjAByaHIkBs36rSnyihvzOHXgaXVebnKupjbJbeU60oinigqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4522" target="_blank">📅 01:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4521">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاید هم عاقل شدن
چه میدونم والا</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4521" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4520">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فکر کنم تا اسرائیل حمله نکرده نت رو قطع نمی‌کنن</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4520" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4519">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مرز "یادگیری" و "تنبلی" با LLM ها واقعا یه خط موی باریکه</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4519" target="_blank">📅 20:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4518">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خالق لینوکس: هوش مصنوعی یه ابزاره، هرکی دوست نداره جمع کنه بره!
🐧
یه بحث جنجالی توی لیست پستی توسعه‌دهندگان لینوکس بالا گرفته بود سر اینکه آیا باید از هوش مصنوعی (LLMها) برای بررسی کدها و کمک به Maintainerهای لینوکس استفاده بشه یا نه. بعضی‌ها خیلی سفت‌وسخت مخالف بودن و می‌گفتن کلاً نباید پای AI به هسته لینوکس باز بشه.
اما
لینوس توروالدز
(خالق لینوکس) همونطور که از شخصیت رک و بی‌اعصابش انتظار می‌رفت، وارد بحث شده و یه جواب به شدت قاطع داده.
خلاصه‌ی حرف‌های لینوس ایناست:
1-
لینوکس پروژه ضد هوش مصنوعی نیست:
لینوس صراحتاً گفته: "می‌دونم بعضی‌ها از هوش مصنوعی متنفرن، اما لینوکس قرار نیست یکی از اون پروژه‌های ضد AI باشه. اگه کسی با این قضیه مشکل داره، می‌تونه طبق قانونِ اوپن‌سورس پروژه‌مون رو Fork کنه یا کلاً از اینجا بره!"
2-
کسی که میگه AI به درد نمی‌خوره، اصلاً باهاش کار نکرده:
به گفته‌ی لینوس: "AI مثل بقیه ابزارهایی که داریم، صرفاً یه ابزاره. شاید تا یه سال پیش کاربردش واضح نبود، اما الان دیگه شکی توش نیست که مفیده. هرکسی که به مفید بودنش شک داره، کاملاً مشخصه که تا حالا ازش استفاده نکرده."
3-
به جای غر زدن، درستش کنیم:
لینوس قبول داره که هوش مصنوعی گاهی اوقات به خاطر پیدا کردن باگ‌های خجالت‌آور یا تولید کارهای اضافه، می‌تونه برای مدیران پروژه‌ها دردسرساز باشه. اما می‌گه راه‌حلش این نیست که "سرمون رو بکنیم تو برف و بگیم من چیزی نمی‌شنوم". راه‌حل اینه که یاد بگیریم چطور از این ابزارها برای «کمک» به تیم استفاده کنیم، نه اینکه کلاً حذفشون کنیم.
4-
انسان‌ها هم بی‌نقص نیستن:
لینوس یه تیکه‌ی سنگین هم انداخته: "بله، AI بی‌نقص نیست. ولی محض رضای خدا، هرکسی که به مشکلات AI اشاره می‌کنه، بهتره تو آینه به خودش هم نگاه کنه! چون هوش طبیعیِ انسان‌ها هم همیشه اونقدرها عالی و بی‌نقص نیست."
حرف آخر:
در نهایت لینوس آب پاکی رو ریخته رو دست همه و گفته لینوکس یه پروژه‌ی تکنولوژی‌محوره، نه یه کمپین مذهبی یا اجتماعی. ما اوپن‌سورس کار می‌کنیم چون نتیجه‌ش می‌شه تکنولوژی بهتر، و تصمیماتمون رو هم بر اساس ارزش‌های فنی می‌گیریم، نه از روی «ترس از ابزارهای جدید». به قول معروف: پیشرفت منتظر کسی نمی‌مونه!
لینک ایمیل اصلی لینوس توی لور:
https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4518" target="_blank">📅 18:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4517">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قبلا چندتا مقاله خونده بودم، اما تا با چشم خودم ندیدم قبولش نکردم.
واقعا AI ها، زبان TypeScript رو خیلی خیلی بهتر از مابقی زبان‌ها می‌فهمن</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4517" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4516">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build  داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4516" target="_blank">📅 16:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4515">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آیا هوش مصنوعی داره قدرت تفکر رو از ما می‌گیره؟
🏃‍♂
یه مقاله‌ی جالب توی وبلاگ ArtFish منتشر شد، درباره‌ی اینکه چطور داریم کم‌کم «فکر کردن» رو به هوش مصنوعی واگذار می‌کنیم. نویسنده‌ی مقاله خودش توی بخش توسعه‌ی Gemini کار می‌کنه، ولی یه سری دغدغه‌های به‌شدت درست و روانی مطرح کرده که خوندنش خالی از لطف نیست.
خلاصه‌ی بحث و چند تا نکته‌ی جذابی که گفته:
1-
از موتور جستجو تا ماشین فکر:
قبل از چت‌جی‌پی‌تی و جمنای و...، ما برای پیدا کردن جواب می‌رفتیم گوگل می‌کردیم، ولی همون سرچ کردن هم نیاز به «فکر» داشت. باید سوال رو می‌شکستیم، منابع رو می‌خوندیم و خودمون ترکیبشون می‌کردیم تا به جواب برسیم. اما الان هوش مصنوعی تمام این مراحلِ میانی رو حذف کرده و یه جواب شسته‌رفته و آماده می‌ذاره کف دستمون. این کار زمان رو ذخیره می‌کنه، اما «فکر کردن» رو هم حذف می‌کنه
🤔
2-
داستان ترسناک مرد میکروفون‌دار!
نویسنده تعریف می‌کنه که دوستش تو یه رویداد استارتاپی تو سانفرانسیسکو یه نفر رو دیده که یه میکروفون کوچیک به لباسش وصل کرده بوده و کل مکالمات روزمره‌ش رو ضبط می‌کرده. آخر شب هم می‌داده به هوش مصنوعی تا تحلیلش کنه! اون آدم با افتخار می‌گفته: "کلاد از من باهوش‌تره و تفکر انتقادی (Critical Thinking) بهتری داره، پس من کلاً فکر کردنم رو سپردم به اون!"
🎤
3-
مرز بین دستیار و از دست دادن استقلال:
ما همیشه بین «جواب‌های سریع» و «تفکر عمیق» یه معامله می‌کنیم. وقتی برای هر سوال کوچیک و بزرگی (از اینکه "شام چی بخورم؟" تا سوالات فلسفی و تاریخی) سریع گوشی رو درمیاریم و از AI می‌پرسیم، کم‌کم قدرت استدلال، حدس زدن و بحث کردن رو از دست می‌دیم
🗃️
4-
داستان سفر پرتغال:
یه جای قشنگ مقاله می‌گه با خواهرش تو پرتغال بودن و براشون یه سوال تاریخی/فرهنگی پیش میاد. خواهرش سریع می‌گه "بذار از ChatGPT بپرسم". اما نویسنده می‌گه "نه، بیا اول خودمون فکر کنیم." شروع می‌کنن به حدس زدن، تئوری بافتن، مخالفت با هم و استفاده از اطلاعات دبیرستانشون. بعد از کلی بحث، می‌رن از AI می‌پرسن و می‌بینن خیلی از حدس‌هاشون درست بوده. لذتِ اون «مسیر فکری» دقیقاً چیزیه که داریم با هوش مصنوعی از دستش می‌دیم
🗺
5-
اگه من کارای روتین رو بدم به AI، زندگیم بهتر نمی‌شه؟
اینم یه زاویه‌ست. خیلیا می‌گن اگه تسک‌های خسته‌کننده (مثل ترجمه داکیومنت یا خلاصه‌سازی) رو بدیم به AI، وقتمون برای تفکر مهم‌تر و جذاب‌تر آزاد می‌شه. اما مشکل اینجاست که مرز بین «اتوماتیک کردن کار» و «تنبل شدن ذهن» خیلی باریکه. مثل دانش‌آموزایی که حل مسئله‌ی فیزیک رو می‌دن به AI؛ درسته که نمره می‌گیرن، اما در نهایت یاد نمی‌گیرن «چطور» به اون جواب برسن
👍
حرف آخر:
سوال اصلی اینه که ما دقیقاً داریم چیو اتوماتیک می‌کنیم؟ «کارهای انسانی» رو یا «عاملیت (Agency) و تفکر انسانی» رو؟ استفاده از AI عالیه، ولی یادمون نره که بعضی وقتا حدس زدن، اشتباه کردن و با ذهن خودمون به جواب رسیدن، همون چیزیه که ما رو انسان نگه می‌داره
🛡
لینک مقاله‌ی اصلی:
https://www.artfish.ai/p/offloading-thinking-to-ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4515" target="_blank">📅 14:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4514">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Un8ugpttfWmSpWC-JzlXO12OSlhR3vO9t11Lgpp7VJXh036jc1cNlkrWZlIqmBuFDVTPAlknY9LZTUb0tEP0bPDQ_4onHCjWlC5gSv_OT_P5H47G_kNwS1ce1vt4ijMCWm_0CdP4fpVo_-z_XjG0_s_jTqilLBvlyZGGmL_-NSJB1AvYM1Zu04AtWgqFKPAmsUl0jTsltJ-woMqgGFlbre9zU-TbOEbBxAYh0tOG46Zm2l6P8-HMgg9aV9VtVv3cNjNQ88YLefN2alyiL-0viy9OxTK6Y2LhBtuUTE6w4aCPNVjl7UQ-z7XZsGhfSEnhXRRonMfo3KlKGwSm0sWY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای اوپن سورس شدن xAI Grok-Build
داستان یه مقدار خنده‌دار (و یه مقدار دارک) هستش. همونطور که می‌دونید Grok-Build همون ایجنت کدنویسی تحت ترمینال شرکت xAI (مال ایلان ماسک) هست که به‌تازگی توی گیت‌هاب اوپن‌سورس شده؛ اما پشت این اوپن‌سورس شدن یه رسوایی بزرگ خوابیده بود.
داستان از این قراره:
1- رسوایی سرقت کد (Spyware شدن ابزار): چند وقت پیش، یه سری از محقق‌های امنیتی و دولوپرها نشستن ریکوئست‌های شبکه‌ی Grok-Build رو مانیتور کردن. دیدن این ابزار وقتی روی سیستم کاربر اجرا می‌شه، فقط فایل‌هایی که بهش می‌گی رو نمی‌خونه؛ بلکه داره تو بک‌گراند کل هیستوری گیت، کل فایل‌های پروژه (حتی اونایی که بهش ربطی نداره)، کلیدهای SSH، پسوردها و Credentials رو زیپ می‌کنه و می‌فرسته روی سرورهای xAI!
😂
2- مچ‌گیری و آبروریزی توی توییتر: وقتی این قضیه لو رفت، توییتر منفجر شد. همه شروع کردن به گفتن اینکه xAI داره دیتای خصوصیِ دولوپرها رو واسه Train کردن مدل‌هاش می‌دزده و اسم ابزار رو گذاشتن «جاسوس‌افزار (Spyware)».
3- ماله‌کشیِ سریع xAI: شرکت xAI وقتی دید مچش رو بدجور گرفتن، سریعا یه بیانیه داد و آپلود اتوماتیک دیتا رو قطع کرد. گفتن تمام دیتای قبلی رو پاک می‌کنیم و یه دستور /privacy هم اضافه کردن که کاربر بتونه کنترل کنه چه دیتایی بره به سرورا.
4- تیر آخر (اوپن‌سورس کردن اجباری): برای اینکه اعتماد از دست‌رفته رو برگردونن و بگن «ببینید ما هیچ کدی رو قایم نکردیم و چیزی نمی‌دزدیم»، مجبور شدن کُل پروژه‌ی ۸۰۰ هزار(
😭
😭
😭
) خطی Grok-Build رو (که به زبان Rust نوشته شده) اوپن‌سورس کنن! الان سورس کدش به صورت کامل روی اکانت xai-org تو گیت‌هاب منتشر شده:
https://github.com/xai-org/grok-build
خلاصه:
دلیل خنده‌ی ملت اینه که xAI از قصد نمی‌خواست این ابزار خفن رو اوپن‌سورس کنه، ولی چون دولوپرها مچشون رو سر «دزدی بی‌سروصدای کدها» گرفتن، واسه فرار از رسوایی و اعتمادسازی مجدد، مجبور شدن کل سورسش رو بریزن بیرون!
ولی خب، از هر زاویه‌ای نگاه کنیم، این رسوایی در نهایت به نفع ما دولوپرها تموم شد و الان یه ایجنت کدنویسی لوکال، قدرتمند و اوپن‌سورس داریم که می‌تونیم مستقیما رو سیستم خودمون (بدون فرستادن دیتا به سرورهای اونا) اجراش کنیم.
هرچند فعلا باید خودمون بیلد بگیریم با Rust
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4514" target="_blank">📅 08:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ماجرا داره این اوپن سورس شدن
که خب به نفع ما مردمه به هر حال
و خنده دار</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4513" target="_blank">📅 07:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انقدر خندیدم که دل درد گرفتم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4512" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">https://github.com/xai-org/grok-build</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4511" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برگام
گویا Grok-Build به طور کامل اوپن سورس شده
😂</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4510" target="_blank">📅 07:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.  در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است.…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4509" target="_blank">📅 07:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZgrLNtHqhB4cDtW0uPSyzSHzxvkXxCyVA_uKQdLgF0MFvnwATR3-xAHTurnNxRQETDEA6amd_1yk3vJmgXCGtCSplzRDSeZ-CReIVlm_AjKdd_HmTToSKKiDWmAU4hb0MWbtzx9oayvv6npxUi2uAl0iZ3-fud1IORYTwp76Xr-AHxBpduiKgJqG4JPBQtvUXiu7hVOJ3dX_r6SLj0COYFro3UirSV0LxeR0K0j1um1MW32xITXteu1iYeMITXNtGLqjWj3L_OPTvJ3bWOCizqHtCQsAic07-VZosOxqX_VO3yt-Dp8wO1FHWGLpD1PkVA_WGtvCrek2oKMemaJpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هک Suno فاش کرد این هوش مصنوعی با دزدیدن میلیون‌ها آهنگ از یوتیوب و دیزر، یاد گرفته موسیقی بسازد.
در یک رسوایی دوگانه، گزارش 404 Media فاش کرد که Suno، سازنده موسیقی با AI، هدف یک «حمله زنجیره تأمین» (نفوذ از طریق تامین‌کنندگان نرم‌افزاری) قرار گرفته است. هکر با دسترسی به اعتبارنامه‌های یک کارمند، به کد منبع دست یافت که ثابت می‌کند Suno برای آموزش مدل‌های خود، دهه‌ها محتوای صوتی را از یوتیوب موزیک، دیزر و پادکست‌ها «اسکرپ» (استخراج انبوه و غیرقانونی) کرده است.
شرکت Suno پیش‌تر ادعا می‌کرد بر اساس «دکترین استفاده منصفانه» (قانون اجازه استفاده محدود از اثرات دارای کپی‌رایت برای اهداف تحلیلی یا آموزشی) عمل می‌کند، اما شرکت‌های ضبط موسیقی معتقدند دور زدن پروتکل‌های حفاظتی یوتیوب، نقض صریح DMCA (قانون کپی‌رایت دیجیتال) است. این وضعیت مانند آن است که کسی برای یادگیری نقاشی، موزه‌ها را شبانه تخلیه کند و ادعا کند چون آثار «در معرض دید» بوده‌اند، کپی‌برداری از آن‌ها مجاز است. علاوه بر این، داده‌های حساس کاربران از جمله شماره تلفن و بخشی از اطلاعات کارت‌های بانکی در Stripe لو رفته است؛ حادثه‌ای که Suno در نوامبر 2025 رخ داد اما آن را به عنوان یک «حادثه امنیتی محدود» پنهان کرد و کاربران را مطلع نساخت.
منبع:
https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/
✍️
هوش مصنوعی گراتومیک</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4508" target="_blank">📅 07:15 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
