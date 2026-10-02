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
<img src="https://cdn4.telesco.pe/file/t-R1rgFxngI6clhi97qQqVAv4oMqzQk82QQEvWl6UYj2-x6DNu8s26iSGo9qanbydk-gOmin22RR8CJbr4Tiyk0lYh4V_iIudttnLieynZnf3fw1gH6no7s0zDRpfzt6h8iQ-Uim_qEz-JLbbJgJO5-cEvnnzOfQBMbPmNPlzvpSu--BVtAeDEF3Ul5xfjDMm-Kzv8avdA5YvyLYP_mFmORnAEd27TSJpBgBY2XrtXThJCal-XXu1UtZmy8QiWlDYirgIfTsiY8PF4AdX6p_VsBDntyQCbcesL83AL6fNVagKlkWLXPL8O9pNsbhUrw2MRxz5vPF5cUDt-53XzuASw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 05:52:28</div>
<hr>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزارت دادگستری آمریکا:
اشتون حامد الابودی، مهندس برق ۵۱ ساله و کارمند وزارت انرژی آمریکا، به اتهام تلاش برای ارائه حمایت مادی به
انصارالله یمن
( حوثی‌های تحت حمایت ایران ) بازداشت شد. او متهم است برای ارتقای ارتباطات این گروه، تهیه تجهیزات پهپادی و قطعات ساخت مواد منفجره اقدام کرده است. تحقیقات از دسامبر ۲۰۲۴ آغاز شد و در سپتامبر ۲۰۲۵، الابودی به مناطق تحت کنترل انصارالله در یمن سفر کرد. او همچنین با یک منبع محرمانه FBI که خود را عضو انصارالله معرفی کرده بود، درباره
ادغام سامانه‌های ارتباطی و راه‌اندازی یک مرکز ارتباطات سیار
همکاری و برای تهیه تجهیزات آن کمک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/withyashar/24732" target="_blank">📅 02:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/24731" target="_blank">📅 02:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">😥</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/24730" target="_blank">📅 02:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ درباره جنگ با ایران: شاید پیش از انتخابات پیروز شویم... آن‌ها موشک‌هایی دارند، اما ما می‌توانیم از پسِ آن برآییم. ما می‌توانیم از پسِ آن برآییم. آن‌ها موشک‌هایی دارند، اما تعداد بسیار کمی از آن‌ها باقی مانده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/24729" target="_blank">📅 02:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=L1zFjwPxcfFx8uT6Om9Aedf6521bXXskimj_4zgYNzdj5j941GMF3WB67DeuZqoKhElhNp16ALD36SCe7OIWMyixIBwmMIH8Ni3qkYdNgv_ZzloObTutLU4YZ-prBFGVzCmzfdozB7ls6yT9Q5G8LZjun31_L-EeklCvvluZb9but9qmM9FwI6EneIcnWSr-tZyYpKEsei7PAF1WWUNY_dkK50ZhV7q5QaELMiUutr8lt_NWO0FgQ4HI0WzlYz7jrI6v1xXe_Cz_qDrHpx8M2uhP-K7FLmjszFX7aNrR8aVTQskIi429UmDZT8ZlKWoAWzKeGnTfCDEt1ErNezjACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=L1zFjwPxcfFx8uT6Om9Aedf6521bXXskimj_4zgYNzdj5j941GMF3WB67DeuZqoKhElhNp16ALD36SCe7OIWMyixIBwmMIH8Ni3qkYdNgv_ZzloObTutLU4YZ-prBFGVzCmzfdozB7ls6yT9Q5G8LZjun31_L-EeklCvvluZb9but9qmM9FwI6EneIcnWSr-tZyYpKEsei7PAF1WWUNY_dkK50ZhV7q5QaELMiUutr8lt_NWO0FgQ4HI0WzlYz7jrI6v1xXe_Cz_qDrHpx8M2uhP-K7FLmjszFX7aNrR8aVTQskIi429UmDZT8ZlKWoAWzKeGnTfCDEt1ErNezjACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر
»
@WarRoom</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/24728" target="_blank">📅 02:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=VsTXEa2Iep8HgI7KLfiFjyMXAsdZXzb9qzUOAVp8CP61L6h1Pv5D3HO81BcQqaf3hmQJzoMJBNm__4lUXufXcwwCsBlRXBmgM-w5hir8cpQ58YbwgezJX1UNNIfMNVng6n7gnPSE0Hac0X7s6zPe6P0tofoccvbvUEdUfNsJKskQQZS9tX7I63OeoXhYA9C3JNZpEisJ5EwBj0iRrJXPaVB5TZt4zy5EbKika-ouacCIA7SYypeP44Btqj8-vL-TZ4Hi2uGve-WLCZsGi3rhWfwgd9Vn3ok2B_2SFvPRkmS3JtZhJ24NT0PhlnPae0WoPVzpOGnAjHUxV2eCSds20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=VsTXEa2Iep8HgI7KLfiFjyMXAsdZXzb9qzUOAVp8CP61L6h1Pv5D3HO81BcQqaf3hmQJzoMJBNm__4lUXufXcwwCsBlRXBmgM-w5hir8cpQ58YbwgezJX1UNNIfMNVng6n7gnPSE0Hac0X7s6zPe6P0tofoccvbvUEdUfNsJKskQQZS9tX7I63OeoXhYA9C3JNZpEisJ5EwBj0iRrJXPaVB5TZt4zy5EbKika-ouacCIA7SYypeP44Btqj8-vL-TZ4Hi2uGve-WLCZsGi3rhWfwgd9Vn3ok2B_2SFvPRkmS3JtZhJ24NT0PhlnPae0WoPVzpOGnAjHUxV2eCSds20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره اروپا:
«به آنچه برای
اروپا اتفاق افتاده
نگاه کنید. آنها دارند
زنده‌زنده خورده می‌شوند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/24727" target="_blank">📅 02:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=ugpfaQqCJj_4OkzGbjq74SwMnxxmcogpfoQaupJJnNM3z4vKCxJxv9aEsxU7sRXnKRKjcG4Ok0qTaOg3bTyhFnjLdRFo-gWXnIrgyQ8hLE422kKRoq2lStEJ27lwvGh1eztdZfR5_lk6FbPnj_TQrgN8biaM9nmR35BT9pf-4XmMxgBSGpYURbYoKcjTGtp3zpm0VSfM6y_n3pwEXEzKl8G-k3Mi-1ek9Mr2vQWAnr_z-NtVyhfekM6fkmnWthkFfYsT1D_beFwvAlBlYVo48F1lQnHG1CKg7rSL0zzO_iBvbDu5foJnFrvh2UmgnQKKBQc350fE1kenjDhPkT6ATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=ugpfaQqCJj_4OkzGbjq74SwMnxxmcogpfoQaupJJnNM3z4vKCxJxv9aEsxU7sRXnKRKjcG4Ok0qTaOg3bTyhFnjLdRFo-gWXnIrgyQ8hLE422kKRoq2lStEJ27lwvGh1eztdZfR5_lk6FbPnj_TQrgN8biaM9nmR35BT9pf-4XmMxgBSGpYURbYoKcjTGtp3zpm0VSfM6y_n3pwEXEzKl8G-k3Mi-1ek9Mr2vQWAnr_z-NtVyhfekM6fkmnWthkFfYsT1D_beFwvAlBlYVo48F1lQnHG1CKg7rSL0zzO_iBvbDu5foJnFrvh2UmgnQKKBQc350fE1kenjDhPkT6ATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«آنها یا
کاری کاملاً درست و عاقلانه انجام خواهند داد
، یا
برای مدت زیادی دوام نخواهند آورد
.
وقتی با آنها
توافقی انجام می‌دهید
، این احتمال بسیار زیاد است که
به آن پایبند نمانند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/withyashar/24726" target="_blank">📅 01:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24725">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=qY3D1nXAKc0LIecOQoodTW0GTojL2nVUGME5Vd1cbIPnKrUa_7eVrUCcsebBJ-crUweKN7kMWYXYvsdUlEkgoQfeje32qtP3vZYvKlZ0w7Mf8aFKLsBjhYHaHyeegdGos_T6zOEmBpU_Vf8c41SJ4j8CD3W2IJoRbLChlR2cgiKtwW5AYrWQQVlwl-l0D-UiiwXpIyOked_EXF38guGD1c0ifLVnDGOyu0IAeeMlCQxBlJyH3OiVCpKQO4LG9Ehni4q8XXpLfaoxFOKcRnH8UJ9fk0rl8qSK9imxkrKt3Lxad6awZuBmCo52LayNWAbvKwEneFTAV0g6udy7fJ0ZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=qY3D1nXAKc0LIecOQoodTW0GTojL2nVUGME5Vd1cbIPnKrUa_7eVrUCcsebBJ-crUweKN7kMWYXYvsdUlEkgoQfeje32qtP3vZYvKlZ0w7Mf8aFKLsBjhYHaHyeegdGos_T6zOEmBpU_Vf8c41SJ4j8CD3W2IJoRbLChlR2cgiKtwW5AYrWQQVlwl-l0D-UiiwXpIyOked_EXF38guGD1c0ifLVnDGOyu0IAeeMlCQxBlJyH3OiVCpKQO4LG9Ehni4q8XXpLfaoxFOKcRnH8UJ9fk0rl8qSK9imxkrKt3Lxad6awZuBmCo52LayNWAbvKwEneFTAV0g6udy7fJ0ZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
« کسی حاظر نیست آنجا رئیس جمهور شود ، رؤسای‌جمهور ایران
دیگر در کنار ما نیستند
، اما ما تلاش می‌کنیم با
فرد فعلی
با ملایمت برخورد کنیم.
(منظورش رهبر هست)
بالاخره در مقطعی باید
با یک نفر وارد مذاکره و تعامل شویم
، درست است؟»
@WarRoom</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/24725" target="_blank">📅 01:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=jnIqI68v-6O5RZ_W-mMSsV0JGJdCNuaYhp0oLUoXOZnOO4UVtGVL9-IHPxWpZ1C0P5IvknpLGpk3AoKm7X88gGWalLeduw22FCXEXTF-y-DJF0AXGM25lUNe-m5GSljOp8ajlfTDSHbE23kNIRdzrSKPLjD21pIP53s386wGjAGHrWjm9Y-IssVH9i9HTW2v-gRl7yEvKpRVXIkB59OsCX_zAXLE1c2tffsqsDToJbPipNDip6UQEVGCM23zoW8eGk2DX9hdZX-8xRhJPGbrbAw33b9e-Icr3fkPD2f2gyHsMbdv_WVhyOiKxDZ6LYM4LKg9_ZZ4zL1S5gTNk8Af04WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=jnIqI68v-6O5RZ_W-mMSsV0JGJdCNuaYhp0oLUoXOZnOO4UVtGVL9-IHPxWpZ1C0P5IvknpLGpk3AoKm7X88gGWalLeduw22FCXEXTF-y-DJF0AXGM25lUNe-m5GSljOp8ajlfTDSHbE23kNIRdzrSKPLjD21pIP53s386wGjAGHrWjm9Y-IssVH9i9HTW2v-gRl7yEvKpRVXIkB59OsCX_zAXLE1c2tffsqsDToJbPipNDip6UQEVGCM23zoW8eGk2DX9hdZX-8xRhJPGbrbAw33b9e-Icr3fkPD2f2gyHsMbdv_WVhyOiKxDZ6LYM4LKg9_ZZ4zL1S5gTNk8Af04WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ایران
آماده تسلیم شدن است
. ما همین حالا می‌توانیم
خیلی راحت پیروز شویم.
»
من یقین دارم درست بعد از انتخابات ، شاید هم قبلش
@WarRoom</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/withyashar/24724" target="_blank">📅 01:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ویولن بیژن در قم فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/24723" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=oeJgOD4y7fwGvyE-lHKsPIUlxt5cXoV5NgAkYS88Tk2_968bADAIyK4gqDXMf6UMf0QK-xw_Ka5SaUvutmi3yGFsi3QyakWWml3iwxhFK6bWTXjofCndNp3-VUrbQoEE0uOXewXRlU2i_bdwjUjhubNdtLwlq24bURSoTOWHgzvTnK56R4tyaxqyl5AJEH-CE_5TC94mhkF4tqwXk4cd7VAT4DUJTlAtUTbaJEbJCjFI4FSm7e54WD0obIPumTxStN9Syk-u230ORN4Z1uuRF5dsy28K3IN9t9j7DL-7jGFBZT8P6WrWcpMt-1LXcgmtROOD7Sisg-z6T2ViDoB-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=oeJgOD4y7fwGvyE-lHKsPIUlxt5cXoV5NgAkYS88Tk2_968bADAIyK4gqDXMf6UMf0QK-xw_Ka5SaUvutmi3yGFsi3QyakWWml3iwxhFK6bWTXjofCndNp3-VUrbQoEE0uOXewXRlU2i_bdwjUjhubNdtLwlq24bURSoTOWHgzvTnK56R4tyaxqyl5AJEH-CE_5TC94mhkF4tqwXk4cd7VAT4DUJTlAtUTbaJEbJCjFI4FSm7e54WD0obIPumTxStN9Syk-u230ORN4Z1uuRF5dsy28K3IN9t9j7DL-7jGFBZT8P6WrWcpMt-1LXcgmtROOD7Sisg-z6T2ViDoB-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله ایرانی سیتیزن بریتانیا را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در…</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/24722" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
قیمت نفت بیش از
۴ دلار در هر بشکه
افزایش یافت؛ پس از اعلام اعزام
سومین ناو هواپیمابر آمریکا
و تا
۱۰ هزار نیروی اضافی
به خاورمیانه، همزمان با توقف صادرات فرآورده‌های نفتی چین به خارج از هنگ‌کنگ و ماکائو، نگرانی‌ها درباره
کمبود جهانی سوخت
افزایش یافت.همزمان، محدودیت‌های صادرات گازوئیل از سوی
روسیه و چین
و تحولات مرتبط با ایران، فشار بیشتری بر بازار سوخت وارد کرده است.
قرارداد دسامبر نفت برنت با
۴.۳۷٪ افزایش
در
۱۰۲.۳۱ دلار
بسته شد. همچنین گزارش‌ها از
هدف قرار گرفتن سه نفتکش با پرچم لیبریا در تنگه هرمز
حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/24721" target="_blank">📅 23:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL5EdV2wd_kAxy0zr5rS1zzA_L2mUtDE6ZX88udhI9Ihmq32nHVeVvz0vSRkpg04WC6Ldhczss9nupft3IwgPCyDGsRhFy_w5wub978tcBlabypf87LB3C37V2byRnTuoqrWpbFZdQ13jb-ze1HN8asbKVDh1LuYiKgEfjstgtgeV_ZV9JiPcujZM34iU2zTM2XjybW-OuKCMfYhUeNnUocKdtcmulaNoXOthHoXufKWqybG_7X6N6RLp8t0xHiQlRqeaaoDoahcfLdeu3RZyrUWXYu8XM8569Q_XgKzm9YLJW7BUlRQgYILNiPFx4aDY_zgXW49jT4VMLsRqxuGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجرات دریایی بریتانیا
:
یک نفتکش هنگام عبور از
تنگه هرمز
با یک پرتابه ناشناس برخورد کرده و در پی آن دچار آتش‌سوزی شده است. این گزارش از سوی یک منبع ثالث دریافت شده و
خدمه سالم هستند
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/24720" target="_blank">📅 23:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24719">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فاکس‌نیوز: ژنرال بازنشسته جک کین، تحلیلگر ارشد راهبردی این شبکه،
آغاز عملیات نظامی جدید پیش از انتخابات میان‌دوره‌ای آمریکا(۱۲ آبان) وجود دارد.
کین گفت ترامپ در حال بررسی زمان‌بندی چنین اقدامی است و عملیات می‌تواند پیش از انتخابات یا پس از آن آغاز شود. او همچنین گفت
عملیات مخفی موساد علیه ایران در حال انجام است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24719" target="_blank">📅 23:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=fxmcHPIj9polNRKb-bJeiMAQGVRbssDnySi7ZZcl7XUXIhpJgJldgqIIsDbZAGhPAaslt5qF6cxSIlETAgCb1SraBHvQZBCk70J0GXcUEFFaBKXVuhNy7sUkjWM-LM3zxZRvzDUCWhhycRdu25vug5eg1HyEPYVyx_AALCKR9E3N9nosJFCL9g2_SOROZYb1obvp6dMWnDQNMnHlybqt2MaS2rW_xcvNaXsoOZ4FyU3vE7f63Fx0Mi8e9wN5SlqajdhVPz3ZCwpYmbm2nyRX-UH6KSAJQhbevKndrDen0aqckBlfYLN1cgbN7uEXFMW4ErF0L-_qd6n2CS5mpOix9Jk1fx-ENkdYI9-nx7UszgIk3sCliLcDOfs5431PtYXrDxa_AVqMXxs5_KcHtdUkueVjyHxTprsdfrZwzk_y3fjanLsEw5XoByZkEh79iz3ZN9D7zbz-xfuP6DjTaGRC3dPQQGpwmVoWeNMwlwnjtePEk65ih1xXEAawoKcrM48oPldvJNTeG9YNDI1hCYyQ_L7VORazVXVub-s8dl5Fyvdp8ALyi8WN940Y-jaSBD-bL3pGWCskK0iQVvyC0PP0GX8Z5WQ1WiqFQXDUBwsagnH4AifPrX_7fAFGoumxXZ3neK0RpknuqB27U_Cb6GdjRsY-qhzVu5C67m3UuPGl1pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=fxmcHPIj9polNRKb-bJeiMAQGVRbssDnySi7ZZcl7XUXIhpJgJldgqIIsDbZAGhPAaslt5qF6cxSIlETAgCb1SraBHvQZBCk70J0GXcUEFFaBKXVuhNy7sUkjWM-LM3zxZRvzDUCWhhycRdu25vug5eg1HyEPYVyx_AALCKR9E3N9nosJFCL9g2_SOROZYb1obvp6dMWnDQNMnHlybqt2MaS2rW_xcvNaXsoOZ4FyU3vE7f63Fx0Mi8e9wN5SlqajdhVPz3ZCwpYmbm2nyRX-UH6KSAJQhbevKndrDen0aqckBlfYLN1cgbN7uEXFMW4ErF0L-_qd6n2CS5mpOix9Jk1fx-ENkdYI9-nx7UszgIk3sCliLcDOfs5431PtYXrDxa_AVqMXxs5_KcHtdUkueVjyHxTprsdfrZwzk_y3fjanLsEw5XoByZkEh79iz3ZN9D7zbz-xfuP6DjTaGRC3dPQQGpwmVoWeNMwlwnjtePEk65ih1xXEAawoKcrM48oPldvJNTeG9YNDI1hCYyQ_L7VORazVXVub-s8dl5Fyvdp8ALyi8WN940Y-jaSBD-bL3pGWCskK0iQVvyC0PP0GX8Z5WQ1WiqFQXDUBwsagnH4AifPrX_7fAFGoumxXZ3neK0RpknuqB27U_Cb6GdjRsY-qhzVu5C67m3UuPGl1pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : ناو یو‌اس‌اس جورج واشنگتن (CVN 73) در حین حرکت در آب‌های منطقه‌ای خاورمیانه، عملیات پروازی انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/24718" target="_blank">📅 23:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه… @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24717" target="_blank">📅 22:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24716">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولادیمیر پوتین: پیشنهاد انتقال اورانیوم غنی‌شده ایران به روسیه ارائه شده و این پیشنهاد
همچنان کاملاً روی میز است
. اما سپس آمریکا موضع خود را سخت‌تر کرد و گفت انتقال اورانیوم تنها باید به آمریکا انجام شود. از آنجا بود که ایران نیز تصمیم گرفت موضع خود را سخت‌تر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24716" target="_blank">📅 22:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بلومبرگ:
عباس عراقچی، وزیر امور خارجه ایران،بطور غیر علنی پیشنهاد داده است که تهران در ازای
کاهش تحریم‌ها، دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به تمامی تأسیسات هسته‌ای آسیب‌دیده ایران را از سر بگیرد
. این پیشنهاد در چارچوب تلاش‌های دیپلماتیک برای دستیابی به توافق میان ایران و آمریکا مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24715" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24714" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24713" target="_blank">📅 22:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش زیاد از ایست بازرسی های پی در پی در شهر های ایران مخصوصا کرج
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24712" target="_blank">📅 21:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">(پدافند) بیژنه غرب ایران کرمانشاه فعال شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24711" target="_blank">📅 21:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24710" target="_blank">📅 21:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24709" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تحریم‌های جدید علیه ایران، بخش‌های خودروسازی و راه‌آهن و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف خشکاندن منابع مالی جمهوری اسلامی اعمال شده است. وزارت خزانه‌داری آمریکا امروز ایران‌خودرو و سایپا و همچنین…</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24708" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال‌استریت ژورنال:
دونالد ترامپ به دستیاران خود گفته است که انتظار دارد
پس از انتخابات میان‌دوره‌ای نوامبر، بمباران ایران از سر گرفته شود.
مقام‌های آمریکایی می‌گویند هنوز مشخص نیست حملات احتمالی در چه ابعادی انجام خواهد شد. در همین حال، آمریکا در حال تقویت نیروهای نظامی خود در منطقه است و یک گروه ناو هواپیمابر دیگر نیز در راه خاورمیانه است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24707" target="_blank">📅 21:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24706">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">BTC 85000$
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24706" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مقام اماراتی به کانال ۱۴ : ارزیابی‌ها درباره اینکه ایران این حمله را سازماندهی کرده، در حال تقویت است. کاپیتان هندیِ مجروح نیز برای درمان به امارات منتقل شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24705" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgcZy2Hv4CPQwn1ECgF1I_E0f_7V8yWnCXjo279OxYGhtOio0jVQTcIswwNm8d93itu6ohQdWOS3Oh2ADGZyr9WE8eMl0xhShVadBaNbLSEtdCSmSP6WXBX7pSKQn1wTKKI6UyR3KNY8YSQFBzg0uQx3bMMTQpHL2Gv2YoO5CZ2tzCj79KxPNfmJbp-C-ZHXvBceN1-rNzK5wbQxOSRbOKhzG43a-1CKNmPrJ-6XhpOF5QGQk4_tyUSEfbbQYw_Dz6y04zGSl2lDZFzdWtpEMCm5nvMjIeCByIX-fYWX7aLQj79ERGKads8BsM5aKLHqxlN_24z4mlp2YTh3xVHxlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث سوشال: من بارها اعلام کردم که از بین بردن
تهدید هسته‌ای ایران
۴ تا ۶ هفته زمان می‌برد، اما من این کار را در یک شب انجام دادم! بقیه این مدت فقط برای اطمینان از این است که وضعیت همین‌طور باقی بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24704" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تحریم‌های جدید علیه ایران،
بخش‌های خودروسازی و راه‌آهن
و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف
خشکاندن منابع مالی جمهوری اسلامی
اعمال شده است. وزارت خزانه‌داری آمریکا امروز
ایران‌خودرو و سایپا
و همچنین چندین شرکت خارجی مرتبط با تأمین قطعات، مواد اولیه و خدمات این صنایع را تحریم کرد. واشنگتن می‌گوید این اقدامات بخشی از کارزار
«عملیات طرد اقتصادی»
برای قطع منابع مالی حکومت ایران و افزایش فشار اقتصادی بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24703" target="_blank">📅 21:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال 14 اسرائیل: «این عملیات برای دستیابی به سه هدف طراحی شده بود: کشتن تعداد زیادی از اسرائیلی‌ها، آسیب رساندن به روابط ما با امارات، و آسیب رساندن به خود امارات.»(زیرنویس فارسی)
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24702" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=dsE5HEIrdcUMJYfvnEMNGXpnGS57ZVOyEwBj_kY1_XPFqEJLIo-chX1AwdjhXPPuQ3apEdhMNUQvSvilEawUezw74_TwS-DH8osJ1r2FMJA7MSzsZwtcJ0sq-MMByhagWoz4a-vc9xwQKRm-45oe_iwccefZe-RF8l68xDskZKDBuCy91LV3FY9Bv1ErpntZCj_wB7AWqJYjcFrzGHJlnkfDiys-GSP4GsmYZDvnCuTmmjuw3WUEI0-rXkUzJWPD4wZOMJClZs3ZxZZ2szcYwAACRaIEJDfybIyznzeNlHLxyO1sYTeF13gqPX3GirCbTrZMRTgI70SPG2KOgGtpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=dsE5HEIrdcUMJYfvnEMNGXpnGS57ZVOyEwBj_kY1_XPFqEJLIo-chX1AwdjhXPPuQ3apEdhMNUQvSvilEawUezw74_TwS-DH8osJ1r2FMJA7MSzsZwtcJ0sq-MMByhagWoz4a-vc9xwQKRm-45oe_iwccefZe-RF8l68xDskZKDBuCy91LV3FY9Bv1ErpntZCj_wB7AWqJYjcFrzGHJlnkfDiys-GSP4GsmYZDvnCuTmmjuw3WUEI0-rXkUzJWPD4wZOMJClZs3ZxZZ2szcYwAACRaIEJDfybIyznzeNlHLxyO1sYTeF13gqPX3GirCbTrZMRTgI70SPG2KOgGtpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوکی از شبکه فاکس: این خلبان فلای دوبی ممکن است توسط سپاه پاسداران منصوب شده باشد، یا به نوعی دیگر افراطی شده باشد و سپس سعی کرده باشد هواپیما را سرنگون کند؟
ترامپ: ممکن است، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/24701" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=h9BlJzgPDp1XH5JAimoqu2Ov7xLlek7Dhaw9HFZW29Uq-KovmXU9GD1bYqgs9DhncFqnXGr-xVVHOhBwdyuAfRypCPQ_pdkzzT4bodd8LdpvdJyTJmFkum4kYxANfzR5CRjlMsGnKzma1h13xgznWD8vH1UyTfBdJdIFvhKINGxq2BtLRB9cvCaRCryKmNnS0mtNzVgAAFrt7YqrB1W8mXGb9DGeYjLF1ofnOtWIWTAzbBKLWUsyGuLx0u7yBOD_GgHJli5ITVpda5kVgr_4p7-cr4dl0xoIWYnddnF1-BL7iDuXmAdsqw5ChVeYpFdnLEmxnAKxdmrh1t2doi-ZBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=h9BlJzgPDp1XH5JAimoqu2Ov7xLlek7Dhaw9HFZW29Uq-KovmXU9GD1bYqgs9DhncFqnXGr-xVVHOhBwdyuAfRypCPQ_pdkzzT4bodd8LdpvdJyTJmFkum4kYxANfzR5CRjlMsGnKzma1h13xgznWD8vH1UyTfBdJdIFvhKINGxq2BtLRB9cvCaRCryKmNnS0mtNzVgAAFrt7YqrB1W8mXGb9DGeYjLF1ofnOtWIWTAzbBKLWUsyGuLx0u7yBOD_GgHJli5ITVpda5kVgr_4p7-cr4dl0xoIWYnddnF1-BL7iDuXmAdsqw5ChVeYpFdnLEmxnAKxdmrh1t2doi-ZBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سوال که آیا ایران در حادثه مربوط به هواپیمای فلاي‌دبي دخیل است یا خیر، گفت: "به نظر من، با توجه به اطلاعاتی که دارم، بله، اما ما در حال حاضر در این زمینه کار می‌کنیم."
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/24700" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=YQ-aDhjQBqmtAHdnyo9aQ2oO4XH75p2bAmFwgTyPGKzJfLwqE6Dd-VPMpHL6QomqG_HDn6STvLbHLSYZYWs9fYOeorlJ1W_G68dfOGHkMYPFMjtAPWpjls5ROyxiqjL4wNeNqqjwG8ORw-36jzx6xT8yp418ayWYV-b4N4LPDRAVaOAflG4uGMMaVa9M6zhTVhtd8D1HsVSD4eNlfLgXknTzaCDAVUbgdIqqKYgH0WrEaYjcLhbUcJ8L2orI-RgeJEVqHic6hLBup6H-do4wIGS299wDHY5FO_KXSNYQajp-UKBCnDzQEU6fZJMJFHjAcl4adhMPxavqIPLgznZUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=YQ-aDhjQBqmtAHdnyo9aQ2oO4XH75p2bAmFwgTyPGKzJfLwqE6Dd-VPMpHL6QomqG_HDn6STvLbHLSYZYWs9fYOeorlJ1W_G68dfOGHkMYPFMjtAPWpjls5ROyxiqjL4wNeNqqjwG8ORw-36jzx6xT8yp418ayWYV-b4N4LPDRAVaOAflG4uGMMaVa9M6zhTVhtd8D1HsVSD4eNlfLgXknTzaCDAVUbgdIqqKYgH0WrEaYjcLhbUcJ8L2orI-RgeJEVqHic6hLBup6H-do4wIGS299wDHY5FO_KXSNYQajp-UKBCnDzQEU6fZJMJFHjAcl4adhMPxavqIPLgznZUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت در گردهمایی انتخاباتی جمهوری‌خواهان عازم اوکلاهوما شد. دونالد ترامپ، رئیس‌جمهور آمریکا، پنجشنبه ۹ مهر برای حضور در یک تجمع انتخاباتی جمهوری‌خواهان در شهر دورانِت، اوکلاهوما، به این ایالت سفر کرد. این مراسم در چارچوب انتخابات میان‌دوره‌ای کنگره آمریکا برگزار می‌شود و ترامپ در حمایت از نامزدهای جمهوری‌خواه سخنرانی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24699" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک…</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/24698" target="_blank">📅 20:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=XrBJADpthpI3aRU8zt6taNaNbmcydu-ASdLWEVwx7AGx2FsiUdyfe5BdMAY5d1z7zB-CQQ4xUlEb9IB9QjZWdI5VvUUfuD6bpSgR9YfnDMXq4MsJ9-zg8NEhOfNdfC-7VwEZAEM_poKMZYzZDK8ItFxD6Dq7mj74Ov_TuAPc66ddqMPD9tQgIeYeOLKWcPZYYaWeasoPVopVroiWu0CUxJq_KbW98W1O17dQPRnZ8Nb7M8DvsW_8Dcs2BDNiIJpfj-Hra21NwS4XYlKraX9eZzAbxy0JAsMfxovvtuclfcnhG7s0Ed82ve9eHfSiSwA8LI-cJinTOhSMQIajYh7P-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=XrBJADpthpI3aRU8zt6taNaNbmcydu-ASdLWEVwx7AGx2FsiUdyfe5BdMAY5d1z7zB-CQQ4xUlEb9IB9QjZWdI5VvUUfuD6bpSgR9YfnDMXq4MsJ9-zg8NEhOfNdfC-7VwEZAEM_poKMZYzZDK8ItFxD6Dq7mj74Ov_TuAPc66ddqMPD9tQgIeYeOLKWcPZYYaWeasoPVopVroiWu0CUxJq_KbW98W1O17dQPRnZ8Nb7M8DvsW_8Dcs2BDNiIJpfj-Hra21NwS4XYlKraX9eZzAbxy0JAsMfxovvtuclfcnhG7s0Ed82ve9eHfSiSwA8LI-cJinTOhSMQIajYh7P-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چه نظری دارید؟»
ترامپ: «هر اتفاقی برای ایران بیفتد، برای نیروهای نیابتی آن هم همان اتفاق می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/24697" target="_blank">📅 20:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=lmFLXk2kkWDBewZ0F3dF7pvr6a7tLImE2oQ6OgLGcRoHT_R9SKVQW18Te37ImgsIogBMioE3GbEp1x6PquI2Lb3e_Ba21SljQt-B2I50t4-TVQQqxmUFeNchVTYUEFNkqQH3vbCMlUtXy92au2qkxPUlL_8zC0R7cZCmEAAQoGHX095quOFNPp4Zp4jjOnCEcE1JNanp2cvBdwAqzWebllXaE-SD3foWmZy08KiKalsKl9lkLuJqmA_VTmErZNdhup69Eh5YgVoWDro9rYG0oPOjSmblnKdwlLpHvxAxGiA2eBt1poeV3YR9iehcnmc4AT0liBypwC8mI3LiaCAf6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=lmFLXk2kkWDBewZ0F3dF7pvr6a7tLImE2oQ6OgLGcRoHT_R9SKVQW18Te37ImgsIogBMioE3GbEp1x6PquI2Lb3e_Ba21SljQt-B2I50t4-TVQQqxmUFeNchVTYUEFNkqQH3vbCMlUtXy92au2qkxPUlL_8zC0R7cZCmEAAQoGHX095quOFNPp4Zp4jjOnCEcE1JNanp2cvBdwAqzWebllXaE-SD3foWmZy08KiKalsKl9lkLuJqmA_VTmErZNdhup69Eh5YgVoWDro9rYG0oPOjSmblnKdwlLpHvxAxGiA2eBt1poeV3YR9iehcnmc4AT0liBypwC8mI3LiaCAf6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: به جرئت می‌گویم که صددرصد مردم,  از جمله در سراسر جهان , با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/24696" target="_blank">📅 20:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک مرز اسرائیل بود، اما دو خلبان جایگزین تمرینی به‌جای فرود در مقصد ، مسیر را تغییر داده و بدون فرود حتی در اردن، هواپیما را به عربستان بردند. نتیجه این اقدام، نجات خلبان تروریست عمانی و جلوگیری از مشخص‌شدن اسناد این عملیات بود. یکی از دو خلبان بریتانیایی بوده و هویت خلبان دوم اعلام نشده؛ احتمالاً فرانسوی یا اسپانیایی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/24695" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=uA67SLe_3unyzAISP8yQ7FGnqCuDWv7EonK3NQHRZqewBKg1egctWZA6o8u8J5tB951CKEg7oT7F0-VehHVYDdj49Qx5-BWkXnPhq6pSNAR92IhZ7SPKAtojMlP8yzHMOd8Gm1PfnhkNCfYQo1bD22VhnG230hpIA0fhuNBVA0bGJiXaiXkBh3vH2votoGnOrXEqFeafEGDs7pCDy_izHcc4ZZqipZkoQLnCAx-Yh_KoSAwflbkiQhMHRpDkLDEGpEWQpP15l5N3Jcvhh86B4l-89Gy7chNnc7MBxX9bXBAo8SqM0k5BodBNe3IQHjxzps83pnt8SqnLbEUJ1BftiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=uA67SLe_3unyzAISP8yQ7FGnqCuDWv7EonK3NQHRZqewBKg1egctWZA6o8u8J5tB951CKEg7oT7F0-VehHVYDdj49Qx5-BWkXnPhq6pSNAR92IhZ7SPKAtojMlP8yzHMOd8Gm1PfnhkNCfYQo1bD22VhnG230hpIA0fhuNBVA0bGJiXaiXkBh3vH2votoGnOrXEqFeafEGDs7pCDy_izHcc4ZZqipZkoQLnCAx-Yh_KoSAwflbkiQhMHRpDkLDEGpEWQpP15l5N3Jcvhh86B4l-89Gy7chNnc7MBxX9bXBAo8SqM0k5BodBNe3IQHjxzps83pnt8SqnLbEUJ1BftiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: اگر ایران پشت حمله به هواپیما باشد، آیا شما علیه آن اقدام تلافی‌جویانه خواهید کرد؟ آیا ایالات متحده تلافی خواهد کرد؟
ترامپ: آنها ضربه سختی خواهند خورد، نگران نباش. فقط از آنها بپرس؟ آنها می‌دانند چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/24694" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=SYDlXu6gL-nB2mc1lOj7r0j7qisl8KiIdHG4n7RNQWtD5bKJ9_BBZpZAt3JC9ikPXBTw9c-MLHYHDHkFZAAY45Poc-HOkVwvGtTDz14LCWSl1Rimx9_vlOCaeusBRsUVBv1n5EfCLOiNzzyLBIiXIOXNZ0K3K0gpD6w9to_NlySNi09YyQ-CwJvBaEGSlqHDU49E_MX_fOBRDcFPKtMdmZ8oVEfMGXDx0g-2HK3O8oKlV5hOg7T9PqLcWBS4aej4R76GJ3a5JT_eXSdnIleXQnJ8kKXp6Gcs97jHDEiIuBcI1P175pLsgDmlh3MawtMXGSQfpX89CGy_bQKMqvcNDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=SYDlXu6gL-nB2mc1lOj7r0j7qisl8KiIdHG4n7RNQWtD5bKJ9_BBZpZAt3JC9ikPXBTw9c-MLHYHDHkFZAAY45Poc-HOkVwvGtTDz14LCWSl1Rimx9_vlOCaeusBRsUVBv1n5EfCLOiNzzyLBIiXIOXNZ0K3K0gpD6w9to_NlySNi09YyQ-CwJvBaEGSlqHDU49E_MX_fOBRDcFPKtMdmZ8oVEfMGXDx0g-2HK3O8oKlV5hOg7T9PqLcWBS4aej4R76GJ3a5JT_eXSdnIleXQnJ8kKXp6Gcs97jHDEiIuBcI1P175pLsgDmlh3MawtMXGSQfpX89CGy_bQKMqvcNDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت؛ آن‌ها نیز پذیرفته‌اند که چنین سلاحی نداشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/24693" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=MdokYMQrfGN04XG1giiDCzPpMjb6RAcu8rov7iByHSXFlAIY1jlhA3cdnOwd44IpONIfPXLc8XdkYcIRG1IQ3W-VBkVqRoCFhnUfETh2Y0JzBJji3idiElUrwWmDAOOFoKy0Gp9aViQ_1Xb1P2D0v_OvYpW7kV7m6jFWkeBeT3DgKK9ATp7fsozXo5wTdg9tfkeeAz75urVNE5IG79pDw65wj05bA8-YE-5Q7uTX3hnUsuKay_MgdTdzwuqrgGU1cLCYy3CDetgbrhRAxc2MISC5jSrPogwKm9OqSxmSSj8r_kjA2R_6OitNbcpGkcmBLDmMTvSa3Rm2XzlIOrbW6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=MdokYMQrfGN04XG1giiDCzPpMjb6RAcu8rov7iByHSXFlAIY1jlhA3cdnOwd44IpONIfPXLc8XdkYcIRG1IQ3W-VBkVqRoCFhnUfETh2Y0JzBJji3idiElUrwWmDAOOFoKy0Gp9aViQ_1Xb1P2D0v_OvYpW7kV7m6jFWkeBeT3DgKK9ATp7fsozXo5wTdg9tfkeeAz75urVNE5IG79pDw65wj05bA8-YE-5Q7uTX3hnUsuKay_MgdTdzwuqrgGU1cLCYy3CDetgbrhRAxc2MISC5jSrPogwKm9OqSxmSSj8r_kjA2R_6OitNbcpGkcmBLDmMTvSa3Rm2XzlIOrbW6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نرخ‌های بهره می‌توانند رشد را کند کنند. ما خواهان رشد هستیم؛ و رشد موجب تورم نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/24692" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1487770b48.mp4?token=dVZ6i-zjp-OEdsqwJhhDvrjEdsOa5_aRyMTtXGYexhbtfNFr3v3cidKdlOgorvBZ6tmeSdX0uBZt7T9NOLW_zhl1CP9PaCK1hYvpqPcSu6zIShCAt1R3UOuI4yDl-s3aatEgD2EWkADOSFPUHzS6ag62UX2V7dcPTQZk8OGqseOX8AScQu1T2a807tvLoY0IgHt87kZcNOIW_mUo-pfCRD1y7qPQU-zdvyEZ_2OatU3PcVb5VjjR4xy2DqaiwUrv1Xz7NwRUoavEnbgvXZyJuwo2_DGb6yrZeLxIKmsugKFhgDltnDqeMf1IJZupIj9v_5pAbw6O4Vyzno9zprxDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1487770b48.mp4?token=dVZ6i-zjp-OEdsqwJhhDvrjEdsOa5_aRyMTtXGYexhbtfNFr3v3cidKdlOgorvBZ6tmeSdX0uBZt7T9NOLW_zhl1CP9PaCK1hYvpqPcSu6zIShCAt1R3UOuI4yDl-s3aatEgD2EWkADOSFPUHzS6ag62UX2V7dcPTQZk8OGqseOX8AScQu1T2a807tvLoY0IgHt87kZcNOIW_mUo-pfCRD1y7qPQU-zdvyEZ_2OatU3PcVb5VjjR4xy2DqaiwUrv1Xz7NwRUoavEnbgvXZyJuwo2_DGb6yrZeLxIKmsugKFhgDltnDqeMf1IJZupIj9v_5pAbw6O4Vyzno9zprxDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/24691" target="_blank">📅 20:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله
ایرانی سیتیزن بریتانیا
را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در لندن بازرسی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24690" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/24689" target="_blank">📅 20:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/24688" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ برای سومین بار اعلام کرد ایران موافقت کرده است سلاح هسته‌ای نداشته باشد
؛ او پیش‌تر در ۳ ژوئن گفته بود «آنها قبلاً موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند» و در ۱۵ ژوئن نیز تأکید کرده بود ایران «کاملاً» با این موضوع موافقت کرده است. ترامپ امروز، اول اکتبر، بار دیگر در اظهارات خود درباره ایران تأکید کرد که تهران نباید به سلاح هسته‌ای دست پیدا کند.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/24687" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/24686" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=XbYXFalxZyTf3KDRhQFARcq0kERFHKE216nyGJA4u1v1x4Og2-xATeM69BqqzRXlHeDqHmnzsIOkKwaLbAx2x67zOb_YquE5qavTD8Ho_d-6fxDyX1s9FRgCclqcMLXB391MznvwnnGgC03app8oX5j-ZoFU2BaYTj3BzcWOsAS5xLdOoX7AH5Dy62_45MdLWniSSwRCku8hJ0npTX_fnPuWlwYZG_ffKKBanNcnEaaj-lGr5tNLWa7bsVD3pZ7_S2-XGNr3bymQfrWyJv-lABX-gCTd_Kz51mnQmfEBBr_xC_VOdUR5fQzrnAeLbOpTcKp_5mAydwYi18B-CRjSCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=XbYXFalxZyTf3KDRhQFARcq0kERFHKE216nyGJA4u1v1x4Og2-xATeM69BqqzRXlHeDqHmnzsIOkKwaLbAx2x67zOb_YquE5qavTD8Ho_d-6fxDyX1s9FRgCclqcMLXB391MznvwnnGgC03app8oX5j-ZoFU2BaYTj3BzcWOsAS5xLdOoX7AH5Dy62_45MdLWniSSwRCku8hJ0npTX_fnPuWlwYZG_ffKKBanNcnEaaj-lGr5tNLWa7bsVD3pZ7_S2-XGNr3bymQfrWyJv-lABX-gCTd_Kz51mnQmfEBBr_xC_VOdUR5fQzrnAeLbOpTcKp_5mAydwYi18B-CRjSCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین , رئیس‌جمهور روسیه
: اگر صحبتی از حمله مستقیم به فدراسیون روسیه، به کالینینگراد برسد، استفاده از تمام تسلیحات موجود در زرادخانه ما، اجتناب‌ناپذیر و فوری خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/24685" target="_blank">📅 19:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: گروه حوثی با استفاده از یک پهپاد، ایستگاه توزیع برق "طیبه" در شهر مدینه منوره را مورد هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24684" target="_blank">📅 19:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLnVgIk5urBRxsw-GgQqB32plQqWreSY8m3MLyGwFDvUmNUyI_Jl5X08AR4rUxIMuI52BaxR_CCBXiO7q9UGugvpN94SUPj_vdssRrYj-uWWT8OazCITN5a9x9TogwSIblmpbrqEvq0yexz4rlWdZDlpVG0Q4RgbEJPAAYRh9PgGtie71ITdnU0E3in_bX414fL5C1GjL0j1z8KQpbmZVrCvcm-Q7OS_qSIjxpjCd3coeaeDkvGxIVDzW8lMWdgjxqhv67SYqhX-lJVzOB-kuxy7CO8auTWlE5RFYzhZSmC-zTJpGnc_UecOMgwfJ0BQlvkIxakNRziNFlL-GeP2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک جنگنده‌ی A10 که از درگیری با ایران برگشته! نشان های پرتاب بمب‌های جیدم و sub به همراه کیل مارک«نشان نابودی» دو قایق تندرو سپاه را هم بر بدنه دارد!
@WarRoom
🔥</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/24683" target="_blank">📅 19:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEtptG67dOaJFM8VXXSyBPI7Wsw8BNjUDx8_YjKgaUh7xpzGeKyRVfBQV2e5Kg8FjZnixD_-NV23FtZICfcSNjIpMFMURMADUKORY9dfyeoDnjr-O2AoGDGIf1iIzXOWz6d_WntcY3XgNgiHuxZYDNvmmDimUwTxFdnVM8qlwYIQ2zl-s-wsE5u_67gdgJCqQzCrmhjjwtz-Z1V0jFcdlM7A_lq48oUcT0STFhrvKWzTNnGRzfRaq38oCZj8_Jg6dg-_jaXM1IO63lt1GRXnlzeUS8mH9iTa4kIvZ-LzE7LOZvXBKK5Nh73nxDXi_rKzvHNG8PzEfh3hS-8bcYKyi-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEtptG67dOaJFM8VXXSyBPI7Wsw8BNjUDx8_YjKgaUh7xpzGeKyRVfBQV2e5Kg8FjZnixD_-NV23FtZICfcSNjIpMFMURMADUKORY9dfyeoDnjr-O2AoGDGIf1iIzXOWz6d_WntcY3XgNgiHuxZYDNvmmDimUwTxFdnVM8qlwYIQ2zl-s-wsE5u_67gdgJCqQzCrmhjjwtz-Z1V0jFcdlM7A_lq48oUcT0STFhrvKWzTNnGRzfRaq38oCZj8_Jg6dg-_jaXM1IO63lt1GRXnlzeUS8mH9iTa4kIvZ-LzE7LOZvXBKK5Nh73nxDXi_rKzvHNG8PzEfh3hS-8bcYKyi-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده نشد و اشاره‌ای هم به انقلاب شیر و خورشید نشده
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/24682" target="_blank">📅 19:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مرد خردمند ، مارک لوین : مردم ایران را مسلح کنید!!!
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24681" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏آیا سنتکام در حال آخرین تمرینات آماده‌سازی برای هلی برد در داخل ایران
ه
..!!؟
‏تصاویری از فرود دو فروند هواپیمای ترابری C-17 گلوب‌مستر III نیروی هوایی آمریکا روی یک باند خاکی غیرمتعارف در محدوده تمرینی نِلیس
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/24680" target="_blank">📅 18:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الجزیره: ناو هواپیمابر روزولت به همراه گروه ضربت خود بعد از ترک اسکله سن دیگو همچنان به سمت خاورمیانه (غرب آسیا) در حرکت است
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24679" target="_blank">📅 18:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امشب مهلت ۴۵ روزه شورای عالی امنیت ملی برای برداشتن محاصره دریایی تموم میشه!
محسن رضایی اعلام کرده بود اگر در پایان این ۴۵ روز محاصره برداشته نشه، بصورت نظامی و با زور محاصره رو میشکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24678" target="_blank">📅 18:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=BRCVujn4IfQwsSHtE48y2xLCzA8U6QTkBWYT_AgmAfD0eg3zPlSEQwXac6f9lJF17vjfg8aqzE4WWTECZ0z8nbkraYCExBPArcjLX_vqzjTSXtl16bwnwbXqXZhee-UsLmLdnasllcRvOMpDrI3uMHH5CrKX86vSZplLZFe7f5YWCW2fjN-Vi-op8IwF6hyq-VLvfyV0sKIvWEOl5AcrLsS1YhSG7gPeZg_ZBc8uwReoPSeqddo5RcuAzCf3SPegBSpaq8xGA7HHL-dCloLom7slLT_E5295CvJqkbsFfnVq49QVrsj7Xi2kqhaMnzYt0XrCYA8O8oGA6TYujR7cxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=BRCVujn4IfQwsSHtE48y2xLCzA8U6QTkBWYT_AgmAfD0eg3zPlSEQwXac6f9lJF17vjfg8aqzE4WWTECZ0z8nbkraYCExBPArcjLX_vqzjTSXtl16bwnwbXqXZhee-UsLmLdnasllcRvOMpDrI3uMHH5CrKX86vSZplLZFe7f5YWCW2fjN-Vi-op8IwF6hyq-VLvfyV0sKIvWEOl5AcrLsS1YhSG7gPeZg_ZBc8uwReoPSeqddo5RcuAzCf3SPegBSpaq8xGA7HHL-dCloLom7slLT_E5295CvJqkbsFfnVq49QVrsj7Xi2kqhaMnzYt0XrCYA8O8oGA6TYujR7cxYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه فارسی وزارت امورخارجه اسرائیل با انتشار ویدیویی درباره ماجرای هواپیمای کیش‌ایر نوشت: حالا که بحث هواپیما داغه، بد نیست یادی کنیم از هواپیمای کیش‌ایر که ۳۱ سال پیش در مسیر تهران به کیش با ۱۷۴ سرنشین ربوده شد. وقتی سوخت هواپیما رو به اتمام بود و خطر سقوط وجود داشت، اسرائیل تنها کشوری بود که اجازه فرود به این هواپیما داد و جان سرنشینان رو نجات داد.جمهوری اسلامی هرگز نتونست پیوند میان دو ملت ایران و اسرائیل رو از بین ببره.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24677" target="_blank">📅 18:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز: آمریکا مصر را نقره داغ کرد
و به‌دلیل همکاری مصر در جنگ با ایران، شروط حقوق بشری (فراهم کردن شرایط نقض حقوق بشر) کمک نظامی به این کشور را کنار گذاشت. وزارت خارجه آمریکا تصمیم گرفته است شروط مربوط به رعایت حقوق بشر در مصر را برای تحویل تجهیزات نظامی به ارزش حدود ۳۰۰ میلیون دلار اعمال نکند. این تصمیم در پی نقشی اتخاذ شده که واشنگتن آن را «کمک‌کننده» توصیف کرده است؛ با این حال، جزئیات دقیق همکاری مصر مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/24676" target="_blank">📅 18:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی : سفیر بریتانیا در تهران به دلیل اتهاماتی که به ما در مورد حادثه در نزدیکی پایگاه ویرفورد وارد شده است، احضار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24674" target="_blank">📅 17:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرنگار تایم:
پس از حملات حوثی‌ها گزارش‌هایی منتشر شد که عربستان از اینکه آمریکا از این کشور دفاع نکرده ناراضی بوده است. رابطه شما با سعودی‌ها چگونه است؟
ترامپ:
خوب است. رابطه‌ام با آنها بسیار خوب است و رابطه خوبی با ولیعهد دارم( پاسخ نمیدهد)
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24673" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به تایم : خیلی‌ها می‌گویند جنگ با ایران بیش از حد طولانی شده، اما ما در جنگ‌های زیادی سال‌ها جنگیده‌ایم؛ در ویتنام سال‌ها حضور داشتیم، در افغانستان سال‌ها جنگیدیم و در کره هم سال‌ها آنجا بودیم. جنگ ایران حدود شش ماه است ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24672" target="_blank">📅 17:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ درباره ادامه دار بود حمله به ایران به مجله تایم :
من آنها را از بین بردم و می‌توانستم همان‌جا متوقف شوم، اما تصمیم گرفتم ادامه بدهم. وقتی سایت‌های هسته‌ای آنها را با بمب‌افکن‌های B-2 زدیم، آن تأسیسات زیر هزاران تن آوار قرار گرفتند. می‌توانستم همان‌جا متوقف شوم ، اما احساس کردم این کار درست نیست، چون آنها می‌توانستند به شکل دیگری دوباره فعالیت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24671" target="_blank">📅 16:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرنگار تایم :
شما در اسرائیل بسیار محبوب هستید. آیا اگر گادی آیزنکوت رهبرحزب یاشار در انتخابات اسرائیل پیروز شود، آمریکا می‌تواند با او بهتر از نتانیاهو کار کند؟
ترامپ:
نمی‌دانم. درباره او چیز بدی نشنیده‌ام. اما نباید نتانیاهو را دست‌کم گرفت. بارها او را کنار گذاشته‌شده تصور کرده‌اند، همان‌طور که بارها من را کنار گذاشته‌شده تصور کرده‌اند. من او را دست‌کم نمی‌گیرم
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24670" target="_blank">📅 16:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ درباره اسرائیل و ایران‌به مجله تایم :
هدف اصلی من کمک به دفاع از اسرائیل است. ایران نمی‌تواند قدرت هسته‌ای داشته باشد، چون آنها دیوانه هستند و نمی‌توان اجازه داد افراد دیوانه سلاح هسته‌ای داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/24669" target="_blank">📅 16:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رویترز:
چین صادرات سوخت به خارج از هنگ‌کنگ و ماکائو را برای ماه اکتبر متوقف کرده است؛ این تصمیم در شرایط اختلال عرضه ناشی از جنگ ایران و حملات به پالایشگاه‌های روسیه، می‌تواند فشار بیشتری بر بازار جهانی سوخت وارد کند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/24668" target="_blank">📅 16:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng64JLq9WIvh0WVNKSdy4xnSfqhF9-FpudpTQgDjnHSNYgILWohdYmVNqiT0rNhaDEEfROD0XhOczffuE5viOY_RqekT9lhWghteRbFL1yBHAFZggtZmZTNqRof-j4nfflDBkvz6pexHowxxlvVNbpi5fxhooiLbSYMY1-DF5OeEki4Wwq3KnHCmZ-Hk0iCqavknnGWeYV2s1P1wR8l023GCG04Wr_N3iD2VCJKKJHw9Km5as4kq5eH9vBvjNzbXiueKnq6sP3xjWzfpijnsibIvXeaDlci8a0jyCotSZRt9qctYci-vv76lKu95AsoIa2-3aMOy_xsE8asq-iASIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل: ارتش اسرائیل دو تروریست را که در حمله ۷ اکتبر به اسرائیل شرکت داشتند، از پای درآورد. یکی از آنها در حمله به کیبوتص بئری و ربودن ۶ نفر (شارون هرتسمن-آویگدوری، نوعام آویگدوری، عدی شوهم، نِوِه شوهم، یاهل شوهم و شوشان هاران) نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/24667" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ در مصاحبه‌ با مجله تایم:
هزینه‌های مربوط به جنگ ایران برای ما کمتر از درآمدی است که از نفت ونزوئلا در یک ماه به دست می‌آوریم
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/24666" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ به مجله تایم : ممکن است ایران نابود شود ، این یک احتمال است چون احتمالا دارد پس از انتخابات میان‌دوره‌ای، حملات به ایران را بیشتر کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24665" target="_blank">📅 16:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24664">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو: ما همچنان در حال بررسی دلایل حادثه هواپیمای شرکت "فلای دبی" هستیم و می‌دانیم که کمک خلبان،
تحت یک فرآیند آموزش ایدئولوژیک افراطی
قرار داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/24664" target="_blank">📅 16:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به مجله تایم: فکر نمی‌کنم ما هرگز با ایران به صلح دست پیدا کنیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24663" target="_blank">📅 16:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24662">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو: «ظرف چند روز آینده متوجه میشم که آیا کمک‌خلبان ارتباطی با ایران داشته است یا خیر.»
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24662" target="_blank">📅 15:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تتر ۲۵۸،۱۰۰
بیتکوین ۸۳،۹۹۰
نفت برنت : ۹۹،۸۰
@WarRoom</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/24661" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دونالد ترامپ با روزنامه تایم: خبرنگار: آیا در نظر دارید که قبل از پایان دوره ریاست‌جمهوری خود، اعضای دولت خود را مورد عفو قرار دهید
دونالد ترامپ: بله، قطعا این کار را خواهم کرد؛ جو بایدن که به خواب علاقه زیادی دارد، برای همه عفو صادر کرد؛ من بالاترین ضریب هوشی را دارم. من بالاترین را بین همگی دارم و بسیار خوب هستم
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24660" target="_blank">📅 15:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه…
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24659" target="_blank">📅 15:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ به مجله تایم : اگر من رئیس‌جمهور نبودم، امروز عربستان و اسرائیلی وجود نداشت
@WarRoom</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24658" target="_blank">📅 15:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=mF_UOH-9hBIqWul3wbiEgPNIAbWs89LUkO9099CQ-y-174ElBEtmrbKw1EaTx0ZtsA9VkHEQRCwaxkQKbkNoylk9mq-Rt_qapssXdub9zY7NUqMSC_SfGxhC7fTjjYnSLme8eCrY3hNrNYR7NW5_w9Tl5-olPbQLhx2enlKI3zg8MT2Txs7JFozWwlsJeD_V6fO787lpJjnJrpvQ3gTNVrQH36iZldgSm3RXCkfrDo3w6ZHgh9yOVj3OM9NPzU9ybBYu1S-OOwQ2l3ujxt9hP2hvj3cwrsRVp1cCQ_7pBjh6VslV3dpCFnvmAmrXzvicXxgx2ZYB73rjZ3h4j005Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db5c82ed3.mp4?token=mF_UOH-9hBIqWul3wbiEgPNIAbWs89LUkO9099CQ-y-174ElBEtmrbKw1EaTx0ZtsA9VkHEQRCwaxkQKbkNoylk9mq-Rt_qapssXdub9zY7NUqMSC_SfGxhC7fTjjYnSLme8eCrY3hNrNYR7NW5_w9Tl5-olPbQLhx2enlKI3zg8MT2Txs7JFozWwlsJeD_V6fO787lpJjnJrpvQ3gTNVrQH36iZldgSm3RXCkfrDo3w6ZHgh9yOVj3OM9NPzU9ybBYu1S-OOwQ2l3ujxt9hP2hvj3cwrsRVp1cCQ_7pBjh6VslV3dpCFnvmAmrXzvicXxgx2ZYB73rjZ3h4j005Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، درباره ایران: ببینید، ما فقط سر راه آنها هستیم. ما مانع آنها برای فتح سراسر خاورمیانه هستیم، اما هدف اصلی، شما، آمریکا، هستید. به همین دلیل است که آنها شعار می‌دهند آنها ما را
«شیطان کوچک»
می‌نامند و
شما را «شیطان بزرگ»
، و آنها به دنبال از بین بردن «شیطان بزرگ» هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/24657" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ درباره طولانی شدن جنگ با ایران: خودم خواستم جنگ را ادامه دهم
خبرنگار تایم از ترامپ پرسید: «ابتدا گفته بودید جنگ ایران حدود شش تا هشت هفته طول می‌کشد؛ اکنون وارد ماه هفتم شده‌ایم. چرا جنگ این‌قدر طولانی شده است؟»
ترامپ پاسخ داد: «فقط به این دلیل که می‌خواستم جلوتر بروم. آن‌ها را از میدان خارج کردم و همان زمان می‌توانستم جنگ را متوقف کنم، اما می‌خواستم ادامه دهم.»
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/24656" target="_blank">📅 15:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: ما سلاح‌های زیادی داریم و وضعیت ما عالی است. در حال حاضر، حجم زیادی از سلاح‌ها را ذخیره کرده‌ایم و آن‌ها را نگه داشته‌ایم و به متحدان خود توزیع خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/24655" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد. @WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/24654" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دونالد ترامپ در مصاحبه با مجله تایم: وضعیت ایران بسیار وخیم است و اقتصاد آن‌ها در حال فروپاشی است. آن‌ها می‌خواهند یک توافق انجام دهند، اما من می‌خواهم یک توافق واقعی داشته باشم.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/24652" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رئیس جمهور ایران: آمریکا باید از این خیال پوچ که می‌تواند ما را از طریق ترور و آدم‌کشی وادار به تسلیم کند، دست بردارد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/24651" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ درباره ایران : ایرانی‌ها پیشنهادی برای باز کردن تنگه هرمز ارائه کردند. من برخی از جنبه های آن را بررسی کردم، اما نه همه آن، اما به سادگی کافی نیست.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24650" target="_blank">📅 15:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24649">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است @WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24649" target="_blank">📅 15:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مجله تایم: ترامپ احتمال افزایش حملات هوایی به ایران پس از انتخابات میان‌دوره‌ای را مطرح کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24648" target="_blank">📅 14:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24647" target="_blank">📅 14:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزارت خارجه امارات: دادستان کل دستور تشکیل تیم ویژه‌ای از دادستانی عمومی را برای تحقیق درباره حادثه پرواز فلای دبی و نقش احتمالی ایران صادر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24646" target="_blank">📅 13:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24645">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQVptWL8OgvudM1ZYsLbDh8eA567xm3N9mOcFIDng3RKfzvBymA-SIc1hy4_DeDdmCM7Clj7TmRj8VQqunMa8j8rj0SIi85AjHak57aLfst_rBwr2NouAuRyH21m_LGZgR6PwlDWRjZd8ECaLIoY5pYwnUrBsXQdKT5RNPWvIaWm6SrZgRCEtjr8Nx1AgMDxOeIEaLXa4gzRiQvMpVlu3Na8SUVedOxtu5sRGizEXrPkJ3hkXPkKoxJoYi9Nkyb-is9wAllm2MZJW2Nrdvosf7xckwgvt9ISjaog6xRw7_PZD1QaLQ78K6BtK4qWL9kbooRNA_HECDhZ2z3Z2B3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: احتمالا ظرف دو هفته چیزی از اقتصاد ایران باقی نمی ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24645" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ویدئوی جدید شرکت اسرائیلی XTEND؛ نمایش سناریوی عملیات نیروهای آمریکایی با پهپادهای تهاجمی در ایران:
شرکت XTEND که در سال
۲۰۱۸ در تل‌آویو
تأسیس شده و دفتر مرکزی آن اکنون در
تامپای فلوریدا
قرار دارد، ویدئویی تبلیغاتی از عملیات زمینی نیروهای آمریکایی در کویر ایران منتشر کرده است که با پهپاد شکارچی حمله ایرانی ها را دفع و با مدل انتهاری به ایرانی ها حمله و آنها را نابود میکنند. این شرکت می‌گوید سامانه‌هایش در
عملیات واقعی هم علیه ایران
استفاده شده و سابقه همکاری با وزارت دفاع و ارتش اسرائیل را دارد؛ همچنین در سال ۲۰۲۵ قراردادی برای تأمین
هزاران پهپاد FPV
برای نیروهای زمینی اسرائیل را تکمیل کرده. اهمیت این ویدئو در این است که XTEND هفته پیش اعلام کرد وارد فاز سوم برنامه پهپادهای تهاجمی
نیروهای عملیات ویژه آمریکا (USSOCOM)
شده است؛ پروژه‌ای شامل
STRIKER، Scorpio 500 و Scorpio 1000
برای شناسایی، عملیات در محیط‌های شهری و بسته که حملات دقیق با پهپادهای قابل‌بازیابی و گروه‌های پهپادی را شامل میشود
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24644" target="_blank">📅 13:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=L_9maA7Yf0a5ig2xilOKIMmi90Nm_j2xR_EIE5OMNfr2stHh0MdskD9od1aIOFWmmIzk-Pel2r3ef47lg_fz_W6uAZC3gBP_LSKPKKECwqxUkkQJoAKW2pWeH4te-6k0bsbsDMDbBRolTjLm0HE7w1vrMEd5yikTo2UI8dIzVfetxfoqGHhS1JDVdQF_n9heRxFf3GcuV50G9vlOHAN2CwnQuw30ATArIGVYCSSTLFaqKTiXSzgJCcCzFr-UicastCbSR6v1dNSK2dAEMKKzxR8wCdwPpshuAOqpPAZu3WiDmDT_cAhc15uwVx4kBolsAlaCh6lr-CeHwL0VhNfo0ohUNWMPbdKFTvKsIjf5vcTE1GCxOYWOkQr-mMraHf_ddqO-i7KMoYfvmPAixOhFUrdKsjJlF-qMzmLx7w8lfPYOhOb1sMpg6dQpITVpVw3WjnZ5tVfXa3oNlEZlvVE1TWCibr_1wKZZ-HJGpoDCJ07HasXuJvGplqfxPRdOMwW7pKh9Dy5wJPPvyG-nKtRMEoxABjWsqFkNdwmDiOcy1NJSFga58GOmJLzMxbA-UH6lXRbETUgjs0RZgs-SlGiOE7maYwlr7wCny2H_gjEtA1LWYPsxucKjuJYZNbWLJuUy31FL8qdsgZ3cHwHLmVNTGKPl4VqsPWFRFffhfkKJ6NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb859cb846.mp4?token=L_9maA7Yf0a5ig2xilOKIMmi90Nm_j2xR_EIE5OMNfr2stHh0MdskD9od1aIOFWmmIzk-Pel2r3ef47lg_fz_W6uAZC3gBP_LSKPKKECwqxUkkQJoAKW2pWeH4te-6k0bsbsDMDbBRolTjLm0HE7w1vrMEd5yikTo2UI8dIzVfetxfoqGHhS1JDVdQF_n9heRxFf3GcuV50G9vlOHAN2CwnQuw30ATArIGVYCSSTLFaqKTiXSzgJCcCzFr-UicastCbSR6v1dNSK2dAEMKKzxR8wCdwPpshuAOqpPAZu3WiDmDT_cAhc15uwVx4kBolsAlaCh6lr-CeHwL0VhNfo0ohUNWMPbdKFTvKsIjf5vcTE1GCxOYWOkQr-mMraHf_ddqO-i7KMoYfvmPAixOhFUrdKsjJlF-qMzmLx7w8lfPYOhOb1sMpg6dQpITVpVw3WjnZ5tVfXa3oNlEZlvVE1TWCibr_1wKZZ-HJGpoDCJ07HasXuJvGplqfxPRdOMwW7pKh9Dy5wJPPvyG-nKtRMEoxABjWsqFkNdwmDiOcy1NJSFga58GOmJLzMxbA-UH6lXRbETUgjs0RZgs-SlGiOE7maYwlr7wCny2H_gjEtA1LWYPsxucKjuJYZNbWLJuUy31FL8qdsgZ3cHwHLmVNTGKPl4VqsPWFRFffhfkKJ6NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سکانس پایانی تایتانیک…
سکانس پایانی رژیم هم یه نوازنده ویلون نداشت که اومد…
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24643" target="_blank">📅 12:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52888268eb.mp4?token=V-XewfpY6Uk3mkYq7_sB_6uDio5Vkd_pKiOWbUGg9LlARgowpB-E5DvuRoLdXC-ryVJht-YED4VKufAZ_OYrjvxIfOiumOSAr3q7yXxSb0DBJQXJlbq9ksWLgcnGalxeZm4A0YY61-gxaaRMh56SBunJHoyAwOxIfGHJoLufWALGHUlrBry1FI41AZuSE-bG5lRaLjiLG1S5Rst5vGXWPmGmNmgpskVml46geJYBLFzao_JErbYzwTX6EQN2dOQKrbKFKRlVJtw-aajQiSCjBfm-5AzvhmrUKti5G_oSMf4Qck6OOhFrDcR5Rh3reMW3AmtWPD4cv6-fxHpjtoyDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیلی مک‌انانی
،
فاکس نیوز:
«واقعاً چقدر ساده‌لوحانه است که فکر کنیم شعار «مرگ بر آمریکا» معنای دیگری دارد؟ سپاه پاسداران می‌گوید این شعار هیچ خصومتی با مردم آمریکا ندارد، اما هم‌زمان از آمریکایی‌ها می‌خواهد علیه دولت ترامپ موضع بگیرند. انتخابات آمریکا پیامد دارد؛
ایران این را می‌داند، کارتل‌ها می‌دانند و چین هم می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24642" target="_blank">📅 12:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=kQ7SV2PeDCfbLwaba2xEBYXBqBajN7HjDKu0d4x19nuiSkn7vkgT-B5VEpLUx8g9NIr-rzxXnA8to5fU4uZlUCD_1emacG3rvL1JQn4hNpONB3ErPPVAYNC1yY-jMDMpPl1nfbVWCiFopy_p3py2JY_wWHlIgovuIZpym29rmSOOmTmdm-mt6p9hCcbze2GCC_I8hH4C8yKnE5_KJQCVEmq2lwk4P-uXpAqYcOZvjnieefLdVPex85RkLOuZtWf0-t3uThdDidNM1q7hrmjQLEzBQRkOD4S18NELGMu5YPzQkGO9TycOCBo-sjaNG8dUEmlmOUb2cYe2CAdmKuWJwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60c71917d.mp4?token=kQ7SV2PeDCfbLwaba2xEBYXBqBajN7HjDKu0d4x19nuiSkn7vkgT-B5VEpLUx8g9NIr-rzxXnA8to5fU4uZlUCD_1emacG3rvL1JQn4hNpONB3ErPPVAYNC1yY-jMDMpPl1nfbVWCiFopy_p3py2JY_wWHlIgovuIZpym29rmSOOmTmdm-mt6p9hCcbze2GCC_I8hH4C8yKnE5_KJQCVEmq2lwk4P-uXpAqYcOZvjnieefLdVPex85RkLOuZtWf0-t3uThdDidNM1q7hrmjQLEzBQRkOD4S18NELGMu5YPzQkGO9TycOCBo-sjaNG8dUEmlmOUb2cYe2CAdmKuWJwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏درگیری مسلحانه شدید در زاهدان ادامه دارد ؛ صدای تیراندازی و شلیک آرپی‌جی
‏از حدود ساعت ۶ صبح درگیری مسلحانه میان نیروهای نظامی و امنیتی جمهوری اسلامی و افراد مسلح بومی در منطقه منزل‌آب زاهدان آغاز شده و همچنان ادامه دارد. صدای تیراندازی سنگین و شلیک آرپی‌جی از منطقه شنیده می‌شود و تاکنون گزارشی از شمار کشته‌ها یا مجروحان منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24641" target="_blank">📅 11:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آسوشیتدپرس:
ایران تأیید کرد پاسخ رسمی آمریکا به پیشنهاد تهران برای پایان جنگ را دریافت کرده است؛ جزئیات پاسخ هنوز منتشر نشده و موضع ترامپ درباره این طرح همچنان منفی است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24640" target="_blank">📅 11:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد @WarRoom دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24639" target="_blank">📅 11:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در‌ انتظار‌ تایید : در همین لحظه خواهر عباس عراقچی، پری سادت عراقچی، (لواسانی)، رئیس انجمن دیپلماتیک بانوان وزارت خارجه، ریق رحمت را سر کشید و مرد
@WarRoom
دیروز شایعه مردن میرحسین موسوی هم پخش شد که تکذیب شد</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24638" target="_blank">📅 10:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24637">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آژانس ایمنی هوانوردی اتحادیه اروپا (EASA):
توصیه‌های محدودیت پروازی بر فراز
ایران، عراق، لبنان و آب‌های سرزمینی خلیج فارس و دریای عمان در محدوده بحرین، کویت، قطر، امارات و عمان
تا
۱۶ نوامبر
تمدید شد. EASA همچنین از امروز محدودیت جداگانه‌ای برای بخش‌هایی از حریم هوایی
عربستان سعودی
صادر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24637" target="_blank">📅 10:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec6681269.mp4?token=quJuWVwh-L1xwBmL10LCILWN8mFMpAG-knZc154T6suu5ETtcCyMmYnmAqzljqW8q3TOxuvacZNWvuD_f7k6dgMNzCm9Bejsuhr1DOwb5L5HPXMlWjUwAbAqkpdsD0Jo2lrRY3rcIXC5eZyyBNQ6Fu3B23xJFEJlrVt3RwtJ3A76vSuPnKslKYKb3OvHe1YPKGX8kSws1lG6UWyBwuFGQVEl0tW5k694OJVuqFKGE4LHsgABSrGIsM9NBriiMxvG8kZLxUUf4VhwFHFeCoVTSt2M4wHCtYkDC3PWck3tWUhAHdTxow3NyUot1CWfLzThbi-_b1wHd7n7eDS9XvZTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در
مورد
اسلامگرایان تندرو
:
ما در حال مبارزه با
بربرها
هستیم؛ این افراد
بربر
هستند.
(منظور او از «بربرها» افراد بی تمدن و وحشی است
)
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24636" target="_blank">📅 10:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85883a33b.mp4?token=i_zUH_pyi3q-d5YUSQhCFLMtI_KgGmt6Z_GG5cr2l7R5PWw11BolX_ZYT0O5G296wS9sqhoeh-nfOXkCkv7ArnEZPxLFzwo5llipffifToipiIwGtSehWGzr2EfEUXr5dL0lgUdYsn7SsO4f-npQhrgewin8xCD4lkjFtTcIiFAGij0SCd58FoWO1fzlnpwo_zid5nVmImFJio5T3uYPQNKmTI5R7hiFmN4E4CLHYtTIPfco0CZp_kxF6zhRB3097p85fdKnqZAM4SU72yYrX2GwxS3Nz7Kop8ZSXFhrcOFCxYhzoXtH-9nS4__KXELvoh3wHdow3ihLyAT0fSBJqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CNN
:
این یک
رژیم افراطی و بی‌پروا
است و نباید سلاح هسته‌ای داشته باشد؛ این موضوع کاملاً روشن است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24635" target="_blank">📅 09:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24634">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4854e3d13b.mp4?token=nsRz6sjftTLsoQTLYYVESQtXCll_6yjh2Qi6c_Bt5bYjEQSys7Sci1PH4I6jYA4O48ze8up4XnZR1-Fg3ZSLFOtRKLhf7bSDSlUGTGGUA-AD5ySoMtjG2niu9b3R7qSohnw2hM-96y8f_H2mWYxUyHuY-CL-BnGTK0DhCjj0Z9iW-0s1c0Xr1wV1Q4Wn18ksdRHlkKmVsHjjkA0sdLhKHdk9GzlwpDWyHxusSLFjsPcp3lWzi5pao7Ai77gtqi7ABw__shWQU_UBipjwAlxEEQUbY4f3MQB6mlnleJoKBfQmGwYWDHr-C_LcLb8MTD1Oqdf3OBnYydBrViWmpmeUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره بریتانیا
و
ایران:
ما اطلاعاتی در اختیار بریتانیایی‌ها قرار دادیم که نشان می‌داد قرار است یک
حمله با حمایت ایران
انجام شود، اما تقریباً روز بعد، آنها علیه ما تحریم وضع کردند. واقعاً عجیب است؛
عقب‌نشینی و فروپاشی در برابر ائتلاف اسلام‌گرایان و مارکسیست‌ها
برای آینده غرب بسیار خطرناک است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24634" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e94c9fbb.mp4?token=UrNHLnJH3v5jU9wAtCT7neA3eMH07s2iyF8YtaS-n2zFZsy2cr36PujgbfXBMDoVcfBBY5jPqKF5BPtXSzLEHI2wyt3neEPTBqsqwl93PkoA6hO4GRSbbcLEWQ3ki7XzWW3YJ5t_rEvL0Ft7f1UnackGlk0zSaNEusRIFvWCfFNUNxTzfk-m1b5fpKibtBUoEQc5ME76E9o3a9dRqLyxCgVvCvd5DinIklqyq8y-kgtpGP1jG9EcAAinL-cIhfeQD6dUQ0K8Aa7Ve8CfFWPHHpbV8n9Kvs50138QM9juTV8iyZcsbmi94Neee-yB4HxpW2ty_7bqbVPJk5NsOpNtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران
به CBS
:
آنها در تلاش‌اند
سلاح‌های هسته‌ای و ابزارهای لازم برای رساندن آن به هر شهر آمریکا
را توسعه دهند. این کار مدتی زمان خواهد برد، اما آنها در حال کار روی آن هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24633" target="_blank">📅 09:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919a200a36.mp4?token=cvxwDMUB1f82O2JzmeyA4s5PR8qSrZRNinOQPHM0_YQYR4LLDCuKdSw1VcgjhXXQU70N4XHmIxD61z-EBCx2wXCFQKfryiJciToG5Sl37b24uJjHLusdHbO9hZq6VxaR7ucOH7fLZO1qD3VnSvK0vI1OqGd5yOVugTAdnSTiboypscrQp2x5S1k62Bmmy3UPmoIpPQUf834IccQdsO154OIKvsZt1hrfqMvHRw4B0DwuBLkcuBUN8RbRcbO-5quKJmbZhHvMrMRMIUGg57WYWmu63BLThXXbgXy0Cr6AvhvDIkn7kgz4H8ScDEeC-ciJ48x3MiaQZadqyydpmCFY9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
بر کسی پوشیده نیست که ایران می‌خواهد اسرائیلی‌ها را در خارج از کشور هدف قرار دهد و در داخل اسرائیل نیز به دنبال حمله است؛ ما این را می‌دانیم. در واقع، ما نشانه‌هایی می‌بینیم که نه‌تنها ایران، بلکه نیروهای نیابتی آن، از جمله
حماس و حزب‌الله
، به دنبال انجام حملاتی پیش از انتخابات هستند و ما شواهد روشنی در این زمینه داریم. اما اینکه
حادثه فلای‌دبی نیز بخشی از این طرح بوده یا نه، هنوز نمی‌دانیم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24632" target="_blank">📅 09:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0159708785.mp4?token=GX1mR9OhK8bqiiXvyO7egNv0xyrad3PEciFX8yr8knWLXhoTCvQQK2YgGHi89Ful6_lppyusE4Bytsz1vU6g8tU-cGrCZIH_OSqRG_RM0Mz0z2jB-cM-sZGng5DKGQPS9oSpr_heb5WDB2kHMhCLAxMx5LVBkbPRwETlQ1B-TNnWqOGCF_X0-YWmszdwhaNKBHMxtyaPIq1y83MRBG6WpXYbkg78ctFULW3mMpMNqvQ9B6hfvihhrhaILhARXepzZr-kx-98roBTJzAtcqWvbVS6nOry_7ypr3ZuGNH_oiDxmisnE3vvWwjHO3ybN2y6VOietoichvHX7eLhXuER_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0159708785.mp4?token=GX1mR9OhK8bqiiXvyO7egNv0xyrad3PEciFX8yr8knWLXhoTCvQQK2YgGHi89Ful6_lppyusE4Bytsz1vU6g8tU-cGrCZIH_OSqRG_RM0Mz0z2jB-cM-sZGng5DKGQPS9oSpr_heb5WDB2kHMhCLAxMx5LVBkbPRwETlQ1B-TNnWqOGCF_X0-YWmszdwhaNKBHMxtyaPIq1y83MRBG6WpXYbkg78ctFULW3mMpMNqvQ9B6hfvihhrhaILhARXepzZr-kx-98roBTJzAtcqWvbVS6nOry_7ypr3ZuGNH_oiDxmisnE3vvWwjHO3ybN2y6VOietoichvHX7eLhXuER_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در گفت‌وگو با فاکس‌نیوز:
به ریشه این حمله‌کننده خواهیم رسید؛ اینکه آیا همدستانی داشته و آیا ایران پشت این ماجرا بوده است. فکر می‌کنم خیلی زود مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24631" target="_blank">📅 09:18 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
