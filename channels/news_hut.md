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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 207K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=WQFf7RYG1UZEj-LlfxKA7qahWXULju7ed34A4pF8Nh7Bzj7ouOdtLS0BpfK7bQJ7t5w_Q38YDPzy6UFKaGbuR--peyE-BNvMLVRm-FUH64byqox-8ZM3M1Mb8A3xz9VWaNozJNdwE7C-KOUgefYHK6zpw0oBNSXNEkoPMJbulIBAaOtre_uejOAwNjkPM-_eseRh4UchJQxc79cieFAjV8d57w_lcQ29NJsGnD66m9uB-spumn3a8-iY1DRJ-9IY023SGczR2q9ytFym7umobl-ACrcaGlM6uMd613Qm1IK5ZrsHtQ3XWTt3Gfa2pQezJtzRtqvU9QAa7UCFiKz1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDWy4pzi4Ip5XV7vgElrgnwJbFAvfcRovbKXFsMQfktjsbJuyxWNIM0YGwif7vrTGD8XeZ0Lgs1XNBVnzhWoPCqYNe4bhEkCMaSXBCG2egIIuV9Qdu-zzyQtI34Dj0uB7ysJNMUh2WG9F3GqGuKBpUeN4zkhnzeEah0001WFsCCEmhzRB3o4Bl2f4IJP53cIUfdbDWplPPLBh7lFI5Hx78kG_ZmL74E4sYJLgdPkNUlSdj9b9ipL6bP-tqdxQsXmFkIbNThqJMk9qX0B1u0y6OQ6_E7vjFvPgp4ZgeaL5xCinMANTVihO4gWYID1uGY40Pvox5mpHlKyaeHiWZa2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm6tcfojvOdGL_83bYjDUh7y0BWt3V52alrsqGSuAkPjNP9PRg55kdIqlJerYybGLl5NlTwljMKzF4EOQqdVPImA_MkBeLJf_XuegOHnA_VUrfn5wHFCqkGpv9_RwY7QflTfGJNQemMhqwMVdcFcilBOfa_m-P3fQ2pQtD9ipD-YU0y5UHpjthTMXGjPNRel19UHSU10RLHiJC9hAXAy1azkF4j3Lp5dUFsi8t46n9iSzKcpqrUQBAI5ctWP1JZTxipjpLKyIn1qdR2e4Lwf4dAD_bDfZHoHdoUwZJ7rg5FZ3FfVdxlSzjUbiC9KKHhneqdI-1eCR0YiHlwKLDsAkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-x9-aOaeoV_adeiI6vJbRO5RJJ23JGEbe2axdaJK8uqYooCOtcZfu_YI3nTjT_HCpf8cOn7xYGzfZjLrAiERUYERtJZnhFZgabzbnZm0NWPtIfFiqI9BAWmOaonuOfrc4_p6IpnCrEEGsnlQ2oetS7oRLdEFOPWOltgIlLS8y5u8ZmfTUtqaPo4O5hOZlpf43VeqspUjE8OwLIoUDlM5qy50px87s86x5Gdpbj161rxrXKk-Re0Q76Mq7OMu1h2xno3M4QWo7p-3EQKQhvz_YVC70MlI14_8fI5Jb9-_Iz6Vnr0-b7VvBcZtaBvrx-b7yz5zcgH5oZvO2e3j1B-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=GxHoaPVxkwVCFTpbW6WbZY_jyyEebY4SZX7F4ea_CjjFKuk0FRy0Of6noOy8ms9w0KTXOSzzHFV4k9vzcY5I1AFrD3nF_A5mQN9Brnxna5665Tt3ZX4AYuo-b5unTBxyeCLNvFiduFgGSVYDMkM9z5ahwF3s5KEa0AXQa3fzQeZ8p3w9Mx81ikerernX4BS83i4RsEtKyj4TPEcuyTgo12AOIa05uwhrb2nDblebB-ucFTW9-trUhyUhpEMwmGwDfDCsZA5NiHQl1fQh5jLr-cwCJQKHEHxHTY9B3JAhlWoR_wQ_dGXHv9Fu7kzTtG3qwoOKj100Df1PXhmkO50CiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=vBNJseh73LA_AoupbqKPBCW44o65Xge_mxcIuLOH_ZtWpnsx3zE7MusDdNnKmAISHRyqtYeKgeaWnuvy5DbFaBTw0KSd1tanYZihjlK-DfkT0TfMaLdYKBR411fzV0Qlf7KKM5yNi8Frf-GeeC_p2LNYBFl7vEsLojQcDaZNO7lCn5NGLb6SbEhJBK2bsZLEH6CEn-gROCOyTUEwKJhQycp3jVrPoR0PsjLTFuqXDzAEpoD1txA8HTWHbcOnG_z08r90gVVxW-GLB1RTr-PRxbutaa1Mg2tiJMHPIXIjt_nRzR5GoMxd1TJb6VfGUm89Mda_US8dJHt70rUNUxmgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGyidfyl8IRbkqaAq1M9__Vaze3zlalljbwjKSwbppvPFGqddS6JjaZ1TY_wT7PNKBgb-Q4e7w2K66b1oXFfSLgQbrr6QfS43jg2zI4VQ9HCAxg8DgfHJF2o_Up9o145RpH1ma2lTF1OJs4GvBz7X_yLQf6PgoCiAHk1LEoHeK6zKfyJf67VLRZqDsYgWECdydR24lV3LZP2gUpU7ICU5h0fdl4xxGNUKAcZHLfSsxVdMRG5PILfWKDS0lSINB1sJp5mxiR8LuCClVDpp2IyEHwv15ssQO5srQ9BPvUPfloUicDo5_jWQDd6h2xmJVts5HMw1JbAaiCcUb7gE4GKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBe-n5-XJ7eEpm0cKUvwMvRDINe0BD0DiaVO7qXAVtU5JQPnjMF55kSoTeCVG9B40ZK4LngQK48YBQWpnLEsAUKkGYuyHye48OSgGANvIw9lgpROv11qeyhRGsPgTJLyOxcHl2sTkiPvFYEN3-cUoOrnoCq5TGnirMcRL5R0Aj-gy_w6HZpP3YHQGCJrNduyUIJja5tERIkAQMOZEXEm19z92boLeb01KtYkkMn7FU9lwfLD0vylaWHc0Ej6Y9OvQk9d8-4XXlu5rSZd2VYiMzPcdau-3CkPRVpNSz3rKESct80om2jiL3JoHznzBH6CXrRlkynmMyHkL5rFGoCUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtatJ_urYgV3jA8hrmHntL4B3BGxS4j3kxrrRZP2pcikItiOkE7JHvsLJUhoSq7miSz7FB-_4lmxJPz7GwTajk8sICAm0LX8NW0yqXD2vN0H0O22LwHolNw8xT8wb8lDyw1DVOmhgp5cXD-mTXYWGKC1F5gmDR9y7AQAK6KoUv_LV8sy5-2YJmvXlpouQJmWQXV9xxhIpFpVutdSo9C8W7hJ6ZBJtQ35lcp6tHDwttMqsPo6IN8F9MjeeXBumo6JEopmStVMPHGZmhXeKqyl7YSr57x7w-oeEPIEJ2AKKbVpfREM7LH17c38A0KtBu0JE8_NTGqWPHe9CRMJXU8iAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4uks0s2zIVQQxXW699xzRqEv254JCxDX8v1oXz6EeHET-fdEUTVkQEF9MDnvBZVIZ2S5FkSv54CSz5wSXel_7u8X2FA3JAIasdfUfWUKXCiRqL5l1f5ZIVYklj1zmAz5PSgYNIN5O46175NnQOKZ_XchNnG5fZEuxD6ximpI3N6Qlm0fzuM_buZqSqwU82LPgPZtc0Zwur3T2OpuYpbqrTTDd9AMe5qBXsMLyGfw2b8LQBgwZuIoKAJvdIUZ5EhVfz860B5BMqbHrAmyCgrhmCxtnbbQtwcmRodEIv-8Wa8G91kDV29lvXTh-vHw7fKqIRlCbpDrcAagCUX9autA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijsVamUHk69bunzsYH-hW1qjzn9CcMOfsSr4om_uE4oSvQKw2tYkn8xoIWJtnDc52JF1SqxqGU-EGsMoxWLSjis35e8HRonaw_HbLV-YPK-EeinlpQPOb6KD8qR4cJ011aMyfKQhaClnwBmmwJHQ80cK4N_0Kxgqkecnh_3b_-KJB6ZyZJ8_tWoRoOIgLI_hOo7MpjxiyKoqEaN35hbPoiZdAxZxwSxvI1CED2BnLwUA03GCZXEVpU2V6WJrwrI_IYrUUAiga0LR8QvhLNTANalFNZCF3gPCwZcWKTkgtqOS5QLIMx90vfcjUzd0Sa-_BFYmOtg_zlOqiH_if4Mq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWoXKWQhzENQ4p-r-wdSmEmLmswM7576CoSxiQlgxosMR4clIWyGmPPIe3dUoEbhAqjVwiIkDfLmG-YzlZrf1YbwuKK5oBhkJq6WfWuRGic3-RNp5ElnVzCWJMvMWwTR_wHx8ws9aUtIIBaQuHwrxneT_FPMsUdDl_AvXc13a-TH3rzY3aeKnSirX2yFLGeBR57KTq7BDnVBOFMCo02-Ys0g5ETq6DJFuM53wpNWF5bekeg6pQESESMJVJ0v4meEjdu0-Ymdpc8KIJN0kMlusS0-dNi_saBZA7iqFM2yb6njez3OkppGy6-OFyBe_wkwKtNDA6BsSU7XkaYj6wXqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlmrQBA_H2sCSavpCH3tnm7RcNxyurbO1dWs8Crc0huSAPa7d0p_H-YqTNtpn8h3D1SgGxsEAMZSvVLUKT6dmemDNdzKQtI6n2ro-9JLa6VJbppiY-oaxtuvbOI7DIwbmnHCaaBiMTHRFoo9FREZXjCb-e2FJTsuTe_-QfvTxmVIYbbBNXFvhBDstykRPhxqNEcMMfqDc3x9gVdaSRl0M0uZ4twacoSlCY3xIanvLtLOsGw3nDtFy3tPZZ7GhyWIiOqGs4OoK2JnLSz7D_uAcZScFGd-ZicFfTIPGJi_caTqiryaBdrfC2N0zQNDI4dPrmDYqov2qaseBey7q3sOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qu5dVTJYGBUIhhhPnHFLLvokewesoana07XLY9ZIiJ8yjB31cmZuZNzmCjcrn_yn5PRGoUGjViMNz93PVmJ8SIKZkPXe0zPtr5hQP4UOsJFD69zfVTFlLzVclEbrbhT4YwLv1iy1alJeoKDuyxTNpw_Ou2p7SIqs2dDyqIrq3SpfOAadKMPq_xy3ApkVxfvAkV5wgG9-GgVk9t5e1uR0MADIv1LDWQM5o1gfEt82V7T_mF7E3fkhAqXbCP6dHB67UcQ1EOfMP94R4aGQxWNt8P73_z5JY8x8FpEjQhiqjsbZPWVGXVdPKSnDp3ftvvI-3gxykYfz2cI4hSVAKwnDtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=Y-QK5NBDhGAGGJJdWqGa0SSN2WWyboA0eex1Zqbx9RwVs2uVkxFfhwv1mFGaz6vJAzP9OAIk6BXZWyJSwiOgPJZah6iLIU6h9qx6Rm6L-SQMqPIJM5hHYqxH3u9-0OJb1U_jFwZmnrDH5jHbAvl97IAU4C_vQA1-tWQEIAwo70wZP5AVa384EpDVaboObFXqlS9elUUvtlmPD8lsYRo8oWdMYMad7OQ5_EkZcnXQZQ2K2e8M4tK3WIXQtLdd_OSmEM_c8EvThRojt0pNhB-5koj0pt-DwmT2HupZ2j3pu-4aolTk58OklwZWBEd033fJ1kf84p3ko6hzJBlhgQ71mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=Y-QK5NBDhGAGGJJdWqGa0SSN2WWyboA0eex1Zqbx9RwVs2uVkxFfhwv1mFGaz6vJAzP9OAIk6BXZWyJSwiOgPJZah6iLIU6h9qx6Rm6L-SQMqPIJM5hHYqxH3u9-0OJb1U_jFwZmnrDH5jHbAvl97IAU4C_vQA1-tWQEIAwo70wZP5AVa384EpDVaboObFXqlS9elUUvtlmPD8lsYRo8oWdMYMad7OQ5_EkZcnXQZQ2K2e8M4tK3WIXQtLdd_OSmEM_c8EvThRojt0pNhB-5koj0pt-DwmT2HupZ2j3pu-4aolTk58OklwZWBEd033fJ1kf84p3ko6hzJBlhgQ71mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbRL0D-vU_irFWuDPpgERSCoS4bpsEQJzI_Vjm-Cezg4rT33EsOeGRuTN78zHsfW9b9-mS3tmktGqcrjbHlWSZLd9aXrz58Cjqk4fIiC2SLaaFGQWt3OfNvkN8WX6BmgIEaIfxcSOjFaw7ZHi0TbznHLU65_CwTehymlIHyKUXAgc7T37eWwTACML2nlZsVVa_N91vVsikRpDQP7vZI4y8rqr0ae_VpfzaGdsIKAJmDIm7Uxr4waccS49qkPwthJEBp2Hoalnd5KClA1aazKaR3kSvln5JYNZN5DPeHc-nQ2pEyhHSrBV3tdK4YWbKnqyMlVZj7W5T1vjfCf9YxayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsDIqkwztmHFRQ3Ori7wvOQ-V7Xqy-UqC9EphI7SSAgv6QvLvgqxHezxyMGfD874Seg0GKzK2eeN-39oaW-gUfxSWLCjib-hjw4gvBIXBGX5qonIBDNSejC4iiUzc3CWvBZ3TX31NP8NBa2rTFInWWtU7qYAkLzSI8KDZZPp9lFYICzeHHYIY3hdZFjnTuEJjB2wo2lg29EtkW7sQoXUC9J0h49NZ48FrGFE1TZyfX7TBNuc96h1QV9OsJQ0rhepz65ahzG4VVcB21ZRBdCRG7nG9b0wF7XN1PDhBAfREIrBwZuNpnPS2k7PpRkZ30ukW6AwSa_vZ9Iy7lvJdJCmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fib6SADQBkY_aXVDLFRCbdfW3XzOoz-cVqfNSHvFckoo6Z05QI6leqcx1OxmhQfGkS66ySQlxivgIcgW7QdIiU_-qAe4tTUzgle_CbAdyYMiUyQu22NfQFZwEiPmhtj1KZGBQJM-qHPDd9buCatzq9R_1OVgQMUU9XnzV3PgpEzOndKVN6yBscuvto3_Lhfnio0lZCkyh1cPNsYYHNnrpjISQFdE-7SHCuauMZEvswYLPu5v4iFF5yp4SjxAhf9p2qF8WUQC6TOW_xXCtqHYt97iv0rcFXDTGlbndRZvpujtQPoRqKhOm_wwfcIArswMxX_SJ5y2axGGT8pWxSz0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=lxbPRken4QTza8Ynyj9hfV8C41c75Q0pP-PrMpgHcbGAGyFQX3d_cXxlJuofBQ5IiWAaFMMsAA3gJYFFWK1u702fpcIKnUlxTfmY3UOoZj71K1EWW2m4C8puZbP-x1c2zIG1SJplsyht6s72B73kdMxhbkAkWotDLFo7kNNN-YagBM1pnyOw-R7IM8-AbZr4mm9uhCn3sHpV1OSWa6B3P-uIQWkDqFuCqUnuUf3hYgss2n-1wxB_iHyvr6WxUsdk0QJHhjVUFACDv_YW_p1bEp1d5HUJ_lvTV19trNLKxmEmFs5fdIm8d1WojkdOpZ68KrbaTQbiKhe2b1S46N8aSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=lxbPRken4QTza8Ynyj9hfV8C41c75Q0pP-PrMpgHcbGAGyFQX3d_cXxlJuofBQ5IiWAaFMMsAA3gJYFFWK1u702fpcIKnUlxTfmY3UOoZj71K1EWW2m4C8puZbP-x1c2zIG1SJplsyht6s72B73kdMxhbkAkWotDLFo7kNNN-YagBM1pnyOw-R7IM8-AbZr4mm9uhCn3sHpV1OSWa6B3P-uIQWkDqFuCqUnuUf3hYgss2n-1wxB_iHyvr6WxUsdk0QJHhjVUFACDv_YW_p1bEp1d5HUJ_lvTV19trNLKxmEmFs5fdIm8d1WojkdOpZ68KrbaTQbiKhe2b1S46N8aSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfCHa93X9OmqcYUsQ5CJHLpzlQxbo13iyUSk3kN2khd8kO4Zp1GXbtHHPiJ-WnG-NBhc5YShzeBibzUN3BNSih2_jD3sjTltj4lFxmOD2VjjZ2Dlk-G1POaYTstWCk1kSZo-sufcNJ54VkBfpUPIsyU1OVT_uNTgQ791KG3ZVLQ1MLxW67Ro-jWCgt42FmlyakQXLhl9wCSd4YxnGaVQPp7rtAZTrPkvz54rXhpqtHh0YMZJNQMsHOJe0m8nBSGcipRlk0O6vA6RA1k9WOq99ngY6e_9VYg10MwhhfnPQCuXfH9XLlPF4JLo7iLH03ZEcjlsaa0dQ7rpclvWlzNMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=lXBpMNKBqMBCx4wwCxuoHs0VsiC8iU1v1g9nj8Y752tLTO2M7iicYSXpaiBJzfhsYo0b-JSHO37FrbgwZRZz82HknCN939XcT75au0JRv3kfrfcXzv-2bfxQvTbZJ23pDfJ_tuRjW7poYegFJFq9CIYZ00_cXIdo-iiuf3h3EMEoavcauPxfMOHkchrnOMZj2766a2E0jjrQURtzxuxjwxs9X5Bw41B_NA264yS417wOw28FOl0k8KEdLrkodwMeeqnjy6cxYBojtRZejKf0lF2iaEA1nYA7Y3ZbpgBxAf8YzTCLd--4SDJkI5UHhHuYuwzZuFejFmTaqrx3tqzQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=lXBpMNKBqMBCx4wwCxuoHs0VsiC8iU1v1g9nj8Y752tLTO2M7iicYSXpaiBJzfhsYo0b-JSHO37FrbgwZRZz82HknCN939XcT75au0JRv3kfrfcXzv-2bfxQvTbZJ23pDfJ_tuRjW7poYegFJFq9CIYZ00_cXIdo-iiuf3h3EMEoavcauPxfMOHkchrnOMZj2766a2E0jjrQURtzxuxjwxs9X5Bw41B_NA264yS417wOw28FOl0k8KEdLrkodwMeeqnjy6cxYBojtRZejKf0lF2iaEA1nYA7Y3ZbpgBxAf8YzTCLd--4SDJkI5UHhHuYuwzZuFejFmTaqrx3tqzQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ZP7I1EXYUr8UAtAjF9wG29MkZ6qyQMeKYs8k8I5Kmp7dZm2B6k0liTQ9K_LS9xfar44WvUlPHk7nggLE6Iol_LPaSvRZhLfKDUllp430cIUNMADgooRlmgSdkTd6o0Iqy8bxd1EiJgMbrpu9txrzjLbIRHjlba8T0elVSkuRkEYDnhI7Tzw_BUOS12upZMmd5N2Hbfz_hqlFeWXxDM61Ii2OkR4ZPh8Za3iKzh1IiJICsQErQU6S7ISZdGJuDpM7_y1CFshj0_3eMOdIshadL7knnTPCMaCSfzdGEgfdyFsplvsU8V776FWpobEZ3q-ool8UYpisSYDuhkpvwbMKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ZP7I1EXYUr8UAtAjF9wG29MkZ6qyQMeKYs8k8I5Kmp7dZm2B6k0liTQ9K_LS9xfar44WvUlPHk7nggLE6Iol_LPaSvRZhLfKDUllp430cIUNMADgooRlmgSdkTd6o0Iqy8bxd1EiJgMbrpu9txrzjLbIRHjlba8T0elVSkuRkEYDnhI7Tzw_BUOS12upZMmd5N2Hbfz_hqlFeWXxDM61Ii2OkR4ZPh8Za3iKzh1IiJICsQErQU6S7ISZdGJuDpM7_y1CFshj0_3eMOdIshadL7knnTPCMaCSfzdGEgfdyFsplvsU8V776FWpobEZ3q-ool8UYpisSYDuhkpvwbMKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=jeQt1vjeOM1-gxo4dnOPzTZBQztkH33ZoYG_FIrS_wqFkiIgAFPIRrRZM5nKP1WS6KyCDY_IntA0ZeG1Icg42Dt-boXiFPUIv9zYfIBILIPSFe8FsXPdh1QMm08o6Bu6adG4wUg__Uc2MImwQ0msS4KteGDQTI0xDvsnKJGX-gxD2bo5Sc2RxgFPboGL7XEI81_IvUABAyXX71iEIqySMZVsJc_o1pCNe2y94Y3teLFOJCRlILy0_b1qiP_fs3QWDqkvwD6E_0N4GBDE6t21Rks1mYAh2K8cPrSlDGbTvoDee6t_IV5fQz8eVniLEfEjqiw6eG-AnnMa-xc33EincA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=jeQt1vjeOM1-gxo4dnOPzTZBQztkH33ZoYG_FIrS_wqFkiIgAFPIRrRZM5nKP1WS6KyCDY_IntA0ZeG1Icg42Dt-boXiFPUIv9zYfIBILIPSFe8FsXPdh1QMm08o6Bu6adG4wUg__Uc2MImwQ0msS4KteGDQTI0xDvsnKJGX-gxD2bo5Sc2RxgFPboGL7XEI81_IvUABAyXX71iEIqySMZVsJc_o1pCNe2y94Y3teLFOJCRlILy0_b1qiP_fs3QWDqkvwD6E_0N4GBDE6t21Rks1mYAh2K8cPrSlDGbTvoDee6t_IV5fQz8eVniLEfEjqiw6eG-AnnMa-xc33EincA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=t4O7wXKHIhUQmPvcS4Kc8TRdYDmcEGpZ57pstiA4dFap7wkGiQyFlH_QmtpffmVA3zhRoHVsqtnNUUoFlx41qxEk0YCg4AJAH1oG7ljx-n1d2eNMKFJyDj-7mdCzn_DTaxExVt0qTMywpk-KMODadQu7pbGt2ad6cTTFvp0-9iK7uenmZlIPuww-n31QtUqha5YbJbo9tzD0_-DOrBJNWxPqoHUUFeVdwkIbbj7MPEV-EsKqHYWWb42lQIkkGmbcaz34vVN4ftdMUdeOtjjNo4YKi4Xryr89DeovIwD5aOMb0N2c33NbgfTwQvDbv3r14JlY8gP-SkD8h3laht7xTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=t4O7wXKHIhUQmPvcS4Kc8TRdYDmcEGpZ57pstiA4dFap7wkGiQyFlH_QmtpffmVA3zhRoHVsqtnNUUoFlx41qxEk0YCg4AJAH1oG7ljx-n1d2eNMKFJyDj-7mdCzn_DTaxExVt0qTMywpk-KMODadQu7pbGt2ad6cTTFvp0-9iK7uenmZlIPuww-n31QtUqha5YbJbo9tzD0_-DOrBJNWxPqoHUUFeVdwkIbbj7MPEV-EsKqHYWWb42lQIkkGmbcaz34vVN4ftdMUdeOtjjNo4YKi4Xryr89DeovIwD5aOMb0N2c33NbgfTwQvDbv3r14JlY8gP-SkD8h3laht7xTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=sD9YVzmY-1R6S9sv_2Zsv_nNhzipIsKvdjlecpWKHelhS5QKRx5RSq8xcm7UA9CGa3NI5O3ZAbkdSzLsbqX37daJmIBJL_sNbb6dptGFWEatQjyN5KWhJ6bta1tWGXh1w1pOg_zK5sjOHuDNlWUjtL8ANsNpXXvSyMDAlwRqcQH3Ybt-brAm7YowYCBlCntlgRsu6KHN_S-h2VICA1MJ_4q4SWE3SUt1l8q1wl3vRTlfmdnwVxYVTXGY7w1FjmxzDgKe7lL2lwEFwrhQJdBt8R6uABJpRAhD-35_xW_Xjka9VIX8Nz_kR4cBYwlEumq2JwkpPh4Vy7pgPwWPNl2RjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=K9AvTxPkB-kLZ0VbQiflJ044lDbh1nRP5xvVeau9prS1ErPOpx3X3KFpQeedjro91j_RNohqIjn2sdkpdk7GeDcdhvBdhhQpdpSIEvCdmMOnvpPPNT0lwmP4Zs341vPfx-jCJZsjuGz-prphCHdjIX-uJixHeShnqGokE7rr7kXL798oRLvBdwId1cpKqm-dDeiD-9YMXj-5qn3p88gq2rBNcSfq6RMPTJ0vxRsM5ciIZcWc83zSXihadoPgbqNfiwJk1RZ8QPX2DKu3M8kkT658t6SOm2gdXb4H9g3GgKMYNqGRNWGsNr5ah5rxNARU9wTKHJVI1jCzMhMm6uBrkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=K9AvTxPkB-kLZ0VbQiflJ044lDbh1nRP5xvVeau9prS1ErPOpx3X3KFpQeedjro91j_RNohqIjn2sdkpdk7GeDcdhvBdhhQpdpSIEvCdmMOnvpPPNT0lwmP4Zs341vPfx-jCJZsjuGz-prphCHdjIX-uJixHeShnqGokE7rr7kXL798oRLvBdwId1cpKqm-dDeiD-9YMXj-5qn3p88gq2rBNcSfq6RMPTJ0vxRsM5ciIZcWc83zSXihadoPgbqNfiwJk1RZ8QPX2DKu3M8kkT658t6SOm2gdXb4H9g3GgKMYNqGRNWGsNr5ah5rxNARU9wTKHJVI1jCzMhMm6uBrkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=fj9jwWlkfUhdcAu-4U62Yl52lPSaSOvcQuDBScovhABOoJ-PEa94YG5XkW8tWJR4A4qnMazbkKRAapDgwSvfHL6N64R2TDW_WTgtVwFcijRdtvfUbiQksMuC51MiCgY-Zj0mD2B1ENDdGm7zasCmw0PmAWtSRPgx383N-k1g6HEphLGg6zxVh33K0Aab4Dsc0kFm-d-_Xr-aAP2MkUkNGvYQ3C6CG4RSjhlIjMwos1eveAbSfllTV-7et2cagMYsq-9NyvVUm0zPk_Ol_ZgKOoxTjrH-8sPM0_yV20awatXdmpsDVM2Qn0BbtS5dDRfrK6I9ifBrVaz7CPWJZZglCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=fj9jwWlkfUhdcAu-4U62Yl52lPSaSOvcQuDBScovhABOoJ-PEa94YG5XkW8tWJR4A4qnMazbkKRAapDgwSvfHL6N64R2TDW_WTgtVwFcijRdtvfUbiQksMuC51MiCgY-Zj0mD2B1ENDdGm7zasCmw0PmAWtSRPgx383N-k1g6HEphLGg6zxVh33K0Aab4Dsc0kFm-d-_Xr-aAP2MkUkNGvYQ3C6CG4RSjhlIjMwos1eveAbSfllTV-7et2cagMYsq-9NyvVUm0zPk_Ol_ZgKOoxTjrH-8sPM0_yV20awatXdmpsDVM2Qn0BbtS5dDRfrK6I9ifBrVaz7CPWJZZglCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tmTzHyLE9bSOtNalk-h9kDcYXjlFlOceAJIGBFLW9gTPoIUE01sovig_SPDkyPVTqlw9pfrnYX8pAv4w10afLOa9vh5YV06v8UcNk1kGYEc1xAIpFt832jblIVY4BGYlD1KuJBZjd_Sqo8qHzqsT3XLyqlFnpY7vF-ca8JsMytldNMsyhyjM6ILdW0hbiqSTZiQCyfwRagAwq9TBJNZjFP8M5tBF67tv5B4l62D6mMWFH-2Hy8JnZ4p5pEIK9wzJlXyzhFbmZom-KBnkG-x4_LVsRTEVUPlJVT92OU-uk0tmv3cn5tWnQ8DBDlbOgZW8D2z5F3iBM-ga6BbPJCoZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq70ZD8DS9Lj6lTOoRme6tWeL_su5PJ1k5OLRciHEGTJDd5YMc6MSKX2bAilXR-Ctust_uHtetaeC4YwurIX71qJiIi577nBKeb7k7FjBNT8fnUVjFawUpHi0FNav9dZtWzD7osI16VHuih_4sQmvbtif87rJLKZ-wRrxbsZiKKEaG3NTbXNYKV9FJ3KArDcXuFSoyAFs_hZdFfMi8dseRF4wTpoov4CA__0Ha-GB1B5_-BPkR-_GnMceOlhaxVMeO_tpSPqS8KLvTbQqsOlRsoKvu4jom4QjSGZZ3hJt_MgoVTkwTC49ybixUQKaGRwrV8FCvx60H6QYG9fYqmM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Gz0UGTbmb1l6s8Yco3aPzKPverUQnPLA-kXjWezW0uwAdVVjgHrht78GMhJJuodPAuy5hkuwNaGYkspJEVLPXxvCkK5qx8QC-AXja4L0hSfkJRTZEvU38sXrf74j0Jd5NRNsS_laGQAcCOCWnfAQpbJ9M5aKs_btDxRmRQJj9JIccHxZhTXSSiMed9hf8XFeD0-U8z7pNIJ9vgCQX0P5Qn2EHx03Hf6QkvsnIyM_yaxFErHUv9NdlPSGEU28Huq6-FE4YhKUimdS3WYvXR2UkOr3IOTf0BY5oYhXE-c-yuCdaI_lLtju4azenqFP7JI9DLYiOjAMOnGWxMKzE3TMaQbuVuTGwnQ1fuRezzuwReugq9gMKMB8qlMECm_F3DfNTubfwoKx9jpFQcDg53avy807MR4gaay0smHRgIu7mPewTayvADHt35PHzgB0nNViNZ76a4Xv47jeu2Wtjh6OSV27-52EPozoUerOW_4ve8ExIETczxzgmM1WzpJWO-IUpbxtTU46i83NtxSZnobubnn0kq2gjbwXUlzKWhRKwYecPI2HT0HeEu9fxPryOdntP8Yhm2LYQJ458LEa2Std8UfNEhLp_cotsBWk0ZGDCpACuqsNBLICVAUULgWypAiN_W3vU4InarcER_FIy-X4EEdm5nUCB9lBOHx8n-6fQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Gz0UGTbmb1l6s8Yco3aPzKPverUQnPLA-kXjWezW0uwAdVVjgHrht78GMhJJuodPAuy5hkuwNaGYkspJEVLPXxvCkK5qx8QC-AXja4L0hSfkJRTZEvU38sXrf74j0Jd5NRNsS_laGQAcCOCWnfAQpbJ9M5aKs_btDxRmRQJj9JIccHxZhTXSSiMed9hf8XFeD0-U8z7pNIJ9vgCQX0P5Qn2EHx03Hf6QkvsnIyM_yaxFErHUv9NdlPSGEU28Huq6-FE4YhKUimdS3WYvXR2UkOr3IOTf0BY5oYhXE-c-yuCdaI_lLtju4azenqFP7JI9DLYiOjAMOnGWxMKzE3TMaQbuVuTGwnQ1fuRezzuwReugq9gMKMB8qlMECm_F3DfNTubfwoKx9jpFQcDg53avy807MR4gaay0smHRgIu7mPewTayvADHt35PHzgB0nNViNZ76a4Xv47jeu2Wtjh6OSV27-52EPozoUerOW_4ve8ExIETczxzgmM1WzpJWO-IUpbxtTU46i83NtxSZnobubnn0kq2gjbwXUlzKWhRKwYecPI2HT0HeEu9fxPryOdntP8Yhm2LYQJ458LEa2Std8UfNEhLp_cotsBWk0ZGDCpACuqsNBLICVAUULgWypAiN_W3vU4InarcER_FIy-X4EEdm5nUCB9lBOHx8n-6fQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=DmcfdNxzeHPnEhxCUJd2rU4v_PPHUwPDiGIU4gm2Sz1gOj0WVS9UdCBNkEUJJwfMYLkyxI1f6OONcnWTq74J5w4whEIFkeIGmFdluN01HFM8FyrDdiVNEKxhbempqMhGXHwjxQdfSAI6sdr7k6mOna_gtZf6_6htASqKJJW4P_3D1apGVkrODA8ocT499j48zUtiRkDkrzudfZLSBClWylj5mojKcleLFghHr-Hgacqme0BjNiqINj-tu5kkGsCgZEfVgEYf1q6cg8A_tppTAmv5wrz0mTTdLR12X21TGcb0kcRW_4ObKunpKg9QC4w60a0osJS17xTBWRzj5CExyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=DmcfdNxzeHPnEhxCUJd2rU4v_PPHUwPDiGIU4gm2Sz1gOj0WVS9UdCBNkEUJJwfMYLkyxI1f6OONcnWTq74J5w4whEIFkeIGmFdluN01HFM8FyrDdiVNEKxhbempqMhGXHwjxQdfSAI6sdr7k6mOna_gtZf6_6htASqKJJW4P_3D1apGVkrODA8ocT499j48zUtiRkDkrzudfZLSBClWylj5mojKcleLFghHr-Hgacqme0BjNiqINj-tu5kkGsCgZEfVgEYf1q6cg8A_tppTAmv5wrz0mTTdLR12X21TGcb0kcRW_4ObKunpKg9QC4w60a0osJS17xTBWRzj5CExyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=EjQym36GZYE0cAIsjYDzQgSiSXxqy6TF2bowkDpkF-ZNSYqQ7GPAGhcgRptnQEflUMssQTEOVqrS2FRZnfsVvx4zSTOAtndu59vVc8KSk-bL7bJjgRbMGGjS3BHh5235F3K2G4nRTzcaNDEeUzIodoLz618MvfJFnViPOw9zLBgLDOFBZI7Qf62CIs-rQrqARttY3yxx4TP2qpu064_ElRr3ipdd74TZ5joscXx1-A0rF6WQeJXSKjp1Bk_LNl-dp2fBFLNa0Yh0J9Cc6pR4OWyVTF_YbY_0kVyDYgM96qctH71Keazsx2qNaaIabTGZ-HWJbTHybRhI1hJYFIktnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=EjQym36GZYE0cAIsjYDzQgSiSXxqy6TF2bowkDpkF-ZNSYqQ7GPAGhcgRptnQEflUMssQTEOVqrS2FRZnfsVvx4zSTOAtndu59vVc8KSk-bL7bJjgRbMGGjS3BHh5235F3K2G4nRTzcaNDEeUzIodoLz618MvfJFnViPOw9zLBgLDOFBZI7Qf62CIs-rQrqARttY3yxx4TP2qpu064_ElRr3ipdd74TZ5joscXx1-A0rF6WQeJXSKjp1Bk_LNl-dp2fBFLNa0Yh0J9Cc6pR4OWyVTF_YbY_0kVyDYgM96qctH71Keazsx2qNaaIabTGZ-HWJbTHybRhI1hJYFIktnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=H651PKGUq7YQLCsW122yiLPW2EleF5O6p1UdDSRseJwKxGxVBSFNB4EdaR1wNYzCCdn0-G60EAeG6ly9wV6E1PaIaZWhYlQqJ4cYjAZtK5SZaWTZrgTBOjm1wXjMb1A8y6C5McYDjHHcfR4p5jvTgIMj5JJGtfQg0-tNN9jFsjdhV7CWWiU5Q9H-DQjk6qnp8ks4gj12HLXcyYiZlrIY4GwlnUwbpqZoF6REhxDgZe5Dwl8ks3SusGtf9Qj_qMv0lqOwGC-nNrQZEKKd6HWt_LGNXWtLgP1vtu0a9uLAHdXpJBKFuHfFAUVv6gjKl-xRi7haD0NZaQ3hmtEYca_6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=H651PKGUq7YQLCsW122yiLPW2EleF5O6p1UdDSRseJwKxGxVBSFNB4EdaR1wNYzCCdn0-G60EAeG6ly9wV6E1PaIaZWhYlQqJ4cYjAZtK5SZaWTZrgTBOjm1wXjMb1A8y6C5McYDjHHcfR4p5jvTgIMj5JJGtfQg0-tNN9jFsjdhV7CWWiU5Q9H-DQjk6qnp8ks4gj12HLXcyYiZlrIY4GwlnUwbpqZoF6REhxDgZe5Dwl8ks3SusGtf9Qj_qMv0lqOwGC-nNrQZEKKd6HWt_LGNXWtLgP1vtu0a9uLAHdXpJBKFuHfFAUVv6gjKl-xRi7haD0NZaQ3hmtEYca_6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=GacvOfC1GmQ53WzkA4Z-N2bcQcYiEWB850qJGINVh-YXHDYzHnsiUA8RpK1sSKAJ-GMi8py7pFMb7YtWL_ZCO_QsVGzSym1esSdQUaWghPAzsYOXQ6SXjYgREx_W_x8tSWvma2ZuVndMJb-IB2aafQTIlbW5eD6U6q41e1R35-Zn2-rKLJMG2BZUyObBjF0Sq-suMP0cDzkypFGdQDlUQDHvOMUkb9SIZ_fr_NirBbEP8SSDH-vRnKtHoF2iVHF47QikjLWH3rpwcRvogI0W065HHkV9kVacm0jhKxbUgkiRiSmqb1IKe7eZ4w_yAH996UddAC0Ldj9PpLqgqDMNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=GacvOfC1GmQ53WzkA4Z-N2bcQcYiEWB850qJGINVh-YXHDYzHnsiUA8RpK1sSKAJ-GMi8py7pFMb7YtWL_ZCO_QsVGzSym1esSdQUaWghPAzsYOXQ6SXjYgREx_W_x8tSWvma2ZuVndMJb-IB2aafQTIlbW5eD6U6q41e1R35-Zn2-rKLJMG2BZUyObBjF0Sq-suMP0cDzkypFGdQDlUQDHvOMUkb9SIZ_fr_NirBbEP8SSDH-vRnKtHoF2iVHF47QikjLWH3rpwcRvogI0W065HHkV9kVacm0jhKxbUgkiRiSmqb1IKe7eZ4w_yAH996UddAC0Ldj9PpLqgqDMNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTOjVX3cjHtcRDxpj2Oh4engJUbjiNop8H4EZCHQ0eHCnt7XxuKH66-aUQeZc4pzxhE09zvF1-5CAL6IbRkdxJKkHDoFsFH5t5-HcMZFrolmXy_ZR5CGNUblAkRgzamP8kghJF9gj1_uQ6Szt9kEcELWo-Jg84uxmwajGNIzlIzOIEu1QkZhCl15wVh8Bz54ndOjCw7t1xkXlRGrAqRO8GmfsPxJNf4PVd5WaBWRVTlcUJe_gjHc5oKgBLPA5J8x9JfJi1NDG6wF16YyCT4BJ65JVySEJJr70HIsWgmFqpret3X6OeL4cX1CcQPpw97Wt7MRJt5JsRBf01QnBPBjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmwdXkpKDULzlSEHOArS93zju-YYVVZcBEy5LlRkXYQqiZgKkojvtDXfn92F2--nFUEt8dyB1dkCTivepfbqJROtms4tW3965-3NPniePy28yWPH0S0INVTR-aHepuZ4KyiWYOjMYN5WvQoUCVPWKxITEp-kkSSl-Y_UuRU6GO9YOvu8XkbphHQh_PiKLGonBay6Ifbu66cG39shtgPsOVIuqETxqdtPLTkPn1WdWH-NxWEbiGFbcYfucWiUjmaDokGlfCpS2VMuGFClYRthkNBgZj1Ght4jazqySurUbBedL3aU6zj24tyr6Jy5ipjHVs1gIGWn4PuywonoJS2Olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqxfIkLKkRTAsZn2FSzN15t-3GZ_BxjvUAPng84A5JuG-7s_cuG23o_FshX5DbJI2vSpqz195jr1rTbUhUOvQxj0Jf3zKLLp1tr7yoe3Khxz7E-wIso9F45RJQQPLbzikW19PHA21XvYKZPB0uj_P-Pq3HtkSlGFj8bbud0na5zhHtP5f-NcagwHA_2lmzmqmg_HAxGTmaGJP030Uzy-WTB0P2odw5nCqlDnmKS-XuJhc8h30o-3fjd_lXfHgjGdzqWKddRsGvgJ7luTVgQNr0z7LprVx3kBEVreJVCBxo9EzGEQq_J_j0SwrxTVql1f7qouZkZw6nxf8sbBg4gxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jko3KKVtpfNvX_qEPDv2jSTMsetqUbaoezDDQufejWQ8OyhxM4KxGr0LiCvsilOHqyq_7bh_wail3XISk7Hfxh8H_q2fhg467YWZ0lj70THfae2gBOUPqFzQyRg3UhDYejLUmPASxpIUo7BbetpM4OGIrji70mzTrjFi0PisUTPGL6K6medboOdxsDRTdoTn5M4iMs02H1de1-iLUET0kvUxcxCKV7TE9s-f0-e9i0mJXb1INBP7KMkHoLmU4gbkOzcxFMTLriDd4q9bg3K45EEXSi9l8KUotsboZ5EfwvfnjZBhBiW4coXHnOk_GpaYNZHu9471UXm0FepNAB5UmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw9-ULdFkBmJu4I0gxPbLiHMWMjmDTdvPK2MRDLcr-AsxT1L7kSYsqfta4b1Hw46VYW52-qOgUTthNjmQHs_xcu-36uy9msIYcNwxiwH6BmbLeZ-o2TyJNKS1B11E1cUFW1pzuPVFleiZs3dc5Af5pVSXZ193bhaB7LI839sSzT0N9MzsokC0q2mGhXrWVQUSbzqVpzuHYzPswRWGaL7a0vyZNt5VXBq5-XHhqGmPmS0eEtU9tAC-DIA9mYtBvoDYxVYceN13bAbcIo1QVkaX8fqSO2OSk56hWTeV_PmNgmFk00qnCNXVQEQYW34u-zeopnMB02J-Waahy-DA0SabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS_U5uKP64hg0BLyIbd02FIZ1FVZRROGm5w7JmIpRAq3PAtMe36Z6-l1tB1e77WQRVa-ZdJ2rZOdAuyGD5SAMuRZlcvnCJi4ky7HxHUv4joNN3Ym4VN-eZiar9vnbhHgR9kDLXN6vR1M7JsCoz_5A-S2fAXyWbZBemlJTJPn76HlCwV0E6EeevHdcCRfkEJ_lS5PlRermssKMMdl2t0A_3Ukf304auLcTXRHUJziP8ec2vZVkWerMlmb7etaDrXVp_EfRji8Y6Lx0VeWdR4_1jKOYA3t3qyNACfmofZBVQ98PlqBeLGsKcRuD69izZVXYtMyFKAeFii7ADrMw7jWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=esM9Rn0WkM5_gByhPlsBW5DKB0w4lHxIYYAR5YN07L4FaXjcRSa8S_9YkXKTf5m0wehDOepXlOyIKtwxLlwG_3hpMsA9DQK6Ko0m9xF4wlHThuk6Dm2DWaNOEbomuNNLYqE6gAezUokEKbucGEu75cTU_Ogk-Ev1RD7rh-iGtykdk2UgbMIJbq8QZEyeb_CMHTm3YslgjPTXzEbO3piUqF0SQhItXAVbDjvfFt6LcwtvCBkkeIoQr9ISZXVV3blCopppBKbYD09J6C57U7tf8dOMA8HRm5NEZmN8UqQ-L7BMPSHMPa8C65Zfl8F_mNaIgdlvT10D0pOfCSptcn10tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=esM9Rn0WkM5_gByhPlsBW5DKB0w4lHxIYYAR5YN07L4FaXjcRSa8S_9YkXKTf5m0wehDOepXlOyIKtwxLlwG_3hpMsA9DQK6Ko0m9xF4wlHThuk6Dm2DWaNOEbomuNNLYqE6gAezUokEKbucGEu75cTU_Ogk-Ev1RD7rh-iGtykdk2UgbMIJbq8QZEyeb_CMHTm3YslgjPTXzEbO3piUqF0SQhItXAVbDjvfFt6LcwtvCBkkeIoQr9ISZXVV3blCopppBKbYD09J6C57U7tf8dOMA8HRm5NEZmN8UqQ-L7BMPSHMPa8C65Zfl8F_mNaIgdlvT10D0pOfCSptcn10tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CCuevmqnioOC8Hd61SC3U4jx27emKPuY_Iq8EHEAclfEzZpEGIGiKGx8sAjDG5CQFsWQALjjGN3jwvGMI2YepbgzynYDa1J4Z2jzTn0J2BWgfqoEcLGNyrmtoXJWR0O06Fjs7jf8Y0szIuNPaxXYfscm0ImXgq4wgpcCPhVg9g5JAp7tLRid8Zgdffo6be0efJpdJz0zpsPu8T-apAAdgp4RUpSSBaYXF4OBFnR0uka2p2sqBKriCXp1jxIKK_cqabKE42UnlVjRnXa5bxeuc2DFmurzgD3FfjeO74bvt-fMwMEWncFGQ4KfScXFqtFzYd5mZ3r6DzxmrWoZR5DtJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=RnWumNrKWWikFhPyuMaENGPDsH1QDXf7HqKwNWoYPkjo9c3JLAthE2av-h0Jo_WrUK3xNY9Twpn8XoA-oFIGo4YeZNQkwwNxDY8CfBd_KIxegV2tDU_7Q-U1rmnoT9YluIVpPsD0LHpaEo70zGLNmBzEuuU0N2BIRYOfPZ68MaZQ_oX_a_jRIvqPgG8q1xLyd137HWn5hmxNvkzDe5BVDM37B1QT_uJlzyDcOXzUKb0xhVrnyQNnvKMv1SBOOYLTDkP-Xv7F98zEfq0bLzHQJwibiGvdKn0YDOwXPo1vkQ5YyVCWiCPEHWeySMeg4XWabLuT35uLmSGGKOJstCpMKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=RnWumNrKWWikFhPyuMaENGPDsH1QDXf7HqKwNWoYPkjo9c3JLAthE2av-h0Jo_WrUK3xNY9Twpn8XoA-oFIGo4YeZNQkwwNxDY8CfBd_KIxegV2tDU_7Q-U1rmnoT9YluIVpPsD0LHpaEo70zGLNmBzEuuU0N2BIRYOfPZ68MaZQ_oX_a_jRIvqPgG8q1xLyd137HWn5hmxNvkzDe5BVDM37B1QT_uJlzyDcOXzUKb0xhVrnyQNnvKMv1SBOOYLTDkP-Xv7F98zEfq0bLzHQJwibiGvdKn0YDOwXPo1vkQ5YyVCWiCPEHWeySMeg4XWabLuT35uLmSGGKOJstCpMKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=bzftEMTrDZRk7HZc7sEjptIM0AWLqqMZTxPCChHKea6ph_MAInNacT4DUm3xSH4FyevMW0Yt3yMGMSAmCPJAPrt5hI17J_2ZO-gNnsWp5ASKV6a6DxkCjcpEqUwoUxlJ2oTwEz7mLmjSCDol0Q5rr0iaxpJ9E3R97oJa2sEvc6vyAdNEfUZdss-DaEfdy8Zpxmk0CuZwMplzOqRjLq7yueKWxBgsKFbDlrcjQ6XLdMJs3wK3Q43HYZMTAVTkFPA8ilJh92nvPzqtQBwl44Q3Ep5uchqcwouh1mgDbe1KmXuHAx45NhwIvpRBr-3nfTj3EUTMjK7z97_RLJbt9yf1SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=bzftEMTrDZRk7HZc7sEjptIM0AWLqqMZTxPCChHKea6ph_MAInNacT4DUm3xSH4FyevMW0Yt3yMGMSAmCPJAPrt5hI17J_2ZO-gNnsWp5ASKV6a6DxkCjcpEqUwoUxlJ2oTwEz7mLmjSCDol0Q5rr0iaxpJ9E3R97oJa2sEvc6vyAdNEfUZdss-DaEfdy8Zpxmk0CuZwMplzOqRjLq7yueKWxBgsKFbDlrcjQ6XLdMJs3wK3Q43HYZMTAVTkFPA8ilJh92nvPzqtQBwl44Q3Ep5uchqcwouh1mgDbe1KmXuHAx45NhwIvpRBr-3nfTj3EUTMjK7z97_RLJbt9yf1SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=q1RlBHYuzLxAqjQ3k4lUJYI7mgMxqBdutBOeXyP_mxJROYNx6jOehKk1ylKjOl1ficstbMOM6-Z5UqDPtY469w4kP051DWoUi-GhB6nl_O4WSP_emKFOVbu3MWW3BjCWPXVk1uB4qDb482gJ8VCkbyQXJ9VMbsB5hSMfKJ9TPk_S1qnA9OOTqR9yi0Tpc_hSStiZKu-xZxHOqv8h6P9jGfQKCbSrpwyuw2uqTjbsBu5OEIVvqW_M7QevKwpJmNI-7EapYd4_3ZyBIpNisCMwFOrHWVtRjXP-sH3WM2e0vmxEz_z4ak041lFUeywBOrVaduA9G6YzGtMv2d524km4wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=q1RlBHYuzLxAqjQ3k4lUJYI7mgMxqBdutBOeXyP_mxJROYNx6jOehKk1ylKjOl1ficstbMOM6-Z5UqDPtY469w4kP051DWoUi-GhB6nl_O4WSP_emKFOVbu3MWW3BjCWPXVk1uB4qDb482gJ8VCkbyQXJ9VMbsB5hSMfKJ9TPk_S1qnA9OOTqR9yi0Tpc_hSStiZKu-xZxHOqv8h6P9jGfQKCbSrpwyuw2uqTjbsBu5OEIVvqW_M7QevKwpJmNI-7EapYd4_3ZyBIpNisCMwFOrHWVtRjXP-sH3WM2e0vmxEz_z4ak041lFUeywBOrVaduA9G6YzGtMv2d524km4wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRDJeYZtIU0XU1Kid_KgCe1L089j5H57YIG4ScuUIyxW0DyKvJh0o0GUOpT163Kctz-oZX7gGTV50PAuCzx5yUx4BIdY0dVa8pQDuSQF5MdOUUjjdzTcbeXeqt5CM5h9ueOIBeb1GC-7vyD8lKil-CQQ45Hnt-orb4-oznZFeiCaSFdokbCbKK1qNOIqJDTDZ79UhkoibzJMQtOeep3CTHrHX1ity9rppw4QWetXQWvd_HTH0QX4lb0Y2jwNh0QNvKzjL88Gduf9QBjAs8QfV9D5-0ivVkLmcp_7_rg7sPtfnxB-VHx4z9NbGGHOLAiHjFZnIqAH9R5NTb0nBS3D4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=u_YJ4J3V5UAcHexhpRR-Lt2p5Q4DqzXVO4iIjhsZxBbb3ZixTnte4oL8thdQWkhuoh5NZFqCgc-E1hHCNoZFwxDTZkRlKlWoBuaGUW_ru3OFUtPiykfkM_08BXamXb3r1Ioua4YVfFrH94DYmv6f1tnm_96ZjvusNud3FsJ1cAKkotsgifcbyt62eQMNDv2aaEyEomjX2_dRw9HazXH6gNjibhgnPEh07Y3GJ1Wj-YmJN1PV_Myfjn8taNJHhmzFNe5irhG1SRMPXiCmv4eZ6HwBwh76Ke3ar23RAtJqHVLZRFMCwigvA2bZfIqn2kiLZqhPeY0XMv93w5P3cVCwOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=u_YJ4J3V5UAcHexhpRR-Lt2p5Q4DqzXVO4iIjhsZxBbb3ZixTnte4oL8thdQWkhuoh5NZFqCgc-E1hHCNoZFwxDTZkRlKlWoBuaGUW_ru3OFUtPiykfkM_08BXamXb3r1Ioua4YVfFrH94DYmv6f1tnm_96ZjvusNud3FsJ1cAKkotsgifcbyt62eQMNDv2aaEyEomjX2_dRw9HazXH6gNjibhgnPEh07Y3GJ1Wj-YmJN1PV_Myfjn8taNJHhmzFNe5irhG1SRMPXiCmv4eZ6HwBwh76Ke3ar23RAtJqHVLZRFMCwigvA2bZfIqn2kiLZqhPeY0XMv93w5P3cVCwOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=EGZB1gDKTEd9wNLwfZ2QCBcXZUmq4hV6SepjG4itoBqKR7MFuONBxsoG-d6ry5IbFsIoD6ValkRAeHb30BLfKiQRF4qVcDNIZE39-yeUU_AYGwCxj_LlTk0ELX7xEg_3fsiLH_VWRceX1Rxvp_YoWPrmg0gXftHAor0oH9bD5H9wWzaavkX8zL_rLgVg0drrqSOs3sEE6C3JDZaGlcFQURCPm9HfZilKzIlNJJRtOT8EYirkdGEgT2X3TKApTXC9QXEHF6_MeaUIg9N4xdvhquLBCrt5bnswsPKr5r1koirPdTPggSpE48g-u3dRLHRrXHLxU1rtUG0JgLwOznQRNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=EGZB1gDKTEd9wNLwfZ2QCBcXZUmq4hV6SepjG4itoBqKR7MFuONBxsoG-d6ry5IbFsIoD6ValkRAeHb30BLfKiQRF4qVcDNIZE39-yeUU_AYGwCxj_LlTk0ELX7xEg_3fsiLH_VWRceX1Rxvp_YoWPrmg0gXftHAor0oH9bD5H9wWzaavkX8zL_rLgVg0drrqSOs3sEE6C3JDZaGlcFQURCPm9HfZilKzIlNJJRtOT8EYirkdGEgT2X3TKApTXC9QXEHF6_MeaUIg9N4xdvhquLBCrt5bnswsPKr5r1koirPdTPggSpE48g-u3dRLHRrXHLxU1rtUG0JgLwOznQRNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=AZ5tkEkYg-lrUfEj3xJvkv_PkFkpy6p9s5efJFCdTDW_9r-CKIbyhid8WohuGilJhmZ7cBTwLK49lhWd7C_0Hhwlrjkydxp4hzE7qL8Utt5LxMjbXyk5eQHd-BEsJghFRG4sHUz3VDPwM8T3ZILPJSbmlgSR4vWPJIHHQhVucSyUr7WJT69j-P8Fk1NxrmVgNd0D-04UrPI8_6QiXG9Y_ozRKjiUoH6aB175Tf6vPYhdHrKt0pGaSJLiFuxehFnmrL_-pYRmbSbEtOCUljkZBkRH2ooc3z6ucUVaUDtQ76QfnhvKoH43BVo-W9nZAwL27kN2k6_9HJk8x2YyGq00dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=AZ5tkEkYg-lrUfEj3xJvkv_PkFkpy6p9s5efJFCdTDW_9r-CKIbyhid8WohuGilJhmZ7cBTwLK49lhWd7C_0Hhwlrjkydxp4hzE7qL8Utt5LxMjbXyk5eQHd-BEsJghFRG4sHUz3VDPwM8T3ZILPJSbmlgSR4vWPJIHHQhVucSyUr7WJT69j-P8Fk1NxrmVgNd0D-04UrPI8_6QiXG9Y_ozRKjiUoH6aB175Tf6vPYhdHrKt0pGaSJLiFuxehFnmrL_-pYRmbSbEtOCUljkZBkRH2ooc3z6ucUVaUDtQ76QfnhvKoH43BVo-W9nZAwL27kN2k6_9HJk8x2YyGq00dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhS8giQv3CHSO0F1AHMfMbrOcMqiMGvov6piyqvgUf6e38GdQxhGW5_gFJNyXIwbpj3fYh0KIigmJJS7k5Hz8dyhZ4c3UQzityExFG6GvMtSs30FBOf4JLAOGqqeIf31OUNzCgjJZLZH3lcwkYQClIqsfZZQerEhKquroMQIwj_8aD9La1f-PapZ0hFxUNSLDm-2QGhvx1svUwnPYRodk48LwOZLYgg-pwSvmG9GGd4Y2Ex3wg_C03PvbZVVVpMhOJMI1t09PrGeqytUrwWH3Wf6ORvpNgWuz7mr8efDQ6wjSAt1mfKnsGS2SLbP07kLBkJGZClY998nXIufIad3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P07OjRla8jrgfYWF33HSK4Mu3iBwixYGU0xAQn2rk0yCoXgNWUClNwiuotCYF8LSBeULh3A5uNMbwEJ7LwJS2UR1loE8l8MAqpfiL3He_m6XaJ5OKHKAtayQXNVQYVmCz5eRIoJBHRyvmi1aIpatlzXu7zoentfj91ay-m-77xAA64Rp3NOi-rtZWLm57GTkcF7U-J3PsQXoC5CWM4MCv7uD3lbzEQ5F6_WQgObvZQsr0Bi4nkX7NvxdZSj1aTO_EoO4JlRWJW3uc67zHhZAmEc0rz063QdcQATXssBizhr3dF8DpBHd-wCG74TYEer-48E6MJgjh0Ka92xRXDFAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=mnVlT1QlLvHHITK_Mk7_8tX0BfVSitZ7ZFmK4WVlyPvpUYmodfOm9ggnbtjPkd4cM8PC3pg_kdff5nI9KPikbfSnZJ2dSC1Uuldf4oAgex-ohJShk6YfVgekcWkn88k-sJSxTP7L2FQg00zWPV6ZgZ26AvC179SEGob-UDnUcWw9jb10LxXxmlHJ9_aAKLdxduAZN_o_d0mAI5PrGj1N7jWCM_veAdYpdsd_P3hznHUp3kuyp0aDq6EnCkHka9roxfqbl-srGIEP2CUVYAa5Eb-HP3wodVT8K1EP7ih6s-HVkiDXkZeqI25B7SFBQeJM89wyIRyLSdkDo3nOxpa-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=mnVlT1QlLvHHITK_Mk7_8tX0BfVSitZ7ZFmK4WVlyPvpUYmodfOm9ggnbtjPkd4cM8PC3pg_kdff5nI9KPikbfSnZJ2dSC1Uuldf4oAgex-ohJShk6YfVgekcWkn88k-sJSxTP7L2FQg00zWPV6ZgZ26AvC179SEGob-UDnUcWw9jb10LxXxmlHJ9_aAKLdxduAZN_o_d0mAI5PrGj1N7jWCM_veAdYpdsd_P3hznHUp3kuyp0aDq6EnCkHka9roxfqbl-srGIEP2CUVYAa5Eb-HP3wodVT8K1EP7ih6s-HVkiDXkZeqI25B7SFBQeJM89wyIRyLSdkDo3nOxpa-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B2nbDIE1MVABMeikZzNJAdjbYCjRpPtwVgao7hDh4qrjf3cYJ_8788iYt_NgRfd_QpB79yHvww7I8SU2rJSdSK1UvzsRveKmyAn020BJCJjxq_Wqjz7tWZurby7hGPXur3KSG9pZAwr1qZoLg4iMEAwR3G8x3Y5BbNfc9md9_Y5RTwAeEgP3Yg1Plr3P0y-vmaie2TNGFJzVfgwqeHxDBBpECrxIqgFudFnIdbBzUUOwRzkmkLoLsnCT6lR4--6ejwntrCtm6J5fGkS0tUj-OpwEo9LC88TsbbYzY6P5uU8OZX1BhHTYmgpF3Ayxp6UxnmQFEI6yQQBaWZYbPnvibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=a3cwxf1Oy_6ZXWOB3L1KrkmZ9CTeqKyPXS1hcuMxUixgX0zLiTEQ9ncXnAv55GNNmBpGRdpHO46aIZWibJbgZi-4v6ch5VxydnxE9veCio_hxbODFi6RXQdBRxpo3UEwiLo8H1gdm8G5To59fnmWCqunCPiInU2puE05g48YCv2ICRj-oVmhxAO74xMXWfpTCGQQJrrXj61dk8HsadqCTC5n_VB-ywdKs_DXjGV8gvhqN092OBfC7nGSwJQrNwhRhyhgs6RoN4p0wPB9qdKb1C8GfdWIoSaDJB7nLz4-oTMD_QCdL7An4DtctEgSra4snYPzMoqeioLTeJh9zWbb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=a3cwxf1Oy_6ZXWOB3L1KrkmZ9CTeqKyPXS1hcuMxUixgX0zLiTEQ9ncXnAv55GNNmBpGRdpHO46aIZWibJbgZi-4v6ch5VxydnxE9veCio_hxbODFi6RXQdBRxpo3UEwiLo8H1gdm8G5To59fnmWCqunCPiInU2puE05g48YCv2ICRj-oVmhxAO74xMXWfpTCGQQJrrXj61dk8HsadqCTC5n_VB-ywdKs_DXjGV8gvhqN092OBfC7nGSwJQrNwhRhyhgs6RoN4p0wPB9qdKb1C8GfdWIoSaDJB7nLz4-oTMD_QCdL7An4DtctEgSra4snYPzMoqeioLTeJh9zWbb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3ENyzUx7AE2QrkVi3bkU6CgzKAUIlem4UIZ5iCDPyVDf3kEpuyyuxuAoKC9ShIEnablnbktaqf3saFtg8AwcdurT-7LV5L6_UbNTk6Tbgp-rpdqeKN_XH2QwTeamrk9qpi8Z162jxBwm9s5eyhZ6p-itSYuNgZSiM8UyXdy1QhFYwI7v9vd5lB5I5y36LKKV_o-L2OURXfDg1G3tOGxZ5Pr_irxsy-ca75dGDGXAf0ZFltUye9LPGTq9uNJ7Se_ViG_L98W-zOZ1bA6KCBVCyL8jqV9NRQVTAUIiMV-FaVedNo1tFj2HyIOnKZiCnR2sUM6EAmYoKyA1gqC9xXluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=u6F3-vKHDidLKf4FXSppIcricCUp1wbNCdLFtwEQwGq99fIU9Kyi2hp_SSshJs41ZLc0IwdMkMBLNS_2lnX6LRjpba-IPG7VOFzqOc5L07cjoqSp2ZJIc4lTjDnqdChUvGhmuAG_prflZro4g_Bqs3IBYdk3J_DMWrYUPJJOVqaGasyTyv3qXpKlNa3S-WRekHaelM-Wfmn493yLMcy28VuDEtDm_7_yOa2j7QTosOIXfYY_quwNYhQCazxDN-4vNrzGNgucWPSdiT0LGsqW0NJMTquA3BGbeEHmEx0685wJf12yLRSXKzedlqJLdLczeu7aSTj7rOAKJkNTURziRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=u6F3-vKHDidLKf4FXSppIcricCUp1wbNCdLFtwEQwGq99fIU9Kyi2hp_SSshJs41ZLc0IwdMkMBLNS_2lnX6LRjpba-IPG7VOFzqOc5L07cjoqSp2ZJIc4lTjDnqdChUvGhmuAG_prflZro4g_Bqs3IBYdk3J_DMWrYUPJJOVqaGasyTyv3qXpKlNa3S-WRekHaelM-Wfmn493yLMcy28VuDEtDm_7_yOa2j7QTosOIXfYY_quwNYhQCazxDN-4vNrzGNgucWPSdiT0LGsqW0NJMTquA3BGbeEHmEx0685wJf12yLRSXKzedlqJLdLczeu7aSTj7rOAKJkNTURziRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=XRqvQy_mLHJb4j8nETT7l3wY_fenV316o2LQ3iSPm9CqiFL6LZ-jgCxDm8PBVOKpk1wMvLAHT8PcTVmXv8ppVXUKOBUlHsl8kgALPlVyyVZdW7lBrrJY7FTw3GNbqzbBhp2T3KRpni8pYS9d67PIgGB3Ofk2RCxQcQa2MoG3JaLKzobbSKyFjzMF2z8pCO_1kPp7jO2XnB4_874Aj0olkBCi-ltllH8AkwYKB0exLxOdlAXU_PLtyXpQBcvcslSPzfr68dH7H035eCxFUI2qYa_YRdIqSxPbXIUYGeRX4MFjdhvg4_Af5C97I_D77HQmVYBFtnVeJ_ea4GjybltL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=XRqvQy_mLHJb4j8nETT7l3wY_fenV316o2LQ3iSPm9CqiFL6LZ-jgCxDm8PBVOKpk1wMvLAHT8PcTVmXv8ppVXUKOBUlHsl8kgALPlVyyVZdW7lBrrJY7FTw3GNbqzbBhp2T3KRpni8pYS9d67PIgGB3Ofk2RCxQcQa2MoG3JaLKzobbSKyFjzMF2z8pCO_1kPp7jO2XnB4_874Aj0olkBCi-ltllH8AkwYKB0exLxOdlAXU_PLtyXpQBcvcslSPzfr68dH7H035eCxFUI2qYa_YRdIqSxPbXIUYGeRX4MFjdhvg4_Af5C97I_D77HQmVYBFtnVeJ_ea4GjybltL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyMBOILWLTA3k0cOj9jNnAFQia6LcR7kSsrBfF6uk5vNGJ2jHXf8MMCR1OMYJuYL9Fs0k7z1J7wRELMAf5USknmaCGsb27uG_xwNR6uVf0TG3P3dCYNNw2b13f1Rfwk0nolIrO7JuaknY6ge2XRq4WC6mBgv59EbmCFR501ULorv3ai9ERNngvGfs48rddkQQEDy3jz4gjpV7XghMBoP4XkG1cp34X-gjE6Rfu8B8YM-rhgFL083iiCkhSRtFUsTr8X6MOEUsQ05oGD5daItn1ihsi2Wwk3ZW82F-4LgvBzno2XUm00Ubl8y-r5aTI_PlUzLp7SVjMRM5PSrLNsGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6s0YssgZkSspmKSGsRlQVHCmAKbeXsFcbnOhGsoPk2MjI1LWpBD-uEkakMn_zQz9RvsVnkVfoclzN5FWLDRcyIZsNluG7ZQFBVNypGYvLnC6ysBxB1l5RaOmTKWHkfvSeQKRkgRpIhXWWtNrB77JUg3HnWdTQEoCIsLUW28WXxVUGXUy670A1melBq4-akASYWPpNtJdAX2WmLtWWK5CkK2Bm1-lFF-OI9oHy5NWwZiBgGM2-LjlpQbYAeCBP_bcTmeH6xAThNzKVzvXG1mjf9Pl00JOfy3b1Wy4X82M2OKOZ1u9RDZrwH43b-y77bZfM-8zjJ5lIqOF3YUmXl9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utNSz9iRMGbPmfIOtFLw4Tq7mdXomvDnCH1JdQWkn938MHHTdz2HqG_ufXlzXsYLyX1XDMLYQGQ-tkIKC5h2XyEtVE3MhAx_Lh4UsvBC0qUm4VPey4Sh_WQI1cOUBxJDeghVltUbmI3GO4zsAOE8zBNAB0vG6-5kbITr1RXJiyam12hGE9AvZFBOzq3IXhkIk6S2kTP5aDbmV1j1DTuPAJZwPYeFkRJQvKom4GoDO-R-xWzKoiGDTCucIHnsjw3ot5GJDipF2B8F7ixCA7jiD9uDJX-ftQCPFIqPijEWl9ubEf7T9pX2cgIYkMD9Q49xzxA4cBxJsqVouZcjWvyKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=rHLqqtvOrO8_LRnnFJMZ6z5Fh7OrQYy_eFCbY-RLRrzTHhcW1zdREwag2eMKo9nUagssJSjGTPvy9ejmZbmicW71bz1HOt3h-NGPa3DrhC_MPnI5-rSYxpiNkRiPVAjHDqQcEtnh8rYVC2IB-mCEz2kVKRRKwl2bbDZ4KdzpGD3LsBHCFNAa_LNzUEiwdQjSodGQFdSzCpRTyBx3igfzq7EogOGlFBK5_2ms060Af75RgOQ7gtnw_hUVQb8IMa-6zfIBsbDHLY8HwgrJAEABhqE6oOM2mz5Fqk_kpk2w3c45eaYyScOXUJBekDeTyo_sTOpOQRY6tQ4N2bYA7r_jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=rHLqqtvOrO8_LRnnFJMZ6z5Fh7OrQYy_eFCbY-RLRrzTHhcW1zdREwag2eMKo9nUagssJSjGTPvy9ejmZbmicW71bz1HOt3h-NGPa3DrhC_MPnI5-rSYxpiNkRiPVAjHDqQcEtnh8rYVC2IB-mCEz2kVKRRKwl2bbDZ4KdzpGD3LsBHCFNAa_LNzUEiwdQjSodGQFdSzCpRTyBx3igfzq7EogOGlFBK5_2ms060Af75RgOQ7gtnw_hUVQb8IMa-6zfIBsbDHLY8HwgrJAEABhqE6oOM2mz5Fqk_kpk2w3c45eaYyScOXUJBekDeTyo_sTOpOQRY6tQ4N2bYA7r_jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=HQMWa_E2d1ccDj0jV2ypVtIk0aG8hVZCQpGtRiT0EhbRZQqzvF3XoF2OGfqoKVsrFCneGDoCd3cWSCMrpu7Lzsnsa2cCgR0J_nwRkSR1Z9xI83TqdcqfPinx3g2SCp_uV3gaCqBAIz-X5kPQ_KR_0eBzts6CDUip2K4E9rekWFkSHc6AZ4LMHIwQO5lcFTo5vicDL4Th_b-hScRAEgoWG2ubEG7L9oOuobF_PCMoLDv8jCkr_ALUor_Qa9GN7eIvDEj2FPWcu_gBdxA0z2mKMu6kVJE48xWyS8MOcNJZdNQgyvizzV0ze1ywt3r7LJlFhr30CzO4X8vZZZcA2XwxzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=HQMWa_E2d1ccDj0jV2ypVtIk0aG8hVZCQpGtRiT0EhbRZQqzvF3XoF2OGfqoKVsrFCneGDoCd3cWSCMrpu7Lzsnsa2cCgR0J_nwRkSR1Z9xI83TqdcqfPinx3g2SCp_uV3gaCqBAIz-X5kPQ_KR_0eBzts6CDUip2K4E9rekWFkSHc6AZ4LMHIwQO5lcFTo5vicDL4Th_b-hScRAEgoWG2ubEG7L9oOuobF_PCMoLDv8jCkr_ALUor_Qa9GN7eIvDEj2FPWcu_gBdxA0z2mKMu6kVJE48xWyS8MOcNJZdNQgyvizzV0ze1ywt3r7LJlFhr30CzO4X8vZZZcA2XwxzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENbnzRy02Xus3YilE4Uz3FnEryQyJ4so4RZJKCZ_TWM5vePqn0a-sBcNhAuk9_7WL4ceyztBBrB6Ua0wVLcDEHhrREu1jGjw1_ZsVsl1hNAnU2Gb5TfoYHvhCY9FpWWFCuA5aeJypwTLVT5meThKVZu5XO_-QOPDQk_fmfcoXN0IlXwgA2VQWop0fyawzjuSpjSt26wEwYuClxWRaZKGyQUeeVwlA4-oNLZSfx_IWk0kOuZpqjG4Tq7v___qz_OzvjyYZs5lcpJjcVp6aGIEkuN6xsACTpSfLZkRcRY5jplVIEckgwft6fTl_araUFA1vOjxEEsPEmEgYKDzKqgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=uEl2CESbLiQkV-JN60H-VI1GiI8wh_U9LhO_Q_iBR5EXfRHHCzr82dqx9CGSPem8gBJGDSJ52lRWUOWDEBwYzxsm1AX3XA1i3-BF9Pi_ShB7d_XyqHTSO0SKFKFnWgZG21UJVwb7dAYuY2XIe967vZMAs4IgvjX_mNlxUMs9RBSJYxXvrgamR44UZejmzsaZ3WYrNfRJiD4e6v1-0nixq5mCQxvaa4ohtsIYZSZbJw2AzIwODsUeloxyGogiAG3IvHq2FnYD_kPk2wyBO7noRRzzKkwf7pvd5xEebj-8aVmBzLGoNrk_wKhRlS5aA9kJrgCATSjYxyFsdZbcqZEA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=uEl2CESbLiQkV-JN60H-VI1GiI8wh_U9LhO_Q_iBR5EXfRHHCzr82dqx9CGSPem8gBJGDSJ52lRWUOWDEBwYzxsm1AX3XA1i3-BF9Pi_ShB7d_XyqHTSO0SKFKFnWgZG21UJVwb7dAYuY2XIe967vZMAs4IgvjX_mNlxUMs9RBSJYxXvrgamR44UZejmzsaZ3WYrNfRJiD4e6v1-0nixq5mCQxvaa4ohtsIYZSZbJw2AzIwODsUeloxyGogiAG3IvHq2FnYD_kPk2wyBO7noRRzzKkwf7pvd5xEebj-8aVmBzLGoNrk_wKhRlS5aA9kJrgCATSjYxyFsdZbcqZEA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srchq5mH81I9eXDeCSIwAen6CLxTfmBHoqiJJpyqDuuIzgDqw80rDX1jeCur7kyPoGkO1vlq_r64zy0n_W9D2gfbxEuILnSh7jXSpBaVmemAeJzkjBTRLOxZFYcbQnxcrvJtj4znQXeaIl5d4RfpS-oadzN0Em72JAi51RP_fyIYxJ_TQfuEV7Pl2gpoYeTok5vKKBjl--9sQC96jAYCWD2yQu4hFNmx02NE5r0hBMhMphZCCPKu8H3ZYehBOmVXo7g0nbwrolAaDmdSL6LCRVFYfH0HgzNeHa1_CcAQAxerU7p1cYxjd6gq0rql2fDsHZ4Bo8aelwD_EW_ORLXyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=GWVcgYsfggt34SUpf7ywhEkVFgu68Bgsl3ZUptIJOpBCLkhW0VwWEEnlFCCA65FzhW-3I0YPCcgOonMEL4IjqpFs2_96KZ51eBXHFtd1f-6CkcHM-9hGWkTrKit8Q4AmuWMN0rTgrvHWaUgQZI7x5n1nsoDTiGbAmM8-NOqLRQN5QmsxzaEvQ1YT0tf3uIsQ1Jm8Nw6GLsyUBrMKJ-wkM-wn8Rt_wtjkMRcWP42oUe4ZI8kLSXsg3cDWTiFQ7hR39-nGO1JDEKNIsytPAileTvovPFlNo5pcC7_X4U_ki04jLudMEa7ZY4AzA14LG1jgdP0xztZzgTJiBQwAoe35ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=GWVcgYsfggt34SUpf7ywhEkVFgu68Bgsl3ZUptIJOpBCLkhW0VwWEEnlFCCA65FzhW-3I0YPCcgOonMEL4IjqpFs2_96KZ51eBXHFtd1f-6CkcHM-9hGWkTrKit8Q4AmuWMN0rTgrvHWaUgQZI7x5n1nsoDTiGbAmM8-NOqLRQN5QmsxzaEvQ1YT0tf3uIsQ1Jm8Nw6GLsyUBrMKJ-wkM-wn8Rt_wtjkMRcWP42oUe4ZI8kLSXsg3cDWTiFQ7hR39-nGO1JDEKNIsytPAileTvovPFlNo5pcC7_X4U_ki04jLudMEa7ZY4AzA14LG1jgdP0xztZzgTJiBQwAoe35ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYB_EkyDpwAK_eaJiX-7KptOqR4tHKnqL0r5Hi-Lfwk-HwZESLlef3pZRQmTirHiwJ0TW2qoQNGq5LjT20lbJMy-43GhIRhulrFBcN3zx-tDfIfmpN7LTcFVtK7NnnfVArVg1PIYs282kZh2AAqrg7pi26YA842yLl_rc5lJV-94IL5L7Em9V4HyibwQ_ApyzaQGnTmVjqIhn2bfcLqPJwjZ2zKt6semRh-dMAvJF14quhmQuaJezE-dQos71g7iocbU8zPBqTu-fTMVdjLPukJOt64UOCO62Ot1GTF9NiMTCX5du9aN6dtKhVMvGEa1ZVrfuAlV46PV6ttzOv7syA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WAVl1pC2ew2mTW4iHPEGVAXZ5MjTRwwLN7boXIYgedV8FfwSGR6NmOtE_HjlufUzME5jQCf6uGMZ1dwPeMAseP6W_DLzhACzJttjfs-LdqaKweqPFmBxxxVdPgo97xtsGzLouorz_v7a40Kc71my446aeYkOz4EnVUdLou7BCBUPe64LN8W88iCfHGrKdHbZsJAyVNswfAK7vwqYUGi5VICiCpcfS2sYYI6PKTtumsU1ZRUdG5-Ri3NXSI1G4acet2dZ1acHhWYH4SWfDiduOAgcSNVbWGJ-27pzJ_Hn830C0mKERNA7tE2TSNQNiPHzxN2PKNZiKxEqkjGRWd4F-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=WAVl1pC2ew2mTW4iHPEGVAXZ5MjTRwwLN7boXIYgedV8FfwSGR6NmOtE_HjlufUzME5jQCf6uGMZ1dwPeMAseP6W_DLzhACzJttjfs-LdqaKweqPFmBxxxVdPgo97xtsGzLouorz_v7a40Kc71my446aeYkOz4EnVUdLou7BCBUPe64LN8W88iCfHGrKdHbZsJAyVNswfAK7vwqYUGi5VICiCpcfS2sYYI6PKTtumsU1ZRUdG5-Ri3NXSI1G4acet2dZ1acHhWYH4SWfDiduOAgcSNVbWGJ-27pzJ_Hn830C0mKERNA7tE2TSNQNiPHzxN2PKNZiKxEqkjGRWd4F-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=TAA0a4x--xlC6cx227J-wlrkSZ5o10mKdVwbkOAvNG8eCxouFT7F4321CIEfcWX2MaZOgTbmzO8CsHHlOzNkE6LdDiMkclaaOsQ6tKYGj2UPD0Vojb8R4Zy2v5NWoSDT-m_w-Dv_gJPiu5QFbbzoloDcNsinx-WwXOXk0cBia_PSAxu5LN_8ozWfTixm90EQ9LPHdk9aA2QiE8u3FqYHcyeVflKDwhR_FKngFYtPlpECg4VvSllphRsuDbgr7vb8-1OZW_pnWNDYnGudYvO_n2NP2uZnN7kgHxbvz7L3dQfDHFQ_sgyIwiwGHwtz_JVF9JeQPsW-MfCBgluV-D01NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=TAA0a4x--xlC6cx227J-wlrkSZ5o10mKdVwbkOAvNG8eCxouFT7F4321CIEfcWX2MaZOgTbmzO8CsHHlOzNkE6LdDiMkclaaOsQ6tKYGj2UPD0Vojb8R4Zy2v5NWoSDT-m_w-Dv_gJPiu5QFbbzoloDcNsinx-WwXOXk0cBia_PSAxu5LN_8ozWfTixm90EQ9LPHdk9aA2QiE8u3FqYHcyeVflKDwhR_FKngFYtPlpECg4VvSllphRsuDbgr7vb8-1OZW_pnWNDYnGudYvO_n2NP2uZnN7kgHxbvz7L3dQfDHFQ_sgyIwiwGHwtz_JVF9JeQPsW-MfCBgluV-D01NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=b6_Mtntm72wxkfPLvZp0tK-x2WLmskuJ2PQB4ArVIF8nU4HJyC7XN9CzCo7kDkuOQOt0PNJRVOFclR-1vFw-szsF7iI4GQp7UpHD_PZ1cRLA2xaSIHRuTN3AglbW5q23X47QD_l1-SbCBu9lyuCNIKUDYai9Wj4__orw4QAeuk7S3s8s6dHackYe7x2k2ukpZ_BZVH7zGWyX4cRcljOjrXNr8rNjXr4rcoxE3LSIp0I_qC-VvDJ7qYC-LKGRjLr3lmgiwym6g9TPz5ruy1TONnUM4Y0a1G4lqPlSxrFIoPScl53gCpfc9wgPeCwJnIObYkfWs-HoknD2HbhLFT9axA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=b6_Mtntm72wxkfPLvZp0tK-x2WLmskuJ2PQB4ArVIF8nU4HJyC7XN9CzCo7kDkuOQOt0PNJRVOFclR-1vFw-szsF7iI4GQp7UpHD_PZ1cRLA2xaSIHRuTN3AglbW5q23X47QD_l1-SbCBu9lyuCNIKUDYai9Wj4__orw4QAeuk7S3s8s6dHackYe7x2k2ukpZ_BZVH7zGWyX4cRcljOjrXNr8rNjXr4rcoxE3LSIp0I_qC-VvDJ7qYC-LKGRjLr3lmgiwym6g9TPz5ruy1TONnUM4Y0a1G4lqPlSxrFIoPScl53gCpfc9wgPeCwJnIObYkfWs-HoknD2HbhLFT9axA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmgXvxNupq-1tqOS3UCPWl92ucz2DfYwmmbqaENxv3gUSDZqq5TezsCZHZQtVIThUZnil1SFDaOouVKupeQPb9yX9oEbIHrn_z1lcD9zvX7Bmny-CVBm-9bi7X0wclwcElX7KavbK8YYZusoFRZ4s4TkMBWg9zeenxhOWsQHf4lkReZPKCvW7RzgjV3sBo8qW5bskd5sN3Snb56VpLUfMf8LTH3tBtECEfu17DS7izpEHyj1hqmp6zi7sPORU9-SyksSrUf9epqrguTfw8A7kC0xcBoNrik7Bhsly0xxZE4L-uLKrBEWDpfBy6lDY7PTVFY_jcq1AKLtXMEnj0LWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky0f9n3WLtLBOmWgz6XQg4I6c11WIzdwDOImkw_GcHkEIfIMhtYMBZRmfXxsduDCrhS8CuagH-MNgPSLfdYbpK8U0UmwAO5uUI7yRbtLO4AfUnv4LKugaeJ29qnsinGCLrZGSv2xv3FSJIDTSDz5fTrhJ-g1oWZIxKqSn_ZwQNLXyjmMoTpoke3nqoPdYNdGrgGVwZEnCWnHEp1mMXMOnjxrdXNEeIkty1-a9JYZK1jLpcJyUxNwLySIz31c1CaoP-FJEnmSDmzBfDOZO9Fmg2F3Y3T6uwYAcQsUCE-06ubDETj-F1eY8_Y8iGAg7mRjyC3rIE4j6OidmT7VQ_bSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otrsWu7P6DY8L7uK6qWZu87bPzaSXiEsCzjP7hvqFDWyV8jh-coTuciQI485VjroQXbVinXY9kHgy7xBkpEOyLXrDN3eJ_NeDZhB_woULOhnW-oja6YVdRxdQStSOrrvYM8QK2s1Vs8AyWCmzWO1sglldJkv006M5uWOuq0AhELGGgtffdDaMF7WjZiW6NfJCmIIFBiHNIeA0Y31-pgu6xpQrzzXunbK2oaXvYEr6OP8lQPqnRx2DudrOqyi-Myoj-agN0-JwP-xf1ZjJhJ_nFIy6-2WmckeukpmbGCON2RIdcak7uMOMY7yqIqqUf3Vt7lCz5G48S6Ehari1HvHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=cZiJpZCjHBaO9l8m2dRCHREj3vVGkfEtcgRQBO89lN6vSx4d72kila39f-VEiwuazt4eJoK5BWNgvvLi0LFIdQxk1r2IQi2Zj3c1Ck7ahE70qkrotWt7Bs_iTKdM4wfhxYvUUPx-t658kk7quTMIRsH-by1y7lleM_rF3CCq-dY7O7vzm9CfBOS6QbG1_8WYgX0e3LGMRyKOvhSdjuFoXBLSkfid2ceyhVxObG3uuLQTzdxD6YkDpmzG12qkuPGNQDqwTZkogU6wxS_rZsqlwvoF8ncV1NIdUNsKq6iFN8FfpWFZCroJtak6xg5wmNC4t8_8q1O0Gf0ihBWDQ-HaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=cZiJpZCjHBaO9l8m2dRCHREj3vVGkfEtcgRQBO89lN6vSx4d72kila39f-VEiwuazt4eJoK5BWNgvvLi0LFIdQxk1r2IQi2Zj3c1Ck7ahE70qkrotWt7Bs_iTKdM4wfhxYvUUPx-t658kk7quTMIRsH-by1y7lleM_rF3CCq-dY7O7vzm9CfBOS6QbG1_8WYgX0e3LGMRyKOvhSdjuFoXBLSkfid2ceyhVxObG3uuLQTzdxD6YkDpmzG12qkuPGNQDqwTZkogU6wxS_rZsqlwvoF8ncV1NIdUNsKq6iFN8FfpWFZCroJtak6xg5wmNC4t8_8q1O0Gf0ihBWDQ-HaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKj1nXHhhnWO_ei57Vm7WVv0SNd9pdxfNvuUEB9wOVsZL3zx4KiIKbKiRmCaNDbuZEPP4vO2Vr5Wdp7bLClKv3s6WSQx1fPKPIPGwje5piWSlwFSrNlMZ-Vo4vzxu-cUTvDBRpAr-slGw7RvGiCqMU8hpYdLZy7AqCydh8-N95ZBzZngg5IQB5Ya7PpebpQTx7sQijfqg6EzkTx51sZN5C12vxzM0160hg0uYZT1XDf25SPDkJSO0aitoWHNXitcC1BWM-JnGAlRV5A04EYcDcEOLUnt9sLYQis0L5lIBY6k0hhlkiE_i_8VW2a7C4OrocKQSbM5iCgut97XE5KDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=IoM6e7qUqcixBmMyEZH64wioyiYYfYrJP8WCAjaQGgE_WPPZDsHMo5tpwh1fILUK4UHig2PO8yZCsaY5XmERByX7EMqeEPGLd_ki_MC9Uewa4gdvmLYeTMbRbkBUt-LRmQs8wrRSQewxAnsBoCfyE6KAIKCUtteMhYGK8v4HAqsE50s13Qx6IBUqUzEoUMWttzD0Y4awLxDoVNjvIORP02PAK0qVIbhMMPpLYd-bEj1g1QdCiiNo3h31QkZuANxpeuCiGJXs6LxaeukD6OSC3yj0jP4ielshLpFeJZjMUNyxECoBI6cb4U0ejIYEyIgbVtCMGbJS5SjUthBo9R9OuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=IoM6e7qUqcixBmMyEZH64wioyiYYfYrJP8WCAjaQGgE_WPPZDsHMo5tpwh1fILUK4UHig2PO8yZCsaY5XmERByX7EMqeEPGLd_ki_MC9Uewa4gdvmLYeTMbRbkBUt-LRmQs8wrRSQewxAnsBoCfyE6KAIKCUtteMhYGK8v4HAqsE50s13Qx6IBUqUzEoUMWttzD0Y4awLxDoVNjvIORP02PAK0qVIbhMMPpLYd-bEj1g1QdCiiNo3h31QkZuANxpeuCiGJXs6LxaeukD6OSC3yj0jP4ielshLpFeJZjMUNyxECoBI6cb4U0ejIYEyIgbVtCMGbJS5SjUthBo9R9OuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvGvaVVqvefXAezmA_AvW0aa8KI1PU0v-uS0iozKi3Oh2xRtVODiyaRFoPUEAL48ePktWaASxphOy1ak9sD0y786-TsA5aZbNejG7nxuczv_nSBrfZJXJgmI7zwJ0-ncDxXsDU6iOFDNGyaXyhtR50GX8GFk4GNC90PwjkyP9rjeC310tXEdcQDLDSlgvBlPiWLCmF76juMo1JqJjBOOt_v8eL7XUOzUdXGEBJnuxpZyTehrFs6qcmDm_uYPvyc6YkdOkovA_0uPoXzu2csMhY9bqEdG9iDEmBOjqwhnI_frFGk44huMpL01BvArvQgO1fWlavjyKMTOErAeW3k1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=pWn1ruP_AbZ25KIc-EdqsjyYkGmzHHnAgKuUKKFDpAJPpgRhOjRWUXXArx4g--2bB1e2eJRWD40BMUT2Rob2p3wrp0XGnKaFeF5gqboLefAoyd_W0bVz99oQmlOtxJ4HaFFzEJYfoY-MABOvEeLAODl1tBI_Vy1C8dH2O86z-uyjBRhqJBcCLhAUbaXdv53F5A_7URRznNq4BaW0gb26q-tVsy1zdqBoFWWXPxRsViB_iyEHjEQaFVcVLZGbu7cbC42D5ycJTEPwFOdOxidFJMVHFWxDv_EeotCYrTu_Ho4IqUvcg0XBQZ1CgEpf-g1Wy8DNmRb-j-FOIDU_D78T1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=pWn1ruP_AbZ25KIc-EdqsjyYkGmzHHnAgKuUKKFDpAJPpgRhOjRWUXXArx4g--2bB1e2eJRWD40BMUT2Rob2p3wrp0XGnKaFeF5gqboLefAoyd_W0bVz99oQmlOtxJ4HaFFzEJYfoY-MABOvEeLAODl1tBI_Vy1C8dH2O86z-uyjBRhqJBcCLhAUbaXdv53F5A_7URRznNq4BaW0gb26q-tVsy1zdqBoFWWXPxRsViB_iyEHjEQaFVcVLZGbu7cbC42D5ycJTEPwFOdOxidFJMVHFWxDv_EeotCYrTu_Ho4IqUvcg0XBQZ1CgEpf-g1Wy8DNmRb-j-FOIDU_D78T1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9QoepBp27H42bB5BTJSXZ-XFF7FvYk3-fJjSrMTsgw4f9rMNga0C3CeaSCZgyJaYOUZWQfEtsNWqMoDGzigPSWcVExyfLuE-Ao6O8dlANhysr2xkUjGdEe32Hl13IazbNsYuFAfw-jKWTXvjGieBCB7JiF7tkiIYnSHM5abMUK2Y0hSihXMMrZe2BbgZb4jrGVRncMbJNUQlYSztvjXs7JBBxyXDUeKKQJZ_CTg2iKmfGoLrymSfL_MfvOGiqVkX8CFaul3u-jbN22Q2j6uEbk652Ei22nR_8UqW1OD9qLyZhBp884BR2Qm-Y-d4rMBrB-_6VIT3-x_PtX3jRA1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDmA_CuzuRT5Ojg1Lw5WftQFrcDCfM1hE_CyaKY7uZBfKvVYF0fEfRU09koyirOM-AJBj6EtzdvXrimR69x4rZVkPe4xYIxhik9vh4PhaqW_OS-0Xo_uHQwDQZI4WCLQWBvst3WCJCovNmMZVTx7IMhdIkLZoOyZLleW3BNr5-8Dkq-1LoDjgAfckbbDQDwmTuxbOcGZcmj9nKvuJryl4-VgcrJs0ld_C9GnvreqdAaFhDoznPqxOogBQGkzSFbPHMNST3T0zLCJFt1MA9ZTzSBlD5rPHaCmGDpNsbodrnX-OkSU9VJsxZAdqUzGihRp9RWFbOjpKrrCM4YueLRSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW7LHJ0hwUn_dZFAUJyKYfG1XiyrIO0D8gOzyxdFKpL0y1Puj9efxzslDW9TanMppDb2JH1n7t6GKlNePIVrIUU-oVskQDz9ieke89HRyN3nsH0Kzv821iSJOkZ3NWAW0r8xz5wHLJ6fQnM8fjtNnpEWMCpGf2BHJwNw_dCN70UuN6lALtPnQhD6lSmMJZyTK14ykIChC_wfUIUWtDL46DoU32rVdvDxhceQ6C8-xdIGebod9Ljdrwvi-fBNDt29x__m0DwDqlTB2NE53mB-oAqMAsOOLBvkTee87009HhRAL6fk6U0nXwrYiqvMDiQ9MLQamsgTc90PsM-19JVokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oURbte8Vo_ZGcHs7IEX82pxs0xE7Q1V4_Xa2ElnsoEj6XHrjY_unf4Xof3gtIkG_mziQNEtOYkpb_2vi8KVhUaaaQ5130HLotC7dhSjY9Kec9ykLzzzJe6OL-fpmnJTeFYQpRACyz2rZmYBK00MUwd5vULzCYGZnJChv2CXY0JM9p8doDiZW71xvjAsGnzeXXU_qu9ldw_mi_QFQmF6BCv9zZvnNQeuQ7AV2zfGV7hYpn05iJ6vlAU_8hUiUxLsQMlGhu8LS6cJAxUk9hJiFo_y8zX9KjUhCa_tq3OcFIfdzCXoW84DoYlrVlWRGk1nzHdjOhN6W2RIUGYov61_vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2_csqzRYqXIHx3_sNAg19YTCX27jHgUNDHVaoHStAZdkcM3PjMuHYEvZ9BgxaJKSIuHRVZpd6IUKD8nbkCwzvhgLCHAqcg8vuRXzBeg1euE82vGEOaPW-sMI9AayECcRpuoR74aG7T8CeKekYCYihLO_71Mg4bzwDdjFsvHAgqqjgnLH3VbzUDU_GWyy1h0_Q0nEdreI7IZpanUEPmb5KLdxBAVFpzS5GSNAE2IudYjswpm3gwgQODg2Ft5PlK5QowJEz16jA-29zX-7S3uSlkNywo3_3zcScOws8yEHqPqS2v3i6e0HltzZAQEKIYxrSYQv_VzvzpZ9fnjNV4kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=a-BGVxwxe15Q4eltpjMvwYlLY8leY0SoynKxvllTO0ee9MdRFDadMQIa7oZOxRRnYAu-4kNOCTKZ-yZjIRo1Ll8hBtvQBpcan-GdKEJOCyWbUWzkjWnLbbZgbQwh9Hbj54yrFbzNt2fBNkwfLXGwB0jg_QiqG4puiNH5Pr1-bpKRBWmNCX6w_ZoBU9lsveKHNNTTX4r6c1vaUfoh5aucZNYXNIP1yvdY3CQ8xH19usiAJ9-HUd9GyTS2BAjX2nU8TbCwa893sdv42vRieYPIsvpu9x4xDGLRRipXEg6OXv53Do2dGIzt2MToC1Uby3ufQDtdUeaje_wU_D66RHmN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=a-BGVxwxe15Q4eltpjMvwYlLY8leY0SoynKxvllTO0ee9MdRFDadMQIa7oZOxRRnYAu-4kNOCTKZ-yZjIRo1Ll8hBtvQBpcan-GdKEJOCyWbUWzkjWnLbbZgbQwh9Hbj54yrFbzNt2fBNkwfLXGwB0jg_QiqG4puiNH5Pr1-bpKRBWmNCX6w_ZoBU9lsveKHNNTTX4r6c1vaUfoh5aucZNYXNIP1yvdY3CQ8xH19usiAJ9-HUd9GyTS2BAjX2nU8TbCwa893sdv42vRieYPIsvpu9x4xDGLRRipXEg6OXv53Do2dGIzt2MToC1Uby3ufQDtdUeaje_wU_D66RHmN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=JH_95AK7wzeDBfI4B4eLtuVXMLjTQXUT_1_r0A126Nz0TYANYba2W0NYWAjjB6QlrXjopX5p_3H2k0YCGbMOPHHNfY4Dee0UyzlRTXIIVu8MvGunBaEUo3Y1BdEO5XOeKvvATUrU5jjM_XR9WKY3CtIUT5cxrDQI3RYCCq6diosK9Z6Wx-08dmF2w4_kHiZXkk8jU2MimWqFGG6Gp22754wy8cuteXdc9hVKar3LO5bls0LoN2ukjgBNQUfJId6UWKmnDUoYpfLf2caX56sSDsZ2NKySWDyxbF7bpqMuEB9-CXFEiA06wl_vKVUpEV5imsanEXUJxpGUQyBzS-fCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=JH_95AK7wzeDBfI4B4eLtuVXMLjTQXUT_1_r0A126Nz0TYANYba2W0NYWAjjB6QlrXjopX5p_3H2k0YCGbMOPHHNfY4Dee0UyzlRTXIIVu8MvGunBaEUo3Y1BdEO5XOeKvvATUrU5jjM_XR9WKY3CtIUT5cxrDQI3RYCCq6diosK9Z6Wx-08dmF2w4_kHiZXkk8jU2MimWqFGG6Gp22754wy8cuteXdc9hVKar3LO5bls0LoN2ukjgBNQUfJId6UWKmnDUoYpfLf2caX56sSDsZ2NKySWDyxbF7bpqMuEB9-CXFEiA06wl_vKVUpEV5imsanEXUJxpGUQyBzS-fCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=cpvdWvuhOveKWcvhfcP1PTzrIb2lXcEtWoH7ZSllcDm-CFNmM7LVRqhi9N29r_EfKrtUZQA-EVVlGy4DMV_MuRXKSLTTF83xPfRil-R_ufMKLnN1ZiN73ZmELFXJMTRp4C-TmGdttwtQ2gbOd5bjvoFx-ihBAM96Vz_sRvyXnoTYqtYihNskVYnILA9fgFBJwyZvo4xQ6O5Y06nUyjuk82XmCYefO4MF06zCKBevVdhrVtk3P_qMr4kS9usc-k6jwgQVe6sYxuC0ExaO9s9q8gMmGVn_ArwakB_PCBKc7xMONurpI2_vMWae8cWmFzuw9XIr6e6GVOMV9DjncOyT7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=cpvdWvuhOveKWcvhfcP1PTzrIb2lXcEtWoH7ZSllcDm-CFNmM7LVRqhi9N29r_EfKrtUZQA-EVVlGy4DMV_MuRXKSLTTF83xPfRil-R_ufMKLnN1ZiN73ZmELFXJMTRp4C-TmGdttwtQ2gbOd5bjvoFx-ihBAM96Vz_sRvyXnoTYqtYihNskVYnILA9fgFBJwyZvo4xQ6O5Y06nUyjuk82XmCYefO4MF06zCKBevVdhrVtk3P_qMr4kS9usc-k6jwgQVe6sYxuC0ExaO9s9q8gMmGVn_ArwakB_PCBKc7xMONurpI2_vMWae8cWmFzuw9XIr6e6GVOMV9DjncOyT7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
