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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 21:15:03</div>
<hr>

<div class="tg-post" id="msg-656905">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ad6c3195.mp4?token=fbLi0-gvg24crtXo6MvBKuu3getOEf_wAQzcqrZNm5tBsGHI0vhhueU0JutzTqQgvNVQCLxAz5P0PTdRCXBGXQ_WCkSq0QZEXnAEgXI-1Y1lIVmkKsRiYxbrfN-G_TIR-oRYFVKGLfAk6zD3LZE0WjCg3fZ3BrRVsEJQWem6TJAcUWRjatEs5tVVeoXxgbiOEaqNmdHfZnFUz_bxJbTaOCrp7G3JKV1HjmbOVpwtausxh6oN6qeVY4BPc3aLc9-Uq_d3D_NS3LJo8483tl3aIAlRmlAbkC2HVeW7xVH7NEHxwZT8pI7btTUvnPtTxNjZKrsDPGW8f9w-__UBnXQKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ad6c3195.mp4?token=fbLi0-gvg24crtXo6MvBKuu3getOEf_wAQzcqrZNm5tBsGHI0vhhueU0JutzTqQgvNVQCLxAz5P0PTdRCXBGXQ_WCkSq0QZEXnAEgXI-1Y1lIVmkKsRiYxbrfN-G_TIR-oRYFVKGLfAk6zD3LZE0WjCg3fZ3BrRVsEJQWem6TJAcUWRjatEs5tVVeoXxgbiOEaqNmdHfZnFUz_bxJbTaOCrp7G3JKV1HjmbOVpwtausxh6oN6qeVY4BPc3aLc9-Uq_d3D_NS3LJo8483tl3aIAlRmlAbkC2HVeW7xVH7NEHxwZT8pI7btTUvnPtTxNjZKrsDPGW8f9w-__UBnXQKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: گروه مذاکره‌کننده، آدم‌هایی نیستند که جا بزنند در نتیجه ما باید با قدرت وارد صحنه شویم و از حقوق ملت دفاع کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/656905" target="_blank">📅 21:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656904">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a0e145a87.mp4?token=UVIRCgHwReWEoLxTR0SdZT4kSjWnpDObZSGOlzGwYIhaMfV3GnOlmEQ3MStSnl-w4zTi2aQ3P1JnKcziNjnHZ4UWtrSw3VLQPofp5cxeg1gRzAnSyNB4L9Kr0wiavxtZig0SeNp9oUkSpLiWAk6W5D8LTu9Rm_ro0RO6L9xPxpTklJkA8G65yy4kf1ypyJiVPolLD8t9cCGMBJFTBLGSyLjNeEoj1O88AOZXi6AjzBD0i2fY_ymy2rcXSwTDdFIAi2MSvwqh7yaCbwybrF-i1iEvpPkz59z4XjjqW3vNA9OGTHIYFOcYyIZtOOLSOTzv7IhEgJTk04iOEzaACPBinAKKKCnfsiNQwyB9fZGDAn6E0CICKzKIQkd0246EzDiHqlqttHu-js3nUHoepLOW8bvKW-pwMB6lLwzXl1YWWLJuGrv4mTEudMAhjntJeq9UGYcc-TG_ziR_nIW-bz_QXw0TATjTRAI1rnMYhDhBKfx1yFXF6fuFWidMgedjeyv_3VSul559ua-W-qcGdDMDJsu5nb49z4F0CeoIq0LPSue28Rh1DGjwA1pIa2THvaAR17M5HwvfkelYr7DJ4_pXZSgn-42zNQMLPs5OFnzrepqf8vugRYcM74P94nKgF2hON1MjUEC42vEHQNIqAaWaArWTaErp_2V984Et1o4z8RY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a0e145a87.mp4?token=UVIRCgHwReWEoLxTR0SdZT4kSjWnpDObZSGOlzGwYIhaMfV3GnOlmEQ3MStSnl-w4zTi2aQ3P1JnKcziNjnHZ4UWtrSw3VLQPofp5cxeg1gRzAnSyNB4L9Kr0wiavxtZig0SeNp9oUkSpLiWAk6W5D8LTu9Rm_ro0RO6L9xPxpTklJkA8G65yy4kf1ypyJiVPolLD8t9cCGMBJFTBLGSyLjNeEoj1O88AOZXi6AjzBD0i2fY_ymy2rcXSwTDdFIAi2MSvwqh7yaCbwybrF-i1iEvpPkz59z4XjjqW3vNA9OGTHIYFOcYyIZtOOLSOTzv7IhEgJTk04iOEzaACPBinAKKKCnfsiNQwyB9fZGDAn6E0CICKzKIQkd0246EzDiHqlqttHu-js3nUHoepLOW8bvKW-pwMB6lLwzXl1YWWLJuGrv4mTEudMAhjntJeq9UGYcc-TG_ziR_nIW-bz_QXw0TATjTRAI1rnMYhDhBKfx1yFXF6fuFWidMgedjeyv_3VSul559ua-W-qcGdDMDJsu5nb49z4F0CeoIq0LPSue28Rh1DGjwA1pIa2THvaAR17M5HwvfkelYr7DJ4_pXZSgn-42zNQMLPs5OFnzrepqf8vugRYcM74P94nKgF2hON1MjUEC42vEHQNIqAaWaArWTaErp_2V984Et1o4z8RY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان کاشان و آران‎وبیدگل را درنوردید
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/akhbarefori/656904" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656903">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حزب الله لبنان سیستم جمینگ پهپادی ارتش رژیم صهیونیستی را هدف
قرار داد
🔹
حزب‌الله لبنان اعلام کرد یک رادار ویژه اخلال/جمینگ پهپادها متعلق به ارتش اسرائیل را در اطراف قلعه تاریخی شقیف در جنوب لبنان با پهپاد هجومی «ابابیل» هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/656903" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656902">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYgqBh6hwupT7T2WSS3MXqiSF3CUcu8yK2zCtcOO7hlLtjCORXELVXpIzYiRBeP6OwfsE-y5eVciVP9IckxPxnfi_Ga4R_o7d8jeYSa75oUofl48Liw9Q6Udxe3gGRlNppR_QDZ_5YVbT6JQKkKKHKJfiKJGYhFp6-pdvwjCj3TftSOFeRTm_AZN_nkPoDowiDrILw5FNAE-qLKwGZO2PBSUv17Gy1Gif8OGmuXYy3IppJbnwaKeb_O129dRtbohPI_a-95tPNauQawaqWPulP0QsxYurO0rkUBNRVy7VJsbvu6OuxdZ2hAMK6Iq8mGLNE8qr0raamPz5x0MATo5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسعود پزشکیان: تاکید من بر حفظ وحدت و تحمل تفاوت‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/656902" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اعلام جرم جدید دادستانی تهران علیه زیباکلام؛ قرار نظارت قضایی زیباکلام تشدید شد
🔹
با وجود اعلام دادستانی تهران مبنی بر قرار نظارت قضایی زیباکلام مبنی بر ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت سه‌ ماه، این فرد با نقض این قرار، در مصاحبه‌ای جدید اظهاراتی مطرح کرده است که همین مصاحبه و ادعاهای اخیر او منجر به اعلام جرم علیه این فرد و تشدید قرار نظارت قضایی وی شد./تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/656901" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161940211a.mp4?token=NTw-cR2pl3ByhVVrrYavKuPDy80vE-ElC_zsoR94UuEolC29IHZlV1kR7NCXMg6EcugqcX3squG4PRIHxZqDTuZlkeikA0z3nWY7e2D5x-y_U906jNynSxLn_iKkuOXw4f2rTJf9xxTlIVSogI0W1nIty9czTtM4DciRIB1KQ68J-zHh7BQNdyFEdGmAzcpUqor2naKFhkqAaa6ULBkolz7sNTxQHS2wCOuiO8mo4OZlmCp0hEE6A3pDyOIoO703GSxLYhYnKVzEWdKccBlfMCwbR8bmoCgdl4A13UwA4aGmpx28VBGVE1NL_Rz8Og7n0SjPsAkIsr2jy6iikRQv-pk6EZLoFQUVsrPu-T_2asSqT7FDOxZqLDg72GV9GxYK3yfYr0T3-01JS0ipdeHpn6tumXCGjcOiiAwuQoLfg0q7WN5mn0wsYOB2yLUBNshB48N3lE-VethYhF1qyz3zFjUi9xmbvQSn8O1Rlqmqk5PywqTnI1blSAxejooGpRYkD23BBlDr6gRL2Dqi9ci4ZMAVC5CUDrU4M5BzIQYiVTWpnLq5iV0SyGl5jDI9puHYQJSQT1sp_Z9pqU3AEGxnPORpRJBKNg9D2_g4Nu0n3-ouo1LHI7iIz3fijdi4gst9G547FGyYzmvNp_m1g5tcRJLUMYyvwKzSvPwYv2ijgNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161940211a.mp4?token=NTw-cR2pl3ByhVVrrYavKuPDy80vE-ElC_zsoR94UuEolC29IHZlV1kR7NCXMg6EcugqcX3squG4PRIHxZqDTuZlkeikA0z3nWY7e2D5x-y_U906jNynSxLn_iKkuOXw4f2rTJf9xxTlIVSogI0W1nIty9czTtM4DciRIB1KQ68J-zHh7BQNdyFEdGmAzcpUqor2naKFhkqAaa6ULBkolz7sNTxQHS2wCOuiO8mo4OZlmCp0hEE6A3pDyOIoO703GSxLYhYnKVzEWdKccBlfMCwbR8bmoCgdl4A13UwA4aGmpx28VBGVE1NL_Rz8Og7n0SjPsAkIsr2jy6iikRQv-pk6EZLoFQUVsrPu-T_2asSqT7FDOxZqLDg72GV9GxYK3yfYr0T3-01JS0ipdeHpn6tumXCGjcOiiAwuQoLfg0q7WN5mn0wsYOB2yLUBNshB48N3lE-VethYhF1qyz3zFjUi9xmbvQSn8O1Rlqmqk5PywqTnI1blSAxejooGpRYkD23BBlDr6gRL2Dqi9ci4ZMAVC5CUDrU4M5BzIQYiVTWpnLq5iV0SyGl5jDI9puHYQJSQT1sp_Z9pqU3AEGxnPORpRJBKNg9D2_g4Nu0n3-ouo1LHI7iIz3fijdi4gst9G547FGyYzmvNp_m1g5tcRJLUMYyvwKzSvPwYv2ijgNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از لپ تاپ جدید هوآوی تعجب بلاگرهای جهانی را برانگیخته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/656900" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس قوه قضائیه: هدف اصلی حملات صهیونیست‌ها به بیروت، نسل‌کشی شیعیان است.
🔹
ترکیه: اسرائیل تمام تلاش خود را برای تضعیف مذاکرات اسلام‌آباد انجام می‌دهد.
🔹
هلاکت مسئول امنیت شهرک صهیونیست‌نشین به دست حزب‌الله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/656899" target="_blank">📅 20:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
صدور کیفرخواست برای عباس عبدی و مدیران روزنامه اعتماد
🔹
متعاقب انتشار یادداشتی از سوی عباس عبدی در روزنامه اعتماد، دادستانی تهران به دلیل جنبه عمومی جرم علیه نویسنده و روزنامه اعلام جرم کرد و پرونده برای انجام تحقیقات به بازپرسی ارسال شد./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/656898" target="_blank">📅 20:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHgNMC0IjQ_7NADpxtBIfmJqK2UebZERZaPLPxIyBFzPXwz0MvXaEMW0m7mvITRRLyIOreEON5mL1s0SKc0otabMsl-0mG533nqj6siKDLdcQqfOwNmBMW5Ra_ntyI1PjJtS7G7B0G6as82tsM5fSTrWiBVAxDuuOP-tzL5eltVqK_xFnxLjZV4BG6cvP8Ajml3kLTzxl0bYqlIpJcyzNOoBqj4rsbxOJkbF4wD4i9Y0o8rv2j_BWKR95RmLWrEyxLXFb6hS8c57njdiaNyhOaxY56XN8S1cxZMsIZVqMwAnxNoAFzRCjRMdb0I0jkqwDKYPw0VpzuN4_Xi3RuOCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HL0CnXCKo7BCBgg7vCI7KNm2Z0ZOKVmzbrsIbiLMnnG6n0SioZrWcsMhD6SQue-m-BduCzP-DpSwBmB8r0ixRuQsowXXMBF-QxaFPbdOvqVUduWjSDbJSi0UrcGoI4ZWh0DCej0QffpndgtNRhT8yVaPsx6kmMedtVxRS3JHQyhEgGRdSmPauAjPhskmjoO5mPdhpkug9CQcCRvSNZtt9Xck2ay_XIHHV8D8_dh0n3ikTBJROfIoYc_B9b7JTMhRqCQZSIGtNGY26WeYvXDszy86mqW6c6j7-YNZmRCylNtyOMmNISkS_Oc_9oXgDjgYOdi726BNKaOCIqXJuDcNbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بی‌کتابی
🖋
نویسنده: محمدرضا شرفی خبوشان
🔹
بی‌کتابی، داستان میرزایعقوب آنتیک‌فروش و دلباخته کتاب‌های خطی را در دوران مظفرالدین شاه قاجار با نثری دلنشین و خاص روایت می‌کند. کتابی عمیق و تامل‌برانگیز که سند جان‌سوزِ تاریخی است با زبانی ادبی.
🔹
اگر دلتان…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/656896" target="_blank">📅 20:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f214296a68.mp4?token=v-luXi81EjSoss-KexlKN1OaxJfHqamOTwe0qEWcYg6Dko5NxL62Kmm2VTkGo5mdhd3oByFMHorEeWonrW4Be0YII3a0a5Cj7IYq7Jb05qKksxhRJ90xMEvAYZu6HUvjBWFta0eXh5rgp-kLfPik9-MO8Mw-7vraXZbPxsE-Wn52jtRrH24zrnHjj4T8Y2ncexbcnSF1f-BOHNGI7KNNPB9oeJH1UrI90xYfTBuilvMYY-LOuHJymxPeiqNCG_6Sg6BkoLp9bcUtTjPfqIcG6liIUHqDenPJcATPlBdbVwqmbphynQu7hrg-bW_cU4uk4BjtiF1hCWbfyAO-w9NeCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f214296a68.mp4?token=v-luXi81EjSoss-KexlKN1OaxJfHqamOTwe0qEWcYg6Dko5NxL62Kmm2VTkGo5mdhd3oByFMHorEeWonrW4Be0YII3a0a5Cj7IYq7Jb05qKksxhRJ90xMEvAYZu6HUvjBWFta0eXh5rgp-kLfPik9-MO8Mw-7vraXZbPxsE-Wn52jtRrH24zrnHjj4T8Y2ncexbcnSF1f-BOHNGI7KNNPB9oeJH1UrI90xYfTBuilvMYY-LOuHJymxPeiqNCG_6Sg6BkoLp9bcUtTjPfqIcG6liIUHqDenPJcATPlBdbVwqmbphynQu7hrg-bW_cU4uk4BjtiF1hCWbfyAO-w9NeCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: دوست دارم حملات دقیق
‌
تری علیه حزب‌الله انجام شود
ترامپ در مصاحبه با ان‌بی‌سی:
🔹
من و نتانیاهو به خوبی با هم کنار می‌آییم. ما رفقای خوبی هستیم. دوست دارم حملاتی دقیق‌تر علیه حزب‌الله را ببینم، فکر می‌کنم باید دقیق‌تر بشوند.
🔹
ما می‌توانیم در این زمینه به آنها کمک کنیم، یا می‌توانیم سوریه را پیشنهاد بدهیم. آن‌ها مایلند کمک کنند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/656895" target="_blank">📅 20:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV6lSqjqRFy0e6WlAfEd5HyBIesMhoVU7J_phrPz5Jf4tVgIo1mUkZZ4yxEEmms5Y3x0dSTYkZfNc6wc-Fl8f1QkTGKyP1LGQEL6uczg4bD651XiAXirw-kaceK6k_UjH1Hz_M4AlNXzE0kVSekyWrqd54sSDrh9mUvXAauGZmGqzGSQwIb98Q-TndxhtjYSDSiqhY0mL7Pocl4dRjvOOBfxYvlHEqTpFn_u-4Zvv2P4ZYgIc7Ow3kKXz5LjdUAOTRyT0HHtTWIMLN0atOwgt4CFqVJ6se4XTL1VvMFD7djRcB2epPt96uVwqvHcuM4DfLVmdIKkM53DHx3BCQXoTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دست نیروهای مسلح ما مثل همیشه باز است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656894" target="_blank">📅 19:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656893">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صدور دستور محدودیت پرواز در قطر
🔹
قطر با صدور اطلاعیه‌ای، پروازها به حریم هوایی خود را از امروز تا ۱۴ ژوئن (۲۴ خرداد) محدود کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656893" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656892">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
نشست اضطراری نتانیاهو با فرماندهان نظامی
🔹
بنا بر گزارش روزنامه «جروزالم پست»، بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی، برای بررسی وضعیت بحرانی جبهه شمالی، جلسه‌ای فوری با وزیر جنگ و مقامات ارشد امنیتی تشکیل می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656892" target="_blank">📅 19:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656891">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8138d67574.mp4?token=Wc6w_pkoB58VDF2poItTo7yLl1ED_xAWOgGn6wviRDjh7sWLN1v23N64QI63xgrOjFuCb-Sg8UdOZDrFWkyRUHO6-XUzRr-k1FAxzxDMX7s42UpMZ7fN83QBgwxJ7ksJuPeCsRJkrX5ygBYJWYNUtVssQs5VMNAwCEvnqzdZ9N_8jpCMZUpzV9yUNQWlfBO07rnKhcqdIEn4sJmMt1JlkAMzh03AWmYfleYlXKGRDXR3Fz_jtca5Uz_q8QIEDSCsOfO0haBgu7bi8ESsERqnXo0Je0I0e-ydyJApo77kRgdt27-auKAjdEm_Wnw2W7tFYEpp6t6L2uB1WOTftVLY6BqRB-ZHPlIqkY6wnXMaRhinXd5nE2sCxtZEK7o7isUblqDA3y7zsQgrOOmQhsvy_g6p8jgnhgBpFwl9eP4XhJieJwsivdSXPzTu-gzoXxG5iLDI7E80--MAfd1Quc-8GD2DUp0Vdg5IOKxatV_apPjWvchuF5VWcVjhPxs8-WRq-D1CvhxYFk6ACOy-QClkpsOUcQCRFFpxeles5fKIiprb2hJrzjJwmsGaNvGcFIOKfJ1BND_T2c8QUtDCaVE2MbpuWIbVhfvNkhIkrI-NyXqpPddmF6JzP-umSVSqHkb10GUe08syPp_li3sVsfDeA6sM6JjIqUjLY79TQEPfOek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8138d67574.mp4?token=Wc6w_pkoB58VDF2poItTo7yLl1ED_xAWOgGn6wviRDjh7sWLN1v23N64QI63xgrOjFuCb-Sg8UdOZDrFWkyRUHO6-XUzRr-k1FAxzxDMX7s42UpMZ7fN83QBgwxJ7ksJuPeCsRJkrX5ygBYJWYNUtVssQs5VMNAwCEvnqzdZ9N_8jpCMZUpzV9yUNQWlfBO07rnKhcqdIEn4sJmMt1JlkAMzh03AWmYfleYlXKGRDXR3Fz_jtca5Uz_q8QIEDSCsOfO0haBgu7bi8ESsERqnXo0Je0I0e-ydyJApo77kRgdt27-auKAjdEm_Wnw2W7tFYEpp6t6L2uB1WOTftVLY6BqRB-ZHPlIqkY6wnXMaRhinXd5nE2sCxtZEK7o7isUblqDA3y7zsQgrOOmQhsvy_g6p8jgnhgBpFwl9eP4XhJieJwsivdSXPzTu-gzoXxG5iLDI7E80--MAfd1Quc-8GD2DUp0Vdg5IOKxatV_apPjWvchuF5VWcVjhPxs8-WRq-D1CvhxYFk6ACOy-QClkpsOUcQCRFFpxeles5fKIiprb2hJrzjJwmsGaNvGcFIOKfJ1BND_T2c8QUtDCaVE2MbpuWIbVhfvNkhIkrI-NyXqpPddmF6JzP-umSVSqHkb10GUe08syPp_li3sVsfDeA6sM6JjIqUjLY79TQEPfOek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ورزش: فعلا تصمیمی برای کناره‌گیری تیم ملی از جام جهانی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656891" target="_blank">📅 19:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای هگست درباره توافق احتمالی با ایران
سی‌ان‌ان:
🔹
پیت هگست ، وزیر جنگ آمریکا مدعی شد با وجود پاره‌ای اتفافات در خلیج فارس، ترامپ همچنان بر مذاکره برای یک توافق متمرکز است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656890" target="_blank">📅 19:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99130437ee.mp4?token=pIinbCL8aYCQK2aiPGY-CtM7MlUPTsZ671AJO_LPnN8UdObA42Gjn8f9AxZbQJ7FtHuKtijyJlpiYG-KwcfSOZAowy-0GkpF10392e1xFr174qF0_sZQTprKRNKoGuuZwGyIWC8-zAlOPbty_EihralLJPicswmoHI6-yzr_z9Mj8IuTCJRXwbK38kWGnYUwcN8nVvd7RYXqj_qV1LkwDcLwJIDMNcIZo7aHcFw2xDWpDfsoCoMfIJBlNseSy28JNQ8N8zNwUSwlB3JHxxd740XrdbWTNfDETehWWBxGIS683lZrHuYcK0OUOQdKVSb3XA3ukz9roBtpwDwy_4VZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99130437ee.mp4?token=pIinbCL8aYCQK2aiPGY-CtM7MlUPTsZ671AJO_LPnN8UdObA42Gjn8f9AxZbQJ7FtHuKtijyJlpiYG-KwcfSOZAowy-0GkpF10392e1xFr174qF0_sZQTprKRNKoGuuZwGyIWC8-zAlOPbty_EihralLJPicswmoHI6-yzr_z9Mj8IuTCJRXwbK38kWGnYUwcN8nVvd7RYXqj_qV1LkwDcLwJIDMNcIZo7aHcFw2xDWpDfsoCoMfIJBlNseSy28JNQ8N8zNwUSwlB3JHxxd740XrdbWTNfDETehWWBxGIS683lZrHuYcK0OUOQdKVSb3XA3ukz9roBtpwDwy_4VZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ایران روزانه ۴۰۰ تا ۵۰۰ میلیون دلار از محاصره دریایی ضرر می‌کند    ترامپ در گفت‌وگو با ان‌بی‌سی:
🔹
ایران به‌دلیل محاصره دریایی روزانه ۴۰۰ تا ۵۰۰ میلیون دلار از دست می‌دهد؛او گفت این اقدام را جنگ نیست و آن را «مانور نظامی» توصیف کرد.
🔹
توانایی‌های…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656889" target="_blank">📅 18:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
آماده باش اسرائیل از ترس واکنش احتمالی ایران به حمله به ضاحیه
شبکه ۱۴ اسرائیل:
🔹
به دنبال تهدید امروز ایران مبنی بر حمله به تل آویو، اسرائیل در حالت آماده‌باش کامل قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656888" target="_blank">📅 18:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz58YqYLkcPoutcWoenpf-xWL9LkaLCMlgHP5yfDLDl6nvwP9xKD7di8gf9KeRm46EtlZW4h2BbXeVwsxUGtiK7BCiATGyK89D6NY5d58LP8nLjJFlBGvWBmZGlowuMNrdfVrOyGJUAu0eSnxHn81FT3vyzqpsWVE1sc9IHDrFVcv6HTd7ljc5CQKDQynOOlH-CrWewWEi93cbUG4IEpS8-8LQVg7yXTQF8GoQ__PDldZcnXXdU_XltC63xF1Gcu4olW_8WeK8qEJUSWGPBMoiJ-m-qVxwcZDGJgG0zcX4QUyQu82nl-T4HG4GJPdde2ckHYyY7z9EzhvQt0aebHvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/656887" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ae042875.mp4?token=o6zN55WHQtoggRS26X3teA96s2Rtmgh4yc3ABmkvdu-rEKWvqeicQ9n-vA566RxZhGXSzwg35qL05lcLh6_7gFlm5pC-l1Ealc1Dx3jIJdjRmHG9SRvy0ZQ6Zm3xsCExjFKjUFeFDvAfHvViQskW8ihRuVRVwRXq1wi-zjzV4t1xXDhJ02assjVQ4TBtXybA8_kOa8K8W9o8IIMvK_9Jnbz56LOs2P4IAudzIFZNkXr6xjFwQKd7ShdBip2uVXVuxr6wnMjvWLgxmXMYV-pSK0T28A87FNsvuFU9LT4qLQNpOszYlSldKvZziKxb0sXPeMXF9HvvXuLzfxijJV3jAakshzGwnWeE2iTQ6OeFkTCX1E8cGrRtsigLj6O4oPpGNQ1bRAAESVDqAcy68zPt-WKkxTIvR1l8ujeAVUujl0kRzLhSLDikbWZ8jPJ3pivSiLAJgYpyLItHuBAVI2CJVfjulxuNnlXROa_6nZHibS54CCmeqIGdjKWKfx_azEL8TWHakKfVXcyVI0oESHBfY9mwERiKU0ap1QVtw2wLS-iV5LhFDe01hOfbNNHVMN_Tbb_tWZvwKxaecPSYkBLVH5SyBTBNVbrRC1QIztgWGzARzrvARv0oHP_vgKnSbONRQaxZxtfL6871wbKcBWAlEAQe2nzsjR8A5-nRp7NHlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ae042875.mp4?token=o6zN55WHQtoggRS26X3teA96s2Rtmgh4yc3ABmkvdu-rEKWvqeicQ9n-vA566RxZhGXSzwg35qL05lcLh6_7gFlm5pC-l1Ealc1Dx3jIJdjRmHG9SRvy0ZQ6Zm3xsCExjFKjUFeFDvAfHvViQskW8ihRuVRVwRXq1wi-zjzV4t1xXDhJ02assjVQ4TBtXybA8_kOa8K8W9o8IIMvK_9Jnbz56LOs2P4IAudzIFZNkXr6xjFwQKd7ShdBip2uVXVuxr6wnMjvWLgxmXMYV-pSK0T28A87FNsvuFU9LT4qLQNpOszYlSldKvZziKxb0sXPeMXF9HvvXuLzfxijJV3jAakshzGwnWeE2iTQ6OeFkTCX1E8cGrRtsigLj6O4oPpGNQ1bRAAESVDqAcy68zPt-WKkxTIvR1l8ujeAVUujl0kRzLhSLDikbWZ8jPJ3pivSiLAJgYpyLItHuBAVI2CJVfjulxuNnlXROa_6nZHibS54CCmeqIGdjKWKfx_azEL8TWHakKfVXcyVI0oESHBfY9mwERiKU0ap1QVtw2wLS-iV5LhFDe01hOfbNNHVMN_Tbb_tWZvwKxaecPSYkBLVH5SyBTBNVbrRC1QIztgWGzARzrvARv0oHP_vgKnSbONRQaxZxtfL6871wbKcBWAlEAQe2nzsjR8A5-nRp7NHlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: برای عملیات‌ وعده صادق ۵ آماده ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/656886" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh5CunKz-Re6Huxr8EO-VrHbeHlk_5KgnokHYW-3xKbhmirGaKQjCSiL-Fko0sn8z452SxE0K8Z_XB7m5l6_aUnZsLLgtZgfV6DoiLcMfO0-UgLhkN_f42jv0vEao3JFVYgdFmeJiPHMLU55NbqCBkm3b-nAeMCPwIq4yosgZ2xpKwcnOaOYDhdSbC2dkhcf2esEM7BWOriF3ac6unv_74qLvd-Bp5ZZc8L9FpVK70QXhY8mPvuy1l_7nukzBNqo-BaMUrASeNKhBClGfWAkJuZPv7ZZR9L56j_rXTwvja1ujZ9kO-YoqJ7DgBej6dhPypKEYtp9BQiMJy1COU6NLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی، عضو تیم مذاکره‌کننده: صهیونیست‌ها مجازات خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/656885" target="_blank">📅 18:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
۵۴۰ هزار نفر در صف وام ازدواج
نایب‌رئیس کمیسیون اجتماعی مجلس:
🔹
حدود ۵۴۰ تا ۵۵۰ هزار متقاضی وام ازدواج که پرونده آن‌ها از سال ۱۴۰۴ منتقل شده، در صف دریافت تسهیلات هستند.
🔹
اولویت دولت و بانک‌ها کاهش صف و تسریع پرداخت‌هاست و موضوع افزایش مبلغ وام نیز در صورت تأمین منابع در حال بررسی است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/656884" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB8ky_dc1L7v9rC2z8IDkmTC9IMd07kavozHrtmulFj-AjFrHjJVtkZzdASR5Vvtnok4DZq4pV-2Za-WMHYn6fUvVqeKPuRJY_pOpXOnOAS5O-qPAH7MCBcIX4pJ10NYv8LIT32ZJfW3R85KPJZ9DyLkyVM6S9SSmNblXtHsXxKRy09zlhMVgq9KUDWYqS7Seu6JLJhkDuVqj0g2zm_8EeNi0Y0AE0ZXhm8RHjlNSzD4Rd_VBWuANiWjdzqDvK4KGLZMTz_0RLltv-Ax8dhJL2cLT2uCIrX9DI4hzyOPWMvRPicJbM2Qo1TEZ_EnKpRuDa2UVZj3Ba-vTLuIu9V2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
تفاهم‌نامه همکاری بانک تجارت و «شرکت بازرگانی بارز پخش» در جریان سفر کاری دکتر اخلاقی به استان کرمان به امضا رسید.
🔺
مدیرعامل بانک تجارت در مراسم امضای این تفاهمنامه با تبیین ظرفیت‌های متنوع محصولات نو این بانک از جمله تأمین نو، کسب نو و روزنو، نوآوری‌های انجام شده در فضای کسب‌وکار کشور را خلاقانه و امیدآفرین دانست.
🔺
مهندس حیدرآبادی مدیرعامل شرکت بارز پخش نیز ضمن تقدیر از تلاش‌های انجام شده توسط بانک تجارت گفت: شرکت بارز پخش با بیش از شش هزار نفر نیروی فعال در زمینه تأمین، پخش لوازم یدکی و قطعات ماشین، درخواست استفاده از طرح‌های کسب‌نو و روز نو را در راستای توسعه فعالیت‌های خود دارد و امیدواریم امضای این تفاهمنامه به افزایش هرچه بیشتر تعاملات دومجموعه منجر شود.
🌐
مشروح خبر
👉</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/656883" target="_blank">📅 18:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b752c3463c.mp4?token=CDrMpDzO1onEisslOY2J-Mu7VyuhiUPu3-XQ5qk0M94oUrKsJBW_M9PufQBJ4k-B3QvEK2DbpCT1qYCbLhmjBZqGbWRTcZJIIEcEgKLeLwLCpChcAhjragmE2qAe-mFiB_BLn3AS_UaCsSutfw3XDFE5J_PnHO05IdkVY2Hg59l_nxw8Tho3XHjESbaaBYKRTpzmYEQ2JVSHPEYibyJm5l4hetDLEQ4E8ycmkJN__wRNDSRvjf6U2LWhnlFralh4ZqzcjtjAmi99FzdnEj2GY0nKDU_kVEp9AeUr7CSXaoDGPerc0iH4GOXfxmMzyKyddbqez9h-ZdBATZaw4j-uxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b752c3463c.mp4?token=CDrMpDzO1onEisslOY2J-Mu7VyuhiUPu3-XQ5qk0M94oUrKsJBW_M9PufQBJ4k-B3QvEK2DbpCT1qYCbLhmjBZqGbWRTcZJIIEcEgKLeLwLCpChcAhjragmE2qAe-mFiB_BLn3AS_UaCsSutfw3XDFE5J_PnHO05IdkVY2Hg59l_nxw8Tho3XHjESbaaBYKRTpzmYEQ2JVSHPEYibyJm5l4hetDLEQ4E8ycmkJN__wRNDSRvjf6U2LWhnlFralh4ZqzcjtjAmi99FzdnEj2GY0nKDU_kVEp9AeUr7CSXaoDGPerc0iH4GOXfxmMzyKyddbqez9h-ZdBATZaw4j-uxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوهر خیراندیش، بازیگر: من بچه بودم عمو پورنگ برامون سریال‌های کودک بازی می‌کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656882" target="_blank">📅 18:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcOTUMTyWEi-UmI18kwvgLidd_ywD8ltSx14yoOPeTxYuTAUU0okuG0hBHhKUwJMdnyDwFlKj7kElTnQhgvq5DeTYb04HCn0mQ4PxKhxHqdbqcaWvyBAgosgK735r7Z-NurpZozLdCc7-t1z_iSdeQUdGOQhRzhYwuzuHphFR36Xk1Ha1n2HX0HxDFUDRGGAfwkLCGntkYnwR0iai29ogh3Rc-fYwhe2zx1R5Xr6zp9dY_3zYszgFYDhnK_me7P9VZDN1-IWnB-hdwgdZWxkF21u1wJHUOPGCXKHrEpMACuXP5N8lXLRuoYPZShvFE-7SBoz3ZtiRmwVRAzGjnQmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی چند روز پیش: در صورت حمله مجدد اسرائیل به ضایحه بیروت آماده واکنش هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/656881" target="_blank">📅 18:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656880">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
احتمال تأمین نشدن تا ۲۹٪ تقاضای برق در پیک تابستان
رئیس سازمان بهینه‌سازی انرژی:
🔹
در اوج مصرف تابستان احتمال دارد ۲۴ تا ۲۹ درصد تقاضای برق تأمین نشود و حتی با استفاده از سوخت‌های جایگزین نیز جبران کامل آن ممکن نیست.
🔹
سناریوی بدبینانه نیز باید در نظر گرفته شود و برای رفع ناترازی انرژی راهکارهایی طراحی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/656880" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656879">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR61ORjpToXkioTEywmqh_vAtxvd6E9hT73khyCqa0DHlq9Cehpbb-3Fl1HLMYmE3iiYWYp_MwtR-X08b33NRa3silM8geTq4fKabC7bChzLNRAopPYpMEWZgJsFWgwmG480cGPuD1ufEk7qasKvzFOEpV7NGrjlEEHO9nGYaCTCsoJa-n253BJlJZETXz9jAeUVKs87tBtnOR__tv3gisACNEw0MpFR7f6GTJaTZWQNQ1mO34Ara47St1Uagqla5wKSK8SQuSn2ZxsnsNhFrb8cX9qNDFQ3DYWyeLHnGELweJOy-9ngVQ3aVuMbRbT4c75vdVDN3FDd4lxcF71STw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/656879" target="_blank">📅 18:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656878">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2cTBnQ9o60FmUStVezSCX0cOF_y4ODlH5vhrN6XYlqFMSex1uayi1v2TfBaj7N8-P_lI3RLKmGsGtfOXqVPxvlcrVo9Bc0v4p08hwSlK69-i3XOxhb19T1D8pOLokHu1zH2DrrEfw7CbYFx0FAI6rmXqJEtOA8gPlhHzXnL1WSZ5OhLmspOMqXeFzVDdfD2Fpe1_VRAnp-Uya1WHRFh9YQNznrgT3eHEtqe29kVjTfpsJTaXgSJzEFLrMlpb3g5gT6pvTKJ7Gxg4d-LbxIUf2sbYukRz3Np82KB1aWepslWagMa3H2A6joEH8uFvhZY77jg-2mmVsq2TLHubw3-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابوعلی بلعمی، پیشگام نثر فارسی
🔹
ابوعلی بلعمی وزیر دانای سامانیان و از نخستین چهره‌های بزرگ نثر فارسی بود. او تاریخ مشهور طبری را به فارسی بازنویسی کرد و پایه‌های نثر تاریخی فارسی را محکم ساخت. بلعمی هم سیاستمداری کارکشته بود هم نویسنده‌ای تاثیرگذار که کمک…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656878" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656877">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2007c56683.mp4?token=RmdDywwYb3s7Cu1WTiZ0k6PJOTBidiD2ZLzQZPX3LVyq121VBkJog3GL1ICl62w09FI8fArwcX_6kx8jLEMg7PecCGeR7_BREqGISBhwwLDIAHB_HuyRRJ6OvwHpovpqxMWE-X8seUukSgIDOeStVzLcMLVzEZnYOm7bahmCHH9WpSSU_ONncsrsHjUYA7WoZwjNafv1lH_wXa1mEOe_WLV6Z8DGDT6w82HBOjL7SoCA_EdJbvhmUAMbGQv-uK99SOIi7dihtOO8JNM_cUrGtE6Kjg4MdIg7F4r4cHgxRr8gZvy14XlQOjkC3K0AiQq6izPVmWT3JX0fk6HUWbM-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2007c56683.mp4?token=RmdDywwYb3s7Cu1WTiZ0k6PJOTBidiD2ZLzQZPX3LVyq121VBkJog3GL1ICl62w09FI8fArwcX_6kx8jLEMg7PecCGeR7_BREqGISBhwwLDIAHB_HuyRRJ6OvwHpovpqxMWE-X8seUukSgIDOeStVzLcMLVzEZnYOm7bahmCHH9WpSSU_ONncsrsHjUYA7WoZwjNafv1lH_wXa1mEOe_WLV6Z8DGDT6w82HBOjL7SoCA_EdJbvhmUAMbGQv-uK99SOIi7dihtOO8JNM_cUrGtE6Kjg4MdIg7F4r4cHgxRr8gZvy14XlQOjkC3K0AiQq6izPVmWT3JX0fk6HUWbM-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم حملات شدید و تجاوزکارانه رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حملات شدید وحوش صهیونیستی به شهر صور در جنوب لبنان گزارش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/656877" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656876">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq3sMtVoTTlrRRPUuOEWSeRy828LABIX4Kt9BQtEKic9qIu4l-eCHoqtbL_e0rj8x5C2y0w4gmr3SnVOpIgnUZaix0BAjmNNPc2cuqUyiO7uOHkOnziFlfII3bwHpOj8bKJ6al_zICOy0SasECSXEPwpkMEsjYnP0nfQ9sAg7Y_Th_e6iyEhaN-TOQd5iIjG4f-FoF1vrBpQ1hg9UOttLu1Uvsr5wL2u5S4YFjXXZwfJKCzK2_eScvFeJbQLGpGgk0XgOzONpEPR2c1-KV6NTB_ILPReGN6fQaY4TuPUSIZkgjHcR_rypkwdWhtfMsJoAn7MOTIUS1g5EGqIZ9fbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های غربی درباره جنگ اقتصادی علیه ایران چه می‌گویند؟
🔹
بازخوانی گزارش‌ها نشان می‌دهد که تاب‌آوری یک‌یک ما، هدف اصلی این فشارهاست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/656876" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656875">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای رادیو ارتش اسرائیل: هدف حمله به ضاحیه ترور نبود  رادیو ارتش اسرائیل به نقل از منابع امنیتی:
🔹
در حمله به ضاحیه بیروت یک مقر وابسته به حزب‌الله هدف قرار گرفته است؛ منابع نظامی این رژیم همچنین ادعا کردند این عملیات با هدف ترور شخص خاصی انجام نشده است.…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/656875" target="_blank">📅 17:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656874">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ترامپ قمارباز: من رهبری جدید ایران را منطقی‌تر و بسیار باهوش می‌یابم
🔹
مجری: آنها چه کسانی هستند؟
🔹
ترامپ: نمی‌خواهم به نام‌ها اشاره کنم، اما شما می‌دانید که آنها چه کسانی هستند. آنها رهبرند. آنها توسط مردمی که باید به آنها احترام بگذارند، محترم شمرده می‌شوند.…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/656874" target="_blank">📅 17:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BK240jhcAXwiPSS85p-8AkrBqllVHb-b11_W1PSQR2Edq-uZ-erJJRq4r8JN0fyIb20Rpppv1RY3QKtHWarzB0RHEkxTxiiwXOaIRQe3Tn6y1Qn6TIHr5Ryb-OIk7JBHbcB2DF86ReSQIgjY6W4d5-aFTAnqvXvNw4QuaDLV3I7JGTouajlWOTp3HOv2pdLDVO13qZNgMzKus-ooSDw6p_hWNV_0PkgDlpT2lWv93bv2fpC0SyF64AKiipgBPgJRblj5W8rsL1fO5nAk9-KRO2qPKuJgae_H3ZJxrsbpE6fdx0J_w2-gHLgT-QQQ3hkDePfty2j6TsIgkemfle1nKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RS4Bnqy9OsUtuUQ17gDM6iqYzuRB_mutdQgH5jbw8-6MoDNet1vOBOJ1NrXykJACx4lpg6pTxvq72_D9m-VnVw662a6DsbidylFNRNzUl8Ei6Av_CFaHeX56aBGpivc1giAApAuVVrYO0mqhK--OiocFRvOPzhdqI8G-3Ysv1OeV4UMjk3oHx2DLgvivdCIxMKdQY96SbTl0TkW_i_HDTDZQD-s8V1-LRLjgazfAs18xnPMnjWMW6DpbVuJvl6thGicoh0nK6LHbibjnSldnJOoSSITBzo9gDElyou1G8czCmIgHd4Hr9hrmLc0zJI7SCngfIw3plHK5MHR3T6Xk_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6AGt5Hn__n7PoiTw0YyLLz_SpE5zeLg9AMOJnHfO_4PCLNb9msBZUfNCXVJMRqOCEhMtEkszUZshEStG_JOZgHMu8fFIvBjsnlKb-ez2DnK4aRrc9wF73sBkSwn53jS2w_195368ATzby4LnzvdVXB64uXFeHqpIY0ibt_t239plwVtCVyb30nKm_PkltswnEcZg7RGNhTq-e7RWHpuNaf3Z-X4X04_tkaYLdEmIDif_XZmekMR_0zLiqoXVo9XWWQ7BWKLefwznE7qk_-zbE9Z09LhuYjOBrsvcLDbl3KDqjq7_uWgOsN3-knhGxVSwRCfLSZvcxz26RkbyTtCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s63n3uL1K72jgqofGvNsXW6RrFN_km6LWfvmrgTIFL8Eaoxjypy5CRk_OKr5do6TEZTjd95AKeV41_0xziD9aEpgrZMC7f7Mjk5xk4kitogz0KUI8DcwIeXMfjA17kuVwrJIRjkvFwMC_MKI-rHjDqWZIYfBT5mhMUWpRsSWe0dL0p3TGkZTrK_-vwrEY9VnVT_x9HGCjnhgkTWYj5dMz5p9ElbCDhaH4yo9ykLxgQ0Yv7O7XaY2o4dfxjPbXDxNYX6oVs96efDN4P16m62F3ddC6Txg52HZbXQaaisym_4X5sEnvhWp4R3fNB1O2NahzmuF5WABeFcI0rzemKA_cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از لحظه ورود بازیکنان تیم ملی به مکزیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656870" target="_blank">📅 17:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c3f6852f.mp4?token=Kq5JR23jeZmYytKWrCyaVjNdZSFIO0Fp5XTGlgXNPxTWza7GfacVa1eb41buZcWD4HdiVHlRvqJiYXSCQf5aP240CFKxLJEfgyZVwTG_gNecnJjeTbKxv3K1qv_vayf5Ykbo3HwlD1gHO0Cqpo1QjoQ7FBBSEk3udwmmLk3Cvkgf9Zkknd_jwlPU5qFQTVjJBZzbsCeur5RNrZ0hxtumtvyY3SxbNauMs7kVoFYGwRyNE4gxXQsrmWMG8L382RybGEhb3M2w6plcmaTH5LZ2iLQe2zR15ux7Hmpovct1gOYYfQ9MFsCmWpvdduzf_9CVDG4QvOO15aXrh-W3xI7DDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c3f6852f.mp4?token=Kq5JR23jeZmYytKWrCyaVjNdZSFIO0Fp5XTGlgXNPxTWza7GfacVa1eb41buZcWD4HdiVHlRvqJiYXSCQf5aP240CFKxLJEfgyZVwTG_gNecnJjeTbKxv3K1qv_vayf5Ykbo3HwlD1gHO0Cqpo1QjoQ7FBBSEk3udwmmLk3Cvkgf9Zkknd_jwlPU5qFQTVjJBZzbsCeur5RNrZ0hxtumtvyY3SxbNauMs7kVoFYGwRyNE4gxXQsrmWMG8L382RybGEhb3M2w6plcmaTH5LZ2iLQe2zR15ux7Hmpovct1gOYYfQ9MFsCmWpvdduzf_9CVDG4QvOO15aXrh-W3xI7DDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به ان‌بی‌سی: ایرانی‌ها قدرتمند بوده و به خودشان افتخار می‌کنند و موضوعاتی است که فکر نمی‌کردند روزی آن را انجام دهند اما مجبور خواهند شد تا آن را انجام دهند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/656869" target="_blank">📅 17:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dffec21fa.mp4?token=vTyouK-r2XhzQZGsfpROdZc83jzr1GiTUTSleWndy3rd6X1UZjAKToxYdPf3ausp30Bw8xsMGZgrtn-92tdUHtVkIl-rzzfsFHr9VSZZxYH7p7y8AY0bjD8aSGMqy4rHhcsLDJhreLiQpo8-FSfl_GgvElYX5SQqKa7wdaDXRBpJ_hwdtsHqUuAHmfvcRrWOVeooUndFTFvtTpmoFVR1UVO-ZO81sTEEwlFzrEMqP_DP6q5yxR0GRYCF3dd6DYJxkexruP7rcjP5JioyrT1TSDJ7oZj1hnBUaw8W_C5-zjfnFUpUjctBO8KesptxDvOHT7Q0enhCPfq5spRl4fReRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dffec21fa.mp4?token=vTyouK-r2XhzQZGsfpROdZc83jzr1GiTUTSleWndy3rd6X1UZjAKToxYdPf3ausp30Bw8xsMGZgrtn-92tdUHtVkIl-rzzfsFHr9VSZZxYH7p7y8AY0bjD8aSGMqy4rHhcsLDJhreLiQpo8-FSfl_GgvElYX5SQqKa7wdaDXRBpJ_hwdtsHqUuAHmfvcRrWOVeooUndFTFvtTpmoFVR1UVO-ZO81sTEEwlFzrEMqP_DP6q5yxR0GRYCF3dd6DYJxkexruP7rcjP5JioyrT1TSDJ7oZj1hnBUaw8W_C5-zjfnFUpUjctBO8KesptxDvOHT7Q0enhCPfq5spRl4fReRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مقابله حزب‌الله با جنگنده اسرائیلی
🔹
حزب الله لبنان با صدور بیانیه‌ای اعلام کرد که رزمندگان مقاومت امروز یکشنبه با یک فروند موشک زمین به هوا با جنگنده متجاوز رژیم صهیونیستی در آسمان النبطیه مقابله کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/656868" target="_blank">📅 17:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای رادیو ارتش اسرائیل: هدف حمله به ضاحیه ترور نبود
رادیو ارتش اسرائیل به نقل از منابع امنیتی:
🔹
در حمله به ضاحیه بیروت یک مقر وابسته به حزب‌الله هدف قرار گرفته است؛ منابع نظامی این رژیم همچنین ادعا کردند این عملیات با هدف ترور شخص خاصی انجام نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/656867" target="_blank">📅 17:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a815a7f956.mp4?token=FkZPXjSBX8ZwxkhaJXMLPIMuQet2UwUn3sfbQqn7-K_3jm0PFnWfV4NfSl8Mr_85PIZDDvHplxyRlalisSfJWp8iAnykzKYowXx57szE7-lfov7-KvFgESkesEyXcyA2YQ5DuWR8LlX9hV8R9YqRX4iZ1IwnPFU24qlw_0khRulMmMpTI7m_pylZMa65hYZ0L1gDBtXie_oqL9lyO25wXQk1-s4uqqT5r8wB1VQa95eC_IlQG9VOow2FyudLzTEl3fOEpPCdpTLNLGslVA62NA6lsucs-74Z2Za42BiLL4uFTKrWCn-qKWx1arPyrpyRj0pqymGQ_ZglWFH90csYPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a815a7f956.mp4?token=FkZPXjSBX8ZwxkhaJXMLPIMuQet2UwUn3sfbQqn7-K_3jm0PFnWfV4NfSl8Mr_85PIZDDvHplxyRlalisSfJWp8iAnykzKYowXx57szE7-lfov7-KvFgESkesEyXcyA2YQ5DuWR8LlX9hV8R9YqRX4iZ1IwnPFU24qlw_0khRulMmMpTI7m_pylZMa65hYZ0L1gDBtXie_oqL9lyO25wXQk1-s4uqqT5r8wB1VQa95eC_IlQG9VOow2FyudLzTEl3fOEpPCdpTLNLGslVA62NA6lsucs-74Z2Za42BiLL4uFTKrWCn-qKWx1arPyrpyRj0pqymGQ_ZglWFH90csYPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران به تیخوانا رسید
🔹
تیم ملی فوتبال ایران پس از برگزاری اردوی خود در ترکیه و برگزاری چند دیدار تدارکاتی در راه آماده‌سازی برای حضور در جام جهانی ۲۰۲۶، از ترکیه عازم اسپانیا شد و از آنجا به مکزیک رفت. #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656866" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnvwxmZVehByxmm9P2L-mLR-c64d6xpPN_0-cQtq12IdRgNdFaMjFMJWc6bRxLosDXdqB5uWVGE5_LC83cZ4Ac5qfHCLkQRGkkmUO_5upbCE7YI8A9dlUodUb98tHbPNz5MHBOGCm6P-MaxPkOL4P-UVniCDpYRGVG3wIHdORD-UykAOi79LS_op4gpFZgDs6CMCewNCa7jUEKZWCWeh7pub69SKeu0iEpFf3sUQXDswxVl_C9vJiw7q9JSU71lye9O8VL3N0KTop1pqnG9EX-8nI7MiM5Ax7QkzaaaRMMHqFIyve-uaY0IH443tI1hXQt_dXjBNyVDXgQsNZ5FgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه «بازدارندگی» ایران ترمیم می شود؟ / اگر این اقدامات را نکنیم حملات پیاپی آمریکا به ایران حتمی است
🔹
تجربه جنگ ۱۲روزه و ۴۰ روزه نشان داد که ایران به جای تمرکز بر الگوها و عوامل سنتی مانند قدرت موشکی و نیروهای نیابتی باید روی عواملی جدید سرمایه گذاری کند. از جغرافیا گرفته تا تنگه هرمز و وحدت داخلی می توانند مهم ترین عوامل ایران در ترمیم بازدارندگی باشند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221230</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656865" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
لابی گری آمریکا در شورای حکام علیه ایران
رویترز:
🔹
آمریکا در حال لابیگری در بین کشورهای عضو شورای حکام آژانس بین‌المللی انرژی اتمی است تا از پیش‌نویس قطعنامه‌ای حمایت کنند که از ایران می‌خواهد آژانس را از سرنوشت تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده ذخیره‌شده در آن مکان‌ها مطلع سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656864" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای ترامپ: ارتش ایران را به طور کامل نابود کردیم و فکر می‌کنم که فقط ۲۱ تا ۲۲ درصد از ذخایر موشکی آنها باقی مانده باشد
🔹
برخی از چالش‌ها در اجرای صلح سریع نیازمند تغییر ریشه‌ای در مواضع طولانی مدت تهران در قبال آمریکاست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656863" target="_blank">📅 17:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656861">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdvsJzXnUe9Jqs13vaj30Jndv6jS-iSsb_guRipfDqR_veG6hcIvWrnWFrqqMus9NNpUIhbgw-0czkGfdayOBKEYV9bjBHkUDRjBrtqb3RAWLK0YoJM992rUYzb-SK8MZekgGl_0iHYeeBIngFLfaSxwBKIq3-k1jCjc7fJ9fE0A5kSOxc0YuiuH1RKpAHeS7MEoJg8NgnEDAjbzLMYYOjjKlynHUP_jRlJuwG_UuS846-Ua_pN5Od7YiIbNgSiXxX_9na5vKE_D14D-2E_v9XIaPuiXomYOFyl90kcMw7Y7Jsh1UVklbZy8WC5phZPQWDurg-xOLLhcgqSpsmmy1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: نیروهای مسلح ایران «با قاطعیت و تمام توان» به هرگونه حمله احتمالی پاسخ خواهند داد
🔹
آمریکا باید غنی‌سازی و دسترسی به دارایی‌های مسدود شده ایران را به رسمیت بشناسد.
🔹
تبادل پیام‌ها میان دو طرف همچنان از طریق میانجی‌های پاکستانی ادامه دارد.
🔹
آمریکا باید تحریم‌ها را متوقف کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656861" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656860">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ترامپ: نیروهای آمریکایی در منطقه باقی می‌مانند  ترامپ در گفت‌وگو با ان‌بی‌سی:
🔹
خواستار اضافه شدن بندی به توافق هستم تا ایران نتواند آن را دور بزند.
🔹
نیروهای آمریکایی تا دستیابی به توافق نهایی با ایران در منطقه باقی خواهند ماند و حتی در شرایط آتش‌بس نیز…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656860" target="_blank">📅 17:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ترامپ: نیروهای آمریکایی در منطقه باقی می‌مانند
ترامپ در گفت‌وگو با ان‌بی‌سی:
🔹
خواستار اضافه شدن بندی به توافق هستم تا ایران نتواند آن را دور بزند.
🔹
نیروهای آمریکایی تا دستیابی به توافق نهایی با ایران در منطقه باقی خواهند ماند و حتی در شرایط آتش‌بس نیز قصد عقب‌نشینی ندارند.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/656859" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هشدار گروه هکری حنظله به ساکنین اراضی اشغالی: برای حفظ جان خود، فوراً خانه‌های غصب‌شده خود را ترک کنید!
🔹
زودی موشک‌های سنگین خرمشهر بر سرتان فرود خواهند آمد.
🔹
تمام مختصات محرمانه توسط حنظله به یگان‌های موشکی سپاه پاسداران انقلاب اسلامی منتقل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/656858" target="_blank">📅 16:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI1WVtdvursAJVKYJ7v-P7KUx9wtbocasvUsnw1JR5GEi4o0wIrdxWIm977llWS-kuMjPETwIkD92pdBmKOUS5RnzN1pE4bgzlvg8GNU9vkOvJR63gXJwnuwaqJMJ80J5Z2iP05V4ynzjBMdrm_BtuKp53FIcixURpBjok92wg3xZq25CY_rMeSqqUhSx9VFCTmfwlWcMs9Ri2HualX0wdm8ABEvTisEL2q0J_zOvk6-_jHbEPhpmgfff1KhcVDssa13dSW6_VUzIB3q8MysC80whODMvpuZ4f6fHGlXAQonMLVdyhNyEaREgnxaxxdu5DnphMrro_a6zdhxZulQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXnEdcdhpmHgPrMkDbVJt_fqvECQx_5l9I6gKp6fFSgVEGvireGCobwOs37pylnOlHQh6cTGgXB4AZ7qnYigsIFgpn_3jgT1GeoP1-OmKoLj6Fzb7S4myyOiSS8v6_wTuYXhk0DCY6vrjDCdO_2_c5qjBF-0Q-CL_UxiVZrOqvcs7RmpXQ4aJSj9X93rSfBd5Hpehdl2w66CMdTopp0YJh8cg82-p_AEty1GB-pEAJlwBSgisvumArRro88iKVTkdP8UaPf43K6pWEruqJTsQAfx6hqGm65ndaCb9eVQYqO7i_8n2ZkU-Kl-6Dz6BGsAJckmMlcn5cn5q-4T-69olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyzRF04oVknk2kWKzTBgXtKojisNb1P6Gc_aTBVP80alhiEeDC1Gm3k530STUDU7y33lSIj8Q0GLr-8VqZr1pmE-awt_DmwVhUgTI3AxjbUpOa1ZpbxIK43yR1hYSeqpBYwE_Wzd_A2P3YdocSuqNTCba9RhAjagGI0dIkj6j0dAdgLr-uzkbM__aGxSOwAIYvp67yZwR3kmiDezFONGEPNWq3kM236-ajX9QeBBodHEKvmrn5MX8cYS7bZEq7Cjsb_YPK4d1xhJxhJOfBQk_ol9-16zT16I7rxhRjNvbyCWkfVhOMfOKcobqHTPq3NbsEyARg2CUz4uvJ2V77_2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ2o8h98HDjqEQY1ydY8lMVfOB1JxNSiBA0Cr6aCEm2-jSuHUw_kZyl7F0Mp2pw5AocKvZho26J5thjS2OvzBCFYfKwYYfVlAI0x0-aS0gO0UOsHURHwytVE6eeVdXOcRSenDeFfXvfbO--XIKzOjpExOCM0B3dOi-MdTqUdOVGDtsesNJkJVGqNTb9V2dvIHEUlpMqDrvuh17sC2bebDzc5dx6g__2oAkg-Ex4owh50XMenLls6D9yGxzKl9YRklyWO7pSNI-HppyN4DWGstyit8qqg3mcvTkQyixuM8kDJmB33SJ19ALZRREIZLeWG-_6tQ_Wa6XIOn36W3WP2kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازگشت با شکوه فلامینگوها بعد از سالها به آغوش مادرانه و مهربان دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/656854" target="_blank">📅 16:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/656853" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656852">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e712b63f4d.mp4?token=gw4fqZ-vlIPeoETpSS_VkdcLE1lVlowdXVQEgYvf9SDz5ViPdHYGuWIak0mFrsF2FOg2IZJLJqcwPqBUmwlRTAwzDat6bFx18ELNXGwQVZDh0RH3cqMpRRBfLTfKzFdpFS8cV7HKhq4oTTLy9qZudYmq6HxrJD27uBe1PxUcpKPYlkKozaNDa3211diIchWgxuBWl13UV2hGLS0OMsOh8t29yHOloIV6BVDvKPDakPkwhIcFjXs-V66REmwiq6O_HbObcXF3exylMZA1Z96fHFPJrawod2qt1qXkXXfMsv8JNnPZpTqpyfqQgrePsqAcQN7i_N4O8uyLoKaNsyYwFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e712b63f4d.mp4?token=gw4fqZ-vlIPeoETpSS_VkdcLE1lVlowdXVQEgYvf9SDz5ViPdHYGuWIak0mFrsF2FOg2IZJLJqcwPqBUmwlRTAwzDat6bFx18ELNXGwQVZDh0RH3cqMpRRBfLTfKzFdpFS8cV7HKhq4oTTLy9qZudYmq6HxrJD27uBe1PxUcpKPYlkKozaNDa3211diIchWgxuBWl13UV2hGLS0OMsOh8t29yHOloIV6BVDvKPDakPkwhIcFjXs-V66REmwiq6O_HbObcXF3exylMZA1Z96fHFPJrawod2qt1qXkXXfMsv8JNnPZpTqpyfqQgrePsqAcQN7i_N4O8uyLoKaNsyYwFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مکزیکوسیتی میزبان موج مکزیکی
🔹
هزاران نفر در مکزیکوسیتی برای ثبت رکورد جهانی «موج مکزیکی» پیش از جام جهانی گرد هم آمدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656852" target="_blank">📅 16:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656851">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">100.jpg</div>
  <div class="tg-doc-extra">9.4 MB</div>
