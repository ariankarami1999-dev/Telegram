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
<img src="https://cdn4.telesco.pe/file/tdTmhAtoY087R3ehIomqW-t5lWjSSd-RkzI0yefhIMRQAuroPMVLWNEWEU6br1prKDX84l9-_ALdKRnn-EjmcYCAO-S9-rSFsgXSkG2wEOs6-VzFxiZLb5chsSeQ0e8okwU-W5xm1Q1YhK9ITe-nfOuhOee5meOXqFCDDt3HveNNrgZwquOGibjSEBmlxz3WFYcoTuMjEg94YCQFllHR52a6QR-ruXThF-7P0n8ZpDFPOr8YMBxBE6VK1khOmCrsMEMf9ZVqwid26WkI6xCtzMcqLqWbT-U8OxdwyIpeoqO0Z8ZKlk32OesTeciseJuLo86aVxi2bUTlakWXYDJSdg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-693781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsAY4uXAbGGsZN9rNQaVzaVmQ82lw5Xu7Tj95h1H-Mnmo4JjsdgfoduuvnLETdTd3r3TI_lEGVYQrFAPyyn9dlLcLXpmoPMtc1WPClOuTDXg3X1_pm6_AHgondYMq4igC_iHs4A8xyPOB477O5dGt5Hstw--1mmqIC9qQKWE7TSwLYJxo6DPWhtC53uUk0imi6SCFsFGvkLBrjkN_m0Z7j1eu9lexE-476P33-9Cb2BjazmHv0T1H53kXEsRrhk-aVAAGM-jLSUXV6TAHD3nXYV0tEggapTMEZXblM5cmBzhW-CYGZeCpuiFSaU-oY58hpyu9z42WJXgC01WXkbozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین بارش استان‌ها در سال آبی ۱۴۰۴ - ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/693781" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
‌ حمایت سران حکومت عراق از بازگشایی فرودگاه نجف به‌روی پروازهای ایران
🔹
ریاست‌جمهوری، نخست‌وزیری و سران دو مجلس عراق از خواستۀ دولت این کشور برای معافیت فرودگاه نجف از توقف پروازهای ایرانی حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/693780" target="_blank">📅 21:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5ZjcVZhQBn8yYE6m5oPYq8AphCqq_NyJo3Hl9bPLvb6gNUv3YWEgUY_s6k0Ns1H6JjiXoE27xNES8LNc3wVpw6DSUDfiVqCTCXSS0-IvzuxzIICiTc_VVk8lE5CU6qJTTAkWvmxGQj5XHxBGrO1UCTbUKAKZM8RhPJ6QWbGHn9yAUGDp6J47YK6SzLFefpWO6CEENjnYNU9SNpHURBt4LNxVEaRV7sPbitOEi9Z0gcT2oqFWQPekXsvbfID0S3tf6URFXnGU7fTDBbHFZrsxxBS2SMSDEJkHH3G8kTs6mBilrf8qRKSYfi0egfB6CVK9yju_Hgt4-qe8RbAQkewgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت قیمت نفت برنت؛ ۱۰۴ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/693779" target="_blank">📅 21:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqTSpnFE1xHQhwlgSKSBnFvQjOCPdQwMma_RDIgYTvVv_SpzuVe1HdEp_r9fvtCvFxIcuaVe-SgfGSZRvvu520i4NCxvVh_0tTSNZ88zZvUBQFJPG7tdPj6h-nJKbz5_7hbGi6EW5myjFvj-AXuI7N9BEiZ5WcHTAQpftMfmOSf4ftm7Pl_NsiO04mWEoxITyw8rdyJjQI8GIIwCjcvCQgJjAujFWC0bSKch-tTrzyDDJ8vJhl6Ksovi48wwBuC3X5Jet2XmquKBcm0-augF-kgL18V-LxxlUMHM7gl22_cKxpuY-BkJiJuhJSy2223md4ACysGkyNTCqGWqYCacCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIj_s8MNHCsqBXvfk8sUieO6pB68Lw8rZYpxXJwmR0hJ4QOC3FD_LfwwMzpuOKrC2VBnpXvgEbfnzFktUEUMH8Sm_uzLYJYl7tsc9WnRQoFvc1kvKhCeXZxOuz_ok9VS4JTBAd_zQ6Dvf55QHGmdt0AUGtJeU4y12O6RAcloOYc-G0PfklFPyvG043Gedx2dLRKQYEUtlpTtKVwEuRn12mcPD_UaBvwtSFcuxBpPoNT6j-60PIjdC4bGmlJ3QlhADDR3dzoOjpdnU0fjJFvD0mjWvBzA5JRP_bFs-nri35eLviYtvYhY8xz0w0BFrbkDW4VplReQtAR9ynpa1WFRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBUKn8RFJeasrGiDgls_ID59b5_WshOw6d6JK5yCqC48D5jqnhEM6kjCxEgGqhdfC9ZY1INXKOswh6leNuRqzUHbYWmWJ-lGkteVgJ2rLEUta3PUnJ54gr2EBBe1QSyf9kERxwVKBvdnoMWltitp_Sq3ZE6U1fWq4CVUP9ePk7QeqGTmLI2iUlEHy7dwhoTpnMLrf59YBnl-Rgldc4BWor_oNguHRXFbd2RyuEC-xW9WZUVt1eYI-O2qAGjHVoF09_c1leGs-FdZNpO08emsXOUanu9E0nG4T0RmwNlj9Pg1bN0TEcIy-3keqHVonZHJU6keFxAdDaSfv0G31BKTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upwsQtEidjphZua3KGdDGUde1fNXyYmrOTAsvqe4zv7RgusEtO0a6biJTSpgg6qbsM53LLG2Bg_ZzN7HCuQmQZk8C6eOU7D9TCBM9MNFy5LgyP4CsPzqetFGIhRyfXIaxFQyI7sO231QGTuIXNbUitY_JS7uVGG58b3Bb7VhOhumY2aEUJXAmsBBT3hrj3E3rVQspHeNDAd_xBK2nvoCjl6w4I-EY37Cw53Qgy-r2Z4MLCV97V3RA9xD_Qjjkr91goWmH9uRPZvj5BlWswOHZYg8DvPrG7cOHV2Vg1jWClyC2VwfJMHEMq-1FlV243IZgePlXS3i3D-wOERloMvUfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۶ کد مخفی چت‌جی‌پی‌تی که کمکت می‌کنه بهتر ازش استفاده کنی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/693775" target="_blank">📅 21:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzUt-My4CC5eja5t3V507m7H5zRBoun6CZfbn62OGEzes7lXBvVyx4LV_FOJGJNIivn4OxZBYU46_FrYLXUu5ELBWrzp2NRqdOFvIFDnDJ2B4shc-CquoiGNshXJbrG-xxQdLW5O9fW84KTOaClrH-ipQq1Aejk-7mUf1XqUC6wxZBOao8K7M8BSd4DyPYzaEG-2yD2-SqtW--Uy8AGZrKA8_5da3lw1U6aVeif2PQ8LpvhFMh-wsCGccQBLGR2iiJeJkq106SI981ZwHtivqqpFQULfYNYFFTGX7TJjCguJnAVplaoqZle0uH72XIKZtsKzHzPMtq5j1xyYFkIvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍃
☕
دومین جشنواره ملی رسانه‌ای چای؛ روایت  چای ایرانی!
🎥
📸
📝
محورهای جشنواره:
چای و تولید، اشتغال، هویت فرهنگی، سلامت، گردشگری، محیط زیست
بخش ویژه «نوغان و ابریشم؛ میراث ماندگار لاهیجان و گیلان»
⏳
آخرین مهلت ارسال آثار: ۱۰ مهر ۱۴۰۵
🏆
اختتامیه: ۲۳ مهر ۱۴۰۵
📲
آثار خود را در قالب‌های مختلف از طریق سامانه زیر ارسال کنید:
🔗
pressfestival.ir
#جشنواره_ملی_رسانه_ای_چای</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/693774" target="_blank">📅 21:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693773">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل ادعا کرد:دیدار نتانیاهو با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/693773" target="_blank">📅 20:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693772">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6ad181ed.mp4?token=tjGlbs4SdCcHmZPX4sbuU3W9VJcLIWgukpD0-agGQXH2E2JMMPFALdh8vTi4LqGDXW2vD09sprsNv8uo5JyKoDAJVofTkDdXpZC3Gg7IDD8qfIx-ZkC1PCJqb_G4CLKeh4zDgXNrL6z5QkT9G34ei8U7R_5PxO7d13zZpE-M3ognvolVzssmgmjOADluinl-oRbrrsE-Awo8_SC7QpQ4WkU8LOnOwnqa6dxjdb5GrUGwYBVEdp5Va9vG4pl8FsiWX2zPLl9-D_OpvGHnTYm3H73kK2DLwWExydzoX8G9BE-o3LOCXOHSn0fBtqFrO5U0GQZvi3w9_1dGIqhbQPZu75a8WByokmkpDlJ0eCmEem-VtJlbnUmWzw0TRCeXX3nQ4CsCUaN17AKAwmSktmi_pxk41f2_H-j1r-L9JILKxJhCtq1R0wy7pq3YdGEARHPpq9Gt_5sv9FpZlQJsoGjzQr46-43td5552eI1SdTZsxVNlRHikR6E4w9HUaDI9uZgajUMz4pe9IHtAohptRu74vcrxmYURrjcl3n9rx6Z77QGsI7ySbXVihJpinesVt6pokyHBmy8T07Q19p2ElOiMToo3leD9tB7nJ9eQdnoIHCuFdyZ9ytSvbsR14tejvueiHo8gNZH6h8WtRoEodG459FH2JIwdx_LBG-23Q2Dfd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6ad181ed.mp4?token=tjGlbs4SdCcHmZPX4sbuU3W9VJcLIWgukpD0-agGQXH2E2JMMPFALdh8vTi4LqGDXW2vD09sprsNv8uo5JyKoDAJVofTkDdXpZC3Gg7IDD8qfIx-ZkC1PCJqb_G4CLKeh4zDgXNrL6z5QkT9G34ei8U7R_5PxO7d13zZpE-M3ognvolVzssmgmjOADluinl-oRbrrsE-Awo8_SC7QpQ4WkU8LOnOwnqa6dxjdb5GrUGwYBVEdp5Va9vG4pl8FsiWX2zPLl9-D_OpvGHnTYm3H73kK2DLwWExydzoX8G9BE-o3LOCXOHSn0fBtqFrO5U0GQZvi3w9_1dGIqhbQPZu75a8WByokmkpDlJ0eCmEem-VtJlbnUmWzw0TRCeXX3nQ4CsCUaN17AKAwmSktmi_pxk41f2_H-j1r-L9JILKxJhCtq1R0wy7pq3YdGEARHPpq9Gt_5sv9FpZlQJsoGjzQr46-43td5552eI1SdTZsxVNlRHikR6E4w9HUaDI9uZgajUMz4pe9IHtAohptRu74vcrxmYURrjcl3n9rx6Z77QGsI7ySbXVihJpinesVt6pokyHBmy8T07Q19p2ElOiMToo3leD9tB7nJ9eQdnoIHCuFdyZ9ytSvbsR14tejvueiHo8gNZH6h8WtRoEodG459FH2JIwdx_LBG-23Q2Dfd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمید رسایی: نه شرمنده‌ام و نه عذرخواهی می‌کنم؛ بلکه در برابر این ملت باعظمت، سربلندم؛ کسانی باید شرمنده باشند که کودتا می‌کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/693772" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693771">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693771" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dce2a39e9.mp4?token=htgquutX0XV1-qlh3JIWSqVDMM3xmRhSAwO2h1hHI2tFSUyqd2lSGBPZiev9xDKNaN6gfl-SZEoiaUWyd1zGY9N-eUX4nburEXqJvXYPtM57VWHXlWKCq2DFGArDvcja01yi8qC6RDKFq8eipawIQy0wHgajAJr1DTyvjCM_Ys64QJsW0FJnYqDEqy7EpCdVJqJd-gdbYu0zdQSDtWZjHB7qvfOgBxedaeXBem5aXKt9_11BXNjNDT2dxmLvDUigtPhNWBbcsVRTQUT0CXGop5ECln0A4gW_kytiOizL9ed6uDPDfEQf0kbZMT9jWjV3jP8dJRk0TR-vKNw7p9w6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dce2a39e9.mp4?token=htgquutX0XV1-qlh3JIWSqVDMM3xmRhSAwO2h1hHI2tFSUyqd2lSGBPZiev9xDKNaN6gfl-SZEoiaUWyd1zGY9N-eUX4nburEXqJvXYPtM57VWHXlWKCq2DFGArDvcja01yi8qC6RDKFq8eipawIQy0wHgajAJr1DTyvjCM_Ys64QJsW0FJnYqDEqy7EpCdVJqJd-gdbYu0zdQSDtWZjHB7qvfOgBxedaeXBem5aXKt9_11BXNjNDT2dxmLvDUigtPhNWBbcsVRTQUT0CXGop5ECln0A4gW_kytiOizL9ed6uDPDfEQf0kbZMT9jWjV3jP8dJRk0TR-vKNw7p9w6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آجرلو عضو کمیته رسانه تیم مذاکره‌کننده: چین به ایران گفته مسائل‌تان را حل کنید و این جنگ بالاخره باید فیصله پیدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/693770" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رسانه عبری: دو اسکادران جنگنده آمریکایی وارد پایگاه عوودا در جنوب فلسطین اشغالی شدند
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد دو اسکادران جنگنده آمریکایی طی ۲۴ ساعت گذشته وارد پایگاه هوایی عوودا در جنوب اراضی اشغالی شده‌اند که استقرار این جنگنده‌ها در چارچوب تحرکات هوایی آمریکا در منطقه انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693769" target="_blank">📅 20:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693768">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
یک مقام آمریکایی در گفتگو با سی‌ان‌ان: مذاکرات مثبت و سازنده‌ای را از طریق میانجی‌ها با ایران دنبال می‌کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/693768" target="_blank">📅 20:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693767" target="_blank">📅 20:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5bbbe83d.mp4?token=qQS5wcYimY7OHctDhFR01tlrVdinz06HsJRrADN1UlDGg0B_3_3jffMYm2tm3yJvW_nzcH_AbSxY5oMWc9eQqOfmADvCHy7S9XYQQlnehzaaOjyMLyWIMmFywHaQpBecT6rScb8qZRZoGK7IQmMrrIQDC8BeU3Bhirdt15heMa2snuM1-ty6AHDUa9ZcI59aZkGQwkEaR71ipR1XM3Ny_a6qNwRQRgmbfs76UaQlTVD6L-bRCfPipLkDNSv9RwtJ9jxlykgszqs0FyBZeer5X1okv3tJjY1QS1eFMJPM3HzT5T9kxT1bRO5Kf7TnZ0d_HdpsHdz5MPNP9rv8J9vrOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5bbbe83d.mp4?token=qQS5wcYimY7OHctDhFR01tlrVdinz06HsJRrADN1UlDGg0B_3_3jffMYm2tm3yJvW_nzcH_AbSxY5oMWc9eQqOfmADvCHy7S9XYQQlnehzaaOjyMLyWIMmFywHaQpBecT6rScb8qZRZoGK7IQmMrrIQDC8BeU3Bhirdt15heMa2snuM1-ty6AHDUa9ZcI59aZkGQwkEaR71ipR1XM3Ny_a6qNwRQRgmbfs76UaQlTVD6L-bRCfPipLkDNSv9RwtJ9jxlykgszqs0FyBZeer5X1okv3tJjY1QS1eFMJPM3HzT5T9kxT1bRO5Kf7TnZ0d_HdpsHdz5MPNP9rv8J9vrOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده انتظامی کردستان دستور رسیدگی به برخورد غیرحرفه‌ای یک مامور را صادر کرد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/693766" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693765">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای دروغ اینترنشنال درباره تجمع دانشجویان دانشگاه علامه
🔹
رسانه ضدایرانی اینترنشال کلیپی قدیمی را به عنوان تجمع امروز دانشجویان دانشگاه علامه منتشر کرده است. این کلیپ هیچ ارتباطی با تجمع امروز نداشته است.
🔹
این تجمع در حیاط دانشگاه برگزار شده و عمدتاً شعارهای مربوط به مسائل اقتصادی و اعتراض به افزایش هزینه خدمات دانشجویی برای سنواتی‌ها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/693765" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8032c7661f.mp4?token=ZQlZt8Ot88AIuS5_egkEhPU-_kVGV184vB0nWXn5HoPWx-3OZg_k3WqSG-Sbw4QTG5owHepDHCtDk5b3P3uHmwFEGTrgI_KQc7elX6-amaMH_dxDuPtpd0s4mPBFNaio44gtOZmX0q4JziFdsP5NlbAfsd5uXwLv7f1yM0HFpFKBxj0zBuaB8YFo94N3GbO2FE6h3m54IPb7wf-SzraPHTcaSXDUaH9Kr8JYCfCC_--kX4GluezqQik7FpGj2ElWBiKeogF1TFwLy0eRc234Sn_3nTR-kiZi8ZF6Cgu-oDnVifhaVX6x-NAR00qaAmZBPQ4l0avzV6zsKjm4p2qxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8032c7661f.mp4?token=ZQlZt8Ot88AIuS5_egkEhPU-_kVGV184vB0nWXn5HoPWx-3OZg_k3WqSG-Sbw4QTG5owHepDHCtDk5b3P3uHmwFEGTrgI_KQc7elX6-amaMH_dxDuPtpd0s4mPBFNaio44gtOZmX0q4JziFdsP5NlbAfsd5uXwLv7f1yM0HFpFKBxj0zBuaB8YFo94N3GbO2FE6h3m54IPb7wf-SzraPHTcaSXDUaH9Kr8JYCfCC_--kX4GluezqQik7FpGj2ElWBiKeogF1TFwLy0eRc234Sn_3nTR-kiZi8ZF6Cgu-oDnVifhaVX6x-NAR00qaAmZBPQ4l0avzV6zsKjm4p2qxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش هولناک زمین در نپال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693764" target="_blank">📅 20:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693763">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyxjgGJKbajQO1PmDpVkGBo3a4UAUg5bjrudJBjpOGHlii-niJfjNC5YGruABATp9KBKDNiHe9rZkUm1b8ZKmgLocQHrkyERk11xSKEEOWIA0_sL2yC1I15n13FkzRG-CVkxt0WjAUxBRNxpoIbuyv5swaTilQwOp2RUjE3u2R2aEc5XQyTFKHMtFeuiiGP9YmF0LAT1mS2muzFFCJsfK4PckRMNIuuldUY6D1ctkwXY372-KmVleKW9IwiLvHfAkxArRE-H9xI6bg3aZcMljpT1ZqjceL6Jw1CYey5A3rO3npWqS-KZIQxczV6l8HU8CNAUAOa6TtWNV1BLH7OLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصلاح تعرفه‌ها، راه تداوم سرمایه‌گذاری اپراتورها
🔹
علی حکیم‌جوادی، رئیس سازمان نظام صنفی رایانه‌ای کشور، با اشاره به افزایش هزینه‌های توسعه و نگهداری شبکه، اصلاح تعرفه اینترنت و مکالمات سیار را برای تداوم فعالیت و سرمایه‌گذاری اپراتورها ضروری دانست.
🔹
افزایش هزینه تجهیزات، نوسازی و توسعه زیرساخت‌ها به‌دلیل نوسانات ارزی، در کنار رشد هزینه نیروی انسانی و تجهیزات داخلی، فشار مالی قابل‌توجهی به اپراتورها وارد کرده است.
🔹
ادامه ارائه خدمات باکیفیت و سرمایه‌گذاری در شبکه، بدون بازنگری و متناسب‌سازی تعرفه‌ها با چالش‌های جدی روبه‌رو خواهد شد./ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693763" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693762">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd7004a9c3.mp4?token=JD2cT6NyP2sz9SDoUjYHiCE6b4n1CjuRb7tSyBUJFuEk9T2HiRUCPbS4e2RrF87gKWH3Wjl65Z85Y5Nh0rION1Mt_waE3iw_8p9qkczoFLPNzAXt7q2HsdJvURl54uLS39dL1XJal4oN8IMS8Edn55302ftHFZ5OTj-BgvuIezwlEM_BROm_QXdLfGgyKJ9x-7qkt_0IlT1X-5gtOItEVOSocNgiA2MybWHK0ccPD0pQMVmNlJlYDj_X8J5tG9KmcJxuNszwiwcpJLs1DmV46RHBH51qeo7E-BeyiEBBLQdMuouWTSftUvvXEZJmAapOyst2utzF71V0n0WI5tNsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd7004a9c3.mp4?token=JD2cT6NyP2sz9SDoUjYHiCE6b4n1CjuRb7tSyBUJFuEk9T2HiRUCPbS4e2RrF87gKWH3Wjl65Z85Y5Nh0rION1Mt_waE3iw_8p9qkczoFLPNzAXt7q2HsdJvURl54uLS39dL1XJal4oN8IMS8Edn55302ftHFZ5OTj-BgvuIezwlEM_BROm_QXdLfGgyKJ9x-7qkt_0IlT1X-5gtOItEVOSocNgiA2MybWHK0ccPD0pQMVmNlJlYDj_X8J5tG9KmcJxuNszwiwcpJLs1DmV46RHBH51qeo7E-BeyiEBBLQdMuouWTSftUvvXEZJmAapOyst2utzF71V0n0WI5tNsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی نماینده رژیم صهیونیستی در شورای امنیت: ایران به حماس آموزش و امکانات داد تا به رژیم صهیونیستی حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/693762" target="_blank">📅 20:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
منابع عربی: آمریکا در حال بررسی معافیت از تحریم‌ها برای پروازهای بین ایران و شهر نجف است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/693760" target="_blank">📅 20:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تظاهرات در استان نجف عراق در اعتراض به ممنوعیت پرواز هواپیمای‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/693759" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تبدیل پلاستیک به سوخت هیدروژنی با کمک نور خورشید
🔹
پژوهشگران سامانه‌ای طراحی کرده‌اند که با استفاده از نور خورشید، بطری‌های پلاستیکی را تجزیه و از آن‌ها هیدروژن تولید می‌کند.
🔹
این فناوری می‌تواند هم‌زمان به کاهش زباله‌های پلاستیکی و تولید سوخت پاک کمک کند؛ در حالی که بیش از ۹۹ درصد هیدروژن فعلی جهان از سوخت‌های فسیلی تولید می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/693758" target="_blank">📅 20:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL5N4UthS33XjB3_InB_EXEmzzFXdzVdDRwbE9bf4yWCD1hY9K5vKE5RIHI4kKkwOZDVR8jna5QCpJYvmXBX2-wqDM4AFF_M4gS3iL0B3hzs51BZ4pmtvnusiKP5SAlgjdUOKHQTzLaFvcSal73G__RUJu6GreT9ApLg1bTwqaf3GRDGKsAQntToeRQIT_cL3To6DX0jT3XP8KKbz_fyQgPVAJc-NxaiWl13tnrXJpECto4sLsW--2lSDeWPJBCHzLDrDHbOse6a8ZiDuzIfUDMG4C1VhAaNnes8-s4-a9y9OtCi3pnUTG63VldtbJS7O_lye88FZCDxl5Vnlf22cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاییز شگفت‌انگیز جاده چالوس
🍁
🍂
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/693757" target="_blank">📅 20:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">19-2 Ane Manaee (1404-02-06)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/693756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نوزدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
خاطره‌ای از علامه جعفری و سبک اخلاقی و معرفتی کم‌نظیر ایشان [00:00]
🔹
از نشانه‌های رشد انسان، تسلیم شدن در برابر حق است نه توجیه و فرافکنی [05:45]
🔹
نقد فیلم "مصلحت" و حساسیت انتخاب در بزنگاه حقیقت و مصلحت! [11:47]
🔹
آنجا که حق، قربانیِ طیف و تعلق ‌شود؛ بیماردل از مؤمن تفکیک می‌شود [16:20]
🔹
اجماع، مسلّمات و فقه، ابزار قدرتند در دینِ گزینشی برای منفعت طلبی! [24:43]
🔹
نفی قضاوت‌های سطحی و ناعادلانه؛ روایت قضاوت یک طرفه حضرت داوود علیه السلام و توبیخ الهی [36:18]
🔹
دوگانه "هُدی یا هَوی"، سنگ محک پیروی از هدایت یا منفعت [42:12]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/693756" target="_blank">📅 20:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLbtezHuUkW2GgQ5cyDq2zhyR3tNzPDi5ef3q-wKIrAPLiuP3JFtEp_F2s0QrXhBv66mxhbXdO23V3HlaiOBvO_pQ5ZwFtdIUE_JxSWqrZC2e9jZd_QBP1lUEd8hEld3TiGk3mgopUaVU21Gh-_5rdw26tE5tQLNrPBRG8DwJuHL00Z3-R6JPGgrnRXHB5gNx3m3dRl-UEd_XfxtsC1wsrAuG_iBHD3SQH0EiA7LMYDaevhAXC5QT5lJJ7zZj1CVZYArzYCRIUMVs5svn8oYAbBGhNJ9k6nUQ_aV3-0vjIB-meTfUod_EKN0NdvcUlQbHNqBuM8OqhrHn0C-h5FLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار آکسیوس: یک مقام آمریکایی به من گفت ترامپ مایل است در ازای پیشرفت ملموس در پرونده هسته‌ای، تحریم‌های ایران را لغو و دارایی‌های مسدود شده این کشور را آزاد کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/693755" target="_blank">📅 20:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbPheh9JbWmKBd6QxtaaoPIrciGhyyccflCmBQKI0I1Hbief27XP2YtTpPngH7cdxZevbXjBn7iPrNIgOEMd-46F6Z-cj3lEOr9UW5riOvzafpOEq072bTVLvO003u5NNs90EBhLAZ1vdO7Y1GitfcQyPa9uTMWSExAcNIXHVXbhrNBox7BonqhX3zYJyoED4E_UIMlmdLyHdhQI2W2qlAfwoNa38cEtz6zn3GRd91S26KGPGEUuDqgMPm-1qBqEPurqYM0xLtlA6qbLfjdGmJlNwRBpZi2H-rAJHY3QxGlOcw8Do1QrNfH9VtSp9jhP6vBOQ-h_4fK9XGo7nkLeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این فرصت را از دست ندهید
❗️
اگر برای معرفی
برند، محصول یا خدمات
خود به دنبال دیده‌شدن گسترده‌تر هستید
با ما همرا باشید
🔥
۵۰٪ تخفیف ویژه تبلیغات در تلگرام
📣
پکیج تبلیغاتی گسترده در
۳۴ کانال تلگرامی
👥
دسترسی به بیش از
۱۴.۶ میلیون مخاطب
📞
دریافت جزئیات و رزرو پکیج:
09923104314
📲
ارتباط مستقیم:
t.me/Farahmand_p</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693754" target="_blank">📅 20:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR5l8VW-E9j_PpbMAGwRQHYF8Gk85BpyqwzHmRhUJS_H_Tc62tg_StJ5kRm4VTZW4yDxXX9Zq3zdWUNnvqsEJlLVO79zqbsy4JOOGFMuIGoOb0E9VeyzhVYq1zFQznEFQuf7uWnTfKNz-61VZVVnvV59j3EAwXyGDlrQCAozZDxPui4lXA4i9MPf_AHYlcQf--iSeqQ81FltKMQmUvEZSmD2EOBhFT26hYXkbZ8F2VGvfZ-sC1I78zfFDyoolGXF7g2yyF-vIL4zbOZyekwd07Br9vCWetSVAJ4zlhYTV2OzWYYPU9fHiXmPMLfGJ7VmKvIzBtHKC1Lt7sDJv-A1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥾
نیم‌بوت مشکی مردانه مدل Sorush
یه انتخاب شیک و کاربردی برای روزهای خنک و بارونی پاییز و زمستون
🍂
✔️
رویه چرم مصنوعی
✔️
زیره PU
✔️
کفی پرسی و دوردوزی‌شده
✔️
سایز ۴۰ تا ۴۴
🖤
رنگ: مشکی
🔥
قیمت: ۱,۸۵۸,۰۰۰ تومان
💳
قسطی هم می‌تونید بخرید:
۴ قسط ۵۲۵ هزار تومانی
یا اگر راحت‌ترید،
پرداخت کامل درب منزل
انجام بدید.
🔄
ضمانت تعویض ۳ روزه کالا
https://memarket24.ir/product/brief/63746/180124/</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/693753" target="_blank">📅 20:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی به الجزیره: ما از طریق واسطه‌ها به مذاکرات مثبت با ایران ادامه می‌دهیم و بدون پرداختن به مسئله هسته‌ای هیچ توافقی حاصل نخواهد شد
🔹
ترامپ آماده است تا در ازای پیشرفت در مسئله هسته‌ای، تحریم‌های ایران را کاهش داده و دارایی‌های مسدود شده این کشور را آزاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693752" target="_blank">📅 19:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMwyW4VSSnJjCbggF_viQUl86APUVt9kYPQTK8IYahGQUFANxR5CMefcQb08T9u13iDC2Kz0rNDFSJkqGiTp5kV9SgsfjGeOM2gsoa0eUHYh2LcE8WQccPRe8y-75Tue9z0IFhJ119CJV2rSVnUjyFZL8qGWIcvVTdU635IujLjdu8I1iQZ7Vwj4ETc_gNgH0Fb-oOv3RYirhLgcq7BU10zahQ4FhEvoz9Nv5lR40-K0OLFOEdp1QGLZu5QfH9ad95wiz4bmdLWPGCwPOgKlkcO1T2tbF5EIuoa25xel0rs0jnBsyCX5wzJU5hlIb1nbP5Wq55jtGijgKrwrM2xUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مرد عنکبوتی»؛ مارمولکی با سرخ و آبی خیره‌کننده
🦎
🔹
اگامای صخره‌ای لکه‌قرمز به‌دلیل تضاد رنگ قرمز سر و بدن آبی‌اش، یکی از مشهورترین مارمولک‌های جهان و معروف به «مرد عنکبوتی» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/693751" target="_blank">📅 19:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سامانه واردات خودروی ایرانیان خارج از کشور غیرفعال شد
کنسولگری ایران در دبی:
🔹
بخش انتقال خودرو در سامانه «میخک» موقتاً از دسترس خارج شده و صدور کد رهگیری این بخش امکان‌پذیر نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/693750" target="_blank">📅 19:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693749" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
عراقچی امروز در نیویورک با میانجی قطری درباره پیام‌های ایران و آمریکا و شروط هفت‌گانه تهران برای بازگشایی تنگه هرمز دیدار می‌کند
🔹
یک منبع نزدیک به هیئت ایرانی نیز گفت برنامه‌ای برای مذاکره مستقیم با آمریکا وجود ندارد./ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/693748" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS_A0Q_mrOdVKI_GNxBFAzZ8jSbJD8hg7ajRCBbEWb6wtD5A9MqyU2BMuWnQ7x6CdoNyOUp4K6sUOryAQqyOWvrIHQbpwY6140lpix-Ei4K5c_FN9UNOe_LsrB1t8KyRIk1frVNW8ZzCvjgH5pDH06D0OPs0EnH2qLFp33EB2G287GFDszEwWPSMrmJzlrMrVLMpJBuG1FIgYDBLiIvLgDU8x4V9uWPQW0N0mOMe9Cf0FQwxcJ6vtDogVJUjU6Og_3Yt3zAflIPTgh5c13O9aXnsQymzgcRW5jzGCO15vTBnHk4LJMg9U9waAEGfB7vARqxMXcDq9wxJncIXx7RFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت بی‌نظیر از لک‌لکی در لانه‌، در غروب دزفول
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/693747" target="_blank">📅 19:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای دریافت ۶۰۰ میلیون تومان زیرمیزی برای یک عمل!
محمد شریفی مقدم، دبیرکل خانه پرستار در
#گفتگو
با خبرفوری:
🔹
دریافت مبالغ خارج از تعرفه به یک یا چند مورد محدود نیست و در برخی خدمات درمانی از چند ده میلیون تا چند صد میلیون تومان مطالبه می‌شود.
🔹
یک بیمار شهرستانی برای انجام عمل به بیمارستان دولتی مراجعه کرده و جراح برای انجام عمل مبلغ ۶۰۰ میلیون تومان به‌صورت خصوصی مطالبه کرده است.
🔹
در برخی بیمارستان‌های دولتی بخشی از اعمال توسط رزیدنت یا فلو انجام می‌شود، درحالی که پرداخت‌های اصلی به نام پزشک متخصص انجام می‌گیرد.
🔹
خواستار ورود دستگاه‌های نظارتی و بررسی شفاف پرداخت‌ها و منابع مالی نظام سلامت هستیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693746" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادامه کاهش ذخایر راهبردی نفت آمریکا
🔹
ذخایر راهبردی نفت آمریکا تا ۲۵ سپتامبر به ۲.۸۳۸ میلیارد بشکه کاهش یافت که پایین‌ترین سطح از اکتبر ۱۹۸۲ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/693745" target="_blank">📅 19:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odChW0EE0tO20Ol7F0uwwU48a4I-aK4IL8KuFBB4Bj3qdnTh4FQVrxQovK448nyCSRBknyxrLnFkUk7SbwQk8pFnsZhvUmNbGl7p4JAoYzqAnPc7qUeHBSn-rSHsz2hDZGz3fQbQiPMV5YuMjg17gfEr1pNVdYwSAb1ZGvvRZtEu0y64_cDIRQifW1IK56iLcFCYgElcTKx7qdiJ1KCx3e4egsp-_kMKe8kNrpUlZ8nettst6qhfqUWGnQ_S8JyaQ556hxmle5SEbRCLEFhEPe5I47ciMOEx9sEw_UGrUskaLFFFqWAiyJo0dZI5LG5qfor0Dq1yH9WsxIEgDz9Fyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا استعفا داد
🔹
سی‌ان‌ان استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/693743" target="_blank">📅 19:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری: ایران با هماهنگی وزارت امور خارجه، اعتراض رسمی خود به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی کشور را به سازمان بین‌المللی هوانوردی کشوری (ایکائو) ارسال کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/693741" target="_blank">📅 19:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faddf05fe0.mp4?token=WIC5wM3edE8wxX35lUZtPrtu9UHcux9zEfRHHlPJOSxnpTk0-rQmWwMZ6YUSOrvBvUEAYuXB7kpLKD9aeU4W1epW5IgCLTxnqEeHKMRJnJcFPymE4g0biKxLWUu_RZMyoXVtethBOynNfTmJ0cDOIECKVGB8PHI0mB2nbxmwR9c211G5K5a_Xxp_YzbBjevntoKCaWvi1ayUCmC2gIVM2Vhw6_jyJAEI80EyWxAo_dBhsXxKMr1c6IB7nRWoIyUVpPmN-KWdhkaVJS8_3Yp8V584Cl5Q6W8gyyEpI49abSzdnU3yFFp2tIxCtN2fO_BCLYZQInFE9M7RsBD0v5TphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faddf05fe0.mp4?token=WIC5wM3edE8wxX35lUZtPrtu9UHcux9zEfRHHlPJOSxnpTk0-rQmWwMZ6YUSOrvBvUEAYuXB7kpLKD9aeU4W1epW5IgCLTxnqEeHKMRJnJcFPymE4g0biKxLWUu_RZMyoXVtethBOynNfTmJ0cDOIECKVGB8PHI0mB2nbxmwR9c211G5K5a_Xxp_YzbBjevntoKCaWvi1ayUCmC2gIVM2Vhw6_jyJAEI80EyWxAo_dBhsXxKMr1c6IB7nRWoIyUVpPmN-KWdhkaVJS8_3Yp8V584Cl5Q6W8gyyEpI49abSzdnU3yFFp2tIxCtN2fO_BCLYZQInFE9M7RsBD0v5TphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین اتاق دنیا؛ جایی که پژواک ناپدید می‌شود!
🔹
اتاق‌های بی‌پژواک با جذب امواج صوتی، بازتاب صدا را به حداقل می‌رسانند؛ به‌طوری‌که افراد ممکن است صدای تنفس و ضربان قلب خود را واضح‌تر بشنوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/693740" target="_blank">📅 19:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3168aaef59.mp4?token=AzbuPLdHWeUuu1nUmzo3tPjSr9prNGUvTe6zuAclGkvnUnoL6Ic8GUQ33sJ0L7HVd92CI9vGemfZeBW8o3EcnZKdlph2JYF78U0cMfELJuwhokw7j2fJWgT5yutlzOjM6AnGcsAteIOhoPFE-h2vjZP_9gvI9E28-csbmi_3jB73ewKy4a-Z_X7x81qZro4QiEGCfhpzqeDjCYPGCMZCARoOHmg5OQ32RziYuqRz5ktLwFiTNlDSwTena1F9O_zpXTk1K1UqsGcy-TxH2QVvB2Yceahrm-MvVUcmWvbIZcq1twCwo5_eCgV5R7J-gudR1F8RNbizWikUDLEXwdddxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3168aaef59.mp4?token=AzbuPLdHWeUuu1nUmzo3tPjSr9prNGUvTe6zuAclGkvnUnoL6Ic8GUQ33sJ0L7HVd92CI9vGemfZeBW8o3EcnZKdlph2JYF78U0cMfELJuwhokw7j2fJWgT5yutlzOjM6AnGcsAteIOhoPFE-h2vjZP_9gvI9E28-csbmi_3jB73ewKy4a-Z_X7x81qZro4QiEGCfhpzqeDjCYPGCMZCARoOHmg5OQ32RziYuqRz5ktLwFiTNlDSwTena1F9O_zpXTk1K1UqsGcy-TxH2QVvB2Yceahrm-MvVUcmWvbIZcq1twCwo5_eCgV5R7J-gudR1F8RNbizWikUDLEXwdddxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از عجایب رشت که از درخت نخل یک درخت انجیر رشد کرده است
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/693739" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmp1G1N7sH5KZVeQHzNR3USGFbvTR-wsLbL6ARUnq32r3O5-fhhFg-dU4Bl4EXntZhjKzcnAll2z604UJ6TlciFpkqFubsGkQ0Uk__VD8n71yjKzOIjv-V_DmJ9JT-hQHm6t0ejozBxOz5bDeGsR_QtQ6RWPKSM5-hTsE5Djuphs-eMJY5MiQ_G4cz3GuTkwZxizvW9yj5hTGQXb1mi0L0V0ebOypfqHBTny5eqZALTCEQEYFz--N6qEDfsVKCE44vRHWehUwdpd1xgAdskWP4powwMcZrVE9FZNcp6SlDM-9fSP3bTw-09NpTyAbD_H-hQKl4SuCBZJVyRaD-rqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qte_Z56Q432qXwOioqYCHp5nblMsswpiOqhywP4bMnNRQgn8lco1MAiksXkyKZ3kvjiPGz9AIZWHR1848GEpcCN0SbCXpeidfumcW4ZgLD-J3gXcbqtOdLZW1C20anddevIBkh0JjqblQjNKKAxQwzIbDDpLP21XruUDCqgJm6luBXkA2aset4zcopCoZ3FOMlHwq3ooM3e28GU2mnD3rFzwV-kuud05Osv0aeD3E0ynSR1ncqNATyGG3SsghEaxchnVOxs4H6CnPmQbCFhz7AurHhG5i168BfycezUgKtFXMyIf2frCRTh3IrXeTLtH1BmLuLy8Fj5FN9A2QOaI6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امروز روز خوبی برای طلا و نقره جهانی نیست
🔹
طلا و نقره امروز مجموعاً ۱.۲ تریلیون دلار از ارزش بازار خود را از دست داده‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693737" target="_blank">📅 18:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruO_Wek4YinIvygRed_qknHs887YtqZv_lEAB5qI40fgAkz7xMCFyR_CSGgWm5rdFv5VNgrPoTTsy7wP3mh0RxiE3St29KCnm25Dttv2bzZllj6bz1hs9j9HT_2_xCif2UmH9dKUkdVxdjsjzrqriDT0tgqZixU9EE8p72GWC3LV6v7RSeR81K78Wo-t9SoGAvFle_dluSilq1eva2M_2p4ZxeAVvm8JouwADvo58rpkjD9OUAxVs5rvrATsWWjVXnxSBiWAwAS4TBvQlWxpHA_FeJouIfGhpsB_ao7Co9NIwdqP8tC4sys6AAmmrO5FIGuXx1PhgXQraQru5YmV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیابان آتاکاما در شیلی، خشک‌ترین بیابان جهان، به‌دلیل بارش‌های شدید ناشی از پدیده «ال‌نینو» به مزرعه گل تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/693736" target="_blank">📅 18:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پرونده قطر برای اسرائیل باز شد
🔹
قطر از میانجی مذاکرات به یک کارت سیاسی در انتخابات اسرائیل تبدیل شده است.اما این کارت به کجا خواهد رسید فشار سیاسی یا جنگ؟
🔹
جزئیات را در این ویدئو ببینید
@TV_Fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693735" target="_blank">📅 18:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693732">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693732" target="_blank">📅 18:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693731">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
عراقچی امروز جلسه‌ای را تنها با میانجی‌گران برگزار می‌کند و قرار بر مذاکره با آمریکا نیست/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693731" target="_blank">📅 18:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693730">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e414fe.mp4?token=SH7gParEXaE0MkdBxzT4l59trKRFhle_9aWjET9eeLh2uidmIe9Z9BWehmtLDITlfW12raY1jLezE2uK2hZk3eCMRxOPBdIyean_NNAoypS2YflmsEuMxXy268VDiTN9IhKuA0jtwa-fupCMt-QiSIuE6PgPwuMecmSLMelT-CkQsbxtwdAfM1uk3AlGCc7cbQ9gWH0e1El6kXeIcH8uPHyPwlcvce9GzjRed7gznqpmC5AL3El3KxdEmddZk-KOzRHIpDHm-9F28fEBbauUzFsdv2ZmkR1IUPwQj8VElzfDQh8nScZAgpOngHHuRlKG_2Blcr6cug7VBKWE0UWI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e414fe.mp4?token=SH7gParEXaE0MkdBxzT4l59trKRFhle_9aWjET9eeLh2uidmIe9Z9BWehmtLDITlfW12raY1jLezE2uK2hZk3eCMRxOPBdIyean_NNAoypS2YflmsEuMxXy268VDiTN9IhKuA0jtwa-fupCMt-QiSIuE6PgPwuMecmSLMelT-CkQsbxtwdAfM1uk3AlGCc7cbQ9gWH0e1El6kXeIcH8uPHyPwlcvce9GzjRed7gznqpmC5AL3El3KxdEmddZk-KOzRHIpDHm-9F28fEBbauUzFsdv2ZmkR1IUPwQj8VElzfDQh8nScZAgpOngHHuRlKG_2Blcr6cug7VBKWE0UWI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات در استان نجف عراق در اعتراض به ممنوعیت پرواز هواپیمای‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/693730" target="_blank">📅 18:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693729">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd2be7225.mp4?token=QAyY1tUMqi-zBcM67ua2-YIdyreOzRsO4NgipJhYSdH2gZMLEirYAjYlPov0GoLTBGfN3Ok7_ctjUoHgSVvIoURnWK0gJGkFUp4HqGVEi0oX_mYaUwI9w0BmIqBBW5p0Ve4No4a9UWHwpUSwTuHenJy0LOgz_epvIuuwZ8hN7ETlBZhyv7BepucLhI3xGd4CbcCY8ppQzAsCNqw6kDQMdfhyoJ-PPBX38R3TzYcR_QE9Ous2734wESqOAeAXzTbOkMP5xW9NhyLTDhEAn4s1-S4d1REMFgoqPMYONXP6FAdmUTOrxth_F_Q4ix0A17NS4uoEw1Ljk8LSbJvnIyJUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd2be7225.mp4?token=QAyY1tUMqi-zBcM67ua2-YIdyreOzRsO4NgipJhYSdH2gZMLEirYAjYlPov0GoLTBGfN3Ok7_ctjUoHgSVvIoURnWK0gJGkFUp4HqGVEi0oX_mYaUwI9w0BmIqBBW5p0Ve4No4a9UWHwpUSwTuHenJy0LOgz_epvIuuwZ8hN7ETlBZhyv7BepucLhI3xGd4CbcCY8ppQzAsCNqw6kDQMdfhyoJ-PPBX38R3TzYcR_QE9Ous2734wESqOAeAXzTbOkMP5xW9NhyLTDhEAn4s1-S4d1REMFgoqPMYONXP6FAdmUTOrxth_F_Q4ix0A17NS4uoEw1Ljk8LSbJvnIyJUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی هوشمند شفاف، طراحی آینده‌نگرانه‌ای که مرز بین فناوری و دنیای واقعی را کم‌رنگ می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693729" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693728">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFx9NtTye3lvszgGPN_6psWIleCaF5udY9Rd5_ZTOIWNK99WKq0vFDS0ONUJMVAM_J4Vwb4ES5fea1B57KKEeZzCd-Ku8j9GvecD6Lr6f1pcTsB1HnuGoGKTLcvGvl-rW4fNcSiCYh3mBdklqFpBWUTtZbD0eDn2vh6n9lp4t3GA9Yl5gQedvjovA0rsIa6qrZDp_Efu33sHX6B75csC3AWUpSBL5lahFO_6VIPVlAVIzgRkosRIqnVmFimx5E_urv-6htTWMaUmUCMIWCxi5tMTW0IMgmc0kn7q_Th37z5KihZdlXXSXX02vRoVIVQSRwpc_lSmjlQAHZWedK4Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل‌ارث تصاویر ماهواره‌ای غزه را به‌روزرسانی کرد؛ حالا می‌توان ابعاد گسترده ویرانی و خسارات این منطقه را مشاهده کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/693728" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693727">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: در برخی کالاها افزایش قیمت ۱۰ برابری رخ داده‌است
کریم معصومی خسروآبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
با افزایش قیمت‌ها و نرخ تورم قدرت خرید مردم کاهش یافته و افزایش حقوق کارگران، کارمندان و سایر اقشار حقوق‌بگیر متناسب با این افزایش قیمت‌ها نبوده است.
🔹
در برخی کالاها افزایش قیمت چندبرابری و حتی تا ۱۰ برابری رخ داده و در برخی اقلام نیز رشد قیمت‌ها به ۱۰۰ درصد رسیده است.
🔹
کالابرگ با رقم فعلی نتوانسته هدف تقویت قدرت خرید مردم را محقق کند و حمایت یکسان از همه افراد بدون توجه به سطح درآمد و نیاز از نظر عدالت محل انتقاد است.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693727" target="_blank">📅 17:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693726">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952dd3bcd9.mp4?token=cPj9H8GOoWkj5mz_pUh0m4_Lselcm58sG_iw-cDBUTpRRDfwTGo1U6CgaWmjNL2SUJllC-WLY296XZlp-m2cdLrM6LJejT3fYyLN7aU2BxpDilaGl7LzgO30MiWNfIqHCgiy_6Kx7erVY2GiAlsDsh2GyhjZJzH453froVnD4v4PAqB6TZkxbsZqpjnGmGCr07NSrzphgaIwfM5pgjJ8P59KwoE8EHc6UzLjqWj3ouBNtvR8ITuWyxWDaFE59yUiHZJuLwGVreUSHviU7SXG-GIlo4OtvSr8_3AhGSQ7JsHb5qdL7EhaOTIn_lGUX_nhbt9c1byV2bdUe0zM89QsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952dd3bcd9.mp4?token=cPj9H8GOoWkj5mz_pUh0m4_Lselcm58sG_iw-cDBUTpRRDfwTGo1U6CgaWmjNL2SUJllC-WLY296XZlp-m2cdLrM6LJejT3fYyLN7aU2BxpDilaGl7LzgO30MiWNfIqHCgiy_6Kx7erVY2GiAlsDsh2GyhjZJzH453froVnD4v4PAqB6TZkxbsZqpjnGmGCr07NSrzphgaIwfM5pgjJ8P59KwoE8EHc6UzLjqWj3ouBNtvR8ITuWyxWDaFE59yUiHZJuLwGVreUSHviU7SXG-GIlo4OtvSr8_3AhGSQ7JsHb5qdL7EhaOTIn_lGUX_nhbt9c1byV2bdUe0zM89QsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان هواپیمایی کشوری گمانه‌زنی‌ها پیرامون برقراری پروازهای عراق را تکذیب کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693726" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693725">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde8aae273.mp4?token=ia0KgHi9Y5TDfOdeUQEOZ1Lz86VfWmacXzEFG4spyj_Z3HkbLSAKsZaXp8Sr03vj0_m7xUMlH-9jfXR-fAcF_JGXwUmKCeR6SlQvEGzxi-zBtDa1Ay0pBO-81c8-hDv7zbQKxjDYY-CVHAqq0XNlkfOvqMKZ-1YpYYSIf8XwNkUiaGgfEp6oYmwR4_20N3Gz_2dOMApRfmNg7sXmT4KyQlCd0qE9DHbJWIr6ZKy77tsqD-3E5s5Y0QcAJYqyY1ff_JUUKYbA3zfP-P0KR7Lvn3dYGa97hrFW_-nKw4YyawV964MTIhAcRNaS52AkfW8p8A9nvmXyTICbk3JJxNWXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde8aae273.mp4?token=ia0KgHi9Y5TDfOdeUQEOZ1Lz86VfWmacXzEFG4spyj_Z3HkbLSAKsZaXp8Sr03vj0_m7xUMlH-9jfXR-fAcF_JGXwUmKCeR6SlQvEGzxi-zBtDa1Ay0pBO-81c8-hDv7zbQKxjDYY-CVHAqq0XNlkfOvqMKZ-1YpYYSIf8XwNkUiaGgfEp6oYmwR4_20N3Gz_2dOMApRfmNg7sXmT4KyQlCd0qE9DHbJWIr6ZKy77tsqD-3E5s5Y0QcAJYqyY1ff_JUUKYbA3zfP-P0KR7Lvn3dYGa97hrFW_-nKw4YyawV964MTIhAcRNaS52AkfW8p8A9nvmXyTICbk3JJxNWXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان جالب به‌وجود آمدن یکی از محبوب‌ترین خوراکی‌های دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/693725" target="_blank">📅 17:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0vApifRXHXLFKC5aImdPwxfZUbkwwH4qVxiAC1y883lAQPmCZvuJZFOazwTECPIeUB8v6detl43dkOJiQR7Y5xfkvBLJsbiWAafzAeMP4tJQvL04j9rD7x9FYCdm9mfu_LYcGBvmfKKFdox8MuN6lB5vkRd4M-4PUoTfEEI9LE8YDSp25-wlHJrxhWHjdaI3Mum5wSDIg3ujOlxd4rIig_oWGZZJfTpJ8r8abv4cgOYnn8alvEwgCoxEnqJPYdsTIZsFPCQEr2eccATGvivFltpFgR7h72GdsuM4aoyC5SO24og1af2Xm7-Y2I3vHRcUZomzdj7UezwIW62mgG5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: قطر به دلیل بسته شدن احتمالی هرمز، حالت فورس ماژور بر روی محموله‌های LNG به مشتریان آسیایی و اروپایی را به مدت یک ماه دیگر تمدید کرد. زمستان در راه است و محموله ها لغو میشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693723" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
رویترز به نقل از منبع آگاه: میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
🔹
عباس عراقچی و میانجی‌ها در نیویورک می‌مانند تا مذاکرات را احیا کنند. مذاکرات در نیویورک بر نسخه‌ای اصلاح‌شده از آخرین پیشنهاد ایران متمرکز…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/693722" target="_blank">📅 17:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niRPu7RpvaossCyu0QaKIB_A1W3IjYvNmwxN5y-uee8i8MNiBSWbG9AtnOwjeNC-ZSeAIF8WqMvbcM6WxiIFKtxyvoIiVbIRGalFW8FKnXhrE7wDXQVirh3I1LVWffYHGwNbh1vkEevpe-A9AhFZc88dBr44PRu2GKKf1-H0cNx9nY8bV8iqxgHJ00x9U1kYLjznqD5bBbmqVsBUaSP0l0eLMiVNMAZpKnppMKicebFtJw3ew792crFvynmNxMb1Rm1IMnY84ZQ_Z74-IskcZDcYgVt401FP0iJwVl9vRF2yTWlH4SMwMuOBXB0OHX04tN8EniRWHEQgT6NAENk4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی امریکایی با کنایه
:
🔹
دو هفته تا پایان جنگ ایران مانده است.
🔹
دو هفته تا دریافت چک‌های DOGE ما مانده است.
🔹
دو هفته تا طرح مراقبت‌های بهداشتی ترامپ مانده است.
🔹
دو هفته تا بنزین ۲ دلاری مانده است.
🔹
دو هفته تا کاهش مواد غذایی مانده.
🔹
دو هفته تا کاهش اجاره‌بها مانده است.
🔹
دو هفته تا چک‌های تعرفه مانده است.
🔹
دو هفته تا بهبود اقتصاد مانده است.
🔹
فقط دو هفته دیگر.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/693721" target="_blank">📅 17:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار هرمزگان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8050bd59a4.mp4?token=nBxxHPEX9hoidms2t_CkzY2LQPPJfVw4UZlGcbNw5aul_9Lgxd4XQudoKSz5RVcU43mGGh82j9HEwLIu_QOHJ9GOiR61aOcyb8mueYeLBNfKYmv8aQkEoZmsHT84XBwKyzO3EBU8TOdEkDFv7VuWsKRQIt25BzJL_C48VyGyuwKoqHDqNQJ-6wQlq-eERkOP20nUoRcJfJJX7KNE0-F8BNQm6gGPBE2OBxN1e0X3lg1d-04uMd5Ztzoxv5UCBWoZ1lyk205HpNn2R6xIjJwc0efvFaiIW_2II5b0rAOMv-TF1-dgJ53_hf--mTVJW3offJJRY1cAvARLyW0GYPl-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8050bd59a4.mp4?token=nBxxHPEX9hoidms2t_CkzY2LQPPJfVw4UZlGcbNw5aul_9Lgxd4XQudoKSz5RVcU43mGGh82j9HEwLIu_QOHJ9GOiR61aOcyb8mueYeLBNfKYmv8aQkEoZmsHT84XBwKyzO3EBU8TOdEkDFv7VuWsKRQIt25BzJL_C48VyGyuwKoqHDqNQJ-6wQlq-eERkOP20nUoRcJfJJX7KNE0-F8BNQm6gGPBE2OBxN1e0X3lg1d-04uMd5Ztzoxv5UCBWoZ1lyk205HpNn2R6xIjJwc0efvFaiIW_2II5b0rAOMv-TF1-dgJ53_hf--mTVJW3offJJRY1cAvARLyW0GYPl-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مارو دوباره تمیز و بکر شد
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/693720" target="_blank">📅 17:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWZjAv7i1oRlMqLsJsGOb3QHdXjaCY4kC3iMxo9F3gjXlpRd1-FTOAdzmgXPf9V7DJZXEN1vLRc7dw23Z0Z9-bi2viHImm62CaQI8rK5b-UT65-DGSN81tqmGhrrQgfUrKk1-zFTkUh2Pl30k2-D8QJy49kBhG3F8wARSK6fUJ3LY7aZyZhPvPLiT1Rmv-NA4GCSLEfkyGPHvjGhFaIsEB5z7XMfQMVV8L8zTgKv1_groQQ3eF3uF6rJoGYQD54yGOQ4iAucuL9MpAyZ2fYeC9mOWotiGAVQcV1fI3BcoZ-DCC_6-SGMtIoJL1z8LEi7_X_h1XgEB37xK4aO6MIdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ان‌بی‌سی نیوز: دو هفته پیش، یک موشک کروز ایرانی به یک کشتی در تنگه هرمز اصابت کرد و هشت نیروی دریایی ایالات متحده را مجروح نمود. آن‌ها دچار استنشاق دود و آسیب‌های مغزی تروماتیک احتمالی با علائم شبیه به ضربه مغزی شدند، اما طبق گفته سه مقام آمریکایی، آسیب جدی ندیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693719" target="_blank">📅 17:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc544c6945.mp4?token=KP1L6i4_TsUEtObyH-hYmvTbN3k2d7p28-sygRn8pPQ-_3Ggdv_5FtNNW70t1Ar9ESV9OeKwZ0KY8YgQ8r9Q-cUJphpZDPrPg72_iDT8RJbpQQeqxICfTYmpq8_yflM_F7Jrq2U3XzXZ8wtRsUb8ut5GNBeQLqkoCvoAW9UEiV9ngtfDJ9EtmpuQ-u2FWc6O1DtqiVNNPGLNMa7YJ-Ou94PaC-rv2rlpmCOlV2AnTFCHRQEkw8tRRdcS0ZgVmmpgVZzicaGtWDBynhhyJfbetDjJ_klNk3Zg-0KkFvhnkwFFwz9m05DgFq_RD_s-kXN7Fozg41RrPOLToYsI3iExfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc544c6945.mp4?token=KP1L6i4_TsUEtObyH-hYmvTbN3k2d7p28-sygRn8pPQ-_3Ggdv_5FtNNW70t1Ar9ESV9OeKwZ0KY8YgQ8r9Q-cUJphpZDPrPg72_iDT8RJbpQQeqxICfTYmpq8_yflM_F7Jrq2U3XzXZ8wtRsUb8ut5GNBeQLqkoCvoAW9UEiV9ngtfDJ9EtmpuQ-u2FWc6O1DtqiVNNPGLNMa7YJ-Ou94PaC-rv2rlpmCOlV2AnTFCHRQEkw8tRRdcS0ZgVmmpgVZzicaGtWDBynhhyJfbetDjJ_klNk3Zg-0KkFvhnkwFFwz9m05DgFq_RD_s-kXN7Fozg41RrPOLToYsI3iExfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از بامزه‌ترین ترافیک‌های دنیا در روستای کوهستانی سوئیس
🐑
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/693718" target="_blank">📅 17:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcNr8rDFOXCZCIelc1JMC5IrFBp1Cy8JzYo2T9NIOMk6THikfFLowCfyp9xy_HxP2kCaD3GVB1xVhWyHPqKNHtae85erkEu1qBA0Pz-g0WnJrSW5fdtEyeDFwjkBzcZxv-E7uG4_6xgB8GbffiaXueP7rmBLa4mX40ZEIrgmIqv_gyOw8IIZ76t9OUcWKTsZVw4_H6uI8rnNBrvQ69uwT09WMTiorJgMYFgLKQHff6fIOyWt-2A7-kOaSVQqXpGy-d9KHE2yl42oHd0xtC_9XYAWoCSD9LUhqJvbayoByY-A5LgE0zy59gvkSKLTAyOHxv2wYKPRFbLTMZlYtxzRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس تبلیغاتی باماتاپ برگزار می کند:
✨
همایش بزرگ «معمای پول»
✨
با هدف آگاهی از استراتژی های رشد مالی در شرایط فعلی
با راهبری علیرضا مطلبی
📅
زمان: جمعه، ۱۷ مهرماه |
⏰
ساعت ۱۰:۰۰ الی ۱۴:۰۰
📍
مکان: مشهد / مرکز همایش‌های بین‌المللی شهدای سلامت (برج سپید)
کد تخفیف زودهنگام به مدت محدود
BMT30
🎟
خرید بلیت زودهنگام:
https://evand.com
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693717" target="_blank">📅 17:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpDQp1pIAAWQxshXJyhsm3h08p4e_sTExezlWwVqUHrH47Y1gf00KbKTiChQuQSVXouVddaM9UYcS0odp_IuCJqtblUuKXfEPcZDmcaUD0RZkvfWHAgzmSXvAmRkCbqaYYzEwhsO3BUqkEOf9ZnHbtCf_e2l3Hyg8CMrqTnE4SzlmuCSc40ZgIQU0H3_hbhLuBx_1936QF08RGKkjlJp762BRd9rDLp-Mr6ciNnkKX5US55R1LMCRs5D1dL9qv3UFz038DfGn9KgSNZ_2Vey9JfEmNzjp51bJ5GWTAR9yKsDTrhXzvZsv-p2xHRKM5GKJltLn-i1P0VwdlXOnpC9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل صبر، این گل شگفت انگیز هر ۷ سال یکبار در کوهای نی ریز فارس می روید و عمرش فقط یک هفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693716" target="_blank">📅 17:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cc2d28b5c.mp4?token=UgtCr-BGRrgDsD84bN6lX6oH4X408jRnpdaK1XII-n9Ghv5cudh_rSZXJrhm-grJndDXF23F0fhyixC9iSR2p31TIUjSTI5FPW3hZpDyilN-gmsaYQcINB6sAZEwXnJf7ZtXn2K9KXmyRzdJiWnOIRKGv19fZXeHBSN7a9Rvx_5T4FnW49yn4ian6sQ4MThyu0304m2H46wt5tqnVFLx6tvgq-jYbz8li8Es9jQWx1PHytG5EZsO2hM1_VRPLRKrelKUAUcXxDzwrY8SChueLdhYqT4rYmP44xQlYLk_jq9dhPotegwkSh8NgGz3TEUO4BOqOpMZhbUkLgVN3r2CA7FxYyYjj_kYO6HoS9mMGwHHcM4qEHeCnZ14XIEil0mXR_qrQuBKBt8q0aFHVFp387plcnEF0TfVMNAXQ-d_Z9CFk7H98x1qhYUUI4G4T_vIP9cFLSiLXx4CUNWzoWjqaETdbLX6ghNRF37RdCWa_4brSo2fF9H5kLjOgMI0O9lT_2Zyg_ivt_ijQbPgmU6dG8i_-KPjYR0opGp3YcA3AkL2HQ9VpGacnYJT_COXl2EMqwJQT7Qjq1mrXXKKkOjBEWu_GiOfLEBjQT7K_AvbgNXBXv5WL1RNPjEUCtzzFVkkdZenIiBBjyhn8FPSl3KEvkKYvhNxkkQMwonaVuiR2MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cc2d28b5c.mp4?token=UgtCr-BGRrgDsD84bN6lX6oH4X408jRnpdaK1XII-n9Ghv5cudh_rSZXJrhm-grJndDXF23F0fhyixC9iSR2p31TIUjSTI5FPW3hZpDyilN-gmsaYQcINB6sAZEwXnJf7ZtXn2K9KXmyRzdJiWnOIRKGv19fZXeHBSN7a9Rvx_5T4FnW49yn4ian6sQ4MThyu0304m2H46wt5tqnVFLx6tvgq-jYbz8li8Es9jQWx1PHytG5EZsO2hM1_VRPLRKrelKUAUcXxDzwrY8SChueLdhYqT4rYmP44xQlYLk_jq9dhPotegwkSh8NgGz3TEUO4BOqOpMZhbUkLgVN3r2CA7FxYyYjj_kYO6HoS9mMGwHHcM4qEHeCnZ14XIEil0mXR_qrQuBKBt8q0aFHVFp387plcnEF0TfVMNAXQ-d_Z9CFk7H98x1qhYUUI4G4T_vIP9cFLSiLXx4CUNWzoWjqaETdbLX6ghNRF37RdCWa_4brSo2fF9H5kLjOgMI0O9lT_2Zyg_ivt_ijQbPgmU6dG8i_-KPjYR0opGp3YcA3AkL2HQ9VpGacnYJT_COXl2EMqwJQT7Qjq1mrXXKKkOjBEWu_GiOfLEBjQT7K_AvbgNXBXv5WL1RNPjEUCtzzFVkkdZenIiBBjyhn8FPSl3KEvkKYvhNxkkQMwonaVuiR2MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: صراحتاً گفتند ارز ۲۸۵۰۰ تومانی تمام شده/ اگر تمام شده، قرار است چه چیزی را برای مردم جبران کنید؟
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در جلسه ای در مجلس بحث کالابرگ مطرح بود و این استدلال مطرح شد که ما ارز ۲۸ هزار و ۵۰۰ تومانی میدهیم و این رانت و فساد است.
🔹
استدلال دی ماه این بود که ارز ۲۸ هزار و ۵۰۰ تومانی رانت است و پایه پولی را بالا میبرد. هم چنین دیگر ارز ۲۸ هزار و ۵۰۰ تومانی نداریم.
🔹
صراحتا گفتند ارز تمام شده است. در نتیجه گفتند به جای آن یارانه ای که قرار است به صورت ارز ۲۸ هزار تومانی به مردم بدهیم، به صورت کالابرگ می دهیم.
🔹
همین جا یک تناقض وجود دارد که اگر ارز ۲۸ هزار و ۵۰۰ تومانی تمام شد دیگر کالابرگ چه معنایی دارد چون ما در بودجه ۱۴۰۴ رقمی برای جبران شما نگذاشته ایم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693715" target="_blank">📅 16:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693714">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رسانه‌های عراقی: طی ۲۴ ساعت آینده ممنوعیت ورود پروازهای ایرانی به فرودگاه نجف اشرف لغو می‌شود./ایسنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693714" target="_blank">📅 16:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
توضیحات قوه قضاییه در خصوص پرونده رسایی  قوه قضاییه در اطلاعیه‌ای:
🔹
در صورتیکه حمید رسایی موفق به جلب رضایت شاکی خصوصی خود می‌شد پرونده در دادسرا بسته می‌شد.
🔹
مطلب «دستکاری قالیباف در اسناد مجلس» در دی ۱۴۰۲ در رسانه‌ ۹ دی منتشر شده که در آن زمان رسایی کسوت…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/693713" target="_blank">📅 16:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49026b2418.mp4?token=a24p1todZLemrHf3gw3ufrKpd4Yk07f7EyQjLJmXjquS5sbZ0n8bkqHwAPJwRV2UUe_uvpQc40ayqMSNoTNgvqSgd2Si9kZ6RWNn-Ex9ubEpB-9cB48S0lmqmXBlF-2YEdmJw5aeTXYsRFlee0hJuka9jqXAMQOsqGn2bY_UU-CTePTUoXUzK3XvsJ00eJoMtUyp-yEyk03zsONKzRHKe7SuNiihXrIPMTnk_6IXNwxzazz-o-POEIS4suaZk0g_CMG1GG2qRPD6B14nLCZcVmdMlRUtJpuzTrBLUi5Qj2XL69nQ8jF47NyM6tmK0Sc8y3PyGWaOw48rVt5R6pZO0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49026b2418.mp4?token=a24p1todZLemrHf3gw3ufrKpd4Yk07f7EyQjLJmXjquS5sbZ0n8bkqHwAPJwRV2UUe_uvpQc40ayqMSNoTNgvqSgd2Si9kZ6RWNn-Ex9ubEpB-9cB48S0lmqmXBlF-2YEdmJw5aeTXYsRFlee0hJuka9jqXAMQOsqGn2bY_UU-CTePTUoXUzK3XvsJ00eJoMtUyp-yEyk03zsONKzRHKe7SuNiihXrIPMTnk_6IXNwxzazz-o-POEIS4suaZk0g_CMG1GG2qRPD6B14nLCZcVmdMlRUtJpuzTrBLUi5Qj2XL69nQ8jF47NyM6tmK0Sc8y3PyGWaOw48rVt5R6pZO0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاییز اومده، انار رو اینجوری قاچ کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693712" target="_blank">📅 16:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693711">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سفارت ایران گمانه‌زنی‌ها درباره ارتباط با حادثه فرفورد را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693711" target="_blank">📅 16:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رسانه‌های انگلیسی: پلیس انگلیس در حال بررسی ارتباط ایران با یک طرح مشکوک به بمب‌گذاری در پایگاه فیرفورد (محل استقرار بمب‌افکن‌‌های آمریکایی) است
🔹
ظهر امروز پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/693709" target="_blank">📅 16:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147301ed24.mp4?token=KcJ8dh0RdkAsDkTcOqrIlfz6SYx6DMSiIbABUz5up98rTLFdVLC2-hyDjXOGnG1Dc4aAtOJSj0Ch8WE8E4pk-PIr0Mg2lU_-jy6P4WXXfiwTr7Ib7Z7vxRDGlyOVwO1ZZ8E6QmreTdMryus-NPgCAbADjzbNa9dxTiK64cKsPl3CayMWdcUMqUgpj9Y-pXR2JyUiReGDn91ncuvmNMHks-rU4fPChkiGzPRwaJFSKKBC-ueLs8kNg4f1lbjewTELIXOvLqACvs9eYZUDlDF71dJmox_FUCtwROi-LkewL60pj8vGCk1zTYYr_BNjS0P_GytSphYBcZZUFRKcwxNvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147301ed24.mp4?token=KcJ8dh0RdkAsDkTcOqrIlfz6SYx6DMSiIbABUz5up98rTLFdVLC2-hyDjXOGnG1Dc4aAtOJSj0Ch8WE8E4pk-PIr0Mg2lU_-jy6P4WXXfiwTr7Ib7Z7vxRDGlyOVwO1ZZ8E6QmreTdMryus-NPgCAbADjzbNa9dxTiK64cKsPl3CayMWdcUMqUgpj9Y-pXR2JyUiReGDn91ncuvmNMHks-rU4fPChkiGzPRwaJFSKKBC-ueLs8kNg4f1lbjewTELIXOvLqACvs9eYZUDlDF71dJmox_FUCtwROi-LkewL60pj8vGCk1zTYYr_BNjS0P_GytSphYBcZZUFRKcwxNvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رقص ایتامار بن‌گویر در مسجدالاقصی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/693708" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d969ab6024.mp4?token=D6n23JJTs9NQu00wgLA3q4265UhEi2kXclUpFejkgglKHb4sO42Q2MCSPJCsO-paL8maTIthPpInm47dM4XijiXhS8lumF3YSekY4_G8xFDyJVBqavCY5J5Oq5HhRuxYKLtAAlPg27_Sb0BEY0ikKToV7RAdljKEU7TgMGRdoEv34HK2ATb8HMoDk-cq5yY86G7z02NtNjk252WXDySpUVd7yfPCYOVCTnwv8zmRrnrfC58ykJs2ubDvXuHYBrbeZmGJKr_gfuUuoNA0LHDg1sm4G8guM0C6ifoU6pd_WPhHHMNY0SvBQXLMQclbJagHEAukuICw83BaT7sbLGdSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d969ab6024.mp4?token=D6n23JJTs9NQu00wgLA3q4265UhEi2kXclUpFejkgglKHb4sO42Q2MCSPJCsO-paL8maTIthPpInm47dM4XijiXhS8lumF3YSekY4_G8xFDyJVBqavCY5J5Oq5HhRuxYKLtAAlPg27_Sb0BEY0ikKToV7RAdljKEU7TgMGRdoEv34HK2ATb8HMoDk-cq5yY86G7z02NtNjk252WXDySpUVd7yfPCYOVCTnwv8zmRrnrfC58ykJs2ubDvXuHYBrbeZmGJKr_gfuUuoNA0LHDg1sm4G8guM0C6ifoU6pd_WPhHHMNY0SvBQXLMQclbJagHEAukuICw83BaT7sbLGdSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدحسین احمدنژاد، مدیر روابط عمومی سازمان منطقه آزاد کیش با انتشار این ویدئو از ایمان قیاسی نوشت: برنامه قهرمان در دوره جنگ در کیش ضبط شده است‌ و تصاویر و ویدئوهایی که امروز از آن منتشر می‌شود، مربوط به ماه‌ها پیش است.با این حال، برخی رسانه‌ها به‌ اشتباه این تصاویر را به روزهای اخیر نسبت داده‌اند. زمان ضبط و تفکیک آن از زمان انتشار از اصول اصلی اطلاع رسانی‌ست. زنده باد ایران و ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693706" target="_blank">📅 16:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حسین صمصامی، نماینده مجلس: گفتند ارز ۲۸۵۰۰ تومانی به سفره مردم اصابت نکرده/ پس چرا با حذفش قیمت کالاهای اساسی یک‌دفعه بالا رفت؟
حسین صمصامی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
با حذف ارز ۲۸ هزار و ۵۰۰ تومانی قیمت کالاها افزایش یافت و این نشان می‌دهد رانت بر سفره مردم نشسته و به آن اصابت کرده است.
🔹
گفتند ارز نداریم. سوال این است پس در حال حاضر محل تامین کالابرگ از کجا آمد؟ آمدند با اذن رهبری دو میلیارد از صندوق برداشتند و گفتند این را تبدیل به ریال کردیم. شما که می‌گفتید ما ارز نداریم خب همین را برای کالاهای اساسی می‌دادید.
گفتند این دو میلیارد کاغذی بود و ریال آن را بانک مرکزی داد که همین موضوع پایه پولی را افزایش داد.
🔹
همان آدم‌ها یعنی رئیس سازمان برنامه بودجه، وزارت رفاه، بانک مرکزی، رییس مجلس و کمیسیون‌های اقتصادی مجلس دوباره در مجلس جمع می‌شوند و طلبکارانه می‌گویند ما ارز نداشتیم و باید حذف میشد. همان استدلال‌هایی را که در دی ماه مطرح کردند، دوباره دارند همان‌ها را مطرح می‌کنند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/693704" target="_blank">📅 16:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1KYcNiffHPfxe1Jp0MQxkJlXYwliZpur3KSPr9LL8zlPJPASU2QDWXMWv6GZABoFMqBTGqeDmnpho7K_5UKkkQ_s-LoaqoUXYoaEFGp4mtnZSDV2d3dSw2ZZqBSukT5fQbSL6CrIn4LUPHueQSST31O2y0fndxVS6-61eDIv36Eo4j4AhRLZhgRiXczGvIO50Q7PREtctRw_yIphIDJcE5tALS57gGVyxqaBULRk8wq74Han905PVjwj32ZnEsVn--HBWHabjam6XT3DgEfplMulD68gswSFqKKQ36N3g1rl1BZb8INC9gmrqtLc3bDlGAC4e-DRwx-Mr-9ezlGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق [سلطه‌گری استعمارگران بر ایران] که دشمن ما آرزوی بازگشت به آن را دارد، گذشت و دیگر هیچگاه تکرار نخواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/693703" target="_blank">📅 16:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پزشکیان به سی‌بی‌اس نیوز: تیم ۶ نفره از نهادهای مختلف درباره سیاست خارجه تصمیم می گیرند/ بی‌اعتمادی میان ما و آمریکا مانع مهمی برای دیدار مستقیم با ترامپ است
🔹
اگر آمریکا جدیدترین پیشنهاد ایران برای بازگشایی تنگه هرمز را بپذیرد، تهران به تعهدات خود پایبند…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/693702" target="_blank">📅 16:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مرزبانی هرمزگان: دستگیری ۵۰ متجاوز مرزی و توقیف ۲ فروند شناور متخلف در آب‌های هرمزگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693701" target="_blank">📅 16:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3d1c7f42.mp4?token=T5h0hXmYanONPmJYdiMiIwGQsC9ceBAHTR7-xyPSVD8wSjJRDz3hlDaA-eCnvhnFgHIaXaxY-uzxXp1ijsaw2F3baJa5S7nrQocx4j64mbiwU_oRnFVoZLK7I6ZF4khtBJVWBL21uXWnXd5oBd5Uo9rXC4-kDAvrkBA59iksSl3OMt6MM4nJt-SkO1U7jW2WHDIVCkaS0eB_Dol7UO6P_mM0k1ICTTcfaY06eeeyjKYqDAbkh5SYULl2YbwH0NzxE_vrEJy1lOOrasnZCH2yA3rH5pmD5Fyddwwy8GY9uUZrpmtFAtL4MAyUaffmVhYiJxTuU9j08KY3VQTgeBNHEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3d1c7f42.mp4?token=T5h0hXmYanONPmJYdiMiIwGQsC9ceBAHTR7-xyPSVD8wSjJRDz3hlDaA-eCnvhnFgHIaXaxY-uzxXp1ijsaw2F3baJa5S7nrQocx4j64mbiwU_oRnFVoZLK7I6ZF4khtBJVWBL21uXWnXd5oBd5Uo9rXC4-kDAvrkBA59iksSl3OMt6MM4nJt-SkO1U7jW2WHDIVCkaS0eB_Dol7UO6P_mM0k1ICTTcfaY06eeeyjKYqDAbkh5SYULl2YbwH0NzxE_vrEJy1lOOrasnZCH2yA3rH5pmD5Fyddwwy8GY9uUZrpmtFAtL4MAyUaffmVhYiJxTuU9j08KY3VQTgeBNHEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غروب زیبای خلیج گرگان
🌅
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/693699" target="_blank">📅 16:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87bee21d98.mp4?token=Le3cgUv_fMbhXkJq-GkDKNdY5bFF_v-fOyS14IkXhYniVgvdcKPn0VZcojuwnuJqHs7Ql5DZ1Xzfb6xAfvi71-cpT_V-nGUUDgtCWLOdVLPgfe5boUTuhwzclEzltdgRQ-ka094-9pGGbtOn5s3Bw8b51uAdigyFmjLQbUY0a_DYRb0TVEc5tFcJMl_oowgE8WGF6Fhu6Wm3ZbBd4LcKi2GqKeorb1lKa51DzS90d5fV-88_yOyWAVp9xcGq_3wxD_SjnvsT--zdr8iih3tfwR9WfhEU7bosNykr6CcAe3_4KqQs8WO9ZQ5LqMEYISKgLgqz3Cjb4PTMcmS-8Fg0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87bee21d98.mp4?token=Le3cgUv_fMbhXkJq-GkDKNdY5bFF_v-fOyS14IkXhYniVgvdcKPn0VZcojuwnuJqHs7Ql5DZ1Xzfb6xAfvi71-cpT_V-nGUUDgtCWLOdVLPgfe5boUTuhwzclEzltdgRQ-ka094-9pGGbtOn5s3Bw8b51uAdigyFmjLQbUY0a_DYRb0TVEc5tFcJMl_oowgE8WGF6Fhu6Wm3ZbBd4LcKi2GqKeorb1lKa51DzS90d5fV-88_yOyWAVp9xcGq_3wxD_SjnvsT--zdr8iih3tfwR9WfhEU7bosNykr6CcAe3_4KqQs8WO9ZQ5LqMEYISKgLgqz3Cjb4PTMcmS-8Fg0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهران غفوریان به تلویزیون برگشت؛ این بار با یکی از متفاوت‌ترین و هیجان‌انگیزترین مسابقه‌های تلویزیونی!
🔹
«بی‌باک»؛ مسابقه‌ای متفاوت با یکی از بزرگ‌ترین دکورهای تلویزیونی که قرار است مخاطب را وارد شهری کند که ورود به آن جرأت می‌خواهد…
🔹
برای استفاده از این کلید، باید بی‌باک باشی!
🎬
مسابقه بزرگ «بی‌باک»
با اجرای مهران غفوریان
به‌زودی از شبکه سه سیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693698" target="_blank">📅 15:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3219369b01.mp4?token=Mey6rssjHjqdiwS0doplMc6VJc7aaJUxLxajnB62_ttc0VuxPNPwclcb1OXWKY-BUWSNi3-v8ZKT6rw3LHuNWQvxwCajpMXJ4oiQfeWYE0pyuXjJyBSSExetUeaHGjxmup8FkFWhF1blHfOlBxS7T21AvO1HlcEgdnR7kfo5Fhh7EGBSTC3m36S5cG9XLy0gTof3Pdv4HU4hNtiZSkAqJGprtN9XEmB_S1jxFxDj8lAaaihmJ_HHaYRP1xXJfUSOdhxrBP_0zBn-IRWXpwcaPpYx_IrSMJlnNa7RDNyV2eWFmBzDIcCOPl2C8ugysV7l4U_-dl7kMJyuOvoRehvK7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3219369b01.mp4?token=Mey6rssjHjqdiwS0doplMc6VJc7aaJUxLxajnB62_ttc0VuxPNPwclcb1OXWKY-BUWSNi3-v8ZKT6rw3LHuNWQvxwCajpMXJ4oiQfeWYE0pyuXjJyBSSExetUeaHGjxmup8FkFWhF1blHfOlBxS7T21AvO1HlcEgdnR7kfo5Fhh7EGBSTC3m36S5cG9XLy0gTof3Pdv4HU4hNtiZSkAqJGprtN9XEmB_S1jxFxDj8lAaaihmJ_HHaYRP1xXJfUSOdhxrBP_0zBn-IRWXpwcaPpYx_IrSMJlnNa7RDNyV2eWFmBzDIcCOPl2C8ugysV7l4U_-dl7kMJyuOvoRehvK7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک خرس به طور اتفاقی وارد یک بازار محلی شد، مستقیماً به سمت یک غرفه نانوایی رفت و شروع به خوردن نان کرد
🐻
🍞
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693697" target="_blank">📅 15:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QCP63rFnIrK_Bm9p1ZYLeSB-9xCokUXUlLojxIqYT9SEzhkzzwvGczdHHF9e2Hw53YaePQTAvnhhRfJbi8F2LevKiwtj14VIbQPp3VRaPt4oiNzorUPF2PPeqGuy30HbR89UqA4uS1Owuhy95PzdwY3p-pQeml8819GBOS9mKAbR_SdPQlTy3Awj5mL_yff7AXWAnr79sG2BAxUXcQXiaKAuovsvPwCmL6sHgU1K4ibamptUboIITitdxixmqM1LpdapOf_mnAyMCL-1bsvPg8TMn5ibmj2_9SfnDm9zfVgRjkBkeS-5c6Fuk0zdxhE_i-H-LV8zFktr2YiOkDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک مرکزی چک‌پول ۱۰۰ هزار تومانی جدید را با تصویر یادمان شهدای مدرسه میناب و ویژگی‌های امنیتی منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/693696" target="_blank">📅 15:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای پوشالی سنتکام: ایران نیروی دریایی ندارد، زیرا نیروهای آمریکایی آن را غرق کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/693695" target="_blank">📅 15:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
طرح غربالگری سلامت معلمان هنوز به مجلس نرسیده است
محمدرضا احمدی سنگر، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح غربالگری سلامت معلمان تاکنون در مجلس مطرح نشده و جزئیات آن نیز در اختیار کمیسیون آموزش نیست.
🔹
احتمال دارد این طرح در قالب یک دستورالعمل داخلی وزارت بهداشت دنبال شود که در این صورت، مجلس فعلاً نظارت مستقیمی بر روند اجرای آن نخواهد داشت.
@TV_Fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/693694" target="_blank">📅 15:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ug7mH48jBGa6P1AtJfHqLw6BIx7VO75_HF11nNNt1NRjmaXm3-dmkZ5pzLygv8vU2Y5OEvoeq7QkEBcXJiBPdPav8cOMzbAUNULUzhZUBYEdW1siirYBAk5TXredqAOWHBihxhVorvur4I-YAFU33geqxNPA9mz9mikfyqmhGk6T6hZL1fYhvPeQ17jES09s-jB16T-mzVUHfY-ShO_ssd0YGD61e0ulx5qeGiT2GemV4MaoDtm9eKklfoz6raYdG9sX32t-53AzVs113SIbXqaGp7WdAVQEC4QXxMmkYThlG28C-HJz35jPiLNnO2h_FlGW7etOzTOixdPV8ueg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
طلای خود را فیزیکی تحویل بگیرید
🔹
در
طلاسی
امکان
تحویل فیزیکی
سفارش‌های
طلا
فراهم است.
شما می‌توانید با ورود به بخش «
تحویل فیزیکی
»، طلای موردنظرتان را انتخاب کنید و سفارش خود را به یکی از این
دو روش
دریافت کنید:
✅
تحویل فیزیکی درب منزل در سراسر ایران
✅
تحویل حضوری از شعب طلاسی
کافی‌ست وارد بخش «
تحویل فیزیکی
»
سایت
طلاسی
شوید و روش تحویل موردنظرتان را انتخاب کنید.
👈
خرید طلا با تحویل فیزیکی
👉
❤️
@talasea_mag</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/693693" target="_blank">📅 15:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رویترز به نقل از منبع آگاه: میانجی‌ها امروز یا فردا در نیویورک، مذاکرات جداگانه‌ای با آمریکا و ایران برگزار خواهند کرد
🔹
عباس عراقچی و میانجی‌ها در نیویورک می‌مانند تا مذاکرات را احیا کنند. مذاکرات در نیویورک بر نسخه‌ای اصلاح‌شده از آخرین پیشنهاد ایران متمرکز خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/693691" target="_blank">📅 15:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رهبر انقلاب: بنده به‌عنوان خادم مردم عزیز ایران اعلام می‌کنم که آن روزهای سابق [سلطه‌گری استعمارگران بر ایران] که دشمن ما آرزوی بازگشت به آن را دارد، گذشت و دیگر هیچگاه تکرار نخواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693690" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نماینده دائم روسیه در سازمان‌ ملل: ایالات متحده از سال ۱۹۸۰ تا به حال منتظر فروپاشی اقتصاد ایران بوده است و برای آمریکا بهتر است دست از این انتظار بیهوده بردارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/693689" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110ed92196.mp4?token=tDDBY--1IW789yS0evzRpP6KCgAtRd514JuxlrjaQC6mvTPaXJNaPQsE4SKrTGmLp9bJIESAsFVpF84iLVLadoBipgjmWSBe8fmGcFbzMrz_phwXojrVQAYECWKmi8AZBc1ZhQQWFqdYQ-pIxp2CAZKFWns-oe5Wtr3J_3LXqxkfxSwflAttlxKwtdYwmyEh9QtOPQkwjJnjVUuVbGVz-hGchIXhdlyit21VfINKD94UO-F122Dyq2QRwTu9tyN9tMfsrCHUNMA3P1oP_a2yKNsH1QIRiFxj1RDAXq3t9chN_v52l--mzRW4MLX_ot1C1gycT_700KsnuvM4_ikgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110ed92196.mp4?token=tDDBY--1IW789yS0evzRpP6KCgAtRd514JuxlrjaQC6mvTPaXJNaPQsE4SKrTGmLp9bJIESAsFVpF84iLVLadoBipgjmWSBe8fmGcFbzMrz_phwXojrVQAYECWKmi8AZBc1ZhQQWFqdYQ-pIxp2CAZKFWns-oe5Wtr3J_3LXqxkfxSwflAttlxKwtdYwmyEh9QtOPQkwjJnjVUuVbGVz-hGchIXhdlyit21VfINKD94UO-F122Dyq2QRwTu9tyN9tMfsrCHUNMA3P1oP_a2yKNsH1QIRiFxj1RDAXq3t9chN_v52l--mzRW4MLX_ot1C1gycT_700KsnuvM4_ikgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باگ عجیب سیستم‌عامل iOS 27
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/693688" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWle-H8V2tGh8w9BUFL0LhQtq7INQvEt3LB4xOwIuiyYF6IXAC3oKIPSIl_6VpLzHGVYeUJ94PiaLKA1J7jaDCOsatANOh84NgTQkojE9w62eq0oalaIqxfxugleaapOiGvbeCAmJ_oPULAuxPNc7PWCOEvpL-k2dCJnu0v4b0YsjIP17mPqaqfFHMo4YwVRQP3QxamnLPefZVNe-guiOUOLeMLsYIY0OhGPjzt-wAXNHXgNz90bbGxhaqvf9Wof6C6EbMayweBCaCBdOM_GUn65LpoZGqxfyvlD3FOxHRaSSdBIJgTCctDs9oCXSal8a8YIGLL4T1gN582Kd-ZQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتخب مسابقهٔ «عکاسی نجوم» سال ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693687" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e7f52399.mp4?token=dy3UPPtvvE6AqcIgxunyB2T9lpAW-tBDyPM2pNPVNdMF8-6d9qNMnYiCeDhlwNxru7IobN9OSmTiDXBqsLwgYnYguigOeDoI6J6jmaM92apuTI-WAnOs8IOvyUjgtaLDqFIjM9BZSH1UCflX-yHEVV6n2-_6RE8LnddswSjPCxLd293cP7B2ukgkEZzQ2r11-Ix4XP0T2mjobrMQacDVgyuFG5UChdWCJ1b4z9neQInykWBbarGEYOKxrEtLSD3pR0ZLoQSjfgaMwQ9SUZfI0aSXBltC0H_GhX8lw5QEaFHLs-fddUZC8mVB1V4IIonEseRIvlNCEVCObPTwZUGJCwZzt_nssvPLl5Yjrq7qkgyHAX0mAACLu7zqcviUupuHW6MlwEvAo524JFDajVwD59kJ4F2kJj09lFhnWZZQrLMS_3dIXE-aJwIMJIU0vnQuNA6ZgWFjHGn3C5dj2laFWTTwy1eYtuKUTWvQorgq6cIi_a56j0cC3qgfUNLsg0f7gr-sX6iBtIGlCkEhywsSfkl36SO0dpR4mdvHIUrb1O7dpg2RW8qo2CggiQEmMgl1tSuiv-7fzTb-Abo_YYEaJGQdRUe4iq2cxgERc8MlJxI5jHucQE-lZYpVwYKzytaORwtKoP1zYMaXXCFUWybeS2Lu7_iftsVPKUEjSYEIEbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e7f52399.mp4?token=dy3UPPtvvE6AqcIgxunyB2T9lpAW-tBDyPM2pNPVNdMF8-6d9qNMnYiCeDhlwNxru7IobN9OSmTiDXBqsLwgYnYguigOeDoI6J6jmaM92apuTI-WAnOs8IOvyUjgtaLDqFIjM9BZSH1UCflX-yHEVV6n2-_6RE8LnddswSjPCxLd293cP7B2ukgkEZzQ2r11-Ix4XP0T2mjobrMQacDVgyuFG5UChdWCJ1b4z9neQInykWBbarGEYOKxrEtLSD3pR0ZLoQSjfgaMwQ9SUZfI0aSXBltC0H_GhX8lw5QEaFHLs-fddUZC8mVB1V4IIonEseRIvlNCEVCObPTwZUGJCwZzt_nssvPLl5Yjrq7qkgyHAX0mAACLu7zqcviUupuHW6MlwEvAo524JFDajVwD59kJ4F2kJj09lFhnWZZQrLMS_3dIXE-aJwIMJIU0vnQuNA6ZgWFjHGn3C5dj2laFWTTwy1eYtuKUTWvQorgq6cIi_a56j0cC3qgfUNLsg0f7gr-sX6iBtIGlCkEhywsSfkl36SO0dpR4mdvHIUrb1O7dpg2RW8qo2CggiQEmMgl1tSuiv-7fzTb-Abo_YYEaJGQdRUe4iq2cxgERc8MlJxI5jHucQE-lZYpVwYKzytaORwtKoP1zYMaXXCFUWybeS2Lu7_iftsVPKUEjSYEIEbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وسط جنگ، کدام بازار به مردم سود داد؟
🔹
فکر می‌کنید در وسط جنگ و تعطیلی‌های پیاپی، پول در کدام بازار سود کرده است؟ جواب این سوال شاید خارج از انتظار شما باشد!
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/693686" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-tx1tzYSeMOnlwVKyGYQ3JdT5NSXQmD2lSJflUmajZ6hWeEJSXYgzE0i1c6mOFZZxy3VmiM66yDc_WgWbbblmhv_U-WyDYDpAwypMUgbijmUIkE_33EhK9UJBH52Ny7_dH8l7B7-0BpDDc0IwE10CRjq-SXDiKuYyetMzMJKQXEiKSB10mdKt8lQG9dVBTboPTSVrPIj8wrfmdsNIP-uMk4yGhJihcgKCzWddyurGamCYh5--WnQEG8NevZMKqT6g0k2dl7Qmkt6J642zBIySXBIUwEcfy_I0T3Ybltzz9lg9XSsoVRm9bTlS-SRcow83EUPjlQlABRiT0TcihPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همایون شجریان هنرمندان را به «هر جا که تویی» دعوت کرد
🔹
همایون شجریان با اهدای لپ‌تاپ شخصی خود به کمپین «هر جا که تویی» دیجی‌کالا مهر، از دیگر هنرمندان خواست به این جریان انسان‌دوستانه بپیوندند.
🔹
او در پیام خود تأکید کرد که یک لپ‌تاپ می‌تواند نقطه آغاز تغییر در زندگی یک دانش‌آموز باشد و از مردم خواست در کنار دیجی‌کالا مهر، برای ساختن فرصت‌های آموزشی برابر همراه شوند.
🔹
کمپین «هر جا که تویی» دیجی‌کالا مهر با هدف حمایت از دانش‌آموزان مستعد مناطق کم‌برخوردار و فراهم کردن دسترسی آن‌ها به ابزارهای آموزش دیجیتال شکل گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/693685" target="_blank">📅 15:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693683">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e617f48c.mp4?token=SAFHo1nzlrwVdBdgevnfL2kSldE8wudwpZXsJpisO4LCj6E3vQWXU4CEf3AkIh3mZnOJmDunwON1mlAOUKqsHxgCClT36Qepk6GD22jL3FnjxPPEOkuM9PDg75Thja2Ok1qzLPHgvnPz9PvIuZ8OUdCyIf7YPTE7KBcA_2wT4L867w8KL4EGZDvM9e7wUxtDx-sHnBs11euNnMKby_QH6s7IooKwVSpB6s6fL09nUrk3K1EXHVVZ5tWvrMlVlhJQOXfxWTx_YJB1lmpizv816ndsF_VdSl6UIyb6VGaYS1asAG1aNuPGB2dzNGmddG_VZt0rFa3x4_LzeFJjgoxt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e617f48c.mp4?token=SAFHo1nzlrwVdBdgevnfL2kSldE8wudwpZXsJpisO4LCj6E3vQWXU4CEf3AkIh3mZnOJmDunwON1mlAOUKqsHxgCClT36Qepk6GD22jL3FnjxPPEOkuM9PDg75Thja2Ok1qzLPHgvnPz9PvIuZ8OUdCyIf7YPTE7KBcA_2wT4L867w8KL4EGZDvM9e7wUxtDx-sHnBs11euNnMKby_QH6s7IooKwVSpB6s6fL09nUrk3K1EXHVVZ5tWvrMlVlhJQOXfxWTx_YJB1lmpizv816ndsF_VdSl6UIyb6VGaYS1asAG1aNuPGB2dzNGmddG_VZt0rFa3x4_LzeFJjgoxt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل ۲۸ ساله شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/693683" target="_blank">📅 15:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693682">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1BnIvyo31ZUoZIUF4aa30EtNBVopeANVKm9B61kZNMCbnKIwkBwKDfV7z5uErUXMSVgGXQQ6w79B7o2NTrzgkg9N3Ulmwxv5yQoVQyRfWryMcxvgcEaU2Q5rzIMEUUni7urzA-GRS438K1SYldSzo3ZmnTqeMvMxEKHy4YhNPz8vpP5ubkFgm1GGaxBmZuruAOb1Qn-2-PVFXnkyt3gyXgcRJpwmiKdhQbvU-EHJkKugcGS8ZM6x1ZeqO5atYXmoiobvgsEawtugyCyMK3ipDOXLUqERFoTOGDw8wD9-D3Q7ViBrcnnAs22fB1ByT80uhaRjw4rEPHFe_7EdHci3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور عسل طبیعی رو تشخیص بدیم
🍯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/693682" target="_blank">📅 15:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693681">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98930222f.mp4?token=iFsG2xsTusia2m9aAWGucoIG6_EW2-b776JrzlBb3MPDMw4CZC_VUUr1-0Pn1CF9Aop185r1lIrbecdRmJwhILb9oLgP9HnttrdoBgPfVH-eDsQoSBk9vQooE2EJkDvbfe3JAJ7TGi8S1OD3zyMANBSHtTVq1UGzYi2Kq-Vj8oNRo3agYTVIiqy191ZxY_O_fv54UF5opobR5BAN1QF1anWIeo1jEoLXQoh4GH-21Anz2huKzO02le4id4Yy1_CLL4M3-KvSsG_msZSwJ35PknXK9iJcL3Zh3BL0o9a4ncpWB5wc2odm0vyEy9vP9xu02DcAfq9AONkGndjtg06-a5okw9RYOZp5_hbHzln6q8Zdc3xzhGTXlM6nlGlVg44h8nr_jiw_osQMMzLaSWHQPlUjBWvm3RO9uH0_EYi9MF2XMwzXn29gkjYmLu0SUtL5lAl832_uwaDvCzfDU7R0xBYsY9a1NYARyuxW_iec7U9KoiuWlPhG1LYOdoAXa-tH8TmSba2J1hGSvSM0KRiZ-rw5eMRFzEpmDOEi_YFD2jkdVPoGkfRmAr50kPJs3JdLcKFbgqrNRkZppk89RmfECsqEP3EwVNbXnOXx9MvV_bTqdQ8xzl0Kn-JPzolSAWJL8-Xj1BM4FfcGcc0LC4ehS2WCy_IH_hAaN_qDerqy2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98930222f.mp4?token=iFsG2xsTusia2m9aAWGucoIG6_EW2-b776JrzlBb3MPDMw4CZC_VUUr1-0Pn1CF9Aop185r1lIrbecdRmJwhILb9oLgP9HnttrdoBgPfVH-eDsQoSBk9vQooE2EJkDvbfe3JAJ7TGi8S1OD3zyMANBSHtTVq1UGzYi2Kq-Vj8oNRo3agYTVIiqy191ZxY_O_fv54UF5opobR5BAN1QF1anWIeo1jEoLXQoh4GH-21Anz2huKzO02le4id4Yy1_CLL4M3-KvSsG_msZSwJ35PknXK9iJcL3Zh3BL0o9a4ncpWB5wc2odm0vyEy9vP9xu02DcAfq9AONkGndjtg06-a5okw9RYOZp5_hbHzln6q8Zdc3xzhGTXlM6nlGlVg44h8nr_jiw_osQMMzLaSWHQPlUjBWvm3RO9uH0_EYi9MF2XMwzXn29gkjYmLu0SUtL5lAl832_uwaDvCzfDU7R0xBYsY9a1NYARyuxW_iec7U9KoiuWlPhG1LYOdoAXa-tH8TmSba2J1hGSvSM0KRiZ-rw5eMRFzEpmDOEi_YFD2jkdVPoGkfRmAr50kPJs3JdLcKFbgqrNRkZppk89RmfECsqEP3EwVNbXnOXx9MvV_bTqdQ8xzl0Kn-JPzolSAWJL8-Xj1BM4FfcGcc0LC4ehS2WCy_IH_hAaN_qDerqy2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رشیدپور: اینقدر ما خریت کردیم که گفتیم امریکا دشمن ما نیست که کار به اینجا رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/693681" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693680">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
با افزایش قیمت بنزین مصرف CNG در کشور ۱۵ درصد افزایش یافت
احسان جان‌محمدی، رئیس انجمن صنفی CNG در
#گفتگو
با خبرفوری:
🔹
روزانه حدود ۴.۱ میلیون لیتر CNG جایگزین بنزین شد و مصرف روزانه بنزین نیز در مجموع ۹ میلیون لیتر کاهش پیدا کرد.
🔹
حدود ۴.۹ میلیون لیتر از کاهش مصرف بنزین نیز ناشی از کاهش مصرف خودروهای بنزینی و تغییر رفتار مصرف‌کنندگان بوده است.
🔹
در نیمه دوم شهریور و همزمان با افزایش قیمت بنزین مصرف CNG در کشور ۱۵ درصد افزایش یافت.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693680" target="_blank">📅 14:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693679">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نخستین کشتی سوخت‌رسان سه‌منظوره ایرانی تا دقایقی دیگر بهره‌برداری و وارد آب می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693679" target="_blank">📅 14:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رهبر انقلاب: اینک پرچم پرافتخار او [سید حسن نصرالله] در دستان جناب شیخ نعیم قاسم حفظه‌الله است که دلیرانه در پیشاپیش صفوف مستحکم و عاشورایی حزب‌الله، راه او را همچنان ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/693678" target="_blank">📅 14:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1941cb0cd1.mp4?token=umCLxaCTzo9em-U_ZbjENBD5bOjbG866nHVPQ1XTEULT3hdjnTw-ir6OVGqyUb_DDyxebyEN90zYei8DhP-08WffMA2pf64Mkcd1Kwz8xmA6rTFiQrLoaxlu8yuiI-8BTJQwwmT3iI5DP8w2-lZj8QX7hDGuuwIUiKmShpIwPTG_Vuptj-1AuV-np22xmHojdH8nGCeIrG1KZIv9BhYw57Go72r8kW7ypkZO9mW_ZRaeBIPcO9IOFVY6iM7tLzzcpdMn4dUa-lLUFJFGFlVvE8BFw63dQD0DNsV3VN-35z4A7tHOv8DW0MslzZ9WJIPY_YuCLRG_wpTrJfpI_a1n4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1941cb0cd1.mp4?token=umCLxaCTzo9em-U_ZbjENBD5bOjbG866nHVPQ1XTEULT3hdjnTw-ir6OVGqyUb_DDyxebyEN90zYei8DhP-08WffMA2pf64Mkcd1Kwz8xmA6rTFiQrLoaxlu8yuiI-8BTJQwwmT3iI5DP8w2-lZj8QX7hDGuuwIUiKmShpIwPTG_Vuptj-1AuV-np22xmHojdH8nGCeIrG1KZIv9BhYw57Go72r8kW7ypkZO9mW_ZRaeBIPcO9IOFVY6iM7tLzzcpdMn4dUa-lLUFJFGFlVvE8BFw63dQD0DNsV3VN-35z4A7tHOv8DW0MslzZ9WJIPY_YuCLRG_wpTrJfpI_a1n4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر بیژن مرتضوی: بازگشت بیژن مرتضوی به ایران صحت ندارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693677" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKrPVmtckgI80he5SdW_YQqIUfBa6U5B46Ga1SlHTihIJ-JeXjTeF4SZfl6cBQOYgYPl8ws3fkyZkiv7fMUu7ihzg0iqyaJKcGfqNnpR7pdNBYk_I-38NwOspjMVvEydwBJWNnOwclZm3_sGqnnFcujrHaIAAMtw9UpGkl4YWZ2bRHYQL7gscc7X44vYooV9soO9JUe2quKlTUOW9JoDVC__XlR65AbFRFHSgwEf77B9_CzBQ9at42SzjUWaKoLVddhEH3MGIkbJ770iXMy3TY2Vb6aYTsnDAE6FB_r8OTk8FnAB4786KPDiuoCNo57fSMDVnUWawOSDBQc-8BKehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل ادعا کرد:دیدار نتانیاهو با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/693676" target="_blank">📅 14:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
کسانی که در لبنان چشم امید به وعده‌های دروغین سلطه‌گران دوخته‌اند در اوّلین تورّق صفحات تاریخ، مدفون خواهند شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/693675" target="_blank">📅 14:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
کشورمان اینک به روزهایی رسیده که سلطه‌گران متجاوز در مقابل حملات رزمندگان اسلام، دست التماس به تَرک جنگ برمی‌دارند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/693674" target="_blank">📅 14:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
کشورمان اینک به روزهایی رسیده که سلطه‌گران متجاوز در مقابل حملات رزمندگان اسلام، دست التماس به تَرک جنگ برمی‌دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/693673" target="_blank">📅 14:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693671">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رهبر انقلاب: روزهایی بود که سلطه‌گران با عملیات روانی و ایجاد فضای اِرعاب، خیابان‌های پایتخت را خلوت ساخته و کودتایی علیه استقلال‌جویی این ملّت به‌ راه انداختند و پس از آن ۲۵ سال ثروت‌های این مملکت را غارت کردند؛ ولی این روزها هفت ماه است هموطنان ما میادین…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/693671" target="_blank">📅 14:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693670">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رهبر انقلاب: روزهایی بود که سلطه‌گران با عملیات روانی و ایجاد فضای اِرعاب، خیابان‌های پایتخت را خلوت ساخته و کودتایی علیه استقلال‌جویی این ملّت به‌ راه انداختند و پس از آن ۲۵ سال ثروت‌های این مملکت را غارت کردند؛ ولی این روزها هفت ماه است هموطنان ما میادین…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/693670" target="_blank">📅 14:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693669">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
آخرین درخواست رسایی پیش از اجرای حکم: به حقوق نیروهای مسلح فکر کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/693669" target="_blank">📅 14:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693668">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUT9Qg1YIVqFcvT1G7sJKD4z763xtj0sUM_rxl5ALh_kyEfWLDg4nNL_J-3OwwnMTIn2ffHmB-JvExqpIpji5AXk-vsq7FpRgkqh4bpY2744wWeSqlLbIEDaCSUrZb2ix_1Z95GMC47EnZi8wSvjPzCthuDUYLguN8yi9qetMUCDWSjKjTRKa6DmxGO48pbiygh6D3okEn4tDKLVVkuNfbdzdgQFIybXglKFhyvdb-tKkJFwAq2_k2t0rqQSRE7ywZHasDuTLJlXwI00SLMpSYx6Gj8kawchfvQlLBAO1rF6iP-3T5VuJ6LOJJp1fS8QQeRP1RlH4zHpUOR3YQsPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
پرداخت ۲٫۱ همت تسهیلات قرض‌الحسنه در بانک اقتصادنوین
🔹
میزان تسهیلات قرض‌الحسنه پرداختی بانک اقتصادنوین در نیمه نخست امسال از مرز ۲۱ هزار میلیارد ریال عبور کرد.
🔻
اطلاعات بیشتر:
🔗
https://enbank.ir/s/mfaba6I
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693668" target="_blank">📅 14:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693667">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
رهبر انقلاب: روزهایی بود که عنصر دلیری مردمان این مرز و بوم با مردانش شناخته می‌شد؛ امّا اینک بانوان در بعضی از عرصه‌های حضور دلیرانه، از مردان سبقت می‌گیرند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693667" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693666">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4af3cce0a.mp4?token=QwSBrHcgBTVaW9w2MgMEQAPfqTySRwYms1_d03BKIpNLVTTCIrW5OA1KZposVbEPoUjj-3IgVv7gr_NlNSd62aF4O_12rjZMIopGN1oNaN-rAYGOWV2rtLfKEjohuVUi33SvD9C5mCfFu7u1lc7w6IVoFhOcg-k8_cv1tbVNzMSx5TitZPDV8ejFp4eSWchUoV0bDh6GFDEdfrIYEjlOL1Xr-xmPYFvDEkqNQQSP4TYn-bIi9XuYUD_tJwNvm3Jo93lnog-cl77p17k1RPwh_51S70Qmf_RXhjStRb9n0tsVqQFsV2i8xBW8XpU1cfF5Vgodt3dcEUk9cbi_FfgIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4af3cce0a.mp4?token=QwSBrHcgBTVaW9w2MgMEQAPfqTySRwYms1_d03BKIpNLVTTCIrW5OA1KZposVbEPoUjj-3IgVv7gr_NlNSd62aF4O_12rjZMIopGN1oNaN-rAYGOWV2rtLfKEjohuVUi33SvD9C5mCfFu7u1lc7w6IVoFhOcg-k8_cv1tbVNzMSx5TitZPDV8ejFp4eSWchUoV0bDh6GFDEdfrIYEjlOL1Xr-xmPYFvDEkqNQQSP4TYn-bIi9XuYUD_tJwNvm3Jo93lnog-cl77p17k1RPwh_51S70Qmf_RXhjStRb9n0tsVqQFsV2i8xBW8XpU1cfF5Vgodt3dcEUk9cbi_FfgIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل‌ارث تصاویر ماهواره‌ای غزه را به‌روزرسانی کرد؛ حالا می‌توان ابعاد گسترده ویرانی و خسارات این منطقه را مشاهده کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693666" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693664">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
در تاریخ شامات، پس از انبیا و اوصیا، مردی به عظمت سید حسن نصرالله سر برنیاورد
🔹
نصرت و فتح، همراهان دائمی او [امیر قهرمان عرب و نماد بزرگ جبهه مقاومت، شهید عالی‌قدر جناب سیّد حسن نصرالله] بودند و بی‌تردید در طول کلّ تاریخ شامات تا کنون، پس از انبیاء و اوصیاء…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/693664" target="_blank">📅 14:19 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
