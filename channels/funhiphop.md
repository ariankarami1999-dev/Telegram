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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 17:28:38</div>
<hr>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUldquMBf0w13wYzitcbeo14bNarKwUbRBENZUnFnkdJhVgkn-yyvnChtMT9RX4uQfclj8-Qdo4nhlrgxK5FEBpBckwlT2Puo0DLTA4nsPns8GdFDJA-YDl1LuTzSwiogsF_0qqgbnbQ-au33ymu6Wp7fXiBOOHlrqVX5gW2xH2GvuE8fXVd895S3eDmKNw4JgeNjvqDmkGkoL3A5A2cToXdaMAWpU-7ZAbi2kUAxpP1kgdkcQINZaKy1AYsemMB0eoZHa5WEQFx3DtSMzR9dBkaL9lwFW6DjD7KEpWyuJ5TtmAJYoIpPpFB9MjPd3nxyzHn1atFuf03Vjscc2P73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت تجهیزات و پوتین کماندو هایی که قراره جلوی مجهزترین و قویترین ارتش دنیا رو بگیرن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/82303" target="_blank">📅 16:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/82301" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/82300" target="_blank">📅 16:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شایع این پست نوید محمدزاده رو لایک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/funhiphop/82299" target="_blank">📅 15:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-M-hBo5RwdEU6Q-MAsLE2kBQx61rdNVqLGbNJtQLOYMRDA9kubVdpDlywEydM_TxyB80SXRIiZEmpdxYSgJgw0P_qrxJIn7b1D_xUscC59AVXwYVcX0-QOZu3j6Xa_9IHijgsayVVuwq9YKK1UtBmzMaq8qu5uEjsDt5-8fYtFbptRi-Dc527orF_9VWScWbhHQJ2tfTMOdu71MxC_iUJfUCSwqp8CU9dpT1LPjPlK_4XG_3agfNckdge9XxsDxp-PPjdQUlkdYdUk0fGZaIRHGbBdqb1AyEDtGQ9EnkTK1fydEQh0EFXIvJuMpD6IxKBXc2n2nxRO0j58ET5TgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/82298" target="_blank">📅 15:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/82297" target="_blank">📅 14:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svOEIPG8xshro82I9yvSfqYQTQRtOU0h-GR282RKv_Z05lVqBtc_OG018CJrOzoACO3Qz-1ZO14K7bkRv-Xp4nLysAXoPqBYpDEBuiqnT7UmeBVA-xZnrLlMopfHeilfGA220rrLpUBfX4y4EaLm1nSYk5LkyfzVJGkuSghsQEMmMZdv2AVFgW5wNW0LbJhCwfCRd4EjoqR8lk_g5b7aMiHEj1TBjaUG0ykZrwL5ZZ8u28iJQvwG2Zp3bZEcM8QeMdhBOrimAtjp55t5pjGgEZ3oUXBMyJXlwN5zrDTXFwJpAZAJCfXmgQ1ckCRPGA5sOaxguViXjIt_zylLxaiBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری الیگودرز لرستان، کف رودخونه رو آسفالت کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82296" target="_blank">📅 13:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pePt9unrZv0gMa-uUyI0twFCyeDXO5GWNiwAfWtTh5wJz-pEwK1A1chfiLTjfoNhqIy6039fGxUViPzBPzEkUINftnTyO1Yw4SpeLndySGTF_C34YRXf_EDujlTmZBF1Y4jNP1vk_ux8mYaP94rSd6NaCJOrDFJEmOkpSRPrS5Bazsofsh3E44oQL0DzAaXkBupDSmqR4svWZy4GFor9FNuVHp4HlTdSbzAmw8_ry4cRDI9nWbq3frVeiiVynD-z8EFAb3hO9jjtor6OI1efYF2Os3RtupfgBkjLgkPWSHsFHO6P7r8nT-jsqUv7qQLBud8AQPt-0BJtoi67rhRsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک میلیون نفر نوید محمدزاده رو انفالو کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82295" target="_blank">📅 12:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewChMGtuOF9N-3qD__bXxgOeJKMRsDtcCPIMWyA7zlmj32tCrUHBUxnp7aRDsN1n8hJy70SqoLx2x27hVRHZDPO1CBUrUHHK8aeWd8UCKEbhLUZyjvxL0_dkhwhCyiEvy3E4Se3urf4QKtqkVt1gaHBzA-cNK_0ZQcs5YWwOmyJBCbfJirbDveXTXk9IkdT1UBW8cRVtM8XJ9bU-QkbmHJNElXJp-UltyQCBVqf0Wg8jayNdzZEmsBDySL6JPAgheSXYGkcjDuqEEmiDjeK-kl7er1rb7rupj8ngGxAdCMSFqu5UTXzSGhtHG911wC0DSKKgO04-WgpwLe_NzYMQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82294" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF-qluAV8jy0DK54gXW1KD8kvtGmgr6uDIokybCnm-sFouqryOl-F5gicu1zx5T_cHOCZtqJYKV7uCCgiUJBB-UpnvoZAP7bHoBAUzeJaHm1sjzOT4PXziDtAE_8P0IaQRZERF8ApJ9duULbKt9IDAoAUrvDCIDaNP3_5k5MUyyHIDA0M93Co-Dq1dv3tYjpsa1Oy8wJtymAUlTXHkbsjxOIiiEKvoPFA2dPGTWt16aPLsgCG0HOPey7S8E59cdppF8puDiBQboVMxeWyhLm38dCq2daOTOwvZ1LoHr_eXRpRGiYeJeiWymqBq_VOpdm10nWIQ9oiOsYsRenqsrGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو : احتمالاً این آخرین سال فوتبالی من خواهد بود و می‌خواهم میراثی فوق‌العاده از خودم به جا بگذارم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82293" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82292" target="_blank">📅 10:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82291" target="_blank">📅 02:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نوید محمد زاده: قبلا از فلسطین حمایت کردم،الان میکنم در آینده هم خواهم کرد چون با اسرائیل حال نمیکنم،تمام اسطوره های زندگیم از مارادونا تا کریس رونالدو طرفدار فلسطین بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82290" target="_blank">📅 02:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToJZK73h9eo9VH34CPstdycFIvsMOa6a9oT4kR_bOufaVxzd0n3xIOpaocjkUr4cAuER36AvllO3qB3bFLPdlu82n9ohlt-UKOLHckrIw8Xurx_7RACEhQsYTkhPkvfqkUgs47lE0NxUQd5bjToHvuBzGu8uAcbKKay8VQG_8XaYugRXkVFcPxPH5UcuJdvJ_1ERgOKqaBABKPlrl2_07KGD11lSiCXDlt9c81QyC00aVBkVdGFsibIRsA0xaQA6HiS0bnTZQxkBv3LWpkYeXg5FTKdZGpoRnxK5Yo27SVwrXViyBex0bW7iabux61PrgSN69goz89f991BngAdEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثرات تمرین با فران تورس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82289" target="_blank">📅 00:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">5 ساعت و 45 دقیقه دیگه آتش بس تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82288" target="_blank">📅 23:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYV4PrWc3XEHiqB7LdVLyPOX58JSG1bQzRNW6zqCVmQWkkiqXRDik-PrGTDjfhuheUQO05YuXDYQCITUqZxlN6E942fHwNLWJDjQx6B3a2QB5Z0m6upN6C1NT0G-5U-VY8MWrqZJtAACmlPK28kf3ukxaByy-0DpsByCv5RzjiaogMge8cxS6yLiLTA0PueoInE5WwAOS8-mhb2eU27fE3Dy4HD-pjpLM9nkf2RO--Rg7xdDWBp7aL40ywrsfB3QaPdc4PNWto_7RFte67LOjmMh4e54K1G7ldThGnLGoSMOaxWUothiGbMJHYFYS4unFjpMFuicmgheoZ6X7TLmWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی رو معرفی کنید که توانایی مقابله با این خط هافبک رو داشته باشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82287" target="_blank">📅 22:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqsUonu4OxHp1wPph0bPEhySduKahESoPbjDmVrZGrBCC4vKlkDJB2SvC1lWZyBVRdEdsfGfDIY2Qvdou-gV8x2j9UnClwx1zsyaekkCrwSIh9QUIqAvgc3FGcsHnucvwGQOkb3SsskKjFf5bfW9dicbvIw-DXE2lprdfvyrH17ALfc-nix8P_4KJs0vqo4Q93aLQy-wA1_l1wo4WOJrUhptOoiikddV5l0krQQIeYboITa7hzguaXoRoi5oNg-UsBd7fs1EcvFJ4H9C9C31cZ6k7Evu78Jstg_D1g6Z_Pd8W29p9gemqMNMxyIW2grZtNmoMTQqdd1P1fq-9eB2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیر وی گووو
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82286" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIMjKUn4Gf0n8G102I8wT1couF-_YjQMXkA2a1ujKbBRPSH6D6x38RNwfXloPV7dnClutQ1LxGGiXcAVyKNkA0Nli00758Tf7Iuvr8t1yifWDzV2n0niWu8riN0rxp7Fp_X6NnJtISDGfcXBT_C8Gp-a9y04Mc9wTciiO5Wm83hcWJHcFBYWVyANKzvJIDmpD2mGUOiqSoAkVeJ3rL0XjcqAY0o5J13ZkemY6O3-gSlzScrg1rIYTAeUfpkUGJ3CpHsheYhFmzJazXm0CqpfKEsgo2pklpM6ZXYtsdly8KQdUGm5L2BTn6rDL-1SosuePC5R6rIloEKHphyX-hHyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین تلاش های مردم برای حفط آبرو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82285" target="_blank">📅 21:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=AFlzWyjQoVG1vnJSxXRTKWaPAa6AoMWzdp4fc47hKDdKNWdTjdm0Cu7r5edQidgceLVsPOElnjAuFUKhl4G6IFqcUfn6dzy750D9bXHrRLS5v7bQqDd5lgPJdJ1lSTj-xdrZfHqqmugPd-OgwVzLb3NRbyG1HG-2u6Q-iw1dheFSA6-VoOIPswPJ5TLojfy0Cz-haNfDPQKY9ZBrfH_AwxoocpAVaGaY4IRKb2ARQdK17ITRf_15J9TuEvKH_Lq7B_I6QkYM2KYdScbVxHAwQlADmBfyv1ZreHUDZ2g8mz1PTFyPHN6_iBqYFy_5yq6hfEQd_g6DqaJr_nb1fBcBRLwTplJgcyc68Jw41m65j6VQ6asONH6WOtdp_zctZEhQrrgtWTPJbN0B1eRo_yWh9CUjjPYBTf-04ZNYZk635YwibDrsVBoL9TJmpB1HEqCT4XgkBAm0YK06hymAoi7J-VX_rE6Z2cXoxlRvgUVrjA_xkNbolptBpMb_wppDO0p3Gi31Au_JEourvc2ehn1LfBRLa4iDWuBD4YbHVoNcliAc398xBiwFTHMEpbLnQ0JInbTnqk6svdrWotgAZTLJ8m79KV2V9sxNuw3-LrcNaj2L-gH4C2Dw6dD9hU7ZQsI2lbgWSSrVPNPqGzhc9UtaumwE8tmrRHXe7WMJYeOFMkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd9bdf52c.mp4?token=AFlzWyjQoVG1vnJSxXRTKWaPAa6AoMWzdp4fc47hKDdKNWdTjdm0Cu7r5edQidgceLVsPOElnjAuFUKhl4G6IFqcUfn6dzy750D9bXHrRLS5v7bQqDd5lgPJdJ1lSTj-xdrZfHqqmugPd-OgwVzLb3NRbyG1HG-2u6Q-iw1dheFSA6-VoOIPswPJ5TLojfy0Cz-haNfDPQKY9ZBrfH_AwxoocpAVaGaY4IRKb2ARQdK17ITRf_15J9TuEvKH_Lq7B_I6QkYM2KYdScbVxHAwQlADmBfyv1ZreHUDZ2g8mz1PTFyPHN6_iBqYFy_5yq6hfEQd_g6DqaJr_nb1fBcBRLwTplJgcyc68Jw41m65j6VQ6asONH6WOtdp_zctZEhQrrgtWTPJbN0B1eRo_yWh9CUjjPYBTf-04ZNYZk635YwibDrsVBoL9TJmpB1HEqCT4XgkBAm0YK06hymAoi7J-VX_rE6Z2cXoxlRvgUVrjA_xkNbolptBpMb_wppDO0p3Gi31Au_JEourvc2ehn1LfBRLa4iDWuBD4YbHVoNcliAc398xBiwFTHMEpbLnQ0JInbTnqk6svdrWotgAZTLJ8m79KV2V9sxNuw3-LrcNaj2L-gH4C2Dw6dD9hU7ZQsI2lbgWSSrVPNPqGzhc9UtaumwE8tmrRHXe7WMJYeOFMkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو هفته پس از هجوم قبلی، دوباره هزاران مهاجر از مراکش سعی کردند وارد سئوتای اسپانیا شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82284" target="_blank">📅 21:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRKiALihZSDJrKvpUDQG3AYQBUapj3T9el_IjytxIkjpwgsT42EdLneiYeuWrFvf1VNELazNxT_MefgnYhTkGM46YQg88_ALP8pejA1ArA-O635FL1vABMz8EQTpal1XMiJnF-NCIv_NzwRpQr_68vhIboVhcP_EffT8aTIvm5xZAQ65vp8WzSWos8klUNlAY0vhR87EU0cLwcy-uqdCnCgItlPBHL0vRCwvl3pXsPFZJK6Le7ndtQ9OHj1y81bgRbb4SU6nWIPXzlTocuipUJZuLqoB_InWw5AEiQN7ty9eT4k8XXDxv8lOt9uTO5d5B4FY6gjBstQ7yIQ7xCaldA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82282" target="_blank">📅 18:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پست جدید چرسی تو چنلش  تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82281" target="_blank">📅 18:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXz6SGaG1sAaCHfEv96El6hf-6VpqccIkMhvYwhBDTdqHsF9IUjH0K0kah_ELv29eIJEKJ4OjMGi-E9DqVAwOwSRFFWGXskI-UIpNczTfr3itTfcZ9p_qB4BHIVa9idMi4Xz0dArqqYmALTdzaGPlBrPA8Nf6s03K5AkRqYOOqzxB_YPxmR8Kzy7GX9LFU7-QkVka501EBXAfpEyJWjMMbD3n51D6X6dkE7Gh5_oN5sI_DfVldKeXz_cK7z4GxP0S4lgHQRdkRvkGzbQWVIPOYF3hvG8QLHx_KOOCzK08W-BM-E7WikAXdxzniEBLGBQr_1Hz_Xx9upB66_WVKE7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxY5CXgOK4PydZSAg3SHHY1sMdAXitIQTKsG6gpbR5Q-FVa0ZBcZyt9AsLueDweLYzSUWAzmIORg66ig4R_uvZ_-Ucb44VRLsAO9o0omqpXL7PgpSs6_75jTf5EjZ5_A1XRzB2B7A9vBODxSgQFdhfSyIQCsR1FckMVLVQI0AAk7d2IcyBXam6S_ocaKfxvQLLqMadPJTKrS59ThHE8ScPzBW5JlOA8DeE3ymIP7wgIidjkFTQVAVVpmv4ai2fzh9z5RqIboDt2EJxgLsDvonHZuXOY_KOQodtKS5xZsyStjGSTkzu9CeLdE_XfQV3_ejhshwOFtM2JqD8MZRoe-Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید چرسی تو چنلش
تا این لحظه تنها کسی از بین اون ۱۴.۱۵ نفر که قبول کرد اشتباه کرده و معذرت خواهی کرد چرسی بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82278" target="_blank">📅 18:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQIptDoKqaEIPbp7TLAw8NkJge_w05aLArzNSbNQYdcL03z9l1wWpea1DNvfn39w81zoUd_N-OaIFCHaMKxahjdANhEdNvO-kg4tNQdbYBO5KGE22p_xcrEp47fbUawl1QV-ppVRyH3meA3jopfImP6Q2n4ntMETzIy4Mp3T3V1VDNfuL5W1s5ZfWiekAXe5jkzKoZ7z3c-f5Xu1q8B-xesnFKLPnGuDsZzAdG4OvuAk1jWzujbGLYMvM8BF_bf9UMNiJOGMHgOZXAFxL_A8_d_QHilL2asRRhUT8nD4ZmPChLEyDGxCyZXRjg3gLI2uatn9tYj_lf3Wa3Das7CeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیار این کارو نکن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82277" target="_blank">📅 18:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عربستان جملات ضد اسرائیلی رو از توی کتابای درسیش حذف کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82275" target="_blank">📅 17:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFRu9snNkyhFFcj2I0WptKcKqoWQHeZL5miNHuxYdZZjxr0m_mI8EIJAWuNaRcdeRIk9RGr5fWtqIIB7kv4-PWCpZTf1uKBpC8Rg9wo00Y1XCrr0vVjPQM0yy7hOkWuDP3ek8EU_ky0RAMX1jf4yeHpq8qiw2EAansZmZcwTm2ScaJaVpNbOILENJyD-Sm4v_r3KBCURDnT00r9P6Ggcm3aH1uuNpD0lnxAYo0ieOWAwutEifJcU50pdb2_IvIb5_15jdcQ13d40jOq5eT7k7kwrGDrne9uwRkyH1rtV1ICXklW4bZXATLb57AgxPjWMV6h1pnWbnnEZ4wfejR0AQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82274" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_zK6JUDR2_ZX9rOeNe2_p2Gzkdc-tiE5vCn05cBFNyPtnIiO6EUHK8G8L-RrThjFtMweNv192od4dEqMtIZ4sWv3Tw-h4OheQjiEMQEqDuonvJq_x2qAQMgih2-edDTlGVq0opV1KgxL1d_qj3eCD7zsMZ7YLYyTPL2oLKTP1ZZj5wfW94AEZQI9tBiWdHTX9TTl3GIaYnOOKHCnX2xQJvewNsC9_5vV78lBjxK1xAxdJHGZ1A8OWiFUOae8u9ECOocQp2WFq2fvveRBVQG-YB0SV4g8u0cb6lHcVVn0vSO2p2BuhF2m5gFrG15l78OJjW7B-h3tl0XMslrKz3qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید متین فتاحی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82273" target="_blank">📅 15:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxACeeNfIzR9cLx8j_4HMu5WklR550dYjLOM5xaos_R8tOTKrLomQ_9w-pZtXegOzbpvmnLCnNbLhp1kcN_7G6wfipuamk-2PLeJEUoX64_TwRNEUFlOnAY4ZQCjtRDofrTwgAMAyhYhdlUdqtY-4nr4AN_JUZqrSuqqFFpOw-MlVeiL9TF1ogSIMb-QNPhU4huY62_f0jvt3u9kjQyK5XG7_SzGJQIBvVx3du1i1OFEjmwaCYAxV3J53QsIzFNPzm8HyfWZOs7YNn4fj4LiqFB5_y-ySeHK4tY_vZa7LAY6azSzjcm0FobaIJ4g-QApF7ie-4GUem8qb0_br2synA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرامو از مراکشیا یاد بگیرید، اسپانیا چون عاشق اسلام بود بهش تزریق کردن که احساس کمبود نکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82272" target="_blank">📅 15:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyRxaeqbjgtgHAQr3LApfyHPLlBw1l7MqLHH1SqtneBkIrFRjxBoCYn_oUjzBtdU6U-OUDoxCfZvF06vrK2FewumhhV2ViFhWBQw9eTC495zEU0Apr16N5BEr2r7HpvXtZHrd29tTvdF0DHgND2DYsE_WYF62ukiA7dwg6NH2uV6By_ss4jflIN_cww94laCgumuER824NR8PwnMDvc26xSQqgUr84QTFtJRz0y-cLsZxsbcf4ymNkifby-TQsC0_9Xnuzh47QQMOilHMXmu_SDf7pIEh-ixP4IyGTltK3lPoc7LUm13WetE4xGUjXIenD9ull8nbcU9FfuHkI4rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح اطلاعات و نگرش آرتیستی که خودشو یک شخص با سوادِ سیاسی و تاریخی میدونه:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82271" target="_blank">📅 14:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرمانده کل ارتش:
هر ایرانی بتونه یه سرباز آمریکایی رو اسیر کنه یا بکشه 30000 دلار میدیم بهش.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82270" target="_blank">📅 13:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82269" target="_blank">📅 12:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QblHvg89XkySl2JxK1lMmgjKcuJpWbRJEqXbOy1GZa9AWunFVh8eN-daqAXMP7hXdsfJpzXMhVl2yyWCeTTVvBeamYSH9_hTn0XMbzTyhGhUhj2gAdSj0zh0H286R6XIu-EfGGLkYOPxZ8Wz-GrXwuJR2PUDRFDXPBHo5qBzzAoRyy876MOa8pb6kfpNc7hnTTspE3ZBQJWrxCPaSVV2X5KRuM1DRWI9lD_cUcb7M1KVB95VpTYIgRJ7GxTg9s-XnLTdZnUKmy-DcTjkwbiCfjqqnjLAWTrACyuXl6zuZkStvnp5BWgRXhn5RtxLyjlplncIdD_dmRw57gE5X1b_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82268" target="_blank">📅 11:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La-6pavr7qwnCVx-_byRNMadVVApxTwgZwKitdvZZj-ptkA7k7j11rv3IiLc1ArI95rcUBJN6gwy-UrHK9EW1eN4AEYfJjF113VBBlWc1ph1xX9zs85oBr7JwopC_1TEK827TKZZNxxe_3E7tw-G-6Aq18K48y2ZUMuJ_B0O6lKt4BtU3LDA_1LjcQ-xoVtLEfia1CV_WgmCXGOUdXVSP0zuDuLWoytDOrhIQb6bxpvelXKS1xwwQHL_XrM1tdnOri71pMirruYcPmJ7_RAZ9PvRPmiSzEnwk9Ga8pKxI4Yo36qWicxDfgdYvp8YnI9VJoG9nZpIfYE76DQj9mFaVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرام صادقی یکی از معترضان در اعتراضات 18 و 19 دی در کرج اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82266" target="_blank">📅 10:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2bK_6VJq4pl0HViMg9ifzgkRsoojXsybWzEfYPjy_CgAyO8Ercrq_mePGc5jMiNfwzdbQm-AI83kfgoRa_A3K9iWhDG2Cg-x_ZeXDxUFkXlPMw7Zu041HUe1miQALw4mxbOwXHxrEt9f4SNlnPYz8qiShmDzEd5Q4AlvAARUxxP2Lzh_LUw9Pyr8esb6zlEUmTb7B5609KIlHewNX7-YfPS5b5j6qX9wnBg9qhgty5sV30d4qBxB2ZMYPiQvk8ndcjKT0gWpRXuVtiSbF5olqPkb2I1AHisNR72YKUWDSl-mfmXzN8jO2TuvQaDxzIKkq8yvCYcnkATk3rcVfJE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی پیشرو سیک سینابو زده و سیناب برگشته ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82265" target="_blank">📅 08:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovQI8q4qlvLdHTrjZLv5AzCNjqjtvrRwIayrRxzJuz15veAqvolTNYfGHkBT0jumCytBafBShQ2BdxwwLcUoL3VFHS6wS9goEIM_Jjo29j0NqVlTuWpEtCOSNkHV2FJNKqsaXGfKEJFfLSnP4X9w8AYSE1zaVYobXCPdp91VRw0ktqIt-26TCogvCNPmAHzXc4hYS3R6ovoeB1w25TgXsvboVd4nURukEoWSxc3yOZeotBN8tEWU2McXWYudCuyk17p12CqpyfzGDjm5wYtdtjtyQu5g9RDccgYQv2LoXo6iu8tPt7YV6hxQdsrOeggWpfi8sEmy1DJ0Og6XDbY99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه کم کم بریم سراغ ایونت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82263" target="_blank">📅 03:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82262" target="_blank">📅 02:19 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نمیدونم براتون مهمه یا نه ولی دلو فردا ترک میده، اگه دوست خودتونم بود باز بکیرتون بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82261" target="_blank">📅 00:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFeGg68kg_ibVO2ZWrjk-swYOtJJClaThZaIL-drzNTRdJhUONbAHF2gCq6Phix-sHEoR3JZXpQ1S88wAH_fw-DQ7JrxpRi7D8yqa39iBD_MzPw1lgm78bLaPfEb2SsBGGE4ogtgZA5sFlY7s6fEeQLQcvSQ7z17TRvY3gEkY9ksR7n-eUm6gTasBy6JlUSXt8BB2oSOeOt9M2qSuPsb4i5-PGcF8rDrZUd-3VEkLzP_I_qfWgzMOPfaPe9bbkNi3rqeQykDPEF3zsHoYRgGQXjiNkkTn4b1br2ieRssRQ7AZ9M08eGvqiax0i6pFYORXAQih7zICYPlKGlsAVzkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم انتخاب خیلی بدی کرده و رو چیز اشتباهی نشسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82260" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NmE2AXTyx7oM6JIquaqNh8KU7J-IMiPI3LqlYkRQYlTjY5cOCpGpt2iDmsiu5tvNTLXDtRCbrUx0sl6fU635COsKWHU-wsnnK25DzxoKSRFghYS3FfRm8hxRh-a4FhY6sToSVL2GHdG2LtvX5ZxAjwBGj_I2aVeWuAygNAojv6W3YLgxeiIfOIl-GfF9HWPloFN4MnYK21QsMOFEEOMFGg03VwM5KAFG6jXzKQBsSZjPvB_rrX8YiVHJspUpBUCYsJFYE1MjsM_IxcIqu-9iV1cLU0CS14VOnW5NI9j4RhzeON8MEMd1-22OrUlj1YPBCM3zV8zr5vPum2j1mWFwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYpa63JfVWjjMu5_AUA-GRs_uaLJSsMoHIeOX0PlIv5-CSylPfnPONRQA8uDlM1aI8O96qKy9PlOMOcnOnmh4TuiQhTc822SW4xI-gSXaLNm7IDJtah8qcglBzhl1le7Rf-M1AxFJRdE-lZC2fqBA0ZC65k8Q1CfGAF9zcASz15FikegjpnD0Wamr1RLUDX_ZXYLSl-H7V-kuVlYQGJmQckdj0N0Tzl_SBSi8ovkxhlFD8bY2XHxv7eFrUIwyAQoiYSbJNSyzKKgFjRdk7xgFOham2H24RMjvuMqnCe3rkAa7hiBmKnEeT_hMcaGVR_WOQd_jhDAe40f0MBGDMnOGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اوبی میرفته دایرکت ملت میگفته عکس با کارت ملی بدید عضو گارد جاویدانتون کنم و اسلحه بدم بهتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82258" target="_blank">📅 00:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
احتمالا همتون داستان جدید رامین رضاییان با کیس جدیدش (گوهر فرشاد) که چت‌هاش رو پخش کرده رو شنیدین یا دیدین؛ + حالا به همین مناسبت یادی کنیم از زمانی که دوست دختر سابقش طی یه حرکت منطقی عکس و فیلم شومبولِ رامین خوشگله رو پخش کرد :)))
📥
مشاهده عکس و فیلم‌ها…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82257" target="_blank">📅 00:02 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82254">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82254" target="_blank">📅 23:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82253">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روسیه بصورت فوری تا زمستان ۲۰۲۷ صادرات بنزین و دیزل خودش رو ممنوع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82253" target="_blank">📅 23:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82252">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82252" target="_blank">📅 22:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82251">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">راستی این یارو امیر علی اکبری تو راند 1 ناک اوت شد اونم با ضربه جب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82251" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82250">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سلام فریب جان سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82250" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82249">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سلام فریب جان سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82249" target="_blank">📅 22:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXfKXspcs9QDLxBr5I_z9JikW-aQVDVXx53QC7l0pAmZAYuEEzcC4UJ6_Vvh-BHUW7L_cNT0fFF-0HbPIU9UpVziR6x9hK0JCIn9vOAHwcgXubpUp3DbwPCuuQcwKR1q3VqV012mJpJQPCCQlQSJsnMZ2Q3bzDKsArzfXBgW_wh1d2VodvVRdR88ud2QSEZrCOfV-vgNrBhmxobTMibyZRFJWYIwdRKAD2nU2FTRZBocBiTYxZBxmqQc1rJoaoqZo6QZgyVgpm4gRucVdIf8bQK0dF3-VN8xj82fChFPrk2TDq93kxONGByOndG7ZxxCrpgM2c9l5b8p6wmboetchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82248" target="_blank">📅 21:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaj1bHk37v-Bi3MxxxdD-5Q8JLhp0KFWhOISgVpG7leu1YhsbUndYO_fnQFFiS0d_eTCeczwPPr8YW6cwwm6jcViO1aXQyH-3jxcWMIiyeMUAbKANzcnS7VdqXRyiTB1depJMsN-Kn_wzZG0-4vSEZbw6KK9ORsLp_ylOLzZVTCeG1Z7yx2dugBcqYb5ESjY9wjzbShbVHyjy5diJeI82vPOqizcCeC_7QL83xrh0iPpGJINfnD6SXJn3rTlPM9mfR0wni42UnTmJmRAOvKIBmKWxVN2p7DALbmWa1iq51_aLB-GQnx3tD12cEjQHPX-MEo8jA6JAlSEO8fvfk1z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل نصف حیوون آزاری های جامعه این بازیه، فک کن وقتی بچه بودی اینو بدن دستت بگن کتکش بزن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82244" target="_blank">📅 21:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یارو بهترین کص ها ایران اشاره کنه زیرشن بعد بره دایرکت یکی نود بگیره جق بزنه روش؟
میفهمی حالا سطح تفکر من و شما و دلیل اینکه میگم نادون و احمقید؟</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82240" target="_blank">📅 21:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCgove5GJDf6rwIbtUb5j9tGgF5QabIe_zuO277k7MgPl9yyehacjBIFVwzf9Ec0Qat5O7Lp2e4agJYMNQ9dPVbrDuH7xqYwlyOzJCne93PEyxiS3eEAcfkSna8IM44cBok2xvdXtmLJrDMKFVWTOyNdTw3hxAiJvK3V9oDz2dYoSSVTKfDy8VH3V0JMXlO7gUnYBS9BC8NPnyxcHdTjiENpidaHrv6VJWN2w4gLT0kCfDqtQqN4GAtoTigykHZtpWgTDXdpeZJjrbcVlinmG4GZr90JvRQ9BrnRBjCdMyvP1BY70UBWgm6WuUKofkV4C0PvEb5EWqpuVHLnMmkUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان رفته تو دایرکت یک بازیگر دو رگه ایرانی - آمریکایی به اسم جول فرشاد (بازیگر سریال ایفوریا) و ازش عکس نود خواسته و ازش خواسته که وارد رابطه بشن. نه تنها چند خبرگزاری خبرش رو کار کردن بلکه این خانم‌ هم این موضوع رو علنی کرده و گفته بزودی تو یک مصاحبه همه‌چیز رو میگه و آبروشو میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82239" target="_blank">📅 20:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پرسپولیس تارتار بوی سه گانه میده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82238" target="_blank">📅 19:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZIWXUT3q3Bhvs6TK1qtqSDaouFPNQSUDfOMbAcV3PO2s7DDF6p569ad7JObdNQ4MkzTnuONCdCPm6_bT_Po0rw5ipftN8oYr-LOQGqheTqbNJCApcwK4PTW_yZTeehs28mqZxBrzClwtBKqzNd5C4T7CfJIlb1J27jFqSEX-jswZKnEglaYZVRbGNR0dxrXSi71q5Z8m62nUKYm_Y61Pva3noFZjAuP7PSeXTfi-PchoNUV9W8_4xAXICEoQdJlYGrJAjp3dMpNlh0n1yUSgznDD-Df_sAamksmu71sol582k_BU1g_YGWdK2D-tR0kSAl3KmA7ES07hSOE5q_QOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5Lk-vudGaEgWDvJqsAil8Y0SIWufGXke934-4x4MgRgTbX_FulYjy-iYCkCAmjIEpWC4A6yi6ICleMul5lfsXfjylqbZXiM0x3oQKEXsYDrzJY-5uHTXrKP6jbbb4G6Rq3bPUCK9iC25_LfJykUe8uuYy-DMwSJoa-h54NeGlGL6Ug7pbCmaXj5YSyYbaYcyZOL8DnbpcJzdC4d43gKMHKfpUL0Z4V9tKB5N89l0nMBoWs_r53dpOtDxAExZ7hKP3OVj1HUPVTMKFXh4P0zaDIqO2Uc4es0Ict4ZGbnCRRvbLXbAK2NfFQGjX1QqSjV0h9BVvj8_L8PUJ1ZFswqIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-H7k0EI7gd6ArAKdS4y2POHgJCogxIEcWd5mS0gkqBGeX69toFdSQ739uzxcrMTHKBUgXAfSSf52m4__lJ-1dX0SyADYcrm06UyPf4TgHh-kj521AzSCkrqX2t9JF5aNG_nJWugOMv9OGgWKtezTQ1Rl9MbL_xmt4iJGIH6xHMpgaSQiGng2Esjwc_dPpfrD9mZH_QNRAqPLfDEK8oC3Xd75gq40xVbfrQwBvTufbxsrhLrLj3bdC0T3kfuHLCbxb0QNsIeO84Nnkp3N3ZvlfgQhck7CpkEs-Pr4UVDEyose0VQo3NKCJYHRzjIujbridB_5YnpKMolk_K7W5m6Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افغانستان
🤝
فلسطین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82235" target="_blank">📅 19:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8lEHcALkIKNeZXNrDGhqwTB4MiLX6rooo38Z75UyYNwjqZw4OJs6Gd6NdW4659-zLidnT_jdbaWhpQQ3UQr6FAHucJ9MPp9FFm4ZMN8JNZZYcT6_SpxeI7t2pN5t8y9O0bAgh9Qc7Hrt3U47HuPOqN5pr0UsECqpmozTyedl1uaV-c6Pq75FWDVzQSCQE3rW9SA8LYpFhmho5D16GNPVD6xBIiZk1hZ4qFsw3yimmcFoP-6HgFHg-_lvFytWLurhXiziaWBxQCVR3WFgYgpwNYwDvccWzrCuzXesY_SNnUZpf1vUHZguygI3yPIo8f2jDPCEC00dGDkyMo03khHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه محمود خستمون کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82234" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82233">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82233" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upNVQ9_bLquTkotJzR9uoCs2YPtxRYxMAw7T3Cbq_FAWubqND33AbNZi64-sGjedai-J1hF4LS5oV9wa63qm7Esgy2Rf7FcdqnSEomEYM23Xwshp72k9F521RpR93bX2OFg6Nxkeui4GeK47SPmNNmNVMyq854bzcNIaBpcip8uLKCSehsBslRZ8LjdlzRgAtJcyneciLxpkd1mYIzl-hDF72ko9ZddbTx5LlxObW6IFbNEiWbr084HYX0SFgrVfj0nSZcHsqvIdjaOWJNK0dSJC4IqgPoqStBD1eFEDqbF_9TMT8vhv9TCCvRtcAmaEUq37U0UMMWlQLBGQPIhggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده بعدی توپ طلا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82231" target="_blank">📅 16:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حال ندارم عکسای خیانت بیگ شگی رو بزارم برید چنلای دیگه ببینید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82230" target="_blank">📅 15:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تیجی چرا آلبومشو نمیده، گایید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82229" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یک نوزاد شیر خوار.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82228" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82227">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82227" target="_blank">📅 12:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82226">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82226" target="_blank">📅 12:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خلسه میگه دیس خشی آمادس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82225" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82223">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82223" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbzpVsTTPECEuJ8t2Hw22bMOH7rTZjkJoR-1ZC4GCTTJ8IBIDa1Dh_ZOBGRQo7bXJDOcnE1Ks4dsJYG6JXB-_N_8wi7AgQfcZ49ign2e6aSqBBcfp2jd_dn8G7RkAjwJgR2HrYxqTt5jTYqqg1WJDxWBgI9mbKdS6UgkRl_6MmoImBvwy0JaZdZLjzb7DVZgwFK-M-Hku1YwlqlmvHvbfdoRnxx_OHrbgamS8POYfpfwiJtXMcokhdkVJ4ecxWkH09nVc4Po5ahvOeMFtSQmO0QxBT3W7uExYPTUdPbVRBXNyyfMuk9-rcW-cEANRTKm5Jf-5_LoY14qi4ijtWtx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری شیپ استیلر و کوروشو کجای دلم بزارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82222" target="_blank">📅 10:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82220">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من بعد اینکه فهمیدم منو لک لکا نیاوردن:
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82220" target="_blank">📅 03:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfRT-67XCSJtiWBReCyvTBm7jD6SGgFEFNWCgHNVBqhfX05Cx_xCvNUEr0StFjayH2xeigGyf0oKDcXcikpjY5ts5gt8GVOiDlXvP9tZ3CtnVoDVmfE8KblNr-g54aiGDBFS1-Qi_y4v7MOSP0lOefg57PsptT_tEcJqEjSVc9pcJ1nlckz-X8sTc28uLbJp-W4Q5MbVEGyDiu2iQccFiVS2cc2vKdKo88uXP2PxP6GXoTbtlXJdZ4tDs0JPaCksIotPQQ73uCD_Uf3Xt37rY5s_yvzLYfMeKEw-tM6lZOx9adnof9eL1JlNlOGzRYqRTQIZ3cc41EWtNA3whGM3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tp5a7epvyVjdNIp06TYf9RhrrjtufROXAfSFHwxLMuQKanfyVRaF4gGgfoRcPXYy6km41df9pv7DOA_CYAm3-AsIQABl2s85X9NG5V4YgBKFsODKoEndgNAkFnbnolCpMBsKVcWKknNPUYMlqMW4RRcZV47A-SCARkAVc2snprthjaVetOvHNA0ywoman4BMCtSwLog7uKgx3j0cmkxObRbEw4g8NtAU87kpr9Fxw7-IhB1sqj3wPZ7anYnDmZYtIh1G4BBoy8yX2qKQAgx8g7RJ3b9sMmcGvlnFRSTvRyrf_kXzjPr78VlRKlueZlPALkV8DyJXzZlm1VxIiqNZVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آخه کی ظهر مست میکنه پوتک جان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82218" target="_blank">📅 03:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abcufazydUWl4srYVs9Oim3Yi_YHDbeSkFjgdHKS_7D_QTAuJItT5Ehvk5-JUlWLxW8H2abYOqEesGiUsHAZMSWOhdRVph9lld-wqyPZ5snweopdHFdbJYQcGGCXIRRdDPhRkjm4WbaDY6ohmESquxWLPrBuixX8A62vD65ZIeKok37FphSvsqNhpZB8VILsVRMShf1zjwVfpOJchfY9OYhgf6oho1gV0-Lz5VhWvENx6udVbtLvnoFpNso8WtnqqFd-9VBKEwuKGgzpScuW3yqlmaJg_6fXkdxwtc7AkGnj3HSgR-G9EOHk1UxpYOilmk2bHAckWOrpBZnqaer2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته بود: بچها زن نگیرید، خوراکیاتونو میخورن استیکر گول زننده هم میفرستن هیچی نمیتونید بهشون بگید.
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82217" target="_blank">📅 02:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: تنگه هرمز تو کون ملانیا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82216" target="_blank">📅 01:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiiUoaPm4Bfq6dTooG9yM3hw-pvVIWBFmm4etUuu02uhHg1koReK0DuQXhGPntSNKhMaDGw_G-Y-PDWx7pBGA67QMpzIn5sPhBFrx96BhEbtFqo-qDR457zOi3CefHU_RUAk7UDTbviOP5i8cgMu6By5EostZTxpXth4v3o3q-dty2CqQe1Mt_J1MZ8iWz_OvudLaCN0cAXC40yK_vpTrff6ITcK0W2eiEG60DdgOBt_66pthbraeTJkXr08JSLyAVszUmwV0QnnvPDVtHdQuHzu7bmIxL1Jho1P9vm0t0Vngrlvc-Ydz5Kmy9EYOGhVoAc8Gc6Ww23VsfVFolHXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا همینقدر موجودات ساده ای ان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82215" target="_blank">📅 00:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پاریس یدونه مهاجم از دست داد سه تا گرفت، بارسا دوتا از دست داده یدونه هم نگرفته
رئال یدونه وینگرو ۱۴۰ میل خرید پاریس ۳ تارو انقد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82214" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1OUf_S_EVbTv-Cq2QreNMzwSsIxOB2k-8MUSl4y9wnvxeCPMVcMpBP3woZgBcdCfmxiI8U93ncGDWamrVdGt9pKy8ZLTMRT0zgMrkBcm7pb-HjwU9k1lfE7DMu-7WS4huxPfsKfWC-04loyOQ52Ws0XRbecA1-RJViZqdbS362b4K0rWkD44YUTxNLHXlVWO77wPdMGuzxXpfb8egVMAD029VEEo5NruR2dDqBu2IhXOpIEsGMW-fE80rZx1cm7njdSz79USRs7AOsevBzen1jvYKsgWR26qyLvcGqCf0MsHFAGL7PimeznUCPhs9CvDv087LRPRcKwqO9f4YqeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش و جیدال تو یه حرکت انتحاری مادر ددان رو هدف قرار دادن و دارن یه نسخه دیگه از همکاری هاشون با ددان منتشر میکنن و نسخه اصلی رو از پلتفرما میکشن پایین که کردیتش به اونا نرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82213" target="_blank">📅 23:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به فاکس نیوز:
ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82211" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3EdBrUtVEuc08UVuxW4zNPsC02cFCeN3UB8oeptgiw43yvtFtJYtXucLIGhnVq7SZpgJlx1Ztc-cMAfPnYN7e8NiFS2pF11sn2B9uU1IKq_8jJZ_DDPyEPQdeUIhSnfX-SXXQM8sgGpLGHsNOJcOPM3cUefjl4Pw7xkxDlWtdCZYbE5vMPndQ9mNWEvHvgZ9flflm0MJk5iWxPwpGMipWvmTu4yw4LuRNYnZ83YwV1XBtvWj5J_NzQfyEug1w2-v5J8lqPaRNDAPdSJqQP27k-Co6KQoq_8sC5GENhxxdanXHEKJEbPAvD_vHnqoiaOppNfUw9Ou9vsZCMwi2uzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو تروقران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82210" target="_blank">📅 23:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82209">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Fit9_JXakElfTnFRPEKUzmA8GQUIyM1_rDizyZfvRKoGHcw0Wc3LrRY7egixDdl5_-Nou1ZorcJKKXKXYIGp1EgEK_N48vc4xv0Ce4W6enynB0aHW5ZOXoQ3kHpfDxeOHITqWRdffYp6tYD6JdBaUGFODr_MNi2YBFNWsuLBry8SgDQySHOm8W_8JvQlTgjNasQMcgu7GpQ8bjtzzy8Xg41dJXO_1-aHPBW8wvSyxOaTCF2_j39TvZQu4WI43tCl21tNdBQRPDhx9fG-g1H5x-hQXDsBdV6_thc7STrjS409FoRPYH3DSDdisspWH-5Ne-nvpSwOSE1E691yGyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم نفت رها شده در اطراف هنگام و قشم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82208" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82207">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مایکل اولیسه :
با تشکر از رئالِ مادرید، فصل آینده اگه مقابل این تیم گلزنی کنم به احترامِ حضوری که در فتوشاپ‌های این باشگاه داشتم خوشحالی نمیکنم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82207" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSFAwyDX0vicW9UBpVQDrfxNzTigpkxurppFLHfpyrDAvKH3M84ZapxApmiWTr_oXWwpI-GegyILUUVGYAmtsHoqTJY3eR78UXrXe0iwwt5fr5cR0SEw0IpCt5-BQji-FeXtOG3zaB_PTlMj2eCND4Sq1hSapY9JE8bbLvKNlEmfjiQvaX7mNn3SXD2acRE0ayBsaCW3bpZYVM3Pg4FF4t2lAajMhVev2hUv26o9Y0c5j-R6Umjsv_hSokDpQ0knPW86eCN5w5h4SrMDtV6Vsqtx6bf72Y2DGyVkWE1o38_LNSS2TTqQzGfvuGNADS3xoXmHQ9Kds-7S-6QIjGfdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLjxdmMsFGcrSUhwtdiVTvs_oPk3Ms9Z6NuHZPTa31nv9MCYyil-lqTSNfrlOoPBTUO2bSIJnkwUW7qKz58v27D0KM18HOFHWp82n4lAHoup6-Q6R67R5435fT_lfXoBeU3wtUiQLSlaROGZcnvAeVY_9BIgMWkdc68Pp2eg1lYDLZtwrSfOctMCV4NSmUQuJLsPH9EA_HcWKyoCKTRE5V_8syLcCAXmCMBGR6JN1q8EJeP54qi1rFfxDNEtvilGRquHoiV9ZcV2fAPavW998DFN14LFB-i5mfykCV-J3TgRXH_cTe4DqNWSCJpppdXLNMmhYC6VhkHTNepx2OBgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT0tZaYCLkybqMCe_ivwUHwJbARcUrSlURV_eYMIJ3VBsTIJVuAIuqnDVhU9Hakx5-2tBNXwEpDP_nlbFECPn88sAGLr88CXPdxDL--AHXig8Ed8BazCisniUxUb_d0cvBowYQ45qovhBRdbrs_wd6qJIKxgYQ-j4LIXDJ5zsy09bIpjevffggZi5K5D1WXS672nzTFIx2NFlqR_Bqo5hSZuDupMGjhTmXj9biMz7dQlOaxDSUnRtSermbuQQoO16h2hhGGYi0fNnLK9p8L_a6ojojMf9tXZ4NURsidjHwZeC4vmbCjZSX5ylu0tcYcLaHwBzuS5xDaLSC34sE4i3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrIAFuvHyLSqHxdzZKFacgqkwBrt-Esl524Om_QwRGsDHv6lHhvMKnik3WSQ_1kr3a1xopkHMsauWZjDu3vupMKk90L-4fdH-KPnNAwjzOIRarQzakwm16_Xh6QWPa0NbO8AG5UBPGFAn62TJcQPSeACps8hRdw3aojp2OmEh3NFWYKignHxAOrGzH9cFiW9DWYcMs12zMGWzT_p9gD4NCRE-VfzYXgvr7lzzBrPM-Re5ApfYWCOaYYmVd5181qJuBUFeMk5Q8c3z1ALkXM3a7HvmhB5lNpbnVmdb4qrNOkc8gCCLX5Px98U-tzhzAm8KCixAJ1Wf6J43nvrzoQgyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ0RPwh4LRlHnu0GZAbNd_kClHCQJWtoZbUMVPT2zJL0_Sr5JDaEVxkGz4dHdKpVumSTngCmyTE0oAiwnJYY3I9X8FkAqNHEzrpbaMrjpfHCzbFlAByYeUC-IlP1KuFmbecQ9etJ3b4POMUvsPL-003S7DAdKYaCz1aKfrMNZX1-MCqtRUcM-TuVXm3lLgiX0UQKURWnkw7uQxOYz4a2OaaZ2dPRydKqmpPiqpHvLtxALqUgmKrIQpeQoRUvMWwkSYzjC62pdrufhiCPA06nwunhsHpLsE7JjAlwTVoM_lfMar9N_IargADDT8anc5XHuHW6wnCH1eqNspAhfn3JUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/og0b-Ae-bcRxaXlCkJ68s8uq3dgZ598ijGDIMf5tJzesXDZyyONzRoPVAf7JX3LC9m0qkhjR7UdRIIadWyP3RlgQ_1XWCa3PAPOdenU9fsalnT-YDjPQoyuZr1327F7hMkawRNuHnX2GVFb1i_9q1q1ByrMMnXRSmg0hcqwBYqchD5YdfRDNfxdJhjzLdc6WvxmIDMjueKWSVAMztHu_OdP5gZBagVMwLthGPeuypwKyYGoqyQb6_OUeSqM8qlwsraa_fABzjK45Gik1YuBCmVpU-Zze4QK_LdDJpGIvjFNyfPj7dK_uy-lZ4QPUzbSuDgCcTGrRMk1MiMXy9t6-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gp2wsEyXcBgbX6JPeI16xkitUgJSr8AerxHO_6z_ltrd27-oZLSX3Fg1K-FqGypc0yNI9f5DTYZFbdrD_c1vn-3k3ornmMAzhHQgLLyO4LDGOcrk_JEnGyYGqzrgDpETV3p1OwdsTUrb9njPODh3bhVVB0oibI7zvygWsFnYzRsVyVB0QvujKVs-SvNuUJ9zG2mZD14sa82nWgHwOOa3q6NDcGjZ8mDRX7CpsHfJbMJXlfTELmMKJWRdkuLkLMMio7p0VQub1KXIaA5ClbkdwwGiJPVEtXJJHBmuN5M2eHL61lT_FCT_dAIt3mHXhw9fn0pQ_Dr9cvyoGYPF0j060Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i70hiIVB0Lys2hXI8bmgavfKuuumW69JMOil03dPC_ssWEUNtWtw1undHK4qUjjWJQh9vh3bHUQgxJAV__OV1zgx9q-6b5i-mhHJm72M7uthMQDCa0CEGOBvC4QEKv24maWdNCVRxbSwRKLRa8h6lVjagh-AXlKYB8K8JgOLe0ib95pNTDJMC4zcKz7UxLGD1SwmeA4StujL9FA8yFvEVa6gxlpxMA3rjbsLbmejCN8TvmrrsgJPPOWr45ilvTWfhwoMqw1vNHfsegxhZUJp3AjBwnTGpi7WEHefXco1pbRTpQgStTidZe1zCFcBodwTbA2qBM-MWjrMD5UPxUwTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoJ9QjzoHfYGA4GfDDvIjVMno1gh9y3UXHtNhSD5EzA0xzENZ5jlyLgiIKX1E_J3puOXaY88Ka7su2aVoxD423hHUgxciEKeQ8WrZQFadxNz0JiP6ClkqL6ljLeBWiNs_IUqNMS-VqI_LeoQh5DIs4JMiL0VltfNzkDdSuH7JdPV355Kan3VVBoI4Z7EcPkRzW3QIxPeOb-tKSSQygsn0lbCzV_dbGws7VboWvrCrkUmc6Npe9Dd4WhuQCwo7-RJ05b_SCyaGz-7re3l8tQH_M7TpF0sjDLKwZDZTEMPQY540L5TNvgXv6_gHx5CdumqQYuYpEv79Hz0b0HpTjmodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQuu-BeEGZ9w5mKMxISeHvC7kdaeUcadQZsxiFKnpxdkHpLm3G2It9jM4otQ25jkeOYJuEfiO7mAoTOIdWMS4IrnvE7W3jah8ZkN2yBMc8O2gQGuQ1lWitvmvbbv9hbI1FnA4HuLlE6yWX0Z6JufE-dCj6sEPHBGpvSP3g8d4NtPEeTc1iZbkZ4YkFULwmTpXEJLie0Mi4a5IimBMnqyH21sqiUT_-yOUV4YS1KNIHwywy-HGn5h8h5Ohuz9FgcHF6DhO2RY5b9C6bAfC2ua8KluiVYc498vWjPFkdcUji6pE8cnK4xRXgYb2EbEdVvYIQYokxYYKdPrsBU5F5jLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvOfc8PEuH782Pe74V9C_FROnXN73UmSegk4dxt8aRnzS8zRP1AZEh8M8U3BTDUHqpWMdc6rlchuBVfQrwBbSusfXYLu82gdJM2_NJ7ngaRbYZ6CNhadQ_5IZUSiRobj6qclaVF8mKwixXqFLGuEgQe5YjDPoLG1B_9mZsvktpdN_VLPdouATlsyWfw1KiYfhR89siUb0Z-6r50MOebvCKMjnNIHo_W8pTD_MWJQKS8ndOJ2D57u56DD6EngN1vzpxBdgNkzpNSeAf-fjacS-Kf8YvH-oBePSWKIv9WQfXZNqGwRo7gxrJS4wtAJrWvb01UekfjLrd1XNt9y-8sfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYT8f3jo2tytnRbipzwdRH5-Oyk5fMs6gGbkqCGXrBz5G3nSFB4n6iOcw5i1am2qB0P8aH8CD-rmwFTk9zdV-ESS16pVT79Xwtcq_f5PrGw2quAVoYxwNJciqHcKHRL4nmuuaRU5it1nJ3fW6Aqq3i1yYuTEqhawsxmRkgKAOuFODm6Bp9PMwd9mpFclhpn5Tttq0VYtxaYvgfJ-990XXKwMYgKD3xuHxdleFIYVYDoZa4tQbqvUz2Vt9P2ydgY_rRQVuHwNr0umkBjJqh-LIBn78Ro3Kv64to_4Hn7iCiswOWwxnc3a6rxPh8KVEKOo1AtdoDMZkgsFGwfN1fWXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnJR78sbH_vC2UsqpqHh4VqTZ3Y49cI6kPMmls7Y1Cgidotkm55VjthYkAkwdineRWPl2dtwOXjh90V_v6vyr3lDlQMPoPQ5tlx-MCGqrPq7PYpwo6ZzdQl_aWYCiD9acHDUFynKfcnZuv30DKWQU3rzt22zvbpi8KCqFeH58OjOoiRfDEIN9wcyW23-7lfP_Pp87A3VKdF4U4Np9mrWbgYmVlMbfxfuehQM8MRppa06gm3nLEYfrqibSElb0sMUNpd4NBdnOfNYdnF_Egvlj9rtfmqexry6qhaPt8Pt3RLK7DQBCChy4x7VrVY6K457HWXqyPd4zbKEbt3XWlbw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzpy6CG0LWJCYWt01Uh5z0JWKAplwMYrgMSZgOu397hrYeOo_-2tqf9ehDeWgh4qV_xjLTxBF0wHtDLz8ak_GA5r9Vg5Lid83OD5Uco0dAuPQf7CkFq38Hvktp_FS0v4pdohM9QJtI2wFTQ_q1pSXcK7DohLvASOJ4upRFAR2YkjVJBxg_FyWqP-s6xVjTO_ciBrgg7LccwHxsmG2qUgROLt7hiiK2Q2lokZXRTjsmMr2fedQQCu2_zCh8x15k3_xmPuTV31gpFNaUcPsHoicaFq4EAiBmOnumhD-iHkalmra62Kq3adCR6fK7DLG54QFEqs95Qgwd7lgxeaMVXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpctKvVp6kgAevY6N1CoLCqbZeiuBEpOlkL-q0LYtre_D8b1Ld8ORY1_Je2p0i7CysPUFj1ihau3CF-M8h14RBl-Cf9EeWZDYhixpPeczY3e-A_AmQ7llaqhW_kQj2EpCRpR6ZIVbdBL5xBilTZHelwj1qQa0oWC-q8zj9Y4MC7vALASM-l1BWPwyleELWZmqyzvTzq170AARAFfdsCh0uAYJ-ue0hQiJINoXPoeigjC_UU8YPTgXzJhm1_nofZjcmbMAJ53oRKxq6VcZUi8YJLXukLfSGNDhUzDV8ZRs5M2R3NVzun5JE_mbO4h6_JF4YAJW13vky2zr14GPBtQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=jJ1vhyt9NM-Q9sBr6FmKzwfbD8ljjkxjRz_nJ1tjT5b5BvAjXr74ATYHckL8-IzmVlH0LEpwTVaJcTpGyVaDhdbDZuDi0THb0W71LvG9USaDupioYyNheqeOlwpimkNAn_UzMCLBEVRF4IdbE0cHCZRMUqWfO2_kQEkUd4heoYEYgD6J1IWrXEBNdu5wRIegUxGWubANiQbJp-VgCnybCbKTgPY_moXXKAdqZ4DauXPLhZ-zMug5rZBmwzmk3ndzKJXz27Q7VlMONJ6gGRxgJ0hC4u41h0rpFj1VkslYtlc3s8XrZl5tbyXa5WIftxU6M2GtJx7iBlKvBScU0KRHV7NdRtap0SnQBLjBo94w3JQHrVjWnlQ5kb2VdX_eZ_zschTL4jCd0NICHI0ItlQzrGBjXyBSrS3H7_EE9dLw4e_ClUSgrujb9FQ2zC42VgiENxUe-hU5GcE0XGGPtbqJPS4gZQRd7sIsUir4cK69HDxGL9Hq63BUOTDjwK8Z4ZkgifCAVb2CDisrcmRbzPQJVL-Y1kwBzC-me8WJB8oB1igwOuql4srLo2sE86NGhDBfcHTTsUVLKF-0ndEyfQxJtFqjNF9fmzUZVj8EjwyJ-iY4YZOAd1oNlzg_q1VXakKkGxsc3ulSNpLGd0BdRSA-E4xIYxRQyN3V39WUOMBWYAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=jJ1vhyt9NM-Q9sBr6FmKzwfbD8ljjkxjRz_nJ1tjT5b5BvAjXr74ATYHckL8-IzmVlH0LEpwTVaJcTpGyVaDhdbDZuDi0THb0W71LvG9USaDupioYyNheqeOlwpimkNAn_UzMCLBEVRF4IdbE0cHCZRMUqWfO2_kQEkUd4heoYEYgD6J1IWrXEBNdu5wRIegUxGWubANiQbJp-VgCnybCbKTgPY_moXXKAdqZ4DauXPLhZ-zMug5rZBmwzmk3ndzKJXz27Q7VlMONJ6gGRxgJ0hC4u41h0rpFj1VkslYtlc3s8XrZl5tbyXa5WIftxU6M2GtJx7iBlKvBScU0KRHV7NdRtap0SnQBLjBo94w3JQHrVjWnlQ5kb2VdX_eZ_zschTL4jCd0NICHI0ItlQzrGBjXyBSrS3H7_EE9dLw4e_ClUSgrujb9FQ2zC42VgiENxUe-hU5GcE0XGGPtbqJPS4gZQRd7sIsUir4cK69HDxGL9Hq63BUOTDjwK8Z4ZkgifCAVb2CDisrcmRbzPQJVL-Y1kwBzC-me8WJB8oB1igwOuql4srLo2sE86NGhDBfcHTTsUVLKF-0ndEyfQxJtFqjNF9fmzUZVj8EjwyJ-iY4YZOAd1oNlzg_q1VXakKkGxsc3ulSNpLGd0BdRSA-E4xIYxRQyN3V39WUOMBWYAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9Yf_yRw4alEBqY3_Y9hCbJzcQ0uXRgmTeg6wRyZ_ThLcNMeQ3vrNZXgay8QcjD1IShnuOOoADSfF108iIRSE1TC9CP-LLYSxusMDiWc-k3xi93ntwNLzplbBqihOFAC9P48AtZzCpXFB0UxdUlF2enZnK9YKn4EHpDWXBNrf3Z4dRkPcIwCtEVoSrZxP4Ge22rY-B5MeF_hwVJw7PynSGLzlNNOo_qRlzB7YdxVddZeGeklCJLzTL-3lb0BGVEWNRD3Yyi1Fg9iEWMKCLwR4UwiRH-Dl8m2mHjSEPSYVQIGGOK4fCWX29rRm1omDz4DHlJLl-rUdXTmHhyNInijsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
