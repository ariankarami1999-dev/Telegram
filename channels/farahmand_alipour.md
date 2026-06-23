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
<img src="https://cdn4.telesco.pe/file/LT3hMl2R7w7y6l6yPsDugVDXYOPjJa9G8Gk1FUKJ6Nhmgy4ULMkJzuEgGDC5EzO1keP65ohgHtQj1ODY-zI8fuwkN_N_CocBgfYYOKHSTgsDr5G_cT56Lx8CnlTUV9PyV0F4YLp2UK-z8E7UC-pVNqBD1E4ioe0GQo8wSI_eIT4guiIFX4ZC26Tf27e-si2Z_lsPJfNi2Z3LglHm9P85Yray1HaAvbuuuIMXFFXyEnC4aRXaZJtqxxXCljUaARVfDK2pmNa8qkTD-oHB8XLyGMESDan5GUPQJN0LPwAx0tz6yjOKHyQ97lKNkWW1aEfu-8w6LlZjz-HyCJGCYdi-Kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 08:07:29</div>
<hr>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=f4aCp0NGD5T8tHXyMHIA7c0Ztf9__pBQsgjwb5U1YnbWKT9FG8p1LmUZpLdlrQfoxIQp8TZIj_OYdJAbSNbI0jKLlIzVboaQicmRAkPB1s-hPAwThWxfUr-Q-dxNuOk4-cgOL6cAdT66zKuvbO2LJRpNeWZRVPjYjotnuex9j8sefHjYByChM4JwXFk22M9EC3XJRBahlg8GkIiM2C4VYJbtcyqaW_5llzELVwNvITFlu5kJ5GyqzYk5PhMc5mHv-XWsS2kYxgSfkXQYK7DP29ELpDoVgYBq3WEDliDWSzORSiCpu759OFkdaAvxq0ku9XvNKPlJ01J5hvewOeBn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=f4aCp0NGD5T8tHXyMHIA7c0Ztf9__pBQsgjwb5U1YnbWKT9FG8p1LmUZpLdlrQfoxIQp8TZIj_OYdJAbSNbI0jKLlIzVboaQicmRAkPB1s-hPAwThWxfUr-Q-dxNuOk4-cgOL6cAdT66zKuvbO2LJRpNeWZRVPjYjotnuex9j8sefHjYByChM4JwXFk22M9EC3XJRBahlg8GkIiM2C4VYJbtcyqaW_5llzELVwNvITFlu5kJ5GyqzYk5PhMc5mHv-XWsS2kYxgSfkXQYK7DP29ELpDoVgYBq3WEDliDWSzORSiCpu759OFkdaAvxq0ku9XvNKPlJ01J5hvewOeBn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv4zlnOPtBcyxvpNu53dEjnxLCY9FSYzpUGEa8o5G8wPV0waLcREqAJZtb1H5HCsKlWz-gXL0OF4KqsWCGj7jngJOBuZuZWxloo5L8fZtG3v2qHg17S8uwjZsitxOAPoa4XMtFpyqC-5HGc1BieB5QExO531_P-kz4MVKsbVbm2oc8Verf1I5Pg0478VUh0zrmwYLcEH-Cq-fA_VjyRuRAYfXBbx6pY9ulPF4GhZAdIghMVarN_zC2toQ3ZjtBS2_My7SIOPFYDYPEb24BaAGy4Dk--6j2r7KBlllinWIOBj-G2ttarumz_-_6uc9xvCpFnU2CWkG162nSZHZ0SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3z67X9JkE0iA6VGYTVb7vqyZUkVjtXzKoYKxqA9JjfZGG5BhKzYtjBpJkcJsb02p0Ud77sD4jGuW6DVr4XLmmMSUPfX0Cu1Rq6zDp7kSGLEmlkSwDYwlPcVeLOmBkCR3FE92fN5_TgNtsEE8StX-h2D3EvnXXis_Gk_Lwyd-CQhBCOWxcpmpLiCyATmOQxW4b5xL45RmMoIQkMWhmaMFbflpwE3xjTw5rlrpjm7Qw9zekNmreEJhEyI6R-2zIAXOPz7HOXBVcPfAcBWwCZx0BTwK0NRGgXKGVFIB6dqlNXeXxqq3vMH6vI6DF7i-rTrD24QASs3zFlZo-t7KpW1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScwO_3xK60fcKFljmgBJYNV4e4DxBgqzEO1uLenk2HPvA7TS5onQn5rZA_X2yNFwcZsHXBsbUikXWCTpD9Dr1bu9JtbtVedrgMQI9QZmvCLi_PztZ6ukdWeP28RVTYs88n-DsmIQ5n_V6Q0rhUG7HnPbRNGF1ZOungfj6kIo9mnYIjjQy8jshqJrI5xfyrAB3nKIrxWKv6FCSfeBJ914TRN8xF08ZwcpvygjimUi9h5waxF8iLjah4-GFvuCGZuDM2YdSyRHbpCg0zaYXAeVt7Z3CMkGrAUPdK886X9d2YhCYO6u2zrCJiFyY-7JMqw6eW2Hq7YRWaeKmdo_W9xGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3bxx4fxSx63_FfohgEqFjE1qGXeTDA3PbgbUXfn4-UBWE2tNwtZpY94ILw_HFCpqV7gDm3U4qyrTJW5URhuOqlkFeXrX0msXySBvg3VzD1230_-Ky0eoCs6ROVCXB9yEqoxkBhT9IDTTaxuRapMh9WoVAFXVa8R8sazgR4khfsfc4kcWhD4G3fe4VRhKnJXsgjWJqnbEHE0QbKwE1m76EHzHQ282hdhodCQ3QGwSwwtdsJsVG9Mo6mO7LCXniobGjJpBYTnlr4l-RS8PeVcDPWe58b-aCKLB1-TRzymFHshMCQrVLVtPMllBtxnnLo3bolui9VpDrC0FUrH-nitKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMEJDHImA3LZAKp0PlrLbwyqddPAs-Nx8LbBSYrTVEqk23uh8oppLDPO-HYR-MOlGIzDmRfs-ftdSEVHW9-1G1UZQM0FGPVxRIQz2GfdVji1to_LDR-UkVXAM3lFNvbITVwojZpIy4C7prwsBuGcV8WcAu9xUihIkvGcZHK4YU_FOz8QP3ifMaMLHhA74iSaGQmI9cLQf8d_kx3Uj1RZaufuYiLQZEOLgKgQEQryLmPjDS1hQi3RShukQZ7_wjDwZ6ZijgCHNatQ_MDjeQbcP9Tysr2yJh-G8xzdobbrigcfzNhDiF6vrjxML2O-g2gkFjubhaSgF66LIuL-WQbElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYnfPFsRRGpKzNNfc8YAodSzpW0H_a4thhaeJ_XXbdUtteXIyJye54Rvd0MhzD5SIhc_I_4ReovGtP9fdpMdQG_T6SXAOJCSQhJDXf0FPepfXTQTuIdkaVtZkgyFia6jPmu_zSkL2siOFaRRmhMX0IRz5Wq9itjlC4FyOVDD4LGYiiEu-hXgZ6xEDzhObUaQRsYEjIieVIZmSY8oPHs9FUt3SXTII_D-bFZWAZiXWxSSorVS4e_K6MO042IcPNZznsnbIa07XJvLMYhdT_HWMSnRNGgbFbXLsvzNsehd8J1UdkbieK68wEqaWYsUzoYsNArgmdkkh1KGcgOSLSoUVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGDpQYbsRnHcRhiuLK-CHbGv71MFTGG5GPZFl2r3elL4oKOtw-pv9Tvnisyu_tgGOmHwRc-GEKsZfk60emItmd4mipuwhF2CADw4GzXrr18Qlorbg-vgCyJyee973YEmvBD8D3QidZo5AI7rRGyE-_Ey1Dj08pGUu3CJyu7AtKX_q__8l954K5B5H5GQwtScfyCuq9nFb3X5YqD4tVmL1oFz8oqmg_EWueYBcptR_I0t-ZnSENUAa6XmO9UTIh_wWt0JDReInQVcx7uMKS8GPQRJos-TmaSqySb7dOjyU-fqnA-FOAJHGXHBqdR_U6HtoMfL_uYIWn4-azMK-2W-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzq-SJCeK5iUsRqrtzeIl9PiPEA8q3oSzYdnbVRLY80icvC_4LTQciHrnV9pRKte7WeyE-jBbb7S46Bhhx8Tuf25UUn-H8UrM2QSzbH9tgN7ATXL_hE8NlfaCv8jXLQ-QZlxogfOW5npf4VGrKBt4wovK8rC7H3y4Aak66zjJteOhkmZQGcBL0iyKnTau4tjoTyYssEh_wu5vzDhg_G47-vDe4dl1y58G3MUmn-zfxX0DCeTHV6yT4SSVYNg9lOZM0NYQxG1q3YwJpqAgiFwQ6A0qSXw5dtPjrVLT2DRu2pTeto4sAKY1rDdAdPhW5d20-XCq0zuWNuZ0o8rtW-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvabggeV_gp5uCRBhKTWs-Ue7yxOdq_rfaAOvs2UrdfEteqQjXhE79lev_iS3wcYrEYbbHceY38H5CKlIjE0ZQ5PByez3fvvNvENYL3xFw56HtNdE0H37mOJ_IG2wmtb4my_GBs7zEnlnky2Vx7RbB7Leir6DWzCQ-TsdYmtJZoFoDIuonUYYtxUs0bZV6xIXj-HQARCXDUVW87GtKVKrRm8L-bx5DDclgfLkpUV8g4i6ZCBxPTs46o22Gn9nO9CaIvMaJaBchZIOyuyYkC7xja0G_LV_lC6brjsU9XPuUSsOv2-Lka37BFRgz1MpvtqBo02kRp7vE9u5I2ZHdnvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkWDD8rY5G4nSdXYwW2TdbC0X93oyNnIstH5hwDH2iyhDhujGBIqXTR5dvrDHfL-1VY8eXjMxUgsCwIPnIm8pS-k0Ep-BPMRDrvRlCR9A6-wz68Q_L-TbBs9QIZbLCQ3EEC9g2LQKU-VbssvD2Wq7o2i8ynJqXx1m7A83swoqqK0tWd2augq-dLFWjH2OmGpTbvdljlCgh0E1iJKIZoSykjf3Sv6urKo88iH9asobAHH6kUKZWBD1EEcRqTWpjKBtAxRtydDRWlFfLApnE4l7xaFLFa_ux9TPAmMtN2tHmY0rIbobhpMzGU0EEP3ZnuVpoZeV1v_qOJONCxpVnzhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9tfr9ooPoEpSVExNRXoTSfCi99IMOf43EUTZkyDnZJ1VEqhOs4ICgESZC3HQ0v5oUWv7MdlQKkNGMO0ovUwgHlIRpGmcF4E8DlOqYXizKzp9UyL1Ygkf3yjSRwQzumloGU3INOSlD2aDlYdXgQ1MyuYPKyNGclZub7XjpYRsVmXGDMHOOK00dDUArt6W9XI-sTMlaMfIwR0skCWBi_ty4nU1L51Mcwyd2F9O0tfXn5Na28Sk41vDRl9s2ujcxhwgKqJl9q5uuG0dFXFerU69EqEkUMwPDNttQv27Ozi8P0huhI7tO8gDeBQthISpM7rZBz1DjDBNuj-8FGeVrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIY4IQfe_-jkn7hX0ZFA17nUWwMhxDDZ8t5qK1EbO3GuMi5nsJhgVS5PkAralxHLinuSLgFLoQ0qoTIsAns470aozIMKynerLLRoGDAdCvsIhbR8FeB8pU2cDHrUDjeX8Qn2nX1Y2B0U7Y33CCEULPlPSap5fCb_eCa3ezQOxJF4Jxrlc8tAEf3M99cEtnCyRyGP2WDYib8tG-Qx0vh8QJXSMmaBovXRSk2vURFQvh-Ca70ATLxUnjGvEmRMsakCEF7HksgHL1da3YfyYQkSx8khSl9BFf40p9ZOn5f98fQ0xWG1Eav2qpoLEb2IvTynju_zNSQiGFPOjZSe5lLGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgZCQD9qze35xAC_36bLogtEauZ6N1SEgu836PTasnYYXXXT2JNueq2TD87unYjmr4Nzb1mVhnKdQuKuTbc5EKGn4P5r8LgVUwpEeRinHzZ29ec2W1Owj_sCnTbxGXV6bVOZW_ib6aIDX2kXFfvC8BKhv4LpCYb9HUf849Azu5P3nIVdlkw1pwmUy8D_QBcKM2HzhErijIRKb0UduCB0IumIRCPtvQHOg_w2KTstDiXIeerNDptoPn06JstLmDuw0ymIdCnA2Ft2iv8f7CnD3Tq3-Ali0P3xVKYof7sWRTD8rk3Vludcb6tBqMywKSsC6HHz6PMPbzlui-tN5Wbinw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG-3nx6yxTpDCHwinKjfFTp2Q9WQgQK1TbqoNsvYZempkPgGVtSm9NUydhQIv2WfA6RTk3E9KtBBpwMunMPBexng0NzlAvJIK-k3wELYR2GZUnuEXhW1wJznm3NPJsV7WiN4aAWbLgWJLaWVuJWyhHpResKBMzF6OZZgiUBPTCtjGEarLH5a5Bcb2h9N8fThUuasYJi6-9eDgw2bFdI0zLK-n_CQGLgbW4j7_9XM7y0lmQaGElfFF0j2gVkObFEa8MZPoxACCFYdQwvzMkl73EkdEtPMK50wYPV-Vk8bJ9mIk5kVAH2_zAvbzQTSRFQ8BsjyOtCRYEDNiZCfIHlh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=d3SsGR8lGAe_rHcJmdcK9CK21d8H87A9lwIqBEUVfDHom5RDdpWjj09nW4d_PUiFa9Q2AFTRJP_7MrQs8e1c8F2Umsu34kpoQW54Cn7cDanj-s7U8uB2EYAwRyS9kg7EX9ER8cK-a3KkmUOaYCoTYeSMde7ikTtG8q0pQGnzXCDtB2cKqTPFmdhOl_0PW8OIsFYKlJSLrpYZyRcLPfCw0-1PKaiuhCTAW8aEjMZQcVijUD04aLp0zeDweIuey71J5wIS4I41RW2VdUZnZOOUF8-D6cOZk72E2LXYUPKXbocamqSURcBY34AewBFnJpaZvm9Om1ag1BBPb3Hg0CTTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=d3SsGR8lGAe_rHcJmdcK9CK21d8H87A9lwIqBEUVfDHom5RDdpWjj09nW4d_PUiFa9Q2AFTRJP_7MrQs8e1c8F2Umsu34kpoQW54Cn7cDanj-s7U8uB2EYAwRyS9kg7EX9ER8cK-a3KkmUOaYCoTYeSMde7ikTtG8q0pQGnzXCDtB2cKqTPFmdhOl_0PW8OIsFYKlJSLrpYZyRcLPfCw0-1PKaiuhCTAW8aEjMZQcVijUD04aLp0zeDweIuey71J5wIS4I41RW2VdUZnZOOUF8-D6cOZk72E2LXYUPKXbocamqSURcBY34AewBFnJpaZvm9Om1ag1BBPb3Hg0CTTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcxMQagBtJQxZiP4VdeKNIsYJ5l0O0rM_iusNmUqUJnbFZuhPgd8FJZHT7-zDT09tq7yfx1vw8M_m3rBJb49SbjogN5Ph6s9yXBjWQXFWep8UeD8r0lIKmZliKQ8aW-Cjqvi5AQUu3WPKJ4YWXFg6wmGg20Z8qdBPTEp9__FPgwP1db2oT88LI_0htbHLrQ2RuRCb_z4GRMx5KPjUfkzWH16qWxIMAXsoglN6ewRsVyCHwkpy8wm0BWmvjNS-N0838GwsKmA_MTX-aVz95zjagor9GaT95xYyTRTH8RBaHHQhv_T1np5KKwOo7ECAGXavEy7hUjYYpSLcXc7pH2VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=L64ixPP1-fF8x_DUgVg74AEoBcfQfCgY8qKscF4KFswtCOMoFIqj1cHDXrJXEla1JVwiVZsKANbPIC9wDpY3c0nQ-TeeJ-r-hnCS105BbQpCcRYI-4X4ZIWu4BC7YlAZpbf5wtutUWYCfyzyq2SF_abtTEJW0bAm0a7rp1inCR6pKDkWrCGDv9cRjOfwE5FMKFqNypRZF25iRDzBB8vVjxM86vPIebIs9dBelmMMS7WTJ8zT7Mass_FU15E14rZ8ObSTqHNYFQ_1DLzj_i12pd7EkJCbOZY1DvYvJo7ZjlEMBbKNgMvg8dkHdV702rUfkWFa7KjKO_aBOqaUVxA83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=L64ixPP1-fF8x_DUgVg74AEoBcfQfCgY8qKscF4KFswtCOMoFIqj1cHDXrJXEla1JVwiVZsKANbPIC9wDpY3c0nQ-TeeJ-r-hnCS105BbQpCcRYI-4X4ZIWu4BC7YlAZpbf5wtutUWYCfyzyq2SF_abtTEJW0bAm0a7rp1inCR6pKDkWrCGDv9cRjOfwE5FMKFqNypRZF25iRDzBB8vVjxM86vPIebIs9dBelmMMS7WTJ8zT7Mass_FU15E14rZ8ObSTqHNYFQ_1DLzj_i12pd7EkJCbOZY1DvYvJo7ZjlEMBbKNgMvg8dkHdV702rUfkWFa7KjKO_aBOqaUVxA83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=p69cXmM9yOnmankqb0lyUfNyKjYYhjWcdWw8ggQcL-rG3B3fy98hkvtwPpPhJcyMhTEG0y9wf4-Y4IwdS9MjUBofakFuSEEQIusZ2ppsXZAfO6lIT17xd_JZK5mf34Ak_MikwoBHtUvr8Yp-z7lh2jKl8aDAXmjgAwMQf6JB7HzpkBI2wh3lBoI8xiBd1tE8MUotgJrxb_N-lHx3CkERoizZm6UqYFLB4fWU-Hmu7ws_fGoe1YQY6uPWSSV2oW2Ph0nJnqmQiLfNW7RfljXwklKYRX1jgRw1gRCQwnYVTboL4dJz_CBPt97OJnjYClY5J8foBU1db9pY-7JQ399opg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=p69cXmM9yOnmankqb0lyUfNyKjYYhjWcdWw8ggQcL-rG3B3fy98hkvtwPpPhJcyMhTEG0y9wf4-Y4IwdS9MjUBofakFuSEEQIusZ2ppsXZAfO6lIT17xd_JZK5mf34Ak_MikwoBHtUvr8Yp-z7lh2jKl8aDAXmjgAwMQf6JB7HzpkBI2wh3lBoI8xiBd1tE8MUotgJrxb_N-lHx3CkERoizZm6UqYFLB4fWU-Hmu7ws_fGoe1YQY6uPWSSV2oW2Ph0nJnqmQiLfNW7RfljXwklKYRX1jgRw1gRCQwnYVTboL4dJz_CBPt97OJnjYClY5J8foBU1db9pY-7JQ399opg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqWQQTntQ1BppWx9E4Br_1VL8PO9vnfrBqMQ4lUhr80IqWuQp5ByZeUwXoVU4s4A8Se0SRhm0nVi60fXCE3QVta18zOLnc1XIF3So0ATkGQsA-v2Ve3VqafI1H_clxEKPDHGGOeurRBzZQxeWGuiDWUgyeN65vXsVUPsa_3C_4We8O9kCa7UQHQ8b6ZrjIxKw2kFqkOxuzHOmsVKz_ngfE7fOeX_CfgYinpMkv6PLS_3r4J8AgLAS80h0kddQKi-IvXrcY2BAlB56ivf1RCdq8UkYiNoQ9lFN3dhv9TYJTrfRMW1XljU6f1i3k9g7rqlEn6EU6rDm3XMWGTSJHa_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VucjHUXXLGAY5oxxLEHDAlVQbqd0wX3VpS27LLYvKi9o9_qaJklbUUjhcfNy5-Lvc0eFoevpnP9aI0y_z8lzJWx-fyHji_CWRfzFHFvc5FCsgoh3Js8LAzavzsmHm4SKAgEwbl2vwKG5XnCul_6wOeeuHz1X2JQKe9S1ttE-6l_8JvMHf7q-RIT7eVDH_kBIRdpVZjx8_WcziW_8McvNa6Uy88nK7gW6UzdkOa-srUcuT0R2As13vSY6FfyssjhFxB3wRTKygMGISPTTf1CUeGfikhFdaEKuFTFsQ6wIyriktfDiozzzXxSX97Ihp0VufAu5NJj-LByI7VK-AgBApA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=VucjHUXXLGAY5oxxLEHDAlVQbqd0wX3VpS27LLYvKi9o9_qaJklbUUjhcfNy5-Lvc0eFoevpnP9aI0y_z8lzJWx-fyHji_CWRfzFHFvc5FCsgoh3Js8LAzavzsmHm4SKAgEwbl2vwKG5XnCul_6wOeeuHz1X2JQKe9S1ttE-6l_8JvMHf7q-RIT7eVDH_kBIRdpVZjx8_WcziW_8McvNa6Uy88nK7gW6UzdkOa-srUcuT0R2As13vSY6FfyssjhFxB3wRTKygMGISPTTf1CUeGfikhFdaEKuFTFsQ6wIyriktfDiozzzXxSX97Ihp0VufAu5NJj-LByI7VK-AgBApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVgquxKc9lmsKYhCNwUyCclQguYkw2H8ZXaN0lVkuV1fBIypoLfNaLhi0shPfUhuEbbf3cEy7HMT2FI_0HOql1mHmIyL57OemjWcyZ0Z5F3pPu6JSpBzDyhQIV5fLUokOp5o6Lg6UL6udAaATHmkSE6YB_H9zsCX3kjYuoTygq6xWhBZlkpYZF84F_9c1kPeC5SBtP8PuPT1h7P0uniqIxO-OzYN77AlNcmX3vosNz9r9fvnH0MBAH2-uuXAkTGpt6XvHVuRzLo9vxHks6BCUwh8K34OMzoPvIzfjcqF0y9GFRENDauHykYRJf0CqJbRn_1fcRyZHr2WE101QGpClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlcLyPsC_EO0y7Jf1sfw_pMbtFckcpgCUO3XIoS_RVF1VcZjiToXZB1Yb1WVHhgYgcSEuvpGT_2-agYTVlBSSEZM7Z61UxNEQFdtpr0rI5mkMC89GGqxz-hZkYIz2fmICLv0K6knFWB6Tw64W02BnHbSmwBwwBZarN3wb_ZqTER-lNsVoGwcRSjrRVXPb0X_MxAMGhxHad5znNjwnMmEibWeam_FgGLwrJaBc7fiOVnxK6XIri8KDlhpn2NLFxJowr3CZHBYpJfXnVnnFexnL7cLLdINMV7af6wxFfiscVuORzjcqmcrVMBRHZ-k1W9r0NrVZ3tYPcCZRCz6QNDkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWpQLoyihmDGsFyUxwoZ4OmgqSQe3WpIy9toUd_l7ezAqy43DrbMbnFxfiCRuIlePyBYyizaXf2loxTcL5Hgw8UwlPkR4bsZ0-1KYA86PEz2D5lXB5Etw4R8j4iJg4FMt-YHy5hFmgndJs6RTZTwvYv2eOxq0EvHiocHjyQ3lRP2tOAiNiimE0YxPokvCsIiCCfWvAb3gVNY-h7fzwBDOmaho-OkCTIERZ0U4ELths3ng_oS4MzUtIBtCDGzGz_RMqigvWwuNbx-gjSlXpABiDiFaE4VEcu4r9G8gCwZG0kRWD7Ss_uqLXkJ5QbzujBlTOOc6uY5IxFs0JmHlp7zyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnxTXkMkc9uQ2--ZxciyexWQIED1f_N8-Qvlbf7X5va6juU89bsmDY29IbbY16P_2N9k4NiAi0k4l-pYq7V7ffxfmy8mAMZMnppv9LfWgrO5c5E1RMvmNmKNqr_gsoq6tBE6hhxHrTGYC1Q1cNtxFvVq8J8tQxRFUCoXJ5P2BZrUygDh8tLp74BVjMBOsuMF1aBRWw1BLGw4pl1C1gd8exS93jjf-gZpA8q7nV5Z7g7CzB6_3wXvfm0_tzGs7d0vmu8rWcP5pZwb_DArOlmOO9U1gYwFAlPi7_pLFmbIPcZRLyrTlOeWcoPqT-ZE--HFjpwOCjPDJm0uicbSbqOTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=hKH0406rTQ5-o6wNVHSxpKTPxg_C_04hZOU5si7gLHHNTicbTT_BrXKAH6FwIGiaxqI_LUvo68turpj04AU1QBamxRbhMqmxECcE4nK79-Zke_bdYkykcW08gVvuXWBaoH_xKbQkyV42JTF-DSqGJhICCJy6OvHaM7TIGXeZoK4IRMepPXDa-dPZu6zddk9Nnd4VfnJukfL-NvKHk4lUusKCo83nietJpA6cSXFOluugS4AnRXiu-NwNlVA_7OQbu3oM7xu8iiwOAc3A5ZVn0P3wQLTirLBZOFa4HDW6HKoGbkYQqxID_evTouxsmYxMRVsROMJYgWpwNgtYU4xPNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=hKH0406rTQ5-o6wNVHSxpKTPxg_C_04hZOU5si7gLHHNTicbTT_BrXKAH6FwIGiaxqI_LUvo68turpj04AU1QBamxRbhMqmxECcE4nK79-Zke_bdYkykcW08gVvuXWBaoH_xKbQkyV42JTF-DSqGJhICCJy6OvHaM7TIGXeZoK4IRMepPXDa-dPZu6zddk9Nnd4VfnJukfL-NvKHk4lUusKCo83nietJpA6cSXFOluugS4AnRXiu-NwNlVA_7OQbu3oM7xu8iiwOAc3A5ZVn0P3wQLTirLBZOFa4HDW6HKoGbkYQqxID_evTouxsmYxMRVsROMJYgWpwNgtYU4xPNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SCLNXQ3MZfWZpZ1DRLDBuY6m2zgLCyX3Q4aOEgNKKe0dCDsJNzq9RnoWUxPVZNiBemUHj1_8zSV2H0B_jyLGWSpWJO95GvZ-KYufGOwj9LcyRuz_VHE4lQXurIwDfEsW0Ya8zt7l6HP23VtvzQatgUYhzbdMK_GsMorbrkgv6tjwEm7mvtaoY5x1sRnZlLr3WVOOVHG9YOG8Txh2tp_NW1vXNusuGFuIiN0pijjMZBOyjVyDJvl3KHYh6V5xjh9oTWuk4PgJPIuI8w8naMGutLrwgG_d-C0OwXpK7yANIhKHkKfvrCQY6xH5K_easlfyFyPdi0NrNA5eEtXj9r_5zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SCLNXQ3MZfWZpZ1DRLDBuY6m2zgLCyX3Q4aOEgNKKe0dCDsJNzq9RnoWUxPVZNiBemUHj1_8zSV2H0B_jyLGWSpWJO95GvZ-KYufGOwj9LcyRuz_VHE4lQXurIwDfEsW0Ya8zt7l6HP23VtvzQatgUYhzbdMK_GsMorbrkgv6tjwEm7mvtaoY5x1sRnZlLr3WVOOVHG9YOG8Txh2tp_NW1vXNusuGFuIiN0pijjMZBOyjVyDJvl3KHYh6V5xjh9oTWuk4PgJPIuI8w8naMGutLrwgG_d-C0OwXpK7yANIhKHkKfvrCQY6xH5K_easlfyFyPdi0NrNA5eEtXj9r_5zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=PD6lz4-8aXMx4fEDuQ_6saxKRwkVZt3vwdE_l01eNPOQpXCxpIvImmE-GrdjPXhxtN5cmjOrs_v5nNd2xtfaw-jjUBsePtpdHJ9pLfDAFK_-S3jiTGm6lA2aEnT4HP-j2ojfQBsHwkqdhdW6GUdHHanA6i5YXalROu2c0bbw3xC8ZdCZLC7p8-FAP-lj8ckjZRIingeeeYrpSAtbA5113sxx4M-tr7GKH8AigI7JTOONgDU76qX2UBStwHXf_2_gTthJ6WJpbZqxGvyiPwDkQMTK_k9LcVS1XP0Xnslx34dz0UWY3Ht35gqPGGnN1bEhQGzNbvwUPIKliGbShuyz0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=PD6lz4-8aXMx4fEDuQ_6saxKRwkVZt3vwdE_l01eNPOQpXCxpIvImmE-GrdjPXhxtN5cmjOrs_v5nNd2xtfaw-jjUBsePtpdHJ9pLfDAFK_-S3jiTGm6lA2aEnT4HP-j2ojfQBsHwkqdhdW6GUdHHanA6i5YXalROu2c0bbw3xC8ZdCZLC7p8-FAP-lj8ckjZRIingeeeYrpSAtbA5113sxx4M-tr7GKH8AigI7JTOONgDU76qX2UBStwHXf_2_gTthJ6WJpbZqxGvyiPwDkQMTK_k9LcVS1XP0Xnslx34dz0UWY3Ht35gqPGGnN1bEhQGzNbvwUPIKliGbShuyz0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=Z84syJA7sFr3QXze0F_Dm4rjQvr_gE5MQBcySu1Zg3xC8v6Rnn1LSGyfuM9OMFnyLXJQr-NQDlqSF_BodvU5q2M3Mb0pNRSDoM08lAn1sBu8IYWMFr6MNVv9TfnJpB75fc2sQcxG4nuvMRg8UOi4byzsck9_hzkdbVaoNxtQppFoq1BRW6Pq0QEEDmdZCNYo3iWpIejRfU_PxoL21wvCruJRnmPWGXJVqfKr_lOp8b9RC_CEi6QSpncNqDD7dwIfQbyxFlKpw71BfkdN4wToWfCah2itPnm31i9hr2lwrCoE9EFfmp9EhjwNKj0pbDIZSDsB-3fUKCEHoUzoeFukYyHFa0tToa50-Fe2NpBiyiEoVzPhXL8oYFCXsIE4h69uiLbbmZXI3eX4cHMf7gUFcQp6lbwKZAOx5dPh9j2TW6XG7NBFMzfMrrUh5AIPZtB2cAzwzW8XsQ9HESHFBGogxDgg6di6GXBhlaedHBkunf2csdFagV5H7vNO_M3rVIzQBOHwsfpIDjAX_LXl8K38Yh5yfaJf1HEyYukfKg4Xr8BoxAAgt8_Zqlk1wmE0eG9Q4N0F4XVdycQFi0E2tNvAIX-PTdQi8auaElwB5HT23Y-sJp2U2lZb_Aarn1vOkHo3P91gn2O1bkaFI-hLl6nP65K6M4QftI0LKr_BZyMq6Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=Z84syJA7sFr3QXze0F_Dm4rjQvr_gE5MQBcySu1Zg3xC8v6Rnn1LSGyfuM9OMFnyLXJQr-NQDlqSF_BodvU5q2M3Mb0pNRSDoM08lAn1sBu8IYWMFr6MNVv9TfnJpB75fc2sQcxG4nuvMRg8UOi4byzsck9_hzkdbVaoNxtQppFoq1BRW6Pq0QEEDmdZCNYo3iWpIejRfU_PxoL21wvCruJRnmPWGXJVqfKr_lOp8b9RC_CEi6QSpncNqDD7dwIfQbyxFlKpw71BfkdN4wToWfCah2itPnm31i9hr2lwrCoE9EFfmp9EhjwNKj0pbDIZSDsB-3fUKCEHoUzoeFukYyHFa0tToa50-Fe2NpBiyiEoVzPhXL8oYFCXsIE4h69uiLbbmZXI3eX4cHMf7gUFcQp6lbwKZAOx5dPh9j2TW6XG7NBFMzfMrrUh5AIPZtB2cAzwzW8XsQ9HESHFBGogxDgg6di6GXBhlaedHBkunf2csdFagV5H7vNO_M3rVIzQBOHwsfpIDjAX_LXl8K38Yh5yfaJf1HEyYukfKg4Xr8BoxAAgt8_Zqlk1wmE0eG9Q4N0F4XVdycQFi0E2tNvAIX-PTdQi8auaElwB5HT23Y-sJp2U2lZb_Aarn1vOkHo3P91gn2O1bkaFI-hLl6nP65K6M4QftI0LKr_BZyMq6Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mNyQ0IByj9CpGypduWo828kXWs-TjyF60WeepYAUnbLD0g9t-fQxnKnQ2xqOH7aUUIZHNnNu-JrXjm0SxxX8lhZ72h5TmiqYiLz1xfCzdo-TQiJK9QntyBZJ195VmMQI91dTzh4zsMTZeDE3ifp4-yMqL6vDkTsRiYIXWeIW5RHoXk8RNv4hgAms_Y3ooE2Lsf9t16wF0N2nYXGbgDr_0yoKZ2g5mipnK1N7kCuVW6ioEwA7KGwaIi8--JPPsr2KJNuYCuqGj3ZNnY6f_kkw496SJFnCN603WJMNhwjW9l9bgWNRHPl6IUa3I6MwTpQTVwvZDds81ZAIbvjaHAbG_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=mNyQ0IByj9CpGypduWo828kXWs-TjyF60WeepYAUnbLD0g9t-fQxnKnQ2xqOH7aUUIZHNnNu-JrXjm0SxxX8lhZ72h5TmiqYiLz1xfCzdo-TQiJK9QntyBZJ195VmMQI91dTzh4zsMTZeDE3ifp4-yMqL6vDkTsRiYIXWeIW5RHoXk8RNv4hgAms_Y3ooE2Lsf9t16wF0N2nYXGbgDr_0yoKZ2g5mipnK1N7kCuVW6ioEwA7KGwaIi8--JPPsr2KJNuYCuqGj3ZNnY6f_kkw496SJFnCN603WJMNhwjW9l9bgWNRHPl6IUa3I6MwTpQTVwvZDds81ZAIbvjaHAbG_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=hMORjMTZYlIsfnoIr1YYQbvEY_yJ2wJ78L1VnCF2DuiF4wC4gshN6NNlT7JDxfpDexHpzPFR0R8iCD_eP8PNerPN3j9F8ekLZVRWBt5NyQU0U2NzIh0gGdDLjp4kTrWShkM554683x_2WeNP0w1wmBBWxp6X8KTP399aY_kEyUKjkXaXKehFW5TO36M35j7amUbYedUHGYcGJf3BlWKciT2T8IcFRy4oudOtEsX-sFl9g4BqwOPKFoMcB3cc-2PE5a1D18xzmPg_UHgF070kh3jVo2xBoJW8gRpvznTYBog4Wxg9eVW5U1WkwOZkS4DT_pi-zWPimrXi8kk6Ef-DmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=hMORjMTZYlIsfnoIr1YYQbvEY_yJ2wJ78L1VnCF2DuiF4wC4gshN6NNlT7JDxfpDexHpzPFR0R8iCD_eP8PNerPN3j9F8ekLZVRWBt5NyQU0U2NzIh0gGdDLjp4kTrWShkM554683x_2WeNP0w1wmBBWxp6X8KTP399aY_kEyUKjkXaXKehFW5TO36M35j7amUbYedUHGYcGJf3BlWKciT2T8IcFRy4oudOtEsX-sFl9g4BqwOPKFoMcB3cc-2PE5a1D18xzmPg_UHgF070kh3jVo2xBoJW8gRpvznTYBog4Wxg9eVW5U1WkwOZkS4DT_pi-zWPimrXi8kk6Ef-DmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFV9WPGvDsrwqQFtMSgTTUuYlBXRMUVBRZBO-AKtnD1KTxUMKO7p8aZw3rCReny5WGHTMgnXAROBb12JuxplJ4fX7JsIYXuedcAameTFWQZqpKDRrghawWxTqizXR0Ff0B2sypkJcWDB75qpDb4v96LE3IsXjuGoHmirRW4bDfJa7JPFGxJZCND9Uv7lNaFe9_PvD3OOx8KWhoQqjiS9ETB6mGQEYff-lJ6Q8DBAzcW26OsBBWZ-y5pa_sQMza-JBu1KlagbPY6QntsXuRl31OHidi5EqHLx1GynwugFMdMLqVHIQROi9uhU1c7JViZ67mj4FLhC1fYZiIA7v2pHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ZssFF73QKuzPpR0DPJyx2eH2Qya_BnLcp_89MYwFkHYiUAEYpTvg9OH8tLpgpbInPkVxjQScNdUYBiH43Ydf6ngSnTx13ubfjsiy2HXDyFrj3-EPji8OWSCZJxgTFosDPzyWOnU6nlDw8LX553hlcwvjSojp7WIIf0F2_yKrIQpiwiGexgQIuwxiEDcSHBCfRlhvpNoW7EPo4Qgi_BxdeaDEJCNF5p60_TbzcZf31pV_pDiBLL1htLFB2Z986jxlOsP79C0y81qZ9rFd7D3M8qEeRXaBB49Np7or7EDujTwG6R8mozvlvzb44GzBxVrLj8XLruvwuVeDFHLL5GXU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ZssFF73QKuzPpR0DPJyx2eH2Qya_BnLcp_89MYwFkHYiUAEYpTvg9OH8tLpgpbInPkVxjQScNdUYBiH43Ydf6ngSnTx13ubfjsiy2HXDyFrj3-EPji8OWSCZJxgTFosDPzyWOnU6nlDw8LX553hlcwvjSojp7WIIf0F2_yKrIQpiwiGexgQIuwxiEDcSHBCfRlhvpNoW7EPo4Qgi_BxdeaDEJCNF5p60_TbzcZf31pV_pDiBLL1htLFB2Z986jxlOsP79C0y81qZ9rFd7D3M8qEeRXaBB49Np7or7EDujTwG6R8mozvlvzb44GzBxVrLj8XLruvwuVeDFHLL5GXU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRmWdQp3Tk1ABWlh0MyKfm4GJYD74r1fZm7_XyJrGu84z2t68_X8WBz88UCTjAex5-VnxtyWuwKmc1Dux_SYCAANy26ecn5nDT3pE814rhd4kdYv2koZ9cC1xhMbMZOn3l6OwFeSvHbHPDYpYVAYRuA9imZoIwxXGjglEw-kcKWPQX2rQ0xoeVAbKvoVKN480n9j2dI3tOmgCGyljwWMPjsmBHyEgNdg-LIr0yLbs7BUyw5KeQQjag8v-4AElBPcml2yzSEtid5lvwfbREDP_FzIKrdJWHds_rf3YcKHo3wBg5cuN6lyzR6Ke8RnjALXBGVEXD7xFh0KiXwByOCb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5g4Xt5cSaMv5Zqe0hlRRH6hQbPE7eaDzOYCWaUAqcRUSG4oOyV31oni9pESYcaZBD3nxVMhm6NQxQSUCoyuXSpLK1wbamWdvvpqjbCO8l5EQyZ2ODC1T-5CpLfOWUpNTrbJF2v5l3i4NX4xkQI8ZuTS5QWGgzCDx2y_m3dXWcry3eqktGf_iavkgd2JDy8M79lruJpwjsn-RlNRiKBC1TZNtAA57m08_-3mAYDPcr1cjJYCNCr7hv969mr7dEOfChe9JX0M6NeVUrgPX6ECZAK9etL-6vRelTi6uKxR1p6ym9hgVl7i2GTvytnUuUf3KrSZjfjz2-pfbSyh1XIMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=QgyuRTANHTe8stxA6NHBD-pYJqN0_W1dj-6uSTaS6nxxAD7m2zUVtgJomWOjUKK-11ffjz7Nyej_VVb-Xog-lZwb_YjrGJ9cTO0njxEzOhf5Pozm5LuF0ZOmUsYRBdEKjHGcEdvsRJLJlNT9T2eMPr3VA22151Thtw9qkvyzY22-EydxMC5EjyPIC-tziJy61EFqN_NVLxpAP39WZD4NUB1gBQbX2VLbokKxvX3PcAHpHX5daCb1XF3UL7tfPdSnYA_ANpb3P9jFAKI4h5DuOAV4a94-p8UoRb8tW70p_SSV6pEdYzZEy9LwWpXXoq7SAGlBNfjK2Cmw6_SnwUOhhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=QgyuRTANHTe8stxA6NHBD-pYJqN0_W1dj-6uSTaS6nxxAD7m2zUVtgJomWOjUKK-11ffjz7Nyej_VVb-Xog-lZwb_YjrGJ9cTO0njxEzOhf5Pozm5LuF0ZOmUsYRBdEKjHGcEdvsRJLJlNT9T2eMPr3VA22151Thtw9qkvyzY22-EydxMC5EjyPIC-tziJy61EFqN_NVLxpAP39WZD4NUB1gBQbX2VLbokKxvX3PcAHpHX5daCb1XF3UL7tfPdSnYA_ANpb3P9jFAKI4h5DuOAV4a94-p8UoRb8tW70p_SSV6pEdYzZEy9LwWpXXoq7SAGlBNfjK2Cmw6_SnwUOhhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=bFmOR5YIWGph6GRyntBnw4pAOoDSjru1bvpvUANRz3s3BuIPiTBYCp2-kj-sQYIGp98vRuthXwc2LdLPtOdqIY3FJ0xIo-j21oOVsAQVPuInmI9x_32-V9_QAWFmnENmr8dUU9dHDtFlKTBX7ILKrXQt5geuonHK_fR9CHK4xPjfNA2T_3fruPfwMeIda4LHWEk2zrgN3J1zu8Lp8a-n1khcV4gyhmDLZmWiIx734SMX6eac0RPmFTooxJiqQxorLpUvU9zDcqrYA547gDX4_BLU4TTDO9JjgxSjo37Vcfwnaafn53NAmS-bHpUC-u3R2MQa1FWVoLwSksSrpKTxrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=bFmOR5YIWGph6GRyntBnw4pAOoDSjru1bvpvUANRz3s3BuIPiTBYCp2-kj-sQYIGp98vRuthXwc2LdLPtOdqIY3FJ0xIo-j21oOVsAQVPuInmI9x_32-V9_QAWFmnENmr8dUU9dHDtFlKTBX7ILKrXQt5geuonHK_fR9CHK4xPjfNA2T_3fruPfwMeIda4LHWEk2zrgN3J1zu8Lp8a-n1khcV4gyhmDLZmWiIx734SMX6eac0RPmFTooxJiqQxorLpUvU9zDcqrYA547gDX4_BLU4TTDO9JjgxSjo37Vcfwnaafn53NAmS-bHpUC-u3R2MQa1FWVoLwSksSrpKTxrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=WtbrZEZHv4fv1op9MOo5Azr94WZSXa4ay8g6BwuLVBT5RwjLe0Qn2RNGnA344FEaZVG2Iqgg5f0iNNhrXAPdbn1R0D5Jbh6D1sRIB7_IiIE-dAQJSN2esPaILHhcbV8QVtV85VU0EF0zsLwsL9n2sUZZxk93TljIgPUJVDnjiEnWfix4sZ1v_xSa3nd1ko0OwxjWkLBrz_Gpp_-3zX8gWwtDRpaFjaIOIquIc1YE55JA9AWFmp10B5xuKrRXgvec-sMLxF4E6sJUHwXgc0Ofw-cOXw3bXzNfmFEV02NDj5WHmVUQ_tZEkdt-rTqY00cJ4LBNSvNIQ35Z0tfczqtJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=WtbrZEZHv4fv1op9MOo5Azr94WZSXa4ay8g6BwuLVBT5RwjLe0Qn2RNGnA344FEaZVG2Iqgg5f0iNNhrXAPdbn1R0D5Jbh6D1sRIB7_IiIE-dAQJSN2esPaILHhcbV8QVtV85VU0EF0zsLwsL9n2sUZZxk93TljIgPUJVDnjiEnWfix4sZ1v_xSa3nd1ko0OwxjWkLBrz_Gpp_-3zX8gWwtDRpaFjaIOIquIc1YE55JA9AWFmp10B5xuKrRXgvec-sMLxF4E6sJUHwXgc0Ofw-cOXw3bXzNfmFEV02NDj5WHmVUQ_tZEkdt-rTqY00cJ4LBNSvNIQ35Z0tfczqtJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swJTy6L__4fceVrnmCRgOYnuuwEKVgJRFG4BzPc3LRJ1CZj7n9snXy2SqChMCCuf8OflLM_t_hXoO9AJsbT6tE74RZ77PvoCl0k0H7rtmCzsWZ-Xobvp3KObVmnp1ydoPxFJ5HXKzgSDggXpM0tIzMYdLFlNBe8b1tbKNDo9eZduD0EJcntBbfzZrrBusu5sAbfzThqVWPUXltm5JwhueJEc9MVOBh98ZgsoDd_Sgj2fbSSQ8706hSTD4hqPffWLeqOWcXwGeGv_Tu44ivCeBpK5W8jhL5T5oGj5KvRLvpVQse9UdBfl-Uhf0i7pXw9GTud5EVPcy_O7gdO6J398xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=EGWR8Wz_zpYenmCEG-ODa_JEMqVeTDIIey7LPq0QZPUYDA2FXn-d-pqoGGfLhryow0xdgn-hdobNqFrs39jLaCbfTJMw6ki5anrKrKqWko38G14BFlP1nEKXfWoiVgcYHYuuSrDrIdJVYjoGeTlJ3ajyn1gLCx6DiisSKvYtVUjGojprlhygMJcLflCMhPHRJGFlfeJmW3KWh0VyfkBhVoIMVj_fbKqBZq6R181HTFIMFfIjklXhDUXb7V0m4TwuWdzKWrH3VbzmHRMn9yNiatEQdPvYb0sNjFdvbk5HwGgPwuzNJ9-8lQMvTmR2T0h5faeyqgM2ZTSl7OaM9s4zZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=EGWR8Wz_zpYenmCEG-ODa_JEMqVeTDIIey7LPq0QZPUYDA2FXn-d-pqoGGfLhryow0xdgn-hdobNqFrs39jLaCbfTJMw6ki5anrKrKqWko38G14BFlP1nEKXfWoiVgcYHYuuSrDrIdJVYjoGeTlJ3ajyn1gLCx6DiisSKvYtVUjGojprlhygMJcLflCMhPHRJGFlfeJmW3KWh0VyfkBhVoIMVj_fbKqBZq6R181HTFIMFfIjklXhDUXb7V0m4TwuWdzKWrH3VbzmHRMn9yNiatEQdPvYb0sNjFdvbk5HwGgPwuzNJ9-8lQMvTmR2T0h5faeyqgM2ZTSl7OaM9s4zZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ndfDlxnpc44v2WyMzW_PYFvnlskuEM0LtMrkENodYEHU0cbhPU9E8QTH6aPQi3DwbKoNvcbMLyMjeOAAX5rZEVddsTVwdyxU06Zva0Q2X4a34CFyP3dT7v5w1UvHStpgTo-yzMS2ZJacfqcgeTaXbfY0FTMhFacVbgMPWBCylYBNZqz3aOdbM4ZZ7znQ-iBOW1z-p1cZ7f3cO4pZ9onP8d6i1DmHqvdXF_T1OTyfnqse62Xh2L4tA7zqmJYBEQiPwUd0_0TSmcCpRdldBNSbHsH0LyOvpMfFvDQO1UZYszZ7vSqRgelbFvoU4Q_JKr56Nj5NEBp7YyGJyEic2QGkFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ndfDlxnpc44v2WyMzW_PYFvnlskuEM0LtMrkENodYEHU0cbhPU9E8QTH6aPQi3DwbKoNvcbMLyMjeOAAX5rZEVddsTVwdyxU06Zva0Q2X4a34CFyP3dT7v5w1UvHStpgTo-yzMS2ZJacfqcgeTaXbfY0FTMhFacVbgMPWBCylYBNZqz3aOdbM4ZZ7znQ-iBOW1z-p1cZ7f3cO4pZ9onP8d6i1DmHqvdXF_T1OTyfnqse62Xh2L4tA7zqmJYBEQiPwUd0_0TSmcCpRdldBNSbHsH0LyOvpMfFvDQO1UZYszZ7vSqRgelbFvoU4Q_JKr56Nj5NEBp7YyGJyEic2QGkFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=DZxoQx7gIYg6Cv6y_UEpijv0r2TlzPx4-mA3c8Jv7f0bSRfRAPjBahEQdvzwSHIQdsUdP2z62ka99Y5xlwNwMml4Xurb4Yjz23nS1Db9s_44cjI-xu6RaTQ-n9_B0gvau4XQiT_8GYRFgT5mw1jKiZNKicTnskToIBvxUuITA0XSDKj7mHLNjnkDdBrRlnU1OVYw3TJsjAEeHh7tQupZmTsjKcI3wvng2fpmA3LbiLe_sjT7kuNNfwaMoSooCSsXwEiowX16ETMRctVILPiE5julHDZJxvrQArrMhMAmTCH0VMyna2GoFmIbKdNn_7vhNg7gnfWgy_dYEoJymmhRaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=DZxoQx7gIYg6Cv6y_UEpijv0r2TlzPx4-mA3c8Jv7f0bSRfRAPjBahEQdvzwSHIQdsUdP2z62ka99Y5xlwNwMml4Xurb4Yjz23nS1Db9s_44cjI-xu6RaTQ-n9_B0gvau4XQiT_8GYRFgT5mw1jKiZNKicTnskToIBvxUuITA0XSDKj7mHLNjnkDdBrRlnU1OVYw3TJsjAEeHh7tQupZmTsjKcI3wvng2fpmA3LbiLe_sjT7kuNNfwaMoSooCSsXwEiowX16ETMRctVILPiE5julHDZJxvrQArrMhMAmTCH0VMyna2GoFmIbKdNn_7vhNg7gnfWgy_dYEoJymmhRaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw_Vr_IAGTdDbD4rPZgDziDj4SbcZnvYr6nfAqj1OZX7U27tdehMqkGTPVw_CA2I9g6kH5cZQ6OAL4n8rEAJRsMVMjL4F5J1nT3yzKEn-XaoMYapfekT3NB1sVdOkf4StR4tPyiiKMW8R1DWmNyVYgaNI14qChgc9OplIBREkbGvg5GTB7SumYwWhPmX7oGJp48h6LGvctcLFWrM4RKNNmHT0xTHVnT9MvbhD9xTmcf0gwnZ86YxAEwVLVt0h2bNU4O_ZR5bEey-ncn9ZMBPkARWcFvFm4ntkmt-mWHheAKt036mBrn_ggHveNWBzYxvC11V-hznc1wMEWRH_pl1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=btg6RIkx4Zaz-YZ6CPgt4Pvm3X2UTlcxacc1Y_XLIRsKGZhXMpswMAF2BU40_z-n16e_KRWM4IhtIcfaCrahe6Iu6OH8CscWYX5AVU0__-fKHo0U0y2EZuaGYxZbRezWlrcBTF0lm6soHg2C24klJePn3rK1WdePZqkC2SB4b2tfPVXE_Fl_tRLXLgpq2qsOShvm7ugsW94kbzo42bCHhknwuk3I5QFXV7eeYJtA9QXhEOkepERzTcOpAhrKDJ2ZO-N_7ymFB7IM5CpnTjjWHbKA4_VhTKfxGc22lqyrNZGxdJCGzjKca-nIuwYU0Lav1inkU3YehZERQIgmR1GvMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=btg6RIkx4Zaz-YZ6CPgt4Pvm3X2UTlcxacc1Y_XLIRsKGZhXMpswMAF2BU40_z-n16e_KRWM4IhtIcfaCrahe6Iu6OH8CscWYX5AVU0__-fKHo0U0y2EZuaGYxZbRezWlrcBTF0lm6soHg2C24klJePn3rK1WdePZqkC2SB4b2tfPVXE_Fl_tRLXLgpq2qsOShvm7ugsW94kbzo42bCHhknwuk3I5QFXV7eeYJtA9QXhEOkepERzTcOpAhrKDJ2ZO-N_7ymFB7IM5CpnTjjWHbKA4_VhTKfxGc22lqyrNZGxdJCGzjKca-nIuwYU0Lav1inkU3YehZERQIgmR1GvMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnJi3gS0DvNDKRYTYe1wHIDJxrGM-T-lgJxJqdhGBqo9aoWi0N8cDf79_JFKhitV8PXsEscHBt9rRXjouOg1nyXoRtSe0TEJZ_m0QA5_c9wf-hqFr28jwT59QvMVwR90tkw_jPwaaAx3lkb2XTLRNTz929wpdPWQqnlRKk9BiH6gy4lshG9vuLtQVk7ga0GfQhAwUK469OduYJzYge2TREkdfDgm-b2-3xZEixHqLcn2vZCOJZecPIhK1CzfFK-rHUat5cAZnfNJPtm0R92VD-GsV4qqQJ2StC1cAfuRCXMQU3cqo_cGDroJQnK_Xe8XEyMK1zw2Jf9q8tH0X1sy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=CkFZX36LD5femyVe06PPEcAYKuSBgkQUwBI-1sdv13zVdgKDATTqZXqa9RsZ1u56LWV3TdLkLAg5YXbDXnmj145ZImukxvLmYUL5txiXTgkSFot359pyZa-ZrX5ECVlhTNSuJPEdT6LYBKVD1miwqFLGgD9xz_6fRjUUXEKdNqvRCmVYcrVOg35nGmZCY3YGHAK9YCrJG4hJOOmXrJsxnFWPjdYCZwT1XiPnOo_FWy1jIZxZenAbQ0V1XPQ5RQxxn3Mlh4AkHTr8lbLLDcqQFQS0rd5BGJxQXQ8hl73YzO_q4UuPQ3f2d8rcnhYg60pcNILEi0osi7zU2TSDQzC9_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=CkFZX36LD5femyVe06PPEcAYKuSBgkQUwBI-1sdv13zVdgKDATTqZXqa9RsZ1u56LWV3TdLkLAg5YXbDXnmj145ZImukxvLmYUL5txiXTgkSFot359pyZa-ZrX5ECVlhTNSuJPEdT6LYBKVD1miwqFLGgD9xz_6fRjUUXEKdNqvRCmVYcrVOg35nGmZCY3YGHAK9YCrJG4hJOOmXrJsxnFWPjdYCZwT1XiPnOo_FWy1jIZxZenAbQ0V1XPQ5RQxxn3Mlh4AkHTr8lbLLDcqQFQS0rd5BGJxQXQ8hl73YzO_q4UuPQ3f2d8rcnhYg60pcNILEi0osi7zU2TSDQzC9_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSWd_Jr5vi_tQhOhroLmyWBCtBneQrQsXfyIg51a9W76k2m0y5OPTDpCKL3ue6MWuzalWaKQNaTzTslI9AuAWI92uDn1MFzZHxee6LXqvok4CePc-GZkcVE5K8nrCCXwMIRSZclkCfInKJNv5HiDvaEv2OOPdUOKfpLhifGMAI8Gi22OQqgV7D3BfLS501TDFKgN5ZACbwo-nSbp8BDERSmAISGLuh7zikQfdfsLsJII0WRULdZihN3GyIyyNjqcuTf3QMes5hUPyp9v1ow7yw3w1UX1fGZavRHiWMm13oAFNiEQYeOV8ebQ2e5XkGGJGxbIFNgKPqOGKkAXvQOiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=md2qKbE6mY5GI4pWs0c09usIE3PB0cDSgvgDv1uS81xOzu4rsgT_aAWekwAUcNIBDUPhtA5IovNBsnANpecm0AbDUQGdU-fEfUfRMAp6sfgR-vIhNJJvdMD2o9V8qXVG3v1P4JsW30korfupMra2NJwIyPw0odYNZf5pRsPMif_bZvx2XQPKyzbbSVX2m4BOrfrgfmX0WOGKNUtyakHDP8--1vPDL3eH9j19mMRNhdob6vJ4VWKGLTJNq0nICqJAVc8VXHs00tiJR5bjVMEn0LiA5acDtyNGcOdDaNaV9t9z4Z3-sx7Xulg7ldWio9gczUmM5aVqJunlK-iaH4iOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=md2qKbE6mY5GI4pWs0c09usIE3PB0cDSgvgDv1uS81xOzu4rsgT_aAWekwAUcNIBDUPhtA5IovNBsnANpecm0AbDUQGdU-fEfUfRMAp6sfgR-vIhNJJvdMD2o9V8qXVG3v1P4JsW30korfupMra2NJwIyPw0odYNZf5pRsPMif_bZvx2XQPKyzbbSVX2m4BOrfrgfmX0WOGKNUtyakHDP8--1vPDL3eH9j19mMRNhdob6vJ4VWKGLTJNq0nICqJAVc8VXHs00tiJR5bjVMEn0LiA5acDtyNGcOdDaNaV9t9z4Z3-sx7Xulg7ldWio9gczUmM5aVqJunlK-iaH4iOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEbSl4zJTTILCLDWkgl0x17DRnGw2MmOW7tRAmokrj5txP9xbwFbn3-W7gxQjbxvp5byCCsxIDI7bmXAjOMFsMV9CxyJJL8XZY48YF1vU2ZDFpYPebaDqrz6ZpIjXyTaU5_CjCLC-IqImz0vNt6SRJbzPDcEp1PQztTkZA82ZObVOw4nk3NRRiL3ctMZDz01ApA72VbeHLJpR-TyMYnRbLdjfZyygyJD57gtYb2TaEiKgo_UOsZdIBx2mekCP7ZXI6ZnCk0BpHtUGiWremfiMpujszRjqOVnQYw7pSefDWwyShzM5yKSAI2zuMbbC8tdM8x13LKqqKKUHzsayU9SQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSwpIF7AygX94scDacFgT82wLiMxuSh4TyYsC_XXr2Boyjypk3JqUEqeBF51EAdAM_D78zoEb2vZfwYzVtP_YLO1HhCec8F9Q-zbDlJnBnf6NzvqWLdn_BGgtxzMPyv6puF2nGsYLCIlPSH7ihCBMU9xIQIYHw56X8MGVP6sZJIwW_pi3UIBGhGAC-1-degjk1LrY3vHuQvC4ky6llnKhgMALLpoI_ruvUMghD05eITchpRH8OOgrGkqVcaWJcTyByhPwWO_jhFGqJxFYrNBWWu0rZHDqJboeUICI6dMa4xC1gLhouDRFY3WDBPbdEkfXZ2IVxJYJCX8Q6oi-Ak43w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=ZdPREB3I3v1U6Ah5ec4coz5XuYbp-3O-GivZHME1E6E9XBFTO9u98xZ9eA-QRHzp0mepaQ5-5F_c4G-kFIhOP1Y96LsTjkcVUlp6LdTHmhQbKCd5RE-OeAzMudcH6QRE-VVX0NF5JGbq4jMNNAfCQVYWPIDtu9kyawXD7yzhJDNDehUwFyLqjXuLVpQMoj-LzaiVk7_JaIBPKQQJVwRRdQTp3QqOZ6YqH4SlGRkWIeV2vCF94xxEAfRfecyu3Uq4N-pynfdHsQXv2pGqry6H2ixQaDgiLQackU76-zo8PJms2OrId93Q_4Z0fi8cVCT7fnpo2nVwUe_qyAu1XYu2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=ZdPREB3I3v1U6Ah5ec4coz5XuYbp-3O-GivZHME1E6E9XBFTO9u98xZ9eA-QRHzp0mepaQ5-5F_c4G-kFIhOP1Y96LsTjkcVUlp6LdTHmhQbKCd5RE-OeAzMudcH6QRE-VVX0NF5JGbq4jMNNAfCQVYWPIDtu9kyawXD7yzhJDNDehUwFyLqjXuLVpQMoj-LzaiVk7_JaIBPKQQJVwRRdQTp3QqOZ6YqH4SlGRkWIeV2vCF94xxEAfRfecyu3Uq4N-pynfdHsQXv2pGqry6H2ixQaDgiLQackU76-zo8PJms2OrId93Q_4Z0fi8cVCT7fnpo2nVwUe_qyAu1XYu2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuMrkXtKH4IQ8JWN1d9dpZuGMGqTLFVXfMx4C1uhJQmYP7syyxBz9BUcNcht_wR2fRKq3kCbLw9SYnnW5vP6P0-u3wAWNUO5tg3k-JUL27EAfb1mqsNzSVNm0cd6ofGe5derBmTOtk0Wprw2vSc_sE1L5kPAs-AO6yG5Rdy6ZiV-nhKIE91t8f5unwc5dwJvMnyZAxJS9caisqdTnSYcpbDgJLsSKKwaIhOcYP0rN9Rw4c-8gcqwfr4OWbIiqPWaA4AUF55CJNPAX20d2mLjbvc-JAyVoWJWVCi_nY1VqQyonCWkT0nwWTT2CWLHhe19MaCoJiaTfGlgH5BTLtfLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4Igrnm32FB0hNI2E24sKPT-rZh0eMseUZTa5dlcEUC9B2o7IP0gjA6syYFVBCRZpZqXnbDnxEsYBjgoBmywVlRxsMMJuoqN_c190cYU3j3Se0wRwY6AWq2f2x20YwfvtDJf3z89CzdOjXfKug6VlBuBM6bsPm1wUyHqBWBJz_11dRVT1DeFU0hSR3XKbmTd95hpj5a3s5iqWdHyhrvI9hAKcReFl6CJpfTBRx0vI5ZQ6iEbXFMORJnVeGa1O1MxcXNQ9ww0_3vnrrGw2T6xkzMdYK2_Ux2-tif1vlajyyjB2kEEYFKnmHt3FqwSsMuAW3_XxTdNRkEtFySLdO3WyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBCRxjFKFE2eVbLVqb0EN9Wbvod6dcr_VwAb1rXGNaw05ErCnz8dJpJXpMVbAzcLHlNEqXbpFbVy0DhEGw7VXZ6swXdH6FLzwa5em0YDTIS5FwT1wsf1NCotwy_At1kFOX1egUlTgk9ZhbjY_7XCfPV-GJLRraLaam3m5UoHkTmxkGmwykSzvDYJCCknHsHfBm5syN9kX-wD7inncutsfm3TcmTaIVEqcfjSSGWhjQ6ubqGpUEumkwZJIz6HVoEnQeExEHUZYLguX_XPvO_KTp0FMox2ed7lMY4Jx-r1P1AtuwYw7tu9ZQiSAPoEF51Joj5odiItjpjNQZVc5d8XRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnrQ01whK2E48kc1W-aGDvyTNw1BQIygFsHlzowt54V63P9xDQuQBmoCCZNEe75y7Bi1Uw-VWLj1NCFHjMXwDyMp_M9KpQTUetQ-l3VCSJrV-h6JOX0AmYDJFUWRMT2aPMuv95bmOHDkg-SUNRcauVuaF7nGLbvWYIbCjHwjC-9f1lc2XpNgTr4qkwec5ujf9nzts3kilvA7iQbc5HoyYPdG4nqnlj5cDMhA4cAz8YnjtcmRS4DQb8Xmt0zZ-mJC88ZDJH0ZNMWlRECt28VMd3hlUvqR52D4VjoViaFZcfdctdooYrua_5pKfoEtUhdd7aUJTcncp1rPKvMBxdOIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAJoPwiKfYnDoxQqOc6Ug8Xp7DExeIfF2bmJw6tVbrU4TcAZiGVLfq_9iobtNBX5qcUquwLFTxYeWd45OYXMLvjPvi5t8nwCwEwsi3YHhDmHSvGMIN9LQRMkh7ys96hTrqec4Fp7gpedbR6gRUTAgnNRLnaSGfqHi9gNroNUFsMh8l8u25buGL3q_NrhgLn4642QaoxcV4FSluftw4o76aO5pSnVNBavgE2Ld6qBNg5_AhHOqQLXnIi88ytYyB8FICtg7vf5NjMwBTn87rQPe0PeLAHYweh8ab6F6fUEX5p9gHo8C_v5a29RVeDco1K_h5v4qdsLvp19eA3cMRG0qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=PySmeLEFwrtdIPBVqsOz-8xXzTc42-v-84P_jbrDd_yzYo43Nft6a93SK73THQZzFock451qS19K6WFHnL3Ny7olvtkVRnLIvpNb_Rz2l0nfv5-kCMtNNagDEDwKzgji05oO2h0Px92nkUVOmgiMUgY99ZatkbPVXvBLJ_5VJ5aszGuZ3x9M4sOMWM_JrNTbWl2tYmLbKxFC3GA6m8EFNYbomeViLRl2v3bdH9YKZhIrEwEjB1RFWLDCQMegZQQNLOGnkwLdQDq84_SmtDSEMynYaZcXXd3FDk5D2knv_T-tBmB8Dlfu1QRU0Vr7b6q20NM2h3nLX0ReOQWI7Xbs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=PySmeLEFwrtdIPBVqsOz-8xXzTc42-v-84P_jbrDd_yzYo43Nft6a93SK73THQZzFock451qS19K6WFHnL3Ny7olvtkVRnLIvpNb_Rz2l0nfv5-kCMtNNagDEDwKzgji05oO2h0Px92nkUVOmgiMUgY99ZatkbPVXvBLJ_5VJ5aszGuZ3x9M4sOMWM_JrNTbWl2tYmLbKxFC3GA6m8EFNYbomeViLRl2v3bdH9YKZhIrEwEjB1RFWLDCQMegZQQNLOGnkwLdQDq84_SmtDSEMynYaZcXXd3FDk5D2knv_T-tBmB8Dlfu1QRU0Vr7b6q20NM2h3nLX0ReOQWI7Xbs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=cMcBWLYg0z5AzRqmsB1KWLuWD6tgFhuWKDjIsfGPwz8UDAr9MRRbGjuyhApZZHc0Stl_ya09TZJKAs2mmG6pWtunXjs_S0uyyrEZtGxYniZ679nm8a2GRfPcYAPBWT6dAZ98_evBYJ4yIIunE0L1POApphzXCU3cSkZIhR8tWr5mQgBPSWCQvBTmizwjyAKLpPy6l_r-yFFyz2nT3yUsJRvOoLYiCbM5dUe05pUJR-pTp8wfUKg2v8U-cNG1VTUyMwdTIzHaa-40b1PWM6-2Aan2fsL61URidPOr1dmDLuFrzG8dogV0XhACORGDf4IVFnRyiTFo0hlUoIIpZjYENA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=cMcBWLYg0z5AzRqmsB1KWLuWD6tgFhuWKDjIsfGPwz8UDAr9MRRbGjuyhApZZHc0Stl_ya09TZJKAs2mmG6pWtunXjs_S0uyyrEZtGxYniZ679nm8a2GRfPcYAPBWT6dAZ98_evBYJ4yIIunE0L1POApphzXCU3cSkZIhR8tWr5mQgBPSWCQvBTmizwjyAKLpPy6l_r-yFFyz2nT3yUsJRvOoLYiCbM5dUe05pUJR-pTp8wfUKg2v8U-cNG1VTUyMwdTIzHaa-40b1PWM6-2Aan2fsL61URidPOr1dmDLuFrzG8dogV0XhACORGDf4IVFnRyiTFo0hlUoIIpZjYENA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=L5XVx8FkQyQRf09ioAJuWofj2oFs4KHQ1KADovfVyQQgy90Paxze1xirLOyePKmV9mNV8eURfavkmDWoPccaeWjMhK5umH7s1-o7kId_tskO4hiIuFSsL68EAuOrJINmrGRztNS7ZzViKLgk--NzZF7eW6xTV-ord11h55JG0a7sdR4xo1Db-933hQjto1Y4nHyXFAv5TPrynEQRxvhSp8DNx5izu_iyMCNgm394YVz616p0VlJWZvrdOo9lXvO35QmEo7vWhmE9-n1derwvHRQoPWzJcguUul3jOfxAoUB-CWIQeD9Hd1rAknpwPorj516HEer1iarpooWI7fTCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=L5XVx8FkQyQRf09ioAJuWofj2oFs4KHQ1KADovfVyQQgy90Paxze1xirLOyePKmV9mNV8eURfavkmDWoPccaeWjMhK5umH7s1-o7kId_tskO4hiIuFSsL68EAuOrJINmrGRztNS7ZzViKLgk--NzZF7eW6xTV-ord11h55JG0a7sdR4xo1Db-933hQjto1Y4nHyXFAv5TPrynEQRxvhSp8DNx5izu_iyMCNgm394YVz616p0VlJWZvrdOo9lXvO35QmEo7vWhmE9-n1derwvHRQoPWzJcguUul3jOfxAoUB-CWIQeD9Hd1rAknpwPorj516HEer1iarpooWI7fTCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=pBpzHi9duQonFAH6FaarSTXO7T7hBmEJVPP_ZGeyaYQOQVDvscamd2cO9NqbeHjDMh3hucnFKQ8BHwke-fuZJBXVOZHjhMgm1O0A4_EkfioM4fN7Y9WY55Ox1whbMfqnyMVpYXTe_TTWEh04JIH1d_qZSw5OEHORuw3WGb6N8bW-NtiweCvULMx46l5349GBtBkb2iF6yksy9JFFwtHIPFSbtCUyxbi_ffpKHMlEd4xyhOKKqZjqVuxVSE5WKX6AJoplzPzI2dIjtmQY27BYdO4uP_6zef73iGBNkX5SHhJfSTV7iPyrfFuYGyUiYnyN1WNcCviSj-il2NpU-u-FVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=pBpzHi9duQonFAH6FaarSTXO7T7hBmEJVPP_ZGeyaYQOQVDvscamd2cO9NqbeHjDMh3hucnFKQ8BHwke-fuZJBXVOZHjhMgm1O0A4_EkfioM4fN7Y9WY55Ox1whbMfqnyMVpYXTe_TTWEh04JIH1d_qZSw5OEHORuw3WGb6N8bW-NtiweCvULMx46l5349GBtBkb2iF6yksy9JFFwtHIPFSbtCUyxbi_ffpKHMlEd4xyhOKKqZjqVuxVSE5WKX6AJoplzPzI2dIjtmQY27BYdO4uP_6zef73iGBNkX5SHhJfSTV7iPyrfFuYGyUiYnyN1WNcCviSj-il2NpU-u-FVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6Hd3lPHVK31dP-Ig0T9Hr9bEO_rQZpNaHsAw-q_YxFBXUpj3abvBiRjzGokojaO5BxmWqrf5W9cAcOz7ow8LRjqYWQzgmTTvP_KAdouNxvBYvii33g6KwE5HdK4FSwgg--BoHJB4O2Qg-0TgOni9YA_nxURCW0_GXq_U4f2B6CMk4SeRbaSjomxZR8RoHp7kj4zOwncU-puH9vlNyOF0x9Kj2eBcnUm7ex9jVloxGhRkoPspBiRI0CWqWmshTrDAcFKIXCg9w4_Et7Up93EUnPOAGEhNsVRBfAmjfNdYynbrAAUhedxz4wttfe_DyvracSrkk6z78D2sLMOnVaeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obBE3Y1jfr5MGdUZOIUlgV5xQuLMax4SVr_UrNQvF7WF-SmLVGzBFmBYvPEPGrGK2i6HU1g_564z6dOOmX8Y9Bw3RC1acp5DJLuxWpisiWze1eGpioNpXB7--lplYbImn84t2V1v940ZLiRdFEe6hpkMrEX0dlNoGzSvR4NhEIiGKna7gFMNgXH9iURPiZB7f8X0cdkFujfmWdM_NlrDm0XLpfodDy2NIEjGQrAY9M-I08S0R0E8v7rEc958Isrw7GzmPPp-ra8gnYBJVkv4l0L_fi-4BHQWxs9on-dPmqCy9UdTsqjkpwotutmQ4pbh66-VEBJCzAkd-l0v9PD7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=dZICttaxO97CHQyPj4Z7tTLIZ8_5vt_QnnU_80YgycyQo3HYCYFcH1-fUd9A_8wRyrro9nuWPIG5QPEgDQhHQ9DHcbqEw5Ank0Q-EPtI5JTOJWj-kdGeWVH4nZxeVuv2xPyi36m11foZgIF81s32yKUJnqHsc2TIc6627f9HAYIpIWVA25aT_uoQ_CuqtJhc2rpEI3exwFEdZHVnCuKe5re2BkeH3DXHlBq8VDDOkTrb_FIPjQkwqOse4hzLpjOmlTVrvd8IjH09ZDzfQ3KRjFl-yq997T8yQk32ag7QWjMhH-e2aLY5hgH2IdpYTZenaZMhnxyaQRaanLIv7lh1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=dZICttaxO97CHQyPj4Z7tTLIZ8_5vt_QnnU_80YgycyQo3HYCYFcH1-fUd9A_8wRyrro9nuWPIG5QPEgDQhHQ9DHcbqEw5Ank0Q-EPtI5JTOJWj-kdGeWVH4nZxeVuv2xPyi36m11foZgIF81s32yKUJnqHsc2TIc6627f9HAYIpIWVA25aT_uoQ_CuqtJhc2rpEI3exwFEdZHVnCuKe5re2BkeH3DXHlBq8VDDOkTrb_FIPjQkwqOse4hzLpjOmlTVrvd8IjH09ZDzfQ3KRjFl-yq997T8yQk32ag7QWjMhH-e2aLY5hgH2IdpYTZenaZMhnxyaQRaanLIv7lh1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ-WyVm835fyEgSyX9wuepHZaGJf7XFReP_0CIned2dNEUYDA37-DKT2DHVFCDv8CBqd1RrHQhvT9q0qDaF1yh36rDAbv1wm4oQZOQR-G06W-NkCzvRXmH_ToQHyKfRNuLfCCN2ZrrCTwPQ6kXi4gZHY8Usoln4LGjp_4jWSybLI515D5Lfyej7WMaxOqF8w1itpgCXECzlYBpFhsNEXW1sxHrn8bDpLO3dsM54kT8cZ2ShqobWIUtUTVXNoJNXA-EfcrbZunUM6TbZ7CLUxHZFNxdAtSXpPxNsYZvNGrT4ZY4Ww0zidAYAW84AwObxaQIRa53o88quSV3TdJPKbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=khsZtMoBlxb9jnhyljlzJfu0550JaBm9flQ0sBqfIwwSSLoAqorlIcvZJmgwEK_A-XQT-feD7yQ1W0HJOZRRNvo3HiwM3re8mO2FzD-aP2pBAN-9fLQnSWKgtaHFuYcUXbCsvhb3_iC5KaXxcPiUKeiUPBB7-qRHMXZSak-qVQc0gwow2K9qM42hIUAF-Vrk_wvq_uMeRtN26xuWo55a-pboN3W5Uvc79SdhoGgNkUzaVUOoHK4g15PyLYIQmhYSAYW7sbUGAcOTMZq_q4OEsuUkSrxGVKryOuxvN7YjXzSACcL0ShLqfy0-i9T78pguA7-fF8rOyOUUijcGK8J7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=khsZtMoBlxb9jnhyljlzJfu0550JaBm9flQ0sBqfIwwSSLoAqorlIcvZJmgwEK_A-XQT-feD7yQ1W0HJOZRRNvo3HiwM3re8mO2FzD-aP2pBAN-9fLQnSWKgtaHFuYcUXbCsvhb3_iC5KaXxcPiUKeiUPBB7-qRHMXZSak-qVQc0gwow2K9qM42hIUAF-Vrk_wvq_uMeRtN26xuWo55a-pboN3W5Uvc79SdhoGgNkUzaVUOoHK4g15PyLYIQmhYSAYW7sbUGAcOTMZq_q4OEsuUkSrxGVKryOuxvN7YjXzSACcL0ShLqfy0-i9T78pguA7-fF8rOyOUUijcGK8J7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdmu-00rEvti4lY8eDJ8vB8KUCnAKcFvMwqB7fTtquQMfVI0Y25ogMjJ1AmHVmTzorJF_-BAKRc8nqKcJ-LhyTcozyJ7wsysqplqpaMeJNe0O-QKlDJm_CvXb3TBJFJfO2AzHi57cq_a3UQJXp6svCAIuns5M9XEWg080iYzA5Bj0h4XHGARxYIk3u28P4J9JJXHC0GWsdLvZitYTmu2ghsv7E_fAo5z4wOJdBc9JZs6lhmZVG5GKqgWoWpA1lGKDrDXdRRu3jL6WONNS4bnBFaFL0g7BJx8dP9ox08APpMF8KKIBocKY9CTsiSy2ZTVzefoud3L2yEVZYwMrLkPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3y6Wu6SEjePi4uADKHbNRKP0MofqwqULCpE0XQmqIR78TT5iljYrbQp2OWL93PrqypJdiVUcjSBObzUd38sAPRYq7NMCcbfp5azWEEI9vFkP_ZfWHlIeKp47q9bRUCQ6rCgs3XO9V025cFOSKGZUFJkz9Ekqo4f_OxIaBmyAiwEX3KkvwCZs7oR6lI0Ke-njxg-7bMqfRB9ZZfrS301NPAztMlbPcdawuDyeJOB8n_Tm0h4A9gsinVHxJ9Exa_5be8WpOXmjBJJIeQn6EaQU2OyURAEG2B5eAYtAW9ZPah3aXsPo64JG2FMwd3zynKcbowuB0S42hKWMdTDnr7Xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=li-sVfi2ILzPjgKVikMVKB59VX7WbU3sve9mZcWmqZLr3pREhGNnj2d7ZFisCF8VtCJ0qDog4usew5YRBYxu1v_vp9PrPWJaPQrW-KwTfPfZHatXGPZWx4X2VdVW_cpOtJEViYkFTzdggWRyptwmExyMB0OrqUsoP22Fku8xKQMx_nSBKgLOIUn8mMPm-o4xCFfr0LkUIT4JFna9ugM6TQWfoyGtUhgxhZDNNviwsw9LrYtLQz0tUP3DN6sko1s3q7Um96S8VP38vpvNZyjzF2VfShnvt9gizBBYZ4XxtzFw_zeD7CjBZu6WFGD_oqCJUTRvP-_j11A4q8HVpbCbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=li-sVfi2ILzPjgKVikMVKB59VX7WbU3sve9mZcWmqZLr3pREhGNnj2d7ZFisCF8VtCJ0qDog4usew5YRBYxu1v_vp9PrPWJaPQrW-KwTfPfZHatXGPZWx4X2VdVW_cpOtJEViYkFTzdggWRyptwmExyMB0OrqUsoP22Fku8xKQMx_nSBKgLOIUn8mMPm-o4xCFfr0LkUIT4JFna9ugM6TQWfoyGtUhgxhZDNNviwsw9LrYtLQz0tUP3DN6sko1s3q7Um96S8VP38vpvNZyjzF2VfShnvt9gizBBYZ4XxtzFw_zeD7CjBZu6WFGD_oqCJUTRvP-_j11A4q8HVpbCbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=kiwT7RM1sf_mWdbs2LIn0d90LXDMR4YESHh-BAexMw4anGvfXSFBwpquiKl_JAdeGwuyhm-MCEnSdRcU9MP9gNmOWcjvMJKm_Uwmuyy3enqx83uEtTA854fyn_JFChiC7YZO6Ijba0C19MHSgMEqJUTEdjQaBDROR-L_cXsmLf_rfUu49u2H27boeU6pRMJ3lxMb2zOvLQOOBf34W7z-IfODCDotAK7FRMOiFe8M7AknK64V_Zb6UdsxuByjWPZzN2DoDXBNCxto7o9WQpgysmlFmVwqSpP3W8cK4vGm4QQd-SKHR9VxpA4ASIhqXv-3M5APl-hmRBvA3RtEZkDFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=kiwT7RM1sf_mWdbs2LIn0d90LXDMR4YESHh-BAexMw4anGvfXSFBwpquiKl_JAdeGwuyhm-MCEnSdRcU9MP9gNmOWcjvMJKm_Uwmuyy3enqx83uEtTA854fyn_JFChiC7YZO6Ijba0C19MHSgMEqJUTEdjQaBDROR-L_cXsmLf_rfUu49u2H27boeU6pRMJ3lxMb2zOvLQOOBf34W7z-IfODCDotAK7FRMOiFe8M7AknK64V_Zb6UdsxuByjWPZzN2DoDXBNCxto7o9WQpgysmlFmVwqSpP3W8cK4vGm4QQd-SKHR9VxpA4ASIhqXv-3M5APl-hmRBvA3RtEZkDFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpT006GitVBFvztjZP2srMXjziguH2MKSc2XC-Evzwhy0_pbfRPonQGbLEy_Yalz_tmLOLU7edb16z7WxRe5w8QRSYXqrOJoi9QVPtR69945MVVXX1OamKtrljA21mj_dwwtv9orcRmaYXAXOAUqODb_xyaIXeR3sAgouxUsCg8OCyAKDFNBxqbW8me1zpQkeeGpmNpPKzRVN7jFIu5EeDNLFA40g3pRFjrWsK9KtWYeVOMun7ec2LN9Iew5om-5Hm2Ge0nk3bBRzmRiuyLfKOgeOSI6nf1KoaMIrJsfFh8HtxYjOABA-wKfh4bLLZOC5pwAMxRwjpjapJkcHqXWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf-4W0IpSbkuhQoEtRbFKaNeS9_8AYzkK237Lr2MZdk1E-S1x_K7mmFHLZ-TjQJ73y1fEnDlWAcW7UBg8m4aJzRQzeu1ArmT3ah3j8Bg2WhfFiTx4nOeXNY7crzsuO63akzvOs7o7N91G6FtVsnzUqmf3mn3o6AG3x98UzswXdMPm-8lH-rN81jt7jj14vwqjo_yNNfQoDKZtjlFvPleC8-zmLKI27mLNUoPXhxYlGDWgQiIq0uC4OErXdcYBrHtidoMlIMewFjBC5gA33Dd0C2IjTxAiwaejUqeChdG6kahDwYpdIeBCmihG1RbuURgYkYzQOc877wmBzuDCw0UuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0d2dqbxjRKg8HX_zotXr8yz2hSrzOU-4n0ynTDGzKMv9esOMlFNAyMcp-zgP2PrcL-0qh0Qy9CrzzCZT1tK4QlPdUpmtOw-F9kS63_Lg5CYHxJu3ljZfh3mjQVfUCpf5zC0WQlgzlGekILRNSEN36P4qWNy0-TQHRfG_SjzT-jz4OM9wuOMfz-kbaDv6TM2vwjoeDJo6_P4wa88gE28_l4p5CbtXUTzW3fFoK4YJWnxkztA99hWhQpBJaWTgaMjbCaai6yQeWKuz747J4OHQd4hIuqkyen3qP8R9SmTVfOa7dsPjEojy9gojdjVwr3by86gZ7o6jX96RFUngvn0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=SELkVTwjLpwoPeRdZ3ytuSG7DONfRqBm5iJxJNqqcRcjsh7TlV2jaztn5BZhGAWB9EC2c_yW6FkxFfUZK1sjM3dhfqhf_Fc3tN014tzKGESQXdbj5XlKezwIFN91tzRARaQ9WRt1IUb4fsqNjdPY3Sy8vXM8jUGMiRXFTGugRNAEXjlYmxFyYl1MOx33t0cIp_eVqPgZ94OZ4Ze80tr5ENqXWbvoSMD_Jz5aqjt_qYtGY-6gDD5OmdT_x-x2BEdNI3X-mZicpZR3kRMVyHS0-u9ShHguo8HyPCn4uq0GDquuPcbxaP2t8MBj6XKvqm0OnLx3v8BXTikc5H7dwaZVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=SELkVTwjLpwoPeRdZ3ytuSG7DONfRqBm5iJxJNqqcRcjsh7TlV2jaztn5BZhGAWB9EC2c_yW6FkxFfUZK1sjM3dhfqhf_Fc3tN014tzKGESQXdbj5XlKezwIFN91tzRARaQ9WRt1IUb4fsqNjdPY3Sy8vXM8jUGMiRXFTGugRNAEXjlYmxFyYl1MOx33t0cIp_eVqPgZ94OZ4Ze80tr5ENqXWbvoSMD_Jz5aqjt_qYtGY-6gDD5OmdT_x-x2BEdNI3X-mZicpZR3kRMVyHS0-u9ShHguo8HyPCn4uq0GDquuPcbxaP2t8MBj6XKvqm0OnLx3v8BXTikc5H7dwaZVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PudQf8fCj1ZVMJtfP-sfB3oHkbHxPOZNesk3nG_Q4PUqh8dmwBiyM2kUzO2BE-oSnEf7oUC_mOGPO1eMDEdahiSW6tSGSGxrE21dBHCq91VFW7lGXfALTitbWWeq3aD90PUta3gxFZJTJVSHeV0_DnzpVDPFVHv94T9t6vtmw_Y4g2_KCXxxCYRFS3xVtH9ZDmirGBeTsMrrjRHFf1cMY0d5zknpXA6sAu5CDCF9TaAI86vxB7v_8GMHw1ew0yFprHydcr3LGSgbJDo-sBABVvpS6mw6x-W1MjGiupI3w93Uxrqwjbsvgpsllg9LHNwdsdUisltYGyDlgUpmNnGwYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n19BctbDxst1BD7Egl6_7pc3VUwoNwYMwybZPD2YVDGA67r0PrpqZLtiM1N3z9iICEbvKC3pv0bvyyvEkzxxpNe893lpKgSiht7Y2k0jWZVyfLRUaXvI_e_RB3LOnIH-uGJS31Bs2cev_ejApBFgIZRe0xRmvGPRd1cJr6p0UZtaiY8-2eKLyKHC53v-3ImOQSxvqQsPH175aSwV66rqol1jUujWy_Da-4JlioOLVAT-nUKefu2Jum9LFOP4qRNk3r-Goofe23AhbU180g2QSSB9CDROUwTnRADZSbJmjIWBToSjg9WJXwe4rEdGufEveScvBiy6RlohyBUMVnyKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s21lmsTkdVKlhY0MFi7xw-f6MLI-RLhdTmF1jGZgWpgIWxB-NBk6zdnuSOXsl-qiXVm7O_hXOGfS2HsPNtrdx9rmgbFF-h5tG1BvwxGW6SQxFv80LbOVkm5YWjC1-buV4U8FXWfMQ6WCgV_x8b6T2lhlNFpGzZKuDV2oxgRQayCldQEpQUDmjClL19y7zj0IgG50qPllicpHOFhPcwyq41T802ve4_4Gz7svxU1RcVFac5cXGXgmEkNFHGaUJOBtdN3p1czDmnH_8HpTlc0089AHznX0-kWFy9ReRIXkTFPsZn4txse-HYKgW2Y4xL5fsYrBu_ibMX83AGbm6U659g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNjSClzmg5TY_Ak8QWycO8A6tjqKK4crOmGvmyKo0MQI0vpZVe7itNpZrmYOpNYyFnUBvXpmlOoPcJp9vm8M60o-DvP6Z2zFpnHuUt8EpTYtmfUQiagjTqTLd_4RKacTlaCW55FdRFJYHDYX_DUu8An9tREF3wvGpsWIA4ffrquZJCAj6_-mXyFGQ1S5KstecJ43AK0qJEyHkjwDY92LWO_F6CrOsXcx05CrNQHxechHxIc4O24_s9p8upZE96A-qMUtpUVi5Xi6h5PFcRTt1rjxJNjpxJbi2vx1rEzV_4vu70k8xbPpXaBVjp_C4nbCv22gSwYcw-WzcRIqfAxLjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XBAtH_zwXqmRv1D1XjyeQ2o9K0_C8bWzP1qr8Ucap4nrkg9KPB1bOGvyXMdBNWDpOvecfHOAywkOGRn5UbC1xtXyXOc7MoQUujj07fBto-JHYHdOIDEPSOhUfhT7qax-MPSqucxnBUBiQ2m4iP3QL8WyoWRP5FHMXEmdso-1DhX1XJeCqZslIpJcbXd_p0zoiPsWIs13oR_irnE8sk_HA-jg2IKt9m1hbgFsv1sx7WVn_xlLI-9jVsUgfLV5iGAgBs5FNgPK5MTz7xyX6v7PJMsrbh0B6R1NlNryiS3_JUakB9wzYO6Aywtxlf5zWc1dGEY8UfvpVMcRUnDewvwxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XBAtH_zwXqmRv1D1XjyeQ2o9K0_C8bWzP1qr8Ucap4nrkg9KPB1bOGvyXMdBNWDpOvecfHOAywkOGRn5UbC1xtXyXOc7MoQUujj07fBto-JHYHdOIDEPSOhUfhT7qax-MPSqucxnBUBiQ2m4iP3QL8WyoWRP5FHMXEmdso-1DhX1XJeCqZslIpJcbXd_p0zoiPsWIs13oR_irnE8sk_HA-jg2IKt9m1hbgFsv1sx7WVn_xlLI-9jVsUgfLV5iGAgBs5FNgPK5MTz7xyX6v7PJMsrbh0B6R1NlNryiS3_JUakB9wzYO6Aywtxlf5zWc1dGEY8UfvpVMcRUnDewvwxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NevHiv6v8Q25CSaEa84o_XfRktaMkMoms2hPfzAuJQ52qTO_SDMnnut0-9Q-iKkj9NLjv4Nst6i92ugbjJfWgghBlsE3zFfWwSd1W8Z5gU7uJqHIfwQ36m6JabieAtJwUpI9VuvFsa6ITopCHc6BzedjHlB5WRKpV3E3S5hF0wQ3K1VOOGmFtRpI32t7oPzn2iSbTgKxjEzU1dsLICC-_2jbLB_Y4KHYaMrWWBPbtxvaPsUSRrWV458NlQ9jUPDLihD4nv1bPiCi8F2WF1s04hJwUcMUjt9NKaZOpqdaCE70-qNqSWC2_WPXDSNbvUhL58yhg8XBkMm6SJkk_pEPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=mH8BOs0khY5sOEEBTlYraHlP4OfZI51GjE4hLFDXuaMrk4Kdv2FEOzNSXmkR_swM0bEW3ermLAMRwI4ZHdvId-12YczHFnGg9f9AyIGrVcmG7bV_-4xBW45IC8YZcouPQgqzX3YQOVUc_phr1AKe1rXp8q4593AfasUWhK14STLKWP7lW9WI0rAzySaz9BVVK8xN5Zdqt1Wpn1PAMwDTG5hKMn07k0aYS71owgYJ1WefRwpBmmojdckjR5FA2pRBfZ0KgifZnvqSdGVA4qPeCBlD7kVnJc9_Od1bBLhl8xql4_8svOZG2kRYnpeAMbY_9kDGmbX77DR0qjz7eeJKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=mH8BOs0khY5sOEEBTlYraHlP4OfZI51GjE4hLFDXuaMrk4Kdv2FEOzNSXmkR_swM0bEW3ermLAMRwI4ZHdvId-12YczHFnGg9f9AyIGrVcmG7bV_-4xBW45IC8YZcouPQgqzX3YQOVUc_phr1AKe1rXp8q4593AfasUWhK14STLKWP7lW9WI0rAzySaz9BVVK8xN5Zdqt1Wpn1PAMwDTG5hKMn07k0aYS71owgYJ1WefRwpBmmojdckjR5FA2pRBfZ0KgifZnvqSdGVA4qPeCBlD7kVnJc9_Od1bBLhl8xql4_8svOZG2kRYnpeAMbY_9kDGmbX77DR0qjz7eeJKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=lfAh_MO2PVSs4H4mCyYpTpa7PTnm9Ff5L-uifXeEolZVl5Hz9UOpaImD9N58rkffe07osN2CTHz2F9f1yy7NlsCXi9f8eoOyR4iioMpifSxhi_D2EkY0UeaaooR-sCy7jZYDBhl-dNDEeXt6j6JbmCijrOL7K7T9GZnLJqa6qSMapgNVrntfzX47XHyUIZQa4pNeq5vdsjvzAz66R_IPLlW8dqYeU7oRyO-yEhWC1vL394A0wpEflpOMl-aa1kgy2OleiNVUFeiUW8YOBavbppmDcHniuCDM3wdhnFiHdBxxsAAjxy_jSmlwB21VoTPHgg3ufcMWshkUJeFbcPTBtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=lfAh_MO2PVSs4H4mCyYpTpa7PTnm9Ff5L-uifXeEolZVl5Hz9UOpaImD9N58rkffe07osN2CTHz2F9f1yy7NlsCXi9f8eoOyR4iioMpifSxhi_D2EkY0UeaaooR-sCy7jZYDBhl-dNDEeXt6j6JbmCijrOL7K7T9GZnLJqa6qSMapgNVrntfzX47XHyUIZQa4pNeq5vdsjvzAz66R_IPLlW8dqYeU7oRyO-yEhWC1vL394A0wpEflpOMl-aa1kgy2OleiNVUFeiUW8YOBavbppmDcHniuCDM3wdhnFiHdBxxsAAjxy_jSmlwB21VoTPHgg3ufcMWshkUJeFbcPTBtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnkk1Em5Ux79FTxIFFOpanXq7khMEHfvteCy3icDWwcaqHRAVmW0KHDSZ2bsD-5BKDY6zHb-VOMRUNFgvP-aAMFNJn-h9nXUf5YkWF6EEJXxXtSjZO64lPhPpJ80LBMsnpE_R_eILSsBAs9CsORXd76NlFTy9-S8FAMV2XmDx0j8vGruNCMJZeMOlmcZgh3qrLbi6Fc5oloIrd1TYRJpKhJLhi6xPgi3t9tLPAchmdathvwz_Z4e0_9QXUZykeoMe4aFnDFLtMv8I_5N1s8O3jKB9n77CkHHWEBskIWyTpifx_mh8w3ORjdYKYfsdEWjCsTsfQoqqvRWIz0v0Tph7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
