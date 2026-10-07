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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 06:03:32</div>
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
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNsOc_Nugb9zJaACVMmr0ovP4k5CR0gMXA3fSVo0WKVayYIP7cWsw_aKvw86jSeJICoGTX8m_9LzDeM_zHSgF4w1EVSmzuEtEm8hzeIvsFD3SVj43YwMyxp4gY3oTRdVkz1IBA8o7sK5uZI-0-A4b_0lOiKcgy8PPPV4JnpLfZPYx-MzTZjppkyZy1OY9HSzIod5K6fiskRntC6Jlq6ihA4IwFEsiypFCVmwBURnYi6SJR_BDzLzVblJYlB8NLMW2vSptLiB06HxB5Q4vTC134iT6LDyFaexoPAcQTdSFRwejBo3znrHp52rp_C4qKR1rQUc8PIIuXl4z9mjU613ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U31aXK5FejxWCnA478a5tVBQGpzf_tGgk9peiNJhTJdMa8Rc_xyOY3pU3S4WeZihaZF-xGBqtRoNgDES80aSDpQjJ9UAKBCb8eBBhTxcVfyy94917kv302NBkuhcgG-MQRpmNbZs_jjXMN4ITgnt79taozkwAjAXFtWy_-NeRWX8owatshv1k-CqBhGh1doB-1Fy10twq_ngAsln4cZz7ndZ7yNHAlmuKsHZYKnyXVgSx2G5W5vjdVoHcXVCoU4zi4a2JSVPLMsJYH_deUVzJOcCd3h77Vxhzb4O1WoPUv46b40leIybuZvDDth6lUQmo8EilT-dla2OxIQ1XTaitA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pdKMLlAurVNTcV_UVn_-wtD_PFpyKEWvyvbWe5Q40vnBnFfaUB74UfeKyLthEP4k1jOEj81lRE75l0kh18zWSOaXkZRrVYUVlZ2WuzTmOqrVY9tT6kTP7Dw4CwHR0EZu--_BEiEzAd5p9i5_udtsNAsHTEMoRo7M0xF3htT98yXngq5Zf72fNhQOdwr9zMpOY-ZdojAhrguo9Por0DuJisY4NLU0jpqzgzNaNKpyQcHoQLuj4d8TrR8g6kCTMrkwYyJ-eFAQIMGnRmarfNIG96c4r1ruF8Um3qHDeVf73ARWyqODy-7FruRWQnY5YUFlbrVThiQXSC0htz5ndYLINg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cl7VWcreCBP1y3X6ZH7v_9BxmJCwFO90BXM87V6afLJ2hYTU-f-l5q4vDDLDN3Bdt2lOGZ3hebYxcjP0RDgB0PX66WEb8bn_gbJSfbCIPbLYMdlCLA_C5PHO3I9KpF1A7MnRzvc5OqS2w41KUizBVmR-eGIWetca3a-Hm6aLaCjHZ9Gie51rhCW5AJizarXT3sSZm9Q9_TN4SP66xP76cPUbWni7nMDQl4l02NfJzq2CPTkJLBT2oxhBfUb5CrGsjfZ6G3tAf0yyyh-3tbo0R5XJDB0uNcOOnOTvNqq7Jm7m_6Rn-MlgdFvsF3g9OFgktmRoY5emmPblMDd6SSTsUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LPuMXwdiWfmwPF3Tn8diz67NGYQ9atVvSLDaG6IuUGlGqkfTW4O1kZjnhfotbbc8ODfacfwFu5903paJmpNujvggwy0p_xXe7SAPN1PfODrMQijHQvC0xepTltBbqnobH6tHJwwApu9Gbp2MLXnZSehek8S8aaJOSZTlSKrngGHfQehy_qsDAAHpTIi8x0E71TELC9RH5tYRKr3A2n00cwatu85HfZ4kYlSpvGA-wqv-EQLWhlFRbonOBjNSPHhThZcOMGL3fKCTLhRExRzRd2A90zTnuOAlKEPW8zDckLbhUmnws-0F3kBXPsGa5evNRd-LdKpGEihnpIM84wdCOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBgbCK9eRfpDhQ0nf6I4ykdUKQBPrq__Q4FcNGD9vJ80550jdAgaUIuI8poZdxX4p1_TCq0D25kdbMrjlE1lBfVBUAqnAtE29F_RQBNSe48p_Np06pzsvd_hqkiUj39TZs_Vga89kvSRlaulFilJUUu79xM-CIyIctjBiea_BDhiirGsT9Mjb8_8LnHUevmY5NzIdxxajKAPdEj61PouZ5Ki0HH_ajt6FjDoyCkQwiTE2SHBD7IoQPkKJ5bNo_T8LV31YqIPwNUo4WtQXmJNWIu4zfzDirDmdipdHMaB0GkJg7HW0n6nZlXkm2rwpX0bHek7ayPK9rvHTydasad_BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyHo82Ew7SxIB4N8Lr6b70dpczqWeqA9I6IQZU0RN2TqXMX-wk4YzsFmfw3__u8W29sQcKZ_4YhzS5H2MUoKze7O7kcXu5giHwZcqqPmXPTzMAC_rh10rPgu7h0jEakc6IJxJuJbDBI_klqjOCMuOpbNkeTFgT840mKXtf1lvs6PRXgw3BZwI9ZUFssPkhZe0rQeDSBhLPa4hlXVfRmGxmRi06XEYsvycu3BEiHZ1WsdvjjF7Op30sFPJnqkR1iWEeScF0iyeuLjCdO1ZAt2VRiETBzecfLIlQYtGO6k-GUWjMXacrjjnh0aAA-7cPZzX-355dHZMOYzo3hmUFPX3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WeoiOZdRq5JSCf0Xxgr3pe4hbMEeRQGkLHsonm_dx_1Llj9bmJ5DJgkvYcwkx1_fKFl8c7NhObLGBXEaWo7PzPNtJknDoHu3xs0gA16GwY2QPrUuroX6eWRN6Hhni5Rs81m8mk_02Ul-iCB8tK1xZloyJoIyzm2KgcZdw2_pY-TV7U9eXfGHTkVM5086zCeTgFoN21omyuIOYznePxJyhHY4ZZ7lLEQo1YB-slghUQ3Z7Nu5uSMFD2hwTCGKo2dPDUA512dui6jhHU6a_slDHwTYo2YLt22nPKMvocr0gskfNXd6L43hzLw5MOaKAWNYUcErBIKTTkfNBEQ7xDknnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uw6pO7FmjTr8x9Y5-2tGO0J4zTILNYze1ODVSJJKUJmwGKrPVlnXwhWHMrQ2ZpTzzxNXmpdk0UXZYyM_dRXGI1H2gHmOFL9-P0kcCOqP8q6AjQmnocBNlYOT3qzDQqANSLnvRPOIqAhAYt5fdxjgA3X8uOIfJaLAMsqDd3j6lWHSZczL0NCGJMj0Cx0_RkAIC-B0nbKdzWLQPR3lVnKu6c7742XDb1ec2JQ3Zthf96Ro6NkeaXgxwJ6xLMxn6_uHF-whzDWqyhYXUJE_BnncjwfGR7Il6XREUdlIvqGbalgoZ1VftDP080ezFtBbx2qU0_LC-J4W08CFBuhecPmoDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tCvTn-IYbtqcznJN7VIwLgCl21ZeE3lRUBCQfGc2ISlfyLME-VrJYdfRViZZBwS7dyej6Xsy5O0xZ6pwNQGS5vbRcO6wzpzR0DqB5gwQpT1oxX19NNYExwYI7n5QhOOo_SZ1iW7_4jn7bpEkgE5z7TV4DLbROLZ1aijzy1FpdJ7HUn57wM6YiIWYmdf7rroDELU85pX3jKypBZfMfVrtY2SXsjT0YzQT9e557aTUrzsdx7YgisFNaPgY5ptLqGUomGSyrVW4yRPl-y7DP8efL2DkD_Xl_h3hQ4r9kqDxlaq9jMNNbDpzZbXBgKX13TmTFSF-XMD2GE_EkcBbSr5HPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fNKHAx2laoY7ZNheur8myZpR_W75S6GqJHn2mAxiaSi5nX_enj6T6Wj_geg48mNe_EvXXbx_U8cvz98y9_h777iZGrYYue6pFAVOsUDc0lYP85H6bpnup23YNN4zE-npPyNbXfQBL5zS3m9ZFWkeOTnTpsR8ugzS53EeOHar01f-fC_sTL8EqScEArbv1ri0Y0XJgjz1SY9PX5I_20lSs9zwMYT1STUsFyTIwb5ISmgrEernmLb_EUfOmefA2OvZhNPGslvnJA1YiSVoAPcyEjPEmD0TfT-dAz9Bdjht5J1PiNlpPgS4fdV0tYTqk5g74Hgd89QXKHAiZlKbL6nZCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrKyUeaYnpI6jnbqU2NMYiARRa5e0nIKC7UvuvOmcLUjVZGhi1plcQy6JuIfHnav7H5WhTxAHYkQIo5NND9t6TZLcSIZbwc78FNjAY3y3Sn7-6G2QvAMJWf4yjnAHvvWTFDgD4P4ZjdXy7rqgMIXLtSmtYMzxBlWFbGuybF7WvqjOhBPHTuA4uX_CaZQ5alC6NN9iHikgnu5yN9xsaXiMEjlkRpg8AQ7yh0w4lmEybYodkCbJeuHBpiiwi1Z2GT7VJTfatJZPoEFNEmP4l1xyCnKEjk0vHRPocDBkTLDsoqp9I2-rgAFwpFDjCwwkatIng-eQ3UpPD1wF1U43FPN6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNjzRCaeoZG4-YN0foTjWUfqFhE08h_3VagWMhNopBRZeWP4-l-YlfGeHSXCAv89IZz3y3dmhEm9vdeGFpc5xACBiZjnP_LdIElEWWM3ST55N1Dpu7dWpwEa50Y80RT5iU24Ip0BRNiXhAVWpWcteDHoxMFUAXbAduCG_m-IZ-kr-ad1n0pYzyYa0lL913rmISTPkBSaQ3A6HMSulezRBIMR_fosHDYMYAZeJLaHmuR7OC79HVNDOosejJCCOmS114ZriDo5ZRxwJKytU0OY85UqBCV8NAhNn9F3yZrHxCaySyU_mjWXNQ7wpq96jSLLpowo2rg7mGC1X0odzph74A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/afeJlI0v_CbYgBou2f_FjqBd90YqCkzZ3iKHIklBCsgUQjxS3g3sT9K1SDI6aagX5VttEjjssbe18jsIl9-ihQGXCexzABUjIJEaij8wKIz4w4jxxLWkr9jCiDVqD3WnCxMS0aprvYA5k_9ODTJS6X86gVAAh0IGp1txmN06fGm2rUtqB_bLksDLJ9QDklW4MeScExs5UBdR7fK3cCzbKM_yO3ReIy7r4Pu3Ymtyhao_3cjjqvVjZknchM8vkaZdXtktY8KUq-AX6BleAnGtaXbsxy-qIGBW8-9t-kqLyI2xWl6UzlJUfB9naC0LRBMJnhEEYImyfq93P3gOrE_eTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRWn0iivrWD6sQt7shW4g_AcBpvWVB6wNxv4naAijlGsGljBpeJ8Ap_-RNPyY2y6puyuurqBcixaaUvjf6twrFqLsHx69i3SpzaF75ikVWOYvyF5OgIjYQhyoW3TssXu1eFpQDg53kIWd1fMWP93QbtyViOKXVMo7iSNqC8QCq4ZLz8shuaCYZZydVTePJE5zJe4klHL4g9RVJj0HxEUHBOgMHbGAKDKDAKOk5C57We52cXJ2wqt_Qx8wxyfmL_JSvLIeaXHKCGFBjE4daxIbZg50BxJ1kdrgaT4eYgksLGm8XHyWMGPNqdwEt4xzxrPPrlQVtMaY3ecX2Zms7rFOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4SG8tFuy28yobcRkfAbCtvz6g7aGx_K9_zb1k3JJSDNV1nUXAz65O1AyVb63KlbILGanPM9aERI3L4JPzxRVeFpAshHq43hvDm6g9wMCcnE6ICHDfyjbl2jdc1sIM9A1osYIUdNEZpgPKYHNMylvQEz_c39JGiPLeGBbfhwH5_q5nGNAckLQEfXgRT0Uu4U59oFf-PmsiMNd8pfdOz-JmJ5N31XUIs69blWJY5djla6b6cb3Q-UKU741nr85cZuNnByHJqvrC8hrfnGWAC2-yLxUTdxfI-aH0FQ7a1NQUpoxs-8XB39xRofeqXhw4ugSANnkv33tyIyMWeay7_qqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DJUVSayzB3xGVbdnV_P2qPZbXbD8s3q43VzbdLj6MLsTROoPkzX7pt0bJCEf5-pLQ66JcgRLdKGc6RqRFqQCDIQRu3rvOyY1adduhFlQPzYBplVKHTBL6CyqEAGMX-5ZWZjoD8kAIPENjEH8Wz65hUP0XjPlFqUa4DRlSJzqaQ5PcyBrZTY31ecnXckJpU4Un_zUtTbS401lzQo5bPfZsuOXTccr208kNBvFbOZpFODMUBc6bgIqiddjXQ-YlHF4TarvGyLhEPgyreP339FI0ji7E11ANo2SSaKXMXEsqe6mn0AUUG4xmpj6nqk40UY3tZLMxwDgJywcU3C8XKXU5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TA-besmysrf15LwTW6vJmrLUrvcHkfMDpjWNTke5zjzV1jG0iDDcoaj81nw2BHz75abiL2oN7POnGkVsPkK5rQRDAWQHo5hqRIvhZWuv5Rc4uaKmwQES5yOPuybuOMbZiYhioIYjUe7KQhDvmfHBpHGILE57WNkkwE2NaR0ODzlT1QKafHh4EPiLabFcarpfm9T9UVdUyAb31ygOwe8MQ9fT3YMLdNkxMqYvIed25yHMrPw2d8M-aC-FMPG_r-nZjavc6Tgi9tK1h0Rud1c8BObnUufrhQ6WaiVbO3kJUviq3lAt9UUGJn8-TOZQuGzPN959KPk86sv4nZmknbe8CQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AUhcfdT2c2AYj1OXvTgNuE_128_egaxsUXRQ7AgD8b5cGRove7aXGYS1iyi_Yzani1ThBM6mjyvqU1RSGWFf2HzdjbkGOexHAm80_c-x4_wpWLVVeO-ph3E67Wc4wIGCTGDdklvJk5A3UwW4En3WF1IweDtA0PT3dR4LZ8LSYfBIN718CJzseTAsiLlUo9EPb8b7B0qcNlwPST_Z6UdArxfBDqF5dZ7NtMYO7_ZH2nPMxAZ1JgVcuOXoRfA8m2V35uJ8Qk9TlsmwFuqSmEmk2SOuwcr1oZfjjXyg4L73r5hvJbL0AjAV7CTY0qruS_SI6t9B0xbUOH_-ssCCfgmoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZTb846cyTR3iuDNHQMfnnM-J2JFHxBDUgHdGTEOv6RcopXHUW8qYttq8UNU45dNXsqvcpQBDF7gnzpwkLVkqhtTpyYfV7fXAUrTc7rK6WAhyUeAnihvD_QX-a2J8-Q6gVxo8Psc1ON0SPKx3Cwq_D2E3BxSSfGPp4V1DNDdbCIojVLVaw2HKFwieax5uhK5KLGxisrZgHW-sqCxSUMOtQUTABMYlaCvwZjg8pMXO5P_EK8IYemHTAsTa8NoafSeE0nXlgGGfGXC5UVaj3wGCpyBJFoQwYsw10h3G1Jp-UlccyIU-NC7oe7zJTCZEPfj_jfOZV1vt6EPO0o2JduKEeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GZMk-evqqRvL4mKe85FYinZQlfBjUC65df0upz9tgLs6O0p6-8rBkZIBmF52aHLSx4biKT29G18jXGpfUhfXpO0T8_f-dkt6NXDowcCNpSY1bwvTJhNm92ocfXSUdYe6SI3eMnSGuER7cIxYQqAHt9eVs8Tfsf-fbyxipQTCbbBdZ3wMg_ZULwPNtX6aN-upSWdTezDOpD3VKHo4FzXH4VZVptro1S1TPtOnW5g4gkGv7SzFs7pOpEaOsKrhRff7cSyrk0tT50PNNyQV8jS2-cul1P7VDHj_XnbQ92E4FftoU-nqeFchjIPRvF_9tkTFwHH6cgr3KhxHOD-AY6HyyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FTH3apw4otD4Tjoo4DUeky0pdtiCWuk8I2OrQQ7PScwFuEqrfCiN6Siq9cXTNJOKTjgvoHSAyWP_NX4OK5UpTLXGe5bnH7FLyhNoksgHMl2uDArwiMsQq424hNVDtrubzSwnTV94cJWlut3H91GIGb4HY5BBqR0qYKEsotmela1hOrXiA4A6pKnfGlFvsTFDaaM7Gfm7ECdLGnz-Ls0s434X4QM7wQvV98sYcfe3nL7rSk0bylljr9-s4BdhmeYOdJbTNbejhkYxyNOfGkW8sHcsgh_tAixEokQ91sNZUm9FvmoVNlwU12Q-QZSuX_MsFU8R9q82lYP5FsIQTNYSUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GCc9KbfbGkH-WFCnpCFR2sulOAMQBtqkgnNnW0Y-fycnmaen8VDMmWvSwZDwr6nxvoEPrPC-zeriVHFuIVAxXOOLZLPwISuL4KY7TPlCk2YQsOMNxgRmujpsKkY_Ht7coSM4W_mbFh7n1mlex2QFNBCPUs0ssfIYxiCkIDnrORap3Ez1sVDSG9DAUoZcbec2ISzeUIWUP2o_Hw3OE_PXmboWlWkfMph7x6SXTLMb4Ywzz2pFh_yyFXlFpxPWCCGBGOVTfNBj1UX7h8QKrr49tTaen1QBpXrDHvipFAwZEOQ76tkVvI0SVwKZLbXpC5ZVG6vGdul1o_hjCPl7hioanA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/falfzJIDyuy5hzAao1aR-RAwN2o4WkjlOY2JCr3Ym-BhyY48uVdxT7ZDmLH2fgYB5OmdqVHkWsR5d6oqfz_CvZpV-hmBVhPh0tHIkf_z-gkal1BEhwMnilLBw3OwZBzQXOwxHutpbFEz68NPrAaY8RPXZvWKkLcG3M-jo4zwFBnJzLzPfUobGg2SpS-m7viQmYY4shAFe6L1y81oXH3QpOr7dABoKYaKqVyOig_TFVA3YcwyPXFCZ3paqvuDdIt1bXFwwv2I950hzXtnJYtGMHyiG3BbbgvOoNXqe5H7lPEhyGMLz5RofuAsZsF0jQxDKD-YhwUCOEhTTQXl9HPBiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Up_AC33qPU2rt6BkJojqBh7UbX1z2-e8n2-hfKoI995LeLCyPqUDLv1yei_gz8gDDcEla2vTRww3NiP4tXPYJXZmKosu4T7Rh1Ebktw83qde-KnLgvzigsvCWmw3KWlYV852YcZFqC6V_oe3PrY1QCpDPu0pyyu0ctPGJj8XDWpkL1iyKcucKxF3lhtAdB16JM-djTNXpkNAIC4lzqk_C8FWYaSRVoF2TFpRq9Y-aZ3Fxkx6VFz6XqZGRnz16olOW76B_yMNPozGe36xuK5S5MaGB3jqW-fSrNWvmiimxyWfZbLmPp24Cy69jeqRVidK_AYbhnQNwZyXG3HGcVLuAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frzY9B6P-dmLteAZrb5igvIrrmBI_p9kD3kPdLtuuLb2n0lw46KP04X4U-i9R5zv6Je4UpCqi35Wej5Wy_3Z8o9HgsWSZQVDl67n3YlZJoo8_TYP0Yo3dFiWLTVAefpWScPAnDQaxbL7p1vTzWPVVsJr_zm87_jRytbloZ8vqsVzlyL8FyMv0OO8ppuS-h2WuZSSm7HaRosDzm4MitgkyRFMFQXEIH1Cmq4A8B0pBfwGY8lWtUO7C8SgMNIBKQujr0tnOB2eMaPhN2zPhDPl2z8hOlTKV1DNt_8A3IFCDRs-P8BhaPdciEXx0HwaAQ2C8-vnW4pUbiix4-eTZA-R-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IN6lyXhkFovEcbf34Ax073CzL89B2Je61PakAs8MmBJ-3AcUkN41jR16Eh08OSS2tVvm-xBIciCa8cG7j310gLFQ_I3ehKOjNTyrqqGJ3nGm19JmElrVziBA8aFq6vUjyi6n7qSYONfmDtnsspATC2UjVUxINbhLncxD_rU1KpiM7bFMqw502loyrK6_zgeSDonnX7AVUj3LUC_wHOJzUpizxQPWfAlypXnEUla8oywBTS9OwJKsf5boZKZe44KczunDWmM6dvw_9wxnNgBkyos0cMni-lJdfqWu334UHNzL9toyLPPd8-pWUKTGGMd2NoAe_gKxECfnV8B25OQ6PQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OMFu3_Kxlartj_CdU89OcJygirOfqIVpm4EZZOQRCgfa1efRg5XROGKntw5ctvbkN9lai-zDI37avqOO1vm4_OoczEOL8q2q9bpZE7XgRd-TERHY7Z3PpHRifeTGAWfOaMay35hsLx3SUBwe1-JRogrceGDRlzWJAGdPs6GCpCq1Ka8dll03R9RYvPBqrD0od-cLatWIFapHI9tZ2KVS-Gw77QynEeiHVFKniWcNFcAUvyHFyIWY2EzZxv6l8AdOBPDQgqBAfLV8qVE3AQJg-hxiVxjtSsK5IOq0a_hxo7nZlWVZY7lT8LkRGwl3knEaOK5p8iZk4hpK5AYnnZdngw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeAgJu1yaooe99C8kA0V-v476Mz0N21xX94CRTzCKe7jfgaEGQBE1vhCYDk5iajc4bHxouWGRlTHSui1hlrSoKTGqIC4VUTlil7SVEk_JSKm89ekqLYUO_6RbwBGNd9yaPokQz7UUS_egRLGQHEmsH-p6a9iLYNc0VfxPUgKF06ijPknyDZsQukCIaQw3N1Kn8Fm375Hp2MPIp5qgvPzRSHsPQrOCrtEIp4ujwNXeyLZMLZDpK2qauJNqikmvDhO_iYTmLQyHm326tD8Gc1aszs1czspRNQygOGaZT6LWqIitUycJ9PLvzbduhEcmn39phSxeSYBfCQPafmKZD1iVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FP_-DxYGncTFRDRnD0i5WY4bDnOtFVyfctd87Clt5-EakPeWjltJyB7B40jSbFBtce8fT0cHcY9UwaUP8ivpMxpSip3ULbqpCuCw-rW37FDrppl1g090C281D_rGVgni_oUFmgzLH3CuvPNKFLhWqSjwVqvG7HPQWestc2ttx919R6JXO7lrAt1fNVyf79oHVvt7Mvv3r4AtIoA3iuPAtYHVP0iqZymerhbZUpQsfgEKYQq5SBKlKDiFCwvN-ydjybqgGYt0LvorYDE6SshFnr7B2O6mnt1khfiGqziqaaf-nmDz-DQ_JEzewdLDLxln90AfDDspXr_nKsFB1PMRWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-vwLHsXa1NE78qnB7a6i7Y3O0thOB70wVQqCJnMjAm1gpTKRwYVTC5Geyg-JfxVxl2EDb9VEphmhGG37mEhJIGSnZrwuFbp5osYtng3EWm_O70hITc8EDVTyjPxvnthQAjOsWcrt_Nq_LAIjBTh0KojtaDas8zVTiw16dxb8nBp20PBQiPF_MjCgIFdrY0m6QqhxBH_k2ws7olhX4gJ2dBMDQB2Po92xjfGMRF1WfL_xB58iLgxq7VMNmFfEJWmSOl2kwCvHjqx6DNM-KkgD2P5nu06RH2yNrSquQYTQBIp3w5RaIrM8S7rxCUyl4J9xm3xNLdrcRGi6VopInVLVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TANJtHwBAh8aSXGydY9PKsvJc6DA12-lnVyzVqjDPAM-bsy7slac_fxAX6hZN6oZVONK3luXy_HuGRnpl-hRbI0y7SmVIMomNttBhlwqvThuaOL3grjK-a5YP3BPnD3UV_P4M7vMNlyVTbMz0KjWVyPDtQIh7DSo0L49vBbOalC0tBwsBE3zlPUEF-Mn_5-eCBE55FxAs3YK2Pc9n4Ksq7xvelaIWwbmwpoxlJRP-7m-YrPUGapcCKqqpdRlVMMPIhakjLqj6twNpBt7XmXjR_NysNDN-_JvGhNb7Jgjv9WjPT0K2hJJY3gEq_ix8yRBkkGQJ6ObsRQV7egdd7hrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wr2xpHu3gYk56a3JHZKXYopoRV26BWZsQcbkwmhJWQxZLfwpafSGj4ni4iDOoKXdErTxl2nEL7sAQD3ZOpWQl5nLCg-KgspNhqntAazQyIiD-pol74A1S7ScjQmeN6Vo_G4EBt1Q4wYy5xXGGwi-zDlDRmWEM6LAqwfk8egfj2IICxBYcuBW9biKA06FZ6DFQHe6zjAtUBYkKt2xgZAViGUdLWDRdF3vMGGE_BPMBw5Rkn7EpZkeqz2jJRWsGIMhAoWhNobjs8cvr2DLWa-CR-h5Qdy189vIADakyoTomYyja-1e0pESXtxf-3ZvQkrhMIWAg_GBypLQXgW70e3gTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFsJUNdJkm0JUzxOLj2jUPKKHzxOWJtDHFrCuB3-UN0CFhx04jCEE6TBfF21y1NzwMEbxQltYeoeKNGk2hACc7o337hhQkU4QOL6ltVmyvWKJa2ckV-CbjIulBHBWR0WNKf4-9sbUdDGKiHKmMqaeuf-QzeijOZxT_8ZwpKEUBZKJrpAuPHVWKZ-3iP7O7-9FDNwys6IzHD9wm1BVQjyYz9VFZwvlycF3B5i3RX4ai9q-y6i-g15t9mesIkuSBDcTEKpN2dms6NcZ5tGnF54XmUYsfdFractDseIWeMQ880NhVN7Jpx9auhIBlqe_haz_jFf5fzoxWiNKIcwhriENA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QXxyAz1akrl_WnOUt--u-fYp3CFWyDx1Jj1UOvKOJaHL0QpSF8ZbDGj8MB5gM1FtWoMWkAei1mqqy5BEfz16vxVOX9T2hkf1DmtNWNxgEoqjSMO9G9lly7xPMvkMxpzOBSDAnJ1Wkw3JemnxPgDalLR8wtHfb0_--sB-XZKbuhtRIxMZh8V9zRvPEu7onsZHzcT3wWDjVtVrEXKJZ0pNxgmJszTMJntX6rWipiPmiyXpk3dZseL7KrEvWoFwDGhneSxheX3YJ_6y4OfilzrUknck0hyAuw5riR1AxujRyO1kx7IFJzlGnnCJ4QWCvlefvZTxfWlve1P7Rer6zXqQAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eqFfPE65pkTNV7wCgain32W6rfylPeWiU6mh2jhuaZJDo0MFUbVCPlTjfPNK36A-2UwFw5F6hTFtyvur79auCMTA2v14al2mUzwmCee7ENCv27_xEccHLizrysEP-Ud5OAEVHKLKOMXhETdf0HBaZH36xkz6PgZQbb8c_ng-4xzF3FW0fIOHi0hdkkg9dQbCR7v9JmJmPu6oE9S1oIewsPrBrLn5F69Q_1qOsJ7o4cCL6zY_o4Bp6uhosKnNn9hqzib-ARRKoyg-PiQIEtgFcEaxHMcK80DBI5_wQQiZWhMfJUw0m38K2wHZ1h2IwYpS78C8SKVEeeUVNuVOQm0jgw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AExQ1H5fNUv-9CqNS3QCTZfpJvJ0j3KQqZkDkm2MnhXND0KOJfpXxIZMLEUkErcFhbOJrII5FKjAbqyZHP_uIzJumtNfGl03ydQW1jFJ5Cc7s4wPX5-A73wKJspPf6pwILer5Gh1gAt3h4u0HrSR5l4QIbug7bxCG15W3khOvUgvtsKg6Ve7aMVeA2oxhohKiByrFA6AJca6WDsK7TdDEYDMEZB53ZjFjIdLNSsfAlV6z-32hlnKp3aVKu14NaM2GKMhDM_uDwZcn7ikuUPifGq2C3izEKtrzZlRMqLzTf7OwMnjTg441QP5Cuf6MPL3gQCcDB4SrJ-ymQkN2aYkSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBN0M48ZYjWKY-fI6CGE3Ti4BJN39Vz2mMXPnKvq9P9hQAjKHBLTzqzCpQeVr8V1kLfw-NKsy8IfK5dlutYss8WYnIbLomPWGcPNVut6OKk_DbubUe4Hy-f6zPQpldGkl79uv-IEnCSDRxZugRWv5IDEV39sIhiNPtfKwv7tD4EVe9HcKdex00V-9tzqIZQr2J9cffAnuhQheebHMawzo2BbyMfJvWFEP4kxS4g7tHAhRTk2zMdg8sD-oLoOZLKmTr-5WW2E82T56NzDmot2gETQ6hr3oSU1lBZgliQpjKfdJPnyGz38ZxcF8P3R4-XHiSpNnikkUUdmHwIT3Jf-qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SyJ9c5ZuKqjOqSMNnjJzhDxk0IwbTyg1vvO4yJXd4UONZEnYaUJ_osjpvB2tNljIQciJZEK9qFFYFaQbtGFZL5O-0Hi5TQe5yBvIBOwQW_x5u6rThQZm2KgD-ZXv6CMWzSG1nNy5l0u6vlqoW9PzeNUieEZkc1Xfw5kHpcTTIqzzHhTMnXGx9V0laMZkflC3cKmfaRjUFN0oLKAWZU3EbLt9MJ2nt60bwp_GuXIEkiJaKX9bduzuNGwf-LR3_H7omSG2o4zN7n7gt0IzTeTnPIFPxpmFBNsBUii8wacyon-sLtMMZY_ry8281vov0zT0XPOvqkHzKkjifyeoszIo2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/urs40PdSINchzpO4lb3kPautUtF2zePBC5rLD7wMiYfzA2zvcQFRnVJ7dIemWoHR6bGPlNMqAwBRoiphqv47YQq4-rkgF0UDYL6tiCz1DWnrVyibecUfukWfVm0nmq_GK7YnRjlx4oWIIK0RjR7HFhUDuoQ-2vRna_hSJbJIReRyyhAvN2zadbDtaW1H_0IM5II3agOjaT1tagc_BnMHnEK50exMiQckRqAO4xfMrcSmfYmLKrzkEGeO-8xFvdjYqGTbPKUsb0BYAqVhUJzk4NxEzCbLmLM4gt6fmWrDRuF-etOCahJrfRjsUOTge-s82Vk3T0IWz1Gstu3xGc9isg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hgsIJrunVt87tU1xoQYf_s9WstY4ShCA005_vhCCg9m2bhBreIAKwue3nSNqeQraOeUJcCFt7HuHiBEnwdwd0YAVK6-XskRQ_7jq4y0-wTY4u6QwI9g-_YePBl3WM0BKE5f2E70LukvR_Dxd3mcpkJHZobGdYmzbEUkc7iUL7sMgVNBOUefsVdYXD6hKhUG9Jo8s10onLK5aXoh2Ol-wWfxvCKJ52Hp2vfieY6zSM4kBD-thmAEgL9EcPG4WjwPXvIj8CNOBPFvxK0rXBW6y7b5auRgBcBp3HkwrQ6IFLx0bOe3Gn3n_ivWAOPdx3H_AxY-ha4Z-50_mVV3Cp7owAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D_AndZ51NUw77aDUxkp5Urc4aa3nNLa9AXfPlAYIr1dgQIlVESZrdxa6GMDTxWbGRy1Tb2GPB6bwdBnfEWuECsVVAl93ms2PMBiLKn-tgBhpu9KjxoVG34qm_YtcznoYkQ-QNUoQhLo8zuD5NRjLi86Gd93nKySXQg5UzhIOGnsJSsCxT5HWfjrnyk0G5pOnZXrVPgi9L97frODzz4HCJMisU3dUX1KWV5Ea1Mwz9-7mjWOHZ1Bfrw0Kx9IwbNrz8KdEfQRyotCyDj8Dx0qODEMhzZyiUc365w--zuZ8CLAKlW-3xO3Zv8Rjegl6p0lfPhjqtDmMOo9eV828Lx9iJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfNhRD5nnxCysfFqc5CqT_QHwiBnot2_DtZ0N1UiP0Sg3PldtRRFUXp-eOh0obLZbwuDmbhwrxKmb1eNa925NuO-wwNwTCT0xxQa889O61Zf9_3iqfRztdcw51P6m9Lq5JrhArXyjV0QmQpF_hPXaqBVVL11pXB9GFLfMHBLJGflnbpN8lXM_fNnokHwSK6lvsfeOcyIm13nCzB5VFHcxhTfFMlTdAxs5n7F9HJZfFpTgM-k3d1lrv_FLPMZwLTX9GVqBt-WM65zL6aLcuEauF3HvPTu2lziwLy5eGW-mY2owQVvT9Eyv5sMKbvvAe5Awizvlc1uhBNujgxiq_yqpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khiK9h1gwMNIHsqhF5upsQ8OBy1kQUsKvkNHXhNbGrXOBoCwIVpywcx4pLyziwHeXV_XCCAFqbBd0QikrLlQVPv2AdnuNvnkHrnOevVg-LWSWYfyzfRWcUhdckyhpY_rm-W6rc_IAHeiAvz4HGcFDxNpw-ZMriFqOV5-XWYYyRU0vynFI8gUHWR4ZsN6A1Q39mqR-BzRC1LxFyVUus2D4-H4o-eFh5SfqOnwI9U3iXvV5wV97Z5mXLQmRs98771TeZEjwDF1Qwv5XwST-OlMhcK53eiIYYsVq0WD7laAeU9C9QnsG6lgxM2_BnDAM4nKrNhrdMxK7PXuleNtP6Eb9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s-8NREYmELhxo_4pP09WzbbRI6kmxaFWhIPSSqaMPDVurStjUmX1UFcyIIxciOaTPh7GEgpgyiKoXuv5UDdCMmup3Je0vSk3O2T711WpyzAAZV_nTc8H6sNojHVY2OybA8xezOOq_GIPFjOOKNsMbLSdB3kgiN49AtMcQYhHkNP9QFPPFIRpNzhd4HFWkrDBly0aScbnApO--eKAbNw6URh2_TiSjEdOwb5Jwj2H6K9O1GjkLLKfCrnn-ebyg7GKDsDLVTxvhgsYUcXZcdp71m9qfCdhYi2qq8nWorOkXRPlbCt3_xNk1v4pDm8VcO4SVcx2kf0FRxKm6FCWoVg0gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCLMl5itRKucF4kxXdSnfjbd74PLrFchm6l69om4r-zaAtG0ZbI93ivOhvV9QQM4u2WWEjEq0jl-emOTOoOIhj_3lJfNMVO7jEeIut69ZmU10KDxqkYOT2mMwQf0CO5OcP3GJgnxwTdnOjrMYmvcyZ7TKrnHPRG77q9xdrlFPBLEdrJkpMeSNG4kQxj13-DyGr6ZcdNA6Ynbxdk4_2jijhTa2NV5WvQwtxaRphxFaaPcZ5roxbLoXpFTljnnz3QNGv83d-xdWZgr3DSd3pXlUyJ3jlPNNB9vfDb7bFnsfALYgFsNyuvlVRflCb5kGor8hgmWfD6PjVN1ZYfnR2T5OQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uaI7PVpwFbvTmPXDt1_fA4SpzXwu1nIEZGRAoa64yuCPgk9XyW4jio8LNWgAKKM8pQLAMQoaXQCmWzp42wYdsQwZ6VLF9AhxsCcXls-MNGJAValazs5Q4rVPoMFonNdjFojk_4M40vWvdu9i1v7s9UAf3dC46E1z3dS7noxOrLT32dFWmm_2Hr7FVoWwgd9kNh55D4lmcLHHpS7e3sCP-1fPkWs3Eee-z0R7tHVbiMgXrD1PSSbQzue4UIa4FdPjw0XlRa2Xc7b_SMeegRwqAta0vpg_btUOQEEvplEblteWcpDqEZcUDooggypXhTBcJW5EWu7Hr-D-LpfgJC87AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbMbfu8zxM3Nyx9afgz3-9hT4DP5fmBOEO75vSTB3DHGVPYnQUwo6RW3Qa7oqtN1OKfx-x0mcD-orVoRUx3h1Mf-DYoJapJ730CZLsl9-g517XcS-k4rjz6vb6fJG5v2S9DskDZUyplnCXyHFqwSjul31P1Qs7uZ_a-tffvNo-V2LdOQufL8AymwWkCdwNNqvLdu4e4Dwq8YKGKaVwta8ZElNxFOWtVMbQ-2psZYHYy3fAfYjHa7-suUUNYuUP0x9xZWNW5lix1tZp-BL0FX7mW8CIHbDSm4ri6fPyq6yA-YZj0wxERKK6qVFRi8czFcwO_W1Pf4nJ6Ca-kGMoopQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OQBVtI4zGYuYbl1hoc91p-mJGSElvvsZkV4d-EaRzLzveYys3LWxz84cnDIq15w-jbiKjAUBIgwS72HEcsis_DwAR5iEZOVjkib5CR5hKp9W5XAEPsvnABZ0W64febGEXbcvld_-z25adJdAyWxyTp1KGgpZ9NFCBZUB3CxQUja02ZL6oiNqEs21YgI1IbUXq3mw9QX5x13heFJ1OAEHTaYLy23uTNFPRX5eAvYxP131zl9Uh_hy-azijCHSPNm579BvtBfbP9zkYc_3fVCwGy7JMKLGksrNc49Yz42DgmWZ2TsK6CoRXZvLla2QSOlX8n9yzhirxXYtJg03Ap7PfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOCVe2BaSigNhwPUtzY679-2ExZtAWNjtn-iqLT5j67vQyQY-BSGm3HV-kxSSvGFrMJuVurU1ZS8z5urjCNHaw1fUausvWLiGJR-eOyZLfstnAXmaP4mOJW6_8Pcq81FLiz7q5_FVmhZ52SstU5lYODwYDWVib41lINgh2QsCMUUYa0bfV3HfEziupaDXIw_EwgR2sN0UHnaELZlzzVeMy38owBj1Wl6OKDsAVBu6-E8pK26YuD9a9SymNy_OAv0dnk3U-uGDm4t_FycEtwOI2mJbDW6K0zEGE5YSZkPRCtTgWNiKvf9RNqihQ9lgA1e3Bi9sAcNn4tvDXxsLDVYyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GMFA4-Edebu7alKLsKECi7aMLilF4Wa_5SO_g3VBoq6t4uT3nUMmD_SFMBwhJVvMACyffs1PN51htGAkeM9NZdNwQwhdOx9mF1yYX1gizq_prwQvR4WWkOSERyJamNbbvf8tyRFWOvGFr8Umaju6ahuNzR1h8kPgj7r1_aCRRucap6aYx48PRVkQb8CfEckLKje9mE77HlybESFWPI_1-vTtzIgauyHIGnUMkAEydcsrhCxRO-TA3yrHsIgdgkUEApMbScr3Pn_phxbqPP9F4XvGnpa30XfhFNF6MxgEnZpl7QnDCFp1vGYxZyXub9IBvQYFl8WaJa9vaKkh12wATg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dM2J0zfCuAf0Yi1cNjhsHzeLIUCjPrO_t2GXXaGbjmaGzCkqvVkXPNBPx-ytGtvu2xbUp4U5Md9enVAh7H8_Q3pPoi0I2XVYdad0mRprYU2Ayb3tkDKlUDBUVM-Ytv9K85UxFsvWfNz6ZlVITAuwWCeGkaffFWlupjuln6NjKmaVyCSwTXT7Qodr4-rKv7rhI9m6iGgpNkRplro1iDGWT3tq0zW3r7mrZ_KyPeVuGXZYRS9S1myxlHOZNvH_1o2KWjre6hMbr5bzH0xowqOkkT4BZYujEbi_I5jBywAbYJYOWE6_iXNP4z2L03ihBuF1ytnaFs1qWlyK-smkwWcfYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X2MhVoWX6tiDdkk_SeGJbuzJDX27GRKz0pWZS9vyJq2EmbkSWX4qz7a-WGerf22ZM1YmBHH1nVNq2x6cntz1i_LIfH3aUDDgccUoo1xIcsuQLkSQgmswbAFEr5sMk5-pDpeKuLuWppi1THP4y_7OfWuQB2fgyUmbM7fX2S_X1uMoEP1h8XHhVv_fZe3ZdVgZCG8QD89nDcwORtffPn6mPu85H5nHnM33LPniqSyobYU-76hoZmKAMZwcukE5S5aL4YuIWco4WrAGgt1n1DBfP8WchZyfQF0f07gNSujO4xnIzs0Vy-Ayf7A8azMxmAKlW77_Di8pgf4vMoBc80UnKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IXPTiFrZENfP_Hr1h17NZsCMKRLYwcGVhvVsLcU1SiCkD-6dKoJnpHt9VI0GNoctVsIoobouNVAnff0HFp93ROKf6b0cvm89l0GvsExE52T4YUmD15Lq7bNe1g3s1f2i21oWir1pFWjyabANMUTD7RrnJEkcefpR5HN4RbNVVfOZqCrbd63UrhAdv1IShY4J0pTE59BX8eKHtVnDOfn7L5fioTexRky3JdBAGRHlJ3jaCHU1Zatns3mc_ellFmMFluSFDSMCxxPjqr0s4yeIp_gTPdxZhmioScGpd6wLsqhZjmClUggkZF2dmVPS6smLYEA_7IUASEjnOBLW1YfnGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhXf4e7f7lfqqX3igCUuNqjIhWer2vbLAbkgSMJm11jzsm9mDgCk5z3cpZBz2yfoqujHNDpcUtAolW0-WPEDM36z9WGc-t5XSK-94feiAWdGetv49HrSRKLyIq0UKa3CYOquluTwNz5RtXe3gDy8IsZtGby5TG8l57nU6rfi7I76B3T49br66LT72N1DZm2BL6UkojtTJMECQmr9lDeQ3c5YkD28bsUIUsnIQ3RkS11lmNMJ85IVdC0nFKmZ_0itNMb-gyk8N_7qOySJElnGri_lGJABAslQJRtNJ8tT8i01nG1evJcetleZPWxN8kCUnnIppkzY9U0nLvTVREOvlA.jpg" alt="photo" loading="lazy"/></div>
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
