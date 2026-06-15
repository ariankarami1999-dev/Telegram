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
<img src="https://cdn4.telesco.pe/file/gpgC7JP2ulAj13MLrXj5_iMYk0R6E2sfXqQmrBryg-Moud7_cW5P-adcM1F2PovnVR2fkS9QSNIzK7nNWCJRt1H4vBg4luNd7PxbbfwEmse8AlwHjbOZepFM_Uxw7qK02po_2PCnZcnFu9NDnGtwiXTBV2KRrn7TFnymmrokhtSimxXYwPxeGml6XxbXLPcZM3ouOXjzrlIYIXF-d4gN6C4em_vCwoC81tNBaJ_O3-bDfEY4x9iKkRU8U2J_lvymcr_QL6cbBTPLzoaULpDaMWjQGoueFhYKkSCL0h5X_d5BARCvexvZJU5FoWdXBcyxFdwk91UCL_7sZ5U4fmRxQg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 03:17:21</div>
<hr>

<div class="tg-post" id="msg-128357">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvQFQrd09QjOduXEquOpSMrwxa6Ldb_Lixh13xw9d3MtqYFZwZIyjfvDJ8k_pwYprrwajqZkHY3WPH-hnPJaO4GClcjIJHGyNbGPn3b9K5UjeSKlBQyeooPy4a7HcRU5Y6BF2_RdgvbPeOvzMXeQyqfCIlKTQ715q_2R-PJMzjhGCi11F4cnKjT6Gv-O_wHnhzUHV_dMXkSkT_Uef5QoUYvCPsiVxuSnatQTg5sSJSjPQcwgUlUcx6Ypqi9acdZjWB9hZrunRaYItPPIORZ8EnQmRPlagCNSUb8sjhIld16Fn0zcG8a3AO38Z2BlQdLNsiCThWdAQKimcP1vt-cUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد.
🔴
داستان پرداخت ۳۰۰ میلیون دلار توسط آمریکا به ایران، خبر جعلی است که توسط دموکرات‌ها تبلیغ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/alonews/128357" target="_blank">📅 02:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128356">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مسئولین امنیتی ورزشگاه So-Fi (محل برگزاری دیدار نخست تیم ملی) دارن تمامی بنرهایی که عکس مقامات سیاسی کشور درش هست رو جمع آوری میکنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/128356" target="_blank">📅 02:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rLV8ireufCibsPgVt7WWfZjuePROIOKUuDc4xaxTaUCWs04C7uybD2U8bCxRBNKA53K5l3hohEk5ZRhm_aPPZA6RFkI_oRzauNlK5S9xPYl4re4oMtx6_C57T-QiswwIbAAdB2vS9rztIrlP7O3wTEYdIIzLiilAPom_Vp1m6o1VDLDs1enDyrNuHvGORozHrqFZEBoOatMQrNJtV-Mi2aAK8Zs35AaNdejf-kkxuSo6M3-sfZD_ajESDF5AQr_-EBY35UZZDLRMFARnR-X_-834Oey0vIF_fW4km5cZ8JxHRJU1ssV4VIt6lMHgJMlV_KUxZuv5hIB_I1a5FxRQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V7ebOT-2yGsh26_AMGjNytu3Fi3nKC2mEj9_sjtxVGqg0nCmtdYw3liF2_xowEHUCDt-m_gw1DpKn-nbKn28wS17pqDttcSTMzWVTGVUAV5U5kUmGKULuCB-D1brLGpiLiAkJJzsvoYi6226lzwZdsQk0LGER73-uu0zTppcrJf_vlYb9TUv6R8T6rnryMECfhErmi9pwfXuqUoScY_yVJITrYBEc3CsCkj-Zau_kSV6NUAxsMg0xfSEA7OGGW69FyY5fEPreENlM4H1myAK9mgmytt2Sm-lqeif20BToqAPKxiKXTGJKIMkKCsqpnXhXk_v97o_qYdNEB27eNKdrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا این برنامه قراره تو استادیوم اجرا بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/alonews/128354" target="_blank">📅 02:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67b749fc7b.mp4?token=M3_yiO_ZEv8RcfoMGU1YncLlQGRXjDiSOFU50aHlOsZOk7n64-UdwEcyLtC5iaZDa66LR83-cgdvQpxpnCMM8Pea3BTI_fg5ikgmcYiSRp7EF_1iefZpNFmgwmJPNCiIRTcHEG9QQOCx_JgIDcAg1JVfS7c2NyW5RugCse5Oki5iCUFr4-5kIhvKLv9nHWJolgR5Nw3lOF51OwSvQ2x3cl2o0hpLdPZHyU0p0TTTjKZVNk5ydetx22OL-tDUV6uZ2lOwtw34NAb9Pz_qRqxd47tKMtaLblAYDPuPnK6K-Zg1_aUFzvSaDxQjswwPkYADj0W8ZeKuI4iMU9OCIxfRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67b749fc7b.mp4?token=M3_yiO_ZEv8RcfoMGU1YncLlQGRXjDiSOFU50aHlOsZOk7n64-UdwEcyLtC5iaZDa66LR83-cgdvQpxpnCMM8Pea3BTI_fg5ikgmcYiSRp7EF_1iefZpNFmgwmJPNCiIRTcHEG9QQOCx_JgIDcAg1JVfS7c2NyW5RugCse5Oki5iCUFr4-5kIhvKLv9nHWJolgR5Nw3lOF51OwSvQ2x3cl2o0hpLdPZHyU0p0TTTjKZVNk5ydetx22OL-tDUV6uZ2lOwtw34NAb9Pz_qRqxd47tKMtaLblAYDPuPnK6K-Zg1_aUFzvSaDxQjswwPkYADj0W8ZeKuI4iMU9OCIxfRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع ایرانی‌ها با پرچم شیر و خورشید اطراف ورزشگاه
@AloSport</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/128353" target="_blank">📅 02:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=PL_-Zk9wwyP-R8YmwJU6NBMxpuNwWvreQoWNEHDeoPGd57Go1OadpyNtbTuHzb8ZvTdCZH1C053rOeNd7MkCxFncPlX5uOX4_FDVQGsjObpc6VQxg_RZRt2RvqjvjjWcyFU6DynM84SSU1A9dk57U2rQSSb42L4KAbw8wt4Nmng8sl4xhO4Ln-3BTYMWBb1Wp8XAZuvJtVRnVuze7aVyPvCWYLF3iaDA-P7lV9zaLHYh07Rj6caCWGYiaA0LfrUTNWan3MmIUpwDqR0NDdZKuzbWi2WIMtCcYn4h41e9DClrZBBQyvlqyPzPD7DYhRwB0yJObVv72HF0OooMj78wKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8e3f17e9.mp4?token=PL_-Zk9wwyP-R8YmwJU6NBMxpuNwWvreQoWNEHDeoPGd57Go1OadpyNtbTuHzb8ZvTdCZH1C053rOeNd7MkCxFncPlX5uOX4_FDVQGsjObpc6VQxg_RZRt2RvqjvjjWcyFU6DynM84SSU1A9dk57U2rQSSb42L4KAbw8wt4Nmng8sl4xhO4Ln-3BTYMWBb1Wp8XAZuvJtVRnVuze7aVyPvCWYLF3iaDA-P7lV9zaLHYh07Rj6caCWGYiaA0LfrUTNWan3MmIUpwDqR0NDdZKuzbWi2WIMtCcYn4h41e9DClrZBBQyvlqyPzPD7DYhRwB0yJObVv72HF0OooMj78wKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارهای مخالفان جمهوری اسلامی در اطراف استادیوم محل برگزاری
@AloSport</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/128352" target="_blank">📅 02:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اکسیوس:
در تفاهم‌نامه‌ی ایران و آمریکا بیان شده که
ایران با عمان برای ایجاد چارچوبی برای اداره آینده و خدمات دریایی تنگه، با مشارکت سایر کشورهای خلیج فارس، مذاکراتی را انجام خواهد داد
تا به توافقی مطابق با قوانین بین‌المللی و حقوق حاکمیتی کشورهای منطقه دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/128351" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128349">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62ec6f238.mp4?token=YGTaz3Lx-sfeCViFGzQth3eyZhr2Nd7FGFXJ1dTV0b-9AvwMUkWuv87LpegYmzOo3bwMAzd15Q_Ldj7Km3-7tJ4dq2AXgle9wwjOC2qFpuAei4yr04kda4NftXygtLRu8cuhmW_MzUfl23KnVL6Qwwuceduhrz2IsYg4yilKeQEcXzcHbAoHaPNrSjzI7vrMwQ9hDyvbyEOT8PBLyDqfuTeCgg-vFICntpmpNdJMDSz237A2pBcxuXM23q9uVyTGUemTu4EvxJbpKnphqsHACtV_JGANOlByrqdHQrXY31pFc3CipXl-wKq0Aah9CnAuil3sG8MVmUgp-q0w-FHIMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62ec6f238.mp4?token=YGTaz3Lx-sfeCViFGzQth3eyZhr2Nd7FGFXJ1dTV0b-9AvwMUkWuv87LpegYmzOo3bwMAzd15Q_Ldj7Km3-7tJ4dq2AXgle9wwjOC2qFpuAei4yr04kda4NftXygtLRu8cuhmW_MzUfl23KnVL6Qwwuceduhrz2IsYg4yilKeQEcXzcHbAoHaPNrSjzI7vrMwQ9hDyvbyEOT8PBLyDqfuTeCgg-vFICntpmpNdJMDSz237A2pBcxuXM23q9uVyTGUemTu4EvxJbpKnphqsHACtV_JGANOlByrqdHQrXY31pFc3CipXl-wKq0Aah9CnAuil3sG8MVmUgp-q0w-FHIMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طبق گزارش سی‌ان‌ان، هشت خدمه در سانحه سقوط بمب‌افکن بی-۵۲ در پایگاه هوایی ادواردز جان خود را از دست داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/128349" target="_blank">📅 01:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128348">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS_HDsV4-9499--7pCHYU-t3HaV4tW_9TGMPYRnLS-38tK1BY7vfdcMY76vaenHCLMaYmUOgegzKFBdBGzyUhjo3GE28OexyonJr4W50VooTvxRZiK2bpTSWbI4UMFzJzb7mgsJbnV3oRXryL3Z-loPvOwEqeUoX5R4ljdGaaO5QtdVw9Ja1PVKrRs90cZx1MI6Bma8BE4eIkvAsrQ0JeXUnx8FlpLUj-VGdo4zlOJilLZeq_Ipy4ZchGTlKsMkHXyJ1i-uheQG-0OPsc-P1pfyTndxvupa4m8BfqHmLMkjfoXsMnLtMagFLX-pyjm6GuqqoJVqH8tl1aTaI434pCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش فایننشال تایمز، دولت ترامپ آماده است تا در چارچوب یک توافق نهایی برای پایان جنگ، از ایجاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران حمایت کند، مشروط بر اینکه تهران یک توافق جامع شامل توافق هسته‌ای را بپذیرد.
یک مقام ارشد آمریکایی گفت که واشنگتن درباره تسهیل احتمالی تحریم‌ها در کنار «یک صندوق بزرگ ۳۰۰ میلیارد دلاری برای بازسازی کشورشان» بحث کرده است و تمام مشوق‌ها به «عملکرد» ایران در رعایت تفاهم‌نامه‌ای که قرار است روز جمعه در سوئیس به صورت رسمی امضا شود، وابسته خواهد بود.
این صندوق تنها پس از یک توافق نهایی و پس از تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و ادامه مذاکرات درباره برنامه هسته‌ای ایران تأسیس خواهد شد.
این پول از دولت‌ها تأمین نخواهد شد، بلکه از شرکت‌های خصوصی علاقه‌مند به سرمایه‌گذاری در اقتصاد ایران تأمین می‌شود و در صورت لغو تحریم‌ها، کسب‌وکارهایی در اروپا، آسیا (از جمله کره جنوبی و ژاپن) و ایالات متحده ممکن است به آن علاقه نشان دهند.
ساختار و مدیریت این صندوق پیشنهادی هنوز نهایی نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128348" target="_blank">📅 01:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a7cAZEDpPQ8xnmcCnm-jtp_0s2WUgXObPATgdx_F-_wSEJqfuB7_i3InuHNLftOaoQI-6xMGGOQXL7xhd7hhvfitPNdRPO2r2NzzJSF9_dgt8bnpynNiWaFbRtSu0kKfPAoaT05MOBl_uDwb8i6CNy2VD55AJoR4WyoTnqyZoVN-soumeQvc916D1yOgacOUvi03SkvhcLtwj-AaHp8DAka4Eswzs6Q4TtJ-Xfmzs_PNODF24mQULWcy216xv2cNVPFzOtTpuku1EqgsMi_pyx9vZhb3t3Wa8h4b_vFnAo2NLLky09ZRnFY0CQddXX7uxf64BLn_ga-j3JYlCLhodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
11 جنگنده A-10 در راه برگشت به آمریکا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/128347" target="_blank">📅 01:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-poll">
<h4>📊 دوست دارید کی ببره؟</h4>
<ul>
<li>✓ ایران</li>
<li>✓ نیوزلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/128346" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3033df34c.mp4?token=PjpCtna2ur58QgD1AeBtcJOHiqCUftLAVjqJ7iyNjCc_wrSkEIKWU0F1I1GyhifT9XXkjj1TSIyF65BlfMr4N_a0QP_51IuXO8MHRaRv52pxnS6JOueFTANTL_gWaRALxBloNS6bnx7lGxm3vGH_aARiGxhN4dnalSFHohGfkwy8ZEptK36C2rTjw-3scSubR4B4Mf2WtDXD67Tv8oT1gmzQMM2j46uB_rEJzPONAMJINWZfP1M3hbJrNWHIarKkl0_nMH0NRASBQNknJpOE_MjppZ_t5ffDF0-6FIW7xkROCxMCqAZqSDy0waa1aichI3HPfWsRU1hBMkJeE2o1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3033df34c.mp4?token=PjpCtna2ur58QgD1AeBtcJOHiqCUftLAVjqJ7iyNjCc_wrSkEIKWU0F1I1GyhifT9XXkjj1TSIyF65BlfMr4N_a0QP_51IuXO8MHRaRv52pxnS6JOueFTANTL_gWaRALxBloNS6bnx7lGxm3vGH_aARiGxhN4dnalSFHohGfkwy8ZEptK36C2rTjw-3scSubR4B4Mf2WtDXD67Tv8oT1gmzQMM2j46uB_rEJzPONAMJINWZfP1M3hbJrNWHIarKkl0_nMH0NRASBQNknJpOE_MjppZ_t5ffDF0-6FIW7xkROCxMCqAZqSDy0waa1aichI3HPfWsRU1hBMkJeE2o1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : هیچ دلار تخفیف تحریمی یا پول بلوکه‌شده‌ای، نه از آمریکا و نه از هیچ‌کدوم از متحدای ما تو خلیج، آزاد نشده
🔴
این امتیاز فقط وقتی بهشون داده میشه که به تعهداتشون تو توافق عمل کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/128345" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
درگیری عجیب ایرانی ها با همدیگه درنزدیکی محل برگزاری بازی ج.ا و نیوزلند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128344" target="_blank">📅 00:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ونس معاون رئیس جمهور آمریکا به سی‌ان‌ان گفت: یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
🔴
یادداشت تفاهم چارچوبی را ایجاد می‌کند که به ایران اجازه می‌دهد در ازای ایفای تعهدات خود، مزایایی به دست آورد
🔴
ایران باید تامین مالی سازمان‌های تروریستی خشونت‌آمیز و عوامل بی‌ثباتی در منطقه را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/128343" target="_blank">📅 00:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuC4y-NHYUURGzX9lC3YZhiz-4ikKG0SSAbepu45WXKICUqHaYAl71eBAupDkLEGK4nAT_Q4seR4EAJg6XYaZ6XvjcMVkQyhXpmGhak2PnYBsbfSZT4tb0OqeFcb9HWqxtqGiU4bavxcBh4AfteaWJM_G65voF-1xzU3s55aSlLgT7sjf24qmXVOhtAWiL1KmjQxAPn9oeDO7n593ZfMgaA3S-TpXF1gVLPe2ITwM2yAj_FsrEUkmDfykJA3taMgnzcawLcFJmuTnMjxc5CXAgjrBXaaks9sSIv83EGIOOuJBOi6e-PvwWbhhYeIoG1ABi51mBjXix9FcQTFysJxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شجاع خلیل زاده:
ایشالا امروز پرچم جمهوری اسلامی عزیز رو بالا میبریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/128342" target="_blank">📅 00:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj0O40JclRZfMsEb2kZ8xp6gwY9EdpfrOduKgUGWExTJaldp6xr_7sZY9LrRS0GN3qqF_pdPlhSMJsgs0ZpvVyRqwW6mKYrY-HBDqeO4QGDWedh5P5j-hzFV0bTWREhrf73y1RuTgMiYZa2_xAogoRjdGdkqfDiceuc1AwAy5_imjgdtHaycXUF_fXmEtkoSbngquuSgyzu7YLlk99Kd_7OE7oqpcri_Qq_PQ1PnMVe7xMpo0msch8_s_h3ZD6zM9q7k6o8dq3_5FKM_PJMjbqZZdUQnXlu9iTCQpW_yk2hxm65QJKlTJ-r9178DPO73FSydVc1t7qOT2rtaz2Ki8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در خبری عجیب و به گزارش خبرگزاری MSN، به مارکو روبیو و پیت هگسث گفته شده اگر با توافق با ایران همچنان مخالفت کنند از مقام خود برکنار می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128341" target="_blank">📅 00:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">😁
هنوزم ۱۰۰ گیگ و ۲۰۰ گیگ رو به اسم نامحدود میدن؟!  اینجا نامحدود واقعیه
😎
💯
🚀
یه ماه کامل با خیال راحت استفاده کن بدون استرسِ تموم شدن حجم
💎
❤️
فقط گیگی 5 تومان  نامحدود هم 200 تومان
❤️
👇
👇
👇
✅
@TurboVipV2raybot
✅
@TurboVipV2raybot</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/128340" target="_blank">📅 00:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUb_peLu0E-gPlbqCqrv5dTZzQPLzqZs2_CnnbBuD4QrSxB4LqgkDqCpw0tWlt_lTwbLzAY1JPgD4mpPcT829R38OpNqREtFvqGGsxgYMlUjKH2tSVK7JUEIkYgv4dI4NBrJURnCHRM6rKbu4jB5geevEVMvIFYp5FjmMWVhei4XKlPdjJERcNFQdlnw-Bry3Vk_KVzxTK-uuEP7MS5Ssu8F2WCxN1Q0Y9F9VuQZXax7AzCVk3S2IS8WYc_Z_ZB2bbzaKu7wpo7manrQ4Rb_TA1whBOgi5IWfJYfN8FwVaq0XweovYVeMkdlDN5w3PpSIjTbbS-CWdCEf1_HufzFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
هنوزم ۱۰۰ گیگ و ۲۰۰ گیگ رو به اسم نامحدود میدن؟!
اینجا نامحدود واقعیه
😎
💯
🚀
یه ماه کامل با خیال راحت استفاده کن
بدون استرسِ تموم شدن حجم
💎
❤️
فقط گیگی 5 تومان
نامحدود هم 200 تومان
❤️
👇
👇
👇
✅
@TurboVipV2raybot
✅
@TurboVipV2raybot</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/128339" target="_blank">📅 00:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMJzPfZw71h0zNXV_2K14VFKfI93fOr4Cz1vpuhXfwSulUlr00b6htRL2d0CV2zvP-KSX7JkaAXe3WyziOX80kZNR_Tj5y7UfCbXKHD2-ucUv4okcZ0GakfVdds68mC4JNW9-JoYa0RFoGjeH6Ly5u2841OCqt4yLMK9xxayC_l3kH5qgvjTd8z2rD7U5yN4DdefTM2LLxPMWiTI9M78CJBSql_ATbbgipIszKiG3ab8W1Ted9Sy6hPH5KnzMb7SXjJ0FSfmwUXIxot7Pa64kX792eoXOlXpPaOqLz0ECJiILhkr5FbEJU3uvmzQdF4LalNw7JKvhc_U1NtVkzpvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو :
من هیچوقت نگفتم هدف عملیات سرنگونی حکومت ایران بوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128338" target="_blank">📅 00:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKI9sknibRufLjW-1FsIPIw8pivXXILGiLzJcNe3Bm9t-9aH8Q0jceGY2C5wgZTym94Tox9tx-tLGtDn4opzS9YK1kW5refYBlg8q9Mislf579KQR7SyKhxCeBBnDcFFRjcz6Abkzaj5GaFWGFXxRbE35ko_8YlFLSKqc8B7mMd3JkpkwgrqKNl8RvwoJbWUkwEPS0IsbX5TPMQE685AM2TD7SpBxtSRBPzz_yVuakmbZoikrh73AW6R7F9uDdgmgt7zDiMRH80IlGvrjTiRxBsmuZ3Sn27UD3RLv3IeAGT0M1M2YV0jk_IxpVMecTnFsPJ34UBpKVr7iRSE5rPxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرس تی وی: ۳ نفتکش و ۲ کشتی با کالای ایران از محاصره دریایی عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/128337" target="_blank">📅 00:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128336">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / خبرگزاری تسنیم : رفع محاصره دریایی عملیاتی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/128336" target="_blank">📅 00:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128335">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhrPY0x8RWhwCaHACiiZJiHmtTmqCDZvgr-uOqm1_sP-aVqtcB-3Rh1Xlxaq-2QMY_ugL60yhqs-9AI7VOtDIzx-VhDfX355yyVQrtQpDA4ecHZka7fHiGJ-d7z3ioubOcFWZHtWvO95c0ZV9t3JVu7eEU7mD6EPARN7_eOZh-pYb-ajfAA7OR5W_dkWSCoQ_9hvefWeaoQ8KB9Vyblm58w22Uc5StBMuTL2kRdAx_5CyfPcCEwJXmmJ1sKmc61xsiNJXQJ0YyADjfN7VG5p9EZgUYJdr8kV6iYh7-8ktMOxPRYquFj0jMbiYXc0cdUjiD6geaJfHeU_RFsSHaUVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار بعد از مدتها، هیچ پرنده آمریکایی در آسمان خلیج فارس نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/128335" target="_blank">📅 00:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128334">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ گفت تنگه هرمز تا روز جمعه باز خواهد شد، در حالی که یک مقام ارشد آمریکایی به خبرنگاران گفت که بازگشت به فعالیت عادی حداقل دو هفته طول می‌کشد.
🔴
ترامپ همچنین گفت که متن یادداشت تفاهم (MOU) بعد از روز جمعه منتشر خواهد شد اما آن مقام گفت ظرف ۲۴ تا ۴۸ ساعت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/128334" target="_blank">📅 00:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128333">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
الجزیره: اسرائیل بزودی برای نابودی توافق آمریکا و ایران اقدام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/128333" target="_blank">📅 23:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128332">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMkP_UMMfbgarBykXv_jmjAlZdeMQo4qj8ypm1u0ngv1EMHXiwZT8Pnd8r6ki11aZAhnF5Ndgwd6n9b99MzDKpsQ2HrmisRyXuHgGAVxLDww6_AJv4QNh4zBoGbL9Mu7pAOtKK7TqYlWLc4wSYzj35-G2Y2aD5dC9A6gISEN8qey0c_s3IAc_0_AGP7YVlckmQwpxQPbzFmAEJF0umj79XEgaBzRGWg4WJr-ZHeE2kf0ASmTvLrLtlKz9c6SSSCX75Lgvm-EI5n0xq_HRlkUbVKvk7TZ1JRXwn-BfhIBHKAxfSzcDUOe9BJ4-60jlVD9M7jsfnDJlY4na3m8osbnmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری ناراحت کننده از وضعیت این روزهای عمو قناد، مجری معروف برنامه کودک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128332" target="_blank">📅 23:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128331">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: تعجب جامعه اسرائیل از این بود که مقامات ایران قبل از دفن علی خامنه‌ای با قاتلینش توافق کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/128331" target="_blank">📅 23:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128330">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
حمایت ویژه سردار قاآنی از قالیباف، عراقچی و دیگر اعضای تیم مذاکرات
🔴
فرقی بین تیم مذاکره کننده ما و بچه هایی که پای لانچر بودن نیست و جنسشان از جنس مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/128330" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128329">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/128329" target="_blank">📅 23:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128328">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل قضات دادگاه نتانیاهو درخواست نخست‌وزیر برای کوتاه کردن جلسه فردا را رد کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/128328" target="_blank">📅 23:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128327">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نفتالی بنت نخست وزیر پیشین اسرائیل:
بر خلاف دولت فعلی، در انتخابات جدید اگر رأی بیاورم به صورت خیلی فوری اقدامات اصلی برای تغییر رژیم در ایران را انجام خواهم داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/128327" target="_blank">📅 23:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128326">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/128326" target="_blank">📅 23:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128325">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سردار قاآنی: باب‌المندب یکی از برگ‌های برنده جبهه مقاومت است و اگر لازم باشد برگ‌های دیگری هم رو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/128325" target="_blank">📅 23:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6A_cfKPQWHbaz-W1i11zIROOUFrnVQ0jpam7JupZLvri54p5Aot8KAiYBcKHhku6PsEPT1JNeakaA4G41YTXWl1fmoJyr327u72g3WvRYGxLFznkjAqNkiz-RKIkkuvj6hBkVp0zpdqSvW-Dlr2X2Ff8aa4yp7MrYi0p9yQDa6_kSZiDRmwsQgpz5psBfbxQii0Rc_hV8H1_S6cs3pd814AWd25RtbMAsItvOt-zPdwE9I32actHee0rAKy97cTszqY_uO4jLBY-j1m_3TP7cLI4mF-HfwISzAFldF8Ri0q_Qj04_PmW_qq23wVUrp2wDv79dwGpE6dYKKaDTt8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان از قالیباف و عراقچی قدردانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128324" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی کمیسیون امور داخلی مجلس و شوراها: انتخابات شوراها به دو ماه بعد از اعلام رسمی پایان جنگ موکول شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/128323" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آکسیوس: توافق ایالات متحده و ایران روز یکشنبه به صورت الکترونیکی توسط رئیس جمهور ترامپ، معاون رئیس جمهور ونس و رئیس مجلس ایران، محمد باقر قالیباف، امضا شد. اما بسیاری از سوالات حل نشده باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/128322" target="_blank">📅 23:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/128321" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی ارتش: ایران در دوره اجرای تفاهم یا توافق نیز به تقویت قدرت دفاعی و بازدارندگی خود ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128320" target="_blank">📅 22:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcn3CPr6DPpPbYsW7bBibRuvaBqdBDE8fVujbKbIOcsEwUKkjlOxTNdl8lkIxkzEUlbaW2Vm6Gx5TdlAQB3SqNXxUarOerka8PlOsJckBjQ8T9MiJUVsgWglIOOwVu0R6QvUcywZ95fMfAAGrOWT4J_rnt8gtQ1sO6y0VhZ3_cFlkvIPjGmwnJkY-HZsP3C4wCjJ6bxVzNcO3fht5qhUcPi9kBOa5gHTYv7bQxkE7S_xKWKGv6zGyQpAbABEGxc9UDqzRtKnXt7AjFkD0C6ijE5EGkJKz2TrXHz2DLz_Bm6NYRgeITXAJxnR4qXMEHQlnwEEwornPpVGrdbgZAYCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUdTr_xFc7QLzNkza7GUf-owsNmAzuOPNzoIxY9KmqaOgRJZblXQrtCZxgdfaXMx-aAkXpiqBI8u3K9mjbwIjxS3EwOo9HsFCyfCgsaqYrQMkYC49Cn-JLcrLY09hh0Bhc5IM_Qx-9egM3eiHc9r2W9Mk7MJWnvIa53zjf0nUOup3GCSm3uyLHBYS7Dho-F7MqsukLn7Crvs7GYcpgvCf8cQKc_kyCQz5OtkM_51jrEFGNMRU9iylKUDp1Y421wHNVK32T9IJu5M0F2dftMdRm3auq3sB7j3qOlNI3k7OrNGV6yl_Ldy-1v8kCCdymNJ0xvZcCt9OZPGceOzJyaA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du9YLa9m_ini_1k5aXZuB3kJnsvSaFHVds-q_ornal7lq6rhjLD7AwLOKZZXbbHjAL6DM8sVrPDisn25i2GpeSU5LpYfgqyRugCEMEU54TKHW_zqEchN_FkL2ePB_H8Azcf7D94wuCGmM7-iyYP9SERGDjN3hj6t1629BkvW6xY96_IYsp7ONN2HsHjUvH_g-ahTwFNs-y34yXXvyzsXgZ8K-62_War1u8uoYLi_asyGykI9UmVuYs1K9DkLQj7kfUBNDoQdxrNloVxFXz8P2k2BA5ZQmOaXG7TARM3K_pYrZXXI6yROeKqDAeiei3tn3mjI7rfOLmzVzMrQBbSRfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک بمب‌افکن B-52 استراتوفورتراس نیروی هوایی ایالات متحده بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
🔴
جزئیات تلفات هنوز گزارش نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/128317" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128316">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fea3f1828.mp4?token=CHqcQp2_dHDEZS2XBo8LMYgrD1HrIWwvCxWvYU9KUs9Kugh8Y3ySLoGCQEA-qB_fEoxFb2PpA2O4ZsfuDWuZ2FLaKc0X5KgwsqOgyBYLvNeAQ95UCrkyLdBkXkMKg8y3G-5chxN40YpC6epaXRmXQRbfaCr7z4_3fCq4Z5p6TXsfhZJiKmX8mVDP2c6SYVOo9Jb__q_LX4Qw34Czq_eypTHlSXASJQSXlONnVzc5yX63HV63WvutiwkdFwgGx3R6ctwtVmW6Zkd_OYDpDVKa6NomIbLzr5umFOlgLRslP1vw4Ow-B2CYUjU7n80D4AigchFpIQRnyk2Rwuk6m5YrDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fea3f1828.mp4?token=CHqcQp2_dHDEZS2XBo8LMYgrD1HrIWwvCxWvYU9KUs9Kugh8Y3ySLoGCQEA-qB_fEoxFb2PpA2O4ZsfuDWuZ2FLaKc0X5KgwsqOgyBYLvNeAQ95UCrkyLdBkXkMKg8y3G-5chxN40YpC6epaXRmXQRbfaCr7z4_3fCq4Z5p6TXsfhZJiKmX8mVDP2c6SYVOo9Jb__q_LX4Qw34Czq_eypTHlSXASJQSXlONnVzc5yX63HV63WvutiwkdFwgGx3R6ctwtVmW6Zkd_OYDpDVKa6NomIbLzr5umFOlgLRslP1vw4Ow-B2CYUjU7n80D4AigchFpIQRnyk2Rwuk6m5YrDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
عادل: اگه تو مرحله حذفی به آمریکا بخوریم میتونیم ببریم؟
پیروز قربانی: خیر!
@AloSport</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128316" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/حملات توپخانه‌ای اسرائیل به ارتفاعات علی‌الطاهر در نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/128315" target="_blank">📅 22:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=bsqkgmS2ql4868xW6Dh-CD2CpGu6Ni_2D32QPeHSqw4_BkkBCoFPsJWq4ltCxVZ5rK7trCssy7a7Jd2-5FkLgnsHdscNERqJAyKoQg3gwO4rWQEKFyp3YBJgw9N_skl-DGPx7bOKM540pXF2JILtpbFdjhg-hFcCrZWw1GkiJG6T_l3akDZzpU0-we7iHj85_GIYGCMvZqS1LuDYwv_sLawuBZSlL_osNGQ4fosRh_IRrpdqkhinqSTOxKXlBkjGVOWKxVc8QNt8_jTku9jsVYPEQgSiz2hqz8ZZJBw0P8_OVTwy1Myv_dnXjUSQj0cTmOVFdUFk1ap3S8UNLC-_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdb7c0670.mp4?token=bsqkgmS2ql4868xW6Dh-CD2CpGu6Ni_2D32QPeHSqw4_BkkBCoFPsJWq4ltCxVZ5rK7trCssy7a7Jd2-5FkLgnsHdscNERqJAyKoQg3gwO4rWQEKFyp3YBJgw9N_skl-DGPx7bOKM540pXF2JILtpbFdjhg-hFcCrZWw1GkiJG6T_l3akDZzpU0-we7iHj85_GIYGCMvZqS1LuDYwv_sLawuBZSlL_osNGQ4fosRh_IRrpdqkhinqSTOxKXlBkjGVOWKxVc8QNt8_jTku9jsVYPEQgSiz2hqz8ZZJBw0P8_OVTwy1Myv_dnXjUSQj0cTmOVFdUFk1ap3S8UNLC-_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده اف/ای-۱۸ هورنت از پایگاه هوایی MCAS میرمار در نزدیکی دریاچه ریمرک، ایالت واشنگتن، در حین تمرینات دیروز سقوط کرد.
🔴
خلبان به‌طور ایمن بیرون پرید و سپس توسط یک معاون شهرستان یاکیما نجات یافت.
🔴
سرویس جنگل‌های ایالات متحده به آتش‌سوزی ناشی از لاشه هواپیما پاسخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/128314" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=e7euEu4Do4Pf8jiqcQ3wM6XfhLQdM89w4PlQBwEx9W5s-LxHuG5wjH_CM_2UAd1FsiOxxON5KD3LA-cSNoDdUJtUnJlr9meTZ7QRow18SvV23pWTPTJ5EK5QruUcbF2JIOHWXYBajWnspXEX8zzJEBr9QDBekV4Y9sG6diqNkFJiBJ5J2cbmosq-8Yz9IxARzhI6vhMjT4HGSZDqsI5mpu5XTqKQQrRRhU2ci5t9PuKcWnblcEs5E8EqIBhzU0t5il8-7qeyte5PBHp8beASg1E5g66mlDOs1gjOCdFoW-NiFrX3jXkbNckZmsioTBeXL5_3DKP9xTVzcy9DO91UOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c4ddc193.mp4?token=e7euEu4Do4Pf8jiqcQ3wM6XfhLQdM89w4PlQBwEx9W5s-LxHuG5wjH_CM_2UAd1FsiOxxON5KD3LA-cSNoDdUJtUnJlr9meTZ7QRow18SvV23pWTPTJ5EK5QruUcbF2JIOHWXYBajWnspXEX8zzJEBr9QDBekV4Y9sG6diqNkFJiBJ5J2cbmosq-8Yz9IxARzhI6vhMjT4HGSZDqsI5mpu5XTqKQQrRRhU2ci5t9PuKcWnblcEs5E8EqIBhzU0t5il8-7qeyte5PBHp8beASg1E5g66mlDOs1gjOCdFoW-NiFrX3jXkbNckZmsioTBeXL5_3DKP9xTVzcy9DO91UOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر صنعت لبنان: درحال پخش شیرینی
🔴
خبرنگار: «مناسبت چیست؟»
🔴
وزیر: «آتش‌بس»
🔴
خبرنگار: «گام‌های بعدی پس از آتش‌بس چیست؟»
🔴
وزیر: «از سفارت ایران بپرسید»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128313" target="_blank">📅 22:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
تسنیم: در صورت جنگ یا ترور در ایران و جبهه مقاومت توافق نهایی انجام نمیشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/128312" target="_blank">📅 22:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری /شبکه ۱۳اسرائیل به نقل از یک منبع: تل‌آویو و واشینگتن بر سر عدم عقب‌نشینی کامل اسرائیل از لبنان به توافق رسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/128311" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نتانیاهو:  توافق با ایران توسط ترامپ انجام شد، این تصمیم او بود و ما منافع خودمان را داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/128310" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نتانیاهو: همانکاری با غزه کردیم با جنوب لبنان نیز خواهیم کرد،همانطور که غزه دیگر تهدید جدی‌ای برای اسرائیل نیست حزب‌الله نیز در آینده نخواهد بود
🔴
ما در منطقه حائل امنیتی در لبنان باقی خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/128309" target="_blank">📅 21:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو:  من در انتخابات شرکت خواهم کرد و قصد دارم در آن پیروز شوم.
🔴
گاهی اوقات بین من و ترامپ اختلاف نظر وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/128308" target="_blank">📅 21:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نتانیاهو: ایران به سمت دستیابی به سلاح هسته ای حرکت می کرد و ما توانستیم برنامه های موشکی و هسته ای آن را نابود کنیم.
🔴
ترامپ رئیس جمهور آمریکاست و من نخست وزیر اسرائیل،من مسئول امنیت کشور خودم هستم.من از منافع اسرائیل نه با غرور و خود‌خواهی بلکه با خرد و عقب دفاع می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/128307" target="_blank">📅 21:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
نتانیاهو:  کسانی هستند که می‌خواهند دستاوردهای ما را کم‌اهمیت جلوه دهند، و ما به دستاوردهای بزرگتری هم دست خواهیم یافت.
🔴
ما استقلال خود را در زمینه تسلیحات تضمین خواهیم کرد و نوآوری‌هایی را توسعه خواهیم داد که به خیال‌پردازی نزدیک‌تر هستند.
🔴
من بر منافع امنیتی‌مان در روابطمان با ترامپ و ایالات متحده تأکید کردم
🔴
وضعیت ما امروز بسیار بهتر از هفتم اکتبر است و ما محور ترور را در هم شکسته‌ایم.
🔴
به وضوح می‌گویم تا خلع سلاح حزب‌الله،اسرائیل از منطقه امنیتی جنوب لبنان خارج نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/128306" target="_blank">📅 21:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نتانیاهو:  ما نصرالله را کشتیم و از حمله به جلیله جلوگیری کردیم
🔴
ما کنترل مناطق کلیدی در لبنان را که حزب‌الله از آنجا اسرائیل را تهدید می‌کرد، به دست گرفته‌ایم
🔴
ما دکترین جنگ را تغییر دادیم و سد ترس را شکستیم؛ ما ابتکار عمل و غافلگیری را در دست می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/128305" target="_blank">📅 21:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نتانیاهو:ما در لبنان خواهیم ماند. کار با ایران ممکن است همچنان تمام نشده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/128304" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو:  ما خطر نابودی اسرائیل و ساکنان آن را دفع کردیم و آن را از ویرانی نجات دادیم. مبارزه ما هنوز تمام نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128303" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو: ما خسارات عظیمی به ایرانی‌ها وارد کردیم و اسرائیل را از خطر نابودی هسته‌ای نجات دادیم.
🔴
اگر ما به سرعت برای حمله به ایران اقدام نمی‌کردیم، این کشور به بمب هسته‌ای دست پیدا می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/128302" target="_blank">📅 21:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دلار 155000شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128301" target="_blank">📅 21:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز گفت که خروج از لبنان بخشی از تفاهم‌نامه نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/128300" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر اقتصاد: مبلغ کالابرگ دهک‌های پایین به‌زودی افزایش می‌یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/128299" target="_blank">📅 21:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اردوغان درمورد اسرائیل و ایران:
از ۲۸ فوریه، کاملاً روشن شده است که چه کسی واقعاً خواهان صلح است و چه کسی ادامه جنگ را ترجیح می‌دهد.
🔴
کسانی که تمام امیدهای خود را به ادامه جنگ در منطقه ما بسته‌اند، بدون شک از تقویت فضای صلح ناراحت خواهند شد. همانطور که بارها پیش از این انجام داده‌اند، همه تلاش خود را برای مانع‌تراشی در این روند به کار خواهند بست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128298" target="_blank">📅 21:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانال ۱۳ به نقل از یک مقام اسرائیلی:
ما از لبنان عقب‌نشینی نخواهیم کرد، اما از این پس هر عملیات نظامی قابل بررسی خواهد بود.
🔴
ما برای دستیابی به توافق بین واشنگتن و تهران قربانی شدیم.
🔴
معاون رئیس جمهور آمریکا از نتانیاهو خواسته است تا حضور اسرائیل در لبنان را کاهش دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/128297" target="_blank">📅 21:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e5df9e7a.mp4?token=tqhSc9VO65jiUdztTe6kV-mF9zxtbKLYr4Od74RAtIWDc8l2zoZ6WZUNA3F7HnMS_W9O-Sd70v9a4HDjqG7uWqRLSfFsEcqfQR3cn3gXCPlek7gUnmqDNotZLL119tJeOtXe-TUkpYs0V-ijOPpNw4Bq3cnHJMGOteOhHuxdOCX2-j34ai39Y2YjWiSWoWDf172r2evxHo8i5fHEmbR9WY83E1rTPb0l1u4f7_jngu-06XGdJBXmKQ8vkz4BZVU9VKFKmzk5tVmz9s250osLDJQgLUE7h1YYTwz50AMjvIzKSdggbiB9W9xZOgHKCLcIp_xsxtH4zVhCzQEXaEXOXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e5df9e7a.mp4?token=tqhSc9VO65jiUdztTe6kV-mF9zxtbKLYr4Od74RAtIWDc8l2zoZ6WZUNA3F7HnMS_W9O-Sd70v9a4HDjqG7uWqRLSfFsEcqfQR3cn3gXCPlek7gUnmqDNotZLL119tJeOtXe-TUkpYs0V-ijOPpNw4Bq3cnHJMGOteOhHuxdOCX2-j34ai39Y2YjWiSWoWDf172r2evxHo8i5fHEmbR9WY83E1rTPb0l1u4f7_jngu-06XGdJBXmKQ8vkz4BZVU9VKFKmzk5tVmz9s250osLDJQgLUE7h1YYTwz50AMjvIzKSdggbiB9W9xZOgHKCLcIp_xsxtH4zVhCzQEXaEXOXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی کامل در جاده منتهی به شهر حداتا در جنوب لبنان در نتیجه حملات اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/128296" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از منابع:
گفتگوی پرتنشی بین نتانیاهو و معاون رئیس جمهور آمریکا در مورد حضور اسرائیل در لبنان صورت گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/128295" target="_blank">📅 20:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک مقام آمریکایی به الحدث گفت:
«به زودی خواهیم فهمید که آیا تفاهمات با ایران می‌تواند به توافقی تبدیل شود که مسیر منطقه را تغییر دهد یا خیر.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/128294" target="_blank">📅 20:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
شبکه سی‌ان‌ان به نقل از مقامات ارشد دولت آمریکا: آماده انجام گام‌هایی برای آغاز کاهش تحریم‌ها علیه ایران هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/128293" target="_blank">📅 20:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به i24NEWS گفت: اگر می‌دانستیم که جنگ از نظر «عادت سیاسی» به این شکل تمام می‌شود، مطمئن نیستیم که ارزشش را داشت که وارد آن شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/128292" target="_blank">📅 20:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IE8bQa9qEpch4_xY3kOv06OW3MQ35oicsbx0zMmxI-159u35xtDy4zqWS1CsViP4YHp0zN29Ips5-7rPiDhQxABuUiUYFOrY4RmGOYW5VNNAPpnZjVnc756HvUf2YVES2shOFD4K1yJSGY2Jr7aZeKV0rcm9jAA0C9aLSuktqJ_5oxM1QQ4ShDRQHh90O6I72tAbBcQBhh9Jj5fgKHJzskKN0-DNvyxjYD6uUsX9SA_kidLVGTyFKXU-Yk8TzDhVD2lh2ZH0SCftw6SRnWg04ZVqSucPrQocCLmFgzIKI_8lDx0nw6ouruze_l-qSWJc6gV8oAzOQu_8O0luTf8XUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس آمریکا در کمتر از ۲۰ دقیقه ۱ تریلیون دلار به ارزش بازار خود اضافه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/128291" target="_blank">📅 20:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128288">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiC24YW3YTUqSE-6y-bOLXmoAru_SUO8j7Q4bN9Djeb1obye60-zz16CnI3I7TncobvN9OG301kB1aE4wNkCKSNUbamc1GZi3NXbyBTIB4tqGWiEwC9iaQYRdHnC90RyzEqAXyMlVDwDkCoSpYKtqdUDzfzsaEZET1LY8MKKH3pSRcvy1GEOUppjlrBvLzWepXZezKz6XWlHIKa0Y1JSp3pNX9xXWCrF35ov3a8SCXgMZVbXOYQ7Z9SzM2vtEHnjbpiHJW8Wpb_A65E-x3Gl8spsXGG8OiF5rIWk_CrhJBDJ-TCHSW_2VCAAjBGE6n3lQFXV3LI9QwBmhIJ9zcr3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpkqXwWW5vq2d_CJDMtvQgTtfXz-1jVc-zDVv58TA0VYy-A0DWXAeWTFlNe_0TuS9tHXfknwbDFpT29HCkwim58F5fKz-h7MyIAC2o1tVb2GKkilK66ksgyvrsrk1aMLX972NrKQ3PDB73QEuRJO3nVFu8XCQO-ril8H9yT7ITd5bJU5hWx7wjae-8piYTRYJkOlVzYYqNJNiYeWOnU6oHXNFHcZPiIXgpXQ2XELbysLIVpGC0b6TzHnECAkgUAs19LA5XvZjg3ObxTJaVPRVH3AuM2FeecOED6Gi02skjvDJ9GhGzWVOouexNrNSOm7pGp54xWJd-rtzr-di7xsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTCxcnQ0VQeRiv3APp35nbJhlukPWsmOhDwbH_eveKTdgS8ulWN7btms0e6mpMlMxO4BT3YTGqOeImufHfGNtkX_9cpUiZli0m9RHx0scOAXhsWXHiitNs9gEWPcT4LFD_XC1S6OQ8ihRQLz7u4i_jKwxuZd5rQOV_Q_o5dMgOhOq4cYxdrfXdRSlYUBvij5kEAE1I9a6maSrMbHsT4fPe87z8LbzUmfh0mepKBBhsmyUvJY_BtifhfvPRs-gqfQDUsBKkjnh8yp2Mjc_hTOPRssX1FjsNUhGSrJFBCKifHGj3imhkyDLHHw6UGoLlBfptXeNmA2o0hxkAZR1-duZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از سرجنگی عمل نکرده موشک کروز BGM-109 تاماهاوک در نزدیکی ورامین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/128288" target="_blank">📅 20:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128287">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
مکرون: ما از ایالات متحده، ایران و عمان در بازگشایی تنگه هرمز حمایت خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/128287" target="_blank">📅 20:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128286">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: نتانیاهو هم با توافق موافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/128286" target="_blank">📅 20:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45b122799.mp4?token=Mx_nlKYC7u_7wqDde9FnRJ2T8RXEcupZtfN-OVjMiXl9hpcp9NLazEjq1FqvL3JXnkXkiVsp5aoINcQJ3hxGBshkbuCFo0vuJVcNcKljbhl98y6Lz4FJV4RnEVhJoJ2KB3-3lPY5HiyjS7y0d7INz7snSSlTXWV3y0aJLoTMwbTywt_3L1sRbSz0KiFBucR02_CnMI3gFwAYteLptjXNN65WBKxUEuLdvOJRIBEUUjai0wSb6KKKlbD56QT2FjJubpr5gu3bIFLuYOgI1IuyPUMDPj08Bqv0TfnGmCOR-j7igwy648OuKZqxRtSM1OI7p3CwxRCDD5POh4Ny5nrbGy4pPI_jVjSkL_ulxaOftphG1wXs8QSYTdDUlOFmu4wIwAslm2QePz1N77OgXWYiEruE7mj4RrBJuViq17YVJ3GvwrZeDF2UvT6TC0MWi9BElNUv0xWHU2Zf2MDcfqRufwoQtgNZ6oGknn1DiO4WXlL6S1iXb5yBPiLjkinLkRZ1XnyynWyqSoq3UF_p6NG-Or2cAk7AsKzcrFzSWd0sPve4nMnDfLbwzsG1IuWkW3HTUrwwGzBcudZOXPhKrVb_OOb9wbAGOVm5geBy6ARDYJeDoV8JF3WkT90peFSty4_F6d1h1hE_90qojVUp7S4OYapY18z61i74UqtFQk58fMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45b122799.mp4?token=Mx_nlKYC7u_7wqDde9FnRJ2T8RXEcupZtfN-OVjMiXl9hpcp9NLazEjq1FqvL3JXnkXkiVsp5aoINcQJ3hxGBshkbuCFo0vuJVcNcKljbhl98y6Lz4FJV4RnEVhJoJ2KB3-3lPY5HiyjS7y0d7INz7snSSlTXWV3y0aJLoTMwbTywt_3L1sRbSz0KiFBucR02_CnMI3gFwAYteLptjXNN65WBKxUEuLdvOJRIBEUUjai0wSb6KKKlbD56QT2FjJubpr5gu3bIFLuYOgI1IuyPUMDPj08Bqv0TfnGmCOR-j7igwy648OuKZqxRtSM1OI7p3CwxRCDD5POh4Ny5nrbGy4pPI_jVjSkL_ulxaOftphG1wXs8QSYTdDUlOFmu4wIwAslm2QePz1N77OgXWYiEruE7mj4RrBJuViq17YVJ3GvwrZeDF2UvT6TC0MWi9BElNUv0xWHU2Zf2MDcfqRufwoQtgNZ6oGknn1DiO4WXlL6S1iXb5yBPiLjkinLkRZ1XnyynWyqSoq3UF_p6NG-Or2cAk7AsKzcrFzSWd0sPve4nMnDfLbwzsG1IuWkW3HTUrwwGzBcudZOXPhKrVb_OOb9wbAGOVm5geBy6ARDYJeDoV8JF3WkT90peFSty4_F6d1h1hE_90qojVUp7S4OYapY18z61i74UqtFQk58fMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به مکرون: شب گذشته بسیار دیر با شما تماس گرفتم تا تبریک بگویم. در دسته‌بندی سنگین‌وزن، یک بوکسور فرانسوی پیروز شد.
🔴
نمی‌دانم — شاید این حتی مهم‌تر از جام جهانی باشد. برای برخی افراد ممکن است این‌طور باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/128285" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8oxGAa5RZDVsYsr9Tgln-ITDOF5BKoxGwlKzzOGZuEohtXtvGmj-CgQTFTTplSq7mlAzrb3fYdtDI4b61YRjV5DmWL7FHBkEAuIZQlEVcEpt-cM7kC0NtTqR4X-5jWHsgRgHWNWle5siTkxXql0mM1jSj6p1Ra7mUL0zHF96y2gH7ETZH0jWApdNN8VwyEH-wfv5CJJj5vrZImIJgXEUFFhspe8KTMd_76ItLY-ruJDOq71WQpoiT7qjmsQEtEetL39idrDuO97ggEBoz8-QzZUuBXQWmsDBZpykvPkgiBdSMwiruEqMHB6uhUKtIrtU1qVhUG2alWjMnLpcZX_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پارلمان مجارستان اصلاحیه‌ای را تصویب کرده است که محدودیت هشت ساله برای دوره ریاست جمهوری نخست‌وزیران اعمال می‌کند و عملاً بازگشت ویکتور اوربان، نخست‌وزیر سابق، به این سمت را غیرممکن می‌سازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/128284" target="_blank">📅 20:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01951dffa5.mp4?token=sKuJsSgwEPc8vmwsU7qPTsrlAsbCMv_7_8-OKrmgXkVw0MV815nvfOu3AtW80FkFihXnFBBFNMGJrkkp4YrONLnL2izeuKLZoHEyE_CEm0vvoiqvSWwNZ1Sd9lgSV13C0kaWufMNlxqe9LqgYrjOEwfsyUOxyEZBl7X0u5iMNMJzfP5AKyd42KL1BeRNYsSBK6SiWsAz1IHWgPV1k26DHiLVWuEdAYpDE6TEmC4FPjTurzHp4kPeZzddY_O2A_y6J_aPPHHSbFp8b22bWm1_JUeYCxYcBT_4WcNWMb9NtPJOEX--cjWqzZ7b1H-F2l7Bdyasx7G1lFiJFxPKf_Du_quuooDV_1UlJJxj9mX7m7DQ_dH57un9j-GxqxRtTKRs_WLO8f40IDGZbjUc34YxMZPa-QifA4ozSL05vH-m3u-7DBru6HO0oF3KGos-VLUrQynQcYHmlbEkFkWaHwESLw85AY8EtJ_KAIhiY2JwkBMgvQ6JArnYF_dHjmgvT5e-3dXmm08XQiUCSi6n3KBmrT-EPjV_ZrnY58sAyC-TVwXiWwwiVtW6MEFLYZhBksVSCcru4EBn-bDpLINR5yrKG1f6ecTrainthR3Exf_Xq863c1Z02JYJRPuMuWckktKArif2_8j_ClZFLCODVRXBF6MatEPuefjJhmX43s39ylE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01951dffa5.mp4?token=sKuJsSgwEPc8vmwsU7qPTsrlAsbCMv_7_8-OKrmgXkVw0MV815nvfOu3AtW80FkFihXnFBBFNMGJrkkp4YrONLnL2izeuKLZoHEyE_CEm0vvoiqvSWwNZ1Sd9lgSV13C0kaWufMNlxqe9LqgYrjOEwfsyUOxyEZBl7X0u5iMNMJzfP5AKyd42KL1BeRNYsSBK6SiWsAz1IHWgPV1k26DHiLVWuEdAYpDE6TEmC4FPjTurzHp4kPeZzddY_O2A_y6J_aPPHHSbFp8b22bWm1_JUeYCxYcBT_4WcNWMb9NtPJOEX--cjWqzZ7b1H-F2l7Bdyasx7G1lFiJFxPKf_Du_quuooDV_1UlJJxj9mX7m7DQ_dH57un9j-GxqxRtTKRs_WLO8f40IDGZbjUc34YxMZPa-QifA4ozSL05vH-m3u-7DBru6HO0oF3KGos-VLUrQynQcYHmlbEkFkWaHwESLw85AY8EtJ_KAIhiY2JwkBMgvQ6JArnYF_dHjmgvT5e-3dXmm08XQiUCSi6n3KBmrT-EPjV_ZrnY58sAyC-TVwXiWwwiVtW6MEFLYZhBksVSCcru4EBn-bDpLINR5yrKG1f6ecTrainthR3Exf_Xq863c1Z02JYJRPuMuWckktKArif2_8j_ClZFLCODVRXBF6MatEPuefjJhmX43s39ylE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لبنان
:
ما می‌خواهیم ببینیم آیا می‌توانیم مسئله لبنان را مرتب کنیم، زیرا به نظر می‌رسد هرگز به پایان نمی‌رسد.
🔴
و این نسخه کوچکی از کاری بود که انجام می‌دادیم. اما نباید سخت باشد.
🔴
حزب‌الله. ما باید کمی با آن‌ها صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128283" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خبرنگار
:
آیا قصد دارید در مراسم امضای روز جمعه شرکت کنید؟
🔴
ترامپ:
خب، بستگی دارد. جی‌دی برای آن می‌آید — در اصل قرار بود او این کار را انجام دهد. احتمالاً تا آن زمان من رفته‌ام.
🔴
ما تا دیر وقت می‌مانیم، بنابراین ممکن است درگیر شوم و ممکن است نشوم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/128282" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: احتمال دارد جمعه حضور داشته باشم و با ایرانی ها دیدار کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/128281" target="_blank">📅 19:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ در ادامه: از اینکه مجبور شدیم دو شب دیگر به حمله ادامه دهیم، احساس بدی داشتم. و فکر می‌کردم برای بار سوم هم همینطور، اما ما قبل از آن توافق را انجام دادیم.
🔴
فکر می‌کنم اتفاقات خیلی خوبی قرار است در خاورمیانه رخ دهد.
🔴
قیمت نفت در حال سقوط است و بازار سهام مثل موشک در حال افزایش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/128280" target="_blank">📅 19:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ما می‌خواهیم ببینیم چگونه می‌توانیم مناقشه در لبنان را حل کنیم و باید در این مورد با اسرائیل صحبت کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/128279" target="_blank">📅 19:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بدون عوارض بازگشایی می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/128278" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: کاهش تحریم‌های ایران به رفتار این کشور بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/128277" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: می‌خواهم یادداشت تفاهم با ایران را منتشر کنم زیرا سندی مهم و قدرتمند است و ما به زودی آن را منتشر خواهیم کرد
🔴
تنگه هرمز پس از جمع‌آوری مین‌ها به‌طور کامل باز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/128276" target="_blank">📅 19:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: جی دی ونس در مراسم امضای تفاهم‌نامه با ایران شرکت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128275" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: ما خواهان روابط خوب با ایران هستیم و اگر این اتفاق نیفتد، به جنگ باز خواهیم گشت. امیدوارم این اتفاق نیفتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/128274" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: ما خواهان روابط خوب با ایران هستیم و اگر این امر محقق نشود، به جنگ باز خواهیم گشت و امیدوارم این اتفاق نیفتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/128273" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: توافقی که اوباما با ایران انجام داد، این کشور را قادر به ساخت سلاح هسته‌ای می‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/128272" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: ایران سلاح هسته‌ای نخواهد داشت و من با این موضوع موافقت کردم. این اصل موضوع مناقشه بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/128271" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ: توافق با ایران به نفع منطقه خاورمیانه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/128270" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ: ما با ایران تفاهم‌نامه‌ای امضا کردیم و تنگه هرمز تا حدی بازگشایی شده است
🔴
تنگه هرمز روز جمعه به طور کامل باز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/128269" target="_blank">📅 19:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
معاریو: اسرائیل از توافق میان آمریکا و ایران شوکه شده است و به‌تدریج در حال از دست دادن اعتماد خود به ترامپ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/128268" target="_blank">📅 19:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی: جزئیات توافق با ایران ظرف یک یا دو روز منتشر خواهد شد و مذاکرات پیش رو بسیار مهم خواهد بود.
🔴
مذاکرات فنی اواخر این هفته آغاز خواهد شد.
🔴
ما نمی‌توانیم به ایران اجازه دسترسی به دارایی‌هایش را بدهیم یا اگر از آنها برای حمایت از تروریسم…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/128267" target="_blank">📅 19:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9573421eb8.mp4?token=XuTtZs1CtDgK-DhtGpK6vlYuiQhm1M1WhuAiergMFro4YSbiaUFGaIowdrV4zJoLWbhzOV_JdYa_XCSjfLRyztc0SYL7hPxPLE1yF3pPq4BuOMMf5a6BEFDhb3C--ml7e2BuW-kMDEm9n5OfIhunAjcxG8YJx9Hivy0cg9jsx7USWSBxEzuO6dR3opQR8I6bV2GoGcRomgPYT2tWbzPK5kqFUZvzxIGOx1-V7ymZOXGbkxpu6z1vbMaGUmTmmPimJHyTzZeurM7PQY8qjbhzGmL9vBaZ0V7-pG6ez21eigrvJLV7RgCFqF9cBNuEojl3RRl8l8SLSlZmUAYjTCHbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9573421eb8.mp4?token=XuTtZs1CtDgK-DhtGpK6vlYuiQhm1M1WhuAiergMFro4YSbiaUFGaIowdrV4zJoLWbhzOV_JdYa_XCSjfLRyztc0SYL7hPxPLE1yF3pPq4BuOMMf5a6BEFDhb3C--ml7e2BuW-kMDEm9n5OfIhunAjcxG8YJx9Hivy0cg9jsx7USWSBxEzuO6dR3opQR8I6bV2GoGcRomgPYT2tWbzPK5kqFUZvzxIGOx1-V7ymZOXGbkxpu6z1vbMaGUmTmmPimJHyTzZeurM7PQY8qjbhzGmL9vBaZ0V7-pG6ez21eigrvJLV7RgCFqF9cBNuEojl3RRl8l8SLSlZmUAYjTCHbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فکر می‌کنید تفاهم‌نامه ایران و آمریکا طولانی‌مدت و دائمی شود؟
🔴
وزیرخارجه لهستان: ان‌شاءالله!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/128266" target="_blank">📅 19:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی: جزئیات توافق با ایران ظرف یک یا دو روز منتشر خواهد شد و مذاکرات پیش رو بسیار مهم خواهد بود.
🔴
مذاکرات فنی اواخر این هفته آغاز خواهد شد.
🔴
ما نمی‌توانیم به ایران اجازه دسترسی به دارایی‌هایش را بدهیم یا اگر از آنها برای حمایت از تروریسم استفاده کند، آنها را آزاد کنیم
🔴
نیروهای ما استقرار فعلی خود در خاورمیانه را حفظ خواهند کرد و هرگونه کاهش نیرو پس از امضای توافق نهایی انجام خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128265" target="_blank">📅 19:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام ارشد آمریکایی:
ترامپ و ونس از طرف امریکا و همچنین قالیباف از طرف ایران این یادداشت تفاهم را امضا کردند.
🔴
این توافق، بازگشایی فوری تنگه هرمز و لغو تحریم‌های آمریکا علیه ایران را تصریح می‌کند.
🔴
ترافیک در تنگه هرمز از همین حالا شاهد افزایش قابل توجهی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/128264" target="_blank">📅 19:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH8HEy_CFwcw32VJLKpk_E16MQ6kh9xbFCdohfRrA0ZZA89_MHv_UfDRDtfjCP9qCf3urXrJAiR3LvmCEOYsly6tyvL8LzgqYJKDuo26W5fNAIXCQJT6i8qTXYS05wPuRbGyjJ9AKY6zG0AAPeONSBsiYQMUtjJQpX4wY88d5etYKg2FhV6emGP3Z3YbxsMJF0bOpZ8PWfKI8qhd4HAPjyjFhmLyOsXZtYMXI41WAUqGf6wUngC5ZWHQnZe7gP8jsSqaBb4VfaiQVSsJ7uWcOZ0bLZ-t1uEDvaCQJtvLJiuNYvbt5-RzzCD4J_-gyy7NvJ0A7fQ7tvwt2SC27Gq7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف : ایران گامی بلند به سوی پیروزی نهایی برداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/128263" target="_blank">📅 19:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت آحارونوت:
اهدافی که بنیامین نتانیاهو برای توافق با ایران تعیین کرده بود، در یادداشت تفاهم میان آمریکا و ایران جایی ندارند و به نظر می‌رسد در توافق نهایی نیز محقق نخواهند شد.
🔴
این اهداف شامل خروج مواد غنی‌شده از ایران، برچیدن زیرساخت‌های غنی‌سازی، محدودسازی برنامه موشکی و پایان دادن به حمایت ایران از متحدانش در خاورمیانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/128262" target="_blank">📅 19:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عراقچی: روز جمعه احتمالاً در کشور سوئیس دیداری بین روسای هیئت‌های دو طرف انجام و تفاهمنامه بین ایران و امریکا امضا شود، سپس اولین دور مذاکرات بعدی برگزار شو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/128261" target="_blank">📅 19:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb39df108.mp4?token=MZYfvLaSKiokbLj88yodi52E86gAFMbWDeg8Dfh88KqLcIZnBtHlQzfilgzNaavduxDFsQ3-JFy5pJkfxlwWMjHyQ4JkDN2ru4CWpghQEMdNL3sSikizhEEiSNHn0fdtKr_VKxgA3nWBN5BlNyljjJrLL5LGWLwFIcPoqpTgQj5dDut4LbZh7t-EHqLH79HVMSvjRi8v7Ta4EVtgmf5kWaZljgUJWTHZJ_iNwd4DukhR-sHbQTiko5sm5KqDlUpu-uTIB_yZCDRw7gTiyHCqQpOPrPLuoFfQd912O6hZWYWOqzPjuSQzO1y0m7Rrvipn2EzVhHRHRBjbQeJArPsa_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb39df108.mp4?token=MZYfvLaSKiokbLj88yodi52E86gAFMbWDeg8Dfh88KqLcIZnBtHlQzfilgzNaavduxDFsQ3-JFy5pJkfxlwWMjHyQ4JkDN2ru4CWpghQEMdNL3sSikizhEEiSNHn0fdtKr_VKxgA3nWBN5BlNyljjJrLL5LGWLwFIcPoqpTgQj5dDut4LbZh7t-EHqLH79HVMSvjRi8v7Ta4EVtgmf5kWaZljgUJWTHZJ_iNwd4DukhR-sHbQTiko5sm5KqDlUpu-uTIB_yZCDRw7gTiyHCqQpOPrPLuoFfQd912O6hZWYWOqzPjuSQzO1y0m7Rrvipn2EzVhHRHRBjbQeJArPsa_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌ پلیس راهور :  صدور گواهینامه موتورسیکلت برای بانوان داره اجرایی میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128260" target="_blank">📅 19:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
شرکت مخابرات سوریه به سانا اعلام کرد که یک کابل زیردریایی بین‌المللی که طرطوس را به اسکندریه مصر متصل می‌کند، در نزدیکی ساحل طرطوس خرابکاری شده است.
🔴
این آسیب باعث اختلال در بخش قابل توجهی از ظرفیت اینترنت بین‌المللی سوریه شده و خدمات اینترنتی ضعیف‌تری را در چندین استان به دنبال داشته است.
🔴
شرکت اعلام کرد که تیم‌های تخصصی برای تعمیر کابل اعزام شده‌اند و هشدار داد که بازسازی کامل خدمات ممکن است به دلیل پیچیدگی فنی تعمیرات کابل زیر دریا زمان‌بر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/128259" target="_blank">📅 18:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3f87619.mp4?token=fSlz-zgi4HIkivqwIW3eUb4l7hwK_xtw2CikBl9ltVOmFzzTtmuV5LMNkXu9IBlPPGt-yMCbho_1UjSbgP6Yy14ZKItkpNlzi4kHngx3C_HiQQnb0UKAKhXqPSob_nj7f2wSYQZows77iXMWkwqoGAfb-uCTF2_NI6V4Asdx9IgdyerL1OCNmi3IpLaOabx2xbv0o8bBa8-vckip6HSGMy91uJvqD4AGIZH4nwYqIThJVh6Yvu0wSXGWGE7tWeiG-dhe72r_Shom_qkvPDjUfWGesv2PkmK1PE8BxSJXFwmUGWk9UxzA6thJF8DRkC1G6U_xiBRo6reYiRYYaGgOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3f87619.mp4?token=fSlz-zgi4HIkivqwIW3eUb4l7hwK_xtw2CikBl9ltVOmFzzTtmuV5LMNkXu9IBlPPGt-yMCbho_1UjSbgP6Yy14ZKItkpNlzi4kHngx3C_HiQQnb0UKAKhXqPSob_nj7f2wSYQZows77iXMWkwqoGAfb-uCTF2_NI6V4Asdx9IgdyerL1OCNmi3IpLaOabx2xbv0o8bBa8-vckip6HSGMy91uJvqD4AGIZH4nwYqIThJVh6Yvu0wSXGWGE7tWeiG-dhe72r_Shom_qkvPDjUfWGesv2PkmK1PE8BxSJXFwmUGWk9UxzA6thJF8DRkC1G6U_xiBRo6reYiRYYaGgOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، برای شرکت در نشست سران گروه هفت (G7) وارد شهر اویان-له‌بن در فرانسه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128258" target="_blank">📅 18:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نتانیاهو تا چند ساعت دیگر سخنرانی خواهد کرد و این اولین واکنش رسمی او به اعلام توافق پس از ساعت‌ها سکوت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/128257" target="_blank">📅 18:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128254">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwZtUhrhBDBBAVqvuUHO7yCv1idU0x2s0FxiOyRTVFP0hMl74HRQUCFXcp1QXk-qDLmeseZpjMx2tSVqeRfdrxpCprK6ltsE-fOVydZPwKMVnVSXwdYG92daflAvuPQOlRJSM0Uky-3-21bEDMkvB-h7Gntgw42eG2StCbzk4rZ7Gwq4_KPALefCtrVGrePX0cDfYCeU-LYS1x6iL3C4oJeg4FWHDmI9_pWpSDnnXQkpP3hCd94X0LPonatRD55l5s3h4e12hPnDxDPSyVw70TuN3JPNHlCBBt0vhSqaDnhOlDSo69o6FSfCKoFvH5idcVzqDXQMsUQ7BED2jzdwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5_92I2Zj1SLeqrTqeMTEhthoUtK6HZbEZI9eDavEkku29SWR5Hdvuoc9WoFeVIskjcjMZLMMkpRIjWrOlesi7yfdIOIdPDOHLaCCDDKoUj2CLMX19EFnkb_9wlSaXQXwWPAlAN1mYn_XshTiIycHd0cM9FlCltpYzAyDcaAVGR2_RC0S6GCVnplHyoUPAMbDqsn_cWuLDGa6KyGV7LfsN8z5y8XMyMYD__R3-uwbUFPjEOqwo8d7Qf3_QUh2lDPwzQW7CtIc1PkdhjVeixXmw1Iodz-1Ib5QAJO7TA0Mj1_6GI3q6taHoT_wLXjR5kbJuYsmNxfF7iWtWumMUW2bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7b34be62.mp4?token=aYlZFiFTfoMSShQtD1mQsuBqNLOrICjk_e6feM2PVW1G88ZxURTL5YYZxGyNLej2Q8Ph_JAZNBlWf7prjxED7SCXbT_Jk5Ddlstdd5Wwr8ShqM1AejdmN2oV9b22My0HgHF6ZM9aZwnUP2fOyIrqdiE_nWfDSZdDXViyAi4AmC1bSOaMp0omhPcZOYGyAXYremuEx7vm6jprzVU-uKLmeg1oNtx6yJCFilaL2bDu8Me2LMiST2gQUEcwvLzDuGDyPXHHTrdp4AOz4tzcYCFYy8VRswFOvJyypev4nSdmt7P5TnlTVeX5McKhFGvAehTjxCmu0_2GgCB9wS3gA967og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7b34be62.mp4?token=aYlZFiFTfoMSShQtD1mQsuBqNLOrICjk_e6feM2PVW1G88ZxURTL5YYZxGyNLej2Q8Ph_JAZNBlWf7prjxED7SCXbT_Jk5Ddlstdd5Wwr8ShqM1AejdmN2oV9b22My0HgHF6ZM9aZwnUP2fOyIrqdiE_nWfDSZdDXViyAi4AmC1bSOaMp0omhPcZOYGyAXYremuEx7vm6jprzVU-uKLmeg1oNtx6yJCFilaL2bDu8Me2LMiST2gQUEcwvLzDuGDyPXHHTrdp4AOz4tzcYCFYy8VRswFOvJyypev4nSdmt7P5TnlTVeX5McKhFGvAehTjxCmu0_2GgCB9wS3gA967og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آتیش سوزی آتش‌سوزی تو میدون تجریش، تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/128254" target="_blank">📅 18:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
براساس گزارش‌های اولیه، یک نفتکش در آب‌های ساحلی یمن هدف قرار گرفته اما تاکنون جزئیات بیشتری منتشر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128253" target="_blank">📅 18:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128252">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: نگرانی و عصبانیت اسرائیل از توافق،  نشانه‌ای روشن از موفقیت و پیروزی ملت ایران است و به فضل الهی این مسیر با اقتدار ادامه خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128252" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128251">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی مجلس با اشاره به اجرای آزمایشی انتقال سهمیه کارت سوخت به کارت بانکی از تیرماه، گفت:با اجرای این مصوبه، هیچ تغییری درمیزان سهمیه و قیمت سوخت ایجاد نخواهد شد و مردم از این بابت نگرانی نداشته باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/128251" target="_blank">📅 18:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128250">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان: تیم مذاکره‌کننده‌ای که برای امضای توافق اعزام خواهد شد، به هیچ عنوان از چارچوب‌ها و سیاست‌های تعیین‌شده از سوی رهبری عالیقدر عدول نخواهد کرد و تمامی اقدامات در چارچوب منافع ملی و خطوط ترسیم‌شده نظام انجام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/128250" target="_blank">📅 18:39 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
