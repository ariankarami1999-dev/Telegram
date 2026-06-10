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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.63M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-657941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9eb7155a.mp4?token=KdMXzyO4agTTXywl5o7mSMPf5tkiADM61FvfqDgtWnkJm8jTIZI1gO4r1EPyIvqKlK8GDZ8z1SBYWK2WdCDUl8dj9GG2aW6jUoCP_ZQJFULJwnP6qcNwPfTEBPCPYt5D_-q-ZhRjPwXawWS1sorviWPjzHmdIlVuBSs1HgFZ1f6TYytdKTqJ4LhqbEwDcFsl0VCdNm6XyN0FFM1oLqh4_-zLdCFcJQBFcvyp2XXwQkHBjrsQzjDeGI5ojsnejpDFSyX8MCGEcXwssvcwgLG6JfuDbJiA2_wtAt2Te0ZwvPcISSle7Pdo8iST4cUQWeE3ILyA0So1ypUymBXEVsBH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9eb7155a.mp4?token=KdMXzyO4agTTXywl5o7mSMPf5tkiADM61FvfqDgtWnkJm8jTIZI1gO4r1EPyIvqKlK8GDZ8z1SBYWK2WdCDUl8dj9GG2aW6jUoCP_ZQJFULJwnP6qcNwPfTEBPCPYt5D_-q-ZhRjPwXawWS1sorviWPjzHmdIlVuBSs1HgFZ1f6TYytdKTqJ4LhqbEwDcFsl0VCdNm6XyN0FFM1oLqh4_-zLdCFcJQBFcvyp2XXwQkHBjrsQzjDeGI5ojsnejpDFSyX8MCGEcXwssvcwgLG6JfuDbJiA2_wtAt2Te0ZwvPcISSle7Pdo8iST4cUQWeE3ILyA0So1ypUymBXEVsBH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ از بیخ گوش فیلمبردار گذشت
🔹
در جریان بازی دوستانه مجارستان و قزاقستان، دوربین فیلمبرداری از ارتفاع سقوط کرد و تنها چند سانتی‌متر با برخورد به فیلمبردار فاصله داشت!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/657941" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0cb9d3c2.mp4?token=C3W3mf02ZXHCIEz8Ffoi2z6RWFJe6naUF5B-G5EW8WCzwT_7eDl3jRvYiKuXrZzYpaDAajzJvm7rsUrFYN1odgCsTICWF9TVcVdXB4IeZE7Npm1R3Wu6tYVXU3gY5qrZchfN1nz0w_aM60AQ_AzZicf8P7yYdMeqHA5cD_TQFwFP-_ybDzDJyj5BPHGTIKHX0aTJ3YMpP3931Gha7WQWdWI9sdL_GI7eomvv9TazaTUETf_-KVvoSP5crpPjAqIcCLQt2LfJzTn_2TJsnRA2rTzozZbU3ZkD_VWfDxxLxegazMmJbKnqpFbt9mIVndtqeYYL7eGchp12SzepLhJbyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0cb9d3c2.mp4?token=C3W3mf02ZXHCIEz8Ffoi2z6RWFJe6naUF5B-G5EW8WCzwT_7eDl3jRvYiKuXrZzYpaDAajzJvm7rsUrFYN1odgCsTICWF9TVcVdXB4IeZE7Npm1R3Wu6tYVXU3gY5qrZchfN1nz0w_aM60AQ_AzZicf8P7yYdMeqHA5cD_TQFwFP-_ybDzDJyj5BPHGTIKHX0aTJ3YMpP3931Gha7WQWdWI9sdL_GI7eomvv9TazaTUETf_-KVvoSP5crpPjAqIcCLQt2LfJzTn_2TJsnRA2rTzozZbU3ZkD_VWfDxxLxegazMmJbKnqpFbt9mIVndtqeYYL7eGchp12SzepLhJbyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شده پرچمتو تکون بدی بخوره تو سر یکی؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/657940" target="_blank">📅 10:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ریزش قیمت طلا شدت گرفت
🔹
قیمت طلا در معاملات روز چهار­‌شنبه بازار جهانی تحت تاثیر تقویت ارزش دلار و افزایش قیمت نفت، کاهش یافت و به پایین‌ترین حد خود در ۱۱ هفته گذشته رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/657939" target="_blank">📅 10:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c7ed1810.mp4?token=YPHGKO-eoYH19gUCEJfzDnMqbhMzVRNq1w_wZqEpx_cg_zvg0bbi3sGtPy8_mf2p0yjiA5XDMsVCaaBtH8o6Mythvce5moYVpvyx2gXEcoSCPE_9OTTlps-QgayNUqNlZNQ_F2DYU4Iw2fUfH-_JIeMsjcO5T7eL80zpiyUvyQ-dzZVPbmURMJwEjETK3RuSlRGktDcDoqb5RmEq3uT93eKTKjagDcc0bwu-Gbc0weHo68wET9mYdKXXcrhwkvlC4fL7xsNHO13pmHeSnJeIrIOSxBcl3-qVnIbG6sVWxYYRO_w3zNCix-V8_yQilwVbIQPnwV4nNLtbX-f_D0-1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c7ed1810.mp4?token=YPHGKO-eoYH19gUCEJfzDnMqbhMzVRNq1w_wZqEpx_cg_zvg0bbi3sGtPy8_mf2p0yjiA5XDMsVCaaBtH8o6Mythvce5moYVpvyx2gXEcoSCPE_9OTTlps-QgayNUqNlZNQ_F2DYU4Iw2fUfH-_JIeMsjcO5T7eL80zpiyUvyQ-dzZVPbmURMJwEjETK3RuSlRGktDcDoqb5RmEq3uT93eKTKjagDcc0bwu-Gbc0weHo68wET9mYdKXXcrhwkvlC4fL7xsNHO13pmHeSnJeIrIOSxBcl3-qVnIbG6sVWxYYRO_w3zNCix-V8_yQilwVbIQPnwV4nNLtbX-f_D0-1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رؤیای دیرینه صهیونیست‌ها برای نابودی ایران
/
بمباران، تجزیه، جنگ داخلی!
🔹
اعتراف تحلیلگران اسرائیلی به اهداف شوم و دیرینه رژیم صهیونیستی برای نابودی ایران!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/657938" target="_blank">📅 10:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657936">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f03dc55a4.mp4?token=UW-ZSJBZzaGALb_XpKoxJQzpQYYajDWdA5gXKsBEJViODcaZYGYmiU2D6tVsYrKC2f2fpPj2Njlle5N3vYnfMrCKB6BM8s1cZnSSydm4cmQ0fY_4smXN9d8U0yAUOnmZcBBKfrz2KMcFUIBW149O10J83X9EF5Du1SSnwSiIoAlseLTqpL_3Wfrpn8uSity25G1JOhiGcCv3WdaVDGQs2DPNOMkor_6vMmdVmQ5hToM1lLblp-mLL5335kofWDmgQejErf6GpOuVT-xdmAEj2V4CLSfcvi9NFkmCwNIZ3sAJooenbbPR0ro1FwgQ0Z0Wk7Aa5NNXw-pr4NROgJinQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f03dc55a4.mp4?token=UW-ZSJBZzaGALb_XpKoxJQzpQYYajDWdA5gXKsBEJViODcaZYGYmiU2D6tVsYrKC2f2fpPj2Njlle5N3vYnfMrCKB6BM8s1cZnSSydm4cmQ0fY_4smXN9d8U0yAUOnmZcBBKfrz2KMcFUIBW149O10J83X9EF5Du1SSnwSiIoAlseLTqpL_3Wfrpn8uSity25G1JOhiGcCv3WdaVDGQs2DPNOMkor_6vMmdVmQ5hToM1lLblp-mLL5335kofWDmgQejErf6GpOuVT-xdmAEj2V4CLSfcvi9NFkmCwNIZ3sAJooenbbPR0ro1FwgQ0Z0Wk7Aa5NNXw-pr4NROgJinQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور کمالگرایی می‌تونه مارو از مسیرمون دور کنه؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/657936" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
یک منبع آگاه نظامی: ارزیابی‌های اولیه نشان می‌دهد حدود ۷۰٪ اهداف عملیات بامداد امروز ایران علیه پایگاه‌های آمریکا در اردن، کویت و بحرین با موفقیت مورد اصابت قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/657935" target="_blank">📅 10:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fck4YC2EKYickN6adhU4nS7w6BWX7JX8-4pyyMpTkU34Ggz5lWgEbkpUPFuVwBwQ4ST_xdxqtVIrL9xq1WiN0O-8K0bi10ArDEaVxvhWq52tRnlYFn00K4PumlH8n2U2WUdTqTNa__iKDalWqGU3cHGjEWSlJS2ItbuNtpjRMTPS-Ca91FjpooR3uMd-cTZ66GjyqvlZliEWMA_0COq22PONw7LflxIH8AKV7YJ4ditlp0n9vN06ux8HGlx-fsUreh8WFGyDcEBbC3bQeiDYWB6HbUGtdEWd1DrWQKNPObHQ3SPvxb8TYHl5HCJ12V9MgOAr1QNaGJiaTqoDmPEvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت خرید کیا اسپورتیج از طریق کوشا خودرو
در ادامه عرضه مستقیم محصولات کیا که از ۱۸ خردادماه آغاز شده، متقاضیان می‌توانند برای خرید کیا اسپورتیج از طریق وب‌سایت رسمی کوشا خودرو اقدام کنند.
فرآیند ثبت‌نام و خرید به صورت کاملاً آنلاین و از طریق بخش «فروش اینترنتی» انجام می‌شود.
🌐
وب‌سایت ثبت‌نام:
www.kooshakhodro.com
کوشا خودرو
فروش و خدمات پس از فروش کیا در ایران</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/657934" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657933">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3863f2a74c.mp4?token=XCml89kdhzXggqgKxRigmcP6BMLXfhjUP6czBXshz_AfvFOfitcVFYtShXE1tOaEir2aAp8pwBIybvPEL3Nw-HslOa1HdDWqDd0dD9bkLgK-xvHgoajIVDIV1Vi5WU2cfPPEhiuVoWpd7liPWgjeYf-hojMBpEqCt2gW-GbJZPof-ikBabPhYIgc5BGaxCLkrlyOKwuoV45kXupBA016RZDv71744qStr1Y4ta9ZAmWHGn6qHhbR7cRqwaKwIhMu5YwbSMAXur-QrRYivD86d4xWyd2_TNMSYIN2SBVcBKz33NBZpa3VNsVoK_k8ZM-P2SNzgtXIC0EoXrVSDvlAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3863f2a74c.mp4?token=XCml89kdhzXggqgKxRigmcP6BMLXfhjUP6czBXshz_AfvFOfitcVFYtShXE1tOaEir2aAp8pwBIybvPEL3Nw-HslOa1HdDWqDd0dD9bkLgK-xvHgoajIVDIV1Vi5WU2cfPPEhiuVoWpd7liPWgjeYf-hojMBpEqCt2gW-GbJZPof-ikBabPhYIgc5BGaxCLkrlyOKwuoV45kXupBA016RZDv71744qStr1Y4ta9ZAmWHGn6qHhbR7cRqwaKwIhMu5YwbSMAXur-QrRYivD86d4xWyd2_TNMSYIN2SBVcBKz33NBZpa3VNsVoK_k8ZM-P2SNzgtXIC0EoXrVSDvlAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت یک کودک شیرخوار به دست نظامیان صهیونیست
🔹
تصاویری از لحظه هدف قرار گرفتن یک کودک شیر خوار ۷ ماهه به نام «سام ابو هیکل» با گلوله یک نظامی صهیونیست در الخلیل منتشر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/657933" target="_blank">📅 09:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657932">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/657932" target="_blank">📅 09:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4JIXklxSRNqbVOJxUKLUsKWL7d8j1BEWh5Q_n-Igr0ai1uTuiNSC2t6pJKy_SrmwzT_ZEGypijne4MWuFckBg4uQhk3A4feirfdSIPEK6xMc14jAsTDUahpB6EZn5RaRWPWYPo5xwcUz94wJQTAs027KWTsLC9_uJVKqfUUIKGEfUSm2z6fPEdlFkI_y2FNLqZ7qjYjB3aAPGBuJ9NqTUpkN8Wi1UOo_alZRZ_dkKgT3CRORU9acSwMz67ABE1iBVI4VCLOL4EuThCIRAceyE66iEyYnH1d8XLcdnMx-riCI2lEUzYISjMufsaNtnqt5VTVX9mLc0OnuiEA5n9u0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه دریایی در آب‌های یمن
🔹
سازمان عملیات دریایی انگلیس گزارش کرد که یک حادثه در ۸۸ مایلی جنوب غربی بلحاف یمن اتفاق افتاده است.
🔹
در این حادثه، یک قایق با ۶ فرد مسلح به یک کشتی باری نزدیک شده و تبادل آتش بین قایق کوچک و کشتی‌های باری رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/657931" target="_blank">📅 09:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
بازی شطرنج میان ایران، آمریکا و رژیم صهیونیستی؛ ایران بنا به چه راهبردی به تجاوزات اسرائیل به لبنان واکنش نشان داد؟
🔹
پاسخ ایران به تجاوزات رژیم صهیونیستی به لبنان برای برخی ابهاماتی را به همراه داشته اگرچه مشخص است که این پاسخ در همان پازلی تعریف می‌شود که بسیاری سقوط سوریه را مقدمه‌ جنگ علیه ایران ارزیابی می‌کردند.
🔹
امروز به وضوح مشخص است که تضعیف حزب‌الله می‌تواند موازنه‌ قدرت در منطقه را بر هم بزند و هزینه‌های امنیتی ایران را در تقابل‌های آینده به شدت افزایش دهد؛ به‌خصوص که جنگ حزب‌الله با اسرائیل بخشی از ظرفیت نظامی این رژیم را در جبهه لبنان درگیر کرد و مانع تمرکز کامل آن در جنگ ۴۰ روزه علیه ایران هم شد.
🔹
براوردها از رفتار اسرائیل در جنوب لبنان حاکی از این است که اهداف این رژیم فراتر از تضعیف حزب‌الله است و تخریب گسترده روستاها و زیرساخت‌های مرزی مقدمه‌ای برای اشغال بخشی از خاک لبنان حداقل تا رودخانه لیتانی ارزیابی می‌شود و تضعیف جدی بازوی زمینی ایران در کنار رژیم صهیونسیتی است.
🔹
از این منظر، تضعیف هر یک از بازیگران محور مقاومت تهدید موجودیتی علیه امنیت ملی دیگری را تقویت می‌کند. بنابراین پاسخ ایران صرفاً واکنشی دفاعی نبود، بلکه پیامی در جهت تغییر قواعد درگیری و تقویت بازدارندگی فعال در برابر تهدیدات اسرائیل و آمریکا، در راستای حفظ منافع امنیتی و ملی ایران و لبنان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/657930" target="_blank">📅 09:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035a4f599f.mp4?token=iVRv5JCdEzicPR7eYLBnbi7HRKJikR7r4PeiPp9wB_RUnC_MkoLZXs52Cm2nutSqUHQwmK4KKt4AqDzyPEOoS1lQ5fJ6Pw1zl_pIF2ED9jkDs26GGx-vENLQ2oxNG4JR9mM4fD8uqEC258_cpQdzN315Y1jE04PTlzEufAF_fgSE55IrEXlxQXD-sqnKTpwhO79PBPFxcoM6ddO_60z5LdbvJAmBsLJ73SY-CT_AL4_B3iPtaDAzHhOnT3yddJIDoZqAdF9C_5lfHtJut6mbPU9HBo1ouVZ53WSt53OxX8jPT5HeSQrqJ0hVNmdmgmjoD9Bz9K2oI_d-MPoqYrF6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035a4f599f.mp4?token=iVRv5JCdEzicPR7eYLBnbi7HRKJikR7r4PeiPp9wB_RUnC_MkoLZXs52Cm2nutSqUHQwmK4KKt4AqDzyPEOoS1lQ5fJ6Pw1zl_pIF2ED9jkDs26GGx-vENLQ2oxNG4JR9mM4fD8uqEC258_cpQdzN315Y1jE04PTlzEufAF_fgSE55IrEXlxQXD-sqnKTpwhO79PBPFxcoM6ddO_60z5LdbvJAmBsLJ73SY-CT_AL4_B3iPtaDAzHhOnT3yddJIDoZqAdF9C_5lfHtJut6mbPU9HBo1ouVZ53WSt53OxX8jPT5HeSQrqJ0hVNmdmgmjoD9Bz9K2oI_d-MPoqYrF6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سایت Global: کمپ ایران بهترین کمپ جام جهانی از لحاظ امنیتی است
🔹
پس از حوادث امنیتی در نزدیکی کمپ‌های انگلیس و سوئیس، رسانه‌ها از استقرار ۳۰۰ نیروی ارتش و گارد ملی در اطراف کمپ ایران خبر دادند؛ آماری که در میان تیم‌های حاضر بی‌سابقه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/657929" target="_blank">📅 09:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: ایران به جای تحویل ذخایر اورانیوم، آنها را رقیق خواهد کرد
🔹
نیویورک‌تایمز مدعی شد توافق احتمالی هسته‌ای شامل توقف ۱۵ ساله غنی‌سازی، رقیق‌سازی ذخایر اورانیوم ایران، برچیدن برخی تأسیسات هسته‌ای و بازرسی‌های سرزده خواهد بود.
🔹
به ادعای این روزنامه، ایران به‌جای انتقال اورانیوم به خارج، ذخایر خود را با همکاری آژانس بین‌المللی انرژی اتمی رقیق می‌کند./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/657928" target="_blank">📅 09:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044ad13ff6.mp4?token=m3bwwvUOwVW6DbzSxTfoh-cctm0pW9sVdaADp2zqe6M4t_j7Fu-piUk3TN9zc2Zk2sVvtYdjVuYN2_LOSrUIjxtBPSq7VFkbCfF8oOis7ewomdC7-7dhmj0vlQB3eTP9Nu1xTr0SDv06f1PMiecv_wsOkd7hcNOOR1ltHjqmFbI5Z9PYKRWJE4I08wl6ZzOifxk8a3u8CyjtwPlgY7Keig34xi5MJIHTjZY-gFU9rG8T3Q8SNUCCylt8K_roxXixti4hM_nQVjYy-RfX6kvXzipFXbLElOZyYc22lb2RiZptxiyUB68-qh-NLocERxmLltBUjEKlwE_8OCkxqpYMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044ad13ff6.mp4?token=m3bwwvUOwVW6DbzSxTfoh-cctm0pW9sVdaADp2zqe6M4t_j7Fu-piUk3TN9zc2Zk2sVvtYdjVuYN2_LOSrUIjxtBPSq7VFkbCfF8oOis7ewomdC7-7dhmj0vlQB3eTP9Nu1xTr0SDv06f1PMiecv_wsOkd7hcNOOR1ltHjqmFbI5Z9PYKRWJE4I08wl6ZzOifxk8a3u8CyjtwPlgY7Keig34xi5MJIHTjZY-gFU9rG8T3Q8SNUCCylt8K_roxXixti4hM_nQVjYy-RfX6kvXzipFXbLElOZyYc22lb2RiZptxiyUB68-qh-NLocERxmLltBUjEKlwE_8OCkxqpYMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی عجیبی از یک انفجار اتمی در بندرعباس که ساعتی قبل در پخش زنده شبکه خبر منتشر شد!
🔹
در حالی که خبر درباره سازمان توسعه تجارت ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/657927" target="_blank">📅 09:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d0cc9941.mp4?token=GmbYz5RiypZOvYRuzuBli44eWKrKcNTFZch7fmYf12NYMY8n6iMUJOwjvqwL9AszoDv1krTxmG_g7ObamlpIrwpKKH6fIymiCOFNJrDBpNnNMg7zy9VZG86G34WbWwgC0uJRgLS1cEt-AJCKCI-4OSDUAyh9CXqp7aXWBC0upN_5c04jqWGeqQBHbNJcW8JkCEtvRbV60jGmP0XxjTFFKV8DdQen1KgNSm6Up6FVqliLuRFGic4Yn0ZixppsvwRw4pmsIVhNc1-QB7O4tV5G2hpMzy4ra5Q1ntJ-FVacYtikyWaVOHRwoBXQD3Cj6zk5kBDs9KPis_0jU4fEcMmRLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d0cc9941.mp4?token=GmbYz5RiypZOvYRuzuBli44eWKrKcNTFZch7fmYf12NYMY8n6iMUJOwjvqwL9AszoDv1krTxmG_g7ObamlpIrwpKKH6fIymiCOFNJrDBpNnNMg7zy9VZG86G34WbWwgC0uJRgLS1cEt-AJCKCI-4OSDUAyh9CXqp7aXWBC0upN_5c04jqWGeqQBHbNJcW8JkCEtvRbV60jGmP0XxjTFFKV8DdQen1KgNSm6Up6FVqliLuRFGic4Yn0ZixppsvwRw4pmsIVhNc1-QB7O4tV5G2hpMzy4ra5Q1ntJ-FVacYtikyWaVOHRwoBXQD3Cj6zk5kBDs9KPis_0jU4fEcMmRLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دختر شهید نصیرزاده: پدرم می‌گفت عزیزانی که کار رسانه می‌کنند ارزش کارشان بالاتر از ارزش کار ماست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/657926" target="_blank">📅 09:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaae64f0bb.mp4?token=udNtaH2M5_2T-k09nUbmsBFUB39zMetjX6tTjeDvpR58x_VySkKKicGLU5kLPeAVOqDLX0pzfVr7bAc_STTFUpo4Nop4hgLUakmjbfhTFXrXQG8kzQcPGafxYViqIfS5muNSvKVD9fLXFqEOCX5UbKDF7L0gb1kOBKEnU_PDD6Egu_ZWExXuMMDSgMij_BLBezoM4DOKDichT94867gypCKDqCz5d0ew7zFbYmXVeSuedhahYFCpo8Mky_Jw6xXSjySr_HYd4UePT-Izarz_3E6rencbH3VwEKXjlQHYHelPy8cU8_VXJ5UWMME4QQBCsyhtNJXioZrPVSm5Jvtp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaae64f0bb.mp4?token=udNtaH2M5_2T-k09nUbmsBFUB39zMetjX6tTjeDvpR58x_VySkKKicGLU5kLPeAVOqDLX0pzfVr7bAc_STTFUpo4Nop4hgLUakmjbfhTFXrXQG8kzQcPGafxYViqIfS5muNSvKVD9fLXFqEOCX5UbKDF7L0gb1kOBKEnU_PDD6Egu_ZWExXuMMDSgMij_BLBezoM4DOKDichT94867gypCKDqCz5d0ew7zFbYmXVeSuedhahYFCpo8Mky_Jw6xXSjySr_HYd4UePT-Izarz_3E6rencbH3VwEKXjlQHYHelPy8cU8_VXJ5UWMME4QQBCsyhtNJXioZrPVSm5Jvtp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عجیب استادیوم‌ محل برگزاری دیدار بامداد امروز آرژانتین و ایسلند در شهر آبرن واقع در ایالت آلابامای آمریکا، ۳ ساعت قبل از شروع بازی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/657925" target="_blank">📅 09:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
خوابیدن نظامیان صهیونیست در نفربر ممنوع!
رسانه‌های صهیونیستی:
🔹
ارتش رژیم اسرائیل نظامیان خود را از خوابیدن در داخل نفربرهای زرهی در لبنان منع کرده است؛ این اقدام پس از دو حادثه ای  رخ داد که منجر به کشته شدن دو نظامی صهیونیست و زخمی شدن ۶ تن دیگر شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/657924" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شاخص کل بورس ایران رکورد تاریخی زد
🔹
شاخص کل بورس در این دقایق با عبور از  ۴ میلیون و ۶۰۰ هزار واحد رکورد تاریخی جدیدی رو ثبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/657923" target="_blank">📅 09:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf9f16584.mp4?token=LtBsG8ZtY1egvCUG-kJtZ53ErlF0GiOY5MOub0F7QIG_rDn-fsF-O05PkXJ_nqgrR4ABUUFlbaVOmu_0t8YuXrrom6ti9xLy5T1f4JOetBWBHC2vPkGyww1SyZ0OTrTxzLLRglJSErGyC7QyMAEbBpi2owaJ-MMnzvIna0ro-MvQgn6u-ZH9WQSpKhuaDtUVrwn3Sy27wUGHlVmqg-aTFsz4a91IjumDKYSUElqf4P4YJBu6nXB5VIYRHw2gdEgtgZT60Pz-GpqCyClaFiBsbq4IdZvxS5t0dlu_adV1w7rCt4QnYgEEtMf_3eYVmY4byH9X0vCo9z1W5fINYvsYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf9f16584.mp4?token=LtBsG8ZtY1egvCUG-kJtZ53ErlF0GiOY5MOub0F7QIG_rDn-fsF-O05PkXJ_nqgrR4ABUUFlbaVOmu_0t8YuXrrom6ti9xLy5T1f4JOetBWBHC2vPkGyww1SyZ0OTrTxzLLRglJSErGyC7QyMAEbBpi2owaJ-MMnzvIna0ro-MvQgn6u-ZH9WQSpKhuaDtUVrwn3Sy27wUGHlVmqg-aTFsz4a91IjumDKYSUElqf4P4YJBu6nXB5VIYRHw2gdEgtgZT60Pz-GpqCyClaFiBsbq4IdZvxS5t0dlu_adV1w7rCt4QnYgEEtMf_3eYVmY4byH9X0vCo9z1W5fINYvsYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه کارشناس فاکس‌نیوز به ادعای نزدیک‌شدن به توافق با ایران، درحالی که حملات ادامه دارد: اگر فردا بشنویم که به توافق با ایران نزدیک‌تر شده‌ایم و تقریباً به آن رسیده‌ایم، فکر می‌کنم کمی پذیرفتنش سخت باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657922" target="_blank">📅 09:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به شهر صور در جنوب لبنان
🔹
رسانه‌های منطقه از حمله هوایی رژیم صهیونیستی به شهرک طيردبا در شهرستان صور در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657921" target="_blank">📅 09:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657920">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2007b0e50.mp4?token=d2JoBzdKGvSx5XzVPP_BUTXa4koibSueObke4Jx87K6_uIJgeNZc7QQDtsmEBHal82eQiZlFSYcmN6Qkrgy9nYE5sjE5Ni7LM4B0BsF3oKCCpLublMzythsLQ6j8M6u6pAfmSBnyB1ZUI1v7zSvLueEv8n32RkOdBsh8PM0HqkZNf_F5R3bO_UFGpiyWvwPIJy3g3yZVG92FObEQiqgU7ovPALosW-qzqUPWcLY4Vq7DEfwEZZULoCfnthpvuBS4lA08dHl7be-k_lSBq6dqeDK8n8HYCKOC2yU_3Z28qGcPjUKNJKKPb08u4ceqyfXGQRUVMhg5wwCfxUTSjC0jHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2007b0e50.mp4?token=d2JoBzdKGvSx5XzVPP_BUTXa4koibSueObke4Jx87K6_uIJgeNZc7QQDtsmEBHal82eQiZlFSYcmN6Qkrgy9nYE5sjE5Ni7LM4B0BsF3oKCCpLublMzythsLQ6j8M6u6pAfmSBnyB1ZUI1v7zSvLueEv8n32RkOdBsh8PM0HqkZNf_F5R3bO_UFGpiyWvwPIJy3g3yZVG92FObEQiqgU7ovPALosW-qzqUPWcLY4Vq7DEfwEZZULoCfnthpvuBS4lA08dHl7be-k_lSBq6dqeDK8n8HYCKOC2yU_3Z28qGcPjUKNJKKPb08u4ceqyfXGQRUVMhg5wwCfxUTSjC0jHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روايت رهبر شهید انقلاب از روزی كه پيامبر اکرم دست عزيزان خود و حضرت علی (علیه‌السلام) را گرفت و به ميدان آورد
🔹
بازنشر به مناسبت روز مباهله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/657920" target="_blank">📅 08:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657919">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ao_Av0pFo2cckvgrFp5MYSilu9yhAVBlytBlI4KygbryYnnWBcFYtP95EZ-r_AdL2Q6j5b-4YbWuZ6b9siop7dmdCEMFSbnne8bEYKVBL0fu_rkd_ZZJi2utLAuFXwlluVALpKyx-RUbunjeNQLgSE1YwmsEQ7mU4bXvqBBbf-iRBFeN_8-jDKTeuxJN5iaidIZOko5-ehY8lRVMWOKHorqhaI5D04jAT88AV6ti0sH10Zt9QMvr8aG81ZH78feP3hvQVhwQjZeqQbvOAACs_ANsaicpEFuuvTE7HE50GBT2UBlM9cahGuDlap-wKi9GPZ8WwvzPXVU083gCq0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مباهله؛ روزی که حقانیت اسلام در برابر تاریخ درخشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657919" target="_blank">📅 08:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657918">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
وزیر علوم: سهمیه جنگ در کنکور ۱۴۰۵ قطعی شد؛ جزئیات نحوه برگزاری امتحانات
حسین سیمایی صراف:
🔹
همچنین امتحانات دوره تحصیلات تکمیلی، همانطور که کلاس‌هایشان حضوری هست، حضوری خواهد بود.
🔹
کلاس‌های درسی و امتحانات دوره کارشناسی نیز غیرحضوری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657918" target="_blank">📅 08:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657917">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPPaaD-FOvQURzH17uSVLMSSoCSuQ-ISJW_EgDwlUivF18ofA9pgww96uQrIjpg12STLfGN9WkK3D3GcoSRmUoOg_iNPlAxoDTXzFvKmrWWcVhyhBUYH7NJBMKa-y4fV9iTG3Afe529PRx73gLqsWpxvkhUz3XEeKihoT9wcgdvq_xNeQS_4YAa-MrT5Y27Uj1qrMY1b-T_CpFVoSOjr-1Zbw9SfkWNiGCQMvvHXkPSG-gclZNcWTDjmjI-D1l45C8FxIjaec8FGGGAtAUs3VMPqxBVJjPE2B8WyqEF0V1EsEYuQytMZDl-i1IjEvt5LBhBwn3ILhoM2tRm7PEs3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی از تابلوی نتایج جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/657917" target="_blank">📅 08:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657916">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7377d61fd8.mp4?token=O8OSH7zJr3yB5ifzwZTRyxWRcAln07bkEgpmUWwsCHTnA3z02W6RIqzHSUFhelvOON1D3QJ0bA_xj5KlPAPpvlm6rM88pBgrimVu7hPTY8Ger107VuF1LMhb4zb3pQVaxirieBeQMyfWXUVk6x50nNe8JIskRV3OFcKZw5pSculiyoFtMJFMZRn8XXL5nZBbkCDn0kGpCizk5f3guApKWn5FVYCmQaFe-s_dwtnuTGJk9xFQvnF0MMwuevsN2tKUBvZ030aZdojlSU5Ou4p-hWmWbR_OyThU3urVnE1SbmYeSuQaOSrqojRPd5P09QRufV35LVM4hjeFav7HDEAcsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7377d61fd8.mp4?token=O8OSH7zJr3yB5ifzwZTRyxWRcAln07bkEgpmUWwsCHTnA3z02W6RIqzHSUFhelvOON1D3QJ0bA_xj5KlPAPpvlm6rM88pBgrimVu7hPTY8Ger107VuF1LMhb4zb3pQVaxirieBeQMyfWXUVk6x50nNe8JIskRV3OFcKZw5pSculiyoFtMJFMZRn8XXL5nZBbkCDn0kGpCizk5f3guApKWn5FVYCmQaFe-s_dwtnuTGJk9xFQvnF0MMwuevsN2tKUBvZ030aZdojlSU5Ou4p-hWmWbR_OyThU3urVnE1SbmYeSuQaOSrqojRPd5P09QRufV35LVM4hjeFav7HDEAcsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهر: منابع خبری از شنیده شدن صدای چند انفجار در شمال عراق خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657916" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657915">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
گفتگوی تلفنی عراقچی با وزرای خارجه ترکیه و عربستان
🔹
هاکان فیدان و فیصل بن فرحان، وزرای خارجه ترکیه و عربستان، در تماس‌های جداگانه با سید عباس عراقچی آخرین تحولات منطقه پس از حملات آمریکا به جنوب ایران را بررسی کردند.
🔹
عراقچی ضمن محکوم کردن این حملات و نقض حاکمیت ایران، بر حق دفاع مشروع و پاسخ متقابل نیروهای مسلح کشور تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657915" target="_blank">📅 08:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9589895de9.mp4?token=NXY7QVvD7lP5gRr9spdOVge67EN0BQkzitYcVnOwka_IOqYFvpdn1JQrnPGADHbXqZVSCGb4oz6kmkesoPkdbRGE2UBADjnPTJWwG4ZuDRzLkEOauyttuECrJ_eKqQ4p5gKGSGWdFqnhdhoySlvHeRD0irJX8fyLA_2ZDmvvygq3jEeOXQ0wzIDB-btI_YKO0DcR1bvkR289MXnDOF8oS9wUMeBBIL0oTH3g_vqksk5BaFnRzPJEPv4MnZMGM0_0Oqo6mQglCXblHmwdW-xWnRr10aOqjF7r7wF2eO44SkpgZldYQBw-ff4bEBAr3Bl-0TSc2-EMqc74KUy4BqBs2RZQPBrHo992miWy4eYeB5A4NlsuMmweyOFNJpUXbw9DXVKVWRtR6YQ-TLUH94gBG9uz0nErns23I-cO3RGHmbYtfRpd9ex0zhGGr-sX5mi26-JSB20gQN5IwRXfdl0c68GSYK0nyt4y4c0iQO-6GAe2Dr7DK8eGWaHQ8gWugBKpuJoySMSoAXzvpLOYQUaHhKGQkWFamFVQbvvLHMmmCmVTIeMIgR-f6PCvMfH7XgOVgqwVb--0URu1meUAZc-hWTrZfNJXv5mNYQElCKsWSuPrs0NvCcNIdS3edgkNFDpu3WiBUh4VGlD8dBYZaIbrnIOH-KugoqHDqGEBiZ0p-Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9589895de9.mp4?token=NXY7QVvD7lP5gRr9spdOVge67EN0BQkzitYcVnOwka_IOqYFvpdn1JQrnPGADHbXqZVSCGb4oz6kmkesoPkdbRGE2UBADjnPTJWwG4ZuDRzLkEOauyttuECrJ_eKqQ4p5gKGSGWdFqnhdhoySlvHeRD0irJX8fyLA_2ZDmvvygq3jEeOXQ0wzIDB-btI_YKO0DcR1bvkR289MXnDOF8oS9wUMeBBIL0oTH3g_vqksk5BaFnRzPJEPv4MnZMGM0_0Oqo6mQglCXblHmwdW-xWnRr10aOqjF7r7wF2eO44SkpgZldYQBw-ff4bEBAr3Bl-0TSc2-EMqc74KUy4BqBs2RZQPBrHo992miWy4eYeB5A4NlsuMmweyOFNJpUXbw9DXVKVWRtR6YQ-TLUH94gBG9uz0nErns23I-cO3RGHmbYtfRpd9ex0zhGGr-sX5mi26-JSB20gQN5IwRXfdl0c68GSYK0nyt4y4c0iQO-6GAe2Dr7DK8eGWaHQ8gWugBKpuJoySMSoAXzvpLOYQUaHhKGQkWFamFVQbvvLHMmmCmVTIeMIgR-f6PCvMfH7XgOVgqwVb--0URu1meUAZc-hWTrZfNJXv5mNYQElCKsWSuPrs0NvCcNIdS3edgkNFDpu3WiBUh4VGlD8dBYZaIbrnIOH-KugoqHDqGEBiZ0p-Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش هولناک خبرنگار آمریکایی در نشست مطبوعاتی کاخ سفید: اسرائیل از صدای ضبط‌شده گریه نوزادان برای بیرون‌کشیدن ساکنان اردوگاه آورگان و شلیک به آن‌ها استفاده می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657914" target="_blank">📅 08:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657913">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تصاویر شلیک موشکهای سوخت جامد و مایع دوربرد قدر و عماد و خیبر شکن به سمت اهداف امریکایی در منطقه در پاسخ به تعرض بامداد امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/657913" target="_blank">📅 08:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657912">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnuA3SGQhrxC-16Q88Jicr5icAnlMD4ASRlhk2SuGaRSoeKNZNylL9BZzraOut1Fma7fkRMcFzf7hXUps7bduwd4aAVI7L9hEn0XFk-hdBhLwHqrusZ2Swx14aE9l_p53ETexLLhGdyfeuXZvNAUCNDkj_1RR6GuzRZj3G500LoiDueZn1snI5LcKvzcMtOvFU03j4fpfbfqa3MIbl3yjGGogeJB1c8fNR1san31s65KT5oBMdNageGycbizmImA9Chw7h7f7_qEYNLoLhNkm3lj3qqszQUEU5nOxgGRyTJ74m5GfJW3hIG9WfUp5UtAt-wP5ITRWITYEJCyg5ZtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش خبرنگار گلوبو از برخورد نامناسب در آمریکا
کارین آلوِس، خبرنگار شبکه TV Globo:
🔹
«وقتی رسیدم از من خواستند موهایم را بالا بزنم، آن هم با لحنی تند و بی‌ادبانه. کاملاً گیج شدم، حتی کفش‌هایم هم بازرسی شد. مردم با این رفتارهای تند مواجه می‌شوند. متأسفانه آنچه می‌بینیم محیطی بسیار غیر دوستانه برای کسانی است که برای پوشش جام جهانی به آمریکا می‌روند.»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/657912" target="_blank">📅 08:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657911">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36823db122.mp4?token=NmR6kf26mnA1LR3SyEscqvuJVC0SrJiaA8TXXjaCenkfxihhpEowQFKMQoJAtRXQuL2dl4HWQI4jiLtBbl14WeqfKjMU5J3twHJ0Cz3DLtqxTLKXyKrfUhnNX3zSC3g11sl5mxTICFF10ejdN5mWnIN6s4ZOFIt4zihD04DabheCwmby5D7YLLmg_nlKRddRxT3M9vPW8UBOXv0LJ_4vqRSmX0oH97QgJGMz6QxN3Ap6WeTHkXiBbc6VI-lUFCJJI6IHXudMlkO2EN540JpDCn7EMPo_QCJ73IJOhHIq-Ub_bw6SKdFsZwPR4QsKoUdxm9Wj_gZZMj6bliJipgmZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36823db122.mp4?token=NmR6kf26mnA1LR3SyEscqvuJVC0SrJiaA8TXXjaCenkfxihhpEowQFKMQoJAtRXQuL2dl4HWQI4jiLtBbl14WeqfKjMU5J3twHJ0Cz3DLtqxTLKXyKrfUhnNX3zSC3g11sl5mxTICFF10ejdN5mWnIN6s4ZOFIt4zihD04DabheCwmby5D7YLLmg_nlKRddRxT3M9vPW8UBOXv0LJ_4vqRSmX0oH97QgJGMz6QxN3Ap6WeTHkXiBbc6VI-lUFCJJI6IHXudMlkO2EN540JpDCn7EMPo_QCJ73IJOhHIq-Ub_bw6SKdFsZwPR4QsKoUdxm9Wj_gZZMj6bliJipgmZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک اشتباه رایج در حرکت شنا! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/657911" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657910">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyRpecMaD1Twoq1eSev4jQo36moVIcI6EDSnFfWlo4Kk7Cv5NjBeqYtgVp1KMp8S6Ncq-RBxNN-Y6f-5xxtVHpK5Wp21rCMuB8eLt1E6zZgj5_UHa-E1goZlj4ZTq5iQIZGo5vHQlqQbgOhEdM3qX9bS-b3QKI3_0rwoYxmh70Ik26B2iYp53p_tkVXmu6HZEPdr5Nm2hg-ZmRLRNb3yD03k2gXxqU4-__AfmGh1pHlkj-2n0wKGcEjMrsntrSwSwsQVIuUlnt_cOargNumJqLv2eIdIiUGIc2BSMjBwPofJhudnQVILt65s5ChEg8fAvxQ3geKH8G7rw9ywIZ_UdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در خصوص اقدامات تجاوزکارانه آمریکا علیه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657910" target="_blank">📅 07:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657909">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
قطعه «تهران» با صدای قیصر
🔹
من شهر زیاد دیدم ولی هیج جا برام تهران نشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/657909" target="_blank">📅 07:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657908">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzKZKrfM64HDWPTHu1s9ae11Ukds4_oRFzT11pLeQHGxNuRlH_93DG_Cf-kUdxO0agCzz1D-Rram_30E4NgDphCS8L_hB-W3UsJlxdBnFX_zCIP_I4lsXNp53udoCymQ9et1uWpzzxiIflFsdslqHSWW3V_oa-XukaJU9e5NEHLV21B5DMpHrAcCmNUKbchNjJPjDw0abFDJunatGqQx9n_ep1tPCxnvicNcJNMY8K_Apht52inZC2R0QTi2YUHRFKmBOKRi4OOABfSlvdPh8Vt23kyVqzkT3PK6LDYkden_NVidEkSPSxvF9wAOjNCrkSqy4-HX6hB2NsJKG4EyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‌
انتقاد آمریکایی‌ها به سوتی جدید ترامپ
‌کاربر آمریکایی:
🔹
خدای من! ترامپ به معنای واقعی کلمه «افزایش شدید کسری تجاری» ما را جشن گرفت. او حتی نمی‌داند «افزایش کسری تجاری» به چه معناست. او فکر می‌کند به این معنی است که ما بیشتر از واردات صادر می‌کنیم، که خوب است، اما دقیقاً برعکس است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657908" target="_blank">📅 07:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657907">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_YHMkjk8qi-J099ER4NXlGpdLFUn6_mYmr2mKuW-sCvtICXFIG0hPebpfX2V8GQQc5-IWgtvsn6NP3K5WGy-5CDKAHGzm0NTrgxXrWyNVYnBPzkx-a-bMgblh793bcYnJeIu0hrKXStU3krn2AZGwMBa0YTJoWABaJHcUDAfcC-eY7WQfaQNDdP3VZxPjt_rW4ieTNUKbrsln7UBT9bMw9_UVU2G43CFZ9Sl_qLQwV_hhl0rhesIh5f92bRVwv0xENINrDPj4_wTeDkI-RghwyBMaqGNVhnZb4NbO8bFnGZ7pBKutJX7EFP48agZ7yec_OyNomP3Qnx4eo_Evve-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه هیچ صفحه‌ای در توئیتر ندارد
🔹
سپاه پاسداران اعلام کرد هیچ صفحه رسمی در توئیتر (ایکس) ندارد و تمامی اکانت‌های منتسب به این نهاد جعلی هستند.
🔹
پیام منتشرشده در یکی از این صفحات نیز با هدف ایجاد تفرقه عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657907" target="_blank">📅 07:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657906">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به چند تاسیسات نفتی روسیه
🔹
ستاد کل ارتش اوکراین اعلام کرد که نیروهای این کشور شبانه به منطقه کراسنودار کرای روسیه حمله کرده و پایگاه انتقال نفت گروشووایا در نزدیکی نووروسیسک را هدف قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/657906" target="_blank">📅 07:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657905">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdbba6d5c.mp4?token=Bzv0I-bnBu2c-MLSBk5wrLhzdamuuRy9qsLj2bVogEgkXJioYnkq4CiRmuvg8jD5FumKSA2TIDJZ-Y5hGCEZHw620nV0zFxxdS9kU9zTqbPbhb1LiJY11n9w-UHCv6iA5_My-wHKSxuHu-hJVBWDCry__YEa6NkqdlB8QDVZUOTcy34vJIAi3xfl90uN7LOV14p4IkiYMhmyAoeKiDoAMSo1hC-r941SHVk7VjYUO37Ubi1vHK73uMcVuPRrGpaNtJtbofoItMgZnia91IwAASPuUrh5gsVd7i_lW1f7iNwpRT6n_EYmv37mhCN2iPOvr81z6lueNlFxNCP3-K-zQCXjZNKFNH2GOliNbG-wZg9TBvWd1ul7bPXV_9rj-qIzvHM3q5se6prnW051coD-wSV22Hzv5_b8tV8Xu5We9xAXKEG4dvrGPZCCOD4gLSr18y0p0US2O5qQKKrshXjuP_DijncU-uKz8gaD0I34QOHupK4RID7gYSma9viQjkCbZ05z3uvTZxFtSLTT8elaYGBo-eqO8QXupbx9oEP-vAQcbq8facbG0-FrKDa-OYSKk7OEcB_s5Rr_DnJbEnNBqPH88mTGo7FP3GL1dKei7UgHx2yIprnMqX-q1LHBp7plkxjLiYSmntlUdzI1kV27rvnwovL84L3Ej73QNUTVePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdbba6d5c.mp4?token=Bzv0I-bnBu2c-MLSBk5wrLhzdamuuRy9qsLj2bVogEgkXJioYnkq4CiRmuvg8jD5FumKSA2TIDJZ-Y5hGCEZHw620nV0zFxxdS9kU9zTqbPbhb1LiJY11n9w-UHCv6iA5_My-wHKSxuHu-hJVBWDCry__YEa6NkqdlB8QDVZUOTcy34vJIAi3xfl90uN7LOV14p4IkiYMhmyAoeKiDoAMSo1hC-r941SHVk7VjYUO37Ubi1vHK73uMcVuPRrGpaNtJtbofoItMgZnia91IwAASPuUrh5gsVd7i_lW1f7iNwpRT6n_EYmv37mhCN2iPOvr81z6lueNlFxNCP3-K-zQCXjZNKFNH2GOliNbG-wZg9TBvWd1ul7bPXV_9rj-qIzvHM3q5se6prnW051coD-wSV22Hzv5_b8tV8Xu5We9xAXKEG4dvrGPZCCOD4gLSr18y0p0US2O5qQKKrshXjuP_DijncU-uKz8gaD0I34QOHupK4RID7gYSma9viQjkCbZ05z3uvTZxFtSLTT8elaYGBo-eqO8QXupbx9oEP-vAQcbq8facbG0-FrKDa-OYSKk7OEcB_s5Rr_DnJbEnNBqPH88mTGo7FP3GL1dKei7UgHx2yIprnMqX-q1LHBp7plkxjLiYSmntlUdzI1kV27rvnwovL84L3Ej73QNUTVePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دنیای لگو تا افتتاحیه جام جهانی ۲۰۲۶ آمریکا؛ این ویدئو را از دست ندهید!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657905" target="_blank">📅 07:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657904">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtBR5bQlQZ20FOvZ9rYyRnTpGhRCZLBO8Zgx2eCk-R_GC89t1owRVgd_zuV9mr-451sZKkiN0wCSiTdEULfzOYUxeSVjMzlLHCIMCqGHK1iPIBjWQPiS7Qm-a1rDbtCi2oQwljphwmbWqKT-ki2QG-cLQ4IlvEdzRiBgz6icRYf2Jnr0gzCcynDDX7vJjLhunw5w031t4LowG3PDOLQywlm2RPe-xjjOVldmIk1hfV-sR8tyccCciDzrByok3rJsmDc-D7dUcq8QTyIv-Sbf2hd1wxhogwB3iwyXs8Pluw6lEANBmDwIdSwvSsky6_SfDKO8x5goCLorGkKxFSQWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۰ خرداد ماه
۲۴ ذی‌الحجه ۱۴۴۷
۱۰ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657904" target="_blank">📅 07:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657903">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2YaMlxhMyMjnyMPL1yOeBiYfx-Dk4XozgcUuaOeVzROebNCMCsTjOT0LF6LJyLqk1UI-Ee01NRrT1OXfDnahxNVMiBIPHOFHJoNakCjUKx2nrk0whzeb_1JdJPhwu3SEDPq1aMyNox4UtgfTRterUkk1jjFUcYDUdhKEf8ne485nGBAdhjT_VvhQPLKs3wLS_sUohQFXXvHWM5DW_ua8Y-ZOTwhMqeEN2z1fQZTXn5srwS6ARR7yp34YV6G3EWj_Sjz1AtBkepT-NbLhBIvqVl5FlUuyvvIy7GCHdZZYB1H0NYRxjpjU4A9hZATzaO3Sj1qkdBxqgj8mn2RYYUUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سینای ۲۰ ساله اهل یکی از روستاهای همدان
در نبرد با سرطان خون است و مادرش با دستانی خالی، تنها تکیه‌گاه اوست
😭
💔
تهیه  داروهای گران‌قیمتِ بازار آزاد در توانِ مادر سینا نیست
😔
برای اینکه سینا به آغوش زندگی برگردد چشم انتظار همت شما هستیم.
😭
🌹
با دستانِ پرمهرتان، مرهمی بر زخم‌های این خانواده باشید:
شماره کارت/شبا خیریه نیک:برای کپی کلیک کنید
6037691990491201
5892107046740463
940190000000116489768002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام نیک
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
⚠️
مازاد کمک‌ها صرف امورات مؤسسه و یاری به سایر کودکان محروم خواهد شد.
💚
آدرس کانال ما :
👇🏻
👇🏻
https://t.me/+YQ8wu_Q7QahjNmNk
https://t.me/+YQ8wu_Q7QahjNmNk</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657903" target="_blank">📅 07:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657902">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال در خصوص تغییر نظر ترامپ
وال استریت ژورنال به نقل از مقامات آمریکایی:
🔹
ترامپ در ابتدا نمی‌خواست علیه ایران اقدام تلافی‌جویانه انجام دهد، اما پس از توصیه‌های وزیر دفاع و رئیس ستاد مشترک ارتش، نظر خود را تغییر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657902" target="_blank">📅 07:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657901">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
طالبان: ۱۳ نفر در حمله هوایی پاکستان به افغانستان کشته شدند
🔹
سخنگوی طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657901" target="_blank">📅 07:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657900">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
مقامات کویت انتقام ناتوانی در مواجهه با ایران را از شهروندان می‌گیرند
🔹
دادگاه تجدیدنظر امنیت دولتی کویت یک شهروند شیعه این کشور را به بهانه عضویت در حزب‌الله و نیز سه نفر دیگر را به اتهام همدردی با ایران به مجازات حبس محکوم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657900" target="_blank">📅 07:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657899">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تاکنون هیچ گزارشی از بمباران در خوزستان نداشته‌ایم
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
تاکنون هیچ گونه خبری مبنی بر بمباران نقطه یا نقاطی در استان خوزستان از سوی دشمن، گزارش نشده است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657899" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657898">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
منابع عربی از انفجار دوباره در بحرین بدون به صدا در آمدن آژیر ها خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/657898" target="_blank">📅 07:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657897">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657897" target="_blank">📅 06:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657896">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۳، ۴، ۵ و ۶ شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/657896" target="_blank">📅 06:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657895">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
ارتش جمهوری اسلامی ایران با موجی از حملات پهپادی، پایگاه‌های آمریکایی و سامانه‌های راداری ناوگان پنجم ایالات متحده را هدف قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/657895" target="_blank">📅 06:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657893">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">منابع خبری از حملات هوایی رژیم صهیونیستی به شهرک‌های النبطیه‌الفوقا، حبوش و کفررمان در جنوب لبنان خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/657893" target="_blank">📅 06:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657892">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cad7c4a14.mp4?token=hp5fKlnl3BFTaNapc2CRLKmolOLFhdKubxNuLgoH_4Np20u-EyYEaC96A_G6S7dA6QkiI6ex7kMacB2TVc7Vfqc1I-kU6gf4X3QMcBEdiHxIG7SiTw6Zz1pClJuCzIikI_TVjlR-UtW8KTfSMFK0ERzHn1uWWoTBXlyxF8XMcrOQQJhewyR31-KEnMEXPANJu4yerJtH-27f5JmlGJ5neMUzO3r_HZmEotghxOruMdr9zZkzyoLe_u19FxcnJGeiiUxGK12xF0gN9SBBTiAzJWvaIKJYQlRiS2lLoYjJNnupm-WDDEDt60unG4frg3BN0CMf_aMYHZVpEVczmG5WIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cad7c4a14.mp4?token=hp5fKlnl3BFTaNapc2CRLKmolOLFhdKubxNuLgoH_4Np20u-EyYEaC96A_G6S7dA6QkiI6ex7kMacB2TVc7Vfqc1I-kU6gf4X3QMcBEdiHxIG7SiTw6Zz1pClJuCzIikI_TVjlR-UtW8KTfSMFK0ERzHn1uWWoTBXlyxF8XMcrOQQJhewyR31-KEnMEXPANJu4yerJtH-27f5JmlGJ5neMUzO3r_HZmEotghxOruMdr9zZkzyoLe_u19FxcnJGeiiUxGK12xF0gN9SBBTiAzJWvaIKJYQlRiS2lLoYjJNnupm-WDDEDt60unG4frg3BN0CMf_aMYHZVpEVczmG5WIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در منابع عربی از اصابت به بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657892" target="_blank">📅 06:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در پی سومین موج حملات ایران به پایگاه‌های آمریکا در کویت، ستاد کل ارتش این کشور از تلاش سامانه‌های پدافندی برای مقابله با موشک‌ها و پهپادهای ایرانی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657891" target="_blank">📅 06:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هشدار عراقچی به آمریکا: منطقه را ترک کنید تا در امان بمانید
🔹
وزیر خارجه ایران در واکنش به نقض آتش‌بس از سوی آمریکا که با پاسخ قاطع ایران مواجه شد، به واشنگتن هشدار داد که اگر می‌خواهد در امان باشد، منطقه را ترک کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657890" target="_blank">📅 06:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای ستاد کل ارتش کویت: سامانه‌های پدافند هوایی کویت در حال حاضر در حال درگیری با اهداف هوایی متخاصم هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657889" target="_blank">📅 05:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcc150c12.mp4?token=jUf7-kj5QF6eRm7jdo9RdBKn26ZOvFKQ31gSn98R630R14pBFsp4SaCmWegvKluiwuRzpF-_nWBHrKjYSW9WVJS4ZR3A_q7k87nxiKsOtuMhaWYhlBno8sSnsDOV6QqVpaXmHGHt7jY28XYgqp20FhsyEsNFzACvAJa-JgMXpGrkdJFMN3K3YpMDFBa7izKgQgHCNi2VVyFibm97xka81VCoG-kH_LkUcBb068OWNMZsgPOUXsA2qX2HYS7yKIqN5cVnRLGV0QzWbqWUJhIqgf4xl2Hl-VAo6c2LkjlgVNrVWoVVLZQcgRGceYVEYDX3iz7mBPba4N2yh03f6qk5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رد موشک‌های ایران در آسمان اَمّان، پایتخت اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/657888" target="_blank">📅 05:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">موج جدید انفجارها در کویت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/657887" target="_blank">📅 05:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک‌ منبع آگاه نظامی: ایران با استفاده از موشک‌های دوربرد سوخت جامد خیبرشکن، آشیانۀ جنگنده‌های اف۳۵ آمریکا در اردن را هدف قرار داده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/657886" target="_blank">📅 05:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بسم الله قاصم الجبارین قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک،…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/657885" target="_blank">📅 05:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تلاش سامانه‌های پدافندی آمریکایی در پایگاه الازرق اردن برای مقابله با موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/657884" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657882">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ثبت لحظه انفجار و اصابت موشک به محل استقرار ناوگان پنجم نیروی دریایی آمریکا در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/657882" target="_blank">📅 05:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657881">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آژیر هشدار در پایگاه آمریکایی‌ها در اردن
🔹
رسانه‌های عربی می‌گویند که موشک‌های شلیک‌شده توسط ایران، پایگاه «الازرق» محل استقرار نظامیان آمریکا در اردن را هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/657881" target="_blank">📅 05:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657880">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4aee3aed.mp4?token=PIJLSet3qAiXeYS2LuX1vkJT2wQaHJdgJ-JwMr8whP6GsN12UEGISZSyrELXiacNKFE6xZEas2CNuSHd1AeBadBusUAUhdmaGlEJ6eOpw-Mu0QesgoUYp32e7ns9GSeYE59aivooL1wiUbvB5RpiHbB3TVnQZ4w7qb6-p-la9V5kO_XqRcsIO6oA6slFT7OeMyrimDlUTfN4_ECSDPX6PPUD0yFfkODjFKcCWqbC01RrdFbiYJx1mOrFNoSKrutS9yZtzBk6P0GmLxWT5i9Sglcxjkd_tk6fWc2yOiwIV6WopSGEnBTaosO5FAn4u9p8OOmBqQgeZhM4iiad0t7wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4aee3aed.mp4?token=PIJLSet3qAiXeYS2LuX1vkJT2wQaHJdgJ-JwMr8whP6GsN12UEGISZSyrELXiacNKFE6xZEas2CNuSHd1AeBadBusUAUhdmaGlEJ6eOpw-Mu0QesgoUYp32e7ns9GSeYE59aivooL1wiUbvB5RpiHbB3TVnQZ4w7qb6-p-la9V5kO_XqRcsIO6oA6slFT7OeMyrimDlUTfN4_ECSDPX6PPUD0yFfkODjFKcCWqbC01RrdFbiYJx1mOrFNoSKrutS9yZtzBk6P0GmLxWT5i9Sglcxjkd_tk6fWc2yOiwIV6WopSGEnBTaosO5FAn4u9p8OOmBqQgeZhM4iiad0t7wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاربران شبکه‌های اجتماعی تصاویری منتسب به اصابت موشک‌های ایرانی به مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین منتشر کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657880" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657879">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سپاه پاسداران دقایقی قبل پایگاه آمریکایی الازرق در اردن را هدف حملۀ موشکی قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/657879" target="_blank">📅 05:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657878">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزارت کشور بحرین: در پی به‌صدا درآمدن آژیر خطر، مردم فورا به نزدیکترین مکان امن بروند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657878" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657877">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6EGfMIz50pxFW6uVC8MqqijovPIWnYyxzbTGstFdBlF_aXHPYw3URPVXSTKMuQg6VtuPKGKXEn3E4BsL4nAPMTqmf_FawDPpRfzfb6KhiiuO9ZCSVHQfGz0lR9okpmjh3oqW0aM3J4nfp4hRyyBTifbwbolJaF2ZdhCSJelG5CXVxr2Mek_m5kC5B8u4HjFEeKOQO712b5ADwY5mFiaCn0l3AtQmkIbN8wCtD2klE0f7zA-Ji4GedOtcZmhIbf4rQJDk7689efmnjwaMyXdGfGDm3KrEC2sgqy10jKEFBtTXuQH0N8U91Onu5xaG0ITQKTWQXsZ2Zh_XgFzRatRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاهده چندین ابر دود در آسمان بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657877" target="_blank">📅 05:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
صدای انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در کویت و به صدا در آمدن آژیرهای هشدار خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657876" target="_blank">📅 05:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
انفجارها در بحرین قطع نمی‌شود
🔹
منابع محلی در بحرین می‌گویند تاکنون صدای ۱۶ انفجار را شنیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657875" target="_blank">📅 05:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تکمیلی/ انفجارهای متعدد در کویت و بحرین
🔹
منابع محلی می‌گویند که انفجارهایی کویت را لرزاند اما آژیرهای هشدار فعال نشدند.
🔹
گزارش‌ها همچنین حاکی از آن است که انفجارهای متعدد در بحرین همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/657874" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صدای انفجار در کویت
🔹
منابع خبری از شنیده شدن صدای انفجار در کویت و به صدا در آمدن آژیرهای هشدار خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/657873" target="_blank">📅 05:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین به صدا در آمد
🔹
منابع عربی از شنیده شدن صدای چندین انفجار شدید در بحرین در پی حمله موشکی ایران خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/657872" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات ما به پایان رسید
🔹
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در واکنش به سرنگونی هلیکوپتر آپاچی ارتش ایالات متحده در روز 9 ژوئن، حملات دفاعی خود علیه ایران را به دستور فرمانده کل ارتش تکمیل کردند.
🔹
نیروهای سنتکام با مهمات دقیق نیروی…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657871" target="_blank">📅 04:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657870">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بسم الله قاصم الجبارین قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ  سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک،…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/657870" target="_blank">📅 04:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657869">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدای انفجار از شمال غرب اهواز شنیده شد/
صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/657869" target="_blank">📅 04:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657868">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای سنتکام: حملات ما به پایان رسید
🔹
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در واکنش به سرنگونی هلیکوپتر آپاچی ارتش ایالات متحده در روز 9 ژوئن، حملات دفاعی خود علیه ایران را به دستور فرمانده کل ارتش تکمیل کردند.
🔹
نیروهای سنتکام با مهمات دقیق نیروی هوایی و جت های جنگنده نیروی دریایی ایالات متحده، پدافند هوایی، ایستگاه های کنترل زمینی و سایت های رادار نظارتی در نزدیکی تنگه هرمز را مورد حمله قرار دادند. این عملیات پاسخی متناسب به حملات اخیر به نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی بود که از آب‌های منطقه عبور می‌کردند.
🔹
نیروهای آمریکایی هوشیار و آماده دفاع در برابر تهاجم غیرموجه ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/657868" target="_blank">📅 04:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657867">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
یک فروند پهپاد MQ9 رهگیری و منهدم شد
روابط عمومی سپاه:
🔹
در جریان درگیری های هوایی جاری در تنگه هرمز یک فروند پهباد MQ9 که از آسمان شمال خلیج فارس قصد نزدیک شدن و مداخله در صحنه نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش  رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657867" target="_blank">📅 04:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
صداوسیما با تایید ۲ انفجار در بندر عباس: هنوز دربارهٔ محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست و بررسی‌های مسئولان مربوطه ادامه دارد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/657866" target="_blank">📅 04:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
سپاه پاسداران انقلاب اسلامی:
🔹
رژیم جنگ افروز آمریکا در اوایل بامداد امروز با بهانه های واهی چند نقطه در جاسک، سیریک و قشم را مورد حمله قرار داد که به یک دکل مخابراتی در سیریک خساراتی وارد آمد و دو مخزن آب بخش بمانی این شهرستان  منهدم شد.
🔹
در پاسخ به این حرکت شرارت آمیز دشمن، رزمندگان نیروی دریایی سپاه ساعت ۲.۳۰ دقیقه بامداد
ناوگان پنجم دریایی بحرین را مورد حمله پهپادی
قرار دادند.
🔹
درگیری‌ها ادامه دارد و پاسداران غیور ملت ایران در حال پاسخگویی به تجاوزهای دشمن هستند و در صورت ادامه شرارت، پاسخ‌های سنگین‌تری در راه است
و ماالنصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657865" target="_blank">📅 04:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
صدای انفجار در اهواز شنیده شد
🔹
منابع محلی از شنیده شدن صدائی شبیه به انفجار در اهواز خبر می‌دهند.
🔹
هنوز جزییاتی از علت و مکان دقیق این حادثه یا احتمال تلفات جانی منتشر نشده است و پیگیری‌ها برای روشن شدن ابعاد ماجرا ادامه دارد./ مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657864" target="_blank">📅 04:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در قشم
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657863" target="_blank">📅 04:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
المیادین حمله آمریکا به ایران را بی دلیل و غیرموجه خواند
المیادین انگلیسی:
🔹
ایران ادعاها مبنی بر اینکه نیروهایش یک بالگرد آپاچی آمریکایی را سرنگون کرده‌اند رد کرد؛ این در حالی است که فرماندهی مرکزی آمریکا (سنتکام) اعلام کرده بود پس از آنکه جمهوری اسلامی ظاهراً یکی از هواگردهایش را سرنگون کرده، در حال انجام حملات هوایی علیه ایران است.
🔹
ایران اعلام کرد در ۲۴ ساعت گذشته هیچ عملیاتی در تنگه هرمز انجام نداده است؛ موضوعی که نشان می‌دهد حمله آمریکا بار دیگر بی‌دلیل و غیرموجه بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657862" target="_blank">📅 04:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کانون صداهایی که حدود نیم ساعت پیش در بندرعباس شنیده شد، غرب این شهر بود اما هنوز دربارهٔ محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست و بررسی‌های مسئولان مربوطه ادامه دارد/ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657861" target="_blank">📅 04:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c08e8a50.mp4?token=MeMD667Cc890v2tQdGS5kpYffMN4XBhyNmemSN9leyAK4iHpCHM3i7vXvRNVXHZ0veQ6NsNhiy7A2CzccRsH9J72FUYd5IMJg8skoPlKcqeDXw1rM7IekK31VO_5MYVgrmQPTLhF7_kQoq0JPO8EsRKVfaD77bM8Sn--2u1gkgcGpkU5YjPLJr71kxkjECHuJtX_4_YF0R732I-ZoGpF5-YcyNtQC9zCAImUfGE0IJ2FikuZ8yAahf7KnD33XYWFhtfqgg4r-R8f8j6l3cNKsK3fBFM2Ncbm-FQlv_KJ3wVX2jfI1llmbOFlGj4xw27ojcqW-V2iy4xGwqbJFW9x-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c08e8a50.mp4?token=MeMD667Cc890v2tQdGS5kpYffMN4XBhyNmemSN9leyAK4iHpCHM3i7vXvRNVXHZ0veQ6NsNhiy7A2CzccRsH9J72FUYd5IMJg8skoPlKcqeDXw1rM7IekK31VO_5MYVgrmQPTLhF7_kQoq0JPO8EsRKVfaD77bM8Sn--2u1gkgcGpkU5YjPLJr71kxkjECHuJtX_4_YF0R732I-ZoGpF5-YcyNtQC9zCAImUfGE0IJ2FikuZ8yAahf7KnD33XYWFhtfqgg4r-R8f8j6l3cNKsK3fBFM2Ncbm-FQlv_KJ3wVX2jfI1llmbOFlGj4xw27ojcqW-V2iy4xGwqbJFW9x-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشات اولیه از انهدام یک شیء بر فراز آسمان بوشهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657860" target="_blank">📅 03:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد
🔹
این صدای انفجار برای چندمین بار است، که در جزیره قشم شنیده می شود. پیش از این نیز صدای انفجار در بندرعباس، سیریک و جاسک شنیده شده بود
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/657859" target="_blank">📅 03:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657858">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
جزئیات حمله آمریکا به زیرساخت‌های آبی سیریک
حمزه پور مدیرعامل شرکت آبفا هرمزگان:
🔹
نیروهای آمریکایی به زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک حمله کردند.
🔹
در پی این حمله موشکی که ساعاتی پیش به وقوع پیوست، دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته و به طور کامل تخریب شدند.
🔹
این مخازن شامل یک مخزن ۵۰۰ متر مکعبی و یک مخزن ۲ هزار متر مکعبی بوده‌اند که نقش کلیدی در تأمین آب شرب بخش بمانی و شهر کوهستک ایفا می‌کردند.
🔹
در حال حاضر روند توزیع آب در تمامی روستاهای بخش بمانی و شهر کوهستک متوقف شده است و تیم‌های عملیاتی و مدیریت بحران آبفا در تلاش هستند تا اقدامات جایگزین برای تامین آب پایدار انجام شود./مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/657858" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657857">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
گزارشات اولیه از انهدام یک شیء بر فراز آسمان بوشهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/657857" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657856">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقام آمریکایی: دور سوم حمله آمریکا به ایران درحال انجام است/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657856" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657855">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در سیریک
‌
🔹
دقایقی پیش صدای انفجاری مجدد در محدوده شهرستان سیریک  از سوی منابع محلی و ساکنان روستاهای اطراف گزارش شده است.
🔹
بررسی‌ها نشان می‌دهد، این حمله مربوط به نوار ساحلی این شهرستان بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657855" target="_blank">📅 03:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657854">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
صدای انفجار در بندرعباس و قشم شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657854" target="_blank">📅 03:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657853">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
صدای چندین انفجار در بندرعباس شنیده شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657853" target="_blank">📅 03:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657852">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
گشت دریایی P-8A آمریکا که از بحرین برخاسته، همچنان در جریان حملات به ایران بر فراز عربستان در حال عملیات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657852" target="_blank">📅 03:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657851">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
منابع خبری عراقی: مشاهده جنگنده های آمریکایی در تعداد بالا درحال پرواز در آسمان عراق در نزدیک خط مرزی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657851" target="_blank">📅 03:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657850">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گزارش ها از ادامه انفجار ها در بندرعباس خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/657850" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657849">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فاکس نیوز به نقل از یک مقام آمریکایی مدعی ادامه حملات آمریکا به برخی مناطق جنوبی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657849" target="_blank">📅 03:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b372cea86a.mp4?token=r94pPkQJsGYe4WbYyKWs7Tmr-9PA4plIqpCS-8iYdXvNgHOU2x8HxAI9ghGwvxa4EHj0vF53L_Vl1a1mVwFa87X9USyl3W2gey5iUbxtSd8V82CXO9QcIxDrdMb58ZEDk0CaWbGvuha3RxbZGWxHdvVjzthLtCyx3Mzepmi9QnyVYAe_a8cKkdSYXyW-EpK1rgkneeLjzvLIUNOnkOvARuJCx7i-X5CMPqB9Et1fdrAdCcx-rd6cQmPD0DS_pp6W5jQrYcLNaXZCmI0xJGTr60NUN6brgiPgCrzawP9J6O0Waju552MVgXuJY1PsUNSWqVICzCO0yRI_a9hZLc_XwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ، عصر دیروز، درباره هو شدنش توسط هزاران آمریکایی در محل برگزاری فینال لیگ بسکتبال، گفته بود «فکر می‌کنم بیشتر تشویقم کردند» اما این ویدیوها چیز دیگری نشان می‌دهد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/657846" target="_blank">📅 03:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/657845" target="_blank">📅 02:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657844">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای اکسیوس: یک مقام آمریکایی می‌گوید دور دوم حملات در ایران در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/657844" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657843">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/657843" target="_blank">📅 02:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657842">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
شنیده شدن مجدد صدای انفجار در شهرستان جاسک
🔹
دقایقی پیش، صدای انفجارهایی مجدد در محدوده شهرستان جاسک از سوی منابع محلی و ساکنان و روستاهای اطراف گزارش شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/657842" target="_blank">📅 02:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657841">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f35de44f.mp4?token=CY9y_GJwQ9FSab952NV9dwoMANmgdXKl1aWB2woGu4k4yc8VMAwxF4O4NZFUj5FmGdHmAuEedENw4erJl4sfjjoo1VtFqiu9DDF53hD_eByBzVHeoVSamRZEU34PQoTlu_EX1Uzy4YWzuTKvYm6J3t3cAXYtserGrlC5LS4hCiH-su6l-p1L69e9lPWLNJdsEV6fRXugV6LX1QIxl5_jsfLSsOWsR37dnRm-9EBYRlFYh8i5memwk7MgVh9bDGPRfATU-j_paSmdKgtGlIa_hJYctvN6qaIFUfmxCXuhfb6OOwcnOGsRKzLslZyIIrxrHhrew-9zosRL7CbjMgKN_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سه انفجار در خط لوله گاز در منطقه داغستان روسیه
🔹
وزارت امور اضطراری منطقه‌ای روسیه گزارش داد که سه انفجار در یک خط لوله گاز در شهر کیزیلیورت در منطقه داغستان روسیه در قفقاز شمالی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/657841" target="_blank">📅 02:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657840">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نماینده پاکستان: شکست دیپلماسی، مأموریت حیاتی راستی‌آزمایی آژانس بین‌المللی انرژی اتمی در پرونده هسته‌ای ایران را مختل ساخته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/657840" target="_blank">📅 02:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657839">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد
🔹
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657839" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657838">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آماج‌نیوز افغانستان: لحظات پیش جنگنده‌های پاکستانی اهدافی را در ولایت‌های خوست، پکتیکا و کنر بمباران کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/657838" target="_blank">📅 02:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657837">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42fc015a.mp4?token=Sx3x6WQtwWQHVLpxbYUu5roLcm_hPPD2_7GFzg0DJ3T0wftl5wSJnqckZ9ulGCiFzd8RiLaFZNNnOwlRpVr5MO45Hejn8E4V34YFQ3TsxnzrLZBNUmbo2HMqQgUstt4WnQWYbMLp-zJi88Ua-UJGQtopTh0AN5I12vD7NMu5A3kyFV8emre1ij3HSpcqcRim1eoDdOHssspzZkKPGra0ZTCqDwdEf8RpaE8I0vhB-iu9kqIeD9ePFONFipz83VcixXETON0MNXo-A5XJzrZ3jGtxG_roE-xXauEq0wuDneTUfmYIIy5qwKwiAO8tMxfUcVQj8E6AZprXilThf2M7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تحلیلگر فاکس‌نیوز به ادعای تکراری ترامپ مبنی بر «نزدیک شدن به توافق» با ایران، همزمان با ادامه تجاوزات آمریکا: اگر فردا بشنویم که به توافق با ایران نزدیک‌تر شده‌ایم و تقریباً به آن رسیده‌ایم، فکر می‌کنم کمی پذیرفتنش سخت باشد!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657837" target="_blank">📅 02:26 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
