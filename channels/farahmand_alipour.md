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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX2Em57BlV8AHrCHXvQjzSsDaWeE202zmSRAsTfJuGGzQsv-Jh8ge2zHT2DcmIyIgNLjtjcYMybGx2PhoCZpj3sozzZm_mgvUjOxPzGgihLVSe75kGM6KWfLDcqYDK_BsrdkhA5tJtnBE2xykOk0Rp_drzY3sOFcgnoAiWQsNXRD_DbrNC4y1rOgPYrMakY8FlT2ApJlTfrV7P3sqomo1OLUyErcB6gxvreLz5gedLYyhSzszeXYbKAukjh8Aytr0LRJTUgqev5ZiX8AB3rSUdDo5Jfh98HVtj2ccTs-LOj7G-2_DR1jgqjPwmhI_NFCkeISF_fstFLoSOXSasXSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlrkF_uOBjBspnUxnru03JVdiZqjQE52T0JcY7tLPb6LKL9R4FDdVhkB7LHiKfN0dNqLjiHhrOrgPfmi_XURGCGNigvtLEXDu81YOXotODcWekauSIRQQGKHeJ3QLRXTZ6fP7-SdAvhEv1C6ZzI-yCwGQGvar3H20Yum9mOpwXLdfngYwhcp_yQrHhk_kfmJ7j96-EOwnf7uhyeQVHyVClCFFPdAFApFsxNjevfG4HIz9OEu5GahLVHXnTquka-JqaZkd_4wXfh1Lt8So1PSDcPBYbu5hSRiIHZucwzzJJq1guwsoR9T6ru7P22gb-nt-r4lm2rX6Gj4LRV4LHoV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=PX3zHDXBqQEXd4oLvAo1UmUEkjo2iqRBfsAKrJidrJsi0y8Hi8xTOWD0cxbXjRgaCww4T7pUvjbhotVekWSPHeX78lQXRvKUKDp-g7fjp1O7IyEKtph-n5-sY-Isra4QVsj5WbCD27oPRWtH-VcKepqijtW0BY7KHeoXmAfDIMciMEox5HfQm_YRMiUhOaaMVhv8Ay7hTMYlGIf4RrHqe8IUWpOSKSWaflnUCPvb_i0Ctj57P6XM92TEXNLx-mZRWb_tD06yS06azx15woW4uMSyxMEUPoa9dgcJ1K8JS_mtBntjFYI65qZU_pWfzs-GcnogMytjxfQFN78op_0Jxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=SxPnhcOA_Ab1TO9oIDEk7ybUBFSjeyigopKpBXGtZGP0iO8SgPOuL7P6P9KlBTRbBV0GSC9tSsc6n4L1ReckjtsEB3VH_ik3neyPCnfM5LdBZXyAK4mlTEgE6V-UO8esp8On-ybHK5Msdqu5BClcfxtgErM3VgXy0BXE2HXvL6TfcxSYPlRybPF6AWN0gwL1gLbzsBjR5CZPZhlA5FRRUrtYM4YL4wFHPZA-WPtRq5I9Y2SEnYCVNuHdZk5p-Ax7Ff5u5T7WQw5CT2IcU04p7LMmdKavrHh8RTICq9RGpY50WVEtxkmkysx7ZmFPtQYIYyeuF5RvF6fccBrRi4VBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi9io86Op95OGkoodVGRmLU3JqldejETKqeEaUeJ7ubKoTMmxaYJdJOd14AF7aUc0pS-FMXOHfIt1pbx-7v_9R0WbCVF2NnVKUmGIPfBI76-Rvqlhs_9aCYqFTNN2-PXR4mdZACdF_nRiuanKKluJG_cZP0AhtPPOHbRl08q11xIV17rrQBpVIh0rfm3ihDeWjNuIGz9RY6dhnuTObPna63n3EYlJkgDpp1w9dbZUfgGFE-zZSevUBEAWt3w1xBT9mYreejg00D8to2OofUi1tZmJnNZhKNxqfd04abFuwtn42WNOWxSkirBwI7fF-loYDqsnJPNqpPVqyyTughrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPv4zlnOPtBcyxvpNu53dEjnxLCY9FSYzpUGEa8o5G8wPV0waLcREqAJZtb1H5HCsKlWz-gXL0OF4KqsWCGj7jngJOBuZuZWxloo5L8fZtG3v2qHg17S8uwjZsitxOAPoa4XMtFpyqC-5HGc1BieB5QExO531_P-kz4MVKsbVbm2oc8Verf1I5Pg0478VUh0zrmwYLcEH-Cq-fA_VjyRuRAYfXBbx6pY9ulPF4GhZAdIghMVarN_zC2toQ3ZjtBS2_My7SIOPFYDYPEb24BaAGy4Dk--6j2r7KBlllinWIOBj-G2ttarumz_-_6uc9xvCpFnU2CWkG162nSZHZ0SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3z67X9JkE0iA6VGYTVb7vqyZUkVjtXzKoYKxqA9JjfZGG5BhKzYtjBpJkcJsb02p0Ud77sD4jGuW6DVr4XLmmMSUPfX0Cu1Rq6zDp7kSGLEmlkSwDYwlPcVeLOmBkCR3FE92fN5_TgNtsEE8StX-h2D3EvnXXis_Gk_Lwyd-CQhBCOWxcpmpLiCyATmOQxW4b5xL45RmMoIQkMWhmaMFbflpwE3xjTw5rlrpjm7Qw9zekNmreEJhEyI6R-2zIAXOPz7HOXBVcPfAcBWwCZx0BTwK0NRGgXKGVFIB6dqlNXeXxqq3vMH6vI6DF7i-rTrD24QASs3zFlZo-t7KpW1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScwO_3xK60fcKFljmgBJYNV4e4DxBgqzEO1uLenk2HPvA7TS5onQn5rZA_X2yNFwcZsHXBsbUikXWCTpD9Dr1bu9JtbtVedrgMQI9QZmvCLi_PztZ6ukdWeP28RVTYs88n-DsmIQ5n_V6Q0rhUG7HnPbRNGF1ZOungfj6kIo9mnYIjjQy8jshqJrI5xfyrAB3nKIrxWKv6FCSfeBJ914TRN8xF08ZwcpvygjimUi9h5waxF8iLjah4-GFvuCGZuDM2YdSyRHbpCg0zaYXAeVt7Z3CMkGrAUPdK886X9d2YhCYO6u2zrCJiFyY-7JMqw6eW2Hq7YRWaeKmdo_W9xGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3bxx4fxSx63_FfohgEqFjE1qGXeTDA3PbgbUXfn4-UBWE2tNwtZpY94ILw_HFCpqV7gDm3U4qyrTJW5URhuOqlkFeXrX0msXySBvg3VzD1230_-Ky0eoCs6ROVCXB9yEqoxkBhT9IDTTaxuRapMh9WoVAFXVa8R8sazgR4khfsfc4kcWhD4G3fe4VRhKnJXsgjWJqnbEHE0QbKwE1m76EHzHQ282hdhodCQ3QGwSwwtdsJsVG9Mo6mO7LCXniobGjJpBYTnlr4l-RS8PeVcDPWe58b-aCKLB1-TRzymFHshMCQrVLVtPMllBtxnnLo3bolui9VpDrC0FUrH-nitKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMEJDHImA3LZAKp0PlrLbwyqddPAs-Nx8LbBSYrTVEqk23uh8oppLDPO-HYR-MOlGIzDmRfs-ftdSEVHW9-1G1UZQM0FGPVxRIQz2GfdVji1to_LDR-UkVXAM3lFNvbITVwojZpIy4C7prwsBuGcV8WcAu9xUihIkvGcZHK4YU_FOz8QP3ifMaMLHhA74iSaGQmI9cLQf8d_kx3Uj1RZaufuYiLQZEOLgKgQEQryLmPjDS1hQi3RShukQZ7_wjDwZ6ZijgCHNatQ_MDjeQbcP9Tysr2yJh-G8xzdobbrigcfzNhDiF6vrjxML2O-g2gkFjubhaSgF66LIuL-WQbElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYnfPFsRRGpKzNNfc8YAodSzpW0H_a4thhaeJ_XXbdUtteXIyJye54Rvd0MhzD5SIhc_I_4ReovGtP9fdpMdQG_T6SXAOJCSQhJDXf0FPepfXTQTuIdkaVtZkgyFia6jPmu_zSkL2siOFaRRmhMX0IRz5Wq9itjlC4FyOVDD4LGYiiEu-hXgZ6xEDzhObUaQRsYEjIieVIZmSY8oPHs9FUt3SXTII_D-bFZWAZiXWxSSorVS4e_K6MO042IcPNZznsnbIa07XJvLMYhdT_HWMSnRNGgbFbXLsvzNsehd8J1UdkbieK68wEqaWYsUzoYsNArgmdkkh1KGcgOSLSoUVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnzq-SJCeK5iUsRqrtzeIl9PiPEA8q3oSzYdnbVRLY80icvC_4LTQciHrnV9pRKte7WeyE-jBbb7S46Bhhx8Tuf25UUn-H8UrM2QSzbH9tgN7ATXL_hE8NlfaCv8jXLQ-QZlxogfOW5npf4VGrKBt4wovK8rC7H3y4Aak66zjJteOhkmZQGcBL0iyKnTau4tjoTyYssEh_wu5vzDhg_G47-vDe4dl1y58G3MUmn-zfxX0DCeTHV6yT4SSVYNg9lOZM0NYQxG1q3YwJpqAgiFwQ6A0qSXw5dtPjrVLT2DRu2pTeto4sAKY1rDdAdPhW5d20-XCq0zuWNuZ0o8rtW-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvabggeV_gp5uCRBhKTWs-Ue7yxOdq_rfaAOvs2UrdfEteqQjXhE79lev_iS3wcYrEYbbHceY38H5CKlIjE0ZQ5PByez3fvvNvENYL3xFw56HtNdE0H37mOJ_IG2wmtb4my_GBs7zEnlnky2Vx7RbB7Leir6DWzCQ-TsdYmtJZoFoDIuonUYYtxUs0bZV6xIXj-HQARCXDUVW87GtKVKrRm8L-bx5DDclgfLkpUV8g4i6ZCBxPTs46o22Gn9nO9CaIvMaJaBchZIOyuyYkC7xja0G_LV_lC6brjsU9XPuUSsOv2-Lka37BFRgz1MpvtqBo02kRp7vE9u5I2ZHdnvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkWDD8rY5G4nSdXYwW2TdbC0X93oyNnIstH5hwDH2iyhDhujGBIqXTR5dvrDHfL-1VY8eXjMxUgsCwIPnIm8pS-k0Ep-BPMRDrvRlCR9A6-wz68Q_L-TbBs9QIZbLCQ3EEC9g2LQKU-VbssvD2Wq7o2i8ynJqXx1m7A83swoqqK0tWd2augq-dLFWjH2OmGpTbvdljlCgh0E1iJKIZoSykjf3Sv6urKo88iH9asobAHH6kUKZWBD1EEcRqTWpjKBtAxRtydDRWlFfLApnE4l7xaFLFa_ux9TPAmMtN2tHmY0rIbobhpMzGU0EEP3ZnuVpoZeV1v_qOJONCxpVnzhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq9tfr9ooPoEpSVExNRXoTSfCi99IMOf43EUTZkyDnZJ1VEqhOs4ICgESZC3HQ0v5oUWv7MdlQKkNGMO0ovUwgHlIRpGmcF4E8DlOqYXizKzp9UyL1Ygkf3yjSRwQzumloGU3INOSlD2aDlYdXgQ1MyuYPKyNGclZub7XjpYRsVmXGDMHOOK00dDUArt6W9XI-sTMlaMfIwR0skCWBi_ty4nU1L51Mcwyd2F9O0tfXn5Na28Sk41vDRl9s2ujcxhwgKqJl9q5uuG0dFXFerU69EqEkUMwPDNttQv27Ozi8P0huhI7tO8gDeBQthISpM7rZBz1DjDBNuj-8FGeVrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIY4IQfe_-jkn7hX0ZFA17nUWwMhxDDZ8t5qK1EbO3GuMi5nsJhgVS5PkAralxHLinuSLgFLoQ0qoTIsAns470aozIMKynerLLRoGDAdCvsIhbR8FeB8pU2cDHrUDjeX8Qn2nX1Y2B0U7Y33CCEULPlPSap5fCb_eCa3ezQOxJF4Jxrlc8tAEf3M99cEtnCyRyGP2WDYib8tG-Qx0vh8QJXSMmaBovXRSk2vURFQvh-Ca70ATLxUnjGvEmRMsakCEF7HksgHL1da3YfyYQkSx8khSl9BFf40p9ZOn5f98fQ0xWG1Eav2qpoLEb2IvTynju_zNSQiGFPOjZSe5lLGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2DtUpzGdWY0GV2cSmk1McW6cvdbfdmPJiiiS8zTkkW6fhbu196P1UDQQtauzrEKcIPWV_JuH3M-MFRrMrvFfeBB7oVr3Xe16zbOK_EqrnwP3QEdV-WyxQ4_PCAQblw_4kfw6cVodE92lsiulQNl8kjCJmwQyhrf83vqKxyrG2ieF9xfDdN5uL-flrcXmAEStfZhUc7H_0ceBHvgeqf-3Hza7on4FBj4hKAjCenXtrtvX3-9VdU4VKOPT6S6HtJ1otjzA1tjGRnriMIRLvQU4bQzi6AZoul9rbwwoqT8PUyorjL9kacOzXqR9f0GU1i2KMfeHA-yEVywDJUYlev5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKXjOLPD5FFiyz-o_xtpWa45pG5bo7x9h8G1P9BeGvaNnGS-Z3QL5sfLqRllpadejhBS42FFebDPK4NhA2wlNhKyDdlNRug3VkJo1xtLlb-SLGGuc8ocU5LhVjuayG8hRogDPVnIzAIuuBfxkFvSAmalevfDpxoQ566V0IviVeg10DJWdSpzQNqVV-OFJOyjj6eVPrE00HJd2gvbrMItmn4ZqBQRh6GabeVk40xTcjEx771bFBGjHBli72Odxx6c256jGHQB8TLEJA-B4gqKAI_dJwgUXmJVxDQdmwWchYQBNTrUVc4lv03zu-WEy9UIQ-TH-EImUJoiSYdZ9JIcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=LRi882xoZXhRy3nBvc5Ov-PlQZnW1tkYedhaxWdpdHyQcTq5Ce4290BEQXbihBFzk7jivdTgrT-X3Ua3I0XpllWTM_RapVfdGAA6AmNYCIio6Z0_-QdeI3Sse4HOgUumTZnu6zKQnOLDH2-mPyoxEUtQDRU22NC0E1X_X3Bairo2CRjemgqHXbs9sQr-lyohtDq2ULS_kk5-OBUrxuahv2fe5TzqtiW7G6JmME2ZVGNn8D6E3fy-yiGTEb7C9AulKaNeCPVYEdXS0GLlYmSJhOuarNtC3yDQG4n8a6HdUpcveVZu5k-2STnqBgqcZKC8_DxRoR0rgrsXz1vh5obB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=LRi882xoZXhRy3nBvc5Ov-PlQZnW1tkYedhaxWdpdHyQcTq5Ce4290BEQXbihBFzk7jivdTgrT-X3Ua3I0XpllWTM_RapVfdGAA6AmNYCIio6Z0_-QdeI3Sse4HOgUumTZnu6zKQnOLDH2-mPyoxEUtQDRU22NC0E1X_X3Bairo2CRjemgqHXbs9sQr-lyohtDq2ULS_kk5-OBUrxuahv2fe5TzqtiW7G6JmME2ZVGNn8D6E3fy-yiGTEb7C9AulKaNeCPVYEdXS0GLlYmSJhOuarNtC3yDQG4n8a6HdUpcveVZu5k-2STnqBgqcZKC8_DxRoR0rgrsXz1vh5obB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwvMxzVNbfy_GBpcDdZB669THQk8zlUJMaY3CNQWgNu8NLapporMSqo2JVpubZivI53QP8txeDRKgu--P84M9wVTyX-wiCYYPLJe60ed-car9HFpTRwTpJKcyxaCtR09P2thEI995QK2-6RqfT4uSbpgKvkkDodJFloD3Gz0JHlr4HzYSnygiGb1fjjfMvkEO9L5sYCoZ7vY2i_HD7lEMqm6OYCkpxp8Po0gzIh2WARoue3mhF6lG3nLwFYOBvnm5doWjKhwj7g5O5HxSd3q0VPMeGEb5ll862fmk-QqX6LSal5JHKF8PnbAsZBAY14MWBbtHWoHkqeaf5XmbNd0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=HYYhcfvbMTRMIi1u-k7NxeW0pBdd7imkOj_f52kXdwXEzhRyoon_AsdDUEItHofuvvficSYlo4P1C48dTV8w7YrTEpxSc3gFJbNxGmcJT2tkX0qgokKQTQ3T_7StKumR47IMqb1e8KjJ_C6x8kcd59zve4gxJ0AbDzpPJ920YdF_JWO4s7MvvAGIykBAVAIqZpxBtETrHyT9amPXxuTM9vAaHuBHQgpVv8bFCd0UlK9JUM2ohLEW0P27iSOrQyluGEWHaZw_BAYoh3Qo_hKH7KWN7m0vSWNqit1bXLBkHfdKOeAFrtr27PeBo-PUcBcNFCj105P88UMc9mtKn9bYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=HYYhcfvbMTRMIi1u-k7NxeW0pBdd7imkOj_f52kXdwXEzhRyoon_AsdDUEItHofuvvficSYlo4P1C48dTV8w7YrTEpxSc3gFJbNxGmcJT2tkX0qgokKQTQ3T_7StKumR47IMqb1e8KjJ_C6x8kcd59zve4gxJ0AbDzpPJ920YdF_JWO4s7MvvAGIykBAVAIqZpxBtETrHyT9amPXxuTM9vAaHuBHQgpVv8bFCd0UlK9JUM2ohLEW0P27iSOrQyluGEWHaZw_BAYoh3Qo_hKH7KWN7m0vSWNqit1bXLBkHfdKOeAFrtr27PeBo-PUcBcNFCj105P88UMc9mtKn9bYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=fQZMAppvIRnmh3_yYnplmIKHYyGUrgQMhorVMDrSk3KOWpidH4bsATk8WGa0_mRx50OYQ-AbTbKRfUPHLkIU3bs5af0F8Q0hytlo-kDcwvp9s9JemiB7Utue7qyGbCByx5RWhHDne5LHSpd-Aqw5MHANv7heY1xaPwycR19VTkrTUTwVbk3t-pVtZnxr85PLQOjHLx3XDAg5Q__TiOuADbw9AaI_U8L69vn5ijjXO-CJYZzR4XHsGToqiZcabYCAgSeRqtfnQ4ZU0ERWOcBSPP1--gy5hLsY4AWqYhZ-jz6ozgW6DWCTqrnD5cnRF0hkmDUrcvcisVgREfT7BsSorQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=fQZMAppvIRnmh3_yYnplmIKHYyGUrgQMhorVMDrSk3KOWpidH4bsATk8WGa0_mRx50OYQ-AbTbKRfUPHLkIU3bs5af0F8Q0hytlo-kDcwvp9s9JemiB7Utue7qyGbCByx5RWhHDne5LHSpd-Aqw5MHANv7heY1xaPwycR19VTkrTUTwVbk3t-pVtZnxr85PLQOjHLx3XDAg5Q__TiOuADbw9AaI_U8L69vn5ijjXO-CJYZzR4XHsGToqiZcabYCAgSeRqtfnQ4ZU0ERWOcBSPP1--gy5hLsY4AWqYhZ-jz6ozgW6DWCTqrnD5cnRF0hkmDUrcvcisVgREfT7BsSorQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6pbu68kxme8WpckZUmBwIHyJpINcIVjVVyJH7YS0EFV2zaNClfbqsaAsPyW-wuQILEGNVKtVYm8AQJ4GGTCZnT18LEyRI998HjQkBaeUMNt5vpGH1H4PrJDATFInbe7W-dYjPBj1YTN29p2imbMrZSUCaYvDtnzoEKS6oT9M6lekIX_t0YZf8zupvRJgBUwkhO843Pdg4rdPtSWd0IJF2J10K3RSEO1CsEOk42SLBT8_rzKFLUAp0S3MfrCKcTSeqYmSNQ9G_PELKU1Y0rrTKi2Qwmhk7YFCfEcy9wI7NtydQcsd893M_j-5C4aC4b588lbRkoO6MKYsJ_KVhtrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=i-glj-vWKlce-4RXf7b2rxHPqA6pNiN7jTOgC4WDCNdjTShF7iFRr_qGjkjLn4vrQVvQ55oN1epfmgZYx0C928n30aW7hp_4RX873mjIuU9AnqA8vie1IizC8fte8UmmIwlJjglK5UNtx7btLf9BLEUp2ngOTSQSnFDPgulIWr6pEZXNuGlJHMk7Hw0x26wL190PYokQwignyd0rkPaGVdlYaIW4rG9gwBwMNBP5sFmc21sfTQuLn0GSCHXW8gAl3ZzyCFgXEpCT6pPmLABWgeithMlEXDCpAXFxDF_weLGVpHhmAxd5NZqbuGkfeNeWw4LTX-1KnVKrbL34Ek9ROw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=i-glj-vWKlce-4RXf7b2rxHPqA6pNiN7jTOgC4WDCNdjTShF7iFRr_qGjkjLn4vrQVvQ55oN1epfmgZYx0C928n30aW7hp_4RX873mjIuU9AnqA8vie1IizC8fte8UmmIwlJjglK5UNtx7btLf9BLEUp2ngOTSQSnFDPgulIWr6pEZXNuGlJHMk7Hw0x26wL190PYokQwignyd0rkPaGVdlYaIW4rG9gwBwMNBP5sFmc21sfTQuLn0GSCHXW8gAl3ZzyCFgXEpCT6pPmLABWgeithMlEXDCpAXFxDF_weLGVpHhmAxd5NZqbuGkfeNeWw4LTX-1KnVKrbL34Ek9ROw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssY2Zi083xzm8VKntDH2Uuag1DJ0z_ahC2mPUTAv6CRlOhmw-QpbDnRMriGZEaPXrBKQWDGTGCn1Jz8GY27XINfAmXeakK6qMr_-yt5KxgLfg5AH4uBjUMOOmcuGmFKujRlBwLK4QVLKH1_YgljtxCvgPOZv46HBP9v3gz4IApz9P9mwOe90uvhwnJkeh2qOuxh758NB2eSC7EuLoeWndDKHD0AOTsIJIfeKK6yOQrK1x4SIYVfKPLJPXfKMhBFKNxFh2J7KNsWsb5MsUqRXVJenjH-Si22WubD1RWgCpdhOWrTi4I1y-sBGCMeFRIFl_QifV-DbPiln953yAiHfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snW7P0HrANw1S0hGTZMQ6_JMf1-kMSGvAggnnzsitHCNGRZjZE_AU6epiNbPO1nb7aaxL9vbMkBZbdL-ruYhJC4SsyVsEAIzeHJ5ubrNuMRdd3DIanxkIqaypeyQTj5k4EgZ9pMdzWHgP1TUU6yA3zBrQD0I0454AmGcffGYFPDHK-Z9xJ7qxbmLCRS8toY5UR2UpOk109euvvE7pl-ZCdtLel0FYhVmQkIj5F6SfyuRAFxI36Y2qi4xGblFmvrBWHqzss6kcNa4QxB2ChzGzHniUadKaoAWh44xKVacHDEhMbIzRMXeKYbFPMzSE7GXpRNuFF5mrc68G2mOXvSGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgigfVYoL6ybLFbtVkkWfLtBf-JgHnO1v2mQBBSqp0r593o_Q5Xt1GPkZ5MyxcD6P7vCvLw25xDraa6obPXgpAHjKHqxt5wjUKTJ_8orYlXUuF9QiYVWmIHw_xe5tXfFrrJZbQewbPU0_4e-S4tTju-4VmeIh_TlUMtjzWO7MsjdPlU1z9tItBnjBcFulOaz6QcAPf84FxvLzcj7bH2GunhsRegdTIO4wtU4T_WZLoM4tmO6e_vABMxd-CYizfIrYVz_bLQZoojcv9aUSODRvR0A9IfroTNu4N4MrWtikECDsq6_TQ0A0VEfFQskjV4wIiaJKg4TaqATReMWIlpaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK6W9SUnRJ3BmI7Z3UtaGcE_eUTaCmKJtmbkc97RyCH6LkovGzSts7ChAKuRQ9ozVHd2z4nIqMvk8eE574sHioncFEWqkE3eNQdAHrSbIWTEirezMR--_fCGzFX2jMoMWjMHIvFMQVKSvYn4m5FsmhYpqERT9eQyWBK9nRIk2ezB0wQfhjr4ElvkOFlUhgrHCgrH9DVorAINPq_t3RFm4bV01rFrKchFV4_63nlqxnSHCzvmWs2W1LE6aOWf1fWu1l_eSRKQaTK4S-keIniVG-Jba5Ew9bFKEC_Wbxg6Gt7K3jFQs6sURgLpPSLwegBMt0cfGlI2sKQa0DPfD27-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=d3UjSwtz59S4ze7HmykNuZYPc3li07MDlPexwziar5WzdZ27l0OPevRYgDe2JknIHVvleWc0AxWf4yuk-k3YmfA3gdMcgjr2pVKU4IYCqn16LYMGEe_jlHx7n_JjHBIDZexgx8RKFRRLRi-yMGWRV4HVKGHeFVwjfB1LzMQvBAcOVTtudybMyzdv6vSk8hd-ecvwAvLUECqOsof3s-o3HL1jsKMP8XBZ1dtDXKt5WVHcNwOQwbxcepZOSCedb6FdHTyiRWL1yXtujx4efh7zTIkSBvfMFW5N47-JVKp5iVtG3aEjrE8BOigu9rV_mFDiiVSi7wyEh0_fdNCtAoSo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=d3UjSwtz59S4ze7HmykNuZYPc3li07MDlPexwziar5WzdZ27l0OPevRYgDe2JknIHVvleWc0AxWf4yuk-k3YmfA3gdMcgjr2pVKU4IYCqn16LYMGEe_jlHx7n_JjHBIDZexgx8RKFRRLRi-yMGWRV4HVKGHeFVwjfB1LzMQvBAcOVTtudybMyzdv6vSk8hd-ecvwAvLUECqOsof3s-o3HL1jsKMP8XBZ1dtDXKt5WVHcNwOQwbxcepZOSCedb6FdHTyiRWL1yXtujx4efh7zTIkSBvfMFW5N47-JVKp5iVtG3aEjrE8BOigu9rV_mFDiiVSi7wyEh0_fdNCtAoSo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SaVEdpHadMMySGhM8atZd6hgPavpfCpaXsEUk8xgsVovh89R8AI9X_mGqpp9BjrlxhVWNrnX1m7txErGrIwkLJWQtahJ1n29omdwLxjVFcPPXLU0lqxwSjaDKiMY3YK_AnaIB3SfIK6stRCZNSCvCOpl8qHEh4adCyKuLEpI5fkjpcJPgUiFpBmihLMFeETTF75_knDYRAzPSSAAgM5alWH3MB2zH3VWpvfvpgQ8g6i5yLm--CGSR7sXE-Ac6Ea67tArJIYN7t-SBjS6PbZc1yjbj_EVBCtaaOAbPAWGERLfaMRCtmUvQLcsNRtbnrtlx3bESCRO202LPoDYezqP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SaVEdpHadMMySGhM8atZd6hgPavpfCpaXsEUk8xgsVovh89R8AI9X_mGqpp9BjrlxhVWNrnX1m7txErGrIwkLJWQtahJ1n29omdwLxjVFcPPXLU0lqxwSjaDKiMY3YK_AnaIB3SfIK6stRCZNSCvCOpl8qHEh4adCyKuLEpI5fkjpcJPgUiFpBmihLMFeETTF75_knDYRAzPSSAAgM5alWH3MB2zH3VWpvfvpgQ8g6i5yLm--CGSR7sXE-Ac6Ea67tArJIYN7t-SBjS6PbZc1yjbj_EVBCtaaOAbPAWGERLfaMRCtmUvQLcsNRtbnrtlx3bESCRO202LPoDYezqP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=SrgbUMH05dv-vQ5u0ILWTznZEU1dBiobreeRMf3zEC6PtEGDDQVNzDKC6CMPxpLRdfFHFIVCTj_ZtF8m0iq3FXqj1hW7zs2GBF1O7BOHSw-czC1mplEEGGv13Y_LYFlCJQFSJz9TuFmcJqqEPfCzWlEgMB2CGoohnsrC5y-gPV3dnvpVlM_WhZCxNgWihHSZWfeju2dT442QskWT4LxHghzlxwPFcDZTot0nTCkaiMMZZy6BWzske8aw9BItEjg-1vry7sKBFKRhmpXpOOhO9aRruqO5NUZgh7z4hBi5Wpa2lfSgS72cYPlJ2AaP1KTTm5UkV-i7SIWOnpLByvTktw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=SrgbUMH05dv-vQ5u0ILWTznZEU1dBiobreeRMf3zEC6PtEGDDQVNzDKC6CMPxpLRdfFHFIVCTj_ZtF8m0iq3FXqj1hW7zs2GBF1O7BOHSw-czC1mplEEGGv13Y_LYFlCJQFSJz9TuFmcJqqEPfCzWlEgMB2CGoohnsrC5y-gPV3dnvpVlM_WhZCxNgWihHSZWfeju2dT442QskWT4LxHghzlxwPFcDZTot0nTCkaiMMZZy6BWzske8aw9BItEjg-1vry7sKBFKRhmpXpOOhO9aRruqO5NUZgh7z4hBi5Wpa2lfSgS72cYPlJ2AaP1KTTm5UkV-i7SIWOnpLByvTktw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=srPYz8cOb77xydbq5-1skg2bIM5Z60cR6wfWCEt64En1cidaanvQUyAHQCmZykNdkMM9yrUUiT0drEoYi9xFWVuOMt3-F75hXZ4fdqSB0AE9w6pyBRUScvuweSbS63-K_zHXhwrF2nDUUNvAmHIBgYukmQrt56RCpKrSxrdJnoiAP3SPkLePKhhQyDHeGEwION1KmVoMi1i0BU2frsIvPItloC2jOvm5YTREpAY3PvRu_LQQjCuZqIVNMwYCCWDeemN00CCW4ffH9-hHEzw3frzp_od3ZXzDnzQx5wA2d0wAlLEUj8avxCeMiLYHz3Dg-4Bc0ttHElk0TBQ8CW0VN7tOLdqjb6BB5chugZf2XzuKmZPIn4vD9p8b8vBjVqTj4ClwpW-o7yobhrJhuzXFg0t3tMxP09ivP3eqBR6Nc48nPD0bEy9JwWK_z5vvSG7qwEE8yiOtgmZ5FUjagNRpEzZ58eyagm6dUDsfe_UiRmOWSc9rrVii8SWrg3zbXvOViHNgRbYQX-N_5W85CSE6dCXJ7hzJlI9rMZTSOZls8r6tNDJcLsPYPo2D_RtiSdPoRchzvc9oJzWWsYb0dPCGUhNYcBOFaAZe9NSECtuNaLmdGrb9RX2fhmeGz3DAeUQY5p_TnzfOOn1IATJ-LfH09KjpeePTZcQ5D2UtrefUT28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=srPYz8cOb77xydbq5-1skg2bIM5Z60cR6wfWCEt64En1cidaanvQUyAHQCmZykNdkMM9yrUUiT0drEoYi9xFWVuOMt3-F75hXZ4fdqSB0AE9w6pyBRUScvuweSbS63-K_zHXhwrF2nDUUNvAmHIBgYukmQrt56RCpKrSxrdJnoiAP3SPkLePKhhQyDHeGEwION1KmVoMi1i0BU2frsIvPItloC2jOvm5YTREpAY3PvRu_LQQjCuZqIVNMwYCCWDeemN00CCW4ffH9-hHEzw3frzp_od3ZXzDnzQx5wA2d0wAlLEUj8avxCeMiLYHz3Dg-4Bc0ttHElk0TBQ8CW0VN7tOLdqjb6BB5chugZf2XzuKmZPIn4vD9p8b8vBjVqTj4ClwpW-o7yobhrJhuzXFg0t3tMxP09ivP3eqBR6Nc48nPD0bEy9JwWK_z5vvSG7qwEE8yiOtgmZ5FUjagNRpEzZ58eyagm6dUDsfe_UiRmOWSc9rrVii8SWrg3zbXvOViHNgRbYQX-N_5W85CSE6dCXJ7hzJlI9rMZTSOZls8r6tNDJcLsPYPo2D_RtiSdPoRchzvc9oJzWWsYb0dPCGUhNYcBOFaAZe9NSECtuNaLmdGrb9RX2fhmeGz3DAeUQY5p_TnzfOOn1IATJ-LfH09KjpeePTZcQ5D2UtrefUT28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=IEbNi-PDRYIz78eDgNETFKB3i4bXGbrTxsnkpxtl0fIiDTg5bmblTIRisgZrArpKN4dT6PBRsGN13fGK78TuE1jmA1g7AsI6WAXuofJs-7sLJ96WbXfe-nOqSC1mKZV5hwcw6C03QiiyI_2VO3WNar7plhsuCAvfcv0wJQA2wCYnyWvxk_pZ6ffFfLcWEJEFQ2glYTp8GrpN_OTKqMJLAwmb0VL7BN9-6KYZ80PSiW8UK0UUfLB3hfznhb1mpm5KjLVsJOSF93qrcM5dWXxGjBKkg_i_NzMt0nAKSwgYbqXyqv-6M1dlCSoqb2JcdKjpxbBnH4yPqmKGHLFQe60Abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=IEbNi-PDRYIz78eDgNETFKB3i4bXGbrTxsnkpxtl0fIiDTg5bmblTIRisgZrArpKN4dT6PBRsGN13fGK78TuE1jmA1g7AsI6WAXuofJs-7sLJ96WbXfe-nOqSC1mKZV5hwcw6C03QiiyI_2VO3WNar7plhsuCAvfcv0wJQA2wCYnyWvxk_pZ6ffFfLcWEJEFQ2glYTp8GrpN_OTKqMJLAwmb0VL7BN9-6KYZ80PSiW8UK0UUfLB3hfznhb1mpm5KjLVsJOSF93qrcM5dWXxGjBKkg_i_NzMt0nAKSwgYbqXyqv-6M1dlCSoqb2JcdKjpxbBnH4yPqmKGHLFQe60Abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Po8_smWrLM8WsjrnFOqOZzirtegdrc19TEfA405-iUfp_sDxai2RTSJJ6NxZwD6iB-10Q1NKqZtVr9R2UrrImJuSCcesyv3FWNU6mpdKaDTIvG15UiUNN0STmn4H8t4z32n1b-jyrmvUCgG0LNIqptS7KgQeFC6cFfLvwQQSeJ0uLBr7kR23GoWLFOW4eb33ZgY6iunhmR-GUDqVXzcYzcM8wU5gBCs1Uyzij6xg6jffsZgW_CwcI8yZMYb17NpCumW9FyhsnllMfV9CoLJmFWcpPCs_GJTBaL3xoFCdlK-ekW5Uqys6kLipWnaI5YWnQFf7s1v8Qh7MVD6JOtXO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=Po8_smWrLM8WsjrnFOqOZzirtegdrc19TEfA405-iUfp_sDxai2RTSJJ6NxZwD6iB-10Q1NKqZtVr9R2UrrImJuSCcesyv3FWNU6mpdKaDTIvG15UiUNN0STmn4H8t4z32n1b-jyrmvUCgG0LNIqptS7KgQeFC6cFfLvwQQSeJ0uLBr7kR23GoWLFOW4eb33ZgY6iunhmR-GUDqVXzcYzcM8wU5gBCs1Uyzij6xg6jffsZgW_CwcI8yZMYb17NpCumW9FyhsnllMfV9CoLJmFWcpPCs_GJTBaL3xoFCdlK-ekW5Uqys6kLipWnaI5YWnQFf7s1v8Qh7MVD6JOtXO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FphrLNGqUuF0aa0cP3jLsBjkzm95lfy-6QcNqg1NQSwywPLWQGcKTXto8dVagNYL2RVfrXKkeiowr7mNjGxeQH6-V3pa_jb9PLYDTznlpy9n3ah9l7ychcnomaxUpXxJlP5xNaRATWtwaUveBzyDeTySo6jHLJJ79fYBLnVadD82Cq18SuIMMG4BpAD7aBOc7FHc8260Zygfz47TCrwwvPdxWS0CtYr1Q1qRmhV_h2I3Z9-LETHb3TrWCAsH9yS-bVc7MTCbs6oQjKhmbe4jozVH8qE5Dtlfn91ax4ZUed7mFLfxCBXp0CKLuIiWgXI1E0ftbxEf-0CEbAOQQFttJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Qh2ATIlK7f6IJJfxZ1BYWRwHwXtqMRWdelqLnoN55VKIm-wmTqufRP7F_piQN1Y9zD7-1XWseEle75--jvb64a3o7L4Ucwu00udl6basHXkUZr2acSxBXo789Di6HV_9AEAXATZbjROiDt8NxTxnfUqGVXP7ekxoF7jGKgeTUZ_xmtRzKc-ckc2TJABRUm_uGseXNmEEqGHgXlz0C2-lIf2lorZ2YsrlXN3oKEX7D74TdIZEDhvJxymSP6e0QdzXOHYhNpEAa8tIwLHlzAiSmYZC__-xDmuT2TbQu0BjZ4zzOnY0ZhpokeMA6HdOvz1WPqgH96W3xpTHWzODC-S8mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=Qh2ATIlK7f6IJJfxZ1BYWRwHwXtqMRWdelqLnoN55VKIm-wmTqufRP7F_piQN1Y9zD7-1XWseEle75--jvb64a3o7L4Ucwu00udl6basHXkUZr2acSxBXo789Di6HV_9AEAXATZbjROiDt8NxTxnfUqGVXP7ekxoF7jGKgeTUZ_xmtRzKc-ckc2TJABRUm_uGseXNmEEqGHgXlz0C2-lIf2lorZ2YsrlXN3oKEX7D74TdIZEDhvJxymSP6e0QdzXOHYhNpEAa8tIwLHlzAiSmYZC__-xDmuT2TbQu0BjZ4zzOnY0ZhpokeMA6HdOvz1WPqgH96W3xpTHWzODC-S8mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vo_uL9HDFaIixnaCgveLMHj73MxRm5myC_gbq-7Da-MrMKjhXGp6vOrXbqh2xClWBy6FFkgHgCgVx37u-r4cDXDxG9hPLNUGDxLyStpe-o0o4KsWGiovSeM3_iZuUgtBOiNA7Pk4bUu9Qb_4fAHvgDKc94jQlWabfK_styrjvtT-jkaFbxTpR3YFW-uOSao4A6kfLUSn9lfHZI7_qcdjgoDrd6hvGG3N6yubKpSx1Td2dafyPSmFo_mWeXKO0VIPR95bSYEzJeKAlnwRIrF1hRY7Bbsd5mP7QBtz-3XUr4VJdYyKXGGVFh6zqvmpo0YO7zNu73ldvwBF2kP96a7RZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efn2IIWRYWpiZQzZU8EEV623I3Urza_2wukAd1VE5Fxv75jI81OgKLauPoo17rjcuriA0jLH20YSdgmpwbt5LL1kgCQIb5swUNYZZF6ejfFPLCiLYeH5Yk7Oj6DqmPm8QOokllOKtjktd_n9FX1fR1O2lGai-mCKxRWRBnlEG3iJXcjG_2r7ngD2R4ibU_2WgqvW6ay_3_BMLzvdrtXZRTJDkWB0PK6kq1ERrFNRovAzSwtwwKtX_XOubg-0DTzigky9WVAWJN25CwaH8kCPvsN8sXpnAKGNeDURDbg-NaXFNlVLJk-feBGYsczelwtx9CygAXXxWhl7-7gCGJbeJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CQKa8HVjhnb_RhNr20B7z7w88BOI4g_cCiqQWWZbuD4N0xgMDQ1bPZN02pat00km1_HH8kx1ASzECo-3DeaQERiJFRMkw7VVvYcs7mi9OHGv8LGWnEFX_dAhm5LdgnS6qE2dFGHHEnPbwgJQ5_4Tso4Afa617ymDGTYSVVbxCYyXgty3Mafkdmb32Ui2Ncg_6lnrya5_zXnp-0-FtU_IhqYKlwKgGuQy_Wl60G2aQj38p3U0Pn8tpb-2Z_aCwfxVzYI-O_jR95AFnw1XHrZ5Vb1SZG4fXL2PAJcHfCtxtN9nDksjP24sBVyo9N2rE-RijsS0uMX9iXWWu1S1AKgC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CQKa8HVjhnb_RhNr20B7z7w88BOI4g_cCiqQWWZbuD4N0xgMDQ1bPZN02pat00km1_HH8kx1ASzECo-3DeaQERiJFRMkw7VVvYcs7mi9OHGv8LGWnEFX_dAhm5LdgnS6qE2dFGHHEnPbwgJQ5_4Tso4Afa617ymDGTYSVVbxCYyXgty3Mafkdmb32Ui2Ncg_6lnrya5_zXnp-0-FtU_IhqYKlwKgGuQy_Wl60G2aQj38p3U0Pn8tpb-2Z_aCwfxVzYI-O_jR95AFnw1XHrZ5Vb1SZG4fXL2PAJcHfCtxtN9nDksjP24sBVyo9N2rE-RijsS0uMX9iXWWu1S1AKgC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=R4tXA_XS1SzpWHM9tynHDW6hho5tscJXw1o8WQkpkHci7CfV3NhJ7VTacKvnHBgVhGloiXFmNAM6FG45Dr6vjwLfB1MhWWh1PlFWO3SGfMnyzxAbNBYtdYmKvUUx2seM7k9A6jlwTDcglMImZNX9Ku08UDnGB7KuskScxbIVXZsp_Za6CH1k8lplic21Sg1V0--lZ6TFU3zki5fpLmL9nStRyN6bRRJf4j15O6QMtxsqxJ2xs3YdHmotl_-MGDE47rvJUxQ9x47_cbYOTPLAAHCu6O7Qrn2zmi8jB3tmSGylu2vjKZJ7mGXn73aMnMp4-jWitngG1JN4cBUXASwG6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=R4tXA_XS1SzpWHM9tynHDW6hho5tscJXw1o8WQkpkHci7CfV3NhJ7VTacKvnHBgVhGloiXFmNAM6FG45Dr6vjwLfB1MhWWh1PlFWO3SGfMnyzxAbNBYtdYmKvUUx2seM7k9A6jlwTDcglMImZNX9Ku08UDnGB7KuskScxbIVXZsp_Za6CH1k8lplic21Sg1V0--lZ6TFU3zki5fpLmL9nStRyN6bRRJf4j15O6QMtxsqxJ2xs3YdHmotl_-MGDE47rvJUxQ9x47_cbYOTPLAAHCu6O7Qrn2zmi8jB3tmSGylu2vjKZJ7mGXn73aMnMp4-jWitngG1JN4cBUXASwG6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=BFL4za4M-r0ag4QXnb9_fKcD84JP67YyuYK_gPNffMx-My4HUqqAjUHjQXbylNupFVpF4_rAo7JO6XgwAoJxz6MwEQiafiBByfzxHpqT5-SXHWvvullCzWr2z90DRfy9Ndy0e02qGaH1cjWmzBIWga5Q06BPs2Z3EtRwvDq1fh0cqx_ejyLafuFeeqelChWFrYryZW7KfLE4LsRxPV5VDNMsu0FzbjVgaaWH97jnyzvn83XKfA-tW5xOz3NcZf3g67EPnYd0b-b68Y6yCfeh58hb74WpLRqfDuEEYZIFLq1Tz66rkoPF2D4Xh3KBrySAaX9MOCtFYK4KrsRP5Dq9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=BFL4za4M-r0ag4QXnb9_fKcD84JP67YyuYK_gPNffMx-My4HUqqAjUHjQXbylNupFVpF4_rAo7JO6XgwAoJxz6MwEQiafiBByfzxHpqT5-SXHWvvullCzWr2z90DRfy9Ndy0e02qGaH1cjWmzBIWga5Q06BPs2Z3EtRwvDq1fh0cqx_ejyLafuFeeqelChWFrYryZW7KfLE4LsRxPV5VDNMsu0FzbjVgaaWH97jnyzvn83XKfA-tW5xOz3NcZf3g67EPnYd0b-b68Y6yCfeh58hb74WpLRqfDuEEYZIFLq1Tz66rkoPF2D4Xh3KBrySAaX9MOCtFYK4KrsRP5Dq9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUtReOdU0pKxTqOeujWhP4VMTnrroWb9KIKFsbCCsFlrJEFBwbk6WfE0C6-RovhztRp4JJJgfj5COXOQ7Gdn3UUe_xY1BTv_ZsFEqTQLTmENtnhuEEOSOnCUaCrujjESPoSc-4stdk48uRsXIUpzmZbZKPpWxQ6RworNvlUeqTlPeOQgtd9dQEx-vdmlt6EH9bU5Mn9URXGqZa-OfXyMkBlKmo_96oQeVAORpX-AmGzZpHs9BQoa4oRzkPN9KCkdh2ADvlB6zLHnQn3cSbRfn2zhCxv2KOqigVS_T8_7rFQVBJj3oE_fniFIpT1TF-WSQcsfcc1r3HhQCCkT1899SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=wAGt_qWj8y4qNu9-YAwhtnkD_VAPjArg5dAsJPyCq-aE6ZomFYG6t_QbR3f4cmqnUQMr9VQYCcLeVAYeX_hNB2WItCmrXUr9TZxnS6BTefcUHA_sFcb6Vo_HokiIpBO75qTHzvWx8_0TvqbbqN4PB4LUnUQBfH_GQCUKy1e5gR-mFMr4vdikShainexfED2_GA1ieiv8Ef2orCCQQSjLOGIznq9HZ9BdQHFSNxF_X9EEIVjeiuYJWEQdVW4pPGAii4DZSaa0Z0CYuxaW6ZSqe5LSLI-_EvNojUFaCIl0dHRz6BlNSgnyocR-E5BZzriD5BtnAtHetq74XJNUyYSrrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=wAGt_qWj8y4qNu9-YAwhtnkD_VAPjArg5dAsJPyCq-aE6ZomFYG6t_QbR3f4cmqnUQMr9VQYCcLeVAYeX_hNB2WItCmrXUr9TZxnS6BTefcUHA_sFcb6Vo_HokiIpBO75qTHzvWx8_0TvqbbqN4PB4LUnUQBfH_GQCUKy1e5gR-mFMr4vdikShainexfED2_GA1ieiv8Ef2orCCQQSjLOGIznq9HZ9BdQHFSNxF_X9EEIVjeiuYJWEQdVW4pPGAii4DZSaa0Z0CYuxaW6ZSqe5LSLI-_EvNojUFaCIl0dHRz6BlNSgnyocR-E5BZzriD5BtnAtHetq74XJNUyYSrrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ERCnAfXb4rR8-J34aZyPCFucw1qIlMWvRPWuEz8-Jzgzhtc3TE9E3_6-ppGuPahMHk-7KyT9_Oh7H3pGetUcbpxQ4CCa2WyBpdlh95_rMkGMyY7FgWocIWcraWVmaxAL8KjEKxpfMQV1VHlpkVxt-FX_shiyo3BOXt82PhtgVW6JppunWQ2DxmuqAagRutKTd7edC4qXhwJ67Y6hszUNmkbtwteM14wgqtzqHrPNQgsO0gbqAWxTuxAexWLx6W8xj2I3S00qpwePzeV5AaxFCNc36LHEUfsMkwh7xDPQfjv8JBO-880axYgqw1l85D8vauVnsG-sQFFy42lGd8GSyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ERCnAfXb4rR8-J34aZyPCFucw1qIlMWvRPWuEz8-Jzgzhtc3TE9E3_6-ppGuPahMHk-7KyT9_Oh7H3pGetUcbpxQ4CCa2WyBpdlh95_rMkGMyY7FgWocIWcraWVmaxAL8KjEKxpfMQV1VHlpkVxt-FX_shiyo3BOXt82PhtgVW6JppunWQ2DxmuqAagRutKTd7edC4qXhwJ67Y6hszUNmkbtwteM14wgqtzqHrPNQgsO0gbqAWxTuxAexWLx6W8xj2I3S00qpwePzeV5AaxFCNc36LHEUfsMkwh7xDPQfjv8JBO-880axYgqw1l85D8vauVnsG-sQFFy42lGd8GSyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=pKEa6gKjTTEp16I5Otz-SiY8LufUozvGp5WHyJ7In1Pz2G2EI2wj9pudzGMOe_BaI8TUw7Ps4x_8b3-XJGnE4p7ZCEZLyzS68NJAbruC2tqZ-HTMDjSpCftWzX3Rsw5g8-Rt9BjCEdMnGiNr2i4yO7Q1UQ3CaaopqVN3loEdAhvHOu4_ZXJB655TbI5CajCxP5pDar3m_twpc0fXait9Bz-ZKneJiPh1E16iuj5BbropZe7Q2xsulsK7tR1q7a93qVKVPblLY_jo2hgeHYRdJ3wOiYvlY9mqbD3N9vlYaFz7fnbY1vFXsb_FAA8HQnn58QxWjLomIGe8UdvRmcgTVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=pKEa6gKjTTEp16I5Otz-SiY8LufUozvGp5WHyJ7In1Pz2G2EI2wj9pudzGMOe_BaI8TUw7Ps4x_8b3-XJGnE4p7ZCEZLyzS68NJAbruC2tqZ-HTMDjSpCftWzX3Rsw5g8-Rt9BjCEdMnGiNr2i4yO7Q1UQ3CaaopqVN3loEdAhvHOu4_ZXJB655TbI5CajCxP5pDar3m_twpc0fXait9Bz-ZKneJiPh1E16iuj5BbropZe7Q2xsulsK7tR1q7a93qVKVPblLY_jo2hgeHYRdJ3wOiYvlY9mqbD3N9vlYaFz7fnbY1vFXsb_FAA8HQnn58QxWjLomIGe8UdvRmcgTVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1IVaECcFP7oOFHy3z2JincDO5iItpqFR5R1ghYL1YNWkY-gKicIWmiw7WWGy62Q-2BO3dKkYgj252p6Xgk_B8mWo-T59V4WY69ukX0s98OqfM9vXeKq8LvIwds5Yoc687djyTVJAZUf2d9u0sduWf2HF218rDiG2Fffnd5s-Jn-O6LLUUdOJsCUKTuCbnII9OTklcxB6kS54mZSvAQlxNSzuF9wT5T89HK1TZrRU_hr2sBoptlwjT45uJDJY2I3DCrq-zhHL5lmS8vpxHGUUIMG-FK2aOgvZrfjxflF0ERTzODRITirfsBFLKrxTqFGm63Xs60RHmt_nBml4kM3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WlzkG0z5Y6lYdqUaPaaxVQOBe98xwNFNbMRN_ngVbXEVg1n0Rmqw_d9tzVGFVwhNpBUS1AK87A4jMi6Sxb-AOSJd8K1wh3h09XFLJEw2meBtTg9n8A5k_ZaOJ30K6OyF13e7LuD6iGODQfg6_VQ5Ed8q7PCymnBoq4l7TCdNqbdHWSAp7xTZlZPs6IFX3OA3TdMvU-2vOiKlcX9_jmq8PbdUybvOV3UV6riqw7mOEGvoyLyzuHL-AeNzPBRyzWZ2ZIVyVVnNJqC6D35liG_qF9XUIc0GIEMrdAPCSRqeCXkjVWCZtlhLwmCtFLGBiRfUwLw7yJEjbqWFPH7fV076HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=WlzkG0z5Y6lYdqUaPaaxVQOBe98xwNFNbMRN_ngVbXEVg1n0Rmqw_d9tzVGFVwhNpBUS1AK87A4jMi6Sxb-AOSJd8K1wh3h09XFLJEw2meBtTg9n8A5k_ZaOJ30K6OyF13e7LuD6iGODQfg6_VQ5Ed8q7PCymnBoq4l7TCdNqbdHWSAp7xTZlZPs6IFX3OA3TdMvU-2vOiKlcX9_jmq8PbdUybvOV3UV6riqw7mOEGvoyLyzuHL-AeNzPBRyzWZ2ZIVyVVnNJqC6D35liG_qF9XUIc0GIEMrdAPCSRqeCXkjVWCZtlhLwmCtFLGBiRfUwLw7yJEjbqWFPH7fV076HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miy1otTx1mqgY-ThqCpxmq9_nbmUOgxRuXZ-WHgxEToan9gtf1W4j9zB3eVJjeMWmASYYJB_23RRC5drzd_CIaF2kGKSOMr5o1-rE1mcV1vHaO8tLmuPVKEyVzsmOa2OCAmrlOI8UCRwfie8tu4hx_gPLj9BXJViu-2918bpKc9k_gDx8AdTX9dksi04Lk_Z7rvpWYviKnB1IY_nTeoXtWKfufauq6YYQcuUqszZ4xBMkZnRzaXcWHyiA2WF6FPhw248WSxcwkfDWy6qi-2TR8we8yc1ciVAgB-sogMOwOxrDkBMFW4FiNMFnLVWm16klCYBc949whgm38_4gu79lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=moOp9_fHMwNAQd3wCgxEBdc8BBVLGWcdHUbKIM9o76FC1onL1MN7DXOTI329gytpsT4OlOfqf3sv8pYljeFRR-McziFj8kVlQVbqnfi4S6SAPlsIga2-iTdLRNyZnWXIheXS2pCHkwnsyxBeVmMewUEr0perCsEADbA4rdYKLFHBvmPqDzIFLj_R3gfmx8THx5H1CU9uiqAkr9PsWu0dntXBinpJeyaTWsaJSAeM4sP38ip0qhsVYMfmjgxGlxkp9bcZvmz_VdyRp8mg_VQMsX0csQwWJGOeNMyvYNBniwb_3w7ivvEqSiow2Fm3crAbCqVtoyRdCTV2zQvjE3KuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=moOp9_fHMwNAQd3wCgxEBdc8BBVLGWcdHUbKIM9o76FC1onL1MN7DXOTI329gytpsT4OlOfqf3sv8pYljeFRR-McziFj8kVlQVbqnfi4S6SAPlsIga2-iTdLRNyZnWXIheXS2pCHkwnsyxBeVmMewUEr0perCsEADbA4rdYKLFHBvmPqDzIFLj_R3gfmx8THx5H1CU9uiqAkr9PsWu0dntXBinpJeyaTWsaJSAeM4sP38ip0qhsVYMfmjgxGlxkp9bcZvmz_VdyRp8mg_VQMsX0csQwWJGOeNMyvYNBniwb_3w7ivvEqSiow2Fm3crAbCqVtoyRdCTV2zQvjE3KuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr6u9OKV2XpthuXAy1t8PNjO6witeibJJhesQHZOwgKsHj42AeT9KSYa7sOGtJ1p0HtZ_8k1B0retNQYajf9zCbUvtQj0S6Werxq6wOIkxEoOass9scFnxoA3v-rCROw61AW8W76EAWDAaMZpLFW151Z8l9N_i90bPSZ5TdIR8-q366b16mnvh8mp_TiSsDfgR3POgqIRLkhwu2kZixr6iuHCyFZBWsHpaPbcAXgdgrSznja9v5hJFDqlZOuOVl18G0XRai_At_7OzHS4ajYDhP8RsidqOowTV0IPqdH80hv5KGdWvG5NhQpazsFclYX3KHbcLTHtkHHohsbzDW5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=kPNQ-jiqFbGk5wpCIDlb-0NAsDc6pMgmoi3RMoQFKimVLVA3aiPxVJ55_PUHh2uswPuKD0naZEU1Yi3Gk3vAkGG4h_V-17DmvA4kPTLwWURcmBMkfmOmF173O_m_sDlzV39fhy78RFBPWpLXqfsocb-iWTkarokjPz0zNJy9iqu970PWdQkI6MmVKHUs22BNuTSKnKqY-3R4BWAmTMEhh8UwTpyD0-URoLqpA7ActQIfDbK8essuSslUSCKSY_kreDRuqdgwNYiMPFMaIlaBc01n-mclqrTy5GmFxyzkjfzjzdAFuJC7rrbCOXe2BM8HcBJTtbNWWfFXyTJHqRFekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=kPNQ-jiqFbGk5wpCIDlb-0NAsDc6pMgmoi3RMoQFKimVLVA3aiPxVJ55_PUHh2uswPuKD0naZEU1Yi3Gk3vAkGG4h_V-17DmvA4kPTLwWURcmBMkfmOmF173O_m_sDlzV39fhy78RFBPWpLXqfsocb-iWTkarokjPz0zNJy9iqu970PWdQkI6MmVKHUs22BNuTSKnKqY-3R4BWAmTMEhh8UwTpyD0-URoLqpA7ActQIfDbK8essuSslUSCKSY_kreDRuqdgwNYiMPFMaIlaBc01n-mclqrTy5GmFxyzkjfzjzdAFuJC7rrbCOXe2BM8HcBJTtbNWWfFXyTJHqRFekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1-GG_ALBtuOH_m4TXYrQ7GZW3EgQBp_cjB-YUFOwF1JWmr-qrm8qAPUYoh_R1chi9TdxayW0z7jgVUWrnnIKAxB2jXrvIxM3g_3c8eOjf-UBHUpJYJpjSvIgIXTdJ6pExxSLSumcw6bgOPZRT77rUJEE4vHU1XcuAMzELA1aAuXCLR1Lyb8ZOx6g1ciHJBlBHNHTxUVxcQtWHo7-TVn4WC74_yhajVs9ShFmk7bkRlqTFZzxePyDQecLwpcLFxvB4f1BiDTVyY70pWfj2gAdNEHb4g42nXgG669iwYLJJhJS_C69CJMo1mbHOUGbvOgXeoXYf83ZwhDUuCbH6x66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SeXpoMLoStQpksOIdE8hhSQyjVN37BbWfgSxvQU7wQ7k4oC8GtD9JMg-SuzMQrDxD1zZA-5XaIkVyeRqtoMUo8W2wqepoIlKsjfCcggyWKRtgHPG6APy8GcywwUlFXsAOyFvpHa1um5eJxZo2d2GbOTIJJJhYSUifZ_nlusLUmow400IOsEa4E0qs_dzh9wqoFX53DTwPtr5S18LWbkggr-r-m7B_1nl8GmcT3860rP3XWSxZauYmOlm747wzL3q5CJosqAFbHyhs626YSjmJaoVSHXIDZ18jWq6DsMU1RaZN6wT7IYuFuvzECpZGyGu6ilZRukuyq4BmNlzki1V6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Wwi5dtCBYLnLiDy40OZvdhrW7glX7fw_-DEfIskGJyj9RmQ4V1ZDLRRbMtoQUDob8GheoMIP_NQ8q_PxqyyBS8IhifbsBvPsw5Wtqwjdha4-7ikgGzU-xAWubpQGd9Z5GtmX3izzYEHHJR1AddPIzY8DL4QUNBbXnVUqOYo9R4dgi0tivFl9xBNuUhSTe0WzoZAIbFpj5LaVNEAzTOkYBbUGQk7xsxcAk6NO9TmunqmG_PoPy1gMngAmPfD6PkUeT_W9Cf0HwB5HPCfPj4FsLGyE33dNvHm3UPnROrSGpSeW9OXBJWRp-YcSZKXeQkcDuZ1Ch0aVSBBrAz2Z2tUKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=Wwi5dtCBYLnLiDy40OZvdhrW7glX7fw_-DEfIskGJyj9RmQ4V1ZDLRRbMtoQUDob8GheoMIP_NQ8q_PxqyyBS8IhifbsBvPsw5Wtqwjdha4-7ikgGzU-xAWubpQGd9Z5GtmX3izzYEHHJR1AddPIzY8DL4QUNBbXnVUqOYo9R4dgi0tivFl9xBNuUhSTe0WzoZAIbFpj5LaVNEAzTOkYBbUGQk7xsxcAk6NO9TmunqmG_PoPy1gMngAmPfD6PkUeT_W9Cf0HwB5HPCfPj4FsLGyE33dNvHm3UPnROrSGpSeW9OXBJWRp-YcSZKXeQkcDuZ1Ch0aVSBBrAz2Z2tUKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI26pOTPIZ0mU7X56ADnsB4Ve9jvH1ZLLlCqZODgHmSAyvz-g1YPuLQO7rm_QIo0WcIb304dNQaCdp3c10pdalSgV0qbJMl3U5vZ9qrM7IAF3eM6sqfCulGl7Yg0Vy8wCtEehN0tRc30BsGovJq89vzjv11kPOOeV4e9dTo8sj-TpBenPdADQQFShtiDTxTUHTZAUPdewPwp1dgPO4fp1rHR6UxtQ1FouHgwky0ZgHLx8m7SWxRfUfRY3rkj4ZQe23TxjMPdKGFe9Zc9ptr0DsB2YZdrDtgxIiPu377785CbAdCMlxeRHSDE8l5XVA5-u5cf4KbR6s_R7jDovNpERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTUy-vLQMLNNnaT6XJLQjH55uGuE6oy2czWmDB12LM76YvvuqPjEy_gogFnKlo1h9Ek40K03AT_waG6B4lC03f5c9-U7GwQY-xOAJc2woJrLAOQ2WMcdlx3K6_ySJixhEwYHSFhLpstPU1EtWjnTwZyXeZ48rcGK-9XrEM0b24HfgNFIT50-PsKkya42BUIL8vOVD_hi-MKvF_4yUXipOkp2c_4tPhssyqfoe1XOhEoB6SBtTioy23Kb4fjD6EG_yzWRkG2G_vDo_ZmFtzpOBTo3ytf205BFIoBVJCiLDdlHec6Qj6v5vgtYW5m1uweXB7SX32AYQdMyG_Su2muNHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbsc2-bW4RfJRuC0NxRqQOctw_vCgv53EdjPyurwOaWiyOmB0UgF42mz2kTxjJqh24YubROE8k4CIbgO64HKgA2dDL4Cvo-vYRCvtD0XmSfYi_2dVuoFPGmhiyw60qn4nlZeFSVDmNHv-KqiUMfox2Hqx7loK1FLm3JOARfe-ODiiSv6OL9N1HjrgHY-RYrX1tDCkxifugufA8c1nrtRN9RzMruQRV3B9E_4w_ut7kcQ73muEKCXfRWLdwtr6zau2PuC3ltzDlzD0U9LkLeAlfi7EWKEwiPdksejNofd0WKZ0TR4SKZ4iENcETpVe62KaoIyPBqBshSiY1OtpipXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5-7FSb0b7EsOHD0FW67Gb2tOJbGYs-uea6o4D2L20JP_MGqYqDS2N8bb2NoDkRcwAAlWdVcJG9lL4Ej4Y7cRwxHQd28_24CVqWRiYVJ5vBwqLYwp6RK8IkgrsmHIViukYEydgNGdwj8Gv3sW7n2zgqp7ia1EBPeML8AcHU4JuMsEJutzPOxH6-CR-miCRocwl3Tc-BawvukE_-Abl_VyKDNd9EkpLUTMPzCLuRKQLhBfYqdWxu5kuab8zBK5Vd25JLZxnyYW4vGEHvwChXiUVn6UzsWuwv-ILLlVilnGGXhWB4YlAg8BBe4saWhLIkb9ictFPARFkYuiRI10EGE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arH4amsWb5dUPM3r9Itvh-Yzi_c8utEN2Rs3XR40F_BA8MrXknbWpFaATSCQfhy4GjUVCQPazmHz_ot8ToYQolsXdF8VMMji_skE76GTV7WQkCMcJq6balAqZUX_qdQVsGtsM8PM0eA4_bEvU0AZC6tt1mInfGljqc_8AW9bBSuIJDT44EbYKx9SyWiem_e4ymITBqMAHGKUwm8Kn7u3sSDaC6LAO0MvNjuhq8ZSlyW5FcX556aFAnNLuZxDBf8DxxMvhoDRTgP8mZ7N46XjnHW6WJT_0ZyiIVDgDx-fkonyyJw427V2v8rYjglcoIRRXaoqYTNBYISS_zog_3RNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=TqY1Igq93UWAFYz2LrTlZFftUD--fnorlGiJI5DwLl65jZpR-m_gMtQT_4O10uSpdZlFu67G3ockLlrVJxpRG89w4SHglkq3DURSxnXD0NPJcURHhrMCNFX3weM69Ukad-FR99BMZcAi2jDgnvl57_NXP01YdxC_0pWrcG4FiqBjKdJMfkoOIgTKe7JQl0u0Rzc-b8hDQfrWyyj2s7KOaBkBpMUKo3PdDsZNHKZKBPBU84sfkciZadPMppYYWsh1LJpdItuGREa7xXWuRdCY86d8KRld3wJtn6sjV8eXI9rvfV-ZuRRH3DGLtTT9lEzuWxjuRqSjnApWgG6hEhVurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=TqY1Igq93UWAFYz2LrTlZFftUD--fnorlGiJI5DwLl65jZpR-m_gMtQT_4O10uSpdZlFu67G3ockLlrVJxpRG89w4SHglkq3DURSxnXD0NPJcURHhrMCNFX3weM69Ukad-FR99BMZcAi2jDgnvl57_NXP01YdxC_0pWrcG4FiqBjKdJMfkoOIgTKe7JQl0u0Rzc-b8hDQfrWyyj2s7KOaBkBpMUKo3PdDsZNHKZKBPBU84sfkciZadPMppYYWsh1LJpdItuGREa7xXWuRdCY86d8KRld3wJtn6sjV8eXI9rvfV-ZuRRH3DGLtTT9lEzuWxjuRqSjnApWgG6hEhVurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=kCG1oElsmi7GTNY5djbt0370RI2rNQru1hkAp5foZoWujSAMdDcH5PeHzFXDdAcUY8H9Yd4zRiPeK7Ab391Cs-qqH7TslLRHMjGKQq8Aynv2-EPBLttMxZJ0eAEt8J4E0oDeAygAUJTyHtdpZ6bpjGarP7jE6bBNWuyvSr4TtXuMzR3-K13AvH42Z2BcUEHKM8OU_MeuJh0c93VcvGijKmuubJtAD6BY6uSQ2QJsjB-7WCRvF9LIE8kE4rSAEABZGI_MKqAdhV52tLWtH9NdmeV3_iFKS5tq3qn2XzIBLIYb6aDsc0feSv97uOTj-4ODw3os_rmRMNtviLH_E0ZM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=kCG1oElsmi7GTNY5djbt0370RI2rNQru1hkAp5foZoWujSAMdDcH5PeHzFXDdAcUY8H9Yd4zRiPeK7Ab391Cs-qqH7TslLRHMjGKQq8Aynv2-EPBLttMxZJ0eAEt8J4E0oDeAygAUJTyHtdpZ6bpjGarP7jE6bBNWuyvSr4TtXuMzR3-K13AvH42Z2BcUEHKM8OU_MeuJh0c93VcvGijKmuubJtAD6BY6uSQ2QJsjB-7WCRvF9LIE8kE4rSAEABZGI_MKqAdhV52tLWtH9NdmeV3_iFKS5tq3qn2XzIBLIYb6aDsc0feSv97uOTj-4ODw3os_rmRMNtviLH_E0ZM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k_HTj1spqkb2fiBghaoRiwrpBg2J-hlZaDl87CTniq0zoJr4JO33-opejImQ2BMqZpKtHWMgNDJg4Q-YHhz5qyihKsmzL7RtAtdKj_Yn83Kmny_OgLU6BdX6AwuCYoVs2lasnCkCXEicWwrMyZ48h7qO08n-3R91Xb1Z5vysBqXoGSr74Xy3paP6YsHtpcpagIwf63BwH9Cb0VyVpZQQJBAWQtH3piryYa0CHRP3WdZ1VXIKi4HOAfwZnffXzmLrRy_6x0wZcYUDFk3gopJDCbUGdzahAnN_3OcOER7vKvKV40ybZdRp3n14oh2Ntw7-yfFgs-yNhOq4D8g4rRy8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=k_HTj1spqkb2fiBghaoRiwrpBg2J-hlZaDl87CTniq0zoJr4JO33-opejImQ2BMqZpKtHWMgNDJg4Q-YHhz5qyihKsmzL7RtAtdKj_Yn83Kmny_OgLU6BdX6AwuCYoVs2lasnCkCXEicWwrMyZ48h7qO08n-3R91Xb1Z5vysBqXoGSr74Xy3paP6YsHtpcpagIwf63BwH9Cb0VyVpZQQJBAWQtH3piryYa0CHRP3WdZ1VXIKi4HOAfwZnffXzmLrRy_6x0wZcYUDFk3gopJDCbUGdzahAnN_3OcOER7vKvKV40ybZdRp3n14oh2Ntw7-yfFgs-yNhOq4D8g4rRy8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=IhRd6kZf7ab0WIuKV0T8fak2d-seNJkb1R8gWE6V8eg-ZLgvZQOyzaJnjzNS7Ze3sHUcUuobOPAYzN4-6eyG6TuHk1kqXolTCTWI9cm_gW0l_jFan17UYjUE-_mZE03cTtlRoXENz_k1hF165XFs0OHoCAdhcVtqIRa9ZfJo0DkHj3D8bTkCjS4Jac_miG9lIudEhgbAoWr-TXVwE5x4QoC51BA3WVvECfLyZgqG5lRsN2oDt7X8SyxSSvtri0KfDmKgPjzMFslPoJRGP7qXmm6B5KuoSLfeD7eyoq6AF_minbN3HGCj5FyLvWeqFzm1LXlBxIzVnjfUR2u68wvJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=IhRd6kZf7ab0WIuKV0T8fak2d-seNJkb1R8gWE6V8eg-ZLgvZQOyzaJnjzNS7Ze3sHUcUuobOPAYzN4-6eyG6TuHk1kqXolTCTWI9cm_gW0l_jFan17UYjUE-_mZE03cTtlRoXENz_k1hF165XFs0OHoCAdhcVtqIRa9ZfJo0DkHj3D8bTkCjS4Jac_miG9lIudEhgbAoWr-TXVwE5x4QoC51BA3WVvECfLyZgqG5lRsN2oDt7X8SyxSSvtri0KfDmKgPjzMFslPoJRGP7qXmm6B5KuoSLfeD7eyoq6AF_minbN3HGCj5FyLvWeqFzm1LXlBxIzVnjfUR2u68wvJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuLln0Otej8nbl76R15_4O_frj5h2Hae2Vj1cZS9Mt-1F2TIb9vCZJdz3xUCgS992C92T307pJmAwapJUekbkGB3JAwQqniHsqOj_1LHjPpHWsJIac8B_fx2fbVvD-lKinAtmqit8ixveWW-qc7jDIYI3CFomCb9NgAEqPJfkEsL01WkKGy3CAceYQmtMNBHWpp0U-pDAxQEvwzT_BNGR0LeGhxoVZGafmtxsWut20rQahQM8mypvyCqshNCx6Fb5Al7P9EHylTPtcPaKFsszCe6PzdfYy8VrYEl1s-C3N61WUJ447jgMMj_UPM4Dh4v6nUlxUlxidG3XBqi_W4YHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9-Rltr-augYRzD6tsEXCe80IyRSZoWpB9MCwe5SnCvS5Ycddi0yMarOTFTyR4xZwUmEOaSSeAiLoZsqBTNthXfPg4HK4SOYHLkbK39AVGrVRSFsl5CoWhohZUfggG4mfgVZmTA9oRqngD_xP70-D47h30sKsKYccDd6xGk_uTE0ysa5DGIBhY6-ylbyMOnC6pdcXAEGguVRD__80CvOoLZMNMI9RL7AFb3KLj4UN_AREN5xeBfhduwaoLadLheIcjjYeBmsJ5jDVX3AhNI0pvjNUGi6qvff82eJxsBrx0fMUIwPhjnNYklWwttKo0n4J_1M-KzOz1gZ52vxRRul0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=B7IrK9Edb4C0qifrKsKy7HSq25439zj575SgJDRW3sRtrSrEReDbU1ZrocWA1KO79PdPEkzhCgKZHznnILusmrnqFpo0u0n0Q64mbtVkOYTE-hLY-t8VeKbaR5ox3VdQAz8nB33hZh2sCfVDKQuAD90C2Ad7Ymv65FTmt7kQr6LmeKCC96-RxYVJOz46x2DVO3O_KH4AdFJYIibTBst836z5dKKUrzbVw2oTUdbnlrsDb_0QxvE5K6zmtNS7oG3Bh5MGbrfwDfjy1dK35D0Io3On8ksbyE4h4t28yBmvmm-TR3zwu2nOGppZijaX2-Q6_s96rLzUzs1JNnxo_Lutdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=B7IrK9Edb4C0qifrKsKy7HSq25439zj575SgJDRW3sRtrSrEReDbU1ZrocWA1KO79PdPEkzhCgKZHznnILusmrnqFpo0u0n0Q64mbtVkOYTE-hLY-t8VeKbaR5ox3VdQAz8nB33hZh2sCfVDKQuAD90C2Ad7Ymv65FTmt7kQr6LmeKCC96-RxYVJOz46x2DVO3O_KH4AdFJYIibTBst836z5dKKUrzbVw2oTUdbnlrsDb_0QxvE5K6zmtNS7oG3Bh5MGbrfwDfjy1dK35D0Io3On8ksbyE4h4t28yBmvmm-TR3zwu2nOGppZijaX2-Q6_s96rLzUzs1JNnxo_Lutdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh486WjBpZ7gkICc8Q-VKYKCjfEtFarNmVRj-u95aN17p3Cc0bpxT7OpRvKDd0-Sauk2BIwoRZws6g9AubZ7pN5E52kynInwBhhEPVVLAaS5T9iMQvjA_m_8W3WVkW27fl6HSYGxePnDjyoQgI7K4cnWvQzq0HUTriGDdU3DZP4x8AcFcmil0RNdzb352eKzRVJVKXU1yNjT8ah6Xj5yF8gJg_NTU581o02Q0oYEd4Ejrkv_SIlcQzKICkQDgA14quAPCClGgB8Y8i2zJTuNHDoOnw1kdCcizW8nfmaFnwCisqVIK1lTA7tT6YujGLLVFZsjAF5pnWSzk94uu0rwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=OOr03-nHO3N4W673CQBEFiPpcy8lZi_uRFx5K1xK2aEvU35eOC-8jAvwQ63z18slMSvUNOOzawko-OV1SIlAOze1alLmJL9nG-jOEKr1oIb268t6-2QV7Y-lqy54QjSfe45Hn-v4Z9sa2Vl-JWj9rBZJPGi4ax5_Ns8edzBDHlcXjXuDmxtHo0bLXkeQIGV2OMOR7_dWj6bLclWB24YOTXTQna7rShHbHbcHgLedK5ppxVJd0a_0-6la2IWUWWi1d7zZzHJXP9TUkZnZXCddoVQD3D8EI5IqF_REIANvcYWtfboURy1PFH3Iv9WqpmfwH0JQGbRDYCSOrNOagg9ODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=OOr03-nHO3N4W673CQBEFiPpcy8lZi_uRFx5K1xK2aEvU35eOC-8jAvwQ63z18slMSvUNOOzawko-OV1SIlAOze1alLmJL9nG-jOEKr1oIb268t6-2QV7Y-lqy54QjSfe45Hn-v4Z9sa2Vl-JWj9rBZJPGi4ax5_Ns8edzBDHlcXjXuDmxtHo0bLXkeQIGV2OMOR7_dWj6bLclWB24YOTXTQna7rShHbHbcHgLedK5ppxVJd0a_0-6la2IWUWWi1d7zZzHJXP9TUkZnZXCddoVQD3D8EI5IqF_REIANvcYWtfboURy1PFH3Iv9WqpmfwH0JQGbRDYCSOrNOagg9ODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYZ_Zz6EEg3GlhCSMcSVVTT5YfmvIA-gwEZknix8-qXEzvF3TwL_OH5jkoPrJmvkJX3H8CDbQor-zrAFMmj2rBuCRkRE1PiWyczoYtvg4SV0qweuQVc-7mSCOcvQ_3mLXo1BC8gxEvMv71bKNA63c2umcpl7PWHig3g68jMHjGp3T-w4XmQLHkHpEtr_K1xDc2HabV6oTlvkvqVFwETwM2T4kPFLOn_ubMQ4KxJ4FJqszUTBoeXVq5p19qccLBNrtAMky24E8Bowz1gvaZYjtnbX-ZI3RQot0KAWiMtZDELtdcm0n4NAGfrJCYz9yPI-_85MRLKii3I5xikkTJKnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq4hD8ZfC4nVLWmEZxaBHIDRtua0QwcG88t3AMIXgsbzHq9jVAs1PFGyBc2Y2o82ezRiiZuxee7e__6DeiSK9wDLeEFpY8fhLBMJ3UN9gvDY1vx48AciW6vsE5_9Z2c87YFxJvGx4o3_D1dhsIJoPNtD3XRnKGFU4OCx_zWcxkQWlr06tn9LwHP8Ud31xRjGuEnNu0ZnYktkpv8_1Z2_UV437lwB92VhDB2tX-eWBxzyyQHXSUb-OtCUrsllqUORHycSOKxryP10kvKS_ULwiIYFeFert5GdW310Or4Cc7iZnWB6X5pwopiw5gsM_O8qRDQtQexiabe0Ra2ELy89tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=sLTMmVbZRdKk_HR7v8T9MS33osj55_O0JFYBwktWOjKtznuBKz1Hvh93DSsumOEq0L98zmOrSq6HAOsqgDKjE2iZkOA0HquoxtQIEkPxwqJShv2Nj4-THRZDpztvddaz_7K_PG96St7keFiz-4d5Ld0XYE3ZTR74H36C6xiRPRGwvhsSqqyVPC4ceWLY9PMKdYWbKpAigT4O_dy2zh6aU_tns8O3y-OL8WWMN9SXJ3MVBG7usAalaACLXgrYhiufh2l2BMSneWh6nP70kmkepq8IuziQJvLbK517_gMhDSPLFQRLdh_61s4wRtYtt99N50qmWSqT4MHg-F5UKKrq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=sLTMmVbZRdKk_HR7v8T9MS33osj55_O0JFYBwktWOjKtznuBKz1Hvh93DSsumOEq0L98zmOrSq6HAOsqgDKjE2iZkOA0HquoxtQIEkPxwqJShv2Nj4-THRZDpztvddaz_7K_PG96St7keFiz-4d5Ld0XYE3ZTR74H36C6xiRPRGwvhsSqqyVPC4ceWLY9PMKdYWbKpAigT4O_dy2zh6aU_tns8O3y-OL8WWMN9SXJ3MVBG7usAalaACLXgrYhiufh2l2BMSneWh6nP70kmkepq8IuziQJvLbK517_gMhDSPLFQRLdh_61s4wRtYtt99N50qmWSqT4MHg-F5UKKrq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=pFUUR0uSwJcFhmufWG3f6KQvuzEHZ3uank4bTedH-bChHxzoX0mSecPw_hTcVBbKsj8i-nD_9JmszhqVJMBIfTDa5iRMj4Ob2zChCTeA1J-M1jfrGes7AWFk5D76VKRMnug3ShPFQPco1OYBb5ZwaHCz72tqv56VfVBqBK8PJioiIgE30RIdcguIue7mFVMBjL9QDD4czxTNAlzXY7MZvsf8LGXafOBtCMb8q6xV-pjh9fs0D4L9kmqjonCD95qjutNngfwFrRWSwVpFVKf8X-Rq563RvMqsX8adMMf6oi6XLgqVJ5zmuK2Uyl8wiedC0Y2GMdZ9Gvzd35Rp9XXnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=pFUUR0uSwJcFhmufWG3f6KQvuzEHZ3uank4bTedH-bChHxzoX0mSecPw_hTcVBbKsj8i-nD_9JmszhqVJMBIfTDa5iRMj4Ob2zChCTeA1J-M1jfrGes7AWFk5D76VKRMnug3ShPFQPco1OYBb5ZwaHCz72tqv56VfVBqBK8PJioiIgE30RIdcguIue7mFVMBjL9QDD4czxTNAlzXY7MZvsf8LGXafOBtCMb8q6xV-pjh9fs0D4L9kmqjonCD95qjutNngfwFrRWSwVpFVKf8X-Rq563RvMqsX8adMMf6oi6XLgqVJ5zmuK2Uyl8wiedC0Y2GMdZ9Gvzd35Rp9XXnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftwonOAO4qzCREG99JeO0uLagxPYPMnfTTPCi05oi9kYq8MIPJBIqhmhtQsfttlIlDVGWrh4_0_aTF4IIiiMnZL7Fmdqs2RvHACtX5nPUlItLMfmtssAyGx7ALynnSWiRiWohl-stJqBQGQmdi_cJJ3cXDNSk8LrsYn8lnL4BYvulWgJRWrLzicnoRCRdomjGunU_RRipGRc411HFSHKlemCoF-s030bk4Y8MJd2d7hDKTQs-h1giZx4IzwClHWmEnlnLIkIc22aa7pCg3Vf1dP06WAmXgWb2qd7dzp830xFukpvBRiEW8pU6A-1XZtKALWO_16SiUNF5lFwtnDBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNd3WbSMX9DywvVGOHoDAh03AuRcqNg6FUFG24uFmUQVVJnoyASOoV6Qy0CQXaJxOmaGNsSFUREozGHeBvw8_SWyvN4_x4p1Sy8cEyK1ySdunAArYteVKyuRo29RYRY-gh-1f5q3Oqi9qxOT3sntWgEgfuH6RZ2nyuAIBo4o74FRDNG1S02vNzItGOLD_2qLdTFyG-ixX-w1cTZQJoLggJkmlEH7tOSMQmDbdDvdjOUNR-8JtPYZoxr6r9FEUStCGWopyy0v9VsdqIWcggEy0UpHkAduJ7LH-wBiamyDOgpHqnZNsl2vtB7gJ87AcGhIGx5_ni7lk7YfTyJRH9UboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP3B6apZwvk25X8k8p5YxgXauX8TzXyO9rC-pbATGwC8JZEncW7BpI4NoFbJTwEsvJxbFgQK3FOW1OsOjwd3bxzEfVrKDdFRxN2BQJvVPucibXI2T1lZxk5HUXhH60H5ohHjFecoj7KewPkiSdwHBAEJCKQD_a3ZUgAZsXqO4w-Rpc5Qa0hAzT6rDkynDPUoSo3Ggj28cXCvHb0H3-nBJqb2KXHBNvDB31e6whPrhrakrGI0mxcZF1frI5BxhGpTmO6_B3DIC8jkFEQjkixDk1exxTV9MgjKgpPyPoxKzQ8ga0Ivza05tl1NyK6SePwAjq6Ps6KEC8EPvVF8XlgbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=qlqJOTRTU-ULU5Qrz-SIMJTKeDBWHPmJ7WKa6vfrQTcx-EzX3mhUY1RQu6Zo8AG6FgiEGReJNtCGroSYDJBIU4EEFnuwfSXUtFYp2puohQrMYeiVaujDcBfDKukh5wNfu0-vXRLdZrR2m8gI4C8UVGXgoYd8E9kq9qJJ3ol970AHx5Zn8Ip8fud2YKckcv4bA6bumUqnDCMSsxjNea43BwEtodXHfWjP2CcBizrbaXbxs906jWzEt9FHix0K5bi81X44ER5chY-X55HI_mItPXzeTeWJA8tUJRkCZXlQvTeDI6n7U4m_isogpOlDSJECmkw5ux2XF9pcYke-rvjNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=qlqJOTRTU-ULU5Qrz-SIMJTKeDBWHPmJ7WKa6vfrQTcx-EzX3mhUY1RQu6Zo8AG6FgiEGReJNtCGroSYDJBIU4EEFnuwfSXUtFYp2puohQrMYeiVaujDcBfDKukh5wNfu0-vXRLdZrR2m8gI4C8UVGXgoYd8E9kq9qJJ3ol970AHx5Zn8Ip8fud2YKckcv4bA6bumUqnDCMSsxjNea43BwEtodXHfWjP2CcBizrbaXbxs906jWzEt9FHix0K5bi81X44ER5chY-X55HI_mItPXzeTeWJA8tUJRkCZXlQvTeDI6n7U4m_isogpOlDSJECmkw5ux2XF9pcYke-rvjNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viIFil6TbggP3cKWvXq8fGqJ5hCqa6jaJgUo1PwjXXWwqoi4edmvZS8FeoU-mqpjhcZdimCngR0NWyrXnRrhjoB8PxSLrFdQoC3p5ocO1ajG0jRm-GkWKRyl37BztPFFBuYIV84_ZpI2IzWnVfm-fPfDgfn2YKVdlLTkcZbHqlJszAvixDr42z8OEizptAWsAZLx5HN-GCfVHgTaXY1I3VGxd74g2dHBe7Gv6xGn_zNvA3t7-L6CjV4jzLQqjCpGGpEjxQQgqt7xBFY-WOrwRhBhW4RjznJrUCxQdZBAYxcs2MjhbOS2sXigy1CSqVOi1lht5EQDaL6-5lLH1TwZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTVe3wZKErxmoSUDbhdP3qoAxYbNp2FCZdNNvFUPQeCo2ovS_V8pKKsd2M0HNa8LJ5O8BfFGiwBbzr65zVnEYWW9wrPkBipKWUqZw0AsAZpS_t9RxHVp89h0vfTxokPp2-UddZLGtBm8m9nj1UT4accCKPH7J1BkLIYabJhjcLOBa5FDKokNHtcUk17wWRoJNU-OIJKbqVNQ_3xdpIXgdQ3wP7UNS_VK-AMyohbLauJYCul1y9JdInsh_1NqdhlWx9ioYR_w0keUujmAU-4xtDFEdimeiI9JZg1VBhDvsUaUIO_C2KaVarwW5tmNbs_mDSB2AgSuDYDyA-RmqNpm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc13hNgfeqM3ZHCFX6e8KAf-YMohvCdlXbfXlQ6SXpFJoKl77ndjHmea2nbtFsNBLdW_suDGJ4g0lGDOfeXy2JYWisiv4PM4ptVKKjkMCxcrTFxVRYzwIyhoWMHaKekCDKv8j4kBf_K7FjG6mrbofz6NHFYegJy1Jle2RDuoaPYDmU01J3IjT0eI8EiVEbmrLynrBkDu8N3PFtCsXdpQSWpJFbMd6aiPiUVX-WvcKzqp8xkb8DtDoSOlXpkEjWK9mkpvztWgpzVbW24OmqUCz1U3EHOfoL7HjMbAUe9yWzlzevfMJjdoql62KFuyMpMU53XWoV2Sbpi25ql-AlQEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E00GIaVcpQNOprsuvDL2x2lhueRrKt3naEbeoase14fudrndfqYzWM19yeW3M3_JJCNDyJ0B48y7QjIsa6IXhqZlop_QEOy6au5g6gRJQQipLpTlxmSL7KlubusoATXlkusot4Cj9vGjzibmFFKUmcWUOlQgQW_m39hslbhmylnH6bGLLg3Bd_0qDaPjxRWBPuIeNJ2Xr4bTgdgR_Uecfasb8mZL7rOHiOC1nFfrJ4xRuqefeka8HRCeSHUQsrg1WfoBOqwSeCe3Z8XsV8qLHPMy_RWt91zPp-APotYu3I5PoGfI8hXI_PcUGP4df41LfoLDVCHiKpbN9mZhK4qjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=TMefi1X3f-bEaooeaiFQv8f08FrDOhUbDAecPiEp_R-UotiAcMamYWvZTPA8S8g7EQvB-bSMBb5cBZ3YurATplUzk6yBgYF4ksSnr68N7l3SFOiJ6XmTa6Y_5q0IHSAOjFcVidcHbbrU3U_gB5ZB_AJttg0gQcGPnIf9VH9al_Ml67rByMxAG4hdUJnohUU1AdrdtG5-kUba9P6zDwUwi6FOCWpiafFHoBXbFbMqb4pBI074IYZUuRVuFgLdK1ZA1ncKaIxgS94Peqq-EPAHkc8xxJrbpGY0N7SW-xMrZdbKvxwXGE8BQg9pyigsFE6Ahob1MNdj4ihzvQaZej2ApA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=TMefi1X3f-bEaooeaiFQv8f08FrDOhUbDAecPiEp_R-UotiAcMamYWvZTPA8S8g7EQvB-bSMBb5cBZ3YurATplUzk6yBgYF4ksSnr68N7l3SFOiJ6XmTa6Y_5q0IHSAOjFcVidcHbbrU3U_gB5ZB_AJttg0gQcGPnIf9VH9al_Ml67rByMxAG4hdUJnohUU1AdrdtG5-kUba9P6zDwUwi6FOCWpiafFHoBXbFbMqb4pBI074IYZUuRVuFgLdK1ZA1ncKaIxgS94Peqq-EPAHkc8xxJrbpGY0N7SW-xMrZdbKvxwXGE8BQg9pyigsFE6Ahob1MNdj4ihzvQaZej2ApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLqMuIDaoeCuTFTTCqSr2aFgjV4E4PQdsxiy5QtnjOmHI8-I28RlfhgehnFgQlJ2rGHBxg-x5jDTLc3lot5E9C2PjJf3-l1cfNeYag031M2EYq0cYi81oZS8hVr_VeAAcwqPlzQ5dVHnFI6VdVt-SrSAXqdqVpIpGRK9t4mygwRJoWKinG2PL8XPqJ8G7f7zQawz4DpTIXQkInMAKdiEjEbdSaIS9kSeSqmG1_imOsBFqFfQQ5komo8yzO8JJyLwA4SKvuFQYQCDAsmo9lbVIV_umj4RfTRWwGJ31dX1DmjJJ0JchYTy1IP_WAV7_eMJVWOlBM-1wE9OhEbyCpYLCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=iIkxgZ5rHn2MSZO0s-rrzveD-7-ZCQkpwyYuHEY0XGyDGgI2rjvgPOGnSINkUkE7oE3IgIofT4vvoYHYeaBPDtGXkiAZloeBtznTffkpCpfe1JjuRquKAHtIgnEHSwFSRj39k5a79L9BV7BoMo79bZ96Y3X4y388k3r_U-c-pQ378Q2gdSVawGqkT6OVBAwFm4UJNph031yvVI_1_OmDayqUWFaLzkTi91eQPP_cNnSuOvpoAHDOLb3dp1_0m20n5_ikF_2fsaRv1ianzDkv6Rt4tjgm-ybitQotPUKu8dNZ7Uf6yVHxhcvymCAlci-Fa5C_wykqYv3RkyQviSDj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=iIkxgZ5rHn2MSZO0s-rrzveD-7-ZCQkpwyYuHEY0XGyDGgI2rjvgPOGnSINkUkE7oE3IgIofT4vvoYHYeaBPDtGXkiAZloeBtznTffkpCpfe1JjuRquKAHtIgnEHSwFSRj39k5a79L9BV7BoMo79bZ96Y3X4y388k3r_U-c-pQ378Q2gdSVawGqkT6OVBAwFm4UJNph031yvVI_1_OmDayqUWFaLzkTi91eQPP_cNnSuOvpoAHDOLb3dp1_0m20n5_ikF_2fsaRv1ianzDkv6Rt4tjgm-ybitQotPUKu8dNZ7Uf6yVHxhcvymCAlci-Fa5C_wykqYv3RkyQviSDj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
