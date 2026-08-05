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
<img src="https://cdn4.telesco.pe/file/TfjLwu_097OoJnoZ44M-Ji9pmihqQz1FjWjyseytQvM5kXS0ZGqnn8_cutxsxKo6T6jJgf8vd2CqPQVoj6t-G1NA56-GIdEWYH1wDV9JldK01dIJNphvdxIg3vvpd61JYlqgIg_Gf7JDWbSoqs_G652deWwyUjA1SbvITEbBfccgT0Pfnr7TpOKj6RTbp2kwHiIMl1nuBEMp63atZWC1zdiPSjMDDhJzf0JsL-yguXDWXTHpT_Mz89dRXcJtPqMadMYZlayostozdqb3OBK4RX9dO4Q0tmcVbIDtIpksecISNeSEsH4JrNXhk_4_GzGKJ3iolp7co1zWyncW9grGhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 134K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 19:56:33</div>
<hr>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tky4zdmcB9VE41RQnjhJ6if7DzftinFqm_thjZMi7skQPtLA1Z3EDd6oRel9xfwlbjUUPBSF6lHykH3VGZkPLmtHLOd3rnreTsVTK_rFuK-S7xNiKQHsfqEvfJ-vZ1l6HEDblr9n1q1Da3uCkdqH4Uiw__KpvpkaETpMcoq7FXUEejds9Mx5-kqR4vqlJUTrWPtw8DGhgJNnPXA8uX2sHTcUm2X1nW39RZpoi71BsSR456VNeNU9UZFjtDYHryGxxCe37Dvt30l1nYKMzlPEbZfZaB2M8TnoljBoLBs-J6K3ZZfvbTpPh2h8UR9qlGKTc_W5Ad11mG4A-8v1iJYBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2t8zjQ699wLlxessi_d8uj-0P7Q84GicATwCZDgeLDuPZurMdZQ08ErbJJWGiFikXSgX8e9lNmFvEZ5Aiqg5TlKZ3yPENSLZl_WbWaLP7LRFEcmpfiW4RX5ck7N3sD5nEt0ktwPijyHvNorm_FIjZJ7KPbHUHvNKMfKwGn6iz-cMJhABd5JtgA7cGtAVABKFut8IqiwROtMhuwW-AHkQhhzJ3Q6n1b1HC5gLisb1id7wMIPk9ZzUY3S6ZX6X1q0ey4jo79FJGikHiKyZ_emU3MfGhbZyoRTjxtfSqjNZLBPOaTk1BTx3m209liR8-nTswSnBdic0Hab333N0Tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqXC0b22XjlDhzWHAASMitc0FIlfUu7N2cMsZvX0F4SZSIhm7_CrfTZOvgGMfXnAmw1Mx0LoqtAC_Ez8ZOHZU7TIfYqUK3DdJN_lLAUQ9_GWHh1jp3dEDHbfGEjZwhaGMlBB5fDXYFGJIDVB3i26Y3mWJ_DaASeHXWvsMRw4AdYIyhDoI2BNmkPLX0GxDIw5e8xinLYKSSrF0Nr2FbWjaHSY1ublWHjzjN-sieAuqBmz-70l39On8ly_sNLtrB04i1SyWChQgU-7iyZOVSKIh2mJW7f365R-tknJjgcMUo5Q5xVkPOQDW59V9UFXMFBtbHvZg1HhBaWvpKQ9n-yBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q177bzmUaAbbQ9U-sERREHRwvhXz4ZDpONDivU_OsEg_NrYATL1C0MwN7vYH3idtQWbKcAqdHfINxMcfcYsgkqWm_HepLpDw82-NW20AJ9a5Gkb8tKg9LG_Wsog4SgVwdulpDuqzbjk6xSVi_8V80yNbNoO4a2K21YXmI5eWXP2ZhsoNUBzwaOExj7uDd3gsdiOF4lxlfSZrrBhe_SzeM0tlDOWHQuIZSCr3gJqwnNbJoKOHp5uIrc1RHRgAiV1QiIWoON2X0vb88h3lBdnv5cf7OQ_ym8DiWL4QBlMzKKkzrOngfVaXnyTTSiN7Yp7XiAjIx1Ul9OSCsAz3mKYJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NePd2AjrG-qIKCOGEwSRRJRBu8QPtCXKTg4Jr5xd-M6Al2hvwDNX_KJhsRUYgOP8lPq20xSjliPUH6R3r2mavzA3uHPQWlWiIbOziLmdg3MU65s01bBES8PdA-RlVKKIj9mhZPt0YdpkIPQebwRSo_8H7X1YdHL3-B_4t8EpFUWld94wWP-jENr_-aIvxqaWXPIFKojew1wGpCUUCaH2LII7m_XBcdQOgaHv_0r6XNAnhJLYVnM-OJq0NQb8W70dbbzjo6wnECG-xTuNNJSq8bxuX-vffIRjvyEKXSX1ZGFNThYrgJu2B7kSx6lvqW_yzfT2i4TL5w7siqgbFTgPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF5vycuiAZPED40pdet7bBmTMcJXa81xLU0ujb_9OwYuw2l18RVpAJTw3pGWBAOW_vS6DDym5AsCa7z4yPc5xtuSv3EkFeRK__zSEjx6Y1zXuH4xlJH3lv5B-cfeYj5CMlOmdjHKTE2y7Z7tp6sn4Ab85K63Q1DOcZjJyWISB05dTR4w657y5-o59d9usF05uVyvptI5fJzZdAHaGUEgw3ywo7OJZ_CLnkyXGRbFk7m_jDpX2uXWckpiYG-ZkLyVKM8p7hbyWUJp9LWNT5clGI-ZC9SmC4fEaR9BT0uc3vjEjdfpNn-K1HCU-SW_zbfAiQGCLgqQ6xsrohkVS6ICZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Db3cnonA-aY3BBQ-RTrETMfG_Pb2Z2pS4P6NAkg2UrswauH9cakLKHhJSf2L4DsoJmXIMt7Ws8y0Yck9jCroTPb1nPvPTxeBKfQozhhGSX6FUj2WMzAKmAhSUGlLWyXZuVp8B-g1ooH34eRX8VppN77TvYAh13dwNSe4cw2ds9xwNNF6DtyX3ROcTD1Ao1-6m03qggxuDdAy5btdZ9n06aW_ieldvBYoduR0IO_qDwjFjEHHewjP1Xz0pwoBj4p-_qoHM7GylzY8M5JDgksTMZChzCjaPzL4rW3q5yJJAGCDl5iLbdml46geB170ySNLIE9QMT5ybOlZHkLVi2Z19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=j5y7JDSbRIrjWznonCRx63zZgN6JwdDjwHZ5B8zNh1YMNet2chFXNDyeOMd5cMQCLMVh0N1f95lgfgbUojQyC9jvh5pgGIGX75_iQfboiLIgnlQa0euPNLHqf0JUy8cIGWMrDRfi5PPKmyStfatAJSbNimGXZU-2EEPCFAVFhLAnyz4XMz3VfrpuQcuyc1pciWUCOSDGQsl_p5dhEzXXqVZh1XyGRjqjNmJ9rdZQ64pwXfWXhWELby_Zjt5bJ5fUs6iLjOJ3f1HiwSej7gaITKESyMCDCxeBMR8OfI-6VjfaFV66-yGN21gpx4E6_lfpEc-S4kPOywbMInOtsrxgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phgihB6RglSJEha4QerpHlyF7p4wA69xQj7mxULcANw9pyKATSBWbsUgQDwymmPuLRNMWL5WCUfIUW0h1zdefrJSnIIv3TDs4BbCNiryvZqhaBPnyVfCQNlfK4ZZ2SRLDAcO36FoG5lw1NeKFbaYhmSsF7QxGb9DR-ZKxWx5JAz3NdRi7cvjrvaD-7Bab_8yT2FLsfqa7cXx-woF7M0ooZCWF01otCxDTjBTjD2d05lFirweHToUSNCEffFaFxu-1XivNwfR6yEl9UWc4oj333htIwmiuiHW2wLdOPgJx1Fp6C9nGemcqBoIVKsHiW2QAXZzqSBpvu9X5JJYlMTfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=LGcZOONBYTnbLzFwfeB7G6rmAhhxoTQpKExgZ0oNY9wgacToIDTzFLmGQF2Mpx0kDKrWf4gmy4DUfnt_puedoLl4stAO8FxdmTAf-AlUOY_PozX7f7qOzUC-NFvya8YgfYK7MfTNIYmo_6Pevg9QFnZMBmriRDSlR3iBM3QQWTBs4R1VsmtV253jpDohTXFjRc3j55LzrlpkUtRHbq8WDwRT2P8YllBrbzP-HxYgTKCiLiIyFbxUnoAESHmY4HD1w9cF3pNfoYHJELRvxEW0tXqw0cYV-B7Ha3W07vKzj1n0jkDgwRZrKIduaZ1iEkIov3pzwVQ1arE_VTsQKDm1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=ifpHp6iNapfj6SbkxiKKGRS1bkQOTDDqGW4z5XBexaO9pfW2r4MU0EiPVBmBh-5Is8Qh1Im7jtO-UEyttdLCRoxm13ONCsIR3nOmzE4AOSH8kqkBuIxiX3ZTFrletD77b3D2IXRwd31tcUE2HVx7rBCplebI1BXJY323iRan6OGf_2GfLY95-1AAloVRZkRUeK3WF7oJiaDFi4r9xJfndoCuJAAfCdW-sguKiJMrFq-5c4JK-9lf1Gb3DHE8Bch9Roji7oNKydcVwI3CmKaA_MgmpM0F2dyPR4X78rism7HUXL-D--8CmhNtGUStRvt0CYco2is1XRmV8HIa9afgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoUC7Nr72cbFM3f1p-UCG20K_XicwfYhKgR8hKnPz6QJ-MPf3GyS4w8HRDL1mPx57AVXvykj7j7pHl_V8YNBB7XZIhZQCOUy7icqMpXkyZXOJdyKDub2F2xq-P7xYzH5QibjUcf8fLl2M2P8qWfjclFfIyIzwDN1VKOu9w_EGd05T6XVW-bd_vYHKxP2bH4xDZGHQq-OtoUHBu_7mxesPM12eWSGrjx52M1bSLFo5LNkzBz0yoU2YhiK7TKn85cfzo8dvsDVaqJ34aV46KVm3SO0MR_ORuiNr6Vp3_S_AlMjtqYOaEdduszIi-n1S_WxVIaSMR3bE6Vx85Rc20NkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=gEaNg3PNy9RWfRpqRCHes4ImAjT3A2FFxp3Amx4xiOI0SjJF41JoG1h1OwzIoODJVZCWmDTiIf1upYQFqkhfqCOgb3q4X5zt6NaIfBhWe8V3QdFwJkkyI4fyZqUQnFTiSucdafl3HgdA_So_GQ6QWIUH1wgMeZD9fzDxwCH8MIbTS3LzDwA8_F4d2hScRicQG3-0j4i8jgLJBkdF5-21tk0nJ_XeMqIiQqlGSiVBTwsb7gfb0tl_Oon-1A057-Ca0jrRFMyGkjxvgOtASHhq6vD7B6d_zPT-tyZE0sPwh6h_v6GKDD0bSHSbCFwPJ1u-WMWvl2WyeoIc7MacAIwAAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=qWN8rEHJn6kfPrawv8SZ2sumGFcIcOAzfzX-i5NDvx1imgI6EJgpk-9hyiPyHlT3xSDa-joXwigfBS9ru8OD12NyTIaB75BGluDvpuhzq8dIbA0QH9lU0jSRaRjwr3GEO4brHTzZipRUDSLzgUlhImtOkoGWvRFaMst-SO0vYvnTOasP6Oap9i6o-V4UYDDgD8uDCusLlRluKiDLpm3HZMuNnVgDVIlXsqCwOkIpaA9tyOpASfVibF1tDqWd2sL3TaBs2dUn6par3vC1gC0UOdFYS9BiGBfBzDrNzlLrukYlEEJl74pRitVm-6SNMH0yIYkPvljZXf87Zxf-7l_nNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjSZUxtcYmQnuZ8I6JcM4NEJA0LgJ3tqJ3DlKo3xrfR4-qiLyLJftYrEikIqemF68aa7XzCnCNGEkkCXch5MAzVR9FLLZ0fftHkBQbiKn-q---jFqA75TCOsqFO8kN0HwkSzHtLi4_ECwrq538g_Si2EcPbxGInUwIpyecEwHHpTNvZZYqXJkZoTYwZsa1BuksHAMzLJb9oSZl1XtEAmHFiD3GUrYUMS2C1SwXpcbwh1Os5YSX9Yg8BTGsLCzOf4gaL9I-m3ewlinEqrIgKkyqytTsaVZGky2KRktciVBXgou4YhzIXBiI6dI9-mrQLNovHfKwJZddT7W6GG6pj22A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=d9yubhK-8Sb5vq7G-badToAdPKxBXJDkpMay0Xjls14Fn9CzW_igDY8mTVxV6pSmPnRZQiOmHMOZSPSOmZfjpOSuBRsT01_ZaEpYiCdRO2MtxAe0yGBal3ZINivOAJyymdGVPgOksahEm4L7ZHI2Zvb2sPhC8Q6NGIkjmDMdwyx6qfTt79REjafTGStY0Iqf81kDT4Pm1w1eSEz8-WNocrYHWwUBsud31yAhPiCA8W93CybCjVFGJhdIcDWcWBNQYFAio06901XGaYzgyZwkzLgocHwQQOb0us34Cnl5MOzjVDC8mFlkkdCyE6Q1I67wy2v-kcIjTuR6HvmgQF-_kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=gpJzbdBHdKcjRws5N9t10l3Flhm0BV3b_URjRbECevsWGfKSx3k3gOoUGQmskC8ZKnVvld4OB9qaZZ2uHQeEqxDLzDi-Y6t6j0nwnPGkHiA8cwBtAkL8zbTRKeQdQIk3G-x6p7BLzg9xCuDulZdNg4vbvTD3EnKwv6hXrVsgrEc6U8K_IUz_V3z-sRAn7N2an-CGpnfJ5ADiJ1Xnk2Pvx_v2mqU68qW66F6_vNMSwRe6sA1MWZuRWwXb019Dx0ssgpYKHpXeGFXC5M4Ex8FJSb4Ypee7T8wvON2wMWbKUPgol3IACDv5enc9bZsITCP2mlanLhLfzUhLyc7Hqak9XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=gpJzbdBHdKcjRws5N9t10l3Flhm0BV3b_URjRbECevsWGfKSx3k3gOoUGQmskC8ZKnVvld4OB9qaZZ2uHQeEqxDLzDi-Y6t6j0nwnPGkHiA8cwBtAkL8zbTRKeQdQIk3G-x6p7BLzg9xCuDulZdNg4vbvTD3EnKwv6hXrVsgrEc6U8K_IUz_V3z-sRAn7N2an-CGpnfJ5ADiJ1Xnk2Pvx_v2mqU68qW66F6_vNMSwRe6sA1MWZuRWwXb019Dx0ssgpYKHpXeGFXC5M4Ex8FJSb4Ypee7T8wvON2wMWbKUPgol3IACDv5enc9bZsITCP2mlanLhLfzUhLyc7Hqak9XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CphDic5YTXlZUdKgVY2xbU8Z11BTUuT6ucvGzcIkWbnOPt74B6yPXfwFa8WX5s_MAHYQAsuuJme4-A045Oh_L141Nw3jGwZ0TdQhRil6FF6bSQ2YuXY43vlQF6VsKrwj5PrR0iTPJROXuWRwMWMoW2ITAsLMZPxPciS4rEvVWKmR6n4SBS1rpEW1gKwxpuIGo1Lw98pWjYqcjUrBIYp7o6XkVg9-vqAJbuDwjSFmk5RzhWfRBy9DdaKBM-LcqQHYq_srvvqrJZheFT1i021u_rml4pI_9bmvjKa-EsYWxj4zvQA52PAIuf_maB6x615CN0LA2sUBB_WmYuQwaBnzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6me5sC-0U40M6o3N7Z5DSMD5ur2vYCHtz8rQzBSx_smy6TWuu7DTAPmciZ0LrLXcB-r4XzhBiTBHD6JCGQgDYljQbIIggSVzpIGJ3O7snnGTzUblJPhuI4tRhFs72ztK94H-x4m0o2yOeXeg0T4DopKfT3rK4uWA1VVXAjoRgXzvz7TPPXlzUW_aALrPyPXivg69198SYcxpv4koD7DUiJtBAtlc1teWA0TkBlagPwxAWCLIfJN-qbACZkkU7GVxuT4kuze1hiRb8I5gT-rUQf0QZ1nDoYPat-YCMD259ud7TBZ1yNd4CR67ZVlQwGQzscihSjDJ81qsnFg7_XrVxOM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6me5sC-0U40M6o3N7Z5DSMD5ur2vYCHtz8rQzBSx_smy6TWuu7DTAPmciZ0LrLXcB-r4XzhBiTBHD6JCGQgDYljQbIIggSVzpIGJ3O7snnGTzUblJPhuI4tRhFs72ztK94H-x4m0o2yOeXeg0T4DopKfT3rK4uWA1VVXAjoRgXzvz7TPPXlzUW_aALrPyPXivg69198SYcxpv4koD7DUiJtBAtlc1teWA0TkBlagPwxAWCLIfJN-qbACZkkU7GVxuT4kuze1hiRb8I5gT-rUQf0QZ1nDoYPat-YCMD259ud7TBZ1yNd4CR67ZVlQwGQzscihSjDJ81qsnFg7_XrVxOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=TcbJE45kkpqsTdESjsjD2QaCumvTpMBizmbO9ZVaaZCnIf1H9vYlmc6a16fzM66q7maSuN3zEiy6i_2N-8izg3ZcJs_Zo_AkKpyTEQWaTVsLRXk55g98RcZr2GyiPwKb5ecszsXkCT7P9pkPbvyvnkMW8x-xdYLWpVps2fY9273mTifbohL6pOnKFhZwobZEgnnUveKPdZeYoraAySBINLGEzZQ3pP3VSudfol9QKzSrSrfJWIS0fpCYNMD0_xVJ-KzD0HOPyWZJGp8HG8eUUnXG-FE6Bktr5p4yDK-FmLKELLjY0xceNbZebvgOQHGc9Fx-aqrehHdy6lCfMEzzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=TcbJE45kkpqsTdESjsjD2QaCumvTpMBizmbO9ZVaaZCnIf1H9vYlmc6a16fzM66q7maSuN3zEiy6i_2N-8izg3ZcJs_Zo_AkKpyTEQWaTVsLRXk55g98RcZr2GyiPwKb5ecszsXkCT7P9pkPbvyvnkMW8x-xdYLWpVps2fY9273mTifbohL6pOnKFhZwobZEgnnUveKPdZeYoraAySBINLGEzZQ3pP3VSudfol9QKzSrSrfJWIS0fpCYNMD0_xVJ-KzD0HOPyWZJGp8HG8eUUnXG-FE6Bktr5p4yDK-FmLKELLjY0xceNbZebvgOQHGc9Fx-aqrehHdy6lCfMEzzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSpbY4Bn7879deH84mNvbQG6eEY5xp8YLtbpWlTY_Y7i0cNlWwI0EgFY3lpPilI4TvtI1lG_zpIQOZfcl5Rg3iPuiGDHYUkJUZp02BJ1d81gCMUhhNmOFz5PO_aLy3_89wgxnnQFHe8FSjLjuXUD94qPcWGFOOeECLwlgtcCYsMaSRpsYH8VnPVR5iJZ4zk45vTD8xaEzRQ9lF49xb9GjEZ2j7GV9Yzl8XqvL1volnmbTLdiDJP6fmn2b4vfRzW097i75HRR87LCo-QeTTfeogAsgEq3kG-tQZGVaXHNY2dxhcu24vfWFoITJsQPBflWrGhzs2FLYl56z4Hp7mF3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI9qXqxAS-W5IjzCRJbc0VhJf0UkgZUBJFu_6KyEF93fBFENUWLTI2MfpMBom6UBOmkK8ZMYzGYjfl9H3hIwltjIftU7NxhPvqbbCSctnyUHvBsZawSEKOA4xOHp5MmgxSab01T1_cnkPm9Fi3X8qC5G6OjQnlnVN9GPY97dOm6MJnZX2iEFRoW0k6AmPFMfNh_lJXmD7rWweKfP2BabbUngtA-WeVjxkuuX_6ftpiM7H6ZcLTNqQio3JOVGeDUvNcsVNFuUUSzYg9rk8f9aruKdJu3SnZ6831cErQjxT__lp18asxCZPTQwrxJ_12l3Mr-csTWTTkeWdoSM6E9u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=FHhQ1vro6W0TIQ5TdnSjEcWvK39yQ2sausJd6Ei_ED_H4o5V6nyXPel6xm87fJNKvz4celdDbo9plAeRvuBgh66hV72h8K8oYtoNtTO9cua15GIuNjN6Yr5kq4QWRxx0alRoNsC6wbqH3g--jA_8rPYTmafyP-WAPfr7TI2-m3Ajmx9s40g1klHdTWHZvHVlX-r_R0_LrtyFmbPRlnxH3uanBXKOamBiHNoxzFTujOCfHSkOyI-maKxEIFQQBo88MVR4lULzxq-EnKsPX2GFsFgqhVARpq8n_dlSyR5fGV42mUs7aP7dc8qAJtI_0Ctw-M0ZPdtl99_E91x4losxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=FHhQ1vro6W0TIQ5TdnSjEcWvK39yQ2sausJd6Ei_ED_H4o5V6nyXPel6xm87fJNKvz4celdDbo9plAeRvuBgh66hV72h8K8oYtoNtTO9cua15GIuNjN6Yr5kq4QWRxx0alRoNsC6wbqH3g--jA_8rPYTmafyP-WAPfr7TI2-m3Ajmx9s40g1klHdTWHZvHVlX-r_R0_LrtyFmbPRlnxH3uanBXKOamBiHNoxzFTujOCfHSkOyI-maKxEIFQQBo88MVR4lULzxq-EnKsPX2GFsFgqhVARpq8n_dlSyR5fGV42mUs7aP7dc8qAJtI_0Ctw-M0ZPdtl99_E91x4losxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwegdNTHBifrCNGBYkygHXxegJAtLzJ0gy0XVuQg9cqbu5Tb_JUR4qnuDx9M0nPGgkQW20_Dtc7YJ8SvQuFKuQhiDddKBIAYvvAj4-1VcShCCowlGtSuPxOvGrv43LHOLCk1sKpS0hsx1oPPT-iKCSCwQ9DQrIESA-gfgeIKSil8ttHge-mvj1ZgtyBTVOQWrWtfILl7Y9OToksYePyK0Y4Y_z4CtCRHYSAVuugll1RWITzgvNMVTyQQW7Co0A_GklGMMrLrNqanr_fLnqGwGhUzeSa-I70N75xumWrpIUW4hVCZO2k7exzxFrHawFsXiM6UPeerLnzn-D0zH78lPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKNadVKoMJvUOBHv1cdMsdv45_D4I4Db54hi7DvcmuqGrfz32sWoxNzS6yvCsvTXAhC_CWOo6lx9-xVZ3n21RYj81Ehpy_Ah2D7LixZ2aUpaXQ8u5ybZ-9Lk_4NtbpN8C-uVvZmlUXUozhUFWnzVcQlXpundYy8fHkvO_4W-sb2mnqurQQhzSpcC-ZUSXbpgC0DZwUdth5VaSatZsTd5nukTjt2qSntXShh8h8SfG5e2ie0a1tlbinczIFsh2lJe5xyVaXHiBlk0H71n36YuX4-H_Qa2IznzxoHDYolJK7h7bSmRnRZKKTtosE4dhIAXULB4G81dUFybIo21I8VauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOtVA9SXgZTpcKpebpq70qLfnxzJA0h8cM3UwMLFDmmHJMuNOOidUGelnvwOrma2uzCU588e_i9WKNtoYTUiTwcLKeA5P56f13zUGf6KE_xQYa2FMf8QaCZUFFV3XBy4pvnkNYpM2tXkNu5hMBYvEVipIRD8O_rDXCZvMcMtalhZ0FiIdyCMK7K9AMK3-33r08MiJ40TtWZts1q9y1SYS0aQgrYPwkPFRoVfMLesjrAuXcLwf5qfWzHGLQyZJ3HfA0FSTzPEK_OKpmTnvPPTne8J17zTibrD4p-HWp69drIthbciroHkhDy5zp2PKDOVk5AGRefPn6HU87Z9QYCMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=NF8r_k3izn7kM5-PnxUIThmfeLFPbBf2iVGbm0fgpNaG3doGaSXjaUkRvV2pDuUjYrWkBMcRFhgaoVOT5v299wDLbpK8q6xzH6TvgOYyQeEfcOfz3M4YYK1dzYsj1-VPcD73f5VYKKvN8RMJ1wARO4bQ7a0y1rzQAEGgPY0ddgE1j3tDt1_UEl6TgxgqlT7erpa-JbifGHHklzYb613MtGavgLEK5rWkY_ZXJsgHChyShbDT7WOkx11gGVz-R4MNCiL7giUMUfnhg9Rz5ATyd4MMMMvSmAEkC4Ktp0cobeAeiLt-AaY-3Ugg4VcoxE2L3DU6TRY8Xc-0pClAKzkgxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEXVXCy4QW1HvhJJ5c0MKs8zLu-qXwzdOYJVTTLnXWmqg8p2-qA1uADibnZMUYv94NpR9uRl69tIGnBIoluJMt28xQw9zgnhP0fxjvA1Dpnv03U14LoSiCtCyRWDiDjuPCyL2t6NwUeMbMOiZEDWYWZEF9pb2ir1ayd7uUgrsy44dmcL2pvlGl_5DkPDbLF3S8v2pOs-YmDhMyfS6pq8jz-JJwon6vARFIZ1v1WYTubl2G5TyHeMXpugjJ1JGgjFONO3tyO86od2QpDOyWxRYiNEU4dioR7tF2rfrTZyl4_giwcIW_MC-Eo542B_2XJXVm66StAMWuorDy3mXxsYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y71v42MdgSnPe2kIWZka2IBa2hJ-0aJa6JAMQdImn07LW41biE9wLfiv8FRHmHmy7bxWrObGNj4ew5wIrIKOf0qv2xfpfmmuWcmYvyqXffGihuwGPq5lJxXLmwAYqAsMSAhjTWWSxh7aucG-Wle4tI5WTAV3sFL1VxTD6yUPRCdJuOnvVXcxVWjNr0mSuSIgthW43vJQQ4ehE8Ex4a3GuomQbncjOBgyMRWabcQSD9h_SSr-dj5JW15sVb1dgzi8K2xx2CEMrDmS4QeaLoKmmv_pU01vHPjf8AXKDUo5MBoWl2YkO4aRibp3xln5T_qYFgfmWo_UiShgc9jvfJiNYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqlQULPdVJ2g7uzSiDnzDZHk3mWOiJgitPtBC62RbrL-hnoQ_NnKOx0ktKqSv02HHmiLPCBkIjpo6UtaZAw1jB1_Phls2W44yOKTFZ7KIrxq45-8XrEYzITOOMLds6Jpr5hnmMEFEpAaA8eHnmEUqxpbPZbhgWqUg26im84LAaAixIzfg9MnBqS5fRlpgSmZRlazHtb0W-pwJwT8ilr8ittgW9crOMSsbN53HaNXnTZUYFTNMMawQeEGxiwd2i-sZAoIsJeXJZ-szUKzqonLLXsawNJrTKLfBMqw-y-zj9KM_C0Dm72cvZKg_ecKANn_n4y67wCZpbgX73holZQB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=BhTGwk1KNBVa_dce1-udH4-IPaiDIC3Krs2pkI6yQFibYkcMMLIeJaWf7G0rm07XBlWdcATYoin8bugTOLioUUW3cOr2On3BtEisITPbKzbkeMFLSriCmApUt3Oh429d3dLhpzCbBSkS2HFcWbEO_UbhBqdq-78kZk2QfSJAjgxh2EzMX6xTi1tlYiBXw5w-XE5IRO4O2ImxzKtRC3NVN6x1wosEYetXECNE1sVQG2jOSNiTGCbT9gin-Hfe3HGneQUefqh5MeXAz2w6v_HGT2YrpGJ2DibfHyYkGAfCqZ20WqB0JjYwRuq-uaQqER-nN99QwRZjojxf_gkTLdHC7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=MCgzKMqe9-Gnb2v8cMzWCsCeftEzNfR-ctdysxOL_Ct5gj0rRmmtFPW2HipRoRE0xQzRrdw3HyRh5KEyaInXvjmaaJfcSFaYkAL7FRg9uvSDTUSBkm-yrmzKSAMg5g6xo1wf8LsPc-6qJtc8wuUWY4w8Q3cmlKS7ZbUFp6T18EG6h6Y_CQHp7KpMJQZqKdDyDtV1D3zPBltmNKk6ECengDIBNY5YGlC-2wLlHXpB3y-oHxDc0aCesBHClKSoMh1wKUEb2Kh_sPngDOwkpHuVJ5EOforh2rPfxxhHEC9c8St-vkyXC_OD2k9MobzW0u0QU01bzizq4zT6qnKJTbgZ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=MXekHXz3KebBU53S8sr9JIg8LV_RbBzKuibwoxpVQC3PMiLR43GdOd7HLaZ-BI7mQ2hST_RSuZHOH4YhU2mGLGt5rGo89hHQJsjPn_wD_m0uTA4SseDJD5jH2MyDHGPG_E-aCSDcSpYM83x2SQ96mLh3x5sr_CLMzPNjYfpeAL88HUtvuoz_n4N_yF2sZ79DpWpD78kz54DbsXiOJsp7fMdLEpXATiMSIw7OxHQZh2IoySGP6EeO8IVthGFbCQIOIwzaeW9zo40gATXV6Deoh7MYGZM_NCJmPpmbLKAzqukA3gUKrVElConOyXR0SybKUhbdjdIdnkjrSBaonBaIfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh4v_6xtldQi_W7-VGn1IouNVCpKbcI4WV8h6kQPQHvjoN08SFkaFbfCsAD-BqtSEFsjaY3B1dTB5I9vvU2Kws0t214-dzpEzZWd2xNYdwfMOfSv5sa4KWk1m5fvI-OIIQK-A7cbPV70_H5y4Yc0ocGRdPbNOfEJz14vEpsQNOmwNGBn_sBngXbcbBPsLXB4OCARRKCmg3ZmKbSYfzkbb5MuadixuFxrHp4_8mSpcAANdeCcv5sd06ygvNqkk8DVu9_ZTlEvHLPiqcPf_Wet2N3gAMwbbOiOESn0cxcSscPy_7huzZeOluXSC-A7e2-hTHDrwItUlNnJqMhwqp97Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtTBqr9Y7cJXGgnVFOy8H_sdB1-MaofDDq0z1SwI483rFyFyZyGAeGjC_d5p84ZkzcHdEGScrn-WzoPYHlFBthgEB0nXQPZuKkqCw5ZJ4eWeuAFPfzWUkDONwYtVTlHjqHYjrVJII7ScgQZZUWW10aH3KabXyAAmlCxclaKUdNbmqJJSP9bjqimh1jErv5tBkbsGX0dZFLoaSqYc1qZvfaQOYuI27pJNbhqD_J22mafhFP75zdSTpOVQz8gu66UStk3a5UkuSH5ZMM3ZP-A_1WGuqtkvzJOvyqGvAx-RJKTKUT4lT--Vl1EzzWLCIaUeXZ1TDre6SzwB7XwEciiGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=YXUIqEmlANW7R3PJ0uO_mxc_NEmurAiBX_VKsJTAVwi6wv1RFs1NcBYFVFzflsATgT3t87ovmoVvq3aGV5plrmiyuOwCgE0KIvlT5MQ7vgXjp0yjOT-q7EkR5jGOphrmq5nLCR1selLQDb7RsRHS-ds6iQvmTrRKKuEhXRbIMZnxz5dr9uRosJ_XMtvZUOuhWdhDFFvsUi0I8s4mwoRgUQGw_Z0t6z1nMmo-wXF8DEsxhjkeXn2uMM7MYYTr3taODhpgPieBR-ywwt6qsQukviqXpyNSErc767XclgNncwqH_FzMAZxZRNDWc-52Sk7Yuq_hNOdlN1FhSZKYLKBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1J_5l6qAH61huRFhbXWQYlG5qKdlMzwe5im0bmWjjpc7uwluYUPv2HiCfmamK6nEMVxa1LttMAORlw_T9z4QPzLcesEB0fDqjbtKjKoQy0lPCeYtP8kLx07V21tQzkJymWHHHB9dbjERTPdIUHFNPhg83ll_ztrJRoeSzdrWE4jsShINOca_w1fpYW3ZK_vG0YtwX50U8hLAgSihPGqB4ZspBavWAiX0hdSMXblwadAQ5zPxSDHMY0y88cDtauZgxvPUoQqgZNlUIgGPHIdcncQieieEm-SRR2A17ug7y6zgWWan3PgfTVT0ahmxBCEuM-ONGhIpOv3UwctXxUDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=tpnfvjQLvph4Qri2mVtJMSXzvtdrVu2Jz8ThovhKqT4bBywbGP-yrp9jaRDH6NAt_0kum50grX8iKeA50gsb4FgL6gBoG0acLTLnHllaSU2h1TB7JkMJZxj_bsuwgWgsahMvxoo0_xACGPXJFnthKyYqVG5nHhZM5OvSmdyJChOpHmsJ4Qz2b2I3K_V7X_y4ZLAgLTje3_Lw_KksVirbQPN1ig6WGNx_d2e8KrSKx6oouNME5BMi3XnG75Uzo_frZ-eNko9WxUF3NgWdeP3oCJjRf04a5B3yuLtNLgDdPtnR-VWIAJyoCy4FHxVf2Xcsyf_5fTly70yty5ltz8q3hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=tpnfvjQLvph4Qri2mVtJMSXzvtdrVu2Jz8ThovhKqT4bBywbGP-yrp9jaRDH6NAt_0kum50grX8iKeA50gsb4FgL6gBoG0acLTLnHllaSU2h1TB7JkMJZxj_bsuwgWgsahMvxoo0_xACGPXJFnthKyYqVG5nHhZM5OvSmdyJChOpHmsJ4Qz2b2I3K_V7X_y4ZLAgLTje3_Lw_KksVirbQPN1ig6WGNx_d2e8KrSKx6oouNME5BMi3XnG75Uzo_frZ-eNko9WxUF3NgWdeP3oCJjRf04a5B3yuLtNLgDdPtnR-VWIAJyoCy4FHxVf2Xcsyf_5fTly70yty5ltz8q3hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFMjG-Nk8GQPu3HbLaKxAov8HLGHvvFL0EuLo2aAdbSswf28renib2G1-JJLJOj_NxY27tbEnEz0_8yDgKtS1Pu5CQ16oGUrhEaZ_96RDgKD7YhVxpRoyKfgfpcb_25bvLHir7QUYxGWu7840c6yCw82Nm9G_bZBWxmojEIOmiCgRXITJm-PoRvRWLvD1-UL6eiVBJXv7h459or7yauRQD8Z-G_beSvXIICveFunidTo3k0KALk2NgnRyhAfts40JWkwjiz227epKirghHaoAlBJHffjsew6L69OPCuNlnJMurELmh04MqKloIg2Wl8nLbQF3JgSSDxJhhfavEp0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=G9Vr5L9z-FlvoMBulbWG9arRTYlzBrD0s2OqgrX8x-8a3wApdrR06dZbAfJho-dDuTH-4QGW8KS-NKaTNly-k3HeUYKoDfaNRZpoJDFZIwzIZNx6YprJDBOQba7TKDlE4atybL1RROfjZV6cDm6UIK2ONjug9yv-9NIpwIa_rxF06LLU099tEV2ahPKCBKGQ9_ZPioerif-MBLCCVHPLFmvQuwhh5t32ROZolU1tF1xjnMfofiacpPLtBi2mEZWDIaTxswgY9ckTm0y-psvWuUU4dVFdFMOYf2unP9JYqB4vkAMuK2oDOQUz_dnbxVxPSHgiMC1g-vtc-i5U-MyKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZHpAOKseQPdR7_pPMD1eTCHiAaLD2QbixZnPssJBH0NkS287k7oo2MSLfFq8O5izKIvvt8VvdWlCVovpSN5FtJ3LvrCDcM9ZmZF55QlKLz4yRdk2x9sn9CD0ZhaINmam8Xt78n9tj8tjTvXJ8IR4lHifo0HTl2xkqAvxq3tpA9VM3fDrwjrzXwRWj_RxaWHZeEtmendmHaCUP_4o264uHDILe-peosP6EBH47JVH9oCyxf_f0jYdG17b2YzEbzE12PEMbC3H8sEXONUOBtoJKd-Y8yrGCYX4sIidWLUrQK5ciwW7jXOK5i9BF8yJ8JYZ6I5cqzRDMgTRRhvmpQzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=OT4zhjbxqyJNWX1fNFNgtNoHLYyG8LmEwB6WH7fKVUyRZJuY7e7jWgnXzQjdioKFnmqRI72PLaNPvh50q6c-y4aU-pB8uQN7JsEzPs4GXSm_mbdhQL6pGo0qduaLoQavixBJFP1uHaFHKse5_5iqOiwBuNCKx75vogvn5wO3dGzut-IqQYlcqTCxucAt2dEBcnD-DwwfFYg6-tWh2a3S4ERiSJh6W4TJhlbdRpdnms_AynyllKdFaoRwIWNtq1s_6ucsKp2ruZ6_5CkhJ357t4nT4-3hMNTR-d5SiIkmAbAqadiaD8Wn4iE5QsNwibZMFWw_wK9u_-G2L8UoZrLHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=T4flvaw_lbYtNQiKzYVQw_oxYfvv_hAPQtXypwCFGxTDEPy43FYy0FUrIuPqJjXxLr2a_wsn8NayMG8MWNPQxDum7CnqZcSe3SbYHEfF_imvG14LDq_gvWfwLUKdXo4TsBkwVUhscp7MbAI8fLNX_UbiB7CfSK0u4GT3e6K3EihBzh8rWesM-qeV8aehzOtq9QKFQWTFIE6qdEREr1huYSxKw8w3wOrw029w_Hd1qdCyMmigzmm6Wx3iAWSeKx1efCsdr7WnliocWJL0ebKl7POPHn9-0BGlBWSrmCFTVrbFyGjYBEmtxopKZsWclCKxhm8JX6R_kQhLlRlP0bNd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lpm9Y1V8NSLK-XwAWBQoeEs_wfylCcaHhBvCvkKL2LIDibRV9s3ZbYHuJabCb0jON0lY8i--w33DCOEVJdOVhL1G0aRA89FEygid09m1mVxGIhlfjsM08uxZy_slMp4GBFI0k8KxRt_pGZCXXMvZNLad2qarKf1zOHeZLaQi0B5wCxdCBLYr1kdFeRx5pCylOqNqjNfxEJ6hdZLflYLlxn96oS2YJvPCNRjppVcFpx-LAx5nEkY-rKbWpBGPioSUMQrndpJs4jWX3u7FB652hDUR3QwJRoKSaV7sMmmqQ3f6EgbpSgpvoRk4zhGEQp8oSz1b7on38IuXfFNRHSbGszs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=apFBff4hlRm6LaXHZlcsaDr5O26Va42WdGu9IewLK5u8NLe3BTS89F6cZQuT-eT37rhUvEQMZTrKrGEvfOiHBDuA_7ahnaFsRXANoB610OhCTxm3bsLAhogL_JFYg1bOiPgkTMY9xfpp6AdsEELi6YELPU72DncqYw9xDcYm66rm3Mz-mfC6m1VKpH6oVwyAE67nuJ7RrxSO9N0-QkGe3_83eIwUFoya0YtNr3PYWdaGvgamYf9Kz6qXE7fF91bGP4NHHhWfY4nb9L9byYvrug-XwUHQroWSKum6KLVOqWuMbg55W6D36SYqBJzXfwZFvn9hwiyh02z7F2tqTYCxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=apFBff4hlRm6LaXHZlcsaDr5O26Va42WdGu9IewLK5u8NLe3BTS89F6cZQuT-eT37rhUvEQMZTrKrGEvfOiHBDuA_7ahnaFsRXANoB610OhCTxm3bsLAhogL_JFYg1bOiPgkTMY9xfpp6AdsEELi6YELPU72DncqYw9xDcYm66rm3Mz-mfC6m1VKpH6oVwyAE67nuJ7RrxSO9N0-QkGe3_83eIwUFoya0YtNr3PYWdaGvgamYf9Kz6qXE7fF91bGP4NHHhWfY4nb9L9byYvrug-XwUHQroWSKum6KLVOqWuMbg55W6D36SYqBJzXfwZFvn9hwiyh02z7F2tqTYCxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=eBavtZ-mBHN_26pL4jtFq8SwTUt4iW4Be5K1tkO-fkM9Kyrk23jitmsFpKga5PJ19waKmGSUntHQNEdNtQoIvX-5ekIp91Fib7toLNbgWziEnL7MyZXct58ZKxV4b7YegvKQwNdccAoIKe4DW_nAvPBwHtNhCYel8l0b4O3uBoGWQEG-sFTnH6TDQ2PUlS5NquQ-tvx8Y9TRSfi5o03DE6VU0wQfKJItbpfn80rD8f_vzZUHINZtqzu_gO2LOF8PU5W643TUoERD2z_ZeFnut7iN-zBnvR_WkSmrfpTWcpOTOdAVZo0mR4W9d2fcjrhLrd7s2U6DeOMwR_SsfwdfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=eBavtZ-mBHN_26pL4jtFq8SwTUt4iW4Be5K1tkO-fkM9Kyrk23jitmsFpKga5PJ19waKmGSUntHQNEdNtQoIvX-5ekIp91Fib7toLNbgWziEnL7MyZXct58ZKxV4b7YegvKQwNdccAoIKe4DW_nAvPBwHtNhCYel8l0b4O3uBoGWQEG-sFTnH6TDQ2PUlS5NquQ-tvx8Y9TRSfi5o03DE6VU0wQfKJItbpfn80rD8f_vzZUHINZtqzu_gO2LOF8PU5W643TUoERD2z_ZeFnut7iN-zBnvR_WkSmrfpTWcpOTOdAVZo0mR4W9d2fcjrhLrd7s2U6DeOMwR_SsfwdfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXMkwvwuoXnsmVJNtX12EZdOXjrTkUraWa7yqCMiLVlKpYksZbf1nDiSkWsSeHuqK0GnJQ1WLUtRoRyZf3G9DlY_xtfj2ib2xSlmB8g4DtAJYTyFUwG3vbYcKoaBvWF4B4f7-p7CZRK0ggT64KF6-PTlZvKStyEWn2Sex7C5WfzK5bIC6_MI493bHM3SOQzWzZr2cAjoDnscY1iY5LUe1GtHxd6pl7sTVximOB2N61u8BPD4pNbhBJHiKL5pDJb5jSzpmE35uEcWk8kR2DqDwxTyS06OFjh9ybN_rNAk8y90NJz7zaESyCRqwHGITO_CfVScHHuX_1G4rAuLDOvf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XicmtXUjo9pVFp2UG-sFHEtHHBXh_c4oAwSAzqIP9U1V9bBDG1oF6PeyGlVCGAifuRmYdxU7x0fWmx8llMdGTESpVlH7E3xKqcbi_YdIZi7VbtXZMyWnqL_gqRIJVC2Z8ilC2TJLifeDIhV0reonETYgCoWz7cDqN4J-D_i_xrqZLet8jbUcAFrtvuD0m1q9UYaBec8QymDaMW3bq3zVx6TbPT2fTBmGFzYd1N-At_XBn2Ah8lY29jFYYj6d9WQcupnEvns-R2WkQOyki1azdyoh28pG6CfygERDOm9xobtBujpTVoBLbJFk0Bx0mzra8CM1nyL265mnghH6C4650g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=WhrJj2L_J6UvFSPrNN7vexVyE6ZsFMHREAEbYmoM47J6V7ScuJkBIpQ5YTwk1ytXpTP-sHvm8xq_JNtoDLQ51_dbBb-rXni8z0KFby-kHCxzyKNSyFFtQPU94J-T4ka0roOd7a1SZGaa46I6Nj7nChAQxdRihKp-LkF5_bwbFSwFkCdyTHqMwNvuWNVDaat4wHXMmJQDCCpXh57azrUBD4UlAiZRlZMbhn66jRmkuRD7AnoO57mutl9MUVjOBT1dNks12tGhaaQ75Zg8cJF9zXcV6Nsrl_gEjoxvHh-VTiE1lsWtGrQR2Kw_dTRBpQ_9Fh2nUDUJrvOWtQ07OasDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=WhrJj2L_J6UvFSPrNN7vexVyE6ZsFMHREAEbYmoM47J6V7ScuJkBIpQ5YTwk1ytXpTP-sHvm8xq_JNtoDLQ51_dbBb-rXni8z0KFby-kHCxzyKNSyFFtQPU94J-T4ka0roOd7a1SZGaa46I6Nj7nChAQxdRihKp-LkF5_bwbFSwFkCdyTHqMwNvuWNVDaat4wHXMmJQDCCpXh57azrUBD4UlAiZRlZMbhn66jRmkuRD7AnoO57mutl9MUVjOBT1dNks12tGhaaQ75Zg8cJF9zXcV6Nsrl_gEjoxvHh-VTiE1lsWtGrQR2Kw_dTRBpQ_9Fh2nUDUJrvOWtQ07OasDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggLaI5gyWDr7Oom4el7LXNe646VU88zlmMNfvcPgQDT-6zAJt2F3HkfF67ouO2azoSGZBn79_rsMLlVlSUXIEtHL_aUekuJch8X1NgbmhUzihbD16p9UwC_RPqAPqjhX3AYJT5hbEQnn3dLdjRGmYD1iCSO9DZfoi9oEysO6ncTXABmlagPcmBqMLB1B1g3_kASlbBFV0Stvc6hnsaH9ByOfhPNXbjteM4BtsnR3JF5Olc14jVXe-gTDgJtM-GQRr11RWoTC8osOXAecZ1okd951Z6_mkOdsc6P18LGneMiNUz9UerzRjPKatdUkv4XwtR5YoC8jZxnWl_WkM-2sxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8ZlC3ydgIOqs6EUT5_JlAlZG7moEYT71VE49XrpRfZW1Tal3ce2tMPjM1lkX3qGxwLu1p2JoR3sy5SFqce0KDVZg99C7oUBOP5DmtHKsZ2d4Qb3_MjKd75gzDL_LP_8cFuwiQC8H6qXaCEdd-cAS5HWE9t3DMkOeXWV0tM8HtS7bytxTX10DRJ1Q0-cc2CneaQ30eNTZgaUaUNyBZfyBNLObxXen74zsHQyQhbtm1x8VDTX4vcPvbHaZyojdOmsVeSNQ8ZieGyJlUaLP6ufZx4TJPrCfmSBxxpz4jHVePd0moE-CjcXZwhoECmpXbSSj9VjAeEBjnDCO5eF6waCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aM2WecsPH0WHGhXvThzVFEewPNVDNRiscJPxWDxmEdh5qMVm5QEHO80B4Pt5PEGzUkkYRztBB0Xg6GuObM0khgaPl3yF9aIEP6odyzWmXI_5jZNc10C7c18ZtOyEoIwOdrXKt6L2cPU82lP9OdQnjxzwar9XHK1u68HCyKdO5CpFLgCrDH1EwXdpMlsi_ZYLSoidZoWy9jo70wYbsfpfYshn4dtgTOhtJ5rxNZVWIPPqZqWg-xT5bRaIrwAiXbOoq_viOyMOCOCNY4jgTq8Ib72tfz6TBTDDgc6cRy6EGvs-6XtTW2ATcdxcBq0Y9xSmJMG7nuLkQN-Gdz3ihoM2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e964Af8ynPr_IjTO_jjz9kcFseeThpgoOZFxEtJdKXhTKPlKfH-2nvCyTswxhGg4Wg4LifgYEF9zP3C_nW2y07DecTT3s6gzrFqgwvRxq_1_KguIp5UgPP_DqxcSKZMRtLbQfmmaQSUzDXYgLUCr-oaLlpx_QnyjBuUDhRyewACR54WtC0lb1sV0sII0wAyJzraqmdWap6CUX_AOUiw0Zp_eCOqgP8Hn8FJE3I9GSMGJxmBRlQwXnFvRzHaCtAAZ3_VlG3-3A7A-gR8J7MST4YcPxlpPIUZzzsThT5CjRew1FHDDIJVNPiJBlTsuTX8jWEdvODsoRPHcmkAkOa1irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu-BMh1Q3e_FTkqBKyWCf8pb8VQA7Z8kd6mTmXwlbnvtRLm5Q-JF9kJHc_BVJK7yj7Vo3kKELM7WHLqMkqzcKphDGeA6IE8cIknrnZsadcCACRGoyHJdK8MeygA8YRwKWKKb75Rp6aYeLRhJpTy7FSrFEDdt_F7qYyZO3cWE95qSiOXgSspShokbgPk2KXPuyQSo022ApVGMdgE3Wo4RvzLhbc6Jz9qR2zzN3LMBdUSzb8oOFTAsX0PxW-amzn4BF7tI8nbWTgar7S-yoT26vtiJXBz7ERynWUfL3JIB0QPRXb6dmE3ote3MDKOmS0x4FmGCC6MKlcGpkISj7yNyFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=ebBn1rogFccqHgGWy6IxTiIA-CqWJVYrS7CgpbHDNuIYai_posalDfkD15tr5A4XfwN2QYRwYbU0TaHX9K6PK-AVtFvyJHMks3-PBUaxwrWvB_EdtJ2NiSXaW-thLG5TtJJNys7tugTa0yx1uJnQbG2zOy6kW16tsibyMHSZak01P0TccWP4mXd4HhiVqm2zmHYAl7cm1NdfRWZLyxAR5AfoYcrQGnYzMMArQ0nLIzJ1LrXKrnrVKR0YbsiRmzODzhks507Ii-pzgfkjEU4Sjjvi0B1bHSIhDwe1b8kWaOGo_387Xbt3QtCBDL39tYI2ASHpuTsOyKau1wLHkGhywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=ebBn1rogFccqHgGWy6IxTiIA-CqWJVYrS7CgpbHDNuIYai_posalDfkD15tr5A4XfwN2QYRwYbU0TaHX9K6PK-AVtFvyJHMks3-PBUaxwrWvB_EdtJ2NiSXaW-thLG5TtJJNys7tugTa0yx1uJnQbG2zOy6kW16tsibyMHSZak01P0TccWP4mXd4HhiVqm2zmHYAl7cm1NdfRWZLyxAR5AfoYcrQGnYzMMArQ0nLIzJ1LrXKrnrVKR0YbsiRmzODzhks507Ii-pzgfkjEU4Sjjvi0B1bHSIhDwe1b8kWaOGo_387Xbt3QtCBDL39tYI2ASHpuTsOyKau1wLHkGhywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=hkYEohTxEWhP9OWFRfVG_3wjvF-jaqp2wMYPRdnxDWwYP_RWcKqQ2wjsUUAG5KuPbGz5lTxU_ovAVhYiiNQntwY_uC7_pJdX6bh0IlphDvDGgbIH5W_LZCXtwW8IF4_tGDO-FeUU5sHkF98Wu2kPpDtdTxFkHTnua8h7yuFKcPf3MgEBFlCoLOgowGf2_XQVblGFbi1wfRa-NTGCaz1CGrDNQJpTf_DUMiA0al9KAGllC9ywrhg5KOdi7zO9oDSSm6qRo0zI4pJyRG_IgZ5AcaZNwq64jWip5__IX5pN_jk5mx-Ki-gx5ihUGuwWPfaXKIn7xFUoChY24wXrE4slDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=ggNI_qrR2Ywmq2WJS_w-PRZ8sfC3zBTkTNChhDFBehXIySBq6ZhnIN_WPwQrHAQRUwSeHK2wBFz43plxQHOGX0ZgsWFjgbGcN8YuHfbHy8nVAsWslI9Upy4ZLV2bZmlYAqEcImmw-hs-1H2n1p5SlLT4qRABn544S338qcdozK3F0hsxZ9FCG7i6oKgYdF9_vZuwd3h1QM_gTOGZ5PCFN5QPnjQ306I0VgJJXc_xOMazyariSV4_ad1u10hVrECtgRIXGaTgarqaR9mG6YownreG99WcZd38_0ddx_X-cOcgaCj3CAUQCbjT7iICkT09VnSFMywM-2oU7f9RsqZK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=ggNI_qrR2Ywmq2WJS_w-PRZ8sfC3zBTkTNChhDFBehXIySBq6ZhnIN_WPwQrHAQRUwSeHK2wBFz43plxQHOGX0ZgsWFjgbGcN8YuHfbHy8nVAsWslI9Upy4ZLV2bZmlYAqEcImmw-hs-1H2n1p5SlLT4qRABn544S338qcdozK3F0hsxZ9FCG7i6oKgYdF9_vZuwd3h1QM_gTOGZ5PCFN5QPnjQ306I0VgJJXc_xOMazyariSV4_ad1u10hVrECtgRIXGaTgarqaR9mG6YownreG99WcZd38_0ddx_X-cOcgaCj3CAUQCbjT7iICkT09VnSFMywM-2oU7f9RsqZK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu2MB1VTe4nAKMJQFyBHhDqlrV0lFaYw9LAzOIqFWylCyaYQe6RS_9GQAtMP40TTQH3_pJbO9fBvCCxdZDbSDoHzrrOIh3fIC1YFP_jlQJfvYLccsBAgEcGFjcs5Lv1V2Oniob9dKTQFmRJuZPhhxKmZVwAWN-4M5WaovoBgKg3_qQeRP8s_9hF693woBK60mUK0kFZiMVshNhBvEqFJHyoEl8DdlemGl4-FoRq0-v3QIQZnGSxsY3WkyxUU-Ndv6lvJaU3JIsb7eWlvHhTBm5h2G9lnoemJWkpYMGL8It-eFDjW9_718uT00gx0QCsw1fjybcC-dOhY1av6OpLySkr8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu2MB1VTe4nAKMJQFyBHhDqlrV0lFaYw9LAzOIqFWylCyaYQe6RS_9GQAtMP40TTQH3_pJbO9fBvCCxdZDbSDoHzrrOIh3fIC1YFP_jlQJfvYLccsBAgEcGFjcs5Lv1V2Oniob9dKTQFmRJuZPhhxKmZVwAWN-4M5WaovoBgKg3_qQeRP8s_9hF693woBK60mUK0kFZiMVshNhBvEqFJHyoEl8DdlemGl4-FoRq0-v3QIQZnGSxsY3WkyxUU-Ndv6lvJaU3JIsb7eWlvHhTBm5h2G9lnoemJWkpYMGL8It-eFDjW9_718uT00gx0QCsw1fjybcC-dOhY1av6OpLySkr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=ozC3UvcefdIbj5ZH1k9v-CREC1Gy73TbTErl9WmWacBq8SCBrsuwoSGcMj9-q-Q0a1hHIU1bYZbRMmEVqJWa1vh9M6-0lh3d1WSFbN1M-HKZNNpkZkkF4dc6v1yVpWBjrnGPaOudhYefLe3Hf6ElSJnMli557ZdtVywHEtl7Vy7Qu22ZX40hJahqX4Qd4E8y0FpTFyO9r5g3itttAWAhmZgYjtyX-3ARdUR4yXOHdADPECB5syyE6wB32dVKwgJLaJCd3WaviZWGyu2-jk3EkR2YJOpyIG130ox63LyS1ZJCT67mHpBR-86pgoGeiIWZzgLNRn_SNZtMDTp29xb0rb8psgOaaBFZ9Q-_ov0nwKYLJx-DM6-TTf2ej5NOz3W4fcxtQN66jAOfFjNDqhtHAmGEWJGwvdib2FNTmTd9GP5Wnpxn2auYYz5CzOZfemyrrMv2Tb5Fu6AgPjsQFORgDDQzwxe6HyeaIpus6DhWTBaigylw-R4QxtqloUPC7QH4j_2czrSyAAIPZtTMzXwF87CYfWKefiN2gsZHKjDgfF_5hBbuK1LVKavi8ZPcBobQ91N9ddXMLRbDx2loMfY2g8Ehyc75kMvTIBIrQDqZ0WuvyQyxleTZIwecus5mejImzFC8bah2ij6GIOlkJ8HiQf4fgZo68RmAZm4XsH8BXCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=ozC3UvcefdIbj5ZH1k9v-CREC1Gy73TbTErl9WmWacBq8SCBrsuwoSGcMj9-q-Q0a1hHIU1bYZbRMmEVqJWa1vh9M6-0lh3d1WSFbN1M-HKZNNpkZkkF4dc6v1yVpWBjrnGPaOudhYefLe3Hf6ElSJnMli557ZdtVywHEtl7Vy7Qu22ZX40hJahqX4Qd4E8y0FpTFyO9r5g3itttAWAhmZgYjtyX-3ARdUR4yXOHdADPECB5syyE6wB32dVKwgJLaJCd3WaviZWGyu2-jk3EkR2YJOpyIG130ox63LyS1ZJCT67mHpBR-86pgoGeiIWZzgLNRn_SNZtMDTp29xb0rb8psgOaaBFZ9Q-_ov0nwKYLJx-DM6-TTf2ej5NOz3W4fcxtQN66jAOfFjNDqhtHAmGEWJGwvdib2FNTmTd9GP5Wnpxn2auYYz5CzOZfemyrrMv2Tb5Fu6AgPjsQFORgDDQzwxe6HyeaIpus6DhWTBaigylw-R4QxtqloUPC7QH4j_2czrSyAAIPZtTMzXwF87CYfWKefiN2gsZHKjDgfF_5hBbuK1LVKavi8ZPcBobQ91N9ddXMLRbDx2loMfY2g8Ehyc75kMvTIBIrQDqZ0WuvyQyxleTZIwecus5mejImzFC8bah2ij6GIOlkJ8HiQf4fgZo68RmAZm4XsH8BXCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=qySj8yXGBPsK5Gi732aScPmFnvRYsbzuf2qt3btj106I-KkiT23FEDGo21ihBl5JcTFZX5w8W5SH0sqpUWIttzdOZ_w6oEcBL2A5yxHk01T8McW1Rok4pUHDi_sYzBSwJa34OTzSxvzAeiT69o2zu6RksfkUH3RD6Eo56ZcGYgsKIhrCjEtAysMjzYruL7CsjvmiYI9kTX_guRfOeeC8EYZ1oC57lmhYfKHYdquwkDtLfdonhZy1tQTyjEfxw708oBV8ysGmtd_vwz05IfUij3tfg_vJre9ZRveT7LUSK3xlneAWwRd2DYRGz7VG4ugE2u4h_5M8fdIGu1g1ze04Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=qySj8yXGBPsK5Gi732aScPmFnvRYsbzuf2qt3btj106I-KkiT23FEDGo21ihBl5JcTFZX5w8W5SH0sqpUWIttzdOZ_w6oEcBL2A5yxHk01T8McW1Rok4pUHDi_sYzBSwJa34OTzSxvzAeiT69o2zu6RksfkUH3RD6Eo56ZcGYgsKIhrCjEtAysMjzYruL7CsjvmiYI9kTX_guRfOeeC8EYZ1oC57lmhYfKHYdquwkDtLfdonhZy1tQTyjEfxw708oBV8ysGmtd_vwz05IfUij3tfg_vJre9ZRveT7LUSK3xlneAWwRd2DYRGz7VG4ugE2u4h_5M8fdIGu1g1ze04Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJUruNhBS7mK5xUqH_yfBujEyA07huYkUAlyM1M_A3SmsXBWLPbJelZXrM0iTLKUUGMeLQqyQRIDMA-1Mfx9hf-cFbiB21FdmZcS_PwXbzCJhyxvP-H3CFVPmQrwABjlH-y50u12ExGy53x8LgvU2m0mQkbx1vL12I0X5a2ahnqT9bYCVzoRA97KgC3cw-WtRKNQ6YXkS-d1ZyW306mGgQU6uD8Bpt-wfGo-GtPiUhdMvQwgoUZATpUN-48MkLpYrvZzGoYRrS1k9Lx0vlrR9wUI9_-6FtSY0yxqVMcMY3AXvvI8-K_7vQrJnB1ATzCMlWKyB9EK7bZ27hpw9i-HNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=dVDkLdAR4VbGb6w99DnTgKk3Tb189v8-mfa-sj49oY6AhG06r-WSiAv1M3kFFk3diFoNjYkAYY0yi4r3nbhKTjGxYHkci2Gr67e2SR6u3Pg4NNto6Yf4m7LEEJAUeYWC7vszxWO5c0fxYWz92tlGWe76WgSkivxyK2dqkqH2TkGWRLm_0uD2X8YMzt7mnL9Hqst0qbqLLmNtdw-dnkXLYHXh9gIigGD8dIPg5pJze3N2O46BeWdwwK_Hq1vC8VbP8Tu_L1jCcb5sZMXIAhnLT5PpmGY4iwclT-375ig45vKFL_WP6VpK2nbTa3uXncCUXSQZD3GMTblLeEL0P1GNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=dVDkLdAR4VbGb6w99DnTgKk3Tb189v8-mfa-sj49oY6AhG06r-WSiAv1M3kFFk3diFoNjYkAYY0yi4r3nbhKTjGxYHkci2Gr67e2SR6u3Pg4NNto6Yf4m7LEEJAUeYWC7vszxWO5c0fxYWz92tlGWe76WgSkivxyK2dqkqH2TkGWRLm_0uD2X8YMzt7mnL9Hqst0qbqLLmNtdw-dnkXLYHXh9gIigGD8dIPg5pJze3N2O46BeWdwwK_Hq1vC8VbP8Tu_L1jCcb5sZMXIAhnLT5PpmGY4iwclT-375ig45vKFL_WP6VpK2nbTa3uXncCUXSQZD3GMTblLeEL0P1GNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrpGrM-F0c1Um87FNJd2Lc2UV8gO3P1bfx-lBRQCv-BB_zQ_trXsHUi99rUT77lKxpEmD_CEwCgIVBKv2g8HC_we278XWIcVAh1qof7HXYsBURiLsQqslOPncEZq2N4mSomKzjJ-McpNz43rZFnRMmD9XAi7yJxmKQ5IooEHCgdnsgi5Ks7GfMwW1EK6A73SCdXoV5WJai7Vx42U0ipVvg3u-x6W3JpqlPVZVLeTzsat47FBEVyrXDLhNYVbVvhPVm-c3SNaAg3tz7kyRrewrIESGvVER-c-wXglCB7TSQ7CQ5b1mt_8H3MThoLtByorIGDJNB4IqmrvwnW8L5yaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=g0oOPVGU8v7Dq6c7zyUm6PlZMEPclmR14r8PnLhI0scJyz26WqFN5vz78SP9vGLeCebamZWhS14WP2Xg6d0u5CLqQEmrE53TkfJgvqH8WMQQ1QaGsohFxYDNzW2ReyokCfnA_KtG4a4Nkg3kCS0E8CPjMJmcFT3I1scTunOXnNkoW9GuqIO9tdvfngIvzbdZ1rvDXV2Nrz54Q2scGvFLGRhRgWmy6lhjs9HeEj6WQOueXt-8-sM33X-BXGbglpSmcj7epl1QbGMDHCKPrUNBbw8SdulZCqW6OvNp6DEXvDPsBs6B1tMNaz2_C2BwA0_YFKo3w9R9DZL5ds2kqGsCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=g0oOPVGU8v7Dq6c7zyUm6PlZMEPclmR14r8PnLhI0scJyz26WqFN5vz78SP9vGLeCebamZWhS14WP2Xg6d0u5CLqQEmrE53TkfJgvqH8WMQQ1QaGsohFxYDNzW2ReyokCfnA_KtG4a4Nkg3kCS0E8CPjMJmcFT3I1scTunOXnNkoW9GuqIO9tdvfngIvzbdZ1rvDXV2Nrz54Q2scGvFLGRhRgWmy6lhjs9HeEj6WQOueXt-8-sM33X-BXGbglpSmcj7epl1QbGMDHCKPrUNBbw8SdulZCqW6OvNp6DEXvDPsBs6B1tMNaz2_C2BwA0_YFKo3w9R9DZL5ds2kqGsCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=ixLcESmGlG7O5Dp6Zuc8RAkjMnlS__i3dgq6tXIgybHiR5BpmGXbdNWZjmBxYPu5wZxYCC1ULZxcaBBmP3D1LeiXjT5eGqV-eZAvjpQZrCND4XKUkfo-PJdVh1gaI_x3BQ2bR71n8Xnn1MU8tfDVfqPaKw2HGLTcp_ViLsz_rwd6mJ_vkOzL7obLkikwrlK85Ay1xhJR084CxON3iwEiWQD5h9a4EwW1vpEO_LmbIEedjkiZZ32WDesauJH89o6mXnRqWXrj9GYRvP-GhZ9ZhTBu7XK3sBmrUjEafcLWn0hdH67JfOnc-6OPDZwQY2o1-va6a9XkgmQDN_qGGvNmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=ixLcESmGlG7O5Dp6Zuc8RAkjMnlS__i3dgq6tXIgybHiR5BpmGXbdNWZjmBxYPu5wZxYCC1ULZxcaBBmP3D1LeiXjT5eGqV-eZAvjpQZrCND4XKUkfo-PJdVh1gaI_x3BQ2bR71n8Xnn1MU8tfDVfqPaKw2HGLTcp_ViLsz_rwd6mJ_vkOzL7obLkikwrlK85Ay1xhJR084CxON3iwEiWQD5h9a4EwW1vpEO_LmbIEedjkiZZ32WDesauJH89o6mXnRqWXrj9GYRvP-GhZ9ZhTBu7XK3sBmrUjEafcLWn0hdH67JfOnc-6OPDZwQY2o1-va6a9XkgmQDN_qGGvNmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-oWuIs4OJemsvJ3CUkkCJ_Ei-CVkdtp3AlghU1Fs-_sW6vhIW3QBYK9UmV28wiBqG-kOAokk4VqgmFBmwkIfsQUKUpCnHOiVnlWGFUZqo6NzQNvW8iAW6yDJUrrjvNRDgA9qLKoO3hy9IjQQf-E412iwsInh2BNgqvMZ7Q3horkhy_kic5uwZRFksK_GTJuFfg1LPUgEC_Sjgjmj2id2XHkTwtIsHtvq-3S6kXT2cG9e0pmNeu_WU3k3c9b_kWBmRZa2p69T-AJqf0t8nlkUTIj6V476wwLoKl5imf8fwvLomHkC-fCeiPVZNhYedv5zim-Dhka_nuys86HTGjOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=GcGqZbZuuOzQFxyZfUOiImdiwpFBiMk8i-ppBgl55iK4ht8pHn3IrnjK82Lz3MD39B65F8KmPinXcg3P87xE1BeRjBLGY9C49IMCUiR6Y808qZWkuy7Q55sBDgCK7V2YILPO0iFx4Ak9GvQYHQy6NLMPK1DNXHHlZ-peyuLajec0u3vWhTZN1o6TjF8JwJ8QUdCHtUuaAtYW9XI4-mydS5_biUlGIBgVHvQl6MNQAXLr5oRg_QQssZw9lYFC063Hoh6HTeMKV6oNzGD-1B4vDhAX2hMTvScIO1Us6U84DiX3BBv2_dc6jWFeI3yxuPAVEjxRzv_bCGaYtt7QGdW-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=GcGqZbZuuOzQFxyZfUOiImdiwpFBiMk8i-ppBgl55iK4ht8pHn3IrnjK82Lz3MD39B65F8KmPinXcg3P87xE1BeRjBLGY9C49IMCUiR6Y808qZWkuy7Q55sBDgCK7V2YILPO0iFx4Ak9GvQYHQy6NLMPK1DNXHHlZ-peyuLajec0u3vWhTZN1o6TjF8JwJ8QUdCHtUuaAtYW9XI4-mydS5_biUlGIBgVHvQl6MNQAXLr5oRg_QQssZw9lYFC063Hoh6HTeMKV6oNzGD-1B4vDhAX2hMTvScIO1Us6U84DiX3BBv2_dc6jWFeI3yxuPAVEjxRzv_bCGaYtt7QGdW-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=TwD3vq1qRu4mz6pl6KV51lD8Gad4RKqjgKa9SOGAoou3KwTdNQKvXwae1AqZI2XCD3ROShCG1lCzDeX_DYRZxbR2EJkHpLk1OVRr6pCTlOIEq3P0IHb-OmOh0E49ct_CDcGkqgziQX0evlfJKYpMgLTgiotHGRUto-IHAWiaKqTb1wWz44qzez-y839X3jdYMIHJxzCdCcIVb1Kk2ZQn2irMFikIakKMojsaVc1UJEwbJjcTcgkFYPqpmWmlpbo40FhfG8YX0A9c0TUebCxjeu4A4Z_H1-Cc-69FtNsPJVnddlPoO8oqDArZr8fNw5mD2vl2CnFOrBeDTMJNZZNa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=TwD3vq1qRu4mz6pl6KV51lD8Gad4RKqjgKa9SOGAoou3KwTdNQKvXwae1AqZI2XCD3ROShCG1lCzDeX_DYRZxbR2EJkHpLk1OVRr6pCTlOIEq3P0IHb-OmOh0E49ct_CDcGkqgziQX0evlfJKYpMgLTgiotHGRUto-IHAWiaKqTb1wWz44qzez-y839X3jdYMIHJxzCdCcIVb1Kk2ZQn2irMFikIakKMojsaVc1UJEwbJjcTcgkFYPqpmWmlpbo40FhfG8YX0A9c0TUebCxjeu4A4Z_H1-Cc-69FtNsPJVnddlPoO8oqDArZr8fNw5mD2vl2CnFOrBeDTMJNZZNa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFILqq6aX5zPIAJJzlDhSV4TOAehlJ692BVf6L_3gu86nhTVipqj8ynFjDC_r9BKL8F4ibta2JPlmJ3mYdm9TvsF2DOn9w1HyBQc7GM3D82ECLvJqL1YeWy24GxYkevdiXe595U8QZBkQBNDrbGEJK9Zfi3QAVrIk5BqHD0HG9CIp4KsBPU4dpdQv-cmWJGMpUc0cGrXiebsdryuTR4Upfv_j_VTrmzwDW2ajSs-LdeBc6kODaMSdFBD4fCqRGlmjKT_LVK2kLIy3IBW2ynzMdgBGPZ6jDrbdrHStKbMkZhiWZkSxMAtnQg0barn2HZ0kt-N5NdzwpM-0D6IxsEbOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaVBKfvhOSQpQVbzD4jA5zT4GG2SDtqDpm-r6XHuP1ZLO_ClUZhy0mhkS4jUJAgkdozGXSOFO1XtncwD01YzzjZvPKk0KqP3qdzSJOAd0pDF3HVMigHFq8IlYdQuiWy7mfO3TAatQa260dNXMTO3vGmas4JH4YPZkvx2KFLR8FxjngC_089d8e-TR1nN7zp3sTaW5A90yrBkfi1dl6SAqONG_zvX5bAj7wWR-Rkzl9ukek8JNrGXKwACJUGRRvopbF7tqjgXZeHfnEyVdAaZCXPoB3Ys2UVahnmaAEoq82HFKDqz1RcbuKKF0sLw0CPrtxZIoFdxNreyslZ0MPhIPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh3IqJpP4-6D34rfmsGzBEgnpG5JgKsTrirNfx2DK1LBxIwSXFUff81SYqSiGnWkfOsWQQ4hqTyNWfiYF5U5oJ5vb4VkAwyoqrma0dC29AwtLII8IKxVew-9RFq_wPMCW9bQnpUe3zBRGUoeuxxdC6h7rHYneBXhrQhYOl_fTzTpK7RNRh1e4FsCZP6YhhXSiV-OZEQYzTvuT2liOgSoYRA0w-ATKZISivnV_rO1oPMGxKNP6GR0xyRdPPh9Ivw9S4UG1bTtDDnxw6PmuEeBFopeg89877FbY8TA81uizfRo21r4zx0h6xdJIMFut7TdExkVclWDTdqJd2Tac9D0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nk8_idtOod5o5pTgX5tnwimNs_GzIruP2rA-ZJ0mpOjHMyflxPoipVN8ysiJV4ZaJwCt7qS7ujSS_TpWFxAxQ7Yu0VsaiBTM6ovHZNvjw26GvZM7hgjS1dx2A7bSXVbJnzudlPPuMaWj3BN5pF0bf4DnxDGiSwvul5gPj1uuuvsvteopYxK_b91D8NI8aJd6lolgcX3cLTAsFgvij_F6tQlFcG1E2YChdSGehryxNsjn1ct1YtFBARHxINBUcD80vTKfl7TmYhhi-i29jifcN8PH7rc9uSXTKl58g0Ac6m83vk55LKeKkCGf8pccJfanXzhenk_lln82Sd0KLvsGFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=VViugU0xVoVDWezTlXfZEOaEXblLk5CRSzZ7ZS2COZyJFnJ1X9bLS5rdrmnBgkKkZA14hWn-tfg7MZ731loJkC6NROk_4BD2B7cH8Y75nJ6DEp3cwKYRiu-8QcwI0OW89UaEviWL9DvnQdXkUSAH8HaAqAIyMwGA55NIcbn-yXNz66reYhMr_A_-DX2JzeDmp6HHKRrGrXRXQMoXyI3CcnPjgJtF9FSeQpoDmYbqScjO8Y0E7ZulY93Xtgvo92XMppwTqZwStwqtLpPFYAtFJXXjsrvHTDWJuVwJNTG6VujjWv-oz4JNUg9FhTruIcEIGQaG0zIdT4_LBSi01Sb4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=VViugU0xVoVDWezTlXfZEOaEXblLk5CRSzZ7ZS2COZyJFnJ1X9bLS5rdrmnBgkKkZA14hWn-tfg7MZ731loJkC6NROk_4BD2B7cH8Y75nJ6DEp3cwKYRiu-8QcwI0OW89UaEviWL9DvnQdXkUSAH8HaAqAIyMwGA55NIcbn-yXNz66reYhMr_A_-DX2JzeDmp6HHKRrGrXRXQMoXyI3CcnPjgJtF9FSeQpoDmYbqScjO8Y0E7ZulY93Xtgvo92XMppwTqZwStwqtLpPFYAtFJXXjsrvHTDWJuVwJNTG6VujjWv-oz4JNUg9FhTruIcEIGQaG0zIdT4_LBSi01Sb4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=C071FOTjn3DOg9bzXPcmQrxxL--Vo1CIXpIRaE4LRFK4Qr-8N9QZP6tG_-iOsFfHpBzxQjjx8W4Fc9HAxDnIS6RnOCGXtLeOZkO6UVULeXHF7uqXUqs72ytra6v5naEVdW1fdw0a-eDT_k32sZx35jTmeZ_8cgrrdxZNYxJxjUU9r3l40XH3c5xkY9AaLlCIsuMuAr31vW_CEveu3SRi0b-mvU45lJK6ahIc5TB80UUsJHKpNC70OiRMVN4M-Gp9SroQRdTga8rxKxNjdDM8HQRzakXfGlG6vi9zIjtTaIiUcWBM_bhAz1LY_9_sld3iVeEm-JnOt16vH6V7nHzuYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=C071FOTjn3DOg9bzXPcmQrxxL--Vo1CIXpIRaE4LRFK4Qr-8N9QZP6tG_-iOsFfHpBzxQjjx8W4Fc9HAxDnIS6RnOCGXtLeOZkO6UVULeXHF7uqXUqs72ytra6v5naEVdW1fdw0a-eDT_k32sZx35jTmeZ_8cgrrdxZNYxJxjUU9r3l40XH3c5xkY9AaLlCIsuMuAr31vW_CEveu3SRi0b-mvU45lJK6ahIc5TB80UUsJHKpNC70OiRMVN4M-Gp9SroQRdTga8rxKxNjdDM8HQRzakXfGlG6vi9zIjtTaIiUcWBM_bhAz1LY_9_sld3iVeEm-JnOt16vH6V7nHzuYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=vqWyT9bzcAoIO0cm2HVsXGBNImXFfSu50MHZM7N3Gx2j5CA5B8dxX_rBTqSHl20SQAzSpqJV3aVyCB7v0VYua_mMy3eiGm_S4QfqFwq_doqHyDX9P3vxfuhib0i4RL6zgqzjz7op7C7Fbrjn1zvLuopJGRbzY5Jt-K1CZZkJJIT6TypooPXhinsQ7-5C3EdAkB_AoIKEmILyyat5u5W1rhdBMxZAVUOssOxA-JvOiD1Rrfvi7R437Q1OeorPZPGYiiLBfSdkDiOgxhp_sE5oIS7KJadAdhMJZtCbklfRQpgrlizIS8Rvem3yKDomT14_eU50JyG0YC0MD2yChz67Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=vqWyT9bzcAoIO0cm2HVsXGBNImXFfSu50MHZM7N3Gx2j5CA5B8dxX_rBTqSHl20SQAzSpqJV3aVyCB7v0VYua_mMy3eiGm_S4QfqFwq_doqHyDX9P3vxfuhib0i4RL6zgqzjz7op7C7Fbrjn1zvLuopJGRbzY5Jt-K1CZZkJJIT6TypooPXhinsQ7-5C3EdAkB_AoIKEmILyyat5u5W1rhdBMxZAVUOssOxA-JvOiD1Rrfvi7R437Q1OeorPZPGYiiLBfSdkDiOgxhp_sE5oIS7KJadAdhMJZtCbklfRQpgrlizIS8Rvem3yKDomT14_eU50JyG0YC0MD2yChz67Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T1JfetxfueuDv6DauW6YpGRdCydme22de2J6pot1loSwz6LlGT0DlfC-52wxAMVCFJlKfsNZdpizipoYud0S7QJa9vyY6NkjEx_O31Ef3O6OYwUqKKPNUqg6LGDq7rwsVvcIZn-wyylstrsr2cdg3N_yQlS91Ea_y0skLdO_niMu8k5Wn2J1qBIScq_E2PEhXs5DAhrX08TlDKHg8hRPa1NSwWZazXU1E_QuSIqg0LHCga4oAEToUtsaPibxW_PoBifoEt9zxEH2plBtU_XVEC6YYugfz9-yPZHL6_9k7TR4IARbG6wWJJrXZap_uF5n_kgu2igXOjf2-Ew4xtqdvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T1JfetxfueuDv6DauW6YpGRdCydme22de2J6pot1loSwz6LlGT0DlfC-52wxAMVCFJlKfsNZdpizipoYud0S7QJa9vyY6NkjEx_O31Ef3O6OYwUqKKPNUqg6LGDq7rwsVvcIZn-wyylstrsr2cdg3N_yQlS91Ea_y0skLdO_niMu8k5Wn2J1qBIScq_E2PEhXs5DAhrX08TlDKHg8hRPa1NSwWZazXU1E_QuSIqg0LHCga4oAEToUtsaPibxW_PoBifoEt9zxEH2plBtU_XVEC6YYugfz9-yPZHL6_9k7TR4IARbG6wWJJrXZap_uF5n_kgu2igXOjf2-Ew4xtqdvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=LPPu8ss4eGNViQT394o6JkGlp8qmIodJWbmyGEAteY31Nca_5R9QjDQSviL7bPx012rpTRnvqNtMx_gX8GHylq6uOAogvBwrK18bZTaDbmQ_X_bKRtGc5Me9810JFELNDq1Cd5bZD_Xxlv1fVd3oXvmwfPuEp0mnZrZiD4vGBES8gFBVe-8ojEP6CEGuObMV2EeHwCjAZCCObL_RvPUKlabjfAUmjvwbkR4XSai8lJepckILzMG8kXJ7bxI_2wmisyYK-nzm_xrZdDSE5doj1PziOA5zz2TWzZHLfWWDgpAzAVwDPMrziayKJgrvLpYs1HajqJ3sb31pQaotL72hGJlIEGoF3VW97xwczXKKDzV8fRfiCQLlVSUFLhqkzj0rAEkhFpOVmWMYfSuCRGNrz4-tITUglVEXhE4bS2-8OscRHvCIwA0S7uSFiS_r7gzqwyDNz7wZ7P2F05SMxS6LQB61kq4YnaXLqEYKWFNrUC2lnHFha99xTB87v01JjQSbXI_-_Dh58rj79v_ua8WjsVaYX9jcvizXFXK2tKShQnc9nGEi5AxE3XknzWgNInum15GXQrbB71Al307PqHZ5gCqQ3xEMZMVGAdk3RBgnN8sGAZ1lxLJ145t8wSJC9R59CYkNh0EcL-DSghfFiZNJgy5K6Nx2ycUEdyNmt63Pku4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=LPPu8ss4eGNViQT394o6JkGlp8qmIodJWbmyGEAteY31Nca_5R9QjDQSviL7bPx012rpTRnvqNtMx_gX8GHylq6uOAogvBwrK18bZTaDbmQ_X_bKRtGc5Me9810JFELNDq1Cd5bZD_Xxlv1fVd3oXvmwfPuEp0mnZrZiD4vGBES8gFBVe-8ojEP6CEGuObMV2EeHwCjAZCCObL_RvPUKlabjfAUmjvwbkR4XSai8lJepckILzMG8kXJ7bxI_2wmisyYK-nzm_xrZdDSE5doj1PziOA5zz2TWzZHLfWWDgpAzAVwDPMrziayKJgrvLpYs1HajqJ3sb31pQaotL72hGJlIEGoF3VW97xwczXKKDzV8fRfiCQLlVSUFLhqkzj0rAEkhFpOVmWMYfSuCRGNrz4-tITUglVEXhE4bS2-8OscRHvCIwA0S7uSFiS_r7gzqwyDNz7wZ7P2F05SMxS6LQB61kq4YnaXLqEYKWFNrUC2lnHFha99xTB87v01JjQSbXI_-_Dh58rj79v_ua8WjsVaYX9jcvizXFXK2tKShQnc9nGEi5AxE3XknzWgNInum15GXQrbB71Al307PqHZ5gCqQ3xEMZMVGAdk3RBgnN8sGAZ1lxLJ145t8wSJC9R59CYkNh0EcL-DSghfFiZNJgy5K6Nx2ycUEdyNmt63Pku4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=v6YGxfqxvnlh-0Tg8piV4mMkunp-m7VhnzsQows2ix8z2h-rWmZjlvKY-ygKg1EpZVmsGF-iEJCpEjkws87zb7DgokaoWgGCjHYmdwsACycEX6wPeIdjY3gT9RD0mEoMTFUpIzv0t5lQUhU_HmjhvkaMYOB4_RB0pfmbV3NkrXKA6VFMyy13IkqpKJQb3PYgz0cMyYMcKyNV06eK8sdYoQdZ2f-2pgFPSOWpC_eHFaHQXXgjwLALdAuqxSBmz9ru6dXYC2QunApc_ayOVNQ0rhdMKDeVv6hSULbpfv5UTJHuR2xIskapOKqKfR-IEzgyXYGkYqBYF-DZLwEW0184Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=v6YGxfqxvnlh-0Tg8piV4mMkunp-m7VhnzsQows2ix8z2h-rWmZjlvKY-ygKg1EpZVmsGF-iEJCpEjkws87zb7DgokaoWgGCjHYmdwsACycEX6wPeIdjY3gT9RD0mEoMTFUpIzv0t5lQUhU_HmjhvkaMYOB4_RB0pfmbV3NkrXKA6VFMyy13IkqpKJQb3PYgz0cMyYMcKyNV06eK8sdYoQdZ2f-2pgFPSOWpC_eHFaHQXXgjwLALdAuqxSBmz9ru6dXYC2QunApc_ayOVNQ0rhdMKDeVv6hSULbpfv5UTJHuR2xIskapOKqKfR-IEzgyXYGkYqBYF-DZLwEW0184Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=Q-GDV41ep1cUTuK76d0EID9qLTpGU6aW00KuQlNd9QeGlurCzBee-VCpSqeFOzzLPESdOVYWnudsDGrXvD2llpFCCDlN6lWmRAD-GZLDgOCS2Vr8qh0E-8qbpweLvZvOxO4WLP4FbNJ5rSD8rp-04iVBfOA96H1LV5WA8sEmXCY9K4PYzS8wLzyher1h7PYFVCX3vn2a0hbngLmtEQE74lJb0QV2rGFSzaKZxUkoXvYpFw8hWTPRwJPlDGHQPTf4tMnaFlRkMgxaP9HJcLxRE_bDXFARMss6Phm5XBWmklnXi0lxmB3KXLS2v4Bo4uaLI6O7w0VpnWriq25YEHB_jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=Q-GDV41ep1cUTuK76d0EID9qLTpGU6aW00KuQlNd9QeGlurCzBee-VCpSqeFOzzLPESdOVYWnudsDGrXvD2llpFCCDlN6lWmRAD-GZLDgOCS2Vr8qh0E-8qbpweLvZvOxO4WLP4FbNJ5rSD8rp-04iVBfOA96H1LV5WA8sEmXCY9K4PYzS8wLzyher1h7PYFVCX3vn2a0hbngLmtEQE74lJb0QV2rGFSzaKZxUkoXvYpFw8hWTPRwJPlDGHQPTf4tMnaFlRkMgxaP9HJcLxRE_bDXFARMss6Phm5XBWmklnXi0lxmB3KXLS2v4Bo4uaLI6O7w0VpnWriq25YEHB_jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=Ly1C0Ce7xERGQP7dz0X5rZz-v26B-iWndNONQeeN_OWgHP5HhYD4r7rbXoXjqTYsCHwYYVvahU1AxfJBDeG38N-ttn-9lQ2qKDCn8oU8-j_LPvsIesvmD-_j2i0MRt1V5DHBgsUnB-R4iYFRIkArNwuuTl_Ton1m_aNLqte-FRx0CyJGYGnBUt3nWLN8iPfZAgYzKksDVTzWn1T8NNzQBIYOh3TMAaz_ORuIdzTKCaGXC0GZ7nN17x8zulD8Ic9y3NVWwAmtkW1rqzCd_3QFBgQsfLFZntb4P3RmZsbLCvB-H3GOfdJEVSM5pRN0lismlOyZpXbTsmovUa8d-tmMSliYM59eqTJUUFFyvaj-7C6aWize6oQdoZFy2KgHx-ghdCe0YQSmtcJ4p2tXhNvyebD2mRqvkYfDofc0uYBZjkr6ffGwx7rXb8ahqB939EFNfGI3LbOkQdMQbygMRon36p0ZkR7RM1Je2tsAe_qqjZEyVfSvQVgVA3eQ4Xh_Vb1okiMjnTJiVjcmU6t86UZB4yO9EvVHBBOYlxG2XNjp5PYB38VjSQiGDXMF55IFbb-GBz4qELrz6aMkUoqSNjavfefMSaCN7s7xJ1XeRaq_is8pJa6KL8ZFb7-5nFpzk4CsYjWCq40rm4RM40kcaZhdVbckLFOPguoExHGpCpWGhK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=Ly1C0Ce7xERGQP7dz0X5rZz-v26B-iWndNONQeeN_OWgHP5HhYD4r7rbXoXjqTYsCHwYYVvahU1AxfJBDeG38N-ttn-9lQ2qKDCn8oU8-j_LPvsIesvmD-_j2i0MRt1V5DHBgsUnB-R4iYFRIkArNwuuTl_Ton1m_aNLqte-FRx0CyJGYGnBUt3nWLN8iPfZAgYzKksDVTzWn1T8NNzQBIYOh3TMAaz_ORuIdzTKCaGXC0GZ7nN17x8zulD8Ic9y3NVWwAmtkW1rqzCd_3QFBgQsfLFZntb4P3RmZsbLCvB-H3GOfdJEVSM5pRN0lismlOyZpXbTsmovUa8d-tmMSliYM59eqTJUUFFyvaj-7C6aWize6oQdoZFy2KgHx-ghdCe0YQSmtcJ4p2tXhNvyebD2mRqvkYfDofc0uYBZjkr6ffGwx7rXb8ahqB939EFNfGI3LbOkQdMQbygMRon36p0ZkR7RM1Je2tsAe_qqjZEyVfSvQVgVA3eQ4Xh_Vb1okiMjnTJiVjcmU6t86UZB4yO9EvVHBBOYlxG2XNjp5PYB38VjSQiGDXMF55IFbb-GBz4qELrz6aMkUoqSNjavfefMSaCN7s7xJ1XeRaq_is8pJa6KL8ZFb7-5nFpzk4CsYjWCq40rm4RM40kcaZhdVbckLFOPguoExHGpCpWGhK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=hQSARaGaMPGvJQmSifZUFuvfQdoGgJuYDHaTKxPdS6s7f_Z8hO5QyZpJutDvZ5h1QvR7nWvhdQCcy0DEl5q8i-Zry3KPd2MokjmaIk7VinQFFnJaUJUs7fdauea_gcdgO-Dr66-hfNBZoMWf4N6FoCBW-_dJU-ZPYYJ-NCVlRJ1qKH8qhUqnAhhSkpBJZtZuGag1vyr7Lx3oTGuNFPkCn-03yZDSG5-STC6ZAQCAh81tDgIZhUfiiqoKrou7aVwb6brSvmW7MVFdt44do7mGpRAv5V4_rk343gs0iiqI8b_jonaACH4adPXCyYhJhzuIO3pB79URbXGMq4JTyKbjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=hQSARaGaMPGvJQmSifZUFuvfQdoGgJuYDHaTKxPdS6s7f_Z8hO5QyZpJutDvZ5h1QvR7nWvhdQCcy0DEl5q8i-Zry3KPd2MokjmaIk7VinQFFnJaUJUs7fdauea_gcdgO-Dr66-hfNBZoMWf4N6FoCBW-_dJU-ZPYYJ-NCVlRJ1qKH8qhUqnAhhSkpBJZtZuGag1vyr7Lx3oTGuNFPkCn-03yZDSG5-STC6ZAQCAh81tDgIZhUfiiqoKrou7aVwb6brSvmW7MVFdt44do7mGpRAv5V4_rk343gs0iiqI8b_jonaACH4adPXCyYhJhzuIO3pB79URbXGMq4JTyKbjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=LFhxNN5i17kbikFUaAqi1AqHPMPYw4UyzsrjDweCku3lHdrXFmsb6uWagmLZA2SdwO7ftpJHFr2oXQSMhiFZrCz-QW85Lsb6mQ_Pm4yBQMEPc5lY2hrUv49kJ1zmnxVlfo-ZHtysWpOUe55gUqSCzE3RcFV1C2deHojHPKAL1RaNXd5ivLmCVQ_glNa5kcR2pQFtesa9EpdN-RY-UNfK0ExpqaRKHCWVjC2J4EBLBplUKX3JJlAinJynudGTmLzyLXhWPienb3woaEMlMSA88NkqycluN17Ci6X-NxhLDD1QoCYhV2EJEE9eFcI9LeRoUXvcUZUfgdAevT0ZXzbDpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=LFhxNN5i17kbikFUaAqi1AqHPMPYw4UyzsrjDweCku3lHdrXFmsb6uWagmLZA2SdwO7ftpJHFr2oXQSMhiFZrCz-QW85Lsb6mQ_Pm4yBQMEPc5lY2hrUv49kJ1zmnxVlfo-ZHtysWpOUe55gUqSCzE3RcFV1C2deHojHPKAL1RaNXd5ivLmCVQ_glNa5kcR2pQFtesa9EpdN-RY-UNfK0ExpqaRKHCWVjC2J4EBLBplUKX3JJlAinJynudGTmLzyLXhWPienb3woaEMlMSA88NkqycluN17Ci6X-NxhLDD1QoCYhV2EJEE9eFcI9LeRoUXvcUZUfgdAevT0ZXzbDpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvnAX3_Pc2D4oVIrlOMU77uYJqncaF4WsjSEoy2SvDb5Zd0VJA6cxjTw8GLtCYrz6IMMHXziov3YohNfDyNrN547eHBGkL7uSUlChY8vbvUWx3uGwpo6OBlYNMMwoflclvxUUxwkKc2NehjQBs5I2GWBhnRCyzRXLzkS6VGMqKIKVC2-3FeT1MVUWi9Ay7aLSSJr-Ti5WNSeLzTTE7HKB7zc0eTMxwJE5tf_LcjyVoEkh4sOnOwDwDwiioUtE_yRxv85ltNucLzg_DUuk879qBSmjrXOG4Ah0QlEpVVUJdAgnE8biBIVb92TmUu-NQLl7E0VLNYT2B040L58DK6EkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lywI0e7tr4Uh_Cwzd63mcdgmbOSB6wWNFWHHxSnIufWZjlC2CV55wLp9Ps-kSiApLCCQb-h62_0PuGCOeZr9NHNXqsFY3wCsMst_c8DDDcdIVp1hJOilzP4alEm4lRGFpzf4gnhjOdHz1ec5pfpFj4nlubci1zgdr-0fPkMrx3njFemLEIn0Cxe9IBuaLCyy7wUEaS0Oijal2XYZA9O5DqQAz2S9gTmrYy1nGIC4clM2QOFRvoLOfWyRleZ3QOY71pgsmquaz1iNMV0tvx_nyOOpnv_R-h3Bm6tz858gGj_QVudnEk55svXzgFqRDH6ClsygoZtcfJrgkdUkcPtGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=gqD0QecyotiMANlAXUZVzq-YEv8kj3ExSXRdPLS4MjTfN44Z_G0RYv1GJthcf-6b7WVWNXKb9xl6rW5Z-uUyeP6i_nnDsrW6Rge5SRfPNKB1ZDoh5wrjoWtYizONLuOlH17iLR3fcX1jiOfiw8uhSimsbrfFPfhgRdjo-AknATKTb1ieU3F7LVQGB5LAVH15YDPS9EhE29cybY1e28_aVm8bmqmtS54txo_ahNr1wmJRCG4mpyUN5filuMDR8EJgIA6dQnksYYIUw_umM511s_MVSeo8N-QH_ZMMKP0mPbfT7lgM0x1HH4P8CH0-xpo2IJZs3je_fjNzQ1qAZMFUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=gqD0QecyotiMANlAXUZVzq-YEv8kj3ExSXRdPLS4MjTfN44Z_G0RYv1GJthcf-6b7WVWNXKb9xl6rW5Z-uUyeP6i_nnDsrW6Rge5SRfPNKB1ZDoh5wrjoWtYizONLuOlH17iLR3fcX1jiOfiw8uhSimsbrfFPfhgRdjo-AknATKTb1ieU3F7LVQGB5LAVH15YDPS9EhE29cybY1e28_aVm8bmqmtS54txo_ahNr1wmJRCG4mpyUN5filuMDR8EJgIA6dQnksYYIUw_umM511s_MVSeo8N-QH_ZMMKP0mPbfT7lgM0x1HH4P8CH0-xpo2IJZs3je_fjNzQ1qAZMFUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=IXSeP_mFP5cqVm2iqiMnLWfOnerHYszZAsB_wQhigdN8Te-cPXtA0p0y_w0-UkJD2uLDSof6zmEiUv3aRmR6hhc4Z_4SkRlaopZDUjc5vjjtiH5Yj7igtCUJ98XDo39SuStYZYnmUbVPNVF5oyXluCUkVPmmT1AZoVIeqJbWHwZy6dWiZhzdukTSFh8fJUhQhHiX7JAmhxwumU4hnFoKO36QyFN0rq8ZOO3OAlUXuQqhyS9B8fcUTtpy9PyD2XDlky0RXtFAonSwDCktwg4F5De5tgmseoKKD0WXGp1LUeS2gdp_pnDOEEZ0r6z4BMm91PRzmdlQUbfwIY2hfXC-hpHSpjMzwGtwAb1IPN3Fc7aQpB6ZjJHUmrRzGOYF-TGqkj00djAic7exhA4JsTQE-1BrRvDoG2IFrfKi4jSI0gl7qfw3_m8ZDio2jBmwYw4v8ucEa4Qg5fbdvsmG2TCPvjI4lbDocDVzKhRHrIuw9i32MyyLu8pCPNv0tWoK_rnyn_ZEOaLPv-jbSgwcADTKzsHH671Y48AUzgJIdi10X_8ijtNctGzoLTxRcVzp8CvaC0A1Vty5r3zkOHVreokLCI8IQmCq_L95-66LnBLp5pqmttpZR-R7FV9yElGm4yemgHJQEgNQhb25dLbG_mnnx6Q246_0aHlZfgFH1ZcM9KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=IXSeP_mFP5cqVm2iqiMnLWfOnerHYszZAsB_wQhigdN8Te-cPXtA0p0y_w0-UkJD2uLDSof6zmEiUv3aRmR6hhc4Z_4SkRlaopZDUjc5vjjtiH5Yj7igtCUJ98XDo39SuStYZYnmUbVPNVF5oyXluCUkVPmmT1AZoVIeqJbWHwZy6dWiZhzdukTSFh8fJUhQhHiX7JAmhxwumU4hnFoKO36QyFN0rq8ZOO3OAlUXuQqhyS9B8fcUTtpy9PyD2XDlky0RXtFAonSwDCktwg4F5De5tgmseoKKD0WXGp1LUeS2gdp_pnDOEEZ0r6z4BMm91PRzmdlQUbfwIY2hfXC-hpHSpjMzwGtwAb1IPN3Fc7aQpB6ZjJHUmrRzGOYF-TGqkj00djAic7exhA4JsTQE-1BrRvDoG2IFrfKi4jSI0gl7qfw3_m8ZDio2jBmwYw4v8ucEa4Qg5fbdvsmG2TCPvjI4lbDocDVzKhRHrIuw9i32MyyLu8pCPNv0tWoK_rnyn_ZEOaLPv-jbSgwcADTKzsHH671Y48AUzgJIdi10X_8ijtNctGzoLTxRcVzp8CvaC0A1Vty5r3zkOHVreokLCI8IQmCq_L95-66LnBLp5pqmttpZR-R7FV9yElGm4yemgHJQEgNQhb25dLbG_mnnx6Q246_0aHlZfgFH1ZcM9KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=kuk5oL4-qLmvb8AH3QFtlqbnRppOod2zvjWm5xdTEQKqmAemLTWuYp_4GPAbhKN1RbDl3V7oFv2K-DGXtmd2Oi94726YSXVd9xmMPZ2OJGAjmyr-1FYhNfNkCb7U9cYk1Np6o6UvI_4LFHtzMcV-FrCKLJZp9rFL52jVCwSVurDE-4pv8Mq107088250StEJw0y6K9zwi45AZL0dEbxIcYjqKzsBs3d1UhWoMN6QijQWTaOapz8w0Jxv9FkwG4VcnbeF7IOUUGTkUOXivY-_uuFp00VEMVvuQkKEuvENgwmAy2ufr0K99lKXCS0XiO8nxF3gUV6EoR9rOJZu1Sqlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=kuk5oL4-qLmvb8AH3QFtlqbnRppOod2zvjWm5xdTEQKqmAemLTWuYp_4GPAbhKN1RbDl3V7oFv2K-DGXtmd2Oi94726YSXVd9xmMPZ2OJGAjmyr-1FYhNfNkCb7U9cYk1Np6o6UvI_4LFHtzMcV-FrCKLJZp9rFL52jVCwSVurDE-4pv8Mq107088250StEJw0y6K9zwi45AZL0dEbxIcYjqKzsBs3d1UhWoMN6QijQWTaOapz8w0Jxv9FkwG4VcnbeF7IOUUGTkUOXivY-_uuFp00VEMVvuQkKEuvENgwmAy2ufr0K99lKXCS0XiO8nxF3gUV6EoR9rOJZu1Sqlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=q_YCjo7_k8uyUR0rJdSgNPtqJQFJoUDJUBrz8OHcdQIxdiVoI9MFHZS12ddR0bphhreXZPekJyTmJu0J3JWTmX8T-8bDTMYaW7BLbM71V3B9Gd3r25CpqYsgdWcTFzBTd7cr_kbiAFfaaKqa0BrmwpqNQ7kAKxb7RYX4QBwAybv_kGUkX-8vQ0C2Fb0sw2-xoDLw6Iy1du2jTYTfNz1rt05HFZNTynPgcgcts481EyEEOUTs5LkMEABjonspBJSD0QtK9kUZGAn9MEQOTvNmesSvWWHNn-qkdK50o5O-JTkyxeGbWd0B8U1oOnOJ7ggL6hckYEmnb6k6uq0OGKmc9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=q_YCjo7_k8uyUR0rJdSgNPtqJQFJoUDJUBrz8OHcdQIxdiVoI9MFHZS12ddR0bphhreXZPekJyTmJu0J3JWTmX8T-8bDTMYaW7BLbM71V3B9Gd3r25CpqYsgdWcTFzBTd7cr_kbiAFfaaKqa0BrmwpqNQ7kAKxb7RYX4QBwAybv_kGUkX-8vQ0C2Fb0sw2-xoDLw6Iy1du2jTYTfNz1rt05HFZNTynPgcgcts481EyEEOUTs5LkMEABjonspBJSD0QtK9kUZGAn9MEQOTvNmesSvWWHNn-qkdK50o5O-JTkyxeGbWd0B8U1oOnOJ7ggL6hckYEmnb6k6uq0OGKmc9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=oeGX5_gqlaeHp8mbSIWLbvPvBSfZUoiCbY8t-injbFxtXDv8OXJydTYGxxIF_1xuhnjp5rUmZMmdeBGh0jz9tLH-XwOC-ESnqoaiXQHUphLIu7VjQgJmCtJMHZeBFfS6uHKvEEwSvjr0kurJGVT6slZN3hUIWVeytpm_Ne7OcNkHBQfh47wKotDQ1lVYt1cRbvh_HruF4r_ijxme9pbwhxHSJalhCCF4CZdHqqxnUur5ohWOAARBGXxkmS7PVnzfEl6aXBEI8JFekzEvw62x4R4pkZfL5J4iqeaaNmUUfnqTEvD1WXTngU6E6JmB6CJugz1LtQI5cnD9Vtxhglymrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=oeGX5_gqlaeHp8mbSIWLbvPvBSfZUoiCbY8t-injbFxtXDv8OXJydTYGxxIF_1xuhnjp5rUmZMmdeBGh0jz9tLH-XwOC-ESnqoaiXQHUphLIu7VjQgJmCtJMHZeBFfS6uHKvEEwSvjr0kurJGVT6slZN3hUIWVeytpm_Ne7OcNkHBQfh47wKotDQ1lVYt1cRbvh_HruF4r_ijxme9pbwhxHSJalhCCF4CZdHqqxnUur5ohWOAARBGXxkmS7PVnzfEl6aXBEI8JFekzEvw62x4R4pkZfL5J4iqeaaNmUUfnqTEvD1WXTngU6E6JmB6CJugz1LtQI5cnD9Vtxhglymrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=j1tgAFcqBo0azjMn3nsVB-yEqN-aL9ovocmTgsCbtwJF3Fsbqg9VW63N8E0Y1D_dVOO4bcw6tJITIdxYTdahV2VPbRXfdg3sAZIMY_x8AdxYoud1WF47D_6yYjGcl963LgE_cby3YxFhU-5BTEeRiXmXfq9PGvyBbtmUC8EIC4KlcE2qyRdHBEFsf8XsHoGTRYi5xY36pXKIi2cfwC3AhwGIHq0AYFn-TuPFnWcjNgWEk9EPt8i7XBFN14zOWsp52A24j-nyyq9ZQV9jEYwmmx_c3aLV3DMHtOez-F0UqS8-eNWDjyAoPfh8ecBsowBJG6wcws1kXmRW9ioGTZkIppnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=j1tgAFcqBo0azjMn3nsVB-yEqN-aL9ovocmTgsCbtwJF3Fsbqg9VW63N8E0Y1D_dVOO4bcw6tJITIdxYTdahV2VPbRXfdg3sAZIMY_x8AdxYoud1WF47D_6yYjGcl963LgE_cby3YxFhU-5BTEeRiXmXfq9PGvyBbtmUC8EIC4KlcE2qyRdHBEFsf8XsHoGTRYi5xY36pXKIi2cfwC3AhwGIHq0AYFn-TuPFnWcjNgWEk9EPt8i7XBFN14zOWsp52A24j-nyyq9ZQV9jEYwmmx_c3aLV3DMHtOez-F0UqS8-eNWDjyAoPfh8ecBsowBJG6wcws1kXmRW9ioGTZkIppnKPMAGzTZwFaplVKIiJitb2E-L_QVWW2Cj0_qRX28OtuM80TzgibrwfORNDQ8bIQ9qchI2N259uocolrAF0faLmS-2YSYBGOjqFTfr0m5vuBi35VLYgWo1AzySOe4Z2vW-rE0T3VXD0hRsg2EUvhGneN48ndk0yke-PC7wnFY3--XyVw2r-UL_qIBMsbmJ1VMrV5PBqxXWlDsEO6YwWYCPWjY947EXVu6AsT11_JKFKFxiSQLRSMJhkF6rFj5WCjuMDeJ32Az-AfJEoLO12ZHH88UehTjhPFKfAAkufCfHh6f50PKSE1o9azMv5aZEh6GaxuQ8Iu3fF5pYlrAvOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz1JTfVQljya5FUaLInmB-UqqNyIvi5gnUuE9XCqwX_ce7X_munCLnnlryJNl18v0WuVhxCKH2bcVnzowjBnJi-9ggAP4lULi5axRP05nZV2hvIuXCPNvsKG8PEGZi_zbyUM8-DWOPEl_OhxvO8U7mUzgkcn6j69AmQvzONAta6JspZyXPdcOkU_ovsQ7HTTaXaDM7uGkQ2pPU2t6V9y5SvWNRv1Bq6Jfz9DkbW9ga6hJl9dEHO_RUtzjntuhyK9N3W_wj68y8OZvn2X8OGRjqpJeCz6CkSMR_L3BZSAE0KUz3Qe4LnrMwtRvly0RpCFh_1Jnqy2xxNaynhG90yWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiovmyMxLJg7yjuYOvM_kmYjggWDMEhWaoJG-1KpNndeSTtRNDWU-C3p4LIIQ-4ASiWXjBlVT0nFQrEmpSr95e_8NuartjprD7QaknP7ug7dIfuXlfWgZb_PyUwkpcqZ1lN4OLOJWbplW5Yv57T4C6JWxW7ytMdMII7eTgPza74bMidiIw_9J2i4_mbvg71s9sJnknV29SshQ4i5Z1dcq0zPXOEiFPm5qK0JPTPY7kl5Lyjs2CIR6_UNmYCboJnOq-LGhOpGFKkzkRR7baquryROyO38BHc8l5RFrYdxdk5cQPoB7A4eJY5Sh6SYMPzhAQGtjOjQXqIpG_qBodlsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
