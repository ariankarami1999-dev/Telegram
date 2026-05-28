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
<img src="https://cdn4.telesco.pe/file/Ryqj8MYsapvntTZpREfyy1ymTA70YeBMOZsBIgYH3ffSzlHmY8Ixo-wpTDE8EEmhiEo3kaxJLotocpdUs8o-NTNV05hTehGPSeSxeWMsS0YAocoqd5AHomTXkElPrykZeXi_PBMMBFdgstZQEZGdhBax1E9PeDdgYU4cOe9N894XFI7ZthQGCOG2XrHD-_n8nXHn4p1ahs7mrkn44ef199l9PJ0GSPciKtOuhFy3NyP492J9ZBiNTGYQD5CR0TBd4fdLCEm5HT6Fxw9rePBZnVG7dioBeJGdCfejNYIOId4Vw6RIsogm6KYYum2kxgSrApMBrRbBg7ZaULV2A00UMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 184K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBTqIzJAcFn76Vq_CabmqpyY81yEOXjJ0bGxdfbgb8ddmm_iZJqDOtQaqpEbPVC-67ukX1ApINcb-iQIVZsyfbnt94iielA3IxZkmgU1PUk38AZuVQAmRUXDKhKgXi-VHmkZqwMjHrbL_PjxcINxwqbmFMF7UyIX0QHiHMbxXdX7uIP7tn7PGOpzrz2XwxV9M3-2Vc3SZ7LFRX0VvMQCsp4sGXqp4NG0sDU2y7qTUOWHOddbEC1V27vYGDZFAsBlOJU9qH3yI3yqOC_RA6tejS6lp6DQohznkWykpYkWGpmTwUUNrKsYVky0RJQTY2mVp_1lRBwDyU6UJyO_PmZ6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Minxp1xQw3nyIxcTXVN2yzO1W36tCm2p4nw4FyYpnQKa7WG7iwboQk550b90URJ9heYNu_YJeQwV1VYRoe7B2IRgYACNG9snJjb5U_NobxCKFCK275LIjIJ_ridsheprd8ndIS80M54zOeGHUBXB8Uju0V-Lga-xnpG2RT06o2wRY3TqL0l9lDCQVlpx5KhMST-CWFopgvjbZIbivx7I6-3QJKIYJaZslNvz1mUiroW8wdS-2SAbs7DwsdKV7ofDrbAPruwlsfNt0vYR29fyyGX8SSma8wD9jT8i9ZexReTsOdBDabE5w8gPIwPABCtqj0oqIx7gtPLVqMhY1LTv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22378">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx6q5J1cCWgCyNklCEgwOid28xn9nhiWegCcZkwFvqA2KOAGK3ZNvezWGuqD4l2FDwZzTva0VoRxM4C2IA8VdYhPQ46umBCg3ZsQordyIO0HyMBcyvX1aVQ9uDDaTcKPDPnAInMp67ilcsmQ-8JqP-OP6-JUg5qxlXVksYE61uB2FwvpSyHa6JtFGI1-kXXs_bjdeLnXV7-GcHRyVwVhKKAsi8kWb-DPwf3ZrB1hxiR2T4CIg8lrG3Po_--EZuzDq5iweKDgnsigz6yNDNmDMDgtpvd0jt1B28GSS0e1VRSk7Jh6S3aAeJ-1dMNfwnB5XxD2rijtKVCGaNSMqw7SnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنهاسایتیکه باعضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/persiana_Soccer/22378" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LnTn1RGo-AxOyhUFfgARLefoUJbGzaflxwgRgFkxOgv4jo6RH1B11UOOVLr2odHtvzsvkuIikDH29TncQ_Uxb4OWHebc_6uHXCiAGwhP1wq8lH8GTjQWkT3WqyV6Qa66HxbTEMMgZCj3LXQum_ma4sP3DBbgzJ-Fd0MqxDvyf4hlmn9B9OVTQcxSXlMbwIaO5FRnwYGQkuHz8n07BDz_vHx1ankUDPbuJlNAkLIDJ4OErVkLwFtxg3rPSRSKZNnbYO8YMrwkRduAZGm_NqUJmFM-EnaOyz7okvg7pgwgDf_vuSfteNs6Q4ZPdRhRKI0vWCCtkHWocBhqrWur2OgW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qujpee2BTT0paG-YbFPH9M7mPpjPLy2ER-bsUn6UWtVglPCa3vMYcgnletWqvhbV9u9MaGsfSG8NOztxR6ukYHdRUOyZ28CnHBIT9Pb8MI4WnAj9YG6NYUXaTY-4smiueZLkx6CUwwds7yR9nCIG_VtbAM6IneCZH1jHe-zredlW0wa95GRSPsHmLZ1_asxKRq3DMXuGlCYPpgiHuj5sFJE0rFqsOCF1-B2K5X2ueQyvd99JxUJYJXnHhtFZUq1_7P7uNWbalncP3W6PxTvPCo3KQHkbzvfduDh8cSQnFXQWG_5yWJ_X2gp4bgyvM5_FnmnCm6exPDKNPydDpj9inA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6MBLnnUevNHt1JJIOb1s0YSo3KAY9Bak3hp9SE4qLim2iH5GT9wC9zgmytJYqTBfYkvPofFsaMCTB51ttXyDGzcSkHZNiE6DJR_o6e6AhHzr-XWQ1aeZHbq6ryHpBHe1pALGqOVrCZasTbBv-DiOEDE4zh9Nqo4L0paVLVoXM87BT4KVhY63rNX0Tm48n1zsMvq-r5AP4LrsKloJjgEpwDiezOZwwxG8CSFC-fgQqJvjimszFlNRkQNtt0lXcd0_6I9lOCdXCjBn_9-LgB9zAwRfYp26517RSeS0PExmGOspBC509rCMVHRWWpsOw41Hp-C5ej6q8W2N24uvBzL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAXrXdn9yQPqxpbNTmarBBvdl68iCSe4G1yHBJuiCOUqrQSJuVtFcOQ1LYI9N_Oe10cuz8wnXK3B3qqNr54bXo2bajlQhTgJ-shmDsuVcOAUBFUbN7pmXE02Kb4NAqVoPHO7v6FkbPA6r8d2srLMSUt7hwpW6TuFOhW07vGIyy0wg4KGCqZS08SeTthLkHrxUtVZxunCGxx0c8GwYte9NuvPTwsi-6p4QQTPd9PGqFq5iK2GQDLOBobDNfq5TwTJ8tT31ZqBKjwb69_ZGTijpXrZVd9EbQOZ4N8WcKrA8f7dv8rClaEPpedQIbO9jGHNZmC7gWYbpyJmCu_gVZ6bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUl07PLynFV6ZQiLW54i7ttZNGXmXwGJKYe7eR9ZHVa4nFlsP1Xcg8Xdg33uU9Xo_M_3PPdHbn9A5ZkKj61OVEdo4ocshlD9hEsyq67snoPBzB7YrawAneGl0TmEzgcELdfuPl0zkwnDubcjoer1L7QaSTVxKXnIO83xpc43kUfXfoIdP0R54pqjISzCFdaYhu_FEoD7aweDoYb3or1n8FhTlFiRSNCR5R6j4eG9ErPvzHaNRxbCVbhkzwrCPVcRbYNAmWzZmQUXmRGzWsF8mXDaqr1pq2ADlSjWhU0YkUEsEEsNmfXDWGK7qLfROZ2b-gJppTFYy6X5YBd3ZSbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=c6eEGrctUQFPSvsc3g9fN4-P8OAT0IBKCAcLqR0RnY_zJNneksTuKzkmuvkda6YcWLWTyhDNuMqkDHjRQvFmOoThdQLDIzIoVDF67esyc6NNPeLFnDZ3HTDr5i8jnag4kKfGduTRnVCEl2zSqeCmcUt5MGtUXqH-mTe2RTi7E0wac1cw3Ew0HU5ONxnkMX45ZCm2ZZX-L01obdJ1If0vpdTR7-85RjBvCH98DZAiXMYR0QQAmLLWwmiqroKtNUK8c5i096s6WDMYHxzeYPEPqPkFgykIuZSKi5gCsw1LPFPQm_tYfq1NtEMZCrTjC-e-AYeAPW06RlwA7Db1mFIsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbC3f2WrFQo0EwfqRE6y5nrVy-soXSYL0Xt0EzJMZ7TTfTrwXJfC3xpEQywdhWZh_snOOTquMp0yYJImBsOqttCRINpMnWJKEzZoYMHMUYwl6u-spc1ZFfaKjRHqZGlk_mPf06Aape-7pTu00Ifpv4Elbn3n9ktrMrVVwiwf5D1mFLN6bgpm3QBUR-ruit-OTd7bdPCCFxjwqFuoQZFHAAcV3nm1RjNxkfftk9wtU9Pn3DM4S74zdj_47S6rNtmdaQBrZnpjlv-t-rTpnxZUW0a8jGAmGjrd5UiMKOkpEcECsVhs4L0aaU-5E-nXzul6mWiULX7p2y7OPlw9mVJ5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IygrrdbWIaKnnZpU7SmIkfW7ZAfQCis2tvYU-q2jMjW5hy4jsoIhLSWjG2fCHZgV2G-a5fQ0gVrk3XQmLLVZ3K5p0B7IiBnhZz2qZWqwIA6NTNAyOm6ymT1h2-H2qM6AjFE8lZopo3otTqR3UfUKT-qD5DAHzt9DU_-cPu5JZ8GaFB-n5dZFVM0Q1yEIzL9_WoiqRLwXkXWNsG9Gkw1mKuqt9ODgM_3dD9PHur71yBMTV_xlb3i84KkTXqlNuA5FXwrnXmJ9Qhacc69c-1XJ9bMYouqOkffykyk3fs-N9Ghoso5HwSMZqkDMQbFsVwu8JvGECOmgAUBoHvKqL7QWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Guw-6r_dZWUsVgp9rE_NdZShdF9GVvZn4rbSUFZYOt1e92e8vJgkf8UEI-uPaCHfw1JJ-H-cueAiAX2k0g4JXBngVY21kD1Hb1R9v3GQViNIieHXZmFhf2upzxPIH7QEy0eWK3B7CxJ67FJ_yqWdvuFrmidtKNoBhDhBGPDBANvKn_fWE_ZAQu4-DMhSYq6qPuoCJHtlaz7fR_R6s_UzB_m1MpP5jC1c-dwO7KdmTFkRAezuBI3c5O8m3iv5znx5Y1oDPIe9LYuGp5LgY8naoFXIrk2k4w49ZpclDaIaSybPEG4Mf0PIdBhI6XYn6nQ2wcDTYnXuOtsJcL7SaePYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=Li5SnV8WfkLUNdiBHndQPbKbw38p13AbEzbgo8gUXFkqMJ_HfzOXrHFS4mImG5gC0OFf9ee5rCztONZAzaccyU-jHiLn0EV8XNFLuXewhq4itQy7YPI2f8GZQHVU62E3ImBDU7i0BWplWTKzZKsAPYGFdOpK-1iB6uzIBIwAkoHWNICFkMWvZd-SimEIt3BwmB5tHqbBdixkgY5NAyKIKdmwrJDwjn3q0QcTxZkBmo1Z_H2fG9goc77oV5BJyB9v_xaJfKreOqQe-8UMzY4nI3N2XHRXpw2Ufna5jjYjksHjY1nZeiAoEoZz56Cq1dR-lGt2gQxM0L_DCOXb8LFbLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjzE_qm6Uw-sR7yZFeN6qeQVCbzkFj2rvYWHQP3SZ_88EBExhN5QfmOlL-nyFCG6K6CAiJKeCA9DRA6yEfunxYw0IP_XEP4bPlqYwc-53KWkhV1ZogVPOGprU6Yys_YODvmcWoXpCb2alBpsxIiweTyasrvAO-2RqTgl1zAdqmCEW3FUG6x250I_2vEBXYEauVrl06_IGiSQpSiMKdFH9GWjcRrF6_8-vr8HBqnXKVfRQ5sKbanCFI3jhoqY8rPCv2bxy3RY1SAdnpRXfGkI37ebPdIO-4g_n899tpDeQkER8nZmQGb1PqbUh9G3utYvl08A3w3SqL4OGBRf_N2_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLxrQe-gCsYQdz2IUEf592FjjYMmWBU666NDoTC4spS7SGUgv9YdwAAAPdmFsGBvhHlztjzFdSSJAf5dRCqKCFyg7Nh2GP5o93rhH7TfCn6PSa_pBIvmRuhyOI4NezcLrIUutO5c5JhG4cfnW2WJbN6Rp0AV266e24RObLlypZRw69Y6TXnjlK5ZfVdPHegFzVNG-OfFWjZZuACs0mOXUZdYXLIgkyeHrFExp4MGonJMpYzjSLKDN8PffYwGiXbDgLkkNVkOa_8lLRNEqkrX0a8ubOLFhBvvCNo3aW8c9IYKehBvALpyEdYImtUj1g5tn9B6j2Zqc_up79AZUeGpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_KLKLdRxyXnlvVrQ_J0XzL0E1Dm2bnGtTe2UqKCCkpYl5bqhFSmjlTjZlDCcnkvC_9fh99Cv5LiQHtETXhlzj9-bEsghXG21OdL_0y2eJ3aPi-zXNSZfFe-rwr7qAiUsxGT1HfAsifpUERl0GMD8i7ne07_HU5bx8nMuF-M9xiKH5s6Cx5I7CvdSaoPNfylMxGEYVAXPnHDOwr-1zle3t3Dkxz4Imy87cFrIZA6i6evZheGmLwGEP7PAuYcKJBa50QJmBUbcx4NP3XHu9LzaeEsrL3Z88xEN-wODHcNDlNa648v0WmSQvTBYhvKbhcWCQG0LZnJ9Qop5r61vVTzYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owB7IhEE_7KlXugIvpl5eDTXy1e8lYLBwxK3OOg7RCyyq-STVTUEvIw8zXrn2Pr16t07I0JhRix_8nrCdg-FJhvvB9X5V-jHkYjQfmxR1YhWYWJqdBlRSV4_ijrI0X_YzgX5gDwioLdM4pftAILIHkaQuMvuNehrOk_ZqivZUGQMuEqW3-lCYLTJLaWfElpKaADOmPS6gztq73g42nLx8i_IPMfpXZ9eQAJ-sqaxtsl1onjjxGrZbJiXv7hZs8NX89c9hHT3uj2NMggJ1bOioGcsuGX4sR2RRvvf574DZZUj4SVS1ujynOHfDNANRarqcupy_jO6joZT0Ip9_qKMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=fjaGFx2g0m1igLXXBnLTxMOtW0sedPSVWWymqfc5aHTIUKCN-HlmQo5-w7ZWGvV65dcplXpXHmLA5RZVp83Cjo2rCPqcmqBbj0iUfCzz6WiD574E37aWeNTSTZ3dOm55t-P20EzBFUVqBJiWmkaTonbQyHSDxhOGpbcyPzzdgTSmwsOvuqPh3aPx2OFRaNjexvztgWaRhHYjsBQRU_RzoKdem1Ia6fPxuULeuUE6uj3FoqDrRmnCJjtYIRPZd9-WvJ7AUq_PBAETP3WZ3vPBlvGnLKmk7MAMqJN8ellxxwxqI9Ysl9-6t5EDkDCmYp7RfrG1MertTJDRYDweSXkYxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq36dL29N7GkQM6dwtBi9cv7-2oXdccHPogBxXjaWOb0NY-Ox88aF-zapYVCJCm_lvfQeRTOwhEvVTey428vFxq6jPi9AKsf0UraYW5PeufG5w3REbOezR6_v9Nv2h3fo9wFdC9NX731QqxQgdn7c8QAwtKV6SjTPmUn9CtzRQVYvKUGOw8DAKn_GGEkvQyNsRW4kl1Zz7Zcc0E0uj9V-8YeCb_kLfgJS9FUriSMWxV62qHrlTeaOFI1X1TIc-yKqe4Hr4WEk18XQxrV1KAJF1CiQP9DuorH-GnhCKey7fIdqGTWKNogG8awpUUytzW16A9R-U1l54YrDU1NAeUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=Da5jkPAF2Ypo79_1tzGKAHdid1cW6UOYjJ5LKcJ1N0iSp7zQjg9Y0E61vAHacLn8mMwxoeIWkEp8GEA3pm7_MzNuQH9SW9gSmmS3tz2oAVlJwmfOLXG5umpwzADlqn7Vy6veouZZP73LFKwWgmVgKDDy9w6e34P8pt4YjKBe_adVELooJNRGw7aml9g6B9PuLBOITdfGbtiYrNSFoakgkzfF8g8qPOXoxHyapSnCSL65gjDrqFSmQSIGIMWjaAt8V4OC_fZOk_0oTnXwSDrLbtszFOWYCzYDe6-XrWtFwahUU5BCebG0erXT7m7Jh1V6hr08TIx2tjNvw8sKSmQNRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjbcRtSnIUQZCdlnmg5FhIX2uWLOX2jAvpuKLDfHphEEVkuBmk3WQgT05SUd-bcXQiAG-PbabrNuVjFRMWj6k1-jXKKpn6dq6ltL1OZrbxpVM0X0iO77c3poqjsgURssSwB_wqPuAhTu0O-s2qAGdV4FHSeeqj6RAUHu__olLCu_i6R2YJSaw9FfS_liymN0wA7vheQKA3C5AalmC4LXfTJwMmwJXljtkJjGpzoix_CBOc-0DWcQMPrOdpRaLWoeISBNtud4a3qbOjVtO8q8h4vJTdgcV-iTb1gTECuFUshzQ1xO7RhV4GDJY-k3lpLW8YsgUjLZ1XupJvR40yR3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDZ9gkrlwbN3ogcGc-h0mAJlmktl3n8s05UFkcXQzfMRVPzM1hTOqimj8jFyUsyCjLVdSrdghEwAGHr3MLBPtT-KYJ5PoXv0Gp4a8FkQU02tASDudee9QxjQ1de4gzNQp1lQM77KfJvmf04izsnJOqSlDWXRqTXR5vFnr328jfs8ZNFOeBd6IpA-QJrja_bxtibEs7CDB_Ppv4lZExrDqDEJzuIZqezTaR029z3eX9QTEOjg_t1fvEdT_8pbN7WXXW3od-o5_sFXtheyGaflry5tyjHyxKlkH0AiHKINWaVLxfkGtpUkK4cycSThTGuyH0a4m28T0wFxUYXfx4LeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKDNEi_hDRLqb5Mv3IU-_7Ingqun9YezsGNuTAc_iQ5uHN0OEeWPqgsOJ3AyJIXMMmR_l4AfwHRNMzmaOttBy4n_8CWFm30jVm7frtS278m9AbzeZLJ5EYJpHtRSIHPEBHyliTvR31L8y6Hi_vqSEo3U92Q0OK59hSpGIc1yNDXuyEYV9LbezqPvTaIQ6RBh1k6mvOwxWLkeaCyubaD9_UsPXe1OiOJRUL18VZ-IgdJFQkt3HBg89Rg8psHE6iXpESt7BnuHD-AllFKzGS6y4MMjN-vKF1uFv8epram-XHORnFhC8CV5NxNGecXENGT9zoRCSkg8zf0zJxUOivyhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO48vIeDxHM1nQt_NHa9WdjnITW-IaBFNn-AqvsMH4oOjU5u5ZRIC58a7URUCoy6g_oJiLLRTznswg2I5OvgbsDUExZSDsBO4IYMU_Hv1qg1LrMAv0ojJ-EqQvNbBgjY9oPRwFBIgpx7O3UO5-14mkU4r19_RmbfEOSySeF92SjAZkppaUitdNyD1aI100i4Ubd6qECnF1vX-WKabZF7PjoRM9o6n2LjFOphXXXvQyKaDJQiSZDNBYurzBq5qHwMLRHmnE2UPejzJm48clI7a6ckHfVilHZWkuRdSMhJ-TjFuguiS0X2uAza0x3Ah9fiIKU5qWWyjY0U2WPPZV92kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq48G9ecDkiwUIsYUT2Cir7nlgL37V5lYDBsIT0pUI6ES1wS_UVDvVkgLflrGqNG4bX-DhjPTtzroS92IHJ9SOEo8c1SuA2kPwxUbgshosaJI8oMXi5Ya3RK6DIwK1jcJPBU0Rhde8eLWGn1DPQZIWuHneoNtbFlKmVaDGJYarPwy0hCXGLT8RGA4ESEZEUgpLo4N4tEEimcKoUeVZ32d1IDYzyf0BPqGaEYZ5g5Ul6VWjIcv4h45pedh5TRV4IZrMbzKKbiGLVGAOWyMsPM4qWWobWtUCjBJ6aM1lCUi3MHCzXDXHQxu3_U6kAUjgcSA1Bvw3Kz0WoYH4rBIZHNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=LFE69C_Auaj0PSfZNzp-un3IzBXsMO4M3mzw8bF43wZ8QVs4WJlUC77xFTQ8gNPRow9MuBggICNVGmoLGpRAvlMUj1DigAytC2bwSX_NjxJCS8RtoqO90XZ10Qjatn17PybQaZxwlJvKy22rFNzmvHXHe_n8qoUqPsFgTcWGw-p9JWgqbaSUl7F1S-yPJeBl-vtHLhr5xX-xJWnqCIZjDfWvS83Csr99RtLBYqf_7yYVfLt9GoKxmWyo085iHuyvd3--tokmjqVh3gwtEpBS0CVHdfGYY4bMxHePN-1WmGJmSshiOIy8EyTowerwzlhRwlN-HNQRJ7Dx6UUQPcc8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGyuqKJyYz0W6VtwXAMhgyWJncdL3AtBLpeA95ylnc7uOb6Hmas8DlP2vjm1qidIi8VPf0uxRKInAwkSnGqlIvd_KJxwfkvGneqYvjmgfMOEMnBEPfif0k10ArjY943fidFPpHp8twjt3BXbMWXtqh0qifWipWRkaSeLxPs_Pi9SHbV_Wm4PODwKx14OBRrtfIDQcFYph5v0LML-gMH8oA4ylBWSA1YK-xI09jBQTyNsYScz2bTEnWDGSoy1unGbKyGAju3OKH3WnvPrb5AaNE_bX5aXkyfa6bMEY4XJs5A82J4lsqzIfnoBs6x6cNiYirOm5mvQ8pcS_jqyOp28VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOX3f-esiDFPM_f_SPAyOP62aQ0b4tX0C3JVj4SSyU8sMZxa32GmLewRruk61_VWqQB9D4DfoB-fijIxeTRhhRy7sqTVdMcDJFiJWke7NCRL_Bl9NtX2LcYydGe6fvZK6eHbi56FRCiFrEnneabRU3-TkVOVKke0x471FFnRdsQDu8Z6VfjyWTMTt2knvPxVZ8N_cwMTIVBDd8vlDyg5ESyD9N7MWVtzEQha15qPjxmA9JdovHkXxItm82Tem45mwl-kF3brLVPoCh8NpJE_7Vw8ECbVrAqnkw0u8FlIoFOaFembUYGYytYulhR4Se9Xyn7O1h4xhH6bVaQo4cTOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=fKQhRmZwoy8j3iW4Ep7Fgge65n2tgFz2b9QqxIyRlvQNdv2sUKN4nlcMwp3RVPLNgxsNGlEaiP_gb0Lx-ewTzcOjZm0Q4rpskxWK4WS_XDp49b3LJ0O0VknkRwOv92rOcK7RQZbRvqKwIf61Sc7g_-yBQFbyH3Um89NoGZBZqkFA2A4qBPhKgtYPuMBh4Z_juyIGBZOPATzCShKQSPkHl69NXYDrIOPmKOI6_u0m9KXzqK26V4s2aA0wwSeDccTrJt0ssL75FR_sGXzLuM4ZPisTZXSoRTJE9YH1nCz8pRyfJe3tu2imcviwm_IiF9WIlkIrPfPobGGtzo05-g0ZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=fKQhRmZwoy8j3iW4Ep7Fgge65n2tgFz2b9QqxIyRlvQNdv2sUKN4nlcMwp3RVPLNgxsNGlEaiP_gb0Lx-ewTzcOjZm0Q4rpskxWK4WS_XDp49b3LJ0O0VknkRwOv92rOcK7RQZbRvqKwIf61Sc7g_-yBQFbyH3Um89NoGZBZqkFA2A4qBPhKgtYPuMBh4Z_juyIGBZOPATzCShKQSPkHl69NXYDrIOPmKOI6_u0m9KXzqK26V4s2aA0wwSeDccTrJt0ssL75FR_sGXzLuM4ZPisTZXSoRTJE9YH1nCz8pRyfJe3tu2imcviwm_IiF9WIlkIrPfPobGGtzo05-g0ZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAuxFc48qk_K-gCFdS452IRx1l9iQWYAM0odPH6le8tBqEzUJTw9RZ7ROqZCZmYbhV4Pu0upIzevah3N9JcuWrqe7BKC532DHoVh-GwNARUwZ7Vtxyr6jVFYRsEVVNnIanOFQvGalaW2DhzABbNif2rXHDWDbwsiMNEmbUrCwWRFlIu8T37pgI8XRDrsGHTo-FqkYjP-j7k3n43I-_bhyM-laY9h3lsWsr6ydxUi3TGBqCU_8lWR1ys8rLkJaHBzI4H1fujbDH6lA0FxLiLSPvq544iUMdrwaOyFIGIGrYvUEwn5FYWmGlb41fjWwfxRYu10hvoPssNoHu_OZ44Mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1yJW0WXMeCWizC5LHbFHNVYyzYn3IZ-ED18r5lU4U10jzfAyEoIGgDnACogi72mgkNx5sV_y3_vTFQ25abGR7C-pVSfzo1RbYGlufvQHV-V1fiFM87pygqQywj2e9lgDAXUU6HpacFFxK7wcUGPH_I45h-mJWUssNNZBDVvbS1F4JEJk0Kd_o9iQFfs4Imn2Os_YGJD8vAj7leU94ZaEPleGlv5qF0Cp_ByvM6_IOh49nOCxDHqfTWpKVd1VdOCJFXGEH_oVdcZYJ4dXRE-XBY21uD7MXcLLbQT5_tyGTak1U-7M5R_agr4X3ONjYU4dLRKNX0VeNu1khcOlR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4cIjJQppHW9J7X0Vgwtv4K7J4BrzOBRdWd2Be4l9V9lB2NQHnmdjuiMy4Srmv9NmyHGiwjpCdJGqWMCOEhY9W-8OvxMjijFs2K6pKpEr4OLDt3KlX7gUVsUlXmQ1c9B0ns9soUBjRT7KcMByLlAULAmmVnzWcJ78owM6sc_1Ji2DdqVGMNh-WfOnRx6q2Sd_4I-U4GSUdxYnNqyayrZ7SqRa2_gwCPS6Et14lSqGQzcfyxBtkVeeoKCfRPWtYFRACNfwOK-j11xSX81-ESbZp9skObfdqcKn-QG-T3rrxLX368owUgBdkVxTGEu_2Em2kUMr7HHaucB9mqo5tbdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQSY_CJFRLFB94GB9P02ZrMeaD1Vb6-syWNwDLlgOCJQ5yWSV09fHTy68Zf1h7XuNHCE1AVHtWqp2y1Sk-OaEM58dNRGiLUo_uBZcS46VM2vV7nSkLkhh1IUQSZ3F8NsaQOWkTvMNPlXEKoKWnb_vEPhQFYyx3A5hLSxzfKPbM4P4Lei2n9E8FyFytk2fEiN8qBsXcugJuNQPoW8IrVjYP52VWEbhvI2vo2qZArYUYsSi3xYLwelciD_YmimvFeFmkwQ_8dUfpDjKq4ps6sEXZiI4D9RtDNRrMsit9aMvTEjKL9LYC295KqOZnrFvvO8QhY7TTzxNFmm8296mCRH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnZxYdq9BUMKYTkAEEjH08V_aSi6iOcntbc1JPr77ABhqWeW3NTWRSzQSYv9LCCBUgO_cezweoHaG81zr83beCWfkmUtZWz78kOMBAXbixm1K92zH_kUivux6u5Et7PbTD_Umpcy139q_eea5VPtOVQCTdtslzs8BtZP4W_n3HZw4AY2NNd4NF-OyQSPBaxnYycbkzrHUhqFfwA4OPRBOx2fIzQj_kknlCEoReXyAy1i5Qtyj9GyE6SfblwOfpruuHBwkQrj31IvBOW1l1IDI8VKEmNxvxa8BNl2JsVXrlC4yHVcptu2mOsD20NDYf3sPMXta-EVq9MjQDpsw1wzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpKbdxW6yJ6i5gTNxxnvqKgyUYuqmKdSYFcdfEiykFc9TducFcYs3yzOhh43nxZrQnPOvHXhNzn2tRxj7Q3U0VzpuQaobWzAsdUEOluDU5fVQrBadXNvT0-AFqds5sbDHjoK5wuhfO8Qn895ttTpwypy85wbb2qfMx9NqJpNG9ufZ7w3q7RgWUhPxiA6qDQLekgcPSGtg8pkB7x7R5B523T92QmljoI1Mtog2koX6cCsinPkATE_ZtjyxxJy2lMkrd65jyBtPUY9zIjKoHdBaw7q65VzjSuqx1LygWsq4_UKKV6eci5i7o3yOrk6EXsa6sRrRPYJZ2WVm503zSFKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2VJM_x_k3dVQ-QuPjSd0weII3TL0pH8hxYsLRffAOhF_PngY3vPpZGoNh9Xg3UOpc_CE2u3VCE9FhmSEjcKWP4NHaabi7LMrJRwsjgC7PEzxSCAsrQEO6ov3gsqHKXlzEgkklWszgTM2EsOqDqSCg4bYKxeYyDgmLgQnBPdnk0gw4MMNv4Yz9UzaogQ-mhdKFBvgUw7hfTZ8j1Fz6ZgSXpcoQGGJ76Bk4QLE_eDfvT_ywCvjxrWXCHG2wRNcLKIgiwu6hBCXOBQ_e70aVnKDIo3c7LGCBq5pAHvjMhbiEOUysbA6ShyiZ2pOiIzBKtbMugZ1IwH21Ttmr6hK4jWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sumWYPlYxFl3-Hqi2Ejk_4BIoZrjxNd8pDP_FBOfLPQ9md6YU845V0W3rX53EhbRc25nRAH9OVKH4d9HjIT5KNIIuWfVHbLsO4LAEHV_qOslaw9_EHoVPtObyYZWN4gX0VpnP_Ddr-H319eorzWcY1Xl21ayBiCvWwfucNRrRvDwNdeN1zkGIsKMXygdXdOYpA0zQe8N2FdpVg0WtBrnskb7ZjVsjj-3Tn9Hs-iJKXMWM4cAZsUsBMbpt54zYWIVfCNSdfayOnEttNQzYxo_nbI91oP3d6KOPBNftR_5PBZRXuYXQ07gCgQhfg8HVUar5bJQ8JGV7KReZpGfqbmI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRr_0rEDfsAwJVoAUV6DIbGZBrsYQRTqG_mkKrmEJYQZfnBja33CEjS_f81hsXuLjmLuoyAdLK-U_ljq7RlnUKlSrs42tuI8K-3gCVKYCbpPhEvPFHNo5C0K8j_SFmWku3Nj2Arck2R6sxWeSfdXNCZMrfZuIctxdBny7oWqPQj1CAc7uIOZwANgbaGEL9VRt674-12Ya5F6NJ1kpWhQlHCAmWUsv5_hzbZ4DYDFlZRg-jB6dNeFuRKeX_gzbeg1Xh4dKgG1THeuMYY_ArIxJ_VIkLLuxAZNrrgF8BtAUE0Sb526ygZtfHFlpUu_WB3Q_u3gYuKT2xiAEqQy-07BBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8iewoZd2tmVxx0UGdlmup-4--vLkxDFtMoAm9-HzqaDLEGtaxr7OMaJmzIy-GkW1Z9xjtLfPBEfYy0gEkYJjQssQR-nvxLiIAkLg56ax1peMUuJQKt_T1_OMyKUd--2S3vuxGw3rLJYMfpQXygfRy8qetGT18k6kNDXZ7_KLa9aVzLtQKhp2_3Jqpz6YvAgmbr_pjH5CUgpKol7B6bj2egZVKpBNg6qnKeXyTIs_b7C_jCMk2yxGjdXtL-X-15WXUPdoHmklLIhRkYK0za5Nxhge4_rLO6vy-O_7WcbHc9WYicleguDzTTLYZTzHOAAAGOK-eTBlBQYWqILVKK_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=kC2MqatoMBxcwAj3pACQZ1At3VPanMgiGlrygE6oVK6FLk9BBrAflQmPmFsKhQxMvnWFUa1VOQztOJgdqyLOu4KlnfTlD3B0-7ZMVq9C-U0-MhpEhfKKvf8y6bhLql09wgXf1XMZ8MdLCVAqOj9RBEK7moA3lCS3QqIdcYcK9QNq2E1K8XSWECZnw5m6Nucm7qs07GIzYYE9rsjUgWe8ZDTQz_WnqgBqOnS3Yr7lskHLiKokZRarMMFJhfJ9z29u9_O-FExGaQQn5xHihf9bg2zdVWNbZHESQ6dglVz7SpKW26lgIu6YyxTuaITSxOk265v59W2xFADN9kQp2t0o9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=kC2MqatoMBxcwAj3pACQZ1At3VPanMgiGlrygE6oVK6FLk9BBrAflQmPmFsKhQxMvnWFUa1VOQztOJgdqyLOu4KlnfTlD3B0-7ZMVq9C-U0-MhpEhfKKvf8y6bhLql09wgXf1XMZ8MdLCVAqOj9RBEK7moA3lCS3QqIdcYcK9QNq2E1K8XSWECZnw5m6Nucm7qs07GIzYYE9rsjUgWe8ZDTQz_WnqgBqOnS3Yr7lskHLiKokZRarMMFJhfJ9z29u9_O-FExGaQQn5xHihf9bg2zdVWNbZHESQ6dglVz7SpKW26lgIu6YyxTuaITSxOk265v59W2xFADN9kQp2t0o9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly5DQxMpZ1alUVKxw3ligcz8-cdy1qIcp2Tgk3YZuKx54Hqx1xNrgn3N6gBY9-pp8R3M6odEPiN07f0W4dp279O-i8f5k6kx83NbE4ir_zr6sWrtBfCcLONeqM9cpbBouyxDkxYpCuXBeJQoTQ-j4SDe3iK7esaIH0ODGOhK5D1UuehCoAbytJqkldV_8v5I26GztJJcZkPOclR9hTOm8-vgogBEtt9TtE_H7ez94b7SE1WGXi7AR_S_9QSlVGLQRL5HdXG7HQWD9ACcTZ0obO476xjbOa4nltbumEReG8YZkfSg9nSxCHnRxAdOf26_eBhT_FowxpDUmSrjFB8E1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avqu06RBH5OkN8P2EEyrSN1BMYKs6J2Y_u9n8sVq2nZ6BZ3rXz6W7ODrS1WdL-sAjOLH6S3E1d9345SIDnNnZZKU_jaBx3dW0Em0sRLiXt_rn9bEz9uZLUdc_LccoBZtSobKRVcJ-g6zRSOPO1maMZzwvHIQ8cUiaRIUaC2fq1ivTFe9XToGH-VETJHM-K4ViLHqCrW8taFgXjH6UQBf3JYh7RXhySfFxsFTKZZs13C-3yC5iQk2foIh36ssZGDkOZ6WjjY6dxCcqjxt5YWzocg55qRNV_kVmvsw1994Ap7qbQCa8b2wHOsB4ilu1PV4XPxZsEbZc9EXqnTSSUP79Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFwe3bgpyu9HkRx16i_oASw4VAcZEmV0EGfZuWs4vKpgknLLD_eqdIfBxhjNLff2vSgUpcZ4XmSssKBmhFnZBUljzHxw6yyrWR2OD0uaGApDinEkjnUGfiRtGgnttfaAHWYDoGChmbCXXkSySA4z0yLiirzq5vsIApo7YNyACkwM8eX7FaagkAz2vAhKJ7NyeqAy5lVme-Fne9ol0uewxppTVaBVz-T7qSovcVlhZH7pejIhNKmOnUSGg7iOUGTEoz79gj6D1b1TWkdZABSAYyY7QfFx42_Mo5G62CKmtIXmAXN4ROUC9UZTsJzLe83Q3WmPFVBBdLYnKl15U7Tdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsZlJ3VYVJmd9XZiVVmVzTwpz4KvFGLkwHA4Q8QeNdNAqObuVEBEi4NsaBK1UQpQr1MldDIJfP0mw8wzx6miIZNCWmkLlsYMOdU6avLsCID-1VqWvRs4uHIb5imfVwkxIyLqHNMDmwJjXPVuuSbmdExDlIFN0_3yCooikeAjSiaxaOnsRV3CV14U_9CuclTJLuNZT7OK6qjsyunn55ujvB-a3kxgANN-gi2dmV9qv8jySzLX3oqYlZbNM3mVteqRRkxB9PLp64p1QDUzGSdg3WJxnXdKaxvbgNfK2-YFe9QfGrYFBxgaY4CfpfY2CNQ5NuRSBg7I4e1josqGZRsx1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBTgQACfYl_CN7dTBCruiojJH7S83Y8KNhxrA5QSQWCiDksSJhkYqdHVqLxMB6XQwcdglK_MI5YXDqooduH3XtM78AA1LzOOBpk2o2qWdnOXj8rJwD_YFfVxZSlkyMLgT87D0rFHvcFT003r82b8fXFfResjB0sBcb8ICEyHE8RkCCBEt52J1ND65p8G4f4ubBubfHTgZTLtLDtC6CoZuyYjNy23YeLg5Ou2q8MdOb1_ApTfd5j9OPpdv-l1y-dFVR2x7rSg2z9XJONqdsQdvU4Af7eYJ0MY8qC7Wh-zqiwGA9qZxmQ6RlxsyhsshHvkmHe423vO-nlGZknY--GQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXkikDv1tCERlxUkzSosOu0fSawB24vONvG0fFo2NuH9VXdKCY0KSv1n3h39dM88NvIl7fhaLsclgrdGARG8DcShktbIw-0DEZ0cZj5wWt2W2PbV97AJRyhJEy_2URFUGcBkCf_v6VMYWYvLbcRvKuM5ExpnRtWOZSC-iFfpZvzAWHajoZWivDeOMKuMmOvIUOEbg-LKI21QRNtE73387OCmaXuhOQ1hN2vTkTtst1CN5WkFis4ORW7lOt6TbwMp4Y3zCKfimmdiA_dMSSs8oeC1fn2QcQ5VPm32h1HhqXr_E0B7FA6_5efeSRSmzmbUu9rzNhFk6j4EjI1xzsrLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm2zkeOnUwXaUElQYcBC2Ap4FFPHcgDxq24HOrDTB3GFaEnuMjTW0t1ISk-2W_nGclWmbREm3cBowXkllcCnxmXBGyO8LNdIFcuCMyhLnDUwz_a2b8aKFUfrZwusZWLICV0d4zuMRuwKCjre5424l5Ri82SZ-A7Vu5Acfto7M1oJETGcw8Li1GGyGI78JlLrz19Oik3lndCCQQwIqj7CzedGdbWTbCimIGDiLNigxbKTAuq3j0Va2tX9t3FBd3B808X1es4Ath2HliU49p0VcAfR8xZG1MySMz8tZBxFEp0jrn8Rzjn2O1ICnCD-n9Pi5MNXQ3qBLaeVO8g_SPdoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=bBdNveu9r0HxNkXutUtVeGQ_aWioAGmNvoSOGHdQtk8IfnrMeZj3UvAKkLefDiBbvf0xu3bJESWO-CO8wunuOznEXEPR_22JH4lZ9xnNwFiM7NxfGREjaTzt-HBq3ojqWUO7CeNcMlrHFZBWj6bDSpytXPSBCHTYklKgCbhccgZCCdxK2d_3k56ECj9pd2vkXgqIFUA1DsK5Sw5bfdeNR8fij81eHO6zuT2_VdQt8w5i4WvWcBrpZ51hv7TlMak1GH_P5-vM9H_4jw77EjbfD21c90yO4gXClZeKP0ykpub6N6WgvRnmeKpLPJukJ1rdCrKuV13x7ihYDWuP3dV7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5cIwlgGOMHyYhaX5-P76El2YvmJSMmAtb6YM4-rcC9dRvawMLS0UbI6wQ5zBw1gkEIuStQql-52DmZ2_apXobPndpQPIKHpFZG70UWdE9RxnMZeTsmwbIVGRiz-iLgyqUzwFmmuToRg5D_F3RbeD-hZ3buB-LY0iSAHQ3WK2X_OimW650lm7K_mBwS69LHC1NRle2thhkwLwyDfEE_YXv0n6xPj1L5QN3lsc8YTB5jqCQg22vOJg_VsRs_EGSPkGW3gk95aRRSJbcjsnKDrHm3ALX-ePpGY5qZHwiPv3catyiTA9PD021gWGdQy2Zw_8uM0_W9HfQElbMq6NLUCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx0CFP7ssfROuJl6JJqpXgMru7QLX0MOUCaAj9RG55omyFkDNlS8zq1dv-cOKwNOBH-wm7YFjnScG4t30tTyaXphYWnx-lgy-N_ApB8R8HDYUq9zEcpfIkdojwlHE2hi2-sZvsleFD2EgIORxZZ9Q9yP2mPlyZSY0Hm2K6ykzW9yLMBa8WknUvc3mCQRoYGc0Da9X9ZkbgX6bHaF8imQrxfYawtnUqoS59abVdrK0judlwEI0f0UQLMVVQXEEaTEK8nXsPiFd5a90n3lFTO3ddLjGoSQZSzJ_f9-QASQmfBkb1vUSP27k9BJvPqrjtqljtafgqQ2G52uwvxZbqggIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=CdxVFovPHXwjq7NS2f7Kz8MwrgWG5riz3LjUw9DOmkpFhwIPRaNkJX_nJcoGHvlWP84fNAUehdIJzONjL0U89QPlwzKUIEsTR7tKsn7w2C-VUSl4i4Eto0uN7y8Z3XQIAOqMk6L1RSOS8b2rqeMdIXOThfrY9BZ9oR2VyO1kZ5UltheEbj2DqtzdyXmEd4vrEsZSHa1ThVBTGHG74p_mATXEK1TVkIPexyG2vjXL0jaYtwmUo3sorXM7_tqdbTOHlacHpATL5EcEyWhlVQTUhG-ajNbYqHM4DNxd8_Nwx3p2Kd6azvNkY4HQEaXJqOLqXtJ978_0zcGc4l_pGVO-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=CdxVFovPHXwjq7NS2f7Kz8MwrgWG5riz3LjUw9DOmkpFhwIPRaNkJX_nJcoGHvlWP84fNAUehdIJzONjL0U89QPlwzKUIEsTR7tKsn7w2C-VUSl4i4Eto0uN7y8Z3XQIAOqMk6L1RSOS8b2rqeMdIXOThfrY9BZ9oR2VyO1kZ5UltheEbj2DqtzdyXmEd4vrEsZSHa1ThVBTGHG74p_mATXEK1TVkIPexyG2vjXL0jaYtwmUo3sorXM7_tqdbTOHlacHpATL5EcEyWhlVQTUhG-ajNbYqHM4DNxd8_Nwx3p2Kd6azvNkY4HQEaXJqOLqXtJ978_0zcGc4l_pGVO-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNxWicUP-nLDEmCzs0uzhYF4yb9IRnASqPS_UYM3Ft2B79Opr_jnl9Z20yAejqPbLVOhJR3AVm5IQagmdH5Gbfn7_W7-kJ-8c3KT_9GGtj3gLqtKTGaWeBWIqgjV-F2QQekvGdUYtK8PZXisoCGd5uOFsGr0IeLnMmUkAasBf5m9646-ANlFfsiDNvJP7hh6PrN_T1ZCBLEkH6kvSOD2tp6yG0RSmTkHDgQsSq7t69yUu4rBOj-HkigHVoixa3IYYxLYgxvjy0YZ7lqdoqYmJLhF1TxPq_uzxRI2A-T1GizrjIiTGDVsM5P_0VolOEXCMo82m0A5jFSHP4cOD2jXVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6lbA_W-JJgH8zDcwCpd4lEGTsFqWNvS5el6vWCVJ3ubTvSbA-YLjggXnCCJav5IsDrNr0b_-FFcXjRsTwduWLOnLhT5XhfMFxuQnmRAxXoBCunMGNbCtVQE-n4EvpsqUVkqt305yWrhCfYP0fERReR95gjGkfzphdgFw-GEWJVPCM7R7ttLwWUV2m57-p4WU83NPeeBqTN3edN_IQLfO4PLvCzFtcUN1kPlCP7-MhyQdYF5HOKLoiF3oPwyBVCHf93o0-Q9AM0d2-9PUa80tFMWicZwQZoVG7Qtd3vxoDPjBh-kc5kwzrW2cZ0DLy_vI17hXuZcbch4TcI5VpA93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcmeTp_n4cNotMcxKtdhw535Huvb_D9gMdZzdUiUgpNEXcqVa3wmte5e-4hfzr11qujD6Z5-Ghhi4tuSeWxC5n_OZMcoykTRrexWcRSmU8Z1Ls9iBjIWYxtC8gsv_2JOgHdE25ohq64dABnk4D5D1twLN-KcK9vgDIpArD-H04LX-haLPnvnSiKZVgA3HmAfI9tzctFwB7q_yqqwihwfMb3OXbEEeuiqsxL18zxm-ufxK59XgD0wgBAX0RXIwK1QPvUsHBwN5RmYhO-yFjMcq1ukT9l-4LkTR6WXu2NJLOiim4NtgdfGKWnzC17lxTKSOhyz3FTlre2Jwhnpvz-JZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH9Lodb-LL3AlZJN2S7e1ztPKJnLxWE3kcpfNf977MBZe7e69tXKVFbce4i3QuSywatAl-8X7rssyE6KeItSJnyo7Gcy94U0P6WdGZ3ZtKyeLXZjH3wlWGVPVKS5-XJ1CZr9xeeFOVGK4sSMTk0QDwndm0n04ZPv7z93Vq1s4fIpB2N1r3Wly0-8VhiN1D9QmeXdSeXZSGyTGfzsyAA4GdLiMb7oSg07YCnRiY9EvpsR80aZq81oJTMvdwBVHjOy8TuwOLlsEk2wPwoy8F1vW3NB1iUCQYHf1tqnOsFmVSIftxEY06YEmbRvaJKynQUPix7S_gUMvX3GaXrrbfWxYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=sjMU-zSxJct7GrUE-3HlMwnjRQ61RGvGwYMmW3H1V1ibzdWxtEtOaTN5eM4aoc0sO8_XrRKw_oKXAqCyWXTN6Ycvt3LJMKnX_nYol_x3JnD7ECa5q2TYor7CYOR36U66qjEFzghaRlFkP0y5KR1vbkdP8uW_P_O6xAUaGYKYNIex1fE3YtdY03M6asCIsgY_E6UISK3sW0AWtn2uzfw4dsbYVXJXk7PuOBp4WjDZ-OD3YZ7aTyeq7wtY0SD8KdLcf2PtiPapulQsHaK79iQ1-6vuk-11iskpAx6nJqKUUntH_tycRA88JQga2cpKl-uYx2_NC8911k7BxB6vJ9cZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=sjMU-zSxJct7GrUE-3HlMwnjRQ61RGvGwYMmW3H1V1ibzdWxtEtOaTN5eM4aoc0sO8_XrRKw_oKXAqCyWXTN6Ycvt3LJMKnX_nYol_x3JnD7ECa5q2TYor7CYOR36U66qjEFzghaRlFkP0y5KR1vbkdP8uW_P_O6xAUaGYKYNIex1fE3YtdY03M6asCIsgY_E6UISK3sW0AWtn2uzfw4dsbYVXJXk7PuOBp4WjDZ-OD3YZ7aTyeq7wtY0SD8KdLcf2PtiPapulQsHaK79iQ1-6vuk-11iskpAx6nJqKUUntH_tycRA88JQga2cpKl-uYx2_NC8911k7BxB6vJ9cZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxCPPeStmEEPwniu72u6j9NLQQtg3y_hwsv0fedHWujWNWkv1fIMkQLG9zqx1J55aTsGb1Att2G8-AQP62U2wfH_hh5sDMymJadWQmRvEou8F2Kd_Sp7KP4tu-zUJanxfxySrVvU4I1TQZUwEOYaOQNDIiVApVuf3r2H9UE6YGopB53KrwW-VLVTL7mVNQojkkTOV9cwrEhsSV7arB6CpIvosqqaPu3kNjN82zPKNuNJukan9GRIQTG9EyhWTHuKBX-R2zu42KwDDd53q7v38LpUoymDAAnQJNpIJgPytJ7VmV8s2M3XWGpaJFNOK1qA_AbhxencsRQiPkmMTSyzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyrMvmg6bNV50I3WAuYxHJyFv_l3vtEKYgvYIgCrzCVq5_rtzvoGx15twH-wKQORvaSheUdZ-Ps19-RUo06qa2NBvudzu3Vyyc4vMMcYZ17PtKoGtRLVKa70LIGJTDSjIsmg2-byD45XYekgaCK2k8ccXg1NJxDjw-a94nwRyaWPBLSGrbCl37ZQWlzlYWrOsfzd-j1EuYKPo9wVHG-z9qHDt0Q-M98L68tVkEQ6QxIDZdnJJMRMFfvdHZchg-aThcZcZY1-uPwVDPJs2IcuGoTxqDlwH272WY-0OnTLiqvjGNL4hfxvGEj44vkcIg31JE7jzNqQpT06UEzk-bZEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJMg5-XyY9mbUA_qrTzIKvS2KonGFgGgYl5iBveikXnhiG95m3B1ENHxt1BuimbMBouGJ1Mm7fhyCtqpRuROPU6uBzI1d2SiIsM40lvFdNqxweWIFWVyH3z51ngthTzICKsYQ0vhvja4b41JC3qCDqTpcSrsJzp_QZov6Ivj_EnZFUccJc4Kk_qCdg5sF9UAxMfwf8jbW4_4i3IJBWDS0HEOhAjvj11KtBn_GtBpa3nNrxeZiewbDfP0UbxDNybCzRqCGOa2q1mJV6G9rJbyXimvRLCZM6ilcaTOHai3EkXr5LP_YMJvZ9eV34gl67T68FemmtdoMbENUi1lmHsFbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ1VRKWLp8bM0NzaiOQdK8tHSdf8KLLZKd6BiqYIEqB2Cahl-S-XyBEbnMz0W1MKxK0uEanSVB6fOmkZw5aCuq0xrckt-_6f96X-7C7bh-6y1klF1QDB_nOkGPKEUAP3rgee7P7jHJaS8FNJqlag_jpx6XSPDzh0jVzc3-zf3ABj3TzAEVAj8RJIK6H05z4tVzWK3GDIVz_GTTeDRnpbcHT7Iydb0MjgH2tasJ5C4RqTFLtIMx9H7ziULOthHLjFLb8xirXcVH1eoCSPJ0dfxByYYgsPYYZf3Qb_6cgJyZvAMINL3xcEMHtL7CuD3GcWoWpKJ6jjEHYXn7BJSYb_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMyl5au6LXBB_NWq9XjFcdG4AKybyQ7vxC2YfHz_f6VspElMORbxBrLIuK1XU9HIG2aEbOwrE61_b2G8ZDBfMn3Rlqt7K9ihVntfC7aep5JKV6EcR_N58WT4WkVeH47gAn3VX3BuXU0cy1elGjKGpCoZGY49gy6ByDpRpC0gV6lHPVVbKM112-cfz6lTOcA_IQNnRrg2L6pn_ECXDNxR6qM3d2FTO8WdsPI-gv7p0L_HG8ae2r0Wj5wYZKg2OlIxjg6We0UgQgNnc66oS1uftQ-H9mKrkc40bbPnNWPuC_U5E8QLERoGhXhYVaBH3PDYZgZ8RFOgpzim8HZU5eyhyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMbrLxwhhX2PMIcbmOILiHMawJAKK_wTUCIuZmIbMUG2N3bOz9DDQUtCwWJAHsRO194dKlLqqZWf0EZvYV7BkelqOzCcLu4SxTY8lZ-9NNHv984I60HdDFhmlhznSsHZNuMBxm5lVaHFBqvqBmKop5KTY_y5aSqRiMYqStQTub8R2HnXNcZ7CRcaINk_xrL8iu947g10JGkUaNXCk-fqH7-3IRWZH1mgAVnojcRVcpYJbP_ycOetBYGBT-hREl0qEnX249t3ptaGPxPnU3VEtxIjWCMjNJVshNjeiangGaNiheN0lAUc6tSrQNkJLG40BD4HqFkMUzzYyjBBL-1SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJNHQhACirZef3Q6w6f7NGgygO4A4ql2oB2BPAQM9eyeYIjJf4hrotWkLD7a7A31bAI6EXGHs9IpzYEop-4csNM9hj9SMXWwmeiESY8S1sTd-7YLbLSet-mEFkaCBLA4imvIhpxfn4kO2DfbNxW4U0UGNOxZuYg1oTIDirR7C2I7dpHBOAyRSGrQILypwea3x0KWsi-1FLaQeylXbk-BUVLmXDmUHcrPgphFtx_6VGFYA54KNwpK23skRpyFKsVrv2J2OOCtIQ9VUAgLvRObl2VoT8rAw-eHDF-me_VAA2DfLDi-cH40UTt9NG7DSYgzzAzIrj87ZnJaIPdeVoEyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6As_BADGTfWy9GskpIpIk2uC6xS3vLdArD_aHqzJMgGmO4pKgMziOSBVDBliJ7y2t642QrXaa5S3tQW74vsVHcWT8jn4KQScf3oez-r3sK4naDjHAJw0oLVxZ9FaOyw-ekum504KBi_BU9zbKiONcd4GKeRBdjmtUmeln53ICK1l6b39ibbfP8OFYL8d-O-7rlJsBfN_kvPcofyBnMKGGIWvthWOWvRQjX6d1mD8G3OQ0QRLo3pNeRrLyjUrRH-5_CFgnkWBEq8GaiWrh2S-Qxq7rJ4kfx46w79VnJ9n97Moe0QqQfO7rqbOFZp0btVhh7Na5OgQ3T_nzRA4dlbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqmo4iCqs5Ua0g0MWnlDCQyIcBuuoh72KcGllqpu8DJIylZ3VMRcPzlz-QrZCrHDDGnbUYboAd7xVdRIiefOI4ikWWqHfA9ZxLSWISbf01Nf_hcddLWv_ExNEMvFIUtSLpyDe_iM5LfJn2f26t5IPoJCTnLQ5E3ovtOZ27vWUdLM5OUD4GLKgxspsXs5i4OwhnYYlDFR7uW1KHABnHXrEDY5D3MqBMxVUY4bcbQDqfb73LnCSw1qtUP4NECsUHmlKG86HuIZY_ranyrHt6UrLls_KCnjo5PFBI0D4OO-KXLVUVgAZkrcy02obgYCQUAqv9TmDY331nGl-ZdIHsJFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY8zgSSPqjNN8iXLtYgwM7IST1bNf4O-NpSA9se85g21ltuocMHoozkckSGWMNuBpBENZUqThpPOpP78ksoH1fBi_e99lfeHoD2QwqBS3QPFDf0_JL8JKwXES4TMFGNJ2BKGx_7cfSgVnOPF6HYlD7et8Ys09O6xdApAsfjuoWbLmf_Pv-ZP2yVzSj0oalRhHX6-GrDlGhoSM42933NW7Ej96oCzYXx1S5Oi9MQK3A2C4I2MKKkcviwOx_kGKUa-jQI77rzADLW8tYFeJV3UmQrWmi8wEWS480325s3mGaFx8axPIQNc_SGYkA3e_XRCPlQCLPiIpVCB6qhge70Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR7YSIenrFkGSrMv9dh3CJA4RkPSSuF53Z6QiU4S1kuYe1RsojQAi0ayqb85wgd02ibAdFzEflwqony6MLeWkMnt84Of8soDzdPlBfL4DkB3rcyOjawFoVBK4tHi_zrNsyH5hM1UH0U5fszbOC7ze2taZEmOOqY7Fmlwhcn0BEfyjqSIogFXSR-OJTsAk4Zheyk1arEKEIttCLHuzO-lPgkNITmKDerHPJ4bwN_JlhryueVoi43LC5S6rQAo7rtNgIKVWrvreXNM7CE0PluCYMdvLdP95cCpeiERGd0WYowO2jh-P5IbAv4LWvlShp9nq5h9hv5FNJfNRG_G82Ygdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvj_gEKlrkapkYHxZIVJAxTCVaC51kw_eGhvP9n6dkstQBTgirzgiZEuQtXehQdEG3c12yZkLmaajWhtYFVbnQeHvNgMcPSFCubM37G3EBsKLwzOkEtO705QkqpZcSmall3Wmb9l3RWkY1pLbAe28jSbBcO7AwUFB3QE6xa2eUmSLB4cgxc2XcWa0yzzgMoQ4_CuiagC0pf0TMPm0A5O5RsGzxqXC9VB0CmL8xIfTY9FzEXqKKf-H8fRa1gXMiyiykD7QUQLzlbq8Lyey26ygBsowgKSilT0veHaMJ0qUzx-OwPFWi92TS4D-44yPUouGCIDodKz0d9kodf-neeAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxtparhkrHv6WfdpkXWpWNkDK1iDBkKiNdwRCmC8uCHj3a1eCjnt-TVAClUWYnTF4KUFJHOJ14oEVTJVhsfVH4QcN2crlvITO3MfGsWgBNussxFJ7q4gL2Umx2lFnZZZzulekM2Thwl4fVPPPWfxR28Rlb0sIkdCHYCYUBkJxu6ykmI3uvL7ai3-QWPr-Lg9G57zIHnhSM-cs6HDWZu1HAhzUNa-y6j7grUr54l9ZBi8Ar6sRqgP8K-7_9zXPbZKhwsTIos4IpacFuEIlXUTOp1_OdHUmWgPreKzC0J8gbQZlngyEQSSICHoEviKejL0IdWONmEU0s9xFY6lw2hm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOwST9ExDfINUiKo-J8FQ379GCFPt-xQ_XNYq7K4I8PYwbpRa4DKilH7jGvl4C5PP0BV8vzg_9_anr3V9Vt0GXBJk1WKqSOc503rMrZWz57sYDwfE01FmZ3TqX4rk9yN4PWdw1vMj8QATWUePraf8zJTNV7ARIhUWvMBkvujSOoGC5B4Tb_SNts9gqf08yMrSc-L9-SOcsAD7h1deWKWCq8eT5DGNG3BIWWQ4KssQ8mWimx0cAopyE-LtGxQd5FgpRLqAACuKJTNuwxh2zsKjgSGqvgWDvyVEZ5PsvmqlQ5Yjg8OUqWFzhVAj58gsc4d-vlwNg9eOigiarbbUt50xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1YoeFdu-3aCq9_oo9sffuSK7Dn1oxJb8m_fNvHbr8Gf-ukeZ5DOCKjAsq3AQnqPUWmQW1NO9EDWjZOKbmfs_v25865PQRWuimAYVfnP8PQu2dbg7B8kOi_WyXM0Am3SVg196Un81JZ2IPElT7oocDUcMKRseNGM66uBYUa4GvEc06faruWRcYwKQg2lAjLm9_tEH0POTGubqRzmYcJe2wOXmcHrUFkGC1dpOqbNNa69iocIPtRy0v0_51QAu1TLd7itNfgiOSHOYajN07iKPm_jdTHoh41OELHf6WxnTTpToX7FDi3Cmj6oA_oxTTkb6KhUGnfyCMn84WSb8AOPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YLo_zBVY3A3fogwUNtu-M-TMxl1o7DX4zlAERBXDu6owgKVqR0xO1kyBxKKRRWEo-hL2GT-lGixZC7Gph3_VmpSNI-yFH_g_kaaD8nb6s5k306hBFKQkdOxsRqNGDeZW1rpqgLjsfOfWyaPH3SeVQdCU9KgO_wKvEEkH8hkD5wEDLvbQ5QcqeBdIFTnI1L2-8aEfv9nUcoEkRewzH3u9GOJjOTHmK_AztkRZm63gNUo3YD-xFGP8XWxJBcmMbEi6RwIZfOhYYb5te19A0PASm1tPxBTVVSAmTD2vDr3GDR99BBynRoqEhOuGX7iRSErjYzG5-HFE9lL8ZnikmDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZFejrjph52lDEjSLJT8ot9fwi9LQPNvQnDYQJjj9cVn2WmQd6xLXMa4Akiyw5g3CBBxPDH1bZOYW87icS4roASzavlDFj-ruvyELRpGCuD7IBx68Wph9SE9bajbG58jusiFKQ3SaX0BuwQHJOWhFzFuzCRwJGuarolqfKd5rmyxrbf4dVPvmNU2yZuvrxXTk7HaqPTRoMQfAEwGIwQEPXnCNbeKcEXjcPSS9YSmLye8fvMQhbGZqw51MgzU0whOkcaM1BBt3h7CmVxdpsq8_6U8GPMF2u65AoUZk4_mJTjvBxww1ov3idhaJEj3zqju0BLaP1RLtZK2E-ef-gJBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byxwWtMZC02z25aczQcZb3Ki4vtfUbTk2ttdnB41djyGuhGd1_1d4D31p-gc84kiKlDGmtKiLI_NtxmBr8s0zQf0QXgEvJoxxwixpputmVPFa1Putqjxsl0nIgrRedzVk2XEMs3Edptrz9kaeqi6MB8kDuLH67tj4faCSCPzke_9UhEEuWZaHL65gXndGTAAPg254PMRDylQ789RUCsKZ6zxvmKWgpAXE5E4Z5818ZXPCAfdI6Dmdw-S81tU5oOgxftQqjVZdFMORsDkZ0qOlhH9F9DK8zgBi-7654VKdaORiGJl36W2aA68cZGY_wOqVgMzJs0MXhMDcYS7R2tv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALLY1tbuCYBp04e6stPV0LAcsN0kI_DJfPJGIAedxolPLwNK7Ny0jCdDcLSAgZFIeNpe0uGfs4jLiMp2Ooe7K2coi6XFacwxOOR34ZkTKRxSPZTZenWHx_sCYZu0QKyB3Sxu8Zf-dHAZIuB84nU4ZGC64q8L-qeyRU4Gs08YJpYyFi3EeuBWa3p0FxycL-38vypWKBNfCX-tihj32d8t8fdAjkPQyQCKuAiIhjDB89d6glohfi-M5yITgoJrZ8tm73b2uv5alNJkGUkywOn1J58Kt2D2L0XUezP4l2jHAhFeIvu4U9O2FLXFCC1Z0MutdO4mYmru9K7xzHldJYErjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8ppYwTRRAMtxMmfamyXqyiIE4FfgOjz6eoVllhu2TWOOr2TVGVODEDYITzFyVAlX1qLZAFy02JT3H6oO4SSk1Piiv39WEpNdD5rtITfFYKxfA3aLZbB2AWO60Kyd8aDCd1yDItWiYU54vyrcHT9VW-4mqEc5TDDQ2yG-qW_YussRI7zcKewZd9a28EC_H7-5VOhs8A6Ec06_iGqGHbdPCczT7PnENTl5uGnY7PcVte-DRfGPR9fQ0HQcygMjvMEeLpc9uorzVn9-bqBfTYkz4RKkc7CFMH9F1Bdgb61U76HovtDXWXQLhzG8F86RGVxVxJntUZ3H6H4RRRiBNMsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0nOaNqDNN4JX2JI3IjBskEJpntmWdObFruT2PghrNs1qe8-N3kZ64aUoM0rFjpaMfhJh2_rllAKu_uQqXqBClWKALEnlbICvZZ1CQpFpxSV7n3v6m14iovq1CbnuL4CrFU7nHEisqNPXp3WfThsDGFYfe1n8cLTsdKLecpIg13PdlNvizn-BXGdKA8Jm5XXY8Az1qhkFiiM3VoC5qTWovvyR0RRBgtYRa7W6pDD6mmz4x6p0fKs05oQPTKcv1IOeEazYbQnXl_nuPfPL3IZgTIteLnBLcHUgeUZi8H6XiuDRvhWWWtQbMD9EZ7HM0C_sh-yptP6l-9Ocq5QFvamfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwmHHtuePs7Exb4rK6N6rJIbLtIlVCo2SjOIBYrW3av7PJGxyl37Qasts45g5DXXNP593mBmwGAA4_LElNaiAXFRIE8d4Cfvc0w4V9uPGyxlM0dxoag6KHgyjXlDKymCPKT06GhPHVVIWS_br7HGHEVHYC-n6Ev9tA6E_hcfvWYkWZ0kYXrIddTnhtb1maIa9O5Izq5XeLm9aJux11CMo8uzg-LTx7Lnl6AHCUxlP4ayOZZQAVGgutP4R4ezIznAOxDX0u61i7oCCevUOVqvOI4A5in3dqMlpwi1luJq56qLxbdq50rcQNPx12r_ZLab5rx5dVvvjJIO-iTq1euGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyqK2QW3GZOMWepZyur-T7miSO-SBP5gtalOjPchdeUGx3a4oGBZyyb336xb9HMpizSzKuDJar1dUHSnIPmVvldZ_XJkTC_oCJAu6kpKuj7OpeGo6GCKe37SfIWeOBVNy0Bz04pFxspjT4WILP4uz3RRTlOpvM8IJrN6mcUSQ4vhUW3hLUMi-1KMwnbmDY3HDeaIOO5ir0lima_2kR_-9ukQ_5lunXSBcSKnTldozfQxpuhJzw5U7Wh_AiAL9U87ZTH463lO_BmYD1rhB1eSHKUae7J1x8bxggqddAoHGqTWSFAflvCweqfG4olfi9nPhj09fbYcwykBiTMLgiUjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYfBFcuOd1TNt-eabxPjT19qu_6_8vR-xvtbV6DA5MNE2fXcSHc-p4dQ2ujgECZXkSJ7n0MB3LObHR06YWLoHdWY9oxaxZTfpSegY9ZwW4HfMXhP5zV2mUURoJMGq9ilzY2xc6SqHBUvKjqRjXJnK275jyZ2xoR8PItIhkQ3lkwvqzhipP6fNVdR6XRKrm_1hauHzGhQYTljQLBjHKy4Roa3ApLhRnVFLa_-6FTzuHb9v0r3IxoTgPRWZ_RuHOYakPphxrSnBKRq6s4k84e36EcwAD562ZjgaSuMAAmUipU-MQ1vGUOOtIAP-54bBGrH3dScRKw4Dj1vHLzFEW0_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAL-EviBhT3yfMYnZUmpG23ynOvO5fsfg87Edf7UuLsB3wZsbdausaWf2DP_MUZ7YlxWF-QWPq6GtZkcavEVTdwBG1MDbMXCvnQCusl8uHiT0lJdqyuUCpCqEsYjtSvk3ezu0-o3wgiFCkY-NDoayP0JjOVwLExooOIh8CSwihv3t1ZSVQWXdC3IPoyzoSTqh1h4-mjQ-fZZibteiHfw4yyDusFFuLI51uo_LakyHjlvGkNh_uqOlxMYeJp9knRQ_odXudYHDLR6FwlVwvhzTkvNEFBO7hBesrsJ5lpK9aDAMTb-SBnK7Am_IlmWVOQjZgNRAE9sHfbOQGXHt5Pm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK38ufylAND_87trrJMu-KKZSNsuyinCOEcHvy8WvzF_J3h-rQftormb8Ks5aPlB-364p6Uk4ZFqZeoC6omQH9iIWfDCNOJdnFSYNiuybAR0VcAQOvIgg3DTmoMP-83FSGPGkssdkiDe-qq6ozl-Rj4xbHUpvCUPirfcLM1Q_RkjGRnOh11l6PT5oJGbwHNdw2oc_EqWoz-8bOWflLwckRCfIj3bNuGq0Px0XK5fY1H5dMjYc-Vjn-gDawcbuq4NFs0cOmpqXc7H4m6erS0aA_WkkhXydUX1HTEWR54ckaAvwJ8cqqlScmgvH-P_LfQbFAfEanrQyEsTVGGULAwOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROcLipiPyUol5WZDGOdUBZRBSBh4vY2rBLqEwhuJgeuLVKZYt52Yne9pkahX89GVXSI8mTBL0HrZ_7ivJ_9JFjGMx_4P-8j5ihqYHRtmB5wrVfwjQNP34T2fKnwSGmDOeeDRgMUh2glhlsri4gvn1fto850YWHsWkhQflrk54aw7DiF3B5eE3NF5En4YFfqQBlT0rYonufIbmMG9-Wx8vfvtwZfv9Wu5CxywnzFrvZLEOzjAmTaVgZXRRjNe5D545AcQPg3Zrh6ED9pdXWcWbKXXspC8YlNhWb-pZH4vhU-EDITUO-rvsiR857BEq4Qr5T2pz6yMfygS17rMWoGQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVVSPtsJLnkgoWw8NmJbc3Sod9CJEOffsq1h5tyrN6MvaY7SX_vzWGXmP7TM-8Cc-ioKNW7bAAYgmTteoqP06vAwtD8SV6pKjbL5gXqkiYlc3bvKHcQ38KWUHPsd5m-r7aUqNfjF08PgMFTfZkhvy3H7o2A1Uyq_V4j182eYfdjGkXDlQfsblRUBCJ-OFv0uY52Jjc5IkPk16ELmYQbzePnbk__GpkJLY5lvwRvoDwpudzPxTrG9qk30EbaXSMTtJP5OhVV0E0tJ4qqtKBpNRM1A445JAEHwmTXHgSp_KxQBJ1OZcgIGQze01fZTqPCRmMvoX_SYS7Yvo-bTFeV21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAr117nsr779kHBSJHB11S1TUpJue1gtAStDG9WmKFSr-4qWIKRJK13YooDTBAjxTbBhTX1DCRkf803el2JyNc_vyJzSDOl79RGZ52C9y7STHGQB1EAS8m5BOVfQUowjDPikT8kV1ABzVV6sfZZUCUo50uMmCpFoqjWZSVdeZdUfsLm7BxYXccVERd7ESg5Asg669FYDXd7uWjzlS-FYdtxE11348LezvcJ_N1kiGOJa144rkGCvpxsdZmtGSLBIBK3xqb5nIvYUqnKdQ49InbhpZowYOIXutuUKXcfONgVw33Ji2mL7uoIdf6s4jFDCq8PcLRxtjLIXRMlUilYNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPz1-bqAll3NMzP0e0ms7eJtlJhMCr8_xr2ZKMD_aD2DiKAB5QnB4H2fc_PVFBJmKTqcgJEtvL-UWJ4ap6WfoTQDEo_gkmRheKr9OnBtQc3Ax9lpqhs9vjpaoK4XT1Os1bZwicgD56j-jHg-SaBrhD67PYcrMGcOMhcPDczf4JKrRDua1DF4JIJiJd6H3epUS63cdX_SE7WqVJWUEdSaBHez1r5dLCFosnAHVuctfCw25I2hMNnrHGt9JNAq-et09ujP1U4MwyMmPH1r5V2wMBpmA3dMn2mxGkcRr0OtiqUNyZeoKNEy-Njd69ik46coRJOTxG6ZgTk383noSZnpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dywOCr82LkEytb_V7pB-uu6fM-Jy30soBME6uIRhuynogcGGUbv8Qe0-zlwxEa8SsJhxLLWcZyzGqLPLi8vKimaEXx2ns3FnU0Gha6l7HLG5YbVwmJHu9qxI7-5NTZ3Ap2urzsViS5V0phV86zXlN02H01RE0sR_2jzPhu9yba2dnYWWUzg_ZNOqG46gLiZVYEjseDijqJNpjquA6nE3qPOZBDp-QJwUxC3rIyaX9xIo_kxFZzF2DS4YusDMN0HW9_WbVR9t2TghgAdAKBpLCPpL0H85oB2RunQjUxSeQQWuLdXHuTck10U2oSP4nM-JSv-e4THC7I6XjQgm23kloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKXH8DRgUsozX0Q9LZJmUmFZICEInLx2OpdjuScDeuyMDyKdVg7gEyuV3s5f4BaiHKaKgWApAk8oIAMB-_XbicvIiA_vv8OUU_vR7AzbtGK-38KFerGr8h0a2x12yV3cAKPKsrHnqGll-2FbYCzynhhsbREabdHWD5r8aMKq4By7hnq3NqfElGSRroTtIxEmv2iF_oZgQiQuhiHXksPpIudI7IFYNSneG2AdJdtVUrEJ20qJdNZ2jaK1Q9lC8mXzJCobpcsdc7z3ojga7fyMZJpn7d0pTfnH5RvN3LQhrWb-UlN6OaQIqc0_l_l2Pxp2ucNcgMxycNwgux9O-amxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfBv-VNTV8qj_fvhzGYfHJj1mrfLYMWd74h2wKGW6gJSvF8ZpyjSUYqKCH1QXXPRLmO_x5mm0BOh6zrPdXWcdgc1HAZ7FttVH29jNGzpARzQg0TE-28bN3trnfn1Etd8WzRl_Kd3Hhw7EB-7FjsbZBRBKSLBY_D2zWeNHxLt1gbaoDLmH-pmnSrOWLaslU-gjgjY0uo5ThRj83USzXfEKjkAUJELYEQB4UNfMbvfciqQly0y7N6gAiF2rq9mbX4I54EBw7jbQrDopkAdgVdFOVAkFFV-o-iUu50-q3vNewPLSu4Y2sEDsLMKGIiO8vH7pJRkY9BKbNqw_ZUelob1PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPTY-RwqcxRn-d0bIEdwC8qhVsXjjret0dHroYDKNxm2tgLxkDL_sp_eSn_KMFCqO6lBOuCIuqNHzm9WqlJX8bhFtz2g_tNAV5Sfx9yl-9bLPvl1mCCgZqpZj0c1qHbgY95V9fXXfjAVHG94CEvy-tCAvtSjazDRBFqcX1HcYRpcMaar3aL8Z_R4ro3ecrL4cMwsZOV34t5BUQzIU8goREQNPWlWZ0cqWtUVQt0dFVhcick5KgNfDNh-j_UnQcwk2DZDGYWilRJy9viYhbXjaRaJ1aDlFM-TK_A9utnxmTyyFktd0rCN_oPBrdmvClazLvOeFe8XcH0EL93W7kNROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cttfl1jGTqGC3RKo86k60QYpD9iUM8y8EgNEKSAVAPjLQL1b0SRDMNp21vl_YuxErcg8hkyd5EelZoyaaacTVbqSHpRaWVKlRg1XX8Dai_snzMklFS95RpLRAY0JOsVuP4EuTq511lMG7n_QIcYBakLt934cs3_IwsYY_0zDqjcjZsztaAVwxbsaCe-VPTZyRqs-AKfJIsA-TAUbBCA3Fo39ZCNEwjnZpi_VI7e9ii-3ngk-3Gf0Bu-f3VwQXGL10jqEXQ3TWO4dkaCBziuBu0fNbfFbGIPEwMIqDSGE3Hl3GX2gwjcIpvdNKRX57cJ3c6u6SEArXghzTas_FmcMNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYY0JmrKRf6pa-jSNup2nLX-c9E_W7FyMLc1xuA4L6V9PZ53xqPedbaXL3NDiRfm4v7lfYOPsALzbxYzPcBEw6AZgA6DFMm5UsM3BraQQFOm38uez9Gc8e4KhSMeO6luXL6fpm24CufRlgd1kFtLqe82ElUmuv07WUF_x7Rlvb3RdfvfH4uikgszmO2M4OD3vw6Peg7g-XECU59UBxwx1PW06w6rE21g-OSPKf1LwmifuRerhZlsyYIHKd9EFdjZEkTaBG0k2QHNAbYx7-gIm05Do6UfcA6Gk09rR_OjBbqCtyivOefSmHq9SAGEG-B-Crk5VdlGtN6IezdfeY_0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qec6x-NFgANNkD8HINMSMR994w7AG7PotP7vTjab9kxFBXcFQHNKtVYJRPmlsyX9DK9fJA41yQ6a66iXZuqN7GKMQ6yNXlg8CM4mkW0ibZ8b6nc8na5aUkV8KkWEbDYbEA-IxsZNe_SEaKTR-qsTMWvWULbDXEwmq3YPNatFZTY9MfyzSVsDQKYswwCkLn9lFE1GvR6Xa_sWSAbL418qKP7-htW4bON4mJKwvnANNWE-klbuIxdmwWt6lallrhZDZ5XRSdAUKOgssSNrdcDOvWWEW14HlakCEm7vTGtBBzBV6WuHxyiJV3Vu0Pw2uGMbGNbTqnCZ5G_XrfE_bk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-TL0P0nKjfL5tEZUozmsLySpL6WQnOENCXb5SzZTlZZozjeRYRtFPVuldnWP0lr9fG6sG5aaIYz4dEwA-AivYNaH57hs8v2lnRY474AAy6NC-ztlBSlEZTpu2aHa0X97jYNkgoR-BTkl5GqGjTSsPZvk9Sq6kL_rAUnQSxP-yImGB5wLNlIEnfFrvnhkyfhTLShTRss5fRl7B308pgofiTDAPqvloWp-ic3vBHql27IcW0wc2eXvp3KqqJJBvqIMcJ1sNA2-XqrOkNWAiIV1PTqKA770qIUFz0j2FOiriUbNlhJbkHoBUb6zeAWXk9qS-BArcu6m0JxErITkMRaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXtMqDqKg1dxKt-l0TsnNxHRQUK3BHe60ea1i4Gwr7y6irpNMHnXaNXmPT9XP3rqBCJzMIWsEkwks_Z-nqBDRPkpYYeG711zl8tCU9Y-2PoF3_N3fpKeUuT777sLKMQVZI5naMoPzOtGFxstLNwq8z562R884jNp-j2Xj3PybEzqRVkWxKsC97wV9iYxc6Rdb-8bGkkTy1WLLfxkhyDd9u5KB5bKFCIiSZFnQ4y1YhgSUp3qtwwhpCNS_j4miM4tQnZ3zJzStPVz2mOKqZK78bls1niSMPX110m3iakUXlstC9um0ezQUOoMJCdOQP8113fGjkfXkP0b0RLY3sV-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLVYFlRkWk9fTPC61zLgUITJ-V7ezSyWJHJQ56m80z_LBkrGmES3WhsxieZjTMVT0a1ZQuG-SGa_798AGQMM9y6wubGWI4vdz7TESYWhbBr2Bzavw-SRE9El5tJcYqdEyXVVEJj71pNMKtbOwWQdvNyseuZBW5f_-kSkxlDlHlYCawPr-hpBELb0wpxOjfhVzeZxbfEq58mRv83YKFUDHgvX3nzEqOMlHEvMWeZj0gXILmEVbSIriOCtlUeoqfY1lvMgz62bp5L5GhGjK36lUx9IArZN6RFbPib2bDB3TFLEWbwGJCX9sENhotuY4mhfrSIKL5jb0ZpVPRfUL8BRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHivHy2EsYsKMtJvtsqsiZvrO4qPmtnqWhXK20lrm51JgiOSkpdQoxbhPzPwQ2a4QqJypW1_f1qfU9opE_jWL-tZeVssyIUIzvOg8ypdpPYOugEyJ-0YueXo5kkmPSzEa9GlgulvBRVE3azmHd9jBr_2LOGZE7xDAyOVu1YEeJn7ziGSzJwgSccfW3yMXRmvr-jG5mM4kvGyGVv4Je9QHSQXOr9hMfvZoCeV-XHZnNoqohb4eAUcN5lj1Ny-7zTbu8LGZY3eF7bTl8ag-VbmNS4PC9dYBSSAmyJ1iY0-XpQ2_rNZOlU7yr82nfCuVoNUZdvM6Y5-g_lj8nxK_rQE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvoLC6DrrhGAwWttmoWgsxAFMbvAPZ4rTUbDhCx1m9l3BlIPKEGt5Y-t2GBHbvgRZn_DXmz-dDQ-t80vOKBi0Uj47jMh3mg0cgiB-rNda04d5uXq2vo7RJamAKDwjMKYFXePtfs5YhWr6OIkBhPMGlS6psWXK9YbjSNs8tvFiib6eBUw1ZgRSaeaFX21vRoGksOT1ydw-R6X7VcAEvGobUdLXXLHZ_Qo-cMGe53JXxhsfMXEjj_UHPlgUAbgDlvjN9RON3UPCKZuyQZ1FPZfA_-2dzxRIT3OFEluGYtAgHLUb1anRcmAIG-mO-wYiNT0g2nYPkqKaaMOzVpw0Kwodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo7eFK64xSiWTBVs8ADH41T57FJYFNMFxCSGToIlzkV1aPNIq_a2KnYN8chLBlO1MMmhRcLTzjfgMwpgI4Tuvuz0UrJDDJdrfZ8Zy-QeLEA6ZqHoyqaJWY9wMdOmwl8TOJH4L_CIDs3qckDQfDOi8PENgcI41oYFWDA_cQ_e-FXQJxRmhGt7yhHQzhcFTycPIJomcawarSTKd31-ZGSDvndvzGgrEPITEvmPxcrm5lA0TvrK3pRy6oRL8Q9OZaXpBm_5f-6BALYc69V1zcZhKKLrfY1fFxA5VaATGj1BOITKxczDbGgpw-rZZ6KO_qP87WoDQMxAjc4Djo6e8Jpx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9TN0mC-lafUBJ3w4kjBO72JLLPotvS637t_8sGre0WPeRCxPjBKHR9LsT1yNkx_r3j8wMw-LbolUNyO8ekY8im5kj7BnTsYV4evVDm0fDKKfko3nSRNMgU-N9z4MkDmRPyZS7kypWxIvJ0eoqV3olsGpvQ8tVXZaP1F8uPY83w7H2llFEdRwrwc7bBShf6lLVAXlnNOh5TqmKnu_Ayjy9vbDBxaEr40VMzrqWyWLdy5PjwLoDHZriUkBz20zq8IKjXdQ93qt_Iwmx62ljrMg4JM9mna9fRYqjpPi1bsR9bZb2UUiIuKl0-rtG7FptWXeczpCUgKn5tZjsrYGL8FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=e8PQ_hROufwp1-vJB89Q8lgF_fNuGlOSe1MVM6gXl4ruyKVeat-QKQOEC2bu33vDg9X91T-osYdKtSDhRoLEczYERKCSJbx8ird2nrB_rCDOo5pMqvPAKt5wlLnllJ98waWs1YkI4n8B3GHD2ODhqvub5sCfHI9J01tFfAXdHNeFmcAxzXtV0wQl3tuOaKtSGA3EjNMKAvDW3mwJwKoDZHUIIk1fICxNf4RHyHjyIROKHHeCleE5XOGPWTit_HX3ztVg07-30l1S9pr9ijcYw4v64ROSHntSdLxYguCMQdtpYI3EFWKKMYe9tBfF7KVxvwXx_dg7MUkBBkzjZVTB6bxIGPGaT2iH6s6Jn7H7SQ8xcBHDYHYeuubholGVa71mtnqiAHNAOktWk0_SfvivzM88G_nzv-GewiQAMKMfRUFwmF03h5nTxYY9J8h9RTu0vebzZrChgoBVc9SpATPwv2PnU8yX_TTEnmJiQ_PGEF2fJjGDF8o6-lN1Xx_KoyvGScaq66QGQCKUwTuuSnvq2ODjOllrqG9pojLXW4kB9DbaCUsDzBEE7tcl4U_APIaAMmK9j4hDBOkwOE8byYyvSQ3VLa6pcxKvTJ2dz3288fTAVf3CWJzWTZSEItXBRu5jzAVHuyFLse_i3JaLcaMxpWfmuExQKNLlOwTNNhEOTmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=e8PQ_hROufwp1-vJB89Q8lgF_fNuGlOSe1MVM6gXl4ruyKVeat-QKQOEC2bu33vDg9X91T-osYdKtSDhRoLEczYERKCSJbx8ird2nrB_rCDOo5pMqvPAKt5wlLnllJ98waWs1YkI4n8B3GHD2ODhqvub5sCfHI9J01tFfAXdHNeFmcAxzXtV0wQl3tuOaKtSGA3EjNMKAvDW3mwJwKoDZHUIIk1fICxNf4RHyHjyIROKHHeCleE5XOGPWTit_HX3ztVg07-30l1S9pr9ijcYw4v64ROSHntSdLxYguCMQdtpYI3EFWKKMYe9tBfF7KVxvwXx_dg7MUkBBkzjZVTB6bxIGPGaT2iH6s6Jn7H7SQ8xcBHDYHYeuubholGVa71mtnqiAHNAOktWk0_SfvivzM88G_nzv-GewiQAMKMfRUFwmF03h5nTxYY9J8h9RTu0vebzZrChgoBVc9SpATPwv2PnU8yX_TTEnmJiQ_PGEF2fJjGDF8o6-lN1Xx_KoyvGScaq66QGQCKUwTuuSnvq2ODjOllrqG9pojLXW4kB9DbaCUsDzBEE7tcl4U_APIaAMmK9j4hDBOkwOE8byYyvSQ3VLa6pcxKvTJ2dz3288fTAVf3CWJzWTZSEItXBRu5jzAVHuyFLse_i3JaLcaMxpWfmuExQKNLlOwTNNhEOTmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmCdnFzCdO54jdCXmiBcpqt1o9BOS3KvFD2nKhEE4REwj30RolsuO7fuEox95G3cWLNrEzifwMW3nMwEyVJueN995iwRlRPyxkf4WUN1z4WlMY11kB7mRXnAQShyhDI3RIUd8XMcPFS2oiPF-f4J9-cmOFbnZgQurwj03Zu__X4v1CTkE4aWW9znOLKoQqPRqgfGnTq4i4q-yRjsiziE3ehYmDWPFHK3GmjxlnLPd2Alllcwe4S1hVAOeeYVGJDlc3rcFWXjkJIxqTF9wGpHaaehWmuHsnC1DNPr2Nn1cBdfAcHwQX6mzfG7uTA-KUXAXilHL4oLJn8GU7ui8esS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=sr77HcCXfxXJmDuKtCYJpQg994sMhOPXjtDXKNd-iJgzS7tekIZglSaLmBXl5F7ej0zjRwl6wX4fQMW2ss7CZcFrtkQkrOwjPpYZjNzXiCdTrOPMgTvcN8Amej_4dvKuzqEfmvtko_gNcH7VdQo28iQcmwRq3lQSsYHO8Y_SuzyW2Ki00SYEe461wUBNyRXFyfp8Znau8yZOVTQ3hMRqkhQN0Cfu-aSk_nJNTYIq8pr9U0Z1_cTokDC6_tg8tVpjLSN77iAq4s2x1yMlMmajk7djjg-5WE62ep7yAw5Nbq18SbDzjMrTtzYZMX-qE-CYImMKCmTsNGOHW3icp6iE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=sr77HcCXfxXJmDuKtCYJpQg994sMhOPXjtDXKNd-iJgzS7tekIZglSaLmBXl5F7ej0zjRwl6wX4fQMW2ss7CZcFrtkQkrOwjPpYZjNzXiCdTrOPMgTvcN8Amej_4dvKuzqEfmvtko_gNcH7VdQo28iQcmwRq3lQSsYHO8Y_SuzyW2Ki00SYEe461wUBNyRXFyfp8Znau8yZOVTQ3hMRqkhQN0Cfu-aSk_nJNTYIq8pr9U0Z1_cTokDC6_tg8tVpjLSN77iAq4s2x1yMlMmajk7djjg-5WE62ep7yAw5Nbq18SbDzjMrTtzYZMX-qE-CYImMKCmTsNGOHW3icp6iE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
