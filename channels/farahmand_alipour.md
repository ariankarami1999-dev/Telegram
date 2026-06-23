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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 03:38:14</div>
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
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzq-SJCeK5iUsRqrtzeIl9PiPEA8q3oSzYdnbVRLY80icvC_4LTQciHrnV9pRKte7WeyE-jBbb7S46Bhhx8Tuf25UUn-H8UrM2QSzbH9tgN7ATXL_hE8NlfaCv8jXLQ-QZlxogfOW5npf4VGrKBt4wovK8rC7H3y4Aak66zjJteOhkmZQGcBL0iyKnTau4tjoTyYssEh_wu5vzDhg_G47-vDe4dl1y58G3MUmn-zfxX0DCeTHV6yT4SSVYNg9lOZM0NYQxG1q3YwJpqAgiFwQ6A0qSXw5dtPjrVLT2DRu2pTeto4sAKY1rDdAdPhW5d20-XCq0zuWNuZ0o8rtW-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvabggeV_gp5uCRBhKTWs-Ue7yxOdq_rfaAOvs2UrdfEteqQjXhE79lev_iS3wcYrEYbbHceY38H5CKlIjE0ZQ5PByez3fvvNvENYL3xFw56HtNdE0H37mOJ_IG2wmtb4my_GBs7zEnlnky2Vx7RbB7Leir6DWzCQ-TsdYmtJZoFoDIuonUYYtxUs0bZV6xIXj-HQARCXDUVW87GtKVKrRm8L-bx5DDclgfLkpUV8g4i6ZCBxPTs46o22Gn9nO9CaIvMaJaBchZIOyuyYkC7xja0G_LV_lC6brjsU9XPuUSsOv2-Lka37BFRgz1MpvtqBo02kRp7vE9u5I2ZHdnvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkWDD8rY5G4nSdXYwW2TdbC0X93oyNnIstH5hwDH2iyhDhujGBIqXTR5dvrDHfL-1VY8eXjMxUgsCwIPnIm8pS-k0Ep-BPMRDrvRlCR9A6-wz68Q_L-TbBs9QIZbLCQ3EEC9g2LQKU-VbssvD2Wq7o2i8ynJqXx1m7A83swoqqK0tWd2augq-dLFWjH2OmGpTbvdljlCgh0E1iJKIZoSykjf3Sv6urKo88iH9asobAHH6kUKZWBD1EEcRqTWpjKBtAxRtydDRWlFfLApnE4l7xaFLFa_ux9TPAmMtN2tHmY0rIbobhpMzGU0EEP3ZnuVpoZeV1v_qOJONCxpVnzhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9tfr9ooPoEpSVExNRXoTSfCi99IMOf43EUTZkyDnZJ1VEqhOs4ICgESZC3HQ0v5oUWv7MdlQKkNGMO0ovUwgHlIRpGmcF4E8DlOqYXizKzp9UyL1Ygkf3yjSRwQzumloGU3INOSlD2aDlYdXgQ1MyuYPKyNGclZub7XjpYRsVmXGDMHOOK00dDUArt6W9XI-sTMlaMfIwR0skCWBi_ty4nU1L51Mcwyd2F9O0tfXn5Na28Sk41vDRl9s2ujcxhwgKqJl9q5uuG0dFXFerU69EqEkUMwPDNttQv27Ozi8P0huhI7tO8gDeBQthISpM7rZBz1DjDBNuj-8FGeVrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIY4IQfe_-jkn7hX0ZFA17nUWwMhxDDZ8t5qK1EbO3GuMi5nsJhgVS5PkAralxHLinuSLgFLoQ0qoTIsAns470aozIMKynerLLRoGDAdCvsIhbR8FeB8pU2cDHrUDjeX8Qn2nX1Y2B0U7Y33CCEULPlPSap5fCb_eCa3ezQOxJF4Jxrlc8tAEf3M99cEtnCyRyGP2WDYib8tG-Qx0vh8QJXSMmaBovXRSk2vURFQvh-Ca70ATLxUnjGvEmRMsakCEF7HksgHL1da3YfyYQkSx8khSl9BFf40p9ZOn5f98fQ0xWG1Eav2qpoLEb2IvTynju_zNSQiGFPOjZSe5lLGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG-3nx6yxTpDCHwinKjfFTp2Q9WQgQK1TbqoNsvYZempkPgGVtSm9NUydhQIv2WfA6RTk3E9KtBBpwMunMPBexng0NzlAvJIK-k3wELYR2GZUnuEXhW1wJznm3NPJsV7WiN4aAWbLgWJLaWVuJWyhHpResKBMzF6OZZgiUBPTCtjGEarLH5a5Bcb2h9N8fThUuasYJi6-9eDgw2bFdI0zLK-n_CQGLgbW4j7_9XM7y0lmQaGElfFF0j2gVkObFEa8MZPoxACCFYdQwvzMkl73EkdEtPMK50wYPV-Vk8bJ9mIk5kVAH2_zAvbzQTSRFQ8BsjyOtCRYEDNiZCfIHlh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=V07K7Hx80RK1FWX67dTfgmmSBbXArHzFOff4_ORk2ng-SlnmazCUasB7xJcdhOhMzqXOXMB-hj-pkuxTnMyQse1-UpBp0iLESCmTMH0kqQZNP8aHshTFFZ5ldlcoy31GUG4JwQbqYkoNJa88G7epPUnCFVc3GZJJaHUh51vntxS19fKMh7DzLjiCa0ZIfzB_PU2OubAphC0Qyz91wS0mdnYfj8eRumsulnF6bi8phDE__eVwUZZ6C1a0z9YXMZ-m24uzSQSFclNYC1E8anMZt7SwKTDDt5fzhoHccEMixbA0CjC9D6pslEoU9joUAvtR-_JuMU1NLqAw0AUVUkgHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=V07K7Hx80RK1FWX67dTfgmmSBbXArHzFOff4_ORk2ng-SlnmazCUasB7xJcdhOhMzqXOXMB-hj-pkuxTnMyQse1-UpBp0iLESCmTMH0kqQZNP8aHshTFFZ5ldlcoy31GUG4JwQbqYkoNJa88G7epPUnCFVc3GZJJaHUh51vntxS19fKMh7DzLjiCa0ZIfzB_PU2OubAphC0Qyz91wS0mdnYfj8eRumsulnF6bi8phDE__eVwUZZ6C1a0z9YXMZ-m24uzSQSFclNYC1E8anMZt7SwKTDDt5fzhoHccEMixbA0CjC9D6pslEoU9joUAvtR-_JuMU1NLqAw0AUVUkgHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcxMQagBtJQxZiP4VdeKNIsYJ5l0O0rM_iusNmUqUJnbFZuhPgd8FJZHT7-zDT09tq7yfx1vw8M_m3rBJb49SbjogN5Ph6s9yXBjWQXFWep8UeD8r0lIKmZliKQ8aW-Cjqvi5AQUu3WPKJ4YWXFg6wmGg20Z8qdBPTEp9__FPgwP1db2oT88LI_0htbHLrQ2RuRCb_z4GRMx5KPjUfkzWH16qWxIMAXsoglN6ewRsVyCHwkpy8wm0BWmvjNS-N0838GwsKmA_MTX-aVz95zjagor9GaT95xYyTRTH8RBaHHQhv_T1np5KKwOo7ECAGXavEy7hUjYYpSLcXc7pH2VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqWQQTntQ1BppWx9E4Br_1VL8PO9vnfrBqMQ4lUhr80IqWuQp5ByZeUwXoVU4s4A8Se0SRhm0nVi60fXCE3QVta18zOLnc1XIF3So0ATkGQsA-v2Ve3VqafI1H_clxEKPDHGGOeurRBzZQxeWGuiDWUgyeN65vXsVUPsa_3C_4We8O9kCa7UQHQ8b6ZrjIxKw2kFqkOxuzHOmsVKz_ngfE7fOeX_CfgYinpMkv6PLS_3r4J8AgLAS80h0kddQKi-IvXrcY2BAlB56ivf1RCdq8UkYiNoQ9lFN3dhv9TYJTrfRMW1XljU6f1i3k9g7rqlEn6EU6rDm3XMWGTSJHa_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVgquxKc9lmsKYhCNwUyCclQguYkw2H8ZXaN0lVkuV1fBIypoLfNaLhi0shPfUhuEbbf3cEy7HMT2FI_0HOql1mHmIyL57OemjWcyZ0Z5F3pPu6JSpBzDyhQIV5fLUokOp5o6Lg6UL6udAaATHmkSE6YB_H9zsCX3kjYuoTygq6xWhBZlkpYZF84F_9c1kPeC5SBtP8PuPT1h7P0uniqIxO-OzYN77AlNcmX3vosNz9r9fvnH0MBAH2-uuXAkTGpt6XvHVuRzLo9vxHks6BCUwh8K34OMzoPvIzfjcqF0y9GFRENDauHykYRJf0CqJbRn_1fcRyZHr2WE101QGpClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=CFqmJTsQ4Chbzw_utdgcD_FCAC-vAk3ggZrRO96tOiLYflbLjJ-hs7KKkkemxiw0xEOqgLEa8yc1a5bVm9tzeSPnALoulO8cV2yaIOaZabF7MvRCuB6V1-xKXnb6JEsrEcOhiEpwuLJ4YUD9AWiY8dm_7bCQkVDL2eNg8kNLZCRw7IMlwKxtRWyn6FhZoWtAEcLn-LzohBq2U4GXKgPBDZJ7rpet__SCWCTVJjQFrZCC-y5adHcEbyBao1FFZ50pMVKFpJ-zR0gmGtIqxcGE61xLweKa7VL9PJxBcn0HPyJE1bxeIqnc1oqE9T4UJIuqSldPjBrVCH2MYUPuQGLUNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=CFqmJTsQ4Chbzw_utdgcD_FCAC-vAk3ggZrRO96tOiLYflbLjJ-hs7KKkkemxiw0xEOqgLEa8yc1a5bVm9tzeSPnALoulO8cV2yaIOaZabF7MvRCuB6V1-xKXnb6JEsrEcOhiEpwuLJ4YUD9AWiY8dm_7bCQkVDL2eNg8kNLZCRw7IMlwKxtRWyn6FhZoWtAEcLn-LzohBq2U4GXKgPBDZJ7rpet__SCWCTVJjQFrZCC-y5adHcEbyBao1FFZ50pMVKFpJ-zR0gmGtIqxcGE61xLweKa7VL9PJxBcn0HPyJE1bxeIqnc1oqE9T4UJIuqSldPjBrVCH2MYUPuQGLUNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=J85VgnQz9-CAEXlpjx4Vz0uGimFAAFXXbbHSzSTGvWeyCJAa0gZlaXwBg-g8mO8HUzomqfaEO7H9cO83bCEKTk40i4eCfwhJtYU6d50dLTT8CuPt_-xXJzlvaX4lc5A959ImQkheSHH0lSKZbV9DkCw5wwuJLpiQjXr-tSmbWIMl6ROUgJQe9yEWtOqX0MBgesbnAeDWQyDVMvNx7HNn-mMNNKc-omYdgdxDjtHYghM9UjINxJxw7Rvq2swGzm6WwczY7bch4a9Xt21XsJrpDpsGha2hJul1-T5k5B3tzxJxn_MCu3GMH7xj8HsNnicRtC0xx_prXxzG4pNBCNPXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=J85VgnQz9-CAEXlpjx4Vz0uGimFAAFXXbbHSzSTGvWeyCJAa0gZlaXwBg-g8mO8HUzomqfaEO7H9cO83bCEKTk40i4eCfwhJtYU6d50dLTT8CuPt_-xXJzlvaX4lc5A959ImQkheSHH0lSKZbV9DkCw5wwuJLpiQjXr-tSmbWIMl6ROUgJQe9yEWtOqX0MBgesbnAeDWQyDVMvNx7HNn-mMNNKc-omYdgdxDjtHYghM9UjINxJxw7Rvq2swGzm6WwczY7bch4a9Xt21XsJrpDpsGha2hJul1-T5k5B3tzxJxn_MCu3GMH7xj8HsNnicRtC0xx_prXxzG4pNBCNPXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=tsIDY0ZY25J-TBcWoei9MpgUMvWLwmckMhX2QqmGwO_naBss8j7en19X0lXGQl1PZmtdszatE5EwI7SKEbmW8NOt5o4rmPGnwpm2RW_2hemUMC-bq4EqA9rqk5QIyBst2vfb0SIxENNKRLkPV9LAdTm0REVBU0jxE9AKzXNdm6T4dPYe3cTVvyXcz1cf29oPfxj83QEqaYqfxvTz9IolBT60lp8U-mdTrMxJvkNq8zIwqlvXDmGUnC6CQLsMTadTls6Yr36dwiRl9Rk6UzApwbRksXAwPknPQddqFt-HYpA2VmoKFfpORuCNDPKiTgxq-22Y0JWBpZ4ZBhDPadEd3GW5T1uPfQ_rUjcy44neBKh_d9G3K-RSjSN09iP375uGwP8RMnVre84ySrN6nfHkotasDBwo7t6W-9SoQzF72XdJttZz9pbTKmhJNcITBjWTqM1CeNRHKf7AbqQOmAvDdUsM-b7YQ6Ci_G9OuAf_XhwvwMYFVAhxHAtMuK9XeuSbVkwZWdVlh-WoZZgn3dzM9ck7O-BkFyKYm1jQhZqHNoaR8vK9RE84viJCeF5sJX6SS2mkx2aTKjhz6Lzhrjb60myz7_l43RMaeN4wDoYwdE4mGFiR8Djqvv_ywngjVgJWWKgroRyKuCr7U4OOeqYeLt48wH73-hYfg2CvOGyRJD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=tsIDY0ZY25J-TBcWoei9MpgUMvWLwmckMhX2QqmGwO_naBss8j7en19X0lXGQl1PZmtdszatE5EwI7SKEbmW8NOt5o4rmPGnwpm2RW_2hemUMC-bq4EqA9rqk5QIyBst2vfb0SIxENNKRLkPV9LAdTm0REVBU0jxE9AKzXNdm6T4dPYe3cTVvyXcz1cf29oPfxj83QEqaYqfxvTz9IolBT60lp8U-mdTrMxJvkNq8zIwqlvXDmGUnC6CQLsMTadTls6Yr36dwiRl9Rk6UzApwbRksXAwPknPQddqFt-HYpA2VmoKFfpORuCNDPKiTgxq-22Y0JWBpZ4ZBhDPadEd3GW5T1uPfQ_rUjcy44neBKh_d9G3K-RSjSN09iP375uGwP8RMnVre84ySrN6nfHkotasDBwo7t6W-9SoQzF72XdJttZz9pbTKmhJNcITBjWTqM1CeNRHKf7AbqQOmAvDdUsM-b7YQ6Ci_G9OuAf_XhwvwMYFVAhxHAtMuK9XeuSbVkwZWdVlh-WoZZgn3dzM9ck7O-BkFyKYm1jQhZqHNoaR8vK9RE84viJCeF5sJX6SS2mkx2aTKjhz6Lzhrjb60myz7_l43RMaeN4wDoYwdE4mGFiR8Djqvv_ywngjVgJWWKgroRyKuCr7U4OOeqYeLt48wH73-hYfg2CvOGyRJD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=jrEUQYziUmIr3IUB8Mj3IsYFGmVu5p86nTuugqmUq08TJIz7Oo4UOvXEcz7Yzv5L340AhviF0oKCLxCkKCvPhCEZnAGhiszmGTzaRJ67kb8634E5bRz86xAURhvG8u_34m-h9jbAt07GdJNf0Nx2v8FJOKhoSZRS_hqXeDb3CEE732LeGPp5cTZB3kNl3lKERCR46DGr2l7ZVpI_zUPYi1SjGevVPn0J8FGBLW4lvw_HnkX_jzX4frKVAG0OpYnS1ad-wlqXmiKGHVYhHvGl2tNBkKL6hgm5Qz5jcf1Jk2onXvRs5BrtmwON-eC9SzvRMoSiERTbIlR4EKvKfNKOXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=jrEUQYziUmIr3IUB8Mj3IsYFGmVu5p86nTuugqmUq08TJIz7Oo4UOvXEcz7Yzv5L340AhviF0oKCLxCkKCvPhCEZnAGhiszmGTzaRJ67kb8634E5bRz86xAURhvG8u_34m-h9jbAt07GdJNf0Nx2v8FJOKhoSZRS_hqXeDb3CEE732LeGPp5cTZB3kNl3lKERCR46DGr2l7ZVpI_zUPYi1SjGevVPn0J8FGBLW4lvw_HnkX_jzX4frKVAG0OpYnS1ad-wlqXmiKGHVYhHvGl2tNBkKL6hgm5Qz5jcf1Jk2onXvRs5BrtmwON-eC9SzvRMoSiERTbIlR4EKvKfNKOXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=t3IuJPwvvZJI4khiTaEW99SgNC411zdFEV-VfBPzSU42-WfA6cQqzQag4iXGF5xjTC-yCEN3Bx-PRTaxjf6dF8Fy4EHpJJR6X0VgLfg7amnBmrbW-GkHlxBqqFA8R-JJpNZ51qt9BVgD8MWStLo91v1cD2BL1Ck8n-OMMiaeRAxvR4RPRcLqC_trTdG9F-Q7O1sJIZfYeFNVEUcAx-2TjwoZzs0IBnNH5zGZ8Pd7ARCkCPkKTfcDtPPAXrHK0w1toKrslvRK4Hwf-sAWE-53EHxAtXRUA8YUI5AI3WfdF8oApRnQA0oTV9eagLWX5Rc1otaUewzLyOTcbvfmEeaAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=t3IuJPwvvZJI4khiTaEW99SgNC411zdFEV-VfBPzSU42-WfA6cQqzQag4iXGF5xjTC-yCEN3Bx-PRTaxjf6dF8Fy4EHpJJR6X0VgLfg7amnBmrbW-GkHlxBqqFA8R-JJpNZ51qt9BVgD8MWStLo91v1cD2BL1Ck8n-OMMiaeRAxvR4RPRcLqC_trTdG9F-Q7O1sJIZfYeFNVEUcAx-2TjwoZzs0IBnNH5zGZ8Pd7ARCkCPkKTfcDtPPAXrHK0w1toKrslvRK4Hwf-sAWE-53EHxAtXRUA8YUI5AI3WfdF8oApRnQA0oTV9eagLWX5Rc1otaUewzLyOTcbvfmEeaAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz8-sMzY9S4UVcEbpiasaxGgvs_G50movtPvFatVSpy5gv7ij6ZpAqnQQf9TEPzhWqvA_y_JLxS7JXpdhQdtLWIl3eRuG-UJkJiemxGx8zyLCdDSA3nQ-nquP1i9EIWAqqUxFXRygY32biPx_MQW8BVvgmT0kSM_VCU76pfQKEvIFOdNtBNpsL4GBsHoNavFtW7Yw22llpdIH6CC7igSRx9jkBK6u_YQazYUvngPvPzMJAMeBecLKI-5SjfyPbTct2sYhhge6zq96QgLgDRMBSqYpkPd2C540z2b6Bx2UjsRIvblmt25og28WppcOZH08Mj0Tix7jHWzJ1H-FQrF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=glBxo6B_2Wr-omhDb_T94R1pu-WMJhtDxGC-dB9HfmT-SrSbmx8L3jgFGtvLOc9z3gcHF908c4lAvj8O6Xg959m5P5-WukBsNJgmp1Vs4BLqPeAwU2TdTGgjv-2WJ0NqHovZuEEFIzErmDVSzgBysru-CKo8DhPKxUtbHROIudh5WyxTHOSqG2xK61rsJnUr6ypj-pFMsnT0yEwJQp9sonXXhDA9fv35HR19uvdZw-lsAG1trkU1uyg4QCSc7nwEpa4yn6uGtk1Lv7yM2cemiuPQBv-RovHsYKtbJAY5ZxXM6ykT8VCHbcCDetcv20KYkuGjIjGzNrRL3UeOs56g3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=glBxo6B_2Wr-omhDb_T94R1pu-WMJhtDxGC-dB9HfmT-SrSbmx8L3jgFGtvLOc9z3gcHF908c4lAvj8O6Xg959m5P5-WukBsNJgmp1Vs4BLqPeAwU2TdTGgjv-2WJ0NqHovZuEEFIzErmDVSzgBysru-CKo8DhPKxUtbHROIudh5WyxTHOSqG2xK61rsJnUr6ypj-pFMsnT0yEwJQp9sonXXhDA9fv35HR19uvdZw-lsAG1trkU1uyg4QCSc7nwEpa4yn6uGtk1Lv7yM2cemiuPQBv-RovHsYKtbJAY5ZxXM6ykT8VCHbcCDetcv20KYkuGjIjGzNrRL3UeOs56g3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctB6oYJpUm_LAjSCjEfPX4YuvuaqYx24sK7zDS67ky2Nq10SaG2XTI3w0DbikqW4mWFqo3sZscH7f_rchKgLyLmAk7sxPBuBTdYnpaG_ERJ2Esq8appMA8SEO_5mZA_p41b1A1k0bseXUwWINR4AOWnMDhfw5XSizXDB9Sot8jKK4IX5-uzYctW_RhKfhePBT3CfV1hkaOs7EIo48f-BNF4PKF1M9Y_4OIRSAa9-qsEv-l5_4SAJr3DEYBGXwpRmqyXFuUvOj7B1-3J5swmSmhXpaIgWM_cYYgt7a7ZORyAdDlxonkauikvCS6utiX8wNFMdEXJnIJeAAdKEPkPBOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdHZyp9GpRyfaGqK5kdc6bthh0HKj1_zY_bMjrmWdQeUuyCmw6aP4mTVUCyJf1buvGKql9P8EPQPg9zxOSyXkygUFHsqKVlVGoaZEecoCDAJSbIZLrr4-_isUsnP7srkK3teSSnH7xw2X4SKApXVhiZXPBBqtPDef28VBGxubZz993HotHmrfJdB6Sk6l8gI_7C8azY2A-65Glx-yIii1qhW0WDNrXpA0ibhBc7EIo-0QPBoYfROoGgkRt4RcxtVsj3lPyAHOtAIbW2zYu2yGDroPQ72HtpNh2CFzPCyGUYEVjJW63uyrzx8vGcKm4jQc2LOk47hx8gewEG7T9t_og.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Ldn0PFOowEVtQo7SdML468yN7jiwlh_uCNfGhgpp8tvzZT8BTECUCEonzYCJXNCKNp7Wme1hXzd5kb34t6RXutLa7bjlsUTK6n9rfRKjtld2eq4dGnrSdJjWritGeV784e64lUpxSTS7nfG6h_LSqmcBAnQTaBve9CVxaYoNbL4RdY8VZBK-dQF_a-dZFY_ikYqu8fIkIXTjfVqGJktY6iY-v5vxEz8UiOOZjFhxkVpOpefX4xzGmknfSQYid3sUWb-y3JQE8OJCoaeBhUZBZl-8hcaU1cyAF-9p9ltZikTupEQawvWN0hHdplzCDC3LCAEOBcAHkY1CFJORMAN17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Ldn0PFOowEVtQo7SdML468yN7jiwlh_uCNfGhgpp8tvzZT8BTECUCEonzYCJXNCKNp7Wme1hXzd5kb34t6RXutLa7bjlsUTK6n9rfRKjtld2eq4dGnrSdJjWritGeV784e64lUpxSTS7nfG6h_LSqmcBAnQTaBve9CVxaYoNbL4RdY8VZBK-dQF_a-dZFY_ikYqu8fIkIXTjfVqGJktY6iY-v5vxEz8UiOOZjFhxkVpOpefX4xzGmknfSQYid3sUWb-y3JQE8OJCoaeBhUZBZl-8hcaU1cyAF-9p9ltZikTupEQawvWN0hHdplzCDC3LCAEOBcAHkY1CFJORMAN17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=s2KslmmODOssUBkO0kBugnkDeIiXAGzaCdl58IpVgS5x70FOTcz5Dv7O2bASbXCf8EXgAeyeUfFqIyioYf4YHXGxoTi5ZwIkDbsJS62oyc4qGEDy1JiJATlW9cT3etmCNxs8Aw83Lsaffv4Tdr7knlKjcYjepOAX0OC00ecHwoaca1FNPAUX9ovM4Al35nAmoep5TkaC_vf_gYu--X65ki1nUMd6WqykfsYw_b2FJbM6icO6bMHdbrBs4e9ruJUECrC63SOGGsZxrhZTLb2cMZ6q0XklaEX6YDQOlw54JBJyWWkZ5P3ROFObSTdZvNS4kL2xXxQfw_c5LCZFTbev1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=s2KslmmODOssUBkO0kBugnkDeIiXAGzaCdl58IpVgS5x70FOTcz5Dv7O2bASbXCf8EXgAeyeUfFqIyioYf4YHXGxoTi5ZwIkDbsJS62oyc4qGEDy1JiJATlW9cT3etmCNxs8Aw83Lsaffv4Tdr7knlKjcYjepOAX0OC00ecHwoaca1FNPAUX9ovM4Al35nAmoep5TkaC_vf_gYu--X65ki1nUMd6WqykfsYw_b2FJbM6icO6bMHdbrBs4e9ruJUECrC63SOGGsZxrhZTLb2cMZ6q0XklaEX6YDQOlw54JBJyWWkZ5P3ROFObSTdZvNS4kL2xXxQfw_c5LCZFTbev1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=taNfirSuUU04t6QOKm3-VdMooC53ZnKWAITIV9x4JlJ9d-CNBltM6x1qP4Esea9C8eMI2nIdZHTlYihujhNQ8sAWi8AEo7UlA3fzh1pKlfg2Wl6hUynmlPerPsrpx9NleOH8-U66U68i7xu5So72LN5ax4RNfng8reJmI8tQzneGqbVKtsi5FpvCnd0HUrTeswNU4cL5HcxkeIPifEOJh5ZLuzaO6cukMhrKt8Cnl2aoZC-q4OMPXMrTkZI5O1rt5s5kNvBR0DFFakNNCYbjOpckeSfPOqkn037kJLKNjkzjWVInZHydU7YxbhPtuYY5T9G85uVyExr08jvQOu_B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=taNfirSuUU04t6QOKm3-VdMooC53ZnKWAITIV9x4JlJ9d-CNBltM6x1qP4Esea9C8eMI2nIdZHTlYihujhNQ8sAWi8AEo7UlA3fzh1pKlfg2Wl6hUynmlPerPsrpx9NleOH8-U66U68i7xu5So72LN5ax4RNfng8reJmI8tQzneGqbVKtsi5FpvCnd0HUrTeswNU4cL5HcxkeIPifEOJh5ZLuzaO6cukMhrKt8Cnl2aoZC-q4OMPXMrTkZI5O1rt5s5kNvBR0DFFakNNCYbjOpckeSfPOqkn037kJLKNjkzjWVInZHydU7YxbhPtuYY5T9G85uVyExr08jvQOu_B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSB23gi_dC2ImvYuXH1UGk7pPQPwTwEJEWWLzUXPovtaRnD5ZQ-maapZW1h1BkD33W_iGfFf3BV24cU1LnbD01s-t1un_G1fn1RtrvNditd_SvakfX24H-vll76Ev2qM6I1KI8Sxlm9oDIH-JkTPntMXTodtnnRtKcylfedzmaJKjizxzVKuEGwIISgL67MNHzOFMtyrqtTZ9V_7Ox_VmdNCrsMTP4GDsmSBjaJhliwb7d_U7-1nw5NjvIPUi-yAdjdHtyPu6S4ciAXa9dPqfPVqQQh4ZVLw8LcK7NyemuTFMz8tfbryEZhaZXaUgME5eAexmdWRGdFMyu_qVlNZbA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=IUvAtAytk0z8EKUHd1yyTQ0u-z1XdvHpnMB99W8uaaN-gB2A_6jX4_GoBgUN08gfOxNEpWQaPQwaAhO9t4ZyCKVHiyWpORC-qsXs9vhbhOAsSFy-CR1mLmFQBkS_ZsfYSeoTPEBkwL7cuqOxd5hT5UfTBB__eLQEIrNrcOQRJbVmQDtu0mlLmYDspXOTvTEmeaTuwMxqoJIIQNzVEZdgkXUiqiZw1enSgIkxtSkacRwrWjQbHzxP-9FdNYjHt3JwNUevufP1kAm2mKNqG-vJ3Za6gimJgnBRuX0N6sNNPt3JmMuN6N9cTrLRNaoshjYm_LxsBbzShvSygfX6k2iqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=IUvAtAytk0z8EKUHd1yyTQ0u-z1XdvHpnMB99W8uaaN-gB2A_6jX4_GoBgUN08gfOxNEpWQaPQwaAhO9t4ZyCKVHiyWpORC-qsXs9vhbhOAsSFy-CR1mLmFQBkS_ZsfYSeoTPEBkwL7cuqOxd5hT5UfTBB__eLQEIrNrcOQRJbVmQDtu0mlLmYDspXOTvTEmeaTuwMxqoJIIQNzVEZdgkXUiqiZw1enSgIkxtSkacRwrWjQbHzxP-9FdNYjHt3JwNUevufP1kAm2mKNqG-vJ3Za6gimJgnBRuX0N6sNNPt3JmMuN6N9cTrLRNaoshjYm_LxsBbzShvSygfX6k2iqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=aTUpO_kmejoys4Zeb5PPiX5Gz6W0CxH4FLEgBcBIrJsbskbgJBabUDs-4PxHPoEcZDwdS8m1cQiz3UOP7ACQC9pxsu9lEP8sUAkPCO9XmHiG2i0372MvZUEN1N2pdEcRR6IlosBzLUYb5chxzq9u15VN6sqDV3SybZVtOL_J4uv_RZwLZHawawyuTVoPZppKeo5SFyy-5Nw9YnmGsZ4VHLYmmnVwnyiXiVFds85WMarRywy4kbh4NMYyR-NfcE5l2b6mvpADD6zWQQcn42HXcuCFi8WINW7mKA2j4LCvjYgXEJKe95dk7ktrBM7TNatNhmghwCO5v46NWk7tKWV2ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=aTUpO_kmejoys4Zeb5PPiX5Gz6W0CxH4FLEgBcBIrJsbskbgJBabUDs-4PxHPoEcZDwdS8m1cQiz3UOP7ACQC9pxsu9lEP8sUAkPCO9XmHiG2i0372MvZUEN1N2pdEcRR6IlosBzLUYb5chxzq9u15VN6sqDV3SybZVtOL_J4uv_RZwLZHawawyuTVoPZppKeo5SFyy-5Nw9YnmGsZ4VHLYmmnVwnyiXiVFds85WMarRywy4kbh4NMYyR-NfcE5l2b6mvpADD6zWQQcn42HXcuCFi8WINW7mKA2j4LCvjYgXEJKe95dk7ktrBM7TNatNhmghwCO5v46NWk7tKWV2ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=NG1fjzYz2dzpgoBYwXMYJ5xk7RYEDMH9UUur8K9FlGFCK7STp0D3uAM6Wv2kMXj1nqUalF-axl_y301Qr__kQrfSLVq7bYIARHdDFHZWLdXzcISwn8IOk7NHL2GuGnDIeuFIUiqbTvlt1uwnnRN0Yx3zPz8WJTUDoeRQ6A-cjfexoa6dBlyXFVPfhRIffVl3pKfs_oF8_WQP0agZ-kDFXqKVnS7tRJFI9U6BVr53q1uuBfsYbPC6P2iqfd4ybt1Tnf9GfVFFKMkeT8EBIPlLY1cayiTtfhHaJYxqSZAj_rKT8qA4quyWJUnLHaQyRgwn6F9ZkCw0qH75HobiIRwbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=NG1fjzYz2dzpgoBYwXMYJ5xk7RYEDMH9UUur8K9FlGFCK7STp0D3uAM6Wv2kMXj1nqUalF-axl_y301Qr__kQrfSLVq7bYIARHdDFHZWLdXzcISwn8IOk7NHL2GuGnDIeuFIUiqbTvlt1uwnnRN0Yx3zPz8WJTUDoeRQ6A-cjfexoa6dBlyXFVPfhRIffVl3pKfs_oF8_WQP0agZ-kDFXqKVnS7tRJFI9U6BVr53q1uuBfsYbPC6P2iqfd4ybt1Tnf9GfVFFKMkeT8EBIPlLY1cayiTtfhHaJYxqSZAj_rKT8qA4quyWJUnLHaQyRgwn6F9ZkCw0qH75HobiIRwbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT0FXDDDN3XtOmB2rmhnH7ZRlxh_raHfJ-gz1OF7RTSIo4WgFvFAmwRVYVm6KWulNkjHJfGMaCujwQGWsmwLv8qdYg--JhnK9L5jBHOBJhttyMMnFqmYA9NNrimXW8lF-nUtgoaOSANp8-8_NOzjWcgjwIqYfAkNEiRzsbYMaJujzBcAMVR3z7VE2P2v1VyBuEpkqPx7tVB9YSzi0cICet5W2k93kZOn_rf57mX5aSsRvc_pEQs2SgJwgr1Y77PNm7KVcvSrfhJu5iMb4_amCslciGU4AEFzGs6rMc4hu9fFyl-6m9L2HlB86YTGR25DgNeqNouYaxXIUfl-uvulEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ujKmYv-hk0k7tXYwd9PkgjJhtd_tGXpJaUC5-YrTkcR5KvB9P6ZRO8R-r9gxU5_FD6RB5gTurHVxI1HgKgLaIR9Uy_cvCBahrlaTb3mybylI_2xO0ZcYZfD18L8q9vwwgXctO_2CaCMtAn2YIy4iT_PM2op2MiV8UJ3H9wEBXc1n9PGea_wMZIkl9d8XPU9D8aglu8_RU2pYGIQqAomDend-VsuK5J94v3oJfSEctWAzpeFRz2ESho63t1DSzXbixst7BPLrMmJPE6d_iPpiuxGR6yZBs2MmasTC5SlVIvEDS2pvbIN9gjbMsYplWPY1j9DRLhSFUxud5YYu-fI2uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ujKmYv-hk0k7tXYwd9PkgjJhtd_tGXpJaUC5-YrTkcR5KvB9P6ZRO8R-r9gxU5_FD6RB5gTurHVxI1HgKgLaIR9Uy_cvCBahrlaTb3mybylI_2xO0ZcYZfD18L8q9vwwgXctO_2CaCMtAn2YIy4iT_PM2op2MiV8UJ3H9wEBXc1n9PGea_wMZIkl9d8XPU9D8aglu8_RU2pYGIQqAomDend-VsuK5J94v3oJfSEctWAzpeFRz2ESho63t1DSzXbixst7BPLrMmJPE6d_iPpiuxGR6yZBs2MmasTC5SlVIvEDS2pvbIN9gjbMsYplWPY1j9DRLhSFUxud5YYu-fI2uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZjcYuR31ugzBzoN6txtQBhygPMLHBbURLFEGZUpZIlGOqiJW1nCBpAuL-Nl3wNmBGY6lpYmlqJ3wtrSW7yesSj0vISlz9_jRCWxslP5UJnd0dLF7SojL4WMV62U1PlWGlKCeJ9Utx6gdi-GsDS3ic6MvtkRDznL209tEq1B7wBYw88WYqIz5O2xfwHUE-NrP__bM-ufIdpdahOftRW_spMtYD_y1Tpt-r-VnROn3hnGo1TGB0fL31r5YCnKftIk9KaFg4AL2QjivsNltuM3fDRJajfxAhScUegxfZhxKwlicEnbrBeK-0WDbzIbIJdFjb3hmAPt5_kF23COmoz6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=HZ7oa9Vz_kDyKf-b-ng00J4oY6hUhnrT0_pUK4TJD5uYM35ywMgK9PcXwRuhwbpoOHssgMo4-urd7GgCcbQXk0WxBCaarSQgjyG35moSiL2qq5sxzUxszCG3IC0viK2DtULbElh2jvS7-yZgLdrm-KLhrdjGHcpuQSkZqQMu4WxIzYuYi96mwxXwIhDIwerpZQ0hm2HCT7oDTKg6wkxlfesUbqruiIzMcT2vpz2PCHdiNzJe_p1aIQi5gRtOLwfUIX7tV_ILWO95nN7pf7fhnZmp8dAgUCeZNkPcCPK6vbi49KsAXGJ6irGPjtHKf1ixucc2Eyk065rlxubHiVbsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=HZ7oa9Vz_kDyKf-b-ng00J4oY6hUhnrT0_pUK4TJD5uYM35ywMgK9PcXwRuhwbpoOHssgMo4-urd7GgCcbQXk0WxBCaarSQgjyG35moSiL2qq5sxzUxszCG3IC0viK2DtULbElh2jvS7-yZgLdrm-KLhrdjGHcpuQSkZqQMu4WxIzYuYi96mwxXwIhDIwerpZQ0hm2HCT7oDTKg6wkxlfesUbqruiIzMcT2vpz2PCHdiNzJe_p1aIQi5gRtOLwfUIX7tV_ILWO95nN7pf7fhnZmp8dAgUCeZNkPcCPK6vbi49KsAXGJ6irGPjtHKf1ixucc2Eyk065rlxubHiVbsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsAIp-o0x_IDpswfuBit8YBSTK7gxX5W_mm6TQ7sO9GlYlbH59EIafGFSyJsfFqdhQi81PWJ6Xlsx1SNod_U7QwgZ0uoRv5VElMWhUNiUmirICkds29ex05BU3YpYRe-8eRWycsUEhxi7P9tGIRDr7BykdurMj4Pgd9KCjpEHlgwfo9MFQr7OoQULNFck9XqlvflcusgwU57ydSzBPOOGqoOptulWwd-9sfZ-fkjbfADvQtxhYfT4aQIg-sYbctjwudUeNYokFRqpqWetY2OGZJ3Ai7j2d1Dq6MD1LkAABXwvEZMA55mhuqZVRM-G607t8Qngic7fbk5qvkY1wg6Nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=c1ahW2rSj4LI0us6FgemRApJo-hyipqt1OqSkjNzMwFlf9ISkuwiJ74weYWHrqePJit-NJZG7EGrvRur-J1BH7NaAl8eCXtNN4G_tsD5YlvleaAmoZihKXutOkVHf_VvTsFFjyW4IPny2KeHJVGdyDtlqmC9VyNzS6OrRz-OHWlUgH7IK09LzQwjtogvHl0recJ3qNC4PuyCId7Pn2BDgaR2xw6almIh-_JXF1-jlDxMFBfPcnNrEuD8tpwSsZsRLClhgvskUrnshVwJBnm_8kWXV143Swu3xsXJ0a4kbA0OvZyLsKq8Vnr_v-RlrT0oZ3MQ5p08B1_VKfe581zaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=c1ahW2rSj4LI0us6FgemRApJo-hyipqt1OqSkjNzMwFlf9ISkuwiJ74weYWHrqePJit-NJZG7EGrvRur-J1BH7NaAl8eCXtNN4G_tsD5YlvleaAmoZihKXutOkVHf_VvTsFFjyW4IPny2KeHJVGdyDtlqmC9VyNzS6OrRz-OHWlUgH7IK09LzQwjtogvHl0recJ3qNC4PuyCId7Pn2BDgaR2xw6almIh-_JXF1-jlDxMFBfPcnNrEuD8tpwSsZsRLClhgvskUrnshVwJBnm_8kWXV143Swu3xsXJ0a4kbA0OvZyLsKq8Vnr_v-RlrT0oZ3MQ5p08B1_VKfe581zaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKXr2IUtM0sE0Yp2jtnSZ7Ui1EC_mgQgNzRKQxLMNg1wOHCoavqYWFd3DbuWOPOI44A_HUDGGioDPqI8AdLQtLj6HCtfkRiEl7Zh9wQpo9hjEMVlpM75Y571JypImaa0chfiNGNY80gZsQkWYQcRd8cvqlG7nZJP0PPGS480X2RglWmMtpea2TsjeyPo5aByhp8Xj55p12xFJqFSoWkUMEpWWGk5ukUUFwpanRkuTqoncUAY1CaM2RhF5q0cUPeHiGAaW0MjHvvtmWNQlc0xVcs9CXuG1umMUUA87U8d0Ffbq6OThYAboppkOu5W5mZhsobP-bqYz_MKgXwHvsjy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HYQNX-SyriKaGxpAfePkmAQ7sqAsCnV80UobRErGmeiHlqh-ePDMvH5oTyphjrp3cFJzrWrq3dvYRQ1a8nUgIdbeyK9WlfWLPTrDpwCEsoM04soKQZn2OKbgav5I-laT3vZSr3NMlcLvRPEC0oKW8DcKp99InNX77xO2XFwyQLr8KhdGk6fN_7zghWpXv6XI-B3xYASbLx0pmHZxTzah2pg1zwyf_Nts4iuJ9YOaDrGtMLBlgNHAyP9vNHxytJ-ATBOOaaQvgmW3oVTq7Mp3jVTkNyVzC00tXhTl8eBPr35KnylESc144ka5M_Zzf_bnWNjfYS55iHt935TpWnX5XA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=trfLI_HB_ZAsTouNep6gWGzcs-l80zv-h179G1VODXtgjTMOGO3fe9ZTExzHI8H9z83wWJeuub6xgBJs2a3OhrSVtR5mWbaR71__JdB2lh-Nr4R0TpbaFjf4ZO9QxFOpnjmisARn99sNpuXVCAqCdvoTbcHQjk4_nYCkJajYB-l43qTswkx0pnxI0L5fbwM-uV7n-pRm19kOslrYp6wMf58rnij8XK5mT2g1EG6c94JvipvGDJuWJvWAfdeCvbBRCOiIcYpAuyZhjwEyORurDrr853y0-Wmqv_8CcgB0jQHKGVLx5C4XW8E-MBSQVvIk-YnGdoNQtCHetfxW61asig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=trfLI_HB_ZAsTouNep6gWGzcs-l80zv-h179G1VODXtgjTMOGO3fe9ZTExzHI8H9z83wWJeuub6xgBJs2a3OhrSVtR5mWbaR71__JdB2lh-Nr4R0TpbaFjf4ZO9QxFOpnjmisARn99sNpuXVCAqCdvoTbcHQjk4_nYCkJajYB-l43qTswkx0pnxI0L5fbwM-uV7n-pRm19kOslrYp6wMf58rnij8XK5mT2g1EG6c94JvipvGDJuWJvWAfdeCvbBRCOiIcYpAuyZhjwEyORurDrr853y0-Wmqv_8CcgB0jQHKGVLx5C4XW8E-MBSQVvIk-YnGdoNQtCHetfxW61asig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvr1X3t7kphOAzdIqch0M3q0K3TNvNFVuNUNRL8T5RFzmVIfn4TXY00PY-XscwCE6zL6ypXdiEGkk26z--s0SVNnXyuZ7WmL_XCXWfzJ7hbbcxlltM7DuM0zY9x58LzQPlRANiTWhwv8QS6yTlMP9YUGQmebf4CRv0lPxNCVFU7L-e07ttKRSpNLQfvIJTkGjtJBIrVWG6pwfifGxQEDH_1wDbSse4PCXZyVv7C6aMORmqWyLXGq4_CrBewbdcn1KO0GJZUSHoXU198tnHpB6lrpVNfilsvGFjhDo9sbgmcZMcgWBtPr2zD3zw1L6n3TIfIQ3KJ6R1rsU76Ebw4ayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoFJU6h6yvq02oPAYEP0nmBBWgomvV54snZbdWIv14nAZj8OiGh3TgQtoP3JzDv0BDbnwIglXw3EM0_BAKvuW-xD24Yi-KyPEQ4pbFNzBqGY0dYwMviGKFZgE7LvveBDJ-Db4d9XJb-c2OxncwHLcHZNvM5w1F8XsyueUyWJ6wkUiYVteqrIk0-dVnvMvzqXrSEqPxXBvbaCT2WG9Y75636h6OI1qI-5W01OUbgI9G1EpQ3K5Y1Q1TDpUyZjQ2fyAyXF7vJf7jxtq-yaeOArNXU8lCzXh4us2GSZBvBRmoG_2xnyRHi9twe49JhRWSLX_k2J4nNrYzmBCa0UZsgepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9ADr0Ao1kRpA4YDBrDgITmtAMORKKVIPHD7jjEQ3gtcH6HnZMO2GBjk9PKgDuAqYK54ZWcu1GTisINiGA-dyxO2PrWJIHMQzoGgJhZpP1kk2Ssceo35CedQUDIxBC2Ch3_Sc-AvvKLo5fzOZObDhLoAN-KxCjOAz-1yI9C7DrhoK8-qdlRRpFS6mDKcpj097-ybGKKXxtc_BRrSNeosTvuCGk--3AteGBeC1HcT_VtzuajlPk2H1wIDq3gqqVsnn3SEgJ8K4jUqA0Hk_TI-qJciji59mTu02gnIdeYliMMWDoJ4_dE6pXncREv_vRFwEYL5mfiXNPg0c409182uSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpX2uJmkNYPskC3FXsfEBXRpLMJbpx-T8ysmKIv-VLIVnk212zsUgZuBCS27hTSgu0EAvPg2TdOI5iJMs4OyoPe5I-FEeuvuBMBZX1ObeXOJf9CxZzVolicCr89s1nRZfWPic7W-DZe1TUiHBYGg5zcnRKmZWX2KqxkvR-CJEQA7tsO7Qyj0TYCJl6stKylpgRwrKb-uBNYSW46SMG42qmVFqY8ppDF-IqAmWt_a4ZAA174z1XZb4eCxkHD-q_rNaC28Zy-AV-gcVsXYkP9G9-uikAlAV0WVh3lyswLRUrN4OKvtUPW1YJFlezbA0NeGj-AIpXInvpGyg706z5Bdbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCpSsa_m-aRicy9VS4MmO6eWRC1Tm4A-mS422IEliy5fGZQg0hLh3MbiWvbiL88m4saClNbi-VRZrtfsntNGm0n4F0d_85H-0tPREDSdutzpEu-xwcOiVw9iDDJDQf_BpX7E8wxghj6Kr7GqrUN3-hetV_ULD2md0v2MFF7eNaXuqRD1I5VMh-TsmsCY73RbHjW4cV_nYfgM4IPqfv-Htjv3ksU5fVT-154frI7WoaCPdrzr9ajBCjM7pdZN5PNWRrcJ7_3lR-IdyeWSTHewTPltCzwC1458MhCc5EAJORSjNaZ_Jq_ldoiiCfIJM7giU5quPWHD-6Xv71tiboquTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=fNCGqoLzqpozSJk-GXNO7mGM5wfuKeP4Wb9Hdi2Jiwl7Nt3vX-nTG8d-CSWVE_mOlRDs23gIS7ax-KIi4RJkKCS9CIIfm0uFwkwoMiTtfKC0mVkBEFvGoRgqypE6QvQOkoCP3_msZElKKHIaR5ZKnqU09-bU0LISGGo0JD8NIII0ZfGO18TLLb5H0yLHkCwuNfC8TjF66sZ0kn3rZe5VjQnlVqaC8bov739mlqYs91sn5UKip0EHMyRsBjWYKjRsZHRB4CuQk5MJB-gcZFsWJNwMKsk1qKju25HQ3w7x7bQa-XNQgB7Lk_XAatvSK1Pf4_e3r-GZyUeGv5hPDzFvHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=fNCGqoLzqpozSJk-GXNO7mGM5wfuKeP4Wb9Hdi2Jiwl7Nt3vX-nTG8d-CSWVE_mOlRDs23gIS7ax-KIi4RJkKCS9CIIfm0uFwkwoMiTtfKC0mVkBEFvGoRgqypE6QvQOkoCP3_msZElKKHIaR5ZKnqU09-bU0LISGGo0JD8NIII0ZfGO18TLLb5H0yLHkCwuNfC8TjF66sZ0kn3rZe5VjQnlVqaC8bov739mlqYs91sn5UKip0EHMyRsBjWYKjRsZHRB4CuQk5MJB-gcZFsWJNwMKsk1qKju25HQ3w7x7bQa-XNQgB7Lk_XAatvSK1Pf4_e3r-GZyUeGv5hPDzFvHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=KtJKpr1mmY_-CqfJ5mwV9kqohac4j7QsQzZ2c5gDbKVMDVYXtue50uw8Oa-fOvy8zkbK8SzbPVNVuvC__UDgbwGznMn8noPWKil3h0rxhBQaHUu0euoQH3taCQThnrfnmXDN1r1lK_i1kcAMNwoPtkK9ZuVC0JutZoEbrkVXQaO83nQmtxR260zBzg8iQx2RR5Qa25lROHpCe-SQkcc8z23sGHpPjcGBsthkQ_6wxbUBcL0XSYhJN4Wk-avznRf0REH94oNqNvXd_BtdFk0AyOuF5szM93Us7hCr51Nkkn_SA81U9gqxDKacwrI1eOzfSlf9WQKulB8E0JD7Zo0oCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=KtJKpr1mmY_-CqfJ5mwV9kqohac4j7QsQzZ2c5gDbKVMDVYXtue50uw8Oa-fOvy8zkbK8SzbPVNVuvC__UDgbwGznMn8noPWKil3h0rxhBQaHUu0euoQH3taCQThnrfnmXDN1r1lK_i1kcAMNwoPtkK9ZuVC0JutZoEbrkVXQaO83nQmtxR260zBzg8iQx2RR5Qa25lROHpCe-SQkcc8z23sGHpPjcGBsthkQ_6wxbUBcL0XSYhJN4Wk-avznRf0REH94oNqNvXd_BtdFk0AyOuF5szM93Us7hCr51Nkkn_SA81U9gqxDKacwrI1eOzfSlf9WQKulB8E0JD7Zo0oCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Tpe4KCoOmPUf5nCGIYzE8AU9yLPt_KbSynsoh6NKtLxxE02JFl5wLx68eP4Zw4tqReQCHFbobOuzWMrnRv3mUhEFM3YyRT5woVyx_khg7UeKfJ3i9feD8FfQQ0pIoHnLmx3ipCSygBa3BuczHA-cCMbzVbOayW7DPZ2WVbjKtKaXEe6Q5C40nnG0dwgVt0b7fEWlcMwFDXPuqEGG2HKyYPYyNwvPScH3ezpwXzGQtdhtM42WztQtTkWe52lvO88eVCy53HAYvv5uWO1qd0aEYfROp-5qjH1atJhuajVUgYkdzemmO8XM4Mxi2pMP54zoLBruBuoIopTpR4yKY8FkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=Tpe4KCoOmPUf5nCGIYzE8AU9yLPt_KbSynsoh6NKtLxxE02JFl5wLx68eP4Zw4tqReQCHFbobOuzWMrnRv3mUhEFM3YyRT5woVyx_khg7UeKfJ3i9feD8FfQQ0pIoHnLmx3ipCSygBa3BuczHA-cCMbzVbOayW7DPZ2WVbjKtKaXEe6Q5C40nnG0dwgVt0b7fEWlcMwFDXPuqEGG2HKyYPYyNwvPScH3ezpwXzGQtdhtM42WztQtTkWe52lvO88eVCy53HAYvv5uWO1qd0aEYfROp-5qjH1atJhuajVUgYkdzemmO8XM4Mxi2pMP54zoLBruBuoIopTpR4yKY8FkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=UbkFT4RjvhU6-lH-PehZMtb2qRmTeDisvCkb4t2gv2EVkSC43z4ybpQroGj9hk6ICFs8-dUKtzRlkSaJp1i6-EHNjP07f7nY5_tvJjLBmk_X_-9R6yj6bXLvEbKJbk5znH9dXC7Q4mzl_Tm3cE8QFiw4eJZW3gDQWaLO2mWztlEpDs1Z3FPf-Hz2oK0pA4Bw9klacydmB74HY98PB3tyn34TmyKSXbZ5ZgBwXHC_4O1219cEBS43mdgUWw2VPInSUjXiIGm_9K-lKMYmcvp80b5rcCTEkfarSyp6usRwS2Yza1L300IiZQsh8DTDh5Izd5I_r9r30wN_NSjM1psu7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=UbkFT4RjvhU6-lH-PehZMtb2qRmTeDisvCkb4t2gv2EVkSC43z4ybpQroGj9hk6ICFs8-dUKtzRlkSaJp1i6-EHNjP07f7nY5_tvJjLBmk_X_-9R6yj6bXLvEbKJbk5znH9dXC7Q4mzl_Tm3cE8QFiw4eJZW3gDQWaLO2mWztlEpDs1Z3FPf-Hz2oK0pA4Bw9klacydmB74HY98PB3tyn34TmyKSXbZ5ZgBwXHC_4O1219cEBS43mdgUWw2VPInSUjXiIGm_9K-lKMYmcvp80b5rcCTEkfarSyp6usRwS2Yza1L300IiZQsh8DTDh5Izd5I_r9r30wN_NSjM1psu7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqK6_L6NEHll69thCNbiIluHwqOehWRjci0vUI6SOo57Oyv3XsIunTx6ObRFq72mkG8RynweTDGj0APstwNySUX6C8J7YfFxk11BBht-8Muk9kKRlhhSnpOYGabgbZGOttem6BkZW39pgSUkf91V6aRNRYALxZpkAHAhtA8kmkfyQ-hC3fjA75Ugl9gkfhM3I-56Y9-juj2jKddQdMbCdrUZBeOpiA8vwzVl_ShvEUrL90-LuI7aHSTSpgPfy7k7tFAgbERLtKssK-oaiRODYZuJObXE49HjDlJIfyYy7Juqd9a781bnuq0juvcHQ3_MzUCAxEKly0glTR8Kx5RVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp32YKCyz1PU2_d3SQrMLY2ln7RaYtq9LDTIsTLtv0J7vQoV8xhW-bMZYohQm_nj3eg3Rfg6_cc0hmX08luZKL_1_ys_s75wf2zue8N3vAW3gkbF7Vmg5yiWC3CNcunu6DTbMBvlAiWCRmzicPQ4A4ckVec-ygyldUnXhayw0VUiTEqm5cUxLi36RJnL8pQYKzWh_9LVm3-2oy4z5oWw6CyeSNQzsZkhh9QXvJstNxkFZu1Sxm0eqDpJikGST9va3L6D8EtpC0B7DxCAOgOEeiPhsimEKXMBpv0sUF6-VaeHSILDyDGGy5jLjd9OCAmhhHzr38EBJuKc1ayv9kgfnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=M_swo6XzdmtbCD-aSYYNaeWpYq6SsOWJxIRlCiZCzi6DRgX2yNn8qV7S-4-TOagApiHbrGiaMyrUrAsDWMEcG3Aa1D4Jo1ob3vGupyCjtnuWO-ZNE7V5zuYZChR-W5kWOokIBNSxMLK6xVXfuJlldVcXud9FNGdnaBk9nd6pcGWIT_3hJN5DgLjjtvmP6ASssNyvfnfxiv2PKHost2pLw9lmhToxszTnA-EZOaMIdUT90U0-50hvGsALN1USCb8Qo1kfaDi8rZ4OkqKXGPWXqJUWGDXpytdCfiSSaSnjzFuFJToO-T4RFcKd7tYRVrzbOMfdYtcuPXCQKAJwjku3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=M_swo6XzdmtbCD-aSYYNaeWpYq6SsOWJxIRlCiZCzi6DRgX2yNn8qV7S-4-TOagApiHbrGiaMyrUrAsDWMEcG3Aa1D4Jo1ob3vGupyCjtnuWO-ZNE7V5zuYZChR-W5kWOokIBNSxMLK6xVXfuJlldVcXud9FNGdnaBk9nd6pcGWIT_3hJN5DgLjjtvmP6ASssNyvfnfxiv2PKHost2pLw9lmhToxszTnA-EZOaMIdUT90U0-50hvGsALN1USCb8Qo1kfaDi8rZ4OkqKXGPWXqJUWGDXpytdCfiSSaSnjzFuFJToO-T4RFcKd7tYRVrzbOMfdYtcuPXCQKAJwjku3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGgDcNSk7ip1WNUQHjc-56WNfTEEE7kckxxJT7ZVejK4LOgpKom1R5KRI2nrQMGfj9gTsPu0xK61eu91G0pqukTIVJwDrapveUvxhNzp7Ogh8xYsXNPMNEv-7hcyMT-Y0ZCZ1_YypZAxDI8OPDroqpfPZgE_2EezkyrQH0eA8I6-72ij22aHe2Rhl7Eni4HYVhQmrqWbBPpmoNlzvfFibsuL6sMkOj7yCI-8LHduJQi_8b6h3mhUk7sMvjfwfx1oAlpqIcD4sCbfxp117t_xKtF3qbVHQrrpqdrj9uhaA4VnZnp86Sh_gbqire472lHyosxInKH8QnHXgnauR6cGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=dVirFVus1BkpUUsgJBZNqReZXosA_ihlg4EFoRZgEVNB1fq40pQKR2g-Xk5t2XSGml05wLRfVrCl_j-hzXDcbBeOCJC3IMo4jpf7_zQz1S2HMAjN0Cx7mdHKZECuwxJurCriivD34C9g556fMtYHJgi-B-nhtTM5E_dZsFxwbVmFhb7EETebLAOIo7rm6ca3wmyShLIo7FJcLEzZHupemeQzpL9AxhxLjy-5al1oAFOFxFuwPCooLbsckIonUuzwnKcDb1BrIRJSbUeDUUdBYH5Ra-dzAfDU-5BCR8EUkMemKAX-BCul70BmqRZUT2OxCpWx1i9lV2oeerH4sGxiHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=dVirFVus1BkpUUsgJBZNqReZXosA_ihlg4EFoRZgEVNB1fq40pQKR2g-Xk5t2XSGml05wLRfVrCl_j-hzXDcbBeOCJC3IMo4jpf7_zQz1S2HMAjN0Cx7mdHKZECuwxJurCriivD34C9g556fMtYHJgi-B-nhtTM5E_dZsFxwbVmFhb7EETebLAOIo7rm6ca3wmyShLIo7FJcLEzZHupemeQzpL9AxhxLjy-5al1oAFOFxFuwPCooLbsckIonUuzwnKcDb1BrIRJSbUeDUUdBYH5Ra-dzAfDU-5BCR8EUkMemKAX-BCul70BmqRZUT2OxCpWx1i9lV2oeerH4sGxiHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzCRUqeqQuHgmUMXsmOGaNQEpEf9D1P_63g64JRg2moId2maUNbaMX47PK6YNnLi3sALhuPd2WU7rBV0gmiQ_515-90rl4yGePjgcglKvJis10aLhnzGTPBTzOhi5JsWCSZcnekyHzr_gEWaQ4HTySXaG3hICnUjzh3zvTaP3UskeBMOI1YQ23lY-ozi1SBmUKuscGt6_7ItN34kJiQs8BaQugpiWQpDPvxMitTG8AklYFnpSU8bwwwEZxBAzI53bNgGkRYFM8iy2qMDZvQ8ky1DZ8mfVxdtnqoFM4udS8cbAXMtvrzll6aCNKY0kJkgI3eqJrquy0IqoOR3nC_scQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrWhHugtKN6sP51AMwjDGLQpciXtOGP1mMEm0qt8lqVlDXD3Pi6rmcL5fgNl5wvhKzXG43mdR16tpRET1e7qGJBl2EIjO-JYGVBhMhktM5fJKwv4RzQL67vhyXyMO_GKTkD9eP-37RS7m7Nx_0Ez_Pho13aZHfIO2XUb0QEYjsYCwRF7Q5Q5onh3kO5aSFmQdtfvxKdZ2OKdXJZF__qXwJ1cipJr7ABNPuDJAi9-4Ud6MB8xs7mT7B3-SW7C6IWm122J3LEvlW9Zc_S1aVzO5s0mD_MC3kIXj_nokOx_rMVgx2bgoksgT6bh82K3WcfUgG2SrNTnKXTM2X9U8YRiqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=p_eGaRFdqcIaGtjEFERCxyRVwHrUljuBQZEJkxZJUSPB56wyEoOO9hc3jxmY2FGXN9csCH70Ba0TsDZxQV7ukvn2uVMMrP-w-38K5tdJ0_0A0-sYs8aZb4r3kXlTuEj6k4jqo8-j-c955J6UNOga09YWRp_0niajmp2NMabKBNvWpIrGndq4V4wnW2ojVwGlexElWLBhECM_BBDtSe1YNhwEaqNh6Zzn1k9GK89xNDT-129uVBloaGT6IbJMxn6M_aTz88kG5ECP6c7UOTGoeaPdPrrZjPurc5RgJIOF4wfgmzxnU-1WnPjJ0y6fyxp3obmJxYvIq-iC7oQFNK7Tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=p_eGaRFdqcIaGtjEFERCxyRVwHrUljuBQZEJkxZJUSPB56wyEoOO9hc3jxmY2FGXN9csCH70Ba0TsDZxQV7ukvn2uVMMrP-w-38K5tdJ0_0A0-sYs8aZb4r3kXlTuEj6k4jqo8-j-c955J6UNOga09YWRp_0niajmp2NMabKBNvWpIrGndq4V4wnW2ojVwGlexElWLBhECM_BBDtSe1YNhwEaqNh6Zzn1k9GK89xNDT-129uVBloaGT6IbJMxn6M_aTz88kG5ECP6c7UOTGoeaPdPrrZjPurc5RgJIOF4wfgmzxnU-1WnPjJ0y6fyxp3obmJxYvIq-iC7oQFNK7Tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Lpt4Dk4C9Pn5SBK0VJj2xE0RF2U0_M3kMeyl9Ciq__yNYjO1qc1GuwbCjrpKQhfFON8JZwPtolS0NnlLbRSrGHPEaGkoL3Rtch-QzbVu8fnUbGSX8i562Wcj7BLv5uArVHlp9wDUUnQiEMdSujFKsQS9WvZ8QJI83RMd2_M5t9V9rxqjLJ_XcwIJIy-OBt2L8vMXbqFyFUmyypFIbhi3Oo__vSxoGD04n-tipZCygNshEZ0-jR-smSGMylYom4wTl5jpu6fnXKqHvs5UKlJphvX8TY4apLhT8p6CCrLLRl7RM-G8osVbfN-EMDlIeq91MpGCNLysRpbdmnMgE0J6qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=Lpt4Dk4C9Pn5SBK0VJj2xE0RF2U0_M3kMeyl9Ciq__yNYjO1qc1GuwbCjrpKQhfFON8JZwPtolS0NnlLbRSrGHPEaGkoL3Rtch-QzbVu8fnUbGSX8i562Wcj7BLv5uArVHlp9wDUUnQiEMdSujFKsQS9WvZ8QJI83RMd2_M5t9V9rxqjLJ_XcwIJIy-OBt2L8vMXbqFyFUmyypFIbhi3Oo__vSxoGD04n-tipZCygNshEZ0-jR-smSGMylYom4wTl5jpu6fnXKqHvs5UKlJphvX8TY4apLhT8p6CCrLLRl7RM-G8osVbfN-EMDlIeq91MpGCNLysRpbdmnMgE0J6qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqgLXBmtko6EMIFJEeapzmVcGJnlEXnbcnW-1rLCDlWlIpwEL8ASeH78yxFXHbV6KiZ2zDU4QIw3lIzdM1-uJcUa9rcKesIWYD_A26h3LaZ2R4fn0Dx1lK9GDOMZUpFOh1fNNCYRN_mG_ArN7MZrxKg_b4mKJpxRyFPtE4yhL2sWLzoNq_mDGpkZzpiTUNxYw3WoFiXierNtybL6HwyQ4uwuikN1o21Jk6Kf08udHEaWYkAztrIaT9OY_cxYztuKY5nHwIqWLbR6pN3NcnA8DajEYelU1Hbs1mIvoAJCc0UsEaVSHzL3U4uGePj3BfS5qgOwftTyFChh6lMEmsYDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvWVB5JCr2ASky8L4CqFA3sWwnSqU39CuSaWbp1961TADb2R6ou_ovPXOEZNPWNS9Gh4Binf4aRBnBb3XzSyiJHeSCiRwqIaMe_oN8t8tUtFBZFq8gXRIC5zByHxMm-Tol983FchQrzPZgb686FWKzW8YxBaB3f73hISTmubtnOg7jwoPz9rrfsybNv09prP44ezVlhbBmFk7lam4meGOEbhO6hWaerXX0d_mXQKd1eslytBhlarNMlo5H97fjQCxhYz5HVOPxA6milrCi38DWxL-B1jqkuF01Fxuz_pFK7BFXiR4QCcHgshPnoK-1Zzh6HNqaIGYi9_Cgdj8vsEFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH1i-vRexLemYArexI2Bqtsm1qWogYcjHrgjijlcCV8dWQXH4coqilcdtAyG1syeQAgzm4Fd0m4pyAerTDq6h0hNHXSUd-X8u2t4KywuQmg5AhrHdf1oebm_VArJrYNYrnULK4MTVByzBOS6JhYGFF-ScjQc1-2ZRb0DZpO6JXAvH-9RJ4wUq7mCkSaw0zqcd0rCluncb_Liz5Geua_2sUJy8dU8IODoRVAqYHUbL2HeLqrmBUF3PU-UT4TMuce3ggG1tTj5jmlxy1_TU6RBvl9q-I45GLH-yqS443SdUHYJ1tEysvLynu7-5RqyqNUhm__BJ7uE_LOdItREORIKeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=GtYPercvLIugJkEmtN3O2XYOldLi-gIJz0aspVcXCf0gfi8iZ8lOSvKYmTpfRNmkHR-5EzWmbYNrOlWCAC36dUwaU72nKeQiM-Urf1bddrqE61EcUgMKxPBZwiktvuH8M_VE7jhIWpV4vETA4zt_F9u0sNrf13syxGGhxttEDFhBpV6afrOU7ncBrcVTsDbFMKZIbFeoa40NycMWnR8pTztAZ-LuhrB5UKPReRFUoJHGb8j_mIjBZr-sKKAZtkJWCLD-73XnkVYVukT5f-gq2SyGV3YsOOKbS7zSRZnTrTL0ucGuEhrOJyEZqHH4UpuYcN8FRa1wArGw93i0IQppSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=GtYPercvLIugJkEmtN3O2XYOldLi-gIJz0aspVcXCf0gfi8iZ8lOSvKYmTpfRNmkHR-5EzWmbYNrOlWCAC36dUwaU72nKeQiM-Urf1bddrqE61EcUgMKxPBZwiktvuH8M_VE7jhIWpV4vETA4zt_F9u0sNrf13syxGGhxttEDFhBpV6afrOU7ncBrcVTsDbFMKZIbFeoa40NycMWnR8pTztAZ-LuhrB5UKPReRFUoJHGb8j_mIjBZr-sKKAZtkJWCLD-73XnkVYVukT5f-gq2SyGV3YsOOKbS7zSRZnTrTL0ucGuEhrOJyEZqHH4UpuYcN8FRa1wArGw93i0IQppSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybl2lIfVruKyRuJfpgm7YDbwFhsc-_5AyKqtJdhkG59cSJSpOkYPVOBaAwz5iXUUqmBRxK-oBtEVPwwEPZP2W_p0qFzVzQzMXoEkhOTSlw5mQDioxzhFQjcQbiajR_NI0xy0yLZYUMMWVir3w0tH7ShVB4I7S7eAjimzqQP58TKpGuoYut7uM0ibxTnkvuRFY0_Tx0__Iu8fn154VwBQMUgquN8UbzEbQgJoPwKUI2VYV8QH9jYc9epZ4EbA3VF_UhczZNq9zlBR9q5wskuunuo_eQD6UPlE7l2N0B8WzGf0WxTGewvt9ySB6ee2pEQrikfiXes_kp_dnqVh-4FnEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYsBkj7_FxmH82p_9A6DWR6cK43h3ly46JNRv7KIpF1vdxwlIQtugN9odagC32NiXADzdYFnDWFa3BLjNmSyhIBoWaGF2kNRd9SwXbbvJ8B_N56e7H6pizqQSKaI-V-lOYm3cm7f8sEou06jB-zOZU3wQ0_h-oqfklZsNN93Z9oaoDTirnUpPpEW6E4LXEdyePUb4LMYijubaLqGFr0XnFQ3bRYzsS1mfka4MaL4lsV3bT2FwvQ0entTz8vZSSD52OzTMFymYSSFzpC8PqVHgEi-aKJCkCR0NvnKF-TPfXzArU3DYWXKNr0RC9ohoVAduDc90xG9DN2uMo3Hp7jGfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqhGYgkdotc9DbBVi-_s8tx2nIMARwYb13WJggLy-2HlSMmKq3AGyv02R4pbsy9X-kgUEf3lCGNokx5GrBZgpgAuAMXPU0Fop8Oy81YGHHm1HF2FWph3ijoxXEAfgwsi1FmosMOGgcwjt3QlM61nm3KHZeSJQoKvYNLM2j-D5sxCs4nLkkvvtyw83h_SGLOtXaBj8ZHdnx2Q6Leiklhu-J358ag8TFxp8ieGd943iwvDOiwe7tw1bWAfqzwuUYuxbq_OUzNDEsyaUdzpUlOCLN_pRtktrUFKp4MWUng0QOE5Gc8FzPtyLodtXNiYhWVvZnsRnStZWyDGMPDd35LAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZsSAQWSy1_t1F8IVTgx2n7qOIp8qiMEw7uV2cqvNYuz3qN1SyynVXFcKXViysGaPMHlRahAIhioe0sxZZtW_Ned-GoesBpE-zZLHP4V58QvMOob1C82YxBhJ0DsvU-groRwQzNzm5rarcbVHNpc_L7LKB_Cv736DNtktrh06JL7OBwoXDD0qbT4zdvOjFTCfnY6VGPLUym50mUTPkKCBJpDAbH0RxaZEghWyX2vdun6kmDIxoDMO86cEaRqr8zhJgL9o_MhJARXE5Mmj3OqkT13kUcoCIA8iDbJGakKQ1moRpCp3BymORkITBWc7wa_bLdY6tkrSPBhkWe0xu-1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=CcyLZI4Cg97gtzPT8vum7F_gi9ck_I7ek8JC7xzPEzNSm4-qbA_WCLf_3HcWSyDiWBCIAcGSFNL89vD5mUd8BlwVxe-YzFeB_ZOH9IOMAQQ2vNSf9xSf9qoKXv2bTrFU02bhlqdOreXbUdn_r7mUwMl39uHgMKW-FeQIlzVkk7T06e7kfKEtsJiPQLFEyy5FQh9-nfcfAGKbrvPnY7ASV8_xIPfS3G4B0EY4BzQuusEPVtxP1hvtphxFG4ZpnHZQ_QJGkTf9q-nPtq5axKhBcX_z-Dcurazu73GizvIuMaGC8jet53vQY795ypuARYQHi6LFb2nEj9RZ9P7DMle1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=CcyLZI4Cg97gtzPT8vum7F_gi9ck_I7ek8JC7xzPEzNSm4-qbA_WCLf_3HcWSyDiWBCIAcGSFNL89vD5mUd8BlwVxe-YzFeB_ZOH9IOMAQQ2vNSf9xSf9qoKXv2bTrFU02bhlqdOreXbUdn_r7mUwMl39uHgMKW-FeQIlzVkk7T06e7kfKEtsJiPQLFEyy5FQh9-nfcfAGKbrvPnY7ASV8_xIPfS3G4B0EY4BzQuusEPVtxP1hvtphxFG4ZpnHZQ_QJGkTf9q-nPtq5axKhBcX_z-Dcurazu73GizvIuMaGC8jet53vQY795ypuARYQHi6LFb2nEj9RZ9P7DMle1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL01-gkCDeE4B2_4fu36zuQ56MaoK1Ah655C_TaA5iqx0SYXoXvcN0_3qVkPSSmgJPb6AiO5QdMyAwXGvbEOUHXFaKj27YhZVHc28pyjK0LeyJfmc7AsKZ32J1Pqli8seGoQ9-4pV9qiS727yU5fIFV7VZhJ5DmKA-pQ-fr9UPmRLYUA1nDeUNT_YChWt_VLF0oiZVFtZJKwIrT5cx0-zdr-miQ-i2nQCJZw8qzUXDPORR506Mmy5s_T0-Vfvssz8QMxuy6jj8haNdmMFpxmORlaQT_bu1HNv-jTz2vZBHAtNiZjJ4OoA7Yu5h33_E5KjQWFfnYCs1T__cZtpBav4g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=h7NqwrLTVubYp-4Gm4OOGBLm6fKuKTLd6l1YyI9UxNdjXlml76fHDk2jEM-O4UiamppsW9pi_Ww2823NNr6Dba9y4uhdbCoa7Wn7TVydP3_ydqOL4vtleRIPxu2Iz-o_UrPVCQQRtkw5MjFLZYDI1ZBj5xYK_pisl4Qa-EjcKbKO3farxCUfuTqMDJpjPxS3Zoobaclr1qFJXjHsFhyOsIALln7FBoi4m0NYjaQ8QS2XBKaGh45UG1WyfL6h1heYDB7M43wmclM26VknbtGhGpdeE3qORyim9aPAxEk2rmYfDUjRZrMLpYAhTqwd4BSchkkNZgpCvjy5wNtESbo56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=h7NqwrLTVubYp-4Gm4OOGBLm6fKuKTLd6l1YyI9UxNdjXlml76fHDk2jEM-O4UiamppsW9pi_Ww2823NNr6Dba9y4uhdbCoa7Wn7TVydP3_ydqOL4vtleRIPxu2Iz-o_UrPVCQQRtkw5MjFLZYDI1ZBj5xYK_pisl4Qa-EjcKbKO3farxCUfuTqMDJpjPxS3Zoobaclr1qFJXjHsFhyOsIALln7FBoi4m0NYjaQ8QS2XBKaGh45UG1WyfL6h1heYDB7M43wmclM26VknbtGhGpdeE3qORyim9aPAxEk2rmYfDUjRZrMLpYAhTqwd4BSchkkNZgpCvjy5wNtESbo56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwVA0DdeYFoqTY6ykdyPVtinZGYI6xCNvucMxWOI5znI_W6JKOpkDzorF6M9VTagWhcMnTvh7tkTLniROihmuYIXZl5-09-lc3VJZ7Xza96D40xRH98U8abvcSwAezbPEzsFHdWbB-slp2IaZNNk_0IZJSX_4vD-d6vltndsXVPhlySu6vSVlMLTlcbURSWYdHRyez2v1b2cPg85bEHBqPy2GHbwqAK1Z0NzamjaIWIQ8b_CTSEXMlKvCp9YKp0ebsHlG7SEpkzWfTOt0jQkoY4yUtBq_MA06akMj8MDecUiAYOb1C5GU2YwhKIfWoKfVQSAwRFfJqZWl7t3O64OmQ.jpg" alt="photo" loading="lazy"/></div>
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
