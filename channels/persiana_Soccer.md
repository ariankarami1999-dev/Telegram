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
<img src="https://cdn4.telesco.pe/file/VTowa2YT4JSguY_UEIRY_83e8fAdAX4v44whZpun5wcs48GhKwWLWs2bR9q8LeaudBMKFlZu2VYzVqQBR8MerMGe3dSWBkq9HWG4M7DZwdV7MB2cEC-v1ztGIbVOvlJmyotDyY3bIa8DuSxYBIhVU5nBcwI4J95X15JndBzyeFKT8G8tPdChe-qsLFfVSEsXGYScBA1j5ahRiVPQLyIIr06ZwXdM7qEi0U8a__krAFk7biDnTvFm85x12ZGXRnKFogl94AfbOkS2iC8udDRPk6v44yohFRESkqupz5n0axXtbhpITh62dsUHjhHXk3FoUWWcRA73383e3qL4KNvrjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 448K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 00:06:01</div>
<hr>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H95lNf2fCk4lxft6rsXiW_Ef690wPr_AmuYTF-HePvx2mQbI2C7szHFE65SFIiP_cYjyyQBiuN-fkrZcy4eaojxrtCnuKaY4LymK5ZaqlHknydTuIJJzr5I2Wd6ux73b2aCYveY_n7QS9_6yz-fOcozfAYEe-X8z-iLyTHDk4tKGJlv0XkKIUibEotIIcyS8b0CCv4VH8cqIDRmf_hJy7as0VA5mVkXOgULUVT-LxybRHsiF6TzWhaBzj5dDSbwuWWzHaLQio7zg1pIluMRkNudyFy6QpkZ3lLGgQ5aCA81CA04EV3b3drDAWWlMGEHN3js9nxZ3z9yWhTCAtM5jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nptYs_YOGGuBwK_rlCSL3E0XVMd-uLuCVetKT2M86bZYTY0cC-1jJ_hhzyJElgTILdulF2tKHo3KgAhBzmJPPg3zgk-GPBj6DRnqj1ToHAKcnApkZl9NoIDuCBQE1v9Bu4oFwJTpvzwPImVe-84kLhbzru2wdNbGmGkjbXwfyy8_GwhBnboM5Ckym0CPCbVLN7Z_USPpP7RptPAcV39-_PBap2PM6i2qsYLaXX6rblF10dc2MXoJkSwwQiId11NpYoGGNzl2CAbXlBsNNrQjKlnDuPm9LnlGs4u82XWw_je0o-MiVSZHVEm0JxhEyhxUG1M55XZkPrW7RC2_Vhxhdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jli9nvZGfJe-WkqX6PQhO8njeVLHZrr273jvGfGmVI6X1EzIb0mw0b8YmZtMEf2kLvsvy5chcPPNX5vJr6OS2vkewhl8I32BpOYrZoMb4fVFkFr-PbdV9Qp8J6LIBQ32J4p2z7ot-KEOjj9iasGDbIzSRiZlT5opRwJloiPJPBkdL3VHmQfoysf6kAn4qtWJTxSE1njE9q-JDlzOh3U6rXcApD366IE0F33MP-NGE68IBq2ddFrD9uPTjz3tCZrEVf7spvlfrgOM6syt0GwBnMmjAltw1V0PXIKdkCd62kswlULXM9VyPC3iSRCa2SZJysLW_0OcRRGddg3uQW2cMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsnSkZgZxpg4Svha_9sApbK08AVAY2doH97HBXp2jfBCHqyPa_82ezS-Su6zMTIf1fmKZxNtTegVormRXl9ZgQ9BABHs-sRIDW4n2z3NeN4_DbTvsyqdOO_10u3lY5LO649NiGkoRiOZlAvQLXgh9Ppvt_cV5Zpj-U_1IHKTIpw_JCaP72_Zq1ZInBOkIcNeghPU4YNjpHK5Td0O9Q2Yk5G7-AAyKdLyh-ms8w9olYnKZJFncMIaT2AYj3dd9qFaXfTtSJP-ZnscJhfMuqVwGxclg3TeqHdxf8YFL3HxDCW4Ysg8P9q0bd0IludCZhiZ5pkn-UDQOe72mgqnM2ZAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tge8y2urWsws3A-8hbklBcGLSbsWQRRcktttnIlq8J-SjkRcnr-pEDfsltG4-tUJ01ZALlLBrqvdAD-Q32vppaX6O3C2F_ssqrvlC2kBXybsEc7BwjlBd5WT_5oDCqSIwLuLiy2uOZrNTJExT_WI0zAin-06IV2QhbSDxNX6sAEAzwx5kbGQufl7vWYDD5u41oEqZg1YTfq3gc9z8CbGKQsCSV4PkJTm6ojw4OuMgrtH2GSsytWfcvcxQty9gMKlFrZdQJpuPSKJ9b9VGTtuJeOkSCaZ6GiszDQK36WMKdtYsxYoOgc_uFDPPVEetiG7hPMnJIVNxedTFCBVdqFsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRQ9J4brAc0LASee7RmnVQC2VthjbKQcbfLPhBkVy73BPFBLe1zVUFdih1_7PJW6lNttPNQ1La9SI7tpb-GymeU0jzNx-1-5NAzDwMqRgvTnXkALX4REzQ0fLLOVpZ_6-2BlRT32X02F4lCJp2Gr4Fba_FgucbwWSG8orqQ2wGdhTqgzK8msuvIBJPC7BIdZ7Wbd6hz7xOBxK_9nJjnNO-nDBw0ynUZ_sHcGI2j8ObX7CAVCRxJtsNkIoyubp8xJ7lkGwogfpd-lM8jccyCMLVmxrWcGvfGboUXuQvTCEYVgUaLQcUA2Fz6yTzqPjPZ9tUxJY7LAzoJwquTPkbYFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tukTtHbbh3kPeTP2Lon34EOHvXboEWjiWpXWeJTx7cgI62t1wcTn2rlTybmZrrwohf-H7FlzUTUlGxt1WUdPIa-A4CuYrOm3SJheFCjCUwRGciZ1haCbYLvBJq3LTlzQVTUNGVcMEcUDAx5dk77gDzxEGZ6DdMNZUA3Hyq4qHTE8KLdBZ4MXgk_91Poe63VqkgAKOgo0JGARRLFFPt9GANAg_xRCjl0wBJ3Z4-3Eu5Vf7lKWPkTvvZ3M7s6aHM5MDs8ZSGRzNHvHacI9EKoto6EnzCbGfJQubIshvwiYkkWn8yJKoOQb8es9Shv5ztf_68TmO0jfNoB8GxA5IgEX1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=ungUb1xKBKeYf37A1t1ZTkARD2LloXTT5Y4opOH78vJp7qnTJZrN_NAQ84jISmXLeftmWgajpSQjagKRXTB5n0oKBVfttaStFyZnfTeP5ynyzc38qWRBdKZ8H8fcqBD-6oybvjELsA-hj-gjuJj1aQaGAvkgjDcGkRs_R8ha8IZZqANWacXjL6j7Rhkuh6RpCO6h1J1XQ_ETJFT2svDU7bCZSvp_RljKGAArtR9v6Yv19Ofca5tskqbhOExqq4wNoy7e9GjgWEsTq5Zg0C0hEoSNydRqz9PMFTYEVU4chxNtRw7dR_CXQ6mXSnL2F4U9XbBbH9IXLtfv-bRCbH0A8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJOMRgcj0FSEbv-KqLUQCdyXLbmqabbsGTc9-oTUaTpS1WhfF6otYqgOR-WHVKTczvM_aW0RKX0X2y7i-Chju8yPBLUGpH1njMtKz4-g6Z7a3LbzTmsYoyvhokSwameM19HkX0Yjq0R4y3W0ypiCN4LeOllq28VcfKe0AmrzbqNIS6xzwd2TD_5rMKRC6jnO2nVv4nWqz-TS5oNhb491-owKFSCXCMdGqweLf92ck5SCqKPtQCU1ygfsHYzlvCfHMrf-nOVpuIlnMqmfDKeFZoktP4zBQzNLVDg5Sg_eYnY5ntNNgVw4MTWDU22VEwNBA4QaUW92WjAEaEj2LfjLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwzeCgz_iEj59qi3qk7DaSaFe5rpXlzPtPEkg2HhTBSSJIvUdCyydTPqug1SyZZBnbW67cU8BtcdICQjTUgFd5EIS6saUHBIdGIluMBtWuX-XkD5bcepYzcNr3cxS25eVMVdjTDE1__-1K9OsvRYY4WPyXAtRgVoAGbHsrvOxz6PWfk5n7nNuw1D8MhlcexGc86L-CBU2-HehO9kNWfRqV3VPFGixPBimxidoUiTHjTGCGE_JmYhFeO6NI13sMsvxDAQs8OqaDiDYj32EdhTAGbITS6ORny1dZifgeJsXQ6WdzG3w7fydU4CA-VBuyqJNwzilFDpCMRNfC8AsYw9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30431">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5WVrSVjol1nrf3cqkLglFRmzFhcj8qCvjLxG2JxbKcr12anLKQwWE_JrLvxML6V2kycOm1rv75t5asy3vVl2WVXJWLzpw2LoKjBNTL2nwL-t-z435fn67NgNUDPaZSDbtuos9kI6AgllRE5v-UpFN2r8C82dkafuUii59g0lLzIe9QYwy-DIJnnqnkC0kuhV-XrCkw2m4RBNMSpZyi8oCOveEKruVh148Q3ogxHEvrCTFwfZZdJ34q1iRUqrketJKbJjCKRW-tZTqu6l8VSta3KH4AwOcAIAIew1_PUbHCzu29ZD0dkM8qItBhtvB_vKFWY4DkK2fm5KuXQZLB7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لیگ ملتهای اروپا
🏆
⏰
شروع بازی ساعت22:15
🇹🇷
ترکیه
🆚
فرانسه
🇫🇷
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30431" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=mX49xOuoT9ZZ_pfF7OGbuOkOMMKmFx1yRo2vyyMfCCZU-hW__6DrX6moB-Gdmuzh7Dnb2EPJpPoYmq29WT3-gGL5gi_cOdZFEuS46SUU_PpYJAn5Nid4yA586s7Jvpu90wcoqqY-VvGuYm9RLB67C8FYeMBxXrrB63TxQlX1iKAavLmC8Qi2EJnV11EOuGtxIjP9yQ5FJ5kRqfPDIRvaAXZGCy1kFs2fgW4sBvad2DQAHYoPt3jIzX5UFKZwl7ioZJ0ikxqcaTf4s-3mEzyMYzwFGLQYSEr3vJLapOM2WKvvt6Nk-h8d9i3zBshX9TxLwTujVGbIJ8QsYSMqMFHXgFPaNCaFEtvTp7UnWt6iVMZHNjc4fxXChyeKJ7JxXaUvQAV_eWiy2dHqUdpjff3tr2etoIYDulaKVWbhoMLGqTl5ZdmOVkHM75ipcBhFjCyA2qTm_kwuIV_hF27HVnLhd2GyNEOWntAwW6VWS5NPEh8fqO1AIHjd5MrApEfTltBFzfg1I6XiVPt1eGLNWEKH7I-xm9BLR7n65ry4FlMfEy34LDmjA04aALFcW7C-bHPkK2ag4MDiIiREISeKwRp-RVpPURRu2sB2Jy9KxrlOiPEWKg1eiI4RvmQGlv_AzFoUjuk7xgwDJzcriDmBtS0xUnURdtrwLefFasVasuHt76Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=mX49xOuoT9ZZ_pfF7OGbuOkOMMKmFx1yRo2vyyMfCCZU-hW__6DrX6moB-Gdmuzh7Dnb2EPJpPoYmq29WT3-gGL5gi_cOdZFEuS46SUU_PpYJAn5Nid4yA586s7Jvpu90wcoqqY-VvGuYm9RLB67C8FYeMBxXrrB63TxQlX1iKAavLmC8Qi2EJnV11EOuGtxIjP9yQ5FJ5kRqfPDIRvaAXZGCy1kFs2fgW4sBvad2DQAHYoPt3jIzX5UFKZwl7ioZJ0ikxqcaTf4s-3mEzyMYzwFGLQYSEr3vJLapOM2WKvvt6Nk-h8d9i3zBshX9TxLwTujVGbIJ8QsYSMqMFHXgFPaNCaFEtvTp7UnWt6iVMZHNjc4fxXChyeKJ7JxXaUvQAV_eWiy2dHqUdpjff3tr2etoIYDulaKVWbhoMLGqTl5ZdmOVkHM75ipcBhFjCyA2qTm_kwuIV_hF27HVnLhd2GyNEOWntAwW6VWS5NPEh8fqO1AIHjd5MrApEfTltBFzfg1I6XiVPt1eGLNWEKH7I-xm9BLR7n65ry4FlMfEy34LDmjA04aALFcW7C-bHPkK2ag4MDiIiREISeKwRp-RVpPURRu2sB2Jy9KxrlOiPEWKg1eiI4RvmQGlv_AzFoUjuk7xgwDJzcriDmBtS0xUnURdtrwLefFasVasuHt76Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opMDDiemdi0x0C3H7jd_MTTE_KzaSpNUoVtlclfwQAuLygSGJlI7gUChzM6pFins3ptYqdcn12OQZ8Ib6qf1pmy0Q4_Bq3LGHkdM0vCHvhRrnqwqm3OevjXCfTZBqshF92xr_1eTNV4GEn5e4ACUuZ0adZcn8yWTIFrVAH0Rjg2Go1D2jtpgmAZGq6-hts6YBOc2autw6dRIy55HnGYF4zVvjrT0aodrj353w9_YlBgcxs0prtIDy7rqXBZr6AbDobT0Zsl3EWyFr7VZ_9dCg56HxGH5z3ZjzrvD7PFVhAgvRqmIfWPGkCmj5z3cKfu4EfjAAKnDbxpjS1MazaefaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEJHaFtFd7S8gDkJgECdzn63PaL8ope9Hc8mJPLrFnxbzu9kmlTekIUQIpXmzAk3RHb1VRy17rW0jFYBBr6dVdUDZwrjqE3hOdfXRy_PSDGP-axP3ZmI0PAxwKSIgjs0sbGkrHkVzRPaEYvlCb2QxGd9tWYFmmLeuX7p77jJS__TyKk3w9bzDb32MjqnFMUbzr-ompiUajrWp2forLB3-qR3caPXvNg3O4cAUchlNjsn3ktqPxHE0iqZp5JiP6uzHZeGtevdOJablC7U3SOYE2PGMwz5rj0DSTWWpgnZrj25m_fLe9oeOJvGAnDXH3tCaj1iCoXmIk0HqhPqzjsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ROpXu-lf4aDNJD8Jojca7ZJJx-6ahO2Z-i0DLrDVbyswK8QHnarLw8wXdbNV92K7V9aP5Q8RJw8_zYs7-xuEArYv1Sk_OupfQnVuXbQZoFiUaJPDnosOLzB945fzvsWf8FL8UsGMAO0vVALp30hGUS-SSouFIGPWQR9I5k6xhkCEMjIcLP206vE9MzdfI-x9wHMhiSaOOXvvWwKEPfS5osovtxQQPfSWm3o55MgMosxLiiVI1ehxBoW-yq_dYsBPAkWeBHDtGACWkkV14KhefPG_dmN1wj9P5qEa4cdDW2xJhC7u4jo-8kqlWw04RN5UL_-wlwzCCurktBvV60qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXwNEXBLlZe0j6mlpcRT1p5QDY1coFF0EiONaWiDv5lWeBeLaXs3Bisf8VNbzQmmXLnc-bz6Imi0k1y-3nJo5o6aq4Y21JT1IHDrVHJX7w4CeTYCfAqJ6ph8ynq9hLkOhMGPhNjx3PBvZsmoA1QMqhDhKXd8aq9-mUmweKovXCz4hm6p5R_AZlKPDWUaebMiuigLAnOfc-WXh76wV7sjDfrxE9v_NZQdj4fpVRSgSIuZlq3nzGICmcpORIQyN4TXLL0p2CicwjBv1fXmqui_5UvgM_CWIHp5GcwDvMtqNgGQbcbZAF3qRk-PJ7TC--SYFg90dHtXWQJIb8kZ09xCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKeg_MXkMwX6eJwwtxV7B9ETOgleFCA1z6Kr4ma2ckLs--WUJg5A5FdYM_uvKxcKHZYhs7bMlyuqxWQ35QmWd_v61lB8xGAxImCXQiTHSO_MGjWmk9HhqNBKTfmwnkC0V4D-7F_-e4wfxuSmFyojCjB23aLm0pX0Du-raBfvXOhBN-izs3wO96NCgdf3pHPNyVHS1LQI-PQCyZIkSBAWZWzUoUhA98k1MVC9fePf-A-CP-oCFXiKNg9M2XYEnJFRuCYJAqG_NnO5u0AE8T8I8fxqBwVFVltUQFCJrjZ6Qu2CMcdL5iEFgjv9X8g8KkoyxEilZNlTIRTwI4aMWwQYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d45DIiONNpjRBzjF9Beowy1KF2RjNi26JGWm4_oRjPQ_eU7_tBRf3BVhGYQ1y0XkJvyZXyV5GnaDjZiFrL5u6z9IZCK2n1VPWnQmboChQmcKPg65R5Hj1BKHXnU1-aFXqIZ9aC-CAPKdIvZz-Q-Qd0Ni6yV2DPMEPsfA7CaQ1yKn9eZPfGPA__G2xp0T4IQdWpt6DuH6GGZ_QwezqAFzrIoPwDGUfw8PzOINw0_FALD-K2T9-YrXkhk7pC9jBatNz4Zykz7ktr2aCNaF6yOiwkJ1gQ7obd_-bnK7egd4NU7hoH4aS9Azgy_FyCDojQPGCsfRJCV6utuQKWaKTKzzRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puylJMJfHy1seRcvDw-4YxUdaIS-iBD0weg3P-h_3KJrlJmym5m9p_gYbRX5esGmnK3NYG0s2JJFU3TUqrnH_o3wwRr8kQlbBVhr_-LCAFkSy71tvajT5nJawy51GcFTzMDga4DrgXZ6QvSRDqRwtM3338vmJ_xVvct3LHqyAHbMhKfTPWttOcRDvbKkJ6LoemmlvTmVSEaCR-3LG6hTacp5XMDeOe8kgUpF_KKtvnrD_jHUu0MRVbQrz2O7qC1pd4hjq1s1IzWu7_kgk9e7gbvKW7g3RGiS3I1uK68Wfom92V_Q_iFyBEzER_h_UaZeLNteRWMV-v52Q6NVmo3KBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFncDItagjVkmrVSTQCxCslKRlpP2OOYlLrlLM-YwWVCOijZ2FSs7AmvyDCifTPj2kRTxV5jEOXPUzq-DWWjAw9-mS9_eQ9Ui458B0CJ8skIxfGoKEFh_cslakE8M6XcYlEkWuwvBZyiyhNgzFZHLRf0Ng_BS-SATMVL8Oc_z-fwmewwuZkqCR_TiAPvvztxf_QnhPTgHu867284wf8FNOFQhYbEKR0ND5xZ99cuEG_j7rZEJywiAywdKcpwHub7I7I5G0MfbGYvH3ukTIihwqibZ07LHEHs5dLPTacmOp18HVmkUzgOS47TRAlNzl7S_uJ8z9Xhck2a5mTDaiEfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsGpL3E8iU7v14gslkFA8jQ-2pssZBp2PXdcqdJDnfOPrrjaUPd-VDB3tXdD3L3ISvF3zvLsbPdUQFivuPJVImFhsRreNQ_WQS-1wOQkQKQb_GSQj2pDLv4LSp7525_NaMAuIC2jUkm4u-4H_rHw3-ssItfiE3ho_RK7OxC-98HVGMtqeqRUcF4iaz6J3C4QQtKIgFDPj4lKmxLKTINpYronWhXRugw3GvtmjSjYvDx8c-XooyyTS3r1_2pEBv6Ez5mZINoBYb6483jh5M8OzOdGXawMEDAWpDHUgXA5O8JD5IooblonASnobdeyu0KE1zZlXCCkmd6L0DJGt7TauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzy_uKJY09wq4mc6ZO5B4DpkFhd5a5F8MGXeCmaloQd_104r0UOUIJ0pSHhTCmUdsxede9jIyI60798aXPFZ4XTCNVm6Mgk1kE-QmsbZtaKFPKxCONWCxzySNibFCRBfJPEOHiKrEujNTMd9TsQysiZ_srR883tWqJEuNz09Mh1WH62dSdr09W7hJDPT3NHHDU0ZYUYkDZd57yZefR2qiJHM1pCqtOQ19nfHmeGYxtW_QNEfK0gaZTmnr1kxl4waQEXquzYdSAeTrYcFmX1IYZIz3An4bOBi5dAdxY7FXI1N7zmbJOZiteCgKiw7WmRIm95DP-t_9AhUy10PYL5GBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlT_kEJ5nr4h8r-4GsUncZ9vqEj4z7kQzHAtxulz6W1oimPN9_IIhflhyIQAt1H5G4c2yXSllPlSYODhqZeJsYpJGR1JQcXgzdfNhDUtyK5imcrfdXh_i52g3k6ss84ehKFEuHwW3YywSjgsa2p9eYo8ofYYgG8H6euNW01kEwJ6oiqvyDTX5APK1J8_vc320cLqySnqikC_-kpBIq13bPICm3vVWbRR_Bz_MQP1cFewD-yEj4zRizX2azWJXYP_x9Bws49U-WUsNO1uQFtEx1tTDycutS_e0--gyfL6QSGqNgGJvngWBahZ6UP4B8XWzdWD-awHFvG09TmIXLaiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=mVchqkatbQbwqDXJ8zVKtaWsr_ju8WZqrAKSKc11zFVzencOIoQ581e8Ze-OAAZuUueBq2uCI2Cs5vS_I8QoxuDIM_0q4jvMzR7E4ZRehLIGXSEbAWpUOYyyIxOZZk2w-ixYVlRhwFoqDrPUFWl8k_gNKC9ouAQI7ob208K2Tbarrim7s0len0NVG1PPmXIRgJx1y-zOdPhWtEx2qrO85R-P59afFOd96N9irme5gcjcgCvBjPSulJ-dzM0PoO5CNqy9JIJIB_6WSPB_NE849bQNQcaDnpZ33UKjSWf-qQmTvzhVZ5klv07xdaALzJjscaHAPo6H3IBXCflydc-u3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=cUSME8yactxxTEimJkkhWb7ZWkLChe1crAN33vyE0pgSjz4h20OhEQqMsOhQ17OdnNvFJLuXiMijqKL2sFzZDrKfVOQgcwzjQR665RHORxYDYBJakzB2NJntHBdYo7zmQ6iaS7ew6C1W_gTmIv_Iu_tOwUhVha_4nx4RPxwR6_anqU4rXjNUJvVf5XInv1zkaUNRQlfSp-f3-7U-fvZ4aNYtERXLt46YJrFxg2yYCpzE37P_aKZtPgD_Xf0fKEvF-BWYC7PHntMxCqh_DsfF0KxYjJB2hTkq3BY4y5icgRtoGmUBZleg9hsg57VB0X5RjGp4OcIz4YISjGZos3eCxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g20xPmk8yfy39zGdsokKKzSB-MRQW0Ht--JUMe5nbDNh7_YRnse6anVV0RnQQV6OvIkyHTuc5c_8fPx7Y0KKNny_bvp4W4M9Q7CbHUyBu2ybrNiCPu690gHsDl6M9CHmlNmIB69P2BjO5K0aBOPMZJnTTeoxr9cFneOZOkVXMWCoDaFzuq_KIGOSutAP-YjE5T-Ujre86zvv63ZTP6ySEDWJSYc8diKOpFCcntqrt08STBterrTZzpe4_7Gw-9g205I5nAokspVVz7J0rsi82MnKdpEpRM1Dp0ORKVz3G5UxbeZPfsE2aSBkJzDH5ok2CD-TMrUSHGSPLgINtl_U6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp0M6C6f2hKSqpGsvvpYPZlBiyZS_sNwYlkWNG2Op12UorpPT3om0I8-qiYoq_D9d1yykJXM6TryvXuGl9BIzaEZSCJjXGJF2u-mwPBZakhrTECSBMlxDf5yPgYnxC4Y7EpIpADR3ycqFaZCoeBJURAmMslhWYa86661QpXMrysna_mkwDyRppLYfHzY-8ihp_4Fy6smIJOvdSVEl2ohBYYHInzD5CEkfXJUbLP0soI6wNFw3S4I0Yc2U-8qAgI6B6iiX0ezAK7BuysoJyPRp3AEhgfuLrBVGE6Oi-JX059F6QPevJIRqYhf_vgiL55imYRjRqJfIoUX-_gLZZWMlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=WXxVI7mZLmRnYm74MrBuyUo7EZ1xG2pqH1ozOqwvjXGaXXydPaAxSMg87xjwImcpya6tx_tIh2TnuOBhdv8kpRoW3Z70KEYvR2pMLF3LLtkp8gF7rXsOkz13NKkS9CdjHs2uZ3v-bwOWuDXjRN8_Gqmg6KCbpDDw_842OELgZvVC7I3eJzPoK5vXUXAXM5KpGDFM33rRgEX7zdfasSkC3GTcxXLpiXmJdWiGcIIl2ShVDAPh1OoXvbkm_pFoN1S8f0O_fSzXqD3vmtfto456x642miDDmzsApF2v4xP_IwzVXbm0BhdPriFr5qKubwtaul_cFt5ZvSe64ILDqZhKT5bj7EGNM4qblzgP-wbO1VnS3M-0bGfDKjnSbfyLAd5RnaG1kSJoro47_kBuMOF35_tLKCGOam1kmo4NWYFpA_9lc4VJ3ciK0r4r8nYaqI4fJwTw0puLGn46_70UQmjaZ07p7eIIg_uuUrhgxyolBI1T4J48GQicN_7TKDXmZFDJGGNC1B54bRHqxp0CXODBDGegDz9s5R_xWwJ2gSGQgTz7mvIzE_1dMpXoolCI3VRoexxRfy4wxfQJsY9I8kIYNZqp5n5HZRjfndmMI4nNlHh3KNAoyPaH9ZXGuJrhC3sC25p_MHqPBKTgC2WQHJS2lLar-RvvNATssUKPnETZnto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=WXxVI7mZLmRnYm74MrBuyUo7EZ1xG2pqH1ozOqwvjXGaXXydPaAxSMg87xjwImcpya6tx_tIh2TnuOBhdv8kpRoW3Z70KEYvR2pMLF3LLtkp8gF7rXsOkz13NKkS9CdjHs2uZ3v-bwOWuDXjRN8_Gqmg6KCbpDDw_842OELgZvVC7I3eJzPoK5vXUXAXM5KpGDFM33rRgEX7zdfasSkC3GTcxXLpiXmJdWiGcIIl2ShVDAPh1OoXvbkm_pFoN1S8f0O_fSzXqD3vmtfto456x642miDDmzsApF2v4xP_IwzVXbm0BhdPriFr5qKubwtaul_cFt5ZvSe64ILDqZhKT5bj7EGNM4qblzgP-wbO1VnS3M-0bGfDKjnSbfyLAd5RnaG1kSJoro47_kBuMOF35_tLKCGOam1kmo4NWYFpA_9lc4VJ3ciK0r4r8nYaqI4fJwTw0puLGn46_70UQmjaZ07p7eIIg_uuUrhgxyolBI1T4J48GQicN_7TKDXmZFDJGGNC1B54bRHqxp0CXODBDGegDz9s5R_xWwJ2gSGQgTz7mvIzE_1dMpXoolCI3VRoexxRfy4wxfQJsY9I8kIYNZqp5n5HZRjfndmMI4nNlHh3KNAoyPaH9ZXGuJrhC3sC25p_MHqPBKTgC2WQHJS2lLar-RvvNATssUKPnETZnto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibqb74tCHmmKJ7h2iEkdgmQ2JtKjlPIVhXQXIC6VaCWqn7Hdb8s4qev9hpl95MyblBG6pD_-rms4brsvlR5YDrlvZp7VcM2m6fTjhJ6goTwAYV6R8HSal17FtzyZklLW2lFQ3_RrLyTOCIrPvkaR_N9dkNLu91uQpxcXdUnFxAwT8kde5yEPTi_bzhP9FQ6qPYseX0IYpAB-ZpgoOVtUUtJz-4Q2_acJf3ZRSZ7_VEWDDcgWKB5bFaOH3tMauH2ECTVuB8iMpb553GVx5xywzfJv2Z3M5b1sTZv_ZA6Db3jJOU9rKaYDahvSsF61dP0zdRikN2PeyvGKNvG7OIx2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgxSV9UAuhnxzRuBEknW-ujqgIx40Sg4_-zGKVMYKqTRpvsUzudHcXAhYxMMi2mLu1p-CFzKOLClsNHifMdE4pMMiGFy4lYhdTA_S3pQ3Ukkyd8L7Lfjw7unEPpf2aS8dn1_eM6jGTaqppziivrO2rtxEaUF3WL6J5eH650DfduNrFyFwOSGGO9cuzI3iIOQkCU-1y3B1lG-rppjyRdTWR3K2vUwu5shqiB-C0qfK2n79yS6TTjgz1WiJVqf8eVxN61LFNqIG4feAsTc2rLYOqAa-Of1sOe0eA9hqIdU_IWzkPiFZnJzyq3EyOiadD_S25ay2mhHKE7tom1sLkbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVPXnbEyWXJukJkSUvnptTP1BmbdnsIkID2UHRWGqKYK562P5XCbMnw2uXdDegtbC5A5g5hl5szvtV9MuQIz63kMyrlCwT48Vi7j7Yt1PgG0sgWySzwZ8qDWCXxm5PJWR6aR-Sx8dFKCYTnE-oOHH3wrEcUrAjxyvIit3QCybzWTvLyajwxZjIsQQhFbPAyPG1cCHx4glvjVA3glhcg_1p2mIulOGCnMD29fRd8WYwbbFxmKMk0nBsamDcukNl3I4kbMTlKr3L9-AC6Zpnb9Brc9x44FEMg_HGVjSl9aWIROlvhfUh74p35r7Sj8K3ryXQu8ingSEKXSNbCvQUEFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyxrXvq08QWydoMzFTCpI4jdIfKQBpb8u7JSIHHQhS64VGKMY0lY7VUK8SzEQk4slM49L7X4BkPq3QVQ1iS4OOdWsC9oa_l8fmH2wvd57W3uLTHaCJ7p0oumedh5soQBGyfyvKC5XKuywmBwh4zHcs6AUA5L87ZvoRjHJdZEJmAq9aLSYluPNTtzUUxeIn6o8lg18JHWufn2kwyH5WlMIMjr-Hcl8sl8u0orqwORZia5RHGWtr0IVflrdHf6c1v_q_Rq0l12sJdnvBypzWKA7Ictd2IDDfQiIsA-7Ny0L7hh5H1V5aqOjl1pyItLs6_GSmIXu5aHyFapf8kXmFW9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLg2wivdnaP090j7ByZAi3BeRnU96sQIO73u8_7vsadZIJGVM-XfTlBCfguJLQu8sHC7eDTMJAmVtmuM8mtnjlP3T98XdBkcBh0Fq4brnl-X9Ke4assk8PqIE9rfqNg6sOjSRTgF2jeUuSYmlRbY1dg-cEaTHRms_N5SpM5FP8rPyFJ205HjpM9JxybI3vV9-YflMjkw7G1Wp_ADYNJUyRDxEMTh35rCMqcoiIdG_Simae906Bdj4Di4yaYy3JhE2Bl1x_3hkIqrnpObo90Ovis9q9gHuVC-rvbpgHUJKPqzuosj2I_JgYK-CxTYxX9WkQYqLEvX7d4BkyPyk92RPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ2gNFxgfWLMLhfK-HhXTzpYYIC7S82xKEj8T3d6Y0A2OAsdRBA7puTxG5ZhZxwEmJrAz3hKvo8b9U6VkEiJ4oTBEOlKCy2DTFlBDcLwgTF0ZndXRXlnoXYQe0uB25NqHQ8rWnMBjxYwz0zacFqYmr_7i_ZxQHjrxYfMzRalpSb4chqkMPne8pO1HZzglP6uCEJwwBTuif48RzTSPSqW9Pwdd0G4q0XjxutrAiaNB37XIvBEnRoMroKNeGwjZa_SxpEYlGLDLGw7z6uq_Wua3YGH5gJ9hTc94jxZro0vJlgg-Ys3i4bYRlZ0MReZQNa5ObKlzos4S6Op7lGXa8p5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeepI--RrTRD68vdD8vPZZGpTtjWQ8RmnkVAjrPUTJHss2StLw9eAepVEQTg6HRKtZ8d8Osjf1cJpwEk_CUAhJ-1Xn30giEjrCrUJhdbAtjDInJZOGS8Rh75mrQYvSS1uJlK6aoX7pp9d05nrO0ITGyFFmfIkhShLHrTZa1iq3Ph6crczmsAJjDntXU8z9FG3uYEQBaAa_1EjEw96D1kKW5vpNz8A4zFml_pRdxCbggLGakyfj8LAmOyPcQkXi50GLQPWrl7-a62CuK1q--attbQJlO9Arvm2gYm97nI_osZ5pakwoDsC1dDty7QDacsucelwyPtwbGKzBPWEgKm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV8qDV9KK8sNdBaYRWRds_TRG0DRMykov_2MIfScYDtLb04UNrphOdzf_JqKGEgKT6ke3IaVMCIEsxFEba6rtMBpQpJjKL3dBhbDMR9Rfa84uSgJkYDO9fPNpiFgj9JjEyKHNZJUkN_KYk_OtpvPsEsDZA5AZZ0Jij3nzd0imQTY5-3OyYYEqwNvl8TmC62tZGsaMeFuspgVyGgCYc8JAZ7OAUB2GnxN5-Dtv003TzzFRqfwC7WGBdeRXuVk-0bPzNnuH8GCXBrwz0aXzeejpOrI5ZaSL3wtTyQem0gQVrob5HljYAFJ3Gv8OSLRKvA8_9DwNVlE2brh0WPCzRr8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M42l54RW0sRP0IfvlvQgEqXxUry3fVCTboqKiLHVCAgxT8Z-NBE0k28INM4R9ClqtTvIhhO3iMpCoda4M-iVGW8BI7yf1-4QxeM6YyN1bdgxpeD9cNcNZnx6rh-NXf6zTrueRS95LjarTGA2tguWSJ8_Ng4Rale0YwUkvlQfiSfcTJDsJw19voyYMBYAvZh7_jiAczDTPn1llgjO6_jud3DVOUFU5trQjvNOdbc-fkmyO0HWrpOfzi6IpAD3QueppEbdEx98hEwJa_XHdUmFuS4ZChd_6mmQRN48DtBJ7Dj8-Qcl_P3x4ZAh6DipUNTUW-iCKklmQ5L_z9hn7pxPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30403" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciky19wKEdCsH4otU3zgKEqyxP5k4Y11tqWgSkRBP1YItwNq0PtJkpv1zXHf_MqIwrKb0nW5J5C5pCvOL-4gfprjQIGFljHKVBVNh6ctL1nf-a3NoHQaObcrB1fonxBSqLM0xjuu2BJnuO_re02jtSgfiFE9lPjyt9eojqwNHyU6pjmK1B2Avmwf7PJ87bF_Da2ndfO3NtKQU8Y49cXzUMUxdr9rnoO4N6GTUVwpcOPBbGCGrG2XLWZJt92jKgCrUcBuVb9e-JyZ8V3x6Onxk5O4xgKLQFyizCilHznlbcHLL38ByJSuayockq0Hr27WFHRqlW1imCct6k4PlOjEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=nLWXan_CBOTnNxeOLBzJQ8QI8Adk1QchSmb2xzQitZDZBj5ZotzvM9HU0tSlNlTJudGtW2rh5jLq5KF4y_DA-L0rXufn0Hh7Bx1u0LFA__BonHr_DF3IcVRHMYLpW6VdJCrmoYXormMAoHQEzi85kDDLI1165GWNEJjBSa_67yYSXsyHdUaGQmWwsLVL6823uIpuqLoaF-GKRiusVyuMyOaZEYTRVqV9YrnpKO75jPZktz_cA8kDuOp90LKqS13Loik3t7Wt5sbRoSvF-0KOyu-RFid5lbgKIORTyF2NTawG0blnAjaJIABD1h9PymEy5ZWtTJe7Jqva14-mCPLuDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=nLWXan_CBOTnNxeOLBzJQ8QI8Adk1QchSmb2xzQitZDZBj5ZotzvM9HU0tSlNlTJudGtW2rh5jLq5KF4y_DA-L0rXufn0Hh7Bx1u0LFA__BonHr_DF3IcVRHMYLpW6VdJCrmoYXormMAoHQEzi85kDDLI1165GWNEJjBSa_67yYSXsyHdUaGQmWwsLVL6823uIpuqLoaF-GKRiusVyuMyOaZEYTRVqV9YrnpKO75jPZktz_cA8kDuOp90LKqS13Loik3t7Wt5sbRoSvF-0KOyu-RFid5lbgKIORTyF2NTawG0blnAjaJIABD1h9PymEy5ZWtTJe7Jqva14-mCPLuDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQKdr2cUGvOYM0Xpz-1QGmBWriRbcozwGyWbx0zaKTzVmXvTEjBnVOTVmp-xgjqJpwIo1gHZZYkPs4uOeUAettPDtEArz6srz2Ev2SV6EN1j0huH3VfncuSuJDUrtAw66WxEbYrz-wqFyIM0FmZT6YSO7RGNG8PW0jfORVi50tnBLH3EPdv6iQQvNafj6xd7fWrnseks9eVkCciXXek0aXJ5BDJilc13ihvsvNB1uixMBQ4IweGirbZTiNxyS1WwMZkF_ioEGRVSTYMyciBWxCBkCbZIDs8S37txZn3S6o295E2vzpf0OwOfqc5r4jXQGVTACN-pU8cT1KPWduIr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=Q9jMIn-xgKGgGPAkHGw7sOMT68CaA-B5urGXnvaRQlsLKukRvpQEEMdHkkvFcUCc6t0aE8puM5GvjeLeNeQmDi3VfrD2fT4ThOGL4WaoZEjZFnChmOhXGVa335iuzmBU7hxJttad-gaEyxVX37_BX-QHvxvIxnFULlG3FFZBpxeG9i2era0pZlu8jnZTmR-UJ7ZwgSPXPojXW8POnpXb0Uoguv6GGWTJk9gOET_SoZyxVkMC-UTMZPDScDAgkc14NXJ-F7yslJ9eZ1bBKKloGvbho8oFA9EPzfdE2jXDn0GsKrktmSmaymG2Eq98Mf0cvtmCOQR0hbca1G39NmN7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHrP4UTV1oFeI1G9M7Q0tVUAVfXtZHmUHFwxmyjngb0BCMMvBeiDVGlrRkw74F8y2M7wqWLf51HBYI3mF8QO1k85jkvAhYr-tUp5C--CexjsW_QeXvDC95pSPnSEq8F9lEhpEOdsxdxObBxopHxytrAEH2dZXNm447mP-UJI-ufnl28SS1iiNklI_vmvQpyM3MZEcB85f2zEKBt3JjY34KUN-JIWupwZJvzi4FCOqXj0zkZPZuULgwZNv0H4eklQnpsi7s7r07k2BVhKEkpZ0zvtytTN8XkyIslluTeQ7bxRMF_vNzIaBicbjRiyIPU85JQdBOnL9F2i5rLEAYIFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=FLaqHfvzbU_NOQ6ROQVc3lq5e_rEHMPglhLpB3__kUfpiL8lIk5JAwIa53g_Y2laXu66fU-6MSUIwH_l3vQYcDIiu6ie5MZDeM2hpG9-USeJ9wvN_cVqsk1HqYOKB3XKWbA4BUd9fRxIuNsWzAabnj2OI98rbzlCNgyNFb9TidYRl06NzHDIeyetZKtBRUQZcrkPjkG90kVYkgtiwLn4nHYUQtTfwhN0YsVdyeXX7Yew_B_cONcRE-5g0korh29JhipD0FqHXUNiB04FTqQmJf6YvCchFUupllrTEKZB6JcGLQYYJDbfd7ehsjCJIQXbK1Q39-Lg7JpmvVXm4yiOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=FLaqHfvzbU_NOQ6ROQVc3lq5e_rEHMPglhLpB3__kUfpiL8lIk5JAwIa53g_Y2laXu66fU-6MSUIwH_l3vQYcDIiu6ie5MZDeM2hpG9-USeJ9wvN_cVqsk1HqYOKB3XKWbA4BUd9fRxIuNsWzAabnj2OI98rbzlCNgyNFb9TidYRl06NzHDIeyetZKtBRUQZcrkPjkG90kVYkgtiwLn4nHYUQtTfwhN0YsVdyeXX7Yew_B_cONcRE-5g0korh29JhipD0FqHXUNiB04FTqQmJf6YvCchFUupllrTEKZB6JcGLQYYJDbfd7ehsjCJIQXbK1Q39-Lg7JpmvVXm4yiOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYrREcwtZKX0j6Ca8AtJBxtBfPmZBC0PTTcpGExcF4NlmOUyxXDtoLy4-SzzeuZsfSzznp75D3LmJ0jDgDbhjVs3wFsYeOcSkzpPW7rtJhr8_4vjiJxfYt8jzpOvKcn_IJc8OxAwKw28M2YnCOVfDuTCTGzM83zfLE8BaSRgMv6zQ_n44SZfZAbkLuqE53bnHe_kGLLiH1pMDcU3HO3beweGn_OgHHOJQbh9ppIOYUKmcLi4-crXNejAFdbhxVmnq4LPYokAbCxeT6Nhv8F5EC5uT0LGL_ZYKZCoqGmb9J0-M4pzBJIO3rQITfIfQC6tk1jgltgeY1TCRVcDrOzOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpEIA_HSktP64JmlYBvIY0txNqloHJNXOqCXRPz_HqotIsffY4V_8a--Ypv1EkfMer5Bv6ZO_Tk2yk08SBrQCji-Aaw3ho9Ndl9txGKikd0BK2UfgRcQyXVZagoaE-hvxz7TSkx5mG3vppG2PfapqpvtnFEmZ4Gizd92dipr1kae97-RddK1-bmp2ygYUwXv9aXrDgkDvltz_39CnUTXdbCDvH6H71xCbvlvDF1defic3wHCMdn6_zPDGDYmtp78aTI-byfr5Sm9nhWHnKbnsyG55ntlUHDNutyG_fHJdZojWKZtKPmh1R8Tn1TQ_0YB4MbJXHJogqgnEEEgwwYee160" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqtBpa1X_msjsX53XLquAPSUX9DY6vyk7lzKAO6lMlNSor0qzSQrewhlipLmQEhihgqc3H5LljpZiaWyiDNAzoSOrVWY7GS_ez0lI5K-aS6T_r0P__noHlYaadWfTi4z08SegTpuygqOruuE6jQjwRvOng0Fze6bzDhkzgy3IgAxVxJEQF3l2LSczg5VmBgU0vDKzWP36gQe2cfWYrdn4G_25Bi-9cXLeQEW9u8jUkxwdPiLGOKPodNrkaT1w6fxh1njkU1lK2Yd-68U0gQxwg4G5tz-zrdSVVpgtQKokY9U5Nne1Y7rrAzRBgMIhEECyI-__RJ9-TyQw1LyvXJuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng2kCW4TbwJpbJi0qWembrtUf__4lG6LTfeOHKOXJp2EAo2H-zw4UC0I9bGd8NtzhiPQbyPPAwLrUVUxyYBPaUBZfa2BVbXPN7h4ZQpPh8W40rXwzNC6bDo0zvx_82g86MKMzgO-9IntbfmwEQHViTQOOp7rHLC2r2ReJixAvYMvxfr-Yjz2Pzr3laOYD5Tfwy1-MIQKFtXuTDFnOAqjMOPdR5H7IRr19J2ySvmCOnRWp9G4UgU2HXDbvb615Dta_ce-7wyUoYQmb6X0VRr9V_8kgL5B6eYSA2-UiuC6rn2E4KGGSfU2fi_ZsDuVoDsyNuvmHKWRliOI_IucuX4hwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=rFmt9QRYU-ChXU51vuY6Ej1EfCAX6ztbngOfIyKfccdxr5UVIcYZv8vGsdQlrLRamDDdtTTCLR7P7Yw1d6rulMswmHN2pj-yuPzVQTxWml88pHB5aJ5xPEI06s7vX7PDb0Xf3DVsfoXSzzDCKfkxrMwptnpo_QSgG6G4JY692msqrh_FwhIvITOWw3o5cDj04TnJCU5CgQeCl8bN_UeGoYgHZfcsaW9PJL5DwZLCufDlrmFVWFN2cjQfLsk5fTCqkrKCw4PQia8kveGofAqfUS3Du8jC6A5zOWKznTNZLvTkxfwSuYGF9Ue4uxoBGeIG_NoRpFwHj-5Cr2LftRZDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=rFmt9QRYU-ChXU51vuY6Ej1EfCAX6ztbngOfIyKfccdxr5UVIcYZv8vGsdQlrLRamDDdtTTCLR7P7Yw1d6rulMswmHN2pj-yuPzVQTxWml88pHB5aJ5xPEI06s7vX7PDb0Xf3DVsfoXSzzDCKfkxrMwptnpo_QSgG6G4JY692msqrh_FwhIvITOWw3o5cDj04TnJCU5CgQeCl8bN_UeGoYgHZfcsaW9PJL5DwZLCufDlrmFVWFN2cjQfLsk5fTCqkrKCw4PQia8kveGofAqfUS3Du8jC6A5zOWKznTNZLvTkxfwSuYGF9Ue4uxoBGeIG_NoRpFwHj-5Cr2LftRZDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn8z40OWiSAtSOj5zCER0B6Fim6FVPZpwijqt9PjTGuN89dfIWejmpdZT1-_JfAlVkRQOTwA-u3tAEFpe3BDXlQLEysT9mtgYFl6khRkdyegdvPGQXQNDyZyevjhhrHDamy0hX6nX668j2NYeD_jUuT1KBaNm1Lo3ERr3dPUkVD-Di5FDVNPFsH6usxljm8kk6fOQyZ3YfM9-ftdKx-thTlqo9M7mRzVwsT-iTktSc5OqFJ_BYTWS9Tj3pAHYndesLQtJeOJNZzr3M-Bp4VJI6_96OCF3mLYeC1mRTgCD6lgSUqu6FeYyRGw9SBwTGQPprIGsBadQ94MyUiRtwO7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKJ9VeVEqjhXk7-S2a48o0c4MiIPGH-RhbAKXj_jwHv4IkERGMDYBM5QnTolmWGG90xMIqpwNEHgMuGAVYfzHXWYLVqxKYYtamGLSTR0LLLYJZC2GhUgcCh4MlMTMAcZZalTb9ARTmymzywd_207axuE5Tv_-ODiDOwnA7KZBOm3Puz9Xk_KYkQLUsnJWnBtx9irsUiM7scCd6dHDZBNYp8oWWXStBpywFJrJh90aVmXGy2tlSnEVm8lKZlzwxHqkU4i8gThYihTVGYN6hk_RSxTVlH9FqbVQPYs22OOydohrC0YHlKkFQxBAYviASDWDjysKQw2bp1QOQx3ZKK0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qteFQ39KTPXUF6zIRSWqPUFvAMAJi6Uk9O8hkJhPxEpJhcu8OkvDiQmYPrhqYo2nxdj7U94Fxl83e4B4UM_tCLOxviWMXC2wBicIFQH3nF6xYfqwRG-oDM4OCIU8AWl9t7ze7st1HR2Ssf5wMR7N0Dd8UQSLuxnMX0TAg7GOpCWU4nmGtvuSt5u6AZCQjqTO2i1rJiUJnSmUq14ZYwqjKIMJZXdtIbbJvpBpPEFPOqJGbv_lOY4LrlqxM37NhpQSY64iRPp7IZcmldxuAULA1Slh9o9rx4rFXRVAGFP3gE0A10UL7IU1WPTqcI0IS7tsDqQcRqL5SzVVGUd_IoA7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6_qhsjTa2dV87ZiBmCSIvno7W33_Vlt-1x0-v634JprVw3772mMF3jedgbstlwcev07XzTGwaUp3P8OYQCdxaT1t8pCOFKv9E_wSLxJe6uEr2gatjlUXksyVhbeEfVS6kTSoX3cT5Sn9_UdP3yrzbKKcEl23iIAOlGfeeu54IqYjSgiLtu-i6g_CyTKn8TorbyHJViMIQYyP_dpgRH7rOsupFJKpo291q46sMMKrBb1Fayan7xVLgHemskHHSyQO0KFKFcYVKgQlo_aYsLe6k6VcWdBnMYx_670CFpvZLX5d9nQ0FUSH2Ce17BiOVHx5ccszNtii18afGCXDrcAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBqjQoYRhX4mjY6LURP3wrYQPb5z0bFoGmMqCHKjmwlscpkDU_UCB62HK_qPi98uImTK4ZkRwJfRkSqxeEhweOh6KNrElBOCqsMoJs4dFAbUB7qHkwl12-YuOcZFFM4_P2W12Pi-gvg1IQCLrUoXbAPMj7gYByFGhv9rC49DktUCSmGlUNvs_bDmx7Cj5HZxlY9pWR_ZrekenelvswVU1KZx34qrODw8IAgOzRvEiPI5Ngv4ZPBhFzgJeVhSdfpDRVwqo9Gzre7vjvglvoW8XXvich6nHI5Kjuc2Uh378zJHz3yrnO8kgMLuPobDEBdO5ESqiYoGfdz9W2UvQpXs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVoGQnWc-vaQxffVXJmA4i5JdO3Ds6zNBtL3fDLZypXnoQ5xrXOUQCu2gaTUNklmCSALoKGFlwK8xIwhKAt1oRtAfuTbB-DbTq0cABP4pK5SRR4u2oswWaTJtHjPtFLCWv74Ahz3Rcf8NnYyI7ut7SXdmDnFG_0z4mCIBWtzBSEQeYD8fJorj8HezpRN6WG6XVLjh7B77h7tIbbOFsmDEj8DFbg9ileoA8_CCGiNMUIA1oWHMozNuGABLYuXq_wsKRuJ5t-MYHmKuSUS4bjXyVgq6AwMjkg8ihrEcrEGxvoY7E9DhiLSMcI6LUqQ2n3s8OfLv0EZTI_QVaU-ytGWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcC0T-OnKQD5TPC6ZojryFZI3-ZqTPmhS2z48drKXnnpBRdwVPKPnSMu7WCP4jk8k8O25uamd04awXApWcVyBtMT1o7--i3s9oQVSbUqvjd0QOkZ9tf6sROPsJrAD0E8MzC6MdqFR2a6CQiiYkHLrRvA2v_Pk3jx7uLr86nVenb41N8tK7yzC_5mntRYNWVRCzoDKe5uyOsvsq9Nc28-NQ-Kv6hedj8mzDX9u_r_7je5WOR9Tm7YSBH4mqGjLCCrFgHEuRwK3I6S3toVjdBfj_MUod69YITyElAddSyz0dVZoLlRdVXQzaelUKbmtrDO7d2YqnW8maECmHztt3-KFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=NpT44szQfPbKyuvSSkMIFYzb7Z1dTqzrRL2MJqWw0qWt6gdg_BznjMA0GcslbiTZL-QGsp5IG0C_ZxvDRPGmJTbysQKOtNMCaq0PTjQ-o3rJkV-WddjHwhE6DoTYfhP1w2syFO4bu660tZx0Q9lgqBrxKH5fUokPcYBc04AdYAUCK73qIX7Ry9NDnqBvLRZSR84QPN2Cw9uWXY6HSMREOcIEkTVuXCnbIdn-aso_hgLpOk3syiyQfdc-HdAR6dBg9bM5pVtsmXgxZkEYb1EwCI7jgU5xNQtxHgU7wvNth3wucI0UOI4xqYr6DUKn00I6cNE3-oiZCwCHEdBYkdkUyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=NpT44szQfPbKyuvSSkMIFYzb7Z1dTqzrRL2MJqWw0qWt6gdg_BznjMA0GcslbiTZL-QGsp5IG0C_ZxvDRPGmJTbysQKOtNMCaq0PTjQ-o3rJkV-WddjHwhE6DoTYfhP1w2syFO4bu660tZx0Q9lgqBrxKH5fUokPcYBc04AdYAUCK73qIX7Ry9NDnqBvLRZSR84QPN2Cw9uWXY6HSMREOcIEkTVuXCnbIdn-aso_hgLpOk3syiyQfdc-HdAR6dBg9bM5pVtsmXgxZkEYb1EwCI7jgU5xNQtxHgU7wvNth3wucI0UOI4xqYr6DUKn00I6cNE3-oiZCwCHEdBYkdkUyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRQg2DAobtfQ963K1I84j0fkg1943SG96pqYCCEVO89IvyYOPCdUlcL9VgXjfX4t26Hg58kPZEGhFvhRdcu7bWl2IYTqjMkGG9QO_U1HSgPQ6GJM8ZqjX25J--6RTjfM_svJTiZ2hJRawsrj8DnSD-H7ylqu8wkXucVjKHB4PukuJdTMeZmhXzewdvnNFQYalLt9paL35gel7tKhuB8yM-9ghOvW-8uoow2sFrDAJlRpfvZW5StRozZlldiPkmcGbzuUPi-EkCck2tpj197A2p1shAA5mtL-7PPAJHmVgID57jWJPY3FB5kEwqrSGaxeYifoTfXgfvi3l2KAhU5Z3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPN0X_-IYxuumgqDRlCbJpBv3oLDIm24q6mWcKlzXc8V3NzDyiGUg3k0GADAfU5BGPLd5L0zt_VoRpIxC8gpj4wjPxyTMieI9CPakRF_lR8vMbD8aMvvm96SUomYvBNgZDfIebnntn7zH_juhrD4F2I-oekHGlESjMuVI3gWUfq_1mr_9UCzSTbIFrEtkd4Vb_0DCaXTm5EVxguV_wZQw9FPZOooqFHMjyoAP9pr_-4uNAqte5EQgESPiJ2wA4t4VglndmseUKUuZwZQx10M2stY4P5RAezmqxwhvYLzFhoCbmPUB_KNTig1yvnMU-rw7IDmavmIvLWdrzJ5EAJw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj7Rw8pNzHD-fJdWPaaYz1vhb7Zw8lcEcEZmqKNz8DnJZm61bZLazGuH-yHef9qx_exkMopGzdkFjLZwpz6P1nkgLlX0UFdxUDKh2stx3fg97ExtjNxwvgst4Jv-eoRmjZbLqlqmGmO_m2I6kxW4BvmOSbBpy9H02-AoVDvqqlioMLXu7UeZLvbN8gr8lhuukX3Z0kG6Otonw6FTmSW-U1N-aOureuQ2VRcSZIPW58GcjjIZAEIec8MDtoPw3OczdHVRaM45kOEGY5NmIDlJxA1byqzUj0kikozJrQI4SnRpdqaFx4W08aDzMRLlrXhIPpYlgY8svYR19uMdkz6img.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LVxCTPbN090nMy3j4ROlfY3d9UnljK9Ow5njxNK7uEgZXDPPn03flYrQKtOHHHAUyguSCUF7ubVshTytQb_Bm5aJJKgQseccf48IrmoviRbwiT4ERWmpp0L_T9KcuOYGhtHvtpfnIZ6LwzcaXFquXKCfFkpj5zneJ9iqkLG2PZkozRJweiOWE3Bqe6CML08LnUzfYJyd3c8-TJkR6Wl48boOD7G6aLN5GFC3fXuhXPuO6or37WRH_5RUfgLGXzts8fTvSYW0eddEs_94PvxOH6OL4k1H3izpldyRy5UhqElHNwykc4Y0MatESer52zBL9wgZEbbBmYbsXHdwiwvz1j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LVxCTPbN090nMy3j4ROlfY3d9UnljK9Ow5njxNK7uEgZXDPPn03flYrQKtOHHHAUyguSCUF7ubVshTytQb_Bm5aJJKgQseccf48IrmoviRbwiT4ERWmpp0L_T9KcuOYGhtHvtpfnIZ6LwzcaXFquXKCfFkpj5zneJ9iqkLG2PZkozRJweiOWE3Bqe6CML08LnUzfYJyd3c8-TJkR6Wl48boOD7G6aLN5GFC3fXuhXPuO6or37WRH_5RUfgLGXzts8fTvSYW0eddEs_94PvxOH6OL4k1H3izpldyRy5UhqElHNwykc4Y0MatESer52zBL9wgZEbbBmYbsXHdwiwvz1j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQ5rr6ueY-BmVBs3S8zF-k4Bnc522bNl21Ia1QiBTFDnEqF6y7in-K8qTCA5jsCB6o0lSJMJb7GlL2lJaV9EWtXPpB6yD1nFXmo1THVUai_4DWad8azphDCtcSOb7xK7vx08CyCya7Dkv6vbbo8AihCh9jb3JT_IXeD9-DWJ-vzbD19SOHECyeKsKtBanLjq06QSiqwmlKgZfgW2P6wSrG8LsqagsP_v7DJPuDyE-SkFTT5YB2gsomGJg02o_fISjz9r-hix5SQNuaFgwRp1SGUcukjlI_AHbMCR8_gyQqCo2wMhaIRRv8DDU1AlBwqX132OBG04-lu4vxtNl2TFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQifm7fd3xXc8ERaateH4bg6DQoufoNaatAgvkhYinCs29_0II4FLI3rp4EVGd2Zc8xoSysW89QZ7j6JrfbqufkGpkrqtjkTIzfRO_WGpp4kKk5Fh3ohH3y033tW5yfR7fvrlqigHDS7KmYa8gD-hir4-eP1Xpsm6PRqGm_0qVnrBdzKV4pdoYjty0zuCRBNmiqdvAKn8WWNT1P4wa0_msV8e5_r80qMWqiikdxlhkoXg8oN3NoebXMk4sNMSDb7WMxxKAqGP3mtSxIcLWhB3ltafwjMLQgrRhWyaqaXXyDjLJAF-pktV0KOUibrXoxQzxuuYjaipkP3wl5RNWFGvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7y_dVwgnnCrR3ukE40CzE9wVzGuQphYjblBpglnjfrz7W4sbOZOW9d1XqBr55ey454bEe1k6wGZ0XOtvRuRfMhwLge3KXaPwMxO5eBXiNzwjl79_SCmtpZyhjArAYk1ltZO8omFyqYo0lsi61Cm3DQkOd1c9-0cXuOHk2GIKqiSYZXT353ouPV90cIQ4s6QPdyQay0sSuBXZM3p-ek4FYMR9HOKuGGdnnTI-UJkVVC16IjlqfG_9ejg-Pk-bPTVrqItRU_kwKhXml6CZc_sN0mZUkuLCBgLyZTf0MIvYtSIitJRcP_u7jBZ7wUwQ_zQl7sKzy9SvZdgCUOkHifmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWoXIClakIaZ8KTonmLSKnMV32kRnBzM5lnBlCItGWJymue8YrxCb8N2zazJkKXUfBuYgXT2DFjAFMHh6z2AuddfUcs8hdbWxFK_tumuniYL02Fz_AFgGjvNzj3S5vM3RNOK2d8lO7w2nKl6cbDlVSqAhyaiXyxKDdBUPoHg7L1RxrMwL0nqRC1wgdT2ylimL9I5D2YnBsjLYUEX9zygiSLXEqrokkyTwytawHwG4YMjkHqKM4amXjgARVNdVtKLdwu9xxRGzaUnF9lUa609UUjxg6TFBJh0mWr6r_vb0-1hoA9hn3C9O1zqYwAYrlDzrQ9fR0Hl00eBMFm3qXK_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSNXFDdXyW-nk43_N--4EaUGdzdmTVf1negT9SfJy9LSfDCj2eNEe-pm-1j6C_2wQNXMKVrsJ0Pr3AZ8vePz3WmueliNFLxiAq_mDPpnLsE1ssDc9QZBssBUbbnQDG9d1ymSVBLzmX7ccqBekkec0EsC9l8GlLeUIbIlgGwrjqCYxKU52DcwrW9q4ZddIYgRCAYc9N2rIS96qYh92X3FJcI_s-yaxmnj1bjk1s1QEQn3XhYGr_IPbea0Y-J5wF84VoHJTOuKWBQ8Zej3qbCf9EGE1JS6dQtAiHMNBEIZSk81a8FVl7LiJSFNSkSf6Bo4P8yKcUUaGJjXPCVkY9YJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOkDqXon-tc-q3302BC2uh_ZAxhg1EeJpManRSEsQUr2stvRTdibQz2EQ-thfOg4bFeZaVEH7nrxyuPYbbDESKIYm2ZcC-UJ6PcvMFUHX8YDiI8r1UeWNM4I4XnXBR3mD5ayz0fmI6u7UUo2YItP5lboXxXIjuyai9BC7OWsnBROmS3aiQvThm46Hb-lPzCqo1QCoMVqQgh5H5VE4zgyTqYAol58UvMl2Lavszk1D7KDo7r7rpPcCpdpTWzBx-dtigbKU3utbJTr0CSdH2Ix2w-P6BPcN3y80VmD1yIe3mJfngY_ObogvUShJprlBjU4rGOs98BYkajAabnZ-6zhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDAO78w1t22QCHTGzsZGP4WEeG4IqcS0LEcXXctM6qcm42aLeZLi_mi1gZkhhhpHly9imjxXwlplNu7oyP2VMnqHBOrDR-HbG5R9isSAS2bDtuBPCSDlaKKsRoQVOGn_PZ5ZWkKtISjpIV9WBvBK3ztitfqrZXgsb9CHn5JFspuZQOa4bcTUMmBpVsFGHdUMoonFfIi2SDMviwfpE9dC25jHuLtblERDtFAmUu7CuvJBFsSNmRVSeOXgFjduNuhqgzzHlThbVMxgNvcZedkh_H-s_88rImsD8jWhBtdEZ7nsWB3oEOBCK3FRRy7DufqifTvoB0A-vQCl1QiGELaPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxJC5rIwGoUpTH7xRwbbz_9YS6551_Qih9IQUMMGwAlNWNDbIRfOk36F_kNl-r1OPwxGfKxKwjVFSNSHC3iW2xdKeY-LNtsP74GMhrBSQMCW2_GqscRljWv9xSPRY-DQkPQSUfLF1Pbo83rb51W09mLI64ziS_Y-mSCZewAGZCOhuTCGXybYkArNnGPdOAWsYnpxBzJnYD2caq5-gVGxe59zhQ1a4WpvJikvX0gHXf-kSnFf8H5mq6WGTNddiSY9qBLtXrPuTLUwaHUBocwrGQh0IBq4F0ZK2sk-UHNI0CvFhCw6Go_s81bJkfnu_T6reB5EJCp8iBTgmHisOFQ4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=aX7eAPvrsLYRKikkcFY_tNXJExUmvwNA_VaUoqs8oaWkyBBJZMYuSOTr7H43YtSWBHBdzVat5Ns7dXJDHY_MY-Ge1uNectBgGy3HdP4vcf9eTon2uGHgJgRQfwm3CGMrKGs8zIviZlSjZouVi88H_VXw9xmxtoGG5sHxXyMQq2ywjVVZ_CR8hj0t5HLj8t_MBRoPRdwpjd9Drzg1hZbNFPEmYmRgDkKccpkHhg-_1IdCfihB3FuQ4SIiSNX7ce43pMuXeUyqqfaprJTKRSctvoUI6_uZBB_zj7c-x6Ruv5ohthwcCyGcBra6rXsAbR66vM98El42xLpUHembYDiITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=aX7eAPvrsLYRKikkcFY_tNXJExUmvwNA_VaUoqs8oaWkyBBJZMYuSOTr7H43YtSWBHBdzVat5Ns7dXJDHY_MY-Ge1uNectBgGy3HdP4vcf9eTon2uGHgJgRQfwm3CGMrKGs8zIviZlSjZouVi88H_VXw9xmxtoGG5sHxXyMQq2ywjVVZ_CR8hj0t5HLj8t_MBRoPRdwpjd9Drzg1hZbNFPEmYmRgDkKccpkHhg-_1IdCfihB3FuQ4SIiSNX7ce43pMuXeUyqqfaprJTKRSctvoUI6_uZBB_zj7c-x6Ruv5ohthwcCyGcBra6rXsAbR66vM98El42xLpUHembYDiITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXmA14-2aITuLFwQ9ZP74tX3O2hGSEMLVxaOeHOySgAoAgSwl-EjFQW9okSDc4PIiy3_YKYMBcd8jRp8nJ5m6KUMgbCAchyamsH6vdEBHnpX_rW2_5VsJIWkcoN2EjowFIWmR7WpW2kfyUnB1W12tX-tSDxz3J3AX6XN7uOtZJBM5aZX8ijrpbmkoIxAjD7qZN03REx7rrvifggwwbhLvTA_j0mKeXIIS0PHQqceDAmUsK6eMbO306djtFpFhBZOnTy7IbWccz6oVCTG7GXivBRohIXkX3z_6F_-x6bfR38lc-WnBg08_1rZawxCk1sO_i1iB-YQ9f3trAlrTSoRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=iknlnxuYHw-4zZ-CvGN0PSlH8kFRwbEpNZeIgZuMc0OdKNjO_c_8_UlL13B_ysZopA69DNeL4aclTNi3PAosmKxz8cRx3SUheOcNgD1DKfdJuDEAQf3wqVQRHnew54FceIniw0yfvWOP_-qaWzlsXh5LmED-JNBMiDhCDoUFjic1U2zSk6sEHFS9QRhlmcxbEVqnaXZhV0zIDquKkoSF4ushhvOje51teQLRh5EneWlMVsZ-ZN6WuwWIHKgxjzVxxu3x0ukdL1mOQi-fxCaGxWL8fYow26kC4KaJz_QhziGL1yj6VklkIQKjpkz98u37A1XUmrHF2b3ZY_3fNSIM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=MH3WFk2kRzD4GBihJifhn0z20dhIPmEDVDNCKTM2D2sR1O-o99Q8v2HAtBZQE7Pl2hdAp42Zb5duUHajwNrXWicpIjrMwnXs-h52Hd4Z6vlRKiZ_zdbS9r6JTnx-RTh-vk2jEZ8SNqHtL2vBaDwHnhwAt3MvzirB83itQK-eepWHkl-bJfTuCOwCaPB2cMFtfDjYT3dm4RhRU96nDKfVhLeG1j1VX3qflS60RkoNXBt5Qd9eS1ffu-SXzv_FA0c7lU2EOSXHht4B_IIVkapWeYnpaqJhGeYNknDP9ORvrLnPKDmTvJBP5Ekm-Ch-zyAxQyCDQP4_VrZFUoZNe0Cljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=MH3WFk2kRzD4GBihJifhn0z20dhIPmEDVDNCKTM2D2sR1O-o99Q8v2HAtBZQE7Pl2hdAp42Zb5duUHajwNrXWicpIjrMwnXs-h52Hd4Z6vlRKiZ_zdbS9r6JTnx-RTh-vk2jEZ8SNqHtL2vBaDwHnhwAt3MvzirB83itQK-eepWHkl-bJfTuCOwCaPB2cMFtfDjYT3dm4RhRU96nDKfVhLeG1j1VX3qflS60RkoNXBt5Qd9eS1ffu-SXzv_FA0c7lU2EOSXHht4B_IIVkapWeYnpaqJhGeYNknDP9ORvrLnPKDmTvJBP5Ekm-Ch-zyAxQyCDQP4_VrZFUoZNe0Cljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU1QYxvhxLiwUWJzbAv2w3Y9eN-q1ESwIjg2IDkqQoN-yEzpryryW5CfmL_YsHG7OgKQaagrGBbsXunJIkxGveMkv2jaee3eqy4cPbELdPUrGb7B5F8StfXtxkXID58LjGJaBD7JGBdDq1hgs0maqXVz-5LgIllYIDW-Et6AgVI3YShKoryrZVg6ScWbeZfr5YjMBkcKoMpAbWgzJS4axi0wc0MbEsIvdRVoI-OWdVn10y2eGrEB4yn8S7hLffMWisJGVZfcHWWbur6K2k5m9z3uE1noV8aJA5qJo6VXwFeg8T62SXBBX57ZopPZ20NQZFGdWCrXL6eznKfvreWWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=dNOzVkgwawI1FMt6BfhJMTatTAy14-H8Nt8jOxjWZb3Qtf6lJz1VbTzXcKFZJadJpD14-8Bk6WtDHbc0pSnOvU1suxBRbOBbcxMl-AfGHvqZsI6OaA3yr3-qyL1Y697LeSSsWJCtDZ7lfYGmxuT-BPv-hmceI2xxq_9QEEJz_3u_inf0_Q4kJygqHVcyekNLnWB9Hk4JZIM1dTc1276JpdxpMk_HIY8DwhnHDd1wQUK-fddXhMtw5YenOPwgddqdjxLH_nQjA3a-_GBpVL_ISYh3dTp4OJG3DuI2ZNB4ht76Q4zFP_0esaNgOOfriv7joww7hr71nLCQcDtx7yd9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=dNOzVkgwawI1FMt6BfhJMTatTAy14-H8Nt8jOxjWZb3Qtf6lJz1VbTzXcKFZJadJpD14-8Bk6WtDHbc0pSnOvU1suxBRbOBbcxMl-AfGHvqZsI6OaA3yr3-qyL1Y697LeSSsWJCtDZ7lfYGmxuT-BPv-hmceI2xxq_9QEEJz_3u_inf0_Q4kJygqHVcyekNLnWB9Hk4JZIM1dTc1276JpdxpMk_HIY8DwhnHDd1wQUK-fddXhMtw5YenOPwgddqdjxLH_nQjA3a-_GBpVL_ISYh3dTp4OJG3DuI2ZNB4ht76Q4zFP_0esaNgOOfriv7joww7hr71nLCQcDtx7yd9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=kPez6GtkWRUE1rVMZ5WxTldjKFQ-CciIBWoek4TgmUrd23R6bq-l1YP0F7O-uQnNA2AwQc4EtdJehch6BHCrAQbOiTRrEvaQSRjHTO0RvYMXasNkJLyux5O_4RLRT5sDVAlBjMdpSLTxigbVoeAGtHe88cB22JJXrlmAvXC3lJf2oSf5jx0oXP-26IqNx3Ryv9jI3hNZWg5vxoh6VBJXX34c6HJuHZRSWSMsT0aHPqtHsDD8ZIPT_BrZXkal41hy6queLVNyFmWN0qxnU6CLQmU4FQYpBLWg6bxKATU_rhZR7v3qUGLIoyuQ3fcgDTDE3e7Hy1a5fOe2wxAgV2bgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=kPez6GtkWRUE1rVMZ5WxTldjKFQ-CciIBWoek4TgmUrd23R6bq-l1YP0F7O-uQnNA2AwQc4EtdJehch6BHCrAQbOiTRrEvaQSRjHTO0RvYMXasNkJLyux5O_4RLRT5sDVAlBjMdpSLTxigbVoeAGtHe88cB22JJXrlmAvXC3lJf2oSf5jx0oXP-26IqNx3Ryv9jI3hNZWg5vxoh6VBJXX34c6HJuHZRSWSMsT0aHPqtHsDD8ZIPT_BrZXkal41hy6queLVNyFmWN0qxnU6CLQmU4FQYpBLWg6bxKATU_rhZR7v3qUGLIoyuQ3fcgDTDE3e7Hy1a5fOe2wxAgV2bgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMAI3wj8UCvPGp74KPISoL73TkmcDx9Pkk-xz6u7gZeElSsdvNsep3P4CRB2hLBeHefMnBqUZc2pFoj9bJCh5zljnrO3KR6Njjml030rxQYLeEQZHfOyTAS4dDkwgRug0esajyz_KkmizhVVtnC1aO7ye9YrnCSv8sKIhLKJq5uZFiqUWTPlncFtbBX3Usf22eSH2ZM3HeSd4gGrgUiRYaGooodJiRxFV8OCDZ5QeRY3cqlc7LTbnTJ7eX6If_1HEwDenwRSQpATBjQ1YVDNtkwWfBWqK6f2i5HfgCqXY8LegWbJQqDm3C4wmx1fLwQ6gR-IcnRJbjZ5dSFITts9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbsixCzAuVUGNPnRuduR83T3Dkbb7_PluEq_fKmz_iIuRPB7H-E9QQtdt6UKPGE1hr8NG7p3qJG6LiK0ayvL365XaR7-d-gEDEAEPx3iqaE7grzG__P1205mH-1UCNa_lDEByaOk5K2S08p76jd85OANE6g0Cg7hWo6hIYYL9GVzBYS9akBCLKvCXzDhjeisRxXv-ggvpQQoMhFV2KDFdVsgok4RJyUVYjvALYY_QKUlaxLRHYQVVkkvr7tqJcgO1mWc8i8bQXAyh5jSqbaT1QVRZrRzFScfO9T0LqeHDdHTgMhPh-ImaF0L0wwhJko2QRaGkS9gbhtiFXZMPp1UXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=dEm1TI-JzyUHwwjzoZX6WuS4Zs8XWEMZhCsm89fgYgKtwOnwF6HDytG36o1vflyxOK0ez0ln3QwsxDSz5-6L2URhnS4gjPdT-EWomUTsmOPWEuw6z8gX-FRcRLe9ViSlrEQKkJ1o_lwZbUiEFXdAzaHLb2y3XH3almeOJa3H84M7gIoJRcV7K3e_h0MAeblPwFyHbAqmAbKeBFUN5PfJZQXjDyLFwyvfzaBPfM74rF_drU0wPFyECYa8XFi5ENlLKPZBtie662hiJ8t7npopgiGugBotrGSGiPg7gdPKqqpXzmtju1e6_AqHe3UroR_DcwxojdR7njGTHLx27dGVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWKPXk135aYjyXfB1tTHbVMdFXBYuqH-WlC3ICVNs_QrrWQpB70475Pdvqh8s9AC598IUus1w6xfHOsCC6ErQcVvx06mzl8s0l8zX0QgQqKdHsOUPFcs9k_pceAIJTGQOWlk8_7yj_DwR40CsjSouzuRqM360cajMDOT-5TKwd_30upelyMeldZ5LzE8t3cTIj8iw0Gkv_bDJaZk4qQ3Vbq51MC0NlmkvYTfPI_lJLFOp7BFNENEt8DF8Y6WhJaiCfvLcWIebyIO1Rzu6NWUCHh4AZbxSSmK3FjD0kpHOvUmqmUXQ5XoCKreSxhIm3ly-PKSy763Bs8jqGE6jM5x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwXABZk9838sHIj5TvZ-kWS_qFCZwZ4npQqAKyHTOVOeH8nI9PLHpW3_Tx1SrMrbk2iYwqDmMwKwAtxt6NFWS-BR030ibJ_KBPUsMpO4hZ5Am2s5Kx9vQsAAL-nMCHAdjAEvvkqDmzRabvgsHbc3zK9LYhAvcaPeGEvoXrLnTDEKjClRlM8JTv5NgkF2i9WTleOgFgaQvgtsyGJYxZspKAtx9N_AhLWh6OkzUFWzu4PXAlAk9JhphxrUqNj5tVyrRyWnhScux73SVe5jV27MiFcQToUPHQddRW77FEnX-w9uohW-9wla61R5noBl8hQT7C8eH-RdWQFBus_YOGCpUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfmN4p5RcJWrlb6yRCN2eCSwIIsTiR3RRfUPEIoxJvDkhJSYuFr1yWrV2IyNlvNb0PDnPDh70-4A0dtH2QfxKGVoyv3bhmygCoC6eXNPEJ0JnWUWZ6piLfhAD0yzgBryYkfFKEbb14GEvHacEihc84DNCKy_aumaZPLAMqyl1QXy7N7x_aUL42aLfyrat7Ju3mYgLsko9Xlx58441a-73bwghpTpTkjZdvqJg_1EvNDvwPuv1JAArGRDA-I50fIG_ZLieuK-wQZcAm1hXVRGMZ6HuQhEXfadWCNXQDvBc6QX4oV1CN3jFsBJdt5gYlelrJBnTWp-Z0MSle30pxXbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WV27er0AKyDozQamb2YWCzV8FVzho7L7en8GRUA7X6YQVwAfP0Ju_wRXorJAbxMqCc7xsPaENcTEmdrS-wPrCzadWEc2RUBg1IFReVqa-ToEAt9EflJknvjLekBELcFlhxkSAsVUlTcqvcAUnVUrf3iTirbDrUt4ab3b1NqgmpaHMrMK6rD4a7ngExniaiOGSr6kGIDQTWoOT-dFA0SitBGSIxHzaGUwZZAhKU-r0R35o2HV5My8yELKAxCZ-h3UAY8aU50HzqkJx0mRjh9lKYm9RQWN1pzvPZtFB7pEWsmt6MXPNPvAzHhNIlbUPZSgfW4cV0qqLoD5of0-z2KPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLfnLDW-TJouDnCnTbFjxQjWJHX9oKeFGzI3_397p7yepNvgyGdfYwKgIrvhxgAyHL7ebOb-n1htrAEj69s2ZEz_A7DIDHlvk1ymllq2W-OUIytyxtN7giYuibvilTHx8Gw89w4bf9d7ITBwFYJVED75McF-C1g6MOl2Uxi9F_HrIhzlYv7W9x8AzH9QjX68ovSTbs9n3wxwoPnVYQap1hI0h44BMSJJQLRh3jklzQej5tGjH3acNyFfbNc3BfgoG5RpxCebK6EDZvlyx77dNKVeheJ7q8CCJ7fR4Yk8zxeHkd83GKDrrQIeC9RmzZj_525UqqRBtT7w6Whjegccpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccNbacPqeIHhrOJQRjLgUGxS1yk2OAvSuhkcA4MuG_SH7DXHiw4RakOWTKMVPOoAJYKJoHO5ye-lBtoNbzhNtG0wLeswXt9aRCmlO4jWvmcQsUsU9S81yVQOAX_A2u1aAMdDvcdTgIA6ui1qF4LTjSsty3AUXEIFIHjh4HBT5q4ZNNxaOYNDQOE2q7A6Ejwl7KiwEhadPLPcIJX-U7jzEgfXLISwNgRvAtSOOeSLWh78xnPJt6MuxrSJS-IPthY9GzDy6ezp9_aIYTx4VKwdxDRT7i6KFZBZedUFM_Nq2qUhrLJGWdwu73jIuNTBjvKP7tNqUniE8ojjOFlrmJb8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Enq0yfNeQen5qlxlsN_XK0SHSt4OHj4d2PETj5pINiWoZqAoKrrOaTOUAH5Rs8oz88SoZSchU2OofCwR1F7uN_at3-SK39w1x_gLzI0Wtc-zIRJQ-FdUjrrpqolik7mxeWL9F1RkqKecWkz4AIJhcx8gQ05Jyiu-t3rNhywvXGoy9dAIdrxlm-ZbhsggUWH66jRgvSHpEgNA9CNvS6ntVuOseQIuwnhwxkJfba0-CjklXoD0lliwuKjkQwQ4IUyIxgKKZToPAAP6WtRT5ursPCsLg3rCzQNRYn7vmfvNnCDuUbs6dbuxiHkGS20k_9eLJX6kqo5j_G-U8TCtps7xDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViLfJySsw2nxBCR4KXNaOUZ-RWZBVtjOEECjAZ752uoxd3CgryooJpwE5HH7ilk4zfSBF2KYyZhh8i3NBCruM71FG9Dii04sc3paH8j26Xq0Wgx6zCQSl2r3cjjHVXY5xVfcqMkbgQP8z-KVVeoHT0lHl0hbTuta8fuRbhN5sreCopxJ1yl35Q-q657EK6BKiNglvLL8EXQ2lVHAw2FeJRqcx22gMJ0qsLP-G4tvnSAdT-kh8_2zVE-7G3JFCIb8SwJYYGKj90sgOklMXnoeFuASIXLQZbCTJo-EchOgyTrEKB8uM-oDEPK-yWRpQYBmFPNZQG_2SQpDrm1Xil1bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMDHZG92Xyg8yWcdv8igWj5M0yhbclVdXGGlRIkDF0qmirS3WRiHsIKk5LK6Fcs4DwMhUVazT1EaTIRyd3e07xLylQa8WHsr2vV9KAhqgSPp06g89enlkN4Tm4w35rxkUJeCyQOh43s2E_-5cZyONPqSLRwGQ_cFM3a0b51qjiECohfTvDZ1no-XmSwV2-a0V5jnCh53ETXMzJ9LMOAcEPRqizJ0NR_fiyVU5r5zQC5nlm1in1iwnP99Z0nvm4x5O_CgONllzsZGX2xmak0oAxlIlSe9MPtDp8pvxv9g2M8EJBDmqmbMakdnB_XCOvjNgwBNp719PoW3oQpflvNSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqDwafd-C_zqBjr1-VdAxBOaBnieI_Sth7hrGEVp2bOMk_BB2oH4ecU7gyuRg2LXaLjcYbQx7UHx38c1oxeO8GM0XgKtpM53aLwvWrwntsau1HfxWjHQXg2UqNN37XPyD-Ch_3DscJ7dk4sVHfn-QGyqpzNWaBkvo0pcBrl4-s-Zxt-MjL8nyNrfD5w6JQ0pST1JZ6xqbtmHZO1bgaoRiWLFU_lfC5RcawnmmCuGoFKQYvrvJMfzgefP7KwpJhZopl0m68pcBETRqzKfSfOZoWi-Lu6wHzLkNG1cKXCkXJDP0LNavDwZdr1ehTK-2sLiF7dEdDf4x3JZp_YEUU9veg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khh9MYLerchpTqLSviFyB9F_CPE3PB1rTJbB4A1Ni9s4sIJLP7Z5EHO3KcjenYbUF1tR_FP0GAJtxjN33WCjFjS5QbQWf1Wi9diTUWT4-JRb9xSV5ihv5QXMyyVJ6f16stb_EIkdLAj7WtcP9NAIQ7WdjG_fU5yHGGOSTNM3Vn_I-7vrwpUUHQspjgKTh1pT41kU1-gy_cdHtpTlNIjKgZvZPRVnv8MoAuuAFTWtZYtY1quoczVl9MD6UDBAIwfHAvr6sYrx89Ewm98zcbg9JCUAq8WUL3pVlGQtL3ay628xSytEA8waam1meRU_shjQSS1F_NfwX2Dq8FzQE6MOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwhzJ2oli8W6H6pa1KqezdUJfyPbr_AoRnnshyfPmNpmJmYHB6gFQS2cHHxsOpns31WoMFEDU2JVBo4W93cH7odOTNLd0FUzA1Yit0PmtBQGtbb5s4OwtFrboFSxVZN2mRQ2CiTePMIzy79rXU7FoBiBvKKFRt7L0SIwstmphqlzFRi2O69PfTvADzqfaaljLdXMP21T7vSQzOpdTM-b9YKyNRhNE7AmfBNdNH4xFQuUEfYvlvpCauCs8onhLndhonL0oWIMjHxKye4pPzgZLKHNRhXEUyxPc_yk-nEx_zCgA9F6p3HVY0OLOiFQO70lOD-iAQRC6iTiHPXF2_SB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNQZb1BLfqigRcjIETje7PLZltYfG9SibLymjhhUOqKG0pCO78i9OQEH1rj3dC7_5OzohXuhK0nGYvZ3exM9GURp4fyL-TkPeh1JTl-5-ppItYWKFUjnrzLp5_1LYpbozNgIu3a5aA4OIAFL1VRdLsehIWgymRZSABMWrEBMAei2WUnD-ILSR4DSjAMvfr3MW15xc5NwgTOPILqWwQcpQj72_0-NERJA74qZQ3Uf1BnLlgHOK6LAKbF939FdmwovaLjguKbIWob3vVpw-A3FAxSPIW11Wfh6tBRIOYPawk6L3C8JqeyslIuwep0kMPE1aoY2Do9SB_reMPR5M57pxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6UiZP7xeI5uDDiOtbU8602jTXABoQSD8VGp82kS38ePbTWnAuVgpfSLbv8PPzbap5_ZeI9qeDDu4g_HT4IoXb_oqHYZObNSM6Xa3mlTp_06_xCVNqpsqtKsSfMaTypagEWRLjZaxR-yucXLl8GgVavQr-6KNgMvP55hexiYyQYkir0Hp51qCTr6RJ2YPsy_PBlG1acNryvOKsdxr-mtOoFVUFb_YZpPx8kxmygmx5CB3IPqUR1I_kZpBBRr8CvxamjtmFrTGIpQ6UK2pctKpLG_AFjy6NlKbe3Egi2zHFwRh9reYWKnBWJ_jNPI4L3JJ1VK1nbrGsLLFPkXSVeSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCuV9A4FvMq71FsD6NYNVDzNaxOqFW6S45A3wQSfR9bFXTD7lCUsF3wnz1caGaOOzmUWlVu-cyTxKe0C-DcWMlgBAf5I2z16L--c10bD0fC5EChTbfCP2yO9p2l93UDuKWBRgmR74nsdFdgCnm9Nn-vi0LK0wM4cdocXHQNaD3U9iuetCJKMJlN-pqy-yDRWAujeTSHRf7-Vqovg4RbElTWt0OhfVUkjbWd_W-rBualYsv--Rvebg7Ob-Iu9uJlxqEvP1Q_KA-EqjwHp5UX3chhudZLDJ9JUeiX4CK4MJAS0RmxsApbH_t9Tx4Gug7RM1TsXgmuljDMgXj75Jejr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-R3L_Ah7wop2ouFj9unQ7uDM1LOcbQfV_M8iKOSQvTd6YUZV4C42OzZjYZxIvpwKkDI73t5Bv0EWGdvAiaU92e2nISmwW6kbCgABOQF9hdf8NdmmBO7HPi_ivOs_zAtVy-pBP6LVtZC55AKU3LvrRrf6e-bHokkeIygQNMiD9VINkil9Mom4TuLdqMuQ6dkKag2t3caUe7pL4ap0TXfkVe6Fd6d3nTsZ1ea-DS6xb3PTU4EQsW_epzHN59HcCvBVN4CJX0EW_CDH5Ua2lDOtR9oxDLiYx3z8icxGG4U6Ljp3YrMIyEu_-AbvzkCAHvKILCpAqNMYj8bBmUeavdPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=L-yjl9NuZfjL9h5iYiZ2a3yIDHqLJt65Ix1hBIiMldDkNYv-tl7jlSW88Ni-GkPJnW8rFisCawEtnedt7qTZYbX3Vlz4rI7Xij4z4mlrH2JoFHWlRrNHmvtnW6gJyPxxhg8HSNUTtLwqgOpIUzfo7OJSeSomhsnAPUjYuZzUAFfDnphWBuFo9rmukJcfELvJ0ZALB3Omso5ZTPPByoYJOcZFcyp95LW-28PVwZbxz7WbhL6gwupqByvOQecMEJD91fp0F9CgaA9zf9oXSHAH1lh9UmBGIviAZgD4jsGSpl_eezvKDSh-kT2r0oTrKDW3fk64Z8rDDDwj3LjxJxiIIKBU94GJsQhi0AzVb2Bk2PEo730leRAWKPR-tt-EwGxXZKuXWGj-kV9vjVSi3XKfOiMcpjNdGzBCI2Bkzvp_xrsJkLXgzBDlPV2YN-9TdjkkTw7k_o0ewbahrXzK4UN-34Bw_r0bEvgu4Vib9aRtIpFQZt4AEr_lqA7DtP6mGgy4jTXus7vUkAfbWscnwCkYVUfaMJTR72pCTwaAHqGkMvyMleXB8XxUxcVAfXyJ2cMNdQrNFhCV9ZIoZNMsvaDkAEKp_VPb_PCntGH9BPSnwDYPD5csQ3mxD1lyRc7VSBX4ZXDWnb7ijFjsZrVhGJk93bhImpNasJrgceGY8XknN14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=L-yjl9NuZfjL9h5iYiZ2a3yIDHqLJt65Ix1hBIiMldDkNYv-tl7jlSW88Ni-GkPJnW8rFisCawEtnedt7qTZYbX3Vlz4rI7Xij4z4mlrH2JoFHWlRrNHmvtnW6gJyPxxhg8HSNUTtLwqgOpIUzfo7OJSeSomhsnAPUjYuZzUAFfDnphWBuFo9rmukJcfELvJ0ZALB3Omso5ZTPPByoYJOcZFcyp95LW-28PVwZbxz7WbhL6gwupqByvOQecMEJD91fp0F9CgaA9zf9oXSHAH1lh9UmBGIviAZgD4jsGSpl_eezvKDSh-kT2r0oTrKDW3fk64Z8rDDDwj3LjxJxiIIKBU94GJsQhi0AzVb2Bk2PEo730leRAWKPR-tt-EwGxXZKuXWGj-kV9vjVSi3XKfOiMcpjNdGzBCI2Bkzvp_xrsJkLXgzBDlPV2YN-9TdjkkTw7k_o0ewbahrXzK4UN-34Bw_r0bEvgu4Vib9aRtIpFQZt4AEr_lqA7DtP6mGgy4jTXus7vUkAfbWscnwCkYVUfaMJTR72pCTwaAHqGkMvyMleXB8XxUxcVAfXyJ2cMNdQrNFhCV9ZIoZNMsvaDkAEKp_VPb_PCntGH9BPSnwDYPD5csQ3mxD1lyRc7VSBX4ZXDWnb7ijFjsZrVhGJk93bhImpNasJrgceGY8XknN14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUGJnyiA5dekeRwoJqhVw6Qa1RMfbmbIuAuc8boiZFEPUjFwGwTsqDBHOdQegzaPY8HGgw8qnmEApTTbBLmP9jVcqa7bu9_D9ndrKQVgsqjm68tODsk8WAmepgK41dLn528B4RhjJzIov8HdwUYKw2mWqedgzk8xHl-Zruhmh-PG9-e7M7rGCwJ3kIFJTEZwheYdTA_lXAwmG2EV0SYuShGnQzF1bO6r3ZkMLeP8cY0SmZUnB3qjeUJYh3P0jusCNs7_z7YXOlz3iCn1SkqjnjZJLktA6lX2OGWYCBdTAn36v7qyc42wtEnnbEh8w3KyKz_ERiXwVVaf70LC2gaExdzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqUGJnyiA5dekeRwoJqhVw6Qa1RMfbmbIuAuc8boiZFEPUjFwGwTsqDBHOdQegzaPY8HGgw8qnmEApTTbBLmP9jVcqa7bu9_D9ndrKQVgsqjm68tODsk8WAmepgK41dLn528B4RhjJzIov8HdwUYKw2mWqedgzk8xHl-Zruhmh-PG9-e7M7rGCwJ3kIFJTEZwheYdTA_lXAwmG2EV0SYuShGnQzF1bO6r3ZkMLeP8cY0SmZUnB3qjeUJYh3P0jusCNs7_z7YXOlz3iCn1SkqjnjZJLktA6lX2OGWYCBdTAn36v7qyc42wtEnnbEh8w3KyKz_ERiXwVVaf70LC2gaExdzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
