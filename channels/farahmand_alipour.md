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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 00:48:02</div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzq-SJCeK5iUsRqrtzeIl9PiPEA8q3oSzYdnbVRLY80icvC_4LTQciHrnV9pRKte7WeyE-jBbb7S46Bhhx8Tuf25UUn-H8UrM2QSzbH9tgN7ATXL_hE8NlfaCv8jXLQ-QZlxogfOW5npf4VGrKBt4wovK8rC7H3y4Aak66zjJteOhkmZQGcBL0iyKnTau4tjoTyYssEh_wu5vzDhg_G47-vDe4dl1y58G3MUmn-zfxX0DCeTHV6yT4SSVYNg9lOZM0NYQxG1q3YwJpqAgiFwQ6A0qSXw5dtPjrVLT2DRu2pTeto4sAKY1rDdAdPhW5d20-XCq0zuWNuZ0o8rtW-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvabggeV_gp5uCRBhKTWs-Ue7yxOdq_rfaAOvs2UrdfEteqQjXhE79lev_iS3wcYrEYbbHceY38H5CKlIjE0ZQ5PByez3fvvNvENYL3xFw56HtNdE0H37mOJ_IG2wmtb4my_GBs7zEnlnky2Vx7RbB7Leir6DWzCQ-TsdYmtJZoFoDIuonUYYtxUs0bZV6xIXj-HQARCXDUVW87GtKVKrRm8L-bx5DDclgfLkpUV8g4i6ZCBxPTs46o22Gn9nO9CaIvMaJaBchZIOyuyYkC7xja0G_LV_lC6brjsU9XPuUSsOv2-Lka37BFRgz1MpvtqBo02kRp7vE9u5I2ZHdnvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkWDD8rY5G4nSdXYwW2TdbC0X93oyNnIstH5hwDH2iyhDhujGBIqXTR5dvrDHfL-1VY8eXjMxUgsCwIPnIm8pS-k0Ep-BPMRDrvRlCR9A6-wz68Q_L-TbBs9QIZbLCQ3EEC9g2LQKU-VbssvD2Wq7o2i8ynJqXx1m7A83swoqqK0tWd2augq-dLFWjH2OmGpTbvdljlCgh0E1iJKIZoSykjf3Sv6urKo88iH9asobAHH6kUKZWBD1EEcRqTWpjKBtAxRtydDRWlFfLApnE4l7xaFLFa_ux9TPAmMtN2tHmY0rIbobhpMzGU0EEP3ZnuVpoZeV1v_qOJONCxpVnzhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9tfr9ooPoEpSVExNRXoTSfCi99IMOf43EUTZkyDnZJ1VEqhOs4ICgESZC3HQ0v5oUWv7MdlQKkNGMO0ovUwgHlIRpGmcF4E8DlOqYXizKzp9UyL1Ygkf3yjSRwQzumloGU3INOSlD2aDlYdXgQ1MyuYPKyNGclZub7XjpYRsVmXGDMHOOK00dDUArt6W9XI-sTMlaMfIwR0skCWBi_ty4nU1L51Mcwyd2F9O0tfXn5Na28Sk41vDRl9s2ujcxhwgKqJl9q5uuG0dFXFerU69EqEkUMwPDNttQv27Ozi8P0huhI7tO8gDeBQthISpM7rZBz1DjDBNuj-8FGeVrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIY4IQfe_-jkn7hX0ZFA17nUWwMhxDDZ8t5qK1EbO3GuMi5nsJhgVS5PkAralxHLinuSLgFLoQ0qoTIsAns470aozIMKynerLLRoGDAdCvsIhbR8FeB8pU2cDHrUDjeX8Qn2nX1Y2B0U7Y33CCEULPlPSap5fCb_eCa3ezQOxJF4Jxrlc8tAEf3M99cEtnCyRyGP2WDYib8tG-Qx0vh8QJXSMmaBovXRSk2vURFQvh-Ca70ATLxUnjGvEmRMsakCEF7HksgHL1da3YfyYQkSx8khSl9BFf40p9ZOn5f98fQ0xWG1Eav2qpoLEb2IvTynju_zNSQiGFPOjZSe5lLGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZEUxik4qkJOxt2zT3M0zPIEtgXQV5xt35_mCBT17DAz0rWwr-YZxJ-w4w7O355ISyODabxtHfiUjw8rZi1TLgUhoU-WHv-hk8C2HWLRP-Bnf_ACQ5EQc5v_qXW-Q59GM69UTW32x5rRJLNOjL7x42dAJ569rymI2VVdkGoNE4kI_TD5k04zPC5BwOR8Ab5j0JkrSphgWF50RkPDWeoP8nzG-BlRIFeJalW7jM3GZjmwEQ8U4maGJ4BDRcJ2gXuyTiUV6ssgjIYFknUsKqtFCcnIf78qGzsII4asH1D2B-Bns9r4PLNvAmpSSgV2NdrZpKLiXvx_D6FrN7SSSy28kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbQ88cbc9JkPY6MBzhTdnlh1gN_DP2rftIDatKBIBa9g0seSU3ApaaEHWGLNHJm2fh989ZF4aukxXwturVk3sYourRCDw9s7pPou2D_7bkL5LJhi39CXaMVnL7RFJfEN3LHNxZqn9Xuu57yi-SH-LJYZej8aqh7EaBBlT9cKGZmPkGpGjDsm40FhZoZx6IyfYmhDnEq7Cw_Pk87Q9K6nHgVxofpRfb7e0PScIswKS2CekyuzKGMaTeebN5VhIJ_RO98kCUgfYI7Gf0m-FhgqvnrUNEoU-KDdyMIqXq-oycCuV5JKVh2vUb0CPKztRfpJLh9o4P1aPIfhkyCdmtovRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=IoUZrIzUlAStS6KXLwPgNQEh6vcZVy234b-_kul4XCae_-rpF5-Qmw5b3TJ1ms1G58_IhpcasdW7eblLt2rBQOHk0241ggvcq8XrgZeyV9tVXO2KRft3u3MbGKxXnRHTeyxmRmDpgpqvGJpsKXFCQuKsLXWEuyxkGrXrJse6f-xb7SI8CFzrJi7rjUpsRVJe_Nvu19EBUpLVUWVUwf6SPlNuTpiUcpDu5vSQk76LnUa_W58XnO53zkIK2e2PwY9bdxPfjNLofrmvswZ29lJXBwaqgDgyszoPWFs-UtTI2AaSDwHfJBx4OmsTGAAzT6JXyFYYyYNGxxelS2XGxLpJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=IoUZrIzUlAStS6KXLwPgNQEh6vcZVy234b-_kul4XCae_-rpF5-Qmw5b3TJ1ms1G58_IhpcasdW7eblLt2rBQOHk0241ggvcq8XrgZeyV9tVXO2KRft3u3MbGKxXnRHTeyxmRmDpgpqvGJpsKXFCQuKsLXWEuyxkGrXrJse6f-xb7SI8CFzrJi7rjUpsRVJe_Nvu19EBUpLVUWVUwf6SPlNuTpiUcpDu5vSQk76LnUa_W58XnO53zkIK2e2PwY9bdxPfjNLofrmvswZ29lJXBwaqgDgyszoPWFs-UtTI2AaSDwHfJBx4OmsTGAAzT6JXyFYYyYNGxxelS2XGxLpJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJIkUMZpt6hVDGH9w5qKYgRFFFiqXm4hi8DWkiCy64IagJztLLL4LnIfAU6m0udkfY3OFHd_uAbMDVAZM4QzUpzqwEyJ8Qwzj07TmIK3iceOCLAxg5OiC2gNfAbI5zXvTQGgDUn2d4UhpfHa9NgVmKX6L5PrR2H85OSvrseAKszlmCUX6jsbzvYBQeK8TyLqOb_B2tWfVNVi2ZI4XdHq2oBHcA9wmSUdPuintM-Zs-XJDTKKc6VMBWvQ2a65SHTCo3hACHnhZEJZKvYUDori9BSL4Sn0bdtlC4XhsnWzQUOuZLg8auq_I42kkfEJlEb58Ob1MW9BFhZC42UDPH-q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=WFVCK2WlSycKOeOWsl7pukN5sNpWXAnjhjg-Fdc9xM2H1y2-jPuv7y3z53f3rvoz4P92IAuJhG1teIjlrg2_NH5Vxt_ciEAGx3ua76npczxeGzTF-egQLYDRCn59hiSo366GAA41KVNvKPoszRq1nK2k26hz3RhG1PzqLLgXH3C7mFy5ApsSR0SxWnb6KwC-S4U-xtS8ohQXp29jzH-1GRErwg3EUswxpTvpJGDZo8JONxeY_YFOl537F17JZoYVNwCRKykcRxnMaIQIZ8IpRAIm9iPA9DgPcFZeIKrY8pWoR1wxrkwxG9dVve42bj5W1mBEzRib9FOXhQW3qtGJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=WFVCK2WlSycKOeOWsl7pukN5sNpWXAnjhjg-Fdc9xM2H1y2-jPuv7y3z53f3rvoz4P92IAuJhG1teIjlrg2_NH5Vxt_ciEAGx3ua76npczxeGzTF-egQLYDRCn59hiSo366GAA41KVNvKPoszRq1nK2k26hz3RhG1PzqLLgXH3C7mFy5ApsSR0SxWnb6KwC-S4U-xtS8ohQXp29jzH-1GRErwg3EUswxpTvpJGDZo8JONxeY_YFOl537F17JZoYVNwCRKykcRxnMaIQIZ8IpRAIm9iPA9DgPcFZeIKrY8pWoR1wxrkwxG9dVve42bj5W1mBEzRib9FOXhQW3qtGJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=JVMaokwQ2dyb3Vj9V12fRPQ3N7HYU6VYixdO9A2x21fEcHfGR5h-W2Orxqni8MBtgvwwQC4yE17teYj9wYhS8R3A9xvOmtx4C7vGMDBLPkNC0T3XNW2Xy2JCrtEqtrnvNps9scZKgAm6lil7AnhOghg3A0BbFQ-hQLRBSY9O5vZCSKRCue2OMMqoRcdMDRKC-W89O-AybETcjL_K59Z-l1dsknGimDV2dsslnBwTgP1ExhBejBx0jSmR1hbRkSe9Ryl8X4_AkQoFz0gGBMIlLCxnfqYzvNeLHMEjAZxLS4Zp0vmHl0XtQdqBFZBX5RQF_aLWE2LgCqmYIXtFDbfdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=JVMaokwQ2dyb3Vj9V12fRPQ3N7HYU6VYixdO9A2x21fEcHfGR5h-W2Orxqni8MBtgvwwQC4yE17teYj9wYhS8R3A9xvOmtx4C7vGMDBLPkNC0T3XNW2Xy2JCrtEqtrnvNps9scZKgAm6lil7AnhOghg3A0BbFQ-hQLRBSY9O5vZCSKRCue2OMMqoRcdMDRKC-W89O-AybETcjL_K59Z-l1dsknGimDV2dsslnBwTgP1ExhBejBx0jSmR1hbRkSe9Ryl8X4_AkQoFz0gGBMIlLCxnfqYzvNeLHMEjAZxLS4Zp0vmHl0XtQdqBFZBX5RQF_aLWE2LgCqmYIXtFDbfdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLonYtGmWa5SGPFi7M4lWd1i1fDLTD38VQC6vU_CsSWpOra4qzWLOGntaLNVCd5Svj1T7OJh0hULfrDELMPJEV6LA4HIwkRwgzOCc-3iwapIWcKAFlFRPpr3x8_gkb4XwKlnd7rOzby0asnSj3yL_F69vIjDmpyusFnPYVxh0Sr-LS9jwEino3rIcoKRYdkjNpP2NYemrHGn08iYiCzVv_HBCxDJ3ssZLRQHvG0CLwObJVv6Agj5qKc_5J4cLT6xKel0qOg0NqDfooZAlcNO2juk_8dZZ2rGwVtJsdghiKR8soLIxKpQrgZVKQIeGrv3rOgDrzl1orw-VlioDy9KJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=ZV5DKEjdyRDacrT8SXSMFQ9q7phvCqPZFkEA2mvXDh9aaun0gC0TMFUFRS1zvC0GJp3seUtTKJ6eMmZwym9JDSy4Qe7kqlC1JGAUBBdLllnzzOmkN4dZvBEdep1lDanNGSZBi_K_4aYyAsLayDGrjsY8sO1PNKTXMO-niYWf-zhGuNxgyM4TU-UrGDupYpis9YmjUOJsRGyqEp0U1oJ9g2_Ynynb12DBq_xjCZwsiOjBhU02Yc2utyTgDbqREBwwq35V721OT9GGQoX77KWmAby-eb05PcWX3ODUAS90LcKKsVhFcchnHWfM88H9toYUR-nqaoNiJoE8FxC-kRONuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=ZV5DKEjdyRDacrT8SXSMFQ9q7phvCqPZFkEA2mvXDh9aaun0gC0TMFUFRS1zvC0GJp3seUtTKJ6eMmZwym9JDSy4Qe7kqlC1JGAUBBdLllnzzOmkN4dZvBEdep1lDanNGSZBi_K_4aYyAsLayDGrjsY8sO1PNKTXMO-niYWf-zhGuNxgyM4TU-UrGDupYpis9YmjUOJsRGyqEp0U1oJ9g2_Ynynb12DBq_xjCZwsiOjBhU02Yc2utyTgDbqREBwwq35V721OT9GGQoX77KWmAby-eb05PcWX3ODUAS90LcKKsVhFcchnHWfM88H9toYUR-nqaoNiJoE8FxC-kRONuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcl3qZS3jYc2aYUvF44Hr6LE2zYysBQWBqI0FQIcxiKUP8bsWYBQRkJSrFjrOlQY8aIIbqi3hcZrFczqXP37a-mFdWdi386lengGouqBn6RRQ-mFHa4yqtDKSjeJtR8H0vsofLaZOnFzStV9ys-Cy5JJCwC_GT62oIWmYjt1LAUTrTo9gHNdCXRidhk-5GomrEfbOcNBUoAQFWSa8ukc4sD78jYDfgIJdWNiBUYunTWAXphiolzGh1i-gAikr-Qu0O1kdBuGFGjBWC0AyhAlf1uHVLU3ALMCcKjLiUiSiSlZQyLZKzxG281Z_OyjX7mGA5fx3VclPJvzwwS0e8Woxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPQfXJknIw4bAsvi9BsJaNf1c73NPr_ePENlyiUE9yx1bsdsFlKNMuds4mlO_tJJBUacryq1KJfefgloYDKpcTYWkNDUX6adLO0S7woD3BdFsyEryMelx5NcLeZQiTuJt_2kPIQxFJAfBdHfyVSDXNbvtHby1lVSGbH8gtPt-in-Xv7dhfFrMhDVv1TrWlIhshkOmZDwtlTc-Siwc3utROuGFxnWF4EDfMNvnRGE1Ez2T_-ICY3ylHlQorotU3_f0-Wy1Z98jmLw-RZnveJMcaK8d4zqShUxx0Om4a_na0bQt_ZAjiEjshiAvisC2nktqOUW5S1J8Cr7nTh98aGRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-N4UGWMt6iCzRfXHKNX-g5B7s5YS4tIp3VmkJKWQWJLLQ6HXvrWVJje0qzMbs6pvd-hV7voVKYlip5Y0oTOaQ47PM9CLRWEP4tALzBWtBwNHZINDTae6G8YBIUULJAjJKU1SR40teEQ2o7GcMpztJ8vrMcqZxuKWQ5BiLCnAuzWx17lkPfC6SC7xRqENZ4RJARKeCp1-LsMDwBRBwFCZpzXu7h9XrIqdYPtowrZFSOAmejAqDj47coGrXoThALew4yZI2sIiRgBSppVw2iMvzBj6W9l7Pn0MLSeOCKohk_h-wtzlyHLP55TVE2jqtL_DFw6AEwMuJn_VkvPO-Qm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY_6oFxJZy-j8uUQ565N-r4mULKI7ZIKV1KCtYlURzHPnIrNk4TwbmdLoTKs6Zad_Td6U3p09jYqqbsEvv1scOTitI4h8Im_cZzkTHv_R2GP9NXJdvIGc16ApBV2LxBvuIEcYs4iq4Nipndgot6Ey27qIP6bNlsTjo8Ttz-6DHFDyCbl5YPVa1OWBvlmJtoWR8WE4iEmURsmyWqUNLj4it4HeySr_OMI2SCpYecJuAR8yQuDjwKA6ImcS44I1q8Lot2vyyrg_ssGE2fwd9n5cBGzPtXh8vFWn3ylglO0UhmtGSVo9evowWVsKJ6_xWT9ni5JhaLC6e34KUt1eituig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=LpnWpDg42xbMwvrxOjshqadbjgLN2V6BGrjCc0dYkz9adDieORI77dFkRtHZlYu-417QCnSkM0kI6hwgHR7yMAUi4I7zGYhgDTcpe6kIRtQur0jgCtOG4AEe6qC-9w9aeZbBMGEz-XqXsk7wQJY_sgQHLAYBrBk2ZCj57IV9-Qf84WhE4FlFJnWWx9HKeaSoOeViKJzvDghBK1ZJMOhhGroS7M2kwGecAUZnignW-NMS27RShH7LQh_sbuc3xtAV2DI9-RhzwL3jO0YIZvjixILfErvaXeqLupuH3L7DrjE3uzU86PNla8WCkOw_Q_nQHfT8cA5GApWN9ZENuE3p4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=LpnWpDg42xbMwvrxOjshqadbjgLN2V6BGrjCc0dYkz9adDieORI77dFkRtHZlYu-417QCnSkM0kI6hwgHR7yMAUi4I7zGYhgDTcpe6kIRtQur0jgCtOG4AEe6qC-9w9aeZbBMGEz-XqXsk7wQJY_sgQHLAYBrBk2ZCj57IV9-Qf84WhE4FlFJnWWx9HKeaSoOeViKJzvDghBK1ZJMOhhGroS7M2kwGecAUZnignW-NMS27RShH7LQh_sbuc3xtAV2DI9-RhzwL3jO0YIZvjixILfErvaXeqLupuH3L7DrjE3uzU86PNla8WCkOw_Q_nQHfT8cA5GApWN9ZENuE3p4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=vfCor4jL_RsxacbKhawTM0S2vFM2BeIjhtZDdiKqkudCZUZ8bJqrb-HjUnxzOi2nOnbpzd_lEDiumzs_OvQvEekM8OIKkxa7SG65bPPTgF5gA-SJH-C6_eqmrlM8g72VulQa0e_fcpxdgZNmvc7lAhAKNBfbWJ0rVJOwMvoq9MOgwpAbpz46i4DKkT-sfQKRCfudailXqRXVCPb7U6lbbf2XtUwF6u7v3Xxg6mfl2inKlL8ZEnOl0DokIo9IHfoJ_LHRb5UpRjQmGq7lwcRCgbj_roKl8b5tEmnLpTh1c92zbpgodQ1h2n7SGffLQ-Y8BPCJisv4Ra3PyaeGdT09XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=vfCor4jL_RsxacbKhawTM0S2vFM2BeIjhtZDdiKqkudCZUZ8bJqrb-HjUnxzOi2nOnbpzd_lEDiumzs_OvQvEekM8OIKkxa7SG65bPPTgF5gA-SJH-C6_eqmrlM8g72VulQa0e_fcpxdgZNmvc7lAhAKNBfbWJ0rVJOwMvoq9MOgwpAbpz46i4DKkT-sfQKRCfudailXqRXVCPb7U6lbbf2XtUwF6u7v3Xxg6mfl2inKlL8ZEnOl0DokIo9IHfoJ_LHRb5UpRjQmGq7lwcRCgbj_roKl8b5tEmnLpTh1c92zbpgodQ1h2n7SGffLQ-Y8BPCJisv4Ra3PyaeGdT09XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ULz8gGGt_QDn3K-miovs7zpqfTm0tC-fecEGEfBrZrTV_wPWkfER3424bUqSqm6sBFV1GGCeQUw3oDxZkrfc09BIIbMBkElR6HRdbrwdw52LybziroHFyjk4-Kj-MRPGDcIgveoEIbxO1VPjhP0QorcBZ1xa7UqdAPwYyWtEy8AQt9J-K98dxBuFBkZtJyh8gRF5AdN8XwpZE6y2WWwdOyD31HXe9F0wEv0cKEsVYkWZjsmg6-2yetTRPBCf4r5UjvCw2z0iVG8qtsYlTKH2mom4QzN7uWe7in0dMY4yGMp9yuyCXcmeeHr1M64gapvSm5wtPuxt7Z1w1aGUH_RqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=ULz8gGGt_QDn3K-miovs7zpqfTm0tC-fecEGEfBrZrTV_wPWkfER3424bUqSqm6sBFV1GGCeQUw3oDxZkrfc09BIIbMBkElR6HRdbrwdw52LybziroHFyjk4-Kj-MRPGDcIgveoEIbxO1VPjhP0QorcBZ1xa7UqdAPwYyWtEy8AQt9J-K98dxBuFBkZtJyh8gRF5AdN8XwpZE6y2WWwdOyD31HXe9F0wEv0cKEsVYkWZjsmg6-2yetTRPBCf4r5UjvCw2z0iVG8qtsYlTKH2mom4QzN7uWe7in0dMY4yGMp9yuyCXcmeeHr1M64gapvSm5wtPuxt7Z1w1aGUH_RqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=N6PjJlaFINzwm-8RHQkhYgVKTesNnsoB48RYUz0f6gydMyvcQRbahOe8DiQ3eLQNkp_PxibMp-j3Ti8Zb2lSlbyQr79Ac3NKOz9BgHifJIcjVa-JKlRwuMTbtFc2JSr14bFsAKAzYXN8OEWq3JIJYjqm-19-BTMkVfuesNMAq69lIMmYvBJ9ghetNYveWgXat7xAgc_M2cDhvQZE-X-ZI1pb4fQKHBe7h0xEPpvUQLmns07q8Qr8mflLASttMQG5nuVi6LjZi9Y4D2ohC84B4YmL2VOvimh9GRcfGQAzCm2dOuX0UhQZVaIvEboku4A93RY_XLmboUXEWBuh0HJQJ4U01wgqR81e7UbVavr_vCVXEESpKDVOrcfvjLVk7Dkt8Phs9HCqcahOBDTO2YZeFeP78xfcU1ko6czF45Na8eX2iq-yY4LyUjIGQHYrMqaeFkjHIwYbs_Buy_dncgThKEVJ_FfFPLsKHUAUsclT153BJsXRZaMuTnSvYtownaWOoUYSdHNYVbRhaOgO1O3OEF3hsN8sy_NoxNG4zRpMIe3GcBvGwpijeK1eUs5YZS4Y0SFpSQbulGfSt-nL3FhYpvze-s3lnS2Qp6_PNuFjRXAtAYpchEli0Ql-mfE5CZZdgmW9cUBzQMAygop3v9f6NTzrDXJwW6WIUvTBoXVsJ8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=N6PjJlaFINzwm-8RHQkhYgVKTesNnsoB48RYUz0f6gydMyvcQRbahOe8DiQ3eLQNkp_PxibMp-j3Ti8Zb2lSlbyQr79Ac3NKOz9BgHifJIcjVa-JKlRwuMTbtFc2JSr14bFsAKAzYXN8OEWq3JIJYjqm-19-BTMkVfuesNMAq69lIMmYvBJ9ghetNYveWgXat7xAgc_M2cDhvQZE-X-ZI1pb4fQKHBe7h0xEPpvUQLmns07q8Qr8mflLASttMQG5nuVi6LjZi9Y4D2ohC84B4YmL2VOvimh9GRcfGQAzCm2dOuX0UhQZVaIvEboku4A93RY_XLmboUXEWBuh0HJQJ4U01wgqR81e7UbVavr_vCVXEESpKDVOrcfvjLVk7Dkt8Phs9HCqcahOBDTO2YZeFeP78xfcU1ko6czF45Na8eX2iq-yY4LyUjIGQHYrMqaeFkjHIwYbs_Buy_dncgThKEVJ_FfFPLsKHUAUsclT153BJsXRZaMuTnSvYtownaWOoUYSdHNYVbRhaOgO1O3OEF3hsN8sy_NoxNG4zRpMIe3GcBvGwpijeK1eUs5YZS4Y0SFpSQbulGfSt-nL3FhYpvze-s3lnS2Qp6_PNuFjRXAtAYpchEli0Ql-mfE5CZZdgmW9cUBzQMAygop3v9f6NTzrDXJwW6WIUvTBoXVsJ8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VHMBhOtSeWcN6YnoZPGjMI7X5ki7OVDz_ryn0PoLkwOMjzO6Zg9irNrTxMcmml5XT5wT7_k-UUA6B14UJA1w4bLRJlmup6XHhRDJvLwq0PUP6-YskGDttH2xu8CXR2rud6j2xKQl2F9jJ53_ixYr0bDYvyBVLDPd-4zO33WzxhszOsjit4UjslVjCvGcnOn8AUNLLBNLD0F9raAoAKJt1byGT6ZeBnITisjNHyP-cNlxOczbmPoGQIHSoQ-SFAxbKmIk7AjGfGq8XU_yoVQ3lvbwm_07j8myfHUbGJh3QmQ0PXA8PYS5DVANzPJFkdXPUmlBObtOvTHKqTzxn7WmFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=VHMBhOtSeWcN6YnoZPGjMI7X5ki7OVDz_ryn0PoLkwOMjzO6Zg9irNrTxMcmml5XT5wT7_k-UUA6B14UJA1w4bLRJlmup6XHhRDJvLwq0PUP6-YskGDttH2xu8CXR2rud6j2xKQl2F9jJ53_ixYr0bDYvyBVLDPd-4zO33WzxhszOsjit4UjslVjCvGcnOn8AUNLLBNLD0F9raAoAKJt1byGT6ZeBnITisjNHyP-cNlxOczbmPoGQIHSoQ-SFAxbKmIk7AjGfGq8XU_yoVQ3lvbwm_07j8myfHUbGJh3QmQ0PXA8PYS5DVANzPJFkdXPUmlBObtOvTHKqTzxn7WmFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=fBH7j-AzhBNRc7kGeYQ2wD4fU0lHDeVd-1greLpLvwwVNoVYSX3DpTE6Y75I7VCJE-Qt8vyWfTRBdUj-ZuRu-1127Aa9Jracam_6cEKoeECnZHh411XyPgjzNHR63vI57rMIglDO_IipBk61ukANjcuigj_umij78ZbynEx2IkD7NpB3q7U6xMDn8a0svgn_Lft6rg_NoSRmA5onXD1ylcpSA_6A1DmiSilqH0o7xAd2rKKjD7bJH2X1XK2NqDQpcVknTInlI6tFU42xcGEIcU0RPbMR7vc2JF7Ig90WhuMFEuv-TGlCITHuGukT-hw4nUTca5T99ANzj1T0BatLuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=fBH7j-AzhBNRc7kGeYQ2wD4fU0lHDeVd-1greLpLvwwVNoVYSX3DpTE6Y75I7VCJE-Qt8vyWfTRBdUj-ZuRu-1127Aa9Jracam_6cEKoeECnZHh411XyPgjzNHR63vI57rMIglDO_IipBk61ukANjcuigj_umij78ZbynEx2IkD7NpB3q7U6xMDn8a0svgn_Lft6rg_NoSRmA5onXD1ylcpSA_6A1DmiSilqH0o7xAd2rKKjD7bJH2X1XK2NqDQpcVknTInlI6tFU42xcGEIcU0RPbMR7vc2JF7Ig90WhuMFEuv-TGlCITHuGukT-hw4nUTca5T99ANzj1T0BatLuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUNmMs6_NF4AcMH01zNsXMSNe-XD52RTON45ak_vjux3GuQNyA-hQG8h378_lyAkxvQG0cuafIDGuyvmYz0e0TkceuSc_NpWLpErKtA4AhxZx7oDHy40HlRUxndavbqB9s8Yh-EUHHK9qp8_e_YFJu6yoZsDMiWCtAnNgczAQq0TOwFvqvBZejAo4Z9Z_CVCrqM_DCmu2h0aVDyz6BYNR569VykauKcFVzenDGFB4hIdNavBug006ZbiSu_PKEfUqXGJb9bJ1d_gv4xWmw0K5O0obuuVUvXayEkUPz0Pgt2kupWJ0T7YrMIyHSsKPHUj9q-j1c16rqYVW4q32vdcVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=L4KUgrAnV18-Fr_OhF9kF3IGbrs2VYALyPi1nfvksFKNGkL-fy7aO3ofI2EWsev_g-fNbIPT5Fn4sncl43fqBbnhbdvC6lZU_PJcLP9jtEk_ApNnPfekfwwWVHTY-8GdQcOl5b38l6SRxfy_XhC3FoXjDi_r3YZKix687ExIewvEaaPIhlpwMc8Z4cME6XXQq3iZZLidu9UBIdztNLRJvidTtgukOsHJvgEJdxHhoJYCD3DBrsklolxems_LfNwq_XcgNcLwrviIL3sBP9wxA5CTS5L4z31iYAxsRMkZMIQslEN5QNyjvPCgrGVsYqdu9wQ-CEezowKhNYdGfETBfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=L4KUgrAnV18-Fr_OhF9kF3IGbrs2VYALyPi1nfvksFKNGkL-fy7aO3ofI2EWsev_g-fNbIPT5Fn4sncl43fqBbnhbdvC6lZU_PJcLP9jtEk_ApNnPfekfwwWVHTY-8GdQcOl5b38l6SRxfy_XhC3FoXjDi_r3YZKix687ExIewvEaaPIhlpwMc8Z4cME6XXQq3iZZLidu9UBIdztNLRJvidTtgukOsHJvgEJdxHhoJYCD3DBrsklolxems_LfNwq_XcgNcLwrviIL3sBP9wxA5CTS5L4z31iYAxsRMkZMIQslEN5QNyjvPCgrGVsYqdu9wQ-CEezowKhNYdGfETBfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KODMrbSTjyKFHxrwFfagWqL-1lMfsCxMwnPO6F4q0oa5jtxy1QoTS_-LICTxnz9iu0Y3SPYFqM7j_e3eC10yyR1OERNFqQ1HZuSThU6AaiG0p-HEjETSRI0QpJDBUU3uE0lU951hdTloizy4Owa8k8pRY_VsxlGZyAuRzpZfLqLiY4sBXa0BwZsiKH8H8_1kxPYDINIsMWtcDasl1rGYQ2AgDMJKrQe8TkfoV68Godvy1UTndvgiqRQuiH9xC1eKYyWaMJd7n7JEkvEttcqKTGO9Sgv4k6RPZKSyVe0I67MYb8r_iHsRZTLCiife5VRz4q6ayjiRie5lNBMvw1UH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnYIgWsiKpTU4a9x1E_i1YGU4oSPW2zZbgsmUrdIk8fUsQca52wVv84ymBi9Nf5FP9OxjhXDUXG-66u-X8nd-uJecijfvgLLVppI3-ZZxfORuHQ9NWAQdbFoTdG-KqsgPEY7zZhQdnQVdQWmOzoHwJh07mbgdEn5nGQFQSR829wOCPWHJyfxdXaVG9w2IgZ_3uuDoco7KOZsOYEJxPSJ7BcQ_sNfZMe3RzpL-8tLqZqdQIzju6Dt3IuiAKUjRZhM1fxnUdmSaspR-iwodFTmb_EHL-ZsaD1DygUFC0kHuL1PV8GPLeO9xaBlV98fjXQtGuuQrmgKFaiAKOTI9CLQ_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=RPMJ74xByf_CqcqO_3w9QYKdUGw-neey0u3ZYG3LjI5a3N85S3jCiUOGIBw6qbWUXbmMS20KcNS-LSAE1U494FEbCW2L_QB04stqCLu3q3dCdaJtfP4QINWFKZ9z4queHO6Nz4hYVuWNR_vnsoqGxmxvH8apZTF4M0jNR-0ngmjpnIh0prfQonHZ3OBQfxGjDm9wGmaDu2NwpQRSxZzoNmZNahOLLWWrQWcRSuyMtr8sFiR-TWR1TlXV4NIYtSguuak5GfePwkGU9gZCePwqEgeB13xL98LvNNq1RAarHna0lB8-z6ihwCiVUBu4dFFy9pqKSK-qBLKHj-0tkUYozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=RPMJ74xByf_CqcqO_3w9QYKdUGw-neey0u3ZYG3LjI5a3N85S3jCiUOGIBw6qbWUXbmMS20KcNS-LSAE1U494FEbCW2L_QB04stqCLu3q3dCdaJtfP4QINWFKZ9z4queHO6Nz4hYVuWNR_vnsoqGxmxvH8apZTF4M0jNR-0ngmjpnIh0prfQonHZ3OBQfxGjDm9wGmaDu2NwpQRSxZzoNmZNahOLLWWrQWcRSuyMtr8sFiR-TWR1TlXV4NIYtSguuak5GfePwkGU9gZCePwqEgeB13xL98LvNNq1RAarHna0lB8-z6ihwCiVUBu4dFFy9pqKSK-qBLKHj-0tkUYozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MLPfCwPi02AZumYMMYnyGzjv4Zp5zH82jakxmNQZmtgkpYNz1BHqoLGGukQnXosaDsfZmBLldGpyzEb9o0-JDsH-wvUN2zD7-D1ua2D_SiCsFE9mdQ4F_pfKQsp9VYFFxvoR0VJri2b-ytjj4QfYmvrtCAt9VGWXpcJr914F2kQwfPX5XkhtpxIBOmdrAOsXdpdgfq83tDcGLOVBgOIH7WlogU51W_EAuuGYR59dEZLFP6-q86qItOq1e5Bmu2ESBJBY8OMXvs3ivO0_nnUNlI14sXTNePMtvMoWsj7W2d3liCLBC8b0pUAExAZJH7VF0GtDYj9G5M07tMy4mVNrlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=MLPfCwPi02AZumYMMYnyGzjv4Zp5zH82jakxmNQZmtgkpYNz1BHqoLGGukQnXosaDsfZmBLldGpyzEb9o0-JDsH-wvUN2zD7-D1ua2D_SiCsFE9mdQ4F_pfKQsp9VYFFxvoR0VJri2b-ytjj4QfYmvrtCAt9VGWXpcJr914F2kQwfPX5XkhtpxIBOmdrAOsXdpdgfq83tDcGLOVBgOIH7WlogU51W_EAuuGYR59dEZLFP6-q86qItOq1e5Bmu2ESBJBY8OMXvs3ivO0_nnUNlI14sXTNePMtvMoWsj7W2d3liCLBC8b0pUAExAZJH7VF0GtDYj9G5M07tMy4mVNrlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Y3NWk8dNVERNLl7BbCSx-OKe4cWlCcgtfBaaCcsLnNkMp8v6DcH-l_a6jtuV9zoMX1tddhFv7eSNVSYR6gcJaznUZ7f1xVdUT-1iL5encf6AhWk5vdwlC6KTiFUVZDoSlZmC8IKvWXNCx8gD38mi5UP1ynLXHrM9bDYxoW-Y_yrNpyggyHfEjiBp9axiIxy0ASH8zO6G2tRJlCqE1HixMhLO7OB3PIB9B4ThxXuUIZUxSgP_nwZMoIMqPa4PZp01ACdBnM3NfZilgeHNVsjdaH-r4qHs-2BzjccNb7KA44ZCipzdNb2Fmm5DMM2jiSR7k6zU8lXTp6EOQ6bkmFe5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=Y3NWk8dNVERNLl7BbCSx-OKe4cWlCcgtfBaaCcsLnNkMp8v6DcH-l_a6jtuV9zoMX1tddhFv7eSNVSYR6gcJaznUZ7f1xVdUT-1iL5encf6AhWk5vdwlC6KTiFUVZDoSlZmC8IKvWXNCx8gD38mi5UP1ynLXHrM9bDYxoW-Y_yrNpyggyHfEjiBp9axiIxy0ASH8zO6G2tRJlCqE1HixMhLO7OB3PIB9B4ThxXuUIZUxSgP_nwZMoIMqPa4PZp01ACdBnM3NfZilgeHNVsjdaH-r4qHs-2BzjccNb7KA44ZCipzdNb2Fmm5DMM2jiSR7k6zU8lXTp6EOQ6bkmFe5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXeAA2yKHTLsgtu3YPcq8Q_UNwBQDs977jkhXnjuvNQhM8MkWJ-G47rGUOFoi5Rj-jiha4vs2S4aTSBEWRtKpmjxUAoVdeY5i0DJ_gFF3NdibzfXzqkcZpIJoWe7KDaCZfYyEsfNWocWY0DFe4wyIa0uGOIVwPn0ckJfZgZWEoQ0h8hEovvvZP9zOdmerUmcFUdrD_Dvrvg_PeB1HUAXWlX02qvv--I4xzhlwbhMLTulBBAX_-Gc8rlRl3Mz_DU23_Yuf6fzs462OFvO_LtugmqdY5l9PsrDxHNbqhF0SJIgtoOMDtldLR67VvR7U8s99I-l0VrATIAV196y2cnDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=oHwBcEhJ7SBGdh3ophm07cenZcU8HZTKKyDtK3TQWitA-B5so5quHdzdz122ZX-0vag78lndjWzRDaB2MeQF1DcJj1BqZQqN8Eym1IiUzxNSRrNn76B-85r7rsS9Pb4t710g4oI-ppJqy-4_3Ux5ykpJKStNIoFaVmVyv79bUfxVE0fdijqHBQt82lQ0Fz59er0rELK5vxvUhok_E2KZuiTMQ5guCff_2ECxiDt3vQUqEIPVBl6HTiVw1zbANcEr-bTt_2R50DhpruKhbH9TNHm_1mI5nDTZwBAryCf0rR76r9xM8Hyqv_b5vaEV38-hXwdBOrinU9oM1cndQS7viw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=oHwBcEhJ7SBGdh3ophm07cenZcU8HZTKKyDtK3TQWitA-B5so5quHdzdz122ZX-0vag78lndjWzRDaB2MeQF1DcJj1BqZQqN8Eym1IiUzxNSRrNn76B-85r7rsS9Pb4t710g4oI-ppJqy-4_3Ux5ykpJKStNIoFaVmVyv79bUfxVE0fdijqHBQt82lQ0Fz59er0rELK5vxvUhok_E2KZuiTMQ5guCff_2ECxiDt3vQUqEIPVBl6HTiVw1zbANcEr-bTt_2R50DhpruKhbH9TNHm_1mI5nDTZwBAryCf0rR76r9xM8Hyqv_b5vaEV38-hXwdBOrinU9oM1cndQS7viw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=Gn-Og_jH8d5sktyNOphTQGgSmcSMFN8SYiLMA0o6aJe8WjtxZmWRW9_vCRkPK8RCCEWRBRyhda1-HIMZc_dpR35FaeA3ecnYn_mhUnxMes4vDh5I1NpYf3NlJjI11nHVCzUQhT4snq-TDmwf8eMAg_DSC1rtmwrpTEglAFcPIscFDmSCWI7Mu8wW3c9Bm4xCOC0LX1vJ4rlEmO4yJjEyviljeU2FQj3UDeqdOtAD_VoclflA9E8df-n59ujrJVyUYePC20Wk5qD3d4SphHDFJiwsurojN1pkwy2MR579KUx9BhcMVfhcx5uSONMBrWgilCv6HjzmfFrruSvrjhLg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=Gn-Og_jH8d5sktyNOphTQGgSmcSMFN8SYiLMA0o6aJe8WjtxZmWRW9_vCRkPK8RCCEWRBRyhda1-HIMZc_dpR35FaeA3ecnYn_mhUnxMes4vDh5I1NpYf3NlJjI11nHVCzUQhT4snq-TDmwf8eMAg_DSC1rtmwrpTEglAFcPIscFDmSCWI7Mu8wW3c9Bm4xCOC0LX1vJ4rlEmO4yJjEyviljeU2FQj3UDeqdOtAD_VoclflA9E8df-n59ujrJVyUYePC20Wk5qD3d4SphHDFJiwsurojN1pkwy2MR579KUx9BhcMVfhcx5uSONMBrWgilCv6HjzmfFrruSvrjhLg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=J4tXmZjS6fN2SQQPob6lCDJEmF0QKUG5YPo7mzl8Gm5xndTrqx0kkCZqTjWdtWKwwVYOmXSx4GLOR7RJfAVLqtxyVllQbBDFLs_OtLdI48EcbVvD1nidNQSUTwvq__ce9DrZmQeOYpa0USC7lN5pUfPPsvNSKymfJcN5H10wr0Y0T-sSE13Ez-8eBcjQucJ5LDdH_su27FLxozXa4Zl7hkuPq5WbvnVWeCRhPBFG_hIrqedxHSL8l4HTdHsmv-qjyMBZ3j-1ythUfL2bmIr8ip8_EO9s_OOaUmuSzW8hjwY5rlq2WDFvixF3ldTlDlPyJ2n6jpEVyfoS2kbE64lBXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=J4tXmZjS6fN2SQQPob6lCDJEmF0QKUG5YPo7mzl8Gm5xndTrqx0kkCZqTjWdtWKwwVYOmXSx4GLOR7RJfAVLqtxyVllQbBDFLs_OtLdI48EcbVvD1nidNQSUTwvq__ce9DrZmQeOYpa0USC7lN5pUfPPsvNSKymfJcN5H10wr0Y0T-sSE13Ez-8eBcjQucJ5LDdH_su27FLxozXa4Zl7hkuPq5WbvnVWeCRhPBFG_hIrqedxHSL8l4HTdHsmv-qjyMBZ3j-1ythUfL2bmIr8ip8_EO9s_OOaUmuSzW8hjwY5rlq2WDFvixF3ldTlDlPyJ2n6jpEVyfoS2kbE64lBXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpvL7Ava_wNQm8BDXAvUt-1P8jFg8Ez6UP-ACQltg4gtrC8sKvDE6TPjxMk7Jgr814bswlU0EQbhCGielF4LjYXuLx-kVd5BFMPtRpvfeFXWXp85BpRg9KFlMOHrlWAGGLMbJVay42PpmswwUbmEPYMPbZDesPMidUvSnLQ43t6tI1zj-Uq86zYKKdXB6RdDJypHJrTR0IQgfwgRdGt0k8t8P6WNm4YWscX6LIZCnk1TCT2dgSNcrDaf7POC0OluPzVWmJICb1hF5TnOJgmkd7dhsB-csJGS6yyFWwh1Qxc-ipriTtfUJkkTUs4Lv_KE8tx4kzapGLnxFxsVh5zgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=pO0I9nFOG_QrDVXACCqNlK-uYjop31kz2RnwQeCdXf5_IdysMe_xwO_VoCtnrNYtbfMe4TtWUQzCR94nuE4H_3CpMMYbP20d6f_wJoQPdFeWVyvm7PUelD53w8igU0sIK-JF7fs3p8-N_bOBeK5LLm0WdQIGeC_ozbz5zbw48h7QmgE38g-Kyn6O-j1G9I14wwNQcWo4Xys1KYTsB8bWYCeVpHCauLpmgdersx2c_Br1OymvaFt0-IBfs2f_mvOipyWdZWNdWzw-npQZwI5KpKf5D8-_8qYZyQdjtS8M2sbggCdxoOUm6GQAkV_WHotJB_vHUd_ru4dPf1NeIHR68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=pO0I9nFOG_QrDVXACCqNlK-uYjop31kz2RnwQeCdXf5_IdysMe_xwO_VoCtnrNYtbfMe4TtWUQzCR94nuE4H_3CpMMYbP20d6f_wJoQPdFeWVyvm7PUelD53w8igU0sIK-JF7fs3p8-N_bOBeK5LLm0WdQIGeC_ozbz5zbw48h7QmgE38g-Kyn6O-j1G9I14wwNQcWo4Xys1KYTsB8bWYCeVpHCauLpmgdersx2c_Br1OymvaFt0-IBfs2f_mvOipyWdZWNdWzw-npQZwI5KpKf5D8-_8qYZyQdjtS8M2sbggCdxoOUm6GQAkV_WHotJB_vHUd_ru4dPf1NeIHR68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XupTMLOqqrOCwZs6Y84yQEuuzfQ0ykGRU9qEIx1GJXjQxs9XGKOzjQXCmzVrDYr02icWdgo2Q3Ob9l0FvlZGyAHhm0Tv-y37ckRf-S7e8J_gVM4l5RqzU5i6j-4Jt62ZytEwCRumSLHkyt4C5lgKqBefUPXXNWNarc5JEhskcWbMZLtWE2wCcsmMAcoXHjx_9lB1XFld-4fj8lFBbT4pJjKs_8j0xGdSVvJ-Riz2HyEI0oy2JH7YB6lz79h_J_JfapZopoUfrgBAb682942WoUXXPK-jW4jAUseQnocxajOxklJSmfDbJQllB_IcFs33sgoDmNn_sjFKxk6xhjaiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=iE9rKwjuRETYH-n82G1fcMKRbkGCSPf1wVSvHdZtDxGhtSKZLV0KWKGSlw0GxI00zNRobhilEucybhY6Qua9CIxPbrFyTppycd1CV6T2ZVXCf8LKd3W3vF9BxoAIzGeDcKEzDhMQOmUlguR4eT7vIbptSZJ9Sgy90HOUxWOvpcwwXKf4u0SeSJQ-aj44AIPUIG8sOoO5EZC3nl4GWYVxjoFWbz-oINRTSfED4u9WQaqhIaXQ_aAGWRD7apQPzAV1UW-CgAaTy9IiwRna7gmoIr7mJfOI_uUjEYAcpOTjYjb8jBlbT2H1t-gJkCleqyss7t1b-45eOKrgyzsHm6p2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=iE9rKwjuRETYH-n82G1fcMKRbkGCSPf1wVSvHdZtDxGhtSKZLV0KWKGSlw0GxI00zNRobhilEucybhY6Qua9CIxPbrFyTppycd1CV6T2ZVXCf8LKd3W3vF9BxoAIzGeDcKEzDhMQOmUlguR4eT7vIbptSZJ9Sgy90HOUxWOvpcwwXKf4u0SeSJQ-aj44AIPUIG8sOoO5EZC3nl4GWYVxjoFWbz-oINRTSfED4u9WQaqhIaXQ_aAGWRD7apQPzAV1UW-CgAaTy9IiwRna7gmoIr7mJfOI_uUjEYAcpOTjYjb8jBlbT2H1t-gJkCleqyss7t1b-45eOKrgyzsHm6p2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd7svgC-d8eTxJJSbsyroMA-b0O3O2fL9j15yFeaoWpgSgNt_tHXEShNStGl42W6jZPg24tyU4C65vU4MdsKGsdqEZ6ggDYxaSRcJj7XU_hWk-IWaHymGNgzMeP4BRJwTl1Wt3nAmcO_BwzbkARfblBYuRvsM-LKI4V-kHmFnyNSa92EmttdJZLH9dZ-kkvRaYcDllUfo6RDj5IWyKR8Akaw7mxOzT3WKpU8gIO8OWkcLCOk-wR1OlGTKZPFfsPcn35PLsIMeRo9XMmk5__jOyyiRDOTWQO35mUppTxyksKkfiPAxShqbkWDQ56yAS7YUvBGt5IgnuPsNJcl9tSa0A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=vDP2Oyu_4otwv3OlU0U32yDNwiq4pBWiK6e9vdq-EDnwv5xihLLSns6p6PwWILz39NTv8YsTk2fzFQ2MjRVdsPmerEcQsreMRLX91AjG06ZawhFFehUmloyjSaXTRSC3UKg5gEWAOB2RFalpM7zXxIlem4cdPT2Y05nRUq11sWWVbcev6F-uOD9ZkEVeg6woX5Q-E65AoLAdeC_WIlR5E5hPalXffY4_BY4OAJx9O2LOwNlaRjcoZ14G6a5PPFISofR4uBfQZJWuxOOj_9__pvrqDaBvPQIPQnZVF9hlRl1kHX3q3nDoG73p1xOjyzyoD-o3w5dBzlWCLE2Cc3z-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=vDP2Oyu_4otwv3OlU0U32yDNwiq4pBWiK6e9vdq-EDnwv5xihLLSns6p6PwWILz39NTv8YsTk2fzFQ2MjRVdsPmerEcQsreMRLX91AjG06ZawhFFehUmloyjSaXTRSC3UKg5gEWAOB2RFalpM7zXxIlem4cdPT2Y05nRUq11sWWVbcev6F-uOD9ZkEVeg6woX5Q-E65AoLAdeC_WIlR5E5hPalXffY4_BY4OAJx9O2LOwNlaRjcoZ14G6a5PPFISofR4uBfQZJWuxOOj_9__pvrqDaBvPQIPQnZVF9hlRl1kHX3q3nDoG73p1xOjyzyoD-o3w5dBzlWCLE2Cc3z-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFju8gDrz21EkgV3ZvUdsdR2MR--xUEvPGpTOhnt-Ngy4I3-y53EwwUuVpVX7D2Cz2HY7iuQ6yr-ZUCrsccm9N0jW9ovCbIm94I8dOswVKSgF_o0SL9zE2GQmYFmI7xQB2FY6YNY8tkVMEC_SSg9IP3XoHsdHMNuHwVe5fLKCY7PdCk6vB-avMyuHQcBTcgUFu-P3OM3ESq5Yp9KifBfp9gOM8b7vw9bJ5okiM8oIA3F6VhQsxuibgLShsIv7EOQi3cMyCRwuBHmDcApnjgscThDfhrhY8iGmdP_0MNGVCka6VQ6vYNVgdu1wyejDVGSAT0k1WAxVR03ejO1VvXMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GotQQIzPspeQ-LoFk2Xh4vnEcNHF0FOGTXDUQGfV8DiBei1moh0tUzXdhwvCAZ3cSQTuMxkJe--xanCnG_bOwGS8ePD6tkPKo75XNJuJ8rvN3jEcfHEPndGDp3ZyUoUs0iTkHk4hZz-n2Mn6bXEc52qfAGO3J5RGe7Jp0NkevPc3pLuEedHUAvmYsZtIyNqjMTZFjtngsZDUCaDXDKnxZjMSQynBXUVE3rBYWMfYTrx6kRJuqUcBrddCeI5VMc9JBSCWFcpt29vdin_feUKx2fNkimihXYdiDTLTXWowNtU9rOKmoqLwGzxFIHBpF9ADHK57pYM7zU2Qi77vWVYtjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=ZO5-iZ1zZIAHXtYQmkaX0l5XqgyuxZzY9LiDjxBb-g8mmIZJjQGll_7FEEm3_43dNXwNlYeajQiQxLh2qx5HDEL2olvfRNOlSZZDA9HWZ_BwG4nn60jxUgfkx3iEgkXXs-HTwYTRr9m_WzHdk_iWY8_JHSyvRFiLZp-rLyrppgC2EAZZO7f_idaRviHE8CKVcIQN4HFkScTPhpslmC5VUTvBmIMjM7884jfhF7y_DxpjbgOO7reChONl-U_lBXRRFTLgzy4CFeicXGXKNXlh17FkcXHMiPsRDKkCYpjZ4k9WLq8lN4C4Rw_z08P9xOWQiyOZ1dJqvEpaKiiWFMFNJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=ZO5-iZ1zZIAHXtYQmkaX0l5XqgyuxZzY9LiDjxBb-g8mmIZJjQGll_7FEEm3_43dNXwNlYeajQiQxLh2qx5HDEL2olvfRNOlSZZDA9HWZ_BwG4nn60jxUgfkx3iEgkXXs-HTwYTRr9m_WzHdk_iWY8_JHSyvRFiLZp-rLyrppgC2EAZZO7f_idaRviHE8CKVcIQN4HFkScTPhpslmC5VUTvBmIMjM7884jfhF7y_DxpjbgOO7reChONl-U_lBXRRFTLgzy4CFeicXGXKNXlh17FkcXHMiPsRDKkCYpjZ4k9WLq8lN4C4Rw_z08P9xOWQiyOZ1dJqvEpaKiiWFMFNJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9nFpaYcnaQnpQ2F20a4V6q9ls62T1A4OUD0xU6Jal0Y4b8gOVGvQfNlCobwX4v8zA-nx64-7qzdhIIUI1WmHT7Wilq9sYlF4cJhnR_sS0mOpT7NRsnbEm3ByyDq-rnsCwclOrZxBFw93p64QZYPv0xlY7GY2aSjH5WBeaRXDwiLslXOMRs1g_lUUYlZUI8eeabbGHQ53QW71hzi_OGTwEPp96zk7Kt1TCXmmwWTRtgN7gMO8_656fIfoKVUdOY1IkZSqjluNOm_qaXpciQ3NW-EUlufKXmw9GxBgbDFsgEVDi2aoU5bggzV4aH2cFRiSfedMzjPzDGVOTy_MNyzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMa6hHgIup3UvYeNbGz0FvjgqAOJEtiK-S0h9KsGnmtkoYzyEncbj2Ybcx3y0zzJZ-i6GKz4oAAoyf_kKU14YM7u6RPiUTqTTSCZwV8XlyLLjqSIk37a4e5sVh1oPKRjshJF9Gyw-v_WZdLSGvtep-95mL22KVqIf_uAwB6ausYDRlJkaITi_0OQDEE01KBnNcgkbyrVXIoyb37zlk_9NxFX7WeTbo-KvWnOHFC1YTNzA8ZlCfetJe7tQ_goCRPUf8FSa-JdfS4CWJPB8q14qLJJ6rhhaVfPd2Gj5bnu2uNcoXI49tK-PVS3pzdNL32ckRt2f84CTMIRMB1JQToVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q83kG3xCiIdM4m8rgA317VmZlgrPKHB_Kk8nHbwxT2JD_REJP0HN0IKm1SNWfsPM_wOlf4f4-Fij1hvt3MWCaMVwz1zyp0R66duWxvgvDoqKCbj-G8rl5Bo3dbo6pBQslwrz9re0eXB5v-ctJDePhgRpSLZPHBgF5LxdDsX5kONCfA2pK33e3ffy9aEUVnn7PqpNzJA9x85q4jNWJzanQgE_lBIEY7d1MsScC6I9L_gknw0Djefd34Pe-H9UgF7KpsH2IbRYsvBBF9vG5wzp_efaB_I4uTWhyd497-tsjLX8PsUUwin33-im73AQl0-Fx24sXOgv0Oxbi-UVEV4vlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRrPxaSjoahEuDSQgPmOEuheRNZgUtMRgy-J76-nZfU__ld3GP-xOYU73Clf5Hwilktxx7NdtYkWbwysn9Hs9hAVV_I_eQ7p9IicU7xy_5QM-1E7G9gFzgWIWJxpqGYVAQXViznpBdOCcMZhOrO0SFUMyvB4Q2EIWS1YRHEoPi0SBEi2tMKx6gNiqDtnNOaLwqBaDlLcm1vwt24dPa-b2rrQxztLKAPJbAijTezKvFj6TnSX_15c0TFhcEqlr122xRA4rA8W5SMdVwV1dZddWDilTpkjbwtGAYOwIAFPljm23LK-y4gx1nhNjyHLZbPSjeP5u6m5L84EJm6kg5I0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnEFmeBAex8Qr0Ik0pcvobVHmNELLqMzbSJbUBz8wOwWBv02g7vIcJYNsmO73hoNWCXbGC2IESEP2rf6883cPwCxlBmhmyawEXkcy1PDepjVgoyO15v-rRPKS1B9FO2WbhyrO4E9v4_mi0K79QtRDwsYIAuAXcDLygmV_VQ9P2yIhSM9swLLkH8oAayqv9XinndKWVXKsQNCLQQWq3uarhY5xRIKuZMABtMKD1v8oSsSUzlPHYHvYPoHWWXaSKdTqMLnUnLwJR43qGyDhyRNJxaJgSiXu3LKb9Fy3GTzT4tm0PnW5aLaW3hQoJN5enRZfu8ium7vAgjWFmKstzNGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cTJHWpQLCLCrWcFnMG4kGECoJTfdi_Su9y6rZpQJ0R9202OKrQqlc6ZI0Zd75jvWOBBBaakAUk7t11y1EA7_tkWPo-GKt75vpcVda0qZVl2JyIFIesYCnWlWmD9CCtRk_z6NZDrXODLsie1QqJoOiUa84vjyC3EtNTqYxuoRY9-W6Iy_iggvKtKiTH9wLNr4nmbWsPQg7Z92uZeRw5M7oJlY77s9zwQs_NzCiv__qf316H7bgobVa8UU4peTCQMc492sNTefxB0h71PzxJTHCYQdWhWlwac-JIWLNDvaG43v2kLRxkkHKZSAvFaxB5IRwQ2NJuLg2ZZa_qVjv0yyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cTJHWpQLCLCrWcFnMG4kGECoJTfdi_Su9y6rZpQJ0R9202OKrQqlc6ZI0Zd75jvWOBBBaakAUk7t11y1EA7_tkWPo-GKt75vpcVda0qZVl2JyIFIesYCnWlWmD9CCtRk_z6NZDrXODLsie1QqJoOiUa84vjyC3EtNTqYxuoRY9-W6Iy_iggvKtKiTH9wLNr4nmbWsPQg7Z92uZeRw5M7oJlY77s9zwQs_NzCiv__qf316H7bgobVa8UU4peTCQMc492sNTefxB0h71PzxJTHCYQdWhWlwac-JIWLNDvaG43v2kLRxkkHKZSAvFaxB5IRwQ2NJuLg2ZZa_qVjv0yyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=b8Zp9MmuSEoMRP_NvWXitvy8EhJsC9sA8I3xRR1-4bMYPiY-F6saAhYpaw7wBJwtdgSLR0ngOKdyhT8POoYNpjNvIi2O3xoDfFj5EB1nfPRfcF3uqpknu_TVtp2Qe69DZ0qeJhne3O0suVhffg2z8IfhSOqGZ04FGaP10SFS244KJc-JiFG1d6J7t3Dbo3CAMrbAfKzQGNKelEveAClQyzGDEwpK0TV3gfDLzjsIq0ad0IrH8YIizMYtH5PjKDIf5_-qxdTog12ajNL-e6VhnjGHIH7O2xsmh6SwcOLJbHiosdVST_honlPuLrGdkVckgjrnbyzShHMchKWUZLAapQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=b8Zp9MmuSEoMRP_NvWXitvy8EhJsC9sA8I3xRR1-4bMYPiY-F6saAhYpaw7wBJwtdgSLR0ngOKdyhT8POoYNpjNvIi2O3xoDfFj5EB1nfPRfcF3uqpknu_TVtp2Qe69DZ0qeJhne3O0suVhffg2z8IfhSOqGZ04FGaP10SFS244KJc-JiFG1d6J7t3Dbo3CAMrbAfKzQGNKelEveAClQyzGDEwpK0TV3gfDLzjsIq0ad0IrH8YIizMYtH5PjKDIf5_-qxdTog12ajNL-e6VhnjGHIH7O2xsmh6SwcOLJbHiosdVST_honlPuLrGdkVckgjrnbyzShHMchKWUZLAapQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Jn72FXQRpysRt1IKB4185thmrf-OAoFaO_nNRkPl_bfm9CLNVQBqdYCTm5B2rZhNhX9_A2UBuEobna3iI00UfMMab2QEtuTjl-6IorW3kRHS9JdBV0RUEM0mASzX2ww8mqxzLKpoELBVNSaiOlNu0efhD6MkrgQfymgTlYSe9NObyHMx-YUjVSze7PZr77UIzS_N_Puq3PvFz_ns28Blx4j5YP1sRJqzqT5I0bJEEbow8myN67YIsFNRTluCARKzDjHSpR3IjRORxai0AAR0u-nzl8XwoU3QhHS9nflpOKjNajUwtwjzfy5PQN3M6QMr58EKUa1C_a8RozEWaDXY5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Jn72FXQRpysRt1IKB4185thmrf-OAoFaO_nNRkPl_bfm9CLNVQBqdYCTm5B2rZhNhX9_A2UBuEobna3iI00UfMMab2QEtuTjl-6IorW3kRHS9JdBV0RUEM0mASzX2ww8mqxzLKpoELBVNSaiOlNu0efhD6MkrgQfymgTlYSe9NObyHMx-YUjVSze7PZr77UIzS_N_Puq3PvFz_ns28Blx4j5YP1sRJqzqT5I0bJEEbow8myN67YIsFNRTluCARKzDjHSpR3IjRORxai0AAR0u-nzl8XwoU3QhHS9nflpOKjNajUwtwjzfy5PQN3M6QMr58EKUa1C_a8RozEWaDXY5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=FTWsJ9Oqb3_OrfUD1yTGfew08TLtSDG5NSdZHjYuBCdTVRxNuFSTYOTjpn5fAeHz9F8a43XlRj2A3mMVIiKWxhwLb32SrM0o7Oz4cHAfxUcV3GpVWZvHL7LTRWm-7UV-1YcYo14FwmUCMMTwrrk4LX3Xov4cDXaOaUCxmE6zkwpUNtJ9OMV4a2mmWMT2n-qTHsEnj2VIGFpbvUJR8lwJzwV-swg2TePYOOXJrz7LVNqDDn71HynUwBBF9ggZ1ZKT2CJTJiZWvJcOR5xUztk47nY0JyB-yZYNQKbv3megMwUppN4LIumZ160BRU6Fi9IoT6vehii_VBhDcIfKbIG-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=FTWsJ9Oqb3_OrfUD1yTGfew08TLtSDG5NSdZHjYuBCdTVRxNuFSTYOTjpn5fAeHz9F8a43XlRj2A3mMVIiKWxhwLb32SrM0o7Oz4cHAfxUcV3GpVWZvHL7LTRWm-7UV-1YcYo14FwmUCMMTwrrk4LX3Xov4cDXaOaUCxmE6zkwpUNtJ9OMV4a2mmWMT2n-qTHsEnj2VIGFpbvUJR8lwJzwV-swg2TePYOOXJrz7LVNqDDn71HynUwBBF9ggZ1ZKT2CJTJiZWvJcOR5xUztk47nY0JyB-yZYNQKbv3megMwUppN4LIumZ160BRU6Fi9IoT6vehii_VBhDcIfKbIG-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4lF4AXyDs5Akznm8h_n5yUmtEp5kYYJAe0rlU2mlGTMqWWKS9IiroMPhLFJHS6Gq1rs8MVkksUmKeWxTeHF6joaIVMqAjZmhvRup-jiwXgjG1Hy5Jy50ay6M-AKmOilxzoKkYI-XfGK0oblOi2b__jKfjvv__H_5eM0XdoFaMlXkiJDYws7uKpi90eNsR_mpaqrTq9ZbAWxxKDFM3314qwFr-TvObHjCnM_-YGYWesVFo4IrKWBoWOzt6G0oCoBayQJLfp0e9I0rH4PknDty57Daz1c1ZA2GTWhulAxW60Ipo5Xd9SoEfgrsgfAETNcuID16ltKxHXfZKW9GXXhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fu7hV0vWR5MXsqe50NbsyL56K7lrcKsO1u9MShmUPO0MOWjP61gYnAKZsvfiuaAJoEpMYCSh8k2-GaGn1IlX88ZtVm-lHgcHAHg29wFv7jdsNUYCGshWAQhMIUE52ggdwblMev_H-1tjEo9YIFx98xby9hS3fk1i4kqJeaGAZERkVOzqJcJzHmCrC3PDrboyWARSlxnTdJJkzw4diGMwVeLCke2ee8Xs-TbUTlAgseokIPnxb0gCKKIDwg3023YQ41nzD7I-kjujfhZXiaGICwhL-nxwpBDEuDCVvdLUx58agoGSIPy9bXG7FTtFTnIr3P6R9X5boonL-goqJMRbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tWGoFq3vFtILFyj3KspTVMCSgHXJZ5JH9wKSzkuUpy-P50l1tHDMG2f2VMcx1I_eQEG-kOaVhtZJmraxoWhWBD966uuKeHjXkey-FtZCodVUDWmnd0zX_8cD3sBt9g0LFDC29jPUnNUYSdOMUIhf6eTi-0hpr0hhNLEe4fb-9Cpl3G8JjpZ1ehjjo8OlOaf3qzha72XbWPOBwApobqwEifaQddcHuN1P3QwCP2vfeVWiz5DfYlKpMa6J3TW7RwLZBiujb2jd4FKISiI-InH_esOmLMmaejuQ8PgJ6WPJ0n0i03uHeSObU5qjJkRMfjIdnxIqqAbE-Qs2fgMVt10gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=tWGoFq3vFtILFyj3KspTVMCSgHXJZ5JH9wKSzkuUpy-P50l1tHDMG2f2VMcx1I_eQEG-kOaVhtZJmraxoWhWBD966uuKeHjXkey-FtZCodVUDWmnd0zX_8cD3sBt9g0LFDC29jPUnNUYSdOMUIhf6eTi-0hpr0hhNLEe4fb-9Cpl3G8JjpZ1ehjjo8OlOaf3qzha72XbWPOBwApobqwEifaQddcHuN1P3QwCP2vfeVWiz5DfYlKpMa6J3TW7RwLZBiujb2jd4FKISiI-InH_esOmLMmaejuQ8PgJ6WPJ0n0i03uHeSObU5qjJkRMfjIdnxIqqAbE-Qs2fgMVt10gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ssi45dULGFczuy963Cnv5Exv-aVexqJNWUw-b1Cc0_PxR-ubLCjzWYg_DHbQZf-ljWkqdWbYFjOWN6Zo8h_APJjCqLZedwL8mZYfqJzJRJMJBeFOWbulEb7ut-gp-cdrrsv_mdXwkrbTHn6ZzhocmVAQMIfEXqsCV3xUPLTFckGM_TgKCUA5agka4tuemppZYmxzPt2KTF2etiHj1bwBmx4oQEzv4wkg3wWx82P9Myw9d-8sZZjlrnRrICMRT5Kc34dveBvWe4NRUSiRR3i8P43F2SX09VcJO8bWD9JU79x-VRE62VDlGx9hCc5wsXhCCiW-eah9VVWWpUZCB9gYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=cHMTmvGmqp4lBtdO_hjJZtj_A0okJCsCEWMMTTg3adwwqoHSsHBc2I7rctrGAUWMAtlwZH9pY5Sl5xxe_c-lZXHBXs73fUWbNme0pW8ZKPfgSgpAN1zLWBk7kM7nzE8hQ0y-9U287o_eHiTQO0rAJJQIUsaJYcbQZeRGcR7lv6SeCxFcLZlnk4kRHo64SbOKCf079CgdVsupG619FYpeFmmmnMis6IGKZr-g0E8lGcMvR1HE2Q3VV9NZTai0IDX7CmzZURIHYoSjV_rSjYZluTEuHHO4WOo0MEmUSe5MEXrPChK58Bqm4tS-KLSgQj6P--WNfnyHiSTLmm2Vt1jJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=cHMTmvGmqp4lBtdO_hjJZtj_A0okJCsCEWMMTTg3adwwqoHSsHBc2I7rctrGAUWMAtlwZH9pY5Sl5xxe_c-lZXHBXs73fUWbNme0pW8ZKPfgSgpAN1zLWBk7kM7nzE8hQ0y-9U287o_eHiTQO0rAJJQIUsaJYcbQZeRGcR7lv6SeCxFcLZlnk4kRHo64SbOKCf079CgdVsupG619FYpeFmmmnMis6IGKZr-g0E8lGcMvR1HE2Q3VV9NZTai0IDX7CmzZURIHYoSjV_rSjYZluTEuHHO4WOo0MEmUSe5MEXrPChK58Bqm4tS-KLSgQj6P--WNfnyHiSTLmm2Vt1jJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUWAlL8ZAXabvgZJnGDTVXw9lHTKyKA5g83CrsTUuFVpT1VshiAGQmpMDShlKib7ytfB9tSUevOyoPGeQ8RZC-92ehS39QGkMaX3RW67Ckry0zzMswlfxzMGNWyLGbNaSB1lwsOBWXR2YS1q_FI1jbHKbVEN_PwY9vzv3AAKeERBdttHZyFPWkrxGpDv-7irR8ySIfRgw43bouSl-uTkRZ4R4II1jYvR91mQECXnZ8NdIgG9qR6hAbo-a8c7W4VRJtIk6waiDu7Z_Vwo7ZmB6ZHEaVQGdTJnmHh2rPRQPRjE-P3YK9xIXkuO7NKO5SGA-NhrBHHiXwassnfH335VXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHhWx5xBoSDRNg3SArJBm6AzSTZN2itbVHzCnJwOx93FgaoIkxxpwVPpBvtNrGFgCpRIqwKJEtMOLONwXlDnjOI2-FXUVXM80OYQut2FCMbI6NkV_6OMRwOekU-bHBHnT4pqEPxtGl4bhvbS5KKtJr2XUswg_LnkviBpw8wqH6lS15zSKYkC3wiF2g26bU3-2vKrPnnozk_0VH3S4gFo01nBZv7KLsTSVc7JGC9US6VFM2eEYzVSrGBD9_mJ4jQE05cm0_jfi3Tl-9a-xSYjZa7FNVk-f_9nxbIix7VUWQyVhsBQWxFMpYoGMYtmJuc6G_Y32fS_21vafgVc8RDEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=NSxaA6LTjen_3zrWatTsxR83_djchwMzDeAq9kPUrAJUlze6NC17MmekrvlhCVAeLMh_IXSGyvfVDNdZjagrlB9GOt122FpyW9ZLoBZOIC1plD9avX6h74zs19kHOqFeJnYbjLVajS0mbB-PTigrA4clbbpA4-8fh1LAYRD0y4j1mVUnyXHnTq77DKU-qoH3crQutBYw0AbaoTr8iJt1qJi2p2Nw4iCIeTkNzcK5xv75qDiAQNhwxgtFGGHBboL_jgskLHz8NtdkWVZaUj6lJ9L0o4KcxZcRrNoG0hCXLZSQ4v4uPM0bLclfVUmRGGzuOiebU09JuH9UeCZgxkDlhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=NSxaA6LTjen_3zrWatTsxR83_djchwMzDeAq9kPUrAJUlze6NC17MmekrvlhCVAeLMh_IXSGyvfVDNdZjagrlB9GOt122FpyW9ZLoBZOIC1plD9avX6h74zs19kHOqFeJnYbjLVajS0mbB-PTigrA4clbbpA4-8fh1LAYRD0y4j1mVUnyXHnTq77DKU-qoH3crQutBYw0AbaoTr8iJt1qJi2p2Nw4iCIeTkNzcK5xv75qDiAQNhwxgtFGGHBboL_jgskLHz8NtdkWVZaUj6lJ9L0o4KcxZcRrNoG0hCXLZSQ4v4uPM0bLclfVUmRGGzuOiebU09JuH9UeCZgxkDlhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=RS_TEkhqE9FqvQpNvPXxH6bbpy-ERqSo-_JleQr4rtPB5D2abZKslkSTFdyBJecjkAX89dhTX3DuFzwg4kOfHcKdrEg7w2lM0P5Mbe7AnHTjYlZ_XKrJw1ISDLaxz-Qi628Pg2TiVCsxWHTQjlqIVewE6npZmXgfvxkd_JdtWBMKl7RaQ7p-whSgTXm77pHRZY2rpZbAbu2mOqXGAxQHQ0L81wlCjRIbPUwqvLzgwBDBbDcfEC_1VVUfxb6-S12XMBUNeHcu03IzEixFsqmMNIfjkN-EvvH0uwhYoNkbbVfyPMv3SXtcVwKBuh626RLQAWnY3w2v5TxgXGzFDLEH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=RS_TEkhqE9FqvQpNvPXxH6bbpy-ERqSo-_JleQr4rtPB5D2abZKslkSTFdyBJecjkAX89dhTX3DuFzwg4kOfHcKdrEg7w2lM0P5Mbe7AnHTjYlZ_XKrJw1ISDLaxz-Qi628Pg2TiVCsxWHTQjlqIVewE6npZmXgfvxkd_JdtWBMKl7RaQ7p-whSgTXm77pHRZY2rpZbAbu2mOqXGAxQHQ0L81wlCjRIbPUwqvLzgwBDBbDcfEC_1VVUfxb6-S12XMBUNeHcu03IzEixFsqmMNIfjkN-EvvH0uwhYoNkbbVfyPMv3SXtcVwKBuh626RLQAWnY3w2v5TxgXGzFDLEH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ScZ_6ttaEEmuNeImi0pXIj4yXGkSTsTkhdV6fAuvbiLU3ClERATk8u1k7KxcxiM8al6ElwoZLuPoMmN98RSWcxZOT2XsZWwwQHEwsCcj69RS43uFjG_0at532YHPwdWoL80qBs8BOZpdVFggEgWxr_rTYoZmIM9wdzPGYbTZGzaoMXwuYORwVUy4QuQH00YjrjrJ_WA3aq5HS2yzKluz-mvlyhgOrG8kKmRhrQtBmqcuFSdX1zKrdTn76pKNNhxKXjP39vAy3huJi89rv_uelV_CZMFk3SJh_K6krs7No5RupzeJflQzscWJl_TS5-16kaJiJEY4h8y97aPM-I3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmRVkUHgys38quvGYIBpoNqQcpK5UHiVul5_os0gD73W5jzDoIXAy_7HsryI-oOU2Ji1pBzfPVDY6iHHwPEFeBwzAKwfV6aMbdKTn5V4hvtgE4b2uEasMBtjGrNdCsjU74S3riOuSR767GbhCr4zA8oZD1vBAd8tqUTL9LzT8jVW0XbtVGUX_nQee7NtPpbhhb3Ql4CyfZJiiEfYbxX7AKQwEDJ1x6qxngl2gwLIV0z9X-Rqcr2bqi9UVnK-x_t5WY10D75UIHPVVR2UaA_yvDe4n34_WcO3nNvF_j-c2cOoJyMheUu6v47aax4QfTzo1yzQWHsfnEkncnnatuOBWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFfVptLBw2WEBu78i2Q1U165RCrg3EV388_Cir4-1jrf4e-ya3LNpKwIhRfKxnhEhPB4lblLZRqkM7uHd-bFjdxrzIO6faFRHyad2FRnZAAJemwkeK8WwQ5M3oX8_kMwwwfZykPbW1MId0LFff9xnk3V6ieh8ZhThvDKA-9sKIeBvmQMnWDNc-YQrCSggMV0sFgjCk0hKLGsam30KcY1mTpYF7jTK2XlvdA6UG5fUyXwPjHC7_AIcUvCe7Am15W1y8XolhGsho3ZykVS6cQIxiBQ28YXtClt7YSuOThYpN8VBsg40c7xTurxYayNK_L8HPBpV0jCP-MpxvmpF8m8XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=VQI6cEqcW1VXaUg1iJIvJr49TlFmtcSN5ZQ0uLQdynbpoKB-uiXqIQ_O65Qb_aGgXLFM4ZAKPdl3b17Qagzda1T3VDmVlt8Ro0Zj6rZSoLqkT6u9e4sGzXr1SmckRzQzBZZAFEOCCix9TDO4JshfC6Bo5ka0WymMuaLKwwr930t6Pwu9bRj1mLBSKYoQ5yohM9vC3sOhuyMrdLEcsiNpUGTWHQ5o5Kp34ly3qKvIpZoZ4RHlLi6vCYHcs7ZDkuVwnp2b771DfRTtIFLT6D4x1IglgC16fBt0iTOblYh38FleoHMFnBU_Vcd_2a8n_rZtuCiKvbALgxOZASCFE6sDow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=VQI6cEqcW1VXaUg1iJIvJr49TlFmtcSN5ZQ0uLQdynbpoKB-uiXqIQ_O65Qb_aGgXLFM4ZAKPdl3b17Qagzda1T3VDmVlt8Ro0Zj6rZSoLqkT6u9e4sGzXr1SmckRzQzBZZAFEOCCix9TDO4JshfC6Bo5ka0WymMuaLKwwr930t6Pwu9bRj1mLBSKYoQ5yohM9vC3sOhuyMrdLEcsiNpUGTWHQ5o5Kp34ly3qKvIpZoZ4RHlLi6vCYHcs7ZDkuVwnp2b771DfRTtIFLT6D4x1IglgC16fBt0iTOblYh38FleoHMFnBU_Vcd_2a8n_rZtuCiKvbALgxOZASCFE6sDow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4YgSNj6QgAzXB7uQHeAuTAEjLtIX-9rn60qdtaeGDtTG9DGZ2zoDuzCS_Q7yrHvfGp4tzQZHKJUTJJAUo7x6fn3ZNH10E-e5HCJNySOVE7v8t1HVuV6fj-mOBysFCck9x7Sb5o6r6WSNYwTot9Y1KVVobFp-go3xPNVmOEpbGcwCZnA6wdVfSTSJ6bnroBV4lSaq0iZjhkPKdpwS4-KVhsqMubKjjYecn7RuPnZGGoVofBSJPjKCGYIOAXBo7gFSimSivh6yVEkIzUyBdyjs0f8alUO7IsPfM3F0a8-Uw_YZwJ1vhoSX4FHqUYuARn8vFu-uffQEWW2-9qvgJIvag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt5WkdGJfZxYFiAsZudfZceESv4Ak_o9s5_C50eedWLEWbPRUiKGoX2YHVuQlcy52-hoTC3aJIx5VoUW-tT5sSfGvXhVDXSHVFXEbm8c3pUWMbm5Zj36A6NAZq9MVH7Y9r0iMPiksAemRg162JOhk8ZLJveQDKJkWWHwABUdRWVGWI9ADRrJ9hW-29p_zWrDbl4six_A-Yz0_9CQzuZGRHXSPif1-rPzqk-iUqEWLeHPEfg1-cAE0HdSr2w0DmsAqKOSwxNpx6Q4O0jFG3WJ199ysv813h_AGKzN4rtPiW_EgECshW2gkzWF7_T6Rb9UuD4pKDoHqLmnkfbrW8WjMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcHytB0iaaoC3bAowDF06KGttVKnVMGibIPmffotArwyZcFITG4vuDPMWhCI1xCiwbVA28IF8BvdjRBTWdZedldwQ5Au2bRcZyedMxFrPkGS-Qw7AC-Gbxg81dJCBrDmrpwGSHYf9RqEqR5fKcsvSfcX6-gRSNQRih1FyaWyAzM9xiDMQERzRYmjWhxBRXnMGi2QAmDRHJDiX-JNvZxnQKLk21by5nVVbsX39v0--k1wbvovGf0uxF7WF9pZZ6GbbbhCUu5d2ld81Z8o79sV7dKMzDqqDb1qoO9-hr3Xf7RqIvyoEtGuC-GcY7AVNZgz8HuG52Q1x0CIXVgSkSy_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvZXkzwx9gMMF128bzIjP7NSbXkbkHsRPOYTNYYqHmAJhYqeH6nYzkMZQ2K-r9MrRSKeIIzVTebkJqnw1hN4xiFarMeqi9FEhwBO5zwiyUd1eOzYs11gIR5_jfWQMlt5fqqWXESJ3mxcVIJSq5rkaVDfwEO8s-2K6qig2FPcerTaTOsiOJTUU8AZcRaYfhILgl6s9s2WHIoQQFLMmkKaPOphOCJvqZZe0UMfaTknJui-QSY8hF-AKyNEZXbFMQo-B1Yvacwer-DVyws4A6yeZAd0F9GmSjXDUNzci7Txr5vPs9gmEj65Pi9G6EqDpjrByz_aDlBKfCbCw5qVOkRuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=u_2F3Sp2NKmzzx0R-pJCTdlU_xAm69T4C1rqfrJ2heztSNEo52kNT5daOcaifMA12_F31Fm9jtEcL7Yisss6T40aSDYWBGbv0fwGRuTNy8BT0MYPg4gk8gSQP0v5odOMKLIRaHINhmWjL3OjB_u2eCL3lJmV11JhN64cOQZK_rQda8s2pKSLJbx23ETBph3Szl8RVRQ-8AuLwx0Qbzq6RT9sX-Lc20SP9ilWnzS8SlTmfBPlRBytaL00EDA_5_O3g-Nw4Oc17ZsAdVYSM_LQkTGi94kHHmujCECI09GWTxDhOdkR7vB8nlzY-D0ccFe5Al1oajugB4ECOCv09Y-dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=u_2F3Sp2NKmzzx0R-pJCTdlU_xAm69T4C1rqfrJ2heztSNEo52kNT5daOcaifMA12_F31Fm9jtEcL7Yisss6T40aSDYWBGbv0fwGRuTNy8BT0MYPg4gk8gSQP0v5odOMKLIRaHINhmWjL3OjB_u2eCL3lJmV11JhN64cOQZK_rQda8s2pKSLJbx23ETBph3Szl8RVRQ-8AuLwx0Qbzq6RT9sX-Lc20SP9ilWnzS8SlTmfBPlRBytaL00EDA_5_O3g-Nw4Oc17ZsAdVYSM_LQkTGi94kHHmujCECI09GWTxDhOdkR7vB8nlzY-D0ccFe5Al1oajugB4ECOCv09Y-dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDspacRmh3XYUdQFSQFH4Gxwy5S1bjbSpKiOiWXNSyUrcFcacaZeEfDRV-0kC1fAy16mQvX5TN0azP2S2eZ3uIcOQQnniAOWjq2-5pAQ8_0q2FtD2RclMQZMxEyuK_XFFLrhAXScYI9Er5tZOhO5EHVtoB4xb8pJ4vOUr0HtJEPjacO6fYXjRCRUEZg0A2GDndJ3yveE-HhCnCcj2GVPMDeVbCxPJlp-S_OLu4gdiyqACmhhixJnIwRy-f3Wm6_dZwNDb15SFKAfP4skRaYtTX2B-Zwy-E9SzvBKLlmXiLaHpAV46LHpurf9DEfnFzfHvVkz99hPSpjnQnh11M11oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=cuxc3ub_bnuRG9C5ck3mPKynfmc9zhDTNNfiEzU6QaIP5_gAfXSPDREbvah69TWxJf2FTFkBiCWdlpZ4R3xqILdw5bo3TjMl3kTsZMbc8k4SFeoXeowND6zpksyVIUHkXlzwFSPy1JQrAyeWcRpKRliAIB1l05moccH7YTEal_fd5W1qH3L45g0qgQszZ9Uy3KJH-olaqAuPwbj4WAXQRJ-sAZ5dNOhmGp8_bRCUSLI1LpfvjH6dPK2hDhfCRyGynQyC_4pI6AgRXbkbWHw-7Sav5VTbq06BvRr1EbqYnryb2CHbjs8_SmIkKXnr2YglOMurH4HKQ3jxO13I5I-p5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=cuxc3ub_bnuRG9C5ck3mPKynfmc9zhDTNNfiEzU6QaIP5_gAfXSPDREbvah69TWxJf2FTFkBiCWdlpZ4R3xqILdw5bo3TjMl3kTsZMbc8k4SFeoXeowND6zpksyVIUHkXlzwFSPy1JQrAyeWcRpKRliAIB1l05moccH7YTEal_fd5W1qH3L45g0qgQszZ9Uy3KJH-olaqAuPwbj4WAXQRJ-sAZ5dNOhmGp8_bRCUSLI1LpfvjH6dPK2hDhfCRyGynQyC_4pI6AgRXbkbWHw-7Sav5VTbq06BvRr1EbqYnryb2CHbjs8_SmIkKXnr2YglOMurH4HKQ3jxO13I5I-p5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTwvP1Cd-JjddqSH4bV1U8TapRO04Ojx0jjSHqTAbak4M2BGVt3KDmSdDdwh6Zzh0bjhA_i3wcfgKZj8xyTcapLSMwP94B1MHC1jNL1E9dBVfQz6q8y94NRDaiV9TTD04BLJeBFSJVBKBPmoySgASUCDglOBLGZDXFN56KmTKCgOTSYnpyltflE_IlEgn5VefzLbT34xLFky6HHT4FdFXzPfWQlIeRxU8T79Oxt67N_XgI3N2JTo8UVZFO-iXaXoSJQL8oqDZSW-9tiCtCeDRb9IsbLNzBeIhhHLBOeUMdek79UTpq-NC0P2hnWgUcdbunoD0ohsCLjmb6dPKMljDw.jpg" alt="photo" loading="lazy"/></div>
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
