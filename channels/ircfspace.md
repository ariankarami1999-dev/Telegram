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
<img src="https://cdn1.telesco.pe/file/KjZwPF0Fr_yMdvartlnLztOXefjeRpZcbTUoXDTos9-hxoOWTxg6aaXorHKv86ZK-xYhRmKd1kUhszXdMWxtam5fXdMLzo6BzUbtDhNwU-0RstUM4Ekqkt1I9ECZ7tIHK5ILVPEf5VOtRlClLGnKA381xSzLAxex3UrqQex0DRDB8t-L5Y_k5hGCQ3FxXSTnuztc_k2tfyfyBGrih3B-oYU1ybd0QkFuFuyfZmz29G53ua3_EDX8nqAgb1hTGihvUrr8HBk9WkthUFmlZ8jO1a1vva8z2MpjcDdlOudIiwZJddQYQMUi9hmksshiWtqdYvYrvxWVU-fWy7882SRkPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ld1tQVnPGyBfK8NlSgLz4i7pLIjVOuXBbjsdR1LEGwlDoh6MfEg8K8eaJwhSPY4i9SBJjDT09vqyYcrdFH5er4e5a-Dds_21fdcHNyhKtVvlIE4qjIYu8T-VVhH-JyBVVQh9CEctE9cs8_4_JdB4Y_6yLbRPUcSjz5JPdKvUg1JJ-ySSkt1RUKjRpCSjJve7RtIpE1wT3n9W7YdAPJqvBr6dwXfCXtCNk2t9_RriF8NFASTqlvdrrjqJIw9jISkfeMYEpVlVPEYHPJ11SrbqfNLcAhv_aRvwa0ja4CVZkTsRM3us6nOu1LqEFwYn90hD1KfWqXePXLU1UR1RRjyv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت متن‌باز و رایگان ZedSecure آپدیت جدیدی برای اندروید، ویندوز، لینوکس، مک و NixOS منتشر کرده. در این کلاینت از هسته‌هایی مثل سینگ‌باکس، ایکس‌ری، اسلیپ‌نت و شیروخورشید پشتیبانی میشه و در کنار پروتکل‌های DNS، امکان استفاده از OpenConnect (سیسکو)، IKEv2، OpenVPN و AmneziaWG فراهم شده.
همینطور OpenConnect روی دسکتاپ بصورت VPN سیستمی قابل استفاده هست و امکان اجرای زنجیره‌ای روش‌های اتصال مختلف اضافه شده؛ مثلاً میشه سایفون، تور یا SSH رو از طریق یک کانفیگ Xray اجرا کرد. روی اندروید هم قوانین مسیریابی میتونن بر اساس نوع شبکه (مثل وای‌فای، دیتای موبایل یا اترنت) تنظیم بشن و با تعویض شبکه، بصورت خودکار تغییر کنن.
👉
github.com/CluvexStudio/ZedSecure/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dd9bgLedulm80tAqabJeWUwrnup8vFZjaS8Ma3YbJ1H-O2ODdE_Cv4DWglaaqnZGRihMyR_1yH-WLQ1KsgonEx89GZxkbI7jtFpxvMJZ88gsr1LPW30gSNyV5C0B0rbNjbMlgaEWWsFo8VFf8N5GyV9a4QvFtnYsrQAIK2aLIA9IHi2q8pbA0B6JCcAN0pECa16DKXs_2voMV8p5KcXqcMQN0MnuuX42hgux7n2Mfk6jRsJZAs0zoKWJB2JQadS531UvtZgU9lUQtu0rtZloJEpNyQu6snqhC2a-_GCxtFIFI9MPJVEoEVCfytgmEt_tEFi-znwhzq-aI6bxHP0z_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UW5RGZ3KNzqQBUIE1KuezluKFri4sp3f9TgAMtzCXeObmv6iBd7z0zZIFQilSd5T3lBAVjuUh__xtG2FEqbIi_tA-lH8UXsv_9PeFXxnseafVU-bj3yGvg8nFA_9lWEVQ2OY80O_om_eKzf-bqkYV8GQ5Y9rVXNEq0k8ZVVx3tZNaJ50X4i8nUD8KI89kbb_p4xZTAwUg6YGWE5gYiYUnOIooD3lVf-ZM6G8sDGP4DajPpau3XbNctvt3ZYlaXZvVdcZjpkl5QXkuPCn28EdtLiL_zG7XlXzQDt83zRCWKRnIl4FbrFtrzPSx_UDb3-sWGs07wls5hkIF_rIQkI8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eONVmmga7sJuI5qKyMjdT-LwcIsMGg5xcfrydHG1fgpKjfLd2m53-seRoPTeUaDoYg6KdzQ1bXsPVDk2lyg9zdjvEpvaRg0_I9jjLbaYkrnmkb_FXBdrn-XsO7GME61akwC9aF_kT2vnuDAhfTryMFxO7-_mZ4SOEIN8q72R4Sq8upLkLKqSFxXg27ygp_dFvWau6OIQhmLrst717aSSstmUsTZQWFwFdeI0CFoJRuzJkBGVDnqeqrjAqT_9RqEysjSZ2CaTtGGmMEMNmU9X9vqDK0qvabjTOAPLyc0kiOmD4lLqAKzIYEiO70iNp51OUWG1V2FqGe5vge6M5O-NGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اسکنر متن‌باز و رایگان SenPai Scanner برای ویندوز، لینوکس، مک و اندروید منتشر شد، که توی این آپدیت قابلیت Anti-DPI اضافه شده و با تکه‌تکه کردن ClientHello (مشابه چیزی که در PattNG انجام میشه) امکان دور زدن بعضی از محدودیت‌های DPI رو فراهم می‌کنه.
حالت Gentle هم برای اینترنت‌هایی که وسط اسکن آیپی‌های تمیز کلودفلر قطع میشن اضافه شده و حالا می‌تونین آیپی، رنج یا دامنه رو مستقیماً وارد کنید و اسکن رو از فاز دوم ادامه بدید. امکان ذخیره اسکن و ادامه دادن اون بعد از قطعی هم اضافه شده.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شستا ۱۰۰ درصد سهام رایتل و ۵ کرسی مدیریتی این شرکت را به مزایده گذاشت. قیمت پایه واگذاری ۱۳۰ هزار میلیارد تومان تعیین شده که با نرخ امروز دلار آزاد، تقریبا معادل ۴۸۳ میلیون دلار است. فروش به‌صورت نقدی و از طریق مزایده دومرحله‌ای انجام می‌شود.
©
stup360
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dyg1GOIO4tTIISX2pVBJbHiA-ujU0Bniuo1qzLmgUnzZeODwLDzbCf3oolEY7Xbp-cI2q2KWtApLOmVJ4bf0t5PHHMvwPdAx-Hv4eLR6ox8nbPA1mHGi3n1AThulfc4qLbJujKntm0-kNpOyQIOB5wpZYNyZNhjE75D8hv1Y15C8feZShtiaPnMPkzJVuYLOzQCX0uS1OxCxdynLagEEzwT73fuH6jR7YcTLVfWxDsB2dUAiAFsNoBFvZnLqF4ZNwbuDjKFjhSr50UtEQSkIBdv8FFC7sAdwD6Fav9iHocGozhgXP08JtaO7E7Mjr8ay-oZuNQafu3HSyxWzVMBxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها در تحلیل وضعیت فیلترینگ ایران، جمع‌بندی روش‌های فعلی اتصال به اینترنت آزاد از طریق کلودفلر روی فایروال همراه اول و ایرانسل رو منتشر کرده.
بر اساس این جمع‌بندی، روی فایروال همراه اول میشه برای اتصال به CDN یا Worker از روش ECH با یک IP مناسب استفاده کرد. استفاده از IPv6 هم یکی دیگه از روش‌های فعلیه که بسته به فیلتر بودن یا نبودن دامنه، تنظیمات متفاوتی برای finalMask داره. برای WARP هم میشه از متد WARP-in-WARP در اتر روی IPv6 استفاده کرد و با اسکن، IP مناسب رو پیدا کرد.
روی فایروال ایرانسل، برای CDN و Worker میشه از متد F&F استفاده کرد که نیاز به تنظیمات مشخصی برای finalMask، cipherSuites و فینگرپرینت داره. WARP هم روی این فایروال قابل استفاده هست و محدودیتی برای نوع IP وجود نداره. علاوه بر این، روش MASQUE/H2 با اسکن IP و تنظیمات مشخصی برای فینگرپرینت و finalMask می‌تونه برای اتصال به کلودفلر از طریق هسته اتر مورد استفاده قرار بگیره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ieaEOUj_zZNW0VEO8wHc6RloEtjSCXK3iIgUrbvyvKpEtbzckjB3Wuo6cchpzo3A16zPd5-44laUk4flqbTXxyZXQk5V4B15buhP6J8p4JDeiFdC2mkjU4AYMshHnWtxwex73NF2sxpOQh8oUuY7p3DzICu4ESr6PHLNGZZZY2Cx1YzUxD-EssTMvvkvJGNMpPAM_ixNXFDo_XDhjBP16ZkR9zJJZ59IzdVu2gMNEmrGf2h2GXsvzA_flRfEARqp--GJvh8EOWf9HobhZBshZsvAIBCYOHeDPz8jb8KkABSxJuE74YZ2UrVW0Wx42aK2fBt-6pQhJptb3NdMDVPVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن دیفیکس توی جدیدترین بروزرسانی خودش قابلیت تانل‌کردن کل سیستم رو بصورت آزمایشی برای ویندوز و لینوکس اضافه کرده.
در این بروزرسانی عملکرد کلی تانل بهبود پیدا کرده، مشکل نمایش پرچم کشور محل اتصال رفع شده و چند ایراد جزئی برطرف شدن. این نسخه درحال حاضر روی گیت‌هاب و گوگل‌پلی منتشر شده و بروزرسانی مایکروسافت‌استور و اپل‌استور هم بعد از تکمیل ریویو، در دسترس عموم قرار می‌گیرن.
👉
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/msKtBKJtcYYul3fr7GmTSfhpnMd76Gxw9gC6mrtjDYoJDOL8lx7ABNkEW3Cu_1-W2VDSUCcrduQWELmNttN1i-YZ_uRT3o6AttC4gH1STbyF_6aNf9YXyKJtn7vYfSZUQJSI3e88HZQ-Avz8JfyGsGbS4bbHWZmKwRrauUwXJ3ZhO3QiVHaMWNemkK2OR7K6v1DdpGHu40Bbudkmv-xfjda-9BHdmIxUqTmsa202bqI_82NJL37To2yegbArMBIKVkoa7s6kGHTbfZOfcdFyoPR0bOjPHLPmuAQkAZw4GIWFt75AjVdrg0HPdd2hjeBl_XVc1Q5RUT3h2mlyUO7a_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1nRIMQdhNQsz2JtB7g0P70cmdv2YNKdIMRacfMJOw9uuAD4wmWEJzDicOZdN_H7bvfm2u-6Ft4ns_4m9O4mluPNtjhdxWQ8RtdTbIU9fQ4iJhXDkuFZs6e_93jy4-dJ-OQy-qRNo4q1TjnyWivLFDOS9Nb0UjYkYhOotTiO_V6DINshfEHR1ZuHgtJ5BHFoq0fUuVm38Rl7rIYFDuGok7maOqc8Ozli8z43h1LndG2t8Hccite6GhSgRKadT2oUT1dAAcGu5lzrjpg6fJKnHpqNW7fRevJh7geDFjCMjpdQ415t1aLgiWN-AGPhNkYh6NYm9_H9T62XqaVlcN4T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در جریان اعتراضات دی‌ماه تونست با جمینگ و GPS spoofing روی
استارلینک
اختلال ایجاد کنه و حتی تو بعضی مناطق کیفیت اتصال رو به‌شدت پایین بیاره، اما اینکه بتونه استارلینک رو کلاً از کار بندازه، دور از واقعیته!
اسناد ITU نشون میدن که با وجود این اختلالات، ترمینال‌های استارلینک همچنان تونستن به اینترنت بین‌المللی وصل بشن. حتی راهکارهایی که SpaceX برای مقابله با این اختلالات اعمال کرد، باعث شده سرویس در بعضی مناطق دوباره پایدارتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W70v1_G7pURg-sGfR8cKVx7Cj8EGq8mh4DcjEjLKCuV2uptrrw-mFLAx2RWu1iYPnFCkPT2wvdV1lpcft2cWLycAhrQq3h8rgOz-bpB4lheXmKj6mfzmLmyOojLRcOGO3butTqJ77CLq4L_hfF_5xh6_RVWwnM0zEBX6HQ3lbkEqb9X5LOSXLyqwZID42Vl3rxo_nc1vKGRG-aqY34RfEesQr86KYgMQ9j79ao77-teMqvRnId1DON6MVH5jJV3qT9qPc_mjNWqAq4HSgw-g8NT0XhsBzn7sTk73ky5eUSFmCObK_1avkPGkvI6oHYvRBzsNsLb87X85E6AQ2QukwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ateY8GKEVrbMQyjHWz2KVXOsVoMZlujWx8vdtrAfElZC2M8IECm_xuW5Yhw_ETFGeCxJHe7jKyYUTS8qM3zN-dfyhigkOOpnjm5SKwRm__aeBX5aFf5VmwHSJs-3-XxoWbzUCTIxfkALAKV5TJ65dvlrrWZOdZvvFTV7aKyEYoih3YamSqzAzhXQT-B17UexGU4I7bk7Ei1XwJSdBxd1LyvFofAfYuJVn5KzrvxSaDo-JcUL9nHu_9SPDhsF4RESc7pCLnjmdXfztJbWDloorYtNUn4TU4wWqZoKnhggA5Rt8_Kt-sclJAq6eJcrsRwtm6Rj1HGR8fOOI_O7w8IxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از فیلترشکن متن‌باز و رایگان Aether-GUI با آپدیت هسته اتر به جدیدترین نسخه و اضافه‌شدن متدهای اتصال سایفون، تور و مسک‌این‌مسک برای ویندوز، لینوکس و مک در دسترس قرار گرفت.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eu4CoDnM_EyfYw_ay-gQXXKWmhZghPiybQlGfg92o6sSNRR8Vxx8-u-oNTXPUfWnYqCWm3jgRjkKB2lfP1zCwItuHt58IXwx6QkzdAhGztnBukfRurhKszwGzvv2Hal3kYccR4KHeIupNifEhXgJqiWcbRDziNi29kR4Le7yW_uFz_ZVkX9vWad_3LkfnhJPbwEdGfe99fGRuB6hPp_BpFDuhYawYibSfEl2it-zdGlCnpw4B_PJyVTz1SBHLupEHoWLSkgWBTlrcagP2X4fyIgYWdkXmONPUMs-qdXS1c6G-rVe7cTHviYBiBKOngUWyBjlsFGP8FN69Qu_eXJRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dwakBIyYI_3Mzptp1wiaIkHpOiLawKJGzV4eN4q7rtVNZyVJX15-2Lpai_7Lez_5xye_LSif6Iea7-fVdznjx_wWtVuW7wLK69Y-kuzwQDL8FqiAP8gMMtl4H73gz3a4cghhp3c_viXJRsisY3MJbdR5VWjopHKZXWnoqGko0cBV6qwmxrG7th9x6f1ZbzxKfqyVP0rmVxDmr5gVv9JdZans4lRmF-kUPrPmCUbuo9Wn_6kSM99H1S_K8A3cUidooMbNnEcBBOiM25w7_Q3Qxn8apWMTfNFrEfMgG1BkhB-_qHd26ffCm2Lg--8T0hc05LozY2raw8TLW4BPqgJZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زومیت در گزارشی نوشته که در حال حاضر دو راه رایج برای دانلود فیلترشکن JumpJump وجود داره، که یکی از گوگل‌پلی و دیگری در گروه‌های تلگرامی هست؛ اما بررسی کارشناس‌های امنیت سایبری نشون میده هر کدوم از این جامپ‌جامپ‌هارو دانلود کرده باشین باز هم در خطر هستین. فقط خطر یکی بیشتر و اون یکی کمتره!
جامپ‌جامپی که از گوگل‌پلی دانلود نشده احتمالا یک فیلترشکن دستکاری‌شده هست و به نظر می‌رسه این فایل یک exploit یا آسیب‌پذیری قابل سوءاستفاده داره که می‌تونه دسترسی root در اندروید بگیره و رد پای دولت‌ها در نسخه دستکاری شده دیده میشه.
حتی اگر نسخه کرک‌شده رو دانلود نکرده باشین، بازم برنامه اصلی دسترسی‌های نامتعارفی از دستگاه می‌گیره که نشون‌دهنده ناامن بودن این فیلترشکنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORnksidqJ-APN29a8ccIOFWb7Q1WcMpWnZ6t_MyCHZkS3V6F3mLWgPZFxe5u-oMaSzPDY7RvEb9fZft6XnxIHh42Y0sBFmCbTiYDGffgPqHLnYgjB4Nbmr1ESMuVgCLE1yf2zAGrXbw9SSMe8f3M7HOrjj05cdQUsogNBE9ru5t8JG3ggDFLyEBolUPOF06ixkeA71G_xxkTrpT3m6B9d-P7_kctZZrU_j_5aNHdKbQJSvY0nnqoKWeXWJWJZ5xiG3OTUWLLciRz6_cm1lXeMBHZ1P0ESr5zbOjg7CndpWwdQWS0otvRc7q2JPYGTW14zmiO5Xm-jalGKU2FMLxtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از اپ سایفون چندروزه روی اپل‌استور در دسترس قرار گرفته.
👉
apps.apple.com/us/app/psiphon-vpn-secure-access/id1276263909
💡
play.google.com/store/apps/details?id=com.psiphon3
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fdx1VMeSUn1rc9YrB8tBWQM-n_dASEuR9HSCkse7vjS0wsPMzPtT4SU6HAAeuse8522OXaYwoG5QPZuKwHsBfE1aluT6VifIQRXn2CGACjufZjVrqYLeG4sAb_TIMRUrfjI6nIKqaXNrV3q6lKJltITBBVgm8eg1wb7vOJ0JJEoiZbS_O33lnHHvZC_kxYMEUVQGe0X8KJFn6WXCuqiVCd_yauglK4H826225tTnJ7TiqKlEiSiBZpF83wW1moCvpPK_sUf7JeJuhT6XLYUMbqMn8gpZTmn7jlSZwaKdhLautQq8iNZGaUMOsRWXCI3CrVmkwhzkqpQTowyvARSXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق آمار رادار کلودفلر، از ۲ روز گذشته ترافیک ایران به کلودفلر به شدت کمتر شده. اکثر کانفیگ‌ها و اتصالات به کلودفلر مثل وبسوکت و xHttp مختل شدن، فرگمنت روی همراه اول و مخابرات بسته شده و روی ایرانسل ضعیف کار میکنه؛ همینطور پروتکل UDP به سمت کلودفلر کلاً بلاک شده و اکثر رنج آیپی‌های هتزنر و OVH از بیخ بلاک شدن.
©
mahsanet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXd8pDiVWP9kiJgfBwx-lIm_r6tdBFCLYBDMWcIth2kJaW7zUmo3I2jncTO5o1JY5RQsikjepYdHSgtbbrTJNBDCqDOPKZfaoOukYSp8eMGE9V4oJHFDi31xPF7LdRpNi4CYV-4_zs6D2R_53CmlQwbwDp5Zuix7hk1rj3admzfHJBO1a1SRKtWz9_GRLyuvH_Xu-8FInIa1LckMkAkWlbrO79O-6MYcR3mZaX3zEbq-T3ngaObI9GznyL5-WgexAjTBTipIVZqryi-nwJzcFBqhCMgBqFTu-n2-Ov5ldwsDDUL7CoeqjtpSuXcUY7yJaYXaWlkn0xcthEPg7D9rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه استفاده از برنامه‌های PattN و PattNG برای دورزدن فیلترینگ
📽
youtube.com/watch?v=CnEQipAJ2hE
💡
t.me/ircf_toolbox/25
©
𝐀𝐥𝐢
👉
github.com/patterniha/PattNG/releases
👉
github.com/patterniha/PattN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZtjtkfY78ZGRu03i7HEDLOBohUS4Fuf7i6ynVbXr6hMEp-MucX70tV7v0WCIarIVa1t2YCa0zeFRFC4rxuP49a7s8Pk_lxCmzSJ5gJzRWdizsHliCMhKvLPQrcO19Fv72RbvxpJezNVynu3pVo3UB8FkUCoHpy_LS5bn2ndAlb_NVLS4UC6tHF63AYe6YQ2hP_5paCZ-Jn6yS9Aosx51u4CJOyztYg0-tEGLgbicoc9LgO8ZJMYktlk2j2Y88VnCtnmvui6cQ0EWfC1YoKcvRVH_LGVp5Jz1IUduzSS8e-AC7y1BdWlUcw3mJbEERT1P5NKdT7bmRUvQJdqpxci26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید از هسته Aether مشکل برگشت آیپی ایران در متد اتصال Gool رو برطرف کرده و محدودیت اخیر دریافت کلید وارپ و مسک رو روی بعضی از اینترنت‌ها دور زده.
اگه H2 روی سرویس دهنده‌هایی نظیر ایرانسل به هردلیلی ایراد داشت، میتونین طبق داکیومنت از فلگ فرگمنت استفاده کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKbrIYOK08ScVv0OTJpjD7Zr6Mv1KJaPMhPmFL81P70E2vbtKlhNsii1aoNdfkD1Sa4C8yvI96jeq37i7fNAQyrJoIJNyT-LDNM9DvVFzFbOimmUIdlEa4FOYYTo_-8-dREaxcfk1rqfYe1dQQwfl__uz4lifdLWsA9WpmuE4JzgtwheLlXhu8pxkjJtf2mN3b411UiyvsyjA6wi8GdCdDlx9K7WJ5_sedLQnbfz3_XdQijm1-qou1hC5kxVW51uLJjiuNHzOkdlGbKCs9dt7WJkaaG_LdMNP0F5uwTh5zhYUIeht-cKOogq8GlQ7Z0yuWFW1nQ84RaA6FYJCHquWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱۸ از فیلترشکن اندرویدی MahsaNG منتشر شده و توی این نسخه هسته Xray مهسا آپدیت شده و پشتیبانی از پروتکل MASQUE رو اضافه کردن.
برای وایرگارد و مسک حالا یک اسکنر IP اختصاصی در دسترسه که از نویز و پورت پشتیبانی می‌کنه و میشه کانفیگ‌های این دو پروتکل رو با کلید Auto ساخت. امکان بکاپ از کانفیگ‌های شخصی، صفحه پروکسی تلگرام برای کپی و تست سریع پروکسی‌ها و بهبود Fragment و حالت Auto هم اضافه شدن.
چند نویز جدید برای عبور از فیلترینگ UDP، کانفیگ‌های جدید یوتیوب و پشتیبانی از Cipher Suite برای افزایش سرعت آپلود در متدهای پترنیها به این نسخه اضافه شده. FinalMask حالا روی پروتکل‌های جدید MASQUE و Hysteria در دسترسه و علاوه بر رفع یک سری از مشکلات، ابزار زنجیره‌ساز کانفیگ هم از Fragment، Hysteria و MASQUE پشتیبانی می‌کنه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dvYIry1JRFO1hUmkytx-ifagPi4IGBHVFNjA3qWwM6W7poCIpbP-zJSoJN5IwlzhhsUnzXVdK4Q0mdJidVwRLIfUEhz3huUvFUadH6Z2DEdmU__Yxv4Xof8X5tt3vv9-Wf1BS_IHN0efcB0Y1MyMXAqb62CUt5SJgiLRnWGqSyrRnu04o47zOPthzbTbG2cWgFAkG9qYI6rJ6FojczIJ-XThfAY7GxyhRrSOCivrc4xsDwXx9N1pJ68mBK8SDw-4Q7sV0TbS6y0_Xmp4CM4CQaYn2AGFCHEF1e6L43kIapfggKmsLQL7r1ysmTYndkPtaVKy6_llNYR1WUzZ0_jkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل از نسخه iOS ۱۸.۱ قابلیتی گذاشته که اگه آیفون ۷۲ ساعت آنلاک نشه، خودش ری‌استارت میشه. این کار باعث میشه اطلاعات گوشی دوباره وارد حالت محافظت‌شده‌تری بشه و ابزارهای فورنزیک مثل GrayKey سخت‌تر بتونن قفل گوشی رو باز کنن.
حالا شرکت Magnet Forensics که سازنده GrayKey هست، ظاهراً راهی پیدا کرده که قبل از این ری‌استارت خودکار، گوشی رو در همون وضعیت نگه داره تا مأموران بتونن فرصت بیشتری برای استخراج اطلاعات داشته باشن. این قابلیت با نام GrayKey Preserve و همچنین Evidence Preservation Mode معرفی شده. البته فعلاً این موضوع بر اساس یک ویدیوی تبلیغاتی لو رفته از شرکت مطرح شده و جزئیات فنی روش منتشر نشده. در واقع جنگ بین اپل و ابزارهای بازکردن قفل گوشی همچنان ادامه داره.
ناگفته نمونه مأموران توی ایران برای باز کردن قفل گوشی بازداشت‌شده‌ها، نیازی به GrayKey و این ابزارها ندارن؛ زور و تهدید راه ساده‌تر و دم‌دست‌تریه واسشون!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پروژه Nexora یک پنل برای مدیریت چندسروری VPN هست، که تا ۲۵ کاربر و ۱ نود رو بدون نیاز به لایسنس و با تمام امکانات پنل در اختیارتون میذاره و میتونه برای مصارف شخصی یا گروه دوستان یا خانواده قابل استفاده باشه.
نکسورا مدیریت کاربران، نودها، اشتراک‌ها و پروتکل‌ها رو از داخل یک پنل انجام میده و از پروتکل‌هایی مثل VLESS با REALITY، XHTTP و Encryption، VMess، Trojan، Shadowsocks، Hysteria2، TUIC، AnyTLS، Naive، ShadowTLS، Snell، Mieru، MTProxy و SSH پشتیبانی می‌کنه؛ در کنارش پروتکل‌های کلاسیک VPN مثل OpenVPN، OpenConnect و WireGuard هم قابل استفاده هستن.
از قابلیت‌های دیگه Nexora میشه به تانل بین نودها، پشتیبانی از CDN و چند آدرس برای هر نود، همگام‌سازی بدون نیاز به ری‌استارت، Rule-set برای مدیریت ترافیک، مسدودسازی تورنت، محدودیت دستگاه بر اساس HWID و انجام عملیات گروهی روی کاربران اشاره کرد.
برای مدیریت و نگهداری پنل هم امکاناتی مثل احراز هویت دوعاملی، بکاپ رمزنگاری‌شده، بروزرسانی خودکار و Webhook در نظر گرفته شده، امکان مهاجرت از پنل‌هایی مثل S-UI، 3X-UI، X-UI، Marzban، PasarGuard، Hiddify، Marzneshin و Remnawave رو داره و از زبان‌های انگلیسی، فارسی، روسی و چینی پشتیبانی می‌کنه.
👉
github.com/nexora-vpn/panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDEyhaKIqVBAQYVkUFvs1SGYiyDzA0EW4im4KKMMW1_LCr2nkC5DYUF0kjrElyyHgHrQIRjGA_n_oNTOQcQSBAVNerMmjwLSzcRJhCq3_lbrdptWw8LhLimJ1O1l__YGXE0R9BOseLZw0fr-tag3suwYisav2bIqoecqYe12azZKbRAaXzeaYvmXpzeyViGtLQu6agEARtmEeHXKWYoCPJCxh4zhiV__rGpYDbR4VgoCdV9rfP8ysX72OwS78W_TLa_N0ZBYJANxZAWobwje6K4sZOtRUGE6wCiVz1V04oMFHA-p8J3O7N9xNr00nbZ76j01IzCAGbhOMzd6zX-DQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد و مهاجما از اون برای تبلیغ یک رمزارز جعلی با نام $Clippy استفاده کردن.
هنوز مشخص نیست چطور به حساب دسترسی پیدا کردن و تحقیقات ادامه داره. مایکروسافت هم اعلام کرده هیچ ارتباطی با این رمزارز نداره و پیگیر اقدامات قانونیه.
©
theverge
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRMvfqawTq8MA2z6rDVm1baQATRgT_6MVj93MaJPrTv_R0RJeHf8yjFWyl06d3dDjX9m-9l0Yi1KyhRtQsjuvLpTmfA_KNtlA6Z3vR78icWoC2uDQW3AboAYRM8cIM8f8uSshVWkmwXUZl9nDlGAFnlJoxOLZtVezwxzOLAjOQcT24dyb6aLbTaA4OjMbv46CY17u67WdqzI3ZOJ8R1OnyN5pU5VhEQF3uUNs7Cjf_IF5Z9yzRSdsHaTySb4wWUiU-um3LQZx8in4q9Vd2pKp_VwljAAcRQ6gerVMgM8UfFkdR8uTPR0ovvqIMdlKoQ4w91h15_xXspuVvzhBDnmWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XYXtftPANqBxDcHQluY4Pyrmo_I4PvQjYbe6zE5cY1-jkDLlgpD4fKnaJtVzZeam7BaUeYf_be3Sz5Kqrc7kKAr7-K3y1NgUCaC0YQhW6zqfd6C8dIpSNWUuwSncuxwGpojqm4P5vSQ5JpqEqTlb3Pvh-RAOSkFY70lu5mUejRHsFkedD8qkam5TDVJkwKipng-JhU_aK9jyo2rLI-oT-DKmcWY15bMw_gaODGqEFaWT4tqD5WY-kgNMOtbliF2py5yoF5bRfyP2bgZ316vDqzK4StBPGD66w3NXF6sjJEU2fCHhdm-d8XV6wdOzc4VnBfebou8GsMQKSgSIFPt59A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYXADrbGRMTz_QHY8_fVLwMmBs-ONOuIuksi1ZaWe8vfxhPuAXawgvXClnrrBN_lzZiVLfjzghJIoYcEr7pK_Rr_GoLrKoB9Y8gych0kC_vXggK4MY_-bOHZdl04c8MEAsE3BkKKS6yiWlSuzhCS5Arpu1pXIFm3pF4l6SHYTNlOR3Qo8w5Zz8XwOYBOYqC4CsLM6R7z_6MJcBNEK4S8BlDSgmPschx0qO9JRW_Elzw9rYH2EU9-VZiwn0CUeV5yeqREHUPrTxhoZLeO0Ym2dOb063SQ45hkwA34gxqqtTDXYbkfnKdrkjdbn2Y6u4RdCBfwPhUU0Ac95bPfx0H0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GHsCRbwkalQNg4yK8t9WHsBoGIwKHMQS8sbbYvs4bP9YC3kalz4N5pe3Mjft4lBkUK5K_1YJrO0nNraktLrsrd_cYRa7bwqea2A9kMN7ufaad0GuJqGN2lFrPwe2XnFlIZ-a7czZ77T3jXPxkBr8gsPJWd9tKbm_jH6DYr64ZxTQIU8MGDdScp5lzKV5SvLPbvtpp4y0p1wgXVEVS1MyqhSE3YIQRNDUo5OS7N8EMK5MLgGtoc0pbh71JBaAggxpSkFEgYN06hP3osVcIY7cVBAuvrQ_kKvDrqmy8_vaNe42BoFdX7vcSk4ImVRhoSjf5y6h09KL0WlYl9RTMQwAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAVgSSYhTkelujURRuCO4n4Qt9zx6W62mFbK1lC2W481V6n-a4XZLJjdWcmOEKtsHNsxSoFHrLPsAMQIcViTD2R4gO0u8FhAWa3h5F2yNKFKjyL8_-sJpXlxCcdCchA3VqR1hV-7skaFTr_dOTnVBIt9NlMqeJ-2_hMhVUAHxMadICMjtMHeva2ETEMu8mm3ATEpP9fiyhK4dFlGFBlw9XR-9-y83ZtxAj8U9Qg1Ipj00456Ko75UdXdEByMaBReN6sPlWjbBSLrz2KlyzexkhPnmwZWWabdV7gaOI3AQmfpUwoiEeqZcgbjn-Yya9lGJUf9jOHq40AILOLJB1yVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TF8AAHnUNztqVn8NeXZK8ZV3reaqoVTgtTYljhOaRvMHuzfyOH8STWEvN3Ih0KSk35XaG0icaDaP_HmPVBhSONeUxhCo9aZZuTa3Z6zwbTtu01LjXo9CLyHMLDQw9v65LzJ8514P4BQNWSlbX7WAqathtxk_JfyCT-4GgH7dUf84VyQg3bNltnoAlPmd6VvveDpj0M6gOzV9B9_nmtz5E7hcaZIGG0rOuwKNVJ5NhbEIaZRGjWnR2Iv1E7WVPUb3Od-ykMD9A_SwIcAbbzuoNTSs_jR4afShf0o-J2zCb8V3VheBdpBPl08c2p31Fp3xOGemAKY2-pvo_i47_zYWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c82-x_CQRYpwQgSlodh7VLeHuDwchE5Bb2amuWtiz2-eAx0WmfXmUmPSehytgTwoCd-vwyOu0jizjc6WzrbeB7Sb3jrILOND_aItVNntIe5wi4qPacqDJ1gppKjrQkcwQqjjPj78Q2uUYVxyhG7kHvGoyNw3jUBfmSvSmj-kutQAak87hu7SM676dSIfivteitN0gaGq_02HuFvd1To_S-wVpJh3zc0ANWrKtEfl05vgPTjffKz5qkvQnq8cWq1crRHZrdRLp1TTCu1Dt8p384gl3HJefERx6ZFDJBAGkdsbXzQyhRoh9eaEgSVZsdmJBYvkCQz-PXc7LU4gOKnq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oM-xtSa6-cy8o6kkKSh--mC_YaBWZ2OdkDXjBQ9RzBoY-dr6h9fiLyiZD-z9zPNCmgouw1bjncHLbo0axcznNNpFPNvoCrpD1dsD6SFGRwo6nvJ2ZMp2JJJSgPlwA1Ah4ESehJ4q0Bk2ORKbbjkFH1fSj36xdwe7XFwoiOy2EPLcoFwevraw0T_qVwh5ZXKp_FPiX4WtY-xm5Eq0HMfKrkY-h7yaE2xLjkEbZmgmVXkXTSy4OSXVwGxWMa64dJCh79l7NFDYqDF4W5RmFw0oYaucChJ2HIOCNkUDUsPsEnm8NCTsUlq4jpFEFVycQsjH_GESUh7RVXYej29_st7bdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YasQ24ROnptSN-psF5Lj5jBqQ9eU03aEcYo2DEdiX4vbb8sth1h_Du86OUuY4Pd8Gqr6ou5KjyPjiFgeXspSdTEb1V_Y3QtN8s2xQDr6-5608Jt8hSe7wS7H1Q7biRKrw1KhbPbwkxMKu8TZatBmWzcX-YR6gzyWjWvpbXrgXo2iriCItw48qV8_qOpGn9XjPD_3ZqnFaIH67ZA5WyvSXigsBSddzl_5jbMZTGE8ck4l_BW9P0rVayXhbTcF0eS2w5meOcU6GBdHpvPB2cbX_QbtuSynZ2W0nBIH5QKQrQ_osSXKSh-Ni78HGNNoR2kV3NlKsJcTU3rhNf_PDOj8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frXHqnetIUoS-mvxCDb2dZMPvq94ig5UGpBuJMHrr65ofuF5FZXNRNxmPF62RpWhAggqQK9wG3uwhKb5tiRpeImpenx2jn3fKco7-MW_qD_v3-d0ApG6SGkOAvhDUfeflzR5pGGtazPLrV9XNPqOEZZz8LHS-_PZP0SDBpAFEhDPjxPykuk3VIiEkWbmXC2kYEw_e9xww6Emwcqx4ZvMg6-q76PhKS8Yio2sITmwOln-VYuqY3CIYLDe1OsLIuKLxpN0zbHLpUJVoWKlbvXhLhIM2PTx9TlNuNCes5PQi4lw_rI44BMoX4yeg4XaxUhtHuMIwb5hKfbexziuV5y5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcasvzDDSEUUC6yYfvBOIgya1AWvV0ZyR49IFf9A854HK_YiXI7x6RttKQ68hfotpsgs63OruGsgDCXgA3HMKU2WCHh717lOgcSfZdoNDZuvOCvLiPVZbDv4Nip4tcrhkD2_FtvDhf4XJD1Ah6vfuj0mA8Mxt6uePFkakZhwMYSR0VMHZE_PL9AAlQ3lAqSPXm7oT-PSqwvnJW6SH2qvNgUHuQwM4Vg0AwB7g1F5FBi6YZBGkP9qhDieZlvA-c2OUE-hQNmxLSll6qNQBCQ3B0x4yMM-Vl-2ZsUC06IT9cGpqitD-eqA61pAk7Tt2WSXtCVe40Nb29oIdhJ8OvDT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJYk6aKu8JUqDHm40stSXhx0AbWdj7EA1XRpUhgeLMFjT7ufsCZvO_Mq39HgG-ejNTwxTpuXCp0PRH6qia1xLGxEcyt0Y2TJ7Biao2wAfqXhC0_Vfx0Hv2P5KYPQBx-XF3c4M-qpHDd8Ji_7kepqBfe4RmTdMo6oyyJtxyVXTVbOXG6JBR5Yhul5hP1evMMJUP6Ui6rezpdymXnh3XNtJuL32XXTduiUyExqTVwt4nwSq-nAw5ky96BBUnpDC6AzYr7R58uKqZ2KstmEzXdL4Pn-w7xebtZtXmzkcCRjk6tTlC_Fz8J5TWKnBL_K-u7ynO4IdsbmsJ9VtYIqa6pzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K3afJhDMA8OtQ-K8igjotHygfr-6zJqdfBsSjCWIR7-y9eXGg3AzRpgRAwU4U20lOqkITeKC3KwIzk4FCbTH2-EEkhQ4VyNjdQHuHiSvOw5MZe_-E01x-9mSfDrKJdkyyuWeNZTmEdQSNWd9ZMZik52S6fcwSo6MIEKOM95UScUL6LRY4okZNauxLMO5dopdWWZWSRWd1k_HrvcRxKusVvc0lQx27YFNkaw61CrEiD3f8R1kfbTDetvlzRJcGHgintXFGWvOEDnjkRmrQqhCwooNRGVQeB6idVyT98f2NSo-rMJfJRp_EwnWYdaRMFxHfj8RYfwb__jVlI2UjIhCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGWXQW2O9p8NBYHwMOvmYxIH6ocLciS3fdDEWJWXcQ6GFOmzowLMU8EYJSqVm_eIPVZoDD6229myeYNxVuqS_g5V58EeHW-ct52sjwcEpEVIkz76q4H2zZfZN3NZlbD2uTNrB5vn-vhJFSXCQFYrKSfQp-b2GYwuZz9UnoH1dNxsrFID5GNeXVD05f66m9c9rLDm8UObRSu1VlXIMjOTuLaOps2SSwd_L8LH2FShCEf9eP3jYcjz_6cGFP5e84mFL_6r156yMHYyebm0VKw7LhlZKb6nuHlveJX_HLBziSXchPDXTSAKJ2HGk5lQHBq2XbPPR9D19JZbqkipsIOJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YS8tDfg2mdidAtuWJdetlQuLMp3l1kFN3q72KvaOvm4LCT1t7ZrY7mEPA11juakgmLf9qh5eh3PGz6H2uSW-p-1hTmI6eS8ORroOklLj-KAYHPNrpfZ4hCbBtb3hSwJQpMO3kc82hCknslEzCYbq_2dJm8XvfNggASOWXSmMIilIfqSqa-tqm83eACOBrekAOadfilDruFXC8PbxfE20WRi0w0Pn20PKNXxbQYT2sspIl1-j-PXahA9GoBSTtYvC8DfUm44gP-VfhWxkQSyffCCpqeFN4zTTVZn8r4zyr30fg_izKGBe2oI26wl1sjKQ0WvhzFnEMLnZL7yRzbF0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CyM0ggzdAKh5_HyssgalBAwupLK3Q25SLOghgnJFuacBQRivGW4Vlfz5Wpv7I3ruRWacF27rPrwFEnCcBQOgqT8d9igBvSeYP7QPYtjTnLMebCzgEwEnC69L2VjwSS9t8fI0PV3gxF7Uns89MHMaJTbWgQXHe8Hwe8EB3kc666XUrjWlwcZ9S-0haqtPmmSBVor0j7uC5XHLRw6g_BGW25awIxllmUhGpY4mLUj03XKCR3iXEJqatsx7j5aEIm9BGsJkdz9fBGkTg4L9qG9-sLx4n9S8HsmEi_LfqOPdBk0fXBlEozUFPFiXDVtis9A12Ml1IWXlEQ7OV02BsY8HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMolkjeVXW96P_WINnmhV1Mbx5nw4kwPyoroxZvZZmFZWf12Xe4x2qXBYHAMYXdqeaBm8uTkc8LQeAhwa0Xh9SiWO-6IN7ESkmeUvrHTJlwD4wPMccej63_3zcPO_zwD7Y640zQyj8Duh1vK4zy1UOWdZbFCALDg8uKWdkqeYZz-oZupXyTMTzCQbEwgG5O4L5HU-nxZeg_U-HSWvTjgiE2xmBLgYxKcCsnt8ZhouswdTNLCEueAA5TZjaTFJGHSWa_beoA7KM67vDAsLesh0kN-CY_ALGQxlyAh3BRht2ijjrkc8rESVuZhNdixRRh2BPjwWzlTsl09e3TnmQsL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EuYdYOdzAaTYS1--SIpSvwkoFoKgJq0naiGlj-oSlgq5xvWDDLdFpn5VWj1ygG9JSYsRvP_eFX3_qyN-gz9fk5EAZcFIxn-lgw_lhLivzY2ZJoC8JYPlnPgvXBAWMeriDwU1bI_Xs8xIqQn9KWmwnkSrwS0enttFXxFU8x_dGchWimYmSaGEqC6iFvjT2D2FKtFGAmWJoNCUOTwJaodi6V8SWDDrN8mqJ83QyTN0LoUnJnULeJzU8MFfhVedRuSWHDa444pGw6izjN6UZhOX7opl91LlAKO2Heg408ICknMZpgZkiIWKyug1xseFlAeYyzqcHc6U9XKQH05SguoF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ccZbHSr6sTmTRjSkzM6IQ8yi41m9b0t9k-xjiSMU6fkAcD1o2GawieQRrFlvFLr4tFhYiSV1Z45T1ESe-fxzuQAnzJYlPhfWxdDUmEymET8pDTLR-p6iBzigo2Soalu-n2DN9WE2aS-gkNFVC8omrxHG7C_8wvGZ9pA_WF_yHnbO3tSYVPW4OtJ1TK2_AIv0JF4ZjKpDSs3jVEaJPrhQoPMaGCjlvAa42-XjWflefm1O00om_cobmAWrYhcjyeYc3rnGhhRiigiz7E0ESf1P0ehUQZmW-1SmQzBWF9NBnruPUZdMAmJ4LIr5D1pQQ6aBzPQakT5_7ZULLNyL7a5q7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cEfbtMpF5wezV8DGBuzpfngBcwvivpPy0NpkBv4vM9zxV6ZQy_QTJdNeKNcvMUH0BvvRYfv-ZBRTbqRNLLYF15a4F23mPjZTqjLlsp0J-bo_v_QsypeWmZLc69l7-sKzpIPNn10Q9MV6Zx46Yh-nWULkAwBb5UH8mrY09dmjo7PUN8ZQSsbu-DQFPLy15vwyoV7DmJiXoM6Vbe_HzKB4aq50DmgEht4vZYKCwM4fuFBkHtm0BdYRPChlRhVUtyVH5hxyeLx-zqeRHz3BtBx35-oOh4m5W_msu3NqYnWFwEZI9V1grNUMzd8pl0ouWstGEknxv1lPAyfitSQpJQSKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KTYUue0tQ8bY5t6Y1-vMkHyadwxoUmHH6dAWXpsws6VRkrwYOjmF1r_a3yYDfSDz4FJf4d8zlrtWJ_9-AfpV8MwixpJmxuzjd8iITk0bUNhDqkzcs6A9xXMljU00Owh1qR6KwbOiD7Rmz9hgv4uJTweNbbrkFWpVucBn_uX-qDQ0shBpR1rOUHnX999XZj3r0Otq7nVXOVfZOl2jSTN_zwMv5d2noveq1X_UdGjIFVDvus3WkhWo8BovqckHzml_CfqB7NlaQfyoZuFf4pBIM7ciKopfiD4lGTjN0tFn5OY6Ez_YM0lx_4xS6sHQ-E8kqR5ruEI-X3YiPAGVntRSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhgi0Qw3vnqgBjKKIE-FpWUMvxarZzPknjpS27IbMlJoei2_TmW4yIDILW7L_9JzpKRzcX1l-XO1zTGznpRIMKLauSi_MEyPkPMTOHjKuUuIYIXsruVOvE6I5Njs7J75amtp6Zp0_43cbR7jl635B_hmvMNO_kcn30mth36STbETN6bNZJR6yzA75pqPBwpxXUJMOfWn_RSyDpVeY_Rn-Qk8jq3CTPRckE2zlIU6EculceSvLyNSIxrQzk9ymM7ymBOrd8-kRBQ_sUVsmMawaE7M0sLIfZbinYbc8hucldo1Ny_jpe797v0thcGxu41Zpg2cFUOoHfmcYVSNZAibCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ngkj3EKyZNF7bS6oDRSnHUDFhQHhuBYN03R1QtJJGnFt4BaAGu8UhBtuvKV_VDVsllnTG9M6cO_A5ePQidxOgSSyfdovlv9-9uTk9ywJMjRwZ3o6eSLmqAnObJl2baXhKaKzI5snj3cJCwXmb5SSX-rk9L1k3kK5Nf8CsO8-3mq163YV9fQyJg6LHFIUa5d5xLqFXs-pHcn4P9AJMEutjf136-W-GsumbJI4HStWLyxRPhObmE3wDL6PIX0YfD44SeEZKpbJmw9OOW-sqy89dX9Dis5ez9AsMmY3RfnsnnWlI1XCPSiMU51xuahjUcYOKmREj0urunQEouK_pVgYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca5KNQSH4iadP6EC2bPdRjauFYgRJhM6DxFK3fA_q0ozL3ESG540xdOvbfvbg-bCAAQIUnrrCWOtKn3RYummSkYMTZefjvUtUYvR5dfGq48wjmI1L3bkD-J23RrI8kClmKBhepJO6iRiQGfwYLx16qFqYMSxk4Gv9hx1kBg9ObhGnh3CAc8ZraUUMs-EsKc0_iTnnZazfx_rDXAt7MFeWlYzRV6XeQ0LQmF-qkXNZsQnIXFQmpaXMj0yDmvo0S7fMHuIeFsRzq02t_3f_oSkyyd4gDRK1kDX3MqCo46l0UPITi_L8-So554YqeMCiFZsSJysejRF_iNc_k-A4ezwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fydFasBH_V5jpHgNL7ZNN1n0rOclomEsBD81JPqiX_SG6okeU0Bgc3DnUEeZn9yW-KoptQV63Vms70rt0xAGxGs5wvRnMVNPYHDUxQ2LrK1IfDmHzpSAtpDSdnEF3gpPEC4vdWBoUTqIrbA2FIRDpOCgnmuaaCrEA8TmaO0mH3L_HoWiVyRLw2rlg69iq00EiaI96HCFvEItBnZN94_KGaUKf7HjQ4CV2igPzwJ40Ag62TH71Y7E9j97xlNVvJzVx6AcMa85wPo_TvTATdUOYKqo9WZvoUoOY68b_7Sf_gGT81Q4CTkz9Ggd_51S1iW-CQ9ulKkjaT86q_j-m54dqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xc1uJyzCooRwpyyZLYrtJoy1TnagV3gAVgtrB9pSl94kPZSqaKq7y4Qc5Flj1G3oUiavrQKKEH1hBAFOH_DMswI5pj-WEgI-ypouw1ZVXfwPtMiFyPr4sTb-A5zsx0Jox2wjZFe9tRLrFL3bqbB3zxVlI_WbRduh0QSiRjVu79uFpIuuXyX733gB7W2jWLqYlOa7_d3JH8OO7ds29oo3qSwL7niS4epXKV_969pJe371UjRlGXh80mxv9pt2gohH3vDbhRFnOnDtHukIDcz413uXy_p0ytjbOrpS5q3v860XNAWcuMxlNEINS9BPVP_Djo2RX4_G6t8n21X49SB7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CWps1krB1p7Wme5YgVFTn2V5qY_CZzA4RRv227fjKRhy1as7OELa7FkBiwB34r2e0Kzp_E1aDPi2E7PgMDfRlCCyHdLCmU32ANmGn1UbQylclPNN-WjscAy29hntUpAfm2DeaQGXDh8ELJsAg8pRuY8zu7D0HtobF6eNKEsga5nJENmJXZ_QTrV1h9C1sYjdZ5c8gWv8V_LD4v8LTQuWddpsSzlL1xhiFNsmffCC-j2Gn8cSIhR1s_VHlRzBuxv7HM35rR5_0NV0L7zBZ-rvP72SAfVWDSVVdXpLCLHwRn7b_zkfQ1fLYBUSCeyJrPIjjyMe2tdx0sE7KFU6GwtAYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kCPwB5Nrgxr9GvvBMnQf_pU_EF5A1ldDUAYdgiLKF2ZR5jKzt5Ztl7jXh2YCdO2V4Dyr_h17PawR2ZOiDgAqcqDayVPMNkHFUGQh3fXtmNDJUL9BjBOGJ9b1K6F3zh1h9amvL948ekszMYp1juR2eFuEKyDVpaAzrbMiTHuFYL-lUjzXvhdyx5sAg-PL7G7Qx48H2b7m0yCshzcJxnKPOLc2eivjKuKvPRNS4iD1CZeNUyUul4nS-Sewgnzg84M8hh2aYPhjzrpnwgaOv1cvDStVyVTkE9UaZ3KZqLriyi5MyYKsZERlkSqGhit4e50_lQKb78RVHCCVuPGPyUXqeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uiaL-fJuexQOXShW8U-i8l-MWhQEAH-EAHgtbjhrvJpbzbA2Mr66P0VmLSnnYfKd6Gk-AnDAkxPkixp4Bw8q_UQermmUVoz43ix_uW-5J1yISh_1O6aVvZMC6CtSeO-weZNO7PKqGzQv2wnZu3eSdD9qKSCzretDxWndfLQ7QF8pX26_Yoh3qE_5KXS8VKc984hVa5nYoOur5jEtRw6GuTebDtDUk4ZO_Tu_N01Zsu622TckEeQNHk9xPwadLLctlt0jjRmevYFG8USBl-Uh1X2g6Fmo1cWMFtQ7Aa-Z5PHj_QtmiymAEEUScSuiZwA2P7xM6hJgwzqgDTbSv1QZVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snjNM_pt6TwTkmw6Ano9qZWstB_-5wmwzc9Mq9b9JkSDzsqCd5HvK9ivCBeK6u-MYhdLymqs2WIbhh1e_G1j-hxThD8JmY0Z82NeMB4feAAMEN4hbwow3XN4KLBoN333sTQJjjz1MEqBOKEpOMnH9JTOMC3EjowuuwNBlUFb4FdqbPqyyjEPzZXfWeTBk8ShhwSjxJgDbDEkrV-E-MvtPyptia96nm220AXE0N1K8H2VI5MgBFKVchntRalMNT9hD45uj5f5EBI3V9jd9Kse5bA2ZiODPgGSLkFyCCb2kXX87VZ4fKPi6VOTVxL2ZcILfj5xjxmQugtu5Ef1jWHywA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/useAtVIK-BqwOqGmvH8foDRTuZiBDclAuSxhj8h9kdAZX3CE4EjjUQ1eCwP-FhJr6divCjR4aAor9K1iZSZleBAOCLGcInVtIXp3B4UrQwUXWyPBm-giuybAQ1JzqLsWYlb9y91oay7MmpUXRiF7GgO_gTG8XyX6rzDvzPtyKdDyyzHd0gd_zNVv4tZdO4u5cfWmMOvrh-Wb0_V_2s28siuloV3d9hkjKcVN7u19n1lFu6UXaYpk1jEonOyf_bSZBSdP68shirA7A29zz3pnfrDD-aU3NYA9vDfV6WNIsxymvHcqhfcENkn4Gh0mS-4iUA8oq5q8lxH_wAIW7MN24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PzzURNLEkidtWaSSHbrDfoLxLrWOt-9bRMGNaxdSVa3OMvJ5CcmL7hprr8Zt6wY7K_Vi2UgQ1k7JkVW4GCq0jcVaIz-0uuiCAkd-1dqotGLlxKyQlS3IkaHyMPvCwpYlxU5Rba79g1mU5mB7mHcgN1MT9TfmyX7bWCCjeFcZhSpc1rb4SUdRW8RaSakyBkA3znd33-7yaWngD4ReiEmfNWnoR52TucQ3qBqMt-akH7ViIFVOMi4XSTmbzecsqIkJPtqx2hJHZcBstpKfxBPMTnK29icy1uOz__kyqK2QXZp_UeIpn16zjXkl0dtQNI_KrlVNthD7QHJt0rrLb9iW6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i4hAebhkOI080bTz7KTH7vXXnJgSv_SkcDfywtx0F6NUtnLcjPQ8LOohY0i3sK8y3E82g9KKFyjvK-Pr4m4VMfQ-_rMMG8Phgp2G7NF5_LWFkKdDU42mCqnnaWU-nnH-6akwB_1ezfDmetwuwgo_rU0V2g9PLShFPC-4wylmLlZcKt3wutF1CK9XCX6vV-k2YKGyb8J2sK853rK77SmXcmrrtRAlCYDbWub26GWJuCJXsq48F4DQfwXIZubln42JS17GNZnyfZXoRGdkr2pnpYGqKdBSX7yvHlst1R-tUGlAt-mdpLmKPbduA-cz1P33FBUNVI88coSr0Emkqm5Nig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DjRu79itTFo6n_rlDmAxMIfwKvoS0irMHHA8c3CC7tF_qov4vhMz_tDCKPT-iCRKkETXngg24wb9Fb53xqVtqTvvyokw9rPlhGnIXzFVKxIL_oiuznTwrJ2XgtZWL9SCbwTxQ9uESWVVi4UOlDAxEm-IfpWIohN3NhxyO2q3YVhwjtrNr5B3wkewTKL-ML_QuKmX3MpnClH1g1OG1jnmcGaX8VC2pVmnb85j9U3iGatTCEwqN282AoLcgYLdKYbDqiX7tnRj7cs5MrwhKXhcIDM_lJ7BWAgPEHP3yVNRpIBUALwDqWyz_9d2cUd_4kNIDu_eg-jEgwXfbdv-mvr3bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5RoUP8R2dNzdIMJtSiR0xLn9NheZfeqpCN88yvaNwzKAhToRitzat224xHIDQlAXhzbMtQwWR3FHjqD1dVDwvXA3QRDhcy3wpl__CeoFi30P7KKFKOsEgOMOLHO5nt-3n2P2J5fHxJ07caFM4lRy281zqn6noZ5uuQGUvt2ZNi_uzuoZN9Ei3l5QArt_cgSF3QQx8LuT9CH0AtEDddkMo52_RO7A1Mb0ezNInVDM7D5b17O2SFlQmvtH9i6HrRLB2zfVukkwjtdP8OA3NBlUdEUOKKHkl0P68NUxh0SrsfiuqRtwubCa8JfJA2PeIcUwv5Nb7NNCnpSwRAmtgfbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDCzmjKjruxCXIQ6mfM2lspg1BUV5fXYIAH-FLwBQxkTSSxFOSFfZwMY4Ha-CqN2NIrSghGSDlK80R7cTAiNOLV9Zr4beR21omflDzBNuQ1RO-TGpwNuQ67BfQu_AS8abAXBgH0Mo1VDwwJEY86-mVK3y8v3_12S5EyxLmS1xZ7cVYMWPyupKzhax4q6uODWOMC9vw7pG8cUMYUoZxDA2StohIeyDptHVerJ4F-rf-v3DPVMJSM81cAlKl1Y72a1yVOpPwKaUFK1K5yH60EWCYPaImU5gb5TZe3EjDnFLh6nPimv3DeusFgYiGCLctKPeSD23brQ2vHxyQX3GNCejQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vEAHdSBVMu_CQb-cJSPDOn20OsviNx10b9QcULlaXwsE9Y63AWW2QE8g_rh7HPaBX1P6tJUeH5uczwTaO4I1ZOfekrxqmIvHSOnyCOgDVlvisLVjrlj2fDB6CGaCFMHKag0Yx1xU0GlALy-8gF-G8LmDRWi0R1h4OlSrx4J6-FoRL2qW23Zowvv1LFQy4_sZl1pyGd7ahDMEz-oq6OfWaG7Cv1fK4UFp-VoxUl1fxmjoDxkLeKeAVehbwQdk8hHTnphjihSEvBDN_ghEV7OPcFc7Y0NgEK7sq1X_L25UkL64-wAJ_t5hlh33epGuXzf90BhIW2hkv2LtTuqMX57xwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XILZ7QhkAWg0C3QN2ycsokG037WmUnSuD3y0jZZjayzovQd4JKbjllbGcf0iz-yJdpGyqintaahQKJkg7Mca3Hms4fAlaN16aSzmaZY8sosD0M1mab9x_eGrY2rZskrn2E86E4VyjOH1P-pvUN1e-gPy1iXiNz-19ml0MAKNDo4bM3fL2O1dws1-8ugKmScz_F6ZV4Py78u55pKLgGaU3wQcWUTC1620yzWgl1cqd2qJh0Rn_IXmhfE1zVigE9omUXMQSTx5xPddtIcyykRR5bSgBVTu2ktXfnvcEZKa4YX4Zw1Ke3fLohjtXjPIrHErziiV8kPR8tMfMfQ8SJ7kpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ATFl1c8omz6q9HQ0NShOJTF1eJyRZjcB3m2GTwxEIZMI5BQUYfk84F2WqyP9MChvPjKml8zZJVaz4SSfojnjLT1iPEHQf1obuF2vKXcgcKQfqizBK6B1t1bhaZWO22RRuh97Of5ycqFf8e86LiInoFe9Z6LQnhjvQJKJygCVoI-Ny0TUQIGr3_Z63e1qJVkEi61tQxqfm1hM0fDUbynnWgowT8fQ2JBd68eLWCDGThG2a09C7mdomeiIEyTHMDy3T6KIGc_vxGTUw0Pv2H-DAvJw9r7eA9s9Ng74wKE26Kj6CskgK5edqWTXBqOzJavJdP0a_MlokYzZLCzLF7CGPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIe8CWS2aXopClqMR5rQ8WHDBdDoyJeDMlR3QVF_CSTTJCUuMZS-_GN8IzYlkuUuq4kf3gDE2csLfbmp7-D-_pYHWxon7MtnhY-sZPQvuVx4ETNsLoys0LBOLMWD2nCnd1DtzhTN39phRduK9jGR-WW48Y-XgPH4oWeu-HhOrzom9tUjcL5VINjFQKBNvtYK6AhgBdADyapWinJ6W2ULUtQMCgWazm5hlBxRp9GFBlqVi-iRoZMDvf40g9DyjE_zlrHg8Jghtk_rD1_qT8yqgTTAjalwP83naPDLEL2LHar_00hkAh0tCtcUsk4Fws3lsk1sYDpKlVBciDMtF6Dt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sUBX5gxqVZtccQxtO_zHJh92x_xvjjcyNSBPwEKKkUZpUZgA9S3W7FwDNpaQM1CmhdpqIwmZvDJ9Xy38s7VXoLk8n8gHuRjb9lE5IqUCN2BVy-VN3pHYeXxpJ8L7F5MXSHoNi5kIkvK83hw5mMdF2g4rk065MoHATp2FNzVMQN98y-b_AKZ8lVqAIsrUv0R9QtJJvKOmQj05HV9VfP1RvfiSzRECsqZFZI8dZ9u45lO8EXC9M2pJX8M8XBQ3Xh6BG8BTVZmrdYIlg-AmwF5O7NFmdSChtc2Y4rKVO_nZqiEWy38aEzLARlU5y__4MqzaiDLxnaxgq0ucyIWPi6siOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KSMsVhJ5P3MHrYpUdelgcRvt04GB2Ho_g5PWB7WKkVUKUb0gLqUSxgOcceMT_VsZgmKrK3pYn1Uf3TC7Dnt_UQvSE2pG9t_FMqIzaZ0nfnIzWMzcjrgoQEXx5RNG1s_q81vil4DjlCv1NnIt5Nfz7V3JDJtwhaPGMq-mHUQzJKGSu26ynHkGHAktZousmELViabDmZhDDtI25ZbLbvuAM8VU_4kDejLQHI3QG5WJniBpUAtrlyL1nrIPq7p-58t1MeoeCqCR1utu8VT2C2p_t1AETeb54RGKuRc7_YXr9ul1Zet7aC-jsmkvVdS0VHyrAiQnLRRVbdDC2lbrL7_myg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FA3yhD-LQBW9UhAKBfN4FGdPkuXZJrvBSkbgZ0JfctGjJQF7AmTJOq4Rr_QvHuYVchu2awRkOZr2gwQx9a55hPW874HtzC11YuSnFjn5UmMakHvGDk6Bw_XCqUKulA0u-ytqQ2ZnpWpm6D-s-8WAkMaDQ49455lgDwKBrr7zwIarbiZuUMhCqhlGg5CSL1FKQVH7NSARza0JqD-johIvaCfzabuVU4o5fVpjgbR_eqKalWjCx6r-jLgTcva7zXWzwnYiqIZ17GAevx0q4w6QA-fJd9KwmR2znHYwERSiWqQtqlm0RPd660_TnBDDULNYBMHz5AEl40cd7tmfEZGilw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tGzLCSY5dMHYWXnQEsSwokJ0kaKIJJ_2Ktkalrb6cFT0f_4O2XH9W2uHEzwcOsv_McZ2mOXMqng3ifTR69ePWocpyQn9MHDneVuW2qcoeO1bL6YAxE7n4OAW6m-iMpTqVChfYJpQDsjUyZZK9aFphe9JBJN9HyWJAIZSQ8hrQlKSNHQ3vXpYDlZMcNCblfEqycCfbZU9KgdN2dV64EYO2MNRRjhieyoKvlc0nV6lR0Q-c84wBPZ4DlDRx7frTCioBqsMJbu6QDR8BQqmQvLS3wBbsysI_zbJu5rKHarOvBaPgrI0FzyMMDYiZrJtjqbVonoCdNuOALXMY0rYScDZ0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrdRlqhhNpELIWKl9X5Ov4AaG1cMG938PA5HvuncUwIjfe1oJg2CNLuVcIfoyCM2uOWFXiRH5PuK2foIKmbBDX2byUMxcCYv2Ct0YM6s1sJXTBjac9HMj5S687QFwhct5oxcj5573_rJujJ-nt3EIXpuaYo3ISmgH1xqL49jAkWBllSsN7RLppuDwArJD1Z81W4uN-qpCnrsptk0VpZbLJrLIuf2o3AjxIhDUaTq47JEmeRBEzaA-jMn6nv_4QgDtnyhFDxn-k1uDSS8Rcm8TvgoUQMyeB0pRNMlQ7rV8FqACgZodkODgfHkn7vbui4hv0XKWmHVjQB4mesawnLbHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PghtWhesULofFI74gogUVuwrp_15Y0q7sSCQWx25zBjzfIo3zcYIlXjHxlZyrlEDoieT-LFBY8729pgKgHYsVgjYmTekEeCDnVh9xMMvr_jdCSOL8I99Kfb7rITaLJJLObSLWkyyw-sMOtTUdjjLEy-cytuSJmWHG5jmzt3lwyW3hv4HaTV0K3iYRhSoEqkv-1uv6PRtNf0WZR1or2ipZ47irXMcpybGNeHJapVuvGGZciDUs2HXh7jVlyMmmnrb4ovb0slJSIGrzn647Ioh_xriTrovhUXqsvegqC5Gb9ZL_dX1rBDA7ojxVl1Es4k7xHzxP1QUx75ngsQNxBaulw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BxxdcJX73fpE3AQ9IKy_3P-DmbhRXg2hhxOMSYUf96VM6qWJBJ61LmFMAd7LVHTmtQlhSEoMNAeazj_QGS93wsHZwp7Ca2gQYGsWB-s2-4SOakgSDDiwusRivv66u4VQX03f8ktOJUrCO9oJRGz-S5F8QWn01pxdQC0TQl_VbQ0hymjV9tgMz4dQDyhfkA0pe0ytcnVzuj4rXmX2TXw8PWabpx37_p8J_OfONQCCCP_siS8GS0_PaahKS7_VWRTX5wSmYCq6t5Zf6Tb_dwYzjQwnKvC0dyQAfuk5IoVZmj3VIL-13YMba-2R-z3s67PPIsX4eeXZr_XxSo-kuqjkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b40bUTAtEnLfjnN7Jv2I7QrKcTIASj5i8_cCmTDO6cLuWErF2T-6SzRZIsz4QlGpQLpWWJ91k9ZB2PR85-IXexbkfoxRoyFxD0osEEslDOKOxEucM1F_zWeXz4cdM92wPGfDTTwcIOMcSwZHpGsaN2Bbt_GPhSTFlEoq5azBzpe_QDSwjxGpt94lzvPzM5EQ0ovuG3YXMNMlenEZqH6ekbMGCf0wASuV7YEMeRA5xsrVfsnaNTG5MgWbnQ_QMOldNs7YqX1w_9KSv7u4BP60DMW6ew7g4vAL2Qt_OqknqFoXmlxX9HKmmXgb_otIcJpTe7VEGrQlb2WCBOvbgzaSmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A5vqJEI7TGObD3eNGHWKFMnZazHHkWkpd9_0yMi3chKAM51_V1qH_bg5VGUgDbvlIxQ2D-i65csNqJRGIuBfZFjQ8obsDCk3HYQ9emw9Vwb6nnve9iLlD-wHJdZsfWGryw7bkN1GtBx0v3PI_MbOKxC-J68sFiWkwQuApaKTdXMc7jlYtVbshcTjc-m3XEWdNuGDKgB78rBYLhndKUm-W-xeoDVbm-0fAdvXa9RRAdsPfvpQZzob9rL8U0iUMNrABgccb4MTfY7vxBVcWiZEvG-WpXDRpQ_1478KGKlwMamEfbuyq28wkthIknjmwm5TygdNzIgdQe8tyMt1VcLXzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LypO7tcM_SiB8EZHt_piETQznABe2t0g92qomMAzNVVpKNZnKfWsIfuQqBKfYOaCSk5qWqS4G6PDWs4ElhnWzojRF98SWraMJYUKzeZdK97PRtHQWR-9rkb4DgeHemL1tTn55Yj0KKRSpmSN3MA3IVL1StjUaEpRT5_GVXJSBdDpuCjtv8dzzstcT5kNyynNCgYdtHd0_WrjUVOv7PqluyhybYnpAwU4Vj1KjMJdS2SeFf6jFbccEdm3OX8CdGCAeT5wGcxuPcGJ2Vs5ofPrIUTdXZTjqSPUCNuvpgtKjQqv5RbSE2DNPPm9HEIruLHSodA5ra4B3O6GOj_FuZDHuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DsjShIeaQ8I0G8ziyKXtFOTTd-T8F2EwjXU2RuRHoS4_vJUxvS2ouOrzckMC-MFX-AwkkkTek55AFfWje2Hl5aLnNGxx01k6I5zjW8syK3Tb7ZojwdbS3eNlXKhKLlfCHuU0QyHAJD813L90q5AY9J0PodnXkQeNoOE1Sy1LCAD0XBjPPNRugIjTduegb76hm6nFJctsYQgfSAAlxj720tNCRDypj_oncUlMEfyHJxXAoLFd8-M93zdHFfr7KtQB8HM0Y6syoIOT3EQaIKyqExk3M58rW8T0j6QDSFB5pl4kIrfFKX8E9-VcVvcB8fsn903vlMvacOuHIvvnW9cvag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNSQa0L835YLDxQlkF9IUc0j-ACrSy0bO0g5mYbnDUXAjsn8sJUJ9EGgSGGPm_4ny0OfCLhYrUUDCXypzpQoIR-cnNza4LzYY300iEAv_jzLm1VBdk5EvSXz7UCvvOCcC60wbyg1IhPSDP_bkWLJRDNJpsiwMc5DJHoWUsHg9FJ_BcnsBvNJU6G6DXAloMiqG_ns3MG3WlVxnDhNt60B8iGMMQTQNeZUkN3vGH8QFDLZfjNKKxXjFolIcnK4cMIabhC1XOJbuBZ7CegFMzM242encgmRava-LHKUdYGVTfWYLzeLXsR7s4mhfAVCoGRdpWwk7eYJUBmgweMCFe1dHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b4MBgmLkanDLs4Zisbik9C5_rNvKHJD23W_OzEXLVv6P8bAWOWafspdUkdLoEP15-CHdaO3If95fs27trzoIzvriZ08GCG62QiFO247Dq2vWcTKtGXrDOQNhC-pqrbRvkVKhibnGCmv-rS-mIuSEg7Xokz6n961Jvk6ZFBYg42JO_gJcP40PEEnwvRzDgSbszNnkLx_hTS7cxKBmjuaERsUqzJB35VMVQ1YxydAanLmMdKwJerVOFQbsHdrjCTvl3w5Cw_LHz9A3WNZO3LsUAI90b7c9-58II2OL41I8L13uQYetLvgE_QpOxKYUgSpwZiw6GOcYmVTDw1j4h5Pdww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RxV1D-SHa4_XLOPKOw3RlsTEZxBcqG64IqdGFqsF0o88NXPEuagmWqKd4D_ltZ5BYYVMA34gS2NynoNrdfqpuPNgWoxNnEYj1q7bAHnz8kr7YOP5tQf_5l2UqwjZLbfRuuV35-HjW5UsLKY-8z7EaVG19qye6WKwWDsCC8yQ8RRoOKfCnWGmsDddUVlgHfxQyWpSaPRy1W8F0wJE7FL_iNHxovIebaPkrgMX40lKnhyqxMasZENov9jG2y-nx2NZ8_WpgaghbFrkJ5G15kmt2pHXwyQPuvLvvf7BaQcuWDb0qvSNeWU-yYPP_cjyAWIwbwwkPKg-IWNxWzsd8jYnLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiZW1qnIcW2vp80TjWBRzZW-_qphCTv7M3wMHfrIegJTYaDNn4AWjZ_X63obrnjjw7tUqpgWv1cGy-9f4v7eZCk0p-R1dpVfPvdGHar4ghI2KRXGsFAy573wMBa1Ofq3dxxLBM-P6ox9TnS6c-kucgq7zSUnmREGA5_H1HrlNP8Wo1jepu8P8g-e57TIeUbo9GNMQ54CYXu5LWI7sQOFVrGYbrTmizSjKeW6AEjHKi6MW5XItIkALjXtsUt0XssdMLBJ4EG1tEh04WtqOXAPvSaGCS-Y7Af5aAsrcD_mZsvRMytGSWwBCE5V5UPn1tciAAi4Qfdu1cEyRHdyCG9gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NanFxjRMIYw3cgHEDDUcYcmwILyVzXX-btNp-Uo7hbsC7qqqirRXxJFE7LZ7sxIseIKVD9LdEhcDLqEQBmTS_0qrhbZQjFHi-381FnNNr8TlG8sZqUJaEvR8wlptD9MofqxFVVBiAMu7DVwl-so_RB6wCQVQfrX6niZBdgd19GGQ5BPoeomsPl_3kTIJPJ3-vbzRbpVYq8CCD5cfW26tQ_N7YtmXofgfwmptIjbdXLBi-zBIrRRWZGF8GAboVuSmzuSENSLBL2BxaRKndh5LE9Lc74uw_vK0FYYyBaE5JFgif693qEgB00Pm6M6-JmDRm1tWPydF9zBw1jMPJd3m7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VewZUSqrWCNxUluOKi-Ujco1BEtSM1PcRhlkS47WlfnZovswZdsj39DhgbYbaV4BOmnupWhb9CqKy8S2gydg24zknlOZe-GGpPYalZS0rpKeMMfoqKw810ixBO8l_z05X5S1-K3FJCWA-YKd3LMl49UvF52gh2V4tp3TIZ1t4xwB1IEkMPBYxQaeburg7PPocYwO_cV0vMEDwehQOpmCHLaG_aEtnGlnhhFUQxnchrxbgEI8yr18TPp6WVBPl_deC5CU4bZpfIhHEWhTBBneP3RfutgrlggkFnGYHw9HwLGm2Ka6Zl9EwHIEiVqCGf-AbWVM7ferXHRaa93tCHA85g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSnvAQcETQkVdw-NRJTowbUkcDwKNadoOhcMUwmirUAPS8CeEoCYR47AlZgYR0828TOb-lQkHyv8wrPr74K8ZnyWgi-BvzOoWhF9iEvDPEPOIXZp8bvCyLgy1uU4sDOCc3kR_XEmQNiNwDZOIvOFteU-XSrEPvzUUZ5a0k58XBab1GC-gSxXWkwi9DuyhMwvrdAG4nwGSXL5f0gOcCohUxNBJxuNyvpdHUgkOhyH6s2HhQGBsouesNeOCKu2_C49La8Fbcsz2wtjpDgb5lc3nJrhJhuJtYDef-6BRnIiE8iEp4xBY5rPAlNrnp_CelogTnuZR-D36nnPg6CVsYE9fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0JAalme4Ax3XX7roMIkkBE763UF9e693xumK54fh6qpxEJ40--r5mVp5P0v17bDchGlTvDW1yYwFLsH6_UKlngyoIxIZmiyuunPwmx2zWsY2WdrvT8tTrUeK7NZrDm7X5y3-m8B2Lb4nayg3xGOrxyELefJ3Ph1Upn4cSDg6eT2My4iMQLixq_Y-gL30yjhL_hcDIh2B7C_0No8LKAx7eP7cvBgK0vidmErUJC9cC5xRhVViNU1xuk8vCRxbNDScFRYWnPM9K3T4rgyKCkXLMUWlA3YBwa85-vfoYb2Ovbge46jTy2WOouHiHgAGOyYtLcjYi23zy2rT76WkOK32A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bOIe_FrhmEoVrhPK9xkXrE3Ph1cCA4cEDJ9EHb9ffLyYEELsucZax-POvAcZUuA_r68dqjAx9nZWPEcxiCAaz_moisnfQqx-q3d5WkzmeqKvYU9tXbpuAO3Xfx6kyLwAmUQWgNZQq_j4aSn70BYDtw8LDgkFQUWahb-pS27M2o5G0dcdGJtrgZ5u9z7sC2y0WEbWySjVjem1tkAqPVBj_q5Ur5oV3g3lve0a-AosXI4m-oQfvW_VsgpKpMvpdSPetEJrYwQAf6xKRBtLxW0s8wOs4NbWbGzEzs00nEgrebRd9K9J68mEtsrSNWLTAg0WBTMAO3ooIuDGpt5EW2zw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SusC4pVMyXogkLZ03t8avo7YWTThc9CIvZCbVSzgIeiC_3kyhGh9mUPqnD1bL4LU4OS5B68GP551QOqN9o1qgGJ7zSEx3M2vDpEeQzpyfQWR1zqtT_xFjUEEwFBobquT9GkmAg5JpppBFKbfB0YPwdwAkWB2Frw7j_u2jdJss3TnDc6SORR3UayfHeJCwRZQvhlCHBBvNnfmqYY_AasdoAAtM_N_XRqv31wgZuLunh_oqObj-a1I5lFttxoP5MhQn8lDPf7V52OL52KjBfY1dNP-zEz9AhM6ozN3aA0uEDbGzTh59iI6rfvJLbDyqEknG3NW_DMf84VtyIKtwspOEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kb8iMvrRJHgcp35qj9mTQOkuILPlPQr0-rhPoUU-i57TW2DVDoiHSWjrBumYnMTgkYXBMewnDhe5MSHa0bTc_vg1S09NfHB2AHsmbkDX7YWCJUi8_SuQrbJRXAtJJfTpzjZ53FxC2YrDI92LARBLKXj9uYHEw1knA5F6WtQmr27ioinvww62ma_tcdbcHLL4ruH_PRKM9TBpO7IPKBJOBRQ5iqkEz1pUTC0PXUCznbjP7O__EHXJ_xumWFxrRaPZ3uWED851MfIKFXrsQDSIJ9tjpW7kWXc0eUAa_3-2Xf1LJpjknncefw0q1_K6vcdmDFNI39dcnRl11ihxIN1Fbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
