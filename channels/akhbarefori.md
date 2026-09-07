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
<img src="https://cdn4.telesco.pe/file/WhyQmDaD8UBl9Eq-I8gwlRcY7UCaVS_0dLOsIM1pqQG1Nc6Gklab_iG95Y0in9USfSwFFMn7ifOB_11i4U1_HtenDkt4j0fsoH2IQ_bRUjPpqizlqhp8bCEMDghDQy7go0CIc-ojG3C8N9zm7TuuxLUdSh0NS4D_yn92LlCkFDshFpnsANWftkpRPzKVgTANTnvQT0x93Epo8JQAVK3F8cE-q-tOrd08wjpwl5S62Q_XiGrai06kXSFqHhH_Kl8hMJF-m592oyF59biSndldKvWdIUuGxcgi9lDe4CYvIZcJHDHLQIRqmcoJb4TjCfUp5vgWJqhpLs612hdG4hGeaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-687929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ریزش معدن آلبلاغ اسفراین؛ یک کشته و ۲ مصدوم
🔹
در پی ریزش معدن آلبلاغ در خراسان شمالی، یک نفر جان باخت و ۲ نفر مصدوم شدند. عملیات امدادرسانی با انتقال مصدومان به مراکز درمانی و خارج‌سازی پیکر فرد فوت‌شده پایان یافت.
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/687929" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رسمی الکام‍‍پ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaffec5c4.mp4?token=ZQKtg2wvhqI4-bp_8FJYNJLcrXm45xn3RWBVFzUHBYXv_nNktDmi_kYAHcM97s_M1aE_K1NIIETh4-WfN_mbUh_3AUqwDWJwdz0VejBjeizolCP5AYb2R6Yco_4yjW5r-4C_WIRPQ5KYy6Lg6L0f6G8MhgyQx3oDFVcCyMgAm721EAR5EA_85scI3ZHwbx9Q64IagraW_KEuMCwuZAa-tc614gSzG8XW_L42paBqLtkWwLq1EwHmzi0ZcsuwVTzQfljLoMgEUsdc5xzJizf3D_z5pxGYvDBR3opSK3kdbdr18orRhjnNq1Yf4I-EdOZ8__dZSJm-hRMYhM-OjvHa_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaffec5c4.mp4?token=ZQKtg2wvhqI4-bp_8FJYNJLcrXm45xn3RWBVFzUHBYXv_nNktDmi_kYAHcM97s_M1aE_K1NIIETh4-WfN_mbUh_3AUqwDWJwdz0VejBjeizolCP5AYb2R6Yco_4yjW5r-4C_WIRPQ5KYy6Lg6L0f6G8MhgyQx3oDFVcCyMgAm721EAR5EA_85scI3ZHwbx9Q64IagraW_KEuMCwuZAa-tc614gSzG8XW_L42paBqLtkWwLq1EwHmzi0ZcsuwVTzQfljLoMgEUsdc5xzJizf3D_z5pxGYvDBR3opSK3kdbdr18orRhjnNq1Yf4I-EdOZ8__dZSJm-hRMYhM-OjvHa_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور فریلنسرها در
#الکامپ۲۹
، جایی که عرصه جدیدی برای ارائه مهارت ها ، توانایی ها و کارایی
#فریلنسرها
فراهم شد.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/687928" target="_blank">📅 14:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687923">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOSPov8Jqlmayl82PhICtUkt_7s_VMBpxhWocnS2En9GyAL99-I6O6XosnzceH8VDzCx5zrclJ-gyR4dHjo6_5yUaDYKxVnmr6ey-Arl-dW3PJi0oONlx54Q_vrUeujopB5To-W0PBDNq50BTuqksSAdialInaYla1A8gklQg1tZ3B8UT12xlAY9ubcoMk2IjRilRv62sTyUwhvvJPpTlouRH-1DTS3PyVSK5cTgI_lza4k5YlZKLu65kf1pZqcLbTKNSoviLrJtp11L_ODt5OkRt_XXCY83Nqmrkwr-lbeRAlMVkex1P9oEFNsAYCUdQ8wuF3tzVNUqefTvyGietg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiO57kTlbLN4hQAvXqwG3PtzmrUv2TN8gMplHf8Kbk_6-4HNmScujGKBM-lvhjIond2s21-ZBWevKGV6W-sidoM44CKvH1iWZ1UMfLWbRWpLe08aE0T_tr-Y58ZQR1K1fwhZFsG8JcYox2eWfmEINV7BQxLcBluQxQr1NwAuslzE2qlXG3DBt7E7O_sOPoxYfKPJ9IfTeOhGIR8ZWCmjwhKqJlufpz9Q6cJnpViwrYvyQddAAbmEbOQ2mkhRYKvxoZ74KwawoPKl_XJUaz1jkkn5iy7xeM701nH44AuBEONwKHE1PyUYSVMBfcMhPpOHqfIwocW40aYIdGLDDuPvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA_po7D_S_6tXSlK0q5ckjJzkD5SJK9eSTeBBHZ5WEJ_tLUccd_Ux-Y-4eG66intZmXXyZBjg50nN6ahShgdxMPZDFNnbpk-jkNuo4spYnNHgvA0SzQgj2Gd3uaJyCAgT4l3VYlEI_y1aa2CJwAorz1CwYfkTtkH_c53Qj5l5-saWzVW9WFMVGTUxB2HLq6F-ONYP3t1GmySE_qR8XMBog8ozObGSxRu3VVWtDyiHVsjhOj9C9qbyVQzjTjyWBwkBpEg2eV9OkfFo_f69sHXhofBkDMAb9EQ5CnacIJLikeuv1dmkrP8GqyZrxCvUiTE3eJZi6CjT-chU-0JPfWj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ai27r3TDevEYrw2EnHgAgL4__-yplwVZmf6QUdccA2kg0nLwfWcxi7CF7NStHVqf6Dq4YeWhsnf7LUMylekkY5WPBFOQlHEyPsVqt6zGnHt-iN9wHsHqBmnLW-Jt9JN7gMpQUp3szYGoYvNCTJtTqHkavKLwClNiSldBp9-5V8yHUVEB-QCaIPBgOoMqHafGmw9nXPJSdQHCzGyLyCIByL9M8lTkmGKQvGbj18zxJSPk-1suDXa7RmjkwoyBQ7bSIWRIJdBJ0UdBG8cztPfj9iUstkkaIO0el3Av0zcdkH0GnPgVUJtI9CkA8ekoqI3p6TDOe6ES3t1yPlFSRFvBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfW_EOhdBIV4O4zqsu58w_Xnszz2yn5X-ndIoEvzzn1wL_fyARhsjQpgyyzDOqKpAaQY9WcTjd8mxyXVz1B3yRpf4ShRvVccb1pSh68BziQipaQ6EqbmN_P2ANfY8VhuTBTnMulIdeHIfo_rBtlNY14C4Snm7rzEsTwaFjLgied8fFuyd5Ow6tE08EYYyk3Tfo-bB6ORalcAEJE8S7u9BPMn2wyKSyG99Zta3bFoMh7ZJmKhX2FDlUmYyVkDiUpw7O3M_4SCCrIDlmlwTRKqfzQ6OTOJ2IW-m90caLapf-g85ai7D_48dMRB4XesGssRigQkfc9m56SK-bdtuX1n-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتشه با سرآستین‌های متفاوت و شیک استایلت رو خاص‌تر کنی #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/687923" target="_blank">📅 14:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687922">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600ae9e147.mp4?token=iXXzXbgXuxlMwq8U3CwalZYOJM6w6ZqoPp8fSfVNoDp36Ccnba_LxBMhWxcQnXmJFm0Bj6rRQmgXtO0ezpGke6ogThe22ig2oes4nP6x-4q8W5tUwI0jpmmnSzz-JfmR9Bh6fkcM2fjOJNZtC1P8fyfDM-b8L8DDLuS9QJ655N6r5Svr4cFrJfR2q6nXdJn1OklFUhQfrTPONNyQuacCPtVNhLEoxfo4beXhmqnCCY138VyZs3Ug3-UFsTPU5DohKgIjH_Vh9P9BdslhZho71XVYpug3kFoXIIPSD0rBFBzGq9br_FWvWBug27fqxiY4fwbnFT4xGP66c-xCcjIwdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600ae9e147.mp4?token=iXXzXbgXuxlMwq8U3CwalZYOJM6w6ZqoPp8fSfVNoDp36Ccnba_LxBMhWxcQnXmJFm0Bj6rRQmgXtO0ezpGke6ogThe22ig2oes4nP6x-4q8W5tUwI0jpmmnSzz-JfmR9Bh6fkcM2fjOJNZtC1P8fyfDM-b8L8DDLuS9QJ655N6r5Svr4cFrJfR2q6nXdJn1OklFUhQfrTPONNyQuacCPtVNhLEoxfo4beXhmqnCCY138VyZs3Ug3-UFsTPU5DohKgIjH_Vh9P9BdslhZho71XVYpug3kFoXIIPSD0rBFBzGq9br_FWvWBug27fqxiY4fwbnFT4xGP66c-xCcjIwdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پیگیری وضعیت سه خلبان سوخو  سخنگوی ارتش:
🔹
همان‌طور که قبلاً هم اعلام کردیم، ما به طور جدی خواهان روشن شدن وضعیت این خلبانان عزیزمان هستیم.
🔹
اقدامات حقوقی از طریق وزارت امور خارجه و ستاد ارتش با طرف‌های قطری و طرف‌های بین‌المللی انجام شده و این…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/687922" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687921">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ثبت سفارش واردات موبایل آغاز شد
🔹
امکان ثبت سفارش و ویرایش ثبت سفارش واردات تلفن همراه هوشمند از امروز ۱۶ شهریور در سامانه جامع تجارت فراهم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/687921" target="_blank">📅 13:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687920">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
هشدار درباره تبلیغات آمپول‌های لاغری
مدیرکل دفتر پایش و نظارت بر مصرف فرآورده‌های سلامت سازمان غذا و دارو:
🔹
داروهای کاهش وزن راهکاری برای لاغری صرفاً با هدف زیبایی نیستند و مصرفشان باید با تشخیص پزشک و متناسب با شرایط فرد انجام شود. مردم نیز نباید تحت تأثیر تبلیغات و توصیه‌های غیرتخصصی این داروها را مصرف کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/687920" target="_blank">📅 13:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687918">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285cead3c.mp4?token=IgpbUuL4lmywaGFWxSh3QXDPWQWuGoldRkKPJ9kb-Otr5p5BgT4VQpq8RHjiwqzMXl914ymHL3f50ctwCaTtyN8VdLBqXXrnvn44o9JW1XF1eS5wnpERQv3x80Z8kOlRvghbUQoGsImDwDEOTkW5ylsUrF0Ek9r6LIIsWdF83267IkBmCmEdkJaevw3jofjJTGjzqkCkdSdAschYOJhQ6of6B-YcTA72V8RaEC3oQArNVdLYIyAil3Hnd5OYKvbk5xD6mTPyYXoVVCOr_Y4hGz-X3JWPSOv_b2Kj1hRjUecQNQQ78QBiwNSHEzktg5qJXpJLXi-Uc5KHYbdaX1bwbpAarUS-mmp-ajyXFu-V46W6p1yK1SASJtyv9OZIJ8D7uFtfEpu8eXliCWGbPUjqGr-RLYEq7D9MttVJr6gb7e-hwNFUKGVtYj8h0m4TMf6j-EGK6h1BpVr65ls4fGxCzeSW9qqO4GFZlsjB8XrEpD4bXW7ug4o3xSMzFzvnZoGdCRICu7jEtwT2jTwEVaWl3qMke13qRIRU_tkJlXH7w1qSQLXEMtchfBKV8WiVic2UxIOhdxDDIHj3WHwQnoh-pGAm1VpWmt4Z6s9pNJu9r5H0qo-LagAAy1lNOYJkUWZVC0mLsSdbfFYyvwOJylb_N2cLuRygYNgB2lYPH_xA7fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285cead3c.mp4?token=IgpbUuL4lmywaGFWxSh3QXDPWQWuGoldRkKPJ9kb-Otr5p5BgT4VQpq8RHjiwqzMXl914ymHL3f50ctwCaTtyN8VdLBqXXrnvn44o9JW1XF1eS5wnpERQv3x80Z8kOlRvghbUQoGsImDwDEOTkW5ylsUrF0Ek9r6LIIsWdF83267IkBmCmEdkJaevw3jofjJTGjzqkCkdSdAschYOJhQ6of6B-YcTA72V8RaEC3oQArNVdLYIyAil3Hnd5OYKvbk5xD6mTPyYXoVVCOr_Y4hGz-X3JWPSOv_b2Kj1hRjUecQNQQ78QBiwNSHEzktg5qJXpJLXi-Uc5KHYbdaX1bwbpAarUS-mmp-ajyXFu-V46W6p1yK1SASJtyv9OZIJ8D7uFtfEpu8eXliCWGbPUjqGr-RLYEq7D9MttVJr6gb7e-hwNFUKGVtYj8h0m4TMf6j-EGK6h1BpVr65ls4fGxCzeSW9qqO4GFZlsjB8XrEpD4bXW7ug4o3xSMzFzvnZoGdCRICu7jEtwT2jTwEVaWl3qMke13qRIRU_tkJlXH7w1qSQLXEMtchfBKV8WiVic2UxIOhdxDDIHj3WHwQnoh-pGAm1VpWmt4Z6s9pNJu9r5H0qo-LagAAy1lNOYJkUWZVC0mLsSdbfFYyvwOJylb_N2cLuRygYNgB2lYPH_xA7fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا اسکورت نفتکش‌ها برای آمریکا به بن‌بست رسیده است؟
لوسیانو زاکارا، استاد پیشین مطالعات سیاست خاورمیانه:
🔹
اسکورت هر نفتکش و حضور نظامی آمریکا در منطقه در بلندمدت قابل دوام نیست و ادامه آن برای واشنگتن پرهزینه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/687918" target="_blank">📅 13:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687917">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو: یک میلیون دز واکسن آنفلوآنزا از چین و روسیه وارد می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/687917" target="_blank">📅 13:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687916">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
لغو ناگهانی بازگشت صیادان ایرانی؛ امارات بدون ارائه دلیل مانع خروج شد. با وجود صدور بلیت و انجام هماهنگی‌ها، خروج صیادان هرمزگانی در آخرین لحظه متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/687916" target="_blank">📅 13:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687915">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEmZ3TwBEBT-9cz0-dVE_IGW3k39miV-d5BhJGYyeKb5l3TzbYgJqJe0SaIvua6ZFxASFPSVb2R2-N1e0LJ7J-owRel2g4QTZLguntdbjLmI3p-oTOMdzCY0kEkyLIh4rtlfTsMrvLZU3sZh89gd0p3ksyrx0QOyiZRNJL0pmWu5-BUek2Ls8Cbct0UdGadK6FfGihtDAn1jZQZAINGgMUSlGIgWr1eq5wsVFZftDD51NCnupa2IXnKnXQ2sUA4uHBZFDJER6nc6S3_SczG2zoBw2Rz7ock5aeyk7-xby4CA5IkFk33CeIVj1ZG9rKuKP7rUwGpxI8zpJ0EJa5fyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا آسم در زنان شایع‌تر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/687915" target="_blank">📅 13:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkkTcsNOqaDxnpbZT5a1z-jMBwVkhR0UsNaoFYreZ1LsPhr2wV5Z0_PD47pmR9Ykwsqz6ut_qIIFOM-J7mPJxKPR_Ge3BsjOdxbmHEhTV49-CsOQGybjMnr3P6yA7KcWNo8YulJ79i642RShXLJ-vgbqWmMMZYacLSu_yMpGYBNeBirDQ2eMrvMV9Gna41EOWZ7WN7GqBIjVcLOCxiL7ce8e1E3NfzrtHxBrwaW5PJEbiF9Fn8BVTt5bAtbe_xenfmIaVBtUr0iaGBQU74_5g7X8cbmmA1pORjvrLNSjSkFBdox5-3TDB8vORHViN6ukQs8nLUcI-aBf7HcOAgRt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDj0__H-XrdcAEfpg8fb9AjcL0e4sNx0XYLcgNU_z4jOwGG7IblbPadKDc33pRffi5iZBNHQtRD_B3BW-ZuZ_AT3otDtBHpuRMqgUKcV630E7E_WDGab0aWCStri_3JX4QLxLQ3MK7snY4OoMTUa4cZYTsfuP3AneMa3T_e0RtM2DbDHJpxOw_jyN5j4-MINAEZLYmEMciYO-Rv2JBfrL9sdBhbzOCitMJ-Jj8E5KGxjt2oR2ezuug2jtXlYOt-RBB3Q5O5ztC6hIMB6he3wc9uQEVjOSy3u0K66HZ02bGZE270nqLrQ1hQhXOQ814dmpIFtx3o-bEeo4ySvd7tsuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو روز تا رونمایی آیفون تاشو؛ شیائومی و هواوی از همین‌حالا رقبای قدرتمندی را آماده کرده‌اند
🔹
شیائومی ۱۸ فولد با تراشه‌ی بومی Xring O3 و رم CXMT عرضه می‌شود و ابعادی نزدیک به طراحی منتسب به آیفون تاشدنی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/687913" target="_blank">📅 13:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رسمی الکام‍‍پ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb7e2fb20.mp4?token=tI6bF75CPRr0zfIzUOw-2YKqiOxxR3lUa5A42pXgpjLkHOCmojrc1wn8au3_YOo3WEV9SGiAVBcIRg86N8CiMZrmTcp5QNr8q0CeFlPhW5BJu-R9qB5Vfxs0qQ_HZz-rlg1UvYPARjmqFX7E1UfroPTEBmJlKRY6j0vOE27s5g1t-tXDUOyMjZSiX57L8C1lyNlZZTGq18nsKY2W0dODeYwvr8g7KT9FXHTiy7olUkdXvgga8-SVxLHqV2CDk6GK9_jQfwGbQqGIo6e-4snD93g10coZGUYbSzBTqGphd-18ELs-oxlsgOyMrZMk3keF-e6VtpNkEijXLHbuaCfVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb7e2fb20.mp4?token=tI6bF75CPRr0zfIzUOw-2YKqiOxxR3lUa5A42pXgpjLkHOCmojrc1wn8au3_YOo3WEV9SGiAVBcIRg86N8CiMZrmTcp5QNr8q0CeFlPhW5BJu-R9qB5Vfxs0qQ_HZz-rlg1UvYPARjmqFX7E1UfroPTEBmJlKRY6j0vOE27s5g1t-tXDUOyMjZSiX57L8C1lyNlZZTGq18nsKY2W0dODeYwvr8g7KT9FXHTiy7olUkdXvgga8-SVxLHqV2CDk6GK9_jQfwGbQqGIo6e-4snD93g10coZGUYbSzBTqGphd-18ELs-oxlsgOyMrZMk3keF-e6VtpNkEijXLHbuaCfVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#توان‌تک
از ایده تا عمل برای بهتر کردن زندگی برای معلولان</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/687912" target="_blank">📅 13:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687909">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
فریدالدین حداد عادل: زندگی آقا مجتبی بسیار طلبگی و ساده است/ در قم خانه آقا مجتبی ساده بود؛ کف خانه فقط موکت داشت
برادر همسر رهبر انقلاب:
🔹
زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰، ۸۰ متری ساکن شدند.
🔹
آقا مجتبی در علوم روز، کشاورزی، آب، روان‌شناسی و علوم شناختی مطالعات گسترده‌ای دارد و به حوزه‌هایی مانند استارتاپ‌ها و کشت‌های نوین مسلط است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/687909" target="_blank">📅 12:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687908">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFbG-vP48hY7OeBUR6TMAxcUcInmUTtWKUPuVmr3wk5FynlCXjgXaIu0o6anERpUTukZ-yeHP6xLKW2OyimtE2xKiQd8q7SzvUou_94wLPW9qqF_QYy-Jij9FFgKT3qLmq2UZvI1JG3ifJZosm6OcQldunGFR_yifi0_WE0Dq_Z2IT8b4e48sm0H2g9_NvMf0tJYDT-7oyKCj0HRiuMc5KIvxfGTJOrlyaAM9-FCrEMTrX2H6Y89a_euGyHyt9FVuNVJhLGPKQ1q4f7zPq9SlZR5IROFd8APswoE1BtV0NV9V0ilnB3zv34VttVAN0iRNDEdplbgnUtpkuBO0VDt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۶ شهریور ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
بازارهای مالی امروز یک روند متفاوت و جالب را به ثبت رساندند؛ دلار در حالی که روز های گذشته را در مسیر صعود می‌گذراند، امروز کاهشی شد و به ۲۲۲ هزار‌ و ۸۰۰ تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/687908" target="_blank">📅 12:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c018ba1b33.mp4?token=oqNtjNWElxPTuHpKTOjkzX44WjWbgpbzbqSIDT66rUzAcsp-o6NkuU0467cgtOucOK5sK0WcqgfXIDA8AwRTR2fW9xl4jstY1YbrYkqH0PFxWRopzGSG_geJlo9ZUMvFAaEnRjP8VUAFJwJlPG_pT949SPHqnKG1GmVwNw0JFbvZ1RHPmCEHwFHkjGjaqpbPs2DPrKn2hdJ5a-dg2AzrXpYYlk3ErXcLWWBPKUL6qfGjAreLjNTOfERTwqtxFbGPrVDHgCazvCca0-qfKV_m7ch09mCg-1B5329jCvSiKDjOnM1qlWw9MmJni6iN_zsGE901ztzT1cIAKr-RbqOXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c018ba1b33.mp4?token=oqNtjNWElxPTuHpKTOjkzX44WjWbgpbzbqSIDT66rUzAcsp-o6NkuU0467cgtOucOK5sK0WcqgfXIDA8AwRTR2fW9xl4jstY1YbrYkqH0PFxWRopzGSG_geJlo9ZUMvFAaEnRjP8VUAFJwJlPG_pT949SPHqnKG1GmVwNw0JFbvZ1RHPmCEHwFHkjGjaqpbPs2DPrKn2hdJ5a-dg2AzrXpYYlk3ErXcLWWBPKUL6qfGjAreLjNTOfERTwqtxFbGPrVDHgCazvCca0-qfKV_m7ch09mCg-1B5329jCvSiKDjOnM1qlWw9MmJni6iN_zsGE901ztzT1cIAKr-RbqOXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسروپناه، دبیر شورای عالی انقلاب فرهنگی: پدافند کوآنتومی نیاز داریم. پدافند متعارف جواب نمی‌دهد. لیزر کوآنتومی باید در دستور کار قرار گیرد/اگر ارتباطات بر اساس الگوریتم‌های پساکوانتومی وارد مخابرات شود، دشمن نمی‌تواند حمله سایبری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/687906" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diUrb4S2hvHR9CV1FxocVIXSeG8ax9iFJ9BTlSFMx5aM3ZZSZYccTjhVe1rso1WugpIsTTS9zSqhs_Oz2TpEUV8FUsNB7QX5eJxirS0b7L-T7O1aFUshW1oJfdTjg-qgsXoMHwxee5lTMHeNpd4STfzTKh1UX7dARmOkUa8i1gzPhl2pZRZIFmlz4YjcZ9eYGyEvnUn9XV91_MBp2gWyKnM5JYd6Nca10Y2pkWt8mGZH7ZYhd_s6QKHXPUNFvHB0vw_2BaLMd-i8Gen5fKBJCefQFTPv4gl1Z4RdNyuKtYB0hklG7jhnOsnp4YgfaN7Y0HLFo4_GK3Yh4pc2cjiADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl1nLtGNljZruhR3vjOdlwJs7sNqr5cg6-kfb88pYU1-oahTG0Fb4AqC868SISBsdAUkKHMl1k_hOlPyBJockzLn9FhRRxyorwu9anJ63KfMtD-EB4PAxy0Mn8OliLXcK4dx948Gu6PRhjFGQZVX_bnXIpiFvMczYaIysiZ39ETPKGy43SzyKxY62dc78PHXp01xxqbojcDhrK7zon4uuC2kcNbTh6WlRot6PhzdOj_4xEAWhwvipIkky6eWBhS5AXZODyu66ZWwFKs74q1L2dVKzv6-iV71ksG38UjpIymG2pFHpGp2hMz5p63oqhj7Ceu-cOQJJGVolfvQBaKREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oviYj2WNp9htUYV07PWsyakxGyIrgmqySD5gwuRFJRQdfOSMaXOkxNU1m6lfilIYRdjmc309NSw_HcM1WvgapwGYkzULqUPKKEIIicZta_uFE65KTJI1HjjxTv5J7m9dBCZuApgmiHMmhSrdSCgtI8zHzCTcTpd3XlFO5e84aPeGNuqKXlM99ihHnyjKzf7JXN0E4DLfw6SpsIN0LXET-g-wOz449pidfQcfI7tD7aG5F-gSBcWHWd8oIjzsueQPwEFuRUdfD243JwLShjjjW4HMN0_XBUESSVzmthnd-Zf58B12vKYAxrVfsWM1f8gXmdSRTCVMS6TNcIUjTGahDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXjisr6sqLARNIWXWmbGsSDskiUjT3-kw4DQrctN5p7xYxvoYI91hbJhz-yUMAdQkgmTVG9DVUD-tm-PwiJunZHHFD12WpmxIXphK1Crsy-44Cdt6TgRPTVYoDkwuZfdsm0YLBNd_0EymTMmi-9EGGC_LuUEnwQtfNTLg0TzLuX1XFVYOILcmHApa4lXUEYsW8hrCr8O9D5NkpsTll7_-pns-A8q1Rj6oiI90O3i4IRJiY1P2vekPJ6grzZ0KzbeMazHNegQbbV4o1LU83Kf5L_sX3KAQKKfyR8gS_Va9gaQaUbm3gIQfcAO1_-QXRkmx1Xtc3kaMfSGL0DsSUTWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-tLNnoOW6UyeKcwKiU5iPIRLRIwbJF7hPRzafzTwyNL80u9HHORuygBfGDWBYgWMpxNBnxynSrA2SSs2IE1YvXA8RBbddXQGl4U0wTaQJ_AoBtL6NUTU4E_m4hBGI_wB304rsZRBH8G_K34SM7FG4PSWdmg5oTlvg6ckJk7O5IImy7IoN0xIs6vPrmg3Asi8dHN8G9vGmkWuFT0ZvuPmsGMrRu_SECInFft4JDJF6dyHquZKBIv50WqI0uHEFsZ77EGUu70-6jcgamuh1CIc3bID46bWZWrrDRY8cE4EhaNIppRHot_28Yc5ceLVz6f_uNOazBWnAgAZNC2lOQOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vucoD74p-DXDreKMNGDTYUngqZsYFa1eV4ue_Uq7JoW3_qG13EV6lfBv4YgO3XE_nh9zDKrxmLQUY-U2DFz0rF8YwvZt3Q2g59Q8GR9paaYG-odWrfKOwpZkAj22TvoF1vgSfnFnx66nRkgpHCgS7hEbcmO7V3CZESDl4hdVMgKIdtvqHOogTfy2zFWvS-TICIDAvXFurni6QhODQxmFO5A83yHxgywPkoyT9TnsuvGJorNMlRQCa9uX5YiX0lkuPGQCpW_hz4QlI_bx_3CRtHKOfyNsaNZzOdqEmURinqOidlw2ZbqDAFaqeDuoA_BENeJnfaRspOKfggIZEuwJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKqNrdJFBYcYLlePgy2IlKX9nY-pPpVNwaxL4VxdCq-oa4f0gvWSEOEerfJIn8ropy8GFjXDzM47SyDfTTPEtxJB_b9tTiy1BkN5L4rK8QR7tM4cxStVPWW7Ia0vHhKxyW5hM6h6t6wqQzXJFsnjsXqj5qpMb81R1AQ4sBbgzitR8vA1AsA36DqkIPLAa88_UivNjWFSVwUFSw1f2Ku_oiNjjYL4ER8bQFnDu40eIGYFZoucKqC58Pe7mi0Jbf2_P9_BcPKm_JcBon6PqBrVwRFP0xmyOsD8Z5K4VM-tMYtdBVqrxAxnNqsE0PBLmImj84vJCgoe3nqc67S7K1M2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpXndGgMSjsehrg4ukoVQ_R0uVLdkzzLrpXqSCAscSXPTyq3Xw8ofK98SGADPpUOmBN9ov514C5rA9M1w6JQgcxsQbDUJKMNZeGTRpJpujYNO3g4uO_N5mKgVHkHvc2lMtiAhUK9k8hnXGUQeF2_TznMXvD87fBis5QvLUfiqsPSzbqWHa_SD0w2EmNAEr1J52LJjbMFH9KpaKXl_FVU9QClQGvMnMBTyEWpvz6ez5lmWYpMAengefQuSvVD-2hU-1CLLOu_uz0_bo3-i7J-OD9FyM-Dh9umlWxs1FveOrW39DPLOxopjZXjpTKcfdNjCowGmK2nsfMxNHQEE3szgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8vuSxtMeagRDTaN3xeAQTPyvwoVCPj_Fab8bZkEwB-tRXwLBzBtjTVirksHIc-WIA2K2cmbEyeFhXi92cg1847E5sn2pMHHfyWlxVkOHYI0in8Vi83qqoa9bFT3axR_2sdOuetUVKtaFZXS5Nakw69023uYSAR1okF2uNveHSH_hlnxuva_rxgkTm4rVfoWHt0b2d_At8WXhG2d3uKEtxhSaOJUEr5_t8VQJ1pwG6l-v_wn-n1s9FCRrANHKAJswAn155iDrEc0bFgKLu62LcFXX6yMupp98Fu7WZJUgbcapobrHGuswmjqedhN7uFsGjOFaRgdd-P2dp_mZ6PdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUtSiv6dSJP3yfbWjqnJrjvFYeUW1LM5hWO1E7yIHd20aEW0aZuy3nMKcoAQ5DQAoI4hlurK7-_m0iMXETB6J48Z3XXNlEMnmgfNV7Z2-L2rgt-CJADyLD9zHBWYhfTJrWdJRZvvhMLN8dILcF0QbqfxwQY7uwTer26H7PLvgyD1CUdBWg88wQgCr5OahegcfI-n13puLZlyRN3-kS6SuhFZ5m-nj3wR9zn608_k1w5Rlv5S0WRNKdrCi_OsV6oSNib7A_WbV1AeKI0o3HhH7lbviAS5uMqSZCpV20b9xHHTEOkz1t7BXMl0t5RVWN0Iaqk-WtWW5JvOIlKnKhLAwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
بازتاب دغدغه‌ها و مشکلات شما مخاطبین عزیز برای شروع سال تحصیلی جدید
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن کوتاه  ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/687896" target="_blank">📅 12:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687893">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vix8vp-v_4Qh-_7HX84lk11ynf7JN7fmr51blP5vHY7Ahqgo3ktIKV9TJqLl7OD7jtMT6Izt9cR_6wNg-T5CFahis1hzjW1u6UowX6HG8RA6tahSl0zEpN1WahhFq1UujFNniP-_kZypLL6HLPeQjXuTZFpGNFsRLaaNPeT4VgqyfQzlBQ5mM11K-104b3BruBbbBGm2mi9pjAp0OcW7TvhcrVtoY97J8RdUs-eDgJA7l6rUKtIu-50Wes29H-TeRZidm1qL1eyD2c-TIgcLa1bz9gUG3hRyyGMAaU-R2PAtoNgxjLNerizEdfBcVa-aID2HVNWRHjb1hNrxYEeDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-laoC2gHSBi95f0PCLySQeBaS70uiKPtP5itA1pzVGm5Pa1Oo4Q6CeggdskSGibB2-Y6tf21fVHJYpidM0NPRnvvnN4e3xiCRS09lnFghBmUncdzdwsckMiOhLUR1GS-ZvKQ-DMvg7UVbhCYZfYOTSCa2dchVKO-v1Vy_b8toIrVURx5rKWNbvlYHlyEQ1fd1Pt0tXy5mjRyubu2Soz2vAxsZG7ODlCapOm5625ka1KjlUoFGweBn3fQVLQ0ebVWr13tWJ8sS24TmAZnO2D5RkDDijRfOYtkwa2lx4QhJ0DSs_5stIGamK7OyN40mvV0S-Br8K_jVYuxw9zjfrrGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac8da80b1.mp4?token=ocQqps7ZXYA9En6tE2M0AhVYDaRPBVDzzc_lkfPRGVBHtKsDwfSkOhraYDKXuf5ap6MGo57p2wi2m7ycakhVDIJvT-50hwFtbf78vngCfpN8s7uYohK7BUSYNw7Ifx02ML-6tzp9BNaDK-FvlXHxq1zFQ3GgCvhtFTlUUnEJUUQceXJyVXX7WmvssHkSO-W2INkkzNPl-lTqPEAWHgQDimQ-wlUvy3oOXXCFJLhZIlye3HfsAT-3n7CEVzw7WKHSCM0tHICYqM6WYFm2in_vFToaaa9FXWlkIq8Mqe0-hnXh09vIxhqO4xf9dbcclUtUaX92a7xv4tde9yAeteLhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac8da80b1.mp4?token=ocQqps7ZXYA9En6tE2M0AhVYDaRPBVDzzc_lkfPRGVBHtKsDwfSkOhraYDKXuf5ap6MGo57p2wi2m7ycakhVDIJvT-50hwFtbf78vngCfpN8s7uYohK7BUSYNw7Ifx02ML-6tzp9BNaDK-FvlXHxq1zFQ3GgCvhtFTlUUnEJUUQceXJyVXX7WmvssHkSO-W2INkkzNPl-lTqPEAWHgQDimQ-wlUvy3oOXXCFJLhZIlye3HfsAT-3n7CEVzw7WKHSCM0tHICYqM6WYFm2in_vFToaaa9FXWlkIq8Mqe0-hnXh09vIxhqO4xf9dbcclUtUaX92a7xv4tde9yAeteLhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👕
از یک تیشرت ساده تا یک کسب‌وکار خانگی
🔹
کمپین
#چرخ_زندگی
تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ چاپ طرح روی تیشرت رفتیم؛ ایده‌ای ساده برای تبدیل تیشرت‌های خام به محصولی جذاب و قابل‌فروش.
🔹
با خرید تیشرت و مواد اولیه به‌صورت عمده و تعداد بالا، می‌توان هزینه تمام‌شده را کاهش داد و در نهایت سود بیشتری به دست آورد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/687893" target="_blank">📅 12:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687892">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو: یک میلیون دز واکسن آنفلوآنزا از چین و روسیه وارد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/687892" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687891">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeP7ycf-TkGf5-cNoywmp2Ce3L2WkfUCKvVKuvrkg6jqm4j6N8n1IZZHhG30jotx7svYhrA7iS-LRPwf44Mmc01SDyUNjD41q5htJmHx_g7FxDkh9x7JKplMA3Go00EBpgwFnh8uwLCQspR-WwosJDjL_76OmgiqM7WQ3dDLJ6m4MSKJXqb_1TB-t-05E2PnxgpilNB_KsVML6O_0x0CE9lnDYppFPnXhE4pyv4I_AUFuDphoKzy1HqtvHtkUA6RlLwAHV3rKBUxQGAaZ1RODJhIQunCkY_ys-BLkssVTFVOnKiPR6g23VkEyZfwP65f0-URlfUS0EoXwWKrd7OtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵۰
درصد مخازن سدهای کشور خالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687891" target="_blank">📅 12:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687889">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدمـاتجهيــــز | Damatajhiz</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=mJuos7AyY2J4oOgWDKEyHHKIjXL08Zf1JpvSOn2F386mfqr-UO-yFwx_1Tn019WD24dDSkbWWkPWyKO7fzmTl-wZlnpMJS7QxJPBZvPkGAiDCcSQe_iODVZ5fR8oyRpkML9E_IaFOGLmP_Ij2RP1hl5a3UwtjJUTp1tXszePUe-x7kPd0Z6WPgWC3nYmHPXNHYlZ_LhSr0D1a3TTV8goM86cHFLFDhDGytUzRs438eyyoPMM2ChAE3uWXK8-t757w8KMbKjkKIncwhDzbix4PhCl7x0Wai4VUltI4d0ux2ro8VKyCukVleSBk_Mjq7mlXuh77Z53gjjzp8yx59t0Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=mJuos7AyY2J4oOgWDKEyHHKIjXL08Zf1JpvSOn2F386mfqr-UO-yFwx_1Tn019WD24dDSkbWWkPWyKO7fzmTl-wZlnpMJS7QxJPBZvPkGAiDCcSQe_iODVZ5fR8oyRpkML9E_IaFOGLmP_Ij2RP1hl5a3UwtjJUTp1tXszePUe-x7kPd0Z6WPgWC3nYmHPXNHYlZ_LhSr0D1a3TTV8goM86cHFLFDhDGytUzRs438eyyoPMM2ChAE3uWXK8-t757w8KMbKjkKIncwhDzbix4PhCl7x0Wai4VUltI4d0ux2ro8VKyCukVleSBk_Mjq7mlXuh77Z53gjjzp8yx59t0Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
دمـاتجهيــز؛
انتخـاب ،قیمت ،تامین و تولیـد
تجهیـزات تهویـه و تاسیسـات با
اصالت
گارانتی
(از سـال ۱۳۸۳)
داكت اسپليت
+
ارسال رایگان تهران
كولرگـازي واسپليت
+
نصب رایگان
👌
فن كويل و تجهيزات كنترل
🏊‍♀️
استخــر، سونـا و جكـوزي
🔥
دیگ و تجهيزات موتورخانـه
☕️
تخفيف ويژه
دمـاتجهيـز تا
15%
- انــواع ايـرواشـر
- بـرج خنـك كننـده
- چيلـر و ميني چيـلـر
- زنت آپارتماني و صنعتي
- هواسـاز آپارتماني وصنعتي
🌎
www.DamaTajhiz.com
☕️
☕️
🙏
☕️
☕️
021-88822550 خط ويـژه
Join
🆔
@dama_tajhiz</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/akhbarefori/687889" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687888">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=Lr8ZXAmcGkUJxZ_Giqz-eyDXsBGNbtYtWAlEYSboE7b3EMW7wooWUrtZoo8IJE8TYkfVUXd0RrysKDfVqHYxblaHfILF4DDeg3PceAQQuWcvNjuFM0Lnn7knHnPvq0qJckRUiE2Hj7qQ2Msf2Wu8a5F8UKvi3KVB_PVKJfGAiaj2_S3jE_GDympRI1lT-oeNT2C_oVGKf6upmHh0a4wnAD1EMfHPGzNbq4lOSlhkMxwAiHvrCDTh58LuR9-Z459FiUOMxs-lfMCFILu4lnAZyR7iKp0BnTdDf9InHRpFVuUrwMl9HcxC7BudwHf5BxUo6ut5TZeiGloSANYiSewbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=Lr8ZXAmcGkUJxZ_Giqz-eyDXsBGNbtYtWAlEYSboE7b3EMW7wooWUrtZoo8IJE8TYkfVUXd0RrysKDfVqHYxblaHfILF4DDeg3PceAQQuWcvNjuFM0Lnn7knHnPvq0qJckRUiE2Hj7qQ2Msf2Wu8a5F8UKvi3KVB_PVKJfGAiaj2_S3jE_GDympRI1lT-oeNT2C_oVGKf6upmHh0a4wnAD1EMfHPGzNbq4lOSlhkMxwAiHvrCDTh58LuR9-Z459FiUOMxs-lfMCFILu4lnAZyR7iKp0BnTdDf9InHRpFVuUrwMl9HcxC7BudwHf5BxUo6ut5TZeiGloSANYiSewbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
🔥
قیمت ویژه امروز: 1,089,000 تومان
🏠
پرداخت درب منزل
🛒
خرید
👇
memarket24.ir/product/brief/26903/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687888" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687887">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fc067d.mp4?token=qPRwaqi3qE3MDRYxnLIrfOs2RBSTbqnFhQTfJB7uQ8V4f3Y-BPfmVsWl58DEBSBfxawGnz1Z2LyN6ilQQQKTQA7KaMgGWyyIK-NbTHfIZ3rUajassY3PB735WrPo7AVbBt7rkzDM-2jDbVGbX9Bx8sXeh-f6MPA4Q-WUvHmyObrBambW8l6RnjyhE5H6hI-I5g_6Dye-WlrQReRGcrN4t1_cUqPXjrM5Thv3Ouwiuzo4CHYvtvqv5QHWMD_tPfgguD6ALwtNaSVacTN-NmtUawlJz7ky-gEd7_0vIBO_nv_YYwFf1wYF76MUYdhTQDcKr4F_aLhKwA-Erj-jj-dvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fc067d.mp4?token=qPRwaqi3qE3MDRYxnLIrfOs2RBSTbqnFhQTfJB7uQ8V4f3Y-BPfmVsWl58DEBSBfxawGnz1Z2LyN6ilQQQKTQA7KaMgGWyyIK-NbTHfIZ3rUajassY3PB735WrPo7AVbBt7rkzDM-2jDbVGbX9Bx8sXeh-f6MPA4Q-WUvHmyObrBambW8l6RnjyhE5H6hI-I5g_6Dye-WlrQReRGcrN4t1_cUqPXjrM5Thv3Ouwiuzo4CHYvtvqv5QHWMD_tPfgguD6ALwtNaSVacTN-NmtUawlJz7ky-gEd7_0vIBO_nv_YYwFf1wYF76MUYdhTQDcKr4F_aLhKwA-Erj-jj-dvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله غیرمنتظره عقاب به یک مامور پلیس در بازی‌های جهانی عشایری در قرقیزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/687887" target="_blank">📅 12:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687886">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162214e774.mp4?token=TZzIV4m0-9os1mUdtJU9TOFiQRx5osQbA33QX9RZoR7iP-XdawROYKcWdMsXscqp891yOLj27HlqaOcTwk0r5w3lpPM51JBKCE5K_231EWjoN2vOPPFALLf79gY7-VgJPv8ZGqRGRdKLdt7TUWY-im58n-dzWWE7W0dpUFlAPAUT45gZi0EunvILIhkfAPmZBzd49eVwexdRjsbCeLwpyQZ7hiw3Fq1BmcZGEu9buYYSuqTlESOx3rMsW9VbzVAdlJtNPa5k7tzF-_0cgPeLcaGA8Awp0LouGeMVstonnle1ebyomi2Oi20-tNKSJkr2ADDl-_arle1km0w8k24hxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162214e774.mp4?token=TZzIV4m0-9os1mUdtJU9TOFiQRx5osQbA33QX9RZoR7iP-XdawROYKcWdMsXscqp891yOLj27HlqaOcTwk0r5w3lpPM51JBKCE5K_231EWjoN2vOPPFALLf79gY7-VgJPv8ZGqRGRdKLdt7TUWY-im58n-dzWWE7W0dpUFlAPAUT45gZi0EunvILIhkfAPmZBzd49eVwexdRjsbCeLwpyQZ7hiw3Fq1BmcZGEu9buYYSuqTlESOx3rMsW9VbzVAdlJtNPa5k7tzF-_0cgPeLcaGA8Awp0LouGeMVstonnle1ebyomi2Oi20-tNKSJkr2ADDl-_arle1km0w8k24hxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای سرزمینی که هر گوشه‌اش یک خاطره‌ست…
❤️
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687886" target="_blank">📅 12:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687879">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiCjh94rnB6iiABzuPigPsXvKZ1WGY6MjduqvrHgCh3RPqKexCnF8hSA6Un7RtnT5XVKLv8_oYcFQejnnZURYow91ulgguLrmaOzwQIns8xAyGGQMJxs7EYO36fq0syp7ELkuE0XJlJXj8Qmr5gZl9hAyrZ4siHKcyZCxiXsyrpLGjaooJG4MGs3S9koqiCqYUIONJseKqP6SYuZmxiThLjBiXLvdAgODq4AVuwahHnoqh4eYh1Jiaorj-lxlqry2BoNXRuR9lycIJCRC3d-_d8p6dbTGxL6L0Lj2A-pc8Ye8PIpqMiCRB87VTcC8PUrN4Yc-OiqWBRjcgB-BpOqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8Go6dVwyzXw9TqrtErdyo5mSmLqonDl6U-bRgkKqzxk8Vm8WK-nDbWRbBwZehgFiRpulFEGqBsXibIZYrbl6fOl7GKbk4gs1SfDY_b4MtG4VGsdACZSTZglEpuHDEA-X09UELpulA3ZlZeWAY_YRLuKajMrizfFKp5foDGnKuxG4f9qmhS2PNV1n53ZdVMartZGmd3qZr13aCxjXSKYRUwloHwg0yg1GOOZ6JaSXlZgW5mLdjok58MbvAQ_ToTMDamorA7k4QjHiZMTs4kvfqS-3Zg8b_lBEOiQCELgnIenWb11OkE5rkgBVnKGpaynpjEUqoWbzYlSBywH2Qs10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7o0QOGweqq45kH5lcDVLzjJUq9NWce2lrx2k-7zY5LmDXaHg5GMtoGdATQ3_GWS726OznUkcM6NYwd53MkZlUWELu2JJLrsdMBQZ6uGDIocU1xvTgj2ODMGCiNprqboMRRZkZEm38Bm5naALT9Sta5xDhCmpAVka4NUlTRvyrIfFNoiPsPxT6DFkZ4hmOdSd7ChroEbGrcCESGqakdOH0DwykB6DRy1IF0aJIqHMg8ZGgO8AzNoiQkJW_mJLC4AGUuy0guA4Hts7_4ojSEUW1XcDS5P-d_4cX1aCH2SVJLopyyyQ7rkBAcuyxw_zi4Nl60iSTxXxyKnfD_y1BSACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiZT5yL3fs7h7inzTCHmnBvrEkoLLY1-22vdg9MaM8ebFm_2P0UXbyuzsUwQZEwtKFbfvu3sARuc5oCFjJINRGOihlUvfmGSSjw6VD--JW0oN927aEdDMgSlU8yngePidtiufxcUBTKsY6gWz4oi2jW7T8ZOaGbx-Uwofub2KKm5aExLMJJU_giOwuJP48aztKNzEoOy8gd1zZCBpbJubBwLXyeMZN9Eq6zSiZofPKtHXB4YHt74a9aVePlHS8RToR3IGFS5PS0v6ivqtNMHF9Q8r7ivBiNjC2AzcUkXcnk0vFslFJTba1ZUML1AkKOTgMUbAd0Ajnx5PPwC2YwXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXX7o4439w3SZTfU1gCSAeiNDCQOShVXHwWNZJOjamAESTZ-o-CKESj5TdDAD4UEKtZVTPIlhNRrg7-McB7PVXYUZeUqE2_JGiQAul9nHTkc-lq1-ZcDve1PBBreScwPN8jBB7yUDYpS4_SGF1oAI-ZTS8hzKV-fu7PyaZGQ0jousOJs8MCmSowWyNCHbV9VW4VrMXFo43PMJdALSPl5L80faY2E_dtRGj63WfhQ-WzFPh0MLnatxjAmtiCW9o8xFNKbdAzrGifW5kLmpfScyU66cqpdUTeHh9qxCiDCfb-TLMoEYP8L583xef1BbafWfieJ2tOUqWO3gV8M8LzyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDPBB1oMz9-6I172H1e7W6rOCus3LZWibSa8hVe9E6CR4FUd0cwOYLozN13KfqfUSKI33t7Hw4fjR0ISk9W_QNbvkaXeFuu6nkuOJykmyJSl8hWI1xSPTYudlDpetZWGScHtH57mxU-HJjV1ECzAjMXTGI6TKoMOxF0ByguAlhnvrRrYR-jVxMsB5zPT7fVoO_dHdrTbMljUGxPRItXA7zYoghAjMa06L4YjVdMpA71QjwgI3mIYbMsJf0sARYasrY817JJ1aqM7jZgQEhwqN2Y4NvR4Njd6bi-t9SYT-Ahq51bnSxJYUtEaImig-SSdUgoAF1vvHZD076Bs-p2Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LE8Y6-MI8yS-vrDwlCSd-IKfc4DJmxqY-9umZSGbCxn6LBWYZtKL4vFzFsTxawzwwkF9ddbNELeeIqXflySKTj1r3Tryo6VqPS2w3_XaLYKasTVU_VAvoEC9GrBzKONZyxBvnpScjvHv1NCfa8WpkNV0SIZlLFuEjwu0nCPLSOKzTHg04e7ZkZlx8nbMV-00n-8sByjSNr4-fCdiD-4tPNt_-lewLBozD9eiogrXqJoNlikqdCHsFJqP3IeZFXmIippZGCoBJCLWgFegyeYlWpGjeralp0dLifusgIatSkqA32hO9rcTxzpFZTdrXK26TdRLNPDZx1f0Z5OVdL8Oyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
باورش سخته اما هیچ خواهر‌ و برادری، پدر و‌ مادر یکسان ندارند #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687879" target="_blank">📅 12:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687878">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بقائی: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687878" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687877">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ9_vtd3H_Vp4GqnY83iO5HyfSunz-fEUHUBsrKFkRe_EtkcA8z5aPJ5AEDBDK7ZA7SI89Jtc3qVKv3bthdpUblP1wWBzIWO_L3NtOUj2-MMSwN9zN3lM_hPc5bjxVOZqHvb7prOA80juw0TjbSvR7SqkwbM72rdASLpE2s2BNeP1n9yK_go8ZP-8oJAI2FTktSqimcoKCXxgoGBuIWqqgEkxui-nf_1A4FLJSLbOdcMKkziS4RoHw1U9Hsqniu77CZni5WD3FbOvAVXLHD5UwKWiSy7uH2F4v6ZRfTznNXzHawDcjWYerAzv8RjcrHrK_JIRCQq8LDPOrshQjl8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موافقتنامه ترانزیتی و حمل‌ و نقلی ایران و عراق؛ فرصتی برای توسعه همکاری‌ها و بازارهای هدف تجاری
🔹
مدیرکل دفتر ترانزیت و حمل‌و‌نقل بین‌المللی سازمان راهداری و حمل‌ونقل جاده‌ای از انعقاد موافقتنامه حمل‌ونقل بین‌المللی جاده‌ای کالا بین ایران و عراق با هدف توسعه همکاری‌های تجاری و گسترش بازارهای هدف خبر داد.
🔹
سیدحسین حسینی گفت: تسهیل فرآیند ترانزیت و‌ تجارت، هدایت فعالیت‌های حمل‌ونقلی در جهت رویه‌های بین‌المللی و انتقال کالا از قلمرو دو‌ کشور به سمت کشورهای ثالث از مزایای اجرای این موافقتنامه است.
‌
🔗
لینک خبر:
https://www.rmto.ir/s/mfaonQz
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/687877" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687876">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVSiT44HnYAGaqbU0HxKydU2SV5lVcZw23n8jpDKOI8-pyvTGObxb-r8H_8dxWuVy2pqOW8SD_GdSX7oAwvuoeiRjHv4FYOn-7U_UaH8JkpxLl9hWOLs_-N2OXYTvCGoWBVjJsARBt6AkwvOi5_nC0IROIIZPreZKtLIcMXyL01IGbyUvbSo0Rv2xh0N1WnACn4T5AMtjmAldihKlUt_cjX7fjqPadEIZG8bl72zwVkJAuIQjuAZ5RxzmVjIdYQdcMhb2s1SrCXcht5Px7Hvf5RldOThSgRp4KwakM8UjZwWSTP9oXvQbrla0fXr8bw2_GAiTnYYLVN188A1BfQVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قالیباف به واشنگتن: پاسخ، فراتر از انتظار خواهد بود
رئیس مجلس:
🔹
ساده و قابل‌ فهم است: زنجیرهٔ تولید نفت و گاز در این منطقه گسترده و پراکنده، در دسترس، و آسیب‌پذیر است. شرکت‌های نفتی و گازی آمریکایی که در این آب‌ها و تأسیسات فعالیت می‌کنند نیز همینقدر آسیب‌پذیر هستند.
🔹
اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت. ما این توانایی را قبلاً ثابت کرده‌ایم. از پایگاه‌های نظامی‌تان که غیرعملیاتی شده‌اند، بپرسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/687876" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687875">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb01cf1796.mp4?token=awpXvvwM-RRr2lxgXo5VDYlI5NyzuX9QIX0W9XMSKTDYAwJ_q4Ke7YGzAtoxIbwpm9N5f_DOuCmPw9LRknrYxKctTIyIH7esbDGeg8N-q_lXCfWcwYBsVMQSW3NIeIIKPAWYqYvA6uZT-qvlvTmkX1sHmvmpOIZ6DWch0890-qs71waWAnQYqBrmBkPg5DnvONYaQXzxx2TsbNL-JhZi_wqUwwarXIFTZlfAGa4fHt_3igP73ZtsXt765fxwFJF1eq4QofAImCJ_J9JZ1CRcG4w0fb5VTiQMfExXauzkovUkne4lI_BYVykyDq8RNrv5pXo-r2oq_oDd5tyRglouLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb01cf1796.mp4?token=awpXvvwM-RRr2lxgXo5VDYlI5NyzuX9QIX0W9XMSKTDYAwJ_q4Ke7YGzAtoxIbwpm9N5f_DOuCmPw9LRknrYxKctTIyIH7esbDGeg8N-q_lXCfWcwYBsVMQSW3NIeIIKPAWYqYvA6uZT-qvlvTmkX1sHmvmpOIZ6DWch0890-qs71waWAnQYqBrmBkPg5DnvONYaQXzxx2TsbNL-JhZi_wqUwwarXIFTZlfAGa4fHt_3igP73ZtsXt765fxwFJF1eq4QofAImCJ_J9JZ1CRcG4w0fb5VTiQMfExXauzkovUkne4lI_BYVykyDq8RNrv5pXo-r2oq_oDd5tyRglouLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات؛ انهدام ۳ هسته‌ی عملیاتی گروهک تروریستی-تکفیری با دستگیری ۹ تروریست و به هلاکت رسیدن ۳ تن از آنان در جنوب شرق کشور
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/687875" target="_blank">📅 11:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687874">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noHyjEUFmfuF8XahyKl26ltQuCMcS7m4OnaVxcLh20zwR9WXds-lGpZKIFpEY4b-EMB-Y-DG6iYt0uYdgTp01sStkSDA9895yzx76xbYQeS2czBD6B5zj-yOIP9vGwISHEx6mJVh163kUksEbpg0Gwm3dbP69MRh89v8bekJCVzsUuiLkk9dvRR76GfaJGhN9yEJzSWyEgKyhFb4nYi9ieU48cKOq9VqkmWamwRlNRcq6s_XqK6OA3IAd1UYj-KPyBOq0c-kwvQVB-slHUcCwfBHsz15WUzaOGxFQsKH4IqQhw3flLIaumqpCX8-PHVVDzXJxeW88g3Rka8jV9yUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش تحت حمایت آمریکا هم برگشت خورد
🔹
نفتکش TITAN HARMONY صبح امروز هنگام نزدیک‌شدن به کریدور جنوبی تنگهٔ هرمز مسیر خود را تغییر داد و به‌سمت جنوب بازگشت.
🔹
این تغییر مسیر درحالی رخ داده که قبل از آن نیروی دریایی آمریکا درحال پشتیبانی از عبور این نفتکش در مسیر جنوبی تنگهٔ هرمز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/687874" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687873">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a8d94677.mp4?token=Esb9PZ8iAPQB1urXCzY8YG1exeWlSJQCL2XRGJnzoPkCsO9EeAvS9BcVKfGAm75hKK_y3idG8Lvxvyz8U3TPaKI3diYxFIZgCnpaz05do9hBI_Xd7YC4XqdnG7qcJR3DPjSu8b0GKMYUhvNINLC68AQNIJJf-lVBlSZOr6otSF9CzgTdey60vb3zv_u-ZztQy1_fly9n5YQrUwzmvm8gsMeU0m0_79yBlxkwiGJ9j3URwDGva3opNi4K809OfLSCihpsVKIGKtXOVnN6VEh3VyatfDKCUkt_Mf9rfZ87c9TgyqQrof-Zueuk30_OFx_yfMtim3IozBJvOtB6ge_2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a8d94677.mp4?token=Esb9PZ8iAPQB1urXCzY8YG1exeWlSJQCL2XRGJnzoPkCsO9EeAvS9BcVKfGAm75hKK_y3idG8Lvxvyz8U3TPaKI3diYxFIZgCnpaz05do9hBI_Xd7YC4XqdnG7qcJR3DPjSu8b0GKMYUhvNINLC68AQNIJJf-lVBlSZOr6otSF9CzgTdey60vb3zv_u-ZztQy1_fly9n5YQrUwzmvm8gsMeU0m0_79yBlxkwiGJ9j3URwDGva3opNi4K809OfLSCihpsVKIGKtXOVnN6VEh3VyatfDKCUkt_Mf9rfZ87c9TgyqQrof-Zueuk30_OFx_yfMtim3IozBJvOtB6ge_2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریزمان در حال مبارزه برای زنده ماندن؛ وضعیت ستاره فرانسوی در هنگام کولینگ بریک به سوژه رسانه ها بدل شده است
🔹
در هنگام برگزاری دیدار اورلاندو و سن‌دیگو رطوبت هوا در فلوریدا، بین ۷۰ تا ۷۵ درصد و دمای هوا تا ۳۴ درجه گزارش شده که باعث به وجود آمدن شرایط سخت برای بازیکنان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/687873" target="_blank">📅 11:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687872">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
«مرد هزارچهره سینما»، ۴۰ روز از رفتنش می‌گذرد، اما سال‌هاست که در قاب خاطرات ما ماندگار شده و نامش با سینمای ایران گره خورده است
🔹
در شبِ ماندگاری که با میزبانی «محمود خاضعین» برگزار شد، اهالی فرهنگ و هنر دور هم جمع شدند تا یاد و خاطره سلطان کمدی ایران اکبر عبدی، این هنرمند تکرارنشدنی را گرامی بدارند. شبی که با رونمایی از تندیس او و مرورِ هنرمندیِ بی‌نظیرش، دوباره ثابت کرد که هنرمندان بزرگ هرگز نمی‌روند؛ آن‌ها در آثاری که برایمان به جا گذاشته‌اند، همواره زنده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/687872" target="_blank">📅 11:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل در ناکارآمدی حمل‌ونقل عمومی در شهرهای بزرگ چیست؟</h4>
<ul>
<li>✓ فرسودگی ناوگان</li>
<li>✓ کمبود ناوگان</li>
<li>✓ عدم پوشش تمام مناطق</li>
<li>✓ ضعف مدیریت و زمان‌بندی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/687870" target="_blank">📅 11:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
لغو ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها  معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔹
ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها، با اجماع کامل همه اعضای ستاد ویژه ساماندهی و…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/687868" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFoH7nxHbUUkD5kIBUNsfYcsBGnnsZDh9nq5E68DfBSBx_gx0hJZHy85woLr2K-2OYtLBCsWO1niqNnVjr2dQAPh_A8Lb4nycYMAUVTMzlmFKTz8puAyFYdCjPySb0XhjSHFsZVHfFKboeIoxbImvqySVbWvmvDFrz_J_gts73t18mSLrQQYTlQ9fSEqIPGxkXDRpWQs3QAdnqPziKLxVuPyAAadhACAGaLcvSrvLWqECircqhYDhMCJIsPkPLWLlvEW8z21T-oM3t5JhkKx8rJJULQupYd19Bfhlm3HGTGT0rwls5yslHqMypCF1ZxtY-iqcXqcWOvBO5fceNfRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtSZUesfaFejk0fzWud9FU4ZUe7hA1mET1mMPG3AbHWFmJMCOXLYoqXND-N1Esm94sHpNCCi_-dz9cReYYmLJ-NUF4zMRmifcGrETYdV8UgKlUYbk24udfhMP4wYJzb2q2Nmh8hss5VveXZFTA24eTCHf4bnXLYWHDR2VONZ6_032D6_QirTVyULPLcn63aOxWX5svAbGm7VvBJAFRFsKqsRok79DCg84kSD9CY7njD6GFjajaacpbba--0rbqtYexP4ZITpTbBMmmR3G6NveykLTOg7z45hb5-7idpPoaQWd1QzoAmYXBo6Bj6iLf6yyHkSf0zYqXzDkh-Dw6bxXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیوار نویسی‌های عجیب و معنادار انجام شده روی دیوار منزل رضا کیانیان بازیگر سینما
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/687864" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6437ad10.mp4?token=GCZ0S1kapnpaDKtLKqzkghM8fKasrcruGrzVLfhYtS6uyOGTwZb8RnOiFkRDqC9FUo00u5nKlYUYdUkFGjJTE5qv_rCnJ1caMVRNmj7YEq3hChyJR8WSldiLQToIJiH_TndFPoApPFAUMh8rnJDgYVHaEEEQ2maqcARKc5DjdSGhfcz2wiyDypRoMrDrnZarvQj3rkElJND84g1r-XtXkTP_8W-sGlzMm5_puK8FRlgF1AkMd7jF8fJiJX6E-UzSDRhxo3Ou79PQF4CcLGU_K990ZLL-lgbw0iqaTlze-kUoCRw1hmMtkx28sE1_38bS5KGpb0oMyLTg8gyCmi8WL039tEYdOPQVMYB0h_3qySirrz6Bc0OVMxey_9wAbsz80dv4qP046O8hOCPCLSaAuPTheyb2loN_pC6qedsIlUPUsfDcz0C9eUEuCvtrXgKvPIvdQB8xspwZ5CioK2xSJ8ptGaCTeCsWfJwgNbFezXHUq5N3KGYYtNZo2h5Rk9PmkiWqkiASWJTg7Wx8QXvuIzccnEctgj8DmGf7Vat9_A-ts5j2-U3jlv6gzLzPPl13dKE6C40XLeKAdv9x1QJezqP9piKXjvq5kELECFQuz9SyNPDWb-d5HehYfakBdAfh6bfdzsQiWm-zJnMt_-J7jhQqoYOWilqx4B0pGeMg3M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6437ad10.mp4?token=GCZ0S1kapnpaDKtLKqzkghM8fKasrcruGrzVLfhYtS6uyOGTwZb8RnOiFkRDqC9FUo00u5nKlYUYdUkFGjJTE5qv_rCnJ1caMVRNmj7YEq3hChyJR8WSldiLQToIJiH_TndFPoApPFAUMh8rnJDgYVHaEEEQ2maqcARKc5DjdSGhfcz2wiyDypRoMrDrnZarvQj3rkElJND84g1r-XtXkTP_8W-sGlzMm5_puK8FRlgF1AkMd7jF8fJiJX6E-UzSDRhxo3Ou79PQF4CcLGU_K990ZLL-lgbw0iqaTlze-kUoCRw1hmMtkx28sE1_38bS5KGpb0oMyLTg8gyCmi8WL039tEYdOPQVMYB0h_3qySirrz6Bc0OVMxey_9wAbsz80dv4qP046O8hOCPCLSaAuPTheyb2loN_pC6qedsIlUPUsfDcz0C9eUEuCvtrXgKvPIvdQB8xspwZ5CioK2xSJ8ptGaCTeCsWfJwgNbFezXHUq5N3KGYYtNZo2h5Rk9PmkiWqkiASWJTg7Wx8QXvuIzccnEctgj8DmGf7Vat9_A-ts5j2-U3jlv6gzLzPPl13dKE6C40XLeKAdv9x1QJezqP9piKXjvq5kELECFQuz9SyNPDWb-d5HehYfakBdAfh6bfdzsQiWm-zJnMt_-J7jhQqoYOWilqx4B0pGeMg3M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره عجیب ابطحی از رادیو تلویزیون مشهد در سال ۵۸
🔹
در تلفظ عبارت
«مُدَّ ظِلُّه العالی»
و
«قُدِّسَ سِرُّه»
مشکل داشتند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/687857" target="_blank">📅 11:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf87d180eb.mp4?token=X0skWcSGd6duIyrw8pw4t5rbaBwX9xryPP9h3rwi_tajC6a_hlRzoNd59zgU1JXhcTyUqKOgd76eOwIv8JanMMuh-l3RZixTvM8mNVZMBKEYnJYtxbOyXNEY7eVMbGmTiaHy2VA6GM7dXZ6Yt20-5BMUJuqyHSpdv7nAvoAQohhEWbx30qb5JxCXgRFKFEY_R6x214rPAsNB0tjgFTy-2pdupNcmr5W9YwHvJk91g1ZTPoekj6puVwYzg2vg3bPRoGv5h4nqKmtbhPmvVVKqGRZJJSWlfBIaNRy3K4DW9mAF1yFUlTKNX5zkeiTjEegULIexu9rlTeThp5waajlCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf87d180eb.mp4?token=X0skWcSGd6duIyrw8pw4t5rbaBwX9xryPP9h3rwi_tajC6a_hlRzoNd59zgU1JXhcTyUqKOgd76eOwIv8JanMMuh-l3RZixTvM8mNVZMBKEYnJYtxbOyXNEY7eVMbGmTiaHy2VA6GM7dXZ6Yt20-5BMUJuqyHSpdv7nAvoAQohhEWbx30qb5JxCXgRFKFEY_R6x214rPAsNB0tjgFTy-2pdupNcmr5W9YwHvJk91g1ZTPoekj6puVwYzg2vg3bPRoGv5h4nqKmtbhPmvVVKqGRZJJSWlfBIaNRy3K4DW9mAF1yFUlTKNX5zkeiTjEegULIexu9rlTeThp5waajlCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده پارک دوبل برای کسانی که با پارک دوبل مشکل دارند
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/687854" target="_blank">📅 10:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله مس چی | پلتفرم خرید و فروش آنلاین مس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgjLTZge3-IyetkO9mccbzFs2rIYtK8Rz3hoR7x5Q3pwMPvj7NO0FvuimAhJB3nvpMEY3dj9NOMe8feQvjOW7Y0hb1oi13UGXdvUkbwnYgLO-fhH0jLykCqJpcyewhu_32HznllkLFb216xRF8QTGj5r0cJ4jW2yZeHCJKZcrO81amW75FhCBP3hlqYp1wVqW-qptofYynYkApp1NHXhPYa8N4CH0MxCM9DCzhHsJqeSfkLeS6pbvhJGvKcoIV3Q88lonwrrd6bQvavpC_Wrby-W5D_PTcVpKtU2nUQ6xBeX0ei3siKw0SErVQFASBQMu1s0Nq8eCMg4pGISLpOCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
فرصت طلایی خرید مس — ۰٪ کارمزد، فقط تا ۲ هفته دیگر!
‏
✅
با توجه به استقبال شما عزیزان، کارمزد خرید مس در مسچی تمدید شد!
فقط تا
۲ هفته دیگر
فرصت داری مس مورد نیازت رو با
۰٪ کارمزد
تهیه کنی.
🔺
بدون کارمزد
— تا ۱۴ روز آینده فقط قیمت خالص را پرداخت می‌کنی.
قیمت در آستانه رکورد
— ‏LME نزدیک ۱۴٬۴۰۰ دلار است.
مسچی؛ پلتفرم خرید و فروش آنلاین مس
🌐
خرید مس با کارمزد صفر درصد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/687853" target="_blank">📅 10:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مدیرعامل شرکت پخش فرآورده‌های نفتی: اصلاح قیمت بنزین از ساعت ۲۴ امشب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/687852" target="_blank">📅 10:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMWYltrKsbsv8kLQ-whGbe_49IJkMfWU0KAwQZjFL65Q7zsbz9cCb2T-2UZtewXyesimPVkGZbvClvbHNXRm7kx_ricAPHt3BzRqi9Ec0bh9Y3kCxMJld7QueBz8hyUcILhTy4vMjy5vKjpJg2_PIqvfmLx385ZkOQCa49cCY-Fb6aNaQ1QD2iLNUKUd75wHrQeGcv815Ae9nVKpXsQSq7ZEWJpoHTCEhnJeFyQ5ewPm0gzpuHYKDxQ9ei5LvcBkxcGHN1ywDuTnUEntfREUWF71PWfl1bKndieUPx7NphRMXzyXsvW5GbUnGwwp4S73spcQIkd0iCxahpW6uCoKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سفارت ایران در غنا به توهمات ترامپ: نکته جالبی در حمله به ایران وجود دارد: دیر یا زود، فرهنگ ایرانی شروع به رخنه در وجودتان می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/687851" target="_blank">📅 10:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6fa73d8b.mp4?token=pCgdb3BYdnZsdisbsbT5RcLl_XNLvNjHfrv_pMX62_bejGDAKC_uRHztQf6z7WKhciOY-n9uAvSzW3pKcuWjEnpdiQJD2vmvZL4bYifRw5RAlFx-FvcMi26HEuGi2uYczhGp1jCnvNNu96NldRR8MEMNAixFji3dFWhXpnVYumdgCSww_NV24PoY2CU-KTir7Fh_g57QO7u23L0nGERe2p_Pvk0shy1keMVx6Wz5rWMVAwUPcj2mP037EC-lSU4VntXl6MbBoaXUUNE6OD-n4IGpBA025uyCy6SF2c75a7TH9RAZi4Hr9YdJCDbiFyBUJg5cOTzp4XjpvLmxfJ7lKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6fa73d8b.mp4?token=pCgdb3BYdnZsdisbsbT5RcLl_XNLvNjHfrv_pMX62_bejGDAKC_uRHztQf6z7WKhciOY-n9uAvSzW3pKcuWjEnpdiQJD2vmvZL4bYifRw5RAlFx-FvcMi26HEuGi2uYczhGp1jCnvNNu96NldRR8MEMNAixFji3dFWhXpnVYumdgCSww_NV24PoY2CU-KTir7Fh_g57QO7u23L0nGERe2p_Pvk0shy1keMVx6Wz5rWMVAwUPcj2mP037EC-lSU4VntXl6MbBoaXUUNE6OD-n4IGpBA025uyCy6SF2c75a7TH9RAZi4Hr9YdJCDbiFyBUJg5cOTzp4XjpvLmxfJ7lKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میلادت مبارک
آقای زِدیده پنهان و در دل عیان</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/687850" target="_blank">📅 10:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a016153d30.mp4?token=um4n2iydYEZuhhNfQrw4g9IanLXbIWjOr5-HE6Yd5FgMsKyVTBz_KHWOIe9sS-__vUzjDajzqil7yppQX8OoeTE_UVco7fJCSk8TgJ7PcTlZLS_jPAzKLeDGw5_8EHJDQ4cY_MmECPeA1dBDx2MdDMYbp2bqhV5fiaql7v6R5RZj_hTWas4T4vRxXaqR3JBTHmcO32W964y97LyhWgxKx5-Ogcx2tYN9jTNm-8n1MN52v_jqskHvhcunQNjxW_YPy0yUUoEe4wJwWK_7F2buDRM8X3FPBRZVhbs6S7o1b6H3BNjbxBRxHMoMvp3HJsQZHAuC7vUk6zWTZvqYHHU1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a016153d30.mp4?token=um4n2iydYEZuhhNfQrw4g9IanLXbIWjOr5-HE6Yd5FgMsKyVTBz_KHWOIe9sS-__vUzjDajzqil7yppQX8OoeTE_UVco7fJCSk8TgJ7PcTlZLS_jPAzKLeDGw5_8EHJDQ4cY_MmECPeA1dBDx2MdDMYbp2bqhV5fiaql7v6R5RZj_hTWas4T4vRxXaqR3JBTHmcO32W964y97LyhWgxKx5-Ogcx2tYN9jTNm-8n1MN52v_jqskHvhcunQNjxW_YPy0yUUoEe4wJwWK_7F2buDRM8X3FPBRZVhbs6S7o1b6H3BNjbxBRxHMoMvp3HJsQZHAuC7vUk6zWTZvqYHHU1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های جدید آیفون ۱۸ پرو در روسیه؛ گیلاسی، نقره‌ای و آبی
📱
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687849" target="_blank">📅 10:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن، بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687848" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Om7OonWtji_Sk1U0ALKkICZAwhjMC0y6fI-oe0OnES-Qs_UvWfDJlCzM8vGR-IFivPNzm9E8apcHCF-BKiGFfIadKVwTc4WoV5oaehLQLWRDb6D5SxL7SWZKfCndAW8L7m6gSjlr410Rp2sMunEv0f2lrf5TVzd3E_rBBYqaO3tmlpd1wc9RDXnmDtRtO0u30nImdzjV0q70ISoZARRWXTr48842nIvQmHIY2u2O4snhmGlHBG-UWwnAIWo_1JIcnU_KBbnQvmbc8_3wp-DusiidfDS5AnbLmwAf_eNOAIOzWK_4M-D4gMT4DwjmGAgOiasRIsBZeu7_iscEyOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی: ایران به‌طور سیستماتیک در حال تضعیف و نابود کردن قدرت نظامی آمریکاست. طولی نخواهد کشید که آمریکا عملا بی‌دفاع خواهد شد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/687847" target="_blank">📅 10:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ec33636f.mp4?token=OIcws5yS_OWZUmX2XZGQ704DqOFyp0lP9D43fQCcL9o6XzSYob9VMK5vjCyFAITjSpZuXEAN8-TnndRTPEKUb8rfJQmNsGgRbY1ad0HIhSlKbFSGQ4a3vLRl_MYAmpC4zwGqw7UkfDd2LCP6LAQnNajYqcCl0YRU_4o_014rNkar7a6CVYftCB1QSzVNi7uyRxOr7JZrGpxVU95HBavn7jGgsqyBVZImXYKPKKqiQdfirm4_b7fVkDCy2mTlWZRZb6A_jz1GXKEZFmFh81O9Ztn3ll_AgtSBCuquOKAwj1kIVKKj89QE299vT8VM00X4ZPG6xmBSx23Q-VpqjPh7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ec33636f.mp4?token=OIcws5yS_OWZUmX2XZGQ704DqOFyp0lP9D43fQCcL9o6XzSYob9VMK5vjCyFAITjSpZuXEAN8-TnndRTPEKUb8rfJQmNsGgRbY1ad0HIhSlKbFSGQ4a3vLRl_MYAmpC4zwGqw7UkfDd2LCP6LAQnNajYqcCl0YRU_4o_014rNkar7a6CVYftCB1QSzVNi7uyRxOr7JZrGpxVU95HBavn7jGgsqyBVZImXYKPKKqiQdfirm4_b7fVkDCy2mTlWZRZb6A_jz1GXKEZFmFh81O9Ztn3ll_AgtSBCuquOKAwj1kIVKKj89QE299vT8VM00X4ZPG6xmBSx23Q-VpqjPh7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورهای غلط درباره فیزیوتراپی؛ مواردی که شاید شما هم اشتباه فکر می‌کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/687846" target="_blank">📅 10:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔹
این درحالیست که وزیر نیرو روزهای اخیر مدعی شد قطعی برق متوقف شده اما همچنان خاموشی‌ برنامه ریزی شده پابرجاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/687845" target="_blank">📅 10:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac420da3c7.mp4?token=g3ZRPZj3QMpzIkyjaHmLNvixIIkWYuNmWvDDA2Oe461HSOgbdn1UhL5-Lqde5xyXY6jr3WvZIEzhG6b3KWi7oBC-oZuYsSIUgY6VA3-zAwFEiy-Cl1aXMadqnCQys8mTDoMdOB9tRn7vHoEf1A6GIU4RakLxn4AgE8Xj9DMxTKlNMhDBOtzHGCBzzszc4mOok6cINduH94DrQyg5OkNT3-FaFPhGppaf2Rn3kTlVtpbOzdxXCWpWW6tWa7Hq9q3KG10b4bIKFZarISMwGrBXR4QQUl3_mdU-_G7Ixu0spgSnShmtIDgvPqr7PtaLeLHDpDZReOPXA7hjE5BEDvCKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac420da3c7.mp4?token=g3ZRPZj3QMpzIkyjaHmLNvixIIkWYuNmWvDDA2Oe461HSOgbdn1UhL5-Lqde5xyXY6jr3WvZIEzhG6b3KWi7oBC-oZuYsSIUgY6VA3-zAwFEiy-Cl1aXMadqnCQys8mTDoMdOB9tRn7vHoEf1A6GIU4RakLxn4AgE8Xj9DMxTKlNMhDBOtzHGCBzzszc4mOok6cINduH94DrQyg5OkNT3-FaFPhGppaf2Rn3kTlVtpbOzdxXCWpWW6tWa7Hq9q3KG10b4bIKFZarISMwGrBXR4QQUl3_mdU-_G7Ixu0spgSnShmtIDgvPqr7PtaLeLHDpDZReOPXA7hjE5BEDvCKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور جنایتکار آمریکا در ادامه توهمات خود نام ایالت نیومکزیکو را به "آمریکای جدید" تغییر داد! #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/687844" target="_blank">📅 10:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687842">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a35e76b7.mp4?token=amVDE9GOGUMLy2WcXEjQkgwX22CNmcEswPLRK8KAsVhk8C-z_6ovNpkJ1CC3xHkCY-haX4s0imsFE-GSBxziJq6JLhkJeM3UqLgS-aQ2lYrdI1t49MkrdGGDhP48bm365O2wBWJvJ_-oEkEdTK0nRtoyLhqoT5TM_IZCieQkVON-3aOmHtkNRRzs8heygemXOzRyk_705YHPbtuZhWQJCc83HDZR0np4xA6i1-Y2RWQJGbDSV4dR1k833tcfQMDAq1iuuYCH0HYZEdDTBW99ai8A9Wrr3yCfY3uU6XniyQFfEpW--rz65Fy30czZS-n1BRyF-v9_bM9cUiUE4A7_J4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a35e76b7.mp4?token=amVDE9GOGUMLy2WcXEjQkgwX22CNmcEswPLRK8KAsVhk8C-z_6ovNpkJ1CC3xHkCY-haX4s0imsFE-GSBxziJq6JLhkJeM3UqLgS-aQ2lYrdI1t49MkrdGGDhP48bm365O2wBWJvJ_-oEkEdTK0nRtoyLhqoT5TM_IZCieQkVON-3aOmHtkNRRzs8heygemXOzRyk_705YHPbtuZhWQJCc83HDZR0np4xA6i1-Y2RWQJGbDSV4dR1k833tcfQMDAq1iuuYCH0HYZEdDTBW99ai8A9Wrr3yCfY3uU6XniyQFfEpW--rz65Fy30czZS-n1BRyF-v9_bM9cUiUE4A7_J4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر دلت یک پیراشکی خیلی راحت و‌ خوشمزه می‌خواد این رسپی رو از دست نده
😋
مواد لازم:
🔹
آرد ۳ پیمانه
🔹
سوسیس ۲ عدد
🔹
خمیر مایع ۱ قاشق‌ غذاخوری
🔹
آب ولرم به میزان لازم
🔹
فلفل دلمه رنگی ۲ قاشق‌ غذاخوری
🔹
روغن مایع ۲ قاشق‌ غذاخوری
🔹
نمک، فلفل سیاه
🔹
زردچوبه
🔹
پاپریکا
🔹
آویشن…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/687842" target="_blank">📅 10:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687841">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه‌خدمات بازار‌سرمایه پاداش</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2WrEhcpfO-KOGyRzl4wl2Uz6gNWYEHFNU_aai7yjP0SHqnuEOHRm_zILOi43Nog_cUFC1gFt4azBitRY3qirt_6xLWAxmovJwrFAiWLRc_pOJAtg7lmN_ETF-ACTdMm5dBFMo-7EJrPNMILJgliWJUwRSovqyMbI1c4p3hK3UXzggFc-zn3Xf2cegh93P9Nb1f8yB2v_xv0Hs58W4F58sMY1JkpVZZEmzyAbWrO4ICo6HUUHodmGsfvmUwif58R4o1J8-t0sQw_nd-FkX0vSaWV3121XVENoVXjgd9eqgOk5ZY-sUlVpQkxoCGQxG5_aKU2G3E8V7ln011HZQuuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سیلوا»؛ یک میلیارد واحد سرمایه‌گذاری
◀️
سقف صندوق نقره پاداش با نماد
«
سیلوا
»
به ۱ میلیارد واحد سرمایه‌گذاری افزایش یافت تا فرصت سرمایه‌گذاری برای تعداد بیشتری از علاقه‌مندان به بازار نقره فراهم شود.
🔺
«
سیلوا
»
از روز دوشنبه ۱۶ شهریورماه بازگشایی می‌شود و امکان خرید واحدهای این صندوق برای سرمایه‌گذاران از تمامی کارگزاری‌ها فراهم خواهد شد.
🔺
مراحل خرید صندوق نقره پاداش «
سیلوا
»:
🔺
وارد سامانه معاملاتی خود شوید. نماد
«
سیلوا
»
را جست‌وجو و سفارش خود را ثبت کنید.
🔺
امکان خرید از طریق تمامی کارگزاری‌ها
🥇
صندوق طلای پاداش «گُلدا»
📈
صندوق نقره پاداش
«سیلوا»
📞
۰۲۱-۵۸۷۱۸</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/687841" target="_blank">📅 10:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687840">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCBMUndYIjR7PrFGaV0xGWGfHw6QeNU0EGHdo3BkUo6Y5YtD9FckAcTOfHD5PrhFe8XL-v32Cm2e7fKTkNfs6OwlTqE_RcuB9gPiLmqppvXONlEVzgFo9idsfg4gjUEsyPBt2gQL4Jpv5ROs1bCGFCfIVLNvxk45-RXRbqg-84aMbVfGNGfhvZOFbCwodGFTcAbWdYSvzykueKSSS5mwrwOvjcNvKVjcMljrgnJFNcx786tufGHffQdYPBKtd3SrMGDB6PpOHpw-5dVPoMeiBVTfJMiBPjjYMceaWkf4Upvj2rOf9I74rIUdpaY0zCCvASxkw6kUFefGwNoTLhd7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
فروش ویژه فرش سجاده آریا | جشنواره میلاد امام حسن عسکری(ع)
⏳
این شرایط ویژه فقط تا میلاد امام حسن عسکری(ع) برقرار است.
🔥
فرش ۷۰۰ شانه بخرید، به قیمت فرش ۴۴۰ شانه پرداخت کنید.
✅
۲۰ تا ۶۰٪ تخفیف
✅
خرید مستقیم از کارخانه
✅
فروش اقساطی
✅
ضمانت ۱۵ ساله
اگر به دنبال فرش سجاده‌ای با کیفیت واقعی و قیمت اقتصادی هستید، همین الان تماس بگیرید.
📣
درخواست قیمت و کاتالوگ فرش سجاده:
تماس بگیرید یا عدد 1 را ارسال کنید
👇
📞
شماره: 09128044740
📲
آی‌دی:
@farshsajadeharia
https://t.me/aryiacarpet
💫
💫
فرش سجاده آریا
💫
💫</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/687840" target="_blank">📅 10:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb3e1c4d7.mp4?token=FzuYtAN0wW76uys9TkcC-VJkNsUh3maSIavaiB1yCpGwdKxMyrruAS10nAbkBUcBr39mUweFGqKl8bRIR00diI1R8SrAynWKQDfOjcBMTFBn8kAxaylc2OV6QuKLF4o2JcZlXuMKqpZFlIM2eEu00gColTujdjhlZMoyBDGQWnvqj8oUWUlMp9V_m3Cd9mrbQG0L2VKGpzkv41fu7ZkIlu4qbGzlE2OKAcmBu8J00EVoWk5HEIa6rn6H2CgNyI432x7GZvhGiCV0hLvXbyAXkgtxetQ-a87tiyYyhMiGsyIktL99lWFjZLFenSbjRxWHE3Y7VgF6WoKXrzTHlw_w8g5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb3e1c4d7.mp4?token=FzuYtAN0wW76uys9TkcC-VJkNsUh3maSIavaiB1yCpGwdKxMyrruAS10nAbkBUcBr39mUweFGqKl8bRIR00diI1R8SrAynWKQDfOjcBMTFBn8kAxaylc2OV6QuKLF4o2JcZlXuMKqpZFlIM2eEu00gColTujdjhlZMoyBDGQWnvqj8oUWUlMp9V_m3Cd9mrbQG0L2VKGpzkv41fu7ZkIlu4qbGzlE2OKAcmBu8J00EVoWk5HEIa6rn6H2CgNyI432x7GZvhGiCV0hLvXbyAXkgtxetQ-a87tiyYyhMiGsyIktL99lWFjZLFenSbjRxWHE3Y7VgF6WoKXrzTHlw_w8g5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جالب با ۱۲.۷ میلیون بازدید؛ که با هوش مصنوعی تولید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/687838" target="_blank">📅 09:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
چه کسانی واکسن آنفولانزا بزنند؟
⁣
مینو محرز، فوق‌‌تخصص بیماری‌های عفونی:
⁣
🔹
افرادی که بیماری‌های زمینه‌ای دارند، زنان باردار و کودکان از جمله گروه‌هایی هستند که توصیه می‌شود واکسن آنفلوانزا را دریافت کنند و در صورت وجود امکانات و تأمین واکسن، سایر افراد جامعه نیز می‌توانند واکسینه شوند، اما با توجه به محدودیت احتمالی در تأمین واکسن، اولویت باید با گروه‌های پرخطر باشد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/687837" target="_blank">📅 09:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/687836" target="_blank">📅 09:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خرید لباس فرم جدید اجباری نیست
⁣
سخنگوی وزارت آموزشوپرورش:
🔹
خانواده‌ها می‌توانند در صورت مناسب بودن لباس فرم سال گذشته، از همان لباس استفاده کنند.
⁣
🔹
در برخی استان‌ها تقریباً تمام لباس فرم دانش‌آموزان از ظرفیت هنرجویان، به‌ویژه هنرجویان دختر رشته طراحی و دوخت، تأمین می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/687835" target="_blank">📅 09:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687833">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ویدیوی جالب از دامداری پیشرفته در چین؛ آیا در ایران نداریم؟
🔹
مشکل اصلی دامداری مدرن نه پیچیدگی فناوری، بلکه ضعف مدیریت، بهره‌وری و نگاه صنعتی به این حوزه است. ایران هم به این حوزه ورود کرده و حتی نشانه های صنعتی شدن دامداری در یک شرکت ایرانی در فریمان خراسان رضوی شروع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687833" target="_blank">📅 09:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687832">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2c121812.mp4?token=cROzdTqFp44BBy_ZJDKpbb-JIJ9bvoKH29BELvQfyHjkzJiEbmHdgL2wCZP6_kIgbfxsJHd3wVY4kMP3I8c0nFbqXBGjuGSfy_sg5ohg7oLrI5LNCj2qlUsij1A0p4TpSblxU7oQRwjMHQTNY9yRbVrsbXHf6ZWHxRVXh3XmOpKVP8g336vTJq_u2DzBItNoV-joTkoAmYCsPnsTl2DsWtLwokSMFO4Lncd0jiHidHDnJBLJV5teYC-p4GX2k0JbbWF8Ot6wpIeQ1Q4B6iXrTynvx8lb2ZuxlXKirEKMHHWjIeTCdCnBfl3mleAezN9r26lGxeJcsQ7UrJTPr65AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2c121812.mp4?token=cROzdTqFp44BBy_ZJDKpbb-JIJ9bvoKH29BELvQfyHjkzJiEbmHdgL2wCZP6_kIgbfxsJHd3wVY4kMP3I8c0nFbqXBGjuGSfy_sg5ohg7oLrI5LNCj2qlUsij1A0p4TpSblxU7oQRwjMHQTNY9yRbVrsbXHf6ZWHxRVXh3XmOpKVP8g336vTJq_u2DzBItNoV-joTkoAmYCsPnsTl2DsWtLwokSMFO4Lncd0jiHidHDnJBLJV5teYC-p4GX2k0JbbWF8Ot6wpIeQ1Q4B6iXrTynvx8lb2ZuxlXKirEKMHHWjIeTCdCnBfl3mleAezN9r26lGxeJcsQ7UrJTPr65AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل شرکت پخش فرآورده‌های نفتی: اصلاح قیمت بنزین از ساعت ۲۴ امشب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/687832" target="_blank">📅 09:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687831">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آیا اسکرین‌شات در دادگاه قابل استناد است؟
مدیر دفتر مطالعات حقوق قوه قضاییه:
🔹
اسکرین‌شات پیام‌های موجود در پیام‌رسان‌های خارجی قابل ارائه و استناد در دادگاه است، اما به تنهایی دلیل کافی برای اثبات یک ادعا محسوب نمی‌شود و اصالت آن باید با بررسی‌های فنی و کارشناسی احراز شود.
🔹
رویه دادگاه‌ها در بسیاری از موارد به این صورت است که داده‌ها و پیام‌های ارائه‌ شده برای بررسی صحت و اصالت به کارشناس رسمی ارجاع می‌شود. در چنین شرایطی، دستگاه مبدأ که پیام از آن ارسال شده و دستگاه مقصدی که پیام در آن دریافت شده است، می‌تواند در اختیار کارشناس قرار گیرد تا اصالت داده‌ها مورد بررسی قرار گیرد./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687831" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d5c374e08.mp4?token=Ij2-MvQSxOZJsDEichb5yZpEZw-mnujRlISNlzPFkiA5vM7hHLIiAlW5ca_5HFNBJLTO3wo9xNtHbaimmfRKICCzVtT-qIlxYfo3IdirhSJTTosXq1UDr1I6AOBqODjQZkkRA8yJDlAP9k5aIJr2J-ywyNgJbE09XsE-1lKt1rf5OoLySX7hQhoIGiivlQv9N-GsT3STcAccyFRT2ogv9-t3QWDdbyjjOeOE4R74UGh-V40Q4RlmFpAoOneVDWQiR0c_TY9J9sKIzrKFwR5j14qkLdLEJh-5N-eiIz5_5kW1TzGRRk6Gh1J8aCuvRD-1ioLkkcJeyyeLEtuRtgzFqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d5c374e08.mp4?token=Ij2-MvQSxOZJsDEichb5yZpEZw-mnujRlISNlzPFkiA5vM7hHLIiAlW5ca_5HFNBJLTO3wo9xNtHbaimmfRKICCzVtT-qIlxYfo3IdirhSJTTosXq1UDr1I6AOBqODjQZkkRA8yJDlAP9k5aIJr2J-ywyNgJbE09XsE-1lKt1rf5OoLySX7hQhoIGiivlQv9N-GsT3STcAccyFRT2ogv9-t3QWDdbyjjOeOE4R74UGh-V40Q4RlmFpAoOneVDWQiR0c_TY9J9sKIzrKFwR5j14qkLdLEJh-5N-eiIz5_5kW1TzGRRk6Gh1J8aCuvRD-1ioLkkcJeyyeLEtuRtgzFqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارت هوشمند سوخت برای افرادی که کارت ندارند، به‌ صورت یک روزه صادر می‌شود
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی:
🔹
کارت هوشمند سوخت بصورت ثبت‌نام اینترنتی و ثبت حضوری به نسبت دریافت از طریق پست با سرعت بیشتری صادر می‌شود. هزینه درخواست کارت هوشمند سوخت بصورت اینترنتی و دریافت پستی ۱۰۰ هزارتومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/687830" target="_blank">📅 08:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687829">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8fdc708.mp4?token=kLgd0t2B-k0fFXmh_cKmHl4p8lPHSy6kmQKarbIQB5Lss_7Ic3ZZwNxWt0ZoK9kU_JgAlWt9zaWKJ7lMbbBBCFn83iew16wlMNTl4r1enMn5AfSAJ3Uvg3IQDmIaqyn_MwQP1bvbfUiAm_iSOLgbQDcbT-D-AJ9nBAjz2MOFeZQjJ1Xjh0JzSUQC9-BvvJmDg5CpsK89-HwG7AlhVq1ehlF-DzmmUR7hpC_l2e87US89omPPdq2TKu0eGcFfWBs3OGUXhXqB5N1A4aveNCF02qxH9wPplEok7NJgCxwfp2gyyYaR0QmPg9W5X2ZzdbZy1I2WBUECfApSt342T7_HjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8fdc708.mp4?token=kLgd0t2B-k0fFXmh_cKmHl4p8lPHSy6kmQKarbIQB5Lss_7Ic3ZZwNxWt0ZoK9kU_JgAlWt9zaWKJ7lMbbBBCFn83iew16wlMNTl4r1enMn5AfSAJ3Uvg3IQDmIaqyn_MwQP1bvbfUiAm_iSOLgbQDcbT-D-AJ9nBAjz2MOFeZQjJ1Xjh0JzSUQC9-BvvJmDg5CpsK89-HwG7AlhVq1ehlF-DzmmUR7hpC_l2e87US89omPPdq2TKu0eGcFfWBs3OGUXhXqB5N1A4aveNCF02qxH9wPplEok7NJgCxwfp2gyyYaR0QmPg9W5X2ZzdbZy1I2WBUECfApSt342T7_HjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودیتی برای استفاده از کارت جایگاه اعمال نمی‌کنیم
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی:
🔹
با سهمیه اول و دوم کارت سوخت شخصی، حدود ۸۵ درصد نیاز مصرف‌کنندگان تأمین می‌شود و کارت جایگاه‌ها نیز همچنان در دسترس خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/687829" target="_blank">📅 08:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687828">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی نفت: تنها نرخ سوم بنزین مشمول تغییر است و از ۵ هزار تومان به ۱۰ هزارتومان تغییر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/687828" target="_blank">📅 08:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687827">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یارانه ۴۵ هزار تومانی سال ۸۹ امروز چقدر می‌ارزد؟
🔹
برخی محاسبات نشان می‌دهد این مبلغ با معیار دلار، معادل حدود ۱۴ میلیون تومان امروز است؛ یعنی یک خانواده ۵ نفره در آن زمان قدرت خریدی معادل حدود ۷۰ میلیون تومان یارانه ماهانه داشت.
🔹
با معیار طلا نیز سهم هر نفر حدود ۱.۳ گرم طلا، معادل نزدیک به ۳۰ میلیون تومان امروز برآورد می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/687827" target="_blank">📅 08:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687826">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
احتمال شنیده شدن صدای انفجار در محدوده جنوب اصفهان برای امروز از ساعت ۹:۰۰ صبح تا ۱۴ بعدازظهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/687826" target="_blank">📅 08:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da83e76fd5.mp4?token=n0hxdBiv1PcAoHiidiWt4KRyhe1wf6xRMDV-GYYqHfuzaLgp52WS6-WyMeBaaAyqnjZrAN-9kc45f9s2XE4bCx2ZnumCl7qutABpVrG1js0zdgHgAA2_CxL80b8ojpJ5E0my59xt9st5GeY-foyQry2L-27byffDNydB84Zzs2U_5GhT9ko2eO0W6mYwgg2nLVRJncDJCtiVVz8XuvWO0vz-aiSAR8i91x5jtpfD2zy8ROcv1gtAa2lOxvRkpB5rSxAD5avLlpulDDejorYpKufuXQssVZINytYXNrU4wOhAodLcLcLew5x-2_5Psbmn9zXUo9LCAZcAXzAnwElp4LRgnirMcl4wW3nexj9aM2R7rQBiELtczSyhevrLZUNFtWGbYUALHo6jzNP_EHAMr1_4VeJeGZ3mPJttNNOKeMdjuBP75zlFeZ8yiT6PX_UNSmRbLahanp9hxoUylDvMd7OPP4zi5jvMM0bO9q_POdEYXlQthEQ9c7nn27QmRj6snDMucjxKXO0TK3nQLuCHpdLaDVciKO_3T3arVaq7XVRtNok1XRfoVz-X3Xej3HBtxZAKIEkH3xgVvQ5cDiA4L6Xv-lA8rQwzNrMvdtX_PhPnTn2M8j4ZWG7K9d0obf4L-UqKdiGMHEjNSpH3godKq2xbNWCGz3qw6iy9CIhhZlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da83e76fd5.mp4?token=n0hxdBiv1PcAoHiidiWt4KRyhe1wf6xRMDV-GYYqHfuzaLgp52WS6-WyMeBaaAyqnjZrAN-9kc45f9s2XE4bCx2ZnumCl7qutABpVrG1js0zdgHgAA2_CxL80b8ojpJ5E0my59xt9st5GeY-foyQry2L-27byffDNydB84Zzs2U_5GhT9ko2eO0W6mYwgg2nLVRJncDJCtiVVz8XuvWO0vz-aiSAR8i91x5jtpfD2zy8ROcv1gtAa2lOxvRkpB5rSxAD5avLlpulDDejorYpKufuXQssVZINytYXNrU4wOhAodLcLcLew5x-2_5Psbmn9zXUo9LCAZcAXzAnwElp4LRgnirMcl4wW3nexj9aM2R7rQBiELtczSyhevrLZUNFtWGbYUALHo6jzNP_EHAMr1_4VeJeGZ3mPJttNNOKeMdjuBP75zlFeZ8yiT6PX_UNSmRbLahanp9hxoUylDvMd7OPP4zi5jvMM0bO9q_POdEYXlQthEQ9c7nn27QmRj6snDMucjxKXO0TK3nQLuCHpdLaDVciKO_3T3arVaq7XVRtNok1XRfoVz-X3Xej3HBtxZAKIEkH3xgVvQ5cDiA4L6Xv-lA8rQwzNrMvdtX_PhPnTn2M8j4ZWG7K9d0obf4L-UqKdiGMHEjNSpH3godKq2xbNWCGz3qw6iy9CIhhZlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از تجمعی با شعارهایی علیه حسن روحانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687825" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cbe8d86d.mp4?token=XNPZpmf3Zu3jD-5MyvFbdLpR6Y0L6K0jYnLF-gLq_A5rktwctfl2QQwKi8iYlJbPQdPouHAcQl1DychUwtttAfzwcipAjFJQ75GAhWQrTXBe0L-8oMwHIFWX6mVJe6LH8lYL0TNS-XD7oKxhoHa0MQDfgdmfvlictqBjpmbckEf53KQQZTO7Y9RYpak3Xp2Gq0afWONEorWX24UCdUJmhW_CIxS4nGzb33uND3M3RxSVYZHPDmYgaNiqXvJVCrTIU-X0LLATnum83iMuKKdSnb-dcjNhgcPHFopKxwwSnlMiLoZUWC8bgn1irT0HpRE6JvPJyHaQOJXRRjHkV1pAw4Su2nmYhztWsBQDAv-7RVF5d89gU2k2F0wzn-gSZ95wLHRzqNDWVFrFSSocsiTJjUh1w3yLiRp-qkWZKSL9XIC-k9Ph5payBu1WKOVGOVqazv6MGMw_tWtTyf5bZBQn9vwuktOtjY97L_7lcbqxdJzgaPZSwbeixDq2_jL2UsCBA3ioORyQS5GxJOYQlRmuix_FZkE4Tc08njUtBMEJztN0aEEjyi-YrI73KcCxTGBMGs-B6wPBVg1ULnyTDsG6sRPFrT1ad8KIywejFyziYRayly7Ixyz4RVDIp0N0bdeutYEVOYf3eHoYh-jgFp8_LxskF1NI_X5UqIN5U03SNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cbe8d86d.mp4?token=XNPZpmf3Zu3jD-5MyvFbdLpR6Y0L6K0jYnLF-gLq_A5rktwctfl2QQwKi8iYlJbPQdPouHAcQl1DychUwtttAfzwcipAjFJQ75GAhWQrTXBe0L-8oMwHIFWX6mVJe6LH8lYL0TNS-XD7oKxhoHa0MQDfgdmfvlictqBjpmbckEf53KQQZTO7Y9RYpak3Xp2Gq0afWONEorWX24UCdUJmhW_CIxS4nGzb33uND3M3RxSVYZHPDmYgaNiqXvJVCrTIU-X0LLATnum83iMuKKdSnb-dcjNhgcPHFopKxwwSnlMiLoZUWC8bgn1irT0HpRE6JvPJyHaQOJXRRjHkV1pAw4Su2nmYhztWsBQDAv-7RVF5d89gU2k2F0wzn-gSZ95wLHRzqNDWVFrFSSocsiTJjUh1w3yLiRp-qkWZKSL9XIC-k9Ph5payBu1WKOVGOVqazv6MGMw_tWtTyf5bZBQn9vwuktOtjY97L_7lcbqxdJzgaPZSwbeixDq2_jL2UsCBA3ioORyQS5GxJOYQlRmuix_FZkE4Tc08njUtBMEJztN0aEEjyi-YrI73KcCxTGBMGs-B6wPBVg1ULnyTDsG6sRPFrT1ad8KIywejFyziYRayly7Ixyz4RVDIp0N0bdeutYEVOYf3eHoYh-jgFp8_LxskF1NI_X5UqIN5U03SNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نارنجی برای نوار شمالی کشور؛ کاهش دما، بارش شدید و طوفان گردوخاک در شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687824" target="_blank">📅 08:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d98eb297.mp4?token=fhKiCjgLiYOTMnBu29slQcv-5P0NaZQZnJdcKgemNIQn2uUZooIsbWMzjfAY4FwqC82Xd3QfN7B9JA_I-WOgChwzUG4RxXuQQDlJRUA9jnVkEQpP3m8bvClVRsRcvXuB3SSK8PmxNd3Pdrti_A61ZjvyVD3PEwbCWo1lXWBl5c6FWcEJHpO1B6bCJSFsoMwvfQ_AcKJjSseNc32u1-PxbDFMkzmRHNCvLJ2GPoU8FiBfsnSK4c3CCjxfOAyczlhZjzTyTi3wi5v2rMBB8AYuCIiNy3t6M-aL9NMHimHJXaeOJaT1z4qnymdl3tMEPIQ6pE_1cncDp-JXoSugMw2LhC6d6eU6k5_6NPRY6bqHRzkrK_cDAx0soesYiEdOAQWVH3IZmj5fpmhl0tzYpBraaP-dNIrOniaUFsURLCGkZikkWDGWeB-1McNo3yIvPexCtn5WqFaFcHSWZnP-3NH1w2obNAfwPGN9ClnwGowUuGjF7LCmPGTCSaynrd5TWssBPRCbFSV16Wz6ILrullfmhW8cvxbBvYEr2FDex0UwOQKgv9sMsh8nJPwVej-hjxaXY4hxYFbtXyk1VWbQ3jZi2QxC1bN71lKK7Tfp9kNO67ATLP9zyK2xmb7knrJ7I5QEBjd9g4xXXw7uK2wI_CXSsddEz-Re58DNdl-Sj91V9SE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d98eb297.mp4?token=fhKiCjgLiYOTMnBu29slQcv-5P0NaZQZnJdcKgemNIQn2uUZooIsbWMzjfAY4FwqC82Xd3QfN7B9JA_I-WOgChwzUG4RxXuQQDlJRUA9jnVkEQpP3m8bvClVRsRcvXuB3SSK8PmxNd3Pdrti_A61ZjvyVD3PEwbCWo1lXWBl5c6FWcEJHpO1B6bCJSFsoMwvfQ_AcKJjSseNc32u1-PxbDFMkzmRHNCvLJ2GPoU8FiBfsnSK4c3CCjxfOAyczlhZjzTyTi3wi5v2rMBB8AYuCIiNy3t6M-aL9NMHimHJXaeOJaT1z4qnymdl3tMEPIQ6pE_1cncDp-JXoSugMw2LhC6d6eU6k5_6NPRY6bqHRzkrK_cDAx0soesYiEdOAQWVH3IZmj5fpmhl0tzYpBraaP-dNIrOniaUFsURLCGkZikkWDGWeB-1McNo3yIvPexCtn5WqFaFcHSWZnP-3NH1w2obNAfwPGN9ClnwGowUuGjF7LCmPGTCSaynrd5TWssBPRCbFSV16Wz6ILrullfmhW8cvxbBvYEr2FDex0UwOQKgv9sMsh8nJPwVej-hjxaXY4hxYFbtXyk1VWbQ3jZi2QxC1bN71lKK7Tfp9kNO67ATLP9zyK2xmb7knrJ7I5QEBjd9g4xXXw7uK2wI_CXSsddEz-Re58DNdl-Sj91V9SE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرر ۲ میلیاردی متین ستوده و کامران تفتی؛ اعتماد به یک تریدر گران تمام شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/687823" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687822">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f37f0fa2.mp4?token=p5RFxTE0pfbn779auOnGTDU6gEeSV40aSHVWNwDjnaVDhKbiFyrYS9patvPcj9aBAu83b2glicCmLTuTQ6gtRnJkDCPYfafaXxpZ0ttCfe3Qmha1vxylwVwfAJf2YwzP14IKIRtYPwGBGCxE1V93oBCdsd8THzjkxhsxdmkUrrhHE5RMGjybVTqVCbhWWQlmMQI0nqV4kIxpO-PgU2NtJ3VsyvwXvsj9PdtLpW0amF7hQ-ELGzUMEtbCzZrFN3egX2F3Hwuk_1aznshZmUvDwIbSTw8dm0KBdnnq0ivjFbTeVL41OBunaBkHon3l1O7mv0qh7idtLlQ0f3AXof1ZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f37f0fa2.mp4?token=p5RFxTE0pfbn779auOnGTDU6gEeSV40aSHVWNwDjnaVDhKbiFyrYS9patvPcj9aBAu83b2glicCmLTuTQ6gtRnJkDCPYfafaXxpZ0ttCfe3Qmha1vxylwVwfAJf2YwzP14IKIRtYPwGBGCxE1V93oBCdsd8THzjkxhsxdmkUrrhHE5RMGjybVTqVCbhWWQlmMQI0nqV4kIxpO-PgU2NtJ3VsyvwXvsj9PdtLpW0amF7hQ-ELGzUMEtbCzZrFN3egX2F3Hwuk_1aznshZmUvDwIbSTw8dm0KBdnnq0ivjFbTeVL41OBunaBkHon3l1O7mv0qh7idtLlQ0f3AXof1ZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شفای ناگهانی بعد از حضور پلیس؛ ترفند عجیب گدایی با ادعای بیماری!
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/687822" target="_blank">📅 08:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687821">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=RHws9ATm1G37hC17VN_WRs7IQsgHw8v7pwWk1Qy8EuxirMTukVcnhPF51cmRszCniroEgG4CeMNkmtUro54IjpWc0A9xTZXPo4G4DyYl1rPhZIYofZzIcgpRTWdyHYwIW5YBb3xDqeO8PzvaiJ8OMoyHIzoPk1iaMSbgc3iolgwUzveeUHk7XkYMbwVqhOkl0OW1TcDEPQHeHYKHS0_q_Kk4Lm_8vq1zNX7pjqSDAaWJXmXp6KOT9o0F2orF7STDsMP53k5URxFwHtKiHlSk7RZTyvmsvUyS81b2Mg16tZgkEaYNfEQRc0XRTxrQe8pyTEs-XbKDcSnKvLrbPU41ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=RHws9ATm1G37hC17VN_WRs7IQsgHw8v7pwWk1Qy8EuxirMTukVcnhPF51cmRszCniroEgG4CeMNkmtUro54IjpWc0A9xTZXPo4G4DyYl1rPhZIYofZzIcgpRTWdyHYwIW5YBb3xDqeO8PzvaiJ8OMoyHIzoPk1iaMSbgc3iolgwUzveeUHk7XkYMbwVqhOkl0OW1TcDEPQHeHYKHS0_q_Kk4Lm_8vq1zNX7pjqSDAaWJXmXp6KOT9o0F2orF7STDsMP53k5URxFwHtKiHlSk7RZTyvmsvUyS81b2Mg16tZgkEaYNfEQRc0XRTxrQe8pyTEs-XbKDcSnKvLrbPU41ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی از حملۀ پهپادی به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق و برخاستن دود از این محل خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/687821" target="_blank">📅 08:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPLQwPo6n63_EyuNpU9rQvgRM4BlnhUXTBZvfubKqGg9gC-g-JBSTUnofHCXNMWYn6ADW80pt4F1nUtdAuxlhUIZpIPFkzWSyvySzJ1DQg5O6fi9Asd0SLdZnQH-FVqAnjPtkyYLyE9id5tiiC8TFYJeoarXoMabMYGd7guiud4DSS_GFkYsK6yUO5Ut-lmyHki_qANDMbZbXBoW6Yxk_2VbL_n8OFSMYd_aXPuWp3inQmAdONRZxYM9dqGlzfj0f4YHgcM5AVYl0A31bmDGtm5kyQhhFpQS8rztcmwCR_B4kcLyb4a2JhnJOl3KF7sEb2uslUqapDUXDYIwMOIU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmIIhAVqGJJ73bYLGbnAhv7aM5qk7-JuXcb1HbchSV7vJ-uvI94vHnyXKs0rdqXt9_sRWXZ5rsGvpo5UjAWtizlbfHDvI0DebNOxtBPJx7DWELSbx6m-OORE0GVRL5phBH3kmVJoyND-GWyNCTXtb7sMEL6Gh9wkMdB4tYI5lfNawpoJlxKP7083CjB_9ChcaP88esn04CD-9ku8Q0FJKT7aBLzJY0kL6-44Nz1twh8yMKtr1L0zY3sq9G6YWqptw5a9qfWnLcQ30Rlzuul_UwXKBsKjG7TM_HUsPyEVl7GLmonBgWncrRHX6uNmhRS8cMxjiYr3StiGefTfzgq2xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر حضور جیم تورنتون در یک چت‌روم مشکوک خبرساز شد
🔹
جیمز تورنتون مجری مشهور آمریکایی به دلیل عکسی که نشان می‌دهد در چت روم پدوفیل‌ها حضور دارد با رسوایی شدید روبه‌رو شده است
🔹
این چت مربوط به تجاوز به پسر بچه‌های ایرانی است، نام‌های «کیان ، ابوالفضل و ماهان» در خط سوم چت قید شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/687819" target="_blank">📅 08:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687816">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تاکید بر ثبت‌نام به موقع کتاب‌های درسی دانش‌آموزان
آموزش و پرورش:
🔹
والدین محترم دانش‌آموزان عزیز توجه داشته باشند چنانچه دانش‌آموزان در وقت مقرر ثبت‌نام کتاب‌های درسی را انجام ندهند، بعداً در تحویل کتاب درسی به نسبت تأخیر در ثبت‌نام، دچار مشکل خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687816" target="_blank">📅 07:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687815">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSUUMTHh3N_fC8JuMBQL-0KvEwezXKSaqsPe1P2CgAKji3jKc3WTQKKZNGJG1TLAOfoSDtL5tBwZeffT7Ro3T_vZRFTCxdxg2BQNNTj8GectwfFQ-Y3vVXQaYdZXIsahgegl9kmdDK8mwznMWJRm11_V6C5zGnt4siWbFx5s6g9kYMn6wevFca33PgdCv6JCMtLKxLuAkrc7HYskMtxWscHbB23Bpx8EzDajQRlV5RYIIdQtMr6RXKnKq9J5_ALy1IXMzDIp5EKK6Ufjt7T18sbKD1b5NRnL86csuOUVnPkDbVcXPYYF6lMWmPbcLtkBO8fQlVhFwxgf1ZIrqANMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۶ شهریور ماه
۲۵ ربیع‌الأول ‌‌۱۴۴۸
۷ سپتامبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/687815" target="_blank">📅 07:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687814">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1EvlUhTlkACVdx_qCkBU-Ig55Et2GjGRPLoPpdGWs5ohAvGTEG4ujlU2tumLr9S5gsEPesOMnUVnI9_Tn8kpraxCEuvXPsEvVDEHxyCSBQY02y40q7cztPsWPyCglRi9dXSA6XyeLBSqxC7MrMIrTgmbqWhytBUDvWZKLWyCnlW8ArpXM_7aZynTWMwyZgvCw30iK5hj1jgVeKnW06LXHIZlnnZrwJTPj_raahWKfAZQH3W-AE2CvXdJumUJJXnyLj_AytNfRNagrIfkqUbkjiTVRJMeatZEe_o6GWXJrAiKGdqBoAiK_Jzdi22uKPy-G8PgAnbX7xcoymDlxQpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه‌چیز برای مدرسه!
🎒
از
دیجی‌کالا
بخر، با اعتبار
بلوجونیور
!
تمام وسایل مدرسه رو در
یک خرید، اقساطی و بدون دردسر
تهیه کن.
🛍
😊
لینک خرید از سایت دیجی‌کالا
برای شروع مدرسه آماده‌ شو!</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/687814" target="_blank">📅 01:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687813">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بقایی: اقدامات تجاوزکارانه آمریکا عامل ناامنی در تنگه هرمز است
سخنگوی وزارت خارجه:
🔹
آمریکا جنگ را آغاز کرد اما انتظار دارد که تمام جهان هزینه آن را بپردازند. این کاملا مضحک است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/687813" target="_blank">📅 01:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687812">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJ9PJtYOPxjcBdDaXr7pfDnO91RWYiUmKt75RmrUNh9lXQ49ysja1DIW2Vj-QfJVFaP-Wcb5jYzFnrNEi5MGCPqlB-1Jq5luy7_EZmodAMPPa_ZrJvdUzTccQOxt1d5U0YmFt-WYcqx9KG2v-j9cMGU6cJHXins6BmsAz4xWgp8rX3b7uFU7P5G5T70__Yt4evDhjS2WfM1P6BP0lei5tIkfOUSs1q821nUlD-d0vNezxyA9YP7Asnmq8q-Dl9ftDOiBPdPMg29IbDyB-IgrC5kp-6EMNcZhA2VYBTZ2swdI4GXFNy-Bz1UZRn5R4K-gY_2bRdEnx6QGiiAlSI23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریس مورفی، سناتور آمریکایی: ایران قدرتمندتر از همیشه است
🔹
۱۸ آمریکایی کشته شده‌اند، میلیاردها دلار به پایگاه‌ها خسارت وارد شده و ذخایر موشکی به‌شدت کاهش یافته است.
🔹
کشاورزان و خانواده‌های آمریکایی نیز با فشار اقتصادی و افزایش قیمت بنزین مواجه‌اند.
🔹
با این حال، رئیس‌جمهور آمریکا می‌گوید «چیز مهمی نیست»؛ او به‌طرز خطرناکی دچار توهم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/687812" target="_blank">📅 01:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687810">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf90fd297f.mp4?token=urjOgj_27Ba8d8K3NaPF9xIBPbmZctvpyGss4a-tXgWdKpHKuBQ_p4NIxCEQ9x6He1gEmaCoFZpS8yN26if25cWEd9aRjB-b7SkiK0RCNFSBAvcFqT20xTj0gHUMXswyN_dSaPAKYX7ZnPAwVfrIr0sO0T9x3R9faZ5VxIy-Q88nnH7RVGcKE-Wll3APXz5bjK87kVWY_jH0jCy2EcGKCYNv0iLZf5oycXgIc-atnJH2Qs1tabSDAyp3wkfgWDzxaVCyEKHlraO-fvHQaQ-t-Vra6ed6HqdIRO_7YlMH47TqOU9Mt0kzRRTFwNtxGqr97-02eOzYqlHfFcyWrEr96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf90fd297f.mp4?token=urjOgj_27Ba8d8K3NaPF9xIBPbmZctvpyGss4a-tXgWdKpHKuBQ_p4NIxCEQ9x6He1gEmaCoFZpS8yN26if25cWEd9aRjB-b7SkiK0RCNFSBAvcFqT20xTj0gHUMXswyN_dSaPAKYX7ZnPAwVfrIr0sO0T9x3R9faZ5VxIy-Q88nnH7RVGcKE-Wll3APXz5bjK87kVWY_jH0jCy2EcGKCYNv0iLZf5oycXgIc-atnJH2Qs1tabSDAyp3wkfgWDzxaVCyEKHlraO-fvHQaQ-t-Vra6ed6HqdIRO_7YlMH47TqOU9Mt0kzRRTFwNtxGqr97-02eOzYqlHfFcyWrEr96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه هوایی در فرودگاه بین‌المللی میامی آمریکا
مقامات شهر میامی آمریکا:
🔹
۵ نفر در پی سقوط یک فروند هواپیمای باربری متعلق به شرکت آمازون کشته و ۵ تن دیگر زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/687810" target="_blank">📅 00:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687809">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb69f7c693.mp4?token=jjJ5MT5hKgCbX1CDW5j7SK5H9oV5hR1DZ2ZbD_MWx9lU6UkY4zFuy_qGbU3Z5H7dQh3qrRzLLfaIUQlk1gAI9OYoOgSUoxAoDYjNx5tS-M_9o0Ce4agzJa6yhbv-I4QnGHNLyVous6Vt8W5UtVXXKr83tVq2EAx-hzBV7D-piui7eEcl4TEMZshHJR8I-7JnQl2s0gahjaUozWuHF4YqhRdvUYlPjT-KQGeOruqmhNPbzj_-p7LMrSUUoYd3ZXudBhe_RXrZyY6d1s0CUySEPblHoQTmYqCQATdrIJy4dAlsscfjCkFcrxZS-LamOp1ql_pu_R_rJ_u7Pa8u7kDESoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb69f7c693.mp4?token=jjJ5MT5hKgCbX1CDW5j7SK5H9oV5hR1DZ2ZbD_MWx9lU6UkY4zFuy_qGbU3Z5H7dQh3qrRzLLfaIUQlk1gAI9OYoOgSUoxAoDYjNx5tS-M_9o0Ce4agzJa6yhbv-I4QnGHNLyVous6Vt8W5UtVXXKr83tVq2EAx-hzBV7D-piui7eEcl4TEMZshHJR8I-7JnQl2s0gahjaUozWuHF4YqhRdvUYlPjT-KQGeOruqmhNPbzj_-p7LMrSUUoYd3ZXudBhe_RXrZyY6d1s0CUySEPblHoQTmYqCQATdrIJy4dAlsscfjCkFcrxZS-LamOp1ql_pu_R_rJ_u7Pa8u7kDESoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریسک‌های پنهان صندوق‌های بورسی چیست؟
🔹
چرا این صندوق‌ها با پلتفرم‌های خریدوفروش طلا و روش‌های دیگر سرمایه‌گذاری متفاوت هستند؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/687809" target="_blank">📅 00:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687808">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e13df248e2.mp4?token=uXNpYxF3QtrsFAYAuMiLoIBZfGVJUwgTm9lrIaK9n2yEGbrc2gZC8GLRrpC8-Uexi9TfRjzNg2pizef5TjC6WbQQaHnR8Wu9VvuXwvQSWzzzcshkpc1f6HjGQ2Hp7ghww5y5f-sznOpbg8ktf3Hpv2NuBC99VhUuoqys_e0afAOsrsyC_AaaABngg4dNcK_V_YwHmAO436lv_dU-BtOPw4JTlecADRazJw6JbGrx-xKU2qw8b-7PNANaZwtxqdRyG1vpHhNM1PvhWEXWRSZuQxdfgiEgzwm7zqWZk3bA_rsXpSmqtY4Wu6dh7YqAbtuO5lQBc_pMQKVDf_wSqgNa9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e13df248e2.mp4?token=uXNpYxF3QtrsFAYAuMiLoIBZfGVJUwgTm9lrIaK9n2yEGbrc2gZC8GLRrpC8-Uexi9TfRjzNg2pizef5TjC6WbQQaHnR8Wu9VvuXwvQSWzzzcshkpc1f6HjGQ2Hp7ghww5y5f-sznOpbg8ktf3Hpv2NuBC99VhUuoqys_e0afAOsrsyC_AaaABngg4dNcK_V_YwHmAO436lv_dU-BtOPw4JTlecADRazJw6JbGrx-xKU2qw8b-7PNANaZwtxqdRyG1vpHhNM1PvhWEXWRSZuQxdfgiEgzwm7zqWZk3bA_rsXpSmqtY4Wu6dh7YqAbtuO5lQBc_pMQKVDf_wSqgNa9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کیفیت دوربین سامسونگ S۲۶ اولترا!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/687808" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687807">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd0ad2cc1.mp4?token=BzBomZ-lLPLEIoBYQ0drV0FR7llctZ1d89lIGk2OuNLgBqzb3TrY4RDmQIQ0ZV0D6HD94Q108XcLUJImpHsu-um3vV57CUNDJ06yYTwMzS7SsKlX1SzDJpjw6h4SGzpNT6INekSK-7mBwmy95FVGOl9cdVzE7C3Rry0hpAaFpG_8c2pMUFuO5QDH_fYL3TdgoocAfyeMh_U8zMwdXHVh5jSY0gllCuv_8WMIhKQoQNxKHnkBiml42N7BDGCoApXTTCOikWBRw079lqLFh-Jp42nEs8hZv235Rg4GyRccOrgA6ZhpOwMB3P2aGQ_qfwW-L2kcpNp6Cv75Ot36qGE3Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd0ad2cc1.mp4?token=BzBomZ-lLPLEIoBYQ0drV0FR7llctZ1d89lIGk2OuNLgBqzb3TrY4RDmQIQ0ZV0D6HD94Q108XcLUJImpHsu-um3vV57CUNDJ06yYTwMzS7SsKlX1SzDJpjw6h4SGzpNT6INekSK-7mBwmy95FVGOl9cdVzE7C3Rry0hpAaFpG_8c2pMUFuO5QDH_fYL3TdgoocAfyeMh_U8zMwdXHVh5jSY0gllCuv_8WMIhKQoQNxKHnkBiml42N7BDGCoApXTTCOikWBRw079lqLFh-Jp42nEs8hZv235Rg4GyRccOrgA6ZhpOwMB3P2aGQ_qfwW-L2kcpNp6Cv75Ot36qGE3Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشخصات دقیق بمب استفاده شده در حمله آمریکا به عروسی کوهستک اعلام شد  رئیس کل دادگستری هرمزگان:
🔹
بر روی بدنه بمب، کد شناسه نظامی و دولتی ۹۶۲۱۴ ثبت شده که طبق پایگاه داده زنجیره تأمین دفاعی ایالات متحده، به‌طور انحصاری متعلق به شرکت تسلیحاتی «ریتون» است.
🇮🇷
…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/687807" target="_blank">📅 00:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687806">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHK8uQMXvyGF_Cpny7bZmnjCMcu3TtFJ3HH2cL-J_PrjPEWukY6_PhlrApg1fyOoxqdZp39iuqkhgp8-EWxkE96lgPOyUdx8vSDWRdUNXKbI-oCVERLzoCEu-gQIxrm2CRh8wUJZQpHjEKWXEGxi2S2j5at7eMleexKzWBtb26jvZ5lX4xCD3oLDhu3vySfP6UvNx8-0CCfAD9RmGj3IqefBw8Jtc8PrOnkXGkBoGRARfZF_z_i-Aye6ORtPMts8JrNnQJcqaUbce2xtcEfCTvO_Yr7CZZztu7uqcWbu2vQj_opJBMHiwV22bOr9JBWmTZw0ACDeOKKl3zo2NSJ9QGzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHK8uQMXvyGF_Cpny7bZmnjCMcu3TtFJ3HH2cL-J_PrjPEWukY6_PhlrApg1fyOoxqdZp39iuqkhgp8-EWxkE96lgPOyUdx8vSDWRdUNXKbI-oCVERLzoCEu-gQIxrm2CRh8wUJZQpHjEKWXEGxi2S2j5at7eMleexKzWBtb26jvZ5lX4xCD3oLDhu3vySfP6UvNx8-0CCfAD9RmGj3IqefBw8Jtc8PrOnkXGkBoGRARfZF_z_i-Aye6ORtPMts8JrNnQJcqaUbce2xtcEfCTvO_Yr7CZZztu7uqcWbu2vQj_opJBMHiwV22bOr9JBWmTZw0ACDeOKKl3zo2NSJ9QGzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شهید سلامی از دستیابی به تکنولوژی انهدام ناوهای هواپیمابر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/687806" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687805">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=okG1hgFV2B-QrOoREvKjP6klJCeravzcjjCrfL-sG4Sgl_1xR0Pjh8pOeTX1-z3w-_FNUCniokjJGKvUjIWfmETKlNX6MsCNtFfis-r5PZrB5L5UtXdmE4_ZkEg2cz5rRWw1REmUrHDdxI0TSYix5LY_N3_kw0hcRkjvGhLdupexpcyMz27wTD_T4kHlJ0ARd6y18tZPV6jCNIkwsyvaoe2Mrog8emCNEQ9HeI4Q8UEZOCvdlFCHDpUpSs2jnk9Q5zls99a6vT6GyeEVry8ISJQUUmAEkMIHURg_pAUeowQyaskfbG5PFN1kLSJ42EyLd7SIJcjDN_UJzJ9TaAQ64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=okG1hgFV2B-QrOoREvKjP6klJCeravzcjjCrfL-sG4Sgl_1xR0Pjh8pOeTX1-z3w-_FNUCniokjJGKvUjIWfmETKlNX6MsCNtFfis-r5PZrB5L5UtXdmE4_ZkEg2cz5rRWw1REmUrHDdxI0TSYix5LY_N3_kw0hcRkjvGhLdupexpcyMz27wTD_T4kHlJ0ARd6y18tZPV6jCNIkwsyvaoe2Mrog8emCNEQ9HeI4Q8UEZOCvdlFCHDpUpSs2jnk9Q5zls99a6vT6GyeEVry8ISJQUUmAEkMIHURg_pAUeowQyaskfbG5PFN1kLSJ42EyLd7SIJcjDN_UJzJ9TaAQ64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدیدترین مدل OpenAI بدن انسان را سه‌بعدی شبیه‌سازی کرد!
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/687805" target="_blank">📅 00:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687804">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c7abcd69.mp4?token=H25X2sUNfRSzwxZ-_PXtaFEsbwx-rEt0HBnVZP2ZLRY8wzjF_rSFYsmyjpVq3sjNX3lQzmfuXvi91OT4NzXKua3LjBoK0lm-CUTd0rZdb8SJaFZ7ju6PcurUXLhhflGI1UiANATQ1lxPet4A3y6rWwydmzAdIYLihGqnSKk82QuJBVsPZPoqzGdDqDc8G0jVwTe_p_oqyFUFAPkanFrkZjEJYNDg-E18Vfy2RTPDDCHz5--1ywrHODKJpp9HHZrBUd_1QanuTmNO-n5uR6fst7xcIveerBTHt_Mr8MGf3Uz88gROF1uBil-RFoJ67YfDmZr_Pu8O_keyalrnKqiimANh7y7nltyLxbrmE4nnh6lKn1wKtAxHinfkp32B9Ongg2jr8BCvRNYlbCiu_l5XkR46gImB4cK8z_Nv5iKt6_wnd80B4nEtk6PpK0NpYO3eJ2RLNtjPm6becoPrMdDq0oWPtvR9qk_6WqPvMg2TweKcDydKUyWajJl5NmDNgQEXLaSraxpqZh9k3w3oQ3p0MN6yTlQFkbmkujfNHTzaYvmAD06J-Qk40nYN24TUnK95fFSokwG20z6BPmxV3pBFFpW3NOCFN2M1E1TtY94dYPqfnWktrf3o5SVRIEQz962o0sQobSQYMY2siJKTI0M1fQYzJLh7aegKR5yi7PoQMO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c7abcd69.mp4?token=H25X2sUNfRSzwxZ-_PXtaFEsbwx-rEt0HBnVZP2ZLRY8wzjF_rSFYsmyjpVq3sjNX3lQzmfuXvi91OT4NzXKua3LjBoK0lm-CUTd0rZdb8SJaFZ7ju6PcurUXLhhflGI1UiANATQ1lxPet4A3y6rWwydmzAdIYLihGqnSKk82QuJBVsPZPoqzGdDqDc8G0jVwTe_p_oqyFUFAPkanFrkZjEJYNDg-E18Vfy2RTPDDCHz5--1ywrHODKJpp9HHZrBUd_1QanuTmNO-n5uR6fst7xcIveerBTHt_Mr8MGf3Uz88gROF1uBil-RFoJ67YfDmZr_Pu8O_keyalrnKqiimANh7y7nltyLxbrmE4nnh6lKn1wKtAxHinfkp32B9Ongg2jr8BCvRNYlbCiu_l5XkR46gImB4cK8z_Nv5iKt6_wnd80B4nEtk6PpK0NpYO3eJ2RLNtjPm6becoPrMdDq0oWPtvR9qk_6WqPvMg2TweKcDydKUyWajJl5NmDNgQEXLaSraxpqZh9k3w3oQ3p0MN6yTlQFkbmkujfNHTzaYvmAD06J-Qk40nYN24TUnK95fFSokwG20z6BPmxV3pBFFpW3NOCFN2M1E1TtY94dYPqfnWktrf3o5SVRIEQz962o0sQobSQYMY2siJKTI0M1fQYzJLh7aegKR5yi7PoQMO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدواج با کسی که سابقه طلاق دارد، درست است یا خیر؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/687804" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687803">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
برای اولین بار کاربران سکوهای داخلی از سکوهای بین‌المللی بیشتر شد
🔹
طبق گزارش سوشال لیسنینگ دیتاک و بعد گذشت حدود یک ماه از وصل شدن اینترنت همچنان جمع کاربران سکوهای داخلی با ۱۱۷ میلیون کاربر از ۸۷ میلیون کاربر سکوهای بین‌المللی پیشی گرفته است.
🔹
در همین گزارش به استقبال گسترده فروشگاه‌ها  و کسب‌وکار از پلتفرم‌های داخلی پرداخته شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/687803" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687802">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5QpG0ImV7Dal3wOBG5FO4o8zqkpRiVDfzZb6-y00DiJZXK3HmPzXGEfXhZK16F6mqgIiDEfe0FE-TVZ8EcF8yReSrmCeN1L4WuMRf2afzBByAH0psoLlKpASjGoC98UaB4vKEMuhdiqQkYbcJxhdRi3GjF8bTOdfzyFbjxKROhfIPrbeurQlh2hBDw6nLhpxXdYKaGxAbWgV5hLZ16k3Jpko1QJhy_nwWdkSmKuKYOHaOHeMw-qk6Pgog02cco9ypQNj5DxuF4iwpA5OitfvdkZJnpjWLFPUje_vgvq6Xz6AgqOMk6kRPScwuaqVude6375twi8w2auqThS760Mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/687802" target="_blank">📅 00:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vI9CwUddgmdV-E7UP5dIpzFFAPWLSbb1XBFUW-snH7_cpKILFHN44eqZlVPKlSlUnISUz1OruDbBz4jm7pjUKV-qnk5pdk-UbfbfdrtFDeFkfudStv7cah7Cz10ukrONrM6COg-e4cuJetgRtyh6vl0OqM7uwQ50XWd2RUakMXnuaSEY7y8PGX7C-PoZzlkqfoRRJGCtyxYi4rUxkqJ1rFLKj9gi9myX1zH-50WfR0wVX3VtU_JXyAeUtBwCSNXmv8vVR_o_jC1_8wMC98VPCZbWsMyNfcaCPQRZ0WopyHJoBVwEQVYThV15rVsU8jwEKy6IBnDvxqnm1F8x40BGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFUe0DwQB-485B3SGIt5eHFyvseWJ_dHSWvn-KF4LecI6sPp3AEGI1bTHp3dNb7XcJ-PCyTjDVjlUj8V0a3Z0OgjiFPlUNB0Dp-l-BUfClUFFpPTja7k1L-q8kX7K4roMNP8Gm559lM8xplleUf0sycS5jR08cKEP1lxqbViXSrJEVka_cBeSc864wnEO0IFKgdTDeeMurMo7dlczEcstw0qUuXqWLnKl4PwOkT846zvsqVQlFTwsioO-H6qlo_a_8539bToNWY51aV3DQHZpYcp4u1vu9h986etl3ZTaTofKMEzx79pjwyM_Rf_JBofXIdGUNFoit5PzhvGJBEQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQVk76N9S--J7zfKd5IFCXVviEPqPcp6RmKCD5EYWMZH3zGIh5VNfLFzK23oYOK9MLUraOhjGGUfMru028FeonX_bRV6N5QLjFLjMTjVriZpv7DqNDZcttqXpEJIHna8dFkHXvbPAigw-gfhuL9Of3fwEK4wyvoUtXOfkpzzVR6Bv59BRow7vzRHrchKbYooHV3wcE8_Hdh8SgR_QbwTyDJISBOpPdPMKrXySb7pD_9Q_bWzDl9mOeEC5jLRnjvxwvZy3DKfwp-LHDAxd_SKMI9g93w9b9F4U9lyabj2tABVZtrpHFAUFqB9zml01hf-24TgoMuIj62Uu1Z3rWGKqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ارزان‌ترین سبد لوازم‌التحریر چند در میاد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/687799" target="_blank">📅 23:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
زمان اعزام عمره اعلام شد
سازمان حج و زیارت:
🔹
بر اساس برنامه تدوین‌شده، اعزام‌های مرحله نخست عمره از ۱۵ مهرماه تا ۲۰ آذرماه پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/687798" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687797">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: با یک حمله موشکی دقیق، جلسه تعدادی از مزدوران سعودی را با موشک بالستیک ساخت یمن هدف قرار دادیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/687797" target="_blank">📅 23:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قیمت بنزین برای ۸۵ درصد مردم تغییری نمی‌کند  مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران:
🔹
افزایش به صورت تدریجی انجام می‌شود تا امکان انطباق برای استفاده از سوخت‌های جایگزین فراهم شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/687796" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZC7zRmnxs8EhRxJ-qTvhf0_SlydpZwsdLjPCNlf7ijMFM1ZYBLAmH7wZJnGm7ACNenix_7xGoez52m8iP7q2lVsuQ0GnKpKV7RNV0wZ6GbgioaoMS6LFv7q5IpUuuzpQA0K_wX25qolHa6RTS5FdJ8jSgRi9OdX4ZFt59FPRSPM1FXLJbEo_az8ag1tXiDugat8ZIqzeObqpLnVFMtc6GOi5vPYREfa07aG8ByMMgb7xA0uK21bvHzJu9dFCNTlkFgFb6JK1qfNOcAyLnEIHM5zZWEq75vZVAfllWhtncYYH2ZBObMuYVeNbykni4YDaxHtkn0M2isT7vApSiuvs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dK0z1vIsxh0E2sBALPb-C4rt6S4aTxxtnEhs4-cPdv8-_CndxkF0JMaz1UTEO-C6lZCxoaqhdqti-O3c5owOdk0t4gzlwntni_MCVBEGm-kVricBnFKJnSYUvb96LChgf-B4ZgO2Af9-XvYpAaPAsnRlURHVRDfQGUdt-R2Q8KLobE_SPJ04aaOMcQM1resW5OyEkp5LO_f7WMoZhUToB5xafHsEpmHARLv57jnRDL5hZzj2krjAglWutMOpveE9Waa38XtK24fn6y7VAqd3V8M38sEbYYe7uDdtWyJIeRh8Y9HyDxFZdlz2bjm9pGnVHWeGmmK5QNKOO5LcQtZwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPi7zld6j9XIbUy7Yl3LoZck_PiZL8PyGGJU99dArURn7bd7yppAOpuCh4QqR00Elxdomp12War1gDAXDW8mwsNM8CFILgNDyPhDJzhWAT4YKUT4BoOU-dY8hjJD_La7Ocjv1nS19PCt7l8swneLtjQI8XeJUY24llCCc67Hx3Mh8RVJ7QrhlJReNQxue25_8D1cn8pNdGj0MRrlyQx-vGv2APnPxtnmfy0Bl8k2_xJwuHRjplnoRXqJ9ZkfiusQ5VwQO08CGhv7pQYfs6ariLyR8COXc5tVeytiAmtsDqw-MWfphdCUMibaKgajtgi3dF5AO-0DxEgwlrVz1SW8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMD4na6AvM71TME2QTCDFDOvzcwAR6HeFxPmIycFoqTNK3Z25CoE1rVBSDqqCBeRlxY1trXFM8ziZb-Uvp0EE5iMBKCzViwp-l0XETcfYcQ3pXr3m-fI_HJnRzkR5Gh9X58E-TeJc-UxkadlYoEjcx9gLSKmKe50wrzVJCvLO7dvNZFxCV6VNHds0BsTwgbHhJNGVBwxg6ATs1Sp11B0mtOQ-bnoKV971TjmvU9j9_DLn6NIEwO_ikeXKQm5hLM52T_Q5EUosGqNaDmc8m8whOlp1502o1CPokDzCJUra6yoEhle2_uNxLnks-Vdkw7F_0dQjvwWpj9z5F6BGVmC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pie7OzSh1eeFfW2asP7IGpPK-BgBEq_PYfoc2UUS09XNfJTHCE9cy1es80QHk6tbfMGg6i1_D_-ADPcNIjn9ZmRGtkgb_My8M6CI2dxmXGnytdhKEZfqEkHKu5AFuyg-BRw0fd0tcKsAOOGqXe5ucP5bUcO2M6V7mKKcJHDL-3d0eJ0BhK37J10ZgCxf0iz89LN8yF268PsMEMD6NnloESGX6pCRlebNK9mNfyi1M8Fa-acFHILad5KBLo5NykxTs8y42C4QlY8Z4x7N5vZDSDtVmXZIgxr_Kf0mOZw-aOER2Aq3fnRRMcS8rQx1PcWpbXaLNTovLxf8cEIKvjQhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U12a_wLjZd56VWL4en5KojufYXatJx8FL9SpFqUzIeM4Dz1mWbnm9oRBOgkiNyLEc30aXnLL_vTQ4lTVnqG3Tv2qSTGKfxKAYQtWQULlPnBrLiGSxhDwq3MW0aDin_DzZjxoTgSi0n48GA_xYo_mPMwKfRtR8JRK6mATNs24jxX5gc01Z4iZr_VErzLaMn2n0Db1pCOTT2Ouk0GuGcr6wGXSUzxNZMGhcWZ45k39cSt6zoBML-2Y_utkUrcZLlVsufoTEQzINPG1JLIilZ3EJAmCCotFm7wV5ptq1mHQm9cfuUZlPcoh_96928okbAg_QA-jsWqZOJ_TRzAvMrsSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGhuKfSuhzq8NAafRRN10a-orOPTTMJMsehKP7LIA7ymdbn5bJFkTV_ZIa5FoL5bzjq2W75XawcJ3COomjyU_XiZc0Le1Y_ZPVMfkAHRjX3wliftz139w4NJ92-wGIba6LsLZsWEqT_93ZoH9PTwfDHyfKNmrxVYJGSniKkO2QhLX8tTasXrYUsM9avtxWkPVXP8jBN8w4A-dfZQPqblLNEkapskjyXAZWumRFcEG94ceNEIQuB5s-2izw5JBNTSN6gF2a3wHuKriofUQVjldvk-8lu6Mowal2iFrDPFMNO3DhUgJc3ELfg8z3qFLWK0mOTmWYMWJscJgr-2Sq7IAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ0_fNpCqyxWBneQauAvhKfbC5O8J1Ynzi5TnE36-VF2A12L9RyuNAZrnmEskm7TCmU0aa5qq9m0dhaKOeGzSFXMCysm5xyZHT4vuUqbnnYa7MzRfpJsBlZ7x7zUcwLWSdzOuljZA4wSuzi-WWT_RImHRvVW6_QpaptCTCKPhVl0_sZpl5wV3EvPf4Tmvt3VYFuPD1rYiulg5zL5W0d66WF5R0u-X6WgD3okWas0ZbOnr0pZH24XbQgJZoLWn-1aLlmFrf9aeMVOsutpf_c7vFt9DEkd7uMBct48vo2asjJs4WBnVMMJNHeNAmLS_pgFmg2_nWOOcYSnYZiF-Zwwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf-KBDLqk2mBF48h_uI3NQSNMbxHmjvUeUHyozrjAw2JZbDrtxCmOlUJ4SY4YRxK-3xGqyIxSJRBoIOdIYsnK2vyHmhvF77n0EmiXveivEe4hz77_YmtIVqBCPOFVNsl5XRX4KfCDgTbVbkI3lRTZAnFm86Mz59tuU2cJAyJis5J23iw0J3TU2Jbd7t1UzAqV_fGmJxiSwZ3KdGaAYsW4Wnu1p8xUjOGEGQDpyDJxM-fwhCQRJpMGvQp0XIHEmw9yPd81WmpdQJbyWKT833R0o93Z4832gmqipMlZIibn35ca_zJd6c_Fu3qPN7x8YreTrbEYRPrWvco6IQiR1CJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVwwASKfMY0bxqVmdpwRrgnu0oEiAAUmMqT4J0QX9WfPVb-cGbCfh-cH2AgbrCnGIoclaKN6jETH03YoyiVzoXODz2sXK2bK0-OZgA_2LY7rQ7r-XAn7ZncXOHfsM9X8_fci7nhZO3OJgRs8ZhvewHZict4c12jrs4mSnmRZnBFAok-7xUNYcclTdAkcc-Ny6w0_TkYgd5muhWbJ6CX7wtpdpeKn9DexGf3hjIfh08E8_HUxBbYG7le3O8HjAOl8YVyG4gBPUoV_dz13zTqC2mdpqFObmjcwulXsAp2tORNdsEgNekOlY88hlLZN8j4yEK8x4d8LoxOyUBCGpciLMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
بازتاب چالش های مخاطبین الوفوری در تهیه اقلام دارویی موردنیاز
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/687786" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/687785" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قبل از خرید دلار این گزارش را ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/687784" target="_blank">📅 23:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=nLnJKHbuO0GLR-dOq02ITDR_tX6-Dq14sLmTRYVBQK4D3-gI3C4gm64zLJSIdX0Me-VRd8pfE9f4eAxIMLapCA0AyLzIQM0q0gRGrMjHkSbwPbdO2kZlj3tFyUCpiPTQcUJif2pLeqy_lM6cAsmglciSQE0oBo534x8bYx61oUF2EF3VDu1K9UGhniKuy1GM_YAi9xYWlZNrC5w_45j6T5_Jz6-OIptB3PYh66nD0GQps7esMfjXjj9VTr9SKiHiPvunJ9Ib91-S8o5U0ZYAYygZT5XdLb3Iv_x3OrCIp9CzU_wR06K2LidvITR-wgXR0fODYXkXjbk2I-b1_eOKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=nLnJKHbuO0GLR-dOq02ITDR_tX6-Dq14sLmTRYVBQK4D3-gI3C4gm64zLJSIdX0Me-VRd8pfE9f4eAxIMLapCA0AyLzIQM0q0gRGrMjHkSbwPbdO2kZlj3tFyUCpiPTQcUJif2pLeqy_lM6cAsmglciSQE0oBo534x8bYx61oUF2EF3VDu1K9UGhniKuy1GM_YAi9xYWlZNrC5w_45j6T5_Jz6-OIptB3PYh66nD0GQps7esMfjXjj9VTr9SKiHiPvunJ9Ib91-S8o5U0ZYAYygZT5XdLb3Iv_x3OrCIp9CzU_wR06K2LidvITR-wgXR0fODYXkXjbk2I-b1_eOKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/687783" target="_blank">📅 23:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f11a95fc6.mp4?token=LXeM5CGMzHNxXxkJOf70IbTMzih9TbWVjmHgDnNGSY-WOD6BUbb4bThgaus99l-DvRiLFbNjjDmZ6DXCunFBzVyHtmRC3b0fyg9X0ys1jxVg5k0Wpx80BHnN8sr3qajW1XFQJSsF1BVcYCH9NN4aT8A2E2enSQ4P4JQR2FSGad-Eu5vcdaWOXVj-q7SUaWFjziifMnlcSiIK2rLDvH5WuIozGEpIUOWBg0_4SXLMdqRM6lr3FBZnrHCO2kCaMMvuEzBqsHzyRjvuyjR0UL7xAOhobx-q8qcqjrtksyfhCT58dBgO_P5vHejqARbY2YWydNFCGFFCzLe90eB9M3iW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f11a95fc6.mp4?token=LXeM5CGMzHNxXxkJOf70IbTMzih9TbWVjmHgDnNGSY-WOD6BUbb4bThgaus99l-DvRiLFbNjjDmZ6DXCunFBzVyHtmRC3b0fyg9X0ys1jxVg5k0Wpx80BHnN8sr3qajW1XFQJSsF1BVcYCH9NN4aT8A2E2enSQ4P4JQR2FSGad-Eu5vcdaWOXVj-q7SUaWFjziifMnlcSiIK2rLDvH5WuIozGEpIUOWBg0_4SXLMdqRM6lr3FBZnrHCO2kCaMMvuEzBqsHzyRjvuyjR0UL7xAOhobx-q8qcqjrtksyfhCT58dBgO_P5vHejqARbY2YWydNFCGFFCzLe90eB9M3iW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر سهمیه کارت شخصی و کارت جایگاه تمام شود مردم چه کاری انجام دهند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/687782" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687781">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
معاون وزیر نفت: قیمت بنزین تولید داخل به هیچ وجه تغییر نمی‌کند  عظیمی‌فر:
🔹
قیمت سهمیه اول ۱۵۰۰ تومان و سهمیه دوم ۳۰۰۰ هزار تومان تغییر نمی‌کند و این تغییر قیمت که بصورت تدریجی انجام می‌شود شامل بنزین وارداتی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/687781" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687780">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
رضایی: الان اگر پهلوی هم روی کار می آمد، [آمریکا] بلای بدتری سر او می‌آوردند  دبیر شورای عالی امنیت ملی:
🔹
تنگه هرمز تنگه جنگ نیست، بلکه تنگه اقتدار ایران است
🔹
برای داشتن وحدت باید به رهبری نگاه کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/687780" target="_blank">📅 23:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687779">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
معاون وزیر نفت: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/687779" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3882c73266.mp4?token=DoroqG93b6usajfPm93MTCh0hIsz9bVSB0YuMYIsCcYGeoiW-wOscwaihUyE7edqxFDdWMKclV_-5lWC0qehL-GganNb64I7ZL_gm8WFkZ93mcfgNUSx-R9vpl7BvIRZOiNFpCbfpZ_3xf8lNR4YnEmbYt5SIBbm5LjyE_C3zuuLWe74UBKZKDCqx7jBLqyg0z7eAQx9i6MLpzzTtoX1yiglXa-J7xPewY2R9q3PG2a5lb-cL5_64d70SLCsM9-yOQBPmF0vjPlvUOYjDM8hot_6PqHtoVORDOax8avbwFjzlIl4vesHPbobVeHCSROtZunNjFWhxtvNXtamIzcLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3882c73266.mp4?token=DoroqG93b6usajfPm93MTCh0hIsz9bVSB0YuMYIsCcYGeoiW-wOscwaihUyE7edqxFDdWMKclV_-5lWC0qehL-GganNb64I7ZL_gm8WFkZ93mcfgNUSx-R9vpl7BvIRZOiNFpCbfpZ_3xf8lNR4YnEmbYt5SIBbm5LjyE_C3zuuLWe74UBKZKDCqx7jBLqyg0z7eAQx9i6MLpzzTtoX1yiglXa-J7xPewY2R9q3PG2a5lb-cL5_64d70SLCsM9-yOQBPmF0vjPlvUOYjDM8hot_6PqHtoVORDOax8avbwFjzlIl4vesHPbobVeHCSROtZunNjFWhxtvNXtamIzcLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا گلزار: قدردان شجاعت، فداکاری و ازخودگذشتگی عزیزانی هستیم که در روزهای سخت جنگ برای دفاع از این مرز و بوم مردانه ایستادند/ در این جنگ جای بعضی آدم‌ها برای همیشه بین ما خالی شد. رفتن دانش‌آموزان میناب غمی است که با هیچ کلمه‌ای نمی‌شود حق آن را ادا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/687777" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ae421f19.mp4?token=Rk_vOWBy60tBVQYF_uWOPuwkTgqA34RfjCozZV5jw6s7QJVztc0yb4tosd12h_65udiuRkHqS7xXw0yZHO8cPgOHTE_hX2D5eEj26Gm9DP1BqA-5VXJktwaeEryXW7N-soqBG5S4mupnLQeAKY0Y6N14zvej0EjZSDJYUxX_iCpuS7RsYpltJKyyn4upXKgbXkSpDhJWKwgt23N5zcZW014-ktZDP1nKCRV5hcZjvtu80Bby3kGPXVIvYb0K7xBIXc8K53aXcGRV4bJRQNxeK9veX1hdAriaTd9rANkHYPX0GJe4_UcfosYP3fo2ZpmDUouqsa8-emmXViM3vkUgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ae421f19.mp4?token=Rk_vOWBy60tBVQYF_uWOPuwkTgqA34RfjCozZV5jw6s7QJVztc0yb4tosd12h_65udiuRkHqS7xXw0yZHO8cPgOHTE_hX2D5eEj26Gm9DP1BqA-5VXJktwaeEryXW7N-soqBG5S4mupnLQeAKY0Y6N14zvej0EjZSDJYUxX_iCpuS7RsYpltJKyyn4upXKgbXkSpDhJWKwgt23N5zcZW014-ktZDP1nKCRV5hcZjvtu80Bby3kGPXVIvYb0K7xBIXc8K53aXcGRV4bJRQNxeK9veX1hdAriaTd9rANkHYPX0GJe4_UcfosYP3fo2ZpmDUouqsa8-emmXViM3vkUgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ میلیون لیتر کسری بنزین داریم  مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران:
🔹
به طور میانگین روزانه ۱۰ میلیون لیتر کسری در بنزین داریم. البته مصرف نسبت به سال قبل افزایش نداشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/687776" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=Gn1NDB-Q8qw1GMx9WKznkT4mCwhItVFXHsRhto_TDrna0JKDnyzlY2cKhnAn0zavDBLxF8BAhaADoYgvobl2nm9xM3Ws910MWffS5nbEdIXaaDQgzpDUtfnfEda3GF9ODaIdP-sflgKcasFQ0o-q8Gy1pWzuHVKbj6GsmgBlvL5dJmvC2Y20rvwWr56DYwftuZvcHdPGMjyzi1P8qcG5K0FaCePcHCCjbfL7TW7JwUocUcynTPWKntxVdeykFbJjazFYqBRqLMuLoxJkjxDjAPs0_545mHYHtxWGkSnmKFdWsl2QkaccT4HXsHQ6W7KrouWFl0vn7XPqKQ9aQEdf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=Gn1NDB-Q8qw1GMx9WKznkT4mCwhItVFXHsRhto_TDrna0JKDnyzlY2cKhnAn0zavDBLxF8BAhaADoYgvobl2nm9xM3Ws910MWffS5nbEdIXaaDQgzpDUtfnfEda3GF9ODaIdP-sflgKcasFQ0o-q8Gy1pWzuHVKbj6GsmgBlvL5dJmvC2Y20rvwWr56DYwftuZvcHdPGMjyzi1P8qcG5K0FaCePcHCCjbfL7TW7JwUocUcynTPWKntxVdeykFbJjazFYqBRqLMuLoxJkjxDjAPs0_545mHYHtxWGkSnmKFdWsl2QkaccT4HXsHQ6W7KrouWFl0vn7XPqKQ9aQEdf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/687775" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اوراق بدهی در مسیر نرخ‌های بالای ۴۰ درصد
🔹
ابتکار دولت برای افزایش نرخ بهره، معادلات بازار بدهی را تغییر داده است.
🔹
متوسط ریالی فروش اوراق نسبت به ۱۰ هفته ابتدایی حدود ۲.۵ برابر شده و تقاضا برای خرید اوراق در نرخ‌های بالای ۴۰ درصد افزایش یافته است.
🔹
در این میان، افزایش عرضه اوراق، تنگنای منابع در عملیات بازار باز بانک مرکزی و رشد انتظارات تورمی تحت‌تأثیر دلار، همچنان فشار برای افزایش نرخ بهره را تقویت می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/687774" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1mKLKNAJMzkXBT9vrNWz4I8dhHSfUGAlXumB7D-298xKR6Pi42mfWK_JqPgXpGvTzf63Gpz9fzFbG8GSAWq6eioud7f6ejm1cw68LbvuYtJJj7tFaJCALUDnzM-QpjudugOZgmLxKdRfJS0boBQlmqYBoCp9WL-qyK8JGaoAKmYonEsZ0G2tKx7YpNvyML5qhvgvQdwLGAkK7meEPaTxTSR8TLZT_9S0T2DOU-ICezi2WkEBOAkx4hx0UbX3EM6nWwGwj5a-Hb4bw0YCFWjMOTNAyKl1waR2YExnhGLZUm0skDzTqaofF3M36563NNG8Z5Zgi3RtMCOPYcyu8jaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون دفتر عارف شایعه «رفع فیلتر پیام‌رسان‌های غیربومی» را تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/687773" target="_blank">📅 23:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک فوری برای شیمی درمانی پدر سرطانی
🔸
این پدر بیمار کارگر ودارای سه فرزند دانش آموز ، برای هزینه شیمی درمانی نیازمند چهل میلیون تومان است
🔸
اینک برای درمان وبازگشت به زندگی درکنار خانواده نیازمند مهربانی شما عزیزان می باشد
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
6104337806663215
شماره شبا خیریه مهرمبین
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687772" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsLJQNtijq26CBaqPj3ohkGRwC5NAQQs4AJweMvIMi_QI0RZ89_ELJJzuur1XR9Oav1t6b7gHo-ET9-uHbUYQ7RTzZ24odUDOLNJO7BYQJoOOVA51Kd3AnHVdVALgO4Jed3XQYzwBrE1rfb-Lkgb09bsYDxAjDpZkSajMm8lw0ioklvbf7f2qKK7yf4-CTSnVuDxOusKtbsLgiQVnNDm9MGTXmnE9hctD0E8znlJhoOf8UgEH14ainxvV2Y7dZuiROy9t1rnGz4wArC0EeGgatO6mCSjOTnnvdqealXypvpgeHbRFrbCw7hgtLYQ-w_t9j5ub6nIE9ghaUBOgKtPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام پایانی دبیر الکامپ ۲۹
برای آنان که ماندند، ساختند و امید آفریدند
چهار روز الکامپ به پایان رسید؛
اما آنچه در این روزها ساخته شد، تنها یک نمایشگاه نبود.
در روزهایی که ایستادن آسان نبود،جمع بزرگی از خانواده فناوری ایران تصمیم گرفت بایستد، بسازد و به آینده امیدوار بماند.
#الکامپ۲۹
، روایت همین ایستادگی بود؛ روایت شرکت‌هایی که با همه دشواری‌ها آمدند،غرفه‌هایی که با عشق ساخته شدند،
جوانانی که با رؤیاهای بزرگ قدم به نمایشگاه گذاشتند
و انسان‌هایی که باور داشتند آینده ایران را باید ساخت.
به احترام همه شما که در این مسیر همراه بودید،
از صمیم قلب می‌گویم:
خسته نباشید و سپاسگزارم.
متن کامل این پیام :
Elecompiran.com
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/687771" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
