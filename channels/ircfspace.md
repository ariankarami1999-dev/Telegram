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
<p>@ircfspace • 👥 96.6K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 20:36:45</div>
<hr>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKdLyTWAGXzBgC6qu_ts4622a6UAWpcmrQ5I3MBOO3Eofytavzg_gsFG7pZeVWpdvzEMVYFfjX2Rmf327uZTHtAOoO456sZVkDvqBN6c_6-wOkj-_U456-rPT7IEGWd3MrylZnCnPfeSq7ZSMnRFbuQ8Mz4xKGU1BLGkIrLinlR8UnYtMQSpBENS37ACJV2oVWBnPetsfk26TBHUov2ZiaoNU5-ZpJO3UeE89JBJTmopSJuR9T9vn-gPvMjwbzIVOX2JvfSHjukqGK3N-YiOXQqi6dNMEmdYLALjxlDoG153Tuvc2VyliD3IG_DwOzlgjb4kzFZuu7KHVr9ZMtN7CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/ircfspace/2657" target="_blank">📅 20:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nj2B6gl_g77pPswdY0ny6TtdUz491ePKri0gFNXrUbiVRyNntVNYJq5ImJ5MM50uc8Tk9ib-yozXEELe7EwAUqqhFc1RtG8fqoHeZPt2GoYlBtUon1IOv1nL44Aq0MH0SaTJ3e1irn0DxFiujFxt1T2CbFfPJ5G3skAql6qAPTTTMvUYw8NEyH2-yyNZVzF_lDcnzHgcJCLchcIT5LAvJv220LWVv0hsatzlqbfaEBMu4UFsUEtjffCMI4Gon7m9WZM0co9NcpiGJ77vpQtiA1phYV66GfQoR7XYJm1Yu80VnVnHK50g1D2VrTfod-VaJ8FtllcMtcNv97Xyb8Jv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس داده‌های رادار کلودفلر، از ۱۲ مهر یک ناهنجاری ترافیکی در ایران ثبت شده که همچنان ادامه داره. ترافیک اینترنت بعد از شروع این اختلال بطور محسوسی کاهش پیدا کرده و حوالی بامداد ۱۴ مهر به پایین‌ترین سطح خودش در این بازه رسیده، هرچند بعد از اون کمی بهبود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/ircfspace/2656" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CizJRF7yIbbsGdVbmAnxJiNikWadgV93bt7c0PJ0exzZfK423AAgTon7s13bjC2_BYfODFNoAws7QxzI4zCScNicoJnu5RZVVgu4lIi4Am2_G7kO4u-iqqqnkbg6cDqwy9BBx6UHd3VeAh8J6vgtPrsB90izC-WzkPEojc1TR2BZAsPX4OWAUa5qcXqzT_Mzs_3cJLbhp1NXGzBy1P8ZcPYVVBicgLWVae3Cigp87M8snDtH5Nb8Ac27Kq44yf0FADJQXXN0bCVb_BmIZkXimUWaocJsA6gFw7TYlFywGhoIOPPjkQJI5BGjJWUOrlDTrPF1ree1LyDBsE9tuOZdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه جمهوری اسلامی در واکنش به سرکوب اعتراض‌های دانش‌آموزی در فرانسه، سفیر اون کشور در تهران رو احضار کرده!
با در نظر گرفتن کشتار ده‌ها هزار نفر معترض دی‌ماه و ۸۸ روز قطع سراسری اینترنت در ایران، ممکنه فکر کنین طنز باشه، ولی منبع خبر تسنیم بود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2655" target="_blank">📅 19:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_E0ZENxlDJk8wssEik88iFUYLHb8aMazOuLZBdMbXsLjP422Z1UImgfiwRw0S6wPYtPIwitPcmF3OMSVGAEWGM8wVAhV4-cM3nh2EYL3sD1DjB9DzyPAPjQwbXXWAM_A75pmWhtI8ZG7x8V1lymD8zycUtC1TVgEZSX8lo9a60RslAK_bGoMiP1wOwyc5WkR630jGQ9R0WOsmYMGe3B9azN8uzxuFyzadSAypU7_O62Fnv6p3K8BGa7ZvGA4LDR3ZIXXRWte488DDuAkZxFhQZuLsLvCTkDBf9IE9uyE_L9UJA_x1imM5EhI23-w5E88LBwzsiSS0YnDjPTipRdqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/ircfspace/2654" target="_blank">📅 19:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2653" target="_blank">📅 19:38 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2652" target="_blank">📅 23:57 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2651" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iC9P5iDcsUgq4NlvxGV-E1nilc5g90ZW19YhEtpflcv8fJ3_dCdowUc4cf6-M-DiQ6tIsnj1V0r_S1lQExk9FcySNyj4oHp3kuTMuq45XTwxIBSqwbEdfj6yBT1irGjGsv-8w8m_jQ1YKRwKxvs876F1vt6cYJJ6fPGN0b9h6rfTz9Un8alG5TBjsmt9Zufv1Lzk06d-noQfprfFs4kdw1rZaAVHEykdowKzqkfZ1C6fvKsx-SauYV6Z5Fz6hh0chudhALpZto2pdvrIP_6GJdPnjVUcGLCp5eKBFX8FsS5oUpmkppb--lrOzm0jhR7w_aYMID_NKXTy1k-7Mj28Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای "قطع اینترنت کل کشور فرانسه به‌دلیل اعتراضات دانش‌آموزی" فیک‌نیوزه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/ircfspace/2650" target="_blank">📅 18:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKIEbwD6ad9kQUVoIiNhNVS4aTPndW5gYz3DQzZZPWTLqTbDV3dq9an-Y-bDM7SRJGIre4DsDl2GJAUnc8ymvUGbbR7ym12LouEOl-n9VjNWGXKL2GfpFaUadlzvU4dofThUxadS7IUt2GZE6uRU_nAw-1PNLa89nWkvb4iNpOupG79LjaVlyF01-tlTNW2DbTVf7rhZTrapRrEBuSOMQl7dNc2lrEkRSZUXFe3NgU2YBmqT4XM8Fetl33_1dPL7AvkBKniWIRIUXhFd-bKCZicGEHHf1sNjwzQXsjAzLtAdqfK0aCx9X4PCOKDWFnMs7DNB2mg4IOyMwoV8iV5-gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2649" target="_blank">📅 17:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JIRwRS-8A0EADEHCDUpRWztbyeyAULlBTnYmWM3-fuxeapYa4bqZ83D5NA_FXUh1I14aJ6org_I1OdIrDlXjymqDodIaYuJwms8xywk9axWCi7i03v8MwusLv3pwsXwK9afQiGwp7MfcJX7FmQHdEHdGFYi0RaQKDpSwoNEHXck_Ew_Ztzryo_0eRZ7PFil33K-hYnP7_HoVh6GNT4hPu3rfXuADB0valQ-r5zdC8NI-k_LlW8TJGDfiawaIoqOC4UCHRif61Y99RW1E-NtO8tiD2ERMPX6gEaxpH40Xf-gfjShp2cSHbdu9gtz5AVErfCxeoEmlCvfvObggzcJTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا: هر سایتی که اقدام به اعلام قیمت‌های کاذب ارز کند، باید بداند که برخورد قضایی و پلیسی با آن به‌طور جدی انجام خواهد شد. /انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2648" target="_blank">📅 17:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXHyZt4okl-Y9ay7fhAURyGvVip5ZonmF7gt5QQDmP8jB3aNtkisBmbAsz7N-EsSzC8cnsFG_uFF8YHf_ylZwKDQlV-ZK6n9ckpzoZuYNNAp4D6E3ruDUYiGwatACPZDb8OXosRU1RDjozJ4tyMStt2bku0PK1MEAdQP9Lv9_5531mqh24iNQ1dhYCp3KCYtNJnNIuQ9dhQ6djpbOuiwXM8rUkzBDgBke9wdLsxYS1q5vtg-e49dUDev9wD1yIilfHz44pSNzBpO1NVrjtRA3eFsVE6_jsh3YEfNy9soxThVomuAsKR3i8H0zazLqwx3k10wwlhpKA1UgojRinstUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2647" target="_blank">📅 17:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/btaCmU0_13Q0tlqo09mTBAk5OeYnnmiYYN3MG9BCI7ObHeyiqHs6TDdRuqQsE4PoZ_urIqCG2YhhdqP1xtrJQeZXwrRE0i7ry6iE1iYCdHiTn-ey1dJacVmiNHDDOdmpNYrfeJBGwxjUAOiklAtSYlXvkiRRsm-KmPu2aXBkEh9P0_Sc9RaN6RHCKkIxF1JYq3w3IsN28lW05X0H2EJaV_UGI0l2JTSr0OUMXx2hztkNsS2zTjyuj8YKuqrtcJzxHoQZdGBI2Ud1OVUzwWqlHTORwxEJ3TSlIgNlORTBy6MYydGMrSGtuOnG5eQagiOe2nK5VZEV59LrqnCBrKiCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مرکز ملی فضای مجازی گفت: ایران برای اولین بار توانست با موفقیت پایانه‌های استارلینک را در جریانات دی‌ماه سال گذشته از کار بیندازد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2646" target="_blank">📅 17:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lG1ZWajRrSJ1uMOdjX20rrWmsWuuVDXL61rY5BYSRhH1zO0vm_9RAj4CRGup6Qkitr5-Bhl3x5OClVGgFgl-G_O-JfXiqZbFsrl-woNrMIeejfFIKLB6iQEkMxN7eW447dWjL6lGGfJr_e3-Fwczm9h_DEjuaEpNl3512A9DmW-TCZWBZobFqCrSBzVKs_TzVwxKCKMMwdQ-l6Pn4PDiXDPAuAkskF0eZhYwc6JjK_4ZVMI8_uqJjDZ8QRQ9572oaN1xent2CzJnDWPY6Hr-UIWL3o_4uSvQS4JzIF4tyCfPIVYd0t8CZrZCA4WoFghKH9eEvKjD8Y6zkXbAwSfn4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2645" target="_blank">📅 17:28 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2644" target="_blank">📅 23:38 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/ircfspace/2643" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2642" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2640" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2639" target="_blank">📅 08:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8L0EG0RhxGGXEE2FTSJpe0aLYdJFhhkz0YCJq-zpHbTc5dKQHt5hqnb9jksy5kiHBm0unM-9GmLtOc_aoWkKRHPowmM_GeHC4umBnwj9T7ENuWbarTd2Z0R7yM9ro8X0bd5njb5wiVdkhZ6y90dJ3N3wlrI9NvqaEPSEOF8xjJHQveyY8z7a4bEbyu62zcAfxhv13Kn0UwHozTKmPSlB-knkB-tklyV1O2ELZY1x4_iuat_yISQToBNZ7nm32M34MG2E210RXwVu6mJqltOVxVdYGx4Nee_WaqtJp3ng5MQ5Hu7mTY2xwQLCrIHv_Q0v15yYOSuhDvWP0X8G51mRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2638" target="_blank">📅 19:42 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2637" target="_blank">📅 19:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hysm220L9TdWF7yKsNXE9-jHhWxMLbtBnGmQF2owzK0HnekyUrO1Vh9yhgRZsdTXV-MsSGYhCV3QlHIQCn_AgaWA8I0ZNiINIerDvNzmkZPi6qqpKOSyZ9mRoRQutHYD-gbjzC8EEPb5gvKmaXEa8yZi5iDnvcMSKuUpTyr55I662DufcjAMAb-CXOc1KpC9fYlls8Wnj1n0mpEeSPhra-Ety5xxz9pCUiqb3u3j1l6-9CYf2GLMpfGbuF3TYTq4tD_CasNvWT9Y6qJ_a-BWEDKh5kAicIhzMPMjXIu5XLNAMIbgr_mFFEy1xOTpoLXp3ijFKfIqMxkTslHXDiQL1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2635" target="_blank">📅 19:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xiluaxc13ZwAd4Cu1EZMknJHd3uY1prlAqREJatAJsulSgGv9STS_3P96HpsBn_uXqNtfx9j9OZCWXjP-9rqyuWPOK_eTu69xXFv3p4GKKwWt36Jk7pI6_VNtUuw22CfMrmmzReDJXMX8kBv0_fyvrlIm-az-IgHqRsQH0vRHGzJlR-v7-g60mbVPL520WPh_UBtx2aJaxniNbHnTTl_dYUkKjBhYKGoy1W4AOdk7VuuuDHAGgzuMjhZulUB5ZyQGLZmXpAvxCOCoGMZX9HRiIJfCNtMu2yRlrKmsBpkTgfl6vyCKpfyaVeaNZPy7C7j7HuawO5uFmiC4-TL_9qETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/ircfspace/2634" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxA01vD-tBSL8Ol2qDOrly87s0P11UPljj7D7auvwfjnIZ1iMyj_839sGPvbGSqSVq6mxvRmVMfnPL5Qvcd31Zno-8b2Ml5oSm0h2NKhE43l2r8oveuh5Mh7HFNKqXd9rho7KI-LOljnvZnXKiWOJXYluwIBo-XrbsH9WDVCAqrjeILi4e71_fm_6vhS9uxizsjkbVtBEMHSZeZkQWE7Tq2JA-E8ruSINdDvzwmDEu6DcoZmQViZhDS1YThq-Qyz25K_bhrf7BJoQ3P22OKUxbWXyJuVUGbLbllHY8qf77-drBXbzwVbjltdpTt5RKT2sKmbZm_BU80uJZG9C-XPoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4NsIoANWiNUkOThPrZ1MpAtQ2QFUiiTdHIuLsJLePSkPRUhRxxizYUAHUCa7Ur_WDf12oG_L0X3A3yuhcsNSoPZoMxm8UOBhdhBkm_rsiexpNjKIh0u8ub3fzlp4uILz4fhiQDiue6mAf0Nt2LvkLZuEh7hQRYq5R1ZjVYgN2MSN0nY5Pb-KnPBQt_tgZ5rOqor0Nm2Hfyxh-yyS5i6X4MbXH91GTx0Tswyp3RB3O1sQiAQJt0VxucFdXPGzOJqulcGxV7VJKJLUICX2gBz8YLMAeNR4Fl1N1ECNTMX5u7Sk4QXAIfaTTUg6zIm9lied3Himye3ucNNDsKqQAuMFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXKCmVvmgqiSbOG4WcxlRnk2BEhSCR_EN67Mhs63k_21mDbumI_JzNo9-8kzrBCQWCjZtPHsSNOjHlzldj864qJQOm9xLmL6uHvtTEY8YVYMQiPsZLXigkBzKF3dPxjGsiFb1_yJ0lKmb2fEm3I99aN2Rod8-MXE5_R3HDBQ8ab_t3C27VypS9St8aR5BoPsBbEHIDbil5wICrRszT4A3OCbPCmYLpnVsg0aZm0BoQ1dv9Gtg-dbgmK8qAdSck_bG_69sSCnE_8TRvDr94Jpu6jLcE4nGNOyDWbYUb44Y7vM6eFCB4cWHk1MZJ3quy6brQ0vcTOkzdTpRkc8svKKWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qzb2EUFbmG-5GfYrw72hnqHuK-vMKHKEGwIH3Z5tXy55mJE5Gjd3VP0XM-4Wm5Xbv_folIVfHVxQXa7N9miFM04EDkftxICTyiNNeKdnqH-Q_DeN4Ozj71PfQLq0ZRoT6AdwmddLHkHgRgkWu7l7Lz5i1YZqJmmP_9k8b6xRM4L0kZDgVrrhG7L85px3ytlu0MAJr9lZ_CViawCr_GzdOXqjXHqmG7PaQIwQ9tZdFGMhUZubooJo1iWd3bnoT07WP3GFBwpQJFtofOmnF5XwavXS4frA3kEAlkeIuidi1NOx3gdrb3o2oAzQJxEF-_orf5gjxLUG2GKyhfb4qTJo1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eviwt1QlwhCap5U2QOO-r6Db8xNWtU451fvZejWixdZwlawmvPek034CgXZ1X_7sAC3loCqps1YnrDfUjdnu-wrLNi7s-lcVRwyJIUkQR157QiM7Z4DI99abb8zs8xThR89eaAAd5kUybxWrgnfLlCzvJLoL5swCCVN2eXLiW2zmXV0yGKVn-OjpQ0oW_l4G_9etbK6QJA6imFGvCty9qqURrdR72oAnSueliaCH9uFfo58ticI0X5RNuW5JygKsz0YAq8uHOB5qSQCWLQXDViJbaJOV0Hee8FwflfK9mMa21SMQjz1fWAH8T6PSDDa7Gj1JWT3pftBADEqP-hGoWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPA9IQW4Z-6JQ65uzFBwx12TEc1WcIEoeuqgPfkJOkpiwe-V3_DobUvPwphfwwT0lfYXUU9YK9Tf4YgJ9rgvc_3iEKyonuckVoAX3GNQdkin_X_CEvyVgPcNZ1wVckMt92A_NnFFr4P4Oh_T1eVvffAL0h3nuN57HWpP_tILwpc_ryYZm24Iid2c29U1bUO88tQSXw3F0jhz8ZLGoAuAhEE3glBITxBM4pKWfZVlwZ8BQbixm99I-YLX_LToojl03Tx7trW4JOM9mgh37XmeAfnh1bGSgTWbhbvvCB8-oBDxyWLgv7o98FLtP8csDdAV7K8IZm9OhXSd-Lpym3wBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hT3G2k_SYCDwAPqROMQ2KYxyolFTh35E73UqNM_s4jUzYij9UU8dFO-DoYEQJrJYKbsLAC5Vo9zbykUVXc6y7lZ6sarMN5dK_derTf78WydI6tFMBiqh6MdoVmKcBRsGVoTy8RqyfqFEvX_NV6s7QoKbHvU1dFZaFdOj13dIZI1I3zYPoSiVD4TmlfdFDJc3OzDmn3TO6JG2dgRCc8bmHqP4UB1DKluLnvTxHBFqHU0QrsmGuLQtPckukxN78gCUzwrJjbYp0Y7yp4kxuyMs5G98PssOziKAa-Uw0n_Gg_p8OoSf2kcMf86o8uFKK_JgR4X_ZD7SaA5g_x1MojZJvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_uTZoN5jWkhiAIkkfYawDoN94UL6SdUFYeI5Mk2ManYQnZ-0zMBJgo2GtcyEXWbFk9maK2xGZjllAuu7YXwkqwqx-Xz10Cm20ElPIdMztgkUbhqOfil-c08I-0rzN-bJXmKxLfTPs6Yp7ZwU9i_MR3wuI9aIwWwU-YwJS9pe49IGe_jn3vSaM28_TFkRlNkjZZlKYgwa_yKb7aaOwd_lRHIylk_H7dm7NLPsgrB8SgnGcNV6xlJbkmVSfgn3G2m4ASU5M3iG0ZIyOLBqoxknM0K32sEM7IxRCsAh4AfCfxo0LxyHzxeS04GGDwmI6pfHjizgF13pTHrTt47-WYwug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1rsln37IfvkeeoAq5HOoHMxQ4Uj0dSASj1agh1f8a67SKrei3tnCcUC-b_eKw2_g0ta8yYLJsDJ2OY_vs0RktjgcBdbpbWcL5WzFtLx9-Bn3qMyov5qaFxYxangantFFy1tOTZ36rR-Llot-igep5m-3RIBLLRrhD1Di7y8F0oQ4Xu48R01mM7rFRwK4jyGOy7ci62JzELg3zu5jAUL6l3JhtoeO7HmwmiMvRrkCARRKBgBtQ4mJN55EYjoKC6NP1eAh88zxwUvbh2I9tYkqZdJxPShZKHENsBbFz5HXssSovR4RrfkK1v4vc_NzahhjeNLPdlW_6NDA11MjOEkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kzQiqetsIbxFOk756djHlvifZcyRkIuZL16rOSqolpt2vNnGbM4-lJHpIlmNiYZxjBsMBHgVdboUgv9iBpVeM-Pa4ICIC6CafXdytvFSaSVpVLCNe5for7NSKUDYL5807nSe66B-CTUpt6tCs9ioVDAS18audVx5VZrJkT1CBVJA9LZHrqLvJrPR_kCApCyxwQLUi1vETF_d2L7ahKlzsq5XCwRQmoW7h9rYHvluFwN5rfsj8IMiSaV2httOVj8X5fRH6-QHFfrwdhIfmzbKHm808XlwZM2S3l3os1c3KSK4Z2YPb1mEv6Hyg3i_f2jVeYzMgdSjqLCNkD-5Um_0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyTa4AiNfBSEGFdA1u5zHirf7mMIhVdQGSTxbYre2j3QOLhO78fp4gXom3tUUEooQd2bS1k0C3kf56CVMRepaw4OCEu0ZSOkeI5VFT41DwxPbiKKcgyKbz6ptCdVGNBzUH9-qwk81AZd4J2oQbjS45rs399ONWeCb7XZz_IOxyhWrce3Q6yBDDfy36n1kJ-IrY3aGwN_jaj2pxL42XTEWwJIKM_bnqapJA__zPjVChaQ5J_ADNcVyS8aJD-CIFVqbvzqW_DBb-uJ2UZpdLyZqh-DBo7y_mfr2QUudqacdY-OGxg4phAo9119q2efMZ6k3IQ1trDG3KzGL6Ho_RHGhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJCXhxmXYrzR9L24Wm23Hrw3LJ51uNBDQJqXA7g0IKEQvJni4NEUY5oyMrE-CD_QCw6u_HOUkp00wTRiKlcEaD7ZauMqipznu5XAKI9JnngrUsiOmeNvk-DM6gCf4py3V3KfKooHSS5CPc9aZ4e778TCe8uWZH61wR5qaKZe2oEZXA96atwe6ZNxaPAiQ05jeoDfECUkguXkweXO_78dSx0ztd2dV9vDO5ya7uCpNTH4XptjYiM9jmOKawY7iyzSsemhTPE7KjF1a6wywkEwyW92BDKA1TA1xsvK9xWYOIOKGuzhQoF4B4K2S7ialhPSgSmJLofFxk8rXdjrC-6i0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HaX8EJ-z7atUCeHc77hvItIw-x3dnvmdN5HGIdWgMsZhJG_2XHF_6ysdEo7Ki1Z0Wb-lm_W_ocJR6vVc-iF_RnfVG_jWUWys3pcWU_624bKT2vhBLXKe38uUVKASfnMeGEQnZWw7tgeHUFb11fyWyBjqk_YcEpvhSrb9wxlrlpydcpjjGTF2JkH5G2C_S7gg7YmT6UlXmHd6kk3caqleWEBj-mRoGlBtxRp5TMO73TLwu_NA__vMErWTaYwG-UO1sxPTBByPtk9qYko8ss4HIF1rzVZ5qI5BvU6U3saJ4jxB56p4hHj0WuzuQgFs-IXyGCP-IZbHN_h30zI3GugXOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uovdoJYi9ErfIHQgAuTd78NTnMo1HNY_uqwoLh0blvEkvIEvUjMpS0re4fGmn5ngaTfTvz8ZmH-yH3xzEPyaf04xWEn_cIPU-TmYPIKuMXfYagf_ATHK6OJSDC9WeV10TjPRn8Ckg3z3XCN_z4uYz2psvIZrKQzmA3culJrbpVllTOUVtX_Ac8uwF5eUvXu4-SpIfF3RrhuOOYHN8TlXYsXL3D3IxOY4qU4bQko2T4XzfVYNpvywR7QyWEy-evAfijvlWmhI0__9w3EHmRkX7bimwiPoe7qbpKCJcJwOSHrMPQqOeymHNgxAnlvfWVCkOmzyDt9pGuDXnFnAlSjxGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VqMgjznqrmSR6L2X2m36bRk2VRTV0_7RdooRj7LOclHpByeDBlxLZzIzb-khEKPmnlX2_EFdJ4Quml-XOAKvHaltn1Q66zTjOVCFAV5578Sr9_2E2rXYjQ2dmVLVTK3fJeL9la147hhXC1wNqzB3OZpM5osRu-LQ6E6RJm4tcyx4tHWXptVsrLPuzIG_QgwFED_HcNk4yhxkE5jZX0zbIo3ZDKDop2YtnSDeqglNd4nZIgDBV4vOtxg9zP0NSe1VtBoN7mWORht_tAF-bBcjLh69H2B-NyrvxXY3XAeI3Y9V9HXMJh-zQ-7-cYixcCw7MofN4V3gYcIYbtNLXj6UHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SGrDubV1vkAEzHnj1JvBUMHeAMA-p8qtGK1a62AbrpIkN1fL6blEFTp75dvQLimu13I9dpjE0GT4-ja70Cr--pfHHhzXw5gWbGRhd1L31AIsRmeACSuk4AE-_JZJL1vNUDz4NqueI1pNXRpWQucou8Vp-mdn66aOsJjUPxnMJfXxGJ9sxwrhmGd8xkegtRa0H6Mxu9F2nFOBvksu1NWdjHLRSH5ffzcFwvD8WqLDNJNkTiIN_2Z7oIJbdO2h2PhbER9sqbdGoWcR1-Rqxw6RUQ0r6Gpugw6LkCaBjCVzvNdkR9kyng3uuoSqoXSq34tQUdfWXN1ymhSlGqb0BGf4aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HNomO3LXruj-FSXgmHDiiztHHN7gOna9buuVJ72yv3rZRs_NfuEnl_iM81eD8HElZNnKHrMioZfElBxAiVbq74dmjUGgyjM6_yTbTSFZ6TkTFfBE7_M303GcdGKjK9TkufWSaCt7nbAyRZnMMCqWV7Brhk0NllVKnk6GQ_-R64xIyt2PnTA7-erWyYnIep0rhx5_gW3Vo0dI2OkoxVhVoQNiIs-8rthEj0asFrIEBxSTsDaHlJnN_0MpQ-v3wCqet4iFt_GRjZgkZsNgce5Pecin_aLO-ZjN4rWxFZ84ALHZyXqWD2PpiWEwxVR5AZciXyWuN35c2lGjW0qqDr1vcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aJ_DuRk-FLSu6rpAFcH_a-zT0qKgZyD93-PEWkgULXg_2AxLYIDeUIVRwNSwhOZJtc9Q10oGfw40NTBDqGEaqeZCwjXONawXQ5loSPJpqAemWYpsT862vqx8F1cyVq548Rd6kGDZqdoENrACrnel26FP-kNp2HDHdXXDykXhbdE2WKLwXd0ZZj1HTXIiVlFnIWW7eDY3KpMGs49wm45yGM50KsuDTme8VntMUKjv630b8WZOt_PYCclGEUBRJ_WAndw5Nsom8hkdfFC7Wkk8b3n3r1KbvkOizJ46gkeHq4e7ma9VSzf4_gS-Vpp5DjwXLxxu2uPd3gDgE7E-U7NOfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KNfw21j5UnnO9RnwbtdWFsU_Bv7nj7-0q3BDhl9ReG_peHW-S4bwpkMmkVK2EQa-zHLWpGUl7jt61RVD-jsn-5vCbluL5G0W4pT9oZq9z3ryLP2ezuaK8nJUbeD4wA4l3nTUFEyknOeYIp0Z-14aLpV2kG18K8yXAI-Ec6N6hkN0_P8t0bHqI_OIbzxWUUx43ORngEHk6L--w0lPzXxYRoYGSfYN5KqMDreHvAe7BTzeQu5pVOZifLP2lpCmXQltTUB7fidLJqyN0PM6RkZohyi8AuUUr04JSRI5ACGoGzwWV-L_kDTJg3B4OBIabwmdUpk1jqoUO4ntLQvpy-wx6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkVqiDVNQkQIauVVs2wUovYKpuFbnMAMLIejpolcYs03Nvsk3UKr6zFi6NPoRLLWngongxCS2oR6ryCCFpWl1reDCT3-uLwwtID-xDe-N1fGruB9tcJF5uaq6itHwErhCsoQqWmyLmUxEim6cGtIthf1ZExMzyjV9qfACRA7KOoDcu7KOwjCA0YZw8ohCLslaEp_7_-rqk8wlrNU2ZlOzfX6WxsdGjebGP4JvUiO96QQ4REKmdwgx1Xy_GjEY0NruxQT49wZg6ikaob_TMDrKGmRV4FhexWb2UZw6arnECNeTqS4hNSAFgJ5lGmYGVVM36vhceVNLYCS7oa1Q7qwDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlLGr3aRSnQg1Wu28nO4wFgkVn-He2pv_Sm40KNk0wkZbi2NoxbkcIxutH6-LKXEf9wwiu-fybD6tVatF-kJu6h3280Zc2uIAh-zkKNB6IorWiUgJwx1PwL1ZWU02-CNlXgXnzFz7aRpL87-u3p2Adhaf6UIPMiSM5zpavEHEr2ZizOo8AfP7APT7V81hOAwA2rDFBICPXgWYEitmpEXSYR39Tky_JwgLl26GzstvNZBUDanLZpAgaiTTD0HwaPR3yygQeksQTwghaL4brhQDHdPG9hbkB3eyaLQvotxg8iS3Ay_oltCoO5pGYHGGH_u7eG0KGnH2Xa3OJlgUAnYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngT4Ubn_kNAVSOgbtHfkUhnnC0dyMLMaVN8vuxxv-XimZWVLlcyTB4yKzcDTq-CTxn-KJ81uJcnEkak4u-kM5OLgNGmlfspejyjOcXUATK1o1L6gnGdUY_3u8sRVaBYQ8adNtkDiSx8NpQEG6SVyj_Oeh0pVs7InFuc0uK44CS8jHvXEDS5laT6e-QOZK-iWohIYRB3ke79TWFATEzjKiiYwR-NMyfqjOI0-ntbgHGCUt3AQQAzsa2kAthH63NOZSbEsqf7vPHlec6LB--L6BDGJ9UXs0nMOanRKbHU9TyVGyPYRiw-PfAfVm8YbRBICllRK3k2hqfd01rxcA08NNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7X61IHGOxsA048KAXXjiipntxmbNvc0NNhjmpmU4TSi_N5UcRchd6-1tJ50aiD-UZnP2YXlYTGCIWoLg8Xg9l_BnPei_IVbxRHjGNNnj0p51AA1HvGBQvckrxEEcFmbioZKjD3rmV8NiUZjwj3SusEM3lxKoKGZB8AxOtz9ISYcLulcSDHazgIap7DHGcFENgOsjFv8et6BJuWqsQjsCXy-ZoG3QLLAsi9Q38lBOb3rgiSaCydsAKvpzRkejN-UghAYJh7R_VhYC1fpopCYWNrlSc1rPOg-f32PqSLPnb2Eu15xI7BbERfwx0y2CUuVIe9SAwZk2_3EA0SA5_Q2LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Amb-J6-KiFY72T0GO0-cfD8wvSxBNxl6iRAKMvQ_MQuZShiuRcBn2bdAjsA8x9ljDLGVPPyFgC9S4MVZqV07nPr6uD4uflx5a4bDU3Q1-CsZxgJmF35y61n2YBo2z17vqxcSshWYd_46Zrr7xfxrqOZJvm41mgpm_6qBcsijTzwxOCcuW-8s4krtPYB1rLCYhJ-Lx3225Ol9YzxzkBNrzgwixOnMelvjBP7YMDkR079s1m65heDuP4rbrNFNGRLuPEjzEcw3HXQnFz2vrDj3flFiRrZ7QhnO-va7ZTmI03mYVvxcCJF9cVzFomZHTz-0bvkRvrVOmUXBxrorwanB5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/onk7tCu2VXyLeNXtqoQczVFZ4t-RfzHINcphfAI31zZgm6v_LKTiURJy1Q3cDOJidxvOCv1QZ7k4GkXbr41QqT7xFCo1hNVJc0tQ7IrSbnDy_4wb8k8RGxD023vXd8OYTNnCBDktYtQ2gYxojYFF-o22xRc1kFbOc5Pl-znlJwAHYvr3uAlTIWM6GTWEq40l-j6B7z8X19e9m_0JVWjwJdMyaEWlLzfjrALymiGOaZOsl9ZeRG1lzONSMfVifsMYnOH3PiKsf65I6XnZTZigboMYJQcnBxU40lNXuOfKRGpOx9ftq8ojTFpBJonnjZ2nogqEVzm-Jen-JmWyGFsJ1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dD8wFrbM7mfGzsahkDvB_hxxsBhaoiq8jig01oekbuTgI_uxVdEeYpN1UaRYZ1h34ECR452ACtml263DplML-5mWYsW3r6oi0FKc2Vf6K-0aLDPMEOxr56xciwmrI9oLasxtYO01XD-L3_7HbjQcwmtwQzRl7b3aYJNkInfQfRNDeGkoFY2obyCQN3bFAej69dv-nBL5zsDp5klEJ9dvRsBqMWCn1WJN8x5awNRZEc1ui1FVV29Vqdf2PBBtCpZ6KonJ17v2HvIuDlP2mKR83bD84aAIDfEklHarak63qToqltU0c3senYU8hcwCkc4L6Nz7tDe4_4Y5Vh5r-xPoKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XF8n2Y_QvIb1vKZI61GWaaAqRz8pTB9-kVV0bTk8zl6nuibmPWGb7Q2suTsj3kocCXwf8GEfQZcXTyoetUKpWaz5f7lBJ15LYnlLBxkzmI6QGD06XHdESj-Q6V0BTZw3dp-IpJnDJORUDsekPxG12Znyt-YJnwRnDgP1LlcSHSzyRi-n6Bbcp4oSYmE8ljydKkXZGG4egEglkv-dIPuaLCiqxjYd7BjxYuuahAZrpcjNuaHpURfO_YLxKAOWl5_EhXVkyztAc7Almu9NNqHUwup2Si3WJWeR_Z_9zz0o0HaAAP4-vAHiZdIaLh9Nwmv2LsweUQZnGv2-PoaOhPys9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/alCJzNfIp2BkVXCo43KK3chSNTdTsb879RRJ_km2rGNyBBTDb2sLOQJ_br__OcliXXUY6ASCCwfNcyO9Bp7nF4rPxsri6l_ln-pd0NJDw0IrRtLEcldFacMERsveB-bw6z8M8TrYG-dSoH1Z9N0wh_DDf9_6d6CAmmDVk_HjfTKiUIBypZMcIPnrNIGuaeDxrRxdUxOKp10mSolHgtj5y7sk7ORsw92TAV7KYL0EYmdnopMFUy1ifo1QUbYHyZfous1j75l24ENgJmwOW_WMv1h8BMcrFHRnHlzB-AYtW9yuWUzHm_08jGJyzv12PJ4Omx9rBl5vEL4-SmbttKboZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UIYuMsLvcgiTfwhEk80vK808fTM9b7V6r_BRhxhNtPbFVm7Hhf6JwsEpWEzMpnbTFGbNg3Hm5Jh8abnDje6nv0d90HWZfmgbGMKx1bQ8FXFjReR2P9QbREd1MT6HatDGmyRLFm4GsZ0x3PmHhGFs5SNZrw51eozTsrg3bsTudGJ6Mv8cbCvglaDJR3sW_C4vYFIGEOqODjHChqpFU__J4WEwyK6_qmhrgkveGGS4OsQAjXo5DsjMFVpk1m1nxtP37sHIrZhMmUq7nmPCCANUIZZhmK99RgZYgfQSHyI6-1Y2TWZ2p1K5az9FK_S3pirhlJ-nEqPV9vK7D8VqKzXtAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGb6A6-5_aQMI55oesd4U-75O2SFtGie8q-tvIasy9qKOz_TYzeBDfkyoYfzTZ_cELAhmDwXWn0ndjKOe7nlPZFjTwL4AUd6fagKj2ngnbv58MYe8wfbZHLTjH4HST0ZAGS8E5B4G9_EaIiza8Ks8PwhBenOC1AXX1LYAv553hD7eDUJ8lP88izsnXkUd0OGV7XTSyBqK_2eGPaD1DFzSAa9d5UqUUC31POiwJCjXLuFye2Rb5GZaibkx8Y_0Nq1wbQu-LVTKWM8gYEjL8vvohZ1S39AuqLgEqQe-FMt84Cm8fjltmvArgHOAk2Y9ONca9jnnXPBUg7NAA8LK9uH9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wga6YrK2azrmBYjCMUncDb-qi9T00DBMRE9GoqbrJepKWauIc-j6hpioRzRudQTj1oeSWrhITRnoXPuEWuvyIv6jvdckoWTsWmbdDY91zRHpDmJbuCT_9Vh47B3oH2aMP_p0iPjcxye-tRFCUsEHfxfafSA0gVIclLO8vHKeYppC5tNZe_UPU5BZitSJqB9SJhmKcJKyMgo4rOyMsu5r82W8Ish0reQr4cgw8xXyY0RYX45X1JfMN4FQGM_pW1sE5mjpzVdFnSwNQaV0P9-a-ykcfD3Ygtzyt7wxEyGvBQZKOdidslTLY_Ef5spErMrUvbfurf_VLj1cu754adM6Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qk1-lAr7rxNyXG3LQJqMe7R_0eQDwuu5kAZDg_BJexy6R8lF0RPuxE5SZ7NAWgsVmeZSaamlK2fT-VgdiQJpXUQHBxg1VjQKpAOYy1yw0PhM2Tsdmw1ODuu2-pKOtffLdNMgZ0bOYU-e62kt_kaEb9B7nfqwQ8cCUoCAlv00-lVl00Q_yxVlMW91ucnGgIEh3ivRM0AOOxoPSjb9YHsUD3oXtKgpLgsWbiRJF-w3hReKrqWl6cspx55RIrKVhnQ_E7XNrvfJxvdpvkIyQcLWw9UjGnZMxjCXcMfjetDYw13-xZHEBdXVaROk-C-wr7cpnpKa-pdYtok0qryxmGsBvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t98Q-6UrjdWwn21xfC5TE9iCf4A4VCA-GiqggFhe-ociGJCcSoBbmGLCB9hgY_TFgXxHhDNFWnRdx54QHacPTN-RjqrbAPk30kmwmw-x1Mt9rOHNKD7UrJ8986B9Y-gZnGk1F8kiOPvhao-_LlDy6KbQOB2e8Wj4TJhcOqEsEDLOJdC26hJyQEgaTMCCGQFfeWsem9iTszonQwm2anB-K3XxJKP7xrX10bRE0-nqH0QxnKCkSC9uAQh4ZDEncQGioDlXtf3zw7MMQoau0XSX2qCPobhakH-3pDPUcfKBp5QCTrkdann_R2092WlLzwRzJdnkBdwoixsuqiqagjQjrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CfoJeG8KiUMl79QrD0XJ8aUVsADJXth50QZcDTg93Iipj-6ttdS_GGUORMc3OEeY7W-0wQ3f5FDiyv7ItVrluoMPFV_L7vx0E42pwKtdBpvvLmaZ0J6rVsuxhMlCRI6NPZXYl9aijA2kG9gpUvyE7Hs1EX0AaUn1ru5494u39kkXV1o1JSlrUrsfuI6B8cvZ5FyEj332kXKM5gQ_nToUV1859SKx2DsWSCatvYimsQ--g_hvZ35_jn9SfDX5-W_Lw49bfwZdSW0dusrdplKZalA10rk4Rt6rcZ5I-k0GFWNvqmEwjyh32BDG992g3ECYLm29kaH2iWyZv1PJHpbtDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2hdujiv0Hz08ebGJWjXtuKymQpTHAvKeE3r4IxWB62lAtNKdiM2bf0ZinFwqdsEb-r9o3q7_PGCKC7-0OedZoaA1bgV-Cl73YaDUivJ8Ya94czxjYw30RitcPXQt_Qwlg7vl1vvjhJ4E7DqAB2PyGPk-TRs4ItBdiR_GHVMRWzik2aRvq-CQ0elx_NYizL3KHVLEw-Dew59sMhVbRW0ZVDUYIzD53og1JwSSSKCo7cXUVbdtqQvLO81ZZdL_d5HIAVBWEPehVLxh3p3nHdgKa45U9mFpWcinMFJgGRc9tw8TBuLCIGwOYWU5k77KnpOIxshvBA_jKxPWcFxceoz7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AewBTaX5ZTRcKIYzAaqMS6OZF4Z1tPynWWtcTTRviiwMfeUNUniov3ILKXZ4nSlnX_n09k27JqBoSDsdvflhf36MiwfrdBIBpElsyQaDsd5sEtN6emyrVuA24Bgl_wMrajofCB8tA6L9_09qNkY0u7Drr2mO6dcaHYiaLrMW5tiqluml6SmDNI9uwvhzYc1BRWlO-a3L_6kpHpLZp-rJ_E6Ck6lFI3bqpcCq0dcbXWBT3eq2-sw8va_GUTriiImS8I0xAklSwaYoGHgOzMHp2JgE09R9DzJRpUsKK8Kw79H0m4mwk0hX7zjVGWG9ZMBg7ttqo00XpdaOlOe_qED-LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2ihjkVkTrG_1DTlXABquaMCm841AdQxnfmYvhT1O0-Dpob4cOAj5K_nktxqkQsjjvj-nqFqejMvrXpxFKKm0ZKcISpmt3b4mdJ-7_FLCngMg1v3gvqSujzMDFVICEeSzilcfv5DzOUdpQTnR1nHUOBMRLVwdTiLXGrMTxMATi8bGc2C6JSP2gf4E_y9t7Bn41t_FEVxwDR1Vds8wHREIULUvjYeTwysk1KH6orviVFqBlhtkJwQDlXLknH908IDBD_mdVElES7xf7L4Z4P_EK3aLRH5k9M6ZjR7vQiXhd50GTsbDUYDEqddZSMhyVxUbfMlW-0VQEUwN0Nt_U3yHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z51r7-3vfbupJotJP1P8Qbu4YUmL9vbI4jRHC266YLTb_Q2f3K0-HZ50paceyx9JF5UPQ7d-lZ9jrWPFo-Qm1hpagrD4wSNszHxOeVmqETxiBYJQuRHUidfQqc2cO1H_2PGebvDzZkLrVUOCGVW1CYOZzYEXRyztH7XfKCd2ltQ6znRw6CzHuAjq3MrwNW6dWnbcgBsuTLvEqPeIATv6494Ge6Sn9o-tzYe1wrJ8M_AY0CFovN5G6nrUGad0kWZIbw2hXYLdvS6d06g37VkBjs2CNbzO3NPVfU91H5G_H0nEElSRszeAzy0C5g678grDMtbAMX4lrsUo28FjB92v4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TGY2iWe0lSRjgeUJDm-vKZCgEOtWhS1oKffkS5-M6EPH4_Ch1YBm1_n22IizFhmQ61zjLFuHhKiYw4xFoNbrP7WSH63GA98ICHPi-4e9uexqfezyWJwHEsdCcTvtlHinBHwT6d967RR3AHDf3vlFh7G37QgNKBQgehKjUa_ATzsfs5xcRYooN5XpQZYKSw-4WIolarUd1uJL6E-ATI7zDKPledknYYECm1jSt3WQvCDIu3xdYeY0CfLq-DqFKH8XxYXyBRTpVaAZkZKeqd_PY1z9AOVu_2aVoeMB0Eg6vQ0Ybf69hcyNTM9L9pR-bPYNmsSy8qnwnHl1SswgY-EjZQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qx_qwztHN1E6wCVHJ7ENOle2yBW7Yy7BI-qDvX7eB88mUgx8Zck7m03dL01Hor1WLQd0fxJzBl6kqXKgkQmC8M2st1w-QAnSE0TsPcNZ0PH89epAVAj7Ssj2p0R1_0KCBmzczkr_6y-doq5ZpmtiI8mk6SBYzkApnzqztC6-QvUTD_4q0_y5fUUHILE-oekhAi0aIvqYCqNEdr8LeQ2OdYlMEMrm1rPbS0UTzzvKwK0tv5XXHPtMNtZ6kxe_dON6bpp05v2AfIkUJO8N81n55r6N9McYbVxglMQnJmVo3OHA5R-kFlgqOsCmXI3_OuP8hqB2sm0-oO29h5xFz75C4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cffu8hq8ZHfBsAe7MU4Qkm4FSllquy6x2mbGd0rJNooRnvd4HyW5jClFmtJf9LQzEtCp4AauxuRYTiiHfwWF_rhf0yzj2XFeMMmojYFc1Im2U9rFFrIYfB1zNYdfHsZe2LtTqooG7twgi-zV2FkHhFBjiF4Mn23053eSEkyLx01yzvOKnhZbzOCXqCJhghcUQ92y5poci3aD1ETYcSlbLYuNjGzFXhVH71qr3J-9WQ43-yfxbxsixhJ4ov8Ak_Q3r3O-lpGBh54EXZegKu1kr2Lg4pzWGuHlZG7wLvvxmQ-q732L7FDrLCjCcG4Clhyv2xB3JAlO9iLQEpSxoDTGbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rvxO6npq-6Jo9ADLQ83SR0A2GAAQMa1fyS7hXDLOyxxdx5cxLPj7xEDbX-4v4Cjh7e-wfVApR0JQOPWx5QSZ1qGyqV5gCXI1NkUgcNY9IqoS7c52ES-pQJCysdEbJluhMYMar06PmSJ9-pIR688BV7TsnzHbBjlXynts4a4m97ugCBpfkFIUZjQ3plPtADtt3z5LoHbbuE08rVYVOyzFrpxNeD1dakO5I2dXdmZbN2UyDKrXZ4plq9zuZb6cOkCYrwmdoJ8dq_xnzG_ucw6Y8hQ9_u3LOxJ-Tt36Xunnnxi-Nk8sunpW5ihS_VJ1y9DFNiv-Z_dyuRuxbqnB5yBzOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVi_XVJOtVqxqms0MYzj3B4NLv3t-ebk6mgfdNt_1U1niq7CRmC7M20tzkDh6rc_ztl_TYc8M189vnZAmb8xk5wOplU9HmTqP_VSr6kHw_06lpwuCl6Of39OikxaxHJOlXn-dxnpiSnx7ymO75dKGgg5Nt9-S3fkgGZ3Ln7k5KYFn--XqtIfrFmjWWC6CkCH38Rgds6IQ2DH74ul815938qf4Ccc1nOs65SntFYuPuG6TG6uM1UD2voiBESdgpt0fzhTq8Arkp6wR1UyFpc2hp4evPUKvBb5SggjgECZZkGl79TQDCThoU6hqSv0CHmzjNptJphm0bV2gvVwXi1EfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDpz3YBVglYVTfyW82jeRsTq0erJlxX74U7pUeGns-z5rb26IukW-KAL-rGqdUBP-K8T825WEbyTWsXgk-6gjGcOZlmBsj1rHoOvryLZUzUCUS5pn5fa90jodIZmeqMkobDS07xhUa0tCCJFwElliqG6FeEg8HMxCoRGd66VA8n-cciek-gI50b1AHc9fHpB25-L333LprZqlhy0gB_IJcJFMWUeWbanBQ5ESuIMaw0DYF6S8DSdeIGOVXecnaHa1HBFNHW1pwpH2C_cUH2hvOMrz7LQNZzUfzQ292vHfJb1QeLT-MYWztcGHqBaoES9e0aQL5tc55Rnql-qYuY-Vg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAAwsXQneShN5mpvBCU_ioHxvX4Kt_bTvL90VW6KC6RiPuR3ugtDU8Ka2pOcbAUmVHwMxYGKyFYBG4zY07h9BkS83V4WJzm7D7yG1QPEgXbFuNw_pTggdTAx7gr1T-aYHdaWSh-twwe5S0oFOcGuCGIjHK063_JB8emA8kKal_cIjyPa6tcA0pqsjawtgyJq5inKZpf_kN_50-qDtrDEQDNWYfMXVM0IS5S4tdEwvVKIBVA2E7hzTO4VetaYEgF-F_kt1Ocn30iDlqQ8bbXXOo0ZSOvH62N5wXaFGuKJD7ngsVSaGq-T5DmUfltfgshtJ7uoFZftAqfuiMQikpefmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fD5fLpvHeclIb-V26hC0fkBwpMOWwXmddGP15Jvk-Qn1pwKnefp1_N08g12fZ6oLLjO8NgRqjJlW82mnwyzsNn45S_WZX9txKNqodcU0hceiJ4fo1sCeOw-o4xfieiMUBVE_XDV37zxvnvLVD2lzsb_VNbreprCQ_PkGhUCTdYCcPjY02uHtD3uyKAXcSkvG7vdYqjaFZ4uJ33PSgBvFaY_Wzjb1nfD-Z0WXvHCLhmZJQsoyNoekh4kYtCH9bxLCGlfW1VsXZANAcI-i9drb8aTsbjgCvhrTqjutT20pOrfaa5SnLp-ijrou5sBW1oJM1RufPTSerkWQZQ1C7A-Qaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7ni3NU5hiE34BTaLouOXe6c0tmGtF1r9c_tdOaVFC7-lVgJYID_BBtvABhuWlagkMheI_fyUpBdY_bwUKyVf2e6bg_8clZCSL90I6hoCWceQZ9ielqxYmcMhNqjH51c2D9fND9y6NJHGsIp8YSSDwXo2E07CbQIvSejLCh7dOFgusQwVgdSV-esXJUgDe0QHkqjvaO2IeAF_sqhxXzOn9C2Wy6VW9dDU7yhfYcaKOZpA6H5w8Fife1PQePdg8uysJTkaYq-VW5aYYzb8aj9KwdYIeabsY0xCEYg5LrLKtOG0eO6DZTtub_M4UYpIs1PB6nF7GDqxs-AY1Mtz_VY0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VsbFAZrRX-AjRb3h9dHks7et7mClrkXrfTfWpvYuqnZJe-cIR12DE43TB7H1mIuOIewjIXCnvbn_515u7x9VPebxLnxurKgNd5pMNmAINHBgBHZA3Z4Xnlm0uEXOQUcYlZOE0fAoptJpcpEgOqN9aUxbnTi5cB_uAB4puSNexsJIulypMWDIuiCJt2NBqb-OaKlRYxYW6C5l5NMmOkA6XOCj41RnJcb2yh_KE-Ibj_bbbtrJ-FeOqfLmdVq8sTpglfYWLlUVypUIebrO3NaGCVsto_3NhyXK15FsPjkAU_IjbQRLGba2XFijHoipJtPlzvyjJHKp585IR9fqwbY04A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1BZY_kq3wGC_y4Bz4_2aKvnrFT6IX1Y3zLcofQJW966njD5EvSl1jLFICi-WqTWAcWnduV-icDabGAV9Aixf8WOfSiSQSDMmkAJARqEerFEmLWY5rKhVEDbGgHiT8k2eL0FZ8pp4IdQbMeUJ9PtJW7dmcMrGcCw2FWmFUwn0bCNQbYuTkQUtjANjR7neZ5jI9rIYAphWg0iCEpE-hmjAFL499oNrYpJ6VfC1Whk-URUUn4mAFGh9CtC0tsCepulfJPWU9g3R2dD8FrIiaesoE2n6VVC7AT__6RwhzqTmTQBpYY7Ykq8Wc4sqnnsm_xZaXsEezqVChExTWI95efeDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFdy8DfNJLGboyIY1rfEkBJh_tK_vIlciNk9Mr2CF6W2KoVaYR6eA9wLt7adFY0XKJT9T78gtVAWNcvvNwC36FCtRQOparVqaPfc4Yx-H220eOP83utg1MkmRlWXKDYKk5oAmUfNHRiVIwym8ZbvwUwDJ7EueiulwvevihOBZj-oG8yjWdXDtUbf3CVLs3ZRuOeINawuXj8xBvfunzWoDgPTQmZ84FBfJgtDGKQLcBpfzmnwd_6JXhth7gfJ5bywlNt9pzA24AxcVLfYEEhvGM5RJVHUYaLIAsMFogp2P4d3F77jIXYccOgxqqGJ6eRk7LULwXYSjBzHYuvbw5J7cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MzNGSfTMlDOL4p5whds-LLyAS1aub_N6n0WoloCYe0AOscGhezAFryCrvczIi-EGAOPQQrnVsdq4h9JrWKGoudZPVssXG3ugfXGq7w4qdFOkL3zjGKbAo3iPZ73lhmuM8ophVeiSt0UkrmJ9lB8P4XOoiwduH5t3UgtBPbownnwBNmBIsrbJ-HtPDL_n6kCUlJKFdZXsKUDMvqA3Rdp5iLkxRbVWeMZhr05NVjsyWms93KxDEkQHmf2CjKQh8YQHKrQEzEaBOXTp_Dh8c53Mz4P7TQB1RHEb5tlHGdZhwN4nQ-cVrx_zdCObt81RC6Xf3XGTHjcAqrPGwSXMCnJzbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eaGiRFY_U1MMJ3h-gzCJBWWpIu2iTmseYYdw1aweNnnjiMpPCNOHceEkGroi7CF2lhu1oHopvXku-81GNfHlRgHTuaDKBUOrucvrVD7UR1gxr-yC68jZqQOqpCBjry2r8Oh9UQBSRB0YtKScBY6BSC8vBmiNQ0MWPJuAKkoJXjk-l2-ORjtV8WNSlsUBUDtQi839BprxteqwlVyveY11kD0lbSdHJN8hu5uLT9ABo06EhQh9AQceqQ3EndS3lONAXXwGE928Zju7sD3HKf4I0WmF5R8gHFew33OLtkRu3Lfhdy1ISs2Uh178WWx0EDFIuBRwvcZ0TjPW5Tnc8W_CeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l0zK1Ri0v___6L8VjRmu6iotuxHeKOkp0gZVxXkmGZMSMCqRSsFtxCAS4B9ckvKFxE_Jx0wTD1zEwg55BzDDWXd0tS0ANAO_ElvS8FjZ-cojx1ElE7iCn5DOPPTf4yLqpkqEczeAA26LbSeLiZCgK_fi1ieW6fVgqNVFuBxyh0PM8sDmMDyEMs3VfGmUAAXv2AfGfQwBrz2ixjEgY_DfDPWH7pmNyXWEo4K4-uA1yZ2lkXXukHDDwW_D_-CEx-huSRT3lKeG51u4cJd-SgUoMh3bERS1o1Xh9yE8nrYR_DJX14-3qEOfY83yOYqkqH7SfdyIC9evybUxTbN6CX7DSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SmVUf7buBizPhzSLxYB-uDQETun-E63e1q9czktw8oJR3HxQ8sJNoRXNriiRSJSv27KHyybI0QnzE8xG7ITw-CKxkOkercfVUMr8bry6DKaT8ueMb9qjdDaY7pASrh5YgeUWxCGAQvg7aSWNXx7v_PKx4pgamcg0Av2xnIb2JwG3RvtfODidY0jYsUW2yczbKhw8IYlSskXQ_xgA4Kui5ZGs_Ckbie1w7cfsaTD92HBgKZbxHzTJiZxnArnskJDNtIkjTue0G5Bz9QoNb4dI5oCVGWxRTAv14TYs9QjBo-rBI6Aq4RdxUgI8ZZeZTwLhWfoPIRftA2U5R2EJUh4zTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a492ZsMDrxXACwVexZ5uu0HQSrIakSrXUFfRSAhFUiztfBkpOObgcC_qW-m0YgxK6-uhd-HFBf03u2wzjZPon4koeFEckePUy-QgKCBarbmO_u8jNtiXXKNZ5QvEg0MFmcew_nSPVWI4F2TiCKxBCr95wzIKjXJ1Ni6fMVU--Amjc7Fxs8HY8e24Jj6qgN045dr3Zq8deJqCMGC8WbNEhCViRW4IJGpPf7aoJylkkygxc4l-dIldHpAqRBxGhqMgOyHscpAIoJ2nG5biZeMuMjaxnrXuktRcLf0V1-Ix49Iz_ZHCq1OxtWlmzzHncuahM1GoWCX_HFqT9T5WYlA1HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSSrssOeZL2Hc46DdZhooZmlrmzncYykB0JeT_Jww2CPUXijOXo4N64rh15OpiKWDOaPIXAnawB4J0PkRTvZoBsvI5wGiK-bX2Dep7abVgCSggQhnnTiFRM2CwVNYlPxTUXnS5e7scieBVuxhQpknFT9ZhH7I9PXifktHoOdhimCkPD1bP_um3w0c1KScObbvcSv_fVtk50MdE-xJ9tq1t0jmnhV8_M_Kox5v0wcT_XLDxeUn4lddxZ4bMU3Ufxj5ogMDHMiJnSSLZ6qKSXy9YR4rx1itp8QRrFDoOarZg-aYbvVksta-3-s2ZKLXrnOKCM8JFHtque-TdTlR7-FAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkM1Uuai3nhUr6lT83m5OlyTT_DNN4k4OEY3GQFQiOnZa-WOdlvB0Y81YdgvKMYPii_oUvDH8uoXfVKatlSpPIb4nkDWUEHy9M8eK3vKR5yUOYdHq33cNefVM2KAzGvBp5qsWd5BLvxYpB1ATnIW1Z5UC88A9FFRkmjAgyxzOAXvZYcsuO_r37Ly-L8Vj1gfuRxLYLnUs9m-CsGL_uS-rK1dNy03mBB21KVvhh9xTVQrzSWOLsFkQ47mMgqQ8QX1jAl9ExpyOUUXBldd4W5UjB6ob0Vo4VtVE49w825V5JVHNE2nE9mWYO_VHjupIfGpY_EaptU5Or3PMv02o9A-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VXRh5nb5c1GRLm0hB_1hum3XXmexwUmjFK6SGQx0Yg_1hApm1_O0eiaz3emGOrt9zoiKxf3fZudXcMX_Nxzrcf55PQcBduryx703I1VcVyx0IlLCItzbfZJA3FpJfAW3MIa4un6V6Iw5-SS2qFrYO0irWI-ic2pUU9QVeFze77hTK7qUzARIreNV7DMi6SsAST3eh_rK4XOYQ4vwRGZ7zPJXJkbR-3YnUjtfvZxYk8dkkacv_B6L9nqtm0BH0wrqmReQq-5zzaE6I9ZCXu_hvZ9GBrPAOSiXnNp2f5f6Hza9HVH0y-gASgwm0BS0GsxZOKk_21SDmbMf5VFhJ5TCJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUFEw9WfJUriHRtBwQIPYQ31GM5FBHNVzdwlA9tCa0Q_Y_xX1T2MUmP1rjbn-q9a3kJ4c1xziwo-3PJAVVm5EgKeQFQdZ2C5nkP3FprcktwChVXvgP5jCyg01fgvHA_nQ-zQULDgRMPcxyk87WYir1aDXrAGh6gc-FEcGWHJ4K1zX80LyFOahmUFO5RpDPCeCfs45jLtNv86UJGei0FAazIQ4nL-QG-vCPAwLZPP2VxTQlYVCQT92PI97dck8l5V4NtUwgXn4cHi0o6bOb771WCQgP7QincZ2LhFUGHUJpX4h-9903rmfG32lz1uusfgh9VjLs09SkyzN-_9j1V2Kg.jpg" alt="photo" loading="lazy"/></div>
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
