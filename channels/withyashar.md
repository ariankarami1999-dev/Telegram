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
<img src="https://cdn4.telesco.pe/file/FndBMVPKIZfOBegxH5jLnafjadZaEVRrJev0Lm217Ei9x8ZL97LI4ptgU5a2VOMcbyQ4FRNQPkr-0BnIpV129S33EcTtI76vipQah_C4IzEihKFqZOq_e_BSUZUzw5nyKHVHgs5W0l_JF2DQSThElX2jpwl5Hu_B5id_npnenOp5Hv_W63hQ9GzmaX8hjfhPZ6lwNJt71EuOS3pjsT2ubGVd9TbsWxb7RvDEfI8md1s1LBhJYJc5QA72yJKBzITEeYZuH8V9E3UkXAjENmYlTLVI6cdR67l5ELR4MwGI6wSd3FAxQeirKRkZg0waxFObmbJCBDskiVO9x_571XCX-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 311K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-14285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سناتور لیندزی گراهام در رقابت با بازرگان مارک لینچ، در انتخابات مقدماتی سنای جمهوری‌خواهان کارولینای جنوبی پیروز شد.
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/14285" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=QZwIdqIa7DoHgV6uotSI1wf0xXXjVfxgOrBn7T_wukdnwD_W5RStFOGMdxYHDfChI6FqbXYhFcHFNOjJd4VGTk3Res3KEY4hY2v32yMBSAAL8smt4TFoLglTpKqPgoAt1c4LMTDwaILT3paydKnAlXSeRPsyHZnuSijYdoqevjEVVUqs4uj8_cD-IIK_F_a0twDx-spKz9yoptCGJkqW6Pu09FzRI06GERcDyvH_u5S1XP0VbERFNTc54-qxtrlLLu9rPd0jIe7oTzTS_ZhLjYQB5l4T-yeYT4K6bUA1BDScOLMMlJdHN0WS9nr2zD2jVfZQypjhP41KR3E_SXtf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=QZwIdqIa7DoHgV6uotSI1wf0xXXjVfxgOrBn7T_wukdnwD_W5RStFOGMdxYHDfChI6FqbXYhFcHFNOjJd4VGTk3Res3KEY4hY2v32yMBSAAL8smt4TFoLglTpKqPgoAt1c4LMTDwaILT3paydKnAlXSeRPsyHZnuSijYdoqevjEVVUqs4uj8_cD-IIK_F_a0twDx-spKz9yoptCGJkqW6Pu09FzRI06GERcDyvH_u5S1XP0VbERFNTc54-qxtrlLLu9rPd0jIe7oTzTS_ZhLjYQB5l4T-yeYT4K6bUA1BDScOLMMlJdHN0WS9nr2zD2jVfZQypjhP41KR3E_SXtf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان: ما کاملاً آگاهیم که هدف نهایی توهم «اسرائیل بزرگ» چیست.
ان‌شاءالله هرگز اجازه نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/14284" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران می‌گوید دیپلماسی با ایالات متحده به دلیل این حملات تضعیف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/14283" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اردوغان درباره رئیس جمهور آمریکا، ترامپ: «شرکت او در اجلاس ناتو در آنکارا برای وحدت اتحادها مهم است»
@withyashar
یاشار : امیدوارم ترامپ به این اجلاس نره ! جدا از تمام مسائل مذاکرات، می‌تواند به آخرین تیر ترکش جمهوری اسلامی برای به خطر انداختن جانش هم تمام شود.</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/14282" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است. در پی آتش‌سوزی در اتاق موتور یک نفتکش، یک نفر زخمی و دو نفر از خدمه مفقود شده‌اند؛ این نهاد، هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/14281" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یونی بن مناخیم، تحلیلگر ارشد مرکز اورشلیم، به کانال ۱۴ گفت که ایران سیستم‌های دفاع هوایی که چند هفته پیش توسط ایالات متحده و اسرائیل نابود شده بود را بازسازی کرده بود. بهبودی با این سرعت بدون کمک مستقیم چین امکان‌پذیر نبود.
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/14280" target="_blank">📅 12:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم اکنون صدای انفجار‌ در‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/14279" target="_blank">📅 12:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8515c2be09.mp4?token=eWgqJfvjOr9nzMBajNbMWw_hcRN4cGl-uzY50qGERrHB6fbP6hOlGc6MdKdwR97AOaO9Fdip4e_RkIKZBttjyZtqwIpR5CCXHfbjoVrJra8ON1MTcIN73a9P4jhS4nzE4BWBKEQpIlofHD-Xp327ZTbV7IEn4G3AEU7JGl-RV2NHCVwsabgDHc_dtkinPVNncprw51ED57szfYN5gC1CGV5DvTrYXhPoyN8rz_S9quATzCtbRTrQVwlJvsvtiKIjlfy9PxhuF5AyEgNpg6lLUd53US8PYH5DKxn4BeR4aXzEu4cmLCBzDuGsNbBMMmsRYSvPO2PnD6w5aCOJlagULbIEDZThnjmUVmM2n1xwm-aK_LizXQy3DDQOHWdQk_BGOzMciG-JoRNX73RooKu-5plsUHgu-YBx3qR8nkWbjc2ouzbmTxhzHGAElg9TRLU7vyau3VI4mEEM8ksra2HgBsgw4gNwdbD5GbBSGnhslkSTG42NxxRp9dhh4IwMH720NSVYC6uqTMqP2W4Y40uacOe0c9RKAKyUp-xrTYUUhMBcEzqmtuCeQ_Rh7kbfOkoMYjfvaJxo3Nq-9C_ceczOEot8aX_-oGH008U5zQuZ7jJr8IidZQYGyaHJltiaPh-x1LS-M9WmeNOp3BaVKTNpu-1jV3x1N-BcfE80D1Tirh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8515c2be09.mp4?token=eWgqJfvjOr9nzMBajNbMWw_hcRN4cGl-uzY50qGERrHB6fbP6hOlGc6MdKdwR97AOaO9Fdip4e_RkIKZBttjyZtqwIpR5CCXHfbjoVrJra8ON1MTcIN73a9P4jhS4nzE4BWBKEQpIlofHD-Xp327ZTbV7IEn4G3AEU7JGl-RV2NHCVwsabgDHc_dtkinPVNncprw51ED57szfYN5gC1CGV5DvTrYXhPoyN8rz_S9quATzCtbRTrQVwlJvsvtiKIjlfy9PxhuF5AyEgNpg6lLUd53US8PYH5DKxn4BeR4aXzEu4cmLCBzDuGsNbBMMmsRYSvPO2PnD6w5aCOJlagULbIEDZThnjmUVmM2n1xwm-aK_LizXQy3DDQOHWdQk_BGOzMciG-JoRNX73RooKu-5plsUHgu-YBx3qR8nkWbjc2ouzbmTxhzHGAElg9TRLU7vyau3VI4mEEM8ksra2HgBsgw4gNwdbD5GbBSGnhslkSTG42NxxRp9dhh4IwMH720NSVYC6uqTMqP2W4Y40uacOe0c9RKAKyUp-xrTYUUhMBcEzqmtuCeQ_Rh7kbfOkoMYjfvaJxo3Nq-9C_ceczOEot8aX_-oGH008U5zQuZ7jJr8IidZQYGyaHJltiaPh-x1LS-M9WmeNOp3BaVKTNpu-1jV3x1N-BcfE80D1Tirh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
b52</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/14278" target="_blank">📅 12:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cea3e4e8.mp4?token=deknCaN2jqHR-i2mtVvhACwBVRpsYOXAY3jlnwuJ3IqwH85mPoODb_dWqTPvNcwDTM0BjP2CTGxj5UkVzXnuQIXB-jHfATSkWFdGVba5NjtA50T1_uR_kSXA1BPcaiA56MPqS1Pa24cXsGt8kq7w3ktuPIagUFMQRaLQ_8XX5RUjwSsrUs0_Gsm59ht8nyS8h8BVoDu-CjG4mescqepPoe2w8hP1HSEjIQq7O12A3ojCALkjaXGojkpGTdFeKwq9qIRsh5FJEl8HbuPN42Qfj0vd-Y0cdDFOEdCruXMyPYpPjK9K1lihcED06q4lLr00-VqDS-EMy4Z0D2gg1mDjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cea3e4e8.mp4?token=deknCaN2jqHR-i2mtVvhACwBVRpsYOXAY3jlnwuJ3IqwH85mPoODb_dWqTPvNcwDTM0BjP2CTGxj5UkVzXnuQIXB-jHfATSkWFdGVba5NjtA50T1_uR_kSXA1BPcaiA56MPqS1Pa24cXsGt8kq7w3ktuPIagUFMQRaLQ_8XX5RUjwSsrUs0_Gsm59ht8nyS8h8BVoDu-CjG4mescqepPoe2w8hP1HSEjIQq7O12A3ojCALkjaXGojkpGTdFeKwq9qIRsh5FJEl8HbuPN42Qfj0vd-Y0cdDFOEdCruXMyPYpPjK9K1lihcED06q4lLr00-VqDS-EMy4Z0D2gg1mDjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعت 01:59 به وقت جهانی (UTC)، یک بمب‌افکن B-52H متعلق به نیروی هوایی آمریکا در حال پرواز بود.
این هواپیما از پایگاه ماینوت در آمریکا حرکت کرده و به سمت پایگاه هوایی فِیرفورد در بریتانیا می‌رود.
این پایگاه یکی از مراکز مهم برای استقرار بمب‌افکن‌های راهبردی آمریکاست در میانه حمله و در عملیات‌های مرتبط با ایران نیز مورد استفاده قرار گرفت.  نام ارتباطی این پرواز THIRD51 است.  خلبان در مسیر، موقعیت هواپیما را از طریق رادیو به مرکز کنترل بر فراز اقیانوس اطلس گزارش داده است.  بعد از عبور از یک نقطه مشخص، به او گفته شده با برج کنترل شانون در ایرلند روی یک فرکانس جدید تماس بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/14277" target="_blank">📅 12:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانال ۱۴ اسرائیل فاش کرد:
طبق جزئیات فاش شده از مذاکرات، دولت ترامپ در حال انجام مذاکرات محرمانه پیشرفته با تهران در مورد یک توافق هسته‌ای جدید است که برای متوقف کردن برنامه تسلیحاتی ایران به مدت تقریباً ۱۵ سال طراحی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/14276" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53b13459f9.mp4?token=NgevF9hkA7n35fsdQDJx4qpm3HnAr67OhzHYJDE3aE5BFGD6rJYAYVehoOPEhAeqIjQYKkG7Zf_vYri-YRbtuUpoarSZEC9FhCFr0T_LnHgJdb10-vhFM-T2N7MfhXyDNeAVbU_Fhzcesxi4oNL3tjpxBM2wSreoW_9j-xUo6oHY0n2xHSCGgPkXXSWc_PpUaqkZediU175s74mhT52sX0BMK4YRtRXlBBRgBbUyq35-S-gDzgviZo4k704xA4XztJv_O7Agw1zQ16YoJ7R1xj3UNVfieGyHypUS4mJgB7brPXjvAJhM6ak7m_m9dn-YrcDI7i3WLa2VNpbW74RQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53b13459f9.mp4?token=NgevF9hkA7n35fsdQDJx4qpm3HnAr67OhzHYJDE3aE5BFGD6rJYAYVehoOPEhAeqIjQYKkG7Zf_vYri-YRbtuUpoarSZEC9FhCFr0T_LnHgJdb10-vhFM-T2N7MfhXyDNeAVbU_Fhzcesxi4oNL3tjpxBM2wSreoW_9j-xUo6oHY0n2xHSCGgPkXXSWc_PpUaqkZediU175s74mhT52sX0BMK4YRtRXlBBRgBbUyq35-S-gDzgviZo4k704xA4XztJv_O7Agw1zQ16YoJ7R1xj3UNVfieGyHypUS4mJgB7brPXjvAJhM6ak7m_m9dn-YrcDI7i3WLa2VNpbW74RQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاکستان تصاویر هدف قرار دادن اردوگاه‌های تحریک طالبان پاکستان در کنر، پکتیکا و خوست در افغانستان را منتشر کرد.
این هدف‌گیری به وضوح نشان می‌دهد که این سازه توسط بمب‌های هدایت‌شونده لیزری مورد اصابت قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/14275" target="_blank">📅 11:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانال 13 اسرائیل: ارتش اسرائیل توصیه کرده در پاسخ به هرگونه شلیک به سمت اسرائیل، حملات گسترده و شدیدی علیه بیروت انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/14274" target="_blank">📅 11:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اتاق جنگ با یاشار : خبر ۳ میلیارد دلار خبر فیک با منبع رسانه داخلیه خودش هم گفته باز به نقل از یک مقام سپاهی!!!! @withyashar اون پرواز هم چک کردم رفته پرسنل رو تخلیه کنه !</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/14273" target="_blank">📅 11:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارشها از صدای انفجار هم اکنون در قشم
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/14271" target="_blank">📅 11:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCTuXEJGS-SDf_F1Pv0PP7enj1Ct4rRFK2MT0sDwm4P4DnAv9VEBslpq-UhuwSOtGJwwDwUF8qaWwLnivWFrrmuEXfx-B3rst48SvJZGUzsAE3nSfz6H2vtGkgoZEwcT6cwMviNOOXikDm1BgC65-cRDaY6oCf72pZ5tha7RKwyfHQnuqVZi_yHAsNaA0132qJq2YNTdxPqGJK8tfd2KNxev7z6yXwOWFqicWnq6dIStWk0hy35GrJThZoj64FbWAOe071Imdf8NUtzRKFh6e4v29CBnsvejNuepszUFEd0zflPPr3dB7s77DT2jbeNnBnTsZ1tz-EmC0r0YhoglJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از کشف تجهیزات جاسوسی برای پشتیبانی هدایت جنگنده‌ها در لواسان
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/14270" target="_blank">📅 11:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز @withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14269" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14268" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeHD1LRQvuAR2MRav7tJe2GRMrkvq-jBXKxPpiiOTcBa_Mwy-8JyCb6IJyONwkIhnTGKb7pRTSJpXvEzA_wkP_6rUOg21Gl0TVUBpWiLJcPYsxi8JSjeh0YV_G-Dry-VSM5PHixwMgjWHmyuYYhx1VuWLOQRdRQlOxmVlqOhA7YPH-r-YBDzz5wP9W23UIHSP0-XqheSORjTSHAsPHCN4X0VgaYhWERPWwAuASmK3bvo94pXySNZUDbuZpNzbCBYtQeHms02RxelUecj7E3REAOGJLWqVyiBZmdXa4qdqcmt4_UKdWaZSc_W7x8JSrsAOqbAcZgp1kBdQyVXx9XhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خمین دم صبح موشک اومدن ول بدن برگشته پایین
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14267" target="_blank">📅 10:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هشدار مسکو به تهران:
صلح، پوشش حمله زمینی است، نقشه پنتاگون برای پایان آتش‌بس دوهفته‌ای
شورای امنیت روسیه در بیانیه‌ای تکان‌دهنده که توسط خبرگزاری «تاس» منتشر شد، هشدار داد آمریکا و اسرائیل از پوشش دیپلماسی و مذاکرات صلح برای آماده‌سازی یک عملیات زمینی گسترده علیه ایران استفاده می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14266" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:یک کشتی تجاری گزارش داده که در جنوب غربی بندر بلحاف یمن، یک قایق کوچک حامل ۶ فرد مسلح به آن نزدیک شده است.
به گفته این سازمان، بین قایق مسلح و تیم حفاظت مسلح کشتی تبادل تیراندازی رخ داده و در نهایت قایق از محل دور شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/14265" target="_blank">📅 10:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">روزنامه همشهری: خوشبین نباشید، ترامپ از این جنگ دست برنمی دارد
روزنامه همشهری: واقعیت این است که دعوا بر سر چند درصد غنی‌سازی نیست، دعوا بر سر نظم منطقه است؛ بر سر این است که چه‌کسی گلوگاه‌های راهبردی جهان را کنترل کند و چه‌کسی موازنه قدرت آینده را شکل دهد.
برای همین شاید آتش‌بس باشد، شاید وقفه باشد، شاید جابه‌جایی تاکتیک‌ها را ببینیم‌ اما تصور اینکه این کشمکش با چند توافق فنی برای همیشه خاموش شود، خوش‌بینانه است.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14264" target="_blank">📅 09:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14263" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD3J0zeOxO9u1qJJWncnUgVxpcovERYMWEIp2srmS-vCZ8vJ0E6wfE2zROuQrY9P6vlSUkcsq0B_krCjHdt4KPz5iflPZgbQQ-cHD7upWrV_u-jSMmsxKGeCSYi-jOJonmssyZFDAvZEDZ3MCbgLyYH4MgUPXhpA07UDdTZVyxGqjs-rCZt8bPVfwz9T_2gXRE6VZp9uKgfOftd3MwJXnbqvhns13RwbOVPKZSWFV1l1fW7gRQo_hfmJPZOehzEtAqLrXUk3K_E1V8yG3ZuMISoyVTfRkqfAqNyT9RdCVmx_Yw9pHeTn553t5G0mtPBYeB-oiI8CX4r4gsBw1td4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت سامارا روسیه پس از اصابت پهپاد‌های اوکراینی
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14262" target="_blank">📅 09:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سخنگوی طالبان:
دیشب ارتش پاکستان حریم هوایی افغانستان رو نقض کرد و چند خونه مسکونی رو در ولایت‌های کنر، خوست و پکتیکا بمباران کرد.
تو این حملات 11 کودک، یک زن و یک مرد سالمند کشته شدن و 14 نفر دیگه زخمی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/14261" target="_blank">📅 09:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۳پا پاسداران: به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه…</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/14260" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۳پا پاسداران:
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه هوایی ارتش آمریکا در الازرق اردن رو مورد هدف و انهدام قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14259" target="_blank">📅 09:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار وای نت:
در چند ساعت اخیر در رویدادی جالب سامانه‌های پدافندی آمریکا تمامی موشک‌های شلیک شده به 3 کشور مختلف رو رهگیری کردن. صفر اصابت و شاهکار پاتریوت!
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14258" target="_blank">📅 09:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی نوشت: ترامپ تمایلی به حمله به ایران نداشت، اما پس از توصیه وزیر دفاع و رئیس ستاد مشرک، نظرش را تغییر داد
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14257" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیروهای مسلح اردن: پنج فروند موشک ایرانی که به سوی پایگاه الازرق شلیک شده بودند را رهگیری و سرنگون کردیم. در پی سقوط بقایای موشک‌های رهگیری‌شده، هیچ‌گونه خسارت یا جراحتی ثبت نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14256" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">https://t.me/boost/withyashar
۳۹۰ بوست پرمیوم هاااا</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14255" target="_blank">📅 03:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">۴ انفجار‌شدید بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14254" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هم اکنون انفجار سنگین سیریک و اطراف را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14253" target="_blank">📅 03:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حملات جدید به بندر عباس و سیریک
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14252" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14251" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال 12 اسرائیل: در موج دوم حمله‌ها به ایران، آمریکا داره پدافندهای هوایی و رادارها رو هم هدف حمله قرار میده.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14250" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-zJIBiyX_e4h75eKBFkGOXsQVQeTm1RGtZZPNReiF5OVtl9jmsQw3yEuBqoV_jJr01vex-q-YbJlvCH8-zc0l0mnRkpgEjoZGh8HVZ8mGSBEKbGPsVxm7GDGw-TmWx4ftdxAh4L20l03QY_fuhlYbEn4TzlF_w8zbrb6_cORfpJmkCI5FSS0rFoH-ji_IKH7d6YGDu3icBUP_bYKFHnwjyr7tIu9uWNeK-KmwVM7zlEkDfgG3keDGrJGNTF68H3m2C1bALP8h9yOT14Ne8wg57CScmIrW0W4ad4kovP5ropwI2nijPWS76k-AHy2XXXqCj3ggvC1wYnG8UsFknuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : بر اساس اعلام مقامات نیروی دریایی آمریکا، نزدیک به ۲۰ هزار ملوان و تفنگدار دریایی آمریکایی در حال حاضر در دریا و مستقر بر روی دو ناو هواپیمابر «یواس‌اس آبراهام لینکلن» و «یواس‌اس جرج اچ. دابلیو. بوش» هستند؛ به‌همراه ۱۸ ناوشکن مجهز به موشک‌های هدایت‌شونده، یگان اعزامی سی‌ویکم تفنگداران دریایی، و بیش از دوازده اسکادران هوایی.
این تجهیزات و نیروها در مناطق مختلفی از جمله شرق مدیترانه، دریای سرخ، شمال دریای عرب و دریای عرب پراکنده شده‌اند؛ جایی که نیروهای آمریکایی در حال کمک به دفاع از اسرائیل، مقابله با تهدیدات حوثی‌ها، انجام عملیات مرتبط با ایران، و حمایت از امنیت دریانوردی در اطراف تنگه هرمز هستند.
این نیروی دریایی بخشی از حدود ۵۰ هزار نیروی نظامی آمریکاست که در حال حاضر در سراسر خاورمیانه مستقر هستند.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14249" target="_blank">📅 02:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14248" target="_blank">📅 02:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14247" target="_blank">📅 02:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14246" target="_blank">📅 02:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14245" target="_blank">📅 02:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس جوگیر شد و گزارش کرد :
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد.
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
شما بازی را شروع کردید؛ ما تعیین می‌کنیم چگونه پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14244" target="_blank">📅 02:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که حملات هوایی آمریکا به پایگاه‌های نظامی و دریایی، تأسیسات راداری و باتری‌های موشکی در پنج مکان در سواحل جنوبی ایران، از جمله موارد زیر، هدف قرار گرفته‌اند:
پایگاه‌های دریایی در سیریک و جاسک
سایت‌های دفاع هوایی در بندرعباس
باتری‌های موشکی در قشم۶
برخلاف گزارش صداوسیما مخزن آبی در سیریک هدف نگرفته است و مانند مدرسه میناب رو به دروغ آورند!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14243" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنگ امیر تتلو و زندان
امیر تتلو از پشت تلفن زندان موزیک ضبط کرده و همین الان پخش کرده
https://youtu.be/ixhpdO88-IY?si=dmb7e06_W8ShLkkA
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14242" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار صداسیما در سیریک: در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
@withyashar</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/14241" target="_blank">📅 02:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اتاق جنگ با یاشار : با خسته شدن و خوابیدن ادمین های تلگرام جنگ هم تمام میشود
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/14240" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258b122927.mp4?token=c-jbZLshenpxYQHP3Lxtwd9dJ0tYchX5JKelsHEpnTfOdgdoo6nXmt9xmwUuwBB2s1vqTKc8Fs0j6SFQWeNLqDLQ2VjGalKvxI8Liu6W8cqAbgSgAYdvUmVaunkM1jEtxbaRXKXjZX4cmZNYBZAvkn8b9U1fD9UFYZ0TchI8WJB0tlo4DZ5qvfx6631ewSwLPoL-5GczmEQMAStR3f6TnwOnOIK-AJ34Zx_uNxXtq-QntK7MFk35topR8sjAsOMubNY9d0cwZrFNvFQ9WBiO8_b5Pl3uX62UUM7Fn4ustWC_r6lcELZ8ajpMJmMD6pAe1rkD0btKBdHBe4G4PmZNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258b122927.mp4?token=c-jbZLshenpxYQHP3Lxtwd9dJ0tYchX5JKelsHEpnTfOdgdoo6nXmt9xmwUuwBB2s1vqTKc8Fs0j6SFQWeNLqDLQ2VjGalKvxI8Liu6W8cqAbgSgAYdvUmVaunkM1jEtxbaRXKXjZX4cmZNYBZAvkn8b9U1fD9UFYZ0TchI8WJB0tlo4DZ5qvfx6631ewSwLPoL-5GczmEQMAStR3f6TnwOnOIK-AJ34Zx_uNxXtq-QntK7MFk35topR8sjAsOMubNY9d0cwZrFNvFQ9WBiO8_b5Pl3uX62UUM7Fn4ustWC_r6lcELZ8ajpMJmMD6pAe1rkD0btKBdHBe4G4PmZNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعالیت پدافند مشهد امشب.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14239" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جسی واترز از فاکس درباره مذاکرات ایران:
فکر می‌کنم ما همین الان یک پیشنهاد دریافت کردیم/از واشنگتن می‌شنوم که از آنچه می‌بینیم خوششان آمده است.
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14238" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=BquebS7spMQWHZccVpX5QGyrhJztiWUtGcdZJkFL-J7Bk9PK9mGwNTbtmYl0HHpq1a36RuC58klWvCm3EIPMj9RFbzxHoiSH14kuA5d3AJrwRW9r0dVh2bBaz8E8J13_pXcf6hymyIW_7yYZUPI0fJhvhVWFjgSlvqFqlUnRM-9-TfGO8CsDkIOsybyQowwOCu9IiFEGfmNHYszRHkfzgLLiZvfqzHsn60IvNBJNrPjJXteHvdcW7_IAUkLxFzna5hVrPecfsGSg65C_ohM5jPNf02T1XrymIl8MPik8RL-_GYdXhzNp6IJLbKgIqs20CxrXWCiPHebrkrwaWUXxHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=BquebS7spMQWHZccVpX5QGyrhJztiWUtGcdZJkFL-J7Bk9PK9mGwNTbtmYl0HHpq1a36RuC58klWvCm3EIPMj9RFbzxHoiSH14kuA5d3AJrwRW9r0dVh2bBaz8E8J13_pXcf6hymyIW_7yYZUPI0fJhvhVWFjgSlvqFqlUnRM-9-TfGO8CsDkIOsybyQowwOCu9IiFEGfmNHYszRHkfzgLLiZvfqzHsn60IvNBJNrPjJXteHvdcW7_IAUkLxFzna5hVrPecfsGSg65C_ohM5jPNf02T1XrymIl8MPik8RL-_GYdXhzNp6IJLbKgIqs20CxrXWCiPHebrkrwaWUXxHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده پهپادهای انتحاری‌ ایرانی در آسمان عراق
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14237" target="_blank">📅 01:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14236" target="_blank">📅 01:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ولی یه حمله شکی توش‌نیست حمله شما به دایرکت اتاق جنگ
😭
🤣
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14235" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هم اکنون خاورمیانه:  حملات آمریکا به ایران حملات اسرائیل به لبنان حملات پاکستان به افغانستان حملات ترکیه به عراق حملات ایران به بحرین و کویت  @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14234" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شلیک دو موشک از سیرجان
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/14233" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارشات از حملات توپخانه ای عربستان به یمن
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14232" target="_blank">📅 01:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/14231" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی ان ان به نقل از مقامات آمریکایی:
انتظار می‌رود چندین دور حملات دیگر بر علیه ایران انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/14230" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هم اکنون خاورمیانه:
حملات آمریکا به ایران
حملات اسرائیل به لبنان
حملات پاکستان به افغانستان
حملات ترکیه به عراق
حملات ایران به بحرین و کویت
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14229" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هم اکنون حملات ترکیه به شمال عراق
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14228" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای من و شما شاهد است که هیچ ردبولی رو بیهوده حروم نکردم
🤣
✌🏾
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/14227" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مقام ارشد آمریکایی به باراک راوید خبرنگار آکسیوس: عملیات ادامه داره و آماده‌ایم برای چندین حمله دیگه.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14226" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش
انفجار در اهواز
.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14225" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14224" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سید مجید موسی : ‏و ما النصر الا من عند الله العزیز الحکیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14223" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14222" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هم اکنون بمباران مواضع حکومت طالبان افغانستان توسط F16 های ارتش پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14221" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به ای‌بی‌سی نیوز:
من به پاسخ قوی اعتقاد دارم و این رویکرد من است. ما توافق بسیار خوبی با ایران داریم و فکر می‌کنم همینطور هم خواهد ماند.
@withyashar
یاشار : زبانم قاسمه کتلته</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/14220" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز گفت: حملات هوایی علیه ایران «ادامه دارد» و اهداف شامل پدافند هوایی و تأسیسات راداری است.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/14219" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گزارش ها از شلیک موشک‌های سپاه از کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/14218" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : امریکا و اسراییل به طور هماهنگ و گازانبری به ایران و لبنان حمله کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14217" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14216">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">۳پا :
حملات سنگین علیه امریکا در راه است..
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14216" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کشورهای حوزه خلیج فارس در حال بستن حریم هوایی خود میباشند.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14215" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار در ضاحیه بیروت  @withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/14214" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری تسنیم:
آغاز حملات ایران
جمهوری اسلامی: همانطور که چند ساعت پیش هشدار داده بود، پاسخ قاطعی به تجاوز آمریکا خواهد داد که تحت پوشش سقوط هلیکوپتر آپاچی انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/14213" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">از خوزستان موشک زدن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/14212" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجار در ضاحیه بیروت
@withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/14211" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🤣
🤣
🤣
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14210" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سامانه‌های دفاع هوایی دوباره در بندرعباس، قشم و سیریک فعال شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14209" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فهرست اولیه اهداف:
– پایگاه دریایی سیریک
– پایگاه دریایی جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/14208" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مقام آمریکایی: نیروهای ما به حملات خود علیه ایران برای دفاع از خود ادامه می دهند و عملیات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14207" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صداوسیما : پایگاه های آمریکایی رو هدف قرار میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/14206" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">صدا و سیما می گوید دست کم صدای 6 انفجار در جزیره قشم شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14205" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روابط عمومی نیروی هوافضای سپاه اعلام کرد تا لحظات آینده پاسخ سنگین به اقدامات خصمانه دشمن داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14204" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14203" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش‌ها از هدف قرار گرفتن دکل‌های مخابراتی درقشم
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/14202" target="_blank">📅 01:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
هم اکنون ترامپ به ABC درباره حملات ایران:فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم،
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند،من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14201" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارها در قشم، بندرعباس، سیریک و جاسک
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/14200" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کانال 14 اسرائیل: ترامپ نتانیاهو رو قبل از آغاز حمله در جریان قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14199" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۹ انفجار بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14198" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxa0dtCTR-1_DbPBmJu3nhQPvcxUQMQPW9Bm7RmtCeWwvH6RfPdWJL6b_K79wHNZcl9vPFcCWmKymYYg7503vLToKXWHhx3XPPj2NkL1JWbthd6-R05y7l8WdICKFpeEeYGZ3oGU2Kn1Jl4N3yTKlRVasHrEl-lsKpAj2HaVlq33_B6BZwhobugJfcvpiu-SiPWhyY2KrQBDSeKN9XInKYrfn82dm7wovgR_Wh3dPrlT5Kq5xoQirBMq6qr7Trl7oHsW4PR6cLEgT8JXFDCAbOzHKNCfZ_vwqSKzVaCR1I6W2fuBEEDBrgijKv7RY9F-8KNALk_3Qi7mKUKPfbVk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@withyashar
شکار‌ لحظه کردم</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/14197" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طبق گزارش ها تاکنون حملات در جنوب ایران متمرکز بوده است.
هم‌اکنون پدافند در جنوب ایران مشغول دفع حمله است
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14196" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارتش آمریکا از شلیک گسترده موشک های کروز به سمت ایران خبر می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/14195" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک @withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/14194" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3Ab8ukZ2tOoSaPcIZ-mFhXzgJh9gJLBKDNjE1sn2ZItHbC1puHQZKwKOOST59b0sk05D9l3uilKZQWZSO41m-CiOcNWf4Et-woS_T_VTgyHIdFIq3LxnPjLwWW4Df3kpskHBYtY1UVs4U7rkSrmkxSNZ_ooN8TXq9bWbTtW0p4moxFryEisjm79ko6T6xkF2lDkUqQUio7AuYL3vcJVscLlul1z1PEv-g2QriIa41RsSYivU5AcYmV24zlN9SfsV5KMBHy4LRQRIoImM5ecQeui6aAGD9XPjiOxN8yK6x29iVqJb0vE4bfgCogqgLBMf88ASEceAKhW5hPLnqIQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری : نیروهای سنتکام به دستور فرمانده کل، از ساعت ۵ عصر به وقت آمریکا، در پاسخ به ساقط شدن بالگرد آپاچی ارتش «حملات دفاعی» علیه ایران شروع کردن و این یه واکنش متقابل و متناسب به حمله ایران بوده.
@withyashar</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14193" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14192">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/14192" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14191">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش‌های غیر رسمی از هدف قرار گرفتن پایگاه شهید راهبر در میناب
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/14191" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرنگار کانال 14 اسرائیل:
هرچند امیدوارم اشتباه کنم ولی پیش‌بینی‌ من اینه که ترامپ در پاسخ به سرنگونی بالگرد آمریکایی، یه حمله‌ جزئی و نمادین انجام میده؛ مثلا یک ایستگاه راداری و چند سکوی پرتاب ضدموشکی در منطقهٔ تنگه‌ هرمز رو میزنه.
یعنی حملاتی از جنس همان حملاتی که قبلاً هم چند بار در جریان آتش‌بس دیدیم، نه چیزی که جنگی رو با ایران شعله‌ور کنه.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14190" target="_blank">📅 00:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14189">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش های زیاد انفجار هم اکنون از قشم و بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14189" target="_blank">📅 00:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtG1K4KZLBtm3BcdWnyCjFKE2Nx8jVd9R-SCn4eO_4qWfGax3RfW5b-yDomzJOylKvLHU7fLuvLQGPhQyRqrtoyu9D8xCfxz1Ilvce7DJSimyLDJV4WZhl9tMNBMjwYzC4FxkhLCY4PNplovRKoRizdKqDXIYbWbUq5Txli0bjHzBMlsBJXfst7QkVTnZpy0Va_oy7UNy3SKeSt45NWWjdIOEpJXGKZwWqIaFD0XcPCFjo_pf6TDFCFPFvIZunwGLycXV_HX53EzvBLjIU_S6Pl9_ivhGL-rUI0Hqx_ovTCoEZajh4spR4fKm7ulmE7ZN9YJ4oCHZXLetlnLAdGW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انبوه هواپیما های آمریکایی در جنوب ايران
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14188" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14187">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/14187" target="_blank">📅 00:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/14186" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ان بی سی : فرمانده سنتکام کلی اطلاعات به اعضای دو حزب ارائه داده که همه قانع شدن حمله ایران به هلیکوپتر اپاچی کاملا عمدی بوده و باید تلافی کنن
@withyashar
این اولین باره که دموکرات ها تایید میکنن حمله به ایرانو</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/14185" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
