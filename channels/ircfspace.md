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
<img src="https://cdn1.telesco.pe/file/pXJOLAqNXf7Zia-dppT5GTqvvX4epEZhTyl5PQP3-XHCbQi4OjOErZcfOsDyRR_r_h4q_ghGuZNc8U6He9jnxppRNESyihUV7yyugBlUy1-sh1MPTAZbUGBmUw9szWOGLSb5qGrpf0pmxyJjj_Acqc6ZsIDaC7an8KG_14KPxc8-1ku84rMOcGYNwSThZiWNXiq9pIBF9875l74ZpXjZvr5PC_O7zFnfsewMs3suqbOX01-1rVeQWo4ZytB-fZotlb1bIP6p8dpyeU2dKhBO1dfdL-152DzWWMlCFt4F1Uvr6ssQukJEkCURV4h_hQgTNQvp_SXdwJvljKSKxs_kdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bie1lCMXbcEjqrHMZXgcw1bv_z6E4P1Ym11GyDukdx6Y2PmR5i9N2lc4RKCpzxAcD8UKbYGscSSBEIt6Ox5QtB5gak-Hmt2pEOBiU6OvEq3RvoSYIeKMmzF4pOiGTy5yN9mIgNUhlaKt01OHQ1v3nszG5_RIUzFBI9Qccb7kppviv-glxRbleaQsYfqoWZCCNKePTlWiUm2hmUHuH9W4FZz1cVBmsQ8mAdA2vOv0mQZzW47ie7qC_xB4MEPbJcCo0vEBRUlJIzYuHxYY1I0Fu-LZBx6H0d5X85trzCSfLuPYuQvCnXIcFn7Hwqu0KlH5OOPW_XiiN24ZI_tvgCxq0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rnv2c-p3DJ62kVQlJ95cLR_YXayvgrohK3X6GSPYvYw86QcDfyT0imgs--Mvp1WM2UEjWwdG_47Y4fEW9x-9ssUVDsSSNfKHLVbh1LIkDTq54uA9lCise_XEymnYaW6k2AgSio_Ob3--lQXWcdzu_8zelesEmtNjfGLNLjg3EzgKUJmzbA2-f94lPv_3Hde1FOtMHe9P0XhlgMhKO_Kpf_Z5nMPX7JADEuBYPQ43cIHPSuLWoGAALlgWv2LyXjPLrKsuZj2wxIPct11fpztX0QQfrcyW4GDS0dk8yqGL1xoMeJZ0oJCm98GcBl-PVUUzuD5myDuSnaLouvhvw_MZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dD7C0IAPaVqxxriYLDQS7uKtR0h8hb0Yu1l9HdfNEERVOKytHtio_qUJkEdbMsM7s6uGtJSV_kPXxxK1fpsQN-0FGJg0xK6tN9OyvMZs4ceHx_Ikf8Uq0uHKr4iCXoH2adj_qXi_tpIRqlby4iAde_K14gDTu2k0rK-R_TBoZ5NoYchzpJ4AKN2K7LNOBjc_C947FCt51pfZpew5AYxw9UN_U6MQPt8Hqpq5MGSd5txXHvaq3BeJh5zVOV2otUkiInmC8q_o3c-PiTUcItH-xjszYjyKDeMRgFL6UK8bzralETYq5jzYbUaHlrnPUlfiRZ5O-lphvixE3ViCMzDIyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O7Pn6w7qtC6rzs4bZNcza93L50Jo89g78emLDx90dGhqsCUEUXjVfG-bI9Z2kTaXiGWIDauyaR-3liZmepWhKs7IUCSd1iZIxPUCnevphX7pbXLcJoaG54Ja_XJT0-MsooXLaoHInVurbkb6H1hI5CLb3T6tgLuKUDZoZSlQX64Vr7tnnkvyLXma4UfDlxjkfgq7SSmdmWy71jQLfIE1T-iJvHgjp5JiBP1Lo4nB_F4PGs6B--oS5eObe221frT-W9a-b-bNuoEea8L6yAsFwrAmEIycsul2WLhTWenk6jyr6uq0NnJZSf8khHMrAO3qecm6eM2db6T8lDMRHSsoKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A24UpdLpP0wTB_6jZkWRyslX7ERyv-mJFP9ja_x_zPzarIsmF8QYa1vRMBAlhPQX6Aw5S2XmsLmCY0gNDp_iJjRJ8woXJy26vigXwJ0lnITcJ3fvzGE8AXTFNiFrZCb_nPsJD701JJCQ2v1X1ULYJiYhLMjsWGbbEnTgJH0wN38FjnBeqZkQa0Hb5wmOoWh6v44vB0oYMhM3XHWEyTwBFmT-kThuAjkqMYAOAu8OovEqls2Xeq4NQ0hNMCoq1Hyx-EuMpGT888KvT5_JNVnkHw7WExYJU_SRDtSXiwE9pqGn_0o0kj0-02I_2wY8YVPW3r6kyN-EVIWyOwdZgmJ_Qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uloT1nZuTuNqspZxs7XSFdkDgpdRW88jWXdq0YKU_1_bJ0OyFzr2WLvlGcxbJ3jzNpHcvhcS4w0ak8KxtMGIjZwk5YwZAjDBWv_v7IaS7T8D0b_Dmy301RTY2RYtjO52nfg5osNJ5qRLwLqx8eq4UubCpWta3KKWAzYyVZGFq5-VURoPFcpUzkB0UmuYVAruHUwtn5h-EhpU-VTYK-l7EcZyzi2eom6LaUbw4AlbK8wbfl8o6bCJWOWkH2lKNGxtlDb34JnHm9n77TvczqnERpxx-o-bpPZ-CP_RNt7-6wAOEXvxbz3RWeweVtDdQJUEjg_on4W2sNVJypjy4Sc_4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ab0PJYoVIV6nH7Qj5gBIbOn6IZEB6zgRKCtrwamgIUtVtTl3Q8lXTg6pK1WQhhig5mmGLl6H3P3wjMMI3-0iy21zArVvag2Hfz8ZkralZNeVpDZnxTKSUSAF-LJ9gqdboxnyN-RMf2styW05-7fvB15U27FRM2A88rCanD1pz3ev48Dcd3P4xcunyoTCJXvlH1vxppmNiZunUQUuYemW9JjXZ2GwaTpafTXgx4x-NhZ3QPHuX0i72AaONCh1N1yUtxUDsFy2X3s4jYCc6zJA5ct92kaAO3rba6YTqfOpTInsd5_QeFBr53r04i7zB44DohRb3cal3jefFrquLhZAzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/daNTOQeeVAwIJVPXiIMnu4xPogpQovCCvoi2K2iFB_nLLgWYqyVSjmHI768y7uspT0wiOHH29-kZ4cdMbRn0ad_XFbG5jLt-Y7xPwPiEqQQ8BE4nXWDpMNW1mjT1OtGtNkHe8ZAEWgo8Jng0s6KoAxQZOi1YoxdylNsRoUwPwrGvpUVZ9XCq85gVb8fcZsjaTGt5uWPw6HgbSXdkmCMjwMppOmWJ9yqFZLTaJR1UE-ZiAAd1Gfub064PUMlnkdVt8WYeqUIG1c87dFtLcedMHhZxOqQ3Hzni0UYPg5qGal3GdruQxZ0NoaJSy_VRZLmygUsJG-mizPOLeAWeeHIHRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/flQsw-rqkUNQX94ahtFBGNfYnbSq3cjj7PNFKlXTaC1yTSzXjgwxGocncpyvmypVLCDUKsn_x5RPZJt_2QP57_BCo4ObiF0X9cseh931pTkQb2Fjhu-zTAmh7cqdAAIgFZUkohyZ_izufe5lxrCQBS7yU6CYv-C2eg5W3vhQfpzchTO3rcJqKX_ZdEpNw2FODKnzpSWTDC3OJj46GSB7yvEJdbOvQLzjjazHdhKU_i7drqIM_hIMXx_Qx_lzmveHn8a9ap5g4FfLWx0Fk-3lRxoYrvTWEq0tiGKsVBqwEuFlOX4XjgLn375eE2uOBRt5ITaYxtheL4IsmW2LO0GwiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G74s05idHeeNj9azvcPNYmEDYcaqlVN75GLif-AuFHoePG3hoEgAUEdAGUMX2AcXddAyuSIVVHlJc_u9QNG0OmLdCpjrxG4VOUClDHed8EE47rCvecN4vN8eeD_MOpbuup7sgado-0DV4anNZx4Wc7Ieew8Xack9tZ-vImiwpH9oHnrMMVxzo2tSCY4q4ZNQC1UiYVLh5Yw09EGwzGnMXuXGZ6QC4t0dUj-kXDkKNkdF7dKtaO5STQSoEYYPsMIVPS5DGt8mxkhj6g_Ybcfzg4Ep68s1X5cuyegPGNCDirN0oNpw3qfuiRwnQQXvbgnlihkuG4md_Saeuu26hAWUHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unBaLvp0bf0ppBNVK9M69pafg01nvk6Hjb3iSwPDyycenFy8q-PXJYSl1pRjfdZ3sqFa3FzTafo1rBYRGeWqpSmrBDVPi_V7zqbR1N2QHOCpbyBl4tqJEYLipXBkxjEwR_DpIUtL_mTxp7Gc2lH_8VvdveypteNhroLNLEuKIMO8T8Za7315F77QT6pkUYejDQoxMHgUBXSRXsZjSEoCItjiCQkQ-ZEOX5tUpqHrZSPnzKMNXSWnssjy4QxOSP39McoQhHXdOaTFDpYNDE_aox73I4AC4TvZFw-TANNFP4zUe_rOVjM6eyXJMt4Dj9Y_T0KHXrE2Xsd_AIBSFgC-5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOjeV2LmC1eAut7uXPV04ifJRMtxIC8taDGzovrbavJivQAdRlsQ1BPcunTp7vXg3JwqOP51-NNgm7ttKXxkoP00e9tT5HxN6wpqZfTb4lhL_lg82ijX7lAb6DKIYj6ElkXo2bGxnnMbYKwnyN-uEkFSqB_WbRvB7d2R_I2rQRevskQ09Z6aFTa-YLdHXI75-T2vQZ8ont3AdyjuC_ZY1wHW4P6POIwd4TZ_Ja0pbulEmSbi2CuoZDyLq2H_GUScoIrQ9iCLCXbaCuKSfbh0fkTtNhfP7EnY-zL2hZzUQs7xDQk3hoE40-v-329gNfuyZFi693un4IwRjd7YU68juQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-FaKL_7BA-9sYJrk4-23_RUpnyGnKMJjC79mNdKe0fFhnbF0we45YqxIIi2cjOROsjZ2PNbehKMylWk8PJ7ZD7zVs6FYp_LIvpFQJJAaH6lGZ8lulUUpjdRb04ujtoUargAa8OeSvH5GhfmkGe7hMmVUlbkf3zdiqNHj20L443TDd1phOEs5ma4RId-47CGxXmguNfPB5FX2BITh1kvwZnSeaCnRbf5RYtg7Af6W75UbfJCjnzXi4_bTNyP3hQmtaI1e8xuaX2mHP0btcbgrDUITPPzAeQ0RF3VVpNQNE-X-8xAD1AOamaykORhshyB7lKG1-dG8jy2evmn3coKog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhHSohDOkakbnZfdWETVfPYMEVeMk9YfffQOpfb3KKrAOVoVqByf7v3XfMJDhyCgLZ8sZDmaCM6eb0xFtIFxnVc2NtK8gZ5oafJqAihp4sshoTcQNq-9UKa2Mtiz4c7NAveuKz-NapoT9TukyIoJApzYkMbe6j9_tMvCGz9QrAH0bKUQQtgRmMizKkuMgulcoOG7qnTCbJgmIVNr8ZV3Jer3xDd8mDi5zl7VGkpvu5SRI-CHpqqxsbJqGoFiylBMYBAFrUgDUcn-drT7S6z_XaQ9kiqIKPjqCLq-oCyStVBYWyiLH_iO_K7lo8rj2ZrH3-9emDw75riyjwJIaDnkjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fH3ilGjOzXEL5c2xyj-BCI772gXxEE3e21EkM74EwrARAWHdpqmaROoOzNQbPMRaOskpX5EW8c2csWCX4hVhf6sQg5tUG4R7do8oqb-6klA3ef2XbgAtOkeWbFiF2zr9pUqN-SokuylVrNoIh-5Bxhk7EIte1dVbUkjavrTPZy--8ByMOTLmQdEow-6pmqCV3Wh_haRduD8jvIYKv9COCkau_VYMazPT-SnpY7MB53WUNtKkZ4F8kZloFRnTcPGV1AKbuYh4ZTQqjyJPOwm77vrf6dfL15y3qJY8iwgmpf7mU9nZNsn36Q6oaiGazq8CXjV1XIrI4w3Dtn3J4RAO9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YRoJ6JAMFl9P3F5HPhZ6rDtZmB903646vFj9j0QUqgXktomlx6jYJNYXm_La2FaTOb8n3Q-RQAGK6CzpdU2tWgfEdbW5DuxzvTnYjddUDarcbnMf-TNh3KUeVj67yqo31JPGsBZpBjCKB8sVSvAO9JxVX6osMUGN4jJ8qZ5pxqH26XSYFL4YcBEMGwbImzMzUx8RNoNlVXSMO6TVR1iqbPuv-3GZwgwSlc8O-zKrM-g-9Exo4C8nrb_W8i7B4tKNFUL1Wt3tbNSal55PBFTbUqyPkJ9N4HZVicO-zVmr-_sdpUFhqTD9KOsWjr0z2K6I0yR1fO6KICgHejCy3Spc0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8rTZl3TtwnA5SR9hdelZLr-Lq793YXq6RmxgIqnQmg3wqVeZ8041gF9_WuTZOLTTTD_zhXxl8gWy4a_o-q6trfEv2bsPUSRo0hq-PmPdwo6n6WqUzTnLTLhROMG_qXQACx4emvnmhC-CgZyZxV8mFIfvIi2vRaSmn_wH8Y75rKgnVvZ71jmeGeEYRaFgG_F3FMSjsQIE_ui5YoWgVDjZUMmXMNH5Et4tF5nBjoyaZxZmmJs36ooGBZeTL6fTKenQFfAjQtr4_7IhkZVnDC-6roCWXsdKQ3EZqz5x3yViTCDT0yybvDGsetBSRtFo-IvrrxvtdUdKyg4cxXjxNq3og.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3itqhuk_7ZaB-cAwHiUIfgZmimWU39Z8ReSCT-Ar3qP3dY8bO4FC56Yvz_ne1Bcsqfke5kk7SWPrXaTmIyRAddk-ZAl3zUhhlNViwbAciEtlCiHcIKG2NaTD0wRR40AsxE0M-6VeF7tujtbVJa6jDk2-FvnmCc5yO-3pEw4pi3f02YjRxz__1qtPQMKMrRdJkmtGLMq2NyaHYzNWn7vH4S0I229Ow27z2tYqueJBoXzLE4ickAzyDM1aYrKzP4PvoCRmWkyZWJmBLKRABbOxRcU6ztWeC0WfECz9QVqUhzXzUqh5tchp5_jtaurfdLh28FlPXUWpxwAhxMECkHC7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpWA2vZZKJZ4U9R-ua7pRr8ZS8aq6aCnbjBQ05l7c2nSyLQefxZ2_Q3nNKynPJFNPPNGuNK35EvltOv7zthQYUONssyq2PFJ22iAYfl4oK0FT8q_0W3JlTlUcwuMWe80K53-Pu_jWMy_Ud0QpeJfROdDDeG6gDfEXdahwjuZekXdIykylSyhzehx_k4bQj-Of9KHIB6i_4uY5GluJCeUxHpftZFnCoFaMLZrgZsu1uy3SGUfZbM7EeKN3ZVBZr2YRyDgLuBCv-XqPPEgeRrWBNC16yITyfRoDu8cH6QqpwSdemg5fJ02WRIuAxqbCo2cBL25kSFjAmQVFarNF93L8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QV-sXuyy6OTTIYVDLR6inN7E492QmCKJGmrjtXR-YMNZucm1xHZTnNuoVUM_XsPEj4GDGbLtnvud6-3-hD0T9G7u7RvJOxkvFE5UJJcwrjMCizZx7oI82pFv5kkNBIdLJo2T5ZrCYeeG7D4vDN7T0rKnUsA-jsZz6SAfjof6RaaIESZrlcJVYjY_Hk0e5tu1iecWUK1vngV91cqgAfNOOxhAO8hO4GZ32BLxMJU_zi2lE8w2OhBtwpjdkdO1b0878m_d24P7qhhsDMLEM3Z2lQEFsV_NVa_gDSFSZwPuglAMh87hWeC5ZrPSFR3o4eJ1FY3TZyKh9wuIG7JTcTukag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUvHK3naPIFtpHmYK6pi-Nk_tUKTPWgiDsWb_nIHzWBTJbXhjFHfqIHtB-nTgcxTerHFAFWZ6-Pl7qzyJdSFdhfNROYJGsZnZeO3t446AYaqe7tK2V2cYRqbONpJKXdkMKE2trWn8ccLbbbWnIe_EsD84GlcU6_LYQvtzKfO7fwLC4CtOc3ZWmVJ6_E4NqP3GQp-uxt4BnQArAhxJHpK5aiu2zQPbXq1HixuNzLw_7rPqu9qAsa4_U64EYgDmZkWEroGCXrTHRNpYO68lzs51aEpJRZX7ieEOth5xjWlZlBzqiibO3lABEjgnjeVJmgxwCe-pZ0VspnpsOrAEq0FbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gb78c5yR9Z2lYvqrYU0P4AwYaRgBiXWzd-PEniF6UpQiVj5BZDI24nHWq_JWhFj9IdoyJy0urscuBMLeh3nAZmM5yTLHyIpiYtsMQd21UNN5Svg_KjgCrnfPNc5dKzaWGmncatBgQ9DvcWfcL95f1v5GUBKPTH3Z2iJOd55N3MAtN44iTv-XKVYVIkFqtv7EfUnb3XRwPSBeDEUDNyUPvfnwHX5-QjgEbIOxPru8YrA-3G19gnpGYCtnuC75OdiqnuuvJPAFsiZDBZ64dfMPW_4TnIRs9uwaAoKPC4qCe_lvqoaVeESb8ytHmlrPW7oa-lwy7xUZGIxIQ0BQT7auFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uKzyBPEy9h-pyvKE0N3R3KSw0v5GjLbCadWbAybV-Bk_-bizflZFYKagP9wFd-_sVWW1xskV3RLaGycOwV3TDJYzUbwmvq74lHqP5BT7ZmmSX1J90fZQE95Gq-zxpvKwPO1rYeNjPHP5JbZk3GxsAkK1vmO7_VbT8e4ZsMOp_S-LlYZt85h6bvmj9F-r1RMv13BkmB0nnQCYd-G_IN6E99B9iC7MacWw4ezRkZvOaV8HcSNsEwxkrxggeMgLy0JIdvo34Dk7SycgLtz5ZArsBvwtTo8anYLgoozjsWqwP5dx3jYqAd7isNgzeQJ2AJ6ubO8aZJZsQYTiQydHcKj4Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICLDknATPm6PrRdTM-Kj2Htbpa4-CliR8OmV0gpaJswA9rVbHpeUKGKxgXYnPBjHoejw0kJEnBF9R8DMVZPvEtEIdkqvay6LWFw64tQxiP6hhX6hXSH6eqttvhYMngmv5IWvGma1ugKI_fuFgUbwdoUEtvYis9t4Av4oPugII3WCyq2gQYQPFfCR-P0oiKV3GiVtgQzZQvuYcg8ZqACsHafLv4PW2BmLphWGbO350fPLq6hloOeebMFXpdJExhGCMb4JgGI9wzMGR1xyhNlJoI-J70LZsRwNWc_peksypXZWRQQqnBBBp6B4e1d7yTZltpY7ojjWPXhSd85fHI9lyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iFumotQqkP__xToifsmJCQsrZKO3VeF0f91qEo2NvgHKhAtn3dTstgyYuq6-kPHb5UWorM-Cn1aIWeAPJ5q2peAGqdk0CjI-ac-6NtCaKafpKN0JVIYLV3e_R4ADa-aSyBnjhdobLcc3mu3DEJMf7uGZpVt1-otEoOQnmVkETudlistY_jtKUNeycK0Z1lZ1SE2BE8HmeHVVHPLLMS35j-1JOXwrsWJ6e4xG2PXDjVEGQefLkGSXE6s8acER8u3MU898r0qXN2pWKusSYKj3jtybET16t3Go72lTLodQMPmiOSy-OpPBY7s6QNprH8zQT7zFlkswC0yDiqudow_Z2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpB57w4qZ-qMvCGQGJsT4asM7Al_ezs2FvNOG8uI6IqILlUQcMttCV7BDQbgolMvymZ13Jyt5wefd_KTwpU20RCPTwLKb9l7V7EZsWvrveQoQoS8LS1D5HlX6diChhv7EJ7Ggvk_qVXhqsiD8kFTpLyhzpCaiAxe-n8pF_mxlWvG4CNd2p51UAGi7OzmO47x8YnIA213tKrupxAalACJ2ZNgjJElBGo1U2EyzTBA9Hi1oOCE1ifjD3ZLPY4dLkO0FcKx7GPs-2eysbYbrnfEQZUGzokgadYXETRP7ARdbEM-ZRvzN-bDqbLWiyHGLPJRN3v9lyl74gmbTk6hw5owUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rrt4HIIgUxCwbGvPaizbqHrLjaegjD8qys4XwaSEI0aJmT3hhHZp0z41PH9V1C-Cb-BGRZ_rHaHEmn1BagDNcZWKmleRBhpztLc1QzFOMbU14xNv4BiUGMB5-KDnTFLZ338csadfKxTErgXB06eCXddwJerwOKNbdTiTu4O9ZH93bxaU9zjD8b_q5MtCWG7LN5DhquvbkIkShD3TMkM5fZZoW85jC4AOGDNFnSDAPBga80FwxfY8GMZCAIK14uKxUdeGIbqFCG2zsNrFChCV78DL9WMiwtfgd_mKdvEpneBga5qU8G3Le7QBR0ppQRzlabStS26C92gBXXk6mO5eSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lYUax3m1MDaCt-aVFZftChCDc1CBwHPPu_OdHyKQhVH7bdkKeqrMtpMgYNgObnsu-EDon5_kaCagc1k_QNFZeLPcoI9Nl0xIG7hyh1cKlJ5bhc5TDTfOaOUvV7uHis9mgzqQZ-dOBkmmE9l0bhiH4adqNTT9dxuhJBCtg1uprVVn1NYiwTVgg2KKt964MtJzHgI-8J8o-pDSz4MC-UJ8Ox4SGKCgkwkRRMPdWWhIoz0rqLBidHjNPO54n_1445l4NcuAoERSlwPmHhWvF3k1ENhJMpZLea9AORX8ZlmwzV6OJqQrAallwvH_Ao0238ZcQ5P2poTrMwQxAuNuhCLNaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vA2lWP9n2E6zZJ57OvVYPoUlcjs4J4dz5gLD4r68V4P0EiV1iPmm5b9CBn4YHV5AtlLdtA2XCBWkgaKJP2oVph09CK4UbWj9d4cWu_SVC9cNBWa8sz-6oeoLho2TB3veMEYjB7FVLAuK3tNqmtFO2gXSU4FwLakmODuGhidCp5ngEhGFDiNJxJ2vUW8h1ZmDkHzp0dWIn1TcwFHovnUQrerLam4vAhMsd2UE41cqqLcpgy1wsOmiLCs1O8v6-nDjDxAwWrt7v53X9-kLecJ5wpHlF_k0P477_hjtQa6RG_TKO4W71M6kaLYqYmOcUkj9nTbkOZ-i94E4JtqjXU9g0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HXoAxsvX0YGBY3JyoAdCjFEC8hhh7gWPhR6Pdh_C1DOJchuQRTKEgd2l1VRahWJG-DdUNghjGeyfIUZJUAXC-RRSQkkgHeyT2TioSQLJHmgygx8jWzJEoM4CuFZwqIRRUdNpfddpewbqusESniZJqp3yx018ee4bbPCterlfJUcKmjYd0ZhYMqLtfo8j_LeZiPWeIjQlepoGyaO7t53whK0e7wpQULrcw3cy6ZkAgNYx2A76sIny0vKdNw3VSXsoP3v2N33kuRgcpQUIFCyL73Jwz0Aoc4X6PnqFnGUX3qdyy4ZXTYbBltkQuppa1ZPC0McruWF2vy5ZGwEzifwxhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KIDkVcpkjElQ6BqSxOQtOs8dFvE9YxV-AUdZ8W4lw6YmFNujVPwE0pQSyZKRMy-yf5fIA4ZeLu48bFEqMQIbPlfxPLT9Ef5TQm-2e1gfnLq4MDf4a_pSDB1AlDOnBtG0oKtm5lQZJeZLpIEkHCaRlBDjE1mLo-dhLs_XqEtTDmo35HQyGPcd7XxwmuV7eYyreylYG7wnqlcBRl1MdT2rOeVfLUWNk9WSZ3E6jFLZjqkFht9Kq9osJ2ObYIUIEqrr8RwGs9TtIOUvmLgkhrQca0nVW-dZsIntHy3f39202I2bNlOXqfogU8tW4lSmU88wkh3zQa74fZAMsoxrdAKmHA.jpg" alt="photo" loading="lazy"/></div>
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
