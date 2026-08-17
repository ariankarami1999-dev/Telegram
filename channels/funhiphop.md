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
<img src="https://cdn4.telesco.pe/file/tG_4aCD8ErDuNRHHafT1sYF8YcysnBDZS7LgQ1tj4tPnnqsm9WZf8zabQsW2Ems6WfBjoSVT2ssIWG6Zur1m5EMoY9rvAQGb4J3Suc_uJ3HBA09YGukWV3fSu8dIFQB5Lazmq_FM26XgEB-865_8AUHNM35HQhKpqJ6QDbxJm35TuZMOIF0XfVDabKo6kleosGPQpC6CWtVZv23XaAfnpE9j-dpNd8K7AJJ6KWXsAWu2vovI8iLcP7_tjpiqM0I-k2m1t9Pi9LSQl7TLQhQ_JArZfDKsl4wzm74rXLY5ovnSzXWMAuSXAJryTV67QGsAmeW-IZCtO7QJk7hterKD6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 21:54:11</div>
<hr>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTaxrHwvjyDIX4VnDeoBIn-ocQYNw4_wgkYTQIoG9sqsVqcjJg0YmU6Mlue7fjaWgNnVV85WYUKy8eazOu2bRPmoy7RiFHDXxHESIUhL9wbE6hO_utRUMm12TucvHWyrYZvxGTt6r4ZQ-YLGQZXamBrRO_M6wqwvdxLsnaU17nrS6pH10vPV-6utltvJWF6heBBYtzB8R8c8-HgQ4BESvdeQvnGNDUDYKy70DYaydRgg63ET4kk2hdKdr8ND9w4cqKQNkNbboYDhNN-gyrmtoEIKFE7VzT-frKolCwx6Jr_S0XBxmrU_M69qo4iekZ0aSsEXeR4VI1ubJftV05zSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7oYtnNv3ojmAxPTyBNjXcmPKno_w2b7KDK-BW8zwXS4rLndtgxoOjCJypZwTtirIdidqeb2-WvvvRt4ZNw4-rs9med9DX3Ff0Ma9G5g-GxdlYAtN0imgQI2L2uM7bClMdApwYOK-E8l8drYPLItyJHij9b0VOvvDPr0Ox3KIhmBW2r_8Pb_YgxDGfnbrc5psisCeBMxvu7d1s2atiAPPrDtqqOsKEfpb1Xp4Qj9FW8C6i5YEqp_jJyYm8mP8SMWpjnTE3YElfShLNe0X5qCr8PnbGFxhm2eTFgz49S5QutUIJ6MFoVZLRCHBRs46xR1SVX1pJFMqVUNnLmt97V98Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونفر تو عروسیشون خودشونو شبیه شرک و فیونا کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/82308" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسرائیل مثل همیشه جنوب لبنان رو زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/82307" target="_blank">📅 20:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/funhiphop/82306" target="_blank">📅 19:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این چه دیس کصشریه کچی به خلسه داده
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82305" target="_blank">📅 18:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG1KVNcRJeGyXXUD28zkGRWeo-xSNrEUSLFuetaDhHqBwObrxBE3AozAzaMlpzchjdBuxEVpGHdAjaDiioDypN81ZgKn51PlCgyEIyaZCPsgW-FhRZdqwBNisPZy6PRQXwPBcwIlwdUx97bDbM3pheZCC4hJoo4LmPoGCRapOSU5Rs1lLZ4eBGgPPaN6C711hOi-m2kXSGSh0gI1p2JEKtXBQBRsEPEjPNCayEcfGaUQM__QxPCJYZ5qm0vqpmZtUdqAZim1E_3KUsTTA22JwPoNblvtmXb_cF9CqtEM-6aYnaXFv2ONlLxv-MFlZCBo_vMb6J365G9kynqNhjMINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لرا پرچم بالا
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82304" target="_blank">📅 17:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUldquMBf0w13wYzitcbeo14bNarKwUbRBENZUnFnkdJhVgkn-yyvnChtMT9RX4uQfclj8-Qdo4nhlrgxK5FEBpBckwlT2Puo0DLTA4nsPns8GdFDJA-YDl1LuTzSwiogsF_0qqgbnbQ-au33ymu6Wp7fXiBOOHlrqVX5gW2xH2GvuE8fXVd895S3eDmKNw4JgeNjvqDmkGkoL3A5A2cToXdaMAWpU-7ZAbi2kUAxpP1kgdkcQINZaKy1AYsemMB0eoZHa5WEQFx3DtSMzR9dBkaL9lwFW6DjD7KEpWyuJ5TtmAJYoIpPpFB9MjPd3nxyzHn1atFuf03Vjscc2P73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=a5RHEzwBZD99neHAdRjd8Xx4XmJ3IKEJ6j1sMvCgGw4FCS70pmnyJ9aq_hodSUAvpGqV_2GLgJbg4zs40wZeEPnV4SOgOHpmyoUlXgnTssw3zFevNpuYhZaq2jiTTeKkog9Fr8pKgjfTRCxVcJr8U13f-za0fEtrQyI7_V9IXq8OcbTr_teUcLLmoJQXaPTXIIOthrQnCIhWM1OI8Eg7MBMfM6QaesftvSPhO3ov92Bk5cqlDIYFUNUCEr7mRWbEERnA1I2pMllrcgW4ZYMY3QlNYsjxqS-FDz86OjI5moLAYAL0cbIo9U-4_6fimRrX8KaAMXSBchv7UfnyfnkkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f8430bb.mp4?token=a5RHEzwBZD99neHAdRjd8Xx4XmJ3IKEJ6j1sMvCgGw4FCS70pmnyJ9aq_hodSUAvpGqV_2GLgJbg4zs40wZeEPnV4SOgOHpmyoUlXgnTssw3zFevNpuYhZaq2jiTTeKkog9Fr8pKgjfTRCxVcJr8U13f-za0fEtrQyI7_V9IXq8OcbTr_teUcLLmoJQXaPTXIIOthrQnCIhWM1OI8Eg7MBMfM6QaesftvSPhO3ov92Bk5cqlDIYFUNUCEr7mRWbEERnA1I2pMllrcgW4ZYMY3QlNYsjxqS-FDz86OjI5moLAYAL0cbIo9U-4_6fimRrX8KaAMXSBchv7UfnyfnkkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صداوسیما یه برنامه جدید به اسم «با عرض معذرت» ساخته که توش ترامپ و اعضای کابینه دولتش رو مسخره میکنن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmTwv_3KWgl4jHVO8_nbnh2hdfdvpAgeCxGkcD7qc08D4yn3bwS1UOv091wuGYA0I-fl5ZeNUpfQ_AH3smLynI8QQ8AFZgmKe78eoN4sH9LgpBZ6NzOUpDsHtA39KNJKqDx1KVhzfTHRIneChYuZ2_h7hVmJbKTUcLnCNKRWKFCYvsAwl83QnddiAx75kfyRC4CHqytqqExuepPfsf_1mRo7lZ0matRi4BTgmVoxWztzssm48yPMDPg8VAc2fE7piw9wAmORQucwNxvRk1FLJ9fXfR9AtaLcCJf0YDfT8cdZbjkkyKM_QIOmMh5hEHZui1qS5y8teFXj7kyLZGH3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-M-hBo5RwdEU6Q-MAsLE2kBQx61rdNVqLGbNJtQLOYMRDA9kubVdpDlywEydM_TxyB80SXRIiZEmpdxYSgJgw0P_qrxJIn7b1D_xUscC59AVXwYVcX0-QOZu3j6Xa_9IHijgsayVVuwq9YKK1UtBmzMaq8qu5uEjsDt5-8fYtFbptRi-Dc527orF_9VWScWbhHQJ2tfTMOdu71MxC_iUJfUCSwqp8CU9dpT1LPjPlK_4XG_3agfNckdge9XxsDxp-PPjdQUlkdYdUk0fGZaIRHGbBdqb1AyEDtGQ9EnkTK1fydEQh0EFXIvJuMpD6IxKBXc2n2nxRO0j58ET5TgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svOEIPG8xshro82I9yvSfqYQTQRtOU0h-GR282RKv_Z05lVqBtc_OG018CJrOzoACO3Qz-1ZO14K7bkRv-Xp4nLysAXoPqBYpDEBuiqnT7UmeBVA-xZnrLlMopfHeilfGA220rrLpUBfX4y4EaLm1nSYk5LkyfzVJGkuSghsQEMmMZdv2AVFgW5wNW0LbJhCwfCRd4EjoqR8lk_g5b7aMiHEj1TBjaUG0ykZrwL5ZZ8u28iJQvwG2Zp3bZEcM8QeMdhBOrimAtjp55t5pjGgEZ3oUXBMyJXlwN5zrDTXFwJpAZAJCfXmgQ1ckCRPGA5sOaxguViXjIt_zylLxaiBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pePt9unrZv0gMa-uUyI0twFCyeDXO5GWNiwAfWtTh5wJz-pEwK1A1chfiLTjfoNhqIy6039fGxUViPzBPzEkUINftnTyO1Yw4SpeLndySGTF_C34YRXf_EDujlTmZBF1Y4jNP1vk_ux8mYaP94rSd6NaCJOrDFJEmOkpSRPrS5Bazsofsh3E44oQL0DzAaXkBupDSmqR4svWZy4GFor9FNuVHp4HlTdSbzAmw8_ry4cRDI9nWbq3frVeiiVynD-z8EFAb3hO9jjtor6OI1efYF2Os3RtupfgBkjLgkPWSHsFHO6P7r8nT-jsqUv7qQLBud8AQPt-0BJtoi67rhRsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewChMGtuOF9N-3qD__bXxgOeJKMRsDtcCPIMWyA7zlmj32tCrUHBUxnp7aRDsN1n8hJy70SqoLx2x27hVRHZDPO1CBUrUHHK8aeWd8UCKEbhLUZyjvxL0_dkhwhCyiEvy3E4Se3urf4QKtqkVt1gaHBzA-cNK_0ZQcs5YWwOmyJBCbfJirbDveXTXk9IkdT1UBW8cRVtM8XJ9bU-QkbmHJNElXJp-UltyQCBVqf0Wg8jayNdzZEmsBDySL6JPAgheSXYGkcjDuqEEmiDjeK-kl7er1rb7rupj8ngGxAdCMSFqu5UTXzSGhtHG911wC0DSKKgO04-WgpwLe_NzYMQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF-qluAV8jy0DK54gXW1KD8kvtGmgr6uDIokybCnm-sFouqryOl-F5gicu1zx5T_cHOCZtqJYKV7uCCgiUJBB-UpnvoZAP7bHoBAUzeJaHm1sjzOT4PXziDtAE_8P0IaQRZERF8ApJ9duULbKt9IDAoAUrvDCIDaNP3_5k5MUyyHIDA0M93Co-Dq1dv3tYjpsa1Oy8wJtymAUlTXHkbsjxOIiiEKvoPFA2dPGTWt16aPLsgCG0HOPey7S8E59cdppF8puDiBQboVMxeWyhLm38dCq2daOTOwvZ1LoHr_eXRpRGiYeJeiWymqBq_VOpdm10nWIQ9oiOsYsRenqsrGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJAwHOQWzQye0H5YHi_YoBz90AVNcsN_pK_ghj6Y_0kCsXhJMDhwB0EOonu8JO5dktvQnZB4K2tQfqqF75rX3SFntrVY1KGTPGTgWIF4a78leD5tGZV0dsEGDEbWTzW8z-GW_aDJ7QEI-sLOGJnSArHzesrtKmM2GApfEZ_pwbM3tfbwqcczCuVIMAOJuEvLn17l28oHQdFvj_UX37yWfLPscPQiNvDzX6n_gSy3xQ6CNfST1n8ubZ9tAzRAhk8sqpLiZdhRYwAKtAiJ6VGrG_F9bKqRoc1HEd5yVXKJURS-1NZxC3BJGHV2Q_-reTFkE6yGKPtsRu0V6gI3tPR0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس افزایشی بازی‌های رولت زنده
🔘
⏩
در روزهای دوشنبه تا جمعه با حداقل ۵ میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی در میزهای رولت زنده، در صورتی که در همان روز حداقل یک میلیون ریال پیش‌بینی ناموفق داشته باشید، بت‌فوروارد با توجه به تکمیل مراحل از ۱۰ تا ۲۰ درصد مبلغ پیش‌بینی ناموفق را به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/ROUL20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r26
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToJZK73h9eo9VH34CPstdycFIvsMOa6a9oT4kR_bOufaVxzd0n3xIOpaocjkUr4cAuER36AvllO3qB3bFLPdlu82n9ohlt-UKOLHckrIw8Xurx_7RACEhQsYTkhPkvfqkUgs47lE0NxUQd5bjToHvuBzGu8uAcbKKay8VQG_8XaYugRXkVFcPxPH5UcuJdvJ_1ERgOKqaBABKPlrl2_07KGD11lSiCXDlt9c81QyC00aVBkVdGFsibIRsA0xaQA6HiS0bnTZQxkBv3LWpkYeXg5FTKdZGpoRnxK5Yo27SVwrXViyBex0bW7iabux61PrgSN69goz89f991BngAdEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMk4AcwrrbCk2HVF_qzT6OPDSM--DwjDalhyPCNH-dwIjFfrrU4g9J6OJ4Ry0PJG2KGfxOURqZk6Bcxg302pjqjNon5eRz5fPkIvo0KFnpVN6qsGW7MbEcXLLWgiSu2oFn4R0nBC4sWyZyZ_26bfUYDVG9dLVeIo4NIo4KCMD99mRgSGiGa8W_XtNHRHTCe7I1qZyUXWsCE-HXPK28-YGOxjEW8mL6PCaPUG674pv1jzdiKii13sWaHqFIwWhAT0CwU_vv64LEtyim-6XEd7H1g95HdpgwKDLn9wbpA4yBXAgb78JHfYYTQBiArZqLd1Y0-dn3bX4qtK220i6qpnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZvU4oAuGaYv4s_u30AREmFgdqrJFlxy6OEJBks-VWBxY4VuoEuD9XNDUYG9iZWdh3AmW8xX6mUziDFdODZ4E8UWL-T_5zR2zAgaiE8_j6XBRelJH72te6UOZUh8L_7q0FTKnBIvieF2mboQrJDWOEaj18PgEu7NjyBbQqj5AsvX8MnOTKmCKJTUcXap2zU8mHu3Iud-e_ddpjZNIdpfuSExg7Rqgl9UT6WG8Sg_4GNq9y3rZa3XgZIXY46KCAcLxXISoUouh4tX4n1cHeegch48shxE81FPS3kjPl1nFJx9EZS2n-IZ64NVXTH3I-RyxQ8x69U2Om-dC2Nh6Gld7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVRFXinZGRWCKmNYkBOzz4qYXYQzJSkiFIXQlGAaM8FRnal5AQJJWZeHj3ArrXRNpGqbyUF5RDVEh4uyn_DP5in7sAPnBj3MUv4zdf-AxQsKXAtCC4wy2mv08SHFdEhBpKh1Qa4aL4rNqP3a-tah66mBt-_Vhma6zUkukK-3IOtQgjeAp979yuA--yGekmi3rQlPPvsL5GJRqVsp4AhbuEdGvgUMDHXCMNiE4O6oyIGsCrJxyMScabBBHcCr4UbWnZ0FHzbhpanuCRzU4Z2cw00q6VwTUXQGmlZ-ZSYo5OjoQEVKLHsmIByGii5_z-5eeDnYmtt_ClZw64biNW1vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=UQg0XQiKmi_gA4hD47_Awe7Tk1OACNI5jrc2ymBNcFooGufYwM1ufMYzI8mmCQZIbCBN456hlpVls5e6vFEa_Gf7lR2AzuXDOjzn1lKrE_Irf78YFePj5FUSfT-So36YxzOSb8stBrh6HjmzzguZfI5-bTHgZiNRVWW3Wm41QvoYUoknujEjeWJ3rvW37Wdq4vE2c_7G0cIfa9dT6r-5Wwhah4iZuQ0z-udM_wEIJUwj2jaJf6CHP7JFtXSBGhISAgA_NfSyhCakaAFHgmpurLo_rqndx-BZBJloaIr7LXncS2cZGFYcRQU6_DzmCAcWaJrYoeZPaxUfh9b-DXURq56JRxSOx2KMY6Pj4xgColSokaJgVzp8XgTyXLYGeuUIBD19VNyaxwTKiBGvNgcpl5oNcEmhvH2x0v53xNav87TApc74VpBBoOyOXEsmvT7pqKjx0zDPOaiYZM10V8cU1N_brfPlAKDcuwBBUJqvzQBVsQZDQHcmHjC4yyxf5VD_C2TcZOlV8bMSYtZ-Cb0hF3CXvoiFqeiQj_FmaDeW5bvfNBoscyTrMBmFQ3zYod8lKXHS_JV5T8wUXrvEruv_YCaW3nDuoa9DqgC8HRd83-YeXtqoK51fENlGJU7Fsbmck_aj688ZVrT-KQbH17GRmD7rkgl9w-mAb4MnvcRt9O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=UQg0XQiKmi_gA4hD47_Awe7Tk1OACNI5jrc2ymBNcFooGufYwM1ufMYzI8mmCQZIbCBN456hlpVls5e6vFEa_Gf7lR2AzuXDOjzn1lKrE_Irf78YFePj5FUSfT-So36YxzOSb8stBrh6HjmzzguZfI5-bTHgZiNRVWW3Wm41QvoYUoknujEjeWJ3rvW37Wdq4vE2c_7G0cIfa9dT6r-5Wwhah4iZuQ0z-udM_wEIJUwj2jaJf6CHP7JFtXSBGhISAgA_NfSyhCakaAFHgmpurLo_rqndx-BZBJloaIr7LXncS2cZGFYcRQU6_DzmCAcWaJrYoeZPaxUfh9b-DXURq56JRxSOx2KMY6Pj4xgColSokaJgVzp8XgTyXLYGeuUIBD19VNyaxwTKiBGvNgcpl5oNcEmhvH2x0v53xNav87TApc74VpBBoOyOXEsmvT7pqKjx0zDPOaiYZM10V8cU1N_brfPlAKDcuwBBUJqvzQBVsQZDQHcmHjC4yyxf5VD_C2TcZOlV8bMSYtZ-Cb0hF3CXvoiFqeiQj_FmaDeW5bvfNBoscyTrMBmFQ3zYod8lKXHS_JV5T8wUXrvEruv_YCaW3nDuoa9DqgC8HRd83-YeXtqoK51fENlGJU7Fsbmck_aj688ZVrT-KQbH17GRmD7rkgl9w-mAb4MnvcRt9O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am5fQvzIx3FGrDa66DozonzFNNrG9tJ5RboCCHNZYZ6MMzJ5ESPTZILbkCEzxJKu7DLTC0B_6NsPP6--u0mg10mf8pmPvPP5HS-L-YZFXb4orLAn1yD7txExxgXoQCoPh29VKII1W8VogGXswxKRXQWwNzUUog0WsoXL4Nq85Ica1q3MiT_-eb6Zb5TuKQAKdUK9Q3JxMyeiSOG2ekhyX5TywED3FLkJbEOh5HC1zR-A_u5S4nY7jJB8001sFuHDiQofbMeYVHQ9F-WNSbWhLzU7DspGdABAaDguDbo0vqO517yNpXgWmaOA9VlzkdH7rPwrTUgISXUX-47yoQu2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooOK6AV1oPeNKR2XD-5NH40UCfB0wUukXr3pqM_qazXiJfS5_Nn8tftApxZ45H_Wn4-8ol1RzIuTcyJJ9PSmCzTcTmbq6S1gKBTxchwDq93GJQu9gkOh6Zs5wrAJSkS_71JbF9flDxjbHpPeaAGwcebxgIinDL3cvWqfbHjxvEdHwNyNAL2-vQ4rh0OupVdjQ8KSDL5T8VXKP1KNt79Avl8-7Qdzc480GTqWrvHB9tae5Gp3RAT936FT6FLmooV_ehdtLkp7TUCbWUrvLMBrf5uiTfls-F05n-8OHhGqUcHMhBy9Fl6Eyd16qnxmAzmG8IYVS1xsbay7tSDtBVrdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auIZmqkPdxX184YaKK8331PGm4hFJ_9Mo68_qdgV8HkPqjWYIAxi5pIpsJ2wg5DI9rFCFZY2sT5BuUHGSl5ZeXf2sgyvOTH5NJB2zK-dmPyy4591hwGHoSzeRdFKc8oCS11T74wxisrlks-K1hgj1YIAYT5YxYtWpSChv1uBv8FjVqs6hEchMa45LlvDyQ0F2KdfGcbC2A0HCEsN2wbKE6sEo0unNo9iH59jAnLt2vOR1ZiI4pf2L7Ifi8swyBd2AEzdXrJdulDmHZ8Fjck69eL84RzfoAxVLZbe17Ipildk0vW5K3kWLpimtUopoeJO68xCqVkAKcZlJrD4RW2tOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiJ-Ua0Qym6TUw1DB24fubunbCbFOaqzRJl5Z04wWFzCM68G4YqADgAOHqRDLMf4coCVtSEpGuUWpj91JLeMgN1tcRtyA0vz65CuLZE2MDNBKiR0AQ-vGDSggNQqN1F4aXX3pqo0nP-ZXIb0F04AgH4y5COAh9DYg8Xfp7C819P2ZVWZ0Fcjh70ZTzSpNxB2LTQxFndHv44jHvreYgJdQQ8y4dxJbZAhW_v2SdUZZ57EcN-_geK8QLGblsSzbEm3-CmesPYTIic6dnw5p6ppnwcXLSO0PkCw63TIpJTF7tEdciLNeSWZ1ZB-w9CBSYtPG5zxrTolxPuqbak_csVKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFRu9snNkyhFFcj2I0WptKcKqoWQHeZL5miNHuxYdZZjxr0m_mI8EIJAWuNaRcdeRIk9RGr5fWtqIIB7kv4-PWCpZTf1uKBpC8Rg9wo00Y1XCrr0vVjPQM0yy7hOkWuDP3ek8EU_ky0RAMX1jf4yeHpq8qiw2EAansZmZcwTm2ScaJaVpNbOILENJyD-Sm4v_r3KBCURDnT00r9P6Ggcm3aH1uuNpD0lnxAYo0ieOWAwutEifJcU50pdb2_IvIb5_15jdcQ13d40jOq5eT7k7kwrGDrne9uwRkyH1rtV1ICXklW4bZXATLb57AgxPjWMV6h1pnWbnnEZ4wfejR0AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_zK6JUDR2_ZX9rOeNe2_p2Gzkdc-tiE5vCn05cBFNyPtnIiO6EUHK8G8L-RrThjFtMweNv192od4dEqMtIZ4sWv3Tw-h4OheQjiEMQEqDuonvJq_x2qAQMgih2-edDTlGVq0opV1KgxL1d_qj3eCD7zsMZ7YLYyTPL2oLKTP1ZZj5wfW94AEZQI9tBiWdHTX9TTl3GIaYnOOKHCnX2xQJvewNsC9_5vV78lBjxK1xAxdJHGZ1A8OWiFUOae8u9ECOocQp2WFq2fvveRBVQG-YB0SV4g8u0cb6lHcVVn0vSO2p2BuhF2m5gFrG15l78OJjW7B-h3tl0XMslrKz3qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxACeeNfIzR9cLx8j_4HMu5WklR550dYjLOM5xaos_R8tOTKrLomQ_9w-pZtXegOzbpvmnLCnNbLhp1kcN_7G6wfipuamk-2PLeJEUoX64_TwRNEUFlOnAY4ZQCjtRDofrTwgAMAyhYhdlUdqtY-4nr4AN_JUZqrSuqqFFpOw-MlVeiL9TF1ogSIMb-QNPhU4huY62_f0jvt3u9kjQyK5XG7_SzGJQIBvVx3du1i1OFEjmwaCYAxV3J53QsIzFNPzm8HyfWZOs7YNn4fj4LiqFB5_y-ySeHK4tY_vZa7LAY6azSzjcm0FobaIJ4g-QApF7ie-4GUem8qb0_br2synA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyRxaeqbjgtgHAQr3LApfyHPLlBw1l7MqLHH1SqtneBkIrFRjxBoCYn_oUjzBtdU6U-OUDoxCfZvF06vrK2FewumhhV2ViFhWBQw9eTC495zEU0Apr16N5BEr2r7HpvXtZHrd29tTvdF0DHgND2DYsE_WYF62ukiA7dwg6NH2uV6By_ss4jflIN_cww94laCgumuER824NR8PwnMDvc26xSQqgUr84QTFtJRz0y-cLsZxsbcf4ymNkifby-TQsC0_9Xnuzh47QQMOilHMXmu_SDf7pIEh-ixP4IyGTltK3lPoc7LUm13WetE4xGUjXIenD9ull8nbcU9FfuHkI4rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=cLig0xRUh_LrWEi5CVp4LU0wkmk0jxTg7ypClOJjoCMRHo3j6UhLlGKb_O42wImH0sXlb1QHC--ziY4hw_DR-3_v-GS8RAr8_sRkgYhZM-8I32fQrvdfaG9F806R5qJdNQTiEwHT9jh1bKoYqUa4LIF96Xw_57Dj-GNWI5cC3TqDxcdjqws69fvvLicJ3yPbHRLNmTaVUNvPBEEHc0bQFIQyjRW_C54lecxUqpI8KT96XvAZNwa5onrCO5cQsdt6mhDIO2Tp3oEciyNk0BDHxSmrgxMf6JBBkurtlHRgh_sBLn7Z4M2cLPVEFu0DnaAClUqKRn985QTZBd1U9Gz4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1569dd1b49.mp4?token=cLig0xRUh_LrWEi5CVp4LU0wkmk0jxTg7ypClOJjoCMRHo3j6UhLlGKb_O42wImH0sXlb1QHC--ziY4hw_DR-3_v-GS8RAr8_sRkgYhZM-8I32fQrvdfaG9F806R5qJdNQTiEwHT9jh1bKoYqUa4LIF96Xw_57Dj-GNWI5cC3TqDxcdjqws69fvvLicJ3yPbHRLNmTaVUNvPBEEHc0bQFIQyjRW_C54lecxUqpI8KT96XvAZNwa5onrCO5cQsdt6mhDIO2Tp3oEciyNk0BDHxSmrgxMf6JBBkurtlHRgh_sBLn7Z4M2cLPVEFu0DnaAClUqKRn985QTZBd1U9Gz4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهی دیشب با زنش رفتن کنسرت د ویکند.
یه i love you هم تو استوریش نوشته که من متوجه نشدم با د ویکنده یا با زنشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QblHvg89XkySl2JxK1lMmgjKcuJpWbRJEqXbOy1GZa9AWunFVh8eN-daqAXMP7hXdsfJpzXMhVl2yyWCeTTVvBeamYSH9_hTn0XMbzTyhGhUhj2gAdSj0zh0H286R6XIu-EfGGLkYOPxZ8Wz-GrXwuJR2PUDRFDXPBHo5qBzzAoRyy876MOa8pb6kfpNc7hnTTspE3ZBQJWrxCPaSVV2X5KRuM1DRWI9lD_cUcb7M1KVB95VpTYIgRJ7GxTg9s-XnLTdZnUKmy-DcTjkwbiCfjqqnjLAWTrACyuXl6zuZkStvnp5BWgRXhn5RtxLyjlplncIdD_dmRw57gE5X1b_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La-6pavr7qwnCVx-_byRNMadVVApxTwgZwKitdvZZj-ptkA7k7j11rv3IiLc1ArI95rcUBJN6gwy-UrHK9EW1eN4AEYfJjF113VBBlWc1ph1xX9zs85oBr7JwopC_1TEK827TKZZNxxe_3E7tw-G-6Aq18K48y2ZUMuJ_B0O6lKt4BtU3LDA_1LjcQ-xoVtLEfia1CV_WgmCXGOUdXVSP0zuDuLWoytDOrhIQb6bxpvelXKS1xwwQHL_XrM1tdnOri71pMirruYcPmJ7_RAZ9PvRPmiSzEnwk9Ga8pKxI4Yo36qWicxDfgdYvp8YnI9VJoG9nZpIfYE76DQj9mFaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2bK_6VJq4pl0HViMg9ifzgkRsoojXsybWzEfYPjy_CgAyO8Ercrq_mePGc5jMiNfwzdbQm-AI83kfgoRa_A3K9iWhDG2Cg-x_ZeXDxUFkXlPMw7Zu041HUe1miQALw4mxbOwXHxrEt9f4SNlnPYz8qiShmDzEd5Q4AlvAARUxxP2Lzh_LUw9Pyr8esb6zlEUmTb7B5609KIlHewNX7-YfPS5b5j6qX9wnBg9qhgty5sV30d4qBxB2ZMYPiQvk8ndcjKT0gWpRXuVtiSbF5olqPkb2I1AHisNR72YKUWDSl-mfmXzN8jO2TuvQaDxzIKkq8yvCYcnkATk3rcVfJE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovQI8q4qlvLdHTrjZLv5AzCNjqjtvrRwIayrRxzJuz15veAqvolTNYfGHkBT0jumCytBafBShQ2BdxwwLcUoL3VFHS6wS9goEIM_Jjo29j0NqVlTuWpEtCOSNkHV2FJNKqsaXGfKEJFfLSnP4X9w8AYSE1zaVYobXCPdp91VRw0ktqIt-26TCogvCNPmAHzXc4hYS3R6ovoeB1w25TgXsvboVd4nURukEoWSxc3yOZeotBN8tEWU2McXWYudCuyk17p12CqpyfzGDjm5wYtdtjtyQu5g9RDccgYQv2LoXo6iu8tPt7YV6hxQdsrOeggWpfi8sEmy1DJ0Og6XDbY99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFeGg68kg_ibVO2ZWrjk-swYOtJJClaThZaIL-drzNTRdJhUONbAHF2gCq6Phix-sHEoR3JZXpQ1S88wAH_fw-DQ7JrxpRi7D8yqa39iBD_MzPw1lgm78bLaPfEb2SsBGGE4ogtgZA5sFlY7s6fEeQLQcvSQ7z17TRvY3gEkY9ksR7n-eUm6gTasBy6JlUSXt8BB2oSOeOt9M2qSuPsb4i5-PGcF8rDrZUd-3VEkLzP_I_qfWgzMOPfaPe9bbkNi3rqeQykDPEF3zsHoYRgGQXjiNkkTn4b1br2ieRssRQ7AZ9M08eGvqiax0i6pFYORXAQih7zICYPlKGlsAVzkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmE2AXTyx7oM6JIquaqNh8KU7J-IMiPI3LqlYkRQYlTjY5cOCpGpt2iDmsiu5tvNTLXDtRCbrUx0sl6fU635COsKWHU-wsnnK25DzxoKSRFghYS3FfRm8hxRh-a4FhY6sToSVL2GHdG2LtvX5ZxAjwBGj_I2aVeWuAygNAojv6W3YLgxeiIfOIl-GfF9HWPloFN4MnYK21QsMOFEEOMFGg03VwM5KAFG6jXzKQBsSZjPvB_rrX8YiVHJspUpBUCYsJFYE1MjsM_IxcIqu-9iV1cLU0CS14VOnW5NI9j4RhzeON8MEMd1-22OrUlj1YPBCM3zV8zr5vPum2j1mWFwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYpa63JfVWjjMu5_AUA-GRs_uaLJSsMoHIeOX0PlIv5-CSylPfnPONRQA8uDlM1aI8O96qKy9PlOMOcnOnmh4TuiQhTc822SW4xI-gSXaLNm7IDJtah8qcglBzhl1le7Rf-M1AxFJRdE-lZC2fqBA0ZC65k8Q1CfGAF9zcASz15FikegjpnD0Wamr1RLUDX_ZXYLSl-H7V-kuVlYQGJmQckdj0N0Tzl_SBSi8ovkxhlFD8bY2XHxv7eFrUIwyAQoiYSbJNSyzKKgFjRdk7xgFOham2H24RMjvuMqnCe3rkAa7hiBmKnEeT_hMcaGVR_WOQd_jhDAe40f0MBGDMnOGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gicmrBpw7xiMVJG0l3mox0LetMw2ktgr67Rwyx9ClkcW4RKGJYBQ882AZ70dNDNqjl_OhlABmcpqxYHv3bfwcXjUGzZuHoUO9sDTPMRDXi_UEOyWhKRKNlJd6UiOSjMDqhBZti56j7KDfLH9MMRmNFXvRXvuU4nTlexNjLEA6ugRtmah-I4HrHzkpPgEMNEkE54oRLyUgAA63p5lnk_zDpwsjLCwTB8mmoGy_cm_9MQh03KCDslNud5kSgpi5x8fwXilF3QSX3SvdT6ajQlg_rHWtcPS-x9_FrOdCsBBnPwKjablaNGx0ITByZrc88EbeXuq63X9L47sVEm9FSBlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LneDQ-gZPOaQmFY7JwSGFxmbA5HmcTiFlABmPl7PKZIDG7-TW3J0lSfX1om_2ZmnoVBVzFtKT387mHxZTf1AImxAU8Ks2qIReg3046O-wSHxNf7MhE_M-m0L9h5q_5AlxxJvjQkO7LN2mItjWhlU89Y6_ryLd2ZzEGmll8ITvNxCtpzVjCYF5m3PDWmQyUCON2LZD6NtS5LS5eyKAZU6cG5fBq4PogP9dKho3KEdjyCsEojKzRgw3BlxG8-nZncgkKdjyf6xyDHEhnkMy3KXGIiUyLHTSmlUVXSECqfwJHx5oZsqwvnK8P3ZKkTY3LwrzYR2TaplzfzefJh8TC1WYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZywgVyqp3irDeujqTwrKj_tJ41jHB9vid8F4AU7RZ36j1nefGga7rtXig7JlS7iV31Pra9lbs7-vE33o-c_yyasAbx4bNgWFfhqj_mdh7SOYHDKXnqbdIkdVr4bYHFWkMWvs4crm-kCNgg0n_n3_MDp2ze7i-QozbmO8-GoFcW__pPObTXlnWmcDilC-mv8NWvvrhiC5YC6VbwlNZPXyu2uFlvA2R2F1BuecCa2WbGbdY7sGkSCZctfyZqIVP2dINW9B50xG9vDBEI3NRSzu4EIV0Xf0uityz6FAotb0ldZ8xw0mfAl7y7qvHryM1jKpN2Fe-Rtzo_j-y5FKQVCww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛
+ حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها
@TopTel</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=A5bQFNjAfhfaZL-U0Am54sPyxbM5Rp_Fv1eD39ZeR22oF-NY5X8kQ26bgFPHlVkddiJJO0ZIHNCt57nbIelHuedZfPNiWsJKOueaeaudWohY29_iM_NNMwR5vAKu-z6yYNniKY7TkECAwZhDmdbfbAYLHkGXRnhSoMvNEiX9JyKJ7f8m2T1VrQONcca0bv4xuRqLipIxx1uJmoOiaimNwWW-rk0XZ8PKBrZKNi_6HN2KbVhXM521pKzje1O_WqZj4hg7cYORQ6ZK0gab-HMGv2tANYLhEz9wrTYIbsBELjS7KIN02dBlhmWauw7KIBpMhG1bkdteS5a95dNdHU-RIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d727b7c564.mp4?token=A5bQFNjAfhfaZL-U0Am54sPyxbM5Rp_Fv1eD39ZeR22oF-NY5X8kQ26bgFPHlVkddiJJO0ZIHNCt57nbIelHuedZfPNiWsJKOueaeaudWohY29_iM_NNMwR5vAKu-z6yYNniKY7TkECAwZhDmdbfbAYLHkGXRnhSoMvNEiX9JyKJ7f8m2T1VrQONcca0bv4xuRqLipIxx1uJmoOiaimNwWW-rk0XZ8PKBrZKNi_6HN2KbVhXM521pKzje1O_WqZj4hg7cYORQ6ZK0gab-HMGv2tANYLhEz9wrTYIbsBELjS7KIN02dBlhmWauw7KIBpMhG1bkdteS5a95dNdHU-RIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش فقط یک دقیقه‌ کیر گوزیدی، چطوری تو راند اول ناک اوت شدی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbXLkjWcE0xMEecT-n43C2YgCcMl14TyrY6myFG81nV9I_C0s5dJR5qXXBsalIEu8dVbLWpQvkvQLgEJd6iXVaU0JCbS4ak4_-q9It0SnHEeNq744WgorL9mH_o_sSfE9-YfoPzWk9BpBNRWDOvH09LBHUQrgiBy7fyJrhwqw4ig-qZx27tmAxv2SOrByZ16UvUu93KHfoE-9PHYfBkEh9DwytdQDIt0duSagrVvgqYIA8K6lQyFSi0NbdQ1zD5MhBeCgY5NGrT08_1qp2UV6frU4_MEFbpKmCxNBxcTAxBE7zDCcW1WuELj7ySeKqMWYJRneRRiYGUFTCoApqHM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MerxYNaTRVLNgf550QcSJ2NdX_zfIMN88YkBDpRmGxHtB-fOWsnvAIajQbZx87UudX15CJD1ISGMlXTXzYNXkdJ7ZvGZ6VNlOVzk-RybX7d2Pp4VWsUImgLcNErWZKrP_cAiTbHSIio54ZnGlmziAN9cKMJ4LAekCFnrVVbMyv3DYUONLmO2--NuHGyyuxVx4t3OEgKARiTjbpIAsVchA51FHoY-mpiYigHz9DdSfYYVJn9icxkyVmT5Yju4vpi39G3Cs7MXjsU1g6CwojJuLyT7Pv20mXNObVjaW7M-VvF3OBhVtMmlAB4U336sYaZpFzlwJ4ylBG12PzzX5m1yRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfKiCF1QsJ2LO8d0oRG5oAV2N1ZkBMcid45joyp22Fzj_k9o-ir9IQIjS4coB2VEnixZS7dc61EPT4jijcH7DiRywC63LPGP6RZd-Q-E7KGHQVFbMokCQ3P4m38tTFPHnCwCAkZ62RwRya3tguc0h_v2veQzbwz4TF1kgrKVw8gBPUHGPYTc97ICLXmxXpjvoMysiEHxkGgHYLQ6HPFl6Rowx6s49kdZuZlHIuyNB7kNAKZ1p_U04ueAPxIKkHd6oX7UAdQssIH-XTpJ3hHlIprnAjh7UBrMnmq7jiB9PvmMwGFr6RniietydIVAIsUH9R2yqI1E0AtwZi9OhgPdIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWIIytmJEmQMRQD29YaW5sazKCN0mJosKDp3NYNxosiYhu9ydpcckCXh644TrvatWsX9A2B0WuffHx-vCnwCW35ixTGzeaENuP9oLWuEGI-IZzofWFXrdtRezhS5wtNJwUzVTSivspf5x1Unu0EaoObcRvVur9JjAxKbN3VO3r9v4nQZXwWBL-6LODghYxw2uzkHFTNqdGRDlMQUHtSGKyKCPun0Q_M8aQSD9PQTcz0sxfTIxBDrwdTcfHJ4YhEFyrGV3RazVC0onSo_-bHbJRqYrHyxeqSiY1tLL6Jnj-hXBFyBCKWZzPxhzhW6onWUks72hTpjYeKhg86Ft03AHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRTrkmEO1myWBcF1-WfJlX4jp5nURUPOnJ8X9CPic7lS2Pp1uO77qGE_3B6ECapMjNxcXGNHFczzbOdCLaw_7ts2qopcBUtDjwmz3aFFS7c7nyPZE74pDOsbu-AjhjjzqAp7sIrUk_WZ31hupflogUlSQFw0lPnJ_hx7N_iLIPzPQKhzKos-tdQPZu6LXC4zGHyxzdWknt1q3SgBqVu3sXMvtoS3lwsA9yiyHFSPLD0dl2f3sZZh7Jf-bxl938hQ9DLhtVIuCeZtfGG44Vq3B6k4flvDVhHlEeTORytmKIX_lzgP5pzIEA0uTu0J1aYaySUc8jl6NScX092rl-XWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHaVOCuTBEBdYK-xH_tW9c4Ju0h_yKSVIMTMdAqAG8dA5HQlQGc-kzonzpk1o9ErK3kMDrhYCIRzlCDXms_rc2AGeT5ybFBI8wu1pEGCtCIhbdppJ1YwMyU3VQT9F6aKrWIUNZZfARBg1D1Dv3LRMrfx-3qZ8DzhiwavUCk5-FPx8jI_b9C-xoPKFdE_wap3mru7XbMyTF3CnPVpVif2JcTFfZcOzvhfHMbIR25XC-3tvPSqvpaAIEuhAlg-8t5O5zk1DpQnE0YueS07_ZXZPSUt353S8OMI-mx2ps0PYCYXiQrAN2y5qsXw0xEAsZF6hAbMgBPcNc_uKm3i5zaqOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUuuA-AvI53TLvahSLzjnJrXWXD3IJZjlLr0Js_b5whzWd_1e3bNnRg9mRT3Od6pfqcXYZm-LnU4A6M4FySW_qmFHyq_06E_mCjvCKUEztsyG48XKK6UIjERhkFo-6bslo4kNri-2rqSfQ8DRSwGxQxP5ZJPeth1_-1aKmSRe3VNWVmXDaRpSuq21c5beVSDFv-MTNt1qmDpxDc6WTI1aMsj2IvXj7UUZyTraDMnLT0iV2Td_Hwaj0XzFPRnSKMJmIH2-iIqwg-kBsAZAoMFyv0NYwD08NGSqUddDdAAV37nejhJTVubKBsxwzJKmJvoP_Y6rTZ_QjO2wKdln8cxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=RSRpC1O6Iia-rJCZEilk7D2XKeaNyH-lsAXvbNB2B6mKnwf_YhVnWH6hLe95J5dBQpcxKixh6rHbvGfVGZVBmmcQB6O5RSOkPah3iyghjc0l5eTPVu5c7CU3k_fNJgkEuwGwLHRxs5CPVawnLmFLM9W8GEDIZ3l9CRybnCAWjI0DoyLXMf7vduH3ZurxOV_-OwMLJN8FljO_p8O5vNkpLpXjG_mL2EXIz-fHXGDlPLcyXuPTWinSVnUqsfrxjMzJdcMghssJeVoGC7B-uHD-7U7WkZTGb_rPDhaavKszB_FTETMore-bJHRQSDc3yb9H4dkail7eOJZ789LVJff7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d93334e9d.mp4?token=RSRpC1O6Iia-rJCZEilk7D2XKeaNyH-lsAXvbNB2B6mKnwf_YhVnWH6hLe95J5dBQpcxKixh6rHbvGfVGZVBmmcQB6O5RSOkPah3iyghjc0l5eTPVu5c7CU3k_fNJgkEuwGwLHRxs5CPVawnLmFLM9W8GEDIZ3l9CRybnCAWjI0DoyLXMf7vduH3ZurxOV_-OwMLJN8FljO_p8O5vNkpLpXjG_mL2EXIz-fHXGDlPLcyXuPTWinSVnUqsfrxjMzJdcMghssJeVoGC7B-uHD-7U7WkZTGb_rPDhaavKszB_FTETMore-bJHRQSDc3yb9H4dkail7eOJZ789LVJff7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم دیشب یکی از هوادارای استقلال داشت مصاحبه می‌کرد که یهو رفیقش جلو دوربین انگشتش کرد
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upNVQ9_bLquTkotJzR9uoCs2YPtxRYxMAw7T3Cbq_FAWubqND33AbNZi64-sGjedai-J1hF4LS5oV9wa63qm7Esgy2Rf7FcdqnSEomEYM23Xwshp72k9F521RpR93bX2OFg6Nxkeui4GeK47SPmNNmNVMyq854bzcNIaBpcip8uLKCSehsBslRZ8LjdlzRgAtJcyneciLxpkd1mYIzl-hDF72ko9ZddbTx5LlxObW6IFbNEiWbr084HYX0SFgrVfj0nSZcHsqvIdjaOWJNK0dSJC4IqgPoqStBD1eFEDqbF_9TMT8vhv9TCCvRtcAmaEUq37U0UMMWlQLBGQPIhggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=YucZ3u7EZ5tpR4e-N4KohrTSlJG-cA8y-pier7JhprMs0jjQvhR0tIS7iqID1ObbO-odBHl7Lr_5RyGzt3-WQbnyUg_WXmaBSwydlNdL-lU58-UVWothBohneR_dVz0N4v0sBJ5l7A2sdwfbggpEOu9znRjGEKLaeWHe9Wspg_0qgAVWDLhoCZovl5CVzM4JmG6_7ZUKQwlkY0Gjuq0IZarBGS0uLWrinmHjqogJvgghvLzIZyT-c5DzVyv0tAMRZhG3RMQVcr3evQ_lSini9CQxrAADwY1NOD1tJfkuo5ct3FVhm69E8yCgo5OTJCgaiSTrYLEW2yJ_zl0Wl4eL54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=YucZ3u7EZ5tpR4e-N4KohrTSlJG-cA8y-pier7JhprMs0jjQvhR0tIS7iqID1ObbO-odBHl7Lr_5RyGzt3-WQbnyUg_WXmaBSwydlNdL-lU58-UVWothBohneR_dVz0N4v0sBJ5l7A2sdwfbggpEOu9znRjGEKLaeWHe9Wspg_0qgAVWDLhoCZovl5CVzM4JmG6_7ZUKQwlkY0Gjuq0IZarBGS0uLWrinmHjqogJvgghvLzIZyT-c5DzVyv0tAMRZhG3RMQVcr3evQ_lSini9CQxrAADwY1NOD1tJfkuo5ct3FVhm69E8yCgo5OTJCgaiSTrYLEW2yJ_zl0Wl4eL54WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴
: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=c3mevA_G_PbfBAdfsXQLj2AmhI7Erh7OFBii9Gz54rXFyrkDbrxwr4Fq7WhLbBr9c8gdtOIrQQqrJFPDNDZXvMR-cOsofb1kScJuwOi0TXfMaIKWBPGHUM0kfwh3QSlet22RXbw_q_t_a29rTYG7XRumv9DradCsApdji1rwOmHCkMaTbqHy97ixA9uwJKMEDJlx9TWRYtbYFHc_g9zk7iIzH-kczz49k7msO3H6SDMXN6s7YzsrXpnaP0HwJLAqdapc8U56HYczXMn8IGOKCK7BBx1gCg8IRF-TcvBsmZf56QWQV79CsDNwp0rZm7s8KXf4iWcTKsodar47FzCkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aaa49746.mp4?token=c3mevA_G_PbfBAdfsXQLj2AmhI7Erh7OFBii9Gz54rXFyrkDbrxwr4Fq7WhLbBr9c8gdtOIrQQqrJFPDNDZXvMR-cOsofb1kScJuwOi0TXfMaIKWBPGHUM0kfwh3QSlet22RXbw_q_t_a29rTYG7XRumv9DradCsApdji1rwOmHCkMaTbqHy97ixA9uwJKMEDJlx9TWRYtbYFHc_g9zk7iIzH-kczz49k7msO3H6SDMXN6s7YzsrXpnaP0HwJLAqdapc8U56HYczXMn8IGOKCK7BBx1gCg8IRF-TcvBsmZf56QWQV79CsDNwp0rZm7s8KXf4iWcTKsodar47FzCkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مامان ددان تو اینستا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=Nz58TvuUvWDaWXSCq4IUzdNc784QdKdnERsOBNKkQW1O3aWgp_Dsa_nFlR7R64c-GHVlW5B-XD6lSiNT3Ary60uyW4NlmUCvqufJ0lgDrg0FlMn9YYZ1FLxv6zpclBJcAxD-_iw-u2NJYuwknXgxGL_MANc1NxU6gG6ADQwa0RIYp9lxvjc3UkX9Ci7MgXvXRsj7wClrhTlf-PfeByifs0ikgWU0R6FyxwqUhi7OL0R9FmC_dNZc_nz67Go6Ag7SOw40QbjG3DEMt6-FeWqrNyA0g6NBv9Tj-E5f0vBGW11ucweSMpZi1BM3bTncpYZQ3YcMvZChZROaACkbhweudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a989fde7d.mp4?token=Nz58TvuUvWDaWXSCq4IUzdNc784QdKdnERsOBNKkQW1O3aWgp_Dsa_nFlR7R64c-GHVlW5B-XD6lSiNT3Ary60uyW4NlmUCvqufJ0lgDrg0FlMn9YYZ1FLxv6zpclBJcAxD-_iw-u2NJYuwknXgxGL_MANc1NxU6gG6ADQwa0RIYp9lxvjc3UkX9Ci7MgXvXRsj7wClrhTlf-PfeByifs0ikgWU0R6FyxwqUhi7OL0R9FmC_dNZc_nz67Go6Ag7SOw40QbjG3DEMt6-FeWqrNyA0g6NBv9Tj-E5f0vBGW11ucweSMpZi1BM3bTncpYZQ3YcMvZChZROaACkbhweudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فیلم Avengers: DoomsDay منتشر شد
۴ ماه مونده تا انتشار خود فیلم، این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbzpVsTTPECEuJ8t2Hw22bMOH7rTZjkJoR-1ZC4GCTTJ8IBIDa1Dh_ZOBGRQo7bXJDOcnE1Ks4dsJYG6JXB-_N_8wi7AgQfcZ49ign2e6aSqBBcfp2jd_dn8G7RkAjwJgR2HrYxqTt5jTYqqg1WJDxWBgI9mbKdS6UgkRl_6MmoImBvwy0JaZdZLjzb7DVZgwFK-M-Hku1YwlqlmvHvbfdoRnxx_OHrbgamS8POYfpfwiJtXMcokhdkVJ4ecxWkH09nVc4Po5ahvOeMFtSQmO0QxBT3W7uExYPTUdPbVRBXNyyfMuk9-rcW-cEANRTKm5Jf-5_LoY14qi4ijtWtx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfRT-67XCSJtiWBReCyvTBm7jD6SGgFEFNWCgHNVBqhfX05Cx_xCvNUEr0StFjayH2xeigGyf0oKDcXcikpjY5ts5gt8GVOiDlXvP9tZ3CtnVoDVmfE8KblNr-g54aiGDBFS1-Qi_y4v7MOSP0lOefg57PsptT_tEcJqEjSVc9pcJ1nlckz-X8sTc28uLbJp-W4Q5MbVEGyDiu2iQccFiVS2cc2vKdKo88uXP2PxP6GXoTbtlXJdZ4tDs0JPaCksIotPQQ73uCD_Uf3Xt37rY5s_yvzLYfMeKEw-tM6lZOx9adnof9eL1JlNlOGzRYqRTQIZ3cc41EWtNA3whGM3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tp5a7epvyVjdNIp06TYf9RhrrjtufROXAfSFHwxLMuQKanfyVRaF4gGgfoRcPXYy6km41df9pv7DOA_CYAm3-AsIQABl2s85X9NG5V4YgBKFsODKoEndgNAkFnbnolCpMBsKVcWKknNPUYMlqMW4RRcZV47A-SCARkAVc2snprthjaVetOvHNA0ywoman4BMCtSwLog7uKgx3j0cmkxObRbEw4g8NtAU87kpr9Fxw7-IhB1sqj3wPZ7anYnDmZYtIh1G4BBoy8yX2qKQAgx8g7RJ3b9sMmcGvlnFRSTvRyrf_kXzjPr78VlRKlueZlPALkV8DyJXzZlm1VxIiqNZVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abcufazydUWl4srYVs9Oim3Yi_YHDbeSkFjgdHKS_7D_QTAuJItT5Ehvk5-JUlWLxW8H2abYOqEesGiUsHAZMSWOhdRVph9lld-wqyPZ5snweopdHFdbJYQcGGCXIRRdDPhRkjm4WbaDY6ohmESquxWLPrBuixX8A62vD65ZIeKok37FphSvsqNhpZB8VILsVRMShf1zjwVfpOJchfY9OYhgf6oho1gV0-Lz5VhWvENx6udVbtLvnoFpNso8WtnqqFd-9VBKEwuKGgzpScuW3yqlmaJg_6fXkdxwtc7AkGnj3HSgR-G9EOHk1UxpYOilmk2bHAckWOrpBZnqaer2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiiUoaPm4Bfq6dTooG9yM3hw-pvVIWBFmm4etUuu02uhHg1koReK0DuQXhGPntSNKhMaDGw_G-Y-PDWx7pBGA67QMpzIn5sPhBFrx96BhEbtFqo-qDR457zOi3CefHU_RUAk7UDTbviOP5i8cgMu6By5EostZTxpXth4v3o3q-dty2CqQe1Mt_J1MZ8iWz_OvudLaCN0cAXC40yK_vpTrff6ITcK0W2eiEG60DdgOBt_66pthbraeTJkXr08JSLyAVszUmwV0QnnvPDVtHdQuHzu7bmIxL1Jho1P9vm0t0Vngrlvc-Ydz5Kmy9EYOGhVoAc8Gc6Ww23VsfVFolHXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1OUf_S_EVbTv-Cq2QreNMzwSsIxOB2k-8MUSl4y9wnvxeCPMVcMpBP3woZgBcdCfmxiI8U93ncGDWamrVdGt9pKy8ZLTMRT0zgMrkBcm7pb-HjwU9k1lfE7DMu-7WS4huxPfsKfWC-04loyOQ52Ws0XRbecA1-RJViZqdbS362b4K0rWkD44YUTxNLHXlVWO77wPdMGuzxXpfb8egVMAD029VEEo5NruR2dDqBu2IhXOpIEsGMW-fE80rZx1cm7njdSz79USRs7AOsevBzen1jvYKsgWR26qyLvcGqCf0MsHFAGL7PimeznUCPhs9CvDv087LRPRcKwqO9f4YqeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3EdBrUtVEuc08UVuxW4zNPsC02cFCeN3UB8oeptgiw43yvtFtJYtXucLIGhnVq7SZpgJlx1Ztc-cMAfPnYN7e8NiFS2pF11sn2B9uU1IKq_8jJZ_DDPyEPQdeUIhSnfX-SXXQM8sgGpLGHsNOJcOPM3cUefjl4Pw7xkxDlWtdCZYbE5vMPndQ9mNWEvHvgZ9flflm0MJk5iWxPwpGMipWvmTu4yw4LuRNYnZ83YwV1XBtvWj5J_NzQfyEug1w2-v5J8lqPaRNDAPdSJqQP27k-Co6KQoq_8sC5GENhxxdanXHEKJEbPAvD_vHnqoiaOppNfUw9Ou9vsZCMwi2uzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=UDmSdrmqoPJ0ylT-8P5eP6_sQdoAYjRj1A9d4wG88AxilcBpLZLXbziwxdRxPsRwoiFqmylrMkPAG7BL2lZq3vGPj0lf7qbp3ZwMHisUtaCht1LDc8hQXHqnyhFVvEC6pwz5Oe6y0tCpcR2d4YM0gP4jD_3q0Ve5GJhmFeY_H28WGKE8mXMigG7OxEPBwUxZzYlGozWrbCVa1smrQfPPY4h2talvgeTdt29Ry0JOYF1DzWyitveyM-Vuco_tBGfu982qV40ndlpdyty_EbkqarfknzlZ0QpcIBIj0SJ3s064yr0Cwp5xuEmLmo5Ip8Nm0b8ONEsGfPGSHhGYQJkftVInnX3gz8qyEixPPYJqpwkGfk9qW3J1hbCBi0LdkrwUIUzsV0BT0pDMYiKeSscEpxCIJWhF6BY8TIF6n95F9eeI2Rx1FlolIk8YZn6kH0vTk6WVta244taVlkkxl0NRaay410h_tuLCG8uBaysVdrsG0KMzoMP7hra2hP4-JiZVwsggtYWOvIcBZzAa_XBpbpcz1CdRDWon9_feqTtVhUO94V71Hh_mC5z0QfjpoILtLsTk-FkFLWiAVvTLnotk0-eMhlFteq_Ge07hFuZ0qKoixyCSRii8RWkIq4ftXjbrNdh8ssiIKG0mN0ld_EwCuWtTAwFpmFT4chytcpD0wjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/407c0f01c8.mkv?token=UDmSdrmqoPJ0ylT-8P5eP6_sQdoAYjRj1A9d4wG88AxilcBpLZLXbziwxdRxPsRwoiFqmylrMkPAG7BL2lZq3vGPj0lf7qbp3ZwMHisUtaCht1LDc8hQXHqnyhFVvEC6pwz5Oe6y0tCpcR2d4YM0gP4jD_3q0Ve5GJhmFeY_H28WGKE8mXMigG7OxEPBwUxZzYlGozWrbCVa1smrQfPPY4h2talvgeTdt29Ry0JOYF1DzWyitveyM-Vuco_tBGfu982qV40ndlpdyty_EbkqarfknzlZ0QpcIBIj0SJ3s064yr0Cwp5xuEmLmo5Ip8Nm0b8ONEsGfPGSHhGYQJkftVInnX3gz8qyEixPPYJqpwkGfk9qW3J1hbCBi0LdkrwUIUzsV0BT0pDMYiKeSscEpxCIJWhF6BY8TIF6n95F9eeI2Rx1FlolIk8YZn6kH0vTk6WVta244taVlkkxl0NRaay410h_tuLCG8uBaysVdrsG0KMzoMP7hra2hP4-JiZVwsggtYWOvIcBZzAa_XBpbpcz1CdRDWon9_feqTtVhUO94V71Hh_mC5z0QfjpoILtLsTk-FkFLWiAVvTLnotk0-eMhlFteq_Ge07hFuZ0qKoixyCSRii8RWkIq4ftXjbrNdh8ssiIKG0mN0ld_EwCuWtTAwFpmFT4chytcpD0wjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر فصل دوم سریال Mobland که ۲۷ شهریور منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82209" target="_blank">📅 22:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNCa3Wj6e2Jj4aXBsS1ayArRbpdZUiS87VNyeyehYqIP90OAkqvoULCvj1uD_C6KKoJSUGjx2E88W6aodioctqSEvONpii_pNKH3UYeBQWmhPgghTHckepu52l52BD1xunbOAZlzwYarM6y0H_y50gCtSRBf-ZIFXxxLK1eYieRmOA0BFy7yBh5WpihCH8y9FSj3zNOquZGv3UmtEhw9BaeLPVVWCtFupOPgS8YFkyasYDUdvlfjLJiOKmNicF6v2Wc1MlDGmxR6qtv4hohG8khcBHl-zLwKqH-l0BYvcx1mOLBlyGHTQK6nEY647QKiU42JbSv1etszhCGSYN8ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAwOCqm14MZdxS4boLiFYWfdgAYPWgjA9tqkbNjSOmu80HrP53EUpxUSCR4wOpAv_tXNNLZQJgFKvTTMWxZTZ0KDL5LKojj6QRM4j024FnzjmDrQC-5T3aXUKDKjvK07-TTtNtGSolmioN0X7xlEtjg3RiIyp894d80oGZoLvD4B77BsLEvaX012tuI5T-GuUiQUGNZaXD3RfZhjBi9XzP5OMBjoVkJgIFOHmxnBPXIKU-reI915IaMhGqJuIabnhS8HCxvrACU3hmMkoFRtxfnpSzuM3tpO15j-Vm28f-tb2qxYZZhFiVvx_iE5INZ7tAT1TGotL95ZMxuBNf2wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnRPvGsx64POBn11VUBsOJEnfqgxbYsykDMqzhE722w_IXDbFsO18HOQm92avdDEMM9Ss0XDbCTM1_C9w0B0QVWtX41Hr2pvlU15upM0qfg-WLUt-2RZWp8odK-VmZ58PWSnp-digEW5oP3Qlp6aREOT1by2qnM60qDAxG4E2-zzdfiNLrJMltR_OYBYBzKUFbd0LoyF7jkVvVaNt8bCw-sszpbC1HNj6wwFW1zFeYPytvnILkbGjQFVJ8saRymG2PdQYQXPtw7yoGufCADrh5TvlTEQ1F9udbFAfWivE70xawp16cF0F2uTQT-5y5wo6Ipm3hvSQ2MTbN5_7BVzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekWKXkhtGPgXHAACL1FbpmfywAq-2apJ9qr3HAW6VRAWIP5SfUsgjhpX41BvYLQ40YUMfmi-RiCZWtNpoxDXQm0Q0jdBxrt8qngfe3lcB2_KZdXGWiqxqvYMeATYXOLqIh7X5bHqcOOH7DIFsU4Lfmd7Kd_eF2Hjv94qzYsyKii_U-OBsqgkqJBFaOmQszHf16p-EMFhcw9FWr_VN7Y8MWSF_yoUW_jT57XzbKeQpgsc676WRSp0lrBLkHJug4BMwtc_dTr70xlGnzzCuHcBjAI-fRLcneJLx-RmZDe0-qnEiGoeDWYdJlQU1D4Gy7DPSt-SE1V0C0wMEdiSEdwVSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuyXLvkEtYAKUCzg3LFxSZN17nJX3szcEi7kk0M331HJJALXPyL_KvRvh7baVFSHdBBi0CiPjCHi6xKuQAJOIOR9_DAiwSZW5u143g2wr0tqQ_pWn8LMFXW_5XYVOGzKDuh6MieW4u3U7MHw2i27eJFfYQoUFu-f9zzwd84u3dGBihmeehaTwcQrSyWzUcMjEww8en-F9xBqdVy0AjpXndHenCCNlHq0Tt1Z3itouaIWaWHpb6SDfNyGCkaVcgXP_FpmWyOG3RwHGLFIs1FxJoSDzXlZ6Snk0qy1BJQ1PonhGVwXuMtK_Vjy3lIM5Ne-4d26fdd2xL7oXqTzF_vLzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ0RPwh4LRlHnu0GZAbNd_kClHCQJWtoZbUMVPT2zJL0_Sr5JDaEVxkGz4dHdKpVumSTngCmyTE0oAiwnJYY3I9X8FkAqNHEzrpbaMrjpfHCzbFlAByYeUC-IlP1KuFmbecQ9etJ3b4POMUvsPL-003S7DAdKYaCz1aKfrMNZX1-MCqtRUcM-TuVXm3lLgiX0UQKURWnkw7uQxOYz4a2OaaZ2dPRydKqmpPiqpHvLtxALqUgmKrIQpeQoRUvMWwkSYzjC62pdrufhiCPA06nwunhsHpLsE7JjAlwTVoM_lfMar9N_IargADDT8anc5XHuHW6wnCH1eqNspAhfn3JUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/og0b-Ae-bcRxaXlCkJ68s8uq3dgZ598ijGDIMf5tJzesXDZyyONzRoPVAf7JX3LC9m0qkhjR7UdRIIadWyP3RlgQ_1XWCa3PAPOdenU9fsalnT-YDjPQoyuZr1327F7hMkawRNuHnX2GVFb1i_9q1q1ByrMMnXRSmg0hcqwBYqchD5YdfRDNfxdJhjzLdc6WvxmIDMjueKWSVAMztHu_OdP5gZBagVMwLthGPeuypwKyYGoqyQb6_OUeSqM8qlwsraa_fABzjK45Gik1YuBCmVpU-Zze4QK_LdDJpGIvjFNyfPj7dK_uy-lZ4QPUzbSuDgCcTGrRMk1MiMXy9t6-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=JTdg7m_B-wX0IXqP0Jq-nIzZjGXvIBnAuzBY-hLbd_bQff5VfW44126mkSts_2wtQLlBw7mo2Gf1KMVAgpzQBbgC-r5ujmEVku3qid3sOOs2IJFyid5Ew2RwgOpAnLPPtmMvQcXxG2Yz4mnXT64fGg5vpt6IUIK89GN4gpVkTZGb7dtNaVfon-ew3lMj6AVnHKXXjHlTy92sgdhBtsJgg5hzjhRqgF7PWM9JvB5MdU-Fo4HcsdnaA7Tpxom5VI0lrYulLGuP8fk0CRevakK5AIrxwa5RdYypbNWmXTnG420_b7SBnqBIlmwTb7aJNVJIGql5_D2uVrbb5eIzCysrsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=JTdg7m_B-wX0IXqP0Jq-nIzZjGXvIBnAuzBY-hLbd_bQff5VfW44126mkSts_2wtQLlBw7mo2Gf1KMVAgpzQBbgC-r5ujmEVku3qid3sOOs2IJFyid5Ew2RwgOpAnLPPtmMvQcXxG2Yz4mnXT64fGg5vpt6IUIK89GN4gpVkTZGb7dtNaVfon-ew3lMj6AVnHKXXjHlTy92sgdhBtsJgg5hzjhRqgF7PWM9JvB5MdU-Fo4HcsdnaA7Tpxom5VI0lrYulLGuP8fk0CRevakK5AIrxwa5RdYypbNWmXTnG420_b7SBnqBIlmwTb7aJNVJIGql5_D2uVrbb5eIzCysrsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp2wsEyXcBgbX6JPeI16xkitUgJSr8AerxHO_6z_ltrd27-oZLSX3Fg1K-FqGypc0yNI9f5DTYZFbdrD_c1vn-3k3ornmMAzhHQgLLyO4LDGOcrk_JEnGyYGqzrgDpETV3p1OwdsTUrb9njPODh3bhVVB0oibI7zvygWsFnYzRsVyVB0QvujKVs-SvNuUJ9zG2mZD14sa82nWgHwOOa3q6NDcGjZ8mDRX7CpsHfJbMJXlfTELmMKJWRdkuLkLMMio7p0VQub1KXIaA5ClbkdwwGiJPVEtXJJHBmuN5M2eHL61lT_FCT_dAIt3mHXhw9fn0pQ_Dr9cvyoGYPF0j060Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i70hiIVB0Lys2hXI8bmgavfKuuumW69JMOil03dPC_ssWEUNtWtw1undHK4qUjjWJQh9vh3bHUQgxJAV__OV1zgx9q-6b5i-mhHJm72M7uthMQDCa0CEGOBvC4QEKv24maWdNCVRxbSwRKLRa8h6lVjagh-AXlKYB8K8JgOLe0ib95pNTDJMC4zcKz7UxLGD1SwmeA4StujL9FA8yFvEVa6gxlpxMA3rjbsLbmejCN8TvmrrsgJPPOWr45ilvTWfhwoMqw1vNHfsegxhZUJp3AjBwnTGpi7WEHefXco1pbRTpQgStTidZe1zCFcBodwTbA2qBM-MWjrMD5UPxUwTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoJ9QjzoHfYGA4GfDDvIjVMno1gh9y3UXHtNhSD5EzA0xzENZ5jlyLgiIKX1E_J3puOXaY88Ka7su2aVoxD423hHUgxciEKeQ8WrZQFadxNz0JiP6ClkqL6ljLeBWiNs_IUqNMS-VqI_LeoQh5DIs4JMiL0VltfNzkDdSuH7JdPV355Kan3VVBoI4Z7EcPkRzW3QIxPeOb-tKSSQygsn0lbCzV_dbGws7VboWvrCrkUmc6Npe9Dd4WhuQCwo7-RJ05b_SCyaGz-7re3l8tQH_M7TpF0sjDLKwZDZTEMPQY540L5TNvgXv6_gHx5CdumqQYuYpEv79Hz0b0HpTjmodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQuu-BeEGZ9w5mKMxISeHvC7kdaeUcadQZsxiFKnpxdkHpLm3G2It9jM4otQ25jkeOYJuEfiO7mAoTOIdWMS4IrnvE7W3jah8ZkN2yBMc8O2gQGuQ1lWitvmvbbv9hbI1FnA4HuLlE6yWX0Z6JufE-dCj6sEPHBGpvSP3g8d4NtPEeTc1iZbkZ4YkFULwmTpXEJLie0Mi4a5IimBMnqyH21sqiUT_-yOUV4YS1KNIHwywy-HGn5h8h5Ohuz9FgcHF6DhO2RY5b9C6bAfC2ua8KluiVYc498vWjPFkdcUji6pE8cnK4xRXgYb2EbEdVvYIQYokxYYKdPrsBU5F5jLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvOfc8PEuH782Pe74V9C_FROnXN73UmSegk4dxt8aRnzS8zRP1AZEh8M8U3BTDUHqpWMdc6rlchuBVfQrwBbSusfXYLu82gdJM2_NJ7ngaRbYZ6CNhadQ_5IZUSiRobj6qclaVF8mKwixXqFLGuEgQe5YjDPoLG1B_9mZsvktpdN_VLPdouATlsyWfw1KiYfhR89siUb0Z-6r50MOebvCKMjnNIHo_W8pTD_MWJQKS8ndOJ2D57u56DD6EngN1vzpxBdgNkzpNSeAf-fjacS-Kf8YvH-oBePSWKIv9WQfXZNqGwRo7gxrJS4wtAJrWvb01UekfjLrd1XNt9y-8sfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYT8f3jo2tytnRbipzwdRH5-Oyk5fMs6gGbkqCGXrBz5G3nSFB4n6iOcw5i1am2qB0P8aH8CD-rmwFTk9zdV-ESS16pVT79Xwtcq_f5PrGw2quAVoYxwNJciqHcKHRL4nmuuaRU5it1nJ3fW6Aqq3i1yYuTEqhawsxmRkgKAOuFODm6Bp9PMwd9mpFclhpn5Tttq0VYtxaYvgfJ-990XXKwMYgKD3xuHxdleFIYVYDoZa4tQbqvUz2Vt9P2ydgY_rRQVuHwNr0umkBjJqh-LIBn78Ro3Kv64to_4Hn7iCiswOWwxnc3a6rxPh8KVEKOo1AtdoDMZkgsFGwfN1fWXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