</div>
<a href="https://t.me/akhbarefori/656851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
فایل با کیفیت روزنامه خبرفوری که با ۶۰۰ تصویر از تجمعات مردمی طراحی شده است
@rozname_fori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/656851" target="_blank">📅 16:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656850">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJUW6f5bC0w_AH4aCj11-sacksjSWNbRwtnY4ltvApL8ch1_ilRPTDTEJiFH214m9yPHSOnJ1XNI8QVR73we4YtE3Vq37fdU-xZUtaojhsTTd1H9uDc-rGVfOIL9VtVPqh7JR-zi11TMKQcdNrFo8nR4bmbezeBxVsquNtTbXCvkhYDIJsU1N-jEm06QEiMNS2HS21arlQ7ubGuh0epw_S_7MAU7DAd86_OAE6QAcwEriCeDA-VB8mzRBNQZGrkPHkMXnox603keX81Pirrwbw6uwh4yWWMPcFlj7SIb3aFe1KyaW_OsvOSA1G8waK_kLq1FCgA6OfiBrgNLLaMh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ ایران
🔹
صد روز از تجاوز آمریکا و اسرائیل می گذرد و صد شب متوالی است که ایران در خیابان نفس می کشد. از نخستین روز تجاوز تا صد مین شب مردم پای پرچم ایستاده اند. نه برای شعار که برای تنبیه متجاوز و پاسداشت وطنی که جانشان است. مردم در خیابان دشمن را بهت زده کرده اند. آنها که خیال آسان تسخیر ایران را داشتند، اکنون در برابر اراده ملت زانو زده اند. بافته هایشان پنبه شد. این حضور حماسه ای است که معادلات را به هم زد. صد شب در خیابان به دنیا ثابت کرد که ایران فتح ناشدنی ترین سرزمین است.
🔹
طرح جلد امروز روزنامه خبرفوری متشکل ۶۰۰ عکس از تجمعات ۱۰۰ روز اخیر ایران است
🔹
هفتصدوشصت‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656850" target="_blank">📅 16:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRF3drwUMgUKw19AA8GYq6Z5IyeQtmPILted4zt_teuvDhGUAN6idLPvkq5plMVa28yhkanb9Wot2lp71Rl1uRKWu1pyIB2HLvE-qJq_hlzsCnmh5w0mpibq8wGDxwFPn7VKdP5bJI5yeL7Y6Xn17JSW7KzULlcWsBJuPV6pdq6k1YDHrmH7BmrwddwxOISUKVrETEYsy1pWeTIdKhsWYI59t-I4Z88lTC23JePF3HBJq1R7Zr8NVLPVJJ0FFbOWFpGopvw4-wKWbtmV3KqtshpP2JF8NVt88OPgUpIubxbl8nWbN78KorK_atet_XGjL5qBO-48NZ7dRAYRJ3fr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656847" target="_blank">📅 16:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نامه وزیر اقتصاد به معاون اول رئیس‌جمهور درباره افزایش اعتبار کالابرگ
🔹
سیدفرید موسوی، عضو کمیسیون اقتصادی مجلس ضمن تاکید بر ساماندهی و افزایش اعتبار کالابرگ برای دهک‌های پایین جامعه و حمایت دولت از اقشار ضعیف جامعه از نامه وزیر اقتصاد به معاون اول رئیس‌جمهوری در این خصوص خبر داد.
🔹
به گفته این عضو کمیسیون اقتصادی مجلس، سیدعلی مدنی‌زاده، وزیر اقتصاد در نامه‌ای به محمدرضا عارف، معاون اول رئیس‌جمهوری بر لزوم افزایش اعتبار کالابرگ تاکید کرده است.
🔹
لازم به ذکر است که مسعود پزشکیان، رئیس‌جمهوری صبح امروز در جلسه شورای هماهنگی اقتصادی دولت دستور افزایش اعتبار کالابرگ را صادر کرده است/تجارت‌‌نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656846" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی می‌گویند این حمله با ده موشک و با استفاده از دو جنگنده صورت گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/656845" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3xCqjveWU_gYosFiAp-dgQT3NIKZBDOq8IKvXApXxNZj67le4eGlC0l3Y7Jf0x2HysFlPtN4wBYicWC89nXXOE_3yglmIOGgbYaSjXpGuBSjLgrtwdiNf2m-n95AtoQc6NrbDd9oi6FoMetRAA_nysK_F-BA0MPNd--6xQXkVFYGVZoQgkI2OQ3XjrabadaFSiYQcbVzoFQRrql2fej79CJiLPAoVLsKIT-S27ZaaV66t7mCnbZuooIC4W3WCtXabfxAnJnyrMWYcvOC8MAcNXwtKaKl-uRZ9iChYJYBA9SMA6_ft5o4R9k0WkfvSndu0T0Nas2cjxLWHPNBEOP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام جزئیات طرح «شهرآسا» بانک شهر؛ از تسهیلات ۱۰۰ میلیارد ریالی تا جوایز نقدی یک میلیارد ریالی
🔵
مدیر امور توسعه بازار بانک شهر از اجرای طرح «شهرآسا» ویژه پذیرندگان و دارندگان درگاه پرداخت خبر داد.
🟡
به گزارش روابط عمومی بانک شهر، رضا قنبرزاده با اشاره به حمایت‌های بانک شهر از کسب‌وکارها و فعالان اقتصادی، به جزئیات طرح «شهرآسا» ویژه دارندگان پایانه‌های فروشگاهی و درگاه‌های پرداخت اینترنتی متصل به حساب بانک شهر پرداخت و بر مزایای گسترده‌ این طرح از جمله تسهیلات بانکی، تجهیزات جانبی و جوایز نقدی تأکید کرد.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656844" target="_blank">📅 16:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSRWPvAdpXefuqnJb4tXbxTXWcAUbn10dpfc9Ol4QcvG2uqV596GunnlrHhB1uVH7KuXOOjBSi1XfSumFbQvvViVwgijaL4cQlmlMZR1WiPH3SyNUayMQYZTaejDquKjsfECVtJDzcfY_-Km-xPud7oeQaRqzaEZUM3ahF3j3axBZyRk7_FzSlF3kuBh3VVfzfTk-muJeWxqRHlDsHD6Ze1hHQXmTqjF6WMX936hO5N43cy22OLK_eTi2uSMiKDVEEK2N_NEEjIUEQ7Jme-7MvxXbdb9D3hLpbvCS4mTtzpBL6CuuJDxbGew3RKRH0Z7rubNshb92wsAh2fgDKeqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حدادی‌فر سرمربی تیم ملی جوانان شد
🔹
پس از حضور حسین عبدی در تیم ملی امید، با پیشنهاد کمیته فنی و تایید هیئت رئیسه، قاسم حدادی‌فر به‌عنوان سرمربی جدید تیم ملی جوانان انتخاب شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/656843" target="_blank">📅 16:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
♦️
حمله به «ضاحیه» بیروت با چراغ سبز آمریکا صورت گرفت
🔹
شبکه ۱۵ اسرائیل خبر داد مسئولان رژیم صهیونیستی پیش از حمله به جنوب بیروت، آمریکا را در جریان آن قرار دادند. @AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656842" target="_blank">📅 16:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تصاویری از انتقال مجروحان به مراکز درمانی در حمله وحشیانه رژیم صهیونیستی به ضاحیه بیروت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/656841" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
بیش از ۳۰۰ نقطه از آثار تاریخی ایران در طول جنگ آسیب دیده‌است
خسرو معتضد، تاریخدان:
🔹
بیش از ۳۰۰ نقطه از آثار تاریخی ایران آسیب دیده یا نابود شده‌است.
🔹
هدف این اقدامات، تهی کردن ایرانیان از هویت و فرهنگ خودشان است، این بمباران اماکن تاریخی حماقت است؛ هیچ‌کس تا به حال چنین کاری نکرده است.
🔹
ایران با مردم یهود دشمنی ندارد ، ما باید در تلویزیون برنامه های عبری داشته باشیم.
🔹
کاخ گلستان فقط یک ساختمان نیست؛ بخشی از تاریخ سیاسی و دیپلماتیک ایران است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656840" target="_blank">📅 16:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4706c6d2d4.mp4?token=VIOfALuI3V1vBQ7Cb3rD0BehFYTweMB6fBU74GqDFsb5Id-9poBCmf0hGrgbmqki-bJBVg1qGwBeOASEpFYIq-b7hlaxOJTSFkEbvWR13HfPa2N6sicgz9WcXZNihqow5FUvxSmJq9X7Yxz-94BsGdfPyHTQWrnELJcaEIZ145gjzGY8cWl5gpG6hZ2kkRzEnFthT8HGUSnVg4L-PmR7pd1pPz0UbDbmPRdOfx2aOOBtdLjuP_iPBGOGXb1RZElgk9rLik1a3EdBmyHWX2gkXn5xJ-4EQjsukDOiGY9I9SONsalQnoOqt_GeYP0dndsZlVcIRAACLYidl936iMYe-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4706c6d2d4.mp4?token=VIOfALuI3V1vBQ7Cb3rD0BehFYTweMB6fBU74GqDFsb5Id-9poBCmf0hGrgbmqki-bJBVg1qGwBeOASEpFYIq-b7hlaxOJTSFkEbvWR13HfPa2N6sicgz9WcXZNihqow5FUvxSmJq9X7Yxz-94BsGdfPyHTQWrnELJcaEIZ145gjzGY8cWl5gpG6hZ2kkRzEnFthT8HGUSnVg4L-PmR7pd1pPz0UbDbmPRdOfx2aOOBtdLjuP_iPBGOGXb1RZElgk9rLik1a3EdBmyHWX2gkXn5xJ-4EQjsukDOiGY9I9SONsalQnoOqt_GeYP0dndsZlVcIRAACLYidl936iMYe-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی هدف قرار دادن اتاق عملیات حزب‌الله شد
🔹
وزیر امنیت رژیم صهیونیستی مدعی شد که نیروی هوایی این رژیم اتاق عملیات را در ضاحیه جنوبی بیروت هدف قرار داده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656839" target="_blank">📅 16:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656835">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAm_2ApwqQ96orZtqf_rq2r-6I2gk_Hx4Kwdi9p4HCV-qXpS01gjgv2OEUeNMyafTlu3eK3p2UywzogSkOJ8dPQaVtw0hh_Ju6vQ2o6ERSIxqq-BoQXHIDdgBe6y5LwtqgC9k1DPMbbSM9Ar2rADcP4PHxd3r_tADc-lGPCc7aSroH8V4xlejhzTLeZIXo-7mjdcBsi57LjumdKwG1FYAxLTcMBS1A8hd_nO8HnDk7ehYWwY2nO2af-C3KGg3kDJqJnxlWzFzpnJHW1p0UPU2eeG7itkJh5nrwFgFrXZ2aO_YbbaEPyk11J4trHzx_l98UXenGPuQJ7fwBzqT2-LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyDwtc94dN_4LrbDaeiG8MUc8G4D4DkDskNmXYA5pn_ZoOfErqvUe0PHMdM7tB0DmTjZo5q10kT3hAcmiGqZHaZodn19ITI1ajQcbIhj-xfcXlhOq3MsWhohcdTr6zZ2KeVJPrriKO9VB0y2kCB9BEET_16ClMXETeL0JzlqrGLFfHHbNdiZb4sDaMK9f5e1gsblHeWcqU7POgv7shcyDDNDLMonExq1AIGxd6gVhSC36OR6cVpEX5T28gIZwop7mj6ZIulD45Magy66psasm5R1lTUCipnBrtZpwdr7vAGbz3KRzzrVs71J5Fb3ejGEsmEAR-qZqzxqIuGXOmyLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7R_1asBJDBgOBJGEEwPOGWkQpZ8SnVCfQdTO5oUOP_ggGt6UCmiL19NHwEw0BqDD5tf2p3HVwok3MlxHLVnXadF9BDAaj5Da06aZdTqSqRhneZJ-1EMagN_rfP8Tfnz1h7Y1l_j9xHMyMenK8bQmUTebwMN6hCWh6bLwnocu5SEAclf55SKaUFWV9p8Jy3xrWohc-6zb8eCY5yVoCnG3Qjc1Kp5bIlo97gM8lJyTyNT-FBEm_CapSmPQTwddm84rsyAOB-uihPIK0X0lFAnnuMQN5oiHKjxdpkt3QuQfUCaOhfrpz-N2Tyd2gAV_TB6mnC9wVLyzJjHGMiPjm9WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj5rlvRwRv-FtaUxXhgNMR7k7TeamfOwZgcDqoOsu58I5fogb3G18krF5QrndcONYIKd2R1FcgTGhcv5RfCXqf5EuWU3myvh0RE2LgGJuro9sTsgguHChEK7iEzOZW_3bJ6PHlF2URs1ArWf8SS5O1fKzsyKIiwbQRPVfwVXhddsRmuWpHY9u9M5mTk91hwXi7e79gL9rhsm8YJ9gN-XLN9kqjcML0dP7t5gs0hZUxvnaG459zRA9XdkX9N8QyNgJzG885p3_fMHRNpoui7X49vt3SNG52hTjJVRdx0zh7UftC-dzi-lZt0LFIBq38OwmZ-tTBBpTWFxqBY7V56Klw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هوش مالی بچه‌ها رو به این ۳تا بازی تقویت کن #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/656835" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656834">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تکلیف افزایش حقوق بازنشستگان مشخص شد
🔹
درحالی که طی هفته‌های گذشته میلیون‌ها بازنشسته در انتظار مشخص شدن وضعیت حقوق سال ۱۴۰۵ و صدور احکام جدید بودند، تأمین اجتماعی سرانجام اعلام کرد احکام جدید بازنشستگان و مستمری‌بگیران صادر شده و از عصر امروز قابل دریافت است.
🔹
در احکام جدید، افزایش حقوق سال ۱۴۰۵ به همراه مرحلۀ سوم طرح متناسب‌سازی اعمال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/656834" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186c03c558.mp4?token=WWBvxREJnqfYOrnCI32soHv2ev8J7P9kyLvQDz83cThiLR0uSSdYDcBnSvlSd-PmSeoynvevsjqWZZuCHjMsqb55gfKkg1rsyR6gRPuK8ztqbSSCPwXZyl5mPhcqnIk5jHakiIlZTIF6O8IWsir-_JGnFqGhJmVgtFoZTfvsVFK1p81VoHFUYm5R7LZhmjBiRg8WQY9c5BRMRpI-nOXuQ4IRXtTy1-g-NSMBIdhyBSvi2DWdX2Eov_B84qmf0DEgLbKjAsLZIiHOqZ8XHfe7ixHohwFLENgPw2tz0RJKTgPvcNdqWexeX8FPbQnueh-0X39sG-U0JWwqo8W1zkOIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186c03c558.mp4?token=WWBvxREJnqfYOrnCI32soHv2ev8J7P9kyLvQDz83cThiLR0uSSdYDcBnSvlSd-PmSeoynvevsjqWZZuCHjMsqb55gfKkg1rsyR6gRPuK8ztqbSSCPwXZyl5mPhcqnIk5jHakiIlZTIF6O8IWsir-_JGnFqGhJmVgtFoZTfvsVFK1p81VoHFUYm5R7LZhmjBiRg8WQY9c5BRMRpI-nOXuQ4IRXtTy1-g-NSMBIdhyBSvi2DWdX2Eov_B84qmf0DEgLbKjAsLZIiHOqZ8XHfe7ixHohwFLENgPw2tz0RJKTgPvcNdqWexeX8FPbQnueh-0X39sG-U0JWwqo8W1zkOIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بنیامین نتانیاهو: در لبنان، نیروهای ما تنها در هفته گذشته ۳۵۰ نیرو را حذف کرده‌ایم؛ ما ارتفاعات بوفور را تحت کنترل گرفتیم؛ جایی که یک تونل عظیم زیرزمینی کشف کردیم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656832" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CG6wp6VNTMYTZopQUdazHxnzSHiEFtc1fnKRvNTdqHCLq6Eky6XwSLyj6u7qZDBlxNkZEnE6bw_Z4-jTBqhxp7olo54-3sp008dBkProW9A9pbws7Pl_Er0EmRgUO3HHsPKTjw-hoelflET6Es-c_cruFfECfHvkBgh2NNglu0kQsEWsCrIQy7PSeoYtkk4Hq3yUL52Z8eYeS_huRO85AP4wv1sPbizOnN00A7Df9qmiIz4f4anQTv7Fcpvj1ZwNrHifuBsogHv-z395SBR56ima7fvRrMFnYirDiFXKqctTjyY_s-mMGqfLiimIQ_sT3ogo63XML6L5_cDSomGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YobEf397A69ZbRNW0yhdQx4QqQw2aQNIP9oPqMZVICBqxALHU1b0DmEIs2hnPwKsQyoJOGISz4VWG98u-pmwIavDNb7ByyrGFsd3Lj409b8cwmBeNLKg9dYMtzpvLRMzfyrAyPzmuwWOqo4zJu6dLH7db-ieBK-7RRO9uo6Y-iSaADd4eay6ttiF5Y5vrp16VjCBN9Bhu5XJpRKi5eGxPftQIcCx-JlaK92x5KegF2nV9E8mgnvzVXS-iPBARgI9LZX10_kCBXl-y87BMiPjDJZNheh8rD7XXqsilc1DyqSIh70mZKe4kalemeq77Dx-RHk7_mKSperSgXIyUYPFqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/656830" target="_blank">📅 15:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/656829" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16df92bf92.mp4?token=b8ef07wSkpwh6mIIybs2Y0-sNHxsILsAH5eh5rngMmulXX9lNB6O1MBIvaZcAlUVqq3jQbniUpUJxqY17Tl8UlqQ_uc8IJOC6LYZAjRrfprAit84GGoE_GeWjUCFxq3Lj3wcCqlTG72Z6c6BgExWwDBmYfvjmunXx4io_XK7Ua5ZVcGREhDYLI0oEG9aYhdCEnE4ZzZ5bPUk5tkvvIGAEq4Zca7osrGamlrBRduXxnvPj4a7iHVZeC4PKAdBd6h-vMRAwSq2d-NED4TTCnnyxiNQoCesuuDC3Mp405jOJQMH4O2yK27kRsO78oowQutvU2E0ZEJUqJt7BPO1e3fhOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16df92bf92.mp4?token=b8ef07wSkpwh6mIIybs2Y0-sNHxsILsAH5eh5rngMmulXX9lNB6O1MBIvaZcAlUVqq3jQbniUpUJxqY17Tl8UlqQ_uc8IJOC6LYZAjRrfprAit84GGoE_GeWjUCFxq3Lj3wcCqlTG72Z6c6BgExWwDBmYfvjmunXx4io_XK7Ua5ZVcGREhDYLI0oEG9aYhdCEnE4ZzZ5bPUk5tkvvIGAEq4Zca7osrGamlrBRduXxnvPj4a7iHVZeC4PKAdBd6h-vMRAwSq2d-NED4TTCnnyxiNQoCesuuDC3Mp405jOJQMH4O2yK27kRsO78oowQutvU2E0ZEJUqJt7BPO1e3fhOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/656828" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران به تیخوانا رسید
🔹
تیم ملی فوتبال ایران پس از برگزاری اردوی خود در ترکیه و برگزاری چند دیدار تدارکاتی در راه آماده‌سازی برای حضور در جام جهانی ۲۰۲۶، از ترکیه عازم اسپانیا شد و از آنجا به مکزیک رفت.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/656827" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aebb5eb86.mp4?token=wCaTyY0V9z1i4832V4UfyT8eX3paLGjLQA1qBFKnZm3bglT3SN1IcocNIt4ZRi_GUmJFCUTdKJci5WOge1bV5cEwNZNFrmlgj3WBpllWEQ9PLhQ8zCfo_1LRy2-NdprzS5sT6Zm4ZnSZWwyp4y_EwJZ9coAB63yXZN8jvPGWY_HQClAEPrwRuTO4uWsgVCinRKYpT_dSSe8ilnHX2JgQNBdvMa5cBA0bekrD-WnQSVyO4AQZNduvOX8A7CI777GiwbKQ66greMJqcwEw9IjeXoBbtLeTtYyAVUI5_tAFeqnbXT40WFjTL7LtmQJgHvCr-Qhc0tES6diuxoIdOIlFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aebb5eb86.mp4?token=wCaTyY0V9z1i4832V4UfyT8eX3paLGjLQA1qBFKnZm3bglT3SN1IcocNIt4ZRi_GUmJFCUTdKJci5WOge1bV5cEwNZNFrmlgj3WBpllWEQ9PLhQ8zCfo_1LRy2-NdprzS5sT6Zm4ZnSZWwyp4y_EwJZ9coAB63yXZN8jvPGWY_HQClAEPrwRuTO4uWsgVCinRKYpT_dSSe8ilnHX2JgQNBdvMa5cBA0bekrD-WnQSVyO4AQZNduvOX8A7CI777GiwbKQ66greMJqcwEw9IjeXoBbtLeTtYyAVUI5_tAFeqnbXT40WFjTL7LtmQJgHvCr-Qhc0tES6diuxoIdOIlFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات عجیب بدرقه تیم ملی به سوی آمریکا؛
یک دوربین علنی و ثبت جنجالی‌ترین اتفاق اردو!
🔹
دوربین شبکه DRM ترکیه لحظاتی از ترک هتل آنتالیا توسط ملی‌پوشان ایران را ضبط کرده که صحنه‌های آن روایتگر مکالماتی جنجالی است.
🔹
قلعه نویی: برو بهش بگو فلانی گفت دیگه تو اتوبوس تیم نیاد!
🔹
البته که به طور واضح نمی‌شود از این فیلم متوجه شد که قلعه‌نویی از چه کسی عصبانی و ناراحت است، اما می‌شود حدس زد که منظور او امید نورافکن است. در ادامه این مستند قلیچ‌خانی برای انتقال پیام قلعه‌نویی نزد مدیراجرایی و مدیر تیم ملی می‌رود، جالب اینکه ثانیه هایی بعد مدیررسانه به صحنه می‌رسد و با متوجه کردن آنها نسبت به دوربینی که مشغول ضبط تصویر است، می‌خواهد که این مکالمات پایان یابد!/ورزش سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/656826" target="_blank">📅 15:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ثبت‌نام مسکن استیجاری زوج‌های جوان از فردا آغاز می شود
🔹
با اعلام وزارت راه و شهرسازی زوج‌های جوان واجد شرایط می‌توانند از ۱۸ تا ۱۹ خرداد برای طرح مسکن استیجاری ثبت‌نام کنند.
🔹
این طرح ویژه خانوارهای فاقد مسکن و دهک‌های درآمدی پایین تا متوسط اجرا می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/656825" target="_blank">📅 15:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شورای صنفی نمایش با پخش بازی‌های فوتبال ایران در سینما موافقت کرد.
🔹
بقایی: مواضع متناقض آمریکا مانع اصلی مذاکرات است.
🔹
سیدمصطفی حسینی، مرزبان خراسانی حین کنترل و مراقبت از مرزهای جنوب شرق کشور به درجه رفیع شهادت نائل آمد.
🔹
حماس: در حال رایزنی با مصر، قطر و ترکیه برای تضمین اجرای آتش‌بس هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/656824" target="_blank">📅 15:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
هزینه‌های ثبت نام کنکور و مصاحبه فرهنگیان سال ١۴٠۵
‌
🔹
ثبت نام در کنکور فرهنگیان: ۴٠٠.٠٠٠ تومان
🔹
هزینه مصاحبه گزینش: ۶٣٠.٠٠٠ تومان
🔹
هزینه مصاحبه ارزیابی: ۶۷۰.۰۰۰ تومان
🔹
آزمون عملی ورزش و هنر: ۵٨٢.٠٠٠ تومان
🔹
هزینه معاینات پزشکی: ۶۵۰.۰۰۰ تومان
🔹
ترمیم نمره به ازای هر درس: ۹۵.۰۰۰ تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656823" target="_blank">📅 15:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXxL2KTddLb1xRjm4JbsduwlSi1oWB52pJ6mlLaIUP1kghLjQxSZjvfpZkO81KwqcHckSbdHSTK_KdOqQ1_IXWpzmJcuIomUTTUhm4BWbLed_vty_q7NzmGes5rIgaLRS-DYFNLrns3BlTcdUin1DTaSuE0f_7tcS3c2F-jPsyhcy3p_wkXzBAu05xAEDxYWyHjBl0KmCq7GToGLwS0NILkmk98p4fIet1VHtVYVzLcg8zJJ9Ghu_wqJV6HFxdlvYb2PvVURJ1FnzZAcjVGBr1WuAbIPvwZKErcxSibsIO8oHUQ_a6Sn5C1xbDM4y6z14ylwezTtUcArdQEtocF_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جعفر پناهی بابت فعالیت تبلیغی علیه نظام به یک سال حبس و ۲ سال ممنوعیت خروج از کشور محکوم شد
/تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656822" target="_blank">📅 15:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دستور پزشکیان برای افزایش اعتبار کالابرگ
🔹
رئیس‌جمهور بر افزایش اعتبار کالابرگ الکترونیکی و تقویت حمایت معیشتی خانوارها تأکید کرد و خواستار به‌روزرسانی و یکپارچه‌سازی اطلاعات اقتصادی خانوارها برای تخصیص دقیق‌تر یارانه‌ها شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/656821" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مطالبه بازنشستگان کشور چه باید باشد؟</h4>
<ul>
<li>✓ افزایش و همسان‌سازی حقوق متناسب با تورم</li>
<li>✓ پوشش کامل هزینه‌های درمان</li>
<li>✓ پرداخت وام و تسهیلات قرض‌الحسنه</li>
<li>✓ ایجاد امکانات رفاهی و فرهنگی</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/656820" target="_blank">📅 15:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7af76ab1.mp4?token=tzY7YfbpajGjDr82EpN0946g29j-BbuM-SAx8Ki6_dgVOLxi7I9OJeCr-vtYq_gnx8kRS5M0vijg9zRuI2EfEmcBfPZRi53CLWjIBImsXXC5jib84LkbkwlOQ7_75l5lweXxy0HPZEf_RwzwQuuBWLoLVnzKBith4pwih2ua26VX25QLIzRBCvCVTH_NJap8uLg7BRg9kZc-xc4oL1kRWzB3LYbr24eY_yjyzBWwMw_F0aynVirvCTRHf2yTXT1HaufjZOjq0NEEp_kG6NBN3gTxBdLvbr7Vh5tHDVzEwf6aK-1iIBfLypXHtNVqJyxhZQCZHIDGZzYC9Uh2v-gvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7af76ab1.mp4?token=tzY7YfbpajGjDr82EpN0946g29j-BbuM-SAx8Ki6_dgVOLxi7I9OJeCr-vtYq_gnx8kRS5M0vijg9zRuI2EfEmcBfPZRi53CLWjIBImsXXC5jib84LkbkwlOQ7_75l5lweXxy0HPZEf_RwzwQuuBWLoLVnzKBith4pwih2ua26VX25QLIzRBCvCVTH_NJap8uLg7BRg9kZc-xc4oL1kRWzB3LYbr24eY_yjyzBWwMw_F0aynVirvCTRHf2yTXT1HaufjZOjq0NEEp_kG6NBN3gTxBdLvbr7Vh5tHDVzEwf6aK-1iIBfLypXHtNVqJyxhZQCZHIDGZzYC9Uh2v-gvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف طولانی کشتی‌ها در تنگه هرمز از لنز دوربین یک گردشگر در عمان
🔹
ویدیویی منتصب به یک گردشگر عرب در فضای مجازی منتشر شده که در آن از صف طولانی کشتی‌ها و نفتکش‌های غول پیکر در تنگه هرمز فیلمبرداری شده است.
🔹
در این ویدئو تعداد زیادی از کشتی‌ها با اندازه‌های مختلف دیده می‌شوند که متوقف شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/656819" target="_blank">📅 14:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656818">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
اتحادیه مرغ: قیمت تعیین شده دولت برای فروش مرغ، غیر ممکن است
ناصر نبی‌پور، مدیرعامل اتحادیه تولیدکنندگان مرغ گوشتی تهران:
🔹
قیمتی که دولت برای ما تعیین می‌کند به عنوان قیمتی که ما باید محصول را بفروشیم، غیرممکن است.
مردم تاب هزینه‌ها را ندارند که خریداری کنند.
🔹
قیمت تمام شده ۲۳۵هزار تومان است و ما داریم ۱۸۵هزار تومان می‌فروشیم./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656818" target="_blank">📅 14:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656817">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33fa146e1.mp4?token=QahLphQ2I6IGGUYL5IubQhgzH9Wi49yMtB7b_rdfGMGpGASDSAaWgyFzGNr1it4ObFjXeV1BrOfBBp0OP3sHiB6tI05euPinH00xUg-Fa-uRPkeLLk2RGx6U7x_nIKIbP5jhl07ojSBp-qpdTzzCs2AWO3FbqNN-s6XzXEoOyuz2S4qAgw3aMAMtOXmMwIOGpd0Hp9g-vw28hwwRZ1H3wSOQWzANBXk-HfmagNivLN6maSqPE2y91D-KD7iPt_GM-WuMBzeNmh4_Nl2-qjW0APYIh7DccPeMZMJU6lTXGa87XzzCcMhnc11cOPwPXNbKglSTdLULAXXtSXNsDDIFsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33fa146e1.mp4?token=QahLphQ2I6IGGUYL5IubQhgzH9Wi49yMtB7b_rdfGMGpGASDSAaWgyFzGNr1it4ObFjXeV1BrOfBBp0OP3sHiB6tI05euPinH00xUg-Fa-uRPkeLLk2RGx6U7x_nIKIbP5jhl07ojSBp-qpdTzzCs2AWO3FbqNN-s6XzXEoOyuz2S4qAgw3aMAMtOXmMwIOGpd0Hp9g-vw28hwwRZ1H3wSOQWzANBXk-HfmagNivLN6maSqPE2y91D-KD7iPt_GM-WuMBzeNmh4_Nl2-qjW0APYIh7DccPeMZMJU6lTXGa87XzzCcMhnc11cOPwPXNbKglSTdLULAXXtSXNsDDIFsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو یکی نه‌ای‌ هزاری، تو چراغ خود برافروز #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656817" target="_blank">📅 14:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656816">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS_2T7irQNuaQ3qbG7osiUYVpIRafxJQ5lWOeWrdM7s-de1rH6-nKAD52DYK9WA7tozXpmCnS0ojmxE8veG8v2ZtPqo3DEWlm8CjdknJ5cH3_Ru2WQ-Fa6v9rBIuSRCARuRxFo_uGClUcmG3h4pQAh05wZYO_qVLMUJM5zBgDsLg1FV-Jhr8O-GA7L-MfliPJUBGq54Wo2npaw4QkqcLqUEgA_hHuNHpBxHENfmSFus1KTlPQ0BvjFoV2xFKr3dPKvv9Nw9IG4-D9gjkkGRmLNSSfuT9ncN7j5ErsnYjIr3FVXE_dkc8CCjpD7XS3JUk-oCukOBhNd-b2MXOUgR4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بیشترین گل زده یک تیم در تاریخ جام‌ جهانی
#جام_جهانی_۲٠۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656816" target="_blank">📅 14:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656815">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
دستور پزشکیان برای افزایش اعتبار کالابرگ
🔹
رئیس‌جمهور بر افزایش اعتبار کالابرگ الکترونیکی و تقویت حمایت معیشتی خانوارها تأکید کرد و خواستار به‌روزرسانی و یکپارچه‌سازی اطلاعات اقتصادی خانوارها برای تخصیص دقیق‌تر یارانه‌ها شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/656815" target="_blank">📅 14:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9WiQmnGpaFCACQ2AXzz3V2rmJ1Rr2x6-KWyxTAKAsKfnv_2gbO6nX4ppfIqGnJRo_NUpaILKMJsNZ9QI1c1dUcJT12k5iTUnMqC9SQrjWuWObjZF_SnXBz5yRtolbvhfaIR2p4hid9RRKjk4kzB3KoB47RVCtIOEHJQKJUIAzL5Rhz_zSDxRTFuCTOVlM_MJ-QFXeDSI9dIv_DWpRlUQopJEoTmwezQMZmIMmbDjHuAq9jCEH4odfb2257amlnjCtPT-jnruBrqaROP2FNUf2AsZvLUzgagOuoglbNCUctqaO3g4m5uFAtjMgo8d4VePElzh695GtJ96yLD-s5STQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656814" target="_blank">📅 14:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تیزر قسمت نهم از فصل چهارم
🔹
در این قسمت سرکار خانم فاطمه سجادی با وجود اینکه تجربه سفر به دنیای پس از مرگ داشته است ولی به دلیل مسائل اجتماعی که نظاره می‌کند به حقیقت دین اسلام شک می‌کند و در میان جستجوی حقیقت، تجربیات جدیدی کسب می‌کند و با ما در میان می‌گذارد
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فاطمه سجادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656813" target="_blank">📅 14:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfkI2pW9fNnaK6JOlzfuRbRAGY9SrP42CJovapLC7mE4xhFlqRoYD0YzNde3yYJMdapg975h_-D6ArOS2okJdlGwOx9xpEItwFGKBXY2_F1e5SREuSGmD5-CBrmtB-HNgfboe658QI_h7nwKYwf_nQ6Ny8vbhqwzQlDxpahbWP7HTQtRxgLX40Xy0MK-Rlkb8zv6eL7dALdbBmno2VLetpZZPxVPpjwAhjdLJFk9EdtQYB25-sy8_u9s2ospmFNaQ9NeoiFxf-R7x3G4FoWS-Tua3QFV8sx2N0LPhqElakIuCQUDUgoBEw8f7HkfhB4wRTAHKcIWZHJgvVBkW_RKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پراید سوخته ۱۳۹۵ با قیمت ۲۱۰ میلیون تومان آگهی شد
🔹
با وجود آسیب‌دیدگی و سوختگی شدید، یک دستگاه پراید مدل ۱۳۹۵ در بازار با قیمت ۲۱۰ میلیون تومان عرضه شده است؛ رقمی که حتی با حقوق یک کارگر، حدود یک سال پس‌انداز کامل نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656812" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDPrNMs9irvhyxsKzGy4GKYarKHQReHkhfE6i1eHIv0jyB6RXBSrQ8I1SKsI-GPYXkzSgDqUpti2Qm9XLGcBoyHlJolvUrNQLFIDCJp5yzK-M6bviUSfSuQZjqw2V9tbWx-PmJjAu2X31vK3cXg_5qTz5am1qdDCLzsIgF5mSr67dWGlkWxIqeRlC7jTbA6iIxcuCNuqrDjLYNQ29Au7WTwqAJQJwcb-L3ah-litaOmzwHv_W-b91zGREXi3Ct7YwgKKWnTaSUuxlwkzIyoJgrxJnCdZd6-qBrdU1_MPtjfsq6qSn_DZNJpeCK9fx6DnqAQEy0wkVH06gwaAynPbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رحمان عموزاد طلایی شد
🔹
عموزاد در فینال رقابت‌های کشتی آزاد رنکینگ اتحادیه جهانی در وزن ۶۵ کیلوگرم با نتیجه ۱۷ بر ۱۰ مقابل شامیل ممدوف از بلغارستان به پیروزی رسید و صاحب مدال طلا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/656811" target="_blank">📅 13:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
۲ زلزله پیاپی پردیس تهران را لرزاند
🔹
۲ زلزله پیاپی به قدرت ۲ و نیم ریشتر پردیس تهران را دقایقی پیش لرزاند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656810" target="_blank">📅 13:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvbVPYrbTNngQH65sn88VZHiRDGTinlX0AmjelbUMtGzYZPQBmijaMNM4qgWdZk02SccdaQqdXsbTY3AGEpfPPnT9tBpkBF3Z8JuAiUuudifUbQ5PLgS3fdYshP4cFs-nJ-_5LTD_G_WhjnoWfqx2WYfLskNp3koriOfDin4K3Q0EsPo9bXMij4rNCYYyuYIl5rAd44XXEcD62foCCxbjqOi6YqU_vduKe2efF1O4nRrPjECJM7bLgK3DFS1pZldrvdFCvrd0ueNL4UWPXXBPL26Br3agcDjdbPZzIaSAjyBhKsLlJfzlJcEZfSHdzuI6QWp9PjQ4gjoSXiFORRMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرغ گران‌تر از گوشت گوسفند!
🔹
میزان رشد سالانه قیمت گوشت قرمز از مرغ کمتر بوده است.
🔹
ماهی نیز کمترین رشد قیمت را نسبت به سایر محصولات پروتئینی داشته است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656809" target="_blank">📅 13:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
هلاکت ۴ تروریست درپی درگیری با نیروهای امنیتی در سراوان
🔹
به‌ گفته یک منبع آگاه، درپی درگیری نیروهای امنیتی با یک گروه تروریستی مسلح در سراوان، ۴ تروریست به هلاکت رسیده و مقداری سلاح و مهمات از آن‌ها کشف شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656808" target="_blank">📅 13:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb376fa143.mp4?token=jlRg7qV3Ua6FlDRvSLrB2_M9x_KCwlD14bDEXv3df5-ihwYn6fvxa7RcOK_Y2MImQ3LOJov_Dnla8HTuM4fO3n25N95_N_RSeC1qoOTXRcoPzTHeDeMty8lxO1RWSjivm93WZn2Xsrk_Ynty_qrhRuuIz8IgWCwQ-9UtWetOG4kTh2cexER7JlRGDI3ks0o5MRiIdsiMR_dEXND3UiA39iWZF2-13Lr-mvgXdCJ3GFRHHqpBLyqNXiHt7G0XXZdzKZ5wzlVoep9IJJgqI3gEr1PwsZBY76THw2Upg4KhUdq5R1ReQVDZp3AD7JAaKu7t2FlY0egxSenuXMLkaUDfKgaKuCzG6XOokFIdUuDOgHzAReejfNMErh7odidAQXsOdt2fONmqrIVQLjnbReiT6rreZQKWVvTzboI-ahfvaEVFPsP5Wj32yu3MtpAEqiTc91_g6s65lkwAYY-KfTkFloSKxj3wtlpXPqxZfE6G2W5vpT-pOK6o9lgz5OlBmoHNs4gaQJhX4Zuq5oa3KwhPlPXFjoDsODP8HeT5w28dFGT_OAnBKvZlKnJFsCLFQp1LmHvdbnOCoBmrfLDTlKSVSMuaezIeByr-zDB3YAf3WXyS5a-O30uua6wlqo6FA_YKZ6_JpWZjh1ropY9ZmXTN4X_SQE66nhPkTVQWC8KTY2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb376fa143.mp4?token=jlRg7qV3Ua6FlDRvSLrB2_M9x_KCwlD14bDEXv3df5-ihwYn6fvxa7RcOK_Y2MImQ3LOJov_Dnla8HTuM4fO3n25N95_N_RSeC1qoOTXRcoPzTHeDeMty8lxO1RWSjivm93WZn2Xsrk_Ynty_qrhRuuIz8IgWCwQ-9UtWetOG4kTh2cexER7JlRGDI3ks0o5MRiIdsiMR_dEXND3UiA39iWZF2-13Lr-mvgXdCJ3GFRHHqpBLyqNXiHt7G0XXZdzKZ5wzlVoep9IJJgqI3gEr1PwsZBY76THw2Upg4KhUdq5R1ReQVDZp3AD7JAaKu7t2FlY0egxSenuXMLkaUDfKgaKuCzG6XOokFIdUuDOgHzAReejfNMErh7odidAQXsOdt2fONmqrIVQLjnbReiT6rreZQKWVvTzboI-ahfvaEVFPsP5Wj32yu3MtpAEqiTc91_g6s65lkwAYY-KfTkFloSKxj3wtlpXPqxZfE6G2W5vpT-pOK6o9lgz5OlBmoHNs4gaQJhX4Zuq5oa3KwhPlPXFjoDsODP8HeT5w28dFGT_OAnBKvZlKnJFsCLFQp1LmHvdbnOCoBmrfLDTlKSVSMuaezIeByr-zDB3YAf3WXyS5a-O30uua6wlqo6FA_YKZ6_JpWZjh1ropY9ZmXTN4X_SQE66nhPkTVQWC8KTY2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه شمام تو هوای گرم تمایلی به خوردن غذا ندارید سالاد کارتوفل می‌تواند گزینه‌ی خوبی باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656807" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixlNgBcEGF5nZDvu6knidXDLpGn4H7UJhABAIWQaY8N5Wd0Ufzf95ZczBgx8_aWp1PH9bjaU_anbQiaqBd9iVcy5jQ5O8hl6we3p7hvIcgc8UqOFotBUiRMYTm_rXOZ8OhOvaZiffl6ZiKjXkNAHRFWka-EFmFBEgAB3AAO_qkYyMS42BAG3Pq5DjFNNeEGPekDXgefjWjMYzg1uOxVpkPz9CrGbAUJb9f82XBhdwqUSOT9uJn708Oa4MZVUyDC3rYro031dvjvXBUQbCRDAuTnAMZcy-XvgIjK8nvjtPUGtf7kgiq9MoH7troUT-Wl_s20e8YA6EV-IzEq308is3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXFeIwAZkrTZuzOGEMOmBt2bOM_bcsI3sEFdJ13pVRXWjxCeoECiruapwbfWi-DlxaBqyZ8-lmFGeeu_iPL51DA3NfEMfhEocgu96cAMC478KElQsXx5tKXzjZVtoNRZ9UcIul9hQ-DPPLH9qkcYpzB45npDux2zfiHwaUgQI8fVl_K7AUN0PylMUTQzi0lvsgPr7FsKQb7a_jy4Ep0WJYFRZwiHyiCcWr1nHUJ2o1zoDlNrL4-P8TTs2a2hnv-zyOi17vpD1OGgIZuV_ft9i-pBuin6b0aTca8koVm9jyazBIk1eGFarmoZX5SHRmboe__J1F5XQqzNkys8UEsR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH8xyfgauDjBS2BJZ990k6LmpztS82TkHqx0pGCayYoiYDL5A3bvIH8n2hjmIh4BY4wd3LiToNTLUiBYDZmP5xq3HJz4huvyBTP42F5sL8FRtgYkLCVI3S5uEILjNw5toclunDW_fWM--TK1qKGvQST5R5Cd_niY8L6YNjrr3JYb0jAN6pPj3kBTJTbcfqrTHYxdNSfYprWFqpRvyt68Dpik4xi18m8bj32hHwHrO4j7XjqrZ_TUtlvto3RxDEL7g2HoQ-ShLGfGSy_ZxukRHPRBQYWIefnxUzgLPY3ShUC2vZF57X7vG515-7yq4-uvgOOB1OqV61ZPW0Dfg2NEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hh4JphdZbnfF65-kP53nmYI5-D1NjYad3ABorzxg4uNUSZDXhz4DA_NzNsAccGk0o-LbXAeTiaH_qN67ZLSPv6cHH3Txo6KhNJZr1BOe3_IHZO-YdMXjC3gQJet5vHohSznXPV0ejdZ4Fhlz5iWBm2W7ci4Hm9QQGD0y8iQJkxabT5Y9j7maIVVe5o_VLlKf3b26xpAsAIMOywCy5QVDbZWzM5aShv7U5hhgsSHlUGLVIDF-coLylviYbcZxPjMDk8jI6KgJcw6EF7KWZfJOyDzuZm3DGPZuWl-UA2HdBTek_R_QelbbOze29Lr0VImga3CaPHYM7kMPQYxj87IrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCuoP8ghGNzFQ4JhmxTfmGgjyhzSx3Yjd1zvqD7MuXfFCDgKBSdaZt5o2TReiIKN_iR9wkn1Rd25g2lLbIfcmRyLW36P2_zA3td15cTdDF_rJFhQRdmGwNpRm8gAJLwD7IhUpc2O6orNkG5VE3IXXDz1UPsoMmGV9iy26qrLxNpX8uufJPPev8u3ErnkBDNVx5fCk4R2xuQfVBjUV-zCl8fzq2jXjSDApVadFbrxkV6jgtYuYEn187EzT9UZqRbHuz6rRQWkjG2FcR7h1HH0TZqFCvQJUYJYMHGsAH_j0EAjZrgTmBHbIIQZjbDv9dt9_FjLab5ZZH6KYsyzuWnwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFPCSkkM4BirlpRFqrV6CZaLjjG9fxjbY2699xLU6Ljj88Djr6dHIKbUe7NbQ3XC1bzAH-aeUtZiwlQiCYDzvxDKw1KW--aC03PEXn90Z8vbknZdt6GRBUceTtVrheOf-mnVw1dCCIvZeth0wEQWFzyX_w0wtykVEl7lCPrt5Q37ssRr8O7IP1YNfkZlmCfLTrtfvs7ODU0hx3DM4ldn6rrlpKy4NOpuk9-P9kXXWSbxI3p67r1S0cTcmLSMtSsxLhrrr7MAE5dit3DioprVDVTmcVyOv8eSL4DHXDMWTPbOmPglxW1xfwMurEAbKF0Q__FAkcldkxgE7mPI_mj7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXkwDFbu6BK0HtL9svOkVY57MDrYa87cZG9noNfEnIPphzweSvjsD5bEEBrfbWyIcGUIZs3xHQUFlludGaL_Y297yLmV64FUCNDVuJp052ETUBvQFy7NIzoPFcue7oq2DDMzMCDoHpR1_n0e7SBj6PJBy2JMLGFFXG65AyxtYA-g1pu81a04sU6X5fU4V7Do2FWqnejShjrrbJt65RHRA4e3eCxFX7EoHqCQ0OHCmeukkUkVWCfMo2UrAV7C5URK3kgknObypVLP2nl_4gEOJTXZZU4CTECrepfN9bvbhk0nnpfNNxpT3GwapQYfXMj7hXTUSAcsP4dCEXttuT-kGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت سهم‌های کوچکِ ماندگار
💫
✨
این روزها،
#همدلی
فقط یک واژه نیست؛
حضور مردمی‌ست که کنار
#هیات_قرار
ایستاده‌اند تا هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی، قدمی برای حمایت از خانواده‌های ایرانی و خانواده‌های حائز صلاحیت بردارند.
همدلی شما، ادامه‌دهنده این راه خیر است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/656800" target="_blank">📅 13:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سیر تا پیاز واردات خودروهای خارجی
رسول رئیس جعفری مدیر عامل منطقه آزاد تجاری - صنعتی سرخس:
🔹
اگر فردی یک خودروی وارداتی از منطقه آزاد سرخس بگیرد علاوه بر اینکه در استان می‌تواند تردد کند چهار نوبت دو هفته‌ای نیز می‌تواند در سطح کشور تردد کند.
🔹
واردات خودروهای عمومی نظیر اتوبوس‌های شهری و بین شهری، تاکسی‌های عمومی و هتلی و کِشنده‌های ترانزیتی و تجاری نیز در دستور کار است.
🔹
فقط سرمایه‌گذاران می‌توانند مجوز واردات خودرو بگیرند، سرمایه‌گذار کسی است که ثبت شرکت کرده یا زمین دارد یا در پروژه‌های سرمایه گذاری و عمرانی منطقه مشارکت دارد./اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656799" target="_blank">📅 13:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دریافت هزینه از کشتی‌های عبوری تنگه هرمز وارد فاز اجرایی شد
زنگنه، عضو کمیسیون برنامه و بودجه مجلس:
🔹
از هر کشتی عبوری از تنگه هرمز به‌طور میانگین ۱.۵ تا ۲ میلیون دلار دریافت می‌شود؛ طرح مدیریت تنگه در ۱۲ بند تدوین شده و برای اجرای آن مجموعه‌ای با همکاری وزارت اقتصاد و زیر نظر شورای عالی امنیت ملی تشکیل شده است.
🔹
مبالغ دریافتی طبق قانون بودجه به خزانه واریز می‌شود و بخشی از پرداخت‌ها نیز به‌صورت تتر، کالا یا تهاتر انجام می‌گیرد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/656798" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jroC26yRCQ2AFgNJ3A6m0kEdsZVVDkP3cJmriuqw_N2u_hbH5z-HrYkpUfzapCYUaS2wLh0eGmtTE_qxQDJkZ4CICxxEtPzuoOhaWf_maN7gVkr4Y2Hcs3R8InFeNPX96nOVAkVAt1T7b7gjze4qYPTM9q-JGz5gfyFDFFaNrJ7Ivhq3MKBs4nMDOG13NRL7HHN0n5k-bW-CtDS_Y8OSq4hNy-ixp5A15pWhq8cpvxcX0ICi8JCH0DciEH34nhmtVWmCfmKF-lUqnZ7kddIiHLqM6D1husmThzCX7Yh5km-yvz6y8HCWmw5w3U6FkgenSQ6sveUvuaxSyu82Fx5HCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/656797" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83207df46e.mp4?token=DnyjEfWMRXkZKopmmXfPnFYYqx8Q5uFkcrf6Nz91Zl2G0M-pB9nBUUxyf5hTtQ5c76HsVZHrjhSo3Nir6FYX5dOpUGoNql_4ZVw72UPHIUaZK6fvHcdIj2oVrfMjmmfSzENMGQm9XrqTSqpc0ICiN6rONZte7o2PQlBuHCr77ayv8lnheb4EZg3tzxE0MD9TksW3kD8MEHvW77ayfqthGqPpT7vxTbMGKAgh8bqzzHFB0hn-LZCVjsUW6vTPgfL6qPq77At7uRV2SSZf8ItnVxQAuYW8RVi2_9fA7C2e5Seqnoo2X_mqgVAWxSlXUdGzLCp3VpwU-ul5yQBTj7yBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83207df46e.mp4?token=DnyjEfWMRXkZKopmmXfPnFYYqx8Q5uFkcrf6Nz91Zl2G0M-pB9nBUUxyf5hTtQ5c76HsVZHrjhSo3Nir6FYX5dOpUGoNql_4ZVw72UPHIUaZK6fvHcdIj2oVrfMjmmfSzENMGQm9XrqTSqpc0ICiN6rONZte7o2PQlBuHCr77ayv8lnheb4EZg3tzxE0MD9TksW3kD8MEHvW77ayfqthGqPpT7vxTbMGKAgh8bqzzHFB0hn-LZCVjsUW6vTPgfL6qPq77At7uRV2SSZf8ItnVxQAuYW8RVi2_9fA7C2e5Seqnoo2X_mqgVAWxSlXUdGzLCp3VpwU-ul5yQBTj7yBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونی‌اریکسون با نمایشگر شفاف در سال ۲۰۰۹
🔹
تصاویری از یک گوشی سونی‌اریکسون با نمایشگر شفاف و شیشه‌ای منتشر شده است؛ موضوعی که با توجه به فناوری آن زمان، توجه کاربران را جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/656796" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77f4a7f60.mp4?token=vDffjqh3q-6i80COaMvSrSJmFuUcB5oJODqJlvR4bGg5ujymQuswoyUsv_kUrl9SYDCT1fA9RyT5wUzLia7sm-vdpEZUsfNWtpWQbLCRuMPZG5B7Q6jFas90uu5XCTxAg4JzjW4uH_5lux9zAJDQT3zIFZA4smHf3HhgSntju2WR7xf3auqpg-l3mAhdyTIDVfZzHNlbleipKLaCXcUSZR7NtldiAriF6J8Umt9GXKoHoyomqjPKpNPq8E95pV62O6q6ZTXtWDDvHqFTmBLOWwEdIoimgQAEPYUlitnV4zd6vyok6-wPhnvDUSteNbTG4cZKL0JWyh2vyoZGEcQoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77f4a7f60.mp4?token=vDffjqh3q-6i80COaMvSrSJmFuUcB5oJODqJlvR4bGg5ujymQuswoyUsv_kUrl9SYDCT1fA9RyT5wUzLia7sm-vdpEZUsfNWtpWQbLCRuMPZG5B7Q6jFas90uu5XCTxAg4JzjW4uH_5lux9zAJDQT3zIFZA4smHf3HhgSntju2WR7xf3auqpg-l3mAhdyTIDVfZzHNlbleipKLaCXcUSZR7NtldiAriF6J8Umt9GXKoHoyomqjPKpNPq8E95pV62O6q6ZTXtWDDvHqFTmBLOWwEdIoimgQAEPYUlitnV4zd6vyok6-wPhnvDUSteNbTG4cZKL0JWyh2vyoZGEcQoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلر آرژانتین عکاس شد
🔹
امیلیانو مارتینس در لیست بازی بامداد امروز آرژانتین مقابل هندوراس حضور نداشت ولی کمی آنطرف‌تر مشغول عکاسی با دوربین یکی از عکاسان بود.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656793" target="_blank">📅 13:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656792">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b5785b55.mp4?token=rzyGlCDKW11P3V3CkMH3TOzC3kLNj3MEm4d4IsmW1JPX3xO73AxFPD3RnC_zk4G87OCBs0RGG8XanJdogkK3pK-jsUj1yWkKv0p50gdRiMTTaiFDjih0dk5SnNTFYPmAm9AUxUI6VwCgI3CrA_c1ws86EtKtzrFb-VwnsFArqgisWg6jI9gU0SQfPhUbSKM-4he9nF6U6XpMm5mWNbqvSQZ7XIJqwoongiAY2G4o7Q_UmVTS7jJHaXMggJwmdJVLCID8aW8-LD46RUdqTzJSPbiusbrfPVErRH_w2HUVjDeg-or_i4DOAh_5-Ns-ox1LTD7C2EkH9vlQmX7Nyc5Z-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b5785b55.mp4?token=rzyGlCDKW11P3V3CkMH3TOzC3kLNj3MEm4d4IsmW1JPX3xO73AxFPD3RnC_zk4G87OCBs0RGG8XanJdogkK3pK-jsUj1yWkKv0p50gdRiMTTaiFDjih0dk5SnNTFYPmAm9AUxUI6VwCgI3CrA_c1ws86EtKtzrFb-VwnsFArqgisWg6jI9gU0SQfPhUbSKM-4he9nF6U6XpMm5mWNbqvSQZ7XIJqwoongiAY2G4o7Q_UmVTS7jJHaXMggJwmdJVLCID8aW8-LD46RUdqTzJSPbiusbrfPVErRH_w2HUVjDeg-or_i4DOAh_5-Ns-ox1LTD7C2EkH9vlQmX7Nyc5Z-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ندای خونخواهی بلند شد؛ نوبت مراجع است
حجت السلام رفیعی :
🔹
آقایان
#مراجع_تقلید
و علمای محترم اکنون نوبت شماست که به پاخیزید و اعلام مهدور الدمی را برای ترامپ و نتانیاهو اعلام کنید موجوداتی که خون نائب امام زمان عج الله تعالی فرجه الشریف،
#شهید_ثالث
را بر روی زمین ریختند و جنایات عظیم دیگری را نیز مرتکب شدند.
‌
• آیت الله سیستانی
• آیت الله مکارم شیرازی
• آیت الله نوری همدانی
• آیت الله وحید خراسانی
• آیت الله شبیری زنجانی
• آیت الله جعفر سبحانی
آیات عظام...
‌ما مسلمانان منتظر
#حکم
و فتوای شما هستیم
✊
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656792" target="_blank">📅 12:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656791">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnSXHpF44hps-p0ENDRlih6u2UpZkZWSXTMKiOixAd3ChvwuT2FEx9PmRvYN7t6LSJze_NFl8HkUvVS5mRn_fB2jwIiagLYi5dXr-QoWOeDe6rLUrCZOOX7KNIUFAj222H9Hs6N5DGd-agIMkIMGGSlokdiQNl86SkejPQCJfxD5veDWfzMniuJeziyRsOG0ih26ikCjCZJnmwWsPZ0c3gryeaRnRKjMqI2V4kLEYVjRJ7u_PlEQDHFBt0MrmLyCKUWgbi8KbUNQAlwZ_6hoU5uv-8zlr4QPSDDmEcVfr_r7Muobct0aCswdgtrVn1E52jIUDk8_6__CjT1gYRdq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لرستان، دره خزینه پلدختر
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656791" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656789">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf-z1LnNMCgYzKiVhoHS5-cmUOtFedUbCmteXEhWqHJA2gilp7q7AlolA6pdzI40vqvT8Afp2Q5LrnOyJctS-iKJ4NaWo2emW5Yr4IBZlZi_-IVvvG_get0sOQhvdvVOoniht9EwWfKORLBfd_YIIprgXbcTuud3qaOgfw5uMBDAQ53xeQND-JoYaJa35K1vjEu6pQvvz_HT-7A1q_-vM1cOsdHy_olbU4LEdrKuoggfq0kKSVLdp4rUIdd_FRVBkMtbPf3d4D4NaIbTu7S3jLNqF-RGjSwmSxafG-BBsBrjnhj33n29BL9cgNXLQhVDgzbDur9Xx5xTzTH97M5IoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiqeojJQcPBYpgMY3fwMAGUDCw9KJXscM8-pkdTs0FYB2YV9t95HYXnoTyhG9nKcRSqSkZlqogDRhSm_0Ky77UG9gpVwOK2N6QU2_1FhaIsVNCfi08cJIWDq36ncm0pz8XqpoL2f9wHd4bvDby8M253d80DWmkRv3JHa7qvTzQdUIiZmaxU8m-R1CbvmcmouDGw3ulY0ofJERDi1D6MjXQ01_5Opalec0efz05az78raUjKw7K6jkQiZf-CI4EvbYtSg6yqb3RgFRly70xe4585KftK7yoDUsBJY4mbYeLwy0eJheDgHTZlzF3WmCGIcBVBcsRjN-njgpftTrfYxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب‌های‌احتمالی تیم ملی فوتبال ایران برای جام جهانی ۲۰۲۶/ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656789" target="_blank">📅 12:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656788">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSg0TTBcA1mwcO2ZMSV_qUWF0U3pMS3YeWRfLm_xKQpA6xZUJKWUBnlH1LhvvLBHk7Clgd1pmNJKFaMNjVH3K9-68qmVm_kSFcBA8pjmbLSJX8WFdIfSJ3PSvhuYPSn4UqvkuaimZBeU1cEND56vtrArdqGN870u3zl0uhSnMUgAeFR7VI6YEVVf0FijZkzIDptsNKcAkCri1ye4b6ulV4uhg1zQ251gAZpgMaWUgGxMT51l2HMYK23Wx72aaafxMywD8XnUTAQ4TDHiRHY0iYzIxNMLIz8N9pf6cmvMcuWUgnmIVIsXmdcTTnyqsGhBeFtj62mZLkhLT4y0p_m8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس همچنان سبز؛ جهش سه رقمی شاخص کل بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۲ هزار واحدی به ۴ میلیون و ۴۹۴ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/656788" target="_blank">📅 12:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656787">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJmVnEDNpuGJHd4Q73re8ASq0neDB0okwsEOgqmd7kqXXAoJ-z4bEKuHsE7FSgllCTnXWNACXD3Lm_stF88Od9rFdyKDjXt-MFRMp8MkJv9-_EdXukk-Ba-WiArxP3wZd-xNek89PmCIs4fyngmukbFRLVPUnRX02orz4kvTO0J-V3e9j_ibK8a3rXSo3VFTYcSygfqEM0NfRVnRagT0JdbAYsbpZcfN01Hqy9PNixVLNdCjdBbd65eFgiedTyaYLqIPJGxDS0Eh-fk7jlqRuXKKEk8oplTTOCLV8ZGTQZpfePTQv8vbSZtI_5-dRJBVZQxdtT-vCukksJvt34bfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت پرونده تتلو از زبان وکیلش
وکیل امیرحسین مقصودلو:
🔹
موکلم مشمول عفو اعیاد قربان و غدیر نشده است؛ توبه تتلو از سوی دادگاه پذیرفته و پرونده برای تصمیم نهایی به رئیس قوه قضائیه ارسال شده، اما هنوز حکمی صادر نشده است.
🔹
وی همچنین خبر درخواست مرخصی برای مداحی در ماه محرم را تکذیب کرد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656787" target="_blank">📅 12:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656786">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymnp2VXSkZmVvcAmoy1db_P9sg6TAAzRjnRiXwlYapMZjqLeBGN5TyAqPs5D5roBikDcLQ1XVrYOLNS11oUSaocTypQUv_2_V3YX7uxl2zt3-VJ3Sxsdy4M7aCc3Ie0jbIPH69e9vG82_AW-1hq88lWdcjohki_AmD78j18ax6SVrrlW1DvmyVDB2a3Zw7yR5bpVOp2lv16aiNyQWkzMse5vhLwoCGpDqpTGQqpBzDQfULjEYGLySWT602_3I6y_Gp-Ijz2Mwpf1nCUtvZ1H_NzSiYvRXfOEhgjy57KumkNSq3zeNOXk5v4pwQhv1mRsc-98CGAERqb_3cH1XGVZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر تحولات ظاهری علیرضا بیرانوند؛ از تورنمنت آسیایی امیدها در ۲۰۱۴ تا جام‌جهانی ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/656786" target="_blank">📅 12:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2-M0EkTm1BG1NJzxjQVMHPuUi-oP8xCtlWt4mF4QQgTVdJ7OrfsZM4PTw57KakqV4MOoRyq1POpBvKcHIELvFrdaQtciiD-Jjwlio3d1YsmKk5TkZqHeVUVDMzPhLgvpOksRH9vHPfw1EpUHhkRp7OYhb2YCDh_nJXmsuxw8-GOtC1wDCK3n4LqKF8CrKLcJwpd2A7V69D-YXj3U1br85v-1g1H-hw5INklNBZySotlPkpWj3Ha3-BmURxkpGVb04lPiZiiJW6LfinVTOlNjwNOoUvtg6eC5Iv51dhL4suf_5Oc01Uy99oQ_ZtlE7IaH1TxVa_2K2ZSqJr2-yxc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ نمونه مشهور از اخبار جعلی
🔹
شما کدام‌یک از این شایعات را به خاطر دارید؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/656784" target="_blank">📅 12:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656781">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF1Xwk0WrmMqzPxHCjR0TubB3LfPHyBI8fokfHLPhKNvIAljUUMqaDPx1PV--2YQFgfOL39W842xyQnjriM3AgyAYONrFTX63y_KlhZsAEO0zzZOlBw3TDbAJ6qJFdeJ2HdkCNrHq2VoQ_YJFYi7fMEVPYB93llSthGwCLOC4FdFFYCfhwNV-sdTM28wB-aBsTl9qEmAHeiy3EymwllCTyCSMfwHBu5KgjTrX6W0W_xA7QBOyX3zjaS16bI-YBK0vWDLxSkUWjC27BkC1CIcgGIrz5QkXplCIRNEYCUjnueBrYPCf8oXgRKlO296Pj3rfeK_nkjr_LeYQ7D78Vemcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/656781" target="_blank">📅 11:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656780">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آغاز عرضه گواهی اسقاط خودرو از ۱۷ خرداد
🔹
عرضه گواهی اسقاط خودرو با نرخ جدید از ۱۷ خرداد آغاز می‌شود و نحوه اعمال آن برای خودروسازان مشخص شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/656780" target="_blank">📅 11:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656779">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKSVmL72poh9xVavKIAHLfYK9aF8IgqxHc7yVS1OK4tNzOy3dwnUYqok1AybGLnEYlBWqZKvRh2MBfFcZpQV3TDWvNX3dewUVp-PF9ge80aMI5xCuKbzdV64mMiPLBNOJM4L6AvijNMi64Pls0iZaUyhiDfaP_iy62LoLXxiwnvP2HnwurtrwzoiFneDk-Z9nSL6J8Ci2Ze2RomAizaGdvjbKkgS6catmhpoo9UFEJUZhhwwV8gL_5c7OmHn8Zxf7mOGxdX_csP8oX9e3WP9X_LvB5tyU8127S7RjCZaXRr6CmXqqxYpR5dopQZoyOo-ibd_DfGZmaTDJxZJljd6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656779" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
