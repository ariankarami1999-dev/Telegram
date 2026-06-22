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
<img src="https://cdn4.telesco.pe/file/qHrhrOlJW0Ab8yBq6dj5CaDMG2WCOrGwMTsCnStIBblnmtpFKlb4tVx5X_UREvm12D95-Qm2Zhr6H_m8XqUi94mW8ffk3ux6fBYWFgISoqq8P01jvOA2zfGfXdTAedF05Yqz6H8vG9fHwlynwFQStGRNGEOwLgyP23uJguvMsCMFjWwqPpXcuGPx4dpaYuFgYcpukv6KBTddlkcFgjnic-GMoes9Q-RQK0FwmYlOUruous5t88J_qQ7r6t5GGunADraZm3m0rFtI31fdTDRAwPB2ABtA7LACC_OPcc-S_fRDESWeQJcMDjZ6jRoI7q_8hQ3ALopkwCMfN6cwqP0u8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 220K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-66697">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z7qKWIcEkUBmMXMKJx3UK2aCFnvu9hvPL6I3lTVbw_KRwA_-t1BfoR6KF6PWllDJkwlXWy7WIxbwQ733e6QawxKAmvM1qMsIuvqk4ns68TimXaamLoOI6wwgBRa07R4k89cQeISs4-YM7yhoMDzrb9XUP09nN5RJhEmNJ-M_ZCjbHlDkZP5RjrBtPrJGF3UEip51ISbLDze2dB8cH58eyUgS1AYCceVJRC8NI58yoJ2gUMcUW1yFGAcSeAckHp6jGFyKyXmzLxV_KgBwlThLeKF5fZuNVqlbQ8JqseCOCxvfcC07bQrL-LqXz5UxewUtoEvEv1hU142AILI52SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
همه کاملاً آگاه هستند که ایران با بازرسی‌های عمده تسلیحاتی موافقت خواهد کرد تا «صداقت هسته‌ای» در آینده طولانی تضمین شود. رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/66697" target="_blank">📅 20:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66696">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA6jrcoWfgfd8qtqEp8Xyv1bE21ouQg_m5nBzGjCDTdcx-SFMvqdiDvJ4uy7erpF3So5-zjOIKa08uM_BDEIvCndNDY7Vwy8Va72-x-cUENfJTU9XlJ7RzRKH3i7Oxsl3rGzyAKsfGUU_p3z5FtAQDU2KwDAoTPkiMyN8GTmvIc5JeMuW6_R7k_HnS2-E76XIPArBkNHbKiS8JmaVkUWZGEmiJoJdbdWJEpuZCS0tCjX0NC0mFlC3qmLslfqdXBriPQfwsx3THG65EVDbHLZGxNqpuuZwl4n5ViQBp5XAJqkE7rE_P4k_wJ5a7Z7ujCKVGWJqwIPegyKp8O8yIV8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏رجا نیوز:
در حالی که جریان رسانه‌ای حامی تفاهم‌نامه اسلام‌آباد تلاش می‌کند آن را یک دستاورد تاریخی معرفی کند، اظهارات «جی‌دی ونس»، پرده از ابعاد فاجعه‌بار و تحقیرآمیز این سند بر‌می‌دارد.
سخنان ونس نشان می‌دهد آنچه به نام «آزادسازی دارایی‌ها» به ملت ایران وعده داده شده، در عمل یک سازوکار استعماری و نسخه به‌روزشده همان طرح «نفت در برابر غذا» است که این بار قرار است عزت ملی را به گروگان بگیرد.
ونس با بی‌شرمی تمام، مکانیزم طراحی‌شده را اینگونه تشریح می‌کند: «اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند... سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.» او با وقاحت می‌گوید با این پول قرار است جیب کشاورزان آمریکایی پر شود.
مشخص نیست این توافق چه نسبتی با پیروزی‌های خیره‌کننده ایران اسلامی در میدان نبرد دارد؟ آیا خون شهیدان میدان، باید پای میز مذاکره با وعده «سویای آمریکایی» معامله شود؟ آقایان مذاکره‌کننده با چه منطقی پذیرفته‌اند که حق حاکمیت ملی بر دارایی‌های خود را به «حق وتو» و «نظارت» آمریکا و واسطه‌ها واگذار کنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/news_hut/66696" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66695">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/news_hut/66695" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66694">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR1eyaN3aN6ortsUIyV6zrmNQebPn95xsQFpIzbW1H0sHRdIrPSGXl3BarTzsEGG7MbCCxc8LkQt9ERXIpRkcRqTcyNX7XJDITPmOaQlaTf_YlYOsqYDMmnESGo5c05g5FfG5ZHQO9aFBK6oCaxKcPv-5P_w2Iq1L8TSj6segIxzzNLO4AKVsehHfhi63zPaDfamyFqJCpMmSQqgxlKCbUzGDaLJIegxB7n3owEelrL-_3h6jne96jQl2kPRrG4P2mlqIoTdww7OceYM-NdnUyTsT7SwlLTW1NFK5MfKLeG6UWX18fOcXFYoUdYSrDBKJVpODzahr6wiGSRTzVLaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 7K · <a href="https://t.me/news_hut/66694" target="_blank">📅 20:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66693">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTYBJZaaKWwHHlRR1ggS9ygCVUWi98mSlYbLJK_8zaAT2vaLN-E7mYJhT54tprgZ-vlIGQikCD8wRvKp7CO3wQilMj7pDT5E9ULAZxpCW_foACcqOWpD-zET3FwdHP4R-HRDaO5mX1f1vgGXR0jaykVD2lJiOwEIVZn7YRVgGZ-v_PbUlwL1O2Szl1FEIRXBKiqGqT2FfTM1DPMdAj1iXfQPEM47wI5DuPZoRZ2Y-e6DV2oUs2eaZ-OTL3TVAXM6BV5XcDpwQNSjz7m0vvAteoRGNo-q7ORj8oBCE9rw7tNNF03o3qBcK0XHj-rOOMcZrJ53Tx9Pb1G4a8X83PvWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/news_hut/66693" target="_blank">📅 19:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66692">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f18d416253.mp4?token=dpMWSsbMDm-63AD8WP9QpzqhdSjlvUAtu8V_wkp87SEY0OAOzOwg_LNJsBjR0ZvbGBHkEmxfex74lPJYoti0qYuDtNdrsfep9aClSaFEP8TyXWCWYzRdbuuIbZ0GwUJ5bNa5om6Uc2Ik8QWh19WRL8QnkXZiRsZxZkR373W6VXtxjH0bN04R7jNdJCnMUrkrtIzhjovRnaGfbTXv3r-hFadhjo4Ltco7sP4jBuE8fWMcWXbzZAU4QSy1h1tq9Ez84bhNu6b7r0Dxwj8Zkjrupvju699R2aPDASY5Bra93pVnvEDc1tANXanGnLE4IiBuTMtutMYOQtxXaArAZuFCLIcb079eswKtesbqB2R1k_Xz1qk1yxZIzItS0WV-1HUy2yKLPiPE6RVDWUPjKfQV9j66UTKjUWo4aSiEJXv1-45daLlYiJYBwLqasysZUVAo5XEOcGLIKXfMl004KVRRfKG58GGwKtslMJbsNX-6W7vBr0TKGThJ8PgHCvkpPx7czLjGrn0sxfYjIXYy8LyDdbSZhcD94yJyKcGrathnIbFMXHlkrsbzqbRPiS9tZPu_U8FAR5D3QihMnauGeAHGWl3_AjPMUKlE9EHRvqEWHffXj9-3uekI7F4qFaRuT4XExXxknLxB2-GVEm-1FamQJLkRijBB4Uf5D51kG0F3wnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی‌جماعت حتی کف آمریکا هم باشه بازم دست از کسخل بازی برنمیداره
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/66692" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66691">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9af9079d6.mp4?token=lIwb6I9SaEDnykDgqa4njzngfgnsIyn1ooCuo9E7iUD_ZEotouJN0wv5TcYdR9izQbhf3QEpDsYrS67x3mcPmA0Etz-d890EifyTy3aHL4HvepD7XVsKjJtXiXCay4gckpBz30Wk9EUknXFspw2So1mEI4KQRYYtHSFdL2xkdPygLin6QtIehegO3--V47d8D8Cx6r_mHRuvVHEiht4tqUONRbjcnRmyE0igtYsazDtufIUBXej1q3IMopb5Ol2yHvzSNDQKzGSHkizla17vwWcAMbFgb1xG2Jf8vrdf_XA-66-4bN3G-ql7P4sK8m6A1qZnxyVzNIdJdZn9AkBhyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
یمنی‌های فلک‌زده بابت گل مردود تیم قلعه‌نویی اینجوری دیشب خوشحالی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66691" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66690">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=UD8g0fFrwBB1Qq0Di9cj4eqh2O4kzmi0ntlRIG8IiTee0vAOIEXHf88RWAp0DJEmrYDEYIpH3SjX0p7pVHD9HzdU_B2Rmsaz_WhkxaOrGtKo9CGIF1po911hsp9F13wrY2K9ABDs2ateuAh3WkJ26RJMtAS1eR2NtB-MkWdEDGB2frmXASao63SMVjcslwxsifpe9v2GlJfsWK69tMNxRNEOUj7tNWWekcuYaPSxjYacOkCWXb7Lg-ZdJ0MN9HvKtc_X9ybjJ4XFa7KuUuJsaogBOQAHL6F-3FZHMMqG4rMALvddQ03OsS6KPn9jAmFLnUc1iyd8ZGELX5KWslNEtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f4a6b399.mp4?token=UD8g0fFrwBB1Qq0Di9cj4eqh2O4kzmi0ntlRIG8IiTee0vAOIEXHf88RWAp0DJEmrYDEYIpH3SjX0p7pVHD9HzdU_B2Rmsaz_WhkxaOrGtKo9CGIF1po911hsp9F13wrY2K9ABDs2ateuAh3WkJ26RJMtAS1eR2NtB-MkWdEDGB2frmXASao63SMVjcslwxsifpe9v2GlJfsWK69tMNxRNEOUj7tNWWekcuYaPSxjYacOkCWXb7Lg-ZdJ0MN9HvKtc_X9ybjJ4XFa7KuUuJsaogBOQAHL6F-3FZHMMqG4rMALvddQ03OsS6KPn9jAmFLnUc1iyd8ZGELX5KWslNEtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
دستور من و وزیر دفاع به ارتش اسرائیل واضح است و تغییر نکرده است: رزمندگان ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم یا نوظهور علیه خود یا ساکنان شمال دارند. ارتش اسرائیل هیچ محدودیتی در این زمینه ندارد. من پشت سر آنها ایستاده‌ام، تمام ملت پشت سر آنها ایستاده است. من قاطعانه می‌گویم که تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند تا از ساکنان شمال و همه شهروندان کشور محافظت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66690" target="_blank">📅 18:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66689">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad4cb70b1.mp4?token=E6yvgStXYyOAQ6b6LEL8XAm3T_M51wL8_s3dT4GpvOy5rk7wL8OEkD-Xbjlehg_7B9qGKJv7mq8-JwzPyH6PR9rcX7FQ0_cG0wB0AGms6JVFFsgxd1e_4pRFaSCjCrHBjuS2Gj4oMOBRKupPBUU5MnJfP-6Qzts1yAjitllLGPcWvOsv1kfxIiTk915PMoS1FwdJk7Y6Cu4rCWH6Mo9F31_pmnOAILXFEvSU2krxwe3IWetzlAjd9O_2ivd1w0hbVQwOO_OQFwqFTnX4xbq3GcodFnwdZpi0xK50P9fK9U80fJOGR0bQ3K85NBHIA9ptzlFd6Kstavgxx1o5XV5u6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66689" target="_blank">📅 17:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66688">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPphgGDYYPwxvynwc1mAP-uWgqsbsDQi4dTdBhvHZiPZWuyke622u5XnUVXzCDZYmZSEJW_czeIsEPNR_Lpsmkw1l0c5P_rvwMuRxmHzh-3MYRJF3hVxGXdtofP3aJ9CMFu4cBB9kG1KE_dWVl-qOOo3zAEqU1Oai6HvAJ1mh9Cvar70baXCkHvxPKuLSZydwWdPVGCUhYOiZEVZJsecEbFv92adahyEi3SHkqvWYr4hIzG_fhTU6BQarN8aoAAzYynoDElGZe2bc_AGyxjbDUwSe84x_m7O3Nm0PULlSI7Qrom08Xj0Ncn7hV_py-iu4Ia1A6N9StvuFMuVFDiGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اسکات بسنت وزیر خزانه‌داری آمریکا:
تحت ریاست جمهوری دونالد ترامپ و معاون رئیس جمهور، ما همچنان به امن‌تر و مرفه‌تر کردن جهان ادامه می‌دهیم. در راستای مذاکرات سازنده جاری در سوئیس، ایران متعهد به ترانزیت آزاد و باز در تنگه هرمز و اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به کشورش شده است. به عنوان بخشی از این چارچوب، وزارت خزانه‌داری یک مجوز عمومی موقت ۶۰ روزه صادر کرده است که تولید، تحویل و فروش نفت ایران را مجاز می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66688" target="_blank">📅 17:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d2962b2c.mp4?token=SgssrHGb5RYz-UDGMJLywv87tvAFsXClqBujbq4O7uXNU8v9uUyoIObQxCGdTtjA9giFRhmlYOGZJaoJkx2ilJNRz8U7GbvWGuSmeJoqfk_jqF9UJukVjwh-zcuIeUgAYW1dgVuYwGLQ3VCxxRTzb3ebLz_2I6i5nM0M96y3jdSwftlu0_EwTtSB6dxSJnmNEkLmGTAEHsem25U-qHpsTkAN9-o23rCzjJ37FzLa6CFo37IDJWGiQSXqjxy_rjGdGHJlDu4XoZ03xHiy7YICBN0cNB1xydkHdXymXQdqYWVBm6iwR4JejKAqgw18ybHyXw1yLZ1Skyz_ggBP-M1mQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
استودیو آیت‌الله BBC رو مشاهده می‌کنید بعد گل دیشب طارمی به بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66687" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66686">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea331c08c.mp4?token=i6ozpXKZ-QOkNUiycIrBbrgrqiCGgxqJCu_ZfTbmDmx5qzT-4mF0JM5k_o3XdIVOMkVc9iyNJWzZOvbmrSvgEDYqw63TUgqSOMPRHLQOpGO9YolnFaQ6z2rgGiXpE0geVkuHU3SCiz8njENQr1shx43Su1WRYvc2wc6aX-ZvWAFTHM7ilwVV06LjHYCUYfanWFCulmwiMNNpMFHyE1OSEIjpaBAUte7yskYBEuw5RvDGmYGUfSxxFQ9A_CiTjqSFVVKVaegOe6OsfSVvB2vyIh81Ukmb8Gg5kXSegxwBNn-mw27mqD_nsa7yK4KeVznVaQ2RfS64CastaJQ6Vr-rDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیعت با رهبر مقوایی
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66686" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66685">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c0474e6a.mp4?token=pZM-6q_arxuUFg0D_xgs_lqWghCEzDvwZ7sWw-2xgrOrYbpWZcZiNWr39LmS5iNrASe_rcDANDz_b01raJh29PpK36odrVDdSTMaZK6iY8xVs6NMapqDjWIMJ2xFOVhnsbTo3ANFP0R-hlbOHJbQ5LcLWvLUeE7wmV58RjB8UCVf9PcSCmqFfIU-W3DogbyBa-Dd2Tz_krh8Z_sAB-BTbU-gk_rWkyHmSF_f1kpC2n_sdSUU7wTJIYAG_ZVHq8F-pFZYPLkw2ubtju8GFCGE1qNTGwTfK9fn2rgL4Y09Mb3fxKePZDm8itxfSK6C28X5N7AAWNkYVurtaL8pMiDnyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش‌چشم کارشناس خبره صداوسیما بعد اینکه عادل فردوسی‌پور بهش رید اینجوری واکنش نشون داد
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66685" target="_blank">📅 16:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66684">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a12930d87.mp4?token=bIILyTqek3zwKoD99gxy2ZFyust1ymg8C4FcFm5WkripcWxUj4jzUVzy2AKyS3IqqpFxmaUP3yqoK2WKPahBApcHtEHO-SC1c_lRAOLY79ewmrbAf4IfIWcfGmWX30VjTtuP4C_VqqQaEF7kepDg8LYFrBaz6-fkW7MuGo9IfcucJcETk9EUQrb1GF5-jHla26yUCgXGA-EC9fyyZU1xulSIvTFX8qrU1E5iMe6iw6BeKxMyPchYq04U_zZQ4_6Hqggx-i96mlC_yreumonZWuuMctOrzgACcZYUF6RDjWxW70dbNTnslWLfJD81t_ugOHG2GuRau8sGW-SrC2aBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو ورزشگاه بعد بازی دخترا اینجوری قربون صدقه بیرانوند رفتن. حیف دوربین رو صورتش بود وگرنه معلوم نیست چیکار می‌کرد بیرو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66684" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66683">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad11430f2.mp4?token=nMQjJQDOP4LPag3Dy7pC1DzlTGprUF2xtcD-V4DePNAoQaGQ-Kg9-PR4mBdw9djzFutV9V6sxc2KKXghY09MRTZBswaQE6cKB7o9U-4zxG4Exu0eXrYaQgG7y5k1Z2Z_gBRlGaU_gjMglBU94Tnejoyil-f95RBQ_enAkBWYfkruohlVtsrnO_cY6b7hzZ8Yp-J5kFaTEHIL3SVU8wYHlDkkLe-SEcCGgudrUFDhurAcDA9Ojqh0ZcfM9vn7varB2e-MxJP9M-HZX5c50jM_AqMRQIe5ZZT9haVEY7Uu93xMDcEBpXOt-WBFVgQw4wD7Bo_ZXYczC7DuL0e0uR9stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس در مورد لبنان:
گاهی اوقات یک فرد جوان پهپادی را شلیک می‌کند که از فرماندهی عالی تأیید نشده است.
البته، اسرائیل باید به آن پاسخ دهد، اما اگر اسرائیل در چارچوب گفتگویی که بین حزب الله، لبنان، اسرائیل و سایر شرکا در منطقه در جریان است، پاسخ دهد، می‌توانیم وضعیت صلح‌آمیزتری داشته باشیمما معتقدیم می توانیم به جایی برسیم که
حاکمیت لبنان و همچنین امنیت اسرائیل حفظ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66683" target="_blank">📅 15:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66681">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f7af385f.mp4?token=V-GzgJ-9LiJW95AYIuGLllI98a5tqnbj6RzigVR_yEW67s9MNQdl6cXQm1NorjAW2ClPptKW-yQL6euwyt3yg5zmEojCf0ixNmtRIm1xRCcVesjGGfEmqVt8pmf2E4VpgBAifIaa1zicSUwd0251hwmDdbP6usv4OG16NNg0S3PJpzL8_d2SgtPCp37UNd4PyHumtOkPHYP4Gl8sxKh_TEPekDxoG5BfuxHYJeXN6Gn_4hNwVFaPDQoCVYx4PUZwWjQ-P8ysO46_48oXWA0oY6pQWxTWO-vQtcx4Mz76Qe1ddXt7slFkF8EjwO8s8n_D4Z1W_4X1YeP49jaVEsy3uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
ایرانی‌ها تهدید به ترک جلسه کردند، یا حداقل تهدیدهایی در رسانه‌های اجتماعی مبنی بر ترک جلسه وجود داشت، اما آنها ترک جلسه نکردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66681" target="_blank">📅 14:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66680">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس:
ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کنند.
همچنین دارایی های مسدود شده ایران آزاد نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66680" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66679">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی دی ونس:
من نمی‌توانم 60 روز آینده اینجا بمانم. به ایالات متحده برمی‌گردم.
تیم‌های فنی مشغول به کار خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66679" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66678">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5fcf3266.mp4?token=rHq24EJf3ipgalO6xtSJZT0_P8-9DWtI5XngGfHdbfyL9J0v8F8V2PAqJPjKU_C0nbIGZEvtolDRkqb3NKQGDswxjbs6e8bhDqfYMXXfPQG_WSKY2ue4if1uNgjfhIEIsOVquYi9A8ex-Ra_vhKfAd7IH3H5qiZvcc6ZIhvfmQJ69zDLQGKTAVpzn46qERgz7h7Mj9gwdYpd452ujNPoLKWTSZOOkZKmhX6M7q938M81IoRGmrwKA-keLiZsmFq-UbPUHwxQos1HiOiu8KOWG2cVAuiKKmUEv5JajiycdOtEDeQLORXz8eY0eR0xhxZufIljoL9Nrtsg1xDgTb0Emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی دی ونس:
همانطور که ترامپ گفت، گاهی اوقات این آتش‌بس‌ها به این معنی است که شما کمی کمتر تیراندازی می‌کنید.
اما ما می‌خواستیم مطمئن شویم که هماهنگی مناسبی برقرار کرده‌ایم تا اگر تیراندازی شد، اگر حزب‌الله به اسرائیل شلیک کرد، یا اگر اسرائیل پاسخ داد، ما واقعاً با یکدیگر صحبت کنیم و بفهمیم چگونه تیراندازی را متوقف کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66678" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66677">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38c244991.mp4?token=ibio4Mry8UClgB7t0vXGfvTiaZJQOFwgFLhMgX2RNYJIuU_I4kKPI57wjQS7C9HALCZSZZDUPUioDZBnj_OiMiHcSlWLW1kcEtp3R9M-vEMtkTm4aT5On_r3cqjcWojp1dCR2O_SxcS4YNabmTjb0ubYMO5iVmCM7CMj2yX7L788e2M_5vvXCP8rQEmAWBug4J9KMrrwGBemD2Mw-kqgqcDqY_4gt7KZR9x2DmmNaUatkbJ8yBYXpchj4pI3LEIj67xd8tOpHtB4D5gsECHhqcAkhyG4anl3NsresaklGN9x--UkjSEhn-LdXQj3PBFaydn4qg3TV3ZnpfUiBvjs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38c244991.mp4?token=ibio4Mry8UClgB7t0vXGfvTiaZJQOFwgFLhMgX2RNYJIuU_I4kKPI57wjQS7C9HALCZSZZDUPUioDZBnj_OiMiHcSlWLW1kcEtp3R9M-vEMtkTm4aT5On_r3cqjcWojp1dCR2O_SxcS4YNabmTjb0ubYMO5iVmCM7CMj2yX7L788e2M_5vvXCP8rQEmAWBug4J9KMrrwGBemD2Mw-kqgqcDqY_4gt7KZR9x2DmmNaUatkbJ8yBYXpchj4pI3LEIj67xd8tOpHtB4D5gsECHhqcAkhyG4anl3NsresaklGN9x--UkjSEhn-LdXQj3PBFaydn4qg3TV3ZnpfUiBvjs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی ونس:
ما می‌خواستیم سازوکاری برای باز نگه داشتن تنگه هرمز ایجاد کنیم.
ما می‌خواستیم مطمئن شویم که سازوکاری ایجاد کرده‌ایم تا مطمئن شویم وقتی درگیری‌هایی ناگزیر پیش می‌آید، می‌توانیم از آنها عبور کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66677" target="_blank">📅 14:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66676">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=eiswEYGajdrX1ph8dCNQW19v-OCle8qJXNLpily5CKTK6qng27jn9aSx_QdmEngWyQZTf1SgGkAnWuoRdFqV1hxbC2yMAbu0L4HyqWUf3EwaurjVhsMU3xJELUtVchq_oFQ2C85NV5B1PAlAcEkZqoRbh21KXG0RuwS8_m4QZJoNL2WYnjIJZu1eBtfuAvTZInPpWD2L8suRUmf2qYzEvPBjehUPDYy5Ht2RRBHIgCc0_bdv9ntzNtq_Q7Ys_vxD2bucnAkWxhV6eY7_CcM0dEIRSNTe1JfQEzDB8a6yr4nqu0v7puvLl0USw5eSUoN7WDzr1tlpfXnfYvxlF9t70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8d548d8c.mp4?token=eiswEYGajdrX1ph8dCNQW19v-OCle8qJXNLpily5CKTK6qng27jn9aSx_QdmEngWyQZTf1SgGkAnWuoRdFqV1hxbC2yMAbu0L4HyqWUf3EwaurjVhsMU3xJELUtVchq_oFQ2C85NV5B1PAlAcEkZqoRbh21KXG0RuwS8_m4QZJoNL2WYnjIJZu1eBtfuAvTZInPpWD2L8suRUmf2qYzEvPBjehUPDYy5Ht2RRBHIgCc0_bdv9ntzNtq_Q7Ys_vxD2bucnAkWxhV6eY7_CcM0dEIRSNTe1JfQEzDB8a6yr4nqu0v7puvLl0USw5eSUoN7WDzr1tlpfXnfYvxlF9t70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی دی ونس معاون ترامپ:
در زندگی خود دو فرد بسیار مهم دارم؛ همسرم و عاصم منیر.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66676" target="_blank">📅 14:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66675">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ry8FbTTCY5nC-OWvGSo0u1VOnJ2htcGj5LuqRgI1B7QE6grNDseVWaWHespOLw6tTHOOKu723YhRRTkPHlPWH8kL2gyXQjAjbCWhHPruogMglzgvgpspJ3NrpM5ugwuaVdX0mWaeVvFnea5bIfdnRSTPdhsHp-IwCy378d8tRokMuW7gkhAbfCcXi31JA4z_yBwBnyt2-sdxF8v3m5KCERfL4cHILbA0H60F4HYJol9p_Xk73z-oEMr3WDjlqHm1bwxS7zTS1MnOY28_u8bpqir4TubNCPonIKPK9Lk_S0PbJ0AT__tmK5vzGH7EnR3D1Ef14N7KFOkDHB9dP4BCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1295a122.mp4?token=ry8FbTTCY5nC-OWvGSo0u1VOnJ2htcGj5LuqRgI1B7QE6grNDseVWaWHespOLw6tTHOOKu723YhRRTkPHlPWH8kL2gyXQjAjbCWhHPruogMglzgvgpspJ3NrpM5ugwuaVdX0mWaeVvFnea5bIfdnRSTPdhsHp-IwCy378d8tRokMuW7gkhAbfCcXi31JA4z_yBwBnyt2-sdxF8v3m5KCERfL4cHILbA0H60F4HYJol9p_Xk73z-oEMr3WDjlqHm1bwxS7zTS1MnOY28_u8bpqir4TubNCPonIKPK9Lk_S0PbJ0AT__tmK5vzGH7EnR3D1Ef14N7KFOkDHB9dP4BCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین کشتی کانتینری پس از پایان محاصره به بندر شهید رجایی در استان هرمزگان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66675" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66674">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66674" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66673">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66673" target="_blank">📅 14:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66672">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=NYnpKYZ1ypc9e_Pqq8awP-DBNYfurGAnZMUM-ml_LgYCcBMEMP5TeRNZYhdtuE3ZPnGgGLzYyXMMgTY21nr_jvU9QHnIA6poxyhh5dahLAW17Cb9zjlEQ43jJvKAIW7pX3zzj7jDzHFjtompOJ_v2ij7ZRpxTUUbIP7yiyKhJV-9i9nFZUAOPvJpTxaC4ezd743IaGLyWJKg0VCR_X_E__tpkR1R6F6bgCWfsbu3PGZqyLZT01ff69096DqyP45Pfw1u8bJlLkJbebS6QTg4v8bzR7M4pLLlb7nOs_3-rdRXj7y7TmmMTCzdiTt87qo36-eh5gFaHWufdnOYgS_R4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e293401f8c.mp4?token=NYnpKYZ1ypc9e_Pqq8awP-DBNYfurGAnZMUM-ml_LgYCcBMEMP5TeRNZYhdtuE3ZPnGgGLzYyXMMgTY21nr_jvU9QHnIA6poxyhh5dahLAW17Cb9zjlEQ43jJvKAIW7pX3zzj7jDzHFjtompOJ_v2ij7ZRpxTUUbIP7yiyKhJV-9i9nFZUAOPvJpTxaC4ezd743IaGLyWJKg0VCR_X_E__tpkR1R6F6bgCWfsbu3PGZqyLZT01ff69096DqyP45Pfw1u8bJlLkJbebS6QTg4v8bzR7M4pLLlb7nOs_3-rdRXj7y7TmmMTCzdiTt87qo36-eh5gFaHWufdnOYgS_R4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پهبادهای اوکراینی بر فراز مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66672" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66671">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymq14t1KU6rftUVtB5W0Yb8TRhs1j8dFBCrSzRIwN5oztsqEE8hzYuue87CnabzoUN2Y6mv2Ty8zij6IBXOp-1oj-pFKgpnNoWVawVz_P_ehwjYVEOB3g6nHM-ssREww4-JBadio5okNJnHlU2hpOWRQYW8cCKxV8v9j9kKaiDT26wDuzwmq2vm4x_549peNlQoSfcWTakMXQGGFhhDrxDBwDwtnHCL9Bdgpfwp0OKdoFN9cK_ccmbTxopL-QqXbcGg7R2HLFsoDtAfjpiEjZNKC--ZonpUvtu4dYjJr_hyKcOs6xn1grsJovSw3FNd9GrzdYCNLvnEyPCtXCORBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل بقایی:
هیأت نمایندگی جمهوری اسلامی ایران بعد از انجام گفتگوهای فشرده درباره اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵، عازم میهن است.
این گفتگوها با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ متن یادداشت تفاهم، از صبح یکشنبه ۳۱ خرداد در سوئیس (Lake Luzern) شروع شد و تا ساعات اولیه بامداد دوشنبه ۱ تیر ادامه یافت. بر اساس بیانیه مشترک کشورهای میانجی (قطر و پاکستان) که با مشورت ایران و آمریکا تنظیم شد، ساز و کارهای اجرایی برای نظارت بر اجرای مفاد یادداشت تفاهم پیش‌بینی شد و مقرر گردید گفتگوها در سطوح کارشناسی و فنی برای پیشبرد اجرای موثر تفاهم خاتمه جنگ تحمیلی ادامه یابد.
با توجه به اینکه طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی، منوط به شروع و تداوم اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است، توافق‌های صورت گرفته در این نشست (به‌ویژه بند ۱ در رابطه با خاتمه جنگ و عملیات نظامی رژیم صهیونیستی در لبنان از طریق ایجاد یک سازوکار کنترل منازعه با مشارکت طرفین و جمهوری لبنان، و نیز بندهای ۱۰ در رابطه با صادرات نفت و محصولات پتروشیمی ایران و ۱۱ موضوع آزادسازی دارائی‌های مسدودشده ایران) تسهیل‌کننده روند اجرای تعهدات متقابل خواهد بود.
مبنای کار، «تعهد در مقابل تعهد» است و جمهوری اسلامی ایران ضمن رصد اجرای تعهدات طرف مقابل، از همه اهرم‌های خود برای اطمینان از اجرای آن تعهدات بهره خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66671" target="_blank">📅 13:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66670">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=fBg7-NzzcQiifk8eAb1ZRwQuSd89PeDlWfw-UPaOlWw9LuRdaWVksu9yiR6lzRtvNYgEeMfYgFwozFMMiUtih4blW7R8xV2ZzoYZHE-XOQ67TwFwAlXfmiMTFUWv_73us0BTvW_3acYOh4u_yg5Ro8njCtznF1h2lyW8-7f-Zljg-Ff0o4BNNkUong4ejD-ALBBG1NIBPXop_80MKxYjFcpeSNKYCN_fegmZR0T6sKwvPPs3Thn-FKgM4mRWNBVD6Ph6l_HmZlUY5-L98h2v63BXQl1Mb-CPUuu7BFqGjpZA32FWSEFoIg8pc-JWkehHRthM8RLfAg2vfcy8LzjeLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe1a1177a.mp4?token=fBg7-NzzcQiifk8eAb1ZRwQuSd89PeDlWfw-UPaOlWw9LuRdaWVksu9yiR6lzRtvNYgEeMfYgFwozFMMiUtih4blW7R8xV2ZzoYZHE-XOQ67TwFwAlXfmiMTFUWv_73us0BTvW_3acYOh4u_yg5Ro8njCtznF1h2lyW8-7f-Zljg-Ff0o4BNNkUong4ejD-ALBBG1NIBPXop_80MKxYjFcpeSNKYCN_fegmZR0T6sKwvPPs3Thn-FKgM4mRWNBVD6Ph6l_HmZlUY5-L98h2v63BXQl1Mb-CPUuu7BFqGjpZA32FWSEFoIg8pc-JWkehHRthM8RLfAg2vfcy8LzjeLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
روز اول جنگ آمریکا از طریق یک کشور اروپایی به ایران گفت مثل ونزوئلا تسلیم بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66670" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66669">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=FdP3wXY9qKqFZUZ0SZ8VIQ7i39NDkNS8b0TCm5cE_66oCa0I055CWJcZoVqtDLD9ZYI6gEzcGVZd67LFCAgcROOt1WlmkWxxSAtyviIt7X2oxyFbb89sCx873EM57oHqEHRBi8e1-krg_WtysadckPXM-Z443f4Xeu0h3uyWYX5N-Rwq8Qz9Z_-1iRKYp2jKzZDImSFI0tF_qqkf3afxapNNMHiGnyUhElWW9pZuC3diSVrce_G2m1CFgPJjGQUTD8lbJRifWOE9ggQgi2ir9MxcCKO_e235uwNLyEBtmrc5JjOZ13IOF2AcOqqb9PdlTIHqSr7dRiIn-8J6dZTJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7d3de545.mp4?token=FdP3wXY9qKqFZUZ0SZ8VIQ7i39NDkNS8b0TCm5cE_66oCa0I055CWJcZoVqtDLD9ZYI6gEzcGVZd67LFCAgcROOt1WlmkWxxSAtyviIt7X2oxyFbb89sCx873EM57oHqEHRBi8e1-krg_WtysadckPXM-Z443f4Xeu0h3uyWYX5N-Rwq8Qz9Z_-1iRKYp2jKzZDImSFI0tF_qqkf3afxapNNMHiGnyUhElWW9pZuC3diSVrce_G2m1CFgPJjGQUTD8lbJRifWOE9ggQgi2ir9MxcCKO_e235uwNLyEBtmrc5JjOZ13IOF2AcOqqb9PdlTIHqSr7dRiIn-8J6dZTJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کاپیتان نفتکش وقتی میفهمه تنگه هرمز دوباره میخواد بسته شه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66669" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66668">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f482273e.mp4?token=IzmoOOudoNEXNNbIH52Aj1-3sWNFNf5GwKwnC5-w0z0i8eJ8IJDevcrB_IWnDZjuCnah5LT1zAgKD4cNiDelwmj30K5DXGN9621gkeV3bJc2kdOQyLzujfFHd1yT0X_tOpX_lPt_WMk0S99uD7mpX1DYiRHItu0b6mLofC7-tCQFNr59e9Qv5oVixQiZ5eX5AIpOZxEdWqjCE4coRmRHRu6JG1jlHOQdRTkW9w8FePYm8d2naXKUf5PGg4cUGqGSjTCkEKrrf4bJPWxFlYTynUBKF6ct_wX5DBry-90zV39TKFw97HvT3IkpcrOEQp5WzwvwmeyIWAG3z2SZiEdlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
دلیل موفقیت رزمنده ها بخاطر پشتیبانی ما بود.
دولت بیست میلیون بشکه نفت رو داد به هوافضای سپاه تا بتونه خودشو تامین کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66668" target="_blank">📅 11:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66667">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdiYeokO1FUgr1gpCzGT3L3wbAc0lGEN9uzJa3DYg-CZKWz6HNGZIXbI_TwI_ri5CTN5q74TFvx_6jU91YZnpcZoGvh0qKacZGQQ8GnXKEkzIF0KhlSppbi9MsqloRGL17N9WoFduHkTWBDvHY6CVBoCiMunNndIml3ZD7zGJSxYBq_O99n4J050_ZBlhoLbm9tHP7QU7P4DVjWJ7Tw-7_P_fv_CxiBOSnjLWBW72168qwZdVcd4O4nRuxGllh5dEMUTuAcBRK3NRZZyBy-NXpw4alcSWzkERPrrgJSq_s-DrHNsNpej886ba9xWLxhDs1EQU3OPNDoqn63YpC_CXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه؛‏بیانیه پاکستان و قطر:
نقشه راهی برای دستیابی به توافق نهایی ظرف 60 روز تدوین شده و یک خط ارتباطی برای تضمین عبور امن کشتی های تجاری از تنگه هرمز ایجاد خواهد شد. یک مرکز هماهنگی برای جلوگیری از درگیری در لبنان و تضمین توقف عملیات نظامی تشکیل می شود. همچنین مذاکرات فنی آمریکا و ایران در طول هفته در سوئیس ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66667" target="_blank">📅 11:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66666">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372418cb00.mp4?token=C--9kmZRzfahi6RefqsRE1ddQoGESCpAiwDb376E_ih1wbQok0u3zYp_0wH81oeEonwnPN_ALPztHHOALF2Wr6aJlHN3BQQum6pjD0uJGx-BRliTNMQxjj5lI6-YjITimlYZeXIOqtPnFE1lwhlPE-ib4n-Q9vQ_cyOq1Psl1RchSZ7AAMtVHMlaBiwhojtkLCbhEFxI4Gp5afVf5b5RjAuzrtq_qvFrjnBa5z-K54vbtQUd0QNH6lrtg52awHQv5PCszVcC-cfYpQAusk0ScdNO9auKyM2edFXAUw6ZTdcOajwe49MYY12C2pNrG72mIJSA6Q5LIXSBVMCmHBY5YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372418cb00.mp4?token=C--9kmZRzfahi6RefqsRE1ddQoGESCpAiwDb376E_ih1wbQok0u3zYp_0wH81oeEonwnPN_ALPztHHOALF2Wr6aJlHN3BQQum6pjD0uJGx-BRliTNMQxjj5lI6-YjITimlYZeXIOqtPnFE1lwhlPE-ib4n-Q9vQ_cyOq1Psl1RchSZ7AAMtVHMlaBiwhojtkLCbhEFxI4Gp5afVf5b5RjAuzrtq_qvFrjnBa5z-K54vbtQUd0QNH6lrtg52awHQv5PCszVcC-cfYpQAusk0ScdNO9auKyM2edFXAUw6ZTdcOajwe49MYY12C2pNrG72mIJSA6Q5LIXSBVMCmHBY5YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسماعیل بقایی:
با حضور میانجیگران، سازوکاری برای تضمین و نظارت بر تداوم آتش‌بس در لبنان و در تمام جبهه‌ها پیش‌بینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66666" target="_blank">📅 10:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66665">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
‼️
مدیرعامل توانیر: ادعا نمی‌کنم که بتوانیم تابستان را بدون قطع برق بگذرانیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66665" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66664">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS7TEkB0m8R75is3XwDmfW3I1uzJRLpScs_iZNkA6FnfiuGxHiQ7VoOKCnl5dQSW2cLQSdCxUlVQI4JobBuhe-4lKYoqa02Ze2QBg6XQlwhgb7adi_r4BmWp-aNiKKjTcGOGwF63loT4NYXUbsX7ppkDrB5u-P8XrRtmlMlfXWJalFco0lNObaQKXUX48u1V5DK0FfzqiAiVjngOmFLwHwUY0FVJtL0GkbXe-Auv4qlY42pBh5MXcqGTAlO6gCVSpS3Wg7gkLsV804bkYdF1cW1hxNSItX9g_PrAranuKl-kTAvpkudKOu41lKRK5Jq-pCz75buALcKLvgesNyIrEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
عراقچی: تحریم صادرات نفت و پتروشیمی تعلیق شد محاصره دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66664" target="_blank">📅 09:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKksPgqzqtNSMDtiYCke3lHjrY73LPwnI-vkqXQSQKSR_w1pPOldROMb97Sob38WCQqMIaYaUxa_71F2PHCMCDsL3ODVRZgpY9GO3onCcbxmiHsjuarB3movjRAvrr2I_a1WWeE26HQdSjGzFvA2YcO6hhH0CVoYb0PReStuYBNYKlWXRvC9HYXTv-5D-YroyGNcjDGfekoZKp3YZm5uy8cezcWVZUUsKqqquE_ubyYYl1nJrouRI71QALefJR5Eo-3rocIZPs2BzF7TBmm56ZcmITHPTVNGcaLMZzGbEE3pQec3hPxZPrl1Xs6mYw7NwlPveh485ssq-DZjWk7RXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66663" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66662" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NXZ5lA_S5JZz_LEnFZxKnPRewLoEYxuiADa5cLQS-GNuEut4TF1z81Lb66yD47jztKW_q-G95Lh3jK2jaCWja_kot5NIBEhpDLs5nH37s6pNQdhOSKlDg6r9CAqQYiYd4ZzbRuledsAwIQqodQEZSSi3PkEI5s2gc9glrew8nzYXlYuxsv04FvLEi_jjMSXxOqjy3gO-umHYz_Urwc_5OeOmz-sJg1nqbXM9yGD0RqHRXq-cmA2ACUlDkCduYhH2Jdbo585nJeA6Px5SnOxFy2PdVAefehS8K96Rv-1SzFSMYPu4anX61qbxGboIU4X2Aha-9vBEPnCiQuB6tHDuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66661" target="_blank">📅 02:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXZEjUkz7UtAqz2CO3nQzL1-FzHr-6J65EhXQ0_-ZHD_oIt-tc1O4a0jiIzTiVMSb_gIAn94qo9TA-YkB1z0FrmFW5rVtp8J8yaFnCoPFAP8lA8juQlCrQjlEwBjnqIqXZqVfO0C6sF1VLOfUGBRX-5mxe8U_M1kConyT-hiPum_1IyOyDwQS1975w_38zA5s42cY2hqPnhv3V5qxABypu7xHu6uudt2uYkC-Dww4MJaDdcWjaH30hT_FaqZTZQaxqqA0LCBhUdOoo2RpoUdn8mAyC8ATRRiLSk1eRk3m4FSb0qwwr01DbGoxelSFK771qLnvKag2HT4ojcQQC_ymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قالیباف:
ما به این شکل از سرزمینمون محافظت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66660" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dErKmu17BiCvQp4mF7StGWl4aVUFiZKZ6BjRz-KhJKCJq0IE1YTajtla516jUNdvb6C0vHOIQTrAyDFseZoivKRFOowrnoxkuzrGrn37NIG5zJmC9pLkZ97AGcLFS0-yJdSCCFgbhU2Vowv26EgBdyTqyypLb5ReqCr5CvfwbftDZQ9BIT8YwSUeb8AQwObyK2eqcmFX7i0P4dSOc6ZUW_MTsgh5uoL7EAgFOGv46jfCbmYlXQcwlSlyBISPXlNPK5TvlCDqS-X9_G2f-1ulY6N8_EL-8SvTpMxdCypgK1thTopcNnNk5dY3-B5Z-Dxr6OnsfGZJxPZj_8rfsu50GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
تیتر نیویورک تایمز فاسد و شکست‌خورده: «بعد از تقریباً ۴ ماه جنگ چه چیزی تغییر کرده است؟ تحلیلگران می‌گویند چیز زیادی تغییر نکرده است.» واقعاً؟ ارتش آنها نابود شده، نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آنها تقریباً از بین رفته، دو گروه از رهبران برتر آنها از بین رفته‌اند، تورم آنها ۲۵۰ درصد است، اقتصاد آنها ورشکسته است، سربازانشان حقوق نمی‌گیرند، تنگه هرمز باز است، نفت فوران می‌کند و بازار سهام و مشاغل ایالات متحده در بالاترین حد خود قرار دارد.
این چیزی است که تغییر کرده است، شما بزدلان فاسد و بی‌اخلاق، و موارد دیگر!!! رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66659" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=XeVSCOp1I2k89QwGj0VyNn18qPwz56_iSr5bm8sWmNx5JaBLyxZy6o1ioKQAlFb7DvPceiiFs-sdupwiblG5QLUpqQQEpc3MaYhwblcdD9CXzx1BCkujz4gtZzHYbVNsgtDl-xRCJwojsJ1jQRP3lfAIekJ9tWgapGZa-aB8JB8Rny8CYFROmtYvMpfVETzIsbpwM1GRSwcqj5BvZR9ZTcQkIoAalcqOe3OcTpBEcRLtLiPZUsXw8MS3F1HfgMjgIvmzpdauwxSSAy2oO-6Gl1WZZUyUVZjyr6ZcR4e3f-LwYN0f7tEqtC1vj47AEx6IN7grtsVTdrKr3m3QVao-Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536d5ab3c7.mp4?token=XeVSCOp1I2k89QwGj0VyNn18qPwz56_iSr5bm8sWmNx5JaBLyxZy6o1ioKQAlFb7DvPceiiFs-sdupwiblG5QLUpqQQEpc3MaYhwblcdD9CXzx1BCkujz4gtZzHYbVNsgtDl-xRCJwojsJ1jQRP3lfAIekJ9tWgapGZa-aB8JB8Rny8CYFROmtYvMpfVETzIsbpwM1GRSwcqj5BvZR9ZTcQkIoAalcqOe3OcTpBEcRLtLiPZUsXw8MS3F1HfgMjgIvmzpdauwxSSAy2oO-6Gl1WZZUyUVZjyr6ZcR4e3f-LwYN0f7tEqtC1vj47AEx6IN7grtsVTdrKr3m3QVao-Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساکی و رفقا بعد بازی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66658" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قلعه نویی تیم ده نفره بلژیکو نتونست ببره
بازی صفر صفر تموم شد
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66657" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلژیک ده نفره شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66656" target="_blank">📅 00:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
فاکس نیوز به نقل از یک دیپلمات آمریکایی اعلام کرد که هیأت ایرانی همچنان در سوئیس حضور دارد و مذاکرات ادامه دارد. این دیپلمات گفت گفت‌وگوها در طول روز به‌طور جدی دنبال شده و رایزنی‌های گسترده درباره تمامی ابعاد توافق هسته‌ای همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66655" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmPF_U2k5MrObuG1ru-LsUL8an7WccEucYMvOATvJMmTxaimjdVZ71PZt1u62NED2rQXrw_VNsHTy27HhubDz62Qb0Qi0hjPw37UltgufgW2WFLUi_WcFKusowANs2EEpm2ErNIwIrn_OwtNWNA-8uDtBx-1pdBjMQLDB4WElQB4dldbyOgqqAmdIAcoz77UuNS90Jeh928h_Is0sWZiWEupAIb3Pu2HgzPEOy5c60HlXvknvrM6CxZelHEur6Drp68HtGW-F2iqyqkzfZAaN4ZcR2yHvatLVl5HN6KCILJzOX0QE6ulK0IKpWFlSvLX4gOpA6rBrqpqANC-XpqOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم امسال:
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66654" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اخبار غیررسمی از انفجار شدید در دوحه قطر
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66653" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66652" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">طارمی گل زد #hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66651" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طارمی گل زد
#hjAly‌</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66648" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چقد خوشگل بازی می‌کنه بلژیک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66647" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4NBLKNlMulo3KkIfoBQ6QZEv8y06jfv-DyZYwys2T0NT-X1X6Q8YVU5_FllnBH3eDndO5ETEVIeWH_kbZCCBKVoDl2npz7KY79BuaanCqPjPCcjd-0HDO6mMIFGpcdVSY6hJUCXG8Rh2Tm9_i9LFCVBekX5SpQ4WRamqv9vB76bH6v7nxMDD96rRmSFuuXF0_7LT2SNgB7CCE8kxRBO1D0jaeSJIIgta1BU4yaZEARdH7hLOHAOMJR_InJgdZsr2a79z5GyAS9tU-D2WNnTg_gS_o0EUK_LroumCYhuMy46pk-LlZ9WX7Bwp15xeaiyoV5Ch15HA9KO1DOoW2g4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از نکات فنی قلعه نویی به تیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66646" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=sTaqbZPlMrnffF1hISge2sr_ZlKG-yJF4nagjFa3BMs-8XVHdQxec8kbKW7hGKYmLXzKmED7Clvg1zLYPs-N5yKY53RAwOtr4XfZ1AWRyDWvi82FKGki86K4hmLABLqDZ0jx-gtzdnEaTCuUaRdgxPgD09nrjAFMpHaR_38lWzi4VKCGI9oAU3ue-JuOZ0jYxID7VZSbqasThB2yTW0Pzkt4QEPb_11cDPRoy7_rcZjYDd_iXo0hef4DDoWqvzEi-hd7cc2RAi0Rmn5ZHfUPZlOnltERoGs-BpHT8MxzVHL57xZjbmVLXRaW8-hDZHMVPmwFJ5ivl1vs0-6OmI4lzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=sTaqbZPlMrnffF1hISge2sr_ZlKG-yJF4nagjFa3BMs-8XVHdQxec8kbKW7hGKYmLXzKmED7Clvg1zLYPs-N5yKY53RAwOtr4XfZ1AWRyDWvi82FKGki86K4hmLABLqDZ0jx-gtzdnEaTCuUaRdgxPgD09nrjAFMpHaR_38lWzi4VKCGI9oAU3ue-JuOZ0jYxID7VZSbqasThB2yTW0Pzkt4QEPb_11cDPRoy7_rcZjYDd_iXo0hef4DDoWqvzEi-hd7cc2RAi0Rmn5ZHfUPZlOnltERoGs-BpHT8MxzVHL57xZjbmVLXRaW8-hDZHMVPmwFJ5ivl1vs0-6OmI4lzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
ایرانیان حاضر در استادیوم لس‌آنجلس
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66645" target="_blank">📅 22:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
سال‌ها به ما می‌گفتند: «شما نمی‌توانید به خاک ایران حمله کنید.»
بله، شما می‌توانید عملیات موساد انجام دهید. ما تعداد زیادی از آنها را انجام دادیم. من به بسیاری از آنها مجوز دادم.
اما شما نمی‌توانید ارتش خود را به ایران بفرستید. ما این را تغییر دادیم.
ما خلبانان شجاع خود را بر فراز آسمان ایران فرستادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66644" target="_blank">📅 22:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در نشست بین‌المللی سیاستگذاری در اورشلیم اعلام کرد:
در ایالات متحده می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد، و در اسرائیل می‌گویند که من هر کاری را که او از من بخواهد انجام می‌دهم. خب، هیچ‌کدام درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66643" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=V9uMpRwY-PaASEjIvhuQH7K5SEohJsV2E6jsw4ZBjtiN-GbK--5MuwYBAQjLcbutxR66SPTQ1I_1DdrKJsq2bmdxiDVPRL-RDuZjiPujcrAriTsrdgw9-0GzrXPz98k_PGzRMZ5NwmTB_NJ1XzebXNufoPRm9j0nBtWzfuaEp_sGEl9s8b3liVlBO94e4pP_suiPZ8eb03C7c91Dw7WYbNhWZWFcItn7f39vK-6O_2DTJCAhME-sP-6Aaw_RL1cabGreykoyAHWu0_S3h_iviH7WRtZhe8GRD_6udPVaOwbsfM9hPx5x298tWFGVUGs3vnhJS-qAEEeyvqdZKlyjUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=V9uMpRwY-PaASEjIvhuQH7K5SEohJsV2E6jsw4ZBjtiN-GbK--5MuwYBAQjLcbutxR66SPTQ1I_1DdrKJsq2bmdxiDVPRL-RDuZjiPujcrAriTsrdgw9-0GzrXPz98k_PGzRMZ5NwmTB_NJ1XzebXNufoPRm9j0nBtWzfuaEp_sGEl9s8b3liVlBO94e4pP_suiPZ8eb03C7c91Dw7WYbNhWZWFcItn7f39vK-6O_2DTJCAhME-sP-6Aaw_RL1cabGreykoyAHWu0_S3h_iviH7WRtZhe8GRD_6udPVaOwbsfM9hPx5x298tWFGVUGs3vnhJS-qAEEeyvqdZKlyjUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxHrMZ-0wTiHsRLp6S6lz-dBCJ84ZuLIZPgnAciSaBTHsWOggkCsaYAiAUfjuKemVG-bKHBeqMNZavBreXvXX2bbpyzxD9NHki3FwC1YilpCG3lK8wpWNCQQVjHUSSg426T-ah62USpBPtNkRs7adlIYP-BSsl80TwzwDuTGp1CpvSKe3LAVJo7TVLsJNBRwW42mDWbZuBK23P401EHd7I-ZmSMKLd2lUOxjNRZ-m91zAoXSZZF0LXuCXbhqPYDLq-Fv-J9Eb7Ank2at9Aa79fssiWiCFQ1j5OdlEJ7PhOR19gyMSz-rFuHS3vuwxZBevLfak0oZcL4leyGfAWXC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnU3pOR43H4fxMIZJCmtVK4w5A8MNbwO0w3ypJ1jhXOjee02doLGCVccfs_1-QAq8xRB_TYpwPtmYJ8ArOJUJAPp0qZ9GXq6oggb3ovRm1-h5bI_ER0q2Zve4G7F-L9gBRTDLfvi0Ucjxrxa4JpMCrDxjXONolcZlH22UJo0E0U5JzYo9OrgVcDsY1izyjYqtRdNlbAqKxBODdu2Ift4Ddr8uU8Z-WgIUA4zS9YRoZICmYill95eLAJZ0urMK2RO8t7KrYGk4x0Jq2Rt6qgt8G25jZwKxgU_KOqHptcK8uy3ZM5QX9aUYqAJjb69GrvOG8MW-Xjc96F9l-oe0u5zNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUTaBa6ZU5o20FlqgBTNWUnLSiS6TQAj_dfETWNK0b_EkOUQZpZ0YRSlVJHtKMsBHzNMYwvq3IptClaPRmKi8CVylr5sUi_TWTZGSomaKEwPnmDMooikBshzJ4o21mq6Hr1Ev6KRL2MVSmOcjVpN2ZEqIPuaFjRF88-OwV1_3rYhdWoUTJB2HCNUwbtDBiQlW6T0jUuvmuuuy1ySclFKvpIJMqF_U3DdnRlnQZBea5uLFrBNl_zsjxlNKoXTIboqk7bYxM7HIxOw2NWXhZHCxX-V37cKXGnRlwiLOZEDQGvcBRegnvX9lDT6J-7UkUbZg_ODLWESuzMzF5I1KdHEJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcvINwI8IwolXbvuLGCXkC6R4didde7j4f5BV_aaRgoIQd-mNvvZ2qXykdmdTXlDjGdReotbDf-Dx6FuiR7egqbFn_LqvQQ1a46dgAnDLm1sStjCHTQjcEa_QhPFCuF82MapzGuf2SsVRcSB96gQwNYPSXGFgLeiH917859_banJG-ZvGjo2LoF8v8QzkclaJe8FE9WoLVZ6cCkPOdEdlKGqe7IFyFc1UO7bOR9yoLKEVDU7AWaLWIPs939oyCQVXSZCqUTgWoE8OjpJImSXDZyQeGW5IRX7oeHPUxLC0lsEttXGA8609DSD6GXibCKZAq9-DYPuZFwYKKvCUV3GOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUXXkpeeVpe_c2UThaHuUKSHwone9h9E3kk0cuKGDYVFdgxqfXa2KAy42QHMcLS3CQUJeX_VNFrHn7FqSmv9DQ3dcn-KILrwBV4vhe_hq5xTu0dBIztpI9e378d-6njO8oXQSyDFrL_ijVZ5MSoXWKd4IkmIEKPRGa1_Xo2lruMt0Ei5Yonlt2t7fhX8_J2CTPBEAWpEOnSsSZjkSN5xLHUtGA6vUsSeMG628A01D-NWwQ7iNSBIJNVulXeF3VmDLftcig_ameeCdn-OLi0VswDqymiXLnMzp8B7S62Wxqm0xgKk7Z6sgwdYcmGScNQcqYIrWziWkJWVq3yNn4yo5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgYiGA1TfiHWRYj6_6K0VsSh-TeM3k3bINOvzCoh2gmfQvp2G9Et6HyWDez7ttVjLuk8CneGOKv7ZLhJIWRRB00ccjF0Jtilgwmjs9j811Z7OCwQf1LUCTLJLmL-LcwvUZ1oyo54lm5dxYh8RJE1GM16cP3UAI7HzeCljuaqmzWVdR93VptPq-xyNXCLJTQbHZz-EvdkRFahBYkT3RNL8QgnhHAjVl3ZzVyQHaEKt5HrP3zbvOeMJWxx68QEP4RRfzQ_3QwZpEsChoP8Kj7EgPN29V-pdM4LXWJFt-ExwPnAMQDtBiV9peoOrR_6A0XJ7t7TV1n_ZZjdGv82kiT7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFGmi1Is5kD2lmoe562P6ssp_QPku1HuL7tfcf8dtMX-6pBZHsaTkhixi2CkCJHEt4dAM5b37Kg5C5PJ1nss3ouYmKTsSfYZuCm0pZDSkcUfgvzE3sTxQ5gLZCO9LNe-UQQ-sFUULh5NKMmPHMnz5vOHhyDygzLpMycc_S7892liirN2xn0krjUm3vZQTJlWqPBAFVvOoNjSbTnzHZr5bKmrUPC0gn6c4nnssK1Kei3ZTigBUdkxPHtA0BwogyjBOOyXtexb6d-Y_iwHywTn-uL9F-5HlLdVBj8EwLN_4L3GaAU_mAwWFslPcjUJRzzkbDdhsDWh9fsogGpDi8wvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEQJgGbDwgAYV3OdOnRWVNXHzq9_uEso9qLLNMmhFNZSD9N1aSjkA1iqUY25wTzXqXkRiuLV_tK7smOBv3m2AuHVfRlsUnrPkCuI4P9DiqnRIfRUEChE27oVb-0PLjkBQaZpFTgqmKyO-AAjfELvfxkxBKTTyrq7zaSvJoGk2y6U9p1Wqeq27REq_odhhw_JY9L-P2tOs27EgRui8CTCX_RL0WwukLE2vqryB6RYQy7WmV9yuTucZaRTRHHPpqPxvJOPy_2EaNrwNdJtazLKdv9eEaZdBxWcObGfprkH3Es50xh8xN1k3NjH0ooZW7x7MHZZp-hzz4uUjypFjz3-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUQFkwQGs0fqH1hBY3y7Z6FkpOjZo0Bt9xC2Y5waBQQ78_QcIdNbKscwofNTckoGXmPwlXqFKs7BQQBwA9XGm_4jQIrIT9QlJ2JfxobGgScx2nt4sPNfjbfLvZKQFq6kLVd1beYuHJoJVsFvGy6evesWgW-naz_hJFTiunJ8bgCYRz9_gdN6YBI8uwbsX_5HaAdSOwBX6XiQLe0H0RAqjw2vkfaS3VEQWQ5xwD2UoaAZrw0g7J2UnUVPHHeizm0rR2RM0KFGoqWcGmarLdVsIAUei1cmHqENHkOYovt4xdb7XHsZ9ytI5hqWln4C-PQyMxt8NlI5MYTgGxgwIrNnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-dnsT3gSRdDUZFSgvGMnKWOz9-uqyZ-GlM2NhOOaBYTfbypQANYgQivlKVtwwBT9xhftKDjWTcWkmsKZDgdGfoZqzNKQFkwQ4Jfkqytf5Ojq-Exw38S7LGAqBSUnsCZ5Kt_Z5HErdupKbKfa9wy-w-42L7uE0apjutgK_TIjlZOwbX9b5dbmzIhG_4JB3HDy8anvTrz1gBAoHtu8ZnVocZjw7J8-u1ETuqnA95Bjm8ns0DkBbixUAevyhw0Oz2i1Nhu0CGW6oFJNpOvlYNaJN-Soj91A5UpsJGiGkrPJnC2N4XwfOFJgSKtTBiJ2JcxEcG6WHOS-L44iVeoaicDgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGHyzpeNcwrJmjjE8blyiXzRlaRzCpsRju0Xr642osq2pLnhPXP1P86bFmWagqOMCW3BuGNDgE6coJzeINMxRst2NeNq3ek0f4QsXRE3KxA9TXSHQQGWUMYJbzH1nxmiwhsOW-9TmRM9EQFehaBVCdREdVh_zeRhWd0phhJrLx0XKlMVAONh3A7R6b6aU2i7AFhIXXrE7Au9DC_KzOXb_HSkwKeryfcU4Ypfj2BWrSJz4Cl_mxzwkK02QghxwZKWieFbTvWJhnSafiOIdTvVJ461S8rkGzWoPzfdWq9I1qF4CldVN5JdqeGZEZMrY0kGAMqwDRkhOknGpMP6_UehNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEgzX9LHkqnqQh0sS6CwaEvz0dK5B6WUgHBfrqH9T2B_ZhRnhCYeIhDqbzrtjXj8fU4NJR_c9LySHLWbKP83K3cAWf1SeNn-OwxWwizlr2381shQXjFRHUzKhrsIKfNApkgPcR67lpYO5ZoC3G4SeUNxpyQfDgIcN3q0npQD3-iAVu4PMlur6pFMh6JRXPgLqf2Rnna88EUY-qccq2owC6ioYJ7fbTjKhP78F-Jyysjk-AQfso9RpObxoYgETh6b22dQITHKWR-4H2_i-M-1fIxwDs2UOYnO4mqDzHJazg7u4pgXuXRBTsojKs66vDE7tBBt8auZNJaz0RTG3ZKzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=XEvBpmVn43j69PI0mchPTiw34gUcoYN16sYjq2rEi4uHSIElpxQX6g6SrvOs0NmM73dXfsZ5XRZtokVzrDFKxwbDYIjhVQaHdhHF_Y4GDEDg8BgPS_duV_G_mhRsBE55sjtJBnw1ZwD2jtzgI9uuFXU2hqgcdy08nzOosZEA9bYTFepoL1QqgWtGDel8sv4KHZOPrFYV9PbUJidlcaYsIUAESuzioyiykMB15uSjuV9THuSVHXBF3EBQeMIPW7nDhDrnY4hsifnwLwKhoW23Xbv57jIZaF7bneASACmylcT_gKn7yd7iEE5uv1PqI5HAmy4WNuKkYkBLxqboHooYJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=XEvBpmVn43j69PI0mchPTiw34gUcoYN16sYjq2rEi4uHSIElpxQX6g6SrvOs0NmM73dXfsZ5XRZtokVzrDFKxwbDYIjhVQaHdhHF_Y4GDEDg8BgPS_duV_G_mhRsBE55sjtJBnw1ZwD2jtzgI9uuFXU2hqgcdy08nzOosZEA9bYTFepoL1QqgWtGDel8sv4KHZOPrFYV9PbUJidlcaYsIUAESuzioyiykMB15uSjuV9THuSVHXBF3EBQeMIPW7nDhDrnY4hsifnwLwKhoW23Xbv57jIZaF7bneASACmylcT_gKn7yd7iEE5uv1PqI5HAmy4WNuKkYkBLxqboHooYJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=vPwSzSQt7tamhxC9fr5ySKp84R8VzSZeqtWMBJ5p_GXMJg3jnQQ74qHlP8SOz_gs6c2UCfaC54p2R0_nD62TCq3Bhet9UgTn6oVxN1jJ3Sw156eZ-m9OkQ0Dtv71ZC_dSk6RF3Ry6tdUfInpyipIQt24rUOixMtJhBEuBVRRsSVTRuqN6NMyU9pIEDzS2N29FhJz9YEDsVeaTwZmcq8foVvNjxK-NIaiBbvhziCCeACsEd6L-wvo2I2pouUzNXhA9NV8XyPVGYfoenCmIot_k19UvXe487CvXOWu6gw7zX52fc_gTYVvtdYfbBodNzKQwzA9iUFPFwOM9jvbw8JMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=vPwSzSQt7tamhxC9fr5ySKp84R8VzSZeqtWMBJ5p_GXMJg3jnQQ74qHlP8SOz_gs6c2UCfaC54p2R0_nD62TCq3Bhet9UgTn6oVxN1jJ3Sw156eZ-m9OkQ0Dtv71ZC_dSk6RF3Ry6tdUfInpyipIQt24rUOixMtJhBEuBVRRsSVTRuqN6NMyU9pIEDzS2N29FhJz9YEDsVeaTwZmcq8foVvNjxK-NIaiBbvhziCCeACsEd6L-wvo2I2pouUzNXhA9NV8XyPVGYfoenCmIot_k19UvXe487CvXOWu6gw7zX52fc_gTYVvtdYfbBodNzKQwzA9iUFPFwOM9jvbw8JMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGTdG7zm5BVkT6uipobeLKGIklbuVVrewvg8vp2ssZ7LzHQ3-5LiNKaS0CbzTsk3CzR59ixyVVKs7e8_leins_MHcQnsvwrLvoOh7wCShxboLTv91MKV6qEpW1tTCMyT3zx2MKAZiNaEnDvZbcoE9I1_4hCBakdsuEJBhan1CSSBX6yO3wSKNMc2SXy-q7lKVPQgpnYpBOXAdmJl0a8PwWHI_fq6Y2Pr9YzhxttpRU27XQDepzq_0TNFVoU0IzWOHEgPaYQ2ecMkQ40HX5BQz2isfgmgrtt4OsdI6CZNjSojvAAOJ7L-U3FgQeG6Ot7GHoFYVL8ifoZwCO4IgC_N-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvXE_6owhO9imvkQT1NtIhIqJ4us9SVkjQKR1RJoaC8oQntUsbWsRdmhivfdfe8FKlmjUQ8yEu4jKL6UX6t-5MzOJTiFghmmmM7SkJmkJEeo6G9THt9Z1XcKR36TVA0ZJNNgb4VWIjFzrJ1Wl2NiiD-goeuZeQ6IfcuU-y1q-W8ysTEDXKrGEUst8uAwzgUEXsbIJPepJG9F9GF51SO__8SxeHpBLRjdkGyKhFtdlrigPpA4-B1naS38Pw7_9qKEJRAvoZ3rb7UcO6nZi0qKz_v-NuFbjNLUUqbAUstcG1kmqiEOB82ImSeO462-KsV33AjO2eSQXXHi5RAIpeeEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=vNF0NLWoglxLM79-JdKC1GdHfYXMGRMz0yc0PqFrl65OTPGUiOhGZnOThbsQgfheYtngfy7REmGq-rf_5l1ETS7p3pMe8ll5LBIsdBiGZRRPA7T5gYS5e940aKoOAg4B4JXie9jWiZ5JQqm-odB1dcpAiUlPkoIi36JH03gM55Kc2CwoZGfWVmcQIzOf9131jnFzImjvLSLfsHbfEX-u-9d-cGLd7_Z64h04QLEKuRm35b6cJOZZFGYOjhr5d8riZn9PnKVFxdubR0htrY2bSvLfvaKUT9rcqsIa8bgdEtYqszG28yc3UogTiiSfLtyN-1gu6OPzJ0_QmCZezmqZGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=vNF0NLWoglxLM79-JdKC1GdHfYXMGRMz0yc0PqFrl65OTPGUiOhGZnOThbsQgfheYtngfy7REmGq-rf_5l1ETS7p3pMe8ll5LBIsdBiGZRRPA7T5gYS5e940aKoOAg4B4JXie9jWiZ5JQqm-odB1dcpAiUlPkoIi36JH03gM55Kc2CwoZGfWVmcQIzOf9131jnFzImjvLSLfsHbfEX-u-9d-cGLd7_Z64h04QLEKuRm35b6cJOZZFGYOjhr5d8riZn9PnKVFxdubR0htrY2bSvLfvaKUT9rcqsIa8bgdEtYqszG28yc3UogTiiSfLtyN-1gu6OPzJ0_QmCZezmqZGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18DjkdwQNGqyUcDDx9sKScj_2QlSpS82AwIXMdp_o8hycaLdS9ZpXeD8-iszy6XZGjPVYMps86oWCOBxRs_rY90WwQKQuEfBXptcZOSxaX6ygOztK89VNaPnQxB7seB7t04OimHNxBkwKv1oahtQ6c2F7frs28sLRHjEil4rofwqPo3jm1Okd9urjOJG5DoZl0IYGO4KOO-HBSDCJ-oYlSWdQEfN8SjyOcjs1ZOtmoCIGcvjfNcb3xHDdckt-a939Ejb6mydZArvRDMN4eC906kgBrfRQzY7QV0DMXucs_niTsAQsGyFtWpxLPrUlKuY79mij1lIwAaLNoJBXGhiARHR4sio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18DjkdwQNGqyUcDDx9sKScj_2QlSpS82AwIXMdp_o8hycaLdS9ZpXeD8-iszy6XZGjPVYMps86oWCOBxRs_rY90WwQKQuEfBXptcZOSxaX6ygOztK89VNaPnQxB7seB7t04OimHNxBkwKv1oahtQ6c2F7frs28sLRHjEil4rofwqPo3jm1Okd9urjOJG5DoZl0IYGO4KOO-HBSDCJ-oYlSWdQEfN8SjyOcjs1ZOtmoCIGcvjfNcb3xHDdckt-a939Ejb6mydZArvRDMN4eC906kgBrfRQzY7QV0DMXucs_niTsAQsGyFtWpxLPrUlKuY79mij1lIwAaLNoJBXGhiARHR4sio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt997t2yYjHfcCeezVj9VuTt5JvuOqD6VOPlHrW2n1tVS2XjlyxU74LhCyC9xrwMdcIovH8ialexEvyVIUWeCJbyEeuDSaE-tj_zAEU9o0-2XSgJHDGFJ_lNSZrVU8GntNE6Tg_qFHC1MMLhs7FRKEIT8M7Dp3PHE5PGm5QZmH0lLg3NIRoY7QkRGaxVXmm6EC0DQSvS2jju6ejvxH1-TIv1cOa2uDJKv5GZmIM7Do5sDS_lgs1C6sxMBYGilgTYpPiCLmGlZURCnNhbm4gQ-IyxdeiYaNxmzU7UaQ1qjzQC8ZyUJRs5ZsAsBqxLTuAI6TnxPRsoWe-Wij0GWpifog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=sLixDWkYDb-MxkF9vfR66axKcAHBMruXO3bxMV9OSk34D-9HxvNI0F9YBtEXjSofYLLYWrvjnOl4rNNx8mzywaXTqAsaeuLb9nquwH2VSbdGrY41cGjBJAGp7s3j8DYPwbdQr6U1o7N6qZwX1L36fmhWEAjYIA0cDTsJXJ0Q_DsNvObkWvBcyjAq9mdBdQHoK0cbDJw0zVyboCZNeQSq78j30X6NrWBmh6zoyFrbbWttDH8M1dhkNapjqtciKa1Y-aYivHTliLKpumYLbCqCHTbjAy9JZprKtEFXcKcBz4aWdetbEUXBUr09l3wU7OjwJ_UEpQRBwyRWhcJjK8xtL5brtBAqPeb-q8lQfj6jJP8LQZbOjigvKONk8olfxtLHE1UicLqGb_cu7jgF_czstf7_wthtgdcIEHMPZMKQGQuHOJnHCb2RRg0caztC9HNVrn8CGxaWhbqlNp3C4ODvuOmbrs-ndGduL8THE4WLi4R0fIbKUV2pezJfaIIhymLCrMQ7jhAwVaDcTy-xzmTeg2_I__1GYFjSsmAlDj6cRNQcraTAgQhciWjcywO99jN0wCNcUxl8zmQOZKsXvOCHmZvn73ZJp0ijIeUK6KAs81sQOlbjVS9IKBzySYCbk5TZRuO7MWvAupW4NMfM6nDdYTZBzYDBjwMw8_KV_i8VmEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=sLixDWkYDb-MxkF9vfR66axKcAHBMruXO3bxMV9OSk34D-9HxvNI0F9YBtEXjSofYLLYWrvjnOl4rNNx8mzywaXTqAsaeuLb9nquwH2VSbdGrY41cGjBJAGp7s3j8DYPwbdQr6U1o7N6qZwX1L36fmhWEAjYIA0cDTsJXJ0Q_DsNvObkWvBcyjAq9mdBdQHoK0cbDJw0zVyboCZNeQSq78j30X6NrWBmh6zoyFrbbWttDH8M1dhkNapjqtciKa1Y-aYivHTliLKpumYLbCqCHTbjAy9JZprKtEFXcKcBz4aWdetbEUXBUr09l3wU7OjwJ_UEpQRBwyRWhcJjK8xtL5brtBAqPeb-q8lQfj6jJP8LQZbOjigvKONk8olfxtLHE1UicLqGb_cu7jgF_czstf7_wthtgdcIEHMPZMKQGQuHOJnHCb2RRg0caztC9HNVrn8CGxaWhbqlNp3C4ODvuOmbrs-ndGduL8THE4WLi4R0fIbKUV2pezJfaIIhymLCrMQ7jhAwVaDcTy-xzmTeg2_I__1GYFjSsmAlDj6cRNQcraTAgQhciWjcywO99jN0wCNcUxl8zmQOZKsXvOCHmZvn73ZJp0ijIeUK6KAs81sQOlbjVS9IKBzySYCbk5TZRuO7MWvAupW4NMfM6nDdYTZBzYDBjwMw8_KV_i8VmEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=NghGU21JXmJ1Vk2ZsOtp5D3DytDkbgI9LtI4z7XXZ4jAHUNmoog7KJznuCkN7VuNGM3JcTku4OhXF6DsmChqnYvvMlGAXjNuZNR_yq-9rzpLeeoXxNrSiHkqG7n1p2OOyn-SnnGfvYjifBqWRMl1KhyhNJoQ3WSdwGwNFbHJ-1FOS_-3fMykw1RS4K-QTBaP4k0ilCtG-2D0h0w9zXY0v-a7tjwaXStgKInBJ7ORqLW8n6pXbSs5Yc1Gohpqf9qu5z98m-uUnbc9Wd-FnAXanWuSx7xf3A7DwlZS2id8fJ_MikAZKLRrMnC2A8nEnJWaU5Y2nzy0wO0hhu60aCUgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=NghGU21JXmJ1Vk2ZsOtp5D3DytDkbgI9LtI4z7XXZ4jAHUNmoog7KJznuCkN7VuNGM3JcTku4OhXF6DsmChqnYvvMlGAXjNuZNR_yq-9rzpLeeoXxNrSiHkqG7n1p2OOyn-SnnGfvYjifBqWRMl1KhyhNJoQ3WSdwGwNFbHJ-1FOS_-3fMykw1RS4K-QTBaP4k0ilCtG-2D0h0w9zXY0v-a7tjwaXStgKInBJ7ORqLW8n6pXbSs5Yc1Gohpqf9qu5z98m-uUnbc9Wd-FnAXanWuSx7xf3A7DwlZS2id8fJ_MikAZKLRrMnC2A8nEnJWaU5Y2nzy0wO0hhu60aCUgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=U8yJjFUb3w_5a_Qdi9mV1-rK_L4W6-mTj9kQgLbgn3IqrdtkQG3qenU7HcWSuos9KQdnq_mGKTXckFsS7D4UsEFAx_bJbsfpfduRRBAkoQ94gU6wKxGviMPADl1Cia0CW1ktuk0MTBeV95yZK2Kqffz0gOGGqWjhjOy55306pakEKg7QdCFacXKw0SQU4ddEWwu6l4Y-JBMVp-mjmRDIlddsqH0pXG2AB1djwtkHhivZ4qJocmQijhuNRYB9PzDefHRCVBlvoyJEX3eA7Mbt8bWOQVl7bULYJAgEAmEnHhherFgze2fPNRuhzH07rr7um54eA-y3gE-ji1NW5UaAaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=U8yJjFUb3w_5a_Qdi9mV1-rK_L4W6-mTj9kQgLbgn3IqrdtkQG3qenU7HcWSuos9KQdnq_mGKTXckFsS7D4UsEFAx_bJbsfpfduRRBAkoQ94gU6wKxGviMPADl1Cia0CW1ktuk0MTBeV95yZK2Kqffz0gOGGqWjhjOy55306pakEKg7QdCFacXKw0SQU4ddEWwu6l4Y-JBMVp-mjmRDIlddsqH0pXG2AB1djwtkHhivZ4qJocmQijhuNRYB9PzDefHRCVBlvoyJEX3eA7Mbt8bWOQVl7bULYJAgEAmEnHhherFgze2fPNRuhzH07rr7um54eA-y3gE-ji1NW5UaAaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=DYcCJc-YPcaCgWMWw2KOjoL4UHA7ozQai9LY3hxzW5Z_h17qv-f00c23fzClVenOiw-QlSJiUgP466I9Ldc7irhmmkH2i7YgHfxRB9v2k4_ztKwC6_RAcs6W7qidX45-yemAdrmRuo4mArU0YHtXdLVmkIJpxNsQEqmq02nVjeOd-N6GaQ3Jt8QlOnipr6-9ecX9OEJr4hTHw0ar9IfntUR87xl8n4uXdMH2Sh5CddwrtIS7EXCPdkBPfyodEEJmPI6_Pie-3unMN9aXsgepgtXxXl8AKqHRcmQ4ivDwk9UPTmJU89KCJ1KRC-wqj4zRtqqwZCn-lBM3MPfpQDAiZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=DYcCJc-YPcaCgWMWw2KOjoL4UHA7ozQai9LY3hxzW5Z_h17qv-f00c23fzClVenOiw-QlSJiUgP466I9Ldc7irhmmkH2i7YgHfxRB9v2k4_ztKwC6_RAcs6W7qidX45-yemAdrmRuo4mArU0YHtXdLVmkIJpxNsQEqmq02nVjeOd-N6GaQ3Jt8QlOnipr6-9ecX9OEJr4hTHw0ar9IfntUR87xl8n4uXdMH2Sh5CddwrtIS7EXCPdkBPfyodEEJmPI6_Pie-3unMN9aXsgepgtXxXl8AKqHRcmQ4ivDwk9UPTmJU89KCJ1KRC-wqj4zRtqqwZCn-lBM3MPfpQDAiZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKt15i51WsMCxwUyM7muXlm-7d763gh6NhYfhVfQhqnQ1ONlJALegyQs8WgwIyPyLl4hn-y7UYTpcxLcPBY_Bd-7piMzvaYyTa3YqwJx2yQ7uDPQIaNgWZ_fFAO4_c_QlFPELgiLO8RWjC5l0wGktzXw9zRlLqOQ6bXDA-vfEBtH8lnaRlO5PQmpy_DpFYKvf_QYiqoszCtTpknyDMY7H67q86PhKUU13TB4qwRT70cFnQ76TdSlVgTzcdSTDWPc_sHJNIGkIihhdsuAoRPlJKwr1hVnbuPA8zUTzJTr_s05iFyXVpV3tq1An2ZMuZX9bRnHQr44-_5MBysykSc9Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5ZBC21G7ZaaWaiy9epdANCavHuTzma6aTJEXZWHFFj57UZ61GGf_p6i5---kKOxFLA3bbgC58_a7cCNDSHocZcxr4bRazc5sz6Yj2NC_hSja-8VfosDuAI2zG5fM0n4G7iLkT5HAyYD2-dNZpS6_mruS5C2H24jvRgSPVpDZuVMqZMDnG52469frXbumoSXXMmPaqJs517m9vpRc2iji99ipWZ0j9Tlg4On5KFZzlsplWGXM0HO8CJ67OgTdlJjs_BBLRJV0DG26PgdE-xLsyDuXZjR7ucAan8vBPrdnRlZHsuXswoBzPaakxebF-sbVGRIml2pI9K20Q5tWp6HFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=tKI64t45_PXF6VxWMHoHPisb27d2y3JY-V5jkGyey6kmPpXYMxjn8GRx7cx2MiHARJ-S9FIB8PihpJbZvLyYew2lOftnwSK42oRsyEZvMY27nyqAT6CRx9S5FNLYBFzqitZL4Ut4h_QAdmLcD5H_UN9WKekt3J3WheYUWoqMlHuRihelpFywS8RuKfbKB903RTXbXHV7LY_wrAkgvowXgxHVctKigdW1Ty-y3ZweDjlF-IA-lRI8cL5rYOTBXchLeu5LjCtySL9IWi7SV2gsECxoKuLFZ2B2fslF_4GAR8pv7ZJNoTFZdwhbPlW-j9ljGZJWnnbBhurdB8m0IA9p1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=tKI64t45_PXF6VxWMHoHPisb27d2y3JY-V5jkGyey6kmPpXYMxjn8GRx7cx2MiHARJ-S9FIB8PihpJbZvLyYew2lOftnwSK42oRsyEZvMY27nyqAT6CRx9S5FNLYBFzqitZL4Ut4h_QAdmLcD5H_UN9WKekt3J3WheYUWoqMlHuRihelpFywS8RuKfbKB903RTXbXHV7LY_wrAkgvowXgxHVctKigdW1Ty-y3ZweDjlF-IA-lRI8cL5rYOTBXchLeu5LjCtySL9IWi7SV2gsECxoKuLFZ2B2fslF_4GAR8pv7ZJNoTFZdwhbPlW-j9ljGZJWnnbBhurdB8m0IA9p1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=vWIklz_rUgQ_cHJoscuPlj1jpMgkCPLLhvFMPPw2PQpRrlxHTflR4V4KGz6cQ1LVcB0-i4ZlsgblXizoyNFh9EHHWmjVko_7u8qUxzTKklZg_VW9bwdGZAjfHMKafniniOU_3iwbalf5_1B30uh2063j84Q7XUVR8XcHVxm97UcgN7igLBOC3R4OncKFkCMabQVTgMDh62sXjJ26ivklS4t8zFlvxEQe78l9FRghxjaF9MPFriTytOKfxcVDBFYsBs3N2rOWBzuOBU0bizp1uRCC9wLMocs92xE1vtjh0jA4HHB3d_7ThuenNBsjDUMkJ4juukISZvI3oPcbOFeUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=vWIklz_rUgQ_cHJoscuPlj1jpMgkCPLLhvFMPPw2PQpRrlxHTflR4V4KGz6cQ1LVcB0-i4ZlsgblXizoyNFh9EHHWmjVko_7u8qUxzTKklZg_VW9bwdGZAjfHMKafniniOU_3iwbalf5_1B30uh2063j84Q7XUVR8XcHVxm97UcgN7igLBOC3R4OncKFkCMabQVTgMDh62sXjJ26ivklS4t8zFlvxEQe78l9FRghxjaF9MPFriTytOKfxcVDBFYsBs3N2rOWBzuOBU0bizp1uRCC9wLMocs92xE1vtjh0jA4HHB3d_7ThuenNBsjDUMkJ4juukISZvI3oPcbOFeUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqRmMy1TIQfTIGfg7BsnFPwA8yumte5HI1o8LFY5Gn6p_yvIuuYx0r_2WKzF_-2Lzl-mSg5Fngyn2T2K-4wHgVcFnoFrJJGFfQexmIb6Z8TEyhKfM73x0uo9nBZCSblhtLsvpAPeIQd-imPCLdY1jDyAuJHmtfoB_f7fXqKX-OplGtfM0mvfNBTvr6n9HHQpvVWfyPPpSMCLFo6MqD8IDzbRYLy0WRBveiqQcfqT1WSGXcbqTKYg5rQjyk5DcPLxl5H2hMrCXn4F2n1z6KPJYXkMyTx8gtYotxk_DrpOM8BYLZpHrwoYqSDMXnAVLMWebCvJG3LyJdaEfpQGk_zHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=Gu7qsdNozKIR7LRQ095PfeCJOoV0nXlfpoAyDforpgKCj1894woodY3-xjibYShQTPyaJ12GmCaUMu-rgPuzFVyovlxwlXlPyjyKHOkrs_vImThNsj4YUk3FuxswzdEoTthuFk1Fhxq7cKSublKqFMri6Ciss-dv9YWttSfLvkCebMFVJKoi6tgQ8dOM1fzg5uWa9p63Z_lb4RwgdiWYPb_yzaCKHfI-VeX0uPDVEgSjWFdVX1Q5CSrGcYEWVk-wG_l_J97a9ccLFMllU32ilJlhV5vYg6fkErB40wMseCvTiXeYkwc63sid6RtXOIpz_lXKlSgXcR96wNqPN5A-Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=Gu7qsdNozKIR7LRQ095PfeCJOoV0nXlfpoAyDforpgKCj1894woodY3-xjibYShQTPyaJ12GmCaUMu-rgPuzFVyovlxwlXlPyjyKHOkrs_vImThNsj4YUk3FuxswzdEoTthuFk1Fhxq7cKSublKqFMri6Ciss-dv9YWttSfLvkCebMFVJKoi6tgQ8dOM1fzg5uWa9p63Z_lb4RwgdiWYPb_yzaCKHfI-VeX0uPDVEgSjWFdVX1Q5CSrGcYEWVk-wG_l_J97a9ccLFMllU32ilJlhV5vYg6fkErB40wMseCvTiXeYkwc63sid6RtXOIpz_lXKlSgXcR96wNqPN5A-Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=OgJV715YVSlyIFpLjl4cKP4vSltWZIFOZn3EMGQZ6q8L9FGWGKVKkPRFkYfxxS4e0NgGl_Z3t1nVclfVdiDguisztPji9XOmjZu8AvzX8Fzmi8rhJn3Om0UdXKQj_VXCxSXEukKI3CYwLhAUK48PXJmWhCyqwJCV52gXAWmrdllq01fDrWFxKybdo-jvtApZD5V2KDS4VKh47bhJl2YTOAvSj7FLH2Dm8L8seol6pyDTlb2kcarDW5ntJC1jzbUGHfkfqioIPnfYmXzYqZbXA_ccWXW1ZMz0gioLWcgO2QTJidMy3u_XZZnxElI9qftV4pqT5Gh0F26j9fOzJ6OokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=OgJV715YVSlyIFpLjl4cKP4vSltWZIFOZn3EMGQZ6q8L9FGWGKVKkPRFkYfxxS4e0NgGl_Z3t1nVclfVdiDguisztPji9XOmjZu8AvzX8Fzmi8rhJn3Om0UdXKQj_VXCxSXEukKI3CYwLhAUK48PXJmWhCyqwJCV52gXAWmrdllq01fDrWFxKybdo-jvtApZD5V2KDS4VKh47bhJl2YTOAvSj7FLH2Dm8L8seol6pyDTlb2kcarDW5ntJC1jzbUGHfkfqioIPnfYmXzYqZbXA_ccWXW1ZMz0gioLWcgO2QTJidMy3u_XZZnxElI9qftV4pqT5Gh0F26j9fOzJ6OokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=PzXUjcPOmNxg57ws2I2bvczF4SmGh_eURZEe-fP8q-bU7GNP1uuDznTyNSgfhZWAvumRPsJNanEAIAqrP89qCIwEoqOJdIxHHlaHVQbtJJWmNhziXpjiVwG7_7bYZtlL2qmZg0p9BEhZfPymF3C5Z8t-gIF_l6N5lLF8At6FynpnZJiA5zbhVn-ScXi-l5B_3ru1VVOQ8LZj5p4rBaxpQAuVn1LCs-YeTr7QSqMyhoUle8o_LFHYXd4OuREERO3EAgERKtsRWU1tyGKUBiVOJ8j-4wXT0UVWvj_ZmPL10N1i11Qu8tAct1qcyr76NOhTZsNEfE2ws9zPKXWO86ZhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=PzXUjcPOmNxg57ws2I2bvczF4SmGh_eURZEe-fP8q-bU7GNP1uuDznTyNSgfhZWAvumRPsJNanEAIAqrP89qCIwEoqOJdIxHHlaHVQbtJJWmNhziXpjiVwG7_7bYZtlL2qmZg0p9BEhZfPymF3C5Z8t-gIF_l6N5lLF8At6FynpnZJiA5zbhVn-ScXi-l5B_3ru1VVOQ8LZj5p4rBaxpQAuVn1LCs-YeTr7QSqMyhoUle8o_LFHYXd4OuREERO3EAgERKtsRWU1tyGKUBiVOJ8j-4wXT0UVWvj_ZmPL10N1i11Qu8tAct1qcyr76NOhTZsNEfE2ws9zPKXWO86ZhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEEluTkaNP4RNJk-7zjqc88DfE8AT6BlL7HPPhdfBIAvyME1Lczzm3tsnhLAI8kt9umY6kwfYnNRv3L7RT71DQ8YE17SnE7KyflDLRhmnGInNOHoCPIwPcNtbEmvxHXllC64FMqCa67HU6ekz-ueosZArr3dxRP-qBqLUyUqnIN7AgK3XioDaM8wOULpVJWzc4GqWwuR8gd4q8SLl8U_WZmxudc6W4q1irZ9-wVaPlo7_P14hDIX8zH4hv_2LuuyBoH_uFisEY3sGyotz6Tn1USjAjK5s2Gb64a1q_qfUXMoGaKcLY3mkzEiUWI1gsxKQhX8xxVpcWkzys8Wuo1kmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdM_TraKgmiLCIl72rEQsH9n2dtc8DRWy-O2_dtM9d7Aq6EmDGWHE43N2eYM1YvJd898HOaPDbvUk-5zveyIFg8m1cYxe3y1-FtheNP6LiW5FqAuOWpAoKJYgjYN2CP5LrHMHRtKzGneLWeeLvXjsEAUsthKAmk3O5QvzMFyd-AzH-RyJnmDB7YgucLqMtd85UB71wJqABBpTsfeW2_-vvMxRyxQH1BcTCOYUzBCc8ZGFeP4VAu_edRYSnMfULPdwSA6o-zS1orLlAoNAw-cc-maAqj2Eyn6lWr6TDyaCr264KkuWIjlSQqo9fi0MOP71m4x2IVpn_U1f_ytCIh9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=rPrk_LOjMRrenm_K6ruI1L7pdxn_8y0-tmNL73kGXcuUXwEWZ2hLPF5Oqvgb0owx0GMOje0VEstaEDLctMIPQ6mfYrq8NBIwKpSlmWYl_Ul4CdNwR2uOqeolkq-3eqlB-JVnvqZrObV8B0KCyzppUpk1ElqDVMokh2meEUm5y309LikuBCGaHmORcHiukIrK7Ea0vWWzYC4Bt2KMgQ8RtB8sDPhJZeYBOb9OVk8YH-xtjKbX3qNAnbh8wy6irbh_ZMPiKf7Gpvc5O4QHZeqXB0xx7PPTOgXDqILKznTZPLVMvI_bApgCaPNLJZsT8hBeqeWirNLkfBFX89ZuAEpQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=rPrk_LOjMRrenm_K6ruI1L7pdxn_8y0-tmNL73kGXcuUXwEWZ2hLPF5Oqvgb0owx0GMOje0VEstaEDLctMIPQ6mfYrq8NBIwKpSlmWYl_Ul4CdNwR2uOqeolkq-3eqlB-JVnvqZrObV8B0KCyzppUpk1ElqDVMokh2meEUm5y309LikuBCGaHmORcHiukIrK7Ea0vWWzYC4Bt2KMgQ8RtB8sDPhJZeYBOb9OVk8YH-xtjKbX3qNAnbh8wy6irbh_ZMPiKf7Gpvc5O4QHZeqXB0xx7PPTOgXDqILKznTZPLVMvI_bApgCaPNLJZsT8hBeqeWirNLkfBFX89ZuAEpQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMEvRwexgHbA_qLz9FGmEoV-0ydW302STW7entiIN7TOqZx1Oe19BukIxTiqlbKvmaDSs7G95X9AIzH1joqrU5gU7CEq3p3G_i5qpM75UiToHPG2e2savnQE2-sHld2A9jGTVoLIvU8SI-MQiBOqS0WoNrvyO1lj-J1oR1TG7xSxgLh_G8levBKzv3Gq35PZ6wzGZFGPtG0klrG_Ir-7mPqHQ4QPRdizlccDm_rTKaZ956RefTCDKrgbSEkvwhBzGI5MzVSq0FSU0MH_NOKD9jcPVBBijyZEQehHwxpwnaVo_ttihghqrl7PPY3m76Kl6wjmZqyTQHomkb1FGLMmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=reAdc1HZSmfnd8XxPAdXTtHfnwfeJLzFxQhh7IgwSqDBTTfwguCQVuWRXDzih_n_ICCQ0holoBSzueoOFhLKS3Dapq1jdJ2CiwtVE7DJ0x2Vr5QWd3h30HdDw5ji33Q_zX5LkXFVHd85fvyTKHwOexj-A2Cul-mJwZrGUfIbJSlpTzRvGrAXTMHeqYYsgcwQLI1UubKE60Ci83Ozvse2pOyoO1AQ1bUBX-BnuRZqyn7bBi1diPeQLwQ9Mb5qd3yM4bcjPLkzDD7aDNjiZMKdEtrpu-kqpZl3_yCf9fCHDxR_ImF3w5Nv8wy0db9NaxhUH0xLckZIwbICddjwSNmJow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=reAdc1HZSmfnd8XxPAdXTtHfnwfeJLzFxQhh7IgwSqDBTTfwguCQVuWRXDzih_n_ICCQ0holoBSzueoOFhLKS3Dapq1jdJ2CiwtVE7DJ0x2Vr5QWd3h30HdDw5ji33Q_zX5LkXFVHd85fvyTKHwOexj-A2Cul-mJwZrGUfIbJSlpTzRvGrAXTMHeqYYsgcwQLI1UubKE60Ci83Ozvse2pOyoO1AQ1bUBX-BnuRZqyn7bBi1diPeQLwQ9Mb5qd3yM4bcjPLkzDD7aDNjiZMKdEtrpu-kqpZl3_yCf9fCHDxR_ImF3w5Nv8wy0db9NaxhUH0xLckZIwbICddjwSNmJow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWpOn0gO6RF00lQSyHwhm4nfFnISv2DDKFJKgZfrQ2bQtOy7pacMw8OIMLG6ABU1uF-IsYBsynCbFe99jyY09OJu7h71BY4os-4bD78jmnURgiZwYzcuYhWGx2E24sAgQX53lWefmWCC4E2ap3h8RgdnyrEex7fo1F6AGwe15pNkwhPMMYP58Wu28TyfNM_6fny08epX8BKzRho5u_J2R3f8kqz3E30HjpESM993aqLIHj6cOsULE2g1zhhQ7XEGrC36S6hQHMqgDYSwmZesT0Ux6EpBdbuiysE7LK9afSVS1zHfpa33PLapLPTtCAn88rAXtp6bu58226XCKBellg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
