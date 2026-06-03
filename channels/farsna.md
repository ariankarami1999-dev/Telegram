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
<img src="https://cdn4.telesco.pe/file/H9Ahly5Wc1DSwAFNpKHCakUUdubgpiEP12LWYJhN2XKCg6hzHkmahxrLCyp6mpp72K5IUdQFS0GMJHmNsFLDyVdFYmAsMfR_2J19TscXGg7v9sT-J2JVG16KraT-Fv1GMriWm_rmvOFeOwCVdJjy2yL7MzNcIrLcnPIzwg6pQdq_xvilZkc56SPIpgkzqQATE0HVcuyZ670vPAHJNxLhMhvzUZBgpx8AXe0AP-vc9OFlfrvmX9IKPB4BDQA-QRyr3HcCS3aPl8neAvq_9q7kclzFKCM4mWvJ-Nv8gNpf840FSQ1a_ewNWJbQ3MnyXoEO22CVEAGmUnuBIYbf6Qj-Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-439649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n335sI4gqzfYDnCKC1esxYlSNH_ZQ2Xg3bylWAWBbIsmCCYKe3D5FrFhel7eas1K7ZUlCcPiqYSNLHDZM7ZuMqKmOBZxBBSyOTLpzGf8VbnFyX9MFIvslHSnGMhKmmRGhjGtL5PbMP_CWALb0p80wMcU4GO7zqTA_S-xC34mRllBYFbY5lkUf1SnZQym2ycYf6SLjnv4YAgtp64we9dS_cYxOPfYhyo8aDOyR8GsZVPdZPxq64cXbZ5fctuN5veV-M1qGESiwtea7NGTvjz3UT1h0pLLlTcHAyUuPuaImcv4n1cAFsxzY0ibJGlV9wFgmZRUPi16_CrCkGMY1PvWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری خبرنگار…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/439649" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc6cb7158.mp4?token=LIS6WM2Tuodd6KsGyvXVZFepbwWOiHtovKcC9Ao7uy73xcQ6Mz5Gme-PlTkyZnS9Oosg9-Y4UdH6tkfElq1JSjyrielsa6woaFbYRq2k8MI2hIUIYYhWsFCp_DXy9tYUE24QZH0pBySz75LmciUunHfZ5M5mLosk77c5OUcveWzrDr-rKN3DsfZwMzgbhTbl_sHSxFSC7NXCcwhA88u_gL4hJFu8ZxMs7gMOYRviC8TGBhOPUgp9pDULuLCjs8Enlddji35SdWIAkReYdkm-LpgxSBkDuRLRP0X5xaVSqQ5xMoM72cGyb2EGRpYCNNHbqRXA8HY1oewwRcsmH6xv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc6cb7158.mp4?token=LIS6WM2Tuodd6KsGyvXVZFepbwWOiHtovKcC9Ao7uy73xcQ6Mz5Gme-PlTkyZnS9Oosg9-Y4UdH6tkfElq1JSjyrielsa6woaFbYRq2k8MI2hIUIYYhWsFCp_DXy9tYUE24QZH0pBySz75LmciUunHfZ5M5mLosk77c5OUcveWzrDr-rKN3DsfZwMzgbhTbl_sHSxFSC7NXCcwhA88u_gL4hJFu8ZxMs7gMOYRviC8TGBhOPUgp9pDULuLCjs8Enlddji35SdWIAkReYdkm-LpgxSBkDuRLRP0X5xaVSqQ5xMoM72cGyb2EGRpYCNNHbqRXA8HY1oewwRcsmH6xv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما هم به این مهمانی دعوتید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/439648" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCKa3BWpUV0xcQSNcAyvGtYAF-qke5YKlTW-tm58iTERg996dgggK6mpFQ9Li8BlD4ukTmBO0IlFNOq-ofRaVEWf91Lh9So7_EwI6LrebkmBqIfpSRRDc3j2UKfC3VX071BBFjRY7IvM08KWYhHly-zij8lqiTT7nEwjuMaBlkV_hd4cIplPOOTMUn9EuzFSLk_CirqD7nhWD8L4J80sO-nPW9EtMNJX9iXtqbmsBokY39790soFcJZ_dof6njFLl4FVuDvTP_gTRPO0QR4myGfUxVviumFYBhkU9pG4u9HvsfAB59Z3nT6KyV--lri3RqSJhQc34Fboq6RWfeha6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی‌سازی بی‌حجابی؛ این‌بار در آپارات
🔹
تصاویری که منجر به فیلتر یوتیوب شد حالا از آپارات منتشر می‌شود. یک برنامه پادکستی مدت‌هاست با بی‌حجابی و پوشش ناهنجار تولید محتوا می‌کند.
🔹
در بخش‌هایی از این برنامه، مهمانان زن بدون حجاب حضور دارند.
🔹
کارشناسان می‌گویند «حتی یوتیوب هم در کشورهای مختلف مطابق با قانون کشور مقصد فعالیت می‌کند و جلوی پخش برخی برنامه‌ها را می‌گیرد و دلیل فیلترینگ آن عدم پذیرش قوانین ایران است، در این شرایط بی قانونی در پلتفرمی مثل آپارات که مورد اعتماد خانواده‌های ایرانی است تنها فرهنگ ایرانی را دارای خدشه می‌کند.»
🔹
نظارت بر تولید محتوا و ارزش‌گذاری آثار داخلی می‌تواند این مشکل را برطرف کند؛ مشابه سازوکار «سند تسهیم» که از طریق ارزش‌گذاری محتوا و پرداخت هزینه به تولیدکنندگان، نظارت ایجابی و انگیزشی را تقویت کند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/439647" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXB-7IhycSczxFJqZ4PZAjYN-prDyTBz72Ov8SSwP41rGhJcSqGOu4fvQ-KOE6LZy_RrgziuHej4eSrOjaYA9tkbLpWrGQv976U4EBCU1k7qr4yQrRxivPceVm7fu9aVICxWAox5wlj6u-pijP6I8ReplXm3hLC_9zbcNxltpx0TuSZPP0Y2UovveJoq6tfivpl9xPFcuegnoLgQ6JMpKRfdmyTQgqThkqVd7SU44ubbvrz9kvC_6-CHNLfTPyZWDqN5QXbQVtnfyidpgg42_-506EemInd98jC9aU6lkw8xmV7sbFwagtRyjZgRnxYSb5JBwExZqhr7FHsAf0WxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw1VStLLX-4zRal_yzDgH5EWtThELTrOT30U0tSCmdU65ykbo3YQR71vRCPdxMEwucn_63VgFYN7r7dcYgzeB2fjQYQ3n9X0xLeES0M5MRedDDX2cuzt9mTDDJua0iqP9FPNluoUx7qVeLjkvFouu6A-jmJplcyZDIVUxHnOXc3OMHnwiC80LuLqUqz2_p7jET1fMtw0ZOXYMVX7EIs6jA-_EYbfEyref1I-CqjIpimJJxdTo-SItM-uJqm30fEWwq0peOcFDn2vUruXyoGc9Ta8uCFDjKzYAGwof4eTUL3vFqw7XJsaFw0pmDl5V83nnlvjvoW_6FsPhW9qp4qQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmUhqsGvI7AtmP4ET-sXdaUfA5JaUO3zOceMbp0q5LmMYsUkre3Fn4lG80ikNtDLTMaUWA-qtBtaPk2sC4IAwJQBI72tPuldrymXuLcRkcm8cmcmYKxHTWP-H9SECXjFQG9dRRzS5DbnnTC8VzhgaDel_B1RFmrj5hazBzLMQRRz9xsV2qcGR0S86cwkqkFFsEIaD9aP1r-p-i-REoxi0AoiI_PfoSYkwscxQc_xXKP_xcYgdPVxOW6oJ4jIa0HXUoEsQ6eYjV3XOsO3XGL8Pm3ON1-KgAiidHDfvGZZ-2ui1s4GCz_SvvNXrJ7qN31heN3GAH-KseXvXQvpqsArFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPz9tu4WyakUyeGH_2wgiFlAxUXDN8giY5cA-I_x6dzV_SmybmtQPSH8Y_jEtCGRT0yXUTV0Q2kBEpSCA_-i-XLL-1X7cQNy-0W-s74o9n1zmZanj_8jCht3ah2ZovNw-BEOC0H9haSdJBqxUGX7tEeOgZ7jbHB8TP5Cek7zZR1eKylA4TmiRY0jDRyjCshiuKVumsZMiSTH9eGEi_PH8BW0Zi3n30bDe0gQyGGxGunhFSUcKjwEOfMH2A8Dm77W_jqMaBOBVW7lrs6JWMD0wvGwHdt-OpHas1gH29ne5wPFKO3m0OO_dqQUd8l2aiY-pgBibZXxFw9LHHjfkPanwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Poh-ctLT1K21u1AY9JSTpNMm2k4io8QspdypBkZySsme0CTHndA86QFtqPL6ybPZQY6-IsiaTl2_0uZ4oQJ1AT9SWxqKR1npucm3zRA9fXznaK2Ghj05S_ZnUrzBI8lQJIXoNqQKpTefyekSpJCeLo_FiQkLrnar2LgYYe2s7pDL9Tmgt0V_spBwOLqbUxacSb7jpC9eeJp3SL0XprvvxDa3IrXAKTfzEBZ4iE582tItZ0GdV0JtTknW7A5diDf3OiK4HZmd_CQtlFEbImHEuEBSYhOxSDCYrjyNkZDa0JA90SqDzvo-MrRMrhgj-8uYp_3QHDPFBtdOHL8I7pzorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f29bFIeneNAohFty9-WDByB3ns3N6s0ZAcu8Uedzp0td7F-yywZOh8h4VuB6qIHWAiosb1eajfIbreFXmuscIkeDAzsBLYb2nGVqX5nWRctOCwioqgE3u4H4_9P9ohhsczNIuKhHZe-KGxOeeX4o2cVahZjgaLcDxgdGCY-NdzPcwJCYDuOIXc9PsPxy0WKXdj6OThahlUwum6fIM22j9ExRD0KgcI1kJjujcPZAYG_1scE_hpMsTNfaEIX0N2z4C1vjKqUopR4QTAdzzgY5RBiT_it-HMm5KlPsjMNIOXyX51Pgs6LRIhrrnNrHWSKp2CxHID680XKvpZ-Bc_zZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScfNGcXK-oYTJAbycgbtVkS65EARu5hf-sX1qkCpx0ghQHilksDGN4cCN4KpClfu6lqNz9JrndroqYNTJuuEBydu1K8NKWhU7hRYpHXlvDhrpTOhhfEU_NCewV9IA_tXPq_Zk5oY4Juz7UI_4-nzH6vp0L94RJO7mHo1h8xHdn_S7UAgeJP5YEkfUCr7GBDt9ed2qv3uLuy9DAVDw_8_3PtoeWGJWfa85fKH0u5pbziv0cpPW6ZoEeBVdBA0szv8tPJsUnPKxeeGNHUdoRcEDNCf1SGry6LqFemqKudP8KouCAyAtXMkGsU7197VprWRncew629OSRBRnaH-1utgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdvDjRYyo5kLZOlboCNfeYQ9c76KSV2RNMNvqS9-RQyt_SbIYP1sc9eLbbw8V3Lx9tBJD_mPSp2WicLx3vRwb2SD0JtI0iRE8mqatiQ-0OGZft7xL9306Wq-10aLqWGWPDdS9jf0BwJ0_qSTGPr96Cr_w6vvCREWmqzfnxKpscxV9uWw7aMqd-H3Ssi9KIhWJlURmnwVf1-dD_wnFl_spsDU1QTGi5SrWpjtfuA372A5inNxPaqQtFPW4BgwE0qkFZ0oT1-vKL6W3XIb_6HuN2OJC8637NQ4scb_axCwvjmkVAK_3V2hDKB9JInKMaFiFbacGDO6Nk9RaiqMO62QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQo0apfNZzqwnAy75k79K62iAEyM6ww5WUQpoZF2VB7DJnweVhj8tSCT-ssbDjBuupeKqGFZdiQtBgp3eX54Snf8Aw_EdOZVQ8ioUq16qEMqSRFhTY-UCePLTLf4uApdGnTEQp7j89qzlAT03I2Nxhk9qgLP1g5Dvo4CUFPwR7r8j9UPuqvOMhI9rTRkYy8LevR17WNtRi5qU3-U1_CDDDB07Mj11Vj9KZ_CVu-d31NwrPOHeYc7ZvXdAyeYpuqN8pKyP0x46_TazMoLoTOkpSDh1R1yR6m2iVBizVHOq0upquZOZPcOOVjgC8BHG_O8YApDRdsBvMTmqenBOq5OcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هوش مصنوعی شهدا را در مهمانی ۱۰ کیلومتری غدیر به تصویر کشید
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/439638" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
سازمان هواپیمایی کویت: حمله به فرودگاه کویت چند زخمی داشته و خسارات شدیدی به تاسیسات فرودگاه وارد کرده است. @Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/439637" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/439636" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سپاه: مقاومت تا اخراج بیگانگان از غرب آسیا ادامه خواهد یافت
🔹
بیانیهٔ سپاه به‌مناسبت گرامیداشت سالروز رحلت امام خمینی(ره) و قیام ۱۵ خرداد: حضور مردم در خیابان‌ها پشتیبان میدان رزم، سنگر دیپلماسی عامل ضروری رقم‌خوردن پیروزی کامل و نهایی است.
🔹
ایرانیان هرگز تسلیم واژه‌سازی‌ها و دستاوردسازی‌های دروغین دشمن نخواهند شد.
🔹
دشمن ناگزیر به پذیرش قواعد جدیدی است که ملت ایران و نیروهای مسلح بر میدان تحمیل کرده‌اند؛ به‌ویژه در عرصهٔ مدیریت و کنترل هوشمند تنگهٔ هرمز.
🔹
مقاومت تا نابودی کامل توطئه‌های استکباری، اخراج بیگانگان از غرب آسیا و آزادی قدس شریف با نابودی رژیم صهیونیستی، مقتدرانه ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/439635" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439634">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df7790086.mp4?token=OqXCPEDLwysk2SihtJG5iLUA0oa0wTmL745G7axpNMG2nsnL7L37dWDWVQPxlx18RIy8yg_JmP4nSB8MUTfPflBeTsRSZ5PEezJRAAdD3pgl5zc-IIsp6VHEgQ_dB0dX1hdjNzvci623zbpXkF_ZqDpgg5-z0qk11sTjV4L5qeSn682-at629ufpDAe_AfAYQwn0UHjS17mqfoevP0hXQVmA9uF-GqCU7V4zHuVRdRkMhPdqiZpX4q6VP8dcgom5Wi4678Nd0gQM48ffQhGqXlDd7TcOAl_1BS6X74gme9pP6Bi14WWevnHKDYeZrlf0frF2KCf4U_Iy2JcBF07IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df7790086.mp4?token=OqXCPEDLwysk2SihtJG5iLUA0oa0wTmL745G7axpNMG2nsnL7L37dWDWVQPxlx18RIy8yg_JmP4nSB8MUTfPflBeTsRSZ5PEezJRAAdD3pgl5zc-IIsp6VHEgQ_dB0dX1hdjNzvci623zbpXkF_ZqDpgg5-z0qk11sTjV4L5qeSn682-at629ufpDAe_AfAYQwn0UHjS17mqfoevP0hXQVmA9uF-GqCU7V4zHuVRdRkMhPdqiZpX4q6VP8dcgom5Wi4678Nd0gQM48ffQhGqXlDd7TcOAl_1BS6X74gme9pP6Bi14WWevnHKDYeZrlf0frF2KCf4U_Iy2JcBF07IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا اسرائیل سال‌ها به‌دنبال تسخیر «قلعه الشقیف» بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/439634" target="_blank">📅 13:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMfp9ERa2itxkLAjvCTlWpd-d4kYn01os_4BitNV5P6k13Bv_Tzifcb-vNlF4sqneY58rRaE2JLFdwpmc3VPKpAUXWQxyRk-2JrCAQY8esxKy14rc7HOKcdoORuUYf-O7BLxyi0Jks_ZtYEnnFyYomrkWXUm6MAmgiamnnvPugODoUN7q6TD9IwF9aAQZD1m71mfc541P19Ggglt3xqEHNvj_RDkkOTyU-yWEc5xHs1weo7yB0HximW2rwrSU90uPnFnMzgnhH4KQXR8PmNAJgEqjG12n3Btgj1K38ae34F4vMcm3DzW2vYJKrqUUxtPJi5qCNO5vuTti51G7i3aTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
پیشگامی بانک صادرات ایران در بازسازی اکوسیستم دانش‌بنیان؛ حمایت راهبردی از آموزش عالی و پیوند دانشگاه، صنعت و اقتصاد در دوران پساجنگ/ تأکید قربان اسکندری بر توسعه آموزش عالی در دوران پساجنگ با رویکرد حمایت بانکی از اقتصاد دانش‌بنیان و فناوری
🔹
در راستای حمایت بانکی از اقتصاد دانش‌بنیان و فناوری و با هدف تسریع بازگشت دانش، پژوهش و فناوری به چرخه‌های اقتصادی، بانک صادرات ایران اقدامات راهبردی خود برای بازسازی مراکز علمی آسیب‌دیده در جنگ رمضان را پیگیری می‌کند. این رویکرد، ضمن جلوگیری از توقف فرآیندهای آموزش عالی، زمینه‌ساز تقویت پیوند دانشگاه و صنعت در دوران پساجنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/439633" target="_blank">📅 13:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439632">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-text">🔻
«بیمه زندگی و سرمایه‌گذاری پروژه محور
#بیمه_البرز
»
•
💰
۴۰٪ نرخ سود قطعی در سررسید
•
🗓️
مدت قرارداد کوتاه: فقط یک‌ساله- معاف از هرگونه مالیات
•
🔒
امنیت بالای سرمایه‌گذاری با پشتوانه بیمه البرز
🔗
خرید کاملاً آنلاین و سریع در کمتر از ۵ دقیقه:
👇
👇
👇
lifeapp.alborzinsurance.ir
نیاز به مشاوره دارید؟
🏢
مراجعه حضوری به شعب و نمایندگی‌های بیمه البرز در سراسر کشور
📞
تماس با خط ویژه: ۱۵۷۴</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/439632" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/439631" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sjw9kcN3ne3LdPn3di-YpeMgtjJ8ONKunjzxKjCzpDVFacnzPZ_ousYbDrf7VBYBbE62bFciyJKW2UvGFj5l6oAAecPJUEGslz83GX_DQJHYQtiTU44plBq_fMo2FWYJ3qUeSNGKZnAAWVroc04d9Nq2OESW-Oeog6Bji9Rzu4xyWId2NmzJ28vJo3OhjrfOh0bmjEST9gaSd_XozGx63KkatYYjOeGgYJFoRJVZuEiHK_fPByCf7uBOe6ODREo64YoEhbsMf1R9wjjeBcxeQ5zS0Fbev7Pn8XX38PwOcAEF7f0-RDNsy99JWFvYpdg-JnaQJy47UyDZS_m08yIoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۴ هزار واحدی به ۴ میلیون و ۳۵۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/439630" target="_blank">📅 13:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56b293a99.mp4?token=PSnVn6vPKWW51Sed99vDx2oR_J4uQTrjgSK8DyW7BQAnyW3VomYWWZ2v5PMqIClKRVYW-R-N8aiLR0JQRtzf88CQmj9mz8k7czcIB8UAfIFeezm4w2Gc_emdMJ17jGIbj-og8x6iieG0EvmY9zFq9e0nvJyKsii5E9OwqBxu6ewD2N-by69zMvS-fzVziy_h_LYNgHuYL5PmB08CIu4HO2XZujlN5FMkHNaVqFd89VntYV6OLF1qqJnJJRL2Y8m_39EwZeXjq9jlKmaVphLDVWgnwIFNEdeQHkswY3lJM9Fgsb_yFUV-3tVB6AMAN3ijXGqDS_2bviAVZIDkAv2-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56b293a99.mp4?token=PSnVn6vPKWW51Sed99vDx2oR_J4uQTrjgSK8DyW7BQAnyW3VomYWWZ2v5PMqIClKRVYW-R-N8aiLR0JQRtzf88CQmj9mz8k7czcIB8UAfIFeezm4w2Gc_emdMJ17jGIbj-og8x6iieG0EvmY9zFq9e0nvJyKsii5E9OwqBxu6ewD2N-by69zMvS-fzVziy_h_LYNgHuYL5PmB08CIu4HO2XZujlN5FMkHNaVqFd89VntYV6OLF1qqJnJJRL2Y8m_39EwZeXjq9jlKmaVphLDVWgnwIFNEdeQHkswY3lJM9Fgsb_yFUV-3tVB6AMAN3ijXGqDS_2bviAVZIDkAv2-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: نباید با عنوان «نظارت» بر سر راه تولید مانع ایجاد کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/439629" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439628">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9SgACtrBk_RPQVDl82-vG1SicwFVJO96BMFbBxItSBF4eB1NdAz1zg4NdnNHn1Z6-uhgbYuI_FqgbkBkwApJfSACBO7AXv2PsqrPnJJ1rUpXdIbDaWUdOqIwDQZdayyCkQTedZj8N_hn4NuMMYdW3xCKYabrHhcHaht2Ia3JI8Tab0qai0zzbxjW4AwHIITwr-IpOPKaMtn-Z2UVWPr7VrGIDATNIeWWZb7f6JB3kRzJJKYebhk_9H-EcfiMA6BJFWMYfwYWHYfGa1tXISywABjUQUG3VmEkHvrYdgn1-CdvmwcYs4qQ0hlWObYaE3x1rawHunAQuHwg5Ymw3bAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ستادکل نیروهای مسلح و قرارگاه خاتم‌‌: نخواهیم گذاشت دشمن به آرزوهای شیطانی خود برسد
🔹
بیانیهٔ ستادکل نیروهای مسلح و قرارگاه خاتم به‌مناسب سالگرد ارتحال امام خمینی(ره) و قیام ۱۵ خرداد: ملت شریف و مقاوم ایران، در سالگرد ارتحال امام خمینی(ره)، فقدان قائد شهید…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/439628" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439627">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbf6rmL4b4Xu91u1KcyiaQksl4u5yC83gmS3z3jNyXDT9vZw8lNtz7wgIqDybKF-vPCpzzP8w3JGlSmU-2-7sB3YlqoOLgLJBLGxaM7vef_YEF8VCCU7XmTXjUIkqCrpo71sl_jrPyCR6wnk2oqHEaibJPIhXC3ufxNvI484onLf--duLvBALQ_fRjrI7X41BjBfYT8dpYz07ZoEmgJCgLdFOMeqFpngMpb3NiGoT0exSzvD-kuj73ukv2yNGK6Jqg-JBza0fMi-IzXmhCOpv2oWY6VcmEHDtOHWl0HoEjeeWctFD_9bfGFszBgmdni1x08_cRm-omdkRIuMxmSwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اینک پرچم های زرد برافراشته خواهد شد
🔹
در تمام نقاط مختلف مهمانی ۱۰ کیلومتری تهران و مهمانی‌های کیلومتری تمام استان‌ها به احترام لبنان پرچم‌های زرد توسط مردم برافراشته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/439627" target="_blank">📅 12:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439626">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4759031cd.mp4?token=qYZS1wJP7Ba0B6xVA77mT-nSOrX5wtsh7Pf4tdQJf8hIXdYRgQZu1VeYiLsCEeteR3t_B9gQfbjVY_GUMEH-mUxZAQock_ubZe3BaKKedTTBa7x7PNS6soxHfE9jTYa9O6D8bPoJdOpZSZjPXyy7o4OgHn0rQzdcMlKTcRf59JMLXkymsblpmsVCiIS5RBes5r3dkDj9NnZTFLdq2fzR3lCSUhnudIQHG3P3Vjz0KPI2SRJG3VxkrQY5RoeYkN--faTIUgIzYRA8qYHhhvlDQD6otc7jAiGjyutQXevby6zaQ7PPLB0dL2TTcNnjKFtgSGSP25kyVYaMztw9ncusnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4759031cd.mp4?token=qYZS1wJP7Ba0B6xVA77mT-nSOrX5wtsh7Pf4tdQJf8hIXdYRgQZu1VeYiLsCEeteR3t_B9gQfbjVY_GUMEH-mUxZAQock_ubZe3BaKKedTTBa7x7PNS6soxHfE9jTYa9O6D8bPoJdOpZSZjPXyy7o4OgHn0rQzdcMlKTcRf59JMLXkymsblpmsVCiIS5RBes5r3dkDj9NnZTFLdq2fzR3lCSUhnudIQHG3P3Vjz0KPI2SRJG3VxkrQY5RoeYkN--faTIUgIzYRA8qYHhhvlDQD6otc7jAiGjyutQXevby6zaQ7PPLB0dL2TTcNnjKFtgSGSP25kyVYaMztw9ncusnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار معروفی: شهید پاکپور تا حل مشکلات مردم پای کار بود
🔹
معاون فرهنگی سپاه: یکی از ویژگی‌های بارز شهید پاکپور، مردم‌داری بود.
🔹
شهید پاکپور تنها یک فرمانده نظامی نبود که صرفاً در جایگاه فرماندهی به صدور دستور اکتفا کند، بلکه با همۀ وجود در میان مردم حضور…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/439626" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439625">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVQtFbNgstAqoUUI3WjpEoIbGbwBF4l6hEL7AFK2YcjZFAfXw83tgIwfTt0N5F8NXHIrcuhlbE7fRWPSxwj160hscZlkv5ktp5l5kjq397Joo2IOmO9j6-7mVpNr_nN5BtUQHyPdk9-upJV0xYMo22glbBrAsJDyiB90ZlIwOZJfWZIUtVh1HjDUznPNYL_8lxoArnYwysk22eK-DAHw6aDLHQI_6GKJ_A765ZFhRBUXOd69d-s1YwemGVs7DXn5JY8Bpe15zeT6jpT99TvKZmhyxd0RB3U1fdglvvpKolIW_spfqKY9s0HhlPpsegi5Hz0_YwkVsQl6tuCiLsZxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی(ع) فخر ایرانیان
🔹
به‌مناسبت عید سعید غدیر دیوارنگارهٔ «علی(ع) فخر ایرانیان» در میدان ولیعصر(عج) رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/439625" target="_blank">📅 12:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439624">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l40WfJ0z1Qkhk8qHTCpYCughVcyP7aJfMSAJeD5Mip3S2g3vhs8mV1AQFP2_eL6pIKse70lSQ-Vi0wEWiBN2L41bRK2Ue0Wn52NRPLz8uUmu52RbWRuy5tdB7SesvXyViRzKk6S4dXiKUPBT0al-QiCwTkqjrh8VpqxC5X8NvXz0wRF-wY0rFnpBqp_URmFIGrEbGgkSQ7gDw81NeiB4DqPmXD0iSMSAUqS9jrTfkkZAaVhjxDTOXGr-W-lueIFrRfJwLs7YouWsuOMfC4M3a0a1HOhPfdwS1ZHByQ8IHXiw4oIapJy2T1PRPJH_P7GjCXX9CQkwmxa4n9ONdONIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است
🔹
‏نه در مذاکره و نه‌ در روند آتش‌بس اجازهٔ زیاده‌خواهی به آمریکا را نخواهیم‌ داد. پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است. تاریخ به عقب باز نمی‌گردد و متجاوز به سرعت تنبیه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/439624" target="_blank">📅 12:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1026a8aeac.mp4?token=rJ2NR-9WOJXWBbJ_y8C3GAEWp6cTruPYBx-B_sK1ph66RFOk2scpYAcUuk0wBpu6DknEGuG7lHp2PYVk5MsQP_vQzFDokKgaqVrLq_ataW6vY6fYukqONcuBQsLITdPKclN6aK-mg5HzgXnifmGqOqY1yxqIUzeXrs-GMyyn-izBuUYXAkb-nbxVyFviey3UfEOQiktB13lF2PG1A6tJqEg0eyDYwM_XNnwBOPtgY6zZynEe15T1UK5O5QMGhoNw6Y_gFf0OVwRugGdsK75qjCFHX79BKcwrxAe0waiMF07VY5woXxymjv3c0lf5pRz-Mo4fw01PSdmHJjX0CiwcwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1026a8aeac.mp4?token=rJ2NR-9WOJXWBbJ_y8C3GAEWp6cTruPYBx-B_sK1ph66RFOk2scpYAcUuk0wBpu6DknEGuG7lHp2PYVk5MsQP_vQzFDokKgaqVrLq_ataW6vY6fYukqONcuBQsLITdPKclN6aK-mg5HzgXnifmGqOqY1yxqIUzeXrs-GMyyn-izBuUYXAkb-nbxVyFviey3UfEOQiktB13lF2PG1A6tJqEg0eyDYwM_XNnwBOPtgY6zZynEe15T1UK5O5QMGhoNw6Y_gFf0OVwRugGdsK75qjCFHX79BKcwrxAe0waiMF07VY5woXxymjv3c0lf5pRz-Mo4fw01PSdmHJjX0CiwcwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیکزاد: نام ایران به‌خاطر ایستادگی مقابل آمریکا در تاریخ خواهد ماند
🔹
قطعاً در تاریخ نوشته خواهد شد که کشوری به نام جمهوری اسلامی ایران بود که مورد حملۀ دولت نامرد آمریکا به ریاست‌جمهوری ترامپ و رژیم کودک‌کش صهیونیستی قرار گرفت.
🔹
علی‌رغم اینکه آنها تصور…</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/439623" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدور کیفرخواست پروندۀ شهادت شهید بخشیان
🔹
دادستان همدان:  شهید محمدجواد بخشیان در هجدهم دی امسال در جریان فتنۀ آمریکایی‌صهیونیستی در شهر همدان و هنگام اجرای مأموریت و درحالی که آشوبگران را دعوت به صلح و آرامش می‌کرد به شهادت رسید.
🔹
با اقدامات سریع و دقیق…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/439622" target="_blank">📅 12:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ستادکل نیروهای مسلح و قرارگاه خاتم‌‌: نخواهیم گذاشت دشمن به آرزوهای شیطانی خود برسد
🔹
بیانیهٔ ستادکل نیروهای مسلح و قرارگاه خاتم به‌مناسب سالگرد ارتحال امام خمینی(ره) و قیام ۱۵ خرداد: ملت شریف و مقاوم ایران، در سالگرد ارتحال امام خمینی(ره)، فقدان قائد شهید عظیم‌الشأن و شهدای مظلوم خود را در کنار پیوند عمیق میان ایمان، بصیرت و ایستادگی در برابر استکبار جهانی تجربه می‌کند.
🔹
جنگ‌افروزی اخیر آمریکا و رژیم صهیونیستی، چهرهٔ واقعی مدعیان دروغین حقوق بشر را برای جهانیان آشکار کرد که شهادت ۱۶۸ کودک مظلوم و بی‌گناه مدرسهٔ میناب یکی از صدها جنایات آن‌ها می‌باشد.
🔹
ملت ایران در برابر تهدید و تجاوز نه‌تنها عقب‌نشینی نمی‌کند، بلکه با اتحاد و ایمان، مسیر عزت را بیش از هر زمان ادامه می‌دهد.
🔹
نیروهای مسلح همگام با ملت و تحت رهبری فرمانده معظم کل قوا از آرمان‌های انقلاب و کیان کشور تا پای جان دفاع خواهند کرد و نخواهند گذاشت دشمن کینه‌توز به آرزوهای شیطانی خود رسیده و خون امام شهید و سایر شهدای والامقام پایمال گردد.
🔹
دشمنان آمریکایی و صهیونیستی در برابر ارادهٔ الهی نیروهای مسلح و امت بصیر و آگاه، چاره‌ای جز تسلیم نخواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/439621" target="_blank">📅 11:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8XWt2QVFAA8p4tS1ZHd4a3Sl36I0b41EGWV7jsd2tSOS-yUMCezxSyWvvVrXRCYuxfmbxOf9cTNFDsaCFsp7NAK7V1GefraSHyufLjVPQ5lz0c_XLaiLXOrWNrHRRBydoiXJZ6xuLFMukAlDumjZ1kT7go3Ozm5Z6PtyWo1grci0dgqzn5NE7G_ku7IJvrFuQTwvddcgfD8JwpCmcgNSu0TU8mt1rZJFiiMmLXF8-I8HMAsPn6mstbx5pNMSHeeqe_AvY1bzv_X4Xj-sGcAofV7sJcZKjfr6Pz5i4grSjWQMGhkXSqg6cprZxWQeu_euIvWUpQZ8My1r7RhxuEDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نیکزاد: امور کشور از جمله مذاکرات با اشراف رهبر انقلاب پیش می‌رود
🔹
منطق ما این است که زبان دیپلماسی باید ذیل فرمایشات و اذن رهبر معظم انقلاب طبق بند ۵ اصل ۱۱۰ قانون اساسی باشد که از اختیارات ایشان به‌عنوان ولی فقیه است.  @Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/439620" target="_blank">📅 11:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439619">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nibAIAC4o6CyrZm4G3eztsPoluW9w_UuxjnDbWmivOSwPNvm0hqVFL0tgAigIkDER8AYMZbtLj81pHIy0sAw-hONUwRBZnrawRuqkvP18Avz27n0J80fq3LPD2gdakFrcSJNOMRlSYAH6sa4Ko-hH3GEz_RvNkthmR5nz1JpqQBNHWn-f4jZkAHQVJSZwJ2o517AhaiHoAyx_sR3HzUXn9Mo407E7IYW4p7PsAeVRH4fK46Fiv827BsbAzvpmapruYdtlkrHBYbtMykmQ3O_2hrZLNqsFl9lrpFjk-b1dl9dWJooFVU0GgxyIBmzhfwc_xWKmM12FaTYb3F__DCpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت هیئت‌رئیسۀ مجلس با برگزاری رسمی جلسات صحن
🔹
گودرزی: هیئت‌رئیسۀ مجلس، تصمیم مثبت و موافق خود را برای برگزاری جلسات به‌صورت رسمی و فعال‌سازی چرخۀ قانون‌گذاری اتخاذ کرده است.
🔹
مسیر هماهنگی‌ها و مقدمات لازم در حال انجام است و به‌زودی جلسات رسمی صحن همچون…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/439619" target="_blank">📅 11:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439618">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIaX_wo-lVVvJPhPZH0xUB9PUHP25HGqhJYlbJ-9Tm9AeW4Pl7pPFd3JGA_eylTmevLkVxIN-Z0Qn6uHK00Xe5wQiNv6C2VfnnacNUJEQj2S2kHYisozzAeOWimmJzaTjIBJtIQvLW7K72mF17A193FnAP1_29mo0uOXbGrd7xI0xe8fjaKGgqcIChZ5g7vRYMEvlP86JfTZV4eVvsiHHQKA6ArMNFxig_86c_ieJGgENj4GMNSCbv0jWQZjARdzeISFgUeJwE3AGSW1h6_XUFpMADavwGB1OsinEiHV4Jm7W8EVlxsSTxSfUFEmf7yVIsxbmiPh5USLMcKRUG44aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفت
🔹
سپاه پاسداران: در اواخر شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز مورد اصابت پرتابۀ هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/439618" target="_blank">📅 11:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439617">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc6258e9b.mp4?token=QpNLF4vfDNBlUd0Vdvs3tHC2m9GoxPQOdvB0MBDFDZzJfG04FSYKa05qu-TxaAE9qg_qTRz_Pgzf-tOxCjM1rZsHh3b-I21apCtuAy5f459w5cM_BhGDp1iw3xAuP5G6B7cOOMR9JWI7qOmaxojNFx_lXpurhR6uKcIpdrJglvMXxcIMaCd-vSjMbx-r02np6q68hI52wJaqSkJBm_yHEtuxIRV480_mF5qJBCuKEUUttAx903xEMMQNdLBDSrEq5rlenp6xJ5WB1fKqxuRxk-_Uz9KtPbOWiBdhrs4OgDyLahyi8T8p3OLbwq4Jeo162xA8649s1NyCpl7zUSawWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc6258e9b.mp4?token=QpNLF4vfDNBlUd0Vdvs3tHC2m9GoxPQOdvB0MBDFDZzJfG04FSYKa05qu-TxaAE9qg_qTRz_Pgzf-tOxCjM1rZsHh3b-I21apCtuAy5f459w5cM_BhGDp1iw3xAuP5G6B7cOOMR9JWI7qOmaxojNFx_lXpurhR6uKcIpdrJglvMXxcIMaCd-vSjMbx-r02np6q68hI52wJaqSkJBm_yHEtuxIRV480_mF5qJBCuKEUUttAx903xEMMQNdLBDSrEq5rlenp6xJ5WB1fKqxuRxk-_Uz9KtPbOWiBdhrs4OgDyLahyi8T8p3OLbwq4Jeo162xA8649s1NyCpl7zUSawWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: تاریخ باید بداند رهبر شهید ما در پناهگاه نبود
🔹
نایب‌رئیس مجلس: این یک واقعیت تاریخی است و باید در تاریخ بماند که حتی خواص تصور نمی‌کردند حضرت آقا در منزل خود به‌همراه خانواده‌شان از جمله نوه، داماد، دختر و عروسشان به شهادت برسند.
🔹
حتی به من گفتند…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439617" target="_blank">📅 11:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439616">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5ed11f6c.mp4?token=fFfQebaG5iv1uaG92jPCxwyic2FXcqceT_jDTl68PEeUjn2xYZAh1ptTAdzZ0255cPVfSuYWD1D4yNXUuWYtKZVw4-cPqKrUEgAQ-N236xXOCseZkC0s64E7zK0GQG84_QlEKwLHaFPkd-TCctPF-JIRMR7_PdnJcrhAMm8FMbIEM4tOC7e3g1VKJr9E5KmtC12LWT7TRvHWEdxR_BaOS1wG5nmhykGsLKXzHOuSO3T20C_S9O09HvLnkQOLiby90twwG25a3iyndHha4P8amZZyYACAqcCb5LIsgK8U9riKzraxaAdf09ZHaSG4cajA3HAHm6olFmYpgdSHXg5Xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5ed11f6c.mp4?token=fFfQebaG5iv1uaG92jPCxwyic2FXcqceT_jDTl68PEeUjn2xYZAh1ptTAdzZ0255cPVfSuYWD1D4yNXUuWYtKZVw4-cPqKrUEgAQ-N236xXOCseZkC0s64E7zK0GQG84_QlEKwLHaFPkd-TCctPF-JIRMR7_PdnJcrhAMm8FMbIEM4tOC7e3g1VKJr9E5KmtC12LWT7TRvHWEdxR_BaOS1wG5nmhykGsLKXzHOuSO3T20C_S9O09HvLnkQOLiby90twwG25a3iyndHha4P8amZZyYACAqcCb5LIsgK8U9riKzraxaAdf09ZHaSG4cajA3HAHm6olFmYpgdSHXg5Xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: تاریخ باید بداند رهبر شهید ما در پناهگاه نبود
🔹
نایب‌رئیس
مجلس: این یک واقعیت تاریخی است و باید در تاریخ بماند که حتی خواص تصور نمی‌کردند حضرت آقا در منزل خود به‌همراه خانواده‌شان از جمله نوه، داماد، دختر و عروسشان به شهادت برسند.
🔹
حتی به من گفتند موشک‌هایی که محل بیت را مورد اصابت قرار داد سنگرشکن نبود بلکه موشک‌های کروز بوده است.
🔹
دنیا باید این را بداند که رهبر ما در زیرزمین یا پناهگاه نبود بلکه در حال رسیدگی به امور روزمره و جاری بوده اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/439616" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E54DYMjDm9mGifRB72fFJRX1stWp28IwTyCMGu-mocjWvrbJF8RVLHzHKEw3nHCi6RMSEYi_RByqi0oF77iPMQf2Uwu9_CNRPLFaUefIbO8ankFqdD7KcPPE3UhzKL_T8WDXWJiK90KzHVGSujg5GbF1IQHKNJRYvSTfUcAonlcEXzwvOltWog3zD6_GOe_WAaGIt4etHz9c8N-4gmfwLh7GpuG3rYmAgVIu77x2B7FGBCVRmg4eaZKJQ7MGPjRrjAQh799r9QCTRuPYWoMqo2Gu9eEgvLFVQnRN_xUjxjQkl94PjkpNeLiBPDk4BQXQ7DyabuSG4VRfoz0f420f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6QL7mMyj617ae4mJFM2ub2hvLj4f3jltMLS_N7jxWhfc2oRVTQXdwqYqzDIZW6hiNHfvH-NmDw7-TI9j6SN9HigJIir6ATK3l_HXFU93c0Pn5V19CX5yPrYvNHw9wjjPYO8lKq9jGMn43gyFLLoDAugon6nUWPbNjlcSSMrlDVrCU5PW7klRKyoaLDIxqVj-Mv4OQrmyHgEeUIQZJFfow64QiQsg1rs01iYeH1H0v2otfnXxOT_JkL_9oJ4sD_-DfwvFonUi3daUVkmfKzqHbNQu_gOuQbnC7cjw1-k7C3Ou4lw90nHYsciU_U-HEd787AabAXq3TM6Idxg_zpUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMxHtaCIXD01VsIGRMD-IqHyPBov6CSu9QNVvXYZ34e14vLWsmkCtGMT84QGOcpzjkdntD5PxAjTr5EP1lq-0MU6Sfm5qRNPylkopiKMOKUUZ178K6jl0RXLtS_Dq3VcJ26hSc7oTUfEfrHbcBhzOzgOdIdkMnspfqtsDB6Q7s86jVepkiQelyd6poPDc-7qFfpeWkADypavQiReyMi7qoKc6elXjwaZ3sIRMv5vbv_wUI4flk3yzjNMmnx3z-xP9Hn2S-3_D0Ix8HAi4-91zxy0cUl-7HBULPp_kLgSv2DeyrJ9KVaKWJI3zFRGUC3RmqgtRkkwLuuFTQGPc86brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTP1fsCn5l-AMO7smtPzghlRTX2suPVRam_0wTWFVe2rdAkMiiWr4xKd8wNjqudi8ag0t2fhz5mfagVGeJPDlwigxA-tIAlEKOtQOzsIedoevKQzOeWUV-6o3t1lxVeQGmllb4SXgLqSwKg2cuvCX_UlKKwPw93uFcIW7BEFYCgdKN6Ij7Qv4lOViSdhr6T1L4S5eu1mGlKdEVj6IY6gD9tZsdxuWDN5GeTnP3F4c1Z4hMFL0DGAIiGbckOyuSrbsXfRnKvbG2_c7o1cyHjgtb81DbQ0t2jpKTmns0fUTEAFZFPEVZyLDGk7cFeRMgyActu0bLzhtUvUE4pRucUjSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دولت به‌دنبال ابلاغ صرف بخشنامه نیست
🔹
دولت به‌دنبال ابلاغ صرف بخشنامه نیست، بلکه تلاش دارد از طریق اقناع، گفت‌وگو و ایجاد تفاهم میان دستگاه‌ها، زمینۀ اجرای مؤثر سیاست‌های اصلاحی را فراهم کند.
🔹
هر میزان که بتوانیم بهره‌وری را در بخش‌های مختلف افزایش دهیم، اقتصاد کشور در برابر فشارهای خارجی و محدودیت‌های بین‌المللی مقاوم‌تر و تحریم‌ناپذیرتر خواهد شد.
🔹
جلسۀ شورای هماهنگی دولت و دانشگاه در حوزۀ مدیریت بحران آب به ریاست رئیس‌جمهور و جمعی از مسئولان دستگاه‌های اجرایی و دانشگاهی برگزار و احکام اجرایی ۳۲ راهبرد مدیریت بحران آب به دستگاه‌های مسئول ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/439612" target="_blank">📅 11:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyRBuUxssCzZ4qbspwVk7iLZxPv7l9BmursQ2f61ffuNpjY6eCNkdgjJHs5Abkh4CGSDTXKJn1HLmy1FENQBSu042-xQVwgJuQarlh7hrttOIi3MOQasalUkE_TvHFx4F75PeGT_cpeLjv3p8mhi03AE4Bkx_-tpkXIqyEfYkSqdZBZjDjrZCTVIdGKGcO_ybgR0w3MA_lQzWw-laQu7MzE_Ms9b03409pkX5aD5YHEh9mEazGods860rCCnLtJkm3wlMXC0VPMZGh1-EBhBZL_DrFNH_nknJ14cq9nM32n9m0S1HVinyXCPNo6Ih351f6DrpRkOMt_o9VcnKrS0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuNV4O6zl1vmrrP1zeJQ1Bbj7MK5rFQaQbl2ArhZTWT7JgMfVEgYNNmlv5Z7zbgC_f_3LZieyz9-ImPvKke59OeeruZXKGfbzZt3g6KjIRYrL1FW6bXrl6PuYZ0QDApMN2XwRFp0q1pD7XrDgcOYIJ23Ojtcm_kcfPraEfAM59S9l-yE82O4xh8D2BLwxJBiiG3cE1XUPI6PJ5sbiJ_8ZTMWm89wsFNvl63moZxTijgc-MUkkDmLh_1dcNGlGh0qAG0RH3X_UPIPHi2p5572Yf06eo7CFz2-A0gUFHvz8Xy9Ae0eIUfYfRR9QcK9EZAonYPZcp43gvJ9NExIo5gMEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار فرمانده قرارگاه خاتم‌الانبیا با خانوادۀ شهیدان نصیرزاده و دره‌باغی
🔹
سرلشکر خلبان علی عبداللهی با حضور در منزل سرلشکر شهید نصیرزاده وزیر فقید دفاع و سرلشکر شهید دره‌باغی معاون شهید آماد و پشتیبانی صنعتی ستاد کل نیروهای مسلح این دو شهید را اسوۀ شجاعت،…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/439610" target="_blank">📅 11:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwHvp_f5ctdEgb70bd1mFyWgTs0NnGE5Gmuy0SknGLFm1697pq9XAz_ARlp26lpguaKAfS9CEMFt3t2duBHtoIFy74sv9M2esNQy6iGOOLLL1eXwHLcyIpWBERTWp8KMDatjn_ZY5cXVCm9P7S5AhwmQ55QXEEkVLYxfSKqIX8tARRkOK2ZVmsXx1pLrfDEzAUoW41Pqq5B73QjFk76aM_lgug5SMWSfpSTe3HS7v_Pa-wjCl9rMONbZG4Xpqgo_O1Q6mXv2cPT6zmX6y2k-X-66y04-tQ8uXL887NDtPyjeXYlinRHz8D7vsH--A77MJl_FNuXTbYom8dujSlcSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان هفتهٔ طوفانی در انتظار تهرانی‌ها
🔹
براساس تازه‌ترین داده‌های هواشناسی، از بعدازظهر امروز تا اواخر روز جمعه پایتخت و شهرهای اطراف آن شاهد وزش بادهای شدید و خیزش گردوخاک خواهند بود.
🔹
در روز پنجشنبه با افزایش ناپایداری جوی، در بعضی ساعات با تشدید وزش باد و بارش پراکندهٔ باران همراه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/439609" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=n4emXvsFDkhBcszIRhEGMpjxHFqQad15BziT8GBo4GRni5iL8sLvaeDOZ72EY6LDUD6fyCubfBYYlYF4eEt4Xbqv8UtxghSJo9ozo2zf726v1FqhSj-Z1bnzOWFwP3iiwyt2fWbGfKaJhyl_s6gpDyk9BBNVEbSPWN6-0YTme8PAJogOBP4dJi0FWp5DW5U2dOhmuw__uLJshugjZdaDIsgMlux1MZSk4oMwVuOHsprmGRMFPRXI8zByPveFh161oGxoxM4-bM8DLV0evjzkCUCxV1KE8WTIOU7CvbFI3s8oYTQQjtYNxGRJ04AXMGWJXTtro-nHXzILCuUZBZ0F1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=n4emXvsFDkhBcszIRhEGMpjxHFqQad15BziT8GBo4GRni5iL8sLvaeDOZ72EY6LDUD6fyCubfBYYlYF4eEt4Xbqv8UtxghSJo9ozo2zf726v1FqhSj-Z1bnzOWFwP3iiwyt2fWbGfKaJhyl_s6gpDyk9BBNVEbSPWN6-0YTme8PAJogOBP4dJi0FWp5DW5U2dOhmuw__uLJshugjZdaDIsgMlux1MZSk4oMwVuOHsprmGRMFPRXI8zByPveFh161oGxoxM4-bM8DLV0evjzkCUCxV1KE8WTIOU7CvbFI3s8oYTQQjtYNxGRJ04AXMGWJXTtro-nHXzILCuUZBZ0F1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ اوکراین به سن‌پترزبورگ همزمان با حضور نمایندگان ۱۳۰ کشور در این شهر
🔹
درحالی‌که نشست «مجمع اقتصادی بین‌المللی سن‌پترزبورگ» از امروز با حضور پوتین برگزار می‌شود، ترمینال نفتی این شهر هدف حملهٔ پهپادی قرار گرفت.
🔹
منابع اوکراینی گزارش کرده‌اند که این حمله همزمان با آغاز نشست ۴ روزهٔ مجمع اقتصادی بین‌المللی سن‌پترزبورگ بود که نمایندگان تجاری و دولتی ۱۳۰ کشور در آن حضور دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/439607" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5667dea2.mp4?token=ffCYOC0mRKRhlS26HkEZOpnhuN7_mFViZFKBbHDD6XW3reWas42bYzA06cFjFhM67OtBzqNTDjI2cPIGtLZwoz4_LLrQAmXP_MsWK9dfMC0PlUgN4ca_m4B2BdTycWyR6DM9uhnMVPAlQVlRFY36p8iLSAFgdtD1ZOWXAeL9R8qnC3PbzGwn1u4Rc8QjS-EQCreZxqpz4Z-X7oegYUdWpoviU26Ao3T5o6AEaO16PtP5tWFKvLAxX9wxKoRfVT_VQZ2B9P8obyknw0Z55DijUvXBLXCzOUUS5gMPJLwmpqPvMU2uUDlawgliqQArdMPn7xEOy3B3vqp0E38ndlJGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5667dea2.mp4?token=ffCYOC0mRKRhlS26HkEZOpnhuN7_mFViZFKBbHDD6XW3reWas42bYzA06cFjFhM67OtBzqNTDjI2cPIGtLZwoz4_LLrQAmXP_MsWK9dfMC0PlUgN4ca_m4B2BdTycWyR6DM9uhnMVPAlQVlRFY36p8iLSAFgdtD1ZOWXAeL9R8qnC3PbzGwn1u4Rc8QjS-EQCreZxqpz4Z-X7oegYUdWpoviU26Ao3T5o6AEaO16PtP5tWFKvLAxX9wxKoRfVT_VQZ2B9P8obyknw0Z55DijUvXBLXCzOUUS5gMPJLwmpqPvMU2uUDlawgliqQArdMPn7xEOy3B3vqp0E38ndlJGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مردم در میدان انقلاب
🔸
مقاومت مسیر روشن ماست
🔸
لبنان همیشه پاره ی تن ماست  @Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/439606" target="_blank">📅 11:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439605">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f300d528.mp4?token=jVi9rxkPfofcyLphBuKKqwjaUgk8wFQ2pCSwHiI9x5vTSBKRfA3aEiiomEmqsIApI51omINsGL4XqZI8dBkagaR7gDHRnO6vZvHlPWVSV7I6SWou4MhCxrqDrYvrbpISWaHEDyMU3cWOVeX2z_VBfHla7q0yvbz4xkYTQS_VBY2Q7X-LEgftXcEODHwpUO5BVunAxnpyeSxhV_7IOkf9T1n88VGtyPUEc9yy0tVBZ3EpRcdzHAm89rB5NEe_nl4ljWp5bYiMExtuasP041UXc5piwvIcus3E4jB7fVrSdUfvnInMpHggQNZkNdFumZhcONXjyjkvRZsbAQ6QGGNahS8RFYuPhyeDQ3yEcWsmaqlxh_qkWGnetAtIRar5VXFt9AlDQTAd_V7hSDmjGxffeaaIcvwNqsE7xXJ_WPdIyd8BXVLnQdMO679L-LsLrRhZWgQ4YFgIIyYvUuh_1htoD_xDfpuPuk_qCwZKnmC6ze-QYHRaw6Ma-KuvTf7DXmBb37iNRbeCH5dgCP5x2L7LuPZk8X10K-Obnikg7dyzHR-HoYz0ifRV3q8F9pMvTg5H-9_vzP9dSMLWkNbBPRGlOFpPzKKEMRkRZmpJI6hMuNDWZEVxO7munb1s4NZAp8QKdtMbP04OsIipy3dTi4BlKp-KbO4TKG-7tw_wDyvQFtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f300d528.mp4?token=jVi9rxkPfofcyLphBuKKqwjaUgk8wFQ2pCSwHiI9x5vTSBKRfA3aEiiomEmqsIApI51omINsGL4XqZI8dBkagaR7gDHRnO6vZvHlPWVSV7I6SWou4MhCxrqDrYvrbpISWaHEDyMU3cWOVeX2z_VBfHla7q0yvbz4xkYTQS_VBY2Q7X-LEgftXcEODHwpUO5BVunAxnpyeSxhV_7IOkf9T1n88VGtyPUEc9yy0tVBZ3EpRcdzHAm89rB5NEe_nl4ljWp5bYiMExtuasP041UXc5piwvIcus3E4jB7fVrSdUfvnInMpHggQNZkNdFumZhcONXjyjkvRZsbAQ6QGGNahS8RFYuPhyeDQ3yEcWsmaqlxh_qkWGnetAtIRar5VXFt9AlDQTAd_V7hSDmjGxffeaaIcvwNqsE7xXJ_WPdIyd8BXVLnQdMO679L-LsLrRhZWgQ4YFgIIyYvUuh_1htoD_xDfpuPuk_qCwZKnmC6ze-QYHRaw6Ma-KuvTf7DXmBb37iNRbeCH5dgCP5x2L7LuPZk8X10K-Obnikg7dyzHR-HoYz0ifRV3q8F9pMvTg5H-9_vzP9dSMLWkNbBPRGlOFpPzKKEMRkRZmpJI6hMuNDWZEVxO7munb1s4NZAp8QKdtMbP04OsIipy3dTi4BlKp-KbO4TKG-7tw_wDyvQFtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف صریح اپوزیسیون به پایان رضا پهلوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/439605" target="_blank">📅 11:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439604">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLe-2j9G_eVyrykNIBevuFz2EeJWCuEnOmkMo5vo27FL9TKjqA30VXCfBZAFllryyGq_c-xYE_VM0m5wIiSFhK2ftOC3BBjARrRZrPqYQjG1m4QoTwqZO6DorpMKaEmEluCP7B11wriDasUKNwZGNylR8CYEQW6FxcCkYTAQ7Sa2-kPhMWFH3l5Jz4AK-irhqFrw_0iHKrkPzJTPiiiszarfA_5OU2TAntaA8NQjTyb7BQpWaEmflUY2BinO_DJW9ptiH537FlzM6oy4LGFKvZjxLeTXpHMU39M-PFa20_1d4Ag5WVTXKi8FuuFWVDs6XLtk2elEZ5jofzg8KmNCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم باز قدرت‌نمایی می‌کنند
🔹
مهمانی ۱۰ کیلومتری و مهمانی‌های کیلومتری در استان‌ها تکرار حماسه مهم روز قدس است. حماسه‌ای که تصاویر فوق‌العاده زیبایی خلق کرد و در پس این تصاویر یک پیام مهم داشت.
🔹
بی‌شمار امواج مردم ایران در بیعت با رهبر انقلاب صاحب‌قدم هستند و برای جبهه مقاومت جان‌برکف و استوار ایستاده‌اند. این عید غدیر شاید چندوجهی‌ترین و مهم‌ترین عیدغدیر در سال‌های گذشته ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/439604" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLAr9GuTRXKTwysz33WENqjdek-ujeLITafkNbawbJ2o0AkSkul5Xl-6fjDStaZMi65KgJENOwI-482UsXCyAcjHjYUte-HN0ieinTa40LCQSl_H5sxZ-A6j1vr4oZU4BDGOA8D4beIpAHxXPmlcjrpfkfV1ZOhKvA1ejrEdwVBAkKvlaC-fgUSOjoWQuNwqM1cnXS3Z9F_jyaMgaq99U21EOJ9RM1vCEY2nUM038uEoWJfsLXw0hCaiN4bd9Bu2719cyDZkvNGFK5Cz2WiZa4fbg5XTuBdGT_k4XU6mJegQxschTe8FzlxgRTCR9gf7zBBiwAuZMGUicfBpdolQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqvjKZta5yMtUdIL440foiGvy6QLE_qrmcr5tCQNpucA94w8fv09SdyrlZh6daIaazObzvgfdWgYa-bSSQZwY533ZTQx-5yUx9Ee14RPU51IF1eO1Nh7F80PAMmNkWBj5OggxPiH16VIwdDfCUESvFg6rkoag8FB_-5f3n5GwokbgSitJnCKC6tvpFnGAD44jO-USQE99mthvpndulQlrboliL3-2nig5JvXe--Jqx9qSCQvJN_nPYlO0pQ2knue4RSJuPUSv804eolOPCXNT0fKT8IRxmyJS04Sia_sMTjOwqqmS7G-eGgol4SqqHxDAEUQrGP6QpLOS4sdhkMmAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار فرمانده قرارگاه خاتم‌الانبیا با خانوادۀ شهیدان نصیرزاده و دره‌باغی
🔹
سرلشکر خلبان علی عبداللهی با حضور در منزل سرلشکر شهید نصیرزاده وزیر فقید دفاع و سرلشکر شهید دره‌باغی معاون شهید آماد و پشتیبانی صنعتی ستاد کل نیروهای مسلح این دو شهید را اسوۀ شجاعت، تعهد و تواضع توصیف کرد‌.
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/439602" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدور احکام جدید بازنشستگان تامین‌اجتماعی، از هفتۀ آینده
🔹
تأمین اجتماعی: صدور احکام جدید بازنشستگان از هفتۀ آینده به‌صورت رسمی آغاز، و احتمالا تا ۱۵ خرداد به پایان خواهد رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/439601" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YD93TD1s6-cOVxV-eCgPRaLAeaquaJOgh80-m9nCVBBpv6znYz0mQgtMlNIwTdm2v_m1XnK--55COUIpoC_4O5AuHnoIWUaCg5mXxycMDckxY46CZCDDTVuiAU0UEY8VcagWwFx_ryJvepeO9cYMxs9A0ZlXvAsQqjxHqxk0SoZALOKsUgPd8SsTHgx1ViK4I14r_ZrNG3-LkriMAS5ckq6CdkCXzK0W2cVVN92haOHkQ00Su-2GgVFcG5KqovlZgGLyeaw1xXvjSB8RPmG_3d6xnmKK_KAXSAP4I_k1xiszKOpfaLaM2e3o_gFJHDl1fhKlaoC76Lsa0raNiUgnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAwBepa6zexfV59Pf53BmfLRxmJU79z8AgxpcLDV4MJHcJS9S3dE4NxbWm_9HwYFv8R8R4hZDoHbskqlXrxf0LSqJQLu-Y-Kbsx5Edu_qKJ8KsxHy7MzHca92uSKSmNvQx0hQi3Yaq_0WUJcIlxJy1DGenSn6rLQx7hUDXwe1ijWTlmvWgUfkh-RX3e5D5rEOu9GHtFKAcI_VK6_oxK-6SNOXSrIHLp63Ywrnhdeuz4RfpMLhSpB5acJMFizPcpDBWrVNyF2tlctkduXfkspJ6caSKwjVrocNbP_FxJhh7r7Q4tmwYeaHkp5doqnCkuLqE3Gu9ZIQZwvrjU0i9vDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdolrgcBLFm7C4krRD524Fe8gpDuEgUebP2CFHLl_VO_Ckl-fPOVlywiQsadTgzwQJwiNAS633qHfxs99Dzec9ujRBxvRG_neJs6kioXHTrDngm88uLzBnj02rbcWcAtGRglRpMXoctgBSr2vuKdGJ7TEaNnwTgdqNI1Wx97OFcAqzO5OG7MMZqUw-oSEts4XddAA6-QMIr0Wrvzcb_at01wXzGLHgkTukqRKeDOPkssLiIR7Fv3IRxfZF-JMBu_nIRI9ShtCGj9v4BdMl_mOheij22zx7W6fD6j-wEmhDt-b9mrC9AghMqUHoh8u-LWhbpvOxuo6DT6uPmM4hiryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzNJxhSfodHqtCjpecR6pfRI45wPp8BF5HtQ3PSTZVgmWMUZzls61jHetekISOsKWL8sU5iHw73-N1nsDVVsnhzDPc6_VK-MsrTbMP0mmTBloGQ38gE6yNL0PE-uIPLusyW14U5bPpmOuPJ5364aDI8SbtPdb2_qDxVNL2QTPwy58InDL7CYuqJYqEcXSNi_intEHNVi8ycuunnxxcnCvD-OG-tu9FOYtdljKTO3MJ1voD0o4oK-i_7_WgkbuefY7qGxpMMHmZC7j1Ptx2I2YM_gSLxFs8g2af0ankh9yP83Lg7Gtt1Rqi01ezH-U-oF5mUCG1OBJtHCoSzVW-n_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2H2FTT18iWDahCsDwcfsYl6od9pBJQ4hUSRs5HXRvNuW7vw4mjD3zl5DyCzrWC1LeKUn2hu2bi_6icqPGU07iZXvsxWfA0oZ9QSfkd7hIDqjsmkZv8aSXSioM3QIDewQpYNSCswEUMVyVd3Frq083Lrz2iVOrZWrtLcb-eGRfqbqeEIzhpNLLeIaxHTFNlpR2ZLXMbaF4Icq28wgnLdt811GTdctkyIQNRavDqG1Udswq0upRry9KZ_7dmF2PdzF1FBnh186WJqYxLB8on2bIK7FeML7IwwcV_eIIICY4En54awd-B0ghEjU7TuVRvFBzEl_giL--QOiXdZx05arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2B5twrB2evE_uLmXuQyDRASmgVF615ikmYEhp1lYKh4FiZ02L3cXIWzXaTpBYTqTmNXL8RNnVt78cUxCVj2vAYtW1juWyEPpDbuPahyj35_b7SR37qZzhzxS97Ue8RUfCuvezwEAUPI8CbXvvHLfHLzDbVssaPMZFdI2RleXXzf_2Juyz4R18HtpRjWaQdGKk8Vkew0wJvGQcbPUn_artnkMirgdVvLXTLhCxCq0VQlnaToxSNXq7s3E900cIiDc05SLF4-5vSFQL4mWlNNB4Z0CYcUaUjQzmk5BxFkoHnpzCyc9-H5urJrQBKeDSe08D4bGVpUFFnTEQFnAl0NRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_eltr_pzVaW6DqiFf7P2HZupe0Dv1g1eMd9A5ltkb2rR7_-mBgOKted7JlM7d2kjhwattSJcPd_AUWkry9lhRCN-Zw1lg19_p5b5H3RAgW8oQ332Or7OuIqW6JYvg3zbqrLq_ONS-KMgBCkMP0yFrKLADSVA_4X4OFaryHfAMv0sc9XN1jQrOIKNB8jviXcyqE5Jyn-i9XT28QyRPE7Q_ag3uHMKui3rG8wpJqen2sR3eQJguX3TR97GBIL2cU2wXJJ31ZR72XEFfj7dpIDEIixYL0VciU1UpTcojx2pdXoWlDSYuKhjTTQ9sAWzSOG1TJiRNlVOgaUSUC0S49Vwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر رهبر شهید انقلاب با خانوادۀ شهید نکوئی
🔹
حجت الاسلام ذوعلم و محسن پاک‌آیین اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب، با حضور در منزل پاسدار شهید مصطفی نکوئی، به مقام این شهید والامقام و خانوادۀ ایشان ادای احترام کردند.
🔹
شهید نکوئی در اثر حملۀ هوایی رژیم صهیونیستی در اولین روز جنگ رمضان در بیت رهبر شهید انقلاب به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/439594" target="_blank">📅 10:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fUkYHXsw6soR3eBEo12BtRwSw99fkliWOrUq9zNzaLVn3LWGknvS1ytjFDblMbYqEADSATPrUAbXZIPwwJzpkwWjTnh_90l_jVd-Xq2dVlJLHgdvFeqAzAQ3UpHjNd4CN_dVyID0bDmSi4xrmODxddiZ8Xpy0RhYTYio_9BI9sbem8AvobRfC5E1A16eiqlghfrI8cpEIRt7KG-0xUQh5yYAFzyIIvC8YUSSa5noDPIb6O7oOoN5lFr2yYVxBAS-vZh82viuGkseaFf_x1uVFHBPG3gVm1W463RZhsTSKcyhDN20xjIWjhi9JMYeP85trQrg0ZbP2r7NaKKINYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش‌های سیل‌آسا در راه ایران؟
🔹
مهدی زارع، کارشناس زمین‌شناسی: ایران در پاییز و زمستان امسال ممکن است تحت تأثیر «سوپر ال‌نینو» قرار بگیرد، پدیده‌ای نادر که می‌تواند بارش‌ها را به‌طور چشمگیری افزایش دهد و خطر وقوع سیلاب را بالا ببرد.  ال‌نینو چیست؟
🔹
ال‌نینو…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/439593" target="_blank">📅 10:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌ ابلاغ سهمیۀ بانک‌ها برای وام ازدواج و فرزندآوری
🔹
براساس ابلاغیۀ بانک مرکزی به شبکۀ بانکی، در سال جاری ۴۳۵ همت تسهیلات قرض‌الحسنۀ ازدواج و فرزندآوری پرداخت می‌شود که از این میزان ۳۵۰ همت برای ازدواج و ۸۵ همت فرزندآوری است.  @Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/439592" target="_blank">📅 10:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اجرای محدودیت‌های ترافیکی در جاده‌های شمال
کشور
🔹
پلیس راه مازندران: به‌دلیل افزایش پیش‌بینی‌شده حجم سفرها، محدودیت‌های ترافیکی از ۱۳ تا ۱۶ خرداد در جاده‌های شمالی اجرا می‌شود.
این محدودیت‌ها به‌شرح زیر است:
🔸
ممنوعیت تردد موتورسیکلت‌ها در جاده‌های کرج-چالوس، هراز و سوادکوه از ظهر امروز تا ساعت ۶ صبح ۱۶ خرداد
جادهٔ کرج-چالوس:
🔸
ممنوعیت تردد تریلر، کامیون و کامیونت
🔸
یک‌طرفه‌شدن مقطعی در صورت سنگینی ترافیک در چهارشنبه، پنجشنبه و شنبه
🔸
منع ورود خودروها به سمت چالوس از آزادراه تهران-شمال از ساعت ۱۲ جمعه و یک‌طرفه‌شدن مسیر مرزن‌آباد به تهران از ساعت ۱۵
جادهٔ هراز:
🔸
ممنوعیت تردد تریلرها، کامیون‌ها و کامیونت‌ها (به‌جز حاملان سوخت و مواد فاسدشدنی)
🔸
محدودیت یک‌طرفه مقطعی بین پلور و پلیس‌راه لاریجان در صورت ترافیک سنگین
جادهٔ سوادکوه:
🔸
ممنوعیت تردد تریلرها (به‌جز حاملان سوخت و مواد فاسدشدنی) در برخی ساعات چهارشنبه و جمعه از مسیر جنوب به شمال در صورت افزایش ترافیک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439591" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvHCG5OyTY2BvcEJpZff5p5769c-0vcUFznKby-wGFacZLTQICof1e2pQAENcGhXXS_-GqQw3p9igDHYp9pgMHsLJZJIu1NE4kAuBeCj9ZdW3UKyC_UjXVVYZX3JNXJn1_KSaU6v7E-CMd-m9NfA0wP1XezxpIe5Jp14DDMbwaWRq8JthA2QqQMZ22cDINR4VOpnXc02VvFlu4rYERpxv50Xs-tjwXmBh_fiv9uRr3F89VANJQgzwnPR0oz6_uXQmcp2Nwnv1oYfQLPIx51Fc7ggOF76a8a2pdFu1ZnIgovQMEL4aZDPx1rnpMv8LCEoaZu7Uzh4u0-1yR7737zidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشد سه‌رقمی شاخص‌های عملکردی پیشخوان های شهرنت‌ بانک شهر / استقبال از کارت هدیه افزایش یافت
🟡
پیشخوان‌های شهرنت بانک شهر در اردیبهشت امسال با وجود محدودیت‌های عملیاتی ناشی از شرایط خاص، در شاخص‌های کلیدی عملکردی رشد سه رقمی داشتند. منابع مستقیم ۱۸۲ درصد نسبت به مدت مشابه سال قبل افزایش یافت و مبلغ صدور کارت هدیه نیز با رشد ۱۰۹ درصدی مواجه بود.
🟡
به گزارش روابط عمومی بانک شهر، در بازه زمانی اردیبهشت ۱۴۰۵، بخشی از پیشخوان‌های شهرنت به دلیل شرایط خاص عملیاتی، با محدودیت‌هایی در ارائه خدمات مواجه بودند. در حالیکه در این دوره حدود ۱۰ درصد از پیشخوان‌ها به طور موقت از چرخه بهره‌برداری خارج شده بودند، روند توسعه و رشد عملکرد شبکه شهرنت حفظ شد و شاخص‌های کلیدی این پروژه بهبود یافت.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/439590" target="_blank">📅 10:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9LBg7Ew4IW4yRo-g31S1ruR9JCJTM-5cU5UFP9ySvr3dlnyhTQNo5Av2wuNpfXXwROnDRqYlq-wGwSBy85bWArUoTm16Wxn-xDiUfkjAPEgP2mHHFS_ytqppFceO6jRVoPH9-w3XjnnNwJJdMzcxYW8-vHtHoDr2029-yU715e_FhlMu_qBJ5aGYN9hejKyWfcvmtjyoz-au4avqB2y7AuZ5jfzDhZ3mq4OUpgoV17G-hLtqoRsMAxcRQW0z0DccP1UT4XQnl3Ftd8dZvdsHRbpfGVpjfwAZFqUGHW2NT3r8tCRMkQjBwgrt_dR5iNZRopzVdQ1c_EdP8Kn_1gFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ملی فن‌‎آفرینی تاثریا برگزار می‌کند:
❇️
بیست‌وهشتمین *رویداد ملی تاثُریا* ، با هدف توسعه اقتصاد دانش‌بنیان.
🔹
*استان‌های میزبان: * قزوین، زنجان
🔹
*موضوع:* شهرک‌های صنعتی در مسیر اقتصاد دانش‌بنیان
🔸
*محورهای رویداد:*
۱. اتصال شبکه فن‌بازار به کلینیک‌های کسب‌وکار
۲. ارتباط صنعت و فناوری
۳. شهرک صنعتی هوشمند
۴. صنعت در مسیر اقتصاد دانش‌بنیان
۵. توسعه صادرات دانش‌بنیان
📅
* زمان و مکان برگزاری* :
۱۷ تیرماه ۱۴۰۵ | به میزبانی استان قزوین
🌐
*اطلاعات تکمیلی رویداد* :
tasorayahub.ir/events/event/qazvin-zanjan-tasoraya
✴️
*قابل توجه فناوران، نوآوران و کسب‌وکارهای دانش‌بنیان:*
علاقمندان، فعالان حوزه کسب‌کار فناورانه، نوآور و دانش‌بنیان در "سراسر کشور" می‌توانند محصولات فناورانه خود را جهت اتصال به کارخانجات صنعتی حداکثر تا تاریخ *۱۰ تیرماه ۱۴۰۵* از طریق وب‌سایت رسمی شبکه ملی فن‌آفرینی تاثریا ارسال کنند.
🌐
tasorayahub.ir
#تاثریا
#رویداد_ملی_تاثریا
#شهرک‌های_صنعتی
#دانش‌بنیان
#سرمایه‌گذاری
📫
هلدینگ پیشگامان
📢
@Pishgamanhub</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/439589" target="_blank">📅 10:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/439587" target="_blank">📅 10:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
پهپادهای شاهد ۱۳۶ سپاه پاسداران در آسمان کویت  @Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/439586" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFcEJYZEDPybsU-TmHqZQN_tQPL7cmNpoO2Kuqf5LMmQ1r-PPQt3UZslGXpZOcgkHbdrFx7DFt1aBKvJty6XnhwP1ters7w2SvwMb0MZTnvegTKmnxOJ007EYGfq16QAxg4XGysGhlmAysnsxVMODHOAy4anv-vXACMV9fnZqVhYhryqzjZPt3ivB7is4bk9V77neUqtoeLHUFOYDZPNiNQ1kpL9WmtAuse9YYu8A4M6L93i0EPGhfDjX-Iab3gohndeAeXizBt5S-TwcM7WIqvVqtA7D25GkPswnCHt2Mmr4lINIC22U12bklAYcGbahaDeMqzR9Gt5ZPigFk5K8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مهمانی ۱۰ کیلومتری غدیر، فردا از ساعت ۱۵ در تهران آغاز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/439585" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارتش صهیونیستی هشدار تخلیهٔ روستاهای ارزی، مزرعه کوثریه الرز و زراریه در شهر صیدا در جنوب لبنان را صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/439584" target="_blank">📅 09:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در دزفول
🔹
فرمانداری دزفول: درپی امحای مهمات از ساعت ۱۰ تا ۱۲، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/439582" target="_blank">📅 09:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379837c74.mov?token=h6fwYH2RZp5c7q_6No3_Ji45SRaBF0rP-uCJaPTSUsLEFn4AsroF97bHZNuxdIMgcwsnG26AwxN5jcntgY6TbY4Yg_HIZaeHw_YfDrJLQx9LsixT5-IZWUfRhMa4dXMutILLG_8VU0oCUn_uTLB5HyQybDciNkJzTj8qvdZHMm3J16hMHYgdVaJv2nSPGyQ1S8BuYd803CqGztEisPuiVGB4k7kuAEKT7MmoXcX5wq6nN496hrO4sus6525wuBlCknPxZ6GE6DVV_Rok85eaSEwRoo10TfJWQpn0MgYOv--cFeDdrJ8dh1B8rEY2pl3QSzv20rEbCU2SkJR7kjhVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379837c74.mov?token=h6fwYH2RZp5c7q_6No3_Ji45SRaBF0rP-uCJaPTSUsLEFn4AsroF97bHZNuxdIMgcwsnG26AwxN5jcntgY6TbY4Yg_HIZaeHw_YfDrJLQx9LsixT5-IZWUfRhMa4dXMutILLG_8VU0oCUn_uTLB5HyQybDciNkJzTj8qvdZHMm3J16hMHYgdVaJv2nSPGyQ1S8BuYd803CqGztEisPuiVGB4k7kuAEKT7MmoXcX5wq6nN496hrO4sus6525wuBlCknPxZ6GE6DVV_Rok85eaSEwRoo10TfJWQpn0MgYOv--cFeDdrJ8dh1B8rEY2pl3QSzv20rEbCU2SkJR7kjhVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست خدا و نفس پیمبر فقط علی(ع) است
🔹
نصب کتیبه‌های عید غدیر در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/439579" target="_blank">📅 09:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6ff7172d.mp4?token=p7T9Anj3DPn9rjhIvvX80fFpYHPsAgvWoClSsG2QhHqtZUCFY_xZ3X5Fqa48ODchYVUIBRaQyIXzwaw0OmIvd06jLv2BmidnnAzJHlswP6XNPVITY9YyPHWiyYJFVbcW6E9u6ZL52nGBSc9-pSr0Pn7EZB9V8924hv6JwSZqJ9SckGltFHCtTftrlIO2e-ryulsOqnYnKty_hopF6TcCO-1uB93zgjkDXsewcneGvaIp615iLTi1SwSnU8sjU_Ce99Eo0zB_yCuwk72y0zI8v9tCZLJs9jTBwWX-KDjXSdagCLaiVbG2CveigxdnmRYxNDi0l_tFmNQlc0WQi3EiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6ff7172d.mp4?token=p7T9Anj3DPn9rjhIvvX80fFpYHPsAgvWoClSsG2QhHqtZUCFY_xZ3X5Fqa48ODchYVUIBRaQyIXzwaw0OmIvd06jLv2BmidnnAzJHlswP6XNPVITY9YyPHWiyYJFVbcW6E9u6ZL52nGBSc9-pSr0Pn7EZB9V8924hv6JwSZqJ9SckGltFHCtTftrlIO2e-ryulsOqnYnKty_hopF6TcCO-1uB93zgjkDXsewcneGvaIp615iLTi1SwSnU8sjU_Ce99Eo0zB_yCuwk72y0zI8v9tCZLJs9jTBwWX-KDjXSdagCLaiVbG2CveigxdnmRYxNDi0l_tFmNQlc0WQi3EiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گروگان‌گیری و تهدید به بمب‌گذاری در کالیفرنیا
🔹
پلیس شهر بیکرزفیلد در جنوب ایالت کالیفرنیا اعلام کرد یک فرد ناشناس که احتمال می‌رود کمربند یا جلیقه‌ای حاوی مواد منفجره همراه داشته باشد، تعداد نامشخصی از مردم محلی را در ساختمان یک بانک گروگان گرفته است.
🔹
پلیس آمریکا در ابتدا پس از دریافت یک تهدید به بمب‌گذاری در بانک چیس در نزدیکی خیابان چستر و خیابان هفدهم، به محل اعزام شدند و سپس با ایجاد یک محدودهٔ امنیتی گسترده، عملیات مدیریت بحران و مذاکره را آغاز کردند.
🔹
سخنگوی پلیس بیکرزفیلد اعلام کرد که یکی از گروگان‌ها آزاد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/439576" target="_blank">📅 09:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439575">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
🔹
مدیریت بحران استانداری اصفهان: انفجارهای کنترل‌شده مرتبط با مهمات عمل‌نکردهٔ جنگ رمضان در جنوب اصفهان و در محدودهٔ شهر بهارستان تا ساعت ۱۰ امروز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/439575" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439574">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
تصاویری از عملیات حمله به ناوگان پنجم دریایی، و پایگاه هوایی و بالگردی ارتش تروریستی آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439574" target="_blank">📅 09:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439573">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
فواد ایزدی: آمریکا به‌دنبال عادی‌سازی حمله به ایران است
🔹
کارشناس مسائل بین‌الملل: کاری که آمریکایی‌ها می‌کنند شبیه آتش‌بس در غزه و لبنان است. حوصلۀ ایران همیشگی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/439573" target="_blank">📅 09:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0876c332eb.mp4?token=ufVZd860gDwOTY38hMvimkAoN2NF673kWJOHgBEsCUaneQV3ewIHWWHBaMv69uKv9OpQn8TdYCJvjCLQR8DerbYDh3IO2DoKPnAtRAFnVy8cFyvKW4PDk1_pbcaMiqj7mNxBfF8EhVnqXyUsYPY-gOTt88w9H3riWGeDhrLkNIR0eVCFHCdCUf3qKGrVg4b6LDhigtl32khqfVCo7Hx7_Jgq2WN4yCeuHpK4fXGdy9dRUeaq2pc3Dlsxp5jty5hM5C0t-dW0_aYaK4VAJHTzzojuupWqNUASRN0XEOp3_jnUAc_G4v6y-cDP7w68H3Y0Ujz3tA5E1DWLdzw0QaCMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0876c332eb.mp4?token=ufVZd860gDwOTY38hMvimkAoN2NF673kWJOHgBEsCUaneQV3ewIHWWHBaMv69uKv9OpQn8TdYCJvjCLQR8DerbYDh3IO2DoKPnAtRAFnVy8cFyvKW4PDk1_pbcaMiqj7mNxBfF8EhVnqXyUsYPY-gOTt88w9H3riWGeDhrLkNIR0eVCFHCdCUf3qKGrVg4b6LDhigtl32khqfVCo7Hx7_Jgq2WN4yCeuHpK4fXGdy9dRUeaq2pc3Dlsxp5jty5hM5C0t-dW0_aYaK4VAJHTzzojuupWqNUASRN0XEOp3_jnUAc_G4v6y-cDP7w68H3Y0Ujz3tA5E1DWLdzw0QaCMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از عملیات حمله به ناوگان پنجم دریایی، و پایگاه هوایی و بالگردی ارتش تروریستی آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/439571" target="_blank">📅 08:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b66b238e.mp4?token=QhBTMydKHTB0D0wkz842wBgVHSV-ibbh7mctBGNrNyPrXlMbeOzkvp5ZqcuaJRNISJEf04Fu7dkUGY5p3TklpQz1NQbG8Z-w_-OlyJCDBG1oNN8PjXfM2Tr7LI23URXzydAQ4-LKL1wue8byjKTl-ggRQ4aJ3LcnY60mS5-mEi23cx-Ug3yjhY00SLhnmBBUwTcpqtt1GorgM1LpT3XOdGlyvlhbMK1n-yjzM2THSKs7KQGOGS2yXcHoTRfg5GCeApyNN1b8VXpxlGCQsrbNbt-4_24YbQS68nMPsB5MoJ915niHzXB5gA863Zq7cBKl60nD3OJfFu2Q4z0qpJhupw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b66b238e.mp4?token=QhBTMydKHTB0D0wkz842wBgVHSV-ibbh7mctBGNrNyPrXlMbeOzkvp5ZqcuaJRNISJEf04Fu7dkUGY5p3TklpQz1NQbG8Z-w_-OlyJCDBG1oNN8PjXfM2Tr7LI23URXzydAQ4-LKL1wue8byjKTl-ggRQ4aJ3LcnY60mS5-mEi23cx-Ug3yjhY00SLhnmBBUwTcpqtt1GorgM1LpT3XOdGlyvlhbMK1n-yjzM2THSKs7KQGOGS2yXcHoTRfg5GCeApyNN1b8VXpxlGCQsrbNbt-4_24YbQS68nMPsB5MoJ915niHzXB5gA863Zq7cBKl60nD3OJfFu2Q4z0qpJhupw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: کسانی که می‌خواهند به شمال بروند، فردا و پس‌فردا منتظر بارش باشند.
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/439570" target="_blank">📅 08:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4702f8e30a.mp4?token=nJ0WS-cvHHUWsOp4hFF-KAAJt_A-wdzmQHwd_8B3xz_f2qjlBoDjGSVjz41OcqNVdsHXRUO7KUVowo1HV2WllPg8kbSR3pJdVkWpgjyTI0IKCcOCrabh_V6MN0d9FxTUoGP1C53743juekYrIk_iqOW52qFDiyKU8gXTSC36VKasvU8q72NRyDAPjhKwexPeNAouaMVNkGOkpV-dL6nHf7lFgxTQoVz62K6fGo_0gEp6C0D2S784R3WdcnNFIrXN1h1tShb-sPBEMmKtDqCQODZ95UtK4qAWpje0AGUWiyv2YG2v1f2lL31V61ZCXXkqHBSug1ePqtPV1NuPranIvJrr00JNzBP9tU3F7zrWA2XUqD1BM4Fq4-EImgt-m_7gzLh-cylnYbdJ0glfi_boh9X9JmpiJlZQPmH_L5VAgBLg9xuMIx00stmQfY5qX1cJUweJ_YeN-MSgBzAXryQj_R-jvDkUCr8vFm2N0bKvghRpBFIrrZk_nLPtUHmQGja7GkAfXFGEJQURb7MC4GqmiHXNDZB8SA1MDGzABR_VXOV8KbFR2mZJHKo63snoNjWvMPND9NI6eJvJVeLMy9XAaob1rc1BC4ye9EaKsTgYKb9z-q8IigdkD3vC2Uua3WyT0zVRWuY6hXackAViQlKVL2jmPJVhfjqESixokfxOnf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4702f8e30a.mp4?token=nJ0WS-cvHHUWsOp4hFF-KAAJt_A-wdzmQHwd_8B3xz_f2qjlBoDjGSVjz41OcqNVdsHXRUO7KUVowo1HV2WllPg8kbSR3pJdVkWpgjyTI0IKCcOCrabh_V6MN0d9FxTUoGP1C53743juekYrIk_iqOW52qFDiyKU8gXTSC36VKasvU8q72NRyDAPjhKwexPeNAouaMVNkGOkpV-dL6nHf7lFgxTQoVz62K6fGo_0gEp6C0D2S784R3WdcnNFIrXN1h1tShb-sPBEMmKtDqCQODZ95UtK4qAWpje0AGUWiyv2YG2v1f2lL31V61ZCXXkqHBSug1ePqtPV1NuPranIvJrr00JNzBP9tU3F7zrWA2XUqD1BM4Fq4-EImgt-m_7gzLh-cylnYbdJ0glfi_boh9X9JmpiJlZQPmH_L5VAgBLg9xuMIx00stmQfY5qX1cJUweJ_YeN-MSgBzAXryQj_R-jvDkUCr8vFm2N0bKvghRpBFIrrZk_nLPtUHmQGja7GkAfXFGEJQURb7MC4GqmiHXNDZB8SA1MDGzABR_VXOV8KbFR2mZJHKo63snoNjWvMPND9NI6eJvJVeLMy9XAaob1rc1BC4ye9EaKsTgYKb9z-q8IigdkD3vC2Uua3WyT0zVRWuY6hXackAViQlKVL2jmPJVhfjqESixokfxOnf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ رنگ پرچمت زیباست ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/439569" target="_blank">📅 08:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1460006634.mp4?token=czzqrVEiYqZS8k3UW73HL1bOWG5XI6hejtku-Jhb3XivNvNKzixs7DWoaoKE3USajvRhn-NbVATsWZRVdZDSN_E8UhUhBEB8N1kikWyM8MquOsaVALBCzbOpv2NFS2_38Vbd0C4FNA9MHzDE8QcjWcrbX2AChLCOnJxtaKRL-YoBMshhvd6gDnLo7becPvLf-YDNWMCClO-9Ez_kfTUhQ-s0HaOJJ0TluNMrZ4J7K1I84o_4Frfc5vj7shshNhd6o_Eb6t3TN0APSBpxuLPbhJALaAwgzoVB6OcxgygTi2Ei7xnldmXmqFe7TETJKQimWgAIymTSXhbRO2w7JZ_X4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1460006634.mp4?token=czzqrVEiYqZS8k3UW73HL1bOWG5XI6hejtku-Jhb3XivNvNKzixs7DWoaoKE3USajvRhn-NbVATsWZRVdZDSN_E8UhUhBEB8N1kikWyM8MquOsaVALBCzbOpv2NFS2_38Vbd0C4FNA9MHzDE8QcjWcrbX2AChLCOnJxtaKRL-YoBMshhvd6gDnLo7becPvLf-YDNWMCClO-9Ez_kfTUhQ-s0HaOJJ0TluNMrZ4J7K1I84o_4Frfc5vj7shshNhd6o_Eb6t3TN0APSBpxuLPbhJALaAwgzoVB6OcxgygTi2Ei7xnldmXmqFe7TETJKQimWgAIymTSXhbRO2w7JZ_X4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس
🔹
سخنگوی آتش‌نشانی: صبح امروز خودروی نیسان در حال سوخت‌گیری در جایگاه سوخت گاز واقع در بزرگراه یاسینی بود که به‌دلایل نامشخص دچار انفجار شد.
🔹
در این حادثه دو نفر مصدوم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/439568" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZYIFPhL2izOomGCtNQ74feGx5kT_82Ur2ag3b18iPlQmBJCUGX4dj1CC_dFUwJIFacOB7XoyAXmVjMwBClLX6mwvXidaoPR8QttlkUrgYs3fJSICFnqBTzypyQt3SekDLrpFiNYUJKibvHKtS49BQS30xYoIcKmX7yM0lMPLlxjZv8S7elgQMnOOEngzlhCYaPT94XoDHxO3oBNHuH0LPCuNdti34pdZj2AHAixJxugGWZ6yEZduDoSrb0l6NPH8V3DI4_NdKUqh8c62gjhVMtTFYCZXVBdWRgoz0rM9HIDB9CGCqd--EGWUZXQo0pI5svEMf5ks-24E5J67FLYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ هزار مدرسه به پنل‌های خورشیدی مجهز می‌شوند
🔹
براساس تفاهم‌نامۀ جدید میان سازمان نوسازی مدارس و سازمان انرژی‌های تجدیدپذیر، ۱۲ هزار مدرسه در کشور به پنل‌های خورشیدی مجهز خواهند شد.
🔹
در فاز نخست، تولید ۶۰ مگاوات برق هدف‌گذاری شده و اولویت اجرای آن در مدارس مناطق کم‌برخوردار، مرزی، شبانه‌روزی و آسیب‌دیده از جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/439566" target="_blank">📅 07:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8daabd898.mp4?token=Le_6WrJOPhvaaySliWCAxzRTaTEUxK3DdweFE7b65By0OYxolnRJsv16A6vdq8Y5OK1JjZSd-rD0aRJXimp-IvpCrRjVaBd_XecTjeBiBx0RXiY2MFv41SOsGcaKJwfyQ633sfQ-jNGo5Lzu0Wg_evMKL67GQQDZw6E_d2FcqVc46WqElf-8zpvtneQMbCNfWEDQhL2KUfqqlUAZjdf7RswV-tmMenHpGwvJU3XgXlBhIvCtVaqlkhwW8lhZTwc5SNzacBlnf9z3sAIDIBeQU6_6xL67sGBsiY7MeJ_0gRnDvFPUAdlq5kotqYRSJrEBrTNc1aHhEUCcyMSs3vhLwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8daabd898.mp4?token=Le_6WrJOPhvaaySliWCAxzRTaTEUxK3DdweFE7b65By0OYxolnRJsv16A6vdq8Y5OK1JjZSd-rD0aRJXimp-IvpCrRjVaBd_XecTjeBiBx0RXiY2MFv41SOsGcaKJwfyQ633sfQ-jNGo5Lzu0Wg_evMKL67GQQDZw6E_d2FcqVc46WqElf-8zpvtneQMbCNfWEDQhL2KUfqqlUAZjdf7RswV-tmMenHpGwvJU3XgXlBhIvCtVaqlkhwW8lhZTwc5SNzacBlnf9z3sAIDIBeQU6_6xL67sGBsiY7MeJ_0gRnDvFPUAdlq5kotqYRSJrEBrTNc1aHhEUCcyMSs3vhLwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفت
🔹
سپاه پاسداران: در اواخر شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز مورد اصابت پرتابۀ هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/439565" target="_blank">📅 06:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
روایت نفس‌گیر آتش‌نشان فداکار و نجات جان ۱۵ هموطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/439564" target="_blank">📅 06:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb057d6add.mp4?token=DFVu9NFOoI8LmpClPQSpf65rvAKeg8YUW31eR3N_cYjRzf6p7ZWOCT50n3iSHB9ncv3v3bTgmVgX9_UOCbR6UW7IwYx5PAK34cwFljrJhZaKPqrsz1X4dz77KiB1RpTp85If7ZXXbRN10mBeXCVSyWgaaLSY6SOHFrqKFvBs9MdEDiPSyWVjh_Ra1WTQhkgT5Hd_g0Jn-KjJXCBh-tDBla5u2TcF5a3vd-sn-fwkKlFoPTqu6J7dqL3wK0CLUekXeGu74GDxUgSOizaYJ-PdGtL4dhQniNyhiqHfdYrK_Hp0sOJRTgEHycWxbdp4qf_1zsb4wfgkqhC8mpqQ1N9DTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb057d6add.mp4?token=DFVu9NFOoI8LmpClPQSpf65rvAKeg8YUW31eR3N_cYjRzf6p7ZWOCT50n3iSHB9ncv3v3bTgmVgX9_UOCbR6UW7IwYx5PAK34cwFljrJhZaKPqrsz1X4dz77KiB1RpTp85If7ZXXbRN10mBeXCVSyWgaaLSY6SOHFrqKFvBs9MdEDiPSyWVjh_Ra1WTQhkgT5Hd_g0Jn-KjJXCBh-tDBla5u2TcF5a3vd-sn-fwkKlFoPTqu6J7dqL3wK0CLUekXeGu74GDxUgSOizaYJ-PdGtL4dhQniNyhiqHfdYrK_Hp0sOJRTgEHycWxbdp4qf_1zsb4wfgkqhC8mpqQ1N9DTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای شاهد ۱۳۶ سپاه پاسداران در آسمان کویت
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/439563" target="_blank">📅 04:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439562">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6776e560.mp4?token=KYQ4Gdy1ScZxFwVq_oLe78QVX9KWRmiUWprOTSFcIEXegFp8rMTgSah4uUD2E4RYuxQOjLbdspJAYtJ3fTFwDGKailyI-_ebJakKoucYFPIRKHEtgyw4rwz8hg5AbayzBNZa1LsuNaLVhRZQOJR7asjPzXafm3wSzCX_KKgdvAMIUZ6UgvT7TWAUWMtdat8oyS3HJMZYyrJ1khBt-QSyz21bM67nJoFcHnk3zj9KQqIveT8gUbnXjkvd14mV4YQV1wJydAA17ngINX2nTzd2rKSDWZ2b23h9K5wtDBJTOzek_0bn7P4AFD9nRdjk8EcXePC9yWm97O4gu8VMkw_RSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6776e560.mp4?token=KYQ4Gdy1ScZxFwVq_oLe78QVX9KWRmiUWprOTSFcIEXegFp8rMTgSah4uUD2E4RYuxQOjLbdspJAYtJ3fTFwDGKailyI-_ebJakKoucYFPIRKHEtgyw4rwz8hg5AbayzBNZa1LsuNaLVhRZQOJR7asjPzXafm3wSzCX_KKgdvAMIUZ6UgvT7TWAUWMtdat8oyS3HJMZYyrJ1khBt-QSyz21bM67nJoFcHnk3zj9KQqIveT8gUbnXjkvd14mV4YQV1wJydAA17ngINX2nTzd2rKSDWZ2b23h9K5wtDBJTOzek_0bn7P4AFD9nRdjk8EcXePC9yWm97O4gu8VMkw_RSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیوی منتسب به لحظۀ اصابت موشک ایرانی به مقر ناوگان پنجم نیروی‌دریایی آمریکا در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/439562" target="_blank">📅 04:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439561">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyANkTF0Ecik-bbgKm4srhgLbXiWlsTV7o78ScUi8-guEmRGBR5iC0aPJIHl_ZyUQZgL2Bp2JTUBLaaD3SCiZZmhwixfzeXC37ic0XjJTiyQOuaFKaZR0CqIGxvNuI7KthTeUSUVV4wlSeCzS9ROpL-uMc7gY8FWUKSCTXqeXQqmlcS6BpDDKrG8YHY3YuCHXmPu_qHNSlCleDkTd8D2ouh5stK3yzfvyCcfhf0TcVJv-hpYv41jPNeojESdrtj6SlQ2mVYDRBRHGDS9Fdw3bcUQo-p7GbFVOIF9ju4koEn1Ilplas2_qi1MXXNsIayEO7Hy7VyH8f8kdV_7HsG4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی هر بشکه نفت برنت از ۹۷ دلار فراتر رفت
🔹
درپی پاسخ قاطع نیروهای‌مسلح ایران به اقدام نظامی آمریکا در منطقۀ خلیج فارس، قیمت نفت برنت با رشد ۱.۰۷ درصدی به ۹۷.۱۱ دلار در هر بشکه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/439561" target="_blank">📅 04:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e86d17c6e.mp4?token=iYQzwcek5H7n6fiemFmvf--ltIVUbBRz2PJGpVcvokRJR6_aZlVqznm8-_InNwRNIKwLCD2ibqytadN6Me8HLQB3t3NJelhRN_GQkhRkfTtKqsKrUn4UJ-VVokHoOLJjKh6lP2yKn8idu254c-3zdlc1SrVp31yuNKJejBrpKHy28ciAOpO3SqzbFPwqcJFNS4kpsRXc90Jj82bDWDk2QixCHUhTDEcAhf11LomwKB8oH_WTWtxNXCazafk6dNP8rjPRfwyVUnhuoJmzxZ49MWMUggWy4wbnsQpWV_cI-GH3WfCyjJNwZH14TuMk-XEvogK2rrxc5_mkD_Clazjtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e86d17c6e.mp4?token=iYQzwcek5H7n6fiemFmvf--ltIVUbBRz2PJGpVcvokRJR6_aZlVqznm8-_InNwRNIKwLCD2ibqytadN6Me8HLQB3t3NJelhRN_GQkhRkfTtKqsKrUn4UJ-VVokHoOLJjKh6lP2yKn8idu254c-3zdlc1SrVp31yuNKJejBrpKHy28ciAOpO3SqzbFPwqcJFNS4kpsRXc90Jj82bDWDk2QixCHUhTDEcAhf11LomwKB8oH_WTWtxNXCazafk6dNP8rjPRfwyVUnhuoJmzxZ49MWMUggWy4wbnsQpWV_cI-GH3WfCyjJNwZH14TuMk-XEvogK2rrxc5_mkD_Clazjtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از کار افتادن موشک رهگیر «پاتریوت» بعد از شلیک در کویت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/439559" target="_blank">📅 03:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدای انفجار در قامشلی سوریه
🔹
برخی منابع خبری از شنیده‌شدن صدای انفجار در شهر قامشلی سوریه گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/439558" target="_blank">📅 03:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سنتکام: ایران پایگاه‌های آمریکا را هدف قرار داد
🔹
ارتش آمریکا تایید کرد که نظامیان این کشور در کشورهای حاشیۀ خلیج فارس، هدف موشک‌ها و پهپادی ایرانی قرار گرفته است.
🔸
شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز، و یک دکل مخابراتی سپاه را در جنوب جزیرۀ قشم هدف پرتابه‌های هوایی خود قرار داده بود‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/439557" target="_blank">📅 03:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفت
🔹
سپاه پاسداران: در اواخر شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز مورد اصابت پرتابۀ هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
🔹
در پاسخ به این تجاوز و نقض مقررات تنگۀ هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک‌های نیروی دریایی سپاه قرار گرفت.
🔹
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیرۀ قشم را هدف پرتابه‌های هوایی خود قرار داد. در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
🔸
پیش از این اخطار داده بودیم که درصورت تجاوز پاسخ متفاوت و سنگین‌تر خواهد بود و همینطور اقدام کردیم. این پاسخ‌ها باید عبرت شده باشد.
🔸
تکرار می‌کنیم برهم زدن امنیت تنگۀ هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/439556" target="_blank">📅 03:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
به‌ادعای برخی رسانه‌های عراقی، شناورهای نظامی در آب‌های نزدیک سواحل امارات هدف اصابت موشک و پهپاد قرار گرفته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/439555" target="_blank">📅 03:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فعال‌شدن آژیر خطر در امارات
🔹
به گفتۀ منابع محلی، آژیرهای خطر حملات هوایی در امارات فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/439554" target="_blank">📅 03:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439552">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09608d223.mp4?token=Xg0WYJed_F9qFytpIFaD9PqGdEItED4DlNDOdmUpl1wdxMNxEqs0XsFvO3a6DXG6cT15TgSwt43oz9YVyTBAMUyFdQX8LZ9jKEN2Tx8c43RzOA599pF08mDm1X2orOUBhd_wVjtvZLebE7JOTp0zpiQKhXk2atVF-vjSiNkX0OYe_btDdbGQys_t5L_BWGVzzooPvlgL6OFgV4KBL5X54Opc1mqihoWJx7Af3eE4CSvol7-pwjXbFXMGNySlw8VK2q9Ctz_RxExL1oe6nk9YMex3Xw1IBsSqcY4V4TX72iEXCUdfjQJXcw0XZoj38PGHWmsd90NQnuW4SuDyYJe1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09608d223.mp4?token=Xg0WYJed_F9qFytpIFaD9PqGdEItED4DlNDOdmUpl1wdxMNxEqs0XsFvO3a6DXG6cT15TgSwt43oz9YVyTBAMUyFdQX8LZ9jKEN2Tx8c43RzOA599pF08mDm1X2orOUBhd_wVjtvZLebE7JOTp0zpiQKhXk2atVF-vjSiNkX0OYe_btDdbGQys_t5L_BWGVzzooPvlgL6OFgV4KBL5X54Opc1mqihoWJx7Af3eE4CSvol7-pwjXbFXMGNySlw8VK2q9Ctz_RxExL1oe6nk9YMex3Xw1IBsSqcY4V4TX72iEXCUdfjQJXcw0XZoj38PGHWmsd90NQnuW4SuDyYJe1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حمله به پایگاه آمریکایی‌ها در کویت
🔹
برخی منابع عربی می‌گویند انفجارهایی در پایگاه‌های «علی‌السالم» و «عریفجان» محل استقرار نظامیان آمریکایی رخ داده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/439552" target="_blank">📅 03:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439551">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
توقف کامل پروازها در بحرین، کویت و امارات
🔹
رسانه‌های عربی گزارش دادند که فعالیت فرودگاه‌ها و تمام پروازها در بحرین، کویت و امارات عربی متحده به‌دلیل حملات هوایی متوقف شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/439551" target="_blank">📅 02:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439550">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
آژیر خطر در عربستان نیز به‌صدا درآمد
🔹
به گفتۀ منابع محلی، آژیرهای خطر حملات هوایی در پایگاه‌های آمریکا در خاک عربستان‌سعودی فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/439550" target="_blank">📅 02:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439549">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a517c4c47.mp4?token=IP44epbWd5CkKMBGH9tP8gMlqWzF0zOI9lWLxGrFov_u9-Zmel5qnZjFf1lhMtOKKQUAJUbQt_ReHjeHd6YCcv50dwant6P_YqWjcpoi7Xxw9ssS-JtGd6LMb59CqZBm9BL0BHn_YtuVXwQQTmoy21qvKXHT0OnJrXkghro9ePpdGJHgpHgFLVdv_oen9Gp5zUzuPM0ubx5Cw7c_E7MeKKc5pf6MmkoPqEmDmunnyBNjv2UkpHlc1Lh7PAY_lktqX9G_UjTDWIp3uK6H8Hsu_uZX0nXNoSykIQh5NnkRhPnmAhTNSjxjMZKcg0lZT8uuyr1Tdtt2AWvl1CWjDRh-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a517c4c47.mp4?token=IP44epbWd5CkKMBGH9tP8gMlqWzF0zOI9lWLxGrFov_u9-Zmel5qnZjFf1lhMtOKKQUAJUbQt_ReHjeHd6YCcv50dwant6P_YqWjcpoi7Xxw9ssS-JtGd6LMb59CqZBm9BL0BHn_YtuVXwQQTmoy21qvKXHT0OnJrXkghro9ePpdGJHgpHgFLVdv_oen9Gp5zUzuPM0ubx5Cw7c_E7MeKKc5pf6MmkoPqEmDmunnyBNjv2UkpHlc1Lh7PAY_lktqX9G_UjTDWIp3uK6H8Hsu_uZX0nXNoSykIQh5NnkRhPnmAhTNSjxjMZKcg0lZT8uuyr1Tdtt2AWvl1CWjDRh-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک سامانۀ پدافندی «پاتریوت» در بحرین
🔸
گفته می‌شود پایگاه «الجفری» و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین مورد اصابت قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/439549" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439548">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
حملات به بحرین و کویت ادامه دارد
🔹
به گزارش رسانه‌های عربی، حملات موشکی و پهپادی به محل استقرار نظامیان آمریکایی در کویت و بحرین هم‌چنان ادامه داشته و آژیرهای هشدار قطع نمی‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/439548" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439546">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7bbe8d9a.mp4?token=WgrN9o0hFsnGAIrd_Iv3AaH97JYDKRFAPJw6ESZ8vzV24sLm07r2UQuLRfNcna4fJ_XbeT0IP-36-oyPSu8cC5XYOBZKUJ83UrAwQHMY6o3-BcK9vQCqf9Gn2hwkVojM9B2_Pn9yChApAZ8hOPfyhZhmV9AWla3M6o7-3eVyh0Z-LSaEwtmIF5c1J0MIDfyWyKd_EoP0jQlJoHZB9XiOHaFxqcXvQA_4GRijdWSzz3GbrkEXA_kAh1lcBPrXfVRhzn6UMV4oKkNAEuYHrXdXSbpzBC_dFsVNsLuw9cxL6RxcL7Laz5OZi8NIMQGy2lGLawebAOW4RyJiK_74MXdyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7bbe8d9a.mp4?token=WgrN9o0hFsnGAIrd_Iv3AaH97JYDKRFAPJw6ESZ8vzV24sLm07r2UQuLRfNcna4fJ_XbeT0IP-36-oyPSu8cC5XYOBZKUJ83UrAwQHMY6o3-BcK9vQCqf9Gn2hwkVojM9B2_Pn9yChApAZ8hOPfyhZhmV9AWla3M6o7-3eVyh0Z-LSaEwtmIF5c1J0MIDfyWyKd_EoP0jQlJoHZB9XiOHaFxqcXvQA_4GRijdWSzz3GbrkEXA_kAh1lcBPrXfVRhzn6UMV4oKkNAEuYHrXdXSbpzBC_dFsVNsLuw9cxL6RxcL7Laz5OZi8NIMQGy2lGLawebAOW4RyJiK_74MXdyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام موشک‌های رهگیر پدافند آمریکایی و حرکت آزادانۀ موشک‌ها در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/439546" target="_blank">📅 02:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439545">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فعال‌شدن آژیر خطر در بحرین
🔹
منابع محلی از فعال‌شدن آژیرهای هشدار در بحرین، در پی حملۀ موشکی به این کشور خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/439545" target="_blank">📅 02:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439544">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار از سمت جنوب جزیرۀ قشم
🔹
برخی مردم محلی قشم از شنیده شدن صدای دست‌کم ۳ انفجار از جنوب جزیرۀ قشم خبر می‌دهند.
🔹
بررسی‌های خبرنگار فارس حاکی است صدای انفجارها از سمت روستای مسن و محدودۀ دریا بوده است.
🔹
هنوز گزارشی از ماهیت این انفجارها در دست نیست.
🔸
همزمان رسانه‌ها از فعال شدن آژیر خطر در کویت و وقوع چندین انفجار در پایگاه‌های علی السالم و عریفجان خبر می‌دهند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/439544" target="_blank">📅 02:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439543">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
آژیر هشدار و صدای انفجار در کویت
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/439543" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
آژیر هشدار و صدای انفجار در کویت
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار در کویت و شنیده‌شدن انفجارهایی در این کشور خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/439542" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439541">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqSEIBWbhw5geG7tbyafj86gQmpb1bz4o93Et7vkTY6p-RsN1VGzh08PWQXGsw8JqX1zMK9GW2-tgopoORKgath48FifdfGPBZ8_Ettzc3Lnxr2HDsVLdgD0LrVhOoRf_MxhrPneDFiqUoaMw6fxElLtSvk7e5KX0_Q5y8tnY0HTH2--K7q2OSfFdEqH8qPWGVdSOQFHUB_N5FA6ATS1FrTKmV-iQPyNNVqFrGBvpKUAdGIgZFOBltRlZm3JI-GH0fGIuOCf4RaC8lNb8KPeDbOO3YaYLLDnL17e73OTwFkcV0EetBsOMQXlJaCgor_M43_5gPiC5zM8V9CCX6SA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینۀ نهایی سرمربیگری تیم‌ملی جوانان مشخص شد
🔹
گفته می‌شود پس از استعفای حسین عبدی، کمیتۀ فنی فدراسیون روی انتخاب قاسم حدادی‌فر، کاپیتان پیشین و سرمربی سابق ذوب‌آهن به قطعیت رسیده و به‌زودی به‌عنوان سرمربی جدید تیم‌ملی جوانان معرفی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/439541" target="_blank">📅 01:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439540">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
حضور نمایندۀ ویژه رهبرانقلاب در منزل شهید ناو دنا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/439540" target="_blank">📅 00:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439539">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار در مقر گروه‌های تجزیه‌طلب در اربیل
🔹
منابع محلی از وقوع انفجارهای متعددی در مرکز کردستان عراق خبر دادند.
🔹
رسانه‌های عراقی می‌گویند که مقر گروه‌های تجزیه‌طلب ضدایرانی در «دره آلان» هدف حملات هوایی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/439539" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SuBFOhS9WRRhr9ipZ5Tvggpvo5HJ5WVb12837D7re-PupnrKNzYAvXAsGpvpo3nZYAvx_x62H7RJKvQQI95CoSSOQcM0zZnskV2mOtYEOZEbrxyq5zOzbD8tu2ojTRIzEsIT3i4k9GJG_rQ0wGXWlU-t18_vODgCcu1y8XXnMctPCn_koim2s-NfggXCq02dLnBwj5i2vdLLMJxgb0CPRNmimzZKeXKiT1i51hkqBZeic7QS58npKmerjNqRQbEgPLhQQjh86GP2lm7CklJZCntRSUOg_aZYWRq3HmgIVdNNHH8fR68CTPVcGdX7U2NAQd_-4S81hGw69HLjQ4T3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je7H35bL9UEwg15poOKL0wv2B2uNP8UKQjHv7D2GKvUJnG-jU5mnm92AxsyGT96J9SthgniGEdGFQ3ol9OVBF3KTKJRgPQ-Ycf6_uxvXpWGy2IYWgv5J6WaaWU-xzrpiyFY8FjwP7x5p4s265G-ccWOMl7HxqdDOXNk9LjSlOJJ2UUiluN-iImdsIhr0mQPOTQ1coMSh54Pgg7ujv52zCWYp_tsnG5L2YNZpiA_Tt_cqLNN_wB4znMt5NF95Q2aB3Zd3HjP7JZF3p6mQ1tNzyXqwtLTnX8FV9XWkqw4e8SHM2Pdnvl1y5_HFHXUm0cQoNCBqCIeYalzGmgBMz58IbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt60W-1YOfZnPvOkAWjYdfy-l0WE3wj7GLyLXx4nuX_EnPiVdwbN_ayCwq-tH3WBbg9MgesqPCF8HY5sghfZSliHM4Ii-okpOrTbfKVW8wbm3z6hsjlx2qWKy8Q739-clbxsNQzf1nVfqizUm62_huja_m9fPNXero7RgIPRRZ9zSsw9jyl1VRopEd8m6CEApqLhBG4lgM8ze7iiMXrRWsoZm8i8A_8uXc8ruN4gDREPBjqxOdybRP9_5I-RQMd7s1n9DoDLem-7Fnye5imZvsizy4i-nK-wMoPlm0lw6XCBq3vXMfdPk7DyGYdt0e7TnGR1ztBE55D4cVUNO7uK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecc_Dt_XJBHkr7lpmotRtC3R5Q_Ku-SnIeB1CyCRuLFnaH5BpQdkNbWTgNTI27q82TKQE-NJuggcOSinZFGTAmBuiyTR5qUsC6c7EfqfHm-GJCScJT7tjStR-Qck_iMutYFc3az64VK9EAw1HqU8RDIU8lUz9FiLC02QoCwCCOPtwdg3N3THtSMxn66TEdC6aIzb5XW7S-PpqiP4rIu8NcooK8BV4nTEKoQpUyugwalUZw1rNFAQTwxW3LghDXT931XIiMXS2FjgZT4gsFhvJBYW8uhS0sPNb3G0VxqnXx6H-qMYfqcmWfXJU-YAXkgUUvpc3GpF82mN00yyYCWBuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9rbJDWos4TXCypbwHU0MEl7Zauq_k7vxF7Sm9n0C9S1PjdCIQnzs9khVhuOfF3Opw2mKBXnR9nZuHxHlDaxa1SkKycpfm6G0RJ6QCo3GRWpDAYSeEJ-BAb2M0RWXkIb6f5IwswBXWC0Ja4ILopslcNIgZk2sVEN-iTvG0nTTJVuhvQPdA7ihPTT2EdM3o6Gv1lsddEIyWx_mlBlEDHL5l58nB2Xe003hix9uRahAPuLkAXHgzgZ7WJchNditSsbz15zUjWwSwhINKmQPqlxjhi1L3d6x3EqrsgoEgyUHgIJtEtbbGbAJfe5j8mrI7O6uinJ-ORYNLPWCU6GUDds1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-lbJ0vccx9xWN6XHv2qGxbs_0W_us9uBnbGFO1YLQ6A9QV21ZVBzIDfPKVYBhzcAR_1Pzne5GcvD_BR5U_LVm3lUlRUdNC8RFUhZmEXq14smDNtuoyj2i7IRMGsH3wkW5tyCzdag5jfDssUO8HJp1_UQfdwt-Zw68um7BaF2t7kLM1j6kunamGiA_j0uHcLcFTGYT9DEpIkbi0DRGsDggqRKMyLOUETUEWWdj1nqF6_io7X-jYNSsXALmVopeyuocH2jT378Z8szCHtMLa2fYy1SZ3qR5sOhTUN_Xczle9kOz1-WNC0OSCAn1wVm0IOglrot86ixnBqS1HYO8kQJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۱۳ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/439533" target="_blank">📅 00:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439523">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9EhY4g22rrGQ8I_bTmGDfMxtRbu-9yg6hQBeAnv1XwJD0uKK2EbHMUGmzJkc9PLW8TXEdlgxodyOf2TTetpnltAOvS4JLZsBblL1s_Z3EWK_CMAOH_BO0JITY2VxGgFM0O4-TjoW9rr8pku87Rxk3Q3889t38B9WK30fClNQGt3hBzjJnhC39eHvs2t2390b3UY_t2411eCYHpeHmHt-pqtLO86dSPLdQ409JbDdnhIUb8JpCBkqwVR1FJbH4JF9cVLtZS41UGFRpqm1Z_J0M0oHeG1YCif-iD4GdWaGGuQqR5a-uzDW0CUhnpAHr-mOz5Zz5Dp0XXKRZj1v2FLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mO55ENiPR3ZGGsvN4eh4aFIeXFZFXsMlZZCHooSrznonUc0fO7jtWTeCaumQ2kHZWaaoFaKvtE8DM-oP0F-DuQb1FM8VUAMVwbgOqhHYjJnMneUyMpy-iI-cmRI15NOsK9FD0rhxfzqFsr0L58j6Ybww61iXRYBUlRmeYUDuJPZDywx2reCqOv1oSdUUpmstL-91jtEbSM9P-RUTemIaEWSSMiP4hg0JwaZUrAkroBJN_U7JRdaP3JX7bylvTB4UrgLce8tJ8o0z4U_n2cnxWg3ahwxyrM5wNhFvuqB26nrLaSRXK33KcTCRRLWH1p7Bw9SLJpZqwL1hdS2_Vn6GtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnMYoEtECn4VN12sQflE-g6cUt2QaKZUVwUjdfRbusDMYnEECXXT6GofcNnO5QUJLlDO37n7joyW_dsh0CVwBxf35pzkSMq5KO8d8nWkoh5rqJPwOUrrLOnq_nbS2o1RsO--UYsmk08QZJZlVAVmER1wd_11Rp8UpZEAhFJpkPfR6vYfEm1pMD_s3E2knDnScZmz7DflTRoDZ8yu9sp0UFBU0EXl7pZ2QnvTubeA-BDMe-Sczhc8rLK-LvSq-LdD9qc4tHNu9n7v9uuehGyOmghvFwggIOYfICwlpanRgWH-6f9SnzKf3jQ3UDeQmZ2C8dNu4MEmVOJ9cg-WXknzng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c0klL_m67QConn7WPyupal8PvSHRiqaWhHtyj8hBmWf-0usUVnGWeFm-v3jiNNgvqkxjQlM-dI-mL7BnHCKK3R1ewQu2DjN5ObF2UDW67dOUHADzMWLDY33jwuZeyRz5hMW13db7ygqg2SuaI1ztSxp2ctaRHP827Sw9oA0lwNppPK0HJBxvL8xsK-XACJF_QxduPZiSAleaTRc9Hs_JEb8aumtNiTp-QaDWZsSneT4exOfjjq61cDo0pOieJmgtuRK9q5ehxQ1_F8N-B03KFhVuZYPOSRnUNG6-1uHT_Wd4ypYmPiOjbdgNg3DGdiB5JJFFD78VhoZzfG_jYfyStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7SQEM94LtOLlvRRPS3yhNsB2N2kdOd9oCupXnhR3W1--WlN2LQZach4KNq3Xjc3oORBvqIUCxp2IzqJKngnHMTg14S88BzU5GdnBHC5qWPKR24uzKd77ytcMmKB-IIG86hb0eJla_sGe2hB0vyBWOfahF_eSuQDiEbfpCDc_otxxOMJDRsOkBZk9ftmuCF0QgwRzOFnM9jGgrWM8AkgCPQYI6bn7VadkxP5Cj_ogbvtBEps-H7v0Tlu2sVZXCbvP-0Ny8V7Ud3Z3_TdIt0GkUHt5ZTyfnGdaM9H88wpZ7CJH6cvjxHDWq5rBk2Et0UQbRc34YfvG_PF6G7sD_9ehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbU7xxNfVootKJ6B-qpvR6jeaSF-yDjd_6o6L3NqzBS4RXjV3R4ZEOKM6wpuxlC7T6SeD7bB9q7pStY5jlD-iE4HNiCYrBbqF38bvZHJdVSgXA_slCRFV9tv3-2tR6zrhu3bR8HCU7YJUV0omZZin2inpjTqRGZl1XuHf7JLpPi1tIJIDvONOsvrJxQWDM8Dzs6cQ-6fTOa5EMlyOlKneeYDHL-qXQ6b7s7rt1YNHxGsGc9NK35H_kKRtQ1snwgQKPsuxyxIrtdZcSZkV8vBV6mA7Bw29q81KYIbjQyEuIsKqW_B-cyHnzI_MOCUh9SbGhadZaGjWzHn1YkrAVAQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P840oNUYFg7DBRGjj47E_j2KepzIbkDrASi6bmqqJx6JpYaJHDE9MLYz5Lhv7o4AZbbvndxrnBy7Xy69OF1AYmggl3Zw9CUgVoig3lJSgt-J8URYI2CrYIvwDJ25rWQHwwLZYTBb1nBId1oBhT-xc0lvLZGRGavUbUdrA6oONQY51no_NNRs83bEM_R0AVaTrUzItPGv7gfuUy0Stkg3m_UVS-uma-MXu9ysHe9VDMAQisnB7pRWGTtjpFYF9HIS_ucrW30MlF2_eqOF6p2ywzZ7hmPMNjtWoa-VYUcM8OfmgR-LXfWdiEf8DB7fwa269ZqvGRHOYk_5gWUyEUphvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAib7V9QZywksID7vgmuQ4nGUqkGC0fSbAzwOxDXkzueScJS--dHAzfi4wglAYuajqag0ufhKRh_xlhvAwiXWwKBECgHeybHaY4TR15gopABPc2cGROA2D21aT5s4nd6kKu2S0x-ishPac8LkF7_tp9S4IkcbxbmGCUhxqv0mrvtP9fpFLLJQjwDL-ZM0PawkivjtHaIT3MbfOGNREeefrtS6RHnBdL2hpoHtFNkh6IkQdB-M6y1thKLy70amrxLf5WgV3UBv4-gIewisq9wXXEwcPmY0WKL1fmrqFTI-vLZAkML6Hoe9XSbgm9ZuFT5Tq8FoLpTckGRx2dYHHow7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGpUrE65bblgO8QtCy9A9920E17EtjiJ7UqKQUB5So43tPcb5MTxp5uwf_elXBen34vELUasUjA1EHVmZoHpltkcuRuR35w2cDTcbKbu5x8jfbNuTjG_72s-u07RPAaiehj4XjqnAVeZe9eHGZSr6oQ10JGPX_gjw2Xnu1c4YPal0UaFG-PTETpCq2uHSvXPQRJDPwamNyScslwTLWIe_-wUXPKMsOLbEXsr7nhmjAvtlxJFAXWHDcdGYmg2742t7R3Hhbq5VV4E7d3JAWdlPJE7xS7Qk9rjTUIaXBOjrULO6NW_mC8TCwQOJh4O5aZrp2KHybA27usFfL5ulA6yQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_-msPZ1GKbiexb8r-L8_M-heVQ-tI9yeIl37q-PqZlVBS1ozi4cMd1yxgRY1u2DMKFUJ_n5Ux0ZzEmVmoAQkZHTPPcho9b_ACOtG6edu49z_5rnj-FRLhs3sdxAQ5U9wrdKZTwTSx7_9XwlKLhF4KveZrBINhRskWpNgA3EhJeCYV_DRfU00aJ4k2sVEWVmApQ9Jmbcq8lHvgiZ1fQITW4j4akd6vMX-IjaZS4G12ZvpuitFuCu11p12uB1rL0S3HvqY-wyWkAYSUptXvDIOlODhMsILyIMbaQ8FUYJZc6_WheOf5qsNsUiGaC5rQdbkNmIe33WFM6mJy9m4qCLsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/439523" target="_blank">📅 00:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439522">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjTVEeFXU21PkUIgl02wyBvEI5BgEReC_5Jb5-Q-V8Mf81I7za3Q7wH4V07mFNgopxnUX-otG_cKtV4FUBbxNzyBZnWp2TpapRY8deO8524prhk9HrcVO-EknKzhrHh_mriI484L1l1c3G_HceemfNlr9j4kSBVPqLYNopy60B62-Reo8DymIa9K_PWn80LnRxpDjtUIFDm7oZzANvlm9n3Py7oI0RQcJ1AedSSgqv470aTYFY3JK94pKY5sj5ojmHqaCzLKZoyutiExxkt5sbIt7683Mxnbk1RpMrAJeNe_OBYJETHyybS6cqJ5azPzjC4rqjYwIQ6ni_9c9RPu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویزای اول برای تیم‌ملی صادر شد
🔹
رسانه‌های ترکیه اعلام کردند که ویزای کلیه اعضای تیم ملی فوتبال ایران برای سفر به مکزیک صادر و تحویل سفارت ایران در آنکارا شده است.
🔸
علی‌رغم صدور ویزای مکزیک و هماهنگی سفر تیم‌ملی به این کشور اما هنوز روادید آمریکا داده نشده و سنگ‌اندازی ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/439522" target="_blank">📅 00:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439521">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81be34d97c.mp4?token=LvD5WkMnjODSHy2eC4X_0iA9fM16noFgAhaQjPtvjz1Jj-5lZRkm27b1mLrh5x7z8KQ3QUitQd9osZoLvUNPfH0KC8gYIBlw3s1MTbi0fMDMvI7nVIML9X4oBo75SI1ZSmMlBP3JM2REQdk5YEZrfIKj0gOwm5dnt7_cSXmNdts9NXd7di63cepxSZgSqvpwrXyoJ9ewk8SBOtwRQXJaUaN-9MwEUrnV1woWM21k__HCHaiQcrAuNpCzsbMnCp-SzrTrvxe9URjVB83_ivzxsdylQDVS1_e8-FHh3axTkxSUMIj4c09voJSpnPSDi7gZrr_e7Ch9wQOJbmCihVLe3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81be34d97c.mp4?token=LvD5WkMnjODSHy2eC4X_0iA9fM16noFgAhaQjPtvjz1Jj-5lZRkm27b1mLrh5x7z8KQ3QUitQd9osZoLvUNPfH0KC8gYIBlw3s1MTbi0fMDMvI7nVIML9X4oBo75SI1ZSmMlBP3JM2REQdk5YEZrfIKj0gOwm5dnt7_cSXmNdts9NXd7di63cepxSZgSqvpwrXyoJ9ewk8SBOtwRQXJaUaN-9MwEUrnV1woWM21k__HCHaiQcrAuNpCzsbMnCp-SzrTrvxe9URjVB83_ivzxsdylQDVS1_e8-FHh3axTkxSUMIj4c09voJSpnPSDi7gZrr_e7Ch9wQOJbmCihVLe3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای نامهٔ مهم امام خمینی(ره) دربارهٔ شروط رهبری که در جلسه خبرگان سال ۱۳۶۸ قرائت شد
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/439521" target="_blank">📅 23:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439520">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPWlYh5MAMFSNi9X4Qrf6joYfAA31hEIsbs63io0qaIaiRY_KBOA5rols4Fi0CshYQTvyT-hrtZ_juPtgB6N19ukVpMLMOJ5Vkn1Wp2qvwJ5X1fg1DPwKH7eilMoF-Vy2LDDyXx0Q5b0u8t2hItCTINbprkVunD4pAGu1DfyZ0dysU55o-TIoQxcLVVoOf6N-hV4LgbCljwaTAUnx4xPRStE2C_jAXU0giGrm0ufHoNjOK95clJbFDQXJMJyaKkomlg8q9-RmfCA1Ohp56jxaqSRvAnp43Ooj6TEDqkdd-VlsMggoNyDNDMTw2ke4Lgv5ymiJoxpqLcj4SlWmyYm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش‌های سیل‌آسا در راه ایران؟
🔹
مهدی زارع، کارشناس زمین‌شناسی: ایران در پاییز و زمستان امسال ممکن است تحت تأثیر «سوپر ال‌نینو» قرار بگیرد، پدیده‌ای نادر که می‌تواند بارش‌ها را به‌طور چشمگیری افزایش دهد و خطر وقوع سیلاب را بالا ببرد.
ال‌نینو چیست؟
🔹
ال‌نینو یک پدیده اقلیمی جهانی است که با گرم‌شدن غیرعادی آب‌های اقیانوس آرام و تغییر الگوهای جوی همراه می‌شود. این پدیده می‌تواند میزان بارش و دما را در نقاط مختلف جهان تغییر دهد.
🔹
گفته می‌شود امسال با «سوپر ال‌نینو» روبه‌رو هستیم؛ نسخه‌ای بسیار قوی‌تر از ال‌نینو که وقوع آن کم‌تکرار است و آخرین نمونهٔ بسیار قدرتمند آن به حدود ۱۴۹ سال پیش بازمی‌گردد.
چه چیزی در انتظار ایران است؟
🔹
افزایش بارش در نیمه غربی، جنوبی و مرکزی کشور
🔹
ورود پرقدرت‌تر سامانه‌های بارشی مدیترانه‌ای
🔹
بارش‌های سنگین از اواخر پاییز ۱۴۰۵ تا اوایل بهار ۱۴۰۶
🔹
افزایش خطر سیلاب‌های ناگهانی، به‌ویژه در جنوب کشور
برای پیشگیری از خسارت‌ها چکار باید کنیم؟
🔸
لای‌روبی رودخانه‌ها و مسیل‌ها، مدیریت ظرفیت سدها، تقویت سامانه‌های هشدار سریع و پرهیز از استقرار و تردد در حاشیه رودخانه‌ها از مهم‌ترین اقدامات پیشگیرانه عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/439520" target="_blank">📅 23:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439519">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
خزانه‌داری آمریکا ۴ فرد و ۴ نهاد مرتبط با ایران را تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/439519" target="_blank">📅 22:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439518">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba4182118.mp4?token=krseh7HGOq3D2T4P1Ejs27Wt50DEpFRb9IcsYjdUQO-853xfza_FS5t-cCUfN0GbnkNw3McsmbfTC8aia4pIEQ5MR-Pb9RogYYbYn5nyjOogkpP6eas_7NbCQ0EnBYRuaqHIALTI58YKK09Th1jvQreKd8FVi69Ads9-MtAeZ08O9AMbXg6IklZbzwHrJcpRl1lmhoVD0sK4_I92Wq8KspXTHgaNMFcaaFh0maqbL6iPn95XJ8Qs1LbeqJf98ObsGsjICGyU-mq6-3knmdCUfe2XGVNsW4L0CW3XKHWiURObthBvU7HQqIER9GIDhNg6xNcUi4673tNqy-bF3WKn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba4182118.mp4?token=krseh7HGOq3D2T4P1Ejs27Wt50DEpFRb9IcsYjdUQO-853xfza_FS5t-cCUfN0GbnkNw3McsmbfTC8aia4pIEQ5MR-Pb9RogYYbYn5nyjOogkpP6eas_7NbCQ0EnBYRuaqHIALTI58YKK09Th1jvQreKd8FVi69Ads9-MtAeZ08O9AMbXg6IklZbzwHrJcpRl1lmhoVD0sK4_I92Wq8KspXTHgaNMFcaaFh0maqbL6iPn95XJ8Qs1LbeqJf98ObsGsjICGyU-mq6-3knmdCUfe2XGVNsW4L0CW3XKHWiURObthBvU7HQqIER9GIDhNg6xNcUi4673tNqy-bF3WKn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام جانباز معروف جنگ رمضان برای آمریکا و اسرائیل  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/439518" target="_blank">📅 22:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439517">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b686bebf.mp4?token=pO12gIbD3a2_mBTEDj-7bPkhnNydPa-vfXsHJ-pqkdf74HjTb1G1Yfm5FoWWk-a5Wly-5IrRAFZSaGkKm7hbJGHf0et-d7iuJvJBpm-U0qvEpR609hlJBr5UU1Ml543Yddjbl6v_xWra8t3lBDue8KYvZssw0bjwiIm_4hJjT9-N3qT0OArxM4cPyDJCMvdkHVa9GXraN0PJ7WRoZMWaeYIjT3A8Cg_vW36U7t3cNk6TMy83-qkNc7R4NkRHhbxqAYNG_dwId1pXGO9M0C5Q-E-QPNkTE-VrOIzW0Y9wWBJc_PKiDYdV4RX-pDkfHFNvUmkPJ6jHm8PPSc6qoMjnTCryVGb8xxl5D4-bKivQRwvQWcs8NduHn6qWWKjzujkHgzqMgEvdPStdBcGCaglcqGgxt0avCHH3KqEDdbLXBNYhcS6g4z8PxNjmzMv1LvrbAkng33zO8fuU41oy4dcXsCHwep0gQsd4i9n9CmEAZwh0vnpYN5R9BLQKb_7CPD-xr5l8Sb6himY2ojVzcIoTLJf437IRiHdKJKjyZHxMwxlGee3WrZsEkDR49dN9OySSbBnz91ETy4DbTpxVw0Rbu1MkFrigaOYPVtxSbGL5pilhsbPubedwtAkE3IM3LtzgzsvKEF6JYxQ0gVi6vzXXwxHThzn_AQTD59SJ8BpYvg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b686bebf.mp4?token=pO12gIbD3a2_mBTEDj-7bPkhnNydPa-vfXsHJ-pqkdf74HjTb1G1Yfm5FoWWk-a5Wly-5IrRAFZSaGkKm7hbJGHf0et-d7iuJvJBpm-U0qvEpR609hlJBr5UU1Ml543Yddjbl6v_xWra8t3lBDue8KYvZssw0bjwiIm_4hJjT9-N3qT0OArxM4cPyDJCMvdkHVa9GXraN0PJ7WRoZMWaeYIjT3A8Cg_vW36U7t3cNk6TMy83-qkNc7R4NkRHhbxqAYNG_dwId1pXGO9M0C5Q-E-QPNkTE-VrOIzW0Y9wWBJc_PKiDYdV4RX-pDkfHFNvUmkPJ6jHm8PPSc6qoMjnTCryVGb8xxl5D4-bKivQRwvQWcs8NduHn6qWWKjzujkHgzqMgEvdPStdBcGCaglcqGgxt0avCHH3KqEDdbLXBNYhcS6g4z8PxNjmzMv1LvrbAkng33zO8fuU41oy4dcXsCHwep0gQsd4i9n9CmEAZwh0vnpYN5R9BLQKb_7CPD-xr5l8Sb6himY2ojVzcIoTLJf437IRiHdKJKjyZHxMwxlGee3WrZsEkDR49dN9OySSbBnz91ETy4DbTpxVw0Rbu1MkFrigaOYPVtxSbGL5pilhsbPubedwtAkE3IM3LtzgzsvKEF6JYxQ0gVi6vzXXwxHThzn_AQTD59SJ8BpYvg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام عربی مردم اهواز در حمایت از مقاومت لبنان
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/439517" target="_blank">📅 22:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439516">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198b8ee713.mp4?token=AYi_9TqAc41FPgcakw-lyq22B-Gt3GSOt2aod-DJKOcaSdGLpBg9JOpeocSxvGapUx-H7ws61isqxYtUuV9MWhqUNrW2vZm_VnZMBUs7NoqtHFP3mJD2EsIVoaLzgkvI5VQ4vf4uQ_ti7k0Tm7R8u_LwKtnQpyjpb_PDC3oGp7WlxbaLx4NntAKJKSpl3KYlkfL6cvA2KLDzlYLKFw8LAMP1K0qEctnfFLy38i-xCxkSWaYHutV-B0aRKDV-i5iwBKaOlNF7Cl--8tQS5Gi-cOQWPNrdfxsH1dzHFm_fJ71ANzAGuBxi5SAu4_Vu5yctUJFn28gfiJkCwMzKIGhhlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198b8ee713.mp4?token=AYi_9TqAc41FPgcakw-lyq22B-Gt3GSOt2aod-DJKOcaSdGLpBg9JOpeocSxvGapUx-H7ws61isqxYtUuV9MWhqUNrW2vZm_VnZMBUs7NoqtHFP3mJD2EsIVoaLzgkvI5VQ4vf4uQ_ti7k0Tm7R8u_LwKtnQpyjpb_PDC3oGp7WlxbaLx4NntAKJKSpl3KYlkfL6cvA2KLDzlYLKFw8LAMP1K0qEctnfFLy38i-xCxkSWaYHutV-B0aRKDV-i5iwBKaOlNF7Cl--8tQS5Gi-cOQWPNrdfxsH1dzHFm_fJ71ANzAGuBxi5SAu4_Vu5yctUJFn28gfiJkCwMzKIGhhlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر خارجه آمریکا در مورد دستگیری یک ایرانی به‌دلیل تلاش برای ترور ترامپ
🔹
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439516" target="_blank">📅 22:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439515">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=K7NSSIh5Q2FozSHdnodZCR-wC5lK5OsYhEl8nJTONyIJf3uSWxfe-huxtfWrOgXxVuDqSd-gM7y5KbMozL6nY7-Gb2N8NVq29CM0ryoOWP3jKJkwpTyCs7-3OkFZsiuxoxTDbKvnz4XolQ2rqcW3TOrqokJ6e9CRxLitStgSn_4wquUY5KUVYQuDxmUQaeHPAQ_v6GKskhazuDfG_6XForAEkY8sPBQdqXLWUgN7YStpoiYnFctcAnLLIHqLH68z-LLYn3tLOmB5dhGexEWlDKi0XPGwtckunya7cCq5CdaEBO5Ilu3jrv2tqZSe_yHYo5VMKL5lB7EBCXZjgzs_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b480a5702.mp4?token=K7NSSIh5Q2FozSHdnodZCR-wC5lK5OsYhEl8nJTONyIJf3uSWxfe-huxtfWrOgXxVuDqSd-gM7y5KbMozL6nY7-Gb2N8NVq29CM0ryoOWP3jKJkwpTyCs7-3OkFZsiuxoxTDbKvnz4XolQ2rqcW3TOrqokJ6e9CRxLitStgSn_4wquUY5KUVYQuDxmUQaeHPAQ_v6GKskhazuDfG_6XForAEkY8sPBQdqXLWUgN7YStpoiYnFctcAnLLIHqLH68z-LLYn3tLOmB5dhGexEWlDKi0XPGwtckunya7cCq5CdaEBO5Ilu3jrv2tqZSe_yHYo5VMKL5lB7EBCXZjgzs_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعای وزیر خارجه آمریکا در مورد دستگیری یک ایرانی به‌دلیل تلاش برای ترور ترامپ
🔹
روبیو در جلسه استماع کنگره مدعی شد: اکنون ما افرادی را داریم که در آمریکا به‌جرم تلاش برای ترور محکوم شده‌اند و یک نفر هم دیروز دستگیر شد؛ از مأموران ایرانی که درحال توطئه برای ترور رهبران سیاسی، از جمله رئیس‌جمهور آمریکا بودند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439515" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439514">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265219d6d0.mp4?token=pGJF2tG_g9ydN7juKestRqDfkmQVCp1KNIjK_rJ-zbOq-vmy0zuveNY12nqOIyTJOXtdz3MpSZNhm6ocWs4MbEhhag3AJHlddu2QVsdwJaheuj1omBShZS4xXRvoOK7Sc2zTt7FiJ-kEumPPacmm_NDlDNzeShdx4Hxt_b4C6xOKj4SetbQ-UEDUyBpxsE-Z2KAw5ZpwljrwWcH5ji4t3-A7fL5KmjT_jOT_9EaG8yhiTymjk7VurPpVxJuOX_SLuxpsfyK9Yioh3B36KH5AjO7K2xko3Lw8VPbV-8rIcvzqcPvDrzaExf7MpqWBL7qL2RH9HZtCXRGRrYrIhk_fHl4XPIqqobIQLoAiPeo0YTB0W3pKsiUK8BsIgWAvlzBlghVEiT7ZlvpUVrGRXeuVbLfjsiMY-6iPSwHFZqnPaY0eHiKEnt7XCwDLRHZq4WTQ1vvXtuWzVpgvVqwk32wMrVN52nbMCCUFtKiHECMfgWLi1MMYTT98VETN8VB7cq9OpWRlbkKCu3Jxh_ZX6VIdKmrb__-44maiOOpexIgoQy3yxh8AbX9LEGm3lDW34MZTiyGPi0jvJY_jiMnnwSGrQ7JDyfISHH8Bbx_xfybb5m5hV75AmqfbY45tH8_tsweuJtIfdqn2goApouhdWLYGebWSVUebZGFKQElj7qefvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265219d6d0.mp4?token=pGJF2tG_g9ydN7juKestRqDfkmQVCp1KNIjK_rJ-zbOq-vmy0zuveNY12nqOIyTJOXtdz3MpSZNhm6ocWs4MbEhhag3AJHlddu2QVsdwJaheuj1omBShZS4xXRvoOK7Sc2zTt7FiJ-kEumPPacmm_NDlDNzeShdx4Hxt_b4C6xOKj4SetbQ-UEDUyBpxsE-Z2KAw5ZpwljrwWcH5ji4t3-A7fL5KmjT_jOT_9EaG8yhiTymjk7VurPpVxJuOX_SLuxpsfyK9Yioh3B36KH5AjO7K2xko3Lw8VPbV-8rIcvzqcPvDrzaExf7MpqWBL7qL2RH9HZtCXRGRrYrIhk_fHl4XPIqqobIQLoAiPeo0YTB0W3pKsiUK8BsIgWAvlzBlghVEiT7ZlvpUVrGRXeuVbLfjsiMY-6iPSwHFZqnPaY0eHiKEnt7XCwDLRHZq4WTQ1vvXtuWzVpgvVqwk32wMrVN52nbMCCUFtKiHECMfgWLi1MMYTT98VETN8VB7cq9OpWRlbkKCu3Jxh_ZX6VIdKmrb__-44maiOOpexIgoQy3yxh8AbX9LEGm3lDW34MZTiyGPi0jvJY_jiMnnwSGrQ7JDyfISHH8Bbx_xfybb5m5hV75AmqfbY45tH8_tsweuJtIfdqn2goApouhdWLYGebWSVUebZGFKQElj7qefvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حزب‌الله رادار ضدپهپادی رژیم صهیونیستی در الشقیف را با پهپاد مورد اصابت قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439514" target="_blank">📅 22:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439513">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4da4fde12.mp4?token=I8rnbN5PiTRG4ERVloXUTJPsFaj4G_UTFvIgD92_aD0dVf0kzHmuiPOoOE3mjEt10zwUuke6xkAUr8IBKsWXctgIZlI434etYa6HjWr_xZn1Z9cebnBsn3DHxuwdmwqob7lmXqX9_8vfPh2E2j3Ej66GmTEBmEhogx8-4SVRt_Diuw78HqwUmBSZZ8n73J7ZX891e5LYjBqJHddglYtrOQ-42C0dv-kz5fG7i3zE_GBOph3J6WtZ_oBAaEcx07_z-D6jhOHOYzbc9ZduX6qqHpH8WzNLRUuuGIBWZgv2FsFccSZIYz3DLp_BmTHv3LuJGADLuqjQb8XXjk0nLpPQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4da4fde12.mp4?token=I8rnbN5PiTRG4ERVloXUTJPsFaj4G_UTFvIgD92_aD0dVf0kzHmuiPOoOE3mjEt10zwUuke6xkAUr8IBKsWXctgIZlI434etYa6HjWr_xZn1Z9cebnBsn3DHxuwdmwqob7lmXqX9_8vfPh2E2j3Ej66GmTEBmEhogx8-4SVRt_Diuw78HqwUmBSZZ8n73J7ZX891e5LYjBqJHddglYtrOQ-42C0dv-kz5fG7i3zE_GBOph3J6WtZ_oBAaEcx07_z-D6jhOHOYzbc9ZduX6qqHpH8WzNLRUuuGIBWZgv2FsFccSZIYz3DLp_BmTHv3LuJGADLuqjQb8XXjk0nLpPQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مردم در میدان انقلاب
🔸
مقاومت مسیر روشن ماست
🔸
لبنان همیشه پاره ی تن ماست
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/439513" target="_blank">📅 22:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439512">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acaaf9a409.mp4?token=BfFmS9f_pMgmo66NLZvdjTe0WQ5qgiuZmrilb3qgnwDxitJU1rp0Akd1AvItRQyr4fG7vrg-luP5J2UEwsAbLnndnomQA0Jwa7VX5BaiArexSzkqp-Aqg5vbCEO9FmSNW9T6QVnOBeVkxlU-pwsNjJDZrejZoroqWUrlyeo90J56RHCFktt_muJVrImNc63CnU2IgKCyNgJwl9fTN0ySteuyRNLCIl2q3mpUbc1KmR43-f7FjCyBjGKGeHr6z_sAeT54jF3R644nqn9_3s9mOt_8Yd-p7q9Ca7i7RaHFHuQsiZaL96UGSAJHPTVgIKLPG31FXm8SCqeuur9-w1XjPyt99pHUWPdT5egyZ99p9XG10IiQdwtRbYQ3lc815AhFyglHX41NO6LhlxrAVfC4GHuRv3OzTdO3KFGNH1l7ACJiImOeh-iB-x20yddmHCpV5LxBfI16llhDNEF2J4X3JvKZ73fsFuAfJghiwitU6iWDHpIxSgOdSzwsyeRirU2LS7R4xFRR83pK7BVOQNhdGQ0Ruo1ToblUK-E-IXsxBwGCrDBUvon6xKYktYwLbGl9rQZ4FxJ4e6kynTu3NL4Li3CnYbSUYuohsPvxEi59qI2-b82pcO5MDH3dfD0Er9OAEKiFZqS4UYysZX7vyMYLIgB4KYOnargYxRjR-nDrsG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acaaf9a409.mp4?token=BfFmS9f_pMgmo66NLZvdjTe0WQ5qgiuZmrilb3qgnwDxitJU1rp0Akd1AvItRQyr4fG7vrg-luP5J2UEwsAbLnndnomQA0Jwa7VX5BaiArexSzkqp-Aqg5vbCEO9FmSNW9T6QVnOBeVkxlU-pwsNjJDZrejZoroqWUrlyeo90J56RHCFktt_muJVrImNc63CnU2IgKCyNgJwl9fTN0ySteuyRNLCIl2q3mpUbc1KmR43-f7FjCyBjGKGeHr6z_sAeT54jF3R644nqn9_3s9mOt_8Yd-p7q9Ca7i7RaHFHuQsiZaL96UGSAJHPTVgIKLPG31FXm8SCqeuur9-w1XjPyt99pHUWPdT5egyZ99p9XG10IiQdwtRbYQ3lc815AhFyglHX41NO6LhlxrAVfC4GHuRv3OzTdO3KFGNH1l7ACJiImOeh-iB-x20yddmHCpV5LxBfI16llhDNEF2J4X3JvKZ73fsFuAfJghiwitU6iWDHpIxSgOdSzwsyeRirU2LS7R4xFRR83pK7BVOQNhdGQ0Ruo1ToblUK-E-IXsxBwGCrDBUvon6xKYktYwLbGl9rQZ4FxJ4e6kynTu3NL4Li3CnYbSUYuohsPvxEi59qI2-b82pcO5MDH3dfD0Er9OAEKiFZqS4UYysZX7vyMYLIgB4KYOnargYxRjR-nDrsG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراغه آذربایجان‌شرقی در شب ۹۴ خروش مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439512" target="_blank">📅 22:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439511">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d2f4ee98.mp4?token=udeYUX-UVO0M6YeDE0UT1eGQdI6jdfGXTPsdbGat1X1bDj50Mw9HmaAx4i-AZjmzopap53yl52f06uVvrVlyKwfjGgzWvV78Zl9PblQ46d9bO8Q3Nux0i7QD31C1L18yhneskqeOr1i_UdqyeVxwD6k32wee0i3pK-yumUDKEqEE7YBNS-B4Qcqm0VzVTV0r_2yAlxYlW21Sp7cU8vBRcyCo9aHSoilgo1Fm-3v49oEAQBz1FpKwVoiPHVL23mdZT90aVy7tlY8wElVNmc8Ut0mQl38i_hnXNuBlFZmDp3JHC9u5Vi1bMSDMJSWS-_h6n3DdD2LZhaGphGfTDYU7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d2f4ee98.mp4?token=udeYUX-UVO0M6YeDE0UT1eGQdI6jdfGXTPsdbGat1X1bDj50Mw9HmaAx4i-AZjmzopap53yl52f06uVvrVlyKwfjGgzWvV78Zl9PblQ46d9bO8Q3Nux0i7QD31C1L18yhneskqeOr1i_UdqyeVxwD6k32wee0i3pK-yumUDKEqEE7YBNS-B4Qcqm0VzVTV0r_2yAlxYlW21Sp7cU8vBRcyCo9aHSoilgo1Fm-3v49oEAQBz1FpKwVoiPHVL23mdZT90aVy7tlY8wElVNmc8Ut0mQl38i_hnXNuBlFZmDp3JHC9u5Vi1bMSDMJSWS-_h6n3DdD2LZhaGphGfTDYU7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آلمانی مقیم ایران: امام خامنه‌ای می‌خواست دنیا را برای کل جهانیان بهتر کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439511" target="_blank">📅 22:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439510">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLgg5EEAeAEX7aAzih2620saC8UsX_NHCZtgbn8YAOzQ5nkyAcePb5sPFJ1ZmstaVm24b7SB2s75-TRsYyG_mGf---DG5-QiraMTnMU_dDQP68F6ZUsdTbDYfmrbsClAceSGRRWXWF0LcSNLjV_quJaU_s7BBMHxnZto1s9ocRU0h4RI6NFRUZTHgEwWb4huozDoPxuFq7RsTx0hI0elMxTHUvmOw-JsY7YRGaF_2gihyEA5nfmZ5fpvk9LF41ylbCJjzKtTHzFajL-UarWIxuwfSpFDyoxW3nKb77Hu5URvsmfrVEiuZDVuwhZkRLqHRkZdKQ_oFWamuXEV3kTGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو شورای شهر تهران: ادامهٔ بررسی طرح حمل‌ونقل عمومی رایگان به هفتهٔ بعد موکول شد و احتمال تصویب طرح بالاست
🔹
آقامیری، نایب‌رئیس کمیسیون عمران شورای شهر تهران: محورهای مطرح‌شده در جلسهٔ امروز شورای شهر دربارهٔ تخفیف برای گروه‌های مختلف، نحوهٔ صدور کارت، صرفه‌جویی…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439510" target="_blank">📅 22:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439509">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">احتمال وقوع سیلاب در ۱۱ استان کشور
🔹
سازمان مدیریت بحران: احتمال وقوع بارش شدید، سیلاب، تگرگ و صاعقه در ۳ روز آینده در استان‌های آذربایجان شرقی، گیلان، مازندران، گلستان، خراسان شمالی، خراسان رضوی، سمنان، ارتفاعات تهران، البرز و نیمه شمالی آذربایجان غربی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/439509" target="_blank">📅 22:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
تصاویر دیده‌نشده از دیدار سردار پاکپور با خانواده شهدای مدافع امنیت
🔸
این تصاویر مربوط به دیدار با خانوادۀ شهدای مدافع امنیت و پایداری تیپ نیروی مخصوص ۳۳ المهدی (عج) جهرم در سال ۱۴۰۳ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439508" target="_blank">📅 21:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حملات هوایی اسرائیل به چندین منطقه در جنوب لبنان
🔹
المیادین گزارش داد که جنگنده‌های رژیم صهیونیستی شهرک‌های حداثا، دبین، صریفا و قعقعیه را در جنوب لبنان بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/439507" target="_blank">📅 21:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69184c7a32.mp4?token=B4Aaz1KAqCbHzIMG8pIoVUTbxJ7jQDfmkS_3jFUy-4WfQGXNcfpg5Biw2pf2TIWHjh5JFiKfNKhRVniiQ5QdXcrBzSyAAgpgMDBDkitrL3K8VySvRdgpPwzr3VpRNN_EeMgBXrB3ZWlLAhft56VANQhpZObkmVcJ9X5iMAUTlGumxG5CvyWn5ouu2R8Nak3qgxk0WUxsWxJ7gRUTCbMa4MMFiMvjcAp_MRiZygFiwuA6tjpcVibYoKF97EaIkqSgYrLrkCmyvidhSThNy-DzW-2-f9aUTyp9EOyzTth5FRVtWosAogKFKS4_kfN7Y_dYItnfUslcRNJioTHooC72_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69184c7a32.mp4?token=B4Aaz1KAqCbHzIMG8pIoVUTbxJ7jQDfmkS_3jFUy-4WfQGXNcfpg5Biw2pf2TIWHjh5JFiKfNKhRVniiQ5QdXcrBzSyAAgpgMDBDkitrL3K8VySvRdgpPwzr3VpRNN_EeMgBXrB3ZWlLAhft56VANQhpZObkmVcJ9X5iMAUTlGumxG5CvyWn5ouu2R8Nak3qgxk0WUxsWxJ7gRUTCbMa4MMFiMvjcAp_MRiZygFiwuA6tjpcVibYoKF97EaIkqSgYrLrkCmyvidhSThNy-DzW-2-f9aUTyp9EOyzTth5FRVtWosAogKFKS4_kfN7Y_dYItnfUslcRNJioTHooC72_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت میدانی ضاحیه جنوبی بیروت
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/439506" target="_blank">📅 21:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1989d23487.mp4?token=aa1wByJy0FCfTdaVaO8Okz2KN-YGuLxuFe7t9kloCJrr2qd2f19BlG1GbC7s_JOeaOge_w5KoJ9fxYd3jXvPYNx3xF-NIlKOMextXozVJovhd7krluFyOE1M0GoE7oTiwDz3Yha1TV-lwj32nDiGcpl0FYthdA3K2EXJzxgR27juQtGNSjlVbVStn7vPIlDgN3LFlhkAKUZYksrJnYA_IRl40E0UWO1h8LO-xuFTNSMTqhpD8_fCTTCvP623-DpDD8d_LtZrDruvhkth0s9QPyhh7lHxtxVbrNuNEU9LJj4N6I5X0bLRUiuizw8UmUiF-OWmYVA9SHlf8_cV4yftJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1989d23487.mp4?token=aa1wByJy0FCfTdaVaO8Okz2KN-YGuLxuFe7t9kloCJrr2qd2f19BlG1GbC7s_JOeaOge_w5KoJ9fxYd3jXvPYNx3xF-NIlKOMextXozVJovhd7krluFyOE1M0GoE7oTiwDz3Yha1TV-lwj32nDiGcpl0FYthdA3K2EXJzxgR27juQtGNSjlVbVStn7vPIlDgN3LFlhkAKUZYksrJnYA_IRl40E0UWO1h8LO-xuFTNSMTqhpD8_fCTTCvP623-DpDD8d_LtZrDruvhkth0s9QPyhh7lHxtxVbrNuNEU9LJj4N6I5X0bLRUiuizw8UmUiF-OWmYVA9SHlf8_cV4yftJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین وضعیت اکبر عبدی از زبان ده‌نمکی
🔹
مسعود ده‌نمکی، کارگردان سینما در گفتگو با فارس: اکبر عبدی یک یا دو مورد سکته خفیف داشت و در حال حاضر به دلیل عوارض قبلی در آی‌سی‌یو است و وضعیتش تثبیت نشده است.
🔹
آقای عبدی چند روزی هم در خواب مصنوعی بود و امیدواریم…</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/439505" target="_blank">📅 21:47 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
