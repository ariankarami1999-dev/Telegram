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
<img src="https://cdn4.telesco.pe/file/UfOLw8wz2SSj1zYvy0gstIFzHjBkCcvlDGj3L1masitDbd7J3ajmiFJ9hKQVKpy1XMA44f5zTcPf_9aCNIoAo7b-l2ueCFqDGs9ssh3Dn6DZJYO2p9ckuhHbZNwSs94PxgvA71v9oz7rI0ntw653Jr7eI0yw95oD4ikMBTnu1zt_YIIViPixudNxbaE3OB8kx2BwVGR3wNtWH-gHVKwYsHFX9JcnS_8Cpkpb0JVmQxBxL4TO-pLtWVqu1Xw42aIBR7ISmY01vvffA5JW_5AgB9X6OofU7B-YrRAB_1L85mlWAX6ZmKb3H8feLxm5OO3DEVMQ3EiU-9udfEqbqcru3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت دفاع روسیه : لجستیک دریایی اوکراین، در حال فروپاشیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/138663" target="_blank">📅 13:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=DpXhKs8GS5w1-HSZotN4tWXOIU1W-sQvj0VLvhI5AVz29JWzQ_hwBrxDO-U0IaxXyQBNn3xKfibigyghXAQSd5n8S2aqpdOmHMcaXppoIK0JkIQGlfFRwra0PAbkfcqy7NZrEN02Tdd4D9sm1Vxqhtcvz0N1PvLF5sLeO6frf4NxoDuPd06AKmDpwGeykAS3FAihymPrvxOXXaKoAMJbkXf8MjLjIMNQ9Wux4S4k3rEM2_wM-GciQ_6xcq23uL27JyR1_8gXQs3iZmgMhwHuezHefXyZUQfbQ0-QvSwR_m6TVisJ8qcHZqWVyEKhCzvg3yjtuhXtF7_vu2y7wwO4SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae07c4c25.mp4?token=DpXhKs8GS5w1-HSZotN4tWXOIU1W-sQvj0VLvhI5AVz29JWzQ_hwBrxDO-U0IaxXyQBNn3xKfibigyghXAQSd5n8S2aqpdOmHMcaXppoIK0JkIQGlfFRwra0PAbkfcqy7NZrEN02Tdd4D9sm1Vxqhtcvz0N1PvLF5sLeO6frf4NxoDuPd06AKmDpwGeykAS3FAihymPrvxOXXaKoAMJbkXf8MjLjIMNQ9Wux4S4k3rEM2_wM-GciQ_6xcq23uL27JyR1_8gXQs3iZmgMhwHuezHefXyZUQfbQ0-QvSwR_m6TVisJ8qcHZqWVyEKhCzvg3yjtuhXtF7_vu2y7wwO4SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی بزرگ در یکی از انبارها در مسیر اربیل - کرکوک
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138662" target="_blank">📅 13:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzrHBy_gKGajJRRnlsPTkzJlcReza7Cxb-Y5j58SU5dfbOw6Tr3KDIq0bFQ_YHNPsOS1Tkcwl50RJEtZUNjNpkpXP1EpiCKCSnK5_rLgsWxXc_1yqWH8ZfZgyYqX5XV_rlxQiJWLu1hsXed3oe9dDwprze3xc523mZ1pv5fRKIEJa5vMZvNAmjyyWqANqwhR-As2ym8wO-RDI82saRedTGHeHX5ohNp1jJiB6YNboMthByvPlAfqF8UxpiZ8-PDYXucU-j62Qy0uEDmWMKHMJ_PpOhNz_Awc68VkMoGgiKd0MhfILEdKYJ6w2bGxnVEJE0Y22nb_ELWaLGE8ErC6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله کارشناس صداوسیما به وزیر امورخارجه به دلیل جلوگیری او از حمله به اوکراین: هر ثانیه حضور عراقچی به عنوان وزیر، خسارت محض برای منافع کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138661" target="_blank">📅 13:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=HacV-QJSxmrEWxAm9YiK6KSc4E42soN8mRIA8uAt2dipg4MuaLFt4xskQnQauXHX1kW0k4945iITFhRp8MMlT_-oWbixSMaxdbDi50R7J8qqzrGU0i4sK7QQlorpw90cifrStXUFIjliIs52mSjHWTyMEVnnKG54_3xmIV2ZhTddpimL5Mnn0rXdxVGQr7lcSY6nMnzQKPg_PvQV3ZJcWwghDABL_y44B1gbiWONK0gUDa_JOYBlyTY-VW06ve_GZ6aABCEBwbeUI5WUGi1iyJvyMGsE9Hv_SKJSE_Seu6HT6FsCbaFDhHNPa5l3TN0Jup3pDmkY8COagUhOV-N3OnWwlB8cEH8pyiHt4g8533o2elAw57_uerb8rogqn-JFNi1ab88uRlVi3SNm9M1Aci7qVtELRa_WshLSXKodgcdUWr2KxmxehPRxIYZ6ll2AdrVhBL_ibSbjM9VaiD_yFGqCwZWAMnDxWNF_LqzWyvg5c7g1LYU9luD3NHZoG2euqV1tbW2sty3zddbOexR66tXLSjGU3uexINUxLaZPnw5BWky6DGMxAnxJZZLpS4xBUQrrwsZQBi3zaz0Eb-UeSnT3ez2xf0WdBv6emDajXhcXe6UrfiYHcXGWcQCn_BIslBFDlFZ731rSZE2DKLVLpPMUQr0Joyxf4m1nkF0OmE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a7dcb61f.mp4?token=HacV-QJSxmrEWxAm9YiK6KSc4E42soN8mRIA8uAt2dipg4MuaLFt4xskQnQauXHX1kW0k4945iITFhRp8MMlT_-oWbixSMaxdbDi50R7J8qqzrGU0i4sK7QQlorpw90cifrStXUFIjliIs52mSjHWTyMEVnnKG54_3xmIV2ZhTddpimL5Mnn0rXdxVGQr7lcSY6nMnzQKPg_PvQV3ZJcWwghDABL_y44B1gbiWONK0gUDa_JOYBlyTY-VW06ve_GZ6aABCEBwbeUI5WUGi1iyJvyMGsE9Hv_SKJSE_Seu6HT6FsCbaFDhHNPa5l3TN0Jup3pDmkY8COagUhOV-N3OnWwlB8cEH8pyiHt4g8533o2elAw57_uerb8rogqn-JFNi1ab88uRlVi3SNm9M1Aci7qVtELRa_WshLSXKodgcdUWr2KxmxehPRxIYZ6ll2AdrVhBL_ibSbjM9VaiD_yFGqCwZWAMnDxWNF_LqzWyvg5c7g1LYU9luD3NHZoG2euqV1tbW2sty3zddbOexR66tXLSjGU3uexINUxLaZPnw5BWky6DGMxAnxJZZLpS4xBUQrrwsZQBi3zaz0Eb-UeSnT3ez2xf0WdBv6emDajXhcXe6UrfiYHcXGWcQCn_BIslBFDlFZ731rSZE2DKLVLpPMUQr0Joyxf4m1nkF0OmE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جزئیات بازداشت عامل انتشار لایو ضرب‌وجرح دختر جوان
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138660" target="_blank">📅 13:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPCMEKRsYvC2tIryYyrU7zWgLxYrJ0s-CqMVJduCizgSyUqrZK28DIAv7c8W_wXG6BCDR8fvMCAqV-V9DjpRftcDKeVAjH2N1KwnCvkDE28UwzOjPZP0Ojf4_z9jb2y6O6zCh1jtmdvKYMyAN1UvBir6QJ-uWnJFIEeh1PWG1nSXVLap6BzjxRZ2zGqSAQMiwCwArjtW2OJgWjaM0BEzboUI82b4iQJSOVk_8QDNFlkpDlgLH9CtxyoY_Lg0Zmgtc-HbtECNW9v6qIF-6hjnUGxs5thMC9l26-kNiOdmj1jMElu7pTaJxIFyHS0xECa8ZYM_yQoNy5qtZcMMnrVuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عطوان تحلیلگر جهان عرب: حشدالشعبی وارد جنگ شود، پایگاه‌های آمریکا در منطقه دوام نخواهند آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138659" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از فرمانده ستاد فرماندهی مرکزی ایالات متحده نوشت: "ما طرحی برای یک کمپین هوایی قدرتمند علیه ایران آماده کرده‌ایم که می‌تواند تا دو هفته ادامه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138658" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
العربیه: تلاش‌های میانجی‌گری تاکنون به نتایج ملموسی در زمینه توقف تنش‌ها بین آمریکا و ایران منجر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138657" target="_blank">📅 12:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=nnFOJweGcvo8MHk-4p12bYjwOXYYgJtekwjn7b8CJWXGfcvNWnoROnV2UxpNu1nsK8r5NN_9zwbNZZGPoK5kBbBvdGy4isQsg4Y3T6jhg4qD1fRNdZntCq2Rd-jOC50vQRNJsCfsYG-UFHeE-ovU792fr4mwwhRS_dSfa-02PGcyV0a4zWufZOC-11UnVRqhtsnWsy0NprB9YkPxfE6slWFwAbZRbuEvRDaZQqodxbUz0cRaAX5k1Km2ntAxFSkt4Z3IDl92eq5GoAOO38zIRd__ur7wvqcib4QTi3vW4gxWOJUStu0IvIaZtctaela3jDzWWhAOivrH-KrLmwJDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfe0b1f3c.mp4?token=nnFOJweGcvo8MHk-4p12bYjwOXYYgJtekwjn7b8CJWXGfcvNWnoROnV2UxpNu1nsK8r5NN_9zwbNZZGPoK5kBbBvdGy4isQsg4Y3T6jhg4qD1fRNdZntCq2Rd-jOC50vQRNJsCfsYG-UFHeE-ovU792fr4mwwhRS_dSfa-02PGcyV0a4zWufZOC-11UnVRqhtsnWsy0NprB9YkPxfE6slWFwAbZRbuEvRDaZQqodxbUz0cRaAX5k1Km2ntAxFSkt4Z3IDl92eq5GoAOO38zIRd__ur7wvqcib4QTi3vW4gxWOJUStu0IvIaZtctaela3jDzWWhAOivrH-KrLmwJDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه دستگیری فردی که برای جاسوسی به
ایران
متهم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138656" target="_blank">📅 12:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نتانیاهو: ترامپ درباره ایران سه گزینه پیش‌رو دارد؛ توافق، ادامه محاصره دریایی یا تشدید جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138655" target="_blank">📅 12:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=qAI0LitIdHAcOfX-gzAAzXLLmt1d1YbaMkCpwY9ZG9ezdhIhin9gTujR18kRjKfbLeChWrTG4u-_Q_h2A0Rmp7KI0FEhl301JGRS7HyCccRVQ5W99XZMtfYVbGVTALxcclyN0z2IOOyN1D8yjb1vLuVjelbWtu4n0L55lKBZAZXnT4uvIoOE7AwJ1YO5Q20aAAdYDVljMsbp-w6NWBjgZkq2ifX-wOM_a3poo0Ts8JXnc8C4kptcrm3WcPPbl3J6_yxqIivhjYt76T2zuAD0DaEQSn4sLdXC118gJA70fWaKu7LYoifKhBjNwr51EVeJ7Frea8HlWWZNbAPyqbozUHTIyxnrfkFAsH0srQAc9DZSKzCArBPm5TgGCG_sy6uiE6iKZuUp_bUG2kVAAi9VCj6WjzUWeronAQjJUNtIApg_dPcSaR92h1rckxEqT-Gz5ZnsRyYgnghrwnq4cEbeTwdEmzzLINzH7VdLbk8sBdJA7zMUuQ6mTYnjWbSJ_ivgGM0NcT0lw8a5KHVDBImayLvpHDJQnOaXFrMD_RhTG4WvYRlmTSYWK8QPblBSSWw5nZ_14yivKlqLMvP0bgCHd0tld5uHv2VwI4B_ebCPVUmr5q4nY4ROXWy59Q9aa2rMSuOIAFJrBUIfrVvzP6ZeHv4pnUyupOKaVptohPyjdSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbbc8eae3d.mp4?token=qAI0LitIdHAcOfX-gzAAzXLLmt1d1YbaMkCpwY9ZG9ezdhIhin9gTujR18kRjKfbLeChWrTG4u-_Q_h2A0Rmp7KI0FEhl301JGRS7HyCccRVQ5W99XZMtfYVbGVTALxcclyN0z2IOOyN1D8yjb1vLuVjelbWtu4n0L55lKBZAZXnT4uvIoOE7AwJ1YO5Q20aAAdYDVljMsbp-w6NWBjgZkq2ifX-wOM_a3poo0Ts8JXnc8C4kptcrm3WcPPbl3J6_yxqIivhjYt76T2zuAD0DaEQSn4sLdXC118gJA70fWaKu7LYoifKhBjNwr51EVeJ7Frea8HlWWZNbAPyqbozUHTIyxnrfkFAsH0srQAc9DZSKzCArBPm5TgGCG_sy6uiE6iKZuUp_bUG2kVAAi9VCj6WjzUWeronAQjJUNtIApg_dPcSaR92h1rckxEqT-Gz5ZnsRyYgnghrwnq4cEbeTwdEmzzLINzH7VdLbk8sBdJA7zMUuQ6mTYnjWbSJ_ivgGM0NcT0lw8a5KHVDBImayLvpHDJQnOaXFrMD_RhTG4WvYRlmTSYWK8QPblBSSWw5nZ_14yivKlqLMvP0bgCHd0tld5uHv2VwI4B_ebCPVUmr5q4nY4ROXWy59Q9aa2rMSuOIAFJrBUIfrVvzP6ZeHv4pnUyupOKaVptohPyjdSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اضهارات نویدِ زیادخان:
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/138654" target="_blank">📅 12:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
دولت عراق در بیانیه‌ای اعلام کرد که هیچ مدرکی مبنی بر آغاز حملات به عربستان سعودی از خاک عراق پیدا نکرده است و از عربستان سعودی خواست تا مدارک خود را ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138653" target="_blank">📅 12:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/452945470e.mp4?token=vPxGf2jSJjlEWml75elYkr0DeONudef4LQuKycTNLej0GUnwbMs_2g58oCJMDkuLN58n_3UfIkp-2Vs_R-P3ViNsjAVabO1Ozpl9vMra7oJ7qm9YGV3G8ZI7IWXOr5fQlM7MEMr6tEXznTowNQMiODXqNErFQQNZ8C4x_LMXgCM_c7NGQ7nnunlTrq07bjyX1B5iK2G96tOwdfWAS_v7Sh1sgCD7QYuzCmp2tswnpLSNPI6x6zjSX88AoLCXnsb7yYBkSz3ZsHu-M5tS7YBaqoUA_XqbCUwbcr_x7Btcq2UD1DdhO-v24z45DVzM9PVaXA34WYlh-5E1xY4AlxsM8w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/452945470e.mp4?token=vPxGf2jSJjlEWml75elYkr0DeONudef4LQuKycTNLej0GUnwbMs_2g58oCJMDkuLN58n_3UfIkp-2Vs_R-P3ViNsjAVabO1Ozpl9vMra7oJ7qm9YGV3G8ZI7IWXOr5fQlM7MEMr6tEXznTowNQMiODXqNErFQQNZ8C4x_LMXgCM_c7NGQ7nnunlTrq07bjyX1B5iK2G96tOwdfWAS_v7Sh1sgCD7QYuzCmp2tswnpLSNPI6x6zjSX88AoLCXnsb7yYBkSz3ZsHu-M5tS7YBaqoUA_XqbCUwbcr_x7Btcq2UD1DdhO-v24z45DVzM9PVaXA34WYlh-5E1xY4AlxsM8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم تشییع نیروهای سپاه قدس و حشد الشعبی که در حملات سعودی آمریکایی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/138648" target="_blank">📅 12:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد مقادیری سلاح و تجهیزات رزمی را در منطقه «مجدل زون» در جنوب لبنان کشف و ضبط کرده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/138647" target="_blank">📅 12:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138646" target="_blank">📅 12:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=ZbTV1HWvKw15F7kNVnz-SqXLsCh2432ex_EA3oUUdDN7K1CizwmJRp-K99_BTCKObthanT3M6B_L8P3dzd5PS4je5pwL3GZvSItBa9LdGhK_EgPqlu-UfJn4G_cWo26Ijtonwm1JJkUVQ-umN7niluq1bppVxl3ZNnmug27_D7YVNEl3S1XpFnTJCd4hKJxetJHKJMTCvP3H8t2vHU7YvbfKjT811Zx5DL7k3ShYsb10DQlEd8lpih3D0lcMNfxWL5q0YQV9bbJbXnGJBPDbT5ub93WjALXxq6JC__x8NvuafyPlXhkTxSK3QZvnOSH2LhYAEs2Izm6EpF56Wqkgug5IrqmyamKZI4y7aPAbfJlUsxHwRKvflKysEuvrQhB7KZ6mM8wD7_kqYf1BjpOjL0_ZnSjbJVFhXFt5Ep7K1MWVxy34enSy53zu10cwuxyHh7dZvioEzouG7u8ncSgWDH-0KZhLRwjwSWpJmDzDQ2TF0TLFHxi0_aR7iH86nIbU3ZGpr0wH4EmKjqJZfQNHGr6KnNTV1aZkJUwWqJ0qJc29yn6ZEK5FjEhEY35j5uI8T3m7I_GCT-MqTk8MIaGlH2KPqRAIbCTQLO-oVMj6mVXEolCsaW7LzoVB82h7RXmGUEijBNmWYEPaG79HCk64MZ_J2WtWlmdXC1SW34blAFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59dcbe8179.mp4?token=ZbTV1HWvKw15F7kNVnz-SqXLsCh2432ex_EA3oUUdDN7K1CizwmJRp-K99_BTCKObthanT3M6B_L8P3dzd5PS4je5pwL3GZvSItBa9LdGhK_EgPqlu-UfJn4G_cWo26Ijtonwm1JJkUVQ-umN7niluq1bppVxl3ZNnmug27_D7YVNEl3S1XpFnTJCd4hKJxetJHKJMTCvP3H8t2vHU7YvbfKjT811Zx5DL7k3ShYsb10DQlEd8lpih3D0lcMNfxWL5q0YQV9bbJbXnGJBPDbT5ub93WjALXxq6JC__x8NvuafyPlXhkTxSK3QZvnOSH2LhYAEs2Izm6EpF56Wqkgug5IrqmyamKZI4y7aPAbfJlUsxHwRKvflKysEuvrQhB7KZ6mM8wD7_kqYf1BjpOjL0_ZnSjbJVFhXFt5Ep7K1MWVxy34enSy53zu10cwuxyHh7dZvioEzouG7u8ncSgWDH-0KZhLRwjwSWpJmDzDQ2TF0TLFHxi0_aR7iH86nIbU3ZGpr0wH4EmKjqJZfQNHGr6KnNTV1aZkJUwWqJ0qJc29yn6ZEK5FjEhEY35j5uI8T3m7I_GCT-MqTk8MIaGlH2KPqRAIbCTQLO-oVMj6mVXEolCsaW7LzoVB82h7RXmGUEijBNmWYEPaG79HCk64MZ_J2WtWlmdXC1SW34blAFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار ای‌بی‌سی: ونس اخیراً گفت اسرائیل در تلاش است تا پایان جنگ با ایران را تضعیف کند
🔴
نتانیاهو: امروز صبح گفتگوی بسیار خوبی با معاون رئیس‌جمهور داشتم و فکر می‌کنم که آن را حل و فصل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138645" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
حمله ایران به اردن را محکوم می‌کنیم.
🔴
در هر اقدامی که اردن در برابر حملات ایران اتخاذ کند، در کنار این کشور هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138644" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
دقایقی قبل زمین‌لرزه‌ای به بزرگی ۴.۵ ریشتر در عمق ۸ کیلومتری امیریه در استان سمنان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138643" target="_blank">📅 12:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در کمیجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138642" target="_blank">📅 12:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گوترش: جدی نگرانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138641" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ: اقتصاد عربستان سعودی به دلیل جنگ جاری که تأثیر منفی بر صادرات نفت داشته، به پایین‌ترین حد خود از سال ۲۰۲۰ رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138640" target="_blank">📅 11:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نتانیاهو: قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تنگه هزمز را به اهرم فشار تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138639" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: اخیراً عبور شهروندان اسرائیلی از مرز و ورود آن‌ها به داخل خاک سوریه به طرز چشم‌گیری افزایش یافته
🔴
فقط دیروز، ۳ شهرک‌نشین نزدیک به یک روز کامل در خاک سوریه ماندند
🔴
ارتش این هفته، دو نوجوان زیر سن قانونی را هنگام عبور به سمت سوریه دستگیر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138638" target="_blank">📅 11:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b3dbc650.mp4?token=J8UR2yw2h0NgeTUp3tBr7ueQBTWUj8uVf-UjiNfdQ7VCWUaNqKkOP5O1gb_QevmMjYXGnur6Jyu-vrBxzd3ZAecp4dTpI17kq9y3TYwH4bUYN9pd7P-b6S610QCknHBgC2GgrJv378LlVGHEawFWBZq0PWQe2ErbU_ZAy9gazRO0MsLWyUjQ9GRVVFicp28SXkvNLFuPbn9Qrt76Fc1YU2rzKHRTbuF2Itkw1aRATdn8smrCqKnzqJS8yIx4p_ZBgcN6SHY9sJcQUF2zg3-L-bxudpofp8TjF964A9I3Psuvjc2GO0kq8EIO2TPOS0CFX1q0pIu7wUw7akxnxVEKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b3dbc650.mp4?token=J8UR2yw2h0NgeTUp3tBr7ueQBTWUj8uVf-UjiNfdQ7VCWUaNqKkOP5O1gb_QevmMjYXGnur6Jyu-vrBxzd3ZAecp4dTpI17kq9y3TYwH4bUYN9pd7P-b6S610QCknHBgC2GgrJv378LlVGHEawFWBZq0PWQe2ErbU_ZAy9gazRO0MsLWyUjQ9GRVVFicp28SXkvNLFuPbn9Qrt76Fc1YU2rzKHRTbuF2Itkw1aRATdn8smrCqKnzqJS8yIx4p_ZBgcN6SHY9sJcQUF2zg3-L-bxudpofp8TjF964A9I3Psuvjc2GO0kq8EIO2TPOS0CFX1q0pIu7wUw7akxnxVEKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا از کویت با
HIMARS
اهدافی وو جنوب ایران رو هدف گرفت
🔴
سنتکام هم ادعای ایران درباره انهدام این سامانه‌ها رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138636" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LiEFzPYDjOcC0p9bIhC9LoccrXTFTQYN1irJF49AR8xbgph47Z0Fco2IHhwgBQX8kGsu6z5TiPUFaxdEFJg7QpGZDrmiwiV_igNlnA_hycz7Cxbw0XYszMXiTrrAPMeJm4x5KSC9hFhgeJOlB1DJY2ylbXLTBtL9BIQD1FOf_NuZqzFZqic_Q3LZjoWhfrlF8nqJd7JjG5qvijou9hQuPJmiWkR1hele4VDEqJKKaZrNgdrXV5qB2N-ITlNdWolWkHlzHyoGseGeEzuGDGKtDGZNL_MwUYke2J2mi__WZYmM5wu3fj0g-X497vCSErjUYjfAGYNJCQydDqrFoV9yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQjRUxKrOKR0J7_icuyc72ecPgdUOiYX7Gp9aX2GZ73pQ-ZmBTr06IpHxXk5EKKy1CaDMqq1zAccgypfKTE11kGM0Sd62RFkfonBWnonHPIJ_RbPtXNmbskpmLjkPyNp4hccwy6lJ0TCpWUje9M5Riuobvyyd8Ue00r8pxk3Wa83vWfNGPnlRg-ZYpyrMoVDyxIr4e0VhdUhvtY-UoX-wwxQ3SlKZd4qG5yU3xVrSZZ422gONlhhqjX4Y6RYvAKJcpJKEYiIu7vLMGpP7s2IWGJIUJcFoHnymbw9FfjoIrwIUixhM6ebjO8DyFOTcKlRGQjudTIGgkXyR1R6OpTGNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138634" target="_blank">📅 11:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
منبع ایرانی به NYT :حمله به کشتی تو مصر، پیامی بود که، ایران توان به‌هم‌زدن حمل‌ونقل جهانی و بازار انرژی رو داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138633" target="_blank">📅 11:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رویترز: با تشدید تسلط ایران بر تنگه هرمز، نفت خاورمیانه با نظم جدید و تیره‌ای روبروست
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138632" target="_blank">📅 11:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs7PHj4NXLyjyfW8PMCIsMbFi-u6RwBDhbGmS437dt-lKaXhT86s2y3yKYrSVuHGPJuCIHms0LABlYYKIzseUxby-9y8bCcPyUPOIBtZNe3vlfFAve1P__PH3jDIpXdPmq2hEkn_aBuEllxJHoMdXPksey7YOMWw_L8T2ypzxhGH4uCRCn39RfPinQQgbDujksJAroie4kuLlMYVSXp85EDZyC9Eaz44O4VJiu_gIvMB8WYvcYiBSKoI5Y9uwAm7AxQKLhnfQpRIIH2JGyP7WqwLSUKzhrL8zXbwl6WIoYe-rlk9IHe2mjDSGFE_2fhXxBsR6EWe4m1NiiMhsc-eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گودالی که در اثر اصابت موشک روسیه در اعماق خاک لهستان، حدود ۱۰۰ کیلومتری مرز اوکراین، ایجاد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138631" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رسانه‌های محلی در اهواز می‌گویند شدت انفجارها نسبت به چندهفته اخیر بسیار بیش‌تر بود و بسیاری شهروندان از بابت صداهای مهیب به خیابان‌ها آمده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138630" target="_blank">📅 11:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سپاه: همین امروز حمله شدیدی به مواضع آمریکا خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/138629" target="_blank">📅 11:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گفته وزارت دفاع کویت یک ساختمان چینی در شمال این کشور طی حملات ایران آسیب شدید دیده و یک کارگر نیز کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138628" target="_blank">📅 11:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وضعیت کشتی آمریکایی هدف قرار گرفته در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138627" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو: به متحدان دیگر شما که به اصطلاح هستند نگاه کنید، فاجعه‌بار است. وقتی ما با ایران می‌جنگیم، در واقع برای آن‌ها می‌جنگیم. ما با این رژیم که ترساندن را به کار می‌گیرد می‌جنگیم.
🔴
ما جنگ دنیای تمدنی را می‌جنگیم، اما اکثر کشورها بسیار ضعیف هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138626" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b55112a2.mp4?token=JYv6AGXmDR54gtGjSlb3NwhSyVn8u36w7YKsPpSHg-Y60eMlqp4kNUWRbVpdvaNT7oaEkQljCrf99-DPYLQp5IV-wQ4XUuVMpWp6HxWqvR5JoxeaMDh2-49fhcayKICEZCYdyXw9xH1H10gMAzNk7iHFbzdmxiG1T_JMRp5TwF8T6R2Vc5JNfevUZREGWk5i3kiWywaXXvnXrZ1en7k2BdNdujd7ykJwtm17ysUxsmRSZHRHUT3oiNDxEsYE1skVG5eP5ENPp5CZ0fkJsiZv4beBFnJIrtRcWB5HjGCvn0M08rb1Td22enc1dAadPDc9qpGGIA5Q8IYcCKtlD0M4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b55112a2.mp4?token=JYv6AGXmDR54gtGjSlb3NwhSyVn8u36w7YKsPpSHg-Y60eMlqp4kNUWRbVpdvaNT7oaEkQljCrf99-DPYLQp5IV-wQ4XUuVMpWp6HxWqvR5JoxeaMDh2-49fhcayKICEZCYdyXw9xH1H10gMAzNk7iHFbzdmxiG1T_JMRp5TwF8T6R2Vc5JNfevUZREGWk5i3kiWywaXXvnXrZ1en7k2BdNdujd7ykJwtm17ysUxsmRSZHRHUT3oiNDxEsYE1skVG5eP5ENPp5CZ0fkJsiZv4beBFnJIrtRcWB5HjGCvn0M08rb1Td22enc1dAadPDc9qpGGIA5Q8IYcCKtlD0M4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: من حمایت دوطرفه برای اسرائیل می‌خواهم زیرا فکر می‌کنم این اساس امنیت ملی ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138625" target="_blank">📅 11:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82cc0cd33c.mp4?token=lmQ5CtIUZ8isI5nsAJKW2PfXWi0ZgMZxANX6iqXpfTmZHajgHjsklw6NVQXvILAzzhtkMpxbzGUcp7-6TogwqAFaevDJD0bK-aEQ0Ko58VL3lfk7h7YLzdgMkerWVTvDLMgvg5OlrMPGDYLHxJPVNtaOYwhb8G3xbkW8ofx-S37gsItYopFi7WSVBTBbzxQKT1CjLV49nhi_h4X3dnKqglB4KUIic8KZmYrEy4hKvNJN3Bi8zFL-LDJASn0443AqZYWFaFmcozjGTxd5BhNqVf_OaoZNMnjHVYP0fOCNRPJ1FrZ8Wq_tGX9eb-gKWcIO8yNQSQHVe-_UZ1cTIQIRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82cc0cd33c.mp4?token=lmQ5CtIUZ8isI5nsAJKW2PfXWi0ZgMZxANX6iqXpfTmZHajgHjsklw6NVQXvILAzzhtkMpxbzGUcp7-6TogwqAFaevDJD0bK-aEQ0Ko58VL3lfk7h7YLzdgMkerWVTvDLMgvg5OlrMPGDYLHxJPVNtaOYwhb8G3xbkW8ofx-S37gsItYopFi7WSVBTBbzxQKT1CjLV49nhi_h4X3dnKqglB4KUIic8KZmYrEy4hKvNJN3Bi8zFL-LDJASn0443AqZYWFaFmcozjGTxd5BhNqVf_OaoZNMnjHVYP0fOCNRPJ1FrZ8Wq_tGX9eb-gKWcIO8yNQSQHVe-_UZ1cTIQIRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو ادعاهای متوهمانه خود را درباره ایران تکرار کرد
:
ترامپ اساساً سه گزینه دارد: اول، موفقیت در دستیابی به توافق؛ دوم، ادامه محاصره؛ سوم، اقدام نظامی.
🔴
هر چیزی که به پایان برنامه هسته‌ای ایران منجر شود، همان چیزی است که مامی‌خواهیم. این هدف مشترک ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138624" target="_blank">📅 11:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d39ced1a5.mp4?token=dgMfrT7ORaDf8jkiAiA5cwjwPvRSEnG4x6MrqvjtPOTCgQ0Ftz9zKIHPr8jcxK8zolC10yTj34n-LHRGl5s_2QCzcxefSzhOuIQfaR8DMZDFYH-E_ltgho3NIRYBb8r5-jfvaHYHi-1csXGDSrnyVbtmfXtkmfSN4y6NSOcnTzTGxX-kjj96FEoUrtFjWUZejSoDLipofy_CvJ7x3u--AukJtJhw46eNQx0nqvftPloAttI89PPosWIUqG0O3CSVOjObCI5O3xlSAcGjHFY7pAg2yyGuCIa_yKtGrod-YQgZiXMW-XYnEHTZKwS5FjZbDpfY8QNAhEPQ4Ba53gapMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d39ced1a5.mp4?token=dgMfrT7ORaDf8jkiAiA5cwjwPvRSEnG4x6MrqvjtPOTCgQ0Ftz9zKIHPr8jcxK8zolC10yTj34n-LHRGl5s_2QCzcxefSzhOuIQfaR8DMZDFYH-E_ltgho3NIRYBb8r5-jfvaHYHi-1csXGDSrnyVbtmfXtkmfSN4y6NSOcnTzTGxX-kjj96FEoUrtFjWUZejSoDLipofy_CvJ7x3u--AukJtJhw46eNQx0nqvftPloAttI89PPosWIUqG0O3CSVOjObCI5O3xlSAcGjHFY7pAg2yyGuCIa_yKtGrod-YQgZiXMW-XYnEHTZKwS5FjZbDpfY8QNAhEPQ4Ba53gapMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره غزه:حماس باید خلع سلاح شود و غزه باید غیرنظامی شود
🔴
این طرح ماست: خلع سلاح، غیرنظامی کردن غزه و ریشه کن کردن رادیکالیسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138623" target="_blank">📅 11:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / سپاه: متجاوز همین امروز تنبیه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138622" target="_blank">📅 11:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای احیای مذاکرات میان ایالات متحده و ایران به کار می‌گیرد. گفت‌وگو بین تهران و واشنگتن در مورد وضعیت تنگه هرمز و کاهش تنش ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138621" target="_blank">📅 10:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دقایقی قبل، زمین لرزه‌ای به بزرگی ۳.۴ ریشتر لالی در استان خوزستان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138620" target="_blank">📅 10:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47170f0680.mp4?token=tHWFvENXMhm5r28c2Xxtg5V6BRMIx6rBL2n0287CIyHKzdbtyZ0gRMCiUWpc9szzN7RjMyrmJEL-7e_djzJuVWRb5JMAm4o2lVTP4ug8AQx-J_LSsaAlFO_vrarjpc4yyqxvFW9YxEUiH4NExYA6TxgH40T_CLHxeIzRRMsh9FDaqqOrXJdvxYHuhQD86jk_s3FRhhQBwdD7t5YQUgnEs8EYbj8akx4NYmMT5XBws3M6in-1W7qvL8kryzFXyzGWJMBVGobDzKHwGRRWcqOP5zj0wsJkLdiae1yQ7eCUlYrfcMgwZafGj3SNXeOiv6JdoEyGO8WvAB-Dhun_FhML8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47170f0680.mp4?token=tHWFvENXMhm5r28c2Xxtg5V6BRMIx6rBL2n0287CIyHKzdbtyZ0gRMCiUWpc9szzN7RjMyrmJEL-7e_djzJuVWRb5JMAm4o2lVTP4ug8AQx-J_LSsaAlFO_vrarjpc4yyqxvFW9YxEUiH4NExYA6TxgH40T_CLHxeIzRRMsh9FDaqqOrXJdvxYHuhQD86jk_s3FRhhQBwdD7t5YQUgnEs8EYbj8akx4NYmMT5XBws3M6in-1W7qvL8kryzFXyzGWJMBVGobDzKHwGRRWcqOP5zj0wsJkLdiae1yQ7eCUlYrfcMgwZafGj3SNXeOiv6JdoEyGO8WvAB-Dhun_FhML8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حمله ارتش آمریکا به یک دهانه پرتاب در نزدیک بندرعباس
🔴
سنتکام اعلام کرده است که جمهوری اسلامی موشک های کروز ضدکشتی را از این حفره ها به سمت تنگه هرمز شلیک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138619" target="_blank">📅 10:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=eaH2STyflkGQAuws3vLRmI7Uvp4wJ0gKWq1PAEvM4zNKfHJ0N8saQQJm9NcJ_M4l086fvYlO9p43O_Q0VfVUPAlfcnhRU55bt-xGkmdUsz86JHxBY4CPvxqQPQ3GTs0EkqZhWfqszBIOMLxVR0EvCkZCPI34P3QrbonDrUrBMLGqvYUEab67qrAJVMHi3A2o7x9wFwCKMRS36QzLDSYbyO9qhFb2RGlq2tF02wei-4q2yuYoeQmXLjbCDa705TRs582In4k1g-e72ITqrakgVXngG3VA4TxEChmmRsy8gyayRYVLa87I9UcPVBpcW3CpB3bUPXF4wRTGGldyTZov8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d6fe82ac.mp4?token=eaH2STyflkGQAuws3vLRmI7Uvp4wJ0gKWq1PAEvM4zNKfHJ0N8saQQJm9NcJ_M4l086fvYlO9p43O_Q0VfVUPAlfcnhRU55bt-xGkmdUsz86JHxBY4CPvxqQPQ3GTs0EkqZhWfqszBIOMLxVR0EvCkZCPI34P3QrbonDrUrBMLGqvYUEab67qrAJVMHi3A2o7x9wFwCKMRS36QzLDSYbyO9qhFb2RGlq2tF02wei-4q2yuYoeQmXLjbCDa705TRs582In4k1g-e72ITqrakgVXngG3VA4TxEChmmRsy8gyayRYVLa87I9UcPVBpcW3CpB3bUPXF4wRTGGldyTZov8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در اهواز  پی حمله آمریکا به این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138618" target="_blank">📅 10:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwCWl9Qg9wBNzyHsR6-QwsCbTgl7p1BitqFymwuhE77PiAtOuY4eqHDjtitC-ZrVhXDOzYs3W3fnj56zXayGBceojUTT1C_q2bXZQwxqJnZ5U1BJSzpiF3lQxuD6F2y1GqIugAEQxbd6vbrkezXw1l12wy9YOzFuNXqI9bh_jP2OfJ8am2TZNy9g2OMiHQjik-GvbVSY9XS0U0E2cC1PomnHIKkJ3B08q9gp2q2eVzONGiSsgDY65Fa5z6CspQQbhpD7uuuRX7HoNeo70WwskSTj-xM7OlMxrLglA_p4VCHemYP_df_cPo1WOrk_zzeJtZywdkCqAbp6JX9aUEgZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: در صورت دستگیری من در کشورهای اروپایی، نیروهای ویژه اسرائیل برای نجاتم مداخله خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138617" target="_blank">📅 10:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aixey4sdpRrp4OyDV9ZJnQJbhnxWt25KRUPEaExu4pYwHuCXw1oAfK9DkygjxJH13Ah0Rkj3qRaja-dAXJF94SvQQGr3FkospaWhjzfyNouJ3nz241OIiKk4fOeDeP9Q7MPiUTh6uBBxk3lPieApymhx0Z3YlMoCC7vbo548kkCCgvAQXEDJcPeQ_soqARMztlnp8clfB0aY3rlu_amJVo9wGksdk1JTnnRr42F6thHYZZTn5KBLIu7hGM-h1PHeCMOj_RNO1NRyS9Ooa6v3Q2V6ZKT5JTlFO_1ET8Tc_qalQfgFGdAUnx78pAyopeg1tOvrpbqjaODFA-JF_2vxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138616" target="_blank">📅 10:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbbZro87JIwbCwiPNvpmzavbVwBnorxh1vR0TILqwMCclpe14_QEQIcGYqsibzpNoCWKuO_pHEcqRrxKy3ogniDsseG-gwYyaKKoXSwWBNe0C2BXrf5PcokFTktKqQHTub5K02rON3kvx5LjfeS6-2X_KlaHhAwU-5uC-WS8CEl4f35QyZ0GpzvCW_SNCy43CkOkJ3EzhqtBa--X1QPfGfLbmDHkHIik0upsfYIf2mHlZcNbYKqYreRfUtwBKIh294nqDEjiVFJlbFqNBl_hPUoI2OfpZID5zPijXH9ZARO6QBullTESPm9MWqLgL7k5NRde27NmgXdvP0d5vBlR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نایا: اعزام هواپیماهای نظامی آلمانی و فرانسوی به اردن برای کمک به نیروهای آمریکایی در رهگیری حملات ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138615" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
زلنسکی رئیس جمهور اوکراین اعلام کرد که در حمله موشکی گسترده روسیه به چندین استان اوکراین، هشت نفر کشته و ده‌ها نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138614" target="_blank">📅 10:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138613">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
👈
شهرهای مورد حمله قرار گرفته از ساعت ۳:۳۰ بامداد
‏
🔴
قشم
‏
🔴
اهواز
‏
🔴
بندرعباس
‏
🔴
آبادان
‏
🔴
اروندکنار
‏
🔴
شادگان
‏
🔴
فراشبند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138613" target="_blank">📅 10:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3gclmx5EnOcDtWpdcKBbEVGXMcYrD524tERtj3klnYte198pSAvg5dh6qOyFSQM6SYI84RNBd_Q_07q3dGznGlSkVLqeA_9wqGd9JJY5LUeR19YXmiU_PHUdr9wbYTSIRulDOnO3Wsh7VXHuLNPtwo71UypO9hLc4I_opmv3ObNHu-ipQYpcxsU5Y1Pb7j4lqxcQkSXWaXKait6QTzHPXnIe4TbPkCMuLu7ns2Q4pI8sJnBMsFWaXQHOuGeCJKu7fFnwLahnFTYmX_vuObLT0rO_NDzGHh_5_AXUe14Ku9LCBO0h9TIkrizqJYOqOC1zdyISL9hTW-sATrqrbaGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۲.۸۲ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138612" target="_blank">📅 10:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ای‌بی‌سی به نقل از نتانیاهو: من در دیدارم با ترامپ، سعی نکردم او را به ازسرگیری حملات علیه ایران ترغیب کنم
🔴
گزینه‌های گوناگونی را درباره ایران با ترامپ بررسی کردم، از جمله مذاکره با آن برای دستیابی به توافقی گسترده‌تر.
🔴
از جمله گزینه‌هایی که با ترامپ بررسی کردم، ادامه محاصره تنگه هرمز یا انجام اقدامات نظامی است.
🔴
من کسی را گمراه نکرده‌ام و هیچکس به ترامپ دیکته نمی‌کند که چه کاری انجام دهد.
🔴
قابل پیش‌بینی نبود که ایران تا چه حد می‌تواند تجارت از طریق تنگه هرمز را به اهرم فشار یا سلاحی تبدیل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138611" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138610">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منابع آگاه به وال استریت ژورنال : ژنرال براد کوپر، فرمانده سنتکام، یک طرح عملیاتی گسترده را برای ایران آماده کرده است که مدتی بین 10 تا 14 روز طول خواهد کشید و شامل حملات شدیدی است که هدف آن مختل کردن توانمندی‌های موشکی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138610" target="_blank">📅 09:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138609">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اولین محموله LNG قطر پس از ۳ هفته  از تنگه هرمز عبور کرد.
🔴
سه هفته پیش تهران پس از نقض تفاهم‌نامه توسط آمریکا عبور و‌ مرور در تنگه هرمز را متوقف به تأیید ایران کرد‌.
🔴
این کشتی قطری با داده روشن و از مسیر تعیین شده توسط ایران گذر کرد و بدون هیچ مشکلی به‌سوی آب‌های آزاد می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138609" target="_blank">📅 09:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVfnn5PShqEDT_rWlKAwUHt4ini94RCtXX1bIeuaQM6hdsxDcSXCVBIDfFLlJor-HlufZXR66gOf7aZrPhFrhTtUxefrORzC-zvGh5WEcKOlWf78WvGcG2xOZQpCAZALInFecynB-TyJoFqOSbO0TJe_1Dxu4GDFz-Uftl__Nwbz-azsle8FWeGGuzUAsHtw2e4MPPaQ7fzNIh75QhM6phDNelZXlosav6lUtYPUwP18wXY4rnUa1FNWDe6h-Vc9MFfUfYLYwbqGqrnoF1kGc-93Ifi1VeecmnyMOq4dqYaQM9TyRiM1ejlTYgX4wSEHjddMn4s7Xiwao2JV-yB1NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین در پی گسترش تنش‌ها در دریای سرخ،«مذاکرات مستقیمی» با انصارالله یمن داشته تا نفتکش‌های چینی بتوانند با امنیت کامل از دریای سرخ عبور کنند.
🔴
اقدامی که با هدف حفظ جریان صادرات نفت عربستان و جبران اختلال ناشی از بسته شدن مؤثر تنگه هرمز صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138608" target="_blank">📅 09:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: پس از پایان این جنگ، فکر نمی‌کنم تنگه‌ها دیگر این‌قدر قدرت چانه‌زنی داشته باشند، چون مردم خطوط لوله انرژی را از تنگه‌ها خارج کرده و به دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138607" target="_blank">📅 09:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTKkVf7bQc7a2vsEiFigRPNNXbgU0euaxuZGtzINSLHhG_gzbf4_KCiXGa4wJTkOUmonqUzxIHvHMw-8dIDRl4bltUZjkhbPWwV-hL-7h7VX7dfKVSIy8NKJXZmbUFhYp92YYCIr0-b5cAADHh-SFn10SKD4ANGzH06fD0rkqmwImuVtJ0epsblLCa3jFNJ7Z81ttKBADQ5s72d-ZbEhvHnlYuZPz7TjXa8xr8JnhPNTvlBC_UB08wrVdLVK1YgiJInFxIfKRhDYSPoypbBlOAWLlnVogeP9DXTxE0Pry3qyOBmtLQRwbbtLUjKDHnVPL9086Uy56ZmnJEEJ3TMvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CMt_vFvNxnWmgu_-oBKPeCJv11rybETeA2pgjL-Sz8X7k6u4KnFZCPtN2Vvrlv8kgNV68SaXSZa5hAAGBEdhdM0IHMaozU3bjgRFjpCcFoQKXdSuf1fO3HzCWS4TZhyP6ydlkR5I0EaCJC0xKAiWKZMie8YlhHFh96jt0eqMyVJFXRG6MLNiOpfNxkLSpyYlshSnBI9ln_DVwIkwwysh7GWfIMSgZHjmnIcmPb911mnkMSRhVnqvl7Ib5T8CwVPSzB0QNrRyPkyQBZaQhg81s5uz4Ui_Qy9tuBkCLJAGGa-SXw6ihsF9Na8_4e8Hn0bZcXmNOLTT87AhSaxjHjkDBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وضعیت قشم بعد از حمله دیشب آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138605" target="_blank">📅 09:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی، دیدار کرد
🔴
این دیدار پس از آن به برنامهٔ سفر وزیر سعودی اضافه شد که او با معاون رئیس‌جمهور، جی‌دی ونس، ملاقات کرد و به او گفت که عربستان خواهان کاهش تنش با ایران است، با وجود حملات مشترک آمریکا و عربستان در این هفته به شبه‌نظامیان طرفدار ایران در عراق.
🔴
منبع آگاه گفت هدف این دیدارها، انتقال پیامی از سوی محمد بن سلمان، ولی‌عهد عربستان، دربارهٔ جنگ با ایران و اوضاع منطقه بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138604" target="_blank">📅 09:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
الکسی چیپا، نایب اول کمیته امور بین‌الملل دومای دولتی روسیه در گفتگو با ریانووستی گفت که با سفر همزمان بنیامین نتانیاهو، نخست‌وزیر اسرائیل و ولودیمیر زلنسکی به واشنگتن، هدف حمله کی‌یف به کشتی‌ ایرانی در دریای خزر کاملا روشن شد: هدف آن پیوند دادن دو درگیری و تبدیل آنها به یک جبهه گسترده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138603" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b2815541f.mp4?token=gCxuKVzFWozTjHNGJ1t7RDi0GQT2CdgqQLUYEUe2BN6gltof-8GvnH52vnpJMidwhmI6A8eOkoO4Z8NrrVLMf0kTgHN7wQjJkuXP8QgT8OZiexXY3w9VWMXsVmfmRAaMRHesfNl7WHjB2lu8aPRjsiZwAkft9cat-652OOn-8bIHt8qVP7O8JUSFEKkr_4xSqgn-UyyyOQv9N95VK5HRReHNahETO5vpcet6WE9IstIcxhnf1nnrNY5FafDX66GmF1GUcz7JjO2pbB6IAlz-3xCqIFJsMqUwr8puWIJwufbRcOn6_GolmhmkDr7m8qBtgSE_U5MfICSyYKzNZMxvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از بقایای موشک‌های رهگیر که برای دفع موشک‌های ایرانی در آسمان اردن شلیک شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138602" target="_blank">📅 09:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a307c5f4.mp4?token=Nm_sTlqt0xCz9spWldZKNW4ZqK_uhIgepJs8bQ4-EruU72zHdH17mF1vIGDvwd0Tbvb40MlIegjgqchCcnxlTqQgmKeJGjDnzHmbxLBSw9r7fKUn5EvvIgJT3Gw8jvLoXRhn_MTy7G2Wu_dhWiSlI2h42E7S-9RQ9DFcjiHdUQNXPMywgiH3NhvjAaQU3hayI05f3Efj-AN4vhP5hs5I6IEm3KP_9x_faX8Yu7o3w-bSKVqXRlAq1Wh_ufair0AjHalcSvsKV5TMCM34OIHCmn-vDpwk8YHCyk8TrXD5MDiesGrOBfEsm4TUh7Qg9ay9d1fGu9WAsuvbsQkDt6VZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: اگر ایران به اسرائیل حمله کند، چه پاسخی خواهید داد؟
🔴
نتانیاهو: فکر می‌کنم آنها اشتباه فاحشی مرتکب می‌شوند و ما خیلی خیلی قاطعانه پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138601" target="_blank">📅 08:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=kP7IE3lD0_nGVPAPGHGVlJTeU3BNGL5M-cJYQtYfoyWaUbEE5kTlxffFnp-lPSsVROrwL-4pGPncEwHz_Fn1pT4lVINcOI2xzK2Zf_cav4h3vBxka50DwjUM0VR4ypGFSzHaBkVxYV9FT8NuSXJR0vJ56hDd0D-SBD3z9vd-FlFbtNCz_RM6O_V-wTc4miFz-5YvXKMcncHlBNzujWEyXdhYee4FiSw7or0rc3L2t4Yh0uW_tWvHdqrveYKg_F_yvX4xe7-tjZCiZwoeui1om8ko15cIsRMF_NZ9N1FmdWn2aUANxSlqoR2YFJNtf-GVlg_RrWv9mOH94p-jRrnk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز درحین مراسم ختم مرحوم اکبر عبدی، عادل فردوسی‌پور دست‌ سید عباس صالحی، وزیر فرهنگ و ارشاد رو بوسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138600" target="_blank">📅 08:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که پنج یا شیش موشک بالستیک ایرانی که به سمت اردن شلیک شده بودند، رهگیری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138599" target="_blank">📅 08:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339de1bf54.mp4?token=XcApzLMgU5yjOyeM_9BKiczj0CVsl5GHh2ApZ7m6AgQuxEiA-bXqjYK_ZRrHiq8yDFEz1seBz47_UUJ-KXOeZSurAiSRfMICjIGjJd6Rx7XF0lE8U9aGEHkcH9awZaCQqdmqdullW3KOfwId_bHK64e9GD6XFlHWMHdvRCSb6K_5s5zCJsqm0pEORdKJJLa6ifwH9AfradP2PPZZ2jNyz6mMoafAUamvaC37EFOSNw5bP844l5RjQFjcfKN80Ft0k4QisMKZc_7q36gdJ6iEcM5vpke-Ilo8mUeMKkffx3Zm4Y2Oy1ja6p9FX9bq6Ox-JyrvhdOXHHvUkP3WzmLdPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138598" target="_blank">📅 08:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwEX3BvCfLhEtpsix_w-2yvMTtEJP11AeR_Vb7hndUstVco4YIGCErbhdoBJVEQ6r2stzh79ZplEBU6U06ug-Z0a77EB9OpTArWS4G728ILuId4cnv0Qdm01NW4A5ajJoHOcw32Gd3hBEucsmplWSEKHIB3kHA3gYFGCEXFiweVrMUhq94GKuhiw2xKgQjdQ-MvWqsy_6dh51qvsvkJjF2EXqUOo59dxzaRLThAZEFT2ZJT5DBFm-BpGe5zKEvrUumL8HZa6YotzK-P9FpwjCIKecGHN-YTZV0sFZQacXBcJEp6zmUqOIM7s8rhCWwAEmZd_YfAYTZhh4avbiZBneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنت‌کام): ساعت ۱۰ شب به وقت شرق آمریکا در ۲۹ ژوئیه، نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در پاسخ به حملات موشکی دیروز به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
🔴
دارایی‌های فرماندهی مرکزی ایالات متحده (CENTCOM) ده‌ها هدف سپاه پاسداران انقلاب اسلامی (IRGC) در ایران، از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های نظارت و دفاع ساحلی و قابلیت‌های دریایی را مورد حمله قرار دادند. هدف از این حملات، کاهش بیشتر تهدیدات ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه خلیج فارس بود.
🔴
در ۲۸ ژوئیه، نیروهای سپاه پاسداران در یک حمله غافلگیرانه، چندین موشک بالستیک را از ایران به سمت نیروهای آمریکایی مستقر در خاورمیانه شلیک کردند. همه موشک‌های ایرانی با موفقیت رهگیری شدند.
🔴
بیش از ۵۰۰۰۰ نفر از نیروهای نظامی ایالات متحده در حال حاضر در خاورمیانه مستقر هستند و بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138597" target="_blank">📅 08:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnOnBDz3hgSglpn9iLfJZZTBM_QdOFOQapW91jGAjWpZK5z-TiKgzhXH5Wmh_PhYnOPuTwWIu4bbRZHIbeAvuRN21LlvPTwWEGgLqczn7pxnHtlgIbe0dtt3zAxoihMZMeThR2B3h3hle9fRRNarYgm2E5oBtqoqOhua7e6eCvE05p16g58Es3dnAuoqwzVKS3FTL9ZVbRNakzm6GUlFjtyXD4J7m90fOYtBP7Q-S8LOdlaeTYfwOCxoGJCbPE8wtHvoKZvh8wYP1DBK6TaDkRgCpCSQiGtT0hrOcHJGXG80BwnmSdmYWybLK_26TtuChiTQRK_229qrZwwjiu8xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده مجلس: استانهای دونتسک، لوهانسک، زاپوریژیا و خرسون و نیز کریمه را به عنوان خاک روسیه به رسمیت بشناسیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/138596" target="_blank">📅 08:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=lF7-h2rvIn2oiNiCrrx2jBkVNrFtZwVV__4_bZNwD0LqEtzCpis3UqUqDfEIUbH6e4AJeEfbu_-1iRxhLXajM3jJayfGrie7v4DTPd8fHH-T6Ff00ZWDncR9hgXEVxX9zglQrH_9Dktlp8SOvtay9O33kcJuXixl9o_3zTL4cE5G7EBWmwZ1kVJEk-yKR7xUMQfZn8Bl2CxlkhmApugp0G3WBq-0b58quq1QYjIezzCMtRpCptZ4dA1SRJs0DWwJPXULs9DXHlEs3Qzpou-L2fg4gF5m_CWiV4Sy7zxcFzgwY7Y8j1NU-PpqwlNZOob4AGVOa10pCUleHaygGTl6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3247c7e9.mp4?token=lF7-h2rvIn2oiNiCrrx2jBkVNrFtZwVV__4_bZNwD0LqEtzCpis3UqUqDfEIUbH6e4AJeEfbu_-1iRxhLXajM3jJayfGrie7v4DTPd8fHH-T6Ff00ZWDncR9hgXEVxX9zglQrH_9Dktlp8SOvtay9O33kcJuXixl9o_3zTL4cE5G7EBWmwZ1kVJEk-yKR7xUMQfZn8Bl2CxlkhmApugp0G3WBq-0b58quq1QYjIezzCMtRpCptZ4dA1SRJs0DWwJPXULs9DXHlEs3Qzpou-L2fg4gF5m_CWiV4Sy7zxcFzgwY7Y8j1NU-PpqwlNZOob4AGVOa10pCUleHaygGTl6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی:
اکثر مردم دوست دارن جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138595" target="_blank">📅 03:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بندر کنگان رو زدن</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/138594" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
جروزالم‌پست: جمهوری اسلامی ایران به منظور بازسازی نیروی نظامی خود، موشک‌های دفاع هوایی دوش‌پرتاب چینی خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/138593" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سیریک رو زدن</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/138592" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
اهواز رو زدن</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138591" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isIWcjlX8XuJg6VXAGqLCE31hlosqfJDXoM2AIZtF7bBP3qX6He4lcOGhYhwW3Fum-neuH3Tw2erExKgW-v2QMP1QDZ793upB1hOZYMTW2LABTyIe9jy5f0knlLu9FVV_76aGpyg_PqZOVvL91TEuskZyWxzFwfkT2Wt0LSWAassDcpiwMDkGuN2vveRrrXqQ85owiFWCXII7FVHb1Y8OBPB7qnZP4xIli6LZqU1VyHdINn2fx7ui46gTijlnNo-rSzornLj-LtxmM54xc8l79qTgGmYSRk3R9FrTDiKBMv1J6n1ZEIEXGqtw5tp5iPrwSRlFkle8q2UJ5U2dyh4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/باراک راوید: حملات آمریکا شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/138590" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گزارش برخی کاربران از شنیده شدن صدای انفجار در فریدون کنار
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/138589" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش های محلی از وقوع انفجار های مهیب در نور آباد، فارس.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/alonews/138588" target="_blank">📅 02:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال استریت ژورنال: دریادار برد کوپر، فرمانده فرماندهی مرکزی آمریکا، گزینه انجام یک حمله هوایی شدید علیه ایران را طراحی کرده که ممکن است تا دو هفته به طول انجامد و هدف آن فلج کردن توانمندی‌های موشکی ایران باشد، در حالی که ترامپ در حال بررسی میزان تشدید تنش پس از حمله موشکی غافلگیرکننده ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/138587" target="_blank">📅 02:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee0836091.mp4?token=CdKJYNdVi-VZ7n__OXVHdOuKWXASzlLhPqkEyJXmtA0FzgXgJNYpWFdS_91odpGdMqtH1eEAr59700v8NtIaNAWc1fXlJYVQOWJxkRDSg1z_tGCm7o7CCj1T5lFb85INf9Sb0yurKLxdxNLR2p8Os9ZyB1tdQeG2t4C4obPyxShZGGqwBjv1nzS_RTKDwwjQozV96P0XUXVmiNq6ftboOZwMRid4oufGDvcnRKi9ESAcTq2H1B93JwvsI0EtdCDVIi05mYrZUou22T1g_Zp0VoHU4Zg8p-gibV_dCBcI5durA49Xqwq8arL-O7a6kJNJHIVLrAaxyCvhaORODSbuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک زائر اربعین:
پشمام اولین باره میبینم یه آخوند داره کار میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/138586" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=nzcp8Yu0ZxRyeq1zafoFY41CsiOzXNU-EMrOfyMHoMlyVVmg2cm9jCy6TXLU4NVNcImIk540IKSizE7WAjbPLrjk7yaP-XkmV9OhQAwsP8rFCDRBJZm5dmTFKdeyrzgkuIB4yWJHXZz8HdJzLonYC49qm438UBQuGuaJuDfu1NXPke8qtE2Ed43gE5JyTAmfuBUVJW-E6f7ppuxxt701BpRWKYiyrcL7gj-SUEuFlySr1SnQ1SjzBKTtnAa3L7zGFOqiHHnsI3mMusQMvzBzxMJYhSOfeqLU3YFXi-9GPq3CWCjFdOoXr4yJvh_IbWXtekgBJdABGO647F8WbTUqFA7B-xcBHK_NIcgm7OQGMr5b8WTOH6E0tObjT-03FuqitBAXOP7SaCu3wgbml7rbPPbHlo_8AHtZBCiIdoyE4qRwIKXKSyHD29f8VtGQ9nhYrMhbEBOpxhmLecJZ4yQvqiAH9G0nMpjC5TSxS9zWgOSiSgEFS83Xc7FtxFWgpkhs8H77sYFWTqTfiDfq_TSYbcRdBsh6sLuTicUHW1X-h5mj4ednqUHZUcdr4egqeQh6vB1az-lv-_ztGBonNvshNMizpWRzT93DzioVgrMENFSIRgc6EFl6gB9yj90LOoorSLSMpT1_Oilr8Fs74szW4rrLpZZUnR_UcK67MjUCq1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501b0b150d.mp4?token=nzcp8Yu0ZxRyeq1zafoFY41CsiOzXNU-EMrOfyMHoMlyVVmg2cm9jCy6TXLU4NVNcImIk540IKSizE7WAjbPLrjk7yaP-XkmV9OhQAwsP8rFCDRBJZm5dmTFKdeyrzgkuIB4yWJHXZz8HdJzLonYC49qm438UBQuGuaJuDfu1NXPke8qtE2Ed43gE5JyTAmfuBUVJW-E6f7ppuxxt701BpRWKYiyrcL7gj-SUEuFlySr1SnQ1SjzBKTtnAa3L7zGFOqiHHnsI3mMusQMvzBzxMJYhSOfeqLU3YFXi-9GPq3CWCjFdOoXr4yJvh_IbWXtekgBJdABGO647F8WbTUqFA7B-xcBHK_NIcgm7OQGMr5b8WTOH6E0tObjT-03FuqitBAXOP7SaCu3wgbml7rbPPbHlo_8AHtZBCiIdoyE4qRwIKXKSyHD29f8VtGQ9nhYrMhbEBOpxhmLecJZ4yQvqiAH9G0nMpjC5TSxS9zWgOSiSgEFS83Xc7FtxFWgpkhs8H77sYFWTqTfiDfq_TSYbcRdBsh6sLuTicUHW1X-h5mj4ednqUHZUcdr4egqeQh6vB1az-lv-_ztGBonNvshNMizpWRzT93DzioVgrMENFSIRgc6EFl6gB9yj90LOoorSLSMpT1_Oilr8Fs74szW4rrLpZZUnR_UcK67MjUCq1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی بعد ۱۵۰شب کصخولت در میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/138585" target="_blank">📅 02:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار را به لاکهید مارتین اعطا کرد که بزرگترین قرارداد تاریخ برای موشک‌های دفاع هوایی پاتریوت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/138584" target="_blank">📅 01:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138582">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روسیه چهار موشک بالستیک ایسکندر-ام به سمت کیف شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/138582" target="_blank">📅 01:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138581">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
آسوشیتدپرس: ایالات متحده تمام مذاکرات را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/138581" target="_blank">📅 01:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138580">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مقام ارشد آمریکایی رو رویترز:
دولت آمریکا فعلا به دنبال ادامه مذاکرات با ایران نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/alonews/138580" target="_blank">📅 01:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138579">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش کاربران از صدای انفجار در بوکان
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/alonews/138579" target="_blank">📅 01:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138578">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه خبرگزاری خارجی: رضا پهلوی این هفته تو واشنگتن با نتانیاهو دیدار خواهد داشت  @TitrDaily</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/138578" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138577">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رسانه‌های داخلی فعلا انفجارها تکذیب کردن اما کاربران زیادی گزارش شنیده شدن صدای انفجار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/138577" target="_blank">📅 01:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138576">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=ooZztkinDIUC0J7nYiO-KGq1oUqJeV68GpXnKK_1gOQYeLQ-PP8UnNWJxv3znA2Enle3QGV95RkHiJv04wBSm04B5Szi-RM5UvUEJ4x4xzJkYZXoyyCdlbEpzan7BeL5AhkFEagAaOf4CZSFJQCI74i0693R1xNyGtspHD7ywquLQME0frT_DEBKMy2bJNi_2nozYfPOXoUK_gUfQlF04JpqkK2ZiXoF3PttvOzd4Twn8HSivFJSK518fStXVv0psD_OHpG9gclJi4DQN4atnby8WYN6MgOmIPdV92LMGjIZgqt27W9dAH7Bpqgbo_Cxngr2QjskQ6jJXMjf1jfAvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e3e7a39c.mp4?token=ooZztkinDIUC0J7nYiO-KGq1oUqJeV68GpXnKK_1gOQYeLQ-PP8UnNWJxv3znA2Enle3QGV95RkHiJv04wBSm04B5Szi-RM5UvUEJ4x4xzJkYZXoyyCdlbEpzan7BeL5AhkFEagAaOf4CZSFJQCI74i0693R1xNyGtspHD7ywquLQME0frT_DEBKMy2bJNi_2nozYfPOXoUK_gUfQlF04JpqkK2ZiXoF3PttvOzd4Twn8HSivFJSK518fStXVv0psD_OHpG9gclJi4DQN4atnby8WYN6MgOmIPdV92LMGjIZgqt27W9dAH7Bpqgbo_Cxngr2QjskQ6jJXMjf1jfAvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز تو مراسم ختم اکبر عبدی، عادل فردوسی‌پور خم شد و دست‌های عباس صالحی، وزیر فرهنگ و ارشاد رو بوسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/138576" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش کاربران از انفجار در ارومیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/alonews/138575" target="_blank">📅 01:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/138573" target="_blank">📅 01:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری/گزارشات از انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/138572" target="_blank">📅 01:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab42f37f.mp4?token=R8rtksZw0FSjzvrun2wKvwsiMcE4sVt-4INhHQN0JQqKlD6mmKsRdmiBI4wt6zvyeRYBtuseP9Gt92ylFpudZKQ4EMP1JY5Fvl9F6eywHCgu4RxkOAkOkhOOa2REqKkT-VS1M7ZzGfcU8HMwP3x6nxUk9nJotpwwiZ2ohztr4KEMFPKuM3xPQmEayoJWC230DlJ9xbSe5PHDs6fApPJT2GJRp-fkRwUcKSKhhkLlhzy6JHPN1i197WOX8Nyk0dWBbOpjOqXV0m-FK44zqeNWaild1A5K3VRvfTo_oJ53sb6BnpanwWJv243ggQp7m0M6f6iqXG8j_T9Xl0akbOmCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab42f37f.mp4?token=R8rtksZw0FSjzvrun2wKvwsiMcE4sVt-4INhHQN0JQqKlD6mmKsRdmiBI4wt6zvyeRYBtuseP9Gt92ylFpudZKQ4EMP1JY5Fvl9F6eywHCgu4RxkOAkOkhOOa2REqKkT-VS1M7ZzGfcU8HMwP3x6nxUk9nJotpwwiZ2ohztr4KEMFPKuM3xPQmEayoJWC230DlJ9xbSe5PHDs6fApPJT2GJRp-fkRwUcKSKhhkLlhzy6JHPN1i197WOX8Nyk0dWBbOpjOqXV0m-FK44zqeNWaild1A5K3VRvfTo_oJ53sb6BnpanwWJv243ggQp7m0M6f6iqXG8j_T9Xl0akbOmCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت عجیب عروس و داماد جلوی مهمان‌ها در یک عروسی در نیاوران تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/138571" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کارشناس صدا و سیما: الان چند ماهه انتقام خون آقا رو هوا هست، لطفا انتقام بگیرید دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/138570" target="_blank">📅 01:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">کاش اینقدر که برای مجازات جوان ایرانی قانون دارید برای آینده‌اش هم برنامه داشتید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/138569" target="_blank">📅 01:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55b2320513.mp4?token=BCDklrpwecdvnd8qEPfxQdQeZZieWNczBoHoMo9F3nE1IKF0nV5FKO4Vg9kGtdCr76KeQPS9TT86mDncJyy6B3Z0Sdv4XEUjrLOnRubnZztO9-92PnTRsJE3svzkpxuWPDL_OWFSDB62_pP9M4XarYyGbBTWd8WGSNVnV20n_c4vkL6BcCyeAl1lssa5uZqCrgi6d6pWZvY2iAtbTCCJINHSlMYEjfESsnrMonq90eU3spzsAcelJ4hvt6kLKIujK09LyE6g-LEIqztA9L_e7-eRsTkLm0d62otc1WcmPQ6xUDXw8dTdVOQ_ju29PD3A1psBqJaPpCJKOPMNy2zl-ap2yQKCvV895ZiXfrE_evXEILORBVq1z0ZBSKItr7jNy1bHWwz2xnw3W_B7b305DiFTWTTJJzG3ksfQ5HJiqoZ18sdLcu0w430zw9VABV7W79f7sGH3Vhy2vKEmI7delPFXTTcvN275xeBq21YFS5IBBVdNkZ2dEEe0e3YRtAIsyxJjSoh1bwjUoGE-tp6wHqCwRWsyBD8y4wI0I_kZ44xSyYriEyunM8Lcv2acQcZLwuG-S9sw1_74IR8vv5cjwwFf2xlIFUmwwxYdVZGM-xpHK7GWc6xkPeCWuAF3_ZQCRBMJ4bqRCgmJIrwg2q3jWSW8RQYpQeFazSfsDxefces" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55b2320513.mp4?token=BCDklrpwecdvnd8qEPfxQdQeZZieWNczBoHoMo9F3nE1IKF0nV5FKO4Vg9kGtdCr76KeQPS9TT86mDncJyy6B3Z0Sdv4XEUjrLOnRubnZztO9-92PnTRsJE3svzkpxuWPDL_OWFSDB62_pP9M4XarYyGbBTWd8WGSNVnV20n_c4vkL6BcCyeAl1lssa5uZqCrgi6d6pWZvY2iAtbTCCJINHSlMYEjfESsnrMonq90eU3spzsAcelJ4hvt6kLKIujK09LyE6g-LEIqztA9L_e7-eRsTkLm0d62otc1WcmPQ6xUDXw8dTdVOQ_ju29PD3A1psBqJaPpCJKOPMNy2zl-ap2yQKCvV895ZiXfrE_evXEILORBVq1z0ZBSKItr7jNy1bHWwz2xnw3W_B7b305DiFTWTTJJzG3ksfQ5HJiqoZ18sdLcu0w430zw9VABV7W79f7sGH3Vhy2vKEmI7delPFXTTcvN275xeBq21YFS5IBBVdNkZ2dEEe0e3YRtAIsyxJjSoh1bwjUoGE-tp6wHqCwRWsyBD8y4wI0I_kZ44xSyYriEyunM8Lcv2acQcZLwuG-S9sw1_74IR8vv5cjwwFf2xlIFUmwwxYdVZGM-xpHK7GWc6xkPeCWuAF3_ZQCRBMJ4bqRCgmJIrwg2q3jWSW8RQYpQeFazSfsDxefces" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمادالدین باقی: چطور میشه برای یک جوان ۲۰ساله یه روزه حکم اعدام صادر بشه؟ ظلم‌نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/alonews/138568" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u7yqM4mb4BhNl6VjMCndSFnCBskd-9Abr2GdOevQlwUCo-trwg6zSFnaVi70JcceevYPrMXbsVFIexHpB8Jn6SR_FJ2IX14SsTvIhCOegcTpIiq8t3j5cXkJ4MoQ7QzEKRTlFbMhiuYUSnDaGO7tvgJ888hq9VIT89JuD8ImiLRuDsfdbCc5y25DjRdMZb2bKDWR7XEr2e_jmnTjzaZ1V2FeQ9qCvfCbmhiR1D2ffy4NMiXTKaSz0UH0Gi7Ua7vF3Z44o5h1_R0X6wDD0M33hC06Y2pfJqAWHdEeB1_9SySzuLxHzFDNZrWivmgAJCJH5eVWIP5UhbHN6_OLXT0FyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=u7yqM4mb4BhNl6VjMCndSFnCBskd-9Abr2GdOevQlwUCo-trwg6zSFnaVi70JcceevYPrMXbsVFIexHpB8Jn6SR_FJ2IX14SsTvIhCOegcTpIiq8t3j5cXkJ4MoQ7QzEKRTlFbMhiuYUSnDaGO7tvgJ888hq9VIT89JuD8ImiLRuDsfdbCc5y25DjRdMZb2bKDWR7XEr2e_jmnTjzaZ1V2FeQ9qCvfCbmhiR1D2ffy4NMiXTKaSz0UH0Gi7Ua7vF3Z44o5h1_R0X6wDD0M33hC06Y2pfJqAWHdEeB1_9SySzuLxHzFDNZrWivmgAJCJH5eVWIP5UhbHN6_OLXT0FyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید جلیلی: نفس دشمن به شماره افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/138567" target="_blank">📅 00:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/رویترز: نتانیاهو پیشنهاد ترور فرماندهان سپاه و ارتش را به ترامپ ارئه داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/alonews/138566" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
هم اکنون پرواز تعداد زیادی سوخت رسان ارتش ایالات متحده در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/138565" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/138564" target="_blank">📅 00:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/138563" target="_blank">📅 00:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال 15 عبری:
آمادگی‌های آمریکا نشان می‌دهد که طرحی برای یک اقدام گسترده علیه ایران وجود دارد، و نه صرفاً یک واکنش جداگانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/138562" target="_blank">📅 00:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ6gDBdJHzTkp5mhkuVWeO3zSTvAI4hYFf9WcL-E3vdGuqvR_kMbEGoZ9IeEC8m3rXb1gpdyjRqZQjLQn0PBBxdu6NHQo_w4S40ljYkvVlLJ59OUctVUeTRYtrs1I-4-9c0Z72y31Yh4CDW0FLr04t2a2ccGMmXcOLW2oz2akswwTntNOLnnxvAJsohxDnjyFigsBzYa_toq3LqS2UYtgRvznxJGU9BefFZMpi1XmAUoFmWX-B2Q66dDci02K2aGWtyoWWmqpv09vARHFLXvPdvfl56vAt0IKJ9Kz-s553P2Z4O58mjFTbeF7vFu44agoK9I9aOBmaEduY3ybKS3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مجری: عموی عزیزم‌ محسنی اژه‌ای بابت اعدام‌ها دمت گرم
🔴
پ.ن: جواب با شما  #عموی_سوباسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/alonews/138561" target="_blank">📅 00:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/138560" target="_blank">📅 00:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cevJ5Gs0DPU4t5CD1qjQytSU15KJK2rGJ_Cnj_R9Wsdr9tESlB44eU5WCwnCgvrq0gaxckpAyTmvd-HIJsgWfccOh_zet9DzDxyWXQ_-K_iYYXt5ddYLpVrk4D00qcl5wlfns4X1lqy6Ofsc8g39cGQkEwqM4xhqp82itRsUENpSDMi6TxtrY3-OjN5jvmuXaAXkaXn8zO5OUP4y5_EU7dDh0AiqoH8MpuRNCg4ajIrfdVNtyIK3DpIo96YyyDVBoUqTjqnvOPC4GBHY0lg3t0kX2YOgt01rOMrNIzS8PM5Azix2_Cz2PGq0Y4JLgWil8Byu9T_Zyx8ysTb1ZPLPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال محسن رضایی: برآوردها حاکی از درگیری شدید و قطعی در آینده نزدیک است
‌
🔴
جغرافیای جنگ از همین حالا در حال گسترش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/138559" target="_blank">📅 00:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ergpc9Tpop-gwDN_j5qQ-FBLecpI_hCYnh59zxorjD_s2jkPbYIXlL5t1x8Zbh7JLjk3NfU7H-je3IL9sV4YcGpYLxsEP4cO9utrVpGxSwf7PhxsYna9BmDg37-oWI2CFmXTy-v6N9c3fHtAP482po6RsiSfl2MiLuihl8Tv0nuqPNlTKRG0HMGYuXO4hmp2bp4IDkHU5brdJ9dr4h0YgGqCYVC-Zl_CrvkeXjinz-r-gANvI6pO_z0J_DcGNfVUKxrzrF-egn23xwpFRuwJOvchFqLGSxtSp8IUxZNOv-hjfXYut59vPmiD-6TV1aOZcPa7sjEW05QTuPZrKaKt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود سنگین کشتی باری در مازندران؛ مدیرکل بنادر هرگونه انفجار را رد کرد/دود شدید مشاهده‌شده، صرفاً ناشی از راه‌اندازی اولیه موتور این شناور بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/138558" target="_blank">📅 00:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شنیده ها حاکی از این است که علت احتمالی عملیات غافلگیرانه شب گذشته هوافضای سپاه علیه اردن، تلاش برای هدف قراردادن ژنرال دن‌کین، رییس ستاد مشترک ارتش ایالات متحده آمریکا بوده که با توجه به حجم انبوه شلیک پاتریوت جهت رهگیری، می‌تواند حقیقت داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/138557" target="_blank">📅 00:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTliwW53huL1b2mmeN0gC2knuTYvmn0nscKFXCZ24Bp6EYcsaDYSt7cBwQLZNhRi2JoVQi2nJ6rAMI7gSWPFgjkRp4_LisShBu_mNjuSvyTiBGpbCcHxPJAdRKNLAHSJw8I9w9EnU6ukqjtNVIGVqb2hI4mWN4cfrkjcIX_pI7PlPkx3aV62sTzX7_aGhAYAtBcas0IAqWo4iFnznZk5FAhNSq-nsDEPk3HKP6NmRITfDFuZ-O7TOrv29ZHeJ3DlchXWowcscXBA70e6EgavCR2Z8FgemKh4t-dZ5tB4KmeB4_C3D-H6PsOqc_UNIHizmm9WyXkF-4sksKu30a4N8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت تعدادِ بالای سوخت‌رسان تو منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/138556" target="_blank">📅 23:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / رسانه کان: حملات احتمالی آمریکا دیگر تلافی جویانه نیست و گسترده خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/138555" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
