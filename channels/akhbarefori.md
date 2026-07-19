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
<img src="https://cdn4.telesco.pe/file/RRTaupuqDauoWbi9cfF3SbNaVVYm6TlIOdDsjHS4YI-ONRs3ioEeO4ZAisRTHCMpM-JUZ-RClLNoqXFjNF2dGWXjpNc3KTaKBRFSfWggJFlfrgRy6dM81fbfcfeZXrs4PzKQC9qpJx5nF7Tlm8pKXBfW-wttNP_x8hSUcc9-QLxP9YQWT9i8Q7A0tVmXGhoZE1w67xDKGEA498wGbQ7jzHQ-Wr2lL2p3H7yQNk2wj4RRJrXUrVs6h-bR2zA8s7PHZHLP4GFz1LpzMmDNorTU9LsInhWSSsCwpElx-Sq56kZUe3yVie2fpcmKqlU4-jiXGpM2TpBC6Npmq5_RP51_TA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 22:23:10</div>
<hr>

<div class="tg-post" id="msg-673124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fabc038fb.mp4?token=lLWfDGouS1xHyhnX8lAHy6Mm1QH-ZQqODZ0L_hevVPKROe933Nd1EhEVuOiwa4OlGt5C34DER67QhstlOPjZL4hmyM-QgMPUlgjVRZKqbqOsf_4AYf-gpPGO9GEGc7R8pVBuLzOX0xiVHW0Vb5ipELDMxR5Fy7jPVgjfzK_LXtVL4CcvCz2J9IQg-_P-ptqZo5lXuJbOS1Q2ySRXLjUpvEQ_Fb9mmvAkdWqJWZ_S9vl-pshWIfTZiPXpQHsgNyAkryhvxwPzLaY1diBw7-0X44G_VLRkyWniksVDQSke-dZRngzIIlLXRnI_n9vgY3QfVLGOa89EiaDCj1LoYO7mOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو و ترامپ در ورزشگاه مت لایف ورزشگاه محل برگزاری فینال جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/673124" target="_blank">📅 22:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعاها درباره توافق بر سر خروج کامل نظامیان صهیونیست از جنوب لبنان
🔹
روزنامه «معاریو» به نقل از یک منبع لبنانی مدعی شد ژوزف عون رئیس‌جمهور لبنان و روبیو وزیر خارجه آمریکا، به توافقی درباره خروج کامل نظامیان صهیونیست از جنوب لبنان دست یافته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/akhbarefori/673123" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673122">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9ad63557.mp4?token=Xm3XzzaC6N9-ZxzRDt90vhdLPnD2cZVxhEHdGvO99c3NwAXURdZYpko9AXJNM60I8GDDO5KMbr6dCpvuEGEQoNN9e9QgmH5YH9bHEgC-wgIT2ui1YbplpmndbgzeWDFtaEZWzLlA9D_b3Z2KY9pPk_mm-tu9Nvz2sL7fWTXescroAQnZuU2wJOdNV0wHICPvQ7yOBT53-fZeBqBPmJQyUrG5pWoi2NF9zEaq09poeb_HDMwa79q8tLQPqO-ZR62tO6JQ2cOtOWdbOopU2-ByiBPScx-qmbIFj0sc6qS5tbK4gvPZQUUs66q31l90VcagTqxGnoeMc390EcJG6zGbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از لحظات برگزاری مراسم اختتامیه جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/673122" target="_blank">📅 22:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRUPfbkBciu3U_kPkb9QQeULg6Ne3K0HfurT0eCtrluT4GqGQsSfwUJqXm9B-Oy4YjliA8sLOwxTTwAyVhN0sSE2uN9gr8DNQJCpv3xR-S3MDM9ScijLtIzWiNlnewvSiP5nMXVwljRt-5JHsJ_AJWmRxvPD3IrqzATekFMrzydHN4yLbDXGT-izdRXS_bxKq_JxBpScSHLfaX3rKice9x9wVuZNlUy3BVgnVoveV5I15dv0RWU50AUvPwLOQqpCQ5PO8ofEXlR5lcxvv-R3RHBJFMIzFMAWPVb-VWs13m5phVGhdmzfhr9C2OgHcJNHuh0mimvPA26dcCS2vpmF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyY0YZOW0KCI4qTb93bQRK5x_WcczQVMhHAG7ISETs60PQAsW_pBC146cleNEqU_7lYLHDmsLK6mQ_XYgSkuhcE7ivA2WzjiUfg5EXhbq0gq8A7t3yBgankpVBQfP1sv-XyFFLA9Qs0eadJn4Nj5pjg2RQKfw202AcR65JMb8qLyOgnjkRh7io3cE-vyxDf1Mtjw0k4bmLgR8O8IhtEIw-znJ9a9nIHramSV9VxZQbhpRQue5Kd7hcpp1KIgO2hykYEGD3TfzfpTvnx_rgR8zaihC2O7zOd0dVijcJvxxNGcmt4sKDgQM5V8t56VrA7JIIGOZolaF2uoD8sWQHhJjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پادشاه، ملکه و نخست‌وزیر اسپانیا تماشاگران ویژه فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/673119" target="_blank">📅 22:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای
کانال ۱۳ اسرائیل: قطر طرح جدیدی برای کاهش تنش میان ایران و آمریکا ارائه کرد
کانال ۱۳ اسرائیل:
🔹
برای نخستین بار گزارش شده است که قطر پیشنهاد جدیدی برای کاهش تنش‌ها میان ایران و آمریکا ارائه کرده است. بر اساس این طرح آمریکا حملات خود را متوقف می‌کند، در مقابل، ایران متعهد می‌شود به مدت ۱۰ روز دو مسیر کشتیرانی در تنگه هرمز را باز کند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/673114" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9016aa38ae.mp4?token=CbQIn9hVSjETcAQ0HoK9xiYk6n3o3naSuGayt9WlIM__FopLd_iJuFS-ofhm4foP90rxqorM1TA0H4M-kKcXqcR8Sgt9KHwUUc61sdo8sg9db8QRRKETnvMjl15Ot7GS5hjzFQS8hm3RpLBkZ4N5eQi0zlsv0uJSOWvyIUs4CFe5Hcx43M4XVxruWQdOC2NZKfImB9oW2BKgGkb09AXM7HvFkio69a6FiQhhyMe1pZjKS6BblyQq8QICVk36uo5OUpoF7utVK5PQx_XNk4PIv_fgQrQDyIxPtRxfI_L6Y8pmeh0MD8qNuPE7qHbTxWREpVf3G_kS5jKYy1Pe2USZcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرج‌و‌مرج در ورودی ورزشگاه مت‌لایف
🔹
مشکلات فنی در گیت‌های گردان، بررسی‌های امنیتی اضافی و دستورالعمل‌های نادرست از سوی مسئولین برگزاری، باعث ایجاد صف‌های طولانی قبل از رویارویی اسپانیا با آرژانتین شده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/673113" target="_blank">📅 22:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خوک هار کشته شدن نظامیان آمریکایی در جنگ با ایران را توجیه کرد
ترامپ در  مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از جنگ با ایران:
🔹
آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
🔹
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/673112" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673109">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3uMfjqX7fPlxzurlzcqSwigX_p5JCMu2IB0KEmpN650S7dlp3GOQsd7Sc4uPkX7e0G2pyxiA3keMnfiUpj8qhbe_xqyqXIhhxWRW0avN9wIRO6YVCKzRe6Fbdr8jA-QYMQi-T7v6vAEYSgUhTcHWaAfzUJQSZ_jvwRgE0vrmz0HC4JMR_1ITr3siNmvPBz6AcD4w00ub54vRRxlA_25fQHtDXxw2wcEVeIYAmMV-E2EFL_5GmnZlArqWujYX2Haj1L3ZOlz-ai_KBrjYef7A3_6b93SJ0pgjOPS2eQSXVNHHOs_yC0S01njhz1tlXqRY-8IBgiLKg-d1QjLusrwVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pAGD7isIp7lqEumz1fXQ5LKbL278VSfOlxP-GXLDnefp8CV7jybiiUn7P_z6LkJLzVXCz9c7Hp3whLGsW57Nl4zdTtMbso3A50m571vYKSuRcDWEl1RDfWufPLe51DgQyUjJSy2-KaRNpmdHJ8_Kx76w5ECHf9lfAlQGbML0LBD0r6LZu2TJAiGheqMZKuC9oEaSfHQmwNRMx8ESqmp3KlB956li6zJ3RQl1rE2rLgaE9GDSnt9vLjNiekKr6XrOfIKvTXyJuTDeegIeUtHb3FEVjyhIkeG3Mpzaa5FaPB7ZrRxref0UtRtqr5-FIKy4-dgFnixBL0Z-8apz7GOjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4pVf_YLfq5ibfqjpzj4Dy-dyD1Q0_nUxsp2oHFUX1C77rMtEzFovxpioCH3yUsC3KZ0Ad6wdJLEY68Zsdn-FTPqX_THG3XNeblk0mPESG9dw7SJb4bmCJYzw4Oe29VId2ZpcSmLgFTY_8QPfqdTeHk-QbthXAdr4c6g49qGiJxSJZBL9n01ceptYXHDlO-8X0HOx-fawuiN037DZBij9Am_EKUwGnxu-kLO-_nGIMFOy60u8IkBcG0dTAV_443QSCum7IFlHinWDtYfmWa8_fu8kAQUOpCXGWEaCKCqq0SndWS3Xm4sMh3sBOzT_zx8uYec0F0CQBXm_uYz3Ta7Vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هواداران پرشور اسپانیا در آستانه بازی فینال
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/673109" target="_blank">📅 22:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673108">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سخنگوی وزارت آموزش و پرورش: سال تحصیلی آینده در تمام مقاطع تحصیلی به صورت حضوری برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/673108" target="_blank">📅 22:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_dTeP6M3_aell4o47EkTND7YasZOcRC1n8b-PLnxAmeQ-I03W8qHwGdQcppBMwEyxPqeCZmBwxTZGrOtHErvZ-e8Ep9nQUe_j89KzxrjU3AewA4Jd8nNyDurtix9K_0FhdqVShazd6Iy8l4G0M5Ez0qGT1xCfW_4eWgFcMgKjvFGIlOX2I_Dh6kL5WlZszzCqgNRfYbhcf7kxI-X6VbGsELdYmvbSx91H33dcl4JHhs3TnDYTmSNfKdLRy2NVJwob9dsQH12zYIkJMDHgWrP6y9XoqRAgmTBA2gJeQBPRd7DuVuGymbyvKT0Hq2gXGH_FQ16asekUPKHq8v9CJnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIoB_y2zbkzjBCFLL3bPLPeO8FDpaTfnZ8cQfWGEwl2EP9YMUAgB68RVtdIYfFmLdOe3toF7mGzrowuEp8JbVmvYDVNpfbpUKUbF-V_9LStLtwBmuHoflrIVou4-64aF-3oMNxqXgtvmsxxK0QKFRn6q7IDdFBtM7zzJHvrnzoSvWVrqF0AnKMoWaqT6EoBXGGNpub0lCb5XpybfwADx9C5UGxHPyfxTCpjyvqXyb3sFSSOr9vJmGd8xt4GEvw6ctfTrpgjjnLDK0U3ivX6Bt5M015BDpLHJXX_EYaiF3qhW5fo2Fmw_0l7vpG0-rimM-gRkwDuLFDK989gLqDRgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaYbk28v19fk2sX9pemzUYiFtoq3zjd1YxcSB7QDIaCahKZdxYE65v_rP_z4HN-wrH5s7jzO0Y4C8OiZWoGvrEP1cJGJaHMaav2RTFAd8khjQhZtQg9xLIETYXYxEdRgoaBTxC5yYorAXCURDlJFh-iWG_4gtdw3Fp6yQi3oD_pAYhimyy_9TUuiNWT7fiNZYVwXBdYgsnoS9sU4hs_PywDYMC39-25DL9bHHqn3RvCRqALF_3CNSAGJvIA9hMVyb3YmnP3sZ0CN8pzCv1fsUkLCqHolaQa8UDhdgpxUs90Z2-hNFyNi7GDHF5j61JHeD--Ht0Ue9DnVrWCGTsOFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z13fJItjMqUF3O0Fav2uXz1HKJP8PhW4CX8Mlv7LzsccmGcjuiu-O1gEHSwVyU_-F5qbW7CqwKx4i3GY3cyosAHBkGHpRNd20cuPB3_oAic4eyyeMm5ww2zuPGAJkH93SYivlI2Ukq9DkxXsD6QaehUbpEGjcgCYTOTYUGwWZM0ZZTQG2k49ENvIvgNVdSUPc6gL3Igq69cijL_5n9H4Pq7BPRG1OLXUQk8tH-VK_tqWek3Nvw3_5Kk_KrWp5LPQIZkZTiZKNdS3UONleSUqeA2eA9TZz2sdB5wYcac4Og43ngTo8MJb8eQPnsy2JvMAUt99D11eUT3sF9hNbnJTzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از مراسم فینال جام‌جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/673104" target="_blank">📅 22:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee935b79a7.mp4?token=s8VSl6JAZ_LJw3dZgpL4I-Z6-W3jmoZwtQi1dW8GxBIpBevAEEs6_WEYW3KbcTJWDpvcR2NCoJU-S0KUt5HZeQ5iAErozwJmBaqbiY8GchAUZ3yuzSXHwGyoefXAhOtKpc3g_ebmxOke18gqMOw8xSVr3P2q8cVCNuQIjJkFvQ47qdbYKStWxRlg-br-RfVnA2arZRdXsB2sp-3uyRrBhawGCve_fj2bSP-pAOL9PLjw4WWjwbV078aqOhg_rd1ku_lgFlvKy5-G87cNI3GONjQSt0JyekqquuxBwZNt4KUDgclrZRkYdBEb8U7-b5XXrbjidGcOvImSUYamf7ij5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee935b79a7.mp4?token=s8VSl6JAZ_LJw3dZgpL4I-Z6-W3jmoZwtQi1dW8GxBIpBevAEEs6_WEYW3KbcTJWDpvcR2NCoJU-S0KUt5HZeQ5iAErozwJmBaqbiY8GchAUZ3yuzSXHwGyoefXAhOtKpc3g_ebmxOke18gqMOw8xSVr3P2q8cVCNuQIjJkFvQ47qdbYKStWxRlg-br-RfVnA2arZRdXsB2sp-3uyRrBhawGCve_fj2bSP-pAOL9PLjw4WWjwbV078aqOhg_rd1ku_lgFlvKy5-G87cNI3GONjQSt0JyekqquuxBwZNt4KUDgclrZRkYdBEb8U7-b5XXrbjidGcOvImSUYamf7ij5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین لیگ حرفه‌ای مبارزه ربات‌های انسان‌نما راه‌اندازی شد
🔹
شرکت
EngineAI
لیگ تجاری مبارزه تن‌به‌تن ربات‌ها با نام
URKL
را در شنژن چین برگزار می‌کند. در این رقابت‌ها، ۱۶ تیم با ربات استاندارد
T۸
٠٠ به میدان می‌روند.
🏆
جایزه قهرمان: کمربند طلای ۱۰ کیلویی به ارزش
۱.۴۴ میلیون دلار
؛ معادل حدود
۲۸۰ میلیارد تومان
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/673103" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وقوع انفجار در اربیل عراق
🔹
هنوز جزئیات بیشتری درباره علت انفجار یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/673102" target="_blank">📅 21:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c64c854.mp4?token=I2E1gd9jTUJ77oaPf97JNUlhlcTMewGWwHIPmqnQCaX4CwjyPWdz3ekxx7Let_en9KcIEp9GgJyMsKwxFNJEEOn1ib7GK1rYNbaTJsKR4b7x9DnOSR92VM64-yknBi72aOHXdwy3tfjP7qU0MNEbpxki7cHS2j_GHQb7WoWNjLg--hCUL9gYTQ2XkFQvt645psQdjjRDf2R5BQxAkyMKUYP-p3l-WzEL3TKSr-qeOTtpNJa85YMbdAYcAd3BwtkJswiK5nhvEG1tFY18GN8NgXWx6IOrwP41hLv6kd2yS5luv4CBKPmO4oTq0S-PX-7y7WmGR4A1ytYxVuy82xmH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c64c854.mp4?token=I2E1gd9jTUJ77oaPf97JNUlhlcTMewGWwHIPmqnQCaX4CwjyPWdz3ekxx7Let_en9KcIEp9GgJyMsKwxFNJEEOn1ib7GK1rYNbaTJsKR4b7x9DnOSR92VM64-yknBi72aOHXdwy3tfjP7qU0MNEbpxki7cHS2j_GHQb7WoWNjLg--hCUL9gYTQ2XkFQvt645psQdjjRDf2R5BQxAkyMKUYP-p3l-WzEL3TKSr-qeOTtpNJa85YMbdAYcAd3BwtkJswiK5nhvEG1tFY18GN8NgXWx6IOrwP41hLv6kd2yS5luv4CBKPmO4oTq0S-PX-7y7WmGR4A1ytYxVuy82xmH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف طویل و بسیار شلوغ ورودی خبرنگاران به ورزشگاه مت‌لایف
🔹
به‌دلیل مشکلات در گیت‌ ورودی و بازرسی‌های طولانی، هواداران ساعت‌ها پشت در قرار گرفته‌اند!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/673098" target="_blank">📅 21:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbQNbxWcxVcMRb7We_S9tvWIAFqZ64dOCON6zV-ApY3hLsRq0znTgTnvsammV4HsvorwuJxkjrEJ3WLSm6PaPG7rGp3SEUjjOmVyGzsPyEBWMv7j2dsXRNiyjKKloe3SounhRhAm8C1DzUNSjGwAjlNkZFTtrDjqyDmaSDosuB-2aFt9IOOHD4MxEPCBVR3S0r-gdLIgWgL6bvX3z9XWJllskBWXmPNHXPC4aUeXY1HnQHS1m_m597021nOuJcZ5YWrNbT_6byqdiM-soCPFXpPuNEd_RjVTQDENGRcgLwx0Sx99Qtu-w45Dh4kwJhzhO11jXQbRkFqYNEb1fEU_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامۀ «طبیب» شبکه سه امروز از بیمارستان شهید بقایی اهواز روی آنتن رفت؛ بیمارستانی که طی روزهای گذشته هدف حملات موشکی آمریکا قرار گرفته بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/673097" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673096">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZDuwDzw_OShMyc2rXGWyJ4Tz32sr_Wl_Oqe1m7_7Kmpr_LkU9JyeswXMVONik91tD62KR4b0TMoMSi7B2jCIbJi2yoOP_Zj5nx-jhHdnGSqEgYSm6NFWbmN0WFRhXHDt-OJmdsN8pf-bKKuIRiA9j1u9v3-GTTxQdyA-78SCwwuPsP0oK6Gw9VLKyxt031Z7sF0AxjbKzkhPGiINgdF2iTF7EQH7r26iMjHjXag8KrlN9fFhPjme1KtaQyRJrQ1gpi4U0AN2zxUS4Cg4OdbLbk3IOrS0UnUWaLldzeENFwThSrQxOfd3_TlmW5Qzz9XuZXnb81jsNFG4f3-8DAXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این منطقه مهم سرنوشت جنگ را تعیین می کند/ ترامپ به سیریک حمله می کند؟
🔹
باتوجه به اهمیت فوق‌العاده سیریک برای ایران، این منطقه به یک هدف کلیدی برای آمریکا تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3231574</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/673096" target="_blank">📅 21:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51ee89650.mp4?token=lAKY_TDskDUqIALmxC_USjdMKDX7439PnqZj6FKs8mHC2YJlDcx1Ek7Ga3UAZhyuYtcFw_VuyyWwCAtBvC8FI7kE-1uY3KeH13FE7PxaWdoAbFZKNzUlDj2Wi2qTXn6AkfDIKa9GC9Vu1dlGaoLUoWTTjn-tpdtAcTtpPY4hRm6nCZJg83YVBkVxJtwgpVDfvh5F-GRzs9GLpJpOXhdh4QGuFyQBoEXrVWziVJaZlW5FXEZzAaDAnJKsy75V9pnSViUITMQ8JrUpAFDsx8V4ByMk4748T-sp8R2HlW5A8rIOd5e38Qb2BSDiAahmg7yca6Jk9xFX1XyScWt5vc9LHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51ee89650.mp4?token=lAKY_TDskDUqIALmxC_USjdMKDX7439PnqZj6FKs8mHC2YJlDcx1Ek7Ga3UAZhyuYtcFw_VuyyWwCAtBvC8FI7kE-1uY3KeH13FE7PxaWdoAbFZKNzUlDj2Wi2qTXn6AkfDIKa9GC9Vu1dlGaoLUoWTTjn-tpdtAcTtpPY4hRm6nCZJg83YVBkVxJtwgpVDfvh5F-GRzs9GLpJpOXhdh4QGuFyQBoEXrVWziVJaZlW5FXEZzAaDAnJKsy75V9pnSViUITMQ8JrUpAFDsx8V4ByMk4748T-sp8R2HlW5A8rIOd5e38Qb2BSDiAahmg7yca6Jk9xFX1XyScWt5vc9LHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: تعمیرات آب‌شیرین‌کن بونجی جاسک انجام شده و در حال حاضر مشکلی در تامین آب وجود ندارد و شرایط به حالت اولیه بازگشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/673094" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
انفجارهای مهیب در کویت رخ داد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/673093" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=X-uAnloxuMS6f2Rr8jeQgI6ASnTWUKWorrg8SRHYQPmzgTkSlFTkjCCuL5j6n5VtVthkoldRFxDEJTr3XioMEct2UKANlKfMmJJH5d1T79ApQTtu7Rd3cWjSzYgXs64D3ld4RBzu53Qt3pE_bc7udDw-iFXrxKuT3Ee_I3ETovZy02GLazMWJ6ChVo8BcEezb65hdGTiCkFxKsb7og2Ll6P9SdDMwrXlbbjchVo0Xa6V9MJ56c811UqMJ2KJGKXM9YzFXZYz2XS2mSYunxjR4vhFRc7cQtfjQkOxRTy5eKngF7_nrnGaRY3NwMeN3Fes23rvTc2Wkd4M9re_fLL0WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d17ba9cbb.mp4?token=X-uAnloxuMS6f2Rr8jeQgI6ASnTWUKWorrg8SRHYQPmzgTkSlFTkjCCuL5j6n5VtVthkoldRFxDEJTr3XioMEct2UKANlKfMmJJH5d1T79ApQTtu7Rd3cWjSzYgXs64D3ld4RBzu53Qt3pE_bc7udDw-iFXrxKuT3Ee_I3ETovZy02GLazMWJ6ChVo8BcEezb65hdGTiCkFxKsb7og2Ll6P9SdDMwrXlbbjchVo0Xa6V9MJ56c811UqMJ2KJGKXM9YzFXZYz2XS2mSYunxjR4vhFRc7cQtfjQkOxRTy5eKngF7_nrnGaRY3NwMeN3Fes23rvTc2Wkd4M9re_fLL0WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی متفاوت از طواف پیکر امام شهید بر گرد ضریح حضرت عباس(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/673092" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJtxfjZHlxF-b9TYLcqTIyeooF-n6u59az4AloT70OlPKFnd5oBKUuVb30Icsh6K_adHcsJw2_OqKcI5bgy10NREkez3D3tCOL00BZtUtsqeRubnZTAnoFG1VJY_OyewUMjukI2a6r_nBXmJx9BoBObcQueYM20QEP0Kb-ENNFK3PYi8CDdeEIO1uv004zti-otTKQwyRmvbPPDaahJPpGoAU5hx4i5bW-q-6071_t27EXxD8ARnodyzq2zPtmq4uw18S3-L26rMzo-5mtFQE737ZCbek0S5SFgfIvX6x23okqfDWtUwfRQb8KCNRV-QTD4mwB990tNeq1aqU-KDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖️
موتورسیکلت کی‌وِی K249N
موتورسیکلتی که لذت یک سواری هیجان‌انگیز را به شما هدیه می‌دهد.
🔹
249 سی‌سی
🔹
چهار زمانه، چهار سوپاپ
🔗
برای مشاهده قیمت و سایر مشخصات فنی، روی لینک زیر کلیک نمائید:
https://l.nikrun.com/tjy
🏍️</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/673091" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG9TQjBQBAFyow2o0zeLlKorAXM3UN_1agzZLE-qHXomysx9fGLPfi4JKUj1Eq2biVvGYNHwRXR43phYMdc78xYrAVg7pFwgmmTb4aVhuWoGb6dOktWPLVcFrB9Jp0V_v7gJrTawGHHfaKtfo7WoL7sNTEHz352-uf_Qc81LdlWIE4HhKsKeTz89Z0IqfPr070N2z2HP3e1Vu_jRsr3vCpnCLSxPijX1S0u4urGxYctWuN1HfFJmHFDK1YCK1jctsDbY_hF9sgT5dcUhdNTu77HnZBhoenp--fgkbP5CBGdVR1UkuHTgxNseTLOlPvKMQWcYqVIxhsqAnAym4L5GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت از 4 هزار خانواده آسیب‌دیده جنگ رمضان با همراهی تاپ
به گزارش روابط عمومی تجارت الکترونیک پارسیان(تاپ)، مصطفی زینالی، مدیر توسعه پذیرندگان تجاری ، از نقش‌آفرینی کلیدی زیرساخت‌های فنی این شرکت در اجرای پروژه بزرگ و هوشمند حمایت از خانواده‌های آسیب‌دیده در جنگ رمضان در سطح ملی خبر داد.
در همین راستا و در قالب پروژه «کیف پول برکت»، بالغ بر 4 هزار خانواده آسیب‌دیده در جنگ رمضان، از طریق شرکت تجارت الکترونیک پارسیان و اپلیکیشن تاپ از تسهیلات بلاعوض خرید لوازم خانگی برخوردار شده‌اند.
این طرح ملی با همکاری بنیاد برکت ستاد اجرایی فرمان حضرت امام (ره)، تاکنون در مجموع 350 میلیارد تومان منابع از طریق کیف پول اپلیکیشن تاپ به هم‌وطنان آسیب‌دیده اختصاص داده است.
مشروح خبر در سایت :
👇
@akhbarefori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/673090" target="_blank">📅 21:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انفجارهای مهیب در کویت رخ داد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/673089" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
قطر دست به کار شد/ ترکیه: امیدواریم در روزهای آینده خبرهای خوبی دریافت کنیم
وزیر خارجه ترکیه در گفتگو با تلویزیون قطر:
🔹
خوشحالم که می‌بینم قطر بار دیگر تلاش می‌کند تا با استفاده از تمام روش‌های سازنده و تمام کانال‌های موجود، هر کاری از دستش برمی‌آید برای حل بحران جنگ ایران و آمریکا انجام دهد.
🔹
امیدوارم در روزهای آینده خبرهای خوبی دریافت کنیم. ترکیه نیز در این مورد با قطر هماهنگی نزدیکی دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/673088" target="_blank">📅 21:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
صدور اعلان قرمز اینترپل برای سران گروهک‌های تروریستی
🔹
دادستان کرمانشاه از صدور اعلان قرمز اینترپل و درخواست استرداد برای شماری از سران گروهک‌های پژاک، دموکرات، کومله و پاک خبر داد.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/673087" target="_blank">📅 21:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ekxq14PSwivi2pXvji4t40PczBOV0WU9syTvFPfoC5bMcg2DBTUxNAUh-fBz79PcyrCBaUYnujkb2KZQ7CSVMho_a1nbPzLnG0OG8rma9SLWHPURjM16VqwXkMdWdO38bwXJU3obWGnQyEGFVYQzpHOhnYGYPrPbs9Z5OoRuYaCqkDt2JIYkb6Ye7QZhcxWB-tabLOmv4j4qhfgLOJobK7QtiRnMtq-j4e76v6CAEVCuMRTEan8lS2gAwZUGAF9awUhXIx-Z7M7R1IMXxv95ZeDTRTHvOOI8l_TK-XWPBjJx4240e5KOpiKlUAunV5ssN2ejjCLEhc649Wvp6o4wYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریس مارتین در کنار بیژن مرتضوی، درحال تمرین برای مراسم بین دو نیمه فینال جام جهانی
🔹
ظاهراً فوتبال فقط برای بقیه نباید سیاسی باشد؛ وقتی پای آمریکای تروریست در میان است، سیاست از زمین بازی هم بیرون نمی‌رود.  #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/673086" target="_blank">📅 21:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673085">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نیروهای مسلح یمن فردا بیانیه مهم صادر می‌کنند
🔹
نیروهای مسلح یمن با انتشار اطلاعیه‌ای اعلام کردند که فردا در یک بیانیه رسمی، مواضع مهمی را مطرح خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/673085" target="_blank">📅 21:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673084">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای وزارت خارجۀ کویت: ایران امروز صبح بازهم یک ایستگاه تولید برق و آب‌شیرین‌کن ما را هدف قرار داد؛ ما این حمله را محکوم می‌کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/673084" target="_blank">📅 21:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673083">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
استانداری خوزستان:  دقایقی پیش یکی از مناطق خارج از محدوده ی شهر و حاشیه‌ی شهرستان آبادان و توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت؛ این حمله تلفات جانی در پی نداشته است
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/673083" target="_blank">📅 21:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673082">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا: ترامپ خواهان حل‌وفصل مسالمت‌آمیز پرونده ایران است
کریس‌رایت در گفتگو با فاکس‌نیوز:
🔹
ترامپ ترجیح می‌دهد موضوع ایران از طریق یک توافق صلح‌آمیز به سرانجام برسد، اما تحقق این هدف مستلزم همکاری هر دو طرف است.
🔹
اگر ایران برای چنین توافقی آمادگی داشته باشد، این پرونده به‌صورت مسالمت‌آمیز پایان خواهد یافت. در غیر این صورت، آمریکا بدون همکاری ایران نیز به تضمین تداوم عبور و مرور دریایی از تنگه هرمز ادامه خواهد داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/673082" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94260296af.mp4?token=SUDGkkePE2HQJj6a1fjl-0U3ejSnWVSvsgeo_NzuxK-mXOgHSpoKaTDGJIpuceZr6-2ZvUgg_q0WbyKy93vK2BdavVcJ8VkLYYt-tHP0P5wEuvwk9mO40AqxFYCZlGEsNhCDE2Y8RmvB4OBt8Wk5HCeN4ZjA9Du5t0svqVwoahkMQSuwO93tXUHVEG3aHYWf1FViFExTptikvIVB3hKKwY_Z9x9oqVYYBfBp3T3ZdnqnPHzadAZbxXz9JLQYTryi8OkO4G-2bg7UQxNbG23NuYD9CKPcwk_SncjHf3mwuGKgu4Jv62DTX9y2mOdDFZJCcsKAhNgMaXMBY95jA9ZaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94260296af.mp4?token=SUDGkkePE2HQJj6a1fjl-0U3ejSnWVSvsgeo_NzuxK-mXOgHSpoKaTDGJIpuceZr6-2ZvUgg_q0WbyKy93vK2BdavVcJ8VkLYYt-tHP0P5wEuvwk9mO40AqxFYCZlGEsNhCDE2Y8RmvB4OBt8Wk5HCeN4ZjA9Du5t0svqVwoahkMQSuwO93tXUHVEG3aHYWf1FViFExTptikvIVB3hKKwY_Z9x9oqVYYBfBp3T3ZdnqnPHzadAZbxXz9JLQYTryi8OkO4G-2bg7UQxNbG23NuYD9CKPcwk_SncjHf3mwuGKgu4Jv62DTX9y2mOdDFZJCcsKAhNgMaXMBY95jA9ZaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: ناخدا خورشید (۱۳۶۵)
🔹
ژانر: درام، ماجراجویی، جنایی
🔹
خلاصه: اگر می‌خواهید یکی از ماندگارترین آثار تاریخ سینمای ایران را ببینید، «ناخدا خورشید» را از دست ندهید. شاهکار ناصر تقوایی، داستان ناخدایی شریف را روایت می‌کند که در تنگنای فقر و بی‌عدالتی،…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/673081" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پاشنه آشیل اختلالات بانکی مشخص شد
رامیار قنبری، رئیس انجمن شرکت‌های پرداخت الکترونیک، در
#گفتگو
با خبرفوری:
🔹
معماری متمرکز سیستم بانکی در بروز اختلالات بانکی مانند پاشنه آشیل عمل می‌کند.  هر اختلال کوچکی در یک لایه، به صورت آبشاری کل سرویس‌های مالی کشور را زمین‌گیر می‌کند. در اختلالات اخیر، قطع موقت خدمات اقدامی ناگزیر در پدافند سایبری بود.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/673080" target="_blank">📅 21:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89423ce178.mp4?token=l6kc2urfuOPEYm0p2OHrL8vGpntvd0AJoEaF2OV_dokKFrc39-IPL7T0mAcbxsOpGiFzvrYZGfvlnP83_pqwLHjDNT0BKRMztWXAeKVUlxAEXORPx4HRqKUr89RBoTg2zQ0aF5jS6JiFIkdhQqICIExCCv5iY9fffwKzuugcpmSA1yte5xWW00C-hLtggP5--pirVKd6fJHt_5NNbFKWNcg61LLsA7FlXUbPC2Trt54yAEm61DU0RR6K4LjPaW97-9ksU8NVwS3p5-UvplBF8ZzjW8li2fr8-FybqqqPjasyQoOWsAGr1xVfmuJWjbeYDZgjDIdDpkbtHQFctaY-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89423ce178.mp4?token=l6kc2urfuOPEYm0p2OHrL8vGpntvd0AJoEaF2OV_dokKFrc39-IPL7T0mAcbxsOpGiFzvrYZGfvlnP83_pqwLHjDNT0BKRMztWXAeKVUlxAEXORPx4HRqKUr89RBoTg2zQ0aF5jS6JiFIkdhQqICIExCCv5iY9fffwKzuugcpmSA1yte5xWW00C-hLtggP5--pirVKd6fJHt_5NNbFKWNcg61LLsA7FlXUbPC2Trt54yAEm61DU0RR6K4LjPaW97-9ksU8NVwS3p5-UvplBF8ZzjW8li2fr8-FybqqqPjasyQoOWsAGr1xVfmuJWjbeYDZgjDIdDpkbtHQFctaY-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه قلعه‌نویی به استایل علی دایی
سرمربی تیم‌ملی:
🔹
اگر او ساعت و لباس برند می‌پوشد ایرادی ندارد، اما اگر من زنجیر طلا می‌انداختم و یقه پیراهنم را باز می‌گذاشتم، لابد «آدم خوبی» بودم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/673079" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFnK_z-wSEA69iL-CwHPwplAjLPs4HBAZOhySHbfJjTvvXRHDkvd6pgVg-HeuXlJShx0TkO-cip87zWLdIpYL4h0BPkxaZFeiei6LCAG2TE06m7g_tAgv-x4tfYQj0Givdjg3khVGnYZL0CJfa0tYmeZxu_m8PHr7J3aIIO17cSqISkpFQwJiQZ9YDZslTbk6_1dNWqj-NGyLusBKrweC3bhVmK4fuwe9hiAu0YuE23Kpw9iv3tlPO5eAZcEauiOA3YH9hoAeVhUudlJJ2u1K9kRSuGFr-4zT9wH1Jj8tEgrHc6vooRyikcJ8BSj5cJo1TBTqqZ2psVEK9YtOFNuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اردن تا کویت؛ پایگاه‌ها و منافع آمریکا در منطقه یکی‌یکی هدف موشک‌های ایرانی قرار گرفتند
@amarfact</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/673078" target="_blank">📅 20:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW2Ipyg3ooSjS0kCx82Uf0hbDlGrTW3yC-aFEbhTmCNf372cS6OEs7FPfO0Lt0VuZVw_xxNfj6CdM5M1oQWKoPdEm5pXOM2eCMm_7gJvIKsKUPJQ6qV8Hi4zbCS-Yzx5zNaUC6dNlP94mjEKbjqSlq_7A9ySdc0PmgVw_vHQ32z0r8U6ogaS993sGNDV4gu-pOFj2EQOiKHam_3YQMtgQf7YqxeJ8eNT53kj7zESBsWf1I8TpRzyGHYjmH8WPNGuyxE4iaU_DvOJYYevFbYI5pkp3vyOeOXaFUdvkXHWACdKGPsw0tGoo_0K9Y8xIC8hYwjeXxZ2fWaUeWJSq6AVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداکثر دمای ظهر امروز استان‌ها
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673077" target="_blank">📅 20:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShkMo4vOJXtjLuwgH5oeMr3S--e5Qn6drFVTQTOt9BjVsJvjVwlrSMXrhyqOvRMAw4tHlmvlWfgs3Pr1RmcesT38ZThMto4VDwzhCXPJC7ERtsqZS8h5WVTH1ogvSjX96Au8wy3MA3iK6zOVZqx623HAF6Y9ihgH3l2t07g-qE8SfxoKtyz1MgWzHxDPnGokDU-nJKdIKmQUunmG5K07enAF6809ZrAT0ZrJ9L2wvyyBw9RADyE0ZOdTTFVz2XkdHTOtVH-ZR9EMLhhMm3VqY8dFlxFRXT6ASbZ-55YG5P49YwyvkPLSQL0pwEQCkDeDZF0rBQkbTq0ndFu2zcjqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdj6L436DwCS31QCboInUD-oUyD0gwRZZ4o8ylprPHcoGkzaSI8mTxjjLp3FghEqqjVlgzo7O-vk-sorFLo1LOpKR-QWEZaccKec9Uphmo4UW3Lmg6ykH4RMA1VIez8olL58VVSvzsQ_qFK6xv_qlQe_DBsWIVqO5EDVpBRNpY1r-uJZk7xPLnd9NaAxo47yfVgG2nM8pSyrpHkQkobeSAnHHGIcXu1edtISiFItEUBwuy3Wk0RXI4o-HT4c1lKZCBaZClW2oWlL2zkBt8l09CbawZepX8b0iFiqC5V4ugriwoDJa9X_cbth8mn6F8JQMExSQmPdDNX71qoIngrpgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تیم‌های اسپانیا و آرژانتین
🔹
فینال جام جهانی ۲۰۲۶؛ ساعت ۲۲:۳۰
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/673075" target="_blank">📅 20:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نیویورک‌تایمز به نقل از یک مقام اسرائیلی: واشنگتن تصمیم گرفته است هواپیماهای سوخت‌رسان بیشتری را در پایگاه‌های اسرائیل مستقر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/673074" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/673073" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673072">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY_jWViVQJsvfIEUGxKiD7EX8t6FyV7Bb2oCa0tP8rxRlP32UvfAAkLFFiVYipMdUymlSV8yiDhcbusI-Hqy4EPtDS1x-Yy9BC6xwtksYY8cIn2qP9oiDfA9-x8BMm4nNg5ELSGeCUhjS_p8HXBeGdzcQ1m1FMrS3s_u4dp3Jkma3sAih_vhrgNn30OKeOv_Amd4sdDtAVqOVXyWOo5jRhbP9Sac6Ycj4_Ur_mScno-_CusSyxbTOj46sywiGg-RnCxHYwBZgWuwqr8PehHiMStnhQdCNUkQNM2YohtjZb-r3LpiY2OCJpgqbvRYrEoF3CavEafAOOMDQSwaIt6KGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت کمال شرف کاریکاتوریست یمنی از حملات وحشیانه دولت تروریستی آمریکا به مردم ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/673072" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673071">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اردن از احضار کاردار ایران خبر داد
🔹
وزارت امور خارجه اردن شامگاه امروز یکشنبه خبر داد که کاردار سفارت جمهوری اسلامی ایران در «امان» را احضار کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/673071" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673070">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ffa57fa1.mp4?token=lTbl37SL_Ci9n33decJEehtdQJD3ySFo54QMtOhMw8RoUh6HDjKOkpaJ7oQ6BqNYRODCmzb0Vx_yp6GwbgHgNz68WwidF3dQ8mabDRcIyXY_SEzeY6VfKyi9HnbkNy27DvbzxBjMKPyK6vkDsVBdiB4YH5vnktwZJSHrGwF2SYhj9lrd-kf3JoIoduzkfyO3GR3_K7pCQyuB2fyJKhSM0rvl0Y5S040d42-51FVIQAFBIBjgYvB1l-fjxvz71BvQd4TxKscoYD_OMoBdUFNBiguqU2AQopF9lLkOxwQ1dcLTCaZYjEvshfc9ChtNTyzCangZN_Z6SRE0fXXnh8pYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ffa57fa1.mp4?token=lTbl37SL_Ci9n33decJEehtdQJD3ySFo54QMtOhMw8RoUh6HDjKOkpaJ7oQ6BqNYRODCmzb0Vx_yp6GwbgHgNz68WwidF3dQ8mabDRcIyXY_SEzeY6VfKyi9HnbkNy27DvbzxBjMKPyK6vkDsVBdiB4YH5vnktwZJSHrGwF2SYhj9lrd-kf3JoIoduzkfyO3GR3_K7pCQyuB2fyJKhSM0rvl0Y5S040d42-51FVIQAFBIBjgYvB1l-fjxvz71BvQd4TxKscoYD_OMoBdUFNBiguqU2AQopF9lLkOxwQ1dcLTCaZYjEvshfc9ChtNTyzCangZN_Z6SRE0fXXnh8pYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این چند وقت قدر هم رو بیشتر بدونیم
وحید شمسایی در مناطق جنوبی کشور: امروز ما آمدیم اینجا که بگیم ما پای کار کشوریم. هر جا که لازم باشد پای کار کشوریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/673070" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673069">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای الحدث: وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/673069" target="_blank">📅 20:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673068">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: خونخواهی نیازمند تشخیص علماست
احمد انارکی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
مقام معظم رهبری در بیانیه اخیر خود بر خونخواهی رهبر شهید تأکید کردند و این خونخواهی نیازمند پیوست‌های کارشناسی و تشخیص علما است و نباید آن را با قواعد بین‌المللی قیاس کرد.
🔹
مهم‌ترین اولویت کشور فعلاً اتحاد ملی و همراهی با نظام و رهبری است و باید از هرگونه اختلاف‌افکنی و تشکیک بین مردم پرهیز شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/673068" target="_blank">📅 20:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673067">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eef2a5608.mp4?token=YZFu6VpKwoZHZujEe1v6tnFR1BaEiQ-X9b6oZFC4R9y4QvhEkXl0Pg7LZDHqT0hI2iyJSyEmg8MexZa4cOriMaf9UUGGB0_wFdAvL1N7f0cOOcWvusySlHjHKnC5C_Sm4ppG1eapM8PcQrxmEth4hvmpD6G3n2CSzSbJvwVjOzVHtffcEqTa3ph74Q7rNpCUxl5NsQqRnTppTb8P4q92r24ASNCxhzv7-tgIqghCC5zLqq4Us8pa9F8joeLOZ6y_BUOQYotAh67OCj8p8nxvyIvPI9qVnO1gRzylxtC-KdHH2pCv9j3SNanTGrOzwy1PJxRCTD7HQ3VNaOc2GKrr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eef2a5608.mp4?token=YZFu6VpKwoZHZujEe1v6tnFR1BaEiQ-X9b6oZFC4R9y4QvhEkXl0Pg7LZDHqT0hI2iyJSyEmg8MexZa4cOriMaf9UUGGB0_wFdAvL1N7f0cOOcWvusySlHjHKnC5C_Sm4ppG1eapM8PcQrxmEth4hvmpD6G3n2CSzSbJvwVjOzVHtffcEqTa3ph74Q7rNpCUxl5NsQqRnTppTb8P4q92r24ASNCxhzv7-tgIqghCC5zLqq4Us8pa9F8joeLOZ6y_BUOQYotAh67OCj8p8nxvyIvPI9qVnO1gRzylxtC-KdHH2pCv9j3SNanTGrOzwy1PJxRCTD7HQ3VNaOc2GKrr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیلبورد معترضانه لندن علیه عینک هوشمند متا
🔹
یک بیلبورد در لندن با تکنولوژی «لنز لنتیکولار»، تبلیغ عینک هوشمند متا را با تغییر زاویه دید به هشداری علیه «نظارت» و نقض حریم خصوصی تبدیل کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/673067" target="_blank">📅 20:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673066">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سفر نخست‌وزیر عراق به تهران در پایان هفته جاری
🔹
وزارت امور خارجه عراق از انجام سفر رسمی «علی فالح الزیدی»، نخست‌وزیر این کشور به ایران خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/673066" target="_blank">📅 20:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673065">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مردی که از کما بازگشت؛ روایتی تکان‌دهنده از دنیای برزخ و دستگیری آقای بی‌دست کربلا
🔹
00:17:00 نگاه ذره‌بینی نسبت به دانه‌های اشک
🔹
00:21:30 دعا و توسل مادرم به اهل بیت زیر باران
🔹
00:26:30 رؤیت بدگویی تلخ ۲ تن از همسایگان در زمان جدایی روح از بدنم
🔹
00:36:00 افراد ایستاده در صف برای جدا شدن سر از بدن
🔹
00:40:50 دست و پا زدن در باتلاق چرکین
🔹
00:47:20 روشن شدن نور امید با حضور پدر و مادر، در تاریکی مطلق
🔹
00:58:00 دست یافتن به جایگاه بهشتی با یتیم‌نوازی
🔹
01:02:10 دستگیری و شفا یافتن توسط آقای بزرگ بی‌دست
🔹
قسمت ششم (نوازش)، فصل پنجم
🔹
#تجربه‌گر
: فرهاد قائدفولادوند
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/673065" target="_blank">📅 20:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673064">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در سلیمانیه عراق به گوش می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/673064" target="_blank">📅 20:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHz6MSYIVPQRP1HfHcrVvvbuUaul1a-KMfqFPFvGTh3TG8mie2Ku3thC2IeAvHN4INMfBKbP6U9pSEalwdqZ_QxfuW-wgw2dRcr8rnRobisG66uj1WCidTdOFP5pOTC9-oxJvk8zdhRAipadRV79KKhF1TU-b7oOt_LUC6at2JH7yYBxBVxQIIJ-Pv_KKW53Te2Nv3vEz1fBWJILqQenG1VLRibWF8Xl3_tcsU35uuOeBMTImxo-gOk4o1jl-jBkrAbXVcoWwmgcxtZmxhfzqWfW5SMpQh_5rqrgfTzhnx-eMSXqJs0tYMYHi8C2zI2h2TmKRgDEBLfimy62J3xKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoZV9cRKQNd9_OPWxVwF1vJBgwa6eU1xjaCdQTOA9BmkwQo6ENBBCYUObaB38mN_rcTKcCd-vxzKCajiXm7IlxbGcGX2V_n1JT860sV0PpPvlcIS-Vk0QV3kGwGNsJv0RmxKvzopqrbXKBaCZdew_e7DSP6dcQQ0HS352HeoRcKrGmFLLLihSl-W13IoE3hIF1qRAt6C4ZIhQ3s-6H1PMFS3Szj3Jb3mom2T15-buWARvhaUnIxM_cKdbqb5tJx4rFQ4pegru87U7syDO9dFjICAc0M72M4tBP9v4yxr6hdyNXbj9n1E98ACgFRcf53NCTAFQEMZKrZvWgUBGjyBIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAJevWlxn8zRVEanQFWVNoIfgc1DoXtXddX5C3Ki1zjbkeB038f-mBXssAoWG1binv_iIKlTy2Yc5BbB1tJsVOEYzP9WFJzDDHiii4cmaR8HHuaDKpaPjRxXfo80jLR5aKsPqeXMrlsjPaOT3WDBf4wVEseYK8RLOr6oN7q088sGCZYIU8cFcJP6VVIerBbnJuPR4gS4aaCfXKiUHL2p4OApty8pEhZ1KFRZsIIZ12Lkdy738Eeb-gdEaHBEFQADaNG1fQhU8jXkbc38ZxI0EV6y0WR6AvHMiV4XutyIKkafOSxcnjPPg3vtOKqHqhrE-OPK6lULhMOlNBju3ZAEpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انهدام یک فروند موشک کروز دشمن متجاوز در منطقه غرب کشور
روابط‌عمومی ارتش:
🔹
ساعاتی قبل یک فروند موشک کروز  دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه نیروی پدافند هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی در منطقه غرب کشور مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/673061" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6519a564b3.mp4?token=PHS1eG1j4L4LOMLNC56z9DX6XHex3nEZRzJer2H1sGoe7pcQUcmjsyAIJBbv6X7dq1lLWkdzukgyMqi2jFUZ9B8rDlYDuf5EssVG7keBMZJT-j2eXfojQJRwuAjrf0gHjfH8GpzagMP-OTBc5kS_sO4KLkOTipQP3PNtCEehQlUtUGifXfh77nR6N5JJWophMMgAcdoHusf-O-UCNhSNjvzsqT23tMHpy4GRyaEb6eaHMWLb0UgubQxhHUQDW4t-S-quVLFp69nIKbBAasFwvoLyazt18jhM9QnKxFh4Z87iqznGuRtqc_3h8_-j24NZPxYzZfBNi0vd7-_0Q5xgp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6519a564b3.mp4?token=PHS1eG1j4L4LOMLNC56z9DX6XHex3nEZRzJer2H1sGoe7pcQUcmjsyAIJBbv6X7dq1lLWkdzukgyMqi2jFUZ9B8rDlYDuf5EssVG7keBMZJT-j2eXfojQJRwuAjrf0gHjfH8GpzagMP-OTBc5kS_sO4KLkOTipQP3PNtCEehQlUtUGifXfh77nR6N5JJWophMMgAcdoHusf-O-UCNhSNjvzsqT23tMHpy4GRyaEb6eaHMWLb0UgubQxhHUQDW4t-S-quVLFp69nIKbBAasFwvoLyazt18jhM9QnKxFh4Z87iqznGuRtqc_3h8_-j24NZPxYzZfBNi0vd7-_0Q5xgp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنگل‌های هیرکانی در مه
🇮🇷
🔹
دارابی‌زاده
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/673059" target="_blank">📅 20:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سازمان انرژی اتمی ایران محکومیت فوری تهاجم آمریکا را خواستار شد
.
🔹
عضو دفتر سیاسی انصارالله یمن: منطقه به سمت انفجار بزرگ حرکت می‌کند.
🔹
الهام علی اف شناسایی نسل کشی ارامنه را از دستور کار اسرائیل خارج کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/673057" target="_blank">📅 20:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سناتور آمریکایی: صدها سرباز مجروح وخیم در جنگ علیه ایران داریم
مارک وارنر:
🔹
ایالات متحده به‌معنای واقعی کلمه صدها سرباز مجروح وخیم در جریان جنگ علیه ایران دارد؛ فکر می‌کنم تعداد تلفات به ۱۶ نفر رسیده است.
🔹
بابت موضوع تنگه هرمز باید بگویم، قیمت بنزین اکنون به چهار دلار رسیده است و رئیس‌جمهور ترامپ هیچ برنامه‌ای برای آن ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/673054" target="_blank">📅 20:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067baf735b.mp4?token=oFmmWEdCP4Gxco8YA9m5PLh2hrK8vNO1vfXjsmKjcTkjmof1L3nVDB45o1iaNG9ITr29M8qyA4-lb-2arGcNyH8fVsHoGC6CckB0GAJLbVWsr6et5sgQeW8aa-4ZCHSEcPEnqqxogD_KrR3R0U6qnkaGn8Lgy4bbFLiHLua_qxO2tCPPTARDa7kVdKZmDi9npaS5vDxARXcW7_mlJRD39Lq7l_K5DjRpcqhUTSRE1MIFChbASmFvFFvhQZh2sTn8IsuODe8nmGVhYfI3t8lac1ofqBRTNDV1V78jqDdF2g5VIpTTMNj8ussm4lb2svi7q6xgMMyXmwQSnqSJB_UeSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان خدمت
🔹
هفت سرباز نیروی زمینی ارتش، در حمله موشکی به پادگان بمپور ایرانشهر به شهادت رسیدند. این حمله که محل استقرار سربازان را هدف قرار داد، شماری از نیروها را نیز مجروح کرد و بار دیگر داغ جنگ را بر دل خانواده‌های ایرانی نشاند. نیروی زمینی ارتش ضمن…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/673053" target="_blank">📅 20:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJqF2mPpiwafw1h6fBpv9U891Ghkl5RoXsA63Iy7WrA_ac0jrWFrLfERNoNkxfTyAgsr6wX7eW0HWYHN705Ow59herhYtyBXh4q5Pp3bothl9sBVeVTALfqBhRGJvaKM16uXbF75T9YacUjXSkiPoAJuENH0wHYi-ScGq0IrJd3rGK5ysZU8uz4YV1FWHsXe17KOc8v1STwM0oUTvAaOcJsOkbxUAzxi63NOz6N1k41wlHUc_0VYOTWxksmTT65xr6Un_mS9Jme7OTy9fb8kRCW4cRiNDaNgBAMv16vP1C0mntgyi_kSGsfNArTi-dsEn9NlGrg-JsJa2-vNWUxpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/673052" target="_blank">📅 20:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9fd7ac1b.mp4?token=VW-Ti11J8162Mgn19D64CcrlubLnpVmhX1-7VCivtxrcFueX2x0pPMRX8jbAzzhqQtHi9ftPG_hqWBvaZFd-BWUXHk1LUJ7AWqdSc6ZX1ZVfzPXdi_xkiK3mH1X-6GXtFbSFAPUvEKjsdYsG4sZsuSD1P-Megzsd4l21E5RFXozksI1YEqk_Y_8mYrFJLRGh549NgYADS0r3EUfEScB2yZYAWdxpbSHWGb9TWn8eOyFMDxC50LZGgm5N05ic8KUY4OtJhdenUlbX9Oycf5LkIbuB9IKiSzZQjfmED-ScjuujyPt5SQke7cQxcJeyzL3fGvkEf3mb0sNh_maPc8of1FCujxQRAzDjoIFmWaiiR-jIoLH3kkOtNEfQ7HBZ9-L7otaEuDvbf2ypxd8YI8mMAyClJLG1cOaPArzENLiPqgR1PMQBolcT87_qZoDHbcwqL1BEuZqwxt0mdApx9LFUwUQVCb3NxDgmwMXBmDaZO9YsVyIxUbEzN7kLw4OXjzPE3Y6AGo2DEof7wtTTYu5rLmyCAmB1YG_AtpVo4J39KXLhsOphJRfeqeiXsyd3uGHL2dP1fUFVu0cCv0W0ZHVsZE3O7sdtxqOLRJxddXry1MyfsCzBi5l9Oza4WI3WfundSz8zJVxKNdKebMewHXS_rZYM8hs-E8S5TvkS_K_UkOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9fd7ac1b.mp4?token=VW-Ti11J8162Mgn19D64CcrlubLnpVmhX1-7VCivtxrcFueX2x0pPMRX8jbAzzhqQtHi9ftPG_hqWBvaZFd-BWUXHk1LUJ7AWqdSc6ZX1ZVfzPXdi_xkiK3mH1X-6GXtFbSFAPUvEKjsdYsG4sZsuSD1P-Megzsd4l21E5RFXozksI1YEqk_Y_8mYrFJLRGh549NgYADS0r3EUfEScB2yZYAWdxpbSHWGb9TWn8eOyFMDxC50LZGgm5N05ic8KUY4OtJhdenUlbX9Oycf5LkIbuB9IKiSzZQjfmED-ScjuujyPt5SQke7cQxcJeyzL3fGvkEf3mb0sNh_maPc8of1FCujxQRAzDjoIFmWaiiR-jIoLH3kkOtNEfQ7HBZ9-L7otaEuDvbf2ypxd8YI8mMAyClJLG1cOaPArzENLiPqgR1PMQBolcT87_qZoDHbcwqL1BEuZqwxt0mdApx9LFUwUQVCb3NxDgmwMXBmDaZO9YsVyIxUbEzN7kLw4OXjzPE3Y6AGo2DEof7wtTTYu5rLmyCAmB1YG_AtpVo4J39KXLhsOphJRfeqeiXsyd3uGHL2dP1fUFVu0cCv0W0ZHVsZE3O7sdtxqOLRJxddXry1MyfsCzBi5l9Oza4WI3WfundSz8zJVxKNdKebMewHXS_rZYM8hs-E8S5TvkS_K_UkOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدونستین ۵ مکان در مشهد که رهبر عزیز شهیدمون باهاش خاطره داشتن کجاست؟
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/673051" target="_blank">📅 20:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای الجزیره: ۱۴ کشتی از تنگه هرمز عبور کردند
ادعای الجزیره:
🔹
طی ۷۲ ساعت گذشته، چهارده کشتی در یک گذرگاه محدود و گزینشی از کشتی‌ها و نفتکش‌ها از تنگه هرمز عبور کردند.
🔹
طبق رصد انجام شده توسط واحد منبع باز الجزیره، این حرکت شامل عبور ۳ نفتکش، ۳ تانکر گاز مایع و ۴ کشتی باری بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/673050" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3Wdkm8T060eT1Cx24yx1w8zmz6o5vZBqDWS9hx4StBMLDWXpvwX--MUv94UjQHd82UkXh4NoxG1dfwsmclh4_SLvdvhjhKZUTn-rWkT7_vCspJtVEqiZHpFLzKgm56ZbOgI_8phPYpejH_XYtU-DJAH79JE_8xQjy-txXdr6rzGnRZQX_lX3XWpijq4dW9t_BOuEfmN5tGeHZp9-lZERlk8TVkXmhkapUbw3_leJhPt-rQ-BMm1vr-lPCByTdW0gftCkos4cW16nTru5dJyLifZQ1H8gDGxrtBlVxRuY1xZ9m9hKAV34f_HpOWfcT6ioTJNDQwYkZPbO8Dr2KAwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pxA5lTsRSdDkeOoOkaSdAHAXBgXpPwxEzUyL-TI-Z9o3U1EMRWVlaDVgfhzI63hn5pnu1OIoI7xkUR29XT5s8stcEjXvB3k3TJXU13Cvl7hQIB_QIidwcJ5ho93snLPRs7Fc7eklaWCD-iHR34pXMtwSAvShTwfQsbiO2PsLNK-SIrEYrNTFLfGiDLxXB9p7aq0D4F-vTWdIcmpsN8yAj4HbfKzu3CSxq2mHesBlEkA-T8frwYdvGtyGzJPZaeMYO9ESth0PpXt5ag-YQjRsCcS7J1EVgzirkDNYfk6CKoJXwTMJkqfTCe0WRW0XHJZx__cubpebYC-qrfhYlXB5Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر بخواهی فقط یک کتاب عاشقانه بخوانی، جین ایر بهترین انتخاب است!
🔹
اگر فکر می‌کنید عشق باید بهای از دست دادن عزت‌نفس باشد، «جین ایر» نظرتان را عوض می‌کند. شاهکار شارلوت برونته، داستان دختری یتیم و سرسخت است که میان عشق، فقر، رازهای تاریک و انتخاب‌های دشوار،…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/673048" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaavt_FlK6ELoC7zJ39H6uPg-jilb6sVxhVFXXmSTM6-pGpH5ZuUaQYUMlWFG07lA6PgmQkazNnPVpIpL-0X35HwZ34-X8E7N_dE9ZZqiiZkmNvuiLwv08-KE-UdfYjMJIUmxtOzAsrKrPeAtgakDjFciANxqO2UGlo2htIkr_SYhfDvFYSpkThse2bDM6MWK4o_JfcHgb0uBX1miCVauVuOn6qbcWypZcDNNmPgmggldOQVdPhxePkjAm9clxLnq440ME98N8CzIxXh8igwGMrRSj23nMW67iP_8gEIdjURZw3hw7fGE5DfoNshYfBEHwhc8Vu0b7soaZVe98iwEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر قرار بود فرصت صبر کنه...
اسمش فرصت نبود
💎
طلای اقتصادی از ۳٪ اجرت
🏦
بانک طلا
🔄
تعویض با عیار ۷۵۰
👰
مرجع سرویس عروس
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/673047" target="_blank">📅 20:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1c0_a7NI4PrsZ0Qle4ogXpEoD6sjxgcJoZEcxwsJOeEQjLWc6fQ17DMxNO7owt6IU_Nv5zk3d7xVYnLEqscvAZrmPTLnPnCg3X2kLaH7J5z8HAhOe79RXU4LCcqD39NiyUXcpTb2vcyIVwMDJHObrt0B_q5IuIfr3QrMN5RQDTsg5BYgk5ZqfWKdTLYWdlDsGGenpgqzTYzb4q9K9BICiUa1RqTOpPAmZC-E7a60jqPCsuxaXn2jaVXT1vLwDNMoyTtVnjPN8X1nVe2NseXdsVqSWd4WFBGKeaj2hpKFqd7t9kcpB3p36fKi61YZUMz5JJMOTw-Wlg_YzZ5RimgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد متجاوز MQ-9 با آتش پدافند هوایی ارتش در منطقه غرب
روابط عمومی ارتش:
🔹
ساعاتی قبل، یک فروند پهپاد متجاوز MQ-9  با شلیک موفق سامانه‌های نیروی پدافند هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی در منطقه غرب کشور، مورد اصابت قرار گرفت و منهدم شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/673046" target="_blank">📅 19:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf41133bf3.mp4?token=t_70tpAvTED7GGfBPRnZ8OmheeU7kcSALpFKM68WHJsEOM4Fxnd2mtxEi9SUgld-WkXAGRAAI-lj6ezl7mVkXHRwCGvwBADslIZDOMk8483XS9OHOrEvaGQppkHpQhHEc51A-7AhCe3B6Ze82Hr5WmOqJ_40p84j74uUWnaJhD4zDPpVlgmwLU56GubTiBJpNZAZMpm4Tg6AhpjlZprh0UKEc6g8HztTVR8qSh85rpnthzlGqDDOALXkEvfhNWxgakolqTAGVYvLEPTh-mSYZJFFx2psMyEFKLBcl6tBgC6130-qmqP45c6oyc3IRbhkJCHbQITfZ0ELTpybC74Wlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf41133bf3.mp4?token=t_70tpAvTED7GGfBPRnZ8OmheeU7kcSALpFKM68WHJsEOM4Fxnd2mtxEi9SUgld-WkXAGRAAI-lj6ezl7mVkXHRwCGvwBADslIZDOMk8483XS9OHOrEvaGQppkHpQhHEc51A-7AhCe3B6Ze82Hr5WmOqJ_40p84j74uUWnaJhD4zDPpVlgmwLU56GubTiBJpNZAZMpm4Tg6AhpjlZprh0UKEc6g8HztTVR8qSh85rpnthzlGqDDOALXkEvfhNWxgakolqTAGVYvLEPTh-mSYZJFFx2psMyEFKLBcl6tBgC6130-qmqP45c6oyc3IRbhkJCHbQITfZ0ELTpybC74Wlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب بچه نداره، همه مردن</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/673044" target="_blank">📅 19:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHZymOrUsq_MBw9vXwgfHvA1unn0x5xIf2efc7MNF9p40K-QcmT81RxuTgLNdrrPrWEgSLLBhOC8j8p6zubtH2iyreOA_GxX9DCgk4wjrop4NOXuy5Qjxv4g9SGZ-W542UM4KKXqqax-ne14BQltclRp3DeabMwWS71_bWw9sfquN-jLHfsXxoT7PdvLCdot5F53OgwU8WdLRHPVj0Lh3_rQYmeGqn0rIoVEtxw55_ZiGQXzu19H3AXswU0e-YwHIzsQAwiY4S1JLWPf7LaBPSHa5bw3HhHB6KHtp2ogJFcavrcrnzPGkGUMBK8E8LZkyzr8iFecnMIvOMetqgfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TU3m_IyoZY9_J_amlvZNdnUi7JR1M8yn9KUT3-1FXDDFeLbTkfvsQkDtCbRZlYT4CyU2vaIlkFDWm33oXXhOBcHbzvf1HITr5MXTTGb9mT5oT6FnecXXs5DAs16zzjAg2yIfCaZPSHxINMa5aMP6A9UOijx8448inQML5qlt2wxMfX6CBaciazR0xg36p6N9QTSMFWU_926XCkHwV05YHt8ClFJhdvBBNGedbnLyvTYnRc7tvaPi40lNgWlMX4T0dCFxZBsUQ4KOg3qRxY9EL_sW2BQc1RrtuCJoRJHHfrSrTChpMD6l0MdqWC5jkJAyDPbRmTlPrr0hfeUOlJWOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ent1azUZrtNdCGgr70gZXE0NZBYDfSGs3wFXMEps_p3HsAiznVIeZWhvRosyKOTMTpqFfnUgDZrB1_baVADAjfJe9GcT7Skbe7hWDs2qhW-9LpRmZ3LEdgvt5ICw6URQyA61D0LtjPQ7UexqPsYHeaDjqtNvOt1q89CJ6aKZ2GG-i6JVOrbxbv5xz-KIHFWRj2WddGvflQFGDWASumjVqXfR5GdsVIBnNDp3S2SEAuKSr4NeLFy66-GAa5aB6OaZ3eE2sYm_qNyeUyNgPbsCb1eoicvSijhCFjFp2KT6J_3XpG3y8kOK8XA4Xv7DFFI39L9yvR46F2o5WZmyDlgJqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تخلیه هواپیماهای راهبردی آمریکا از پایگاه «العدید» قطر
🔹
تصاویر ماهواره‌ای نشان می‌دهد آمریکا برای کاهش آسیب‌پذیری، هواپیماهای استراتژیک خود (مانند سوخت‌رسان‌ها و آواکس) را از پایگاه العدید خارج کرده است؛ اقدامی که اگرچه ریسک را کم می‌کند، اما با افزایش فاصله تا منطقه، کارایی عملیاتی را کاهش و هزینه‌ها را افزایش می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/673041" target="_blank">📅 19:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHQs6yZ0gSqsNStfh-cXRgNYHbbEO6R-etcE52-fumIVxOIp07NsqBAvnSJFVx_PQK_5wUJfO678NW9kkGmIWVw6rsFp1-6qokbrqoLREK3HpX79vHZW3zIRFLAaYH4Y-QQtCtsgkVwBv48pDeBFzdmkIxZ7_qvKzRKkifOKL8r2rgHsxDNX2XQhv_II8PGbfcM4QIZbo8FOL9MZaxYyLa3yEoMth0_mKJTPUr1DI4s2C1IdwqzHIAJjYYg9JJUqbk4yTg6DH9XDSd6NbjqFc9jDIQpd0_qHV4T3oTcfsLoVjFRmZCaPOLJDIm4ne94bIdDju-VFnVW7GTVqeSufaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکار پهپاد جاسوسی در جنوب کشور
🔹
این پهپاد شناسایی و جاسوسی بامداد یکشنبه ۲۸ تیر ۱۴۰۵ توسط رزمندگان تیپ ۴۸ فتح استان کهگیلویه و بویراحمد در مناطق عملیاتی جنوب کشور مورد هدف قرار گرفت و به طور سالم بر زمین فرو آمد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/673040" target="_blank">📅 19:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673039">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=ZYkzObb5ql2rZl56rnqj5hx8fAdjZ8IrpzAlMiH79CQkUBwgSKCHZn5aVRmXk_xqs5S1ViiCewhvCgJaIAqsrZ53di1jxZlJqrgFyVRm5uiGcDc9xa8wSctoP6H9K4o_-gZGWuw8bhGHJZJy7WOlFDwGdao29a9P8uzGFvsR5M_txJPku4cqbMUIrq_oCpQSQrK38jydAS1fHM3IxBSb22PNYEWQ00QoOCJp7vCbY7Nuc8HdYVrPnlFIuS0o8H5Slgmjo8Oftj4yy2IBfpU4JKxGWzm2J2_5aRG2-EkUVjC9_rLk6INnZc84TdJ2pinSLcaUqjNxfU82thRwrPJR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde07cfb07.mp4?token=ZYkzObb5ql2rZl56rnqj5hx8fAdjZ8IrpzAlMiH79CQkUBwgSKCHZn5aVRmXk_xqs5S1ViiCewhvCgJaIAqsrZ53di1jxZlJqrgFyVRm5uiGcDc9xa8wSctoP6H9K4o_-gZGWuw8bhGHJZJy7WOlFDwGdao29a9P8uzGFvsR5M_txJPku4cqbMUIrq_oCpQSQrK38jydAS1fHM3IxBSb22PNYEWQ00QoOCJp7vCbY7Nuc8HdYVrPnlFIuS0o8H5Slgmjo8Oftj4yy2IBfpU4JKxGWzm2J2_5aRG2-EkUVjC9_rLk6INnZc84TdJ2pinSLcaUqjNxfU82thRwrPJR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت در مناطق مرزی جنوب کشور: ما به لطف قدرت نیروهای رزمنده فهمیدیم باید از چشم در مقابل چشم دشمن عبور کرد/ پاسخ حملات به پل، دیگر زدن پل نیست؛ ما از زدن تأسیسات و نقاط مهم میزبانان دشمن ترسی نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/673039" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dedf68ea7.mp4?token=JUv_4FHy_7ugC1S_zJ5xA6h3LnXMDR-MpENpZSkred00dZuCcfOuCtCyA6dx25LpfxE4tHK9l5JFDYKxdAd5kyt-k6OOnKYyN3rE2j7HDIrr3x0uKPmETRzePd8aDmr1SvEDdUvyGIQO7FcjnE19KN1kHIFBSxNuUFUj-N2EUy9gHmM21PYsBZK6_FdMc_DI8Ff7Fcgw_Zw5ebag4jJd2dEFavqFGk2GexSHBXiu2VK7M8Yvtjev8Pj9C9nDwvHDXfW6gQPwuIfMFILc8bHSrPVGJsW_x4XQlyVzOOguxM21Up-Dt7TUXsIuF31ZSCgO3RU9GJvH8x67dntXUSl9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dedf68ea7.mp4?token=JUv_4FHy_7ugC1S_zJ5xA6h3LnXMDR-MpENpZSkred00dZuCcfOuCtCyA6dx25LpfxE4tHK9l5JFDYKxdAd5kyt-k6OOnKYyN3rE2j7HDIrr3x0uKPmETRzePd8aDmr1SvEDdUvyGIQO7FcjnE19KN1kHIFBSxNuUFUj-N2EUy9gHmM21PYsBZK6_FdMc_DI8Ff7Fcgw_Zw5ebag4jJd2dEFavqFGk2GexSHBXiu2VK7M8Yvtjev8Pj9C9nDwvHDXfW6gQPwuIfMFILc8bHSrPVGJsW_x4XQlyVzOOguxM21Up-Dt7TUXsIuF31ZSCgO3RU9GJvH8x67dntXUSl9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام موسی صدر: وطن را نباید خرج بازی دیگران کرد #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673038" target="_blank">📅 19:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlKdLgfT28ggr3YAkhGqPfnKl8sLLVClD4WXNSLglQsAlU6rG_C-n0lvkL_0Pfead1x3slcvHt6O0FYjc-h5jx2Gda9GXeo0Wzx92ndssT45-aH--VhmdL-i-WoSw1XMh3yMv4bFeBnsbBiGtcN39dGxBXcpHZCRDlXyio_OVYpSTGGHfoii22mCKS8p7waJcqS2TSDpTR_OOAiwDfHzOCw5ZUy-4jI0tTjMdicHRhLiaBaTYgqJElB4wOAOD3RiXiNN24oACbmP576yGTDOxj4QIp9S52EC5GVq4PfMSiPmKw9JTIk1lzlV4FgghTPWcOwAxdDOq9_5QkL_hfZBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_lmbKtMgpSDMBeDKo5VliLaBi6QUNfvxylie6mW3SH1fL8gdoOI49T77wF-hzfJMU8CfUXMouWg_1BdrP-9e-EEYN8tTLCCs42Be0EdnbuBzB38bQic8qDa1Drwa-M4pEJF5t-eI9oI7ZimJUbF1kixk1986Px9vJOHdhu3jpB4bbYwzeTPhq9nk5hXuzCtDwEnbwYgRsJAFC666JHp-z7qwqPVkC3P3erGMQV8gF6kH40uGWXOd9P3pmcdRe6kfHJ7K7VUiTXEj4T9_PqyB5xgGNrnBZE9QRzZ2wqD8qP-VMmzhnkQafkMhTNVX2vcpEnauFPJLEsvkczlGpwuLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در پاسخ به حمله ارتش امریکا تا کنون غیورمردان مسلح ایران به پنج کشور که پایگاه‌های آمریکا در آن حضور داشت حمله کرده‌اند
🔹
اردن: پایگاه پرنس حسین
🔹
قطر: پایگاه هوای العدید
🔹
کویت: بندر الشیوخ
🔹
بحرین: پایگاه پنجم و الجفیر
🔹
عمان: بندر الدقم (مخازن سوخت ارتش…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673036" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
حمله جنایتکارانه آمریکا به آب‌شیرین‌کن بونجی جاسک/ ۲۰ روستای ۱۰ هزار نفری بی‌آب شد  مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
آمریکا در حمله تروریستی به آب‌شیرین‌کن بونجی در غرب جاسک، ایستگاه پمپاژ و ترانس برق آن را تخریب کرد. این تأسیسات روزانه ۳۱۵۰ مترمکعب آب…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/673034" target="_blank">📅 19:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-KNs5qv7FyjI3g24GRCxRpVaROQOUtXexvYZmtkaYMERoRCnpjSP5fX55xrKiZMDFUgX29Z4gYWuWpjrVYcVLqVfNZZKxuijJ2JRcvY9IVIg-Y51vNY1I5wP7MgNvZNSmrKja1pwbtYq0HML9EaDKq4ivwo-4CN6A94SzUL-6uzvKb4orCEyVfPUexZOgOe9AIefJDuS-nAWlQdkl06Etqe_HJC9V_8e_E2lcWwtfDrTkawVXNQqlfjUEApWhktn5Uuz_DPJviCw-tPjdq_PihszPWZQLOVRG9BUZmwkyDvVn8yQY09a_TFJciu7r2N_R3NOivRs_QtZPdMJzmr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RH1HKyvTF6oIOdSTqawUpysD3utoFH8bSmNZeZTxscSP4pXO7CvibKxkwfXoal7UNU9zmZhnuH09wMYEMmXnvUz7fvaDFfcwV-UeuAxVpk7UUO44DGAXUDnx67OC3y2oIpmgKO1GIep-7y54ikN5_5X_zhsja7i-nNU6uBszAnWV_apN1h-sSFKHtS4Tlqazn10OhKPMRBIXy0NxTKrUDm2wlgCE2LE20zVVo76Eic9-5qwwr1NyjLlZWtjcaotSd2tBFI8r0aJscNzqwKy2fNF2ffSoI-fBf5v2Q2QRsYpTflOPS4kDH2JYwUbd9ulvogVrqrcZhXxLEydV67Q-OQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر لحظهٔ پرتاب موشک‌های خیبرشکن، ذوالفقار، فاتح ۱۱۰، حاج قاسم و پهپادهای شاهد در موج‌های ۱۷ تا ۲۰ عملیات نصر ۲
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/673032" target="_blank">📅 19:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjHTdw99FDtod-jCES1YPMkirLlDa8AA6cYcL6c9z2HigGtLOfk3gHjz_wwohkYRtDZRlqMc6uQpEKnf3aEZ7kt99_WrWeypqVaIAI5_oJD1j8-08jo0MTnjVSVOaTXxLSLhsunUH7TvnTxy4Y8nPYjo1a6IlTbbdRS_ASfnHfbXbjdHIiWMlN-kD3Cij0vGEipnkI7WDF5RTey4dhlhZXGywSXTKy0B-ZSSquIRgtSX36mNukpSX3IpoQ9Giyrl4Qn0AxfmpJ2lqlpHgH_Xb5F31GB9JyyTQLxrMkLu_grvl5dYT_lHamK1kE7WlOpyxiOfu0QbnX6_9PKRR2Sv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664f982649.mp4?token=aIG_SVTqZ-7cxfuGA2poMPyFyHjbDBEXGnWtFQOsPPL2rgdGLbzm-XC87NyaByEgS_PXTYnamD8Vk2p1SEeBV51or8h5WY5GtF6m0NeGW6iXD8PI2ZSxd6CaIrvsQxoBOPzNXbYI2sa9k_UoqBHlhfSIW3A4EcImNhiU11AF-K0YimFkTyBrnSoEcyQ1IBCfiO9oO2M6x5uXI4Adbkm8NAjrOvaOwtJVh0MRbn5t2z7BZ38B821orTc8AsTyTBafg_P2zSpkrHUI09VgHi1o45wdcQGFMuBbdUzkgKN9WWc94lGzRSZuk43rsLiO_-94Hm_7dX3PjjOmabfywGXJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664f982649.mp4?token=aIG_SVTqZ-7cxfuGA2poMPyFyHjbDBEXGnWtFQOsPPL2rgdGLbzm-XC87NyaByEgS_PXTYnamD8Vk2p1SEeBV51or8h5WY5GtF6m0NeGW6iXD8PI2ZSxd6CaIrvsQxoBOPzNXbYI2sa9k_UoqBHlhfSIW3A4EcImNhiU11AF-K0YimFkTyBrnSoEcyQ1IBCfiO9oO2M6x5uXI4Adbkm8NAjrOvaOwtJVh0MRbn5t2z7BZ38B821orTc8AsTyTBafg_P2zSpkrHUI09VgHi1o45wdcQGFMuBbdUzkgKN9WWc94lGzRSZuk43rsLiO_-94Hm_7dX3PjjOmabfywGXJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥀
پک استوری ویژه شهادت حضرت رقیه (س)
#حضرت_رقیه
(س)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/673028" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473ab0740d.mp4?token=Nqb2PMe2pTXA8tq-0QoWw5AklBnww0q7Z15wWAvrzs6d86jHGqBl8vD4Lg9emvDvKpYlSpmOWRYu7yEbaRpSU7Zx6fAAaZgP1-yat7HT-NjJmuomyZzfzY-C3_kpM7k7BHCBeBQx6hxMQ_s3GPSzAm7V73GPHWCSknUOP_Vdh31KJal02TtJvTDNXSrbKD516tWY3VdHPG43KOV9mmoYaZvvFqH06oi9IeDPelfv18fJKz73YZU0wctwJj_4GK3_HFQhpMLHBv-AkbFiLr1v_HuO6h9_MdpBPAo8n95I_gamV7YoxHPlibcfHxlQV52-_8tZZqJvd6MifgjkkBTdcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473ab0740d.mp4?token=Nqb2PMe2pTXA8tq-0QoWw5AklBnww0q7Z15wWAvrzs6d86jHGqBl8vD4Lg9emvDvKpYlSpmOWRYu7yEbaRpSU7Zx6fAAaZgP1-yat7HT-NjJmuomyZzfzY-C3_kpM7k7BHCBeBQx6hxMQ_s3GPSzAm7V73GPHWCSknUOP_Vdh31KJal02TtJvTDNXSrbKD516tWY3VdHPG43KOV9mmoYaZvvFqH06oi9IeDPelfv18fJKz73YZU0wctwJj_4GK3_HFQhpMLHBv-AkbFiLr1v_HuO6h9_MdpBPAo8n95I_gamV7YoxHPlibcfHxlQV52-_8tZZqJvd6MifgjkkBTdcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از سوختن منطقۀ وسیعی در اردوگاه گروهک‌های تروریستی در سلیمانیۀ عراق پس از حملات اخیر ایران
🔹
گفته می‌شود ساختمان تخریب‌شده محل نگهداری سلاح و مهمات بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/673026" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCPfHuw_2wSD6-zBaACMucmpdIKAMQxu-Rp-XWHVLKtTq1lM9xIpG8eu6JMdfDBDQRGix0EBzWKRDUac12y20Ubac3fE-VREkZd8IclK5QHUXyTmZ-LEUzBTgM21Kc4RgoSYTNDKCzxEJb1XtXb028TDbcgQp-OeOFnMWRrvRBDnUXu87d13zR4gGkgcDswKhhWQ2sXsLwi2v9z45rYgv3yEK_5a_c1Ya0nSEg5CDeFaeNU1RkyNE_qvIqsq_WJUyDVvMprWKwJCtQGCjp2tEJyGR13gxZXZeEB1Pu0MwtoOSzsYFE6wNVoXaEW5vIE4A2TEECldl24YkvwUTwK2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین حضور در فینال جام جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/673025" target="_blank">📅 19:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-text">🔥
تابستان از راه رسیده و همه نگران پایداری برق هستیم...
🎥
این ویدیو را ببینید؛ شاید زاویه دیدتان به زندگی تغییر کند، ببینید اقوام ایران برای حفظ پایداری برق چه درخواست مهمی دارند...
⚡️
"با ما همراه باشید
@tavanironline
"
روابط عمومی شرکت توزیع نیروی برق استان تهران</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/673024" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0yUtjRCe9IPYZnn9DlBTKsH1Bb1w2EtRJxJxjum4m-1C8KQFE_j_MB7s4bmswlc7-v_7JNJq58BVhqLEq98Fd9c5fJUlhTIH_ijWIqRTLmJK6zxlWaRcxWBBfrp_tQDLYMfOw-JMnr3q0EnaDpqjUhJpQq_BxmT1kqcYJldMmNWvWZFNINvDUQ5iTxEvW5MY0TW6VhNIy3aKmXxS-IWYBzt3g_mhrJnDKxjdWxeklNAzHHq7GO0EzMKYJpiwysaVAxFsA4c059pZBUiVZOsQXOeiJ6r138nSlH4MJZZ8bRU0aAfXg6SpQrEszrSPW_F1IBnKphZ6wBg3256RT16qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین داستان ایران شاید مربوط به یک «گربه درباری» باشد!
🔹
در دوره ناصرالدین‌شاه قاجار، گربه‌ای به نام «ببری‌خان» آن‌قدر محبوب شاه بود که تقریبا مثل یک شخصیت سیاسی با او رفتار می‌شد. ببری‌خان فقط یک حیوان خانگی نبود؛ در دربار برایش جایگاه ویژه داشت،…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/673023" target="_blank">📅 19:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miq7Kvf-dPS7b1jG_fjnOgAVcgyTxu3ktfcQO_HZTn6tmvSiL7vK_3HWlqe5YJOcXAEoaKLDagP7aPLIrt5ZfnvK-9L7O6JTHHnANr1k5pRUWj8WuQRKORpOaUBA6ddK_LZvd2NEiPMVQFUfmGtiZ-mSbkIfQSs2Yq8E0nOKFyDeRk7pwt2w9VkQQpQ8I8LgLKQB6DDp7YxSqSqDmrlR4GCWg5JjvB95MgW6WzWaQaNNzv_1PAzbnXYpWP22H7m9PYyuQso6VOnhHzAV-B_T5d3klAKOln5sorKk1t4VV0_etV5IxQp1UX5gCAnJdpGwk7Nta-0A4KcxTxR7xoiSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران ۶ میلیارد دلار نفت فروخت
ادعای وال‌استریت‌ژورنال:
🔹
ایران در طول آتش‌بس کوتاه با آمریکا ۶ میلیارد دلار نفت صادر کرد. حدود ۲۰ نفتکش ایرانی حامل میلیون‌ها بشکه نفت، پس از لغو محاصره توسط امریکا، به سمت آسیا احتمالاً برای فروش به چین حرکت کردند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/673022" target="_blank">📅 18:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673021">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=Ury-Gq3pKX9pAoiTMDOqQpI3Gco6lgKZbcL1c9B-b8RoZ-ykL2kP_9Vor4YQ3II7pixDfbvsmX8UGK7oVELL7CDMEvY1iPfMqa0lKVdETDhrdMv-c06CDwVGeYtqRLVzcMre5bjSSjsOnLq18-gPLFKDGQPnDzP-Oi-vCH20iK_DsH30T3oO5hmhWBJYZ2T3lgwJcHSs56nGvRB8FRF3snCDRpsnvQZjqcar7p5pYGByJ1yRXaQ67zDpTZBFtBtAjBEoKqYPgbVj7a6v483A3hcJ-mRWZc9Ik9nlp59D3pW3aaKVNQjtpjfgnVp6U8FhZVVfxdxrlmh4ZHshG6QQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54d87d9bd.mp4?token=Ury-Gq3pKX9pAoiTMDOqQpI3Gco6lgKZbcL1c9B-b8RoZ-ykL2kP_9Vor4YQ3II7pixDfbvsmX8UGK7oVELL7CDMEvY1iPfMqa0lKVdETDhrdMv-c06CDwVGeYtqRLVzcMre5bjSSjsOnLq18-gPLFKDGQPnDzP-Oi-vCH20iK_DsH30T3oO5hmhWBJYZ2T3lgwJcHSs56nGvRB8FRF3snCDRpsnvQZjqcar7p5pYGByJ1yRXaQ67zDpTZBFtBtAjBEoKqYPgbVj7a6v483A3hcJ-mRWZc9Ik9nlp59D3pW3aaKVNQjtpjfgnVp6U8FhZVVfxdxrlmh4ZHshG6QQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس در مناطق مرزی جنوب کشور: جولانی بداند اگر بخواهد وارد درگیری با حزب‌الله لبنان شود، مسیر آزادسازی سوریه برای نیروهای مقاومت تسریع خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/673021" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673020">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a70005003.mp4?token=pas4AeR8ylvgZgYdizeiqNwLZh2QsmOWX8GPMPfSmql0k-_UGoAIWLsn1GqCWedBrWvTayroN9sjQ2D2j4ITxRFzie32AkYtw-iv5A_J4Pk4mZeSFHPEovl_V1BjrpGjq2ivI5hV_7UlRBdqePm2qEQqzfigCDdvL2JW8CllZqliC2v7NZVXihv0sST86163OLTPXki8tqiybAk39V_ipH5ATMUAF9qyBuRCeCYFzvmb4pbGy4opo1Uc-GcdGOgOssLpOqDoF_xDuIpaSriAvc4Y_zzCbff1sA904Gr1AFB8G565GBbE_DyAhPWmNqA-voqY-ADiW8V-1Xsh81p_YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a70005003.mp4?token=pas4AeR8ylvgZgYdizeiqNwLZh2QsmOWX8GPMPfSmql0k-_UGoAIWLsn1GqCWedBrWvTayroN9sjQ2D2j4ITxRFzie32AkYtw-iv5A_J4Pk4mZeSFHPEovl_V1BjrpGjq2ivI5hV_7UlRBdqePm2qEQqzfigCDdvL2JW8CllZqliC2v7NZVXihv0sST86163OLTPXki8tqiybAk39V_ipH5ATMUAF9qyBuRCeCYFzvmb4pbGy4opo1Uc-GcdGOgOssLpOqDoF_xDuIpaSriAvc4Y_zzCbff1sA904Gr1AFB8G565GBbE_DyAhPWmNqA-voqY-ADiW8V-1Xsh81p_YYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات جنجالی وزیر خارجه عراق پس از سفر به واشنگتن
🔹
با خروج آمریکا از عراق، دیگر چه توجیهی برای ماندن سلاح مقاومت وجود دارد؟!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/673020" target="_blank">📅 18:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
گزارش‌های تایید‌نشده از شنیده شدن مجدد صدای انفجار در کویت خبر می‌دهد/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/673018" target="_blank">📅 18:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673017">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700cf4632a.mp4?token=ZcgkZC9E0lsLQFBcVkCeI5alNlxIY55XXQ1thDpkPOS1nl61OFOFEzhdaUYdMw_NusnJTKEM21uiMQ1zYXbg7sr0QCG1UhOVVO12zKnR5y2pGl9mLBR89ucND5ACGBn11zttL-MyVtlBDx5BtSNxqWWof3ThVQ19VDmx7ITKfGG43LLMQc1Cvmv9pcgznbhh0oqyCcx7EQMl1PvYvubIiKtwE0DYCMl9SoFH7pG7NcPPv6pC9Y7TSlWzG_uwxeRespdUV-m3W4JXPqqgZzUA7ctNmVh7lRehyvDTh7EnhOuFnj6Q4hwhf_aXiYm9JtFisgd35gZc_CxW5OavOwb0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700cf4632a.mp4?token=ZcgkZC9E0lsLQFBcVkCeI5alNlxIY55XXQ1thDpkPOS1nl61OFOFEzhdaUYdMw_NusnJTKEM21uiMQ1zYXbg7sr0QCG1UhOVVO12zKnR5y2pGl9mLBR89ucND5ACGBn11zttL-MyVtlBDx5BtSNxqWWof3ThVQ19VDmx7ITKfGG43LLMQc1Cvmv9pcgznbhh0oqyCcx7EQMl1PvYvubIiKtwE0DYCMl9SoFH7pG7NcPPv6pC9Y7TSlWzG_uwxeRespdUV-m3W4JXPqqgZzUA7ctNmVh7lRehyvDTh7EnhOuFnj6Q4hwhf_aXiYm9JtFisgd35gZc_CxW5OavOwb0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اصابت موشک‌های ایرانی به اهداف آمریکایی در منطقۀ عقبۀ اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/673017" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673016">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eada6596a6.mp4?token=uHEaMln3aWn0Et6w5gtlVuYOwus6lKNjxpq8tqIDCWh5I3fI7Z2ysUYC1cQVr1BkdDoae6pDEOP5X6kkrSL7ejAFJeF4GrN1Ai_yd1P-TbxVLbvsLvJGNlF-rjBkYB7Vbnr0UQyORdUecO6vLFBT-xpyZmmxR7I8y8jIrk9SYBL39mcYjW73q0VG1LRfdfGhEq_ul_HqwD-nH8zx58E5ia_jUDJKrK4bRVCFaWf7JaSqYydI9sHc114oj50JX6ldry4XpLBsYzrHaQmSUP-z0csHsr3xHYoNwRn_qCzr3V9YmOysBTaB10HUAFl-ClPlVxnp6ehEE-TnzAs6qojZEanDU87V2CTp-NfAs4Rn-KXPpvnEJjOB_3NVbDdhBexPNDoOVOhJomhd4m9nmOeMSzUe91Orqrb9w8-ADzOL_rjAmzUOYxdZekWxS9V85qQCcZQGoyzqzoIm28F7YV9MjHT9llW7TqWmA3JZ3c_zPfcUwpLuQl5AkviB8OAwYDjWSo-ESuhFiRK-72-JwrD1ff12FsigSk21y4wMCzd3dNng2x2pSFtwUUrREVV0XZnqz_kkl93j8V32YcNGrGEYUnm_ZOEUZqhYikRNKZhQoJv5-_gtV9itBqxQfgCjAjhRaAmWZDZp78LeSj1vDv2thgUOMgX0WAec9ab4mR2ER9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eada6596a6.mp4?token=uHEaMln3aWn0Et6w5gtlVuYOwus6lKNjxpq8tqIDCWh5I3fI7Z2ysUYC1cQVr1BkdDoae6pDEOP5X6kkrSL7ejAFJeF4GrN1Ai_yd1P-TbxVLbvsLvJGNlF-rjBkYB7Vbnr0UQyORdUecO6vLFBT-xpyZmmxR7I8y8jIrk9SYBL39mcYjW73q0VG1LRfdfGhEq_ul_HqwD-nH8zx58E5ia_jUDJKrK4bRVCFaWf7JaSqYydI9sHc114oj50JX6ldry4XpLBsYzrHaQmSUP-z0csHsr3xHYoNwRn_qCzr3V9YmOysBTaB10HUAFl-ClPlVxnp6ehEE-TnzAs6qojZEanDU87V2CTp-NfAs4Rn-KXPpvnEJjOB_3NVbDdhBexPNDoOVOhJomhd4m9nmOeMSzUe91Orqrb9w8-ADzOL_rjAmzUOYxdZekWxS9V85qQCcZQGoyzqzoIm28F7YV9MjHT9llW7TqWmA3JZ3c_zPfcUwpLuQl5AkviB8OAwYDjWSo-ESuhFiRK-72-JwrD1ff12FsigSk21y4wMCzd3dNng2x2pSFtwUUrREVV0XZnqz_kkl93j8V32YcNGrGEYUnm_ZOEUZqhYikRNKZhQoJv5-_gtV9itBqxQfgCjAjhRaAmWZDZp78LeSj1vDv2thgUOMgX0WAec9ab4mR2ER9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بکش و لاغرم کن!
🔹
همه درباره نتیجه آمپول‌های لاغری حرف می‌زنن... اما کمتر کسی از بخش تاریک ماجرا می‌گه.
🔹
دارویی که این روزها همه دنبالش هستن، در ایران چه وضعیتی داره؟ و مهم‌تر از اون، خطری که شاید اصلاً از روی ظاهرش قابل تشخیص نباشه... قبل از تزریق، این ویدئو رو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/673016" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673015">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_06MxAuvgVSmaY33anzW7YiXuuKmnQR-kbyvM4BUFz1eVSIhC4WNEsyyMEIruUXtQijGxMkLlUmcNOhWLY0ufi7aNjGabLjDNt48tec-3CvOt9FXN7Oqo7svh066U2S7fO9H2VXuqTQX1PekiwHdrKPe8Z8YxJpWqaV5XNqg_MqCKc65tduTRCbpzghXJ4f6V2o8q59_4EnI9kLUma3dnlcQk55pz0-rLhELll_bmHuBkoGg64ucjXZMAiPpNaZqQXZK0ZB3x6_CKFud5VLFz1kPsq6jF7f9x6fsp2roSGwddzqdi02XvmHPRqT6Fg_5xmy6eLFZKKE8wx8dIw-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: در دوره زعامت حضرت آیت‌الله سید مجتبی خامنه‌ای، حفظه‌الله تعالی، مسیر نورانی و پرافتخار مقاومت را ادامه خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/673015" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673014">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTxJ3XnYX3DhNMfmMJWFfvsL8BhpNIRA-F6Ffto8DTpEk-cQ8RKH9aHh77AQnAwlB_BsL-WbHSLki1ERNqeXVw1xDsN7bWLShv9EXNA14vFB4-mp2y4uSs3yf-7I64MHDd8vNuYPhw1lbWcQwGXrbatUeKn1pNwhlGhMtazdeMlKOB0akEbjedGQdc0Ap-yTN2ByVruGOzMNXVFdb1LL8CYOzyFpzpGiH4ITk8Yrqsk-PtjctN5KbReimX5O60DG3Firpz7tTFHZw32N6285a3TQoUD567nvhVwInuFRmnVJGmc2RataA-HehXZgA-0u2XvudORyruGdVZ5KJE2QlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی چهره‌های فوتبالی از قهرمان جام‌ جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673014" target="_blank">📅 18:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673013">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=hp-RgDq7QlAF5CvKBX3cP3crBfy5JzgwkokoC3A1-80qQLatGmFjnf7B9bvYU1ATwNEpCs-i4JOGBc-1WZrmoftec_SsHPeiDcgkzAivSmofAo0E7YeEaB46sWLR6MDgyHluWLlTpS84Ky_wveXwGO4EdsqMH3aXpujokZGhdNVsR_by4RtpHfhAbLUnuxqcAkNvft72yA0jzNvavQMKFA9olaLDZADvTnySDtYwCy2zfbQdyZ8e-irSMKM_41eU49v0QKpW6m7pfNqIK0E3kkVOM6cMa4T0-05IontDHr2L7KKDHPUv15WjKvFDnwUE2albeLP8dZkowAzN2tKbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5143cb7b64.mp4?token=hp-RgDq7QlAF5CvKBX3cP3crBfy5JzgwkokoC3A1-80qQLatGmFjnf7B9bvYU1ATwNEpCs-i4JOGBc-1WZrmoftec_SsHPeiDcgkzAivSmofAo0E7YeEaB46sWLR6MDgyHluWLlTpS84Ky_wveXwGO4EdsqMH3aXpujokZGhdNVsR_by4RtpHfhAbLUnuxqcAkNvft72yA0jzNvavQMKFA9olaLDZADvTnySDtYwCy2zfbQdyZ8e-irSMKM_41eU49v0QKpW6m7pfNqIK0E3kkVOM6cMa4T0-05IontDHr2L7KKDHPUv15WjKvFDnwUE2albeLP8dZkowAzN2tKbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مرزهای جنوبی کشور: ایران برای جلوگیری از اقدامات متجاوزانه احتمالی آمریکا از طریق کویت، نابودی و تصرف پایگاه دشمن را در کویت در نظر دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/673013" target="_blank">📅 18:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673012">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2B6ZJVwsFmU9Qa71nBB6DvbV380bF3rIbZVN8X9E34-sBcN78VR47VXUhQA4pr7T69AjTxuki1rFR1yL1vp6djuyxQC7QBXOTfenu1eek8YV-aIika92k15TjAiuAvBwAIjvnV_2wQhkRBYokpZjhWZZk2LfV0K26W6RMPcuEll81oCoHlHE7wdjCWs09BUZmf91vA_CzBcJT1iBpgmbQ0EWow_9mq6_DkgHSot_MVWYNjwcnaAWlWcQ9NkaukygOSdSO75pUHgAsYokApMAQfXimmA-QQH1mDceYBAmx08qq-5B0DYAMo0o5IP_OEUu2_mb8605cizWP302-tlIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیندا کیانی، در واکنش به حمله مجدد آمریکا به ایران، با انتشار بخشی ازصدای شهید آوینی: «اگر آمریکا تهدید خود را عملی کند؛ و از راه خلیج با ما رودررو شود؛ شما چه خواهید کرد؟! خلیج گورستان آنها خواهد شد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673012" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673011">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
هشدار انصارالله به واشنگتن: در صورت شعله‌ور شدن جنگ، آمریکا بزرگترین بازنده است
انصارالله یمن:
🔹
انصارالله برای پرداخت هر بهایی در مسیر شکستن محاصره یمن آمادگی کامل دارد و منطقه اکنون در لبه پرتگاه انفجار قرار دارد؛ واقعیتی که عربستان نیز به خوبی از آن آگاه است.
🔹
اگر ایالات متحده در کنار عربستان علیه یمن وارد میدان شود، در یک باتلاق عمیق و بحران راهبردی گرفتار خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/673011" target="_blank">📅 18:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673010">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
تشدید گرانی در راه بازار لوازم خانگی؛ چرا ممنوعیت واردات لوازم خانگی یک اشتباه بزرگ است؟
اکبر پازوکی، رئیس اتحادیه فروشندگان لوازم خانگی در
#گفتگو
با خبرفوری:
🔹
با ممنوعیت واردات لوازم خانگی، دولت مجبور به پرداخت هزینه گزافی و مقابله با قاچاق می‌شود آن هم در شرایطی که درگیر جنگ با دشمن هستیم.
🔹
در شرایطی که هم تولیدکننده از وضعیت بازار ناراضی است و هم فروشنده به دلیل اینکه مردم قدرت خرید بخاطر گرانی کالا را ندارند، چنین کاری اشتباه است.
🔹
نمی‌توان سلیقه مردم را محدود کرد، هر کس پول دارد و دوست داشته باشد کالای خارجی و هر کس بخواهد کالای داخلی می‌خرد.
🔹
این ممنوعیت به مرور زمان وقتی کالای خارجی در بازار کم بشود، باعث افزایش بیشتر قیمت‌ها می‌شود.
🔹
ما در حال هدفمندسازی فرآیند واردات و فروش کالاهای خارجی بودیم تا دولت و سازمان حمایت، نمایندگی‌های خدمات پس از فروش این نوع کالاها را فعال کنند اما این اتفاق رخ داد.
🔹
از مسئولین می‌پرسیم این تصمیم به نفع مردم است یا به ضرر مردم؟ به نفع دولت است یا به ضرر دولت؟ در جلسات نشستیم و گفتیم بازه سه ماه دردی را دوا نمی‌کند.
🔹
در شرایط جنگی به جای اینکه اوضاع تسهیل بشود برعکس سنگ‌اندازی می‌شود. فکر می‌کنند ما مخالف تولید داخل هستیم در حالی که اینطور نیست‌ و ما چند سال حمایت کردیم، حمایت کردن وظیفه‌ ماست اما اگر واردات قانونی لوازم خانگی خارجی منع بشود، قاچاق جایش را می‌گیرد همانطور که قبلا بود.
🔹
ما می‌گوییم نباید این محدودیت باشد، می‌خواهید کالا وارد بشود و زیر نظر دولت باشد،  هزینه گمرکش را (در صورت پایین بودن) بالا ببرید.
🔹
هزینه‌هایی که دولت می‌خواهد بگیرد را بالا ببرید؛ اگر هدفتان کمک به تولید است ارز تولیدکننده را بدهید، چرا با بستن راه ورود کالا می‌خواهید به تولید کمک کنید؟!
🔹
برای مسائل جلسه گذاشته می‌شود ما نباید فقط برویم حرف بزنیم ولی اگر هم نرویم حرف نزنیم می‌گویند اصلا هیچی نگفتند. چندین سال است نظراتمان را می‌‌گوییم برخی انجام می‌شود و به برخی‌ها اصلا اشاره نمی‌شود حال اینکه دلیلش چیست را نمی‌دانم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673010" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673009">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هیچ پرتابه دشمن به آبدانان اصابت نکرده
احمدی فرمانده انتظامی آبدانان در استان ایلام:
🔹
شنیدن شدن صدای انفجار آبدانان مربوط به نیروهای خودی است و هیچ پرتابه دشمن به این منطقه اصابت نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/673009" target="_blank">📅 18:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa95e9d12.mp4?token=VRmhzbuDWUozle3c0z1mhSUbaTqFwzluJPNQ7lUXwbLa7OFpFTlzhOQjs7vxCh0qgiBqZ3z18jYOYKz6JFhiiGgYGupln-AjgHTAV5AsX75yiVmRfTcZgqBvyzqs2oLi45a8oAVt8npogbNQCIY-x_5shyJvxwovbPk7jPCWEst1Mzq1kQeZMiH83gsLVjI3R2tP8WAFxC8Bw18cyNEEsPMAHSoqWJ6MTsvDBBVROz_YA2baT53xcFNmH9b8N3Q3D8iNqEzt48HqxXLktJ-jkeBWMeI77AasldmU5zk698hfqrB3FZjnrSHphpt3r4PWZkF_iWLkovbggLx9w-h_4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa95e9d12.mp4?token=VRmhzbuDWUozle3c0z1mhSUbaTqFwzluJPNQ7lUXwbLa7OFpFTlzhOQjs7vxCh0qgiBqZ3z18jYOYKz6JFhiiGgYGupln-AjgHTAV5AsX75yiVmRfTcZgqBvyzqs2oLi45a8oAVt8npogbNQCIY-x_5shyJvxwovbPk7jPCWEst1Mzq1kQeZMiH83gsLVjI3R2tP8WAFxC8Bw18cyNEEsPMAHSoqWJ6MTsvDBBVROz_YA2baT53xcFNmH9b8N3Q3D8iNqEzt48HqxXLktJ-jkeBWMeI77AasldmU5zk698hfqrB3FZjnrSHphpt3r4PWZkF_iWLkovbggLx9w-h_4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترس آمریکایی‌ها از تنگه هرمز ریشه‌دار است؛ کابوسی که هنوز از حافظه پنتاگون پاک نشده است
🔹
شهید نادر مهدوی، فرمانده ناوگروه ذوالفقار، از چهره‌های حماسی نبرد دریایی ایران با آمریکا در جتگ تحمیلی هشت ساله بود. او با مین‌گذاری در مسیر کاروان نفتکش‌های تحت اسکورت…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/673008" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حمله آمریکا به سایت نیروگاه دارخوین  سازمان انرژی اتمی ایران:
🔹
آمریکا روز یکشنبه ۲۸ تیر ۱۴۰۵ حوالی ساعت ۳:۳۹ بامداد، با تعدادی پرتابه به سایت در حال ساخت نیروگاه دارخوین حمله کرده است./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/673007" target="_blank">📅 17:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgKZFOnasZT-ijyM4LFwb3FAAs3U9WqFy5bsz7E4h2BW5Llke0PmPbhzBesQ6VT8bDfjPphZF2_2y8bEKIhkKSQIiAfd3QzUrF4r7mKjjyII9X9MlrKowLMtrfmFGj771wc2xjrIA5OVh3rnnvjxINiGMLc8JlDolbxpPYjMsNXgJuCknC4s5RL02CRBLtZo27UhfJ55YV5WCU_CFaWGKahWexNfui1jas_aWpkuTVzs8eE757YS9cyFwBGGKoVx9HfNiRu-T-dkVGt6fRYpWNcJUtuyhGBJNYmrN2ukEPpgJDl35mf4OzrxtQyh26PP4HKvsMbPxMeTRBZeCR4giw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔔
🔔
اطلاعیه پیش‌فروش بلیط‌ قطارهای مرداد در علی‌بابا
بلیط قطارهای مردادماه با تاریخ حرکت ۱ تا ۱۶ مرداد
از ساعت ۸:۳۰ صبح روز دوشنبه ۲۹ تیر
در وب‌سایت علی‌بابا پیش‌فروش می‌شوند.
دسترسی به ظرفیت کامل قطارها در
علی‌بابا، رتبه یک بلیط قطار
🥇
قبل از تکمیل ظرفیت، رزرو خود را نهایی کنید
👇
https://albb.ir/5wiGw9</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/673006" target="_blank">📅 17:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فروش اجباری بلیت دوطرفۀ سفر هوایی اربعین ممنوع است
رئیس سازمان هواپیمایی:
🔹
هرگونه فروش اجباری بلیت دوطرفه یا مشروط کردن فروش بلیت به خرید همزمان مسیر برگشت، ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/673005" target="_blank">📅 17:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-673004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeAp4_H7E8aisODOrvM3wrRflsqHFKNT-k3_L2-oIqxjV7_Vq6yBRuumBzbXQu6AsX9O03DZ9avUNvZ8muTCWyqflFAy6HjgUXFmyiEbHHdYafWocVRvfJ_kbY8QZPJWsUbnBtyV5k-FI3wggACVsCpkgpyQ7bEfyvwI-l3gHONnH-InsnIMG0zWsfRqr7YEplKqopOaMRGGImw_3cOAY9Es66XXinqs6q-lbLkUI7ekJWTNGipSmF_axDATgA9ybVk60MoMKejh-DmanbqMu6dPciYxzUmn8LA4qhVnLXt3zmGePrP9Ie5VFQ-E3QBJSYtIsxKzSm_YbIu2Yb_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کپی برداری Dior از سبک پوشش ایرانیان دهه ۶۰-۷۰
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/673004" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672997">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9ptZzSTcZaQbUMOt3v5tTh4gZdLlwWExN4xCebcs3P_PSAuX8VwoOQKSK4S5qerq1r-eyF3m5-K1UhGvsGjvbhQWxZAtXHUApUmKadrKWZpzIAaueTQ7MY8PyWl-civitx1-4jnfjtf2pbS6TdlePXSTk6IfFG4EQlTjKhsw1j9kJ31rbEc2VRsXdx0EzH_RWGFo3qNNPWupSi25_s5iYN1V-lPXJoLeUFTU9-tgPULl_9_i9NZh_D1GADS1FNk5bsXgRjbH5atKw7URQB3eQt2Cg87l6QqnJ9A-4BHFcn8Jrpn4YQiEzIYxWg1ufDnYhcgtUtodNSoZhjIoT-ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTaQ0ufD14hI7RehPm6t6aE4J7nQgoJ6RDnQmdF9qIs1zGmOgzlWMYn_fEfxWfYVTvln5dvOTvt07HAYLxA0ep2QbFs1MX_sWVIZrB4XQfO1mN39pHt7kv9I-OBYeoxPZKubcFys3OLIWFT7TUUh8Jjg3VxsczVOI8cS-cCdkdzr8tM1Hz9o4_PyCbEKT0tRzURC27gZVVJJO3wZLHygCQkFmbHM_Ev8MoAm3h5_fiebUTEUHIIzW7cziMOaXW1OD8yIxEDpV9hWcVQw6s0kpmhyWBml2omV_FhVLLPttqGK7R2FtvN8zRla4LRffqLjafumK6-4BeYr6FVDdzerPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASZau1kUAoU6GWrx_4Sjzl-Vf8oML3XoAA62IFK_9OQEzwbu1tKWpEwwFTON_MqiB8lrcltnkPJXfRb6I4Fklzj1f56PR4XnYbk8ICyDQAb8w6MovU3hZB5qXsZek6jj90dp3ccjZ3BMmTZzdXVefZsNgh7lQ97Zcs6En52oojHTS9NSr9U0eRXH52qYRfQ3xT8djzOTw4rVa7klYYMVB9yJP93hPnfj1Zn8hrc3x_xGM9PU_jkigYjevpLSUeEWQx-qV_ZLQiNnuLubVpgYnB49XugEylfB_3pko4BkCXjG1BrFmZZvMGv_JbaSvU4YB_rScwB40mJ5sZIkQuMEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0ygU8qxOSuoLJ9vVTj103leWFdM70WIxZZDSdxKhVqrwRHVPyMeL0TESlW0_p1SFdJAG3y4X527-50wU_--Tm5hEqLiALrNNoB3-r8x7aK1PwfTb7bnar8qf7RZsqGe1ACWeEEN5l3Nbq1wwd2DBSEJHX71uzeOXBQNmxpR5PNjs5ynxe-mP1JfbrQRGVSRvWtazUreKzygA0mYG5jSKYOtAOCV0SgPlo_SgXUt99K_HYXmXX7IDVkFzIlEmM5kQSwGpbe1GbSdW36P4Ek6Yjncd2eFcQYI6YF-v6NnHamnQxaD9PHMe0zYz95gmdbODeia-NU38JlyTfz97yy5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2mtA6W2_RSGo3a2WWx2jOyTVymWWxwaZ94dY3NACi7O5hhRz9cxfxJ1NqWQf4QZAdRUhiE0HWi6SvI8vAwhPKdDHJ_1DRDX13PX0cGg4_224-Qcwg2dMDUvSXwCoqPiNRADbv_BvCi8lsnbqQpKBg2p9RTEZIMqGjGPq2LNCd68kdY7xVQ44j-y4eULQ2JE3TLECM7tgrMLByNm7jfscqPW2mOv2liiGRrEM6AQn9Lr3c6CHk9NILC-V5xzqYlA1bx9UEven3TCOc7R0ka7d9-nJKrlZnspTj-ByGJzpOhcz4vaxH4zFyoB9vPRzkQFiZFy_18r_vnRK_J8eo4ztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgW3ldaQma9etea5-4wDFB3GjGsl85WTtpKtfwTISLG257PeZ-JgBTMus3wqLWarmeit84Vs4cj0XL6GK8h57hBXdf76hs2B6EAhz7J_ugKKPxQduYKttIgtOKhNJ9mivM868rdMCi5HoWajYbCYFa7zuPXDswENRqdP420NHc9KbGH6oBqJbnBOG4NT6rwKuQz66JTOYvi_3j6Z6zCCOD2It7jzppj-1_gHRrSiidyXTGeHDVKULi2uadYJhQuWRAzIQWUrje45w_slD0ap5OrlTsJ7XU6LG6kEktq6T4ekvazp9fuWMI4toL5KgGWZe6Jdxn69koRiiPOkoOFXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzR7dPgwVKIucgW7QSOOVHKi0EK_UMHWlgtdrkzh5UsHhQBvQIu57v4cnaxsc78LrcgR9KwTS3dBQXSkxglQX25Bd7Su1eyB5epjFGa3VJ0WBvBCU6q0DqWjD-M16Itbq3lUiVm4spEBYoIxFK2Vt0SK6Ow7diKOAwCeS6KDmJ_O4VmH7XFiUpk8YcHe5xBeDrSDfisYRFq3JToLj3-APPRNbKY0_XhvaoTYLHAYYb68lyaljFwbeGxgAQWzC1Je2Ia3TOlaWT9elNLLd4NCWkRXUqjGu0Tx2aBHfEnvPEmynaW0VCuOm9zdD7AJvNrI5Kcjef4QpRW9PFbfSxkQ6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نبض زندگی در بندرعباس
🔹
ساحل بندرعباس در روزهای جنگ نیز میزبان شهروندانی است که در کنار آب‌های خلیج فارس، لحظاتی از اوقات فراغت خود را سپری می‌کنند و زندگی روزمره را ادامه می‌دهند.
🔹
عکاس: عباس ذاکری
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/672997" target="_blank">📅 17:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672996">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد آمریکایی MQ9 در همدان
🔹
دقایقی قبل یک پهپاد آمریکایی MQ9 توسط سامانه‌های نوین پدافند هوایی ارتش هدف قرار گرفته و سرنگون شد.
#اخبار_همدان
در فضای مجازی
👇
@akhbarehamedan</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/672996" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672995">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مهر: هم اکنون صدای انفجار در آبادان به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/672995" target="_blank">📅 17:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672994">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjWBSJhd8SrIT2hO8jGe3xggDotvqARDuLbmD9w8nDpig6lgzqL4m_PLXUwfU_bjGtbzwqCHn2R532RIwKGNvktyI6Jogj5UOkucdnTWD2TY8qRoijflGTkMYaJv07KkQR9shLjriseI79kO7zEQ6eeeVzXIac9dJF2DJ71968Vw3U3_eGiIyYfjAz85Zy0DRKV12sW7YGvbQv22nbYpo3CI_9xQeeaqR81k1h5TnraTtckJIdI8Oeavj88jNndF6THBipWpiWfvVu_4SPHWGSK--7v_KqrTab0whASfCM7p1Ksjyvi34vGY4flcGFJyNgmkgkbzw8BCESAlsyyb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برگ‌های این گیاه خیلی شبیه پرنده ست و بومی استرالیاست، این گیاه birdflower نامیده میشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672994" target="_blank">📅 17:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672993">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تکلیف زمین‌های تازه‌متولدشدهٔ خزر روشن شد
سازمان حفاظت محیط‌زیست:
🔹
اراضی تازه‌پدیدارشدهٔ در سواحل دریای خزر که درپی پس‌روی آب ایجاد شده‌اند، متعلق به دولت و غیرقابل تملک هستند و هرگونه تصرف، واگذاری یا ساخت‌وساز در آن‌ها ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672993" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672992">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه تولید هر کیلو برنج به ۳۰۰ هزار تومان رسید
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شورای عالی قیمت‌گذاری وزارت جهاد کشاورزی در اقدامی غیرقانونی و غیرعُقلایی ممنوعیت واردات برنج در فصل برداشت را لغو کرد.
🔹
هزینه تولید هر کیلوگرم برنج به دلیل افزایش چند برابری نهاده‌ها و ادوات کشاورزی به ۲۵۰ تا ۳۰۰ هزار تومان رسیده است.
🔹
با این مصوبه قیمت برنج در حال کاهش است و کشاورزان با ضرر و زیان سنگینی مواجه خواهند شد. از وزیر جهاد کشاورزی می‌خواهیم هرچه سریع‌تر این مصوبه را ابطال کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672992" target="_blank">📅 17:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672991">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✂️
ریش‌تراش/ماشین اصلاح HAIR CLIPPER مدل GYT-999
تیغه استیل ضدزنگ
✅
| شارژی
🔋
| مناسب اصلاح صورت و بدن
🔸
نمایشگر LED (نمایش درصد شارژ)
📊
🔸
شارژ کامل: ۲ ساعت
⏱️
🔸
زمان استفاده: ۳ تا ۴ ساعت
🔥
🔸
شارژ با Type‑C + کابل شارژ
🔌
🔸
صفرزن و خط‌زن برای اصلاح دقیق
✨
🔸
همراه ۴ شانه اصلاح + روغن + برس نظافت
🧴
🧹
🔸
بدنه پلاستیک درجه یک
💪
🎨
ارسال رنگ رندوم می‌باشد.
💰
قیمت قبلی: 1,698,000 تومان
🔴
قیمت 1,398,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/47608/180124/</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/672991" target="_blank">📅 17:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672990">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مهر:
هم اکنون صدای انفجار در آبادان به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/672990" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672989">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
‌
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672989" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672988">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a15429d.mp4?token=na-Hzq9SDzc8r0Iuv0DeySGe2DIgCihJApdVnr9fueUJKZEwiCbhkguVI_QXj61slIBDWNQJs630Ki6aCuFg8Ak8lse2Ig7ZL49Jc31V3HM7ycSqLCipdQs0e52AgvVCv2Exhl2XYXrvxs4W9onlocdt0RLAqpOxn2vxyoM3XtOkmEOuBYkElK_8OD4opF2g4IkKUa0mnnuqcUAb99kI5uIG9GFZAB4UbIGUgrkvnCRXsU4A1QknE4REDIOQciCxAzQAnRK80BkrB8Sk79ZknFFd0e5Gp417m9RjvvI-olaRK8EyQTqfdBygZ8cGz_W-Tt-ZgXKTMu7MtlxSCc26bRKmTOu8WIVQfebWeolFjRDi6iQuxx-HpWW_0MOaNcWREtYh_8n68GD17-GtqARlbSWgA4dXXsbmMkaDqDeZsRugFr17dEfDcNMceNywrV90m5PYSz4SmaDO8dtB8iCmxJI1qZISGMPuTpQK6PihrKxeWJp54jMzdhJAiZ-7ps8BbZgrMJVaxnhzyZe7mvTXSWQooW5aJT7AD5KnnWHVOmZJ6dxTrrmJy84RV_5xg_gfkqCWa9C4gxULdHyaRePvC0xqEU1rQrjTLuYgd1gvJawzG_x0g1qgZvLGRQRQKpSWWNRc_eBr-S-GNOQReXnKIqkggptmgZ4KfwHRoPZSQs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» با آتش پدافند نیروی دریایی ارتش در جنوب کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672988" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672987">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: هواپیماهای سوخت‌رسان آمریکایی پس از حملات به عقبه در اردن، از فرودگاه رامون تخلیه شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672987" target="_blank">📅 17:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672986">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
از آغاز تیرماه بیش از۵۰ نفر از هموطنان در حملات آمریکا شهید شدند
وزارت بهداشت:
🔹
در حملات هوایی ۶ تا ۲۸ تیرماه، ۵۱۷ نفر مصدوم و بیش از۵۰ نفر از هموطنان شهید شدند.
🔹
در میان شهدا ۵ زن و ۲ شهید زیر ۱۸ سال، در میان مصدومان ۳۵ زن و ۱۹ نفر زیر ۱۸ سال هستند، تاکنون ۲۸ عمل جراحی انجام شده، ۴۶۸ نفر ترخیص و ۳۲ نفر همچنان بستری هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/672986" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672985">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
هشدار قوه قضاییه نسبت به هرگونه انتشار محتوای خلاف امنیت ملی
🔹
قوه قضاییه با تشریح «قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم علیه امنیت و منافع ملی» نسبت به هرگونه انتشار محتوای خلاف امنیت ملی هشدار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/672985" target="_blank">📅 16:57 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
