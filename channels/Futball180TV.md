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
<img src="https://cdn5.telesco.pe/file/S2f7k9OsDcygU_UauoYw1PX4vlFWtnpEMQtq4FfE0Yu-3TW5Fb3-DVkN1IFkiDmzsztmSm6EKU0P9ry49aUoNw1tQDeNtTTL5FeKCcRMJFSBCyqvDLtdERLXjQA7IGjjWQge9bKWR2hqgeC_ht4DSrQsf6Y0omcJahcaEyej2lVtHfe-lgopqTipeMqb_G_kQj8saRuMv6rgLHJUc-8IrmoUQ3EumCxYBealmC7a7wR05mEqKC44vJ0rHpssifKf-HFnxBx89hFXtuIqOO8kgMNgle23fVzYP3vuSziNodsriWFRTh8N6kb4TI1hufTfuPwebWicsDDAxYy5HlUYIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 566K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-93241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/Futball180TV/93241" target="_blank">📅 18:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2YARgmmC2RL7BcOpZ4Q72YGlRcgg9C_zEAPTvBA1FfiqD9KEiXUtXpwywjQw1woRbDTANbPlPulbwu3jjeU8TCbBWcF2uCeQsKHtIk8YPtzmHYNkWLyGz5cbxSZzIXd3KwPt3AEL4RNoIow6Ayq6ZgBt5z49_9d-6ul7G4CvCM9eDn0mM-155hgXoJgYPv_n7ey-mr6SocMd4-8QUn6ZA3vQE_M7it_EzdNZM57ANK9q-u9r6QGGiCpPJslfQUpLxFr25h3hnWYGisFdbFvE2_rcPfqCaY8JsCUqDXyjMkx71GiHIdBaTx7NJ1DJWCINJcoESeG7c8KAPI5kSUhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آقای گل جام جهانی
6️⃣
2️⃣
0️⃣
2️⃣
رسید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/93240" target="_blank">📅 18:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/93239" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
فوورییی  بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/93238" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcaPwyi8eK_ebUgnLnGEDfEJCgZVuPi20swcsN9mQrN1J5nriJCeA6AoVLwqTbR8rCMb0t-6fy8zlrf1kGXZYa8CK2YQj6dneglXaSfkq8jZVLqMA_mxIPP1vGT5xEa5Og7WYwW0t9NFICstxQ_BFrB1BDy8QFbE83u7fj_vXegnXlSJvbHm3CcHe_2NtFbSqXX_K90QD66_jPMe0JziD1eFRfzn8jjQvCJzEfnQ6v8ogrrIuVwNRXzdLBda4Rc1-yphOrW7xSZVIIcal1ryYINAcIBmkD7mkVuX_oGmJyIH9zz8jpnoYCLpJ4o5jlZ5M6fTuG4ouPUPz1xWKDtXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی
بعد از دیبالا حالا فردوسی پور با هویسن مدافع رئال مصاحبه میکند!!
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/93237" target="_blank">📅 18:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کلیپ سوپر آدیداس از مسی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/93236" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTmKCB6iMso06LBqcpsrAPISWXWR2ipL1OfWCqyW2K2IW7YsfMGApO_x8deshL5dcxvTHQz_c9FffELtv9EEjSLNr1HBD8tkdCPTQ7ITZsn_Mt3w6g8759pCwJKq8UgJ3wELgPlmoeH_rkK4-d_KRL3zJuY9RXOTlUm2D0YbTxhonlqQtgQ6HkdrC0DywwSiGuF6Ubp24GJAACO3khNeGgeSCKm7QlVsQSBgOnMovvnEqJmpH1cmmkZqJ9-gTCwofCx1oNpNbC5QfoejtnJDF1Uf6-UQWhHtbwYW71e1CI4P6UHgAi9nvjZ7bSW3tlQd7ESHrsWK7vPKCMy5KWdX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست دختر کش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93235" target="_blank">📅 18:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ونس: امیدواریم متن توافق با ایران این هفته منتشر شود.  خواهیم دید که آیا تهران حاضر به امتیازدهی است یا خیر!  🄷
🆔
@EsteghlalPage</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/93234" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f00a8073.mp4?token=Fpyy8psaCgHOqNrsuYH8N6Jrzfh02NZCrQwnjd-bKmQCYA9M0N-7oe-LGe8tyc1IaIff1th_HPel_O_VPx7sKlrOqhWx48M2DbUPKGqVGELCGE627OY_rrsG45ZiwV5AFKe-jIcr2ugCxZRkwr0RjIVHhMsOG_AUnyNT4ToX4F0JnFTPiCztuqjjLYvercBTQRUuxh7xT38cIgeIZqOKqLE3tzIj-VBS5H85N3oPRskq_cVh8t7unqYugW2E0fKN4Zhj3qurQsgvVr0HNiJGeXpxx3dqAt-kEEqOeQr2d87MPTDP_gEOlBrd4lZhY9VTZuSI4UufbbiSWk6tfxCuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f00a8073.mp4?token=Fpyy8psaCgHOqNrsuYH8N6Jrzfh02NZCrQwnjd-bKmQCYA9M0N-7oe-LGe8tyc1IaIff1th_HPel_O_VPx7sKlrOqhWx48M2DbUPKGqVGELCGE627OY_rrsG45ZiwV5AFKe-jIcr2ugCxZRkwr0RjIVHhMsOG_AUnyNT4ToX4F0JnFTPiCztuqjjLYvercBTQRUuxh7xT38cIgeIZqOKqLE3tzIj-VBS5H85N3oPRskq_cVh8t7unqYugW2E0fKN4Zhj3qurQsgvVr0HNiJGeXpxx3dqAt-kEEqOeQr2d87MPTDP_gEOlBrd4lZhY9VTZuSI4UufbbiSWk6tfxCuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای بیرانوند ببین کاراتو مرد مومن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/93233" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTecgQxwStG9oeNE2zydJIBQhCjMJKJrkLhuhBtw-3oYgJQHHbIQpe28QYHglr-cWmGracR4f93k96Iw-dMPmH4_ggksYXONxbmy31kJZFEqUv8QBiM8Oflm9ToSIcczoHJ8nynlxyWYCjp4Mj8LDAUfwDqWakbsMBVrik9JTS7OX5AbQqVkxNPPmZEtXlylY_Sr7w9eRwUQ4YWFCzdDocfEnx4txQNsdizuvCFW8ciSd7FoDVUVQgYa3AeAnyilBlZgbSwkxiuhYRTXb7uOWLy_nnJI6b8Cldf9_OvH40pZEMDgDUM-ctUEBSCzAc5sZ089P6wZyo85shdQ8RnCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل کیپ‌ورد؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/93232" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapp | اسنپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk3Q3xh4vqSBl5nKKp_zZRRiL8yysej9s_GoyfoOL-tQEA6UGSEtoonH4vB6Ow-nL0F7-md1gGQkGg981DsbcKosPBOYT4_144ls8rsS1gRzzvxh8WNtGed8TBiPp9qBylvAKHVzjS5SUjMVuqT2BFfbkhr34VTTS_So1C70z_01AdIxResBU-LEt-BlrVRbsYd4dTMCY6-6vFQv49aSaJitSLnnFb9F6jWi74AjFr2KdfIodxcKazo2ezhyBrF-uKfsMBe_qN_TX2vjosSnBnbZ93whQ8jnEb1ygMSLoANhZ9Ie41EjIP37RwtfAZl9uukKr9lN9XTGHBSxn0VlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران - نیوزلند
نمونده.
🇮🇷
⚽️
🇳🇿
⭐️
با پیش‌بینی این بازی، هم
۲ برابر امتیاز
می‌گیری و هم وارد قرعه‌کشی
Apple Watch 11
می‌شی.
⌚️
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی
«
لینک
»
بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/93231" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc8gM53bvRWUvzrZ8eGnRpiBEAvhSMUTdf4qk5v9YqyU_F1lRKGjnw-eMN_JYQgZeE6BXVpFunO1fA69dn6F4aXGSLhigcHKskSzdFjL2ZpKgLbO7AVaAQfHc1juCV7kULlhvDruksujaD2FyQlHgs9Ca95jet75JfhSWQj1kxiGJqw5tYJY4nXH2WE39SLCTlxuCt0m8BBe-nZMjKX5Tg0tCvPqgReMSk-VW_7TmxjaCzm8HYuEtCxAsAg8urV2TqvSOstXuThf3upwTT69UOFn2HlqBAPG7o5cwnHqtDKTLUkmFq9BCIKlOIof9BR0uPGIQQHyyX-fOQo2R6iQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
آرائوخو:
«در بارسلونا احساس راحتی زیادی دارم. از هیچ رقابتی برای حضور در ترکیب اصلی نمی‌ترسم، چون اعتماد بسیار زیادی به خودم و آینده‌ای که در انتظارم است دارم.»
«باور دارم که بهترین سال‌های فوتبالم هنوز از راه نرسیده‌اند. وارد آن دوران خواهم شد؛ اما این بار با ذهنیتی پخته‌تر و بالغ‌تر.»
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93230" target="_blank">📅 17:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_W2V329D5OU3ce3s7-XKcwiV1CSpkKYOP58-z-HMUdZSUVKdDYC6LIhluBDlbOr1MjUygc08QT-az4jZ68vo9XyDkCjZ2VBkIljqhHakvFZnsz6j7tfvQ8qgMUwjO9p8o5Zz3qQTpihyK3GC5e1wre9m8v3SAIzhXEzC4RbJwU9CIw26bW5gFsJlGxbvmAgigNZgejKWJUrsa4HNZp_h8mI_XGPbf028tmTRv0R98sZaR-EpVePxzijauyL8-MDQOn2mOQahN-ifEWMuK2Eq9d7e_eJ7PQh1YnWD3EJ6rXW1XxZJsJSu8ZSVpZ_Su0PDy7IIhdsiWCAWxQ6mW8PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون بین المللی فوتبال (فیفا) به دنبال برگزاری یک مسابقه نمادین بین تیم های ملی فلسطین و اسرائیل است
هدف از این مسابقه استفاده از فوتبال به عنوان وسیله ای برای ترویج صلح و وحدت جهانی است، ایده ای که جیانی اینفانتینو، رئیس فیفا به شدت از آن استقبال کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93229" target="_blank">📅 17:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
ریدمان عجیب میثاقی هنگام شروع برنامش
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93228" target="_blank">📅 17:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd99b8a0b.mp4?token=ZvrzH0vF7jzkQgKMNGDpQCZBctzkZUucYNsikcTrjZ01w9vJ4YVtf0YVVllmPEtnx0AEVxOg85eh9saK0kDb7GlK76PNlHeyna7iYxGqkmHbFppBKX5PoZz9ivbkw7XCMFBN9kyDdT_Ig6ZV_WIz_VrFYpV32tpIgjH5fU6qfk1h-DdJdVyF0c7brNr62LZVu4dT0dyp6XYg53kVMnePaUZo41lK9xqTvPBaBPqE9Qg0GFMlr5NDDjwHd_M0WAnmumlWwg8y2M5lQR5EU-nbUYLlT590wjcAUsxe5jiWtSdKV2UaNseQ0ZggWxzfKyIdJqXU3KM6RNd4kUjmatEXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd99b8a0b.mp4?token=ZvrzH0vF7jzkQgKMNGDpQCZBctzkZUucYNsikcTrjZ01w9vJ4YVtf0YVVllmPEtnx0AEVxOg85eh9saK0kDb7GlK76PNlHeyna7iYxGqkmHbFppBKX5PoZz9ivbkw7XCMFBN9kyDdT_Ig6ZV_WIz_VrFYpV32tpIgjH5fU6qfk1h-DdJdVyF0c7brNr62LZVu4dT0dyp6XYg53kVMnePaUZo41lK9xqTvPBaBPqE9Qg0GFMlr5NDDjwHd_M0WAnmumlWwg8y2M5lQR5EU-nbUYLlT590wjcAUsxe5jiWtSdKV2UaNseQ0ZggWxzfKyIdJqXU3KM6RNd4kUjmatEXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریدمان عجیب میثاقی هنگام شروع برنامش
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/93227" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZxTyfdcekpJcU36Q9ibsJVcTrkSO_OotUhLYjV5ivpAwg68S30Wco2hA_IOdyUBt7inSlu1_Ixdkw_fHsuW2rnbvikRj6HCEDpDZPxOTKb1wPCjpiyNxhmghhlAxWXd1Z4u7s4UeD_lHiDBijeqyYbbPS_I4a_XQgg2eJWakb7nCVWQmTkMYxZ-3YldINVdQ-aFM0Xr26UVozuz6P0vQQO6dLmJ3q2CVuxdgzVwPeKToUACqjQhr15K33EcYqqiZ7jlvF4JaoRisLnKrZ7CNCa4vYYRMQ-_3r0o4YzCjDoaKeHbpT5orsILGwylL7OdJepQeAWts6NUOkk5tWLNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
۵ بازیکن با بالاترین نمره در جام جهانی ۲۰۲۶ تا اینجای کار:
🇸🇪
• الکساندر ایساک — 8.61
🇩🇪
• فلیکس انمچا — 8.51
🇩🇪
• جمال موسیالا — 8.46
🇨🇮
• آماد دیالو — 8.45
🇦🇺
• پاتریک بیچ — 8.45
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/93226" target="_blank">📅 17:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTRrwnrInOc05cYJATBUg-RrFBSqAWZbmmac630s_U-u9OpFt8azTPtH0lwWzmyqa_jl8ElcTyOPZg8yhM7B2n-iwFehg-nBw5cZ-UNcJa8idpv7hoy8ekNvVvD59Nbp61-R3tiwa7fMFboJuvgsIB05XeTA7NdFUoSBMxslabj_x6kbUi96oth-fpcDBtOpqVxdaeVfJg3g61d4MnULmO6MevWBhfATJDLoUMuhmhkjd22KeSS8nKEteYhc7-KtUsbv19gEjp8Qp8YhltUX7gAs9tXXD-1oD4KbSO-_AeAuQhItdhHanCBsGLf65AA_-qH-IhXs_DGf3EbNar6wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو به نیکوپاز ستاره جوان و آرژانتینی رئال‌مادرید اعلام کرده که در ترکیب اصلی ممکنه قرار نگیره و به همین خاطر این بازیکن میخواد به حضورش در تیم فوتبال کومو ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/93225" target="_blank">📅 17:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9xzggaoONJJ722UTA7hnhYnxUAxKdCqqzj5YogJU3Ou35Q6mMe3EpiAjBSbNeBGE8CTvI-RiUOtDx7EcHeE_xZEEdclEIyiAFVDAhFz44ybZSBoTUyIFckx9PcP3l5kPjF3pcx9vikljqmT42rLu1WCzrBXQ7QD-RcyldUFMAfMaqQE-_eMpQQOodjRRcU-xa6UWN8lm3TePV085MKLDsfFIYOx3W2CqZyLo_yHQTrfaOw2N4d2fEIDTK-H1DtntmiIlNPooR0YtGQWCDTd2Fl_HmOiHbTvAAz-0RSAFb9Jv1T6HA3y4QxzMGgRRMpZStg7ylH34FmV8gEejXeq2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل کیپ‌ورد؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/93224" target="_blank">📅 17:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ3h2T27b2zdDQhkE68Cg2CdiHqAzBChvtRT_MtHj-VEjblbD95S20eruEjkPmtjted9h8w_fx2PtlTaAtO_HHKztc4PfUYvOXOeX4L7nEp1-glnnq1o1LiSxtMO0Z7o0mSs_9eM2PQw1fvr7dcQGnAVFCih7NunL38wNo1kj5N127-Lp82VTQoX3uWHCZm1AZCEEUN0k3u1Ou-Plsc_Jk9g9mbSzeTldVpkyNF04PE03_Q-G6dN5WZAadrNa594-KwUbjQw8t1od5gmXaOIqt6SKeWLdus7aOksjkcLwy9d_ZSIF5pO_DwdZ_Mx9amFBoEukwd6aoLIp9N5Z9QRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
آرزوی موفقیت سردار آزمون برای تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/93223" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🏅
🏅
کسری طاهری رفته دو باشگاه استقلال و پرسپولیس ببینه کی بیشتر پول میده بره همون باشگاه
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/93222" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae9858e70.mp4?token=kPxrPrioPva2xOyaDNgrlFcmWLj12LiSxb8Mf4GcriqgajebyooZxN8-S7KxSajQvEokFvMBJItP6m-LiNtHQUCYbQyIAOtT1n9tRk8Sp4aB3I2bKS9zo0hksB2Le_4BbeRH6HfzEpFScenlaO5YBaPofVDHAAAdCQWJ7ZzRogn4sQ4woVmzxE0Re6-O-HSK4DTSk0OOd1XwD811OO9cYoA8PC9Keee9i3SZndnaEAwqpnSpXZ-7e4sJxkf0kp-hAIli9vAFXOzUPMX1eESLQDgBu-IqAS7oqxLxc_ne5Oa2SrMhG8PG1iJYHm8NRcJIUiy4xe0OkTN1fs7fUH1beA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae9858e70.mp4?token=kPxrPrioPva2xOyaDNgrlFcmWLj12LiSxb8Mf4GcriqgajebyooZxN8-S7KxSajQvEokFvMBJItP6m-LiNtHQUCYbQyIAOtT1n9tRk8Sp4aB3I2bKS9zo0hksB2Le_4BbeRH6HfzEpFScenlaO5YBaPofVDHAAAdCQWJ7ZzRogn4sQ4woVmzxE0Re6-O-HSK4DTSk0OOd1XwD811OO9cYoA8PC9Keee9i3SZndnaEAwqpnSpXZ-7e4sJxkf0kp-hAIli9vAFXOzUPMX1eESLQDgBu-IqAS7oqxLxc_ne5Oa2SrMhG8PG1iJYHm8NRcJIUiy4xe0OkTN1fs7fUH1beA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
اتحاد و همدلی در فوتبال و جام‌جهانی؛ بعد بازی و شکست دیشب، درحالی که بازیکنان کوراسائو درحال عبادت بودن، دوتا از بازیکنان آلمان هم در کنارشون اومدن و با تشکیل حلقه به انجام اینکار پرداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/93221" target="_blank">📅 17:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trY9_tWbZaARdKvrP0DIwZi4n8dkBnI_pFwZ3ptRJHl-WgzDZ5FN1-ozMMK_le9BUsFZY9nTOxuEQ7pF0kqEv9Mn7qMfGn9RjlgRi45XpAhvKtsEsyuSP-Pyi1TKKeJ__zbDg32k3QImaDXApa6cszn3vtW7uJjX-tXabPzcQ_IVtojH5DQ6wUkBUeSLHbMAlEE0VQcujhat309XOG3yzqma3K_5wTCiD8wDWvycuWnQmbmCUxZXISVi83yKVFt8mDkHh-Ekq-wdjPQr4n8rph8DooLBse2TMjptYQR9g57E8T3tkPoFKlpYexf7ZQGJ0F49qyb79ng3Kmuu6805ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فووووووری
؛ مائوریتسیو ساری سرمربی تیم فوتبال آتلانتا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/93220" target="_blank">📅 17:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCmLa7V6RGGJGq6mUBu_jeKdhJQDImUKr3z4cRg0cWqi_Iix7x68B8gSOM-qRhGONBfiah2H2YN3KnY0uNstrKDJPeouUHyocg95EcSA9R2Fe3EeRyM6dyUWZyGS34bbFeTGdb7Y0HapaO3ZtlmOKnZ0sOqRHrkGXqB32dcQLqmTX6JxZQziOE7o5e_Dqurflc6oDbbonMNwtDCikBdluMifI7oUJQGl78Us4WIJyRuJfkiZw5ptkmwg3p8dhS2w1UGddbG_JKRIPcT-OjB-uE4H_vOTwqGrRUBAFuG2PtBpzIuDWtkIYylM0Edt0ucKBZLp-4ljPYyY9xz-oJ_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه هفته نیست جام جهانی شروع شده ۱۹ هزار زن حامله شدن تو کشورای میزبان
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/93219" target="_blank">📅 17:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93218">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e61bc4f6.mp4?token=NFp9xku6ZZdCQA7kadHvWDEsOzbt6QQ-Dq5kNaOgi7t5gBlnxq9W27NA9ArS4usFYeRXzGJcYNqAAdUJQj-hMVO1RBXrEYggHS98BuH3EDe_uH-brWhAjLSisFvGGNo7nHlsQrxWMYpCaEtGhl00uarvmDQY8v4RR0s0JnGNbVKewEfasC41BlMvXgnnFWUYnyUMF7IwvWE4CA1WX4lQxK7q4C4Gk96_Ka7EeZCumdI59n8YcWKELGgMtB935XLoXZIUCST6zjnX0JDwfv9FWybT6cd3DzmJo1dLTX5IflsaXNrKKqb6n9JtLwU2TL_8KGAhuLvTwRxBxKstGuvW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e61bc4f6.mp4?token=NFp9xku6ZZdCQA7kadHvWDEsOzbt6QQ-Dq5kNaOgi7t5gBlnxq9W27NA9ArS4usFYeRXzGJcYNqAAdUJQj-hMVO1RBXrEYggHS98BuH3EDe_uH-brWhAjLSisFvGGNo7nHlsQrxWMYpCaEtGhl00uarvmDQY8v4RR0s0JnGNbVKewEfasC41BlMvXgnnFWUYnyUMF7IwvWE4CA1WX4lQxK7q4C4Gk96_Ka7EeZCumdI59n8YcWKELGgMtB935XLoXZIUCST6zjnX0JDwfv9FWybT6cd3DzmJo1dLTX5IflsaXNrKKqb6n9JtLwU2TL_8KGAhuLvTwRxBxKstGuvW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
🇨🇭
تحلیل بازی سوئیس و قطر با هادی‌عقیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93218" target="_blank">📅 17:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_dxXNiGvjW03V18Xk_EhN2uJdWMQx8QXkOJWgKi3dLYsZbL5QMaImG6ZPDaIw9q7_mbK3z0KR6BJVGTwLNyaBGU6uBfWxOd5bpqvay6bCO3TasPLI85od4fnE0TGQPQKpJNqi2X9F5BjGOnh6Zex1DLiNChTjrPXBceVeHSp770Vy1jQyUO5qRxv2kAe2FXjb-JZdT7jD8oT4YtAYuJAGhCbK55sSQQJvlKFS9dVGTxgNANbMOkatMJewh9w0l4JAPLj5zrYaHKFGfKzAIvi1iKWau_RBG2GYhN5LFFy76q82r3IFEe7R_HpmmvqT-KbdCuRJbeULnUrp-DqohT9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XKNvOB_xM_TPhVW7Is4Uam6XxAJA2gt8-K0_VjmxCPuqY_S8Jho5X_nrLVZBH-J_P-Axn079xtTay-t75Q0ObG1QLNx11VaPkHmY7bAiRLNY6W9m2HXsJb0-5hNSI48FUJ40ebMQdAG_kKgxIVxTVSF-3NOvI3VQyalyewFuuRWGTaUF3Aah9UmQfWZCJAFGeUJvZp3PCB2csEeYBDJZ2AsPc2BCvKH6iOxde574qZuoyzM9-Xiu9jdRSO8K8wEeXPgK9gyKNnAS1Z-W8A8tcWUHvDyHcjaha0GwJSb1gAUj2LPtVLRfVJYjqa8hP3tCUBU5JKTjLvS7EhrSCTMpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdgaIkuCFzneY_6fE9RaR2Xn53wCp7VlxUfNlOCSLjodDtPV35Dts4f4T5ezUJcCF8YhFtkhElvKQdrKQ4kd1M9RX94cYePYZ9mXYLj4sSTlLe_eJlSYszW_m4PktovqNdPO9JuVk4IvWPzbXzG2idQN1JC8KFgF2bPiWwY6Ln5j5u9-jh-9YsuK5s5zi0HccxeEA_O0n_-HcQ816Mtj5gTbaz1qd2jLJbGpR0RLCk5jQqCOt-Cd1Dsid1eUcimYHxh2VlIoL-_9j4-o1B6cljWPAIy4XmbyqXLfkaaQhyh-t8cmAsf6gLaWhjY-8O97l9U73l4-XFIMbN0GDz2HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLk5EznPz674zzIJgm3sIZtwyG6t3bVZQNlDnYpE6tgx6BXMJGWc5mpFqC4KlVF-sBcA5aadwQCtKk9z2xpcXj-j4SQh8PiTt3dqrQpkkjFxLOG-sZXSQJQVBd5OjxfLcxvHNR_MAUylBHUq5HHJQuxHp3tu2DcDVR7WgE3uN0D4qgcrc47cXYvlLv-35W48LlRS0TeZjmUgJbpMx0dQgIUQqRTvM0RYM3ppVPXLSb0E9iz9Tu2UdPOYRfJ3LnYvgUuin5oohDnNh98VE34s8lstFI1MG_Hy1hRve4QUPFjqmHAGLk0g7fXSkiZcnI9M21DVrCAESOqi_ScPnxecvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏆
۲۰ سال حضور کریستیانو رونالدو در جام جهانی
۲۰۰۶
➡️
۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/93214" target="_blank">📅 16:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ماسیس
❌
قرومساق
✅
@sammfoott</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/93213" target="_blank">📅 16:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOGXCJ6sfgd75cxr5AE-4cTaVvf0d39-VEubxF7bj16C43ECOzYLoa9DlrzS7uFVfdw8DYp-ph8icvKXvGNnEBO9Nki2kjiAo-SM13f2bRYNJ8KU357iOoI1QO6rOklJ1ipYTTvEGQNkaWBH8DQt2EKHrPSreUHZ5zDrwOMG0pS5LRz9U25U1sO_FQfmHig0SbTFuaKZLJd1-LK3XxMZRkXUGSy7HQwOABYDSJIqjpdQq5pN4jeHhz7mAH8M2XGZobp1pOVjgncKEWe7ZlUDk_HVVZSRznwYk_coN4p2d-yR0Sn2iXeT4ttyvSHN384Qc5VSVrQDedZChOTYp88YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
زیون سوزوکی گلر ژاپن؛
🇺🇸
در آمریکا به دنیا اومده
🇯🇵
مادرش ژاپنی است
🇬🇭
پدرش غنایی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/93212" target="_blank">📅 16:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io7NGRE-r9pKjCGrb6KDw17sbV7Vgr0EdYKY3dTB9a69I1MdtxENZ5pmoZ7H6LAIZ83WRdRpl5rnv1sGie1p4LiXcehm9BoVG8uaB5weNxZ_Nj79rDghCucgj-6TLElHTEYYe5juGN7kznUJQ8Ny35PQiQ2d3i_dY3Wq1axACCaCEABndWS7mBoRJQDOGEjoRyBdJ4Mg9a_IPd_r6lqUdA2UbNzU275Y8osSGZ4r1T0jA7i-_4E1XluDVgZZpkK7AbhSuDbl7iWg5YpvQjMl4uclJRnzjhiXZoEeUTajIJtPP-Wl3FCZiy1LgEY0QVJi157HXvxLkODREj8kRDmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شزنی : رختکن بارسا پر از جوونه، وقتی وارد رختکن میشم حس میکنم عموی اونا هستم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/93211" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaZTGCCVbVzuZJV8DyuaGfgHyZfDhD2FP4pghMtyzDj4NjxmYtbS388ZD6BXIr2vNk2JGaBQitUIoSJcGdD6Arz2NqMOjT-MvmqN6ogpGm2sGgJoCUZlIh8RL8Z9fnErmdCkuqP127N7wHtqhM_kI8cbnfUAZG2vtPpw1Ba0UEG6KL-dv4CG8wkXS0OA5wcoiDsujoCkuh6EA1I1DttIwNqFIUkO8o46Tfz78-eAR4Pz3gA-5VZhh0c8VyGX4C2I6hVNdo68waYkMXrn0dnASCnaBRQyUsMqrNA8wRfvM97X-pxdCGd3XgRLqg1doyVezQKZB-L7K_g_wOpHiJWvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا میر بازیکن والنسیا، بدلیل تجاوز دستگیر و به 9 سال حبس محکوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93210" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veNXbyt3-anLB8aLSSW6hIz12yFy1KMSYW1m73DRupUoePgL-j-sOW1wnwvwmbDunn_rDWxdKCMpBkMt5cpNQGgkzhPFQG6RuGcx70MTM6zW3FFWhGZvFEGdEQGeMczcCBC6qiG_f8WD6PFVeXnUv2Vv-nMw4ovHixqYByFbo2iS69qz-F6N5LEzX1nmSoRQy9pl8u5V-vSnP4-nsWtcQ8KoFLlNIf8QVyJ6XYROLnuutZYCc0hgIfSbiotx238dmUa_T74b8aC5CeQe2DOrs3zbkdX-LkAuzmvNo5QNtOuN6FGsOMAolxV2qcDUPm2fx1Top7PXhiY6MnrN_it-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کادگیت از زمان جنگ هم فعالیت داشته و از اولین پستشون تا حالا همه‌ی کامنت‌ها باز بوده و هست و حتی پست‌هایی که مربوط به اختلال یا نارضایتی مقطعی بوده رو هم گذاشتن بمونه تا شفاف کار کنن.
فقط فروششون از همون موقع تاحالا به صورت محدود و هرروزه ۱۵:۳۰ تا ۲۰ هست.
اگر امروز بهتون نرسید می‌تونید
روزهای دیگه خرید کنید.
بات:
@KODgate_bot
کانال:
@KODgate</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93209" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fd2eb5c1.mp4?token=TCBF9bCBZMp6Pp7LJtjvvWvoBobXpQ_S_Zwn-fAa06q7PAM1eHi6JqTGvnZnGQhQoMINjizjdaEZwb_jL4rZAXfIa6-s1bfGHwlUVnvC736wTYQxJoE4OsU_-azcgRHEWsa-B2dNbtHsOPK6b4J0J0pTOlSD6fo14fUesLaJpzC9D7LhIcMZxB_4iuBVjrvYSz7_Qa4fRXBN6UEuzbefoE5CMZfYx_QS84XZmFnGgCW6-8JT80wXNElkH9_6Qfevveb9Ldun1TxSaRSPdwQhRjwX6f7nW2-1FWU2H15LaCKmucPA_chykhLK-J9UX2lDLp2NRxyxNObnRXmWZ5bWKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fd2eb5c1.mp4?token=TCBF9bCBZMp6Pp7LJtjvvWvoBobXpQ_S_Zwn-fAa06q7PAM1eHi6JqTGvnZnGQhQoMINjizjdaEZwb_jL4rZAXfIa6-s1bfGHwlUVnvC736wTYQxJoE4OsU_-azcgRHEWsa-B2dNbtHsOPK6b4J0J0pTOlSD6fo14fUesLaJpzC9D7LhIcMZxB_4iuBVjrvYSz7_Qa4fRXBN6UEuzbefoE5CMZfYx_QS84XZmFnGgCW6-8JT80wXNElkH9_6Qfevveb9Ldun1TxSaRSPdwQhRjwX6f7nW2-1FWU2H15LaCKmucPA_chykhLK-J9UX2lDLp2NRxyxNObnRXmWZ5bWKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
🇹🇷
هواداران ترکیه روز گذشته تو این شرایط جالب و دیدنی در یک‌ مکان تاریخی باخت کشورشون رو دیدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/93208" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa5f108ca.mp4?token=WmAryLvwf7JD0E5r4uoMQwPucQWNqqKIYDFNcoMhlqrboo7kAx-PIgX2Ph1nz5zBrS_SS6T0WQcejBxZoxlUtwqma-CWvXjFMrx1nyVGaSlPBbAZ9VCNzm8Me8Qnh8xCzC-CN84onsicEdc9ZC-WtpfRThKlNKxIGppYN_68Kz8eYJVFV19Qi_KiHlMRZ1fR2Ll_AFy5cOCqIci50fT0NGHxW4G6vQR4OmzIvDjSt4kwucfFgIZbiY_u1lbSMCc-PrQZaESdMeST8LDo8EF-4fLDTrlO4cVRu7N4Ovs8I9Usdgnp_IobRgUoUjiTEp3HK64mGsOmAwVSwJAAHS9N6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa5f108ca.mp4?token=WmAryLvwf7JD0E5r4uoMQwPucQWNqqKIYDFNcoMhlqrboo7kAx-PIgX2Ph1nz5zBrS_SS6T0WQcejBxZoxlUtwqma-CWvXjFMrx1nyVGaSlPBbAZ9VCNzm8Me8Qnh8xCzC-CN84onsicEdc9ZC-WtpfRThKlNKxIGppYN_68Kz8eYJVFV19Qi_KiHlMRZ1fR2Ll_AFy5cOCqIci50fT0NGHxW4G6vQR4OmzIvDjSt4kwucfFgIZbiY_u1lbSMCc-PrQZaESdMeST8LDo8EF-4fLDTrlO4cVRu7N4Ovs8I9Usdgnp_IobRgUoUjiTEp3HK64mGsOmAwVSwJAAHS9N6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
دستاورد جدید اوس جواد خیابانی؛ اون دیکاپریو نیست اون رائول خیمنزه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93207" target="_blank">📅 16:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca5c20464c.mp4?token=JtfkONq2dpP8wquXfL5YhLIMklK9uoz6nQx8osnFlxXFSauiwZ536Wc0JBAq4hLfutxCX-hbok4MDbDsxfNQK9hP3XI44evbb16VtrYKbhJcQdWXMD3OiQaDfZipRV2qwzwwYQw6Zho0bLYVYq9ZqAi2hgpDt9Jlw-reHDQDhNmjQbBcW7sNhRmkZwkVe5j2Trcfo7y1Z5s6vtkt0MeKblk5VGlof3bo_sDlsGem9qTQGFVm0ev_k2w6L7KMHffCeVlOtH73jw1IaEpqLEWdMHWpg5wqPcblDAaJDqFDoReWohCh4G9Pdhx1OilSNgd2-fjrHrfCCneQeaaHQEUamQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca5c20464c.mp4?token=JtfkONq2dpP8wquXfL5YhLIMklK9uoz6nQx8osnFlxXFSauiwZ536Wc0JBAq4hLfutxCX-hbok4MDbDsxfNQK9hP3XI44evbb16VtrYKbhJcQdWXMD3OiQaDfZipRV2qwzwwYQw6Zho0bLYVYq9ZqAi2hgpDt9Jlw-reHDQDhNmjQbBcW7sNhRmkZwkVe5j2Trcfo7y1Z5s6vtkt0MeKblk5VGlof3bo_sDlsGem9qTQGFVm0ev_k2w6L7KMHffCeVlOtH73jw1IaEpqLEWdMHWpg5wqPcblDAaJDqFDoReWohCh4G9Pdhx1OilSNgd2-fjrHrfCCneQeaaHQEUamQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇱
هلندی‌ها لامصب از مرد و زن گرفته تا بچه کوچیک همه خوشگلن
🙁
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93206" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ke5Do0_heaMx9YJk8BqiTgDhE369QuHEec0k4IG_RxmXYZ65SPPXZZaW352E5YmLC8rf5GOzKXaK7vsHezGCnICm64M55sC6u2w2ZPPg3yBhIh3rKyP0vwm1Sue9PMTXlOtyIL3-YSXngf4jE-CpV8FI8lqm-KgtJ-ty6QzZ86NIZUs1XOZkdA3b-645zrCvbRRjMR26L9F2mhxCRu6_r2k1ZrVpdwJyh6KbQizuGnBWNPcMu-F78sIGi0AzWnQjC3IERk7uQTMLu3Qw-DrmRimdSJzMG3W-GEv_pGSeE3FMC9rlrh1eI1F1VCKIfopenA1Zd87oBP3e8DrdbWeSSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93205" target="_blank">📅 16:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umvzsL2nn3BBZ0xdoWVyzdBe5HgNM2tfTf2gjvV2DhAMuFVQLlxYJumkzSvsUTxVEgKwMLMUiwcrqaeeh6RzYRthHu3nuK_rNyP7Ps6Y04n_VPM4S5apvctVjUvvG2TI8w93FCtEBtZaeLbmFxEzMxqvW5-OvTe5uNQHImSLh9bdj_obt-ekCy4maeqIMVKO3a4eiMnIwwChi6DA0VcH2oPrLUvoxeZFhsacISyFJ83iiaai0Pu7sjUy2-rBY0XNQwz3BMhPBX7rjQfuuFqSgCbkxLtXP-8qIM_SOKv15eJ5Lk-V2DXNITQEDptWxTkKZh6TXxmB5V5338NtGallCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
این بانو به عنوان داور دیدار جمهوری چک و آفریقای جنوبی انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93204" target="_blank">📅 16:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6X_2NBL37bE32R1DNA86fgjyZQYgpHdnjgNOhNm7PSfeCQ-_QLKb24--f5PAy7gpKdlb5MAD2Ip8eYmriTSuN9dYgAs8bKmX6oTmM_Tlx-hbTTJPko_wmdbEc3FxmjZKOVc6TmD2MpzGxaMSsthlYsrw2TF_vqASyca0Q-zlZ-E8YWY9DgNKV3yyHb5MoUjrrKJWnGZxL4ZGBuSPhF8lq-4A-e_PfGgf9r1J8LN1yklAdnnmZmfZQoE_hiGbE91kRQ7IqZ9heyjIWFFgDt9TyMc3X0Uu-eIVr7ilKL-3jSk3Eqmr8vartAN-x-6HaPXrbTQNk0Re6b_SSmmKy7PlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گواردیول:
این سومین فصل حضور من در منچسترسیتی هست. البته، امیدوارم سال‌های زیادی در اینجا بمانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93203" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💥
👍
مامور امنیتی اینجوریش خوبه؛ پایه و مشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93202" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d7892c2.mp4?token=PUCStXudADVhps1rn_wlvEy9ljWp1IKwN71GySebHgTUuG4no1GMtJoWbGlDqndstobWj1lMDppUrCX9GHWl_o5vV_KWbfN_1t8Y1p04f9JT-2jUYECriuYTEmE49i7MGPZmi_VrOgM8ZrOVoCzmak68SvBhCd7Y8g_iJnRhGE-JinO2HPsaRUbYxAYT_FpJ1ercxR2tUc6p7r50ro6LrUkYyQzurF4PlaGLCi9KQms5RjFr_lOoYgt_WGQtGev9gO3URgrPUWR1eGWzVN_KT5fukO3fdLiv819G-ZTVDM1RZgkMtRFgjUzxCndOMTG_mUG6NzlouRgv0zBIOQrZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d7892c2.mp4?token=PUCStXudADVhps1rn_wlvEy9ljWp1IKwN71GySebHgTUuG4no1GMtJoWbGlDqndstobWj1lMDppUrCX9GHWl_o5vV_KWbfN_1t8Y1p04f9JT-2jUYECriuYTEmE49i7MGPZmi_VrOgM8ZrOVoCzmak68SvBhCd7Y8g_iJnRhGE-JinO2HPsaRUbYxAYT_FpJ1ercxR2tUc6p7r50ro6LrUkYyQzurF4PlaGLCi9KQms5RjFr_lOoYgt_WGQtGev9gO3URgrPUWR1eGWzVN_KT5fukO3fdLiv819G-ZTVDM1RZgkMtRFgjUzxCndOMTG_mUG6NzlouRgv0zBIOQrZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
معرفی دو‌ ورزشگاه زیبای دیگر مکزیک به جز آزتکا توسط‌ رسول مجیدی
بازی‌های گوادالاخارا:
کره جنوبی در مقابل چک رو‌ که کره برد
مکزیک در مقابل کره جنوبی، ۱۸ ژوئن
کلمبیا در مقابل کنگو، ۲۳ ژوئن
اروگوئه در مقابل اسپانیا، ۲۶ ژوئن
بازی‌های مونتری:
سوئد در مقابل تونس، ۱۴ ژوئن
تونس در مقابل ژاپن، ۲۱ ژوئن
آفریقای جنوبی در مقابل کره جنوبی، ۲۴ ژوئن
مرحله یک شانزدهم نهایی، ۲۹ ژوئن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93201" target="_blank">📅 15:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇹🇳
#فووووووری؛ به نقل از منابع تونسی، صبری لموشی سرمربی تونس بعد باخت دیشب و سنگین مقابل سوئد از هدایت کشورش برای دو بازی آینده برکنار شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93200" target="_blank">📅 15:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ae2394f6.mp4?token=G4-716PhoimAKU2ZGcWht5n-DSZ4lQDtDMWf1a3qY1YWJEJaSaAdgKlyv7cNS6FW9GPtqh4NoKWI20jvH5KC86IfToH-reTI7k3aHxkjjQzinaDaDmbxuxSD96QacyV3hvQJcJDU0tko7a7-e3PldiJUauQJL5S_peyHy6ZBKe4n7gfwIRzykwRm-b1hSsTmpb3hjgvigmSlgxqRZ37ofi_otieaKJdKsGN8cAsZDQqmIQpdk2FGW9t94J6Q2idgAEtkht-LOGFHKTe571SGHJ0q1oJDPwnf_GVYOsfgcyK23qGs20AiZ4rnWViNyHz76ImN2Es6692JdgTT6WFJcR27g5F4nMqQXr2D48DIcS51g2srCm9sOsb02XDeoYhM5jYhYX31VJfqQE79Wt26aWdHxIgIcJwBk1-M4znhw7X82CVex-kHlUp5Tpiwdb2_TBukdFAlOSCa2Fsajj3ocFaDELIwV_jqjgC2fhz_EG_ekVT1VRRfgl1SwXTFWZiIUHpAvJT2qsCo338bsuRW8c1Sr7ZE-2IhZVHA4uB_viSV3g_J91cpX6rYnkmVUzk_6L3DecH03804cZ_m4NBErN5yoTpatFcQOkyfMI0TibAy3orykSUli5N7VF9NZ316N1I1n4K42ApUefc4nz4V837CmwLfzyYD3nlnJDrKeOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ae2394f6.mp4?token=G4-716PhoimAKU2ZGcWht5n-DSZ4lQDtDMWf1a3qY1YWJEJaSaAdgKlyv7cNS6FW9GPtqh4NoKWI20jvH5KC86IfToH-reTI7k3aHxkjjQzinaDaDmbxuxSD96QacyV3hvQJcJDU0tko7a7-e3PldiJUauQJL5S_peyHy6ZBKe4n7gfwIRzykwRm-b1hSsTmpb3hjgvigmSlgxqRZ37ofi_otieaKJdKsGN8cAsZDQqmIQpdk2FGW9t94J6Q2idgAEtkht-LOGFHKTe571SGHJ0q1oJDPwnf_GVYOsfgcyK23qGs20AiZ4rnWViNyHz76ImN2Es6692JdgTT6WFJcR27g5F4nMqQXr2D48DIcS51g2srCm9sOsb02XDeoYhM5jYhYX31VJfqQE79Wt26aWdHxIgIcJwBk1-M4znhw7X82CVex-kHlUp5Tpiwdb2_TBukdFAlOSCa2Fsajj3ocFaDELIwV_jqjgC2fhz_EG_ekVT1VRRfgl1SwXTFWZiIUHpAvJT2qsCo338bsuRW8c1Sr7ZE-2IhZVHA4uB_viSV3g_J91cpX6rYnkmVUzk_6L3DecH03804cZ_m4NBErN5yoTpatFcQOkyfMI0TibAy3orykSUli5N7VF9NZ316N1I1n4K42ApUefc4nz4V837CmwLfzyYD3nlnJDrKeOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇧🇷
بعد بازی برزیل و مراکش دو تا هوادار زن برزیلی بین جشن قهرمانی هواداران تیم نیکس از NBA گیر میفتن که مردم میرن سمت دخترای برزیلی اذیتشون میکنن تهش این بندگان خدا با هزارتا خایمالی از پلیس میخوان که مردم رو کنترل کنه تا رد بشن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/93199" target="_blank">📅 15:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e4e5fea.mp4?token=oajZYDyWEgKz8RSV0PQg9UqYu7xFkadb3leLw4c6NzxG7Ck794q1O1-OWBPLmZF0dGfuXAJAG2q8ySdR_PvTuuxlrey5jTySDYGEe8slT7ON_cdmaSF5gg13W0wdSabJavUXtwtb_nVvMcuEJo45eXID_l1jSvGvoF5cbwahtARlMih2FuAY7XZ8MysiVdTmzEUHLiawVWlwO4NGHQDK2zVjnNBL5BzCvor12ScembNbscZ7586mwXOl7M7yP2oXCA4cvCvE97YFQB8v28HlltDoYX99k9ayuQ7caYmA6I5cwvQxd_OLv59Ftr5jMC9J4RgVLHi5jlRJIVNSYKFz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e4e5fea.mp4?token=oajZYDyWEgKz8RSV0PQg9UqYu7xFkadb3leLw4c6NzxG7Ck794q1O1-OWBPLmZF0dGfuXAJAG2q8ySdR_PvTuuxlrey5jTySDYGEe8slT7ON_cdmaSF5gg13W0wdSabJavUXtwtb_nVvMcuEJo45eXID_l1jSvGvoF5cbwahtARlMih2FuAY7XZ8MysiVdTmzEUHLiawVWlwO4NGHQDK2zVjnNBL5BzCvor12ScembNbscZ7586mwXOl7M7yP2oXCA4cvCvE97YFQB8v28HlltDoYX99k9ayuQ7caYmA6I5cwvQxd_OLv59Ftr5jMC9J4RgVLHi5jlRJIVNSYKFz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇨🇴
کلمبیا شاید امسال تو زمین مدعی نباشه اما خارج از زمین با این خلایق خدا حتما مدعیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/93198" target="_blank">📅 15:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❌
🇮🇷
با صدای کمممممم گوش بدید. درگیری یک هموطن ایرانی با حامیان تیم‌ملی فوتبال در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/93197" target="_blank">📅 14:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv4KzhPLmO8VV4SJsP6mQXYYLHoPeFjnC8_VCjxSX70VFBlsDlSTpA1EQQ3O8AeT9x7X6wSj-QOIEtqv8h1Li_8KICsfpxRYKLJNZHpEtSMYSKa3Dd1Y_0oyx_ReMAh7Dsh167plfPwMhZzLNPuwz7cmCTxeHYK9VHSz8cmYb1_2uekHMBbUhRZ1yKga0q5NGir_2T3IiHi1wvZJEYt_3YHSX-ZgKCqEBmHg_3nCCROyuhF8R_zYhHCZL2LwlWZ004ALTJY3sjOmE6n4c1Xkc069HE4yrSe1xo3Ht9aRql2iuflnpgbjcLg8AREYcTU7Mdu2kciTJIMkQUb0n6CATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇹🇳
#فووووووری
؛ به نقل از منابع تونسی، صبری لموشی سرمربی تونس بعد باخت دیشب و سنگین مقابل سوئد از هدایت کشورش برای دو بازی آینده برکنار شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/93196" target="_blank">📅 14:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s6ed3tB9diy6Q-ME6r6-eI1DTcP_xN3yB_YpOrn4f_pe268ZBlm75n9Y9WUZNKP4PaajhY1dfzNr4n8qQAHbjwmdvt4R_xRrtpAmGTC4acsALvsih1Ofk6I1-moB0jShTEDAZG6tEGs-i_MulXKwsh22GCdkyRfoOcDBIqGzPo9SEtB6Qi0cyFcoGRS9aE-vkK4lz67hJXH4FJaln08gq4ygeFGjZ9J_WeFJ2YKdZ7XYugP4OEtbF2WY7iHD9Tz5dgoNGeZlttRttnYuY8LREQ9rFoXo2gZZue34ixfIJ9lRGEPQreLkmpgzM6ui1V2qI4FY9E6hrqyXeE5FoZ21BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اولین تصویر رسمی کوکوریا با پیراهن رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/93195" target="_blank">📅 14:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iq5TQgTrQCcigk6AKDY6La0P-T-nJDb0E_WxukpdQzpt9WPxnuu5fm9Q9cCgFHol8IQDSpUDghl_9Dlx-yLq3GI2ExelbXrNGldJl0UazrSPqQ56KjA6nEokxnBxzKYov-8JpebELwN3unbqCmpiJRSzTzMRAQO5yLd4_Q_c6grfp7egTQL9mrGFH22yC7GfMyYrXVR3RoMbyzetZDQVjmSRZKDMD-8Z2wAr2Frs9IbDk_Y_iKKWKLRJiTUQsxpaqyWQg0RpW5rbakGf9i5uMlLt_oW9VagTl873zV63_wsuxAXGhSxUe9hZ06blkDXWX-vrnhSKBT_X3daridrp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
🇫🇷
صحبت‌های کنایه‌آمیز رئیس‌جمهور سنگال پیش از بازی کشور مقابل فرانسه: فکر می‌کنم می‌توانیم بر دیگر نماینده آفریقا غلبه کنیم. هرچند نباید این تیم هم قاره‌ای را دست کم بگیریم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/93194" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQS9lnJCUxYv6b45EIfHWkDwglhQV_o2vX_Oy-j9ulnfW8EBm1lXl5n9OWrbzP8zw4lQaonUDBoVEJK0RL28nIb8S4Bx0e_bO2BK-Xb3vHXb7Ce9QMyHWxmhnR2kJhqAegtoBDWZE7y_OIiWJ6aQfblMk-OlI4vFC_sPTA-mH1yAF_ALzSRot4e7m0hvQtTLDXisfd6DVusgKUm74nKbEkJ6QtvGl3EHd3mTIxJIbh8a3HBTYiQzODAwi-4GXmyvf1YXFakOGBJ4_pJUi_8qIDfsX3ZEbERVQ-PgP_hLKFKamixb5WoqpUx2Lbcxm09RuDS4y8y034ENWeNLjTjVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
احساس پدرت بعد باخت تیم ملی کشورش چگونه خواهد بود؟
🚨
🇸🇪
یاسین العیاری ستاره تونس‌الاصل سوئد پس از بازی دیشب:
تو باید از خودش بپرسی، نه از من. (می‌خندد). بعد از زدن دو گل به تونس جشن نگرفتم، چون این کشور دوم من است و احساسات زیادی نسبت به آن دارم.
👏
❤️
🇹🇳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93193" target="_blank">📅 14:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a182bce704.mp4?token=VmBmQeis-gpo80mRC-4u_YDcVIEbPBYs4yZ3vY_llcGrfD7VMPQMBMGkx8UROvh_a9L1IG8oZcIWIc2IlQbQa4sdOX5gRhpkZ_bfgTB_8Kcvs4CbIkF2B7CYuAY6ZimRkfLUmocGTOXh3nI9STqV5FfaUGnnySEHeMMLkjPpS2hI7zgAofMYjt8zWor3xvHv5XWmuWmMqGLY40OIqe3R36z8LhWfGMT73trdxoDZ88t7Eu9u8tOTuxDkopFbhfCvsi9C6AQ3Ld_otmf9fQhN8F5H0QEpvaMedvNvDfKntCZ_vL7kM-UPKG1ubg3QRhejUR-WRty-RcxS_9CXLnx_dqLoxhSAM2ivZNWtaqRp6AbFOjDeeHpUi70XmeTxlTHvKIKHtqTvdmQrzqtncN52fXZ3ibvsDkM51_X-gpYXNu_oSpZEiIfOU-ZoKqpVo-YI7IOl6ea_y4Ga3Y08MVwTmSDP6gVYFhPCR0-8Dgn3h9dCRE5mKkpNrOHACZ1ZDDoqvVDCNawWLBdImUkQD4QkrqPrOo5bscTTjNft8wH4eFHU6AfWnXVFnRXexIdtl9E3Z_ABY1i1LDc6fB727EzF0udflCePzxcj5Hl0dx9xwPDUyLE68YE0hOuyiWb--4L-SZYnBOwyDoeYdAaT5rG4_MN4sjWFxJSIjP19vMbB4I4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a182bce704.mp4?token=VmBmQeis-gpo80mRC-4u_YDcVIEbPBYs4yZ3vY_llcGrfD7VMPQMBMGkx8UROvh_a9L1IG8oZcIWIc2IlQbQa4sdOX5gRhpkZ_bfgTB_8Kcvs4CbIkF2B7CYuAY6ZimRkfLUmocGTOXh3nI9STqV5FfaUGnnySEHeMMLkjPpS2hI7zgAofMYjt8zWor3xvHv5XWmuWmMqGLY40OIqe3R36z8LhWfGMT73trdxoDZ88t7Eu9u8tOTuxDkopFbhfCvsi9C6AQ3Ld_otmf9fQhN8F5H0QEpvaMedvNvDfKntCZ_vL7kM-UPKG1ubg3QRhejUR-WRty-RcxS_9CXLnx_dqLoxhSAM2ivZNWtaqRp6AbFOjDeeHpUi70XmeTxlTHvKIKHtqTvdmQrzqtncN52fXZ3ibvsDkM51_X-gpYXNu_oSpZEiIfOU-ZoKqpVo-YI7IOl6ea_y4Ga3Y08MVwTmSDP6gVYFhPCR0-8Dgn3h9dCRE5mKkpNrOHACZ1ZDDoqvVDCNawWLBdImUkQD4QkrqPrOo5bscTTjNft8wH4eFHU6AfWnXVFnRXexIdtl9E3Z_ABY1i1LDc6fB727EzF0udflCePzxcj5Hl0dx9xwPDUyLE68YE0hOuyiWb--4L-SZYnBOwyDoeYdAaT5rG4_MN4sjWFxJSIjP19vMbB4I4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
مصاحبه یک‌ هموطن ایرانی ساکن آمریکا که امشب میخواد به استادیوم بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/93192" target="_blank">📅 14:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93191">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🇪🇸
موندو: رئال‌مادرید یک مدافع، یک هافبک و یک مهاجم دیگه هم میخواد اما تاکید ژوزه مورینیو به جذب بازیکن خط دفاع هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/93191" target="_blank">📅 13:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93190">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442dbd917b.mp4?token=mnKLMR8Ng8rHtLpHSlsyWv9CX75FK4xFB_pU74GTNVs_RosuP46gxu3SB0y7Lu-jBFuxcCTk0PaIrYxYOFiOdeEMOmsinv2iFC1LD1vGZ3JWp3wpDuL5FLImU9wVb7iD15o06ztnNBZDfBKuawVSMpx95SskP8DpZSTHBN-HDmDHXVrEemiZ2kIHQ_Kgsvnazt0af2FQA2NptrStzgtq1wH-qD0EPoFjOjWCEWGY3UHIKIJF9vhEYPDM63XwyA7HiTw42HDCw9T-5Wtize29LIc39KRQFqPrvzpNerlqv5XtFRDMGPG0U4wV0AE7lIeiIkHr8YKjAbPt-aa0hfhhPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442dbd917b.mp4?token=mnKLMR8Ng8rHtLpHSlsyWv9CX75FK4xFB_pU74GTNVs_RosuP46gxu3SB0y7Lu-jBFuxcCTk0PaIrYxYOFiOdeEMOmsinv2iFC1LD1vGZ3JWp3wpDuL5FLImU9wVb7iD15o06ztnNBZDfBKuawVSMpx95SskP8DpZSTHBN-HDmDHXVrEemiZ2kIHQ_Kgsvnazt0af2FQA2NptrStzgtq1wH-qD0EPoFjOjWCEWGY3UHIKIJF9vhEYPDM63XwyA7HiTw42HDCw9T-5Wtize29LIc39KRQFqPrvzpNerlqv5XtFRDMGPG0U4wV0AE7lIeiIkHr8YKjAbPt-aa0hfhhPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از تفاوت مصاحبه انگلیسی رسول مجیدی مجری صداوسیما با فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/93190" target="_blank">📅 13:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93189">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppqin3JlfLyUJe45UkhXr1cmsAVfP19Fx_DTFAZhrSZABpV4ywNy2aOSLDUtdCu0jWRlaoiYZMe9ws0JjviHcjWiRwHtulGOodsVw7MCPva-18-dLfoo5hLDMrUCULUnrft6-hj813WRen5aqt7yS-WweX6UaEFrmeqX_d8u3Of5Crn-9oDh4mJvw8LJcuKIJyP_85DyMEBz6d8P5XF9A_XumfqPS_UZmsMbKW1lL3N_hhpnVpMO9f_X23-uDqAno5PlxTmhXpTYAI9MPhukXVdkSd3ukxTEQowZx4UK6wajY2dvBmakS4iv6K9zeKDJ5y9I7LhD1XgXmmGwkVFimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر چیزی امضا شه  مسعود باید کوشته شه  سطح قافیه
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/Futball180TV/93189" target="_blank">📅 13:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93188">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727341fe4c.mp4?token=XHgTmq2mv6Szgsd9jrPpx0--bDn3v5fPMRe9LQ0RbOjmQiSeUWWnFa9fpBEkMSCVDsp_uiUh3ddC9RkkZXEuM__Iu6OpmEp7q5ysKTdqQa3CKkIH6QbiecnBx_7I5WyIZBO1K2BW1l5VgQ-Y8rYzBrHFBsSNx_az76kklA1r4TFwZ1-Pk9lCzlJU9VnO2fbLy_y3_z5cBMI8UvtZefjBIQYYyDV7fO1K5sHVo9ndVRWHyNwd-Qw__7tFiZqCY3vuDczLbiuZ8erftRWlrDx66wJDLczLuss8LdLpV-Um6xgmAk5POq7nMf4aFbt8ExygTaQaHfpJQX6Ch-bYOxFP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727341fe4c.mp4?token=XHgTmq2mv6Szgsd9jrPpx0--bDn3v5fPMRe9LQ0RbOjmQiSeUWWnFa9fpBEkMSCVDsp_uiUh3ddC9RkkZXEuM__Iu6OpmEp7q5ysKTdqQa3CKkIH6QbiecnBx_7I5WyIZBO1K2BW1l5VgQ-Y8rYzBrHFBsSNx_az76kklA1r4TFwZ1-Pk9lCzlJU9VnO2fbLy_y3_z5cBMI8UvtZefjBIQYYyDV7fO1K5sHVo9ndVRWHyNwd-Qw__7tFiZqCY3vuDczLbiuZ8erftRWlrDx66wJDLczLuss8LdLpV-Um6xgmAk5POq7nMf4aFbt8ExygTaQaHfpJQX6Ch-bYOxFP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر چیزی امضا شه
مسعود باید کوشته شه
سطح قافیه
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/Futball180TV/93188" target="_blank">📅 13:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93187">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlmnpebsYkfNuefiNXULihuF_j9dBgBzO9BdNqAILGzUQJigc8965wCPo3s1AKLej2dEPM4atTciVgFqhI9eQ1PPlB9Xs6e1l7om9CFloPFwk_JoT1xn2Ji2pNKrTNeITCvuXOEmE0B9_JDwLXJgH2WE7Xip1O4Fi6-lkxKgNkuYu8Ly90C6MK883H1HXRgYDXsN6ioM9FiPjNTri1CIXu1Fv4WfsTVSdSrJJ7fpy88TKxGxh9YOPzAmDyJsiRWzmfvPTvjrlKTFRgbTJYDVE3AHFs8HUj9dpDY9wI2Bbye_nmq_gCgA05vdHvJ3PdIiz04owd4SX0-W9scwXL14TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی از ابولا پرتغال:
🔴
آموریم به عنوان سرمربی میلان انتخاب شد؛ قرارداد یک ساله با گزینه تمدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/93187" target="_blank">📅 13:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93186">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55757cfe39.mp4?token=a32-KblrSox7EwQ3w6ATBDgbNlYypz2NJoa5iYLB--wdgPH_VuoyAi7h_skP2j5DhqgijUd9eecLaOAW_yAWHlA3_CLNqAWd8Wq_BcJBPZ75XvV7DmusdQi4mU4ZhJuKglaOWt88WsB8ZMAyNgoh0LrdrxFooUUVhopu3uYvGUvf7ki1skEHN3ipjD3LRxh8FDVu65tY9ySPk_82nO4_ILNZ6JOmiBtMP5CrDJlteKuU8zhd2w1M-E4VfweDke-XCQvYol89jVtnLws0eB1VtwWHMEHPU_cTZy4xvlVETznvLdIjWht7FrqhcrfFO8mG5OXQS_Y5dMWDJaMRaChoPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55757cfe39.mp4?token=a32-KblrSox7EwQ3w6ATBDgbNlYypz2NJoa5iYLB--wdgPH_VuoyAi7h_skP2j5DhqgijUd9eecLaOAW_yAWHlA3_CLNqAWd8Wq_BcJBPZ75XvV7DmusdQi4mU4ZhJuKglaOWt88WsB8ZMAyNgoh0LrdrxFooUUVhopu3uYvGUvf7ki1skEHN3ipjD3LRxh8FDVu65tY9ySPk_82nO4_ILNZ6JOmiBtMP5CrDJlteKuU8zhd2w1M-E4VfweDke-XCQvYol89jVtnLws0eB1VtwWHMEHPU_cTZy4xvlVETznvLdIjWht7FrqhcrfFO8mG5OXQS_Y5dMWDJaMRaChoPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو کوتاه از درخشش ایرج‌دانایی‌فرد اسطوره فوتبال ایران در جام‌جهانی ۱۹۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/93186" target="_blank">📅 13:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93185">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhzZ0gtK-3uU4I1VS8VlFvAFRf5kpMdUqXc35eCHLoIbDF_2Z4Qks-1owi3TnRlU38BEtq8rlJoBj-3uxVU0u2WUkHGEblHZARr1natA-Q_IpVA0urNJHIOKp1J1kXJaOk2IZ5aZKs9K5EMMQk7D3A6nicKefYBO7D4bb8_JhihasBw-aHnZ0ODIL9cF_zfkcCtDKLxCS0HCVRlFhh6YvXH-kCFTQwiN1oq93STAEuHCqjSThM7z57grVSS0o87lIkCAohrUSu56ED4HIerTP2pUO5TqvVlb32A24syx8Z8uKUD56PYrhZDDZWDo8Gcf3yjvddxPFxtTlGTpvg3SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال مادرید الان 4 تا دفاع چپ داره:
1️⃣
الوارو کارراس
2️⃣
فران گارسیا
3️⃣
فرلاند مندی
4️⃣
مارک کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/93185" target="_blank">📅 13:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsI6jlFA37oOw3UjAXwj2LT4RWasuwtkD_-4o24KyDBh2JoR6_jass25dwcVFcXda_WCgBtJK3TCjSKqLnXT-0XNt8WxwLq7ZGnP6mbiR3DnA83-CiAcxAVLOq4oJDDYebJGJV0E3xIDCl0cljtBMYVRTPsJ0eFnXIOov5G40bGjI-OAIFnflHdMMz6-6nEtCiTqMpbqdXc1pTn_kKye7c_qLVRLUFgU94CQO1jrvGHEwheEp1dHnF0RifSu4Uycp-LAe5dI9hvR6KQrVrPTOZxXZXmV2vjwlvghQXp0LeDSdEPqDYLMpeL-IPze7hDAifbZXkXlY9vKKblvIXei6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از ابولا پرتغال:
🔴
آموریم به عنوان سرمربی میلان انتخاب شد؛ قرارداد یک ساله با گزینه تمدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/93183" target="_blank">📅 13:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🏆
‼️
ویدیو دیگر از عشق و علاقه مردم ایرانی ساکن آمریکا به تیم محبوب امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93182" target="_blank">📅 13:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd5gn0-6nZtdiVMIxxYlXesVNRmrEBqcdADZxwhHyyIJLho2_B1RexEXZkRaeHoDLvUKg9_YdiOepbpwNn_OuEeYtaL-CFiHJ8ZW1Rn-g-C6Z1KMLCgBW1k6zzAHj7mWqnYVUUiAFS7ZSLVrGMuhzKo3xoyjWs0PRgBocbNbgwocFZ5vdaHy-sl3nWRUHppA8Y5iSUfU4NW2kDemJ6W33yJ_M6dWlc8nQfhYuthno4WAMKEoSu-cpTlN41B-srQWitOk3pSVckAAJO6EC69pjcKfNUXk5ydjITbBgdAHrev3_ZNelQGW_Jh9meq_zONLMsCnzon4Wuw0HCJG-rvXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🇪🇸
پس از گذشت یک سال، رئال مادرید هر یک از آنها را تغییر داد:
آلونسو
⬅️
مورینیو
هویسن
⬅️
کوناته
آرنولد
⬅️
دومفریس
ماستانتانو
⬅️
برناردو سیلوا
کارراس
⬅️
کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93181" target="_blank">📅 12:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125bd5997d.mp4?token=BijnVul4Fk7JwGFTGHzMxze8lK0iSQvKRC42YPbw5tNcsI-5hmfhs1r1T-0epvnZfifsFBjskGgw9gX8CmBkFgLocOWXcn7jDMl2ZmgYTo61UenUkLflJovu7IBnD3ymmgEi2e-cuHWU42_AV2uzOkUWcP_KC55TDAfPbArhOav4CFV91a8-la6gDWPKPxiMEFBfEcI3akeMU8yfqPELgXQIa7eYTIJDR95d0MUh3l3QpNdac5FWYcjdq83dWlpiu_6D-qE3ZjsBh1MsrczcSCWj2XIa-mDUGSq5u-oFpFRpv6VuXcXPTk5pL6szx5nSdxe7atWwCmqkUL79SNDK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125bd5997d.mp4?token=BijnVul4Fk7JwGFTGHzMxze8lK0iSQvKRC42YPbw5tNcsI-5hmfhs1r1T-0epvnZfifsFBjskGgw9gX8CmBkFgLocOWXcn7jDMl2ZmgYTo61UenUkLflJovu7IBnD3ymmgEi2e-cuHWU42_AV2uzOkUWcP_KC55TDAfPbArhOav4CFV91a8-la6gDWPKPxiMEFBfEcI3akeMU8yfqPELgXQIa7eYTIJDR95d0MUh3l3QpNdac5FWYcjdq83dWlpiu_6D-qE3ZjsBh1MsrczcSCWj2XIa-mDUGSq5u-oFpFRpv6VuXcXPTk5pL6szx5nSdxe7atWwCmqkUL79SNDK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
مستر هپی توی کنسرت افتتاحیه جام جهانی ؛ صداشو کم کنید نره درتون
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93179" target="_blank">📅 12:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG2lXru7ZSnVqYyXkUsApK_j3h9LpMdofRtiOCBCgN1u8Hnx8x7SriVFUTG8tRUo7FQu-0UqkOadhZ5UUckkQxCUqpJigzoCl0w3i0YgnPB_DxcAJbHfek_ArnMyAVURMXJKOqu5NtFFTS5cBdeP47Tf_F7tCtDcmM2V1vrjtMfvSk5a9gATWDI4_XrWJXJtbDR9IZHpMbJk_SMEMz4-eFXESRMcJbjN5t0B6JFSWlnYB-ij0_HQggpD9GGpc_SD-S7xu0RB5i9tNg7DowoAhhcBWCI9vhbRtO76VhwUT_02tyV9aXjHZDOXR9wqQfcS3VoU3L8MXHw0lYe4a6eEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
؛ رومانو: اسماعیل سایباری ستاره آیندهوون با رقم ۵۵ میلیون یورو به بایرن پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/93178" target="_blank">📅 12:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3faddfb96e.mp4?token=jRbgNnVYBw3ANkl6CZ5Mg_9X1jSCMQ8doPslckEs8nZiv4v6lxy5rOJgWB8hGXyT0Xthnb2YvF1oZ9XJ4TZSZhNoN3QiYSu8Ehsi6ZgOA9X5a5uk52YQ3D9leL-gpu3iLkmafRAREgL34PE6RAN866MlbQ6TRP90UFaurHbklPdawxzZkU4wSlifJbDk6AlEiDqka69hcZ6kcPDnjgujHTtBKodXdDkmfNyaRnCyrIyoAStjkz2k_0ooT0moFz6NLZwxAkSkmnqAqZOoSzk2wrXNAaJfE_XH5byLwJriwQhByNkfbzBf6FUBx1NaHYL_6fDnoCGf2GzXfAxVANaZfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3faddfb96e.mp4?token=jRbgNnVYBw3ANkl6CZ5Mg_9X1jSCMQ8doPslckEs8nZiv4v6lxy5rOJgWB8hGXyT0Xthnb2YvF1oZ9XJ4TZSZhNoN3QiYSu8Ehsi6ZgOA9X5a5uk52YQ3D9leL-gpu3iLkmafRAREgL34PE6RAN866MlbQ6TRP90UFaurHbklPdawxzZkU4wSlifJbDk6AlEiDqka69hcZ6kcPDnjgujHTtBKodXdDkmfNyaRnCyrIyoAStjkz2k_0ooT0moFz6NLZwxAkSkmnqAqZOoSzk2wrXNAaJfE_XH5byLwJriwQhByNkfbzBf6FUBx1NaHYL_6fDnoCGf2GzXfAxVANaZfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
تعصب ابوطالب و سیانکی روی شاه عبدالعظیم؛ ابوطالب به سیانکی خاک شابدوالعظیم هدیه داد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/93177" target="_blank">📅 12:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72816eebee.mp4?token=X7R027HGiNWZko7b7kc3UPy8NGD96-PAv5akUF8vWkPPXNgv9WMWAUC1yW5IrA1fqs96jFIb_GVU_ytEvdL-Bmsmn0fBvMlobDaOEvsy0ajGA-66tKewXJzyH1YlsRqVZ5m58ngSIZohhOhmjl29xSUsdHDkcoS8_gb6ILEl1vndfGOIozh0tw7u5DcYERYFqxQhy7aJUyrkbW5Xm6PFr3193Q9YFuVFwyr0lsMsijQ2In_RV0717e3OrfjeeVfNpsnVdzHMAH8K7n8ajFy82kMIcMSmeXM0Jyezeb1o5I3SHjbdCVa3wQeOxs3P_w8c1_MnMsn31l5rXOSXaEvoxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72816eebee.mp4?token=X7R027HGiNWZko7b7kc3UPy8NGD96-PAv5akUF8vWkPPXNgv9WMWAUC1yW5IrA1fqs96jFIb_GVU_ytEvdL-Bmsmn0fBvMlobDaOEvsy0ajGA-66tKewXJzyH1YlsRqVZ5m58ngSIZohhOhmjl29xSUsdHDkcoS8_gb6ILEl1vndfGOIozh0tw7u5DcYERYFqxQhy7aJUyrkbW5Xm6PFr3193Q9YFuVFwyr0lsMsijQ2In_RV0717e3OrfjeeVfNpsnVdzHMAH8K7n8ajFy82kMIcMSmeXM0Jyezeb1o5I3SHjbdCVa3wQeOxs3P_w8c1_MnMsn31l5rXOSXaEvoxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
کیم جونگ اون در جام‌جهانی طرفدار مسیه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/93176" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/93175" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93174">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoK1W1SodL-drvPy5r_eqtxFJNtIkNT7HdbWs1BG5TQdB3cd4IxCrj3FASqm-8oOTap7gQ7MZeptr6E8AUrrnMAck6qrKu5FzgzsdFACfwD1gHtKP5TduLIJC46D0W33K7ZxyrbfnvbOCkcvg0nMPNf9T3EhJYw6SVU_4se1mJLANYSWXBo4DdsEOVXmBESJ8wCt4P97C2PrV9K316pgu_UcsesPwAIvUazifytoLLKKE6NEsRQGprmNE_H5x5oom9un1-HEeAhslwrfpKm4S9uw15IoDb_7VjTPS-ysjt0DObIACr3w38RB9Lr9sFEw6tO1UfOlPLE3hQBF4BhzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93174" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8fAHTs-HSRHdXQPOC31hc_7Z6lFIYqsxXGNPtmSLEojep9ZdbAhopnaAUZbNPqbRrOW9CwsqOGam2UWy7ESh1PozKM3k2dizASAiLesr7fBDlNbIvG9f0y9o6ixgDiXXIbDWXMlxPgQoPAP80hQlBXti5Gz3Up_ZvEzox8U38aCXbzwnFmsGdw_EGsSq7sD5dF3b6W0yAnR7o0bua1mlnGciXb6gdaBR7LBqduUHYK8pDJTAQfIYfstLJjKer8E2Xaf4CA4cWduWFQdE350Lzg7g0j8eSxk-79F1ookvSmtZABDE3IIIKrk07oDRiVOSn1jG9VgVgNMU2d6cjvyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مارک کوکوریا رسما تا سال 2032 به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93173" target="_blank">📅 12:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imDySN9EfquOpVNhZu6SUVDFlT7z1STs0r8tmJgXZ8FhAUldRmQMUjhxyY0BhqnD-ywhLzoKR-h0Vwhsaq8AhnE8oNQQkXwzdyVR7Z-JPTjG_JG2uZSSt3J7Y96j7lfX33nXjqc8A04GPTVag24otEYU0q-OLN4FGGAwmtIUCi2NoAwBBIAD2Tk2ba-N5__G5O0tAuRcghyOD6sAJqiQln_wqqScWpDiekZV7GBgjlMOa7nmLKhht03j4gMMXrh7X3UH151RdUJA1a5QKm092SnxxTdql4tJXg5M9GNjVR25lANtUuSM0z4R8T9LGJQF5ZDAjQwrqVZ0V2ZAoT_0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بازمانده از آلمان ترسناک 2014.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93172" target="_blank">📅 12:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b56f4be0f7.mp4?token=EVdMcQ9xki_ACthrf5S29aICoKumvfWKrjvNHVCmruwYPVskEFSSmewsHwNCJwK7pXwilob3U1TEzCEDVjQS7hI3_UQiyJhN2qqU0rZUktxvdg2l3t_HQOAyMbeJ77Lzgx4xlSDIsGf7pPW9NcxjPYUsRsBQ9QTIIZHrkV_lcBF__EliaBDpvmFBqAELgys6OqPH2u7MrZqEfAMyuBjDXjNaOzpY139MxDMG8YLVkK9TrV30tCpn5N27t2L3Sp25as1SAu2xCMDJdUqUZRZi9VM6Poi-gcRH3tBxtnixTSVCVBGqNE8VFtbQS8mO7kByw7F89CV3dGBoXkdjbZHnaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b56f4be0f7.mp4?token=EVdMcQ9xki_ACthrf5S29aICoKumvfWKrjvNHVCmruwYPVskEFSSmewsHwNCJwK7pXwilob3U1TEzCEDVjQS7hI3_UQiyJhN2qqU0rZUktxvdg2l3t_HQOAyMbeJ77Lzgx4xlSDIsGf7pPW9NcxjPYUsRsBQ9QTIIZHrkV_lcBF__EliaBDpvmFBqAELgys6OqPH2u7MrZqEfAMyuBjDXjNaOzpY139MxDMG8YLVkK9TrV30tCpn5N27t2L3Sp25as1SAu2xCMDJdUqUZRZi9VM6Poi-gcRH3tBxtnixTSVCVBGqNE8VFtbQS8mO7kByw7F89CV3dGBoXkdjbZHnaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردم ایران رد دادن. این چه کاریه ناموسا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/93170" target="_blank">📅 12:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pai6H5FhA3dycizCtYpi3A9xp1kn-o_fphMBgMbMML0cplwwTC-EU8eQfzz--q_H5IoBCoIKueHMBi-uP9hFZ3WeSONU7P9XbZyH1jiI_PqgAY6t_d45B2Q7RdpPFQF-zkC5jAAqPBMMvJxPKg9VeFw5552nnOXJFH0NQCMgbKBJJSBmJ8EHGDMzvpmcGdobyQGcE55l4bO7swnELcyuiTS6XpWYnmHWQy5hfuAqgSiXqUcmOcgL6MTdUw8ocSqj_9P0MYv-jVWyPDm9lnCrFO7Zu1e_5nR4TjfXXq7ZCnNlNVZi6OTiDTNCQWKX49AKJxHZQzOqf77QiGJ9vUCiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇸🇪
| ویکتور گیوکرش با تیم ملی سوئد:
⚽️
•  34 بازی
⚽️
•  21 گل
🔴
•  7 پاس گل
⚽️
• 28 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93169" target="_blank">📅 12:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2801ce72e0.mp4?token=SMfse9WsvJdmbS0p6lUVL4E8vZrHxOKdEd0G-bN-dL8h_JNEKGnKslFB9oq2ToJylilrfQhG6fY4rOXjKMxldWexOsQhzTVfXtBD8RMRjBj4ENenmjXt6M2sF9tda8GSIct6pso8bCkFMy0b88a2kX7mOFJ-8Yuj76L4DlBz0FGBUf52BLkAHZYQoXkXhhBCtqdtlZmiIj5uv_Ta-iZ3QpBdHKm5iDJITz1mF5N_75Jm-bAk0rWWNeBhrArHB6HIzlYdH5MPkwlHIsUBalp0q61gYClb8zZEZC6dxAxNCGqHiWPrs4Dq8O9mXYD5aDC9ORkBiSXiso24-ISgAicCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2801ce72e0.mp4?token=SMfse9WsvJdmbS0p6lUVL4E8vZrHxOKdEd0G-bN-dL8h_JNEKGnKslFB9oq2ToJylilrfQhG6fY4rOXjKMxldWexOsQhzTVfXtBD8RMRjBj4ENenmjXt6M2sF9tda8GSIct6pso8bCkFMy0b88a2kX7mOFJ-8Yuj76L4DlBz0FGBUf52BLkAHZYQoXkXhhBCtqdtlZmiIj5uv_Ta-iZ3QpBdHKm5iDJITz1mF5N_75Jm-bAk0rWWNeBhrArHB6HIzlYdH5MPkwlHIsUBalp0q61gYClb8zZEZC6dxAxNCGqHiWPrs4Dq8O9mXYD5aDC9ORkBiSXiso24-ISgAicCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
👀
#دانستی_کصشر
؛ عجیب اما واقعی: اگر ۷ میلیون لیتر آبجوی خوشمزه آلمانی که هر سال در جشن اکتبرفست مصرف می‌شود را بگیرید، می‌توانستید آن را به طور یکنواخت با عمق کمتر از یک میلی‌متر در هر اینچ از کل ۱۷۱ مایل مربع زیبای جزیره کوراسائو  پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93168" target="_blank">📅 12:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qXuPGMb-_zXBrW5v8FXgEOz3mW7jxNtTvMdC0-0tC1zSi5Op8Sy9Gd3JguiHfcFuI4Her1xrpd424IDFAlNcegJhYhiWpkODZg1AKKuJEcTf-CMDguWQaskkV_SBkIJrNuYvXDFu0QDiXwwMA7FkrB8jw1LIFn9g0q7zft6xZT9W719IbgugodEVlqB6t32Gf8iwEqL22wj-MhBym_LyrfKpM4rLJYNvRqwnvsgagkrFp44UkEtop4SX-QwqP9ZaqwmAOnYut9vnA2eXdgp-ZXSpWhwn3vsCUa3JnAx6kRmDpzFp3w7omX8e2D6dbf62pjVeUXX2wPDJrTu50pxitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کوریره دلو‌ اسپورت
: اینتر با رئال تماس گرفته تا درباره خرید کاماوینگا پرس‌وجو کنه اما پرز‌ در همون ساعات اول پیشنهاد‌رو رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93167" target="_blank">📅 11:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P7MzgJK7o9Rhrh-Mzi4bAP7yTMeJOQa2ngrJoIJ9vzJMJQ_iFXCbvdRcPN1KfpVPUhkFt8NRfRNt44y5pyS_0E6OZW4wu01S2qIlEroJFkslcCllXWAadj2l_w4mH1EYU0cVN2-TnchYger9beoB-nQtYJ97faUB9ADrNsG_5Op9a-VoSYkgn3DIYLicK5iZL4BLfdCYTqZhFk6r4l4cp7zOkq2moo7JuvO1cUg1DXLwCp_NrE_Wg-O2Utkm9N_YVADWIY6N6juWeHeET3lvnJl_E4VsHvi_m6sJT5S8n1agBaZzD9EXOeJHxSaGYdXPBpAsvxChFZJPq2GXE1nGMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇫🇷
امباپه: در آینده برنامه‌ای برای حضور در ریاست‌جمهوری ندارم چون فکر میکنم بین مردم فرانسه منفورم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/93166" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇪🇸
پس از شکست در جذب کوکوریا، ظاهرا اتلتیکومادرید تصمیم گرفته که با گریمالدو مدافع بایرلورکوزن قرارداد امضا کند. گریمالدو پیش از این اعلام کرده بود که طرفدار بارسلوناست و اگه پیشنهادی به دستش برسه قبول میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/93165" target="_blank">📅 11:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060d49d1f9.mp4?token=nm62Ps43fSsGr3VCqKpHbgvXJWKxcpD8w2S3wySmeEskHmfuGBKkWugXUspKF94dGQRjt_FuRmxxgxCkaBRSU9VOz3yT582-3p03QXjWGsbRzlTAvb7I_jZfOzqaAfto8kxuji0gLkF4AlHS3GT6kN2ihfnSNuSjl8ln4kHgoR4Kv2K0qvjLNlA5mtuqd5xOgDzEW9-fS2lkfbVCEg7WnVW77ojiEJWcxcgHvF7HQSvYQ2S_s3IQuQ9VSZGAaKAfq6QNQHHVcPOFAkMBlzSIHxGS1i8wTamOkqYTEQNlFrZNrHBeNCBSRh7ojVkQrf4mENEM1kE9LNwz6SCOycVrby1Tx-aVPNtEXOP1qlATFKgG-ROgGg8rlJBP2qGVVTmo-b83IrcOAU-3YyVMAzzhK_5iLdU5zr5Tj3UDzARjHZ38lyUnIbg7SptUC5V_42bn_xWGXl7I6TvLLnt81oSBe6drRO1k5aI67pyRR5615HGIeMfYGtmCgU89ywNCv4s1Ppcd690V9f0PTcxE9iVZsFWGTHFvRmMvyPEmBaKyl1t5n0FlXhaZsZibcKPc-mntVT1C2XNgmKyYRxEWC3gDHhstzagF0vqzkhWWv6h2D0wcDN0WMZfzrHuhjiFuToyPHWbcy3axG857najB1hVdHFcEO9SRLDWq4WwPqfWn_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060d49d1f9.mp4?token=nm62Ps43fSsGr3VCqKpHbgvXJWKxcpD8w2S3wySmeEskHmfuGBKkWugXUspKF94dGQRjt_FuRmxxgxCkaBRSU9VOz3yT582-3p03QXjWGsbRzlTAvb7I_jZfOzqaAfto8kxuji0gLkF4AlHS3GT6kN2ihfnSNuSjl8ln4kHgoR4Kv2K0qvjLNlA5mtuqd5xOgDzEW9-fS2lkfbVCEg7WnVW77ojiEJWcxcgHvF7HQSvYQ2S_s3IQuQ9VSZGAaKAfq6QNQHHVcPOFAkMBlzSIHxGS1i8wTamOkqYTEQNlFrZNrHBeNCBSRh7ojVkQrf4mENEM1kE9LNwz6SCOycVrby1Tx-aVPNtEXOP1qlATFKgG-ROgGg8rlJBP2qGVVTmo-b83IrcOAU-3YyVMAzzhK_5iLdU5zr5Tj3UDzARjHZ38lyUnIbg7SptUC5V_42bn_xWGXl7I6TvLLnt81oSBe6drRO1k5aI67pyRR5615HGIeMfYGtmCgU89ywNCv4s1Ppcd690V9f0PTcxE9iVZsFWGTHFvRmMvyPEmBaKyl1t5n0FlXhaZsZibcKPc-mntVT1C2XNgmKyYRxEWC3gDHhstzagF0vqzkhWWv6h2D0wcDN0WMZfzrHuhjiFuToyPHWbcy3axG857najB1hVdHFcEO9SRLDWq4WwPqfWn_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
‼️
ایرانیا تو لس‌آنجلس یه خط تولید پرچم شیر و خورشید با تیشرت راه انداختن و قراره امشب با جمعیت خیلی زیادی راهی استادیوم بشن. خلاصه که شب جنجالی در پیش داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/93164" target="_blank">📅 11:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1tz6SG1l5I8SjmyiZ7t_7s9T90efqTzY5eS2e0hn7SKIxh7t7jnxfj_zleyvOSHCNfzMEEii5XTdByKA7klhfKKmTjdpurtzygVhs3aDAhxzf0LBso8ymi4YU5CyZAisCvBh4ta_KsJCePLYxUxBTQaNWa0rYjGfcfxq4yKPE1F8JLs7CesW-38I-pYJTasNQazKZRdyPzX-_yizlpaDP6kywjzWFq-vcRhiDYO4itXFaz_k27yN4731EArBYzxQqgL18m1lQ1J60D1iPeia6LMjs0xGE_Jjz9byrqRLjxui3cAhA6KAugNjbeaKpPrRsItVIMqb8p1YF0fdaI9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🏆
🇯🇵
ژاپنی‌های با فرهنگ اینجوری اشغال‌هارو بعد بازی از روی سکوها جمع‌آوری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/93163" target="_blank">📅 11:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93161">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULfAY4lVKZc1xFwsjGrwbtbn07GBMcIxzMuNtE2R1Fdt-aHWBBuJEj7NgtKsk9_c4dZAAn2KfhruzEURCEwlH2vFCHeEZfthKoWljASp9Vq5sLG2jaMW7635Ejv-aBAkxLgS8V06Q1A7QBUrp9ebL_2PkAiMl6-OZS4lMZ6xG_Kqe-IGFgtVI9CHnciZrVk3QpmAwYs1JkN9GZ9eNc_waL69ev7Kab0b3boUtnVUkal6GCXLAe1HQUZXDhOSk6vAfpfrUJfX4dtUTr6ij_m_6g2GFHdF36eU6qerC_7Ohv3ThVwfQfnenAHOyp6FKbBhYLwzc9AVnVnKMXpGe2DWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
🇵🇹
هشت سال پیش در چنین روزی، کریستیانو رونالدو یکی از بهترین بازی‌هاش رو برای پرتغال انجام داد و تو بازی با اسپانیا در جام جهانی ۲۰۱۸ هتریک کرد. اون طرف دیگو کاستا هم حسابی درخشید و آخرش این بازی جذاب با نتیجه ۳-۳ تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/93161" target="_blank">📅 10:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
🇲🇦
ریدمممممم ینی؛ تو اردوی تیم‌ملی مراکش یه شعبده‌باز آوردن سر میز ناهار که با ورق نمایش انجام بده بعد یهو یه مار ازش میسازه که اشرف حکیمی میرینههههههه به خودش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/93160" target="_blank">📅 10:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6c107b207.mp4?token=v1cwtB9MXhoY91IfbqzNa7e9nIyF84xiZrXoSl3vf7eS--mhbkgXtlmI9klwUlbVu2FRMtPAeSlXlqmJd34ixmSNnHrgd6eOfzCyDUvYoriiybZchp8spbqN2jrtMiwL6E-vkKca5ZMtCcGxjWhk73nPsb4NFOH2BFvXNmS-HcT0h-4b0qbCsPP_-cS9AF4iicjQehJ_29uZ0C5MWuAGWgzc19yXIJlRGCOo-_7agGhco5KFEhUD1ZL3BXi_fx8CEb3YBGdXhsc89-UwFDU-BSaEi-Gs9y-PTulFv2mQfundQmOMwo-tGQ8fbLnHblEbZFklaJJJ7BXJth7nhakeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6c107b207.mp4?token=v1cwtB9MXhoY91IfbqzNa7e9nIyF84xiZrXoSl3vf7eS--mhbkgXtlmI9klwUlbVu2FRMtPAeSlXlqmJd34ixmSNnHrgd6eOfzCyDUvYoriiybZchp8spbqN2jrtMiwL6E-vkKca5ZMtCcGxjWhk73nPsb4NFOH2BFvXNmS-HcT0h-4b0qbCsPP_-cS9AF4iicjQehJ_29uZ0C5MWuAGWgzc19yXIJlRGCOo-_7agGhco5KFEhUD1ZL3BXi_fx8CEb3YBGdXhsc89-UwFDU-BSaEi-Gs9y-PTulFv2mQfundQmOMwo-tGQ8fbLnHblEbZFklaJJJ7BXJth7nhakeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇭🇹
تظاهرات گسترده ایرانیان مقیم آمریکا مقابل هتل محل اقامت تیم‌ قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93159" target="_blank">📅 10:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93158">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9debed864b.mp4?token=AJn79x9TejxhvrI-N_GsFKbsuhOx1k5WQteH7CJwJ5J-rjWENURWmuUpvjfW4yDj09NHJ3TcbXW-a2AeIF-dlSbCeWoFnctC0qjhYG3eqgkwoWrBVSNMpI9G3icU-xCe4dUM23hFk9ahk42TYhjtyamjHj9_XscGGALfkBf33cBiRpLXPow-MaB9ccHivKyEjpMb52L1y43Hv8Ke9v8F__txo6LSoNmDJ3uCqOC8Ogg5afULCXCYex04Zkxpe3OpyiWkwzXVgXjJSEyFtpnI53cCBGmxhlPoPIc8-XtfEpZmKwHXX_86m0QxrHS1X7gXxBk-DDhJrCNtegOZR8qq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9debed864b.mp4?token=AJn79x9TejxhvrI-N_GsFKbsuhOx1k5WQteH7CJwJ5J-rjWENURWmuUpvjfW4yDj09NHJ3TcbXW-a2AeIF-dlSbCeWoFnctC0qjhYG3eqgkwoWrBVSNMpI9G3icU-xCe4dUM23hFk9ahk42TYhjtyamjHj9_XscGGALfkBf33cBiRpLXPow-MaB9ccHivKyEjpMb52L1y43Hv8Ke9v8F__txo6LSoNmDJ3uCqOC8Ogg5afULCXCYex04Zkxpe3OpyiWkwzXVgXjJSEyFtpnI53cCBGmxhlPoPIc8-XtfEpZmKwHXX_86m0QxrHS1X7gXxBk-DDhJrCNtegOZR8qq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تو ویژه برنامه آپارات برای جام‌جهانی یه مجری خانم آوردن برا اجرا که به اشرف حکیمی میگه حشمت حکیمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/93158" target="_blank">📅 10:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93157">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b27bfe16.mp4?token=dXQjAUCDAmWOqFkA0oEWkp-7wtlbKXuLnaFinFiz9yG606GiI-dK3cyxhWRHuwWSvemJ_2l1PQd4BbB4lk8Dgl-9Y8YAr_T-7nRmmSzh0SQEmxvrCZIn4HXAK1cYYgqge9PIK5h_B3wWGmXPs4OLXTbg0XalYWpJ503SLfBEG6s7WZEMrX3cqequOj9SAZjEIqbFLSRv2B64v2C-XJlpLElzRfSwwjzeRDCxk6ZN7rfh4Peh_Wiz6hwxJrrN4ECTot_anU-YlCybNSRXTGOobVRoDSyAL-FlL-T3Rfd-RhoL9kY0xrhXEKo2YZ7QpYXMjkVhAhLd8ih0d_Yjq67Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b27bfe16.mp4?token=dXQjAUCDAmWOqFkA0oEWkp-7wtlbKXuLnaFinFiz9yG606GiI-dK3cyxhWRHuwWSvemJ_2l1PQd4BbB4lk8Dgl-9Y8YAr_T-7nRmmSzh0SQEmxvrCZIn4HXAK1cYYgqge9PIK5h_B3wWGmXPs4OLXTbg0XalYWpJ503SLfBEG6s7WZEMrX3cqequOj9SAZjEIqbFLSRv2B64v2C-XJlpLElzRfSwwjzeRDCxk6ZN7rfh4Peh_Wiz6hwxJrrN4ECTot_anU-YlCybNSRXTGOobVRoDSyAL-FlL-T3Rfd-RhoL9kY0xrhXEKo2YZ7QpYXMjkVhAhLd8ih0d_Yjq67Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی: هرچی سکس و ... داشتم تا الان کاملا اسلامی و قانونی بوده
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/93157" target="_blank">📅 10:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93156">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iejPUf2iJIy_07FC2Eho6dEvVeB--4NEdvoh3TQqtBwTDKNKIJAkh4CnhbzdXNThnNSF-xU6tmo3kz0UGA2nbyv3JMvkeqoaL_GClobVZj5RxGsflGyz3S3LxLFDTFj4BRR4r0xJmmuY_qypKhKF7nXA0q41wrfeLDAJKby11v1CIPeSsOHzYUTybeJpxbrLGKMkiF2q8LjHWq1VWwhXjbTgNs8hhMA77X_yCqO2Z0VxWTc9Ao4VrqUBqiU9mPHCDAzq7hzTyfKb5naq7kNbjNJPOA8iDAI5VYGKOHeHu4ZaZkCocnFblwGjw4m5kg7hsb-P_mRDXS131dwF_ugcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پرتماشاگرترین بازی‌های فعلی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93156" target="_blank">📅 10:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93155">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🏆
▶️
به‌بهانه ثبت اولین‌ گل‌بخودی در جام‌جهانی؛ مروری بر گل‌بخودی‌های خاطره‌انگیز تاریخ مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/93155" target="_blank">📅 09:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm7cMyBamrLIfIEuuZ7Xk3uaNSz9BsnSn_qSWo8btdiBWySGSYWvctVAi9tVp5alrtlP4iYx50J_J29ts3FpbYiWWj6CmLm5A1kLwyc-u6_SvGmv6pdSTB8adzPi88U7BHk-sapquW0aMvlTaJr2VzAmSPVnRv6xgrZngT58e1D6a2l3QyHduNmBD3KZQ5aIrOLBJ5x-9mBgOCz_qxbzbzp0EH_v9BzpC6uUF4IXnZIii8DhZIo-hIXl1m1jX5WiTmkLM5BYMCamCM7qnLsBdfHvYBZYktQlgXnbmIgWr1wEmpP1hUYnUnT8mt0LEeJZiDrzhXV-ILKgxL6Fdbx93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPsQW7cb-rrbTKosufirN4cvrAHEx6g5rK7K23mMhgRd-GPyefBN0OkBJTyZY1VPReS_KaboUTKMMYaJl8Am--G1Z6DN54eJBHrFYIzprckaVTBBju_2FzXX5x8snxKZcjwiZ30kToFGp_rb6Vfm2XZJgPji2oonx-FCqGhAwbnnD3Hgw5v1-lKjhk_S318Q9UDYhIw_VdLldVPdLYyuV2cxclR1j_oovOPuT6VVlX6CiM5LtptStJIQLtf6bnV7OVCTNQaNfEJA7d56isWrRofhVnUdnBvCKNqhzfLMJ1_OdQ4S15QSBYvUAclSRHNsKLn3Gqn212zVW3-ieCHIMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
وضعیت اینستاگرام بوادی قبل و بعد از بازی با برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93153" target="_blank">📅 09:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24856ea49c.mp4?token=b-iHBaGMyDPfomXY4_qWR9DKFso6l6H40oN9aIZdOH5Kc0u4JrR9WTYpSUTRBru77f5n7TCoSOg_dEZCp9DtPpZsxyKhnTozpy7KwPUqVVySuw_Qfk4sZoxRyTlebj0m-7AkcjGdQcfyDpnZZq5b9IaBmaGLzwR03y5-WFSHBSPAsiSBk-WrE0O3BOddMUCSKHIzOnDNwzx_vH-yJQZHBsP4H69E2vSA7_s4dAm1vKI7eZvZNfnFTE1iisMsNNVh42lK_gkwoRI7RZACgBXIKP6guKwLNs88Nm9csGunrluIWpo9w6hln_QlRoMRkcGwTzmsgcjvYKvpOgifxExlfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24856ea49c.mp4?token=b-iHBaGMyDPfomXY4_qWR9DKFso6l6H40oN9aIZdOH5Kc0u4JrR9WTYpSUTRBru77f5n7TCoSOg_dEZCp9DtPpZsxyKhnTozpy7KwPUqVVySuw_Qfk4sZoxRyTlebj0m-7AkcjGdQcfyDpnZZq5b9IaBmaGLzwR03y5-WFSHBSPAsiSBk-WrE0O3BOddMUCSKHIzOnDNwzx_vH-yJQZHBsP4H69E2vSA7_s4dAm1vKI7eZvZNfnFTE1iisMsNNVh42lK_gkwoRI7RZACgBXIKP6guKwLNs88Nm9csGunrluIWpo9w6hln_QlRoMRkcGwTzmsgcjvYKvpOgifxExlfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇧🇷
هوادار برزیلی که این‌شکلی خودشو برای استادیوم رفتن آماده کرد و تیپ‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93152" target="_blank">📅 09:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93148">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQrktAYCBsewIh8F5OLflfcsjSZdWVOOngMA2i4t-dIQBAYT-_xfRn22JugHamcgQjA4d3RhHzZGoqCXAETbVV6pVaMLb1nfYcGv07vwULULP1L9s8KAVaTPBBtgZr-2a47GNjQg_maifa7cTycHlM6Ed5cYu7NaegX8j_d8ekmsu6-92WRl7LalDYnU0vUMGiiYX0QrbZsgedD7SInqubhibNnb-UDZztfvnj3IfIZkYK3R1vuu00fSehXZujPrJT5qKRNpSSIz7tfHrZdgaOhFR-GOh6JS9oILnV_5aKP9Zh_euvr4_ueSeuxXm-RzoBZJQMPRMna9bFVe52VvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGRoPgaHX4n60iqatMQQg95d-RSNsqi0hR6swGElwLjshEz03AGeE5UqICz5f3kGYmvJSq4XV4nlK1a3dqmxKyNG-p4WEn8z1mvTjzY8jDIvNWYkOkuTa-t6wEMrmHq9g-ETM89ojlZ1nlxu8kn50qnlXqagSxeLJe0WxjYpjBbelsHlF3yonhz3W0HWicT7Bv6IqRhTo9oMJwdhyjUSdYgT1TcH5_fLibMDHrrwp-Sg_YNhxR2TLgTTS9SAw9Lk9C-4Hc9aH-MpQScmZ8esA2tgCDx4IQ3SFafHf4nnW5sirEqMio5sZRI9FTtdGs2TIdMqwBK2UBL5_dhmfoPqBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsMTFRHrFjau63HAZbO2TZw6QcBJIWycJdMIe67_9JTjWV0MYKJWhE7LAtk-HjhqBjik7AFznA3Akn6cDyr--RB8mJkUtEQGtWeVNDpjtRkQVOEWG9V_FRnez30bC-uitkQNr0RHGevqiA1tbJeBvLmcLvKCAC9E7gG9zOpqgA3Ii3i_lpV3eq_IIJnJ9Ds1DlRGEPDSH5anUSmujHN8rolJ7mSNjR9CfrlbqvJ1CXiPA7avm3UZz8Jh8V37Jub1n-owHjGU7Sp9dWa-jSpm1GbF46A0I6_y_NZI3jS4aJv_bxJ58ll-AhOTdXSSiOLnSptWNDp8-kRf8CjfvuMaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPG52uczyxGPRLNzSpEDQ43bllkUDf1tk3IaIcVD156O7HY1C-w0_GDnBM7nKgJeEI1HO3bswHkIxFsmzrHlRacVBUF_t_55VC3yIx4VP2WCf6ePdAcYjcCzw7g7iMfe0rP3KMpcGHLrAeELJ28MMWcxIFdMPehxgQcH4CbAsBEj7Iei0JN8PHI3vfqaWIWdTaqjzUtOBmoh7b_lETp6FbauV1KS9v1jTSetj_5IQe1m-9Zsadt9Heg06ARwt5OYJQFWpvZNk4A4LRljEd62AHTNZ3F65c2t4A4R84_wOPaxyxdfSR2CBaybuqO2Ss_EY_VNVOzbv2vGgFS4FUKSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
🔥
آلمان شانس قهرمانی داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93148" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93147">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d067350c0f.mp4?token=qtz4_fv7xPwEruylxKWLRaX5ZGuvBvPAgy2ARQQb6dnCGaZMnHFCbjclqKCFela7m4maiWh0-U5m5_ICU9O5NUgVn9_GGnXU7ExAJdgFKu1U07khDbRPfkLjFPpj-IoG6QT5qvU1J1Tq0AzroWjKcCw1969Q6JkI_g6fqjpxc7JvO41BlIXNSE3XIj7YVVsDARXgRVtgosf4JAiqIrBCidSF3LXM68JtbL7qzZeQzrNootR1dJjQcrEg2fk99zNEGs9fDsRAfOsxqMD6qVKx_WMjKdNk_pEnhyN2pVsudSPH_lxr1qLQPWILs8x95JdbUms4jrg6y6YW9POGFHKXdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d067350c0f.mp4?token=qtz4_fv7xPwEruylxKWLRaX5ZGuvBvPAgy2ARQQb6dnCGaZMnHFCbjclqKCFela7m4maiWh0-U5m5_ICU9O5NUgVn9_GGnXU7ExAJdgFKu1U07khDbRPfkLjFPpj-IoG6QT5qvU1J1Tq0AzroWjKcCw1969Q6JkI_g6fqjpxc7JvO41BlIXNSE3XIj7YVVsDARXgRVtgosf4JAiqIrBCidSF3LXM68JtbL7qzZeQzrNootR1dJjQcrEg2fk99zNEGs9fDsRAfOsxqMD6qVKx_WMjKdNk_pEnhyN2pVsudSPH_lxr1qLQPWILs8x95JdbUms4jrg6y6YW9POGFHKXdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
پاسخ عادل فردوسی‌پور به کسشرای میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93147" target="_blank">📅 09:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe_MeXgcQby60uPTfl9P3AoUFF-XN2QnixHhiRHqjiwE0I-oRUrIx7_o6jjyupycpRMilUtjkk6XrBREklLSZOtO3DF5AKEyG7elKsle9HnpT8soxHzoAMoN3mxANWXeCNTI5dLnySrpuWYSdxryDoeg6ClF6BEa5duMkvD7VRHnK1Jn4r2w-9ndsSiAQGPCge_tbMiFbtRDzuHHG58swwdfO756yHlUYGHebQALaT3qYA5U9CH_NRYfvsoIKKnAn1K3M1RjvJJ0bBtO3F6F_16q5SPIrfZ_BY5qoys-m8OpLE8sVvmZ4RH6KbP6Sq1FdGwz8slAMN9Wci_sHzsAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
رده‌بندی گروه F مسابقات جام‌جهانی؛ سوئد با گلبارون کردن تونس، صدرنشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/93146" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-gLVDh_twuFFBMn7GXApmPqMwIUnVH0OODrhUe3ncxAPMO5o68dTDlqc6PfAPTR1KZF9GvJwuGvkK4z7b0FTpfgjNPQuHbnvAHGb4GSi4swdBt53q70uBDQBpyyPDKbVlKCyL9uAdKfGjQ_YpNFu6WvWkRMg59JanDmeQPSRhhBNkY3oHw3uoU09BtwwcpaCYjrKnZh4pbzC6rEelstFCwW7EwkdYs0vMA8wZ8H3GK3HsrdqRqlhFSSZbuaes3ww6BNFUER0Y4GzMcupJGCsHcVTYkVtkJoSaiF-dwR-bphIYFmeQrYXvVod4NJtjvUfhTFqERehWdYfYjUWKP7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
در ۴ بازی روز گذشته جام‌جهانی، ۱۹ گل به ثمر رسیده که رکوردی جدید محسوب می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93145" target="_blank">📅 08:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سوئد اولیو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/93141" target="_blank">📅 05:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/93140" target="_blank">📅 05:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شروع بازی سوئد و تونس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/93139" target="_blank">📅 05:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2AXg1Y6iJ4SK-9n3mb77VTnSFD_6CF_wUNWUFH2H-Orp4NQF-mRfePNmh662xgFA9lh0Zi1teNS5C0P3UrzE8DyAJBu0DeFA4AZwY9jD3oNBzxwknTDHC9LJTkLy7KAzlnd00-14e_XGoRKvfpxFFYoJWItqNPdXbOinNIi358qbJCfHdqnxMkXZ-itUsipxa-2FoKBPMLfUzHml8ixD0vo853cIZsGvW9TDkUq3pK0w_LEfAp2luvpigFPgyZKNl-i9dLH_o5QbJAhAfX9YUG9w6lNbXgx7Q7QLmreYyKvw4j0dsApXklsP_w9lIShQefvFdFH2vdCe420B-C1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ : اگه بعد 60 روز توافق نکنیم باز حمله نظامی میکنم بهشون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/93138" target="_blank">📅 05:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o87Ejo9DiLeM0WDAUAr7ni3bKAUmsCbiPk7oDT9J4xRQV6QAiHXAghAOag9K0xIGnTs22i5CS65oLcSAE5iIPM4zfEJnnt96zq-N3OIkvLLGWuLxZjeEswYbBV5FWbQxxxuX0YXrUt9IYEWZOpcCVZ1eF2eGS31rowGDoMNPiO8_tAvwxXkOrLHt__uqNSdrs67CyV17cvexUcC2yyaUQVkMx-OTOncw55IN3gi3b-vgASwcK_epTyGZa660x_RVWiaBZF500Kj8siE3RMjLIuXrs-gqD0eK_lGGjsdFEPshU9yUMWtK3Q_9ODS1JML33x5uc5prtHWF0DU26YXjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TS5gFaf5qvlA6wjeYHVEp-MOZGcx1rokjoxuniZ0ryXMIpwlBlKw85YZrmAFzcM0hLfP2hxhXLiewrlUoA71a_Y6p2-H5Wz1TqnuJbqjSUfIn3keP_wdBaA4CBYxp3T-yRClokyB4HC5Of2j1RrLeyiguSYFf2J9L8h6qcmsrnMLoizW6lfnSCDtxAYrPuEqZsFyoVhvGebJSNA2bseyh-fLOstHIBtmoxqt-B6okTAQWQcxpOQgTa0Dhsu2ENe_QFgJ6z2bzBkl9GnjI6EK7POy7QZIt3u1afoqkwecAmaKu6uZPWun-4Ak1oyo4rI-yEWWlWt8MNrSHakyuVjnKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇸🇪
🇹🇳
ترکیب رسمی سوئد
🆚
تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93136" target="_blank">📅 05:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncdbn2d6UQapp8yuTZQL2lO09UbCNDGP8WOTJRViw9G9fnSSEbteU6Kg2GzTX6xyzkXpnFXOu4E68dklzeUhfJxOt88tMo6oAXT9ARVzm1jyMCO1YBupzjQXaUlT1VQk56GdLiEg71hc9QyTnQYi0EMrTs3bH31ABBQEuRg_ULLY3jVN4lwrrV2RObRjpkn-83Pmoi6THgp5ruT5nSUZYys_nbUAJ753UQeJQ4jGDtWkYMJxiXvFvyqqabdYHsfO3eIWSr154PEgNDJaeMw0YhefhYdqk8cz7gxp_7wOqKY6FefRFrFuEt5xTm49Bgm6EXIVUimltTTEySVjxPxuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوقلوهای ساحل‌عاجی که حسابی تو جریان جام‌ملت های آفریقا ترند شده بودن دوباره برگشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/93135" target="_blank">📅 05:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMdWvrIlohzdWhN4BxgrpT08CJXQjEmT89A874kDp5DA7bcvnf9mJolpZoobbZj3ol8dvA1078Qn2JrA8EC7x4tn21RcB11boBvekWerzv31yEup097COOc4uYeJ3uMBzR2MJCrSgX6Px2vVplp8KmF6bOVuz-xphNG2Zfccfhyun7vGvYrGWJatPHoqGSeuIyQVisHe39m3gggjxK0XujJJgwMPNJHoQfd-cH5K_OF4hWRhyOTTToHInuxzkBJrEKKlyO1VHGp6FinVJXVYgAopFsmWp5voKYf5l1RmE3i4OHn8bu7G-dw7aIYU9GXaIyQTZRP0TQcH66wXk1Hw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
‼️
تیم ملی ساحل عاج، به روند 19 بازی بدون شکست‌ تیم ملی اکوادور پایان داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/93134" target="_blank">📅 04:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSOZfl75g84jB_QzHCDlluOTEJ7PWuqcutsFh7F7WHP2XUtNTEocb0rGUWbtC8isjFeImsmHnKZzaPw1ogMYfYIjTfYp6fEfKfhV94Rc7NUFf2ByjLYkkSWXn_GPseH1GbYB_fcMov9LSLfFANc6uWY6fWaMnFHM51Pjk4mRcBKIlkgsE6sLwYVnbbdnioFBdV2mTO6vuiRBoCsxQW1nw6pv6Nwmx1txGkDhyEjbW-OiT8q5fnonopWrDJzSFSAbjO9xuxWFQLylY3A3EztIUOdgtPt3lStNEO6_piATNhm7424oh7jBBubogzMPGWe0ZmnY6_7PbMh02_IkRJ43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه E جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93133" target="_blank">📅 04:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHJwkzU-NakiAR_Lu7adA0s7mIXXAHHXNHgi5Q6tCAhZzAtIwUT4CJ7NqpXKJ0QltK_4vLnKkYY3wV1kcMK7isp43-pzVTavfhJUPJlvz2v0QZoi_pn-VpdoZH84480XPosnawUPfBLqk5-nFoJGCJ7DWI6Wg8ZVfgAcHGwFD3U7XEURE2T_GUq55D08qrHCGJzFCF_yRzh6qs12HehCTtqMz670vGz_2fwd4zX_2sC8M3KMc3ztnDyfhFG6NCoGifqk227SS74zedalHpj_pRO1VR-vuqH9os6zqWseGZdUEjp0znIajIhdQ_SoVFuJy6b1txj6lyLiwrsLDJfuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی | آمادو دیالو فرشته نجات ساحل عاج! سه امتیاز شیرین با گل دقایق پایانی
🇨🇮
ساحل‌عاج
1️⃣
-
0️⃣
اکوادور
🇪🇨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93132" target="_blank">📅 04:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/93130" target="_blank">📅 04:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلللللل برای ساحل عاجججججج</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/93129" target="_blank">📅 04:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlWRGYwmx3dDU7WUPhAPCdZwJNE40HZ6BdydlEdwoR46zYCNh961iyWpB4UuK-XhMhl-Szp79-dIP-o-9T0qA10LdUnskx_nJSrXrbangKMm-ixwp32ndLJ138o_FK4suMc_WvWT6It1UChtUthItcUH0Cesi_hkJYuqtCRjV5HLVYF3PsRNjyWju_S7CgaJou058yt_d-YqoX6N87s0ozlQ3ul7GbpZFbQvlN3j5fK1iOvnnxVH4LGiXb9Fs-DMK2cZJgg1a6YToJpyWLBjgoGOhyiSBeRMBr6YVPkLO0afsJ31oxoMPjEhElkKBcmMtAZ0fUy3fUYONnyppADdXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIh7lnBqE8xgb8n4DWS1cJaKFLLVKXBR02TxMz4K87wgF495LaPjaibZn5WvBOEGKj78zrfUlGV54V_A4LzUF_-un3nyVzBNBRO4Q-htI9oZRy_81wMj8fpAsCi-JHd3pCSCUfZBNzd-2iycXnSMkDUa_8EVpzvVhu_MoTFdaHu3E-x6liapGxb8xR1Z-35MKcHUUi58VyglJrUxtC27fuSnmvRZtxw9_YXe_WK_SawlavqjZsAqTNYxKc5RpbYuRw1qTHw9W_4MokAOW1OFFqvi2wKO8mnBE9RPkQ0W8jKkurb7qyALuNFcoMjmeIzYUCcfvmGnTGa3t6u7AuN9mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇸🇪
🇹🇳
ترکیب رسمی سوئد
🆚
تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93127" target="_blank">📅 04:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73b39896d.mp4?token=IL3wK-t3JyNHI-w4p1nRlIrhEtiRHNtGbpZsuYgy-PF4bS7EL3yuv73_qVzxn_ZeMuqB-8pyPh3qI501thIpqZJFwmCzO2-T95kagO_Pifp0gfTQ8MC7WBgRdxG5i9Kt2hpYe65nUCHbSP_TDDwMrS1XQ-04m4Xi7gRXWeO-YAA65X4NbQOOO93Lwa_iKW4QU8cj5yhSZFsuL6eawuZugGp8f4zRmGlrG0OxayCyfD4751yBHDrIbnHIE_K36WkC_zmmxrA9WIb297upultivzQMI6FVihrhGSmSZWjtXQJxSfV3MdlGJM6_J8FVKMojnaiXzFG6m_wyzYvLBJCrSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73b39896d.mp4?token=IL3wK-t3JyNHI-w4p1nRlIrhEtiRHNtGbpZsuYgy-PF4bS7EL3yuv73_qVzxn_ZeMuqB-8pyPh3qI501thIpqZJFwmCzO2-T95kagO_Pifp0gfTQ8MC7WBgRdxG5i9Kt2hpYe65nUCHbSP_TDDwMrS1XQ-04m4Xi7gRXWeO-YAA65X4NbQOOO93Lwa_iKW4QU8cj5yhSZFsuL6eawuZugGp8f4zRmGlrG0OxayCyfD4751yBHDrIbnHIE_K36WkC_zmmxrA9WIb297upultivzQMI6FVihrhGSmSZWjtXQJxSfV3MdlGJM6_J8FVKMojnaiXzFG6m_wyzYvLBJCrSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
حرکت دست ناموسی داور اتاق VAR بازی دیشب کوراسائو و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93126" target="_blank">📅 04:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khxMlxIp2yEZfOxL9aKWGAG81uWXDS7OQm-TQV9NJfuQiWoMUALdCjZlu-gqNEX9nuwfKTau0T_O4F7eAYXQIwPxl-zNUGpg33eZs6IxeGW2BwVjlMz97_80h6E9rrpCENcV18pJUT-OLKg76wg8fZgl39JaXPW_yURQHWaNQGbGPlqSzP66psPGVC9MUhHuekERmKFBMq_ELRCAoJr1tiXu5TA7iowUK62wlzS0d_G5j3LGNa1Un0hWJmRhlHcot3IE34ZEg_m-zzS2W9IGs1Y_x8e7_0gYsY54b6Yx7vzJFnk1Z_2eIjVvFNpTRwvcf3DqOg3fyk_bl174x54yPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
برای دیدن خلاصه بازی آلمان - کوراسائو فیلترشکن خودتون رو روشن کنید و وارد پورن هاب شوید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/93125" target="_blank">📅 03:47 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
