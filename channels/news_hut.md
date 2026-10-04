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
<img src="https://cdn4.telesco.pe/file/LP84syQkixBjY2HgrjZmL23Lf9f_T2CL_5XYZ2pi2UwzHAnG1YmR3exAiZ2g-4YA8BmhPaTbrr7IuOh2M_MLR1xWvg9BicYjp9dZ76VQ0jatZIGpfxdj-0-b7VXjTaUAu-GT3yZ3C55NgtgbkOBq7V5XGLjzfjm7RR8aB9igjTpMPzRI8jLJazoleiMlX7oeqtobxE_hDP2pKfz75F1T6Bnwh4MYm0yz0cDcvnDibXw0lEmFh-dFhq7i5aqtbX5TXAyM7R9HXvNqT48mlBKYB1N3yfRSII8ruHZ8tSDyco0GBPEphfU6CRwwF4TkW3w6jJyGrWG0UnrDzV1t3bt0Hg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=fnY9zOGGkZf9830vlpLP5iUr78mWOhQ-6b8vAZUBrdDVeLkM_b-DiTF8fZdYZNDE6TiFvuOKYvx-z9srnpyAO7Q9DCopS7nQizWO6AKBXUvhRz_e-E8W38r4RqqC5Gfn5a8E0Z7Ql9B3GX1OMqaXXPcHa3P13ziipZWxZH84TQASSWQy7rlirt5KBFTF-oYvqchstBrs3fRsVbvJSIe25prpcJerERGFn5IK7bHByGDYMZ5JSjA5_y4d2Knevj16i4Emdr0ZobZ7onOSVd82gW-TWu2tVxDjAMBJy3ALdys95mMyKNjgD8ibksQ9Y9LMLJ59DpcDgBfxPxt8bzP1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=FULAkLCUhMDIGOJXqoNXTEmABlDHsieOyyX0H4XTlCRnHs6YSNX01ZN0Ugrne2lWZnzlNFAWj9m8j442hXfV2WrpiawBWYCxl3786tMhdRqgLvYLvZOs0GVsInRpZmnIQLpSASMEEuPV1qAMVrehdSOZm7vhCPJBZD00476q39aabETZ5k-WtxIQuyY9_JsV-b1o8VAUh5emk8Sfr8KOBz2PMdS_to6oM7rTBh0QQ7Po1S2YoRiTV5ZuWs8mbB9-eU3I8LdPMpypZUSHimSD7jjla8QtxTLwoQ8WrHfYz3RxPOr1LanNyTWTil5guK4Gt-Y4Nw6OguEmfBV5LfRMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=MolsRkj3v7pg0Mi8kVxtJHfkBvPi3aYvSnj1DYigUur3iKTlze-b9-CZY8JTlPfrVgmY5gxZZYTqRsEfPKQ0un_NORYFlR-WPbALjYV58obXcTrffkfhvYO2yZm-ayaqjU9CLlq1ApBGKen9Zk6quEDuMasbqRqWn4bjtxE-jlN5CkdbJ0D7pZh_E9VYyzXO0Fk38-2-NzFiBTN2ioWHC-Ax-MNe1yKGsuKa1fptuif-7SSSNvX_46A5wozDmXxOLaLi44H1_7B53RFJRn70c3MSFPhulFIubhPke1H4-3Xmhv6dsyQaZOdp_gnuOPV5jwVdITbAzHbqT8LE9fsoYAHHrIUWVMmKnswQSqp8LiuIgUDDnH-B8vEklUNvbvDRJJlUjLwx-f4mmMmD0UfLKkzbOAFBFq5SAURrDbQPC0sI8uEUtUR6kyH79afkSJmDMszi8ynE0CwKs1xDvtsD92WA9OyfqnfDBtkN4uN9NiCI7Iey7xRSPHXn-cEpJkIahFFdBGDBEPO8ETAn9jzg0kwqkApbY3rf8IvLG4ViDNktkdb13J6TRLw-RIJ6yxh17e_lD48aEMMF3dVcSduNyBh3dPAHYudPgwncjTol26t8oYYy2a-FZ4SZ6YUXdZwEl7ykRgPotKMvWkDFqDmrb4aE3PBy-RYP2tnMRBSHifU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=CW-RmmqPxbb6b3Hc-N1NyKPdh59uzJgvWtfhvb57W-sUMBcBZ3If9rePAk5ZDKnjqRWKSq4VspBjBHFmki_Wj9LcyHmm4sLl5br316NSM4Ck_4Ae719X4x7tr8EzzkFL0uJYZNxLVA6C0ZmngZoe2wLr6D1MYM7g-LfgmEkTFyiwqMLNcDNUMvPejDcdIt5Q_7r3Kw9nd68GWsQCbFSShB-u9iNh5mkIIz_lhz69AX7JETtaxKDLZdxbhWYH7vibhSHyOLR7KGfPh_ltOpnD6v84T8ec4pRAovHKEhCpkdS7-guWnd62gPj4Ws60JUpKCbW1NPeJiKrTt6ePWBOdpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7872ea066a.mp4?token=pSGY8VwZxR9-GroUZ4kTxk-KkFHiQh-iFZL-aNnl21J5HWQWmvyM1Z61gPm777GDwkNQe-gnGQ3jzJyldsMHlaxMAZn4JgNwtOPdmhkYfGIgkjUtQNzl1WeJVf1S-s7YLv6Yr1920zAvceTzELi7WiIhtFLy1fwJr3IrR8lwSjc1n2dswJjMzgt5zF8dItapTI3QekSxS0HxGwcWNxgPAIa3BGsnzKeSD9JAtSWV1ZnvWxS88ykJBCG2ZzC_XGP9BDhFArEU_13fPZjpasEXuFNpv58JpDOqObuEdbqR3SArRQOLA0UR8BINoN7C7ElvhenOx8iL2JYfWQk2wmFgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکشنبه ۱۲مهرماه۱۴۰۵؛آتش‌سوزی در پاساژ خلیج‌فارس عسلویه به دلایلی نامعلوم:
@News_Hut</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/news_hut/72719" target="_blank">📅 14:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDesa5_kt6wJV_MUzPI7MhdjpBktGmdgvvPBRu3Qr2o1MdablP5tn0vdlB1AXTYEakF_hKt2RskZSny1i9DXOoD4TP4E4MfZ--CN4aieSelRHiRZaQ2WvDKo78l6eHEqbcJj0HxAFeFS7ygr1EBmF8SmU8G6xyHruVggjE6Y6IVn85p458DM17PoElGlA-OjKRHmPzcr4RD_XCdwQ-yUQ1mMEEkRUtFj6B-1jUAOR3hS34YFhQQZw8vCexfDCTZetR-GCHixuujK1RtAoJhXAzgtqTbGPpLXHlj-3g6fsBTVuCg0VgUnaIdGwN2zL-rP8-jHlQ9uxJtVzv6tQirSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران _ نجف که قبل از محاصره هوایی حوالی ۱۲ تا ۱۹میلیون تومان بود ، دوباره برقرار شده اما بیش از دوبرابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/72718" target="_blank">📅 13:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3330937cb2.mp4?token=BDdjLjuFIP__runP94ZVL78lEFRxkqsb3t3KE4-DZOz-Pq9lWNJEeyLvS-btlH9iSHrDFtzz54C6-cX6ciHAMUPA5V0rVn6fEJXI92aT0VYI4Eq1tqIHdYeV8bZ4nhR7VYuJ-B6KcGg-vAY5iEOg4D8ICyRUR9ArSDqpuEvrVexyVPmAL-hBl-tFSNitgIu-n5TaueI8q6pqZ5uRuOZ35yak3DIF-vdaH_nOJIoS-IqS5JDLX6YSnoPaOYOA9xyA_aUO-fmOkkZL7hX4GaRyQIOfdlCez20ULzVHULGVrZDg2UQY2nYkIi22TErHvkCa1VS47O02H7qsffjdHeW7HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش روسیه به پل شمالی در کی‌یف حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72717" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=oPQRo0Zu4K6kQm_n7l5nlyNUuHMrB6KcVlZcdjRJ7hNInPNXS71WqQuOgAnNjqbuAVNo_zsDvDrclDLa2mUjrsmnu5LsiNdf78B2S-fOMx3Xt2D9YxNLWD5l2NTfTafG0hMtOCwqDq1kXb8beitfIsULgczLKM5skfxFecfD2YDz43P0B4UhqIjy8vQo0kU4fetLHHL9U3ebDtSKuaR5kY8dJCFfGt70gUewriHcddyPWRNewjEm6pYfQydK_mJ5jeIbuqT4vJ8bqSSdM39yQyg_SyQxoviz9mg5dRWaTh-OPFMWL7cTx5P7sm7OQ8dRof8Wpozb4yO_y0P1qewsEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حرکتی شاهکار نگهبانای ی شرکت رفتن با سلاح برنو بالن هواشناسی رو زدن و بعد زنگ زدن به سپاه گفتن پهپاد آمریکایی رو زدیم بیاید همین الان جایزمونو بدید
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72716" target="_blank">📅 12:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار ۲۷۱.۰۰۰تومان
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72715" target="_blank">📅 12:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da8647691.mp4?token=i85BRVIkrukhWbd6Aj9LYfJSubApoh9YSzzFZADwJKNiPHeK_9FwniBYseuyBxFe2M-Zth02DjtoN2bEu6e_xoQoQfvuku_wJKEgiLz4g5vSjl9TF58rQadZln8WRjY-TciuqjI9vYyykB6pF10ZNOQZo34t20gTTBNtKQCc1TLbCSsmPsKP1098A7hNu-wCFO3e8UxIpUMhRhr1XZ5pL1kqAqhU_RSj_fCAjfCwOP9vSimjA8JSUti5riBVZF0AlFu1i2eAj7N86e7lY30E6zvb3Ha1_Oeo1E2qdE_C0VwroJrOFGVWrQBCkajTz039kpdkCh3nj7J1rUr02ezBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da8647691.mp4?token=i85BRVIkrukhWbd6Aj9LYfJSubApoh9YSzzFZADwJKNiPHeK_9FwniBYseuyBxFe2M-Zth02DjtoN2bEu6e_xoQoQfvuku_wJKEgiLz4g5vSjl9TF58rQadZln8WRjY-TciuqjI9vYyykB6pF10ZNOQZo34t20gTTBNtKQCc1TLbCSsmPsKP1098A7hNu-wCFO3e8UxIpUMhRhr1XZ5pL1kqAqhU_RSj_fCAjfCwOP9vSimjA8JSUti5riBVZF0AlFu1i2eAj7N86e7lY30E6zvb3Ha1_Oeo1E2qdE_C0VwroJrOFGVWrQBCkajTz039kpdkCh3nj7J1rUr02ezBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت بر سر قبر علی خامنه‌ای، علیه مسئولان نظام شعاردادند؛
«گرانی رو آوردن، سازش کنن با دشمن»
«مفسد اقتصادی، سرباز آمریکایی»
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72714" target="_blank">📅 11:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8qqtues5tUa8Wm2QA0BGGD_XzDdhkONOxMXCGJUZnQQY2xxN_YlkZVDXnLGjDjqlVmx6mKpXDhSAfAWORUXCXEYMSAKjaO00IzJyTi0P1R1-7iFOdDMdGZ3mdEanUWr1pVMIxIJ5-qu8sPwVMNkfc2SFjt0y5BAK_5CExfd1ldL0RdoB6SfvG0DfqCt9mnIeQBCWbqZtr-mEkXEgZefps1b5N-z_3DBPnIOUuge08PeJ9h8oyJDfESJzny4OQGQCuLhDciW756v9nFvOgxfTnk8tp2gHriBkZl9TKCpSKqHVGuiJvavZklsYp6Pg6_zcnu7hVOwyHP8f4k4No90eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72713" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72712" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SutOHwy3n9k_A7Uy4uGFYGPcwLNd6xANPFJy9lWVgFUXdZAB-iterbunL5qQGGxL-T267OJHjeFjIX2HQLkOOTOx6nRDwkK1PrXfi7X_Ui1MNTnkC_grjSVad-nBkNdFnElyOcSV9dJLyv1K38Sx05UuuF1-AJlZ98cSHgeVpykOLJuPiyMm0bDuf06X9R6ZDVhbprXbZ5i0jYEeFfbI5rWNrOeM9ZOJ7QXJtRckEV11POb-mN6KAFcKsnKpPOn_VR3dmUhQGnprUxdURta-WJ-30lssK4ytHB4c3LxrPZ6TgE0lMqaQwa5avszjcGVJEnxRjNhM9EZjOqciaUl4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72711" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e9a4b7ef.mp4?token=E6GXW3nmyeqA4WWQ0umSal1jdAX2ufnjeZxnKKK88Yy27EFxZhlefWZ_WatrhkKh9cqQl5tLlQCNg2xY4a3rqYroeVKfThsujmknuPWp03okrVGLJ6pGZ02ujVIslVzecQeyZtqdmX6GMHGPhuvzXt7mkn_APsWcCjPKSx6dleBrYuTwcoYX7kCwdB01Fz7EhXjVSXz4OeSYrF9GRmBbyInoeJRaoaSq5B-qdX_MegdLMv-kkqtSK2YFo-_1ry5s_7dRKf0C2edK1GwxjFen6wVc3hnbVRyQrk2DVRe0Xm74nc0BHukaanVvD0VkuEeKJzTtSkcgR8YN1ZZBdlNwHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابایی، رئیس کمیسیون اجتماعی مجلس:
می‌خوایم حقوقِ کارمندان دولت رو 5 الی 10 میلیون تومن افزایش بدیم!
قراره «فوق‌العاده خاص کارکنان» تو کوتاه‌ترین زمان ممکن و با امتیاز 2 هزار تا 20 هزار واسه کارمندان اجرا بشه.
این افزایش از اول شهریور محاسبه میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72710" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EWVP1uh07m2VklzZHKaeovUvYj80LUHl4jmReriGbA2Vspk6z6_0ibu0HM0Chi-PSksVax9IwCJQdBdMq1CMAe49xyhj2lxnZ9jXQ4dnr-GfXlEQwgPGnc71Y_nZ8-oc-HVANA8x8VXZzTRa9AUXZI6mPOjuXJk_z76h6BXktTQQM_LuC4uSR4sW2BDWCF5KEGSbcBtzja9LDInaqg4kLv48KQeO7H1wLbVzbDgxMwb7d-AsS3uBOgxwo7yEe0iaiHelTIdIJ4_qp06305TqV9qfcLuC8O2iURCBe8fNrgOzZW0u4APwi50Vfv5euJ-Aq3yJh1br34EMapmFtTHN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a343c0ae1.mp4?token=EWVP1uh07m2VklzZHKaeovUvYj80LUHl4jmReriGbA2Vspk6z6_0ibu0HM0Chi-PSksVax9IwCJQdBdMq1CMAe49xyhj2lxnZ9jXQ4dnr-GfXlEQwgPGnc71Y_nZ8-oc-HVANA8x8VXZzTRa9AUXZI6mPOjuXJk_z76h6BXktTQQM_LuC4uSR4sW2BDWCF5KEGSbcBtzja9LDInaqg4kLv48KQeO7H1wLbVzbDgxMwb7d-AsS3uBOgxwo7yEe0iaiHelTIdIJ4_qp06305TqV9qfcLuC8O2iURCBe8fNrgOzZW0u4APwi50Vfv5euJ-Aq3yJh1br34EMapmFtTHN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانوم 15 ساله به‌خاطر اینکه هر هفته پریود میشده به دکتر مراجعه میکنه تا بفهمه مشکلش چیه؛
بعد از اینکه معاینه میشه، دکترا متوجه میشن ایشون دو تا دهانه رحم و دو تا سوراخ واژن داره.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72709" target="_blank">📅 11:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=ZpNlA3hGqYfEPtiTnzRAHF2_sJhkUEFsYMNYeA_lnzFkDp1QSr1Zpu9cZKMJZ1u5nJGsyA6odbcLhk7gJQwDAYFS6oAoYQOhGeX7jFlhV1TDvUhrDxmCgO6_RXODjfHuIi1QuBmIleTavL8QESIkdkSmcD1CwcJrAnq7lUnImZOgdz8PMeuQKIfsm3nwWQkkeGwUlAwBJiEcpFrN8taOrCLTtiHl0v1tQfeWesu48MMCFn6LJHtk2RfXTVEIZsrlkxI1JTYrWZwB4Hom96DTjrcwu_gZ50eho8fqXcCdbK3D_IU1WkyBpWkwCEYMMjtnRaQkFvBQD_rjmM7iUKtU2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aed172c29.mp4?token=ZpNlA3hGqYfEPtiTnzRAHF2_sJhkUEFsYMNYeA_lnzFkDp1QSr1Zpu9cZKMJZ1u5nJGsyA6odbcLhk7gJQwDAYFS6oAoYQOhGeX7jFlhV1TDvUhrDxmCgO6_RXODjfHuIi1QuBmIleTavL8QESIkdkSmcD1CwcJrAnq7lUnImZOgdz8PMeuQKIfsm3nwWQkkeGwUlAwBJiEcpFrN8taOrCLTtiHl0v1tQfeWesu48MMCFn6LJHtk2RfXTVEIZsrlkxI1JTYrWZwB4Hom96DTjrcwu_gZ50eho8fqXcCdbK3D_IU1WkyBpWkwCEYMMjtnRaQkFvBQD_rjmM7iUKtU2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:‌ حتی اگر بمب اتم بخوریم باز هم نابود نمی‌شویم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72708" target="_blank">📅 10:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9499513e9a.mp4?token=NWOJYNkvWQUIX7dYY-A03ke6rQF0gwczktsqpvTOXIYcV-prejc5Wmx_R-4ZENDEFt1iu7SuJUBBjkeofGx07nWkVQwt5mawTEw05xrrcGEBvdNMcUPs9k08UFhY-YUNSjoiwmlbjY_kurSmA3QhIc5ZuSBYQ1lKlKxREhFtMlI-9pMm-zPaU9mohsSmY5n_PlBfxL2q-cwVsxgnGGIRmqLEi20s5qtSs2ntge7ef-y9LGS0XivSDKr8wOOqcpMMx6Oahhh-Xisf8FKp0Nv9zGLFPY7vekiCCxRXJUy7Hxe0xVYoT384xZKY4BM-i3dBJ_MLBJRekpTP7LjjwOTuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه این مدرسه اس
پس ما کجا میرفتیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72707" target="_blank">📅 10:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8589525917.mp4?token=k5RPYTXIoyW1ITx9SGMwNn79iNX6JYUTZZ7Vm5icJwSORYU4MmRlxv5Y3YUm-oEx8wCed9NRvGceaaru0t4qvJKL-miEdKQuxoxA25RyuTYLCFL2AojB322VhyLUoxSCswqpUP5aBb8-AxITMhiK2IpmRKCWHmmeI6QDWM9pZakp1oor1o4qrC9VTSXcsXzF41YaEy_azbzJ_trucuCpXxQRcIVSO16Cj_pLwmdQPlgc1XXEYnnrqbIrFVgVfJ6fypn_FE9_A9wcY22A2-pGmvE7y-3YELdTIdfRdE8F6LuYzaAfft8bFGN3TOjrKwzotIdGussGGS_w8eg6hVhqqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8589525917.mp4?token=k5RPYTXIoyW1ITx9SGMwNn79iNX6JYUTZZ7Vm5icJwSORYU4MmRlxv5Y3YUm-oEx8wCed9NRvGceaaru0t4qvJKL-miEdKQuxoxA25RyuTYLCFL2AojB322VhyLUoxSCswqpUP5aBb8-AxITMhiK2IpmRKCWHmmeI6QDWM9pZakp1oor1o4qrC9VTSXcsXzF41YaEy_azbzJ_trucuCpXxQRcIVSO16Cj_pLwmdQPlgc1XXEYnnrqbIrFVgVfJ6fypn_FE9_A9wcY22A2-pGmvE7y-3YELdTIdfRdE8F6LuYzaAfft8bFGN3TOjrKwzotIdGussGGS_w8eg6hVhqqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بخش‌هایی از کرج، از جمله باغستان و جهانشهر، روز شنبه ۱۱ مهرماه ۱۴۰۵، پس از بارش شدید باران سیل جاری شد و خسارات نسبتا زیادی به شهروندان وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72706" target="_blank">📅 09:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=G4MuFoRjX2hHxtjgTH9f6fh400sUz73o-HDNwLK1F70TxPVfMUArY2Utpu5DQwoRAEzGa0di4HNmqPnwh2DIHcJfCt6CuKzkQcV9UUvnXRVXo9vKIn4ohJX2S99cENwLC1XD6q5IpnJwL3QDXxF0V-n_TUwqrnRqOD-Zz7lWFbRdQG34WcjVu2Nq5vUV9aFdMjxvXtiAZWPCWIbmxGdhH77WSo-V8E0Gl2Md8glRL3dvrNc6omQ8y6aooy-HtuKTbkT0TUmvhk9kO3xyrA7YrPIYFH286xDFnc2KOcPSDYgwUv6M3ZTPRojsDUxRC_pUZ74PB_PDBsHNyRSu2pY8ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c198c4452e.mp4?token=G4MuFoRjX2hHxtjgTH9f6fh400sUz73o-HDNwLK1F70TxPVfMUArY2Utpu5DQwoRAEzGa0di4HNmqPnwh2DIHcJfCt6CuKzkQcV9UUvnXRVXo9vKIn4ohJX2S99cENwLC1XD6q5IpnJwL3QDXxF0V-n_TUwqrnRqOD-Zz7lWFbRdQG34WcjVu2Nq5vUV9aFdMjxvXtiAZWPCWIbmxGdhH77WSo-V8E0Gl2Md8glRL3dvrNc6omQ8y6aooy-HtuKTbkT0TUmvhk9kO3xyrA7YrPIYFH286xDFnc2KOcPSDYgwUv6M3ZTPRojsDUxRC_pUZ74PB_PDBsHNyRSu2pY8ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خراتیان، کارشناس صداوسیما: چین ارسال تصاویر ماهواره‌ای به ایران را متوقف کرده است!
مجری صداوسیما: چین به ایران گفته ابتدا مشکل خود را با آمریکایی‌ها حل کنید و بعد به سراغ ما بیایید
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72705" target="_blank">📅 09:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72704" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72703">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVmg_gR4y1yriq7JLA71eDENl7McMb6TwM0Pakaaly1N33SIbar7rucDsetA4oUxnNFZBgWOl7Iy0O-o6cEvNJt6_IorlyheP-HSU8nWt5l1vaeUpUPg95lOjYvO9Tn6rsWROYj9UzmXfQ17BSo1AS1jv94QuNAyrgz_R3NaK0VCy1hOr1NJ0a2335ATJvddJPX4EbXH7N4M6oDU7Lf0a5KF6jizJb5z6X-nrbd8wmsJ7JAlbSUxTJUwv32J3LRcj4KTNilk8dOsTCVCHIixXDUgYilrdOe-6v1wcb-JzUChF4rcnGwZYD7assKd0Ps7WIcPwa6SSttioKjQvW8z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72703" target="_blank">📅 01:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72702">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2qqpW4KoBVgiCVEOdNYgKCNcsSplf57OqQlhqRLADRdmd6KVloqq7I0eJpw_rNjh3QwCKn9HWSwxEoCm2e646zDU8j9lGpdzWwfem9wZEGijzZFJSSorelMdhuxKfFJErncIMBG1bgFXC83SV5GU5BJVdnvKW7F8Emxg11dnjdr7-FuPwl_w7lrbMfkk1E7ujCyRUv-jXIOOAMCSEx83iRN1YtjMRZ-uqrxhC7YL0wUdCor3heZf6qpGEcJ-EajwLPsCLNLbv8BAVhRkN9vJpLtV5R35z1YrC52Bx9FDXS624KMA_Oct_jUD3CRmCEfiws8YhEVqwj5OGS9Ferpimro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2d851559.mp4?token=ZuDwpDqHLeSWHafZ_IASCXIdN6vLW7x1JjsQzA1NaI1FTB2q7S_taym3snN3YtOch0j4GhDIU5qb4PRqqZ4iJVyrOxTNj7K_fVtfMaYl4hDOHBq0EtDi_f7FqqCi0H1rBdn0fibxrdp7ZrY7opEtLTQR2_8W-uerbVHArKGUD-CYbNUwrPiUnAzNydpZK_wl6sR1Yq-Nzc7OHikt5vj4r5X7bhKTHham7YqQ2VKiBy22nUz7gv7rJdLiMoyT2a80L6FJ_J84aZQlZiexU6c1ZAI908oNciWcGHRqg6q_J6cfzSeV_rNE1SeDctd82k4-nxRdyEOSS21M9WfCE0sB2qqpW4KoBVgiCVEOdNYgKCNcsSplf57OqQlhqRLADRdmd6KVloqq7I0eJpw_rNjh3QwCKn9HWSwxEoCm2e646zDU8j9lGpdzWwfem9wZEGijzZFJSSorelMdhuxKfFJErncIMBG1bgFXC83SV5GU5BJVdnvKW7F8Emxg11dnjdr7-FuPwl_w7lrbMfkk1E7ujCyRUv-jXIOOAMCSEx83iRN1YtjMRZ-uqrxhC7YL0wUdCor3heZf6qpGEcJ-EajwLPsCLNLbv8BAVhRkN9vJpLtV5R35z1YrC52Bx9FDXS624KMA_Oct_jUD3CRmCEfiws8YhEVqwj5OGS9Ferpimro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفنگداران دریایی ایالات متحده در حال سوخت‌رسانی به یک فروند هواگرد «ام‌وی-۲۲ آسپری» (MV-22 Osprey) در خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72702" target="_blank">📅 01:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72701">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=jWnk2ARFgOomcbM4mlXJtnB9vXoAYBX9jMme4gDH5YDUEg4vjV2QLO_Hr0cqvu0ItO-PG3xbRCXnE_yNEhblJnkf51HDd6rmi1VuKvYPuuXXeWmMqDMLa0J8AtPq--rSTBXWfSOp7QklHinRVfPViV1dx9KhXABpKvX1ZoUerTpu3kfrFY6mr1sCJQafemXXccTTO2-Vnm4qBS3mIIPnF66W5MWnbv_QlZXbXbmgvo3ZyXfqd_oleh2-sYGkxFUEFj98WRuFuvnS78i3EYIMfEs5hT4hsLCGS3A7Udo4-Ja0hGM-pyMwsYZtZGGF4jIuV63kDDRW6EBfunjSOzSppw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f216caf4ae.mp4?token=jWnk2ARFgOomcbM4mlXJtnB9vXoAYBX9jMme4gDH5YDUEg4vjV2QLO_Hr0cqvu0ItO-PG3xbRCXnE_yNEhblJnkf51HDd6rmi1VuKvYPuuXXeWmMqDMLa0J8AtPq--rSTBXWfSOp7QklHinRVfPViV1dx9KhXABpKvX1ZoUerTpu3kfrFY6mr1sCJQafemXXccTTO2-Vnm4qBS3mIIPnF66W5MWnbv_QlZXbXbmgvo3ZyXfqd_oleh2-sYGkxFUEFj98WRuFuvnS78i3EYIMfEs5hT4hsLCGS3A7Udo4-Ja0hGM-pyMwsYZtZGGF4jIuV63kDDRW6EBfunjSOzSppw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. البته، همان‌طور که می‌دانید، ایران عملاً از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72701" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72700">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=grbQ3w8dC_rVYANqlj5MVg600NVeWA67rQp4yOjiFyT5GK2uwWao3Xwz_UuWX1d-1KYYqCrQufjTfrlRly_01c1wUl6667w_XFYUf4qEzPfC6ZWzFTwkUnzdRDA-QsDUemms3gGNaprCua7UZU3yVog9YYrQNlCPTTrA5wvXDMDxwqG8KwzZeLfxnL6C7Ppv9b3YJpo46kRP5CcKedQPrUhm6ShjfMNrlwMgiod6vepNFKL5vQBbOan1SN3aFPNDTH3rYVEZKvRrYI_cA1JkauqENjstJ-GNHHLAta-K0-5Jdk8Pl7sjf9shgSv9U_uZSF88g4gjG9K9pAKWYXokJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33db7c818.mp4?token=grbQ3w8dC_rVYANqlj5MVg600NVeWA67rQp4yOjiFyT5GK2uwWao3Xwz_UuWX1d-1KYYqCrQufjTfrlRly_01c1wUl6667w_XFYUf4qEzPfC6ZWzFTwkUnzdRDA-QsDUemms3gGNaprCua7UZU3yVog9YYrQNlCPTTrA5wvXDMDxwqG8KwzZeLfxnL6C7Ppv9b3YJpo46kRP5CcKedQPrUhm6ShjfMNrlwMgiod6vepNFKL5vQBbOan1SN3aFPNDTH3rYVEZKvRrYI_cA1JkauqENjstJ-GNHHLAta-K0-5Jdk8Pl7sjf9shgSv9U_uZSF88g4gjG9K9pAKWYXokJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ: تصمیمی درباره ایران دارم که باید بگیرم. کار را یا به روشی آسان پیش می‌بریم یا به روشی دشوار.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72700" target="_blank">📅 00:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=U7u3e1dvDB7SdD7nO7chBU47vbRqDsUUj9QJ5aBbR4tmhcj0T3RVcIwchN-aev8H5lFrOaFkWHZifTxMIGUT8t8U8MHART8qrKZakDTtQ0jIdCkz1IbPAw9P3KxU-b-5nKL0JhNZTh0gu47Tb_SS9-j4eqTaqbmXCn-thhH-bm-y0ZmAXGN30IBDA_vHNsC6tHqr4WVU26FCC182e_m_iw70QdBKxbwxOhWZOemM85ECz6pp46Xxgp8p7HPhCVNDe4uky_oiw8lBsmqzQ2wj3KbR2Pu_Icnio6zApktNnA4QowOoioea-H1Jev9YmoCPbxD8m75XSnlJOfPMLi8wXpzrR3koDgCOqy0KyXz1QvoKtlBTyMN7dU7uPdGinNFlvEOK0Ojp9hrYVSWLE8uVYzdLk-Wyd4JyQmG0Wx761n3s13GUCBoYhQZwE4Y0RNkq4not644sQCTHADfj-RcABBLpXze9o9V7J9cKpD0pCvOHq6TLqm-TmDQDoZs9ZE-UuVjxrDxJPoO73mEY00ovAWwpWJ6REmzC4gldCQJoQRHavj4U6XbF65853oA9Ul977em1hXT8B2LN2_RPt0Roa0EzKK1kLff69pqj0wwvsR4Dm8UgaWFcDTGf4UpzVoDsN44OxJkMMZVCEVdg8-EZ6-DxkEEgRYChbbOIZFIyHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62816af7e.mp4?token=U7u3e1dvDB7SdD7nO7chBU47vbRqDsUUj9QJ5aBbR4tmhcj0T3RVcIwchN-aev8H5lFrOaFkWHZifTxMIGUT8t8U8MHART8qrKZakDTtQ0jIdCkz1IbPAw9P3KxU-b-5nKL0JhNZTh0gu47Tb_SS9-j4eqTaqbmXCn-thhH-bm-y0ZmAXGN30IBDA_vHNsC6tHqr4WVU26FCC182e_m_iw70QdBKxbwxOhWZOemM85ECz6pp46Xxgp8p7HPhCVNDe4uky_oiw8lBsmqzQ2wj3KbR2Pu_Icnio6zApktNnA4QowOoioea-H1Jev9YmoCPbxD8m75XSnlJOfPMLi8wXpzrR3koDgCOqy0KyXz1QvoKtlBTyMN7dU7uPdGinNFlvEOK0Ojp9hrYVSWLE8uVYzdLk-Wyd4JyQmG0Wx761n3s13GUCBoYhQZwE4Y0RNkq4not644sQCTHADfj-RcABBLpXze9o9V7J9cKpD0pCvOHq6TLqm-TmDQDoZs9ZE-UuVjxrDxJPoO73mEY00ovAWwpWJ6REmzC4gldCQJoQRHavj4U6XbF65853oA9Ul977em1hXT8B2LN2_RPt0Roa0EzKK1kLff69pqj0wwvsR4Dm8UgaWFcDTGf4UpzVoDsN44OxJkMMZVCEVdg8-EZ6-DxkEEgRYChbbOIZFIyHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، درباره ایران:
ما از همان ابتدا اعلام کرده‌ایم: ایران هرگز به بمب هسته‌ای دست نخواهد یافت؛ تمام. این موضوع، یک منافع حیاتی ملی برای ایالات متحده آمریکا محسوب می‌شود.
ما این مسئله را در جریان «عملیات پتک نیمه‌شب» (Midnight Hammer) به وضوح نشان دادیم و در «عملیات خشم عظیم» (Epic Fury) نیز آن را آشکار ساختیم.
ایران می‌خواهد با مسائلی همچون تنگه هرمز بازی درآورد؛ اما کنترل آن در دست آن‌ها نیست، بلکه در اختیار ماست.
آن‌ها عملاً هیچ چیزی به دست نیاورده‌اند؛ چرا که محاصره ما آهنین و نفوذناپذیر بوده است و ما هر شب تقریباً با همان ظرفیت‌های پیش از جنگ عمل می‌کنیم.
ما احساس می‌کنیم که در موضع بسیار قدرتمندی قرار داریم. ایران باید تصمیم درست را اتخاذ کند؛ در غیر این صورت، رئیس‌جمهور ترامپ تمامی گزینه‌های لازم را روی میز خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72699" target="_blank">📅 00:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6316faf3f3.mp4?token=N87fqbn7krG8_8ebuT0TQon6u9gW5dD7xoPdfmUH2rtqItCTmgFSW0L-DalcBVi5BqiJpBn9kEyUbC3Vwf0QLPJhaxEVOSJPhOQn-gNso5R61yIry0mjCJScbTp4L-V2aJQyQxr_iqrttWDV-6zpcTa0o05qFNtfBHLYJLNC6MTnEFocG8DnphzP-Ta_R5yTShf0gFCdyiaxpTjWrHIemr31peAfRnh04sPj7GGjEeh261GSAdQnd4BXt88chBQGj9JE1jGoRVvfJT4qE8m3Di1nowu95zGd4_vMy4QjAVyqQ9M-1q38yk78juNdjK3IX_zidsX7vfGccrhuowwjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدت زمان حضور رهبری تو جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72698" target="_blank">📅 23:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e8309253.mp4?token=CgGIxUT4h0eVW7tXD8iCif-GTqm_pXfqaadut1s3AqdMJg1_y9GuFwjWBL0dhe8vvCyoO1e5UBu7URRpoVWuEU-SrfO6R5I8SLMUmg9ycyHfdoFTSYpuJtOj-0EaP-BHim_GtjT54I4kYXKGljx_00PP_uitW7HPBXNUJYbhLU1g8CtMV0waNYwqIYJi-Gt_P8UxU3CMgFFFi97zEda0N3VGai7-G5af_3pJ4b6a0x-lvuuxbbp1iU11VzxBwn69jZDal11dwpWmB-5QH0Vo3ijXLhT9IecsaMiPe4YEyak1G0A4so7atMbbsYyUZ9v2F31UfOsR3XoYEydtnSZeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e8309253.mp4?token=CgGIxUT4h0eVW7tXD8iCif-GTqm_pXfqaadut1s3AqdMJg1_y9GuFwjWBL0dhe8vvCyoO1e5UBu7URRpoVWuEU-SrfO6R5I8SLMUmg9ycyHfdoFTSYpuJtOj-0EaP-BHim_GtjT54I4kYXKGljx_00PP_uitW7HPBXNUJYbhLU1g8CtMV0waNYwqIYJi-Gt_P8UxU3CMgFFFi97zEda0N3VGai7-G5af_3pJ4b6a0x-lvuuxbbp1iU11VzxBwn69jZDal11dwpWmB-5QH0Vo3ijXLhT9IecsaMiPe4YEyak1G0A4so7atMbbsYyUZ9v2F31UfOsR3XoYEydtnSZeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
؛
سؤال: آیا ناو «یو‌اس‌اس روزولت» قرار است جایگزین یکی از دو ناوی شود که هم‌اکنون در آنجا حضور دارند، یا اینکه قرار است سه ناو در منطقه مستقر باشند؟
هگ‌ست: سؤال بجایی است، اما من هرگز به آن پاسخ نخواهم داد.
ترامپ گزینه‌هایی در اختیار خواهد داشت؛ بگذارید این‌طور بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72697" target="_blank">📅 23:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=TBOC1z6YdY5tJlyBcB7I_dDGSys4WWfxZdFHA26bIEp-A92XoCthv0Y-ML5GZIM5G0sXq6A0s6yq0mmNTF3aKI7Qox3E29_hVs8Xcn0S4vhz7FuRV0PiUZMk2POEdsZ1zsAU3yvOdQ5AujUj86P3dym39JAiBCkPf-vqx3VH-rT-WCMUwahipqE1EIz1RD-6CPOVqbCq3TvOIb1IY_cw-rGr3jZEIXmglyVcpZ8FE_L7gU1B8KwaxrjZCyrSqFMTGuoN-tJKFkPF64-4Enq3HO-9zsyZ6wB5ZYopTBQodvJT3NZLlW6TftSi-rMh7rhnNXOatSyQ5lQHUKHcbNoosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6961bcdd.mp4?token=TBOC1z6YdY5tJlyBcB7I_dDGSys4WWfxZdFHA26bIEp-A92XoCthv0Y-ML5GZIM5G0sXq6A0s6yq0mmNTF3aKI7Qox3E29_hVs8Xcn0S4vhz7FuRV0PiUZMk2POEdsZ1zsAU3yvOdQ5AujUj86P3dym39JAiBCkPf-vqx3VH-rT-WCMUwahipqE1EIz1RD-6CPOVqbCq3TvOIb1IY_cw-rGr3jZEIXmglyVcpZ8FE_L7gU1B8KwaxrjZCyrSqFMTGuoN-tJKFkPF64-4Enq3HO-9zsyZ6wB5ZYopTBQodvJT3NZLlW6TftSi-rMh7rhnNXOatSyQ5lQHUKHcbNoosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز قبل تیک تاکرها باهم دعواشون میشه؛
چندتا دختر ریختن روی سر یه تیک تاکر به اسم ستایش و اینجوری همو کتک زدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72696" target="_blank">📅 22:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=GXAF7_kMmY84wL5WHwsXzaiupFN955hozXOs8X_hhfdVQwmETIaiU-yvtmkeJfZV5seaiz_d78JPxP7K-1gTx4paLxYaeAV5nT3tcHCKGrAuttDqXPNXUzF-wSz9-lZ38NA74R_R0XLOzLRZ5uK2-eID0TMAkHngvRBBLlVYww6MCWcIEfkhaBq4lW8jyYELtnPMa6ut2okvFOxl-2GRbme9O5id5FpOROlx7Or0IFmshH6B7K7dRxZfHI8bKD3-IfegS-WI5adz7Gv_RnTKgXZ4AKr7CnOhN84O32DMGVptXTsazYl3fJMJNA_dsfdPbUhjcnbr4kH192qMUBbwMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=GXAF7_kMmY84wL5WHwsXzaiupFN955hozXOs8X_hhfdVQwmETIaiU-yvtmkeJfZV5seaiz_d78JPxP7K-1gTx4paLxYaeAV5nT3tcHCKGrAuttDqXPNXUzF-wSz9-lZ38NA74R_R0XLOzLRZ5uK2-eID0TMAkHngvRBBLlVYww6MCWcIEfkhaBq4lW8jyYELtnPMa6ut2okvFOxl-2GRbme9O5id5FpOROlx7Or0IFmshH6B7K7dRxZfHI8bKD3-IfegS-WI5adz7Gv_RnTKgXZ4AKr7CnOhN84O32DMGVptXTsazYl3fJMJNA_dsfdPbUhjcnbr4kH192qMUBbwMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72695" target="_blank">📅 21:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af7d5f80.mp4?token=isycbWZWYXVuDVOvPuYVhqhgeh8kmYArSixG8k8ULNQbFk8HLg601mX-ioJ7eD8JaO72xTkqGGrV7LFrEz0Yks1xz8HQnRLybColpFaYP-bCB1_xNMUUCptjRydJfxvyJyrXhd2fHY4Q1BUYyKvm8S2Q3ICC9dvPXkw8qWibGCsNHK5ejXZUIQU2Kxk_NrZLFHDvzAK5XdFuZwvi3o5suUS8wwRFY9sm-1HvoYrExFl2ER-sEFFJvBv-N-ihA2PfYf78EUTXLimKpvNNAwfxqTIdFXaMEE19piANPHIETd6ZD4bu8QCG3aC0wUFQ9qSgkLQIPwmWUHx-jiUSW-gsbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بمب‌افکن راهبردی رادارگریز B-2 Spirit نیروی هوایی ایالات متحده بر فراز محل برگزاری مسابقه تیم‌های نیروی دریایی و نیروی هوایی در «کلرادو اسپرینگز» پرواز کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72694" target="_blank">📅 21:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=ksxFgIwX2PUur-HBeI0_Wu6X9uPsvx1tpehwqWydcKSMSAoSmk7gGpv93hlLGXlmyo5d04zwX5QGEn1QO6vKGq_I8PBIcxA1hs01p-4uzEdI6SOoyXt-7OGpkj1e5XhFeiuf9eKTGmbZi4tLOWRvVciPJDfxU1sO-Noo8FWFnxhmvDq0dD1rzSfPjCQsCRjLdGcqwWK87_u8rNYlBFOb4n0MjkVzysMI5-unnGX1hL6McfFN7Jat1g3n-bT8Snu0OhQyTyK-uxdvPvB8LIPrUt9dIZ9AgWR49MacH9LcnFWocq-74OAxtrbDnY9UL-uHPvSiLNulEplpIC59KRK-ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/24bef6628d.mp4?token=ksxFgIwX2PUur-HBeI0_Wu6X9uPsvx1tpehwqWydcKSMSAoSmk7gGpv93hlLGXlmyo5d04zwX5QGEn1QO6vKGq_I8PBIcxA1hs01p-4uzEdI6SOoyXt-7OGpkj1e5XhFeiuf9eKTGmbZi4tLOWRvVciPJDfxU1sO-Noo8FWFnxhmvDq0dD1rzSfPjCQsCRjLdGcqwWK87_u8rNYlBFOb4n0MjkVzysMI5-unnGX1hL6McfFN7Jat1g3n-bT8Snu0OhQyTyK-uxdvPvB8LIPrUt9dIZ9AgWR49MacH9LcnFWocq-74OAxtrbDnY9UL-uHPvSiLNulEplpIC59KRK-ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از سیلاب شدید امروز عظیمیه کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72693" target="_blank">📅 21:06 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72692" target="_blank">📅 20:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1UluoE1fIeU3E_Z8BaSNzkxCQFPtAShm8_FnGCUbt8wlv32Hjkz8KLbFhF0b-hgSVdfrGNVY0R_O4G6wSeqVMQi-G8EvOn9erXh4rnXfpJ1S_m6JYwcLv_V9V3UuvCwXrqXJ49_ClQEVm18s_FeK8U5XEL7zBPKU-dhcQmLHsJQDLlFMP6kPjFLTIqsgzPeCPviWOeInIK796cCGoidqG1T1muXRl2RTV7UhzsV6CZDuMOlKn0-RKkMQMpmnThCpLe0dsVA4uZ55RUZuBHW9JC-nisU9aiZswW0sdlSBmqEKLrhHQLpzXfriQeWBngael-VNOxG37GbJh4SA_iLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌تایمز، مقامات بریتانیایی و آمریکایی معتقدند افرادی که در نزدیکی پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford) دستگیر شده‌اند، با عملیاتی تحت حمایت ایران — که یا به سپاه پاسداران و یا به یک مرکز فرماندهی نظامی دیگر در تهران مرتبط بوده — در ارتباط بوده‌اند.
بازرسان در تلاش‌اند تا هویت فردی را که این افراد را به خدمت گرفته، شناسایی کنند؛ کسانی که یکی از مقامات آن‌ها را «افراد ساده‌لوح و بی‌خبر» توصیف کرده است.
با این حال، مقامات اذعان کرده‌اند که جزئیات مهمی از این توطئه ادعایی همچنان نامشخص است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72691" target="_blank">📅 20:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72690">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دونالد ترامپ به تمام شهروندان بزرگسال ایالات متحده وعده داد در صورتی که جمهوری‌خواهان در انتخابات مجلس‌نمایندگان و سنا پیروز شوند به آنها ۵۰۰۰دلار خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72690" target="_blank">📅 19:56 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx178UzADtcLUD8yYY8tmWr5CoDGUpaNDtYCkkY3Q_zT0hfVDBn0yzZaDrYdeUYjTtEvnDFFWSAXKF1sKnXcnboPLt14FUn7x33XkNK5YHm3pO1XmUUuXr-AF9P0PbrFwH587UuZu76fu4RCPoV8v6nh7YUIxwhQTsfhYHsRsW27vfHqMHmJBRWns1t2UmdwsNMnuedu389QEZc2SfX4AHEvv9j3mkqs41svrUUnFBh9NeytcMdJ8BKVEUlBQolnaEmAyx1Q9kB4JC9cwRXKVEIrO5i2otzkBSa73TAT5hzhHxkwrwfykkZVpdhoj3Tc6BcGSWrWVTC18ggLZmqQgGRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a49047dbc.mp4?token=H13V44NoUsl2gehIE6YjTum7zNZX6erH4BE9XkmKMfyaHyNmphbuNOMyqA09jMNV3hLd9jap0Ar35DJDNnsmu605JQA8JVcZc0pwmtQyi15bEo7Trhf7Hm8fmcnNVGnWAzE4hrX73TWmY1zoCvmIAIY5dXWIYM1N3l_WsPtua1leipeb4GoHnAH8q2bv0BhMa1PdFf6W-l_Qc-qSsqWrtm4hbQwIWvEra5hmZelSRoEE07JB-RkYVRb5rdHMlDRG0IWPAWx3xvsSg-lvRBVvz2zdkSDMtxVrWJIoj4B_D9bVvBDXpRtuh-LU81c0zSXVJ5vMxwR01YCY4LowCoLcx178UzADtcLUD8yYY8tmWr5CoDGUpaNDtYCkkY3Q_zT0hfVDBn0yzZaDrYdeUYjTtEvnDFFWSAXKF1sKnXcnboPLt14FUn7x33XkNK5YHm3pO1XmUUuXr-AF9P0PbrFwH587UuZu76fu4RCPoV8v6nh7YUIxwhQTsfhYHsRsW27vfHqMHmJBRWns1t2UmdwsNMnuedu389QEZc2SfX4AHEvv9j3mkqs41svrUUnFBh9NeytcMdJ8BKVEUlBQolnaEmAyx1Q9kB4JC9cwRXKVEIrO5i2otzkBSa73TAT5hzhHxkwrwfykkZVpdhoj3Tc6BcGSWrWVTC18ggLZmqQgGRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
مرا بفرستید تا با «کت‌قرمزها» (نیروهای بریتانیا) بجنگم.
مرا بفرستید تا با کمونیست‌ها بجنگم.
مرا بفرستید تا با نازی‌ها بجنگم.
مرا بفرستید تا با اسلام‌گرایان بجنگم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72689" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc7b08156.mp4?token=YfVEQCNM6FBPsKivWEihhvqNX6DSf0CmKgzXcVE5yCZoLIsDQT1dT3NPBNRqDinjfyNC3Phx69peiO4kWjb3Tu6E8hOwTbRKwjmlegz19b3qVNRVboqnL80XdTniAtijpPSf07Acqe2pC_Fbeh417f7BE55C0p7szdcEnvGfoiPJd6LE85KR-1xae1TWdBQdZ55zakyTD7mtpHBGl4mQg6TM3g4LslLJxqDfwqK1LZ6up-t8y1YGY2FWcP7WdxN5ntlWsweo3_3Qztogqbqy4VFuI4K25Zx4dSWmW9zSYui4xXuAcqdwDA6XjufzEkLvIOOAnnm7RVb3uzFhbTvzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ:
اطلاعات نادرست، اطلاعات گمراه‌کننده و تبلیغات عامدانه‌ی بسیاری پیرامون ناو «یو‌اس‌اس آبراهام لینکلن» وجود داشت، اما ۸۰ درصد از کارکنان آن گروه ضربتِ ناو هواپیمابر، برای تمدید خدمت خود اعلام آمادگی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72688" target="_blank">📅 19:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee4b7ed20.mp4?token=QxL_eBx2Zz46z8_YtOiU9V3yjURNbTJXqOocetKl5RUQQOtUukelbmpZ9HZ9OScXfgwNHqSa1MQ8YNHRAHIAKXOWJ6QFMqXQyMrYII2LWWWMHbPYwYHDdyIQf0d6ZOtrdUmql04ybqM3Jlgf_6HPPcvDEB6CUAMQSoqc2735kPua5PpiZPp_qCjlj9FxONe5vwLiM56WChMdRNtISSvVq4BJnH3ZDIzdRxrUIhFJLWqmuXPSwRTnA1N0emd6w2KTgVljB8WNDC3zQj8D4wAJPnOrGrp5fVsPepfWuY5M64TseKRwkMS9k_gda_S7LNfwVlTGEgxAAUpVczK9eVYTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست لحن و رفتار ترامپ رو تقلید کرد و چیزی رو که ترامپ هنگام پیشنهاد این سمت به او گفته بود بازگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72687" target="_blank">📅 18:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=jLdXLalTwkh5jgjapsVI2Kb6OzEAYeVbD81msa8F8yrEKvXQqSabFJiVMqBV_zLttwUyXFeODrp40_I3qrEISyMC-t4CAB3B1uWkvFLVvkM6kZ5QM0AKUOA-n_KCZpsERicOSnzhFQKhnrXrEjBBfsDM2DHDsVy4kMVA_XSEBO486ra2MaPVS9u7mkJg4IHgBwoz0_wtsdc2IWitFFE8BUlUkR7nnpgpQpAlKafylO3hDxceRFvLH_pZK17qatZLzekfcn46FlmiXT_mnlxZ6Ec21YOOAbMj8T7GEJmDq--qdckVslTXm2jnDWbu6wtDJYvxRlh_ti7LASduCrdm_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7350ab9.mp4?token=jLdXLalTwkh5jgjapsVI2Kb6OzEAYeVbD81msa8F8yrEKvXQqSabFJiVMqBV_zLttwUyXFeODrp40_I3qrEISyMC-t4CAB3B1uWkvFLVvkM6kZ5QM0AKUOA-n_KCZpsERicOSnzhFQKhnrXrEjBBfsDM2DHDsVy4kMVA_XSEBO486ra2MaPVS9u7mkJg4IHgBwoz0_wtsdc2IWitFFE8BUlUkR7nnpgpQpAlKafylO3hDxceRFvLH_pZK17qatZLzekfcn46FlmiXT_mnlxZ6Ec21YOOAbMj8T7GEJmDq--qdckVslTXm2jnDWbu6wtDJYvxRlh_ti7LASduCrdm_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آب‌و‌هوای قم رو ببینید
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72685" target="_blank">📅 18:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/po2b2gf0qMuyYpObaeOByn_gzPlDu9at-8n4a7hFPBBhwgGpZ1rW-st7n6zyLJ030qCrrNQVkWbAj4HRdIBjq42ebZ6oASRAqezakZ-oT5B6NE8Op3IemTbnUii5-z91QBu2hh0K9pUqAY8UpEi4z2c84fMOk7ClCIDtkZmBcpX3jVyoSToF7tnCoNhAMSPBcw6K12fEJfLYdIhdQDizpahOXADNl5Mw8VgUZNO76KY7dr2d3FgrFY1pfkLfWBZInDPjseuuuQXtixOVBj-L114nQ8fcuUfT1gZsDpm5cKrQa2PK04TrehscsHHh6iIUl5inL_t_gaTWN-BG8MLVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4GFBCOvTAfQfvN1oGux-0QDOCkrO8E0EkP9xDjqAzF9vEPAtNhspvzAoxyoarzBCbkPaeyB75bwWUda_U_O1DG7EKHM6w__iIC_2xSELmBsQKGeDKySuqTyuFNWFWEN0Sl1rJwxqJb4y9oh94WQWL054EMwQ0y9P00k81E1fAN-NNdvDOLU0wTDRbu0QhYeCLXnazOZLczPE24xAUgh1sZo99gzH81-8gc9tlhaiskvNW11ccaAWTIXi1UaqDJrsBO354SsLF0_wasUmY7zULZsafVnyptg0boN7uRGfpUSuwV3MTMU8d7sGfLKXTNRaZRXecZ_xMyijOvZItIsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrTrogMCy5Z2Tc96hLcdimwYR82jko1heQ3E8gOoyHvxJFTnNisEE9hxZ7UNuXiKJQjjS5yqALNN0j0MIQJ0AWezLqCgeb4wGzEdyDbR_OOsIfHS5k3CPnuK2nMEApsWW7rpeIFx9NhBXaNbbhHdVGxKpSTEwDCmqiSvr6A8W1dYHIS5a3k6cppCx_B56NeYLKrkD7juzPQCc5kf-eYCfvaKxjx61vkPLm3Un4UaeT9_QqKako7XjVf5xVXWzSWgSTV1f-G3bXn9V3c2YUQ9mxN8PdLw-1PCqDQMOglRfDqQ1PuqC1dm0rL4gXHJDXztzfbmoBa5JbjE8a8BB1PivA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایلیا هاشمی:
ساعت ۱۶:۳۵ شنبه؛ ابتدا صدای جنگنده در قشم شنیده شد و سپس یک جسم مشابه با بدنه موشک، داخل شهرک بوستان قشم
سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72682" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72681" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2rdh4dE8Q4qb_skQvH6KkeKDyap03fVe51IinN6CMrKwdpkozjsuOIQvnMpbsStjIGCEVnE8oMcaLOkBBD4Sf-0-X41IgJJkXnnasjepKZNFrIRk63x94HHRgt79vu492wRnWtcxnklWuPxBvZZxtVAsYuEfun4F0A4-NaBsNZRK7yXKX287gNJ-scyMnrEqzjPwAk1SGCSbVD8wBh77-4tLvmJ0lHR-CZKiO6T0wr60Bk7e3giPJgzVqaQzKiAtq1S0Wz9e83TU5kL5Jh4FZbiczLeoYWqMAzpf9dZTorBXYQxjWEJHs0pp4aMOUQnXfDq7N7owE_CbSDA38lIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز انگلیس
🆚
کرواسی را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
انگلیس: ۳ برد، ۲ شکست و ۱۳ گل زده
کرواسی: ۳ برد، ۲ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72680" target="_blank">📅 17:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323337b42.mp4?token=Mt2I6NRUexHkIdBFHCHhN3HJzTaC0hsX_5_Kmv2EjBxs58MQMsZKAbul4OHbXPRhz46sLuTuHuEntNrMjyPrLFcZPT3kP4jPnfnJIyxxKnhnynCcRrR7FgGHeeCQLVR3Nqfh-OOqkK8vD7AyQpx9_FE8PMaQfhXm1XYEeFvZOynGKkj571ZqtuvhsHrPPqpBpTLS3yR3JtGU4L-xn0vaDhPurOlRGl6uSwMJv0SXRapbIVZj_2YY_WtMx-EP9-Kpa8VP9tuw2fe_26sQCq1nF5X0Arxl9xgEuGnlsBzHuv-4IBHyqT79FNtqE04rh588crafHj5I9iRaZ4mvfEg_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن مرجانی، رئیس انجمن صنفی تولیدکنندگان شیرآلات ایران:
اگر این وضعیت اقتصادی دو ماه دیگ ادامه پیدا کنه
کل کارخانه‌های شیرآلات کاملا تعطیل میشن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72679" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ناو هواپیمابر USS George Washington  در حال انجام عملیات پرواز در آب‌های منطقه در خاورمیانه است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72678" target="_blank">📅 17:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0fbd5c19.mp4?token=AsWpsfs9GwRn9dc_AkWzTsikuIk0uGLZI8WCWe7XUjK7j_TUTxCX6W96PJ_ZO3qp4h1aYJbUCNY3sFFyXaJdJ2jMgwuxd0985fhYjI7lV8DGVFC37B-6ybmUjJAwXOWUVVrHSUjK2kK2al6DReofp7e0FGFaIW-zFVoP5Ke3wpaJVPWSZCSAjkfQaDGXFxPm_M5lyIJN0J1ZmbomCWiwKd6LO_H2jKZ_Xnt82VmqdX0usObbIe0imZ-gbEpR4CCg0FRwRHePrHQ3iNoMmj7hNRN2HpVqx0i_lQgw4ivBgpdsbCMhnMiaK5ZB4fsumKcdKTR42c8UY5cdNfU9bTkLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
برای نخستین بار در تاریخ — از زمان آغاز استخراج و صدور نفت(ایران) — آن‌ها در هفته جاری هیچ نفتی روی آب (در حال حمل‌ونقل دریایی) نخواهند داشت.
آن‌ها هیچ درآمدی نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72677" target="_blank">📅 16:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72676" target="_blank">📅 16:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yt903JpS_534U3xKNaW3Uwc6fRZm-sbvS8ruzkCuw8GtvH-uE2TElIKLLKNwNwr-fsW_rMFusMa5r78GIRREhv49DfHpMKkv7r8VN6DO1VNU6UbPm8i9_SjLuSlDwxN8mD6DSfIfQH326kQDuK_13aHnEL0BgrlwN7shZs4nC1v5LFVlsa-i4bDj1CDfRqly1TEWAxTwKt8FTFysMkweTH0V__weA1dRAcovdvluhP0KaU6K75rN-vo6v02N4c1Bfi2sCyFzJJZUd5iWEFnGW6a8a9y5Nw0VNCmcXbsLEytU7HqT2QTSMXeNLZRkypc9eTqM4O92mqNMp4bI1Wxylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf54-rj3-KeMPECQFXJq8wurCblZtW0sATzB5NbTmIJqKIvbnLAEY0Tuz4YCq0Xyr-APBKlsfM9_0jiflb9lM9vSUhgCYV1xh7tcU1FaruHnB02O9X9L0D-cDgJwKTgpViqB5fQMe7gStGo4YLbA-GRjEfp1UoHT4m9BIPMxpX2fETnffl3JpLKeBjGToyZoaPnGwQdspTeFC8xCIclRVUj7RAMHLwcna5NZ3DpBCvZL-vDYChxOaWKF3GoOzK4Dr68viRJZqWZ7n3Aj-3Rxom-1-haeTzQukMsuTm6JiCITjPNTLtr1lUzTUO5bmyEojbdbR7XdYry2WDYMz-rPbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمونه کار:)
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72674" target="_blank">📅 16:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bq3tjWowjKjdSbQRf0VcWZDSGtkoNM6eodDjmsLKsrHHtiNkGNeKcXquGBJfEwwt9T0Lrofnr-azgVQhycOCCdOOyUZGRjCoASOGcAmouGidJ91e_t97ycXdd9VAt_jF0YNKnMQeAY7rFtT73PRRvZgCe5rNS-ZVGn7DCKgVctluZG7_cHhVm9Vmj5Tn2W2haPo0mG_GYJRI0QruyQyF6JMGviPb48UK6reluvQQqteODyvtYGd4hfvhED2PJPkfjycSMnfwK8E4102dAMOPKifuaoeZvuWm3UzSWWul1vjuD4AqfkcjbKcSi4Kcmx4cF9dYb8Us7bPRFC2HnJl_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به دانشکده 05 کرمان
✌️
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72673" target="_blank">📅 16:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72672">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#فوری
؛نتایج اولیه کنکور ۱۴۰۵ اعلام شد!
با ورود به پنل شخصی خود در سایت سنجش میتونید کارنامتون رو مشاهده کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72672" target="_blank">📅 15:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72671">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=TQ-oSdU1wsoYvSYiJKrDrptBdcNhmGTw79AjnW2nOkvf7MFT-oIIHugesbg1iXbFw7evuq55xB5DkmuK3HYKRET1DlQluFe9YLHS4a3hNOuWn9lvvBE-1EU_ziiuzBTpVSaPDmz_CEiV8jiv2a5aGUtm4OyM1hZnDDG9_jHxImGdSKJSbHLhZznqynAliUJb5FGQPvovERqrRs-aOARIGv6wAviJhJq07ka0tSoB9xYLvO9sMSLlpeeY1TvVvIkP8cjmNevBLcuD06t--oiGSc8J5uiI-xueZrOJ6yz50kdBlxno1wqnNAFjJzh6jshvmtTpRFTt5S8Eeu-O8bmb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c967ea5781.mp4?token=TQ-oSdU1wsoYvSYiJKrDrptBdcNhmGTw79AjnW2nOkvf7MFT-oIIHugesbg1iXbFw7evuq55xB5DkmuK3HYKRET1DlQluFe9YLHS4a3hNOuWn9lvvBE-1EU_ziiuzBTpVSaPDmz_CEiV8jiv2a5aGUtm4OyM1hZnDDG9_jHxImGdSKJSbHLhZznqynAliUJb5FGQPvovERqrRs-aOARIGv6wAviJhJq07ka0tSoB9xYLvO9sMSLlpeeY1TvVvIkP8cjmNevBLcuD06t--oiGSc8J5uiI-xueZrOJ6yz50kdBlxno1wqnNAFjJzh6jshvmtTpRFTt5S8Eeu-O8bmb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ما از این مناقشه با ایران عبور خواهیم کرد. به گمانم عرضه نفت بهبود خواهد یافت و قیمت‌ها به‌مراتب پایین‌تر خواهند آمد.
روند افزایش دستمزدها ادامه خواهد داشت، چرا که شاهد رنسانس (احیای) بخش تولید هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72671" target="_blank">📅 15:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای انفجاری از سمت دریا در قشم شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72670" target="_blank">📅 15:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=lom7jjzitlCZEsU_2hqukOGakgG9pnNt7jcyk06fV1oK04JH_gY8KY3Rq6jot0T3Lj2B_Wl-3jKQaJXFBuCTZ-JniBiXMHpCuW8Z6FPXJhag0M06iAYvmYQySj50sPFoGl6vNH0JK3QPcu2XMhQUVpbMgd6orqBdM8ZD_PZI3h7c7otZvN5TVjkAyr75ll2r05No4B72XQssx-gR_Gx17jZhjMT0xDGMzRl4L51InnFEehmdg4yHw7x2fWLHs3pVicZfh-o9dNEfYpni4H4FoQr8Z7Nw0WygjgXh2C7lGjLvudKkREhVN1aZ3wdVIhGbxUC3BntrvzaAE_xwddy3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fafdeb0b.mp4?token=lom7jjzitlCZEsU_2hqukOGakgG9pnNt7jcyk06fV1oK04JH_gY8KY3Rq6jot0T3Lj2B_Wl-3jKQaJXFBuCTZ-JniBiXMHpCuW8Z6FPXJhag0M06iAYvmYQySj50sPFoGl6vNH0JK3QPcu2XMhQUVpbMgd6orqBdM8ZD_PZI3h7c7otZvN5TVjkAyr75ll2r05No4B72XQssx-gR_Gx17jZhjMT0xDGMzRl4L51InnFEehmdg4yHw7x2fWLHs3pVicZfh-o9dNEfYpni4H4FoQr8Z7Nw0WygjgXh2C7lGjLvudKkREhVN1aZ3wdVIhGbxUC3BntrvzaAE_xwddy3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واژگونی ترسناک کمپرسی بر اثر ترمز بریدن در کازرون
💔
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72669" target="_blank">📅 14:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پشماتون بریزه!
ایران‌اینترنشنال در گزارشی درباره مهدی نادری جهرمی، رئیس هیئت‌مدیره شرکت تهران‌اینترنت و مؤسس و مالک اپلیکیشن هف‌هشتاد، ادعاهایی جنجالی درباره ارتباط او با شبکه‌ای مرتبط با موساد مطرح کرده است.
نادری جهرمی با نمایش چهره‌ای کاملاً همسو با جمهوری اسلامی و حضور در ساختارهای اقتصادی و تجاری، به تدریج به موقعیت‌های حساس دسترسی پیدا کرده است.
ارتباطات و فعالیت‌های او در حوزه‌های بانکی و مخابراتی، در اختیار شبکه‌ای قرار گرفته که با عملیات موساد در ایران مرتبط بوده است؛ از جمله انتقال اطلاعات، شنود و نقش در برخی عملیات اسرائیل در ایران.
این گزارش بر پایه اسناد تجاری و قضایی، مکاتبات بانکی، قراردادهای شرکتی و روایت فردی با نام «کیا» تهیه شده که ایران‌اینترنشنال او را مأمور سابق موساد معرفی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72668" target="_blank">📅 14:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4hwdBQijZ3FUHcpK3Km6fJKmheEgAmL8eaCK7QwtDi3daqYw3rmPBysXW6opcKY6uf6x6GD-P9Xe9RPsNXXeCQ07X-QMbViFS9x9oakd25vhkVX0rDhcKzu4K8V3MXIc9KNYm90gtigQFZ1Y6FQ6pC4Fj8an6b2fTCAIGO0ZHKAbhOW1B6Xh8zYNvYa4EZIX3CYHkAcpR-NlqPLX40Af4PDFxyn-vt-xTxCbKGcepyFa9EzXD1UdrxU5cSUunQ2b2U36Vu9ivoULR1c4z6yCUcvCOsaA_4jgeIfsEUDyx-LkufZD9Q-_huen-MiHDQ6y7s3Tqrx4LJP0453m761JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=SRr149ZVpAj_q5PnEUrcDIkDqV390Ag_JgZw99kIkgRuCIEkRsNmo11ttb4-DtF9ieY3bgXhCwBj18gzcR-KC7aseoVdxP6nsex3xyn6NnzqoTyr3hrdkY2_9DU05DsnS02yd3mO1TaT3bu-4HXQnEt_2EoSiPVzz1_v8XoHXZeMrhsdMTFF7cbOTtI9UhkY-_un4teE7oPgBh6UHtdiWRSRIKwLjtfxebS_aqvJwmLEvecF_beG5k7UN2EgNzdruW4a3qLRf1kqWSe4dd4fciEWdjP2QFKzDfXNUjMEyrF0eAz0U6qS4293FyyMmQ2E2Bd_fyv1QB5FNGLpOqVrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1908d250d4.mp4?token=SRr149ZVpAj_q5PnEUrcDIkDqV390Ag_JgZw99kIkgRuCIEkRsNmo11ttb4-DtF9ieY3bgXhCwBj18gzcR-KC7aseoVdxP6nsex3xyn6NnzqoTyr3hrdkY2_9DU05DsnS02yd3mO1TaT3bu-4HXQnEt_2EoSiPVzz1_v8XoHXZeMrhsdMTFF7cbOTtI9UhkY-_un4teE7oPgBh6UHtdiWRSRIKwLjtfxebS_aqvJwmLEvecF_beG5k7UN2EgNzdruW4a3qLRf1kqWSe4dd4fciEWdjP2QFKzDfXNUjMEyrF0eAz0U6qS4293FyyMmQ2E2Bd_fyv1QB5FNGLpOqVrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هزاران دانش‌آموز دبیرستانی فرانسوی به دلیل کمبود معلم، ازدحام بیش از حد و ساختمان‌های در حال فروریختن، مدارس سراسر کشور را محاصره کردند.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72665" target="_blank">📅 13:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72661">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=Zupepg1B0NbAvnYJIoB-OZmhgTRBvyPuLoUgFB50TtEUSS56gCm1HkTRwtE5Wb5SjWzb3Lp2qNhQ53lMzl8RLR1niv_lEPpC1uEARbFOaqKQZ32t_s-dtIIRCbHRuHUqWM3igivYv38IKyrVi6Waf-cKECp99hB57qmI-FXf_YJtxYD06MP742PHUyzqH8pqOQCwA9WwnXLjoPBBti1-lMVsA7uxdei2A5UlScP4XklvDPI2HL0BPiGORQKfNKDrPnWmg5evlQe4SLOKYkP2zhNvt4qRHy9bMvDwy8CzfQU4GD-7lTqmRTtxQAEG58eNh1EXKvGz7beVc3QGLgu-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b9ce8d805.mp4?token=Zupepg1B0NbAvnYJIoB-OZmhgTRBvyPuLoUgFB50TtEUSS56gCm1HkTRwtE5Wb5SjWzb3Lp2qNhQ53lMzl8RLR1niv_lEPpC1uEARbFOaqKQZ32t_s-dtIIRCbHRuHUqWM3igivYv38IKyrVi6Waf-cKECp99hB57qmI-FXf_YJtxYD06MP742PHUyzqH8pqOQCwA9WwnXLjoPBBti1-lMVsA7uxdei2A5UlScP4XklvDPI2HL0BPiGORQKfNKDrPnWmg5evlQe4SLOKYkP2zhNvt4qRHy9bMvDwy8CzfQU4GD-7lTqmRTtxQAEG58eNh1EXKvGz7beVc3QGLgu-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از انبارهای نفتی آرامکو در ریاض که هدف حملات موشکی حوثی های یمن قرار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72661" target="_blank">📅 12:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72659">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKeLCJ2VdDo8CIRoBX__303ZJ9H62DmAzeMMLk-ZOymBH2jVtj8acsqcxvpBShAIKf8auBJqDxZAkEuzVDkHvCGqW0EUGdd2e6Ssq0--vTqcCVdJDv1AdPxGsc4nOsro_h-n1eSaxQwXylQ8Jf_nWIx8_FSXeys5uiMLG_kgbLwgc8DzYzIbB4n7FCUefkYGTn74AU_DExS7DaPu3rSGmQMHxMssli0S9iwh_rEqy_vkst_PZmPLuHpEY9nafQol3U__7CoqL8_TKagvohqlyrwI8EKNR-G84DLq-i46TvtA-ygItgHsQ5jKBBpkJyGcCp43z95z2ZpLDnv3VJrBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=uw9wZBda1cdJjBHoazNWgRHazX5schVFngVMXH6RMAhkQUqkY_oA16vho3Ei0iDdUDxyLjYqUztGfNMQXGR7T2yTaKa55eeMRmLm0Nq7Eqz22cLErOXLT-VBKLBDQCTebbxn1SHECjqLEOoijgx2Ix6pP4nheuBBPs4Tth_CTiPAycOvqE5PwYlIXIwvY8pW7fM4QCyV-fwzJdkFh7tzxsKpJio0ip8sL8g0AexMYr4jDdIPORaDy12Cb6GGy6dmKZJavsp3WWC0BmJVyOqfLLGEA1LLotvxWuicH3rRQPmpa7CM7C1SBdCumZQLQ3sPujzie5bsp6uak7dHaFV2GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=uw9wZBda1cdJjBHoazNWgRHazX5schVFngVMXH6RMAhkQUqkY_oA16vho3Ei0iDdUDxyLjYqUztGfNMQXGR7T2yTaKa55eeMRmLm0Nq7Eqz22cLErOXLT-VBKLBDQCTebbxn1SHECjqLEOoijgx2Ix6pP4nheuBBPs4Tth_CTiPAycOvqE5PwYlIXIwvY8pW7fM4QCyV-fwzJdkFh7tzxsKpJio0ip8sL8g0AexMYr4jDdIPORaDy12Cb6GGy6dmKZJavsp3WWC0BmJVyOqfLLGEA1LLotvxWuicH3rRQPmpa7CM7C1SBdCumZQLQ3sPujzie5bsp6uak7dHaFV2GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی جنوبی ایالات متحده فیلمی از عملیات شناورهای جنگی آمریکایی Saronic Corsair نیروی دریایی ایالات متحده در پایگاه دریایی گوانتانامو بی، کوبا منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72659" target="_blank">📅 12:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72658">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:
باید با چه کسی طرف شوم.
کسی نیست که بتونم باهاش درباره ایران تعامل کنم. هیچ‌کس نمیخواد رئیس‌جمهور بشه.
من می‌پرسم: «در ایران با چه کسی صحبت کنم؟» تق‌تق(در میزنم)...اما کسی خونه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72658" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72657">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72657" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72656">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIPf2A4Fs5QECXZv1Ba4KhW1LXetLsQUQ03htoqA_LikdHMh3jtW-0YYsXeKBgnLypjHoNTHkqLqKmYYK2n3I84ggHyx8Mk1cZY1iuDswk-hysItQp2d0rFAlxnJargSkuCPdRewi85m2iq_x5ke_b445Ci2UsOoke0UDgj2GGdUDKHBp_nVBuGkvXJuPH1-HjN4smyKijhhcT4-ptGa_SDG5Jakve7ufuHd90M6Lgj-WZlJeMVFlLrjQTIp0egGvtvE-IuV0v5BCkScpoWAJtAer7KYr213lg_qXk73dqBt9SRn2orc6RoZwSY912ItI5ef8fEiReGyTgE0SV9a9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
کرواسی
چک
🆚
اسپانیا
اسلوونی
🆚
سوئیس
لومتزانه
🆚
اینتر
یووه استابیا
🆚
لاتزیو
برزیل
🆚
هند
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72656" target="_blank">📅 11:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=QQhb5MYsL-FpkeFoqHw4hyT1rMzCE2NU9kOlOzXTjYUe9Z56fd-MbouZlHXLLhiVD8K6lg2lNlb_LoF_wohBByQndax0o7u5YNilDrTtNy8ZfALZ1zODzF0zi6CXDv1Err8naRQJNRg8Sp8ATtwa8Cxuch1SCz7jW_ODGLGAA5K1TGa1_vvAvQQDOQ96S9QHahnEzzilSlmpLAZ9WMoN2StXZ4O1sDYei6myI1l3fwCPChgGAdoNu8q8QKbtcyQYbjX-nCHpebBaB-bOONfV-H6yb2cShMvdMlNSKdg8-BSXBzR5XwqvxC0lA7_7jIpNZg0Qnl5q58IggkYaneH1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533100ff9.mp4?token=QQhb5MYsL-FpkeFoqHw4hyT1rMzCE2NU9kOlOzXTjYUe9Z56fd-MbouZlHXLLhiVD8K6lg2lNlb_LoF_wohBByQndax0o7u5YNilDrTtNy8ZfALZ1zODzF0zi6CXDv1Err8naRQJNRg8Sp8ATtwa8Cxuch1SCz7jW_ODGLGAA5K1TGa1_vvAvQQDOQ96S9QHahnEzzilSlmpLAZ9WMoN2StXZ4O1sDYei6myI1l3fwCPChgGAdoNu8q8QKbtcyQYbjX-nCHpebBaB-bOONfV-H6yb2cShMvdMlNSKdg8-BSXBzR5XwqvxC0lA7_7jIpNZg0Qnl5q58IggkYaneH1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
گروهی از افراد را دیدم با عنوان «هم‌جنس‌گرایان حامی فلسطین». بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها می‌کنند که باورتان نمی‌شود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72655" target="_blank">📅 11:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72654" target="_blank">📅 10:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stqPf87v6GBzJireAf7PLb0tBfMGxelhDr1iF2ZsjWT2cI6o1kOULgUspxdCxbJE4yXtiEwRlhz_z9g2xMgwVrvZOKOsKZtgytvQZVsDXf1cHgWyWjajm8Ck6b-JedBpiW1lJ4Qt_p5ChM0WU5V8u_AdRrExIdfcfq9Fg4ZJtt_bhF2ox0hIvF92dzb42RIQrUUy8V5yQYY5gpV6NUxtmpjojrb1eFd5asDLfhtheXX82mSPESEtDayJqeBC4ruGlwR9fQ4hYLqgHdRESKwIwnKfH6LTkUkm11K1YI6yLmtC3H38l5pSdyGipgUEdZGeWg3WeKdVec5TA_Z1N56lNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی نفرات برتر آزمون سراسری ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72653" target="_blank">📅 10:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتایج کنکور سراسری برای عموم کنکوری ها فردا میاد!!
انتخاب رشته از دوشنبه ۱۳ مهر ماه تا ۱۶ مهر ماه ادامه خواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72652" target="_blank">📅 10:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWTIpx0e18sfl2Fjeu_fWE11H9YrACtK8WweKywy8Xm9DOrWJtRdwbsyzcWJFzJPv-3LFoFViX7xg-viZmIv5rq94a0FBxT0J-2LFhq3treUVhyum47su1tUkxFPvMdfVBmh9OkCFh3VzdkiUaHw-YatJWTxA9F-v5eZ9pKnyn3zcDFz5oGwUp3hGba0H_PTbpFgy7Y9_fYttb0mpFt2zR7H9JItDdpa7ByLvNnqnqJaiXsIuDDzJ4wm-eak_lSagbi9V5nFUtOom7319TCvn0okspyQIoz_XPkR9YPfvvcVe7KWn7V32Y1lhPpC5enVc4wSFhn0CsaEKFEch6GqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست خبری سنجش تا دقایقی دیگر!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72651" target="_blank">📅 10:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lrt1m8w1vMnZki1Nl0bn0HqMhirFHWJlaEuY75BMVPtt9D_lIR3pSmCra0RKFQ73p2g2omDmvk1TkSGltbhJ4GCU4VZQO2mHtXj-GI6hyU-x7kmnGUDVA-RHW8OrJbN_gpGDhG0t5gR45g63r__eLE9A5Dc0xO90U66WJoKeCaSDNap7awpKIEJgeaEyBbLMgc2kFd-luq8WBDMejM9l4FtOyTqXSOgm6xzqbqRgS96mrGJ1B7DFqxeWf5wJXfByGkj2xYsb8TpPGC17azkuDSikmIAZXtgXa5S9f9a2MDAB9htGzn9J9In4anB7P7uN99CMjg4n_jckoDqj3Zeifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛ اکسیوس به نقل از سه مقام آمریکایی:
مقامات ارشد کابینه ایالات متحده در «کمپ دیوید» مریلند گرد هم آمدند تا درباره گام‌های بعدی در قبال ایران و انصارالله گفتگو کنند.
یک مقام آمریکایی اظهار داشت که در این جلسه تصمیماتی اتخاذ شد یا دست‌کم بحث‌های عمیقی پیرامون این موضوعات صورت گرفت.
ریاست این نشست بر عهده «جی. دی. ونس»، معاون رئیس‌جمهور بود.
«مارکو روبیو» (وزیر امور خارجه)، «پیت هگسث» (وزیر جنگ)، ژنرال «دن کین» (رئیس ستاد مشترک ارتش)، «جان رتکلیف» (رئیس سیا) و «استیو ویتکاف» (نماینده ویژه در امور خاورمیانه) نیز در این جلسه حضور داشتند.
آخرین باری که نشستی مشابه برگزار شد، به ژوئن ۲۰۲۵ و پیش از آغاز «جنگ دوازده‌روزه» توسط اسرائیل بازمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72650" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=WitqTWEav6-XRynDx14Bc12ci0pBg7y_5Hqcv8vFC7YGAj2XH7ahyZLzQO7_wSNK5Fcu9e4a7jDwP14mFWdwzoxg8UmonHjzQ4_2da9RWlzSdy2jCDcGNmhiQdIo4MOZwXzbTx4mSh4LkQbRSnZsZndfOZ4Cs61VzFMm8z5ycjIgcgSy6IwJ_rc8_8rCIx_qtl4MiUVfImZtWdVUwSe8bsnmYWPv5hgeSdXrATMdzUz63QP-cVL8xs0Bor3dLm4q0G6wguSwHuVxK7n5ZEAqVi74-NhEJYk1XKQ90w03pfBo0Gsz1ZeDS0o8d8LndPdm9V808PBAF_fkmIH7maknNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f04d52dbe.mp4?token=WitqTWEav6-XRynDx14Bc12ci0pBg7y_5Hqcv8vFC7YGAj2XH7ahyZLzQO7_wSNK5Fcu9e4a7jDwP14mFWdwzoxg8UmonHjzQ4_2da9RWlzSdy2jCDcGNmhiQdIo4MOZwXzbTx4mSh4LkQbRSnZsZndfOZ4Cs61VzFMm8z5ycjIgcgSy6IwJ_rc8_8rCIx_qtl4MiUVfImZtWdVUwSe8bsnmYWPv5hgeSdXrATMdzUz63QP-cVL8xs0Bor3dLm4q0G6wguSwHuVxK7n5ZEAqVi74-NhEJYk1XKQ90w03pfBo0Gsz1ZeDS0o8d8LndPdm9V808PBAF_fkmIH7maknNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ربات‌های چینی با لباس‌های سنتی عربستان، برای شهردار ریاض و سفیر چین رقص محلی اجرا می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72649" target="_blank">📅 09:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmlvi8KceK9F4y9m5IS7x2Bo2bNAc1ZR-kahF8f1zhQrWH-MmjmWu9y1KCthdjmy_6fHoi3gdHs935Zbj6YxbXmN3uuYgzowqJdOlQ7RQstl5bAkklyGYrLyIRuW72oOw-TvZT3VjVpvSpWKxl0vvPfGrKEq2x8vz9RLvgLxWrzmPnE_qOQtwuuCyQzjGZvhAo7BZiMwn0VxykCcpAimuZnZjbMl2rTyuhBad4bIPEjvrOVvWp538o0B6tfD8cl3BwwYENJXerA_54J58nxxHo3N98x9gdkmuFOQlPbWBNb2LIIwtdxdmhI89b9aJ6PUQj1WBgXDFQw13mtRZNXOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «ای‌بی‌سی نیوز»، کمک‌خلبان شرکت «فلای‌دبی» که به خلبان حمله کرد و قصد داشت پرواز شماره ۱۰۷۳ این شرکت به مقصد اسرائیل را ساقط کند، «همام الحمامی»، تبعه ۲۹ ساله اهل عمان شناسایی شده است؛ او اذعان کرده که قصد داشته هواپیما را در اسرائیل سرنگون کند.
الحمامی در سال ۲۰۲۴، در دوران آموزش در شرکت «عمان‌ایر»، پس از کشف مطالب افراط‌گرایانه نزد وی، از پرواز تعلیق شده بود اما همچنان در سمتی اداری به همکاری با این شرکت هواپیمایی ادامه داد.
بازرسان در حال بررسی چگونگی صدور مجوز پرواز برای او در شرکت «فلای‌دبی» و تعیین وی برای مسیر پروازی اسرائیل هستند.
الحمامی با بازرسان در امارات متحده عربی همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72648" target="_blank">📅 07:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72647">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHKrlO1cb7fdcEYXThPwkHy-svslwuiu01FBsUNlInXxqWPdeiWLxLl9s17fgU_c8HbtvHNicpWVN0_dR0qLpUibPR_jNglkBMCq3SrKkeGazGyOLQ-O9CvO5298uvbYNlxfcONij9XJV33oqSQUjF1a9acFTQ4t2zoPSDacTWu3owNchvN66Cr7dGwj2qoli6NEEdyycuJ4Tbp0QmFTVV4VPIMycIqQn2rXYHZesempBVcOlUtdyEmSOzi8fxl0qiHp1t7ckjuWMrMCG-WZhi2oKPcdQF8EEpB26FBVNAuvsxw7zo4C-DMkuVBOAU6GgdcAcY9Ifn_AQ9icU4mZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟  ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛ اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.  @News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72647" target="_blank">📅 06:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72646">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72646" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72645">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOET-VznaovDItIRYHux38JrA8Qt4_NRBjFFWA2LhMSji4xdWzRbOb5zGdhKV9b4QiFzGQ-0lCAKTKurh_P2Bc5sHG5QmnLgOht7qHaRUyF8DBava5XRF2ABP8AW4gQiUq1qMB6KoSZAvEy_sg8Btqj-efrKLsHcTJdJbZjTb6MRKTRDb5EI3qD4Z_H9oPwzipMeqYzyyewq9RSLtTcrQ5QBQShMRSINhvMD9nlMnH_n3IkeE9LwjSdp8xY0q3jYCaEHS8TjVToXKR4oSI3LS1E-miXfe4TANALZyAYT_PG4MePfEemh46VuW5bhwnCpv7HaEqhhCS9UszANlJp3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شماره معکوس تا رویارویی بزرگ
​
🦖
دیوسون فیگاردو در مقابل پیتون تالبوت
🦖
تجربه اسطوره یا طوفان پدیده جوان؟
​هیجان واقعی و پیش‌بینی بالاترین ضریب‌ها در
TrexBet
!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72645" target="_blank">📅 01:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72644">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=kYMOPL7-F2LjuQ4ZxSnprFbpTpS_hMzNhoSr0zdMsW-ysYew5TpCCO4RZSVXf6I-RVFNZIFn_dq-r9X34U5_XRjppAFP2RyvmwqCMKSMFPxPRhTb6rZBobX4rJxQI5_z8mM2SW49GdhDogrAzgf4nTPDoewrn-Jy9vPA7kp61dSIg0FvEYpOm8uUQIZ1q6CU9SAgp-xKZzroo5Bc1S1hFKGXaySPYwovXUag9czLrXHJ87CRATt2DJDAXnJJnfflfORoVVNbPvlWIiImknOZrVLLlf10kkmRABdku-tApHaEBExfcec8jNxoFXpJyCSFf8zShW6JC5HJ478FSHVSwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=kYMOPL7-F2LjuQ4ZxSnprFbpTpS_hMzNhoSr0zdMsW-ysYew5TpCCO4RZSVXf6I-RVFNZIFn_dq-r9X34U5_XRjppAFP2RyvmwqCMKSMFPxPRhTb6rZBobX4rJxQI5_z8mM2SW49GdhDogrAzgf4nTPDoewrn-Jy9vPA7kp61dSIg0FvEYpOm8uUQIZ1q6CU9SAgp-xKZzroo5Bc1S1hFKGXaySPYwovXUag9czLrXHJ87CRATt2DJDAXnJJnfflfORoVVNbPvlWIiImknOZrVLLlf10kkmRABdku-tApHaEBExfcec8jNxoFXpJyCSFf8zShW6JC5HJ478FSHVSwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: گام بعدی شما در قبال ایران چیست؟
ترامپ: خب، اگر به شما بگویم، خبر بزرگی برایتان می‌شود، مگر نه؟ اما خواهید دید؛
اوضاع دارد خیلی خوب پیش می‌رود. وضعیت ایران خوب نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72644" target="_blank">📅 00:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72643">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ساعاتی پس از معرفی رتبه‌های برتر، کارنامه داوطلبین برروی پنل شخصی هر داوطلب در سایت سنجش قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/72643" target="_blank">📅 23:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72642">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">طبق گفته حسن‌پور خبرنگار خبرگزاری فارس، فردا در نشست خبری رئیس سازمان سنجش رتبه‌های برتر کنکور ۱۴۰۵ معرفی خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72642" target="_blank">📅 23:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72641">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=SP3dCeyL8Y38rOg5OBINAnGWnklxDKFXOeioZcQKXjEMzwYSshn-kSlwq0hSqZVeYLWucH2eS2f1GgEWe_bzQn76W3BQB4czzk06-8-zEh8J03R79ueeIyuckmFZhvNB5NV-JkE_Txx5zuV39g2-ueegDEfic9vdy--htR2H2XnZxW8eVF3VmRUPgV8BL3alp1eyS9FdPO-bVt1UgC1m1ixf5SWGunO03QUcB234zN-tykj2AuW7Jp4l4yFiZmQ7vtpJXq7e9IYsx1DCMkOve2at0y5TgMTYD7yn9UD4Qt-mG1P6N6PKFB5nZ467x2DaM5gY5d6qLfp-UVGRZdCTLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d476b5a95.mp4?token=SP3dCeyL8Y38rOg5OBINAnGWnklxDKFXOeioZcQKXjEMzwYSshn-kSlwq0hSqZVeYLWucH2eS2f1GgEWe_bzQn76W3BQB4czzk06-8-zEh8J03R79ueeIyuckmFZhvNB5NV-JkE_Txx5zuV39g2-ueegDEfic9vdy--htR2H2XnZxW8eVF3VmRUPgV8BL3alp1eyS9FdPO-bVt1UgC1m1ixf5SWGunO03QUcB234zN-tykj2AuW7Jp4l4yFiZmQ7vtpJXq7e9IYsx1DCMkOve2at0y5TgMTYD7yn9UD4Qt-mG1P6N6PKFB5nZ467x2DaM5gY5d6qLfp-UVGRZdCTLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر گوگل‌ارث با مقایسه وضعیت در ماه‌های مه ۲۰۲۲ و ۲۰۲۶، ابعاد ویرانی در اطراف مدرسه «القادسیه» در رفح (واقع در نوار غزه) را نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/72641" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72640">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=OjkLTXaFxCPnj-TWDuDcR6ik_aBKjQE-JOyx-EqO1yXgLKV7mZ-vHdnK_pdlGUwTxFrWwUv4CSUqubVUPtl22KWjF6a46qkIW41LqVTwKyqVRLc36kJ3E5COCorVKf00eFtFBuZ54fdxL8_NbFO9a_tB2Nqzj3Y1Cp10SfDbicEGxeHUn3STLyT1_g0taFUOyQRWL84BuPWTtFdl_XiY59TVjdT5b92uLdHLSVCgJ9s-dNKSC5WW0buP6-7EV1XQUltEBBduN03hgrxxInfvmFUJM2HuWnEt4XCeK3fTLMCcoUWuy_YmCQik_qiDrWIakYbC8zQO_Zwuvb-EP6vlKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f0ca8354.mp4?token=OjkLTXaFxCPnj-TWDuDcR6ik_aBKjQE-JOyx-EqO1yXgLKV7mZ-vHdnK_pdlGUwTxFrWwUv4CSUqubVUPtl22KWjF6a46qkIW41LqVTwKyqVRLc36kJ3E5COCorVKf00eFtFBuZ54fdxL8_NbFO9a_tB2Nqzj3Y1Cp10SfDbicEGxeHUn3STLyT1_g0taFUOyQRWL84BuPWTtFdl_XiY59TVjdT5b92uLdHLSVCgJ9s-dNKSC5WW0buP6-7EV1XQUltEBBduN03hgrxxInfvmFUJM2HuWnEt4XCeK3fTLMCcoUWuy_YmCQik_qiDrWIakYbC8zQO_Zwuvb-EP6vlKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم میخواسته بره مهمونی و لباس درست درمون نداشت؛
اومد تصمیم گرفت یکی گرون ترین لباس‌های آنلاین شاپ که بالای
۱۰ میلیون
بود رو سفارش داد.
حالا چیزی که به دستش رسیده :
میگه این چیه لامصب؛ من با این برم مهمونی میگن خرم سلطان اومده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72640" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72639">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=v_TlIFygiQ5rt0hzUdUrHcKJJEhrfRXghJ84dfoiRhiIsSaSbtMbpqB8huOQIS6-dUF2i0VdawT95TJGm8Nk70THB-uVwfnp6u_n088qkfP4EDL8uzm4CB5Fy1p_rm4a9JIFIWSC_WACgtQrBWgtEMW7tC9y9Lk4ynbpv4x7WzDNaUIOrthBtsJ3FYnyr6EQ2r5gWMRgkG1zwuCXudRQhosXH-XyojAHDijqoh05znRTsWQIyj8wlSWNfWT8IyAtf3DQdai7fvolscYS0V_Z7Ou5KlVjOA4AOK9HxN-ZS_kA-3optL-oYX1uVKAtqWGuMyxoijAyCmOgcBmKaOfqCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62412d8d06.mp4?token=v_TlIFygiQ5rt0hzUdUrHcKJJEhrfRXghJ84dfoiRhiIsSaSbtMbpqB8huOQIS6-dUF2i0VdawT95TJGm8Nk70THB-uVwfnp6u_n088qkfP4EDL8uzm4CB5Fy1p_rm4a9JIFIWSC_WACgtQrBWgtEMW7tC9y9Lk4ynbpv4x7WzDNaUIOrthBtsJ3FYnyr6EQ2r5gWMRgkG1zwuCXudRQhosXH-XyojAHDijqoh05znRTsWQIyj8wlSWNfWT8IyAtf3DQdai7fvolscYS0V_Z7Ou5KlVjOA4AOK9HxN-ZS_kA-3optL-oYX1uVKAtqWGuMyxoijAyCmOgcBmKaOfqCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسره سر صبح رفته گوشی داداش ۱۱ سالشو چک کنه که میره تو پیامکا و با همچین شاهکاری روبرو میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/72639" target="_blank">📅 21:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72638">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LPPLSGJH-UBKZ5gO82PAfqnvMO3T-Jv2MOK8iKs-phNbbK_DQeqEDJROnIcIhRQubGt32AEaSrK2N6HAzl7eEqfRhcLXQmrx9xXrNHhHbufmDEjjSIiXJ_wlOn5IlFkCAnDCTD9f_wlwuNsytGWXkKBXV7BUAmoFD9cVMZV2FVMqeWT8FU5YS8fWX42WNoKsZdmh5dlsZ-du54QAmX6HEihGtxu8r5dhKjilmMozVO1kpVkj-T5l3jQmQy-S24QyrdOMzNIQpC9czw8oVAobotZqKab9n8w4h-sFkkyzL1G32S4ZbbCG1pN5Xi-fTjcGm7r8N4q5q3p9BXvl7iiWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که ناخدای یک نفت‌کش گزارش داده است این شناور هنگام عبور از تنگه هرمز مورد اصابت یک پرتابه قرار گرفته است.
در پی این حادثه، آتش‌سوزی مختصری رخ داد و برق کشتی برای مدت کوتاهی قطع شد؛ با این حال، آتش خاموش شده و شناور به مسیر خود ادامه می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/72638" target="_blank">📅 20:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72637" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلار 265
😑
#hjAly</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72636" target="_blank">📅 20:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=BQrRErzRs2qawWrJgbkgIAiW4j0dyz6fQLHd_PX2KFzp7gGmjii0Df7oU0-Md-QC_9SWuB9FzV2n-UbacmgdhblT40DmOXsYlZF5F-wQ7WYwtLKCnHxhY44B_mv3oCKqzH-GbtF8ziyLdG83uY8eqpi-nxzm9HeWlSE-NNhDaUjY-HKx8A6cV7WdIYZDH87iYKE_Q2e14A6lmg7N44cAy_MtypoCD5g8hE1ubDqS98JHeimuHkK8_K2u9Pg9a8Mfu4shIhBea3kHaYJv3XvgjdY0ybrSyJpgbB1HYJNd5_g3hHOZuHlOu5GN-rh4y5nBYeb0IYINvY6LmYkrCLjD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd07c4e807.mp4?token=BQrRErzRs2qawWrJgbkgIAiW4j0dyz6fQLHd_PX2KFzp7gGmjii0Df7oU0-Md-QC_9SWuB9FzV2n-UbacmgdhblT40DmOXsYlZF5F-wQ7WYwtLKCnHxhY44B_mv3oCKqzH-GbtF8ziyLdG83uY8eqpi-nxzm9HeWlSE-NNhDaUjY-HKx8A6cV7WdIYZDH87iYKE_Q2e14A6lmg7N44cAy_MtypoCD5g8hE1ubDqS98JHeimuHkK8_K2u9Pg9a8Mfu4shIhBea3kHaYJv3XvgjdY0ybrSyJpgbB1HYJNd5_g3hHOZuHlOu5GN-rh4y5nBYeb0IYINvY6LmYkrCLjD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش تاییده خیالت جمع برو بگیرش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/72635" target="_blank">📅 20:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
😂
😂
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72634" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراق اعلام کرد که مجوز معافیتی برای انجام روزانه ۴۰ پرواز توسط شرکت‌های هواپیمایی ایرانی (به‌جز هواپیمایی ماهان) به مقصد فرودگاه نجف و بالعکس دریافت کرده است.
هدف از این معافیت، تسهیل سفر مسافران و تأمین نیازهای بشردوستانه و پزشکی است.
نخست‌وزیر عراق از دولت آمریکا بابت موافقت با این معافیتِ درخواستی تشکر کرد.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72633" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=LuxCQ9mCFG1v3U-FNiJ4Dh8j_TrwsZTE6dzqPGyOtV-FgYn381kwbbuUCMFfq3e7o6UFLvhwLDLzg6cuvxnrVHh-HWwnMaiijP-XPOZST2-BH0sxE3WCWlXkv-GKLVhQJU9FXH1q2Uj0eHbx9X6csuA9FcdXIK_1sfSe1lkYk_YvshnPO0dnH1fsoccdOoQoT68d3hA0--Wchmf18_C3JcRw7y5bxX4rZvA0Q0q8tWVX-MPcwSFcYlNm9jCCD1Dj-LvlIRwbuGpGdY1NW6pAzHHuroyi8BzPNVodNLg16lkMkMSdHdDMPvsCuBSNKdusZm-7MgqyLTnorZycuR1bFyaftJjm9UEuBbi2ZNE7ZuIRm9s41z8bsXGV_iU7oVImdz5Z6QZz2_pKgno-RGpw93IFi2LUhc1QiuMiYZhFeoRiypxjLHHGttCjcEPBeKfpZfmDUJMPVOJbUpYDR_DqlmRK1XaQKsORdbxFg4QMrPcuEHh7X8leZg2S_KAAn994EyXu3AtryDAtBBjFZoRnmV6HeuH1dyhWDM1pc64elwRzFcE88RaBV60raNx-vPu_EyfJ5qTa5iY783Pp-4ThUUu7prSukVldp-rFWF5sqqNzq_c5AzseReTUSAGr2Ik-qfY2j8lObgkAo9PsQY-cA22QztmwNZ6SiRTS17dAdYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2fb6f9cd.mp4?token=LuxCQ9mCFG1v3U-FNiJ4Dh8j_TrwsZTE6dzqPGyOtV-FgYn381kwbbuUCMFfq3e7o6UFLvhwLDLzg6cuvxnrVHh-HWwnMaiijP-XPOZST2-BH0sxE3WCWlXkv-GKLVhQJU9FXH1q2Uj0eHbx9X6csuA9FcdXIK_1sfSe1lkYk_YvshnPO0dnH1fsoccdOoQoT68d3hA0--Wchmf18_C3JcRw7y5bxX4rZvA0Q0q8tWVX-MPcwSFcYlNm9jCCD1Dj-LvlIRwbuGpGdY1NW6pAzHHuroyi8BzPNVodNLg16lkMkMSdHdDMPvsCuBSNKdusZm-7MgqyLTnorZycuR1bFyaftJjm9UEuBbi2ZNE7ZuIRm9s41z8bsXGV_iU7oVImdz5Z6QZz2_pKgno-RGpw93IFi2LUhc1QiuMiYZhFeoRiypxjLHHGttCjcEPBeKfpZfmDUJMPVOJbUpYDR_DqlmRK1XaQKsORdbxFg4QMrPcuEHh7X8leZg2S_KAAn994EyXu3AtryDAtBBjFZoRnmV6HeuH1dyhWDM1pc64elwRzFcE88RaBV60raNx-vPu_EyfJ5qTa5iY783Pp-4ThUUu7prSukVldp-rFWF5sqqNzq_c5AzseReTUSAGr2Ik-qfY2j8lObgkAo9PsQY-cA22QztmwNZ6SiRTS17dAdYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایوان نخستین محموله شامل دو فروند از ۶۶ فروند جنگنده جدید F-16V Block 70 را که در سال ۲۰۱۹ به ایالات متحده سفارش داده بود، تحویل گرفت؛ تحویلی که پس از ماه‌ها تأخیر — که تا حدی ناشی از مشکلات نرم‌افزاری بود — صورت گرفت.
این قرارداد ۸ میلیارد دلاری، شمار ناوگان جنگنده‌های F-16 تایوان را به بیش از ۲۰۰ فروند می‌رساند.
وزیر دفاع تایوان اعلام کرد که انتظار می‌رود پیش از پایان سال ۲۰۲۶، تعداد بیشتری از این جنگنده‌های F-16V تحویل داده شوند.
@News_Hut
| Reuters</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/72632" target="_blank">📅 19:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-R7NmP8iq76b_soSDdifQp67yxa2atGQ-uac78Lke_RXSsFhK2MfNMhCIIaYV_EtB8y4XpPUfqEWV9kASK_ylDXJ00oaQgOUVOy1TrWHwc5Zr_k6LOCSVdsqMv3qLPawl2wgVm7WgWR0Bv55qfFP71hWqvnP9b_vOxWZKk7KTac7gYi875PXj-HV0vyGY1hcO9iJtsUPQ81dfXDHbvOlUlZYfxPYhjX5ZXqTp1p7eVby-G2VloQ2VELQ_76QCy6FGuSI15FAlqow2mfSRwQoPHInXNv90cSNjJvRlqSgE1WK_SJn4T0uYaxcIBVB8uREky2BK5ViUhjlXwjhg5JuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=WeZG_o5JUiSsFxYYMKI2H7Nhu0zmOK4CCxAWeSohdtjqNWQ1V48r9ZIfuji67o_9qcJ6OGf_oA7h1kURrYH3ZSAVnStq-FJxBkSNUrmD2xveZZN5mcr9-_FjZ44PR0lcolcyn23Y9PbcwdAEfaTX2KB86sW4HD57APli3NaGAtjUP8vAvg4Tyo6B0wh7x1tTnievi3ZEn7fGSO0b61b4P6jRC37m_YZnVp3-BZ_FVs0l9wmsEEwaiuZ4uw0V6N3Zjkrtn78XRBRSDjMSxQ6z7McTbZ9nk3BBh62-s81wiLR6PstkpX1lPwh5xEO9qkCfqJjzhyO4LrZsufLDhtGQOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=WeZG_o5JUiSsFxYYMKI2H7Nhu0zmOK4CCxAWeSohdtjqNWQ1V48r9ZIfuji67o_9qcJ6OGf_oA7h1kURrYH3ZSAVnStq-FJxBkSNUrmD2xveZZN5mcr9-_FjZ44PR0lcolcyn23Y9PbcwdAEfaTX2KB86sW4HD57APli3NaGAtjUP8vAvg4Tyo6B0wh7x1tTnievi3ZEn7fGSO0b61b4P6jRC37m_YZnVp3-BZ_FVs0l9wmsEEwaiuZ4uw0V6N3Zjkrtn78XRBRSDjMSxQ6z7McTbZ9nk3BBh62-s81wiLR6PstkpX1lPwh5xEO9qkCfqJjzhyO4LrZsufLDhtGQOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr5yFVW7w0R7DQAPR8gnF3vTCxx0KVoXKXcaXnHDJlvHNWXWcGRNeCbssSn_x0m6HDqaOzK0alWbgQe8F0c_qND1C7YTQuDF9AuS47XmDd83w6Ax7oO1pD00NwUZsBdonEfGTEfgI_BkhacKr_fq2DDenYeasYP5Bf_j2PWrepU4iqcuzE2YVexN34oVBl0hWF33VDJmzLZq2_SXt3HCVBcZ-5qe7nBeUqQxfeFakQ4WScBDuYPsLdUpxfo52dPAyRLbf8ftNM6yYBxRk1oehLBLpg-pxuzAobncBmOMflddsdsJskgTLsJtrCQ03gIRp3mgfvZahbak7PO4JhG5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=SKMnLDkzGmoCZyjg3bAxWpCMoGNe1S8LiPlF4FeEaQPLm6As9xd1Mz8q5oMxM1wo6lm-n8h_S4pRusZyceIHw-OQFBfiQXvCur0lTfWKebffjlBQI42MzSurw-JokcZucEnot1u7U-OZOxSWqjUGxeAuq_L7YMrvPnT3zeJOeTka66L_hGvYfTy2UOXQN_VZne5yZQzZeMaGHUl_nEnR8YyxJC4moEC5yDRckRs41ZZvZtVVwPQbT1anJgd4K7vhHvRoq62eucjxNZJxzLQXOqUTbUy-VyKZj2fKTVvHcdbzVy4Rgq9YTkisOxf_vA5O4Y62i7tFEunDl46AWgAgYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=SKMnLDkzGmoCZyjg3bAxWpCMoGNe1S8LiPlF4FeEaQPLm6As9xd1Mz8q5oMxM1wo6lm-n8h_S4pRusZyceIHw-OQFBfiQXvCur0lTfWKebffjlBQI42MzSurw-JokcZucEnot1u7U-OZOxSWqjUGxeAuq_L7YMrvPnT3zeJOeTka66L_hGvYfTy2UOXQN_VZne5yZQzZeMaGHUl_nEnR8YyxJC4moEC5yDRckRs41ZZvZtVVwPQbT1anJgd4K7vhHvRoq62eucjxNZJxzLQXOqUTbUy-VyKZj2fKTVvHcdbzVy4Rgq9YTkisOxf_vA5O4Y62i7tFEunDl46AWgAgYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=ViZiEDnvWhdNLoW1hv9iXfI58XSq2-JDlJeXNH6qMWz4POyg1BzkJBCZKI9tkhgMaA8DCL1Xah-fpfEp2yuAEx6gndKHY77vooeCJC3qDkRr3W9HnnFiWbaInXv2aELpNEbayjNofgyWwGpmM_ii6vVushC9DNoDzm_SFWZpOic9hCUyEPKiOaF3GJa3Sljb-W0_NXJHifXdlG-xt2TwI0X4j4Rvgef0Ny7JIPmzTHkkYaJ32i3CJwNLYoWQLVde3DsLGrexZZODFGdS9sRYCRY4_Jfrmv2IA0eBWbKVsiW9F8Gq67wYdrM-yaYbKp3mTDIwtB43sRCvS7uHffjSGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=ViZiEDnvWhdNLoW1hv9iXfI58XSq2-JDlJeXNH6qMWz4POyg1BzkJBCZKI9tkhgMaA8DCL1Xah-fpfEp2yuAEx6gndKHY77vooeCJC3qDkRr3W9HnnFiWbaInXv2aELpNEbayjNofgyWwGpmM_ii6vVushC9DNoDzm_SFWZpOic9hCUyEPKiOaF3GJa3Sljb-W0_NXJHifXdlG-xt2TwI0X4j4Rvgef0Ny7JIPmzTHkkYaJ32i3CJwNLYoWQLVde3DsLGrexZZODFGdS9sRYCRY4_Jfrmv2IA0eBWbKVsiW9F8Gq67wYdrM-yaYbKp3mTDIwtB43sRCvS7uHffjSGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=c68qFJBdZ5_g4TlPQoGJ4jK9mxsZBYCCjHDv4ju5Nz5qGjV-3TEBJCoOR_xSXsN9atcX4Op5rHJPDv3CdbCZ26hffeJuRPqmcjvRjBUfa7NMOJObK4Bka2yF54UNRj07UHWRq7Xe6fJDKKaZuzDuNP3Sa9qDkr_NcSiXuGkfjVL1lnpchzlBvDMcYxJ5kN1KdeR_66s1Z9J_tv2qyp8nxazbrk4KEO4Y0LtbZUBh78wEXqfLSxGDsqG8nJapYntvzPZ8ug1joQlzCxRjJR6l6xQZlFurpL8VT_JjIKjaDz9fpznZLVDDBQiydEWciJq65qRT0zuZdcFKHFAFivKjJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=c68qFJBdZ5_g4TlPQoGJ4jK9mxsZBYCCjHDv4ju5Nz5qGjV-3TEBJCoOR_xSXsN9atcX4Op5rHJPDv3CdbCZ26hffeJuRPqmcjvRjBUfa7NMOJObK4Bka2yF54UNRj07UHWRq7Xe6fJDKKaZuzDuNP3Sa9qDkr_NcSiXuGkfjVL1lnpchzlBvDMcYxJ5kN1KdeR_66s1Z9J_tv2qyp8nxazbrk4KEO4Y0LtbZUBh78wEXqfLSxGDsqG8nJapYntvzPZ8ug1joQlzCxRjJR6l6xQZlFurpL8VT_JjIKjaDz9fpznZLVDDBQiydEWciJq65qRT0zuZdcFKHFAFivKjJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=NsiOgVD71PrOP-pX39gQjBJxp8icbrBDTkth3vm8w4Pni_W6HTZfQpVUj1mKNP8cqPK06azF7Lq5QzHLcw7sexuhG3Qn6BSG2uvcclYwJPa-9quSEl2Wq6OTv_wyHfBNFmHVCZCbQ-S9wuou7aBwXdRKG3JebzsR2EV_73L_z3xP7g67mvfgemKRixlu5_S-iYWPjU6cu2_CtfcjtrZDNsGzfAQnG7rsHbN8uAcKPeo4BWSF8SY7PFzxF_jLjyuqShfe2fpG0m0xXFxoqBJ8yDv0CPXsfLksZNKtZPDTxboVoiuG5Gj1PYWAmh7GtXU3k1gQs75o8lKzDmcvP-GtmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=NsiOgVD71PrOP-pX39gQjBJxp8icbrBDTkth3vm8w4Pni_W6HTZfQpVUj1mKNP8cqPK06azF7Lq5QzHLcw7sexuhG3Qn6BSG2uvcclYwJPa-9quSEl2Wq6OTv_wyHfBNFmHVCZCbQ-S9wuou7aBwXdRKG3JebzsR2EV_73L_z3xP7g67mvfgemKRixlu5_S-iYWPjU6cu2_CtfcjtrZDNsGzfAQnG7rsHbN8uAcKPeo4BWSF8SY7PFzxF_jLjyuqShfe2fpG0m0xXFxoqBJ8yDv0CPXsfLksZNKtZPDTxboVoiuG5Gj1PYWAmh7GtXU3k1gQs75o8lKzDmcvP-GtmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ_jkI9elfC4VTWH8mT-1lOhcrJmew5dfRBcYu_j65O8UawzOudjFyLfhEzxUYgBnCrYUII_jBOaYtfIUdYK6M1d89DLU4M6owje7PkqeQYt4Rx-9mG2DhtxFYRKFCutExgnDrg-GgIGYPnFfZ4cht6Se5HbxoW-dl_ey_Auu2vtsAoPwtyMYihIQFUdBW3h4FVmXebpQ5UmkwBFZb1NxhmUrPyPARKmJOtNhwh2CRL2feo3IwjjZE0JFIeVVxB1oBrfOyG_BGw4csglpxNUIfL_PX7nlbSgoPT2tO868M8SYexInHWfR2hbfuRRanhgHDbIal3FmirjnZ5NZX8pyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=p6CHpq0qXK3oUam3c-woSEGOhS1RZBmc7XWeCCVGNItOhsMAUZKWKzs9C0T71mcoVEz_aAtcmYPQAguLnWZpW4tNMOM2r1wa2jD4gOEldMuR0nNoOPkvnq9To68fHSBi89S92vDQF-fDqPKMXADbu3p2-lxIl4vjPIQdO2BKTjP6fS4EuTFJWdcDMpqkaB4r5b8mYBTCrfKcwyWUdE1pF9dAmuGcCU9LVRImFbcH2GbpZGUXtQG61HT5weIuH3c7sdvozEoiDaXlcLIRAtp3FBnRtOA7SlzGB8h351dVUBsNLBqVdo2NAQgBiN5tsmWg0A0z1rbY7kE3Pgth_jgJrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=p6CHpq0qXK3oUam3c-woSEGOhS1RZBmc7XWeCCVGNItOhsMAUZKWKzs9C0T71mcoVEz_aAtcmYPQAguLnWZpW4tNMOM2r1wa2jD4gOEldMuR0nNoOPkvnq9To68fHSBi89S92vDQF-fDqPKMXADbu3p2-lxIl4vjPIQdO2BKTjP6fS4EuTFJWdcDMpqkaB4r5b8mYBTCrfKcwyWUdE1pF9dAmuGcCU9LVRImFbcH2GbpZGUXtQG61HT5weIuH3c7sdvozEoiDaXlcLIRAtp3FBnRtOA7SlzGB8h351dVUBsNLBqVdo2NAQgBiN5tsmWg0A0z1rbY7kE3Pgth_jgJrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsVi1dB91UXJogAybzdNixguAJIWoud9x_TYbxkPKxMMM8C1T-1aR36S-TfWhV--WhlfZvOHhD4sINaf3hNovc-k6iulO8wXK-214UaA2LC5g0kxcQYNKr0jyJ2yld2O7eooRtbSJYtjieAHtAlv1L-rPuIlUAorGO737stVpcWZiWFBEZC-vVSQuLrwrOObBvG9BGhHKMuKbNKAjcbGpYTtWtuuxOsZ1WLRfyIbHfy1I381awxaMIreuuFjDR-NaJCTaUiTn1KHDZFVGE_V81LrdFhtPgkZR8IQdSbJld6rHC1St4Lparakyx6X2QzJNn3aYsJuxzypiTJzh9UMkvqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=AlRLRPySOtj4WeVZ4qp44Ps8h7hQuQZhKxeas2i3a7FioxzO2b7owFnhF1EWSshItp6O6mJLvFN6oEr1p2SQ-OQq1lbttKhxUy939OC6LgmHF0J99srvq4v0ybUy5nOad88IKUnMeVoaNWZ7arW1fL_qjJhPFCgqI8sQrpZJWpvL2E0LXWWcdvS0KYZ0cRXCIE1eUc5FefdIesq3pjCnSP1n-f6LPScuzeHGAQQsDjZhtAEONCC9X8mmCtytSynU1kXdDShi1ZbNr9tYZ5sEFHPW8swCI3IEn4NftDAzEfQhxqaznhFD_qygT1PK5jAX8FkwxgAijV3fdrY7GQhfsVi1dB91UXJogAybzdNixguAJIWoud9x_TYbxkPKxMMM8C1T-1aR36S-TfWhV--WhlfZvOHhD4sINaf3hNovc-k6iulO8wXK-214UaA2LC5g0kxcQYNKr0jyJ2yld2O7eooRtbSJYtjieAHtAlv1L-rPuIlUAorGO737stVpcWZiWFBEZC-vVSQuLrwrOObBvG9BGhHKMuKbNKAjcbGpYTtWtuuxOsZ1WLRfyIbHfy1I381awxaMIreuuFjDR-NaJCTaUiTn1KHDZFVGE_V81LrdFhtPgkZR8IQdSbJld6rHC1St4Lparakyx6X2QzJNn3aYsJuxzypiTJzh9UMkvqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HZzfWQltfBp2xMyqCW7QBmho3PY-Qp33E4pBl8IVH3OGaX5lCEicKbeYfVEQtKOC2XS6hJ60N-BmkVDJUYDJmzAku_zXO0rmNQj-BBA0xPKftTcjWlDFjLCMG6oF_5FNL6yAskbF0axk-HF7VB1CaL9I9qzgiloLRjBTakEeik2aMxj3c9stIC3Ni-ksQheCqy7y5pLjyeZhiR6lHFaPICX97wxUrSebWvI1_E-G5s7tqE-X5lRT6UDqHS1j-i9zPc9GH-DaOejAoZQ7q-6HYIxASnlzQLmfP5PaCJLVHcs8KUWWV-fNaxjebf3zn57hRPBFIrly2_VHo6BEPQpPQtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HZzfWQltfBp2xMyqCW7QBmho3PY-Qp33E4pBl8IVH3OGaX5lCEicKbeYfVEQtKOC2XS6hJ60N-BmkVDJUYDJmzAku_zXO0rmNQj-BBA0xPKftTcjWlDFjLCMG6oF_5FNL6yAskbF0axk-HF7VB1CaL9I9qzgiloLRjBTakEeik2aMxj3c9stIC3Ni-ksQheCqy7y5pLjyeZhiR6lHFaPICX97wxUrSebWvI1_E-G5s7tqE-X5lRT6UDqHS1j-i9zPc9GH-DaOejAoZQ7q-6HYIxASnlzQLmfP5PaCJLVHcs8KUWWV-fNaxjebf3zn57hRPBFIrly2_VHo6BEPQpPQtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y6HusUmKUjOWbNLbtD1_jZvoN-Ublr4AOc630VXjc3g0_N3hW0_Y32W0x0cAVzhdcMwwyeP5KYl1wvf0YajBWT77eWX0SGycpyK2e-zIqlM4eLnKO3iwoupCef_x_tF1z8jBQuZtUupPlZbGkzhOqHR0AhMp7X5tMzOyGIP1Jdqg-rTM-HwMniOn91V-tCVgsD_OUk8se3eKE-R24aOtB-BVpOKDBqTANoKA1FMEYZnti_tXJgJhCiILf9IX-A3bRlwqDrhZJ72667LkN7sscIU9EpEUWHC07L76RGOtHWmdZjbGZl4Amd0ZhAAv8eBGY33H3jJl3qfHdx_L322i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aORWQNv3aHWyePmu02tvBehO-U1Th76v6nvLB-LDHmvz1WKraTxoqxIfr6iJQuyfJAXzkDAGlYf22lf2we5MoY8ccJzfAbIn0u_FMptFHK6YG9Bd52Ow-6NGDwA9ezVzg6jhMCZUL4kcIUHINAnOfyPZ40pb8qg5XBA-TpaF5nrwGoqrbzS217l8-B6n08uPrJyGk1FLeqZno4lrrBtsiUP23jUJ9GqN47UpdcaYx4XWm0cM5qMGhyvF1ReK4TEc29fJ8_MOreHlIYqZkI77g0JgvnJNGPMpJT6V3GJVjlsk5Y7LIGw9n-_rdhYX5ufl-XDseFXMecs1DYxDpMyRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=Q3RM0awnpDBHZRZW5wfEyA27WWn0IXTNLQpJD-Ev_4Y8XV5w3c0BHsNLbCo7BNUgWQU6nGVgHUPkaPE98TqRdQhKdcwAI6Q12HYroYvXPLEWHig-n4AbqgOWg7bOEeFKZBvV7GbtBNdCziGKZG6UGt-Ce6EvBwOE0KI5RzktG9dso-KzvRc6xdmqBTxDVWJJF5dM7BTM1c3H0Qv2JJy2-pbq6l8cOMbXBDqzowmSE4dn7D11WV_nGuOOlfOyCvoi6We7fuWw2MtCb5eV38NItDIYqox2KuSviBj7c6cbq0IbUicsdAeYgR1T1oEwfgLK-25zsw9Q39wx2jobWcasMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=Q3RM0awnpDBHZRZW5wfEyA27WWn0IXTNLQpJD-Ev_4Y8XV5w3c0BHsNLbCo7BNUgWQU6nGVgHUPkaPE98TqRdQhKdcwAI6Q12HYroYvXPLEWHig-n4AbqgOWg7bOEeFKZBvV7GbtBNdCziGKZG6UGt-Ce6EvBwOE0KI5RzktG9dso-KzvRc6xdmqBTxDVWJJF5dM7BTM1c3H0Qv2JJy2-pbq6l8cOMbXBDqzowmSE4dn7D11WV_nGuOOlfOyCvoi6We7fuWw2MtCb5eV38NItDIYqox2KuSviBj7c6cbq0IbUicsdAeYgR1T1oEwfgLK-25zsw9Q39wx2jobWcasMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzvoXQx9nyCuyLL6oR7-eAnzdBDe6QuHqs2GPaDXTQ5c4dpkM_7dZbu_TtlJlFzoXMDIPaeUsnmdix6PngCEaRGDE2LJ8sttMYftBBMIcHvwcZSJ86SVElZODp0NFa0-a1heG10AL361zhmUl0lBbJ6jd2i7Fs4IRChi0QTuKwrqDyhUAxd15ZYWhRKFfgk0r2i6M8Fx7o3kyOJ65TSNQATqU3YvwFiS6XMSYXxddl5mb2OeCKTxUXKIDZlgTwzxFvaERtGX3_ksCxmnS694_x86C84hYfc7Hohm5_buByuI1ra4hleEN1Q_1sn8zQfiXxTC0WAt0pOWnFU0hi1nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
